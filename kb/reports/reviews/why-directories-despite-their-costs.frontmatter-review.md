<!-- REVIEW-METADATA
note-path: kb/notes/why-directories-despite-their-costs.md
last-full-review-note-sha: 6f593e9f705987eb3548fdc8708acce03b690973
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:57:53+01:00
last-accepted-note-sha: 6f593e9f705987eb3548fdc8708acce03b690973
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:57:53+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: why-directories-despite-their-costs.md ===

Checks applied: 4

INFO:
- [Title composability] The "Why X despite Y" question form is slightly awkward as a linkable clause — "since why directories despite their costs" doesn't parse. It does work as a reference ("see [why directories despite their costs]") and the question form suits the exploratory, trade-off-weighing character of the note. A claim-form alternative like "directories are worth their costs up to moderate scale" would compose better, but given `status: seedling` this is not urgent.

CLEAN:
- [Description discrimination] The description adds mechanism (orders of magnitude of human-navigable scale, local conventions per subsystem) and scope of costs (routing, search config, skills, cross-directory linking) that the question-form title cannot carry. Strong discriminator — an agent seeing five results about directory organization would immediately know this note provides a cost/benefit trade-off analysis with concrete operational costs enumerated.
- [Claim strength] The title is a question, not a claim, so the claim-strength check applies loosely. The note's `status: seedling` and exploratory structure (weighing trade-offs, arriving at a stance rather than asserting one upfront) make a question title appropriate. No false claim issue.
- [Title-body alignment] The title promises an explanation of why directories are used despite costs. The body delivers: benefits (scale without tooling, local conventions, metabolic separation), the types-vs-directories orthogonality argument, a detailed cost catalog (7 items), and a current stance with mitigations. Tight alignment.

Overall: 0 warnings, 1 info
===
