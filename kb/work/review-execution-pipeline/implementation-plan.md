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

### Two execution media share one queue

There are two execution media over the same persisted jobs:

- **subprocess runner path**: an operator, CI job, scheduled process, or wrapper runs `commonplace-run-review-jobs`; the command pulls queued jobs from the DB, claims them, invokes runner adapters, and finalizes;
- **orchestrator-agent path**: the parent agent lists queued jobs, dispatches workers itself, and finalizes when each worker writes the expected output.

For the dominant live-agent/orchestrator path, sub-agents are pure file transducers:

```text
prompt_path -> bundle_output_path
```

They must not run `commonplace-*` commands or mutate review state. The parent creates jobs, delegates prompt files, and finalizes outputs. Therefore v1 does not need transactional multi-process claiming for the orchestrator path, and orchestrator workers do not call `commonplace-run-review-jobs`.

The subprocess runner can still mark jobs `running` because Commonplace owns that subprocess execution.

### Claiming and concurrency policy

V1 has no formal lease/timeout for orchestrator-driven jobs. The parent lists queued jobs, dispatches each prompt path once, and finalizes the job when the worker writes the job-owned output file. Manual recovery handles abandoned orchestrator jobs.

The subprocess runner is queue-driven by default. It claims queued jobs from the DB, optionally narrowed by explicit `--review-job-id` values for recovery/debug runs. Claiming is an atomic update:

```sql
UPDATE review_jobs
SET status = 'running', started_at = ?
WHERE review_job_id = ? AND status = 'queued'
  AND model_partition = ?
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

For the first version, do not store separate runner-model or runner-effort columns. The concrete model is **supplied by the executor at execution time**, not derived from the stored `model_partition`: `normalize_model_partition` is many-to-one, so a partition cannot be turned back into a runnable model id.

**The model is validated at execution, against the job's partition**, before any model call:

- the subprocess runner enforces it in code before claim/execution: `normalize_model_partition(--model) == job.model_partition`; mismatched jobs are not claimed;
- the orchestrator enforces it by instruction: the parent spawns or selects each worker with a concrete model that is a member of the job's partition.

The spawned/selected model should be the **newest member of the job's partition** — capped by the partition, not the newest model overall (which may belong to a different partition: the harness's current `opus` could be `claude-opus-4-8`, a *different* partition from `claude-opus`). A newest-member-per-partition lookup is part of the deferred `model_partitions` registry; until it exists, the orchestrator instruction names the model explicitly.

Reasoning effort is not a v1 review identity field. In the orchestrator-agent path, Claude Code worker effort is inherited from the parent/session or fixed by a named subagent configuration; the parent should not treat effort as a per-job dynamic request. In the subprocess path, an effort flag should be added only for runner adapters that can actually set it; unsupported adapters fail early rather than silently ignoring it. Making effort a deliberate freshness distinction is a registry change, deferred.

Finalization stays model-agnostic in v1: the membership gate already ran at execution. Runner telemetry can still be stored in `telemetry_json` as a secondary "did the runner honor the requested model" check, distinct from the partition-membership gate. If execution later needs first-class provenance for concrete model or effort, add nullable execution-provenance fields then.

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

## Command Surface Overview

The canonical commands are:

- `commonplace-review-target-selector` for target selection;
- `commonplace-create-review-jobs` for queued job creation;
- `commonplace-review-job-list` for queue inspection and orchestrator dispatch;
- `commonplace-run-review-jobs` for subprocess/script execution;
- `commonplace-finalize-review-job` for job-owned output finalization.

`commonplace-run-review-jobs` is not passed the orchestrator's worker list in the normal path. It is a queue consumer: it selects queued jobs from the DB, optionally narrowed by explicit job ids, then claims and runs them. The orchestrator path uses `commonplace-review-job-list` and `commonplace-finalize-review-job` directly.

## Phase Plans

This file is the shared design overview. Detailed implementation steps, migrations, and tests live in the phase files:

- [Phase 1: honest job state](./phase-1-honest-job-state.md) — implemented and recorded by [ADR 033](../../reference/adr/033-honest-review-run-state.md).
- [Phase 2: mechanical job rename](./phase-2-mechanical-job-rename.md).
- [Phase 3: job creation and listing](./phase-3-job-creation-and-listing.md).
- [Phase 4: job-owned finalization](./phase-4-job-owned-finalization.md).
- [Phase 5: subprocess job runner](./phase-5-subprocess-job-runner.md).
- [Phase 6: ack provenance](./phase-6-ack-provenance.md).
- [Phase 7: no review relocation](./phase-7-no-review-relocation.md).
- [Phase 8: docs, ADR, and workshop close](./phase-8-docs-adr-and-workshop-close.md).

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
4. `runner_model` and `runner_effort` are deferred from the first version. `model_partition` remains the opaque freshness/acceptance key; concrete model selection happens at execution time and is validated against that partition.
5. The `model_partitions` table is deferred to a reference proposal about aliases, validation, and default runner-model lookup.
