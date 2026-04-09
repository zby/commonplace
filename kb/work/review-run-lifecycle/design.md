# Proposed reorganization (revised)

The core problem is real: lifecycle logic is scattered across 5 scripts, producing inconsistent data depending on which command path was used. The fix is to centralize lifecycle transitions — but with less ceremony than originally proposed.

## Core claim

Scripts should stop coordinating state transitions themselves. A small set of functions (in `review_db.py` or a thin layer on top) should own the meaning of run creation, recording, completion, and failure. No new module with typed state returns — just centralized sequencing.

## What stays from the original design

- All scripts should stop open-coding run transitions
- Telemetry attachment should happen in one place
- Model partition assignment should happen in one place
- Dry-run must not persist rows

## What we're dropping

### No `prepared` status

The original design proposed `prepared` → `running` to distinguish "created but not launched" from "actually executing." But for split-agent runs, the agent *is* the runner — there's no observable transition. If the agent crashes, you have a stale row either way regardless of whether it says `prepared` or `running`. The status enum stays: `running`, `completed`, `failed`.

### No typed state-machine returns

`prepare_run() -> PreparedRun`, `start_run() -> RunningRun` adds types for states nobody inspects. Scripts don't branch on state types. Functions return run IDs.

### No `requested_model_id` / `actual_model_id` split

One `model_id` column, updated in place when the actual model is known. The lifecycle functions centralize *when* this update happens — that's sufficient.

**Rekeying safety net:** `record_and_finalize_run` accepts an optional `actual_model_id`. If provided and different, it rekeys the run and any already-written `gate_reviews` before appending `acceptance_events`. In practice this rarely triggers — nested paths already know the actual model before gate reviews are inserted, and split-path agents typically self-report correctly. But having the rekey in one place means no path can produce inconsistent partitions, even if a future caller supplies a correction at finalization time.

### No mandatory telemetry

Telemetry remains nullable. The lifecycle functions centralize *where* telemetry gets attached, but don't enforce *that* it's attached. No "unavailable reason" tracking.

### No `aborted` status

Deferred indefinitely.

## Lifecycle functions

Three functions cover what 5 scripts currently open-code:

### 1. `create_run(...) -> int`

One place that calls `insert_review_run` + `insert_review_run_gates`. Returns the run ID.

Called by: `create_review_run.py`, `run_review_bundle.py`, `run_gate_sweep.py`.

### 2. `record_and_finalize_run(...)`

One place that:
- optionally inserts gate reviews (nested paths pass them in; split path has already written them)
- if `actual_model_id` is provided and differs from `review_runs.model_id`: rekeys the run and all its `gate_reviews` before proceeding
- checks gate coverage
- calls `complete_review_run`
- appends `acceptance_events` (using the final, possibly rekeyed `model_id`)
- optionally attaches telemetry, raw bundle markdown, debug log

If coverage is incomplete or recording fails, calls `fail_review_run` instead.

Called by: `finalize_review_run.py` (for split gate-by-gate path), `run_review_bundle.py`, `run_gate_sweep.py`.

For the split gate-by-gate path, gate reviews are already inserted individually via `write_gate_review.py`, so this function validates coverage, rekeys if needed, and finalizes.

### 3. `attach_execution_data(...)`

One place that stores execution artifacts: telemetry JSON, debug log, raw bundle markdown. Does **not** rekey `model_id` — that is exclusively `record_and_finalize_run`'s job, because rekeying must happen atomically with gate_reviews and before acceptance_events are appended.

This replaces the scattered calls to `update_review_run_telemetry` that currently live in `run_review_bundle.py` and `run_gate_sweep.py`.

## Path simplification

### Remove Path 2: split bundled agent path

Currently there are two split-agent paths:
- **Path 1** (gate-by-gate): agent calls `create_review_run`, `write_gate_review` per gate, `finalize_review_run`
- **Path 2** (bundled): agent calls `create_review_run`, writes a bundle file, then `record_bundle_review` parses it

Path 2 is an awkward middle ground — the agent does the review work but outputs in bundle format, then the system re-parses it. There's no clear reason the agent can't use Path 1 instead. Removing Path 2 eliminates `record_bundle_review.py` and simplifies the code paths.

The bundle format remains for **nested runner output** (Paths 3 and 4), where it's the natural output format of an autonomous subprocess.

### Repair script: defer deletion

`repair_codex_model_partitions.py` (275 lines) compensates for historical data written before the nested wrapper added telemetry/model corrections. With lifecycle logic centralized, new runs won't need repair. Deletion is deferred to a follow-up once the lifecycle functions are in place and no existing data depends on it.

## Surviving paths after simplification

1. **Split gate-by-gate**: `create_review_run` → `write_gate_review` (repeated) → `finalize_review_run`
2. **Nested runner bundle**: `run_review_bundle` orchestrates create → execute → record → finalize
3. **Nested runner sweep**: `run_gate_sweep` batches multiple notes through the nested runner

All three use the same lifecycle functions internally.

## How the scripts change

### `create_review_run.py`

Becomes a thin CLI over `create_run(...)`. No behavior change.

### `write_gate_review.py`

Stays as-is — it validates and inserts one gate review using `review_run.model_id`. If the actual model turns out to differ, finalization handles the rekey (see split-path rekeying rule above).

### `finalize_review_run.py`

Calls `record_and_finalize_run(...)` with no new gate reviews (they were already inserted). The function validates coverage and appends acceptance events.

### `run_review_bundle.py`

Orchestrates:
1. `create_run(...)`
2. nested runner invocation
3. `attach_execution_data(...)` with telemetry, debug log, raw bundle
4. `record_and_finalize_run(...)` with parsed gate reviews and `actual_model_id` from telemetry

On failure: `fail_review_run(...)` with whatever execution data is available.

The `--dry-run` codepath prints the prompt and exits **before** `create_run(...)` is called.

### `run_gate_sweep.py`

Same pattern as `run_review_bundle.py` but batched per note. Shared telemetry attached to each run through the same `attach_execution_data(...)`.

### `record_bundle_review.py`

Deleted.

### `repair_codex_model_partitions.py`

No changes in this phase. Deletion deferred to follow-up.

## Dry-run fix

The dry-run bug is simple: `run_review_bundle.py` currently calls `insert_review_run` before checking `--dry-run`. Fix by reordering: build the prompt first, check `--dry-run`, only call `create_run(...)` if actually executing. This can be fixed immediately, independent of the rest.

## Implementation sequence

### 1. Fix dry-run persistence (immediate, standalone)

Reorder `run_review_bundle.py` so `--dry-run` exits before any DB writes. Pure bug fix.

### 2. Write the three lifecycle functions

Add `create_run`, `record_and_finalize_run`, and `attach_execution_data` to `review_db.py` (or a thin `review_run_lifecycle.py` if `review_db.py` is already too large). Wire all scripts to use them.

### 3. Delete `record_bundle_review.py` and its CLI entry point

Remove Path 2. Update any instructions or docs that reference it.

### 4. (Follow-up) Delete `repair_codex_model_partitions.py` and its tests

Once lifecycle functions are in place and no existing data depends on the repair script, delete it.

## Minimum viable end state

1. Every persisted run was intentionally created (no dry-run ghosts)
2. All surviving paths use the same lifecycle functions
3. Model rekeying owned by `record_and_finalize_run` — one place, one rule
4. Telemetry/artifact storage owned by `attach_execution_data` — no rekeying
5. Path 2 (split bundled) removed
