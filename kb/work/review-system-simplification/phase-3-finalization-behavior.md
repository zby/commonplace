# Phase 3 - finalization behavior

## Position

Third phase. Revise this file after phase 2 lands; its exact tasks depend on the derived-path and status representation chosen there.

## Prerequisite

Phase 2 complete:

- artifact paths are derived
- schema no longer stores path fields
- pair status representation is simplified or ready to finish simplifying
- review tests pass

## Purpose

Simplify the behavioral core of review execution:

- provenance is recorded at finalization time
- claim/running state disappears
- finalization is all-or-nothing
- live parsing is strict

## Scope

This phase intentionally changes public behavior. It should update tests as behavior changes, but full documentation and ADR cleanup can wait for phase 4.

## Tasks

### Finalization-Time Provenance

- Add optional `--runner`, `--model`, and `--effort` to `commonplace-finalize-review-job`.
- Validate supplied `--model`/`--effort` with `build_model_partition` against the job's `model_partition`.
- Record `runner`, `runner_model`, and `runner_effort` before job completion in the same transaction. Reuse `attach_execution_data` (`review_db.py`) for this — it already writes exactly these provenance fields. Move it from the claim path to the finalization path; do not delete it as "claim-specific."
- Smoke finalization with and without provenance flags.
- Verify a model/effort mismatch fails before state mutation.

### Claim and Running Removal

- Remove `commonplace-claim-review-job` if phase 1 inventory found no active external dependency.
- Remove the script entry point from `pyproject.toml`.
- Remove claim-specific DB functions and tests. Note `attach_execution_data` is **not** claim-specific after the step above — it is now the finalization provenance writer and must survive.
- Remove `running` from job status values and schema checks.
- Remove `started_at` payload/display assumptions if any survived phase 2.

### All-Or-Nothing Finalization

- Missing expected pairs become fatal for the whole job.
- Do not complete any pair until all expected pairs parse and all artifact writes are valid.
- Append acceptance events only after the whole job is ready to complete.
- On parse, coverage, or artifact failure, mark the job failed and append no acceptance events.
- Remove `mark_missing_pairs` and missing-pair status code paths if phase 2 did not already remove them.
- Update pruning and warning selection assumptions so accepted pairs come only from completed jobs.

### Strict Live Parser

- Add a strict live decision parser.
- Require exactly one final result line inside each pair block:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
```

- Remove live use of fallback inference from severity bullets, `INFO`/`OK`, `Verdict`, `Outcome`, revised result, flagging phrases, and bold first-line decisions.
- Delete fallback parser tests or move them under an explicit legacy parser if historical parsing is still useful.
- Update prompt text to make aliases invalid in live output.
- Drop `unknown` from the `review_pairs.decision` `CHECK` enum in `review-schema.sql`. It existed only to hold the permissive fallback; strict parsing never emits it, and the store is schema-current so no legacy rows need it. Remove any code path that writes or branches on `decision = 'unknown'`.

## Expected Delta

Large test reduction from removing:

- claim/running tests
- partial salvage tests
- permissive live parser fixtures

Moderate production reduction in finalization, DB status helpers, CLI command surface, and parser code.

## Cleanup Gate

Before ending this phase:

- Run `rg "claim-review-job|claim_review_job|running|started_at|missing pairs|mark_missing_pairs|pair_status|INFO|OK|Verdict|Outcome|Revised result|flagging as" src test kb/reference kb/instructions kb/work/review-system-simplification`.
- For each hit, remove it, update it to finalization-time provenance/all-or-nothing/strict parsing, or mark it explicitly as historical/deferred.
- Delete the claim CLI module, pyproject entry, tests, and docs if claim is removed.
- Delete partial-salvage tests and fixtures if all-or-nothing finalization is implemented.
- Delete or quarantine permissive parser tests under an explicit legacy parser if historical parsing is retained.
- Update phase 4 with the exact public commands, flags, status values, parser rules, and retained legacy references after this phase.

## Verification

- `pytest test/commonplace/review`
- Smoke finalization both with and without provenance flags.
- Smoke a two-pair job with one missing block: job fails, no pair decisions are stored, no acceptance events are appended, and no result files are accepted as evidence.
- Tests for valid strict footer and invalid alias/footer shapes.
- `git diff --check`

## Exit Criteria

- Normal workflow has no mandatory claim command.
- Job statuses are `queued`, `completed`, and `failed`.
- Failed jobs append no acceptance events.
- Live finalization uses strict result parsing.
- Phase 4 docs/ADR tasks are revised to match the exact public surface after this phase.
- Cleanup gate is complete; no unowned claim/running/salvage/permissive-parser leftovers remain.
