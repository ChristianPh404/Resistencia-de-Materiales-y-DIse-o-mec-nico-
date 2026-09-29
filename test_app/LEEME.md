# ⚡ ResisTest - App de Repaso & Flashcards (RMDM)

Aplicación web interactiva para preparar el examen de **Resistencia de Materiales y Diseño Mecánico**, diseñada a partir de los tests de autoevaluación de los apuntes LaTeX.

---

## 🚀 Cómo abrir la aplicación

Tienes dos opciones muy sencillas:

1. **Opción directa (Doble clic)**:
   - Abre el archivo [`index.html`](file:///f:/universidad/4º/Resis/Apuntes/test_app/index.html) directamente en tu navegador (Chrome, Edge, Firefox, etc.).
   
2. **Opción servidor local (opcional)**:
   - En la terminal, dentro de la carpeta `Apuntes`, ejecuta:
     ```bash
     python -m http.server 8000
     ```
   - Abre en tu navegador `http://localhost:8000/test_app/`.

---

## ✨ Características y Modos de Estudio

1. **📝 Modo Cuestionario**:
   - Preguntas tipo test interactivas con feedback inmediato (acierto/fallo).
   - Opciones para aleatorizar preguntas y el orden de las respuestas (A, B, C).
   - Barra de progreso y marcadores en tiempo real.
   - Atajos de teclado: Pulsa `1`, `2`, `3` para responder y `Enter` o `Flecha Derecha` para avanzar.

2. **🎴 Modo Flashcards 3D**:
   - Tarjetas interactivas con giro 3D.
   - Pulsa en la tarjeta o presiona la barra espaciadora `[Espacio]` para voltear y ver la solución.
   - Botones *"Me la sé"* / *"Necesito repasar"* para reforzar puntos débiles.

3. **⏱️ Modo Examen**:
   - Simulacro completo con cronómetro y evaluación final.

4. **🔄 Modo Repaso de Fallos**:
   - Permite filtrar automáticamente únicamente aquellas preguntas en las que hayas dudado o fallado.

5. **📐 Renderizado Matemático**:
   - Compatible con fórmulas y notaciones LaTeX gracias a KaTeX.

6. **🌙 Modo Oscuro / Claro**:
   - Botón superior para alternar tema según tu preferencia.

---

## ➕ Cómo añadir nuevos temas (Tema 2, Tema 3, etc.)

El sistema está preparado para detectar automáticamente todos los temas que añadas a la carpeta `Capitulos/`:

1. Crea tu archivo en LaTeX (por ejemplo `Capitulos/Tema2.tex`) siguiendo la misma estructura habitual de preguntas y la respuesta correcta marcada con `\textcolor{red!85!black}{...}` dentro del `\section{Test de Autoevaluación...}`.
2. Ejecuta el script extractor en la terminal:
   ```bash
   python extraer_preguntas.py
   ```
3. ¡Listo! Al recargar la aplicación verás el nuevo tema en el menú desplegable.

> **Importación al vuelo desde la App:** También puedes pulsar el botón 📥 en la barra superior de la web y arrastrar directamente el archivo `.tex` o pegar el texto para cargarlo al instante sin usar la terminal.
