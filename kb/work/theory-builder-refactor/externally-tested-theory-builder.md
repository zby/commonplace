# Externally tested theory builder

> **Status:** Workshop definition, 2026-09-15. Added after the operator asked
> why the workshop grew more complicated than the research-program articles
> it was meant to simplify. The answer is that the articles work in a special
> case whose outside supplies three things the general
> [theory builder](./theory-builder.md) must define for itself. This file
> names that special case and keeps the general case intact, because the
> general case is where the difficulties show. Not a library definition.

Every theory builder has an **evidence interface**: what, outside its
boundary, supplies the cases, consequences, and acceptance judgments for the
theories it is responsible for. The general definition leaves the interface
unspecified. This definition fixes it.

An **externally tested theory builder** is a [theory builder](./theory-builder.md)
whose evidence interface supplies all three of the following from outside the
declared boundary:

1. **An external falsifier.** Consequences arise when a theory is applied,
   and they contradict the theory without the builder deciding what counts as
   a contradiction. A failing test, an invalid release, a bug report, and a
   user's rejection of visible behaviour are contradictions by the interface's
   own rule, not by the builder's judgment.
2. **An external objective.** Acceptance of outcomes is judged outside the
   boundary, and the outside may change what it will accept, including what
   the builder is responsible for. Objective change is therefore licensed from
   outside continuously, as
   [revising an improvement objective is licensed from outside it](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md)
   requires.
3. **An outcome level independent of the builder's evaluators.** Because of
   the first two, the builder's performance can be measured on outcomes the
   builder did not assess. Its internal evaluators can be wrong without the
   measurement being wrong.

The paradigm instance is a [software house](../../notes/definitions/software-house.md):
the product's operation supplies the falsifier, the users' acceptance of
visible behaviour supplies the objective, and the two together supply the
outcome level. The research-program articles describe an automated software
house; in this vocabulary that is an
[autonomous](./autonomous-theory-builder.md) externally tested theory
builder, and the four witness conditions of the
[conjecture article](../../articles/automated-software-houses-with-fixed-llms.md#what-a-witness-house-must-show)
are its evaluation.

The interface is a parameter, so the special case has degrees. An interface
may supply a falsifier for some consequences and not others, or acceptance
for outcomes but not for the theories behind them. The definition names the
limit in which all three are supplied; a builder is closer to it the more of
its consequences and acceptances arrive from outside.

## What the general case must supply for itself

Each of the three supplied items corresponds to one of the general
definitions this workshop had to add. Removing the item is what makes the
definition necessary.

| Supplied by the interface | Definition the general case needs instead | What the definition costs |
|---|---|---|
| External falsifier | [Fallible theory](./fallible-theory.md): warrant per claim and scope, a consumption threshold, a frontier of claims below it. The builder must say when a claim counts as contradicted and how much support retention needs. | The warrant-policy clauses now under review, and the literature checks closing condition 3 requires. |
| External objective | The [objective clause](./fallible-theory.md#the-objective-clause) and the seed-closure question. With no acceptance arriving from outside, the objective is whatever the seed evaluators judge, and no change to it is licensed. | The closure claim, contested in the [Gödel-machine comparison](./goedel-machine-comparison.md), and the autonomy draft's objective section. |
| Independent outcome level | The [resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md): a standard for separating an error in interpreting a theory from an error in the theory, since no outcome absorbs both. | The interpreter's scope and guarantee questions, and the semantic-work record's paradox tests. |

In the special case the same questions exist but do not need answering for
the conjecture. An interpretation error and a theory error both show up as a
product that fails, and the comparative standard, a human-staffed builder
under the same demands, scores the failure without attributing it. Evaluator
warrant is still what predicts performance beyond the tested horizon, which
is why the training article's four situations of second-order learning
remain in scope; but the witness does not depend on it.

The closure worry is the clearest example. The
[autonomy draft](./autonomous-theory-builder.md#the-objective) infers that
with no person inside the boundary no objective change is licensed. Its own
boundary rule keeps users outside supplying acceptance judgments. The
inference holds only when the interface supplies no acceptance, that is,
outside the special case. Inside it, the objective is revised from outside at
every request, and the question is moot. The two claims are consistent once
the interface is stated; they looked contradictory because it was not.

## What does not simplify

The special case removes definitions, not work. The builder still performs
every internal role: interpreting what a theory implies, choosing which part
to blame, producing and selecting revisions, and extending the machinery.
Credit assignment along the internal path stays hard. A failure may lie in
the product theory, the evaluator that admitted a change, the retrieval that
never surfaced the theory, or a skipped check, and the interface only reports
that the product failed. The
[training article](../../articles/the-software-house-as-the-unit-of-training.md#why-this-is-theory-refinement)
lists these as the cases that force a theory of the builder's own path.

The interface also has costs the general definitions do not model. A
falsifier that arrives late, rarely, or at great expense weakens the outcome
level in practice while leaving it defined. The
[transition-closure supplement](../../articles/transition-closure-and-continuation-reliability.md)
carries this as the input process's effect on the evaluation.

## Consequence for the conjecture

The workshop's [conjecture](./README.md#goal) counts doctrine edits per new
area at reliability comparable to a human-staffed builder. That comparison
needs an outcome measure per area, and the outcome measure is the area's
evidence interface. Testing the conjecture in an area therefore begins by
declaring what plays the role of bug reports there. An area whose interface
supplies all three items is a software-house area, and the articles' witness
protocol applies with the product replaced by the area's product. An area
whose interface supplies less is the general case, and the general
definitions say what the builder must then decide for itself.

Whether broad theory building requires the builder to become a software
house, the [side conjecture](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md),
is unchanged. This definition says only that the software house is the case
where the interface is complete, not that every area has such an interface.

## Boundary cases

- **An automated software house** is an autonomous externally tested theory
  builder. The product supplies the falsifier, users supply the objective,
  and the four witness conditions measure at the outcome level.
- **Commonplace today** is not externally tested, and this is why the
  general definitions were needed to describe it. Its theories are
  methodology, and the operator's acceptance of a methodology note is the
  same kind of act as internal evaluation: judging whether the theory is
  good. Declaring an interface would move it toward the special case. Agent
  task outcomes on work that consumes the KB are a candidate falsifier, and
  the review system's verdicts are internal evaluation, not acceptance.
- **The Darwin Gödel Machine** has an external falsifier and an external
  objective, the coding benchmark, and measures at the outcome level. It is
  not a theory builder by the persistence clause: it runs a search over
  agents and holds no continuing responsibility for any of them. The marker
  deletion shows the interface's known weakness, an objective proxied by a
  score the builder can reach without the outcome.
- **The Gödel machine** has no external objective. Its utility function is
  an internal formalization, and observations enter through it. It is not a
  theory builder by the theory clause, and it would not be externally tested
  if it were.
- **FORTE** has an external falsifier, the supplied examples, and no
  persistence. It is not a theory builder.
