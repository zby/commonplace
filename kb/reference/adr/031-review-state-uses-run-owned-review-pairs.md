---
description: "Review state stores one prompt invocation as a review run and each requested note-gate check as a review pair, replacing the earlier split between run-gate metadata and gate review rows"
type: ../types/adr.md
tags: []
status: accepted
---

# 031-Review state uses run-owned review pairs

**Status:** accepted
**Date:** 2026-06-22

## Context

[ADR 010](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) moved review state into SQLite once reviews stopped being authored git artifacts and became operational state. Its first implementation still carried the old execution shape into the schema: `review_runs` described a note-scoped invocation, `review_run_gates` captured the requested gates for that invocation, and `gate_reviews` stored completed per-gate outcomes.

[ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) then made the execution protocol explicit: the unit of review work is one `(note_path, gate_id)` pair, while note-packed and gate-packed calls are only packing strategies over that same pair protocol. After that change, the database still had to translate between "run plus gates" and "review rows" even though the prompt, parser, selector, warning picker, and acceptance state all reasoned in pairs.

The mismatch produced avoidable complexity:

- Gate-packed review sweeps wanted one run for many notes sharing one gate, but the schema still implied a note-shaped run.
- External batch execution wanted one artifact and one ingest operation for a set of requested pairs, but the manifest had to reconstruct which lower-level records belonged together.
- Finalization had to decide coverage by comparing requested gates to returned reviews instead of updating the requested pair rows directly.
- Failure salvage was ambiguous: a prompt invocation can partially succeed at the pair level even when the run as a whole has missing output.

The storage model needed to match the protocol's real invariant: a run is one prompt invocation, and its children are the requested `(note, gate)` pairs.

## Decision

Store review execution state as run-owned review pairs.

Concretely:

- `review_runs` stores one prompt invocation and records runner, model, status, telemetry, raw output, debug log, and `packing` (`note`, `gate`, or `manual-import`).
- `review_pairs` stores every requested `(note_path, gate_id)` pair inside that run, including pair ordinal, pair status (`pending`, `completed`, `missing`), decision, rationale, evidence, gate SHA, reviewed note SHA, reviewed note commit, model id, review time, and review kind.
- `acceptance_events` points to the accepted `review_pair_id` when acceptance comes from a completed review; ack and override events may have no accepted pair.
- The current freshness view remains acceptance-driven: latest acceptance per `(note_path, gate_id, model_id)` is compared to current note and gate SHAs.
- Note-packed, gate-packed, live-agent, and external batch paths all create one run plus its requested pair rows before execution, then complete or mark those same pair rows during ingest/finalization.
- Missing output is represented at the pair level. Completed pairs may still be retained and accepted while the containing run records failure context for the missing pairs.
- The old `review_run_gates` and `gate_reviews` split is retired rather than kept as a compatibility layer.

This refines ADR 010's concrete schema while preserving its storage boundary: authored KB content stays file-backed, while generated review state remains a scoped SQLite exception.

## Consequences

Easier:

- The database, prompt protocol, parser, executor, selectors, and warning surfaces now share the same unit of work.
- Packing becomes provenance on the run, not a different data model. A note-packed run and a gate-packed run both contain ordinary pair rows.
- Finalization is simpler: requested rows already exist, parsed output completes matching rows, and absent output marks rows `missing`.
- Batch artifacts have one stable run id, manifest, prompt, and bundle output for the invocation that produced them.
- Acceptance points at a concrete completed pair, so warnings and stale-state checks can recover the exact reviewed text and provenance.
- Cleanup and repair tools can reason over obsolete review pairs without deleting an entire run artifact unless every pair in that run is obsolete.

Harder / accepted costs:

- A run no longer means "one note". Consumers must inspect `packing` and child pairs instead of inferring shape from the run id.
- Pair rows duplicate `model_id` from the run so selectors and repair utilities can key directly by `(note, gate, model)`. This is denormalized deliberately; model rekeying must update both tables.
- Partial success now has two layers of state: completed pair rows can be useful while the containing run is failed because some requested pairs were missing.
- Historical prose and old table names may appear in older ADRs, reports, or migration artifacts; the live schema does not preserve old production aliases.

---

Relevant Notes:

- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — supersedes: keeps the SQLite storage boundary but replaces the concrete `review_run_gates`/`gate_reviews` table split
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the protocol decision whose pair unit this storage model makes persistent
- [review system architecture](../review-architecture.md) — part-of: the subsystem whose data model now centers on `review_pairs`
- [storage architecture](../storage-architecture.md) — part-of: the broader storage boundary that treats review state as the SQLite-backed exception
