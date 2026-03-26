<!-- REVIEW-METADATA
note-path: kb/notes/indirection-is-costly-in-llm-instructions.md
last-full-review-note-sha: be0292335f5208c66c204d1c13c0b4caaf71b3f8
last-full-review-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-full-review-at: 2026-03-24T20:55:16+01:00
last-accepted-note-sha: be0292335f5208c66c204d1c13c0b4caaf71b3f8
last-accepted-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-accepted-at: 2026-03-24T20:55:16+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: indirection-is-costly-in-llm-instructions.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism (interpretation overhead on every read) and scope (contrast with code where indirection is nearly free at runtime). It goes well beyond the title and would clearly differentiate this note from related results about LLM instruction design.
- [Title composability] "since indirection is costly in LLM instructions, we resolve variables at build time" reads naturally as a sentence fragment. Composes well as a link anchor.
- [Claim strength] The claim that indirection is costly in LLM instructions is specific and non-obvious -- it identifies a cost-model difference between traditional programming and prompt authoring that someone could reasonably contest (e.g., arguing LLMs handle variable substitution fine, or that flexibility outweighs the overhead). Not a truism.
- [Title-body alignment] The body delivers exactly what the title promises: it establishes why indirection is costly (context competition, interpretive overhead, error risk), contrasts with the code cost model, identifies specific indirection patterns, proposes build-time resolution as the fix, and draws the boundary between eliminable and necessary indirection. No drift.

Overall: CLEAN
===
