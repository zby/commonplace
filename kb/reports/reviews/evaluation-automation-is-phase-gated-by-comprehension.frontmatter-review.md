<!-- REVIEW-METADATA
note-path: kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md
last-full-review-note-sha: 00a2aee140c0d902b2f587f53a90b28d703ea2a7
last-full-review-note-commit: 0fb6abb05758625dcd0af533b14a6532d84fbd24
last-full-review-at: 2026-03-24T20:54:57+01:00
last-accepted-note-sha: 00a2aee140c0d902b2f587f53a90b28d703ea2a7
last-accepted-note-commit: 0fb6abb05758625dcd0af533b14a6532d84fbd24
last-accepted-at: 2026-03-24T20:54:57+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: evaluation-automation-is-phase-gated-by-comprehension.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description ("Optimization loops require manual error analysis and judge calibration before automation can improve behavior rather than just score") adds mechanism (manual error analysis and judge calibration) and implication (improve behavior rather than just score) beyond what the title carries. The title names the gate; the description explains what the gate requires and what happens without it. Strong discriminator in a search for evaluation or automation notes.
- [Title composability] "since evaluation automation is phase-gated by comprehension, we enforce explicit verifier-construction gates before optimization" reads naturally as a prose fragment. The title composes well as a linkable clause.
- [Claim strength] The claim that automation is phase-gated by comprehension is contestable: a practitioner could argue that automated discovery of failure modes (e.g., clustering model outputs) can substitute for manual comprehension, or that starting with automated evals and iterating is faster. The note argues a specific sequencing dependency that is non-obvious.
- [Title-body alignment] The body establishes a three-phase sequence (comprehension, specification, generalization) where comprehension is the first gate. The "Practical implication" section reinforces the gating claim with concrete stage gates. The body directly supports the title's assertion.

Overall: CLEAN
===
