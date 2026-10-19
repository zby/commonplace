---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Supermemory runtime baseline: public middleware, tool loops and MCP admission paths, with the memory engine opaque."
run-id: AAS-2026-10-19-supermemory-1cc18c778c48-01
reviewed-boundary: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
---

# Supermemory runtime report

## Runtime account

Supermemory's inspected public code submits content to a remote memory API and returns selected retained content to model applications. It does not implement the complete extraction and maintenance engine. The [boundary](boundary.md#boundary-and-evidence) fixes a complete public artifact but partial product loop. All source citations below use SRC-1 at the frozen revision. Newly inspected implementation includes the shared retrieval/cache/context helpers, OpenAI facade preparation, MCP authentication, upload/session state and mutation handlers, the Agent Framework context provider, and the tools publication workflow. Self-hosting documentation supplies design claims about opaque model components. No target code or tests were executed; operation, model compliance and benefit remain unobserved.

### Ordinary shipped invocation

The SDK playground's `runTypeScriptChat` dispatches a selected SDK, with caller messages, namespace and conversation ID. Its AI SDK middleware path constructs an OpenAI model, wraps it, supplies a fixed helpful-assistant system message and caller non-system messages to `generateText`, and returns response text. The application imposes a 120-second deadline and 2,048 output-token limit. The wrapper has its own 5-second pre-model memory-retrieval budget. These are separate control points, not a single transaction deadline (SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`, `packages/tools/src/vercel/index.ts`).

[RT-RTE-vercel-call](#rt-rte-vercel-call) traces the wrapper. Code, not the language model, decides whether to fetch a profile, query search, or both. The namespace and conversation ID are caller configuration. A latest-user-text key selects a wrapper-local cached memory string during non-user continuation calls. Otherwise the adapter requests profile/search, deduplicates and formats results, and replaces its own marked system-context block. The provider owns generation. After a successful response, configured persistence submits the original conversation plus generated assistant text. Submission is not awaited by the caller and is not atomic with model success. A later invocation can receive server-derived profile/search content, but extraction correctness and visibility timing are external contracts (SRC-1, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/conversations-client.ts`). The generation model and opaque backend models are separately recorded under [RT-CMP-openai-model](#rt-cmp-openai-model), [RT-CMP-extraction-model](#rt-cmp-extraction-model) and [RT-CMP-local-embeddings](#rt-cmp-local-embeddings).

### Alternate paths and four forcing cases

1. **Retrieval failure or no query text.** Both `doGenerate` and `doStream` catch retrieval errors. Default behavior calls the base model after stripping SDK-owned memory context; `skipMemoryOnError: false` throws before that call. Query/full mode with no user text clears context without making a retrieval request. This is not a universal requirement that every model call contain memories. Cached continuation calls also avoid retrieval. OpenAI Chat Completions and Responses have independent preparation and fallback branches, not the Vercel strictness switch: [RT-RTE-openai-call](#rt-rte-openai-call). Direct calls through the original provider remain possible; wrapper-local controls do not mediate them (SRC-1, `packages/tools/src/vercel/index.ts`, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/openai/middleware.ts`).

2. **Persistence filtering and completion.** `includeToolCalls: false` excludes structured tool-call and tool-result parts in Vercel conversion, but the earlier string-content branch copies non-system strings regardless of that option. The declared compatibility message type is imported from an external provider package, so supported reachability of a string-valued tool message is not established here. The converter's behavior is inspectable; a supported bypass is not demonstrated. Ordinary assistant text and user text can also describe tools. The option is not semantic secret removal. Stream persistence runs on transform flush and gathers text deltas only; an unconsumed or interrupted stream does not establish a committed save. The input eligibility predicate accepts user text or supported image files, but final serialization drops data URLs to `[image]`, not image bytes. Thus image eligibility is not image-understanding evidence (SRC-1, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/vercel/util.ts`, `packages/tools/src/vercel/index.ts`, `packages/tools/src/conversations-client.ts`).

3. **Forgetting and confirmation.** MCP IDs go directly to the forgetting API after shape checks. Content-only input searches up to five candidates; exact text can forget immediately, whereas approximate matches return candidates and require a subsequent call. That second call need not be a human approval. The legacy `add_memory` action can invoke the same forgetting handler. UI metadata and descriptions do not establish an enforced per-content human gate: [RT-RTE-mcp-save](#rt-rte-mcp-save), [RT-RTE-mcp-forget](#rt-rte-mcp-forget). These are narrower than the independently exported framework tools, which include document deletion and memory forgetting: [RT-RTE-tool-loop](#rt-rte-tool-loop) (SRC-1, `apps/mcp/src/server/tools/add-memory.ts`, `apps/mcp/src/server/tools/forget-memory.ts`, `packages/tools/src/ai-sdk.ts`).

4. **Alternate HTTP admission.** MCP calls authenticate through the bearer-token handler. File upload uses a different endpoint and a short-lived upload token, not a fresh account-token validation at that endpoint. Preparation binds account bearer and namespace into Durable Object storage. Upload consumes that capability transactionally before forwarding the multipart body. Failure after consumption cannot reuse that token. This supports bounded single-consumption, not exactly-once remote ingestion or universal namespace authorization: [RT-RTE-upload-session](#rt-rte-upload-session) (SRC-1, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/space-state.ts`).

### Controls, guarantees and remaining coverage

MCP's entry authenticates API keys through a cached session lookup or OAuth tokens through issuer/audience JWT verification. Invalid credentials return 401; recognized transient backend failures return 503 with retry guidance. Successful API-key validation can be reused for 60 seconds. The entry covers `/mcp`, `/mcp/` and rewritten root protocol requests; the exported legacy Durable Object is an empty compatibility class, not an inspected alternative request executor. The upload path is the material alternate above. Authentication owner: MCP entry/auth module. Enforcement: request dispatch plus external session/JWKS contracts. Guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. This does not establish immediate revocation or authorization of every selected namespace (SRC-1, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/auth/index.ts`, `apps/mcp/src/server/legacy-protocol-state.ts`).

The capability surface includes reading documents/profiles, adding content, forgetting facts, changing active space and preparing uploads. The current deployed grant set is not supplied. Code propagates the authenticated bearer to the API; UI access calculations and default-space selection are not the final backend permission decision. Explicit space arguments override active state, and app-only save takes an explicit namespace. An access-checked active-space setter therefore cannot establish isolation for all mutation tools. The inspected isolation envelope is request routing, actor-keyed Durable Object state and namespace-bearing API calls; provider/service infrastructure isolation is uninspected (SRC-1, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/space.ts`, `apps/mcp/src/server/auth/rbac.ts`, `apps/mcp/src/server/tools/set-active-tag.ts`, `apps/mcp/src/server/tools/save-memory.ts`).

Context management is selective insertion and replacement, not inspected full-history compaction. Vercel removes its marked blocks, reuses cached strings for continuations and preserves caller-authored instructions. MCP's requested context prompt bounds each static/dynamic fact list to eight and describes three other recent spaces; it returns a user-role message, not a forced model invocation. Framework tools return their results into host-controlled turn context. These paths are detailed in [RT-RTE-mcp-context](#rt-rte-mcp-context) and [RT-BAP-memory-context](#rt-bap-memory-context). No sub-agent frame or delegated remote worker is used by these inspected paths; this is not a repository-wide absence claim (SRC-1, `packages/tools/src/shared/memory-context.ts`, `apps/mcp/src/server/prompts/context.ts`, `apps/mcp/src/server/space-presentation.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts`).

Python lifecycle hooks are not presumed equivalent to JavaScript. The Agent Framework provider defaults storage off and can save system text when enabled; LiveKit branches between `llm_node` and realtime turn-completion hooks. [RT-RTE-python-context](#rt-rte-python-context) records the inspected provider. Available but uninspected Cartesia, Pipecat, Python OpenAI, Mastra and Voltagent consumer internals prevent a cross-adapter guarantee. Graph visualization, connector flows, other package publication workflows and non-public engine maintenance remain outside this selected runtime trace, not evidenced absences. The boundary includes these public paths where available; specialists can inspect them under SRC-1. No performance claim or exhaustive permission audit is established here.

Product changes enter through source/package publication, not a demonstrated self-revising runtime. [RT-RTE-publish-tools](#rt-rte-publish-tools) records the inspected npm release gate. Retained knowledge enters through automatic conversation submission, model-requested tools or caller/UI content; remote processing admission remains opaque. The runtime routes do not establish formulated-theory criticism, improved future capacity or exercised self-improvement. Those properties cannot be inferred from a save followed by retrieval.

## Shared records

### Components

#### RT-CMP-openai-model
Label: Playground OpenAI generation model

Identity: the OpenAI model selected by `MODEL_NAME`, default `gpt-4o-mini`. Representational form: distributed-parametric model state, consumed through generation APIs. Storage substrate: external provider; local code retains a client/model handle, not weights. Parameters changing during operation: uninspected provider internals; no weight-update request appears in the inspected caller. Exact version pinned: no immutable model revision is specified. Mutable endpoint resolving to another model: possible through environment selection and provider alias resolution; actual resolution uninspected. Implementation evidence: SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`.

> return process.env.MODEL_NAME ?? "gpt-4o-mini"
> --- `apps/sdk-playground/src/lib/chat-handlers.ts`

#### RT-CMP-extraction-model
Label: Server-side memory extraction models

Identity: documentation's proprietary production extraction models or operator-selected self-hosted model. Representational form: distributed-parametric. Storage substrate: remote service or local model provider, not implemented in this artifact. Parameters changing during operation: uninspected. Exact version pinned: not established for production or configured local endpoints. Mutable endpoint resolving to another model: afforded by provider/model configuration; actual versions and updates unknown. Design conclusion status: claimed. Evidence is doctrine/design, not inspected extraction execution (SRC-1, `apps/docs/self-hosting/overview.mdx`).

> In production, Supermemory runs its own proprietary models, purpose-tuned for long-horizon data understanding and memory extraction.
> --- `apps/docs/self-hosting/overview.mdx`

#### RT-CMP-local-embeddings
Label: Local embedding model

Identity: self-hosting default `Xenova/bge-base-en-v1.5`, 768-dimensional embeddings, with alternative providers. Representational form: distributed-parametric model parameters and generated numerical vectors; storage implementation uninspected in the non-public engine. Parameters changing during operation: uninspected. Exact version pinned: a model name is given, not an immutable weight digest. Mutable endpoint resolving to another model: configuration affords OpenAI, Gemini or Ollama alternatives; endpoint behavior uninspected. Design conclusion status: claimed. SRC-1, `apps/docs/self-hosting/overview.mdx`.

> **Built-in local embeddings** — default `Xenova/bge-base-en-v1.5` (768d) on your machine, no API key. Opt into OpenAI, Gemini, or Ollama instead — see [Embeddings](/self-hosting/embeddings).
> --- `apps/docs/self-hosting/overview.mdx`

### Operative objects

#### RT-OBJ-memory-cache
Label: Wrapper-local MemoryCache

Identity: `MemoryCache<string>` in the Vercel context. Form: natural-language formatted memories as value; symbolic namespace/conversation/mode/text cache keys and LRU selection. Substrate: in-process `LRUCache`, maximum 100 entries; not the durable memory store. New user turns fetch afresh; non-user continuations can reuse a nonempty value. Whitespace normalization means distinct requests can share a key; it is not a unique turn counter. No TTL or remote invalidation is configured in this class. SRC-1, `packages/tools/src/shared/cache.ts`, `packages/tools/src/vercel/middleware.ts`.

> private cache: LRUCache<string, T> = new LRUCache({ max: 100 })
> --- `packages/tools/src/shared/cache.ts`

#### RT-OBJ-space-state
Label: MCP SpaceState

Identity: `SpaceState` Durable Object storage, including active namespace and separately named upload sessions. Form: symbolic namespace, token hash, bearer, expiry; namespace selection affects which natural-language memories are later requested. Substrate: Cloudflare Durable Object storage. Active namespace object naming includes organization and user; upload objects use upload UUID. Active-space state is shared across that actor's requests, not isolated by conversation or OAuth client. SRC-1, `apps/mcp/src/server/space.ts`, `apps/mcp/src/server/space-state.ts`.

> return `space:${JSON.stringify([actor.organizationId, actor.userId])}`
> --- `apps/mcp/src/server/space.ts`

### Routes

#### RT-RTE-vercel-call
Label: Vercel automatic retrieval and conversation submission

Owner/progression: caller configures namespace, ID and mode; wrapper code retrieves/formats context; base provider executes generation; wrapper proposes conversation content to the API. Retrieval uses symbolic rules over natural-language messages/results, not an adapter-side model decision. Persistence defaults on. Code authorizes submission when `addMemory` is `always` and original input contains persistable user content. No per-content human approval is wired here; the caller can disable automatic submission, the API can reject it, and post-submit deletion/replacement semantics remain remote. Guidance is shipped filtering/formatting code plus optional caller template. Operating mode: open application requests; no answer oracle or improvement-trigger evaluator. Recovery: retrieval can fail open by default or throw when configured strict; save errors are logged/swallowed, with no rollback of an already returned answer. SRC-1, `packages/tools/src/vercel/index.ts`, `packages/tools/src/vercel/middleware.ts`, `packages/tools/src/shared/memory-client.ts`, `packages/tools/src/conversations-client.ts`.

- Immediate return: Base generation result, or stream with unchanged forwarded chunks and accumulated text deltas.
- Later read-back: Submitted conversation can produce server-side profile/search content for later wrapper calls; remote processing and durability are not verified.
- Delegated visibility: Provider receives transformed model parameters; memory service receives serialized non-system conversation and generated text, subject to conversion.
- Selection predicate: Mode chooses profile/query/full; query is last user text; namespace scopes API calls; continuation cache uses namespace, ID, mode and normalized user text.
- Invalidation or expiry: Marked blocks replaced/cleared; cache LRU capacity 100 with new-user refresh, not server mutation invalidation. Durable expiry is uninspected.
- Activation or effect: Model-input modification and API submission are wired; compliance, extraction and behavioral benefit unobserved.
- Evidence limits: No runtime trace, provider-package implementation or remote storage implementation; image bytes can be reduced to placeholders and structured tool payload omission is not semantic redaction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (msg.role === "system") continue
> --- `packages/tools/src/vercel/middleware.ts`

> if (typeof msg.content === "string") {
> --- `packages/tools/src/vercel/middleware.ts`

> content: formatConversationText(params.messages),
> id: params.id,
> dreaming: "instant",
> --- `packages/tools/src/conversations-client.ts`

Guarantee owner/enforcement: Vercel wrapper's retrieval catch and two persistence guards. Strength: best effort for memory supply/save; protocol for configured strict retrieval failure. Covered paths: wrapped generation and streaming; alternates: cache hit, no-text query, original model, framework tools and other adapters. External contracts: SDK abort propagation and service admission. Implementation guarantee conclusion status: wired. Operation guarantee conclusion status: uninspected. The five-second timer aborts the retrieval signal; bounded wall-clock completion still depends on the external SDK honoring it.

#### RT-RTE-openai-call
Label: OpenAI Chat and Responses middleware facade

Owner/progression: caller obtains a distinct facade; preparation cleans owned context, converts supplied history, optionally submits it and concurrently retrieves memories, then invokes the underlying provider create method. Responses injects into instructions; Chat updates messages. This differs from post-response Vercel submission: current generated output is not automatically appended by this inspected preparation. It can be submitted as history in a later request. Code proposes/admit-submits content under `addMemory`; caller can disable it, API can reject it, and no human per-content gate or local rollback is wired. Operating mode: open requests; answer oracle inapplicable, no reference comparison. SRC-1, `packages/tools/src/openai/index.ts`, `packages/tools/src/openai/middleware.ts`.

- Immediate return: Deferred API promise preserving access to the underlying prepared request/result; Chat or Responses output/stream is provider-owned.
- Later read-back: Submitted input history may enter later profile/search reads; completion of extraction remains remote.
- Delegated visibility: Memory service receives converted input history; provider receives cleaned messages or instructions plus selected memories.
- Selection predicate: Caller namespace/mode, latest user input and persistable-input checks; no-text non-profile branches skip retrieval but may still submit eligible history.
- Invalidation or expiry: Owned memory blocks removed/replaced on normal and fallback paths; durable expiry uninspected.
- Activation or effect: Facade preparation and API calls wired; no observed answer dependence.
- Evidence limits: Detailed conversion behavior is not treated as equivalent to Vercel filtering; the original supplied client remains callable.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (shouldPersist) operations.push(persistResponsesInput())
> --- `packages/tools/src/openai/middleware.ts`

> "Memory search failed for Chat Completions API; continuing without stale Supermemory context",
> --- `packages/tools/src/openai/middleware.ts`

Recovery is fail-open on caught retrieval failures and save logging, not the Vercel configurable strict control. No adapter-independent failure guarantee follows.

#### RT-RTE-tool-loop
Label: Model-selected framework memory tools

Owner/progression: shipped playground supplies tool definitions and system guidance; provider proposes symbolic tool names/arguments; AI SDK executor or explicit OpenAI driver dispatches operations, appends tool results and requests the next model step. The OpenAI driver loops at most eight times, then errors; AI SDK uses its own eight-step stop condition. These are bounded action loops for open user requests, not bounded experiments. The model proposes memory content; tool code submits it without inspecting its truth or requesting individual human approval. Caller controls exposed tools, API can reject changes; rollback is not wired in the inspected tool definitions. Natural-language tool descriptions guide proposals; retained outputs are remote documents/facts, not modified local model weights. No answer oracle is supplied. SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`, `packages/tools/src/ai-sdk.ts`.

- Immediate return: Tool success/error JSON enters turn context; shipped caller returns final text and tool trace, or max-step error.
- Later read-back: Add/document-add requests can affect later retrieval; forget/delete request removal, with backend semantics unresolved here.
- Delegated visibility: Provider sees schemas and tool outputs; executors receive model arguments and configured service credentials, not a separate autonomous worker context.
- Selection predicate: Model chooses tool and arguments; search tool requests hybrid search in configured namespace with clamped limit/threshold.
- Invalidation or expiry: Forget/delete tools exposed; no local conversation-context eviction is wired by these tool definitions.
- Activation or effect: Tool execution dispatch is wired; whether the model chooses the intended operation and service commits it is unobserved.
- Evidence limits: Destructive capability surface is not the deployed grant set; helper/backend deletion correctness is not established by tool naming.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> stopWhen: stepCountIs(8),
> --- `apps/sdk-playground/src/lib/chat-handlers.ts`

> documentDelete: documentDeleteTool(apiKey, config),
> documentAdd: documentAddTool(apiKey, config),
> memoryForget: memoryForgetTool(apiKey, config),
> --- `packages/tools/src/ai-sdk.ts`

#### RT-RTE-mcp-save
Label: MCP text-memory admission

Owner/progression: authenticated MCP client supplies content; `add_memory` resolves explicit/active/default space and invokes API add. App-facing `save-memory` requires explicit namespace and invokes the same client method. The server registers both; app visibility metadata is not an independent backend permission check. Trigger: tool invocation; proposed change: submitted natural-language content; code admits a request after schema/namespace processing, remote service owns actual retention. Human authorship/approval is unresolved for generic MCP callers. Caller may abstain, service may reject; no local undo/rollback is wired. Operating mode: open tool requests, no answer oracle or content-quality evaluator. SRC-1, `apps/mcp/src/server/tools/add-memory.ts`, `apps/mcp/src/server/tools/save-memory.ts`, `apps/mcp/src/server/client/index.ts`, `apps/mcp/src/server/server.ts`.

- Immediate return: Text/structured save result with ID; regular add also returns backend status. Exceptions become tool errors.
- Later read-back: API-created content can be consumed through search, profile and document tools; backend extraction completion is not established by the success label.
- Delegated visibility: Remote API receives content, namespace, bearer and source metadata; MCP host receives result, not a forced generation.
- Selection predicate: Explicit namespace overrides active/default for ordinary add; app save rejects missing explicit namespace.
- Invalidation or expiry: Forget route is separately exposed; creation has no local expiry or transaction rollback.
- Activation or effect: API add is wired; downstream behavioral activation unobserved.
- Evidence limits: Source/content truth checks, backend acceptance policy and human UI use are not supplied execution evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const result = await this.client.add(this.namespace, {
> content,
> metadata: { sm_source: MCP_SOURCE },
> })
> --- `apps/mcp/src/server/client/index.ts`

#### RT-RTE-mcp-forget
Label: MCP exact-or-ID forgetting admission

Owner/progression: MCP caller proposes IDs or content; handler validates IDs or searches content; exact match dispatches directly, approximate results return candidates. The caller, possibly a model, selects IDs on a subsequent call. Code can reject malformed/no-match requests; service can reject individual IDs. There is no mandatory human veto. Operating mode: open maintenance requests; exact text equality is a selection rule, not an answer oracle. Persisted change is remote forgetting, not deletion of this report's local context. Recovery returns partial errors; client disables mutation retries; no local restoration is wired. SRC-1, `apps/mcp/src/server/tools/forget-memory.ts`, `apps/mcp/src/server/tools/add-memory.ts`, `apps/mcp/src/server/client/index.ts`.

- Immediate return: Forgotten items/errors, or candidate IDs and instruction to call again; legacy add action delegates here too.
- Later read-back: Requested forgetting can change later API retrieval; actual visibility/invalidation semantics remain service-owned.
- Delegated visibility: Caller sees candidates and partial results; backend receives namespace-scoped IDs.
- Selection predicate: One to 100 deduplicated nonempty IDs, or exact equality among at most five search candidates; approximate-only matches are not automatically forgotten.
- Invalidation or expiry: Mutation requests remote invalidation; no clearing of already injected prompts or wrapper caches is wired here.
- Activation or effect: Forget request dispatch wired; removal from subsequent retrieval unobserved.
- Evidence limits: Two calls are not proof of human confirmation; this gate covers this handler and legacy delegation, not every framework forget/delete API.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const exact = candidates.find((c) => c.text === content)
> if (exact) return await forgetIds(deps, namespace, [exact.id])
> --- `apps/mcp/src/server/tools/forget-memory.ts`

> if (args.action === "forget") return forgetMemory(deps, args)
> --- `apps/mcp/src/server/tools/add-memory.ts`

Guarantee owner/enforcement: forgetting handler candidate branch. Strength: protocol, limited to no approximate-content auto-forget on that branch; ID and exact-match branches intentionally differ. External contract: backend search/forget returns valid scoped IDs/results. Implementation guarantee conclusion status: wired. Operation guarantee conclusion status: uninspected.

#### RT-RTE-mcp-context
Label: MCP active-space selection and requested context

Owner/progression: client requests context prompt; code resolves active/default space, fetches profile and namespace list concurrently, formats bounded facts and returns a user message. Selection changes use `set-active-tag`: supplied namespace must be accessible through the API namespace lookup before actor state is updated. The app picker merely presents options. Trigger/proposal: caller namespace selection; code/schema and API lookup admit or reject it. UI human selection is afforded, not established for every supported caller. Recovery: another setter call can replace selection; prompt failure returns an unavailable message. Operating mode: open requests, no answer oracle or improvement evaluator. SRC-1, `apps/mcp/src/server/prompts/context.ts`, `apps/mcp/src/server/space-presentation.ts`, `apps/mcp/src/server/tools/select-space.ts`, `apps/mcp/src/server/tools/set-active-tag.ts`, `apps/mcp/src/server/space.ts`.

- Immediate return: User-role context text with up to eight static and eight dynamic facts, omitted-fact counts and up to three other recent spaces; setter returns confirmation.
- Later read-back: Active namespace persists in actor Durable Object state and selects subsequent default tool/prompt reads; profile content itself comes from remote retained memory.
- Delegated visibility: MCP client receives prompt result and chooses whether/how to place it into model input; there is no automatic delegated model call.
- Selection predicate: Explicit tool namespace overrides active state; prompt uses active/default, preserves backend fact order, slices fact arrays and sorts other spaces by activity.
- Invalidation or expiry: Active space is replaceable with no configured expiry; context is rebuilt on prompt request, not a guarantee of clearing host history.
- Activation or effect: Durable setter and prompt construction wired; model use and compliance unobserved.
- Evidence limits: Sharing by organization/user is broader than conversation isolation; backend namespace permissions and host prompt placement remain external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const CONTEXT_FACT_LIMIT = 8
> const RECENT_SPACE_LIMIT = 3
> --- `apps/mcp/src/server/prompts/context.ts`

> if (!(await deps.getClient().getNamespace(namespace))) {
> --- `apps/mcp/src/server/tools/set-active-tag.ts`

#### RT-RTE-upload-session
Label: MCP single-consumption upload capability

Owner/progression: app tool resolves namespace; server mints upload UUID/token and stores bearer/namespace/expiry under a hashed token; HTTP upload consumes that record then forwards the multipart stream to remote document/file API. Trigger/proposed change: caller's selected file. Admission is capability/schema processing plus remote API acceptance, not inspected file-content quality approval. Interactive selection is afforded, but generic tool/HTTP callers do not establish a human gate. Caller/service can decline; network error after consumption requires a new capability. Operating mode: open uploads; no answer oracle. SRC-1, `apps/mcp/src/server/tools/prepare-file-upload.ts`, `apps/mcp/src/server/tools/upload-file.ts`, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/index.ts`, `apps/mcp/src/server/space-state.ts`.

- Immediate return: Preparation returns upload URL/token/expiry; upload forwards upstream status/body, or local 4xx/502.
- Later read-back: Uploaded content may later be available as remote documents/memories; retention/extraction unobserved.
- Delegated visibility: Browser/caller receives temporary upload capability; remote API receives stored account bearer and streamed file body.
- Selection predicate: UUID-shaped upload ID, bearer upload token, multipart content type, body presence, matching unexpired token hash and bound namespace.
- Invalidation or expiry: Two-minute TTL; transaction deletes session on valid consumption, expired reads delete it, alarm also deletes it.
- Activation or effect: Streaming upload request wired; server-side ingestion and resulting memory use unobserved.
- Evidence limits: Local single-consumption depends on Durable Object transaction semantics; it does not prove exactly-once remote writes or immediate account revocation enforcement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (session.tokenHash !== tokenHash) return undefined
> 
> await transaction.delete(UPLOAD_SESSION_KEY)
> --- `apps/mcp/src/server/space-state.ts`

Guarantee owner/enforcement: `SpaceState.consumeUploadSession`, checked before forwarding. Strength: protocol, conditional on Durable Object storage/transaction semantics. Alternate paths: ordinary text save uses authenticated MCP dispatch instead; direct service uploads are not mediated by this capability. Implementation guarantee conclusion status: wired. Operation guarantee conclusion status: uninspected.

#### RT-RTE-python-context
Label: Agent Framework before/after-run integration

Owner/progression: host invokes provider lifecycle hooks; code fetches profile/search before the run and extends instructions or system messages; optionally serializes input/response text and calls remote add after the run. Trigger: host lifecycle; proposal: extracted conversation text; admission: `store_conversations` flag and nonempty text, then service acceptance. Caller can disable storage, remote API can reject; exceptions log and return, no local rollback. Guidance is shipped mode/query/serialization code and caller context header/entity context. Operating mode: open application runs; no answer oracle or improvement evaluator. SRC-1, `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py`.

- Immediate return: Lifecycle side effects, not a replacement answer; provider failures log and allow continuation.
- Later read-back: Optional saved content can enter future remote profile/search; storage defaults false and includes eligible system text as well as user/assistant text.
- Delegated visibility: Host context gets formatted text; API gets conversation text under configured container tag/custom ID.
- Selection predicate: Mode chooses profile/query/full, last user message supplies query, context capabilities choose instructions versus messages.
- Invalidation or expiry: No history-compaction or remote-mutation invalidation demonstrated in this provider; host controls lifecycle cleanup.
- Activation or effect: Lifecycle methods and API submission wired; actual host invocation and improved behavior unobserved.
- Evidence limits: Helper/host behavior and cross-adapter parity are not established. LiveKit independently dispatches realtime versus ordinary LLM hooks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store_conversations: bool = False,
> --- `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py`

> if role not in ("user", "assistant", "system"):
> --- `packages/agent-framework-python/src/supermemory_agent_framework/context_provider.py`

The LiveKit hook distinction is implementation evidence, not an observed voice session (SRC-1, `packages/livekit-sdk-python/src/supermemory_livekit/agent.py`):

> if self._uses_realtime_model():
>     await self.memory.on_user_turn_completed(turn_ctx, new_message)
> --- `packages/livekit-sdk-python/src/supermemory_livekit/agent.py`

#### RT-RTE-publish-tools
Label: Tools package publication admission

Owner/progression: repository push to main changing tools package manifest triggers GitHub workflow; code compares local/npm version, conditionally builds, checks AI SDK compatibility and publishes with provenance. Trigger/proposal: a source/package version change supplied through repository maintenance, not runtime-generated revisions. The workflow admits publication when version differs and preceding steps succeed. Maintainers control source admission; branch protection/human review requirements are not established by this workflow. Job failure or unchanged version prevents publish; rollback/deprecation is not wired here. Operating mode: bounded release workflow; npm version is a release predicate, not an answer oracle. Persisted result is an npm package, later installed by consumers; not automatic replacement of running clients. SRC-1, `.github/workflows/publish-tools.yml`.

- Immediate return: CI build/compatibility/publication result, not agent answer.
- Later read-back: Consumers may install published package; actual deployment/reload uninspected.
- Delegated visibility: GitHub runner receives checkout/dependencies; npm receives public build/provenance.
- Selection predicate: Push on main touching package manifest; different local versus npm version; successful ordered build and compatibility steps.
- Invalidation or expiry: New package version changes future installation options; existing installations are not invalidated here.
- Activation or effect: Release pipeline declared; no supplied successful publication or deployment run.
- Evidence limits: Workflow inspection does not prove actual test success, repository approval rules or production rollout; other publication workflows not assessed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - name: Check against AI SDK 5, 6 and 7
>   if: steps.version-check.outputs.changed == 'true'
>   run: bun run test:compat
> --- `.github/workflows/publish-tools.yml`

### Claims

#### RT-CLM-engine-boundary
Label: Public integrations and non-public engine

Claimed operation: local binary provides ingestion, extraction and search, but its implementation is separate from this public repository. This limits all runtime explanations of server-side admission, contradiction handling, graph updates and embeddings. Doctrine/design conclusion status: claimed. SRC-1, `apps/docs/self-hosting/overview.mdx`.

> The SDKs and other components in the [public repository](https://git.new/memory) are open source; the downloadable self-hosted server binary is built from a separate, non-public codebase.
> --- `apps/docs/self-hosting/overview.mdx`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-memory-context
Label: Retained text into model context

Consumer: generation provider behind the Vercel wrapper, or host model receiving MCP prompt/tool results. Channel: system-context text in Vercel, instructions in OpenAI Responses, user-role prompt message in MCP, tool-result turns in the shipped tools loop. Force: interpretive information/instruction, not a hard execution constraint. The `readonly` marker protects neither truth nor instruction compliance; delimiter escaping only prevents retrieved Supermemory tags from terminating/nesting the SDK block. Horizon: remote retained content can cross requests/sessions; cache lasts wrapper lifetime, while host context persistence is host-owned. Routes: [RT-RTE-vercel-call](#rt-rte-vercel-call), [RT-RTE-openai-call](#rt-rte-openai-call), [RT-RTE-tool-loop](#rt-rte-tool-loop), [RT-RTE-mcp-context](#rt-rte-mcp-context). SRC-1, `packages/tools/src/shared/memory-context.ts`, `packages/tools/src/vercel/memory-prompt.ts`, `apps/mcp/src/server/prompts/context.ts`.

> const escaped = escapeMemoryContextDelimiters(normalized)
> return `${MEMORY_CONTEXT_START}\n${escaped}\n${MEMORY_CONTEXT_END}`
> --- `packages/tools/src/shared/memory-context.ts`

#### RT-BAP-space-selection
Label: Durable active namespace as routing authority

Consumer: MCP namespace resolver for later default-space tool/context requests. Channel: symbolic active namespace read from actor-keyed Durable Object storage. Force: code-level routing default, not model persuasion; explicit namespace overrides it and backend permissions still apply. Horizon: across actor requests until replacement, with no configured active-space expiry. This is distinct from memory text authority and from conversation-specific state. Route: [RT-RTE-mcp-context](#rt-rte-mcp-context). SRC-1, `apps/mcp/src/server/space.ts`, `apps/mcp/src/server/server.ts`, `apps/mcp/src/server/space-state.ts`.

> return explicit ?? (await getActiveNamespace())
> --- `apps/mcp/src/server/space.ts`

## Annotations

none
