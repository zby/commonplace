<!-- REVIEW-METADATA
note-path: kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md
last-full-review-note-sha: 5c428a69e09d5d16662c2c4e75e5a0be98ef35f6
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T20:57:48+01:00
last-accepted-note-sha: 5c428a69e09d5d16662c2c4e75e5a0be98ef35f6
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T20:57:48+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: unified-calling-conventions-enable-bidirectional-refactoring.md ===

Checks applied: 4

WARN:
(none)

INFO:
(none)

CLEAN:
- [description-discrimination] Description adds mechanism ("name-based dispatch over a hybrid VM") and a concrete exemplar (llm-do) beyond what the title carries. It also names the key implication ("without changing call sites"). Strong discriminator against other notes about calling conventions or refactoring.
- [title-composability] "since unified calling conventions enable bidirectional refactoring between neural and symbolic..." reads naturally as a sentence fragment in linking contexts.
- [claim-strength] The claim is specific and contestable — someone could argue that calling conventions are insufficient because the real barrier is semantic (type mismatches between unstructured LLM output and typed function signatures), or that unified conventions are superficial without deeper structural alignment. The claim takes a concrete position.
- [title-body-alignment] The body establishes the core claim through the llm-do hybrid VM mechanism, then demonstrates bidirectionality with both the codification direction (neural to symbolic) and the relaxing direction (symbolic to neural). The scheduler and typed-callables sections extend beyond the title's strict scope but are clearly framed as additional layers, not alternative claims.

Overall: CLEAN
===
