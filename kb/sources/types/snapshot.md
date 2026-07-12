---
type: kb/types/type-spec.md
name: snapshot
description: Captured external source copy with capture metadata and no analysis
schema: kb/sources/types/snapshot.schema.yaml
---

# Snapshot

## Authoring Instructions

Use `snapshot` for captured external source copies stored under `kb/sources/`.

A snapshot is stamped by capture tooling or a snapshot skill. It is not normally authored directly. The artifact should preserve the source content and capture metadata without analysis; analysis belongs in an adjacent `ingest-report`.

## Metadata

- Set `type: snapshot`.
- Set `source` to the canonical URL of the original source.
- Set `captured` to the capture date or datetime.
- Set `capture` to the capture mechanism, such as `web-fetch`, `pdf-read`, `xdk`, or `gh-api`.
- Set `genre` to the source's genre (see Genre below). This is the single authoritative genre record for the source; ingest reports read it and do not restate it.
- `tags` are optional topical tags. Do not put the content family in `tags` — genre carries it, and the platform or container is already visible from `capture` and the source URL.
- Keep platform-specific metadata such as `status_id`, `conversation_id`, `post_count`, or `api_url` when the capture tool provides it.

## Genre

Classify what kind of document the source is as evidence. The default vocabulary:

- `scientific-paper` for peer-reviewed papers or preprints with methodology, data, or citations.
- `practitioner-report` for reports from someone who built something and describes what worked or failed.
- `conceptual-essay` for framings, analogies, or theoretical positions.
- `design-proposal` for RFCs, API designs, or architecture proposals for a specific system.
- `tool-announcement` for new tool, library, or framework releases.
- `github-issue` for bug reports, feature requests, or PRs from a specific repo.
- `conversation-thread` for discussion without a single authorial thesis.
- `code-repository` for a repository whose implementation, structure, documentation, or project history is the source.
- `court-opinion` for judicial rulings, orders, or opinions issued by a court.
- `news-article` for journalistic reporting on current events from a news outlet.
- `official-statement` for a statement, release, or announcement issued by an organization, agency, or public figure in an official capacity.

The vocabulary is open: a value outside this list validates with a warning, not a failure. Extend deliberately — a new genre should name an evidential kind that recurs, not a one-off container. Genre meanings are fixed everywhere; collections and installed KBs extend the value list, never reinterpret existing values.

Two extension paths:

- **Occasional off-list source:** just use the new value and keep the warning — it is the standing signal of an undocumented genre, and a validation sweep lists every such extension.
- **A KB whose sources need their own vocabulary** (recurring new genres, domain-specific lens guidance, extra capture fields): do not edit this shipped spec. Declare a collection-local snapshot type — drop a type-spec doc and schema into the sources collection's `types/` directory and point `COLLECTION.md`'s Types menu at it; the capture skill stamps whatever snapshot type that menu declares. The local type owns its genre list and lenses outright, with fixed meanings, the same way this spec owns the defaults. Types are the extension point; scaffolded specs are not editing surfaces.

`genre` is stamped at capture as a surface judgment. If ingestion's closer reading disagrees, correct the snapshot's `genre` in place — the snapshot stays the single ground truth.

## Boundaries

- Do not add commentary, claims, or relevance analysis to the snapshot. The single `genre` classification is capture metadata, not analysis.
- Do not use source-family labels as `type:` values.
- Do not create a template for snapshots unless direct human authoring becomes a real workflow.
