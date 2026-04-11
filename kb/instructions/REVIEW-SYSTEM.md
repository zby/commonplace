# Review system

The review system stores per-gate review state in a local SQLite database while keeping notes and gate definitions as markdown files in the repo.

This system is experimental and opt-in. It is not part of the default note-writing flow, and reviews should not be treated as always-on checks.

It is also a scoped exception to the repo's file-first design. The motivation for that exception is recorded in [kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md](../kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md): review state stopped behaving like authored library content and started behaving like local operational state.

## Concepts

**Gate.** A markdown file in `kb/instructions/review-gates/{lens}/{name}.md`. The `{lens}/{name}` path is the gate id (for example `prose/source-residue`).

**Bundle.** A directory of gates sharing a lens. `semantic` means all gate files under `kb/instructions/review-gates/semantic/`.

**Gate review.** One stored result of applying one gate to one note under one model.

**Acceptance event.** An append-only event recording the accepted note sha and gate sha for one `(note_path, gate_id, model_id)` key.

**Current acceptance.** The latest acceptance event for one key. The selector queries this derived state rather than mutable review-file metadata.

**Rendered review.** Optional human-readable markdown reconstructed from DB rows. Rendered markdown is inspectable output, not canonical state.

**Model partition.** Reviews are partitioned by `model_id`. A review or acceptance for one model does not satisfy freshness for another.

## Storage model

Canonical state lives in a local SQLite database at `kb/reports/review-store.sqlite` by default. Set `COMMONPLACE_REVIEW_DB` to override that location.

This DB-backed state is intentional, but still experimental. Notes, gates, instructions, and source material remain file-backed; only review state crosses that boundary today.

Schema: packaged with `commonplace.review`

Primary tables:

- `gate_reviews`
  - append-only review history
  - one row per reviewed `(note, gate, model)` instance
  - stores decision, rationale markdown, explicit `model_id`, reviewed note sha, and gate sha
- `acceptance_events`
  - append-only acceptance history
  - records the accepted baseline for selector and ack
  - latest event wins for the current-state query

Derived view:

- `current_gate_acceptances`
  - current accepted state per `(note_path, gate_id, model_id)`
  - defined as the highest `acceptance_events.id` for that key

### Canonical status vs review prose

The Python layer assigns the canonical DB statuses.

- `gate_reviews.decision` is normalized into lowercase enum values: `pass`, `warn`, `fail`, `error`, `unknown`
- `review_runs.status` is normalized into lowercase enum values: `running`, `completed`, `failed`

The human-readable `rationale_markdown` is not canonical state. It may use different casing or wording inside the review body, for example `## Result: PASS` or `- WARN: ...`. That is acceptable. Treat the DB columns as the source of truth; review-body result lines are parse inputs and readability affordances, not the canonical status layer.

For stored gate review prose, the canonical layout places the parseable `## Result:` line at the end of the review block. The parser still accepts legacy result-first layouts on ingest.

## Freshness and staleness

Selector behavior stays the same at the prompt surface, but acceptance state now comes from `current_gate_acceptances`.

Three artifacts participate:

1. the current note file
2. the current gate file
3. the latest acceptance event for that `(note, gate, model)` key

Rules:

- no acceptance row -> `missing-review`
- accepted gate sha differs from the current gate sha -> `gate-changed`
- accepted note sha differs from the current note sha -> `note-changed`
- otherwise the pair is fresh

For now, gate freshness is keyed by the raw git blob SHA of the gate file itself. There is no separate bundle manifest hash in the current tree. If bundle-level manifests ever return and become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf gate-file SHA.

## Write paths

### Full review

The canonical live path is:

1. create a review run
2. write one DB row per gate review
3. finalize the run to append acceptance events

For live agent work, the preferred path is the direct-write helper chain:

1. `commonplace-create-review-run`
2. `commonplace-write-gate-review`
3. `commonplace-finalize-review-run`

A full review write contributes:

1. one `gate_reviews` row
2. one `acceptance_events` row with `acceptance_kind = 'full-review'`

The important invariant is that the stored `reviewed_note_sha` and `gate_sha` are the exact values used during review generation.

### Trivial-change acknowledgement

`ack` no longer rewrites a markdown file. It appends a new `acceptance_events` row with:

- the current note sha
- the current gate sha
- `acceptance_kind = 'trivial-change-ack'`

This advances the accepted baseline without overwriting review prose or mutating a review artifact.

## Read paths

### Selector

The selector still answers:

> which `(note, gate)` pairs are stale for the requested model partition, and why?

It computes:

- current note sha from git
- current gate sha from gate files
- requested model partition from `--model`

It then compares those values against `current_gate_acceptances`.

Prompt-facing CLI remains stable:

- `commonplace-review-target-selector`
- positional gate IDs and/or bundle names (e.g. `prose`, `semantic/grounding-alignment`)
- `--all-gates` to check all gates
- `--note` to filter to specific note paths or directories
- `--current` to filter to notes with `status: current`
- `--model {model-id}` selects the review model partition to inspect or write
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`

### Ack

`commonplace-ack-gate-review` requires:

- `--model {model-id}`
- positional `note_path`
- one or more positional `gate_ids`
- output lines of the form `acked: <note_path> <gate_id>`

The storage backend changed from metadata rewrites to append-only DB events.

### Render/export

Human-readable inspection remains required, but it is now a derived view from DB rows rather than canonical state.

### Warn/fix queue

`commonplace-warn-selector` exists to build a fixing queue from the current review state.

- It reads current accepted reviews across all models from the DB
- For acceptance rows without an attached review body, it falls back to the latest review row for that accepted `(note_path, gate_id, model_id)` key
- It only considers reviews attached to a `review_run_id`
- It selects actionable findings from reviews whose canonical decision is `warn`
- It collapses model partitions to one current entry per `(note_path, gate_id)`, choosing the latest accepted warn review for that gate

This intentionally excludes legacy imported rows that are not attached to a review run.

## Agent workflow

### Running a review bundle on a note

Instruction: `kb/instructions/run-review-bundle-on-note.md`

1. `commonplace-create-review-run --runner {codex|claude-code} --model {model-id} --json {note} {gate-or-bundle}...`
2. Read the resolved `gates` payload from the JSON output
3. Review the note gate-by-gate in the current agent
4. `commonplace-write-gate-review --review-run-id {id} --gate-id {gate-id} --input-file {tmp}`
5. `commonplace-finalize-review-run --review-run-id {id}`

### Sweep

Instruction: `kb/instructions/review-sweep.md`

1. `commonplace-review-target-selector --model {model-id} {bundle-or-all} [--current|--note kb/notes kb/reference] --json` — get stale pairs with diffs
2. Triage by reason: `missing-review` and `gate-changed` need fresh reviews; `note-changed` needs diff inspection
3. For significant changes: run `commonplace-review-sweep`, run `commonplace-run-gate-sweep`, or use `kb/instructions/run-review-bundle-on-note.md` per note/group
4. `commonplace-review-sweep` runs note-local bundle reviews in parallel, up to 4 at a time by default; override with `REVIEW_SWEEP_JOBS=<n>`
5. For insignificant changes: run `commonplace-ack-gate-review --model {model-id} {note-path} {gate-id} ...` to append acceptance events

### Gate sweep

Use `commonplace-run-gate-sweep {gate-id} --runner {claude-code|codex} --model {model-id} [--current|--note kb/notes kb/reference] [--batch-size N]` when the execution set is one gate across many notes.

This path keeps freshness gate-local and still creates one review run per note, but batches multiple notes into one runner prompt. It is the preferred path when one gate changed and re-reviewing it note-by-note would be needlessly expensive.
