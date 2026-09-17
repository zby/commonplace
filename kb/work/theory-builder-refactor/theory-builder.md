# Theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-17 against the
> [main-path episodes](./main-path-episodes.md) to declare the evidence
> interface and measure extension through later capability under a budget.
> The episodes are illustrative, not measured results. The boundary rule,
> persistence clause, and evaluation clause are adapted from the
> [software house](../../notes/definitions/software-house.md) definition,
> because they are not specific to software.

A **theory builder** is the complete persistent system responsible for
developing and revising [tentative theories](./tentative-theory.md) about
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

The builder must interpret theories, cases, and consequences to derive
predictions, identify candidate faults, and assess revisions. Its
interpreter is a component of the builder. These roles can fail, and a failed
outcome does not by itself distinguish an interpretation error from a theory
error.

The [resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md)
is a proposed standard for investigating that distinction. Its fidelity and
completion guarantees remain open. An externally assessed outcome comparison
can record a failure without first attributing it to either source. The
ideal is therefore deferred from the main comparison; a claim about the
internal cause of a failure still needs evidence for that attribution.

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

## Evidence interface

An **evidence interface** declares how cases, consequences, and acceptance
judgments reach the builder, what they can assess, and under which
assumptions. It is a parameter of every assessed builder, alongside its
boundary and seed. If a judgment is made internally or no assessment exists
for a claim, say so; declaring an interface does not supply the missing
evidence.

Retain the declaration as a versioned artifact. State both its competence
and applicability assumptions: which claims it can assess, and what must
hold for that assessment to apply. This design draws on the
[competence-and-assumptions account (snapshot required)](../../sources/knowledge-engineering-principles-and-methods.ingest.md)
and [explicit interface mappings (snapshot required)](../../sources/upml-framework-for-knowledge-system-reuse.ingest.md).
It does not assume that naming the fields makes the interface reliable.

| Field | Declaration |
|---|---|
| Assessed claim and scope | Product or theory, claimed capability, task population, exclusions, horizon, and applicability assumptions |
| Task supply and acquisition | Who selects cases, sampling and inclusion rules, passive input or active probes, and acquisition cost |
| Consequences and acceptance | Observable outcomes, objective, judges, what they see, and who may change acceptance requirements |
| Consumption | Version of the product or theory delivered, consumer configuration, and evidence of what later work actually used |
| Feedback | What returns to the builder, its delay and cost, and which roles can access it |
| Evaluation protocol | Seed baseline, comparable conditions and budgets, stopping rule, success criteria, and uncertainty reporting |
| Exposure and renewal | Evidence used to construct or select revisions, evidence reserved for assessment, prior exposure, and how evidence is renewed or reused |

The [externally tested case](./externally-tested-theory-builder.md) fixes
where outcome assessment occurs while permitting internal diagnosis and
active testing. Commonplace's
[downstream protocol](./commonplace-evidence-protocol.md) instantiates these
fields as a proposed study; its unfilled parameters and lack of a run remain
explicit.

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

An evaluation examines particular demands over a particular period under
the declared interface and budget. Those limits bound what its evidence
establishes; they do not define the builder's future responsibilities.
Outcome performance, interpretive fidelity, and the causal effect of a
retained theory are different claims and may require different comparisons.
Neither an outcome success nor an internal approval establishes all three.

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

An **extension** is a retained change to the machinery that demonstrates a
capability beyond what the seed delivered on a stated demand under a stated
budget. Establish it through a comparable seed baseline under that budget
and later work that consumes the retained change. This is a bounded
comparative claim about demonstrated capability; it does not prove that the
seed could never have supplied it.

A single seed failure followed by a candidate success does not establish
extension. The evaluation protocol must state how its comparisons support
the difference, accounting for variation in tasks, consumers, and execution.
Record the seed and successor, retained change, later consumption, measured
effect, and cost in computation, elapsed time, evidence, and internal human
work. Declare both the budget for producing the change and the budget for
later tasks. Merely installing a change does not show that later work used
it, and consumption alone does not show that it caused the improvement.

A new artifact, a rewrite of an existing prompt or procedure, or a change to
model weights can each qualify under this criterion. Artifact differences
identify what changed; outcome comparisons and consumption evidence establish
the demonstrated extension. Probe weight changes through their effects on
later work under the same criterion. Who produced a change, or whether a
general constructor could reach it in principle, does not decide whether it
qualifies. A change proposed for later evaluation remains a candidate
extension until the required evidence exists.

The research question is: under a stated budget, how far can a builder extend
its seed, and does retaining useful extensions make later advances easier?
The comparison basis is a builder with people in its internal roles under the
same demands and resources. Two limits bound the answer. The first is cost:
the search for an extension may not finish within budget. The second is
warrant: the builder must state what support licenses an extension's
consumption path. The [retention-policy draft](./theory-retention-policy.md)
proposes checks relative to a declared objective and records the unresolved
claim that warranted extensions are closed under the seed objective.
Those policy requirements do not follow from calling a theory tentative.

Extension is independent of who performs the roles and of whether machinery
changes are guided by a theory of the builder itself. The two conditions
supply those.

## Exclusions

- A model, a prompt, a retrieval index, an agent harness, or a refinement
  algorithm is not the theory builder merely because the builder uses it.
- A user is not inside the builder because their evidence changed a theory.
- Retaining a theory for inquiry does not establish an extension or license
  routine reliance. State its intended use and support; an extension claim
  needs an observed
  [consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md).
- Persistence is not evidence that the builder retained experience or learned.

## Boundary cases

- **Historical systems** are assessed against their described deployments
  in the [boundary-case assessment](./boundary-case-assessment.md).
  Persistence, external assessment, and reflection are separate questions.
  The Gödel-machine classification remains under review; neither proof-based
  switching nor an internally represented utility decides it by itself.
- **Commonplace's note-review loop**, with the operator performing internal
  roles, is a human-staffed builder. A note's approval is internal evaluation,
  not independent assessment of its downstream consequences. Its ADRs record
  machinery changes, but those records alone do not establish extensions
  under the comparative criterion above.
- **Commonplace as a KB house** is the arrangement proposed in the
  [downstream protocol](./commonplace-evidence-protocol.md). No consuming
  project has yet supplied the records needed to assess it. The three
  [episodes](./main-path-episodes.md) test the definitions, not the builder's
  measured capability.
- **The research target** is a theory builder meeting both conditions, with
  the autonomy warranted, whose extension under a stated budget compares with
  the human-staffed baseline, under the [fixed-model constraint](./README.md#goal).
