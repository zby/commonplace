---
description: "Theory refinement's operations — derive, compare, locate, revise, evaluate — are what the three theory properties require read from the theory's side; the interface decides which classical results transfer and grades addressability per operation"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, self-improving-systems, learning-theory]
---

# Theory refinement is an interface of five operations, not a representation

> **Status:** Draft note produced by cp-skill-write on 2026-09-09 before the operator asked that the interface framing stay in the workshop. Held here as a candidate alongside [theory-refinement-interface.md](./theory-refinement-interface.md); not a library artifact.

[Theory refinement](../../notes/definitions/theory-refinement.md) — revising an existing
fallible explicit theory against empirical cases — is specified by what one
refinement episode must perform, not by the language the theory is written in
or by the procedures that perform it. Five operations must be performed:
**derive**, **compare**, **locate**, **revise**, **evaluate**. The theory and
the machinery implement them jointly; neither side implements any of them
alone. Read this as an interface and three things follow: the three properties
the KB requires of a theory are the same contract seen from the theory's side,
a classical result transfers to new machinery exactly when its derivation uses
only these five operations, and addressability becomes a five-slot profile
rather than a degree word.

## The five operations

| Operation | What one episode must produce | What the theory must expose | What the machinery must do |
|---|---|---|---|
| derive | what the theory implies for a case | commitments that bear on the case | apply them to the case |
| compare | whether that implication conflicts with the case | an implication definite enough to conflict | decide the conflict |
| locate | which parts could be responsible for the conflict | parts a conflict can implicate | search over them |
| revise | a candidate theory differing in those parts | parts editable without replacing the whole | propose the edits |
| evaluate | whether the candidate is better on the cases at hand | consequences to re-derive | re-derive and score |

The split is a decomposition of one episode, not a control flow. Order,
iteration, batching, and how many candidates are held at once are machinery
choices that leave the interface unchanged.

## The three theory properties are the same contract from the theory's side

The definition names three properties a theory must have for the loop to run:
consequences a case can contradict, parts available as candidate repair
locations, and parts editable separately. Each is the theory-side half of an
operation pair. Consequences a case can contradict is what derive and compare
need. Parts available as candidate repair locations is what locate needs.
Parts editable separately is what revise needs, and re-deriving consequences
after the edit is what evaluate needs. Nothing in the property list is left
over, and no operation lacks a property.

The two sides fail independently, which is why they are worth separating. A
theory whose parts cannot be told apart defeats locate however good the
machinery is: there is nothing to search over. Machinery with no consequence
procedure defeats derive however well-structured the theory is: nothing
applies it to the case. This is also why the task/algorithm separation the
classical papers make holds up. The task names the operations; the algorithm
names one implementation of them together with one representation that meets
the theory-side contract.

## A classical result transfers by restatement only when its derivation stays inside the interface

Restating a result in new machinery's terms is cheap, so the question is which
restatements are warranted. The criterion is the interface: a result transfers
by restatement exactly when its derivation uses only the five operations and
their inputs and outputs. A result whose derivation reaches past them names the
implementation, and reaches the new machinery as a hypothesis to be tested
there.

Task-level results pass the test. The classical task is to take an incorrect
initial theory and cases and find a "theory that is correct on the given
instances" (verbatim,
[Richards and Mooney](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md)),
minimally revised. That statement uses derive, compare, revise, and evaluate,
and nothing else; any machinery that implements the interface can state the
same task over its own theories. So can the two directions of failure: compare
can report an implication that should not hold and one that should hold but
does not, so revision has a narrowing direction and a widening one. So can the
non-uniqueness of blame: nothing in the interface requires locate to return a
single part, so a conflict identifies candidates rather than a fault, whatever
performs the locating. So can the relativity of acceptance: evaluate is defined
over the cases at hand, so a theory is accepted against that set and not
against the world.

Results measured of one machinery-and-representation pair do not pass. FORTE
"can be caught in local maxima" (verbatim,
[Richards and Mooney](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md)),
which is a fact about hill-climbing over its operators rather than about
evaluate; different search over the same interface has different stopping
behaviour. The same holds for how far small syntactic edits approximate
minimal revision, for the example counts below which repairing an approximate
theory beats inducing one from scratch, and for which operators carry the
benefit. Each of these is a measurement of Horn clauses plus proof plus four
operators plus a domain distribution. Carried to a general interpreter over
prose theories, they are conjectures with their own tests to pass, which is
the standing of the KB's [sample-efficiency
conjecture](../../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md).

The criterion has a refuter: a classical result that is task-level yet cannot
be derived from the five operations and their inputs would show the interface
is under-specified, and would name the missing operation.

## The interface grades addressability per operation

The definition says addressability comes in degrees. The interface says which
degrees, because each operation independently takes one of three values.
**Mechanical**: a formal consumer computes the operation, so its output is a
fact. **Interpreted**: a model judges it, so its output is a judgment that can
be wrong about the theory rather than about the world. **Unavailable**: nothing
performs it, so the loop does not close. Addressability is then a five-slot
profile, and a system is placed by reading it off.

At one end sits fully codified machinery: a representation language that
expresses any computable theory, with consequences computed by proof or
execution. Its profile is derive mechanical and the rest unavailable *against
evidence*. A case that contradicts a commitment there is an inconsistency
rather than a repair signal, so compare yields no locatable failure, and the
commitments change only by proof from themselves rather than by revision
against the case — the shape [Gödel machines
show](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) for
a theory of the machine itself. Such machinery keeps derivation and loses
refinement, which is why it is a limit rather than a destination. A workshop
draft names this limit the universal theory manipulator; the argument here
needs the limit, not the name.

At the other end sits a general interpreter, a model applied to theories in
prose. Its profile is all five interpreted. That is what buys entry for a
theory whose language, variables, and acceptance test do not exist yet, and it
costs exactly what the five slots say: every output of every operation is a
judgment.

The profile is per part, not per system, wherever a theory is mixed in
[representational form](../../notes/definitions/representational-form.md).
[Codification](../../notes/definitions/codification.md) moves a part's slots from
interpreted to mechanical one part at a time, which is why a real system's
profile is a distribution over its parts rather than a single row. The profile
also says what a repair must fix, since an unavailable operation and an
unreliable interpreted one are different problems: the first needs machinery
built, the second needs a check that a contradiction is real.

## A builder that generates its own cases needs apply in addition

All five operations take the case as given. The classical systems were handed
labelled cases, so nothing in the interface produces one. A persistent builder
whose theories guide the actions that generate its cases performs a sixth
operation, **apply**: using the theory to shape a decision. The definition
excludes applying a theory from refinement deliberately — it is a neighbour,
not a case of it — and the interface shows why the exclusion is not a
technicality. Apply is the join that makes a consequence return to the theory
that guided it, so a system can implement all five operations well and still
run on cases whose production its theories never touched.

Apply is also where the cheapest evidence attaches, since [citing the retained
theory at the decision
point](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
is a record that the theory entered the decision, and none of the five
operations leaves that record. A theory nobody applies and nobody refines is
[not on any consumption
path](../../notes/an-action-model-matters-only-through-its-consumption-path.md).

## Scope

- The interface fixes what must be performed, not how well. It says nothing
  about whether any operation is reliable, whether the loop converges, or
  whether the resulting theory is true. Membership is by operation, as the
  definition already holds.
- Five is a choice of grain. Derive and compare could be one operation with a
  two-valued output; locate and revise could be one search step. The argument
  needs only that the operations named are separately implementable and
  separately defeatable, so a coarser or finer split with that property would
  carry it equally.
- The transfer criterion is a criterion, not a completed audit. No systematic
  pass over the classical results has been run against it here.
- Apply is placed outside refinement by the definition's own exclusion. Whether
  the mechanical/interpreted/unavailable scale applies to it as it does to the
  five is not settled here.

## Open Questions

- Does evaluate split into two operations rather than one — checking fit
  against the cases, and ordering revisions that all fit? The definition puts
  [reach-assessment](../../notes/definitions/reach-assessment.md) outside refinement
  while letting reach order the survivors, which reads like a second slot with
  its own three values.
- Does the profile predict anything about where a system breaks first, or does
  it only describe? An interpreted slot that fails silently and an unavailable
  one that fails loudly would predict different failure signatures.

---

Relevant Notes:

- [Theory refinement](../../notes/definitions/theory-refinement.md) — defined-in: the operation whose three theory properties this note reads as one side of an interface
- [Reflective theory refinement has separate structural, epistemic, and implementation lineages](../../notes/reflective-theory-refinement-has-three-separate-lineages.md) — extends: the slot-for-slot comparison this interface makes explicit as a per-operation contract
- [An open-domain theory builder becomes a software house when new domains require production-machinery changes](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md) — extends: what follows when the machinery implementing the interface must be built per family
- [Theory refinement may improve sample efficiency under structured shifts](../../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md) — extends: the classical empirical result carried across as a conjecture with its own test
- [Gödel machines are a proof-governed case of reflective self-modification](../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the derive-only profile of fully codified machinery
- [Citing retained theory at the decision point is a mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) — mechanism: the evidence that attaches to apply rather than to any of the five
- [Codification](../../notes/definitions/codification.md) — grounds: the crossing that moves a part's slots from interpreted to mechanical
- [Representational form](../../notes/definitions/representational-form.md) — grounds: why the profile is per part in a mixed-form theory
- [Reach-assessment](../../notes/definitions/reach-assessment.md) — contrasts: the ordering among revisions that fit, which the interface does not supply
- [An action model matters only through its consumption path](../../notes/an-action-model-matters-only-through-its-consumption-path.md) — grounds: why a theory outside both apply and refinement is excluded
- [Automated refinement of first-order Horn-clause domain theories](../../sources/automated-refinement-first-order-horn-clause-domain-theories.ingest.md) — abstracted-from: the task statement that transfers by restatement and the search property that does not
