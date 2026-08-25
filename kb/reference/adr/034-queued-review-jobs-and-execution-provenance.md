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

Builds on [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) through [ADR 033](./033-honest-review-run-state.md): pair-unified execution, persistent pairs, DB-owned freshness keyed by `model_partition`, and honest job-state timing.

The review system has one execution model:

1. deterministic Python selects targets, creates queued jobs, snapshots prompt inputs, claims jobs, finalizes output, and records acceptance;
2. a parent agent or harness dispatches workers and owns all model calls, fan-out, retries, and budgets;
3. workers are pure file transducers: read the job prompt and write the job output file.

That split removes Commonplace-owned subprocess dispatch and keeps the review package focused on state, prompts, parsing, and finalization.

## Decision

### Store queued review jobs

`review_jobs` stores one prompt/output invocation. `review_pairs` stores each requested `(note_path, gate_path)` pair inside that job. Pair vocabulary stays aligned with the sentinel prompt protocol.

`model_partition` lives on jobs, on acceptance rows, and in generated per-pair review-result frontmatter; pairs derive it through their parent job. It remains the freshness and acceptance identity key.

Only load-bearing artifact paths (job prompt, bundle output, per-pair result) become state. `MANIFEST.json` remains a written human/debug artifact beside the prompt and output files; no pipeline command reads it as state.

The schema is current-only: a missing review DB is created from the packaged schema, while a mismatched review shape is rejected rather than transformed implicitly.

### Create jobs only from selector JSON

Job creation accepts only selector JSON with a concrete top-level `model_partition` and targets carrying normalized gate identity, grouped by note or by gate. There is no direct note input, direct pair input, explicit packing mode, or prepare/ingest command surface.

### Require ack to carry review evidence

Acceptance rows written by full review and by acknowledgement point `accepted_review_pair_id` at a completed review pair. Ack is a trivial-change re-baseline of existing review evidence, not a waiver mechanism.

Ack lookup remains path- and model-partition-keyed: it carries forward the latest completed review pair for the same `(note_path, gate_path, model_partition)`, then snapshots the current note and gate text as the new accepted baseline. If no completed review pair exists, ack fails and the pair must be reviewed.

### Do not relocate path-keyed review history

Review identity remains path-keyed. Note and directory relocation do not rekey jobs, pairs, acceptance rows, or stored artifact paths.

The old path-keyed rows remain historical evidence under the old path. A moved note needs fresh review under the new path unless a later explicit review-history or target-identity workflow is designed.

### Store dispatch provenance separately from freshness identity

Jobs carry nullable execution-provenance fields: the dispatch medium or worker label (`runner`, not the concrete model), the concrete model and reasoning effort requested or selected when the parent claims the job (`runner_model`, `runner_effort`, if known), and optional telemetry gathered by the parent harness. Null means "unknown or not exposed by this harness", not "default". The store must not guess effort from a model partition or from a harness label.

The parent records provenance at the same moment it changes the job from `queued` to `running`.

### Validate model partition at claim time

The job's `model_partition` is the freshness key. It is not passed as a runnable model id, and it is not used to derive one.

The parent supplies concrete execution settings and validates them against the job before dispatch (operative through `commonplace-claim-review-job`): the claim succeeds only when the partition built from the supplied model and effort matches the stored partition. If the harness cannot expose effort, `runner_effort` is stored as null.

Worker agents do not mutate review state and do not run `commonplace-*` commands. The parent remains the DB writer.

### Keep workers hermetic

The parent lists queued jobs, claims each with known provenance, lets the worker write output, and finalizes. V1 does not add leases or worker heartbeats. If the parent dies after dispatch, manual recovery uses the `running` job row, `started_at`, and artifact paths to decide whether to finalize, fail, or create a new job.

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
