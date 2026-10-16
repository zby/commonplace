---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Cludebot runtime baseline: authenticated chat, memory entry modes, maintenance and dashboard execution at the frozen repository revision."
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
reviewed-boundary: cecf234f10397b1e21dec2ff65ded864982f3564
---

# Cludebot runtime report

## Runtime account

### Evidence and claimed work

Cludebot's source calls the memory engine Clude. Its central claim is processing retained experience, not simply returning stored records; see [RT-CLM-cognitive-memory](#rt-clm-cognitive-memory). This account uses SRC-1 implementation and doctrine/design at the boundary revision. No target, test, example, model call or service was executed. Wiring below is inspectable; invocation success, activation of delivered memories and benefit are unobserved. Nothing here upgrades tracked benchmark claims to independently observed results.

The ordinary invocation selected is an authenticated chat message: an identified wallet's conversation and retrieved memory become a model input, a streamed answer becomes conversation state, and a sufficiently long input also schedules a memory write. The model chooses answer text, not arbitrary tools, in this path. Code owns identity, retrieval, trimming, provider selection, persistence and return ([RT-RTE-chat-turn](#rt-rte-chat-turn)). The actual model sees dated summaries and bounded content snippets, not necessarily whole stored records ([RT-OBJ-memory-context](#rt-obj-memory-context)).

### Ordinary invocation and working context

`chatAuth` accepts an active Cortex key or upstream Privy identity. A supplied wallet on the Privy path must be linked to that identity. The handler then fetches the conversation by both ID and owner, checks rate/content/balance and attachment constraints, starts owner-scoped recall with expansion skipped, and inserts the user message before loading history. Temporal results can supplement recall. Recall failure becomes an empty result rather than preventing generation. History loading orders ascending and limits to 50; therefore the fitter's newest-first walk is newest within that fetched prefix, not necessarily the latest 50 turns of a long conversation. A universal claim that it always preserves the current/latest turn is not supported (SRC-1, `apps/server/src/routes/chat.routes.ts`).

The code-rule context controller always keeps the base system prompt, reserves space for memories, walks fetched history backwards until its heuristic budget is exhausted, then takes a prefix of the memory list. It estimates tokens by character count, with floors and reserves; this is not a provider-tokenizer invariant. Omitted conversation text remains in the database; retained memories remain reachable through later recall. The caller does not receive an isolated sub-agent frame or a summary replacing the discarded tail. Each generation is a reconstructed window, not a pointer graph: IDs in metadata do not give the model implicit access to omitted text. Memories are grouped by type and ordered chronologically inside groups after selection. Images are inserted into the last fitted message only when that message is a user turn (SRC-1, `apps/server/src/routes/chat.routes.ts`, `apps/server/src/lib/memory-prompt.ts`, `packages/shared/src/core/memory-grounding.ts`).

The handler resolves a BYOK provider or an OpenRouter model, invokes `streamText`, and pipes UI message events to HTTP. A timeout/disconnect abort signal covers this call. After the streamed result, the handler writes assistant content, conversation timestamp and usage, deducts a balance when applicable, generates a title asynchronously and asynchronously stores an episodic interaction. Stream delivery and memory durability are separate outcomes. Logged recall/store/billing failures do not imply rollback of already delivered text. See [RT-RTE-chat-turn](#rt-rte-chat-turn) and [RT-RTE-memory-entry](#rt-rte-memory-entry).

### Four forcing cases and guarantee boundaries

1. **Unauthenticated chat:** `/guest` is mounted before `chatAuth`; it sends a simple persona, at most ten client-supplied history entries and the current input through its own provider HTTP path. It does not perform the authenticated memory loop. This falsifies a system-wide reading of the persona's promise to remember conversations, without establishing a defect in an authenticated-only contract ([RT-RTE-guest-chat](#rt-rte-guest-chat)).
2. **Local/direct entry:** MCP dispatch selects JSON local, hosted API, SQLite default or self-hosted memory code. The SDK independently chooses hosted HTTP or an injected service-role database client. Consequently hosted authentication, rate limiting, request owner scope, PostgreSQL enrichment and chain behavior cannot be presumed to cover every invocation. Local modes change the storage/execution boundary; they are not merely alternate URLs ([RT-RTE-memory-entry](#rt-rte-memory-entry)).
3. **Dashboard execution:** a separately instantiated Anthropic client drives a tool loop, bypassing the shared `generateResponse` prompt assembly and the chat renderer. Allowed names filter advertised schemas, while the dispatcher checks the global registry rather than the per-agent allowlist. The time limit races a promise without cancelling the losing work. These are limits on policy enforcement and timeout strength, not evidence of an observed malicious call or post-timeout effect ([RT-RTE-dashboard-task](#rt-rte-dashboard-task)).
4. **Durable/background variants:** main dreams, owner-scoped hosted dreams, asynchronous writes and flag-gated enrichment do not share one transactional boundary. Main dreams race a timer and reset their guard on completion/failure; the timer does not cancel outstanding phases. Encrypted-content storage explicitly falls back to plaintext when DEK-wrap persistence fails. Neither "timeout" nor "encrypted" is a universal end-to-end invariant ([RT-RTE-dream-cycle](#rt-rte-dream-cycle), [RT-RTE-memory-entry](#rt-rte-memory-entry)).

The load-bearing controls are scoped as follows:

| Control and owner | Enforcement point and strength | Covered paths, counterpaths and external contract | Separate statuses |
|---|---|---|---|
| Chat caller/conversation ownership; HTTP service | `chatAuth`, owner-filtered conversation query and `withOwnerWallet`; protocol | Covers inspected authenticated chat handler. Guest intentionally precedes auth. SDK direct DB access and local MCP have other principals. Depends on active-key records, Privy verification and query/RPC scoping; not a claim about all tenant APIs. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Grounding and temporal resolution; prompt author/model | System prompt's memory rules; policy | Applies to chat-rendered memory input, not an answer verifier. Shared response service and executor use different prompt paths. Requires provider/model compliance. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Context limit; chat handler | Character-estimate fitter; best effort | Applies to assembled authenticated chat messages, not every provider request, guest history or executor transcript. Requires estimates and provider limits to align. Prefix-limited DB history and minimum budgets prevent a strict latest-turn/token-limit guarantee. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Tool grant; agent configuration | Schema filtering; policy | Dashboard advertises a configured subset, but execution dispatch is registry-wide. No isolated per-tool credential or sandbox boundary established. Depends on model tool-name behavior and downstream tool services. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Write completion/encryption; memory implementation | Insert, optional envelope/legacy encryption, optional outbox; best effort | A memory ID is not enrichment, chain finality or always-encrypted-at-rest confirmation. Local stores differ. Depends on DB, crypto and optional worker/chain services. Explicit plaintext fallback defeats an unconditional encryption claim. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence for these qualifications is retained in the linked route/object records, not inferred from the table labels. In particular, request identity, capability surface and deployment isolation are different facts. The executor registry can post tweets, recall memory, store findings and update task state; the configured tool list is the advertised grant. The actual running process credentials, network policy and database privileges are uninspected. No inspected dispatch boundary establishes a shell sandbox; setup's process/configuration operations are a separate operator path, not an executor tool grant (SRC-1, `packages/brain/src/agents/tools.ts`, `packages/brain/src/cli/setup.ts`).

### Change admission and remaining coverage

The shipped system admits content by caller-authored SDK/MCP writes, automatic chat writes, imported packs and model-produced maintenance outputs. Configuration changes also replace task prompts, model names, iteration limits and advertised tools; setup installs MCP configuration and instruction text. These are different admission mechanisms, not one universal human approval gate. Their controls and recovery are recorded in [RT-RTE-memory-entry](#rt-rte-memory-entry), [RT-RTE-pack-import](#rt-rte-pack-import), [RT-RTE-dashboard-task](#rt-rte-dashboard-task), [RT-RTE-dream-cycle](#rt-rte-dream-cycle) and [RT-RTE-host-setup](#rt-rte-host-setup). This report establishes runtime admission, not whether the resulting memory revisions are warranted theories or improve future capacity; those findings belong to the specialist accounts.

Added SRC-1 implementation coverage beyond the boundary's initial reads includes bounded handler/control ranges in `apps/server/src/routes/chat.routes.ts`, `apps/server/src/routes/cortex.routes.ts`, `apps/server/src/routes/dashboard.routes.ts`, `apps/server/src/routes/memory-packs.routes.ts`, `apps/server/src/bootstrap.ts`, `packages/brain/src/agents/executor.ts`, `packages/brain/src/agents/tools.ts`, `packages/brain/src/agents/types.ts`, `packages/brain/src/auth/require-ownership.ts`, `packages/brain/src/memory/memory.ts`, `packages/brain/src/memory/dream/cycle.ts`, `packages/brain/src/mcp/server.ts`, `packages/brain/src/cli/setup.ts` and `packages/brain/src/sdk/cortex.ts`; full small renderer, owner-context and local embedder implementations; and provider/hosted-dream/worker symbol searches at the same frozen revision. No additional source or evidence layer is introduced.

Worker registration names mention polling, mood tweeting, active reflection, campaigns, sentiment, compound jobs and task execution (SRC-1, `apps/workers/src/jobs/index.ts`). Their detailed social loops, marketplace/payment/title/chain transfer admission, mobile/web client behavior, experimental local memory, evaluator internals and deployed infrastructure were not substantively traced here. Likewise SQLite dream-engine internals and hosted-dream output checking are not equated to main dream behavior. These are available included source paths, not absences or access gaps. This selected runtime baseline supports the ordinary loop and four forcing comparisons, not an exhaustive audit or a guarantee across those unresolved branches.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Chat provider model

The model selected by `resolveOpenRouterModel` or BYOK resolution is a distributed-parametric computation behind a remote provider endpoint; weights are provider-held, while source configuration stores model identifiers. It supplies the natural-language response in [RT-RTE-chat-turn](#rt-rte-chat-turn). Parameter updates are not performed by this handler; provider-side parameter changes are uninspected. Exact weights/version are not pinned by the request. Provider aliases/endpoints may resolve to changed implementations; deployed resolution is unobserved. SRC-1, `apps/server/src/routes/chat.routes.ts`:

> const result = streamText({
>         model: llmModel,
>         messages: aiMessages,
> --- `apps/server/src/routes/chat.routes.ts`

#### RT-CMP-anthropic
Label: Anthropic task model

The dashboard executor's `Anthropic` client consumes `agentConfig.model` and remote distributed-parametric weights. Model identity is symbolic data in database agent configuration/defaults; exact provider weights are not pinned. Runtime config can select another model name. The inspected executor performs inference, not parameter training; mutable remote resolution and provider-side updates remain uninspected. This is distinct from chat's resolved provider instance and from dream generation through the shared client. SRC-1, `packages/brain/src/agents/executor.ts`:

> const response = await client.messages.create({
>             model: agentConfig.model,
> --- `packages/brain/src/agents/executor.ts`

#### RT-CMP-generate-response
Label: Shared response generation models

`generateResponse` combines personality/task/context text and invokes either OpenRouter cognitive routing or a direct Anthropic model. Distributed-parametric model state lives at those providers; the symbolic configuration and prompt text live in source/process state. The SDK can override the Anthropic client/model. No parameter-writing operation is shown in this inference route; provider internals and any provider training are uninspected. Exact model weights are not pinned, and configuration/routing or mutable provider resolution can select another model. SRC-1, `packages/shared/src/core/claude-client.ts`, `packages/brain/src/sdk/cortex.ts`:

> const provider = isOpenRouterEnabled() ? 'openrouter' : 'anthropic';
> --- `packages/shared/src/core/claude-client.ts`

#### RT-CMP-embeddings
Label: Remote embedding models

The shared embedding adapter sends text and a configured/default model identifier to provider APIs and returns numerical vectors. Weights are distributed-parametric remote state; vectors are retained numerical representations, not trained adapter parameters. Provider defaults include Voyage, OpenAI-compatible and Ollama choices, with a separate query-provider fallback and Vertex support. No weight-update call is established in the inspected adapter. Exact weight revisions are not pinned; configuration and mutable local/remote model resolution can change the model. Provider internals are uninspected. SRC-1, `packages/shared/src/core/embeddings.ts`:

> const model = cfg.model || providerConfig.defaultModel;
> --- `packages/shared/src/core/embeddings.ts:159-164`

#### RT-CMP-local-embedder
Label: LocalEmbedder

The MCP SQLite mode constructs `LocalEmbedder`: numerical feature extraction through a downloaded/cached transformer, separate from remote embedding selection. It caches vectors in a process map and model files under the user's `.clude/models`. No runtime weight update appears in this class. A named model and quantization are specified, but no immutable model revision/digest; later artifact resolution may differ, and actual cached artifacts are uninspected. SRC-1, `packages/brain/src/storage/embedder.ts`:

> this.extractor = await pipeline(
>       'feature-extraction',
>       'Xenova/all-MiniLM-L6-v2',
>       { dtype: 'q8' }
>     );
> --- `packages/brain/src/storage/embedder.ts`

### Operative objects

#### RT-OBJ-memory-context
Label: Rendered memory context

This is the transient model-visible natural-language rendering, not the underlying retained memory rows. Strings are assembled in process memory as a system message. Symbolic type/date handling determines section membership/order; the resulting summary/content prose and rules receive consequences through model interpretation. `renderGroundedLine` retains summary text and at most 600 content characters; unsupported memory types are not rendered by the chat grouping. Sorting is within selected type groups, not a claim that retrieval delivered all history. SRC-1, `apps/server/src/lib/memory-prompt.ts`, `packages/shared/src/core/memory-grounding.ts`:

> export const GROUNDED_CONTENT_MAX = 600;
> --- `packages/shared/src/core/memory-grounding.ts`

> sections.push('<behaviors>\n' + procedural.map(renderMemoryLine).join('\n') + '\n</behaviors>');
> --- `apps/server/src/lib/memory-prompt.ts`

### Routes

#### RT-RTE-chat-turn
Label: Authenticated chat turn

Endpoints: authenticated HTTP `/messages` to owner conversation, recall, provider generation, streamed answer and later database/memory writes. Principal is the key/JWT-resolved owner; code owns progression; [RT-CMP-chat-model](#rt-cmp-chat-model) chooses text. Input/history/selected memories are natural-language context; database identifiers, limits and accounting are symbolic. No tool schema is supplied to this `streamText` call. Conversation ownership, selection and trimming are described in the runtime account. SRC-1, `apps/server/src/routes/chat.routes.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed answer plus usage/memory-ID metadata; errors may return JSON before headers or interruption events after headers.
- Later read-back: saved messages enter later history loads; asynchronous episodic memory writes can enter later recall.
- Delegated visibility: the selected provider receives fitted system/history text and signed image URLs when attached; not every recalled row or whole stored content.
- Selection predicate: owner-scoped query recall, optional temporal supplementation, type rendering, prefix budget fitting and ascending history query limited to 50.
- Invalidation or expiry: context rebuilt each request; abort on configured timeout/disconnect; memory decay/updates affect later selection, without deleting all source messages.
- Activation or effect: provider invocation and post-stream persistence are wired; actual dependence of an answer on a delivered memory is unobserved.
- Evidence limits: no execution trace; token estimates and persisted memory IDs show intended delivery, not answer correctness, provider attention or successful asynchronous writes.

Admission: the caller supplies input, the model proposes answer text, and handler rules automatically admit the exchange to conversation storage and, if input length exceeds ten, episodic storage. No per-answer human approval is shown. Content/rate/ownership gates can reject the request; memory failure logs a warning after response. No atomic rollback of streamed output plus database plus memory is implemented in this handler. Operating mode is open conversation, not a bounded evaluation curriculum; no reference-answer oracle is supplied. Guidance is the shipped system prompt; persisted material is user/model exchange plus metadata, not changed model parameters.

> recallMemories({ query: content, limit: 25, skipExpansion: true })
> --- `apps/server/src/routes/chat.routes.ts`

> if (content.length > 10) {
>         const memoryContent = `User said: ${content}\n\nAssistant replied: ${fullContent}`;
> --- `apps/server/src/routes/chat.routes.ts`

#### RT-RTE-guest-chat
Label: Guest chat alternate

Endpoints: unauthenticated `/guest`, IP quota, content check, parallel OpenRouter HTTP requests, SSE response. The caller supplies current content and optional history; code selects bounded recent client history, races Kimi/Venice/Llama model requests with `Promise.any`, keeps the first successful HTTP response and aborts losers. This selects by availability/latency, not answer quality; a winning response need not yet contain a complete answer. This does not run memory recall/store. These remote distributed-parametric models use named identifiers without pinned weight revisions; no parameter updates are implemented here, while provider-side mutability remains uninspected. SRC-1, `apps/server/src/routes/chat.routes.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SSE text and final guest/model/quota metadata, or a rate/content/configuration error.
- Later read-back: inapplicable — this handler does not persist/reload the memory or conversation exchange; client history can be resent but its retention policy is outside the inspected handler.
- Delegated visibility: provider gets the guest persona, last ten supplied history entries and current content.
- Selection predicate: valid content, IP quota and content filter; `messages.slice(-10)` controls history inclusion.
- Invalidation or expiry: per-IP quota uses a 1440-minute window; a 30-second timer/disconnect aborts provider requests, and losing race requests are explicitly aborted.
- Activation or effect: generation/streaming is wired, but persistent memory and memory activation are not established on this route.
- Evidence limits: no provider run or client retention trace; this route does not establish authenticated-route behavior.

> ...messages.slice(-10), // last 10 messages from client-side history
>         { role: 'user', content },
> --- `apps/server/src/routes/chat.routes.ts`

> winner = await Promise.any(attempts);
> --- `apps/server/src/routes/chat.routes.ts`

#### RT-RTE-memory-entry
Label: SDK and MCP memory entry

Endpoints: SDK store/recall to hosted `/api/cortex` or direct memory functions; MCP tools to hosted HTTP, self-hosted functions, SQLite or JSON local store. The caller/host proposes content and queries. Symbolic dispatch chooses execution/storage boundary. MCP returns text-encoded JSON rather than directly injecting a system prompt. Downstream model use is host-owned. SRC-1, `packages/brain/src/sdk/cortex.ts`, `packages/brain/src/mcp/server.ts`, `packages/brain/src/memory/memory.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: memory ID/null or recall records through SDK; MCP returns JSON text and error indicators.
- Later read-back: stored content is eligible for later recall or explicit hydration; the SDK exposes summary recall followed by hydration, but automatic host use is not guaranteed.
- Delegated visibility: hosted calls send content/query to the HTTP service; enrichment can send text to embedding/extraction providers; local SQLite uses [RT-CMP-local-embedder](#rt-cmp-local-embedder). MCP delivers selected records back to its host.
- Selection predicate: mode flags/configuration first, then per-tool schema and supplied query/type/tag/threshold/limit filters; hosted auth resolves key owner and wraps memory operations in request scope.
- Invalidation or expiry: memory management differs by store; MCP exposes update/delete paths. SDK requires initialization. HTTP errors/timeouts propagate or become tool errors. No cross-mode invalidation equivalence established.
- Activation or effect: insertion and dispatch are wired; successful chain registration, complete enrichment and behavioral activation are separate, unobserved effects.
- Evidence limits: local stores' full mutation semantics, all recall RPCs and hosted endpoints were not audited; no claim of mode parity, universal tenant isolation or universal encrypted storage.

Admission is software/caller-controlled: a host may call MCP autonomously, and the SDK caller need not be human. MCP constrains schema/lengths; `storeMemory` rejects empty text, applies a narrow duplicate rule, clamps scores, truncates content/summary and inserts. Human content authorship and per-item approval are not established by the presence of a caller. Open-ended storage/recall is not an oracle-scored experiment. No answer oracle or semantic truth veto is shown by these syntactic checks. Source-provided importance/tags and auto-categorization guide stored metadata. Read-back makes content available, not necessarily obeyed. Recovery is error/null reporting plus separate update/delete operations, not a cross-service transaction.

The hosted key gate is not a deployment-wide isolation proof. Direct SDK supplies a service key and optionally a module owner; an unset owner can yield unfiltered reads while the fail-closed flag is off. Registration itself includes public wallet/email admission branches, so valid key ownership cannot be generalized into proof of externally verified wallet provenance (SRC-1, `apps/server/src/routes/cortex.routes.ts`, `packages/brain/src/memory/memory.ts`, `packages/shared/src/core/owner-context.ts`).

> const isSqliteMode = !isLocalMode && !isHostedMode && !SUPABASE_URL;
> --- `packages/brain/src/mcp/server.ts`

> return isOwnerScopeFailClosed() ? SCOPE_BOT_OWN : null;
> --- `packages/brain/src/memory/memory.ts`

`storeMemory` can enqueue a durable enrichment job when enabled, otherwise launches embedding/link/entity work without awaiting completion; chain commit is separately asynchronous. Server bootstrap conditionally starts the outbox poller. A returned ID is not a completion receipt for these effects (SRC-1, `packages/brain/src/memory/memory.ts`, `apps/server/src/bootstrap.ts`). The encryption fallback is explicit:

> log.error({ id: data.id, error: wrapErr.message }, 'DEK wrap write failed — reverting memory to plaintext');
>         await db.from('memories').update({
>           content: plaintextContent,
>           encrypted: false,
>           encryption_pubkey: null,
>           provider_delegated: null,
>         }).eq('id', data.id);
> --- `packages/brain/src/memory/memory.ts`

#### RT-RTE-dashboard-task
Label: Dashboard agent task execution

Endpoints: owner-gated dashboard agent/task mutation or manual execution; pending-task poll; direct Anthropic tool loop; global tool registry; task/activity/budget persistence. Task/agent IDs are database identities, not delegated tenant credentials: `ToolContext` contains task ID, agent ID and agent name. Each task gets its own message array/system prompt; the loop accumulates tool results without inspected trimming. The foreground chat context does not enter automatically. Returned tool text crosses into the task's model context; persisted result/log metadata crosses back to dashboard storage. SRC-1, `apps/server/src/routes/dashboard.routes.ts`, `packages/brain/src/agents/executor.ts`, `packages/brain/src/agents/tools.ts`, `packages/brain/src/agents/types.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: manual endpoint reports launch status while execution runs in the background; model/tool outputs produce task completion/failure metadata later.
- Later read-back: inapplicable — executor builds fresh task input and does not itself reload previous execution logs; `store_finding` can separately write retained memory for later recall.
- Delegated visibility: remote model sees configured prompt, task description/metadata input and accumulated tool results; tool executors receive arguments and task/agent identifiers.
- Selection predicate: poll chooses pending tasks with assigned online known-type agents, respecting local concurrency slots; atomic pending-to-in-progress claim with returned-row checking coordinates polling contenders. Manual execution checks known type and the local running map, but does not require online status, enforce the poll's slot limit or check a returned claimed row; do not extend polling coordination guarantees to it.
- Invalidation or expiry: configured max iterations/time limits; stop clears polling but does not establish cancellation of running requests. Promise-race timeout does not abort the loop or tools.
- Activation or effect: dispatch can post to X, write findings and mutate task/activity state using process services; no exercised effects observed.
- Evidence limits: no deployed grants/credentials or isolation configuration inspected; schema filtering is not an execution-time allowlist; timeout is not a hard effect deadline.

The admin supplies or replaces configuration JSON; known fields override prompt/model/tool names and execution limits. `ownerOnly` checks a proven wallet against configured bot owner for mutations. These are human-authorizable capability/instruction changes, but code alone does not establish a human authored each payload. Rejection is HTTP ownership enforcement plus config/tool-name resolution; no versioned rollback is shown, though the owner can replace config and retry tasks. The model decides tool order and completion within an open task, with no reference-answer oracle. `complete_task`, end-turn without tools and iteration exhaustion can all lead to the success path; "completed" is not independent correctness validation.

> const ownerOnly = [requireOwnership, assertOwnerWallet];
> --- `apps/server/src/routes/dashboard.routes.ts`

> return allowedTools
>     .filter(name => TOOL_REGISTRY[name])
>     .map(name => TOOL_REGISTRY[name].schema);
> --- `packages/brain/src/agents/tools.ts`

> const tool = TOOL_REGISTRY[toolName];
> --- `packages/brain/src/agents/tools.ts`

The dispatcher has no per-agent allowlist parameter. The executor forwards each model-returned tool name to it. This makes schema restriction a provider/model-facing policy, not an invariant against unexpected registered tool names. The shared client's anti-URL prompt is also not inherited by this separate client (SRC-1, `packages/brain/src/agents/executor.ts`, `packages/shared/src/core/claude-client.ts`).

#### RT-RTE-dream-cycle
Label: Dream cycle orchestration

Endpoints: episodic importance event, scheduled/SDK trigger, ordered maintenance phases, stored memory/dream log and emergence output. Code owns scheduling and progression; [RT-CMP-generate-response](#rt-cmp-generate-response) proposes natural-language maintenance content. Main cycle calls consolidation, compaction, reflection, contradiction resolution, learning, deep connection and emergence in order. Phase labels do not establish epistemic success. Main event-triggered execution explicitly clears request owner scope; hosted dreams separately iterate active owner-scoped agents and are not the same algorithm. SRC-1, `packages/brain/src/memory/dream/cycle.ts`, `packages/brain/src/memory/hosted-dreams.ts`, `packages/brain/src/sdk/cortex.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: asynchronous event scheduling or awaited SDK cycle completion; errors logged inside main trigger, so resolved return need not mean every phase succeeded.
- Later read-back: generated semantic/procedural content goes through memory storage; accumulator/timestamp persist for later scheduling; later recall can expose maintenance products.
- Delegated visibility: consolidation sends selected memory summaries to generation; internal phase state is not the entire foreground chat context. SDK may intercept emergence through a callback rather than posting it.
- Selection predicate: event accumulator threshold/minimum interval and guard; six-hour scheduler fallback; phase-specific recent-memory selection. Hosted dreams have separate agent/cooldown/count predicates.
- Invalidation or expiry: phase failures/time race logged; finally resets local guard. Partial writes are not rolled back by the orchestrator and timeout does not cancel losing work.
- Activation or effect: ordered maintenance calls and automatic writes are wired; exercised memory revision and downstream behavioral dependence are unobserved.
- Evidence limits: only orchestration and direct-consolidation admission traced substantively; other phase mechanisms, SQLite parity, hosted model-output checking and distributed lock coverage remain uninspected.

Admission example: direct consolidation asks for 2–3 observations with cited evidence; code splits lines, keeps up to three, parses citations, rejects cop-out responses and automatically stores semantic insights. This is a model proposal with code admission, not per-insight human approval or independent truth validation. No expected-answer oracle is supplied. Open-ended maintenance triggers follow importance/time rather than an experiment curriculum. Guidance persists as shipped prompts; generated text/evidence references persist as memory and dream logs. Main orchestration offers no transactional rollback of earlier phases. Whether generated statements constitute formulated theories, criticism or learning is left to their content-level analysis, not inferred from this route's name.

> await runConsolidation();
>         await sleep(3000);
>         await runCompaction();    // Beads-inspired memory compaction
> --- `packages/brain/src/memory/dream/cycle.ts`

> if (isCopoutResponse(text)) {
>       log.warn('Direct consolidation produced cop-out response — discarding');
>       continue;
>     }
> --- `packages/brain/src/memory/dream/cycle.ts`

#### RT-RTE-pack-import
Label: JSON memory pack import

Endpoints: Privy-authenticated `/api/memory-packs/import` with optional wallet ownership middleware, caller-supplied array, sequential `storeMemory` writes, count response. Proposed content is arbitrary pack data, not model-selected truth. This is a separate bulk admission surface from SDK/MCP schemas. SRC-1, `apps/server/src/routes/memory-packs.routes.ts`, `packages/brain/src/auth/require-ownership.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: imported/total counts, invalid-format rejection or error.
- Later read-back: successful entries become normal memory rows eligible for later recall under their effective write scope.
- Delegated visibility: importer passes pack fields into storage/enrichment; no separate remote worker context is established by this handler itself.
- Selection predicate: requires `pack.memories` to be an array; maps type/defaults, truncates text/summary, records source/import metadata; underlying store applies further checks.
- Invalidation or expiry: failures can leave a partial import; no batch rollback or per-item review shown in this handler.
- Activation or effect: sequential row admissions are wired; later owner visibility and model dependence are not demonstrated.
- Evidence limits: handler does not itself use `withOwnerWallet`; optional ownership verifies a supplied wallet but does not establish async owner scope. Effective deployment/middleware/module scope is unresolved; do not claim imported rows necessarily belong to the importing user's wallet.

Caller decides the pack, software admits individual writes, and there is no per-content approval/truth gate or answer oracle. Operating mode is open import. Rejection/rollback is limited to input check, underlying failed writes and later memory management. Original IDs and pack name persist as provenance metadata; this does not authenticate authorship or correctness.

> router.post('/import', requirePrivyAuth, optionalOwnership, async (req: Request, res: Response) => {
> --- `apps/server/src/routes/memory-packs.routes.ts`

> if (id) imported++;
> --- `apps/server/src/routes/memory-packs.routes.ts`

#### RT-RTE-host-setup
Label: Host instruction installation

Endpoints: operator CLI/setup to MCP configuration and project `CLAUDE.md`/`AGENTS.md`; later external host session/tool calls. Symbolic JSON config launches a process; natural-language instruction text requests recall/store policy. This is capability and instruction admission, not the inspected system modifying its own source code. SRC-1, `packages/brain/src/cli/setup.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: configuration write status and instruction injection result (created, updated, appended or null).
- Later read-back: installed instruction block is intended for later host sessions, directing memory recall/storage; static shipped policy is not accumulated experience.
- Delegated visibility: host obtains instruction/config files and can receive MCP result text; exact host prompt loading and tool approval remain external.
- Selection predicate: selected IDE/config target and `agentsmd` flag; existing section markers determine replacement versus append/create.
- Invalidation or expiry: replacement is idempotent by marker; file errors return failure/null. Host/operator can edit or remove files; no automatic rollback history inspected.
- Activation or effect: durable file writes are wired; actual host loading/compliance and grant are unobserved.
- Evidence limits: no external agent execution evidence, package-resolution digest or deployed config was supplied; writing a policy does not enforce host behavior.

Operator initiates setup and chooses target/mode; shipped text supplies proposed policy, and code merges configuration/replaces the marked section. No per-future-memory human approval is thereby created. This is open installation, not oracle-based candidate testing. The policy asks the host to recall before responding, store selected discoveries and use Clude instead of `MEMORY.md`; it persists on disk until edited. Installed `npx @clude/sdk` invocation does not itself pin immutable future package content.

> At the start of every session, call \`recall_memories\` with relevant context before responding.
> --- `packages/brain/src/cli/setup.ts`

> Use Clude memory INSTEAD of writing to MEMORY.md files.
> --- `packages/brain/src/cli/setup.ts`

### Claims

#### RT-CLM-cognitive-memory
Label: Cognitive memory claim

The source claims maintenance beyond storage/retrieval, including decay, consolidation, contradiction resolution and reflection. This is doctrine/design; orchestration and selected writes are wired, not independently demonstrated cognitive improvement. SRC-1, `README.md`:

> A cognitive memory system. Most memory SDKs store and retrieve. Clude also processes memories over time — decay, consolidation, contradiction resolution, reflection.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-chat-grounding
Label: Chat memory grounding policy

Consumer: selected chat provider model. Channel: system message carrying rendered memories, typed sections and grounding/temporal rules. Force: natural-language instruction, not symbolic execution or answer verification. Horizon: current invocation, reconstructed from retained content on later turns. Delivery is wired; obedience and causal benefit unobserved. See [RT-OBJ-memory-context](#rt-obj-memory-context) and [RT-RTE-chat-turn](#rt-rte-chat-turn). SRC-1, `apps/server/src/lib/memory-prompt.ts`:

> - Never invent memories, past conversations, or details that are not written above. "I don't have that in memory" is always better than a confident guess.
> --- `apps/server/src/lib/memory-prompt.ts`

#### RT-BAP-agent-configuration
Label: Agent configuration authority

Consumer: executor and provider model. Channel: database agent config merged over defaults; model/system/tool-schema arguments. Force: symbolic selection of model/limits/advertised schema plus natural-language direction through the system prompt. Horizon: later task executions reload the configured row. This grants no demonstrated per-tool isolation; dispatcher scope remains registry-wide. See [RT-RTE-dashboard-task](#rt-rte-dashboard-task). SRC-1, `packages/brain/src/agents/types.ts`:

> ...(agentConfig.systemPrompt ? { systemPrompt: String(agentConfig.systemPrompt) } : {}),
> --- `packages/brain/src/agents/types.ts`

#### RT-BAP-host-instructions
Label: Installed host memory policy

Consumer: external coding-agent/IDE host. Channel: project instruction file and MCP configuration. Force: requested tool-use behavior plus process availability, conditional on host loading/grants; not an enforced runtime invariant. Horizon: future project sessions until overwritten/removed. See [RT-RTE-host-setup](#rt-rte-host-setup). SRC-1, `packages/brain/src/cli/setup.ts`:

> const fileName = options?.agentsmd ? 'AGENTS.md' : 'CLAUDE.md';
> --- `packages/brain/src/cli/setup.ts`

## Annotations

none
