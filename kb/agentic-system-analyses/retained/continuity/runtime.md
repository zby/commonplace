---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Continuity runtime baseline: desktop conversation, isolated research, memory admission, plugin capability controls and Threads publication at the frozen source revision."
run-id: AAS-2026-10-14-continuity-3e490e1d39f0-01
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
---

# Continuity runtime report

## Runtime account

Continuity owns a desktop model/tool loop and several independently driven state-changing services. This account uses SRC-1 implementation and shipped prompts at the boundary revision. No supplied execution trace or experiment establishes operation, model compliance, activation of retained guidance, or benefit. The boundary's source register remains authoritative. Additional inspection covers provider request construction, plugin registration/authentication/SQL handlers, native grants, Threads scheduling/publication, organization push admission and SDK database routing; these are implementation evidence, not runs.

### Ordinary desktop invocation

A user sends text to the active thread. The React chat provider rejects overlapping/empty sends, creates a thread if needed, saves the user message in Tauri mode, obtains configured credentials/provider/model, and constructs one fresh system prompt. Without configured AI it saves a configuration instruction instead of making a model call. History enters as role/content messages, not by replaying previous tool-call protocol records. The current user message is appended separately. SRC-1, `providers/chat-provider.tsx`.

The system message combines shipped personality and workspace guidance, user profile/custom instructions, current narrative and passive memories, tool instructions, and optional vault context. Canvas tools are selected per message rather than always loaded. Failed profile, memory, narrative or vault loading is noncritical and can silently omit that context. This is best-effort context delivery, not a complete-context invariant. Plugin-tool descriptions have a frontend consumer, but the separate host prompt registration does not itself prove arrival here; see [RT-RTE-plugin-admission](#rt-rte-plugin-admission). SRC-1, `providers/chat-provider.tsx`, `lib/ai/plugin-tools.ts`.

The configured remote model chooses textual output and tool calls under automatic tool choice. Code owns the next-step loop and executor dispatch. Tool IDs correlate returned role-tool messages with model calls; the thread ID scopes canvas work; memory tools can write global state instead. Dispatch is sequential within a response. Canvas/database changes refresh the UI; web, memory, vault, MCP and plugin calls reach their respective executors. Malformed argument JSON is logged and replaced with an empty object before dispatch. Tool results return to the next model invocation; unknown tools return a failure message. See [RT-RTE-desktop-chat](#rt-rte-desktop-chat), [RT-RTE-memory-admission](#rt-rte-memory-admission) and [RT-CMP-ai-client](#rt-cmp-ai-client). SRC-1, `providers/chat-provider.tsx`.

The desktop provider has a ten-iteration bound on its outer model/tool loop. This is a local code invariant, owned by `ChatProvider`, not a bound on total tool effects, model calls throughout the system, wall-clock duration or provider cost. One response may contain several tool calls. Research launches an independent workflow; synthesis and Threads make direct calls outside this loop. Required external contracts include provider response/tool-call compatibility and eventual completion of awaited operations. A hung operation is not terminated by the iteration counter. On a tool-producing tenth round, results execute and `finalContent` is cleared without a guaranteed final answer round. Final nonempty assistant content is saved with model/token/tool display metadata, and a debounced synthesis check is scheduled; exhausting the bound can therefore leave effects without a saved final assistant answer. SRC-1, `providers/chat-provider.tsx`.

> const MAX_TOOL_ITERATIONS = 10; // Safety limit
> --- `providers/chat-provider.tsx`

> // Add tool results to messages
> currentMessages.push(...toolResults);
>
> // Clear the streamed content for next iteration
> // Show thinking in a collapsed block instead of clearing entirely
> finalContent = "";
> --- `providers/chat-provider.tsx`

For this guarantee: guarantee strength: invariant; implementation conclusion status: wired; operation conclusion status: uninspected. Exceptions become an error UI message and reset activity state; already performed writes are not rolled back by the chat catch. Streaming, accumulated tool displays and provider/token metadata improve visibility but do not certify tool success: the display derives success partly from text prefixes. SRC-1, `providers/chat-provider.tsx`.

### Forcing routes and control boundaries

Four forcing cases challenge a single-loop or single-policy account:

1. **Independent research calls:** `deep_research` returns an initiation result immediately, while planner, parallel source analysts, gap reviewer and synthesizer continue outside the ten-round chat counter. Each analyst receives a fresh context rather than the foreground history. Selected source text is truncated to 2,000 characters per source; findings are further abbreviated for gap checking and synthesis. Findings/results escape the isolated contexts, not their full message windows. Cancellation is cooperative. Report-to-canvas and summary-to-message writes occur in completion callbacks, separate from ordinary chat completion. This is a useful stack-frame comparison for isolated windows and returned findings, but no literal references or liveness tracking connect the remote windows. See [RT-RTE-deep-research](#rt-rte-deep-research). SRC-1, `lib/ai/research-engine.ts`, `providers/chat-provider.tsx`.
2. **Independent retention and maintenance:** the external stdio MCP memory service directly admits structured calls to memory CRUD and narrative/learning tools. Desktop `remember` dispatches directly to persistence; narrative synthesis makes a tool-free model call and automatically saves the result, including a raw-response fallback after JSON parse failure. The chat tool loop is neither a human approval boundary nor a universal maintenance scheduler. See [RT-RTE-memory-admission](#rt-rte-memory-admission). SRC-1, `server/index.ts`, `server/tools/memory-tools.ts`, `lib/ai/memory-tools.ts`, `lib/ai/narrative-synthesis.ts`.
3. **Plugin RPC versus process authority:** host handlers check declared capabilities, but registration takes the capability list from the authenticated caller itself. A host token is shared with spawned plugins; the plugin ID is supplied in the connection URL. Native launch grants allow interpreters with arbitrary arguments. These checks do not establish per-plugin least privilege or an OS sandbox. Moreover frontend tools/prompts remain separate from host session registrations. See [RT-RTE-plugin-admission](#rt-rte-plugin-admission) and [RT-CLM-plugin-controls](#rt-clm-plugin-controls). SRC-1, `plugin-host/src/index.ts`, `plugin-host/src/server.ts`, `src-tauri/capabilities/default.json`, `lib/plugins/manager.ts`.
4. **Threads publication:** the scheduler searches, scores, stores qualifying posts and drafts; it does not call `postReply`. The review HTTP endpoint does. This separates draft admission from external publication, but the endpoint's existence/name does not enforce that the caller is a human reviewer or that the post already has approved status. In the bounded search of `plugins/continuity-threads-engagement/src`, `postReply` has one production caller, in the approval endpoint, plus its wrapper definition. See [RT-RTE-threads-engagement](#rt-rte-threads-engagement). SRC-1, `plugins/continuity-threads-engagement/src/cron.ts`, `plugins/continuity-threads-engagement/src/ui-server.ts`, `plugins/continuity-threads-engagement/src/threads-api.ts`.

Provider adapters serialize function tools and return model-requested calls to the desktop executor; the inspected request bodies do not request provider-native hosted execution tools. External MCP subprocesses, enabled plugin code and independent SDK model workflows nevertheless expand effects beyond built-in function dispatch. The current live grant set, installed MCP servers, enabled plugins, API availability and OS/deployment containment are unobserved. The source-defined native envelope permits broad HTTPS requests, interpreter launch and home-directory filesystem access; it must not be described as deployed isolation. SRC-1, `lib/ai/openai.ts`, `lib/ai/anthropic.ts`, `lib/mcp/stdio-transport.ts`, `lib/ai/mcp-tools.ts`, `src-tauri/capabilities/default.json`.

### Change admission and retained consequences

Knowledge admission includes model-selected desktop memory writes, caller-selected MCP mutations and model-generated narrative replacement. UI and memory maintenance specifics remain for the memory analyst; these runtime facts establish the admission owners, not quality or memory revisions. Capability/production-process admission includes installing a validated manifest and enabling its sidecar, persisted in the app database; disabling kills the child but is not a rollback of external or database effects. Threads draft selection/publication has a distinct HTTP admission point. Organization memory ingestion has authenticated schema validation and timestamp-based server upsert, but the shipped SDK pull path omits a database target and therefore reaches the host's default app database, not automatically memory.db. See [RT-RTE-org-ingestion](#rt-rte-org-ingestion). SRC-1, `lib/plugins/manager.ts`, `lib/ai/memory-tools.ts`, `lib/ai/narrative-synthesis.ts`, `org-server/src/routes/memories-push.ts`, `plugin-sdk/src/db.ts`, `plugin-host/src/handlers/db.ts`.

Shipped prompts shape proposals in natural language; code controls actual admission and I/O. Starting a workflow is not per-content human approval. No answer oracle is supplied by the inspected research, narrative or Threads model judgment: source material, persona and model scores are inputs, not reference answers with validated outcomes. Model weights and provider internals are not locally writable through these routes. No learning, reflective theory-building or exercised self-improvement claim follows merely from these writes. This account does not classify the narrative as a formulated theory or judge memory transformations; those require their own content and consumer evidence.

Source/bundle equivalence for committed server, SDK and plugin-host distributions remains unverified. The manager prefers packaged host/entry files when present and only falls back to TypeScript sources in development. Source-grounded wiring here therefore does not establish behavior of a particular installed desktop build. SRC-1, `lib/plugins/manager.ts`, `server/bin/cli.mjs`.

## Shared records

### Components

#### RT-CMP-ai-client
Label: Desktop AIClient provider models

The source-native `AIClient` is instantiated as `OpenAIClient` or `AnthropicClient` from persisted provider, API key and model settings. Its operative model computation is distributed-parametric, remote at OpenAI/Anthropic endpoints; local request serialization is symbolic TypeScript. Provider weights/storage are inaccessible. The same client interface supplies chat, research and narrative calls. SRC-1, `lib/ai/index.ts`, `lib/ai/openai.ts`, `lib/ai/anthropic.ts`.

- Parameters change during operation: uninspected — no local weight-update request is implemented in these inspected adapters; provider internals are outside the frozen source.
- Exact version pinned: no — configuration supplies a model string, not a verified immutable weight revision.
- Mutable endpoint can resolve to another model: uninspected — settings can change the selected model, and the source supplies no immutable backend-resolution contract.

> case "openai":
>   return new OpenAIClient({
>     apiKey: config.apiKey,
>     model: config.model,
>   });
> --- `lib/ai/index.ts`

#### RT-CMP-ai-evaluator
Label: Threads AIEvaluator models

`AIEvaluator` constructs independent OpenAI/Anthropic SDK clients from provider/model/API-key configuration and uses persona/keywords as textual guidance. Remote model computation is distributed-parametric; the class and parsed scores are symbolic, and persona/draft text is natural-language material. Local storage holds settings and plugin results, not model weights. SRC-1, `plugins/continuity-threads-engagement/src/ai-evaluator.ts`.

- Parameters change during operation: uninspected — the class invokes inference, not training; inaccessible provider internals prevent a weight-fixity conclusion.
- Exact version pinned: no — the caller supplies a model string without a weight revision.
- Mutable endpoint can resolve to another model: uninspected — no immutable endpoint-resolution contract is in this source.

> const response = await this.openai.chat.completions.create({
>   model: this.model,
>   messages: [
>     { role: "system", content: systemPrompt },
>     { role: "user", content: userMessage },
>   ],
>   temperature: 0.7,
> });
> --- `plugins/continuity-threads-engagement/src/ai-evaluator.ts`

### Operative objects

#### RT-OBJ-current-messages
Label: Desktop currentMessages working context

`currentMessages` is an in-memory JavaScript array of symbolic role/content/tool identifiers carrying separately interpreted natural-language system/history/tool content. The foreground loop accumulates assistant call records and returned tool messages. The initial system prompt is rebuilt per user send; saved conversation content reaches a later send, while current-run protocol entries are not simply replayed as those same structures. SRC-1, `providers/chat-provider.tsx`.

> let currentMessages = [...aiMessages];
> --- `providers/chat-provider.tsx`

#### RT-OBJ-plugin-session
Label: PluginSession authority state

Host WebSocket sessions store symbolic caller-supplied plugin IDs, capability strings, registered tool maps, prompt registrations and pending calls in Node.js memory. Prompt content is a natural-language operative part stored inside this symbolic container. It is not identical to frontend manager state; host session registration does not populate that state's tool/prompt arrays in the inspected implementation. SRC-1, `plugin-host/src/server.ts`, `plugin-host/src/index.ts`, `lib/plugins/manager.ts`.

> capabilities: [],
> subscribedEvents: new Set(),
> subscribedTables: new Map(),
> registeredTools: new Map(),
> registeredPanels: new Map(),
> injectedPrompts: new Map(),
> pendingToolCalls: new Map(),
> --- `plugin-host/src/server.ts`

### Routes

#### RT-RTE-desktop-chat
Label: User send through streaming tool execution and saved answer

Owner/principal: foreground user initiates; `ChatProvider` owns progression; remote model proposes calls; code dispatches and admits effects. Thread and tool-call IDs coordinate current work. The model decides under natural-language guidance plus symbolic tool schemas; code decides tool availability and the outer bound. SRC-1, `providers/chat-provider.tsx`, `lib/ai/openai.ts`, `lib/ai/anthropic.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed assistant content, tool displays, or an error/configuration message in the UI; awaited tool results enter subsequent calls.
- Later read-back: saved user/assistant content is loaded for later thread sends; passive retained context is rebuilt in the system prompt.
- Delegated visibility: provider receives constructed system/history/current messages and schemas; executors receive their arguments, with thread ID supplied to canvas execution.
- Selection predicate: code conditionally includes canvas tools; model chooses calls; dispatch uses known tool names/prefixes and available MCP names.
- Invalidation or expiry: currentMessages lasts for this send; no chat-history trimming is shown in this construction; per-send prompt reconstruction refreshes injected content.
- Activation or effect: implemented dispatch can alter canvas/database, memory, vault or external tool state; behavior depending on delivered guidance is unobserved.
- Evidence limits: source wiring only; installed tools, provider completion and live grant set are unknown.

Operating mode: open conversation with a bounded local continuation loop. Answer oracle: none supplied. Human supplies problems and settings, not approval of each returned tool call. The catch reports failure but does not compensate completed writes.

> const chatOptions: ChatOptions = {
>   tools: getAllToolsForAI(includeCanvas),
>   toolChoice: "auto",
> };
> --- `providers/chat-provider.tsx`

#### RT-RTE-deep-research
Label: Asynchronous isolated research pipeline

Trigger: model calls `deep_research` (explicit research action hints the same tool). Desktop code validates configured search/client availability and starts `runResearch`; research code owns planning, parallel execution, gap rounds and synthesis. Model generates subquestions/findings and proposes follow-ups; code caps agents/rounds, selects top search sources and truncates source/findings text. Tool schemas from the foreground are not passed to these plain `chat` calls. SRC-1, `providers/chat-provider.tsx`, `lib/ai/research-engine.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initiation text to foreground; progress callbacks update a separate research panel while work continues.
- Later read-back: completion appends report blocks to canvas and saves a chat summary; later history receives summary rather than all analyst contexts.
- Delegated visibility: each analyst receives its subquestion and selected source excerpts in a fresh two-message context; reviewer/synthesizer receive abbreviated accumulated findings and metadata.
- Selection predicate: model plan and gap decisions, code agent/round caps, source-order slicing and configured sources-per-agent limit.
- Invalidation or expiry: thread change/user cancellation sets a cooperative cancellation flag; isolated call windows do not become foreground turns.
- Activation or effect: implemented completion callbacks write a report/summary; factual completeness, citation correctness and useful behavior remain unobserved.
- Evidence limits: no run; provider/search/source access is external; counter limits are not wall-clock/cost guarantees.

Operating mode: bounded open web investigation, not an experiment with known answers. Answer oracle: none supplied. Proposed work products are admitted automatically by completion callbacks, not reviewed per content. Cancellation/error callbacks and partial-result fallbacks recover limited output; canvas failure is logged without rolling back other writes. Guidance asks factual, balanced reports and citations; report/summary persists, not the analyst windows. Gap checking requests adequacy/follow-ups, not demonstrated theory criticism or a changed research method.

> const messages: ChatMessage[] = [
>   { role: "system", content: SUB_AGENT_ANALYZER_PROMPT },
>   {
>     role: "user",
>     content: `Sub-question: ${subQuestion.question}\n\nSource content:\n${sourceContext}`,
>   },
> ];
> --- `lib/ai/research-engine.ts`

#### RT-RTE-memory-admission
Label: Desktop and MCP knowledge admission with independent synthesis

Runtime container for distinct entry mechanisms: desktop `remember` calls `setMemory`; external stdio MCP callers invoke typed CRUD callbacks; desktop synthesis directly calls the configured model and saves narrative content. These are not the same producer or approval gate. Code owns persistence; model/caller proposes content. Detailed memory object identities/revisions belong to the memory member. SRC-1, `lib/ai/memory-tools.ts`, `server/index.ts`, `server/tools/memory-tools.ts`, `lib/ai/narrative-synthesis.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: desktop remembered-text/tool errors, MCP text/JSON responses, or synthesis boolean/error handling.
- Later read-back: memory context and narrative content can enter later desktop system prompts; MCP readers can request stored records.
- Delegated visibility: synthesis receives memories, unabsorbed learnings and previous narrative in a dedicated model context, not full chat history; MCP caller receives requested results.
- Selection predicate: model tool choice or explicit MCP requests; scheduled synthesis uses memory presence, narrative presence/staleness and learning counts, then a snapshot-change check.
- Invalidation or expiry: key/version mutations and archival alter later selection; synthesis replaces narrative fields and marks input learnings absorbed.
- Activation or effect: automatic writes can change future model-visible guidance; delivery is wired, reliable compliance/benefit unobserved.
- Evidence limits: this record establishes runtime admission, not complete memory semantics, integration success or quality of generated understanding.

Operating modes: open conversational/caller writes and scheduled/manual synthesis. Answer oracle: none supplied. Desktop `remember` checks nonempty key/value, normalizes the key and stores global content without per-item human confirmation. MCP schemas constrain fields, not truth. Synthesis parses JSON but admits raw response text as a fallback; no human veto or semantic quality gate is shown in that save path. Guidance requests structured evolving understanding; resulting narrative persists. Recovery/rollback differs by mechanism: archive/version APIs exist, whereas synthesis updates the current row; the chat exception does not restore previous knowledge. SRC-1, those paths.

> await setMemory(normalizedKey, args.value.trim(), "global", memoryType, args.tags);
> --- `lib/ai/memory-tools.ts`

> // If parsing fails, create a minimal narrative from the raw response
> result = {
>   content: response.content.slice(0, 2000),
> --- `lib/ai/narrative-synthesis.ts`

#### RT-RTE-plugin-admission
Label: Plugin installation, sidecar launch and host registration

Trigger/principal: user-facing manager install/enable calls validate a manifest, persist plugin metadata/settings and spawn its entry. Host registration is a separate token-authenticated RPC mechanism; a caller proposes capabilities, tools and prompts, and handlers admit them into session maps. Enabling a plugin is not per-effect approval. SRC-1, `lib/plugins/manager.ts`, `plugin-host/src/index.ts`, `plugin-host/src/server.ts`, `plugin-host/src/handlers/chat.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plugin installation metadata, sidecar status and host RPC acknowledgments; manual frontend forwarding helper can return tool results or timeout errors.
- Later read-back: persisted plugin enable/settings metadata is reloaded on initialization; host tool/prompt maps are session state, not durable knowledge. In the inspected manager, frontend tool/prompt arrays are not populated from registration.
- Delegated visibility: spawned code receives shared host token, plugin ID and settings via environment; tool execution forwarding passes selected tool arguments to target session.
- Selection predicate: installed/enabled plugin metadata determines startup; host token permits connection; caller-provided capability strings gate selected handlers.
- Invalidation or expiry: disable/stop kills sidecar; disconnect removes session and rejects pending calls; effects already performed are not undone.
- Activation or effect: process launch and host APIs are wired; automatic discovery/delivery of registered plugin tools and injected prompts into desktop AI is not established by these paths.
- Evidence limits: source/bundle parity and actual launch are unobserved; no deployed OS isolation or trusted per-plugin grant assignment is established.

Admission guidance: manifest schema/runtime entry determines permitted launch construction; plugin-defined tool descriptions and prompts can shape proposals at consumers that actually receive them. Code rejects invalid manifests/duplicate IDs and missing host credentials; user can disable/uninstall. No model-selected product-code revision occurs here: externally supplied entry code is admitted. Host handshake itself copies the caller's capabilities; it does not independently authorize the manifest's requested grant set. Tool handler checks and raw Node/plugin operations are materially different paths. See [RT-CLM-plugin-controls](#rt-clm-plugin-controls).

> const capabilities = params.capabilities as string[];
> if (Array.isArray(capabilities)) {
>   session.capabilities = capabilities;
> }
> --- `plugin-host/src/index.ts`

Frontend delivery qualification is based on the complete `lib/plugins/manager.ts` and `lib/ai/plugin-tools.ts` inspection: arrays initialize empty; `getState` returns them; stdout handling accepts startup/state/notification/badge/MCP-control messages, not tool/prompt registration population. The helper builds text from `state.tools`, not `state.prompts`. Host-side registration therefore cannot be equated with foreground model visibility.

> private tools: RegisteredTool[] = [];
> private prompts: RegisteredPrompt[] = [];
> --- `lib/plugins/manager.ts`

#### RT-RTE-threads-engagement
Label: Scheduled model scoring and drafts through publication endpoint

Owner: `CronScheduler` serializes scans with `isScanning`; keyword/search budgets and stored-post deduplication constrain work. `AIEvaluator` proposes scores and drafts under persona guidance; code admits posts exceeding configured relevance threshold and persists drafts in plugin SQLite. Review HTTP requests own draft selection/regeneration/publication. SRC-1, `plugins/continuity-threads-engagement/src/cron.ts`, `plugins/continuity-threads-engagement/src/ai-evaluator.ts`, `plugins/continuity-threads-engagement/src/ui-server.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: scan count/notifications and HTTP results; publication returns reply ID or error.
- Later read-back: persisted posts/drafts and selected draft are read by review endpoints and later approval requests; search logs control later budget checks.
- Delegated visibility: scoring model receives persona/keywords and post text; drafting model receives persona plus selected post; Threads API receives selected draft text.
- Selection predicate: configured keywords and maximum searches, deduplication, model score threshold, then selected draft or first-draft fallback at approval.
- Invalidation or expiry: regeneration deletes prior drafts; status changes retain workflow state; scheduler stop clears interval, not previously posted replies.
- Activation or effect: score-based draft admission and endpoint-triggered external posting are wired; actual human review and successful posting are unobserved.
- Evidence limits: no execution; localhost binding alone does not authenticate human intent; missing external API behavior prevents publication reliability conclusions.

Operating mode: recurring open search with bounded search budget and model judgment, not a benchmark. Answer oracle: none supplied. Human review is the intended UI decision; the implemented endpoint admits any request reaching it with a configured API, existing post and available draft. It does not require preexisting approved status. Rejection/skip/status APIs exist, but no rollback of a successful remote reply is shown here. Failed posting writes a failed engagement record; retry/idempotency of remote effects is not established. Guidance asks authentic, concise replies; drafts and engagement records persist, not provider parameters.

> // Get the selected draft (or first draft)
> let draft = getSelectedDraft(post.id);
> if (!draft) {
>   const drafts = getDraftsForPost(post.id);
>   draft = drafts[0];
> }
> --- `plugins/continuity-threads-engagement/src/ui-server.ts`

> const replyId = await deps.threadsApi.postReply(post.id, draft.draft_text);
> --- `plugins/continuity-threads-engagement/src/ui-server.ts`

#### RT-RTE-org-ingestion
Label: Organization memory HTTP admission and desktop pull routing

Owner/principal: authenticated HTTP caller supplies candidate memories; organization code validates and upserts them. Plugin sync subscribes/queues local changes, pushes batches and pulls remote records through SDK SQL execution. These are two distinct admission points, not proof of a joined memory loop. SRC-1, `org-server/src/routes/memories-push.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`, `plugin-sdk/src/db.ts`, `plugin-host/src/handlers/db.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: server acknowledgment/validation errors; sync updates counters and logs errors, requeues failed pushes.
- Later read-back: org pull/search can consume admitted server rows; successful local memory.db admission through this SDK call is not established because it omits the database selector.
- Delegated visibility: server receives serialized memory batches; plugin receives remote memories; host receives SQL/parameters without a memory database target.
- Selection predicate: sync scope filter and remote since cursor; server schema/auth checks and timestamp conflict guard; local SQL conflict expression is a separate policy.
- Invalidation or expiry: server newer/equal timestamps can replace row content; pending push queue is in process memory; failed pushes are requeued, pull errors logged.
- Activation or effect: organization state can change; current SDK defaults route pulls to app database, so intended desktop memory consumption is not proven.
- Evidence limits: no roundtrip run; app database contents and event delivery are unobserved; server upsert policy cannot be assumed identical to local pull policy.

Admission: caller proposes; schema/auth and SQL guard decide, not human content approval. Server batch transaction supplies atomic admission within its own database; it is not a distributed transaction. SDK users cannot select `memory` through the inspected execute wrapper. Recovery requeues pushes in memory but does not guarantee survival across process loss. No truth oracle is supplied. Persisted server rows are external knowledge input; provider weights/product machinery are unchanged.

> const result = await this.client.request("db.execute", { sql, params }) as { rowsAffected: number };
> --- `plugin-sdk/src/db.ts`

> const target = (params.database as string) || "app";
> if (target === "memory") return getMemoryDb();
> return getAppDb();
> --- `plugin-host/src/handlers/db.ts`

> WHERE excluded.updated_at >= memories.updated_at
> --- `org-server/src/routes/memories-push.ts`

### Claims

#### RT-CLM-plugin-controls
Label: Plugin capability checks are API-local controls

Claim assessed: API capability checks authorize selected host operations, not arbitrary plugin-process behavior or independent grant assignment. Owner/enforcement: DB/chat/MCP/UI handlers check session strings; server connection checks shared token; registration trusts caller capability list. Guarantee strength: policy. Covered paths: those handlers. Alternate paths: sidecar Node/interpreter code, direct SDK network/model calls, and native filesystem/shell grants do not pass through those same checks. Required external contract: trustworthy installed plugin code and OS/process restrictions if stronger isolation is desired. implementation conclusion status: wired; operation conclusion status: uninspected. SRC-1, `plugin-host/src/handlers/db.ts`, `plugin-host/src/handlers/chat.ts`, `plugin-host/src/index.ts`, `plugin-host/src/server.ts`, `lib/plugins/manager.ts`, `src-tauri/capabilities/default.json`.

> if (!session.capabilities.includes("db:write")) {
>   throw new Error("Plugin lacks db:write capability");
> }
> --- `plugin-host/src/handlers/db.ts`

> "identifier": "shell:allow-spawn",
> "allow": [
>   { "name": "npx", "cmd": "npx", "args": true },
>   { "name": "node", "cmd": "node", "args": true },
> --- `src-tauri/capabilities/default.json`

The native grant is a shipped capability envelope for the main window, not evidence of which grants were exercised. The SQL safety regex and handler checks are additional local rules; no comprehensive SQL-security conclusion is made. Caller-supplied capability copying is the forcing counterexample to interpreting the handler membership test as independently authorized least privilege.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-system-guidance
Label: Shipped and retained guidance to desktop model

Consumer: configured foreground model. Channel: rebuilt system message carrying personality/workspace/tool guidance, user custom instructions, memory context and narrative. Force: natural-language instruction/context interpreted by the model, not deterministic enforcement. Horizon: current send, with stored user/memory/narrative content deliverable across later sends. Source-native working-context selection is code-controlled; actual behavioral activation is unobserved. SRC-1, `providers/chat-provider.tsx`.

> ...(narrativePrompt ? [narrativePrompt] : []),
> ...(memoryContextPrompt ? [memoryContextPrompt] : []),
> WORKSPACE_AGENT_PROMPT,
> --- `providers/chat-provider.tsx`

#### RT-BAP-plugin-capabilities
Label: Caller-supplied capability strings to RPC handlers

Consumer: host DB/chat/MCP/UI handler checks. Channel: symbolic `session.capabilities` copied from registration. Force: direct conditional allow/error at covered handler entry points. Horizon: WebSocket session. This is not the natural-language plugin prompt path and does not cover process-native effects. SRC-1, `plugin-host/src/index.ts`, `plugin-host/src/handlers/db.ts`, `plugin-host/src/handlers/chat.ts`.

> if (!session.capabilities.includes("chat:prompts")) {
>   throw new Error("Plugin lacks chat:prompts capability");
> }
> --- `plugin-host/src/handlers/chat.ts`

## Annotations

none
