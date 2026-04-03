# Review system

The review system stores per-gate review state in a local SQLite database while keeping notes and gate definitions as markdown files in the repo.

This system is experimental and opt-in. It is not part of the default note-writing flow, and reviews should not be treated as always-on checks.

It is also a scoped exception to the repo's file-first design. The motivation for that exception is recorded in [kb/notes/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md](../kb/notes/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md): review state stopped behaving like authored library content and started behaving like local operational state.

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

Schema: `scripts/review-schema.sql`

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

For now, gate freshness is keyed by the raw git blob SHA of the gate file itself. That intentionally excludes shared bundle instructions. If shared bundle instructions later become freshness-relevant, this should widen to an effective review-contract hash rather than a leaf gate-file SHA.

## Write paths

### Full review

The canonical live path is:

1. create a review run
2. write one DB row per gate review
3. finalize the run to append acceptance events

For live agent work, the preferred path is the direct-write helper chain:

1. `scripts/create_review_run.py`
2. `scripts/write_gate_review.py`
3. `scripts/finalize_review_run.py`

`scripts/run_review_bundle.py` remains the shell-automation wrapper. It delegates to a nested runner, records gate reviews through `scripts/write_gate_review.py`, and finalizes acceptance through `scripts/finalize_review_run.py`.

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

> which `(note, gate)` pairs are stale for the active model, and why?

It computes:

- current note sha from git
- current gate sha from gate files
- active model from `COMMONPLACE_REVIEW_MODEL`

It then compares those values against `current_gate_acceptances`.

Prompt-facing CLI remains stable:

- `scripts/review_target_selector.py`
- positional gate IDs and/or bundle names (e.g. `prose`, `semantic/grounding-alignment`)
- `--all-gates` to check all gates
- `--note` to filter to specific note paths
- `--current` to filter to notes with `status: current`
- `scripts/review_sweep.sh --runner {claude-code|codex}` selects the execution runner for note-local bundle runs
- `--json`
- `--reason {missing-review,gate-changed,note-changed}`
- `COMMONPLACE_REVIEW_MODEL` selects the active model partition

### Ack

`scripts/ack_gate_review.py` keeps the same CLI:

- positional `note_path`
- one or more positional `gate_ids`
- output lines of the form `acked: <note_path> <gate_id>`

The storage backend changed from metadata rewrites to append-only DB events.

### Render/export

Human-readable inspection remains required, but it is now a derived view from DB rows rather than canonical state.

## Agent workflow

### Running a review bundle on a note

Instruction: `kb/instructions/run-review-bundle-on-note.md`

1. `uv run scripts/create_review_run.py --runner {codex|claude-code} --json {note} {gate-or-bundle}...`
2. Read the resolved `gates` payload from the JSON output
3. Review the note gate-by-gate in the current agent
4. `python3 scripts/write_gate_review.py --review-run-id {id} --gate-id {gate-id} --input-file {tmp}`
5. `python3 scripts/finalize_review_run.py --review-run-id {id}`

For unattended shell automation, use:

1. `uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note} {gate-or-bundle}...`
2. The wrapper creates the review run, launches a nested runner, records one review body per gate, and finalizes acceptance

### Sweep

Instruction: `kb/instructions/review-sweep.md`

1. `uv run scripts/review_target_selector.py {bundle-or-all} [--current] --json` — get stale pairs with diffs
2. Triage by reason: `missing-review` and `gate-changed` need fresh reviews; `note-changed` needs diff inspection
3. For significant changes: run `scripts/review_sweep.sh` or invoke `scripts/run_review_bundle.py` per note/group
4. `scripts/review_sweep.sh` runs note-local bundle reviews in parallel, up to 4 at a time by default; override with `REVIEW_SWEEP_JOBS=<n>`
5. For insignificant changes: run `uv run scripts/ack_gate_review.py {note-path} {gate-id} ...` to append acceptance events
