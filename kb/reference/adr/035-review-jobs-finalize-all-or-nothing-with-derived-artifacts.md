---
description: "Review jobs use derived artifact paths, finalization-time provenance, strict per-kind result parsing, and all-or-nothing acceptance"
type: ../types/adr.md
tags: []
status: accepted
---

# 035-Review jobs finalize all-or-nothing with derived artifacts

**Status:** accepted
**Date:** 2026-07-01

## Context

[ADR 034](./034-queued-review-jobs-and-execution-provenance.md) established queued review jobs, selector-JSON creation, parent-dispatched workers, and execution provenance separate from freshness identity. Its first implementation still carried extra state and workflow surface: a claim step that moved jobs to `running` before worker dispatch, persisted artifact paths derivable from the job id, per-pair status that let failed multi-pair jobs retain completed pairs, and live parsing that accepted free-text aliases and inference fallbacks.

Those features added maintenance surface without enough current operational value. There is no scheduler with leases or heartbeats, so `running` did not enforce ownership. Persisted artifact paths duplicated deterministic naming rules. Partial salvage made acceptance reasoning harder because a failed job could still advance freshness for a subset of pairs. Permissive parsing made model drift look like successful review output.

## Decision

Review jobs now have exactly three statuses: `queued`, `completed`, and `failed`. Job creation prepares queued work and prompt artifacts. Worker dispatch remains parent-owned and does not mutate the review DB. `commonplace-finalize-review-job` records optional provenance at finalization time: the execution medium or worker label, and the concrete worker model and effort, validated against the job's `model_partition`.

Artifact paths are derived, not persisted: the job directory, prompt, bundle output, manifest, and per-pair result paths are pure functions of the job id, packing, and complete pair set.

Finalization is all-or-nothing. The finalizer validates parse coverage before mutating acceptance state, and result-file write failures roll back the DB completion. Missing, duplicate, unexpected, malformed, or result-less pair blocks fail the whole job. Failed jobs reset pair completion state (`decision` and `reviewed_at` remain null) and write no acceptance rows.

Live parsing is strict: each pair block must end with exactly one final result line, parsed against the pair's persisted `result_kind`. Verdict pairs accept only `PASS`, `WARN`, `FAIL`, or `ERROR`; report pairs accept only `REPORT`, which is a completion marker rather than a decision. Aliases and inferred decisions are invalid in live finalization.

Acceptance evidence is guarded at the SQL boundary. The current-acceptance view joins acceptance through pairs and jobs, and only exposes rows whose parent job is `completed` and whose pair satisfies per-kind completion: `reviewed_at` plus a decision for verdict pairs, or `reviewed_at` plus a null decision for report pairs. This makes the freshness selector robust even if an accidental acceptance row is inserted.

Result files are evidence and remain fatal: a result-file write failure prevents DB completion and then marks the job failed in a separate failure transaction. `MANIFEST.json` is display/debug output, so a manifest refresh failure after DB completion does not fail the job; finalization reports it as a warning.

Schema migration remains exceptional rather than a general compatibility promise. Stores whose historical evidence cannot be represented by the current schema must be recreated; a narrow in-place migration is admissible only when paid-for evidence is exactly representable in the new schema. Commonplace has no external consumers that justify a general compatibility layer.

### Result kinds

Review pairs persist `result_kind = verdict | report`, separating protocol completion from a decision. Jobs are result-kind homogeneous, finalization parses against the persisted kind, and `REPORT` completes a report pair with `reviewed_at` while leaving `decision` null. This extends the all-or-nothing rule without weakening it: every expected pair must still complete under its own contract before the job advances acceptance.

### Criterion-axis naming

The generic assay axis uses `criterion` throughout the schema, Python API, JSON and artifact fields, protocol labels, stale reason, and CLI. `Gate` remains only for the closed-ended, verdict-kind criterion type, its authored `gate_id`, its catalog, and `--all-gates`. The invariant is that the concept and every generic identifier share one name.

Deferred:

- selector/create consolidation into a convenience command;
- schema-validated structured output;
- deciding whether `MANIFEST.json` should shrink or remain as an inspection artifact.

## Considered alternatives

The later proposal **Harness-orchestrated review sweeps** supplied the operating-procedure option space for this decision's parent-owned dispatch seam. Its adopted outcome is the harness-neutral [`run-review-batches`](../../instructions/run-review-batches.md) instruction: the parent selects and creates jobs, schedules one hermetic review worker per returned job within the harness concurrency limit, finalizes each output, and verifies freshness. This procedure has now been exercised through both supported agent harnesses, so the proposal's portability trigger is met.

- **A package-owned scheduler or runner adapter** was rejected. Concurrency, budgets, retries, and model calls are harness capabilities; duplicating them in Commonplace would add a weaker orchestration layer around deterministic endpoints that already compose.
- **A saved vendor-specific workflow script** was rejected as the framework form. It would bind the procedure to one proprietary orchestration API and its argument, sandbox, and telemetry behavior. The instruction states roles and invariants that either harness can execute through its native worker surface.
- **A coordinator worker running deterministic steps** was rejected as the default. The parent runs selection, creation, finalization, and verification directly; review workers perform judgment only and never mutate bookkeeping state. This preserves the hermetic-worker boundary and avoids spending model calls on deterministic coordination.
- **Structured worker returns** remain deferred to the separate codec decision. Sentinel-delimited job output is still the portable medium, while runner/model/effort evidence is recorded at finalization when the harness can supply it.

## Consequences

Easier:

- The live workflow has one fewer required command: create jobs, dispatch workers, finalize jobs.
- Job status reflects only durable review-state transitions, not unenforced worker ownership.
- Artifact naming is centralized in code and cannot diverge from DB rows.
- Failed jobs cannot silently advance freshness.
- Strict parsing makes malformed live output visible immediately.
- The freshness boundary has a defensive SQL invariant, not only a caller convention.

Harder / accepted costs:

- A parent cannot mark a job as in progress inside the review DB. External orchestration must track dispatch progress itself.
- A mostly complete multi-pair output with one missing pair must be rerun or repaired outside finalization; the completed subset is not accepted.
- Historical prose and proposals that discuss claim/running or partial salvage must be read as superseded context unless they cite this ADR as current.

---

Relevant Notes:

- [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) — supersedes: keeps parent-dispatched queued jobs and nullable execution provenance while moving provenance to finalization and removing running state.
- [033-Honest review state behind a versioned migration substrate](./033-honest-review-run-state.md) — supersedes-in-part: keeps honest queued work but removes running/start state.
- [032-Review freshness uses DB snapshots, not Git](./032-review-freshness-uses-db-snapshots-not-git.md) — extends: reinforces DB-owned accepted baselines through the guarded current-acceptance view.
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — supersedes-in-part: keeps the pair grammar and packing model while removing partial salvage from live finalization.
- [review system](../README-REVIEW-SYSTEM.md) — implemented-by: current operator-facing workflow.
