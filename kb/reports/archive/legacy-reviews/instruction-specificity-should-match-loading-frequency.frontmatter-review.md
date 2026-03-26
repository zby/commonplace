<!-- REVIEW-METADATA
note-path: kb/notes/instruction-specificity-should-match-loading-frequency.md
last-full-review-note-sha: 7e9624d2815f8f4421e0f9bd30f5f3eb78b97df5
last-full-review-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-full-review-at: 2026-03-24T20:55:22+01:00
last-accepted-note-sha: 7e9624d2815f8f4421e0f9bd30f5f3eb78b97df5
last-accepted-note-commit: 6e2e74d37a330987366c2d846513e4b52f97a11f
last-accepted-at: 2026-03-24T20:55:22+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: instruction-specificity-should-match-loading-frequency.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry: it names the concrete 4-tier loading hierarchy ("CLAUDE.md -> skill descriptions -> skill bodies -> task docs") and states the practical consequence ("always-loaded context competes for attention every session"). Against a list of search results about context loading or progressive disclosure, this description would clearly identify the note as the one about the specific tiered hierarchy and its design rationale.

- [Title composability] "since instruction specificity should match loading frequency, we designed the CLAUDE.md as a slim router" reads naturally as a sentence fragment. The title functions well as a linkable prose phrase.

- [Claim strength] The claim is non-obvious and contestable. Someone could reasonably argue that all instructions should be always-loaded for reliability (eliminating the risk of missing a needed instruction), or that loading frequency should be driven by task type rather than instruction specificity. The note argues a specific design principle rather than a truism.

- [Title-body alignment] The body directly supports the title's claim. It establishes a 4-tier loading hierarchy, explains the progressive disclosure principle, and gives concrete examples of what belongs at each level (universal rules in CLAUDE.md, task-specific rules in targeted files). No drift between title promise and body delivery.

Overall: CLEAN
===
