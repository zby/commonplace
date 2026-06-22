---
description: Plan for replacing the old note-scoped review implementation with a clean review-run plus review-pairs model
status: draft
---

# Review Pairs Clean Migration Plan
## Goal
Replace the current note-scoped review implementation with a clean model:

- `review_runs` is one review invocation, equivalent to one prompt/run directory.
  
- `review_pairs` is one requested `(note_path, gate_id)` pair inside a run.
  
- There is no compatibility layer for `review_run_gates` or `gate_reviews`.
  
- New code, tests, docs, and migration scripts use only the new schema names.
  
- Retire commands that only exist to support old manual or repair paths unless there is a clear current workflow for them.
  

This is a breaking migration. The codebase has no external compatibility promise, so the implementation should remove the old tables and old DB APIs instead of preserving aliases.
## Target Schema
`review_runs`:

- `review_run_id INTEGER PRIMARY KEY`
  
- `model_id TEXT NOT NULL`
  
- `runner TEXT NOT NULL`
  
- `started_at TEXT NOT NULL`
  
- `completed_at TEXT`
  
- `status TEXT NOT NULL CHECK (status IN ('running', 'completed', 'failed'))`
  
- `failure_reason TEXT`
  
- `telemetry_json TEXT`
  
- `raw_bundle_markdown TEXT`
  
- `debug_log TEXT`
  
- `packing TEXT NOT NULL CHECK (packing IN ('note', 'gate', 'manual-import'))`
  

Do not keep `note_path`, `reviewed_note_sha`, or `reviewed_note_commit` on `review_runs`. Those are pair-level facts.

`review_pairs`:

- `review_pair_id INTEGER PRIMARY KEY`
  
- `review_run_id INTEGER NOT NULL REFERENCES review_runs(review_run_id) ON DELETE CASCADE`
  
- `note_path TEXT NOT NULL`
  
- `gate_id TEXT NOT NULL`
  
- `model_id TEXT NOT NULL`
  
- `pair_ordinal INTEGER NOT NULL`
  
- `pair_status TEXT NOT NULL CHECK (pair_status IN ('pending', 'completed', 'missing'))`
  
- `decision TEXT CHECK (decision IN ('pass', 'warn', 'fail', 'error', 'unknown'))`
  
- `rationale_markdown TEXT`
  
- `evidence_json TEXT`
  
- `gate_sha TEXT NOT NULL`
  
- `reviewed_note_sha TEXT NOT NULL`
  
- `reviewed_note_commit TEXT`
  
- `reviewed_at TEXT`
  
- `review_kind TEXT NOT NULL CHECK (review_kind IN ('full-review', 'manual-import'))`
  

Constraints and indexes:

- `UNIQUE (review_run_id, note_path, gate_id)`
  
- `UNIQUE (review_run_id, pair_ordinal)`
  
- index `(note_path, gate_id, model_id)`
  
- index `(review_run_id)`
  
- index `(pair_status)`
  
- optional index `(reviewed_note_sha)` if selector/repair code still needs it
  

Important correction to the workshop migration prototype: do not use `UNIQUE (review_run_id, gate_id)`. That prevents gate-packed runs, where many notes share one gate in the same review run.

`pair_ordinal` is the stable zero-based position of the pair inside the review-run prompt. It preserves prompt/result order independently from note path or gate id. For note-packed runs it usually follows the gate order for one note; for gate-packed runs it follows the note order for one gate.

`pair_status` is intentionally not a run-status clone:

- `pending` means the pair was requested in a run that has not finalized yet.
  
- `completed` means the pair has stored output and can be accepted.
  
- `missing` means the pair was requested but has no completed output after finalization. This includes parser salvage cases and failed legacy runs with no pair output. The run-level failure reason stays on `review_runs.failure_reason`.
  

`acceptance_events`:

- keep the existing acceptance event concept
  
- rename primary key to `acceptance_event_id`
  
- replace `accepted_review_id` with `accepted_review_pair_id REFERENCES review_pairs(review_pair_id) ON DELETE SET NULL`
  
- keep freshness columns: `note_path`, `gate_id`, `model_id`, accepted note/gate shas, accepted timestamp, acceptance kind
  

Views:

- `current_gate_acceptances` should expose `accepted_review_pair_id`
  
- `stale_gate_pairs` remains acceptance-driven and gate-local
  

Remove from the live schema:

- `review_run_gates`
  
- `gate_reviews`
  

Do not keep compatibility views with those names. They will hide incomplete migrations and keep old mental models alive.
## Migration Strategy
0. Treat the revised workshop migration script as a prerequisite before the production code rewrite:

- script: `kb/work/create-review-runs/scripts/migrate_review_pairs.py`
  
- migrated scratch DB: `kb/work/create-review-runs/db-scratch/review-store-gate-packed-migrated.sqlite`
  
- verified on the live DB copy: `PRAGMA foreign_key_check` clean, `PRAGMA integrity_check` ok
  
- verified counts:
  
  - legacy `review_runs`: 2103
    
  - inferred note-packed runs: 1540
    
  - inferred gate-packed invocations: 114, collapsed from 563 legacy single-gate run rows
    
  - manual-import synthetic runs: 2507
    
  - migrated `review_runs`: 4161
    
  - migrated `review_pairs`: 10371
    
  - migrated `acceptance_events`: 8951
    
  - current accepted gate-packed pairs preserved under `packing='gate'`: 543
    
  - lost full-review/manual-import acceptance mappings: 0
    
  - gate-packed legacy `raw_bundle_markdown` rows preserved in aggregated run-level audit text: 543
    
  - gate-packed legacy `debug_log` rows preserved in aggregated run-level audit text: 59
    
  - divergent gate-packed legacy `telemetry_json` groups preserved as valid JSON aggregation objects: 1
    

1. Copy or back up `kb/reports/review-store.sqlite`.
  
2. Run preflight cleanup on the old DB before schema migration:
  

- prune superseded completed reviews if we still want that cleanup before the move
  
- prune superseded unknown manual imports if still needed
  
- repair manual-import decisions if still needed
  
- reparse decisions if parser changes are pending
  

3. Run a one-shot destructive schema migration:
  

- rename old tables to `legacy_review_runs`, `legacy_review_run_gates`, `legacy_gate_reviews`, `legacy_acceptance_events`
  
- create new `review_runs`, `review_pairs`, `acceptance_events`, views, and `review_schema_migrations`
  
- infer legacy packing before creating new invocation rows:
  
  - `packing='gate'` for groups of legacy runs where each run has exactly one gate and the group shares `(started_at, runner, model_id, gate_id)` with at least one sibling
    
  - `packing='note'` for all remaining legacy full-review runs
    
  - `packing='manual-import'` for synthetic runs created from old manual-import `gate_reviews` rows without a parent run
    

- create `legacy_review_run_map(legacy_review_run_id, review_run_id, inferred_packing)` so many legacy gate-sweep run rows can map to one new gate-packed review invocation
  
- create one new `review_runs` row per inferred note-packed run, one per inferred gate-packed group, and one per manual-import row
  
- for inferred gate-packed groups, aggregate legacy sibling `raw_bundle_markdown` and `debug_log` values under legacy run/note headers; keep identical `telemetry_json` as-is and preserve divergent telemetry as a valid JSON aggregation object
  
- copy old `review_run_gates` into `review_pairs` through `legacy_review_run_map`
  
- for gate-packed groups, assign `pair_ordinal` by legacy run order inside the inferred prompt group
  
- mark requested pairs without output as `pending` for running runs, otherwise `missing`
  
- merge matching old `gate_reviews` payload into those pairs and mark them `completed`
  
- create one completed `review_pairs` row for each synthetic manual import
  
- map `legacy_acceptance_events.accepted_review_id` through `legacy_gate_review_map` into `accepted_review_pair_id`
  

4. Verify:
  

- row counts match migration expectations
  
- `PRAGMA foreign_key_check` is clean
  
- no old table names are referenced by production code
  
- selectors return the same stale/current keys on a migrated scratch DB
  

5. Drop legacy tables only after scratch validation:
  

- `legacy_review_runs`
  
- `legacy_review_run_gates`
  
- `legacy_gate_reviews`
  
- `legacy_acceptance_events`
  
- `legacy_gate_review_map`
  
- `legacy_review_run_map`
  

If we want an audit trail, keep the migration script and the scratch report in the workshop, not legacy tables in the live DB.
## Code Rewrite Plan
### Phase 1: Schema And DB API
Rewrite `src/commonplace/review/review-schema.sql` first.

Rewrite `src/commonplace/review/review_db.py` around the new domain:

- `ReviewRunRow`
  
- `ReviewPairRow`
  
- `PendingReviewPair` or `PendingPairReview`
  
- `AcceptanceState` with `accepted_review_pair_id`
  
- `create_run(...)` creates only an invocation row
  
- `create_review_pairs(...)` inserts requested pairs
  
- `create_run_with_pairs(...)` is the high-level helper used by most callers
  
- `load_review_pairs_for_run(...)`
  
- `load_completed_review_pairs_for_run(...)`
  
- `complete_review_pair(...)` or `complete_review_pairs(...)`
  
- `mark_missing_pairs(...)`
  
- `append_acceptance_event(... accepted_review_pair_id=...)`
  
- `load_current_acceptances(...)`
  
- path/model relocation helpers updated to count/update `review_pairs` and `acceptance_events`, not note fields on `review_runs`
  

Delete old DB API:

- `ReviewRunGateRow`
  
- `GateReviewRow`
  
- `insert_review_run_gates`
  
- `load_review_run_gates`
  
- `insert_gate_review`
  
- `load_gate_reviews_for_run`
  
- `load_gate_reviews_for_note`
  
- any helper named around `gate_reviews`
  

Do not leave aliases.
### Phase 2: Finalization
Rewrite `src/commonplace/review/finalization.py`.

New finalization behavior:

- load requested pairs for the run
  
- optionally complete pairs from parsed review output
  
- fail if a requested pair has no completed output when finalizing a successful run
  
- mark run completed when all pairs are completed
  
- append one acceptance event per completed pair
  

The function names should match the new model. Prefer names like:

- `record_and_finalize_run`
  
- `complete_pairs_and_finalize_run`
  

Avoid names containing `gate_review`.
### Phase 3: Execution Paths
Update these together because they form one flow:

- `src/commonplace/review/run_review_bundle.py`
  
- `src/commonplace/review/run_gate_sweep.py`
  
- `src/commonplace/review/batch.py`
  
- `src/commonplace/review/bundle_ingest.py`
  
- `src/commonplace/review/executor.py`
  
- CLI wrappers under `src/commonplace/cli/review/`
  

Expected behavior:

- single-note bundle creates one run with `packing='note'` and many pairs
  
- gate sweep creates one run per prompt batch with `packing='gate'` and many pairs
  
- external batch prepare creates one run per prompt with `packing='note'` or `packing='gate'`
  
- external batch ingest accepts one `review_run_id`, not a list of run ids
  
- artifact directory is always `kb/reports/bundle-reviews/review-run-{review_run_id}/`
  
- manifest lists all pairs, DB `pair_status` values, and run-level failure context when present
  

Update `commonplace-prepare-review-batch` JSON output:

- return `review_run_id`
  
- return `pairs` with `review_pair_id`, `note_path`, `gate_id`, `status`, `result_path`
  
- return `prompt_path`, `bundle_output_path`, `manifest_path`
  
- do not return multiple `review_runs`
  

Update `commonplace-ingest-batch-output`:

- replace `--review-run-ids` with `--review-run-id`
  
- load expected pairs from the DB
  
- finalize pair records and manifest statuses; missing output becomes `pair_status='missing'`, while invocation failure remains `review_runs.status='failed'`
  
### Phase 4: Selectors, Acks, And Reporting
Update:

- `review_target_selector.py`
  
- `ack_trivial_note_changes.py`
  
- `warn_selector.py`
  
- `ack_gate_review.py`
  
- `relocation_hook.py`
  

Rules:

- selectors remain acceptance-driven
  
- warn selector reads completed `review_pairs`
  
- ack commands append acceptance events pointing to `review_pair_id` when there is a current accepted pair, or `NULL` for pure ack events if that remains the intended meaning
  
- relocation updates note paths in `review_pairs` and `acceptance_events`; it no longer updates `review_runs.note_path`
  
### Phase 5: Maintenance Commands
Retire or rewrite each command intentionally.

Retire now unless a current workflow proves otherwise:

- `commonplace-write-gate-review`
  
- `commonplace-finalize-review-run`
  
- `commonplace-repair-manual-import-review-results`
  
- `commonplace-prune-superseded-unknown-manual-import-reviews`
  
- `commonplace-reparse-gate-review-decisions`
  

Rationale:

- `write-gate-review` and `finalize-review-run` are old manual assembly tools. The live-agent path now uses bundle ingest, and the new pair model should not encourage hand-populating individual results outside the parser.
  
- manual-import repair and unknown pruning are one-time legacy cleanups. Run them before migration if needed, then remove them from shipped commands.
  
- reparse decisions is a one-time repair command. If we still want it, keep it as a workshop script, not an installed command.
  

Rewrite, not retire:

- `commonplace-prune-superseded-reviews`
  
- `commonplace-repair-model-partitions`
  

Rationale:

- pruning old non-current review history may still be useful, but it must operate on `review_pairs` and only delete whole artifact directories when all pairs in a run are obsolete
  
- model partition repair is still useful while runner telemetry can disagree with requested model ids
  

Possible simplification:

- Do not support deleting individual pair result files from a shared run directory in the first migration. If a run contains any retained pair, keep the whole directory. This is simpler and avoids artifact corruption.
  
### Phase 6: Docs And Installed Entrypoints
Update docs:

- `kb/reference/review-architecture.md`
  
- `kb/reference/commands.md`
  
- move `kb/instructions/REVIEW-SYSTEM.md` to `kb/reference/REVIEW-SYSTEM.md`
  
- `kb/instructions/run-review-bundle-on-note.md`
  
- workshop README
  

The review system document describes the shipped review architecture and command workflow, so it belongs in the descriptive reference collection rather than the prescriptive instructions collection. Update all links that point to the old `kb/instructions/REVIEW-SYSTEM.md` path as part of the move.


Update packaging entrypoints to remove retired commands.

Search production code, tests, and current operational docs after the migration:

```bash
rg "gate_reviews|review_run_gates|accepted_review_id" src test kb/instructions kb/reference/commands.md kb/reference/review-architecture.md kb/reference/REVIEW-SYSTEM.md
rg "review-batch" src test kb/instructions kb/reference/commands.md kb/reference/review-architecture.md kb/reference/REVIEW-SYSTEM.md
```

Expected exceptions only in migration/workshop files and explicitly historical records such as ADRs, proposals, and `kb/log.md`. Do not edit historical ADRs only to hide old names; update them only if their present-tense claims would mislead a reader.
### Phase 7: Tests
Rewrite tests by behavior, not by old table counts.

Core test coverage:

- schema creates `review_runs`, `review_pairs`, and `acceptance_events`
  
- `create-review-run --with-prompt` creates one run and multiple pairs
  
- `run-review-bundle` completes all pairs under one note-packed run
  
- `run-gate-sweep` creates one gate-packed run per prompt batch
  
- `prepare-review-batch` creates one run and manifest
  
- `ingest-batch-output` salvages missing pairs without creating secondary run dirs
  
- selector sees fresh/stale state from acceptance events
  
- warn selector reads warn pairs
  
- ack commands append acceptance events with `accepted_review_pair_id`
  
- relocation updates `review_pairs` and `acceptance_events`
  
- migration script converts a fixture DB and passes `foreign_key_check`
  

Delete or rewrite tests for retired commands.
## Retirement Checklist
Remove shipped CLI modules and entrypoints for retired commands:

- `src/commonplace/cli/review/write_gate_review.py`
  
- `src/commonplace/cli/review/finalize_review_run.py`
  
- `src/commonplace/cli/review/repair_manual_import_review_results.py`
  
- `src/commonplace/cli/review/prune_superseded_unknown_manual_import_reviews.py`
  
- `src/commonplace/cli/review/reparse_gate_review_decisions.py`
  

Remove tests that only exercise those retired commands.

Move any useful repair logic into workshop scripts if it still needs to run once before migration.
## Implementation Order
1. Add a fixture old-schema DB covering both legacy packing shapes:
  
   - a note-packed legacy run with one note and multiple gates
     
   - a gate-packed legacy group with two or more single-gate legacy runs sharing `(started_at, runner, model_id, gate_id)`
     

2. Add migration tests around the revised workshop script:
  
   - gate-packed legacy groups collapse to one new `review_runs` row with `packing='gate'`
     
   - `legacy_review_run_map` maps every old run and maps gate-packed sibling runs to the same new run
     
   - `legacy_gate_review_map` maps every old `gate_reviews` row to a `review_pairs` row
     
   - `acceptance_events.accepted_review_pair_id` preserves every full-review/manual-import acceptance mapping
     
   - `UNIQUE (review_run_id, note_path, gate_id)` and `UNIQUE (review_run_id, pair_ordinal)` hold
     

3. Replace `review-schema.sql`.
  
4. Rewrite `review_db.py` and schema tests.
  
5. Rewrite finalization.
  
6. Rewrite create/run/prepare/ingest flows.
  
7. Rewrite selector/ack/warn/relocation flows.
  
8. Rewrite or retire maintenance commands.
  
9. Update docs and command references.
  
10. Run full `pytest`.
  
11. Re-run the revised migration script against a fresh copy of the real DB and compare the results against the prereq counts above.
  
12. Apply migration to the live review DB only after scratch results and tests are clean.
  
## Acceptance Criteria
- No production code or current operational docs reference `gate_reviews`, `review_run_gates`, `accepted_review_id`, or `review-batch` as live interfaces. Historical ADR/proposal/log references may remain when clearly historical.
  
- No compatibility views or aliases exist for old table names.
  
- `commonplace-prepare-review-batch` returns one `review_run_id`.
  
- `commonplace-ingest-batch-output` accepts one `review_run_id`.
  
- Gate-packed runs can contain many notes with the same gate.
  
- Note-packed runs can contain many gates for the same note.
  
- Migrated historical gate sweeps are represented as `review_runs.packing='gate'`, not as multiple note-packed invocations.
  
- `legacy_review_run_map` maps all 2103 legacy runs; in the current live DB, 563 gate-packed legacy runs collapse into 114 gate-packed new runs.
  
- All 543 currently accepted historical gate-packed reviews remain accepted through `accepted_review_pair_id`.
  
- `review-run-{id}/MANIFEST.json` is the authoritative map from run to pair artifacts.
  
- Full review test suite passes.
  
- Migration on a copied real DB preserves expected counts and passes `PRAGMA foreign_key_check` and `PRAGMA integrity_check`.
