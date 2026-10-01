import re
import json
import os
from pathlib import Path

def clean_latex_text(text):
    # Quitar \textcolor{...}{contenido} -> contenido
    text = re.sub(r'\\textcolor\{[^}]+\}\{(.*?)\}', r'\1', text, flags=re.DOTALL)
    # Quitar \textbf{...} -> **...**
    text = re.sub(r'\\textbf\{(.*?)\}', r'\1', text, flags=re.DOTALL)
    # Quitar \textit{...} -> *...*
    text = re.sub(r'\\textit\{(.*?)\}', r'\1', text, flags=re.DOTALL)
    # Quitar \text{...}
    text = re.sub(r'\\text\{(.*?)\}', r'\1', text, flags=re.DOTALL)
    # Escapar \% -> %
    text = text.replace(r'\%', '%')
    # Limpiar espacios múltiples y saltos de línea
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_latex_test(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    section_match = re.search(r'\\section\*?\{([^}]*Test[^}]*)\}', content, re.IGNORECASE)
    theme_title = section_match.group(1) if section_match else Path(file_path).stem
    
    if section_match:
        test_content = content[section_match.start():]
    else:
        test_content = content

    enum_match = re.search(r'\\begin\{enumerate\}(?:\[.*?\])?(.*?)\\end\{enumerate\}\s*(?:$|\\end\{document\}|\n\n(?=\\section))', test_content, re.DOTALL)
    
    if not enum_match:
        enums = list(re.finditer(r'\\begin\{enumerate\}(?:\[.*?\])?(.*?)\\end\{enumerate\}', test_content, re.DOTALL))
        if enums:
            enum_match = enums[-1]
            
    if not enum_match:
        print(f"No se encontró bloque enumerate en {file_path}")
        return []

    inner_content = enum_match.group(1)
    
    question_blocks = re.findall(
        r'\\item\s+(.*?)\\begin\{enumerate\}(?:\[.*?\])?(.*?)\\end\{enumerate\}',
        inner_content,
        re.DOTALL
    )

    questions = []
    for q_idx, (q_text_raw, options_raw) in enumerate(question_blocks, 1):
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

        if options:
            questions.append({
                "id": f"{Path(file_path).stem}_q{q_idx}",
                "theme": theme_title,
                "file": Path(file_path).name,
                "questionNumber": q_idx,
                "question": q_text,
                "options": options,
                "correctIndex": correct_index,
                "explanation": f"Respuesta correcta: {options[correct_index]}" if correct_index >= 0 and correct_index < len(options) else ""
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
