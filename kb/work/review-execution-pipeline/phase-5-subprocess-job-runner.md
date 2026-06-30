# Phase 5: Subprocess job runner

**Status: planned.** Phase 5 makes subprocess execution consume the same queued jobs that the orchestrator path uses.

## Purpose

Replace bespoke subprocess execution paths with a queue runner:

```text
select targets -> create queued jobs -> run queued jobs through subprocess adapters -> finalize
```

Start sequentially. Parallelism can move here only after single-worker claim/finalize behavior is stable.

## Scope

In scope:

- add `commonplace-run-review-jobs`;
- claim jobs with an atomic `queued -> running` update;
- set `started_at` on claim;
- set `runner` on claim/execution;
- invoke the existing runner adapters;
- for the first version, pass the job's `model_partition` as the runner model argument and store no separate `runner_model`;
- defer `runner_model` persistence until there is a concrete need to distinguish freshness partition from runner argument in queued execution;
- write `bundle-output.md` and debug logs;
- finalize each job through the Phase 4 finalization path;
- preserve existing usage-exhaustion behavior;
- eventually move `commonplace-review-sweep` parallelism into this command.

Out of scope:

- formal orchestrator leases;
- retrying failed jobs by resetting them to `queued`;
- changing runner adapters;
- changing model identity semantics;
- changing pair parsing or finalization policy.

## Command shape

```bash
commonplace-run-review-jobs --runner codex --limit 20
commonplace-run-review-jobs --runner claude-code --stop-on-usage-exhausted
commonplace-run-review-jobs --runner codex --parallel 4
```

Sequential behavior comes first. `--parallel` can initially be accepted only as `1`, or omitted until the parallel subphase.

## Claiming

Claiming is a short transaction:

```sql
UPDATE review_jobs
SET status = 'running',
    started_at = ?,
    runner = ?
WHERE review_job_id = ? AND status = 'queued'
```

If zero rows are updated, another worker claimed or completed the job; skip it.

Do not hold a DB transaction while a model process is running. Parallel mode uses one SQLite connection per worker and a `busy_timeout`.

## Tests

- sequential runner completes queued jobs;
- claim sets `started_at` and status `running`;
- claim records `runner`;
- two workers cannot claim the same queued job;
- runner receives the job's `model_partition` as its model argument in the first version;
- nonzero runner exit marks the job failed and preserves logs;
- usage exhaustion stops subsequent jobs;
- partial parse salvage is the same as Phase 4 finalization;
- existing `run_review_bundles`, `run_gate_sweep`, and `review_sweep` either compose the new command or are retired according to command cleanup policy.

## Done when

Phase 5 is done when subprocess review uses persisted queued jobs as its work source and no subprocess path needs its own run/job creation or finalization policy.
