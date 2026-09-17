# Resource-bounded ideal interpreter

> **Status:** Deferred workshop specification, begun 2026-09-14 and revised
> 2026-09-17 for the [main path](./main-path-plan.md). This is an attribution
> device under development, not a prerequisite of the downstream comparison.
> [Semantic work and the ideal interpreter](./semantic-work-and-the-ideal-interpreter.md)
> retains the earlier argument and paradox tests. Fidelity, completion,
> abstention, and realizability remain open; this is not a library definition.

A **resource-bounded ideal interpreter** is a proposed analytic device for
separating errors in interpreting a theory from errors in the theory. Its
intended standard is faithful interpretation on a declared class of tasks
and representations, together with attempts at conceptual development using
declared knowledge and procedures under a resource model. A budget alone
does not specify that class or establish fidelity on it.

The [main-path comparison](./commonplace-evidence-protocol.md) can assess
downstream outcomes without first assigning each failure to interpretation
or theory. Either can contribute to a failed product. Diagnosis and a claim
about the reflective mechanism still need evidence, but they need not assume
a universally faithful interpreter. The stronger attribution question is
deferred in the [general-case obligations](./general-case-obligations.md).

**Semantic work**, the activity the interpreter performs, is defined in the
discussion record: establishing, examining, or revising how expressions and
concepts represent a subject and bear on a question. It extends the KB's use
of the term in
[semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md)
by adding conceptual revision.

## Scope to declare before assessment

This table is the workshop's proposed specification, not a theorem that
interpreters meeting it exist.

| Dimension | Required declaration |
|---|---|
| Tasks and representations | Admitted questions, representation languages and forms, contextual conventions, and what counts as a completed interpretation for each task |
| Program language and architecture | The implementable operations, component boundaries, tools, and interfaces available to the interpreter |
| Context and knowledge | Supplied context, retained knowledge, starting procedures, access limits, and whether any of these may change during assessment |
| Objective | What the interpretation is for, which commitments must be preserved, which revisions may be proposed, and the success criteria fixed before outputs are judged |
| Resources | Compute, context capacity, elapsed time, search, evidence access, and other charged operations, with their limits |
| Environment | The cases and evidence the interpreter can encounter, their selection rule, and the conditions under which the assessment applies |
| Horizon | The assessed sequence or duration, stopping rule, and treatment of changes to the declared conditions |

Scope is fixed by the assessment protocol, not retrospectively by which
tasks the interpreter completed. Changing these declarations changes what
the assessment supports. Fidelity and completion must both be assessed within
them; neither is established by labelling the component ideal.

## Faithful interpretation

A faithful interpretation of a representation, given its context:

- preserves the commitments the context fixes;
- preserves the alternatives where the context leaves consequential readings
  open, instead of selecting one silently. Reporting alternatives can complete
  an interpretation task if it meets that task's declared requirements; the
  underlying question may remain unresolved;
- reports a revised commitment as a change, never as what the text always
  meant;
- identifies what a claim commits to without deciding whether the claim
  holds.

The last clause keeps the idealization consistent when it is applied to the
builder's theory of itself. A sentence such as "reading R was faithful" is
read for its commitments and is not assigned a truth value by the act of
reading it. Deciding it is evidence work, outside interpretation.

These are proposed fidelity criteria. How an assessor establishes that a
reading preserved the required commitments and alternatives remains open.
The earlier guarantee that budget exhaustion was the only admitted failure
is withdrawn: no guarantee for completed interpretations has yet been
established on a specified class.

## Conceptual development

The interpreter may propose new distinctions, concepts, procedures, and
representations when the current ones are inadequate for a question. These
are attempts: candidates that need assessment and may fail. Faithfully
understanding a proposal does not establish its adequacy. The semantic role
does not by itself license assessment or retention of its proposals.
Assessment is the evaluators' role, and retention belongs to the
[theory builder](./theory-builder.md#persistence), which is where a retained
extension changes the knowledge and procedures available to later
interpretation. One implementation may perform several roles; their
evidential obligations remain distinct.

## What the budget covers

The budget charges applying existing procedures, searching, interpreting, and
developing new procedures. A semantic call cannot hide arbitrary computation
as a free primitive. The resource model must charge the work of any solver
or tool a semantic call invokes. Context capacity is one relevant limit in
a language-model realization, including
[degradation before a hard cap](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md).
A run can also fail through a wrong reading, inadequate knowledge or
procedures, or an unsuccessful conceptual proposal without exhausting its
budget. Record those outcomes instead of treating every failure as a
resource shortfall.

## Completion and abstention

Assess the full admitted workload: completed interpretations, incorrect
readings, partial results, abstentions, budget exhaustion, and missing
outputs. State what evidence supports each classification. Accuracy on
completed tasks must be reported with coverage, cost, and the conditions
under which abstention is acceptable. An interpreter that avoids every
difficult case cannot establish useful capacity through fidelity on the
remaining cases alone.

Reporting an unresolved result is sometimes appropriate. It does not prove
that resolution was impossible under the declared conditions. Conversely,
understanding a question can be complete while its answer remains unknown.
The required balance of positive completion, fidelity, and justified
abstention remains an open specification question.

## What the idealization does not supply

- **Missing evidence, undiscovered proofs, or the truth of a claim it has
  understood.** Two situations that supply the same accessible evidence and
  differ in an unobserved outcome are reported as alternatives. Reliable
  information about a case requires upstream access to the case or its
  regularity, and the idealization does not waive that.
- **A decision procedure.** Understanding a specification does not decide
  termination or every consequence of execution.
- **Successful conceptual development**, or a measure of how far a task lies
  beyond the current knowledge and procedures. That measure is the open
  question recorded in the
  [discussion record](./semantic-work-and-the-ideal-interpreter.md#motivation-how-far-beyond-previously-performed-work).
- **Its own scope or assessment.** A completed output or self-report does not
  establish that the task was in scope, that the reading was faithful, or
  that abstention was justified.
- **Realizability or a universal reading guarantee.** A coherent scoped
  specification, a feasible implementation, and evidence that the
  implementation satisfies it are separate requirements. None follows from
  the name of the device.

## Realization

Any comparison to this proposed standard must include completion and
abstention on the declared workload, as well as fidelity of completed
readings. The implementation's current knowledge and procedures are declared
where they are retained artifacts and estimated by probe where they are model
weights, following the
[representational-form](../../notes/definitions/representational-form.md)
rule: read natural-language content, test symbolic artifacts, probe
parametric ones. The general specification permits both fixed and changing
model weights; probes assess capability claims rather than treating a
parameter change as evidence of a gain.
The [workshop's research target](./README.md#goal) uses only fixed weights
from model versions publicly available as of 2026-09-17. In that setting,
probes assess the models' existing capabilities and the effects of changes
to the builder's instructions, knowledge, tools, and orchestration. Training
retains those changes in natural-language and symbolic artifacts;
model-weight updates are outside this research target. None of these
restrictions guarantees faithful interpretation.

## Tests

Before adoption, the specification must address the cases in the discussion record's
[paradox section](./semantic-work-and-the-ideal-interpreter.md#paradoxes-and-overreach-to-avoid)
and
[check table](./semantic-work-and-the-ideal-interpreter.md#checks-that-would-move-this-from-a-sketch-to-a-definition).
Two cases from the review of that record remain explicit. Reflexive fidelity,
the interpreter reading claims about its own readings, requires the
identify-without-deciding distinction; the distinction does not establish
fidelity. Objective drift, a conceptual revision that changes what the
objective commits to while its text stays fixed, must be reported as a
change. Whether that change is licensed is addressed by the
[retention-policy draft's objective clause](./theory-retention-policy.md#the-objective-clause).
These are requirements for further work, not passed tests or a guarantee
assumed by the downstream experiment.
