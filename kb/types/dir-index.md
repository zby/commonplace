---
type: kb/types/type-spec.md
name: dir-index
description: Fully generated per-directory listing (dir-index.md) enumerating a directory's files with title, description, and type
schema: kb/types/dir-index.schema.yaml
---

# Dir-index

## Authoring Instructions

Do not hand-author a dir-index. It is a fully machine-generated, per-directory enumeration of every file at one directory level, with title, description, and type. Each collection's curated landing lives in `README.md`; `dir-index.md` is the separate, exhaustive listing.

For curated navigation hubs with an editorial section and a generated tail (tag indexes), use [curated-index](./curated-index.md) instead.

## Frontmatter

- `type: kb/types/dir-index.md`
- `index_source: directory` (the only valid source for this type).

The body is entirely generated; there is no hand-written content to maintain.

## Lifecycle

Rebuild with `commonplace-refresh-indexes`, which regenerates every `dir-index.md`. Do not edit the file by hand — changes are overwritten on the next rebuild.
