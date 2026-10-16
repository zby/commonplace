---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Voiden's shipped agent-facing MCP integration subsystem at commit d7a0d05c40acb6cc483000643c700f17aecba0ef."
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: subsystem-only
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/voidenhq/voiden
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/voiden-98188b4a2f55/related-systems/voidenhq--voiden
  revision: d7a0d05c40acb6cc483000643c700f17aecba0ef
  sha256: null
---

# Voiden boundary

## Boundary and evidence

This run analyses **Voiden's agent-facing MCP integration subsystem**, not the entire desktop API client as an autonomous agent. Its intended use is to explain how external agents discover and execute project requests, retain results, select environments, acquire missing execution plugins, and consume published request-backed tools. The target class is **extension or tool mechanism** and the boundary kind is **subsystem-only**. The enclosing model-driven decision loop belongs to an external host; serving that loop through MCP is sufficient for this narrower target to be in scope.

Voiden describes itself as an offline API client, with requests, documentation and tests in text files, rather than as an enclosing model runtime (SRC-1, `README.md`). The shipped implementation establishes an agent-callable execution mechanism: the bundled CLI registers a project against its own hidden stdio server, then that server registers request tools and plugin-management tools. The model host decides when to invoke those tools; that responsibility is not attributed to Voiden (SRC-1, `apps/electron/src/voiden-cli.ts`).

> const serverCommand: ServerCommand = { command: 'voiden', args: ['mcp-stdio', projectPath] }
> const installed = installMcpIntegration(projectPath, targets, MCP_SKILL_MARKDOWN, serverCommand)
> --- `apps/electron/src/voiden-cli.ts`

> registerFixedTools(server, projectRoot, runtimeVars, activePlugins, selectedEnv)
> --- `apps/electron/src/voiden-cli.ts`

> registerPluginManagementTools(server, activePlugins)
> await server.connect(new StdioServerTransport())
> --- `apps/electron/src/voiden-cli.ts`

The repository tree and shipped consumers establish three related entry paths, not just an isolated exported library. The bundled `voiden agent` / `mcp-stdio` path registers and serves project execution tools; `voiden-runner mcp install` / `serve` provides the standalone runner path; `voiden-mcp` starts the separate publishing server. The desktop MCP IPC handler is also an included caller, not an excluded external application. It writes host registration and refreshes composed guidance. These responsibilities are visible in SRC-1, `apps/electron/src/voiden-cli.ts`, `packages/voiden-runner/src/index.ts`, `packages/voiden-mcp/src/index.ts`, and `apps/electron/src/main/ipc/mcp.ts`. Documentation and comments contain older descriptions of tool counts and registration targets; executable call sites govern this boundary, not those descriptions.

### Functional coverage and limits

This is a subsystem coverage map, not a claim that every desktop or build path has been inspected. All listed paths refer to SRC-1 at the frozen commit. Included but not yet inspected material is distinguished from unavailable external evidence.

| Responsibility | Included paths and initial inspection | Boundary limit and conclusion prevented |
| --- | --- | --- |
| Agent entry points and registration callers | Inspected `apps/electron/src/voiden-cli.ts`, `apps/electron/src/main/ipc/mcp.ts`, and relevant command declarations/call sites in `packages/voiden-runner/src/index.ts`; inspected launcher prefix in `apps/electron/bin/voiden`. Launcher dispatch remainder, Windows launcher and packaging wiring remain available for later inspection. | Desktop MCP callers belong to the target. Initial reads do not establish cross-platform packaged launch reliability. |
| Host registration and procedural guidance | Inspected registration primitives in `packages/executors/src/mcpInstall.ts`, standalone guidance in `packages/executors/src/skillContent.ts`, and composition inputs in `apps/electron/src/main/skillsComposer.ts`. Skill installation, refresh and base-guide paths are included but not yet fully inspected. | This includes instructions consumed by external agents, not merely server APIs. Successful host discovery and obedience to installed guidance are not observed. |
| Request discovery, environment selection, execution and result retention | Inspected fixed tool handlers in `packages/voiden-runner/src/mcpServing.ts`, the main `runVoidFile` path in `packages/voiden-runner/src/runner.ts`, and `upsertResponseBlock` in `packages/voiden-runner/src/resultBlock.ts`. Parser, linked-block resolution, environment helpers and shared execution orchestration are included dependencies available for later tracing. | The core reads project files, dispatches execution and writes recorded responses. This does not establish correctness of every protocol implementation or an autonomous learning process. |
| Plugin admission and session maintenance | Inspected management handlers in `packages/voiden-runner/src/plugins/managementTools.ts` and loader/download interfaces in `packages/voiden-runner/src/plugins/loader.ts`. Registry, store, community and update helpers are included, not yet fully inspected. | Core acquisition and reloading behavior can be analysed; downloaded plugin bytes and live registry contents are not frozen by this repository commit. |
| Published request-backed tools | Inspected `packages/voiden-mcp/src/index.ts`, the initial planning and HTTP registration path in `packages/voiden-mcp/src/lib.ts`, and `packages/voiden-runner/src/mcpToolCapability.ts`; runner publishing callers were located in `packages/voiden-runner/src/index.ts`. Scheduler, transport, authorization, supervision and persistence helpers in these packages are included but not yet fully inspected. | Core publishing orchestration is included. Actual `/tool` semantics are delegated to a separately supplied plugin, so the core interfaces alone cannot establish end-to-end verification, binding or admission correctness. |
| Tests and examples relevant to this subsystem | Tracked test and sample paths are available within the registered repository; no tests or examples were executed. | They may supply contracts or reported expectations after inspection, not observed runtime evidence merely because they exist. |

The retention boundary is concrete: `write_result` invokes `upsertResponseBlock`, which reads the existing document, inserts or replaces a response associated with a request UID, and writes the file. `runVoidFile` separately reloads document content for execution. This establishes source-visible production and later reading of the same document format, not that every retained response influences later model decisions (SRC-1, `packages/voiden-runner/src/mcpServing.ts`, `packages/voiden-runner/src/resultBlock.ts`, `packages/voiden-runner/src/runner.ts`).

> upsertResponseBlock(resolved, requestUid, result as RunResult)
> return textResult({ written: true, filePath, requestUid })
> --- `packages/voiden-runner/src/mcpServing.ts`

### External dependencies and deliberate exclusions

- **External model hosts and providers:** Claude Code, Codex and other MCP clients are consumers, not frozen implementations in this source. Their inference, context assembly, tool selection, confirmation policies and later reuse of recorded content cannot be established here. The shipped host-configuration writers and guidance remain included (SRC-1, `packages/executors/src/mcpInstall.ts`, `packages/executors/src/skillContent.ts`).
- **Separately distributed plugins:** protocol builders, pipeline hooks, extension guides and the `/tool` capability implementation may arrive through plugin repositories or release assets. These are unavailable as pinned implementation evidence in this source set, not merely uninspected tracked files. Core delegation and download paths are inspectable, but plugin semantics and release-byte behavior cannot be reconstructed from core contracts alone (SRC-1, `packages/voiden-runner/src/plugins/loader.ts`, `packages/voiden-runner/src/mcpToolCapability.ts`, `.gitignore`).
- **General desktop application:** editor presentation, terminal/Git UX, unrelated imports, themes and general desktop behavior are deliberately excluded except where they produce, install or consume this subsystem's state or instructions. This prevents a whole-product characterization or a claim that the full desktop request loop has been covered. The included Electron IPC and skill callers are not excluded by this rule.
- **Live operation:** network APIs, user project documents, credentials, installed plugin caches, live registries, host config files and deployment services are not captured. Dependencies such as the MCP SDK and optional tunnel services are not independently frozen source repositories. No target execution, provider calls, test runs or deployment experiments were performed. Reliability, security effectiveness, performance and causal improvement therefore remain unestablished.

The delegation boundary is explicit in executable code, rather than inferred solely from documentation (SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`):

> export async function planServedTools(projectRoot: string, env: Record<string, string>, activePlugins: string[], opts?: PlanServedToolsOptions): Promise<ServeDecision[]> {
>   if (!provider) return []
>   return provider.planServedTools(projectRoot, env, activePlugins, opts)
> }
> --- `packages/voiden-runner/src/mcpToolCapability.ts`

The frozen evidence is repository `https://github.com/voidenhq/voiden` at **d7a0d05c40acb6cc483000643c700f17aecba0ef**, with applicability cutoff **2026-10-14**. The acquired checkout's HEAD was verified against that pin. The overall tier is **code-grounded**: implementation reads establish the subsystem boundary, while source-native documentation and guidance supply declared intent. No additional repository, web page, release asset or capture is registered. The complete disposition means this boundary has been established, not that the entire product or external agent loop has been analysed.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/voidenhq/voiden` | d7a0d05c40acb6cc483000643c700f17aecba0ef | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/voiden-98188b4a2f55/related-systems/voidenhq--voiden`. Implementation: tracked root tree, root `package.json`, `.gitignore`; bundled CLI and MCP IPC caller; runner command call sites, fixed tools, main execution path, result write-back, capability registry, plugin-management and loader interfaces; publishing entry and initial planning/HTTP dispatch; host registration primitives and skill composition inputs. Doctrine/design: `README.md`, `docs/voiden-cli.md`, `docs/mcp-tool-block-spec.md`, and `packages/executors/src/skillContent.ts`. Listed paths record initial inspection, not a restriction on later inspection at this commit. | Implementation: [bundled CLI](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/apps/electron/src/voiden-cli.ts), [fixed tools](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/packages/voiden-runner/src/mcpServing.ts), [capability delegation](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/packages/voiden-runner/src/mcpToolCapability.ts), [publishing core](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/packages/voiden-mcp/src/lib.ts). Doctrine/design: [README](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/README.md), [installed MCP guidance](https://github.com/voidenhq/voiden/blob/d7a0d05c40acb6cc483000643c700f17aecba0ef/packages/executors/src/skillContent.ts). | External plugin implementations and downloaded assets, model hosts and dependencies, actual project/host state and live API operation are not frozen. Prevents full plugin-level execution/admission claims, host reasoning claims, and observed-run or causal-effect conclusions. Available but uninspected tracked paths are coverage to be traced, not access gaps. Documentation reports of manual verification are attributed claims, not registered execution traces. |
