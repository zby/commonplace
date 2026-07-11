---
description: "Semantic Engine as code-grounded ingest infrastructure: local SQLite datasets, source chunking, embeddings, query, and visualization surfaces useful before KB promotion."
type: kb/types/note.md
traits: [has-external-sources]
tags: []
---

# Semantic Engine as ingest infrastructure

**Evidence basis:** first-hand reading of the `Open-Research-Institute/semantic-engine` checkout at commit [7e248167](https://github.com/Open-Research-Institute/semantic-engine/commit/7e2481671cad01f0b4c89f2a1877d6733d7e552c) (2026-06-25).

Semantic Engine is not an agentic runtime and not an agent-memory system. It has no agent loop, scheduling surface, tool-use orchestration, prompt/context injector, durable agent trace, or policy layer for how retrieved material should bind future actions. Its useful shape for Commonplace is narrower: it is a prototype ingest and exploration pipeline for turning external document streams into local SQLite datasets, embeddings, query results, and map-like visualizations before any material is promoted into reviewed KB artifacts.

> The ORI semantic engine is a modular pipeline for ingesting, embedding and visualizing diverse documents and their relationships to each-other
> --- [README.md](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/README.md)

## Implemented Pipeline

The implemented center is `apps/semantic-engine-cli`: a Bun/TypeScript CLI that selects a local `DATASET_ID.sqlite`, defines `docs` and `chunks` tables through Drizzle, imports community-archive tweets and RSS entries, chunks source text, embeds chunks through an OpenAI-compatible LMStudio endpoint, and ranks chunks by cosine vector distance ([db/db.ts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/db/db.ts), [db/schema.ts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/db/schema.ts), [embed-documents.mts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/embed-documents.mts), [query-documents.mts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/query-documents.mts)).

The retained source unit is a root document plus positional chunks. `load-archives.mts` filters and groups tweet material from downloaded archive files; `load-from-rss.mts` converts feed item HTML to Markdown; both insert root documents and split chunk rows. The splitter tracks `startPosition` and `endPosition`, and its tests check contiguous reconstruction, which is the most directly reusable quality gate in the repo ([load-archives.mts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/load-archives.mts), [load-from-rss.mts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/load-from-rss.mts), [split-text.ts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/lib/utils/split-text.ts), [split-text.test.ts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/lib/utils/split-text.test.ts)).

Retrieval is exploration, not activation. The query script embeds the query, fetches `limit * 5` similar chunks, deduplicates to root documents, and prints full document contents with source metadata. There is no token budget, source-grounded answer synthesis, or automatic path into an agent context window. That makes the system closer to a corpus workbench than to a memory substrate.

## Ingest Lessons for Commonplace

**Dataset-per-file staging is a useful boundary.** Separate SQLite files keyed by `DATASET_ID` would fit a Commonplace ingest workbench: one source corpus can be downloaded, chunked, embedded, searched, and discarded without becoming part of the canonical Markdown library.

**Chunk offsets need deterministic tests.** The splitter's reconstruction tests are a small but important bar. If Commonplace adds a high-volume ingest stage, quote spans and source-backed chunks should be testable before any agent uses them as evidence.

**Embedding search should stay pre-review.** Semantic Engine's vector ranking is useful for recall and triage, but it does not decide what is true, relevant enough for a note, or safe to load into a future agent call. A Commonplace ingest pipeline should preserve that boundary: embeddings can propose candidates; reviewed notes, schemas, and validators carry authority.

**Visualization is useful for corpus triage.** `apps/infinite-canvas-viewer` reads embeddings, projects them with PCA, writes GeoJSON, and renders a MapLibre view ([process-embeddings.mjs](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/infinite-canvas-viewer/process-embeddings.mjs), [pca.js](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/infinite-canvas-viewer/pca.js), [src/index.js](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/infinite-canvas-viewer/src/index.js)). That shape could help an operator see clusters before writing notes, as long as the view remains exploratory rather than an implied ontology.

**Provider-swappable local embeddings are the right default for optional indexes.** The CLI points an OpenAI-compatible client at LMStudio on `localhost:1234`, which is a good dependency boundary for an optional ingest index: local when possible, provider-swappable when needed, and not part of deterministic validation.

## What Not To Import

The repo also shows boundaries Commonplace should not inherit directly.

The React UI is still the default Vite counter template, so the usable system is the CLI plus small browser prototypes rather than a finished operator surface ([App.tsx](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-ui/src/App.tsx)).

The Nomic Atlas export path appears stale at this revision: the Python model expects document-level embeddings and column names such as `source` and `creatorId`, while the current TypeScript schema stores embeddings on `chunks` and uses `origin` and `author`; the script also places `db_url` inside the missing-`DATASET_ID` branch ([push-to-nomic-atlas.py](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py), [models.py](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/db/models.py), [schema.ts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/db/schema.ts)).

The community-archive downloader depends on a specific hosted Supabase bucket and includes a public anonymous key in source. That may be intentional, but it means the acquisition path is not purely local or source-agnostic ([download-archives.mts](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/download-archives.mts)).

## Reading Against Commonplace

Commonplace should read Semantic Engine as an operational layer below the KB, not as a replacement knowledge system. Its natural insertion point is before source snapshots and notes: acquire a large external corpus, preserve raw rows and chunk offsets, build optional embeddings, use search or maps to choose what deserves attention, then promote selected material through the normal source snapshot, ingest, note-writing, and validation paths.

The useful distinction is between discovery and commitment. Semantic Engine improves discovery over a source corpus; Commonplace needs commitment artifacts. Moving data from the first to the second should require a source-preserving distillation step, not a direct vector-search-to-note shortcut.

## What to Watch

- Whether the CLI adds reproducible source-span export; that would make it more directly useful for quote-grounded ingest.
- Whether duplicate detection, stale-source invalidation, or re-ingest reconciliation appear; those would make the staging database safer for repeated corpus refreshes.
- Whether the UI becomes a real operator surface for selecting, annotating, and exporting candidate material.
- Whether the Nomic export is reconciled with the current chunk schema or removed.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) - see-also: explains why storing and retrieving documents does not by itself make Semantic Engine an agent-memory system.
- [Storage substrate](../notes/definitions/storage-substrate.md) - see-also: frames the staging choice as SQLite/files/repo rather than canonical KB storage.
- [Representational form](../notes/definitions/representational-form.md) - see-also: distinguishes prose source text, symbolic chunk metadata, and parametric embeddings in the ingest layer.
