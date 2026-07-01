# Phase 2 - derived paths and schema

Historical phase brief. This records the pre-phase state and implementation instructions at the time phase 2 ran; it is not current review-system documentation. Current behavior is recorded in `kb/reference/REVIEW-SYSTEM.md` and ADR 035.

## Position

Second phase. Revise this file after phase 1 lands, especially if finalization consolidation changes function boundaries or artifact helpers.

## Prerequisite

Phase 1 complete:

- no live `domain/` package
- finalization path consolidated in `src/commonplace/review/finalization.py`
- test audit available
- current line-count baseline refreshed

Phase 1 produced these names to build on:

- freshness vocabulary: `AcceptanceSnapshot`, `GateSnapshot`, `NoteSnapshot`, `Staleness`, and `classify_staleness` in `freshness.py`
- finalization entry point: `finalize_review_job_from_owned_output`
- bundle orchestration: `finalize_job_bundle_markdown` and `finalize_job_from_parsed`
- DB completion/acceptance: `record_and_finalize_job` and `complete_pairs_and_finalize_job`
- artifact/manifest writes: `write_finalized_job_artifacts` and `write_job_manifest_from_db`
- failure marking: `fail_active_review_jobs` and `fail_job_for_bundle_parse_error`

Do not look for `job_output.py`, `job_finalization.py`, or `commonplace.review.domain`; phase 1 deleted them without compatibility wrappers.

## Purpose

Remove mutable artifact-path state from the database. Artifact paths become derived from `review_job_id`, `packing`, and pair identity.

## Scope

This phase changes schema and internal APIs but should preserve the visible review workflow as much as possible. Claim, permissive parsing, and partial salvage all still exist at the end of this phase.

**Route decision: Route B.** `pair_status` and partial salvage are *not* touched here. Removing `pair_status` and adopting the derived rule "job failed -> no pair accepted" *is* the all-or-nothing behavior, so it belongs with the other acceptance-semantics changes in phase 3, not in this paths-only phase. This phase keeps `pair_status`, its index, `mark_missing_pairs`, and salvage exactly as they are.

Do not produce the broken middle state: `pair_status` removed while finalization still tries to accept a partial subset from a failed job. Keeping both together here (and cutting both together in phase 3) avoids it.

## Tasks

### Schema Cut

Update `review-schema.sql` to remove:

- `review_jobs.started_at`
- `review_jobs.prompt_path`
- `review_jobs.bundle_output_path`
- `review_pairs.result_path`

Keep `review_pairs.pair_status` and its `idx_review_pairs_pair_status` index — phase 3 removes them with the salvage cut (Route B).

Keep schema-current policy: incompatible review stores are recreated rather than migrated. This is only enforced if the schema version is bumped:

- Bump `REVIEW_SCHEMA_VERSION` in `src/commonplace/review/review_schema.py` (currently `1`).
- `EXPECTED_REVIEW_INDEXES` is unchanged this phase — none of the removed columns has an index. Phase 3 updates it when it drops `idx_review_pairs_pair_status`.
- Note integrity currently checks object *names*, not column sets, so without the version bump an old store with the old columns would still pass as current. The version bump is what forces recreation.

### DB Layer

- Update `ReviewJobRow`, `ReviewPairRow`, and `ReviewJobPlan` — including removing the `started_at` field.
- Remove `started_at` from `create_job`, `create_job_with_pairs`, the `_review_job_from_row` mapping, and `_job_plan_from_job`. Since `claim_review_job` is the only writer of `started_at` and it is removed in phase 3, do not preserve a `started_at` write path here.
- Update `claim_review_job` so it still moves a queued job to `running` and records runner/model provenance without writing `started_at` or checking persisted path columns. It should rely on derived artifact paths and return a plan/payload whose paths are derived for display.
- Remove `set_job_artifact_paths`.
- Leave `pair_status` handling and `mark_missing_pairs` unchanged — phase 3 owns their removal.
- Update list/load helpers so CLI payloads can still render useful derived paths.

### Artifact Helpers

Centralize derived path helpers in `artifacts.py`:

- job dir
- prompt path
- bundle output path
- result path per pair
- manifest path

The result-path helper needs the whole job pair set, not only one pair. Gate-packed result filenames use note filenames and must still disambiguate duplicate note basenames with the existing all-note-path logic.

Keep path traversal protection at artifact root and filename derivation boundaries.

### Callers and Tests

- Update `batch.py` to write prompt and manifest using derived paths.
- Update finalization to read/write derived paths.
- Update `_job_payload`, `review_job_list`, and manifest rendering. Drop the `"started_at"` key emitted by `create_review_jobs.py`.
- Update read paths such as `warn_selector` so accepted review text is loaded from the derived result path for the accepted pair, using the parent job's packing and complete pair set for filename derivation.
- Delete or rewrite tests whose only purpose is mutating stored paths to exercise path-safety code.
- Rewrite the relocation CLI tests flagged in phase 1 (`relocation_review_helpers.py`, `test_relocate_note.py`, `test_relocate_directory.py`): drop `started_at` seeding and assert derived paths instead of the removed `prompt_path`/`bundle_output_path`/`result_path` columns. Leave the `status='running'` seeding for now — `running` survives until phase 3.

## Expected Delta

Moderate production reduction, especially in:

- `review_db.py`
- `artifacts.py`
- finalization preconditions
- path-mutation tests

## Cleanup Gate

Before ending this phase:

- Run `rg "prompt_path|bundle_output_path|result_path|started_at|set_job_artifact_paths" src test kb/reference kb/instructions kb/work/review-system-simplification` (not `pair_status`/`mark_missing_pairs` — those are retained until phase 3).
- For each hit, remove it, update it to the derived-path/status model, or mark it explicitly as historical/deferred.
- Delete tests and fixtures that only mutate now-removed path columns.
- Remove DB helper functions that only served removed columns.
- Update phase 3 with the actual derived-path helper names, row dataclasses, and status representation.
- Update phase 4 doc tasks if the public payload shape changed.

## Verification

- `pytest test/commonplace/review test/commonplace/cli/test_relocate_note.py test/commonplace/cli/test_relocate_directory.py` — the relocation tests assert the removed path columns and must pass after rewrite.
- Manual smoke:
  1. create a one-pair job
  2. inspect derived `prompt.md`
  3. write derived `bundle-output.md`
  4. finalize
  5. verify selector reports the pair fresh
- `git diff --check`

## Exit Criteria

- No DB column stores prompt, bundle-output, or result artifact paths.
- No tests mutate DB path fields, because those fields no longer exist.
- Later phase files are revised for the actual derived-path helper names and status representation.
- Cleanup gate is complete; no unowned path or `started_at` leftovers remain. Retained `pair_status`, `mark_missing_pairs`, and `running` references are explicitly phase 3-owned.
