# Review System (`commonplace.review`)

The review system runs LLM-based quality reviews against KB notes using defined review gates. It tracks provenance (note and gate versions), manages acceptance state, and detects staleness.

For the review workflow and gate definitions, see `kb/instructions/REVIEW-SYSTEM.md`. This document covers the code architecture.

## Architecture overview

```
┌─────────────────────────────────────────────────┐
│  Orchestration                                  │
│  review_sweep       run_review_bundle           │
│  run_gate_sweep     create/finalize_review_run  │
├─────────────────────────────────────────────────┤
│  Gate resolution & targeting                    │
│  resolve_gates      review_target_selector      │
│  warn_selector      ack_trivial_note_changes    │
├─────────────────────────────────────────────────┤
│  Execution                                      │
│  review_runners     gate_sweep_format           │
├─────────────────────────────────────────────────┤
│  Data model                                     │
│  review_db          review_model                │
│  review_metadata    review-schema.sql           │
└─────────────────────────────────────────────────┘
```

---

## Data model

### Database schema (`review-schema.sql`)

SQLite database, default location `kb/reviews/reviews.db` (override with `COMMONPLACE_REVIEW_DB` env var).

**Core tables:**

| Table | Purpose | Key columns |
|---|---|---|
| `review_runs` | Execution records | id, note_path, model_id, runner, status (running/completed/failed), provenance SHAs |
| `review_run_gates` | Gate set captured at run start | review_run_id, gate_id, gate_sha, ordinal |
| `gate_reviews` | Individual gate outcomes | review_run_id, note_path, gate_id, decision (pass/warn/fail/error/unknown), rationale_markdown |
| `acceptance_events` | Append-only acceptance log | note_path, gate_id, model_id, accepted_review_id, acceptance_kind |

**Key views:**

- `current_gate_acceptances` — latest acceptance for each (note, gate, model) triple
- `stale_gate_pairs` — current acceptance states for staleness detection

**Acceptance kinds:** `full-review`, `gate-migration`, `trivial-change-ack`, `migration-import`, `manual-override`

### review_model.py

Encode and normalize model identifiers with reasoning effort levels.

- `encode_model(model) -> str` — sanitize model names (lowercase, special chars → hyphens)
- `normalize_reasoning_effort(raw) -> str | None` — validate from {low, medium, high, xhigh}
- `build_model_id(model, reasoning_effort) -> str` — canonical ID like `"claude-3-5-sonnet-xhigh"`

### review_metadata.py

Git-backed provenance tracking and metadata block management.

**Provenance functions:**
- `review_note_provenance(repo_root, path) -> (blob_sha, commit | None)` — get the review baseline for a note; `commit=None` means the baseline came from the current worktree
- `committed_file_provenance(repo_root, path, *, kind) -> (blob_sha, commit)` — generic file provenance
- `blob_sha_at_commit(repo_root, commit, path) -> str | None` — file SHA at a specific commit
- `file_text_at_commit(repo_root, commit, path) -> str | None` — file content at a commit

**Metadata blocks:**
- `parse_review_metadata(review_text) -> ReviewMetadata | None` — extract `<!-- REVIEW-METADATA ... -->` blocks
- `render_review_metadata(metadata) -> str` — generate metadata block
- `inject_review_metadata(review_text, metadata) -> str` — insert/update metadata block

### review_db.py

Database operations, decision parsing, and record management. The largest module in the package.

**Connection & setup:**
- `connect(db_path) -> Connection` — open with Row factory
- `resolve_db_path(repo_root) -> Path` — resolve DB location
- `ensure_db(repo_root, db_path)` — initialize from schema if needed

**CRUD operations:**
- `insert_review_run(conn, ...) -> int` — create run, return ID
- `insert_gate_review(conn, ...) -> int` — record gate outcome
- `append_acceptance_event(conn, ...) -> int` — record acceptance
- `complete_review_run(conn, ...) / fail_review_run(conn, ...)` — finalize run status
- `load_review_run / load_gate_reviews_for_run / load_gate_reviews_for_note` — query helpers
- `load_effective_gate_review_map(conn, ...) -> dict` — accepted-or-latest reviews per gate
- `load_current_acceptances(conn) -> dict` — current acceptance state map

**Lifecycle helpers:**
- `create_run(conn, ...) -> int` — create the run row plus its captured gate set
- `attach_execution_data(conn, ...)` — persist telemetry, raw bundle markdown, and debug log
- `record_and_finalize_run(conn, ...) -> int` — optionally insert gate reviews, rekey to the actual model, validate coverage, complete the run, and append acceptance events

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
1. resolve_gates     → expand bundle names to gate IDs, filter by note traits
2. create_run        → insert review_run + review_run_gates (status=running)
3. review_runners    → invoke claude-code or codex CLI with review prompt
4. attach_execution_data → persist runner artifacts and telemetry
5. extract results   → parse gate blocks from runner output
6. record_and_finalize_run → write gate_reviews, validate coverage, mark run completed, append acceptance_events
```

### run_review_bundle.py — Multi-gate single-note review

The primary review mode. Runs multiple gates against one note in a single LLM invocation.

- Resolves markdown links in the note so the reviewer sees linked content
- Builds a structured prompt with gate definitions and note content
- Parses output delimited by `=== GATE REVIEW START/END: {gate-id} ===`
- Records individual gate_reviews and acceptance_events

### run_gate_sweep.py — Single-gate multi-note review

Runs one gate across multiple notes in batched prompts.

- Uses `review_target_selector` to find stale notes for a gate
- Batches notes (default 5 per batch)
- Output parsed by `gate_sweep_format.extract_gate_sweep_reviews()`
- Each note gets its own review_run record

### review_sweep.py — Full review sweep

Orchestrates a complete review pass: selects all stale note/gate pairs, groups by note, runs bundles.

### review_runners.py — LLM execution

Invokes `claude-code` or `codex` CLI processes with a review prompt. Captures:
- stdout/stderr
- Exit code
- Session telemetry (token counts, model info) from CLI session logs

---

## Targeting & staleness

### review_target_selector.py

Identifies (note, gate) pairs needing review by comparing current vs. accepted provenance:

| Reason | Meaning |
|---|---|
| `missing-review` | No acceptance exists for this (note, gate, model) triple |
| `note-changed` | Note blob SHA differs from accepted note SHA |
| `gate-changed` | Gate blob SHA differs from accepted gate SHA |

Also provides:
- `ack_pairs(repo_root, pairs, model)` — batch-acknowledge pairs with `trivial-change-ack`
- `list_reviewable_notes / list_current_notes` — filter notes by status
- `note_diff_since()` — unified diff between accepted and current note

### resolve_gates.py

- `resolve_to_gate_ids(args, gates_dir) -> list[str]` — expand bundle names (e.g., `"prose"`) to gate files in `gates_dir/prose/*.md`
- `applicable_gate_ids_for_note(note_path, gate_ids, gates_dir) -> list[str]` — filter by note `traits` vs gate `requires_trait`

### warn_selector.py

Query effective reviews with `decision="warn"`, extract actionable findings from the `### Findings` section.

### ack_trivial_note_changes.py

Auto-acknowledge `note-changed` pairs when only non-watched parts changed. Each gate declares what it `watches` (body, title, description) — if changes are outside the watched set, the pair can be acked without re-review.

---

## Prompt formats

### Bundle format (multi-gate)

```
=== GATE REVIEW START: {gate-id} ===
### Summary
<prose>

### Findings
- <severity>: <finding>

### Suggested Revision
<optional>

## Result: PASS|WARN|FAIL|ERROR
=== GATE REVIEW END: {gate-id} ===
```

### Gate sweep format (multi-note)

```
=== NOTE START: {note-path} ===
=== GATE REVIEW START: {gate-id} ===
...review...
## Result: PASS|WARN|FAIL|ERROR
=== GATE REVIEW END: {gate-id} ===
=== NOTE END: {note-path} ===
```

---

## Repair & migration utilities

These are operational commands for database maintenance. All support `--dry-run`.

| Command | Purpose |
|---|---|
| `repair-codex-model-partitions` | Backfill model_id and telemetry from saved Codex session logs |
| `repair-manual-import-review-results` | Re-infer decisions for legacy manual-import reviews |
| `reparse-gate-review-decisions` | Re-parse decisions from stored markdown (after parser updates) |
| `prune-superseded-unknown-manual-import-reviews` | Delete manual-import reviews with decision=unknown that have replacements |
