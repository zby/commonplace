---
type: kb/types/type-spec.md
name: index
description: Curated navigation hub with index metadata; complete generated listings are appended at mkdocs build time, never committed
schema: kb/types/index.schema.yaml
---

# Index

## Authoring Instructions

Use an index when the document's main job is navigation rather than argument.

## Frontmatter

- Every index must declare `index_source` in frontmatter.
- Use `index_source: directory` for complete per-directory listings (build-time only; never committed).
- Use `index_source: tag` with `index_key: <tag>` for curated tag indexes.
- Use `index_source: tag-indexes` for the hub index whose build-time listing enumerates tag index pages rather than tagged notes.

## Structure

Committed index files are **curated heads**: hand-written navigation hubs with editorial groupings and context phrases. Their complete listings are not committed — the mkdocs build appends a generated listing (tagged notes for `tag`, tag-index pages for `tag-indexes`) to the published page, and emits per-collection `dir-index.md` pages as build-time virtual files (ADR 025). Agents enumerate the same information with the scoped `rg` recipes in `kb/reference/navigation.md`.

- **Curated body** (hand-written): editorial groupings with context phrases. Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- **Generated listing** (build-time, automatic): complete listing under a `<!-- generated -->`-marked heading on the published site only; it excludes entries the curated body already links.

## Writing

- Write a short orientation paragraph explaining what the index covers and how to use it.
- Curated sections should be selective. Do not dump every note; include entries that help a reader navigate.
- Every curated entry should add context, not just a bare link.
- Do not hand-write a complete listing — completeness is the build's job and the scoped query's job, not the author's.

## Lifecycle

Create when 5+ related notes accumulate under a tag. Curate when the build-time listing alone isn't enough. Merge when both indexes are small with significant overlap.

For detailed maintenance workflow, read `kb/instructions/maintain-curated-indexes.md`.

## Template

```markdown
---
description: "Template for generated-tail index pages — curated editorial section above a generated listing"
type: kb/types/index.md
index_source: tag
index_key: "{tag-name}"
---

# {tag-name}

{Orientation}

## Notes

- [note](./note.md) — why it matters here

## Decisions

- [decision](../../reference/adr/decision.md) — why it matters here

## Related Tags

- [related-tag-index](./related-tag-index.md) — how it connects
```
