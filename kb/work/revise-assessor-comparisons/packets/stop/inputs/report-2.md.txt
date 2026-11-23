---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/critique-note.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: b61a1cb7e31b4dedb06d1c40c5c9dd9f
completed-at: '2026-11-22T21:54:36Z'
findings:
- scope: passage
  quotes:
  - A behaviour-changing write counts as continual learning when the system's own
    loop selects and retains it because deployment evidence bears on an improvement
    objective — for retained candidates, search, reject-capable evaluation, and operative
    retention
  reason: The discriminator makes reject-capable evaluation a condition of continual
    learning, but the linked proposal-selection note says learning can also proceed
    by direct evidence-determined update with no rejectable candidate, and it names
    online gradient descent as that case. The field's central continual-learning setting
    (sequential parametric training with forgetting mitigation such as regularization
    or replay) applies every update with no adoption gate. Read literally, the note
    excludes the field's paradigm cases. It should scope the reject-capable clause
    to proposal-selection loops and say how direct-update continual learning stands
    to its governance claim.
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: The note asserts this as field usage but gives no source. The ML continual-learning
    literature defines the term by learning from a non-stationary stream without catastrophic
    forgetting, not by self-selection or governance. The self-selection requirement
    looks like Commonplace's stipulation. The note should either cite field usage
    or present the requirement as this note's narrowing.
- scope: passage
  quotes:
  - 'It requires governing durable changes to future behaviour: selecting a candidate
    update, validating it, and deciding how it enters the behaviour-determining system.'
  reason: '"Requires" can mean two things: governance is constitutive (ungoverned
    durable change is not continual learning) or governance is needed for the learning
    to be reliable or safe. The note''s own grounding criterion, that any durable
    capacity change counts as learning, and that note''s statement that accumulation
    is the most basic learning operation support only the reliability reading. The
    regression argument (''continual adaptation compounds silent degradation'') also
    supports only that reading. Yet the discriminator paragraph uses the constitutive
    reading. The note should say which one it claims.'
- scope: passage
  quotes:
  - persistence does not decide which retained item should shape behaviour or with
    what force
  reason: A store-everything memory design can answer that selection and authority
    are assigned at read time by retrieval and in-context judgment, which is also
    a consumption path. The note says only that contextual activation is a separate
    subproblem. It does not explain why selection at read time is not governance,
    or why governance must happen at the write. A sentence that places the governance
    requirement at write time, read time, or both would close this gap.
contract: report
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/b61a1cb7e31b4dedb06d1c40c5c9dd9f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/c1ecbbc045061af431dee045/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/b61a1cb7e31b4dedb06d1c40c5c9dd9f/outputs/review.md
raw-output-sha256: 052f563e64bb75252af384f13c229e586358041bd8f3a4456fb80783463e586e
attack-outcome: partially lands
---

# Critique: Continual learning requires governing behaviour-changing writes, not just storing content

**Note:** kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
**Central commitment:** In a deployed system, continual learning is not achieved by persisting content. It requires the system's own loop to select, validate, authorize and coordinate behaviour-changing writes across the representational forms it can change.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a machine-learning continual-learning researcher working in the stream-learning tradition: sequential task training, with regularization methods such as elastic weight consolidation (EWC) or replay methods for mitigating forgetting. A memory-layer builder who treats accumulation plus retrieval as learning joins them. Together they pose a dilemma about "requires."

**Constitutive reading.** If governance is a condition of continual learning, the claim is false of the field's paradigm cases. Online gradient updates in sequential training are applied unconditionally. Nothing evaluates a candidate update and can reject it. EWC limits forgetting by regularizing the update, not by validating it. The note's own links concede this. The linked proposal-selection note (`kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`) says evidence "may instead determine an update directly — gradient-, reward-, error-, or viability-driven — with no candidate ever standing to be rejected." It names online gradient descent as a direct-update case that "contains no candidate-adoption decision." The grounding note "Learning is not only about generality" (`kb/theory/learning-is-not-only-about-generality.md`) adopts Simon's criterion: any more or less permanent capacity change. It also calls accumulation "the most basic" learning operation, and credits AgeMem's gains "entirely" to storing and retrieving facts. Under the note's own premises, an ungoverned durable write can be learning. A sequence of such writes during deployment can then be continual learning. The discriminator, "search, reject-capable evaluation, and operative retention", therefore does more than the field's usage supports. The note's claim that the field uses the term this way has no source.

**Normative reading.** If governance is what continual learning needs in order to be reliable, the claim holds but is weaker than the title suggests. It becomes a design recommendation: validate deployed updates against regression. That is standard MLOps practice for continuously retrained production models, and it holds whatever is stored. The contrast with "just storing content" then targets only a naive position, and the memory builder has a reply to that contrast too. A store-everything system defers selection and authority to read time, through retrieval and in-context judgment. By the note's own account, authority "belongs to a consumption path," and read-time selection is such a path.

## How the note engages it

**Partially engaged.**

- It limits scope to deployed systems with an autonomous loop that closes during deployment. This scope covers continuously trained production models, which do pass through validation gates before serving. Within that scope, the regression argument has force.
- It keeps parametric plasticity-stability and catastrophic forgetting as problems of their own. It also says storage, contextual activation and parametric adaptation "remain real subproblems." This leaves room for direct-update learning, but it does not say whether such learning counts as continual learning under the note's discriminator.
- It separates storage from authority through the knowledge-artifact versus system-definition-artifact distinction. This answers the naive "storage is learning" position. It does not answer the read-time-selection version.
- It does not address the tension with its own grounding notes: Simon's broad criterion, accumulation as basic learning, and the proposal-selection note's direct-update route. It does not source its claim about field usage.

The attack does not land on the core deployed-system point. Persisted bytes do not by themselves decide which item shapes behaviour or with what force, and an autonomous loop that writes without regression checks compounds degradation. The attack does land on the note's definitional narrowing of continual learning, and on the gap between its constitutive and normative uses of "requires."

## Constructive findings

- Say whether "requires" is constitutive or concerns reliability. If it is constitutive, explain how it fits with the broad learning criterion the note cites as grounds. If it concerns reliability, rephrase the discriminator paragraph accordingly.
- Scope the "search, reject-capable evaluation, and operative retention" clause to proposal-selection loops. Add one sentence on direct-update continual learning, such as online gradient updates or EWC. Say whether it is governed by other means, such as checkpoint validation before serving, or whether it falls outside the claim.
- Either source "as the field uses the term" or recast it as this note's stipulated narrowing of the term.
- Add one sentence on deferred, read-time selection. Explain why retrieval and in-context judgment do or do not count as governance, and whether the requirement applies at write time, read time, or both.

## Secondary objections (optional)

- The paragraph on mature release engineering says hand-authored changes are learning by selection that people perform. It then says the same edit is "maintenance." Calling it maintenance rather than externally selected learning makes the boundary look like a difference in kind. It is actually a difference in where the selector sits. The note could say that it draws the line by where selection happens, not by whether learning occurred.
- The description says updates must be coordinated "across the representational forms a system can change." The body correctly weakens this: a loop "need not touch all three every time". The description should match the body.
