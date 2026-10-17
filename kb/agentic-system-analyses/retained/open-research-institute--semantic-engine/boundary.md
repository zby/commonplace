---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ORI Semantic Engine's document ingestion, embedding, retrieval and visualization paths at commit 7e2481671cad01f0b4c89f2a1877d6733d7e552c."
run-id: AAS-2026-10-17-semantic-engine-666c064cd8dc-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7e2481671cad01f0b4c89f2a1877d6733d7e552c"
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/Open-Research-Institute/semantic-engine
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-semantic-engine/related-systems/Open-Research-Institute--semantic-engine
  revision: 7e2481671cad01f0b4c89f2a1877d6733d7e552c
  sha256: null
---

# Semantic Engine boundary

## Boundary and evidence

ORI Semantic Engine is in scope as a **memory/knowledge/context-engineering system**: an operator-driven document store and semantic retrieval/visualization pipeline whose embedding and query paths issue model calls. It is not classified as an autonomous agent runtime. Its declared intended use is ingesting, embedding and visualizing documents and their relationships (SRC-1, `README.md`).

> The ORI semantic engine is a modular pipeline for ingesting, embedding and visualizing diverse documents and their relationships to each-other
> --- `README.md`

The boundary is **whole-system**, covering the shipped CLI drivers, their persistent state and later consumers, the visualization prototype, the separate document-similarity page, and the UI scaffold. It does not narrow the target to the embedding API. “Whole-system” describes functional source coverage, not successful integration or demonstrated operation. The checkout HEAD matches the frozen commit; inspection found no working-tree changes. Evidence is code-grounded at **7e2481671cad01f0b4c89f2a1877d6733d7e552c**, with an applicability cutoff of **2026-10-17**. No later revision or live service response supplies evidence.

### Entry points and retained-state loop

The root workspace manifest has no commands; the CLI README supplies the operating sequence, and the CLI manifest supplies database initialization and Nomic login commands (SRC-1, `package.json`, `apps/semantic-engine-cli/package.json`, `apps/semantic-engine-cli/README.md`). The following shipped responsibilities are included:

- **Acquire and admit:** `apps/semantic-engine-cli/scripts/download-archives.mts` downloads archives to local files. `apps/semantic-engine-cli/scripts/load-archives.mts` filters tweets, constructs threads, and inserts documents and chunks. `apps/semantic-engine-cli/scripts/load-from-rss.mts` fetches RSS, converts HTML to Markdown and inserts documents and chunks. These are system drivers, not excluded enclosing applications (SRC-1, those paths).
- **Persist and maintain:** `apps/semantic-engine-cli/db/db.ts`, `apps/semantic-engine-cli/db/schema.ts`, `apps/semantic-engine-cli/db/types/vector.ts` and `apps/semantic-engine-cli/drizzle.config.ts` define the dataset-selected SQLite connection, document/chunk state, vector representation and schema setup. `apps/semantic-engine-cli/scripts/embed-documents.mts` reads chunks lacking embeddings, calls LMStudio and updates chunk embeddings. `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts` clears retained embeddings (SRC-1, those paths).
- **Reload and consume:** `apps/semantic-engine-cli/scripts/query-documents.mts` embeds a CLI query, scores stored chunks, reloads root documents, and prints ranked results. `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py` and `apps/semantic-engine-cli/db/models.py` supply a separate export path. The latter is included as shipped code, not presumed compatible with the current TypeScript schema (SRC-1, those paths).
- **Project and display:** `apps/infinite-canvas-viewer/process-embeddings.mjs` reads joined documents/chunks, calls `apps/infinite-canvas-viewer/pca.js`, and writes GeoJSON. `apps/infinite-canvas-viewer/index.html` loads `apps/infinite-canvas-viewer/src/index.js`, which fetches per-user GeoJSON and displays an interactive map. `apps/infinite-canvas-viewer/cluster.js` supplies the imported clustering helper, although its invocation in the processing driver is commented out. Export paths, embedding representations and generated/loaded filenames require assessment rather than an assumption of a working end-to-end route (SRC-1, those paths).
- **Independent similarity tool:** `apps/knowledge-gate/index.html` reads two text areas, requests OpenAI embeddings and displays cosine similarity. It is included as a shipped subproject; the inspected page is not a document-store admission gate (SRC-1, `apps/knowledge-gate/index.html`, `apps/knowledge-gate/README.md`).
- **UI and evaluation surfaces:** the UI entry chain is `apps/semantic-engine-ui/index.html` → `apps/semantic-engine-ui/src/main.tsx` → `apps/semantic-engine-ui/src/App.tsx`; the inspected App is a Vite/React counter scaffold, not a retained-document consumer. `apps/semantic-engine-cli/lib/utils/split-text.test.ts` supplies authored chunking checks, not observed test results or retrieval-quality evaluation (SRC-1, those paths).

The model dependence is explicit in the chunk-embedding driver:

> const { embeddings } = await embedMany({
>     model: lmstudio.textEmbeddingModel(process.env.LMSTUDIO_EMBEDDING_MODEL!),
>     values: currentChunks.map(chunk => chunk.content),
> });
> --- `apps/semantic-engine-cli/scripts/embed-documents.mts`

The later consumer generates a fresh query embedding rather than merely browsing stored text:

> const { embedding } = await embed({
>     model: lmstudio.textEmbeddingModel(QUERY_EMBEDDING_MODEL!),
>     value: query,
> });
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

The separate browser tool also issues model calls:

> const response = await fetch('https://api.openai.com/v1/embeddings', {
> --- `apps/knowledge-gate/index.html`

### Repository coverage

The table accounts for every top-level tracked entry. All material application paths above were inspected. Inclusion permits later inspection at the same frozen commit; it does not claim every supporting byte has already been read.

| Top-level tracked entry | Classification and material paths | Inspection status, role and prevented conclusion |
| --- | --- | --- |
| `.gitignore` | Included: root ignore rule | Inspected; excludes node_modules from tracking. No dependency implementation is thereby frozen as repository code. |
| `README.md` | Included | Inspected; declared purpose and four-subproject inventory. Documentation is intent, not proof of integration. |
| `package.json` | Included | Inspected; workspace layout and empty root scripts. |
| `bun.lock` | Excluded from behavioral analysis | Available, deliberately not inspected; dependency resolution metadata. No claim of reproducible installation or exact transitive-dependency behavior is supported. |
| `apps/` — CLI | Included: `apps/semantic-engine-cli/README.md`, `apps/semantic-engine-cli/package.json`, all seven scripts named above, database files, `.env.template`, `drizzle.config.ts`, `lib/utils/split-text.ts`, `lib/utils/split-text.test.ts`, `lib/community-archive/client.ts`, `lib/community-archive/community-archive.ts`, `lib/community-archive/types.ts` | Drivers, schema, model configuration, chunker, tests, client and generated API declarations were inspected; archive `types.ts` remains available but not yet inspected. This is not an access gap. Generated API declarations describe the external service interface, not its implementation. |
| `apps/` — canvas | Included: `apps/infinite-canvas-viewer/README.md`, `apps/infinite-canvas-viewer/package.json`, `apps/infinite-canvas-viewer/index.html`, `apps/infinite-canvas-viewer/process-embeddings.mjs`, `apps/infinite-canvas-viewer/pca.js`, `apps/infinite-canvas-viewer/cluster.js`, `apps/infinite-canvas-viewer/src/index.js` | Inspected; persistence consumer, dimensionality reduction, optional clustering helper and browser visualization. |
| `apps/` — similarity | Included: `apps/knowledge-gate/README.md`, `apps/knowledge-gate/index.html` | Inspected; standalone model-backed text comparison. No persistence/admission responsibility is inferred from the name “gate.” |
| `apps/` — UI | Included: `apps/semantic-engine-ui/README.md`, `apps/semantic-engine-ui/package.json`, `apps/semantic-engine-ui/index.html`, `apps/semantic-engine-ui/src/main.tsx`, `apps/semantic-engine-ui/src/App.tsx` | Inspected; template documentation and scaffold entry chain. No implemented semantic-engine integration is inferred. |
| `apps/` — supporting material | Included but not yet inspected: app-local ignore rules, CLI LICENSE, CLI `pyproject.toml` and `tsconfig.json`, app Vite/TypeScript/ESLint configuration, CSS and SVG assets; CLI `lib/community-archive/openapi.json` | Available support/configuration material, not an access gap. No build, dependency-installation, licensing or styling audit is claimed. The generated TypeScript API declarations were read instead of the raw OpenAPI document; no external-service conformance conclusion follows. |
| `apps/` — retained sample and lockfiles | Excluded: `apps/infinite-canvas-viewer/cluster-results.json`, `apps/infinite-canvas-viewer/pnpm-lock.yaml`, `apps/infinite-canvas-viewer/yarn.lock` | Available, deliberately not inspected. The clustering sample is not treated as an observed run or quality evaluation; dependency reproducibility and provenance of the sample cannot be concluded. The inspected entry chain does not load that JSON file (SRC-1, `apps/infinite-canvas-viewer/process-embeddings.mjs`, `apps/infinite-canvas-viewer/src/index.js`). |

The tracked tree and the inspected operating instructions provide no separate shipped agent prompt or model-authored maintenance-instruction path. The CLI README, schema setup, embedding driver and clearing script are the operating/maintenance surfaces covered here. This statement is bounded to this commit, not to deployments or untracked operator workflows (SRC-1, `apps/semantic-engine-cli/README.md`, `apps/semantic-engine-cli/scripts/embed-documents.mts`, `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts`).

### External dependencies and evidence limits

LMStudio and its configured embedding model, the OpenAI embedding service, Community Archive/Supabase storage, RSS publishers, Nomic Atlas, SQLite/libSQL and third-party JS/Python libraries are external implementations. MapLibre's remote map style and the outbound tweet links also leave the repository. Their call sites and configuration are included; the external implementations, credentials, datasets and service responses are not frozen here (SRC-1, `apps/semantic-engine-cli/.env.template`, `apps/semantic-engine-cli/package.json`, the CLI drivers above, `apps/knowledge-gate/index.html`, `apps/infinite-canvas-viewer/src/index.js`). Consequently this analysis cannot establish provider quality, live availability, corpus quality, deployment behavior, or external-service guarantees.

No target code, tests, examples or services were executed. There is no registered execution trace or controlled experiment. Source coverage supports an account of implemented and declared responsibilities, not successful end-to-end operation, retrieval effectiveness, reliability, latency, or causal improvement. A source-level incompatibility is not an unavailable path and does not silently remove that path from the boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/Open-Research-Institute/semantic-engine` | 7e2481671cad01f0b4c89f2a1877d6733d7e552c | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-semantic-engine/related-systems/Open-Research-Institute--semantic-engine`. Implementation: all CLI scripts, database files, vector adapter, chunker/tests, Community Archive client/generated declarations; canvas processing/PCA/clustering/display; Knowledge Gate page; UI entry chain and manifests, as detailed above. Doctrine/design: root and four application READMEs, CLI environment template and schema configuration. | Implementation: [embedding driver](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/embed-documents.mts), [retrieval consumer](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/scripts/query-documents.mts), [canvas driver](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/infinite-canvas-viewer/process-embeddings.mjs), [similarity page](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/knowledge-gate/index.html). Doctrine/design: [root README](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/README.md), [CLI operating instructions](https://github.com/Open-Research-Institute/semantic-engine/blob/7e2481671cad01f0b4c89f2a1877d6733d7e552c/apps/semantic-engine-cli/README.md). | No repository access gap encountered. Uninspected support files and deliberate exclusions are distinguished above. External dependencies and unregistered execution evidence prevent operational, quality and causal conclusions; documentation supplies intent only. |
