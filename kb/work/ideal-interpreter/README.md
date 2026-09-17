# Workshop: the LLM as an interpreter of semantics

## Goal

Work out whether a language model can be modelled as an interpreter of
semantics the way an abstract machine models a computer: a device that
takes representations whose semantics nobody has formally assigned and
behaves as if they had one. The [sketch](./resource-bounded-ideal-interpreter.md)
holds the current material: the semantic-work definition, the option
space, the forces, and the stress tests. What it lacks is the function. A
functional definition would state the domain (a representation, its
context, a question), the codomain (a reading: commitments, open
alternatives, relevant consequences with their premises, proposals marked
as proposals; for an instruction, a selection among operations), the
correctness relation (the reading equals the representation's objective
content under the context, in Popper's sense), and the resource bound that
makes the function partial. The correctness clause is the load-bearing
stipulation and the open problem.

Posed by the operator on 2026-09-14 in the theory-builder workshop and
separated on 2026-09-17 with the operator's direction that it is too
experimental for anything existing to depend on it. No library
definition, instruction, or reference artifact rests on this device, and
none may until this workshop closes with an adopted definition. The
[theory builder](../../notes/definitions/theory-builder.md) records a
failure without attributing it; the
[fence note](../../notes/a-claim-without-external-assessment-carries-three-obligations.md)
says attribution needs its own evidence and names no standard.

## What closes the workshop

1. A functional definition with the four parts above, or a recorded
   decision that none is available and the sketch is dropped.
2. The stress tests in the sketch worked through against that definition,
   with expected results recorded so a candidate can fail them.
3. Either promotion as a design proposal, once the definition is finished
   and something would consume it, or deletion with the reason in the
   closing commit.

## Evaluation boundary

The sketch as moved here and the notes it cites. The
[theory-refinement-interface workshop](../theory-refinement-interface/README.md)
owns the operations a refinement machinery implements; this workshop does
not define the interpreter through those operations, since the question
here is the device, not the machinery that uses it.

Write scope while open: this directory only.
