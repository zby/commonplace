---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Agno SDK and AgentOS runtime baseline: agent/tool execution, delegation, workflow handoffs, approval, durable dispatch and component admission at the frozen revision."
run-id: AAS-2026-10-13-agno-60e6e09dd4a6-01
reviewed-boundary: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
---

# Agno runtime report

## Runtime account

### Work and evidence basis

Agno owns the model/tool loop, not just a tool interface supplied to someone else's loop. Its SDK exposes Agent, Team and Workflow execution; AgentOS adds HTTP dispatch, streaming, approvals and optional durable work acceptance. The selected boundary is the SDK/server subsystem fixed in [boundary](boundary.md), not infrastructure provisioning, the terminal operations package or hosted UI. The shipped quickstart promises a plain-English market brief using current financial tools ([RT-CLM-market-brief](#rt-clm-market-brief)). This account establishes implementation wiring and declared intent only. No target runs, tests, provider calls or experiments were supplied or performed; successful work, actual activation and benefit remain unobserved.

All source citations below use SRC-1 at the frozen commit. Added inspection covers agent dispatch/run/messages/tools, base model execution and fallback, Function execution and ShellTools, team delegation, workflow Step handoffs, AgentOS authentication and agent routing/queue execution, component configuration routing, Agent database reconstruction, PostgreSQL configuration enforcement and compaction. These are additional implementation anchors under the existing source registration, not new sources. Cookbook examples supply shipped configuration and intent, not execution evidence.

### Ordinary invocation, end to end

A caller constructs an Agent with model, instructions and tools, then submits an input. The shipped `agent_with_tools` uses `Gemini(id="gemini-3.6-flash")`, grants selected YFinance tools, requests current date/time and Markdown, and calls `print_response(..., stream=True)`. The server driver registers that same Agent alongside teams and workflows. SRC-1: `cookbook/00_quickstart/agent_with_tools.py`, `cookbook/00_quickstart/run.py`.

The ordinary returning SDK route is [RT-RTE-agent-run](#rt-rte-agent-run). `Agent.run` passes user/session/run identities, state, media, dependencies, metadata and output schema to `run_dispatch`. `_run` registers cancellation tracking, loads or creates the session, merges session state, resolves callable dependencies and executes input hooks. It constructs the actual granted tool set and messages before calling the model. Static and callable natural-language instructions reach the system message; history inclusion, dependency/state inclusion and tool availability are caller/configuration choices rather than properties of every run. SRC-1: `libs/agno/agno/agent/agent.py`, `libs/agno/agno/agent/_run.py`, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/agent/_tools.py`.

The next-step owners alternate. Host code controls preparation, cancellation checks, retries, optional reasoning/output/parser stages and persistence. The provider model selects a response or tool calls from the offered schemas. The base Model loop records assistant messages, resolves callable tools and executes their calls, feeds results back into messages and continues. Host Function code invokes Python entrypoints and hooks; those entrypoints may affect external services, files or the host OS. This is not an isolation boundary. The capability surface includes arbitrary caller-provided Python tools, hooks, dependencies and provider-native tools; the quickstart's current grant set is much narrower. A deployed process/container/service policy would bound effects, but no deployed isolation envelope was supplied. SRC-1: `libs/agno/agno/models/base.py`, `libs/agno/agno/tools/function.py`, `libs/agno/agno/agent/_run.py`.

The terminal output is RunOutput, or events/chunks through streaming paths. It can be completed, paused, cancelled or error. Before completed return, code updates response/media, applies optional output conversion and post-hooks, waits for background memory/learning tasks, optionally summarizes the session, marks completion and calls cleanup/storage. Session state and a scrubbed storage copy are written through separate session and run calls. This shows the persistence seam, not atomic commitment of tool effects, session data and run output. Memory extraction and learning revision details belong to the memory analyst. Cancellation is checked between stages and tools are disconnected in `finally`; retries rerun the attempt with delay/backoff. These mechanisms do not demonstrate rollback of earlier external tool effects. SRC-1: `libs/agno/agno/agent/_run.py`.

The underlying distributed-parametric model is [RT-CMP-gemini](#rt-cmp-gemini). Optional fallback models and compaction's summarizer have separate component records. No observed model version, parameter update or provider-internal state is inferred from SDK object mutation.

### Material alternate routes and forcing cases

Four source-selected forcing cases limit otherwise tempting system-wide guarantees. They are code cases, not experiments.

1. **A confirmed local Function versus a provider-native tool or direct callback.** [RT-RTE-tool-confirmation](#rt-rte-tool-confirmation) pauses marked Function calls before their entrypoint executes. Resume code checks confirmation and can record rejection. But native tool dictionaries are explicitly executed by providers, while Function.execute and workflow custom executors are host Python paths. The pause mechanism is not a universal approval gate on all effects. ShellTools explicitly runs a subprocess on the host; enabling confirmation changes admission, not sandboxing. SRC-1: `libs/agno/agno/models/base.py`, `libs/agno/agno/agent/_tools.py`, `libs/agno/agno/tools/function.py`, `libs/agno/agno/tools/shell.py`, `libs/agno/agno/workflow/step.py`.
2. **A team member pause versus a nested workflow pause.** [RT-RTE-team-delegation](#rt-rte-team-delegation) forwards selected task/context to a member, links child runs and propagates its requirements. Ordinary agent/team workflow steps likewise create executor requirements. However the inspected sync nested-workflow path warns that its parent will continue despite an inner pause. Thus approval/pause propagation cannot be inferred uniformly from the existence of Agent HITL. SRC-1: `libs/agno/agno/team/_default_tools.py`, `libs/agno/agno/workflow/step.py`; see [RT-RTE-workflow-step](#rt-rte-workflow-step).
3. **A queueable background request versus a media/factory/remote request.** [RT-RTE-queue-dispatch](#rt-rte-queue-dispatch) commits a ticket before acceptance and workers re-enter `arun` under its identities. The router deliberately falls back to bounded in-process background execution for nonqueueable submissions. A 202 alone does not guarantee durable execution. Queue leases, generation fences and backend session serialization also do not imply exactly-once external effects. SRC-1: `libs/agno/agno/os/routers/agents/router.py`, `libs/agno/agno/os/job_queue.py`.
4. **A database-published component versus explicit SDK reconstruction or a live Python object.** [RT-RTE-config-admission](#rt-rte-config-admission) versions configuration and changes a live pointer. PostgreSQL rejects modification of an already published config and rejects setting a draft current. But Agent loading with explicit version/label takes a different branch, and live Python configurations remain directly caller-controlled. Published immutability is a scoped backend invariant, not immutability of every executable Agent or its tool code. SRC-1: `libs/agno/agno/os/routers/components/components.py`, `libs/agno/agno/db/postgres/postgres.py`, `libs/agno/agno/agent/agent.py`.

### Control ownership and guarantee limits

**Local confirmation.** Owner: Model function-call dispatcher plus Agent continuation handler. Enforcement point: pause before `run_function_call`, followed by confirmation check on resume. Strength: protocol for marked local Functions on the inspected paths. Covered paths include the inspected synchronous model/continuation path; async code exposes corresponding pause/update branches but is not an exhaustively audited equivalent. Alternate paths include provider-native tools, direct Function/entrypoint invocation, dependencies, hooks, workflow callbacks, remote executors and tools' own subprocesses. Required external contract: a trusted continuation client/HTTP authorization configuration must supply truthful approval/results, and a tool implementation must not circumvent the intended gate. implementation conclusion status: wired. operation conclusion status: uninspected. No blanket effect approval or isolation guarantee is concluded. Evidence is retained in [RT-RTE-tool-confirmation](#rt-rte-tool-confirmation).

**HTTP admission.** Owner: AgentOS router authentication/resource dependencies and configured middleware/provider. Enforcement point: router-level dependencies, not model inference or local SDK execution. Strength: policy conditional on deployed configuration. The authentication dependency intentionally permits an instance with no configured security key/JWT; security-key authentication is an unscoped root, while JWT delegates authentication to middleware. The agent run route names `require_resource_access("agents", "run", "agent_id")`. Direct SDK calls are outside that HTTP gate. A configured JWT middleware/provider and secret/key management are external contracts; this inspection does not certify every router or middleware combination. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1: `libs/agno/agno/os/auth.py`, `libs/agno/agno/os/routers/agents/router.py`.

> # If no security key is set, skip authentication entirely
> if not settings or not settings.os_security_key:
>     return True
> --- `libs/agno/agno/os/auth.py:629-631`

**Durable acceptance and coordination.** Owner: agent HTTP adapter, QueueWorker and configured queue store. Enforcement point: committed ticket, claim/lease/retry/settlement and store-backed fences. Strength: protocol dependent on a conforming persistent store and runnable component resolution. Covered paths: queueable JSON background requests, with separate streamed handling. Excluded alternate: in-process bypass, remote/factory/media inputs. Per-session serialization additionally depends on the backend flag/contract. External tools must be idempotent or transactionally protected if retry safety is required. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence is retained in [RT-RTE-queue-dispatch](#rt-rte-queue-dispatch).

**Published configuration.** Owner: component API and database backend; enforcement point: PostgreSQL config update/current-pointer checks. Strength: invariant in that inspected backend, assuming writes use its methods and transactions rather than external database modification. It covers published rows and live-pointer admission, not immutable external models, registry callables, every adapter or explicit draft experimentation. implementation conclusion status: wired. operation conclusion status: uninspected. Evidence is retained in [RT-RTE-config-admission](#rt-rte-config-admission).

**Reliability and factual correctness.** Instructions such as not inventing a value are natural-language policies, not an enforced correctness oracle. Input/output checks, fallback, cancellation and typed outputs change the control path but do not establish correct finance answers or reliable tool completion. Model call limits are enforced at local Function dispatch and explicitly exempt offload read-back tools when a result store exists; they are not a universal limit on provider computation or host effects. SRC-1: `cookbook/00_quickstart/agent_with_tools.py`, `libs/agno/agno/agent/_run.py`, `libs/agno/agno/models/base.py`.

> counts_against_limit = result_store is None or fc.function.name not in NEVER_OFFLOADED_TOOLS
> --- `libs/agno/agno/models/base.py:2435-2435`

### Working context and changes admitted

Team delegation creates a separate model context from selected task, optionally team/member history, interactions and media, rather than sharing the parent's entire window. Return text, linked run records, media and state can cross back. This resembles a call frame only for context isolation: shared session IDs, shallow state copies, retained child outputs and external tool effects are not popped away. Workflow steps can replace input with the deepest content of the last step's output; they do not necessarily receive the complete original question plus all intermediate evidence. These transformations constrain what later reasoning can know. SRC-1: `libs/agno/agno/team/_default_tools.py`, `libs/agno/agno/workflow/step.py`.

[RT-RTE-context-window](#rt-rte-context-window) records history filtering, summary replacement and overflow-triggered retry. Compaction keeps a summary and tail in the model window; originals can remain in sessions/archive and optional lookup tools can retrieve details. Keeping text in storage is different from returning all of it to a consumer. Compression, offload, skills, reasoning/output/parser subcalls and provider caching are also exposed in the inspected integration seams, but their complete policy, persistence and authority are not established here. The memory and epistemic analyses must establish those material submechanisms without treating these integration mentions as exhaustive findings. SRC-1: `libs/agno/agno/agent/_run.py`, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/models/base.py`, `libs/agno/agno/compaction/compaction.py`.

Runtime capability changes can enter through a caller's new Python object/tools/hooks or through versioned component configuration and registry reconstruction. The concrete database route is [RT-RTE-config-admission](#rt-rte-config-admission). It changes instructions, model/tool references and orchestration config; it is not evidence that arbitrary newly authored executable code can be installed through that API. Models can propose calls and task descriptions; host code and caller configuration determine which executable capabilities exist. Human authorship and per-content approval of configuration requests are unresolved, because HTTP caller identity alone does not establish either. Retained knowledge/memory/learning changes are not redescribed here. Infrastructure provisioning is excluded by the boundary. No objective-driven self-improvement or theory-building claim is made from these configuration and execution routes.

## Shared records

### Components

#### RT-CMP-gemini
Label: Gemini inference model in the shipped quickstart

Source-native identity: Gemini model configured with ID `gemini-3.6-flash` in the selected Agent and sequential workflow. Representational form: distributed-parametric inference behind the provider API; model IDs, request settings and messages are separate symbolic/text inputs. Storage substrate: provider-managed model weights; the local SDK stores configuration, not those weights. Parameters changing during operation: uninspected provider internals; inspected code requests inference, not weight updates. Exact version pinned: no immutable weight/version digest is established by this ID. Mutable endpoint resolving to another model: unresolved provider alias/endpoint policy, so exact identity stability cannot be guaranteed. No execution evidence supplies the actually served model. SRC-1: `cookbook/00_quickstart/agent_with_tools.py`, `cookbook/00_quickstart/sequential_workflow.py`.

> name="Agent with Tools",
> model=Gemini(id="gemini-3.6-flash"),
> --- `cookbook/00_quickstart/agent_with_tools.py`

#### RT-CMP-fallback-model
Label: Configured fallback inference models

Source-native identity: Model instances or string references in FallbackConfig's error/rate-limit/context-overflow lists. Representational form: distributed-parametric provider inference, selected by symbolic error classification. Storage substrate: provider weights and local configuration lists. Parameter changes: provider internals uninspected; the inspected route switches models rather than training them. Exact version pinned: caller-dependent and not established for a deployed configuration. Mutable endpoint: can designate another provider/model via configuration; provider alias mutability remains unresolved. These are optional alternatives, not proven active in the quickstart. SRC-1: `libs/agno/agno/models/fallback.py`.

> # General fallback models tried when the primary model fails
> on_error: List[Union[Model, str]] = field(default_factory=list)
> --- `libs/agno/agno/models/fallback.py`

#### RT-CMP-compaction-model
Label: Compaction summary model

Source-native identity: Compaction.model, resolved to a Model used by `_summarize`/`_asummarize`. Representational form: distributed-parametric provider inference consuming text to produce a natural-language summary. Storage substrate: provider weights; local Model configuration. Parameter changes during operation: not established; provider internals uninspected and the inspected route performs inference. Exact version pin: not established; Model/string configuration is not a weight digest. Mutable endpoint resolving to a different model: unresolved provider behavior and caller-controlled model reference. This role is distinct from the foreground model even if a caller chooses the same provider model. SRC-1: `libs/agno/agno/compaction/compaction.py`.

> response = model.response(messages=self._summary_messages(messages, previous, archived))
> --- `libs/agno/agno/compaction/compaction.py`

### Operative objects

#### RT-OBJ-run-context
Label: RunContext and run identities

Source-native identity: RunContext passed through Agent execution; run/session/user IDs identify work and storage scope. Representational form: symbolic Python object/dictionaries with fixed consumers; embedded input/instruction/result strings retain natural-language interpretation. Storage substrate: in-process state; session_state is copied into session_data before persistence. Dependencies and metadata also travel on this object but do not by themselves prove retention or authorization. SRC-1: `libs/agno/agno/agent/agent.py`, `libs/agno/agno/agent/_run.py`.

> run_context.session_state = load_session_state(
>     agent,
>     session=agent_session,
>     session_state=run_context.session_state if run_context.session_state is not None else {},
> )
> --- `libs/agno/agno/agent/_run.py:446-450`

#### RT-OBJ-function
Label: Executable Function capability and schema

Source-native identity: Function with name, schema, entrypoint and optional confirmation/input/external-execution flags. Representational form: symbolic executable references, schemas and gate flags; tool descriptions are natural-language model guidance. Storage substrate: Python objects/registered callables; persisted configuration can hold references reconstructed through a Registry, not serialized callable machine code. Effects depend on the actual entrypoint and process permissions. SRC-1: `libs/agno/agno/tools/function.py`, `libs/agno/agno/agent/_tools.py`, `libs/agno/agno/registry/registry.py`.

> if self.function.entrypoint is None:
>     return FunctionExecutionResult(status="failure", error="Entrypoint is not set")
> --- `libs/agno/agno/tools/function.py:2593-2594`

#### RT-OBJ-component-config
Label: Versioned component configuration

Source-native identity: component config rows with component ID, version, stage, label, notes, links and config; component.current_version selects a live row. Representational form: symbolic routing/schema/tool/model references plus natural-language instruction content, assessed separately at consumers. Storage substrate: configured component database; PostgreSQL inspected. Config can reconstruct an Agent with Registry assistance. This is not a model-weight store or a guarantee that referenced callable implementations remain fixed. SRC-1: `libs/agno/agno/os/routers/components/components.py`, `libs/agno/agno/db/postgres/postgres.py`, `libs/agno/agno/agent/agent.py`.

> agent = Agent.from_dict(cfg, registry=registry, strict=strict)
> agent.id = id
> --- `libs/agno/agno/agent/agent.py`

### Routes

#### RT-RTE-agent-run
Label: Agent model and local tool loop

Endpoints/progression/owner: SDK input → Agent.run/run_dispatch → session and context preparation → model response/local Function loop → response transformation and hooks → cleanup/persistence → RunOutput. Host code owns stage progression; model judgment proposes response/tool calls; tool schemas resolve host executors. Run, session and user IDs scope current state and storage. Runtime client grants the model/tools, instructions, history/state/dependency policy, schema, retries and stream mode. Effects can escape through arbitrary Python entrypoints and external services. SRC-1: `libs/agno/agno/agent/agent.py`, `libs/agno/agno/agent/_run.py`, `libs/agno/agno/models/base.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RunOutput with content, tool records, metrics/media and status; streaming variants return events/chunks.
- Later read-back: Configured session/run persistence can feed history into later calls; detailed retained memory/learning selection is outside this route's finding.
- Delegated visibility: Tools receive configured injected arguments/context; child-agent visibility is controlled by the separate team/workflow routes.
- Selection predicate: Caller input and Agent configuration select the route; model-generated calls select offered Functions; configuration flags select extra context and stages.
- Invalidation or expiry: Current run tracking is cleaned in finally; persisted session expiry/deletion is uninspected here.
- Activation or effect: Code calls model and Function executors and updates output/session state; actual execution and behavioral dependence are unobserved.
- Evidence limits: Returning sync path inspected in depth; async and stream seams inspected selectively, not an exhaustive equivalence audit. No run proves factual correctness or safe retry of external effects.

Decision roles: caller configures work/capabilities; model proposes text/actions; host dispatch rules accept known tools and enforce limits; configured hooks can reject inputs/outputs. Human participation is unresolved except where a client deliberately supplies approval. Operating mode: open task request. Answer oracle: no reference answer is supplied by this inspected quickstart/runtime loop. Financial tools provide data, not a correctness oracle for the final brief. Recovery: cancellation returns a cancelled output, validation exceptions return an error, general exceptions retry according to Agent settings and ultimately store an error. Earlier tool effects are not rolled back by the shown cleanup.

> model_response: ModelResponse = call_model_with_fallback(
>     agent.model,
>     agent.fallback_config,
> --- `libs/agno/agno/agent/_run.py:554-556`

> # Persist the session row and this single run (both O(1))
> _session.save_session(agent, session=session)
> _session.save_run(
> --- `libs/agno/agno/agent/_run.py`

#### RT-RTE-tool-confirmation
Label: Local tool pause and continuation admission

Endpoints/progression/owner: model FunctionCall → dispatcher examines confirmation/user-input/external-execution flags → paused ToolExecution/RunOutput → caller continuation updates → Agent handler executes confirmed Function or injects rejection/external result → resumed model loop. Tool call IDs identify requirements; session/user/run IDs preserve the run scope. Host dispatcher owns the pause; a continuation principal supplies confirmation/input/results. SRC-1: `libs/agno/agno/models/base.py`, `libs/agno/agno/agent/_tools.py`, `libs/agno/agno/agent/_run.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Paused tool/run output describing required confirmation, user input or external execution; resumed call produces ordinary output.
- Later read-back: Paused run/session persistence supports continuation; approval audit records can be created on update, but audit-record consumers are not traced here.
- Delegated visibility: Teams propagate member requirements; ordinary workflow agent/team steps serialize unresolved requirements; nested workflow exception is recorded separately.
- Selection predicate: A Function's configured pause flags or dedicated user-input tools select the pause; confirmed true with no existing result selects execution on resume.
- Invalidation or expiry: Continuation clears resolved flags; expiry of pending approvals is uninspected — approval service lifecycle was not traced.
- Activation or effect: Marked Functions are not executed at initial pause; accepted continuation can run a tool, rejection adds an error, external execution accepts a caller result. Actual effects unobserved.
- Evidence limits: The gate is not on native provider tools, arbitrary direct entrypoints or all host callbacks; local SDK continuation identity is not proof of a human approver.

Admission account: trigger is a marked proposed tool call; proposed change is that call's external/state effect. Model proposes arguments, host decides to pause, caller can confirm/reject/provide input, and code executes or rejects accordingly. Computational admission and human approval are separate: the API supports human control but a program can supply confirmation. Operating mode: open request interrupted by explicit approval/input. Answer oracle: inapplicable — approval is a decision to allow an effect, not comparison against a known answer. Guidance: configured tool description/schema and gate flags shape selection; persisted run/tool requirements and optional audit approvals record the decision. Recovery: reject instead of executing; continuation can resume paused work. The shown mechanism does not undo an already executed effect.

> if paused_tool_executions:
>     yield ModelResponse(
>         tool_executions=paused_tool_executions,
>         event=ModelResponseEvent.tool_call_paused.value,
>     )
>     # We don't execute the function calls here
>     continue
> --- `libs/agno/agno/models/base.py:2562-2568`

> if _t.confirmed is not None and _t.confirmed is True and _t.result is None:
>     # Consume the generator without yielding
>     deque(run_tool(agent, run_response, run_messages, _t, functions=_functions), maxlen=0)
> else:
>     reject_tool_call(agent, run_messages, _t, functions=_functions)
> --- `libs/agno/agno/agent/_tools.py`

> if isinstance(tool, Dict):
>     # If a dict is passed, it is a builtin tool
>     # that is run by the model provider and not the Agent
>     _functions.append(tool)
> --- `libs/agno/agno/agent/_tools.py`

The corresponding shell capability runs with host process permissions, unless an external deployment isolates that process:

> result = subprocess.run(
>     args,
>     capture_output=True,
>     text=True,
>     cwd=str(self.base_dir) if self.base_dir else None,
> )
> --- `libs/agno/agno/tools/shell.py`

#### RT-RTE-team-delegation
Label: Team selected-member delegation

Endpoints/progression/owner: team model selects member ID/task via delegation Function → code finds configured member → builds member input/history → member Agent/Team.run → processes returned content/state/media/child run → parent model or direct return. Team configuration and member lookup bound available delegates; a UUID child run links to its parent and members share the session ID/user identity. SRC-1: `libs/agno/agno/team/_default_tools.py`, `libs/agno/agno/team/_tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Member content or events as delegation results; a member pause returns a human-input message and propagates requirements.
- Later read-back: Member runs can be added to the team session and optional future member/team history; complete storage scrubbing/selection policy remains for specialist inspection.
- Delegated visibility: Selected task or original input, optional team/member history and interactions, supplied media/dependencies/metadata and a shallow copy of session state; not automatic delivery of the whole parent model window.
- Selection predicate: Requested member_id must resolve in configured members/subteams; determine_input_for_members controls task versus original input and history flags control extra context.
- Invalidation or expiry: Child run finishes or pauses and cancellation can cascade; retained member-history expiry is uninspected — storage lifecycle not audited here.
- Activation or effect: Child run executes its own model/tool loop; return processing can update team state/media and link run records. Behavioral activation remains unobserved.
- Evidence limits: Detailed selected-member sync/stream route inspected; broadcast, task-board, remote and full async variants are available but not fully traced, so this is not an exhaustive team scheduler account.

Decision roles: team model proposes delegate and task; lookup/code rejects unknown member IDs; member model decides within its own grants; caller owns configuration. Operating mode: open task decomposition, not a bounded curriculum. Answer oracle: no expected/reference outcome in this mechanism. A task's description of a good result is requested guidance, not an independent oracle. Recovery: child cancellation drains stream and propagates; member pause requirements cross to parent. Separate contexts resemble frames, but shared state, media and retained outputs escape them.

> if team.determine_input_for_members is False:
>     member_agent_task = input  # type: ignore
> else:
>     member_agent_task = task
> --- `libs/agno/agno/team/_default_tools.py`

> member_session_state_copy = copy(run_context.session_state)
> --- `libs/agno/agno/team/_default_tools.py:690-843`

#### RT-RTE-workflow-step
Label: Workflow executor handoff and nested pause exception

Endpoints/progression/owner: Workflow Step receives StepInput/prior outputs → code selects an executor and prepares its input → custom Python function, Agent, Team or nested Workflow executes → StepOutput carries content/status to subsequent steps. The shipped stock research pipeline configures Data Gathering → Analysis → Report Writing. Host workflow topology owns step order; models own reasoning inside Agent steps. Parent/child run IDs and workflow step IDs link outputs; session identity/state travel to executors. SRC-1: `cookbook/00_quickstart/sequential_workflow.py`, `libs/agno/agno/workflow/step.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: StepOutput and eventually workflow result/events; executor output records may be retained on the workflow run.
- Later read-back: Optional workflow history can be prefixed to later step input; detailed workflow persistence and resume selection remain uninspected here.
- Delegated visibility: Last prior StepOutput's deepest content normally replaces original input for agent/team/workflow executors; optional workflow history and user/rejection feedback add context. Custom functions receive StepInput/run context rather than this exact model-message contract.
- Selection predicate: Configured executor type and ordered step inputs; prior deepest content wins when present. Condition/Loop/Router/Parallel selection policies are uninspected — those classes were not traced.
- Invalidation or expiry: Per-step execution ends with output/error/pause handling; persisted workflow checkpoint invalidation is uninspected — lifecycle not traced.
- Activation or effect: Agent/team steps run their granted loops; Python callbacks act directly. Nested sync workflow can return paused content while its parent continues.
- Evidence limits: Selected sequential Step handoff and sync nested-workflow exception inspected; no universal workflow pause propagation, complete graph safety or output correctness conclusion follows.

Decision roles: caller supplies topology/executor; host prepares input; model generates each stage's product; optional rejection feedback reaches a retry input, but reviewer identity and complete retry admission remain unresolved. Operating mode: configured open-request pipeline. Answer oracle: no expected stock-research outcome is supplied. These are external work products, not proven admitted changes to Agno itself.

> if deepest_content:
>     return deepest_content
>
> # If no previous step outputs, return the original message unchanged
> return message
> --- `libs/agno/agno/workflow/step.py`

> # Warn if the nested workflow paused (e.g., due to HITL on an inner step)
> if nested_run_output.is_paused:
>     logger.warning(
>         f"Step '{self.name}': Nested workflow '{self.workflow.name}' is paused "
>         "(likely due to HITL on an inner step). The parent workflow will continue "
>         "but the paused inner step may not have executed."
>     )
> --- `libs/agno/agno/workflow/step.py:2939-2945`

#### RT-RTE-queue-dispatch
Label: AgentOS durable background dispatch

Endpoints/progression/owner: authenticated/configured HTTP agent endpoint → resolve component and validate queueable input → enqueue ticket/prepare pending run → worker claim → component.arun or continuation → settle/retry ticket → client polls or tails stream. Request/caller scope and component/session/user/run IDs are captured in the ticket. Router owns acceptance, worker owns execution lifecycle, backend owns atomic claim/fence semantics. SRC-1: `libs/agno/agno/os/routers/agents/router.py`, `libs/agno/agno/os/job_queue.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: 202 with run/session IDs and pending status, or duplicate ticket's status; queued streamed requests use an event tail.
- Later read-back: Worker reads retained ticket payload/scope and component configuration; clients read status/results; a resumed paused ticket re-enters the same run.
- Delegated visibility: Worker receives serializable input/kwargs and resolved identities/configuration, not arbitrary accepting-request objects; factory/remote/media cases may bypass queue.
- Selection predicate: Queue worker configured, component resolvable at claim, JSON payload queueable and no unsupported media; idempotency key can select an existing ticket.
- Invalidation or expiry: Leases/heartbeats, timeout and retry budgets control tickets; stale work is reconciled or retried/failed. Backend-supported session serialization is conditional.
- Activation or effect: Claimed worker invokes component execution and writes ticket status; real durability, recovered completion and external effect multiplicity are unobserved.
- Evidence limits: Inspected router and worker seams establish protocol wiring, not the full store implementation, a running multi-replica deployment or exactly-once tool effects. In-process 202 bypass remains materially different.

Admission account: caller proposes a work item; host accepts only queueable items to durable dispatch, with capacity/schema/conflict rejection. This is work admission, not per-content human approval or a product revision. Operating mode: open requests with bounded attempts/timeouts. Answer oracle: inapplicable — ticket state is an execution lifecycle result, not a task-correctness reference. Recovery settles pause/cancel, classifies permanent errors and retries eligible errors; shutdown interruption can requeue. Safe external retries require tool/service contracts beyond this protocol.

> # Enqueue FIRST: the committed queue row is the acceptance.
> # Rejected or duplicate submissions must leave no phantom
> # PENDING run behind in the session.
> enqueue_result = await aenqueue_ticket(queue_worker, job, agent)
> --- `libs/agno/agno/os/routers/agents/router.py`

> "Executing on the accepting replica instead - bounded and observable, but NOT durable."
> --- `libs/agno/agno/os/routers/agents/router.py:1085-1085`

> self.queue_per_session = config.queue_per_session and store_serializes_sessions(store)
> --- `libs/agno/agno/os/job_queue.py`

> elif status == RunStatus.error:
>     error_content = str(getattr(result, "content", "") or "run errored")
> --- `libs/agno/agno/os/job_queue.py:1948-2015`

#### RT-RTE-config-admission
Label: Component configuration version admission and rollback

Endpoints/progression/owner: client supplies config/stage/links/guard → component router checks scoped ownership and referenced visibility → database creates/updates version → published current pointer selects config → Agent reconstruction and later dispatch. Client proposes; API/backend constraints decide admission; subsequent Agent/model/tool consumers confer behavioral force. This is a concrete product/capability configuration change path, not an assertion about retained knowledge quality. SRC-1: `libs/agno/agno/os/routers/components/components.py`, `libs/agno/agno/db/postgres/postgres.py`, `libs/agno/agno/agent/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Config/component response, or rejection/conflict; pointer rollback returns the updated component row.
- Later read-back: Later database-resolved Agent dispatch reads current_version/config and reconstructs the Agent with registered resources.
- Delegated visibility: Linked components/versions and reconstructed member configuration can become visible to team/workflow consumers; complete recursive rehydration policy is uninspected — only Agent and API seams traced.
- Selection predicate: Component ID plus explicit version/label or default current_version; optional compare-and-set guards reject stale callers; ownership/readability checks constrain references.
- Invalidation or expiry: New published config supersedes selected live configuration; set-current can restore a prior published version. Cache invalidation timing and all adapters are uninspected — no deployment freshness guarantee established.
- Activation or effect: Accepted configuration can change later model IDs, instructions, tools and orchestration through reconstruction; actual later dispatch dependence is unobserved.
- Evidence limits: PostgreSQL published checks inspected, not every adapter or direct external database write. Live Python objects and explicit version/label SDK loads are different paths. Actor identity does not resolve human authorship/approval.

Admission account: trigger is an API config request or pointer move; proposed change is supplied config/links/stage/current version. Computational contributors are ownership checks, reference validation, backend immutability and optional concurrency guards. The requesting client can withhold publication or choose rollback; it need not be human. No model reviewer or task-answer oracle is established in this route. Operating mode: explicit configuration management, not automatic evidence-fed optimization. Guidance shaping the proposal: caller-selected instructions/resources and serialized config schema; their origin and rationale are unresolved. What persists: config versions, labels/notes/links and current pointer. Rejection: published edits, invalid references, ownership violations, invalid stage/pointer or stale guarded version. Recovery: restore a published pointer; this does not reverse completed runs or tool effects. No theory-builder or exercised self-improvement conclusion follows.

> # Published configs are immutable
> if existing["stage"] == "published":
>     raise ValueError(f"Cannot update published config {component_id} v{version}")
> --- `libs/agno/agno/db/postgres/postgres.py`

> # Only published configs can be set as current
> if stage != "published":
>     raise ValueError(
>         f"Cannot set draft config {component_id} v{version} as current. "
>         "Only published configs can be current."
>     )
> --- `libs/agno/agno/db/postgres/postgres.py`

> if published_only and version is None and label is None:
>     # Dispatch surfaces resolve only a published version; a draft-only
>     # component is not runnable. Uses the
> --- `libs/agno/agno/agent/agent.py`

#### RT-RTE-context-window
Label: History filtering and compaction at model invocation

Endpoints/progression/owner: session history → host replay selection/tool filtering → optional size-triggered summary generation → summary plus kept tail → foreground model. Manual compaction and context-overflow recovery are alternate triggers. Code rules decide when/what span to fold; a summarizer model decides summary wording. Session/archive/run IDs anchor reusable fold records. SRC-1: `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/compaction/compaction.py`, `libs/agno/agno/models/fallback.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Model-bound message list with selected/filtered history and, when successful, summary plus kept tail; manual compaction returns a result.
- Later read-back: Stored fold records can be replayed in later runs; archive_for returns a database-scoped archive and none without a database. Detailed archive search/write governance belongs to specialist inspection.
- Delegated visibility: Foreground model receives the compacted view rather than all original history; delegated frames have their separate selection route.
- Selection predicate: History enablement and replay bounds, optional historical tool-call filtering, configured token threshold/plan guards, manual call or eligible overflow recovery select transformation.
- Invalidation or expiry: New folds can replace the prior active summary; original stored session history is not rewritten by apply_compaction. Archive expiry/rollback is uninspected — archive backend lifecycle not traced.
- Activation or effect: Code replaces the request head with summary/tail and can retry after overflow; model behavioral effects and summary fidelity are unobserved.
- Evidence limits: Summarization is not a proof of semantic preservation. Optional archived-message lookup is exposed but complete reload/selection behavior is not traced here. No claim that removed material is permanently inaccessible.

Decision roles: host code selects trigger/span and minimum fold conditions; summarizer proposes wording; unsuccessful/no-summary compaction leaves the prior view. Operating mode: context-budget management during open requests. Answer oracle: no reference summary or correctness outcome inspected. This transformation does not by itself establish content-directed criticism, learning or theory-building. In the call-frame lens it removes a prefix while retaining summary/tail and optional archive reachability; storage pointers do not mean the model dereferences omitted text automatically.

> # A stored compaction is replayed rather than recomputed, so the summary is
> # paid for once and the prompt prefix stays stable between runs. The trigger
> # measures this - what is actually sent - not the planner's wider read.
> in_context = _replayed_view(compaction, history, record, replay_ids)
> --- `libs/agno/agno/agent/_messages.py`

> # Filter tool calls from history if limit is set (before adding to run_messages)
> if agent.max_tool_calls_from_history is not None:
>     filter_tool_calls(history_copy, agent.max_tool_calls_from_history)
> --- `libs/agno/agno/agent/_messages.py:1964-2003`

> if db is None:
>     return None
> return CompactionArchive(db, session_id, user_id)
> --- `libs/agno/agno/compaction/compaction.py`

### Claims

#### RT-CLM-market-brief
Label: Tool-backed current market brief

Claimed operation: the shipped first useful agent converts plain-English financial requests into live-data tool calls and a market brief. Source: SRC-1, `cookbook/00_quickstart/agent_with_tools.py`. Claim conclusion status: claimed. The configured model, instructions and selected YFinance capability are shipped wiring, not observed success or a factual-answer guarantee.

> The agent uses Yahoo Finance to turn a plain-English question into tool calls
> and a current market brief.
> --- `cookbook/00_quickstart/agent_with_tools.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-instructions
Label: Agent instruction text to provider inference

Consumer: foreground model. Channel: rendered system-message instructions and tool guidance. Force: natural-language policy interpreted by the model, not a symbolic enforcement of finance truth or tool safety. Horizon: current inference and later invocations while caller/configuration supplies the text. Configuration publication can change the supplied text through [RT-RTE-config-admission](#rt-rte-config-admission), but this record does not establish observed compliance. SRC-1: `libs/agno/agno/agent/_messages.py`, `cookbook/00_quickstart/agent_with_tools.py`.

> if len(instructions) > 0:
>     rendered = render_instructions(instructions)
> --- `libs/agno/agno/agent/_messages.py:1057-1073`

#### RT-BAP-function-dispatch
Label: Tool name and arguments to host execution

Consumer: Model function resolution and Function entrypoint executor. Channel: symbolic tool-call name/arguments, schema and injected run context. Force: executable dispatch to the granted callable, subject to local pause/limit/hook rules, with the effect authority of its host process/service credentials. Horizon: current tool call; external effects may persist beyond it and are not reversed by message cleanup. This differs from natural-language instruction force. SRC-1: `libs/agno/agno/models/base.py`, `libs/agno/agno/tools/function.py`, `libs/agno/agno/tools/shell.py`.

> if self.arguments is None or self.arguments == {}:
>     result = self.function.entrypoint(**entrypoint_args)
> else:
>     result = self.function.entrypoint(**entrypoint_args, **self.arguments)
> --- `libs/agno/agno/tools/function.py:2589-2713`

## Annotations

none
