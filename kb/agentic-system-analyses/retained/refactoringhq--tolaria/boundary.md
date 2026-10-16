---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Tolaria's Markdown knowledge-base application, agent integrations and shipped service paths at commit 48f2a70844c1e8005a7aa5f1499c66f7678360de, with partial loop inspection."
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/refactoringhq/tolaria
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd/related-systems/refactoringhq--tolaria
  revision: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
  sha256: null
---

# Tolaria boundary

## Boundary and evidence

This run examines Tolaria as a file-backed knowledge-base application with model-dependent paths for consuming and changing that knowledge. It is not a review of any one CLI agent's internal runtime. The intended use is to explain the shipped knowledge, context and agent-integration mechanisms from source, distinguishing application responsibilities from delegated agent behavior.

The target class is **memory/knowledge/context-engineering system**. The README describes the application as managing Markdown knowledge bases, including company documentation used as AI context and assistant memory. This establishes intended use, not evidence of those deployments (SRC-1, `README.md`). The source also supplies executable model-call entry points, rather than merely advertising compatibility with external tools: the frontend selects CLI-agent or direct-model streaming, and native commands dispatch into the corresponding Rust implementations (SRC-1, `src/lib/aiAgentSession.ts`, `src/utils/streamAiAgent.ts`, `src/utils/streamAiModel.ts`, `src-tauri/src/commands/ai.rs`).

> Tolaria is a desktop app for macOS, Windows, and Linux for managing **markdown knowledge bases**. People use it for a variety of use cases:
> --- `README.md`

> if (context.target?.kind === 'api_model') {
> --- `src/lib/aiAgentSession.ts`

The functional boundary includes the desktop application, its React callers and native commands, vault files and derived state, agent prompts and managed guidance, transcript storage, CLI adapters, direct-provider calls, MCP server and UI bridge, and the repository's web/remote/collaboration paths. A caller shipped here is part of the target even when it invokes a library API. Native startup calls `tolaria_lib::run`; the renderer lazy-loads the application. The agent dispatcher names Claude Code, Codex, Copilot, OpenCode, Pi, Antigravity, Kiro and Hermes adapter paths (SRC-1, `src-tauri/src/main.rs`, `src/main.tsx`, `src-tauri/src/ai_agents.rs`).

The boundary kind is **complete artifact, partial loop**, not whole-system. The complete repository is frozen and available, but initial inspection traces selected producer/consumer paths rather than establishing exhaustive coverage of every shipped state path. In particular, vault scanning/cache invalidation, editor admission and serialization, watcher/Git reconciliation, every adapter's permission implementation, and remote collaboration persistence have not been traced end to end. These are available but not yet inspected responsibilities, not unavailable evidence or deliberate functional exclusions. Their inclusion in the target does not establish that their implementations have been assessed. This boundary prevents a whole-system completeness claim and any blanket conclusion about durable correctness, safety or cross-client consistency.

Initial inspection establishes these paths and limits:

| Shipped surface | Initial inspection and bounded significance |
|---|---|
| Desktop/model entry points | Renderer entry and native startup identified; frontend target selection and native stream dispatch inspected. This supports the existence of both model paths, not comprehensive lifecycle behavior (SRC-1, `src/main.tsx`, `src-tauri/src/main.rs`, `src/lib/aiAgentSession.ts`, `src-tauri/src/commands/ai.rs`). |
| Retained conversation consumption | Session-store code reads native transcripts and schedules native writes; message sending builds a formatted message from the current message array. Native storage implementation and complete restart behavior remain untraced (SRC-1, `src/lib/aiWorkspaceSessionStore.ts`, `src/lib/aiAgentSession.ts`). |
| Agent guidance and maintenance | Prompt construction directs agents to vault instructions and bundled product documentation. Guidance seeding/restoration symbols and root guidance paths were inspected by search; template contents and migration cases were not fully audited (SRC-1, `src/utils/ai-agent.ts`, `src-tauri/src/vault/config_seed.rs`, `src-tauri/src/vault/getting_started.rs`). |
| MCP retained-content path | Tool registration and service methods connect search/read/create/update/append operations to vault functions and emit UI refresh actions. The underlying filesystem implementation and complete bridge delivery remain untraced (SRC-1, `mcp-server/index.js`, `mcp-server/tool-service.js`). |
| Direct-model path | Native provider dispatch and OpenAI-compatible payload/tool selection inspected. Documentation calls these chat-only, but implementation can offer a create-note tool when its vault/provider conditions hold; the run must not inherit the documentation's universal no-write claim (SRC-1, `site/concepts/ai.md`, `src-tauri/src/ai_models.rs`, `src-tauri/src/ai_model_tools.rs`). |
| Web/server/collaboration | Web README identifies the shared shell, demo backend and collaborative note page; server entry opens a vault, creates a local state store and starts the service. Routes, collaboration flush/reconcile code and shared packages remain available but not yet traced (SRC-1, `apps/web/README.md`, `apps/server/src/main.ts`, `package.json`). |
| Evaluators and fixtures | Tracked tree identifies frontend/native/MCP tests, browser smoke and integration suites, server tests, and shared-package tests. Package scripts identify test entry points. No tests were executed and their assertions have not been comprehensively inspected; this is not observed quality evidence (SRC-1, `package.json`). |

Two short passages fix consequential distinctions for later work:

> Each agent still owns its authentication, available tools, and runtime behavior.
> --- `site/concepts/ai.md`

> if should_offer_openai_tools(request) {
>         payload["tools"] = serde_json::Value::Array(vec![openai_create_note_tool()]);
>         payload["tool_choice"] = serde_json::Value::String("auto".into());
>     }
> --- `src-tauri/src/ai_model_tools.rs`

External dependencies include the selected installed agent CLIs and their authentication/model services; direct-provider endpoints; MCP clients and SDK; the operating system, Node, Tauri and frontend libraries; and optional Git remotes. Their implementation and live behavior are excluded: the source supports how Tolaria invokes them, not their actual enforcement, reliability or model quality. User vault contents, private deployments and the separately hosted starter-vault repository are not captured; this prevents conclusions about actual user knowledge quality, accumulated memory effectiveness or the current remote starter content. Repository-contained examples and generated documentation remain available source, not independent deployment evidence (SRC-1, `package.json`, `src-tauri/src/vault/getting_started.rs`, `README.md`).

The sole frozen source is the acquired Git repository at **48f2a70844c1e8005a7aa5f1499c66f7678360de**. HEAD was checked against that pin. The applicability cutoff is **2026-10-14**, the supplied run date; dates inside source material do not expand this boundary. The overall tier is **code-grounded**. No target execution, live provider calls, fetched documentation, observed-run artifacts or causal experiments are included. No source access failure was encountered.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/refactoringhq/tolaria` | 48f2a70844c1e8005a7aa5f1499c66f7678360de | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/tolaria-42ddaf2ee8cd/related-systems/refactoringhq--tolaria`. Tracked tree enumerated. Implementation: selected ranges/searches in renderer/native entry points, `src/lib/aiAgentSession.ts`, `src/lib/aiWorkspaceSessionStore.ts`, `src/utils/streamAiAgent.ts`, `src/utils/streamAiModel.ts`, `src/utils/ai-agent.ts`, `src-tauri/src/commands/ai.rs`, `src-tauri/src/ai_agents.rs`, `src-tauri/src/ai_models.rs`, `src-tauri/src/ai_model_tools.rs`, `src-tauri/src/vault/config_seed.rs`, `src-tauri/src/vault/getting_started.rs`, `mcp-server/index.js`, `mcp-server/tool-service.js`, `apps/server/src/main.ts`, and `package.json`. Doctrine/design: `README.md`, `site/concepts/ai.md`, `apps/web/README.md`, prompt text. Reported operation: README's attributed use cases and personal-use account only. | Implementation: [target dispatch](https://github.com/refactoringhq/tolaria/blob/48f2a70844c1e8005a7aa5f1499c66f7678360de/src/lib/aiAgentSession.ts), [direct tools](https://github.com/refactoringhq/tolaria/blob/48f2a70844c1e8005a7aa5f1499c66f7678360de/src-tauri/src/ai_model_tools.rs), [MCP service](https://github.com/refactoringhq/tolaria/blob/48f2a70844c1e8005a7aa5f1499c66f7678360de/mcp-server/tool-service.js). Doctrine/design: [AI contract](https://github.com/refactoringhq/tolaria/blob/48f2a70844c1e8005a7aa5f1499c66f7678360de/site/concepts/ai.md). Reported operation: [README](https://github.com/refactoringhq/tolaria/blob/48f2a70844c1e8005a7aa5f1499c66f7678360de/README.md). | No checkout access gap. Initial scope is not an allowlist. Partial inspection limits are identified above. External CLI internals, live services, user vaults and separate starter source are not frozen; no observed run or intervention supports operational success or causal effectiveness. |
