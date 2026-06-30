# Phase 5: Subprocess job runner

**Status: planned.** Phase 5 makes subprocess execution consume the same queued jobs that the orchestrator path uses.

## Purpose

Replace bespoke subprocess execution paths with a queue runner:

```text
select targets -> create queued jobs -> operator/automation runs queued jobs through subprocess adapters -> finalize
```

Start sequentially. Parallelism can move here only after single-worker claim/finalize behavior is stable.

## Scope

In scope:

- add `commonplace-run-review-jobs`;
- make `commonplace-run-review-jobs` a queue consumer run by a human/operator, CI job, scheduled process, or wrapper command;
- pull queued jobs from the DB by requested concrete model's normalized partition;
- support optional explicit `--review-job-id` narrowing for recovery/debug runs;
- validate `normalize_model_partition(--model) == review_jobs.model_partition` before claiming a job;
- claim selected jobs with an atomic `queued -> running` update;
- set `started_at` on claim;
- set `runner` on claim/execution;
- invoke the existing runner adapters;
- pass the concrete `--model` argument to the runner adapter;
- defer `runner_model` persistence until there is a concrete need for first-class execution provenance;
- write `bundle-output.md` and debug logs;
- finalize each job through the Phase 4 finalization path;
- preserve existing usage-exhaustion behavior;
- eventually move `commonplace-review-sweep` parallelism into this command.

Out of scope:

- formal orchestrator leases;
- orchestrator-agent worker dispatch;
- retrying failed jobs by resetting them to `queued`;
- changing runner adapters;
- changing model identity semantics;
- adding a runner effort option in v1;
- changing pair parsing or finalization policy.

## Command shape

```bash
commonplace-run-review-jobs --runner codex --model gpt-5 --limit 20
commonplace-run-review-jobs --runner claude-code --model claude-opus-4-6 --stop-on-usage-exhausted
commonplace-run-review-jobs --runner codex --model gpt-5 --parallel 4
commonplace-run-review-jobs --runner codex --model gpt-5 --review-job-id 42
```

Sequential behavior comes first. `--parallel` can initially be accepted only as `1`, or omitted until the parallel subphase.

Primary mode is queue-driven: the command selects queued jobs whose `model_partition` matches `normalize_model_partition(--model)`, up to `--limit` if supplied. `--review-job-id` is a narrowing filter, not a separate input protocol; each listed job must still be queued and in the requested model partition.

Do not pass `model_partition` as the runnable model id. The concrete `--model` is the runner argument. The partition is only the validation/freshness key.

Do not add `--effort` in v1. If a runner-specific effort option is added later, only adapters that can actually set effort may accept it; unsupported adapters must fail early.

## Selection and Claiming

Before claiming a job, the runner computes `requested_partition = normalize_model_partition(--model)`. It selects queued jobs where `review_jobs.model_partition = requested_partition`, plus any explicit `--review-job-id` narrowing.

Claiming is a short transaction:

```sql
UPDATE review_jobs
SET status = 'running',
    started_at = ?,
    runner = ?
WHERE review_job_id = ? AND status = 'queued'
  AND model_partition = ?
```

If zero rows are updated, another worker claimed or completed the job, or the job does not belong to the requested model partition; skip it or report the mismatch for explicit `--review-job-id` runs.

Do not hold a DB transaction while a model process is running. Parallel mode uses one SQLite connection per worker and a `busy_timeout`.

## Tests

- sequential runner completes queued jobs;
- queue-driven mode selects queued jobs matching `normalize_model_partition(--model)`;
- explicit `--review-job-id` narrows selection but does not bypass queued-status or partition checks;
- claim sets `started_at` and status `running`;
- claim records `runner`;
- claim update includes the requested model partition;
- two workers cannot claim the same queued job;
- runner receives the concrete `--model` as its model argument;
- mismatched `--model` / job partition refuses the job before claim;
- v1 exposes no `--effort` option;
- nonzero runner exit marks the job failed and preserves logs;
- usage exhaustion stops subsequent jobs;
- partial parse salvage is the same as Phase 4 finalization;
- existing `run_review_bundles`, `run_gate_sweep`, and `review_sweep` either compose the new command or are retired according to command cleanup policy.

## Done when

Phase 5 is done when subprocess review uses persisted queued jobs as its work source and no subprocess path needs its own run/job creation or finalization policy.
