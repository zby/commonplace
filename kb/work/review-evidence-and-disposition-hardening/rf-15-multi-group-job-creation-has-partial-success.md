# RF-15 — Multi-group job creation has partial success without a recovery payload

**State:** open  
**Repair shape:** request transaction or explicit partial-success protocol  
**Severity:** medium

## Finding

The create command prepares groups sequentially. Each job is committed before
the next group starts, while normal JSON output is emitted only after all groups
succeed. A later failure can leave earlier queued jobs and a failed current job
in SQLite while the caller receives no job IDs.

## Evidence

- [`create_review_jobs.main()`](../../../src/commonplace/cli/review/create_review_jobs.py)
  loops over groups and prints its payload after the loop.
- [`prepare_grouped_review_job()`](../../../src/commonplace/review/batch.py)
  commits each job before rendering and writing its artifacts.
- The multi-group intervention in
  [the evidence boundary](./evidence-boundary.md) observed one queued and one
  failed persisted job after the command exited without its normal JSON handles.

## Why it matters

The parent cannot know from the failed invocation which work already exists.
Blind retry can duplicate jobs; abandoning the request can strand queued work.

## Provisional repair direction

Either validate and prepare the entire request before committing any group, or
define partial success as a first-class result that always returns every created
job and its state. If jobs remain, provide an explicit cancel/retry operation.

## Done when

- A failed request leaves no jobs, or returns complete machine-readable handles
  for every persisted job.
- Retry behavior is idempotent or detects prior creation.
- Tests fail a later group after an earlier success and assert recovery behavior.
