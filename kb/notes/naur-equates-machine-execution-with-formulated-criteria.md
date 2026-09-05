---
description: "Naur's human-only conclusion needs a further premise connecting unformulated judgment to computational inability; this reading preserves his functional tests without claiming that learned criteria are inexpressible"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, context-engineering]
---

# Naur's human-only conclusion needs more than the absence of explicit criteria

Peter Naur's [Programming as Theory Building](../sources/programming-as-theory-building.ingest.md)
connects two claims: program theory cannot be expressed as rules or criteria,
and it is bound to human beings. The second does not follow from the first
alone. It also needs a reason why computation cannot perform the relevant
judgments without their criteria having been explicitly supplied.

This note reconstructs one bridge between those claims. It is an
interpretation of the essay, not a premise Naur states as a separate theorem.
Removing that bridge reopens the computational question; it does not establish
that a current model or automated house holds a program theory.

## What Naur asks a theory-holder to do

Drawing on Ryle, Naur describes a capacity to relate program structure to the
world, justify the program's parts, and incorporate new demands by recognizing
relevant similarities. Following an explicit rule does not exhaust that
capacity: applying a rule itself can require judgment. Naur uses this regress
to argue against identifying intelligent performance with adherence to a
formulated method.

That gives a demanding functional target. A modifier must do more than recall
facts or produce a patch that passes today's tests. It must understand how a
change relates to the program's purpose and organization, including implications
not already stated as instructions.

Naur also locates theory in programmers' mental possession and stresses their
knowledge of the world. These are part of his account, not consequences that
his maintenance cases independently establish for every possible computational
system.

## The reconstructed bridge

The essay contrasts formal symbol manipulation with similarity judgments whose
criteria cannot be formulated. One reading reconstructs the inference as:

1. Program-theory judgments cannot be reduced to explicitly formulated criteria.
2. A computer can make a judgment only by executing such criteria.
3. Therefore a computer cannot perform the program-theory function.

The second premise is doing essential work. It identifies formal execution
with the prior formulation of a judgment's criteria. Even granting the first
premise does not establish the conclusion without it. Nor does excluding
computers alone establish that humans are the only conceivable bearers.

The claim that this bridge captures Naur's reasoning must remain distinguishable
from the passages supporting it. Another reading may treat his human-only
position as an additional commitment rather than a conclusion from the
rule-following argument. Either way, a human-only premise needs its own support.

## Formal execution does not require a hand-written judgment rubric

A learned model is executed by defined computational operations. That fact does
not mean its designers supplied a project-specific rubric for every judgment
it can make. A fixed model can be asked to interpret a new explanation and
relate it to a case without receiving a complete decision rule for that case.
Whether it does so adequately is the empirical issue.

Two claims must stay separate: the criteria were not explicitly supplied, and
the criteria cannot be formulated. The first does not prove the second. A
model's numerical parameters and execution rules specify a computation, but
that specification need not be a useful human-readable account of its judgment.
Difficulty explaining the judgment is not a proof that such an account is
impossible.

The computational proposal therefore need not defend inexpressibility or claim
that machines were incapable of learned judgment when Naur wrote. Its narrower
point is that absence of a supplied rubric does not by itself rule out
computational performance. A working computational theory-holder would challenge
the human-only thesis while leaving the expressibility question separate.

## What the transfer evidence establishes

Naur's compiler case describes a motivated successor group with program text,
annotations, extensive design discussion, and personal advice. It still proposed
changes the original group regarded as damaging patches, where the original
group could propose changes within the existing structure.

The negative result concerns that [documentation-and-consumption
system](./naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
It does not show that all possible records or interpreters must fail. It also
does not show that the supplied records were sufficient and merely needed
better retrieval. Missing premises, missing application skill, and failure to
activate relevant understanding are different possible explanations.

Retained theory and holding a theory must therefore remain separate. Retained
text is one addressable carrier. Holding a theory is a capacity of the system
that consumes the available state. A document that is never used supplies no
evidence of that capacity; successful reconstruction from other records need
not require that document.

## Tests for a computational bearer

Three tests follow from this functional reading:

- **Project-specific understanding.** General programming competence is not
  the theory of this program. The system must relate the actual program to
  its purposes, justify consequential choices, and handle novel modifications.
  The understanding may be supplied in the seed or acquired during operation;
  its use and its acquisition are separate claims.
- **Access to necessary premises.** A decision premise not recoverable from
  the implementation and general knowledge must reach the modifier through
  some other permitted path. [Attempted
  recovery](./design-rationale-must-preserve-unregenerable-decision-premises.md)
  can expose that information gap without making one document format necessary.
- **Reliable continuation.** One coherent extension may be lucky or familiar.
  The system must sustain coherent search, diagnosis, recovery, and revision
  across later demands, including evidence against earlier assumptions.

[Holding program theory under delayed
feedback](./program-theory-sustains-search-under-delayed-feedback.md) develops
the last test. Interventions on retained commitments or their consumption paths
can test their causal contribution. Altering a written carrier alone does not
isolate the whole capacity when other records can reconstruct it.

## Scope

This is a criticism of an inference, not a proof of computational theory
possession. The functional tests are an operational reading of Naur for a
research program, not a claim that he would accept every system passing them.
A successful computational witness would bear on human exclusivity; it would
not settle every philosophical claim about knowledge or rule-following.

---

Relevant Notes:

- [Programming as Theory Building](../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies Naur's rule-following discussion, human-binding statements, capabilities, and transfer cases; the reconstructed bridge is this note's interpretation
- [Naur's compiler case tests one historically bounded documentation-and-consumption system](./naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md) — extends: separates the failed transfer from a universal impossibility claim
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: identifies when retained project-specific information is necessary
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — extends: develops the longitudinal capacity test
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: separates application, retention, and correction on a computational path
