---
type: kb/types/type-spec.md
name: index
description: Build-time generated listing pages (per-directory dir-index virtual files); committed tag landings use kb/types/tag-readme.md instead
schema: kb/types/index.schema.yaml
---

# Index

## Authoring Instructions

Since ADR 026 the `index` type covers **build-time generated pages only** — do not author new committed artifacts with this type. A tag's committed curated head is a `<tag>-README.md` of type `kb/types/tag-readme.md` (see that spec); complete listings are never committed (ADR 025).

The mkdocs hook materializes index-typed pages at build time:

- `index_source: directory` — per-collection `dir-index.md` virtual pages, a complete inventory of every file with title, description, and type. These exist only in the published site; `dir-index.md` is gitignored.
- The hook also appends the generated listing (`tag` / `tag-indexes` sources) to tag-README pages on the site; that machinery accepts both this type and `tag-readme` (the dual-type transition also covers any not-yet-migrated committed tag index).

Agents enumerate the same information with the scoped `rg` recipes in `kb/reference/navigation.md`.

## Frontmatter

- `index_source: directory` for generated per-directory listings (the only sanctioned use).
- `index_source: tag` with `index_key: <tag>` and `index_source: tag-indexes` remain schema-valid for unmigrated committed indexes; migrate these to `kb/types/tag-readme.md` rather than authoring new ones.
