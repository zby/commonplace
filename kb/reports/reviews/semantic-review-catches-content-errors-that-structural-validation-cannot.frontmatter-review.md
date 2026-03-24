<!-- REVIEW-METADATA
note-path: kb/notes/semantic-review-catches-content-errors-that-structural-validation-cannot.md
last-full-review-note-sha: 8fa0305db3e4941314dd61476e7e9a87d0bab39c
last-full-review-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-full-review-at: 2026-03-24T20:56:37+01:00
last-accepted-note-sha: 8fa0305db3e4941314dd61476e7e9a87d0bab39c
last-accepted-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-accepted-at: 2026-03-24T20:56:37+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: semantic-review-catches-content-errors-that-structural-validation-cannot.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism (LLM adversarial reading), scope (four named checks: enumeration completeness, grounding alignment, boundary-case coverage, internal consistency), and a concrete failure mode example (incomplete enumerations contradicting their own grounding definitions). None of this is recoverable from the title alone. Strong discriminator in a list of search results.
- [Title composability] "since semantic review catches content errors that structural validation cannot, we designed..." reads naturally as a sentence fragment. No awkwardness.
- [Claim strength] The claim that a class of content errors exists beyond structural validation's reach is specific and contestable — someone could argue that sufficiently rich schemas or deterministic heuristics could approximate these checks. The note names four concrete checks and a motivating case, giving the claim real content. Additionally, the note's `status: seedling` provides further exception room.
- [Title-body alignment] The body delivers exactly what the title promises: a motivating case of a content error that passed structural validation, four specific semantic checks that structural validation cannot perform, their placement in the testing pyramid, and the review skill as implementation target. No drift in either direction.

Overall: CLEAN
===
