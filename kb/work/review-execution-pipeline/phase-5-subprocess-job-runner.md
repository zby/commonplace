# Phase 5: Subprocess job runner

**Status: ready to implement.** Phase 5 makes subprocess execution consume the same queued jobs that the orchestrator path uses.

## Purpose

Replace bespoke subprocess execution paths with a queue runner:

```text
select targets -> create queued jobs -> operator/automation runs queued jobs through subprocess adapters -> finalize
```

Start sequentially. Parallelism can move here only after single-worker claim/finalize behavior is stable.

Phase 4 is now the baseline: `commonplace-claim-review-job` and `commonplace-finalize-review-job` exist, the public ingest commands are gone, and the shared claim helper in `review_db.py` is the only `queued -> running` transition the subprocess runner should use.

## Scope

In scope:

- add `commonplace-run-review-jobs`;
- add a small internal queue-runner module, for example `commonplace.review.run_review_jobs`, plus the CLI wrapper;
- add the `commonplace-run-review-jobs` console script;
- factor the job-owned finalization body from `commonplace-finalize-review-job` into a reusable internal helper shared by the CLI and the subprocess queue runner;
- make `commonplace-run-review-jobs` a queue consumer run by a human/operator, CI job, scheduled process, or wrapper command;
- pull queued jobs from the DB by the requested concrete model/effort's partition;
- support optional explicit `--review-job-id` narrowing for recovery/debug runs;
- implement sequential execution only in the first slice; do not implement multi-worker parallelism in this phase;
- select candidate jobs with `list_review_job_plans(..., status="queued", model_partition=requested_partition, require_paths=False)`;
- claim selected jobs with the Phase 4 `claim_review_job` helper, which atomically sets `status = 'running'`, `started_at`, `runner`, `runner_model`, and nullable `runner_effort`; pass it the required keyword-only `model_partition=requested_partition`;
- treat `ReviewJobClaimError` as an unclaimed job, not a partially failed execution; explicit `--review-job-id` runs must preflight the unfiltered job before claiming, because the queue-mode filtered candidate list cannot represent the full set of missing, non-queued, wrong-partition, and missing-path failures;
- use the `ReviewJobPlan` returned by `claim_review_job`; it has already loaded with `require_paths=True`;
- validate `build_model_partition(--model, --effort) == review_jobs.model_partition` before claiming a job, with `--effort` allowed only when the adapter can set it;
- make the minimal runner-adapter API/capability change required for effort support: adapters declare whether they can set effort, and `run_prompt` / `build_command` accept nullable effort;
- invoke runner adapters through that shared adapter path;
- pass the concrete `--model` argument to the runner adapter;
- pass effort to the runner adapter only when that adapter can actually set it;
- collect telemetry through the existing adapter-owned optional API and store it only when available;
- read the already-rendered `prompt_path` from the claimed `ReviewJobPlan`; do not render a new prompt from note/gate files;
- write runner stdout to the persisted `bundle_output_path` from the claimed plan;
- write `debug.log` next to the job output when stdout/stderr diagnostics are available;
- attach telemetry, and telemetry-derived runner model/effort when available, before finalization so result frontmatter sees the best known provenance;
- finalize each job through the same job-owned bundle finalization path used by `commonplace-finalize-review-job`;
- never read `MANIFEST.json` as queue or execution state;
- update command reference/operator docs when the new subprocess command becomes public;
- preserve existing usage-exhaustion behavior;
- update or retire old subprocess convenience commands so they no longer own job creation or finalization policy.

Out of scope:

- formal orchestrator leases;
- orchestrator-agent worker dispatch;
- retrying failed jobs by resetting them to `queued`;
- broad runner-adapter refactors beyond the minimal effort capability/API needed here;
- changing model identity semantics;
- requiring every runner adapter to support effort;
- requiring telemetry for successful execution;
- changing pair parsing or finalization policy;
- moving `commonplace-review-sweep` parallel scheduling into the new runner command; wrappers may remain temporarily if they compose the canonical queue stages.

## Command shape

```bash
commonplace-run-review-jobs --runner codex --model gpt-5 --limit 20
commonplace-run-review-jobs --runner claude-code --model claude-opus-4-6 --stop-on-usage-exhausted
commonplace-run-review-jobs --runner codex --model gpt-5 --effort high --limit 20
commonplace-run-review-jobs --runner codex --model gpt-5 --review-job-id 42
```

Do not add `--parallel` in the first implementation. A later subphase can introduce it after the sequential command has stable claim, execution, finalization, and JSON behavior.

Primary mode is queue-driven: the command selects queued jobs whose `model_partition` matches `build_model_partition(--model, --effort)`, up to `--limit` if supplied. `--review-job-id` is a narrowing filter, not a separate input protocol; each listed job must still be queued and in the requested model partition.

Do not pass `model_partition` as the runnable model id. The concrete `--model` is the runner argument. The partition is only the validation/freshness key.

`--effort` is nullable and adapter-gated. If supplied for an adapter that cannot set effort, fail early before selection or claim rather than silently ignoring it. If omitted, compute the requested partition with `build_model_partition(--model, None)` and claim with `runner_effort = NULL`. Telemetry may later fill `runner_effort` if the adapter reports the actual inherited effort.

`--limit` defaults to 1 for the first implementation. A queue-driven run with no matching jobs exits 0 and reports an empty result.

The first implementation stops after the first claimed job that fails execution or finalization. Later work can add a `--keep-going` policy if operators need best-effort processing across many queued jobs.

## Selection and Claiming

Before selecting jobs, the runner:

1. validates `--runner`;
2. validates `--model` is non-empty;
3. normalizes `--effort`;
4. rejects `--effort` if the selected adapter cannot set it;
5. computes `requested_partition = build_model_partition(--model, --effort)`.

Candidate selection is tolerant of migrated or malformed jobs:

```python
list_review_job_plans(
    conn,
    status="queued",
    model_partition=requested_partition,
    require_paths=False,
)
```

Queue-driven mode uses that filtered list directly, then applies `--limit`. A queued candidate that cannot be claimed is reported under `skipped`, and the runner continues to the next candidate.

Explicit `--review-job-id` mode does not start from the filtered candidate list. It first loads the requested job with:

```python
load_review_job_plan(
    conn,
    review_job_id=requested_review_job_id,
    require_paths=False,
)
```

Because explicit job-id runs are for recovery/debug, a missing job, non-queued job, wrong-partition job, or missing load-bearing path is an operational failure and exits nonzero before runner invocation. Preflight in that order: job exists, `status == "queued"`, `model_partition == requested_partition`, `prompt_path` present, `bundle_output_path` present, and every pair has `result_path` present. Only after that preflight should the runner call `claim_review_job`.

This preflight is for precise operator-facing errors, not for replacing the atomic claim. `claim_review_job` still performs the authoritative short transaction, including the model-partition and path guards, so a lost race or concurrent state change remains a `ReviewJobClaimError` after preflight.

Claiming is a short transaction:

```sql
UPDATE review_jobs
SET status = 'running',
    started_at = ?,
    runner = ?,
    runner_model = ?,
    runner_effort = ?
WHERE review_job_id = ? AND status = 'queued'
  AND model_partition = ?
  AND prompt_path IS NOT NULL
  AND bundle_output_path IS NOT NULL
  AND NOT EXISTS (
      SELECT 1
      FROM review_pairs AS rp
      WHERE rp.review_job_id = review_jobs.review_job_id
        AND rp.result_path IS NULL
  )
```

Do not duplicate that SQL in the runner. Call the Phase 4 `claim_review_job` helper so command-line claiming and subprocess claiming cannot diverge.

Signature precision for the implementer (verified against the committed Phase 4 code): `claim_review_job` takes a required keyword-only `model_partition=`; `list_review_job_plans`'s `status`/`model_partition`/`require_paths` are keyword-only; `build_model_partition`'s second parameter is named `reasoning_effort`, not `effort`; `model_partition` lives on `review_jobs`, not `review_pairs`; and `require_paths` is a loader argument, not a `ReviewJobPlan` field. Use these exact names in code even where this plan's prose abbreviates them.

If zero rows are updated, another worker claimed or completed the job, the job does not belong to the requested model partition, or it lacks load-bearing paths. The helper raises `ReviewJobClaimError`. Queue-driven runs skip and report the reason; explicit job-id runs fail before model execution. Missing required job-plan paths are not execution failures because no execution was claimed.

Do not hold a DB transaction while a model process is running.

## Adapter Effort Contract

Make the adapter change explicit and minimal:

```python
class RunnerAdapter:
    supports_effort: ClassVar[bool] = False

    def build_command(
        self,
        *,
        prompt: str,
        repo_root: Path,
        model: str | None,
        effort: str | None,
    ) -> tuple[list[str], str]: ...
```

`run_prompt` accepts the same nullable `effort` argument. It rejects a non-null effort when `adapter.supports_effort` is false before constructing a subprocess command.

Initial adapters should keep `supports_effort = False` unless the implementation adds and tests a concrete CLI flag for that harness. This is allowed: Phase 5 needs the capability boundary and early rejection behavior, not universal effort support.

## Execution and Finalization

For each claimed plan:

1. read `repo_root / plan.prompt_path`;
2. call `run_prompt(runner=..., prompt=prompt_text, repo_root=..., model=args.model, effort=args.effort_if_supported)`;
3. write `result.stdout` exactly to `repo_root / plan.bundle_output_path`;
4. write `debug.log` next to `bundle-output.md` when combined stdout/stderr diagnostics are non-empty;
5. serialize adapter telemetry when present and attach it with `attach_execution_data`;
6. if telemetry carries concrete model or effort, attach those values before finalization;
7. detect usage exhaustion with the existing text check, fail the claimed job with `runner reported usage exhausted`, and stop subsequent jobs;
8. on nonzero runner exit, fail the claimed job with `"{runner} exited {returncode}"` and stop subsequent jobs;
9. on zero runner exit, call the shared helper factored from `commonplace-finalize-review-job`; the helper reads the persisted job-owned output path, applies the same precondition checks, and uses the same parser, salvage policy, and result-artifact path.

Do not use `persist_bundle_artifacts` for the new runner unless it is first changed to honor the persisted `ReviewJobPlan.bundle_output_path`; the existing helper derives the standard path from the job id. Phase 5 execution must consume stored paths, not rediscover them.

`commonplace-finalize-review-job` currently keeps its path preconditions in the CLI. Phase 5 should first factor that body into an internal helper such as `finalize_review_job_from_owned_output(repo_root, db_path, review_job_id)`, returning a structured outcome that both CLIs can render as JSON. Internally, the helper may call `finalize_bundle_markdown(..., persist_output=False)` after reading the job-owned output file.

## JSON and Exit Contract

`commonplace-run-review-jobs` prints one JSON object on every non-argparse-error path:

```json
{
  "requested": {
    "runner": "codex",
    "model": "gpt-5",
    "effort": null,
    "model_partition": "codex",
    "limit": 1,
    "review_job_id": null
  },
  "selected_count": 1,
  "completed_count": 1,
  "failed_count": 0,
  "skipped_count": 0,
  "usage_exhausted": false,
  "jobs": [
    {
      "review_job_id": 42,
      "status": "completed",
      "runner_returncode": 0,
      "completed_pair_count": 2,
      "failure_reason": null,
      "bundle_output_path": "kb/reports/bundle-reviews/review-job-42/bundle-output.md",
      "debug_log_path": "kb/reports/bundle-reviews/review-job-42/debug.log"
    }
  ],
  "skipped": []
}
```

Exit 0 when every selected and claimed job completes successfully, and also when queue-driven selection finds no matching jobs. Exit 1 when any claimed job fails execution or finalization, when explicit `--review-job-id` cannot be claimed, or when usage exhaustion stops the run. Exit 130 on `KeyboardInterrupt` after failing the active claimed job with a clear interruption reason.

## Old Subprocess Commands

Phase 5 should remove bespoke subprocess job creation/finalization policy from:

- `commonplace-run-review-bundles`;
- `commonplace-run-gate-sweep`;
- `commonplace-review-sweep`.

The preferred first implementation is to keep the public convenience commands but rewrite them as wrappers around the canonical stages:

1. create queued jobs with `commonplace-create-review-jobs` semantics;
2. run those specific job ids through `commonplace-run-review-jobs`;
3. report the existing human summary from the canonical JSON result.

If a command is not worth keeping, retire it from `pyproject.toml` and documentation in this phase. Do not leave any public subprocess command that still calls `create_job_with_pairs` and `execute_batch` directly as its durable execution path.

The `create_job_with_pairs` + `execute_batch` coupling does not live in the `cli/review/*.py` wrapper scripts; those delegate one layer down. `execute_batch` (in `executor.py`) is the function that does create-job → render prompt → `run_prompt` → persist → `attach_execution_data` in one shot, and it is invoked from the `review/run_review_bundles.py` and `review/run_gate_sweep.py` lib modules (`review_sweep` reaches it through `run_bundles`). Target those lib modules, not the CLI entrypoints, when removing the bespoke create+execute path.

## Tests

- sequential runner completes queued jobs;
- queue-driven mode selects queued jobs matching `build_model_partition(--model, --effort)`;
- explicit `--review-job-id` narrows selection but does not bypass queued-status or partition checks;
- runner calls the Phase 4 `claim_review_job` helper rather than duplicating claim SQL;
- claim sets `started_at`, `status = running`, `runner`, `runner_model`, and nullable `runner_effort`;
- claim update includes the requested model partition and path preconditions;
- runner uses the `ReviewJobPlan` returned by claim;
- missing required job-plan paths produce a claim failure without changing job state;
- explicit `--review-job-id` with missing required paths exits nonzero before runner invocation;
- explicit `--review-job-id` failures report distinct reasons for wrong-partition vs missing-path vs non-queued, proving the runner uses an unfiltered preflight load rather than reading them off the single `ReviewJobClaimError`;
- runner does not read `MANIFEST.json`;
- two workers cannot claim the same queued job;
- runner receives the concrete `--model` as its model argument;
- `run_prompt` and `RunnerAdapter.build_command` accept nullable effort;
- adapters that support effort receive the concrete effort argument;
- adapters that do not support effort reject a supplied `--effort`;
- omitted effort computes the no-effort model partition and claims with `runner_effort = NULL`;
- telemetry-reported effort may update `runner_effort` before finalization;
- mismatched `--model` / job partition refuses the job before claim;
- telemetry absence does not fail the job;
- runner reads the persisted prompt file and writes the persisted bundle output path;
- runner writes debug logs without changing the persisted bundle output path;
- nonzero runner exit marks the job failed and preserves logs;
- usage exhaustion stops subsequent jobs;
- partial parse salvage is the same as Phase 4 finalization;
- output JSON matches the documented success, empty queue, skipped claim, execution failure, finalization failure, and usage-exhausted shapes;
- command exits 0 for empty queue-driven selection and successful completion;
- command exits nonzero for explicit unclaimable job ids and claimed job failures;
- command reference/operator docs describe `commonplace-run-review-jobs` as the subprocess queue consumer, not as an orchestrator worker-list command;
- `commonplace-run-review-bundles`, `commonplace-run-gate-sweep`, and `commonplace-review-sweep` either compose the new command or are retired according to command cleanup policy;
- no remaining public subprocess command creates review jobs with `create_job_with_pairs` and finalizes through `execute_batch` as its durable path.

## Done when

Phase 5 is done when `commonplace-run-review-jobs` is the canonical subprocess queue consumer, sequential queued jobs can be claimed, executed, finalized, and reported through one JSON contract, runner adapters have an explicit effort capability boundary, and no public subprocess path needs its own job-creation or finalization policy.
