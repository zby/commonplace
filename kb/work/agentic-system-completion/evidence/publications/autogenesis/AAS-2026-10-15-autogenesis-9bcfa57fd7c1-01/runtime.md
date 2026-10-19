---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Autogenesis runtime baseline: task execution, delegated contexts, live capability admission and durable workflow alternatives at the frozen revision."
run-id: AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis runtime report

## Runtime account

### Evidence and consequential work

Autogenesis owns a model-directed task loop, not just a callable agent definition. Its MetaAgent can dispatch other agents, ordinary tools, instructional skills, connectors, environments and workflows. Generated capabilities can enter the live registry and the restart-loaded extension set. Those are implemented responsibilities; successful task completion and beneficial self-improvement are not established by source inspection. The frozen boundary is [boundary.md](boundary.md). All source evidence below is SRC-1 at its registered commit; Python/configuration passages are implementation evidence, while prompt and skill passages are doctrine/design. No observed-run or causal-experiment source was supplied. The target, tests and examples were not executed.

Additional inspection beyond the boundary's initial scope covered native-tool assembly, agent registry/class construction and round dispatch, the MetaAgent seams, protocol delegation, tool argument binding and Bash execution, permission helpers, model streaming/fallback and OpenRouter plugin forwarding, tool generation/registration/promotion, staged-file validation, evolution-tool recovery, workflow admission/resume/dispatch, knowledge ingest/retrieve and Gateway configuration/playground handlers. SRC-1: `autogenesis/agent/native_tools.py`, `autogenesis/agent/context.py`, `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`, `autogenesis/protocol/server.py`, `autogenesis/tool/context.py`, `autogenesis/tool/default/bash.py`, `autogenesis/permission/context.py`, `autogenesis/permission/types.py`, `autogenesis/model/context.py`, `autogenesis/model/openrouter/chat.py`, `autogenesis/hook/default/tool_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/sandbox/project.py`, `autogenesis/dynamic/server.py`, `autogenesis/tool/default/evolution.py`, `autogenesis/workflow/runtime.py`, `autogenesis/knowledge/server.py`, `autogenesis/gateway/service.py`. These are added inspected paths, not new sources or execution observations.

### Shipped invocation and ordinary loop

The installed CLI offers a one-command client, interactive terminal and Gateway service. Terminal modes create an in-process Gateway; serve offers stdio or WebSocket. Browser clients use that Gateway. The direct `examples/run_meta_agent.py` driver instead initializes managers, binds session roots, starts one TaskManager worker and submits a task itself. It is an included alternate driver, not an external host. SRC-1: `autogenesis/cli.py`, `examples/run_meta_agent.py`, `autogenesis/gateway/service.py`.

For an ordinary Gateway task, startup loads capability managers and the active extension set, starts one task worker and restores sessions. A client submits content and workspace-contained file paths for a session/conversation. Gateway records the task, binds session roots, copies session capability grants to context allowlists and calls `agent_manager` on `meta_agent`. The public task ID passes into the run; the conversation ID scopes memory/budgets/todos, while workspace/container resources remain session-shared. Session identity, task identity and runtime ref identity are therefore different. The executable class comes from the agent registry: `_load_from_registry` associates each registered class with its configuration and `build` instantiates that class. The `type = "Agent"` configuration field is not evidence that this driver bypasses MetaAgent's class. SRC-1: `configs/agents/meta_agent.py`, `autogenesis/agent/context.py`, `autogenesis/gateway/service.py`.

[RT-RTE-task-execution](#rt-rte-task-execution) traces the loop. Runtime allocates an inbox/ref and pump; the Agent stores per-ref run state. Before each model turn, code checks step/resource limits, assembles prompt messages from templates, memory, workspace snapshot, errors, budget and available capability descriptions, and projects allowed capabilities into schemas/routing. The remote model supplies reasoning and calls; code owns dispatch, not the model endpoint. The batch runs concurrently, results return through the inbox, hooks receive action/step events, and the next turn rebuilds context. Model and external service internals are outside the evidence boundary. [RT-CMP-model-manager](#rt-cmp-model-manager) records the numerical component and mutable resolution path.

A `done_tool` call normally supplies the final result; a text-only turn is nudged and consumes a step rather than completing. Max-step exhaustion, constraint blocks, cancellation and no-progress guards also terminate. Code-level success is a lifecycle result, not an independent answer oracle. In particular, MetaAgent's repeated-identical-batch guard sets `run.done = True` for a message explicitly saying the requested task is incomplete; the common conclusion then computes success from `run.done` and the constraint flag. Do not equate all successful Responses or Gateway `task.completed` events with verified goal satisfaction. SRC-1: `autogenesis/agent/actor/meta_agent.py`, `autogenesis/agent/types.py`, `autogenesis/gateway/service.py`.

### Context boundaries and return channels

[RT-RTE-child-delegation](#rt-rte-child-delegation) creates a fresh child context ID with a parent runtime-ref link and selected task/files/allowlists. It does not copy the parent's whole conversation. Only existing file paths survive delegation's filtering. The parent receives the child's `Response.message`, not the whole child context or all `Response.data`. Child internals stay outside the parent's window; file/workspace effects can still be shared. This resembles a separate call frame with a return value, not security isolation or universal heap-like references. A path in a prompt is only text until a tool reads it. An escalation posts a typed message and waits up to 300 seconds on a runtime rendezvous; MetaAgent performs a focused model turn to extract a matching `reply_tool` argument and resumes the waiter. This special turn does not dispatch arbitrary proposed work. SRC-1: `autogenesis/protocol/server.py`, `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`.

[RT-RTE-skill-instructions](#rt-rte-skill-instructions) is different: invoking a skill returns its Markdown instructions to the same calling agent. It does not run a separate model or automatic script executor. The skill manager rewrites `python scripts/` paths and appends resource/script/reference lists. Actual script execution requires another capability. There is also a shipped mismatch worth retaining: base `_allowed_skill_types` returns `["worker"]`; the inspected MetaAgent class does not override that method, although the base docstring says it does. `self_evolving_skill` declares `[orchestrator]`. Thus its presence on disk and a prompt instruction to invoke it do not establish its availability through MetaAgent's inspected type-filtered skill projection. The MetaAgent prompt itself contains substantial evolution instructions regardless. SRC-1: `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`, `autogenesis/agent/native_tools.py`, `autogenesis/skill/context.py`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`, `autogenesis/prompt/default/meta_agent.html`.

Memory read/compaction/revision details belong to the memory analyst. The inspected runtime consumption point is `_get_agent_context`: it asks the configured memory instance for `ctx.id` and a `review_steps` short-term limit. Hooks receive lifecycle/action/step events. That establishes delivery wiring, not complete restart recovery or semantic accuracy of retained summaries. SRC-1: `autogenesis/agent/types.py`.

### Four forcing cases and bounded guarantees

The forcing cases were selected to challenge plausible overgeneralizations, not to demonstrate exploits:

1. **A read-only agent calls a broadly privileged tool.** The agent dispatch gate rejects a named set of framework-mutating tools; Bash checks its own registered entity mode. The shipped Bash configuration is `danger_full_access`. A read-only agent mode alone is consequently not a transitive filesystem/network/process sandbox. [RT-RTE-shell-execution](#rt-rte-shell-execution).
2. **A generator concludes with a staged tool.** Its finalizer invokes a hook that promotes the file and registers it; no per-content human answer is read on that inspected route. The Gateway approval-response endpoint merely publishes an event. This qualifies the prompt's explicit-user-approval claim. Registration also occurs before the smoke probe, and startup loading does not use the add-component smoke branch. [RT-RTE-capability-admission](#rt-rte-capability-admission).
3. **A workflow invokes a tool directly and resumes from disk.** Workflow dispatch reaches managers without traversing the Agent's `_run_one` denylist. Schema validation and target-tool checks still apply. Resume caches completed invocation records but requeues incomplete ones; it cannot establish exactly-once external effects. [RT-RTE-workflow-execution](#rt-rte-workflow-execution).
4. **A client requests direct model chat.** Gateway's playground streams caller-supplied messages without an Agent task, native-tool roster, Agent budgets or `done_tool`. Model streaming retry/fallback applies, not the Agent loop's terminal contract. [RT-RTE-model-playground](#rt-rte-model-playground).

| Bounded guarantee | Owner and enforcement point | Strength and conclusion statuses | Covered paths, alternate paths and external contract |
|---|---|---|---|
| Only assembled names dispatch through the Agent route table | Agent `_run_one`, after schema projection | invariant; implementation conclusion status: wired; operation conclusion status: uninspected | Agent native calls reject unknown names. This is not universal authorization: workflows, direct manager calls, extension code, shell subprocesses and provider-side plugins are separate effect paths. Provider must return interpretable calls; schema projection alone does not prove provider compliance. SRC-1: `autogenesis/agent/native_tools.py`, `autogenesis/agent/types.py`. |
| Selected framework mutations are blocked for read-only agents | Agent `_run_one` checks mode, kind and denylist | policy; implementation conclusion status: wired; operation conclusion status: uninspected | Covers named tool routes, with an overridable exception seam; not arbitrary connector/environment effects or a called tool's Python internals. PermissionManager allows an unregistered entity. Bash uses its own mode. Deployment isolation is an external contract, not implied by this gate. SRC-1: `autogenesis/agent/types.py`, `autogenesis/permission/context.py`, `autogenesis/tool/default/bash.py`. |
| Frozen registered capabilities cannot be overwritten through the evolution guard | ExtensionManager `_assert_evolvable` called by eligible add-component loaders | policy; implementation conclusion status: wired; operation conclusion status: uninspected | Lookup errors fail closed for supported guarded types. Prompt loading carries no flag; memory is not among `_current_enable_evolving`'s explicit lookups. Startup/reload/rollback do not enforce evolution gating. Class source is dynamically executed before the overwrite check; the gate is not an import sandbox. Configuration APIs and direct Python are other paths. SRC-1: `autogenesis/extension/server.py`, `autogenesis/dynamic/server.py`. |
| Failed smoke admission attempts revert or unload | ExtensionManager after live registration, archive and manifest write | best effort; implementation conclusion status: wired; operation conclusion status: uninspected | Default on for add-component, explicitly/configurably disableable; rollback errors are logged. Startup scan/load bypasses this probe. The external model/general-agent run must be available. Probe success does not prove use, safety or benefit of the candidate. SRC-1: `autogenesis/extension/server.py`, `autogenesis/extension/smoke_gate.py`. |
| Workflow resume checks executable identity and skips recorded completed work | WorkflowRuntime `resume` | protocol; implementation conclusion status: wired; operation conclusion status: uninspected | Checks runtime major, workflow name/version and a present program hash; legacy hashless records are migrated after identity checks. Completed records become cached; uncompleted effects may repeat. Requires truthful intact checkpoint records and idempotent/transactional external actions for stronger guarantees. SRC-1: `autogenesis/workflow/runtime.py`. |
| Shared Gateway task roots are rebound on its serialized task path | Gateway one worker and `_bind_runtime_to_session` | protocol; implementation conclusion status: wired; operation conclusion status: uninspected | Ordinary queued task execution is serialized; action batches within a task are concurrent. Direct chat, workflow/control handlers and callers outside this queue prevent inferring total runtime serialization or per-session process isolation. SRC-1: `autogenesis/gateway/service.py`. |

The capability **surface** is broader than the current **grant set**: loaded managers expose potential tools, skills, agents, connectors, environments and workflows; Gateway copies selected session capabilities to allowlists, and delegation can supply narrower child lists. Neither is the **deployed isolation envelope**. Bash uses a bound peer sandbox when present and otherwise launches a local shell with inherited environment and workspace cwd. A cwd is not a confinement boundary. Comments describing project-container execution do not establish the actual deployment. Dynamic extensions execute Python in this process, and provider plugin forwarding crosses a remote boundary outside Agent action dispatch. SRC-1: `autogenesis/gateway/service.py`, `autogenesis/agent/native_tools.py`, `autogenesis/protocol/server.py`, `autogenesis/tool/default/bash.py`, `autogenesis/dynamic/server.py`, `autogenesis/model/openrouter/chat.py`.

Material alternates enumerated here are direct example/manager invocation, callable children and escalation callbacks, same-context skills, manager-dispatched connector/environment actions, shell subprocesses, dynamically loaded extensions, direct model/playground calls with provider plugins, and manual/durable workflows. Gateway also exposes canvas run/save/library, deployment, IDE and science/kernel control handlers. Their existence and command endpoints were inspected in `autogenesis/gateway/service.py`; complete canvas/compiler, science/kernel, connector-host, browser/remote-worker, Docker and transport security internals were not traced in this runtime pass. No universal safety, exactly-once, approval, context-isolation or permission guarantee is claimed for those alternatives. Those are available-but-uninspected implementation details, not absent mechanisms or access gaps.

### Change admission and improvement limits

[RT-RTE-capability-admission](#rt-rte-capability-admission) traces a concrete generated-tool path and its alternate Gateway promotion transaction. The proposer is a model-driven generator/optimizer, code resolves a reported file, validates staging syntax/paths, copies it, executes/loads it, checks supported overwrite flags, registers/archives it and runs an optional default-on synthetic smoke probe. The deciding MetaAgent is instructed to use evaluator reports and with/without probes, then keep, rollback or unload. Those comparative quality decisions are natural-language policy, not an automatically enforced score threshold on the inspected tool-admission path. The smoke decision instead checks whether a general-agent probe returned success without a constraint stop. Its instruction says exactly `OK`, but code does not compare the returned message to that expected answer. SRC-1: `autogenesis/agent/generator/tool_generate_agent.py`, `autogenesis/hook/default/tool_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/sandbox/project.py`, `autogenesis/extension/server.py`, `autogenesis/extension/smoke_gate.py`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`.

Administrative capability/model configuration is another admission route, [RT-RTE-runtime-configuration](#rt-rte-runtime-configuration); it does not share every evolution check. Knowledge ingest is a further write mechanism, [RT-RTE-knowledge-admission](#rt-rte-knowledge-admission): workflow-accessible software appends normalized documents and a backend manifest without a model-truth or per-content human gate in that handler. Memory specialists should separately assess store lineage, transformations and later model delivery. Source-native retained material here includes source files, instruction text, versions/manifests and document corpora—not demonstrated weight training.

The claimed evolution loop is represented by [RT-CLM-self-evolution](#rt-clm-self-evolution). For the boundary of Autogenesis's reusable capabilities across later dispatches and restarts, the objective is better completion of user tasks using a missing or improved capability. The objective is independently stated, but the supplied evidence establishes a standing improvement-directed self-change path, not exercised self-improvement. Evidence-responsive proposal selection is requested by policy; code admits resulting capability changes to live authority and restart loading. There is no trace closing the link from a particular failure/evaluation to an update, and no subsequent operation showing causal dependence on that update. Installation is not benefit. Learning, content-directed criticism, reflection and autonomous theory building remain separate questions; the conditional route assessment below does not infer them from registration.

## Shared records

### Components

#### RT-CMP-model-manager
Label: Model manager and remote decision models

Source-native identity: `model_manager`, its `ModelContextManager`, and provider clients used for agent decisions and the smoke role. The model's operative decision content is distributed-parametric, stored on provider infrastructure; local registry/client configuration is symbolic Python/Pydantic state in RAM. The inspected application passes messages and tool schemas; provider weights and internal state are not available. No parameter update is performed by the inspected invocation/registration methods; whether providers change parameters internally is uninspected. Exact model weights/version are not pinned by the repository commit. The default MetaAgent config names `google/gemini-3.1-pro-preview`; named roles, runtime registration, configurable API base/model ID and fallback can resolve later requests differently. A stable configured name is not immutable model identity. SRC-1: `configs/agents/meta_agent.py`, `configs/base.py`, `autogenesis/model/server.py`, `autogenesis/model/context.py`, `autogenesis/gateway/service.py`.

> self.models[config.model_name] = config
> --- `autogenesis/model/context.py`

> fb = model_config.fallback_model if model_config else None
> --- `autogenesis/model/context.py`

Streaming retries primary calls before any emitted event, then optionally a configured fallback. Once an event has escaped, an exception propagates; Agent `_think` catches failures and returns an empty call batch, leaving later loop/budget logic to react. Provider success and beneficial decisions are unobserved.

### Operative objects

#### RT-OBJ-meta-agent
Label: MetaAgent prompt and embedded evolution policy

Source-native identity: `meta_agent.html`. Natural-language rules interpreted by the model, stored as HTML/template text in source and rendered messages in RAM. Module markup is symbolic template machinery; the operative decision guidance described here is the rendered prose. It requests fix-versus-evolve diagnosis, scoped generation/optimization, evaluation and rollback, review and explicit completion. SRC-1: `autogenesis/prompt/default/meta_agent.html`, `autogenesis/agent/types.py`.

> - **Do NOT evolve** on a first-time fixable deliverable defect (→ continue), on a one-off transient error (→ retry), when budget is TIGHT/CRITICAL (→ finish the task), or to "improve" a frozen built-in (blocked at registration — generate an `extension/` capability instead).
> --- `autogenesis/prompt/default/meta_agent.html`

Its content can influence decision calls through [RT-BAP-prompt-guidance](#rt-bap-prompt-guidance); compliance is not established merely by inclusion.

#### RT-OBJ-extension-manifest
Label: Active extension manifest and version archives

Source-native identity: ExtensionManager `Manifest`, active files and archived versions. Manifest metadata/version identities are symbolic; substrate is JSON and files below the shared extension root. Actual extension Python is a separate operative part, [RT-OBJ-extension-source](#rt-obj-extension-source). Startup reads active paths, attempts loading, archives and retains only successfully loaded entries; missing/broken files are skipped with logs. SRC-1: `autogenesis/extension/server.py`.

> await self._load_component(comp.module, abspath, comp.name, version=comp.version, config=None)
> self._ensure_archived(comp.module, comp.name, abspath, comp.version)
> loaded.append(comp)
> --- `autogenesis/extension/server.py`

#### RT-OBJ-extension-source
Label: Dynamically loaded capability source

Source-native identity: generated tool `.py` file loaded through `load_class_from_path`, then registered as a tool. Symbolic executable Python on disk, transformed into Python class/module/instance objects in process memory. Natural-language instruction/description strings within a tool are a different consumption path from executable method bodies. Generated code may include arbitrary imports and effects; syntax validation is not behavioral confinement. SRC-1: `autogenesis/extension/server.py`, `autogenesis/dynamic/server.py`, `autogenesis/sandbox/project.py`.

> # Execute the code in the module namespace
> exec(code, module.__dict__)
> --- `autogenesis/dynamic/server.py`

#### RT-OBJ-workflow-checkpoint
Label: Workflow executable state checkpoint

Source-native identity: `WorkflowRun` checkpoint JSON and registered workflow definition. Symbolic run/frame/invocation state stored on disk and reconstituted in memory, consumed by fixed resume rules. The checkpoint is not a learned method simply because it persists. SRC-1: `autogenesis/workflow/runtime.py`.

> if item.state == InvocationState.COMPLETED:
>     item.state, item.cached = InvocationState.CACHED, True
> --- `autogenesis/workflow/runtime.py`

#### RT-OBJ-self-evolving
Label: Self-evolving skill playbook

Source-native identity: `self_evolving_skill/SKILL.md`. Natural-language method text on disk and in a skill configuration, returned as instructions when selected; not a numerical parameter update or autonomous controller. It distinguishes repairing a user deliverable from changing the framework's capabilities, requests representative with/without comparisons and records of keep/rollback decisions. The skill type-filter issue in the Runtime account limits claims of its default delivery. SRC-1: `autogenesis/skill/creator/self_evolving_skill/SKILL.md`, `autogenesis/skill/context.py`.

> - **The decision is yours (prose, not code).** Nothing automatically scores an evaluation
>   and promotes/rolls back. YOU read the evaluator's scored report and decide. Own that
>   decision explicitly in your reasoning.
> --- `autogenesis/skill/creator/self_evolving_skill/SKILL.md`

### Routes

#### RT-RTE-task-execution
Label: Gateway task through the shared agent loop

Trigger/principal: a client submits user content to a session/conversation; TaskManager owns queue scheduling. Gateway binds roots/grants and AgentManager invokes the registered MetaAgent. Runtime owns pump delivery; Agent owns step/context/dispatch/terminal state; model supplies next calls. Action effects execute in the respective managers, local process, shell or remote adapter, not inside the schema shim. Model input combines natural-language prompt/context and symbolic schemas; run/ref state is symbolic RAM. Hooks receive trace, memory and trajectory events; Gateway publishes lifecycle events and task records retain outputs. SRC-1: `autogenesis/gateway/service.py`, `autogenesis/agent/context.py`, `autogenesis/runtime/server.py`, `autogenesis/agent/types.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: task submission yields task/conversation IDs; eventual task result is the Agent Response and Gateway completion/failure/cancel events.
- Later read-back: subsequent model turns request configured memory by context ID; retained-session/conversation recovery is separate from full agent-run resumption.
- Delegated visibility: child calls receive selected task/files and allowlists through [RT-RTE-child-delegation](#rt-rte-child-delegation), not the parent's entire messages.
- Selection predicate: valid submitted content/session, workspace-contained attachments; session capabilities determine projected schema lists; model chooses calls from that roster.
- Invalidation or expiry: run state is removed on conclusion, remaining round tasks cancelled; max-step, constraints, cancellation and no-progress rules bound continuation.
- Activation or effect: routed calls execute managers and their effects; delivered instructions request model behavior but actual compliance and task success are unobserved.
- Evidence limits: implementation only; no quality oracle or execution trace; `success` is not a correctness proof, and batch independence is a model/prompt expectation rather than conflict serialization.

Decision roles: user supplies the task; model proposes action batches and `done_tool`; code can reject invalid routes/budgets and terminate. Operating mode: open user requests, not a fixed curriculum. Answer oracle: none automatically supplied by this generic loop; individual tasks may provide acceptance criteria. Recovery distinguishes per-action errors fed into later turns from pump crashes, which mark a ref DEAD, and from durable workflow resume.

> ref = AgentRef(name=ref_name, agent_name=agent_name, status=AgentStatus.RUNNING)
> ref._pump_task = asyncio.create_task(_pump(agent, ref), name=f"pump-{ref_name}")
> --- `autogenesis/runtime/server.py`

> success = run.done and not run.stopped_by_constraint
> --- `autogenesis/agent/types.py`

#### RT-RTE-child-delegation
Label: Child delegation and parent escalation

Endpoints: parent model agent → protocol delegate → fresh child context and runtime invocation → parent action result. Runtime/protocol code controls identities and rendezvous; child model owns its own decisions. Task, filtered existing files, target name and supplied capability allowlists cross the boundary. Parent-ref lineage permits escalation; a new context ID isolates history selection, not filesystem effects. SRC-1: `autogenesis/protocol/server.py`, `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: awaiting delegation yields the child Response; Agent capability dispatch forwards `resp.message` on success or raises the failure message.
- Later read-back: child hook-driven history is addressed by its own context ID; cross-run memory reload is uninspected here and not implied by the return.
- Delegated visibility: explicit task, existing files, target and provided lists; the parent's full model window is not copied. Parent receives escalation text or final message rather than the full child trace.
- Selection predicate: projected registered agent name and model-provided arguments; optional target-derived defaults fill unspecified allowlists.
- Invalidation or expiry: one-shot runtime invocation stops its ref in `finally`; escalation times out after 300 seconds or returns fallback guidance when the parent is unavailable.
- Activation or effect: child executes its own loop; model-mediated escalation guidance reaches the child waiter; shared filesystem/service effects are not undone by dropping its context.
- Evidence limits: no demonstration of useful decomposition, complete grant inheritance or container isolation. The delegate signature accepts workspace_root but the inspected body does not use it to build an execution sandbox.

> existing = [f for f in (files or []) if os.path.exists(f)]
> return await runtime_manager.invoke(child, task=task, files=existing or None, ctx=ctx, parent_ref=parent_ref)
> --- `autogenesis/protocol/server.py`

> return resp.message, False, None, None
> --- `autogenesis/agent/types.py`

#### RT-RTE-skill-instructions
Label: Same-context skill instruction delivery

Endpoints: model skill call → SkillManager configuration lookup → text Response → calling agent's action/memory channel. Owner is SkillContextManager for lookup/formatting; deciding consumer is the foreground model. Source Markdown is natural language; resource lists and version metadata are symbolic descriptive fields, not automatically executed actions. SRC-1: `autogenesis/skill/context.py`, `autogenesis/agent/native_tools.py`, `autogenesis/agent/types.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: full skill content with script-path substitution and available-resource lists in `Response.message`.
- Later read-back: action hooks may retain returned text for later model calls; exact retention, compaction and restart horizon belong to the memory account.
- Delegated visibility: inapplicable — this route returns to the same caller, without creating an agent frame.
- Selection predicate: loaded name filtered by skill allowlist and allowed skill types before projection; skill manager then looks up the requested configuration.
- Invalidation or expiry: the selected configuration/version supplies the current text; subsequent registrations can replace it, while already-delivered text remains in whatever context/history retains it.
- Activation or effect: instructions are returned for model interpretation; no automatic execution of listed scripts and no observed compliance.
- Evidence limits: delivery does not establish that scripts ran, guidance was applied, or the orchestrator-typed evolution playbook was available to default MetaAgent.

> content = skill_config.content.replace("python scripts/", f"python {skill_dir}/scripts/")
> parts = [content]
> --- `autogenesis/skill/context.py`

#### RT-RTE-shell-execution
Label: Tool-owned Bash execution boundary

Endpoints: Agent/workflow/direct ToolManager call → BashTool permission request → peer sandbox or local subprocess → text/exit-code Response. ToolContextManager checks call binding and imposes a timeout; BashTool owns its inner timeout and permission request. Registered Bash entity mode, not automatically the caller-agent mode, controls the permission helper. SRC-1: `autogenesis/tool/context.py`, `autogenesis/tool/default/bash.py`, `autogenesis/permission/context.py`, `autogenesis/permission/types.py`, `configs/tools/bash.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stdout/stderr and exit code; local completed shell commands return tool success even when their process exit code is nonzero.
- Later read-back: filesystem/service changes can outlive the invocation and be consumed by subsequent tools; hook retention of output is separate from those effects.
- Delegated visibility: an optional `ctx.extra["sandbox"]` receives the command; otherwise a local shell inherits process environment with runtime-bin PATH and workspace cwd.
- Selection predicate: exposed Bash capability plus supplied command; PermissionManager calls the entity enforcer if registered and otherwise allows.
- Invalidation or expiry: Bash timeout kills the local process group on its timeout branch; arbitrary durable external effects are not rolled back. Manager timeout is another cancellation boundary, not an atomic-effect guarantee.
- Activation or effect: subprocess or peer command execution can modify resources permitted by the actual environment; no deployment isolation strength is established.
- Evidence limits: source code and default configuration, not a deployed sandbox or exploit test. Command classification is policy; a workspace cwd does not confine arbitrary Python/shell effects.

> permission_mode = "danger_full_access",
> --- `configs/tools/bash.py`

> process = await asyncio.create_subprocess_shell(
>     command,
>     stdout=asyncio.subprocess.PIPE,
>     stderr=asyncio.subprocess.PIPE,
>     start_new_session=True,
>     env=command_env,
>     cwd=cwd,
> )
> --- `autogenesis/tool/default/bash.py`

#### RT-RTE-capability-admission
Label: Generated tool admission and shared promotion

Trigger: explicit capability creation or model diagnosis of a missing/weak capability while serving a task. Proposal: generator/optimizer writes source under extension staging and reports its path in `done_tool` reasoning. ToolGenerateAgent finalizes a successful run through ToolRegistrationHook. The hook resolves a file, validates staged contents, automatically promotes it when staged and calls ExtensionManager.add_component with evolvability enabled. Code, not a human response, admits this inspected path. Alternate Gateway `extension.promote` takes caller-selected files/overwrite/smoke settings, snapshots the manifest and restores file/registry state after a failed batch. SRC-1: `autogenesis/agent/generator/tool_generate_agent.py`, `autogenesis/hook/default/tool_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/sandbox/project.py`, `autogenesis/extension/server.py`, `autogenesis/gateway/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook allow/block modifies generator success; successful registration returns a component name after archive/manifest and enabled smoke handling; Gateway promotion returns its promotion/registration report.
- Later read-back: manager lookups expose the active registered capability to later calls; extension startup reloads active manifest files. This establishes an executable future-consumption path, not an observed invocation of the update.
- Delegated visibility: parent sees the generator's final Response message; subsequent actors can see new projected capability schemas. Already-running work and cached contexts need not see a refreshed roster immediately.
- Selection predicate: successful generation, resolvable path, staged path/syntax validation, supported overwrite gate, registration and optional smoke result; no evaluator quality threshold or mandatory human approval token is tested in the inspected tool hook.
- Invalidation or expiry: version rollback/unload through evolution_tool; failed smoke tries previous-version rollback or unload, with logged recovery failures; Gateway transaction separately restores copied files and pre-transaction manifest.
- Activation or effect: source executes in-process during class loading, then live manager registration and durable manifest/archive update occur before the smoke probe; later behavior can use the changed class or instruction.
- Evidence limits: no supplied generated artifact, run or comparison. The synthetic probe need not invoke the changed capability and does not verify exact OK text; archive rollback does not reverse arbitrary import-time or external side effects.

Decision roles and veto: model proposes source and can request evaluation/rollback; syntax/path checks, supported frozen-entity checks, registration failures and smoke failure can reject. The default smoke uses a general_agent model run, bounded by a wall timeout and usually a two-step copied configuration. Computational success flags decide it; no human veto is consumed on this automatic path. A person can separately call administrative APIs or edit supplied material, but starting a task is not per-content approval. Operating modes: open task-driven evolution; optional requested representative with/without probes; automatic bounded synthetic healthcheck. Answer oracle: synthetic task provides expected `OK` in its instruction, but admission uses Response.success and constraint state, not string equality. Generic evaluator model judgment is not an answer oracle.

Guidance/persistence: [RT-OBJ-meta-agent](#rt-obj-meta-agent) and [RT-OBJ-self-evolving](#rt-obj-self-evolving) request failure diagnosis, one change at a time, evaluations and keep/rollback reasoning. Code persists source, active manifests and version archives; prompt requests do not prove retained causal rationale or adoption of the evaluation policy. The playbook says no memory triad exists, whereas shipped configs/classes include memory generate/optimize/evaluate agents; that doctrine sentence is stale relative to the included implementation, not evidence of missing capability. SRC-1: `configs/meta_agent.py`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`.

> if is_staged_extension_root(extension_root):
>     validate_staged_extension(extension_root)
>     from autogenesis.hook.promotion import promote_approved_component
>     tool_path = promote_approved_component(extension_root, tool_path)
> --- `autogenesis/hook/default/tool_registration.py`

> name = await extension_manager.add_component("tool", tool_path, config={"enable_evolving": True})
> --- `autogenesis/hook/default/tool_registration.py`

> if self._smoke_enabled(run_smoke):
>     await self._smoke_gate_or_revert(module, name, prev_version)
> --- `autogenesis/extension/server.py`

> ok = bool(getattr(resp, "success", False)) and not data.get("stopped_by_constraint", False)
> --- `autogenesis/extension/smoke_gate.py`

Theory account, bounded to the explicit evolution method: the playbook is a localized method with exposed conditions (e.g. recurring structural failure versus fixable attempt); it applies a diagnosis-and-comparison policy, not a fixed automatic curriculum. It asks the model to revise capabilities, not necessarily the playbook itself. For **theory-builder conditions 1–4**: condition 1 conclusion status: afforded — whole natural-language method units exist; condition 2 conclusion status: claimed — prompt requests decisions according to those units, but actual content-dependent choices are unobserved and the skill delivery mismatch limits this path; condition 3 conclusion status: claimed — guidance requests failure evidence and blame at the capability level, without a supplied criticism naming a challenged method claim, result, attribution and actual revision; condition 4 conclusion status: claimed — ordered re-optimization/rollback rounds are instructed, without an observed criticism retained and used in another round. Addressability: individual prose rules and separate source files are inspectable/editable; no fine-grained formal claim/dependency model is established. Persistence: method is shipped across problems/sessions; generated capabilities and versions have a cross-restart consumer; episode rationale's retention/use is left to memory findings. Learning: improved future capacity is not demonstrated or causally attributed. Reflection: capability inspection/feedback and changes provide machinery for self-representation and intervention, but no observed bidirectional representation-mediated correction cycle is supplied. Reflective theory builder: no evidenced criticism of this method against its own operation. Autonomous theory builder: code/model can author and automatically admit a capability without per-content approval, but this does not establish every internal theory-building operation or its success. Self-improvement: standing improvement-directed self-change is afforded/wired; links from objective-bearing evidence to this update and from subsequent operation to causal dependence on it remain unobserved. No successful improvement claim follows.

#### RT-RTE-workflow-execution
Label: Direct and durable workflow execution

Endpoints: Agent workflow call or Gateway run/restore request → WorkflowRuntime admission/drive/resume → target managers/checkpoint/output. Code interprets a symbolic compiled program, owns branching/concurrency/budgets/terminal state and dispatches agents, tools, skills, connectors, environments, nested workflows, plugins, process/data/knowledge/benchmark operations. Agent calls can introduce a model-directed inner loop, but the outer next-step policy is the workflow program. SRC-1: `autogenesis/workflow/runtime.py`, `autogenesis/gateway/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: a run object or Gateway run identity/status; successful outer execution resolves declared outputs or public variables.
- Later read-back: checkpoint reload reconstructs variables, frames and invocations; completed records become cached and incomplete work is requeued subject to identity/hash checks.
- Delegated visibility: each call receives resolved payload/context through its owning manager; Agent dispatch and provider calls remain distinct consumers, not a single shared window.
- Selection predicate: non-deprecated definition, input validation, depth/root agent budget and capability preflight; resume checks runtime major/name/version/hash. Tool/skill/connector/environment dispatch additionally validates callable schema.
- Invalidation or expiry: mismatch rejects resume, except legacy missing-hash migration; timeout/cancel/failure checkpoint terminal state; process-retained run cache is bounded. External partial effects need their own idempotence/recovery.
- Activation or effect: direct manager execution bypasses Agent `_run_one` and its named-tool denylist while retaining the target manager/tool's own checks; checkpoint state controls whether an invocation runs or is reused.
- Evidence limits: no observed workflow run, crash/recovery experiment or exactly-once effect proof; full canvas compilation and all leaf managers are uninspected here.

Decision roles: caller supplies workflow/input or resume checkpoint; code validates and controls execution. Operating mode: caller-directed bounded program. Answer oracle: generic workflow success is not a reference answer; explicit verification/benchmark steps may supply task-specific checks, not automatically a universal correctness oracle.

> if kind == StepType.TOOL:
>     from autogenesis.tool import tool_manager
>     await self._validate_invocation_schema(await tool_manager.get_schema(target), payload, target)
>     return await tool_manager(name=target, input=payload, ctx=ctx)
> --- `autogenesis/workflow/runtime.py`

#### RT-RTE-model-playground
Label: Direct model playground and provider boundary

Endpoints: Gateway model.chat → model_manager.stream → provider → model.chat delta/done/error/cancel events. Caller supplies system/user/assistant text; no Agent task or tool roster is created. Owner of turn progression is the client; the model computes one completion and the model manager controls opening retry/fallback. Provider configuration can include remote OpenRouter plugins, which are forwarded by its adapter rather than executed through Agent `_run_one`. SRC-1: `autogenesis/gateway/service.py`, `autogenesis/model/context.py`, `autogenesis/model/openrouter/chat.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: request ID and model; asynchronous text/thinking deltas and final accumulated text/usage, or error/cancel events.
- Later read-back: uninspected — Gateway event publication exists, but a dedicated replay-to-next-model policy for playground messages was not traced; caller can submit its own later messages.
- Delegated visibility: remote provider receives converted messages; provider plugin internals and retention are outside SRC-1.
- Selection predicate: registered model and non-empty validated role/string message list; configured endpoint/provider/plugin/fallback then governs execution.
- Invalidation or expiry: cancellation removes active chat work; retry/fallback only before the first event, with later failures surfaced instead of replaying emitted output.
- Activation or effect: one provider completion/event stream; it has no Agent `done_tool` completion or agent constraint hooks on this call path.
- Evidence limits: no provider run, plugin execution trace, remote retention or deployed model identity proof; absence of Agent dispatch here is not a claim that providers cannot perform remote work.

> async for event in model_manager.stream(name=model, input={"messages": messages}):
> --- `autogenesis/gateway/service.py`

> response = await client.chat.completions.create(
>     model=self.model,
>     messages=messages,
>     plugins=plugins,
>     **params,
> )
> --- `autogenesis/model/openrouter/chat.py`

#### RT-RTE-runtime-configuration
Label: Administrative capability and model configuration

Trigger/endpoints: Gateway caller submits capability.configure or model.configure → validated fields and manager update/registration → configuration detail and change event. Proposed changes include tool/agent configuration, skill description/metadata/content, and model provider/ID/API base/reasoning/plugins/fallback. Gateway code admits a syntactically valid supported update; it is not the generator's smoke/evaluation path. SRC-1: `autogenesis/gateway/service.py`, `autogenesis/model/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: new capability detail or model summary/safe configuration with change events.
- Later read-back: later manager lookups use the updated registration; durable restart persistence for these administrative edits is uninspected and not inferred from extension manifests.
- Delegated visibility: later model/agent/tool users encounter changed configuration; no automatic redistribution to every already-running invocation is established.
- Selection predicate: existing capability/name, supported editable kind/field/types; ModelConfig validation, allowed provider and nonconflicting name. Caller identity does not establish a human made the per-content decision.
- Invalidation or expiry: a later administrative update can replace configuration; transactional rollback and automatic quality rejection are uninspected for these handlers.
- Activation or effect: manager update/register calls change active configuration, including the remote endpoint and skill instruction content; physical I/O and downstream consumption are separate.
- Evidence limits: no observed configuration change or authentication/deployment audit. These handlers do not establish the evolution smoke/approval guarantees for all changes.

Admission: caller proposes and selects content, software validates; no model quality comparison or answer oracle is used by these handlers. Operating mode: explicit administrative edits, not an autonomous improvement experiment. Guidance: handler field/type contracts; no retained explanatory theory or evidence-responsive improvement trigger is established. Rejection: bad names/fields/providers/configuration fail; recovery beyond reconfiguration remains uninspected.

> await model_manager.register_model(model)
> if original_name and original_name != model.model_name:
>     await model_manager.unregister_model(original_name)
> --- `autogenesis/gateway/service.py`

#### RT-RTE-knowledge-admission
Label: Knowledge corpus append and retrieval

Trigger/endpoints: caller or workflow knowledge step → KnowledgeManager knowledge_ingest → document coercion/backend-name validation → corpus.jsonl append and manifest.json write; knowledge_retrieve rereads documents, selects backend hits and returns records. The document text is natural-language material on disk, while metadata/backend selection and index/score outputs are symbolic here; numerical backend implementation/provenance is uninspected in this runtime pass. SRC-1: `autogenesis/knowledge/server.py`, `autogenesis/workflow/runtime.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ingest counts/base/type, or retrieve records with scores in Response.data; the short message alone does not contain those records.
- Later read-back: retrieval rereads accumulated corpus and type manifest, searches texts by query/task and top_k, then returns selected records. Further injection into a model is not established by this handler alone.
- Delegated visibility: workflow receives the raw manager result for later normalization; other direct callers must inspect the data field to access records.
- Selection predicate: base/name and valid registered backend for ingest; nonempty base/query and backend search, default top_k four clamped to at least one, for retrieval.
- Invalidation or expiry: no eviction or revision rollback is established in these inspected ingest/retrieve methods; disk persists until another mechanism changes/removes it.
- Activation or effect: appends supplied documents and overwrites backend manifest; retrieval delivers selected records, not guaranteed truth or changed decisions.
- Evidence limits: memory transformations, ranking backend internals and later model consumption require separate inspection; no retrieval quality or learning result is observed.

Admission roles: caller supplies documents/backend; code normalizes/appends and can reject missing base/unknown backend or I/O failure. Human authorship/approval is unresolved; no truth/evaluation veto or answer oracle appears in these handlers. Operating mode: caller-triggered ingestion/retrieval, not a demonstrated automatic improvement curriculum. Guidance: schema/backend contract only; no formulated theory revision is established. Recovery: write errors return failure; atomic multi-file rollback is not established.

> with open(os.path.join(directory, "corpus.jsonl"), "a", encoding="utf-8") as handle:
>     for doc in docs:
>         handle.write(json.dumps(doc, ensure_ascii=False) + "\n")
> --- `autogenesis/knowledge/server.py`

### Claims

#### RT-CLM-self-evolution
Label: Task-serving self-evolution claim

Claimed operation: MetaAgent detects missing/weak capabilities and invokes generate/optimize/evaluate roles to change the framework while serving a task. Source is target doctrine, not an observed improvement. [RT-RTE-capability-admission](#rt-rte-capability-admission) establishes a concrete live/durable change path and its limits; it does not establish beneficial or exercised self-improvement. SRC-1: `autogenesis/skill/creator/self_evolving_skill/SKILL.md`.

> - **Two directions, never confuse them.** *User work* (write the app, answer the
>   question) is done by `code_agent` / `general_agent` (`category: actor`). *Self-evolution*
>   changes the framework's own capabilities and is done by the generate/optimize/evaluate
>   agents (`category: generator/optimizer/evaluator`). Evolution serves the task; it is
>   never the deliverable unless the user asked for it.
> --- `autogenesis/skill/creator/self_evolving_skill/SKILL.md`

#### RT-CLM-user-approval
Label: Explicit user approval for shared promotion

Claimed operation: the MetaAgent prompt describes session staging followed by validation and explicit user approval before shared promotion. The inspected tool registration hook automatically calls the promotion bridge; that bridge copies the selected file without consuming a human answer. Gateway's approval response acknowledges/publishes, rather than resuming a blocked approval waiter. The claim is therefore not an invariant of all material admission paths. This is a bounded caller-path finding, not a claim that users cannot manually approve changes. SRC-1: `autogenesis/prompt/default/meta_agent.html`, `autogenesis/hook/default/tool_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/gateway/service.py`.

> - `{{ extension_root }}` — this session's writable extension staging tree. Write evolved capabilities here; they are promoted to the shared extension root only after validation and explicit user approval.
> --- `autogenesis/prompt/default/meta_agent.html`

> # The existing runtime does not yet expose a user-approval rendezvous.
> # Accepting the command keeps the protocol stable while permissions migrate here.
> --- `autogenesis/gateway/service.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Prompt guidance to model decisions

Consumer: remote model called by Agent._think. Channel: rendered MetaAgent prompt and per-turn task/memory/budget/capability context. Force: natural-language policy, distinct from routing and budget invariants. Horizon: every reconstructed turn that selects the prompt; shipped prompt persists across sessions unless configuration/source changes. Embedded evolution guidance can shape proposal selection, but neither delivery nor instructions to review establish compliance. SRC-1: `autogenesis/agent/types.py`, `autogenesis/prompt/default/meta_agent.html`. Object: [RT-OBJ-meta-agent](#rt-obj-meta-agent); route: [RT-RTE-task-execution](#rt-rte-task-execution).

> input={"messages": messages, "tools": tools},
> --- `autogenesis/agent/types.py`

#### RT-BAP-extension-execution
Label: Retained extension source to live execution

Consumer: DynamicModuleManager and owning capability manager, followed by later capability callers. Channel: active file/manifest → class load → registered Python instance/native schema → method dispatch. Force: executable symbolic behavior within actual process privileges; descriptive tool text separately influences model selection. Horizon: immediately during loading and later manager calls, with archive/manifest startup paths across restarts. A retained update has a live authority path, but no supplied trace shows a changed capability exercised. SRC-1: `autogenesis/extension/server.py`, `autogenesis/dynamic/server.py`, `autogenesis/tool/context.py`. Objects: [RT-OBJ-extension-source](#rt-obj-extension-source), [RT-OBJ-extension-manifest](#rt-obj-extension-manifest); admission: [RT-RTE-capability-admission](#rt-rte-capability-admission).

> return await asyncio.wait_for(tool_instance(**input, **tool_kwargs), timeout=self.default_timeout)
> --- `autogenesis/tool/context.py`

#### RT-BAP-skill-guidance
Label: Selected skill content to calling agent

Consumer: calling agent model on a later turn, if action-history retention delivers the skill response. Channel: skill Markdown → Response.message → action/memory context. Force: interpreted instruction, not an automatic code invocation. Horizon: current execution and any later context retaining it; cross-restart horizon is unestablished here. The self-evolving playbook has the separate type-filter limitation already stated. SRC-1: `autogenesis/skill/context.py`, `autogenesis/agent/types.py`. Object: [RT-OBJ-self-evolving](#rt-obj-self-evolving); delivery: [RT-RTE-skill-instructions](#rt-rte-skill-instructions).

## Annotations

none
