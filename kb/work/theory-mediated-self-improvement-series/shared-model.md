# Shared model

This is the workshop's compact working synthesis. It connects the
[target problems](./target-problems.md), durable theory notes, and evaluation
artifacts. It does not promote claims by itself; the linked notes carry their
arguments, evidence, and scope conditions.

## Core conjecture

A mixed system can improve through explicit theories without requiring every
learned result to enter model weights. Retained natural-language theory makes
premises, criteria, and scope addressable. A language model interprets and
criticizes them. Symbolic machinery carries state and exact transitions.
Evidence and oracles correct the result.

The attribution *improvement through theory* requires one causally co-indexed
path:

    retained theory
      -> interpreted decision
      -> realized change
      -> outcome
      -> read-back against the same theory
      -> revised theory
      -> later operation

Co-occurrence inside one system boundary is insufficient. The same theory must
guide the change, be tested by its result, and affect later operation after
revision. This is the central constraint from
[theory-mediated self-improvement needs interpretation and retention](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

Explicit retention contributes addressability, not automatic correctness.
Credit assignment, coherence, retrieval, interpretation, and admission remain
separate problems, as
[reflection buys addressability](../../notes/reflection-buys-addressability.md)
sets out.

## Functional architecture

| Role | What it supplies | Characteristic failure |
|---|---|---|
| Retained explicit theory | Represented premises, objectives, explanations, assumptions, and applicability conditions | Omission, contradiction, drift, inert documentation, retrieval failure |
| Language-model interpreter | Semantic application, criticism, derivation, and proposal where cases are not fully formalized | Underspecification, stochastic deviation, bias, confabulated rationale |
| Symbolic runtime and code | State, scheduling, repeatable transitions, validation, installation, rollback, and continuity across calls | Faithful execution of the wrong transition; frozen decomposition |
| Evidence and oracles | Rejection, comparison, correction, and outcome read-back independent of the candidate | Weak proxies, captured evaluation, self-sealing judgment, incomplete coverage |

The architecture is mixed because the residual decisions left with people fail
for different reasons:

| Why a decision remains human | Capacity that must grow |
|---|---|
| A required premise is not represented | Representation |
| The criterion is unsettled or cannot yet be applied | Settlement and interpretation |
| No sufficiently independent check exists | Verification |
| The decision arises beyond the automatic horizon | Continuity |

No one role supplies all four capacities. The parts are functional roles, not a
required process diagram; one process may host several roles. The derivation
and its limits live in
[each residue class needs a different mechanism](../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md).

## Operating cycle

The working cycle is:

    observation or failure
      -> criticism of retained theory
      -> revised theory or derived candidate
      -> realization in prose, code, configuration, or model state
      -> evaluation and admission
      -> installation and execution
      -> outcome read back against the retained theory

A contemporaneous citation of retained theory at the decision point is a cheap
[mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md).
It is necessary for a record-based mediation claim but does not prove correct or
load-bearing use. Withholding or replacing the theory and observing a changed
decision is stronger evidence.

When a derivation recurs and its scope stabilizes, it may be codified into a
methodology, validator, or scheduler. The narrower artifact becomes a cheaper,
more faithful fast path; the theory remains available as a fallback while
coverage is incomplete. This is the
[two-layer execution model](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md).

## Progress and the human boundary

Do not put systems on one ladder. Tool usefulness, computational autonomy,
warrant, and system power ask different questions and require different
evidence. A change must name which dimension moved; none follows from another.
See
[usefulness, autonomy, warrant, and power are separate dimensions](../../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).

A mechanism has an **automation envelope**: the responsibilities it can carry
under stated conditions. Progress can expand that envelope by moving a
responsibility out of the residual human work, or improve quality, reliability,
coverage, latency, or cost inside a fixed envelope. Reaching a ceiling does not
retract the transfer already made and does not show a path beyond the ceiling.
See
[a method's ceiling bounds the method](../../notes/a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md).

Warranted transfer is adversely selective. It preferentially moves decisions
with represented premises, settled criteria, and checkable outcomes, leaving a
residue that is harder to warrant per decision. The remaining human work is
therefore evidence about what the current system cannot warrant, not about an
essentially human capacity. Each residual decision should be recorded with the
reason it stayed human.

At the least-warrantable point of open-ended program modification, this is the
same problem as Naur's coherent-modification test. Human theory-holders do not
need to deduce a correct change from a complete theory. They use a partial
program theory to guide search, interpret failures, backtrack, and revise under
delayed feedback. Warrant belongs to the process across later demands, not to
the first proposal. See
[holding a program theory means sustaining coherent search under delayed feedback](../../notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

## Closure and strong capability

Computational closure is task-scoped. A claim must declare task selection,
objective and acceptance, system boundary, permitted exogenous inputs and
interactions, horizon, resources, and coverage. Conditional on those
declarations, every remaining required decision and transition must be carried
inside the automatic system. The detailed formulation is
[task-scoped computational closure](./task-scoped-computational-closure.md).

Closure is structural: it says where decisions and transitions occur, not
whether they are good. A non-degenerate milestone also needs externally
anchored capability, consequential revision reach, an adequate evaluator,
continuity, no hidden human cut, and outcome evidence. The
[closure-capability map](./closure-capability-map.md) records these coordinates
and degenerate patterns.

Performance at least as good as a competent remote programmer is a strong
worker-capability benchmark, not the definition of useful progress. Holding the
client fixed exports task choice, feedback, and acceptance; passing the
benchmark therefore does not establish closure over those decisions. See
[a benchmark that holds the client fixed](../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).

## Current bootstrap

Commonplace is a human-inclusive testbed. It already retains and routes theory,
supports criticism and revision, and can turn some theory into operative
instructions, validators, schemas, and code. Humans still choose objectives,
supply unrecorded premises, authorize consequential changes, interpret
ambiguous evidence, and repair paths beyond represented coverage. This supports
claims about present tool usefulness and mechanism traces, not independent
computational theory possession or closure.

The program uses two linked testbeds: Commonplace's own operation and
programming agents supplied with persistent project-specific theory. Classifying
the residual decisions on either path can suggest what to build next. Whether
following that classification produces a more powerful system is an empirical
question, not a consequence of the model.

## Minimum evidence for one episode

A useful episode record should identify:

1. the selected task, objective, boundary, horizon, and starting human cut;
2. the retained theory claimed to guide the decision, with a contemporaneous
   mediation trace or an intervention on that theory;
3. the realized change and the acceptance mechanism;
4. the outcome and its read-back against the same theory;
5. the retained theory or machinery revision, including rejection or deferral;
   and
6. the dimension that moved and the residual decisions that remain human.

Without the same-theory trace and read-back, the record may show a useful
change, but it does not show theory-mediated improvement.

## Open questions

- What task distribution and horizon distinguish a composite that sustains
  coherent program-specific search and recovery from one that succeeds by
  luck, memorization, or a permissive evaluator?
- How can load-bearing use of retained theory be distinguished from a merely
  decorative citation without rerunning every decision?
- Can task choice, acceptance, and evaluator revision move inside the system
  without producing captured evaluation or boundary export?
- On which task distributions does explicit theory improve sample efficiency,
  reliability, or revision cost relative to weight updates or fixed-decomposition
  artifact learning?
- At what grain can residual decisions and displaced review or repair be
  compared without inventing a misleading scalar?
