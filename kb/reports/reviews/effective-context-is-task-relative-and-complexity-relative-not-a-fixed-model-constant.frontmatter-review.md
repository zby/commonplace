<!-- REVIEW-METADATA
note-path: kb/notes/effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md
last-full-review-note-sha: a42b85121e43b94423e9e67a884be02884fa81d5
last-full-review-note-commit: 6b5b381a4b973131eb8ebd0e202a9057a5f97dd9
last-full-review-at: 2026-03-24T20:54:46+01:00
last-accepted-note-sha: a42b85121e43b94423e9e67a884be02884fa81d5
last-accepted-note-commit: 6b5b381a4b973131eb8ebd0e202a9057a5f97dd9
last-accepted-at: 2026-03-24T20:54:46+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md ===

Checks applied: 4

CLEAN:
- [description-discrimination] Description names the three specific sources synthesized (Paulsen MECW, ConvexBench, two-axis context-cost model), adds mechanism ("usable context varies with task type and prompt difficulty"), and states an implication ("nominal window size is a misleading abstraction"). An agent seeing this among search results for "effective context" or "context window" would immediately know this is the synthesis note grounding the claim in those two empirical sources, not a generic note about context limits. Strong discrimination.
- [title-composability] "since effective context is task-relative and complexity-relative not a fixed model constant, we designed..." reads naturally as a prose fragment. The title composes well as a linkable claim.
- [claim-strength] The claim is non-trivial: someone could reasonably argue that a model's context window is a meaningful fixed constant (vendors advertise it as such, benchmarks report it as a scalar). The note argues against that default assumption with specific empirical evidence. Not a truism.
- [title-body-alignment] The title promises that effective context depends on task type and complexity rather than being a fixed model property. The body delivers exactly this: it presents Paulsen's MECW findings (volume varies by task type) and ConvexBench (complexity dominates at trivial token counts), then synthesizes them into the relational claim. The caveats section appropriately scopes the evidence. No drift detected.

Overall: CLEAN
===
