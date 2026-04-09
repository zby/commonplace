# Current review run paths

This document inventories the live paths that create or mutate `review_runs` and highlights where they diverge.

## Shared schema facts

The current schema allows nullable telemetry:

- `review_runs.telemetry_json` is nullable in `review-schema.sql`
- `insert_review_run(...)` defaults `telemetry_json=None`
- `complete_review_run(...)` and `fail_review_run(...)` use `COALESCE`, so terminal rows can remain null

The current status model has only:

- `running`
- `completed`
- `failed`

That forces the code to overload `running` to mean both:

- "prepared for review"
- "runner is actually executing"

## Path 1: split gate-by-gate agent path

Commands:

1. `commonplace-create-review-run`
2. `commonplace-write-gate-review` repeated once per gate
3. `commonplace-finalize-review-run`

Current write flow:

1. `create_review_run.py` inserts a `review_runs` row with:
   - `status='running'`
   - requested `model_id`
   - no telemetry
2. `write_gate_review.py` loads the parent run and inserts one `gate_reviews` row per gate using `review_run.model_id`
3. `finalize_review_run.py` checks coverage and appends `acceptance_events`

What this path gets right:

- gate coverage is validated before acceptance advances
- gate reviews inherit note provenance and captured gate SHA from the run
- direct agent execution is supported

What this path does not write:

- telemetry
- actual model partition if it differs from requested
- runner debug log
- raw bundle markdown

Main mismatch:

- a row exists with `status='running'` before any execution metadata exists
- terminal rows can be completed with no telemetry at all
- accepted model partition remains the requested one, not necessarily the actual one

## Path 2: split bundled agent path

Commands:

1. `commonplace-create-review-run`
2. agent writes `kb/reports/bundle-reviews/review-run-{id}/bundle-output.md`
3. `commonplace-record-bundle-review`

Current write flow:

1. same run creation as Path 1
2. `record_bundle_review.py` reads `bundle-output.md`
3. it calls `record_bundle_review_run(...)`
4. that function parses gate blocks, inserts `gate_reviews`, then calls `finalize_review_run`

What this path gets right:

- bundled review output is parsed centrally
- gate coverage is validated before acceptance advances

What this path does not write:

- telemetry
- actual model partition if different from requested

Main mismatch:

- same lifecycle problem as Path 1, but hidden behind bundle parsing instead of per-gate writes

## Path 3: nested runner bundle wrapper

Command:

- `commonplace-run-review-bundle`

Current write flow:

1. inserts a `review_runs` row immediately with `status='running'`
2. constructs a prompt containing `Review run id: {id}`
3. if `--dry-run`, prints the prompt and exits
4. otherwise launches the nested runner through `run_prompt(...)`
5. tries to recover telemetry from CLI session logs
6. if telemetry reports a different actual model partition, updates `review_runs.model_id`
7. persists telemetry/debug/raw bundle output while recording and finalizing the run

What this path gets right:

- it is the only path that currently tries to persist telemetry inline
- it can rekey from requested model partition to actual partition before `gate_reviews` and `acceptance_events` are written
- failure paths also try to persist telemetry/debug output

What can still go wrong:

- `--dry-run` leaves a real `review_runs` row behind even though no review occurred
- telemetry capture is best-effort, because `run_prompt(...)` only returns telemetry if it can match a session log
- terminal rows can still end with null telemetry if the log lookup fails

Main mismatch:

- this path implicitly owns more lifecycle work than the split paths
- correctness depends on wrapper-specific sequencing rather than a shared lifecycle API

## Path 4: nested runner gate sweep

Command:

- `commonplace-run-gate-sweep`

Current write flow:

1. for each note in the batch, inserts a `review_runs` row with `status='running'`
2. on `--dry-run`, it does not persist runs
3. launches one nested runner call for the batch
4. extracts one shared telemetry object for the batch
5. if needed, rekeys each parent run to the actual model partition
6. records one note-local bundle per run through `record_bundle_review_run(...)`

What this path gets right:

- unlike `run_review_bundle`, dry-run does not persist fake runs
- telemetry/model rekeying behavior matches the nested bundle path
- per-note acceptance remains gate-local even though execution is batched

What can still go wrong:

- telemetry is still best-effort
- all runs in the batch share one telemetry payload, which is operationally reasonable but different from the one-run/one-telemetry assumption implied by the split path

Main mismatch:

- this wrapper already behaves differently from `run_review_bundle` on dry-run persistence
- another sign that lifecycle rules live in scripts instead of one owner

## Path 5: repair path

Command:

- `commonplace-repair-codex-model-partitions`

What it does:

- scans saved Codex session logs under `~/.codex/sessions`
- extracts `Review run id: N` from prompts
- rebuilds telemetry
- backfills `review_runs.telemetry_json`
- rekeys `review_runs`, `gate_reviews`, and accepted `acceptance_events` to the actual model partition

Why it exists:

- historical rows were written without the telemetry/model corrections that the nested wrapper path later added

Why it matters for design:

- it is compensating for missing lifecycle invariants
- if all live paths produced correct final rows, this would only remain as a one-off migration tool

## Divergence summary

The current paths disagree on four things:

## 1. When does a run start?

- split paths: at creation time
- nested paths: also at creation time, but then immediately launch
- gate sweep dry-run: never persists the run at all

The model needs a state for "prepared but not launched".

## 2. Who owns telemetry?

- split paths: nobody
- nested paths: wrapper-specific logic
- repair path: late backfill from session logs

Telemetry currently belongs to whichever script happened to launch the runner.

## 3. Who decides the actual model partition?

- split paths: requested `model_id` becomes canonical
- nested paths: actual telemetry may rekey the run before reviews are recorded
- repair path: historical correction later

The model partition contract is inconsistent across paths.

## 4. Where is lifecycle logic implemented?

- partially in `review_db.py`
- partially in `run_review_bundle.py`
- partially in `run_gate_sweep.py`
- partially in `record_bundle_review.py`
- partially in `finalize_review_run.py`

The system does not currently have one module that owns the lifecycle of a review run.

## Immediate design conclusions

1. `review_runs` needs a true pre-execution state.
2. Telemetry attachment has to become an explicit lifecycle step.
3. Actual model partition assignment must be centralized.
4. All scripts should stop open-coding run transitions.
