# Index Instructions

Use an index when the document's main job is navigation rather than argument.

- Every index must declare `index_source` in frontmatter.
- Use `index_source: directory` for fully generated per-directory listings.
- Use `index_source: tag` with `index_key: <tag>` for curated tag indexes with a generated tail.
- Use `index_source: tag-indexes` for indexes whose generated section lists tag index pages rather than tagged notes.
- Write a short orientation paragraph explaining what the index covers and how to use it.
- Curated sections should be selective. Do not dump every note; include entries that help a reader navigate.
- Every curated entry should add context, not just a bare link.
- The section containing `<!-- generated -->` is machine-managed. Do not hand-edit below the marker.
- For detailed maintenance workflow, read `kb/instructions/maintain-curated-indexes.md`.
