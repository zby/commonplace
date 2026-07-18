---
description: "Proposal: register collection-maintenance targets with collection-text inputs for casebook-wide staleness without per-file dependency edges"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, observability]
---

# Collection-as-artifact freshness

Epistack maintenance must detect when a source collection gains, loses, or changes a member without a pre-existing per-file dependency edge. Shipped v1 freshness registers only `file-text` inputs on `review-pair` targets in `commonplace-store.sqlite` ([ADR 052](../adr/052-general-freshness-store-review-first-migration.md)). Per-file registration cannot see new members until something explicitly accepts them.

## Current state (as of 2026-07-13)

- General freshness substrate is shipped: `artifact_snapshots`, `freshness_baselines`, `freshness_inputs`, and `commonplace-freshness-{status,accept,ack,retire}` over registered targets.
- v1 admits `file-text` only and `review-pair` targets only; generic accept rejects `review-pair`.
- Review parity (selector discovery, capture finalization, observation ack, pruning) is an adapter over the generic tables.
- Epistack casebook maintenance still relies on per-file `file-text` edges plus semantic workflows; no `collection-text` encoder or `collection-maintenance` targets are registered.
- Workshop exploration lives at `kb/work/artifact-freshness-and-referential-checks/future-work-collection-freshness.md`.

## Problem

A casebook spans a notes collection, a sources collection, and a `COLLECTION.md` contract. Adding or removing a source file changes what "current" means for the casebook even when no individual accepted per-file edge existed for that path. Operators need coarse collection snapshots as accepted inputs without inferring dependencies from links.

## Planned approach

A **`collection-text` version function** renders canonical UTF-8 for one `COLLECTION.md`-bearing directory. A **`collection-maintenance` target** registers coarse snapshots as accepted inputs. The freshness core treats these as ordinary path-keyed versions — no source/ingest branches.

### `collection-text` encoding (`COMMONPLACE-COLLECTION-TEXT/1`)

Deterministic UTF-8; hash = SHA-256(bytes).

**Scope:** one collection root; exclude nested collection roots (child `COLLECTION.md` = separate identity).

**Members:** visible regular `*.md` under root via `project_paths.walk_visible` — include subdirs; exclude dots, nested git repos, symlinks, `COLLECTION.md`, `types/` segments, `.replaced.*.md`; no repo artifact-dir pruning inside collection.

Sort by normalized repo-relative POSIX path.

```text
COMMONPLACE-COLLECTION-TEXT/1
--- member
path: <path>
sha256: <64 hex>
---
<verbatim file UTF-8>
```

### `collection-maintenance` target shape

One target per casebook (lhc, eggs, COVID):

```json
{
  "target_kind": "collection-maintenance",
  "target_key": {"collection_path": "kb/lhc/notes"},
  "inputs": {
    "casebook": {"version_kind": "collection-text", "path": "kb/lhc/notes"},
    "source-scope": {"version_kind": "collection-text", "path": "kb/lhc/sources"},
    "contract": {"version_kind": "file-text", "path": "kb/lhc/notes/COLLECTION.md"}
  }
}
```

## Acceptance cases

1. adding a source selects exactly its casebook target;
2. editing/removing a source selects that target with diff;
3. adding casebook notes selects its target, not another case — reassessment may revise affected `.ingest.md` even when source snapshot unchanged;
4. unrelated edits select no casebook target;
5. ack of irrelevant source diff preserves accepted casebook snapshot;
6. refresh after note edits replaces full input set;
7. post-acceptance edit makes target immediately stale; and
8. global status reports stale review-pair and collection-maintenance targets together.

## Relation to document-set specs

The bulk-operations workshop frames the more general problem. Structures bigger than a single document need a **document-set spec**: membership rule, member types, cross-member obligations, derived views, set-level validation, and lineage to the corpus so a diff yields a targeted refresh list. Bulk operations consume that spec through select → shard → execute → validate → close.

This proposal is deliberately narrower. `collection-text` answers only whether the *set of files* in a collection directory changed since last acceptance. `collection-maintenance` registers a coarse casebook tripwire — not which downstream artifacts are obligated to track that membership (for example which `.ingest.md` files must keep `Connections Found` current). Epistack ingest decay is a set-level obligation failure; a document-set spec would encode and validate the obligation; collection freshness only signals that casebook maintenance may be due.

Set-level dependencies are uncommon. When they matter enough to automate, investing in document-set specs and bulk refresh likely dominates registering coarse `collection-maintenance` targets. `collection-text` may still ship as a cheap encoding primitive on the v1 freshness substrate, or as one detection signal inside a later lineage-driven refresh layer — but it is not the general approach. Workshop dependency runs one way: document-set specs are useful without this proposal; this proposal does not subsume bulk operations.

## Forces

- **Encoding cost.** `collection-text` needs golden tests and a documented exclusion policy before registration is trustworthy.
- **Blast radius.** Collection snapshots stale whole casebooks; operators need diffs and ack surfaces that scale to multi-input targets.
- **Supersession risk.** A standing document-set spec with member→source lineage gives finer refresh targets than whole-collection hashing; `collection-maintenance` targets may become redundant once that lands.
- **v1 deferral was deliberate.** Review migration and global status over file paths had to land first ([ADR 052](../adr/052-general-freshness-store-review-first-migration.md)).

## Free choices

- Whether `collection-text` shares `artifact_snapshots` rows or uses a parallel render cache.
- How global status labels `collection-maintenance` changed inputs in JSON (role names vs path-only).
- Whether first adoption registers Epistack casebooks via migration script or manual accept manifests.

## Adoption criteria

- Epistack submission work needs casebook-wide selection without hand-maintaining per-new-file edges.
- `collection-text` encoder passes golden fixtures for add/remove/rename cases.
- Generic accept/ack/retire are exercised on at least one non-review target in CI.
- Schema widening (`version_kind` checks, resolver dispatch) is recorded in a follow-on ADR when implemented.

## Rationale

- [Link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — the general pattern this proposal extends to collection granularity.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — collection maintenance spans library and workshop boundaries.