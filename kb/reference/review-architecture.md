---
description: "Code architecture of the Commonplace review subsystem: package layout, storage schema, canonical state vs derived output, freshness mechanism, module map, and finalization invariants"
type: kb/types/note.md
tags: []
status: current
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review subsystem stores assay state in SQLite, renders canonical prompt artifacts for `(note, criterion)` pairs, and finalizes worker-written output. The persisted criterion field remains named `gate_path`. It does not launch reviewer models itself: the parent agent or harness owns worker dispatch, while Commonplace owns deterministic selection, job creation, finalization, freshness, and maintenance.

This document describes how the subsystem is built. For how to operate it, see [review system](./README-REVIEW-SYSTEM.md) and [run review batches](../instructions/run-review-batches.md).

## Package layout

- `commonplace.review` — library modules: SQLite access, freshness, gate resolution, prompt preparation, output parsing/finalization, artifact writing, acknowledgement, warning selection, and maintenance helpers.
- `commonplace.cli.review` — thin command wrappers. Each command parses arguments, resolves the repo root and review DB, then calls one library operation.

## Execution flow

```
review_target_selector  -> selector JSON
create_review_jobs      -> queued review_jobs + review_pairs + prompt artifacts
worker/sub-agent        -> writes derived bundle_output_path
finalize_review_job     -> validate provenance, parse output, record completion, upsert acceptance
```

The persisted unit is a `review_pairs` row inside one `review_jobs` row. A job's `packing` is either `note` or `gate`; `gate` here means the shared `gate_path`/criterion axis. Packing controls only prompt sharing and result filenames. Every job is result-kind homogeneous.

## Data model

SQLite database, default location `kb/reports/review-store.sqlite`; override with `COMMONPLACE_REVIEW_DB` or a command-specific `--db`. `review_schema.py` owns current-schema setup and integrity checks. Schema v4 stores are upgraded in place by `scripts/migrate-review-db-v4-to-v5.py`; other version mismatches are refused.

| Table | Contents |
|---|---|
| `review_jobs` | One review invocation: model partition, nullable runner/model/effort provenance, status, packing (`note`/`gate`), `created_at`, nullable `completed_at`, telemetry, failure context |
| `review_pairs` | One requested `(note_path, gate_path)` pair inside a job: persisted `result_kind` (`verdict`/`report`), nullable decision, and reviewed note/gate snapshot IDs; derives `model_partition` from its parent job |
| `review_file_snapshots` | Role-neutral snapshots by `(path, content_sha256)`, storing exact UTF-8 text when it must be reusable for prompt rendering or diffing |
| `acceptance` | Current freshness baseline per `(note_path, gate_path, model_partition)`; `accepted_review_pair_id` points at completed evidence and accepted snapshot IDs pin note/criterion text |

Artifact paths — prompt, bundle output, manifest, and per-pair result files — are **derived**, not stored columns. Each per-pair result filename (`pair-{ordinal}-{stem}.md`) is a pure function of that pair's own row (`pair_ordinal` plus the packing-varying path stem), never of sibling pairs, so inline pruning of superseded sibling pairs cannot change a surviving pair's path.

The `current_gate_acceptances` view exposes accepted state per `(note_path, gate_path, model_partition)` key by joining `acceptance` through `review_pairs` and `review_jobs`. It requires a completed job and per-kind pair completion: a verdict pair has `reviewed_at` plus a decision; a report pair has `reviewed_at` and a null decision. This filter is the evidence boundary — acceptance rows from non-completed jobs never surface as freshness.

### Canonical state vs derived output

The DB is the source of truth; human-readable markdown is derived.

- `review_pairs.result_kind` is `verdict` or `report`. Verdict decisions use the lowercase enum `pass`, `warn`, `fail`, `error`; report pairs keep `decision` null. `review_jobs.status` is `queued`, `completed`, or `failed`.
- `created_at` is when the job row and prompt inputs were prepared. Runner provenance is optional and recorded during finalization.
- The review **body** is not in the DB. The finalizer writes it to the derived per-pair result file from parsed `bundle-output.md`. The DB stores protocol state (`result_kind`, nullable `decision`, `reviewed_at`), not prose. `MANIFEST.json` is reconstructed from DB rows and holds no review body.
- Verdict output ends with one parseable `## Result: PASS|WARN|FAIL|ERROR`; report output ends with `## Result: REPORT`. Finalization parses against the pair's persisted kind and rejects the other class's marker.

### Freshness mechanism

The selector computes SHA-256 over the current note and criterion text and compares it against the accepted snapshot hashes from `current_gate_acceptances`, reconstructing note diffs from accepted snapshot text. Rows with null accepted snapshots report as `missing-review` with the diff unavailable. There is no separate bundle manifest hash; if bundle-level manifests ever become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf criterion-file hash.

The hash boundary is deliberate and narrower than the full assay contract: the prompt scaffolding (`protocol/prompt.py` — runner system prompt, reading scope, output contract, the conformance wrappers) and the prompt-assembling code are outside it, so editing them invalidates no acceptances. The compensating rule is that judgment-bearing criteria live only in hashed note/criterion files, and the scaffolding stays mechanical; a scaffolding change that shifts judgments is a system upgrade calling for a deliberate corpus-wide re-review or ack decision. Both modules carry comments marking this boundary. For conformance pairs specifically, a wrapper may say how to apply a type spec or COLLECTION.md as a criterion, never what a good note of the type or collection looks like — conformance criteria that need sharpening go into an authored `## Review` section of the dependency document, where the hash sees them.

Conformance prompts reference the dependency document — the type spec or the collection's COLLECTION.md — by repo path instead of embedding it; the worker reads it from disk. The document is criteria the reviewer applies, not prompt text addressed to it, and arriving as a read result keeps that distinction evident. The document is still snapshotted at job creation and pinned by acceptance, so freshness is unchanged. The disk read opens a window — a document edited between job creation and the worker's read is judged in its new text while acceptance pins the old snapshot — but a persistent edit self-heals, because the acceptance is immediately `gate-changed` against the changed file; only an edit reverted within the window escapes notice.

The two-input shape is also the growth path: the default answer to a new review dependency is a new factored `(note, dependency)` pair with the dependency document on the gate side — as type-conformance pairs do with type specs ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) and collection-conformance pairs do with COLLECTION.md contracts ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)) — not a wider per-pair input set.

## Core modules

### Selection and gates

- `review_target_selector.py` lists stale or requested applicable `(note, criterion)` pairs. Read-only; its public records retain `gate_*` names.
- `resolve_gates.py` expands bundle names into gate ids and filters gates by note type and traits. It owns the single definition of `--all-gates`: all catalog gates plus virtual `type` and `collection`; the heavyweight report-kind `critique` assay remains opt-in.
- `paths.py` resolves the active gate catalog and translates between gate ids and repo-relative gate paths, including virtual type, collection, and critique identities.
- `type_conformance.py` owns the second gate source ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)): type-conformance pairs whose gate side is the type spec named by the note's `type:` frontmatter. Pairs derive from note frontmatter, not from catalog listing plus `requires_type` filtering; the persisted gate identity is the type-spec repo path, and everything downstream of pair derivation (snapshots, freshness, acceptance, ack, finalization) is unchanged.
- `collection_conformance.py` owns the third gate source ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)): collection-conformance pairs whose gate side is the `COLLECTION.md` of the nearest collection containing the note. Pairs derive from note location; the persisted gate identity is the COLLECTION.md repo path, and everything downstream is the same unchanged machinery.

### Job creation

- `batch.py` creates queued jobs from normalized pair lists. It snapshots note/gate files, inserts job and pair rows, renders prompts, writes `MANIFEST.json`, and returns derived prompt/output/result paths.
- `freshness.py` captures snapshot-backed assay inputs for prompt generation.
- `job_prompt.py` prepares `NoteReviewTarget` objects, including resolved and unresolved local markdown links.
- `artifacts.py` owns artifact directory selection, result-file naming, result frontmatter, per-pair result writes, and manifest writing.

### Protocol and finalization

- `protocol/format.py` defines pair sentinels and render-time reserved-text checks.
- `protocol/prompt.py` renders canonical review prompts from captured text; conformance gates (type spec, COLLECTION.md) are the exception, rendered as a mechanical wrapper referencing the dependency document's repo path for the worker to read. In file-output mode, the prompt instructs a worker to write exactly the job's derived `bundle_output_path`.
- `protocol/parser.py` parses sentinel-bracketed pair output. Structural anomalies, missing expected pairs, duplicates, and malformed result footers fail the whole job.
- `protocol/decisions.py` strictly accepts the one final result marker allowed by the persisted pair kind: a verdict enum or `REPORT`.
- `finalization.py` is the public library operation behind `commonplace-finalize-review-job`. It loads derived job output, validates optional runner/model/effort provenance, parses the bundle, and — only after all parse and coverage preflight passes — writes result files, completes pair rows, upserts acceptance, prunes superseded review rows/snapshots, and marks the job completed. Result-file write failures roll back and fail the job in a separate transaction; artifact-dir cleanup and `MANIFEST.json` refresh run after DB completion, with failures reported as non-fatal warnings.

### State and maintenance

- `review_db.py` owns review rows, finalization state transitions, current acceptance rows, inline superseded-review pruning, and query helpers.
- `review_model.py` normalizes model partitions and optional reasoning-effort labels.
- `acknowledgement.py` advances accepted baselines for trivial changes while carrying forward completed review evidence.
- `ack_trivial_note_changes.py` finds stale pairs whose watched note portions did not change.
- `warn_selector.py` extracts actionable warn findings from effective accepted reviews.
- `review_schema.py` owns current-schema setup and integrity checks.
- Superseded-review pruning runs inline on successful acceptance writes; there is no standalone prune command.

## Command surface

Execution path:

- `commonplace-review-target-selector`
- `commonplace-create-review-jobs`
- `commonplace-finalize-review-job`

State and inspection:

- `commonplace-review-job-list`
- `commonplace-ack-gate-review`
- `commonplace-ack-trivial-note-changes`
- `commonplace-warn-selector`
- `commonplace-resolve-gates`

## Invariants

- Job creation always consumes selector JSON. There is no direct note/pair creation mode.
- Worker agents write only the job-owned bundle output file; they do not mutate notes, criteria, indexes, manifests, or review DB state.
- `MANIFEST.json` is inspectable output, not pipeline state.
- Finalization accepts only `queued` jobs and moves them atomically to `completed` or `failed`.
- Failed jobs write no acceptance rows and reset pair completion state (`decision` and `reviewed_at` null).
- `current_gate_acceptances` requires a completed parent job and per-kind pair completion: decision-bearing verdict or decisionless report.
- A successful acceptance supersedes the prior row for the same `(note_path, gate_path, model_partition)` key and prunes obsolete review evidence inline.
- Acceptance state is path-keyed; relocating notes or criteria requires a fresh assay under the new path.
- Missing telemetry is normal. Review identity is `(note_path, gate_path, model_partition)`, not worker-provided execution metadata.
