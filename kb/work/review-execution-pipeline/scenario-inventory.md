# Review execution scenario inventory

## Purpose

Inventory every review-execution scenario the current system covers so the pipeline refactor does not accidentally optimize for only the live-agent path. The system has one pair protocol, but several execution media and packing shapes.

## Shared Concepts

- **Review pair**: one requested check of one note against one gate. Prompt/output sentinel blocks identify pairs by `(note_path, gate_path)`.
- **Model partition**: the model identity for persisted state. In the current implementation it is stored on `review_runs`, copied to `review_pairs`, and included in current acceptance identity as `(note_path, gate_path, model_partition)`.
- **Review job**: target vocabulary for one queued unit of review execution. Current code calls this `review_run`; the queue plan renames `review_runs` / `review_run_id` to `review_jobs` / `review_job_id` so schema and command language agree.
- **Review run**: current implementation name for a review job. Use only when describing existing code or existing command output.
- **Packing**: how many pairs ride in one prompt. Current persisted values are `note` and `gate`.
- **Execution medium**: who consumes the prompt and writes output: a subprocess runner, the current/live agent, or an external orchestrator/sub-agent.

## Scenario Matrix

| ID | Scenario | User surface | Packing | Execution medium | Current flow |
|---|---|---|---|---|---|
| S1 | Direct one-note bundle review | `commonplace-run-review-bundles` | `note` | subprocess runner (`claude-code` or `codex`) | group requested gates by bundle, create one current `review_run` per group, call `executor.execute_batch`, runner writes stdout, executor parses and finalizes |
| S2 | Direct one-gate sweep | `commonplace-run-gate-sweep` | `gate` | subprocess runner (`claude-code` or `codex`) | select stale notes for one gate, chunk notes, create one current `review_run` per chunk, call `executor.execute_batch`, salvage parsed pairs if some are missing |
| S3 | Parallel subprocess review sweep | `commonplace-review-sweep` | `note` per job | subprocess runner through a thread pool | select stale pairs for a bundle or all bundles, group by note, submit many `run_bundles` calls concurrently |
| S4 | Live-agent one-note review | `commonplace-create-review-runs` + `commonplace-ingest-bundle-output` | `note` | current agent / delegated sub-agent | create one prepared current `review_run` per bundle, write prompt and manifest, parent delegates prompt, agent writes `bundle-output.md`, ingest finalizes |
| S5 | External orchestrator batch review | `commonplace-prepare-review-batch` + `commonplace-ingest-batch-output` | `note` or `gate` | external workflow or parent-managed sub-agents | prepare one arbitrary same-axis pair batch, write prompt and manifest, outside executor writes output, ingest finalizes with salvage |
| S6 | Dry-run prompt preview | `--dry-run` on subprocess-facing commands | `note` or `gate` | none | run selection and prompt rendering, print command/prompt, do not create or finalize review state unless the command's dry-run path explicitly says so |
| S7 | Ingest/recovery of already prepared output | ingest commands | existing job packing | job-owned file | load a queued/running job, read its stored `bundle_output_path`, parse output, refresh artifacts, mark completed/missing/failed |
| S8 | Stale-target selection without execution | `commonplace-review-target-selector`, selectors inside sweeps | none | none | compare current files against accepted snapshots for a model partition, return stale `(note, gate)` candidates |
| S9 | Acknowledgement without new review execution | `commonplace-ack-gate-review`, `commonplace-ack-trivial-note-changes` | none | none | carry forward an existing completed review pair to current snapshots without asking a reviewer to re-run gates |
| S10 | Queued execution | proposed queue commands | `note` or `gate` | subprocess, live-agent, or external worker | selector output feeds job creation; prepared jobs enter a queue; workers claim or receive jobs and execute with configured parallelism |

## Scenario Notes

### S1: Direct One-Note Subprocess Review

This is the subprocess case that is easiest to forget when looking only at live-agent workflows. `run_review_bundles.py` creates a persisted run, then `executor.execute_batch` renders the prompt and invokes `run_prompt`. The runner adapter launches `claude` or `codex exec`, streams output, scrapes telemetry when available, and returns stdout/stderr/return code.

Pipeline implication: a future pipeline must have an active `execute` stage that invokes a runner and immediately proceeds to ingest/finalize. It cannot only model "prepare queued job now, ingest later."

### S2: Direct One-Gate Subprocess Sweep

`run_gate_sweep.py` flips the packing axis: one gate over many notes. It still uses `execute_batch`, but the run owns many note/gate pairs for the same gate. Missing pairs are recoverable: parsed pairs can be completed while unreturned pairs become `missing` and the run fails.

Pipeline implication: the prepared-job model must represent both note-packed and gate-packed prompts, and ingest must preserve pair-level salvage.

### S3: Parallel Subprocess Sweep

`review_sweep.py` is orchestration over S1. It selects stale pairs, groups them into note-local jobs, and submits `run_bundles` calls in a thread pool. It does not introduce a new protocol, but it introduces concurrency, usage-exhaustion abort behavior, and many independent current `review_runs`.

Pipeline implication: the shared core must remain safe when many independent jobs are prepared/executed/finalized concurrently.

### S4: Live-Agent One-Note Review

`create_review_runs.py` prepares bundle-local runs and returns prompt/output paths as JSON. A parent agent delegates each prompt to a sub-agent or follows it directly, then runs `ingest_bundle_output.py`. This path exists because some workflows must not shell out to `claude` or `codex exec` from inside the command.

Pipeline implication: "execute" can be a suspension point. The same prepared-job object should serve both subprocess execution and live-agent handoff.

### S5: External Orchestrator Batch Review

`prepare_review_batch.py` exposes deterministic prepare/render for arbitrary same-axis pair batches. It was added for harness-orchestrated sweeps where the orchestrator owns fan-out and sub-agent execution. The paired `ingest_batch_output.py` uses the shared parser/finalizer and supports salvage.

Pipeline implication: the pipeline must expose batch-granular deterministic boundaries, not just whole-command subprocess runs.

### S6: Dry-Run Preview

Dry-run paths exist to inspect selected targets and rendered prompts without executing reviewers. They are useful for command debugging, context-size estimation, and operator approval.

Pipeline implication: prepare/render must be separable from persistence and execution where current command behavior requires a preview-only path.

### S7: Finalize/Recovery

Finalization commands are not only normal completion steps. They are recovery tools after an interrupted parent session, delayed sub-agent response, or manually repaired output file. The job should own the normal bundle output path (currently `review_runs.bundle_output_path`), so the target command is `commonplace-finalize-review-job --review-job-id {id}`. For the first version, do not expose a path override; recovery edits the job-owned `bundle-output.md` in place before finalization.

Pipeline implication: finalization must remain independently callable by `review_job_id`, with the job-owned bundle output path as the only v1 input.

### S8: Selection Without Execution

Selectors identify stale pairs without preparing jobs. They are part of the review system but sit before execution. They must stay outside the execution pipeline or feed it as an upstream stage.

Pipeline implication: do not bake stale selection into job preparation. Explicit pair input and selector-produced pair input both need to work.

### S9: Acknowledgement Without New Review Execution

Acknowledgement commands update acceptance state without a new review output. Target semantics: ack accepts that an existing completed review remains valid for the current note/gate snapshots. It should therefore retain a pointer to the review pair being carried forward, not create a review-less acceptance baseline.

Pipeline implication: acceptance-writing logic should stay factored so finalization and acknowledgement cannot drift, and ack should fail when no completed review pair exists for the pair/model.

### S10: Queued Execution

The proposed queue-oriented pipeline separates stale-target selection from job creation and separates job creation from execution. This is the missing generalization behind `review_sweep`: parallelism should belong to a queue worker over prepared jobs, not to selector commands or bespoke sweep wrappers.

Pipeline implication: prepared jobs need a queueable state. The current `review_runs.status` values are `running`, `completed`, and `failed`; the queue plan requires `queued` so a prepared prompt is not falsely recorded as already running.

## Coverage Checklist for a Pipeline Refactor

A proposed pipeline design must answer:

- Can it prepare a note-packed job and execute it immediately through a subprocess?
- Can it prepare a gate-packed job and salvage partial output?
- Can it suspend after rendering and resume later by `review_job_id`?
- Can it handle many concurrent subprocess jobs?
- Can it expose deterministic prepare/ingest endpoints to external orchestrators?
- Can it render dry-run prompts without unwanted persistent state changes?
- Does it preserve `(note_path, gate_path, model_partition)` as persisted acceptance identity?
- Does it keep selector-only and acknowledgement-only workflows outside the execution path while making ack require an existing completed review pair?
- Can selector JSON feed job creation without a bespoke sweep command?
- Can queue workers own parallelism, claiming, retry, and usage-exhaustion policy?
