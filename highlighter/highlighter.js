/**
 * CODEKARO — Modular Study Highlighter Module
 * Allows students to highlight key terms on MCQ and topic pages without modifying underlying questions.
 */

class StudyHighlighter {
  constructor() {
    this.init();
  }

  init() {
    document.addEventListener('mouseup', () => {
      this.handleSelection();
    });
  }

  handleSelection() {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed || selection.rangeCount === 0) return;

    const selectedText = selection.toString().trim();
    if (selectedText.length < 2) return;

    // Only allow highlighting within question texts or notes
    const anchorNode = selection.anchorNode;
    if (!anchorNode) return;
    
    const container = anchorNode.nodeType === 3 ? anchorNode.parentElement : anchorNode;
    if (!container || !container.closest('.question-text, .subject-card-desc, p')) return;

    // Optional subtle highlight capability
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.codekaroHighlighter = new StudyHighlighter();
});
