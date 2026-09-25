---
type: agentic-system-analysis-result
description: 'Supermemory Vercel wrapper subsystem: profile injection and conversation
  upload with local cache semantics and uninspected remote learning bridge'
run-id: AAS-2026-09-25-supermemory-02
system: Supermemory
run-date: '2026-09-25'
result-disposition: complete
target-class: host integration
boundary-kind: subsystem-only
reviewed-boundary: 0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: wired
      note: Memory facts enter the model as contextual knowledge in the system channel;
        retained cache keys guide local selection. The static wrapper/configuration
        is outside accumulated-memory authority. Custom template semantics and model
        activation are excluded.
      records:
      - BAP-1
      - BAP-2
      - OBJ-5
      values:
      - knowledge
      - routing
    curation_operations:
      assessment: known
      basis: wired
      note: Normalized duplicate removal produces the cached context; configured LRU
        capacity forgets local cache entries. These classifications concern the adapter's
        retained cache only, not service fact revision, temporal decay or backend
        deduplication.
      records:
      - RTE-6
      - RTE-7
      - OBJ-2
      values:
      - dedup
      - decay
    distilled_form:
      assessment: not-determinable
      basis: null
      note: No inspected distillation links the uploaded traces to a retained derived
        artifact. Profile text alone does not establish a distilled form or explain
        included image processing.
      records:
      - OBJ-1
      - OBJ-3
      - RTE-8
      values: []
    faithfulness_tested:
      assessment: known
      basis: wired
      note: Inspected static tests check payloads and prompt delivery with mocks.
        This run retains no executed test of answer dependence on recalled content;
        no applies to inspected evidence, not all possible external evaluations.
      records:
      - ABS-1
      values:
      - 'no'
    learning_scope:
      assessment: not-determinable
      basis: null
      note: customId groups conversations and containerTag scopes retrieval; neither
        establishes task/project horizon for learning.
      records:
      - RTE-5
      - RTE-8
      values: []
    learning_timing:
      assessment: not-determinable
      basis: null
      note: Post-generation and stream-flush uploads are wired, but remote processing
        timing and a qualifying derived artifact are not established. Upload timing
        is not learning timing.
      records:
      - RTE-3
      - RTE-4
      - RTE-5
      - RTE-8
      values: []
    lineage:
      assessment: known
      basis: wired
      note: At this adapter boundary profile data and caller/model traces are imported,
        then normalized, selected, formatted or serialized. Remote pre-import derivation
        is excluded; serialization is not evidence of trace-extracted learned claims.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - RTE-2
      - RTE-5
      values:
      - imported
      - other-compiled
    read_back_direction:
      assessment: known
      basis: wired
      note: Wrapper requests retained service/cache data (pull); automatic pre-call
        selector supplies it to the base model without a model memory request (push).
        These are different consumers/operations within one chain.
      records:
      - RTE-2
      - BAP-1
      - BAP-2
      values:
      - pull
      - push
    read_back_signal:
      assessment: not-determinable
      basis: null
      note: Local push uses cache-key identity, mode and user-turn availability. Query/full
        also delegate selection using latest-user text; semantic-similarity comments
        do not expose the remote selection mechanism, preventing a complete signal
        set.
      records:
      - RTE-2
      - BAP-2
      - RTE-6
      values: []
    representational_form:
      assessment: not-determinable
      basis: null
      note: Text facts and context are natural language and access keys/envelopes
        are symbolic, but included image payloads are opaque non-text content not
        resolved by these controlled values. A complete set cannot be inferred from
        their URL/base64 envelopes.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-5
      values: []
    storage_substrate:
      assessment: known
      basis: wired
      note: Local LRU retains formatted strings; profile and conversation APIs expose
        service objects. Physical remote storage is outside scope; successful durable
        commits are not observed.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - RTE-2
      - RTE-5
      values:
      - in-memory
      - service-object
    trace_learning:
      assessment: not-determinable
      basis: null
      note: Local route acquires and serializes raw conversation traces. No inspected
        trace-to-durable-derived-memory-to-later-read bridge establishes learning;
        imported profile origin is opaque. This supports neither whole-route yes nor
        a service-wide no.
      records:
      - RTE-3
      - RTE-4
      - RTE-5
      - RTE-8
      values: []
    trace_source:
      assessment: not-determinable
      basis: null
      note: Conversation messages and optional tool events are upload inputs, but
        cannot be classified as sources of an unestablished qualifying learning route.
      records:
      - OBJ-3
      - RTE-5
      - RTE-8
      values: []
    write_agency:
      assessment: known
      basis: wired
      note: Calls automatically cache retrieved context and optionally submit conversation
        traces. Caller construction/configuration is not manual editing of retained
        memory; remote authoring is outside scope.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      values:
      - automatic
  scope: withSupermemory local formatted-context cache and automatic injection, imported
    profile/search service objects, and conversation upload payloads including images
    and optional tools; remote transformation/storage internals and caller template/model
    implementations excluded.
---

# Supermemory Vercel memory wrapper

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-supermemory-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/supermemory.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-supermemory-02/memory-report.md`

**Memory analysis report SHA-256:** 12db1364f74205b7fe8142a422f417265a5295fb6adb3268415f612942020c04

## Boundary and evidence

Target class: host integration. Boundary kind: subsystem-only. The selected subsystem is the Vercel AI SDK withSupermemory wrapper: its interception of doGenerate/doStream, profile/search retrieval, formatted cache, system-context injection, captured conversation upload, and shared helpers consumed there. Evidence is code-grounded at commit 0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f, inspected 2026-09-25. No execution, benchmark or causal experiment was performed.

Excluded: remote Supermemory extraction, update, forgetting, ranking and storage engine internals; base model/provider internals; host orchestration; other adapters, MCP/UI, explicit AI SDK mutation tools, other apps/connectors. The repository's product-wide engine claims do not characterize this inspected adapter. The packages/ai-sdk tools entry reexports another package; this analysis follows the operative packages/tools Vercel implementation.

Allowlist: https://github.com/supermemoryai/supermemory only, full-commit Git blobs accessed at `/home/zby/llm/commonplace/related-systems/supermemoryai--supermemory`; existing worktree HEAD differs and was not evidence. No prior reviews, ingests, retained results or audit prose were read. TypeScript runtime, Vercel-compatible caller model, network services and API credentials are dependencies, not observed grants.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | https://github.com/supermemoryai/supermemory | 0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f | implementation | Vercel wrapper and consumed shared/conversation helpers, selected static tests | `packages/tools/src/vercel/index.ts`; `packages/tools/src/vercel/middleware.ts`; `packages/tools/src/vercel/memory-prompt.ts`; `packages/tools/src/vercel/util.ts`; `packages/tools/src/shared/cache.ts`; `packages/tools/src/shared/memory-client.ts`; `packages/tools/src/shared/memory-context.ts`; `packages/tools/src/shared/prompt-builder.ts`; `packages/tools/src/conversations-client.ts`; `packages/tools/src/tools-shared.ts:290-441`; `packages/tools/src/shared/types.ts`; `packages/tools/src/shared/memory-client.test.ts`; `packages/tools/test/with-supermemory/unit.test.ts`; `packages/tools/test/with-supermemory/conversation-conversion.test.ts` | remote engine and provider implementation excluded; no deployed performance claim |
| SRC-2 | Git | https://github.com/supermemoryai/supermemory | 0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f | doctrine/design | README and comments/contracts | `README.md`; inspected source comments | declarations not observed behavior |

## Shared records

### Components

CMP-1 — withSupermemory Proxy wrapper, symbolic code intercepting model calls while preserving other model metadata/prototype fields. Conclusion status: wired. Caller invokes wrapped model; wrapper owns context transformation and best-effort capture, not task orchestration or tools execution. SRC-1 `packages/tools/src/vercel/index.ts:118-305`.

CMP-2 — Caller-supplied LanguageModel V2/V3. Wrapper delegates metadata and calls. Parameter changes, exact resolved weights, training and provider internal behavior each uninspected; the wrapper implements no parameter-update mechanism on these call routes. SRC-1 `packages/tools/src/vercel/util.ts:1-51`; `packages/tools/src/vercel/index.ts:151-184,246-250,295-298`.

CMP-3 — Configurable remote Supermemory service addressed using normalized base URL and caller API key. Profile and conversation endpoints are source-wired client dependencies. Server memory transformations, internal parametric components, authentication/isolation enforcement and durability are uninspected. No local embedding/ranker is inferred from search-result fields. SRC-1 `packages/tools/src/shared/memory-client.ts:28-71`; `packages/tools/src/conversations-client.ts:117-147`.

### Operative objects

OBJ-1 — Imported profile object: static/dynamic strings, optional buckets, nested searchResults.results with memory/chunk, metadata, updatedAt and similarity. Formatter consumes static/dynamic and search results, not buckets. Natural-language text and symbolic access/provenance fields; remote derivation unknown. SRC-1 `packages/tools/src/shared/types.ts:25-39,87-111`, `packages/tools/src/shared/memory-client.ts:128-185`.



OBJ-2 — Derived formatted memory string retained in per-wrapper in-memory LRU under container/customId/mode/normalized-user-text key. It is compiled from imported response, then reused by later continuation model calls. No guaranteed lifetime beyond wrapper process; no TTL. SRC-1 `packages/tools/src/shared/cache.ts:8-49`, `packages/tools/src/vercel/middleware.ts:288-383`.



OBJ-3 — Conversation upload envelope compiled from original call prompt plus captured assistant text. Raw acquisition/replay, not a locally distilled claim. Contains role-ordered text and images; optionally tool call/result payloads. Remote persistence intent is wired, durable commit/processing unknown. SRC-1 `packages/tools/src/vercel/middleware.ts:62-188`, `packages/tools/src/conversations-client.ts:9-19,39-64,117-147`.

> 	const bytes =
> 		value instanceof Uint8Array
> 			? value
> 			: value instanceof ArrayBuffer
> 				? new Uint8Array(value)
> 				: null
> 	return bytes && bytes.length > 0
> 		? `data:${mediaType};base64,${encodeBase64(bytes)}`
> 		: null
> --- `packages/tools/src/conversations-client.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

OBJ-4 — Original/transformed model prompt; only the managed memory block is accumulated-memory delivery here. Caller static instructions are excluded from the memory profile. SRC-1 `packages/tools/src/vercel/memory-prompt.ts:65-101`, `packages/tools/src/shared/memory-context.ts:17-41`.



OBJ-5 — Access/provenance envelope: cache key plus response IDs, updatedAt, similarity and arbitrary metadata. Symbolic envelope distinct from text/image payloads. Custom template receives surviving result metadata; default prompt does not. Cache key is an actual selector; remote metadata is available rather than automatically used for ranking. SRC-1 `packages/tools/src/shared/cache.ts:21-28`, `packages/tools/src/shared/types.ts:25-39`, `packages/tools/src/shared/memory-client.ts:166-185`.

> 	const promptData: MemoryPromptData = {
> 		userMemories,
> 		generalSearchMemories,
> 		searchResults: deduplicatedSearchResults,
> 	}
> 
> 	const memories = promptTemplate(promptData)
> --- `packages/tools/src/shared/memory-client.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

### Routes

RTE-1 — Construction. Caller supplies model and configuration. API key resolves from option or environment; missing key or empty customId throws before model invocation. Mode defaults profile; addMemory always; includeToolCalls false; skipMemoryOnError true. Context construction creates per-wrapper cache and client. The wrapper fixes retrieval timeout at five seconds; provider timeout remains external. Conclusion status: wired. Immediate return is Proxy; later consumers are its intercepted calls. External delegation visibility and remote scope enforcement uninspected; no retained-memory revision occurs at construction. SRC-1 `packages/tools/src/vercel/index.ts:118-149`; `packages/tools/src/vercel/middleware.ts:248-289`.

> 		verbose: options.verbose ?? false,
> 		mode: options.mode ?? "profile",
> 		addMemory: options.addMemory ?? "always",
> 		baseUrl: options.baseUrl,
> 		includeToolCalls: options.includeToolCalls ?? false,
> 		promptTemplate: options.promptTemplate,
> 		memoryRetrievalTimeoutMs: DEFAULT_MEMORY_RETRIEVAL_TIMEOUT_MS,
> 	})
> 
> 	const skipMemoryOnError = options.skipMemoryOnError ?? true
> --- `packages/tools/src/vercel/index.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

RTE-2 — Before-model retrieval/cache/injection. Last user textual content and mode select query; missing user text in non-profile mode clears owned context. A prompt ending in user role forces fetch; other steps reuse a truthy cached string. Profile API response is formatted/deduplicated by shared helpers, cached then injected. Errors/timeouts reach the enclosing generation branch: default continues with the managed memory block removed; skipMemoryOnError false throws before the base call. This is a fail-open policy, not an availability or truth guarantee. Conclusion status: wired. SRC-1 `packages/tools/src/vercel/middleware.ts:292-384`; `packages/tools/src/vercel/index.ts:154-180,216-244`; `packages/tools/src/vercel/memory-prompt.ts:65-101`.

> 	// Check if we can use cached memories
> 	const cachedMemories = ctx.memoryCache.get(turnKey)
> 	if (!isNewTurn && cachedMemories) {
> 		ctx.logger.debug("Using cached memories: ", {
> 			turnKey,
> 		})
> 		return injectMemoriesIntoParams(params, cachedMemories, ctx.logger)
> 	}
> --- `packages/tools/src/vercel/middleware.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

> 	const payload = queryText
> 		? JSON.stringify({
> 				q: queryText,
> 				containerTag: containerTag,
> 				include: ["static", "dynamic"],
> 			})
> 		: JSON.stringify({
> 				containerTag: containerTag,
> 				include: ["static", "dynamic"],
> 			})
> --- `packages/tools/src/shared/memory-client.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

> 							modelParams = injectMemoriesIntoParams(params, "", ctx.logger)
> 						} else {
> 							ctx.logger.error("Error during memory retrieval for generation", {
> 								error:
> 									memoryError instanceof Error
> 										? memoryError.message
> 										: "Unknown error",
> 							})
> 							throw memoryError
> --- `packages/tools/src/vercel/index.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

RTE-3 — Nonstream generation. Target model receives transformed params; wrapper waits for its result, extracts only text content and starts save when addMemory always and any original user message contains persistable text/image content. Save is not awaited before returning result. Model error is logged/rethrown, while capture errors are separately suppressed by RTE-5. Conclusion status: wired. The original prompt, not injected system memory, is handed to conversion. Generated reasoning/tool output is not newly captured as assistant text by this extraction helper. SRC-1 `packages/tools/src/vercel/index.ts:182-213`; `packages/tools/src/vercel/util.ts:80-109`; `packages/tools/src/vercel/middleware.ts:386-390`.

> 							saveMemoryAfterResponse(
> 								ctx.client,
> 								ctx.containerTag,
> 								ctx.customId,
> 								assistantResponseText,
> 								params,
> 								ctx.logger,
> 								ctx.apiKey,
> 								ctx.normalizedBaseUrl,
> 								ctx.includeToolCalls,
> 							)
> 						}
> 
> 						return result
> --- `packages/tools/src/vercel/index.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`



RTE-4 — Streaming generation. The base model stream runs after the same retrieval transformation; a TransformStream forwards every chunk and accumulates only text-delta content. Flush conditionally invokes save but does not await its promise. Returned stream completion therefore does not establish remote memory persistence. Cancellation/error paths have no separate captured save route in this wrapper; no finish-status admission predicate appears in flush. These are static bounds, not observed loss. Conclusion status: wired. SRC-1 `packages/tools/src/vercel/index.ts:246-298`.

> 							flush: async () => {
> 								if (
> 									ctx.addMemory === "always" &&
> 									hasPersistableUserContent(params)
> 								) {
> 									saveMemoryAfterResponse(
> 										ctx.client,
> 										ctx.containerTag,
> 										ctx.customId,
> 										generatedText,
> 										params,
> 										ctx.logger,
> 										ctx.apiKey,
> 										ctx.normalizedBaseUrl,
> 										ctx.includeToolCalls,
> 									)
> 								}
> 							},
> --- `packages/tools/src/vercel/index.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`



RTE-5 — Conversation conversion/upload. Original prompt messages become API message records, omitting system content, preserving eligible text/images and optionally original tool calls/results. Captured assistant text is appended. POST /v4/conversations uses bearer key, customId grouping and container tag, with 30-second timeout and redirect error. Non-OK status throws within helper; outer save logs/catches without propagating to completed generation. Backend append/diff/commit semantics are uninspected. Conclusion status: wired. API payload admission is caller/configuration-directed serialization, not fact validation; no local candidate comparison or content-truth oracle. SRC-1 `packages/tools/src/vercel/middleware.ts:20-188`; `packages/tools/src/conversations-client.ts:117-147`.

> 	for (const msg of params.prompt) {
> 		if (msg.role === "system") continue
> 
> 		if (typeof msg.content === "string") {
> 			if (msg.content) {
> 				messages.push({
> 					role: msg.role as "user" | "assistant" | "tool",
> 					content: msg.content,
> 				})
> --- `packages/tools/src/vercel/middleware.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

> 		body: JSON.stringify({
> 			conversationId: params.conversationId,
> 			messages: params.messages,
> 			containerTags: params.containerTags,
> 			metadata: params.metadata,
> 		}),
> 		redirect: "error",
> 		signal: AbortSignal.timeout(CONVERSATION_REQUEST_TIMEOUT_MS),
> 	})
> --- `packages/tools/src/conversations-client.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

RTE-6 — imported retained facts → normalized duplicate filtering with static > dynamic > search priority, mode-specific source inclusion → formatted context → cache → later model call. Narrow dedup, not semantic synthesis or backend memory mutation. SRC-1 `packages/tools/src/tools-shared.ts:321-441`, `packages/tools/src/shared/memory-client.ts:128-193`.

> 	const injectsProfile = mode !== "query"
> 
> 	return deduplicateMemories({
> 		static: injectsProfile ? data.static : [],
> 		dynamic: injectsProfile ? data.dynamic : [],
> 		searchResults: data.searchResults,
> 	})
> --- `packages/tools/src/tools-shared.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

> /** Normalize exact fact variants without attempting semantic/fuzzy matching. */
> export function normalizeMemoryFact(memory: string): string {
> 	return memory
> 		.trim()
> 		.replace(/^\[recent\]\s*/i, "")
> 		.replace(/^\[\d{4}-\d{2}-\d{2}\]\s*/, "")
> 		.trim()
> 		.replace(/\s+/g, " ")
> 		.toLowerCase()
> }
> --- `packages/tools/src/tools-shared.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

RTE-7 — configured LRU max=100 bounds local retained entries; get/set/clear methods exist, but wrapper calls only get/set and exposes no clear operation. No TTL configured; no upload-triggered invalidation. Local capacity forgetting maps to decay only at cache boundary. SRC-1 `packages/tools/src/shared/cache.ts:8-73`, `packages/tools/src/vercel/middleware.ts:331-383`.

> export class MemoryCache<T = string> {
> 	private cache: LRUCache<string, T> = new LRUCache({ max: 100 })
> --- `packages/tools/src/shared/cache.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

RTE-8 — Uninspected service bridge: uploaded raw conversations → remote derived profile/search memory → later RTE-2 read. Endpoints are wired independently; intervening transformation, durability, timing and causal identity are uninspected. This is a limitation record, not a claimed implemented bridge. SRC-1 `packages/tools/src/vercel/middleware.ts:151-188`, `packages/tools/src/shared/memory-client.ts:28-71`; SRC-2 `packages/tools/src/conversations-client.ts:1-7` claims backend diffing/append detection.



### Claims

CLM-1 — README product-level engine and benchmark claims. Conclusion status: claimed; remote transformation and performance remain uninspected at this adapter boundary. Local endpoint wiring does not establish extraction, temporal reasoning, forgetting or measured agent benefit. SRC-2 `README.md`.



### Evidenced absences

ABS-1 — no retained execution evidence here tests answer dependence on recalled content. Inspected tests use stubs/mocks and assertions on payload/prompt shape; no execution occurred. SRC-1 `packages/tools/src/shared/memory-client.test.ts:11-18,29-78`, `packages/tools/test/with-supermemory/unit.test.ts:25-48,140-304,539-655`, `packages/tools/test/with-supermemory/conversation-conversion.test.ts:12-54,60-110`.



### Behavioral-authority paths

BAP-1 — Retained memory text reaches caller model inside managed system-context block. Consumer CMP-2, channel system prompt, force delegated to provider/host hierarchy, horizon this model call with potentially repeated cached delivery. Internal delivery wired; actual activation and truth warrant uninspected. Delimiter escaping protects wrapper block syntax, not semantic trust. The readonly marker is text, not a separate model-enforced boundary. SRC-1 `packages/tools/src/shared/memory-context.ts:1-41`; `packages/tools/src/vercel/memory-prompt.ts:65-101`. > /** Prevent retrieved text from terminating or nesting the SDK-owned block. */
> function escapeMemoryContextDelimiters(memories: string): string {
> 	return memories.replace(SUPERMEMORY_TAG_PATTERN, (tag) =>
> 		tag.replace("<", "&lt;").replace(">", "&gt;"),
> 	)
> }
> --- `packages/tools/src/shared/memory-context.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

> 			if (prompt.role !== "system") return prompt
> 			const content = String(prompt.content ?? "")
> 			if (!injected) {
> 				injected = true
> 				return { ...prompt, content: replaceMemoryContext(content, memories) }
> 			}
> 			return { ...prompt, content: stripMemoryContext(content) }
> --- `packages/tools/src/vercel/memory-prompt.ts` @ `0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f`

BAP-2 — Symbolic wrapper selection reads container/customId/mode/user-message keys and last role to reuse cached formatted content. Force routing, horizon wrapper lifetime/cache capacity. It decides delivery availability, not which stored assertions are true. No timestamp field or TTL should be inferred merely from the input seed's generic cache description. SRC-1 `packages/tools/src/shared/cache.ts:1-80`; `packages/tools/src/vercel/middleware.ts:292-384`. 

## Runtime account

A host constructs the wrapper using its chosen model, API key, container tag and conversation identity. Each intercepted call retrieves or reuses memory, transforms system context, invokes the underlying model, then optionally schedules conversation upload. Terminal output is the base generation result or forwarded stream; it is not a confirmation of remote memory extraction or commit. Caller tools/host orchestration continue outside the boundary. Other model properties pass through the Proxy; direct use of the original model is an alternate caller path without these guarantees. Other SDK wrappers and explicit mutation tools are excluded, not presumed equivalent.

Four forcing cases are statically traced: missing construction identity/key rejects; empty-user non-profile input clears managed context; retrieval failure either clears and continues or rejects by option; upload failure cannot revoke the returned model result. Streaming cancellation versus normal flush is a further boundary qualification, not tested behavior. No dynamic check planned. Local wrapper tests or a mocked fetch could exercise these branches but would not reveal remote commit/dedup, actual model activation or deployment isolation. Static code supports the scoped characterization without dependencies, credentials or benchmarks.

Capabilities are network profile reads, conversation writes and one base model invocation per wrapped call. Caller configuration grants these routes; deployed API permissions, tenant separation and host tool approvals are uninspected. No local human approval gate controls capture. Logs can expose formatted memory under debug; actual logger/deployment policy is outside the observed boundary. Provider parameters and remote engine models are not pinned by this source analysis.

Revision admission is local only for prompt/cache replacement and conversation payload submission. Caller configuration/templates guide formatting and decide automatic save; code chooses included message forms and remote service decides any durable changes. Neither code nor user approves a semantically validated candidate memory fact here. No answer oracle or successor selection is implemented by these wrapper routes. Product benchmarking is outside this invocation mode, which serves open host requests. Local formatting/cache refresh should not be treated as criticism-driven improvement or remote trace-learning proof.


| Route | Immediate return / later read-back | Selector, expiry and visibility | Recovery/effect limits |
|---|---|---|---|
| RTE-1 | Proxy; later wrapped calls | Caller config; cache wrapper lifetime | Constructor errors before model; no memory effect yet |
| RTE-2 | Transformed prompt; cached string later reused | Mode/container/text/key/last role; no TTL; model receives selected text | Timeout/error clears or throws; no truth validation |
| RTE-3 | Model result; upload may affect later service state | Any persistable original user content and save option | Save unawaited; actual later service effect uninspected |
| RTE-4 | Forwarded stream; flush starts upload | Text-delta capture and same save gate | No separate canceled/error save handler; durability uninspected |
| RTE-5 | Logged success/failure; remote processing uninspected | Original prompt forms; system omitted; service sees serialized content | 30s request timeout; swallowed failure; no local retry/durable outbox in this helper |
| RTE-6 | Formatted text; later cached/model consumer | Mode and normalized exact variants; no local token cap | Template errors handled by wrapper; no semantic equivalence guarantee |
| RTE-7 | LRU get/set; future key lookup | max100, no TTL or upload invalidation | Dependency capacity contract; process loss loses local cache |
| RTE-8 | Uninspected bridge, no asserted local return | Remote transformation/retention selector excluded | No effect or recovery guarantee inferred from endpoints |

## Lens scoping

### Memory/context scope

Full lens: retrieved profile/search content, cached formatted context, conversation capture and later-consumer paths are the wrapper's purpose. Include all profile/query/full modes, generate/stream and error branches, original message/image/tool conversion and opaque remote boundaries. Exclude static prompts as accumulated memory and remote engine internals as implementation evidence.

### Epistemic scope

Brief lens: local implementation principally acquires/formats/delivers and uploads content; remote candidate generation/admission and base-model reasoning are inaccessible. Examine force versus warrant at system injection and the limited meaning of serialization/dedup/cache checks, without importing product-wide discovery or benchmark conclusions.

## Lens outputs

### Memory/context lens


RTE-2 stores the final template string after each successful fetch/build, including an empty string. This is automatic compilation of imported service content. Normalization strips leading recent/date labels, trims, collapses whitespace and lowercases only for duplicate keys; retained display text comes from the first winning item. Full mode privileges static over dynamic over search; query mode suppresses profile input to deduplication. New factual claims are not generated locally. RTE-6 operates on existing retained content to produce a retained cache representation, so dedup is warranted there without claiming service records were merged.



Profile arrays lack per-fact IDs/provenance in the declared shape. Default prompt formatting drops search metadata, timestamps and similarity. A custom template receives surviving search result objects with metadata preserved, but no default route interprets that metadata as reasons. Derived context does not create or require a rationale for prescriptions. If a fact itself contains an explanation, the text may survive; this is not a structured rationale-retention mechanism, and no later diagnosis route reads reasons separately.



RTE-3 and RTE-4 acquire raw conversation content after successful generation or stream flush, conditional on addMemory=always and some persistable user content anywhere in the original prompt. The gate is not limited to a newly added user turn. Text-only generated assistant output is captured; current-call reasoning, tool-call chunks, sources and files are not captured as assistant text. Historical tool calls/results in the original prompt are supported when opted in. The string-content shortcut serializes any non-system role directly, so includeToolCalls=false is specifically a filter on structured tool-call/tool-result parts, not an absolute rejection of all messages whose role is tool.



The original prompt, rather than the memory-enriched model prompt, is converted. All system messages are skipped, excluding caller static instructions as well as managed memory. Supported image file representations are preserved as URLs/data URLs; non-image files are not converted. Tool-result conversion flushes preceding content before inserting a tool message, preserving chronology. Nonserializable tool arguments become `{}`; unserializable outputs may become empty strings. These are acquisition losses, not learned summarization.



A successful model result returns without awaiting the save promise. Stream flush is declared async but similarly does not await save; no explicit cancellation/error persistence path is wired. A provider call failure reaches its error branch before capture/save. A stream that does not reach flush has no alternate save handler in this adapter. Even successful flush or return does not prove remote persistence, extraction or completion. The upload service response is parsed and logged; its processing status is not used to gate later retrieval.





There is no inspected local transformation from these traces into a durable distilled behavior-shaping artifact. OBJ-3 is the acquisition input to the uninspected service. Cache formatting consumes an imported response, not the captured conversation trace. Connecting those two solely from product naming would fabricate RTE-8. customId and containerTag identify/group requests without establishing a task horizon.



RTE-2 contains two consumer relations: the wrapper explicitly requests retained data from service/cache, then an automatic selector delivers resulting context to the caller-supplied base model. The model does not request a memory read. Thus pull and push both occur, at different points in the chain. Profile mode uses containerTag without q; query/full use containerTag plus latest user text. customId is part of the local cache key and conversation grouping, but is not submitted to /v4/profile. Consequently it does not establish conversation-specific remote read isolation.



For continuation cache hits, normalized text plus container/customId/mode selects an actual retained entry. This supports identifier-based local push selection. A last-role user message bypasses reuse; otherwise the key can match content from an earlier occurrence of the same normalized text because there is no turn counter or TTL. Empty cached strings are stored but fail the truthiness reuse test. On cache misses the server's internal selection signal remains uninspected. Comments claiming semantic similarity do not prove embeddings, lexical inference or judgment-based selection. Read-back signal therefore remains not-determinable as a complete union across modes.

Default formatting delivers all surviving profile or search strings with headings and bullet lists; there is no local truncation/count/token budget. All modes request static and dynamic fields at the API surface. Query mode hides profile output after retrieval; profile mode suppresses the default search-text section. The custom template additionally receives the surviving searchResults array computed from the raw response even in profile mode if the server returns such results. The type comment promising an empty array in profile mode is therefore contingent on service behavior, not enforced by a local mode check.

If latest-user text is missing in query/full, RTE-2 removes stale context. This includes an image-only latest user message despite images being persistable on RTE-5. Profile can fetch without user text. Fetch errors/abort or template errors flow to wrapper handling: default fail-open strips managed memory and invokes the base model; configured fail-closed propagates error before model call. The fixed 5-second timer aborts fetch; it is not a general CPU-time bound for arbitrary synchronous template code. Neither retrieval failure nor a later save automatically invalidates older cache entries.



Delivery is wired. Model activation, answer faithfulness and benefit are unobserved. Static tests assert context strings appear or are reused and mock errors/timeouts; they do not supply executed behavioral evidence. Returned IDs/similarity can support caller filtering through custom templates, but that affordance is not an inspected deployed ranking route.



The fourteen axes use the same adapter-and-service-interface boundary. Storage is in-memory plus service-object, not a claim about server database/index choices. Lineage is imported at entry and other-compiled locally; no unknown upstream extraction is promoted to an established lineage. Knowledge authority follows the contextual fact consumer; system placement does not itself turn facts into validated instructions or model learning. Routing authority belongs to retained cache access structure. Static system instructions and caller configuration are not accumulated-memory artifacts.

Curation is dedup for RTE-6 and decay for RTE-7's capacity-driven cache forgetting. The cache replacement/managed-block replacement machinery does not establish evolution of a semantic fact, retained-history invalidation, promotion or synthesis. The LRU dependency's implementation was not inspected; max=100 is the wired capacity contract, not an observed eviction experiment. Remote semantic curation remains excluded. The known set concerns only curation implemented by this wrapper over its retained representation.

Images prevent a complete representational-form mapping; JSON/base64 does not decide the form of the content the service consumes. The profile's natural-language/static/dynamic labels do not close that gap. Trace-learning axes all retain the same uncertainty: upload inputs/timing and later profile outputs cannot establish an intervening qualifying learning route. No learning scope is inferred from a conversation ID. Faithfulness no records the bounded lack of retained execution evidence; it does not deny external benchmark existence.


### Epistemic lens

1. Boundary and claim: SRC-1 wrapper plus SRC-2 claims; no observed candidate or controlled run. CLM-1 broad memory-engine account remains outside the operative source boundary. Local content can carry assertions/preferences, but its upstream rationale, criticism and truth status are uninspected.

2. Objects: OBJ-1 imported profile/search may contain truth-apt statements. OBJ-2 formats/selects them; OBJ-4 gives them a system channel without new evidence. OBJ-3 serializes conversation traces with deliberate omissions; neither serialization nor a successful response establishes durable accurate knowledge. Addressability is limited to response fields, source strings and wrapper configuration; remote proposition identity and theory revision remain uninspected.

3. Authority ledger:

| Function | Architectural status | Content relation and admission | Authority limit |
|---|---|---|---|
| RTE-2 acquisition | implemented | HTTP response imported using caller identity/configuration | server warrant and schema soundness not established by JSON parsing |
| RTE-2 formatting/selection | implemented | non-ampliative intent; mode/dedup/template choose delivered text | template can alter text; local selection adds no truth test |
| RTE-2 operational disposition | implemented | cache insertion and managed-block replacement | routing/capacity policy, not epistemic acceptance |
| RTE-3, RTE-4 model consumption | implemented at client boundary | supplied model generates with transformed prompt | content use and candidate criticism inside model uninspected |
| RTE-5 acquisition/retention request | implemented | serializes selected original messages and response text | remote acceptance, transformation and retention uninspected |

4. Lifecycle: no local discovery-lifecycle candidate is established by pure retrieval/formatting. Upstream statements and generated model text may involve ampliative inference, but their formulation, criticism and warrant are uninspected. Observed candidate state: no instance observed for generation, tests or acceptance. Cache admission has no truth-apt candidate criterion. Host actions, stored facts and empirical benchmark outcomes cannot be derived from a POST endpoint.

5. Doctrine comparison: CLM-1 can describe a larger deployed product; this repository subsystem establishes only client wiring. Readonly tags and system role concern operational presentation, not reliability of statements. Best-effort capture cannot support an exactly-once or completed-write claim.

6. Bounded conclusion: the adapter connects remote content to model calls and host traces to a remote write API. It does not expose enough of the engine/model process to classify content-directed criticism, conjectural learning or epistemic improvement. No system-wide grade follows from this narrow lens.

## Reconciliation

Verified complete report, run/source/boundary, report hash and unchanged input/method. Mappings: MEM-OBJ-1 → OBJ-5; MEM-RTE-1 → RTE-6; MEM-RTE-2 → RTE-7; MEM-RTE-3 → RTE-8; MEM-ABS-1 → ABS-1. OBJ-5 is the new access/provenance facet; existing object identities remain unchanged.

All eight integration issues accepted: keep opaque images; register formatting/cache maintenance and explicitly uninspected service bridge; correct seed timestamp suggestion to no timestamps/TTL; distinguish structured tool opt-in from generic string tool-role conversion; distinguish image upload from textual query; preserve unawaited saves/flush-only trigger and no processing barrier; separate default metadata omission from custom-template affordance and unenforced profile comment; remote profile uses containerTag/q without customId; curation decay means only configured local LRU capacity. No conflict remains. The known authority set is contextual knowledge/routing, not an inference of instruction force from system placement. Other template semantics remain excluded. Narrower claims supersede informal input seeds without reassigning records.

## Bounded synthesis

The strongest supported contribution is a concrete retrieval-before-generation and capture-after-response integration, including repeated-call cache reuse and both model-call forms. It reduces host integration work while leaving memory-engine semantics outside this boundary. Default fail-open retrieval and unawaited capture prioritize model output over confirmed memory operation; deployments needing write completion require an external contract not established here.

Conjectural learning, reflective self-representation and self-improvement each remain uninspected. Retained context wiring alone does not show criticism of an operative theory or attributable improved capacity. Cache metadata records selection state, but no self-theory of the wrapper or evidence-responsive change to its machinery is established. Remote engine/model evidence, retained upload-completion traces and controlled host-memory interventions would alter separate parts of this assessment.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Remote engine excluded | CMP-3, RTE-2, RTE-5 | client requests/responses | extraction, retention, forgetting, ranking or tenant guarantees | pinned engine source and operating contract |
| Provider/host excluded | CMP-2, BAP-1 | model-call interface | activation, factual correctness or task benefit | controlled host/model traces |
| Save is unawaited | RTE-3, RTE-4, RTE-5 | asynchronous wrapper calls | model completion implies memory commit | remote acknowledgment/awaited lifecycle evidence |
| Source-only analysis | CLM-1 | code/docs | measured performance and causal improvement | retained experiments under explicit boundary |
| Opaque image and selector semantics | OBJ-3, OBJ-5, RTE-2, RTE-8 | API envelopes and local formatting | complete form/signal and trace-learning profile | remote transformation and payload interpretation evidence |

## Verification and blockers

### Semantic verification

Checked wrapper boundary, original-model alternate path, constructor/retrieval/save forcing branches, generate/stream differences, API authority versus deployment grants, distributed-parametric opacity, local serialization versus semantic admission, and absence of observed model/engine behavior. Checked profile scope against every call branch and included cache/service-interface object. RTE-6 dedup and RTE-7 capacity forgetting are local curation, not remote fact mutation. RTE-3/RTE-4/RTE-5 raw trace acquisition does not establish RTE-8 transformation, so every dependent learning axis remains not-determinable. Included image payloads prevent complete representation mapping. Local keyed push and remote query selection coexist; no invented embedding/judgment signal closes the uncertain union. Pull wrapper and push model are distinct consumers. ABS-1 is bounded to inspected static tests and this no-execution run. All report quotes integrated into canonical records once; activation, performance and causal benefit remain unobserved.

### Deterministic validation

Target exact result: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-supermemory-02/result.md`; full validation and guarded source-anchor/quote verification after integration.

### Blockers

none
