import re
import json
import os
from pathlib import Path

def unwrap_latex_command(text, cmd, has_prefix_arg=False):
    result = []
    i = 0
    n = len(text)
    while i < n:
        if text[i:].startswith(cmd) and (i + len(cmd) == n or not text[i + len(cmd)].isalpha()):
            pos = i + len(cmd)
            while pos < n and text[pos].isspace(): pos += 1
            if pos < n and text[pos] == '[':
                b_count = 1
                pos += 1
                while pos < n and b_count > 0:
                    if text[pos] == '[': b_count += 1
                    elif text[pos] == ']': b_count -= 1
                    pos += 1
            if has_prefix_arg:
                while pos < n and text[pos].isspace(): pos += 1
                if pos < n and text[pos] == '{':
                    b_count = 1
                    pos += 1
                    while pos < n and b_count > 0:
                        if text[pos] == '{': b_count += 1
                        elif text[pos] == '}': b_count -= 1
                        pos += 1
            while pos < n and text[pos].isspace(): pos += 1
            if pos < n and text[pos] == '{':
                b_count = 1
                pos += 1
                start_content = pos
                while pos < n and b_count > 0:
                    if text[pos] == '{': b_count += 1
                    elif text[pos] == '}': b_count -= 1
                    pos += 1
                content = text[start_content:pos-1]
                result.append(content)
                i = pos
                continue
        result.append(text[i])
        i += 1
    return ''.join(result)

def clean_latex_text(text):
    if not text:
        return ""
    # Quitar \textcolor{...}{contenido} -> contenido
    text = unwrap_latex_command(text, r'\textcolor', has_prefix_arg=True)
    # Quitar \textbf{...}, \textit{...}, \emph{...}, \text{...}
    for cmd in [r'\textbf', r'\textit', r'\emph', r'\text']:
        text = unwrap_latex_command(text, cmd)
    # Escapar \% -> %
    text = text.replace(r'\%', '%')
    # Limpiar espacios múltiples y saltos de línea
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_latex_test(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Buscar sección de Test / Cuestionario / Autoevaluación / Preguntas
    section_match = re.search(r'\\section\*?\{([^}]*(?:Test|Cuestionario|Autoevaluaci[oó]n|Preguntas|Examen)[^}]*)\}', content, re.IGNORECASE)
    
    if not section_match:
        print(f"  [Info] No se encontró sección de test/cuestionario en {Path(file_path).name}")
        return []

    theme_title = section_match.group(1).strip()
    test_content = content[section_match.start():]

    # Encontrar el bloque principal enumerate de preguntas
    first_enum_idx = test_content.find(r'\begin{enumerate}')
    if first_enum_idx == -1:
        print(f"  [Info] No se encontró bloque enumerate en {Path(file_path).name}")
        return []

    # Cortar si hay otra sección posterior
    next_sec = re.search(r'\n\\section\*?\{', test_content[first_enum_idx:])
    if next_sec:
        test_block = test_content[first_enum_idx:first_enum_idx + next_sec.start()]
    else:
        test_block = test_content[first_enum_idx:]

    last_enum_idx = test_block.rfind(r'\end{enumerate}')
    if last_enum_idx == -1:
        return []

    inner_content = test_block[:last_enum_idx]
    # Quitar la apertura del enumerate exterior
    inner_content = re.sub(r'^\\begin\{enumerate\}(?:\[.*?\])?', '', inner_content).strip()

    # Extraer preguntas: cada \item seguido del texto de la pregunta, su bloque de opciones (\begin{enumerate}...\end{enumerate}) y posible nota (\nt{...})
    question_blocks = re.findall(
        r'\\item\s+(.*?)\\begin\{enumerate\}(?:\[.*?\])?(.*?)\\end\{enumerate\}(?:\s*\\nt\{((?:[^{}]|\{[^{}]*\})*)\})?',
        inner_content,
        re.DOTALL
    )

    questions = []
    for q_idx, (q_text_raw, options_raw, note_raw) in enumerate(question_blocks, 1):
        q_text = clean_latex_text(q_text_raw)
        
        opt_items = re.split(r'\\item\s+', options_raw.strip())
        opt_items = [o.strip() for o in opt_items if o.strip()]
        
        options = []
        correct_index = -1
        
        for o_idx, opt_text in enumerate(opt_items):
            is_correct = bool(re.search(r'\\textcolor\{[^}]+\}', opt_text))
            clean_opt = clean_latex_text(opt_text)
            options.append(clean_opt)
            
            if is_correct:
                correct_index = o_idx

        explanation = ""
        if note_raw and note_raw.strip():
            explanation = clean_latex_text(note_raw)
        elif correct_index >= 0 and correct_index < len(options):
            explanation = f"Respuesta correcta: {options[correct_index]}"

        if options:
            questions.append({
                "id": f"{Path(file_path).stem}_q{q_idx}",
                "theme": theme_title,
                "file": Path(file_path).name,
                "questionNumber": q_idx,
                "question": q_text,
                "options": options,
                "correctIndex": correct_index,
                "explanation": explanation
            })

    return questions

def parse_all_themes(capitulos_dir, app_dir):
    all_questions = []
    capitulos_path = Path(capitulos_dir)
    app_path = Path(app_dir)
    app_path.mkdir(parents=True, exist_ok=True)
    
    if not capitulos_path.exists():
        print(f"Directorio no encontrado: {capitulos_dir}")
        return

    tex_files = sorted(list(capitulos_path.glob("*.tex")))
    for tex_file in tex_files:
        print(f"Procesando {tex_file.name}...")
        qs = parse_latex_test(tex_file)
        print(f"  -> Encontradas {len(qs)} preguntas.")
        all_questions.extend(qs)

    # 1. Guardar preguntas.json
    json_file = app_path / "preguntas.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)

    # 2. Guardar preguntas_data.js para carga offline / file:// directa
    js_file = app_path / "preguntas_data.js"
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write("// Banco de preguntas auto-generado desde Capitulos/*.tex\n")
        f.write("window.EMBEDDED_QUESTIONS = ")
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
        f.write(";\n")
        
    print(f"\n¡Éxito! Total de {len(all_questions)} preguntas guardadas en:")
    print(f" - {json_file}")
    print(f" - {js_file}")

if __name__ == "__main__":
    base_dir = Path(r"f:\universidad\4º\Resis\Apuntes")
    capitulos = base_dir / "Capitulos"
    app_dir = base_dir / "test_app"
    parse_all_themes(capitulos, app_dir)
