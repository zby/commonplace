---
description: Accepts SQLite as the canonical store for review state once review artifacts are removed from git and start carrying selector and ack metadata rather than just human-readable prose
type: adr
tags: [architecture, reviews]
status: accepted
---

# 010-review state should move to sqlite once reviews leave git and accumulate operational metadata

**Status:** accepted
**Date:** 2026-04-01

## Context

The original review system was file-shaped for good reasons. Review artifacts were markdown, inspectable in any editor, and fit the repo's broader [files beat a database for agent-operated knowledge bases](../files-not-database.md) bias.

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

Concretely:

- `gate_reviews` stores append-only review history
- `acceptance_events` stores append-only acceptance history
- current acceptance is derived by latest event per `(note_path, gate_id, model_id)`
- selector reads current note and gate SHAs from files, but reads accepted state from SQLite
- `ack` appends an acceptance event instead of rewriting review artifacts
- markdown review files become optional imports or rendered inspection views, not the canonical store

This is a scoped exception to the repo's files-first architecture, not a reversal of it. Notes, gates, instructions, and source material remain file-backed. The database is justified here because the review subsystem stopped being authored library content and became local operational state.

## Consequences

### Easier

- **Current-state lookup becomes direct.** Selector logic reduces to "load latest acceptance for this key and compare SHAs" instead of scanning files and interpreting embedded metadata blocks.
- **Ack stops mutating prose artifacts.** Trivial-change acknowledgement becomes a first-class state transition rather than a metadata rewrite inside a review document.
- **History becomes explicit.** Append-only review and acceptance tables preserve both review bodies and acceptance evolution without overloading one markdown file with both historical and current meaning.
- **Model partitions are cleaner.** `(note, gate, model)` is a real indexed key instead of an implicit convention reconstructed from directory layout and filename suffixes.
- **Inspection stays possible.** Human-readable markdown can still be rendered from DB rows when needed, but inspectability is now a derived view rather than the storage contract.

### Harder

- **Review state now has a schema.** We need schema management, import paths for old artifacts, and tests that preserve selector parity.
- **The write path becomes split during transition.** Fresh review prose may still be written as markdown for a while, which then needs import or rendering conventions until the DB-first path settles completely.
- **The repo now has a justified exception to files-first.** We need to explain clearly why review state crossed the threshold while notes and other KB artifacts did not.

The boundary is: files remain the right default for authored knowledge under git, but once an artifact is removed from git and the system mostly wants indexed state transitions over it, SQLite is the simpler representation.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../files-not-database.md) — constrains: this ADR is a scoped exception to the files-first rule, not a replacement for it
- [007-reports-directory-for-generated-snapshots](./007-reports-directory-for-generated-snapshots.md) — enables: review artifacts had already moved into `kb/reports/`, which clarified that they were generated operational outputs rather than core notes
- [review-db-migration workshop](../../work/review-db-migration/README.md) — develops: the workshop that turned this decision into a migration plan, schema, and compatibility checklist
