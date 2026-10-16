---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenSage's manager-driven execution, delegation, capability admission and alternate runner paths at the frozen repository revision."
run-id: AAS-2026-10-14-opensage-291d1ed79d37-01
reviewed-boundary: "54d64702e18d195c8f0fed711c6db5dc1d62ab29"
---

# OpenSage runtime report

## Runtime account

### Work and evidence basis

OpenSage supplies a model-directed agent runtime assembled around Google ADK. Its distinctive claimed work is runtime creation of agent topology, toolsets and memory, rather than only returning text. The inspected implementation supports model-proposed agent definitions, independent agent instances, peer messages and shell-based capability construction. These are implemented opportunities, not evidence of effective decomposition or successful self-improvement. [RT-CLM-runtime-creation](#rt-clm-runtime-creation) retains the declared claim; [RT-RTE-create-subagent](#rt-rte-create-subagent) and [RT-RTE-terminal-extension](#rt-rte-terminal-extension) retain its implemented paths.

The frozen source is SRC-1 at the boundary's revision. There are no supplied execution traces or causal experiments. Nothing in this report establishes actual activation, reliable model compliance, benchmark performance or learned improvement. Source-native tests were not executed. The account adds implementation inspection of the manager's spawn, resume, dispatch, directed-invocation and fake-user branches; inbox delivery; dynamic-agent building and rebuilding; model registry and budget wrappers; shell interface; local and native-Docker backends; plugin loading and hook compatibility; compaction selection and append; web live execution; direct-runner drivers; and the AReaL adapter. These are additional inspected scopes within SRC-1, not new sources. Anchors appear beside the findings below.

### Ordinary invocation, identities and state

A normal `opensage run` starts with the operator selecting an agent directory and configuration and supplying a task. The CLI imports its `agent.py`, calls `mk_agent`, loads configured plugins, registers the root and its declared subagents, adopts or creates a root session, and starts the manager. The import and agent factory are executable Python in the host process, not a sandboxed model action. The CLI sends input as `__user__` into the root inbox and waits for manager idleness while polling session events for terminal display. [RT-RTE-user-dispatch](#rt-rte-user-dispatch) records the loop (SRC-1, `src/opensage/cli/opensage_cli.py`).

An OpenSage session owns resources and a manager; agent names identify templates, while session IDs identify independent instances. ADK session lookup uses app name, user ID and session ID. The manager creates per-instance runners with the OpenSage session, artifact, memory and credential services, a shared-budget plugin, configured base plugins and a runner-scoped inbox plugin. Instance metadata and trajectories live in nested host directories. The agent object is shallow-copied per instance; separate instance state is not a claim that all referenced Python objects, tools or provider resources are isolated (SRC-1, `src/opensage/orchestration/manager.py`, `src/opensage/llm/registry.py`).

The dispatcher owns wake decisions and changes a sleeping instance to running before awaiting its work. Pending inbox messages become user content. ADK then owns model/tool progression: the model interprets instructions and user content and proposes tool calls; Python tools execute effects; results re-enter model context. The run wrapper injects memory paths and configurable policy, initializes memory directories and persists trajectories periodically and finally. These persistence operations catch failures; they are not a crash-consistent transaction with tool effects (SRC-1, `src/opensage/patches/agent_run_async.py`).

At the end of a dispatcher invocation, code checks budget/quota and may call a configured `fake_user_fn` to supply another user message. This is automated continuation, not evidence of a human approving each turn. When no continuation remains, the instance is released to sleeping and pending messages can wake it again. Terminal output consists of model/event text and tool-call display, not necessarily an independently checked answer. CLI shutdown cleans up resources or attempts a snapshot when cleanup is disabled. Resume restores session state and instances, but **not pending peer messages**: manager startup truncates persisted inboxes. This limits replay and delivery claims even though `inbox.jsonl` is physically stored (SRC-1, `src/opensage/orchestration/manager.py`, `src/opensage/cli/opensage_cli.py`).

### Delegation and working-context controls

[RT-RTE-directed-child](#rt-rte-directed-child) starts a fresh instance from a registered template or continues an existing one. The calling model chooses the request, mode and optional history/model override; code resolves the template and permitted override. A fresh child normally receives no copied parent history or business state. With `use_parent_history=True`, code deep-copies parent events and non-framework state, falling back to shallow copying a state value when needed. Framework session and memory-directory keys are freshly derived. Thus context isolation is configurable rather than mandatory (SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/orchestration/manager.py`).

The child has its own runner and session, but shares the enclosing environment. A synchronous call returns extracted final text, not the full trajectory. An asynchronous call returns a running acknowledgement and later sends final text or an error to the caller's inbox. The result can arrive at a tool boundary during the caller's work or wake a sleeping caller. Large tool-boundary messages are truncated, with full text saved to a sandbox file when that save succeeds. The consumer therefore does not necessarily receive the complete result inline. There is also an explicit non-dict-result branch that logs dropped messages after popping them (SRC-1, `src/opensage/orchestration/plugins/inbox_delivery.py`).

This resembles a separate task frame: selected inputs enter and a result escapes. It does not pop the child's stored frame on return, ensure resource isolation, or make saved paths automatic references. Continuing the instance reuses its session, and shell access can reach shared files. Parent-window savings therefore depend on input selection and return size, not merely the existence of a child.

Compaction is a different control. [RT-RTE-history-compaction](#rt-rte-history-compaction) describes code-selected older history, model-produced summaries and optional verbatim pinned content. It changes future model context without proving that the summary preserves every relevant fact. Its detailed retained-memory semantics belong to the memory analysis; here the report establishes its runtime trigger, deciding parties and bypass limits (SRC-1, `src/opensage/features/summarization.py`, `src/opensage/plugins/default/adk_plugins/history_summarizer_plugin.py`).

### Guarantees and forcing cases

The inspected guarantee owners and enforcement points have different coverage. None supports a system-wide safety or reliability guarantee.

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate path or required external contract | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| One directed invocation starts only when an instance is sleeping | Manager, `_invoke_instance` atomic check/set | invariant for that admission check; dispatcher also marks running before awaiting | Web `/run_live` sets running without the same busy rejection; direct runners do not enter this manager gate. Single event-loop scheduling is required. | wired | uninspected |
| Dynamic agent model names come from the registry | `create_subagent`, optional `call_subagent` override and registry lookup | invariant within those named lookup paths | Static factories may construct models directly; external RL supplies a model object. Not a universal provider allowlist. | wired | uninspected |
| Stop starting covered calls after observed spend exhausts budget | Budget manager, runner plugin and explicit model wrappers/helpers | best effort soft pre-call guard, not hard billing cap | Concurrent calls can overshoot; response usage and pricing are external contracts. Arbitrary shell/provider calls and custom extension code are not automatically covered. Live connection proxy checks entry but does not itself meter every live response. | wired | uninspected |
| Read before editing | Optional `ReadBeforeEditPlugin` callbacks | policy: tracked tool-name matching and post-edit warning | Shell edits and other tool names are outside the tracked set; plugin deliberately does not block. | wired | uninspected |
| Persist trajectories and recover instances | Run wrapper final/periodic writes; manager load/rebuild; CLI snapshot | best effort, dependent on writable storage and compatible configuration | Pending inboxes are reset; missing models prevent rebuild and missing non-baseline tools are dropped. No exactly-once effects or complete capability equivalence established. | wired | uninspected |

The evidence for these bounds is retained in [RT-CLM-soft-budget](#rt-clm-soft-budget), [RT-RTE-user-dispatch](#rt-rte-user-dispatch), [RT-RTE-live-runner](#rt-rte-live-runner), [RT-RTE-create-subagent](#rt-rte-create-subagent) and [RT-BAP-tool-guidance](#rt-bap-tool-guidance).

Four forcing cases changed or bounded the account:

1. **Restricted child tools versus ambient shell.** Passing a restricted `tools_list` does not create a least-privilege child: baseline terminal and orchestration tools are added regardless. MCP prefix resolution can inject an entire toolset. The registry constrains model choice at that API, not the effects of arbitrary shell commands ([RT-RTE-create-subagent](#rt-rte-create-subagent)).
2. **Live execution versus ordinary dispatch.** Websocket execution uses the instance runner's `run_live` directly. It bypasses inbox-draining/fake-user progression and the directed busy check. The report cannot carry the ordinary manager loop's guarantees unchanged to this path ([RT-RTE-live-runner](#rt-rte-live-runner)).
3. **Direct runner versus manager construction.** The shipped local-support driver constructs its own ADK App/Runner and continuation loop; the vulnerability benchmark also constructs runners with a different plugin set. Import-time OpenSage patches may still apply, but manager-added plugins and dispatch policy cannot be inferred from that import ([RT-RTE-direct-driver](#rt-rte-direct-driver)).
4. **Restart versus durable delivery.** Stored definitions and trajectories can be read back, but startup clears inboxes, a rebuild can drop unavailable tools, and the model name resolves against current configuration. Restart is not faithful replay of every pending message or frozen capability ([RT-RTE-create-subagent](#rt-rte-create-subagent), [RT-RTE-user-dispatch](#rt-rte-user-dispatch)).

### Grants, isolation and change admission

The **capability surface** includes supplied Python functions, MCP toolsets, shell commands, plugins, scripts and subagent creation. The **current grant set** depends on the selected factory, configured models, skills, plugins and available sandboxes. No deployed grant set was supplied. The **isolation envelope** depends on the backend: `LocalSandbox` invokes host `/bin/bash`; native Docker forwards configured user, network, privilege, capabilities, devices and volume binds. The presence of a sandbox abstraction therefore establishes neither host containment nor network denial. Other included backends remain uninspected here; no deployment guarantee is inferred for them (SRC-1, `src/opensage/sandbox/local_sandbox.py`, `src/opensage/sandbox/native_docker_sandbox.py`).

Admission occurs at distinct points. Dynamic instructions become a registered and persisted definition when API validation succeeds; there is no human approval step in that inspected function. Shell-created scripts become executable files without a new Python-function registry admission. Configuration-selected plugins execute host Python on import; bridged hook files supply prompts and sandbox commands but cannot be assumed to preserve Claude Code permission semantics. [RT-RTE-host-extension](#rt-rte-host-extension) records this host trust boundary. These mechanisms can change capabilities and instructions; they do not establish beneficial self-change.

The injected long-term-memory policy requests wiki maintenance after non-trivial subtasks. It names what to write, revise and remove, but its delivery is not an enforced per-entry approval or truth check. The memory analyst owns the objects and actual knowledge-write/read-back routes. This report retains only the runtime policy channel under [RT-BAP-memory-policy](#rt-bap-memory-policy) (SRC-1, `src/opensage/templates/auto_insert_prompts/default.md`, `src/opensage/patches/agent_run_async.py`).

Evaluation is not an admission gate for every ordinary answer. The base evaluation driver uses the manager, records events and imposes timeout/optional continuation controls. Native dispatch can run tasks in separate processes. Benchmark-specific output and reward logic is a later consumer; its mere existence does not prove a reference-answer oracle or improved output. The AReaL adapter supplies a concrete training interface: it accepts a model object, invokes evaluation and returns a reward; the launcher hands control to an external trainer. [RT-RTE-evaluation-rollout](#rt-rte-evaluation-rollout) separates this bounded mode from open CLI tasks and leaves parameter updates, rejection and rollback in the external trainer uninspected (SRC-1, `src/opensage/evaluation/base.py`, `src/opensage/evaluation/dispatchers/native.py`, `src/opensage/evaluation/rl_adapters/adapters/areal.py`, `rl/areal/train.sh`).

Remaining runtime uncertainties are local, not absences: provider-native/server-side tools and provider internals; exact deployed model versions; other sandbox backends and their isolation; benchmark-specific oracle coverage; the external trainer's update/rejection/checkpoint loop; and extension-defined callbacks or subprocess behavior outside the inspected examples. `src/opensage/workflow/spec.py` supplies symbolic sequential/parallel/bounded/loop specifications, but inspection of that data model alone does not establish a separate executing workflow engine. These limits prevent claims of universal enforcement, complete backend equivalence or end-to-end training correctness, without negating the implemented paths above.

## Shared records

### Components

#### RT-CMP-base-llm
Label: BaseLlm model endpoints

Source-native identity: ADK `BaseLlm` objects, ordinarily `LiteLlm`, indexed by `BaseLlm.model` in `LlmRegistry`; foreground, child and summarizer routes use model objects. Representational form: distributed-parametric model state consumed through an API; provider identifiers and configuration are symbolic selectors, not the weights. Storage substrate: external provider or trainer, with local Python objects holding endpoint/configuration state.

Parameters during operation: ordinary inspected OpenSage inference wrappers do not implement a parameter update; external trainer-backed objects may change between rollouts, and provider internals remain uninspected. Exact version pinning: a configured string and optional base URL do not establish an immutable weight version. Mutable endpoint: configuration can resolve the same name to another model or provider state on a later start; external model objects can be supplied directly. No deployed resolution evidence was supplied. Summarization may select `config.llm.summarize_model` or fall back to the agent's canonical model (SRC-1, `src/opensage/llm/registry.py`, `src/opensage/features/summarization.py`, `src/opensage/evaluation/rl_adapters/adapters/areal.py`).

> User-written static agents (in ``mk_agent``) may construct ``BaseLlm`` instances
> directly without going through the registry — that path is unconstrained.
> --- `src/opensage/llm/registry.py`

> Instances are SHARED:
> --- `src/opensage/llm/registry.py`

The second passage is documentation of object sharing, not independent isolation evidence. The executable registry returns the stored model object on lookup.

### Operative objects

#### RT-OBJ-agent-definition
Label: Dynamic agent definition selectors

Source-native identity: the symbolic fields in a dynamic agent's persisted `definition.json`: name, model, tool names and enabled skills. Representational form: symbolic JSON values with fixed builder/lookup rules. Storage substrate: host session `agents/<agent_name>/definition.json`, reconstructed into Python objects. The separate instruction text is [RT-OBJ-agent-instruction](#rt-obj-agent-instruction); it has a different interpreter and authority. No counterpart in the supplied boundary, which declares no shared records.

Evidence: SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/orchestration/persistence.py`. Saved selectors are re-resolved, not serialized executable tool bodies or pinned model weights.

> "model": model_name,  # store the string, not the BaseLlm
> "tool_names": tool_names_final,
> "enabled_skills": enabled_skills,
> --- `src/opensage/toolbox/general/orchestration_tools.py`

#### RT-OBJ-agent-instruction
Label: Dynamic agent instruction text

Source-native identity: `full_instruction` constructed from caller-provided `instruction` plus tooling policy, persisted with the dynamic definition. Representational form: natural language interpreted by the model. Storage substrate: host JSON string, then agent instruction/callable in process and model input. It is not executable Python merely because it is stored beside tool selectors. No counterpart in the supplied boundary.

Evidence: SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/agents/opensage_agent.py`. Consumption authority is [RT-BAP-dynamic-instruction](#rt-bap-dynamic-instruction).

> "instruction": full_instruction,
> --- `src/opensage/toolbox/general/orchestration_tools.py`

### Routes

#### RT-RTE-user-dispatch
Label: User inbox dispatch

Endpoints and progression: operator/CLI or ordinary web request → manager inbox → wake queue → instance runner → model/tool events → session/event consumer. Owner: CLI/web owns input submission; manager owns wake/continuation/release; ADK owns the inner inference/tool sequence; model decides proposed actions. Identities and effects: app/user/session keys select a live ADK session; template name and child parent ID identify topology; tools affect selected external resources rather than only session state. Policy form: symbolic dispatch rules plus natural-language task/instructions interpreted by [RT-CMP-base-llm](#rt-cmp-base-llm).

- Immediate return: CLI waits for idleness and displays polled events; ordinary web `/run` returns `{"ok": True}` after enqueue, not a completed answer.
- Later read-back: saved trajectories/session snapshots can be loaded on resume and consumed by later invocations; the run wrapper refreshes host trajectories, subject to write failures.
- Delegated visibility: peer messages are delivered at tool boundaries or the next invocation; child visibility and result selection follow [RT-RTE-directed-child](#rt-rte-directed-child).
- Selection predicate: addressed known instance, sleeping state and pending inbox; fake-user continuation requires a configured function returning non-null text and remaining budget/quota.
- Invalidation or expiry: manager startup clears inboxes; shutdown drops instances in memory; CLI cleanup may remove resources, while no-cleanup attempts a snapshot.
- Activation or effect: wired submission to ADK and tools; successful task action or reliance on retained content is unobserved.
- Evidence limits: supplied execution evidence is absent; persistence and idleness are not truth or exactly-once effect guarantees; `/run_live` follows a separate route.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open tasks by default; configurable software continuation can extend a turn. Human contribution is initial task/configuration and interactive input, not per-tool approval. Answer oracle: inapplicable — this base CLI/web loop contains no expected-answer/reference-outcome comparison. Recovery: directed failures become results, dispatcher failures are logged, and finally blocks release state and permit re-wake; resume requires compatible saved state and configuration.

Evidence: SRC-1, `src/opensage/cli/opensage_cli.py`, `src/opensage/cli/opensage_web_app.py`, `src/opensage/orchestration/manager.py`, `src/opensage/patches/agent_run_async.py`.

> await manager.send_message(
>     from_sid="__user__",
>     to_sid=session_id,
>     content=prompt,
> )
> await manager.wait_until_idle(session_id)
> --- `src/opensage/cli/opensage_cli.py`

> self._reset_all_inboxes()
> await self._eager_load_from_disk()
> --- `src/opensage/orchestration/manager.py`

#### RT-RTE-directed-child
Label: Directed child invocation

Endpoints and progression: calling model → `call_subagent` → spawn → `_invoke_instance` → per-child runner → extracted text/result; `continue_agent_instance` addresses an existing instance instead. Owner: manager controls instance admission and execution state; caller chooses decomposition, mode, optional history and model override. Executors and effect boundary remain the child runner's granted tools and shared environment, not an isolated host principal.

- Immediate return: sync returns success/failure, session ID and final text; async returns session ID/running acknowledgement and later posts text or error to caller inbox.
- Later read-back: continuing an existing child reuses its session; resume loads trajectory/metadata and may reconstruct its definition.
- Delegated visibility: fresh children omit parent events/business state by default; explicit history inheritance copies them; parent receives selected final text, not all child events. Inbox delivery may truncate oversized text and save a full-file pointer.
- Selection predicate: registered template or known session ID; sleeping check for directed calls; override must name a registered model.
- Invalidation or expiry: instance termination prevents further invocation; process restart resets pending inboxes; restored tool/model availability depends on current configuration.
- Activation or effect: child tool execution is wired; returned text is delivered for caller interpretation, with behavioral influence unobserved.
- Evidence limits: separate contexts do not establish separate tool resources, least privilege or full result delivery; ADK/provider internals were not inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: model proposes delegation, API validates identity/override and manager state can veto a directed start as busy. Operating mode: open request within the caller's task. Answer oracle: inapplicable — child result extraction is not expected-answer checking. Guarantee strength: invariant for the sleeping check at `_invoke_instance`, not for all access to an instance runner.

Evidence: SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/orchestration/manager.py`, `src/opensage/orchestration/plugins/inbox_delivery.py`.

> # Atomic check+set (no await between check and mutation)
> if instance.state != AgentInstanceState.SLEEPING:
>     return {
>         "success": False,
>         "error": self.BUSY_ERROR,
>         "session_id": instance.session_id,
>     }
> instance.state = AgentInstanceState.RUNNING
> --- `src/opensage/orchestration/manager.py`

> events = copy.deepcopy(parent_session.events or [])
> --- `src/opensage/orchestration/manager.py`

> formatted = _truncate_incoming_messages(
>     formatted, _MAX_INCOMING_MESSAGES_CHARS, saved_path
> )
> --- `src/opensage/orchestration/plugins/inbox_delivery.py`

#### RT-RTE-create-subagent
Label: Dynamic subagent admission

Endpoints and progression: model/tool caller supplies name, instruction, model and tools → builder validates and creates `OpenSageAgent` → manager registry and persisted definition → later spawn or rebuild. Owner: builder and manager admit the proposal; foreground model supplies content. Objects are [RT-OBJ-agent-definition](#rt-obj-agent-definition) and [RT-OBJ-agent-instruction](#rt-obj-agent-instruction).

- Immediate return: success with sanitized agent name, tools and description, or an error; creation does not itself run the new agent.
- Later read-back: saved definition reconstructs a missing template on restart, resolving model and tools against the new registry/startup tool snapshot.
- Delegated visibility: the new template is callable within the manager namespace; child instances obtain selected instruction and tools rather than automatically inheriting every parent turn.
- Selection predicate: registered model; non-baseline tools available to caller, with prefix matching able to select an entire MCP toolset; baseline terminal/orchestration tools are unconditional.
- Invalidation or expiry: name collisions/invalid tools reject construction; absent restored models fail; absent restored non-baseline tools are logged and dropped.
- Activation or effect: registration enables later calls and instruction interpretation; successful specialist behavior is unobserved.
- Evidence limits: API validation is not correctness evaluation or least privilege; no observed approval, exercised improvement or equivalent restart capability is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission account: trigger is an exposed `create_subagent` call during open task execution. Proposed change is a new model/tool/instruction template. Model proposes; code decides name/model/tool validity and registers before saving. Human contribution is upstream configuration and task/factory grants; there is no per-definition human veto in the inspected function. Guidance requests tools only under selected skills and continued orchestration through manager tools. Baseline injection broadens even an explicitly restricted tool list. Skill clamping is conditional on both a requested selection and a caller selection, and exact-list comparison is not a universal filesystem access gate. Rejection returns an error. Rebuild is recovery, not a transactional rollback; source does not roll back registration if a subsequent save fails. Persisted content is selectors and instruction, not evaluated improvement evidence. Answer oracle: inapplicable — no reference result checks the proposed agent. Operating mode: open runtime construction; no improvement-trigger score is required.

Evidence: SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/orchestration/manager.py`.

> # Always inject baseline tools
> baseline = _get_baseline_tools()
> for t in baseline.values():
>     if id(t) not in added_ids:
>         tools_to_add.append(t)
>         added_ids.add(id(t))
> --- `src/opensage/toolbox/general/orchestration_tools.py`

> manager.register_agent(agent_name, agent)
> 
> # Persist the definition so we can rebuild on resume.
> save_agent_definition(
> --- `src/opensage/toolbox/general/orchestration_tools.py`

> "rebuild_agent_from_definition: dropping tools %s for agent %r "
> "(not in startup tool snapshot — likely the live agent tree no "
> "longer registers them)",
> --- `src/opensage/toolbox/general/orchestration_tools.py`

#### RT-RTE-terminal-extension
Label: Terminal effects and script extension

Endpoints and progression: model-issued `run_terminal_command` → session sandbox lookup → task manager/background process → output/exit status or watcher message. Owner: model supplies command; Python selects available sandbox and manages process status; backend executes effects. Symbolic executable shell/script content is interpreted by bash, with natural-language skills guiding its construction.

- Immediate return: foreground success/output/exit code after completion; background task ID/running status; a wait timeout can return while the command still runs.
- Later read-back: scripts/files written by commands can be invoked/read later in the same surviving sandbox; no automatic install into the Python tool registry is established.
- Delegated visibility: background watcher can send a completion message to caller inbox; shared sandbox files can be reached by other granted agents.
- Selection predicate: caller specifies sandbox name and command; sandbox lookup must succeed, but tool code forwards the command rather than an allowlisted command vocabulary.
- Invalidation or expiry: task cleanup/kill and sandbox cleanup affect executability; file replacement/removal can revise scripts. Watcher start failures leave manual polling as fallback.
- Activation or effect: arbitrary shell effects, including constructing executable skills, are wired to the selected backend; actual script creation/reuse is unobserved.
- Evidence limits: current deployment grants and containment are unknown; foreground wait timeout is not proof of process termination; shell/provider effects bypass named Python-tool policy coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission account: trigger is a model deciding a script/skill would help, under instruction to compose or copy/adapt skills into `new_tools` rather than edit originals. Proposed change is script and optional `SKILL.md` text. The shell/filesystem admits writes; the model decides content. No per-script evaluator or human approval is present in this inspected path. The runtime can reject missing sandboxes/process startup; backend permissions can reject writes. Recovery is command/file repair or removal, not versioned rollback supplied by this tool. Operating mode: open task automation; answer oracle: inapplicable — exit status tests process success, not a reference outcome for the proposed capability. Guidance and resulting scripts can persist in the writable sandbox; next invocation requires an actual read or execution, not a file label.

Evidence: SRC-1, `src/opensage/toolbox/general/bash_tools_interface.py`, `src/opensage/agents/opensage_agent.py`, `src/opensage/sandbox/local_sandbox.py`, `src/opensage/sandbox/native_docker_sandbox.py`.

> target_sandbox = sandbox_name
> final_command = command
> --- `src/opensage/toolbox/general/bash_tools_interface.py`

> args = ["/bin/bash", "-c", command]
> --- `src/opensage/sandbox/local_sandbox.py`

> if self.container_config_obj.privileged:
>     run_kwargs["privileged"] = True
> --- `src/opensage/sandbox/native_docker_sandbox.py`

#### RT-RTE-host-extension
Label: Host configuration and plugin admission

Endpoints and progression: configured agent directory/model Python file/plugin names and search directories → host import/class validation → factory/model/plugin objects → runner callbacks. Owner: operator or configuration supplier chooses executable input; loader admits structurally valid objects. Authorship is not inferred to be human merely from a pathname. Symbolic Python executes on the host; prompt/hook content can later receive model interpretation.

- Immediate return: agent factory callable or instantiated plugins/models, with load errors for missing/invalid definitions.
- Later read-back: configuration and plugin files are imported on later starts; hook prompt context can also be persisted into session history by its bridge.
- Delegated visibility: manager runners receive configured base plugins; dynamic child rebuild resolves tool names against the startup snapshot rather than serializing extension bodies.
- Selection predicate: supplied directory and enabled literal/regex plugin names; later search directories can shadow earlier ones; Python loader requires a single `BasePlugin` subclass.
- Invalidation or expiry: editing/removing configuration or plugin files changes the next load; disabled selection excludes plugin loading. No versioned extension rollback was established.
- Activation or effect: host code execution on import and later callbacks is wired, including authority outside model-tool mediation.
- Evidence limits: no installed custom extension or grant set was supplied; Claude Code hook denial/permission fields are documented as unbridgeable, not an inherited approval system.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission account: proposed change is trusted host code/configuration, selected before agent execution; software validates interface shape and performs import, not semantic safety. A human can select/disable configuration, but the inspected loader supplies no interactive content approval. Rejection is missing/ambiguous class, unknown name or import error. Recovery requires operator/configuration repair or replacement. Operating mode: configuration/startup; answer oracle: inapplicable — interface checks are not reference-outcome comparison. Persisted guidance is Python, config and hook text; arbitrary extension internals can alter callbacks or call providers independently, so manager-tool guards do not establish universal mediation.

Evidence: SRC-1, `src/opensage/cli/opensage_cli.py`, `src/opensage/llm/registry.py`, `src/opensage/plugins/__init__.py`, `src/opensage/plugins/adk_plugin_loader.py`, `src/opensage/plugins/claude_code_hook_loader.py`.

> module = importlib.util.module_from_spec(spec)
> spec.loader.exec_module(module)
> --- `src/opensage/plugins/adk_plugin_loader.py`

> "permissionDecision": (
>     'CC "permissionDecision" (deny) cannot be bridged — ADK cannot '
>     "prevent tool execution."
> ),
> --- `src/opensage/plugins/claude_code_hook_loader.py`

The last passage is the bridge's declared compatibility limit, not a claim about every possible ADK plugin's blocking capabilities.

#### RT-RTE-history-compaction
Label: History compaction control

Endpoints and progression: enabled history plugin after event append → folded-history character calculation → code-selected older candidate window → summarizer model → `EventCompaction` appended to session → later ADK content construction. Owner: code decides trigger/window and admission of non-empty content; model produces summary. This is context transformation, not a documented theory-revision loop.

- Immediate return: callback returns no replacement event; a compaction event may be appended, or the function skips when conditions/summary fail.
- Later read-back: later invocations can receive folded history including the summary; trajectory persistence is attempted immediately after append.
- Delegated visibility: summary stays in the affected session; inherited history can carry that session material to a child when requested.
- Selection predicate: configured effective character budget exceeded; branch-matching uncompacted candidates; configured percentage of older events, ending at a tool-call/response-balanced cut; windows of at most two events are skipped.
- Invalidation or expiry: later compactions expand coverage over earlier compaction ranges; pinned file edits affect later pin reads. Exact durable-memory replacement semantics are left to the memory analyst.
- Activation or effect: reduced/reconstructed model-visible history is wired through compaction events; relevance preservation and behavioral benefit are unobserved.
- Evidence limits: enabled-plugin and ADK folding contracts are required; character counting and window checks do not guarantee a hard provider-token bound; pin read or summary generation can fail.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code proposes/selects the window and can skip; runtime model drafts summary; non-empty-result code admits it. No per-summary human approval or answer oracle appears in this path. Operating mode: automatic threshold-triggered control during open tasks/evaluation. Guidance is summarizer prompt plus verbatim pinned operational strings; what persists is summarized history and compaction metadata, not evidence that criticized theories were revised. Remaining recent material is outside the selected compaction window; full original history is not guaranteed to remain in the model window. Source-native persistence/reload details require the memory analysis.

Evidence: SRC-1, `src/opensage/features/summarization.py`, `src/opensage/plugins/default/adk_plugins/history_summarizer_plugin.py`.

> trigger_by_budget = effective_budget is not None and total_chars > effective_budget
> --- `src/opensage/features/summarization.py`

> if len(window_events) <= 2:
> --- `src/opensage/features/summarization.py`

> await session_service.append_event(session=session, event=compaction_event)
> --- `src/opensage/features/summarization.py`

#### RT-RTE-live-runner
Label: Websocket live runner

Endpoints and progression: websocket `/run_live` → session lookup/live request queue → instance runner `run_live` → streamed event JSON. Owner: web handler coordinates input/output tasks; ADK/provider owns live interaction. Context/state are the selected existing session and live requests, not manager-drained inbox batches.

- Immediate return: event stream over websocket until error/disconnect/cancellation; not the ordinary `/run` enqueue acknowledgement.
- Later read-back: uninspected — this handler's live persistence and subsequent model-context reconstruction depend on ADK live execution; ordinary run-async patch evidence does not establish them.
- Delegated visibility: uninspected — live tool-boundary peer delivery depends on external live callback behavior; this handler does not run the manager inbox/continuation loop.
- Selection predicate: matching app and existing session; retrieves an instance, then starts live tasks and assigns running state without the directed sleeping check.
- Invalidation or expiry: disconnect/error cancels input/output tasks and restores sleeping state; UI cancellation closes the websocket.
- Activation or effect: live model/tool interaction is wired by the runner call; deployment protocol and effects are unobserved.
- Evidence limits: ADK live internals and provider contracts are outside the frozen implementation; the handler alone cannot establish normal-dispatch guarantee coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open interactive text/audio stream. Answer oracle: inapplicable — the handler streams events without a reference-answer comparison. Model identity follows instance configuration, but complete live-budget accounting is uninspected; the registry wrapper's `connect` checks availability at connection entry only.

Evidence: SRC-1, `src/opensage/cli/opensage_web_app.py`, `src/opensage/llm/budget.py`.

> runner.run_live(
>     session=session, live_request_queue=live_request_queue
> )
> --- `src/opensage/cli/opensage_web_app.py`

> def connect(self, llm_request):
>     self._budget_manager.check_available()
>     return self._inner.connect(llm_request)
> --- `src/opensage/llm/budget.py`

#### RT-RTE-direct-driver
Label: Shipped direct-runner drivers

Endpoints and progression: local-support CLI input → direct App/Runner → event trace and optional repeated continuation; vulnerability-memory benchmark input → inner Runner with retry plugin → accumulated response/reasoning. Owner: each shipped driver controls runner construction and stopping; ADK controls model/tool execution.

- Immediate return: local driver collects/writes trace and closes runner; benchmark accumulates textual response and reasoning for task processing.
- Later read-back: local saved trace is produced, but uninspected — this selected driver range does not establish later trace-fed admission or future behavior; included memory benchmark retention requires specialist analysis.
- Delegated visibility: manager inbox/child delivery is not established by these direct Runner constructors; actual tool sets and imported patches remain separately relevant.
- Selection predicate: driver-selected agent/session; local continuation checks `task_finished` and remaining call quota; benchmark uses a per-run `RunConfig`.
- Invalidation or expiry: runner close, quota exhaustion or task-finished state stops the local continuation loop; errors can leave partial trace/output.
- Activation or effect: direct model/tool progression is wired without entering manager dispatch; actual task completion and quota reliability are unobserved.
- Evidence limits: supplied execution evidence is absent; manager budget/inbox plugins must not be assumed present just because the driver imports OpenSage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: driver code decides continuation by session flag and quota; the local model can set task completion through a tool. The static continuation text saying approval is software-generated, not a newly observed human decision. Operating mode: open task with optional finish-until-complete loop, or benchmark task. Answer oracle: uninspected — benchmark-specific outcome checks are not established by the inspected direct-runner ranges; local trace collection itself is not an oracle.

Evidence: SRC-1, `agent_library/local_support/local_cli.py`, `benchmarks/secodeplt/vul_detection_memory.py`.

> runner = Runner(
>     app=app,
>     session_service=session_service,
> )
> --- `agent_library/local_support/local_cli.py`

> plugins=[
>     ReflectAndRetryToolPlugin(max_retries=3),
> ],
> --- `benchmarks/secodeplt/vul_detection_memory.py:884-892`

#### RT-RTE-evaluation-rollout
Label: Evaluation and AReaL rollout interface

Endpoints and progression: dataset/task driver or external AReaL caller → evaluation task with optional supplied model → manager-driven execution → collected outputs → benchmark reward → returned result; training launcher then executes the external trainer's script. Owner: evaluation owns task setup/timeout/collection, benchmark supplies reward function, external trainer owns parameter update and subsequent model provision. Native dispatcher can use separate processes rather than shared concurrent tasks in one manager.

- Immediate return: session/output/result and AReaL reward; adapter errors return error with zero reward rather than proof of successful rollout.
- Later read-back: traces/results are retained for external evaluation/training consumers; actual checkpoint update and later trained-model reuse are uninspected beyond the integration contract.
- Delegated visibility: evaluation uses manager registration/spawn and task inbox; native multiprocessing returns worker results to aggregation; external model object receives provider-side interactions under its own contract.
- Selection predicate: dataset task and selected benchmark; optional fake-user/quota and timeout controls; AReaL task receives the supplied model and reward function is used when available.
- Invalidation or expiry: timeout stops active agent work before collection; task cleanup/configuration governs resource lifetime; external trainer checkpoint expiry/rollback is uninspected.
- Activation or effect: execution/collection/reward delivery are wired; parameter learning, improved capacity and exercised training benefits are unobserved.
- Evidence limits: benchmark reward/reference correctness, provider interaction tracking and trainer updates are not established by this adapter; no causal experiment or observed training run was supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles and oracle: software supplies benchmark tasks and computes reward; concrete reference-outcome providers depend on the benchmark and remain uninspected here. A model judgment alone is not an oracle. Human supplies benchmark/model/configuration and starts the process; this is not per-rollout content approval. Operating mode: bounded dataset/training rollouts, distinct from open CLI requests. Improvement trigger: returned benchmark reward is available to the external trainer, but its use for successor selection is outside inspected implementation.

Admission account: parameter-change proposal, acceptance/rejection and rollback belong to the external trainer and are uninspected. The OpenSage-side change is replacement of task model input with the supplied object and export of outcomes. Guidance is task/benchmark prompts and configuration; retained evidence is traces and reward, with no OpenSage-side rule in the inspected adapter that admits a trained checkpoint into production. This supports an integration path, not exercised self-improvement of the enclosing runtime.

Evidence: SRC-1, `src/opensage/evaluation/base.py`, `src/opensage/evaluation/dispatchers/native.py`, `src/opensage/evaluation/rl_adapters/adapters/areal.py`, `src/opensage/evaluation/rl_adapters/client.py`, `rl/areal/train.sh`.

> task.model = model
> 
> # 4. Run agent using Evaluation._generate_one
> result = await self.evaluation._generate_one(task)
> 
> # 5. Compute reward using benchmark's reward_func
> reward = await self._compute_reward(data, result, model)
> result["reward"] = reward
> --- `src/opensage/evaluation/rl_adapters/adapters/areal.py`

> cd "$AREAL_DIR"
> exec bash examples/opensage/run_opensage_grpo.sh "${ARGS[@]}"
> --- `rl/areal/train.sh`

### Claims

#### RT-CLM-runtime-creation
Label: Runtime creation claim

Claimed operation: model creates topology, toolsets and memory with a minimal scaffold. Source: SRC-1 doctrine/design, `README.md`. Concrete supporting affordances are dynamic-agent registration, shell extension and injected memory policy. The claim does not itself establish exercised creation, useful decomposition or improvement.

> Instead of requiring developers to hand-craft agent topology, tool lists, and memory, OpenSage-ADK provides a minimal scaffold that lets the model **create** and **orchestrate** these components at runtime.
> --- `README.md`

#### RT-CLM-soft-budget
Label: Soft budget enforcement scope

Claimed operation: covered model calls check shared available budget before starting; usage-bearing responses update spend. Owner: `BudgetManager`, `RuntimeBudgetPlugin`, registry proxy and `generate_content_with_budget`. Enforcement: pre-model callback or wrapper/helper call, with response accounting. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected.

Covered paths: manager-built runners attach budget plugin when a budget object exists; registry-wrapped model generation and OpenSage summarization with a session budget use explicit guards. External contracts: response usage metadata, cost/pricing resolution and provider call behavior. Alternative paths: direct runner constructors with different plugins, unwrapped static models, host extensions, arbitrary shell calls and live connections. Only actual wrapper/plugin wiring supplies coverage; a registry name restriction is not universal mediation.

Evidence: SRC-1, `src/opensage/orchestration/manager.py`, `src/opensage/llm/registry.py`, `src/opensage/llm/budget.py`, `src/opensage/plugins/default/adk_plugins/runtime_budget_plugin.py`, `src/opensage/features/summarization.py`.

> This is a pre-call guard, not a hard billing cap. Final cost is only
> known after an LLM response returns, so one in-flight call or concurrent
> calls can push ``spent_cost`` past ``configured_budget`` before later
> calls are blocked.
> --- `src/opensage/llm/budget.py`

> if usage is None:
>     return None
> --- `src/opensage/plugins/default/adk_plugins/runtime_budget_plugin.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-dynamic-instruction
Label: Dynamic instruction authority

Consumer: child model reached through a spawned/rebuilt `OpenSageAgent`. Channel: model instruction, supplied from persisted natural-language `full_instruction`. Force: interpreted behavioral guidance, not an invariant or a tool permission check. Horizon: subsequent calls/instances and restart while the definition can be rebuilt. Evidence: SRC-1, `src/opensage/toolbox/general/orchestration_tools.py`, `src/opensage/agents/opensage_agent.py`; [RT-OBJ-agent-instruction](#rt-obj-agent-instruction) retains the write witness and [RT-RTE-create-subagent](#rt-rte-create-subagent) the admission mechanism. Loading does not prove compliance or theory consumption.

#### RT-BAP-tool-guidance
Label: Skill and edit guidance

Consumer: foreground/child model. Channel: constructor-generated skill/policy instructions and optional plugin warnings in tool responses. Force: policy, not enforced prohibition against editing unread files or modifying existing scripts. Horizon: current agent instructions and later turns receiving tool warnings; file-created capabilities can outlive a turn separately. Evidence: SRC-1, `src/opensage/agents/opensage_agent.py`, `src/opensage/plugins/default/adk_plugins/read_before_edit_plugin.py`; executable effect channel is [RT-RTE-terminal-extension](#rt-rte-terminal-extension).

> Does NOT block execution — the agent may have read the file via
> run_terminal_command (cat/head), which we can't track, so blocking would
> cause false positives.
> --- `src/opensage/plugins/default/adk_plugins/read_before_edit_plugin.py`

> "- Do NOT edit existing `/bash_tools/...` Skills in place. If you need changes, copy/adapt into a new "
> "Skill/script under `/bash_tools/new_tools/<tool_name>/` (with a `SKILL.md`). You can use "
> --- `src/opensage/agents/opensage_agent.py`

#### RT-BAP-memory-policy
Label: Injected memory maintenance policy

Consumer: the model agent at invocation. Channel: configured/default natural-language policy appended into instruction by the run-async wrapper. Force: requested wiki maintenance and pinned-memory behavior, not a semantic admission gate. Horizon: each invocation's injected instruction; resulting knowledge writes and their later read-back require the memory analyst's separate records. Evidence: SRC-1, `src/opensage/patches/agent_run_async.py`, `src/opensage/templates/auto_insert_prompts/default.md`.

> 3. If you found an existing entry to be wrong or stale, update or remove it
>    (and its index line) instead of leaving the contradiction.
> --- `src/opensage/templates/auto_insert_prompts/default.md`

The policy identifies a requested content-directed revision, but there is no supplied operation evidence that a particular claim was criticized, revised and relied on next. It therefore does not by itself establish a theory builder, reflection, learning or self-improvement. These properties must be assessed on the actual retained knowledge/update route rather than inferred from policy delivery.

## Annotations

none
