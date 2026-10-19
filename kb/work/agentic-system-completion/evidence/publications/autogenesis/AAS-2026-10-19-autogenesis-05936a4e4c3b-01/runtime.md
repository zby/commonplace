---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Autogenesis runtime baseline: Gateway tasks, model-driven delegation, workflow execution and extension admission at the frozen commit."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis runtime report

## Runtime account

### Evidence and claimed work

The [boundary](boundary.md) fixes SRC-1, its whole-system scope and its implementation and doctrine/design layers. This report inspects source, not a running installation. No target code, tests, examples, provider calls or experiments were executed. All operation and benefit conclusions remain uninspected. Additional coverage within SRC-1 includes native-tool assembly, protocol delegation, tool and skill consumers, permission resolution, dynamic Python loading, replay smoke checks, canvas persistence and workflow resume. These are implementation evidence; prompts and the self-evolution playbook are design evidence, not execution traces.

Autogenesis claims to complete user tasks by model-selected tools, sub-agents, skills and connectors, and to generate or optimize its own capabilities when existing means fail. The shipped console is `autogenesis.cli:main`; `autogenesis serve` defaults to `configs/meta_agent.py` and can use stdio or WebSocket transport. Non-loopback WebSocket launch requires a token in the launcher. This launch-time check is not a complete authentication audit (SRC-1, `pyproject.toml`, `autogenesis/cli.py`). Direct Python examples are also shipped drivers, not excluded hosts. Their task submission and teardown remain inside this analysis ([RT-RTE-direct-agent](#rt-rte-direct-agent)).

### Ordinary Gateway task, end to end

A client opens a session and submits nonempty content, optional workspace-contained file paths and a conversation identity. Gateway binds project roots before task submission, records the task through the task manager and immediately returns task and conversation IDs. Startup initializes managers and one task worker. The worker selects `meta_agent`, copies the conversation ID into context identity and supplies the public task ID; project identity still determines shared workspace and output roots (SRC-1, `autogenesis/gateway/service.py`).

The agent manager resolves a registered instance/version and invokes it through the runtime. Runtime owns spawn, mailbox, reply future and final stop. `Agent.on_start` keeps a run under its runtime-reference name, emits memory/trace/trajectory lifecycle hooks and advances the first round. Each round checks steps and constraints, assembles template messages and current memory, projects capability schemas, then streams the configured model. The model chooses function names and arguments; code owns routing, hook decisions, execution and terminal bookkeeping ([RT-RTE-gateway-task](#rt-rte-gateway-task), [RT-CMP-model-manager](#rt-cmp-model-manager)).

> ref = await self.spawn(agent, name=name)
> --- `autogenesis/runtime/server.py`

> return await runtime_manager.invoke(agent_instance, **input, **agent_args)
> --- `autogenesis/agent/context.py`

Messages are rebuilt each round, rather than merely appending every previous provider message. They include task/files, time and step, selected memory, prior errors, constraint status, todo content, workspace snapshot and capability instructions. Memory delivery depends on `use_memory`, a configured backend instance and `ctx.id`; retrieval exceptions leave the placeholder. This establishes a context supply point, not completeness of recalled history or backend restart recovery (SRC-1, `autogenesis/agent/types.py`; memory revision mechanisms are left to the memory analyst).

> mem_text = await memory_info.instance.get(
>                         session_id=session_id,
>                         short_term_n=self.review_steps,
>                     )
> --- `autogenesis/agent/types.py`

MetaAgent widens the roster to agents. Concurrent function calls become background action tasks; completions return through its mailbox, and the next normal decision waits for the batch to drain. Each action passes trace PRE_ACTION; an explicit hook block prevents that dispatch. Results and errors reach post-action memory/trace/trajectory hooks. Delegation creates a separate child context and returns the child's response message, not its full internal context ([RT-RTE-child-delegation](#rt-rte-child-delegation)). Workflow, connector, environment and ordinary tool branches invoke their respective managers. A skill call is different: it returns methodology text to the caller, not a separately executed skill worker ([RT-RTE-skill-delivery](#rt-rte-skill-delivery)).

Normal model-driven completion is an explicit `done_tool` outcome. Text-only turns are nudged and spend another step. Limits, cancellation and no-progress controls can also terminate without completion. `_conclude` cancels remaining action tasks, emits stop hooks, constructs a Response, runs specialization finalization and resolves the reply. Gateway publishes `task.completed` when the agent call returns, including its payload; that event name alone does not establish `response.success` or deliverable correctness. Errors and cancellations have separate events (SRC-1, `autogenesis/agent/types.py`, `autogenesis/gateway/service.py`).

> success = run.done and not run.stopped_by_constraint
> --- `autogenesis/agent/types.py`

A consequential countercase is MetaAgent's additional repeated-batch stop: it sets `run.done = True` while its result says the task is incomplete. Thus success is a runtime return classification, not an answer oracle. The base no-progress stop instead sets `done = False`. Review and browser verification are prompt instructions, not universally required code gates (SRC-1, `autogenesis/agent/actor/meta_agent.py`, `autogenesis/agent/types.py`, `autogenesis/prompt/default/meta_agent.html`).

### Controls and forcing cases

The following four forcing cases bound the control conclusions. The intended guarantee, enforcement and external contract are distinct from observed deployment.

| Case | Owner, enforcement and strength | Covered and alternate paths; conclusion |
|---|---|---|
| Capability selection and delegation | Native-tool assembler plus `_run_one`; invariant for rejecting names outside that round's routing table. Context allowlists select schemas and prompt rosters. | Gateway session selections are validated against available names and copied to context allowlists. But child delegation constructs a fresh context and copies only explicitly supplied non-null allowlists, plus target-derived defaults. Parent grant intersection is not performed there. Schema visibility is not a process-wide authority boundary. External contract: callers/child defaults must supply the intended restrictions. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Read-only agent with Bash or extension code | Agent dispatcher denies five named mutating tools; individual tools own operation checks. Policy, not an OS isolation invariant. | `bash_tool` is not in the dispatcher deny set. Bash checks permission by its own tool name; default meta configuration imports its `danger_full_access` mode. Tool manager binds arguments and times out invocation but does not generally apply the calling agent's permission mode. Extension Python executes in process. External contract: restricted tool grants/configuration and deployment isolation. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Smoke-gated extension versus explicit false/restore | Extension manager defaults smoke on after live registration/archive/manifest write; protocol with optional bypass, not pre-execution quarantine. | Gateway promotion forwards `params.get("run_smoke")`, so a supported request with false reaches the disabling branch. Rollback reloads an archived version without smoke/evolvability enforcement. Default probe runs `general_agent`, not necessarily the changed component. External contract: restore provenance, useful probes and reversible external effects. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Graph/direct-model alternatives | Workflow runtime owns schema checks, traversal and checkpoints; model-chat handler owns a separate stream. Protocols scoped to their own entry paths. | Canvas caller supplies a graph; workflow execution calls managers directly, not agent `_run_one`. Model chat streams messages without an agent tool list and does not pass through task completion/reviewer gates. ProceduralAgent runs code once instead of the LLM round loop. No claim that every shipped operation shares the model-agent controls. Implementation conclusion status: wired. Operation conclusion status: uninspected. |

Evidence for these cases is retained in the route records below. Actual installed grants, credentials, remote MCP behavior, provider-native facilities, container mounts and deployed access policy were not supplied. The capability surface includes shell, writable files, generated Python and remote connectors; the current grant set is configuration/session/context dependent. A `ProjectSandbox` computes and creates directories and describes mounts; that object alone does not install an OS isolation boundary. Bash uses a bound peer sandbox when present, otherwise starts a local subprocess in the workspace. Comments assuming the runtime already runs in a project container cannot establish that deployment here (SRC-1, `autogenesis/sandbox/project.py`, `autogenesis/tool/default/bash.py`).

The explicit human-approval claim is likewise narrower than its wording: the prompt says staged capabilities require explicit user approval, while generator finalization can promote and register through software. Gateway's `approval.respond` endpoint publishes an event but has no approval rendezvous. A separate client-issued promotion command exists; issuing it does not prove human authorship or per-artifact review. See [RT-RTE-extension-admission](#rt-rte-extension-admission) and [RT-CLM-evolution-guidance](#rt-clm-evolution-guidance).

### Change admission and remaining limits

The concretely traced generated-tool path is successful generator/optimizer response → registration hook → locate file → validate/promote when staged → extension manager → active manager registration → strict archive and manifest → optional replay smoke → notification. This generated-tool path changes live capability machinery, not only a user work product. Do not generalize its usable later consumer to every module: memory-class extension registration stores a configuration with instance=None, and the inspected extension path does not build it. Lifecycle-memory hooks and agent prompt reads skip that configuration until a live instance is supplied. Import and constructor effects still occur, and archive/manifest retention still applies. Instance registration and explicit/startup build paths can provide live memory instances ([RT-RTE-extension-admission](#rt-rte-extension-admission)). Frozen-name protection applies to the paths and modules actually checking it; prompts explicitly carry no such flag. Python loading precedes the class-name evolvability check, so rejection is not prevention of import-time effects. The smoke gate can revert registration but cannot undo arbitrary external effects (SRC-1, `autogenesis/extension/server.py`, `autogenesis/dynamic/server.py`).

The playbook proposes failure diagnosis, generator/optimizer, scored evaluator, with-versus-baseline actor probes and keep/rollback decisions. The prompt carries much of this guidance directly. It is not a mandatory evaluator-approval transaction. In addition, MetaAgent inherits the base worker-only skill-type selector in the inspected class, whereas `self_evolving_skill` is tagged orchestrator. Native schema and skill-summary filters therefore do not expose that skill through the ordinary worker-type projection, despite its presence in the configuration and prompt. This does not remove the directly supplied evolution prompt or the generator capabilities. It limits the claim that the playbook itself is routinely callable in this snapshot (SRC-1, `autogenesis/agent/actor/meta_agent.py`, `autogenesis/agent/types.py`, `autogenesis/agent/native_tools.py`, `autogenesis/skill/server.py`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`).

Inspected wiring establishes an improvement-directed self-change capacity. It does not establish exercised self-improvement: no supplied run closes objective-bearing evidence → chosen update → live organization change → later behavior causally depending on it. In particular the last link and comparative outcome benefit are unobserved. This conclusion is independent of whether a retained instruction qualifies as a theory or whether a memory path retains experience.

Workflow checkpoints provide a separate durable execution route, and canvas JSON provides caller-authored reusable orchestration. Resume rejects unequal nonempty program hashes, but accepts hashless checkpoints after runtime-major and workflow name/version checks, stamps the current hash and can reuse completed invocations without verifying their original executable identity. Neither durable route is evidence that all agent runs resume their mailbox state after restart ([RT-RTE-workflow-execution](#rt-rte-workflow-execution)). The filesystem-memory path, specialized memory evolution, knowledge/data/process pipelines, individual domain/environment implementations, model provider serializers and frontend behavior beyond boundary-supplied entry-path evidence are not exhaustively inspected here. Their availability is not an evidenced absence. This report establishes the shared execution and admission baseline; it does not warrant universal memory, safety, provider-tool coverage or performance claims.

## Shared records

### Components

#### RT-CMP-model-manager
Label: Model manager and remote language models

Source-native identity: `model_manager`, its ModelConfig registry and provider clients. Registry/configuration and canonical stream events are symbolic Python/Pydantic data in process; model content is distributed-parametric state behind external provider endpoints. SRC-1, `autogenesis/model/server.py`, `autogenesis/model/context.py`, `configs/base.py`, `configs/agents/meta_agent.py`.

The ordinary MetaAgent uses `google/gemini-3.1-pro-preview`. The same manager can serve named roles (main/judge/summarize/smoke), explicit names and runtime model registrations. Parameters changing during operation: uninspected at the providers; the inspected manager routes inference and changes configurations, not training weights. Exact numerical model version pinned: no immutable weight/build identity is supplied by this model name or the client registration. Mutable endpoint resolving to another model: possible through external alias resolution and local runtime re-registration; configured stream fallback can also select another registered model. Provider internals and actual endpoint resolution are uninspected. These limits apply separately to the ordinary model and role-selected smoke model, which can resolve to the same configured model or another one.

> if roles.get("main"):
>                 return roles["main"]
> --- `autogenesis/model/server.py`

Stream retry/fallback applies only before the first event. Mid-stream failure propagates; Agent `_think` catches exceptions and can return empty or incomplete decision data rather than a completed answer (SRC-1, `autogenesis/model/context.py`, `autogenesis/agent/types.py`).

> if started:
>                         # Already emitted output downstream — restarting would
>                         # duplicate it, so surface the error instead.
> --- `autogenesis/model/context.py`

### Operative objects

#### RT-OBJ-extension-manifest
Label: Extension manifest and archives

Source-native identity: extension manager manifest components and per-component archived versions. Symbolic JSON names/module/version/file fields on disk select active Python, prompt, skill, connector and workflow artifacts; those artifacts retain their own encoding and consumers. This object is registry/recovery metadata, not itself learned model parameters or a quality certificate. Its admission route is [RT-RTE-extension-admission](#rt-rte-extension-admission); SRC-1, `autogenesis/extension/server.py`.

> self._ensure_archived(module, name, abspath, comp.version)
>                 self._write_manifest(manifest)
> --- `autogenesis/extension/server.py`

#### RT-OBJ-skill-content
Label: SKILL.md content

Source-native identity: `skill_config.content`, originating in SKILL.md, in filesystem directories and the in-process skill registry. Natural-language method text is interpreted by the calling model; symbolic frontmatter/schema/type tags control registration and selection. Script/resource names are exposed as text, not automatically executed by skill invocation. [RT-RTE-skill-delivery](#rt-rte-skill-delivery) distinguishes this consumer from Python tools. SRC-1, `autogenesis/skill/context.py`, `autogenesis/skill/server.py`.

> """Execute a skill by returning its SKILL.md as instructions for the calling agent."""
> --- `autogenesis/skill/context.py`

### Routes

#### RT-RTE-gateway-task
Label: Gateway task execution

Endpoints and owner: client `task.submit` → Gateway/task queue → agent manager/runtime → MetaAgent model decisions → capability managers → Response and Gateway events. Gateway owns project/conversation/public-task identities; runtime owns reference/inbox/reply identity; model owns next capability choice under prompt guidance, subject to code checks. Context combines supplied task, selected retained state and capability roster. State includes per-run counters/outstanding actions, configured roots and task/conversation records. Operating mode: open user requests, not a fixed curriculum. Proposer: client supplies the task; model proposes action batches; code/hooks can reject dispatch. Human contribution: task/configuration supply is possible but no per-action human gate is required. Answer oracle: none generally supplied; model `done_tool` is an asserted answer, not independent correctness evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: submission returns task_id and conversation_id; final agent Response arrives through task completion events and persisted task state.
- Later read-back: subsequent rounds explicitly request memory for ctx.id; conversation/project state also supports later client reopening. Backend-specific retention/reload completeness is not established here.
- Delegated visibility: selected child task/files and explicit allowlists, not the parent's whole model transcript; see child route.
- Selection predicate: registered meta_agent; session capability selections copied to context; tool names must occur in the assembled routing table.
- Invalidation or expiry: max steps, resource constraints, cancellation and no-progress stops bound runs; memory expiry is backend-specific and uninspected in this route.
- Activation or effect: capability managers can modify workspace, call services or admit extensions; delivery and dispatch are wired, actual effects in a run are unobserved.
- Evidence limits: no supplied task trace or correctness measurement; successful Response and task.completed are not proofs of completion.

SRC-1, `autogenesis/gateway/service.py`, `autogenesis/agent/context.py`, `autogenesis/runtime/server.py`, `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`.

> task_id = str(kwargs.pop("task_id", "") or make_id())
> --- `autogenesis/agent/types.py`

> if route is None:
>                 raise ValueError(f"Unknown tool '{call.name}' (not in the assembled tool set)")
> --- `autogenesis/agent/types.py`

The guarantee owner is the agent dispatcher, strength invariant for this route's unknown-name rejection only. It does not cover direct manager invocation, arbitrary generated Python or shell internals. Parallel batches assume independent actions; no inspected dependency proof establishes that a model obeys that assumption.

#### RT-RTE-child-delegation
Label: Child delegation and escalation

Endpoints: agent-kind native tool → protocol manager → fresh AgentContext/runtime invocation → child Response → parent action result. Protocol manager owns lineage and context allocation; child model owns its local decisions. Parent model supplies self-contained task and optional files/target/allowlists. A missing child or unsuccessful Response becomes a parent action error. No mandatory human contribution or external answer oracle. Operating mode: task-directed open subtasks, including evaluators/generators when selected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: successful child response.message becomes the parent action result; failure raises into action error handling.
- Later read-back: child context gets a new id; parent hooks can retain the returned message for a subsequent round. Full child transcript read-back is not supplied by delegate itself.
- Delegated visibility: task, existing file paths, target prefix and non-null explicit or target-default allowlists; parent_ref supplies escalation lineage. Entire parent memory is kept out of the new context.
- Selection predicate: registered agent selected from the parent's roster; protocol copies provided restrictions without intersecting them with parent allowlists.
- Invalidation or expiry: runtime invoke stops its reference in finally; escalation waits at most 300 seconds and returns graceful-stop guidance on failure/timeout.
- Activation or effect: child tools can act in the shared runtime/workspace; parent receives only return text and escalation/progress channels, so context separation is not effect isolation.
- Evidence limits: no observed child invocation or successful escalation; inherited permissions beyond explicit allowlists are not established.

SRC-1, `autogenesis/protocol/server.py`, `autogenesis/agent/types.py`, `autogenesis/runtime/server.py`, `autogenesis/agent/actor/meta_agent.py`.

> effective_allowlists = dict(allowlists or {})
> --- `autogenesis/protocol/server.py`

> for key, val in effective_allowlists.items():
>             if val is not None:
>                 ctx.extra[key] = val
> --- `autogenesis/protocol/server.py`

The working-context mechanism resembles a separate frame: a small task is pushed and return text escapes; shared files, registrations and services break any analogy with isolated private state. Mid-round escalation triggers a focused parent think call; MetaAgent extracts a matching reply and otherwise sends default guidance. This is computational guidance, not human approval.

#### RT-RTE-direct-agent
Label: Direct drivers and shell execution

Endpoints: shipped Python driver → manager initialization/task queue → general_agent → same runtime mailbox loop; within a selected Bash call, permission check → peer sandbox or local subprocess. Owners are driver/task manager for scheduling, model for action choice and BashTool for execution. The direct example's CLI accepts task/config options and polls terminal task state. Operating mode: open supplied tasks. Answer oracle: none required; shell exit code is a diagnostic, not task correctness. Caller supplies configuration; no per-command human approval is required.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: agent Response returns through driver task state; Bash response contains stdout/stderr and exit code.
- Later read-back: logs/task outputs are persisted by configured managers; next model context depends on its memory setup, not guaranteed raw stdout replay.
- Delegated visibility: inapplicable — this entry uses the leaf agent directly; the Bash subprocess sees environment and workspace, not a separate model context.
- Selection predicate: example config tool_names and per-context tool allowlists select callable tools; Bash permission checks use the tool's registered name.
- Invalidation or expiry: Bash timeout kills the local process group; tool manager has its own timeout; normal runtime invocation stops its agent reference.
- Activation or effect: shell runs in current runtime environment when no peer sandbox is bound; working-directory selection does not itself confine filesystem/network effects.
- Evidence limits: no executed command, installed grant set or container boundary was observed. A local nonzero exit is still tool success when execution completed.

SRC-1, `examples/run_general_agent.py`, `autogenesis/tool/default/bash.py`, `autogenesis/tool/context.py`, `autogenesis/permission/context.py`, `configs/meta_agent.py`, `configs/tools/bash.py`, `autogenesis/agent/types.py`.

> permission_mode = "danger_full_access",
> --- `configs/tools/bash.py`

> if enforcer is None:
>             return ValidationResult.allow()
> --- `autogenesis/permission/context.py`

> process = await asyncio.create_subprocess_shell(
> --- `autogenesis/tool/default/bash.py`

The coarse read-only agent policy covers write_file_tool, edit_file_tool, git_tool, deploy_tool and evolution_tool. Bash is not included. Operation-level Bash enforcement is owned by the tool's permission registration, not a demonstrated intersection with calling-agent mode. `PermissionMode.READ_ONLY` does reject interpreters classified unknown when actually selected for Bash; that guarded mode must not be confused with the default imported danger_full_access configuration (SRC-1, `autogenesis/permission/types.py`).

#### RT-RTE-skill-delivery
Label: Skill instruction delivery

Endpoints: selected skill schema → skill manager → registered content transformation → calling agent action result. Code selects by name/type/allowlist; foreground model decides whether to invoke and later interpret it. No separate skill execution agent is created. Natural-language content is returned after rewriting `python scripts/` to an absolute skill directory path and appending resource lists. Operating mode: task-directed instruction retrieval. Answer oracle: inapplicable, retrieval does not judge task truth. This is a read path, not content admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Response.message contains the skill body and available resources/scripts/references/examples.
- Later read-back: returned instructions may reach later rounds through action-memory handling; registry-backed retrieval can fetch the registered body again. Exact retention of the complete returned body is backend-dependent and uninspected here.
- Delegated visibility: inapplicable — the skill body is delivered to the calling agent rather than a forked worker.
- Selection predicate: caller's skill_allowlist and agent._allowed_skill_types filter schemas and summaries; direct manager calls resolve by name without that native-roster filter.
- Invalidation or expiry: registry updates invalidate instruction caches; content remains registered until replacement/unregister/cleanup. Model-context retention is not specified by this reader.
- Activation or effect: supplies methodology text for model interpretation; reliable adherence and changed behavior are unobserved.
- Evidence limits: presence in config does not prove native callability; MetaAgent's inherited worker selector excludes orchestrator-only playbook content in the inspected projection.

SRC-1, `autogenesis/skill/context.py`, `autogenesis/skill/server.py`, `autogenesis/agent/native_tools.py`, `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`.

> content = skill_config.content.replace("python scripts/", f"python {skill_dir}/scripts/")
> --- `autogenesis/skill/context.py`

#### RT-RTE-extension-admission
Label: Extension admission and recovery

Endpoints: generator/optimizer success or Gateway promotion request → registration hook/promotion → extension manager → component registration, disk manifest/archive and optional smoke/revert. Registration supplies live consumers for supported modules such as tools; the memory-class branch instead retains instance=None. Owner: extension manager for registration/recovery; generated-tool finalizer and Gateway for their respective triggers. Model proposes capability source; code gates file discovery/staged validation, frozen target lookup, archive/manifest and optional smoke. Humans can initiate a promotion or configuration change but are not a mandatory per-content approver on the generated-tool path. Operating modes: open-task capability creation/repair, optional synthetic smoke and prompted evaluator/baseline comparisons. Improvement triggers in doctrine are missing means, recurring structural failure or method deficiency, not an automatic scored event subscription.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registered component name, or exception/hook block that can make the agent Response unsuccessful. Generator finalization's failure does not itself restart the completed agent loop.
- Later read-back: supported active managers expose registered schemas/content to later dispatch; archives and manifest retain versions for reload/rollback. Exception: extension memory-class registration stores instance=None, with no subsequent build in the inspected load/add path; get_info-based lifecycle hooks and agent prompt readers skip it. An additional build or instance-supplying path is needed for usable retention/context delivery. No later usage trace was supplied.
- Delegated visibility: generated tool source executes in the runtime process on load; future agents can receive the new capability schema and invoke it. This is broader than returning a proposal to the parent.
- Selection predicate: named module/file; class name determines frozen-target check; unregistered names are allowed, lookup errors fail closed. Prompt loading deliberately omits the evolvability flag; memory lookup does not establish the same flag coverage as tool/agent/skill paths.
- Invalidation or expiry: rollback restores an archived artifact and re-registers it; unload removes the active registration. Archive/manifest failure unloads the half-committed component; smoke rejection attempts rollback or unload, with recovery failure logged.
- Activation or effect: _load_component registers before smoke; this is live capability admission for supported modules, not guaranteed memory-instance activation. Dynamic Python loading executes code before class evolvability validation, and memory class registration constructs a temporary instance but stores instance=None. Later schema delivery and capability invocation are wired for supported other modules, but actual beneficial behavioral change is unobserved.
- Evidence limits: smoke can be disabled by explicit false/config; supported Gateway promotion forwards run_smoke. The generic probe neither guarantees the changed target was invoked nor compares task quality; recovery is not a transaction over arbitrary Python/external side effects.

SRC-1, `autogenesis/agent/generator/tool_generate_agent.py`, `autogenesis/agent/optimizer/tool_optimize_agent.py`, `autogenesis/hook/default/tool_registration.py`, `autogenesis/gateway/service.py`, `autogenesis/extension/server.py`, `autogenesis/extension/smoke_gate.py`, `autogenesis/dynamic/server.py`.

> name = await extension_manager.add_component("tool", tool_path, config={"enable_evolving": True})
> --- `autogenesis/hook/default/tool_registration.py`

> if run_smoke is not None:
>             return bool(run_smoke)
> --- `autogenesis/extension/server.py`

> run_smoke=params.get("run_smoke"),
> --- `autogenesis/gateway/service.py`

> return await self._load_prompt(abspath, return_version)  # prompts carry no enable_evolving flag
> --- `autogenesis/extension/server.py`

> exec(code, module.__dict__)
> --- `autogenesis/dynamic/server.py`

The memory exception is the same referent as [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission), a material part of this generic admission route, not an assertion that all memory paths are inert. Extension loading passes a class; register instantiates it for metadata/permission registration but retains the instance only when its input was already a Memory instance. The extension add/load code supplies no build before returning. Separate build stores an initialized instance; instance registration also retains its supplied instance. Archiving or rollback of source does not migrate old live session contents or repair this missing consumer. Added implementation coverage: SRC-1, `autogenesis/memory/context.py`, `autogenesis/memory/server.py`, `autogenesis/hook/default/memory.py`, `autogenesis/agent/types.py`, alongside `autogenesis/extension/server.py`.

> cfg = await memory_manager.register(cls, memory_config_dict=config, override=True, version=version)
> --- `autogenesis/extension/server.py`

> instance=memory_instance if isinstance(memory, Memory) else None,
> --- `autogenesis/memory/context.py`

> if info and info.instance is not None:
>                 await info.instance.emit(event, session_id=ctx.id)
> --- `autogenesis/hook/default/memory.py`

> memory_config.instance = memory_instance
> --- `autogenesis/memory/context.py`

The smoke answer oracle is only generic response success and absence of stopped_by_constraint. Although the synthetic task asks for exactly OK, the inspected consumer does not compare result text to OK. It does not force invocation of the module/name being admitted.

> ok = bool(getattr(resp, "success", False)) and not data.get("stopped_by_constraint", False)
> --- `autogenesis/extension/smoke_gate.py`

Guidance shaping proposals is the prompt/playbook in [RT-CLM-evolution-guidance](#rt-clm-evolution-guidance): distinguish user work from capability defects, evaluate, compare and undo regressions. What persists is active source/instruction material, registry metadata and archived versions; this route does not require retaining a criticism explaining every revision. Method guidance is not itself revised by this hook.

Theory account, scoped to that formulated evolution method: condition 1, localized content, is wired as shipped prompt/playbook text. Condition 2, consumption of its meaning, is claimed by instructions to the orchestrator; model compliance is unobserved and playbook callability has the type-filter limit above. Condition 3, content-directed criticism, is claimed for identifying capability defects and supplying failure evidence; no supplied episode shows a challenged theory, blame and revision. Condition 4, iterative retention shaping the next round, is claimed by the prescribed re-optimization loop, not observed. These are separate theory-builder conditions 1–4, not an overall builder verdict. Addressability: sections and rules are inspectable/revisable as text, but the playbook is not individual executable predicates. Persistence: shipped method and admitted capabilities can span sessions through files; retained per-update rationale and its later reader are uninspected. Learning: improved future capacity is not established by registration alone; no comparative outcomes or attribution evidence were supplied. Reflection: the method requests inspecting capability source/flags and revising that capability in response; this affords bidirectional self-representation-mediated change, without an observed criticism episode. Reflective theory builder and autonomous theory builder: uninspected as exercised properties; method-text revision against records of its own operation and computation performing every criticism/retention step are not established. Self-improvement: bounded system is Autogenesis's capability organization, horizon later invocations/sessions, objective successful user-task execution independent of a particular proposed change. Wiring affords evidence-responsive self-change, but later behavior causally depending on a selected update and improved outcomes remain unobserved.

#### RT-RTE-workflow-execution
Label: Workflow and canvas execution

Endpoints: agent workflow call, Gateway workflow command or client canvas graph → workflow manager/runtime → step-selected managers → terminal WorkflowRun and checkpoints. Canvas stores JSON drafts/library copies and compiles ephemeral definitions, not agent-callable registered HTML workflows. Code owns graph traversal and schema/preflight checks; caller/graph selects orchestration, while agent steps can delegate local decisions to models. Operating mode: caller-defined workflows, including bounded compare/verify programs when authored. Answer oracle: step/program specific, not a universal expected answer. Humans may author/import graph content; Gateway identity alone does not prove human content approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: start/run APIs return a run ID or terminal WorkflowRun; rejected preflight is checkpointed as REJECTED.
- Later read-back: resume parses checkpoint state and checks runtime major version and workflow name/version. A nonempty program hash must match; a missing/empty hash is accepted after those legacy checks and stamped with the current definition's hash. Both accepted paths convert completed invocations to cached, so executable identity is not established for every reused result. Canvas library imports reuse stored JSON as a fresh draft.
- Delegated visibility: agent-step payload/context mounts select inputs; workflow tool/skill/connector/environment branches call owning managers directly, not the parent agent's _run_one.
- Selection predicate: compiled step type/target and argument resolution; deprecated definitions, excessive depth, invalid inputs or unavailable capabilities reject at preflight. Resume additionally rejects unequal nonempty program hashes; its supported hashless migration branch does not establish original executable identity.
- Invalidation or expiry: unequal nonempty program hashes, runtime-major mismatch or workflow name/version mismatch reject restore; a missing hash does not. Incomplete frames reset and nonterminal invocations requeue; pause/cancel APIs and shared nested budgets constrain execution.
- Activation or effect: callable steps can act through managers and resume can repeat unfinished work. Cached completed invocations are recovery evidence, not proof all external effects are exactly once.
- Evidence limits: no graph/run/checkpoint was executed; compiler and every specialized step policy were not exhaustively inspected. Schema validation is not equivalent to the agent dispatcher's read-only deny list.

SRC-1, `autogenesis/workflow/runtime.py`, `autogenesis/workflow/types.py`, `autogenesis/workflow/server.py`, `autogenesis/gateway/service.py`, `autogenesis/canvas/server.py`. Added implementation coverage includes the checkpoint defaults and supported restore forwarding below; no checkpoint was executed.

> return await tool_manager(name=target, input=payload, ctx=ctx)
> --- `autogenesis/workflow/runtime.py`

> if run.program_hash and run.program_hash != definition.program_hash:
>             raise ValueError("Checkpoint executable contract does not match the registered Workflow")
> --- `autogenesis/workflow/runtime.py`

The hash guard is a workflow-runtime invariant only for nonempty checkpoint hashes, not universal executable-identity validation. Its external contract is trustworthy checkpoint provenance for hashless restores. This is a reachable compatibility path, not merely a declared type: WorkflowRun defaults program_hash to an empty string; the manager forwards the requested checkpoint to runtime.resume; Gateway requires name/checkpoint and forwards them without imposing a hash. Implementation conclusion status: wired. Operation conclusion status: uninspected.

> if not run.program_hash:  # migrate pre-1.1 checkpoints after legacy identity checks
>             run.program_hash = definition.program_hash
> --- `autogenesis/workflow/runtime.py`

> if item.state == InvocationState.COMPLETED:
>                 item.state, item.cached = InvocationState.CACHED, True
> --- `autogenesis/workflow/runtime.py`

> program_hash: str = ""
> --- `autogenesis/workflow/types.py`

> return await workflow_runtime.resume(self._require(name), checkpoint, ctx=ctx, depth=depth)
> --- `autogenesis/workflow/server.py`

> run = await workflow_manager.resume(
>             name, checkpoint, ctx=self._sessions[session_id].context,
>         )
> --- `autogenesis/gateway/service.py`

Canvas admission is explicit save/export of caller-supplied graph content. Save checks duplicate IDs and edge endpoints; export writes a reusable JSON copy; overwrite/delete and reimport provide recovery choices, not automatic quality comparison. This is product/orchestration reuse, separate from smoke-gated extension registration. No oracle is used by canvas save/export, and no per-graph human approval is inferable from the API call alone.

#### RT-RTE-model-chat
Label: Direct model chat

Endpoints: Gateway model.chat request → validated messages → model_manager.stream → model.chat delta/done/error/cancelled events. Gateway owns request ID and cancellation; selected remote model supplies text. Operating mode: direct open chat. Caller chooses registered model and string messages with system/user/assistant roles; no independent answer oracle or required human content approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: request_id and model name; streamed text/thinking and final concatenated message follow as events.
- Later read-back: uninspected — this handler's event publishing does not establish later model context replay.
- Delegated visibility: inapplicable — no agent delegation is constructed by this handler.
- Selection predicate: named registered model and nonempty validated message list.
- Invalidation or expiry: explicit cancellation or provider error ends the stream; model registry configuration can change later requests.
- Activation or effect: emits model output without an agent tool list, task round, done_tool or review gate. It does not itself dispatch arbitrary returned tool calls.
- Evidence limits: no chat execution, provider-native service behavior or correctness observation was supplied.

SRC-1, `autogenesis/gateway/service.py`, `autogenesis/model/server.py`, `autogenesis/model/context.py`.

> async for event in model_manager.stream(name=model, input={"messages": messages}):
> --- `autogenesis/gateway/service.py`

A second code-driven alternate is ProceduralAgent: it runs `run_procedure` once under lifecycle hooks and returns its Response. Its inherited public entry still uses runtime invocation, but model-round budgets/decisions cannot be generalized to its procedure body (SRC-1, `autogenesis/agent/types.py`).

### Claims

#### RT-CLM-evolution-guidance
Label: Self-evolution method and approval claims

Claimed operation: MetaAgent should diagnose missing/weak capabilities, generate/optimize, evaluate and keep or undo changes. Source: SRC-1, `autogenesis/prompt/default/meta_agent.html`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`; doctrine/design layer. The method asks for evidence rather than treating every deliverable defect as a capability defect.

> Evolution targets a **capability** defect, not a one-off weak attempt.
> --- `autogenesis/skill/creator/self_evolving_skill/SKILL.md`

The playbook also says no separate staging, while the runtime has staged validation/promotion; the current prompt says explicit user approval, while the generated-tool finalizer can invoke software promotion. Treat these as conflicting design statements bounded by the implemented route, not a universal approval guarantee.

> Write evolved capabilities here; they are promoted to the shared extension root only after validation and explicit user approval.
> --- `autogenesis/prompt/default/meta_agent.html`

> # The existing runtime does not yet expose a user-approval rendezvous.
> --- `autogenesis/gateway/service.py`

The first quote describes a diagnosis criterion, not an observed criticism. The second is a prompt request, not an enforced veto. [RT-RTE-extension-admission](#rt-rte-extension-admission) supplies the actual admission and theory-property limits.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-capability-load
Label: Loaded capability authority

Consumer: future native-tool assembly and owning capability managers. Channel: active manager registration, selected schema delivery and tool/workflow/agent execution. Force: executable Python dispatch or symbolic workflow interpretation; unlike a mere proposal, registration can change later available actions for supported modules such as tools, agents and workflows. Memory-class extension registration is an exception: it stores instance=None, so the lifecycle-hook and agent-context consumers skip it unless a separate build/instance path supplies a live instance. Import/constructor effects and archived source remain real, but admission alone does not supply usable later memory retention/context authority. Horizon: subsequent calls for live consumers, with disk manifest/archive enabling artifact restoration across processes, not guaranteed restoration of live memory/session state. Coverage and rollback limits are those of [RT-RTE-extension-admission](#rt-rte-extension-admission); actual later activation is unobserved. SRC-1, `autogenesis/extension/server.py`, `autogenesis/agent/native_tools.py`, `autogenesis/dynamic/server.py`.

#### RT-BAP-method-instructions
Label: Method instruction authority

Consumer: calling agent's model decision. Channel: prompt template and returned skill instructions, including the evolution rules directly in the MetaAgent prompt. Force: natural-language guidance, not mandatory compliance or a replacement for software admission checks. Horizon: current decision and later decisions receiving that prompt or retained instruction text. Registered skills persist independently of whether their returned body survives memory selection. Native playbook delivery has the type-filter limit described in [RT-RTE-skill-delivery](#rt-rte-skill-delivery). SRC-1, `autogenesis/prompt/default/meta_agent.html`, `autogenesis/skill/context.py`, `autogenesis/agent/types.py`.

## Annotations

none
