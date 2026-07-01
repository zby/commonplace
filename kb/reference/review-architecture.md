---
description: "Code architecture for the current Commonplace review subsystem: selector JSON, queued jobs, prompt artifacts, parent-dispatched workers, finalization, freshness, and maintenance utilities"
type: kb/types/note.md
tags: []
status: current
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review subsystem stores review state in SQLite, renders canonical prompt artifacts for `(note, gate)` pairs, and finalizes worker-written review output. It does not launch reviewer models itself. The parent agent or harness owns worker dispatch; Commonplace owns deterministic selection, job creation, claiming, finalization, freshness, and maintenance.

For the operating workflow, see [REVIEW-SYSTEM.md](./REVIEW-SYSTEM.md) and [run review batches](../instructions/run-review-batches.md).

## Package layout

- `commonplace.review` — library modules: SQLite access, freshness, gate resolution, prompt preparation, output parsing/finalization, artifact writing, acknowledgement, warning selection, and maintenance helpers.
- `commonplace.cli.review` — thin command wrappers around those library modules. Each command parses arguments, resolves the repo root and review DB, then calls one library operation.

## Current execution flow

```
review_target_selector  -> selector JSON
create_review_jobs      -> queued review_jobs + review_pairs + prompt artifacts
claim_review_job        -> running job + worker provenance
worker/sub-agent        -> writes derived bundle_output_path
finalize_review_job     -> parse output, write result artifacts, append acceptance
```

The persisted unit is a `review_pairs` row inside one `review_jobs` row. The job's `packing` is either `note` or `gate`; packing controls only which pairs share one prompt and how per-pair result files are named. It is not a separate review protocol.

## Data model

SQLite database, default location `kb/reports/review-store.sqlite`; override with `COMMONPLACE_REVIEW_DB` or command-specific `--db`.

| Table | Purpose |
|---|---|
| `review_jobs` | One prompt/output invocation, with model partition, nullable worker provenance, status, and packing |
| `review_pairs` | Requested and completed `(note_path, gate_path)` outcomes inside a job |
| `review_file_snapshots` | Exact note and gate text captured when the prompt was created |
| `acceptance_events` | Append-only accepted baselines for freshness |

`current_gate_acceptances` derives the latest accepted state per `(note_path, gate_path, model_partition)`. `review_pairs` derive `model_partition` through their parent job.

## Core modules

### Selection and gates

- `review_target_selector.py` lists stale or requested applicable `(note, gate)` pairs. It is read-only.
- `resolve_gates.py` expands bundle names into gate ids and filters gates by note type and traits.
- `paths.py` resolves the active gate catalog and translates between gate ids and repo-relative gate paths.

### Job creation

- `batch.py` creates queued jobs from normalized pair lists. It snapshots note/gate files, inserts job and pair rows, renders prompts, writes `MANIFEST.json`, and returns derived prompt/output/result paths.
- `freshness.py` captures snapshot-backed review inputs for prompt generation.
- `job_prompt.py` prepares `NoteReviewTarget` objects, including resolved and unresolved local markdown links.
- `artifacts.py` owns artifact directory selection, result-file naming, result frontmatter, per-pair result writes, and manifest writing.

### Protocol and finalization

- `protocol/format.py` defines pair sentinels and render-time reserved-text checks.
- `protocol/prompt.py` renders canonical review prompts from captured text. In file-output mode, the prompt instructs a worker to write exactly the job's derived `bundle_output_path`.
- `protocol/parser.py` parses sentinel-bracketed pair output. Structural anomalies fail the job; missing expected pairs are reported so completed pairs can still be salvaged.
- `protocol/decisions.py` normalizes `PASS`, `WARN`, `FAIL`, and `ERROR` result lines.
- `finalization.py` is the public library operation behind `commonplace-finalize-review-job`; it loads derived job output, parses bundle output, writes result files, refreshes manifests, completes rows, marks failures, and appends acceptance events.

### State and maintenance

- `review_db.py` owns review rows, claims, status transitions, acceptance events, and query helpers.
- `review_model.py` normalizes model partitions and optional reasoning-effort labels.
- `acknowledgement.py` advances accepted baselines for trivial changes while carrying forward completed review evidence.
- `ack_trivial_note_changes.py` finds stale pairs whose watched note portions did not change.
- `warn_selector.py` extracts actionable warn findings from effective accepted reviews.
- `review_schema.py` owns current-schema setup and integrity checks.
- CLI maintenance modules handle superseded-review pruning and model-partition repair.

## Command Surface

Execution path:

- `commonplace-review-target-selector`
- `commonplace-create-review-jobs`
- `commonplace-claim-review-job`
- `commonplace-finalize-review-job`

State and maintenance:

- `commonplace-review-job-list`
- `commonplace-ack-gate-review`
- `commonplace-ack-trivial-note-changes`
- `commonplace-warn-selector`
- `commonplace-resolve-gates`
- `commonplace-prune-superseded-reviews`
- `commonplace-repair-model-partitions`

## Invariants

- Job creation always consumes selector JSON. There is no direct note/pair creation mode.
- Worker agents write only the job-owned bundle output file; they do not mutate notes, gates, indexes, manifests, or review DB state.
- `MANIFEST.json` is inspectable output, not pipeline state.
- Finalization accepts `queued` or `running` jobs so manually produced output can be recovered.
- Acceptance state is path-keyed; relocating notes or gates requires fresh review under the new path.
- Missing telemetry is normal. Review identity is `(note_path, gate_path, model_partition)`, not worker-provided execution metadata.
