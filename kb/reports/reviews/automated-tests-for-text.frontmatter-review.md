<!-- REVIEW-METADATA
note-path: kb/notes/automated-tests-for-text.md
last-full-review-note-sha: 4997ca8f5bd52e3d2c569870e14c90c8c1791d32
last-full-review-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-full-review-at: 2026-03-24T20:53:42+01:00
last-accepted-note-sha: 4997ca8f5bd52e3d2c569870e14c90c8c1791d32
last-accepted-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-accepted-at: 2026-03-24T20:53:42+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: automated-tests-for-text.md ===

Checks applied: 4

INFO:
- [Title composability] The title "Automated tests for text" is a bare topic noun phrase. "since automated tests for text..." does not read as a natural sentence fragment. As a reference link ("see [automated tests for text](...)") it works fine, and the note is a framework note where topical titles are acceptable — but a claim-shaped title like "text artifacts can be tested with the same pyramid as software" would compose better and carry more information at link sites.

CLEAN:
- [Description discrimination] The description adds mechanism (test pyramid with three named levels: deterministic checks, LLM rubrics, corpus compatibility) and a design principle ("built from real failures not taxonomy") that the title cannot carry. An agent choosing among search results would easily identify this note from the description alone.
- [Claim strength] The title is topical, not a claim. This is appropriate: the note describes a multi-level testing framework rather than arguing a single point. Topical titles are correct for framework notes per the exceptions list.
- [Title-body alignment] The body delivers exactly what the title promises — a framework for automated testing of text artifacts. It covers the test pyramid, the connection to document types, the design principle, and the current implementation status. No drift detected.

Overall: 0 warnings, 1 info
===
