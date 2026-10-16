---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Continuity's desktop AI workspace, memory server, plugin plane and organization server at commit 4ca8f6b4108aa4494e3861ed33c8019dbd662c67."
run-id: AAS-2026-10-14-continuity-3e490e1d39f0-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/uziiuzair/continuity
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/continuity-3e490e1d39f0/related-systems/uziiuzair--continuity
  revision: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
  sha256: null
---

# Continuity boundary

## Boundary and evidence

This run examines Continuity as a shipped desktop AI workspace, not just its standalone memory API. Its intended use is conversation-driven work with persistent personal and project context. The repository also ships a standalone MCP memory server, a plugin host and SDK, two plugins, and an organization memory HTTP server. These are included even where they run in separate processes. The target class is **enclosing runtime**: the desktop chat provider constructs model inputs, issues model calls, dispatches tools, feeds results into subsequent calls, and saves conversation output. Memory/knowledge/context engineering is a major responsibility within that runtime, not the entire target. The boundary kind is **whole-system**. These classifications follow SRC-1, `app/layout.tsx`, `providers/chat-provider.tsx`, `server/index.ts`, `plugin-host/src/index.ts`, `plugins/continuity-threads-engagement/src/index.ts` and `org-server/src/app.ts`.

The frozen evidence is repository `https://github.com/uziiuzair/continuity` at `4ca8f6b4108aa4494e3861ed33c8019dbd662c67`. The acquired checkout's HEAD matched that revision and its tracked working tree was clean on inspection. Applicability is limited to that revision with analysis cutoff **2026-10-14**, the supplied run date. No other repository, published package, live service, installed user data or revision is evidence. The overall tier is **code-grounded**: executable sources and shipped callers were traced, with documentation used as declared intent rather than proof of operation.

### Classification anchors

The product declares its intended use in SRC-1, `README.md`:

> **A local-first AI workspace where chat is the write path and structure emerges from conversation.**
> --- `README.md`

The enclosing model loop is implemented in SRC-1, `providers/chat-provider.tsx`:

> // Tool calling loop - keep calling until no more tool calls
> let currentMessages = [...aiMessages];
> let finalContent = "";
> let response;
> const MAX_TOOL_ITERATIONS = 10; // Safety limit
> --- `providers/chat-provider.tsx`

The standalone memory service is not the sole shipped consumer. The same chat provider constructs each request using retained context (SRC-1, `providers/chat-provider.tsx`):

> const parts = [
>   PERSONALITY_SYSTEM_PROMPT,
>   ...(userProfilePrompt ? [userProfilePrompt] : []),
>   ...(narrativePrompt ? [narrativePrompt] : []),
>   ...(memoryContextPrompt ? [memoryContextPrompt] : []),
>   WORKSPACE_AGENT_PROMPT,
> --- `providers/chat-provider.tsx`

The shipped behavioral prompt directs model-mediated retention, rather than leaving all memory production to an unspecified host (SRC-1, `lib/ai/workspace-agent-prompt.ts`):

> **On each conversation:**
> 1. Check your pre-loaded memories for relevant context
> 2. Use \`recall\` to search for specific memories if needed
> 3. Use \`remember\` to store important new information
> --- `lib/ai/workspace-agent-prompt.ts`

The application also owns a model-dependent maintenance path (SRC-1, `lib/ai/narrative-synthesis.ts`):

> const messages: ChatMessage[] = [
>   { role: "system", content: SYNTHESIS_SYSTEM_PROMPT },
>   { role: "user", content: userMessage },
> ];
>
> const response = await aiClient.chat(messages);
> --- `lib/ai/narrative-synthesis.ts`

### Functional inclusions and traced paths

- **Conversation production and later reuse:** `app/layout.tsx` mounts `ChatProvider`; `providers/chat-provider.tsx` reloads saved thread messages, builds a fresh system prompt, runs the bounded streaming/tool loop, dispatches built-in, MCP and plugin tools, and saves final messages through `lib/db/messages.ts`. The same provider schedules a synthesis check after saved conversation activity. These are shipped driver responsibilities, not excluded external application behavior. SRC-1, `app/layout.tsx`, `providers/chat-provider.tsx`, `lib/db/messages.ts`.
- **Memory admission, persistence, retrieval and maintenance:** in-app memory tools reach `lib/db/memories.ts`, which writes versioned memories and archives rather than physically deleting through its forget path. `lib/db/memory-db.ts` opens and bootstraps the memory database. `server/index.ts` registers memory, project, search, relationship, lifecycle and narrative/learning tool modules for external MCP callers. `lib/ai/memory-tools.ts` loads retained memories into the chat prompt. `lib/ai/narrative-synthesis.ts` gathers memories, unabsorbed learnings and a previous narrative, calls the configured AI client, saves a narrative and marks learnings absorbed. `providers/memories-provider.tsx` reads retained state for the UI and supplies launch/manual synthesis paths. Inclusion establishes ownership of these paths, not the correctness of every write or scheduling condition. SRC-1, those paths and `server/tools/narrative-tools.ts`.
- **Other retained work and context:** canvas/database tools and their persistence providers, journal entries and links, briefing projections, and Obsidian vault scanning/read/write are included. Vault scan callers reach `lib/vault/memory.ts`; its retained index is later consumed by `lib/ai/obsidian-tools.ts` and the chat prompt builder. Deep research has its own model prompts and orchestration; the chat caller handles completion, canvas output and saved chat summary. SRC-1, `components/settings/panels/VaultPanel.tsx`, `lib/vault/memory.ts`, `lib/ai/obsidian-tools.ts`, `lib/ai/research-engine.ts`, `providers/chat-provider.tsx`, `lib/db/journal.ts`, `lib/db/journal-links.ts`, `lib/services/briefing-service.ts`.
- **Plugin and organization paths:** the frontend manager spawns the plugin host and plugin processes; host handlers expose database access, prompt/tool registration, events, settings, MCP controls and UI registration. The SDK and both shipped plugins are included. Org Memory Sync subscribes to memory events, queues pushes, pulls server records through SDK database writes, and provides a search tool and prompt. The organization server supplies push, pull and search endpoints. Include both ends and the SDK default database routing when assessing whether they actually form the intended memory loop; do not assume integration from their names. SRC-1, `lib/plugins/manager.ts`, `plugin-host/src/handlers/db.ts`, `plugin-sdk/src/db.ts`, `plugins/continuity-org-memory-sync/src/index.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`, `org-server/src/app.ts`.
- **Independent plugin model workflow and evaluators:** Threads Engagement owns scheduled search, model relevance scoring, model reply drafting, a plugin-local database, a review UI and an approval endpoint that calls its Threads API wrapper. Its `AIEvaluator` is a production relevance/drafting component, not an experimental evaluation of Continuity memory quality. Organization-server tests include an injected-server push/pull/search round trip; their text is implementation evidence of a test definition, not an observed passing run or proof that the desktop sync integration works. SRC-1, `plugins/continuity-threads-engagement/src/index.ts`, `plugins/continuity-threads-engagement/src/cron.ts`, `plugins/continuity-threads-engagement/src/ai-evaluator.ts`, `plugins/continuity-threads-engagement/src/ui-server.ts`, `org-server/tests/roundtrip.test.ts`.
- **Shipped instructions:** runtime prompts in `lib/ai/`, plugin-injected prompts, and developer memory-bank maintenance instructions in `CLAUDE.md`/`claude_docs/` remain within the evidence boundary. The developer instructions describe a separate agent-assisted development procedure, not automatic in-app execution. Source documentation and progress claims require implementation corroboration before becoming claims about this frozen runtime. SRC-1, `CLAUDE.md`, `claude_docs/ACTIVE_CONTEXT.md`, `lib/ai/workspace-agent-prompt.ts`, `plugins/continuity-org-memory-sync/src/index.ts`.

### Repository coverage

Every top-level tracked file or directory is accounted for below. All paths in the table refer to SRC-1. “Included” fixes functional scope; it does not claim exhaustive line-by-line inspection. Inspection is concentrated on entry points, state producers, admission/persistence, maintenance and later consumers. Available ancillary files not yet inspected are identified separately from unavailable evidence or deliberate exclusions.

| Top-level tracked path | Classification and role | Material paths / initial inspection and limits |
|---|---|---|
| `app/` | Included: shipped frontend entry points | `layout.tsx` read; `page.tsx`, `journal/page.tsx`, `memories/page.tsx` traced to chat, journal provider and memory browser. Fonts and styling not yet inspected; no visual-quality conclusion. |
| `components/` | Included: user-facing state producers and consumers | Traced `layout/AppShell.tsx`, `memories/`, `journal/JournalPage.tsx`, `briefing/HomeBriefingView.tsx`, `settings/panels/VaultPanel.tsx`; canvas, chat, connector and plugin presentation remain in scope. Initial inspection is not a complete UI or approval-policy audit. Icons, styling and incidental `.DS_Store` not inspected. |
| `lib/` | Included: model, tool, persistence and integration logic | Read or searched `ai/index.ts`, `ai/workspace-agent-prompt.ts`, `ai/memory-tools.ts`, `ai/narrative-synthesis.ts`, `ai/research-engine.ts`, `ai/obsidian-tools.ts`, provider clients, web/plugin tools; `db/memories.ts`, `db/memory-db.ts`, `db/messages.ts`, journal/link modules, `db-service.ts`; `vault/memory.ts`, `services/briefing-service.ts`, `mcp-auto-setup.ts`, `mcp/manager.ts`, `mcp/stdio-transport.ts`, `plugins/manager.ts`. Remaining canvas, transport, schema, tool and CRUD details are available for later inspection, not access gaps. |
| `providers/` | Included: shipped lifecycle, reload and model drivers | `chat-provider.tsx` prompt/model/persistence paths inspected; `memories-provider.tsx`, `database-provider.tsx`, `journal-provider.tsx` searched for reload, schema and maintenance paths. Other providers are mounted by the included layout; detailed authorization/subscription/UI behavior not yet inspected. |
| `server/` | Included: standalone and desktop MCP memory service | `index.ts`, `bin/cli.mjs`, `build.mjs`, `db/connection.ts`, `db/schema.ts`, `db/memories.ts`, `tools/` registration and narrative/learning surface traced. Other CRUD/search/lifecycle details and committed `dist/server.mjs` remain available; source-to-bundle equivalence has not been established. |
| `plugin-host/` | Included: plugin bridge and database routing | `src/index.ts`, `src/server.ts`, `src/db.ts`, `src/handlers/db.ts`, `src/handlers/chat.ts`, `src/handlers/events.ts` searched/read. Other handlers and committed distribution remain in scope; full capability enforcement and bundle parity not yet assessed. |
| `plugin-sdk/` | Included: actual plugin caller API | `src/index.ts`, `src/db.ts` inspected/searched; README API headings scanned. Other wrappers, client transport and committed `dist/` are available; parity with source not yet established. |
| `plugins/` | Included: both shipped plugin workflows | Org sync `src/index.ts`, `src/sync-engine.ts` read; Threads `src/index.ts`, `src/ai-evaluator.ts`, `src/cron.ts` read, `src/db.ts`, `src/ui-server.ts` searched through persistence and approval. Manifests, API wrappers and UI assets available for further inspection. Deliberately exclude the tracked Threads `.db`, `.db-shm` and `.db-wal` contents as uncontrolled historical user state; cannot infer observed activity or success from them. |
| `org-server/` | Included: organization-memory storage and service | `src/app.ts`, route registration and push/pull/search implementations, `src/index.ts`, `src/db.ts`, README and `tests/roundtrip.test.ts` inspected/searched. Other tests, auth/config and deployment files remain available; no tests were run. |
| `src-tauri/` | Included: desktop shell and packaging | `src/lib.rs` and `tauri.conf.json` read; native plugins and memory-server resource mapping identified. Capabilities, build/main entry, dependency locks and icons available but not yet inspected in detail; no packaged-platform or security certification. |
| `types/` | Included: application data and API contracts | Tree identifies briefing, chart, database, index, journal, MCP, plugin, research and work-state contracts; detailed contents not yet inspected. No claim of contract/implementation consistency. |
| `public/` | Included: MCP app rendering bridge | `mcp-sandbox-proxy.html` inspected; conveys guest/host UI messages. No browser execution or isolation guarantee established. |
| `README.md` | Included: product doctrine and reported status | Read completely; declared features and alpha claims do not establish observed operation. |
| `ARCHITECTURE.md` | Included: architecture doctrine | Read completely; implementation, not documented tool counts or directory descriptions, controls executable claims. |
| `CLAUDE.md` | Included: developer-agent behavior and memory maintenance instructions | Read completely; not adopted as instructions for this analysis and not treated as an in-app prompt. |
| `claude_docs/` | Included: development context, design and reported progress | All seven files' headings/context-bearing passages scanned: `ACTIVE_CONTEXT.md`, `LLM_WIKI.md`, `PRODUCT_CONTEXT.md`, `PROGRESS.md`, `PROJECT_BRIEF.md`, `SYSTEM_PATTERNS.md`, `TECH_CONTEXT.md`. Full bodies not yet inspected; designs and code examples do not prove shipped execution. |
| `package.json` | Included: frontend development/build entry points and declared dependencies | Read; Tauri and Next scripts identified. Dependency declarations do not prove installed versions or a successful build. |
| `package-lock.json` | Included: dependency resolution metadata | Present in tracked tree, not yet inspected; no dependency-resolution audit. |
| `next.config.mjs` | Included: frontend build configuration | Present, not yet inspected; no independent static-export compatibility conclusion. |
| `postcss.config.mjs` | Included: styling build configuration | Present, not yet inspected; no styling-build conclusion. |
| `tsconfig.json` | Included: compile configuration | Present, not yet inspected; no type-check result. |
| `.mcp.json` | Included: shipped development MCP caller configuration | Read; points at `server/index.ts` through a developer-local absolute path. It does not establish deployment portability or a live external-client run. |
| `.env` | Excluded deliberately: local environment values | Contents not inspected; prevents conclusions about that local configuration, secrets or configured service availability. Does not remove source-defined provider calls from scope. |
| `.github/` | Excluded deliberately: `FUNDING.yml` project funding metadata | Tracked tree inspected; no funding-program conclusion. No tracked CI workflow identified in this directory. |
| `.vscode/` | Excluded deliberately: `settings.json` editor configuration | No editor-specific behavior or development ergonomics conclusion. |
| `.gitignore` | Excluded deliberately: repository ignore policy | No ignore-policy or secret-hygiene audit. |
| `.DS_Store` | Excluded deliberately: OS directory metadata | No Finder/user-machine history conclusion. |
| `tsconfig.tsbuildinfo` | Excluded deliberately: incremental compiler cache | No inference of a successful current build from cached state. |
| `CODE_OF_CONDUCT.md` | Excluded deliberately: community policy | No community-governance conclusion. |
| `CONTRIBUTING.md` | Excluded deliberately: contributor procedure | No contributor-workflow compliance conclusion; executable build paths are included separately. |
| `LICENSE` | Excluded deliberately: legal terms | No licensing/legal assessment. |

### External dependencies and evidence limits

The implementation delegates model generation to configured OpenAI or Anthropic clients, search to configured web/search providers including Tavily and Perplexity, and host operations to Tauri plugins and SQLite implementations. Threads Engagement additionally relies on the Threads API. External MCP servers, third-party plugins, installed external MCP clients such as Claude Code/Cursor, actual Obsidian vault files and deployment infrastructure are outside this repository evidence. Their integration code is included; their implementations, data and operation are not. Consequently this run cannot establish provider quality, external-tool policy, external-client prompt/reload behavior, successful cross-client use, external vault content correctness or live deployment reliability. SRC-1, `lib/ai/index.ts`, `lib/ai/openai.ts`, `lib/ai/anthropic.ts`, `lib/ai/perplexity.ts`, `lib/ai/web-tools.ts`, `lib/mcp/stdio-transport.ts`, `lib/mcp-auto-setup.ts`, `plugins/continuity-threads-engagement/src/index.ts`, `src-tauri/src/lib.rs`, `server/db/connection.ts`.

There is no unavailable repository source identified at this boundary. Files available but not inspected remain distinguishable from access gaps in the coverage table. No target code, tests, examples, model providers or services were executed. No supplied execution trace or controlled experiment is registered. Test definitions and source-native status claims therefore cannot establish an observed passing run, end-to-end integration success, memory usefulness, calibrated confidence, comparative performance or causal improvement. The boundary is complete as a source-defined functional scope; it is not a completed audit of every included path.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/uziiuzair/continuity` | 4ca8f6b4108aa4494e3861ed33c8019dbd662c67 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/continuity-3e490e1d39f0/related-systems/uziiuzair--continuity`. Implementation: tracked tree, frontend/layout and chat driver, shared memory writes/reloads, memory/narrative prompts and synthesis, MCP server registrations/database, vault index/callers, research caller, plugin host/SDK routing, both plugin entry points and state workflows, organization-server route entry points and roundtrip test definition, Tauri initialization/configuration. Doctrine/design: complete `README.md`, `ARCHITECTURE.md`, `CLAUDE.md`; scoped searches in `claude_docs/` and subsystem READMEs. Reported operation: README status/features and development-context status passages, attributed only. | Implementation: [desktop driver](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/providers/chat-provider.tsx), [memory persistence](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/db/memories.ts), [maintenance](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/narrative-synthesis.ts), [MCP entry](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/index.ts), [sync caller](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-org-memory-sync/src/sync-engine.ts), [Threads driver](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-threads-engagement/src/index.ts), [org service](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/org-server/src/app.ts). Doctrine/design: [workspace prompt](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/workspace-agent-prompt.ts), [developer instructions](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/CLAUDE.md), [architecture](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/ARCHITECTURE.md). Reported operation: [README status](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/README.md), [development context](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/claude_docs/ACTIVE_CONTEXT.md). | No identified repository access gap. External dependencies and deployed/client behavior are not frozen; no observed-run or causal-experiment layer. Prevents live-operation, integration-success, effectiveness and causal conclusions. Uninspected available files and deliberate exclusions are recorded above; committed bundle parity is unverified. |
