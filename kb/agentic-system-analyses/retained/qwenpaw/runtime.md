---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "QwenPaw runtime baseline: native request orchestration, tool governance, delegated work, alternative harnesses and capability admission at the frozen commit."
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
reviewed-boundary: "16b2e712d198166c9359e77055b13bf2668bf5ae"
---

# QwenPaw runtime report

## Runtime account

### Boundary, claimed work and evidence

QwenPaw assembles a personal assistant around model inference, tools, editable workspace instructions and persistent sessions. Its shipped application also initiates scheduled work and delegates to other agent runtimes. The README promises cross-channel access, extensibility, memory and security; these are product claims, not observations ([RT-CLM-assistant-work](#rt-clm-assistant-work), [RT-CLM-security-built](#rt-clm-security-built)). This account uses SRC-1 at the revision fixed in [the boundary](boundary.md). All new source inspection below is implementation evidence except README claims, which are doctrine/design. No target execution, service call, test result or independent trace was supplied. Every operation conclusion remains uninspected; wiring does not establish successful activation, isolation or benefit.

The ordinary path is a console chat into the native backend. Three forcing families challenge generalizations from that path: cancellation/disconnection and context pressure; a change of backend to Codex/Qoder; and forked subagent work plus in-process plugin loading. Tool-policy checks are inspected within these routes, including OFF settings and missing sandbox support. These cases are sufficient to reject universal claims about persistence or sandbox coverage, not an exhaustive security audit.

### Ordinary request and result

The boundary establishes the package CLI, Uvicorn application and workspace bootstrap. The console handler resolves the selected workspace and console channel, registers a chat, supplies effective project-directory context and attaches to or starts a tracked task. It streams a queue rather than binding the agent's lifetime to the HTTP reader. A reconnect attaches to an existing task; if none remains it returns an empty SSE stream so the UI can use persisted history. Thus an HTTP disconnect is not the same operation as stopping the agent (SRC-1, `src/qwenpaw/app/routers/console.py`).

Workspace dispatch selects `config.backend`. Native requests go through `Runtime.run`; other values bypass that lifecycle for `HarnessRuntime.stream`. In the native path, dictionary input becomes an `AgentRequest`; missing session IDs get a UUID, and missing user IDs inherit the session ID. The runtime constructs a context carrying agent, session, root-agent and root-session identities, workspace, services and converted input messages. These are routing and persistence identities, not by themselves authentication or tenant-isolation proofs (SRC-1, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/runtime/runtime.py`).

The runtime owns next-step sequencing: pre-dispatch hooks, slash-command dispatch, post-dispatch hooks, pre-build hooks, agent construction, mode start, post-build hooks, pre-execution hooks, execution, post-response hooks and envelope finalization. Hooks can short-circuit or skip agent execution. A slash command can return a message without a model call. Dynamic context injections are priority-sorted and prepended as a message; importantly, executable code constructs that message with `role="user"`, despite the helper's description calling it a system hint. Symbolic orchestration and natural-language model input are separate mechanisms (SRC-1, `src/qwenpaw/runtime/runtime.py`).

The builder loads agent configuration; validates an active provider/model; resolves channel-effective skills and optional subagent restrictions; starts a governor; gathers workspace, memory, driver and mode tools; builds a model/formatter; selects native or scroll context management; composes the system prompt; installs middleware; constructs `QwenPawAgent`; and restores loaded session state. The native agent inherits the ReAct implementation from AgentScope. QwenPaw supplies a configurable iteration limit and wraps compression, state serialization, provider recovery and tool handling; the external dependency owns the inner reasoning/action algorithm. Therefore the analysis does not attribute an independently inspected full ReAct implementation to QwenPaw (SRC-1, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/agents/react_agent.py`).

Inference uses the distributed-parametric component [RT-CMP-active-model](#rt-cmp-active-model). Model output supplies answer text and proposed tool calls; configured toolkit and permission rules decide what can execute. The executor drives `reply_stream`, wraps idle periods with heartbeats and translates events through the envelope to SSE. Terminal success consists of post-response hooks and finalized message/response events, not a separate truth or quality verdict. [RT-RTE-native-turn](#rt-rte-native-turn) records the route and its lack of an answer oracle.

Session load before construction and save after response connect separate invocations through [RT-OBJ-session-state](#rt-obj-session-state). ACP ephemeral requests deliberately skip these normal hooks. Normal save errors are logged rather than propagated. The storage layer uses path locks and an atomic JSON writer, but those mechanisms do not make the entire response-to-save lifecycle transactional (SRC-1, `src/qwenpaw/hooks/session/session_hook.py`, `src/qwenpaw/app/chats/session.py`). The memory specialist owns knowledge-maintenance and memory-revision findings; this account establishes the session consumer and context controls, not the quality of memory extraction.

Scheduled tasks are another principal: configured cron work calls the same workspace stream and sends events to a target channel. Silent dispatch consumes without delivery; final-only dispatch retains the completed message before sending it. A missing completed message is explicitly logged. ACP constructs an `AgentRequest` and translates workspace events into protocol updates. These are shipped callers of the same dispatch boundary, not excluded hosts (SRC-1, `src/qwenpaw/app/crons/executor.py`, `src/qwenpaw/agents/acp/server.py`; initial ACP evidence is also in the boundary). Detailed channel-account authorization and cron state restoration remain outside this bounded trace.

### Tools, grants and enforcement

The capability surface is broader than the grant set. `QwenPawLocalWorkspace.list_tools` filters tool descriptors by configuration, modes, skills and features. A subagent list intersects permitted tools; the builder repeats a final whitelist pass over workspace, extra and memory tools. Empty subagent lists mean deny all; a missing/non-list whitelist means inherit. These are symbolic toolkit restrictions on exposed tool identities, not a proof that a granted shell cannot perform equivalent work (SRC-1, `src/qwenpaw/app/workspace/local_workspace.py`, `src/qwenpaw/runtime/builder.py`).

Workspace tools are wrapped in `PolicyGuardedTool`. The pre-execution method builds a tool/target/agent/session call specification, asks the governor for a decision, audits it and maps it to AgentScope permission results. ASK delegates veto to a user through the approval service. The wrapper can supply sandbox configuration; a sandbox violation can ask for approval and retry without sandbox. The load-bearing scope is [RT-RTE-tool-governance](#rt-rte-tool-governance), not every executable operation in the process (SRC-1, `src/qwenpaw/governance/tool_adapter.py`).

The current grant set and deployed isolation envelope are not supplied. Session approval settings override agent defaults. OFF can allow all calls before ordinary policy evaluation; special F1 session mode overrides that setting to STRICT in this wrapper. More consequentially, the governor implementation converts sandbox fallback to unsandboxed ALLOW when sandbox support is unavailable or globally disabled. Its docstring says escalation to ASK, but the executable branch says otherwise. The shell function also executes directly when it receives no valid sandbox configuration. These are implemented counterexamples to interpreting “Security built in” as invariant confinement (SRC-1, `src/qwenpaw/governance/tool_adapter.py`, `src/qwenpaw/governance/resource_governor.py`, `src/qwenpaw/agents/tools/shell.py`).

For the native wrapper, the owner is the governor/permission integration; the enforcement point is the wrapped tool's permission check, with sandboxing at execution. Guarantee strength is **policy**, not a deployment guarantee. Covered paths are tools actually routed through that wrapper and the external permission engine. Alternate paths include fallback `GuardedFunctionTool`, driver capability implementations, shell subprocess actions, installed plugin startup code and provider-native harness tools. The fallback guard has explicit bypass/OFF branches too. AgentScope must invoke the permission method and honor its result; the OS sandbox must enforce the compiled configuration when used. Neither external contract was observed here. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `src/qwenpaw/runtime/tool_guard.py`, `src/qwenpaw/governance/tool_adapter.py`, `src/qwenpaw/runtime/builder.py`).

### Recovery and working-context controls

Cancellation runs error hooks, attempts a shielded session save, emits cancellation completion and re-raises. It injects partial streaming output and interrupted tool results into agent state before snapshotting. Finalization closes the agent and runs FINALLY hooks. A second cancellation may skip error hooks; the hardcoded save remains best effort. Normal POST_RESPONSE hooks, including mode/plugin state handling, are not all reproduced on cancellation. The cancellation save shown does not add `mode_state` as the normal save hook does. The owner is `Runtime`; the enforcement point is `_try_save_on_cancel`; guarantee strength is **best effort**; coverage is native cancellation/error paths reaching it, not crashes or the separate harness lifecycle. Required external contracts are scheduler/shield behavior and filesystem write completion. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `src/qwenpaw/runtime/runtime.py`, `src/qwenpaw/hooks/session/session_hook.py`).

Context management is not just accumulating turns. The agent sanitizes tool-message structure before compression and dispatches compression through AgentScope middleware to an injected manager or the native implementation. Scroll persists live content before eviction, counts prepared-input tokens and preferentially folds recoverable completed-turn tool outputs before evicting older dialogue. It keeps a recent raw tail, an eviction index and recovery pointers; compact task state is requested from bounded input. Persistence failure prevents eviction, and an unfit window can raise rather than silently discard undurable text. The builder falls back to native management when scroll recall cannot be wired conservatively; the Python recall REPL has a separate sandbox-availability gate from structured recall. These controls are owned partly by code selection/thresholds and partly by model summarization; this report does not treat their output as lossless semantic memory (SRC-1, `src/qwenpaw/agents/react_agent.py`, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/runtime/builder.py`).

A provider context-overflow error can trigger one recovery, followed by rebuilding prepared messages from changed agent state and calling the superclass directly. A second overflow propagates instead of recursing. The recovery route is [RT-RTE-context-recovery](#rt-rte-context-recovery). It prevents a stale pre-compaction message list from being reused on that retry, conditional on the inspected method being reached; it does not guarantee the new request fits or succeeds. Detailed summary prompts, pruning/visual-compression algorithms, all recall selectors and external native compaction remain unresolved here and should not be inferred from route names.

### Alternative execution and change admission

[RT-RTE-harness-turn](#rt-rte-harness-turn) crosses an actual runtime boundary. Codex/Qoder own inner next-step decisions and provider-native tools; QwenPaw projects capabilities, translates events, bridges sessions and mediates approval callbacks. Codex starts/resumes persisted thread IDs, defaulting new threads to workspace-write and on-request approval. Qoder supplies a `can_use_tool` callback but also accepts bypass/yolo permission modes. Settings can be overlaid per request. Native `PolicyGuardedTool` guarantees therefore cannot be extended to these paths. QwenPaw's callback mapping is inspectable; completeness of callback emission and isolation inside the third-party runtimes is not (SRC-1, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/harnesses/runtime.py`, `src/qwenpaw/harnesses/codex/adapter.py`, `src/qwenpaw/harnesses/qoder/adapter.py`).

[RT-RTE-fork-worker](#rt-rte-fork-worker) delegates a task to a forked session and, when available, a Git worktree. The foreground agent proposes work through the tool; code builds child routing and filters, optionally chooses the configured subagent model, registers the fork and binds background tasks when a task ID is returned. Foreground collection awaits administrative finalization before advertising a branch; background submission advertises the branch immediately when a worktree exists, without awaiting finalization. Task-completion hooks, polling and a separately scheduled watchdog can subsequently finalize background work. Return is text or a task handle, not unrestricted streaming of the child window. The inherited snapshot and selected task constitute a separate context; parent context receives the result/handle and, under these different conditions, a branch marker. A background marker alone certifies neither finalization nor merge readiness; even successful administrative finalization does not verify task quality. The worktree remains for merge, so task completion is not automatic admission to the parent's project. Full fork snapshot contents and merge enforcement are uninspected; no claim of a clean-room child or mandatory human merge approval is made (SRC-1, `src/qwenpaw/agents/tools/agent_management.py`).

Two distinct behavior-changing admission paths are established here. [RT-RTE-workspace-instruction](#rt-rte-workspace-instruction) accepts caller-supplied Markdown into workspace files; configured prompt contributors later consume selected bodies. [RT-RTE-plugin-install](#rt-rte-plugin-install) copies a local/remote plugin into an installation tree, installs dependencies and executes its backend registration in the application process. Neither path is a model-training route. Plugin import happens before individual tool permission checks, so it is also a materially different execution path. Human content approval is unresolved for generic API callers; initiating an install is not evidence of reviewing every executable unit. Recovery differs: Markdown can be overwritten; plugin uninstall cleans registrations and files, but this does not establish rollback of arbitrary prior side effects (SRC-1, `src/qwenpaw/app/routers/workspace.py`, `src/qwenpaw/agents/memory/agent_md_manager.py`, `src/qwenpaw/runtime/prompt_contributors.py`, `src/qwenpaw/app/routers/plugins.py`, `src/qwenpaw/plugins/loader.py`).

Skills, MCP servers, driver capabilities, custom loop modes and product/deployment updates are additional included surfaces, not proved absent. The builder establishes runtime skill-directory resolution and loading, workspace-over-bound-skill precedence, middleware factories and driver tools; workspace bootstrap attempts custom-loop loading. Search located scanner error handling, snapshots/restoration and hub-install APIs in `src/qwenpaw/app/routers/skills.py`, but their full admission pipeline was not traced. The plugin loader demonstrates dependency installation, not the safety of installed packages. These limits prevent a universal capability-admission, self-modification or production-release account. Bundled mail MCP operations, marketplace payloads, provider internals, all plugin examples and backup/release automation remain uninspected at runtime detail. No missing run evidence is used to infer an absent implementation (SRC-1, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/app/routers/skills.py`, `src/qwenpaw/plugins/loader.py`; included surface inventory in the boundary).

### Added source coverage

Beyond the boundary's initial excerpts, this member inspected the console tracked-task caller; native orchestration and identity/recovery code; builder toolkit/model/prompt/context integration; local workspace filtering; executor; session persistence; tool-policy adapter, fallback guard and governor sandbox-degradation branch; shell sandbox/direct split; model factory and fallback dispatch; scroll pressure control; fork-worker dispatch/finalization; alternative harness dispatch, Codex thread/approval mapping and Qoder options/approval callback; workspace Markdown write API and manager; prompt-file reader; plugin install/import/compatibility/dependency/uninstall entry points; README product claims. These are all SRC-1 at the frozen commit, not new sources. Newly inspected paths appear in the records and account above. Searches of missing guessed paths returned errors and supplied no negative evidence. No absence record is declared.

## Shared records

### Components

#### RT-CMP-active-model
Label: Active model and optional fallback models

Source-native identity: `active_model`, provider/model slots and optional `fallback_models`. Representational form: distributed-parametric inference parameters, behind symbolic provider configuration and API requests. Storage substrate: external provider service or configured local engine; exact weight storage is outside inspected adapters. QwenPaw constructs instances using provider/model configuration and wraps them with token recording, retry and optional ordered fallback. Parameters changing during operation: uninspected — no provider-internal evidence or weight-update trace. Exact version pinned: not established; model-name configuration is not an immutable weight identity. Mutable endpoint resolving to another model: possible and not excluded by the integration; explicit fallback can also switch model/provider within a request. Distinct backend-owned model selection is [RT-CMP-harness-model](#rt-cmp-harness-model), not this factory instance.

SRC-1, `src/qwenpaw/agents/model_factory.py`, `src/qwenpaw/providers/fallback_chat_model.py` (implementation).

> model = provider.get_chat_model_instance(model_slot.model)
> --- `src/qwenpaw/agents/model_factory.py`

> if emitted or not self._can_try_next(current_index, exc):
>     raise
> --- `src/qwenpaw/providers/fallback_chat_model.py`

Fallback therefore is not a guarantee that a partially emitted response will be silently restarted on another model. Improvement or provider training is unobserved.

#### RT-CMP-harness-model
Label: Model selected by third-party harness

Source-native identity: Codex/Qoder adapter `settings["model"]`. Representational form: distributed-parametric inference behind external agent runtimes. Storage substrate: provider/SDK-managed model service, not inspected weights. Parameters changing during operation: uninspected — adapters expose settings, not training internals. Exact version pinned: unestablished; the setting may be absent or a mutable model name. Mutable endpoint resolving to another model: unresolved in the external runtime; settings explicitly permit model selection. This is distinct from [RT-CMP-active-model](#rt-cmp-active-model): workspace dispatch bypasses the native factory on this path. SRC-1, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/harnesses/codex/adapter.py`, `src/qwenpaw/harnesses/qoder/adapter.py` (implementation).

> if settings.get("model"):
>     params["model"] = settings["model"]
> --- `src/qwenpaw/harnesses/codex/adapter.py:497-498`

### Operative objects

#### RT-OBJ-session-state
Label: Serialized session agent state

Source-native identity: `ctx.session_state` and saved `agent` state. Representational form: symbolic JSON serialization of agent state and mode state; text-bearing message content is natural language when interpreted by later inference, not an executable policy merely because serialized. Storage substrate: `sessions` directory through `SafeJSONSession`, with names derived from session/user/channel. Load/save hooks use a state proxy; the builder restores into a newly assembled agent. Normal hooks skip ACP ephemeral requests and tolerate load/save failure. SRC-1, `src/qwenpaw/hooks/session/session_hook.py`, `src/qwenpaw/app/chats/session.py`, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/runtime/builder.py` (implementation).

> if ctx.session_state:
>     agent.load_state_dict(ctx.session_state)
> --- `src/qwenpaw/runtime/builder.py`

> proxy.data = ctx.agent.state_dict()
> proxy.data["mode_state"] = ctx.mode_state
> --- `src/qwenpaw/hooks/session/session_hook.py`

#### RT-OBJ-prompt-files
Label: Configured workspace prompt files

Source-native identity: `system_prompt_files`, historically `AGENTS.md`, `SOUL.md`, `PROFILE.md`. Representational form: natural-language bodies, selected by symbolic configuration. Storage substrate: workspace Markdown files read through a file snapshot cache. Reader resolves within workspace, skips missing/empty files and strips frontmatter; helpers process marked heartbeat/memory sections. Empty configured list disables workspace prompt files. These are not the session snapshots in [RT-OBJ-session-state](#rt-obj-session-state). SRC-1, `src/qwenpaw/runtime/prompt_contributors.py`, `src/qwenpaw/runtime/builder.py` (implementation).

> DEFAULT_SYSTEM_PROMPT_FILES = ("AGENTS.md", "SOUL.md", "PROFILE.md")
> --- `src/qwenpaw/runtime/prompt_contributors.py`

> if content.startswith("---"):
>     parts = content.split("---", 2)
>     if len(parts) >= 3:
>         content = parts[2].strip()
> --- `src/qwenpaw/runtime/prompt_contributors.py`

### Routes

#### RT-RTE-native-turn
Label: Native request to streamed reply

Endpoints and progression: console/channel/cron/ACP request → workspace native dispatch → lifecycle hooks and slash commands → builder → AgentScope-backed reply stream → SSE envelope → post-response state save. Runtime owns sequencing; model proposes reply/actions; wrapped tool and approval policy own permission decisions. Context includes current inputs, assembled system prompt, hooks' injections and reloaded session. Tools can affect the host workspace and external services; output is not confined to text. SRC-1, `src/qwenpaw/runtime/runtime.py`, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/runtime/executor.py`, `src/qwenpaw/hooks/session/session_hook.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed envelopes with reasoning, text/tool events and final response status; slash commands/hooks may answer without inference.
- Later read-back: session snapshot can reload prior context and mode state on a later native invocation; ACP ephemeral requests skip normal persistence.
- Delegated visibility: tool results return into the native agent; explicit child work is separately bounded in [RT-RTE-fork-worker](#rt-rte-fork-worker).
- Selection predicate: workspace backend equals qwenpaw; hooks and command dispatch decide whether construction/execution occurs.
- Invalidation or expiry: session replacement/reset semantics and all retention policies uninspected; a new request rebuilds the agent from current config and selected state.
- Activation or effect: code wires inference, permission-mediated actions, streaming and save; actual model compliance and successful effects unobserved.
- Evidence limits: inner AgentScope ReAct and deployed accounts/services are external to inspected implementation; no observed end-to-end invocation.

Decision roles: caller supplies request; model proposes response/actions; code and optional human approval decide permitted execution. Answer oracle: none supplied by this open-request path; model judgment is not an expected-answer reference. Operating mode: open interactive or configured scheduled requests, not a bounded improvement experiment. Persistent knowledge revision belongs to the memory report.

> async for ev in executor.run(ctx.input_msgs):
>     yield ev
> --- `src/qwenpaw/runtime/runtime.py`

#### RT-RTE-tool-governance
Label: Native tool permission and execution

Endpoints and owner: filtered workspace descriptor → `PolicyGuardedTool.check_permissions` → governor → ALLOW/DENY/ASK/sandbox → FunctionTool execution, optionally approval and unsandboxed retry after violation. Code proposes policy decisions over model-proposed calls; user may veto ASK. Owner is the governor integration, with external AgentScope permission enforcement. SRC-1, `src/qwenpaw/app/workspace/local_workspace.py`, `src/qwenpaw/governance/tool_adapter.py`, `src/qwenpaw/governance/resource_governor.py`, `src/qwenpaw/agents/tools/shell.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: permission result, tool output or denial, including explanatory text delivered back to the model.
- Later read-back: governor auditing/policy persistence is invoked by integration; exact policy generalization/reuse semantics uninspected here.
- Delegated visibility: approvals carry agent/session ownership; harness-native tools use separate callbacks, not this same guard.
- Selection predicate: tools registered through the wrapper; request approval level overrides agent default; OFF bypass and F1 STRICT override alter decisions.
- Invalidation or expiry: invocation fields are reset for OFF sandbox preparation; approval persistence scopes and all policy lifetimes uninspected.
- Activation or effect: wired policy decision can deny or execute actions; sandbox configuration is conditional, and user approval can authorize unsandboxed retry.
- Evidence limits: dependency permission-engine calls and deployed sandbox enforcement unobserved; tool-name filtering does not constrain equivalent shell operations.

Guarantee owner: governor plus permission integration. Enforcement point: wrapper permission method and sandbox-capable executor. Guarantee strength: policy. External contract: permission consumer honors DENY/ASK; platform enforces sandbox config. Covered path: wrapped calls; alternates: fallback guard, shell host execution, plugin startup, harness tools and driver implementations. Admission concerns action permission, not correctness of a proposed product change. Answer oracle: none; user approval is permission, not an expected-answer test. Operating mode: open requests under configurable execution policy. Recovery: deny on unavailable governor except explicit OFF paths; ask/retry after sandbox violation. This is not invariant confinement.

> if effective_level is not None and effective_level.is_disabled():
> --- `src/qwenpaw/governance/tool_adapter.py`

> message="governance: approval_level=off, all tools allowed.",
> --- `src/qwenpaw/governance/tool_adapter.py`

> if (
>     decision.action is GovernanceAction.SANDBOX_FALLBACK
>     and not self._sandbox_usable()
> ):
> --- `src/qwenpaw/governance/resource_governor.py`

> decision = GovernanceDecision(
>     action=GovernanceAction.ALLOW,
>     reason=f"{reason}, running unsandboxed",
> )
> --- `src/qwenpaw/governance/resource_governor.py`

#### RT-RTE-context-recovery
Label: Context pressure and overflow recovery

Endpoints: prepared model context → scroll/native compression selection → updated context → rebuilt provider retry. QwenPaw owns dispatch and one overflow retry; the injected scroll manager owns write-through/pressure controls, while external AgentScope owns native compaction. Context and symbolic recovery pointers change; no parameter update is established. SRC-1, `src/qwenpaw/agents/react_agent.py`, `src/qwenpaw/agents/context/scroll/manager.py`, `src/qwenpaw/runtime/builder.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: changed working context or propagated overflow/unfit error; a successful compression is not itself a user answer.
- Later read-back: scroll's persisted history and recovery tools can make removed material available again; session snapshots can carry resulting context to another invocation.
- Delegated visibility: inapplicable — this control transforms the current agent's context, not a worker handoff.
- Selection predicate: configured strategy and token thresholds; provider overflow forces recovery only for a compatible manager and recognized error.
- Invalidation or expiry: old prepared input is discarded after successful recovery; exact history expiry is uninspected.
- Activation or effect: code removes/folds context and rebuilds input; summary accuracy, recall success and downstream behavior change unobserved.
- Evidence limits: scroll summary/model internals, all visual/pruning controls and dependency-native compaction not fully traced.

This is working-window management with reachable archived content, not proof of improved reasoning. The frame analogy is limited: content is copied back by retrieval rather than followed as an automatically live reference. Trigger/retention policy is code-directed; compact task-state generation is model-dependent. No diagnosis against a reference answer or candidate improvement contest is established.

> if not await self._persist_guarded_async(agent):
> --- `src/qwenpaw/agents/context/scroll/manager.py`

> refreshed = await self._prepare_model_input()
> refreshed_messages = refreshed["messages"]
> refreshed_tools = refreshed.get("tools", [])
> --- `src/qwenpaw/agents/react_agent.py`

#### RT-RTE-harness-turn
Label: Alternative backend turn and approval bridge

Endpoints: non-native workspace backend → capability resolver → adapter → external runtime turn/session → translated QwenPaw events and session bridge. Workspace/HarnessRuntime own outer scheduling; Codex or Qoder owns inner reasoning/actions. SRC-1, `src/qwenpaw/app/workspace/workspace.py`, `src/qwenpaw/harnesses/runtime.py`, `src/qwenpaw/harnesses/codex/adapter.py`, `src/qwenpaw/harnesses/qoder/adapter.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: translated text/reasoning/tool/completion events or backend error/cancellation.
- Later read-back: Codex saves session-to-thread mappings and resumes threads; outer harness has a session bridge. External context retention semantics uninspected.
- Delegated visibility: provider-native tool activity can be projected as events; approval requests enter QwenPaw's service when the backend emits the supported callback.
- Selection predicate: agent backend is not qwenpaw; backend controls merge into persisted settings; command support is checked against provider capabilities.
- Invalidation or expiry: new/clear resets adapter session; changed adapter configuration can stop/recreate adapters; failed Codex resume removes stale thread mapping.
- Activation or effect: external harness executes tools under its own settings and callback contract; native guard coverage is not inherited.
- Evidence limits: installed CLI/SDK versions, actual approval callback completeness, provider-native tools and isolation are unobserved.

Admission/decision roles: model/backend proposes actions; QwenPaw routes supported approval requests to a user and maps approval to backend decisions; backend permission modes can bypass asking. Answer oracle: none. Operating mode: open requests plus supported commands. Recovery: errors become response status; cancellation and reset use the adapter lifecycle. Model mutability belongs to [RT-CMP-harness-model](#rt-cmp-harness-model).

> allow_dangerously_skip_permissions=permission_mode
> in {"bypassPermissions", "yolo"},
> --- `src/qwenpaw/harnesses/qoder/adapter.py`

> "approvalPolicy": (
>     settings.get("approval_policy") or "on-request"
> ),
> --- `src/qwenpaw/harnesses/codex/adapter.py`

#### RT-RTE-fork-worker
Label: Forked subagent task and retained branch

Endpoints: foreground `spawn_subagent` fork path → fork API → registered session/worktree → filtered child request → foreground collection → awaited finalization → conditional branch marker, or background submission → immediate branch marker with separate later finalization. Owner is agent-management code and task service; child model owns internal next steps. SRC-1, `src/qwenpaw/agents/tools/agent_management.py`, `src/qwenpaw/runtime/builder.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: foreground result text includes a branch marker only after successful administrative finalization, otherwise a finalization-failure marker when a response and worktree exist. Background submission returns task/session information and a branch marker whenever a worktree exists, without awaiting finalization; that marker does not establish finalization or merge readiness.
- Later read-back: worktree/branch remains for later merge; task registry/polling reconnects background work. Full forked-session retention semantics uninspected.
- Delegated visibility: task plus forked session state/project path reach the child; parent sees result/handle and branch marker, not the child's whole evolving window.
- Selection predicate: spawn fork path and available fork result; optional allowed_tools and skills enter child request context; configured subagent model can override inference.
- Invalidation or expiry: registration failure aborts; foreground absent response or failed finalization marks failure. The background watchdog marks failure on a non-completed terminal task or timeout and invokes finalization on a completed task; worktree/task-ID availability controls its scheduling. Worktrees are retained, not automatically removed by either dispatch path.
- Activation or effect: code can create isolated project work and return changes for merge; no evidence that a particular task ran or a branch was admitted.
- Evidence limits: fork API snapshot details, merge gate implementation and external child success are uninspected.

Change admission: task caller/model proposes project work and injected worker protocol asks for commits. Only foreground branch advertising is gated on the finalizer's Boolean success; background advertising occurs at submission, before separate completion/finalization. When a background task ID and worktree exist, dispatch awaits task binding and schedules a watchdog, not completion or finalization. The administrative finalizer's lock, registry/scope checks and commit protocol remain the distinct subroute described by the supplied workflow finding; the background marker bypasses no such checks when finalization is later invoked. Neither marker nor administrative finalization verifies task quality, and a subsequent controller merge is still needed. No mandatory human content approval or answer oracle is established. Operating mode: open delegated tasks, not a controlled improvement curriculum. Rejection/recovery: abort failed registration; mark foreground no-response, failed finalization, background task failure or watchdog timeout as failed; retain worktree for examination. Guidance and persistence: commit protocol is added to the task; resulting commits/branch are the retained product, not proof of self-improvement.

> if worktree_path and FORK_WORKER_COMMIT_PROTOCOL not in task:
>     worker_task = f"{FORK_WORKER_COMMIT_PROTOCOL}\n\n{task}"
> --- `src/qwenpaw/agents/tools/agent_management.py`

> if worktree_path and finalize_ok:
>     result_text += (
>         f"\n\n[FORK_BRANCH: {worktree_branch}]"
> --- `src/qwenpaw/agents/tools/agent_management.py`

The separate background submission branch is implementation evidence against a route-wide finalization certificate:

> submission_text += (
>     f"\n\n[FORK_BRANCH: {worktree_branch}]"
>     "\nWorktree cleanup is not automatic in "
>     "background mode."
> )
> return _tool_text_response(submission_text)
> --- `src/qwenpaw/agents/tools/agent_management.py`

> if result.get("status") == "completed":
>     await asyncio.to_thread(
>         finalize_fork_worktree_or_fail,
> --- `src/qwenpaw/agents/tools/agent_management.py`

#### RT-RTE-workspace-instruction
Label: Workspace instruction write and later prompt load

Endpoints: workspace file PUT → `AgentMdManager.write_working_md` → Markdown file → configured prompt-file reader → later agent construction. Owner is API/file manager for admission, prompt contributors/builder for consumption. SRC-1, `src/qwenpaw/app/routers/workspace.py`, `src/qwenpaw/agents/memory/agent_md_manager.py`, `src/qwenpaw/runtime/prompt_contributors.py`, `src/qwenpaw/runtime/builder.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: written acknowledgement or HTTP error; no model validation of file contents in this route.
- Later read-back: configured prompt files can supply edited bodies to future agent system prompts after reader transformations.
- Delegated visibility: uninspected — backend/child projection of every edited prompt file was not traced.
- Selection predicate: selected workspace plus sanitized Markdown filename on write; configured prompt list and file availability select later inclusion, not arbitrary file presence.
- Invalidation or expiry: later writes replace content; empty prompt list disables workspace file loading; no content expiry established.
- Activation or effect: delivered system-prompt content can shape future inference; actual compliance with a particular edit unobserved.
- Evidence limits: generic caller does not establish human authorship or per-content human approval; filesystem guards do not establish semantic correctness.

Trigger/proposal: API caller submits replacement content. Admission/rejection: software normalizes filename and checks resolved directory containment; no expected-answer gate appears in the inspected write. Human contributions: unresolved beyond the possibility of direct operator editing. Operating mode: open editing, not automatic experimental successor selection. Answer oracle: none in this route. Guidance: caller-supplied prose, not an enforced revision protocol. Persistence: Markdown content until overwritten/deleted; rollback by rewriting is afforded, not a versioned undo guarantee. This route changes instructions rather than model parameters; it establishes no learning benefit or exercised self-improvement.

> workspace_manager.write_working_md(md_name, body.content)
> return {"written": True}
> --- `src/qwenpaw/app/routers/workspace.py`

> self._assert_within_dir(file_path, self.working_dir)
> file_path.write_text(content, encoding="utf-8")
> --- `src/qwenpaw/agents/memory/agent_md_manager.py`

#### RT-RTE-plugin-install
Label: Plugin install and backend registration

Endpoints: install API local path/remote ZIP → lifecycle-locked install → copied tree/dependencies → compatibility/entry-point checks → backend import and `register(api)` → runtime integration. Owner is plugin loader/API; plugin code supplies registration and can execute at import. SRC-1, `src/qwenpaw/app/routers/plugins.py`, `src/qwenpaw/plugins/loader.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: plugin metadata/loaded acknowledgement or mapped HTTP error; install integration registers providers/commands and startup hooks and syncs tools.
- Later read-back: installed plugin tree and dependencies remain for runtime loading; registrations affect subsequent capability construction.
- Delegated visibility: plugin executes in the application process; no separate worker context or OS isolation is established by namespace isolation.
- Selection predicate: caller-selected source and manifest; duplicate/force lifecycle, version compatibility and entry-point availability constrain admission.
- Invalidation or expiry: unload/uninstall removes registrations and optionally files; force reinstall unloads then replaces; no expiry established.
- Activation or effect: loader executes backend module and registration code, enabling runtime capabilities; deployed installation and downstream use unobserved.
- Evidence limits: payload trust, dependency safety, API authorization and reversal of arbitrary import/startup effects are not established.

Trigger/proposal: caller supplies local directory, URL or upload. Code decides structural installation and compatibility; no model or answer oracle judges behavioral quality. Human per-content review/veto is unresolved for generic callers. Operating mode: open extension installation. Guidance: manifest/version/entry rules shape admission, not a theory-criticism loop. Persistence: copied plugin code, dependencies and registrations. Rejection: invalid paths, conflicts or failed load; incompatible version yields disabled diagnostic record. Recovery: failed import cleanup and uninstall/force replacement; neither is a process-level transaction undoing arbitrary code side effects. This admits capability and production-process changes before individual native tool guards run.

> spec.loader.exec_module(module)
> --- `src/qwenpaw/plugins/loader.py`

> result = plugin_def.register(api)
> if inspect.iscoroutine(result) or inspect.isawaitable(result):
>     await result
> --- `src/qwenpaw/plugins/loader.py`

### Claims

#### RT-CLM-assistant-work
Label: Extensible personal assistant

Claimed operation: local/cloud personal assistant, skills/plugins and cross-channel access. Source: SRC-1, `README.md` (doctrine/design). The inspected request and extension paths support implemented capacity, not achieved task quality.

> Your personal AI assistant — deploy locally or in the cloud, extend with Skills & Plugins, connect across every channel.
> --- `README.md`

#### RT-CLM-security-built
Label: Security built in

Claimed operation: sandbox/guard/scanner/access-policy protection before dangerous commands run. Source: SRC-1, `README.md` (doctrine/design). [RT-RTE-tool-governance](#rt-rte-tool-governance) qualifies this against OFF, unavailable sandbox and approved unsandboxed execution; [RT-RTE-harness-turn](#rt-rte-harness-turn) uses another enforcement contract. This claim is not evidence of a uniform guarantee.

> Kernel-level Sandbox, Tool Guard, File Guard, Skill Scanner, and Access Policy. Dangerous commands are blocked before they run.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-workspace-prompt
Label: Workspace file to system prompt

Consumer: native model via `QwenPawAgent` construction. Channel: selected Markdown bodies transformed by prompt contributors and composed as `system_prompt`. Force: natural-language instruction supplied at the system-prompt surface; delivery is not compliance. Horizon: future native invocations while content/config remains selected. The write path and limits are [RT-RTE-workspace-instruction](#rt-rte-workspace-instruction), object [RT-OBJ-prompt-files](#rt-obj-prompt-files). SRC-1, `src/qwenpaw/runtime/builder.py`, `src/qwenpaw/runtime/prompt_contributors.py` (implementation).

> system_prompt=sys_prompt,
> --- `src/qwenpaw/runtime/builder.py`

#### RT-BAP-plugin-backend
Label: Installed plugin to application behavior

Consumer: Python application and its plugin registries. Channel: module import followed by `register(api)`, providers/tools/commands/startup integration. Force: executable symbolic code, not just advice to the model. Horizon: current process after load and subsequent loading from installed tree; uninstall is not proven to undo all effects. [RT-RTE-plugin-install](#rt-rte-plugin-install) supplies the minimum passages and admission limits. SRC-1, `src/qwenpaw/plugins/loader.py`, `src/qwenpaw/app/routers/plugins.py` (implementation).

## Annotations

none
