---
description: Handle a request to ingest a directory without admitting a directory as a v1 primary source.
type: kb/types/instruction.md
---

# Do not ingest a directory as a primary source

V1 ingest reports require one URL-backed primary source and one primary
Markdown snapshot. A directory path, checkout path, or grouped file bundle is
not a supported primary input.

When asked to ingest a directory:

1. Stop before drafting an ingest or inventing source metadata.
2. Identify the single public URL whose document is the primary source.
3. If that source is a paper and the directory is one or more implementation
   repositories, follow `ingest-paper-with-code.md`. Record each inspected
   repository as a commit-pinned `implementation` secondary and keep its
   checkout under ignored `related-systems/`.
4. If the directory is one repository used as the primary source, choose a
   URL-backed repository document or immutable public revision as the primary,
   materialize one Markdown reading copy under `kb/sources/.snapshots/`, and
   use `cp-skill-ingest` on that file.
5. If no single URL-backed primary can be identified, report that v1 cannot
   represent the request. Do not create a partial ingest.

Do not write `source_snapshot`, encode a local path in `source`, hash a
directory, or invent a secondary role for files that are merely members of the
primary source.
