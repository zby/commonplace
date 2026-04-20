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
- Put the content family in `tags`, for example `academic-paper`, `blog-post`, `x-post`, or `github-issue`.
- Keep platform-specific metadata such as `status_id`, `conversation_id`, `post_count`, or `api_url` when the capture tool provides it.

## Boundaries

- Do not add commentary, claims, or relevance analysis to the snapshot.
- Do not use source-family labels as `type:` values.
- Do not create a template for snapshots unless direct human authoring becomes a real workflow.
