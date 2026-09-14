# Fallible theory

> **Status:** Workshop definition, 2026-09-14. Drafted from section 4 of the
> [warrant-bounded proposal](./proposal-warrant-bounded-open-endedness.md)
> after the operator's correction that fallible theories do not extend
> through unwarranted claims, with the objective clause added after the
> ideal-interpreter review. The literature checks that proposal asks for,
> belief revision in the AGM tradition and formal learning theory, have not
> been run; closing condition 3 requires them before promotion. Not a
> library definition.

A **fallible theory** is a theory in the sense of the
[theory-refinement definition](../../notes/definitions/theory-refinement.md#what-the-loop-requires-of-a-theory),
a unit with consequences a case can contradict, parts available as repair
locations, and parts editable separately, whose retention and use do not
depend on its being established. Three clauses say what fallibility adds.

1. **Warrant attaches per claim and scope.** Passing cases confer warrant on
   the claims and scopes they exercise, not on the theory
   ([theory warrant is tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)).
   A theory's claimed scope always exceeds its tested scope, so its warrant
   is never total.
2. **Retention at partial warrant is a frontier, not theory.** A claim enters
   with starting warrant, from derivation or from a first case, and the
   scope it claims beyond its evidence is what later tests target
   ([derivation and inheritance give starting warrant; evidence earns scope](../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md)).
   Retention above a consumption threshold requires warrant sufficient for
   that consumption. Below it, a claim is held as a target for the search
   that could raise its warrant. A fallible theory does not extend through
   unwarranted claims.
3. **Revision is licensed by evidence against an unchanged objective.** A
   revision is warranted when evidence shows it corrects errors and preserves
   fit on tested cases, judged against an objective the revision does not
   change
   ([revising an improvement objective is licensed from outside it](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md)).
   Warranted revisions therefore chain.

Fallibility is then two things. Warrant is never total, by the first clause.
And the assessment of warrant is itself a fallible evaluator's output, so the
characteristic failure is misassessed warrant,
[false-positive acceptance becoming operative](../../notes/false-positive-generation-is-filtered-before-retention.md),
not unwarranted retention.

## Warrant as a relation

Full warrant is a relation, not a level: warrant sufficient for a stated
consumption path at the required confidence, in the sense of
[warranted autonomy is bounded by oracle domain](../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).
A claim may be warranted for guiding an experiment and not for codification
at the same time. Consumption is gated accordingly. Partial warrant licenses
actions whose cost of being wrong is bounded, the bounded-experiment reach of
the [self-revision boundary map](../self-revision-design-space/boundary-map.md),
and not
[costly entrenchment](../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)
such as codification or a machinery change.

## Two reachable sets

The states reachable by any revision, and the states reachable from a
declared seed under an objective by warranted revisions. A builder's library
reach equals its warranted reach at the consumption threshold; the excess is
the frontier. Whether the second set is closed under the seed objective and
the kinds of evidence it admits, the warrant-closure claim, is argued in the
[proposal](./proposal-warrant-bounded-open-endedness.md) and contested in the
[Gödel-machine comparison](./goedel-machine-comparison.md). It is recorded
here as unsettled and is not needed for this definition.

## The objective clause

A conceptual revision that changes what the terminal objective commits to is
an objective change, even when the objective's text is unchanged. It is
reported as such and is not warranted from inside. This closes the semantic
route around the third clause: reinterpreting an evaluator's purpose instead
of editing its code. The mechanical instance is the
[Darwin Gödel Machine](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
agent that maximized its hallucination score by deleting the marker its
detector keyed on.

## Zero-warrant material

Observations, questions, and log entries are not claims and carry no
warrant. They are the frontier's lowest rung, retained as questions rather
than as theory. "No unwarranted claims" does not mean "no unresolved
questions". The
[workshop layer](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md)
is where Commonplace holds the frontier, and a workshop that accretes
untested candidates is the frontier's known failure.

## What fallibility is not

- Not retention of unwarranted claims. That is the failure the second clause
  excludes.
- Not a property of form. A program or a formal model retained under these
  clauses is a fallible theory. A natural-language note is not fallible
  merely by being prose.
- Not a weakness of the theory. A theory kept consistent by being too weak to
  misfit has no tested scope to earn warrant on.

## Boundary cases

- **A Gödel machine's axioms** are not a fallible theory. They are retained
  by proof, revised only by theorems derivable from them, and a contradiction
  with an observation is an inconsistency rather than a located fault. There
  is no frontier.
- **A Commonplace note** is a fallible theory. It is retained with per-claim
  status, revised against cases and criteria, and consumed as evidence rather
  than with binding force. A validator codified from it is machinery whose
  continued use is licensed by the note's warrant, since
  [machinery persists by warrant, not position](../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
- **A Darwin Gödel Machine child's benchmark score** is partial warrant on
  tested scope. Archive admission on that score alone is retention at partial
  warrant, with archive membership and parent selection as the cost-bounded
  action it licenses. The marker deletion is the objective clause violated.
