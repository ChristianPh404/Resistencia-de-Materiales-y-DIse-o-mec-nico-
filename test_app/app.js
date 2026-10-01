/**
 * App de Autoevaluación y Flashcards - Resistencia de Materiales y Diseño Mecánico
 */

// Estado global de la aplicación
const state = {
  allQuestions: [],
  filteredQuestions: [],
  currentIndex: 0,
  currentMode: 'quiz', // 'quiz' | 'flashcards' | 'exam'
  userAnswers: {},     // { questionId: selectedIndex }
  failedQuestionIds: new Set(),
  stats: {
    correct: 0,
    incorrect: 0,
    totalAnswered: 0
  },
  examTimeRemaining: 0,
  examTimerInterval: null,
  config: {
    selectedTheme: 'all',
    shuffleQuestions: true,
    shuffleOptions: true,
    onlyFailed: false,
    examDurationMinutes: 20,
    examQuestionCount: 20
  }
};

// Elementos DOM
const elements = {
  themeSelect: document.getElementById('themeSelect'),
  modeQuizBtn: document.getElementById('modeQuizBtn'),
  modeFlashcardsBtn: document.getElementById('modeFlashcardsBtn'),
  modeExamBtn: document.getElementById('modeExamBtn'),
  startBtn: document.getElementById('startBtn'),
  shuffleQuestionsCheck: document.getElementById('shuffleQuestions'),
  shuffleOptionsCheck: document.getElementById('shuffleOptions'),
  onlyFailedCheck: document.getElementById('onlyFailed'),
  
  // Vistas
  setupView: document.getElementById('setupView'),
  quizView: document.getElementById('quizView'),
  flashcardView: document.getElementById('flashcardView'),
  resultsView: document.getElementById('resultsView'),
  
  // Quiz
  questionThemeTag: document.getElementById('questionThemeTag'),
  questionText: document.getElementById('questionText'),
  optionsList: document.getElementById('optionsList'),
  feedbackBox: document.getElementById('feedbackBox'),
  feedbackTitle: document.getElementById('feedbackTitle'),
  feedbackDesc: document.getElementById('feedbackDesc'),
  currentQuestionNum: document.getElementById('currentQuestionNum'),
  totalQuestionsNum: document.getElementById('totalQuestionsNum'),
  progressBarFill: document.getElementById('progressBarFill'),
  scoreCorrect: document.getElementById('scoreCorrect'),
  scoreIncorrect: document.getElementById('scoreIncorrect'),
  nextBtn: document.getElementById('nextBtn'),
  prevBtn: document.getElementById('prevBtn'),
  quitQuizBtn: document.getElementById('quitQuizBtn'),
  
  // Flashcards
  flashcard: document.getElementById('flashcard'),
  cardThemeTag: document.getElementById('cardThemeTag'),
  cardQuestionText: document.getElementById('cardQuestionText'),
  cardAnswerText: document.getElementById('cardAnswerText'),
  cardCounter: document.getElementById('cardCounter'),
  cardProgressFill: document.getElementById('cardProgressFill'),
  cardPrevBtn: document.getElementById('cardPrevBtn'),
  cardNextBtn: document.getElementById('cardNextBtn'),
  cardFailBtn: document.getElementById('cardFailBtn'),
  cardPassBtn: document.getElementById('cardPassBtn'),
  quitCardsBtn: document.getElementById('quitCardsBtn'),
  
  // Resultados
  finalScore: document.getElementById('finalScore'),
  finalScoreCircle: document.getElementById('finalScoreCircle'),
  statTotalAnswered: document.getElementById('statTotalAnswered'),
  statCorrectCount: document.getElementById('statCorrectCount'),
  statIncorrectCount: document.getElementById('statIncorrectCount'),
  statAccuracy: document.getElementById('statAccuracy'),
  restartBtn: document.getElementById('restartBtn'),
  reviewFailedBtn: document.getElementById('reviewFailedBtn'),
  backToSetupBtn: document.getElementById('backToSetupBtn'),

  // Modal import
  importModal: document.getElementById('importModal'),
  openImportBtn: document.getElementById('openImportBtn'),
  closeImportBtn: document.getElementById('closeImportBtn'),
  texTextInput: document.getElementById('texTextInput'),
  parseTexBtn: document.getElementById('parseTexBtn'),
  fileInput: document.getElementById('fileInput'),
  dropZone: document.getElementById('dropZone'),

  // Tema
  themeToggleBtn: document.getElementById('themeToggleBtn')
};

// Cargar estado inicial
document.addEventListener('DOMContentLoaded', async () => {
  loadSavedTheme();
  setupEventListeners();
  await loadDefaultQuestions();
  updateSetupStats();
});

// Cargar preguntas iniciales desde preguntas.json con fallback inmediato
async function loadDefaultQuestions() {
  // 1. Probar datos embebidos si están presentes
  if (window.EMBEDDED_QUESTIONS && Array.isArray(window.EMBEDDED_QUESTIONS) && window.EMBEDDED_QUESTIONS.length > 0) {
    state.allQuestions = [...window.EMBEDDED_QUESTIONS];
    populateThemeSelect();
    updateSetupStats();
  }

  // 2. Intentar refrescar desde preguntas.json por si hubo cambios o servidor local
  try {
    const res = await fetch('preguntas.json');
    if (res.ok) {
      const data = await res.json();
      state.allQuestions = data;
      populateThemeSelect();
      updateSetupStats();
      console.log(`Cargadas ${data.length} preguntas desde JSON.`);
    }
  } catch (err) {
    console.log('Usando banco de preguntas local precargado.');
  }
}

// Poblar selector de temas
function populateThemeSelect() {
  const themes = new Set(state.allQuestions.map(q => q.theme));
  elements.themeSelect.innerHTML = '<option value="all">🌟 Todos los Temas</option>';
  
  themes.forEach(theme => {
    const option = document.createElement('option');
    option.value = theme;
    option.textContent = theme;
    elements.themeSelect.appendChild(option);
  });
}

function updateSetupStats() {
  const total = state.allQuestions.length;
  const failedCount = state.failedQuestionIds.size;
  document.getElementById('totalQuestionsStat').textContent = total;
  document.getElementById('failedQuestionsStat').textContent = failedCount;
  
  elements.onlyFailedCheck.disabled = failedCount === 0;
  if (failedCount === 0) elements.onlyFailedCheck.checked = false;
}

// Configuración de Event Listeners
function setupEventListeners() {
  // Cambio de modo desde el Header
  elements.modeQuizBtn.addEventListener('click', () => switchAppMode('quiz'));
  elements.modeFlashcardsBtn.addEventListener('click', () => switchAppMode('flashcards'));
  elements.modeExamBtn.addEventListener('click', () => switchAppMode('exam'));

  // Inicio de sesión
  elements.startBtn.addEventListener('click', startSession);

  // Botones de Quiz
  elements.nextBtn.addEventListener('click', nextQuestion);
  elements.prevBtn.addEventListener('click', prevQuestion);
  elements.quitQuizBtn.addEventListener('click', returnToSetup);

  // Botones de Flashcards
  elements.flashcard.addEventListener('click', () => {
    elements.flashcard.classList.toggle('is-flipped');
  });
  elements.cardNextBtn.addEventListener('click', nextFlashcard);
  elements.cardPrevBtn.addEventListener('click', prevFlashcard);
  elements.cardFailBtn.addEventListener('click', () => handleCardAnswer(false));
  elements.cardPassBtn.addEventListener('click', () => handleCardAnswer(true));
  elements.quitCardsBtn.addEventListener('click', returnToSetup);

  // Resultados
  elements.restartBtn.addEventListener('click', startSession);
  elements.reviewFailedBtn.addEventListener('click', () => {
    state.config.onlyFailed = true;
    elements.onlyFailedCheck.checked = true;
    startSession();
  });
  elements.backToSetupBtn.addEventListener('click', returnToSetup);

  // Importación
  elements.openImportBtn.addEventListener('click', () => elements.importModal.classList.add('show'));
  elements.closeImportBtn.addEventListener('click', () => elements.importModal.classList.remove('show'));
  elements.parseTexBtn.addEventListener('click', handleParseTexInput);

  // Drag & drop JSON/TEX
  elements.dropZone.addEventListener('click', () => elements.fileInput.click());
  elements.fileInput.addEventListener('change', handleFileUpload);
  elements.dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    elements.dropZone.classList.add('dragover');
  });
  elements.dropZone.addEventListener('dragleave', () => elements.dropZone.classList.remove('dragover'));
  elements.dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    elements.dropZone.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
      processImportedFile(e.dataTransfer.files[0]);
    }
  });

  // Tema claro/oscuro
  elements.themeToggleBtn.addEventListener('click', toggleTheme);

  // Atajos de teclado
  window.addEventListener('keydown', handleKeyboardShortcuts);
}

function switchAppMode(mode) {
  state.currentMode = mode;
  elements.modeQuizBtn.classList.toggle('active', mode === 'quiz');
  elements.modeFlashcardsBtn.classList.toggle('active', mode === 'flashcards');
  elements.modeExamBtn.classList.toggle('active', mode === 'exam');

  const startLabel = mode === 'quiz' ? 'Comenzar Cuestionario' :
                     mode === 'flashcards' ? 'Comenzar Flashcards' : 'Iniciar Examen Simulado';
  elements.startBtn.innerHTML = `<span>🚀</span> ${startLabel}`;
}

// Iniciar sesión
function startSession() {
  if (state.allQuestions.length === 0) {
    alert('No hay preguntas cargadas. Por favor importa preguntas o revisa preguntas.json.');
    return;
  }

  // Filtrar preguntas
  const selectedTheme = elements.themeSelect.value;
  let pool = [...state.allQuestions];

  if (selectedTheme !== 'all') {
    pool = pool.filter(q => q.theme === selectedTheme);
  }

  if (elements.onlyFailedCheck.checked) {
    pool = pool.filter(q => state.failedQuestionIds.has(q.id));
    if (pool.length === 0) {
      alert('No hay preguntas falladas guardadas en este filtro.');
      return;
    }
  }

  // Preparar preguntas con opciones procesadas (y barajadas si aplica)
  state.filteredQuestions = pool.map(q => {
    let opts = q.options.map((optText, origIdx) => ({
      text: optText,
      isCorrect: origIdx === q.correctIndex
    }));

    if (elements.shuffleOptionsCheck.checked) {
      opts = shuffleArray(opts);
    }

    return {
      ...q,
      processedOptions: opts
    };
  });

  if (elements.shuffleQuestionsCheck.checked) {
    state.filteredQuestions = shuffleArray(state.filteredQuestions);
  }

  state.currentIndex = 0;
  state.userAnswers = {};
  state.stats = { correct: 0, incorrect: 0, totalAnswered: 0 };

  // Ocultar todas las vistas y mostrar la correspondiente
  elements.setupView.style.display = 'none';
  elements.resultsView.style.display = 'none';

  if (state.currentMode === 'flashcards') {
    elements.quizView.style.display = 'none';
    elements.flashcardView.style.display = 'block';
    renderCurrentFlashcard();
  } else {
    elements.flashcardView.style.display = 'none';
    elements.quizView.style.display = 'block';
    renderCurrentQuestion();
  }
}

// Renderizar pregunta en modo Cuestionario / Examen
function renderCurrentQuestion() {
  const q = state.filteredQuestions[state.currentIndex];
  if (!q) return;

  // Header & Tags
  elements.questionThemeTag.textContent = `${q.theme} • Pregunta ${state.currentIndex + 1}/${state.filteredQuestions.length}`;
  elements.questionText.innerHTML = renderMath(q.question);

  // Progreso
  elements.currentQuestionNum.textContent = state.currentIndex + 1;
  elements.totalQuestionsNum.textContent = state.filteredQuestions.length;
  const pct = ((state.currentIndex + 1) / state.filteredQuestions.length) * 100;
  elements.progressBarFill.style.width = `${pct}%`;

  // Marcadores
  elements.scoreCorrect.textContent = `✓ ${state.stats.correct}`;
  elements.scoreIncorrect.textContent = `✗ ${state.stats.incorrect}`;

  // Opciones
  elements.optionsList.innerHTML = '';
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const hasAnswered = state.userAnswers.hasOwnProperty(q.id);

  q.processedOptions.forEach((opt, idx) => {
    const btn = document.createElement('button');
    btn.className = 'option-btn';
    btn.innerHTML = `
      <span class="option-letter">${letters[idx] || idx + 1}</span>
      <span class="option-text">${renderMath(opt.text)}</span>
    `;

    if (hasAnswered) {
      btn.disabled = true;
      const userSelected = state.userAnswers[q.id] === idx;
      if (opt.isCorrect) {
        btn.classList.add('selected-correct');
      } else if (userSelected && !opt.isCorrect) {
        btn.classList.add('selected-incorrect');
      }
    } else {
      btn.addEventListener('click', () => handleSelectOption(idx));
    }

    elements.optionsList.appendChild(btn);
  });

  // Feedback Box
  if (hasAnswered) {
    const userSelectedIdx = state.userAnswers[q.id];
    const isCorrect = q.processedOptions[userSelectedIdx]?.isCorrect;

    elements.feedbackBox.style.display = 'block';
    elements.feedbackBox.className = `feedback-box ${isCorrect ? 'correct' : 'incorrect'}`;
    elements.feedbackTitle.innerHTML = isCorrect ? '🎉 ¡Correcto!' : '❌ Incorrecto';
    
    const correctOpt = q.processedOptions.find(o => o.isCorrect);
    let descHtml = isCorrect 
      ? '<div>¡Muy bien! Has acertado esta pregunta.</div>' 
      : `<div><strong>Solución:</strong> ${correctOpt ? renderMath(correctOpt.text) : ''}</div>`;
    
    if (q.explanation && q.explanation.trim()) {
      descHtml += `<div class="feedback-explanation">💡 <strong>Explicación:</strong> ${renderMath(q.explanation)}</div>`;
    }

    elements.feedbackDesc.innerHTML = descHtml;
  } else {
    elements.feedbackBox.style.display = 'none';
  }

  // Controles de navegación
  elements.prevBtn.style.visibility = state.currentIndex > 0 ? 'visible' : 'hidden';
  elements.nextBtn.textContent = state.currentIndex === state.filteredQuestions.length - 1 ? 'Finalizar Test 🏁' : 'Siguiente ❯';
}

function handleSelectOption(selectedIdx) {
  const q = state.filteredQuestions[state.currentIndex];
  if (state.userAnswers.hasOwnProperty(q.id)) return;

  state.userAnswers[q.id] = selectedIdx;
  const isCorrect = q.processedOptions[selectedIdx]?.isCorrect;

  if (isCorrect) {
    state.stats.correct++;
    state.failedQuestionIds.delete(q.id);
  } else {
    state.stats.incorrect++;
    state.failedQuestionIds.add(q.id);
  }
  state.stats.totalAnswered++;

  renderCurrentQuestion();
}

function nextQuestion() {
  if (state.currentIndex < state.filteredQuestions.length - 1) {
    state.currentIndex++;
    renderCurrentQuestion();
  } else {
    finishSession();
  }
}

function prevQuestion() {
  if (state.currentIndex > 0) {
    state.currentIndex--;
    renderCurrentQuestion();
  }
}

// MODO FLASHCARDS
function renderCurrentFlashcard() {
  const q = state.filteredQuestions[state.currentIndex];
  if (!q) return;

  elements.flashcard.classList.remove('is-flipped');

  elements.cardThemeTag.textContent = `${q.theme} • Tarjeta ${state.currentIndex + 1}/${state.filteredQuestions.length}`;
  elements.cardQuestionText.innerHTML = renderMath(q.question);
  
  // Buscar opción correcta
  const correctOpt = q.options[q.correctIndex] || (q.processedOptions ? q.processedOptions.find(o => o.isCorrect)?.text : 'Sin respuesta');
  let cardHtml = `<div class="flashcard-answer-main">${renderMath(correctOpt)}</div>`;
  if (q.explanation && q.explanation.trim()) {
    cardHtml += `<div class="flashcard-answer-explanation">💡 <strong>Detalle:</strong> ${renderMath(q.explanation)}</div>`;
  }
  elements.cardAnswerText.innerHTML = cardHtml;

  elements.cardCounter.textContent = `${state.currentIndex + 1} / ${state.filteredQuestions.length}`;
  const pct = ((state.currentIndex + 1) / state.filteredQuestions.length) * 100;
  elements.cardProgressFill.style.width = `${pct}%`;

  elements.cardPrevBtn.style.visibility = state.currentIndex > 0 ? 'visible' : 'hidden';
}

function handleCardAnswer(isKnown) {
  const q = state.filteredQuestions[state.currentIndex];
  if (!isKnown) {
    state.failedQuestionIds.add(q.id);
    state.stats.incorrect++;
  } else {
    state.failedQuestionIds.delete(q.id);
    state.stats.correct++;
  }
  state.stats.totalAnswered++;

  nextFlashcard();
}

function nextFlashcard() {
  if (state.currentIndex < state.filteredQuestions.length - 1) {
    state.currentIndex++;
    renderCurrentFlashcard();
  } else {
    finishSession();
  }
}

function prevFlashcard() {
  if (state.currentIndex > 0) {
    state.currentIndex--;
    renderCurrentFlashcard();
  }
}

// Finalizar Sesión y Mostrar Resultados
function finishSession() {
  elements.quizView.style.display = 'none';
  elements.flashcardView.style.display = 'none';
  elements.resultsView.style.display = 'block';

  const total = state.filteredQuestions.length;
  const correct = state.stats.correct;
  const incorrect = state.stats.incorrect;
  const unanswered = total - (correct + incorrect);
  
  // Nota sobre 10 (restando o no según configuración)
  const scoreOutOfTen = total > 0 ? Math.max(0, ((correct / total) * 10)).toFixed(1) : 0;
  const scorePct = total > 0 ? Math.round((correct / total) * 100) : 0;

  elements.finalScore.textContent = scoreOutOfTen;
  elements.finalScoreCircle.style.setProperty('--score-pct', scorePct);

  elements.statTotalAnswered.textContent = `${correct + incorrect}/${total}`;
  elements.statCorrectCount.textContent = correct;
  elements.statIncorrectCount.textContent = incorrect;
  elements.statAccuracy.textContent = `${scorePct}%`;

  elements.reviewFailedBtn.style.display = state.failedQuestionIds.size > 0 ? 'inline-flex' : 'none';
  updateSetupStats();
}

function returnToSetup() {
  elements.quizView.style.display = 'none';
  elements.flashcardView.style.display = 'none';
  elements.resultsView.style.display = 'none';
  elements.setupView.style.display = 'block';
  updateSetupStats();
}

// Parser de LaTeX al vuelo desde el navegador
function parseLatexContent(text, filename = 'Importado.tex') {
  const unwrapMacro = (str, cmd, hasPrefixArg = false) => {
    let result = '';
    let i = 0;
    const n = str.length;
    while (i < n) {
      if (str.substring(i).startsWith(cmd) && (i + cmd.length === n || !/[a-zA-Z]/.test(str[i + cmd.length]))) {
        let pos = i + cmd.length;
        while (pos < n && /\s/.test(str[pos])) pos++;
        if (pos < n && str[pos] === '[') {
          let bCount = 1;
          pos++;
          while (pos < n && bCount > 0) {
            if (str[pos] === '[') bCount++;
            else if (str[pos] === ']') bCount--;
            pos++;
          }
        }
        if (hasPrefixArg) {
          while (pos < n && /\s/.test(str[pos])) pos++;
          if (pos < n && str[pos] === '{') {
            let bCount = 1;
            pos++;
            while (pos < n && bCount > 0) {
              if (str[pos] === '{') bCount++;
              else if (str[pos] === '}') bCount--;
              pos++;
            }
          }
        }
        while (pos < n && /\s/.test(str[pos])) pos++;
        if (pos < n && str[pos] === '{') {
          let bCount = 1;
          pos++;
          const start = pos;
          while (pos < n && bCount > 0) {
            if (str[pos] === '{') bCount++;
            else if (str[pos] === '}') bCount--;
            pos++;
          }
          result += str.substring(start, pos - 1);
          i = pos;
          continue;
        }
      }
      result += str[i];
      i++;
    }
    return result;
  };

  const cleanLatex = (str) => {
    if (!str) return '';
    let s = unwrapMacro(str, '\\textcolor', true);
    for (const cmd of ['\\textbf', '\\textit', '\\emph', '\\text']) {
      s = unwrapMacro(s, cmd);
    }
    return s.replace(/\\%/g, '%').replace(/\s+/g, ' ').trim();
  };

  const sectionMatch = text.match(/\\section\*?\{([^}]*(?:Test|Cuestionario|Autoevaluaci[oó]n|Preguntas|Examen)[^}]*)\}/i);
  const themeTitle = sectionMatch ? sectionMatch[1].trim() : filename.replace(/\.tex$/i, '');
  const testContent = sectionMatch ? text.substring(sectionMatch.index) : text;
  
  const firstEnumIdx = testContent.indexOf('\\begin{enumerate}');
  if (firstEnumIdx === -1) return [];

  const nextSecMatch = testContent.substring(firstEnumIdx).match(/\n\\section\*?\{/);
  const testBlock = nextSecMatch ? testContent.substring(firstEnumIdx, firstEnumIdx + nextSecMatch.index) : testContent.substring(firstEnumIdx);
  const lastEnumIdx = testBlock.lastIndexOf('\\end{enumerate}');
  if (lastEnumIdx === -1) return [];

  let inner = testBlock.substring(0, lastEnumIdx).replace(/^\\begin\{enumerate\}(?:\[.*?\])?/, '').trim();
  const questionRegex = /\\item\s+(.*?)\\begin\{enumerate\}(?:\[.*?\])?(.*?)\\end\{enumerate\}(?:\s*\\nt\{((?:[^{}]|\{[^{}]*\})*)\})?/gs;
  
  let match;
  const questions = [];
  let qIdx = 1;

  while ((match = questionRegex.exec(inner)) !== null) {
    const qText = cleanLatex(match[1]);
    const optionsRaw = match[2];
    const noteRaw = match[3];

    const optItems = optionsRaw.split(/\\item\s+/).filter(o => o.trim());
    const options = [];
    let correctIndex = -1;

    optItems.forEach((optStr, idx) => {
      const isCorrect = /\\textcolor\{[^}]+\}/.test(optStr);
      options.push(cleanLatex(optStr));
      if (isCorrect) correctIndex = idx;
    });

    let explanation = '';
    if (noteRaw && noteRaw.trim()) {
      explanation = cleanLatex(noteRaw);
    } else if (correctIndex >= 0 && correctIndex < options.length) {
      explanation = `Respuesta correcta: ${options[correctIndex]}`;
    }

    if (options.length > 0) {
      questions.push({
        id: `${filename.replace(/\.tex$/i, '')}_q${qIdx}`,
        theme: themeTitle,
        file: filename,
        questionNumber: qIdx,
        question: qText,
        options: options,
        correctIndex: correctIndex,
        explanation: explanation
      });
      qIdx++;
    }
  }

  return questions;
}

function handleParseTexInput() {
  const content = elements.texTextInput.value.trim();
  if (!content) {
    alert('Por favor pega el contenido LaTeX.');
    return;
  }

  const parsed = parseLatexContent(content);
  if (parsed.length === 0) {
    alert('No se encontraron preguntas de test con el formato adecuado en el texto proporcionado.');
    return;
  }

  mergeNewQuestions(parsed);
  elements.texTextInput.value = '';
  elements.importModal.classList.remove('show');
  alert(`¡Se han importado ${parsed.length} preguntas correctamente!`);
}

function processImportedFile(file) {
  const reader = new FileReader();
  reader.onload = (e) => {
    const content = e.target.result;
    if (file.name.endsWith('.json')) {
      try {
        const json = JSON.parse(content);
        mergeNewQuestions(Array.isArray(json) ? json : [json]);
        alert(`¡Se han importado ${json.length} preguntas desde JSON!`);
        elements.importModal.classList.remove('show');
      } catch (err) {
        alert('Error al leer el archivo JSON.');
      }
    } else if (file.name.endsWith('.tex')) {
      const parsed = parseLatexContent(content, file.name);
      mergeNewQuestions(parsed);
      alert(`¡Se han importado ${parsed.length} preguntas desde ${file.name}!`);
      elements.importModal.classList.remove('show');
    }
  };
  reader.readAsText(file);
}

function handleFileUpload(e) {
  if (e.target.files.length) {
    processImportedFile(e.target.files[0]);
  }
}

function mergeNewQuestions(newQuestions) {
  // Eliminar duplicados por ID
  const map = new Map();
  state.allQuestions.forEach(q => map.set(q.id, q));
  newQuestions.forEach(q => map.set(q.id, q));
  
  state.allQuestions = Array.from(map.values());
  populateThemeSelect();
  updateSetupStats();
}

// Utilidades
function shuffleArray(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Renderizador KaTeX para fórmulas matemáticas ($...$, $$...$$, \(...\), \[...\])
function renderMath(text) {
  if (!text) return '';

  // 1. Si KaTeX está disponible
  if (typeof window.katex !== 'undefined' && typeof window.katex.renderToString === 'function') {
    let res = text;

    // Fórmulas display $$...$$ o \[...\]
    res = res.replace(/\$\$([\s\S]+?)\$\$/g, (_, math) => {
      try {
        return katex.renderToString(math.trim(), { throwOnError: false, displayMode: true });
      } catch (e) {
        return math;
      }
    });

    res = res.replace(/\\\[([\s\S]+?)\\\]/g, (_, math) => {
      try {
        return katex.renderToString(math.trim(), { throwOnError: false, displayMode: true });
      } catch (e) {
        return math;
      }
    });

    // Fórmulas inline $...$ o \(...\)
    res = res.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
      try {
        return katex.renderToString(math.trim(), { throwOnError: false, displayMode: false });
      } catch (e) {
        return math;
      }
    });

    res = res.replace(/\\\((.+?)\\\)/g, (_, math) => {
      try {
        return katex.renderToString(math.trim(), { throwOnError: false, displayMode: false });
      } catch (e) {
        return math;
      }
    });

    return res;
  }

  // 2. Fallback de renderizado en caso de no disponer de KaTeX
  return fallbackRenderMath(text);
}

// Fallback ligero para símbolos y superíndices si falla la carga del CDN
function fallbackRenderMath(text) {
  return text.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    let m = math
      .replace(/\\longrightarrow|\\rightarrow/g, ' → ')
      .replace(/\\leftarrow/g, ' ← ')
      .replace(/\\pm/g, ' ± ')
      .replace(/\\times/g, ' × ')
      .replace(/\\cdot/g, ' · ')
      .replace(/\\leq/g, ' ≤ ')
      .replace(/\\geq/g, ' ≥ ')
      .replace(/\\approx/g, ' ≈ ')
      .replace(/\\neq/g, ' ≠ ')
      .replace(/\\sigma/g, 'σ')
      .replace(/\\tau/g, 'τ')
      .replace(/\\alpha/g, 'α')
      .replace(/\\beta/g, 'β')
      .replace(/\\gamma/g, 'γ')
      .replace(/\\delta/g, 'δ')
      .replace(/\\varepsilon|\\epsilon/g, 'ε')
      .replace(/\\mu/g, 'μ')
      .replace(/\\nu/g, 'ν')
      .replace(/\\pi/g, 'π')
      .replace(/\\text\{([^}]+)\}/g, '$1')
      .replace(/\^([0-9\+\-]+)/g, '<sup>$1</sup>')
      .replace(/\^\{([^}]+)\}/g, '<sup>$1</sup>')
      .replace(/_([0-9a-zA-Z\+\-]+)/g, '<sub>$1</sub>')
      .replace(/_\{([^}]+)\}/g, '<sub>$1</sub>');
    return `<span class="math-fallback">${m}</span>`;
  });
}

// Atajos de teclado
function handleKeyboardShortcuts(e) {
  if (elements.importModal.classList.contains('show')) return;

  if (elements.quizView.style.display === 'block') {
    if (['1', '2', '3', '4', '5'].includes(e.key)) {
      const idx = parseInt(e.key) - 1;
      const btns = elements.optionsList.querySelectorAll('.option-btn');
      if (btns[idx] && !btns[idx].disabled) btns[idx].click();
    } else if (e.key === 'ArrowRight' || e.key === 'Enter') {
      nextQuestion();
    } else if (e.key === 'ArrowLeft') {
      prevQuestion();
    }
  } else if (elements.flashcardView.style.display === 'block') {
    if (e.key === ' ' || e.code === 'Space') {
      e.preventDefault();
      elements.flashcard.classList.toggle('is-flipped');
    } else if (e.key === 'ArrowRight' || e.key === '1') {
      handleCardAnswer(true);
    } else if (e.key === 'ArrowLeft' || e.key === '2') {
      handleCardAnswer(false);
    }
  }
}

// Tema Claro / Oscuro
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const target = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', target);
  localStorage.setItem('app_theme', target);
  elements.themeToggleBtn.textContent = target === 'dark' ? '🌙' : '☀️';
}

function loadSavedTheme() {
  const saved = localStorage.getItem('app_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  elements.themeToggleBtn.textContent = saved === 'dark' ? '🌙' : '☀️';
}
