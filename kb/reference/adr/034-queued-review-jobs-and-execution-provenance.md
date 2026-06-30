---
description: "Queued review jobs store freshness identity separately from nullable execution provenance across subprocess and orchestrator execution paths"
type: ../types/adr.md
tags: []
status: accepted
---

# 034-Queued review jobs and execution provenance

**Status:** accepted
**Date:** 2026-06-30

## Context

[ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) unified review execution on `(note_path, gate_path)` pairs, [ADR 030](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) exposed harness-facing prepare/ingest seams and runner adapters, [ADR 031](./031-review-state-uses-run-owned-review-pairs.md) made the pair unit persistent in SQLite, [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) made freshness DB-owned and keyed by `model_partition`, and [ADR 033](./033-honest-review-run-state.md) added a migration substrate plus an honest `queued` state and clock.

The next review-execution refactor changes the SQL model again. It turns the execution record from a "run" into a queued "job", removes duplicated pair-level model metadata, and makes the same queued jobs executable through two media:

- a subprocess queue runner (`commonplace-run-review-jobs`) that Commonplace owns directly and that can pass concrete arguments to runner adapters;
- an orchestrator-agent path where the parent agent creates or lists queued jobs, delegates each prompt to a worker agent, and finalizes the worker's output.

The same implementation also tightens adjacent provenance policies that were coupled to the old execution surface: acknowledgement must carry forward concrete review evidence, and note relocation must not pretend path-keyed review history automatically transfers to a new path.

The two media do not expose the same controls. A subprocess adapter may be able to request a concrete model and maybe a reasoning effort. An orchestrator may be able to select a worker model, but some harnesses cannot request effort per worker; Claude Code sub-agent effort is inherited from the parent/session or fixed by subagent configuration. Some harnesses expose reliable telemetry through events or logs; others expose none. Treating all of that as universal, required identity would either make the common orchestrator path unusable or encourage false precision.

At the same time, the review store needs enough execution provenance to debug what happened. The persisted `model_partition` is a freshness/acceptance key, not a reversible runnable model id. The system needs to store the partition as identity while recording the concrete model and effort that the executor actually selected when that information is known.

## Decision

### Store queued review jobs, not review runs

The execution table is renamed mechanically:

- `review_runs` -> `review_jobs`;
- `review_run_id` -> `review_job_id`.

`review_pairs` stays named as a pair table because a row is still the requested `(note_path, gate_path)` pair inside one execution job. Pair vocabulary stays aligned with the prompt protocol.

`model_partition` lives on:

- `review_jobs`;
- `acceptance_events`;
- generated per-pair review-result Markdown frontmatter.

`model_partition` no longer lives on `review_pairs`; completed pairs inherit the model partition through their parent job. `model_partition` remains the freshness and acceptance identity key.

The physical column removal has API and maintenance consequences. `ReviewPairRow.model_partition` remains available in the first version as a derived loader field, populated by joining `review_pairs` to `review_jobs`; repair/rekey tooling treats only `review_jobs` and `acceptance_events` as model-partition tables.

Schema changes use the versioned migration substrate from ADR 033. Constraint changes and column drops use hand-coded rebuilds with the same row-count, foreign-key, index/view recreation, `user_version`, and integrity-check discipline as the Phase 1 migration unless a tested helper is extracted in the same phase.

Only load-bearing artifact paths become state: `review_jobs.prompt_path`, `review_jobs.bundle_output_path`, and `review_pairs.result_path`. `MANIFEST.json` remains a written human/debug artifact beside the prompt and output files. `manifest_path` and `artifact_dir` are not DB columns and are not core job-plan fields; commands may derive a manifest path for display, but no pipeline command reads `MANIFEST.json` as state.

### Keep creation inputs explicit without adding explicit packing

Job creation accepts two input sources:

- model-specific selector JSON with a concrete top-level `model_partition` and a `targets` array whose entries carry normalized gate identity (`gate_path` and `gate_id`);
- direct requested-pair input for explicit QA workflows that must review named pairs even when stale selection would skip them as fresh.

Both input sources resolve through `--grouping note` or `--grouping gate`, and persisted `packing` remains only `note` or `gate`. There is no `explicit` grouping and no `packing = explicit`.

Direct requested-pair input requires `--model`, because no selector payload supplies the job's `model_partition`. Because `commonplace-create-review-jobs` covers the direct same-axis pair workflow through these two grouping modes, the old prepare/ingest/finalize-run compatibility command surfaces are retired rather than documented as current.

### Require ack to carry review evidence

Acceptance events written by full review and by acknowledgement point `accepted_review_pair_id` at a completed review pair. Ack is a trivial-change re-baseline of existing review evidence, not a waiver mechanism.

Ack lookup remains path- and model-partition-keyed: it carries forward the latest completed review pair for the same `(note_path, gate_path, model_partition)`, then snapshots the current note and gate text as the new accepted baseline. If no completed review pair exists, ack fails and the pair must be reviewed.

Legacy nullable acceptance rows remain readable through fallback lookup until a later hardening migration backfills old nulls and tightens the schema. New writes must not create review-less acceptance events.

### Do not relocate path-keyed review history

Review identity remains path-keyed. Note and directory relocation do not rekey `review_jobs`, `review_pairs`, `acceptance_events`, or stored artifact paths such as `prompt_path`, `bundle_output_path`, and `result_path`.

The old path-keyed rows remain historical evidence under the old path. A moved note needs fresh review under the new path unless a later explicit review-history or target-identity workflow is designed.

### Store runner provenance separately from freshness identity

`review_jobs` carries nullable execution-provenance columns:

```sql
runner TEXT,
runner_model TEXT,
runner_effort TEXT,
telemetry_json TEXT
```

Their meanings are:

- `runner`: the execution adapter or medium, such as a subprocess adapter or an orchestrator-agent medium; it is not the concrete model;
- `runner_model`: the concrete model requested or selected when the executor claims or dispatches the job, if known;
- `runner_effort`: the concrete reasoning/thinking effort requested, selected, or inherited when the executor claims or dispatches the job, if known;
- `telemetry_json`: optional execution evidence gathered by the runner or harness.

Null means "unknown or not exposed by this harness", not "default". The store must not guess effort from a model partition or from a harness label.

When an executor starts work on a job, it records provenance at the same moment it changes the job to `running`:

```sql
UPDATE review_jobs
SET status = 'running',
    started_at = ?,
    runner = ?,
    runner_model = ?,
    runner_effort = ?
WHERE review_job_id = ? AND status = 'queued'
  AND model_partition = ?
```

If `runner_effort` is not available, it is stored as `NULL`. If `runner_model` is not available, it is stored as `NULL`, though normal subprocess and orchestrator dispatch paths should know the selected model.

### Validate model partition before execution

The job's `model_partition` is the freshness key. It is not passed as a runnable model id, and it is not used to derive one.

The executor supplies concrete execution settings and validates them against the job before making a model call:

- subprocess path: `commonplace-run-review-jobs` receives `--model` and, only for adapters that can support it, an optional effort setting. It computes `build_model_partition(model, effort)` and claims only queued jobs whose stored `model_partition` matches;
- orchestrator-agent path: the parent agent chooses or is configured with a concrete worker model that belongs to the job's partition, calls `commonplace-claim-review-job` at dispatch, records known model/effort provenance, and delegates only `prompt_path -> bundle_output_path` work to the worker.

Worker agents do not mutate review state and do not run `commonplace-*` commands. The parent remains the DB writer for orchestrator-driven execution.

Reasoning effort is not a required v1 freshness dimension. It is execution provenance when known. A later model-partition registry may define allowed `(model, effort)` combinations, defaults, and constraints such as "when `runner_model` and `runner_effort` are non-null, they must build the stored partition." This refactor deliberately does not introduce that registry.

### Keep the two execution paths explicit

The subprocess path is a queue consumer:

```text
select queued jobs -> claim running with provenance -> run adapter -> write output -> finalize
```

It is owned by Commonplace, so it can implement atomic claiming, sequential execution first, later parallelism with one SQLite connection per worker, and adapter-specific validation of model and effort flags.

The orchestrator-agent path is a parent-dispatched worklist:

```text
list queued jobs -> claim dispatched job with known provenance -> worker writes output -> parent finalizes
```

The queued DB rows are shared, but the orchestrator's workers are pure file transducers. V1 does not add leases or worker heartbeats for this path. If the parent dies after dispatch, manual recovery uses the `running` job row, `started_at`, and artifact paths to decide whether to finalize, fail, or create a new job.

`commonplace-run-review-jobs` is not passed the orchestrator's worker list. It is a subprocess queue consumer. The orchestrator path uses job creation/listing, `commonplace-claim-review-job`, and finalization directly.

The old user-facing wrappers are retained only where they compose the queued stages:

- `commonplace-review-sweep` selects stale targets, creates queued note-packed jobs, and runs them through the subprocess queue runner;
- `commonplace-run-review-bundles` creates queued note-packed jobs for one note and runs those job ids through the subprocess queue runner;
- `commonplace-run-gate-sweep` creates queued gate-packed jobs and runs those job ids through the subprocess queue runner.

They are convenience surfaces over the queued pipeline, not separate persistence paths.

### Make telemetry optional and adapter-owned

Telemetry is evidence, not identity. It can help diagnose whether a runner honored `runner_model`, `runner_effort`, and `model_partition`, but it does not re-key review state.

Telemetry collection sits behind a stable runner/harness API, separate from queue claiming, execution, parsing, and finalization. Implementations may use stdout/stderr, streaming events, vendor session logs, parent-orchestrator reports, or no telemetry at all. The stable contract is:

- input: runner name, repo root, job id, prompt/output paths or sent prompt, process/log handles when present, and known execution provenance;
- output: `None` or a plain JSON-serializable mapping;
- storage: `review_jobs.telemetry_json`, only when telemetry is available;
- behavior: missing telemetry, malformed vendor logs, or unsupported harnesses do not fail a review job.

Telemetry may produce warnings about mismatches, but freshness identity remains `(note_path, gate_path, model_partition)` through acceptance state.

## Consequences

Easier:

- One queued job table supports both subprocess execution and orchestrator-agent execution.
- `model_partition` stays stable as the acceptance/freshness key while concrete model and effort provenance is still available for debugging.
- The SQL model no longer duplicates model partition on every pair row; model partition is inherited through the parent job.
- Direct requested-pair review workflows are preserved without adding a third persisted packing mode.
- The manifest remains an inspection artifact instead of becoming another piece of database/API state.
- Orchestrator-agent execution remains usable even when the harness cannot request per-worker effort or expose reliable telemetry.
- Runner telemetry can vary by harness without infecting the core queue/finalization code.
- Ack provenance no longer drops the completed review pair that justifies the accepted baseline.
- Relocation is simpler and avoids misleading review lineage transfer across path changes.
- Existing sweep/bundle/gate command habits can stay while their implementation converges on queued jobs.

Harder / accepted costs:

- The store has nullable execution provenance columns, so readers must distinguish "unknown" from "known concrete value."
- Pair readers and model-partition repair tooling must join through jobs once `review_pairs.model_partition` is removed.
- Legacy nullable acceptance rows require reader fallback until the hardening migration removes that compatibility path.
- Moved notes need fresh review under their new path.
- Operational docs and instructions must move with the command surface, because stale creation flags or `commonplace-prepare-review-batch` references would mislead agents before final workshop cleanup.
- The system trusts executor-side validation in v1; hard SQL constraints between `model_partition`, `runner_model`, and `runner_effort` wait for a model-partition registry.
- Orchestrator-dispatched jobs can be abandoned in `running` if the parent dies; v1 handles that through manual recovery rather than leases.
- Telemetry cannot be treated as universal evidence. Some jobs will have `telemetry_json = NULL` even when they completed correctly.
- Result files and debug surfaces must explain that `runner_model` / `runner_effort` are dispatch-time provenance, optionally confirmed or contradicted by telemetry, not mutable review identity.

---

Relevant Notes:

- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) - extends: preserves the pair protocol and keeps `review_pairs` as the child row shape.
- [030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) - extends: keeps runner adapters but moves queue consumption behind `commonplace-run-review-jobs`.
- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) - supersedes-in-part: renames runs to jobs and removes pair-level model duplication while keeping pair ownership.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) - extends: keeps `model_partition` as the frozen freshness key and does not re-key from telemetry.
- [033-Honest review-run state behind a versioned migration substrate](./033-honest-review-run-state.md) - extends: uses the queued/running/completed/failed state and versioned migrations added there.
- [model partition registry](../proposals/model-partition-registry.md) - deferred: future aliases, defaults, effort compatibility, and hard constraints.
