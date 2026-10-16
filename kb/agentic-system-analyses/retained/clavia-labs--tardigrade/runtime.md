---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Tardigrade runtime baseline tracing atom invocation, governed and code execution, legacy hosting, recovery and actor admission at the frozen commit."
run-id: AAS-2026-10-15-tardigrade-455e1aaccd4d-01
reviewed-boundary: "1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8"
---

# Tardigrade runtime report

## Runtime account

### Evidence and consequential work

Tardigrade ships an enclosing agent runtime, not only a model-call helper. Its consequential work is accepting identified actor invocations, deriving model and tool proposals from event-backed state, executing those proposals through supplied services, and projecting a terminal method result. Two API generations matter: the current atom graph and the deprecated component runtime still used by the server. The frozen boundary and source identity are in [boundary](boundary.md). All evidence below is SRC-1, implementation unless explicitly labelled doctrine/design. No execution trace or experimental result was supplied; no target code, tests, examples or provider calls were executed. Wiring is not observed activation, reliability or benefit.

Added inspection beyond the boundary's initial reads includes current core host composition and invocation/result projection (`packages/core/src/runtime/layers.ts`, `packages/core/src/runtime/actors.ts`); core request commit and recovery excerpts (`packages/core/src/runtime/execution.ts`); journal transaction logic (`packages/platform/src/shared/sql-journal.ts`); permission, budget, tool and code-mode atoms/services; the example actor and its services; model-lock resolution; the method HTTP adapter; Bun sandbox implementation and isolate adapters; child-agent library; legacy server assembly, component inference, model execution and code-mode dispatch; actor build and server push implementation. The source register's existing SRC-1 covers these paths at the same commit. Available but uninspected details, including full Cloudflare thread scheduling, legacy machine internals and provider implementations, remain limits rather than absences.

### Ordinary shipped invocation

The Bun example supplies the clearest small end-to-end driver, [RT-RTE-bun-message](#rt-rte-bun-message). The external caller owns the initial problem and request ID. `createBunHost` composes supervisor allocation and invocation delivery; it stores an instance supervisor database and separate thread journals. A coordinate is actor/instance/thread. `thread.methods.message` submits a JSON method body with host-established sender identity and an explicit invocation ID, then waits for the projection of that invocation to settle. The agent method maps received text/content to `TurnRequested`, using the invocation ID as the turn ID. The caller does not choose each subsequent step.

Code owns progression: `infer` reads model selection, turn state, compacted context and the final tool view. It emits configuration, waiting, cancellation, failure and settlement events or proposes a `Generate` act. A model supplies answer text and tool calls; fixed event/atom rules decide which effects become executable and when the turn settles. The model receives a natural-language system string, selected conversation messages and symbolic tool schemas. Its distributed-parametric decision component is [RT-CMP-model](#rt-cmp-model). `modelServices` resolves content objects and provider-compatible continuations, calls the configured Effect AI provider abstraction, rejects output-limit finishes, optionally checks structured output, and normalizes tool calls. `infer` rejects duplicate provider call IDs and assigns internal call IDs using the effect reference and tool index. Thus provider IDs and durable execution IDs have different roles. Evidence: SRC-1, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/services/model.ts`, `packages/agent/src/actor/methods.ts`.

The normal tool executor is the configured library registry. Tool output becomes `ToolReturned`, then conversation state for another inference. A turn without further reply work becomes `TurnSettled`; `agentReply` projects completed text, failed error or cancelled reason. This is a protocol completion test, not an oracle for factual correctness. The Bun example prints the returned object and waits for thread work. The current HTTP adapter instead returns a 202 invocation reference and exposes polling, cancellation, event inspection and ephemeral execution updates. Bearer authorization is conditional on supplying `options.token`; `/healthz` is outside that check. In-process methods do not traverse this HTTP check. Evidence: SRC-1, `packages/platform/src/shared/method-http.ts`, `packages/core/src/runtime/actors.ts`.

Context preparation is load-bearing but not an all-input-size guarantee. `compact` clips user/tool text, estimates serialized size using characters and image estimates, and requests a summary above a configured fraction of the model window. It keeps a tail at valid message boundaries and supplies an earlier-summary user message to later inference. Pending tool pairs or missing boundaries can leave the current context ready without compaction despite exceeding the estimate. The summary call has no tools and asks that conversation content be treated as data. A summary failure produces a failed context and can fail the turn. This establishes working-context selection and later summary consumption, not fidelity, resistance to malicious content or cost savings. Detailed retained-state revision belongs to the memory analyst. Evidence: SRC-1, `packages/agent/src/atoms/compact.ts`, `packages/agent/src/services/model.ts`.

### Guarantees and forcing routes

Three forcing cases prevent treating the default actor's controls as universal.

1. **Unwrapped tools in a shipped actor.** The Bun example's `meeseeks` uses `libraryTools()` directly, unlike `createActor`, which wraps tools in permissions and budgets. Its services configure fetch and an in-memory workspace. The permissions atom's default is ask, but only a composed wrapper consults its decisions. The default actor's budget uses `configure: false`; without logged budget configuration, the wrapper passes through. [RT-RTE-governed-tools](#rt-rte-governed-tools) therefore records a composition-scoped gate, not universal human approval or an always-active cost cap.
2. **Code-mode package calls.** Current `codeMode` proposes `EvaluateCode` and `ExecutePackage`, not `ExecuteTool`. It admits JavaScript for the `execute` call and lets isolate RPC requests create independently durable package operations. The configured library set and replay call-order checks bound this route, but the ordinary `withPermissions` tool wrapper is not demonstrated to govern each inner package method. [RT-RTE-code-execution](#rt-rte-code-execution) separates that route from ordinary library tools. A script can coordinate several calls; counting outer execute calls is not necessarily counting inner operations.
3. **Legacy hosted server.** The shipped server imports the deprecated host and composes deprecated inference, budget, escalation, code mode, compaction and output validation. Its package set includes child agents, workspace, filesystem and HTTP fetch. Its escalation request callback grants requests computationally; this is not proof of operator approval. Current atom request identities and controls cannot be attributed to it. [RT-RTE-legacy-server](#rt-rte-legacy-server) traces its distinct ingress and return.

The durable forcing case is restart between an accepted effect and its completion. [RT-CLM-request-before-execution](#rt-clm-request-before-execution) is owned by core execution and the journal adapter: execution obtains a committed request before dispatch; SQL stores records, pending inputs and optional checkpoints transactionally by default. Commit failure discards the candidate snapshot and latches a persistence error. Recovery reads checkpoint plus suffix and pending inputs, replays the graph, and may recreate local deferred producers. This is an implementation invariant for effects driven through this core path plus a storage protocol depending on the journal/SQL implementation. It is **not** an exactly-once external side-effect guarantee: a retry/recreated producer can reach the external service again. Correct restart also depends on compatible actor code, recreatable services and executor-specific completion/cleanup contracts. The core accepts no-journal operation and custom journal/commit implementations, so durable storage cannot be inferred merely from atom use. The deprecated host has its own recovery path; parity is not established.

The capability surface is broader than a particular grant: custom actor definitions, service layers and libraries can supply arbitrary host effects; a selected tool catalog is the current callable surface; a permission or budget decision is a particular grant. Isolation is a third question. Current Bun code mode delegates to a subprocess sandbox with empty environment, restricted lexical names, IPC package calls, log limits and an execution-segment timer; a package RPC temporarily stops that segment timer. This does not establish OS-level filesystem/network isolation or safety against all JavaScript escapes. Host library code executes outside the code body's lexical restrictions. The Cloudflare adapter supplies a Worker Loader isolate instead, requiring that external runtime's contract. No deployed policy or live isolation test is available. Evidence: SRC-1, `platform/bun/src/sandbox.ts`, `packages/platform/src/bun/isolate.ts`, `packages/platform/src/cloudflare/isolate.ts`.

Within the inspected standard model adapter, `disableToolCallResolution` and `providerExecuted: false` keep tool resolution on the runtime side. This covers that adapter request, not all provider-native hosted tools, custom `Model.call`/`submit` implementations, direct provider calls inside libraries, extension modules, shell effects introduced by actor code, remote services or manually composed graphs. Those alternatives have no demonstrated universal gate here. The inspected server assembly declares no shell package; that is a property of this assembly, not a system-wide prohibition. Child calls have a separate visibility and completion path, [RT-RTE-child-invocation](#rt-rte-child-invocation); local actor handles are explicitly scope-bound rather than durable across arbitrary runtime lifetimes.

### Change admission

Product and capability changes can enter through rebuilt actor source, executable service/library code and server-pushed artifacts. [RT-RTE-artifact-admission](#rt-rte-artifact-admission) distinguishes byte-integrity/shape checks from behavioral validation: a hash does not establish safe code or improved behavior, and importing a module executes trusted host-side code. Build supports both API generations, while the inspected server definition loader expects component actors. Failed build replacement has a restore attempt; failed server replacement after host closure has no equivalent demonstrated restoration in its push catch block.

NPO and GEPA are shipped model-facing improvement procedures, [RT-RTE-optimization-guidance](#rt-rte-optimization-guidance), not an observed optimizer service. They prescribe trace-fed prompt/harness proposals, fixed evaluations, held-out comparisons, candidate identity and scoped promotion. The optimizing agent and user, rather than a hard-coded runtime score gate, own the procedure. Their existence does not demonstrate learning, autonomous promotion, exercised self-improvement or improved capacity. Routine event retention and checkpoints support subsequent execution and recovery; neither alone revises actor source.

## Shared records

### Components

#### RT-CMP-model
Label: Configured language model

Source-native identity: `Model`, backed in standard services by `LanguageModel`, `ModelLock` and provider/model coordinates. Representational form: distributed-parametric for provider inference; symbolic lock metadata and natural-language prompts are separate inputs. Storage substrate: model weights/provider state external to the repository; local JSON lock definitions and in-memory cloned policy hold selection metadata, not weights. SRC-1, `packages/agent/src/services/model.ts`, `packages/model/src/lock.ts`.

Parameter change during operation: uninspected inside providers; the inspected adapter invokes inference and exposes no weight-update step. Exact parameter version pinned: not established. `models.lock.json` freezes metadata and provider/model IDs, not a parameter digest. Mutable endpoint can resolve to another model: possible under the external provider contract; lock entries include HTTP base URLs and model IDs but do not authenticate served weights. Teacher/student roles in the NPO instructions do not establish additional inspected weight implementations.

> if (model === undefined) throw new Error(`model ${reference.provider}/${reference.model_id} is absent from models.lock.json`)
> --- `packages/model/src/lock.ts`

> disableToolCallResolution: true as const,
> --- `packages/agent/src/services/model.ts`

### Operative objects

#### RT-OBJ-journal
Label: Event journal and pending effect inputs

Source-native identity: journal records, checkpoint payload and effect inputs. Form: symbolic event envelopes and references, with embedded natural-language user/model/tool content consumed separately by inference. Substrate: Bun SQLite files, Cloudflare Durable Object SQLite, or caller-supplied journal. The inspected SQL append checks expected sequence head, preserves accepted input digests and commits records/input changes/checkpoints together by default. It is recovery state, not a learned model. SRC-1, `packages/platform/src/shared/sql-journal.ts`, `packages/core/src/runtime/execution.ts`.

> if (existing.length && existing[0]!.digest !== input.digest) return yield* Effect.fail(new RuntimeError("Accepted effect input cannot change"))
> --- `packages/platform/src/shared/sql-journal.ts`

> yield* options.commit ? options.commit(work, events, expectedLength + events.length) : sql.withTransaction(work)
> --- `packages/platform/src/shared/sql-journal.ts`

#### RT-OBJ-permission-policy
Label: Permission policy and resolved decisions

Source-native identity: `PermissionPolicy`, `PermissionConfigured`, `PermissionResolved`, keyed by action/resource/call ID. Form: symbolic policy and decision records; textual reasons are explanatory fields, not the gate. Substrate: event-backed permission state and configured initial policy. Decision lookup and `allowed` control execution only in the composed permission tool wrapper. SRC-1, `packages/agent/src/atoms/permission-request.ts`, `packages/agent/src/atoms/tools.ts`.

> export const DEFAULT_PERMISSION_POLICY: typeof PermissionPolicy.Type = { default: "ask", actions: {} }
> --- `packages/agent/src/atoms/permission-request.ts`

#### RT-OBJ-actor-artifact
Label: Actor module and manifest

Source-native identity: `actor.mjs` and `manifest.json`, including actor name, schema and SHA-256 digest. Form: symbolic executable JavaScript plus symbolic manifest; embedded instruction strings receive natural-language authority when used in prompts. Substrate: built artifact directories and server actor storage, then imported host modules. Source identity and candidate history are not automatically equivalent to immutable run identity. SRC-1, `apps/cli/src/build.ts`, `apps/server/src/host.ts`.

> const actual = digestOf(artifact.module)
> if (actual !== manifest.digest) throw new Error(`actor artifact digest mismatch: expected ${manifest.digest}, got ${actual}`)
> --- `apps/server/src/host.ts`

### Routes

#### RT-RTE-bun-message
Label: Bun message invocation and agent loop

Endpoints/progression: example caller → allocated `meeseeks` thread → typed message admission → turn/inference atoms → model service → library tool results or terminal answer → method projection → caller. Owner: host for delivery/lifetime; graph code for next-step scheduling; model for answer/tool proposal. Identities: actor/instance/thread, invocation/turn ID, model call ID, effect reference and provider/internal tool call IDs. Context/state: system text, compacted conversation, tool specs and event-derived turn/model/spend state. Executor/effects: Effect services call providers and library implementations; event outcomes update the graph. Recovery uses [RT-OBJ-journal](#rt-obj-journal) where configured.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `thread.methods.message` waits for completed `{ text }` or raises failed/cancelled method errors; lower-level `invoke` returns a receipt first.
- Later read-back: committed turn events rebuild later conversation context; compacted summaries may replace earlier model-visible content; journal records also support result lookup after reopening.
- Delegated visibility: provider receives selected messages/system/specs and resolved file bytes; tool implementations receive call input; no child is mandatory in this example.
- Selection predicate: configured model and tools, turn needs-reply/waiting/running/failure/cancellation state, and context readiness determine proposals.
- Invalidation or expiry: cancellation requests stop outstanding work and settle the turn; summary boundaries replace visible history; host closure ends local fibers, while persisted records remain.
- Activation or effect: implemented delivery of model/tool effects and terminal result; actual exercised behavior and answer quality unobserved.
- Evidence limits: source trace only; external provider/storage success and summary fidelity are not established.

Mode: open user requests, not a fixed curriculum. The caller supplies a problem, not necessarily an expected answer. No semantic answer oracle is identified in this route. Conditional output JSON/schema checks validate conformance rather than truth. A model proposes response/tool work; code can reject duplicate tool IDs, unsupported structured-output configurations, malformed output and output-limit finishes. Human review of each content item is not established. SRC-1, `packages/examples/bun.ts`, `packages/examples/agents/meeseeks.ts`, `packages/examples/services.ts`, `packages/core/src/runtime/actors.ts`, `packages/agent/src/actor/methods.ts`, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/services/model.ts`.

> const response = yield* thread.methods.message({
>     text: yield* Config.String("EXPERIMENTAL_MESSAGE").pipe(Config.withDefault("Hello")),
>   }, { id: "example-message" })
> --- `packages/examples/bun.ts`

> const tools = yield* libraryTools()
> const context = yield* compact(messages)
> --- `packages/examples/agents/meeseeks.ts`

#### RT-RTE-governed-tools
Label: Composed permission and budget admission

Endpoints/progression: pending model tool call → library name check → permission decision → configured budget decision/reservation → governed execution proposal → `ExecuteTool` registry or synthesized denial/result. Owner: actor author chooses wrappers; permission/budget services answer asks; wrapper code enforces final plan. Model proposes tool name/input, policy or service decides, and wrappers can veto. `PermissionRequests` can return an immediate decision or a durable pending handle. Neither its interface nor the name “ask” requires a human. `parentBudgetRequests` allows computational parent replies; grant validation checks safe totals. State is [RT-OBJ-permission-policy](#rt-obj-permission-policy), budget state, pending tools and spend. SRC-1, `packages/agent/src/agent.ts`, `packages/agent/src/atoms/tools.ts`, `packages/agent/src/atoms/permission-request.ts`, `packages/agent/src/atoms/budget-request.ts`, `packages/agent/src/services/decisions.ts`, `packages/agent/src/services/tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: permitted calls invoke library methods; denials become non-counted error results; unresolved permission or budget waits/blocks.
- Later read-back: logged policies, decisions and spend govern later graph evaluations; decision records are matched to call IDs rather than universal grants.
- Delegated visibility: ask services receive action/resource/input and optional read-only metadata; parent budget authority receives reason, amount, usage and limit.
- Selection predicate: recognized counted tool, policy resource/action/read-only precedence, recorded permission result and configured budget allowance.
- Invalidation or expiry: decision identity is per call; logged policy/budget updates change subsequent evaluation; cancellation follows owning execution.
- Activation or effect: only the final governed plan proposes ordinary tool execution; unconfigured budgets explicitly pass through.
- Evidence limits: no observed approvals or deployed grant set; unwrapped tools, code-mode package acts and arbitrary host effects are outside this wrapper's demonstrated coverage.

Guarantee owner/enforcement: `withPermissions`/`withBudget` and `toolValue`, not the provider. Strength: policy. Covered path: ordinary wrapped library-tool execution; external contract: services must return valid decisions and libraries must honor their own effect boundaries. Mode: open requests. Answer oracle: inapplicable — permission/budget admission concerns authority and allowance, not expected problem answers. Proposed grant changes are admitted through validated service replies and logged events; denial is possible; rollback of an already executed external effect is not supplied by revoking later permission.

> if (!decision) return { position: "waiting", reason: "Waiting for tool permission" }
> return decision.allowed ? plan : { position: "ready", counted: false, error: decision.reason }
> --- `packages/agent/src/atoms/tools.ts`

> const budget = toolBudget(pendingTools, { configure: false })
> --- `packages/agent/src/agent.ts`

> if (!allowance.configured) return {
>       ...inner, events: { ...inner.events, ...budgetOutput.events }, acts: { ...inner.acts, ...budgetOutput.acts },
>     }
> --- `packages/agent/src/atoms/tools.ts`

#### RT-RTE-code-execution
Label: Current code mode and durable package RPC

Endpoints/progression: pending `execute` tool call → strict `{ code: string }` decoding → `EvaluateCode` → configured `Isolate.run` → ordinal package requests → `ExecutePackage` → recorded method outcomes → code result/logs/content → tool result. Owner: code-mode atom and services, with sandbox and library implementations as effect executors. The model proposes JavaScript; code selects configured libraries and rejects unknown names, invalid input, replay argument drift or omitted recorded calls. Fixed orchestration is symbolic; the model's code proposal becomes executable symbolic content, distinct from prompt prose. Ambient time/seed and accepted call outcomes allow replay comparison. SRC-1, `packages/agent/src/atoms/code-mode.ts`, `packages/agent/src/services/code-mode.ts`, `packages/platform/src/bun/isolate.ts`, `platform/bun/src/sandbox.ts`, `packages/platform/src/cloudflare/isolate.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: evaluation defers with a durable handle; final result/error/logs become `ToolReturned`, with stored-content handling where applicable.
- Later read-back: code execution entries and ordinal method outcomes are reread during resumed evaluation; resulting tool content can enter later model context.
- Delegated visibility: isolate receives code, ambient values and selected package/method names; RPC host receives method input; only returned values/logs cross back through this route, not a separate model transcript.
- Selection predicate: pending execute name, strict code input and selected catalog libraries; package method registry lookup and replay equality checks constrain dispatch.
- Invalidation or expiry: owning cancellation cancels outstanding package calls; Bun execution segments time out and subprocesses are killed; replay divergence fails evaluation.
- Activation or effect: JavaScript may coordinate multiple library effects; host implementations execute package methods independently of the code-body process.
- Evidence limits: no observed run, escape test or equivalent per-method permission/budget gate; external isolation strength remains unverified.

Guarantee owner/enforcement: code-mode registry/replay checks and platform isolate. Strength: protocol for call consistency, not a universal security invariant. Covered path: configured code-mode RPC; alternate direct library/model/host calls are not covered. External contract: isolate RPC confinement, method validation and external operation idempotency where replay can recur. Mode: open model-generated code. Admission of transient capability use is computational; human per-script approval is not established. No answer oracle. Recovery reuses recorded calls and fails drift; it does not undo remote side effects.

> if (recorded && (recorded.package !== call.package || recorded.method !== call.method || !isDeepStrictEqual(recorded.input, call.input))) {
>           drift = `Nondeterministic code mode: library call ${call.ordinal} differs from its recorded method or arguments`
>           return yield* Effect.fail(drift)
>         }
> --- `packages/agent/src/services/code-mode.ts`

#### RT-RTE-legacy-server
Label: Deprecated hosted server invocation

Endpoints/progression: server-mounted actor → deprecated `actorClient` → existing invocation or prepared method event → commit root → drive host → component inference/tool/code transitions → method state read from log → terminal reply. Owner: older Bun host and component root. Invocation identity includes method, key and current epoch; coordinate includes actor/instance/thread. The shipped built-in actor composes code-mode packages, budget/escalation, compaction and one-shot output validation; the legacy model executor renders component-provided context, calls `collectResponse`, preserves provider continuation/evidence and converts the response into an inference action. The atom implementation is not this executor. SRC-1, `platform/bun/src/create-host.ts`, `apps/server/src/host.ts`, `apps/server/src/actor.ts`, `packages/deprecated/agent/src/component/infer/index.ts`, `packages/deprecated/agent/src/model/execution/index.ts`, `packages/deprecated/agent/src/component/code/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: backend submit returns acceptance; client invocation loops on log-derived method state and returns output or throws failed/cancelled/deadline errors.
- Later read-back: host reads stored thread events for invocation identity and result, restores instance databases and recovers runtimes; legacy inference renders trajectories from event-derived state.
- Delegated visibility: model receives rendered component system/tool/context view; execute code sees packages; child-agent package can delegate separately.
- Selection predicate: actor/method/thread existence, method epoch and existing receipt; component inference and routed tool view determine subsequent transitions.
- Invalidation or expiry: client waits against receipt deadline and abort signals; host close ends lifetime; detailed legacy cancellation/retry parity with atoms is uninspected.
- Activation or effect: built-in filesystem, HTTP, workspace and child packages are available to code mode; outputValidateOnce requests explicit handling without native type proof.
- Evidence limits: no observed server operation; deeper legacy state-machine enforcement and complete Cloudflare equivalence are not asserted.

Mode: open method requests. Model proposes answer/code; components and package dispatch decide execution. The server assembly's escalation callback grants computationally; an operator veto is not shown there. Output-validation machinery is not a semantic answer oracle. Grant/rejection/recovery rules belong to this legacy composition, not [RT-RTE-governed-tools](#rt-rte-governed-tools).

> let receipt = existingInvocation(events, reference)
>       if (receipt === undefined) {
>         const prepared = prepareMethodInvocation({ reference, method, input, at: Date.now(), ...(call.timeoutMs === undefined ? {} : { timeoutMs: call.timeoutMs }) })
>         await host.commitRoot(formatThreadAddress(coordinate), prepared.event)
>         receipt = prepared.accepted
>       }
>       pool.track(host.drive())
>       return receipt
> --- `platform/bun/src/create-host.ts`

> { authority: caller(), requests: { decide: request => request.grant() } }
> --- `apps/server/src/actor.ts`

#### RT-RTE-child-invocation
Label: Child actor delegation through agents library

Endpoints/progression: current `agents.run`/`delegate_task` → core `Actor.invoke` with request-derived identity and target coordinate → execution handle → eventual inbox completion; cancel invokes `Actor.cancel`. Owner: parent model proposes a message; configured Actor service owns child execution. The library passes only message and a tool budget, not the parent transcript. Default actor name is tardie and default requested tool allowance is 20. Actual enforcement depends on the target actor/service accepting and applying that input. `localActors` is a separate scope-local implementation with endpoint-bound handles and in-memory entries; a handle from another scope rejects rather than restarting work. SRC-1, `packages/libraries/src/agents.ts`, `packages/core/src/runtime/actors.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: execution handle, not synchronous child answer.
- Later read-back: durable handle completion is the library contract; actual persistence depends on configured Actor service; localActors retains results only for its scope.
- Delegated visibility: child receives selected message and budget; parent receives result/inbox messages, not demonstrated full child context.
- Selection predicate: configured actor or default actor, request-derived target identity, configured child budget and Actor service routing.
- Invalidation or expiry: explicit cancellation; local scope loss makes local handles unavailable; external/durable executor lifecycle is service-specific.
- Activation or effect: separate child work can execute with its own context; no observed exercise or improved performance.
- Evidence limits: library alone does not establish universal depth limits, budget enforcement in arbitrary targets, cross-host durability or inherited parent permissions.

Mode: open delegated problems. No answer oracle. This context separation resembles a frame: selected input enters and a return escapes; retained actor journals and asynchronous notifications can outlive the parent's immediate call, so it is not simply a stack pop.

> .annotate(MethodDescription, `Start a child agent with a message and at most ${budget.toolCalls} tool calls per turn. Model spend is uncapped. Returns a durable handle immediately; its result arrives in the inbox.`)
> --- `packages/libraries/src/agents.ts`

> poll: handle => Effect.sync(() => lookup(handle)?.result ?? { status: "rejected" as const, reason: "Local actor handle is no longer available" }),
> --- `packages/core/src/runtime/actors.ts`

#### RT-RTE-artifact-admission
Label: Build and server actor replacement

Endpoints/progression: source actor → Bun bundle/import and definition checks → digest manifest → build directory replacement; separately pushed module/manifest → server checks/import → close current host → open replacement → artifact directory swap. Owner: caller supplies source/artifact; CLI/server code decides structural admission. Human authorship or approval is unresolved from these APIs. Form is [RT-OBJ-actor-artifact](#rt-obj-actor-artifact). Source, prompts, tools and control flow can all change inside executable actor modules. SRC-1, `apps/cli/src/build.ts`, `apps/server/src/host.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: built directory/manifest or accepted actor summary; invalid schema/name/reserved name/module/digest/definition or failed installation rejects.
- Later read-back: server mounting imports persisted module/manifest; new actor behavior affects subsequent invocations; existing stored state requires compatible code.
- Delegated visibility: build and server dynamically import module code in the host; this is not the generated-code sandbox.
- Selection predicate: explicit entry/artifact name, schema/name/module checks, digest equality and API-generation-specific definition checks.
- Invalidation or expiry: replacement closes current host; CLI restores previous destination if final rename fails, then removes previous on success; server push catch removes incoming content but does not demonstrate restoration of the already closed runtime.
- Activation or effect: accepted replacement changes hosted executable actor definitions; successful live exercise is unobserved.
- Evidence limits: integrity/shape checks do not validate behavioral quality or safety; build accepts atom artifacts but inspected server loader expects component actors; API authorization/deployed trust boundary is not assessed from this push function alone.

Trigger/proposed change: explicit build or push. Admission/rejection: code checks; caller can withhold submission, but no human per-content approval follows from generic caller identity. Rollback: bounded filesystem restore in build, not general state migration or external-effect reversal. Guidance shaping a proposal is uninspected for arbitrary pushes; improvement instructions are a separate route below. Mode: open artifact submissions. No score-based answer oracle or improvement gate is implemented here.

> const definition = await definitionOf(join(temporary, manifest.module), manifest)
>           const current = runtimes.get(manifest.name)
>           if (current !== undefined) {
>             await current.host.close()
>             runtimes.delete(manifest.name)
>           }
> --- `apps/server/src/host.ts`

#### RT-RTE-optimization-guidance
Label: NPO and GEPA improvement procedures

Endpoints/progression: user-authorized improvement problem → evaluation brief and unchanged baseline → complete rollout traces/rubric scores → prompt or harness candidate → development selection and held-out comparison → authorized source promotion/build/deploy. Owner: optimizing agent following source-native instructions, with user-controlled scope/thresholds. Evidence layer: doctrine/design only, SRC-1, `skills/tardigrade/references/npo.md`, `skills/tardigrade/references/gepa.md`. These are shipped instructions, not executed actions in this analysis.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: prescribed comparison report, selected source and rebuilt digest; no optimizer invocation is observed.
- Later read-back: instructions prescribe saved candidate prompt/source, parent/diff/digest, scores and thread IDs; NPO teacher consumes recent prompt versions, trajectories and score reasons in a feedback window; promoted source later feeds actor operation.
- Delegated visibility: NPO teacher receives selected traces and rewards; instructions require redaction and disclosure before external teacher use; GEPA optimizer inspects informative traces.
- Selection predicate: NPO single-lineage revision and declared best-development rule; GEPA Pareto candidate retention without regression or constraint violation; held-out baseline comparison before promotion.
- Invalidation or expiry: bounded iteration/run/time/cost limits and no trace-supported hypothesis stop search; baseline preservation supports fallback, but no observed rollback/deployment is supplied.
- Activation or effect: prescribed edit of actor instructions or allowed harness code; reaching later live behavior and improved outcomes remain unobserved.
- Evidence limits: no supplied candidate lineage, scores, causal comparison or live promotion; instructions are not hard runtime admission enforcement.

Admission roles: teacher/optimizing agent proposes; optimizing agent applies rubric and selection; user can alter limits/thresholds and restrict deployment. No universal final human per-candidate approval is specified. Answer oracle: deterministic machine-readable checks when applicable, otherwise evidence-scored subjective criteria; task-specific expected answers/reference outcomes/provider are not supplied. Mode: bounded development experiments with held-out cases, distinct from open production requests. Objective is to be specified before edits and independently of candidate text. What persists is prescribed actor/prompt source and evaluation lineage, not parameter updates.

The procedures request reusable explanations and trace-directed revisions, but contain no supplied formulated candidate theory or actual content-directed criticism episode. Consequently this record does not classify them as an exercised theory builder. Under theory-builder conditions 1–4, the conditional architectural assessment is:

- condition 1 conclusion status: afforded
- condition 2 conclusion status: afforded
- condition 3 conclusion status: claimed
- condition 4 conclusion status: claimed

Condition 1 has editable localized instruction text, although whether a candidate states a theory depends on its content. Condition 2 has teacher/optimizer interpretation and later actor prompts, not demonstrated compliance or dependence on a particular theory. Conditions 3 and 4 have prescribed trace explanation, revision and reuse in later rounds; a score or a reusable lesson alone does not establish content-directed criticism with explicit placement of blame. These are method affordances/requests, not observed candidate states. Addressability: actor instruction text is directly editable, with finer granularity depending on candidate content. Persistence horizon: prescribed across search rounds and deployed sessions. Learning: future-capacity improvement unestablished without outcomes/attribution. Reflection: prescribed inspection of the actor's own traces can shape its text, but that causal loop is not observed. Autonomous theory builder and reflective theory builder are not established from instructions alone. Self-improvement: a dormant prescribed pathway targets the actor's own behavior-determining instructions, but the evidence-to-update, live installation and later exercise links are not supplied; no exercised attribution follows.

> Give the teacher the current feedback window. Include each prompt version, its trajectories, rewards, and score reasons.
> --- `skills/tardigrade/references/npo.md`

> Retain the proposal when it improves at least one case without regressing another case or violating a constraint.
> --- `skills/tardigrade/references/gepa.md`

> Tardigrade runs do not record an immutable actor digest.
> --- `skills/tardigrade/references/gepa.md`

> Promote the selected source under the intended actor name within the user's authorized scope. Rebuild it, verify the digest, and deploy it only to the authorized target.
> --- `skills/tardigrade/references/gepa.md`

### Claims

#### RT-CLM-request-before-execution
Label: Committed request before core effect dispatch

Claimed operation: current core execution records an effect request before executing its work, commits state changes before replacing the current snapshot, and rebuilds state from checkpoint/suffix plus accepted inputs on recovery. Owner/enforcement: `drain`/`commit` and journal adapter. Guarantee strength: invariant for core request-before-dispatch; protocol for persistent recovery, conditional on journal/SQL durability and compatible execution services. Covered paths: effects driven by current core and its journal; alternatives: no-journal core operation, arbitrary external calls, custom adapters and legacy host do not inherit a blanket durability guarantee. External effects require their own idempotency/recovery contract. SRC-1, `packages/core/src/runtime/execution.ts`, `packages/platform/src/shared/sql-journal.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!recorded) return yield* Effect.fail(new RuntimeError("Effect execution requires a committed request"))
> --- `packages/core/src/runtime/execution.ts`

> const history = options.journal
>         ? checkpoint ? yield* options.journal.readAfter(checkpoint.position) : yield* options.journal.read
>         : (options.events ?? []).map(event => ({ event }))
> --- `packages/core/src/runtime/execution.ts`

> for (const work of deferred) if (work.handle.executor === "local") localRecovery.set(effectKey(work.ref), work)
> --- `packages/core/src/runtime/execution.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-model-instructions
Label: Actor instructions into model decisions

Consumer: configured inference model. Channel: system string plus transformed conversation/tool-spec input constructed by the actor and model adapter. Force: model-interpreted guidance, not deterministic compliance. Horizon: each inference invocation; actor source persists across invocations when installed, and journal-derived context/summary can carry prior conversation into later invocations. Selected tool specifications inform proposal generation but do not alone grant execution. SRC-1, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/services/model.ts`, `packages/agent/src/atoms/compact.ts`. Links: [RT-CMP-model](#rt-cmp-model), [RT-RTE-bun-message](#rt-rte-bun-message), [RT-RTE-optimization-guidance](#rt-rte-optimization-guidance).

> input: { model: selection.model, system: `${input.system}${correctionSystem}`, tools: input.tools.view.specs, context: messages, ...(input.output === undefined ? {} : { output: input.output }) },
> --- `packages/agent/src/atoms/infer.ts`

#### RT-BAP-executable-actor
Label: Installed actor code into runtime effects

Consumer: host module loader and actor runtime. Channel: imported `actor.mjs` and configured service/library implementations. Force: executable symbolic code, able to determine composition and host-side effects rather than merely advise a model. Horizon: mounted host lifetime and subsequent mounts from persisted artifacts. Integrity checks do not sandbox the imported module or guarantee behavioral improvement. SRC-1, `apps/server/src/host.ts`, `apps/cli/src/build.ts`. Links: [RT-OBJ-actor-artifact](#rt-obj-actor-artifact), [RT-RTE-artifact-admission](#rt-rte-artifact-admission).

> const loaded: unknown = await import(`${pathToFileURL(modulePath).href}?digest=${encodeURIComponent(expected.digest)}`)
> --- `apps/server/src/host.ts`

## Annotations

none
