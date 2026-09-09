---
description: "Definition — theory refinement revises an existing fallible explicit theory against empirical cases, seeking improved fit with limited changes; the KB extends its representation and subject"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory refinement

**Theory refinement** is the learning operation that revises an existing
fallible explicit theory using empirical cases, seeking to correct errors
while preserving useful prior knowledge rather than learning from scratch. It is the
revising case of model-based learning: an internal model stands between
evidence and behavior change, and here the model is a theory. The KB uses the
term in the established sense of
[Ourston and Mooney](../../sources/theory-refinement-analytical-empirical-methods.ingest.md)
and [Richards and Mooney](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md),
and widens what counts as a theory beyond what those systems could compute.
The widening is stated below as a departure, with what it changes.

## The classical object

In the classical systems the theory is a **domain theory**: an explicit set of
Horn-clause rules, supplied by an expert, approximately right but possibly
incomplete or incorrect, from which conclusions about cases are derived by
proof. Three inference modes run over it. **Deduction** applies the theory and
exposes false positives, a proof of a case that should not belong.
**Abduction** hypothesizes which missing premise would let an unprovable
positive case be proven, identifying a candidate repair. **Induction** fills
the gap the abduction identified from the supplied examples. The repair
operators are named: retract, generalize, specialize, add a rule or an
antecedent. Acceptance is consistency with the supplied cases.

Richards and Mooney separate the task from FORTE's realization: improving an
existing fallible theory from empirical cases while seeking to preserve useful knowledge
is the concept; Horn clauses, greedy search, and the label format are the
algorithm. This note follows that separation. Their task seeks a minimally revised theory
correct on the supplied instances. FORTE approximates minimal revision through
small edits and few operations; its hill-climbing search can stop before
training consistency is reached. Neither unique fault identification nor
preservation of all previously correct behavior follows from the task definition.

## What the loop requires of a theory

Three properties, implicit in the classical object, are what the loop uses.
This KB makes them the definition of a **theory**, so that broader forms
qualify by the same test:

- **Consequences a case can contradict.** The theory says what should hold in
  a case, so the case can fail it.
- **Parts available as candidate repair locations.** A failure can guide search
  over premises, rules, or scope conditions without identifying a unique fault.
- **Parts editable separately.** Operators can change selected parts rather than
  replace the whole theory. Evaluation checks whether a candidate corrects
  errors and preserves behavior on the tested cases; unchanged text alone
  does not guarantee unchanged consequences.

A theory in this sense is addressable: a stable unit whose assumptions, scope,
and parts can be inspected and revised individually. Addressability comes in
degrees. An indivisible document can be replaced but not rescoped.

The three requirements read off the two axes that derive
[representational form](./representational-form.md). **Localization** supplies
the second and third: a localized unit has candidate parts to inspect and edit, and
distributed-parametric state has none, which is why a latent world model is
excluded below whatever it has learned. **Assigned consequences** decide the
strength of the first: where a defined consumer fixes what the theory implies,
a contradiction is a fact; where it does not, a contradiction is an
interpretation. The classical systems sat in the symbolic cell, with both axes
on their side. A natural-language theory keeps localization and gives up
assigned consequences, which is the exact content of the form departure below.

## Departures

Two widenings are the KB's own and should not be read back into the sources:

- **Form.** The theory may be natural language, a program, a causal model, or a
  mixture, not only a rule set. [Representational form](./representational-form.md)
  fixes the assessment route, not whether the loop applies.
- **Subject.** The theory may describe the learner's own behavior-determining
  organization. The classical papers say their theory is external.
  **Reflective theory refinement** is theory refinement whose theory is a
  causally connected self-representation in the sense of
  [reflective system](./reflective-system.md); it is composed from the two
  terms and defined by neither alone.

## Computed consequences support diagnosis and evaluation without guaranteeing repair

In the classical setting a proof procedure fixes what the theory implies for a
case. Disagreement with a supplied label can therefore be checked, and proof
traces can identify candidate repair locations. A trace does not uniquely
identify the faulty commitment. FORTE scores candidates against the training
set, but can stop at a local maximum. For a natural-language theory, an
interpreter also judges what the theory implies, adding possible misreading
to the uncertainty already present in diagnosis and repair.

A theory in this KB is a mixed-form object. The parts committed to a
validator, schema, or test have crossed into
[codification](./codification.md): a formal consumer computes their
consequences, so for those parts a contradiction is a fact. The parts still in
prose have consequences an interpreter derives. Refinement moves parts across
that boundary as they settle.

Codification alone does not supply diagnosis or successful repair. A failed
check must be connected to the theory commitments it tests before it can
guide candidate edits. Evaluation then tests the revised theory against the
failure and other cases; its conclusions are bounded by those checks. The
KB has not shown that its mixed-form loop arranges these functions reliably.
Where no crossing has happened, withholding or perturbing the theory and
observing a changed decision supplies evidence that it shaped that decision.
Whether a model interprets prose theories consistently enough to support
useful diagnosis and revision is an empirical question for the pathway in
[theory refinement may improve sample efficiency under structured shifts](../theory-refinement-may-improve-sample-efficiency-under-shifts.md).

Refining theories nobody computes is the older case, not the exception.
Scientific theories in prose and mathematics were refined for centuries by
people deriving their consequences. Popper treats a theory's consequences as
objective and exceeding what any holder has grasped:
"nobody, neither its creator nor anybody who has tried to grasp it, can have a
full understanding of all the possibilities inherent in a theory"
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md),
verbatim). That a failed prediction does not by itself say which premise to
give up is the KB's own statement of the underdetermination problem; no source
for it is snapshotted yet.

## Scope

- **One episode is the minimum unit.** Retaining the theory, refining it, and
  reusing the refined state are separate links on the
  [evidence ladder](../reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder),
  each needing its own evidence. A contemporaneous
  [citation at the decision point](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
  is the cheapest evidence that the theory entered a decision.
- **Retained rationale is optional.** Rules can expose consequences and editable
  premises without recording why they were adopted. Retaining supporting
  evidence or shared assumptions can help diagnosis and coordinated revision;
  membership depends on the refinement operation.
- **Any machinery.** An LLM, a program, or a mixture may do the deriving,
  localizing, and revising. Membership is by operation, not by machinery.
- **Not a success term.** A false theory refines as readily as a true one.
  Whether a theory earns its scope is [reach-assessment](./reach-assessment.md),
  which the loop neither supplies nor presupposes. Among revisions that fit the
  evidence, reach is preferred.
- **Independent of subject.** A theory of an external target and a theory of
  the learner's own organization are applied, generalized from, and refined
  alike. Whether the learner is [reflective](./reflective-system.md), and
  whether the change persists as [self-improvement](./self-improving-system.md),
  are separate conditions.

## Exclusions

- **A stored theory nothing consumes**, since
  [a representation matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md).
- **A latent world model as such.** It is model-based but non-localized, so
  it is revised only by fitting: it has no part to blame, and its scope is
  discovered behaviorally.
  An inspectable causal model or simulator program is both a world model and a
  theory.
- **Applying a theory** and **explanation-based generalization**, which
  regresses a reusable rule from the theory's explanation of one episode in the
  sense of [Mitchell, Keller, and Kedar-Cabelli](../../sources/explanation-based-generalization-unifying-view.ingest.md).
  Both use the theory without revising it. They are neighbours of refinement,
  not cases of it.
- **Post-hoc rationale, retrieval logs, and deliberation** that produce no
  criticizable intermediate object.

## Misuse cases

- Calling a system a theory-refinement system because it retains prose about
  itself. The term names an operation on the causal path of decisions, not an
  artifact.
- Reserving the term for the full recurrent loop. That the theory shaped a
  decision, or that an outcome bore on it, are reportable at their own strength.
- Reading mechanically checked consequences into a prose part. For a natural-language
  theory, "derived" means interpreted until the part is codified.
- Treating an accepted change as confirmation of the theory that motivated it.

## Word forms

*Theory refinement* is the noun and *refine* the verb. *Reflective theory
refinement* composes with *reflective system*. *Theory-mediated learning* and
*theory-mediated system learning* are retired names for the genus and for the
reflective case. Where a note still uses *theory-mediated* as an adjective, it
means that a theory in this sense is on the causal path of the decision.

---

Relevant Notes:

- [Theory refinement may improve sample efficiency under structured shifts](../theory-refinement-may-improve-sample-efficiency-under-shifts.md) — extends: the payoff conjecture, and the test that would decide whether a model interprets prose theories reliably enough
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder and the functions the reflective case must keep separate
- [Reflective theory refinement has separate structural, epistemic, and implementation lineages](../reflective-theory-refinement-has-three-separate-lineages.md) — extends: the slot-for-slot comparison between the classical loop and the KB's fillers
- [Disconnected witnesses do not establish a full causal path through theory](../disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) — extends: what separate links must share before they compose into one refinement path
- [Citing retained theory at the decision point is a mediation trace](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — mechanism: the cheapest checkable evidence that a theory entered a decision
- [Codification](./codification.md) — grounds: the crossing that gives a part of a theory a computed consequence relation
- [Representational form](./representational-form.md) — grounds: the axis that fixes the assessment route without fixing whether the loop applies
- [Reach-assessment](./reach-assessment.md) — contrasts: the judgment that decides whether a theory deserves its scope; refinement does not supply it
- [Reflective system](./reflective-system.md) — contrasts: an independent condition on what the theory is about
- [Self-improving system](./self-improving-system.md) — contrasts: an independent condition on whether the change persists as operative improvement
- [World models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md) — contrasts: the model-based case revised by fitting, with no part to blame
- [An action model matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md) — grounds: why a stored theory nothing consumes is excluded
- [Three 2026 harnesses expose different repair and retention paths](../evidence/three-2026-harnesses-retain-editable-rules-or-weights-not-rationale.md) — evidenced-by: reported repair operations and the limits of evidence about retained rationale
- [Theory refinement combining analytical and empirical methods](../../sources/theory-refinement-analytical-empirical-methods.ingest.md) — abstracted-from: the classical object, the three inference modes, and consistency as acceptance
- [Automated refinement of first-order Horn-clause domain theories](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md) — abstracted-from: the separation of the refinement task from its realization
- [Explanation-based generalization: a unifying view](../../sources/explanation-based-generalization-unifying-view.ingest.md) — abstracted-from: the established sense of generalizing from a theory without revising it
- [Popper, A realist view of logic, physics, and history](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) — evidenced-by: a theory's consequences exceed what any holder has derived
