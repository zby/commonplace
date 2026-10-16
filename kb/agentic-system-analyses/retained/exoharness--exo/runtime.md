---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Exo runtime baseline tracing managed turns, harness alternatives, capability admission and host self-update at the frozen source revision."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo runtime report

## Runtime account

### Consequential work and evidence basis

Exo supplies a durable execution substrate around interchangeable agent harnesses. The substrate admits agent definitions and turn requests, binds conversation state and credentials, selects an executor, streams results, and preserves work for recovery. A harness decides how to turn that state into model requests and actions. The persistent-agent experiment adds background tasks, messaging adapters and a model-requestable host rebuild. These are different loops, not one universally enforced model/tool policy. See [RT-RTE-managed-turn](#rt-rte-managed-turn), [RT-RTE-responses-loop](#rt-rte-responses-loop), [RT-RTE-background-wakeup](#rt-rte-background-wakeup) and [RT-RTE-guardian-update](#rt-rte-guardian-update).

All findings below use SRC-1 at the boundary revision, by static inspection. New inspection extends the boundary's initial coverage to turn admission/draining, Basic approval/recovery, TypeScript tool loading and installation, RLM subqueries, Codex approval/reattachment, local-process execution and deferred guardian completion. Relevant paths appear beside the findings. Implementation excerpts support wiring, not successful operation. Target-authored prompts and architecture prose supply design/request evidence only. No target, test, example, service or provider was run; activation, recovery reliability, task benefit and performance remain unobserved.

### Ordinary invocation, ownership and return

An ordinary local invocation is `exo run <agent.md> --thread <name> <prompt>` using the Basic harness selected by the definition. The CLI loads the definition, creates or updates the saved agent, opens or resumes the named thread, checks local model credentials, and dispatches to one-shot prompt, interactive TUI or REPL. The caller chooses model overrides, attached vaults, environments, mounts and sandbox overrides subject to CLI/config validation. Agent-file synchronization itself is an admission path, not just a read. SRC-1: `crates/cli/src/main.rs`, `crates/cli/src/managed_agents.rs`; [RT-RTE-definition-admission](#rt-rte-definition-admission).

The prompt client calls `Runtime.start_turn` with a user message and optional existing session ID. Admission checks a scoped caller when present, snapshots agent/thread configuration into queued work, assigns a turn ID and a session ID if needed, and enqueues under the agent/thread scope. The observer is registered before the entry becomes visible. Duplicate acceptance reattaches the observer to the accepted turn rather than assuming a new execution. The coordinator, not the terminal connection, owns progression. SRC-1: `crates/cli/src/tui.rs`, `crates/executor/src/turn_queue.rs`.

Managed execution prepares MCP connections and chooses Basic, RLM, TypeScript or the older Exo profile executor. Basic constructs model context from instructions plus selected conversation events, adding cached history incrementally by cursor. Its model chooses text/tool requests; Rust records the model round, authorizes each action, then dispatches to a runtime/MCP tool or client tool. Tool results enter the journal before another model round. A response without tools commits the final events and runtime completion marker together. The queue reads terminal journal state, broadcasts completion or failure, and acknowledges the head. Text, tool events and terminal status reach the client; effects may already exist in a sandbox, external service or client callback. SRC-1: `crates/executor/src/native/managed_executor.rs`, `crates/executor/src/basic.rs`, `crates/executor/src/turn_queue.rs`.

The maximum round setting constrains model-loop continuation; it is not proof of task completion. Basic returns when its budget is exceeded, whereas RLM raises an error. Tool side effects and external service calls do not become transactional merely because their requests/results are journaled. Basic explicitly refuses an unsafe unresolved tool replay unless its inspected recovery conditions hold. That counterexample prevents an exactly-once-effect or universal-resumption interpretation of durability. See [RT-CLM-recovery-scope](#rt-clm-recovery-scope).

### Material alternatives and forcing cases

Four forcing cases were inspected rather than extrapolating the ordinary loop:

1. **Committed model round, interrupted tool.** Basic reconstructs pending calls from saved round/request/result events instead of asking the model again. An unresolved call without a suitable pending approval or frontend-tool case can fail recovery. Durable admission and safe effect replay are separate properties. SRC-1: `crates/executor/src/basic.rs`.
2. **Native-agent tools and model traffic.** Codex runs inside an Exo sandbox and owns its native model loop. The bridge maps command approvals, MCP elicitation and dynamic client tools, and projects native state into Exo events. It rejects some live-turn reattachments when approval state was lost. Pi is another shipped bridge: it materializes conversation history, invokes `pi --mode rpc --no-session --no-extensions` with an explicit extension, and mediates extension requests. These are not executions of the Responses registry loop. Native SDK/provider internals remain outside the source. SRC-1: `exoharness/typescript/codex/harness.ts`, `exoharness/examples/typescript/pi-harness.ts`; [RT-RTE-native-bridge](#rt-rte-native-bridge).
3. **Dynamically admitted executable code.** A tool module can be imported and initialized in the host Node process, including during validation, before a later model selects its handler. The native TypeScript runner is launched by host `Command::new("node")`, not inside the shell sandbox. Authorization at registered tool invocation is not a sandbox for import-time code, arbitrary harness code, direct provider calls or Node subprocesses. The installation mechanism checks structure and conflicts, not semantic safety. SRC-1: `crates/executor/src/native/typescript.rs`, `exoharness/typescript/harness/tool-modules.ts`, `exoharness/typescript/harness/tool-registry.ts`; [RT-RTE-tool-admission](#rt-rte-tool-admission).
4. **Background or remote ownership.** Scheduler outputs wake a conversation without a terminal user, while Cloudflare routes turn/watch requests to thread Durable Objects that drain queues on recovery and alarms. The host must arrange durable wakeups; an accepted queue entry alone does not guarantee eventual execution. SRC-1: `crates/executor/src/native/scheduler_runtime.rs`, `crates/executor/src/native/conversation_wakeup.rs`, `exoharness/cloudflare/src/provider.ts`; [RT-RTE-background-wakeup](#rt-rte-background-wakeup).

The RLM route supplies an additional direct-model and context-isolation check: selected text or a JS variable becomes a separate subquery request with no tools, rather than inheriting the foreground history. Only the returned answer/preview and optional stored JS value return. The complete historical transcript remains accessible in the foreground REPL state, not automatically in the root model's window. This is a separate-context frame with value return, not shared model context. No outcome establishes that the encouraged decomposition improves answers. SRC-1: `crates/executor/src/native/rlm.rs`; [RT-RTE-rlm-subquery](#rt-rte-rlm-subquery).

Cloudflare's public Worker checks Access audience or a configured bearer token before trusted Durable Object dispatch. Native serving requires an auth file for a non-loopback listener, unless running the adapters-only mode. Neither front door governs arbitrary local library callers, host scripts or trusted bindings. SRC-1: `exoharness/cloudflare/src/index.ts`, `crates/cli/src/serve.rs`. Full Cursor/Claude bridge behavior, all HTTP/client retry paths, all sandbox backends, MCP server internals and provider-native hosted tools were not exhaustively inspected. No parity conclusion is made for these included alternatives.

### Guarantees and actual control envelope

The distinction between **capability surface**, **grant set** and **deployed isolation** is essential. Surfaces include shell, MCP, frontend callbacks, installed Node tools, custom harness modules, native-agent tools and guardian subprocesses. The grant set depends on saved definition, per-thread permissions, selected vaults, tool registry and caller role. Actual grants for a deployed agent were not supplied. Isolation depends on backend, mounts and host configuration; no deployed envelope was observed. SRC-1: `crates/executor/src/managed_agents.rs`, `crates/executor/src/native/managed_executor.rs`, `exo/profiles/practical.ts`.

| Scoped guarantee | Owner and enforcement point | Strength and covered/alternate paths | External contract and statuses |
|---|---|---|---|
| A Basic tool action reaches the permission decision before execution | Basic executor calls `permissions::authorize` before runtime/frontend dispatch | protocol; covers that loop's requests. `AlwaysAllow` and session-level tool grants intentionally avoid per-call approval. TypeScript registry, native approvals, custom code and host scripts need their own enforcement. | Caller identity and truthful policy/approval transport required. implementation conclusion status: wired. operation conclusion status: uninspected. |
| Queued turn identity/work can survive worker wake failure | Runtime admission plus stored coordinator; local store writes `turn_queue.json` | protocol; preserves accepted work, not eventual scheduling or exactly-once external effects. Remote/custom stores must honor coordinator contracts. | Storage durability, ownership and future host wakeup required. implementation conclusion status: wired. operation conclusion status: uninspected. |
| Unsafe Basic unresolved calls need not be blindly repeated | Basic `load_turn_progress`; pending-call/approval match before resumption | protocol; bounded fail-closed recovery, not universal resumption. Codex has different native snapshot guards. | Complete journal and correct frontend/tool contracts required. implementation conclusion status: wired. operation conclusion status: uninspected. |
| Local-process backend does not pretend to implement disabled networking | Backend rejects policy unless networking is unrestricted; executes host commands directly | invariant at acquisition; no host isolation follows. Managed executor also restricts certain vault-backed chat configurations with local-process. | Host permissions remain the effect boundary. Other VM/container backends have different contracts, not audited here. implementation conclusion status: wired. operation conclusion status: uninspected. |

Evidence: SRC-1 `crates/executor/src/basic.rs`, `crates/executor/src/permissions.rs`, `crates/executor/src/turn_queue.rs`, `crates/exoharness/src/basic/turn_queue.rs`, `crates/exoharness/src/sandbox/native.rs`, `crates/executor/src/native/managed_executor.rs`; supporting excerpts below. These are enforcement facts, not end-to-end security or reliability certification.

### Change admission and behavior-shaping state

Definitions can change instructions, model binding, resources, tools and harness selection; operator checks cover sensitive configuration when a scoped caller exists. The Responses loop can admit reusable tool code and reread it on the next round. The persistent Exo harness rebuilds developer messages from identity/local profile plus retained memory, todos and skills, and exposes maintenance instructions naming its own source and build path. Retained-content revisions belong to the memory analysis; this report establishes the consumption and executable-admission boundaries, not memory effectiveness. SRC-1: `crates/executor/src/managed_agents.rs`, `exoharness/typescript/model-runtime/turn-loop.ts`, `exo/harness.ts`.

The guardian route can activate changes to Exo's own code and service machinery. Its tool returns a queued update ID, not a successful deployment. The deferred script sleeps two seconds; it does **not** await proof that the requesting turn finished. This qualifies the tool description's promise to let the turn finish. It runs a fixed build/restart command, records exit status, and attempts conversation-event completion; even that recording can fail. No independent answer oracle or empirical improvement gate was found in this inspected pipeline. Rebuild success is not correctness or improvement evidence. See [RT-RTE-guardian-update](#rt-rte-guardian-update).

## Shared records

### Components

#### RT-CMP-model-binding
Label: Configured provider model

Source-native identity: the resolved agent/thread model binding consumed by Basic/RLM and TypeScript model runtimes. Representational form: distributed-parametric provider model, addressed through symbolic model/base-URL/credential configuration. Storage substrate: weights/provider state external and uninspected; configuration is in Exo managed state. This record is the invoked model, not its configuration object.

Parameters changing during operation: uninspected — no provider training or weight-update implementation is frozen. The inspected requests perform inference, not a parameter update. Exact version pinning: not guaranteed by these call sites; the configured model string is passed through, with per-thread override support. Mutable endpoint resolving to another model: possible through configurable base URL and remote model aliases; actual provider resolution is uninspected. Distinct hosted native-agent model internals remain opaque, not additional inspected weights. SRC-1: `exoharness/typescript/model-runtime/shared.ts`, `exoharness/typescript/model-runtime/responses.ts`, `crates/executor/src/native/rlm.rs`, `crates/executor/src/managed_agents.rs`.

> const origin = new URL(context.agentConfig.baseUrl ?? defaultBaseUrl)
>       .origin;
> --- `exoharness/typescript/model-runtime/shared.ts`

#### RT-CMP-managed-executor
Label: Managed executor

Source-native identity: `ManagedExecutor`, per-thread cached executor and MCP preparation. Representational form: symbolic Rust dispatch/configuration and cache keys. Storage substrate: executable source/binary plus process-local executor cache; persistent configurations are separate objects. It connects MCP, validates thread configuration and dispatches Basic/RLM/TypeScript/Exo. SRC-1: `crates/executor/src/native/managed_executor.rs`.

> fn can_resume_pending_approval(&self, config: &AgentConfig) -> bool {
>         config.harness == AgentHarnessKind::Basic
>     }
> --- `crates/executor/src/native/managed_executor.rs`

#### RT-CMP-typescript-runner
Label: Native TypeScript runner

Source-native identity: `TypeScriptRunnerProcess` launched by the native executor. Representational form: symbolic Node/TypeScript program plus line-protocol requests; natural-language tool instructions are separately model-interpreted. Storage substrate: host process, source modules and filesystem tool registry. The host process executes code with its host environment; shell sandbox selection does not isolate this runner. SRC-1: `crates/executor/src/native/typescript.rs`.

> let mut command = Command::new("node");
>         command.envs(env);
> --- `crates/executor/src/native/typescript.rs`

### Operative objects

#### RT-OBJ-turn-work
Label: Queued TurnWork

Source-native identity: `TurnWork` in a `TurnSubmission` keyed by agent, thread and turn. Representational form: symbolic configuration/request envelope containing natural-language input messages. Storage substrate: coordinator state; Basic serializes it beneath the thread as `turn_queue.json`. Principal, turn/session identity and controls are not model decisions. SRC-1: `crates/executor/src/turn_queue.rs`, `crates/exoharness/src/basic/turn_queue.rs`.

> let work = TurnWork {
>             streaming,
>             agent_config,
>             thread_config: self.get_conversation_config(thread.as_ref()).await?,
>             request,
>         };
> --- `crates/executor/src/turn_queue.rs`

#### RT-OBJ-tool-registry
Label: Installed tool registry

Source-native identity: `.exo/tools` registry with installed manifest, source, initialization and install-path entries; distinct from the optional `.exo/agent-tools` legacy directory. Representational form: symbolic executable modules and JSON metadata; tool descriptions/schema strings additionally guide model choice. Storage substrate: host filesystem lockfile/store and optional legacy source/wrapper files. These are capabilities, not weights. SRC-1: `exoharness/typescript/harness/tool-registry.ts`, `exoharness/typescript/harness/tool-modules.ts`, `exoharness/typescript/harness/built-in-tools.ts`.

> export const DEFAULT_TOOL_REGISTRY_DIRECTORY = ".exo/tools";
> --- `exoharness/typescript/harness/tool-registry.ts`

#### RT-OBJ-guardian-update
Label: Guardian update outcome

Source-native identity: JSON update record under `.exo/guardian-updates/<id>.json`, with reason, agent/conversation IDs and queued/completion state. Representational form: symbolic status/identity and natural-language reason. Storage substrate: host filesystem, with attempted conversation-event completion. This is deployment evidence for later inspection, not a validation oracle. SRC-1: `exo/tools/guardian-tools.ts`, `exo/scripts/deferred-rebuild-and-restart`.

> const outcomePath = join(UPDATE_DIR, `${updateId}.json`);
> --- `exo/tools/guardian-tools.ts`

### Routes

#### RT-RTE-definition-admission
Label: Managed definition admission

CLI/API definition → managed configuration/resources → later turn snapshot. The caller proposes the Markdown/frontmatter and instruction body; software parses, prepares resources and stores config. Physical API/CLI submission does not establish human authorship. Sensitive custom harnesses/tools/tool creation/adapters require an operator when a scoped caller is present. Software can reject unauthorized or invalid configuration; local unscoped execution does not inherit that caller check. Instructions become a system message; harness/model/thread settings select downstream execution. SRC-1: `crates/cli/src/managed_agents.rs`, `crates/executor/src/managed_agents.rs`.

- Immediate return: saved agent/thread handles or configuration/preparation error.
- Later read-back: managed configuration feeds future turn admission; thread options can override model/harness and retain environment choices.
- Delegated visibility: executor receives configuration/resources; model receives instruction content through harness-specific materialization, not all original frontmatter.
- Selection predicate: agent slug/ID or file; thread lookup by requested slug/ID and current overrides.
- Invalidation or expiry: updates replace config; later thread configuration can revise overrides/resources. Queued work retains its captured config.
- Activation or effect: wired path to future requests and executors; actual activation unobserved.
- Evidence limits: current deployment grants, human authorship and correctness of supplied instructions are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission details: open configuration requests, no comparison curriculum or answer oracle. Trigger is create/update/file synchronization. Proposed changes include instructions, harness, model and resources. Caller proposes; role checks and preparation code decide admissibility, not model-quality improvement. Recovery/rollback: resubmission can replace configuration; no automatic restoration of a prior definition is established by these files. Guidance is the submitted instruction body; its content persists as managed instructions. Retained-knowledge revisions are not assessed here.

> caller.policy.check_operator(&caller.principal).await?;
> --- `crates/executor/src/managed_agents.rs`

> config.instructions = vec![crate::harness_helpers::system_message(
>             &definition.instructions,
>         )];
> --- `crates/executor/src/managed_agents.rs`

#### RT-RTE-managed-turn
Label: Managed turn admission and Basic execution

Client user input → scoped queue → managed executor → Basic model/tool rounds → journal completion/client result. Principal is derived from the thread caller if any. Software owns queue identity/control and permission policy; the configured model proposes the next answer/action. Context/state/action effects and recovery are traced in the ordinary account above. SRC-1: `crates/cli/src/tui.rs`, `crates/executor/src/turn_queue.rs`, `crates/executor/src/basic.rs`, `crates/executor/src/permissions.rs`.

- Immediate return: accepted turn identity and stream; client observes text/tool/status events and completion or failure.
- Later read-back: later Basic calls materialize prior messages/tool events from the conversation; recovery reconstructs committed rounds and pending requests.
- Delegated visibility: MCP/runtime executors receive selected tool arguments; frontend tools receive their request; model receives materialized message history, not arbitrary host state.
- Selection predicate: agent/thread scope, queue head/control and saved configuration; model selects tools from supplied definitions.
- Invalidation or expiry: terminal acknowledgement advances queue; session end clears pending approval interpretation; history cache uses event cursors.
- Activation or effect: tool dispatch can alter sandbox/service/client state; final answer and completion are journaled. Actual effects unobserved.
- Evidence limits: persistence does not prove external effect atomicity or safe replay; no trace confirms recovery or successful answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles/mode: open task requests; model proposes tool calls and answers, runtime authorizes and executes, approval responder can veto when policy asks. `AlwaysAllow` and session tool grants are separate modes of authorization, not human approval of every content item. No expected-answer oracle is supplied by this general task path. Tool outputs are evidence available to the agent, not automatically truth labels.

> // A durable acceptance must not be reported as a failed turn if waking
>         // its worker fails. Hosts must arrange another durable wakeup.
> --- `crates/executor/src/turn_queue.rs`

> // Commit the final answer and completion marker together for recovery.
> --- `crates/executor/src/basic.rs`

#### RT-RTE-responses-loop
Label: TypeScript Responses loop

TypeScript `runResponsesHarnessTurn` → resolved credential/model → per-round tool registry and prompt materialization → native API adapter → appended events/tool results. Registry recreation permits newly installed tools on the next round. The persistent Exo profile supplies its own instruction/tool callbacks. SRC-1: `exoharness/typescript/model-runtime/turn-loop.ts`, `exoharness/typescript/model-runtime/responses.ts`, `exoharness/typescript/harness/tools.ts`, `exo/harness.ts`.

- Immediate return: streamed text or nonstreamed events; loop returns latest event ID internally when there are no tool calls, except synthetic tool results cause another round.
- Later read-back: each round rematerializes conversation history and instructions; future invocations can consume retained events and installed capabilities.
- Delegated visibility: provider receives messages, tool definitions, output-token cap and turn metadata; tool handlers receive arguments and execution context.
- Selection predicate: configured model/base URL chooses Anthropic, OpenRouter chat or Responses/chat path; model selects declared tools; instruction callback/profile controls injected content.
- Invalidation or expiry: round budget can terminate; registry is rebuilt each round; tool removal affects subsequent registration.
- Activation or effect: local handlers or runtime callbacks execute tools, then append normalized results; no observed activation.
- Evidence limits: custom harnesses may bypass this loop entirely; registration/policy validation is not a universal provider or host-code gate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles/mode: model-driven open requests, software dispatch and authorization, policy-dependent user veto; no answer oracle. Registry calls authorize non-runtime tools; runtime-authorized entries rely on runtime enforcement. Large results are written to artifacts, with inline value only at or below 8,000 characters and a preview otherwise. This is a code-rule working-context reduction, not semantic summarization. Raw material remains outside the window by artifact reference; universal automatic reload is not established here. SRC-1: `exoharness/typescript/harness/tools.ts`.

> if (tool.authorization !== "runtime") {
>       await this.context.authorizeTool(toolCall.request);
>     }
> --- `exoharness/typescript/harness/tools.ts`

> const value =
>     serialized.length <= TOOL_RESULT_INLINE_LIMIT_CHARS ? args.result : null;
> --- `exoharness/typescript/harness/tools.ts`

#### RT-RTE-native-bridge
Label: Native agent bridge

Exo turn → sandbox native-agent process → native notifications/approval requests → Exo projection and callbacks. Codex owns its own thread and model loop; warm reuse, history replay and native snapshot recovery differ from Basic. Pi uses an explicit RPC extension and transcript bridge. SRC-1: `exoharness/typescript/codex/harness.ts`, `exoharness/examples/typescript/pi-harness.ts`.

- Immediate return: projected messages/tool events and completion, or native/bridge error.
- Later read-back: Codex can reuse a native thread or replay materialized Exo history into a new one; Pi receives materialized conversation transcript with system/developer messages excluded and configured instructions separately supplied.
- Delegated visibility: native worker receives selected model binding, instructions, input and native tool surfaces; dynamic client tools receive only selected calls.
- Selection predicate: configured native harness, native thread/session recovery state and process reuse; Codex bridge accepts supported command/MCP/dynamic-tool requests.
- Invalidation or expiry: process/session loss changes recovery path; unanswered approvals and unsafe in-progress native tools can block reattachment.
- Activation or effect: native tools act inside configured sandbox, while bridged runtime/client tools cross their own boundaries; Exo receives projections, not native internal reasoning.
- Evidence limits: native SDK behavior, compaction, provider-native hosted tools and actual sandbox deployment are uninspected; inspected Codex behavior does not establish parity for Pi, Claude or Cursor.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles/mode: native agent chooses actions; Exo translates supported approvals to `context.authorizeTool`, with accept/decline response. Open task mode, no answer oracle. This is a distributed ownership boundary, not permission bypass inferred merely from using a subprocess.

> "cannot reattach Codex turn with an unanswered approval; the native request was lost during restart",
> --- `exoharness/typescript/codex/harness.ts`

#### RT-RTE-rlm-subquery
Label: RLM context and subquery execution

Conversation history → transcript/history variables in JS state → root model's REPL/subquery requests → selected-context direct model call → preview/optional JS variable → root final answer. Rust owns dispatch; root model decides decomposition and arguments. SRC-1: `crates/executor/src/native/rlm.rs`.

- Immediate return: subquery answer preview, truncation flag and optional stored variable name; root resolves its final answer after further rounds.
- Later read-back: inapplicable — subquery variables/history within this turn are working state; this record does not establish cross-invocation restoration of the JS frame.
- Delegated visibility: subquery receives configured instructions, a fixed subquery system instruction and selected prompt/variable text, not the whole foreground history; tools are empty.
- Selection predicate: root model chooses `subquery` or `subquery_variable`, question and optional target; Rust resolves variable contents.
- Invalidation or expiry: turn-local JS state is reconstructed at turn start; budget violation errors instead of silently continuing.
- Activation or effect: returned value can enter root history or JS state; no tool definitions are supplied to subquery model.
- Evidence limits: model compliance and benefit of decomposition unobserved; no complete native-agent context account follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode/oracle: open user task with instructed decomposition, no expected-answer oracle. The separate request resembles a frame whose selected input and return value cross a context boundary. Full response can remain in a JS variable while only its preview reaches root history; no reference-counting or automatic liveness scheme is established.

> messages,
>                 tools: Vec::new(),
>                 max_output_tokens: agent_config.max_output_tokens,
> --- `crates/executor/src/native/rlm.rs`

#### RT-RTE-tool-admission
Label: Reusable tool admission

Model/caller proposal → `manage_tool` manifest source and initialization → staged import/initialization/validation → registry commit → next-round registration. The optional legacy `install_agent_tool` instead writes source and wrapper modules into `.exo/agent-tools`. These stores are not interchangeable, though both feed later registries. SRC-1: `exoharness/typescript/harness/built-in-tools.ts`, `exoharness/typescript/harness/tool-registry.ts`, `exoharness/typescript/harness/tool-modules.ts`.

- Immediate return: installation metadata and `availableNextRound`, or validation/conflict/import error.
- Later read-back: each default/Exo registry loads installed modules; legacy directory loads only with agent-tool creation enabled.
- Delegated visibility: importer/initializer receives module and initialization/context; later provider gets tool definition, not source; handler gets selected arguments.
- Selection predicate: install action and manifest ID/source; registry entries select executable module; model later selects its exposed tool name.
- Invalidation or expiry: remove unlists/deletes installed store; replacement commits new entry and deletes old store; broken modules are skipped on registration.
- Activation or effect: module import/initialization can execute host code during validation/loading; later handler calls add model-selectable capability. Observed usage uninspected.
- Evidence limits: structural validation is not a semantic sandbox or correctness test; import-time effects can precede registry admission; no beneficial capability change established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission details: open tool-creation requests; model can propose source/initialization, runtime permission policy controls invocation, loader/manifest/schema/name rules accept or reject structure. No mandatory per-source human review or answer oracle is established by this pipeline. Source-authored guidance requests strict schemas/type-only imports and warns about secret references; guidance compliance is not isolation. Manifest registry stages source, holds a lock during read-modify-write, and cleans failed installations; successful replacement deletes the old install rather than guaranteeing automatic rollback. Legacy validation cleans temporary files but is a distinct simpler write mechanism. Source and initialization persist; host environment references may resolve at load time. No theory revision or learning is inferred from successful installation.

> const module = (await import(importSpecifier(modulePath, source))) as Record<
>     string,
>     unknown
>   >;
> --- `exoharness/typescript/harness/tool-modules.ts`

> const validation = await validate(modulePath, request.initialization);
> --- `exoharness/typescript/harness/tool-registry.ts`

#### RT-RTE-background-wakeup
Label: Scheduler and hosted wakeup progression

Scheduled command → result artifact/pending fire → conversation user-message wakeup → ordinary runtime send → ended session. Scheduler owns firing/delivery; model owns subsequent interpretation and any explicit external response. Separately, Cloudflare thread Durable Objects recover queued turns on object startup/request/alarm. These are host wake mechanisms, not new model policies. SRC-1: `crates/executor/src/native/scheduler_runtime.rs`, `crates/executor/src/native/conversation_wakeup.rs`, `exoharness/cloudflare/src/provider.ts`.

- Immediate return: scheduled output artifact and delivered wake/session result, or failure; hosted recovery drains pending work.
- Later read-back: pending fire records support redelivery; result artifacts and wakeup messages can reach later conversation consumers.
- Delegated visibility: conversation receives formatted exit/error/report instructions and stdout/stderr previews plus artifact identity, not an unrestricted dump of all scheduler state.
- Selection predicate: due task claim, owner conversation/task slot and pending-delivery state; Cloudflare object name selects thread.
- Invalidation or expiry: delivered fire is marked; missing owners retire pending wakes; hosted recovery can be retried after failure.
- Activation or effect: runtime sends user content and closes wakeup session after result; sandbox command already ran before wake. Subsequent behavioral dependence unobserved.
- Evidence limits: crash after delivery before mark can repeat wakeup; background transport does not prove exactly-once work or reliable messaging. Scheduling/adaptor creation admission is not exhaustively traced here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode/oracle: unattended continuation of configured tasks, not a bounded experimental curriculum or correctness oracle. Wakeup filesystem lock serializes same-conversation delivery locally. Result preview/reportPrompt transformations bound what the model receives; logs alone do not imply learning. Adapter-specific trigger/acknowledgement/retry policies remain outside this detailed route trace.

> store.put_pending_fire(&fire).await?;
>     send_conversation_wakeup(harness.as_ref(), &agent, &conversation, fire.prompt.clone()).await?;
> --- `crates/executor/src/native/scheduler_runtime.rs`

#### RT-RTE-guardian-update
Label: Deferred Exo self-update activation

Agent source edits → model `rebuild_and_restart_exo` request → host detached deferred script → guardian fixed build/restart → outcome file and attempted conversation event. A writable mounted source tree and host maintenance permission are consequential preconditions, not proven deployment grants. The practical profile registers this host tool. SRC-1: `exo/harness.ts`, `exo/profiles/practical.ts`, `exo/tools/guardian-tools.ts`, `exo/scripts/deferred-rebuild-and-restart`, `exo/scripts/exo-service-guardian`.

- Immediate return: queued status, update ID, PID, reason and outcome/log paths; not build completion.
- Later read-back: update JSON and attempted conversation event make outcome inspectable; restart notices can wake adapter conversations.
- Delegated visibility: detached process gets fixed command and record identity; restarted services consume rebuilt executable/current source configuration; conversation sees recorded outcome if completion recording succeeds.
- Selection predicate: registered maintenance tool, parsed reason and fixed `restart-all --build`; source contents at build time determine product.
- Invalidation or expiry: completion changes queued record to succeeded/failed; script can fail event recording; no automatic old-build rollback established.
- Activation or effect: build/restart can change future host execution; current turn is given a two-second delay, not a completion barrier.
- Evidence limits: no execution trace establishes completed activation, evidence-responsive update determination, later changed behavior or improvement. Fixed build success is not an answer oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission details: source edits can be proposed by the agent or another writer; tool permission policy can veto the maintenance invocation. Model/human authorship of actual edits is unobserved. Host script/build exit status decides pipeline success; no per-change human approval or independently evaluated behavioral criterion is established here. Operating mode is open maintenance prompted by changes, not a controlled comparison. Guidance names the self map, preservation of `.exo`, snapshots before risky changes and rebuilding after edits. Proposed source and durable reason/outcome persist separately. Recovery is preserved state, restart/drain mechanics and possible manual repair; no semantic correctness gate is established by the inspected build commands.

Self-improvement attribution: bounded system is the local Exo source/runner/services, horizon spans rebuild to later service turns, objective would need to be specified independently (for example the particular defect being repaired). This is a wired self-change capacity, not evidence of exercised self-improvement. Link 1 (objective-bearing evidence determining an actual update) and link 4 (later operation causally depending on it) are unestablished; links 2–3 are implemented possibilities through build/restart and later consumers, not observed events. Successful improvement and learning remain uninspected. Self-referential maintenance guidance alone does not establish content-directed criticism or an autonomous/reflective theory builder; no such theory route is asserted here.

> const result = runGuardianDeferredWithOutcome(
>     ["restart-all", "--build"],
>     updateId,
>     outcomePath,
>     reason,
>   );
> --- `exo/tools/guardian-tools.ts`

> sleep "$delay"
> set +e
> "$@"
> code=$?
> --- `exo/scripts/deferred-rebuild-and-restart`

> run_cargo build -p exo --ignore-rust-version
> --- `exo/scripts/exo-service-guardian`

### Claims

#### RT-CLM-recovery-scope
Label: Durability is not arbitrary effect replay

Claimed operation: accepted turns retain work across wake failure, and Basic reconstructs committed rounds without fresh model selection. Guarantee owner: queue host/coordinator and Basic executor. Enforcement: durable enqueue and `load_turn_progress` checks. Strength: protocol. Covered path: stored managed Basic turns; native/TypeScript paths have different contracts. Required external contracts: durable storage, future wakeup, correct tool/frontend behavior and journal completeness. SRC-1: `crates/executor/src/turn_queue.rs`, `crates/executor/src/basic.rs`, `crates/exoharness/src/basic/turn_queue.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

The source-supported falsifier of a broader safe-resumption claim is the explicit unresolved-tool guard. It prevents exactly-once-effect and universal resumption conclusions, not the narrower durable-acceptance conclusion.

> "cannot safely resume unresolved tool call `{}` (`{}`) for turn {}",
> --- `crates/executor/src/basic.rs`

#### RT-CLM-isolation-scope
Label: Sandboxing has path-specific scope

Claimed operation: sandbox backends control sandbox command execution, not every code path in Exo. Guarantee owner/enforcement: chosen backend at acquisition/execution; managed validation rejects certain unsafe vault/local-process combinations. Strength: protocol for configuration rejection; no claimed guarantee of whole-runtime isolation. Covered paths: commands through the chosen sandbox handle. Alternates: host TypeScript import/handlers, web tools, guardian subprocesses, local-process backend and trusted custom harness code. Required external contract: backend/host isolation, mounts and provider behavior, none observed. SRC-1: `crates/exoharness/src/sandbox/native.rs`, `crates/executor/src/native/typescript.rs`, `crates/executor/src/native/managed_executor.rs`, `exo/tools/guardian-tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> request.spec.policy.networking == SandboxNetworkPolicy::Unrestricted,
>             "local process does not support policy.networking.disabled"
> --- `crates/exoharness/src/sandbox/native.rs`

> "vault-backed chat requires an isolated sandbox; local-process can read host credentials"
> --- `crates/executor/src/native/managed_executor.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-harness-instructions
Label: Harness instructions to model decisions

Consumer: configured model/native harness. Channel: Basic system instructions, Responses instruction callbacks, and native bridge instruction/history transformation. Force: model-interpreted natural language, not a hard permission boundary. Horizon: current model request and later requests while managed instructions/local profile remain selected. The Exo harness recomputes local prompt, memory, todos and skills instructions; memory-part identities and revisions are left to the memory member. SRC-1: `crates/executor/src/managed_agents.rs`, `exoharness/typescript/model-runtime/turn-loop.ts`, `exo/harness.ts`.

> const localPrompt = readLocalPrompt();
>   if (localPrompt !== null) {
>     instructions.push({
>       role: "developer",
>       content: localPrompt,
>     });
>   }
> --- `exo/harness.ts`

#### RT-BAP-installed-code
Label: Installed code to host behavior

Consumer: host Node loader/initializer, then model-visible registry and selected handler. Channel: filesystem module import, initialized Tool instance, definition and handler dispatch. Force: executable authority at import/initialization and handler execution; description text only influences model selection. Horizon: same-turn next round and future invocations until removal/replacement, subject to successful loading. This differs from mere prompt instruction authority and from sandbox shell rights. SRC-1: `exoharness/typescript/harness/tool-modules.ts`, `exoharness/typescript/harness/tool-registry.ts`; [RT-RTE-tool-admission](#rt-rte-tool-admission).

> const tool = await loadAgentTool(
>         context,
>         await installedToolModulePath(installed),
>         installed.initialization,
>       );
>       registry.register(tool);
> --- `exoharness/typescript/harness/tool-modules.ts`

#### RT-BAP-rebuilt-services
Label: Rebuilt source to subsequent service execution

Consumer: guardian-managed scheduler/adapter binaries and control REPL child; TypeScript harness loads current modules through its runner. Channel: built executables, restart markers and process launch. Force: executable behavior, not advisory deployment prose. Horizon: later service lifetime after successful rebuild/restart. Actual source change, installation success and exercised dependence remain unobserved. SRC-1: `exo/scripts/exo-service-guardian`, `exo/scripts/deferred-rebuild-and-restart`, `crates/executor/src/native/typescript.rs`; [RT-RTE-guardian-update](#rt-rte-guardian-update).

> printf 'reason=guardian-build\n'
> --- `exo/scripts/exo-service-guardian`

## Annotations

none
