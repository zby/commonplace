---
type: kb/types/agentic-system-analysis-result.md
description: 'Tardigrade inference and compaction subsystem: event-derived model progression,
  summary checkpoints and schema correction with bounded host and provider guarantees'
run-id: AAS-2026-09-25-tardigrade-01
system: Tardigrade
run-date: '2026-09-25'
result-disposition: complete
target-class: embedded inner runtime
boundary-kind: subsystem-only
reviewed-boundary: 1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: known
      basis: wired
      note: History/summary provide evidence; correction text instructs; retained
        lifecycle/mode/schedule facts govern eligibility and routing; the retained
        output declaration supplies validation. Provider consumption is wired, activation
        unobserved.
      records:
      - OBJ-4
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      - RTE-6
      - BAP-1
      - BAP-2
      values:
      - knowledge
      - instruction
      - enforcement
      - routing
      - validation
    curation_operations:
      assessment: known
      basis: wired
      note: Summary replaces prior summary and reduces history supplied to the model;
        successful repair suppresses replaced rejection/feedback while preserving
        raw history. This is no claim of factual correction or deletion.
      records:
      - RTE-3
      - RTE-4
      - OBJ-7
      values:
      - consolidate
      - evolve
      - invalidate
    distilled_form:
      assessment: known
      basis: wired
      note: Summary/error/feedback text plus derived checkpoint boundaries, rejection
        modes, replacement relations and retry schedule metadata; opaque attachment/continuation
        replay is not classified as distilled learning.
      records:
      - OBJ-2
      - OBJ-4
      - RTE-2
      - RTE-3
      - RTE-4
      values:
      - natural-language
      - symbolic
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      note: No retained execution evidence is supplied; static wiring cannot establish
        tested dependence on recalled content or faithful summarization.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      values: []
    learning_scope:
      assessment: not-determinable
      basis: null
      note: Correction/retry is bounded by turn/epoch and compaction crosses turns
        in a conversation. These are not an established task/project partition.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      values: []
    learning_timing:
      assessment: known
      basis: wired
      note: Summary, rejection, replacement and retry derivations occur in the active
        runtime progression before subsequent model attempts.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      values:
      - online
    lineage:
      assessment: not-determinable
      basis: null
      note: Trace-extracted summary and compiled control are established; external
        ingress, attachment and delegated-feedback origins are not determined by these
        consumer contracts.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-4
      - OBJ-5
      - OBJ-6
      values: []
    read_back_direction:
      assessment: known
      basis: wired
      note: 'Automatic history, checkpoint, correction and compatible continuation
        supply is push to model/runtime consumers. The execution bridge explicitly
        requests selected attachment bytes from ObjectStorage: pull to that named
        bridge consumer.'
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      - RTE-6
      values:
      - push
      - pull
    read_back_signal:
      assessment: known
      basis: wired
      note: Latest checkpoint and budget/suffix selection are coarse; boundary IDs,
        turn/epoch/attempt/rejection identity and provider/protocol/model matches
        select concrete retained parts. No semantic retrieval selector on these routes.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-6
      values:
      - coarse
      - identifier
    representational_form:
      assessment: not-determinable
      basis: null
      note: Natural-language and symbolic parts are established, but arbitrary attachment
        bytes and provider-native payload parts prevent a complete classification
        of operative content from their containers.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-4
      - OBJ-5
      - OBJ-6
      values: []
    storage_substrate:
      assessment: known
      basis: wired
      note: Logical EventLog/ObjectStorage ports plus incremental projection state;
        physical backend substrate remains outside the boundary.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-4
      - OBJ-5
      - OBJ-6
      - OBJ-7
      values:
      - service-object
      - in-memory
    trace_learning:
      assessment: known
      basis: wired
      note: Automatic summaries are retained for later context. Derived validation
        errors, replacement relations and retry schedules also persist and shape later
        work; unchanged logs and lossless continuation encoding alone do not establish
        learning. No improvement claim follows.
      records:
      - RTE-3
      - RTE-4
      - RTE-2
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: wired
      note: Compaction consumes selected event trajectory including tool calls/results;
        completion validation and retry scheduling consume model outcomes and accumulated
        attempts.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      values:
      - event-streams
      - trajectories
      - tool-traces
    write_agency:
      assessment: not-determinable
      basis: null
      note: Internal summary, rejection and schedule writes are automatic. Included
        ingress and delegated feedback may have external authors; their origin is
        excluded, so a complete automatic/manual union is unsupported.
      records:
      - OBJ-1
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      values: []
  scope: Accumulated event history and derived runtime control, compaction checkpoints,
    output rejection/repair feedback, referenced attachment bytes and provider continuation
    consumed by the embedded infer/compact subsystem; service interfaces and transient
    projections included, physical stores and external producer implementations excluded.
---

# Tardigrade inference and compaction subsystem

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/tardigrade.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/memory-report.md`

**Memory analysis report SHA-256:** 96e2a6b2eb6c559d0ec1f027a21a0528e17710a4ef870b5d44e9831a09954dd9

## Boundary and evidence

Evidence basis: source code and shipped documentation at 1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267, inspected 2026-09-25; no observed run or causal experiment. Target class: embedded inner runtime. Boundary kind: subsystem-only. Includes the agent package's infer composition/machine, model request/execution bridge, conversation projection, compaction wrapper/summary generation, and output-contract correction routes. Consumed event/object/provider-continuation payloads are included; physical storage and providers are dependencies.

Excludes Bun/Cloudflare/worker-loader host durability/isolation, CLI/API/UI, actor transport/delegation implementations, arbitrary tool/code effects, and actor verification/optimization tooling. This review does not establish whole-framework crash safety, cross-actor grants, sandboxing or improvement machinery. Source allowlist is https://github.com/clavia-labs/tardigrade only; full-commit reads at `/home/zby/llm/commonplace/related-systems/clavia-labs--tardigrade`. No worktree, ingest, prior analysis or linked external evidence. Dependencies include Effect, model services and an enclosing executor; not installed or executed.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/clavia-labs/tardigrade` | 1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267 | implementation | infer, request bridge, compaction, output schema/repair, projection and supporting model lock | `packages/agent/src/component/infer/index.ts`; `packages/agent/src/component/infer/machine.ts`; `packages/agent/src/component/infer/view.ts`; `packages/agent/src/model/execution/index.ts`; `packages/agent/src/model/request.ts`; `packages/agent/src/component/compact/index.ts`; `packages/agent/src/component/compact/model.ts`; `packages/agent/src/output/contract.ts`; `packages/agent/src/component/repair.ts`; `packages/agent/src/projection/transcript.ts`; `packages/model/src/lock.ts:1-145`; `packages/core/src/log/service.ts`; `packages/agent/src/log/events.ts`; `packages/agent/src/log/message.ts`; `packages/agent/src/component/messages.ts`; `packages/agent/src/component/compact/context.ts`; `packages/agent/src/projection/messages.ts`; `packages/agent/src/projection/tokens.ts`; `packages/agent/src/object/storage.ts`; `packages/agent/src/model/continuation.ts`; `packages/agent/src/model/execution/objects.ts`; `packages/agent/src/model/execution/prompt.ts`; `packages/agent/src/model/execution/continuation.ts`; `packages/model/src/stream/collect.ts` | host/provider and runtime outcomes excluded |
| SRC-2 | Git | `https://github.com/clavia-labs/tardigrade` | 1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267 | doctrine/design | README framework and durability claims, shipped instructions | `README.md`; `packages/agent/src/component/compact/index.ts:168-175`; `packages/agent/src/component/repair.ts:44-53` | design statements do not establish operation |

## Shared records

### Components

CMP-1 — Infer symbolic component/machine combines child views, derives keyed work from event projection, records model outcomes and checks output contracts. Implementation conclusion status: wired. The surrounding executor decides when and how durable transitions run. Source: SRC-1 `packages/agent/src/component/infer/index.ts:90-149`; `packages/agent/src/component/infer/machine.ts:244-602`.

CMP-2 — Main LanguageModel service uses provider/model coordinates resolved from ModelLock and intersected model policy. Selection enforcement is wired; exact parameter identity and provider-side parameter changes are uninspected. Lock copies catalog definitions/configuration, not model weights. This path performs inference and does not itself update parameters; this is a bounded code fact, not a guarantee about the excluded provider. Source: SRC-1 `packages/model/src/lock.ts:14-33,54-69`; `packages/agent/src/component/infer/machine.ts:67-83,354-375`.

>     resolve: (reference = policy.default) => {
>       if (reference === undefined) throw new Error("no model was selected; supply a model reference or configure a default")
>       if (!modelAllowedBy(policy, reference)) throw new Error(`model ${reference.provider}/${reference.model_id} is excluded by the host model policy`)
>       const model = definitions.models.find(entry => entry.provider === reference.provider && entry.model_id === reference.model_id)
>       if (model === undefined) throw new Error(`model ${reference.provider}/${reference.model_id} is absent from models.lock.json`)
>       return { model: { provider: model.provider, model_id: model.model_id }, contextWindowTokens: model.contextWindowTokens, models: policy }
> --- `packages/model/src/lock.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

CMP-3 — Summary LanguageModel service is resolved from optional compaction model selection, potentially distinct from the main model. It receives no tools and must return nonempty completed text. Selection is wired; exact weights, hidden processing and deployment mutability each uninspected. Source: SRC-1 `packages/agent/src/component/compact/index.ts:176-194,213-225`; `packages/agent/src/component/compact/model.ts`.

CMP-4 — EventLog, Self and object services are external dependencies of this subsystem. Log append and object resolution calls are wired; physical persistence, access grants and fault isolation are uninspected. Source: SRC-1 `packages/agent/src/component/infer/machine.ts:403-430`; `packages/agent/src/model/execution/index.ts:49-50`. Caller-supplied components/tools can introduce effects outside this analysis.

### Operative objects

OBJ-1 — retained event history and its projections. SRC-1: `packages/core/src/log/service.ts:21-58`; `packages/agent/src/component/messages.ts:11-28`; `packages/agent/src/component/infer/machine.ts:425-440,514-538,547-602`; `packages/agent/src/log/events.ts:107-136`. Implementation conclusion status: wired. EventLog is the logical service-object substrate; raw messages, model calls/returns, tools and terminal events are retained there. In-memory incremental projection derives current visible context and turn state. It is not a second durable archive. External message/tool origins are imported at this boundary, while internal append/returned-event producers are automatic. Physical persistence is a dependency contract, not an inspected implementation.




>     readonly append: (events: ReadonlyArray<Event>) => Effect.Effect<void>
>     readonly read: Effect.Effect<ReadonlyArray<Event>>
>     readonly head: Effect.Effect<number>
>     readonly readFrom: (mark: number) => Effect.Effect<ReadonlyArray<Event>>
> --- `packages/core/src/log/service.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>           yield* events.append([modelCalled({
>             callId: input.attempt, model: selected, ordinal: input.ordinal, retryIndex: input.retryIndex,
>             ...(pricing === undefined ? {} : { pricing }),
>             ...(input.stamp === undefined ? {} : { output: input.stamp }),
>             turn: input.turn, ...epochStamp(input.epoch), at
>           })])
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-2 — CompactionCompleted checkpoint. SRC-1: `packages/agent/src/log/events.ts:668-679`; `packages/agent/src/component/compact/index.ts:159-194`; `packages/agent/src/component/compact/context.ts:126-166`. Implementation conclusion status: wired. Derived natural-language summary plus symbolic keepFrom, keepTokens, fileTokens, optional model and timestamp lives as an event. Later checkpoint selection uses the last summary and boundary, not a mutable pointer outside the log. The prior checkpoint remains in history. Empty-content compaction advances the boundary with the existing summary; it is not a new model-derived summary. Reason retention is not required by the checkpoint schema.

>   for (const e of log) {
>     if (e.type === "CompactionCompleted") {
>       keepFrom = String((e as { keepFrom?: unknown }).keepFrom ?? "")
>       summary = String((e as { summary?: unknown }).summary ?? "")
>     }
>   }
>   return { keepFrom, summary }
> --- `packages/agent/src/component/compact/context.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-3 — assembled request, not a durable memory store. SRC-1: `packages/agent/src/model/request.ts:70-104`; `packages/agent/src/model/execution/index.ts:30-59`. Implementation conclusion status: wired. Transient request combines retained-derived messages with shipped/caller guidance, supplied tools and the current turn's retained output declaration. Static system instructions are not accumulated memory. Delivery to LanguageModel is implemented; activation and benefit remain unobserved.

>   return {
>     system: base,
>     messages: render.conversation === undefined ? renderMessages(trajectory, context) : renderConversation(render.conversation, context),
>     tools: render.tools,
> --- `packages/agent/src/model/request.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-4 — output declaration, rejection, feedback and repair records. SRC-1: `packages/agent/src/log/events.ts:182-234`; `packages/agent/src/output/contract.ts:373-384,437-444,474-486,545-549`; `packages/agent/src/component/infer/machine.ts:133-147,321-352,503-536`. Implementation conclusion status: wired. Retained schema is symbolic validation authority. Rejected text is raw evidence; validation errors and recorded mode are derived diagnostic/control memory. Feedback is natural-language guidance; optional delegated decision data is retained but its derivation is excluded. Replacement IDs are symbolic selection metadata for transcript visibility, not rewritten answers.

>   const decoded = decodeOutput(ctx.contract, action.output)
>   if (decoded.errors.length === 0) return completed
>   if (recordsRejection(mode)) {
>     return outputRejected({
>       contract: ctx.contract.name,
>       fingerprint: fingerprintOf(ctx.contract),
>       attempt: ctx.attempt,
>       text: action.output,
>       errors: decoded.errors,
>       mode,
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-5 — referenced attachment bytes. SRC-1: `packages/agent/src/log/message.ts:13-26`; `packages/agent/src/object/storage.ts:14-25,27-54`; `packages/agent/src/model/execution/objects.ts:8-27`; `packages/agent/src/model/execution/prompt.ts:21-32`. Implementation conclusion status: wired. The event contains a file reference, media type and optional filename; actual content is separately resolved from ObjectStorage. Its generic byte representation prevents treating every attachment as natural-language or symbolic content. External acquisition is outside scope. The supplied makeObjectStorage helper can verify content identity; service injection means this helper's checks are not guaranteed for every deployed service.

>     const entries = yield* Effect.forEach(references, (reference) =>
>       Effect.map(service.value.get(reference), (bytes) => [objectKeyOf(reference), bytes] as const),
>     { concurrency })
>     return new Map(entries)
> --- `packages/agent/src/model/execution/objects.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-6 — provider continuation. SRC-1: `packages/agent/src/model/continuation.ts:4-11`; `packages/model/src/stream/collect.ts:18-22`; `packages/agent/src/model/execution/index.ts:65-72`; `packages/agent/src/component/infer/machine.ts:515-523`. Implementation conclusion status: wired. Encoded Prompt response content with provider/protocol/model/endpoint identity persists on ModelReturned. This is automatic response retention/encoding, not a demonstrated distillation or parameter update. Readable reasoning and response fields coexist with the encoded payload; the ordinary projection does not separately deliver the standalone reasoning field. Actual provider-native content and its internal effect remain opaque.

>     Effect.flatMap((parts) => Schema.encodeEffect(Prompt.Prompt)(Prompt.fromResponseParts(parts.map((part) => part.type === "error" && Schema.is(ToolCallValidationError)(part.error)
>       ? Response.makePart("tool-call", { id: part.error.id, name: part.error.name, params: part.error.params, providerExecuted: false, metadata: part.error.providerMetadata })
>       : part))).pipe(
>       Effect.map((continuation) => ({ parts, continuation }))
>     ))
> --- `packages/model/src/stream/collect.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

OBJ-7 — transcript visibility state. SRC-1: `packages/agent/src/projection/transcript.ts:6-16,64-78,83-134`. Implementation conclusion status: wired. In-memory symbolic sets/maps track event ordinals, attempt membership and completion. OutputRepaired or completion of a projectable turn hides associated rejection and feedback records in the model-visible projection. Raw entries are retained; projection can be replayed from them. This is withdrawal of reliance in a particular context consumer, not deletion or a truth verdict.

>     if (event.type === "TurnCompleted" && turn !== "") {
>       next = hideAttempts(next, Option.getOrElse(HashMap.get(attemptsByTurn, turn), () => HashSet.empty<string>()))
>     }
>     if (event.type === "OutputRepaired") {
>       next = hideAttempts(next, [String((event as { readonly replaced?: unknown }).replaced ?? "")])
>     }
> --- `packages/agent/src/projection/transcript.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

### Routes

RTE-1 — Assembly and view derivation. Caller mounts components and policies; infer composes their views, checks duplicate tool names, exactly one output strategy and at most one conversation, and rejects conflicting context settings. Returns current view plus transitions, ordering child intents before infer and other proposals. Conclusion status: wired. Component/executor owns subsequent scheduling. Static system/tool guidance is supplied instruction, not itself changed memory. Immediate output is symbolic configuration/work; later invocation reconstructs from events via CMP-1. No independent expiry or delegated-visibility guarantee. Source: SRC-1 `packages/agent/src/component/infer/index.ts:90-149`; `packages/agent/src/component/infer/view.ts:8-87`.

> 
> export const checkedTools = (tools: ReadonlyArray<AgentTool>): ReadonlyArray<AgentTool> => {
>   const names = new Set<string>()
>   for (const tool of tools) {
>     toolConcurrencyOf(tool.concurrency)
>     if (names.has(tool.spec.name)) throw new Error(`tool "${tool.spec.name}" declared more than once`)
>     names.add(tool.spec.name)
>   }
> --- `packages/agent/src/component/infer/view.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

RTE-2 — Model attempt. Open nonterminal turn with no unanswered tool calls derives an attempt key, checks effective model policy, handles pending retry timing and compaction proposals, appends ModelCalled, constructs request and calls the supplied LanguageModel bridge. It returns ModelReturned plus ToolCalled, TurnCompleted, rejection or failure events for the executor. Conclusion status: wired. Provider request is the effect boundary; custom tool execution is later external work, not performed by react. Attempt metadata survives in supplied log and influences later derivation; physical durability remains CMP-4. Model coordinate/attempt/turn selection is explicit, not semantic retrieval. Terminal events stop the route; resumed epochs and retry schedules are event-derived. Source: SRC-1 `packages/agent/src/component/infer/machine.ts:244-543`; `packages/agent/src/model/execution/index.ts:19-98`.

> const inferTransitionsFor = <R>(policy: Partial<InferPolicy>, derived: InferDerivation<R>): ReadonlyArray<ComponentWork<R | LanguageModel.LanguageModel | EventLog | Self, InferRejection>> => {
>   const giveUpAfter = policy.giveUpAfter ?? DEFAULT_INFER_POLICY.giveUpAfter
>   const slice = derived.slice
>   if (slice.length === 0 || hasUnansweredToolCall(slice) || terminated(slice)) return []
>   const context = bindTransitionContext(slice[slice.length - 1]!, "infer")
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`


An interrupted call can retain accumulated non-reasoning text once; this is partial evidence, not a successful reply. Duplicate tool-call IDs within the turn or an empty tool batch become inference failures. Retryable failures may get delay; eligible failures may switch to an unattempted permitted fallback. These are reliability policy transitions, not empirical knowledge improvement. Crash-loop default is three consecutive unanswered marks, while output-correction bounds belong to the mounted fallback. Native provider tools/direct calls/custom components outside this route are not covered by these checks. Source: SRC-1 `packages/agent/src/component/infer/machine.ts:195-205,313-319,431-502`; `packages/agent/src/component/infer/contract.ts:5-12`.

>           const invalid = action.kind === "calls" && calls.length === 0
>           const checked: Action = duplicate !== undefined || invalid ? {
>             kind: "fail", error: duplicate === undefined ? "the model returned an empty tool batch" : `duplicate tool call ID ${JSON.stringify(duplicate.callId)} within turn ${JSON.stringify(input.turn)}`,
>             ...(action.usage === undefined ? {} : { usage: action.usage }),
>             ...(action.endpoint === undefined ? {} : { endpoint: action.endpoint }),
>             failure: { cause: "inference_error", attempts: 1 }
>           } : action
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>   const pendingRetry = epochAttempts.findLast(({ event }) => event.type === "ModelReturned")?.retry
>   const lastMark = epochAttempts.findLast(({ event }) => event.type === "ModelCalled")
>   const switchModel = epochAttempts.findLast(({ retry }) => retry?.model !== undefined)?.retry?.model
>   const model = (died > 0 ? lastMark?.model : pendingRetry?.model) ??
>     (pendingRetry !== undefined ? lastMark?.model : undefined) ?? switchModel ?? selectedModelOf(head, models.default)
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>           const retry = delay !== undefined ? { dueAt: after + delay, index: input.retryIndex + 1 }
>             : nextModel === undefined ? undefined : { dueAt: after, index: 0, model: nextModel }
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

Stored scheduling is a transformed trace artifact: outcome/prior attempts produce dueAt/index/fallback metadata, which a later invocation reads. Timing is online; representation symbolic; horizon turn/epoch, not an established task boundary. This qualifies under the memory comparison's trace-write criterion without establishing improved capacity. Delegated visibility beyond this component's event input is uninspected; invalidation is terminal/epoch/attempt selection, not deletion.

RTE-3 — Compaction. Child compact proposes a cut only at a completed tool-exchange boundary and advances its checkpoint. Infer selects matching proposals when estimated conversation tokens exceed active model context-window ratio. Missing valid active capacity fails selection; no cut leaves normal inference available. The summary call sees prior summary plus selected projected span, including attached content, then returns CompactionCompleted. Conclusion status: wired. Empty/noncompleted/tool-calling summaries reject; a nonempty summary is admitted without checking its factual preservation. Enclosing executor owns persistence; later conversation read-back is BAP-1. Source: SRC-1 `packages/agent/src/component/compact/index.ts:29-91,127-197,213-279`; `packages/agent/src/component/infer/machine.ts:363-374`; `packages/agent/src/component/compact/model.ts:10-25`.

>       const window = resolution.contextWindowTokens
>       if (window === undefined || !Number.isSafeInteger(window) || window <= 0) throw new Error("The active model requires a positive context window for compaction")
>       const { triggerRatio, proposals } = conversation.compaction
>       contextPolicy = { ...contextPolicy, contextWindowTokens: window, fireRatio: triggerRatio, fireTokens: Math.floor(window * triggerRatio) }
>       if (proposals.length > 0 && estimateTokens(conversation.trajectory, contextPolicy, selected) > contextPolicy.fireTokens!) {
>         return (rendered.compactionTransitions ?? []).filter(proposal => proposals.includes(proposal.key))
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>   const finish = parts.findLast(part => part.type === "finish")
>   const text = parts.flatMap(part => part.type === "text-delta" ? [part.delta] : []).join("")
>   if ((finish?.reason !== "stop" && finish?.reason !== "tool-calls") || parts.some(part => part.type === "tool-call") || text.trim() === "") {
>     return yield* unknownModelError("Compaction requires a nonempty completed summary without tool calls")
>   }
>   return text
> --- `packages/agent/src/component/compact/model.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

The proposal guidance asks the model to retain names, IDs, decisions, unfinished work and file facts. That is an instruction to preserve content, not a criticism/test of the old summary. Whole summary replacement is addressable as text, but no structured assumptions or retained adoption rationale are required. Summary formulation and later supply are wired; content-directed criticism, measured future capacity and causally attributable improvement are uninspected. Old-span lifetime, selector details and recovery are traced by the memory lens below.

>           const brief = [{
>             role: "user" as const,
>             content: [
>               { type: "text" as const, text: "Summarize this agent history in a compact paragraph. Keep every fact a future turn could need: names, ids, decisions, unfinished work. Preserve relevant facts from attached files.\n\n" },
>               ...(input.summary === "" ? [] : [{ type: "text" as const, text: `Summary so far: ${input.summary}\n\n` }]),
>               ...content
>             ]
> --- `packages/agent/src/component/compact/index.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>   if (openHead !== -1 && openHead < from) push(projected[openHead]!, userMessageOf(projected[openHead]!, resolved))
>   if (checkpoint.summary !== "") push(projected.findLast((event) => event.type === "CompactionCompleted")!, { role: "user", content: `Summary of earlier work:\n${checkpoint.summary}` })
> --- `packages/agent/src/projection/messages.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

Empty-content branch advances keepFrom while reusing the previous summary. The ordinary reactor derives keepTokens from current estimated visible history times retainRatio, while trigger capacity uses active model window times triggerRatio. The summary model resolves separately. The later model receives summary in a user-role message plus suffix/open head; boundary selection can back up to matching native continuation. Failure yields no completed new checkpoint and leaves the prior cut available. Raw events are not deleted. This automatic online transformation consumes event trajectory/tool traces and produces natural-language text plus symbolic checkpoint metadata; task horizon is not determinable. Delegated consumer visibility beyond provided projection is uninspected.

RTE-4 — Output-contract check and correction. Completion decodes JSON and validates the turn's frozen schema regardless of provider assurance. Success completes; missing mode fails; native/local mismatch fails; repair/delegated modes retain rejection. Repair can ask again up to its bound; delegated mode parks until its owner supplies feedback/disposition. A later valid completion emits repair markers for projectable rejected attempts. Conclusion status: wired. Check authority is schema conformance, not truth of values. Model proposes text, deterministic checker can veto, mounted policy owns retry/admission, caller owns schema. Human review is not required by this branch. Source: SRC-1 `packages/agent/src/component/infer/machine.ts:101-163,214-227,299-352,503-536`; `packages/agent/src/output/contract.ts:165-183,373-384,474-486`; `packages/agent/src/component/repair.ts:11-40,44-95`.

>   let parsed: unknown
>   try {
>     parsed = JSON.parse(text)
>   } catch (e) {
>     return { value: undefined, errors: [`/: the response is not JSON: ${e instanceof Error ? e.message : String(e)}`] }
>   }
>   const decoded = contract.decode(parsed)
>   return "errors" in decoded ? { value: parsed, errors: decoded.errors } : { value: decoded.value, errors: [] }
> --- `packages/agent/src/output/contract.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>     // A delegated mode parks here. The component that mounted it reads the rejection and decides:
>     // its own feedback through `OutputRetryRequested`, its own terminal, or nothing. The reactor
>     // never schedules the framework loop on its behalf.
>     if (!asksAgain(spent)) return []
>     const allowed = correctionsOf(spent)
>     if (rejections.length > allowed) {
>       return terminate({
>         cause: "output_repairs_exhausted",
>         error: `the response did not satisfy the declared output contract after ${allowed} correction${allowed === 1 ? "" : "s"}`,
> --- `packages/agent/src/component/infer/machine.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

The contract schema is frozen from a copy, so changing a source object does not revise this turn's contract. Successful correction changes the selected answer/history projection; it does not update runtime code or model weights. Invalid/rejected output can carry arbitrary beliefs, but this evaluator criticizes syntax/schema errors only. Conjectural learning remains uninspected because no candidate-linked evidence establishes a theory criticized for what it says or resulting improved future capacity. Correction instruction/feedback is later consumed, with projection and retention details below.

>   const decision = decided.get(String(rejection["attempt"]))
>   if (decision !== undefined) return decision
>   const mode = modeOf(rejection["mode"])
>   if (mode?.kind !== "repair") return undefined
>   return correctionText((rejection["errors"] ?? []) as ReadonlyArray<string>)
> --- `packages/agent/src/projection/messages.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

Recorded validation errors are the reason supplied in later correction text; delegated feedback is read but the separate decision payload is not selected by this route. projectHistory false retains the correction exchange; true causes later projection withdrawal while raw events remain. This online trace transformation produces natural-language diagnosis/instruction and symbolic modes/replacement IDs. Turn/epoch bounds do not establish task scope. No dedicated rollback of the correction is shown; callers can supply different future events under the enclosing host contract. Human adoption and factual improvement remain uninspected.

RTE-5 — attachment resolution and delivery. SRC-1: `packages/agent/src/model/execution/objects.ts:8-27`; `packages/agent/src/model/execution/prompt.ts:21-32`; `packages/agent/src/component/compact/index.ts:150-182`. Implementation conclusion status: wired. On request preparation the bridge selects file references from already selected user messages, deduplicates by object key, explicitly pulls their bytes with bounded concurrency (default four), and constructs provider file parts. Missing service/objects fails preparation; no silent text-only substitution. Compaction also resolves selected attachments before summarization. Pull describes the bridge's requested bytes; automatic selection of enclosing messages is a separate push to the model. Per-request duplicate fetch avoidance is not memory dedup curation.

>       const key = objectKeyOf(part.object)
>       const data = objects?.get(key)
>       if (data === undefined) throw new Error(`Unresolved object: ${key}`)
>       return Prompt.filePart({
>         mediaType: part.mediaType, data,
>         ...(part.filename === undefined ? {} : { fileName: part.filename })
>       })
> --- `packages/agent/src/model/execution/prompt.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

Route audit: request preparation owns explicit byte retrieval and immediate provider-part construction, with later model/summary consumption. Missing bytes/service fail the operation; lifetime/expiry and remote delegated visibility are external service matters. Object identity selects bytes but does not validate their semantic content. No content revision or theory proposal occurs here.

RTE-6 — compatible continuation replay. SRC-1: `packages/agent/src/projection/messages.ts:125-129,155-159,176-185`; `packages/agent/src/model/execution/continuation.ts:5-14`; `packages/agent/src/model/execution/prompt.ts:12-17`; `packages/agent/src/component/compact/context.ts:150-159`. Implementation conclusion status: wired. Response identity first associates a continuation with its assistant/tool-call or terminal output entry. Provider/protocol/model equality then selects encoded replay instead of reconstructed display content. An incompatible identity uses the reconstructed message; a compatible malformed payload can fail schema decoding. Endpoint is retained but is not part of this equality gate. A compaction boundary on a tool call backs up to its matching ModelReturned continuation when present. No selected continuation is passed wholesale into the compaction brief; that brief uses event text and attachment content.

> export const replayOf = (continuation: ProviderContinuation | undefined, identity: ReplayIdentity): ReadonlyArray<Prompt.Message> | undefined => {
>   if (continuation === undefined || continuation.provider !== identity.provider || continuation.protocol !== identity.protocol || continuation.model !== identity.model) return undefined
>   return Schema.decodeSync(Prompt.Prompt)(continuation.payload).content
> }
> --- `packages/agent/src/model/execution/continuation.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

>   return messages.flatMap((message) => {
>     for (const call of message.toolCalls ?? []) names.set(call.id, call.name)
>     return replayOf(message.continuation, identity) ?? promptMessage(message, names, objects)
>   })
> --- `packages/agent/src/model/execution/prompt.ts` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`

Route audit: model-request conversion owns compatibility gate and returns native messages or reconstructed fallback. Retained provider/protocol/model identity selects future replay; endpoint is stored but not compared. Malformed compatible payload can fail decoding, with no semantic recovery fallback inferred. Expiry and delegated visibility remain external. Encoding is not by itself a new trace-learning route, and opaque content prevents full representation classification.

### Claims

CLM-1 — README describes a modular framework around an immutable log, with crash-proof durable hosts and at-least-once external effects. Conclusion status: claimed. The scoped inference machine derives keyed attempts from replay/incremental state, but excluded physical hosts prevent validation of the broad crash-proof claim. Source: SRC-2 `README.md`; SRC-1 `packages/agent/src/component/infer/machine.ts:547-602`.

> External effects have at-least-once execution. Each keyed result is recorded once. Providers can use the transition key as an idempotency key.
> --- `README.md` @ `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`



### Evidenced absences

No separate absence record is asserted. Excluded implementations and unexecuted faithfulness checks are explicit limitations, not evidence of whole-system absence.

### Behavioral-authority paths

BAP-1 — Accumulated conversation/summary and current guidance reach the model through modelRequest/react. Consumer is supplied LanguageModel; channel is model messages/system/tools, force is advisory instruction/evidence over the selected context horizon. Request assembly/delivery is wired; actual model activation and factual compliance unobserved. Source: SRC-1 `packages/agent/src/model/request.ts:70-105`; `packages/agent/src/model/execution/index.ts:29-58`. Summary, error guidance, attachment bytes and compatible native continuation have distinct selection paths (RTE-3, RTE-4, RTE-5, RTE-6); no guaranteed actual influence follows.

BAP-2 — Machine consumes event identity/status and contract/policy metadata to choose hold, retry, fail, compact or complete. Consumer is deterministic inference/projection code; channel symbolic event state; force enforcing within that route/turn/epoch. This is operational control, not epistemic acceptance of task assertions. Source: SRC-1 `packages/agent/src/component/infer/machine.ts:244-375`. Retained output declaration supplies formal validation authority. Transcript visibility and retry schedules are concrete control consumers; code paths do not grant semantic truth authority.

## Runtime account

A caller mounts infer with child components/output policy and supplies model/log services. A message event opens a turn. Component projection supplies system instructions, offered tools, conversation and output strategy. Infer first allows policy intents to commit, then either derives compaction or a keyed model attempt. The bridge converts history/attachments and tools to provider request types, collects response parts, and returns model action/events. Calls are recorded for later child dispatch; an unanswered call blocks another inference. A conforming final response completes the turn; failure/retry/correction paths preserve their own metadata. An enclosing actor executor persists these results and invokes another derivation. This boundary returns transitions and events, not a deployment-level guarantee.

Material alternatives: native output, validate-once, repair and delegated correction; explicit chosen/default/fallback model; summary-model override; with/without compact; fallback messages versus supplied conversation; incremental machine versus complete replay; arbitrary child effects and out-of-route provider calls. Schema checking covers completion in the inspected infer route. It does not establish semantic correctness, custom-tool permissions, platform idempotence or physical crash safety.

Static forcing cases: duplicate view tool names/conflicting context declarations throw before serving; forbidden/unknown model and missing compaction capacity become terminal selection failures; pending tool calls suppress inference; repeated unanswered model marks hit crash bound; malformed output fails or enters bounded/delegated correction; empty/tool-calling summary fails before new checkpoint return. No dynamic check planned. Replay, output-contract and compaction execution tests were considered; static branch inspection suffices for wiring, while dependency installation/provider/host deployment would not establish broad causal performance or durability. No packages, credentials or deployment were used.

Capability surface includes model inference and composition of arbitrary child work. Current grants, delegated principals and deployed isolation are uninspected external-host matters. Human authors select code, schemas, policies and models; machine checks schema/policy/capacity and the model proposes responses/summary text. No supplied expected task answer or empirical outcome oracle appears in these inspected checks: the schema is an answer-format oracle only. Operation serves open caller turns; actor-checking/optimization experiments elsewhere are excluded. Product/code revision admission is outside scope; memory/checkpoint and output revision admission is RTE-3/RTE-4.

## Lens scoping

### Memory/context scope

Full lens: event/log projection, compaction, correction histories, object attachments and provider continuation can carry changed material into later model/machine invocations. Routes RTE-2, RTE-3 and RTE-4 and objects OBJ-1, OBJ-2, OBJ-3 and OBJ-4 trigger it. Exclude physical hosts and separate optimization tooling; preserve all included opaque/alternative paths.

### Epistemic scope

Full lens: model outputs may state claims; summary generation can change retained content; schema checks alter answer admission and history. Assess acquisition, generation, validation, reliance and retention in these four routes without inferring knowledge production from format success. No scientific knowledge-production claim is assigned to this operational subsystem.

## Lens outputs

### Memory/context lens


Acquisition and memory transformation must remain separate. OBJ-1 records incoming requests and results plus machine events; attachment upload and external author choices are outside the commissioned boundary. Infer automatically appends call and interrupted partial-text marks and returns response/outcome events. Continuation encoding retains response content for compatible replay (OBJ-6), without established compression or new knowledge.

RTE-3 is a qualifying trace-fed memory write: selected projected history, including tools and attachments, plus the prior summary becomes a new retained natural-language checkpoint and boundary. The prompt preserves decisions and unfinished work; it does not demand a structured reason for each recommendation. A generated reason may survive incidentally, but no required rationale field, reason-preservation check or reason-specific later consumer exists. The later model receives whatever summary text survived. A zero-content checkpoint only reuses the prior summary and changes the boundary. A failed summarization produces no completed checkpoint on this route; the prior cut remains available. No in-place edit or human approval stage appears in the inspected writer.

RTE-4 is a second trace-fed transformation: actual response plus declared schema becomes retained validation errors and mode, which later produce corrective instruction and bound retries. Error text explains why correction is requested and is read during feedback construction. Successful output yields symbolic replacement metadata controlling later visibility. An external delegated component can supply its own feedback/decision, but its generation and task scope are excluded. Ordinary retry/fallback schedules in RTE-2 are also mechanically derived retained control rather than learned factual knowledge. Their observed effectiveness is unknown.

All included automatic transformations occur online. The log and summary cross model calls, and summaries can cross turns; the code does not equate those boundaries with task or project. No task-horizon claim is inferred from a thread identifier.



Infer's automatic history assembly pushes selected retained content to LanguageModel. The selectors use current turn/epoch/attempt identity, the last checkpoint, keepFrom boundary and rendering budget; they do not ask the model for a semantic memory query. The model capacity check gates compaction, while boundary selection keeps complete tool exchanges. SRC-1 `packages/agent/src/component/compact/context.ts:48-57` sets defaults of 12,000 message characters, 6,000 tool-result characters, 1,200 estimated tokens per file, 200 characters per clipped summary tool/result line, trigger ratio 0.8 and retain ratio 0.5. The operative reactor derives keepTokens from the current estimated visible history times retainRatio (`packages/agent/src/component/compact/index.ts:218-225`); the trigger is active model capacity times triggerRatio (`packages/agent/src/component/infer/machine.ts:363-370`). Do not substitute the older model-relative helper description for this live cut computation.

Size is an estimate: textual/rendered or serialized-continuation characters divided by four, with file estimates, not a measured complete provider request. Whole system/tool overhead and actual multimodal token use are not guaranteed by this formula. The code explicitly clips some displayed content and preserves a notice. A text-message notice mentions logs.events, but that tool implementation is excluded; it is not counted as a verified model pull route. The only included pull is the execution bridge's concrete ObjectStorage read (RTE-5).

RTE-4 supplies schema errors or externally chosen feedback as user-role messages paired with rejected assistant text. A completed projectable repair removes those pairs from subsequent rendered context; raw evidence remains. RTE-6 may instead supply compatible native continuation, so the readable display alone is insufficient to predict model input. The runtime also automatically selects stored retry, model and rejection metadata for BAP-2. These routes establish delivery and deterministic control use, not model faithfulness or beneficial activation.



The profile's service-object and in-memory values name the actual inspected storage/access boundary. It intentionally makes no sqlite/files/kv claim about excluded hosts. Representation is unknown as a complete set because the consumed bytes and native continuation can contain content not characterized by the local text/JSON envelope. The same distinction prevents assuming every externally supplied artifact was manually authored or trace-extracted.

Behavioral authority is established at consumer interfaces: model messages provide knowledge/instruction; stored event decisions govern runtime enforcement/routing; stored output declarations supply validation. No training or ranking route is inferred. Consolidation reduces displayed history through summary, evolution replaces the operative summary with a new checkpoint, and invalidation withdraws corrected attempts from subsequent model view while retaining their events. These describe intended implemented operations, not a guarantee that the summary invents no facts. Mechanical identity deduplication is excluded from curation.

Both pull and push are warranted only because their named consumers differ: the object-resolution bridge requests bytes, while model/runtime consumers receive automatically selected history. Coarse selection covers latest/suffix/budget choices. Identifier selection covers actual matches for boundaries, turns, attempts, replaced rejections and continuation compatibility. There is no model-judgment retrieval selector on the inspected paths; the model generates the summary rather than choosing a query-specific memory subset.

Trace learning uses the comparison contract's automatic retained behavior-shaping-write sense. RTE-3 alone supplies a clear qualifying summary route. RTE-4 and RTE-2 add diagnostic/control derivatives; their natural-language and symbolic forms are retained even though they do not establish improved capacity. Raw logging and lossless provider replay are not sufficient by themselves. The trace sources, online timing and mixed distilled form cover these same routes. Task scope remains unknown. Faithfulness remains unknown because no retained executed dependence test was available, and static test references in comments are not results.


### Epistemic lens

1. Boundary: source register SRC-1/SRC-2, subsystem routes above. Physical hosts, custom tools and actor optimization are excluded. The question is what output/summary checking licenses. Missing candidate-linked runs and external-world measurements prevent actual truth, behavior or improvement attribution. CLM-1 is a durability/architecture claim, not knowledge warrant.

2. Objects: see canonical identities. OBJ-1's user/tool material can contain truth-apt assertions of unknown source warrant; model-returned content may add conjectures, but generic generation does not identify which propositions are ampliative. OBJ-2's summary has indeterminate preservation because the model may omit, paraphrase or add. OBJ-3's fixed guidance/tool signatures are operational policy rather than accumulated epistemic conclusions; its delivered history inherits underlying content limits. OBJ-4's schema and rejection state are explicit formal constraints and errors; conformance judgments have a bounded symbolic domain and do not judge a field's factual truth.

3. Authority ledger (architectural status separate from conclusion status):

| Route/function | Architectural status | Content relation and target | Check/force, timing and authority | Limit |
|---|---|---|---|---|
| RTE-1 operational admission | implemented | no content change; component assembly | rejects incompatible declarations before inference through BAP-2 | code consistency is not task warrant |
| RTE-2 acquisition/operational consumption | implemented | truth-apt acquisition/import of message/tool history | source-selected context passed through BAP-1 | source truth/coverage unknown |
| RTE-2 content transformation | implemented | indeterminate model output relation | model produces final/tool actions; BAP-1; later checks RTE-4 | no identified warranted premises or empirical test |
| RTE-3 content transformation | implemented | indeterminate summary of selected content | prompt-guided model generation after capacity trigger | preservation versus ampliation not decidable from prompt |
| RTE-3 check/evidence production | implemented | no content change; finished nonempty text without tools | deterministic completion check before checkpoint return | not a truth/coverage check |
| RTE-3 operational admission/retention | implemented | new checkpoint admitted after format gate | checkpoint becomes selected later context via BAP-1 under executor contract | retention is not epistemic acceptance |
| RTE-4 check/evidence production | implemented | entailed derivation within JSON/schema semantics | decode/validator produces errors or conformance result | supports schema conformance only |
| RTE-4 disposition | implemented | non-truth-apt response status update | fail, park, retry or complete through BAP-2; mounted policy controls | no general truth license |
| RTE-4 retention/selection | implemented | projected repair history changes active context | replaced rejection metadata can hide earlier correction exchange | raw retention and active context are distinct |

4. Lifecycle: for OBJ-1 model candidate and OBJ-2 summary, transformation is indeterminate; possible preservation/ampliation cannot be resolved without candidate-linked input/output evidence. Generation, bounded checks and operational retention are implemented; observed candidate state is no instance observed for generation, testing, acceptance and post-acceptance integration. No empirical theory-testing lifecycle is established by schema validation. OBJ-4 conformance/error derivation is non-ampliative in its explicit symbolic domain; discovery lifecycle is not applicable. OBJ-3 shipped operational guidance has no candidate truth-apt output of its own. Source acquisition in OBJ-1 has unverified warrant. No stored event's presence alone grants epistemic authority.

5. CLM-1: source demonstrates log-derived transitions and model markers, not full platform crash recovery. Observed-run support and causal support are uninspected. Summary-preservation prompt asks for future-needed facts (RTE-3); its implemented gate checks completion/nonemptiness, not coverage. The difference is an evidence limit, not an observed failure. Output conformance claim is code-grounded within declared schema semantics (RTE-4); task truth remains outside it.

6. Bounded conclusion: this subsystem grants model content operational use through history/checkpoints and can withhold final completion for schema errors. That is concrete context/control machinery. It does not establish that a passed answer is true, a summary preserves every relevant fact, or criticism improved future task capacity. Domain-specific tools or optimization may supply additional warrant outside this boundary; no claim about those uninspected routes follows.

## Reconciliation

Verified report completion, run/source/pin, input/method digests and exact report bytes. Mappings: MEM-OBJ-1 → OBJ-5; MEM-OBJ-2 → OBJ-6; MEM-OBJ-3 → OBJ-7; MEM-RTE-1 → RTE-5; MEM-RTE-2 → RTE-6. Shared OBJ-1 remains the combined log/projection seed; new facets do not reuse its identity.

All seven integration issues accepted: preserve attachment/continuation/visibility objects and distinct consumer routes; add zero-content summary branch, current-history cut budget and continuation-aware boundary; retain correction-reason consumption, unused delegated decision and projectHistory alternative; include retained retry derivatives consistently; keep representation/lineage/agency/task-horizon/faithfulness uncertainty. Integrated wording calls replacement IDs selection metadata, keeping the report's explicit visibility-only scope and no security claim. No substantive conflict remains. Full-result semantic verification is coordinator-owned.

## Bounded synthesis

Tardigrade's inspected subsystem makes model progression explicit in event-derived transitions. Composition determines offered context/tools; the infer machine owns model selection, hold/retry/terminal decisions and output checks; compaction is separately proposed and selected by capacity. These separations make error and continuation policy inspectable while leaving physical durability to an enclosing host.

The supported contribution is a wired correction-and-context path. Conjectural learning remains uninspected: format repair and summary replacement do not establish criticism of an operative theory or improved future capacity. Narrow reflection is wired at the context/retry level: representation of prior attempts, failures and context size changes subsequent transition choice. A reflective theory builder is not established. Self-improvement is likewise uninspected at this boundary; alternate actor optimization tooling is excluded, and no capacity comparison was performed. Source-visible checks can establish schema conformance and operational eligibility, with task truth and summary fidelity requiring different evidence.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Host/platform excluded | CMP-4, CLM-1 | service calls and returned transitions | end-to-end durability, isolation, exactly-once effects | platform implementation and fault-injection traces |
| No candidate-linked execution | RTE-2, RTE-3, RTE-4 | symbolic source | actual summary fidelity, correction activation or capacity benefit | retained runs and appropriate interventions |
| Provider identity/weights opaque | CMP-2, CMP-3 | model coordinates and policy | exact weight identity or provider learning | provider/deployment evidence |
| Custom tools and actor optimization excluded | RTE-1, RTE-2 | supplied views/results | complete framework capability/warrant/improvement characterization | separately scoped source analysis |
| External producer and opaque parts | OBJ-5, OBJ-6, RTE-4 | byte/feedback consumption contracts | complete representation/lineage/write-agency sets | corresponding producer/provider evidence |
| Thread/turn is not task | RTE-2, RTE-3, RTE-4 | event identifiers and timing | per-task or cross-task learning scope | explicit task partition and retained trace |

## Verification and blockers

### Semantic verification

Checked ownership and alternate paths, missing-mode/invalid-contract/model-policy failures, pending tools, crash/correction bounds, malformed summary refusal, instruction-vs-warrant distinction and model-coordinate-vs-weight identity. Checked all specialist issues and complete profile scope: include opaque attachments and compatible continuation, preserve uncertain origin/agency; retain summary, correction and retry derivative routes in all trace descriptors. Pull names the execution bridge, push the model/runtime consumers; identifier selectors actually match retained parts. No provider opaque replay is counted as distilled learning merely because it persists. Known curation and operational authority do not imply semantic truth or beneficial activation.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/result.md`; full validation after memory integration; guarded publication verifies quotes against complete pinned blobs.

### Blockers

none
