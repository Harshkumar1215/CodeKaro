# CODEKARO — MCQ Practice Platform

**CODEKARO** is a fast, clean, and responsive educational Multiple Choice Question (MCQ) practice website built for students.

*Tagline:* **Learn • Practice • Improve**

---

## 🚀 Key Features

- **100% Pure Static Architecture**: Built using pure **HTML5**, **CSS3 (Vanilla)**, and **JavaScript (Vanilla)**.
- **Student Name Entry & Strict Validation**:
  - Trims leading/trailing whitespace.
  - Rejects empty and space-only inputs with an inline alert: `"Please enter a valid name."`.
  - Remembers the student session locally without storing personal details in a database.
- **Global Student Counter**:
  - Displays real-time global student counts across devices without storing credentials or GitHub tokens in client code.
  - Automatically increments on successful student login (+1 per student entry).
  - Double-click debounce protection prevents accidental count inflation.
  - Graceful fallback with clear status notices if offline.
- **Zero Dependencies**: No React, No Node.js, No backend, No JSON databases, and No third-party frameworks.
- **MCQs Direct in HTML**: Questions are written directly inside subject HTML files for instant editing, readability, and maintenance.
- **Interactive Quiz Engine**: Dynamic progress tracking, instant score calculation, percentage evaluation, and color-coded answer review.
- **Light & Dark Mode**: Seamless theme toggle with user preference stored in `localStorage`.
- **GitHub Pages Ready**: Pure relative paths make it ready to deploy on GitHub Pages with one click.

---

## 📁 Project Structure

```text
CODEKARO/
│
├── index.html                           # Page 1: Student Name Entry (Strictly Name Entry Only)
├── home.html                            # Page 2: Dashboard (Sidebar, Counter, Subjects, About at bottom)
├── result.html                          # Dedicated Standalone Result Evaluation Page
├── README.md                            # Documentation
│
├── css/
│   └── style.css                        # Universal responsive styling, grid & themes
│
├── js/
│   └── script.js                        # Validation, atomic global counter, scoring & dark mode
│
├── api/
│   └── counter.js                       # Serverless global counter endpoint
│
├── database/
│   ├── stats.json                       # Central database statistics file
│   ├── counter_server.py                # Optional atomic backend server
│   └── README.md
│
├── highlighter/
│   ├── highlighter.js                   # Non-destructive text highlighter
│   └── highlighter.css
│
└── subjects/                            # Separate HTML files for each subject
    ├── data-communication/
    │   ├── index.html                   # Data Communication Topics Hub
    │   ├── data-communication/
    │   │   └── index.html               # Topic 1: Fundamentals MCQs
    │   ├── components/
    │   │   └── index.html               # Topic 2: Components MCQs
    │   ├── modes-of-communication/
    │   │   ├── index.html               # Topic 3: Subtopic Selector
    │   │   ├── simplex.html             # Simplex MCQs
    │   │   ├── half-duplex.html         # Half Duplex MCQs
    │   │   └── full-duplex.html         # Full Duplex MCQs
    │   └── transmission-medium/
    │       ├── index.html               # Topic 4: Subtopic Selector
    │       ├── wired.html               # Wired Media MCQs
    │       └── wireless.html            # Wireless Media MCQs
    ├── theory-of-computation.html       # Theory of Computation MCQs
    ├── artificial-intelligence.html     # Artificial Intelligence MCQs
    ├── computer-network.html            # Computer Networks MCQs
    └── programming.html                 # Programming Fundamentals MCQs
```

---

## ✏️ How to Add a New Question

Adding a question is as simple as copy-pasting HTML. You **never** need to touch JavaScript or databases!

1. Open any subject HTML file (e.g. `subjects/data-communication.html`).
2. Inside any `<section class="topic-section">`, add:

```html
<div class="question-card" data-answer="B">
  <div class="question-header">
    <span class="q-number">Q11</span>
    <span class="q-topic-tag">Topic Name</span>
  </div>
  <h3 class="question-text">Your question text goes here?</h3>
  <div class="options-grid">
    <label class="option-label">
      <input type="radio" name="q11" value="A">
      <span class="option-letter">A</span>
      <span class="option-text">Option A text</span>
    </label>
    <label class="option-label">
      <input type="radio" name="q11" value="B">
      <span class="option-letter">B</span>
      <span class="option-text">Option B text (Correct)</span>
    </label>
    <label class="option-label">
      <input type="radio" name="q11" value="C">
      <span class="option-letter">C</span>
      <span class="option-text">Option C text</span>
    </label>
    <label class="option-label">
      <input type="radio" name="q11" value="D">
      <span class="option-letter">D</span>
      <span class="option-text">Option D text</span>
    </label>
  </div>
  <div class="question-feedback"></div>
</div>
```

3. Set `data-answer` to the correct option letter (`A`, `B`, `C`, or `D`).
4. Save the file! The quiz engine automatically updates question counts, evaluation, and progress bars.

---

## ➕ How to Add a New Subject

1. Create a new HTML file inside `subjects/` (e.g., `subjects/operating-systems.html`).
2. Copy the boilerplate from an existing subject file.
3. On `index.html`, add a new card linking to your subject:

```html
<article class="subject-card">
  <div class="subject-card-top">
    <div class="subject-icon-box">💻</div>
    <h3 class="subject-card-title">Operating Systems</h3>
    <p class="subject-card-desc">Processes, threads, CPU scheduling, deadlocks, and memory management.</p>
    <div class="subject-meta">
      <span class="subject-meta-tag">4 Topics</span>
      <span class="subject-meta-tag">MCQs Included</span>
    </div>
  </div>
  <a href="subjects/operating-systems.html" class="btn btn-primary btn-block">Open Subject</a>
</article>
```

---

## 🌐 Deploy to GitHub Pages

1. Push this repository to GitHub.
2. Go to **Settings** → **Pages**.
3. Under **Branch**, select `main` and root `/`.
4. Click **Save**. Your site will be live within seconds!
