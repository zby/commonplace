---
type: kb/types/type-spec.md
name: snapshot
description: Local external source copy with capture metadata and no analysis
schema: kb/sources/types/snapshot.schema.yaml
---

# Snapshot

## Authoring Instructions

Use `snapshot` for captured external source copies stored under
`kb/sources/.snapshots/`.

A snapshot is stamped by capture tooling or a snapshot skill. It is not
normally authored directly. It preserves source content and capture metadata
without analysis. It is a local, ignored reading copy; durable identity,
provenance, genre, checksum, and analysis belong in the tracked
`kb/sources/<slug>.ingest.md` report.

## Metadata

- Set `type: kb/sources/types/snapshot.md`.
- Set `source` to the canonical URL of the original source.
- Set `captured` to the capture date or datetime.
- Set `capture` to the capture mechanism, such as `trafilatura`, `pdftotext`,
  `xdk`, or `gh-api`.
- `genre` is optional capture-time metadata. The ingest report is the durable
  genre authority and may correct this surface classification after reading.
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

The vocabulary is open: a value outside this list validates with a warning,
not a failure. Extend deliberately — a new genre should name an evidential
kind that recurs, not a one-off container. Genre meanings are fixed everywhere.
The ingest-report schema carries the same warned list because the tracked
ingest, not this local capture, is the durable genre authority.

Two extension paths:

- **Occasional off-list source:** just use the new value and keep the warning — it is the standing signal of an undocumented genre, and a validation sweep lists every such extension.
- **A KB with recurring local genres or domain-specific ingest lenses:** v1 has
  no operative local extension path for the durable ingest vocabulary. A
  collection-local snapshot type may govern extra capture fields or
  capture-time hints, but it cannot change the fixed ingest-report type that
  validates the tracked `genre` or supplies its Limitations lenses. Keep
  off-list values warned until a durable ingest-side extension mechanism is
  adopted; do not present a local snapshot type as if it changed ingest
  semantics.

When present, `genre` is a surface judgment made at capture. Ingestion's closer
reading sets the durable value on the ingest without rewriting the captured
file, because doing so would change its exact-file checksum.

## Boundaries

- Do not add commentary, claims, or relevance analysis to the snapshot. The single `genre` classification is capture metadata, not analysis.
- Do not link a tracked artifact to a local snapshot. Use the ingest or the
  external source URL according to what the sentence cites.
- Do not use source-family labels as `type:` values.
- Do not create a template for snapshots unless direct human authoring becomes a real workflow.
