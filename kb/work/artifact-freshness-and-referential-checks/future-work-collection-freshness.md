# Deferred: collection-as-artifact freshness

**Status:** postponed — not part of the current implementation sequence. **Terminal deliverable:** promote this sketch to `kb/reference/proposals/collection-as-artifact-freshness.md` per implementation-plan step 9 (M4).

Epistack maintenance still needs to detect when a source collection gains, loses, or changes a member without a pre-existing per-file dependency edge. The planned workaround is a **`collection-text` version function** and a **`collection-maintenance` target** that registers coarse collection snapshots. That design remains valid but ships in a later phase after review-first migration and generic `file-text` infrastructure are proven.

## Why deferred

- The immediate driver is review freshness migration and repository-wide status over **registered file paths**, not Epistack casebook registration.
- `collection-text` encoding, golden tests, and three casebook targets add M1/M3 surface before the review parity gate earns confidence.
- Per-file `file-text` inputs plus semantic maintenance workflows remain sufficient for submission work until this phase lands.

## Planned version function: `collection-text`

Identity: one normalized `COLLECTION.md`-bearing directory path.

### Encoding (`COMMONPLACE-COLLECTION-TEXT/1`)

`collection-text` is a deterministic UTF-8 byte sequence. The stored snapshot hash is `SHA-256` of those bytes.

**Scope.** One collection root. Membership is non-recursive into nested collection roots — a child directory bearing its own `COLLECTION.md` is a separate collection identity.

**Member enumeration.** Collect every visible regular-file `*.md` under the collection root using `commonplace.lib.project_paths.walk_visible`:

- include files in subdirectories of the collection root;
- exclude dot-prefixed paths and nested git repositories;
- exclude symlinks and non-regular files;
- exclude `COLLECTION.md`;
- exclude any path with a `types/` directory segment between the collection root and the file;
- exclude `.replaced.*.md` archive filenames; and
- do not apply repository-wide artifact-dir pruning inside a collection walk.

Sort members by normalized repository-relative POSIX path with `/` separators.

**Byte layout.**

```text
COMMONPLACE-COLLECTION-TEXT/1
<member-record>*
```

Each `<member-record>`:

```text
--- member
path: <normalized-repo-relative-path>
sha256: <64 lowercase hex of member file UTF-8 bytes>
---
<exact member file UTF-8 text>
```

Delimiter and header lines use ASCII `LF` only. Member bodies are verbatim UTF-8.

## Planned target: `collection-maintenance`

One coarse target per casebook:

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

Equivalent targets for eggs and COVID. Acceptance cases from the implementation plan (source addition selects casebook, diff-backed ack of `source-scope` only, etc.) move here unchanged.

## Schema extension when implemented

v1 store schema ships with `file-text` only. A later migration widens `version_kind` checks to admit `collection-text` and registers the first non-review targets.