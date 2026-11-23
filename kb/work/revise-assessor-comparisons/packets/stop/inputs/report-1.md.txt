---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 228f28569e68480ba8137eafea4249bf
completed-at: '2026-11-22T21:55:23Z'
findings:
- scope: passage
  quotes:
  - candidate writes must be **validated against regression**, because continual adaptation
    compounds silent degradation
  reason: UNSUPPORTED — the claim that continual adaptation compounds silent degradation
    is asserted, not argued, and the only support is the scheduler-LLM separation
    note. That note explains why workflow state and defined transitions are cheap
    to enforce in code. It does not say that unvalidated writes accumulate undetected
    harm. The validation requirement may be true, but this sentence does not establish
    it. It also leaves open how a regression check covers the 'open-ended behaviour'
    that paragraph 4 says must be validated.
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: 'UNSUPPORTED — this sentence carries the boundary between continual learning
    and maintenance, and it rests on an unshown appeal to field usage. Parametric
    continual-learning work is usually framed as learning from non-stationary data
    without forgetting. It does not usually require a reject-capable selection loop.
    Without evidence, the boundary is a stipulation presented as convention. It also
    leaves the title''s ''requires'' partly definitional: governance is required because
    the note defines continual learning to include it.'
- scope: passage
  quotes:
  - deployment evidence arrives online and is often sparse, so candidate writes must
    be cheap to propose and install
  reason: THIN — online arrival supports cheap and frequent installation, but sparsity
    does not. Sparse evidence gives fewer samples per lesson. That argues for caution
    or batching as much as for cheap writes. The 'so' combines two premises, and only
    one of them supports the conclusion.
- scope: passage
  quotes:
  - 'The resulting problem is governance: autonomously *choosing* a behaviour-changing
    write, *validating* it against open-ended behaviour, assigning it an authority
    path, and coordinating it'
  reason: THIN — 'resulting' presents the four-part governance problem as the result
    of the previous paragraphs. Earlier text motivates choosing (persistence does
    not decide), validation (the regression joint) and coordination (multiple forms).
    It never argues that a loop must explicitly assign an authority path. Paragraph
    1 only says that authority belongs to a consumption path, which is a property
    of artifacts, not a duty of the learning loop. The description's 'authorize' requirement
    therefore rests on a definition, not an argument.
- scope: passage
  quotes:
  - Persistence alone therefore does not create a governed behaviour-changing write.
  reason: HOLDS — given the preceding premise that behavioural authority belongs to
    a consumption path rather than to stored bytes, persistence cannot fix a write's
    force. The inference is valid, though close to definitional. Its weight depends
    on the later, weaker joints that turn 'not sufficient' into 'requires governance'.
contract: report
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/228f28569e68480ba8137eafea4249bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/7ace43f9abeb5fbbf9dd9940/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/228f28569e68480ba8137eafea4249bf/outputs/review.md
raw-output-sha256: 6211b18f5c4106b74968f3b7a8198e69c3b124fe8b412a3cd2510c281a5a9daf
---

# Friction check: continual learning requires governing behaviour-changing writes

**Central claim (one sentence):** A deployed system learns continually only when its own loop selects, validates, authorizes and coordinates durable behaviour-changing writes across whatever representational forms it can change; persisting content is not enough.

## Filter
**Filter:** SURVIVES

The claim combines four goals: cheap online installation, validation against regression on open-ended behaviour, autonomous selection by the system, and coordination across forms. Cheap installation and thorough validation of open-ended behaviour pull against each other. The note partly resolves this tension because form placement trades installation cost against verifiability, so the goals can coexist through placement. It does not dissolve the claim. However, the note never says what validation means when behaviour is open-ended.

## Thinnest joints

The regression joint ranks first because it carries a stated requirement, but its only citation supports a different point: code-enforced bookkeeping, not compounding degradation. The field-usage joint ranks next because it draws the continual-learning/maintenance boundary that the title depends on. The note asserts that boundary as convention without showing the convention, which makes the 'requires' partly true by definition. The sparsity joint is a local non sequitur inside an otherwise reasonable step. The 'resulting problem' joint introduces authorization without earlier argument. The persistence joint holds, but it establishes only insufficiency. The step from insufficiency to a required governance structure belongs to the weaker joints above it.

## For the human
Look first at the validation-against-regression sentence: it needs its own mechanism or a source that argues for compounding silent degradation, plus a statement of what regression validation means for open-ended behaviour.
