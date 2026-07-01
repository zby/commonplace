# Phase 1 - inventory and consolidation

## Position

First phase. This phase is the only phase intended to run from the original code shape. Later phase files are provisional until this phase updates them.

## Purpose

Confirm the deletion targets, classify tests, and simplify module navigation before changing schema or public behavior.

## Scope

This phase combines the old inventory/safety phase with behavior-preserving consolidation:

- usage inventory
- test scaffolding audit
- `domain/` fold into freshness
- finalization module-chain collapse
- minimal shared CLI helpers only where touched

Do not remove persisted artifact paths, claim state, partial salvage, or permissive parsing in this phase. Those are later behavior cuts.

## Tasks

### Inventory

- Search docs, scripts, tests, and package entry points for:
  - `prompt_path`
  - `bundle_output_path`
  - `result_path`
  - `pair_status`
  - `commonplace-claim-review-job`
  - `running`
  - `repair-model-partitions`
  - direct imports of `job_output.py`, `job_finalization.py`, and `domain/`
- Check whether `src/commonplace/cli/review/migrations/repair_model_partitions.py` is still used after the migration baseline was squashed at `c2497e16`.
- Record updated production/test line counts before code edits.

Note: stored path/status behavior is asserted outside `test/commonplace/review/`. The relocation CLI tests also seed and assert these columns and must be in scope:

- `test/commonplace/cli/relocation_review_helpers.py` seeds `running`, `started_at`, `prompt_path`, `bundle_output_path`, and `result_path`.
- `test/commonplace/cli/test_relocate_note.py` asserts persisted artifact paths (`prompt_path`, `bundle_output_path`, `result_path`).
- `test/commonplace/cli/test_relocate_directory.py` asserts persisted artifact paths across multiple jobs.

### Test Audit

Classify review **and review-adjacent CLI** tests as:

- public behavior tests to keep
- internal-scaffolding tests to delete or rewrite when later phases remove the scaffolding
- migration/repair tests that depend on dead command surface

Audit both `test/commonplace/review/` and the relocation tests listed above. Specifically flag tests that mutate or assert stored `prompt_path`/`bundle_output_path`/`result_path`, seed or assert `running`/`started_at`/claim behavior, or assert partial salvage from failed jobs. The relocation tests seed jobs directly through `review_db`, so their `create_job_with_pairs` calls will break in phase 2 when `started_at`/`status='running'` and the path columns go away — record now which assertions become obsolete versus which need rewriting to derived paths.

### Freshness Vocabulary Consolidation

- Move `src/commonplace/review/domain/snapshots.py` and `src/commonplace/review/domain/staleness.py` into `freshness.py` or a single adjacent freshness module.
- Repoint `review_target_selector.py`.
- Delete the `domain/` package if it has no consumers.

### Finalization Module Consolidation

Collapse:

- `job_finalization.py`
- `job_output.py`
- `finalization.py`

into one readable `finalization.py`, with named internal sections:

- preconditions and output loading
- bundle parsing call
- artifact writes
- DB completion/acceptance
- manifest refresh
- failure marking

Keep `fail_active_review_jobs` reachable for prompt-render failure handling, either in `batch.py` or as a helper in the consolidated finalization module.

### Minimal CLI Helper Extraction

Extract helper code only when it reduces repetition in files already being touched. Avoid adding a broad review CLI framework in this phase.

## Outputs

- Inventory notes in this file or a short sibling note.
- Updated later phase files if inventory changes their assumptions.
- Behavior-preserving code consolidation.

## Phase 1 Implementation Notes

Implemented on 2026-07-01.

### Inventory Result

- Direct production imports of `commonplace.review.domain`, `job_output`, and `job_finalization` were removed.
- `src/commonplace/review/domain/` no longer has live source files; `NoteSnapshot`, `GateSnapshot`, `AcceptanceSnapshot`, `Staleness`, and `classify_staleness` now live in `src/commonplace/review/freshness.py`.
- `src/commonplace/review/job_output.py` and `src/commonplace/review/job_finalization.py` were deleted. Their behavior moved into `src/commonplace/review/finalization.py`.
- `commonplace-finalize-review-job` now imports `finalize_review_job_from_owned_output` from `commonplace.review.finalization`.
- `batch.py` now imports `fail_active_review_jobs` from `commonplace.review.finalization`.
- `commonplace-repair-model-partitions` remains live only as a package entry point, command docs/architecture docs, and `test/commonplace/review/test_repair_model_partitions.py`. No current workflow code imports it. This supports deleting the command in phase 4 if no external use is intentionally retained.

Behavior intentionally retained for later phases:

- persisted `prompt_path`, `bundle_output_path`, and `result_path`
- `pair_status`
- `running` and `started_at`
- `commonplace-claim-review-job`
- partial salvage from failed multi-pair finalization
- permissive live result parsing and `unknown`

Line counts after phase 1:

- Production review Python: **5,326 lines** across **34 files** (`src/commonplace/review/` + `src/commonplace/cli/review/`), down from 5,345 lines.
- Review tests: **4,322 lines** across **14 files** (`test/commonplace/review/`), unchanged.

The phase 1 line reduction is small because the deleted modules were folded into the single finalization module rather than behavior being removed.

### Test Audit Result

Public behavior tests to keep, with expected rewrites as state simplifies:

- `test/commonplace/review/test_review_batch.py` covers job creation, prompt artifacts, finalization success/failure, and manifest behavior. Keep the workflow coverage, but phase 2 must rewrite stored path assertions and delete/rewrite tests that mutate `result_path`.
- `test/commonplace/review/test_review_jobs_live_and_direct.py` covers public command wiring and end-to-end job behavior. Keep the create/finalize workflow coverage, but phase 2 must rewrite path payload/DB assertions and phase 3 must replace claim-specific provenance checks with finalization-time provenance checks.
- `test/commonplace/review/test_review_target_selector.py`, `test_ack_trivial_note_changes.py`, `test_warn_selector.py`, and `test_prune_superseded_reviews.py` cover public selector/ack/warn/prune behavior. Keep the behavior coverage, but rewrite fixture setup that seeds `running`/`started_at` once those fields disappear.
- `test/commonplace/cli/test_relocate_note.py` and `test/commonplace/cli/test_relocate_directory.py` are review-adjacent public behavior tests. Keep relocation behavior coverage, but phase 2 must remove direct persisted artifact-path assertions and update their `review_db` fixture setup.

Internal scaffolding tests to delete or rewrite in later phases:

- `test_review_batch.py::test_finalize_review_job_artifact_write_failure_does_not_accept_review` and `test_finalize_review_job_validates_all_result_paths_before_writing` mutate stored `result_path`; delete or replace with derived-path traversal checks in phase 2.
- `test_review_jobs_live_and_direct.py::test_finalize_review_job_uses_job_owned_paths_and_writes_provenance_frontmatter` mutates `bundle_output_path` and `result_path`; split the durable provenance/frontmatter assertion from the custom-path behavior, then remove the custom-path half in phase 2.
- `test_review_batch.py::test_finalize_review_job_salvages_partial_output` asserts partial salvage and one acceptance event from a failed job; delete or invert when all-or-nothing finalization lands in phase 3 (Route B keeps salvage until then).
- `test_review_jobs_live_and_direct.py::test_finalize_review_job_finalizes_running_job`, the claim tests, and any tests expecting `started_at`/`running` become phase 3 rewrites or deletions when claim/running disappear.
- Parser fallback tests in `test_review_decision_parser.py` and permissive parsing expectations in `test_review_protocol.py` are phase 3 candidates for deletion or quarantine under an explicit legacy parser.

Migration/repair tests that depend on dead command surface:

- `test/commonplace/review/test_repair_model_partitions.py` depends on `commonplace-repair-model-partitions` and should be deleted with the command in phase 4 if the phase 1 inventory result remains accepted.

### Consolidated Module Handoff

The finalization code now has these phase-relevant entry points in `src/commonplace/review/finalization.py`:

- `finalize_review_job_from_owned_output` — public library operation behind `commonplace-finalize-review-job`
- `FinalizeReviewJobOutcome` — CLI payload/exit-code wrapper
- `finalize_job_bundle_markdown` and `finalize_job_from_parsed` — bundle parsing and orchestration
- `record_and_finalize_job` / `complete_pairs_and_finalize_job` — DB completion and acceptance
- `write_finalized_job_artifacts` / `write_job_manifest_from_db` — artifact writes and manifest refresh
- `fail_active_review_jobs` / `fail_job_for_bundle_parse_error` — failure marking

No compatibility wrappers were retained for `job_output.py`, `job_finalization.py`, or `commonplace.review.domain`.

## Cleanup Gate

Before ending this phase:

- Delete the old `domain/` package files if they have no live imports.
- Remove or update all imports of `commonplace.review.domain`, `job_output`, and `job_finalization`.
- Remove stale references to the old finalization module split from docs or tests touched in this phase.
- Update phase 2 with the actual finalization module/function names produced by this phase.
- Update phase 3 if the consolidation changes where provenance, parser, or failure handling code now lives.
- Record any retained compatibility alias or wrapper with a deletion reason and target phase.

## Verification

- `pytest test/commonplace/review test/commonplace/cli/test_relocate_note.py test/commonplace/cli/test_relocate_directory.py` — covers the review-adjacent relocation tests that assert stored path/status columns.
- `rg "commonplace.review.domain|job_output|job_finalization" src test` should show no live imports after consolidation, except historical workshop text if any.
- `git diff --check`

## Exit Criteria

- Review tests pass.
- Later phase files have been revised to reflect the new module layout.
- The test audit identifies which tests are expected to disappear or need rewriting in phases 2 and 3, including the relocation CLI tests.
- Cleanup gate is complete; no unowned compatibility wrappers or stale imports remain.
