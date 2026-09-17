# Workshop: the first downstream run

## Goal

Run the first externally assessed episode of Commonplace as a KB-producing
[theory builder](../../notes/definitions/theory-builder.md): a consuming
project receives a versioned KB release, its agents do real tasks, its judges
accept or reject the outputs, and the builder revises the product and, when
a failure exposes a machinery limit, its own methodology, with later matched
tasks assessed against the frozen seed. The
[evidence protocol](./commonplace-evidence-protocol.md) is the design; the
[three episodes](./main-path-episodes.md) are constructed cases that show
the vocabulary can describe such a run. Neither is a result.

Posed by the operator on 2026-09-17 when the theory-builder workshop's
conclusions were adopted and the protocol and episodes were moved here from
[theory-builder-refactor](../theory-builder-refactor/README.md), whose
[main-path plan](../theory-builder-refactor/main-path-plan.md) records the
decisions this run tests. The hypotheses under test are the sufficiency,
comparative, and reflection hypotheses stated in that workshop's Goal.

## What closes the workshop

1. The protocol's freeze table is filled: consuming project and area, seed,
   models, task supply, outcome contract, budget, horizon, reliability
   target, feedback, and acquisition mode. The first consuming project is
   the operator's choice and is the only item nothing else here depends on.
2. At least one product-revision episode and one reflective episode have
   been run and recorded with the release, consumption, outcome, and
   feedback records the protocol requires, including the matched-ablation
   baseline and the control runs.
3. The recorded episodes are assessed against the
   [externally tested](../../notes/definitions/externally-tested-theory-builder.md)
   and [reflective](../../notes/definitions/reflective-theory-builder.md)
   definitions, and whatever the run broke in those definitions is returned
   to the library as a revision, not patched here.
4. The exact run records are retained under `kb/reports/retained/`, and
   any transferable finding becomes a note. The protocol either becomes an
   instruction, if a second run is wanted, or is retained with the records.

## Evaluation boundary

Evidence is the protocol and episodes as moved here, the library definitions
they cite, and the records the run produces. The
[boundary-case assessment](../../reports/retained/theory-builder-boundary-cases-20260917.md)
records how prior systems fare on the four deployment questions the run
must answer for Commonplace. No measurement exists yet; the protocol's own
statement that it is not evidence of a completed run stands until closing
condition 2 is met.

## Coordination

- [explanatory-theories-deployment-time-learning](../explanatory-theories-deployment-time-learning/README.md)
  owns component-comparison experiment designs; this workshop runs the
  downstream comparison and does not redesign those.
- [theory-builder-refactor](../theory-builder-refactor/README.md) owns the
  remaining promotion and migration work; a definition the run breaks is
  reported there while it is open, and revised in the library directly
  after it closes.

Write scope while open: this directory, plus `kb/reports/retained/` for
exact run records.
