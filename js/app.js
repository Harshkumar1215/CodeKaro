/**
 * Main Application — State Management, Routing, Event Handling
 * CLASS 10 BIHAR BOARD (BSEB) MCQ PLATFORM
 */

window.App = {

  state: {
    currentView: 'home',          // home | subjectDetail | chapterDetail | testRunner | result | dashboard | analytics | recommendations | history | search
    currentSubjectId: null,
    currentBookId: null,
    currentChapterId: null,
    currentTopicId: null,
    currentSession: null,
    currentResult: null,
    practiceScope: null,
    timerInterval: null
  },

  init: function () {
    // Set default language
    const saved = localStorage.getItem('bseb_lang');
    UI.lang = saved || 'hi';
    this._updateLangButtons();

    // Compute initial counts
    this._counts = QuestionBankEngine.getDynamicCounts(BSEB_QUESTION_BANK);

    // Render home
    this.goHome();
  },

  // ====== LANGUAGE SWITCH ======
  setLanguage: function (lang) {
    UI.lang = lang;
    localStorage.setItem('bseb_lang', lang);
    this._updateLangButtons();
    this._rerender();
  },

  _updateLangButtons: function () {
    document.querySelectorAll('.lang-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.lang === UI.lang);
    });
    // Update mobile bottom nav labels dynamically
    document.querySelectorAll('.bottom-nav-label').forEach(el => {
      if (UI.lang === 'hi' && el.dataset.i18nHi) el.textContent = el.dataset.i18nHi;
      else if (UI.lang === 'en' && el.dataset.i18nEn) el.textContent = el.dataset.i18nEn;
    });
  },

  // ====== NAVIGATION ======
  goHome: function () {
    this._clearTimer();
    this.state.currentView = 'home';
    this.state.currentSession = null;
    this._counts = QuestionBankEngine.getDynamicCounts(BSEB_QUESTION_BANK);
    document.getElementById('main-content').innerHTML = UI.renderHome(BSEB_SYLLABUS, this._counts);
    this._updateNav('home');
  },

  selectSubject: function (subjectId) {
    this.state.currentView = 'subjectDetail';
    this.state.currentSubjectId = subjectId;
    const subject = this._findSubject(subjectId);
    if (!subject) return;
    this._counts = QuestionBankEngine.getDynamicCounts(BSEB_QUESTION_BANK);
    document.getElementById('main-content').innerHTML = UI.renderSubjectDetail(subject, this._counts);
    this._updateNav('home');
  },

  selectChapter: function (subjectId, bookId, chapterId) {
    this.state.currentView = 'chapterDetail';
    this.state.currentSubjectId = subjectId;
    this.state.currentBookId = bookId;
    this.state.currentChapterId = chapterId;
    const subject = this._findSubject(subjectId);
    const book = this._findBook(subject, bookId);
    const chapter = this._findChapter(book, chapterId);
    if (!subject || !book || !chapter) return;
    this._counts = QuestionBankEngine.getDynamicCounts(BSEB_QUESTION_BANK);
    document.getElementById('main-content').innerHTML = UI.renderChapterDetail(subject, book, chapter, this._counts);
    this._updateNav('home');
  },

  showView: function (view) {
    this._clearTimer();
    this.state.currentView = view;
    this._updateNav(view);

    const mainEl = document.getElementById('main-content');

    switch (view) {
      case 'dashboard':
        const stats = AnalyticsEngine.getOverallStats();
        const topicPerf = AnalyticsEngine.getTopicPerformance();
        mainEl.innerHTML = UI.renderDashboard(stats, topicPerf);
        break;
      case 'analytics':
        const perf = AnalyticsEngine.getTopicPerformance();
        mainEl.innerHTML = UI.renderAnalytics(perf);
        break;
      case 'recommendations':
        const recs = AnalyticsEngine.getRecommendations(BSEB_SYLLABUS);
        mainEl.innerHTML = UI.renderRecommendations(recs);
        break;
      case 'history':
        const sessions = AnalyticsEngine.getSessions();
        mainEl.innerHTML = UI.renderHistory(sessions);
        break;
      case 'search':
        mainEl.innerHTML = UI.renderSearch(BSEB_QUESTION_BANK, this._counts);
        break;
      default:
        this.goHome();
    }
  },

  // ====== PRACTICE SETUP ======
  startPracticeSetup: function (scopeType, subjectId, bookId, chapterId, topicId) {
    const filter = { subject_id: subjectId || undefined };
    if (bookId && bookId !== 'null' && bookId !== 'undefined') filter.book_id = bookId;
    if (chapterId && chapterId !== 'null' && chapterId !== 'undefined') filter.chapter_id = chapterId;
    if (topicId && topicId !== 'null' && topicId !== 'undefined') filter.topic_id = topicId;

    this.state.practiceScope = { scopeType, filter };

    const pool = QuestionBankEngine.getQuestionsByScope(BSEB_QUESTION_BANK, filter);
    const availCount = pool.length;

    let scopeLabel = '';
    if (topicId && topicId !== 'null' && topicId !== 'undefined') scopeLabel = this.getTopicName(topicId);
    else if (chapterId && chapterId !== 'null' && chapterId !== 'undefined') scopeLabel = this.getChapterName(chapterId);
    else scopeLabel = this.getSubjectName(subjectId);

    UI._selectedQCount = Math.min(10, availCount);
    UI._selectedMode = 'practice';
    UI._selectedDiff = 'All';

    const modalHtml = UI.renderPracticeSetup(scopeType, scopeLabel, availCount);
    document.getElementById('modal-container').innerHTML = modalHtml;
  },

  closeModal: function () {
    document.getElementById('modal-container').innerHTML = '';
  },

  // ====== LAUNCH TEST ======
  launchTest: function () {
    this.closeModal();

    const scope = this.state.practiceScope;
    if (!scope) return;

    const filter = { ...scope.filter };
    if (UI._selectedDiff !== 'All') filter.difficulty = UI._selectedDiff;
    filter.mode = UI._selectedMode;

    const history = AnalyticsEngine.getQuestionAttempts();
    const session = TestEngine.createTestSession(BSEB_QUESTION_BANK, filter, UI._selectedQCount, history);

    if (session.error) {
      alert(session.message);
      return;
    }

    this.state.currentSession = session;
    this.state.currentView = 'testRunner';
    this._renderTest();
    this._startTimer();
    this._updateNav('');
  },

  // ====== TEST INTERACTION ======
  selectAnswer: function (qId, optKey) {
    const session = this.state.currentSession;
    if (!session) return;

    const isPractice = session.mode === 'practice';
    const alreadyAnswered = !!session.userAnswers[qId];

    if (isPractice && alreadyAnswered) return; // Practice mode: lock after first answer
    if (!isPractice && alreadyAnswered && session.userAnswers[qId].selected_option === optKey) {
      // Deselect in test mode
      delete session.userAnswers[qId];
      this._renderTest();
      return;
    }

    session.userAnswers[qId] = {
      selected_option: optKey,
      timeSpent: Math.round((Date.now() - session.startTime) / 1000)
    };

    this._renderTest();
  },

  nextQuestion: function () {
    const session = this.state.currentSession;
    if (!session) return;
    if (session.currentIndex < session.questions.length - 1) {
      session.currentIndex++;
      this._renderTest();
    }
  },

  prevQuestion: function () {
    const session = this.state.currentSession;
    if (!session) return;
    if (session.currentIndex > 0) {
      session.currentIndex--;
      this._renderTest();
    }
  },

  goToQuestion: function (idx) {
    const session = this.state.currentSession;
    if (!session) return;
    session.currentIndex = idx;
    this._renderTest();
  },

  submitTest: function () {
    const session = this.state.currentSession;
    if (!session) return;

    const unanswered = session.questions.length - Object.keys(session.userAnswers).length;
    if (session.mode === 'test' && unanswered > 0) {
      const msg = UI.lang === 'hi'
        ? `${unanswered} प्रश्न अभी तक अनुत्तरित हैं। क्या आप सबमिट करना चाहते हैं?`
        : `${unanswered} questions are still unanswered. Submit anyway?`;
      if (!confirm(msg)) return;
    }

    this._clearTimer();
    session.endTime = Date.now();
    session.completed = true;

    const result = TestEngine.calculateResult(session);
    AnalyticsEngine.saveSession(result);

    this.state.currentResult = result;
    this.state.currentView = 'result';
    document.getElementById('main-content').innerHTML = UI.renderResult(result);
    this._updateNav('');
  },

  reviewSession: function (index) {
    const sessions = AnalyticsEngine.getSessions();
    if (index >= 0 && index < sessions.length) {
      this.state.currentResult = sessions[index];
      this.state.currentView = 'result';
      document.getElementById('main-content').innerHTML = UI.renderResult(sessions[index]);
    }
  },

  // ====== SEARCH ======
  searchQuestions: function () {
    const query = (document.getElementById('search-input').value || '').toLowerCase().trim();
    const subjectFilter = document.getElementById('search-subject').value;
    const diffFilter = document.getElementById('search-difficulty').value;

    let results = BSEB_QUESTION_BANK.filter(q => {
      if (subjectFilter && q.subject_id !== subjectFilter) return false;
      if (diffFilter && q.difficulty !== diffFilter) return false;
      if (query) {
        const qTextHi = (q.question.hi || '').toLowerCase();
        const qTextEn = (q.question.en || '').toLowerCase();
        if (!qTextHi.includes(query) && !qTextEn.includes(query)) return false;
      }
      return true;
    });

    // Cap display at 50
    const display = results.slice(0, 50);
    const el = document.getElementById('search-results');

    if (display.length === 0) {
      el.innerHTML = `<p style="color:var(--text-muted);padding:1rem;">${UI.lang === 'hi' ? 'कोई परिणाम नहीं मिला' : 'No results found'}</p>`;
      return;
    }

    let html = `<p style="color:var(--text-secondary);margin-bottom:0.75rem;font-size:0.85rem;">${results.length} ${UI.lang === 'hi' ? 'प्रश्न मिले' : 'questions found'}${results.length > 50 ? (' (' + (UI.lang === 'hi' ? 'पहले 50 दिखा रहे हैं' : 'showing first 50') + ')') : ''}</p>`;
    html += '<div style="display:grid;gap:0.65rem;">';

    display.forEach(q => {
      html += `
      <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:0.85rem;text-align:left;">
        <p style="font-weight:600;font-size:0.9rem;margin-bottom:0.35rem;">${UI.t(q.question)}</p>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap;font-size:0.75rem;color:var(--text-muted);">
          <span>${this.getSubjectName(q.subject_id)}</span> ・
          <span>${q.difficulty}</span> ・
          <span>${UI.lang === 'hi' ? 'उत्तर' : 'Answer'}: ${q.correct_option}</span>
        </div>
      </div>`;
    });

    html += '</div>';
    el.innerHTML = html;
  },

  // ====== HELPERS ======
  _findSubject: function (id) {
    return BSEB_SYLLABUS.subjects.find(s => s.id === id);
  },

  _findBook: function (subject, bookId) {
    if (!subject) return null;
    for (let book of subject.books) {
      if (book.id === bookId) return book;
    }
    return null;
  },

  _findChapter: function (book, chapterId) {
    if (!book) return null;
    return book.chapters.find(ch => ch.id === chapterId);
  },

  getSubjectName: function (subjectId) {
    const sub = this._findSubject(subjectId);
    return sub ? UI.t(sub.name) : subjectId;
  },

  getChapterName: function (chapterId) {
    for (let sub of BSEB_SYLLABUS.subjects) {
      for (let book of sub.books) {
        for (let ch of book.chapters) {
          if (ch.id === chapterId) return UI.t(ch.title);
        }
      }
    }
    return chapterId;
  },

  getTopicName: function (topicId) {
    for (let sub of BSEB_SYLLABUS.subjects) {
      for (let book of sub.books) {
        for (let ch of book.chapters) {
          for (let tp of (ch.topics || [])) {
            if (tp.id === topicId) return UI.t(tp.title);
          }
        }
      }
    }
    return topicId;
  },

  _renderTest: function () {
    document.getElementById('main-content').innerHTML = UI.renderTestRunner(this.state.currentSession);
  },

  _rerender: function () {
    // Re-render current view with new language
    switch (this.state.currentView) {
      case 'home': this.goHome(); break;
      case 'subjectDetail': this.selectSubject(this.state.currentSubjectId); break;
      case 'chapterDetail': this.selectChapter(this.state.currentSubjectId, this.state.currentBookId, this.state.currentChapterId); break;
      case 'testRunner': this._renderTest(); break;
      case 'result': if (this.state.currentResult) document.getElementById('main-content').innerHTML = UI.renderResult(this.state.currentResult); break;
      default: this.showView(this.state.currentView);
    }
    this._updateLangButtons();
  },

  _updateNav: function (activeView) {
    document.querySelectorAll('.nav-link').forEach(n => {
      n.classList.toggle('active', n.dataset.view === activeView);
    });
    document.querySelectorAll('.bottom-nav-item').forEach(n => {
      n.classList.toggle('active', n.dataset.view === activeView);
    });
  },

  _startTimer: function () {
    this._clearTimer();
    const session = this.state.currentSession;
    if (!session) return;

    this.state.timerInterval = setInterval(() => {
      const elapsed = Math.round((Date.now() - session.startTime) / 1000);
      const m = String(Math.floor(elapsed / 60)).padStart(2, '0');
      const s = String(elapsed % 60).padStart(2, '0');
      const el = document.getElementById('test-timer');
      if (el) el.textContent = '⏱ ' + m + ':' + s;
    }, 1000);
  },

  _clearTimer: function () {
    if (this.state.timerInterval) {
      clearInterval(this.state.timerInterval);
      this.state.timerInterval = null;
    }
  }
};

// Boot application when DOM ready
document.addEventListener('DOMContentLoaded', function () {
  App.init();
});
