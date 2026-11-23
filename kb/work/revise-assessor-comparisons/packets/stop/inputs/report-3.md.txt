---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 6406bbb115ab47788407d707365afbd8
completed-at: '2026-11-22T21:57:21Z'
findings:
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated, read as universal: the governance that continual learning
    requires sits at the write, so governing writes is where selection, validation
    and authority assignment happen. — The note''s own premise says behavioural authority
    belongs to a consumption path, not to stored bytes. Store-everything memory systems
    with read-time selection — for example importance, recency and relevance scoring
    at retrieval in generative-agent memory — leave writes ungoverned and govern behaviour
    change at read time. The title''s locus (''writes'') then mis-sorts a recognizable
    design. The commitment survives if ''governing behaviour-changing writes'' explicitly
    includes governing the write''s consumption path, which the phrase ''assigning
    it an authority path'' already gestures at. — LOCAL — instance'
- scope: passage
  quotes:
  - 'Continual learning, as the field uses the term and as this note uses it, asks
    for more: the system does the selecting itself.'
  reason: 'DOUBTFUL — Universal attribution: the field''s usage of ''continual learning'',
    like the note''s, requires the system to select its own retained writes, and the
    next sentence adds search, reject-capable evaluation and operative retention.
    — In the ordinary case in the ML continual-learning literature (sequential task
    streams; regularization or replay methods such as EWC), a curator supplies the
    stream and every gradient update is installed without per-candidate reject-capable
    evaluation. Field usage centres on forgetting, not on self-selection with a reject
    gate. Dropping the field attribution keeps the note''s usage as a stipulation,
    but a stipulated definition that builds selection and validation into ''continual
    learning'' makes ''continual learning requires governance'' partly true by definition.
    The repair should therefore keep the substantive part (persistence is insufficient;
    cross-form writes need validation and coordination) outside the definition. —
    LOCAL — prevalence'
- scope: passage
  quotes:
  - a learning loop must decide which form a lesson belongs in
  reason: 'DOUBTFUL — Universal: a continual-learning loop must itself decide which
    representational form a lesson belongs in. — Many deployed artifact-learning systems
    have one writable form fixed at design time: a memory file that only receives
    natural-language entries, or a skill library that only receives code. The loop
    makes no form decision; the designer made it once. Such systems are common rather
    than marked exceptions. Restrict form choice to systems with several writable
    forms, or allow it to be a design-time decision, and the central commitment keeps
    its selection, validation and coordination core. — LOCAL — prevalence'
- scope: passage
  quotes:
  - The same edit hand-authored in reaction to an incident is maintenance
  reason: 'DOUBTFUL — Binary boundary: a behaviour-changing write is either selected
    by the system''s own loop (continual learning) or hand-authored by people outside
    it (maintenance). — Hybrid loops, where the system proposes a rule or memory edit
    from deployment evidence and a human approves or rejects it, are common in deployed
    agent tooling. The note lists ''authorize'' among governance steps, which suggests
    human authorization can sit inside the loop, yet human selection is placed outside
    it. The boundary leaves the hybrid case unsorted. Adding a condition that says
    whose rejection counts as the loop''s reject-capable evaluation would resolve
    this without changing the mechanism. — LOCAL — instance'
- scope: passage
  quotes:
  - because continual adaptation compounds silent degradation
  reason: 'DOUBTFUL — Universal: each candidate write must be validated against regression
    because continual adaptation compounds silent degradation. — Online bandit and
    online-gradient learners install each update without per-update regression validation;
    their protection against degradation is built into the update rule (bounded step
    size, regret guarantees) and aggregate monitoring with rollback. Compounding degradation
    is real for unconstrained writes but not universal for every update regime. The
    claim survives if validation may be per-write, embodied in a validated update
    rule, or post-install with cheap rollback. The repair must not stretch ''governance''
    to cover any update rule whatever, or the claim becomes trivial. — LOCAL — instance'
- scope: passage
  quotes:
  - deployment evidence arrives online and is often sparse, so candidate writes must
    be cheap to propose and install
  reason: 'DOUBTFUL — Tendency (''often''): deployment evidence is sparse, so writes
    must be cheap and some lessons must take effect before retraining. — High-traffic
    deployments such as recommendation and ranking systems receive dense online feedback
    and routinely update parameters incrementally; there, cheap installation does
    not favour artifact writes over parametric ones. The tendency holds for agent
    deployments with low-volume, high-variance feedback; it is domain-relative rather
    than general. Name the domain where sparsity holds. — LOCAL — prevalence'
- scope: passage
  quotes:
  - persistence does not decide which retained item should shape behaviour or with
    what force
  reason: 'HOLDS — Universal: persistence infrastructure does not by itself decide
    which retained item shapes behaviour or with what force. — The hunted counterexample
    is auto-loaded memory, where every stored item enters the context. Even there,
    the storage system does not choose; the fixed consumption path plus the write-admission
    decision do. That case supports the note: persistence there creates an ungoverned
    behaviour-changing write.'
- scope: passage
  quotes:
  - then an updater restricted to weights freezes consequential choices outside its
    reach
  reason: 'HOLDS — Conditional: if prompts, tools, validators and runtime policy determine
    behaviour, a weights-only updater cannot change those choices. — No counterexample
    found; a system whose wrapper is thin fails the antecedent, which the note conditions
    on, rather than defeating the premise.'
- scope: passage
  quotes:
  - coordinate whichever forms that update touches
  reason: 'HOLDS — Universal: an update touching several forms needs coordination
    across them. — No counterexample found. A prompt rule that contradicts a validator,
    or weights fine-tuned against an older prompt format, regresses when one form
    changes without the other.'
- scope: passage
  quotes:
  - learning is any durable change in a system's capacity to adapt to its environment
  reason: 'HOLDS — Stipulated broad criterion: any durable change in adaptive capacity
    counts as learning, so non-weight changes qualify. — As a stipulation borrowed
    from a linked note, it can be challenged only for idleness or mis-sorting. The
    note uses it consistently, including conceding that human-performed maintenance
    is learning, so no case it mis-sorts was found.'
contract: report
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/6406bbb115ab47788407d707365afbd8/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/13170f70e91e67db4a3005a6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/6406bbb115ab47788407d707365afbd8/outputs/review.md
raw-output-sha256: d4054a970d1fc3dc81d253d2d49f95acb01c0b4566fc7bd80934c8e189326d85
---

# Premise decomposition: continual learning requires governing behaviour-changing writes

**Register:** claim
**Central commitment (one sentence):** In deployed systems, continual learning requires the system itself to select, validate, assign authority to and coordinate durable behaviour-changing writes across the representational forms it can change; persisting content is not enough.

## Premises and counterexamples

The commitment has three parts, and each consumes its own premises.

1. **Persistence is insufficient.** This part rests on the consumption-path account of behavioural authority and the broad learning criterion. Both hold. One unstated premise does not: that the governing happens at the *write*. The note's own authority premise moves force to the consumption path, and read-time-governed memory systems are a recognizable design. That tension is the note's most interesting internal joint.
2. **Deployment imposes cheap installation and regression validation.** Both constraints are true of typical agent deployments but are stated more generally than the evidence supports. Dense-feedback domains weaken the sparsity tendency. Update rules with built-in guarantees, or post-install rollback, weaken per-write validation. Both repairs are boundary conditions.
3. **The system must do the selecting, across forms.** The field attribution is the weakest premise: ordinary ML continual learning neither self-selects with a reject gate nor chooses forms. Removing the attribution leaves a stipulation, and the note should keep that stipulation from carrying the claim. Form choice by the loop is also not universal, because many systems fix form at design time. The maintenance/learning boundary leaves hybrid propose-and-approve loops unsorted.

No premise failure breaks the core mechanism. Every dented premise can be repaired by scoping or by naming where governance may sit, so all failures route `LOCAL`. The one structural warning is about stipulation: if selection and reject-capable validation become part of the definition of continual learning, the title claim becomes partly true by definition.

## For the human

Look first at the unstated write-locus premise: if authority belongs to the consumption path, say whether "governing writes" includes read-time governance, or the title mis-sorts store-everything, select-at-read memory systems.
