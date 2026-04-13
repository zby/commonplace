# Index Instructions

Use an index when the document's main job is navigation rather than argument.

## Frontmatter

- Every index must declare `index_source` in frontmatter.
- Use `index_source: directory` for fully generated per-directory listings.
- Use `index_source: tag` with `index_key: <tag>` for curated tag indexes with a generated tail.
- Use `index_source: tag-indexes` for indexes whose generated section lists tag index pages rather than tagged notes.

## Structure

There are two kinds of indexes:

- **Directory indexes** (`dir-index.md`) — fully auto-generated alphabetical listings of all files with title, description, and type. Each collection's canonical landing lives in `README.md`; `dir-index.md` is the separate per-collection enumeration.
- **Generated-tail indexes** (e.g. `learning-theory-index.md`) — navigation hubs with an optional curated section plus a generated listing.

**Generated-tail structure:**

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
