warning

One proper noun requires inline identification for readers unfamiliar with Claude tooling.

---

**CLAUDE.md** (line 15, first mention): "A codebase gains a new review criterion by describing it in CLAUDE.md, not by writing a linter rule."

CLAUDE.md is introduced as if universally known, but it is a Claude Code-specific convention (a project-level instruction file that the Claude Code agent reads on startup). A reader not already using Claude Code would not know what kind of artifact CLAUDE.md is or why it controls agent behavior.

Recommended fix: brief inline identification on first use, e.g., "CLAUDE.md (the Claude Code project instruction file)."

---

**Lisp, Emacs, and Smalltalk** (line 45): "This is the same property that makes Lisp, Emacs, and Smalltalk extensible from within."

These are proper nouns (two programming languages and a text editor) used without inline identification. For the likely audience of this KB (people building agent systems), all three are broadly known. The note does not need to attribute them to organizations or describe them in detail. This is a weak observation rather than a clear failure — the names serve as examples and the meaning of the sentence does not depend on knowing exactly what they are.

---

All other references in the note are generic (CI pipeline, GitHub Action, sub-agent) or are KB-internal terms (enforcement gradient, distillation) covered by note links.
