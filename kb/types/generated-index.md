---
type: types/type-spec.md
name: generated-index
description: Build-time generated listing pages (per-directory dir-index virtual files); committed tag landings use types/tag-readme.md instead
schema: ./generated-index.schema.yaml
---

# Generated index

## Authoring Instructions

Since ADR 026 the `generated-index` type covers **build-time generated pages only** — do not author new committed artifacts with this type. A tag's committed curated head is `kb/tags/<tag>-README.md` of type `types/tag-readme.md` (see that spec, and ADR 089); complete listings are never committed (ADR 025).

The ProperDocs hook materializes index-typed pages at build time:

- `index_source: directory` — per-collection `dir-index.md` virtual pages, a complete inventory of every file with title, description, and type. These exist only in the published site; `dir-index.md` is gitignored.
- The hook also links each tag head on the site to a generated member page; that listing is driven by the head's filename and the tagged artifacts grouped by collection, not by this type.

In a checkout, search collection descriptions with `rg` to find candidates. To enumerate a tag's members, use the [tag membership check](./tag-readme.md#checking-exact-membership).

## Frontmatter

- `index_source: directory` for generated per-directory listings (the only sanctioned use).
- `index_source: tag` and `index_source: tag-indexes` are retired (ADR 089): a tag head is identified by its filename and carries neither field.
