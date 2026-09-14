/**
 * CODEKARO — Real Multi-Page Educational MCQ Platform
 * Pure Vanilla JavaScript for Multi-Page Navigation, Validation, Scoring & Themes
 * 
 * IMPORTANT: Questions are NOT stored or generated here.
 * All MCQs live directly in their respective static HTML documents.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initLoginPage();
  initHomePage();
  initQuizPage();
  initResultPage();
});

/* --------------------------------------------------------------------------
   1. Theme Management (Light / Dark Mode across all pages)
   -------------------------------------------------------------------------- */
function initTheme() {
  const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
  const savedTheme = localStorage.getItem('codekaro_theme') || 'light';

  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcons(savedTheme);

  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('codekaro_theme', newTheme);
      updateThemeIcons(newTheme);
    });
  });
}

function updateThemeIcons(theme) {
  const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
  themeToggleBtns.forEach(btn => {
    btn.textContent = theme === 'dark' ? '☀️' : '🌙';
    btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  });
}

/* --------------------------------------------------------------------------
   2. Mobile Navigation Toggle
   -------------------------------------------------------------------------- */
function initMobileMenu() {
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');

  if (menuBtn && navLinks) {
    menuBtn.addEventListener('click', () => {
      navLinks.classList.toggle('open');
      const isOpen = navLinks.classList.contains('open');
      menuBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      menuBtn.textContent = isOpen ? '✕' : '☰';
    });

    document.addEventListener('click', (e) => {
      if (!navLinks.contains(e.target) && !menuBtn.contains(e.target) && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        menuBtn.textContent = '☰';
      }
    });
  }
}

/* --------------------------------------------------------------------------
   3. PAGE 1 — Index / Student Name Entry (index.html)
   -------------------------------------------------------------------------- */
const COUNTER_NAMESPACE = 'codekaro_practice_edu_global';
const COUNTER_KEY = 'students_count';
const COUNTER_API_BASE = `https://api.counterapi.dev/v1/${COUNTER_NAMESPACE}/${COUNTER_KEY}`;

async function incrementGlobalCounter() {
  if (sessionStorage.getItem('codekaro_student_counted')) return;

  try {
    const res = await fetch(`${COUNTER_API_BASE}/up`, { method: 'GET' });
    if (res.ok) {
      const data = await res.json();
      const count = typeof data.count === 'number' ? data.count : (data.value || 1);
      localStorage.setItem('codekaro_cached_student_count', count);
      sessionStorage.setItem('codekaro_student_counted', 'true');
    }
  } catch (err) {
    let cached = parseInt(localStorage.getItem('codekaro_cached_student_count') || '0', 10) + 1;
    localStorage.setItem('codekaro_cached_student_count', cached);
    sessionStorage.setItem('codekaro_student_counted', 'true');
  }
}

function initLoginPage() {
  const loginForm = document.getElementById('login-form');
  const nameInput = document.getElementById('student-name-input');
  const errorMsg = document.getElementById('name-error-msg');
  const enterBtn = document.getElementById('enter-btn');

  if (!loginForm || !nameInput) return;

  // Clear validation error on typing
  nameInput.addEventListener('input', () => {
    nameInput.classList.remove('is-invalid');
    if (errorMsg) {
      errorMsg.classList.remove('show');
      errorMsg.textContent = '';
    }
  });

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const rawValue = nameInput.value;
    const trimmedName = (rawValue || '').trim();

    // Strict Validation: Reject empty or space-only input
    if (!trimmedName || trimmedName.length === 0) {
      nameInput.classList.add('is-invalid');
      if (errorMsg) {
        errorMsg.textContent = 'Please enter your name.';
        errorMsg.classList.add('show');
      }
      nameInput.focus();
      return;
    }

    // Disable button to prevent double-clicks
    if (enterBtn) {
      enterBtn.disabled = true;
      enterBtn.textContent = 'Entering...';
    }

    // Increment global count & store name locally
    await incrementGlobalCounter();
    localStorage.setItem('codekaro_student_name', trimmedName);

    // Navigate to Page 2 (home.html)
    window.location.href = 'home.html';
  });
}

/* --------------------------------------------------------------------------
   4. PAGE 2 — Home Dashboard (home.html)
   -------------------------------------------------------------------------- */
async function fetchAndDisplayCounter() {
  const countEls = document.querySelectorAll('.global-student-count-val');
  const noteEls = document.querySelectorAll('.counter-status-note');
  if (countEls.length === 0) return;

  try {
    const response = await fetch(COUNTER_API_BASE, { method: 'GET' });
    if (response.ok) {
      const data = await response.json();
      const count = typeof data.count === 'number' ? data.count : (data.value || 0);
      localStorage.setItem('codekaro_cached_student_count', count);
      countEls.forEach(el => (el.textContent = count));
      noteEls.forEach(el => (el.textContent = 'Live Global Count'));
      return;
    }
  } catch (e) {
    // Graceful fallback
    const cached = localStorage.getItem('codekaro_cached_student_count');
    if (cached !== null) {
      countEls.forEach(el => (el.textContent = cached));
      noteEls.forEach(el => (el.textContent = 'Cached Count (Offline)'));
    } else {
      countEls.forEach(el => (el.textContent = '—'));
      noteEls.forEach(el => (el.textContent = 'Unable to load count'));
    }
  }
}

function initHomePage() {
  const sidebarStudentName = document.getElementById('sidebar-student-name');
  const homeStudentGreeting = document.getElementById('home-student-name');
  const headerUserName = document.getElementById('header-user-name');
  const headerUserBadge = document.getElementById('header-user-badge');

  const studentName = localStorage.getItem('codekaro_student_name');

  if (studentName) {
    if (sidebarStudentName) sidebarStudentName.textContent = `${studentName} 👋`;
    if (homeStudentGreeting) homeStudentGreeting.textContent = studentName;
    if (headerUserName) headerUserName.textContent = studentName;
    if (headerUserBadge) headerUserBadge.style.display = 'inline-flex';
  } else {
    if (sidebarStudentName) sidebarStudentName.textContent = 'Student 👋';
    if (homeStudentGreeting) homeStudentGreeting.textContent = 'Student';
  }

  fetchAndDisplayCounter();
}

/* --------------------------------------------------------------------------
   5. PAGE 5 — Interactive MCQ Quiz Engine (All MCQ Pages)
   -------------------------------------------------------------------------- */
function initQuizPage() {
  const questionCards = document.querySelectorAll('.question-card');
  if (questionCards.length === 0) return; // Exit if not an MCQ page

  const totalQuestions = questionCards.length;
  const answeredCountEl = document.getElementById('answered-count');
  const totalCountEl = document.getElementById('total-count');
  const progressFill = document.getElementById('progress-bar-fill');
  const submitQuizBtn = document.getElementById('submit-quiz-btn');
  const resetQuizBtn = document.getElementById('reset-quiz-btn');

  if (totalCountEl) totalCountEl.textContent = totalQuestions;

  // Listen for option selections
  questionCards.forEach(card => {
    const radioInputs = card.querySelectorAll('input[type="radio"]');
    const optionLabels = card.querySelectorAll('.option-label');

    radioInputs.forEach(input => {
      input.addEventListener('change', () => {
        optionLabels.forEach(label => label.classList.remove('selected'));
        const selectedLabel = input.closest('.option-label');
        if (selectedLabel) selectedLabel.classList.add('selected');
        card.classList.add('answered');
        updateProgress();
      });
    });
  });

  function updateProgress() {
    let answeredCount = 0;
    questionCards.forEach(card => {
      if (card.querySelector('input[type="radio"]:checked')) answeredCount++;
    });

    if (answeredCountEl) answeredCountEl.textContent = answeredCount;
    if (progressFill) {
      const pct = Math.round((answeredCount / totalQuestions) * 100);
      progressFill.style.width = `${pct}%`;
    }
  }

  // Submit Quiz -> Calculate Score & Navigate to result.html
  if (submitQuizBtn) {
    submitQuizBtn.addEventListener('click', () => {
      let correct = 0;
      let wrong = 0;
      let unanswered = 0;

      questionCards.forEach(card => {
        const correctAnswer = (card.getAttribute('data-answer') || '').trim().toUpperCase();
        const selected = card.querySelector('input[type="radio"]:checked');

        if (!selected) {
          unanswered++;
        } else {
          const val = selected.value.trim().toUpperCase();
          if (val === correctAnswer) {
            correct++;
          } else {
            wrong++;
          }
        }
      });

      const topicTitleEl = document.querySelector('.subject-page-title');
      const topicName = topicTitleEl ? topicTitleEl.textContent.trim() : 'Quiz';
      const backLinkEl = document.querySelector('.back-btn-link');
      const backUrl = backLinkEl ? backLinkEl.getAttribute('href') : 'index.html';

      // Save result data to sessionStorage for the dedicated result page
      const resultData = {
        topicName: topicName,
        score: correct,
        total: totalQuestions,
        correct: correct,
        wrong: wrong,
        unanswered: unanswered,
        retryUrl: window.location.href,
        backUrl: backUrl
      };

      sessionStorage.setItem('codekaro_last_result', JSON.stringify(resultData));

      // Calculate path to result.html based on folder depth
      const resultPath = determineResultPagePath();
      window.location.href = resultPath;
    });
  }

  // Reset functionality
  if (resetQuizBtn) {
    resetQuizBtn.addEventListener('click', () => {
      questionCards.forEach(card => {
        card.classList.remove('answered');
        const radios = card.querySelectorAll('input[type="radio"]');
        radios.forEach(r => (r.checked = false));
        const labels = card.querySelectorAll('.option-label');
        labels.forEach(l => l.classList.remove('selected'));
      });
      updateProgress();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
}

function determineResultPagePath() {
  const path = window.location.pathname;
  if (path.includes('/subjects/data-communication/')) {
    return '../../result.html';
  } else if (path.includes('/subjects/')) {
    return '../result.html';
  }
  return 'result.html';
}

/* --------------------------------------------------------------------------
   6. PAGE 6 — Dedicated Result Page (result.html)
   -------------------------------------------------------------------------- */
function initResultPage() {
  const resultCard = document.getElementById('standalone-result-card');
  if (!resultCard) return;

  const rawData = sessionStorage.getItem('codekaro_last_result');
  if (!rawData) {
    // If no active result, fallback values
    return;
  }

  try {
    const result = JSON.parse(rawData);
    const scoreNumEl = document.getElementById('result-score-num');
    const scorePctEl = document.getElementById('result-score-pct');
    const correctEl = document.getElementById('result-correct-count');
    const wrongEl = document.getElementById('result-wrong-count');
    const unansweredEl = document.getElementById('result-unanswered-count');
    const topicNameEl = document.getElementById('result-topic-name');
    const celebrationEl = document.getElementById('result-celebration');
    const titleEl = document.getElementById('result-title');
    const retryBtn = document.getElementById('retry-btn');
    const backTopicBtn = document.getElementById('back-topic-btn');

    const pct = Math.round((result.correct / result.total) * 100);

    if (topicNameEl) topicNameEl.textContent = result.topicName || 'MCQ Practice';
    if (scoreNumEl) scoreNumEl.textContent = `${result.correct} / ${result.total}`;
    if (scorePctEl) scorePctEl.textContent = `${pct}% Accuracy`;
    if (correctEl) correctEl.textContent = result.correct;
    if (wrongEl) wrongEl.textContent = result.wrong;
    if (unansweredEl) unansweredEl.textContent = result.unanswered;

    if (celebrationEl && titleEl) {
      if (pct >= 80) {
        celebrationEl.textContent = '🎉';
        titleEl.textContent = 'Outstanding Performance!';
      } else if (pct >= 50) {
        celebrationEl.textContent = '👏';
        titleEl.textContent = 'Good Effort!';
      } else {
        celebrationEl.textContent = '📚';
        titleEl.textContent = 'Keep Practicing!';
      }
    }

    if (retryBtn && result.retryUrl) {
      retryBtn.setAttribute('href', result.retryUrl);
    }
    if (backTopicBtn && result.backUrl) {
      backTopicBtn.setAttribute('href', result.backUrl);
    }
  } catch (e) {
    console.error('Error rendering result data', e);
  }
}
