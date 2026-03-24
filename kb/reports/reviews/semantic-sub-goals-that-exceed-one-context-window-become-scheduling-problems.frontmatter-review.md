<!-- REVIEW-METADATA
note-path: kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md
last-full-review-note-sha: dec45995e13d4c20772c4e43a32654d22f9916c4
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T20:56:38+01:00
last-accepted-note-sha: dec45995e13d4c20772c4e43a32654d22f9916c4
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T20:56:38+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md ===

Checks applied: 4

INFO:
- [Description discrimination] The description's first clause — "Some semantic subgoals exceed one context window" — restates the title's premise, consuming about half the description budget on redundant information. The second clause adds genuine mechanism (partitioning into smaller judgments with symbolic collection, filtering, staged summarization), which discriminates well. Dropping the redundant prefix would free space for additional scope or implication content, such as the recursive nature of the pattern or the mid-task discovery dynamic.
  Recommendation: Lead with the mechanism directly, e.g. "Overflow forces a symbolic loop — partition the working set, run bounded semantic judgments, aggregate deterministically — making the parent goal a scheduling problem that can recurse when aggregation itself overflows."

CLEAN:
- [Title composability] "since semantic sub-goals that exceed one context window become scheduling problems, we designed..." reads naturally as a linked prose fragment. The title works as a complete clause.
- [Claim strength] The claim is specific and contestable — someone could argue that larger context windows eliminate the problem, that retrieval-based approaches avoid scheduling entirely, or that the result is a parallelization problem rather than a scheduling one. The note is also marked `status: seedling`, which would excuse a weaker claim, but the claim is strong regardless.
- [Title-body alignment] The body directly supports the title's claim. It establishes the mechanism (symbolic loops: partition, judge, aggregate), gives two concrete scenarios (collection work and corpus contradiction detection), explains the recursive case, and discusses framework consequences. All content stays within the title's scope.

Overall: 0 warnings, 1 info
===
