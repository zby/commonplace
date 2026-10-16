---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Tolaria runtime baseline: desktop CLI invocation, direct-provider note creation, MCP writes and guidance admission at the frozen revision."
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
reviewed-boundary: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
---

# Tolaria runtime report

## Runtime account

Tolaria supplies the knowledge-base application and invocation plumbing, not the complete runtime of its selected coding agent. Its consequential work is to supply vault context, expose retained-content operations, dispatch a selected agent or model, and show responses and file changes. The application has two materially different model paths and an independently callable MCP service. The documentation's description of direct models as universally without write tools does not match the inspected implementation; [RT-RTE-provider-create](#rt-rte-provider-create) establishes the narrower executable contract. Evidence is SRC-1 implementation and doctrine/design at the boundary's pinned commit. No supplied execution evidence establishes successful activation, safety in deployment, or benefit.

### Ordinary desktop invocation

A user sends a nonempty prompt in the AI workspace, with an active vault, ready target, permission mode and optional references. `sendAgentMessage` rejects missing vaults and unavailable targets, ignores input while thinking/tool-executing, allocates an abort controller and streaming message ID, hydrates note references, and builds the request from completed messages. `buildFormattedMessage` constructs natural-language instructions and a formatted history rather than resuming an app-managed CLI session. Local markers, reasoning and tool-action objects do not enter the history conversion: only user text and assistant response do. History trimming is code-owned, whereas interpretation and tool choice belong to the selected model/runtime ([RT-RTE-workspace-send](#rt-rte-workspace-send); SRC-1, `src/lib/aiAgentSession.ts`, `src/lib/aiAgentConversation.ts`).

For a selected Codex CLI target, the frontend installs a scoped event listener before invoking `stream_ai_agent`. The Rust command expands vault paths, runs on the blocking pool with the event name as cancellation identity, and dispatches to the Codex adapter. The adapter discovers its binary, prepares a temporary last-message file, sets the active vault as working directory, configures Tolaria MCP with active vault roots, and sends combined instructions/message through stdin to `codex exec --json`. Child stdout is parsed as JSON lines; mapped events return through the scoped Tauri channel, and process exit/stderr feed the error path. A last-message file provides a fallback if no text event arrived (SRC-1, `src/utils/streamAiAgent.ts`, `src-tauri/src/commands/ai.rs`, `src-tauri/src/ai_agents.rs`, `src-tauri/src/codex_cli.rs`, `src-tauri/src/cli_agent_runtime.rs`).

The principal initiating this work is the user; the subprocess and MCP service execute with their host processes' OS access. Tolaria's active-vault list is an application grant, not an OS isolation envelope. Codex receives sandbox/approval arguments; enforcement requires the external CLI to honor their semantics. The model owns next-step decisions within that runtime. Tolaria normalizes text, thinking and tool events but does not thereby mediate every underlying action. Successful tool events can trigger file callbacks. Completion marks the message nonstreaming, normalizes response spacing, marks remaining pending actions done, and refreshes the vault. Error callbacks preserve partial response and mark pending actions error. Neither UI action status is independent proof of a filesystem effect (SRC-1, `src/lib/aiAgentStreamCallbacks.ts`).

Session message/status updates are published through a cross-window persisted store and scheduled for native writes after 250 ms. Native reads normalize running states to idle and streaming messages to nonstreaming; failed native writes are swallowed to preserve chat usability. This is a persistence request path, not a durable-storage guarantee: the native transcript implementation and complete restart lifecycle remain uninspected here. Later request construction consumes the message array after trimming. Detailed memory revisions belong to the memory analysis (SRC-1, `src/lib/aiWorkspaceSessionStore.ts`, `src/lib/aiAgentConversation.ts`).

### Material alternate paths and forcing cases

1. **Safe Codex still reaches a writable service.** Its native sandbox argument is `read-only`, but the MCP handler map includes create, update and append. The service writes through its own Node filesystem functions. Thus native sandbox settings do not establish that Tolaria exposes a read-only knowledge base. Prompt instructions prohibit shell, not note changes. The native sandbox and MCP effect boundaries are separate ([RT-RTE-mcp-write](#rt-rte-mcp-write); SRC-1, `src-tauri/src/codex_cli.rs`, `mcp-server/index.js`, `mcp-server/tool-service.js`, `mcp-server/vault.js`).
2. **Pi does not receive an equivalent mode-dependent sandbox in the inspected command builder.** Its MCP config builder ignores permission mode, seeds from the existing agent directory, preserves base configuration while replacing the Tolaria entry, and invokes JSON mode with `--no-session`. When settings do not already load the MCP adapter, it adds an unversioned `npm:pi-mcp-adapter` extension. The builder does not disable native tools. This prevents a universal code-enforced no-shell conclusion for Vault Safe; the exact native tools and extension behavior remain external, not presumed ([RT-RTE-pi-extension](#rt-rte-pi-extension); SRC-1, `src-tauri/src/pi_config.rs`, `src-tauri/src/pi_config/package_args.rs`).
3. **Direct-provider note creation bypasses CLI controls.** An active vault plus OpenAI kind or a catalog-declared tools capability causes the OpenAI-compatible payload to advertise `create_note`. Returned tool calls execute locally, without a per-content confirmation branch in the inspected executor. The Anthropic payload does not advertise that tool. Calls run sequentially; an error can follow earlier successful writes. This is one HTTP completion followed by local tool execution and textual summaries, not an inspected iterative provider tool-result loop ([RT-RTE-provider-create](#rt-rte-provider-create); SRC-1, `src-tauri/src/ai_models.rs`, `src-tauri/src/ai_model_tools.rs`).
4. **Stop and browser behavior differ by path.** CLI Stop requests native child cancellation. Direct-model streaming receives no abort signal, and its native command uses a shared, nonregistered stream scope. Stop can suppress later UI callbacks while the HTTP request and potential note write continue. Non-Tauri agent/model dispatch instead generates timer-based mock text, not target agent work. This mock branch is not operational evidence for either real path (SRC-1, `src/lib/aiAgentSession.ts`, `src/utils/streamAiAgent.ts`, `src/utils/streamAiModel.ts`, `src-tauri/src/commands/ai.rs`).

The other CLI adapters are identified by dispatch but their complete permission implementations were not traced. Native simple Claude chat, remote web/server collaboration, editor admission, watcher/Git reconciliation and deployed bridge delivery remain included but uninspected loops, as permitted by the boundary's partial-loop designation. Source discovery adds no observed-run layer and does not expand to external CLI/provider internals. No whole-system safety or admission completeness claim follows.

### Load-bearing controls and guarantees

| Control | Owner and enforcement | Strength and covered paths | Alternate paths, external contract and limits | Conclusion statuses |
|---|---|---|---|---|
| Vault Safe shell restriction | Natural-language prompt tells the agent not to use shell; Codex adapter also chooses sandbox and approval flags | policy for prompt; protocol for Codex flags; only those consumers | Pi extension/native runtime, other adapters and direct calls require separate assessment. CLI flag semantics and prompt compliance are external contracts, not an app-wide invariant | implementation conclusion status: wired; operation conclusion status: uninspected |
| New note does not overwrite existing file | Rust `create_new(true)` and Node `open(..., 'wx')` | invariant at exclusive-create operation for provider/native create and MCP create respectively | Existing-note save/update/append are intentionally different. OS exclusive-create semantics are required; this does not promise transactional multi-call batches, complete content after write failure, or safe concurrent path mutation | implementation conclusion status: wired; operation conclusion status: uninspected |
| Vault confinement | Rust canonical candidate/root checks; MCP realpath and parent checks plus active-vault selection | protocol for inspected native/MCP path validation | Shell/native agent tools and third-party extensions do not necessarily pass these functions. Concurrent symlink changes and deployed OS isolation were not established | implementation conclusion status: wired; operation conclusion status: uninspected |
| Conflict/crash protection on MCP update | Optional mtime check followed by temp-file rename | best effort conflict detection; protocol for replacement | Omitted mtime skips the conflict gate; check and write are not a compare-and-swap. Append and native save do not use this replacement implementation. Node/filesystem rename behavior is required; fsync durability is not established | implementation conclusion status: wired; operation conclusion status: uninspected |
| CLI Stop | Scoped process registry requests `Child::kill` | best effort for registered immediate child | Does not establish killing descendants or reversing writes. `wait` holds the same child mutex needed by abort, limiting a universal prompt-stop guarantee. API models do not enter this registry | implementation conclusion status: wired; operation conclusion status: uninspected |
| Transcript retention | Frontend store schedules native writes and handles read-back | best effort | Persistence failures are hidden from chat; storage implementation and shutdown completion uninspected | implementation conclusion status: wired; operation conclusion status: uninspected |

Minimum enforcement passages for the scoped controls:

> crate::ai_agents::AiAgentPermissionMode::Safe => "read-only",
>         crate::ai_agents::AiAgentPermissionMode::PowerUser => "workspace-write",
> --- `src-tauri/src/codex_cli.rs`

> self.ensure_within_root(&canonical)?;
>         Ok(path_to_string(&requested))
> --- `src-tauri/src/commands/vault/boundary.rs`

> match stream_id {
>             Some(stream_id) => crate::ai_agent_processes::with_stream_id(stream_id, run),
>             None => run(),
>         }
> --- `src-tauri/src/commands/ai.rs`

> child
>         .kill()
>         .map_err(|error| format!("Failed to stop AI agent process: {error}"))?;
> --- `src-tauri/src/ai_agent_processes.rs`

> await invoke('save_ai_workspace_sessions', { sessions: nextSessions })
>   } catch {
>     // Transcript persistence should never interrupt the chat UI.
> --- `src/lib/aiWorkspaceSessionStore.ts`

These scoped conclusions are supported by these passages, the route passages below and SRC-1, `src-tauri/src/commands/vault/boundary.rs`, `src-tauri/src/commands/vault/file_cmds.rs`, `src-tauri/src/vault/file.rs`, `mcp-server/vault.js`, `src-tauri/src/ai_agent_processes.rs`, `src/lib/aiWorkspaceSessionStore.ts`. They concern executable wiring, not observed guarantee fulfillment.

### Change admission and coverage

Knowledge changes can be proposed by a foreground agent and executed through native tools or MCP; direct-provider `create_note` is a separate local admission mechanism. User initiation is not per-content approval. Vault instructions and product-doc prompts shape proposals but do not validate them. Application-managed guidance restoration is instead code-selected template replacement ([RT-RTE-guidance-sync](#rt-rte-guidance-sync)). Pi configuration/extension loading changes the available capability surface ([RT-RTE-pi-extension](#rt-rte-pi-extension)). Git is documented as an inspection/rollback aid, not evidence of a required pre-write approval gate (SRC-1, `site/concepts/ai.md`). Product builds, application upgrades, remote production machinery and all user editor confirmation flows were not traced; their change admission remains uninspected, not absent. No formulated-theory criticism/iteration route or improvement objective is established by these generic write paths.

Additional implementation coverage under SRC-1: history filtering/trimming; Codex invocation; Pi command/config/package arguments; native note creation and path validation; MCP filesystem create/update/append; child cancellation; frontend completion and session-store persistence requests; managed guidance synchronization. Documentation coverage adds the AI concept page. This extends initial inspection at the same commit, not the evidence boundary. Selected source branches, not target execution or tests, provide the forcing cases.

## Shared records

### Components

#### RT-CMP-cli-model
Label: Selected CLI agent model

Source-native identity: the model selected by the installed CLI, optionally overridden by Tolaria's model string. Representational form: distributed-parametric model state. Storage substrate: external provider/local runtime, opaque to Tolaria. Parameters changing during operation: uninspected; Tolaria's inspected dispatch does not update weights. Exact version pinned: not established by an optional model string or default. A mutable endpoint/default can resolve to another model; resolution and provider internals remain uninspected. Distinct from direct-model configuration because the CLI owns authentication, tools and runtime. Evidence: SRC-1, `src-tauri/src/ai_agents.rs`, `src-tauri/src/codex_cli.rs`, `site/concepts/ai.md`.

> Each agent still owns its authentication, available tools, and runtime behavior.
> --- `site/concepts/ai.md`

#### RT-CMP-api-model
Label: Direct model target

Source-native identity: `AiModelStreamRequest` provider and `model_id`. Representational form: distributed-parametric model behind the endpoint, distinct from the symbolic request configuration. Storage substrate: remote or local model service. Parameters changing during operation: uninspected; inspected application code sends inference requests, not parameter updates. Exact version pinned: not established; configured IDs are not immutable weight revisions. Mutable configured base URLs and provider-side ID resolution can reach another model. Evidence: SRC-1, `src-tauri/src/ai_models.rs`, `src/utils/streamAiModel.ts`.

> let endpoint = format!("{}/chat/completions", normalized_base_url(request)?);
> --- `src-tauri/src/ai_models.rs`

### Operative objects

#### RT-OBJ-agent-prompt
Label: Agent system prompt

Source-native identity: `buildAgentSystemPrompt` result. Representational form: natural-language behavioral instructions interpreted by an agent/model. Storage substrate: shipped TypeScript string literals assembled into the current request; referenced vault `AGENTS.md` and bundled docs are separate files. Includes vault scope, safe/power-user instructions, preferred edit/MCP use, product-document guidance and optional vault context. Delivery is not compliance. Evidence: SRC-1, `src/utils/ai-agent.ts`.

> Prefer file edit tools for note changes.
> Use the provided MCP tools for: full-text search (search_notes), vault orientation (get_vault_context), parsed note reading (get_note), and opening notes in the UI (open_note).
> Use create_note(path, content, vaultPath?) for new Markdown notes when shell writes are unavailable.
> --- `src/utils/ai-agent.ts`

#### RT-OBJ-stream-request
Label: Agent stream request

Source-native identity: `AiAgentStreamRequest`. Representational form: symbolic typed/serialized fields consumed by deterministic dispatch; message/system-prompt bodies are natural-language payloads represented separately by [RT-OBJ-agent-prompt](#rt-obj-agent-prompt). Storage substrate: frontend memory and native IPC request, then subprocess arguments/stdin and environment. Agent, model, vault roots, permission mode and event identity determine dispatch/control. Evidence: SRC-1, `src/utils/streamAiAgent.ts`, `src-tauri/src/ai_agents.rs`.

### Routes

#### RT-RTE-workspace-send
Label: Workspace CLI invocation

User prompt → frontend context/history builder → scoped Tauri command → adapter/subprocess → normalized events → response/store updates. User chooses target and starts work; code decides eligibility and context filtering; external foreground model proposes actions and decides tool steps, subject to its runtime controls. Uses [RT-CMP-cli-model](#rt-cmp-cli-model) and [RT-OBJ-agent-prompt](#rt-obj-agent-prompt). Ordinary open requests; no expected-answer oracle is used by this path. Regenerate discards messages from the chosen point and resends that prompt; it is not filesystem rollback. Evidence: SRC-1, `src/lib/aiAgentSession.ts`, `src/lib/aiAgentConversation.ts`, `src/utils/ai-chat.ts`, `src/utils/streamAiAgent.ts`, `src-tauri/src/codex_cli.rs`, `src-tauri/src/cli_agent_runtime.rs`, `src/lib/aiAgentStreamCallbacks.ts`, `src/lib/aiWorkspaceSessionStore.ts`.

- Immediate return: streamed text/thinking/tool events and a finalized UI message, or partial response with error.
- Later read-back: message arrays are persisted by frontend/native write requests and converted to trimmed user/assistant history on later sends; native durable implementation is uninspected.
- Delegated visibility: CLI receives assembled instructions and current prompt/history; Codex MCP receives active vault roots. Tool actions/reasoning are omitted by app history conversion.
- Selection predicate: nonempty prompt, ready target, active vault, no concurrent thinking/tool-executing status; history includes completed nonmarker messages then a newest fitting suffix.
- Invalidation or expiry: clear empties messages; regenerate removes the chosen suffix; history trimming stops at the first newest-to-oldest message exceeding its approximate budget, without deleting the store.
- Activation or effect: request delivery and callback mutations are wired; underlying tool decisions and successful changes remain unobserved.
- Evidence limits: installed CLI semantics, native persistence durability, real runs and all adapter permission variants are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const chatHistory = toChatHistory(messages.filter((message) => !message.isStreaming))
> const trimmedHistory = trimHistory(chatHistory, MAX_HISTORY_TOKENS)
> --- `src/lib/aiAgentConversation.ts`

> for (const message of newestFirst) {
>     const tokens = estimateTokens(message.content)
>     if (tokenCount + tokens > maxTokens) break
>     keptNewestFirst.push(message)
>     tokenCount += tokens
>   }
> --- `src/utils/ai-chat.ts`

This is code-owned window control: old turns stay outside the next request, a verbatim suffix remains, and no summary is produced by this function. Its 100,000-token estimate uses characters/4 and does not bound system prompt, references, latest prompt or the external runtime's complete window. Excluded earlier turns remain in the message store; an automatic reload of omitted turns is not established here (SRC-1, `src/utils/ai-chat.ts`).

#### RT-RTE-provider-create
Label: Direct-provider create-note execution

Frontend API target → native HTTP completion → returned tool-call parser → `create_note_content_blocking` → filesystem exclusive create → textual summary/tool events. Uses [RT-CMP-api-model](#rt-cmp-api-model). The human starts an open request; the provider model proposes path/content; Tolaria decides supported tool and target vault and delegates path checks to native commands. No per-content approval or expected-answer oracle occurs in this inspected executor. Empty content falls back to title/type Markdown. Rejection includes unsupported function, invalid arguments, inactive requested root, boundary failure and existing file. Earlier writes in a multi-call response are not rolled back when a subsequent call fails. Guidance comes from the same assembled system prompt and function description; resulting Markdown persists, not a demonstrated improvement. Evidence: SRC-1, `src/lib/aiAgentSession.ts`, `src-tauri/src/ai_models.rs`, `src-tauri/src/ai_model_tools.rs`, `src-tauri/src/commands/vault/file_cmds.rs`, `src-tauri/src/commands/vault/boundary.rs`, `src-tauri/src/vault/file.rs`.

- Immediate return: create-note tool events and joined creation summaries, or error; ordinary provider text when no calls occur.
- Later read-back: created note is available to later vault/file readers; this executor does not feed tool output back into a second model request.
- Delegated visibility: provider receives assembled request text/system prompt and optional tool schema, not automatic access to all vault files.
- Selection predicate: frontend API-model target; OpenAI-compatible tool advertising requires active vault and OpenAI kind or configured tool support. Anthropic uses a different payload.
- Invalidation or expiry: provider configuration/model ID can change; written file survives request; no automatic expiry or batch rollback in inspected path.
- Activation or effect: host executes parsed create-note requests without CLI permission mode mediation; actual writes in deployed use unobserved.
- Evidence limits: provider reliability, content quality, path-race protection and actual cancellation are not demonstrated. UI Stop does not pass an abort signal here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if let Some(tool_summary) =
>         crate::ai_model_tools::execute_openai_tool_calls(request, &json, emit)?
>     {
>         return Ok(tool_summary);
>     }
> --- `src-tauri/src/ai_models.rs`

> let has_active_vault = non_empty_option(request.vault_path.as_deref()).is_some();
>     has_active_vault
>         && (request.provider.kind == AiModelProviderKind::OpenAi
>             || selected_model_supports_tools(request))
> --- `src-tauri/src/ai_model_tools.rs`

> let mut file = fs::OpenOptions::new()
>         .write(true)
>         .create_new(true)
>         .open(file_path)
> --- `src-tauri/src/vault/file.rs`

#### RT-RTE-mcp-write
Label: MCP retained-note writes

External/app-managed MCP caller → registered tool handler → active-vault selection → create/update/append filesystem operation → UI actions and tool result. Service code owns path resolution and physical I/O; caller/its model proposes content. Open requests, no expected-answer oracle. `update_note` admits full replacement; `append_to_note` admits an extension; create rejects existing file. Starting a client session is not human approval of each content change. No review branch in the inspected service requires a person to authorize returned content before write. Caller guidance/compliance is external; app-managed prompts request file edits and UI opening. Recovery exposes errors to the caller; update uses temp-file cleanup/rename and an optional conflict guard; transactional append or multi-call rollback is not established. Evidence: SRC-1, `mcp-server/index.js`, `mcp-server/tool-service.js`, `mcp-server/vault.js`.

- Immediate return: path/vault metadata, update/append mtime, and refresh/open UI action emission; exceptions become MCP error content.
- Later read-back: file content reaches subsequent `get_note`, search and vault consumers; inspected get-note parses frontmatter and trims body, not a verbatim raw-file return.
- Delegated visibility: requested note content/metadata or search results reach the MCP caller; live bridge/UI delivery is unobserved.
- Selection predicate: tool name and explicit path, optional requested active vault; ambiguous multiple-vault reads/writes require disambiguation. Write authorization uses active roots, not model semantic quality.
- Invalidation or expiry: edits replace/extend files; optional expectedMtime rejects stale update; later file reads see current content. No automatic expiry in this route.
- Activation or effect: retained-file changes and UI emission are wired; model compliance and downstream behavioral change unobserved.
- Evidence limits: no execution supplied; native agent tools and shell do not necessarily pass this service; concurrent update check/write races and production bridge delivery remain unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (expectedMtime === undefined || expectedMtime === null) return
>   if (stat.mtimeMs === expectedMtime) return
> --- `mcp-server/vault.js`

> await writeFile(tempPath, content, { encoding: 'utf-8', flag: 'wx' })
>     await rename(tempPath, filePath)
> --- `mcp-server/vault.js`

#### RT-RTE-pi-extension
Label: Pi capability configuration

Tolaria Pi command preparation → seed app agent directory from existing configuration → install Tolaria MCP configuration → choose package arguments → external Pi CLI. Deterministic code decides whether settings already load the adapter; otherwise it proposes the unversioned npm extension. Human package provenance and actual dependency admission are external/uninspected; no per-package confirmation is visible in the inspected builder. This is capability supply during an open request, not an improvement experiment; no answer oracle. Rejection includes config parse or filesystem errors. No rollback is established for configuration writes if launch fails. Evidence: SRC-1, `src-tauri/src/pi_config.rs`, `src-tauri/src/pi_config/package_args.rs`.

- Immediate return: subprocess command using JSON mode, no-session option, app agent directory and Tolaria MCP entry; external loading outcome unobserved.
- Later read-back: written MCP configuration and seeded settings can be consumed by later invocations; external package caching/version resolution uninspected.
- Delegated visibility: Pi receives combined prompt, active-vault environment and its app agent directory; installed extensions can participate in its runtime outside Tolaria's normalized event boundary.
- Selection predicate: Pi target; adapter argument added unless app or vault settings declare it with extensions enabled.
- Invalidation or expiry: Tolaria MCP entry replaced during command preparation; settings and external package versions may change; no pinned npm version in injected argument.
- Activation or effect: capability/configuration supply wired; loaded extension behavior and actual grant/isolation envelope unobserved.
- Evidence limits: MCP configuration uses the same builder regardless of permission mode; no universal no-shell enforcement follows. Pi/runtime/package internals excluded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const PI_MCP_ADAPTER_EXTENSION: &str = "npm:pi-mcp-adapter";
> --- `src-tauri/src/pi_config/package_args.rs`

> let mut args = vec!["--mode".into(), "json".into(), "--no-session".into()];
> --- `src-tauri/src/pi_config/package_args.rs`

#### RT-RTE-guidance-sync
Label: Managed vault guidance synchronization

Seed/restore operation → code examines existing root guidance → replacement predicate → shipped `AGENTS_MD` and compatibility shims written to vault. Code proposes defaults and decides admission; existing custom content can veto replacement by failing the managed-template/empty/stub predicate, rather than by an interactive human review. Open maintenance mode, not experiment/curriculum; no answer oracle. Rejection is preservation of unrecognized custom content or I/O error. No backup/transactional rollback was established. Migration additionally copies eligible legacy guidance to root and removes the legacy file; that removal does not by itself prove no user-content loss in every case. Evidence: SRC-1, `src-tauri/src/vault/config_seed.rs`.

- Immediate return: restoration status or seed log; errors propagate from restoration while seed reduces sync error to false.
- Later read-back: root guidance files persist and the agent prompt asks future agents to read AGENTS.md; actual obedience unobserved.
- Delegated visibility: root instructions are file-accessible; prompt delivery of their entire content is not established by synchronization alone.
- Selection predicate: missing, empty, legacy pointer or known managed template for root agents; recognized managed shims for compatibility files.
- Invalidation or expiry: replacement/restore refreshes managed files; custom content preserved by predicate; no automatic expiry established.
- Activation or effect: code changes retained instruction files; resulting changes in later agent decisions unobserved.
- Evidence limits: shipped template theory content and complete migration lifecycle not assessed here; synchronization is not evidence-responsive theory criticism or improved future capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fn agents_content_can_be_replaced(content: &str) -> bool {
>     content.trim().is_empty()
>         || content.contains("See config/agents.md")
>         || agents_content_is_known_managed_template(content)
> }
> --- `src-tauri/src/vault/config_seed.rs`

### Claims

#### RT-CLM-direct-chat
Label: Direct-model chat-only claim

Claimed operation: direct models receive note context/history but no vault-write tools or shell. SRC-1 doctrine/design, `site/concepts/ai.md`. The no-write-tools part is contradicted for the OpenAI-compatible create-note branch by [RT-RTE-provider-create](#rt-rte-provider-create); this does not establish shell access on that branch.

> Direct model targets run in chat mode. They receive the active note, linked context, and conversation history, but they do not receive vault-write tools or shell access.
> --- `site/concepts/ai.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-policy
Label: Agent prompt policy authority

Consumer: selected foreground CLI agent or direct provider. Channel: system-prompt/combined prompt text assembled by Tolaria. Force: interpretive policy, not an OS permission boundary. Horizon: current request, with repeated static guidance on later sends. Referent is prompt delivery and instruction force, distinct from physical write authority. SRC-1, `src/utils/ai-agent.ts`, `src/lib/aiAgentConversation.ts`, `src-tauri/src/codex_cli.rs`, `src-tauri/src/ai_model_tools.rs`; supported passage in [RT-OBJ-agent-prompt](#rt-obj-agent-prompt).

#### RT-BAP-tool-executor
Label: Local tool execution authority

Consumer: native create-note executor or Node MCP filesystem service. Channel: symbolic tool name/arguments and active-vault configuration. Force: executable local file I/O after path/tool checks, not semantic approval. Horizon: request effects can persist across later sessions as files; actual downstream behavior remains unobserved. Direct-provider and MCP admission mechanisms are kept separate in [RT-RTE-provider-create](#rt-rte-provider-create) and [RT-RTE-mcp-write](#rt-rte-mcp-write). SRC-1, `src-tauri/src/ai_model_tools.rs`, `mcp-server/tool-service.js`, `mcp-server/vault.js`.

## Annotations

none
