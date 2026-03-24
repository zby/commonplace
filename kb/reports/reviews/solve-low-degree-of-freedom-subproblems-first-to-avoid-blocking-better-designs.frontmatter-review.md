<!-- REVIEW-METADATA
note-path: kb/notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md
last-full-review-note-sha: 8a83e2b64e374af8aee083f0f7b094688685e42b
last-full-review-note-commit: c5670f42129a9b389e107404846653de1c8c7167
last-full-review-at: 2026-03-24T20:56:49+01:00
last-accepted-note-sha: 8a83e2b64e374af8aee083f0f7b094688685e42b
last-accepted-note-commit: c5670f42129a9b389e107404846653de1c8c7167
last-accepted-at: 2026-03-24T20:56:49+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md ===

Checks applied: 4

INFO:
- [Title composability] The imperative verb opening ("Solve low-degree-of-freedom...") makes "since [title]..." slightly awkward: "since solve low-degree-of-freedom subproblems first..." is not grammatical without inserting an implied subject. A declarative form (e.g., "low-degree-of-freedom subproblems should be solved first...") would compose more smoothly in link contexts.
  Recommendation: Consider rephrasing to a declarative claim if the title is revised for other reasons; not urgent since the imperative form is a recognizable pattern and the meaning is clear.

CLEAN:
- [Description discrimination] Description adds mechanism ("commit first to decisions with the fewest viable options, then place flexible choices around them") and implication ("preserve global optionality") beyond the title's claim. It also frames the note as an "ordering heuristic for decomposition," giving context. Discriminates well from related notes on decomposition or Alexander patterns.
- [Claim strength] The ordering heuristic is specific and non-obvious — someone could reasonably advocate solving the highest-value or easiest subproblem first, or argue that degrees of freedom are too hard to estimate upfront. The claim carries real information.
- [Title-body alignment] The body establishes exactly what the title promises: it explains the heuristic via the kitchen example, generalizes it to a constrained-search sequencing rule, and applies it to agent workflows. No drift detected.

Overall: 0 warnings, 1 info
===
