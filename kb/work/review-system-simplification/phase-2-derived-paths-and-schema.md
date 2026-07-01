# Phase 2 - derived paths and schema

## Position

Second phase. Revise this file after phase 1 lands, especially if finalization consolidation changes function boundaries or artifact helpers.

## Prerequisite

Phase 1 complete:

- no live `domain/` package
- finalization path consolidated
- test audit available
- current line-count baseline refreshed

## Purpose

Remove mutable artifact-path state and pair-level missing state from the database. Artifact paths become derived from `review_job_id`, `packing`, and pair identity.

## Scope

This phase changes schema and internal APIs but should preserve the visible review workflow as much as possible. Claim may still exist at the end of this phase. Permissive parsing may still exist at the end of this phase if removing it would make the change too large.

Partial salvage is coupled to the `pair_status` cut and cannot simply be deferred. Removing `pair_status` and adopting the derived rule "job failed -> no pair accepted" *is* the all-or-nothing behavior. So this phase must pick one of two consistent routes and record which:

- **Route A (cut salvage here):** remove `pair_status`, make finalization all-or-nothing now, and pull the salvage-specific tasks forward from phase 3 into this phase. Phase 3 then only handles claim/running removal and strict parsing.
- **Route B (keep salvage for now):** retain the `pair_status` column this phase so partial salvage keeps recording the completed subset, and defer both the column removal and the salvage cut to phase 3.

Do not produce the broken middle state: `pair_status` removed but finalization still trying to accept a partial subset from a failed job.

## Tasks

### Schema Cut

Update `review-schema.sql` to remove:

- `review_jobs.started_at`
- `review_jobs.prompt_path`
- `review_jobs.bundle_output_path`
- `review_pairs.result_path`
- `review_pairs.pair_status` **only under Route A** (see Scope). Under Route B, keep `pair_status` this phase and remove it in phase 3 alongside the salvage cut.

Also drop the `idx_review_pairs_pair_status` index whenever `pair_status` is removed.

Keep schema-current policy: incompatible review stores are recreated rather than migrated.

### DB Layer

- Update `ReviewJobRow`, `ReviewPairRow`, and `ReviewJobPlan`.
- Remove `set_job_artifact_paths`.
- Replace pair-status updates with derived status or job-level status.
- Remove or stage removal of `mark_missing_pairs` if phase 3 will still need it temporarily.
- Update list/load helpers so CLI payloads can still render useful derived paths.

### Artifact Helpers

Centralize derived path helpers in `artifacts.py`:

- job dir
- prompt path
- bundle output path
- result path per pair
- manifest path

Keep path traversal protection at artifact root and filename derivation boundaries.

### Callers and Tests

- Update `batch.py` to write prompt and manifest using derived paths.
- Update finalization to read/write derived paths.
- Update `_job_payload`, `review_job_list`, and manifest rendering.
- Delete or rewrite tests whose only purpose is mutating stored paths to exercise path-safety code.

## Expected Delta

Moderate production reduction, especially in:

- `review_db.py`
- `artifacts.py`
- finalization preconditions
- path-mutation tests

## Cleanup Gate

Before ending this phase:

- Run `rg "prompt_path|bundle_output_path|result_path|pair_status|set_job_artifact_paths|mark_missing_pairs" src test kb/reference kb/instructions kb/work/review-system-simplification`.
- For each hit, remove it, update it to the derived-path/status model, or mark it explicitly as historical/deferred.
- Delete tests and fixtures that only mutate now-removed path columns.
- Remove DB helper functions that only served removed columns.
- Update phase 3 with the actual derived-path helper names, row dataclasses, and status representation.
- Update phase 4 doc tasks if the public payload shape changed.

## Verification

- `pytest test/commonplace/review`
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
- Cleanup gate is complete; no unowned path/status leftovers remain.
