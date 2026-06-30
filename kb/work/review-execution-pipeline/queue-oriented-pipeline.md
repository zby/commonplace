# Queue-oriented review pipeline

## Claim

The cleaner pipeline shape is:

```text
select stale targets -> create queued review jobs -> execute queued jobs -> ingest/finalize results
```

Neither stale-target selection nor job creation owns parallelism. Parallelism lives in whoever *consumes* the queue, and there are two such consumers:

- the **subprocess runner** (`commonplace-run-review-jobs`) owns parallelism when an operator/automation process asks Commonplace to shell out to `codex` / `claude-code`;
- the **orchestrator agent** owns parallelism when it fans out its own agent workers over queued jobs (the dominant path today — see [Orchestrator-driven execution](#orchestrator-driven-execution)).

Both consume the same queued jobs. Selection and creation stay sequential and side-effect-light.

## Naming: jobs, not runs

This document uses **job** as the canonical noun for one queued unit of review execution. The persisted entity is currently `review_runs`; under the project's no-backcompat rule it is renamed to `review_jobs` (and `review_run_id` → `review_job_id`) so the command vocabulary and the schema agree. That rename is mechanical bulk and can land in its own commit; the load-bearing schema change is the status enum below.

## State model: the load-bearing change

This is the architectural decision the rest of the design hangs on, so it leads.

The current schema allows only:

```text
running, completed, failed
```

Queue execution needs a separate prepared state and an honest clock:

```text
queued, running, completed, failed
created_at NOT NULL, started_at NULL, completed_at NULL
```

with clean meanings:

- `queued`: prompt and pair rows exist; no worker has claimed execution;
- `running`: a worker has claimed execution;
- `completed`: all required pairs completed and accepted;
- `failed`: execution, parse, or coverage failed; salvaged pairs may be retained per policy.

`created_at` records preparation time. `started_at` records worker claim/start time. Normal subprocess and orchestrator executor paths mark a job `running` when they claim or dispatch it; finalization still accepts `queued` for manual recovery or transitional outputs that were produced without an explicit dispatch update.

**These schema changes are required.** The workshop scope now treats the queue/job schema changes as part of the simplification, so the queue work travels with a small schema migration (the `review_runs.status` CHECK constraint, the clock change above, plus the table/column rename above) and likely a short ADR. Two concrete code consequences:

- the `status IN (...)` CHECK in `review-schema.sql` gains `queued`;
- `batch.ingest` currently rejects any job whose status is not `running` (`batch.py:258`). Finalization must accept `queued` too, because a manual/orchestrator recovery path may have a valid job-owned output for a job that was never marked `running`. Decision: **finalization accepts `queued` or `running`, rejects `completed`/`failed`.**

This also removes the existing live-agent lie where a prepared prompt is recorded as `running` before any reviewer has started.

## Proposed Stage Commands

### 1. Select stale targets

```bash
commonplace-review-target-selector --json --model {model-partition} {bundle-or-gate...} --note kb/notes
commonplace-review-target-selector --json --model {model-partition} --all-gates --current
```

Output becomes a stable producer contract:

```json
{
  "model_partition": "claude-opus-4-6",
  "targets": [
    {
      "note_path": "kb/notes/example.md",
      "gate_path": "kb/instructions/review-gates/prose/source-residue.md",
      "gate_id": "prose/source-residue",
      "reason": "missing-review"
    }
  ]
}
```

The current implementation returns a JSON list of `note_path`, `gate_path`, `reason`, optional `diff`. The producer contract adds top-level `model_partition` and normalized `gate_path` / `gate_id`. Diffs stay inspection-only (keep the producer payload small).

### 2. Create queued jobs from targets

```bash
commonplace-create-review-jobs --input targets.json --grouping note
commonplace-create-review-jobs --input targets.json --grouping gate --batch-size 5
```

Responsibilities:

- read selector output (file or stdin, default stdin so `selector | create-jobs` composes);
- take `model_partition` from the selector output; optional `--model` only validates that it matches;
- group targets by the requested creation grouping;
- filter inapplicable pairs defensively if needed;
- capture note/gate snapshots;
- create review jobs and review pairs;
- render prompts and manifests;
- leave jobs `queued`, not running.

The job owns `model_partition`; pair/result rows do not need to duplicate it. The generated per-pair review-result Markdown should include `model_partition` in frontmatter so the artifact remains self-describing.

This is the queue-oriented successor to `commonplace-prepare-review-batch` and `commonplace-create-review-runs`.

### 3. Inspect the queue

```bash
commonplace-review-job-list --model {model-partition}
commonplace-review-job-list --status queued
commonplace-review-job-list --json
```

Responsibilities:

- list queued/running/failed/completed jobs;
- show prompt path, output path, pair count, packing, runner, model partition, age, and failure reason;
- support recovery after interrupted execution.

Subsumes the existing `review-run-status-command` proposal; queue execution makes the need sharper.

### 4. Execute queued jobs (subprocess medium)

```bash
commonplace-run-review-jobs --runner codex --model gpt-5 --parallel 4 --limit 20
commonplace-run-review-jobs --runner claude-code --model claude-opus-4-6 --parallel 1 --stop-on-usage-exhausted
```

Responsibilities:

- select queued jobs whose `model_partition` matches `build_model_partition(--model, --effort)`;
- optionally narrow selection with explicit job ids for recovery/debug runs;
- claim selected queued jobs;
- mark each claimed job `running` with `runner`, `runner_model`, and nullable `runner_effort`;
- invoke the runner adapter for each prompt;
- pass the concrete `--model` to the runner adapter;
- pass effort only to adapters that can actually set it;
- collect telemetry through an optional adapter-owned API;
- write `bundle-output.md` and debug logs;
- parse/finalize each job;
- enforce parallelism, retry, and abort policy.

This absorbs the thread-pool parallelism currently embedded in `commonplace-review-sweep`.

### 5. Dispatch queued jobs (agent-worker medium)

```bash
commonplace-review-job-list --status queued --json
commonplace-claim-review-job --review-job-id {id} --runner orchestrator --model {model} [--effort {effort}]
commonplace-finalize-review-job --review-job-id {id}
```

Responsibilities:

- let the parent/current agent or an external harness dispatch one queued prompt;
- mark the dispatched job `running` with known runner/model/effort provenance;
- have the worker follow `prompt_path` and write `bundle_output_path`;
- finalize through the same parser/finalizer as subprocess workers.

See [Orchestrator-driven execution](#orchestrator-driven-execution) for why this path needs no transactional claiming.

## Orchestrator-driven execution

This is the most common parallel case in practice — the path in [run-review-batches-on-note.md](../../instructions/run-review-batches-on-note.md) — so the design is checked against it directly.

Current flow:

1. `commonplace-create-review-runs` creates one run per bundle and returns run objects (`review_run_id`, `prompt_path`, `bundle_output_path`, `manifest_path`).
2. The parent agent launches **one sub-agent per run**, bounded by the harness concurrency limit, queuing overflow until workers free. Each sub-agent is a pure `prompt_path → bundle_output_path` transducer and is explicitly forbidden from running any `commonplace-*` command or touching review state.
3. The parent finalizes each finished output with `commonplace-finalize-review-job`.

Mapping onto the queue design:

| Today | Queue-oriented |
|---|---|
| `create-review-runs` (one note, bundle-grouped) | `create-review-jobs --grouping note` -> jobs land `queued` |
| parent fans out sub-agents over the returned runs | parent claims selected jobs, then fans out sub-agents over the returned/`job-list`ed jobs |
| parent ingests each | parent finalizes each (`running` -> `completed`; `queued` is accepted only for recovery) |

Two consequences fall out, and both **simplify** the design:

1. **The parent is the sole DB writer.** Sub-agents never touch review state; they only read a prompt and write a file. So the queue here is not a contended shared queue — it is a worklist the single orchestrator process dispenses. **Transactional multi-process claiming is not needed for this path, and it is the common one.** It is needed only when independent subprocess workers claim jobs directly from the DB.

2. **The `running` transition is where execution provenance is recorded.** The parent should mark a job `running` at dispatch with `runner`, `runner_model`, and nullable `runner_effort`. If the harness cannot expose effort, `runner_effort` stays null. Finalization still accepts `queued` for recovery, but the normal orchestrator flow records dispatch.

Net effect on the instruction file: `create-review-runs` -> `create-review-jobs`, returned objects carry `status: queued`, the parent claims each dispatched job, and ingest becomes finalize-by-job-id. The dominant path migrates with a rename and a narrower finalization surface.

## Bundle Output Path Ownership

The review job should own its bundle output path. The current schema already has `review_runs.bundle_output_path`, so the normal finalization surface should not require the operator to restate the same path:

```bash
commonplace-finalize-review-job --review-job-id 42
```

The command should load `bundle_output_path` from the job record, read that file, and finalize it. For the first version, do not expose a path override. One job has one canonical bundle output file; recovery can edit that file in place before finalization.

If a later recovery workflow needs an override, add it then with an operator-facing name such as `--bundle-output`. Avoid the confusing `--input-file bundle-output.md` wording. The file is input to the ingest program, but it is output in the review domain.

## Creation Mode And Persisted Packing

Job creation from selected targets owns grouping mode; selection only emits stale pairs. The `--grouping` flag is a creation policy. Persisted `packing` remains only `note` or `gate`; `explicit` and `bundle` are not new stored enum values in v1.

- `note`: group selected pairs by note and bundle/lens; persisted as `packing = note`;
- `gate`: group selected pairs by gate, chunk notes by `--batch-size`; persisted as `packing = gate`;

A single-note input under `--grouping note` and a single-gate input under `--grouping gate` cover the old explicit batch cases without adding a third grouping mode.

## Retry and snapshot freshness (design facts, not open questions)

`create-review-jobs` captures note/gate snapshots at creation time, and acceptance identity is `(note_path, gate_path, model_partition)`. So retry semantics are constrained, not free:

- **Retry creates a new job**, re-capturing snapshots. This is the default and the only correct general policy: a failed job may have sat in the queue while the note changed underneath its snapshot.
- **Resetting a failed job to `queued`** replays its original (possibly stale) snapshot, so it is valid only when the snapshot is provably current. **v1 does not offer reset** — retry always means a new job. Revisit only if snapshot re-capture proves expensive.

## What Existing Commands Become

The goal is net line reduction: the bespoke selection+grouping+execution+parallelism tangles are **retired**, not wrapped forever.

| Current command | Fate |
|---|---|
| `commonplace-review-target-selector` | Stage 1 selector, stabilized JSON output |
| `commonplace-prepare-review-batch` | Removed; its same-axis batches are expressible as one `--grouping note` or `--grouping gate` input |
| `commonplace-create-review-runs` | Replaced by `create-review-jobs --grouping note`; removed |
| `commonplace-run-review-bundles` | Thin wrapper (create note-packed jobs for one note, run immediately) — retained for ergonomics |
| `commonplace-run-gate-sweep` | Retired into `select -> create-jobs --grouping gate -> run-review-jobs` |
| `commonplace-review-sweep` | Retired into `select -> create-jobs -> run-review-jobs --parallel N`; its thread pool moves into the runner |
| `commonplace-ingest-bundle-output` / `commonplace-ingest-batch-output` | Removed; replaced by `commonplace-finalize-review-job --review-job-id` |
| `commonplace-ack-gate-review` / `commonplace-ack-trivial-note-changes` | Retained, but changed to carry forward an existing completed review pair instead of creating review-less acceptance events |

A small number of ergonomic wrappers stay and compose the stages; the experimental sweep commands and the two parallel-prepare commands go away. Surface area and line count both fall.

## Remaining Open Questions

1. Does the orchestrator path ever need a formal lease/timeout, or is `job-list` + manual recovery enough? *(v1: manual.)*
2. If a future recovery workflow needs a noncanonical output path, add `--bundle-output`, or always edit the job-owned file in place?

Resolved and moved out of this list: queue storage (status column, not a second table); orchestrator leases (not needed in v1 because the parent is the single DB writer); subprocess claiming (atomic update, one SQLite connection per worker when parallelism returns); retry semantics (new job, see above); selector diffs (inspection-only); input channel (file or stdin).

Important simplification: historical review records are not relocated on note move. Review identity remains path-keyed; a moved path needs fresh review under the new path. Ack can only carry forward an existing completed review pair for the same path/model.

## Current Phase Boundary

1. Phase 1 landed the migration substrate, `queued`, and honest job timing on the old table names.
2. Phase 2 mechanically renames `review_runs` / `review_run_id` to `review_jobs` / `review_job_id`.
3. Phase 3 stabilizes selector JSON, creates queued jobs, adds job listing, and drops pair-level `model_partition`.
4. Phase 4 adds parent-dispatch claiming, finalizes by job id, writes result provenance frontmatter, and removes explicit ingest surfaces.
5. Phase 5 adds the sequential subprocess job runner.
6. Phase 6 makes ack carry forward an existing completed review pair.
7. Phase 7 stops relocating review state on note moves.
8. Phase 8 promotes the ADR/reference docs and closes or narrows the workshop.
