---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/theory/COLLECTION.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 1894ffdc7fc7462fbdad3a7407fa593c
completed-at: '2026-11-22T21:52:40Z'
findings:
- scope: passage
  quotes:
  - '— defines: the three forms this note ranges over'
  reason: '`defines` is not in the collection''s label table. The registered label
    for a link to a term in `theory/definitions/` is `defined-in`.'
  level: warn
- scope: passage
  quotes:
  - '— sharpens: the unit those cross-form writes range over'
  - '— sharpens: the discriminator between evidence-responsive learning writes'
  reason: '`sharpens` is not in the collection''s label table. Footer edges must use
    one of the listed labels, such as `extends`, `grounds` or `contrasts`, or be written
    as unlabelled inline links with a connective.'
  level: warn
- scope: passage
  quotes:
  - '— exemplifies: versioned prompts, schemas, tools, and tests as one concrete system-definition
    loop'
  reason: 'The contract defines `exemplifies` as asymmetric from instance to general:
    the reader is at the instance and wants the general claim it falls under. Here
    the general note points to its instance, so the label runs backwards. The reverse
    edge belongs on the instance note. If this direction helps readers, use a label
    that fits it, or an inline link.'
  level: warn
- scope: passage
  quotes:
  - '— evidenced-by: surveyed systems already split into weight-promotion and artifact-promotion
    loops'
  reason: Under 'Origin is not corroboration', an `evidenced-by` context phrase must
    say what the claim risked and whether the evidence was recorded after the claim
    or independently of how it was built. Otherwise it must say that the evidence
    qualifies or bounds the claim. This phrase does neither, so readers cannot tell
    whether the survey corroborates the claim or is its origin, which would make the
    correct label `abstracted-from`.
  level: warn
- scope: passage
  quotes:
  - '[Constraining during deployment is continual learning]'
  reason: The link text does not match the target's title, 'Constraining during deployment
    can produce learning outside weights'. It also states a stronger claim than the
    target makes, so a reader would import a premise the linked note does not assert.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/1894ffdc7fc7462fbdad3a7407fa593c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/cba3d69e3b92b7626e2e6d50/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/1894ffdc7fc7462fbdad3a7407fa593c/outputs/review.md
raw-output-sha256: ca0d62098bba87678f8ce89c0d79c8a9510cccd2c03d872a1bbea69a1e3cf789
---

# Review

## Summary

The note is correctly placed in `kb/theory/`. It names no Commonplace selection. Its claim is about the design space for deployed learning systems: persistence is not enough, and governed behaviour-changing writes are required. Scoping system choices leaves that claim intact. The claim reads as universal by default. The note makes no statistical claim that would need a stated refuter. It bounds its scope by naming what governance does not replace: storage, activation and parametric adaptation. It defers the cross-form trade space to its sibling note rather than overreaching. Inline links mostly use connectives and serve the argument. No link points into `kb/work/`. The note cites no tracked sources, so the unquoted-source limit is not in play.

The unmet conventions are all in the outbound-link footer. Three label conventions are unmet. Two labels, `defines` and `sharpens`, are not in the collection's label table. `exemplifies` runs from the general claim to its instance, the reverse of its defined direction. The `evidenced-by` edge does not state whether the survey corroborates the claim or only bounds it, as 'Origin is not corroboration' requires. These are local repairs. They do not affect placement or the quality of the claim, so the outcome is WARN, not FAIL.

As a minor point, one link's text paraphrases its target's title in stronger terms than the target asserts.
