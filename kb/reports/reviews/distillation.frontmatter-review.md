<!-- REVIEW-METADATA
note-path: kb/notes/distillation.md
last-full-review-note-sha: c4db1940c1e576f904a4b81a562ff4006ebb47bc
last-full-review-note-commit: 4b0a5b5c6b7f2e9038cb8832b099366508412131
last-full-review-at: 2026-03-24T20:54:38+01:00
last-accepted-note-sha: c4db1940c1e576f904a4b81a562ff4006ebb47bc
last-accepted-note-commit: 4b0a5b5c6b7f2e9038cb8832b099366508412131
last-accepted-at: 2026-03-24T20:54:38+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: distillation.md ===

Checks applied: 4

WARN:
- [Title composability] Title is a bare noun ("Distillation") — "since distillation..." does not read as a complete clause. The note is definitional/term-pinning, which exempts it from the claim-strength check, but bare-noun titles still compose poorly as link targets. Other notes currently link to it with inline context (e.g., "[constraining](./constraining.md) — co-equal mechanism"), which works but means every linker must supply its own gloss.
  Recommendation: Consider a composable title such as "distillation compresses knowledge for bounded consumers" — this would let links read naturally without per-link annotation. If the term-pinning role is more important than composability, keep the current title and treat this as an accepted trade-off.

CLEAN:
- [Description discrimination] Description "Definition — distillation compresses knowledge so a consumer can act on it within bounded context, making operations feasible that raw source material would exceed; co-equal learning mechanism alongside constraining" adds mechanism (compression for bounded context), implication (feasibility, not just optimization), and positioning (co-equal with constraining). Against 5 search results for "distillation," this clearly identifies the definitional note for the KB-specific sense of the term.
- [Claim strength] Title is topical, not phrased as a claim. The note is definitional (term pinning) — topical titles are correct for this purpose per the exceptions list.
- [Title-body alignment] Topical title "Distillation" promises a definitional treatment. The body delivers exactly that: a definition, relationship to context engineering, prior work survey, operational mechanics with examples, orthogonality to constraining, and ML terminology disambiguation. No scope or claim drift.

Overall: 1 warning, 0 info
===
