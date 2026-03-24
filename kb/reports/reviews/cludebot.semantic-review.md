<!-- REVIEW-METADATA
note-path: kb/notes/related-systems/cludebot.md
last-full-review-note-sha: 11939ec1c9072c9677570654e590808886f2887f
last-full-review-note-commit: n/a (untracked)
last-full-review-at: 2026-03-24T22:10:04+01:00
last-accepted-note-sha: 11939ec1c9072c9677570654e590808886f2887f
last-accepted-note-commit: n/a (untracked)
last-accepted-at: 2026-03-24T22:10:04+01:00
last-acceptance-kind: full-review
review-type: semantic-review
-->

=== SEMANTIC REVIEW: cludebot.md ===

Claims identified: 13

WARN:
- (none)

INFO:
- [completeness] The review says "six-phase dream cycle" while the README says "Five phases." The code confirms six (`runConsolidation`, `runCompaction`, `runReflection`, `runContradictionResolution`, `runLearning`, `runEmergence`). The README is outdated; the review is correct per the implementation.
- [completeness] "Richest reviewed trajectory-to-lesson learning loop" — this is a comparative claim across the KB's related-system reviews. ExpeL has explicit ADD/EDIT/REMOVE rule maintenance, which is arguably richer in lifecycle management. Cludebot's action learning has the richest *oracle* (social engagement metrics as real-world outcome signal). The claim is defensible if interpreted as "richest end-to-end closed loop with a real-world oracle" rather than "richest rule lifecycle."

PASS:
- [grounding] All five decay rates (0.93, 0.98, 0.97, 0.99, 0.98) verified against `DECAY_RATES` in `src/utils/constants.ts`.
- [grounding] All retrieval weights (vector 4.0, relevance 2.0, importance 2.0, recency 1.0, graph 1.5) verified against `RETRIEVAL_WEIGHT_*` constants.
- [grounding] Six dream cycle phases verified in `triggerReflection()` at line 126-137 of `dream-cycle.ts`.
- [grounding] Local store line count (362) matches "under 400 lines" claim.
- [grounding] Clinamen divergence formula `importance * (1 - vectorSimilarity)` verified at line 159 of `clinamen.ts`.
- [grounding] Cop-out patterns verified as regex array at lines 30-37 of `dream-cycle.ts`.
- [grounding] Entity extraction heuristics (Twitter handles, Solana addresses, token tickers, capitalized names) verified in `extractEntitiesFromText()` at line 328 of `memory-graph.ts`.
- [internal-consistency] All sections align: Core Ideas mechanisms are honestly assessed in Curiosity Pass, comparison table matches prose, borrowable ideas reference mechanisms described in Core Ideas.
- [internal-consistency] No definition drift detected — terms used consistently throughout.

Overall: CLEAN (0 warnings, 2 info)
===
