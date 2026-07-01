---
description: Runtime workflow, storage model, freshness rules, and command surface for the Commonplace review system
type: kb/types/note.md
tags: []
status: current
---

# Review system

The review system runs gate-based quality reviews of KB notes and records their outcomes. A single review checks one note against one *gate* — a review lens such as `prose/source-residue` — and produces a decision (`pass`, `warn`, `fail`, or `error`) together with a written rationale. The notes and gates being reviewed stay as markdown files in the repo; the review state produced about them lives in a local SQLite database.

Two properties shape everything else:

- **Freshness is independent of Git.** Review creation, full-review acceptance, and trivial acknowledgement each store DB-owned snapshots of the exact note and gate text that form the accepted baseline. Selectors decide staleness by comparing current file text against those snapshot hashes, not by inspecting Git history.
- **It is experimental and opt-in.** Reviewing is not part of the default note-writing flow, and reviews are not always-on checks. You invoke the system deliberately when you want a note judged.

Storing review state in SQLite is a scoped exception to the repo's file-first design. [ADR-010](./adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) records the motivation: review state stopped behaving like authored library content and started behaving like local operational state. Notes, gates, instructions, and source material remain file-backed; only review state crosses that boundary.

## How a review flows

A full review runs as a short pipeline, from a stale-pair query to a durable acceptance:

1. **Select** — the selector lists `(note, gate)` pairs that are stale or unreviewed for a given model partition, and says why.
2. **Create jobs** — selected pairs are packed into one or more queued *review jobs*, each with its own rendered prompt.
3. **Review** — a worker (typically a sub-agent) reads a job's prompt and writes a single sentinel-delimited `bundle-output.md`.
4. **Finalize** — the parent parses that output and, only if every expected pair is present and well-formed, records the decisions and appends acceptance events. Finalization is all-or-nothing.

Acceptance is the durable outcome. An acceptance event pins the exact note and gate text that was reviewed, so the selector can later tell whether either side has drifted. When a note changes only trivially, an existing acceptance can be carried forward without a fresh review (*ack*).

## Concepts

**Gate.** A markdown file at `kb/instructions/review-gates/{lens}/{name}.md` in a source checkout, or under the installed framework gate catalog in generated projects. The `{lens}/{name}` shorthand is the gate id used at the CLI boundary (for example `prose/source-residue`); persisted freshness state uses the repo-relative gate path.

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Review job.** One review invocation: one rendered prompt, one output artifact directory, and one job-level status. A job is `queued` until finalization marks it `completed` or `failed`.

**Review pair.** One requested `(note_path, gate_path)` pair inside a review job. This is the stored unit of review output and acceptance.

**Acceptance event.** An append-only event recording the accepted note and gate snapshot IDs for one `(note_path, gate_path, model_partition)` key.

**Current acceptance.** The latest acceptance event for one key. The selector reads staleness from this derived state.

**Model partition.** Reviews are partitioned by `model_partition`. A review or acceptance for one model does not satisfy freshness for another.

**Derived review output.** Human-readable artifacts that are inspectable output, not canonical state — the DB `decision` and job-status columns are the source of truth. There are two kinds, distinguished by provenance:

- **Per-pair result files** carry the reviewer's prose. The finalizer writes them from the parsed `bundle-output.md`, not from the DB — the DB stores the pair `decision`, never the review body.
- **`MANIFEST.json`** is reconstructed from DB rows (job/pair statuses, derived paths, decisions) and holds no prose.

Only the manifest is reproducible from the DB alone; a lost result file would need the original bundle output to rewrite.

## Storage model

Canonical state lives in a local SQLite database at `kb/reports/review-store.sqlite` by default; set `COMMONPLACE_REVIEW_DB` to override the location. The schema is packaged with `commonplace.review`.

Primary tables:

- `review_jobs`
  - one row per review invocation
  - stores runner/model, status, packing (`note` or `gate`), `created_at`, nullable `completed_at`, telemetry, and failure context
  - prompt, bundle-output, manifest, and result artifact paths are derived from `review_job_id`, packing, and the job's pairs — they are not stored
- `review_file_snapshots`
  - role-neutral snapshots of KB files by `(path, content_sha256)`
  - stores exact UTF-8 text when the snapshot must be reusable for prompt rendering or diffing
- `review_pairs`
  - one row per requested `(note_path, gate_path)` pair inside a job
  - stores the decision and the reviewed note/gate snapshot IDs
  - derives its model partition from the parent `review_jobs` row
- `acceptance_events`
  - append-only acceptance history
  - records the accepted baseline for selector and ack
  - full-review and ack writes point `accepted_review_pair_id` at completed review evidence
  - the latest event wins for the current-state query

Derived view:

- `current_gate_acceptances`
  - current accepted state per `(note_path, gate_path, model_partition)`
  - defined as the highest `acceptance_events.acceptance_event_id` for that key, after filtering to completed jobs with non-null pair decisions

### Canonical status vs review prose

The Python layer assigns the canonical DB statuses:

- `review_pairs.decision` is a lowercase enum: `pass`, `warn`, `fail`, `error`
- `review_jobs.status` is a lowercase enum: `queued`, `completed`, `failed`

`created_at` is when the job row and prompt inputs were prepared. Runner provenance is optional and is recorded during finalization.

The human-readable review body is not canonical state. It is stored in the per-pair result file at the job-and-pair derived result path. The DB decision and job-status columns are the source of truth; review-body result lines such as `## Result: PASS` are parse inputs and readability affordances.

Stored gate review prose places exactly one parseable `## Result: PASS|WARN|FAIL|ERROR` line at the end of each review block. Aliases such as `Verdict`, `Outcome`, `INFO`, `OK`, and `UNKNOWN` are invalid in live finalization output.

## Freshness and staleness

The selector reads acceptance state from `current_gate_acceptances`. Three artifacts participate in a freshness decision:

1. the current note file
2. the current gate file
3. the latest acceptance event for that `(note_path, gate_path, model_partition)` key

Freshness compares SHA-256 over the current file text against the accepted snapshot hashes, and reconstructs note diffs from accepted snapshot text. Rows with null accepted snapshots report as `missing-review` with the diff unavailable.

Rules:

- no acceptance row → `missing-review`
- accepted note or gate snapshot is missing → `missing-review`
- accepted gate snapshot hash differs from the current gate hash → `gate-changed`
- accepted note snapshot hash differs from the current note hash → `note-changed`
- otherwise the pair is fresh

There is no separate bundle manifest hash. If bundle-level manifests ever become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf gate-file hash.

## Write paths

### Full review

A full review turns queued jobs into accepted evidence:

1. create one or more queued review jobs for the requested gates
2. dispatch each job to a worker that writes the sentinel-delimited bundle artifact
3. finalize each job by id, optionally recording concrete worker provenance

Jobs group requested gates by bundle/lens, so a request spanning multiple bundles produces multiple focused prompt contexts. Each job directory also carries `MANIFEST.json` for display/debug inspection: it is created with pending display states when the prompt is prepared and refreshed after finalization with job-derived pair display states and derived result paths. Pipeline commands use derived job paths, not the manifest, as state.

A successful full review contributes:

1. one `review_pairs` row per requested pair
2. a derived job bundle artifact at `kb/reports/bundle-reviews/review-job-{review_job_id}/bundle-output.md`
3. derived per-pair review artifacts under the same job directory
4. one `acceptance_events` row per pair, only when the whole job finalizes successfully; `accepted_review_pair_id` points back to the completed review pair

Finalization is all-or-nothing. Missing, duplicate, unexpected, malformed, or result-less pair blocks fail the job and append no acceptance events. Result-file write failures are fatal evidence failures; `MANIFEST.json` refresh failures after DB completion are non-fatal warnings in the finalize JSON payload.

The key invariant: the stored note and gate snapshot IDs identify the exact file text used during prompt generation.

For the concrete command sequence, see [Agent workflow](#agent-workflow).

### Trivial-change acknowledgement

Ack advances the accepted baseline without overwriting review prose or mutating a review artifact. It appends a new `acceptance_events` row with:

- snapshot IDs for the current note and gate text
- `accepted_review_pair_id` pointing to the completed review pair being carried forward

Ack fails when there is no completed review pair for the same `(note_path, gate_path, model_partition)` — there must be existing review evidence to carry forward.

## Read paths

### Selector

The selector answers:

> which `(note, gate)` pairs are stale for the requested model partition, and why?

It computes:

- the current note content hash from the current note file
- the current gate content hash from the current gate file
- the requested model partition from `--model`, when model-specific freshness is requested

It then compares those values against `current_gate_acceptances`.

If `--model` is omitted, the selector reports only model-agnostic missing-review coverage: a `(note_path, gate_path)` pair is reported as `missing-review` only when there is no current acceptance for that pair under any model partition. This mode does not classify `gate-changed` or `note-changed`, because those require a chosen accepted baseline.

The selector CLI:

- `commonplace-review-target-selector`
- positional gate ids and/or bundle names (e.g. `prose`, `semantic/grounding-alignment`)
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

### Render/export

Human-readable review output is a derived view, never canonical state: per-pair result files written at finalization, plus `MANIFEST.json` reconstructed from DB rows. See **Derived review output** under [Concepts](#concepts). Use it for inspection; read canonical state from the DB.

### Warn/fix queue

`commonplace-warn-selector` builds a fixing queue from the current review state:

- it reads current accepted review pairs across all models from the DB
- for acceptance rows without an attached review pair, it falls back to the latest completed review pair for that accepted `(note_path, gate_path, model_partition)` key
- it loads review text from the accepted pair's derived result path; if the file is missing, the rationale text is unavailable
- it skips warn findings whose gate changed since acceptance, using accepted gate snapshot hashes
- it selects actionable findings from reviews whose canonical decision is `warn`
- it collapses model partitions to one current entry per `(note_path, gate_path)`, choosing the latest accepted warn review for that gate

## Agent workflow

### Running review batches

Instruction: `kb/instructions/run-review-batches.md`

1. `commonplace-review-target-selector ... --json | commonplace-create-review-jobs --input - --grouping {note|gate}`
2. launch a sub-agent with that job's derived `prompt_path` and `bundle_output_path`
3. each sub-agent writes that job's sentinel-delimited review bundle to `bundle_output_path`
4. the parent finalizes each completed output with `commonplace-finalize-review-job --review-job-id {id} [--runner {worker}] [--model {model} [--effort {effort}]]`

Finalization-time provenance is optional. When supplied, `--model` (with optional `--effort`) is validated with `build_model_partition` against the job's `model_partition` before any state changes, and `--runner`, `--model`, and `--effort` are recorded during finalization. `--effort` requires `--model`.

### Stale review

Use the same `run-review-batches.md` procedure. Select stale pairs with `commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json`, create jobs from that selector JSON, and choose `--grouping note` or `--grouping gate` according to the intended prompt shape.

For `note-changed` pairs, inspect the selector diff first. If the change is insignificant for the gate, run `commonplace-ack-gate-review --model {model-partition} {note-path} {gate-id} ...` instead of creating a fresh review job.

## Authoring a gate

Gates are typed `kb/types/review-gate.md`. See [that type spec](../types/review-gate.md) for the frontmatter and body contract, and `kb/instructions/review-gates/` for examples. This document covers runtime concepts (bundles, freshness, acceptance, write paths); the type owns the authored shape.
