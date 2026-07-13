# Deferred: collection-as-artifact freshness

**Status:** not in v1. **Exit:** promote to `kb/reference/proposals/collection-as-artifact-freshness.md` (implementation-plan step 8 / M4).

## Problem

Epistack maintenance must detect when a source collection gains, loses, or changes a member without a pre-existing per-file dependency edge. Per-file `file-text` registration cannot see new members until something registers them.

## Planned approach

A **`collection-text` version function** renders canonical UTF-8 for one `COLLECTION.md`-bearing directory. A **`collection-maintenance` target** registers coarse snapshots as accepted inputs. The freshness core treats these as ordinary path-keyed versions — no source/ingest branches.

## Why deferred

- v1 driver is review migration and global status over registered file paths.
- Encoding + golden tests + three casebook targets expand M1/M3 before review parity is proven.
- Semantic maintenance with per-file edges suffices for current submission work.

## `collection-text` encoding (`COMMONPLACE-COLLECTION-TEXT/1`)

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

## `collection-maintenance` target

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

## Acceptance cases (for proposal / later implementation)

1. adding a source selects exactly its casebook target;
2. editing/removing a source selects that target with diff;
3. adding casebook notes selects its target, not another case — reassessment may revise affected `.ingest.md` even when source snapshot unchanged;
4. unrelated edits select no casebook target;
5. ack of irrelevant source diff preserves accepted casebook snapshot;
6. refresh after note edits replaces full input set;
7. post-acceptance edit makes target immediately stale; and
8. global status reports stale review-pair and collection-maintenance targets together.

## Schema extension

v1 admits `file-text` only. Adoption widens `version_kind` checks and registers first non-review targets via migration.