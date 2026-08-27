# Evidence boundary

The workshop originates in analysis run
`AAS-2026-08-27-commonplace-review-freshness-01`. The run froze revision
`c5afbf1c5efff02d47d71c4bf05779fa5170ab4a` and inspected the review/freshness
subsystem from selection through result read-back. At workshop creation, the
registered subsystem files remained byte-equivalent at checkout revision
`64e84517712ffa61682bd3f63ba859223f9330cc`.

## Inspected material

- implementation under `src/commonplace/review/`, `src/commonplace/freshness/`,
  the review/freshness CLIs, `src/commonplace/store.py`, and
  `src/commonplace/store-schema.sql`;
- [review architecture](../../reference/review-architecture.md),
  [freshness architecture](../../reference/freshness-architecture.md),
  [the review-system guide](../../reference/README-REVIEW-SYSTEM.md),
  [the batch procedure](../../instructions/run-review-batches.md), the
  [review-gate contract](../../types/review-gate.md), and the grounding and fix
  contracts; and
- registered review, freshness, worker-contract, and store-health tests.

## Observed checks

The complete test suite passed: `580 passed in 30.01s`. Disposable-repository
interventions also established that:

- finalizing `FAIL` creates a fresh baseline, removes the pair from stale
  selection, and does not place it in the warning queue;
- changing only linked evidence leaves a completed pair fresh;
- changing only derived result prose changes warning read-back while the
  SQLite outcome stays unchanged;
- an invalid declared snapshot hash and canonical source do not prevent
  model-shaped `PASS` output from finalizing and becoming fresh;
- failure in a later creation group leaves earlier queued state and the failing
  job in SQLite without returning their normal JSON handles; and
- `extract_warns()` returns an explicit `- warn:` item from PASS-shaped input.

These interventions establish deterministic subsystem behavior. They do not
establish what a properly instructed external reviewer would read, infer, or
return.

## Excluded evidence

No real provider trace, parent-harness dispatch trace, production review store,
operator disposition history, or gate-calibration corpus was inspected. The
workshop therefore treats activation frequency, reviewer accuracy, production
incidence, and model-equivalence quality as unresolved.
