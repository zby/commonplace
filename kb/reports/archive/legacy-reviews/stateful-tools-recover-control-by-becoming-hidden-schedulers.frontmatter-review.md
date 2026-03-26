<!-- REVIEW-METADATA
note-path: kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md
last-full-review-note-sha: 9fbb46263da8a9d2c9effe957282df563320cfde
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T20:56:58+01:00
last-accepted-note-sha: 9fbb46263da8a9d2c9effe957282df563320cfde
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T20:56:58+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: stateful-tools-recover-control-by-becoming-hidden-schedulers.md ===

Checks applied: 4

CLEAN:
- [description-discrimination] Description adds mechanism beyond the title. Title says stateful tools recover control by becoming hidden schedulers; description specifies the mechanism — "recovered control comes from relocating the scheduler into an exceptional tool or runtime, not from the framework loop itself." The "not from the framework loop itself" clause discriminates this note from adjacent notes about framework loops generally.
- [title-composability] "since stateful tools recover control by becoming hidden schedulers, the question becomes where the scheduler lives" reads naturally as a prose fragment. Full clause, no awkward grammar.
- [claim-strength] The claim is specific and contestable. Someone could argue that stateful tools do not truly recover control (they just hide complexity), or that the recovery mechanism is not well-characterized as "becoming schedulers." The note's seedling status would excuse a softer claim, but this one already has teeth.
- [title-body-alignment] The body supports exactly the title's claim: it walks through how a sufficiently stateful tool recovers orchestration control, then reframes the question to where the scheduler lives. No drift — the title promises a mechanism analysis and the body delivers it, including the limits of the recovery (action alphabet changes, context-window exceedance).

Overall: CLEAN
===
