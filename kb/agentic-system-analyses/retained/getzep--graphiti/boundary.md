---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Graphiti's shipped graph-memory library, services, instructions, consumers and evaluators at commit 964bb11d1e7020e3cc67fab244268b0736b6c219."
run-id: AAS-2026-10-12-graphiti-1d535ca565a4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/getzep/graphiti
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/graphiti-workflow-1d535ca565a4/related-systems/getzep--graphiti
  revision: "964bb11d1e7020e3cc67fab244268b0736b6c219"
  sha256: null
---

# Graphiti boundary

## Boundary and evidence

This run analyses Graphiti as a shipped graph-memory system, not only its Python API. Its intended use is to establish how information enters retained graph state, how model-dependent processing updates that state, and how later retrieval supplies application or agent context. The target includes the core library, database adapters, REST and MCP services, shipped agent-memory instructions, example consumers and evaluation code. It does not treat Graphiti as a general enclosing agent runtime. SRC-1: `graphiti_core/graphiti.py`, `server/graph_service/routers/ingest.py`, `server/graph_service/routers/retrieve.py`, `mcp_server/src/graphiti_mcp_server.py`, `examples/langgraph-agent/agent.ipynb`.

The target class is **memory/knowledge/context-engineering system**. Entity extraction selects prompts by episode source and requests a structured response from the configured language-model path. Ingestion retrieves previous episodes, resolves entities and facts, and saves episode data. This establishes model-dependent memory processing rather than a database wrapper alone. SRC-1: `graphiti_core/utils/maintenance/node_operations.py`, `graphiti_core/graphiti.py`.

> return await generate_prompt_response(
>     llm_client,
>     prompt_name,
>     legacy_prompt,
>     context,
>     clients=clients,
>     response_model=ExtractedEntities,
>     group_id=episode.group_id,
> )
> --- `graphiti_core/utils/maintenance/node_operations.py`

The **whole-system** boundary includes material shipped paths for production, maintenance, admission and consumption of retained state. Initial tracing followed the core ingestion path through persistence and retrieval; the REST routes through their request-scoped client; the MCP entry point through its tool declarations and queue worker; and the LangGraph notebook through retrieval, prompt assembly and asynchronous ingestion of conversation content. The notebook is part of the target's shipped usage, not an excluded application merely because it calls the library. Its LangGraph scheduler and model SDK are external dependencies; the notebook's glue and memory-use decisions remain included. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/driver/neo4j/operations/episode_node_ops.py`, `server/graph_service/main.py`, `server/graph_service/zep_graphiti.py`, `mcp_server/main.py`, `mcp_server/src/services/queue_service.py`, `examples/langgraph-agent/agent.ipynb`.

The boundary also includes maintenance responsibilities: community rebuilds, saga summaries, triplet insertion, episode removal, graph clearing and group-scoped service operations. These are shipped responsibilities whether called by a maintainer or an assistant. Shipped instructions explicitly tell a consuming assistant to search before work, retain new information and apply retrieved preferences and procedures. These instructions establish declared use, not proof that an external assistant follows them. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/maintenance/graph_data_operations.py`, `server/graph_service/routers/ingest.py`, `mcp_server/src/graphiti_mcp_server.py`, `mcp_server/docs/cursor_rules.md`.

> - **Always search first:** Use the `search_nodes` tool to look for relevant preferences and procedures before beginning work.
> --- `mcp_server/docs/cursor_rules.md`

> - **Capture requirements and preferences immediately:** When a user expresses a requirement or preference, use `add_memory` to store it right away.
> --- `mcp_server/docs/cursor_rules.md`

Evaluation is included as executable design evidence. The shipped evaluation CLI invokes baseline construction and candidate evaluation; its implementation ingests multi-session messages, serializes graph-building results, reloads baseline results and requests model judgments. This inclusion permits analysis of the measurement procedure, not a claim that the evaluator was run or that its scores establish effectiveness. SRC-1: `tests/evals/eval_cli.py`, `tests/evals/eval_e2e_graph_building.py`.

### Frozen evidence and limits

The sole source is the acquired repository at full commit **964bb11d1e7020e3cc67fab244268b0736b6c219**. The checkout HEAD was verified against that pin. The applicability cutoff is **2026-10-12**, the supplied run date; it does not imply evidence about changes after the commit. Overall evidence is **code-grounded**, with README, specifications and tool instructions supplying doctrine/design. No target, test, example, model call or database service was executed.

External graph engines, language-model and embedding providers, reranking dependencies, MCP client hosts and LangGraph implementation are not frozen here. Their interfaces and Graphiti-side adapters are included; their internals and deployed behavior are not. This prevents conclusions about provider reliability, database-engine guarantees or host enforcement beyond what Graphiti's own code requests. Dependencies and supported integrations are declared in SRC-1: `pyproject.toml`, `README.md`, `docker-compose.yml`.

Proprietary Zep services, its Context Graph Engine, live hosted documentation, the linked paper, release binaries and actual production deployments are outside this source set. This prevents transferring claims about Zep's managed governance, latency or scale to this Graphiti revision. The source itself distinguishes the products. SRC-1: `README.md`.

> Graphiti is the open-source framework for building temporal knowledge graphs at the core of
> [Zep's](https://www.getzep.com) context infrastructure. Zep manages context graphs at scale, providing
> governed, low-latency context retrieval and assembly for production deployments.
> --- `README.md`

Available but not yet closely inspected source files are not access gaps. The register covers the entire repository at the commit; initial reads below are not an allowlist. Backend-specific details, all prompt variants, test assertions and example compatibility require further inspection before claims about them. Historical notebook outputs were encountered during source discovery but are not used as evidence of operation of this pinned revision; their originating code/model/environment pins have not been established. No controlled experiment or pinned deployment trace is established by this boundary.

### Top-level coverage

Every top-level tracked file or directory is classified below. Included directories name material paths and responsibilities; inclusion does not mean every file has already been read. The table distinguishes initial tracing from available material awaiting deeper inspection. Exclusions are deliberate functional exclusions, not unavailable repository evidence. All path entries refer to SRC-1.

| Top-level tracked path | Classification and role | Initial inspection / limit or conclusion prevented |
|---|---|---|
| `graphiti_core/` | Included: `graphiti.py`; `nodes.py`, `edges.py`, `models/`, `namespaces/`; `driver/` and backend `operations/`; `search/`; `utils/maintenance/`, `utils/bulk_utils.py`; `prompts/`, `llm_client/`, `embedder/`, `cross_encoder/`; tracing, telemetry and migrations. These produce, persist, reload, maintain and retrieve retained content. | Traced `graphiti.py` ingestion, persistence handoff, community rebuild and search; extraction call in `utils/maintenance/node_operations.py`; episode persistence in `driver/neo4j/operations/episode_node_ops.py`; clear/retrieve in `utils/maintenance/graph_data_operations.py`; message extraction prompt in `prompts/extract_nodes.py`. Other variants are available, not yet deeply inspected; no cross-backend parity claim. |
| `mcp_server/` | Included: `main.py`, `src/graphiti_mcp_server.py`, `src/services/queue_service.py`, factories, config schema, type models, response formatting, `config/`, `docs/cursor_rules.md`, Docker deployment and `tests/`. Includes assistant instructions, admission queues, retrieval and maintenance tools. | Read entry wrapper, tool/instruction surface and queue implementation; searched tool-to-core calls. Read memory-use instructions. Configuration, transport and test details remain available for later inspection; no claim of actual MCP client compliance or transport reliability. |
| `server/` | Included: `graph_service/main.py`, `zep_graphiti.py`, `routers/ingest.py`, `routers/retrieve.py`, DTOs, config, manifests and tests. Includes queued ingestion, direct writes/deletes, retrieval and memory response assembly. | Read main, both routers and client subclass/lifecycle. DTO, settings and deployment-test details are available for deeper inspection. No observed REST service operation. |
| `examples/` | Included: `langgraph-agent/agent.ipynb`; ecommerce runner and notebook; quickstart Neo4j/FalkorDB/Neptune scripts; podcast and wizard-of-oz ingestion; GLiNER2, Azure and OpenTelemetry examples; parsers and bundled data. | Read notebook code cells for both notebooks; searched ecommerce, podcast and wizard-of-oz ingestion/search callers. LangGraph example both consumes facts in a system message and persists conversation episodes. Other example variants are available, not yet fully inspected. Example glue is included; framework internals and historical notebook outputs do not prove current behavior. |
| `tests/` | Included: core, driver, maintenance, search, prompts, client and integration tests; `evals/eval_cli.py`, `evals/eval_e2e_graph_building.py`, evaluator utilities/data and `e2e_prompt_library_ingest.py`. | Read evaluation entry point and graph-building/judging implementation; inventoried suites. Other assertions/data are available for inspection. No tests or evaluator were run; no passing-suite or measured-quality conclusion. |
| `spec/` | Included: `llm-runtime.md`, `configurable-prompts.md`, `configurable-prompts-tests.yaml`, `driver-operations-redesign.md`; declared contracts for routing, prompt customization and persistence architecture. | Read routing specification; other specifications remain available. Specs support intent, not implementation merely by existing. |
| `README.md` | Included: system purpose, setup, supported integrations, product distinction, memory component definitions and prompt configuration. | Read; performance statements remain declared claims, not measurements. |
| `pyproject.toml` | Included: package identity, dependencies, optional backends/providers and development configuration. | Read; dependency declarations do not freeze installed dependencies. |
| `uv.lock` | Included: root dependency-resolution artifact. | Available, not initially inspected in detail; no lockfile reproducibility claim. |
| `Dockerfile` | Included: shipped REST deployment recipe and entry point. | Read. Recipe installs graphiti-core from package distribution; no built image is frozen or equated to the checkout. |
| `docker-compose.yml` | Included: REST and database service wiring and database volumes. | Read; no deployed durability or health guarantee inferred. |
| `docker-compose.test.yml` | Included: integration-test service setup. | Available, not yet inspected; no test-environment equivalence claim. |
| `OTEL_TRACING.md` | Included: instrumentation doctrine. | Available, not yet inspected; no deployed observability claim. |
| `conftest.py` | Included: shared test setup. | Available, not yet inspected; no fixture/coverage guarantee. |
| `pytest.ini` | Included: test selection/configuration. | Available, not yet inspected; no executed coverage claim. |
| `py.typed` | Included: package typing marker. | Inventoried; not memory state or runtime evidence. |
| `.env.example` | Included: example operator configuration. | Available, not yet inspected; no completeness or secret-handling guarantee. |
| `Makefile` | Included: build/test/development entry points. | Available; development instructions inspected in `AGENTS.md`, commands not executed. |
| `AGENTS.md` | Included: shipped repository-maintainer instructions, distinct from end-user memory instructions. | Read as source evidence only. It governs development, not automatic assistant-memory consumption. |
| `CLAUDE.md` | Included: additional maintainer instruction surface. | Available, not initially read; no claim of agreement with other instruction surfaces. |
| `.github/` | Excluded from functional graph-memory loop: workflows, intake scripts/templates, issue policies, copilot instructions, release/security automation and setup actions. | Tree inventoried. Exclusion prevents conclusions about repository moderation agents, CI success and release supply-chain enforcement; these do not produce or consume application graph memory. |
| `.gitignore` | Excluded: repository hygiene. | No conclusion about ignored runtime artifacts or capture completeness. |
| `depot.json` | Excluded: build-infrastructure configuration. | No conclusion about hosted build behavior. |
| `images/` | Excluded: illustrations and screenshots. | No visual demo or screenshot treated as execution evidence. |
| `signatures/` | Excluded: `version1/cla.json`, contributor-agreement records. | No contributor-attestation conclusion; not graph memory schemas. |
| `CODE_OF_CONDUCT.md` | Excluded: community policy. | No community-governance conclusion. |
| `CONTRIBUTING.md` | Excluded: contribution workflow beyond included runtime/specification evidence. | No claim about enforcement of contribution or driver-development process. |
| `LICENSE` | Excluded: legal licensing text. | No legal interpretation. |
| `SECURITY.md` | Excluded: security-reporting policy. | No vulnerability-response or deployed-security guarantee. |
| `Zep-CLA.md` | Excluded: contributor legal agreement. | No legal or contributor-governance interpretation. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/getzep/graphiti` | 964bb11d1e7020e3cc67fab244268b0736b6c219 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/graphiti-workflow-1d535ca565a4/related-systems/getzep--graphiti`. Implementation: initial tracing of `graphiti_core/graphiti.py`, `graphiti_core/utils/maintenance/node_operations.py`, `graphiti_core/utils/maintenance/graph_data_operations.py`, `graphiti_core/driver/neo4j/operations/episode_node_ops.py`; REST main/client/routers; MCP entry/tools/queue; notebook code cells and evaluator implementation. Doctrine/design: `README.md`, `pyproject.toml`, `AGENTS.md`, `spec/llm-runtime.md`, `mcp_server/docs/cursor_rules.md`, built-in MCP instructions and extraction prompt; root Dockerfile/compose wiring. | Implementation: [core loop](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/graphiti_core/graphiti.py), [MCP tools](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/mcp_server/src/graphiti_mcp_server.py), [shipped agent consumer](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/examples/langgraph-agent/agent.ipynb), [evaluator](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/tests/evals/eval_e2e_graph_building.py). Doctrine/design: [README](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/README.md), [memory-use instructions](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/mcp_server/docs/cursor_rules.md), [model routing contract](https://github.com/getzep/graphiti/blob/964bb11d1e7020e3cc67fab244268b0736b6c219/spec/llm-runtime.md). | No repository access gap established. External provider/backend/host internals and proprietary Zep are outside the frozen source. Implementation reads support requested behavior, not observed deployment, effectiveness, latency or causal attribution. Doctrine supports declared use/contracts, not compliance. Historical notebook outputs lack established originating pins and are not registered as observed-run evidence. |
