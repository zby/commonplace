---
description: Code architecture for commonplace.review and commonplace.cli.review - package layout, data model, the (note, gate)-pair protocol and batch executor, packing callers, targeting, and repair utilities
type: kb/types/note.md
tags: []
status: current
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review system executes LLM-based quality reviews against KB notes using defined review gates. It tracks provenance (note and gate versions), manages acceptance state, and detects staleness.

For the review workflow and gate definitions, see [REVIEW-SYSTEM.md](./REVIEW-SYSTEM.md). This document covers the code architecture.

> **Sweep commands are experimental.** `review_sweep`, `run_gate_sweep`, and `ack_trivial_note_changes` are not yet stabilized and are intentionally not documented in detail here. Treat their interfaces as subject to change.

## Package layout

The review subsystem is split between two packages, mirroring the project-wide `commonplace.cli` ↔ `commonplace.lib` split:

- **`commonplace.review`** — library code only. Pure functions, dataclasses, the SQLite layer, the runner subprocess wrappers. No `main()` functions, no argparse, no `Path.cwd()` at import time. Importable from any caller without pulling in CLI machinery.
- **`commonplace.cli.review`** — thin CLI wrappers. Each module is argparse + `Path.cwd()` + `prepare_review_db(...)` + one library call. The `commonplace-*` review entry points in `pyproject.toml` all live here.

For most modules the lib name and the CLI name match. For example `commonplace.review.run_review_bundles` is the library that resolves note-local gate requests into bundle-sized runner calls and hands each batch to `executor.execute_batch`; `commonplace.cli.review.run_review_bundles` is the thin wrapper that argparse-parses the user's invocation and calls into the lib. Two modules (`resolve_gates` and `review_target_selector`) exist in both packages because they were split during the layout migration: lib helpers stayed in `commonplace.review.*`, the CLI `main()` moved to `commonplace.cli.review.*`.

This document refers to modules by their unqualified names (e.g. `run_review_bundles`, `review_target_selector`) when the distinction doesn't matter. When a particular function or class is called out, it lives in the library package unless explicitly noted as a CLI.

## Architecture overview

```
┌─────────────────────────────────────────────────┐
│  Packing (which pairs share one LLM call)       │
│  run_review_bundles (note-local bundle groups)  │
│  run_gate_sweep (share-gate, experimental)      │
│  batch + create/claim/finalize (external        │
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
│  review-schema.sql  paths                       │
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
| `review_jobs` | Review invocations | review_job_id, model_partition, nullable runner/runner_model/runner_effort, status (queued/running/completed/failed), created_at, nullable started_at, packing, telemetry_json, prompt_path, bundle_output_path |
| `review_file_snapshots` | Role-neutral file snapshots for review inputs | snapshot_id, path, content_sha256, content_text |
| `review_pairs` | Requested and completed pair outcomes | review_pair_id, review_job_id, note_path, gate_path, pair_status, decision, snapshot IDs |
| `acceptance_events` | Append-only acceptance log | acceptance_event_id, note_path, gate_path, model_partition, accepted_review_pair_id, snapshot IDs |

**Key views:**

- `current_gate_acceptances` — latest acceptance for each `(note_path, gate_path, model_partition)` triple
- `stale_gate_pairs` — current acceptance states for staleness detection

### review_model.py

Encode and normalize model identifiers with reasoning effort levels.

- `encode_model(model) -> str` — sanitize model names (lowercase, special chars → hyphens)
- `normalize_model_partition(model_partition) -> str` — collapse known aliases such as `opus-4-6` into canonical review partitions
- `normalize_reasoning_effort(raw) -> str | None` — validate from {low, medium, high, xhigh}
- `build_model_partition(model, reasoning_effort) -> str` — canonical ID like `"claude-3-5-sonnet-xhigh"`

### paths.py

Filesystem path constants and gate identity helpers used across the review subsystem. It resolves the active gate catalog (`kb/instructions/review-gates` in source checkouts, installed framework gates in generated projects), converts human-facing gate ids such as `prose/source-residue` into repo-relative `gate_path` values, and derives display shorthands from stored paths. Lives in its own module so the data layer (`review_db.py`) does not have to own filesystem constants about gate locations.

### review_db.py

Database operations, decision parsing, and record management. The largest module in the package.

**Connection & setup:**
- `connect(db_path) -> Connection` — open with Row factory
- `resolve_db_path(repo_root, db_override=None) -> Path` — resolve DB location, honoring an optional `--db` override
- `ensure_db(repo_root, db_path)` — initialize from schema if needed, or migrate an existing review store through `PRAGMA user_version`
- `prepare_review_db(repo_root, db_override=None) -> Path` — convenience helper that resolves and ensures in one call; collapses the four-step bootstrap that every CLI used to open-code
- `snapshot_file(conn, repo_root, path)` — capture or rehydrate the exact UTF-8 file text for a repo-relative note or gate path, keyed by `(path, content_sha256)`

**Note relocation helpers** (called by `commonplace.lib.relocation`):
- `count_note_path_records(conn, *, note_path) -> NotePathUpdateCounts` — how many `review_pairs`/`acceptance_events` rows reference a note path
- `rekey_note_path(conn, *, old_note_path, new_note_path) -> NotePathUpdateCounts` — update those rows in place when a note moves

**CRUD operations:**
- `create_job(conn, ...) -> int` — create a job invocation with explicit status/timing, return ID
- `create_review_pairs(conn, ...) -> list[int]` — insert requested pair rows
- `create_job_with_pairs(conn, ...) -> int` — create a job and its requested pair set
- `complete_review_pairs(conn, ...) -> list[int]` — record pair outcomes parsed from output
- `mark_missing_pairs(conn, ...) -> int` — mark requested pairs without output
- `append_acceptance_event(conn, ...) -> int` — record acceptance
- `complete_review_job(conn, ...) / fail_review_job(conn, ...)` — finalize job status
- `load_review_job / load_review_pairs_for_job / load_review_pairs_for_note` — query helpers; pair rows derive `model_partition` by joining through `review_jobs`
- `load_review_job_plan / list_review_job_plans` — shared job-plan loaders for creation, listing, and later execution/finalization paths
- `load_effective_review_pair_map(conn, ...) -> dict` — accepted-or-latest completed review pairs per gate
- `load_current_acceptances(conn) -> dict` — current acceptance state map

**Lifecycle helpers:**
- `attach_execution_data(conn, ...)` — persist telemetry
- `record_and_finalize_job(conn, ...) -> int` — complete parsed pairs, validate coverage, complete or fail the job, and append acceptance events for completed pairs

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
3. create_job_with_pairs → insert review_job + review_pairs, one job per prompt invocation (`queued` for live-agent/orchestrator preparation, `running` for immediate subprocess execution)
4. executor.execute_batch
   a. protocol/prompt.render_pairs_prompt → one prompt embedding each note and gate text once
   b. review_runners.run_prompt           → invoke claude-code or codex CLI
   c. protocol/parser.parse_pair_bundle   → extract pair blocks, canonicalize result footers
   d. per job: complete parsed pairs, mark missing pairs, complete or fail the job
5. record_and_finalize_job → write review_pairs, copy pair snapshot IDs to acceptance events, validate coverage, mark job completed or failed
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
- `artifacts.py` — shared artifact naming and manifest writing. It is the only place that maps packing to parsed result filenames: note-packed jobs use gate-leaf filenames, gate-packed jobs use note filenames, and unsupported packing values fail.
- `executor.py` — `execute_batch(targets, gate_texts, …)` owns the shared lifecycle: render, one runner call, telemetry/model-mismatch handling, usage-exhaustion (`UsageExhausted`) and interrupt handling, parse, then per-job finalize or fail. Each job writes `bundle-output.md`, writes per-pair result files, writes `debug.log` when runner diagnostics exist, and stores `review_jobs.bundle_output_path` plus `review_pairs.result_path` in the DB.

### Packing callers

- **`run_review_bundles.py` — note-local bundle packing.** One note, requested gates grouped by bundle/lens; one subprocess runner call and one review job per group.
- **`run_gate_sweep.py` — share-gate packing (experimental).** One gate over a chunked note list; one running gate-packed job per prompt batch; missing pairs are marked `missing`, parsed pairs are retained, and the invocation records a failure.
- **Live-agent path (single note)** — same protocol without a nested runner:
  1. `commonplace-create-review-jobs --model <partition> --note <note> <gate-or-bundle>... --grouping note` groups requested gates by bundle/lens, creates one queued note-packed job per group with null runner provenance, writes each canonical prompt to `kb/reports/bundle-reviews/review-job-{id}/prompt.md`, writes `MANIFEST.json`, and returns a JSON `jobs` array with each job's `prompt_path`, `bundle_output_path`, `manifest_path`, and pair rows
  2. each prompt is rendered from the snapshots attached to that job's created pair rows
  3. the parent agent claims each dispatched job with `commonplace-claim-review-job --review-job-id <id> --runner <worker> --model <model> [--effort <effort>]`
  4. the parent agent delegates each claimed job to a sub-agent, and that sub-agent reads `prompt_path`, follows it, and writes the matching `bundle_output_path`
  5. `commonplace-finalize-review-job --review-job-id <id>` parses the job-owned artifact, finalizes through `record_and_finalize_job`, writes parsed result files to persisted `review_pairs.result_path` values with provenance frontmatter, and refreshes `MANIFEST.json`
- **External-executor direct-pair path (`commonplace-create-review-jobs --pair`)** — deterministic creation for orchestrators that already know the exact `(note, gate)` pairs; decision record: [ADR 030](./adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md).
  1. `commonplace-create-review-jobs --model <partition> --pair <note>::<gate>... --grouping {note,gate}` creates queued note-packed or gate-packed jobs for the pair set (inapplicable gates skipped and reported; missing notes/gates fatal) and writes canonical prompts from captured snapshots under `kb/reports/bundle-reviews/review-job-{review_job_id}/`; returns job and pair metadata, skipped pairs, `prompt_path`, `bundle_output_path`, and derived `manifest_path` values as JSON
  2. the parent claims each dispatched job with `commonplace-claim-review-job`, then the executor follows the prompt and writes `bundle_output_path`
  3. `commonplace-finalize-review-job --review-job-id <id>` finalizes with pair salvage and returns JSON; exit 1 if the job failed.

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

## Maintenance Utilities

These are operational commands for database maintenance. All support `--dry-run`.

| Command | Purpose |
|---|---|
| `prune-superseded-reviews` | Delete superseded non-current review pairs; delete whole job artifact directories only when every pair in the job is obsolete |
| `repair-model-partitions` | Collapse known model aliases in review jobs, review pairs, and acceptance events |
