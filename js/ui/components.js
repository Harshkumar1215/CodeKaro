/**
 * UI Components — Dynamic Mobile-First Renderers for all views
 * Renders subjects, chapters, MCQ runner, results, dashboard, analytics, history
 */

window.UI = {

  lang: 'hi', // default medium

  t: function (obj) {
    if (!obj) return '';
    if (typeof obj === 'string') return obj;
    return obj[this.lang] || obj.en || obj.hi || obj.name_hi || obj.name_en || '';
  },

  formatTime: function (seconds) {
    if (!seconds || seconds <= 0) return '0s';
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    if (m === 0) return s + 's';
    return m + 'm ' + s + 's';
  },

  // ====== HOME / SUBJECT SELECTOR ======
  renderHome: function (syllabus, counts) {
    const subjects = syllabus.subjects;
    const colors = {
      math: { bg: 'rgba(59,130,246,0.15)', border: 'rgba(59,130,246,0.4)', icon: '#3b82f6' },
      maths: { bg: 'rgba(59,130,246,0.15)', border: 'rgba(59,130,246,0.4)', icon: '#3b82f6' },
      science: { bg: 'rgba(16,185,129,0.15)', border: 'rgba(16,185,129,0.4)', icon: '#10b981' },
      social: { bg: 'rgba(245,158,11,0.15)', border: 'rgba(245,158,11,0.4)', icon: '#f59e0b' },
      hindi: { bg: 'rgba(225,29,72,0.15)', border: 'rgba(225,29,72,0.4)', icon: '#e11d48' },
      english: { bg: 'rgba(139,92,246,0.15)', border: 'rgba(139,92,246,0.4)', icon: '#8b5cf6' },
      sanskrit: { bg: 'rgba(6,182,212,0.15)', border: 'rgba(6,182,212,0.4)', icon: '#06b6d4' }
    };
    const icons = { math: '📐', maths: '📐', science: '🔬', social: '🌍', hindi: '📕', english: '🇬🇧', sanskrit: '📜' };

    let html = `
      <div class="page-container animate-fade">
        <div style="text-align:center;margin-bottom:clamp(1.25rem, 3.5vw, 2rem);">
          <h1 style="margin-bottom:0.4rem;">
            ${this.lang === 'hi' ? 'कक्षा 10 — बिहार बोर्ड (BSEB)' : 'Class 10 — Bihar Board (BSEB)'}
          </h1>
          <p style="color:var(--text-secondary);font-size:clamp(0.88rem, 2.8vw, 1rem);">
            ${this.lang === 'hi' ? 'MCQ अभ्यास मंच — विषय चुनें' : 'MCQ Practice Platform — Select a Subject'}
          </p>
          <div style="display:inline-flex;align-items:center;gap:0.4rem;margin-top:0.65rem;padding:0.3rem 0.75rem;border-radius:20px;background:rgba(99,102,241,0.15);border:1px solid rgba(99,102,241,0.3);font-size:0.8rem;color:#818cf8;">
            📊 ${this.lang === 'hi' ? 'कुल प्रश्न' : 'Total Questions'}: <strong>${counts.total}</strong>
          </div>
        </div>
        <div class="subject-grid">`;

    subjects.forEach(sub => {
      const c = colors[sub.id] || colors.math;
      const count = counts.subjects[sub.id] || 0;
      html += `
        <div class="subject-card" style="--card-accent:${c.icon};" onclick="App.selectSubject('${sub.id}')">
          <div class="icon-box" style="background:${c.bg};color:${c.icon};">${icons[sub.id] || '📖'}</div>
          <h3 style="font-size:clamp(1.05rem, 3.2vw, 1.2rem);font-weight:700;margin-bottom:0.25rem;">${this.t(sub.name)}</h3>
          <p style="color:var(--text-muted);font-size:0.82rem;margin-bottom:0.85rem;">
            ${sub.books.length} ${this.lang === 'hi' ? 'पुस्तकें' : 'Books'} ・ ${count} ${this.lang === 'hi' ? 'प्रश्न' : 'Questions'}
          </p>
          <div style="margin-top:auto;display:flex;align-items:center;gap:0.4rem;color:${c.icon};font-size:0.85rem;font-weight:600;">
            ${this.lang === 'hi' ? 'अभ्यास शुरू करें' : 'Start Practice'} →
          </div>
        </div>`;
    });

    html += `</div></div>`;
    return html;
  },

  // ====== BOOK / CHAPTER SELECTOR ======
  renderSubjectDetail: function (subject, counts) {
    const colors = {
      math: '#3b82f6', maths: '#3b82f6', science: '#10b981', social: '#f59e0b',
      hindi: '#e11d48', english: '#8b5cf6', sanskrit: '#06b6d4'
    };
    const accent = colors[subject.id] || '#6366f1';

    let html = `
    <div class="page-container animate-fade">
      <button onclick="App.goHome()" style="background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:0.9rem;margin-bottom:1rem;display:inline-flex;align-items:center;gap:0.4rem;padding:0.4rem 0;">
        ← ${this.lang === 'hi' ? 'मुख्य पृष्ठ पर वापस' : 'Back to Home'}
      </button>
      <h2 style="margin-bottom:0.25rem;">${this.t(subject.name)}</h2>
      <p style="color:var(--text-secondary);font-size:0.88rem;margin-bottom:1.25rem;">
        ${this.lang === 'hi' ? 'पुस्तक और अध्याय चुनें या विषय-स्तरीय अभ्यास करें' : 'Select a Book & Chapter or practice at Subject level'}
      </p>
      <div style="margin-bottom:1.5rem;width:100%;">
        <button class="mode-card" onclick="App.startPracticeSetup('subject','${subject.id}',null,null,null)" style="border-color:${accent};">
          <span style="font-weight:700;color:${accent};font-size:clamp(0.92rem, 3vw, 1.05rem);display:block;">📝 ${this.lang === 'hi' ? 'पूरे विषय का अभ्यास' : 'Full Subject Practice'}</span>
          <span style="display:block;color:var(--text-muted);font-size:0.8rem;margin-top:0.2rem;">${counts.subjects[subject.id] || 0} ${this.lang === 'hi' ? 'प्रश्न उपलब्ध' : 'questions available'}</span>
        </button>
      </div>`;

    subject.books.forEach(book => {
      const bookCount = counts.books[book.id] || 0;
      html += `
      <div style="margin-bottom:1.5rem;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.75rem;">
          <h3 style="font-size:clamp(1rem, 3vw, 1.15rem);font-weight:600;">📖 ${this.t(book.name)}</h3>
          <button class="medium-btn" onclick="App.startPracticeSetup('book','${subject.id}','${book.id}',null,null)">
            ${this.lang === 'hi' ? 'पुस्तक अभ्यास' : 'Book Practice'} (${bookCount})
          </button>
        </div>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%, 300px), 1fr));gap:0.65rem;">`;

      book.chapters.forEach(ch => {
        const chCount = counts.chapters[ch.id] || 0;
        const topicCount = (ch.topics && ch.topics.length) || 0;
        const sectionName = ch.section ? this.t(ch.section) : '';
        html += `
          <div class="mode-card" onclick="App.selectChapter('${subject.id}','${book.id}','${ch.id}')" style="display:flex;flex-direction:column;gap:0.35rem;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;">
              <span style="font-weight:600;font-size:clamp(0.88rem, 2.7vw, 0.96rem);flex:1;line-height:1.4;">${this.t(ch.title || ch.name)}</span>
              <span class="badge" style="background:rgba(255,255,255,0.08);color:var(--text-secondary);font-size:0.72rem;flex-shrink:0;">${chCount} Q</span>
            </div>
            <div style="display:flex;align-items:center;gap:0.4rem;flex-wrap:wrap;margin-top:0.15rem;">
              ${sectionName ? `<span class="badge" style="background:rgba(99,102,241,0.12);color:#818cf8;font-size:0.7rem;padding:0.12rem 0.4rem;">${sectionName}</span>` : ''}
              ${topicCount > 0 ? `<span style="color:var(--text-muted);font-size:0.75rem;">${topicCount} ${this.lang === 'hi' ? 'उप-विषय' : 'Topics'}</span>` : ''}
            </div>
          </div>`;
      });

      html += `</div></div>`;
    });

    html += `</div>`;
    return html;
  },

  // ====== CHAPTER DETAIL WITH TOPICS ======
  renderChapterDetail: function (subject, book, chapter, counts) {
    const chCount = counts.chapters[chapter.id] || 0;
    const hasTopics = chapter.topics && chapter.topics.length > 0;

    let html = `
    <div class="page-container animate-fade" style="max-width:850px;">
      <button onclick="App.selectSubject('${subject.id}')" style="background:none;border:none;color:var(--text-secondary);cursor:pointer;font-size:0.9rem;margin-bottom:1rem;display:inline-flex;align-items:center;gap:0.4rem;padding:0.4rem 0;">
        ← ${this.t(subject.name)}
      </button>
      <h2 style="margin-bottom:0.25rem;">${this.t(chapter.title || chapter.name)}</h2>
      <p style="color:var(--text-secondary);font-size:0.85rem;margin-bottom:1.25rem;">
        ${this.t(book.name)} ${chapter.section ? '• ' + this.t(chapter.section) : ''} — ${chCount} ${this.lang === 'hi' ? 'प्रश्न' : 'Questions'}
      </p>
      <div style="margin-bottom:1.5rem;">
        <button class="mode-card" onclick="App.startPracticeSetup('chapter','${subject.id}','${book.id}','${chapter.id}',null)" style="border-color:var(--accent-primary);">
          <span style="font-weight:700;color:var(--accent-primary);font-size:clamp(0.92rem, 3vw, 1.05rem);display:block;">📝 ${this.lang === 'hi' ? 'पूरे अध्याय का अभ्यास' : 'Full Chapter Practice'} (${chCount})</span>
          <span style="color:var(--text-muted);font-size:0.78rem;display:block;margin-top:0.2rem;">${this.lang === 'hi' ? 'अध्याय के सभी प्रश्नों का अभ्यास' : 'Practice all questions from this chapter'}</span>
        </button>
      </div>`;

    if (hasTopics) {
      html += `
      <h3 style="font-size:clamp(0.98rem, 3vw, 1.1rem);font-weight:600;margin-bottom:0.75rem;">${this.lang === 'hi' ? 'उप-विषय (Topics)' : 'Topics'}</h3>
      <div style="display:grid;gap:0.55rem;">`;

      chapter.topics.forEach(topic => {
        const tCount = counts.topics[topic.id] || 0;
        html += `
          <div class="mode-card" onclick="App.startPracticeSetup('topic','${subject.id}','${book.id}','${chapter.id}','${topic.id}')" style="display:flex;justify-content:space-between;align-items:center;gap:0.5rem;">
            <span style="font-weight:500;font-size:clamp(0.85rem, 2.6vw, 0.94rem);line-height:1.4;">${this.t(topic.title || topic.name)}</span>
            <span class="badge" style="background:rgba(99,102,241,0.15);color:#818cf8;border:1px solid rgba(99,102,241,0.3);flex-shrink:0;">${tCount} Q</span>
          </div>`;
      });

      html += `</div>`;
    }

    html += `</div>`;
    return html;
  },

  // ====== PRACTICE / TEST SETUP MODAL ======
  renderPracticeSetup: function (scopeType, scopeLabel, availableCount) {
    const qOptions = [10, 20, 30, 50, 75, 100];
    const maxAvail = availableCount;

    let html = `
    <div class="modal-overlay" id="practice-setup-modal">
      <div class="modal-content animate-fade">
        <h3 style="margin-bottom:0.35rem;">
          ${this.lang === 'hi' ? 'अभ्यास सेटिंग' : 'Practice Setup'}
        </h3>
        <p style="color:var(--text-secondary);font-size:0.85rem;margin-bottom:1.15rem;">
          ${scopeLabel} — <strong>${maxAvail}</strong> ${this.lang === 'hi' ? 'प्रश्न उपलब्ध' : 'questions available'}
        </p>

        <label style="display:block;font-weight:600;font-size:0.88rem;margin-bottom:0.45rem;">
          ${this.lang === 'hi' ? 'प्रश्नों की संख्या चुनें:' : 'Select number of questions:'}
        </label>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-bottom:1.15rem;" id="q-count-options">`;

    qOptions.forEach((n, i) => {
      const disabled = n > maxAvail;
      const isDefault = (!disabled && i === 0) || n === Math.min(10, maxAvail);
      html += `
          <button class="medium-btn ${isDefault ? 'active' : ''}" ${disabled ? 'disabled style="opacity:0.35;cursor:not-allowed;"' : ''}
            onclick="UI._selectQCount(this, ${Math.min(n, maxAvail)})" data-count="${Math.min(n, maxAvail)}">${n > maxAvail ? maxAvail : n}</button>`;
    });

    html += `
        </div>

        <label style="display:block;font-weight:600;font-size:0.88rem;margin-bottom:0.45rem;">
          ${this.lang === 'hi' ? 'मोड चुनें:' : 'Select Mode:'}
        </label>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.5rem;margin-bottom:1.15rem;">
          <button class="medium-btn active" id="mode-practice" onclick="UI._selectMode('practice')" style="text-align:center;padding:0.55rem 0.4rem;">
            ${this.lang === 'hi' ? '📖 तुरंत उत्तर' : '📖 Instant'}
          </button>
          <button class="medium-btn" id="mode-test" onclick="UI._selectMode('test')" style="text-align:center;padding:0.55rem 0.4rem;">
            ${this.lang === 'hi' ? '📝 टेस्ट मोड' : '📝 Test Mode'}
          </button>
        </div>

        <label style="display:block;font-weight:600;font-size:0.88rem;margin-bottom:0.45rem;">
          ${this.lang === 'hi' ? 'कठिनाई स्तर:' : 'Difficulty:'}
        </label>
        <div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-bottom:1.35rem;">
          <button class="medium-btn active" id="diff-all" onclick="UI._selectDiff('All')">All</button>
          <button class="medium-btn" id="diff-easy" onclick="UI._selectDiff('Easy')">Easy</button>
          <button class="medium-btn" id="diff-medium" onclick="UI._selectDiff('Medium')">Medium</button>
          <button class="medium-btn" id="diff-hard" onclick="UI._selectDiff('Hard')">Hard</button>
        </div>

        <div style="display:flex;gap:0.65rem;flex-wrap:wrap;">
          <button onclick="App.launchTest()" style="flex:1;min-width:120px;min-height:44px;padding:0.65rem;border-radius:var(--radius-md);background:var(--accent-primary);color:white;border:none;font-weight:700;font-size:0.95rem;cursor:pointer;">
            ${this.lang === 'hi' ? '🚀 शुरू करें' : '🚀 Start'}
          </button>
          <button onclick="App.closeModal()" style="min-height:44px;padding:0.65rem 1rem;border-radius:var(--radius-md);background:rgba(255,255,255,0.08);color:var(--text-secondary);border:1px solid var(--border-color);cursor:pointer;font-weight:600;font-size:0.9rem;">
            ${this.lang === 'hi' ? 'रद्द' : 'Cancel'}
          </button>
        </div>
      </div>
    </div>`;

    return html;
  },

  _selectedQCount: 10,
  _selectedMode: 'practice',
  _selectedDiff: 'All',

  _selectQCount: function (btn, count) {
    document.querySelectorAll('#q-count-options .medium-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    this._selectedQCount = count;
  },

  _selectMode: function (mode) {
    this._selectedMode = mode;
    const mp = document.getElementById('mode-practice');
    const mt = document.getElementById('mode-test');
    if (mp) mp.classList.toggle('active', mode === 'practice');
    if (mt) mt.classList.toggle('active', mode === 'test');
  },

  _selectDiff: function (diff) {
    this._selectedDiff = diff;
    ['all', 'easy', 'medium', 'hard'].forEach(d => {
      const el = document.getElementById('diff-' + d);
      if (el) el.classList.toggle('active', d === diff.toLowerCase());
    });
  },

  // ====== MCQ TEST RUNNER ======
  renderTestRunner: function (session) {
    if (!session || !session.questions || session.questions.length === 0) {
      return '<div class="page-container" style="text-align:center;color:var(--text-secondary);padding:3rem;">No questions available.</div>';
    }

    const q = session.questions[session.currentIndex];
    const idx = session.currentIndex;
    const total = session.questions.length;
    const progress = ((idx + 1) / total * 100).toFixed(1);
    const userAns = session.userAnswers[q.id];
    const selectedOpt = userAns ? userAns.selected_option : null;
    const isPractice = session.mode === 'practice';
    const hasAnswered = !!selectedOpt;
    const showFeedback = isPractice && hasAnswered;

    let html = `
    <div class="mcq-container animate-fade">
      <!-- Top status bar -->
      <div class="mcq-header-bar">
        <div style="display:flex;align-items:center;gap:0.4rem;flex-wrap:wrap;">
          <span style="font-weight:700;font-size:clamp(0.95rem, 3vw, 1.1rem);">Q ${idx + 1} / ${total}</span>
          <span class="badge" style="background:rgba(${q.difficulty === 'Easy' ? '16,185,129' : q.difficulty === 'Hard' ? '239,68,68' : '245,158,11'},0.2);color:${q.difficulty === 'Easy' ? '#10b981' : q.difficulty === 'Hard' ? '#ef4444' : '#f59e0b'};border:1px solid rgba(${q.difficulty === 'Easy' ? '16,185,129' : q.difficulty === 'Hard' ? '239,68,68' : '245,158,11'},0.3);">${q.difficulty}</span>
          <span class="badge" style="background:rgba(99,102,241,0.15);color:#818cf8;border:1px solid rgba(99,102,241,0.3);">${session.mode === 'test' ? (this.lang === 'hi' ? 'परीक्षा' : 'Test') : (this.lang === 'hi' ? 'अभ्यास' : 'Practice')}</span>
        </div>
        <div id="test-timer" class="mcq-timer">⏱ 00:00</div>
      </div>

      <!-- Progress bar -->
      <div class="progress-bar-bg" style="margin-bottom:1.15rem;">
        <div class="progress-bar-fill" style="width:${progress}%"></div>
      </div>

      <!-- Question Card -->
      <div class="mcq-question-card">
        <p class="mcq-question-text">${this.t(q.question)}</p>
      </div>

      <!-- Options -->
      <div class="mcq-options-grid">`;

    const optKeys = ['A', 'B', 'C', 'D'];
    optKeys.forEach(key => {
      const optText = q.options[this.lang] ? q.options[this.lang][key] : (q.options.en ? q.options.en[key] : (q.options.hi ? q.options.hi[key] : ''));
      let extraClass = '';
      let disabled = '';

      if (showFeedback) {
        if (key === q.correct_option) extraClass = 'correct';
        else if (key === selectedOpt && key !== q.correct_option) extraClass = 'incorrect';
        disabled = 'disabled';
      } else if (key === selectedOpt) {
        extraClass = 'selected';
      }

      html += `
        <button class="option-btn ${extraClass}" ${disabled} onclick="App.selectAnswer('${q.id}','${key}')">
          <span class="option-badge">${key}</span>
          <span style="flex:1;text-align:left;">${optText}</span>
        </button>`;
    });

    html += `</div>`;

    // Instant Feedback Explanation in Practice Mode
    if (showFeedback) {
      const isCorrect = selectedOpt === q.correct_option;
      html += `
      <div style="background:${isCorrect ? 'rgba(16,185,129,0.1)' : 'rgba(239,68,68,0.1)'};border:1px solid ${isCorrect ? 'rgba(16,185,129,0.3)' : 'rgba(239,68,68,0.3)'};border-radius:var(--radius-md);padding:clamp(0.75rem, 3vw, 1.15rem);margin-bottom:1.25rem;">
        <p style="font-weight:700;margin-bottom:0.35rem;color:${isCorrect ? '#10b981' : '#ef4444'};font-size:0.95rem;">
          ${isCorrect ? (this.lang === 'hi' ? '✅ सही उत्तर!' : '✅ Correct!') : (this.lang === 'hi' ? '❌ गलत उत्तर' : '❌ Incorrect')}
        </p>
        <p style="color:var(--text-secondary);font-size:0.88rem;line-height:1.6;">${this.t(q.explanation)}</p>
      </div>`;
    }

    // Action Navigation Buttons
    html += `
      <div style="display:flex;gap:0.5rem;flex-wrap:wrap;align-items:center;margin-bottom:1.5rem;">
        <button onclick="App.prevQuestion()" ${idx === 0 ? 'disabled style="opacity:0.4;"' : ''} style="min-height:44px;padding:0.6rem 1.15rem;border-radius:var(--radius-md);background:rgba(255,255,255,0.08);border:1px solid var(--border-color);color:var(--text-primary);cursor:pointer;font-weight:600;font-size:0.9rem;">
          ← ${this.lang === 'hi' ? 'पिछला' : 'Previous'}
        </button>`;

    if (idx < total - 1) {
      html += `
        <button onclick="App.nextQuestion()" style="min-height:44px;padding:0.6rem 1.25rem;border-radius:var(--radius-md);background:var(--accent-primary);border:none;color:white;cursor:pointer;font-weight:600;font-size:0.9rem;">
          ${this.lang === 'hi' ? 'अगला' : 'Next'} →
        </button>`;
    }

    if (session.mode === 'test') {
      html += `
        <button onclick="App.submitTest()" style="margin-left:auto;min-height:44px;padding:0.6rem 1.25rem;border-radius:var(--radius-md);background:var(--accent-success);border:none;color:white;cursor:pointer;font-weight:700;font-size:0.9rem;">
          ${this.lang === 'hi' ? '✅ सबमिट करें' : '✅ Submit Test'}
        </button>`;
    } else if (idx === total - 1) {
      html += `
        <button onclick="App.submitTest()" style="margin-left:auto;min-height:44px;padding:0.6rem 1.25rem;border-radius:var(--radius-md);background:var(--accent-success);border:none;color:white;cursor:pointer;font-weight:700;font-size:0.9rem;">
          ${this.lang === 'hi' ? '📊 परिणाम देखें' : '📊 View Results'}
        </button>`;
    }

    html += `</div>`;

    // Question Palette (Horizontally and vertically responsive grid)
    html += `
      <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);padding:clamp(0.75rem, 3vw, 1.15rem);">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.6rem;">
          <p style="font-weight:600;font-size:0.85rem;">${this.lang === 'hi' ? 'प्रश्न पटल' : 'Question Palette'}</p>
          <span style="font-size:0.75rem;color:var(--text-muted);">${Object.keys(session.userAnswers).length}/${total} ${this.lang === 'hi' ? 'हल' : 'answered'}</span>
        </div>
        <div class="palette-grid">`;

    session.questions.forEach((pq, pi) => {
      let cls = 'unanswered';
      if (session.userAnswers[pq.id]) cls = 'answered';
      if (session.flagged[pq.id]) cls = 'flagged';
      if (pi === idx) cls += ' current';

      html += `<button class="palette-btn ${cls}" onclick="App.goToQuestion(${pi})">${pi + 1}</button>`;
    });

    html += `</div></div></div>`;
    return html;
  },

  // ====== RESULT PAGE ======
  renderResult: function (result) {
    const pct = result.percentage;
    const gradColor = pct >= 75 ? '#10b981' : pct >= 50 ? '#f59e0b' : '#ef4444';

    let html = `
    <div class="page-container animate-fade" style="max-width:850px;">
      <div style="text-align:center;margin-bottom:1.5rem;">
        <div style="width:110px;height:110px;border-radius:50%;background:conic-gradient(${gradColor} ${pct * 3.6}deg, rgba(255,255,255,0.1) 0deg);display:flex;align-items:center;justify-content:center;margin:0 auto 0.75rem;">
          <div style="width:88px;height:88px;border-radius:50%;background:var(--bg-main);display:flex;align-items:center;justify-content:center;flex-direction:column;">
            <span style="font-size:1.4rem;font-weight:800;color:${gradColor};">${pct}%</span>
            <span style="font-size:0.68rem;color:var(--text-muted);">${this.lang === 'hi' ? 'स्कोर' : 'Score'}</span>
          </div>
        </div>
        <h2>${pct >= 75 ? '🏆' : pct >= 50 ? '👍' : '📚'} ${this.lang === 'hi' ? 'अभ्यास परिणाम' : 'Test Result'}</h2>
      </div>

      <div class="stat-cards-grid">
        ${this._statBox(this.lang === 'hi' ? 'कुल प्रश्न' : 'Total', result.totalQuestions, '#6366f1')}
        ${this._statBox(this.lang === 'hi' ? 'प्रयास किए' : 'Attempted', result.attemptedCount, '#8b5cf6')}
        ${this._statBox(this.lang === 'hi' ? 'सही' : 'Correct', result.correctCount, '#10b981')}
        ${this._statBox(this.lang === 'hi' ? 'गलत' : 'Incorrect', result.incorrectCount, '#ef4444')}
        ${this._statBox(this.lang === 'hi' ? 'अनुत्तरित' : 'Unanswered', result.unattemptedCount, '#64748b')}
        ${this._statBox(this.lang === 'hi' ? 'सटीकता' : 'Accuracy', result.accuracy + '%', '#06b6d4')}
        ${this._statBox(this.lang === 'hi' ? 'समय' : 'Time', this.formatTime(result.timeTakenSeconds), '#f59e0b')}
        ${this._statBox(this.lang === 'hi' ? 'मोड' : 'Mode', result.mode === 'test' ? 'Test' : 'Practice', '#e11d48')}
      </div>

      <div style="display:flex;gap:0.65rem;margin-bottom:1.75rem;flex-wrap:wrap;">
        <button onclick="App.goHome()" style="flex:1;min-width:130px;min-height:44px;padding:0.65rem 1.15rem;border-radius:var(--radius-md);background:var(--accent-primary);border:none;color:white;cursor:pointer;font-weight:600;font-size:0.9rem;">
          ${this.lang === 'hi' ? '🏠 होम पर जाएं' : '🏠 Go Home'}
        </button>
        <button onclick="App.showView('dashboard')" style="flex:1;min-width:130px;min-height:44px;padding:0.65rem 1.15rem;border-radius:var(--radius-md);background:rgba(255,255,255,0.08);border:1px solid var(--border-color);color:var(--text-primary);cursor:pointer;font-weight:600;font-size:0.9rem;">
          ${this.lang === 'hi' ? '📊 डैशबोर्ड' : '📊 Dashboard'}
        </button>
      </div>

      <h3 style="margin-bottom:0.85rem;">${this.lang === 'hi' ? 'प्रश्नवार समीक्षा' : 'Question-by-Question Review'}</h3>
      <div style="display:grid;gap:0.65rem;">`;

    result.details.forEach(d => {
      const iconStatus = d.selected_option ? (d.is_correct ? '✅' : '❌') : '⏭';
      html += `
        <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);padding:clamp(0.75rem, 2.5vw, 1rem);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;margin-bottom:0.4rem;">
            <span style="font-weight:600;font-size:clamp(0.85rem, 2.8vw, 0.95rem);line-height:1.5;">Q${d.index}. ${this.t(d.question)}</span>
            <span style="flex-shrink:0;font-size:1.15rem;">${iconStatus}</span>
          </div>
          <div style="font-size:0.82rem;color:var(--text-secondary);margin-bottom:0.35rem;flex-wrap:wrap;display:flex;gap:0.5rem;">
            <span>${this.lang === 'hi' ? 'आपका उत्तर' : 'Your Answer'}: <strong style="color:${d.is_correct ? '#10b981' : d.selected_option ? '#ef4444' : '#64748b'};">${d.selected_option || (this.lang === 'hi' ? 'कोई नहीं' : 'None')}</strong></span>
            <span>・ ${this.lang === 'hi' ? 'सही उत्तर' : 'Correct'}: <strong style="color:#10b981;">${d.correct_option}</strong></span>
          </div>
          <p style="font-size:0.82rem;color:var(--text-muted);border-top:1px solid var(--border-color);padding-top:0.45rem;margin-top:0.35rem;line-height:1.5;">${this.t(d.explanation)}</p>
        </div>`;
    });

    html += `</div></div>`;
    return html;
  },

  _statBox: function (label, value, color) {
    return `
    <div class="stat-box">
      <div class="stat-value" style="color:${color};">${value}</div>
      <div class="stat-label">${label}</div>
    </div>`;
  },

  // ====== DASHBOARD ======
  renderDashboard: function (stats, topicPerf) {
    let html = `
    <div class="page-container animate-fade">
      <h2 style="margin-bottom:1.15rem;">📊 ${this.lang === 'hi' ? 'डैशबोर्ड' : 'Dashboard'}</h2>
      <div class="stat-cards-grid">
        ${this._statBox(this.lang === 'hi' ? 'कुल टेस्ट' : 'Total Tests', stats.totalTests, '#6366f1')}
        ${this._statBox(this.lang === 'hi' ? 'प्रयास किए' : 'Attempted', stats.totalAttempted, '#8b5cf6')}
        ${this._statBox(this.lang === 'hi' ? 'सही' : 'Correct', stats.totalCorrect, '#10b981')}
        ${this._statBox(this.lang === 'hi' ? 'गलत' : 'Incorrect', stats.totalIncorrect, '#ef4444')}
        ${this._statBox(this.lang === 'hi' ? 'सटीकता' : 'Accuracy', stats.accuracy + '%', '#06b6d4')}
        ${this._statBox(this.lang === 'hi' ? 'सर्वश्रेष्ठ' : 'Best Score', stats.bestScorePercent + '%', '#f59e0b')}
        ${this._statBox(this.lang === 'hi' ? 'कुल समय' : 'Total Time', this.formatTime(stats.totalTimeSeconds), '#e11d48')}
        ${this._statBox(this.lang === 'hi' ? 'स्ट्रीक' : 'Streak', stats.currentStreak + ' 🔥', '#fb923c')}
      </div>`;

    if (stats.totalTests === 0) {
      html += `<div style="text-align:center;padding:2.5rem 1rem;color:var(--text-muted);background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
        <p style="font-size:0.95rem;">${this.lang === 'hi' ? 'अभी तक कोई टेस्ट नहीं दिया। अभ्यास शुरू करें!' : 'No tests taken yet. Start practicing!'}</p>
        <button onclick="App.goHome()" style="margin-top:1rem;min-height:44px;padding:0.65rem 1.5rem;border-radius:var(--radius-md);background:var(--accent-primary);border:none;color:white;cursor:pointer;font-weight:600;">
          ${this.lang === 'hi' ? '🚀 अभ्यास शुरू करें' : '🚀 Start Practice'}
        </button>
      </div>`;
    } else {
      html += `<h3 style="margin-bottom:0.75rem;">${this.lang === 'hi' ? 'विषय-स्तरीय प्रदर्शन' : 'Topic-Level Performance'}</h3>`;

      if (topicPerf.all.length > 0) {
        html += `<div style="display:grid;gap:0.5rem;">`;
        topicPerf.all.forEach(tp => {
          const topicName = App.getTopicName(tp.topic_id);
          const barWidth = tp.accuracy;
          const barColor = tp.accuracy >= 75 ? '#10b981' : tp.accuracy >= 50 ? '#f59e0b' : '#ef4444';
          html += `
          <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:0.75rem 0.9rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;gap:0.5rem;margin-bottom:0.35rem;">
              <span style="font-size:clamp(0.82rem, 2.7vw, 0.9rem);font-weight:500;line-height:1.3;">${topicName}</span>
              <span style="font-size:0.78rem;font-weight:700;color:${barColor};flex-shrink:0;">${tp.accuracy}% (${tp.correct}/${tp.total})</span>
            </div>
            <div class="progress-bar-bg" style="height:6px;">
              <div style="height:100%;width:${barWidth}%;background:${barColor};border-radius:3px;transition:width 0.3s;"></div>
            </div>
          </div>`;
        });
        html += `</div>`;
      }
    }

    html += `</div>`;
    return html;
  },

  // ====== ANALYTICS ======
  renderAnalytics: function (topicPerf) {
    let html = `
    <div class="page-container animate-fade">
      <h2 style="margin-bottom:1.15rem;">📈 ${this.lang === 'hi' ? 'प्रदर्शन विश्लेषण' : 'Performance Analytics'}</h2>`;

    if (topicPerf.all.length === 0) {
      html += `<div style="text-align:center;padding:2.5rem 1rem;color:var(--text-muted);background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
        ${this.lang === 'hi' ? 'डेटा उपलब्ध नहीं है। पहले कुछ टेस्ट दें।' : 'No data available. Take some tests first.'}
      </div>`;
    } else {
      if (topicPerf.strong.length > 0) {
        html += `<h3 style="font-size:1rem;font-weight:600;margin:1rem 0 0.5rem;color:#10b981;">💪 ${this.lang === 'hi' ? 'मजबूत क्षेत्र (≥75%)' : 'Strong Areas (≥75%)'}</h3>`;
        html += this._renderTopicList(topicPerf.strong, '#10b981');
      }
      if (topicPerf.moderate.length > 0) {
        html += `<h3 style="font-size:1rem;font-weight:600;margin:1rem 0 0.5rem;color:#f59e0b;">⚡ ${this.lang === 'hi' ? 'और अभ्यास करें (50-75%)' : 'Practice More (50-75%)'}</h3>`;
        html += this._renderTopicList(topicPerf.moderate, '#f59e0b');
      }
      if (topicPerf.weak.length > 0) {
        html += `<h3 style="font-size:1rem;font-weight:600;margin:1rem 0 0.5rem;color:#ef4444;">🔴 ${this.lang === 'hi' ? 'कमजोर क्षेत्र (<50%)' : 'Weak Areas (<50%)'}</h3>`;
        html += this._renderTopicList(topicPerf.weak, '#ef4444');
      }
    }

    html += `</div>`;
    return html;
  },

  _renderTopicList: function (topics, color) {
    let html = '<div style="display:grid;gap:0.45rem;">';
    topics.forEach(tp => {
      const name = App.getTopicName(tp.topic_id);
      html += `
        <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-sm);padding:0.7rem 0.9rem;display:flex;justify-content:space-between;align-items:center;gap:0.5rem;">
          <span style="font-size:clamp(0.82rem, 2.7vw, 0.9rem);">${name}</span>
          <span style="font-weight:700;color:${color};font-size:0.82rem;flex-shrink:0;">${tp.accuracy}% (${tp.correct}/${tp.total})</span>
        </div>`;
    });
    html += '</div>';
    return html;
  },

  // ====== RECOMMENDATIONS ======
  renderRecommendations: function (recommendations) {
    let html = `
    <div class="page-container animate-fade">
      <h2 style="margin-bottom:1.15rem;">🎯 ${this.lang === 'hi' ? 'आपके लिए सुझाव' : 'Recommended for You'}</h2>`;

    if (recommendations.length === 0) {
      html += `<div style="text-align:center;padding:2.5rem 1rem;color:var(--text-muted);background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
        ${this.lang === 'hi' ? 'कोई सुझाव उपलब्ध नहीं।' : 'No recommendations yet.'}
      </div>`;
    } else {
      html += '<div style="display:grid;gap:0.65rem;">';
      recommendations.forEach(rec => {
        html += `
          <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);padding:clamp(0.85rem, 3vw, 1.25rem);">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:0.5rem;margin-bottom:0.45rem;">
              <h4 style="font-weight:600;font-size:clamp(0.92rem, 2.8vw, 1rem);">${this.t(rec.title)}</h4>
              <span class="badge" style="${rec.badgeColor ? 'background:' + (rec.badgeColor.includes('bg-') ? 'rgba(99,102,241,0.15)' : rec.badgeColor) : ''};font-size:0.7rem;">${rec.badgeText}</span>
            </div>
            <p style="color:var(--text-secondary);font-size:0.82rem;margin-bottom:0.75rem;line-height:1.5;">${this.t(rec.reason)}</p>
            <button onclick="App.startPracticeSetup('${rec.topic_id ? 'topic' : 'subject'}','${rec.subject_id}',null,'${rec.chapter_id || ''}','${rec.topic_id || ''}')"
              style="min-height:38px;padding:0.45rem 1rem;border-radius:var(--radius-sm);background:var(--accent-primary);border:none;color:white;cursor:pointer;font-weight:600;font-size:0.82rem;">
              ${this.lang === 'hi' ? '▶ अभ्यास करें' : '▶ Practice Now'}
            </button>
          </div>`;
      });
      html += '</div>';
    }

    html += `</div>`;
    return html;
  },

  // ====== SESSION HISTORY ======
  renderHistory: function (sessions) {
    let html = `
    <div class="page-container animate-fade">
      <h2 style="margin-bottom:1.15rem;">📋 ${this.lang === 'hi' ? 'सत्र इतिहास' : 'Session History'}</h2>`;

    if (sessions.length === 0) {
      html += `<div style="text-align:center;padding:2.5rem 1rem;color:var(--text-muted);background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
        ${this.lang === 'hi' ? 'अभी तक कोई सत्र नहीं है।' : 'No sessions yet.'}
      </div>`;
    } else {
      html += '<div style="display:grid;gap:0.65rem;">';
      sessions.forEach((s, i) => {
        const dt = new Date(s.date);
        const dateStr = dt.toLocaleDateString('en-IN', { day: 'numeric', month: 'short' });
        const timeStr = dt.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
        const pctColor = s.percentage >= 75 ? '#10b981' : s.percentage >= 50 ? '#f59e0b' : '#ef4444';

        html += `
          <div style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);padding:clamp(0.75rem, 2.5vw, 1rem);cursor:pointer;" onclick="App.reviewSession(${i})">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.4rem;">
              <div>
                <span style="font-weight:600;font-size:clamp(0.85rem, 2.8vw, 0.95rem);">${s.scope ? (App.getSubjectName(s.scope.subject_id)) : 'Test'}</span>
                <span style="color:var(--text-muted);font-size:0.75rem;margin-left:0.35rem;">${dateStr} ${timeStr}</span>
              </div>
              <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
                <span style="font-size:0.8rem;color:var(--text-secondary);">${s.correctCount}/${s.totalQuestions}</span>
                <span style="font-weight:800;color:${pctColor};font-size:1rem;">${s.percentage}%</span>
                <span class="badge" style="background:rgba(255,255,255,0.08);color:var(--text-secondary);font-size:0.68rem;">${s.mode}</span>
              </div>
            </div>
          </div>`;
      });
      html += '</div>';
    }

    html += `</div>`;
    return html;
  },

  // ====== SEARCH ======
  renderSearch: function (bank, counts) {
    let html = `
    <div class="page-container animate-fade">
      <h2 style="margin-bottom:1rem;">🔍 ${this.lang === 'hi' ? 'खोजें और फ़िल्टर करें' : 'Search & Filter'}</h2>
      <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.15rem;">
        <input id="search-input" type="text" placeholder="${this.lang === 'hi' ? 'प्रश्न खोजें...' : 'Search questions...'}"
          style="flex:1;min-width:min(100%, 200px);min-height:42px;padding:0.6rem 0.85rem;border-radius:var(--radius-md);background:var(--bg-card);border:1px solid var(--border-color);color:var(--text-primary);font-size:0.9rem;"
          oninput="App.searchQuestions()">
        <select id="search-subject" onchange="App.searchQuestions()" style="min-height:42px;padding:0.5rem;border-radius:var(--radius-md);background:var(--bg-card);border:1px solid var(--border-color);color:var(--text-primary);font-size:0.82rem;flex:1;min-width:130px;">
          <option value="">${this.lang === 'hi' ? 'सभी विषय' : 'All Subjects'}</option>`;

    window.BSEB_SYLLABUS.subjects.forEach(s => {
      html += `<option value="${s.id}">${this.t(s.name)}</option>`;
    });

    html += `</select>
        <select id="search-difficulty" onchange="App.searchQuestions()" style="min-height:42px;padding:0.5rem;border-radius:var(--radius-md);background:var(--bg-card);border:1px solid var(--border-color);color:var(--text-primary);font-size:0.82rem;flex:1;min-width:100px;">
          <option value="">${this.lang === 'hi' ? 'सभी कठिनाई' : 'All Difficulty'}</option>
          <option value="Easy">Easy</option>
          <option value="Medium">Medium</option>
          <option value="Hard">Hard</option>
        </select>
      </div>
      <div id="search-results" style="color:var(--text-muted);text-align:center;padding:1.5rem;background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-md);">
        ${this.lang === 'hi' ? 'खोज शुरू करने के लिए टाइप करें' : 'Start typing to search'}
      </div>
    </div>`;
    return html;
  }
};
