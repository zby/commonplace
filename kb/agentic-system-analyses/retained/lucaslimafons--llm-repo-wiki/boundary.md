---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Repo Wiki's shipped knowledge-production and consumption system at commit 38a439cd649105c0cd90b687fc1f8d8dd1d0986c."
run-id: AAS-2026-11-09-llm-repo-wiki-55aae7f87b1b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "38a439cd649105c0cd90b687fc1f8d8dd1d0986c"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/lucaslimafons/llm-repo-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-repo-wiki-bf93d895d69f/related-systems/lucaslimafons--llm-repo-wiki
  revision: "38a439cd649105c0cd90b687fc1f8d8dd1d0986c"
  sha256: null
---

# LLM Repo Wiki boundary

## Boundary and evidence

This run covers LLM Repo Wiki as a shipped, local knowledge system over GitHub repositories, not just its MCP server or author API. Its intended use is to ingest repository evidence, propose and maintain wiki pages, admit human-reviewed revisions, and answer questions from retained code and wiki content. The target class is `memory/knowledge/context-engineering system`; the boundary kind is `whole-system`. The repository ships the producers, review surface, persistence and later consumers within the same application (SRC-1, `README.md`, `package.json`, `src/worker.ts`, `src/app/w/[wiki]/actions.ts`, `src/agent/chat.ts`, `src/mcp/server.ts`).

The model-dependent production path is explicit in implementation: the author job retrieves evidence in code and calls a language model to draft structured pages. Its own explanation distinguishes this from a model-controlled retrieval loop (SRC-1, `src/agent/author.ts`):

> // The job retrieves and the model only writes: tools + JSON output in one loop let models skip
> // searching (or never stop), and evidence we chose is evidence we can check citations against.
> --- `src/agent/author.ts`

Shipped writing instructions also participate in operation, rather than merely documenting it. The prompt loader reads `WIKI_SCHEMA.md` per call, and both author and chat instructions incorporate it (SRC-1, `src/agent/prompts.ts`). The schema states:

> The rules the author agent follows when it writes this wiki. This file is part of the agent's
> system prompt, so edit it to change how the wiki is written.
> --- `WIKI_SCHEMA.md`

### Included loop and entry points

The following trace fixes the functional boundary. It establishes coverage, not that every implementation detail has already been analysed.

- `package.json` exposes the Next.js application, separate `src/worker.ts`, stdio `src/mcp/server.ts`, repository-add CLI, export CLI and evaluation/benchmark drivers. The worker registers ingestion, wiki-maintenance and author jobs (SRC-1, `package.json`, `src/worker.ts`).
- Ingestion jobs bind GitHub, embedding, chunking, stale-page marking and author scheduling. The sync path marks affected pages stale and enqueues authoring after changed-file work. Thus acquisition and refresh are inside the target, not assumed responsibilities of an external host (SRC-1, `src/ingest/jobs.ts`, `src/ingest/sync.ts`).
- Author-job registration injects the wiki-scoped store, search and model. Authoring loads project context and the schema, reads existing pages, gathers source hits, and calls `generateText`. Initial and incremental authoring belong to the same boundary (SRC-1, `src/agent/jobs.ts`, `src/agent/author.ts`, `src/agent/prompts.ts`).
- Server actions implement human editing, acceptance, rejection, bulk decisions and reversion. Store acceptance checks the proposal's parent revision, updates the current revision and schedules indexing. The index-page job embeds accepted page sections into `wikiChunks`. This is the admission-to-retrieval connection, not an excluded UI concern (SRC-1, `src/app/w/[wiki]/actions.ts`, `src/wiki/review.ts`, `src/wiki/store.ts`, `src/ingest/index-page.ts`).
- The shipped page route reloads stored content, citations, stale-file information and proposals for display and review. Chat reloads server-side messages, builds context from summary, schema, tree and project context, runs a tool-loop agent, and saves responses. Context folding persists a model-written summary for later turns (SRC-1, `src/app/w/[wiki]/wiki/[...path]/page.tsx`, `src/app/api/w/[wiki]/chat/route.ts`, `src/agent/chat.ts`, `src/agent/context.ts`).
- Hybrid search is shared by the application and MCP dependency wiring. The MCP server serves search, page reads, page lists, freshness and sync requests for one wiki. Export reloads accepted revisions and emits Markdown. These are material consumers of retained state, so all are included (SRC-1, `src/search/index.ts`, `src/mcp/server.ts`, `src/export/cli.ts`, `src/export/export.ts`).
- Daily wiki lint is registered by the worker. Evaluation and benchmark drivers are included as shipped measurement machinery; their presence is not evidence that this run executed them (SRC-1, `src/wiki/jobs.ts`, `eval/run.ts`, `package.json`).

### Top-level tracked coverage

The tracked tree was inspected at the frozen commit. Every top-level tracked item is classified below. “Included” establishes scope for later inspection, not a claim to have read every blob. Paths named as initially traced were read or searched; remaining included files are available but not yet substantively inspected. No material shipped path was inaccessible.

| Top-level tracked item | Classification and role | Initial inspection and remaining limits |
|---|---|---|
| `src/` | Included: application, worker, persistence, ingestion, author/chat, retrieval, review, MCP, export, project/wiki isolation, UI and tests | Traced `worker.ts`, `ingest/jobs.ts`, `ingest/sync.ts`, `ingest/index-page.ts`, `agent/jobs.ts`, `agent/author.ts`, `agent/chat.ts`, `agent/context.ts`, `agent/prompts.ts`, `wiki/store.ts`, `wiki/review.ts`, `wiki/jobs.ts`, `search/index.ts`, `mcp/server.ts`, `export/cli.ts`, `export/export.ts`, application chat/page routes and wiki actions. Some were bounded reads or searches. Remaining components, handlers, tests and supporting modules are included and available, not an access gap. |
| `WIKI_SCHEMA.md` | Included: model-consumed writing and maintenance instructions | Read with prompt loader and consumers. |
| `scripts/` | Included: repository admission, author/chat/MCP benchmarks, citation evaluation and MCP smoke driver | Read `scripts/add-repo.ts`; other driver entry points identified through `package.json` and tracked tree, not yet substantively inspected. |
| `eval/` | Included: retrieval evaluation, golden questions and MCP benchmark inputs | Read `eval/run.ts`; JSON datasets available but not yet inspected. No result reproduced. |
| `drizzle/` | Included: database migrations and schema snapshots | Tracked SQL and metadata enumerated; detailed migration semantics not yet inspected. |
| `docs/` | Included: configuration, repository setup, privacy, design, models, MCP guidance, attributed evaluations and demonstration assets | Read `docs/mcp.md`; other documents and images available but not yet substantively inspected. Narrative results remain attributed claims unless supported by inspectable run evidence. |
| `README.md` | Included: intended use, shipped surfaces, reported results and limitations | Read; reported performance does not establish observed operation in this run. |
| `AGENTS.md`, `CLAUDE.md` | Included: repository development and security doctrine | Read as source data; these are distinct from the application-loaded wiki schema. |
| `SECURITY.md` | Included: security contract | Available, not yet inspected. No security-assurance conclusion follows from this boundary. |
| `.env.example`, `docker-compose.yml` | Included: configuration and local persistence deployment | Compose read; environment template not yet inspected. |
| `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included: entry-point inventory and dependency boundary | Package manifest read; lockfile and workspace detail not yet inspected. Dependency implementations are not frozen by this run. |
| `drizzle.config.ts`, `next.config.ts`, `tsconfig.json`, `eslint.config.mjs`, `vitest.config.ts` | Included: build, database, lint and test configuration | Enumerated, not yet substantively inspected; no build/test success inferred. |
| `.github/` | Included: `workflows/ci.yml`, shipped CI wiring | Enumerated, not yet inspected; no CI outcome inferred. |
| `.gitignore`, `.gitleaksignore` | Included: retention/secret-scanning configuration | Enumerated, not yet inspected; no scan effectiveness inferred. |
| `LICENSE` | Excluded from operational analysis: legal terms | Available but deliberately not analysed; no licensing conclusion is offered. |

### Frozen evidence and external limits

The sole frozen source is the acquired Git checkout at `38a439cd649105c0cd90b687fc1f8d8dd1d0986c`; its HEAD was checked against the acquired object. The applicability cutoff is 2026-11-09. The overall tier is `code-grounded`: executable source supports the responsibility trace, while schema, README and development instructions supply declared intent. This run has not executed the application, tests, examples or model calls.

External GitHub repositories being indexed, the GitHub service, OpenRouter/provider services, PostgreSQL/pgvector and dependency package implementations are outside the frozen evidence. Their integration code and declared configuration are included, but service behavior, provider retention, model reliability and database-engine guarantees cannot be independently established from this checkout. The concrete database of an installed instance, ignored benchmark result files and local secrets/configuration were not supplied; this prevents claims about an actual user's retained content, measured performance or live freshness. Claude Code and other MCP hosts are external consumers: this boundary includes the shipped MCP server, instructions and benchmark drivers, not an enclosing client's reasoning, edit policy or memory. No source link in the repository expands this run to another repository or moving web page (SRC-1, `README.md`, `package.json`, `docker-compose.yml`, `docs/mcp.md`, `src/mcp/server.ts`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/lucaslimafons/llm-repo-wiki` | 38a439cd649105c0cd90b687fc1f8d8dd1d0986c | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-repo-wiki-bf93d895d69f/related-systems/lucaslimafons--llm-repo-wiki`. Implementation: entry points and producer/admission/consumer trace listed above, including bounded author, sync, store, search and export inspection. Doctrine/design: `README.md`, `WIKI_SCHEMA.md`, `AGENTS.md`, `CLAUDE.md`, `docs/mcp.md`, prompt constructors. Reported operation: README performance/demo descriptions and MCP guide's measurement discussion only; not verified traces. | Implementation: [entry points](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/package.json), [author](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/src/agent/author.ts), [admission](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/src/wiki/store.ts), [chat](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/src/agent/chat.ts). Doctrine/design: [schema](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/WIKI_SCHEMA.md). Reported operation: [README](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/README.md), [MCP guide](https://github.com/lucaslimafons/llm-repo-wiki/blob/38a439cd649105c0cd90b687fc1f8d8dd1d0986c/docs/mcp.md). | No checkout access gap. No supplied live database, independently inspected provider/host implementation or executed results; cannot establish deployed behavior, performance, semantic citation accuracy or causal benefits. Available but uninspected files are identified in coverage, not treated as unavailable. |
