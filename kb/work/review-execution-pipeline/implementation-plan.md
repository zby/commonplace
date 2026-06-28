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
- `review_pairs` -> `review_job_items`
- `review_pair_id` -> `review_job_item_id`

Phase 2 starts with this mechanical rename. It may be its own commit, but it is the first Phase 2 slice so every new command, helper, migration, JSON shape, and test uses the target job vocabulary from the start. Do not introduce behavioral changes while this churn is in flight.

### Queue state lives on jobs

Do not add a separate queue table. The job status is enough.

Phase 1 already added these values to the current `review_runs` table. Phase 2 preserves them through the `review_runs` -> `review_jobs` rename.

```text
queued, running, completed, failed
```

Meanings:

- `queued`: prompt and item rows exist; no worker has claimed execution.
- `running`: a subprocess worker has claimed the job.
- `completed`: all required items completed and accepted.
- `failed`: preparation, execution, parse, or coverage failed; salvaged completed items may still be retained per existing policy.

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

It should not be duplicated on `review_job_items`. Completed items inherit model through their job.

`model_partition` remains the freshness and acceptance key. Treat it as opaque; do not add a `model_partitions` table in Phase 2.

Store the concrete runner model separately as nullable `review_jobs.runner_model`. `runner_model` is the CLI/model-adapter argument passed to the subprocess runner when it is known. It may be `NULL` for live-agent execution or runner-default execution. It is not part of freshness identity, and changing a runner default later must not re-key existing jobs or acceptances.

A future `model_partitions` registry may centralize aliases and runner defaults, but that is deferred to a proposal rather than implemented in this queue refactor: [model partition registry](../../reference/proposals/model-partition-registry.md).

Generated canonical per-pair result files should include frontmatter like:

```yaml
---
review_job_id: 42
review_job_item_id: 101
note_path: kb/notes/example.md
gate_path: kb/instructions/review-gates/prose/source-residue.md
model_partition: claude-opus-4-6
runner: claude-code
runner_model: claude-opus-4-6
decision: warn
reviewed_at: "2026-06-28T12:00:00+00:00"
---
```

Omit `runner_model` from generated frontmatter when the job has no concrete runner-model value.

The raw `bundle-output.md` can stay as the runner/agent output contract unless the parser is deliberately made frontmatter-tolerant.

### Commands share a job plan object

Create one internal value object, named `ReviewJobPlan` or `PreparedReviewJob`, that represents the executable/finalizable job shape:

- job id;
- pending/completed item rows;
- prompt path;
- bundle output path;
- per-item result paths;
- packing;
- runner;
- model partition;
- runner model.

Creation commands write this shape; listing, subprocess execution, and finalization load it. Do not let each command rediscover artifact paths, packing, or item metadata differently.

### Selector JSON is the public handoff

The selector JSON is the only public target-list handoff into job creation. Wrappers may call selector functions internally or pipe the selector JSON into `commonplace-create-review-jobs`, but they should not invent their own target payload shape. This keeps stale-target selection, model-partition declaration, defensive filtering, and grouping boundaries in one place.

### Ack carries forward an existing review

Target ack semantics are stricter than the current implementation.

Ack means: an existing completed review remains valid for the current note/gate snapshots. Therefore an acceptance event written by ack must point to the completed review item being carried forward.

**The review-less ack is an accident, not a feature.** Every real ack today is a trivial-change re-baseline of a pair that was already reviewed: `ack-trivial-note-changes` re-baselines an existing review across an unwatched edit, and `ack-gate-review` is the manual form of the same move. The current `accepted_review_pair_id = NULL` is simply `ack_pairs` never looking up the prior review item and discarding the link — not an operator ever asserting "accept this with no review behind it." No waiver/suppression workflow exists or is used: nothing accepts a never-reviewed pair on operator fiat. So requiring the link removes no used capability; it recovers provenance that was being thrown away.

Target rule:

- if a completed review item exists for `(note_path, gate_path, model_partition)`, ack appends an acceptance event with the current note/gate snapshots and that review item id;
- if no completed review item exists, ack fails and the pair must be reviewed.

`accepted_review_job_item_id` becomes `NOT NULL`. If a deliberate "waive a gate without reviewing" operation is ever wanted, add it as an explicit separate event that records operator and reason — do not reintroduce a null-review acceptance.

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
- the acceptance-provenance tightening — ack carries forward an existing review item, and the review-less acceptance event is removed as an accident rather than a deprecated feature;
- the explicit no-relocation simplification for review records.

The Phase 2 ADR supersedes [ADR 031](../../reference/adr/031-review-state-uses-run-owned-review-pairs.md) (`review_pairs` → `review_jobs` + `review_job_items`) and extends [ADR 029](../../reference/adr/029-review-execution-unified-on-note-gate-pairs.md), [ADR 030](../../reference/adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md), and [ADR 033](../../reference/adr/033-honest-review-run-state.md). The acceptance-semantics change may warrant its own sibling ADR; decide when drafting. The `queued` state and honest clock are *not* Phase 2's to record as new decisions — ADR 033 owns them.

## Target Schema Shape

This is the target shape, not necessarily one patch.

```sql
review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT NOT NULL,
    runner_model TEXT,
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

review_job_items (
    review_job_item_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    item_ordinal INTEGER NOT NULL,
    item_status TEXT NOT NULL CHECK (item_status IN ('pending', 'completed', 'missing')),
    decision TEXT CHECK (decision IN ('pass', 'warn', 'fail', 'error', 'unknown')),
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    result_path TEXT,
    reviewed_at TEXT,
    UNIQUE (review_job_id, note_path, gate_path),
    UNIQUE (review_job_id, item_ordinal)
)

acceptance_events (
    acceptance_event_id INTEGER PRIMARY KEY,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    accepted_review_job_item_id INTEGER NOT NULL REFERENCES review_job_items(review_job_item_id),
    accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_at TEXT NOT NULL
)
```

Path keys stay direct on job items and acceptance events. No `review_targets` table in v1.

**Artifact paths are stored in v1.** `prompt_path` and `bundle_output_path` stay on `review_jobs` because the command design depends on them: `commonplace-finalize-review-job --review-job-id` loads `bundle_output_path` from the job, and `commonplace-review-job-list` shows both. Per-item `result_path` likewise stays on `review_job_items`. Deriving these from id instead of storing them is a separate later option, not v1 — keeping them removes a load-bearing column the rest of the plan reads.

**`packing` persists the physical prompt shape only: `note` or `gate`.** The `explicit` and `bundle` values that appear on `commonplace-create-review-jobs` are *groupings*, not stored packing — they describe how targets are grouped at creation time and each resolves to a persisted `note` or `gate` packing. Do not widen the `packing` CHECK for them.

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
commonplace-create-review-jobs --input targets.json --grouping note --runner codex --runner-model gpt-5
commonplace-create-review-jobs --input targets.json --grouping gate --batch-size 5 --runner claude-code --runner-model claude-opus-4-6
```

Responsibilities:

- read selector output from file or stdin;
- take `model_partition` from the selector input; `--model` is optional and, if given, must match the input's `model_partition` (mismatch is an error). Do not silently let a flag override the declared input model;
- store `--runner-model` on the job when supplied; leave `runner_model` null when the runner should use its default or when the job is live-agent/orchestrator-driven;
- treat selector JSON as the public handoff; wrappers must call the selector or pass its JSON through rather than constructing a private target payload;
- group targets by grouping;
- filter inapplicable pairs defensively;
- capture note/gate snapshots;
- create `queued` jobs and pending job items;
- render prompt and manifest;
- assign the job-owned `bundle-output.md` path.

Groupings (the `--grouping` flag) describe how targets are grouped. Each resolves to a persisted `packing` of `note` or `gate` — the groupings are not new `packing` enum values (see [Target Schema Shape](#target-schema-shape)):

- `note` → `packing = note`: group selected pairs by note and bundle/lens;
- `gate` → `packing = gate`: group selected pairs by gate, chunk notes by `--batch-size`;
- `explicit` → `packing = note` or `gate`: accept an already grouped same-axis batch from an orchestrator, persisting whichever physical shape it is;
- `bundle` → `packing = note`: stricter note grouping that preserves bundle-local prompts, if needed.

### 3. Inspect queued jobs

```bash
commonplace-review-job-list --model {model-partition}
commonplace-review-job-list --status queued
commonplace-review-job-list --json
```

Show job id, status, prompt path, output path, item count, packing, runner, runner model when present, model partition, age, and failure reason.

### 4. Execute queued jobs through subprocesses

```bash
commonplace-run-review-jobs --runner codex --parallel 4 --limit 20
commonplace-run-review-jobs --runner claude-code --parallel 1 --stop-on-usage-exhausted
```

Responsibilities:

- claim queued jobs with the atomic `queued -> running` update;
- invoke the runner adapter for each prompt;
- pass the job's `runner_model` to the runner adapter when non-null, and omit a model argument when it is null;
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
- salvage completed items when some pairs are missing;
- write canonical per-pair result Markdown with frontmatter;
- append acceptance events for completed items;
- mark the job `completed` or `failed`.

## Existing Command Fates

| Current command | Fate |
|---|---|
| `commonplace-review-target-selector` | Stage 1 selector, stabilized JSON output |
| `commonplace-prepare-review-batch` | Folded into `commonplace-create-review-jobs --grouping explicit`; removed |
| `commonplace-create-review-runs` | Replaced by `commonplace-create-review-jobs --grouping note`; removed |
| `commonplace-run-review-bundles` | Retained as a thin ergonomic wrapper: create note-packed jobs for one note, then run immediately |
| `commonplace-run-gate-sweep` | Retired into `select -> create-jobs --grouping gate -> run-review-jobs` |
| `commonplace-review-sweep` | Retired into `select -> create-jobs -> run-review-jobs --parallel N` |
| `commonplace-ingest-bundle-output` / `commonplace-ingest-batch-output` | Removed immediately; replaced by `commonplace-finalize-review-job --review-job-id` |
| `commonplace-ack-gate-review` / `commonplace-ack-trivial-note-changes` | Retained, but require an existing completed review item and carry it forward |

## Migration Invariants

Each schema change runs against an existing populated review DB, not a fresh one. The slices must hold these invariants on the live store, in this order:

0. **Schema changes go through explicit migrations.** Phase 1 added the `user_version` migration runner and table-rebuild path, consuming schema version 1. Phase 2 starts at version 2 and must add ordered migrations on top of that substrate for every table rename, column rename, nullability change, index change, and CHECK change; editing `review-schema.sql` alone is insufficient for existing stores.
1. **Queued ingest path stays widened in both gates.** Phase 1 widened both `batch.ingest` and `record_and_finalize_run` to accept `queued` or `running`. Phase 2 must preserve that behavior when the APIs are renamed to jobs; updating only the public finalize command while regressing the shared finalization gate would recreate the old bug.
2. **Null acks must be backfilled before the `NOT NULL` constraint.** Existing `acceptance_events` rows have `accepted_review_pair_id = NULL`, and readers deliberately recover them: `_effective_review` (`review_db.py:881`) and prune's `_current_review_pair_ids` (`prune_superseded_reviews.py:56`) both read a null ack *through* to the latest completed pair for its `(note_path, gate_path, model_partition)`. Tightening to `NOT NULL` requires: (a) backfill each null row to the same latest-completed item the readers would have resolved, failing loudly if none exists; (b) only then add the constraint; (c) only then remove the read-through fallback from those readers. A null row with no resolvable completed pair is a data-integrity stop, not a silent drop. The migration should print or return a diagnostic table with `acceptance_event_id`, `note_path`, `gate_path`, and `model_partition`; the operator repairs the rows by re-reviewing or by explicit manual repair, then reruns the migration.
3. **Item model partition has live readers and tooling.** Dropping `review_job_items.model_partition` is not just a column drop: the `latest_review_pairs` CTE partitions by `rp.model_partition`, the index `idx_review_pairs_note_gate_model_partition` keys on it, and `rekey_model_partition` updates it. Migration must replace the index, rewrite those queries to join model through `review_jobs`, and drop the column from the rekey tool — together, or the rekey tool writes a column that no longer exists.

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

- Rename run terminology to job terminology across schema, DB helpers, command output, manifests, and docs.
- Rename acceptance-event references from `accepted_review_pair_id` to `accepted_review_job_item_id`.
- Keep this slice mechanical: no new command behavior, grouping behavior, ack semantics, or runner changes.
- Implement the rename as migration version 2 or later, preserving Phase 1's `created_at`, nullable `started_at`, `queued` status, and created-time index semantics.

Tests:

- full review test suite passes after rename;
- command JSON uses `review_job_id`;
- migrations preserve existing rows under the renamed tables and columns.

### Slice 3: Stable selector and job creation

- Stabilize `commonplace-review-target-selector --json` as the target-list producer contract.
- Add `commonplace-create-review-jobs`.
- Add nullable `review_jobs.runner_model` and persist `--runner-model` when supplied.
- Introduce the internal `ReviewJobPlan` / `PreparedReviewJob` loader used by the new job commands.
- Move grouping responsibility into job creation.
- Render prompt/manifests during job creation.

Tests:

- selector JSON includes top-level `model_partition`;
- create jobs rejects a `--model` value that does not match selector JSON;
- create jobs stores `runner_model` when supplied and leaves it null when omitted;
- wrappers consume selector JSON or selector functions instead of private target payloads;
- note grouping produces one job per note/bundle group;
- gate grouping chunks as requested;
- dry/inapplicable targets are handled consistently.

### Slice 4: Job-owned finalization

- Add `commonplace-finalize-review-job --review-job-id`.
- Read `bundle_output_path` from the job.
- Load job/item/artifact metadata through the shared job-plan object.
- Remove both old public ingest commands immediately: `commonplace-ingest-bundle-output` and `commonplace-ingest-batch-output`.
- Remove v1 path override.
- Keep recovery by editing the canonical output file in place.

Tests:

- finalization reads job-owned output;
- missing output file errors clearly;
- old `--input-file` surface and old ingest commands are rejected/absent.

### Slice 5: Model provenance and item model cleanup

This is more than a column drop — see [Migration Invariants](#migration-invariants) #3.

- Write `model_partition`, `runner`, and optional `runner_model` into generated per-pair result Markdown frontmatter (do this first, so artifacts stay self-describing before the column goes).
- Rewrite queries that read `review_pairs.model_partition` to join model through `review_jobs` — notably the `latest_review_pairs` CTE in `_effective_review`.
- Replace the index `idx_review_pairs_note_gate_model_partition` with one keyed on the columns that remain.
- Drop `review_job_items.model_partition` and remove it from `rekey_model_partition` in the same migration.
- Keep the `model_partitions` registry out of this slice; the deferred registry proposal is for alias/default metadata, not review identity.

Tests:

- result Markdown frontmatter includes `model_partition`;
- result Markdown frontmatter includes `runner_model` only when the job has one;
- warn selector, effective-review lookup, and pruning still resolve model through the job;
- `rekey_model_partition` updates jobs and acceptance events only, with no reference to the dropped column;
- acceptance state remains keyed by `(note_path, gate_path, model_partition)`.

### Slice 6: Ack provenance

This slice corrects the accidental review-less ack, not a deprecation of a used feature (see the ack design decision). It carries a one-time migration — see [Migration Invariants](#migration-invariants) #2 — so the steps are ordered:

- Change ack to find the existing completed review item for `(note_path, gate_path, model_partition)` and store its id on the acceptance event; keep accepted snapshot ids as the current note/gate snapshots at ack time.
- Backfill existing null `accepted_review_job_item_id` rows to the latest-completed item their readers already resolve to; fail loudly on any null row with no resolvable completed item.
- Report unresolved rows as `acceptance_event_id`, `note_path`, `gate_path`, and `model_partition` so the operator can re-review or manually repair them before rerunning the migration.
- Only after backfill, make `accepted_review_job_item_id` `NOT NULL`.
- Only after the constraint holds, remove the read-through-to-latest fallback from `_effective_review` (`review_db.py:881`) and prune's `_current_review_pair_ids` (`prune_superseded_reviews.py:56`).
- Fail ack when no completed item exists.

Tests:

- ack after a note-only trivial change carries forward the old review item and new note snapshot;
- ack with no completed review fails;
- backfill maps each legacy null ack to the same item the old read-through resolved; a null ack with no completed pair stops the migration;
- after fallback removal, effective-review and pruning still return the carried-forward item;
- current acceptance points to the carried-forward review item;
- warn selector can still load the review text from the accepted item.

### Slice 7: No review relocation

- Remove review DB rekeying from relocation hooks for the target v1 path.
- Treat moved paths as needing review under the new path.
- Keep old path-keyed review history as historical evidence only.

Tests:

- relocating a note does not mutate review job items or acceptance events;
- selector reports the moved path as needing review unless separately reviewed.

### Slice 8: Subprocess job runner

- Add `commonplace-run-review-jobs` with sequential execution first.
- Use existing runner adapters.
- Claim jobs with the atomic `queued -> running` update.
- Pass `runner_model` to the runner adapter when non-null; omit model argument when null.
- Preserve usage-exhaustion behavior.
- Move existing `review_sweep` parallelism here after sequential behavior is stable.
- For parallel mode, use one SQLite connection per worker, short transactions, and `busy_timeout`; never hold a transaction while the runner process is executing.

Tests:

- sequential runner completes queued jobs;
- two workers cannot claim the same queued job;
- runner receives `runner_model` when set and uses runner default behavior when null;
- failures mark jobs failed and preserve salvaged completed items;
- usage exhaustion stops subsequent jobs.

### Slice 9: Promote to an ADR and update reference docs

- Draft the Phase 2 ADR (034+, assigned when it lands) capturing the queued-job pipeline, the job state machine, the acceptance-provenance change, and the no-relocation simplification (see [Promotion: write an ADR](#promotion-write-an-adr)).
- Mark it superseding ADR 031 and extending ADR 029 / 030.
- Update `kb/reference/review-architecture.md` to describe the queued-job model and the new command stages.
- Close the workshop: promote durable artifacts, then delete the work folder.

## Non-goals

- Do not change the pair sentinel grammar.
- Do not add a separate queue table.
- Do not put `model_partition` into review output block keys.
- Do not relocate historical review records on note move.
- Do not introduce `review_targets` in v1.
- Do not introduce a `model_partitions` table in Phase 2; keep the deferred registry in `kb/reference/proposals/`.
- Do not preserve review-less acceptance events as a waiver mechanism; they are an accident being removed, not a feature. A deliberate waive operation, if ever needed, is a separate explicit event.
- Do not reset failed jobs to `queued` in v1.
- Do not expose an output path override in v1 finalization.
- Do not switch this workshop to the content-hash/event-log source-of-truth alternative; that remains owned by `src-architecture-alternatives`.

## Resolved Phase 2 Choices

1. Orchestrator jobs do not need a formal lease/timeout in v1; parent listing plus manual recovery is enough.
2. `commonplace-ingest-bundle-output` and `commonplace-ingest-batch-output` are replaced by `commonplace-finalize-review-job --review-job-id`; no compatibility wrapper is kept.
3. `prompt_path`, `bundle_output_path`, and `result_path` stay stored in v1 because the command surface reads them ([Target Schema Shape](#target-schema-shape)). Deriving paths from id instead is a possible later change, not part of this work.
4. `runner_model` is stored on jobs as nullable execution metadata. `model_partition` remains the opaque freshness/acceptance key.
5. The `model_partitions` table is deferred to a reference proposal about aliases, validation, and default runner-model lookup.
