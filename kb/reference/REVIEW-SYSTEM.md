---
description: Runtime workflow, storage model, freshness rules, and command surface for the Commonplace review system
type: kb/types/note.md
tags: []
status: current
---

# Review system

The review system stores per-pair review state in a local SQLite database while keeping notes and gate definitions as markdown files in the repo.

Review freshness is independent of Git. Review creation, full-review acceptance, and trivial ack store DB-owned snapshots of the exact note and gate text that form the accepted baseline. Selectors compare current file text against those snapshot hashes.

This system is experimental and opt-in. It is not part of the default note-writing flow, and reviews should not be treated as always-on checks.

It is also a scoped exception to the repo's file-first design. The motivation for that exception is recorded in [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md): review state stopped behaving like authored library content and started behaving like local operational state.

## Concepts

**Gate.** A markdown file in `kb/instructions/review-gates/{lens}/{name}.md` in a source checkout, or under the installed framework gate catalog in generated projects. The `{lens}/{name}` shorthand is the gate id used at the CLI boundary (for example `prose/source-residue`); persisted freshness state uses the repo-relative gate path.

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Review job.** One review invocation: one rendered prompt, one output artifact directory, and one job-level status. Prepared live-agent jobs are `queued` until a parent claims them for dispatch; subprocess jobs are `running` while the runner executes.

**Review pair.** One requested `(note_path, gate_path)` pair inside a review job. This is the stored unit of review output and acceptance.

**Acceptance event.** An append-only event recording the accepted note and gate snapshot IDs for one `(note_path, gate_path, model_partition)` key.

**Current acceptance.** The latest acceptance event for one key. The selector queries this derived state rather than mutable review-file metadata.

**Rendered review.** Optional human-readable markdown reconstructed from DB rows. Rendered markdown is inspectable output, not canonical state.

**Model partition.** Reviews are partitioned by `model_partition`. A review or acceptance for one model does not satisfy freshness for another.

## Authoring a gate

Gates are typed `kb/types/review-gate.md`. See [that type spec](../types/review-gate.md) for the frontmatter and body contract, and `kb/instructions/review-gates/` for examples. This document covers runtime concepts (bundles, freshness, acceptance, write paths); the type owns the authored shape.

## Storage model

Canonical state lives in a local SQLite database at `kb/reports/review-store.sqlite` by default. Set `COMMONPLACE_REVIEW_DB` to override that location.

This DB-backed state is intentional, but still experimental. Notes, gates, instructions, and source material remain file-backed; only review state crosses that boundary today.

Schema: packaged with `commonplace.review`

Primary tables:

- `review_jobs`
  - one row per review invocation
  - stores runner/model, status, packing (`note` or `gate`), `created_at`, nullable `started_at`, telemetry, and the bundle output path
- `review_file_snapshots`
  - role-neutral snapshots of KB files by `(path, content_sha256)`
  - stores exact UTF-8 text when the snapshot must be reusable for prompt rendering or diffing
- `review_pairs`
  - one row per requested `(note_path, gate_path)` pair inside a job
  - stores pair status (`pending`, `completed`, `missing`), decision, result path, and reviewed note/gate snapshot IDs
  - derives model partition from the parent `review_jobs` row
- `acceptance_events`
  - append-only acceptance history
  - records the accepted baseline for selector and ack
  - new full-review and ack writes point `accepted_review_pair_id` to completed review evidence
  - legacy nullable ack rows remain readable through fallback lookup
  - latest event wins for the current-state query

Derived view:

- `current_gate_acceptances`
  - current accepted state per `(note_path, gate_path, model_partition)`
  - defined as the highest `acceptance_events.acceptance_event_id` for that key

### Canonical status vs review prose

The Python layer assigns the canonical DB statuses.

- `review_pairs.decision` is normalized into lowercase enum values: `pass`, `warn`, `fail`, `error`, `unknown`
- `review_pairs.pair_status` is normalized into lowercase enum values: `pending`, `completed`, `missing`
- `review_jobs.status` is normalized into lowercase enum values: `queued`, `running`, `completed`, `failed`

Job timestamps have distinct meanings: `created_at` is when the job row and prompt inputs were prepared; `started_at` is when an owned subprocess runner started execution or when a parent claimed a live-agent/orchestrator job for dispatch. Finalization still accepts `queued` for manual recovery when output was produced before an explicit claim.

The human-readable review body is not canonical state. Current write paths store it in the per-pair result file named by `review_pairs.result_path`. The DB decision/status columns are the source of truth; review-body result lines such as `## Result: PASS` or `- WARN: ...` are parse inputs and readability affordances.

For stored gate review prose, the canonical layout places the parseable `## Result:` line at the end of the review block.

## Freshness and staleness

Selector behavior stays the same at the prompt surface, but acceptance state now comes from `current_gate_acceptances`.

Three artifacts participate:

1. the current note file
2. the current gate file
3. the latest acceptance event for that `(note_path, gate_path, model_partition)` key

Freshness compares SHA-256 over the current file text against the accepted snapshot hashes and reconstructs note diffs from accepted snapshot text. Rows with null accepted snapshots report as `missing-review` with diff unavailable.

Rules:

- no acceptance row -> `missing-review`
- accepted note or gate snapshot is missing -> `missing-review`
- accepted gate snapshot hash differs from the current gate hash -> `gate-changed`
- accepted note snapshot hash differs from the current note hash -> `note-changed`
- otherwise the pair is fresh

There is no separate bundle manifest hash in the current tree. If bundle-level manifests ever return and become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf gate-file hash.

## Write paths

### Full review

The canonical live path is:

1. create one or more queued review jobs for the requested gates
2. claim each dispatched job with concrete worker provenance
3. write each sentinel-delimited bundle artifact
4. finalize each job by id to complete review pairs and append acceptance events

For live agent work, the preferred path is the prompt-plus-finalize helper chain:

1. `commonplace-create-review-jobs`
2. for each returned job, run `commonplace-claim-review-job --review-job-id {id} --runner {worker} --model {model} [--effort {effort}]`
3. launch a sub-agent that reads the job's `prompt_path` and writes the job's `bundle_output_path`
4. run `commonplace-finalize-review-job --review-job-id {id}` for each completed sub-agent output

The helper groups requested gates by bundle/lens, so a request for multiple bundles creates multiple focused prompt contexts. Each job directory also carries `MANIFEST.json` for display/debug inspection. The manifest is created with pending pairs when the prompt is created and refreshed after finalization with pair statuses and parsed `result_path` files; pipeline commands use database paths, not the manifest, as state.

A full review write contributes:

1. one `review_pairs` row per requested pair
2. `review_jobs.bundle_output_path` pointing to the job bundle artifact
3. `review_pairs.result_path` pointing to each per-pair review artifact
4. one `acceptance_events` row per completed pair; `accepted_review_pair_id` points back to the completed review pair

The important invariant is that the stored note and gate snapshot IDs identify the exact file text used during prompt generation.

### Trivial-change acknowledgement

`ack` no longer rewrites a markdown file. It appends a new `acceptance_events` row with:

- snapshot IDs for the current note and gate text
- `accepted_review_pair_id` pointing to the completed review pair being carried forward

Ack fails when there is no completed review pair for the same `(note_path, gate_path, model_partition)`. This advances the accepted baseline without overwriting review prose or mutating a review artifact.

## Read paths

### Selector

The selector still answers:

> which `(note, gate)` pairs are stale for the requested model partition, and why?

It computes:

- current note content hash from the current note file
- current gate content hash from the current gate file
- requested model partition from `--model`, when model-specific freshness is requested

It then compares those values against `current_gate_acceptances`.

If `--model` is omitted, the selector reports only model-agnostic missing-review coverage: a `(note_path, gate_path)` pair is reported as `missing-review` only when there is no current acceptance for that pair under any model partition. This mode does not classify `gate-changed` or `note-changed`, because those require a chosen accepted baseline.

Prompt-facing CLI remains stable:

- `commonplace-review-target-selector`
- positional gate IDs and/or bundle names (e.g. `prose`, `semantic/grounding-alignment`)
- `--all-gates` to check all gates
- `--note` to filter to specific note paths or directories
- `--current` to filter to notes with `status: current`
- `--model {model-partition}` selects the review model partition to inspect or write; omit it only for model-agnostic missing-review coverage
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`

### Ack

`commonplace-ack-gate-review` requires:

- `--model {model-partition}`
- positional `note_path`
- one or more positional `gate_ids`
- output lines of the form `acked: <note_path> <gate_id>`

The storage backend changed from metadata rewrites to append-only DB events.

### Render/export

Human-readable inspection remains required, but it is now a derived view from DB rows and artifact files rather than canonical DB body state.

### Warn/fix queue

`commonplace-warn-selector` exists to build a fixing queue from the current review state.

- It reads current accepted review pairs across all models from the DB
- For acceptance rows without an attached review pair, it falls back to the latest completed review pair for that accepted `(note_path, gate_path, model_partition)` key
- It loads review text from `review_pairs.result_path`; if the file is missing, rationale text is unavailable
- It skips warn findings whose gate changed since acceptance, using accepted gate snapshot hashes
- It selects actionable findings from reviews whose canonical decision is `warn`
- It collapses model partitions to one current entry per `(note_path, gate_path)`, choosing the latest accepted warn review for that gate

## Agent workflow

### Running review batches on a note

Instruction: `kb/instructions/run-review-batches-on-note.md`

1. `commonplace-create-review-jobs --model {model-partition} --note {note} {gate-or-bundle}... --grouping note`
2. For each dispatched item in the returned `jobs` array, run `commonplace-claim-review-job --review-job-id {id} --runner {worker} --model {model} [--effort {effort}]`
3. Launch a sub-agent with that job's `prompt_path` and `bundle_output_path`
4. Each sub-agent writes that job's sentinel-delimited review bundle to `bundle_output_path`
5. The parent finalizes each completed output with `commonplace-finalize-review-job --review-job-id {id}`

### Sweep

Instruction: `kb/instructions/review-sweep.md`

1. `commonplace-review-target-selector --model {model-partition} {bundle-or-all} [--current|--note kb/notes kb/reference] --json` — get stale pairs with diffs
2. Triage by reason: `missing-review` and `gate-changed` need fresh reviews; `note-changed` needs diff inspection
3. For significant changes: run `commonplace-review-sweep`, run `commonplace-run-gate-sweep`, or use `kb/instructions/run-review-batches-on-note.md` per note/group
4. `commonplace-review-sweep` executes note-local bundle reviews in parallel, up to 4 at a time by default; override with `REVIEW_SWEEP_JOBS=<n>`
5. For insignificant changes: run `commonplace-ack-gate-review --model {model-partition} {note-path} {gate-id} ...` to append acceptance events

### Gate sweep

Use `commonplace-run-gate-sweep {gate-id} --runner {claude-code|codex} --model {model-partition} [--current|--note kb/notes kb/reference] [--batch-size N]` when the execution set is one gate across many notes.

This path keeps freshness gate-local and creates one running gate-packed review job per prompt batch. It is the preferred path when one gate changed and re-reviewing it note-by-note would be needlessly expensive.
