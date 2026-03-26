<!-- REVIEW-METADATA
note-path: kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md
last-full-review-note-sha: 7e1f2be5d64dc183efe0e959a6cfc00816c6c212
last-full-review-note-commit: d4237bd4b4d2593667e2675f27766515cdacba25
last-full-review-at: 2026-03-24T20:55:00+01:00
last-accepted-note-sha: 7e1f2be5d64dc183efe0e959a6cfc00816c6c212
last-accepted-note-commit: d4237bd4b4d2593667e2675f27766515cdacba25
last-accepted-at: 2026-03-24T20:55:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: execution-indeterminism-is-a-property-of-the-sampling-process.md ===

Checks applied: 4

CLEAN:
- [description-discrimination] The description adds both scope ("theoretically eliminable but practically ubiquitous") and context ("often confused with the deeper issue of underspecification") beyond what the title carries. An agent seeing this among search results would know immediately that the note covers the practical status of indeterminism and its relationship to underspecification, not just a definitional claim about sampling.
- [title-composability] "since execution indeterminism is a property of the sampling process, we designed sampling controls rather than spec changes" reads naturally as a sentence fragment. The title composes well.
- [claim-strength] The claim that indeterminism is a property of the sampling process (not the specification) is genuinely contestable — someone could argue that infrastructure non-determinism (floating-point, batching) means it is not purely a sampling property, or that the indeterminism/underspecification boundary is blurrier than the note claims. The note's seedling status further lowers the bar, but the claim clears it regardless.

INFO:
- [title-body-alignment] The title anchors on the mechanical origin of indeterminism ("property of the sampling process"), but the body's main argumentative weight falls on a different point: that indeterminism obscures the deeper problem of underspecification. The "Why this matters as a distinct claim" section — the note's most substantive content — argues that people misattribute underspecification effects to randomness. A title like "execution indeterminism obscures the deeper problem of underspecification" would better match the body's center of gravity. Not a misalignment — the current title is accurate — but it foregrounds the less novel part of the note.

Overall: 0 warnings, 1 info
===
