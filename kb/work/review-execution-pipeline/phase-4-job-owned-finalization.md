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
- load the job through the shared `ReviewJobPlan` / `PreparedReviewJob`;
- validate claim model/effort against the job's `model_partition`;
- claim queued jobs with `status = 'running'`, `started_at`, `runner`, `runner_model`, and nullable `runner_effort`;
- read `bundle_output_path` from `review_jobs`;
- accept jobs in `queued` or `running`;
- reject `completed` and `failed`;
- parse bundle output keyed by `(note_path, gate_path)`;
- preserve existing pair salvage behavior;
- write canonical per-pair result Markdown with provenance frontmatter;
- append acceptance events for completed pairs;
- mark the job `completed` or `failed`;
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
commonplace-claim-review-job --review-job-id 42 --runner orchestrator --model claude-opus-4-6
commonplace-finalize-review-job --review-job-id 42
```

The claim command records parent-dispatch provenance only; it does not execute a worker. If effort is known and meaningful for the dispatching harness, pass `--effort`; otherwise it stays null. Recovery edits the canonical `bundle-output.md` in place before finalization. A noncanonical output path is deferred until a real recovery workflow requires it.

## Implementation notes

- `record_and_finalize_run` should be renamed to job vocabulary if Phase 2 did not already do so.
- Use the same internal claim helper that the subprocess runner will use later, so claim semantics do not diverge.
- Keep the widened Phase 1 gate: finalization accepts `queued` or `running`, even though normal executor paths should mark `running` at claim/dispatch time.
- Missing output files should fail clearly without marking unrelated jobs.
- Parse failures and missing pairs should keep existing salvage semantics: completed pairs may be accepted while the job records failure context for missing or invalid output.
- Newly written pair result Markdown includes frontmatter with `review_job_id`, `review_pair_id`, `note_path`, `gate_path`, `model_partition`, nullable `runner`, nullable `runner_model`, nullable `runner_effort`, `decision`, and `reviewed_at`.

## Tests

- finalization reads the persisted `bundle_output_path`;
- claim marks a queued job `running` and records `started_at`, `runner`, `runner_model`, and nullable `runner_effort`;
- claim rejects completed/failed/running jobs;
- claim rejects model/effort that do not match the job's `model_partition`;
- claim with omitted effort records null `runner_effort`;
- a queued job finalizes successfully after the worker writes output;
- a running job finalizes successfully;
- completed and failed jobs are rejected;
- missing output file errors clearly;
- parse errors mark the job failed and preserve appropriate failure reason;
- partial output salvages completed pairs and marks missing pairs;
- result Markdown frontmatter includes model and runner provenance from the job;
- old `--input-file` surface is absent;
- old ingest commands are absent from `pyproject.toml` and fail as command names.

## Done when

Phase 4 is done when live-agent/orchestrator review no longer needs an ingest command with an explicit file path: the durable job owns the output path, finalization only needs the job id, and generated per-pair result files are self-describing enough for human/debug use.
