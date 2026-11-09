---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Kherad's shipped knowledge-base application and model-driven authoring, compilation and retrieval paths at commit 2a8d6992b87a33760688e1f956653c21a6292294."
run-id: AAS-2026-11-08-kherad-ac3e4da97ac6-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/mohammadmaso/kherad
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/kherad-aa095369bdeb/related-systems/mohammadmaso--kherad
  revision: "2a8d6992b87a33760688e1f956653c21a6292294"
  sha256: null
---

# Kherad boundary

## Boundary and evidence

Kherad is in scope as a self-hosted knowledge system with model-driven drafting, editing, knowledge compilation and question answering. Its intended users are organizational authors, reviewers and readers, rather than developers embedding a standalone retrieval library. The target is the shipped application, including its human interfaces and persistence services; the Next.js client and Fastify server are not excluded enclosing hosts. The boundary is whole-system because it includes the paths that produce source material, compile it, admit changes, preserve state and consume that state later. This is a scope declaration supported by entry-point tracing, not a claim that every implementation file has already been exhaustively reviewed. [SRC-1] `README.md`, `apps/api/src/index.ts`, `apps/api/src/routes/indexer.ts`, `apps/api/src/agents/indexer/run.ts`, `apps/web/src/components/chat/bundle-chat.tsx`.

The author's stated purpose is:

> A Notion-like wiki for non-technical teams, backed by real git commits and a merge-request review workflow — plus AI agents that write the first draft for you.
> --- `README.md`

The API entry point creates the database and Git engine and registers page, ingest, review, search, compilation, chat, specialist-session, skill and MCP routes. The compilation route invokes the indexer, whose model receives source/delta context and tools, then stages compiled documents and mirrored sources on an agent branch and opens or updates a merge request. The review route checks review permission and invokes a subtree-scoped squash merge, followed by search synchronization. These shipped responsibilities are included; neither the review gate nor state persistence is attributed to an unspecified external host. [SRC-1] `apps/api/src/index.ts`, `apps/api/src/routes/indexer.ts`, `apps/api/src/agents/indexer/run.ts`, `apps/api/src/routes/merge-requests.ts`.

Model dependence is executable, not merely a documentation promise:

> const agent = new Agent({
>     id: "okf-indexer",
>     name: "OKF Indexer",
>     instructions: indexerInstructions(bundle),
>     model: buildModel(settings, "indexer"),
>     tools: createIndexerTools({ db, git, bundle, pending }),
>   });
> --- `apps/api/src/agents/indexer/run.ts`

The compilation prompt supplies maintenance instructions for incremental updates, source references, concept files, a root directory and an update log. Specialist sessions additionally load stored skills, page mentions, quotations and optional MCP tools into model instructions/tools. Chat constructs a model agent with tools that read compiled content from the bundle's default branch and search its indexed state. The web chat reloads stored thread messages and resubmits subsequent turns. Wiki rendering separately reloads Git content. These are retained-content consumers inside the target. [SRC-1] `apps/api/src/agents/indexer/prompt.ts`, `apps/api/src/agents/skills.ts`, `apps/api/src/routes/agent-sessions.ts`, `apps/api/src/routes/chat.ts`, `apps/api/src/agents/chat/tools.ts`, `apps/api/src/agents/search-tools.ts`, `apps/web/src/components/chat/bundle-chat.tsx`, `apps/web/src/lib/wiki-render.ts`.

For example, the chat read tool selects persisted content rather than receiving an externally prepared document body:

> const bytes = await git.getFileAtRef(bundle.defaultBranch, `${okfPrefix}/${validPath}`);
> --- `apps/api/src/agents/chat/tools.ts`

Human review is one admission path, not an assumption that every default-branch change is reviewed. The shipped remote synchronization routes also belong to the boundary; the raw-bundle remote route explicitly describes direct default-branch replacement and invokes reconciliation. Its presence prevents treating the README's review language as a universal enforcement claim. [SRC-1] `apps/api/src/routes/bundle-remote.ts`, `apps/api/src/routes/merge-requests.ts`, `packages/db/src/schema.ts`.

### Tracked-root coverage

The table accounts for every top-level tracked file or directory at the frozen commit. “Included” means available to the analysis within SRC-1. Initial inspection is bounded: paths named as not yet inspected are not access gaps or silent exclusions. They remain in scope for later implementation tracing.

| Top-level tracked paths | Treatment and material responsibilities | Initial inspection and limits |
|---|---|---|
| `apps/` | Included: `api/src/index.ts`; `api/src/routes/` for authoring, ingestion, review, remote sync, search, sessions and administration; `api/src/agents/` for prompts, indexer maintenance, retrieval, drafting/editing, skills and MCP; `api/src/lib/` for persistence/ingest helpers; `web/src/app/`, `web/src/components/`, `web/src/lib/` for user triggers, editing, review, retained chat and wiki reload/rendering; `ingest/main.py` for document conversion. Docker/build configuration is included as deployment wiring. | Inspected API entry point and package manifest, indexer run/prompt, chat prompt/tools and route ranges, specialist-session assembly/persistence, skill loading, search tools, page rename persistence, review approval, remote-sync search hits, compile trigger, web chat transport/history reload, wiki render ranges and ingest conversion. Other route/helper/UI bodies, including complete specialist tools, ingest orchestration, document-remote and editor flows, are not yet inspected in detail; no absence claim about them follows. [SRC-1] `apps/api/src/index.ts`, `apps/api/src/routes/agent-sessions.ts`, `apps/web/src/components/chat/bundle-chat.tsx`, `apps/ingest/main.py`. |
| `packages/` | Included: `core/src/git/` for commits, branches, merges, versions, source paths and remote operations; `core/src/search/` for indexing, chunking, embeddings and reconciliation; `core/src/permissions/`, `auth/`, `markdown/` for gates and rendering; `db/src/` and `db/drizzle/` for durable schema, seed and migrations; `ui/` for shared UI. The `core` test files and Vitest setup are included as evaluative source. | Inspected core manifest/exports, schema search hits and a search-refresh test range. Git/search/permission implementations are initially traced through API callers, not exhaustively inspected internally. Migration bodies, seed, most tests and shared UI internals are not yet inspected; their availability is not an access gap. The inspected test is a test specification, not an observed pass. [SRC-1] `packages/core/package.json`, `packages/db/src/schema.ts`, `packages/core/src/search/refresh.test.ts`. |
| `README.md` | Included: intended use, architecture and declared workflows. | Read completely; doctrine/design, not proof that every stated guarantee holds. [SRC-1] `README.md`. |
| `PRD.md`, `CLAUDE.md` | Included: shipped specification and developer/maintenance instructions. | Inventory established; contents not yet inspected. They cannot establish implemented behavior without code tracing. [SRC-1] `PRD.md`, `CLAUDE.md`. |
| `docker-compose.yml` | Included: API, web, conversion and Postgres service/storage boundaries. | Read completely; configuration evidence, not an observed deployment. [SRC-1] `docker-compose.yml`. |
| `package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml`, `turbo.json`, `tsconfig.base.json`, `eslint.config.js` | Included: workspace entry points, dependency resolution and build/test/lint wiring. | Root manifest read; other configuration/lock bodies not yet inspected. No dependency-internal behavior is inferred from their presence. [SRC-1] `package.json`. |
| `.dockerignore`, `.gitignore`, `.prettierignore`, `.prettierrc.json` | Included as packaging/development context. | Inventory only; not inspected internally. No packaging completeness or formatting enforcement conclusion is drawn. [SRC-1] `.dockerignore`, `.gitignore`, `.prettierignore`, `.prettierrc.json`. |
| `docs/` | Excluded from mechanism evidence: `brand/logo.svg` and `screenshots/*.jpg` are branding and illustrative UI assets. | Tree inventoried; assets not opened. This prevents independent visual verification of the advertised screens, not source-level tracing of their shipped UI implementations. [SRC-1] `README.md`. |
| `LICENSE` | Excluded from operational analysis: licensing text. | Not inspected; no legal interpretation is supplied. [SRC-1] `LICENSE`. |

### Frozen evidence and external limits

The sole frozen source is the acquired Git repository at full commit `2a8d6992b87a33760688e1f956653c21a6292294`; checkout HEAD was checked against that pin. The analysis cutoff is 2026-11-08, the supplied run date. Applicability is limited to this revision, not later upstream changes. No extra repository, web page, deployed database, user knowledge corpus or execution trace is registered.

The overall tier is code-grounded. Source inspection supplies implementation evidence; README and prompt text supply doctrine/design. Tests supply inspectable assertions, not observed run results. No target code, tests or examples were executed, so this boundary supports neither measured answer quality nor demonstrated recovery, throughput, security or operational reliability.

External dependencies include Postgres/pgvector, the Git storage implementation, Fastify/Next.js, Mastra and AI SDK adapters, Docling, configured model/embedding/OCR/transcription services, remote Git servers and session-selected MCP services. Dependency declarations and call sites are included; dependency implementation repositories, actual credentials/configurations, remote tool behavior and provider outputs are not frozen. This prevents attributing their internal guarantees or real-world availability to Kherad. [SRC-1] `docker-compose.yml`, `apps/api/package.json`, `packages/core/package.json`, `apps/ingest/main.py`, `apps/api/src/routes/agent-sessions.ts`. Available but not yet inspected source files are distinguished above from these external evidence limits.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/mohammadmaso/kherad` | 2a8d6992b87a33760688e1f956653c21a6292294 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/kherad-aa095369bdeb/related-systems/mohammadmaso--kherad`. Implementation: full tracked-tree inventory, manifests and API registration; bounded traces of compilation, admission, retrieval, specialist context assembly, page persistence, remote-sync wiring, web history reload/wiki rendering, conversion and search-refresh test assertions. Doctrine/design: complete README and indexer/chat prompts. Coverage table records detail not yet inspected. | Implementation: [API entry](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/api/src/index.ts), [indexer](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/api/src/agents/indexer/run.ts), [admission](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/api/src/routes/merge-requests.ts), [chat tools](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/api/src/agents/chat/tools.ts), [web reload](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/web/src/components/chat/bundle-chat.tsx). Doctrine/design: [README](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/README.md), [maintenance prompt](https://github.com/mohammadmaso/kherad/blob/2a8d6992b87a33760688e1f956653c21a6292294/apps/api/src/agents/indexer/prompt.ts). | No material repository access gap found. No observed deployment, model outputs or experimental comparison supplied: no performance, quality or causal-efficacy conclusion. External dependencies and remote service contents are not frozen; their internals and operational guarantees cannot be established. |
