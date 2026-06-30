# Phase 4: Job-owned finalization

**Status: ready to implement.** Phase 4 makes finalization operate from persisted job metadata instead of caller-supplied output paths.

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

## JSON output contracts

Both new commands print JSON on every non-usage path. Invalid CLI usage may still use the normal argparse error path. Operational failures return nonzero with a JSON payload so orchestrators can distinguish claim conflicts, job-plan errors, missing output, and finalization failures.

`commonplace-claim-review-job` success exits 0:

```json
{
  "claimed": true,
  "review_job_id": 42,
  "job": {
    "review_job_id": 42,
    "status": "running",
    "model_partition": "codex",
    "runner": "codex",
    "runner_model": "gpt-5",
    "runner_effort": null,
    "packing": "note",
    "prompt_path": "kb/reports/bundle-reviews/review-job-42/prompt.md",
    "bundle_output_path": "kb/reports/bundle-reviews/review-job-42/bundle-output.md",
    "manifest_path": "kb/reports/bundle-reviews/review-job-42/MANIFEST.json",
    "pair_count": 1,
    "pairs": []
  }
}
```

The embedded `job` object uses the same shape as `commonplace-review-job-list --json`; the example elides pair details.

Claim failure exits 1:

```json
{
  "claimed": false,
  "review_job_id": 42,
  "reason": "review job is not claimable: running"
}
```

`commonplace-finalize-review-job` completion exits 0:

```json
{
  "completed": true,
  "state_changed": true,
  "review_job_id": 42,
  "completed_pair_count": 1,
  "failed": [],
  "job": {
    "review_job_id": 42,
    "status": "completed"
  }
}
```

If finalization reads an existing output file but parsing or coverage fails, it salvages completed pairs where possible, marks the job `failed`, and exits 1:

```json
{
  "completed": false,
  "state_changed": true,
  "review_job_id": 42,
  "completed_pair_count": 1,
  "failed": [
    {
      "review_job_id": 42,
      "reason": "missing pairs: kb/notes/example.md :: kb/instructions/review-gates/prose/source-residue.md"
    }
  ],
  "job": {
    "review_job_id": 42,
    "status": "failed"
  }
}
```

If finalization fails before it is allowed to mutate state, such as a missing `bundle-output.md`, a non-finalizable status, or a strict job-plan path error, it exits 1 with `state_changed: false`:

```json
{
  "completed": false,
  "state_changed": false,
  "review_job_id": 42,
  "reason": "bundle output file not found: kb/reports/bundle-reviews/review-job-42/bundle-output.md"
}
```

## Implementation notes

- Reuse `record_and_finalize_job` as the acceptance/final-state persistence core; do not reintroduce run vocabulary.
- Finalization should call the shared `ReviewJobPlan` loader with `require_paths=True`; a missing `bundle_output_path`, prompt path, or required per-pair result path is a clear job-plan error, not a fallback to path rediscovery.
- Do not read `MANIFEST.json` during finalization. It is an inspection artifact from Phase 3, not pipeline state. Finalization refreshes it for human/debug inspection, but the refreshed manifest must be derived only from `ReviewJobPlan` and DB rows.
- Use the same internal claim helper that the subprocess runner will use later, so claim semantics do not diverge. Add it in `review_db.py` in this phase. The helper performs one atomic update guarded by `review_job_id`, `status = 'queued'`, and the validated `model_partition`; a zero-row update is a claim failure, not a partial success. On success, load and return the updated `ReviewJobPlan`.
- Keep the widened Phase 1 gate: finalization accepts `queued` or `running`, even though normal executor paths should mark `running` at claim/dispatch time.
- Missing output files should fail clearly without changing job state. A missing file may mean the worker has not written yet; only an existing output that fails parse or coverage should move the job to `failed`.
- Parse failures and missing pairs should keep existing salvage semantics: completed pairs may be accepted while the job records failure context for missing or invalid output.
- Newly written pair result Markdown wraps the canonical parsed review text in deterministic frontmatter with `review_job_id`, `review_pair_id`, `note_path`, `gate_path`, `model_partition`, `runner`, `runner_model`, `runner_effort`, `decision`, and `reviewed_at`. Keep nullable keys present with YAML `null` values. Use the DB-updated pair `decision` and `reviewed_at` values; the review body below the frontmatter stays exactly the canonical parsed text.
- Write each pair result to its persisted `ReviewPairRow.result_path`. Do not recompute result filenames during finalization. Filename derivation belongs to job creation; finalization consumes stored paths.

## Tests

- finalization reads the persisted `bundle_output_path`;
- finalization loads a `ReviewJobPlan` with `require_paths=True`;
- finalization does not read `MANIFEST.json`;
- finalization refreshes `MANIFEST.json` from DB state without using it as input;
- finalization writes result Markdown to persisted `result_path`, including a nonstandard path edited into the DB for the test;
- finalization emits JSON success, mutated failure, and precondition failure payloads with the documented exit codes;
- claim marks a queued job `running` and records `started_at`, `runner`, `runner_model`, and nullable `runner_effort`;
- claim emits JSON success and failure payloads with the documented exit codes;
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
- result Markdown frontmatter keeps nullable provenance keys present as YAML nulls;
- result Markdown frontmatter uses the DB-updated `decision` and `reviewed_at`;
- old `--input-file` surface is absent;
- old ingest commands are absent from package entry points, and a fresh install/build does not expose those console scripts;
- operational docs no longer tell agents to use ingest commands for the orchestrator path.

## Done when

Phase 4 is done when live-agent/orchestrator review no longer needs an ingest command with an explicit file path: the durable job owns the output path, finalization only needs the job id, and generated per-pair result files are self-describing enough for human/debug use.
