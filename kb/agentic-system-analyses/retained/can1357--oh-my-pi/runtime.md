---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "oh-my-pi runtime baseline: CLI session, model/tool control, delegated contexts and alternate effect/admission paths at the frozen commit"
run-id: AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01
reviewed-boundary: "2431e8a8716a4da73ae327a412f6d54c22f681e5"
---

# oh-my-pi runtime report

## Runtime account

oh-my-pi constructs and runs coding-agent sessions. The shipped CLI owns model dispatch and local tool execution, rather than merely returning a prompt for another runtime to execute. The [boundary](boundary.md) establishes the CLI → launch → main → SDK → AgentSession → Agent chain, and deliberately retains a **complete artifact, partial loop** boundary. This report extends implementation inspection within SRC-1, not that boundary's coverage claim. No execution evidence was supplied or produced. Wiring, policy and declared intent below do not establish activation, reliable model compliance or benefit.

### Ordinary invocation and next-step ownership

An ordinary headless invocation supplies a coding request to print mode. Main constructs the session and dispatches interactive, RPC or print modes; print mode subscribes to session events, waits for MCP startup, refreshes its tool roster and calls `session.prompt`. Its optional strict-readiness setting prevents dispatch when required MCP servers are unavailable. Text and JSON are different output surfaces over this session, not different core reasoning loops (SRC-1, `packages/coding-agent/src/main.ts`, `packages/coding-agent/src/modes/print-mode.ts`). [RT-RTE-session-turn](#rt-rte-session-turn) records the route.

The human/calling program supplies the problem. AgentSession coordinates the turn; Agent and the core loop own progression. The model proposes assistant text and structured tool requests. Code owns which requests are runnable, resolves tool identities, validates arguments, applies pre-dispatch rules and invokes executors. The SDK supplies current system instructions, model selection, active tools, credentials, context transformations and provider wrappers. It installs extension context handlers before conversion to provider messages and performs model-specific image transformations afterwards. Thus a stored conversation is not necessarily identical to what reaches a provider. The provider call includes transformed instructions/history and normalized tool definitions, or an in-band encoding when an owned dialect is selected (SRC-1, `packages/coding-agent/src/sdk.ts`, `packages/agent/src/agent-loop.ts`; [RT-OBJ-system-prompt](#rt-obj-system-prompt), [RT-CMP-agent-model](#rt-cmp-agent-model)).

Tool results join the conversation for another model step. Steering may force a next step; asides and follow-ups drain at the stop boundary. Once those queues are empty the loop emits its terminal event. Deadline and abort handling bound further dispatch, not the truth of the answer. Truncated calls are paired with skipped results rather than treated as completed work. The loop also supports replay of pending tool calls before the next model request. These are recovery mechanisms, not an exactly-once guarantee for arbitrary external effects (SRC-1, `packages/agent/src/agent-loop.ts`). Session persistence and reconstruction exist, but their detailed retention, compaction, backend write and later-recall semantics remain the memory analyst's responsibility.

### Effects, grants and forcing cases

The capability surface includes registry tools, mounted device/MCP tools, shell backends, Cursor exec frames and extension code. The current grant is narrower: request-visible active tools, configured policies, tool tiers and bridge-specific grants. SDK alias recovery distinguishes the advertised request snapshot from a live roster that may change mid-stream. No concrete user's grant set or deployed operating-system/container isolation was supplied. The inspected approval gates are runtime policy checks, not evidence of deployment isolation (SRC-1, `packages/coding-agent/src/sdk.ts`, `packages/coding-agent/src/tools/approval.ts`).

Four forcing cases qualify the ordinary dispatch account:

1. **An extension revises an otherwise acceptable tool request into a denied request.** Core dispatch revalidates revised arguments; the wrapper resolves approval against effective parameters, not merely the original proposal. Deny and rejection stop that wrapped invocation. This is a policy guarantee owned by ExtensionToolWrapper and AgentSession, not a guarantee covering arbitrary extension I/O ([RT-RTE-tool-dispatch](#rt-rte-tool-dispatch)).
2. **Cursor produces an effect outside ordinary tool-call dispatch.** Registry-backed frames use wrapped tools, while native delete/resource-download frames bypass that wrapper. Separate bridge checks are therefore load-bearing. Native delete checks a live mutation grant and a write policy; prompt-required mutations are refused because that channel cannot request approval. Already executed Cursor calls are excluded from ordinary re-execution ([RT-RTE-cursor-exec](#rt-rte-cursor-exec)). This defeats the broader claim that every effect passes through the same wrapper.
3. **Work starts before final tool dispatch.** Optional speculative local reads and streamed task launches have an additional host gate. Local reads require supported effects and captured evidence; extension lifecycle hooks or approval not resolving to allow veto early execution. Commit validation rechecks evidence and authorization. This is not permission for arbitrary speculative writes ([RT-RTE-speculative-read](#rt-rte-speculative-read)). Task-launch speculation shares the policy gate, but its complete cancellation/commit protocol was not inspected.
4. **A loaded extension performs work while importing or binding.** Extension modules and factories execute inside the host process. The host guard patches exit primitives and restores stdin state; it does not mediate all module I/O through tool approvals. Import errors are retained and failed factories are not accepted as loaded extensions. This bounds both the tool-policy claim and what loading rollback means ([RT-RTE-extension-load](#rt-rte-extension-load)).

Shell execution itself has multiple concrete backends: local embedded execution, interactive PTY and ACP terminal integration are visible in BashTool. Its approval concerns the submitted command; a shell command can perform many underlying operations. No claim here treats command-pattern policy as per-system-call confinement (SRC-1, `packages/coding-agent/src/tools/bash.ts`). External providers, MCP implementations and user-installed code remain excluded implementations under the boundary.

### Delegation, context and admission

Task delegation builds another AgentSession. It renders selected agent/context/plan/worktree/schema/peer information into the child's instructions rather than giving the parent a transparent view of every child token. A child gets its own session manager and model/settings selection; optional worktrees change its working directory. The return is finalized output with limits and optional artifacts, not an intact child context. Persisted child sessions can be reopened and revived. This resembles a separate working frame with selected arguments and a return, but retained files, shared tools and revived sessions mean it is not simply popped and erased ([RT-RTE-task-spawn](#rt-rte-task-spawn)). No general filesystem isolation follows from a separate conversation.

Product changes can be made through admitted edit/write or shell calls. The model proposes; schema and runtime policy decide executable admissibility; a human veto exists only where approval requires and obtains it. There is no general per-patch semantic acceptance oracle in the inspected dispatch path. A completed command/tool result is evidence reported back to the model, not proof that a product is correct. Rollback of arbitrary mutations is executor/project-dependent and is not established by the loop's retry machinery ([RT-RTE-tool-dispatch](#rt-rte-tool-dispatch)).

Capabilities change through extension discovery/import/binding and runtime tool registration. The SDK wraps registered tools, subscribes to subsequent registrations and supports suspension/re-resolution. Module acceptance checks a factory interface and successful binding, not a demonstrated-benefit criterion. This is capability admission, not evidence of autonomous improvement ([RT-RTE-extension-load](#rt-rte-extension-load)). Knowledge/instruction revision through memory backends and automatic learning remains unassessed here; the main stream wrapper explicitly distinguishes main-loop calls from side-channel, advisor and maintenance calls. Their existence does not establish that they share every main-loop control.

### Coverage and limits

Added SRC-1 implementation coverage: selected provider-context preparation, tool dispatch and stop/recovery branches in `packages/agent/src/agent-loop.ts`; model mutation in `packages/agent/src/agent.ts`; SDK context/provider wrappers, bridge and extension registration wiring; selected AgentSession preflight code; print-mode prompt/event handling; `packages/coding-agent/src/tools/approval.ts`, selected BashTool backend execution; extension loader and host guard; Cursor direct-mutation policy; task session construction, revival and output artifact handling; speculative host authorization/evidence checks. README product wording supplies doctrine/design evidence only.

Interactive/RPC mode internals, cross-language drivers, collaboration, all provider adapters, eval host-call execution, advisor/maintenance loops, autolearn, detailed compaction strategies and memory backends were not traced end to end. Available source is not an access gap. These limits prevent a whole-system enforcement, reliability, learning or production-machinery-improvement conclusion. No bounded evidenced-absence claim is made from those omissions.

## Shared records

### Components

#### RT-CMP-agent-model
Label: Agent model

Source-native identity: the model in Agent state, selected by SDK/session configuration and read by provider-call preparation. Representational form: distributed-parametric inference in an external model service; the local `Model` descriptor is symbolic metadata, not the weights. Storage substrate: provider-side parameters are outside inspected source; local descriptors/settings live in process and session/configuration state. SRC-1, `packages/agent/src/agent.ts`, `packages/agent/src/agent-loop.ts`, `packages/coding-agent/src/sdk.ts`.

Parameter change during operation: uninspected — the client performs inference and does not expose provider weight updates in the inspected route. Exact version pinned: not established; the repository commit pins client code, not provider weights. Mutable endpoint resolving to another model: possible; Agent permits model replacement and resolver-based adoption, and task execution installs model fallback selection. Endpoint-internal substitution is uninspected. Fixed weights or absence of learning must not be inferred. Dedicated advisor/maintenance model instances were not individually resolved.

> const model = config.getModel?.() ?? config.model;
> --- `packages/agent/src/agent-loop.ts:1919-1919`

> this.#state.model = resolved;
> this.#syncTokenizer(resolved);
> --- `packages/agent/src/agent.ts`

### Operative objects

#### RT-OBJ-system-prompt
Label: System prompt

Source-native identity: Agent's `systemPrompt`, with SDK-rendered instructions and task-specific child additions. Representational form: natural-language instructions interpreted by a model, distinct from executable tool policy. Storage substrate: string blocks in process; templates/configuration are files. Consumer: provider model through context construction. SRC-1, `packages/coding-agent/src/sdk.ts`, `packages/coding-agent/src/task/executor.ts`, `packages/agent/src/agent-loop.ts`.

> return [...defaultPrompt, subagentPrompt];
> --- `packages/coding-agent/src/task/executor.ts`

Its delivery supplies guidance; no observed compliance is established. Prompt text does not replace the execution vetoes in [RT-RTE-tool-dispatch](#rt-rte-tool-dispatch).

#### RT-OBJ-tool-call
Label: Tool call

Source-native identity: an assistant content block carrying call ID, name and arguments. Representational form: symbolic dispatch request, even where argument values contain natural-language prose. Storage substrate: in-process message arrays, with session-event persistence handled by AgentSession. The dispatch consumer resolves identity and validates arguments before execution. SRC-1, `packages/agent/src/agent-loop.ts`.

> const effectiveArgs = validate(argsForExecution);
> if (effectiveArgs === undefined) continue;
> entry.args = effectiveArgs;
> --- `packages/agent/src/agent-loop.ts`

### Routes

#### RT-RTE-session-turn
Label: Session turn

Endpoints/progression: caller request → print-mode `session.prompt` → AgentSession/Agent → transformed provider context → model output → tool cycle → terminal events/output. Owner: shipped CLI/session and core loop; model proposes the next semantic action but code schedules it. Open coding requests, not a fixed evaluation curriculum. No answer oracle is wired by the inspected print dispatch. Human supplies the request; runtime/model determine intermediate steps. SRC-1, `packages/coding-agent/src/modes/print-mode.ts`, `packages/coding-agent/src/sdk.ts`, `packages/agent/src/agent-loop.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed session events, JSON events or text-mode answer; core loop ends when pending tools/messages and stop-boundary queues are exhausted or termination controls intervene.
- Later read-back: session persistence/resume is wired in the boundary's inspected SDK/session path; precise retained-message selection and compaction belong to the memory account.
- Delegated visibility: task calls can return bounded child output; see [RT-RTE-task-spawn](#rt-rte-task-spawn).
- Selection predicate: dispatched prompt after startup; print mode can suppress prompts on strict MCP readiness failure; request-time context hooks and provider transforms select/alter model-visible material.
- Invalidation or expiry: abort/deadline curtail work; model/configuration/context can change between requests; no semantic freshness guarantee for answers.
- Activation or effect: provider inference and tool-result accumulation are implemented; actual request execution and changed user outcome unobserved.
- Evidence limits: no supplied trace; other CLI modes share construction but their detailed lifecycle was not inspected.

> const withContext = await extensionRunner.emitContext(messages, signal);
> return wrapSteeringForModel(withContext);
> --- `packages/coding-agent/src/sdk.ts`

> const normalizedMessages = normalizeMessagesForProvider(llmMessages, model);
> --- `packages/agent/src/agent-loop.ts`

> pendingMessages = [...lateSteering, ...asideMessages, ...followUpMessages];
> --- `packages/agent/src/agent-loop.ts`

Working-context control: extensions can replace the message list before conversion; provider transforms redact text, rasterize selected content if enabled, budget images and drop unreadable images. These controls determine delivered content, not simply accumulated history. Their runtime settings and resulting wire contents were not observed. This report does not infer retained memory from request-local transformations.

#### RT-RTE-tool-dispatch
Label: Tool dispatch

Endpoints/progression: model tool call → core preparation/validation → AgentSession preflight/extension revision → ExtensionToolWrapper policy and approval → tool executor → result in model context. Owners: core, session and wrapper; model proposes a concrete action; code or a prompted human can veto it. Open-request operating mode. Answer oracle: none established; schema validity and approval test admissibility, not task correctness. SRC-1, `packages/agent/src/agent-loop.ts`, `packages/coding-agent/src/session/agent-session.ts`, `packages/coding-agent/src/extensibility/extensions/wrapper.ts`, `packages/coding-agent/src/tools/approval.ts`, `packages/coding-agent/src/tools/bash.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tool text/structured result or error, plus lifecycle events; successful calls may supply additional context.
- Later read-back: tools can alter project files consumed by later calls; session persistence may retain requests/results. Detailed retention is not assessed here.
- Delegated visibility: a task tool crosses to another session; ordinary tool return does not expose executor internals.
- Selection predicate: resolved tool in the applicable request/registry/device surface, valid arguments and successful gates; runnable stop reasons exclude incomplete output-limit calls.
- Invalidation or expiry: revised arguments are revalidated; approval is recomputed for effective input; denied, blocked, aborted or truncated requests do not count as successful dispatch.
- Activation or effect: admitted executor can read/write files, execute commands or invoke remote tools; actual effects are unobserved.
- Evidence limits: no universal gate for arbitrary extension-side I/O or excluded remote internals; current deployment policies unknown.

Guarantee owner/enforcement: AgentSession `beforeToolCall` plus wrapper `execute`; guarantee strength: policy. Covered paths: wrapped built-ins, registered tools, and wrapper direct execution; ordinary loop additionally validates revisions. Alternate paths: Cursor direct mutations use a distinct gate; speculative work uses host authorization; extension imports do not become tool requests. Required external contract: UI truthfully returns approval, tools honor their execution contract, and effects are not independently performed outside these paths. Implementation conclusion status is wired; operation conclusion status is uninspected, as above.

> if (beforeResult?.block) {
> 	entry.blocked = true;
> 	entry.blockReason = beforeResult.reason;
> 	continue;
> }
> --- `packages/agent/src/agent-loop.ts`

> const resolvedArgs = approvalArgs(effectiveParams, context);
> const resolved = resolveApproval(this.tool, resolvedArgs, approvalMode, userPolicies);
> --- `packages/coding-agent/src/extensibility/extensions/wrapper.ts`

> if (!approved) {
> 	cancelPreflight();
> 	throw new Error(`Tool call denied by user: ${this.tool.name}`);
> }
> --- `packages/coding-agent/src/extensibility/extensions/wrapper.ts`

Admission account: coding request triggers a proposed edit/write/shell change, guided by system instructions, user request and available tool results. The wrapper admits the execution, not a semantically reviewed final patch. Configured settings normally resolve to schema-default `yolo`; missing settings resolve to `always-ask`. Consequently initiating a session is not per-content approval. Local tool denials and human rejection exist, but generic shell/file mutations have no general transactional rollback at this layer. Retry is not reversal; file changes persist according to executor/project storage.

> if (!settings) {
> 	return { approvalMode: "always-ask", userPolicies: {} };
> }
> --- `packages/coding-agent/src/tools/approval.ts`

#### RT-RTE-cursor-exec
Label: Cursor exec

Endpoints/progression: provider exec frame → CursorExecHandlers → registry-backed executable or native mutation branch → bridge result/events. Owner: Cursor bridge configured by SDK with live cwd, tools, context and mutation predicate. Decision form: symbolic frame/action and code policy. SRC-1, `packages/coding-agent/src/cursor.ts`, `packages/coding-agent/src/sdk.ts`, `packages/agent/src/agent-loop.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sanitized bridge result and tool events; already-resolved blocks are excluded from ordinary dispatch.
- Later read-back: native mutation changes project files; later file access can consume them; no bridge-specific memory revision established.
- Delegated visibility: provider receives frame response; ordinary transcript can carry synthesized tool blocks without re-executing the effect.
- Selection predicate: registry resolution for tool frames; direct delete requires live mutation grant and write policy resolving to allow.
- Invalidation or expiry: active grant/cwd read live; deny or prompt-required write policy rejects native mutation.
- Activation or effect: native delete calls local filesystem removal; resource-download mutation uses the separate write-policy gate; deployed activation unobserved.
- Evidence limits: selected bridge mutation path inspected, not every provider frame or external provider implementation.

> if (approval.policy === "allow") return null;
> return approval.policy === "deny"
> 	? `Tool "${toolName}" is blocked by user policy.`
> 	: `Tool "${toolName}" requires approval, which this channel cannot request.`;
> --- `packages/coding-agent/src/cursor.ts`

> fs.rmSync(absolutePath);
> --- `packages/coding-agent/src/cursor.ts`

Guarantee strength: policy. Owner/enforcement: bridge live grant and `refuseByWritePolicy`, not ExtensionToolWrapper for native frames. External contract: SDK supplies truthful current grants/settings; provider frame identity and bridge handling work as implemented. The endpoint can propose changes but cannot obtain interactive approval in this native channel; rejection produces a tool error. No general undo of a successful delete is implemented in the inspected branch. Guidance is the provider request/current coding context; persisted result is a file mutation and bridge/session output, not a separately admitted theory. Answer oracle: none; operating mode: provider-mediated open work. Implementation is wired and operation uninspected.

#### RT-RTE-task-spawn
Label: Task spawn

Endpoints/progression: task specification → child settings/model/tool selection → session manager/open → `createAgentSession` → prompt loop → output finalization/artifact → parent return. Owner: task executor and child AgentSession. Child principal has its own registry identity and optional persisted session; parent task call identifies the spawning tool call. Natural-language agent/task instructions guide the model; symbolic settings and schema control construction/finalization. SRC-1, `packages/coding-agent/src/task/executor.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: finalized child output with tail truncation and status/usage; cancelled work can expose salvage text rather than imply no work occurred.
- Later read-back: optional JSONL child session can reopen/revive; raw output may persist as `<id>.md` and structured data as `<id>.json`; revival updates output artifacts only under stated yield conditions.
- Delegated visibility: selected context, agent instructions, plan/worktree/schema and optional peer roster enter child prompt; parent receives output/artifact metadata, not automatic full child history.
- Selection predicate: task specification and agent/model/settings resolution; persisted file if supplied, otherwise in-memory manager; structured-output policy can be strict or permissive.
- Invalidation or expiry: signal/runtime limits can abort; failed startup disposes sessions resolving after cancellation; revival remints MCP proxies from current manager state.
- Activation or effect: child can run granted tools in effective cwd/worktree; separate conversation isolates context, not necessarily effects or credentials.
- Evidence limits: full task-tool admission, every isolation backend and complete structured-output policy not traced; no observed delegated run or schema-compliance rate.

> const effectiveCwd = worktree ?? cwd;
> --- `packages/coding-agent/src/task/executor.ts`

> : Promise.resolve(SessionManager.inMemory(effectiveCwd));
> --- `packages/coding-agent/src/task/executor.ts`

> void sessionPromise?.then(created => created.session.dispose()).catch(() => {});
> --- `packages/coding-agent/src/task/executor.ts`

> await writeArtifact(candidatePath, rawOutput);
> --- `packages/coding-agent/src/task/executor.ts`

Decision roles: foreground model/caller proposes task and selected input; code constructs and finalizes; child model chooses work within its session. Human per-child approval is not established by this executor inspection. Answer oracle: output schema is a format constraint, not a reference answer. Operating mode: open delegated task, with bounded retry/finalization machinery. A child's proposed product edits use its tools' admission mechanisms; this executor does not supply a general correctness veto or merge oracle. Artifact persistence is not proof of valid work.

#### RT-RTE-speculative-read
Label: Speculative read

Endpoints/progression: streamed local-read candidate → host authorization → evidence capture → speculative execution → current-policy/resource/evidence validation → committed result or discard/fresh dispatch. Owner: speculative coordinator plus coding-agent host. Decision form: symbolic effect/resource metadata and byte digest; no separate deciding model in the host checks. SRC-1, `packages/coding-agent/src/speculation/host.ts`, `packages/agent/src/agent-loop.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reusable read result only if commit checks accept it; rejected speculation is not an authoritative tool result.
- Later read-back: inapplicable — this route reads content and caches candidate evidence for dispatch, not a retained knowledge revision.
- Delegated visibility: result can reach foreground model after dispatch commit; streamed task launches have a related policy gate but are not this read route.
- Selection predicate: feature enabled, read/local_read effect, one valid read resource, supported text target, lifecycle/approval allow, and finalized call surviving hook preparation.
- Invalidation or expiry: evidence mismatch, changed target or policy and missing evidence reject commit; early execution is vetoed by lifecycle handlers or non-allow approval.
- Activation or effect: optional overlapped filesystem read; no demonstrated latency or correctness benefit.
- Evidence limits: host gates and core hookup inspected, not complete scheduler proof or experimental races; guarantee is bounded to supported speculative reads.

> if (hasLifecycleHandlers(this.extensionRunner)) {
> 	return { allowed: false, reason: "active extension lifecycle handler" };
> }
> --- `packages/coding-agent/src/speculation/host.ts`

> if (approval.policy !== "allow") return { allowed: false, reason: "tool approval is not auto-allow" };
> --- `packages/coding-agent/src/speculation/host.ts`

Guarantee owner/enforcement: host authorization/capture/validate plus coordinator finalization; guarantee strength: protocol. Covered paths: supported direct/eval local-read effects, not arbitrary shell/network/write effects. External contract: filesystem identity/digest checks and coordinator invocation of host phases. Main dispatch still owns authoritative completion. Implementation is wired; operation is uninspected.

#### RT-RTE-extension-load
Label: Extension load

Endpoints/progression: discovered/configured path → module import → factory check → binding against fresh ExtensionAPI/runtime → registered hooks/tools/providers → SDK registry and live-registration handling. Owner: extension loader and SDK. Source form: symbolic executable JS/TS with any embedded prose interpreted by its consumers. Storage: installed/project files, loaded in the host process. SRC-1, `packages/coding-agent/src/extensibility/extensions/loader.ts`, `packages/coding-agent/src/extensibility/utils.ts`, `packages/coding-agent/src/sdk.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: loaded extensions/runtime and error list; bound registrations become capability surface, wrapped for ordinary tool execution.
- Later read-back: installed extension files can be loaded on later sessions; this inspection does not establish who authored/approved their content or a trace-fed revision route.
- Delegated visibility: prepared factories can rebind fresh instances for child sessions; module graph need not re-evaluate for each child.
- Selection predicate: discovery/configuration path and valid factory export, followed by successful factory binding; restricted-tool mode disables ambient discovery paths.
- Invalidation or expiry: failed import/bind yields an error; provider registration checkpoint restores pending entries on factory failure; SDK supports suspension and effective registration re-resolution.
- Activation or effect: module/factory code runs during loading, before later tool calls; registered hooks can transform context and registered tools can act later.
- Evidence limits: host guard covers exit/stdin hazards, not an inspected operating-system security sandbox; no evidence that arbitrary module side effects are rolled back or installations improve capability.

> const module = (await withHostGuard(() => loadLegacyPiModule(resolvedPath))) as LoadedExtensionModule;
> --- `packages/coding-agent/src/extensibility/extensions/loader.ts`

> await factory(api);
> --- `packages/coding-agent/src/extensibility/extensions/loader.ts`

Admission account: startup/reload discovery supplies proposed capability code; successful import/interface/binding admits it. Installer/operator authorship versus model authorship is unresolved for actual installed extensions; starting the runtime is not per-registration human approval. Invalid factories or import/bind errors can be rejected; suspension can remove live registrations. Guidance is the extension API and factory code, not an answer oracle; mode is configured extensibility, not a bounded improvement experiment. Module files persist according to external authoring/install operations. Loader recovery does not establish rollback of arbitrary I/O. No product self-improvement or learning claim follows from this capacity alone.

### Claims

#### RT-CLM-coding-agent
Label: Coding agent

Claimed operation: an integrated coding-agent surface, rather than a passive model SDK. Source: SRC-1, `README.md`, doctrine/design. The implemented session/tool routes support this architectural characterization; the README's superiority and scale statements are not runtime evidence or evaluated here.

> <strong>A coding agent with the IDE wired in.</strong>
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Prompt guidance

Consumer: selected inference model. Channel: system instructions plus transformed messages/tool definitions supplied by SDK/core; see [RT-OBJ-system-prompt](#rt-obj-system-prompt) and [RT-RTE-session-turn](#rt-rte-session-turn). Force: natural-language guidance, distinct from hard dispatch vetoes. Horizon: current request and later requests reusing/rebuilding the instructions; no observed compliance. Evidence: SRC-1, `packages/agent/src/agent-loop.ts`, `packages/coding-agent/src/sdk.ts`.

> systemPrompt: context.systemPrompt,
> messages: normalizedMessages,
> --- `packages/agent/src/agent-loop.ts`

#### RT-BAP-extension-code
Label: Extension code

Consumer: host module loader, factory binder, hook runner and tool dispatcher. Channel: configured/discovered executable module and registrations. Force: host-language execution at import/binding, and callback/tool authority after registration; not merely advice to a model. Horizon: module load and session lifetime, with later sessions able to reload installed files. Evidence: [RT-RTE-extension-load](#rt-rte-extension-load), SRC-1, `packages/coding-agent/src/extensibility/extensions/loader.ts`. Tool wrapper policy bounds registered tool dispatch, not every operation the module can perform during import.

## Annotations

none
