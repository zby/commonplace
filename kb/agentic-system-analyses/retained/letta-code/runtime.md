---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Letta Code runtime baseline: foreground provider/tool turns, durable listener approvals, delegation and executable/configuration admission at the frozen commit."
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
reviewed-boundary: "271f119dcf37d58649a18e6c733386b3c710a456"
---

# Letta Code runtime report

## Runtime account

### Work, entry paths and evidence strength

Letta Code's consequential work is to run an agent conversation, let a model propose actions, execute admitted actions on the host or through external tools, and preserve context for subsequent turns. The shipped CLI drives both interactive and headless use; the local backend owns provider invocation, while the API backend delegates inference and server-side state to Letta. This is not a claim that the external service's implementation has been inspected. SRC-1: `src/index.ts`, `src/headless.ts`, `src/backend/local/local-backend.ts`, `src/backend/backend.ts`.

The main entry dispatches subcommands before ordinary agent startup. Agent startup selects interactive or headless execution. Server dispatch includes local App Server and remote listener modes. App Server attaches connections to a listener runtime; a local channel gateway connects through the App Server client. Local schedules enqueue prompts into a conversation queue rather than defining another inference engine. These alternate principals matter: work can begin without a contemporaneous terminal prompt. SRC-1: `src/index.ts`, `src/cli/subcommands/server.ts`, `src/cli/subcommands/app-server.ts`, `src/websocket/app-server.ts`, `src/channels/gateway-local.ts`, `src/cron/scheduler.ts`.

> // Subcommands exit before TUI initialization and tool bootstrapping.
> const subcommandResult = await runSubcommand(subcommandArgs);
> --- `src/index.ts`

The paths and quotations added here are implementation evidence from SRC-1 at the frozen revision. Additional inspection covers shared approval execution, permission precedence, tool dispatch, shell sandboxing, child-agent arguments, mod loading, hook subprocesses, listener effect checkpoints, local transcript persistence, compaction, self-configuration and package updating. No target, test or example was executed. All operational activation, reliability, quality and benefit conclusions remain uninspected; executable wiring does not establish a successful deployment.

### Ordinary invocation: a local one-shot prompt

The ordinary trace is CLI headless invocation with a selected local agent and conversation. The caller supplies the problem; the headless loop owns progression. Agent ID identifies persistent agent configuration; conversation ID identifies history, with `default` requiring an explicit agent ID. Message `otid`, backend run ID, tool-call ID and per-turn tool-context ID serve different correlation purposes. The prepared tool context captures the selected registry and execution scope, rather than assuming the global registry remains unchanged. [RT-RTE-foreground-turn](#rt-rte-foreground-turn), [RT-OBJ-tool-context](#rt-obj-tool-context). SRC-1: `src/headless.ts`, `src/agent/message.ts`, `src/tools/manager.ts`.

The request transports messages, serialized client tools and client skills. In the local backend, a turn first excludes another live run in that backend instance, settles orphaned tool calls except on approval continuations, appends input, loads ordered conversation history and effective agent configuration, resolves the system prompt, and invokes its executor. The provider adapter converts messages and tool schemas, resolves a provider model, includes any mid-conversation memory update, then calls the provider stream. The model owns proposed text and tool arguments; symbolic host code owns stop-reason interpretation and the next provider round. Model internals are not an inspected executor. [RT-CMP-turn-model](#rt-cmp-turn-model), [RT-OBJ-local-transcript](#rt-obj-local-transcript). SRC-1: `src/backend/dev/fake-headless-backend.ts`, `src/backend/local/local-backend.ts`, `src/backend/dev/pi-stream-adapter.ts`.

A completed model tool call becomes an approval request. `requires_approval` returns control to the harness, not directly to a shell. The headless caller classifies requests, executes auto-allowed ones, returns explicit denials for requests needing runtime user input, and sends results as the continuation. Tool exceptions become error returns. Abort stops continuation after interrupted tool execution. On `end_turn`, a mod can request another user message; otherwise the loop stops. Maximum-turn checks intentionally exclude approval continuations so the harness does not leave an unresolved backend approval merely because a limit was reached. SRC-1: `src/backend/dev/provider-turn-executor.ts`, `src/headless.ts`, `src/agent/approval-execution.ts`.

The executor stream is persisted by the local backend; local transcript session entries use JSONL on disk. Their natural-language message parts later reach the model, whereas IDs, roles and compaction entries are symbolically interpreted by the store. Cached compiled prompts are reused only when the raw system hash and committed MemFS revision match. A changed committed memory revision can produce a separate mid-conversation system message while keeping the original compiled prompt. This account establishes the runtime consumption boundary, not the correctness or admission policy of memory edits. SRC-1: `src/backend/dev/fake-headless-backend.ts`, `src/backend/local/local-store.ts`, `src/backend/local/local-backend.ts`.

Terminal output is assistant text or headless JSON/stream-JSON output, with stop/error information. Stream-JSON explicitly emits local tool-call/return pairs because those client-side calls are not themselves in a hosted server stream. Recovery includes bounded handling of pending approvals, busy conversations, provider errors and provider-plan rotation. Such retries are not a transaction rollback of filesystem or external effects. SRC-1: `src/headless.ts`.

### Material alternates and four forcing cases

**1. Approval without a local human.** TUI classification includes requests requiring user input and precomputes file diffs. One-shot headless denies that class instead of waiting. Bidirectional headless code accepts SDK permission responses and edited arguments. Therefore "every admitted action receives a human decision" would be false: automatic grants, hooks and unrestricted modes also decide. [RT-CLM-approval-policy](#rt-clm-approval-policy). SRC-1: `src/cli/app/use-conversation-loop.ts`, `src/headless.ts`, `src/permissions/checker.ts`.

**2. Shell effects versus named-tool checks.** The permission checker prioritizes workspace/cross-agent guards and deny rules before mode overrides and allow rules. Its declared cross-agent guard does not make arbitrary spawned shell programs safe. The shell wrapper explicitly describes static shell-command analysis as bypassable, uses an optional kernel sandbox, and is off by default. Workspace sandbox requests instead fail closed when a kernel backend is unavailable. Bash and Codex shell sessions share the shell wrapper, but hooks spawn independently and mods import into the host process. Capability surface, grant set and isolation envelope must remain distinct. [RT-RTE-extension-load](#rt-rte-extension-load), [RT-CLM-shell-isolation](#rt-clm-shell-isolation). SRC-1: `src/permissions/checker.ts`, `src/tools/impl/shell-sandbox.ts`, `src/hooks/executor.ts`, `src/mods/mod-engine.ts`.

**3. Crash after a listener tool effect.** The listener's approval branch checkpoints each tool's transition from provably unstarted to outcome unknown before invoking tool code, then checkpoints exact results after settlement. Unknown is retained as an error explaining that execution may have completed. This is conservative recovery evidence, not exactly-once external execution or rollback. Foreground one-shot execution does not pass these listener checkpoint callbacks. The durable variant therefore has a stronger recovery protocol than the ordinary trace, but it cannot establish a global guarantee covering every tool caller. [RT-RTE-listener-approval](#rt-rte-listener-approval), [RT-CLM-effect-checkpoint](#rt-clm-effect-checkpoint). SRC-1: `src/websocket/listener/turn-approval.ts`, `src/websocket/listener/recovered-approval-checkpoint.ts`, `src/agent/approval-execution.ts`, `src/headless.ts`.

**4. Delegated permissions differ from the parent UI.** Child-agent arguments explicitly select unrestricted permission mode, inherit CLI disallow rules, combine allow rules and apply configured tool filters. They do not simply replicate the parent's pending approval dialog. Background tasks capture parent scope before asynchronous execution, write task output and later notify the parent. Remote deployments submit work with `--no-wait`; service status, rather than the child process, owns remote completion. Memory workers require the current machine and parent conversation scope. [RT-RTE-subagent-task](#rt-rte-subagent-task). SRC-1: `src/agent/subagents/manager.ts`, `src/tools/impl/task.ts`.

Hosted inference uses the same conversation-message client contract but sends it to the Letta SDK. Code verifies SSE content type on message creation; it does not implement or verify the hosted server's internal inference, native tools or durable state. Native tools executed remotely cannot be credited with the local approval/sandbox enforcement points. [RT-RTE-foreground-turn](#rt-rte-foreground-turn). SRC-1: `src/backend/backend.ts`.

### Admission and later authority

There are distinct change mechanisms, not one "self-improvement" switch. Mod loading imports executable modules and registers capabilities; configuration scripts patch model/system settings; the package updater installs a new release; memory maintenance writes and integrates retained text through separate memory mechanisms. The model, caller, host code and external service have different admission responsibilities. [RT-RTE-extension-load](#rt-rte-extension-load), [RT-RTE-settings-patch](#rt-rte-settings-patch), [RT-RTE-package-update](#rt-rte-package-update).

Reflection uses a background subagent and memory worktree; integration finalization and post-merge sync can occur outside the visible parent turn. The integration path tracks whether the transcript was consumed successfully and records retry state. That demonstrates maintenance wiring, not that model-generated memory is accurate or improves future work. Detailed memory edits, constraints, shared-memory sync and reflection selection belong to the memory account. SRC-1: `src/cli/helpers/reflection-launcher.ts`; supporting background execution is [RT-RTE-subagent-task](#rt-rte-subagent-task).

Compaction uses another direct model call, not a client-tool approval. It supplies a summarization prompt and transcript; a Fable-specific branch switches the auxiliary model. Its output can become a retained transcript compaction entry. This disproves an inference that all consequential model work uses only the foreground model or passes through the tool permission dialog. Memory semantics, fallback text selection and summary fidelity need separate memory analysis. [RT-CMP-summary-model](#rt-cmp-summary-model). SRC-1: `src/backend/local/compaction.ts`, `src/backend/local/local-store.ts`.

The selected forcing cases cover approval interaction, local shell/extension escape from overly broad enforcement claims, durable effect recovery, and delegated grants. Full listener ingress/recovery ownership, OpenAI-compatible bridge details, arbitrary channel plugins, provider-native execution, mod-learning experiments, release automation and every evaluator were not traced end to end here. Repository evidence for those shipped parts remains available, not absent. External service/provider internals and installed dynamic content remain outside the frozen source. No source-only baseline closes an exercised-learning or improvement causal chain.

## Shared records

### Components

#### RT-CMP-turn-model
Label: Provider-resolved turn model

Source-native identity: `resolved.model` in `PiStreamAdapter.streamOnce`. Representational form: distributed-parametric inference component. Storage substrate: external provider service or local model endpoint; actual weights and their substrate are outside SRC-1. The adapter supplies natural-language context and symbolic tool schemas. SRC-1: `src/backend/dev/pi-stream-adapter.ts`, `src/backend/local/local-model-config.ts`.

Parameter changes during operation: uninspected at the external inference component; the inspected caller issues inference requests rather than parameter-update requests. Exact parameter version pinned: not established by repository commit or model handle. Mutable endpoint resolving to another model: afforded by configured endpoints, discovery and registered providers; actual endpoint changes are uninspected. Per-turn resolution and provider-plan rotation also prevent treating agent configuration as an immutable inference identity. SRC-1: `src/backend/local/local-model-config.ts`, `src/backend/dev/pi-stream-adapter.ts`, `src/headless.ts`.

> const resolved = await resolvePiModelForAgent(
>       localModel.model,
>       localModel.modelSettings,
>       {
>         localProviderAuthStorageDir: this.localProviderAuthStorageDir,
>         modelsRuntime: this.modelsRuntime,
>         ...(this.abortSignal ? { abortSignal: this.abortSignal } : {}),
>       },
>     );
> --- `src/backend/dev/pi-stream-adapter.ts:584-592`

#### RT-CMP-summary-model
Label: Local compaction summary model

Source-native identity: resolved model used by `runGenerateText`. Representational form: distributed-parametric component consuming a natural-language summarization instruction and serialized transcript. Storage substrate: provider/local endpoint, not retained weights in the inspected repository. Distinct from the turn-model use because a Fable-specific branch selects an auxiliary fallback model and its output is admitted into compaction state. SRC-1: `src/backend/local/compaction.ts`, `src/backend/local/local-store.ts`.

Parameter changes during operation: uninspected provider internals; inspected code performs completion, not training. Exact weight version pinned: unestablished. Mutable endpoint resolving to another model: afforded by the same resolver/provider configuration; the compaction branch can additionally change the requested model. Successful completion and summary preservation are unobserved.

> localModel = await resolveAvailableLocalModelForTurn({
>       model: FABLE_COMPACTION_SUMMARY_FALLBACK_MODEL,
>       modelSettings: fableCompactionSummaryFallbackSettings(
>         localModel.modelSettings,
>       ),
>       storageDir: input.localProviderAuthStorageDir,
>       modelsRuntime,
>     });
> --- `src/backend/local/compaction.ts`

### Operative objects

#### RT-OBJ-tool-context
Label: Per-turn tool execution context

Source-native identity: execution context selected by `toolContextId`. Representational form: symbolic registry/scope references and metadata; descriptions and tool results have separate model-interpreted text consumption. Storage substrate: in-process maps and captured registry snapshots. Carries agent/conversation, working directory, permission mode, external executors and mod context into execution. Missing named contexts return an error instead of falling back silently. SRC-1: `src/tools/manager.ts`.

> if (options?.toolContextId && !context) {
>     return {
>       toolReturn: `Tool execution context not found: ${options.toolContextId}`,
>       status: "error",
>     };
>   }
> --- `src/tools/manager.ts`

#### RT-OBJ-local-transcript
Label: Local conversation transcript

Source-native identity: local conversation session entries and their message projections. Representational form: symbolic JSONL envelope, message identities, parent links and compaction metadata; message prose and summary prose receive consequences through later model interpretation. Storage substrate: local disk with resident message/index caches. This is a container: it does not collapse summary text and raw messages into a single semantic memory claim. SRC-1: `src/backend/local/local-store.ts`, `src/backend/dev/fake-headless-backend.ts`.

> appendFileSync(messagesPath, `${JSON.stringify(entry)}\n`);
> --- `src/backend/local/local-store.ts`

### Routes

#### RT-RTE-foreground-turn
Label: Foreground conversation and client-tool continuation

Endpoints and progression: CLI caller → headless/TUI loop → prepared conversation request → local executor or hosted API → assistant/approval stream → client-tool admission/execution → result continuation → terminal output. Owner: caller loop owns continuation; model proposes next text/actions; backend owns provider request and history persistence. Context: effective agent settings, compiled prompt, history, skills and tool schemas; action effects: host tools or external executors, not just response text. SRC-1: `src/headless.ts`, `src/cli/app/use-conversation-loop.ts`, `src/agent/message.ts`, `src/backend/dev/fake-headless-backend.ts`, `src/backend/backend.ts`.

- Immediate return: assistant stream and stop reason; approved calls return tool results, denials return rejection input for the next model round; terminal output is text or structured headless output.
- Later read-back: local history is persisted and loaded on subsequent turns; committed MemFS changes can enter a compiled prompt or mid-conversation memory update. Hosted history persistence is an external service contract, not inspected server behavior.
- Delegated visibility: tool executors receive scoped arguments and runtime context; models receive tool-result content and selected context, not arbitrary host state. Task delegation is separately declared below.
- Selection predicate: chosen backend, agent/conversation and tool context; stop reason selects continuation; classification divides auto-allowed, denied and user-input requests.
- Invalidation or expiry: abort and terminal stop end the current loop; prompt cache checks system hash and committed memory revision; interrupted tool calls receive synthetic error results on a later non-approval local turn.
- Activation or effect: wired provider requests and permitted host/external calls; actual model compliance, tool success and behavioral effects of retained context are unobserved.
- Evidence limits: only source implementation; hosted native tools, provider internals and production outcomes are not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: user supplies problem; model proposes actions; permission software, configured hooks/mods or human/SDK responses decide client-tool admission. One-shot headless cannot solicit an interactive decision and denies that class. Human authorship of a configured rule is not per-content approval. Operating mode: open-ended requests with turn limits, not a controlled improvement curriculum. Answer oracle: inapplicable — no expected answer/reference outcome is required by this general conversation loop. SRC-1: `src/headless.ts`, `src/permissions/checker.ts`.

> // One-shot headless mode has no control channel for interactive
>             // approvals, so deny tools that need runtime user responses.
>             return {
>               type: "deny" as const,
>               approval: ac.approval,
>               reason: "Tool requires approval (headless mode)",
>             };
> --- `src/headless.ts`

The hosted alternate validates transport before accepting a stream, not the server's answers:

> stream.controller.abort();
>       throw new APIConnectionError({
>         message: `Connection error: expected text/event-stream, received ${contentType || "no content type"} (HTTP ${response.status}).`,
>       });
> --- `src/backend/backend.ts`

#### RT-RTE-listener-approval
Label: Listener approval with durable effect checkpoints

Endpoints and progression: conversation runtime approval stop → scoped permission classification/remote response → checkpointed decisions → client tool execution → exact or unknown-result persistence → continuation transport. Owner: listener turn lease and recovery authority guard coordinate execution and publication; model proposes the calls, permission policy/responding client decides admission. State includes run/message IDs, batch ID, tool IDs, interrupted revision and recovery lineage. SRC-1: `src/websocket/listener/turn-approval.ts`, `src/websocket/listener/recovered-approval-checkpoint.ts`.

- Immediate return: continue stream, interruption, teleport, terminal or error branch; approved tools produce results and subscriber execution events.
- Later read-back: interrupted-turn checkpoints expose saved results, unknown outcomes and provably unstarted tool IDs to later recovery; persisted conversation history remains a separate backend path.
- Delegated visibility: scoped tool context, parent agent/conversation and working directory reach executors; subscribed clients can receive output/file updates while lease and authority predicates hold.
- Selection predicate: requires-approval branch, permission classification, current turn lease, authority guard and ownership checks before effects.
- Invalidation or expiry: interruption/claim loss prevents new execution; revision-CAS checkpoint chain fences state changes; exact result may replace unknown even after publication authority is revoked.
- Activation or effect: callback before tool code durably marks the effect outcome unknown; callback after settlement saves the result; neither undoes an already executed effect.
- Evidence limits: crash/reconnect tests were not run; durability storage and all recovery successors were not exhaustively audited; external tool transactions are not controlled here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: ordinary remotely controlled turns with recovery, not candidate improvement experiments. Proposer: model; computational admission: permission classification and hook/mod policy; veto: denied policy or remote approval response and interruption/ownership checks. Answer oracle: inapplicable — approval response is consent, not a correctness reference. SRC-1: `src/websocket/listener/turn-approval.ts`.

> beforeToolExecution: effectBoundary.beforeToolExecution,
>       afterToolExecution: effectBoundary.afterToolExecution,
> --- `src/websocket/listener/turn-approval.ts`

#### RT-RTE-subagent-task
Label: Background subagent task and completion

Endpoints and progression: Task/reflection caller → registered task/output file → spawned subagent or remote submission → task completion state/transcript → scoped parent notification/callback. Owner: background task lifecycle, not a promise held by the foreground provider. New children get role/system/model arguments; deployments preserve an existing agent's prompt/model and can create separate conversations. SRC-1: `src/tools/impl/task.ts`, `src/agent/subagents/manager.ts`.

- Immediate return: task ID, output file and subagent ID; lifecycle runs asynchronously and captures completion/failure separately.
- Later read-back: task output/transcript supports later task inspection and scoped notification; durable memory maintenance uses separate worktrees/integration, not the task label itself.
- Delegated visibility: explicit assignment, optional forked context/parent transcript, parent scope and memory scope; not an unconditional full copy of parent state.
- Selection predicate: selected subagent configuration/existing target, current-machine requirement for memory workers and available task capacity; remote environment changes submission/completion ownership.
- Invalidation or expiry: abort controller, task cleanup and completion/failure state; cleanup timing and all remote status transitions are uninspected here.
- Activation or effect: child runs a headless request or submits remote work; task output and notifications can reach a later parent turn; actual child action or notification-driven behavior is unobserved.
- Evidence limits: external coding-agent descriptors and remote environments are available alternatives but not exercised; scope and grant wiring is not an end-to-end isolation proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Permission policy: child uses unrestricted mode, inherited CLI disallows and configured tool filter/allow entries. Parent model/caller proposes the assignment; host accepts within task capacity and type constraints. Human approval of each child action is not required by these argument defaults. Operating mode: open delegated requests; answer oracle: inapplicable — success/error reporting is not an expected-answer reference. Memory-worker admission and reflection integration remain separate from generic task completion. SRC-1: `src/agent/subagents/manager.ts`, `src/tools/impl/task.ts`.

> args.push("--output-format", "stream-json");
>   args.push("--permission-mode", "unrestricted");
> --- `src/agent/subagents/manager.ts`

#### RT-RTE-scheduled-prompt
Label: Local scheduled prompt enqueue

Endpoints and progression: due/manual schedule → target conversation runtime → wrapped cron prompt → bounded queue → listener queue pump. Owner: in-process scheduler and listener; original prompt principal is schedule creator, not necessarily an active terminal user. Stored task identity, agent ID and target conversation route the request. SRC-1: `src/cron/scheduler.ts`, `src/cron/runner.ts`.

- Immediate return: enqueue success/failure and run-log outcome; success here means queued, not task completion.
- Later read-back: schedule timing/status and last outcome influence later occurrences; model consumes scheduled prompt through the subsequent turn, not the run log alone.
- Delegated visibility: target runtime receives wrapped prompt and cron task/agent/conversation metadata.
- Selection predicate: timing/due calculation or manual trigger, active-state recheck for automatic work, target runtime availability and queue capacity.
- Invalidation or expiry: pause before enqueue stops automatic admission; missed one-shots have separate handling; local scheduler lifetime depends on the listener. Cloud schedules are a distinct external service route.
- Activation or effect: queue admission and pump scheduling are wired; eventual inference, external effects and timely delivery are unobserved.
- Evidence limits: no clock/scheduler execution or cloud-worker trace; queued log is not completion evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> scheduleQueuePump(conversationRuntime, socket, opts, processQueuedTurn);
> --- `src/cron/scheduler.ts`

#### RT-RTE-extension-load
Label: Executable mod admission and registry activation

Endpoints and progression: resolved mod sources → file read/transpilation/import → exported factory → activation API → tools/providers/permissions/events registry; failures remove registered owner capabilities and abort activation. Owner: local mod engine. SRC-1: `src/mods/mod-engine.ts`.

- Immediate return: registry with loaded paths, capabilities and diagnostics; failing module does not become a successfully loaded registry owner.
- Later read-back: installed source files can be loaded again; event/provider/tool registrations affect subsequent turns in the current process. Captured installed content is unavailable in this analysis.
- Delegated visibility: imported JavaScript/TypeScript runs in the host process and receives API/context capabilities; these are not a kernel isolation boundary.
- Selection predicate: resolved sources/files and load options; reserved names, priority and registration validation constrain registry entries, not arbitrary module side effects.
- Invalidation or expiry: disposers, owner abort controllers, capability removal and registry generations support unloading/reloading; import/activation side effects outside registries need not be reversible.
- Activation or effect: dynamic import and factory invocation activate executable code; actual user module behavior is uninspected.
- Evidence limits: no installed module capture or execution; activation failure cleanup is narrower than rollback of arbitrary code.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Change admission: trigger is loading/reloading configured files; proposed change is executable code with tool/provider/permission/event contributions. Caller/source author supplies it; engine validates factory/registrations and can reject failures. Human authorship and explicit per-module approval are unresolved for dynamic installations. The guidance that shapes activation is the API contract, not a model-output correctness oracle. What persists is source files; registry entries persist until removal/process exit. Operating mode: extension loading, not evidence-driven candidate comparison. Answer oracle: inapplicable — successful import/registration is not expected-answer evaluation. No formulated-theory assessment is claimed. SRC-1: `src/mods/mod-engine.ts`.

> const module = (await import(
>           `${pathToFileURL(importPath).href}?mod=${mtimeMs}`
>         )) as LocalModModule;
> --- `src/mods/mod-engine.ts`

#### RT-RTE-settings-patch
Label: Self-configuration script settings patch

Endpoints and progression: caller flags/files → target/current-ID validation → optional current-state fetch/merge → preview or server PATCH → safe returned fields. Owner: shipped script and external server endpoint. Model/system/compaction settings are distinct downstream parts, not guaranteed improvement. SRC-1: `src/skills/builtin/self-configuration/scripts/update-agent-settings.ts`.

- Immediate return: dry-run patch preview or safe effective server fields; failures report an error/nonzero exit.
- Later read-back: admitted server settings can govern later requests through agent/conversation retrieval; server persistence semantics are external. The local backend also retrieves effective agent settings, but this script's direct HTTP path is not evidence of a local-store write.
- Delegated visibility: replacement system text and JSON settings reach the selected endpoint; output redacts secret-named fields.
- Selection predicate: agent/conversation target, explicit/environment ID, same-target guard unless overridden, supplied setting flags and live-versus-dry-run mode.
- Invalidation or expiry: patches remain until later replacement; no automatic rollback is established in this script. Restore requires another authorized patch/current-state management.
- Activation or effect: live server PATCH is wired; acceptance, later settings use and resulting behavior are unobserved.
- Evidence limits: confirmation flag is machine-readable intent, not authenticated human review; direct shell/API alternatives are outside this script's particular gate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller or agent proposes files/flags; script vetoes malformed inputs, target misuse and unconfirmed live system replacement; external server can reject the request. Dry-run admits nothing. Starting the script or setting its confirmation flag does not establish human control of each proposed text. Guidance is explicit field/target/confirmation contract; persisted result is server configuration including any replacement instruction text. Operating mode: open configuration update; answer oracle: inapplicable — no independent correctness or improvement outcome reference. SRC-1: `src/skills/builtin/self-configuration/scripts/update-agent-settings.ts`.

> throw new Error(
>       "Live --system-file writes require --confirm-system-replacement; use --dry-run to preview without confirmation",
>     );
> --- `src/skills/builtin/self-configuration/scripts/update-agent-settings.ts`

#### RT-RTE-package-update
Label: Release-based package update

Endpoints and progression: automatic/manual update request → registry latest-version check → supported installation/package-manager selection → install process → status/manual recovery message. Owner: updater plus external registry/package manager. SRC-1: `src/updater/auto-update.ts`, `src/startup-auto-update.ts`.

- Immediate return: update result, failure or no-op; successful automatic significant update can produce a startup notice.
- Later read-back: installed executable/package files govern future launches; this is production-code replacement, not retained conversation learning.
- Delegated visibility: package manager receives install arguments and environment; registry supplies release metadata/packages, not a captured trusted behavioral specification.
- Selection predicate: automatic enablement, non-development/non-Python distribution, registry update availability and supported/writable installation; manual path has its own checks.
- Invalidation or expiry: installed release supersedes prior files; retries/cleanup for installation failures are wired. Complete transactional rollback was not established by the inspected branches.
- Activation or effect: package-manager subprocess installation is wired; installed bytes, later startup and correctness are unobserved.
- Evidence limits: registry contents, dependency implementation and actual release integrity are outside SRC-1; no measured update outcome.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Change admission: registry/release publisher proposes successor; comparison/installation code decides whether to attempt it; operator can disable automatic updating. Rejection occurs for unsupported/development paths or check/install failure. Guidance is version availability and installation policy, not model-generated criticism of runtime performance. What persists is installed package code. Operating mode: release maintenance; answer oracle: inapplicable — version availability is not an independent answer/quality reference. SRC-1: `src/updater/auto-update.ts`.

> if (!isAutoUpdateEnabled()) {
>     debugLog("Auto-update disabled via DISABLE_AUTOUPDATER=1");
>     return;
>   }
> --- `src/updater/auto-update.ts`

### Claims

#### RT-CLM-approval-policy
Label: Permission classification precedes ordinary client-tool execution

Claimed operation: ordinary headless/TUI/listener paths classify model-proposed client-tool requests before passing approved decisions to execution. Owner: caller classification and permission checker. Enforcement point: approval classification plus deny/allow/mode/hook logic; `executeApprovalBatch` trusts supplied decisions, so it is not an independently universal permission gate. `executeToolInner` includes mod execution checks and internal PreToolUse hooks but does not reproduce all ordinary approval classification. SRC-1: `src/headless.ts`, `src/cli/app/use-conversation-loop.ts`, `src/websocket/listener/turn-approval.ts`, `src/agent/approval-execution.ts`, `src/tools/manager.ts`, `src/permissions/checker.ts`.

Guarantee strength: policy. Covered paths: these ordinary classified client-tool requests. Alternates: direct executors, precomputed results, SDK/external tools, server-native tools, mod imports and hook subprocesses need their own contracts. Required external contract: responding SDK/remote client supplies valid consent and tool execution implementations honor their contracts; external service enforcement is unknown.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Cross the caller's durable effect fence immediately before tool code can run.
>     await options?.beforeToolExecution?.(decision.approval.toolCallId);
> --- `src/agent/approval-execution.ts`

This also establishes that the durable fence is caller-supplied and optional, not a property of every tool invocation.

#### RT-CLM-shell-isolation
Label: Optional cross-agent kernel shell sandbox

Claimed operation: shell wrapping can enforce filesystem separation across the whole shell/subprocess tree. Owner: shell sandbox gate and host kernel backend. Enforcement point: launcher wrapping at shell spawn. Guarantee strength: deployment guarantee, conditional on enabled/resolvable sandbox context, supported backend and actual wrapped launch. It is not the default deployed envelope. Workspace requests explicitly throw without a kernel backend; optional cross-agent wrapping can leave a launcher unchanged. SRC-1: `src/tools/impl/shell-sandbox.ts`, `src/tools/impl/bash.ts`.

Covered paths: Bash and Codex exec sessions using the shared shell wrapper. Alternate paths: hooks use a direct `spawn`, mods use in-process import, external tools use their executor, hosted tools execute remotely; no equivalence to the shell wrapper is established. Required external contract: host kernel/backend implements the generated policy, and deployment selects the correct roots. Current grant set is runtime permission configuration; neither a tool list nor permission mode proves kernel isolation.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> OFF by default; set `LETTA_FS_SANDBOX=1` to opt in (recommended for
>  * multi-tenant deployments where agents must not read each other's memory).
>  * No-ops when the host has no sandbox backend.
> --- `src/tools/impl/shell-sandbox.ts`

#### RT-CLM-effect-checkpoint
Label: Conservative listener tool-effect recovery

Claimed operation: each approved listener tool receives a durable pre-effect unknown state and a later exact result; unstarted siblings remain distinguishable. Owner: listener checkpoint chain and per-tool boundary tracker. Enforcement point: callback awaited before `executeTool` and after executor settlement. Guarantee strength: protocol. Covered paths: listener approval calls wiring both boundary callbacks. Alternate paths: one-shot headless, TUI, direct tool calls and remote native effects do not acquire this guarantee from a shared executor name. Required external contract: checkpoint storage/ownership fencing succeeds; exact tool-result reporting reflects actual execution. No transactional external rollback or exactly-once effect guarantee is asserted. SRC-1: `src/websocket/listener/recovered-approval-checkpoint.ts`, `src/websocket/listener/turn-approval.ts`, `src/agent/approval-execution.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> unstarted.delete(toolCallId);
>         results.set(toolCallId, unknownResult(toolCallId));
>         try {
>           await params.checkpoint(snapshot(), [...unstarted], "before");
> --- `src/websocket/listener/recovered-approval-checkpoint.ts`

> export const RECOVERED_APPROVAL_OUTCOME_UNKNOWN =
>   "Tool execution may have completed, but the listener stopped before recording its result";
> --- `src/websocket/listener/recovered-approval-checkpoint.ts`

#### RT-CLM-app-server-auth
Label: App Server non-loopback authentication startup guard

Claimed operation: local App Server refuses an unauthenticated non-loopback listener. Owner: App Server startup/auth policy. Enforcement point: host/policy test before listener startup. Guarantee strength: policy. Covered path: `startAppServer`; this is not evidence of remote listener/cloud authentication, all HTTP bridge routes or authorization within an authenticated connection. Required external contract: correct auth settings and implementation of token verification; token issuance, live network deployment and complete principal isolation are uninspected here. SRC-1: `src/websocket/app-server.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (isUnauthenticatedNonLoopbackListener(listen.host, authPolicy)) {
>     throw new Error(
>       `refusing to start non-loopback websocket listener ${listen.host}:${listen.port} without auth; configure \`--ws-auth capability-token\` or \`--ws-auth signed-bearer-token\``,
>     );
>   }
> --- `src/websocket/app-server.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-provider-context
Label: Effective prompt and history to provider decisions

Consumer: turn model. Channel: `Context.systemPrompt`, converted message history, optional mid-conversation system message and tool schemas. Force: model-interpreted instruction/context, not host-enforced obedience; tool definitions also delimit callable schema surface. Horizon: current turn and subsequent turns when retained history/configuration is reloaded. Source-dependent limits: which memory prose survives compilation belongs to memory analysis; actual compliance and effects are unobserved. SRC-1: `src/backend/dev/pi-stream-adapter.ts`, `src/backend/local/local-backend.ts`.

> const context: Context = {
>       systemPrompt: input.systemPrompt ?? input.agent.system,
>       messages,
>       ...(tools ? { tools } : {}),
>     };
> --- `src/backend/dev/pi-stream-adapter.ts`

#### RT-BAP-mod-capabilities
Label: Mod code to runtime registrations and events

Consumer: host mod engine, tool/provider/permission registries and later event dispatch. Channel: executable dynamic import and activation API. Force: executable behavior and symbolic registrations, not merely suggestions to a model. Horizon: registry lifetime and later loads of installed files. Failure removes registered owner capabilities, not necessarily arbitrary host side effects. SRC-1: `src/mods/mod-engine.ts`; admission is [RT-RTE-extension-load](#rt-rte-extension-load).

> const dispose = await changes.run(() => activate(api));
> --- `src/mods/mod-engine.ts`

## Annotations

none
