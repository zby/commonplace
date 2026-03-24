<!-- REVIEW-METADATA
note-path: kb/notes/three-space-memory-separation-predicts-measurable-failure-modes.md
last-full-review-note-sha: 2aaae23d3756fc6700781d6d72145280ba2dfa6c
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T20:57:19+01:00
last-accepted-note-sha: 2aaae23d3756fc6700781d6d72145280ba2dfa6c
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T20:57:19+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: three-space-memory-separation-predicts-measurable-failure-modes.md ===

Checks applied: 4

WARN:
- [Description discrimination] Description "The three-space memory claim is testable because flat memory predicts specific cross-contamination failures" partially overlaps the title's "predicts measurable failure modes" with "predicts specific cross-contamination failures." The added value is the "flat memory" framing and "cross-contamination" specificity, but "testable" restates "measurable." A stronger description would lead with scope or implication — e.g., what the observation protocol targets (search pollution, identity scatter, insight trapping) or the scale threshold question, rather than re-asserting testability.
  Recommendation: Rewrite the description to foreground either the three concrete failure modes (search pollution, identity scatter, insight trapping) or the scale-dependency question, since those are the discriminators an agent searching for "memory separation" or "failure modes" would need to pick this note from results.

INFO:
- [Description discrimination] The description says "flat memory predicts specific cross-contamination failures" — strictly, it is the three-space model that predicts flat memory will exhibit these failures. The inversion is understandable but slightly misleading on a quick scan.

CLEAN:
- [Title composability] "since three-space memory separation predicts measurable failure modes, we designed an observation protocol..." reads naturally as a linked sentence fragment. The title works as a composable prose reference.
- [Claim strength] The claim is specific and contestable. The note itself names the counter-position ("the boring explanation" where separation is mere file hygiene, not cognitive architecture) and acknowledges the failure modes may not manifest at small scale. A knowledgeable reader could argue that flat memory with good tagging avoids these failures without structural separation.
- [Title-body alignment] The title promises that three-space separation predicts measurable failure modes; the body delivers exactly that — three named failure modes from the Cornelius article, an observation protocol for measuring them, criteria for confirming or disconfirming the prediction, and open questions about scale thresholds. The observation protocol and evidence criteria are natural extensions of "measurable," not scope drift.

Overall: 1 warning, 1 info
===
