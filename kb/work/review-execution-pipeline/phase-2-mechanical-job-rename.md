# Phase 2: Mechanical run→job rename

**Status: ready to implement.** This is the first remaining phase after [Phase 1](./phase-1-honest-job-state.md) landed and [ADR 033](../../reference/adr/033-honest-review-run-state.md) recorded the `queued` state, honest clock, and `user_version` migration substrate.

Phase 2 is deliberately mechanical: rename the persisted execution record from "run" to "job" while preserving Phase 1 behavior. The cutover should be complete: do not keep old command names, flags, JSON keys, manifest keys, helper names, prompt wording, generated artifact names, or current docs as compatibility surfaces. It should not add runner behavior, ack semantics, model-partition cleanup, or relocation policy.

It renames `review_runs` only. **It keeps `review_pairs`** and all pair vocabulary (`review_pair_id`, `pair_ordinal`, `pair_status`, `accepted_review_pair_id`). "Pair" is the load-bearing name for a `(note_path, gate_path)` target and stays aligned with the pair sentinel protocol, the prompt vocabulary, and [ADR 031](../../reference/adr/031-review-state-uses-run-owned-review-pairs.md). Only the `review_run_id` foreign-key column on `review_pairs` is renamed, because it names the retired "run" concept and now points at `review_jobs`.

## Why this is worth doing separately

The later queued-job pipeline should not be built on the run/job mismatch the design already knows is wrong: `runs` is retired in favour of `jobs` because "job" is the more common, more accurate execution noun. A separate rename phase makes the churn easy to review, gives every later slice the target vocabulary from the start, and keeps behavioral regressions easier to spot: if a test fails here, it should be because a reference was missed, not because execution semantics changed.

This phase also exercises the Phase 1 migration substrate with the simplest possible schema evolution after `user_version = 1`: one table rename, two column renames, and three index renames, without changing meaning.

`review_pairs` is left alone on purpose. Renaming it to `review_job_items` would trade a descriptive name (it *is* a note×gate pair) for a positional one, and would open a new storage-vs-protocol vocabulary seam exactly where Phase 2 is trying to close one — the sentinel protocol, ADR 031, and prompts all keep saying "pair." So only the run→job half of the rename is taken here.

## Scope

In scope:

- table rename: `review_runs` -> `review_jobs`;
- PK rename: `review_run_id` -> `review_job_id` on the renamed table;
- FK column rename on the child: `review_pairs.review_run_id` -> `review_job_id` (still referencing the renamed parent), including the two `UNIQUE (review_run_id, ...)` constraints that name it;
- index renames: `idx_review_runs_*` -> `idx_review_jobs_*`, and `idx_review_pairs_review_run_id` -> `idx_review_pairs_review_job_id`;
- canonical DB helper, dataclass, manifest, command-output, prompt wording, and test names that carry "run" updated to "job";
- public command entrypoints and flags that expose the old review-run vocabulary renamed with no backwards-compatible aliases;
- newly created artifact directories and manifests use `review-job-{id}` / `review_job_id`.

Out of scope:

- renaming `review_pairs`, `review_pair_id`, `pair_ordinal`, `pair_status`, or `accepted_review_pair_id` — all "pair" vocabulary stays;
- adding job-list, job-finalize, or queued-job runner behavior not present in the current commands;
- adding `runner_model`;
- dropping `review_pairs.model_partition`;
- making `accepted_review_pair_id` non-null;
- changing ack behavior;
- changing relocation behavior;
- changing the raw note/gate review-block delimiter grammar consumed by the parser. Public command payload ids and persisted metadata still switch to `review_job_id` in this phase.

No compatibility aliases are kept. In `pyproject.toml`, replace `commonplace-create-review-runs` with `commonplace-create-review-jobs`, mapped to `commonplace.cli.review.create_review_jobs:main`. Rename `src/commonplace/cli/review/create_review_runs.py` to `create_review_jobs.py`, and rename tests whose filenames encode review-run vocabulary (for example `test_review_runs_live_and_direct.py`). All current command flags that accept `--review-run-id` switch to `--review-job-id`; command help, JSON, and manifests use `review_job_id` (and keep `review_pair_id`). Commands whose names do not expose the old persisted vocabulary can remain only if their behavior stays unchanged and their help/output no longer uses review-run terminology. `commonplace-run-review-bundles` / `run_review_bundles.py` may remain because `run` is a verb there, not the persisted `review_run` identity.

The final grep boundary is live implementation surface, not all historical text. Old `review_run` / `review-run` strings may remain in migration code, migration fixtures/tests, historical stored artifact paths or manifests that are deliberately not rewritten, and historical ADR/proposal/workshop text that describes prior designs. Pair vocabulary is not "old" — it stays. Live code, public command surfaces, current reference docs, current tests, and newly generated artifacts should use job vocabulary.

## Target schema after Phase 2

Fresh stores initialize at `LATEST_REVIEW_SCHEMA_VERSION = 2`.

```sql
review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT NOT NULL,
    created_at TEXT NOT NULL,
    started_at TEXT,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('queued', 'running', 'completed', 'failed')),
    failure_reason TEXT,
    telemetry_json TEXT,
    bundle_output_path TEXT,
    packing TEXT NOT NULL CHECK (packing IN ('note', 'gate'))
)

review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    pair_status TEXT NOT NULL CHECK (pair_status IN ('pending', 'completed', 'missing')),
    decision TEXT CHECK (decision IN ('pass', 'warn', 'fail', 'error', 'unknown')),
    result_path TEXT,
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_at TEXT,
    UNIQUE (review_job_id, note_path, gate_path),
    UNIQUE (review_job_id, pair_ordinal)
)
```

`acceptance_events` is **unchanged**: it references neither `review_runs` nor `review_pairs` by a renamed name, and `accepted_review_pair_id` stays as-is. The null-ack backfill and `NOT NULL` constraint remain a later ack-provenance phase.

`prompt_path` remains manifest/command-output-only in this mechanical slice. Persisting it on `review_jobs` belongs to the later shared job-plan/job-creation slice.

Expected index names after Phase 2:

- `idx_review_jobs_model_partition_created` (renamed from `idx_review_runs_model_partition_created`);
- `idx_review_jobs_status` (renamed from `idx_review_runs_status`);
- `idx_review_pairs_review_job_id` (renamed from `idx_review_pairs_review_run_id`);
- `idx_review_pairs_note_gate_model_partition`, `idx_review_pairs_pair_status`, and the acceptance indexes keep their current names because their key columns do not change.

Views (`current_gate_acceptances`, `stale_gate_pairs`) are **unchanged**: neither references `review_runs` or `review_pairs`, and `stale_gate_pairs` correctly keeps its name because pairs are not renamed.

## Migration version 2

Migration 2 runs from a populated version-1 store. It must preserve row counts, IDs, statuses, timestamps, artifact paths, accepted snapshots, and nullable ack rows. Because the only objects carrying "run" are one table, one child column, and three index names — and no view or `acceptance_events` column is touched — this is a pure `ALTER` migration, not a table rebuild:

1. `ALTER TABLE review_runs RENAME TO review_jobs;`
2. `ALTER TABLE review_jobs RENAME COLUMN review_run_id TO review_job_id;`
3. `ALTER TABLE review_pairs RENAME COLUMN review_run_id TO review_job_id;`
4. Drop and recreate the three renamed indexes (`ALTER` does not rename indexes): `idx_review_runs_model_partition_created` -> `idx_review_jobs_model_partition_created`, `idx_review_runs_status` -> `idx_review_jobs_status`, `idx_review_pairs_review_run_id` -> `idx_review_pairs_review_job_id`.
5. Set `PRAGMA user_version = 2`.
6. Run the existing integrity checks: expected objects, row counts, and `PRAGMA foreign_key_check`.

Modern SQLite (3.25+) propagates `RENAME TO` / `RENAME COLUMN` into dependent foreign keys and the two `UNIQUE (review_run_id, ...)` constraints automatically, so the child FK and uniqueness survive without a rebuild. Confirm `legacy_alter_table` is off (the default). If any dependency makes a rename fragile in practice, fall back to the Phase 1 controlled rebuild helper. Do not silently disable foreign keys or skip the post-migration checks. Prove the chosen path on a v1 fixture with views, indexes, foreign keys, and both null and non-null acceptance rows.

Do not rewrite existing `bundle_output_path`, `result_path`, or manifest files during migration. Historical artifacts may still live under `review-run-{id}` and remain valid because paths are stored. New artifacts created after Phase 2 should use `review-job-{id}`.

## Code changes

Derive the exact rename map by grepping the current symbols rather than trusting the lists below — they are the intent, not a guaranteed-complete inventory. The rule is uniform: a name carrying `run` becomes `job`; a name carrying `pair` is left unchanged.

1. **Schema constants and migration runner**
   - bump `LATEST_REVIEW_SCHEMA_VERSION` to `2`;
   - update the expected table/index sets used by the integrity check (`review_jobs`, renamed indexes; `review_pairs`, views, and `acceptance_events` unchanged);
   - add migration function `2`;
   - update `review-schema.sql` to the target schema and refresh its header comment, which currently says `review_runs`;
   - update `init_db` bootstrap detection: no `review_jobs` and no `review_runs` means a fresh store; `review_runs` with `user_version` 0 or 1 is a legacy store to migrate; `review_jobs` means version 2+ schema. Never initialize a fresh v2 schema beside legacy `review_runs`.

2. **Canonical DB API**
   - rename the run row dataclass to `ReviewJobRow`; keep `ReviewPairRow`, but rename its `review_run_id` field to `review_job_id`;
   - rename run helpers: `create_run` -> `create_job`, `create_run_with_pairs` -> `create_job_with_pairs`, `load_review_run` -> `load_review_job`, `_review_run_from_row` -> `_review_job_from_row`, and any `..._for_run` helper to `..._for_job`;
   - keep pair helpers under their pair names (`create_review_pairs`, `complete_review_pairs`, `mark_missing_pairs`, `load_latest_completed_review_pair`, etc.), changing only `review_run_id` parameters/fields to `review_job_id`;
   - update SQL to select `review_job_id`.

3. **Compatibility boundary**
   - do not keep committed compatibility aliases for old helper names, command names, CLI flags, JSON keys, or manifest keys;
   - if temporary aliases are useful while editing locally, remove them before the phase is considered done;
   - keep old `run` names only where required to read or migrate version-1 stores and to test that migration.

4. **Execution and batch paths**
   - update `batch.py`, `executor.py`, `finalization.py`, `protocol/prompt.py`, `artifacts.py`, `run_review_bundles.py`, and `run_gate_sweep.py` to use the job helper names and the `review_job_id` column;
   - keep status behavior identical: prepared external work is `queued`, immediate subprocess work is `running`, finalization accepts `queued` or `running`;
   - preserve salvage behavior and artifact persistence;
   - `fail_active_review_runs` -> `fail_active_review_jobs`, preserving the active status set of `queued` plus `running`.

5. **Artifacts and command output**
   - rename manifest run-key names to `review_job_id` for newly written manifests, with `artifact_schema: review-job-prompt-v1`;
   - output `review_job_id` (and keep `review_pair_id`) from renamed commands;
   - rename top-level JSON container keys from `runs` to `jobs`; tests should assert the old `runs` key is absent from renamed command output;
   - switch current `--review-run-id` flags to `--review-job-id` with no old alias;
   - use `review-job-{id}` for newly created artifact directories;
   - preserve old stored artifact paths and result paths.

6. **Readers and maintenance tools**
   - update selector, warn selector, prune, ack, repair-model-partitions, relocation hooks, and tests to read `review_job_id` and the job helper names;
   - update repo-local scripts that touch review state directly (`scripts/move-reviews-to-subdir.py`, `scripts/review-problems-for-note.py`) or explicitly mark/delete them as historical if they are no longer live tools;
   - do not change their semantics in this phase.

7. **Docs**
   - update reference docs that describe the current schema to use `review_jobs` / `review_job_id` (keeping `review_pairs`);
   - update `kb/instructions/run-review-batches-on-note.md` and any committed manifest fixtures if they reference `review_run_id`;
   - leave older ADR text alone unless it has an explicit "current system" claim.

## Tests

- fresh DB initializes at `user_version = 2` with `review_jobs` and no `review_runs` table; `review_pairs` still exists;
- v1 DB migrates to v2 exactly once, preserving row counts and all primary key values;
- v1 migration fixture exercises views, indexes, foreign keys, nullable ack rows, and non-null accepted pair rows, then passes `PRAGMA foreign_key_check` after reopening the DB;
- migration preserves queued/running/completed/failed statuses, `created_at`, nullable `started_at`, `completed_at`, and artifact path values;
- migration preserves `review_pairs` rows, their renamed `review_job_id` FK values, and nullable `accepted_review_pair_id` ack rows;
- `PRAGMA foreign_key_check` is clean after migration; the two `UNIQUE (review_job_id, ...)` constraints still hold;
- create/prepare command JSON uses `review_job_id` (and still emits `review_pair_id`);
- old command names and old `--review-run-id` flags are absent, except in migration fixtures/docs about historical stores;
- new manifests use `artifact_schema: review-job-prompt-v1`, the `review_job_id` key, and new `review-job-{id}` artifact dirs;
- existing effective-review, warning selection, pruning, ack, and repair-model-partition behavior still passes;
- full `pytest` passes.

## Done when

Phase 2 is done when the persisted review *execution record* vocabulary is `job` everywhere in the live schema, canonical helpers, command names and flags, command JSON, prompt wording, current docs, and newly generated artifacts; `review_pairs` and all pair vocabulary are unchanged; existing review stores migrate from version 1 to version 2 without data loss; and no behavior beyond the mechanical rename has changed.
