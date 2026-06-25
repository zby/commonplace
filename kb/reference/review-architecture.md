---
description: Code architecture for commonplace.review and commonplace.cli.review - package layout, data model, the (note, gate)-pair protocol and batch executor, packing callers, targeting, and repair utilities
type: kb/types/note.md
tags: []
status: current
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review system runs LLM-based quality reviews against KB notes using defined review gates. It tracks provenance (note and gate versions), manages acceptance state, and detects staleness.

For the review workflow and gate definitions, see [REVIEW-SYSTEM.md](./REVIEW-SYSTEM.md). This document covers the code architecture.

> **Sweep commands are experimental.** `review_sweep`, `run_gate_sweep`, and `ack_trivial_note_changes` are not yet stabilized and are intentionally not documented in detail here. Treat their interfaces as subject to change.

## Package layout

The review subsystem is split between two packages, mirroring the project-wide `commonplace.cli` ↔ `commonplace.lib` split:

- **`commonplace.review`** — library code only. Pure functions, dataclasses, the SQLite layer, the runner subprocess wrappers. No `main()` functions, no argparse, no `Path.cwd()` at import time. Importable from any caller without pulling in CLI machinery.
- **`commonplace.cli.review`** — thin CLI wrappers. Each module is argparse + `Path.cwd()` + `prepare_review_db(...)` + one library call. The `commonplace-*` review entry points in `pyproject.toml` all live here.

For most modules the lib name and the CLI name match. For example `commonplace.review.run_review_bundle` is the library that resolves the target and hands one share-note batch to `executor.execute_batch`; `commonplace.cli.review.run_review_bundle` is the thin wrapper that argparse-parses the user's invocation and calls into the lib. Two modules (`resolve_gates` and `review_target_selector`) exist in both packages because they were split during the layout migration: lib helpers stayed in `commonplace.review.*`, the CLI `main()` moved to `commonplace.cli.review.*`.

This document refers to modules by their unqualified names (e.g. `run_review_bundle`, `review_target_selector`) when the distinction doesn't matter. When a particular function or class is called out, it lives in the library package unless explicitly noted as a CLI.

## Architecture overview

```
┌─────────────────────────────────────────────────┐
│  Packing (which pairs share one LLM call)       │
│  run_review_bundle (share-note)                 │
│  run_gate_sweep (share-gate, experimental)      │
│  batch + create/finalize/ingest (external       │
│  executors: live agent, orchestrator)           │
├─────────────────────────────────────────────────┤
│  Pair protocol & execution                      │
│  protocol/ (format, prompt, parser, decisions)  │
│  executor           runners/ (adapter registry) │
├─────────────────────────────────────────────────┤
│  Gate resolution & targeting                    │
│  resolve_gates      review_target_selector      │
│  warn_selector                                  │
├─────────────────────────────────────────────────┤
│  Data model                                     │
│  review_db          review_model                │
│  review_metadata    review-schema.sql           │
│  paths                                          │
└─────────────────────────────────────────────────┘
```

The unit of review execution is one **(note, gate) pair**; how many pairs ride in one LLM call is a packing choice made by the top layer, not a protocol difference ([ADR 029](./adr/029-review-execution-unified-on-note-gate-pairs.md)). Sweep-related modules (`review_sweep`, `run_gate_sweep`, `ack_trivial_note_changes`) are experimental — see the note above.

---

## Data model

### Database schema (`review-schema.sql`)

SQLite database, default location `kb/reports/review-store.sqlite` (override with `COMMONPLACE_REVIEW_DB` env var).

**Core tables:**

| Table | Purpose | Key columns |
|---|---|---|
| `review_runs` | Review invocations | review_run_id, model_partition, runner, status (running/completed/failed), packing, telemetry_json, bundle_output_path |
| `review_file_snapshots` | Role-neutral file snapshots for review inputs | snapshot_id, path, content_sha256, content_text |
| `review_pairs` | Requested and completed pair outcomes | review_pair_id, review_run_id, note_path, gate_path, pair_status, decision, snapshot IDs |
| `acceptance_events` | Append-only acceptance log | acceptance_event_id, note_path, gate_path, model_partition, accepted_review_pair_id, snapshot IDs |

**Key views:**

- `current_gate_acceptances` — latest acceptance for each `(note_path, gate_path, model_partition)` triple
- `stale_gate_pairs` — current acceptance states for staleness detection

**Acceptance kinds:** `full-review`, `gate-migration`, `trivial-change-ack`, `migration-import`, `manual-override`

### review_model.py

Encode and normalize model identifiers with reasoning effort levels.

- `encode_model(model) -> str` — sanitize model names (lowercase, special chars → hyphens)
- `normalize_model_partition(model_partition) -> str` — collapse known aliases such as `opus-4-6` into canonical review partitions
- `normalize_reasoning_effort(raw) -> str | None` — validate from {low, medium, high, xhigh}
- `build_model_partition(model, reasoning_effort) -> str` — canonical ID like `"claude-3-5-sonnet-xhigh"`

### review_metadata.py

Legacy review-file metadata block helpers and historical Git utility functions. New review freshness does not use Git provenance; accepted baselines live in `review_file_snapshots`.

**Metadata blocks:**
- `parse_review_metadata(review_text) -> ReviewMetadata | None` — extract `<!-- REVIEW-METADATA ... -->` blocks
- `render_review_metadata(metadata) -> str` — generate metadata block
- `inject_review_metadata(review_text, metadata) -> str` — insert/update metadata block

### paths.py

Filesystem path constants and gate identity helpers used across the review subsystem. It resolves the active gate catalog (`kb/instructions/review-gates` in source checkouts, installed framework gates in generated projects), converts human-facing gate ids such as `prose/source-residue` into repo-relative `gate_path` values, and derives display shorthands from stored paths. Lives in its own module so the data layer (`review_db.py`) does not have to own filesystem constants about gate locations.

### review_db.py

Database operations, decision parsing, and record management. The largest module in the package.

**Connection & setup:**
- `connect(db_path) -> Connection` — open with Row factory
- `resolve_db_path(repo_root, db_override=None) -> Path` — resolve DB location, honoring an optional `--db` override
- `ensure_db(repo_root, db_path)` — initialize from schema if needed
- `prepare_review_db(repo_root, db_override=None) -> Path` — convenience helper that resolves and ensures in one call; collapses the four-step bootstrap that every CLI used to open-code
- `snapshot_file(conn, repo_root, path)` — capture or rehydrate the exact UTF-8 file text for a repo-relative note or gate path, keyed by `(path, content_sha256)`

**Note relocation helpers** (called by `commonplace.lib.relocation`):
- `count_note_path_records(conn, *, note_path) -> NotePathUpdateCounts` — how many `review_pairs`/`acceptance_events` rows reference a note path
- `rekey_note_path(conn, *, old_note_path, new_note_path) -> NotePathUpdateCounts` — update those rows in place when a note moves

**CRUD operations:**
- `create_run(conn, ...) -> int` — create a run invocation, return ID
- `create_review_pairs(conn, ...) -> list[int]` — insert requested pair rows
- `create_run_with_pairs(conn, ...) -> int` — create a run and its requested pair set
- `complete_review_pairs(conn, ...) -> list[int]` — record pair outcomes parsed from output
- `mark_missing_pairs(conn, ...) -> int` — mark requested pairs without output
- `append_acceptance_event(conn, ...) -> int` — record acceptance
- `complete_review_run(conn, ...) / fail_review_run(conn, ...)` — finalize run status
- `load_review_run / load_review_pairs_for_run / load_review_pairs_for_note` — query helpers
- `load_effective_review_pair_map(conn, ...) -> dict` — accepted-or-latest completed review pairs per gate
- `load_current_acceptances(conn) -> dict` — current acceptance state map

**Lifecycle helpers:**
- `attach_execution_data(conn, ...)` — persist telemetry, raw bundle markdown, and debug log
- `record_and_finalize_run(conn, ...) -> int` — complete parsed pairs, validate coverage, complete or fail the run, and append acceptance events for completed pairs

**Decision parsing (`parse_review_decision`):**

Multi-strategy fallback chain for extracting decisions from review markdown:

1. Explicit flagging phrases ("flagging as fail")
2. Revised-result headers
3. Standard result headers (`## Result: PASS`)
4. Finding severity patterns
5. Bold decision patterns
6. Legacy format detection
7. Falls back to `"unknown"`

---

## Core operations

### Review execution flow

```
1. resolve_gates     → expand bundle names to gate IDs, filter by note type and traits, then normalize selected gates to paths before persistence
2. freshness.capture_review_inputs → snapshot note/gate files, produce prompt text and `ReviewPairRequest`s with snapshot IDs
3. create_run_with_pairs → insert review_run + review_pairs (status=running), one run per prompt invocation
4. executor.execute_batch
   a. protocol/prompt.render_pairs_prompt → one prompt embedding each note and gate text once
   b. review_runners.run_prompt           → invoke claude-code or codex CLI
   c. protocol/parser.parse_pair_bundle   → extract pair blocks, canonicalize result footers
   d. per run: complete parsed pairs, mark missing pairs, complete or fail the run
5. record_and_finalize_run → write review_pairs, copy pair snapshot IDs to acceptance events, validate coverage, mark run completed or failed
```

### Pair protocol (`protocol/`) and executor

Every output block is keyed by the full (note, gate) pair:

```
=== PAIR REVIEW START: {note_path} :: {gate_path} ===
### Summary
<prose>

### Findings
- <severity>: <finding>

### Suggested Revision
<optional>

## Result: PASS|WARN|FAIL|ERROR
=== PAIR REVIEW END: {note_path} :: {gate_path} ===
```

- `protocol/format.py` — sentinel grammar and the ` :: ` pair-key separator. Render-time validation rejects the separator inside note paths or gate paths and reserved `=== … ===` lines inside embedded note/gate text.
- `protocol/prompt.py` — `render_pairs_prompt(notes, gate_texts, output_mode)` over `NoteReviewTarget`s. Note contents are always embedded from captured target text; the multi-note shape adds the evaluate-independently rule; `output_mode="file"` swaps the destination bullets for the live-agent path.
- `protocol/parser.py` — `parse_pair_bundle` raises on structural anomalies (nested/mismatched/unterminated/unexpected/duplicate/empty blocks) but reports missing expected pairs in `missing` instead of raising, so callers salvage the pairs that parsed.
- `protocol/decisions.py` — decision-line parsing and footer canonicalization; grammar-independent, also used for historical rows.
- `artifacts.py` — shared artifact naming and manifest writing. It is the only place that maps packing to parsed result filenames: note-packed runs use gate filenames, gate-packed runs use note filenames, and mixed fallback uses note-plus-gate filenames.
- `executor.py` — `execute_batch(targets, gate_texts, …)` owns the shared lifecycle: render, one runner call, telemetry/model-mismatch handling, usage-exhaustion (`UsageExhausted`) and interrupt handling, parse, then per-run finalize or fail. Each run writes `bundle-output.md`, writes per-pair result files, writes `debug.log` when runner diagnostics exist, and stores `review_runs.bundle_output_path` plus `review_pairs.result_path` in the DB.

### Packing callers

- **`run_review_bundle.py` — share-note packing.** One note, all its gates, one call, one run.
- **`run_gate_sweep.py` — share-gate packing (experimental).** One gate over a chunked note list; one gate-packed run per prompt batch; missing pairs are marked `missing`, parsed pairs are retained, and the invocation records a failure.
- **Live-agent path (single note)** — same protocol without a nested runner:
  1. `commonplace-create-review-run --with-prompt` creates the run, writes the canonical prompt to `kb/reports/bundle-reviews/review-run-{id}/prompt.md`, writes `MANIFEST.json`, and returns `prompt_path`, `bundle_output_path`, and `manifest_path` in the JSON payload
  2. the prompt is rendered from the snapshots attached to the created pair rows
  3. the current agent reads `prompt_path`, follows it, and writes `kb/reports/bundle-reviews/review-run-{id}/bundle-output.md`
  4. `commonplace-ingest-bundle-output` parses that artifact, finalizes through `record_and_finalize_run` (single-run ingest is all-or-nothing), writes packing-derived parsed result files, stores their paths, and refreshes `MANIFEST.json`
- **External-executor batch path (`batch.py`)** — deterministic ends for any orchestrator that owns its own fan-out (a live agent reviewing many pairs, or a harness workflow spawning sub-agents per batch); decision record: [ADR 030](./adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md).
  1. `commonplace-prepare-review-batch <note>::<gate>... --runner <label> --model <partition>` creates one note-packed or gate-packed run for the pair set (inapplicable gates skipped and reported; missing notes/gates fatal) and writes the canonical prompt from captured snapshots under `kb/reports/bundle-reviews/review-run-{review_run_id}/`; returns `review_run_id`, pair metadata, skipped pairs, `prompt_path`, `bundle_output_path`, and `manifest_path` as JSON
  2. the executor follows the prompt and writes `bundle_output_path`
  3. `commonplace-ingest-batch-output --review-run-id <id> --input-file <path>` finalizes with pair salvage, stores result paths, and returns JSON; exit 1 if the run failed.

### runners/ — harness CLI adapters

Each subprocess harness CLI sits behind the `RunnerAdapter` interface (`runners/base.py`): build the command, optionally decode the stdout stream, collect best-effort telemetry from vendor session logs afterwards. `runners/claude_code.py` and `runners/codex.py` are the adapters; the registry in `runners/__init__.py` backs `run_prompt` dispatch and the CLIs' `--runner` choices. Adding a harness CLI is one adapter module plus one registry entry. Telemetry is best-effort by design — session-log formats are undocumented vendor internals, and a failed scrape never fails a run.

`run_prompt` captures stdout/stderr, exit code, and session telemetry (token counts, model info).

---

## Targeting & staleness

### review_target_selector.py

Identifies (note, gate) pairs needing review by comparing current vs. accepted provenance:

| Reason | Meaning |
|---|---|
| `missing-review` | No acceptance exists for this (note path, gate path, model partition) triple |
| `note-changed` | Current note content hash differs from the accepted note baseline |
| `gate-changed` | Current gate content hash differs from the accepted gate baseline |

The selector compares SHA-256 over current file text with the accepted snapshot hash and generates diffs from accepted snapshot text. Rows whose migrated baseline has no accepted snapshots report `missing-review` with diff unavailable.

Also provides:
- `ack_pairs(repo_root, pairs, model)` — batch-acknowledge pairs with `trivial-change-ack`
- `list_reviewable_notes(repo_root) / list_current_notes(repo_root)` — top-level `*.md` notes across the configured scan roots (`kb/notes/` and `kb/reference/`), non-recursive, skipping indexes and files without frontmatter
- explicit note-scope expansion for files and directories; directory operands expand direct child `*.md` files only and skip indexes, files without frontmatter, and content under `types/` directories
- `note_diff_from_text()` — unified diff between accepted snapshot text and current note text

### resolve_gates.py

- `resolve_to_gate_ids(args, gates_dir) -> list[str]` — expand CLI bundle names (e.g., `"prose"`) to human-facing gate ids from `gates_dir/prose/*.md`
- `applicable_gate_ids_for_note(note_path, gate_ids, gates_dir) -> list[str]` — filter those gate ids by note `traits` vs gate `requires_trait`, and note `type` vs gate `requires-type`

### warn_selector.py

Query effective completed review pairs with `decision="warn"`, skip stale gate revisions, and extract actionable findings from the `### Findings` section. Gate staleness uses the accepted gate snapshot hash.

---

## Repair & migration utilities

These are operational commands for database maintenance. All support `--dry-run`.

| Command | Purpose |
|---|---|
| `prune-superseded-reviews` | Delete superseded non-current review pairs; delete whole run artifact directories only when every pair in the run is obsolete |
| `repair-model-partitions` | Collapse known model aliases in review runs, review pairs, and acceptance events |
