# Theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-10 after the
> boundary-case, duplication, and independence checks. The boundary rule,
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
evaluators and evidence procedures, indexes, validators, and the records from
which any of these can be reconstructed.

Users remain outside the builder when they supply questions, cases, evidence,
preferences, acceptance judgments, or later demands. A person is inside the
builder only when the system depends on them for an internal theory-building
role: interpreting what a theory implies, choosing which part to blame or
revise, evaluating a candidate revision, selecting the retained successor, or
repairing the machinery. The same person can occupy both positions in
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
- **Open-ended.** The builder handles theory families for which it holds no
  refinement machinery when the demand arrives. Defined below.

## Open-ended theory builder

An **open-ended theory builder** handles whatever reasonable theories,
questions, cases, and consequences arise as work continues, without their
being listed in advance, including demands that change what it is responsible
for and **theory families** for which it holds no refinement machinery when
the demand arrives. A theory family is a kind of theory for which the
builder's retained machinery cannot derive consequences, localize faults, or
edit parts. A new domain may or may not bring a new family, and a new family
can arrive inside an old domain. *Reasonable* is left informal, in the sense
the [conjecture article](../../articles/automated-software-houses-with-fixed-llms.md#claim)
already uses. The working standard is comparative: given the same demands and
resources, the builder does at least as well as one with people in its
internal theory-building roles.

The declared universality axis, in the terms of
[universal software factory needs a declared universality axis](../../notes/universal-software-factory-needs-a-declared-universality-axis.md),
is refinement-machinery acquisition reach: from permitted evidence, can the
builder determine, construct, and retain the family-specific machinery a new
family needs. Open-endedness is therefore a condition on machinery
acquisition, not on subject matter or on who performs the roles.

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
  computational and family-fixed.
- **Commonplace today**, with the operator inside the boundary, is a theory
  builder. Which of the three conditions it meets is assessed in the
  condition definitions.
- **The research target** is a theory builder meeting all three conditions.
