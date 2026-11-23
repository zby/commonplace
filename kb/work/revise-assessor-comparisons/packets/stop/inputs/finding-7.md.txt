---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:05Z'
findings:
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: 'The sentence fuses a prior account (the field''s usage of ''continual learning'')
    with the note''s own explication (continual learning as system-performed selection
    with search, reject-capable evaluation and operative retention). Reading A: the
    selection criterion is inherited from the field and the note merely adopts it.
    Reading B: the criterion is the note''s contribution, and ''as the field uses
    the term'' only claims rough agreement. The choice is material: it changes attribution
    (field versus note) and what the note claims to contribute, and it bears on scope,
    since the ML continual-learning literature centrally covers direct gradient updates
    that the selection criterion may exclude. The author must decide whether the criterion
    is inherited or proposed and state that relation.'
  level: warn
- scope: passage
  quotes:
  - the force with which a consumed artifact determines what the system actually does
  reason: The inline gloss presents behavioral authority as a force only, while the
    linked definition records consumer, channel and force. Nearby text ('belongs to
    a consumption path') restores the path reading, so the blur is not material here.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/ea1e9ea5babe934c17e148d7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 7effd51d4999fff0f354a52db7212d0177971fe850670efd5c60bcf2ebd0720b
---

# Review

## Summary

Most passages keep their roles distinct. The opening states plainly that it adopts the broad learning criterion from a linked note. It applies the knowledge-artifact and system-definition-artifact families to one object under different consumption paths, which matches the linked definitions.

The one material blur is the sentence on how "the field" uses continual learning. That sentence decides what counts as continual learning rather than maintenance, yet it does not say whether the system-selects criterion comes from the field or is the note's own explication. Attribution and scope both depend on that answer.
