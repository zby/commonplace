---
description: "Review schema v7 separates job grouping, pair completion, verdict outcomes, execution failure, and snapshot-pinned freshness baselines under one cross-surface vocabulary"
type: ../types/adr.md
tags: []
status: accepted
---

# 043-Review state separates completion, outcomes, and freshness baselines

**Status:** accepted  
**Date:** 2026-07-11  
**Supersedes in part:** [ADR-035](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md), [ADR-036](./036-review-acceptance-is-current-state-not-append-only-history.md)

## Context

The criterion-axis refactor left adjacent concepts under conflicting or overloaded names. Job construction was `grouping` at the CLI but `packing` in storage. `bundle` named both an authored gate-catalog lens and execution output. Pair completion was stored as `reviewed_at`, freshness baselines were called acceptance, and a single decision enum combined substantive verdicts with `ERROR`. Missing baselines and malformed present baselines both surfaced as `missing-review`.

These were not independent spelling problems. They obscured five distinct facts: a job groups requested pairs; a pair completes under a result-kind protocol; only verdict pairs carry a substantive outcome; execution can fail to produce any result; and a current freshness baseline records how far retained evidence remains applicable. The populated schema-v5 store contained paid evidence, so adopting the model also required one direct preservation route rather than recreation or a chain through schema v6.

## Decision

Schema v7 and every active Python, JSON, manifest, artifact, CLI, instruction, and reference surface use this model:

- `review_jobs.grouping` is `note` or `criterion`.
- Execution artifacts live under `kb/reports/review-jobs/review-job-{id}/`; the worker writes `job-output.md`, surfaced as `job_output_path`. `bundle` remains reserved for authored gate-catalog bundles.
- `review_pairs.completed_at` records pair completion. Verdict pairs complete with `outcome IN ('pass', 'warn', 'fail')`; report pairs complete with a null outcome and the `REPORT` marker.
- `ERROR` is not an outcome. It means the worker could not produce the contracted result and fails the all-or-nothing job, leaving every pair incomplete and advancing no baseline.
- `freshness_baselines` holds one current row per `(note_path, criterion_path, model_partition)`. `evidence_review_pair_id` identifies the completed evidence; `baseline_note_snapshot_id`, `baseline_criterion_snapshot_id`, and `baseline_updated_at` record the current applicability boundary.
- Acknowledgement requires an existing baseline and advances its snapshots while preserving `evidence_review_pair_id`. It creates no job, pair, result, or evidence.
- An absent row is ordinary stale state, `missing-baseline`. A present baseline with missing text, mismatched paths/model, incomplete evidence, or unresolved references is store corruption and raises at initialization or the baseline query boundary.
- Type and collection helper names use `conformance`, because that behavior—not the gate subset—is what they discriminate.

SQLite remains the canonical review store for this decision. Whether it should later become a projection over another source of truth is a separate storage-architecture decision; this schema change does not decide it implicitly.

The direct v5→v7 preservation mapping is:

| schema v5 | schema v7 |
|---|---|
| `review_jobs.packing` (`gate` value included) | `review_jobs.grouping` (`gate` → `criterion`) |
| pair `gate_path`, `decision`, `reviewed_at`, reviewed gate snapshot | `criterion_path`, `outcome`, `completed_at`, reviewed criterion snapshot |
| `acceptance` and `accepted_*` | `freshness_baselines`, `evidence_review_pair_id`, and `baseline_*` |
| `current_gate_acceptances` | `current_freshness_baselines` |

The migration preserves job, pair, and snapshot identifiers; outcomes; source text; timestamps; baseline-to-evidence relationships; and row counts. It refuses a v5 `ERROR` pair rather than reclassifying it as completed evidence. The retained store is backed up and migrated only after the route passes on a copy with version, count, integrity, and foreign-key checks.

The retained-store migration completed on 2026-07-11. The byte-identical backup at `kb/reports/review-store.v5.backup.sqlite` has SHA-256 `927d6dccdbdcd364f3919c3da633cae956995b94a91e6bac50cb97d70f7906a8`. Source and rehearsed/target counts were 32 jobs, 44 pairs, 15 file snapshots, and 44 baseline rows; both SQLite integrity checks and foreign-key checks passed, and all 44 baseline relationships joined back to matching evidence pairs and parent model partitions.

Rejected alternatives:

- Keeping aliases or compatibility properties would preserve the ambiguity and create two active vocabularies.
- Treating `ERROR` as a fourth verdict would make operational inability look like substantive judgment.
- Letting acknowledgement search arbitrary historical pairs would allow it to manufacture freshness state rather than advance current state.
- Converting malformed baselines to `missing-baseline` would hide corruption as ordinary work.
- Requiring v5→v6→v7 would turn an unreleased intermediate schema into operational history without preserving more evidence.

## Consequences

Completion, substantive outcome, execution failure, and freshness can now be queried independently. Verdict and report protocols share one completion fact without pretending reports decide anything. Operators can distinguish an unreviewed pair from a broken store, and acknowledgement has a narrow carry-forward meaning.

The change is deliberately breaking across code and generated artifacts. Old execution names, paths, schema objects, helpers, and current-documentation explanations are removed rather than aliased. Historical ADRs and the source-schema fixture keep their original terms where needed to explain the migration.

The stronger invariants cost stricter writes: every baseline snapshot is non-null and contains matching source text, baseline evidence must come from a completed job, and `ERROR` output cannot be retained as completed assay evidence. These restrictions are the intended model, not compatibility gaps.

---

Relevant Notes:

- [Review system](../README-REVIEW-SYSTEM.md) — implemented-by: operator vocabulary and protocol
- [Review system architecture](../review-architecture.md) — implemented-by: schema, modules, and integrity boundary
- [Storage architecture](../storage-architecture.md) — part-of: current SQLite storage boundary
