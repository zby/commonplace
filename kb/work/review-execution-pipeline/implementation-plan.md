# Review execution queued-job implementation plan

## Purpose

Replace the current mix of subprocess review commands, live-agent preparation, batch preparation, batch ingest, and bespoke sweep parallelism with one queued-job pipeline:

```text
select stale targets -> create queued review jobs -> execute queued jobs -> finalize results
```

The output protocol remains keyed by `(note_path, gate_path)`. `model_partition` stays freshness and acceptance metadata, and generated per-pair review-result Markdown carries it in frontmatter.

## Design Decisions

### Jobs, not runs

Use **review job** as the canonical term for one persisted unit of review execution. Current code says `review_run`; the target schema and commands should say `review_job`.

Mechanical rename:

- `review_runs` -> `review_jobs`
- `review_run_id` -> `review_job_id`

Phase 2 starts with this mechanical rename. It may be its own commit, but it is the first Phase 2 slice so every new command, helper, migration, JSON shape, and test uses the target job vocabulary from the start. `review_pairs` and pair vocabulary stay because the pair is the load-bearing `(note_path, gate_path)` protocol unit. Do not introduce behavioral changes while this churn is in flight.

### Queue state lives on jobs

Do not add a separate queue table. The job status is enough.

Phase 1 already added these values to the current `review_runs` table. Phase 2 preserves them through the `review_runs` -> `review_jobs` rename.

```text
queued, running, completed, failed
```

Meanings:

- `queued`: prompt and pair rows exist; no worker has claimed execution.
- `running`: a subprocess worker has claimed the job.
- `completed`: all required pairs completed and accepted.
- `failed`: preparation, execution, parse, or coverage failed; salvaged completed pairs may still be retained per existing policy.

### Job timing must be honest

Phase 1 already replaced the old overloaded `started_at NOT NULL` clock on `review_runs` with:

```sql
created_at TEXT NOT NULL,
started_at TEXT,
completed_at TEXT
```

`created_at` is preparation time. `started_at` is worker claim/start time. Orchestrator-driven jobs may go `queued -> completed` with `started_at = NULL`. Phase 2 carries this shape forward into `review_jobs`.

### Parent/orchestrator is the DB writer

For the dominant live-agent/orchestrator path, sub-agents are pure file transducers:

```text
prompt_path -> bundle_output_path
```

They must not run `commonplace-*` commands or mutate review state. The parent creates jobs, delegates prompt files, and finalizes outputs. Therefore v1 does not need transactional multi-process claiming for the orchestrator path.

The subprocess runner can still mark jobs `running` because Commonplace owns that subprocess execution.

### Claiming and concurrency policy

V1 has no formal lease/timeout for orchestrator-driven jobs. The parent lists queued jobs, dispatches each prompt path once, and finalizes the job when the worker writes the job-owned output file. Manual recovery handles abandoned orchestrator jobs.

The subprocess runner claims jobs because Commonplace owns the worker process. Claiming is an atomic update:

```sql
UPDATE review_jobs
SET status = 'running', started_at = ?
WHERE review_job_id = ? AND status = 'queued'
```

If the update affects zero rows, another worker claimed or completed the job and the runner skips it.

Start with a sequential subprocess runner. When parallelism is reintroduced, use one SQLite connection per worker, set a `busy_timeout`, keep transactions short, and never hold a database transaction while a model process is running.

### Finalize reads the job-owned output path

The review job owns one canonical `bundle-output.md`. The finalization command should be:

```bash
commonplace-finalize-review-job --review-job-id 42
```

For v1, do not expose a path override. Recovery edits the job-owned `bundle-output.md` in place before finalization.

If a future recovery workflow needs a noncanonical path, add an explicit `--bundle-output` option then. Do not keep `--input-file bundle-output.md` in the v1 surface.

### Model partition is job metadata and artifact provenance

`model_partition` should live on:

- `review_jobs`
- `acceptance_events`
- generated per-pair review-result Markdown frontmatter

It should not be duplicated on `review_pairs`. Completed pairs inherit model through their job.

`model_partition` remains the freshness and acceptance key. Treat it as opaque; do not add a `model_partitions` table in Phase 2.

For the first version, do not store a separate runner-model column. Subprocess execution can pass the job's `model_partition` as the runner model argument and store only `runner` as execution provenance. If queued execution later needs to distinguish freshness partition from runner argument, add nullable `review_jobs.runner_model` in the runner phase or a later migration.

A future `model_partitions` registry may centralize aliases and runner defaults, but that is deferred to a proposal rather than implemented in this queue refactor: [model partition registry](../../reference/proposals/model-partition-registry.md).

Generated canonical per-pair result files should include frontmatter like:

```yaml
---
review_job_id: 42
review_pair_id: 101
note_path: kb/notes/example.md
gate_path: kb/instructions/review-gates/prose/source-residue.md
model_partition: claude-opus-4-6
runner: claude-code
decision: warn
reviewed_at: "2026-06-28T12:00:00+00:00"
---
```

The raw `bundle-output.md` can stay as the runner/agent output contract unless the parser is deliberately made frontmatter-tolerant.

### Commands share a job plan object

Create one internal value object, named `ReviewJobPlan` or `PreparedReviewJob`, that represents the executable/finalizable job shape:

- job id;
- pending/completed pair rows;
- prompt path;
- bundle output path;
- per-pair result paths;
- packing;
- runner;
- model partition.

Creation commands write this shape; listing, subprocess execution, and finalization load it. Do not let each command rediscover artifact paths, packing, or pair metadata differently.

### Selector JSON is the public handoff

The selector JSON is the only public target-list handoff into job creation. Wrappers may call selector functions internally or pipe the selector JSON into `commonplace-create-review-jobs`, but they should not invent their own target payload shape. This keeps stale-target selection, model-partition declaration, defensive filtering, and grouping boundaries in one place.

### Ack carries forward an existing review

Target ack semantics are stricter than the current implementation.

Ack means: an existing completed review remains valid for the current note/gate snapshots. Therefore an acceptance event written by ack must point to the completed review pair being carried forward.

**The review-less ack is an accident, not a feature.** Every real ack today is a trivial-change re-baseline of a pair that was already reviewed: `ack-trivial-note-changes` re-baselines an existing review across an unwatched edit, and `ack-gate-review` is the manual form of the same move. The current `accepted_review_pair_id = NULL` is simply `ack_pairs` never looking up the prior review pair and discarding the link — not an operator ever asserting "accept this with no review behind it." No waiver/suppression workflow exists or is used: nothing accepts a never-reviewed pair on operator fiat. So requiring the link removes no used capability; it recovers provenance that was being thrown away.

Target rule:

- if a completed review pair exists for `(note_path, gate_path, model_partition)`, ack appends an acceptance event with the current note/gate snapshots and that review pair id;
- if no completed review pair exists, ack fails and the pair must be reviewed.

Ack lookup is path-keyed: find the latest completed review pair for the same `note_path`, `gate_path`, and `model_partition`. Content hashes and snapshot ids are the new accepted freshness baseline, not the identity used to choose the carried-forward review.

The first version changes the ack write path only: new ack events store `accepted_review_pair_id`, while legacy nullable rows remain readable through existing fallback logic. A later hardening migration can backfill old nulls and make `accepted_review_pair_id` `NOT NULL`. If a deliberate "waive a gate without reviewing" operation is ever wanted, add it as an explicit separate event that records operator and reason — do not reintroduce a null-review acceptance.

### Do not relocate review records

This is an important simplification.

Review identity remains path-keyed. Do not add a `review_targets` table just to support relocation, and do not rekey historical review records when a note moves.

Reasoning:

- pure relocation is uncommon;
- relocation together with content change makes old review evidence obsolete anyway;
- preserving old path-keyed history is simpler than pretending review evidence automatically transfers to a new path;
- a moved note needs fresh review under the new path.

### Retry creates a new job

Do not reset failed jobs to `queued` in v1. `create-review-jobs` captures note/gate snapshots; a failed job may have become stale while sitting in the queue.

Retry means create a new job, recapturing snapshots.

## Promotion: write an ADR

This refactor changes the shipped review architecture and its persisted schema, so it is promoted through ADRs rather than left as workshop notes — one per phase, as each lands.

**Phase 1 is recorded by [ADR 033](../../reference/adr/033-honest-review-run-state.md)** (the migration substrate plus the honest, queue-capable run state). The review DB is now at `user_version = 1`; later schema changes start at version 2. The workshop draft is retained as [adr-draft-033-honest-review-run-state.md](./adr-draft-033-honest-review-run-state.md) for provenance only.

**Phase 2 takes a later number** (034+, assigned when it lands). It should record:

- review execution as a queued-job pipeline with two execution media (subprocess runner, orchestrator-driven agents) over one job state machine;
- the acceptance-provenance tightening — ack carries forward an existing review pair, and the review-less acceptance event is removed as an accident rather than a deprecated feature;
- the explicit no-relocation simplification for review records.

The Phase 2 ADR updates [ADR 031](../../reference/adr/031-review-state-uses-run-owned-review-pairs.md) for the `review_runs` -> `review_jobs` execution-record rename while keeping `review_pairs`, and extends [ADR 029](../../reference/adr/029-review-execution-unified-on-note-gate-pairs.md), [ADR 030](../../reference/adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md), and [ADR 033](../../reference/adr/033-honest-review-run-state.md). The acceptance-semantics change may warrant its own sibling ADR; decide when drafting. The `queued` state and honest clock are *not* Phase 2's to record as new decisions — ADR 033 owns them.

## Target Schema Shape

This is the target shape, not necessarily one patch.

```sql
review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT,
    created_at TEXT NOT NULL,
    started_at TEXT,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('queued', 'running', 'completed', 'failed')),
    failure_reason TEXT,
    telemetry_json TEXT,
    prompt_path TEXT,
    bundle_output_path TEXT,
    packing TEXT NOT NULL CHECK (packing IN ('note', 'gate'))
)

review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    pair_status TEXT NOT NULL CHECK (pair_status IN ('pending', 'completed', 'missing')),
    decision TEXT CHECK (decision IN ('pass', 'warn', 'fail', 'error', 'unknown')),
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    result_path TEXT,
    reviewed_at TEXT,
    UNIQUE (review_job_id, note_path, gate_path),
    UNIQUE (review_job_id, pair_ordinal)
)

acceptance_events (
    acceptance_event_id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    accepted_review_pair_id INTEGER REFERENCES review_pairs(review_pair_id),
    accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_at TEXT NOT NULL
)
```

Path keys stay direct on review pairs and acceptance events. No `review_targets` table in v1.

**Artifact paths are stored in v1.** `prompt_path` and `bundle_output_path` stay on `review_jobs` because the command design depends on them: `commonplace-finalize-review-job --review-job-id` loads `bundle_output_path` from the job, and `commonplace-review-job-list` shows both. Per-pair `result_path` likewise stays on `review_pairs`. Deriving these from id instead of storing them is a separate later option, not v1 — keeping them removes a load-bearing column the rest of the plan reads.

**`packing` persists the physical prompt shape only: `note` or `gate`.** The `--grouping` values on `commonplace-create-review-jobs` are *groupings*, not stored packing — `note` and `gate` grouping each resolve to the matching persisted packing. Do not add grouping-only values to the `packing` CHECK.

## Command Shape

### 1. Select stale targets

```bash
commonplace-review-target-selector --json --model {model-partition} {bundle-or-gate...} --note kb/notes
commonplace-review-target-selector --json --model {model-partition} --all-gates --current
```

Target JSON producer contract:

```json
{
  "model_partition": "claude-opus-4-6",
  "targets": [
    {
      "note_path": "kb/notes/example.md",
      "gate_path": "kb/instructions/review-gates/prose/source-residue.md",
      "gate_id": "prose/source-residue",
      "reason": "missing-review"
    }
  ]
}
```

Selection emits stale pairs only. It does not own packing, job creation, execution, or parallelism.

### 2. Create queued jobs

```bash
commonplace-create-review-jobs --input targets.json --grouping note
commonplace-create-review-jobs --input targets.json --grouping gate --batch-size 5
```

Responsibilities:

- read selector output from file or stdin;
- take concrete `model_partition` from the selector input; `--model` is optional and, if given, must match the input's `model_partition` (mismatch is an error). Do not silently let a flag override the declared input model;
- reject model-agnostic selector output as job-creation input in the first version; use it only for coverage/reporting;
- do not accept `--runner` or `--runner-model` during creation; runner provenance is set by execution;
- treat selector JSON as the public handoff; wrappers must call the selector or pass its JSON through rather than constructing a private target payload;
- group targets by grouping;
- filter inapplicable pairs defensively;
- capture note/gate snapshots;
- create `queued` jobs and pending review pairs;
- render prompt and manifest;
- assign the job-owned `bundle-output.md` path.

Groupings (the `--grouping` flag) describe how targets are grouped. Each resolves to a persisted `packing` of `note` or `gate` — the groupings are not new `packing` enum values (see [Target Schema Shape](#target-schema-shape)):

- `note` → `packing = note`: group selected pairs by note and bundle/lens;
- `gate` → `packing = gate`: group selected pairs by gate, chunk notes by `--batch-size`.

There is no separate `explicit` or `bundle` grouping. A pre-grouped same-axis batch (the old `prepare-review-batch` input) is just a single-note input under `--grouping note` or a single-gate input under `--grouping gate`; each yields one job. See [phase-3-job-creation-and-listing.md](./phase-3-job-creation-and-listing.md).

### 3. Inspect queued jobs

```bash
commonplace-review-job-list --model {model-partition}
commonplace-review-job-list --status queued
commonplace-review-job-list --json
```

Show job id, status, prompt path, output path, pair count, packing, runner when present, model partition, age, and failure reason.

### 4. Execute queued jobs through subprocesses

```bash
commonplace-run-review-jobs --runner codex --parallel 4 --limit 20
commonplace-run-review-jobs --runner claude-code --parallel 1 --stop-on-usage-exhausted
```

Responsibilities:

- claim queued jobs with the atomic `queued -> running` update;
- invoke the runner adapter for each prompt;
- pass the job's `model_partition` as the runner model argument in the first version;
- write `bundle-output.md` and debug logs;
- finalize each job;
- enforce parallelism, retry, and usage-exhaustion policy.

Start with sequential execution. Move `commonplace-review-sweep` thread-pool behavior into this command later, using one SQLite connection per worker and no open transaction around runner execution.

### 5. Execute queued jobs through agents

Parent/orchestrator path:

```bash
commonplace-review-job-list --status queued --json
commonplace-finalize-review-job --review-job-id {id}
```

The parent gives each worker a prompt path and expected output path. The worker only writes the output file. The parent finalizes.

Claiming remains informal in v1: no formal lease, timeout, or DB claim command is required for orchestrator jobs. A future command can be added if abandoned-or-duplicate orchestrator work becomes a real operational problem:

```bash
commonplace-claim-review-job --runner live-agent --json
```

### 6. Finalize review job output

```bash
commonplace-finalize-review-job --review-job-id {id}
```

Responsibilities:

- load the job;
- accept jobs in `queued` or `running`;
- reject `completed` and `failed`;
- read the job-owned `bundle-output.md`;
- parse output keyed by `(note_path, gate_path)`;
- salvage completed pairs when some pairs are missing;
- write canonical per-pair result Markdown with frontmatter;
- append acceptance events for completed pairs;
- mark the job `completed` or `failed`.

## Existing Command Fates

| Current command | Fate |
|---|---|
| `commonplace-review-target-selector` | Stage 1 selector, stabilized JSON output |
| `commonplace-prepare-review-batch` | Removed; its single same-axis batch is a single-group `--grouping note` or `--grouping gate` input |
| `commonplace-create-review-runs` | Replaced by `commonplace-create-review-jobs --grouping note`; removed |
| `commonplace-run-review-bundles` | Retained as a thin ergonomic wrapper: create note-packed jobs for one note, then run immediately |
| `commonplace-run-gate-sweep` | Retired into `select -> create-jobs --grouping gate -> run-review-jobs` |
| `commonplace-review-sweep` | Retired into `select -> create-jobs -> run-review-jobs --parallel N` |
| `commonplace-ingest-bundle-output` / `commonplace-ingest-batch-output` | Removed immediately; replaced by `commonplace-finalize-review-job --review-job-id` |
| `commonplace-ack-gate-review` / `commonplace-ack-trivial-note-changes` | Retained, but require an existing completed review pair and carry it forward |

## Migration Invariants

Each schema change runs against an existing populated review DB, not a fresh one. The slices must hold these invariants on the live store, in this order:

0. **Schema changes go through explicit migrations.** Phase 1 added the `user_version` migration runner and table-rebuild path, consuming schema version 1. Phase 2 starts at version 2 and must add ordered migrations on top of that substrate for every table rename, column rename, nullability change, index change, and CHECK change; editing `review-schema.sql` alone is insufficient for existing stores.
1. **Queued ingest path stays widened in both gates.** Phase 1 widened both `batch.ingest` and `record_and_finalize_run` to accept `queued` or `running`. Phase 2 must preserve that behavior when the APIs are renamed to jobs; updating only the public finalize command while regressing the shared finalization gate would recreate the old bug.
2. **Null acks must be backfilled before the `NOT NULL` constraint.** Existing `acceptance_events` rows have `accepted_review_pair_id = NULL`, and readers deliberately recover them: `_effective_review` (`review_db.py:881`) and prune's `_current_review_pair_ids` (`prune_superseded_reviews.py:56`) both read a null ack *through* to the latest completed pair for its `(note_path, gate_path, model_partition)`. Tightening to `NOT NULL` requires: (a) backfill each null row to the same latest-completed pair the readers would have resolved, failing loudly if none exists; (b) only then add the constraint; (c) only then remove the read-through fallback from those readers. A null row with no resolvable completed pair is a data-integrity stop, not a silent drop. The migration should print or return a diagnostic table with `acceptance_event_id`, `note_path`, `gate_path`, and `model_partition`; the operator repairs the rows by re-reviewing or by explicit manual repair, then reruns the migration.
3. **Pair model partition has live readers and tooling.** Dropping `review_pairs.model_partition` (the v1 simplified model layout, landing in Slice 3 / Phase 3) is not just a column drop: the `latest_review_pairs` CTE partitions by `rp.model_partition`, the index `idx_review_pairs_note_gate_model_partition` keys on it, and `rekey_model_partition` updates it. Migration must replace the index, rewrite those queries to join model through `review_jobs`, and drop the column from the rekey tool — together, or the rekey tool writes a column that no longer exists.

## Migration Mechanism

Reuse the Phase 1 review-store migration layer.

SQLite `PRAGMA user_version` is the stored schema version. `ensure_db` should continue to:

1. create a fresh DB from `review-schema.sql` and set `user_version` to the latest schema version when no review tables exist;
2. read `user_version` for existing DBs;
3. apply ordered migration functions until the DB reaches the latest version;
4. run a lightweight post-migration integrity check (`PRAGMA foreign_key_check`, expected tables/indexes/views exist, and no unresolved legacy null ack rows before the NOT NULL migration completes).

Migration functions live near `review_db.py` rather than as one-off operator scripts because every command calls `ensure_db`. Most migrations can own a normal transaction internally. Migrations that SQLite cannot express with simple `ALTER TABLE` must rebuild tables explicitly:

```text
PRAGMA foreign_keys = OFF;   # only when the table swap needs it, outside any active transaction
BEGIN;
CREATE TABLE new_table (...target schema...);
INSERT INTO new_table (...) SELECT ... FROM old_table;
DROP TABLE old_table;
ALTER TABLE new_table RENAME TO old_table;
CREATE INDEX ...;
CREATE VIEW ...;
PRAGMA foreign_key_check;
PRAGMA user_version = N;
COMMIT;
PRAGMA foreign_keys = ON;    # in a finally path
PRAGMA foreign_key_check;
```

Do not wrap a foreign-key-off table swap inside an outer `with conn:` transaction; SQLite only honors `PRAGMA foreign_keys` changes outside an active transaction. The rebuild helper must disable neither foreign keys nor data checks silently. If a migration cannot preserve integrity, it fails and leaves the old DB unchanged. The ack backfill migration is intentionally fail-fast: it reports the offending `(acceptance_event_id, note_path, gate_path, model_partition)` rows and requires re-review or manual repair before continuing.

## Phasing

**Phase 1 — the migration substrate (Slice 0) plus honest job state (Slice 1) — has landed.** It is recorded in [phase-1-honest-job-state.md](./phase-1-honest-job-state.md) and [ADR 033](../../reference/adr/033-honest-review-run-state.md): a `user_version` migration runner, the `queued` status, honest `created_at` / nullable `started_at`, the two status gates, and the run-creation fix, all on the current table names.

Everything below is **Phase 2**. The remaining Phase 2 choices are resolved here: rename first, use a shared job-plan object, treat selector JSON as the public handoff, skip orchestrator leases in v1, run subprocess jobs sequentially before parallelizing, and defer the `model_partitions` table to a proposal. Phase 2 reuses the Phase 1 migration substrate for every schema change here, beginning with schema version 2.

## Implementation Slices (Phase 2)

Phase 2 begins with the `review_runs`→`review_jobs` rename, then builds the command pipeline. Slices 0 and 1 have moved to the Phase 1 file.

### Slice 2: Mechanical rename

Detailed implementation plan: [phase-2-mechanical-job-rename.md](./phase-2-mechanical-job-rename.md).

- Rename run terminology to job terminology across schema, DB helpers, command output, manifests, and docs.
- Keep `review_pairs`, `review_pair_id`, and `accepted_review_pair_id` vocabulary unchanged.
- Keep this slice mechanical: no new command behavior, grouping behavior, ack semantics, or runner changes.
- Implement the rename as migration version 2 or later, preserving Phase 1's `created_at`, nullable `started_at`, `queued` status, and created-time index semantics.

Tests:

- full review test suite passes after rename;
- command JSON uses `review_job_id`;
- migrations preserve existing rows under the renamed tables and columns.

### Slice 3: Stable selector and job creation

Detailed implementation plan: [phase-3-job-creation-and-listing.md](./phase-3-job-creation-and-listing.md).

Stabilize concrete model-specific selector JSON, create queued jobs from that handoff, add shared job-plan loading, and add job listing. Adopt the v1 simplified model layout in the same migration: drop `review_pairs.model_partition`, join model through `review_jobs`, and update the readers and `rekey_model_partition` that touch it (see invariant 3). Defer `runner_model`.

### Slice 4: Job-owned finalization

Detailed implementation plan: [phase-4-job-owned-finalization.md](./phase-4-job-owned-finalization.md).

Finalize by job id using persisted output paths, preserve salvage behavior, write result provenance frontmatter, and retire explicit ingest surfaces.

### Slice 5: Subprocess job runner

Detailed implementation plan: [phase-5-subprocess-job-runner.md](./phase-5-subprocess-job-runner.md).

Run queued jobs through subprocess adapters, starting sequentially, using atomic claim and shared finalization.

### Slice 6: Ack provenance

Detailed implementation plan: [phase-6-ack-provenance.md](./phase-6-ack-provenance.md).

Require new ack writes to carry forward an existing completed review pair using `(note_path, gate_path, model_partition)` lookup. Defer legacy null backfill, `NOT NULL`, and fallback removal.

### Slice 7: No review relocation

Detailed implementation plan: [phase-7-no-review-relocation.md](./phase-7-no-review-relocation.md).

Remove review-state rekeying from relocation flows and treat moved paths as needing fresh review.

### Slice 8: Promote to an ADR and update reference docs

Detailed implementation plan: [phase-8-docs-adr-and-workshop-close.md](./phase-8-docs-adr-and-workshop-close.md).

Promote ADR/reference docs, clean up old command documentation, and close the workshop when no active design remains.

## Non-goals

- Do not change the pair sentinel grammar.
- Do not add a separate queue table.
- Do not put `model_partition` into review output block keys.
- Do not relocate historical review records on note move.
- Do not introduce `review_targets` in v1.
- Do not introduce a `model_partitions` table in Phase 2; keep the deferred registry in `kb/reference/proposals/`.
- Do not preserve review-less acceptance events as a waiver mechanism. First stop writing them; later backfill and constrain legacy rows. A deliberate waive operation, if ever needed, is a separate explicit event.
- Do not reset failed jobs to `queued` in v1.
- Do not expose an output path override in v1 finalization.
- Do not switch this workshop to the content-hash/event-log source-of-truth alternative; that remains owned by `src-architecture-alternatives`.

## Resolved Phase 2 Choices

1. Orchestrator jobs do not need a formal lease/timeout in v1; parent listing plus manual recovery is enough.
2. `commonplace-ingest-bundle-output` and `commonplace-ingest-batch-output` are replaced by `commonplace-finalize-review-job --review-job-id`; no compatibility wrapper is kept.
3. `prompt_path`, `bundle_output_path`, and `result_path` stay stored in v1 because the command surface reads them ([Target Schema Shape](#target-schema-shape)). Deriving paths from id instead is a possible later change, not part of this work.
4. `runner_model` is deferred from the first version. `model_partition` remains the opaque freshness/acceptance key and can be passed to subprocess runners as the first runner-model argument.
5. The `model_partitions` table is deferred to a reference proposal about aliases, validation, and default runner-model lookup.
