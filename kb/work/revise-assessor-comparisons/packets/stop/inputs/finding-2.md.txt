---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 0177d84330a5bbe930bebfc55c1c352405b81cb00146dd7b5389717615b8d3fb
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 67c579e9396d4e8f900dbd7f72412687
completed-at: '2026-11-22T21:53:08Z'
findings:
- scope: passage
  quotes:
  - 'Mature release engineering already governs hand-authored readable changes. Those
    changes are learning too: the software learns by [selection](./definitions/selection-based-learning.md)
    that people perform on it.'
  - 'The same edit hand-authored in reaction to an incident is maintenance: the system
    learned, and people outside its loop did the selecting.'
  reason: 'The boundary caveat (hand-authored changes are learning by human selection,
    but not continual learning) is stated twice in the final paragraph: once through
    release engineering and again through the incident-edit example. Both make the
    same point, that people outside the loop did the selecting. The boundary is needed,
    but one statement placed next to the proposal-selection criterion would do the
    same work. Merge the two into one sentence.'
  level: warn
- scope: passage
  quotes:
  - Form placement is itself revisable. A stable natural-language rule may be codified,
    while a brittle symbolic rule may be relaxed back into prose ([codification and
    relaxing](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)).
  reason: The aside on codifying and relaxing elaborates the form-placement decision
    already made in the previous paragraph. It interrupts the governance paragraph
    between the list of governance tasks and the selection-based boundary. It is short
    and linked, so it may earn its place as the write path between forms. It could
    also shrink to a clause in the previous paragraph's 'decide which form a lesson
    belongs in' sentence.
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/67c579e9396d4e8f900dbd7f72412687/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/4c3c0dc9c89e5b7a6f8f8b59/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/67c579e9396d4e8f900dbd7f72412687/outputs/review.md
raw-output-sha256: a3e34a3900cf2f4273ab89d89630759e9670a392928b2903248aed362a164940
---

# Review

The note is compact overall, and most of its detail carries an inference step. The definitions of behavioural authority and artifact roles in the opening paragraph support the conclusion that persistence alone does not create a governed write. The two deployment constraints (cheap installation and regression validation) are premises. The parametric plasticity-stability concession is a short, fair caveat that stops the cross-form argument from reading as a dismissal of weight-based continual learning. None of these needs compression.

The overhang sits in the final paragraph. Its boundary between continual learning and maintenance takes several sentences, and the same point appears twice: hand-authored changes count as learning, but people selected them, so they are not continual learning. One statement is enough. Separately, the aside on form placement (codification and relaxing) is probably extendable detail that could become a clause. It is reported as INFO because it is brief and links to the note that owns the topic.
