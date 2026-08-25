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

The criterion-axis refactor left adjacent concepts under conflicting or overloaded names: job construction had one name at the CLI and another in storage, `bundle` named both an authored gate-catalog lens and execution output, freshness baselines were called acceptance, a single decision enum combined substantive verdicts with `ERROR`, and missing baselines and malformed present baselines surfaced alike.

These were not independent spelling problems. They obscured five distinct facts: a job groups requested pairs; a pair completes under a result-kind protocol; only verdict pairs carry a substantive outcome; execution can fail to produce any result; and a current freshness baseline records how far retained evidence remains applicable. The populated store contained paid evidence that adopting the model had to preserve.

## Decision

Every active code, artifact, CLI, instruction, and reference surface uses this model:

- A job groups requested pairs by `note` or `criterion`. `bundle` remains reserved for authored gate-catalog bundles.
- A pair records its completion. Verdict pairs complete with an outcome of `pass`, `warn`, or `fail`; report pairs complete with no outcome and the `REPORT` marker.
- `ERROR` is not an outcome. It means the worker could not produce the contracted result and fails the all-or-nothing job, leaving every pair incomplete and advancing no baseline.
- One current freshness baseline exists per `(note, criterion, model partition)`. It identifies the completed evidence pair and records the note and criterion snapshots that bound current applicability.
- Acknowledgement requires an existing baseline and advances its snapshots while preserving its evidence pair. It creates no job, pair, result, or evidence.
- An absent baseline is ordinary stale state, `missing-baseline`. A present baseline with missing text, mismatched paths or model, incomplete evidence, or unresolved references is store corruption and raises rather than reporting staleness.

SQLite remains the canonical review store for this decision. Whether it should later become a projection over another source of truth is a separate storage-architecture decision; this schema change does not decide it implicitly.

Rejected alternatives:

- Keeping aliases or compatibility properties would preserve the ambiguity and create two active vocabularies.
- Treating `ERROR` as a fourth verdict would make operational inability look like substantive judgment.
- Letting acknowledgement search arbitrary historical pairs would allow it to manufacture freshness state rather than advance current state.
- Converting malformed baselines to `missing-baseline` would hide corruption as ordinary work.

## Consequences

Completion, substantive outcome, execution failure, and freshness can now be queried independently. Verdict and report protocols share one completion fact without pretending reports decide anything. Operators can distinguish an unreviewed pair from a broken store, and acknowledgement has a narrow carry-forward meaning.

The stronger invariants cost stricter writes: every baseline snapshot is non-null and contains matching source text, baseline evidence must come from a completed job, and `ERROR` output cannot be retained as completed assay evidence. These restrictions are the intended model, not compatibility gaps.

---

Relevant Notes:

- [Review system](../README-REVIEW-SYSTEM.md) — implemented-by: operator vocabulary and protocol
- [Review system architecture](../review-architecture.md) — implemented-by: canonical-state, finalization, and freshness boundaries
- [Storage architecture](../storage-architecture.md) — part-of: current SQLite storage boundary
