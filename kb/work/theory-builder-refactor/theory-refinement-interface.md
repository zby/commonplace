# Theory refinement as an interface

> **Status:** Working document, 2026-09-09. Operator direction: write this down
> and work it out here before anything leaves the workshop. The framing came
> from the operator's conversation with Codex; the mapping onto the KB's
> definitions and the placements below are this workshop's.

## The claim

Theory refinement specifies an interface. A theory together with its
machinery implements it; the theory file alone does not. The interface has
five operations:

| Operation | Question it answers |
|---|---|
| **Derive** | What does the theory imply for this case? |
| **Compare** | Where does that consequence disagree with the evidence? |
| **Locate** | Which assumptions, rules, or scope conditions are candidate sources of the disagreement? |
| **Revise** | Change the selected parts. |
| **Evaluate** | Does the revision correct the errors while preserving useful behaviour on the tested cases? |

Horn clauses with proof, named operators, and training-set accuracy are one
implementation. Equations, programs, and structured prose with an interpreter
are others. What the KB gains from saying it this way: to use the classical
theory-refinement results, we do not need Horn clauses. We need to define our
theory machinery so that it implements the interface for our representation,
and then say which results carry over and under what conditions.

## The same contract from the theory's side

The [theory refinement](../../notes/definitions/theory-refinement.md)
definition does not list operations. It lists three properties a theory must
have: consequences a case can contradict, parts available as candidate repair
locations, and parts editable separately. These are the interface seen from
the theory's side. Derive and compare need the first; locate needs the second;
revise and evaluate need the third. Neither list replaces the other. The
properties say what the theory must be like; the operations say what the
machinery must do with it. A note that eventually leaves this workshop should
state that they are one contract.

## Who implements what

The role table in the [proposal](./theory-builder-proposal.md#4-the-machinery-departure-and-the-table-that-replaces-the-ladder)
groups the interface into three rows. Ungrouped, per implementation:

| Operation | EITHER / FORTE | Universal theory manipulator | General interpreter | Commonplace today |
|---|---|---|---|---|
| Derive | proof over Horn clauses | execution or proof; mechanical | model reads the theory and the case; interpreted | model reads notes and the artifact under review; validators derive for codified parts |
| Compare | proof succeeds or fails against a label; mechanical | mechanical only when the observation is itself a theorem; otherwise not performed | model judges disagreement; interpreted | gates and critique: mechanical for validator-backed criteria, interpreted for LLM assays |
| Locate | proof trace names candidate clauses and antecedents | not performed against evidence | model nominates parts; interpreted; perturbation and withholding as the check | premise defeat in the full improvement pass; interpreted |
| Revise | retract, generalize, specialize, add | rewrite of expressions, but only by proof from the current axioms | model edits prose parts; interpreted | agent edits; codification of settled parts into schemas and validators |
| Evaluate | consistency with supplied cases; hill-climb on training accuracy | not performed against evidence | model re-reads revised theory against cases; interpreted | gates re-run; reach-assessment; operator verification |

Three placements follow.

- **The [universal theory manipulator](./universal-theory-manipulator.md) is
  derive-only.** It answers what follows from the theory. Compare is available
  only when observations enter as theorems, and even then a disagreement with
  an axiom is an inconsistency, not a located fault. Locate, revise against
  evidence, and evaluate against evidence are absent. This is why the
  manipulator draft says the limit manipulates theories without refining them.
- **The general interpreter implements all five by interpretation.** Every
  operation is available for any representation the model can read, and none
  carries the classical guarantee. This is the first step of the proposal's
  machinery departure.
- **Codifying back moves one operation for one part from interpreted to
  mechanical.** A validator makes compare mechanical for the claims it
  checks. A schema makes locate mechanical for the fields it names. This is
  what "constructing family-specific machinery" means operationally:
  implementing some operations of the interface mechanically for a family.

## A scale for addressability

The definition says addressability comes in degrees and gives no measure.
The interface supplies one. For a theory in a given machinery, record for each
operation whether it is mechanical, interpreted, or unavailable. FORTE's
theories are mechanical on all five. A prose note read by a model is
interpreted on all five. A Commonplace note with a validator behind one of
its claims is mechanical on compare for that claim and interpreted elsewhere.
The git-history test in the proposal can record each codification as a move
on this scale, which makes "the builder constructed addressability for a new
family" a checkable statement.

## What the builder needs beyond the interface

The definition excludes applying a theory: application uses the theory
without revising it. The builder must apply, because its theories guide the
actions that produce its cases. So the builder's contract is the refinement
interface plus **apply**, and loop closure is the requirement that apply and
compare share a case: the consequence compared is the consequence of the
action the theory guided. The evidence standards for that shared case are the
existing ones, the evidence ladder and the co-indexed witnesses.

## Which classical results carry over

Implementing the interface lets the classical results be stated in our terms.
It does not make them true of our implementation. Two kinds must be kept
apart.

**Task-level results transfer.** These follow from the interface, not from
Horn clauses, so any implementation inherits them.

- A failed comparison does not identify a unique fault. Locate yields
  candidates. FORTE's traces and EITHER's abduction narrow the candidates; an
  interpreter's nomination narrows them less reliably. This is the
  underdetermination problem in the definition.
- Revision is not guaranteed minimal, and evaluate can stop at a local
  maximum. FORTE states both for its own hill-climbing
  ([ingest](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md)).
  An interpreted implementation has no reason to do better and several to do
  worse.
- Acceptance is fit with the tested cases. This is the floor, not the
  ordering. The definition adds reach as the ordering among revisions that
  fit; the classical systems did not have it and did not need it, because
  their cases were supplied and their theories were external.
- The update space is fixed by the operators and representation. FORTE cannot
  invent predicates; EITHER can only express acyclic propositional mappings.
  An interpreter's update space is open, which removes this limit and removes
  the guarantee that came with it: a revision stays inside a space the
  evaluator can check.

**Empirical results transfer as hypotheses only.** They were measured on the
Horn-clause implementations in two or three small domains.

- Revision beats induction from scratch when the initial theory is
  approximately right. FORTE's family experiments support this and also bound
  it: with 100 training examples and eight introduced errors, induction did
  better. EITHER outperformed ID3 on two classification tasks and sometimes
  reached a given accuracy with fewer examples, without isolating what did the
  work ([ingest](../../sources/theory-refinement-analytical-empirical-methods.ingest.md)).
- Relational path finding was needed to escape plateaus that defeat
  single-step search. Whether an interpreter's proposals have an analogous
  plateau problem is unknown.

For our implementation each of these is a test to run, and the FORTE tasks
are the natural baseline: a known corrupted theory, stated in prose,
repaired through the interpreter, scored on the same cases. That is the
discriminating test for the form departure the proposal names and the KB
does not yet have.

## Open questions to work out here

1. **Is compare a separate operation?** The definition folds it into the
   first property. FORTE performs it inside derive (a proof succeeds or
   fails). For an interpreter it is a separate judgment with its own error.
   Keeping it separate seems right for the interpreted case; the definition
   would need a sentence.
2. **What does locate require of an interpreted theory?** FORTE has a trace.
   The interpreted analogue is nomination plus a perturbation or withholding
   test. Whether that is an implementation of locate or a weaker substitute
   decides whether the task-level results about locate apply.
3. **What does evaluate need?** Held-out cases, at minimum. The KB's warrant
   notion (system use is not independent warrant; oracle domain) enters here
   and has no classical counterpart. Where in the interface does reach sit:
   inside evaluate, or as a sixth operation that orders survivors?
4. **How is "implements the interface for a family" certified?** The
   test-shaped answer is fault injection: corrupt a known-good theory of the
   family, run the loop, check the repair. That is the FORTE baseline again,
   and it would double as the acceptance test for any constructed machinery.
5. **Apply and the shared case.** Whether apply belongs in the interface or
   beside it, and how loop closure is stated as a constraint on which case
   compare receives.
6. **Where the interface is written.** As a section of the theory-refinement
   definition, stating the two views of one contract, or as its own note with
   the definition linking it. The definition is already long.
7. **Which classical results we actually want.** The list above is what
   transfers. Which of it the program needs, and for which claim, is not yet
   decided. Listing results we will not use is the storage-without-consumption
   pattern the KB warns against.
