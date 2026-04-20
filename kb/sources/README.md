# Sources

External sources snapshotted into the KB — articles, papers, GitHub issues, tweets, repository READMEs — along with their ingest reports.

Each source is captured verbatim into a file at the time of snapshot and analyzed in a paired `*.ingest.md` report that classifies it, extracts claims, and links it into the rest of the KB.

## What's here

- **Source snapshots** — one file per snapshotted external artifact, with a short header noting the URL and capture date followed by the verbatim content.
- **`*.ingest.md` reports** — the analyses produced by `cp-skill-ingest`. Each report names the source, classifies it as a related system / paper / article / etc., summarises the load-bearing claims, and proposes connections into `kb/notes/` and other collections.
- **`types/`** — local type definitions for the artifacts in this collection (`source-review`, `ingest-report`).
- **[dir-index.md](./dir-index.md)** — auto-generated alphabetical listing of every file in this collection.

## How to add a source

```bash
# URL → snapshot + ingest in one go
cp-skill-ingest https://example.com/some-article

# Or snapshot first, ingest later
cp-skill-snapshot-web https://example.com/some-article
cp-skill-ingest kb/sources/some-article.md
```

The skill chooses the right snapshotting backend based on the URL (GitHub API for issues/PRs, the X SDK for tweets, plain `WebFetch` for everything else).

## Collection conventions

This collection operates in the descriptive register — sources are captured for fidelity, not transformed. Writing conventions for the `*.ingest.md` reports live in [types/ingest-report.md](./types/ingest-report.md). For the discovery and connection conventions used during ingest, see the `cp-skill-ingest` skill.
