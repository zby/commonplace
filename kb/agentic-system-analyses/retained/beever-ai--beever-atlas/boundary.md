---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Beever Atlas's shipped knowledge-production, maintenance and consumption system at commit 7d791af27ef4aa19644cb385c7ca24619bc4f848."
run-id: AAS-2026-10-15-beever-atlas-10a3512c094c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/Beever-AI/beever-atlas
  revision: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-beever-atlas/related-systems/Beever-AI--beever-atlas
  sha256: null
---

# Beever Atlas boundary

## Boundary and evidence

This run analyses Beever Atlas as a **memory/knowledge/context-engineering system**, not just its MCP server or extraction library. Its intended use is to turn platform conversations and imported or pushed content into retained facts, graph relationships and maintained wiki pages, then serve that knowledge to people and model clients. This is an in-scope, **whole-system** boundary covering the repository's shipped producers, persistence, maintenance, admission controls and consumers. The classification follows the source tree and the entry-point-to-consumer traces below (SRC-1: `README.md`, `Dockerfile`, `src/beever_atlas/server/app.py`, `src/beever_atlas/agents/ingestion/pipeline.py`, `src/beever_atlas/agents/tools/wiki_tools.py`).

The source declares the dual-memory and consumer responsibilities:

> Conversations from any supported platform flow into a unified ingestion pipeline that produces two complementary memory systems — a **3-tier semantic store** (channel / topic / atomic fact) for fast hybrid search, and a **graph store** that extracts entities and their relationships. Those memories fuel two consumer surfaces: the **LLM Wiki** (distilled, auto-maintained) and **QA Agents** (served through the dashboard directly, or through **MCP** into Claude Code / Cursor).
> --- `README.md`

The frozen evidence is the repository at **7d791af27ef4aa19644cb385c7ca24619bc4f848**, with applicability cutoff **2026-10-15**. The acquired checkout's HEAD was checked against that revision. No other repository, live documentation site, later revision or external runtime is evidence for this run. The overall tier is **code-grounded**: executable source was inspected, but no target code, tests, examples, deployment or model call was executed. A complete boundary establishes an inspectable target, not verified operational success.

### Shipped loop and entry-point coverage

- **Launch and composition.** The backend Docker entry point runs `beever_atlas.server.app:app` through Uvicorn. The application's lifespan creates and starts stores, initializes the LLM provider, reloads persisted configuration, starts `SyncScheduler`, and wires extraction events to maintenance services. `atlas`, `Makefile` and Compose provide shipped launch/configuration paths, not an excluded host application (SRC-1: `Dockerfile`, `atlas`, `Makefile`, `docker-compose.yml`, `src/beever_atlas/server/app.py`).
- **Production and retention.** Platform synchronization persists normalized messages in MongoDB, then selects inline processing or background extraction according to configuration. Push-source admission also writes channel messages. `BatchProcessor` constructs the ingestion workflow; the workflow joins fact/entity extraction and enrichment before persistence. The persister includes Mongo write-intent bookkeeping and vector/graph writes. These paths, their adapters, policies and recovery services are included, rather than treating the library API as the entire system (SRC-1: `src/beever_atlas/services/sync_runner.py`, `src/beever_atlas/api/sources.py`, `src/beever_atlas/services/batch_processor.py`, `src/beever_atlas/agents/ingestion/pipeline.py`, `src/beever_atlas/agents/ingestion/persister.py`).
- **Maintenance and reload.** The application wires extraction events, consolidation and wiki-maintenance services. The maintainer merges affected sections and saves the page; the wiki cache has per-page and legacy read paths. Shipped extraction prompts, QA prompts, wiki prompts, schemas, curation endpoints, lint, drift comparison, migrations and operator runbooks belong to this boundary. Documentation can describe an earlier rollout state; configuration-dependent branches must be distinguished from observed deployment settings (SRC-1: `src/beever_atlas/server/app.py`, `src/beever_atlas/services/wiki_maintainer.py`, `src/beever_atlas/wiki/cache.py`, `src/beever_atlas/wiki/prompts/topic.txt`, `src/beever_atlas/api/wiki.py`, `docs/runbooks/wiki-maintenance-soak.md`).
- **Later consumption.** QA tools reload persisted wiki content; QA agent construction attaches instructions and tools; the ask API streams answers and has history-persistence paths. MCP retrieval tools read wiki pages from the same stores. The React client fetches page content and exposes ask sessions, while the shipped bot calls the backend ask endpoint and supplies bridge routes. These are included consumers with their own state and integration responsibilities, not excluded external callers (SRC-1: `src/beever_atlas/agents/tools/wiki_tools.py`, `src/beever_atlas/agents/query/qa_agent.py`, `src/beever_atlas/api/ask.py`, `src/beever_atlas/api/mcp_server/_tools_retrieval.py`, `web/src/hooks/useWikiPage.ts`, `web/src/hooks/useAskSession.ts`, `bot/src/index.ts`).
- **Admission and evaluation.** The application mounts authenticated API routers; channel-access checks and signed push admission are shipped implementation. Tests, simulation fixtures, QA grading harnesses, wiki benchmarks and soak instructions are included evidence surfaces, but their presence does not establish that their checks passed or that the soak ran (SRC-1: `src/beever_atlas/server/app.py`, `src/beever_atlas/infra/channel_access.py`, `src/beever_atlas/api/sources.py`, `tests/integration/test_sim_memory_then_wiki.py`, `scripts/qa_test_harness.py`, `scripts/wiki_bench.py`, `docs/runbooks/wiki-maintenance-soak.md`).

Two small implementation passages anchor persistence followed by later consumption, rather than classification from marketing alone (SRC-1):

> await self._page_store.save_page(page)
> --- `src/beever_atlas/services/wiki_maintainer.py`

> cache = WikiCache(settings.mongodb_uri)
> page = await cache.get_page(channel_id, page_type)
> --- `src/beever_atlas/agents/tools/wiki_tools.py`

The standalone MCP executable is included but is not mistaken for the full deployed loop. Its own contract explicitly distinguishes catalog introspection from backed tool execution (SRC-1):

> Tool calls that require backing stores return structured errors in this mode;
> point clients at a full deployment's ``/mcp`` mount for real data.
> --- `src/beever_atlas/api/mcp_server/__main__.py`

### Top-level coverage

Every top-level tracked file or directory is classified below. **Included** means inside the functional/evidence boundary, not that every line was inspected. Named material paths show the initial tracing coverage. An included path listed as not yet inspected remains available to later jobs at the same pin; it is not an access gap. No material shipped loop component was inaccessible during boundary selection.

| Top-level tracked path(s) | Classification and material scope | Initial inspection and limits; conclusion prevented by exclusion |
|---|---|---|
| `src/` | Included: `beever_atlas/server/app.py`; `api/` including ask, wiki, sources, sync and MCP; `capabilities/`; `adapters/`; `agents/` including ingestion, prompts, query, tools and runner; `services/` including scheduler, extraction, consolidation, reconciliation and wiki maintenance; `stores/`, `models/`, `infra/`, `llm/`; `wiki/` including builder/compiler, prompts, schemas, cache/page/version stores, modules and structure. | Entry-point wiring, sync/worker/batch paths, ingestion graph, persister, maintainer save, cache reload, QA and MCP consumers, source admission and channel-access code inspected or searched. Remaining implementation is included, not yet inspected in full. No exclusion. SRC-1. |
| `bot/` | Included: `src/index.ts`, `src/bridge.ts`, platform gateway, session, SSE and rendering helpers; package/build configuration and tests. | Inspected backend ask and bridge routing in `src/index.ts`; tree inspected for other modules and tests. Full platform adapter behavior not yet inspected. No exclusion. SRC-1. |
| `web/` | Included: app/routes/pages, ask and wiki hooks/components, API client, settings and admin surfaces, package/build configuration and tests. Tracked Python files under `web/src/beever_atlas/wiki/` also remain included for investigation of their role, not presumed to be the backend entry point. | Inspected `src/hooks/useWikiPage.ts` and the beginning of `src/hooks/useAskSession.ts`; tree inspected for UI consumption, curation, maintenance and tests. Other paths not yet inspected in full. No exclusion. SRC-1. |
| `atlas`, `Dockerfile`, `Makefile` | Included launch/setup/build drivers. | Searched backend launch and Compose usage; broader installer behavior not yet inspected. No exclusion. SRC-1. |
| `docker-compose.yml`, `docker-compose.auth.yml`, `docker-compose.nebula.yml` | Included deployment wiring and backend alternatives. | Main stack service/build/image configuration searched; overlays not yet inspected in detail. No exclusion. SRC-1. |
| `deploy/` | Included: `launchd/ai.beever.tunnel.plist.template`, host startup integration. | Tree inspected; template not yet inspected. No exclusion. SRC-1. |
| `pyproject.toml`, `uv.lock`, `.env.example` | Included dependencies, Python entry point and operator configuration. | Project metadata and `beever-atlas-mcp` entry point searched; lockfile and full environment defaults not yet inspected. No exclusion. SRC-1. |
| `.mcp.json`, `server.json`, `glama.json`, `llms-install.md` | Included MCP discovery/launch and installation contracts. | Tree inspected; content not yet inspected. No exclusion. SRC-1. |
| `README.md`, `CHANGELOG.md`, `HANDOFF.md` | Included first-party intent, release and handoff assertions. | README architecture and handoff excerpts inspected. Historical status statements are attributed documentation, not substitutes for current code. Changelog not yet inspected. No exclusion. SRC-1. |
| `docs/` | Included: `architecture/oss-pipeline.md`, `pipeline-architecture.md`, `content/` API/concept/integration guides, `integrations/`, `mcp-server*`, `guides/`, `runbooks/` maintenance, migration and rollout instructions. | Architecture and maintenance-soak excerpts inspected; tree inspected for other instructional and consumer contracts. Linked live sites are not frozen evidence. Other documentation not yet inspected in full. No exclusion of tracked docs. SRC-1. |
| `runbooks/` | Included: channel reset, entity deduplication and sync metrics operations. | Tree inspected; content not yet inspected. No exclusion. SRC-1. |
| `scripts/` | Included: migrations/backfills, ingestion and live/mock diagnostics, `qa_test_harness.py`, `wiki_bench.py`, `smoke/`, setup and recovery tooling. | QA harness beginning and wiki benchmark function structure inspected; migration dependency traced from app startup. Other scripts not yet inspected in full. No execution or measured outcomes inferred. SRC-1. |
| `tests/` | Included: agents, API, capabilities, infra, integration simulation, services, stores, wiki, fixtures and root-level tests. | Tree inspected; memory-then-wiki simulation test excerpt inspected. Assertions and fixture data can support design coverage, not an observed passing run. Most tests not yet inspected. SRC-1. |
| `demo/` | Included: seed scripts, corpus, precomputed Mongo/graph/vector/wiki fixtures and Compose overrides. | Tree inspected and README demo contract read; seeds/fixtures not yet inspected in detail. No observed demo operation inferred. SRC-1. |
| `.github/`, `.pre-commit-config.yaml` | Included CI, nightly/smoke/demo regeneration, audit and release/check configuration. | Tree inspected; workflow and hook content not yet inspected. No passing CI or release evidence inferred. SRC-1. |
| `.dockerignore`, `.gitattributes`, `.gitignore` | Included packaging and tracked-file conventions. | Tree inspected; content not yet inspected. No exclusion. SRC-1. |
| `assets/` | Excluded presentation media: architecture/banner/logo images, screenshots and demonstration GIFs. | Deliberate exclusion, not unavailable. Prevents conclusions about visual demonstrations, depicted run success or UI appearance based on those assets. Text and code remain the evidence basis. SRC-1. |
| `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, `NOTICE`, `SECURITY.md`, `TRADEMARK.md` | Excluded governance, contribution, legal and disclosure-policy documents. | Deliberate exclusion, not unavailable. Prevents assessment of contribution governance, legal rights, branding rules or disclosure policy; does not exclude executable access controls or runtime safety mechanisms. SRC-1. |

### External dependencies and evidence limits

Model/embedding providers, Google ADK, FastMCP, storage engines, platform services and external MCP clients are dependencies, not additional frozen sources. Atlas's configuration, calls, adapters and recovery handling for them are included. Their internal implementations and deployed behavior are not. The stack declares Weaviate, Neo4j, MongoDB and Redis, with additional storage/graph alternatives visible in the tree; installed dependency behavior is not established by a dependency declaration (SRC-1: `pyproject.toml`, `docker-compose.yml`, `docker-compose.nebula.yml`, `src/beever_atlas/stores/__init__.py`).

External Claude Code, Cursor, OpenClaw, Hermes and platform hosts are not part of the target. The shipped Atlas integration endpoints and documentation are included; an external caller's scheduling, memory policy, tool-choice loop or later use of returned content is not attributed to Atlas (SRC-1: `README.md`, `docs/architecture/oss-pipeline.md`, `src/beever_atlas/api/mcp_server/__main__.py`). This exclusion prevents conclusions about end-to-end behavior of those external agents.

There is no supplied execution trace or causal experiment. Source-native screenshots, demo fixtures, status assertions, tests and soak recipes do not establish live reliability, latency, cost, knowledge accuracy, safe authorization under attack or improved answers. No live service, credentials, production data or soak results were supplied. These evidence gaps prevent operational and causal conclusions, not source-level analysis of the full shipped loop. Available but uninspected files are explicitly different from these unavailable observations.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Beever-AI/beever-atlas` | 7d791af27ef4aa19644cb385c7ca24619bc4f848 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-beever-atlas/related-systems/Beever-AI--beever-atlas`. Implementation: tracked tree; launch searches in `Dockerfile`, `atlas`, `Makefile`, `pyproject.toml`, `docker-compose.yml`; excerpts/searches in `src/beever_atlas/server/app.py`, `services/sync_runner.py`, `services/extraction_worker.py`, `services/batch_processor.py`, `services/wiki_maintainer.py`, `agents/ingestion/pipeline.py`, `agents/ingestion/persister.py`, `agents/ingestion/fact_extractor.py`, `agents/runner.py`, `agents/query/qa_agent.py`, `agents/tools/wiki_tools.py`, `api/ask.py`, `api/wiki.py`, `api/sources.py`, `api/mcp_server/__init__.py`, `api/mcp_server/__main__.py`, `api/mcp_server/_tools_retrieval.py`, `infra/channel_access.py`, `wiki/cache.py`, `wiki/page_store.py`; consumers in `bot/src/index.ts`, `web/src/hooks/useWikiPage.ts`, `web/src/hooks/useAskSession.ts`; evaluation source in `tests/integration/test_sim_memory_then_wiki.py`, `scripts/qa_test_harness.py`, `scripts/wiki_bench.py`. Paths abbreviated after `src/beever_atlas/` in this scope cell share that prefix. Doctrine/design: `README.md`, `docs/architecture/oss-pipeline.md`, `docs/runbooks/wiki-maintenance-soak.md`, `src/beever_atlas/wiki/prompts/topic.txt` and implementation docstrings. Reported operation: historical status and test assertions in `HANDOFF.md`, treated only as attributed reports. | Implementation: [backend entry](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/src/beever_atlas/server/app.py), [ingestion graph](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/src/beever_atlas/agents/ingestion/pipeline.py), [maintenance](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/src/beever_atlas/services/wiki_maintainer.py), [wiki consumption](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/src/beever_atlas/agents/tools/wiki_tools.py). Doctrine/design: [README](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/README.md), [soak contract](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/docs/runbooks/wiki-maintenance-soak.md). Reported operation: [historical handoff](https://github.com/Beever-AI/beever-atlas/blob/7d791af27ef4aa19644cb385c7ca24619bc4f848/HANDOFF.md). | No repository access gap identified. Inspection is selective, as the coverage table states. Dependency internals, external-agent operation, live deployments and unsupplied run/soak results are unavailable evidence: no observed-run or causal-experiment layer, no verified performance/quality/security outcome. Historical documentation can lag executable source. |
