<!-- REVIEW-METADATA
note-path: kb/notes/interpretation-errors-are-failures-of-the-interpreter.md
last-full-review-note-sha: 448515250548aeb21d2b18438f217db6f2861119
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:55:30+01:00
last-accepted-note-sha: 448515250548aeb21d2b18438f217db6f2861119
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:55:30+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: interpretation-errors-are-failures-of-the-interpreter.md ===

Checks applied: 4

WARN:

INFO:
- [claim-strength] The title "Interpretation errors are failures of the interpreter" reads as near-tautological on the surface — the word "interpretation" already implicates the interpreter. The actual claim is that these errors are a property of the interpreter itself (as opposed to the spec or the sampling process), which is contestable within the three-phenomena framework. The surface phrasing obscures this. A sharper title might foreground the contrast, e.g. "interpretation errors are irreducible to underspecification or sampling noise" or "real interpreters fail in ways the idealised model omits."
  Note: seedling status makes this low-priority; the current title is adequate for early-stage development.

CLEAN:
- [description-discrimination] The description adds mechanism (three concrete failure modes: constraint violation, hallucination, bookkeeping failure) and scope (absent from the idealised two-phenomena model). It does not restate the title. An agent seeing this description in a list of results about LLM errors would know this note covers the third phenomenon — interpreter-intrinsic failures — and how it extends the two-phenomena model. Strong discrimination.
- [title-composability] "since interpretation errors are failures of the interpreter, the remedy is error detection not spec narrowing" reads naturally as a sentence fragment. The title composes well as a linkable clause.
- [title-body-alignment] The body establishes exactly what the title claims: a class of LLM errors that are properties of the interpreter itself, distinct from underspecification and indeterminism. The examples (constraint violation, hallucination, bookkeeping failure, content bias, emotional prompt sensitivity) all demonstrate interpreter failure on fully specified tasks. The "Why this matters" section reinforces the title by explaining why distinct remedies follow. No drift detected.

Overall: 0 warnings, 1 info
===
