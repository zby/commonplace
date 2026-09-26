---
type: types/agentic-system-analysis-result.md
description: 'Complete code-grounded analysis of JAZ: execution, memory, revision and evidence limits at the frozen
  repository boundary.'
run-id: AAS-2026-09-26-jaz-01
system: JAZ
run-date: '2026-09-26'
result-disposition: complete
target-class: embedded inner runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
analysis-cutoff: '2026-09-26'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: not-determinable
      basis: null
      note: Concrete routes establish knowledge from console histories, enforcement from replay/workflow execution
        and afforded learning consumption from rollout export. Arbitrary retained objects passed to later invokes
        can carry other authority; their descriptions and bindings do not constrain a complete union.
      records:
      - OBJ-5
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-13
      values: []
    curation_operations:
      assessment: absent
      basis: null
      note: No shipped policy implementing a controlled curation operation over retained memories was found; generic
        message edits, display truncation, acquisition and code generation are not such a policy.
      records:
      - ABS-1
      values: []
    distilled_form:
      assessment: known
      basis: afforded
      note: Executable Python functions/packages are the transformed behavior-shaping artifact. Comments may survive
        leaf code, but no retained semantic summary or parameter update is produced.
      records:
      - OBJ-9
      - RTE-12
      values:
      - symbolic
    faithfulness_tested:
      assessment: known
      basis: wired
      note: No retained execution evidence in the frozen shipped tree tests dependence on recalled content; divergence
        comparison code and source comments about excluded experiments cannot establish yes.
      records:
      - ABS-2
      values:
      - 'no'
    learning_scope:
      assessment: known
      basis: afforded
      note: The supported route replays the recorded run with original inputs and child order. Parameterized functions
        permit experimentation but establish no cross-task learning workflow.
      records:
      - RTE-12
      values:
      - per-task
    learning_timing:
      assessment: known
      basis: afforded
      note: The qualifying write appends code during the run and finalizes on InvokeExit; later operator execution
        is activation, not a second learning transformation.
      records:
      - RTE-12
      values:
      - online
    lineage:
      assessment: not-determinable
      basis: null
      note: Trace extraction establishes recorder/workflow lineage, but opaque imported objects and returned values
        have no constrained derivation; a complete union is unsupported.
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-8
      - OBJ-9
      - OBJ-10
      values: []
    read_back_direction:
      assessment: known
      basis: afforded
      note: Console cross-invoke history and replay supply are wired; inspection of previously accumulated console
        objects, workflow execution and trainer export afford requested consumption. Ordinary same-invoke history
        reads are excluded.
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-13
      values:
      - pull
      - push
    read_back_signal:
      assessment: known
      basis: wired
      note: Automatic delivery selects retained scope material for a later invoke, console session history, or the
        next positional replay response. No semantic search or matching of saved invocation identity selects a response;
        live invoke IDs track bookkeeping.
      records:
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      values:
      - coarse
    representational_form:
      assessment: not-determinable
      basis: null
      note: Known text, Python, JSON and token structures do not classify arbitrary live inputs/results retained
        and consumed alongside their display summaries.
      records:
      - OBJ-5
      - OBJ-6
      values: []
    storage_substrate:
      assessment: known
      basis: wired
      note: JAZ-owned retention is Python objects and optional filesystem outputs; remote state behind caller objects
        is excluded, not inferred from their references.
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-9
      - OBJ-10
      values:
      - files
      - in-memory
    trace_learning:
      assessment: known
      basis: afforded
      note: WorkflowReplay automatically creates durable behavior-shaping Python from executed traces and supplies
        an executable entry point. Reuse is afforded, not observed; raw replay and rollout accumulation do not independently
        qualify.
      records:
      - RTE-12
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: afforded
      note: InvokeEnter, LLMQueryExit, REPLExecEnter, REPLExecExit and InvokeExit feed workflow code generation.
      records:
      - RTE-12
      values:
      - event-streams
    write_agency:
      assessment: not-determinable
      basis: null
      note: Automatic recording/materialization and manual host population/editing are established for concrete
        routes. The producer and write process of opaque retained state passed to a later invoke are unconstrained;
        source-wide agency for the full declared scope cannot be attributed from the handoff alone.
      records:
      - OBJ-5
      - RTE-8
      - RTE-9
      - RTE-10
      - RTE-11
      - RTE-12
      - RTE-13
      values: []
  scope: 'Shipped JAZ material accumulated or changed through use with a later consumer invocation: retained objects/history
    explicitly passed or propagated to another invoke; console main/helper histories including live payloads; ATIF
    retention/replay; trace-derived workflow packages and their afforded execution; token rollout retention/export.
    Ordinary same-invoke message buffers and history reads are context inventory only, excluded from the comparison.
    External stores behind opaque objects, external trainers, installed custom protocols/hooks, static configuration
    and observability-only sinks are outside this boundary.'
---

# JAZ agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/jaz.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-01/memory-report.md`
**Memory analysis report SHA-256:** b13893eb63d54c5554a945d41eccc89ef9c3edb8a659d79a44d50d503afc22b7

Run AAS-2026-09-26-jaz-01 analyses JAZ at commit `0803d4971be785e95b80054b02259664d70fa3da`, cutoff 2026-09-26. Coordinator model: GPT-6; exact runtime model identifier unavailable. Method: `kb/instructions/analyse-agentic-system/SKILL.md`, with its mandatory memory and epistemic procedures. No prior system analysis supplied the findings.

## Boundary and evidence

Evidence basis: static source code and shipped documentation at the pinned commit, inspected on 2026-09-26; code-grounded. The target is an embedded inner runtime, including its console, hook system, replay utilities and configurable Python executor. Boundary kind: complete artifact, partial loop. It accepts open caller requests and returns values or exceptions; the enclosing application's tasks, supplied tools, deployment isolation and remote model services remain outside it.

The analysis asks what the package actually schedules, exposes, checks and retains. Model-provider internals are excluded, preventing weight-fixity and training claims. Host tools and custom backends/protocols are excluded, preventing a universal effects or isolation guarantee. Benchmark experiments and the companion evaluation repository are outside this source allowlist; this framework analysis does not establish their outcomes. No live model execution or adversarial sandbox test was performed.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | Git | `https://github.com/jaz-lang/jaz` | `0803d4971be785e95b80054b02259664d70fa3da` | implementation | Invocation, agent loop, Python REPL, return/code/budget hooks, console settings and memory/replay routes retained below | `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/repl/python_repl.py`, `src/jaz/repl/permissions.py`, `src/jaz/repl/compiler.py`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/builtin/repl_code_hooks.py`, `src/jaz/hooks/builtin/budget_pool.py`, `src/jaz/llm/_litellm.py`, `src/jaz/console.py`, plus specialist anchors on canonical records | External providers and caller-defined components uninspected; no run trace or causal experiment |
| SRC-2 | Git | `https://github.com/jaz-lang/jaz` | `0803d4971be785e95b80054b02259664d70fa3da` | doctrine/design; code comments are design claims rather than executed evidence | README and operational docstrings adjoining inspected code | `README.md:1-15`, quoted comments on the records below | Documentation does not prove activation, isolation or improved task capacity |

Access root: `/home/zby/llm/commonplace/related-systems/jaz-lang--jaz`. All source reads used commit-addressed Git blobs; neither checkout contents nor changing HEAD supplied evidence. Quotes below refer to this full revision.

## Shared records

### Components

CMP-1 — Invocation and hook dispatcher boundary, symbolic Python. The caller supplies inputs and local hooks; the package constructs a per-invoke agent and recursive callable. Invocation identity includes invoke ID, parent invoke ID, depth and parent iteration. Status: wired. SRC-1 `src/jaz/invoke.py:495-558`, `src/jaz/_agent.py:912-943`.

CMP-2 — PythonREPL, symbolic in-process compiler/executor with per-invoke locals, import/file/attribute policy and execution guards. Status: wired within the inspected implementation. Host callable effects remain external contracts, not transformed source governed by this compiler. SRC-1 `src/jaz/repl/python_repl.py:1877-1909`, `src/jaz/repl/permissions.py:171-228`.

CMP-3 — Configured LLM backend, distributed-parametric inference reached through a model-name string and messages. The LiteLLM path sends completion/acompletion requests; it does not itself train parameters. Exact weight identity and provider parameter changes are uninspected. Version pinning: afforded through caller-selected identifiers, not guaranteed immutable weights; mutable endpoint resolution remains a provider contract. SRC-1 `src/jaz/llm/_litellm.py:142-161,244-271`.

> params: dict[str, Any] = {"model": model, "messages": messages}
> --- `src/jaz/llm/_litellm.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

### Operative objects

OBJ-1 — Caller inputs, scoped values and tool bindings. Ordinary Python objects plus their rendered descriptions; natural-language instructions and symbolic functions coexist with arbitrary opaque payloads. Inputs are local to an invoke; scope is the propagation channel. Status: wired. SRC-1 `src/jaz/invoke.py:312-317,817-845`, `src/jaz/_agent.py:897-900`.

OBJ-2 — Generated Python and terminal result. Code is a symbolic executable candidate; its returned object can be truth-apt, a policy, or an ordinary result depending on caller purpose. Per-invoke REPL locals hold the working state. Status: wired. SRC-1 `src/jaz/_agent.py:664-727,1094-1120`.

OBJ-3 — Console helper proposal and configuration representation. Request, reference, configuration snapshot and histories are text; a tagged answer/code result can propose executable settings changes. This is distinct from automatic application. Status: wired. SRC-1 `src/jaz/console.py:1021-1060,1213-1259,1376-1421`.

OBJ-4 — Per-invoke message buffer and `__history__`. In-memory, automatic trace acquisition. The buffer is model context; the history list is an agent-visible structured record holding code/text and raw exceptions. Created afresh per invoke, with no automatic transfer into a later root invoke. Comparison inclusion: none for ordinary current-run use; only an explicit later-invoke handoff through RTE-8 can make this accumulated material memory read-back. SRC-1 `src/jaz/_agent.py:968-1005`, `src/jaz/_agent.py:601-638`, `src/jaz/protocol/code_only.py:527-567`; quoted support establishes new allocation and untruncated available output.

>             repl_history: list[object] = []
> --- `src/jaz/_agent.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         return REPLHistoryEntry(
>             llm_response=content or "",
>             # Only a ``Continue`` carries ``output`` (#903 dropped it from the terminal ``Return`` /
>             # ``Raise``, whose value/exception — not agent-facing text — is the payload); a terminal
>             # turn therefore records ``""`` — see the field comment on :class:`REPLHistoryEntry`
>             # for why the empty string rather than ``None``.
>             repl_output=exec_result.output if isinstance(exec_result, Continue) else "",
>             repl_exception=repl_exception,
> --- `src/jaz/protocol/code_only.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

OBJ-5 — Explicit and scoped retained object references. In-memory mapping with arbitrary caller/agent payloads, distinct from descriptions used to render the prompt. Payload form and original derivation are unconstrained; the dictionary and description do not settle either. Objects may carry previously accumulated state, but a fresh API client alone does not establish a memory service. Comparison inclusion is conditional on accumulated or changed content reaching another invoke; ordinary unmodified inputs remain context inventory. External backing stores are excluded. SRC-1 `src/jaz/invoke.py:312-352,405-416`, `src/jaz/_agent.py:881-900`; SRC-2 `src/jaz/scope.py:31-53`.

OBJ-6 — Console ConversationHistory. In-memory ordered records of prompt, interpolated live input objects, result/exception, target variable and error flag. Transcript is a derived display, not a replacement for the objects. Default per-value repr cap is 500 characters; no turn-count cap. Status: wired. SRC-1 `src/jaz/console.py:287-359,364-408,492-512`.

OBJ-7 — Console HelperHistory. In-memory request, answer-or-code tag, content, and whether suggested code was applied. Main-history transcript plus helper-history transcript are natural-language/symbolic text inputs to the helper, not live object references. Helper content rendering cap: 4000 characters per exchange. Status: wired. SRC-1 `src/jaz/console.py:296-298,411-453,1366-1371`.

OBJ-8 — ATIF trajectory and loaded replay queues. Event-derived raw messages, per-call costs/tokens, provenance, edits and nested invocation records. In-memory, optionally JSON files written at scope end. File production is opt-in; default output_path is None. Serialized values/displays are not a reconstruction of all live REPL objects. Status: wired. SRC-1 `src/jaz/hooks/builtin/atif_trace.py:190-218,649-673,675-714`, `src/jaz/hooks/builtin/replay.py:858-875,943-1054`.

>         output_path: Where to write the trajectory JSON when the scope ends. ``None``
>             (the default) writes no file — read the documents in-memory with
>             :meth:`get_trajectories` instead.
>         indent: Indentation for the written JSON; ``None`` writes compact single-line
>             output.
> --- `src/jaz/hooks/builtin/atif_trace.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         self.output_path.parent.mkdir(parents=True, exist_ok=True)
>         trajectories = self.get_trajectories()
>         # Single root → write as object; multiple → write as array
>         data = trajectories[0] if len(trajectories) == 1 else trajectories
>         self.output_path.write_text(json.dumps(data, indent=self.indent))
> --- `src/jaz/hooks/builtin/atif_trace.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

OBJ-9 — Materialized workflow package. Durable `.py` functions and, for nested invokes, package files with child-function imports and generated `__main__`. Trace-derived executable Python; output functions accept recorded input names/types and root entry point serializes original values through repr. These are compiled operational prescriptions, not prose lessons or snapshots of a complete environment. SRC-1 `src/jaz/hooks/builtin/workflow_replay.py:179-217,298-373,375-500`.

OBJ-10 — Token-native rollout records and training sample projections. In-memory frozen TurnRecords and Rollouts, exportable JSON-compatible ids/masks/logprobs. Symbolic token data; weight version is metadata, not retained learned weights. Under token-less responses, that invoke's partial log is discarded and recording stands down. Partial aborted rollouts otherwise remain with terminal facts. SRC-1 `src/jaz/hooks/builtin/rollout.py:90-183,185-291,324-385`.

### Routes

RTE-1 — Core invocation and recursive execution. Trigger: host call to invoke/ainvoke. Owner: the host selects inputs/configuration; the model chooses Python code and recursive work; deterministic Python governs execution and return. Context: rendered inputs/scope plus carried messages; state: independent REPL locals and history for each invoke. Effects: code and supplied callables inside the host process. Immediate return: final Return value or propagated exception. Persistence: locals are invocation state unless another owner retains references; later consumers are separately inventoried below. Delegation visibility: scope propagates, ordinary inputs require explicit passing. Selection: model code plus Python control flow; invalidation: invocation end unless retained externally. Recovery: executable errors can return Continue observations; provider failure after retry can unwind; arbitrary tool side effects are not automatically rolled back. Activation and result quality are uninspected. Status: wired. SRC-1 `src/jaz/invoke.py:817-895`, `src/jaz/_agent.py:866-1122`.

> resolved_inputs = resolve_inputs(inputs)
> resolved_scope = resolve_inputs(scope)
> resolved_bound = {**resolved_scope, **resolved_inputs}
> --- `src/jaz/_agent.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> exec_result = self.repl_template.exec(
>     state, span.committed_code, str(iteration), exec_timeout_override
> )
> --- `src/jaz/_agent.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-2 — Optional return checking and revision. Trigger: a candidate Return. Owner/evaluator: ReturnType checks the declared type; ValidateReturn calls the supplied validator. These are separate check predicates using the same return-admission mechanism. A validation exception rejects the candidate, yields corrective feedback for another model turn, or terminates after configured failures; the completion backstop rechecks a replaced terminal value. The model proposes revisions; the host chooses the validator and can veto through it. Guidance consists of the task, type/predicate contract and returned error, not a built-in epistemic theory. Immediate return is withheld or released; the error is read on the next turn, within the same invocation. Scope and expiry match that invocation. The host may provide an answer oracle through its validator, but an arbitrary predicate is not evidence of one. Guarantee: protocol at hook boundaries, conditional on the hook being active and on validator meaning; no generic truth warrant or rollback of already performed actions. Status: wired. SRC-1 `src/jaz/hooks/builtin/return_hooks.py:288-360,455-521`.

> self.validator(result.return_value)
> --- `src/jaz/hooks/builtin/return_hooks.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> effects = [ModifyInvokeResult(result=Raise(exception=exc))]
> --- `src/jaz/hooks/builtin/return_hooks.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-3 — Code admission, capability grants and budget termination. Trigger: proposed code/query. Owner: host configuration and installed hooks. Compiler policies visit the AST, builtin wrappers mediate open/import/attribute access, and ValidateREPLCode can reject committed code before it runs. The model can revise rejected code; Abort stops execution. BudgetPool checks accumulated completed-call costs before another query, and rejects unknown price accounting when a cost budget is active. This is protocol enforcement on the instrumented routes, not a universal billing cap or host-process isolation proof. Calls already in flight and caller-provided tools/backends lie beyond the claim. Returned error text guides subsequent attempts; stored accounting is bookkeeping, not a memory-learning route. No approval interaction is built into each ordinary tool call on this path. Recovery is caller handling of errors; no general effect rollback. Status: wired. SRC-1 `src/jaz/repl/compiler.py:124-149,316-322`, `src/jaz/repl/permissions.py:214-228`, `src/jaz/hooks/builtin/repl_code_hooks.py:108-146`, `src/jaz/hooks/builtin/budget_pool.py:301-372`.

> self.validator(event.code)
> --- `src/jaz/hooks/builtin/repl_code_hooks.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> err = self._budget_error()
> if err is not None:
>     return [Abort(error=err)]
> --- `src/jaz/hooks/builtin/budget_pool.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-4 — Console settings proposal/admission. Trigger: a user % request. The helper proposes code using a current configuration text view and histories; the human chooses whether to execute it. Answer-tagged text is printed; code-tagged text needs a TTY and explicit y/yes before execution in the console namespace. The accepted code can change later configuration and capabilities. Consumer: the console and subsequent invokes; horizon: session, or longer if the accepted code explicitly persists settings. Helper history records applied/declined status; the return itself is not a correctness verdict. Guidance: user intent and shipped settings reference; change admission is human permission, not a supplied expected-answer oracle. Runtime errors propagate and no transaction rollback is established. Status: wired. SRC-1 `src/jaz/console.py:1021-1060,1268-1279,1376-1421`.

> answer = input("Run this? [y/N] ").strip().lower()
> if answer not in {"y", "yes"}:
>     remember(applied=False)
>     print("%: discarded — nothing was changed.")
>     return
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> exec(compile(snippet, "<jaz-settings>", "exec"), namespace)
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-5 — Caller-controlled extension and live object mutation. The host can supply tools, libraries, hooks, configured REPL/protocol/backend implementations or configuration overrides. Library.add rejects an existing name unless replacement is explicitly allowed, then assigns the object. The selection/admission owner is the caller; an agent gains that surface only when the caller exposes it. Guidance and long-term retention are application-defined; no claim of tested improvement follows from replacement. No generic rollback, expiry or correctness criterion is established for arbitrary supplied components. Immediate return and later/delegated use depend on whether the object is bound as an input, scoped or retained by the host. Status: afforded for application-defined extension; the Library mutation primitive is wired. SRC-1 `src/jaz/_library/core.py:136-157`, `src/jaz/invoke.py:289-317`.

> setattr(current_module, tool_path_parts[-1], tool)
> --- `src/jaz/_library/core.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-6 — Automatic next-turn context. Trigger: next query of the same invoke. Producer: loop response/history and observation append. Selector: current carried buffer, with installed hooks' explicit message edits. Delivery: backend messages, after reserved metadata projection. Consumer: current invoke's LLM. Status: wired context delivery; advisory/evidential authority. Comparison inclusion: excluded, since next-turn buffer assembly is ordinary current-run state rather than memory read-back. Per-output character caps are not a total-context or retention cap. SRC-1 `src/jaz/_agent.py:332-401`, `src/jaz/_agent.py:664-675`, `src/jaz/_agent.py:730-758`, `src/jaz/protocol/code_only.py:478-525`.

>         edits = span.ctx.message_edits
>         self._pending_message_edits = edits
>         shown = apply_message_edits(messages, edits.all_drops, edits.all_adds)
>         # Stashed pre-strip: `shown` holds the buffer's own dicts by reference (the fold
>         # never copies), while the wire projection below copies every stamped message — so
>         # this list, not the returned one, is what stamp-back can mutate meaningfully.
>         self._pending_shown_messages = shown
>         return to_wire_messages(shown, keep=self.llm_client.consumes_internal_keys)
> --- `src/jaz/_agent.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         abbreviated_output, _ = abbreviate_string(
>             output,
>             max_length=self.max_repl_output_length,
>             prefix_ratio=self.truncation_prefix_ratio,
>         )
> --- `src/jaz/protocol/code_only.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-7 — Agent-requested history inspection. The loop appends the protocol's entry into the list; PythonREPL binds that list as `__history__`; the shipped prompt advertises indexing and its fields. Consumer: model-written REPL code. Status: afforded read, wired binding; advisory/evidential. Comparison inclusion: excluded for same-invoke history inspection; a later-invoke handoff must be independently established through RTE-8. No observed successful recall. History is available even when its observation rendering omitted content, but the default prompt does not explicitly explain the full-output escape hatch. SRC-1 `src/jaz/repl/python_repl.py:1427-1442`; SRC-2 `src/jaz/protocol/code_only.py:204-223`.

> `__history__` is a list with one entry per REPL iteration, in order (`__history__[0]` is your first
> iteration and `__history__[-1]` the most recent). Each entry has:
> - `.llm_response (str)`: Your full response for that iteration containing your code
> - `.repl_output (str)`: The printed output from that iteration, including any error traceback
> - `.repl_exception (BaseException | None)`: The exception object raised if that iteration hit
>   a recoverable error, else None
> --- `src/jaz/protocol/code_only.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-8 — Recursive object handoff and ambient scope supply. Producer: host or parent agent choosing explicit child inputs, or host `scope` block. Automatic selector: resolved in-scope binding map for each nested invocation, not relevance search. Delivery: description in prompt plus resolved payload in child REPL. Later consumer: child model/code. Status: wired binding propagation; it is memory push only when a later child receives previously accumulated or changed material. Explicit child arguments are deliberate caller delivery and can carry prior history; no such handoff is asserted to have occurred in a live run. Scope survives thread/task hops through bound data; values remain shared references. Same-name explicit and scoped inputs are rejected; nested scopes may shadow and restore bindings. No serialization guarantee crosses process boundaries. SRC-1 `src/jaz/invoke.py:312-352,405-416`, `src/jaz/scope.py:128-154`.

>     invoke_tool: InvokeTool = get_invoke_tool(
>         _invoke,
>         new_prehook,
>         # Snapshot of this level's scope, bound as data so it propagates to
>         # nested invokes across thread/task hops (see `parent_scope` above).
>         parent_scope=scoped,
> --- `src/jaz/invoke.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> - The snapshot copies the *mapping*; the values themselves are shared **by
>   reference**. Under sequential or asyncio execution that is benign (no two
>   invokes mutate concurrently). Under a ``ThreadPoolExecutor`` the scope is
>   visible *and* truly parallel, so two workers mutating the same scoped
>   ``list``/``CostTracker`` is a data race the caller must guard — bind immutable
>   values, or rebind a fresh instance inside each worker via a nested
>   ``jaz.scope(...)`` block (which is properly isolated per Task/context).
> --- `src/jaz/scope.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-9 — Console main-turn read-back. Trigger: every prompt turn after at least one recorded turn. Selector: the entire current main history. Delivery: `conversation_history` input, whose description renders a capped transcript while its live object binds in REPL. Consumer: next console main agent; optional agent indexing is pull, automatic transcript/object supply is coarse push. Records ordinary failures too. Status: wired delivery, afforded inspection. Human namespace access allows direct editing/rebinding, with no specialized memory editor or semantic acceptance gate. SRC-1 `src/jaz/console.py:330-408,479-512`.

>         if history.turns:
>             extra["conversation_history"] = history
>         try:
>             result = jaz.invoke(*hooks, task=task, **extra)
>         except BaseException as exc:
>             # Recorded, THEN re-raised: a failed turn is part of the conversation ("why
>             # did that error?"), and the exception object itself is the inspectable
>             # result. Ctrl-C included — an aborted turn is likewise worth remembering.
>             history.record(prompt, inputs, exc, target=_target, error=True)
>             raise
>         history.record(prompt, inputs, result, target=_target)
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>             "The conversation so far in this interactive session, oldest first. If the "
>             'user\'s request refers to earlier turns — "that result", "what you said '
>             'before", "the dataframe from turn 2" — examine this instead of guessing: '
>             "each element is a turn whose .prompt is what the user typed, .inputs maps "
>             "the interpolated expressions to the objects passed in, and .result is the "
>             "object returned (or the exception raised, when .error is true). These are "
>             f"the LIVE objects — inspect them directly, e.g. {name}[-1].result. The "
>             "reprs below are truncated; the objects are not.\n\n" + self.transcript()
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-10 — Console helper read-back. Trigger: `%` request. Selector: both current histories after type checks. Delivery: `main_conversation` and `helper_conversation` strings to helper invoke. Consumer: helper agent instructed to consult earlier exchanges. Status: wired coarse push. User confirmation controls whether new suggested code runs; retained applied status records that decision, not correctness. Failed helper calls without a reply record nothing. SRC-1 `src/jaz/console.py:1263-1279,1315-1319,1366-1371`; SRC-2 `src/jaz/console.py:1147-1165`.

>             main_conversation=main_conversation,
>             helper_conversation=helper_conversation,
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>             content, _ = abbreviate_string(exchange.content, _HISTORY_TEXT_CAP)
>             if exchange.kind == "answer":
>                 lines.append(f"    answer: {content}")
>             else:
>                 status = "confirmed and run" if exchange.applied else "shown, not run"
>                 lines.append(f"    proposed code ({status}): {content}")
>         return "\n".join(lines)
> --- `src/jaz/console.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-11 — TrajectoryReplay. Operator selects a single-root ATIF file. Loading builds per-invoke response queues from saved agent steps and nested children. InvokeEnter consumes the next child by order; LLMQuerySend consumes that node's next response and supplies it in place of a live answer. The current loop parses/executes the response, rebuilding state through rerunning code. Status: wired conditional on hook activation; coarse push to runtime, enforcement authority through response substitution. This is raw trace reuse, not a newly distilled lesson. Saved prompt tokens/cost are accounting, not evidence of current paid inference or improvement. SRC-1 `src/jaz/hooks/builtin/replay.py:410-418,509-602,858-875,943-1054`.

>         parent_node = self._invoke_stack[-1][0] if self._invoke_stack else None
>         child = parent_node.next_child() if parent_node is not None else None
>         self._invoke_stack.append((child, event.invoke_id))
>         return []
> --- `src/jaz/hooks/builtin/replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         return [
>             SupplyLLMResponse(
>                 content=r.content,
>                 prompt_tokens=r.prompt_tokens,
>                 completion_tokens=completion_tokens,
>                 cost_usd=r.cost,
>             )
>         ]
> --- `src/jaz/hooks/builtin/replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-12 — WorkflowReplay trace-to-program-to-execution. Trigger: hooked invoke/event stream. Producer records bound inputs/scope at InvokeEnter, response at LLMQueryExit, code at REPLExecEnter, completed execution at REPLExecExit; appends generated code immediately and finalizes at InvokeExit, including abnormal partial runs. A generated standalone call supplies the original inputs; a later operator can run the file/package or call its function. Write status: wired; later execution status: afforded. This supports per-task symbolic trace learning at afforded basis, with online production and later deliberate activation. No success-only selection, cross-task induction, repair loop, observed reuse or benefit is established. SRC-1 `src/jaz/hooks/builtin/workflow_replay.py:142-282,298-340,375-500,516-643`.

>                 repl_iteration = REPLIteration(
>                     iteration=i,
>                     code=ctx._pending_code or "",
>                     exec_result=result,
>                     llm_response=ctx._pending_llm_response,
>                 )
>                 ctx.repl_iterations.append(repl_iteration)
>                 ctx._pending_code = None
>                 ctx._pending_llm_response = None
> 
>                 # Write this iteration to file
>                 self._write_iteration_to_file(ctx, repl_iteration)
> --- `src/jaz/hooks/builtin/workflow_replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         # Generate function call with the original inputs
>         func_name = ctx.get_function_name()
>         if ctx.inputs:
>             # Format the inputs as arguments
>             args = []
>             for name, value in ctx.inputs.items():
>                 args.append(f"{name}={repr(value)}")
>             args_str = ", ".join(args)
>             lines.append(f"    result = {func_name}({args_str})")
>         else:
>             lines.append(f"    result = {func_name}()")
> 
>         lines.append("    print(result)")
> --- `src/jaz/hooks/builtin/workflow_replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-13 — Rollout export to an external trainer role. Producer: RolloutRecorder collects completed-query token stamps and freezes at invoke exit. Consumer role: training driver requests `to_flat`, `to_pieces` or `to_turn_samples`; these expose concrete conditioning/sample/loss-mask interfaces. Status: afforded pull to a documented external learner; recording/export wired, driver/parameter update/later model use excluded. Nonmonotone contexts reject flat export; alternate pieces and per-turn exports preserve differing contexts. It does not independently meet trace-learning requirements because this tree shows no durable learned behavior artifact from the external learner. SRC-1 `src/jaz/hooks/builtin/rollout.py:1-26,185-240,338-385`.

>     with RolloutRecorder() as rec, jaz.ConfigOverride(llm=sglang):
>         result = invoke(task="...")
>     rollout = rec.rollouts[0]
>     sample = rollout.to_flat()                      # flat ids + loss mask + logprobs
>     write_jsonl({**sample.to_dict(), "reward": judge(result)})   # reward is driver-side
> --- `src/jaz/hooks/builtin/rollout.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> Export offers three projections, strictest to most general: :meth:`Rollout.to_flat` (one
> flat masked sequence — raises :class:`~jaz.exceptions.NonMonotoneRolloutError` if the
> context was ever edited mid-run), :meth:`Rollout.to_pieces` (flat samples per monotone
> span), and :meth:`Rollout.to_turn_samples` (per-turn conditioning/sampled/logprobs
> triples — always resolves). For reasoning models under ``SGLangLLM``'s hidden-trace
> interface, multi-turn rollouts are non-monotone by design (each turn's trace is stripped
> from the next turn's context), so ``to_turn_samples()`` is the export to reach for — the
> quickstart's ``to_flat()`` fits single-turn runs and non-reasoning models.
> --- `src/jaz/hooks/builtin/rollout.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

### Claims

CLM-1 — Iterative Python/LLM agent construction and optimization: claimed in SRC-2 `README.md:3-7`; RTE-1 supports the execution mechanism. Optimization success needs evidence beyond iteration.

> Agents execute in a REPL loop where the LLM generates code, observes results, and iterates until the task is complete.
> --- `README.md` @ `0803d4971be785e95b80054b02259664d70fa3da`

CLM-2 — Capability containment is conditional on what the host exposes. The compiler documentation explicitly permits sub-invoke reconfiguration if the host supplies ConfigOverride; an immutable security boundary is not warranted. SRC-2 `src/jaz/repl/compiler.py:133-146`; implemented paths RTE-3, RTE-5.

> # opts into letting the agent reconfigure this sandbox for its sub-invokes.
> --- `src/jaz/repl/compiler.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

### Evidenced absences

No generic absence claim is asserted from an incomplete search. Missing deployment or activation evidence remains uninspected. 

ABS-1 — No shipped semantic memory curation/compaction policy established. Conclusion status: absent. At revision `0803d4971be785e95b80054b02259664d70fa3da`, the exact source search was `git --no-replace-objects -C related-systems/jaz-lang--jaz grep -n -E 'class .*([Cc]ompact|[Ss]ummar|[Mm]emory)|def .*([Cc]ompact|[Ss]ummar)|DropMessages\(' 0803d4971be785e95b80054b02259664d70fa3da -- src`. Its searched root was the full tracked `src` subtree. Results were `_summarize_doc` in `src/jaz/_catalog.py`, DropMessages dispatch in `src/jaz/hooks/dispatcher.py`, its effect definition in `src/jaz/hooks/effects.py`, memory-limit/error classes in `src/jaz/repl/_exec_guards.py`, and `summarize_exception` in `src/jaz/string_utils.py`. None supplies a concrete memory compactor. This search is combined with inspection of the inventoried writers and later-consumer routes; lexical absence alone is not proof of every possible implementation. ContextWindowWarning uses previous prompt token count to emit caller warning text. Persistent AddMessages/DropMessages can implement a host compactor, but the transformation and its later summary consumer are not shipped here. Raw acquisition, repr abbreviation and workflow lowering do not establish consolidate, dedup, evolve, synthesize, invalidate, decay or promote over retained memory. Boundary: frozen shipped src tree, excluding custom hooks and external harnesses. SRC-1 `src/jaz/hooks/builtin/context_window.py:119-154`, `src/jaz/_agent.py:366-401`.

>         ratio = self._context_ratio(event.invoke_id)
>         if ratio is None or ratio < self.warn_fraction or not self.warning_text:
>             return []
>         return [AddMessages([{"role": "user", "content": self.warning_text}])]
> --- `src/jaz/hooks/builtin/context_window.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

ABS-2 — No retained execution evidence for recall dependence. Conclusion status: absent. The complete enumeration command was `git --no-replace-objects -C related-systems/jaz-lang--jaz ls-tree -r --name-only 0803d4971be785e95b80054b02259664d70fa3da`. Root enumeration contained exactly `CHANGELOG.md`, `LICENSE`, `README.md`, `pyproject.toml` and `src`. The concrete retained-evidence path query `git --no-replace-objects -C related-systems/jaz-lang--jaz ls-tree -r --name-only 0803d4971be785e95b80054b02259664d70fa3da -- tests evals logs results benchmarks artifacts traces` returned no entries. The full listing contains implementation and comments but not the referenced eval/test traces; source-adjacent reported measurements are not inspected retained execution evidence. Replay divergence machinery checks consistency rather than empirically testing whether an agent used recalled content. No probe was run. Boundary prevents a faithfulness-tested yes and all observed or causal benefit claims. SRC-1 `src/jaz/hooks/builtin/replay.py:338-408`; SRC-2 `src/jaz/hooks/builtin/rollout.py:33-45`.

### Behavioral-authority paths

BAP-1 — Model and generated Python consume OBJ-1 through prompt descriptions and live variable/tool bindings. Instructions advise the model; callable bindings permit effects; scope controls descendant visibility. Horizon: invoke tree. RTE-1, SRC-1 `src/jaz/invoke.py:817-845`.

BAP-2 — Checks on RTE-2 and RTE-3 consume code/returns/query state at admission boundaries and enforce continuation, rejection or termination for the active invoke/tree according to hook scope. Epistemic authority extends only to the named type/predicate, never to all tool effects. SRC-1 `src/jaz/hooks/builtin/return_hooks.py:288-360`, `src/jaz/hooks/builtin/repl_code_hooks.py:108-146`.

BAP-3 — Human-confirmed OBJ-3 code executes in the console namespace, affecting the current session and subsequent calls; human approval grants operational authority and supplies no automatic epistemic warrant. RTE-4, SRC-1 `src/jaz/console.py:1412-1421`.

BAP-4 — Console later agents consume live records and text as advisory evidence over the session; replay substitutes responses and generated workflows execute code, granting operational force on explicit reuse. Exported rollout samples afford an external learning consumer without implemented training. RTE-9, RTE-10, RTE-11, RTE-12, RTE-13; their anchored canonical records establish each channel. Opaque retained objects on RTE-8 prevent a complete authority union.

## Runtime account

An application supplies the principal and task. JAZ assigns invocation/parent/depth identities, merges disjoint scope and explicit inputs into REPL bindings, renders their descriptions, requests model-generated code, and executes the committed code. A Continue result appends an observation and starts another turn. Return or Raise crosses completion hooks before reaching the caller. Recursive calls repeat this path with fresh local state and propagated scope. The enclosing application owns tool credentials, external state and ultimate use of the result.

Sync and async invoke are shipped alternatives; async uses the same input distinction and an async backend call. Supplied hook results can bypass model/REPL execution but still cross completion validation. Caller-defined tools can make independent calls or perform effects; library policies must not be described as constraints on every operation a callable can perform. A raw worker thread calling the public invoke entry can start a fresh root because its ContextVar did not propagate (SRC-1 `src/jaz/invoke.py:875-895`), unlike the captured recursive callable.

Three forcing cases were traced statically. First, an invalid return is converted to feedback or terminal failure, but this does not undo earlier tool actions (RTE-2). Second, a supplied invocation result still crosses InvokeComplete validation, so bypassing generation does not alone bypass return checks (SRC-1 `src/jaz/_agent.py:1062-1073`). Third, a settings proposal cannot use the % application path without human confirmation; after confirmation, its code runs as console code rather than under the proposal helper's restriction (RTE-4). Budget checks and host-exposed overrides define additional limits on enforcement (RTE-3, RTE-5).

> prehook = get_active_prehook() or Prehook(repl_depth=1)
> --- `src/jaz/invoke.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

> if span.supplied is not None:
>     span.complete(result=span.supplied)
>     break
> --- `src/jaz/_agent.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

There is no dynamic check planned. Mock execution of validators was considered, but static branches suffice for the bounded wiring conclusions; it would not establish model activation or sandbox security. Live agent tasks and hostile-code probes would require a separate execution boundary and add little to this descriptive pass. No package installation, credential access or model call was attempted.

Revision roles remain route-specific. Models propose code and responses; Python predicates or host validators reject them. Humans supply task policy, extensions and settings approval. No built-in answer oracle is established for arbitrary open requests. Memory-derived workflow reuse and its limits are recorded separately. These findings describe computational/human allocation without inferring an autonomy grade for the whole package.

## Lens scoping

### Memory/context scope

Full depth: SRC-1 history, console and replay implementation and SRC-2 reuse documentation trigger the lens. It covers OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, OBJ-10, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12, RTE-13. Ordinary transient REPL state and shipped static instructions are inventoried separately from accumulated material with a later consumer. Arbitrary payload opacity limits aggregate form conclusions.

### Epistemic scope

Full depth: CLM-1, OBJ-2, OBJ-3 and RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 plus the integrated trace-derived workflow route warrant inspection. The lens asks whether generation, validation, replay and configuration changes support content warrant or criticism-driven improvement. Provider internals, user validators' semantics and actual generated candidates remain uninspected.

## Lens outputs

### Memory/context lens

#### Accumulation and later consumers

JAZ has two distinct core context surfaces. The next model turn automatically receives the carried message buffer, whose REPL observations may be abbreviated. Agent-written code can instead index `__history__`, which retains the full response and full available nonterminal output plus the exception object. Neither is a cross-invoke durable store by default. Recursion starts a new agent and REPL; it passes explicit objects and propagates ambient scope, rather than copying a parent's conversation automatically.

The console adds a separate, shipped cross-invoke layer. Main turns receive both a rendered transcript and the actual earlier input/result objects. Helper turns receive only text transcripts. This distinction is load-bearing: classifying all console memory as text from its printed appearance would omit the objects the main agent actually reads. These objects can change through aliasing; this is a live reference history, not an immutable snapshot of prior values.

ATIF replay and workflow materialization are different routes. ATIF replay substitutes prior response text into the current loop, which executes it again. WorkflowReplay converts observed code into Python files with an entry point for later execution. Only the latter automatically produces a derived durable behavior-shaping artifact within this boundary. RolloutRecorder exposes training samples, but the training process and subsequent weight use are outside the tree.

Context volume is controlled mainly through rendering caps and optional warnings, not a shipped semantic compactor. The history and console objects can keep growing behind capped descriptions. No inference about better future performance follows from their retention.

#### Writes and retained rationale

RTE-6 and RTE-7 acquire raw local traces automatically; terminal turns lack ordinary output and record an empty output string. History contains recoverable exception objects but a terminal Raise's exception leaves through the result rather than becoming that field. Generic hooks can alter the message buffer and namespace. These are effect interfaces, not evidence of an installed memory policy. Raw Python objects handed to children or held by the console are kept by reference, so later mutation can alter what “past” inspection returns. Prompt descriptions may be authored separately from actual values and uniformly truncated; hidden descriptions can leave the underlying value bound. SRC-1 `src/jaz/protocol/prompts.py:48-102` and OBJ-5 establish why metadata cannot classify payload form.

RTE-9 records main successes and exceptions automatically after the invoke; RTE-10 records completed helper responses and adoption decisions. Their transcripts are deterministic displays generated for consumption, not durable semantic continuation summaries. They do not qualify as a separate trace-learning route. No session identifier is used to assert a learning horizon.

OBJ-8 writes once at hook teardown, including ordinary exception unwinds; abrupt process death before teardown can leave no ATIF file. Disk-bound recorder reuse is refused to avoid overwriting its own prior output, whereas pathless instances clear on setup and remain readable after exit. This lifecycle guard is not semantic invalidation or deduplication. The adjacent TrajectoryDirectoryRecorder streams human-readable files during execution, but its output is not what TrajectoryReplay reads. Existing directories can interleave old and new files. SRC-1 `src/jaz/hooks/builtin/atif_trace.py:190-200,675-714`, `src/jaz/hooks/builtin/trajectory_directory.py:358-377`.

RTE-12 is the qualifying derived behavior route. Its code records actions, preserves recoverable-error continuation by emitting try/except wrappers, and leaves terminal raises unwrapped. It neither checks that a workflow succeeded nor selects only validated actions. Rationale retention is partial: leaf bodies keep comments already present in code, but the purported “reasoning” writer only adds an iteration marker; it does not separately extract explanation from the saved response. The generated function intentionally has no task docstring. Parent workflows run through AST unparse, which discards comments. Python execution reads operational code, not comments as reasons; no later shipped route reads a retained explanatory rationale for diagnosis. SRC-1 `src/jaz/hooks/builtin/workflow_replay.py:309-340,364-373,423-435,633-643`.

>                 # Add LLM reasoning as comment if available
>                 if iteration.llm_response:
>                     # Extract reasoning from LLM response (simplified)
>                     # TODO: Parse reasoning more carefully
>                     f.write(f"    # Iteration {iteration.iteration}\n")
> --- `src/jaz/hooks/builtin/workflow_replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>         # No docstring: the invoke's prompt is not a distinct field (#538) and the `task`
>         # input — the only prompt-like candidate — is neither guaranteed to exist nor
>         # contractually a string suitable as a docstring, so we omit it rather than emit a
>         # misleading or malformed one. The materialized body is the REPL iterations below.
> --- `src/jaz/hooks/builtin/workflow_replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-13 transforms token records into training sample projections and leaves rewards outside the recorder. This is data preparation with a named external role, not an implementation of optimization or proof that improved parameters later returned to JAZ. No controlled curation vocabulary value is warranted merely because samples are split at context changes.

#### Selection and replay limits

Context inventory outside the comparison: RTE-6 supplies the carried buffer at each query. RTE-7 affords exact same-invoke history indexing through agent-written Python, where the consumer chooses which entry/field to inspect. Neither is memory read-back without a later-invocation handoff. No semantic retrieval index, embedding search or ranked memory store is needed or shown. The buffer grows with iterations; output rendering caps bound each observation rather than total retained history. ContextWindowWarning is optional and advisory, can only warn when usage/window data exist, and neither truncates history nor terminates the invoke itself.

RTE-8 automatically supplies ambient bindings throughout nested calls. Explicit child kwargs are independently chosen, and ordinary parent inputs do not automatically become child scope. The new invoke receives its own empty history. Host code can use object references to construct richer recursive memory, but the default does not infer a summary or migrate conversation context.

RTE-9 pushes the full console history container and a capped rendered index on every later main prompt. Reading earlier results by Python index is a separate pull operation, not evidence that the model exercised it. RTE-10 pushes only transcript strings to the helper, preventing live payload inspection through that input route. Its prompt requests prior-context consultation, but instruction is not observed use. Main and helper renders iterate through all accumulated turns; `_HISTORY_VALUE_CAP` and `_HISTORY_TEXT_CAP` cap individual display entries, while the protocol caps each final input display. Old objects remain pinned. The absence of a total history window is acknowledged in `src/jaz/console.py:287-298`.

RTE-11 serves queues by nesting/order and becomes a no-op after exhaustion or optional divergence. `detect_divergence` defaults false. When enabled, comparison covers recorded edits, committed assistant turns and abbreviated/normalized REPL observations, with backward trace gaps skipped; it does not compare the seed prompt. It does not authenticate a source trace or prove appropriateness for a changed task. The single stack assumes sequential nesting: concurrent sibling events can select the wrong queue. Modified responses may be transformed twice and diverge only after the changed first turn is committed. These are implementation/source-described limits, not newly reproduced failures. SRC-1 `src/jaz/hooks/builtin/replay.py:338-418,509-602,943-1054`.

>     Three limits worth knowing. A trace written before message edits were recorded is detected
>     and its edit comparison skipped entirely (the other two are unaffected). No comparison looks
>     at the *seed* prompt, so re-running a trace under a changed system prompt, task template, or
>     inputs rendering reports no divergence.
> --- `src/jaz/hooks/builtin/replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

>     # SEQUENTIAL INVOKES ASSUMED. ``_invoke_stack`` is one stack whose TOP is "the active
>     # invoke", which holds only while invokes nest strictly in time. ``ainvoke`` advertises
>     # concurrent execution via ``asyncio.gather``, and under it the top at any event need not be
>     # the invoke that raised it — so a query can be served from a sibling's queue and a
>     # difference in one invoke can latch another's ``diverged``. Pre-existing (mis-serving was
>     # already possible), tracked in #1310; the assistant-turn detector inherits it rather than
>     # introducing it.
> --- `src/jaz/hooks/builtin/replay.py` @ `0803d4971be785e95b80054b02259664d70fa3da`

RTE-12 has an actual generated later consumer, not merely a directory of code fragments: the `__main__` block invokes the generated function using recorded inputs. Activation remains an operator decision. Its guarantee is limited by repr reconstruction of arbitrary objects, runtime type-name annotations, inherited scope names absent from rewritten child call kwargs, and t-string sibling inputs absent from original call syntax. AST parse/unparse failure can leave invoke calls live; matching covers bare invoke and jaz.invoke forms, not all possible aliases. Child invocation order uses a mutable global counter; code replay does not establish an environment snapshot or safe arbitrary repeatability. Scope provenance is intentionally merged into function arguments. SRC-1 `src/jaz/hooks/builtin/workflow_replay.py:185-194,353-370,408-425,454-464,528-643`.

RTE-13's documented training driver is a valid afforded reader of exported samples, with selection and downstream training owned externally. Neither exports nor recorded logprobs establish the existence of learned parameters. Display-only directory/log/telemetry consumers are human debugging surfaces; no code route imports them as memory for later agent behavior within the inspected boundary.

#### Comparison boundary

Storage covers JAZ-owned Python references and files, not arbitrary services those references might point to. Representational form remains not-determinable because OBJ-5 and OBJ-6 carry arbitrary live payloads alongside classified text/code/token structures. Lineage is likewise not-determinable for a complete set: record construction is trace-extracted, but arbitrary host objects and returned values do not expose a uniform origin. These are justified unknowns, not skipped inspection.

Behavioral authority remains not-determinable for the full declared scope. Concrete console histories supply advisory evidence, replay/workflow code determines execution, and exported training data affords consumption by an external learner. Those route findings remain intact, but OBJ-5 and RTE-8 admit arbitrary retained objects, including instruction or tool objects whose authority at a later consumer cannot be inferred from their display or binding. Instructional scaffolding describing history is static and excluded. Write agency likewise remains not-determinable for the full scope: the concrete recorders write automatically and host/file surfaces admit manual editing, but the source does not establish who produced or changed opaque retained payloads. These unknowns preserve the original boundary rather than removing its unconstrained branch. Curation remains absent within the shipped policy boundary: general Python mutability does not implement a named maintenance operation.

Direction includes cross-invocation automatic supply and requested inspection/execution/export. Same-invoke buffer supply and same-invoke history indexing are excluded. Coarse push is the supported signal: accumulated scope material handed to another invoke, console session history and ordinal replay queues select retained parts. An invoke UUID on a stack frame is not a content identity match against saved invocation IDs. No identifier-based push or inferred selector is established.

Trace learning yes refers only to RTE-12: event stream to durable executable prescription to afforded execution. Its supported horizon is replay of a recorded task; a callable signature alone is not evidence of cross-task adaptation. Writes happen during execution, so timing is online even though activation comes later. Distilled form is symbolic. Raw traces, in-session histories, deterministic capped displays and externally trainable samples do not add an independent qualifying route. Faithfulness tested no is bounded by the absence of retained recall-dependence evidence; source claims about other experiments remain claims.

### Epistemic lens

#### 1. Source-and-claim boundary

SRC-1 and SRC-2 govern this overlay; see the canonical register. Assessed families: generated code/results, return/code checks, settings changes and memory/replay reuse. Excluded host validators/tools and unobserved model content prevent a system-complete knowledge-production claim. CLM-1 states iterative optimization; no framework-supplied universal truth oracle is inferred.

#### 2. Epistemic-object inventory

OBJ-1 imports caller content with caller-dependent warrant. OBJ-2 may contain factual answers or procedural conjectures; candidate transformation is indeterminate without an instance. OBJ-3 combines a factual configuration view with proposed code or explanatory text, whose correctness is not established by its tag. Memory objects preserve the lineage and consumer recorded on their canonical entries; trace replay is not itself evidence that the recorded procedure is correct.

#### 3. Authority-route ledger

| route/function | architectural status | object/update | evaluator, timing and result | epistemic authority | operational authority and horizon | limit |
| --- | --- | --- | --- | --- | --- | --- |
| RTE-1 content transformation | implemented | OBJ-2; indeterminate transformation from inputs/observations | Model generates code each turn | None supplied by generation alone | Python execution and recursive calls via BAP-1 | No candidate instance observed |
| RTE-2 check/evidence production | implemented | OBJ-2; no content change | Type or caller predicate at Return; pass or exception | Declared type/predicate domain only | Enables subsequent disposition | Predicate may not concern truth |
| RTE-2 disposition/acceptance | implemented | OBJ-2; no content change | Hook converts invalid return to Continue/Raise, or allows completion | Same bounded predicate | BAP-2, current invocation | Returned acceptance does not certify prior effects |
| RTE-3 operational admission | implemented | OBJ-2; no content change | Compiler, code validator and budget checks at their respective boundaries | Syntax/policy/accounting domain | Execute, retry or abort via BAP-2 | Host tool and alternate backend contract |
| RTE-4 content transformation | implemented | OBJ-3; indeterminate answer or non-truth-apt settings proposal | Model helper responds to request | Proposal only | No application before confirmation | No instance observed |
| RTE-4 operational admission | implemented | OBJ-3; no content change | Human y/yes at TTY | Permission, not factual acceptance | BAP-3; later session behavior | No automatic rollback or benefit test |
| RTE-5 operational admission | implemented | OBJ-1; non-truth-apt capability replacement | Caller chooses object and replacement permission | None beyond name/update checks | Later bound callers or delegates | Application retention and tests uninspected |

The memory lens's replay and later-consumer records supply retention and operational-use functions; none is silently relabelled post-acceptance lifecycle integration.

#### 4. Per-object lifecycle disposition

OBJ-1: acquisition/import of supplied truth-apt portions; discovery lifecycle not applicable to transport. Source warrant unknown because the caller is outside the boundary. OBJ-2: transformation indeterminate; non-ampliative reshaping, entailed computation and ampliative conjecture remain possible. Generation, checks and return are implemented, but every observed candidate phase is no instance observed. Predicate acceptance cannot settle the transformation class. OBJ-3: explanations are indeterminate truth-apt candidates; settings snippets are policy changes. Human permission does not constitute a truth test. No instance observed in either branch. For retained raw trace/history objects, acquisition and delivery are non-ampliative at the transport level; opaque or transformed payload meaning remains bounded by the memory records. Generated reusable code is a transformation whose replay fidelity is not proven by source extraction. No claimed accepted ampliative lifecycle is established.

#### 5. System-claim versus route comparison

CLM-1 has design support and implemented generation/iteration in RTE-1, with optional checks RTE-2 and RTE-3. No observed-run or causal evidence establishes optimization benefit. CLM-2 is consistent with the configurable enforcement boundary: implementation supports restricted code paths, but host capability exposure prevents a universal claim. Memory export/reuse claims remain at their route-specific wired/afforded levels.

#### 6. Bounded conclusion

The package can retain and reuse conversation or execution material and enforce caller-defined checks. It supplies mechanisms for correction, not a universal epistemic acceptance process. Under the [theory-builder definition](../../../../notes/definitions/theory-builder.md), conditions 1–4 are separately assessed: localized theories afforded through explicit input/code units; content-driven consumption afforded for model-readable theories and wired for executable code; content-directed criticism afforded by custom validators and feedback, but uninspected as a formulated theory criticism in actual operation; iteration of criticism results afforded, with wired next-turn error delivery but no observed criticism-to-revised-theory chain. Overall theory-builder membership remains uninspected, not absent.

Addressability is afforded at the level of named inputs, functions and code fragments; assumptions and rationales inside arbitrary content are uninspected. Persistence ranges from a single invoke to a console session and explicit exported artifacts; it must be tied to the particular route. Learning—improved future capacity attributable to criticism—is uninspected. [Reflection](../../../../notes/definitions/reflective-system.md) is afforded over program-visible execution history and wired over the human-mediated console configuration view/change path; no reflective theory-builder qualifier is established. Autonomy of a theory builder is uninspected; RTE-4 explicitly retains human selection. A standing caller-programmable improvement path is afforded, but [self-improvement](../../../../notes/definitions/self-improving-system.md) as exercised evidence-responsive organizational change is uninspected. Workflow extraction alone is no substitute for that evidence.

## Reconciliation

Proposal mapping: MEM-OBJ-1 → OBJ-4; MEM-OBJ-2 → OBJ-5; MEM-OBJ-3 → OBJ-6; MEM-OBJ-4 → OBJ-7; MEM-OBJ-5 → OBJ-8; MEM-OBJ-6 → OBJ-9; MEM-OBJ-7 → OBJ-10; MEM-RTE-1 → RTE-6; MEM-RTE-2 → RTE-7; MEM-RTE-3 → RTE-8; MEM-RTE-4 → RTE-9; MEM-RTE-5 → RTE-10; MEM-RTE-6 → RTE-11; MEM-RTE-7 → RTE-12; MEM-RTE-8 → RTE-13; MEM-ABS-1 → ABS-1; MEM-ABS-2 → ABS-2.

- Register proposed object records OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9 and OBJ-10, route records RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12 and RTE-13, and absence records ABS-1 and ABS-2. Parent source IDs SRC-1 and SRC-2 are reused without redefinition. Canonical namespaces and authority paths remain the parent's responsibility.
- Include console main/helper histories in the integrated memory boundary. Omitting them would incorrectly imply all useful state ends at invoke exit. Retain the opaque live-payload limitation; the transcript is only a display projection. This affects representational form and lineage.
- Retain RTE-12 as an afforded symbolic trace-learning route, with wired extraction and an actual generated executable consumer. If the parent chooses a narrower learning interpretation, preserve this evidence and disagreement explicitly rather than silently replacing yes with no. Its rationale retention is partial and there is no shipped rationale-reading consumer.
- Preserve rollout export as an afforded external trainer interface, distinct from implemented training. No parameter-update route or observed learned benefit can be imported from source comments about excluded harnesses.
- Preserve replay's ordinal selection and sequential-stack limitation. Do not label its per-invoke bookkeeping as identity-targeted push, general state restoration, or seed-prompt equivalence checking.
- Preserve workflow implementation limits: arbitrary repr/type reconstruction, scope/t-string parameters absent from rewritten calls, no success filter, partial failed workflows, comment loss through AST unparse, silent rewrite fallback and ordered child counter. These limit portability and faithfulness; they do not erase the implemented extraction route.
- Generic persistent message edits afford host compaction but provide no shipped summarizer. Do not classify summary learning or curation from method names/comments alone. Context warnings are not compaction.
- Parent integration correction adopted: ordinary per-invoke buffer/history use stays in the context inventory but is excluded from all comparison references. Scope/history handoff contributes only for accumulated or changed material reaching a later invoke. This corrects the earlier profile boundary without changing proposal identities. Both absence records now state conclusion status and exact frozen-tree search commands.
- Parent integration correction adopted: behavioral_authority and write_agency now use not-determinable for the unchanged full scope because OBJ-5 and RTE-8 do not constrain arbitrary retained payload authority or producer. Concrete console/replay/workflow/export authority and agency findings remain on their records; they are not a complete aggregate for that opaque branch.
- No supplied source fact required correction. No blocking identity/access/scope issue remains. Model identity is unknown because this specialist runtime exposes a family-level Codex description without a concrete model ID.

The coordinator owns RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 and OBJ-1, OBJ-2, OBJ-3. Memory records augment rather than replace them. The epistemic overlay uses the same canonical records and keeps permission/type acceptance separate from truth warrant. No independent convergence is claimed where both passes relied on the same mechanism. No unresolved substantive conflict remains.

## Bounded synthesis

JAZ makes model-generated execution resemble a recursive function call. Inputs remain Python values; scope passes bindings down the call tree, and hooks can intervene before execution or final return. Its useful distinction is between the small invoke loop and the host-configured controls, persistence and user interface around it. Default compiler/file/import checks do not settle what arbitrary host tools can do, and public calls in raw threads can escape a captured invocation's context by starting a new root.

The strongest retained-work contribution is explicit later reuse: console turns can carry accumulated context, replay can recover recorded execution paths, and workflow export can produce runnable code. These routes support memory or trace-derived reuse at their recorded evidence levels. They do not demonstrate successful criticism, faithfulness of rewritten workflows or improved future capacity. Conditional validators can enforce a precise caller predicate; application-level truth and effect safety still require that predicate and an appropriate execution envelope.

Three concrete changes to the evidence would alter this assessment: a candidate-linked trace connecting a stated theory to criticism and a later revision; a controlled comparison showing improved later capacity; or adversarial tests covering the actual configured tool and execution boundary. A host with durable storage, strong oracles or external isolation would be a larger system than the package analysed here.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | resolving evidence |
| --- | --- | --- | --- | --- |
| Static inspection only | SRC-1, RTE-1, RTE-2, RTE-3, RTE-4 | Pinned shipped implementation | Activation, reliability, successful learning or causality | Candidate-linked runs and interventions |
| Caller extensions excluded | OBJ-1, RTE-5 | Built-in host interfaces | Universal side-effect, rollback or oracle guarantee | Concrete tool implementations and deployment contract |
| Provider internals opaque | CMP-3 | Inference request wrapper | Exact weights, provider training/fixity | Provider artifact identity and training evidence |
| Arbitrary retained payloads | OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, OBJ-10, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12, RTE-13 | Memory objects and known consumers | Complete aggregate semantic/form attribution | Concrete payload instances |
| No benchmark evidence in this source allowlist | CLM-1 | Framework only | Paper-result reproduction or comparison validity | Separate evaluation analysis and frozen run evidence |

## Verification and blockers

### Semantic verification

Checked route ownership, sources and quotes, statuses, forcing branches, host/dependency exclusions and separate permission/epistemic authority. Memory profile scope, known unions, trace-fed writes, later consumers and push selectors were reconciled against OBJ-4, OBJ-5, OBJ-6, OBJ-7, OBJ-8, OBJ-9, OBJ-10, RTE-6, RTE-7, RTE-8, RTE-9, RTE-10, RTE-11, RTE-12, RTE-13; any opaque alternatives retain uncertainty. Per-route trace-learning classifications are not promoted to the separate learning claim. No source claim is upgraded to observation or causality. Theory-builder conditions and persistence are not inferred from neighbouring fields.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-jaz-01/result.md`, using `commonplace-validate --full`. Full validation passed with no warnings or failures.

### Blockers

none
