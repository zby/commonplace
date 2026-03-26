<!-- REVIEW-METADATA
note-path: kb/notes/llm-context-is-a-homoiconic-medium.md
last-full-review-note-sha: c627bda889595df6c56a62a3269278b5c754fcf1
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:55:43+01:00
last-accepted-note-sha: c627bda889595df6c56a62a3269278b5c754fcf1
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:55:43+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: llm-context-is-a-homoiconic-medium.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("instructions and data share the same representation (natural language tokens)"), implication ("no structural boundary between program and content, producing both the extensibility benefits and the scoping hazards"), and concrete scope markers ("Lisp, Emacs, and Smalltalk"). An agent seeing five results about LLM context properties could pick this note from the description alone.
- [Title composability] "since LLM context is a homoiconic medium, we need structural boundaries imposed from outside" reads naturally as a sentence fragment. The title works as a linkable clause.
- [Claim strength] The claim that LLM context is homoiconic is genuinely contestable -- one could argue homoiconicity requires first-class eval/quote operations on the shared representation, not merely a shared surface format (text). The analogy to Lisp is specific and non-obvious enough to carry information. The note's seedling status would also exempt it from strict claim-strength requirements, but the claim holds on its own merits.
- [Title-body alignment] The title claims LLM context is a homoiconic medium. The body defines what that means (instructions and data share representation), establishes precedents (Lisp, Emacs, Smalltalk, Prolog, Tcl, Rebol/Red, XSLT), then traces consequences in both directions (extensibility benefits and scoping/injection/discoverability costs). The body delivers exactly what the title promises, with no drift in either direction.

Overall: CLEAN
===
