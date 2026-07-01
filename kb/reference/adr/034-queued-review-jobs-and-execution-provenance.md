---
description: "Superseded historical decision: queued review jobs stored freshness identity separately from nullable parent-dispatch provenance before finalization-time provenance replaced claim/running"
type: ../types/adr.md
tags: []
status: superseded
---

# 034-Queued review jobs and execution provenance

**Status:** superseded by [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)
**Date:** 2026-06-30

## Context

[ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) unified review execution on `(note_path, gate_path)` pairs, [ADR 030](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) exposed an intermediate harness-facing seam, [ADR 031](./031-review-state-uses-run-owned-review-pairs.md) made the pair unit persistent in SQLite, [ADR 032](./032-review-freshness-uses-db-snapshots-not-git.md) made freshness DB-owned and keyed by `model_partition`, and [ADR 033](./033-honest-review-run-state.md) separated job creation time from actual execution time.

The review system now has one execution model:

1. deterministic Python selects targets, creates queued jobs, snapshots prompt inputs, claims jobs, finalizes output, and records acceptance;
2. a parent agent or harness dispatches workers and owns all model calls, fan-out, retries, and budgets;
3. workers are pure file transducers: read the job prompt and write the job output file.

That split removes Commonplace-owned subprocess dispatch and keeps the review package focused on state, prompts, parsing, and finalization.

## Decision

### Store queued review jobs

`review_jobs` stores one prompt/output invocation. `review_pairs` stores each requested `(note_path, gate_path)` pair inside that job. Pair vocabulary stays aligned with the sentinel prompt protocol.

`model_partition` lives on:

- `review_jobs`;
- `acceptance`;
- generated per-pair review-result Markdown frontmatter.

`review_pairs` derive model partition through their parent job. `model_partition` remains the freshness and acceptance identity key.

Only load-bearing artifact paths become state: `review_jobs.prompt_path`, `review_jobs.bundle_output_path`, and `review_pairs.result_path`. `MANIFEST.json` remains a written human/debug artifact beside the prompt and output files. No pipeline command reads it as state.

The schema is current-only. A missing review DB is created from the packaged schema; a DB with a mismatched review shape is rejected and must be recreated rather than transformed in place.

### Create jobs only from selector JSON

Job creation accepts selector JSON with a concrete top-level `model_partition` and a `targets` array whose entries carry normalized gate identity (`gate_path` and `gate_id`).

`commonplace-create-review-jobs` groups those pairs with `--grouping note` or `--grouping gate`; persisted `packing` remains only `note` or `gate`. There is no direct note input, direct pair input, explicit packing mode, or prepare/ingest command surface.

### Require ack to carry review evidence

Acceptance rows written by full review and by acknowledgement point `accepted_review_pair_id` at a completed review pair. Ack is a trivial-change re-baseline of existing review evidence, not a waiver mechanism. ADR 036 later changed this from an append-style history to one current row per acceptance key.

Ack lookup remains path- and model-partition-keyed: it carries forward the latest completed review pair for the same `(note_path, gate_path, model_partition)`, then snapshots the current note and gate text as the new accepted baseline. If no completed review pair exists, ack fails and the pair must be reviewed.

### Do not relocate path-keyed review history

Review identity remains path-keyed. Note and directory relocation do not rekey `review_jobs`, `review_pairs`, `acceptance`, or stored artifact paths such as `prompt_path`, `bundle_output_path`, and `result_path`.

The old path-keyed rows remain historical evidence under the old path. A moved note needs fresh review under the new path unless a later explicit review-history or target-identity workflow is designed.

### Store dispatch provenance separately from freshness identity

`review_jobs` carries nullable execution-provenance columns:

```sql
runner TEXT,
runner_model TEXT,
runner_effort TEXT,
telemetry_json TEXT
```

Their meanings are:

- `runner`: the dispatch medium or worker label; it is not the concrete model;
- `runner_model`: the concrete model requested or selected when the parent claims the job, if known;
- `runner_effort`: the concrete reasoning/thinking effort requested, selected, or inherited when the parent claims the job, if known;
- `telemetry_json`: optional execution evidence gathered by the parent harness.

Null means "unknown or not exposed by this harness", not "default". The store must not guess effort from a model partition or from a harness label.

When the parent starts work on a job, it records provenance at the same moment it changes the job to `running`:

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

### Validate model partition at claim time

The job's `model_partition` is the freshness key. It is not passed as a runnable model id, and it is not used to derive one.

The parent supplies concrete execution settings and validates them against the job before dispatch by calling `commonplace-claim-review-job`. The claim computes `build_model_partition(model, effort)` and succeeds only when it matches the stored partition. If the harness cannot expose effort, `runner_effort` is stored as `NULL`.

Worker agents do not mutate review state and do not run `commonplace-*` commands. The parent remains the DB writer.

### Keep workers hermetic

The parent-dispatched worklist is:

```text
list queued jobs -> claim dispatched job with known provenance -> worker writes output -> parent finalizes
```

V1 does not add leases or worker heartbeats. If the parent dies after dispatch, manual recovery uses the `running` job row, `started_at`, and artifact paths to decide whether to finalize, fail, or create a new job.

Telemetry is evidence, not identity. It can help diagnose whether a worker honored `runner_model`, `runner_effort`, and `model_partition`, but it does not re-key review state.

## Consequences

Easier:

- One queued job table supports the current parent-dispatched review workflow.
- `model_partition` stays stable as the acceptance/freshness key while concrete model and effort provenance remains available for debugging.
- The SQL model does not duplicate model partition on every pair row.
- Job creation has one input contract: selector JSON.
- The manifest remains an inspection artifact instead of becoming another piece of database/API state.
- Orchestrator-agent execution remains usable even when the harness cannot request per-worker effort or expose reliable telemetry.
- Ack provenance always points at the completed review pair that justifies the accepted baseline.
- Relocation is simpler and avoids misleading review lineage transfer across path changes.
- Commonplace review code no longer tracks vendor subprocess behavior.

Harder / accepted costs:

- The store has nullable execution-provenance columns, so readers must distinguish "unknown" from "known concrete value."
- Ad hoc explicit-pair QA must go through selector requested mode and selector JSON.
- Moved notes need fresh review under their new path.
- The system trusts parent-side validation in v1; hard SQL constraints between `model_partition`, `runner_model`, and `runner_effort` wait for a model-partition registry.
- Orchestrator-dispatched jobs can be abandoned in `running` if the parent dies; v1 handles that through manual recovery rather than leases.
- Telemetry cannot be treated as universal evidence. Some jobs will have `telemetry_json = NULL` even when they completed correctly.
- Result files and debug surfaces must explain that `runner_model` / `runner_effort` are dispatch-time provenance, optionally confirmed or contradicted by telemetry, not mutable review identity.

---

Relevant Notes:

- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) - extends: preserves the pair protocol and keeps `review_pairs` as the child row shape.
- [030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) - supersedes: keeps the deterministic seam while removing Commonplace-owned model dispatch.
- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) - supersedes-in-part: keeps pair ownership while simplifying the job table and pair model.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) - extends: keeps `model_partition` as the frozen freshness key and does not re-key from telemetry.
- [033-Honest review-run state behind a versioned migration substrate](./033-honest-review-run-state.md) - superseded historical chain: kept honest queued/running/completed/failed state while dropping in-place schema transformation.
- [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) - supersedes: removes claim/running state, persisted artifact paths, partial salvage, and permissive live parsing.
- [model partition registry](../proposals/model-partition-registry.md) - deferred: future aliases, defaults, effort constraints, and hard constraints.
