<!-- REVIEW-METADATA
note-path: kb/notes/scenarios.md
last-full-review-note-sha: 101f022f5f2ccae8d87f0619f3137e665c05c4b4
last-full-review-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-full-review-at: 2026-03-24T20:56:30+01:00
last-accepted-note-sha: 101f022f5f2ccae8d87f0619f3137e665c05c4b4
last-accepted-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-accepted-at: 2026-03-24T21:37:27+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: scenarios.md ===

Checks applied: 4

WARN:
- [Title composability] Title is the bare topic word "Scenarios" — it cannot compose into a sentence fragment. "since scenarios..." or "because scenarios..." is grammatically incomplete. A composable alternative might be "the knowledge system serves two concrete scenarios" or similar claim-form title that works as a linkable phrase.
  Recommendation: Rewrite the title as a composable phrase or claim that names what the scenarios are for, e.g. "upstream change analysis and own-change proposals are the knowledge system's primary scenarios".

- [Title-body alignment] The title "Scenarios" is scope-drifted broad — it could refer to scenarios for anything. The body is specifically about two knowledge-system use cases: upstream change analysis and proposing own changes. The description carries this specificity ("Concrete use cases for the knowledge system — upstream change analysis and proposing our own changes") but the title does not.
  Recommendation: Narrow the title to match the body's actual scope. Even a topical title like "knowledge system usage scenarios" would reduce the mismatch; a claim-form title would be better still.

INFO:
- [Claim strength] The title is topical rather than a claim, which is not inherently wrong — but the note's type is `note` and status is `current`, and it doesn't fit the standard exceptions for topical titles (it is not an index, definitional note, multi-claim spec, or seedling). The note argues a specific point — that step 4 (grounding comments in evidence) is where the KB earns its keep — which could be elevated into the title as a testable claim.

CLEAN:
- [Description discrimination] Description "Concrete use cases for the knowledge system — upstream change analysis and proposing our own changes" adds clear retrieval value beyond the title. It names the two specific scenarios and identifies what they are use cases *for* (the knowledge system). An agent seeing this in a list of 5 results could confidently pick or skip it.

Overall: 2 warnings, 1 info
===
