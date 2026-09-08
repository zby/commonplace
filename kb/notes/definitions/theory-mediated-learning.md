---
description: "Definition — theory-mediated learning is model-based learning whose model is a theory: explanatory, addressable, and revised by reasoning; a latent world model is model-based but not theory-mediated"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory-mediated learning

**Theory-mediated learning** is model-based learning in which the model is a
theory. A learner is model-based when an internal model of its target stands
between evidence and behavior change; a [learned world
model](../world-models-assess-explanatory-reach-through-action-conditioned.md)
is the familiar case. The model is a **theory** when it is explanatory, saying
why and not only what happens next; addressable, a stable unit whose
assumptions, scope, and parts can be inspected; and revised by reasoning, by
deriving a consequence, exposing an assumption, comparing a rival, or
narrowing a scope, not only by further fitting. **Mediated** is causal: the
learner operates on the theory's content rather than holding it beside a
decision it would have made anyway.

The term names a property, not a mechanism. Its species are the established
operations on a theory: **applying** it, which is deduction and the minimum
mediation requires; **explanation-based generalization**, regressing a
reusable rule from the theory's explanation of one episode, in the sense of
[Mitchell, Keller, and
Kedar-Cabelli](../../sources/explanation-based-generalization-unifying-view.ingest.md);
and **theory refinement**, revising the theory when empirical failure
localizes a defect, in the sense of [Ourston and
Mooney](../../sources/theory-refinement-analytical-empirical-methods.ingest.md).
Classical theory refinement is therefore an instance of this term, and the
[software house regime](../../articles/the-software-house-as-the-unit-of-training.md)
is theory refinement with different fillers in the same slots. The payoff is
argued in [theory-mediated learning may improve sample efficiency under
structured shifts](../theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).

## Scope

- **One mediated stage suffices, and one episode is the minimum unit.**
  Retaining the theory, refining it, and reusing the refined state are further
  links on the [evidence
  ladder](../theory-mediated-self-improvement-needs-interpretation-and-retention.md#evidence-forms-a-ladder),
  each needing its own evidence. A contemporaneous [citation at the decision
  point](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
  is the cheapest evidence for the first link.
- **Any representational form.** [Form](./representational-form.md) fixes the
  assessment route, not whether mediation obtains. Addressability comes in
  degrees: an indivisible document can be replaced but not rescoped.
- **Any machinery.** An LLM, a program, or a mixture may do the applying and
  revising.
- **Not a success term.** A false theory mediates as readily as a true one.
  Whether a theory earns its scope is [reach-assessment](./reach-assessment.md),
  which mediation neither supplies nor presupposes.
- **Independent of what the theory is about.** A theory of an external target
  and a theory of the learner's own organization are applied, generalized
  from, and refined alike. Whether the learner is
  [reflective](./reflective-system.md), and whether the change persists as
  [self-improvement](./self-improving-system.md), are separate conditions.

## Exclusions

- **A stored theory nothing consumes**, since [a representation matters only
  through its consumption
  path](../an-action-model-matters-only-through-its-consumption-path.md).
- **A latent world model as such.** It is model-based but revised only by
  training, with scope discoverable only behaviorally. An inspectable causal
  model or simulator program is both a world model and a theory.
- **Rules whose reasons are not retained.** With no mechanism to derive from,
  a correction to one rule reaches none of the others that share its unstated
  reason.
- **Post-hoc rationale, retrieval logs, and deliberation** that produce no
  criticizable intermediate object.

## Misuse cases

- Calling a system theory-mediated because it retains prose about itself. The
  term names a causal path, not an artifact.
- Reserving the term for the full recurrent loop. Narrower claims are
  reportable at their own strength.
- Reading it as endorsing natural language as the carrier. Prose theories are
  a fact about available substrates, not part of the meaning.
- Treating an accepted change as confirmation of the theory that motivated it.

## Word forms

Hyphenate the adjective, *theory-mediated*; the noun is spaced, *theory
mediation*. Bare *mediation* names the first link on the ladder. *Reflective
theory refinement*, formerly *theory-mediated system learning*, composes
*theory refinement* with *reflective system* and is defined by neither alone.

---

Relevant Notes:

- [Theory-mediated learning may improve sample efficiency under structured shifts](../theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — extends: the payoff conjecture and the test that would decide it
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: the evidence ladder whose first rung this definition names
- [Disconnected witnesses do not establish a full causal path through theory](../disconnected-witnesses-do-not-establish-a-theory-mediated-path.md) — extends: what separate links must share before they compose into one path
- [Citing retained theory at the decision point is a mediation trace](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — mechanism: the cheapest checkable evidence for mediation
- [Reach-assessment](./reach-assessment.md) — contrasts: the judgment that decides whether a theory deserves its scope; mediation does not supply it
- [Representational form](./representational-form.md) — grounds: the axis that fixes assessment route without fixing whether mediation obtains
- [Reflective system](./reflective-system.md) — contrasts: an independent condition on what the theory is about
- [World models assess explanatory-reach through action-conditioned prediction](../world-models-assess-explanatory-reach-through-action-conditioned.md) — contrasts: the familiar model-based case that lacks the three properties of a theory
- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) — extends: places the reflective case against its lineages
- [Three 2026 harnesses retain rules or weights, not a revisable theory](../evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md) — evidenced-by: worked cases on the near side of the boundary
- [Explanation-based generalization: a unifying view](../../sources/explanation-based-generalization-unifying-view.ingest.md) — abstracted-from: the established sense of generalizing from a theory without revising it
- [Theory refinement combining analytical and empirical methods](../../sources/theory-refinement-analytical-empirical-methods.ingest.md) — abstracted-from: the established sense of revising a fallible explicit theory from empirical failure
