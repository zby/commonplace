---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "QwenPaw's shipped personal-assistant runtime and state lifecycle at commit 16b2e712d198166c9359e77055b13bf2668bf5ae."
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "16b2e712d198166c9359e77055b13bf2668bf5ae"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/niceirene/qwenpaw
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/qwenpaw-e41495d47fc0/related-systems/niceirene--qwenpaw
  revision: "16b2e712d198166c9359e77055b13bf2668bf5ae"
  sha256: null
---

# QwenPaw boundary

## Boundary and evidence

This run analyses QwenPaw as a personal-assistant application that assembles agents, processes interactive and scheduled requests, exposes tools and integrations, and maintains workspace and session state. Its intended use is to establish the shipped operating mechanism, including memory and context handling, rather than assess only its memory API. The package description declares that use; the executable entry points and request pipeline establish an in-scope, model-dependent enclosing runtime (SRC-1, `pyproject.toml`, `src/qwenpaw/cli/app_cmd.py`, `src/qwenpaw/runtime/runtime.py`, `src/qwenpaw/agents/react_agent.py`).

The boundary is **whole-system** at the acquired commit, including the shipped callers and state-maintenance paths. It includes the Python application, CLI and desktop launchers, browser console, channels, scheduled tasks, ACP interface, native agent loop and alternative-harness adapters, workspace services, persistence, memory backends, prompts, skills, tool and plugin admission, governance and backup mechanisms. It does not treat in-repository callers as an external host. The shared workspace bootstrap registers session load/save hooks, tools, modes and prompt contributors; those paths belong to the same operating system under analysis (SRC-1, `src/qwenpaw/app/workspace/bootstrap_factory.py`).

The initial entry-point trace is:

- Package scripts `qwenpaw` and `copaw` enter `qwenpaw.cli.main:cli`; `app` launches `qwenpaw.app._app:app` through Uvicorn. The app initializes workspace infrastructure and uses the shared bootstrap factory (SRC-1, `pyproject.toml`, `src/qwenpaw/cli/main.py`, `src/qwenpaw/cli/app_cmd.py`, `src/qwenpaw/app/_app.py`).
- Workspace request processing selects the configured backend. The native backend enters `Runtime.run`; other backends enter the shipped harness runtime. The native orchestrator builds an agent, executes it, and runs response/error/finalization hooks. QwenPawAgent extends AgentScope's agent and wraps its model calls (SRC-1, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/runtime/runtime.py`, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/agents/react_agent.py`).
- Channel processing accepts the workspace stream consumer; scheduled agent tasks and the ACP server also call `workspace.stream_query`. These are included application paths, not an excluded enclosing application (SRC-1, `src/qwenpaw/app/channels/manager.py`, `src/qwenpaw/app/crons/executor.py`, `src/qwenpaw/agents/acp/server.py`).
- Session hooks load state before agent construction and save it after response completion. The builder restores `ctx.session_state` into the new agent. Workspace service registration supplies a session store under the workspace's `sessions` directory. This establishes a shipped retention/reload/consumption path, not proof of successful persistence in a deployed instance (SRC-1, `src/qwenpaw/hooks/session/session_hook.py`, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/app/workspace/workspace.py`).
- Workspace prompt contributors read configured Markdown files; memory guidance and retrieval tools come from the selected memory manager. The ReMe adapter declares optional dream and daily-paper maintenance jobs. Console workspace APIs expose reading and writing Markdown and memory content. These surfaces remain in scope alongside automated retention (SRC-1, `src/qwenpaw/runtime/prompt_contributors.py`, `src/qwenpaw/agents/memory/reme_light_memory_manager.py`, `console/src/api/modules/workspace.ts`).
- The separately shipped `qwenpawmail-mcp` script starts a stdio FastMCP server. It is an included auxiliary tool service, not the enclosing agent loop (SRC-1, `pyproject.toml`, `packages/qwenpawmail-mcp/src/qwenpawmail_mcp/__main__.py`).

Minimum passages supporting the classification and state-loop boundary:

> qwenpaw = "qwenpaw.cli.main:cli"
> copaw = "qwenpaw.cli.main:cli"
> qwenpawmail-mcp = "qwenpawmail_mcp.__main__:main"
> --- `pyproject.toml`

> rt = Runtime(workspace=self, app_services=self._app_services)
> async for item in rt.run(request):
>     yield item
> --- `src/qwenpaw/app/workspace/workspace.py`

> if ctx.session_state:
>     agent.load_state_dict(ctx.session_state)
> --- `src/qwenpaw/runtime/builder.py`

> proxy = StateProxy()
> proxy.data = ctx.agent.state_dict()
> proxy.data["mode_state"] = ctx.mode_state
> await session.save_session_state(
>     session_id=ctx.session_id,
>     user_id=user_id,
>     channel=channel,
>     agent=proxy,
> )
> --- `src/qwenpaw/hooks/session/session_hook.py`

The source is frozen at **16b2e712d198166c9359e77055b13bf2668bf5ae** with applicability cutoff **2026-10-15**, the supplied run date. The checkout's HEAD was checked against the acquired revision. This is a code-grounded source analysis: reading executable code supplies implementation evidence; shipped instructions and manifests supply declared contracts. No target code, tests, model calls or external services were executed. No independent execution trace or experiment was supplied. Therefore this boundary does not establish deployment success, reliability, retrieval quality, model compliance or causal improvements.

The source identity remains `https://github.com/niceirene/qwenpaw`. The package manifest names an upstream AgentScope repository in its project URLs; that is package metadata, not authority to substitute another repository or commit (SRC-1, `pyproject.toml`).

### Repository coverage

Every top-level tracked entry is classified below. “Included, not yet inspected” means available frozen evidence reserved for later analysis, not an access gap or a verified behavior. The initial trace establishes the principal request and state loop; it is not an exhaustive audit of every included feature. All paths in this table are under SRC-1.

| Top-level tracked entry | Inclusion and initial inspection | Role and scope limit |
|---|---|---|
| `src/` | Included. Inspected native orchestration in `src/qwenpaw/runtime/{runtime,builder,prompt_contributors}.py`, agent/model-call wrapper in `src/qwenpaw/agents/react_agent.py`, workspace bootstrap and service registration, session hooks, channel/cron/ACP consumers, ReMe adapter excerpts and English MEMORY template. Tree/search inspection located other subsystems. | Main runtime, state producers and consumers. Includes `agents/context/`, `agents/memory/`, `agents/md_files/`, `agents/skills/`, `agents/skill_system/`, `loop/`, `harnesses/`, `providers/`, `drivers/`, `governance/`, `security/`, `checkpoints/`, `backup/`, `config/`, `services/`, `browser/`, `sandbox/`, `pawapp/`, `tauri/`, `tunnel/` and supporting modules under `src/qwenpaw/`. Detailed alternative-backend, security, backup and context algorithms are available but not yet inspected; no correctness assessment is made here. |
| `console/` | Included. Inspected API call sites in `console/src/api/modules/chat.ts` and `console/src/api/modules/workspace.ts`; page and component tree located. | Shipped UI caller and operator editor of chats, workspace Markdown, memory and prompt configuration. Detailed rendering and admission flows remain uninspected, not excluded. |
| `packages/` | Included. Inspected `packages/qwenpawmail-mcp/src/qwenpawmail_mcp/__main__.py` and enumerated its source modules. | Bundled auxiliary mail MCP service, including mail operations and thread storage. Individual tool implementations and package tests remain uninspected. |
| `plugins/` | Included, tree inspected; individual implementations not yet inspected. | Shipped tool, channel, app, bundle and middleware examples/integrations, including `plugins/apps/`, `plugins/tool/`, `plugins/channel/`, `plugins/bundle/` and `plugins/middleware-demo/`. Inclusion prevents silently assigning their responsibilities to an external host; no plugin-specific behavior is established yet. |
| `deploy/` | Included, tree inspected. | `deploy/Dockerfile`, `deploy/entrypoint.sh` and `deploy/config/supervisord.conf.template` are deployment/launch packaging. Their full startup behavior remains uninspected. |
| `docker-compose.yml` | Included, inspected. | Deployment consumer with working-data, secrets and backup volumes. The referenced moving image tag is not frozen image evidence; source inclusion does not prove image equivalence. |
| `pyproject.toml` | Included, inspected project metadata, scripts, dependencies, package data and test configuration. | Declares entry points and external runtime dependencies; dependency declarations do not expose dependency implementations. |
| `setup.py`, `Makefile` | Included, not yet inspected. | Build and developer launch surfaces; no build reproducibility claim. |
| `scripts/` | Included, tree inspected; implementations not yet inspected. | Packaging, desktop verification, startup profiling, release and developer automation in `scripts/pack/`, `scripts/pack-tauri/`, `scripts/verify/`, `scripts/startup_profile/`, `scripts/github/` and `scripts/review-bot/`. Not evidence that their checks passed. |
| `tests/` | Included, suite directories enumerated; test bodies not yet inspected. | `tests/unit/`, `tests/contract/`, `tests/integration/`, `tests/e2e/` and fixtures may supply encoded expectations, not observed results. |
| `e2e/` | Included. Inspected opening scope and UI-test excerpt of `e2e/tests/test_memory.py`; enumerated scenario files. | Shipped UI/system evaluators cover memory, sessions, ACP, channels, cron and other features. No test execution evidence is available. |
| `README.md`, `README_ja.md`, `README_ru.md`, `README_vi.md`, `README_zh.md` | Included, not yet inspected. | Source-native product and setup doctrine; no claims from these files are used in this boundary. |
| `website/` | Included, tree inspected; content not yet inspected. | Documentation, release notes and product website in `website/public/docs/`, `website/public/release-notes/`, `website/src/` and associated scripts/assets. Documentation and website infrastructure are not independently observed assistant operation. |
| `docs/` | Included, tree inspected; contents not yet inspected. | Contains `docs/pawapp-sdk-app-contract-proposal.md`. A proposal is not evidence of adoption without implementation support. |
| `.github/` | Included, tree inspected; workflows not yet inspected. | CI, release and issue automation; workflow existence does not establish a successful run. |
| `CONTRIBUTING.md`, `CONTRIBUTING_zh.md`, `RELEASING.md`, `RELEASING_zh.md`, `SECURITY.md` | Included, not yet inspected. | Contributor, release and security doctrine, not independently verified operating guarantees. |
| `LICENSE` | Excluded from functional analysis; available, deliberately not inspected. | Legal artifact; prevents conclusions about licensing obligations, not the agent state loop. |
| `.dockerignore`, `.flake8`, `.gitattributes`, `.gitignore`, `.nvmrc`, `.pre-commit-config.yaml`, `.python-version` | Included as packaging/development configuration; not yet inspected. | May constrain build inputs, interpreter/tool versions and checks. No reproducibility or tooling-compliance conclusion is made. |

### External dependencies and evidence limits

AgentScope, ReMe, provider APIs and optional local model engines are dependencies, not separately frozen sources. The manifest declares `agentscope[model-ollama]==2.0.6`, `reme-ai==0.4.1.5`, optional Codex/Qoder SDK packages and channel/browser/MCP libraries. QwenPaw's integration and selection logic are included; unvendored dependency internals, provider model behavior and third-party service operation are outside the available evidence. This prevents attributing their internal guarantees or complete inference/maintenance algorithms to inspected QwenPaw code (SRC-1, `pyproject.toml`, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/agents/react_agent.py`).

Live channel accounts, user workspaces, credentials, model outputs, downloaded images and marketplace payloads are not supplied. Their absence prevents claims about deployed state, external content safety and successful end-to-end operation. It does not exclude the shipped code that admits, stores, reloads or uses that content. Available but uninspected repository files are explicitly different from these absent run artifacts.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/niceirene/qwenpaw` | 16b2e712d198166c9359e77055b13bf2668bf5ae | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/qwenpaw-e41495d47fc0/related-systems/niceirene--qwenpaw`. Implementation: initial CLI/app/workspace entry-point trace, native orchestration and builder excerpts, agent/model-call wrapper searches, session load/save hooks, channel/cron/ACP consumers, prompt contributor, ReMe maintenance/tool declarations, console chat/workspace API call sites, bundled mail server entry point and Compose configuration. Doctrine/design: manifest metadata/dependencies, English MEMORY template and memory E2E test scope. Repository tree inspected for coverage; listed paths are initial inspection, not an allowlist. | Implementation: [CLI launch](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/cli/app_cmd.py), [workspace dispatch and services](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/app/workspace/workspace.py), [runtime](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/runtime/runtime.py), [session hooks](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/hooks/session/session_hook.py), [memory adapter](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/agents/memory/reme_light_memory_manager.py). Doctrine/design: [manifest](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/pyproject.toml), [memory instructions](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/src/qwenpaw/agents/md_files/en/MEMORY.md), [memory evaluator scope](https://github.com/niceirene/qwenpaw/blob/16b2e712d198166c9359e77055b13bf2668bf5ae/e2e/tests/test_memory.py). | No repository access gap identified. Dependency internals, live services, actual user state and execution/experiment evidence are not supplied; prevents claims of observed success, quality, reliability or causal benefit. Uninspected available paths remain eligible frozen evidence, as distinguished in the coverage table. |
