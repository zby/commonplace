# Review system simplification implementation plan

## Goal

Reduce review-system code and workflow complexity while preserving the parts that are doing real work:

- SQLite-owned freshness and acceptance state
- note/gate snapshots independent of Git
- path-keyed `(note_path, gate_path, model_partition)` review identity
- completed review evidence for acknowledgement and warning selection

This workshop starts from the code review performed on 2026-07-01. The review subsystem tests were passing at that point: `pytest test/commonplace/review` reported `120 passed`.

## Baseline

Captured so "reduce code" is measurable and cannot be satisfied by shuffling lines between the library and CLI layers.

- Production: **5,345 lines** across ~40 files - `review/` 4,045 + `cli/review/` 1,300.
- Tests: **4,322 lines** in `test/commonplace/review/` - nearly 1:1 with production.
- Largest module: `review_db.py` at **1,066 lines**.

Per-module starting counts for the surfaces the phases touch, so each phase's Expected Delta is checkable at exit:

| Module | Lines | Cut by |
|---|---|---|
| `review/review_db.py` | 1,066 | Phase 2 (path/status fields), Phase 3 (claim/status helpers) |
| `cli/review/create_review_jobs.py` | 358 | Phase 2 (payload) |
| `review/job_output.py` | 251 | Phase 1 (finalization collapse) |
| `review/artifacts.py` | 242 | Phase 2 (derived path helpers) |
| `review/protocol/decisions.py` | 235 | Phase 3 (strict parser) |
| `review/batch.py` | 181 | Phase 2 (derived prompt/manifest paths) |
| `review/protocol/parser.py` | 146 | Phase 3 (salvage removal) |
| `review/job_finalization.py` | 136 | Phase 1 (finalization collapse) |
| `cli/review/migrations/repair_model_partitions.py` | 104 | Phase 4 (dead surface) |
| `review/finalization.py` | 101 | Phase 1 (finalization collapse) |
| `cli/review/claim_review_job.py` | 81 | Phase 3 (claim removal) |
| `review/freshness.py` | 69 | Phase 1 (absorbs `domain/`, so net may grow) |
| `review/domain/staleness.py` + `snapshots.py` | 49 | Phase 1 (folded into freshness) |

Implementation should report line deltas against this baseline. Test reduction counts as part of the win when tests only preserve internal scaffolding that is being removed.

## Target Decisions

### Keep

- SQLite review store.
- Snapshot-backed freshness independent of Git.
- `acceptance_events` as the accepted-baseline source of truth.
- Review identity as `(note_path, gate_path, model_partition)`.
- Worker-owned `bundle-output.md` and parent-owned finalization.
- `MANIFEST.json` as an inspectable artifact, if it remains cheap after path derivation.

### Cut

- Persisted artifact paths in the database.
- Mandatory `commonplace-claim-review-job`.
- `running` job state until there is a real scheduler with leases, heartbeats, or retry ownership.
- Partial salvage of completed pairs from failed multi-pair jobs.
- Permissive result parsing in the live finalizer.
- The three-module finalization chain.
- The `domain/` package as a parallel freshness vocabulary.
- One-shot model-partition repair/migration command if inventory confirms no current workflow depends on it.

### Defer

Do not add a new selector-plus-create convenience command in the first implementation tranche. The selector JSON pipe is awkward, but a new command can add surface area before the state model is simpler. Revisit it after the state and finalization cuts land.

Do not implement the structured-output codec in this pass. Strict markdown parsing is enough to remove the current free-text fallback chain from live finalization.

## Target Workflow

Planned normal workflow:

1. `commonplace-review-target-selector --json`
2. `commonplace-create-review-jobs --input -`
3. worker reads derived `prompt.md` and writes derived `bundle-output.md`
4. `commonplace-finalize-review-job --review-job-id {id} [--runner {worker} --model {model} --effort {effort}]`

Finalization-time provenance is optional. When supplied, finalization validates `build_model_partition(--model, --effort)` against the job's `model_partition` and records `runner`, `runner_model`, and `runner_effort` in the same transaction that completes the job.

## Target Storage Shape

The schema remains current-only: recreate incompatible stores rather than migrate in place.

`review_jobs` should retain only state that is not derivable from job id or child rows:

- `review_job_id`
- `model_partition`
- nullable finalization provenance: `runner`, `runner_model`, `runner_effort`, `telemetry_json`
- `created_at`, `completed_at`
- `status`: `queued`, `completed`, `failed`
- `failure_reason`
- `packing`: `note`, `gate`

Remove from `review_jobs`:

- `started_at`
- `prompt_path`
- `bundle_output_path`

`review_pairs` should retain request identity, snapshots, and completed review outcome:

- `review_pair_id`
- `review_job_id`
- `note_path`
- `gate_path`
- `pair_ordinal`
- `decision`
- `reviewed_note_snapshot_id`
- `reviewed_gate_snapshot_id`
- `reviewed_at`

Remove from `review_pairs` (both by end of Phase 3):

- `pair_status`
- `result_path` (in Phase 2, with the other path columns)

Pair status becomes derived:

- job `queued` and `decision IS NULL` -> pending
- job `completed` and `decision IS NOT NULL` -> completed
- job `failed` -> failed at the job level; no pair is accepted

This derived rule *is* all-or-nothing: once "job failed -> no pair accepted" holds, partial salvage is already gone. Removing the `pair_status` column and cutting salvage are therefore coupled and must land together. **Decision: Route B** — both stay through Phase 2 (a paths-only phase) and are cut together in Phase 3 with the rest of the acceptance-semantics changes. This avoids the broken middle state where the column is gone but finalization still tries to accept a partial subset from a failed job.

The `decision` enum currently includes `unknown`, which exists only to hold the permissive parser's fallback. Once live parsing is strict (Phase 3), no new row can be `unknown`; drop it from the schema `CHECK` in the same phase, since the store is schema-current and not migrated.

Artifact paths become pure functions:

- job dir: `kb/reports/bundle-reviews/review-job-{review_job_id}/`
- prompt: `{job_dir}/prompt.md`
- bundle output: `{job_dir}/bundle-output.md`
- note-packed result: `{job_dir}/{gate_leaf}.md`
- gate-packed result: `{job_dir}/{note_filename}.md`, disambiguated with existing note-filename logic

## Finalization Semantics

Finalization becomes all-or-nothing:

1. load the job and expected pairs
2. reject `completed` and `failed` jobs
3. read the derived `bundle-output.md`
4. strictly parse all expected pair blocks
5. fail the job if any expected pair is missing, duplicated, malformed, or has no strict result footer
6. validate/write all derived per-pair result artifacts
7. mark all pairs completed with decisions
8. append acceptance events for every pair
9. mark the job completed
10. refresh `MANIFEST.json` for inspection

On parse or coverage failure, mark the job failed and append no acceptance events. This intentionally removes the mixed state where completed pairs are accepted from a failed job.

Strict live result format:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
```

The live finalizer should not infer decisions from severity bullets, "flagging as", revised verdicts, bold first lines, or `INFO`/`OK` aliases. If historical parsing remains useful, keep it behind an explicitly named legacy helper or test fixture path, not in live finalization.

## Sequential Phase Files

The phase files are separate so each implementation pass has a focused brief. They are **not independent work packages**. Implement them in order, and revise later phase files after each earlier phase lands. Later files are planning forecasts until their prerequisite phases have updated the code and tests.

1. [Phase 1 - inventory and consolidation](./phase-1-inventory-and-consolidation.md)
2. [Phase 2 - derived paths and schema](./phase-2-derived-paths-and-schema.md)
3. [Phase 3 - finalization behavior](./phase-3-finalization-behavior.md)
4. [Phase 4 - public surface and closeout](./phase-4-public-surface-and-closeout.md)

Revision protocol:

- At the end of each phase, update the next phase file with what changed, what assumptions broke, and which tests now encode the new shape.
- Do not force later phase instructions to remain consistent with pre-implementation guesses if earlier work reveals a simpler route.
- Keep the target decisions in this overview stable unless implementation shows one is wrong. If that happens, record the change explicitly before proceeding.

## Phase Cleanup Gate

Every phase must end with a cleanup pass before it is considered complete. This is not optional: stale names, dead tests, old command docs, unused imports, and obsolete workshop assumptions will confuse later agents.

Minimum cleanup checklist for every phase:

- Remove or rewrite tests that only protect behavior intentionally removed in that phase.
- Remove dead modules, imports, entry points, helper functions, fixtures, docs, and generated references introduced or made obsolete by the phase.
- Run targeted `rg` sweeps for old names changed by the phase and either remove each hit or mark it explicitly as historical/deferred.
- Update the next phase file before stopping, so it reflects the new code shape and no longer asks later agents to rediscover already-settled facts.
- Update this overview if a target decision changed.
- Record any intentionally retained leftover with a reason and an owner phase; unowned leftovers are not allowed.

## Deferred Follow-Up

Revisit after the first implementation lands:

- Selector JSON and job creation consolidation. A direct `commonplace-prepare-review-jobs` command may still be worth it, but only after the state model is simpler.
- `MANIFEST.json` retention. If it is still mostly duplicate after path derivation, either shrink it or remove it.
- Structured output codec. Strict markdown parsing is the near-term simplification; schema-validated output is a separate harness capability decision.
- Full test-suite reshaping. After behavior cuts, consolidate fixture builders so review tests do not recreate mini repos and DB rows in several incompatible ways.

## Non-Goals

- Do not remove SQLite-backed review state.
- Do not return freshness to Git.
- Do not rekey history on note moves.
- Do not build generic lineage storage in this pass.
- Do not add a model runner or subprocess dispatcher.
- Do not preserve command compatibility solely for old review stores; the review DB remains schema-current.

## Completion Checklist

- New normal workflow has one fewer command: no mandatory claim step.
- `review_jobs` no longer stores artifact paths or `started_at`.
- `review_pairs` no longer stores artifact paths or pair-level missing state.
- Failed jobs append no acceptance events.
- Live finalization uses strict result parsing.
- `domain/` package is gone.
- Finalization path is readable from one module.
- Dead migration/repair surface is gone or explicitly justified.
- Each phase has completed its cleanup gate before the next phase begins.
- Review subsystem production and test line counts are lower than the baseline.
- `pytest test/commonplace/review` passes after each phase; full `pytest` passes before closing.
