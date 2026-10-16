---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "nao's analytics-agent runtime, context-building CLI and maintenance surfaces at commit 0085625a8fd22e4f404b6a3971d153f6b6699479."
run-id: AAS-2026-10-14-nao-f9d36a4b7276-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/getnao/nao
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/nao-f9d36a4b7276/related-systems/getnao--nao
  revision: "0085625a8fd22e4f404b6a3971d153f6b6699479"
  sha256: null
---

# nao boundary

## Boundary and evidence

This run examines how nao builds and consumes analytics context, runs model-and-tool conversations, retains state and supports context improvement. The target is the shipped repository system, not just its memory extractor, Python CLI or MCP interface. Its primary class is **enclosing runtime**: nao creates the tool loop, builds its instructions and messages, streams its responses and persists the resulting conversation. Its context-building and maintenance components remain inside that boundary. SRC-1: `README.md`, `cli/nao_core/main.py`, `apps/backend/src/services/agent.ts`.

The README declares the relationship between the builder and consumer:

> Create the context of your analytics agent with nao-core cli: data, metadata, modeling, rules, etc. <br/>
> Deploy a UI for anyone to chat with your agent and run analytics on your data.
> --- `README.md`

The implementation constructs the runtime rather than only returning a tool result:

> this._agent = new ToolLoopAgent({
> --- `apps/backend/src/services/agent.ts`

The boundary is **whole-system**, covering the material shipped paths for producing, maintaining, admitting and consuming state. This is a functional scope, not a claim that every implementation file has already been read or that the product has been executed. Initial tracing establishes the following connected responsibilities:

- **Context production and delivery.** The CLI registers initialization, synchronization, chat, deployment, skills and testing commands. Synchronization invokes configured providers and renders templates into project context. The CLI chat driver launches the bundled chat server and FastAPI process; it is part of nao, not an external host. Container startup admits local, Git or API-delivered context. Git context refresh and the FastAPI refresh scheduler are included maintenance paths. SRC-1: `cli/nao_core/main.py`, `cli/nao_core/commands/sync/__init__.py`, `cli/nao_core/commands/chat.py`, `cli/nao_core/context/git.py`, `docker/entrypoint.sh`, `apps/backend/fastapi/main.py`.
- **Admission and execution.** The backend registers web-agent, test, messaging, deployment, automation and MCP entry points. The web route applies authentication and project-role checks; its handler creates or updates a chat, reloads stored messages, initializes MCP and skills, and creates the agent. The frontend is a shipped caller of `/api/agent` and reloads persisted chat messages. Messaging services, automations and MCP sub-agent callers also belong to nao. Their external transports do not make their shipped orchestration external. SRC-1: `apps/backend/src/app.ts`, `apps/backend/src/routes/agent.ts`, `apps/backend/src/handlers/agent.ts`, `apps/frontend/src/hooks/use-agent.ts`, `apps/backend/src/handlers/automation.handler.ts`, `apps/backend/src/mcp/tools/sub-agent.ts`, `apps/backend/src/services/slack.ts`, `apps/backend/src/services/teams.ts`, `apps/backend/src/services/telegram.ts`, `apps/backend/src/services/whatsapp.ts`, `apps/backend/src/services/mattermost.ts`. For the latter callers, initial inspection located agent creation; their full channel-specific policies are not yet inspected.
- **Retained state and later consumption.** The streaming agent persists settled response messages. Prompt construction reloads user memories and project rules and assembles available context, tools and skills. The memory service invokes a model extractor and persists new or superseding memories; queries reload active memories and expose editing/deletion operations. Conversation compaction reconstructs history from a stored marker. These are distinct retained-state mechanisms within the same system, not evidence that all context is automatically learned. SRC-1: `apps/backend/src/services/agent.ts`, `apps/backend/src/services/memory.ts`, `apps/backend/src/queries/memory.ts`, `apps/backend/src/services/compaction.ts`, `apps/backend/src/components/ai/system-prompt.tsx`, `apps/backend/src/components/ai/memory-system-prompt.tsx`.
- **Improvement and evaluation.** A recommendation run loads prior recommendations and context-file costs, runs a restricted agent, reconciles collected findings and can request pull requests when configured. Live-context update code is also included, so proposing a change is not silently equated with admitting it to runtime context. Separately, shipped maintenance skills guide an external editing agent. The test service runs the agent and generates verification SQL over collected results; the CLI evaluates tool assertions and compares returned data. These evaluators are part of the target, not an independent validation of it. SRC-1: `apps/backend/src/services/context-recommendations.service.ts`, `apps/backend/src/services/context-pr.service.ts`, `apps/backend/src/services/context-explorer-git/live-context.service.ts`, `skills/README.md`, `skills/audit-context/SKILL.md`, `apps/backend/src/services/test-agent.service.ts`, `cli/nao_core/commands/test/runner.py`.

Two short passages fix the retention and maintenance scope:

> const memories = await memoryService.safeGetUserMemories(this.chat.userId, this.chat.projectId, this.chat.id);
> --- `apps/backend/src/services/agent.ts`

> const recorded = await repairRecommendationTriggerRefs(projectId, collector.recorded);
> --- `apps/backend/src/services/context-recommendations.service.ts`

The latter is followed by reconciliation and persistence, and conditional automatic PR creation in that same source. It supports including the improvement path, not a conclusion that recommendations improve answer quality.

### Repository coverage

The table classifies every top-level tracked entry at the frozen commit. “Included” makes a path available for later source inspection within this boundary. “Located” means tree/search inspection only; it is not an access gap or an implementation conclusion. Excluded development material is not used to characterize runtime behavior.

| Top-level tracked entry | Classification and material paths/role | Initial inspection and limits |
| --- | --- | --- |
| `apps` | Included: `apps/backend/src/index.ts`, `app.ts`, routes, handlers, agents, prompts, services, queries, DB schemas; `apps/backend/fastapi/`; both migration trees; `apps/backend/tests/`; `apps/frontend/src/`, tests and Vite runtime; `apps/shared/src/` and tests. These cover orchestration, state admission/persistence, tools, maintenance, UI consumers and shared contracts. | Read core entry points, web handler, agent construction/stream/prompt ranges, memory service/queries, compaction, recommendation run, test service and prompt ranges. Searched frontend transport/reload, messaging/automation/MCP callers, SQL tools, FastAPI refresh/endpoints and live-context/PR services. Schemas, migrations, shared contracts, most tool bodies, storage/story paths and test assertions remain for targeted inspection; no claims of exhaustive correctness or security follow. Tracked `.node_modules-*` entries are located packaging material, not executed. |
| `cli` | Included: `nao_core/main.py`, command drivers, `commands/sync/providers/`, context providers, templates/config, `commands/test/`, build/package files and `tests/`. | Read command registration, sync dispatcher and Git context provider; inspected chat-driver launch locations and test-run comparison range. Provider-specific implementations, deployment details and tests are located, not yet fully inspected. The caller and evaluator are not excluded. |
| `skills` | Included: setup, rule writing, context tests, audit, semantic layer, custom charts, migrations and deployment instructions plus templates. | Read `README.md` and `audit-context/SKILL.md`; remaining skill bodies located. Instructions are doctrine/design until traced to implementation or run evidence; no external editing harness is claimed as nao's runtime. |
| `example` | Included: `RULES.md`, `nao_config.yaml`, `agent/`, `databases/`, `docs/`, `semantics/`, `templates/`, `tests/`, `.naoignore` and bundled DuckDB data. | Tree inspected; content not yet read. Shipped demo context and evaluator inputs remain inside scope; no demo success or representativeness conclusion. |
| `docker` | Included: `entrypoint.sh`, `supervisord.conf`, extension/license setup scripts. | Read context admission portion of entrypoint; remaining launch/setup details located. No image execution evidence. |
| `Dockerfile` | Included: image construction and packaged runtime. | Located, not yet inspected in detail; no build reproducibility conclusion. |
| `docker-compose.yml`, `docker-compose.ducklake.yml`, `docker-compose.test.yml` | Included: deployment and integration-test configurations. | Located; actual deployment behavior and integration-test results not established. |
| `helm` | Included: chart, values, templates, architecture and deployment documentation. | Tree inspected, including deployment/config/secret templates and connection test. Contents not yet inspected; no Kubernetes availability or security conclusion. |
| `caddy` | Included: `Caddyfile` reverse-proxy integration. | Located; no proxy-correctness conclusion yet. |
| `.github` | Included: workflows for distribution/build/test and assets used by README. | Tree inspected. Workflow bodies and published artifacts not inspected; no CI-pass or release-equivalence conclusion. |
| `scripts` | Included: build/release/setup and configuration-document generation support. | Tree and package-script consumers inspected; script bodies not inspected. No release provenance conclusion. |
| `README.md` | Included: product intent, quickstart, evaluation and architecture pointers. | Read completely; declarations do not establish observed performance. |
| `README-dockerhub.md`, `.env.example` | Included: deployment and configuration contracts. | Located; not yet inspected. |
| `package.json` | Included: workspace and development entry points. | Read completely; dependencies are declarations, not audited implementation. |
| `package-lock.json`, `bun.lock`, `bunfig.toml` | Included: dependency/build configuration. | Located; no dependency audit or installed-version verification. |
| `.claude`, `.entire` | Excluded: repository-development review skill and development-session tooling settings. | Tree inspected only; exclusion prevents claims about nao's own contributor-agent workflow. Product skills under `skills/` remain included. |
| `.husky`, `.vscode` | Excluded: contributor hooks and editor settings. | Located; no contributor-environment or hook-enforcement conclusion. |
| `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` | Excluded: repository contributor instructions. | Located; no assessment of contributor compliance. They do not govern this analysis. |
| `SECURITY.md`, `LICENSE` | Excluded from operational mechanism analysis: security-reporting and legal documents. | Located; no vulnerability-response or legal-compliance conclusion. |
| `.dockerignore`, `.gitignore`, `.npmrc`, `.nvmrc`, `.prettierignore`, `eslint.config.js`, `prettier.config.js`, `pyrightconfig.json` | Excluded: contributor/build hygiene and static-tool settings. | Located; no complete packaging, linting or type-checking audit. Product package/deployment entry points remain included above. |

### Frozen evidence and limits

The sole source is SRC-1 at full commit `0085625a8fd22e4f404b6a3971d153f6b6699479`; the acquired checkout's HEAD was checked against that pin. The analysis cutoff is **2026-10-14**, the supplied run date. The overall tier is **code-grounded**: source text supports implementation findings, while repository documentation and prompts support declared intent. No target code, tests, examples, models or services were executed. No observed-run or causal-experiment layer is established.

External dependencies include model providers and the AI SDK, warehouse/database systems, Git hosting and remote context repositories, MCP services, messaging platforms, storage backends and deployment infrastructure. Their nao-side adapters remain included; their remote implementation and operational state are not frozen. This prevents conclusions about provider fidelity, deployed permissions, actual data quality, end-to-end reliability, latency/cost, successful change admission or answer-quality improvement. These are external-evidence limits, not missing access to the included repository. External documentation websites linked by nao and subsequently published binaries, images or skill registries were not captured and cannot supply evidence in this run. The source register covers the entire pinned repository; initial inspected paths below are not an allowlist.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/getnao/nao` | 0085625a8fd22e4f404b6a3971d153f6b6699479 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/nao-f9d36a4b7276/related-systems/getnao--nao`. Implementation: repository tree; `package.json`; `cli/nao_core/main.py`, `commands/sync/__init__.py`, `commands/chat.py`, `context/git.py`, `commands/test/runner.py`; `apps/backend/src/index.ts`, `app.ts`, `routes/agent.ts`, `handlers/agent.ts`, `services/agent.ts`, `services/memory.ts`, `queries/memory.ts`, `services/compaction.ts`, `services/context-recommendations.service.ts`, `services/test-agent.service.ts`; scoped searches of channel, automation, MCP, SQL, context-PR/live-context and frontend consumers; FastAPI refresh range and endpoint inventory; container context-admission range. Doctrine/design: complete `README.md`, `skills/README.md`, `skills/audit-context/SKILL.md`, memory-extraction prompt and initial system-prompt range. Coverage table distinguishes deeper inspection still pending. | Implementation: [agent runtime](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/apps/backend/src/services/agent.ts), [memory persistence/reload](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/apps/backend/src/queries/memory.ts), [context improvement](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/apps/backend/src/services/context-recommendations.service.ts), [CLI driver](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/cli/nao_core/main.py). Doctrine/design: [product contract](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/README.md), [maintenance instruction](https://github.com/getnao/nao/blob/0085625a8fd22e4f404b6a3971d153f6b6699479/skills/audit-context/SKILL.md). | No repository access gap identified. External services, deployed state and execution evidence are not supplied; this prevents performance, successful-operation and causal-effect conclusions. Unread included files are pending inspection, not unavailable evidence. |
