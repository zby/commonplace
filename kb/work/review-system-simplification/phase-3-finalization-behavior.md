# Phase 3 - finalization behavior

## Position

Third phase, revised after the phase 2 implementation. Phase 2 proved two constraints that shape this phase:

- `ReviewPairRow.result_path` is not pair-local. It is derived from the parent job id, the parent job's `packing`, and the complete pair set for the job. Code that needs result paths must stay job-scoped or consume `ReviewPairRow` values loaded through `review_db`; do not add `result_path` back to the schema and do not introduce a pair-only path helper.
- Finalization is already consolidated into `src/commonplace/review/finalization.py`. Treat that module as the baseline behavioral core. Do not recreate the old `job_output.py` / `job_finalization.py` split.

## Prerequisite

Phase 2 complete:

- artifact paths are derived
- schema no longer stores path fields (`started_at`, `prompt_path`, `bundle_output_path`, `result_path` gone)
- `pair_status`, `mark_missing_pairs`, `running`, and partial salvage are still present - Route B deferred them to this phase
- review tests pass

Current code baseline:

- `artifacts.py` owns derived job paths: `review_job_artifact_dir_rel`, `prompt_path_rel`, `bundle_output_path_rel`, `manifest_path_rel`, `result_path`, and `result_paths_by_pair_id`.
- `write_pair_result_files_to_derived_paths` writes per-pair artifacts from a job plus the job's full pair set.
- `ReviewJobRow` no longer carries path fields or `started_at`.
- `ReviewJobPlan` exposes derived `prompt_path` and `bundle_output_path`.
- `ReviewPairRow.result_path` is derived during DB loading from the parent job's packing and complete pair set.
- `attach_execution_data` currently writes `telemetry_json`, `runner_model`, and `runner_effort`; it does not write `runner`. Phase 3 must extend it or replace it with a finalization provenance helper.

## Purpose

Simplify the behavioral core of review execution:

- provenance is recorded at finalization time
- claim/running state disappears
- finalization is all-or-nothing
- live parsing is strict

## Scope

This phase intentionally changes public behavior. It should update tests as behavior changes. Update live operational instructions in this phase when a removed command would break an agent workflow; broader reference and ADR cleanup can wait for phase 4.

## Implementation Order

### 1. Finalization-Time Provenance

- Add optional `--runner`, `--model`, and `--effort` to `commonplace-finalize-review-job`. All three are optional.
- Flag contract:
  - `--effort` requires `--model`, because `build_model_partition(model, effort)` needs a model.
  - `--model` may be supplied without `--runner`; it validates and records model provenance.
  - `--runner` may be supplied alone; it records the runner without model partition validation.
  - `--effort` without `--model` is a `parser.error`, not a silent skip.
- When `--model` is supplied, validate `build_model_partition(--model, --effort)` against the job's `model_partition` before any state mutation.
- Thread provenance through `finalize_review_job_from_owned_output`, `finalize_job_bundle_markdown`, `finalize_job_from_parsed`, and the DB finalization function.
- Extend `attach_execution_data` to accept `runner`, or replace it with a finalization-focused helper that writes `runner`, `runner_model`, `runner_effort`, and `telemetry_json`. Keep telemetry support; it is not claim-specific.
- Record provenance in the same DB transaction that completes or fails the job. Provenance validation happens before mutation; provenance writing happens before job completion/failure.
- Smoke finalization with no provenance flags, with `--runner` only, with `--model`, and with `--model --effort`.
- Verify a model/effort mismatch fails before any job, pair, acceptance, or artifact state changes.

### 2. Remove Claim and Running

- Remove `commonplace-claim-review-job`.
- Remove the script entry point from `pyproject.toml`.
- Delete `src/commonplace/cli/review/claim_review_job.py`.
- Remove `review_db.claim_review_job`, `ReviewJobClaimError`, and claim-specific tests.
- Remove `running` from job status values and schema checks. The active finalizable state is `queued`; terminal states are `completed` and `failed`.
- Update `ACTIVE_REVIEW_JOB_STATUSES`, job-list filtering/descriptions, fixtures, and test helpers so they no longer seed or expect `running`.
- Move all dispatch provenance assertions from claim tests to finalization tests.
- Update live instructions that would otherwise invoke the removed command, especially `kb/instructions/run-review-batches.md` and the semantic-QA step in `kb/instructions/write-agent-memory-system-review/SKILL.md`. Leave historical ADR/reference explanation for phase 4 unless a current procedure would be broken.

### 3. All-Or-Nothing Finalization

Replace partial salvage with one job-level invariant:

- A pair is accepted only when its parent job is `completed` and the pair has a non-null strict decision.
- A queued job has no accepted pairs.
- A failed job has no accepted pairs, no pair decisions, and no acceptance events.

Do not replace `pair_status` with another persisted per-pair state. Pin the row/API shape explicitly to avoid accidentally recreating per-pair state:

- `ReviewPairRow` drops `pair_status` and gains **no** status-like replacement field — not `job_status`, not `display_status`. A pair row carries only request identity, snapshots, decision, and the derived `result_path`.
- Display status is computed at the rendering boundary (JSON payloads, `review_job_list`, manifest writing) from the parent job's status, which `ReviewJobRow`/`ReviewJobPlan` already carry. Do not thread a per-pair status field through those payloads.
- Derive display status from the parent job:
  - job `queued` -> pair display state `pending`
  - job `completed` -> pair display state `completed`
  - job `failed` -> pair display state `failed` or `not accepted`

Implementation details:

- Missing expected pairs are fatal for the whole job.
- Extra, duplicate, malformed, or empty pair blocks remain fatal for the whole job.
- Parse and coverage validation must finish before DB pair completion or acceptance events.
- Precompute every expected `ReviewPairCompletion` and every derived result path from the loaded job plan before mutating state.
- Keep all result-path work job-scoped by using `result_paths_by_pair_id` / `write_pair_result_files_to_derived_paths`; do not make finalization depend on pair-local path derivation.
- Validate every result path is repo-relative and inside the repo before completing pairs or appending acceptance events.
- **Refactor note — stop the current partial-salvage failure marking.** Today `record_and_finalize_job` completes pairs, appends acceptance events for the completed subset, *then* runs `_job_coverage_failure` and, on a miss, calls `mark_missing_pairs` + `fail_review_job` in the same committed transaction — so a failed job keeps acceptance events for its completed pairs. Invert this: run coverage/parse preflight *before* any `complete_review_pairs` or `append_acceptance_event` call. `record_and_finalize_job` and `complete_pairs_and_finalize_job` must no longer append-then-fail or call `mark_missing_pairs`; delete that path.
- Within the DB transaction, write provenance, complete all pair rows, append acceptance events, and complete the job only after all preflight checks have passed.
- Keep acceptance events after pair completion, but before commit, so DB rollback removes both together.
- **Enforce the evidence invariant at the boundary, not just by convention.** `current_gate_acceptances` currently trusts raw `acceptance_events`, and `append_acceptance_event` has no job-status guard, so a stray append would leak into freshness. Join `acceptance_events -> review_pairs -> review_jobs` in the `current_gate_acceptances` view and filter `review_jobs.status = 'completed' AND review_pairs.decision IS NOT NULL`. This is the authoritative guard (robust to any caller). Optionally also add a defensive non-null-decision check in `append_acceptance_event`; do not rely on a write-time status check alone, since the job flips to `completed` in the same transaction.

Failure handling separates the two artifact kinds:

- **Result files (evidence): fatal.** Write them only after all paths are prevalidated. If a filesystem write fails, roll back the DB transaction, then mark the job failed in a separate failure transaction, and append no acceptance events.
- **`MANIFEST.json` (display/debug): non-fatal.** Refresh it only *after* the DB completion transaction has committed. A manifest refresh failure must not fail an already-completed job — report it non-fatally (warn) and leave job state completed. The manifest must never become pipeline state.
- The evidence invariant is DB-owned: selectors must ignore artifacts from non-completed jobs.
- On parse, coverage, path, DB, or result-file failure (but not manifest failure), mark the job failed and leave pair decisions null.
- Remove `mark_missing_pairs` and all missing-pair status code paths.
- Drop the `review_pairs.pair_status` column and `idx_review_pairs_pair_status` index from `review-schema.sql`.
- Bump `REVIEW_SCHEMA_VERSION` and remove `idx_review_pairs_pair_status` from `EXPECTED_REVIEW_INDEXES` in `review_schema.py`.
- Update pruning and warning selection assumptions so accepted pairs come only from completed jobs. If warning selection reads result files through `ReviewPairRow.result_path`, ensure the row came from a completed job query.

### 4. Strict Live Parser

- Add a strict live decision parser and make `parse_pair_bundle` use it for live finalization.
- Require exactly one final result line inside each pair block:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
```

- Treat missing result lines, duplicate result lines, aliases, and conflicting result signals as parse failures.
- Remove live use of fallback inference from severity bullets, `INFO`/`OK`, `Verdict`, `Outcome`, revised result, flagging phrases, and bold first-line decisions.
- Delete fallback parser tests or move them under an explicit legacy parser if historical parsing is still useful. The live path must not call the legacy parser.
- Update prompt text to make aliases invalid in live output.
- Drop `unknown` from the `review_pairs.decision` `CHECK` enum in `review-schema.sql`. It existed only to hold permissive fallback output. Strict parsing never emits it, and the store is schema-current, so no legacy rows need it.
- Remove code paths that write, normalize, rank, or branch on `decision = 'unknown'` in live review storage. Non-live historical helpers may retain legacy `unknown` only if they are clearly named and isolated from finalization.

### 5. Artifact and Manifest Shape

- Remove `pair_status` from artifact protocols where it represents persisted state.
- If `MANIFEST.json` still displays per-pair status, compute it from job status during manifest writing rather than storing or reading it from `review_pairs`.
- Preserve derived `result_path` values in manifests for completed jobs. For failed jobs, either omit result paths or keep them only as expected display paths with clear failed job state; do not let failed-job paths become evidence.
- Keep provenance frontmatter in result files. It should reflect finalization-time `runner`, `runner_model`, and `runner_effort`.

## Expected Delta

Large test reduction from removing:

- claim/running tests
- partial salvage tests
- permissive live parser fixtures

Moderate production reduction in finalization, DB status helpers, CLI command surface, and parser code.

## Cleanup Gate

Before ending this phase:

- Structural sweep: `rg "claim-review-job|claim_review_job|running|started_at|missing pairs|mark_missing_pairs|pair_status" src test kb/reference kb/instructions kb/work/review-system-simplification`. Every in-scope hit must be removed, rewritten to finalization-time provenance/all-or-nothing behavior, or explicitly marked historical/deferred.
- Path-state sweep: `rg "prompt_path|bundle_output_path|result_path|set_job_artifact_paths" src test kb/reference kb/instructions kb/work/review-system-simplification`. `prompt_path`, `bundle_output_path`, and `result_path` may remain as derived paths, manifest display fields, or result-file frontmatter; no hit may imply persisted schema state.
- Parser-alias sweep, scoped to review parser/finalization surfaces only: `rg "INFO|OK|Verdict|Outcome|Revised result|flagging as|unknown" src/commonplace/review/protocol test/commonplace/review`. Do not run these generic words across the whole tree. Only live-parser and parser-test hits matter here.
- Delete the claim CLI module, pyproject entry, tests, and live operational docs.
- Delete partial-salvage tests and fixtures.
- Delete or quarantine permissive parser tests under an explicit legacy parser if historical parsing is retained.
- Update phase 4 with the exact public commands, flags, status values, parser rules, and retained legacy references after this phase.

## Verification

- `ruff check src/commonplace/review src/commonplace/cli/review test/commonplace/review`
- `pytest test/commonplace/review`
- `pytest test/commonplace/cli/test_relocate_note.py test/commonplace/cli/test_relocate_directory.py`
- Smoke finalization with no provenance flags.
- Smoke finalization with `--runner`.
- Smoke finalization with `--model --effort`.
- Smoke a model/effort mismatch: command fails and leaves job state unchanged.
- Smoke a two-pair job with one missing block: job fails, pair decisions remain null, no acceptance events are appended, and selectors do not treat any result files as evidence.
- Boundary test: an `acceptance_events` row whose parent job is not `completed` (or whose pair decision is null) does not surface through `current_gate_acceptances` / the selector.
- Tests for valid strict footer and invalid alias/footer shapes.
- `git diff --check`

## Exit Criteria

- Normal workflow has no claim command.
- Job statuses are `queued`, `completed`, and `failed`.
- `review_pairs` has no `pair_status` column.
- Failed jobs append no acceptance events and leave no pair decisions.
- Acceptance evidence is boundary-enforced: `current_gate_acceptances` excludes acceptance events from non-completed jobs and pairs with null decisions.
- `ReviewPairRow` carries no persisted or surrogate pair-status field; display status is computed from the parent job at render time.
- Manifest refresh failure does not fail an already-completed job.
- Live finalization uses strict result parsing.
- Finalization provenance is supplied through `commonplace-finalize-review-job`.
- Result path derivation remains centralized and job-scoped.
- Phase 4 docs/ADR tasks are revised to match the exact public surface after this phase.
- Cleanup gate is complete; no unowned claim/running/salvage/permissive-parser leftovers remain.
