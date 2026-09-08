---
description: "Definition — theory-mediated learning is model-based learning whose model is a theory: explanatory, addressable, and revised by reasoning; a latent world model is model-based but not theory-mediated"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory-mediated learning

**Theory-mediated learning** is model-based learning in which the model is a
theory. A learner is model-based when an internal model of its target stands
between evidence and behavior change, and it acts by running the model rather
than by fitting behavior to observations directly; a [learned world
model](../world-models-assess-explanatory-reach-through-action-conditioned.md)
is the familiar case. The model is a **theory** when it has three further
properties. It is explanatory: it proposes a mechanism, invariant, or other
relation that says why, not only what will happen next. It is addressable: it
is a stable semantic unit whose assumptions, scope, and parts can be inspected.
And it is revised by reasoning: the learner changes it by deriving a
consequence, exposing an assumption, comparing a rival, or narrowing a scope,
not only by further fitting. **Mediated** is then a causal relation, not
co-occurrence: the learner must operate on the theory's content, not hold it
beside a decision it would have made anyway.

The three properties are what the term adds to model-based learning, and the
boundary follows from them. A latent predictor of environment dynamics is
model-based and has none of the three: it is revised only by further training,
and its scope is discoverable only behaviorally. An explicit causal model or
simulator program whose premises can be inspected and rescoped has all three
and is both a world model and a theory. The payoff is argued elsewhere:
[theory-mediated learning may improve sample efficiency under structured
shifts](../theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
predicts a gain only where the theory names structure the shift preserves.
This note fixes the vocabulary.

## Scope

- **One mediated stage is enough.** A theory can shape diagnosis and search,
  candidate proposal and ranking, choice of evaluation evidence, or
  interpretation of the outcome, the stages of a [proposal-selection
  loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md).
  These succeed and fail independently, so a report of mediation should name
  the stage it holds for.
- **One episode is the minimum unit.** A theory built for the current episode
  and discarded afterwards still mediates it. Whether the theory is also
  retained, revised against the outcome, and consumed again later is a further
  question, and each of those steps needs its own evidence.
- **Any representational form.** The theory may be natural language, a causal
  model, a program, a schema, or a mixture. [Representational
  form](./representational-form.md) decides which assessment routes are
  available, not whether mediation obtains. Addressability comes in degrees,
  though: a theory reachable only as an indivisible document can be replaced
  but not rescoped one premise at a time.
- **Not a success term.** A false theory mediates as readily as a true one,
  toward worse outcomes. Being able to apply a theory is a semantic capability
  and is all the term requires. Whether the theory earns the scope it claims is
  [reach-assessment](./reach-assessment.md), a separate epistemic function that
  mediation neither supplies nor presupposes.

## Mediation is the first link, not the whole path

Four claims of increasing strength get collapsed into this one term. Mediation
is the first: changing or withholding the theory changes a proposal, an
evaluation, a recovery step, or a realized change. Empirical contact, theory
learning, and recurrent use of the revised theory are the further links, and
[disconnected witnesses do not establish the full
path](../disconnected-witnesses-do-not-establish-a-theory-mediated-path.md):
each link must identify the same theory state as its neighbours. The functions
a full path needs are set out in [theory-mediated self-improvement needs
interpretation, retention, and independent
read-back](../theory-mediated-self-improvement-needs-interpretation-and-retention.md).

Two further conditions are independent of mediation and of each other. A
system is *reflective* when the mediating theory describes organization that
helps determine the system's own behavior; a theory of an external target
mediates without being reflective. It is *self-improving* when the accepted
change persists and affects later operation. A system can be theory-mediated
and neither, either, or both, so the three are reported separately.

The cheapest evidence for mediation is a contemporaneous [citation at the
decision
point](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
which identifies the theory a decision claims to have consumed. Withholding,
replacing, or perturbing the theory and observing a changed decision is
stronger.

## Exclusions

- **A stored theory nothing consumes.** [A stored representation matters only
  through its consumption
  path](../an-action-model-matters-only-through-its-consumption-path.md). A
  theory repository beside a self-changing system is the expected case, not
  evidence of mediation.
- **Rules whose reasons are not retained.** A rule set can guide decisions
  without being a theory. With no mechanism retained, a correction to one rule
  reaches none of the others that share its unstated reason, and there is
  nothing to derive consequences from.
- **Post-hoc rationale and retrieval logs.** An explanation written after the
  decision, or a citation naming everything that was in context, records
  something correlated with consumption, not consumption.
- **Deliberation as such.** Reasoning that produces no criticizable
  intermediate object is not mediation. An experiment claiming mediation has to
  control for deliberation budget.

## Misuse cases

- Calling a system theory-mediated because it retains explicit prose about
  itself. The term names a causal path through the theory, not the presence of
  an artifact.
- Reserving the term for the full recurrent loop, so that a single-episode
  theory-guided change goes unreported. Narrower claims are reportable at their
  own strength.
- Reading the term as a claim that natural language is the right carrier. The
  prevalence of prose theories is a fact about available substrates, not part
  of the meaning.
- Treating an accepted change as confirmation of the theory that motivated it.
  Acceptance judges the change; the theory needs its own read-back.

## Word forms

Hyphenate the adjective: *theory-mediated learning*, *a theory-mediated path*.
The noun phrase is spaced: *theory mediation*. Bare *mediation*, once the
pathway has been introduced, names the first link, not the full path.
*Theory-mediated system learning* is the reflective case, where the theory is
about the learning system itself.

---

Relevant Notes:

- [Theory-mediated learning may improve sample efficiency under structured shifts](../theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: develops the payoff conjecture, the addressability contrast with parametric retention, and the test that would decide it
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: states the functions a full path needs and the evidence ladder whose first rung this definition names
- [Disconnected witnesses do not establish a full causal path through theory](../disconnected-witnesses-do-not-establish-a-theory-mediated-path.md) — extends: what the witnesses must identify before separate links compose into one path
- [Citing retained theory at the decision point is a mediation trace](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — mechanism: the cheapest checkable evidence for the mediation link, and what it leaves open
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loop whose stages a theory can mediate
- [Reach-assessment](./reach-assessment.md) — contrasts: the epistemic judgment that decides whether a mediating theory deserves its scope; mediation does not supply it
- [Representational form](./representational-form.md) — grounds: the axis that fixes assessment route without fixing whether mediation obtains
- [Reflective system](./reflective-system.md) — contrasts: reflective membership is an added condition, not part of mediation
- [World models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md) — contrasts: the familiar model-based case, which lacks the three properties that make a model a theory
- [Theory mediation can coordinate heterogeneous factory development](../theory-mediation-can-coordinate-heterogeneous-factory-development.md) — extends: applies the term across mixed prose, symbolic, and executable machinery
- [Three 2026 harnesses retain rules or weights, not a revisable theory](../evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md) — evidenced-by: worked cases on the near side of the boundary, where retained rules and retained weights both fall outside the term
