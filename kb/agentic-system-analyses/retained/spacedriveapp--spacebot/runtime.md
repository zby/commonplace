---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Spacebot runtime baseline: conversational execution, delegated workers, autonomous epochs, context control and change admission at the frozen revision."
run-id: AAS-2026-10-14-spacebot-6a954b400f95-01
reviewed-boundary: "5c2ee47b397e09c956dc15000ea576ecd28e92bb"
---

# Spacebot runtime report

## Runtime account

### Evidence and consequential work

Spacebot owns the enclosing execution loop: it receives messages, constructs model-visible context, offers process-specific tools, dispatches work, persists state, and routes responses. Its consequential work includes filesystem and shell effects, remote tools, task-board changes, and retained instruction changes, not just producing chat text. The [boundary](boundary.md#boundary-and-evidence) fixes SRC-1 and the whole-system scope. All findings below are implementation or doctrine/design findings at that revision. No executable, test, provider, service or example was run. Operation and benefit are uninspected, not absent.

Additional SRC-1 implementation coverage beyond the boundary's initial inspection includes `src/tools/spawn_worker.rs`, `src/tools/task_update.rs`, `src/tools/skill_manage.rs`, `src/tools/read_skill.rs`, `src/tools/install_skill.rs`, `src/tools/file.rs`, `src/tools/shell.rs`, `src/sandbox.rs`, `src/mcp.rs`, `src/llm/model.rs`, `src/opencode/server.rs`, `src/opencode/worker.rs`, `src/opencode/types.rs`, `src/api/config.rs`, `src/api/mcp.rs`, `src/tools/factory_update_config.rs`, and `src/skills/installer.rs`. Selected bodies and bounded searches, not exhaustive audits, support the specific findings below. Additional doctrine is `prompts/en/memory_persistence.md.j2`. Memory-specific revision mechanisms and their completeness belong to the memory member; this report establishes execution and instruction-admission paths without substituting a memory inventory.

### Ordinary message to result

The shipped Start command enters `cmd_start`. The main loop resolves an inbound message to an agent and conversation, loads Portal or platform conversation settings with binding defaults on lookup failure, and creates a user `Channel` when needed. It registers the channel with process control and API state. Optional platform backfill is rendered into the system prompt, while the channel hydrates its own durable conversation history on `run`. The outbound task separately delivers responses through messaging adapters and SSE. These are the shipped enclosing caller and return path, not an assumed external host (SRC-1, `src/main.rs`, `src/agent/channel.rs`; [RT-RTE-channel-turn](#rt-rte-channel-turn)).

Agent ID, conversation/channel ID and process registration distinguish the principal, conversation and live execution. The current inbound sender drives per-turn authority checks. The channel model chooses reply, skip, branch, worker or other granted tools. Code chooses the tool set, model route, turn budget and history transformations. Natural-language instructions guide the model; symbolic tool schemas and Rust handlers determine admissible effects. Conversation state, memory/task renderings, skills metadata, project context and identity/instruction material enter prompt construction; attachments and prior messages enter history (SRC-1, `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`). Model inference uses [RT-CMP-spacebot-model](#rt-cmp-spacebot-model); its endpoint is not a frozen model version.

The hook invokes a bounded streaming agent loop. Text resembling tool syntax can trigger two correction retries. The result is applied to channel history; explicit reply/skip flags and adapter rules govern fallback output. A successful model response alone does not establish successful delivery: routed output and logging have their own failure paths. The next-step owner remains the channel except while a delegated process owns its private loop. Long-lived context is maintained separately, and persistence branches may run silently (SRC-1, `src/agent/channel.rs`; [RT-RTE-context-control](#rt-rte-context-control), [RT-RTE-skill-change](#rt-rte-skill-change)).

### Delegation, background entry and return

Branches clone channel history, get a new branch ID, separate preamble and ToolServer, and return a conclusion rather than merging their full private transcript into the caller. A branch is not merely a memory query: the implemented server also includes task operations, file reading, and profile-dependent goal, skill and wiki operations. Ordinary branches and persistence branches receive different mutation grants. Built-in workers receive task context and either clean or forked history; their dedicated ToolServer can execute shell/file work and selected browser, search, memory, wiki, secrets and MCP operations. Required skills enter the worker preamble in full, while suggested skills are index hints (SRC-1, `src/agent/branch.rs`, `src/agent/channel_dispatch.rs`, `src/tools.rs`; [RT-RTE-delegated-work](#rt-rte-delegated-work)).

Worker IDs, registration IDs, operation IDs, provenance and task attempts separate current control from durable result identity. Workers run segmented loops, can accept follow-up/injected context, and have a wall-clock timeout that recovers available partial output. Dispatch supervision commits a terminal outcome before constructing the normal completion event; it retries boundedly and can fail without a terminal notification. Completion reaches the channel for possible retrigger and relay, not guaranteed delivery of the entire worker transcript (SRC-1, `src/agent/worker.rs`, `src/agent/channel_dispatch.rs`, `src/agent/channel.rs`).

Cron is another shipped channel entry wired in main, with its own outcome/delivery semantics rather than an ordinary live reply. This inspection establishes its entry and the channel's cron handling, not an audit of scheduler timing or external delivery. Autonomy has a distinct resident channel and durable epochs. The supervisor applies the lesser of per-agent level and instance ceiling, checks pause/due conditions, reserves inbox capacity, begins a durable run, claims wake events and injects a briefing. A model then chooses actions within that level's tool grants. Autonomous output goes to task/working state and `autonomy_complete`, not ordinary user reply tools (SRC-1, `src/main.rs`, `src/agent/autonomy.rs`, `src/agent/channel.rs`, `src/tools.rs`; [RT-RTE-autonomy-epoch](#rt-rte-autonomy-epoch)). Heartbeats are state-reassessment inputs, not evidence that useful work occurred.

### Forcing cases and guarantee boundaries

Three forcing cases were selected because they change where authority is enforced.

1. **Direct execution versus delegated execution.** Standard channel mode is not universal. Direct mode registers shell and file tools in the foreground channel, and autonomy Act adds execution tools. Therefore "all execution is isolated in workers" is false at the capability level. Model calls without a tool server also exist: the rolling compactor is explicitly summary-only. Role-specific ToolServers constrain tools offered through that particular agent call, not every operation of the enclosing process (SRC-1, `src/agent/channel.rs`, `src/tools.rs`, `src/agent/compactor.rs`; [RT-CLM-role-grants](#rt-clm-role-grants)).
2. **OpenCode rather than the built-in worker.** The dispatch tool can select an OpenCode worker. Its driver creates or resumes an external session, drives it through HTTP/SSE, and persists session/transcript/lifecycle state. The server starts through raw `Command::new(opencode_path)`, not `Sandbox::wrap`. Permission events are emitted for visibility but the worker immediately replies `Once`; they are not a human approval barrier. The external OpenCode implementation and deployment isolation are not frozen (SRC-1, `src/tools/spawn_worker.rs`, `src/opencode/server.rs`, `src/opencode/worker.rs`; [RT-RTE-opencode-work](#rt-rte-opencode-work)).
3. **Skill policy versus generic file mutation.** Agent-origin `skill_manage` rejects installed or pinned targets and requires a prior read for edits. Ordinary conversation branches get User origin, not Agent origin. Moreover workers/direct channels have generic file and shell capabilities; the generic file resolver checks path allowance, not skill provenance or pin state. Thus the skill rails are a local mutation protocol, not a global filesystem invariant. This inspection establishes an alternate writable surface, not an observed bypass or malicious action (SRC-1, `src/tools.rs`, `src/tools/skill_manage.rs`, `src/tools/file.rs`; [RT-RTE-skill-change](#rt-rte-skill-change)).

The inspected task approval gate is similarly scoped: `resolve_task_plan` rejects pending-approval/backlog tasks for **task-bound execution**. `task_context_number` requests read-only reference context without that execution claim, and a spawn with no task number has no task-plan gate. Direct mode can execute without using task spawning. The gate therefore does not prove that every shell or remote action receives human approval. Autonomy task-update code additionally rejects approval/ready transitions; this is an autonomy-tool check, not proof against all administrative or filesystem paths (SRC-1, `src/tools/spawn_worker.rs`, `src/tools/task_update.rs`).

| Load-bearing guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths / required external contract | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| Role-specific tool exposure | Runtime, ToolServer construction and per-turn add/remove in channel | invariant at the offered-tool-list boundary; covers inspected built-in agent calls | Direct/autonomy/admin have other lists; compactor has none; MCP/OpenCode effects need their own contracts. Requires the external agent/tool library to dispatch only registered tools. | wired | uninspected |
| Task-plan approval check | SpawnWorkerTool, `resolve_task_plan` | protocol for task-number execution admission | Reference-only and unbound spawns, direct execution and external tool effects are not universal task approval. Task store must supply authoritative status. | wired | uninspected |
| Worker result committed before ordinary completion event | Dispatch supervision, `finalize_worker_supervision` | protocol for that finalizer, not a liveness guarantee | Exhausted commits log failure without the event; task-attempt recording can fail independently. Requires SQLite durability and event consumers; restored/interactive paths need lifecycle-specific handling. | wired | uninspected |
| Filesystem containment | Sandbox backend plus generic file resolver | best effort for configured tools, not a deployment guarantee | Disabled mode and unavailable backend permit subprocess passthrough; OpenCode and remote MCP do not inherit this wrapper. Requires OS backend availability, correct configuration and separately enforced deployment/network isolation. | wired | uninspected |
| Agent-origin skill protection | `existing_skill_rails`, profile-selected origin | protocol on `skill_manage` calls | User-origin grants differ; file/shell, installer and API paths are separate. No filesystem-wide pin enforcement established. | wired | uninspected |

SRC-1 evidence for this table is retained in [RT-RTE-delegated-work](#rt-rte-delegated-work), [RT-RTE-opencode-work](#rt-rte-opencode-work), [RT-RTE-skill-change](#rt-rte-skill-change), and [RT-CLM-role-grants](#rt-clm-role-grants). The current grant set depends on settings, origin, memory mode, browser/search credentials, available MCP tools and wiki/lifecycle configuration; the capability surface is larger than any one grant set. No supplied deployment establishes which grants or isolation backend were active.

### Changes admitted to later operation

The principal inspected instruction-change loop is persistence-triggered skill reflection. Code selects eligible turns/worker signals and starts a profile-limited branch; its prompt asks the model to inspect transcripts, prefer patching existing task-class procedures, and decline unsupported lessons. The model proposes and selects content. `skill_manage` validates structural constraints and origin rails, writes files, records provenance when available and reloads skills. No per-content human approval or behavioral correctness oracle is enforced by this path. Later channels/branches/workers see the index, requested skill bodies, or required bodies. Delivery of a procedure is established; compliance, successful criticism and improved capacity are not (SRC-1, `src/agent/channel.rs`, `src/tools.rs`, `src/tools/skill_manage.rs`, `src/skills.rs`, `src/tools/read_skill.rs`, `prompts/en/memory_persistence.md.j2`; [RT-BAP-skill-instruction](#rt-bap-skill-instruction)).

Other change-admission paths are materially distinct: registry/GitHub skill installation reloads external instruction files; API configuration and factory tools write production settings and reload live runtime configuration. MCP adds remote capabilities to workers. These are not all instances of the skill-reflection rails. The installation source uses mutable `main.zip`, not a commit-pinned installed version. Administration can change model routes and runtime machinery without demonstrating an improvement procedure (SRC-1, `src/tools/install_skill.rs`, `src/skills/installer.rs`, `src/api/config.rs`, `src/tools/factory_update_config.rs`, `src/mcp.rs`; [RT-RTE-capability-admission](#rt-rte-capability-admission)). Source-code editing is afforded by generic shell/filesystem tools where permitted, but an automatically evaluated, approved and deployed binary-successor loop was not traced. API endpoint inventories, release packaging and available configuration files do not establish such a loop.

Unresolved detail remains local: provider-native or provider-internal tools beyond the serialized function tools inspected in `src/llm/model.rs`, remote MCP implementation controls, all API mutation handlers, durable wake failure interleavings, cron timing/delivery, and every restored-worker variant were not exhaustively inspected. The result is a baseline of material routes and control counterexamples, not a security audit or a complete proof of recovery. No throughput, latency, cost saving, production reliability or improvement effect follows from these source definitions.

## Shared records

### Components

#### RT-CMP-spacebot-model
Label: SpacebotModel provider-backed inference

Source-native identity: `SpacebotModel` wraps configured LLM providers for channels, branches, workers and compaction. The inference component is distributed-parametric; its model-name/routing envelope is symbolic. Storage substrate: remote provider parameters are outside SRC-1; runtime stores model names, provider configuration and routing state in ordinary Rust/configuration structures. Provider weights and training internals are uninspected. No weight-update operation was established in the inspected dispatch path; this is not a claim about provider-side training or retained non-parametric state.

Exact model version pinned: no single exact model version is fixed by the reviewed repository commit. Runtime overrides and routing determine the name. Parameters change during operation: uninspected at external provider boundary. Mutable endpoint can resolve to another model: yes at the client-routing level through configuration and fallback; alias resolution within a provider remains opaque. These distinctions apply to the inspected routes using this wrapper, not OpenCode's internal inference implementation (SRC-1, `src/llm/model.rs`, `src/agent/channel.rs`, `src/agent/worker.rs`, `src/agent/branch.rs`, `src/agent/compactor.rs`).

> // No routing config — just call the model directly, no fallback/retry
> --- `src/llm/model.rs`

> // Try fallback chain, each with their own retry loop
> --- `src/llm/model.rs`

Retries and fallback establish implementation capacity for recovery, not model equivalence, reproducibility or successful operation.

### Operative objects

#### RT-OBJ-channel-history
Label: Channel live history

Source-native identity: `ChannelState.history`, an `Arc<RwLock<Vec<Message>>>`; substrate is live process memory with separately stored durable conversation records. Natural-language utterances, summaries and tool results are model-interpreted; symbolic message roles and tool-call structures receive fixed serialization/dispatch treatment. This record concerns the live history container, not the entire memory store. The channel clones it for inference and branches, applies result history, and invokes rolling or chronicle maintenance. Durable transcript-to-live-history reconstruction and checkpoints bound what later invocations receive (SRC-1, `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`, `src/agent/compactor.rs`, `src/agent/chronicle.rs`).

> // Clone history out so the write lock is released before the agentic loop.
> --- `src/agent/channel.rs`

#### RT-OBJ-skill-set
Label: SkillSet procedures and index

Source-native identity: `SkillSet` and its `Skill` values, loaded from built-in, instance and workspace sources. Storage substrate: embedded built-in content, filesystem `SKILL.md`/support files, and runtime skill collections; usage/provenance records are separate metadata. Procedure bodies and descriptions are natural-language instructions. Names, paths, categories, source/origin, pin state and required/suggested lists are symbolic selectors or admission metadata. This declaration identifies the runtime instruction surface, not all retained knowledge (SRC-1, `src/skills.rs`, `src/tools/skill_manage.rs`, `src/tools/read_skill.rs`).

> /// Workers see all available skills with any channel-suggested skills flagged.
> /// They decide which skills are relevant and read them via the read_skill tool.
> --- `src/skills.rs`

### Routes

#### RT-RTE-channel-turn
Label: Channel message execution

Endpoints/progression: inbound adapter or Portal message → main's agent/conversation resolution → user Channel → rendered preamble/history → model/hook/tool loop → routed response and later event processing. Runtime owns admission, settings and dispatch; model owns semantic next-action selection under those grants. Effects include replies, task/state mutation and delegated work. Mode is an open request, not a bounded evaluation curriculum. No expected-answer oracle is used by the inspected turn loop; users may provide feedback but are not an enforced per-action evaluator (SRC-1, `src/main.rs`, `src/agent/channel.rs`).

- Immediate return: explicit reply/skip behavior, permitted plaintext fallback, errors or delegated-process acknowledgement/status; text generation is distinct from delivered output.
- Later read-back: conversation logging and channel hydration restore prior messages; separately rendered memory, task and skills state may shape later turns.
- Delegated visibility: branches clone current history; workers receive clean or forked history and task/skill context, as detailed in the delegation route.
- Selection predicate: agent/binding and conversation identity, resolved conversation settings, channel kind, sender authority and per-process model override before default routing.
- Invalidation or expiry: per-turn tools are removed after the loop; model turn budget and context maintenance bound live state; persistence is not implied to expire with a turn.
- Activation or effect: tool handlers and response routing are wired; semantic compliance and actual delivered responses are unobserved.
- Evidence limits: source trace only; settings, inbound identities, provider results and deployed adapter behavior were not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let sender_is_authority = crate::commands::dispatch::sender_is_authority(&current_inbound);
> --- `src/agent/channel.rs`

> .prompt_once_streaming(&agent, &mut history, user_text, max_turns)
> --- `src/agent/channel.rs`

#### RT-RTE-delegated-work
Label: Branch and built-in worker execution

Endpoints/progression: channel or eligible branch delegation → spawn preparation → isolated agent loop → result/lifecycle persistence → process event → channel retrigger/relay. Branch and worker are separate loops grouped here only for their shared delegation/return boundary; their grants and context differ as described above. Model selects the work request; Rust dispatch reserves identifiers/concurrency and builds context. Worker shell/filesystem tools execute effects locally; browser/search and MCP cross service boundaries. Required skills guide the proposal/execution but are not correctness checks. Open-request operation has no expected-answer oracle at this runtime boundary (SRC-1, `src/agent/channel_dispatch.rs`, `src/agent/branch.rs`, `src/agent/worker.rs`, `src/tools.rs`).

Task execution admission: for a bound task, task/project plan fields win over conflicting worker type arguments, required skills are resolved and a task attempt is claimed. Code can reject unapproved/terminal tasks or unavailable worker capacity. Human approval is represented by upstream task state; merely selecting a task is not new approval. Unbound/reference-only spawning differs. Work product acceptance is a later model/operator responsibility, not guaranteed by a successful worker terminal kind (SRC-1, `src/tools/spawn_worker.rs`).

- Immediate return: spawn result identifies the branch/worker; branch conclusion or worker outcome arrives asynchronously, including partial, blocked, timeout or failed outcomes.
- Later read-back: process logger retains worker outcomes/transcripts and lifecycle state; interactive resumption can seed prior transcript; task outcomes and reflection inspection can later consume them.
- Delegated visibility: branch gets a history clone; built-in worker gets task context, own preamble, required skills, optional memory context and clean/forked history; private reasoning/transcript is not wholesale merged back.
- Selection predicate: tool arguments, task plan, worker type, context settings, concurrency limits and autonomy-epoch admission; memory/wiki/browser/MCP grants are conditional.
- Invalidation or expiry: per-process tool server/context ends with the loop; wall-clock timeout, segment/turn/context limits and process cancellation bound work; durable outcomes survive completion.
- Activation or effect: built-in tool handlers execute granted effects; terminal commit precedes the finalizer's completion event, but exhausted commits suppress that event rather than guaranteeing liveness.
- Evidence limits: no worker execution or cancellation race was observed; test definitions and implementation ordering are not demonstrated recovery results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> TaskStatus::Ready | TaskStatus::InProgress => {}
> TaskStatus::PendingApproval | TaskStatus::Backlog => {
> --- `src/tools/spawn_worker.rs`

> // Task execution and task-reference spawns both load authoritative
> // context. Only execution claims the task and enforces approval.
> --- `src/tools/spawn_worker.rs`

> "worker terminal outcome remained unavailable after retries"
> --- `src/agent/channel_dispatch.rs`

> for mcp_tool in mcp_tools {
>     server = server.tool(mcp_tool);
> }
> --- `src/tools.rs`

#### RT-RTE-opencode-work
Label: OpenCode worker session

Endpoints/progression: spawn worker type `opencode` → resolved directory/server pool → external session and prompt → SSE processing → persisted transcript/outcome and channel events. Spacebot owns admission, session driver and parent return; OpenCode owns internal planning/tool execution, and its provider/machinery is outside the frozen repository. This is an open work request, not a benchmark. No answer oracle is established in the driver. User follow-ups/questions can enter interactive control, but emitted permission notifications are not a veto gate: the driver auto-allows (SRC-1, `src/tools/spawn_worker.rs`, `src/opencode/server.rs`, `src/opencode/worker.rs`).

- Immediate return: worker identity/status, asynchronous session text/tool/status events and eventual worker result or interactive idle state.
- Later read-back: session ID/port and transcript snapshots support resuming interactive workers; the driver loads existing parts to continue persistence.
- Delegated visibility: prompt/system instruction and required task context cross into the OpenCode session; internal model/tool context and external implementation are uninspected.
- Selection predicate: requested/planned OpenCode type and a resolved directory; OpenCode workers are forced interactive by the spawn tool.
- Invalidation or expiry: abort/session lifecycle, server restart and parent worker supervision constrain work; exact external session retention is uninspected.
- Activation or effect: raw subprocess startup and HTTP/SSE controls are wired; `PermissionAsked` is followed by `PermissionReply::Once`, not an operator decision.
- Evidence limits: no OpenCode binary or session was run; neither its internal security nor inheritance of a deployment sandbox is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let process = Command::new(opencode_path)
>     .args(["serve", "--port", &port.to_string()])
> --- `src/opencode/server.rs`

> .reply_permission(&permission.id, PermissionReply::Once)
> --- `src/opencode/worker.rs`

#### RT-RTE-autonomy-epoch
Label: Autonomous epoch admission

Endpoints/progression: supervisor timer/wake → effective-level/pause/due checks → inbox reservation and durable run/wake claim → resident channel briefing → model actions and child supervision → epoch completion. Runtime code decides admission; the model decides what work merits action within the selected grants. Off/Suggest/Act level and instance ceiling are controls, not an objective oracle. Mode is ongoing state-driven work, with no fixed reference answer. Task/goal/project state guides proposals. Code can deny actions by tool omission or spawn checks; humans can change configuration/pause, but no per-content human approval is enforced for every autonomous action (SRC-1, `src/agent/autonomy.rs`, `src/agent/channel.rs`, `src/tools.rs`, `src/tools/task_update.rs`).

- Immediate return: internal run/status/task-state changes rather than ordinary user reply; autonomy completion closes the epoch contract.
- Later read-back: wake claims and autonomy runs persist; briefings incorporate pending events and current work state for later decisions.
- Delegated visibility: children carry autonomy provenance and are registered to the epoch; parent supervision uses their state/results.
- Selection predicate: min(agent level, instance ceiling), pause, active hours/interval/pending wakes, inbox capacity and durable run admission.
- Invalidation or expiry: level changes, finish requests, generation checks, child settlement and shutdown constrain an epoch; stale activity is not interchangeable with a new epoch.
- Activation or effect: briefing injection and level-dependent tool grants are wired; no autonomous action was observed.
- Evidence limits: durable wake/failure interleavings and all shutdown paths were not exhaustively inspected; no evidence of useful work or safe deployment was supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> level: raw_config.level.min(**deps.autonomy_ceiling.load()),
> --- `src/agent/autonomy.rs`

> if config.level == AutonomyLevel::Off || deps.pause_reason().is_some() {
>     return Ok(None);
> }
> --- `src/agent/autonomy.rs`

> "autonomy cannot approve tasks or move them to ready"
> --- `src/tools/task_update.rs`

#### RT-RTE-context-control
Label: Context isolation and history reduction

Endpoints/progression: code detects history/context pressure or a fork is requested → private context construction, trimming or summarization → next model invocation. Runtime owns thresholds, cuts, retention floors, mode and fences; the summarizer model owns summary content. This is runtime working-context control, not a correctness oracle. The selected history object is [RT-OBJ-channel-history](#rt-obj-channel-history) (SRC-1, `src/agent/channel.rs`, `src/agent/channel_dispatch.rs`, `src/agent/compactor.rs`, `src/agent/chronicle.rs`, `src/agent/worker.rs`, `src/agent/branch.rs`, `src/llm/model.rs`).

- Immediate return: smaller/fresh child context, rolling summary plus recent tail, or chronicle checkpoint/trim action; emergency truncation can discard history without summarizing it.
- Later read-back: summaries in live history reach later calls; chronicle checkpoints and durable conversation rows support later rendering/expansion and hydration. Rolling live summary is not itself proof of cross-restart summary persistence.
- Delegated visibility: forks copy chosen history into private frames; clean workers keep channel turns out; conclusions/results escape while full private tool history stays outside the caller window.
- Selection predicate: channel compaction mode and thresholds, durable boundaries/fence state, clean/fork setting, rendered prompt size and provider context ceiling; oldest prefixes are preferentially removed, with tool-result alignment and recent-message floors.
- Invalidation or expiry: child frames end with their processes; history-head/mode fence changes can reject stale rolling summaries; emergency paths and provider backstops may drop content without a semantic substitute.
- Activation or effect: code changes the messages sent to later invocations; accurate preservation of meaning and model compliance with summaries are unobserved.
- Evidence limits: estimator inputs omit some tool-schema cost in the channel warning; summaries can fail and leave only a failure marker; context reduction is not a hard proof of fitting every provider request.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // No tool server — the compactor's sole job is producing a summary.
> // Memory extraction is handled by persistence branches (Phase 5a).
> --- `src/agent/compactor.rs`

> format!("[Compaction summary of {remove_count} messages — LLM summarization failed]")
> --- `src/agent/compactor.rs`

> /// Drop live history without summarizing it, and record a checkpoint
> /// marking the discarded span.
> --- `src/agent/chronicle.rs`

The stack-frame analogy fits private branch/worker windows and selective returns, but copied turns are values, not followable references. A tool can explicitly retrieve durable material; an ID/index entry alone does not make removed content live in the model window. Chronicle expand capability is placed on eligible branches, which curate raw transcript into a conclusion for the channel, rather than injecting raw rows indiscriminately (SRC-1, `src/tools.rs`).

#### RT-RTE-skill-change
Label: Procedure reflection and skill mutation

Endpoints/progression: eligible channel persistence/reflection signal → memory-persistence branch with reflection profile → transcript inspection and model proposal → `skill_manage` create/patch/edit/support-file/delete → filesystem/provenance update → SkillSet reload → later index/body consumption. This route concerns instruction admission; memory revisions are separate. The model decides whether and what to retain. Code rejects invalid names/content/paths and disallowed origins/targets. Humans can pin/manage skills through other surfaces, but this automatic route does not require per-content human approval. Ordinary conversation branches use User origin, which is a runtime grant classification, not proof a human authored or approved the exact bytes (SRC-1, `src/agent/channel.rs`, `src/tools.rs`, `src/tools/skill_manage.rs`).

Guidance: the persistence prompt asks for reusable task-class procedures, prioritizes patching existing relevant skills, treats procedural correction and successful recovery as signals, and forbids retaining unresolved/transient failures as procedures. Mode is open retrospective work, not a controlled curriculum. No expected-answer oracle: transcripts, user corrections and worker outcomes are evidence offered to the model, not a reference solution automatically compared against the proposal. Rejection ability is model abstention plus structural/policy refusal, not a semantic test of procedural truth. Agent deletion archives; restore support exists. Patch/edit writes replace current content; a general automatic previous-version rollback was not established in the inspected mutation body (SRC-1, `prompts/en/memory_persistence.md.j2`, `src/tools/skill_manage.rs`, `src/skills.rs`).

- Immediate return: mutation success/refusal metadata and path; persistence branch completion is silent in ordinary channel history.
- Later read-back: reloaded skill metadata reaches later preambles; named `read_skill` supplies a bounded body; required skill lists inject full bodies into future worker preambles.
- Delegated visibility: reflection branch gets channel history and selected worker IDs; `worker_inspect` grants transcript access with a reflection-specific result cap, not an assumption of all raw execution context.
- Selection predicate: persistence enabled, message/time/event-density or reflection signal, reflection cooldown/configuration and profile origin; model chooses relevant procedures after index/transcript inspection.
- Invalidation or expiry: archived skills leave discovery; delete/replace/reload changes later content; origin/pin/installed-source checks may refuse an edit; no universal expiry of lessons is established here.
- Activation or effect: writes and subsequent instruction delivery are wired; actual behavioral dependence on a changed procedure and improved outcomes are unobserved.
- Evidence limits: procedural criticism and correct lessons are requested, not demonstrated; generic file/shell, installer, API and User-origin paths have different checks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> BranchToolProfile::Default => Some(crate::skills::WriteOrigin::User),
> --- `src/tools.rs`

> "'{}' is pinned; pinned skills are read-only for autonomous writers"
> --- `src/tools/skill_manage.rs`

> First decide whether anything is worth keeping. Ending with no skill writes is the common case and completely acceptable — but treat a session where the user corrected the agent's procedure as a strong write signal.
> --- `prompts/en/memory_persistence.md.j2`

> // When sandbox is disabled, skip workspace boundary enforcement.
> if !self.sandbox.mode_enabled() {
>     return Ok(canonical);
> }
> --- `src/tools/file.rs`

Theory-related assessment boundary: this route can retain a whole localized procedure and revised instructions, but no particular generated theory or content-directed criticism was supplied. Do not infer a theory-builder from the method's request to reflect. Under `theory-builder conditions 1–4`: condition 1 architectural conclusion status: afforded — whole procedure bodies can be formulated and replaced; particular theory content remains uninspected. Condition 2 operation conclusion status: uninspected — delivery is wired, content-dependent decisions are not observed. Condition 3 architectural conclusion status: claimed — the prompt requests evidence-directed procedural revision but does not enforce blame placement or demonstrate formulated criticism. Condition 4 operation conclusion status: uninspected — reload supports iteration but no retained criticism shaping a next round was supplied. Addressability: files and exact-string patches localize procedures and edits, without proving exposed assumptions or scope conditions in generated content. Persistence: filesystem skills can span sessions/problems and reach later workers. Learning: improved future capacity and attribution are uninspected; retained procedures alone do not establish them. Reflection: the implemented pathway can carry the system's own conversation/worker-operation records into a representation that changes later instructions; quality and exercise of both directions are unobserved. Autonomous theory builder and reflective theory builder are not established by those affordances.

Self-improvement assessment: bounded to Spacebot's skill instruction surface across sessions, with the objective of reusable procedures that avoid repeated procedural errors. The prompt defines that objective independently of any chosen edit. Evidence-to-proposal and instruction-write/reload paths are wired, but no supplied run establishes objective-bearing evidence causally determining a particular update (link 1), a particular accepted self-change (link 2), its live consumption beyond potential delivery (link 3), or behavior causally depending on it (link 4). This supports an improvement-directed self-change capacity, not exercised or successful self-improvement.

#### RT-RTE-capability-admission
Label: External skills and runtime configuration admission

Endpoints/progression: model tool request or administrative API request → GitHub skill installer or TOML editor → stored files/configuration → runtime reload → later prompts, model routes or tool capabilities. These paths are grouped as alternative admission mechanisms, not as one universal gate. `install_skill` can resolve another agent's runtime config, install to its workspace skills directory, reload SkillSet and record installed provenance. Configuration API uses a write mutex and validates resulting TOML before writing; factory config mutation shares the coordination but can report that written config failed to reload. MCP tool discovery/calls expand worker capabilities; its external effects are delegated to configured servers (SRC-1, `src/tools/install_skill.rs`, `src/skills/installer.rs`, `src/api/config.rs`, `src/tools/factory_update_config.rs`, `src/mcp.rs`, `src/tools.rs`).

Proposers/deciders: model supplies tool arguments, API caller supplies edits; runtime resolves targets, parses/validates, writes and reloads. Caller identity is not evidence that each edit had human review. API bearer enforcement is conditional on configured token; no token passes through. Registration of authority-sensitive tools and API authentication differ from behavioral validation. Mode is open administration/installation. No reference-outcome oracle or performance acceptance experiment was established. Trigger is an explicit install/config request; retained change is external skill content or runtime settings. Guidance is the tool/API contract, not an enforced improvement objective. Runtime can reject invalid requests or failed downloads/parses; repair/reinstall/config correction/restart are recovery options, not a demonstrated universal transactional rollback (SRC-1, `src/api/server.rs`, `src/tools/install_skill.rs`, `src/api/config.rs`, `src/tools/factory_update_config.rs`).

- Immediate return: installed names/success metadata, API result/error, or a reload warning after a successful disk write; MCP calls return remote tool results.
- Later read-back: changed skill collections supply later prompts; TOML persists across restart and hot reload changes live runtime settings when successful.
- Delegated visibility: external instruction bodies become visible through skill index/read/required injection; workers receive the MCP tools available at construction.
- Selection predicate: source spec, optional target agent, API agent/settings fields and configured MCP servers; exact GitHub install source uses repository main branch rather than a supplied immutable commit.
- Invalidation or expiry: skill removal/archive/reinstall, config replacement/reload/restart and MCP disconnection/tool-list refresh change the available surface; remote capability semantics remain external.
- Activation or effect: installer/reload, config writes and remote calls are wired; source availability, correctness and actual production effect were not observed.
- Evidence limits: not all API edits or factory tools were audited; authentication is not per-content approval, and none of these paths establishes beneficial successor selection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "https://github.com/{}/{}/archive/refs/heads/main.zip",
> --- `src/skills/installer.rs`

> let Some(expected_token) = state.auth_token.as_deref() else {
>     return next.run(request).await;
> };
> --- `src/api/server.rs`

> if let Err(error) = crate::config::Config::validate_toml(&updated_content) {
> --- `src/api/config.rs`

> "config written but failed to reload: {error} — changes take effect on restart"
> --- `src/tools/factory_update_config.rs`

### Claims

#### RT-CLM-role-grants
Label: Role-limited tools are not global containment

Claimed operation: ToolServer topology separates channel, branch and worker capabilities; executable factories implement different grants, but do not establish deployment-wide sandboxing or approval. SRC-1, `src/tools.rs`, `src/agent/channel.rs`, `src/sandbox.rs` supply implementation and comments. Scope: the offered tool list and tool-local path/wrapper checks, not control of every same-process API, extension, raw subprocess or remote server.

> .add_tool(ShellTool::new(workspace.clone(), sandbox.clone()))
> --- `src/tools.rs:758-776`

> "sandbox mode is enabled but no backend available — \
> processes will run unsandboxed"
> --- `src/sandbox.rs`

The second passage directly defeats an unconditional sandbox claim. Disabled mode also uses passthrough. Generic file tools can still enforce configured path checks when mode is enabled, even if a subprocess containment backend is unavailable; filesystem checks and OS process containment must not be conflated. Actual deployed isolation is uninspected.

#### RT-CLM-required-skills
Label: Required instruction delivery is not compliance

Claimed operation: task-required skills are delivered as complete bodies, rather than merely suggested index entries. Source is SRC-1, `src/agent/channel_dispatch.rs`, `src/skills.rs`; this is implementation plus a stated contract. Required names are validated upstream by task/spawn handling; the renderer itself warns and skips unresolved names. This limits any claim that the renderer alone guarantees complete delivery.

> /// Unlike the index rendered by [`Self::render_worker_skills`], this
> /// carries entire skill bodies — required skills are a contract the
> /// worker must receive, not a listing it may consult. Names that don't
> /// resolve are skipped with a warning; validation belongs to the caller.
> --- `src/skills.rs`

Named optional `read_skill` is bounded by the generic tool output byte cap, while direct required-body rendering follows another path. Neither path proves model obedience or efficacy (SRC-1, `src/tools/read_skill.rs`).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-instruction
Label: Retained skill to later process instructions

Consumer: later channel/branch/worker models. Channel: rendered available-skills metadata, named read tool results and required-body preamble injection. Force: natural-language guidance interpreted by the model; symbolic name selection and required-list handling are code-controlled, but instruction delivery is not enforced compliance. Horizon: later invocations and sessions while files remain discoverable and loaded. Update and downstream consumers are distinct: the reflection model decides a write; later work models receive the resulting procedure (SRC-1, `src/skills.rs`, `src/tools/read_skill.rs`, `src/agent/channel_dispatch.rs`; [RT-RTE-skill-change](#rt-rte-skill-change), [RT-CLM-required-skills](#rt-clm-required-skills)).

> sections.push(format!("### {}\n\n{}", skill.name, skill.content.trim()));
> --- `src/skills.rs`

#### RT-BAP-runtime-config
Label: Reloaded settings to runtime control

Consumer: Rust runtime model routing, tool factories and control loops. Channel: TOML parsing and RuntimeConfig reload/shared live configuration. Force: symbolic code rules determine model routes, autonomy level and tool/context settings; prompts may separately represent those settings. Horizon: subsequent live operations after successful reload and later restarts from saved config. Disk persistence and successful hot reload are separate events, as the factory warning shows. No measured improvement is inferred (SRC-1, `src/api/config.rs`, `src/tools/factory_update_config.rs`, `src/agent/channel.rs`, `src/agent/autonomy.rs`; [RT-RTE-capability-admission](#rt-rte-capability-admission)).

> .reload_config(&new_config, &agent_id, &mcp_manager)
> --- `src/tools/factory_update_config.rs`

## Annotations

none
