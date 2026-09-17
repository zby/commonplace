# Theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-14 in a later
> session to place the interpreter and fallible theory under the builder,
> replace the open-ended condition with extension as the measured quantity,
> and add the Gödel machine as a boundary case. The boundary rule,
> persistence clause, and evaluation clause are copied from the
> [software house](../../notes/definitions/software-house.md) definition,
> because they are not specific to software.

A **theory builder** is the complete persistent system responsible for
developing and revising [fallible theories](./fallible-theory.md) about
subjects it is asked to investigate. It operates in response to questions,
cases, evidence, requirements, and the consequences that arise when its
theories are applied. It is not necessarily a program, a model, or a
particular method.

A theory here is what the refinement loop requires: a unit with consequences a
case can contradict, parts available as candidate repair locations, and parts
editable separately. Form is free: natural language, program, causal model, or
a mixture. Revision is [theory refinement](../../notes/definitions/theory-refinement.md).
Development, constructing a first theory where none exists, is in scope for
the builder although it is excluded from refinement; the builder performs both
operations, and refinement remains the one the KB's evidence standards cover.

## Interpretation

The internal roles that read theories, cases, and consequences, such as
interpreting what a theory implies, choosing which part to blame, and judging
whether a case contradicts a consequence, are specified against the
[resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md).
The builder's interpreter is a component. The ideal says what faithful
performance of those roles would be within a budget, and an evaluation scores
the actual interpreter against it on the tasks it completed within budget.
Errors in interpreting a theory are thereby separated from errors in the
theory, which fallibility covers.

## Boundary

The theory builder includes the theories whose revision it remains
responsible for, the machinery it uses, and every person or computational
component that fills an internal theory-building role. The machinery includes
representations and their consequence procedures, repair operators,
evaluators and evidence procedures, models, retained instructions, tools,
indexes, validators, and the records from which any of these can be
reconstructed. The interpreter's current knowledge and procedures are the
part of this machinery available to interpretation.

The **seed** is the machinery and theories the builder holds at the declared
start of an assessment. Extension and interventions during the assessed run
are measured against it.

The builder may change its machinery through retained instructions, new tools,
changes to model weights, model replacement, or combinations of these. Fixed
models are a constraint on particular builders or studies. Neither this
definition nor the conditions below require that constraint.
The [workshop's research target](./README.md#goal) does impose it: model
weights are pinned to versions publicly available as of 2026-09-17, and
training develops the builder's instructions, knowledge, tools, and
orchestration as natural-language and symbolic artifacts. The builder is
the unit being trained; the model weights remain fixed.

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

Retention is the builder's, not the interpreter's. The interpreter proposes,
the evaluators assess, and the builder retains. A retained extension changes
the machinery available to later work.

## Evaluation

An evaluation examines particular demands over a particular period. Those
limits bound what its evidence establishes; they do not define the builder's
future responsibilities. The tasks an evaluation ran bound what it
establishes about interpretive fidelity and about extension. The interpreter
does not declare its own scope; the evaluation does.

## Independent conditions

Two conditions qualify a theory builder. Each is independent of the other,
and each is defined against the same declared boundary.

- **Reflective.** The builder refines a theory of its own theory-building
  organization. See [reflective theory builder](./reflective-theory-builder.md).
- **Autonomous.** Every internal theory-building role is computational. See
  [autonomous theory builder](./autonomous-theory-builder.md).

Extension of the machinery is not a third condition. It is the quantity the
research question measures, defined next.

## Extension

An **extension** is machinery retained after the seed that supplies a
capability the seed's retained machinery did not have. It is judged by a diff
of retained artifacts against the seed, not by what the builder could reach
in principle: any builder containing a general constructor reaches any
machinery in principle, so reachability distinguishes nothing. Activating a
component the seed already retained, or changing a value in a slot the seed
already had, is not extension, because the capability was already held. How
the extension is produced is unrestricted: a person, a model, or a search
procedure over programs. Exhaustive search qualifies.

Bare extension is therefore cheap. What an evaluation establishes is the
record of demonstrated extensions: for each, the demand that exposed the gap,
the artifact added, a later episode of theory work that consumed it, and what
it cost in computation, elapsed time, and evidence. An evaluation does not
establish that every future demand can be met.

The research question is: under a stated budget, how far can a builder extend
its seed, and does retaining useful extensions make later advances easier?
The comparison basis is a builder with people in its internal roles under the
same demands and resources. Two limits bound the answer. The first is cost:
the search for an extension may not finish within budget. The second is
warrant: an extension is retained under the [fallible-theory](./fallible-theory.md)
clauses, so it must be warranted for its consumption path by evaluators
judged against an unchanged objective. Whether that second limit is a closure
over the seed objective is unsettled; see the fallible-theory definition.

Extension is independent of who performs the roles and of whether machinery
changes are guided by a theory of the builder itself. The two conditions
supply those.

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
- **The Gödel machine** is persistent, holds a self-representation, rewrites
  itself computationally, and can rewrite any part of its code including the
  searcher. It would meet both conditions and extend without limit in
  principle. It is excluded by the theory clause: its axioms are retained by
  proof and never revised against evidence, so they are not fallible
  theories. It is the contrast case, the builder with everything but
  fallibility, and it shows that reflection, autonomy, and in-principle
  extension are prior art. Its two known limits, proof not found within
  resources and rewrite not licensable under the axioms, are the two limits
  on extension above with fallible checks in place of proofs.
- **Commonplace today**, with the operator inside the boundary, is a theory
  builder. It is reflective and not autonomous; the condition definitions
  assess this. Its extension record is the ADR set: the review system, the
  tag-README marks, the premise-decomposition gate, and the collection
  contracts were each added after a demand exposed a gap and are each
  consumed by later theory work.
- **The research target** is a theory builder meeting both conditions, with
  the autonomy warranted, whose extension under a stated budget compares with
  the human-staffed baseline, under the [fixed-model constraint](./README.md#goal).
