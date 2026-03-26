<!-- REVIEW-METADATA
note-path: kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md
last-full-review-note-sha: 5574c21c110c6f2a8dd1a6a696ab4fe54a6d0d66
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:56:25+01:00
last-accepted-note-sha: 5574c21c110c6f2a8dd1a6a696ab4fe54a6d0d66
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:56:25+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: reliability-dimensions-map-to-oracle-hardening-stages.md ===

Checks applied: 4

WARN:
- [Title-body alignment] The title says "map to oracle-hardening stages," implying a sequential ordering (stage 1, stage 2, ...). The body presents the four dimensions as independent oracles that "can be hardened independently" and explicitly states "You don't need to solve all four at once." The mapping is dimension-to-oracle-question, not dimension-to-sequential-stage. The body also notes safety "is the only dimension that's already a hard oracle by design," which further breaks any stage metaphor.
  Recommendation: Replace "stages" with a word that conveys parallel independent targets rather than sequential progression — e.g., "reliability dimensions map to independent oracle-hardening targets" or simply "reliability dimensions map to oracle-hardening moves."

CLEAN:
- [Description discrimination] The description adds source attribution (Rabanser et al.), enumerates the four dimensions (consistency, robustness, predictability, safety), and frames the mapping as connecting "empirical agent evaluation" to the oracle-strength spectrum. Against other oracle-strength or reliability notes, an agent could pick this one from a search list. Adds mechanism and scope beyond what the title carries.
- [Title composability] "since reliability dimensions map to oracle-hardening stages, we can harden each oracle independently" reads naturally as a sentence fragment. The title functions as a linkable clause.
- [Claim strength] The mapping is specific and contestable — someone could argue the dimensions don't cleanly map (the note itself acknowledges safety behaves differently as a gate rather than a gradient). This is a substantive architectural claim, not a truism. Seedling status noted but not relevant since the claim is already sharp.

Overall: 1 warning, 0 info
===
