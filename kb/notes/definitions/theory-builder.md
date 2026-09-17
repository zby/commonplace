---
description: "Definition — a theory builder is the complete persistent system responsible for developing and revising tentative theories; identified by responsibility and lineage, assessed against a declared boundary, seed, and evidence interface"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory builder

A **theory builder** is the complete persistent system responsible for
developing and revising [tentative theories](./theory-refinement.md#tentative-theory)
about subjects it is asked to investigate. It operates in response to
questions, cases, evidence, requirements, and the consequences that arise
when its theories are applied. It is not necessarily a program, a model, or
a particular method. The KB needs the term because questions about a
learning methodology are questions about this whole system, and the
components usually named, a model, a harness, a refinement algorithm, are
each only part of it.

A theory here is an [addressable theory](./theory-refinement.md#what-the-loop-requires-of-a-theory):
a unit with consequences a case can contradict, parts available as candidate
repair locations, and parts editable separately, in any form. Revision is
[theory refinement](./theory-refinement.md). Development, constructing a
first theory where none exists, is in scope for the builder although
refinement excludes it. The boundary rule, persistence clause, and
evaluation clause below are adapted from the
[software house](./software-house.md) definition, because they are not
specific to software.

## Boundary

The theory builder includes the theories whose revision it remains
responsible for, the machinery it uses, and every person or computational
component that fills an internal theory-building role. The machinery
includes representations and their consequence procedures, repair
operators, evaluators and evidence procedures, models, retained
instructions, tools, indexes, validators, and the records from which any of
these can be reconstructed. The interpreter's current knowledge and
procedures are the part of this machinery available to interpretation.
[WikiSkill](../../sources/wikiskill-persistent-knowledge-for-skill-evolution.ingest.md)
is an external instance of this list with three layers and three roles:
immutable traces, a persistent wiki of diagnoses and intervention history,
and active skills, worked by a maintainer, a proposer, and a solver under a
score gate; the [independent implementation's review](../../agentic-systems/reviews/wikiskill-stahl-g.md)
records computational roles with an operator outside supplying tasks,
scoring, and rounds.

The **seed** is the machinery and theories the builder holds at the
declared start of an assessment. Extension and interventions during the
assessed run are measured against it. The builder may change its machinery
through retained instructions, new tools, changes to model weights, model
replacement, or combinations of these. Fixed models are a constraint on
particular builders or studies, not part of this definition.

Users remain outside the builder when they supply questions, cases,
evidence, preferences, acceptance judgments, or later demands. A person is
inside the builder only when the system depends on them for an internal
theory-building role: constructing a first theory, interpreting what a
theory implies, choosing which part to blame or revise, producing a
candidate revision, evaluating a candidate theory, selecting the theory to
retain, or extending and repairing the machinery. The same person can
occupy both positions in different interactions. The boundary follows the
role, not the person, so an attribution must declare the boundary it was
assessed against.

## Evidence interface

An **evidence interface** declares how cases, consequences, and acceptance
judgments reach the builder, which claims they can assess, and under which
assumptions. It is a parameter of every assessed builder, alongside its
boundary and seed, retained as a versioned artifact that states both its
competence and its applicability assumptions, following the
[competence-and-assumptions account (snapshot required)](../../sources/knowledge-engineering-principles-and-methods.ingest.md)
and [explicit interface mappings (snapshot required)](../../sources/upml-framework-for-knowledge-system-reuse.ingest.md).
The declaration covers the assessed claim and its scope, task supply and
acquisition mode, consequences and who judges them, consumption evidence,
feedback, the evaluation protocol, and how evidence is exposed, reserved,
and renewed. Where a judgment is made internally, or no assessment exists
for a claim, the declaration says so. The
[externally tested theory builder](./externally-tested-theory-builder.md)
is the case in which the interface supplies assessment from outside.

## Persistence

Persistence means continuity of responsibility for the theories across
demands and consequences, together with lineage: each successor state of
the builder is produced through the preceding state's own revision process.
No particular theory, procedure, evaluator, or part of the seed methodology
need survive; the builder is identified by responsibility and lineage, not
by any component. A change installed from outside that process is an
intervention. It is recorded as one, and the successor it produces is not
credited to the builder. Whether locally warranted revisions compose into a
warranted lineage is assessed, not assumed; it is the first open question in
[a claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md).
In the externally tested case the lineage is assessed at the outcome level
through the evidence interface, which lies outside the builder and is not
replaced by it.

Persistence establishes neither retention nor learning. A builder whose
fixed machinery suffices for every admitted demand still meets this
definition. A system that runs once over supplied cases and holds no
continuing responsibility for the result is not persistent in this sense.
Retention is the builder's, not the interpreter's: the interpreter
proposes, the evaluators assess, and the builder retains.

## Extension

An **extension** is a retained change to the machinery that demonstrates a
capability beyond what the seed delivered on a stated demand under a stated
budget. It is established by a comparable seed baseline under that budget
and by later work that consumes the retained change. The baseline is the
same later demand run without the retained change under matched conditions,
not the seed's earlier performance on an earlier demand, since a gain
between episodes confounds the change with task drift, model variance, and
scoring noise; [PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
builds its evaluation on that matched ablation and names the question
performance attribution. This is a bounded comparative claim about
demonstrated capability, not a proof that the seed could never have
supplied it.

A new artifact, a rewrite of an existing prompt or procedure, or a change
to model weights can each qualify. Artifact differences identify what
changed; outcome comparisons and consumption evidence establish the
extension, and weight changes are probed through their effects on later
work. Who produced the change, or whether a general constructor could reach
it in principle, does not bear on whether it qualifies. Extension is
independent of who performs the roles and of whether machinery changes are
guided by a theory of the builder itself; the two conditions in Scope
supply those.

## Scope

- **Two independent conditions** qualify a theory builder, each defined
  against the same declared boundary. A [reflective theory builder](./reflective-theory-builder.md)
  refines a theory of its own theory-building organization. An
  [autonomous theory builder](./autonomous-theory-builder.md) performs
  every internal role computationally. Extension is not a third condition;
  it is the quantity a research question measures.
- **An evaluation** examines particular demands over a particular period
  under the declared interface and budget. Those limits bound what its
  evidence establishes; they do not define the builder's future
  responsibilities. Outcome performance, interpretive fidelity, and the
  causal effect of a retained theory are different claims and may require
  different comparisons.
- **Interpretation** is a role inside the builder: deriving predictions,
  identifying candidate faults, and assessing revisions. A failed outcome
  does not by itself distinguish an interpretation error from a theory
  error. No standard for that attribution is part of this definition; an
  outcome comparison records a failure without attributing it, and a claim
  about the cause needs its own evidence.

## Exclusions

- A model, a prompt, a retrieval index, an agent harness, or a refinement
  algorithm is not the theory builder merely because the builder uses it.
- A user is not inside the builder because their evidence changed a theory.
- Persistence is not evidence that the builder retained experience or
  learned.
- Installing a change is not evidence that later work used it, and use is
  not evidence that it caused an improvement; an extension claim needs an
  observed [consumption path](../an-action-model-matters-only-through-its-consumption-path.md)
  and an outcome comparison.
- Retaining a theory for inquiry neither establishes an extension nor
  licenses routine reliance on it.
- An outcome success establishes outcome performance; it does not establish
  interpretive fidelity or the causal effect of a retained theory, and an
  internal approval establishes none of the three.

## Misuse Cases

- Calling a language model, an agent harness, or a review pipeline a theory
  builder when it is one component of the system that holds responsibility.
- Counting a user inside the builder because their tasks or feedback changed
  a theory, when they performed no internal role.
- Crediting the builder with an extension that an operator installed from
  outside its revision process; that is an intervention and, if it replaces
  the machinery wholesale, a new seed.
- Reading persistence as retention or learning, or a stored theory nothing
  consumes as a theory the builder is responsible for.

## Boundary cases

- **FORTE** is not a theory builder: it revises a supplied theory in one
  offline run and holds no continuing responsibility for it.
- **The Gödel machine** is persistent, holds a self-representation, and
  rewrites itself computationally. Whether it is a theory builder turns on
  whether its retained content is revised against evidence rather than by
  proof alone, which is assessed per deployment and remains open; an
  internally represented utility does not by itself decide it, as
  [Gödel machines are a proof-governed case of self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md)
  records.
- **Commonplace's note-review loop**, with the operator performing internal
  roles, is a human-staffed theory builder. A note's approval is internal
  evaluation, not independent assessment of its downstream consequences.
- **Commonplace producing a KB for a consuming project** is a theory
  builder whose product is the delivered KB and its supporting software,
  and whose evidence interface is that product's use; it becomes an
  observed externally tested instance when a consuming project supplies the
  release, consumption, and outcome records.
- **Total replacement through the builder's own process** is the same
  builder: a lineage in which every theory, procedure, evaluator, and part
  of the seed methodology has been revised away still satisfies persistence.
  An operator installing a different framework in its place starts a new
  seed.

---

Relevant Notes:

- [Theory refinement](./theory-refinement.md) — defined-in: the revision operation, the addressable theory it requires, and the borrowed tentative-theory status
- [Software house](./software-house.md) — grounds: the boundary, persistence, and evaluation clauses this definition adapts
- [Externally tested theory builder](./externally-tested-theory-builder.md) — extends: the case in which the evidence interface supplies assessment from outside
- [Reflective theory builder](./reflective-theory-builder.md) — extends: the first independent condition
- [Autonomous theory builder](./autonomous-theory-builder.md) — extends: the second independent condition
- [A claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md) — extends: what the builder must supply for itself when the interface does not assess a claim
- [An action model matters only through its consumption path](../an-action-model-matters-only-through-its-consumption-path.md) — grounds: why installation and retention alone establish nothing
- [Gödel machines are a proof-governed case of self-modification](../goedel-machines-are-a-proof-governed-case-of-self-modification.md) — contrasts: the proof-governed admission route and why its classification stays open
