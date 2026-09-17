# Theory builder

> **Status:** Workshop definition, 2026-09-10; revised 2026-09-17 against the
> [main-path episodes](./main-path-episodes.md) to declare the evidence
> interface and measure extension through later capability under a budget,
> and trimmed the same day. The boundary rule, persistence clause, and
> evaluation clause are adapted from the
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

The builder interprets theories, cases, and consequences to derive
predictions, identify candidate faults, and assess revisions. Its interpreter
is a component of the builder. A failed outcome does not by itself
distinguish an interpretation error from a theory error. The
[resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md)
is a proposed standard for that attribution; it is deferred from the main
comparison, which records a failure without attributing it.

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
models are a constraint on particular builders or studies, not part of this
definition. The [workshop's research target](./README.md#goal) imposes it:
model weights are pinned to versions publicly available as of 2026-09-17, and
training develops the builder's instructions, knowledge, tools, and
orchestration as natural-language and symbolic artifacts.

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
judgments reach the builder, which claims they can assess, and under which
assumptions. It is a parameter of every assessed builder, alongside its
boundary and seed, retained as a versioned artifact that states both its
competence and its applicability assumptions, following the
[competence-and-assumptions account (snapshot required)](../../sources/knowledge-engineering-principles-and-methods.ingest.md)
and [explicit interface mappings (snapshot required)](../../sources/upml-framework-for-knowledge-system-reuse.ingest.md).
Where a judgment is made internally, or no assessment exists for a claim,
the declaration says so.

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
where outcome assessment occurs. Commonplace's
[downstream protocol](./commonplace-evidence-protocol.md) instantiates these
fields as a proposed study.

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
budget. It is established by a comparable seed baseline under that budget
and by later work that consumes the retained change. The baseline is the
same later demand run without the retained change under matched conditions,
not the seed's earlier performance on an earlier demand: a gain between
episodes confounds the change with task drift, model variance, and scoring
noise. [PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
builds its evaluation on that matched ablation and names the resulting
question performance attribution. This is a bounded comparative claim about
demonstrated capability, not a proof that the seed could never have
supplied it.

The record of an extension holds the seed and successor, the retained
change, its later consumption, the measured effect, and the cost in
computation, elapsed time, evidence, and internal human work, with separate
budgets for producing the change and for the later tasks. A new artifact, a
rewrite of an existing prompt or procedure, or a change to model weights can
each qualify. Artifact differences identify what changed; outcome
comparisons and consumption evidence establish the extension, and weight
changes are probed through their effects on later work. Who produced the
change, or whether a general constructor could reach it in principle, does
not bear on whether it qualifies.

The research question is: under a stated budget, how far can a builder extend
its seed, and does retaining useful extensions make later advances easier?
The comparison basis is a builder with people in its internal roles under the
same demands and resources. Two limits bound the answer. The first is cost:
the search for an extension may not finish within budget. The second is
warrant: the builder must state what support licenses an extension's
consumption path. The [retention-policy draft](./theory-retention-policy.md)
proposes those checks and records the unresolved claim that warranted
extensions are closed under the seed objective.

Extension is independent of who performs the roles and of whether machinery
changes are guided by a theory of the builder itself. The two conditions
supply those.

## Exclusions

- A model, a prompt, a retrieval index, an agent harness, or a refinement
  algorithm is not the theory builder merely because the builder uses it.
- A user is not inside the builder because their evidence changed a theory.
- Persistence is not evidence that the builder retained experience or learned.
- Installing a change is not evidence that later work used it, and use is
  not evidence that it caused an improvement; an extension claim needs an
  observed [consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md)
  and an outcome comparison.
- Retaining a theory for inquiry neither establishes an extension nor
  licenses routine reliance on it.
- An outcome success establishes outcome performance; it does not establish
  interpretive fidelity or the causal effect of a retained theory, and an
  internal approval establishes none of the three.

## Boundary cases

- **Historical systems** are assessed against their described deployments
  in the [boundary-case assessment](./boundary-case-assessment.md), which
  treats persistence, external assessment, and reflection as separate
  questions. The Gödel-machine classification remains under review.
- **Commonplace's note-review loop**, with the operator performing internal
  roles, is a human-staffed builder. A note's approval is internal
  evaluation, not independent assessment of its downstream consequences.
  Its ADRs record machinery changes without the comparison the extension
  criterion requires.
- **Commonplace as a KB house** is the arrangement proposed in the
  [downstream protocol](./commonplace-evidence-protocol.md); no consuming
  project has yet supplied the records needed to assess it.
- **The research target** is a theory builder meeting both conditions, with
  the autonomy warranted, whose extension under a stated budget compares with
  the human-staffed baseline, under the [fixed-model constraint](./README.md#goal).
