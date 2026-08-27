# RF-16 — Result-file writes are not transactionally atomic

**State:** open  
**Repair shape:** filesystem staging and recovery  
**Severity:** medium  
**Related:** [RF-09](./rf-09-result-prose-is-unbound-mutable-state.md)

## Finding

A multi-pair finalization writes result files sequentially before committing
SQLite. If a later write fails, the database transaction rolls back and the job
is marked failed, but an earlier successfully written result file is not removed.
A process crash can produce the same cross-substrate split.

## Evidence

- [`write_pair_result_files_to_derived_paths()`](../../../src/commonplace/review/artifacts.py)
  writes each pending file directly in sequence.
- [`finalize_review_job()`](../../../src/commonplace/review/finalization.py) writes
  the files before `conn.commit()`.
- [`_mark_failed()`](../../../src/commonplace/review/finalization.py) rolls back
  SQLite and refreshes the manifest but does not remove partial result files.

## Why it matters

The documented all-or-nothing property is sound for canonical DB completion on
handled errors, but not for the filesystem-plus-database artifact set. Orphaned
result prose can mislead manual inspection and complicate later regeneration.

## Provisional repair direction

Stage every result under temporary names, verify all writes, commit canonical
state, then atomically rename; or make result files fully derived from canonical
DB bodies as proposed in RF-09. Define startup/health recovery for interrupted
staging.

## Done when

- Failure during the second of multiple writes leaves no apparently final result
  for the failed job.
- Crash recovery can distinguish staged, canonical, and orphaned artifacts.
- Tests inject a partial multi-file failure rather than replacing the whole
  writer with an immediate failure.
