---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "JAZ's model-to-Python loop, recursive work, hook controls and change admission at its frozen distribution revision."
run-id: AAS-2026-10-15-jaz-a94bea79c61a-01
reviewed-boundary: 0803d4971be785e95b80054b02259664d70fa3da
---

# JAZ runtime report

## Runtime account

### Work and entry paths

JAZ encloses a model-directed Python computation. A caller supplies named instructions, data and callable capabilities; the model emits Python, sees execution observations, and eventually returns a Python object or raises. This is not merely a tool-call adapter. The source-native claim and implementation route are [RT-CLM-repl-work](#rt-clm-repl-work) and [RT-RTE-agent-loop](#rt-rte-agent-loop). All source evidence here is SRC-1 at the boundary revision. No target execution, test, example, provider request or experiment was performed. Implementation wiring is inspectable; exercised operation, activation and benefit are unobserved.

The library exports `invoke` and `ainvoke`. The installed `jaz` command and `python -m jaz` enter the shipped console. Its `main` parses arguments, gates interpreter compatibility, loads console settings, applies flags, builds a namespace and enters session hooks. It dispatches `-c`, files, non-TTY stdin and interactive input separately. These are different input drivers, not different model-loop owners. Console sigils translate prompts into chat calls; ordinary Python entered at the console is host code, not automatically sandboxed agent code. SRC-1, `src/jaz/__init__.py`, `src/jaz/invoke.py`, `src/jaz/console.py`, and the entry-point evidence in [boundary](boundary.md#boundary-and-evidence).

The default components are LiteLLM, PythonREPL and CodeOnlyProtocol; the default LLM has no model selected, so a caller or console setup must supply one. Config holds replaceable component objects, not a hardwired deployment. Provider/model identity and mutability are recorded in [RT-CMP-model-backend](#rt-cmp-model-backend). SRC-1, `src/jaz/config.py`:

> return {
>     "llm": LiteLLM(),
>     "repl": PythonREPL(),
>     "protocol": CodeOnlyProtocol(),
> }
> --- `src/jaz/config.py`

### Ordinary invocation, coordination and recovery

For an ordinary synchronous `invoke(task=..., data=..., tool=...)`, input names are part of the API: `task` is an ordinary named input, not a distinguished control field. Setup resolves the propagating configuration stack at absolute recursion depth, resolves ambient scope separately from explicit inputs, rejects conflicting names, allocates an invocation UUID and parent identity, constructs a recursive callable, and instantiates Agent. Local hooks attach only to this Agent. SRC-1, `src/jaz/invoke.py`.

Agent resolves input wrappers through `__jaz_get__`, seeds an invocation-local hook blackboard, and enters InvokeEnter/Send. Hook input additions and drops affect both prompt rendering and REPL binding before Send. Without a supplied terminal result, Agent initializes fresh REPL state, a session ID and an empty history list, then renders opening messages. Instructions and descriptions reach the model as natural language; live Python input objects reach the executor independently of their rendered descriptions. The next-step owner is the model for code choice and the Agent loop for scheduling. See [RT-OBJ-message-buffer](#rt-obj-message-buffer), [RT-OBJ-repl-state](#rt-obj-repl-state) and [RT-RTE-agent-loop](#rt-rte-agent-loop). SRC-1, `src/jaz/_agent.py`.

Each turn enters LLMQuery, folds hook message edits, projects internal sidecar keys away according to the backend contract, and sends the committed message list. A supplier can replace the provider response. Otherwise the configured client calls the model with retry logic. CodeOnlyProtocol treats the response as code, without extracting a fenced region. REPLExec enters, commits namespace drops/additions and code edits, exposes the committed code at Send, and either consumes a supplied result or executes that same code. The finalized result supplies the history entry. Continue appends a rendered observation; Return or Raise completes the invoke. InvokeComplete may still transform the terminal result before the public caller receives the value or exception. SRC-1, `src/jaz/_agent.py`, `src/jaz/protocol/code_only.py`:

> return ParsedCode((llm_response.content or "").strip("\n\r"), None)
> --- `src/jaz/protocol/code_only.py`

PythonREPL compiles and transforms top-level return/raise, executes against the run's namespace, captures print output, and distinguishes native finishing from incidental errors. Ordinary syntax/runtime failures become recoverable Continue observations. Fatal signals and foreign enclosing resource breaches propagate; exhausted model retries also propagate rather than masquerading as successful terminal results. The loop has no inherent iteration cap. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/_agent.py`, `src/jaz/llm/llm.py`. The inspected retry implementation uses per-exception-category counters, exponential waiting and a total-attempt backstop; retries are transport recovery, not candidate evaluation.

Recursion is a fresh agent context, not a copy of the entire parent transcript: selected explicit inputs plus inherited ambient scope enter a new REPL and opener. Parent/child UUID and iteration provide correlation. The parent receives a native return object or exception; objects can remain shared by reference, so fresh messages do not imply process or object isolation. The recursive facade captures configuration, scope and hook context for rebasing across thread hops. The async public path awaits model calls and `aexec`, permits top-level await, and shares message-edit, parsing and finalization helpers. The automatically bound recursive primitive inspected here is synchronous; async APIs can be supplied separately by the host. [RT-RTE-recursive-work](#rt-rte-recursive-work) records the controls and their thread-context limit. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/repl/python_repl.py`.

### Four forcing cases and scoped guarantees

1. **An alternate executor/result producer.** Async execution uses the same committed-input seams, but hook suppliers can skip a model query, Python execution, or the whole invocation. A claim that every result was generated by a model and executed locally is false. Return validation has an InvokeComplete backstop covering supplied terminal results. This is [RT-RTE-hook-control](#rt-rte-hook-control); replay is a concrete supplier in [RT-RTE-trajectory-replay](#rt-rte-trajectory-replay).
2. **An indirect effect channel.** REPL import and file restrictions do not constrain an arbitrary host callback's internals. The shipped SWE library calls `subprocess.run(..., shell=True)` and real file I/O. If granted as an input, it extends the effective capability boundary beyond secure `open`. [RT-RTE-host-tools](#rt-rte-host-tools) is not evidence that this library is granted by default.
3. **A thread-mediated recursive call.** RecursionLimit removes the tool at the cap and aborts observed over-cap InvokeEnter events, including ordinary indirect host calls. Its own documented wrapper-plus-thread case can undercount ancestry. A universal depth invariant across arbitrary threads is therefore unwarranted; source inspection establishes the limitation, not a reproduced exploit. See [RT-RTE-recursive-work](#rt-rte-recursive-work).
4. **A request to change the running system.** The console `%` helper receives text snapshots and pinned restrictions, proposes an answer or code, and runs proposed code unsandboxed only after interactive human confirmation. That gate does not cover the user's ordinary Python, already granted host tools or all library callers. [RT-RTE-settings-change](#rt-rte-settings-change) records this narrower admission boundary.

The following guarantees distinguish policy from invariance and deployment isolation. Their operation conclusion status is **uninspected** throughout because no execution evidence is supplied.

| Guarantee and owner | Enforcement point and strength | Covered paths, challenges and external contract | Implementation conclusion status |
|---|---|---|---|
| Committed REPL source is the source exposed to Send validators; Agent/dispatcher | `span.committed_code` passed to PythonREPL after Send; invariant of this core branch | Sync and async live-exec paths; suppliers intentionally bypass execution. A custom REPL or hook remains trusted host code. See [RT-RTE-hook-control](#rt-rte-hook-control). | wired |
| Agent-source import/attribute restrictions and wrapped builtins; PythonREPL/compiler | AST policies plus policy-bound runtime builtins; policy, not a process sandbox | PythonREPL code under its configured lists. Host callbacks, imported modules' internal operations and replacement REPLs require their own contract. Capability injection can widen permissions. See [RT-RTE-host-tools](#rt-rte-host-tools). | wired |
| Optional recursion cap; RecursionLimit | DisableRecursion at cap, Abort above cap; policy | Same-context and correctly rebased calls, subject to ancestry metadata. Wrapper/thread gap prevents universal coverage. No cap without installation. | wired |
| Optional iteration/cost/call governance; hooks | IterationLimit and BudgetPool check LLMQueryEnter; BudgetPool books completed-query cost at Exit; policy | Core query seams, including supplied responses. Cost depends on backend/post-transform accounting; one completed call can cross a monetary threshold and concurrent calls are not a reservation-based hard cap. Raw model calls inside host functions are outside this seam. | wired |
| Optional return type; ReturnType | REPLExecComplete feedback and InvokeComplete terminal backstop; policy | Live and supplied terminal Return values; type validity is not task correctness. See [RT-RTE-hook-control](#rt-rte-hook-control). | wired |
| Per-exec timeout/RSS control; PythonREPL | Execution guards; best effort | Timeout pragma can raise the configured timeout unless disabled. Guard design names worker blocking-C and thread-pool gaps; RSS sampling is a growth guard, not a hard allocation ceiling. OS/process isolation is not established. | afforded |
| Human admission of `%` snippets; console | TTY check and explicit yes before host `exec`; protocol | Helper code-response branch only; denial leaves proposal unapplied. Confirmed code is intentionally unsandboxed. See [RT-RTE-settings-change](#rt-rte-settings-change). | wired |

Evidence for the resource qualification is SRC-1, `src/jaz/repl/python_repl.py` and the inspected design header in `src/jaz/repl/_exec_guards.py`; guard internals were not exhaustively audited:

> allow_timeout_pragma: If True (default), a leading ``# timeout: <seconds>`` comment
> in the code sets that execution's wall-clock bound, overriding ``exec_timeout``
> with no ceiling. Set False to make ``exec_timeout`` a bound the agent cannot
> raise; the comment is then ordinary text and is not described in the prompt.
> --- `src/jaz/repl/python_repl.py`

Hook governance is not fail-closed against arbitrary hook bugs. Dispatcher catches ordinary exceptions from governance hooks as well as observers, logs and continues. Abort effects are the supported termination channel. This defeats the stronger claim that attaching a validator alone guarantees its policy survives validator failure. SRC-1, `src/jaz/hooks/dispatcher.py`:

> except Exception as e:
>     # A plain Exception from a hook is a non-fatal bug: log + continue, so one
>     # buggy hook (observer, tracer, user control hook, or even a governance
>     # hook) can't abort the run.
> --- `src/jaz/hooks/dispatcher.py`

The **capability surface** is arbitrary supplied Python values/callables, optional imports and recursion, plus trusted replacement components/hooks. The **default grant** inspected is deny-all imports and file paths with a secure attribute policy, not an automatic SWE shell. The **deployed isolation envelope** is unresolved: the supplied evidence contains no deployment manifest or run showing an OS sandbox. Python executes in process, and host callback code is not recursively rewritten by the agent compiler. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/repl/permissions.py`, `src/jaz/repl/compiler.py`, `src/jaz/_library/swe.py`.

### Persistence and additional coverage

The console's chat wrapper retains prior session turns and passes them as a `conversation_history` input to subsequent invocations; helper exchanges are separately represented. Session model selection can persist backend/model settings, which console startup reloads. ATIF recording and replay admit retained execution responses as future code-producing inputs. Replay maps queues through one shared active-frame stack, not query-event invoke-ID lookup: per-invoke correspondence requires strictly sequential nesting. Concurrent invocations can receive another frame's saved code or divergence latch; replay's existence does not establish per-invoke isolation on that path. WorkflowReplay emits Python programs from execution events; it does not automatically install those programs as JAZ's next policy. [RT-RTE-trajectory-replay](#rt-rte-trajectory-replay), [RT-RTE-settings-change](#rt-rte-settings-change) and [RT-RTE-workflow-emission](#rt-rte-workflow-emission) establish the runtime admission seams; detailed memory revisions belong to the memory analyst. SRC-1, `src/jaz/console.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`; recording identity is established in [boundary](boundary.md#boundary-and-evidence).

Additional implementation inspection beyond the boundary's initial ranges covered setup and core sync/async turns; query projection and persistent message edits; recursive facade construction; PythonREPL construction/execution; compiler policy comments and builtins assembly; dispatcher event emission; ReturnType completion checks; BudgetPool query entry/exit; replay response selection; workflow event capture/emission; console helper proposal/confirmation, startup and settings writer; default component construction; LiteLLM calls/normalization; shared retry selection; and Copilot session creation. These are SRC-1 implementation passages at the paths cited above and `src/jaz/llm/copilot.py`, not additional sources or run evidence. The system template, execution-guard header and inline limitation accounts supply doctrine/design as labelled.

Provider-native tools are not equivalent to local REPL execution merely because a backend returns a response. Copilot's inspected session creation explicitly sets `available_tools=[]` and replaces its system message. LiteLLM forwards to its dependency; OpenAI/Anthropic adapters and SGLang/provider internals were not exhaustively traced here. Direct dependency calls through granted host code remain outside core governance. No universal exclusion of provider-side tools, no all-adapter parity guarantee, and no remote-worker or durable-checkpoint semantics are inferred from this selected forcing set. SRC-1, `src/jaz/llm/copilot.py`, `src/jaz/llm/_litellm.py`. Missing traces prevent operational and performance conclusions, not the architectural findings above.

## Shared records

### Components

#### RT-CMP-model-backend
Label: Configured model backend

The operative numerical component is the externally resolved model behind Config.llm, ordinarily LiteLLM. Distributed-parametric form; weights/storage and provider processing are external and uninspected. JAZ stores a symbolic model name and request settings in Python component objects; it does not pin model weights or a provider revision. A mutable endpoint/name may resolve to another model. Parameter change during operation is uninspected inside providers; the inspected JAZ query route requests completions rather than parameter updates. Model configuration itself can change via [RT-RTE-settings-change](#rt-rte-settings-change). No claim of fixed provider weights or absence of learning follows. SRC-1, `src/jaz/config.py`, `src/jaz/llm/_litellm.py`, `src/jaz/llm/llm.py`.

> response = litellm.completion(**params)
> --- `src/jaz/llm/_litellm.py`

### Operative objects

#### RT-OBJ-message-buffer
Label: Invocation messages

Natural-language instructions, input descriptions and observations are stored in a run-local Python list of message dictionaries and consumed through model interpretation. Python code in assistant turns has a distinct symbolic execution consumer after parsing; it is not made executable by merely being prompt text. Agent stamps provenance sidecars and applies hook edits before provider projection. The persistent subset changes the carried-forward buffer; transient edits affect only that query. This is not evidence of a built-in summarizing model. SRC-1, `src/jaz/_agent.py`:

> shown = apply_message_edits(messages, edits.all_drops, edits.all_adds)
> --- `src/jaz/_agent.py`

> messages[:] = apply_message_edits(
>     messages, edits.persistent_drops, edits.persistent_adds
> )
> --- `src/jaz/_agent.py`

#### RT-OBJ-repl-state
Label: REPLState and history

The source-native REPLState contains the live Python namespace; its substrate is in-process objects, not a serialized checkpoint. The symbolic operative part comprises variable bindings, compiled code and native return/exception values. `__history__` exposes a protocol-produced list containing response text. Continue entries retain full REPL output and any recoverable exception object; terminal Return/Raise entries instead record empty output and no exception in that field. This history does not uniformly preserve terminal stdout, returned values or terminal exceptions for reconstruction. Its text payloads can be model-readable when printed. They are not interchangeable with the abbreviated observation messages. This record identifies the working container, not an independently curated memory store. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`.

> # The configured REPL is a stateless template; `initialize` returns this run's
> # `REPLState` (#1058), threaded into every exec below.
> --- `src/jaz/_agent.py`

### Routes

#### RT-RTE-agent-loop
Label: Agent query and execution loop

Caller inputs → setup → opening messages and REPLState → repeated query/parse/exec → terminal object or exception. Agent owns progression; the model chooses Python under the rendered task/instructions and available observations. This is an open-request operating mode, not a bounded curriculum. There is no expected-answer oracle on the ordinary path; execution feedback reports what code did, not whether the task answer is true. Caller-supplied validation can add a separate decision gate. SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/protocol/code_only.py`, `src/jaz/repl/python_repl.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Native Python return value, or propagated terminal exception; Continue is internal loop feedback.
- Later read-back: inapplicable — the bare core route does not automatically rehydrate a prior invocation; console history and replay are separate consumers.
- Delegated visibility: New child calls receive selected arguments and ambient scope, not automatic parent transcript copying; see [RT-RTE-recursive-work](#rt-rte-recursive-work).
- Selection predicate: Model-generated code from the final query response; CodeOnlyProtocol takes content as code after stripping terminal newline characters.
- Invalidation or expiry: Run-local context ends on Return/Raise or abort/failure; escaped references can outlive the call. No serialized restart is established.
- Activation or effect: Wired model-to-code execution and observation feedback; actual behavior change and task success are unobserved.
- Evidence limits: Static implementation only; backend behavior, arbitrary tools and caller validators remain external to this ordinary trace.

> case Return():
>     return final_result.return_value
> case Raise():
>     raise final_result.exception
> --- `src/jaz/_agent.py:1117-1120`

#### RT-RTE-recursive-work
Label: Recursive invocation and context rebasing

Model-authored code calls the bound `invoke` closure; it delegates through `_invoke` to a new Agent with fresh message/namespace state. Host code can also invoke indirectly. Scope/configuration/hook snapshots and live context determine ancestry; local hooks do not automatically propagate. The model proposes the subtask/inputs; setup determines binding and active hooks can veto admission. No per-child human approval or expected-answer oracle is built into this route. Open-request subcomputations inherit caller-selected governance. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/invoke.py`, `src/jaz/hooks/builtin/recursion_limit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Child result or exception returns to the calling Python computation.
- Later read-back: inapplicable — fresh child frames are ordinary current-run contexts; any retained history explicitly passed across later invocations is a separate route.
- Delegated visibility: Explicit kwargs and inherited ambient scope; references can expose host capabilities. Ancestor configuration/hook context is rebased on raw workers, but local invocation hooks stay local.
- Selection predicate: Parent model chooses calls and arguments; RecursionLimit, when installed through a propagating context, removes the primitive at its cap and aborts greater reported depth.
- Invalidation or expiry: Child message context is no longer advanced on completion; only values/references returned or externally retained remain reachable. Timeout/abort is not rollback of effects.
- Activation or effect: Wired separate model contexts and native-result coordination. Context isolation limits routine transcript exposure but is not object/process isolation.
- Evidence limits: Wrapper passed down and executed across a non-inheriting thread can use binding ancestry instead of calling ancestry; universal recursion enforcement is not supported.

> if event.depth == self.max_depth:
>     return [DisableRecursion()]
> --- `src/jaz/hooks/builtin/recursion_limit.py`

> the wrapper's ``jaz.invoke`` call runs on a thread that did not inherit the calling invoke's context —
> either because the caller ran the wrapper on a thread it spawned (a ``ThreadPoolExecutor`` worker,
> say), or because the wrapper spawns one itself and invokes inside it. The invoke is then counted at
> the *binding* invoke's depth instead of the caller's, so a stack deeper than ``max_depth`` can be
> built that way.
> --- `src/jaz/hooks/builtin/recursion_limit.py`

#### RT-RTE-hook-control
Label: Hook effects and result admission

Active host-installed hooks consume typed events; dispatcher composes effects that alter inputs, messages, variables, code, responses and results, or abort. It stamps live hook membership, timestamps and a per-invoke blackboard; writes become visible after the event's readers finish. Hooks are trusted Python, not sandboxed extensions. Computational proposal/decision/veto roles lie in hook handlers and composition, with human contribution determined by who supplied the hook, not necessarily a human approval for each output. ReturnType checks native types; ValidateReturn can supply caller-defined validation, not an intrinsic expected-answer oracle. Operating mode is caller-defined open work or validation; no universal improvement trigger. SRC-1, `src/jaz/hooks/dispatcher.py`, `src/jaz/_agent.py`, `src/jaz/hooks/builtin/return_hooks.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Composed response/exec/invoke result or Abort exception; observers see final outcome events.
- Later read-back: Persistent message edits remain in the loop buffer; durable write/read policies are hook-specific, not guaranteed by the effect mechanism.
- Delegated visibility: Propagating hooks reach nested invocations; local hooks only the current dispatcher. Blackboard state belongs to this invoke.
- Selection predicate: Typed event stage and each active handler's policy; Send suppliers operate on committed inputs, Complete transforms outputs.
- Invalidation or expiry: Transient message edits disappear next query; persistent edits alter carried context. Deactivating a hook ends its scope but cannot reverse side effects already performed.
- Activation or effect: Wired admission, replacement and veto seams; ReturnType mismatches can yield recoverable feedback and final mismatches become terminal errors.
- Evidence limits: Ordinary hook exceptions are logged and swallowed; configured enforcement is conditional on handlers successfully emitting valid effects. A supplied result does not prove underlying work ran.

This is also capability/production-machinery admission: the caller replaces LLM/REPL/protocol components or activates hooks; component/interface checks admit them, not a security review. Guidance is caller-provided configuration and handler code. A model can propose such changes only when given the necessary objects/imports. Rejection is possible through setup/type checks or explicit Abort. Recovery is caller restoration/deactivation; no general transactional rollback of component or tool side effects is established. SRC-1, `src/jaz/config.py`, `src/jaz/invoke.py`, `src/jaz/repl/compiler.py`.

> # Execute the COMMITTED code — the enter code after any InsertCode/DeleteCode
> # edits (span.committed_code == the original when no hook edited it).
> --- `src/jaz/_agent.py`

> if span.supplied is not None:
>     # A Send-composed SupplyExecResult short-circuits execution: skip running
>     # the code and use the supplied result instead.
>     exec_result = span.supplied
> --- `src/jaz/_agent.py:710-713`

#### RT-RTE-host-tools
Label: Supplied Python capability effects

A caller binds tools as ordinary inputs, optionally through Library; generated code calls those host functions. The smallest concrete forcing witness is SWE_LIBRARY's shell/read/replace implementation. Tool execution occurs as host Python and can invoke subprocesses or real file access outside agent-source wrappers. The caller decides the grant; the model proposes arguments; these SWE functions perform effects without a per-call human gate in their implementation. Operating mode is open tool use. Their return values/errors are execution feedback, not an expected-answer oracle. SRC-1, `src/jaz/_library/swe.py`, `src/jaz/_invoke_tool.py`, `src/jaz/repl/permissions.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: CompletedProcess, file text, None or a host exception, consumed by the calling REPL.
- Later read-back: Tool writes can persist in external files and later be read if granted; the runtime does not itself decide those future consumers.
- Delegated visibility: A tool/reference can be explicitly passed to children or inherited through scope; exposure is a caller/parent choice.
- Selection predicate: Tool grant plus generated Python call; SWE replace rejects missing or ambiguous text unless replace_all permits it.
- Invalidation or expiry: Host capability lasts while reachable; external file/process effects are not invalidated by ending the REPL call.
- Activation or effect: Shipped shell execution and file modification are available if the library is granted. Actual grants in a deployment and execution are unobserved.
- Evidence limits: No implication of default shell exposure, OS confinement or universal file-policy mediation; arbitrary tool implementations require independent contracts.

For product/capability changes through files or shell, proposed change is the model-chosen command/edit under task guidance; the tool performs admission. The exact-match replace guard checks edit targeting, not semantic correctness or improvement. Rollback is external (for example caller-managed version control), not implemented by these functions.

> result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
> --- `src/jaz/_library/swe.py`

> with open(file_path, "w") as f:
>     f.write(new_content)
> --- `src/jaz/_library/swe.py`

The stronger claim that the sandbox is agent-unstrippable under every grant is explicitly contradicted by compiler documentation:

> # hooks' ModifyExecResult. The compiler enforces the sandbox on every exec, but it is NOT
> # un-strippable by the agent: ``repl_configs`` is an ordinary config key, so a host that hands the
> # agent a config-override surface (e.g. passing ``jaz.ConfigOverride`` in as an input)
> # opts into letting the agent reconfigure this sandbox for its sub-invokes.
> --- `src/jaz/repl/compiler.py`

#### RT-RTE-trajectory-replay
Label: Saved response supply into live execution

TrajectoryReplay loads a selected ATIF file. InvokeEnter takes the next saved child of the shared stack's top node and pushes a frame; LLMQuerySend selects `self._invoke_stack[-1]`, not a node looked up by the query event's invoke ID. With strictly sequential nesting, that frame supplies the current invoke's saved queue. Concurrent invocations can instead receive another frame's saved code or have a divergence detector latch another node. Model authorship originally supplies response content; runtime code selects and admits replay content, with no per-response human review established. The caller chooses the trace and optional divergence detection. This is a replay/live-continuation mode, not an answer oracle or proof that saved code remains appropriate. SRC-1, `src/jaz/hooks/builtin/replay.py`, `src/jaz/_agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: SupplyLLMResponse replaces the provider call; its content proceeds through normal parse/REPL execution and final response transforms.
- Later read-back: Saved response content from a prior trace reaches a later invocation as the code-producing response, not merely as quoted history.
- Delegated visibility: Under strictly sequential nesting, queues follow saved invoke-tree mapping, so children do not simply consume the parent's next response. The shared stack is not per-concurrent-invoke isolation: overlapping invocations can read another frame's queue or divergence state.
- Selection predicate: Shared stack's top node, its response cursor and exhaustion/divergence latch; no query-event invoke-ID lookup. Correspondence to the querying invoke requires strictly sequential nesting. detect_divergence defaults false and checks selected signatures rather than complete semantic equivalence.
- Invalidation or expiry: Exhaustion or latched detected divergence makes queries selecting that node go live; this corresponds to that invoke under sequential nesting only. Concurrent events can latch another node's divergence. Recorded edit signatures omit some identity/metadata and ordering inputs.
- Activation or effect: Wired replay-to-execution authority; live effects can run again. Actual exercise, equivalence and benefit are unobserved.
- Evidence limits: Static implementation and its explicit sequential-nesting precondition support the concurrency limitation, not an observed misrouting incident. Trace production is not correctness certification. No supplied trace authenticates a successful replay, and optional divergence detection has documented blind spots.

The shared-stack selection is explicit in SRC-1, `src/jaz/hooks/builtin/replay.py` (implementation); the adjacent design comment names the concurrent countercase:

> node, _ = self._invoke_stack[-1]
> --- `src/jaz/hooks/builtin/replay.py:536-540`

> # SEQUENTIAL INVOKES ASSUMED. ``_invoke_stack`` is one stack whose TOP is "the active
> # invoke", which holds only while invokes nest strictly in time. ``ainvoke`` advertises
> # concurrent execution via ``asyncio.gather``, and under it the top at any event need not be
> # the invoke that raised it — so a query can be served from a sibling's queue and a
> # difference in one invoke can latch another's ``diverged``. Pre-existing (mis-serving was
> # already possible), tracked in #1310; the assistant-turn detector inherits it rather than
> # introducing it.
> --- `src/jaz/hooks/builtin/replay.py`

Admission trigger is hook installation and a query; proposed change is replacing a fresh response with saved content. Runtime can reject replay on the above predicates; rollback of re-executed effects is not automatic. What persists is the ATIF file; saving it alone does not show learning or improved future capacity.

> if node.is_exhausted:
>     # This invoke has no more saved responses — go live.
>     return []
> --- `src/jaz/hooks/builtin/replay.py`

> SupplyLLMResponse(
>     content=r.content,
>     prompt_tokens=r.prompt_tokens,
>     completion_tokens=completion_tokens,
>     cost_usd=r.cost,
> )
> --- `src/jaz/hooks/builtin/replay.py`

#### RT-RTE-settings-change
Label: Console helper proposal and human admission

A `%` request invokes a restricted helper with current configuration text, reference guidance, source-file access and conversation transcripts. Helper policy asks for either an answer or a code snippet. The model proposes; the console interprets the tagged return; an interactive human accepts or vetoes code. ReturnType checks response shape, not correctness. This is open assistance with human-gated actions, not an automated optimization curriculum. No expected-answer oracle is established; reference docs/config are guidance and evidence, not scored reference outcomes. SRC-1, `src/jaz/console.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answers print; code is displayed and runs in the live host namespace only after yes/ y. Non-TTY code application raises after displaying it.
- Later read-back: Main/helper session transcripts can inform subsequent helper invocations; model/backend choices can persist to settings JSON and reload at console startup.
- Delegated visibility: Helper gets text snapshots, reference/source paths and transcripts rather than a live configuration object; its override pins PythonREPL restrictions and a recursion leaf.
- Selection predicate: Model chooses answer versus code; console normalizes the response, then TTY availability and explicit yes determine execution.
- Invalidation or expiry: Human denial leaves proposal unapplied; failed execution can leave partial effects. Reconfiguration/restoration is manual; not all snippets persist configuration to disk.
- Activation or effect: Accepted snippets can change configuration/capabilities or run other host code; source wiring does not demonstrate a particular change or improvement.
- Evidence limits: Gate covers helper proposals only. Arbitrary confirmed code is unsandboxed. Settings-write failure may leave the live model switch effective without durable persistence.

Admission guidance explicitly separates questions from actions and asks the helper to read supplied configuration/reference/source. Proposed changes are Python strings. The persisted model switch stores backend and model; the inspected writer preserves unrelated settings and refuses to overwrite malformed JSON. The operator can reject before execution, but approval is not semantic validation or rollback. SRC-1, `src/jaz/console.py`:

> answer = input("Run this? [y/N] ").strip().lower()
> if answer not in {"y", "yes"}:
>     remember(applied=False)
>     print("%: discarded — nothing was changed.")
>     return
> --- `src/jaz/console.py`

> exec(compile(snippet, "<jaz-settings>", "exec"), namespace)
> --- `src/jaz/console.py`

#### RT-RTE-workflow-emission
Label: WorkflowReplay program materialization

With WorkflowReplay active, InvokeEnter creates an invocation context/file, query completion stashes response text, REPL events capture code/result, and InvokeExit finalizes even partial failed/aborted runs. The observer turns trace-associated Python into generated function bodies and standalone entry blocks. SRC-1, `src/jaz/hooks/builtin/workflow_replay.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Passive hook returns no result override; it writes Python files under its configured output directory.
- Later read-back: Generated entry blocks afford later standalone execution; no automatic installation into the next Agent invocation is established by this hook.
- Delegated visibility: Generated contexts retain parent/child structure and merge explicit inputs with resolved scope for function parameters.
- Selection predicate: Active hook and completed execution-event payloads; recoverable-error code is wrapped in try/except, terminal Raise is written as-is.
- Invalidation or expiry: Files remain until externally changed/deleted; failed/aborted runs can produce partial workflows, not just successful recipes.
- Activation or effect: Wired trace-to-program emission, with later execution only afforded. Production use and equivalence to the model-run behavior are unobserved.
- Evidence limits: Materialization captures REPLExecEnter code; intervening code-edit hooks and arbitrary host objects complicate equivalence. No correctness gate, benchmark or deployment consumer was supplied.

For production-machinery admission, the model originally proposes execution code under its task guidance; observer software admits emitted source without a per-file human approval. It persists program bodies, not a validated theory of how to solve future tasks. Rejection/rollback is external deletion/replacement or declining to run the generated program. Automatic emission does not establish autonomous improvement of JAZ itself.

> case _:
>     # Everything else — clean `Continue`, `Return`, and terminal
>     # `Raise` — is written as-is. Crucially, a terminal `Raise` is NOT
>     # swallowed (#710): writing it as-is lets the replay re-raise and
>     # terminate where the original did.
>     _write_indented(f, code, "    ")
> --- `src/jaz/hooks/builtin/workflow_replay.py`

### Claims

#### RT-CLM-repl-work
Label: Model-directed REPL computation

The package claims a conversation in which model-generated code runs until native return/raise. This is supported as implementation capacity by [RT-RTE-agent-loop](#rt-rte-agent-loop), not as observed task performance. SRC-1, `src/jaz/__init__.py`:

> An agent runs as a conversation with a Python REPL: the LLM writes code, sees what it
> evaluated to, and iterates until it finishes with a native ``return`` (or ``raise``)::
> --- `src/jaz/__init__.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-response-execution
Label: Response text becomes executable source

Consumer: CodeOnlyProtocol then PythonREPL. Channel: final LLMQuery response content, including hook-supplied replay. Force: symbolic code execution subject to configured compiler/builtin policy and trusted hook transforms; comments instead inform later model interpretation if retained in context. Horizon: current turn and subsequent state/effects, potentially external files. SRC-1, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`; evidence and quotes are in [RT-RTE-agent-loop](#rt-rte-agent-loop) and [RT-RTE-trajectory-replay](#rt-rte-trajectory-replay). Delivery is wired; successful execution of a particular response is unobserved.

#### RT-BAP-helper-proposal
Label: Confirmed helper code controls the host

Consumer: console's host namespace executor. Channel: model-proposed snippet after interactive confirmation. Force: native unsandboxed Python, capable of changing live configuration and other host-visible state; not merely advisory after approval. Horizon: session effects and any explicitly persisted setting/file. SRC-1, `src/jaz/console.py`; passage and limits are in [RT-RTE-settings-change](#rt-rte-settings-change). A displayed but rejected snippet has no such execution authority.

## Annotations

none
