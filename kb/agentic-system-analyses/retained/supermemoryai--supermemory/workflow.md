---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Supermemory workflow account: the shipped OpenAI playground tool loop from HTTP request through memory operations to an assistant response."
run-id: AAS-2026-10-19-supermemory-1cc18c778c48-01
reviewed-boundary: f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe
---

# Supermemory workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the SDK playground's `ts-openai-tools` chat path: an HTTP request starts a bounded model/tool loop, memory-operation results return to the model, and a tool-free model response becomes an HTTP assistant message. It was selected because a shipped caller owns progression and delivery explicitly, rather than leaving the coordination entirely to an external framework. It refines [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop), not a newly discovered route. Search, save and retry are possible decisions within this loop, not an observed sequence or a mandatory itinerary.

The [boundary](boundary.md#boundary-and-evidence) remains a complete public artifact but partial product loop. Additional implementation coverage under SRC-1 comprises `apps/sdk-playground/src/app/api/chat/route.ts`, the tools prompt in `apps/sdk-playground/src/lib/sdk-registry.ts`, and parsing, dispatch, search and add functions in `packages/tools/src/openai/tools.ts`. The driver and deadline were inspected in `apps/sdk-playground/src/lib/chat-handlers.ts`. These files establish wiring, not successful execution. No target was run. Remote extraction, storage admission and retrieval quality remain outside the available implementation, as [RT-CLM-engine-boundary](runtime.md#rt-clm-engine-boundary) records.

### Request and handoff to the model

The HTTP POST handler invokes browser-trust and request-parsing helpers, resolves API keys, and checks SDK availability before calling the TypeScript driver. Missing keys or an unavailable SDK returns a 400 response. This inspection establishes those calls and branches, not a full audit of the validation helpers. The driver rejects an invalid TypeScript SDK and dispatches `ts-openai-tools` with caller messages, namespace and an abort signal. Although the HTTP request includes a conversation ID, that ID is not passed to this tool driver; it does not identify a server-side conversation for this path (SRC-1, `apps/sdk-playground/src/app/api/chat/route.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts`).

The driver constructs a provider client and a memory-tool executor with separate API keys. The executor receives the configured namespace and optional service base URL. The model receives tool definitions, the shipped tools system prompt and caller messages excluding caller system messages. The generation model is [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model). The prompt requests proactive recall and saving; it is model guidance, not a code-enforced precondition on final answers (SRC-1, `apps/sdk-playground/src/lib/sdk-registry.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts`):

> Before answering questions about the user, their preferences, or past context, search memories or get profile first. When the user asks you to remember something, use addMemory.
> --- `apps/sdk-playground/src/lib/sdk-registry.ts`

### Model proposal, tool dispatch and return

Each iteration asks the provider for a completion with the accumulated conversation and the seven exposed memory/document tool definitions. The model chooses whether to call tools and supplies names and JSON arguments. The driver appends the assistant message, dispatches its tool calls, builds trace entries and appends the returned tool messages before continuing. This is delegation to fixed operation executors, not to autonomous sub-agents with separate task frames (SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`, `packages/tools/src/openai/tools.ts`).

The executor parses JSON, requires an object, checks required fields for nonempty strings and dispatches recognized names. It does not implement complete JSON Schema validation or evaluate proposed content for truth. Within one model response, operations run concurrently, so a batch containing save and search is not an ordered save-then-read transaction. Results preserve call IDs for the provider (SRC-1, `packages/tools/src/openai/tools.ts`):

> const results = await Promise.all(
> toolCalls.map(async (toolCall) => {
> const result = await executeToolCall(toolCall)
> return {
> tool_call_id: toolCall.id,
> role: "tool" as const,
> content: result,
> }
> }),
> )
> --- `packages/tools/src/openai/tools.ts`

For recall, `searchMemories` passes model-supplied query text to namespace-scoped hybrid search with a clamped limit and default threshold. It returns the service's results and count in success JSON. The adapter does not independently verify relevance. For retention, `addMemory` submits the model's string as content and requests immediate processing. A successful SDK return produces success JSON, not proof of completed extraction or later visibility (SRC-1, `packages/tools/src/openai/tools.ts`):

> const response = await client.add(namespace, {
> content: memory,
> dreaming: "instant",
> })
> --- `packages/tools/src/openai/tools.ts`

The model proposes the memory content; code admits the request through argument checks and dispatch; the remote API can reject it. There is no per-content human approval step in this driver. The user initiates the request, but that alone does not approve each generated save or destructive operation. The tools prompt and descriptions shape proposals; they do not supply an expected-answer oracle. This is an open-request workflow, not an experiment or an improvement-trigger evaluator. Later read-back requires the service to retain and return content on a future tool request; no local model-weight update or automatic successful read-after-write follows from the loop (SRC-1, `apps/sdk-playground/src/lib/sdk-registry.ts`, `packages/tools/src/openai/tools.ts`; [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop)).

### Rejection, recovery and its boundary

A supported recoverable branch is a syntactically valid object missing a required string, such as a search call with `{}`. The executor returns failure JSON without calling that operation. The driver can parse those original arguments for its trace, append the error tool message and ask the model again. The model owns any revised proposal; neither retry nor eventual success is forced. Service exceptions in search/add similarly become failure objects available to a later iteration (SRC-1, `packages/tools/src/openai/tools.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts`):

> if (missing?.length) {
> return JSON.stringify({
> success: false,
> error: `Missing required arguments for ${functionName}: ${missing.join(", ")}`,
> })
> }
> --- `packages/tools/src/openai/tools.ts`

Recovery is not uniform for every executor rejection. The executor tolerates blank arguments as an empty object and returns failure JSON for malformed JSON. But the playground driver subsequently parses the original argument string again without a catch when building its trace. A malformed or blank argument string can therefore abort the driver instead of reaching the next model turn, even after the executor returned a tool result. This is a source-supported edge path, not an observed provider emission. It prevents interpreting executor-level error handling as an end-to-end recovery guarantee (SRC-1, `packages/tools/src/openai/tools.ts`, `apps/sdk-playground/src/lib/chat-handlers.ts`):

> args: JSON.parse(call.function.arguments),
> --- `apps/sdk-playground/src/lib/chat-handlers.ts`

The driver permits eight provider iterations. Exhaustion throws; a missing first response message also breaks into that same error. The outer deadline races the operation against 120 seconds and aborts its signal on timeout. It is not a transaction over remote tool effects: the tool executor receives no such signal, and no compensating rollback is wired for earlier successful mutations. Failure can thus leave remote effects without an assistant success response. Actual cancellation and remote completion remain unobserved (SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`, `packages/tools/src/openai/tools.ts`).

### Delivery and verification limits

A completion without tool calls terminates the driver and returns its text, trace and an empty memory-debug array. Even empty content is accepted as an empty string. The HTTP handler packages this result as `ok: true` with an assistant message; thrown errors instead become error JSON, with 504 for the recognized timeout cases and 500 for ordinary driver errors (SRC-1, `apps/sdk-playground/src/lib/chat-handlers.ts`, `apps/sdk-playground/src/app/api/chat/route.ts`):

> return { text: choice.content ?? "", toolTrace: trace, memoryDebug: [] }
> --- `apps/sdk-playground/src/lib/chat-handlers.ts`

Delivery here means construction of the HTTP response, not verified browser display or user acceptance. There is no intervening answer-quality checker in this inspected success branch. Argument checks can reject operations; the provider's no-tool response decides termination; neither mechanism checks answer correctness or that instructed recall occurred. Tool results remain in the accumulated conversation for subsequent iterations, with no driver-side summarization or trimming. Their authority is model interpretation, as [RT-BAP-memory-context](runtime.md#rt-bap-memory-context) distinguishes from hard execution constraints. No supplied trace establishes that a delivered answer depended on retained content or benefited from it.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tool-loop](runtime.md#rt-rte-tool-loop)

Workflow selection: the explicit OpenAI playground driver, rather than the AI SDK alternative within this route.

Handoff ordering: calls within one provider response execute concurrently; the next provider request waits for the batch and trace assembly. There is no enforced intra-batch dependency order.

Verification and recovery: missing required strings in valid JSON objects can return tool errors into a subsequent iteration. Malformed or blank original argument JSON can instead fail during trace assembly. A final tool-free response requires no answer-quality acceptance step.

Delivery boundary: the driver's return becomes an HTTP assistant-message response; mutation rollback, browser receipt, human acceptance and successful remote read-back are not established. The eight-iteration bound and outer deadline do not make the workflow atomic.
