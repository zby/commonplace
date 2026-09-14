# Theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-14 to define
> open-endedness through machinery extension and leave model changes open.
> The boundary rule,
> persistence clause, and evaluation clause are copied from the
> [software house](../../notes/definitions/software-house.md) definition,
> because they are not specific to software.

A **theory builder** is the complete persistent system responsible for
developing and revising [theories](../../notes/definitions/theory-refinement.md#what-the-loop-requires-of-a-theory)
about subjects it is asked to investigate. It operates in response to
questions, cases, evidence, requirements, and the consequences that arise when
its theories are applied. It is not necessarily a program, a model, or a
particular method.

A theory here is what the refinement loop requires: a unit with consequences a
case can contradict, parts available as candidate repair locations, and parts
editable separately. Form is free: natural language, program, causal model, or
a mixture. Revision is [theory refinement](../../notes/definitions/theory-refinement.md).
Development, constructing a first theory where none exists, is in scope for
the builder although it is excluded from refinement; the builder performs both
operations, and refinement remains the one the KB's evidence standards cover.

## Boundary

The theory builder includes the theories whose revision it remains
responsible for, the machinery it uses, and every person or computational
component that fills an internal theory-building role. The machinery includes
representations and their consequence procedures, repair operators,
evaluators and evidence procedures, models, retained instructions, tools,
indexes, validators, and the records from which any of these can be
reconstructed.

The builder may change its machinery through retained instructions, new tools,
changes to model weights, model replacement, or combinations of these. Fixed
models are a constraint on particular builders or studies. Neither this
definition nor the conditions below require that constraint.

Users remain outside the builder when they supply questions, cases, evidence,
preferences, acceptance judgments, or later demands. A person is inside the
builder only when the system depends on them for an internal theory-building
role: constructing a first theory, interpreting what a theory implies,
choosing which part to blame or revise, producing a candidate revision,
evaluating a candidate theory, selecting the theory to retain, or extending
and repairing the machinery. The same person can occupy both positions in
different interactions. The boundary follows the role, not the person. An
attribution must therefore declare the boundary it was assessed against.

## Persistence

Persistence means continuity of responsibility for the theories across
demands and consequences. It establishes neither retention nor learning. A
builder whose fixed machinery suffices for every admitted demand still meets
this definition. A system that runs once over supplied cases and holds no
continuing responsibility for the result is not persistent in this sense.

## Evaluation

An evaluation examines particular demands over a particular period. Those
limits bound what its evidence establishes; they do not define the builder's
future responsibilities.

## Independent conditions

Three conditions qualify a theory builder. Each is independent of the other
two, and each is defined against the same declared boundary.

- **Reflective.** The builder refines a theory of its own theory-building
  organization. See [reflective theory builder](./reflective-theory-builder.md).
- **Autonomous.** Every internal theory-building role is computational. See
  [autonomous theory builder](./autonomous-theory-builder.md).
- **Open-ended.** The builder can extend its theory-building machinery as
  demands arise, without requiring the needed extensions to be specified in
  advance. Defined below.

## Open-ended theory builder

An **open-ended theory builder** can extend its theory-building machinery in
response to demands encountered during its continuing work, without requiring
the needed extensions to be specified in advance.

When current machinery is inadequate, the builder determines what additional
capability is needed, constructs or adopts machinery that supplies it, and
retains it for later theory work. A new subject may be handled with existing
machinery; work on a familiar subject may expose a need for an extension.
Installing a predetermined extension alone does not establish open-endedness.

Open-endedness does not guarantee that every demand can be met. An evaluation
establishes particular demonstrated extensions under stated conditions; it
does not establish unrestricted future capability. The breadth and reliability
of acquisition, and performance relative to a builder with people in its
internal roles, are questions for evaluation.

Open-endedness is independent of who performs those roles and of whether
machinery changes are guided by a theory of the builder itself. Autonomy and
reflection supply those separate conditions.

## Exclusions

- A model, a prompt, a retrieval index, an agent harness, or a refinement
  algorithm is not the theory builder merely because the builder uses it.
- A user is not inside the builder because their evidence changed a theory.
- A stored theory nothing consumes does not count as a theory the builder is
  responsible for, since
  [a representation matters only through its consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md).
- Persistence is not evidence that the builder retained experience or learned.

## Boundary cases

- **FORTE** is not a theory builder: it revises a supplied theory in one
  offline run and holds no continuing responsibility for it. Its machinery is
  computational and specified before the run.
- **Commonplace today**, with the operator inside the boundary, is a theory
  builder. Which of the three conditions it meets is assessed in the
  condition definitions.
- **The research target** is a theory builder meeting all three conditions.
