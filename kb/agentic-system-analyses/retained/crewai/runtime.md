---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "CrewAI runtime baseline: Crew and standalone Agent execution, mediated tools, Flow control and instruction admission at the frozen revision."
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
reviewed-boundary: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
---

# CrewAI runtime report

## Runtime account

### Work and ordinary invocation

CrewAI owns task scheduling and model/tool execution, not just prompt construction. The frozen [boundary](boundary.md) includes the CLI, generated-project drivers, Crew, standalone Agent, Flow and retained-context callers. All evidence below is SRC-1 implementation, with source-native instructions identified as such. No execution traces, successful tests or experimental results were supplied. Runtime activation, reliability, speed and quality benefits remain unobserved.

The shipped CLI selects an explicit declarative Flow, configured JSON crew, Flow project or classic Python crew from arguments and project metadata. The classic driver invokes a project script through `uv run`; it is an entry path, not an isolation boundary (SRC-1, `lib/cli/src/crewai_cli/run_crew.py`). The ordinary Python invocation is `Crew.kickoff(inputs=...)`: checkpoint restoration can replace the instance before execution; otherwise preparation interpolates inputs and the process dispatches sequential or hierarchical work. Streaming wraps execution in a producer rather than introducing a separate task policy (SRC-1, `lib/crewai/src/crewai/crew.py`). See [RT-RTE-crew-kickoff](#rt-rte-crew-kickoff).

For sequential work, runtime code advances through tasks. Explicit task context selects task outputs; the unspecified-context sentinel selects accumulated outputs, while a false context selects none. Synchronous tasks wait for pending asynchronous tasks before using their results. Hierarchical mode creates or uses a manager agent; that manager receives delegation tools and executes the scheduled tasks. Thus there are two decision levels: code selects eligible tasks and context; the model selects intermediate actions and final responses. Role strings identify delegation recipients, while Crew/Task IDs identify execution and event scopes (SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`).

`Task` calls `Agent.execute_task`. The agent builds the task/schema/context prompt, recalls memory, retrieves knowledge, prepares tools and applies training instructions before executor invocation. Memory recall queries the task description with limit five and appends formatted matches; this is delivery, not evidence of compliance. The executor starts a new message frame unless resuming, chooses native function calling when supported and tools exist, otherwise uses ReAct parsing. Model calls use the messages plus available schemas or tool descriptions. Tool observations re-enter the loop until a final answer, an iteration-limit finalization attempt or an error. Optional human feedback precedes executor memory saving. Task guardrails then run on the returned candidate; callbacks and file output follow, and Crew produces its aggregate output. Events expose lifecycle and tool results but are not outcome verification (SRC-1, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/agents/crew_agent_executor.py`, `lib/crewai/src/crewai/task.py`).

### Material routes and forcing cases

The source checks selected four forcing cases that defeat broader guarantees:

1. **Native versus ReAct dispatch.** Both have pre-tool veto points, but they reach different execution helpers. Native unsupported-tool errors can fall back to ReAct. A claim about one helper alone would not cover ordinary tools: [RT-RTE-tool-dispatch](#rt-rte-tool-dispatch).
2. **Guardrail rejection after effects.** The executor saves memory before returning to Task's output guardrails. Retrying can repeat agent work and tool effects; it does not undo an earlier tool call or memory write. Standalone kickoff instead applies its own output guardrail before its kickoff memory save: [RT-RTE-output-guardrail](#rt-rte-output-guardrail), [RT-RTE-agent-kickoff](#rt-rte-agent-kickoff).
3. **Delegated context versus global visibility.** The delegation tool passes a newly constructed task and the selected context, not the parent's whole transcript. The selected agent still has its own prompt, tools and memory access. The frame boundary is not a security sandbox: [RT-RTE-agent-delegation](#rt-rte-agent-delegation).
4. **Durable Flow versus mediated tool execution.** Flow invokes Python methods directly, with step hooks and optional feedback. Those methods can call agents, direct models, external services or arbitrary application code without becoming calls through the agent tool helper. State hydration and checkpoint resumption also differ: loading a state UUID alone does not mean completed methods are skipped. Therefore neither tool veto nor output validation is universal mediation: [RT-RTE-flow-execution](#rt-rte-flow-execution).

These are inspected code cases, not executed experiments. The guarantee owners, enforcement points and limits are [RT-CLM-tool-veto](#rt-clm-tool-veto) and [RT-CLM-output-validation](#rt-clm-output-validation). Async ReAct hook helpers and Task async guardrail call sites were inspected; exhaustive provider-specific and experimental-executor equivalence was not established. The standalone native hook site was inspected separately.

### Controls, context and change admission

The capability surface includes supplied Python tools, delegation, memory tools, application/MCP adapters and progressively disclosed skills. Crew prepares these from configured flags and objects. The current grant set is the actual tool list plus configured callbacks and adapter credentials, not every advertised integration. No deployed grant list, service permissions or operating-system/container envelope was supplied. In this revision `allow_code_execution` is deprecated and warns that CodeInterpreterTool is no longer available; the flag is not evidence of a shipped local sandbox (SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/agent/core.py`). Python callbacks and Flow bodies retain the authority of their process; an adapter's remote effects depend on its external contract.

Working context is controlled through selected prior-task outputs, delegated frames, optional memory/knowledge retrieval, skill disclosure and context-overflow summarization. Summarization removes non-system history and replaces it with model-produced text while preserving system messages and attached files. It provides continuity but not a losslessness guarantee: [RT-RTE-context-summary](#rt-rte-context-summary). Separate task/delegation frames resemble stack frames only in selected input and returned output; memory, tools and application side effects can escape the frame, and prompt text is not a dereferenceable heap pointer.

Runtime instruction changes enter through configured skills and training artifacts. A foreground model can request one catalogued skill's full instructions through a tool; it cannot thereby select an arbitrary uncatalogued skill. Training runs explicitly collect human feedback and model revisions, then use an evaluator model to generate persisted suggestions keyed by role. Later prompts append those suggestions as instructions. These are distinct admission mechanisms, not weight training: [RT-RTE-skill-disclosure](#rt-rte-skill-disclosure), [RT-RTE-crew-training](#rt-rte-crew-training). Retention and revision internals of unified memory, knowledge, Flow feedback lessons and reset paths remain for the memory analyst; the runtime identifies their callers rather than declaring their storage policies.

Model mutability is local to [RT-CMP-agent-llm](#rt-cmp-agent-llm), [RT-CMP-memory-llm](#rt-cmp-memory-llm) and [RT-CMP-memory-embedder](#rt-cmp-memory-embedder). The source exposes model selection and invocation, not provider training internals. Retained instructions can change future prompts independently of provider parameter changes.

Additional inspected SRC-1 coverage beyond the boundary's initial paths comprises `lib/crewai/src/crewai/hooks/tool_hooks.py`, `lib/crewai/src/crewai/utilities/tool_utils.py`, `lib/crewai/src/crewai/tools/tool_usage.py`, `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`, `lib/crewai/src/crewai/utilities/agent_utils.py`, `lib/crewai/src/crewai/utilities/llm_utils.py`, `lib/crewai/src/crewai/utilities/training_handler.py`, `lib/crewai/src/crewai/utilities/file_handler.py`, `lib/crewai/src/crewai/skills/tool.py` and the native tool hook block in `lib/crewai/src/crewai/experimental/agent_executor.py`. These supply implementation evidence only. Searches located alternate call sites; they do not establish exhaustive provider coverage or execution outcomes.

## Shared records

### Components

#### RT-CMP-agent-llm
Label: Agent LLM and evaluator bindings

Source-native identity: configured `Agent.llm`, manager LLM, optional function-calling LLM and the TaskEvaluator's original-agent LLM. Representational form: distributed-parametric model, consumed through symbolic SDK interfaces and natural-language messages. Storage substrate: external provider/service or caller-supplied BaseLLM; weights are not stored in the inspected Crew state. Parameters are not updated by the inspected kickoff or training path; provider-side parameter changes are uninspected. Exact model version is not universally pinned: strings, configuration dictionaries, supplied instances and environment fallback are accepted, and overlay resolution can replace the declared agent binding. Mutable service endpoints may resolve to another model; their behavior is outside SRC-1. The evaluator reuses the original agent's LLM, not an independent answer oracle (SRC-1, `lib/crewai/src/crewai/utilities/llm_utils.py`, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/utilities/evaluators/task_evaluator.py`).

> if isinstance(llm_value, str):
>     try:
>         return LLM(model=llm_value)
> --- `lib/crewai/src/crewai/utilities/llm_utils.py`

> self.llm = original_agent.llm
> self.original_agent = original_agent
> --- `lib/crewai/src/crewai/utilities/evaluators/task_evaluator.py`

#### RT-CMP-memory-llm
Label: Memory analysis LLM

Source-native identity: `Memory.llm`, separately configurable from the agent. Representational form: distributed-parametric model; storage substrate and provider internals external or supplied by caller. Default model name is `gpt-5.4-mini`, not an immutable weight digest. Memory creates an isolated non-streaming copy where possible. Inspected code changes configuration, not parameters; provider-side mutation is uninspected and a mutable endpoint can resolve to a different model. This component supplies analysis for retained-context machinery, whose detailed routes are left to the memory member (SRC-1, `lib/crewai/src/crewai/memory/unified_memory.py`).

> llm: Annotated[BaseLLM | str, PlainValidator(_passthrough)] = Field(
>     default="gpt-5.4-mini",
>     description="LLM for analysis (model name or BaseLLM instance).",
> )
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

#### RT-CMP-memory-embedder
Label: Memory embedder

Source-native identity: configurable `Memory.embedder`, with default OpenAI embedding function. Representational form: distributed-parametric encoder producing dense numerical representations. Storage substrate: external embedding implementation; output storage belongs to memory. The caller may supply a callable or provider configuration. Exact encoder version is not pinned by the default provider specification; endpoint remapping is possible and provider internals are uninspected. No parameter update is present in this inspected construction path; this does not establish fixed provider weights or absence of learning through retained text (SRC-1, `lib/crewai/src/crewai/memory/unified_memory.py`).

> spec: OpenAIProviderSpec = {"provider": "openai", "config": {}}
> return build_embedder(spec)
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

### Operative objects

#### RT-OBJ-trained-agents
Label: Trained agents data

Source-native identity: trained-agent file selected by Crew configuration, environment or default; distinct from the raw per-agent/per-iteration training data. Natural-language `suggestions` are interpreted by the next agent LLM; role keys and evaluation fields are symbolic structure. Substrate: local pickle file through CrewTrainingHandler/PickleHandler. Its later consumer appends suggestions by agent role rather than loading modified weights. File initialization overwrites prior data and training failure clears both files; no version-history rollback is established. A trusted-artifact requirement follows from the consumer using pickle loading, not from a claim that this artifact is harmless text (SRC-1, `lib/crewai/src/crewai/utilities/training_handler.py`, `lib/crewai/src/crewai/utilities/file_handler.py`, `lib/crewai/src/crewai/agent/core.py`).

> with open(self.file_path, "rb") as file:
>     return pickle.load(file)  # noqa: S301
> --- `lib/crewai/src/crewai/utilities/file_handler.py`

#### RT-OBJ-skill
Label: Skill instruction block

Source-native identity: `Skill` instruction content loaded from configured paths, inline text or registry references. Natural-language instructions and descriptions are interpreted by the agent; catalog labels/disclosure levels have symbolic selection rules. Substrate: source skill file or resolved Skill object plus returned instruction text in the execution's messages. The loader formats instructions in a named block; resource listings are not proof that resource bodies were executed. Source registration fixes repository code, not the future content of a user's registry or filesystem (SRC-1, `lib/crewai/src/crewai/skills/loader.py`, `lib/crewai/src/crewai/skills/tool.py`).

> activated = activate_skill(skill, source=self.source)
> --- `lib/crewai/src/crewai/skills/tool.py`

> return format_skill_context(activated, label=skill_name)
> --- `lib/crewai/src/crewai/skills/tool.py`

### Routes

#### RT-RTE-crew-kickoff
Label: Crew kickoff task execution

Caller triggers Crew with interpolated inputs and optional files/checkpoint. Crew code owns scheduling; agent or manager model owns intermediate action selection. Symbolic task/configuration objects and natural-language prompts run in the host Python process. Task IDs and Crew IDs scope state and events; role names guide agent selection. Task context is selected rather than necessarily all prior messages. Agent retrieval adds memory and knowledge; detailed storage/admission is deferred to the memory member. Final output is TaskOutput/CrewOutput, optionally streamed. Failure emits events and rethrows; the finally block drains memory writes and clears files. A timeout cancels a future but does not prove already-running tool side effects were stopped (SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/task.py`).

- Immediate return: CrewOutput, or streaming wrapper whose producer runs kickoff.
- Later read-back: checkpoint restoration can re-enter kickoff; training and memory read-back are separate mechanisms, not inferred from CrewOutput alone.
- Delegated visibility: manager/agent receives selected task context and tools; see [RT-RTE-agent-delegation](#rt-rte-agent-delegation).
- Selection predicate: configured process and ordered tasks, with conditional skip, async execution and task.context controls.
- Invalidation or expiry: fresh executor invocation resets messages unless resuming; file context is cleared in kickoff finalization.
- Activation or effect: code dispatches agent work and returns task outputs; semantic response to context is unobserved.
- Evidence limits: implementation only; no deployed credentials, successful outputs or isolation envelope supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.process == Process.sequential:
>     result = self._run_sequential_process()
> elif self.process == Process.hierarchical:
>     result = self._run_hierarchical_process()
> --- `lib/crewai/src/crewai/crew.py`

> return (
>     aggregate_raw_outputs_from_task_outputs(task_outputs)
>     if task.context is NOT_SPECIFIED
>     else aggregate_raw_outputs_from_tasks(task.context)
> )
> --- `lib/crewai/src/crewai/crew.py`

#### RT-RTE-tool-dispatch
Label: Mediated tool dispatch

Endpoints: agent model response to registered Python tool function and observation back to the model. Executor chooses native dispatch or ReAct based on support and tool presence; model proposes name/arguments, code resolves permitted tools, pre-tool hooks can veto, and post-tool hooks can replace observations. Native usage limits and cache handling can avoid calling the function. The synchronous and asynchronous ReAct helpers also run the pre-tool hook. Native standalone execution has its own inspected hook block. There is no automatic human decision on every call; a configured hook may request approval. Tool implementation and external service determine actual effect authority (SRC-1, `lib/crewai/src/crewai/agents/crew_agent_executor.py`, `lib/crewai/src/crewai/utilities/tool_utils.py`, `lib/crewai/src/crewai/hooks/tool_hooks.py`, `lib/crewai/src/crewai/experimental/agent_executor.py`).

- Immediate return: formatted observation, blocked/error observation or final tool result when configured as final.
- Later read-back: tool cache may reuse a result; durable external changes depend on the particular tool and are not uniformly specified.
- Delegated visibility: function receives selected arguments; hook receives agent/task/crew context; model receives formatted, possibly replaced result rather than necessarily raw output.
- Selection predicate: model-selected name must resolve to available tools; native support selects route and unsupported-native errors can fall back to ReAct.
- Invalidation or expiry: usage counters and cache can affect later calls; universal external-effect expiry is inapplicable — effects belong to each tool/service.
- Activation or effect: nonblocked calls invoke host functions; their subprocess, network or filesystem authority is not confined by these helpers.
- Evidence limits: coverage is inspected helpers, not every direct SDK call, arbitrary callback, provider-hosted tool or remote worker.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if hook_blocked:
>     result = f"Tool execution blocked by hook. Tool: {func_name}"
>     raw_tool_result = result
> --- `lib/crewai/src/crewai/agents/crew_agent_executor.py`

> raw_result = available_functions[func_name](**(args_dict or {}))
> --- `lib/crewai/src/crewai/agents/crew_agent_executor.py`

> tool_result = tool_usage.use(tool_calling, agent_action.text)
> --- `lib/crewai/src/crewai/utilities/tool_utils.py`

#### RT-RTE-agent-delegation
Label: Agent coworker delegation

Owner: calling agent model selects coworker, task and context; code matches sanitized roles against available agents and invokes the selected agent. A manager can receive this capability, but it is not an unrestricted worker launcher. The callee receives a new Task and supplied context, then uses its own execution preparation. The parent receives the returned result or an error string. This isolates transcript selection, not process privileges (SRC-1, `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`, `lib/crewai/src/crewai/crew.py`).

- Immediate return: selected agent's task result, or localized coworker/execution error.
- Later read-back: uninspected — memory effects follow the callee's configured memory path; delegation itself defines no dedicated retained artifact.
- Delegated visibility: supplied task/context plus callee's own instructions, retrieval and tools, not the caller's entire message list.
- Selection predicate: sanitized role equality within the tool's configured agent list; first match is used.
- Invalidation or expiry: delegated task frame terminates on return; external and memory effects can survive it.
- Activation or effect: calls selected_agent.execute_task and returns its result.
- Evidence limits: no exercised delegation, isolation test or successful coordination evidence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> selected_agent = agent[0]
> --- `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`

> return selected_agent.execute_task(task_with_assigned_agent, context)
> --- `lib/crewai/src/crewai/tools/agent_tools/base_agent_tools.py`

#### RT-RTE-output-guardrail
Label: Task output guardrail retry

Trigger: candidate TaskOutput after agent execution. Configured callable or LLM-backed guardrail judges it. Code accepts/transforms successful results or re-executes with validation-error context until the retry cap, then raises. This is open task execution with bounded validation retries, not a reference-answer experiment. Caller supplies checks; a model judge alone supplies no answer oracle. A callback guardrail can implement an oracle, but none is supplied here. Optional human feedback is earlier in the executor and is not synonymous with this gate. Source: SRC-1, `lib/crewai/src/crewai/task.py`, `lib/crewai/src/crewai/agents/crew_agent_executor.py`.

- Immediate return: accepted/replaced TaskOutput or exception after retry exhaustion.
- Later read-back: executor memory saving can precede Task rejection; rejection does not retract that save.
- Delegated visibility: guardrail receives output; retrying agent receives failure context and tools.
- Selection predicate: configured guardrail(s), success flag and retry budget.
- Invalidation or expiry: rejected candidate is replaced for Task progression; prior side effects are not rolled back by this loop.
- Activation or effect: blocks Task progression or changes the returned candidate; does not preauthorize every tool effect.
- Evidence limits: valid schema or model approval establishes neither truth nor absence of harmful effects.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._save_to_memory(formatted_answer)
> return {"output": formatted_answer.output}
> --- `lib/crewai/src/crewai/agents/crew_agent_executor.py:268-269`

> if attempt >= self.guardrail_max_retries:
>     guardrail_name = (
>         f"guardrail {guardrail_index}"
>         if guardrail_index is not None
>         else "guardrail"
>     )
>     raise Exception(
>         f"Task failed {guardrail_name} validation after {self.guardrail_max_retries} retries. "
>         f"Last error: {guardrail_result.error}"
>     )
> --- `lib/crewai/src/crewai/task.py:1382-1391`

#### RT-RTE-agent-kickoff
Label: Standalone Agent kickoff

Trigger/principal: caller supplies messages, response format and files without Crew. Agent prepares an AgentExecutor, binds tools and model, and invokes it; in an event loop kickoff returns its async coroutine. Checkpoint restoration can supply a resumed agent. Finalization applies the standalone guardrail before saving kickoff output to memory. This differs from Task's post-executor gate. The agent model owns next actions; host code owns preparation, retry/finalization and terminal LiteAgentOutput (SRC-1, `lib/crewai/src/crewai/agent/core.py`).

- Immediate return: LiteAgentOutput, or coroutine inside an event loop.
- Later read-back: memory save/recall and checkpoints can deliver retained context later; standalone detailed memory transformations are deferred to the memory member.
- Delegated visibility: executor receives prepared prompt, selected history/files and parsed tools; native tool hook coverage is sampled in the standalone executor.
- Selection predicate: caller messages and configured tools/model; optional response schema and agent guardrail.
- Invalidation or expiry: new executor unless resuming; retained memory is not invalidated merely by finishing a kickoff.
- Activation or effect: invokes agent model/tool execution and finalization; successful semantics unobserved.
- Evidence limits: standalone initialization and native veto were inspected; full experimental executor parity was not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._save_kickoff_to_memory(messages, output.raw)
> --- `lib/crewai/src/crewai/agent/core.py`

#### RT-RTE-flow-execution
Label: Flow method execution and restore

Caller triggers Flow kickoff with inputs or checkpoint/fork configuration. Flow runtime selects start methods and eligible downstream methods from its definition, invokes async bodies or sync Python bodies in threads, and records outputs. Shared state can be loaded by UUID; checkpoint restoration additionally tracks completed execution. Inputs can override restored state fields. Step/output/execution-end interception can modify control payloads. HumanFeedbackPending saves state/context and returns a pending object; ordinary completion returns the last method output after output/end interception. This is symbolic graph/state control around arbitrary application bodies, not a mandatory model loop (SRC-1, `lib/crewai/src/crewai/flow/runtime/__init__.py`).

- Immediate return: final method output or pending-feedback object; other execution failures propagate.
- Later read-back: persistence.load_state reloads UUID state; fork hydration assigns a new state ID unless explicitly pinned; checkpoint replay is distinct from state reload.
- Delegated visibility: method parameters and shared Flow state; nested agents get whatever the method supplies, not an automatic whole-Flow transcript.
- Selection predicate: defined start/listener/router conditions, completed-method resumption state and optional hook edits.
- Invalidation or expiry: restore is single-shot for checkpoint flag; missing persisted state logs and proceeds without hydration; application state expiry is uninspected.
- Activation or effect: runtime directly invokes method bodies; sync thread execution is scheduling isolation, not an OS security sandbox.
- Evidence limits: arbitrary bodies may bypass agent tool hooks; remote services and deployed persistence contracts are external, and exactly-once side effects are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if asyncio.iscoroutinefunction(method):
>     result = await method(*args, **kwargs)
> else:
>     # Run sync methods in thread pool for isolation
>     # This allows Agent.kickoff() to work synchronously inside Flow methods
>     ctx = contextvars.copy_context()
>     result = await asyncio.to_thread(ctx.run, method, *args, **kwargs)
> --- `lib/crewai/src/crewai/flow/runtime/__init__.py`

> stored_state = self.persistence.load_state(restore_uuid)
> --- `lib/crewai/src/crewai/flow/runtime/__init__.py`

#### RT-RTE-context-summary
Label: Context overflow summarization

Trigger: recognized context-length exception with respect_context_window enabled. Runtime code requests model summaries and replaces history; disabled summarization raises SystemExit. This is working-context removal/replacement, not a database-memory revision. Original system messages and attached files survive; non-system content survives through the model's summary rather than a guaranteed verbatim tail. No source-supported automatic reload of removed verbatim turns is established by this helper (SRC-1, `lib/crewai/src/crewai/utilities/agent_utils.py`, `lib/crewai/src/crewai/agents/crew_agent_executor.py`).

- Immediate return: in-place modified message list, followed by another loop attempt; disabled mode exits.
- Later read-back: next model invocation receives the retained summary within the run.
- Delegated visibility: summarizer receives history chunks; foreground model later sees preserved system messages plus merged summary/files.
- Selection predicate: exception classification and configured respect_context_window; code separates system and non-system messages.
- Invalidation or expiry: original non-system message list is cleared and replaced; summary lasts until later replacement or executor reset.
- Activation or effect: changes model-visible context; fidelity and successful continuation remain unobserved.
- Evidence limits: summary request is not a lossless transformation or proof of improved capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.messages.clear()
> self.messages.extend(system_messages)
> self.messages.append(summary_message)
> --- `lib/crewai/src/crewai/utilities/agent_utils.py`

#### RT-RTE-skill-disclosure
Label: Catalogued skill disclosure

Admission trigger: caller configures skills; ordinary path loading preserves metadata-only disclosure, while inline/already-active skills can carry instructions immediately. Model proposes a skill label through LoadSkillTool; code vetoes unknown labels and activates catalogued content. The returned instruction block enters model context. Guidance is the configured description and instruction body, not an evaluator reference answer. Operating mode is open request handling with selective instruction loading. No human approval per disclosure is wired here; caller selection of the catalog is a different human/software contribution. Recovery is an unavailable-skill response; changing/removing the configured source affects future loads but does not retract already-delivered text. This route admits instructions into an invocation, not an automatic edit to skill files or product machinery (SRC-1, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/skills/tool.py`, `lib/crewai/src/crewai/skills/loader.py`).

- Immediate return: formatted instruction block for [RT-OBJ-skill](#rt-obj-skill), or available-label error.
- Later read-back: static configured skills are not use-derived memory; changed source content may be loaded later but no automatic skill-write route is established here.
- Delegated visibility: only selected skill instruction content is returned by the loader; other skills can remain metadata-only.
- Selection predicate: model-selected exact label resolved through the current catalog.
- Invalidation or expiry: invocation text remains until reset/compaction; source replacement affects later loads, not an automatic rollback of this context.
- Activation or effect: delivers instructions and emits usage event; event or delivery alone does not establish behavioral compliance.
- Evidence limits: registry service behavior and per-content human authorship are unresolved; no answer oracle or benefit evidence supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> skill = self.catalog.get(skill_name)
> --- `lib/crewai/src/crewai/skills/tool.py`

#### RT-RTE-crew-training
Label: Crew feedback training admission

Trigger: caller requests a finite number of training iterations and output filename. Training copies Crew, enables task human input, disables delegation, initializes files and runs kickoff repeatedly. The executor stores initial output/human feedback and revised output. TaskEvaluator, using the original agent's LLM, proposes consolidated suggestions and score from those records; code rejects missing required record fields but otherwise saves evaluator output by role. A human supplies feedback on task content, not necessarily approval of each final suggestion. Evaluator instructions request preserving specific feedback and comparing initial/revised outputs. Operating mode is bounded repeated feedback training, not an independently controlled causal experiment. Human feedback is evaluative input, not a supplied expected-answer oracle. Software admits parsed suggestions; no separate per-suggestion human veto is shown in this save path. File initialization overwrites and failure clears files; a versioned rollback mechanism is not established (SRC-1, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/agents/crew_agent_executor.py`, `lib/crewai/src/crewai/utilities/evaluators/task_evaluator.py`, `lib/crewai/src/crewai/agent/core.py`).

- Immediate return: train returns after saving evaluated suggestions, or raises after clearing training files.
- Later read-back: current training prompts consume feedback by agent ID; later ordinary prompts read [RT-OBJ-trained-agents](#rt-obj-trained-agents) by role.
- Delegated visibility: training disables delegation; evaluator receives aggregated initial outputs, feedback and revised outputs.
- Selection predicate: training_data has agent ID, required nonempty fields, then saved role matches later agent.role.
- Invalidation or expiry: new training initializes/overwrites; errors clear data; no time expiry in the inspected consumer.
- Activation or effect: retained suggestions are appended as imperative prompt instructions; exercised influence and improved performance remain unobserved.
- Evidence limits: evaluator score is not causal improvement evidence; no weight update or automatic product-code revision follows from this path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for task in self.tasks:
>     task.human_input = True
> 
> for agent in self.agents:
>     agent.allow_delegation = False
> --- `lib/crewai/src/crewai/crew.py`

> CrewTrainingHandler(filename).save_trained_data(
>     agent_id=str(agent.role),
>     trained_data=result.model_dump(),
> )
> --- `lib/crewai/src/crewai/crew.py`

> task_prompt += (
>     "\n\nYou MUST follow these instructions: \n - "
>     + "\n - ".join(trained_data_output["suggestions"])
> )
> --- `lib/crewai/src/crewai/agent/core.py`

This route retains feedback-derived instructions and input/outcome records, not necessarily formulated explanatory theories or content-directed criticism of those theories. No theory-builder classification is inferred from the training label. Learning as improved future capacity, reflection and exercised self-improvement remain unestablished independently: the retained behavioral-authority path is wired, but subsequent operation causally depending on the change and objective improvement have no supplied evidence.

### Claims

#### RT-CLM-tool-veto
Label: Tool-call hook veto contract

Claimed operation: returning False from a before-tool hook blocks the call; the adapter maps that to HookAborted and reports a blocked result. Owner: hook dispatcher and tool execution helpers. Enforcement point: pre-tool dispatch before function invocation. Guarantee strength: protocol. Covered paths: inspected native Crew, standalone native and sync/async ReAct helpers in [RT-RTE-tool-dispatch](#rt-rte-tool-dispatch). Alternate paths: direct functions, direct model/provider calls, callback bodies, Flow methods and remote-service internals are not all mediated there. Required external contract: hooks must be registered and correctly implement policy; trusted Python code must voluntarily use the intercepted paths. This is not a deployment-wide prevention guarantee (SRC-1, `lib/crewai/src/crewai/hooks/tool_hooks.py`, `lib/crewai/src/crewai/utilities/tool_utils.py`, `lib/crewai/src/crewai/agents/crew_agent_executor.py`, `lib/crewai/src/crewai/experimental/agent_executor.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if result is False:
>     raise HookAborted(reason="before_tool_call hook returned False")
> return False
> --- `lib/crewai/src/crewai/hooks/tool_hooks.py`

#### RT-CLM-output-validation
Label: Output-validation progression contract

Claimed operation: Task guardrails validate output before proceeding to the next task. Owner: Task runtime; enforcement point: after agent execution and before assigning Task.output/callbacks. Guarantee strength: protocol, conditional on configured checks. Covered path: Task guardrail loop and its async call sites; standalone Agent uses a different finalization gate. Alternate paths: direct agent execution, arbitrary Flow methods and effects already performed by tools are not prevalidated by this gate. Required external contract: callable/model judge quality and any reference data are supplied outside the loop. A post-step hook can replace the already-checked payload; callbacks are trusted code. Thus the gate establishes configured progression control, not truth of the ultimate output or a transactional effect boundary (SRC-1, `lib/crewai/src/crewai/task.py`, `lib/crewai/src/crewai/agent/core.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> description="Function or string description of a guardrail to validate task output before proceeding to next task",
> --- `lib/crewai/src/crewai/task.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-training-instructions
Label: Trained suggestions to task prompt

Consumer: later agent LLM through task-prompt preparation. Channel: role-keyed suggestions loaded from the trained-agent pickle file and appended as natural-language instructions. Force: imperative model guidance, not symbolic enforcement of compliance. Horizon: later task invocations and runs while the selected file and role mapping remain available. This authority path is separate from physical pickle decoding authority at file load. See [RT-RTE-crew-training](#rt-rte-crew-training) for admission, rejection and evidence limits; the quoted prompt append there supplies the minimum passage. SRC-1, `lib/crewai/src/crewai/agent/core.py`.

#### RT-BAP-skill-instructions
Label: Loaded skill to model context

Consumer: foreground agent LLM. Channel: LoadSkillTool result containing formatted instruction text, or configured already-active skill context. Force: natural-language guidance, not a privilege grant or mandatory parser rule. Horizon: current execution until message reset or compaction; source remains available for later loading. See [RT-OBJ-skill](#rt-obj-skill) and [RT-RTE-skill-disclosure](#rt-rte-skill-disclosure) for exact consumer delivery and admission limits. SRC-1, `lib/crewai/src/crewai/skills/tool.py`, `lib/crewai/src/crewai/skills/loader.py`.

## Annotations

none
