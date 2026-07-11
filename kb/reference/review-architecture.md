---
description: "Code architecture of the Commonplace review subsystem: package layout, storage schema, canonical state vs derived output, freshness mechanism, module map, and finalization invariants"
type: kb/types/note.md
tags: []
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review subsystem stores assay state in SQLite, renders canonical prompt artifacts for `(note, criterion)` pairs, and finalizes worker-written output. The persisted criterion field remains named `criterion_path`. It does not launch reviewer models itself: the parent agent or harness owns worker dispatch, while Commonplace owns deterministic selection, job creation, finalization, freshness, and maintenance.

This document describes how the subsystem is built. For how to operate it, see [review system](./README-REVIEW-SYSTEM.md) and [run review batches](../instructions/run-review-batches.md).

## Package layout

- `commonplace.review` — library modules: SQLite access, freshness, gate resolution, prompt preparation, output parsing/finalization, artifact writing, acknowledgement, warning selection, and maintenance helpers.
- `commonplace.cli.review` — thin command wrappers. Each command parses arguments, resolves the repo root and review DB, then calls one library operation.

## Execution flow

```
review_target_selector  -> selector JSON
create_review_jobs      -> queued review_jobs + review_pairs + prompt artifacts
worker/sub-agent        -> writes derived job_output_path
finalize_review_job     -> validate provenance, parse output, record completion, upsert freshness baseline
```

The persisted unit is a `review_pairs` row inside one `review_jobs` row. A job's `grouping` is either `note` or `criterion`; grouping controls prompt sharing and result filenames. Every job is result-kind homogeneous.

## Data model

SQLite database, default location `kb/reports/review-store.sqlite`; override with `COMMONPLACE_REVIEW_DB` or a command-specific `--db`. `review_schema.py` owns current-schema setup and integrity checks. Unsupported schema versions are refused; the retained v5 store has an explicit direct v5→v7 preservation script.

| Table | Contents |
|---|---|
| `review_jobs` | One review invocation: model partition, nullable runner/model/effort provenance, status, grouping (`note`/`criterion`), `created_at`, nullable `completed_at`, telemetry, failure context |
| `review_pairs` | One requested `(note_path, criterion_path)` pair inside a job: persisted `result_kind` (`verdict`/`report`), nullable outcome, and reviewed note/criterion snapshot IDs; derives `model_partition` from its parent job |
| `review_file_snapshots` | Role-neutral snapshots by `(path, content_sha256)`, storing exact UTF-8 text when it must be reusable for prompt rendering or diffing |
| `freshness_baselines` | Current freshness baseline per `(note_path, criterion_path, model_partition)`; `evidence_review_pair_id` points at completed evidence and baseline snapshot IDs pin note/criterion text |

Artifact paths — prompt, job output, manifest, and per-pair result files — are **derived**, not stored columns. Each per-pair result filename (`pair-{ordinal}-{stem}.md`) is a pure function of that pair's own row (`pair_ordinal` plus the grouping-varying path stem), never of sibling pairs, so inline pruning of superseded sibling pairs cannot change a surviving pair's path.

The `current_freshness_baselines` view enriches each current row with evidence-pair result data and baseline snapshot hashes/text. A baseline is valid only when its evidence pair, parent job, paths, model partition, snapshots, and per-kind completion agree. `review_schema.py` checks those invariants at initialization, and baseline query helpers repeat the check rather than hiding malformed rows as stale state.

### Canonical state vs derived output

The DB is the source of truth; human-readable markdown is derived.

- `review_pairs.result_kind` is `verdict` or `report`. Verdict outcomes use the lowercase enum `pass`, `warn`, `fail`; report pairs keep `outcome` null. `review_jobs.status` is `queued`, `completed`, or `failed`.
- `created_at` is when the job row and prompt inputs were prepared. Runner provenance is optional and recorded during finalization.
- The review **body** is not in the DB. The finalizer writes it to the derived per-pair result file from parsed `job-output.md`. The DB stores protocol state (`result_kind`, nullable `outcome`, `completed_at`), not prose. `MANIFEST.json` is reconstructed from DB rows and holds no review body.
- Verdict output ends with one parseable `## Result: PASS|WARN|FAIL`; report output ends with `## Result: REPORT`. `ERROR` is an execution-failure signal: finalization fails the whole job without completing pairs or advancing baselines.

### Freshness mechanism

The selector computes SHA-256 over the current note and criterion text and compares it against baseline snapshot hashes from `current_freshness_baselines`, reconstructing note diffs from baseline snapshot text. No row produces `missing-baseline`; a present row with missing or inconsistent data raises an integrity error. There is no separate catalog-bundle manifest hash; if bundle-level manifests ever become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf criterion-file hash.

The hash boundary is deliberate and narrower than the full assay contract: the prompt scaffolding (`protocol/prompt.py` — runner system prompt, reading scope, output contract, the conformance wrappers) and the prompt-assembling code are outside it, so editing them invalidates no freshness baselines. The compensating rule is that judgment-bearing criteria live only in hashed note/criterion files, and the scaffolding stays mechanical; a scaffolding change that shifts judgments is a system upgrade calling for a deliberate corpus-wide re-review or ack outcome. Both modules carry comments marking this boundary. For conformance pairs specifically, a wrapper may say how to apply a type spec or COLLECTION.md as a criterion, never what a good note of the type or collection looks like — conformance criteria that need sharpening go into an authored `## Review` section of the dependency document, where the hash sees them.

Conformance prompts embed the dependency document snapshot — the type spec or the collection's COLLECTION.md — captured at job creation. A short mechanical wrapper distinguishes the document as criteria the reviewer applies rather than prompt text addressed to it. The evaluated text and the snapshot pinned by the freshness baseline are therefore identical.

The two-input shape is also the growth path: the default answer to a new review dependency is a new factored `(note, dependency)` pair with the dependency document on the criterion side — as type-conformance pairs do with type specs ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) and collection-conformance pairs do with COLLECTION.md contracts ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)) — not a wider per-pair input set.

## Core modules

### Selection and criteria

- `review_target_selector.py` lists stale or requested applicable `(note, criterion)` pairs. Read-only; its public records use `criterion_*` names.
- `resolve_criteria.py` expands requests into criterion ids and filters catalog gates by note type and traits. It owns the single definition of `--all-gates`: all catalog gates plus virtual `type` and `collection`; the heavyweight report-kind `critique` assay remains opt-in.
- `paths.py` resolves the active gate catalog and translates between criterion ids and repo-relative criterion paths, including virtual type, collection, and critique identities.
- `type_conformance.py` owns the type-conformance criterion source ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)): the type spec named by the note's `type:` frontmatter. Pairs derive from note frontmatter, not from catalog listing plus `requires_type` filtering; the persisted criterion identity is the type-spec repo path, and everything downstream of pair derivation is unchanged.
- `collection_conformance.py` owns the collection-conformance criterion source ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)): the `COLLECTION.md` of the nearest collection containing the note. Pairs derive from note location; the persisted criterion identity is the COLLECTION.md repo path, and everything downstream is unchanged.

### Job creation

- `batch.py` creates queued jobs from normalized pair lists. It snapshots note/criterion files, inserts job and pair rows, renders prompts, writes `MANIFEST.json`, and returns derived prompt/output/result paths.
- `freshness.py` captures snapshot-backed assay inputs for prompt generation.
- `job_prompt.py` prepares `NoteReviewTarget` objects, including resolved and unresolved local markdown links.
- `artifacts.py` owns artifact directory selection, result-file naming, result frontmatter, per-pair result writes, and manifest writing.

### Protocol and finalization

- `protocol/format.py` defines pair sentinels and render-time reserved-text checks.
- `protocol/prompt.py` renders canonical review prompts from captured text; conformance gates add a mechanical wrapper explaining how to apply the embedded type spec or COLLECTION.md snapshot. In file-output mode, the prompt instructs a worker to write exactly the job's derived `job_output_path`.
- `protocol/parser.py` parses sentinel-bracketed pair output. Structural anomalies, missing expected pairs, duplicates, and malformed result footers fail the whole job.
- `protocol/outcomes.py` strictly accepts the one final result marker allowed by the persisted pair kind: a verdict outcome or `REPORT`; `ERROR` raises a job-failing parse error.
- `finalization.py` is the public library operation behind `commonplace-finalize-review-job`. It loads derived job output, validates optional runner/model/effort provenance, parses the job output, and — only after all parse and coverage preflight passes — writes result files, completes pair rows, creates or replaces freshness baselines, prunes superseded review rows/snapshots, and marks the job completed. Result-file write failures roll back and fail the job in a separate transaction; artifact-dir cleanup and `MANIFEST.json` refresh run after DB completion, with failures reported as non-fatal warnings.

### State and maintenance

- `review_db.py` owns review rows, finalization state transitions, current freshness baseline rows, inline superseded-review pruning, and query helpers.
- `review_model.py` normalizes model partitions and optional reasoning-effort labels.
- `acknowledgement.py` advances existing baselines for trivial changes while preserving their evidence-pair identity.
- `ack_trivial_note_changes.py` finds stale pairs whose watched note portions did not change.
- `warn_selector.py` extracts actionable warn findings from current baseline evidence.
- `review_schema.py` owns current-schema setup and integrity checks.
- Superseded-review pruning runs inline on successful freshness baseline writes; there is no standalone prune command.

## Command surface

Execution path:

- `commonplace-review-target-selector`
- `commonplace-create-review-jobs`
- `commonplace-finalize-review-job`

State and inspection:

- `commonplace-review-job-list`
- `commonplace-ack-review`
- `commonplace-ack-trivial-note-changes`
- `commonplace-warn-selector`
- `commonplace-resolve-criteria`

## Invariants

- Job creation always consumes selector JSON. There is no direct note/pair creation mode.
- Worker agents write only the job-owned job output file; they do not mutate notes, criteria, indexes, manifests, or review DB state.
- `MANIFEST.json` is inspectable output, not pipeline state.
- Finalization accepts only `queued` jobs and moves them atomically to `completed` or `failed`.
- Failed jobs write no freshness baseline rows and reset pair completion state (`outcome` and `completed_at` null).
- `current_freshness_baselines` requires a completed parent job and per-kind pair completion: outcome-bearing verdict or decisionless report.
- A successful freshness baseline supersedes the prior row for the same `(note_path, criterion_path, model_partition)` key and prunes obsolete review evidence inline.
- Freshness baseline state is path-keyed; relocating notes or criteria requires a fresh assay under the new path.
- Missing telemetry is normal. Review identity is `(note_path, criterion_path, model_partition)`, not worker-provided execution metadata.
