---
description: Accepts SQLite as the canonical store for review state once review artifacts are removed from git and start carrying selector and ack metadata rather than just human-readable prose
type: ../types/adr.md
tags: []
status: accepted
---

# 010-review state should move to sqlite once reviews leave git and accumulate operational metadata

**Status:** accepted
**Date:** 2026-04-01

## Context

The original review system was file-shaped for good reasons. Review artifacts were markdown, inspectable in any editor, and fit the repo's broader files-first storage bias.

That changed in two steps.

First, per-gate review artifacts were removed from git because they produced too much churn. Once reviews stopped being versioned alongside notes and gates, the main file advantage weakened. The review files were still markdown, but they were no longer participating in the repo's normal diff and history workflow.

Second, the files stopped being "just prose". To preserve selector and ack behavior outside git, each review file had to carry operational metadata:

- accepted note sha
- accepted gate fingerprint
- last full review provenance
- acceptance timestamps and acceptance kind
- model partition identity

At that point the system was no longer primarily reading documents. It was querying current state keyed by `(note_path, gate_id, model_id)`, comparing current SHAs against accepted SHAs, and mutating acceptance state when a trivial change was acked. `ack` had become a metadata rewrite over an operational record rather than a normal document edit.

This created an awkward intermediate form: flat files holding append-like state, latest-state state, and human-readable review prose all at once. The mechanics wanted indexes and current-state queries, but the storage model was still pretending they were ordinary files.

## Decision

Store review state in local SQLite once reviews are out of git and have accumulated operational metadata.

The current concrete schema is:

- `review_jobs` stores one prompt/output invocation
- `review_pairs` stores each requested `(note_path, gate_path)` pair inside a job
- `acceptance_events` stores append-only acceptance history and points at completed review-pair evidence
- current acceptance is derived by latest event per `(note_path, gate_path, model_partition)`
- selector reads current note and gate text from files, but reads accepted baselines from SQLite snapshots
- `ack` appends an acceptance event instead of rewriting review artifacts
- review execution creates a queued job first, workers write only job-owned output files, and finalization advances acceptance after parsing pair output
- markdown review files are rendered inspection views, not the canonical store

ADR 031 and ADR 034 refine the concrete schema; the storage boundary and acceptance-event model from this decision remain current.

This is a scoped exception to the repo's files-first architecture, not a reversal of it. Notes, gates, instructions, and source material remain file-backed. The database is justified here because the review subsystem stopped being authored library content and became local operational state.

## Consequences

### Easier

- **Current-state lookup becomes direct.** Selector logic reduces to "load latest acceptance for this key and compare SHAs" instead of scanning files and interpreting embedded metadata blocks.
- **Ack stops mutating prose artifacts.** Trivial-change acknowledgement becomes a first-class state transition rather than a metadata rewrite inside a review document.
- **History becomes explicit.** Append-only review and acceptance tables preserve both review bodies and acceptance evolution without overloading one markdown file with both historical and current meaning.
- **Execution history becomes explicit.** One multi-gate review invocation is queryable as a job rather than inferred later from a pile of per-gate artifacts.
- **Model partitions are cleaner.** `(note, gate, model)` is a real indexed key instead of an implicit convention reconstructed from directory layout and filename suffixes.
- **Inspection stays possible.** Human-readable markdown can still be rendered from DB rows when needed, but inspectability is now a derived view rather than the storage contract.

### Harder

- **Review state now has a schema.** We need schema management, import paths for old artifacts, and tests that preserve selector parity.
- **Execution and acceptance must be separated.** A failed or partial job should remain visible in history without advancing freshness state for missing pairs, which means finalization needs explicit correctness checks.
- **The write path is DB-first.** Markdown review files are rendered outputs rather than the canonical live path.
- **The repo now has a justified exception to files-first.** We need to explain clearly why review state crossed the threshold while notes and other KB artifacts did not.

The boundary is: files remain the right default for authored knowledge under git, but once an artifact is removed from git and the system mostly wants indexed state transitions over it, SQLite is the simpler representation.

---

Relevant Notes:

- [007-reports-directory-for-generated-snapshots](./007-reports-directory-for-generated-snapshots.md) — enables: review artifacts had already moved into `kb/reports/`, which clarified that they were generated operational outputs rather than core notes
- [review system](../README-REVIEW-SYSTEM.md) — implements: the current DB-backed review workflow and command surface that followed from this decision
- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — superseded-by: refines the concrete schema while preserving this ADR's SQLite boundary
