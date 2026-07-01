---
description: "Review jobs use derived artifact paths, finalization-time provenance, strict result parsing, and all-or-nothing acceptance"
type: ../types/adr.md
tags: []
status: accepted
---

# 035-Review jobs finalize all-or-nothing with derived artifacts

**Status:** accepted
**Date:** 2026-07-01

## Context

[ADR 034](./034-queued-review-jobs-and-execution-provenance.md) established queued review jobs, selector-JSON creation, parent-dispatched workers, and execution provenance separate from freshness identity. Its first implementation still carried extra state and workflow surface:

- `commonplace-claim-review-job` moved jobs from `queued` to `running` before worker dispatch.
- `review_jobs` stored artifact paths that were derivable from the job id.
- `review_pairs` stored `pair_status`, so failed multi-pair jobs could retain completed pairs.
- Live parsing accepted several free-text aliases and inference fallbacks.

Those features added maintenance surface without enough current operational value. There is no scheduler with leases or heartbeats, so `running` did not enforce ownership. Persisted artifact paths duplicated deterministic naming rules. Partial salvage made acceptance reasoning harder because a failed job could still advance freshness for a subset of pairs. Permissive parsing made model drift look like successful review output.

## Decision

Review jobs now have exactly three statuses: `queued`, `completed`, and `failed`. Job creation prepares queued work and prompt artifacts. Worker dispatch remains parent-owned and does not mutate the review DB. `commonplace-finalize-review-job` records optional provenance at finalization time:

- `--runner` records the execution medium or worker label.
- `--model` records the concrete worker model and validates `build_model_partition(--model, --effort)` against the job's `model_partition`.
- `--effort` requires `--model`.

Artifact paths are derived, not persisted. The job directory is `kb/reports/bundle-reviews/review-job-{review_job_id}/`; prompt, bundle output, manifest, and per-pair result paths are pure functions of the job id, packing, and complete pair set.

Finalization is all-or-nothing. The finalizer validates parse coverage before mutating acceptance state, and result-file write failures roll back the DB completion. Missing, duplicate, unexpected, malformed, or result-less pair blocks fail the whole job. Failed jobs leave pair decisions null and write no acceptance rows.

Live parsing is strict: each pair block must end with exactly one final result line:

```text
## Result: PASS
## Result: WARN
## Result: FAIL
## Result: ERROR
```

Aliases and inferred decisions are invalid in live finalization.

Acceptance evidence is guarded at the SQL boundary. `current_gate_acceptances` joins `acceptance` through `review_pairs` and `review_jobs`, and only exposes rows whose parent job is `completed` and whose pair has a non-null decision. This makes the freshness selector robust even if an accidental acceptance row is inserted.

Result files are evidence and remain fatal: a result-file write failure prevents DB completion and then marks the job failed in a separate failure transaction. `MANIFEST.json` is display/debug output, so a manifest refresh failure after DB completion does not fail the job; finalization reports it as a warning.

ADR 036 later changed successful acceptance from append-only events to a current-state upsert and moved superseded-review pruning inline with that success transaction.

The review store remains schema-current only. Incompatible stores must be recreated rather than migrated. The one-shot model-partition repair command was removed with the old migration surface.

Deferred:

- selector/create consolidation into a convenience command;
- schema-validated structured output;
- deciding whether `MANIFEST.json` should shrink or remain as an inspection artifact.

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
