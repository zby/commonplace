# Phase 4: Job-owned finalization

**Status: planned.** Phase 4 makes finalization operate from persisted job metadata instead of caller-supplied output paths.

## Purpose

Complete the orchestrator path:

```text
create queued jobs -> parent claims dispatched job -> worker writes job-owned bundle-output.md -> parent finalizes by job id
```

The parent remains the database writer. Workers remain file transducers from `prompt_path` to `bundle_output_path`. In the normal orchestrator path, the parent marks a job `running` with known runner/model/effort provenance when it dispatches the worker; finalization still accepts `queued` for manual recovery or transitional outputs that were produced without an explicit dispatch update.

## Scope

In scope:

- add `commonplace-claim-review-job --review-job-id --runner --model [--effort]` for orchestrator parent dispatch bookkeeping;
- add `commonplace-finalize-review-job --review-job-id`;
- load the job through the Phase 3 `ReviewJobPlan` loader with `require_paths=True`;
- validate the claim's concrete worker model and optional effort against the job's `model_partition`;
- claim queued jobs with `status = 'running'`, `started_at`, `runner`, `runner_model`, and nullable `runner_effort`;
- read `bundle_output_path` from `review_jobs`;
- accept jobs in `queued` or `running`;
- reject `completed` and `failed`;
- parse bundle output keyed by `(note_path, gate_path)`;
- preserve existing pair salvage behavior;
- write canonical per-pair result Markdown with provenance frontmatter;
- append acceptance events for completed pairs;
- mark the job `completed` or `failed`;
- update operational docs and command references that agents follow so they use claim/finalize-by-job-id instead of the removed ingest commands;
- remove public `commonplace-ingest-bundle-output` and `commonplace-ingest-batch-output` surfaces, with no compatibility wrapper.

Out of scope:

- subprocess job execution;
- worker-agent DB access;
- adding a path override such as `--input-file`;
- changing pair sentinel grammar;
- changing ack behavior;
- changing model-partition storage, which Phase 3 already settled.

## Command shape

```bash
commonplace-claim-review-job --review-job-id 42 --runner codex --model gpt-5
commonplace-finalize-review-job --review-job-id 42
```

The claim command records parent-dispatch provenance only; it does not execute a worker. `--runner` names the worker/execution medium being dispatched, not the parent orchestrator that is recording the dispatch. `--model` is the concrete worker model. If effort is known and meaningful for that worker, pass `--effort`; otherwise it stays null. Claim validation is exact: `build_model_partition(--model, --effort)` must equal the job's `model_partition`, so a job partition that encodes effort requires the matching `--effort` flag. Recovery edits the canonical `bundle-output.md` in place before finalization. A noncanonical output path is deferred until a real recovery workflow requires it.

## Implementation notes

- Reuse `record_and_finalize_job` as the acceptance/final-state persistence core; do not reintroduce run vocabulary.
- Finalization should call the shared `ReviewJobPlan` loader with `require_paths=True`; a missing `bundle_output_path`, prompt path, or required per-pair result path is a clear job-plan error, not a fallback to path rediscovery.
- Do not read `MANIFEST.json` during finalization. It is an inspection artifact from Phase 3, not pipeline state.
- Use the same internal claim helper that the subprocess runner will use later, so claim semantics do not diverge. The helper performs one atomic update guarded by `review_job_id`, `status = 'queued'`, and the validated `model_partition`; a zero-row update is a claim failure, not a partial success.
- Keep the widened Phase 1 gate: finalization accepts `queued` or `running`, even though normal executor paths should mark `running` at claim/dispatch time.
- Missing output files should fail clearly without changing job state. A missing file may mean the worker has not written yet; only an existing output that fails parse or coverage should move the job to `failed`.
- Parse failures and missing pairs should keep existing salvage semantics: completed pairs may be accepted while the job records failure context for missing or invalid output.
- Newly written pair result Markdown wraps the canonical parsed review text in frontmatter with `review_job_id`, `review_pair_id`, `note_path`, `gate_path`, `model_partition`, nullable `runner`, nullable `runner_model`, nullable `runner_effort`, `decision`, and `reviewed_at`; the review body below the frontmatter stays the canonical parsed text.

## Tests

- finalization reads the persisted `bundle_output_path`;
- finalization loads a `ReviewJobPlan` with `require_paths=True`;
- finalization does not read `MANIFEST.json`;
- claim marks a queued job `running` and records `started_at`, `runner`, `runner_model`, and nullable `runner_effort`;
- claim rejects completed/failed/running jobs;
- claim rejects model/effort that do not match the job's `model_partition`;
- claim with omitted effort rejects a job whose `model_partition` includes effort;
- claim with omitted effort records null `runner_effort`;
- double claim updates exactly one caller and leaves the second caller with a clear claim failure;
- a queued job finalizes successfully after the worker writes output;
- a running job finalizes successfully;
- completed and failed jobs are rejected;
- missing output file errors clearly without marking the job failed;
- parse errors mark the job failed and preserve appropriate failure reason;
- partial output salvages completed pairs and marks missing pairs;
- result Markdown frontmatter includes model and runner provenance from the job;
- old `--input-file` surface is absent;
- old ingest commands are absent from package entry points, and a fresh install/build does not expose those console scripts;
- operational docs no longer tell agents to use ingest commands for the orchestrator path.

## Done when

Phase 4 is done when live-agent/orchestrator review no longer needs an ingest command with an explicit file path: the durable job owns the output path, finalization only needs the job id, and generated per-pair result files are self-describing enough for human/debug use.
