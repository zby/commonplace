# Unify the review operations

Posed by the operator on 2026-11-14. The operator first redirected the improvement-procedure work from full procedures to its atomic procedures, and then narrowed the first step to this: unify the reviews before the edit operations and the stops. This is a design commission. Each change to shipped criteria, types or code needs the operator's instruction, as the merges and ADR 131 did.

## Goal

Make the review operations one pool under one contract, so that each can be run, stored, tested and calibrated alone, and so that a later procedure can compose any of them without special cases.

The contract is the atom contract of the [one improvement procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md): a typed instruction file, inputs that are files, a typed result filed by the note and the operation, and a way to run the operation by itself on one note or across a collection. An operation that only works inside a composition does not meet it.

The [plan](./plan.md) says how the work proceeds and where it stops for the operator.

## The pool today

The count and the overlaps come from the [overlap map](../decision-lifecycle-evidence/review-operation-overlaps.md), which stays where it is and is this workshop's starting evidence.

| Family | Count | Form today | Runs alone | Typed stored result |
|---|---|---|---|---|
| Catalog gates in seven bundles | 40 | [review-gate](../../types/review-gate.md) criteria; pass, warn or fail | Yes, `commonplace-review run gates` | Yes |
| Type and collection conformance | 1 each per note | A wrapper applies the type spec or the collection contract | Yes, with `--all-gates` | Yes |
| [Compression bundle](../../instructions/compression-bundle/README.md) | 4 checks and a synthesis | Report-only, kept outside the catalog on purpose so that `--all-gates` never runs it | Through its own instruction | No |
| Report methods: critique, composition friction, premise decomposition, connect | 4 | Open-ended reports under `kb/reports/state/` | Each through its own instruction or skill | A report file per note; only connect has a type |
| Higher-order check | 1 | Workshop wordings, run as a gate with their own criterion ids | Yes, as a draft | As an ordinary gate result |

So the pool has two forms. The review-gate type says so itself: a gate is a closed-ended, verdict-kind assay, and "report-kind assays are instructions, not `review-gate` artifacts". The first two rows meet the contract. The next two do not.

## Questions to resolve

1. **One form or two?** Either the report-kind operations are rewritten as verdict-kind gates, or the pool gets a second typed form for reports with its own stored result. A gate result supports freshness, batch runs and counting. A report carries reasoning that a three-way verdict loses. Decide per family, not once for all four.
2. **What the compression bundle becomes.** It was kept out of the catalog deliberately. Find the reason that still holds before moving it. Its `detail-overhang` and the catalog's `prose/proportion-mismatch` state one defect from two sides, and its synthesis step composes four findings, so it may be a small composition and not an atom.
3. **What the three adversarial reports become.** Critique, composition friction and premise decomposition each try to break the note's central commitment by a different route. The overlap map left them for evidence to sort out. Say what evidence would sort them, and whether they stay three.
4. **Where connect belongs.** It discovers candidate links across the corpus. It may be a review operation of a note, or a different kind of operation that the pool should not absorb.
5. **The remaining duplications.** The overlap map lists one pair still open (`proportion-mismatch` and `detail-overhang`) and a table of one question asked at several scales. Decide whether each scale states which scale is its own.
6. **What a result must carry.** The higher-order check needs a kind and a force beyond pass, warn and fail. Its [evaluation workshop](../higher-order-check-evaluation/README.md) is asked to report where the gate shape strains. Take that report as input to the result form.
7. **What "tested alone" produces.** For each form, state the test a review operation must have before a procedure relies on it: known cases, proposal rate, repeated trials on unchanged text.

Do not turn this list into a schema before examining what each operation's actual consumers read.

## Premises set by the operator

- **Atoms before procedures.** The full pass, the fix procedure and the revise workflow are not redesigned here. They keep running as they are, and a change to an operation must not break the one that uses it.
- **Reviews before edits and stops.** The edit-operation type and the stops stay drafts in the [decision lifecycle workshop](../decision-lifecycle-evidence/README.md) until this workshop has a result.
- **Stability is assumed reachable.** Review verdicts can be made stable, and designs here may rest on that. Present stability is measured by the [gate verdict stability pilot](../stochastic-operation-testing/pilot-gate-verdict-stability.md); a poor result names gates to stabilize and does not reopen this premise.

## Shipped constraints

- [ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md): review runs as workflows over result files. Review keeps its code, because it is a batching problem.
- [ADR 131](../../reference/adr/131-conformance-reviews-leave-titles-and-descriptions-to-their-gates.md): the conformance wrappers leave title and description properties to the frontmatter gates.
- [ADR 082](../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md): `concept-attribution` and `misleading-link-text` have different units and are not to be merged.
- The result store keeps one result per note and criterion. Two wordings of one operation need two criterion ids, or the second overwrites the first.
- The [review system](../../reference/README-REVIEW-SYSTEM.md) asks that each operation be evaluated alone before its composition is trusted.

## Evaluation boundary

The workshop covers operations that read a note and report on it. It does not cover edit operations, stops, variants, authority grades or the run types. It does not calibrate any single operation: the higher-order check has its own workshop, and verdict stability belongs to the stochastic-testing workshop.

A proposed change is judged by whether the operation then meets the contract and whether its current user still works. No claim about review quality follows from a change of form.

## Coordination

- [Decision lifecycle and evidence](../decision-lifecycle-evidence/README.md) holds the overlap map, the type drafts and the shelved first variant.
- [Higher-order check evaluation](../higher-order-check-evaluation/README.md) owns that check's wording and calibration. This workshop owns the form its result takes once it is an atom.
- [From live operation to controlled testing](../stochastic-operation-testing/README.md) owns the method for repeated trials. Question 7 takes its method from there.
- [Review on Workjig](../review-on-workjig/README.md) owns the workflow engine work. A new result form here is a requirement on it, not a change to it.
- [Calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) is the standing proposal on known-case testing of gates.

## What closes the workshop

- Every review operation in the table either meets the contract, or has a recorded decision that it stays outside the pool with the reason.
- The one-form-or-two question is decided, and any new type is registered or explicitly declined.
- The open duplications are resolved or kept with a stated reason.
- The test each form requires before a procedure relies on it is stated.
- Decisions are extracted to an ADR, the types and the review-system reference, and the procedure proposal's table of atoms is updated. The workshop is then removed and its active-list entry deleted.
