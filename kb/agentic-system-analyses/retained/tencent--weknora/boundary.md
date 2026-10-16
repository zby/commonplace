---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "WeKnora's shipped knowledge, RAG, agent and wiki system at commit 234aa948db29c10f5ed4b7939285c7b3711c5d4c."
run-id: AAS-2026-10-15-weknora-7adf8a01c381-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "234aa948db29c10f5ed4b7939285c7b3711c5d4c"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/Tencent/WeKnora
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/weknora-7adf8a01c381/related-systems/Tencent--WeKnora
  revision: 234aa948db29c10f5ed4b7939285c7b3711c5d4c
  sha256: null
---

# WeKnora boundary

## Boundary and evidence

This run examines WeKnora as the shipped knowledge system, including its own application callers, not merely its retrieval API. Its intended use is document understanding, retrieval and model-assisted work over knowledge bases. The primary target class is **memory/knowledge/context-engineering system**; the shipped ReAct engine is an included runtime responsibility rather than an excluded host. The boundary kind is **whole-system**. SRC-1, `README.md`, describes the three consumption modes:

> Use RAG to look things up, the agent for multi-step tasks, and the wiki to organize knowledge. All three work on the same knowledge bases.
> --- `README.md`

The classification is also implementation-grounded. The server builds its own dependency container and HTTP application (SRC-1, `cmd/server/main.go`). Document upload stores the source file, creates a knowledge record, and enqueues document processing (SRC-1, `internal/application/service/knowledge_create.go`). Processing distinguishes retrieval admission from completion of enrichment (SRC-1, `internal/application/service/knowledge_process.go`):

> knowledge.EnableStatus = "enabled"
> --- `internal/application/service/knowledge_process.go`

The scope includes the state-producing and state-consuming sides: document and URL ingestion, connector synchronization, parsing and chunking, indexes, enrichment, wiki ingestion and revision, long-term memory, stored conversations, RAG, model/tool execution, permission checks, user interfaces, SDKs, integrations, maintenance queues and evaluators. Source-native names and storage boundaries should be traced by later jobs rather than treating all retained state as one memory store.

In particular, the enclosing application belongs to this target. The agent caller supplies stored history, recalls long-term memory, installs a checkpoint sink and invokes the engine (SRC-1, `internal/application/service/session_agent_qa.go`). It is not legitimate to infer the absence of cross-turn persistence from inspecting the inner engine alone:

> // AgentEngine is the core engine for running ReAct agents.
> //
> // History persistence note: the engine is stateless across turns. Conversation
> // history is rebuilt from the DB once per turn by the caller
> // (see service.LoadAgentHistory) and passed into Execute as llmContext. The
> // engine therefore does not maintain its own cache, system-prompt store, or
> // cross-turn buffer.
> --- `internal/agent/engine.go`

The reload path is part of the inspected boundary, not an assumed external consumer (SRC-1, `internal/application/service/agent_history.go`):

> checkpoint := loadContextCheckpoint(ctx, messageRepo, sessionID)
> --- `internal/application/service/agent_history.go`

Memory also has application-owned write and read paths. The turn handler records explicit statements and schedules extraction; a background worker issues a model call; subsequent agent turns recall retained content into the prompt (SRC-1, `internal/handler/session/qa.go`, `internal/application/service/memory/extract.go`, `internal/application/service/session_agent_qa.go`). Minimum anchors for the write-to-later-consumption boundary are:

> h.memoryService.ScheduleExtraction(ctx, assistantMessage.SessionID, assistantMessage.ID, assistantMessage.ModelID)
> --- `internal/handler/session/qa.go`

> response, err := chatModel.Chat(ctx, []chat.Message{
> --- `internal/application/service/memory/extract.go`

> engine.SetMemoryPrompt(recall.Prompt)
> --- `internal/application/service/session_agent_qa.go`

Wiki generation and queue recovery are included maintenance responsibilities, not external authoring. The wiki worker calls a chat model; pending wiki operations have a recovery path in the container (SRC-1, `internal/application/service/wiki_ingest.go`, `internal/container/recover_pending_wiki_tasks.go`). Shipped retrieval instructions also govern consumption, including the instruction to verify underlying passages for exact evidence (SRC-1, `config/prompt_templates/agent_system_prompt.yaml`):

> - For exact quotes, numbers, or code, verify the underlying source passage rather than relying on document metadata or a generated overview.
> --- `config/prompt_templates/agent_system_prompt.yaml`

Evaluation is in scope. The shipped evaluator drives the knowledge QA pipeline and records retrieval, reranking and response metrics. This is executable evaluation machinery, not evidence of a successful evaluation run (SRC-1, `internal/application/service/evaluation.go`):

> err = e.sessionService.KnowledgeQAByEvent(ctx, chatManage, types.Pipline["rag"])
> --- `internal/application/service/evaluation.go`

### Frozen evidence and limits

The single evidence source is SRC-1 at **234aa948db29c10f5ed4b7939285c7b3711c5d4c**; checkout HEAD was verified against acquisition. The applicability cutoff is **2026-10-15**, the supplied run date. No claim concerns later revisions, live hosted deployments or the current contents of linked websites. The evidence tier is **code-grounded**, with repository documentation and prompts separately supporting declared intent. No target code, tests, services or model calls were executed.

External model providers, storage/database servers, Redis, parser services, sandbox providers, browsers and external MCP services are dependencies. Their shipped adapters and configuration belong to the boundary; their independently deployed internals do not. This exclusion prevents claims about provider fidelity, deployed isolation, remote durability, actual model compliance or end-to-end operational reliability. The DeepSeek Harness plugin and MCP API bridge are included shipped clients; the external runtimes consuming them are not attributed to WeKnora (SRC-1, `packages/dsh-weknora/src/index.ts`, `mcp-server/weknora_mcp_server.py`). The mini-program likewise submits source URLs and chat requests to WeKnora, rather than constituting an excluded application (SRC-1, `miniprogram/utils/request.js`).

There is no established source-access gap: the Git source is available. Inspection is a boundary survey, not an audit of every file. Unread implementation branches, alternate backends and platform-specific paths remain available for later jobs at this pin. They are not declared unavailable and do not justify negative capability claims. No observed execution trace or causal experiment has been established; tests and fixtures support inspection of intended checks, not observed success.

### Top-level coverage

Every tracked top-level entry is classified below. Grouped rows classify each named entry identically. Included directories name material paths or responsibilities; inclusion is functional scope, not a claim that every file was read. “Survey” denotes tree or targeted source-search inspection; “read” denotes bounded source passages. There are no unavailable top-level entries. All paths in this table belong to SRC-1.

| Top-level entry | Classification and material paths | Initial inspection; limit or conclusion prevented |
|---|---|---|
| `cmd/` | Included: `server/main.go`, `desktop/main.go`; download and migration utilities | Server and desktop entry-point reads; utility tree survey. No platform execution claim. |
| `internal/` | Included: container/router/handlers; `application/service/knowledge_create.go`, `knowledge_process.go`, `knowledgebase_search.go`, `wiki_ingest.go`, `wiki_page.go`, `memory/`, `agent_history.go`, `session_agent_qa.go`, `evaluation.go`; repositories, model adapters, `agent/`, tools, compaction, skills, sandbox, connectors, IM, streams and access controls | Reads across producer, admission, maintenance, persistence/reload and consumption paths; targeted searches and tree survey elsewhere. Backend-specific correctness and exhaustive authorization coverage not established. |
| `config/` | Included: `prompt_templates/agent_system_prompt.yaml`, retrieval/context/graph/summary templates and application configuration | Agent prompt read; template inventory. Other prompt bodies and configuration branches remain to inspect. |
| `docreader/` | Included: `main.py`, parser registry, splitters, models, protobuf transport and tests | Entry-point read and tree survey; Go gRPC adapter searched. No parser-quality or deployed-service claim. |
| `frontend/` | Included: `src/api/chat/index.ts`, knowledge-base and wiki API clients; knowledge, agent, chat, settings and artifact views, stores and request transport | API searches and view tree survey. UI state and all interactive paths not yet traced in detail. |
| `cli/` | Included: chat, document/KB/chunk/agent commands, acceptance contracts and e2e tests | Command tree and `cmd/chat/chat.go` survey. Does not establish actual CLI acceptance results. |
| `client/` | Included: `agent.go`, `memory.go`, knowledge/retrieval/session/message and evaluation SDK surfaces | Agent endpoint and memory API survey; client tree. No independent external SDK consumer behavior inferred. |
| `mcp-server/` | Included: Python `weknora_mcp_server.py`, launchers, API bridge and tests | Module and transport tree survey. External MCP host scheduling is excluded. |
| `packages/` | Included: `dsh-weknora/src/index.ts`, client/tools/config and plugin tests/contracts | Plugin entry point read and source survey. Enclosing DeepSeek Harness internals are excluded. |
| `miniprogram/` | Included: `utils/request.js`, SSE/config utilities and chat/settings/index pages | API caller read and tree survey. WeChat platform internals excluded. |
| `dataset/` | Included: `qa_dataset.py`, samples and dataset tests | README read and inventory. Dataset generation descriptions are not measured retrieval quality. |
| `tests/` | Included: mini-program contract tests | Tree survey only; not executed. |
| `testdata/` | Included: wiki documents, MHTML and chat-import fixtures | Tree survey only; fixtures are not observed production evidence. |
| `test_agent_config.sh` | Included: shipped agent-configuration check | Root inventory only; body not yet inspected, no check result claimed. |
| `examples/` | Included: `skills/pdf-processing/SKILL.md`, supporting instructions/scripts and `mcp-demo/` | Tree survey. Example skill bodies and demo behavior remain to inspect, not excluded from the target. |
| `migrations/` | Included: SQL schema evolution, including SQLite memory and task-queue migrations, plus database-specific initialization | Tracked-tree survey. No migration execution or cross-database equivalence claim. |
| `third_party/` | Included: vendored `anydoc-go/` parser binding and build sources | Tracked-tree survey. Native parser internals not yet examined. |
| `docker/` | Included: app/docreader/sandbox images, desktop support, supervisor and search-service configuration | Tracked-tree survey. No deployed container behavior established. |
| `deploy/` | Included: `weknora-lite.service` | Tree survey; supervisor deployment path retained in scope. |
| `helm/` | Included: app/frontend/docreader and data-service templates, values and tests | Tracked-tree survey. Cluster behavior not observed. |
| `docker-compose.yml`, `docker-compose.dev.yml` | Included: deployment composition | Inventory and README deployment context; full configuration bodies not yet inspected. |
| `scripts/` | Included: migration/startup/build/package scripts, browser integration, model-catalog generation, test utilities and local model server | Tree survey. Script bodies and generated-data freshness remain to inspect. |
| `Formula/` | Included: `weknora-lite.rb` packaging entry | Tracked-tree survey; installed-package equivalence not established. |
| `rerank_server_demo.py` | Included: demo reranker dependency surface | Root inventory only; no demo performance or service claim. |
| `.github/` | Included: build, release, lint and client e2e workflows | Tracked workflow inventory; CI success not observed. |
| `Makefile`, `go.mod`, `go.sum` | Included: build and dependency boundaries | Root inventory; dependency implementation is not automatically evidence for WeKnora behavior. |
| `.air.toml`, `.dockerignore`, `.env.example`, `.env.lite.example`, `.gitattributes`, `.gitignore`, `.golangci.yml` | Included: development/deployment defaults and tooling controls | Root inventory; bodies remain available, no comprehensive default-configuration claim. |
| `README.md`, `README_CN.md`, `README_JA.md`, `README_KO.md`, `CHANGELOG.md`, `SECURITY.md`, `VERSION` | Included: source-native product/deployment/release/security doctrine | English overview and deployment passages read; remaining documents inventoried, not independently corroborated. |
| `docs/`, `website-docs/` | Included: shipped API/product/operator documentation and assets | Root inventory and README references only; documentation bodies not yet inspected. Live websites are excluded, so no current hosted-doc claim. |
| `misc/` | Included: `dex-config.yaml` authentication configuration; excluded: `intro-video/` promotional production assets | Tree survey. Excluding video production prevents conclusions about that rendering workflow, not the knowledge loop. |
| `LICENSE`, `THIRD_PARTY_NOTICES.md`, `licenses/` | Excluded: legal notices and license bundle | Root/tracked-tree inventory. No license compliance assessment. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Tencent/WeKnora` | 234aa948db29c10f5ed4b7939285c7b3711c5d4c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/weknora-7adf8a01c381/related-systems/Tencent--WeKnora`. Implementation: server/desktop entry points; bounded reads of document creation/admission, caller memory injection, history reload, memory service/extraction, wiki queue/model call, evaluator, plugin and mini-program caller; targeted searches of routers, task/container wiring, client/CLI/MCP and frontend API surfaces. Doctrine/design: README overview/deployment, agent prompt and dataset README; source comments retained as contracts, not run evidence. Top-level coverage table distinguishes read, surveyed and uninspected bodies. | Implementation: [server](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/cmd/server/main.go), [document creation](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/internal/application/service/knowledge_create.go), [agent caller](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/internal/application/service/session_agent_qa.go), [memory extraction](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/internal/application/service/memory/extract.go), [evaluation](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/internal/application/service/evaluation.go). Doctrine/design: [README](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/README.md), [agent prompts](https://github.com/Tencent/WeKnora/blob/234aa948db29c10f5ed4b7939285c7b3711c5d4c/config/prompt_templates/agent_system_prompt.yaml). Additional local anchors appear above and remain within the same repository pin. | No established access gap. Uninspected bodies are available evidence, not negative findings. No observed run or causal experiment registered; prevents conclusions about measured quality, successful persistence/recovery, actual provider compliance and operational reliability. External service internals and live deployments excluded as described above. |
