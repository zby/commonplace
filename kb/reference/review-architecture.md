---
description: "Code architecture of the Commonplace review subsystem: package layout, storage schema, canonical state vs derived output, freshness mechanism, module map, and finalization invariants"
type: kb/types/note.md
tags: []
status: current
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review subsystem stores review state in SQLite, renders canonical prompt artifacts for `(note, gate)` pairs, and finalizes worker-written review output. It does not launch reviewer models itself: the parent agent or harness owns worker dispatch, while Commonplace owns deterministic selection, job creation, finalization, freshness, and maintenance.

This document describes how the subsystem is built. For how to operate it, see [review system](./README-REVIEW-SYSTEM.md) and [run review batches](../instructions/run-review-batches.md).

## Package layout

- `commonplace.review` — library modules: SQLite access, freshness, gate resolution, prompt preparation, output parsing/finalization, artifact writing, acknowledgement, warning selection, and maintenance helpers.
- `commonplace.cli.review` — thin command wrappers. Each command parses arguments, resolves the repo root and review DB, then calls one library operation.

## Execution flow

```
review_target_selector  -> selector JSON
create_review_jobs      -> queued review_jobs + review_pairs + prompt artifacts
worker/sub-agent        -> writes derived bundle_output_path
finalize_review_job     -> validate provenance, parse output, write result artifacts, append acceptance
```

The persisted unit is a `review_pairs` row inside one `review_jobs` row. A job's `packing` is either `note` or `gate`; packing controls only which pairs share one prompt and how per-pair result files are named. It is not a separate review protocol.

## Data model

SQLite database, default location `kb/reports/review-store.sqlite`; override with `COMMONPLACE_REVIEW_DB` or a command-specific `--db`. `review_schema.py` owns current-schema setup and integrity checks; the store is schema-current and recreated rather than migrated in place.

| Table | Contents |
|---|---|
| `review_jobs` | One review invocation: model partition, nullable runner/model/effort provenance, status, packing (`note`/`gate`), `created_at`, nullable `completed_at`, telemetry, failure context |
| `review_pairs` | One requested `(note_path, gate_path)` pair inside a job: decision and reviewed note/gate snapshot IDs; derives `model_partition` from its parent job |
| `review_file_snapshots` | Role-neutral snapshots by `(path, content_sha256)`, storing exact UTF-8 text when it must be reusable for prompt rendering or diffing |
| `acceptance_events` | Append-only accepted baselines; `accepted_review_pair_id` points at completed review evidence; the latest event wins per key |

Artifact paths — prompt, bundle output, manifest, and per-pair result files — are **derived** from `review_job_id`, packing, and the job's pairs. They are not stored columns.

The `current_gate_acceptances` view derives the latest accepted state per `(note_path, gate_path, model_partition)` key: the highest `acceptance_events.acceptance_event_id` for that key, after filtering to completed jobs with non-null pair decisions. This filter is the evidence boundary — acceptance rows from non-completed jobs never surface as freshness.

### Canonical state vs derived output

The DB is the source of truth; human-readable markdown is derived.

- `review_pairs.decision` is a lowercase enum: `pass`, `warn`, `fail`, `error`. `review_jobs.status` is a lowercase enum: `queued`, `completed`, `failed`. The Python layer assigns both.
- `created_at` is when the job row and prompt inputs were prepared. Runner provenance is optional and recorded during finalization.
- The review **body** is not in the DB. The finalizer writes it to the per-pair result file (at the derived result path) from the parsed `bundle-output.md`; the DB stores only the pair `decision`. `MANIFEST.json` is reconstructed from DB rows and holds no prose. Only the manifest is reproducible from the DB alone.
- Stored gate review prose ends each pair block with exactly one parseable `## Result: PASS|WARN|FAIL|ERROR` line. Aliases such as `Verdict`, `Outcome`, `INFO`, `OK`, and `UNKNOWN` are invalid in live finalization output.

### Freshness mechanism

The selector computes SHA-256 over the current note and gate text and compares it against the accepted snapshot hashes from `current_gate_acceptances`, reconstructing note diffs from accepted snapshot text. Rows with null accepted snapshots report as `missing-review` with the diff unavailable. There is no separate bundle manifest hash; if bundle-level manifests ever become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf gate-file hash.

## Core modules

### Selection and gates

- `review_target_selector.py` lists stale or requested applicable `(note, gate)` pairs. Read-only.
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
- `protocol/parser.py` parses sentinel-bracketed pair output. Structural anomalies, missing expected pairs, duplicates, and malformed result footers fail the whole job.
- `protocol/decisions.py` strictly accepts exactly one final `## Result: PASS|WARN|FAIL|ERROR` line per pair block.
- `finalization.py` is the public library operation behind `commonplace-finalize-review-job`. It loads derived job output, validates optional runner/model/effort provenance, parses the bundle, and — only after all parse and coverage preflight passes — writes result files, completes pair rows, appends acceptance events, and marks the job completed. Result-file write failures roll back and fail the job in a separate transaction; `MANIFEST.json` refresh runs after DB completion and its failure is a non-fatal warning.

### State and maintenance

- `review_db.py` owns review rows, finalization state transitions, acceptance events, and query helpers.
- `review_model.py` normalizes model partitions and optional reasoning-effort labels.
- `acknowledgement.py` advances accepted baselines for trivial changes while carrying forward completed review evidence.
- `ack_trivial_note_changes.py` finds stale pairs whose watched note portions did not change.
- `warn_selector.py` extracts actionable warn findings from effective accepted reviews.
- `review_schema.py` owns current-schema setup and integrity checks.
- CLI maintenance modules handle superseded-review pruning.

## Command surface

Execution path:

- `commonplace-review-target-selector`
- `commonplace-create-review-jobs`
- `commonplace-finalize-review-job`

State and maintenance:

- `commonplace-review-job-list`
- `commonplace-ack-gate-review`
- `commonplace-ack-trivial-note-changes`
- `commonplace-warn-selector`
- `commonplace-resolve-gates`
- `commonplace-prune-superseded-reviews`

## Invariants

- Job creation always consumes selector JSON. There is no direct note/pair creation mode.
- Worker agents write only the job-owned bundle output file; they do not mutate notes, gates, indexes, manifests, or review DB state.
- `MANIFEST.json` is inspectable output, not pipeline state.
- Finalization accepts only `queued` jobs and moves them atomically to `completed` or `failed`.
- Failed jobs append no acceptance events and leave pair decisions null.
- `current_gate_acceptances` filters acceptance evidence to completed jobs with non-null pair decisions.
- Acceptance state is path-keyed; relocating notes or gates requires fresh review under the new path.
- Missing telemetry is normal. Review identity is `(note_path, gate_path, model_partition)`, not worker-provided execution metadata.
