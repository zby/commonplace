# src architecture alternatives workshop

## Purpose

Hold the alternative-architecture analysis that came out of reading `src/commonplace/` end to end, and carry forward the design threads that have follow-on work. The analysis surfaced five structural axes (storage substrate, executor pipeline, content-addressed ledger, load-once KB graph, CLI shape); this workshop is where those get developed, decided, or dropped.

The active first thread is the **review storage substrate**: an append-only event log as the source of truth, with SQLite demoted to a rebuildable index over it. The triggering decision is that acceptance events must embed (or content-address) the note/gate snapshots they accepted — now that review is decoupling from Git, the log can no longer lean on Git to retrieve prior reviewed content.

## Scope

In scope:

- code architecture of `src/commonplace/` — module boundaries, god-modules, duplicated parsing, the executor's three execution paths;
- the review store's *source-of-truth shape* (event log vs SQLite-as-store), and what an acceptance event must carry to be self-sufficient without Git;
- how the durable ledger (acceptance keyed by content) separates from swappable execution orchestration.

Out of scope:

- freshness/execution *semantics* and the selector-vs-runner boundary — accepted in [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md);
- the files-vs-relational *justification* — settled in [files-vs-db-churn](../files-vs-db-churn/files-vs-db.md);
- generic cross-artifact lineage tables — owned by [lineage-mechanisms](../lineage-mechanisms/README.md);
- runner adapters and the pair protocol grammar (these are the clean parts; leave them).

## Relationship to neighbor workshops

These workshops agree on the destination and differ on one axis this workshop has to resolve:

- [files-vs-db-churn](../files-vs-db-churn/files-vs-db.md) argues a *keyed, queryable* store earns its place for review verdicts (cache invalidation over a many-to-many relation).
- [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) commits accepted input snapshots **to SQLite** and decouples freshness from Git.

This workshop asks whether the *source of truth* should be SQLite at all, or an append-only event log with SQLite as a derived index rebuilt from it. Decision baseline: review state — including the log and its snapshots — lives **outside Git** (continuous with ADR-010). That makes Git-churn and Git-survivability non-factors, so the log can't ride in on them; it competes with SQLite-as-store purely on being a plain-text, rebuildable-from-events source of truth. The Git-decoupling goal itself is reachable without a log, so the log-vs-SQLite call is a separate, deliberate decision — not a settled premise.

## Closure conditions

Close when it produces:

- a decision on the review store's source-of-truth shape (event log + derived index, or SQLite-as-store), with the snapshot-embedding rule for acceptance events pinned down;
- for each of the other four axes, either a promoted artifact (ADR / reference / note) or an explicit drop with the reason;
- a scoped implementation plan that does not require solving general lineage.

## Working files

- [alternatives-survey.md](./alternatives-survey.md) — the five architecture axes from the `src/` read, with the leverage ordering and the recommendation thread.
- [append-only-log-with-snapshots.md](./append-only-log-with-snapshots.md) — the active thread: event log as source of truth, SQLite as rebuildable index, and why acceptance events must embed their snapshots once Git is no longer the retrieval store.
- [review-lineage-storage-case.md](./review-lineage-storage-case.md) — review lineage as the local storage witness: readable prose, run/pair provenance, append-only acceptance events, and fast current-state selectors.
- [pure-file-review-store-design.md](./pure-file-review-store-design.md) — pure file/directory review-store design and current-scale fan-out estimates, used as the filesystem-backed relation comparison point.
</content>
</invoke>
