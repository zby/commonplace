# Sources

Tracked analyses of external articles, papers, GitHub issues, posts, and
repository documents. Their captured reading copies stay local.

Each source is captured under ignored `kb/sources/.snapshots/` and analyzed in
a tracked `*.ingest.md` report. The ingest carries the external URL, capture
provenance, genre, and exact primary-snapshot checksum along with its KB
analysis.

## What's here

- **`.snapshots/`** — ignored local reading copies and capture companions. They
  are not published or distributed with the repository.
- **`*.ingest.md` reports** — tracked source records and analyses produced by
  `cp-skill-ingest`. Each report classifies and summarizes the source and
  connects it to `kb/notes/` and other collections.
- **`types/`** — local type definitions for the artifacts in this collection (`source-review`, `ingest-report`).

## How to add a source

```bash
# URL → snapshot + ingest in one go
cp-skill-ingest https://example.com/some-article

# Or snapshot first, ingest later
cp-skill-snapshot-web https://example.com/some-article
cp-skill-ingest kb/sources/.snapshots/some-article.md
```

The skill chooses the right snapshotting backend based on the URL (GitHub API for issues/PRs, the X SDK for tweets, plain `WebFetch` for everything else).

## Collection conventions

This collection operates in the descriptive register. Local source copies are
captured for fidelity, not transformed; tracked ingests provide the analysis.
Writing conventions for the reports live in
[types/ingest-report.md](./types/ingest-report.md). For the discovery and
connection procedure, see the `cp-skill-ingest` skill.
