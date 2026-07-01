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
