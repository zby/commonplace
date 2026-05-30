---
type: kb/types/type-spec.md
name: curated-index
description: Curated navigation hub with a hand-written editorial section above a machine-managed generated listing
schema: kb/types/curated-index.schema.yaml
---

# Curated-index

## Authoring Instructions

Use a curated-index when the document's main job is navigation rather than argument, and a human editorial section adds value over a bare listing. A curated-index pairs an optional hand-written section with a generated tail.

For fully generated per-directory listings (`dir-index.md`), use [dir-index](./dir-index.md) instead — those carry no authoring contract.

## Frontmatter

- `type: kb/types/curated-index.md`
- Every curated-index must declare `index_source` in frontmatter.
- Use `index_source: tag` with `index_key: <tag>` for curated tag indexes with a generated tail.
- Use `index_source: tag-indexes` for indexes whose generated section lists tag index pages rather than tagged notes.

## Structure

- **Curated section** (optional, hand-written): editorial groupings with context phrases. Curated entries MUST have context phrases — a bare link list is an address book, not a map.
- **Generated section** (automatic): complete listing below the `<!-- generated -->` marker, rebuilt by `commonplace-sync-generated-index`.

## Writing

- Write a short orientation paragraph explaining what the index covers and how to use it.
- Curated sections should be selective. Do not dump every note; include entries that help a reader navigate.
- Every curated entry should add context, not just a bare link.
- The section containing `<!-- generated -->` is machine-managed. Do not hand-edit below the marker.

## Lifecycle

Create when 5+ related notes accumulate under a tag. Curate when the generated listing alone isn't enough. Merge when both indexes are small with significant overlap.

Rebuild with `commonplace-refresh-indexes`. For detailed maintenance workflow, read `kb/instructions/maintain-curated-indexes.md`.

## Template

```markdown
---
description: "Template for curated-index pages — curated editorial section above a generated listing"
type: kb/types/curated-index.md
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

## Other tagged notes <!-- generated -->
```
