# Resource-bounded ideal interpreter

> **Status:** Workshop definition, 2026-09-14. The operator sharpened the
> working definition in
> [Semantic work and the ideal interpreter](./semantic-work-and-the-ideal-interpreter.md#working-definition-resource-bounded-ideal-interpreter),
> which keeps the discussion record and the paradox tests. Two clauses were
> added at review: faithful reading of an ambiguous input preserves the
> alternatives, and unfinished work is reported. Not a library definition.

A **resource-bounded ideal interpreter** performs faithful interpretation and
attempts conceptual development using its current knowledge and procedures,
subject to a computational budget. Work requiring more computation than the
budget permits may remain incomplete or unresolved, and is reported as such.

Budget exhaustion is the only failure the idealization admits. A reading that
is wrong within budget is not a behavior of the ideal interpreter; it is an
approximation error of the implementation compared to it. That is what the
idealization is for. It separates errors in interpreting a theory from errors
in the theory, and it gives an evaluation a standard against which to score a
real interpreter on the tasks it completed within budget.

**Semantic work**, the activity the interpreter performs, is defined in the
discussion record: establishing, examining, or revising how expressions and
concepts represent a subject and bear on a question. It extends the KB's use
of the term in
[semantic work can be relocated but not eliminated](../../notes/semantic-work-can-be-relocated-but-not-eliminated.md)
by adding conceptual revision.

## Faithful interpretation

A faithful interpretation of a representation, given its context:

- preserves the commitments the context fixes;
- preserves the alternatives where the context leaves consequential readings
  open, instead of selecting one silently. A faithful reading of an ambiguous
  input is complete when it reports the alternatives; it is not unresolved;
- reports a revised commitment as a change, never as what the text always
  meant;
- identifies what a claim commits to without deciding whether the claim
  holds.

The last clause keeps the idealization consistent when it is applied to the
builder's theory of itself. A sentence such as "reading R was faithful" is
read for its commitments and is not assigned a truth value by the act of
reading it. Deciding it is evidence work, outside interpretation.

## Conceptual development

The interpreter may propose new distinctions, concepts, procedures, and
representations when the current ones are inadequate for a question. These
are attempts: candidates that need assessment and may fail. Faithfully
understanding a proposal does not establish its adequacy. The interpreter
does not assess or retain its own proposals. Assessment is the evaluators'
role, and retention belongs to the
[theory builder](./theory-builder.md#persistence), which is where a retained
extension changes the knowledge and procedures available to later
interpretation.

## What the budget covers

The budget charges applying existing procedures, searching, interpreting, and
developing new procedures. A semantic call cannot hide arbitrary computation
as a free primitive. An interpreter that decided every satisfiability
instance in one uncharged call would be assuming an efficient oracle, not
describing one. For a language-model realization the binding resource is
usually context rather than arithmetic, since
[soft degradation often binds before the hard cap](../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md),
so the budget includes context capacity.

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
- **Its own scope.** Whether a task was within the assessed scope is decided
  by the assessment, not by the interpreter. The fidelity claim is
  conditional on that.
- **Realizability.** This is an analytic device stating what a builder could
  do with faithful interpretation. It does not claim that any program
  achieves it.

## Realization

An implementation is compared to the ideal on the tasks it completed within
budget. Its current knowledge and procedures are declared where they are
retained artifacts and estimated by probe where they are model weights,
following the
[representational-form](../../notes/definitions/representational-form.md)
rule: read natural-language content, test symbolic artifacts, probe
parametric ones. Fixed weights are one possible form of the knowledge, not a
required one, and an extension that lands in weights has no artifact diff and
needs a probe-based record.
The [workshop's research target](./README.md#goal) uses only fixed weights
from model versions publicly available as of 2026-09-17. In that setting,
probes assess the models' existing capabilities and the effects of changes
to the builder's instructions, knowledge, tools, and orchestration. Training
retains those changes in natural-language and symbolic artifacts;
model-weight updates are outside the assessment.

## Tests

The definition must pass the cases in the discussion record's
[paradox section](./semantic-work-and-the-ideal-interpreter.md#paradoxes-and-overreach-to-avoid)
and
[check table](./semantic-work-and-the-ideal-interpreter.md#checks-that-would-move-this-from-a-sketch-to-a-definition).
Two cases from the review of that record are added. Reflexive fidelity, the
interpreter reading claims about its own readings, is covered by the
identify-without-deciding clause. Objective drift, a conceptual revision that
changes what the objective commits to while its text stays fixed, is not an
interpreter matter; it is addressed by the
[retention-policy draft's objective clause](./theory-retention-policy.md#the-objective-clause).
