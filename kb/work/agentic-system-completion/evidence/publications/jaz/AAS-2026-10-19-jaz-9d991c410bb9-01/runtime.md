---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "JAZ runtime baseline: Python execution, recursive invocation, hook controls, replay and console change admission at the frozen release."
run-id: AAS-2026-10-19-jaz-9d991c410bb9-01
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
---

# JAZ runtime report

## Runtime account

### Evidence and consequential work

JAZ owns an enclosing model/code/observation loop, not just a provider client. A caller supplies named Python objects, including task text and tool callables. JAZ describes them to a model, binds their payloads into a Python namespace, executes the model's code, and returns a Python value or raises an exception. Recursion launches another such loop. The console adds persistent model selection and session conversation history. See [RT-RTE-agent-loop](#rt-rte-agent-loop), [RT-RTE-recursive-invoke](#rt-rte-recursive-invoke), and [RT-RTE-console-turn](#rt-rte-console-turn). SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/console.py`.

This is source inspection at the boundary member's commit. No target, examples, tests or providers were executed. Implementation conclusions below do not establish activated strategies, successful tasks, effective containment under attack, or improvement. Added SRC-1 coverage includes the invocation setup and closure; sync and async iteration paths; compiler, builtin policy and execution entry points; return/code validators and result composition; recursion and context warning hooks; replay serving/fallback; workflow emission; console proposal/admission, settings reload and model switch. These supply implementation evidence. Templates, comments and docstrings supply doctrine/design or attributed reports, not observed-run evidence. Other adapters and the full concurrency behavior of replay remain uninspected, not absent.

### Ordinary invocation and ownership

For a host call such as `invoke(ReturnType(int), task=..., tool=...)`, the principal is the caller granting live Python objects. Positional arguments are hooks plus at most one local configuration override; all keyword arguments are agent inputs. Setup resolves scope/configuration, allocates an invocation UUID, and records parent invocation UUID, depth and parent iteration. Root depth is one; iteration indices start at zero. Inputs and scope remain separate provenance channels until merged for binding. Ordinary inputs do not propagate automatically; scope does. SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`.

Each invocation owns a new message list, REPL state and history list. The configured REPL is a reusable template. The code-only protocol supplies natural-language format instructions but treats returned text as Python source, rather than searching for a code fence. The model chooses the next action; the runtime controls admission and execution. A text-only answer in this mode is not a separate terminal response: malformed Python produces recoverable feedback. Empty completion content can become an empty-code turn. SRC-1, `src/jaz/protocol/code_only.py`, `src/jaz/repl/python_repl.py`.

> - Respond with ONLY code. Your entire response will be sent verbatim to the REPL and executed as code.
> --- `src/jaz/protocol/code_only.py`

At InvokeEnter, hooks may edit inputs or remove recursion. InvokeSend admits the committed inputs or supplies a terminal result. Otherwise JAZ initializes state and renders the opener. LLMQueryEnter edits the query; the committed message list is delivered to LLMQuerySend, where a hook may supply the response. If not supplied, the configured model client is called. Complete-stage response transforms can change what the parser receives. The default LiteLLM adapter projects the first choice's message content, usage and cost into a response; its raw provider response is retained, but the shipped code-only route is not a provider-native tool-call executor. Custom protocols can inspect the raw response; their behavior is not established here. SRC-1, `src/jaz/_agent.py`, `src/jaz/llm/_litellm.py`, `src/jaz/protocol/code_only.py`.

After parsing, REPLExecEnter edits code and namespace. Drops precede adds. REPLExecSend sees committed code; a supplied result skips execution. Otherwise PythonREPL compiles and executes that same code. REPLExecComplete composes result transformations. The finalized result is recorded in history. A Continue appends an observation and queries again; Return or Raise closes the invocation through InvokeComplete, then the caller receives the final post-transform value or exception. Exit events observe the post-transform outcome; they are not another result-editing stage. SRC-1, `src/jaz/_agent.py`, `src/jaz/hooks/dispatcher.py`.

> exec_result = self.repl_template.exec(
>     state, span.committed_code, str(iteration), exec_timeout_override
> )
> --- `src/jaz/_agent.py`

Native top-level return is transformed into a private signal, rather than terminating ordinary Python through a return outside a function. Syntax/import-policy failures and ordinary execution errors become Continue feedback. Fatal errors and foreign enclosing timeout/memory errors propagate; provider errors remaining after retry propagate rather than being converted to an answer. Return validation can request another attempt or terminate with an error. There is no unconditional iteration ceiling: stopping comes from a terminal result or installed governance. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/_agent.py`, `src/jaz/invoke.py`.

> for i in itertools.count():
> --- `src/jaz/_agent.py:1062-1062`

`ainvoke` uses the same setup and shared parse/finalization helpers, but awaits provider completion and REPL execution and permits top-level await. Async does not itself provide stronger isolation. The agent-bound recursive primitive constructed by setup calls the synchronous internal invoke; async execution can additionally use asynchronous callables if the host supplies them. SRC-1, `src/jaz/invoke.py`, `src/jaz/_invoke_tool.py`, `src/jaz/_agent.py`, `src/jaz/repl/python_repl.py`.

### Context, coordination and persistence

Recursive calls allocate a separate model conversation and REPL frame. The parent selects explicit child inputs; resolved scope is inherited. Child working messages do not automatically enter the parent window; its return value does. This resembles a stack frame, but live mutable Python objects can be shared, returned closures can escape, and execution is not a process boundary. The closure carries configuration, hook and parent context across raw thread hops, with the parentage limits below. No general remote-worker isolation is established. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/invoke.py`, `src/jaz/repl/python_repl.py`.

The protocol abbreviates observation text before the next model query. It does not equivalently truncate the history record: continuing output is retained there whole, while terminal results record empty output. Thus bounded delivery is not deletion of the underlying text. Hooks can transiently filter or persistently replace messages; persistent edits replace the carried list before the next step. ContextWindowWarning only adds advisory text; it does not implement automatic compaction. See [RT-RTE-context-control](#rt-rte-context-control). SRC-1, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`, `src/jaz/hooks/builtin/context_window.py`.

The console runs Python as well as prompt sigils. Installed `jaz` and module invocation reach `main`, which loads console-only settings, applies flags, builds a namespace, installs selected session hooks, and routes interactive, command, file or piped input. Prompt turns receive the live conversation-history object after the first turn, and record results or failures for later turns. Direct host Python is not an agent sandbox path. Replay and workflow materialization are separate consumers of recorded work, described in [RT-RTE-trajectory-replay](#rt-rte-trajectory-replay) and [RT-RTE-workflow-emission](#rt-rte-workflow-emission). Memory revisions and detailed retained-object analysis are left to the memory member. SRC-1, `src/jaz/console.py`, `src/jaz/hooks/builtin/replay.py`, `src/jaz/hooks/builtin/workflow_replay.py`.

### Four forcing cases and guarantee boundaries

**1. A restrictive REPL is not a deployment sandbox.** Owner: PythonREPL/compiler/builtin wrappers. Enforcement: static import/attribute checks plus policy-bound builtin import/open/attribute wrappers. Strength: policy for the configured namespace, not a deployment guarantee. Ordinary sync/async Python compilation passes explicit allowlists; import and file grants default closed. Capability surface includes arbitrary supplied Python functions and any permitted modules. Current grants are invocation-specific; no actual deployment grant set was supplied. A host tool runs its own Python: shipped SWE tools use ordinary open and `subprocess.run(..., shell=True)`, not the REPL's wrapped open. Granting these tools is therefore materially different from granting direct sandbox file access. Their callable availability must be established by host inputs; they are not automatically granted to every invocation. SRC-1, `src/jaz/repl/permissions.py`, `src/jaz/repl/python_repl.py`, `src/jaz/repl/compiler.py`, `src/jaz/_library/swe.py`, `src/jaz/inputs.py`.

> result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
> --- `src/jaz/_library/swe.py`

Two narrower counterexamples prevent a universal policy claim. First, supplying ConfigOverride lets the agent replace the child's REPL configuration; the current implementation does not enforce an immutable ancestor sandbox through that surface. Second, initialization installs the protected builtins dictionary and then blindly updates the namespace with resolved top-level inputs. Public invocation accepts arbitrary keyword names; normalization passes plain values through, and setup and payload resolution do not filter `__builtins__`. A caller-supplied input of that name therefore replaces the dictionary at this binding point. This is a source-traced caller-controlled construction path, not an observed hostile exploit. It does not remove the separate static compiler checks. The added-input/variable effect path is not proof that initial binding is protected. SRC-1, `src/jaz/invoke.py`, `src/jaz/templates.py`, `src/jaz/inputs.py`, `src/jaz/repl/python_repl.py`, `src/jaz/repl/compiler.py`.

> init_repl_state_locals.update(inputs)
> --- `src/jaz/repl/python_repl.py:1456-1456`

Required external contract: hosts must withhold dangerous object/configuration surfaces and impose OS/process isolation when needed. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-CLM-repl-policy](#rt-clm-repl-policy).

**2. A configured timeout is not automatically an unraisable ceiling.** Owner: PythonREPL plus execution guards. Enforcement: `_resolve_timeout`, then guarded execution in the host interpreter. Strength: best effort resource control. With the default `allow_timeout_pragma=True`, a leading model-written timeout overrides both the caller override and configured default without a ceiling. With it false, the comment is not parsed and the caller override/configuration supplies the timeout. Both exec and aexec resolve this choice before execution. A malformed enabled pragma becomes a Continue without executing code. SRC-1, `src/jaz/repl/python_repl.py`.

> if not self.allow_timeout_pragma:
>     return (
>         exec_timeout_override
>         if exec_timeout_override is not None
>         else self.exec_timeout
>     )
> pragma_timeout = _parse_timeout_pragma(src)
> if pragma_timeout is not None:
>     return pragma_timeout
> --- `src/jaz/repl/python_repl.py`

Guarded execution uses host `exec`, monitoring/deadline machinery and, where applicable, main-thread signals. The guard source explicitly limits blocking C calls on workers, reused pool threads and raw thread spawning; memory checks sample process RSS rather than precluding allocation. Required external contract: an external supervisor for a deployment-level hard bound. A supplied exec result skips code and its execution guard entirely, while a supplied model response still reaches the REPL. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/jaz/repl/_exec_guards.py`, `src/jaz/_agent.py`.

**3. Recursion limits depend on propagation and parent identity.** Owner: opt-in RecursionLimit. Enforcement: InvokeEnter removes the built-in recursive tool at the cap and aborts an over-cap child. Strength: policy over correctly attributed invocation trees. Local installation is rejected; a propagating context is required. Same-thread public invoke inside a supplied callback reads the current child prehook, so merely omitting the built-in tool is not the only enforcement. However a public invoke reached on a raw worker with no inherited context creates a new root. The bound closure repairs missing worker context using its capture, but a closure passed down from an ancestor and called on a raw worker attributes to the binder rather than the actual caller. The hook's own documented limitation matches the inspected fallback. No universal stack-depth bound follows. Required external contract: preserve live context across thread dispatch and avoid untracked process delegation. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1, `src/jaz/hooks/builtin/recursion_limit.py`, `src/jaz/invoke.py`, `src/jaz/_invoke_tool.py`.

> prehook = get_active_prehook() or Prehook(repl_depth=1)
>
> # Call _invoke with prehook
> --- `src/jaz/invoke.py`

> effective_prehook = get_active_prehook() or prehook
> --- `src/jaz/_invoke_tool.py`

**4. Supplied results have different enforcement points.** Owner: dispatcher and installed validators. Strength: invariant of the inspected event/result path, conditional on installing the hook and trusting host extension code. A supplied model response bypasses the provider, not code admission. A supplied exec result bypasses compilation/execution but still reaches REPLExecComplete. A supplied invocation result bypasses opener, REPL and model work but still reaches InvokeComplete. ReturnType rechecks a new final Return there, including one reinstated by another per-exec transform; InvokeComplete's Raise effects outrank Return effects in the fold. ValidateREPLCode instead sees only committed code at REPLExecSend, so it does not validate arbitrary effects already performed by host callbacks or hooks. Its rejection skips the code, not earlier namespace/input resolution. Required external contract: validator correctness and non-malicious host callbacks/hooks. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-hook-admission](#rt-rte-hook-admission). SRC-1, `src/jaz/_agent.py`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/builtin/repl_code_hooks.py`, `src/jaz/hooks/dispatcher.py`, `src/jaz/hooks/effects.py`.

> if isinstance(result, Return) and result is not already_ok:
>     error = _return_type_error(result.return_value, self.return_type)
> --- `src/jaz/hooks/builtin/return_hooks.py`

This establishes a checked type/value path, not an answer-correctness oracle. Omitting ReturnType removes that contract; spelling `return_type=` as a keyword supplies ordinary input instead. A validator is caller-supplied computation, not necessarily a human approval or reference answer. SRC-1, `src/jaz/invoke.py`, `src/jaz/hooks/builtin/return_hooks.py`.

### Change-admission planes

Runtime extensions enter as host-created hooks, protocol/REPL/model components, configuration overrides and live Python inputs. The dispatcher gives hooks input, code, message and result authority at distinct stages; activating a hook is not per-effect human approval. These are powerful in-process extension channels, not constrained plugin sandboxes. See [RT-BAP-hook-effects](#rt-bap-hook-effects). SRC-1, `src/jaz/hooks/dispatcher.py`, `src/jaz/invoke.py`, `src/jaz/_agent.py`.

The console `%` helper is a narrower change proposal route: a leaf agent receives redacted configuration text, reference/source access and transcript text, returns an answer or a code snippet, and only the code tag reaches a terminal confirmation gate. Confirmed snippets execute in the host console namespace. A model switch pings a proposed backend/model before updating live configuration and attempting persistence; startup reload gives the stored choice later authority. This does not establish model-quality improvement. WorkflowReplay automatically emits a Python program from execution events but does not automatically install it as JAZ's next runtime. See [RT-RTE-settings-admission](#rt-rte-settings-admission), [RT-RTE-workflow-emission](#rt-rte-workflow-emission), and [RT-BAP-settings-load](#rt-bap-settings-load). SRC-1, `src/jaz/console.py`, `src/jaz/hooks/builtin/workflow_replay.py`.

The repository's generated-release statement in the boundary prevents inference about the unshipped product-development/evaluation loop. No claim here establishes autonomous source revision, weight training, successful self-improvement or causal benefit from replay. Those cannot be inferred from code generation, settings mutation or retained execution records alone.

## Shared records

### Components

#### RT-CMP-llm
Label: Configured provider model

Source-native identity: the configured `llm` component and its selected model identifier. Representational form: distributed-parametric model, exposed through symbolic Python adapter configuration. Storage substrate: provider-hosted parameters, not weights in this Git tree. The inspected default adapter calls LiteLLM sync/async completion; other adapters are available but not fully traced. SRC-1, `src/jaz/llm/_litellm.py`, `src/jaz/invoke.py`, `src/jaz/console.py`.

> response = litellm.completion(**params)
> --- `src/jaz/llm/_litellm.py`

Parameter changes during operation: no parameter-write path is established in the inspected invocation/adapter path; provider internals remain uninspected. Exact version pinned: not established by the source revision; a configured identifier is not a weight digest. Mutable endpoint resolving to another model: possible through provider-controlled routing and explicit configuration/model switching; actual provider resolution is uninspected. The model chooses code under open user requests; no expected-answer oracle is inherent in completion.

#### RT-CMP-python-repl
Label: PythonREPL execution template

Source-native identity: PythonREPL. Representational form: symbolic Python implementation and frozen allowlist tuples. Storage substrate: installed source/configured in-process instance. Per-invocation mutable namespace lives in REPLState, not on the shared template. Execution is host-interpreter execution, not a newly isolated process. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/repl/_exec_guards.py`.

> if timeout is None and memory_limit_bytes is None:
>     # No guards of our own; any *outer* deadlines/caps remain enforced.
>     exec(code, globals_dict)
>     return
> --- `src/jaz/repl/_exec_guards.py`

### Operative objects

#### RT-OBJ-repl-state
Label: Invocation REPLState

Source-native identity: REPLState returned by PythonREPL.initialize. Representational form: symbolic namespace mapping and session identity; bound values may include natural-language text and live tool objects. Storage substrate: process memory. Each invocation gets its own mapping, but values can be shared references. The recursive primitive is bound before ordinary inputs, so an input named invoke shadows it. This records the runtime container, not a claim about durable memory revision. SRC-1, `src/jaz/repl/python_repl.py`.

> if invoke_tool is not None:
>     init_repl_state_locals["invoke"] = invoke_tool
> --- `src/jaz/repl/python_repl.py`

#### RT-OBJ-system-prompt
Label: Shipped system prompt

Source-native identity: system_prompt.jinja2 composed with code-only format and REPL descriptions. Representational form: natural-language instructions after symbolic Jinja rendering. Storage substrate: package template on disk, then message objects in process memory and provider input. It advertises history and conditionally the recursive tool and scoped values. Text requests behavior; compilation/validators, not the prose, enforce admissibility. SRC-1, `src/jaz/templates/system_prompt.jinja2`, `src/jaz/protocol/code_only.py`.

> You are in a multiturn REPL session.
> --- `src/jaz/templates/system_prompt.jinja2`

### Routes

#### RT-RTE-agent-loop
Label: Model-driven Python loop

Endpoints/progression: named host inputs → payload resolution and opener → configured model → protocol source → committed-code execution → observation or terminal Python result. Owner: Agent, with caller grants and model action selection. Context/state: per-invocation messages, namespace and finalized history. Effects can call supplied tools and mutate live objects. Operating mode: open user requests; next-step decision is model-generated symbolic code, with natural-language instructions. No inherent answer oracle; caller validators may add a narrower predicate. SRC-1, `src/jaz/invoke.py`, `src/jaz/_agent.py`, `src/jaz/protocol/code_only.py`, `src/jaz/repl/python_repl.py`.

- Immediate return: final Return payload or propagated terminal exception; Continue observations are internal feedback.
- Later read-back: console history and optional trace consumers can bridge invocations; ordinary loop messages alone are current-run state.
- Delegated visibility: child receives selected explicit inputs and scope, not the whole parent message list automatically.
- Selection predicate: model chooses code; runtime result kind selects continuation or termination; installed hooks can veto/replace.
- Invalidation or expiry: ordinary frame ends with invocation; live returned/shared values can outlive it.
- Activation or effect: executable route to host Python and granted tools; actual effects in a run are unobserved.
- Evidence limits: no supplied execution, task-quality or provider reliability evidence; custom components can change behavior.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Minimum execution passage is retained in Runtime account; it and the unbounded-loop passage support this route.

#### RT-RTE-recursive-invoke
Label: Recursive child invocation

Endpoints/progression: parent model-written call to bound invoke → hook/config/prehook rebasing → child setup and new loop → parent Python result. Owner: parent model chooses delegation and input content; runtime allocates child identities and applies inherited policy. Symbolic closure/context state coordinates same-process work. Host scope/configuration and propagating hooks cross the boundary; positional local hooks and overrides do not propagate automatically. Open-request mode; no reference-answer oracle or per-delegation human approval is built into this primitive. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/invoke.py`, `src/jaz/hooks/builtin/recursion_limit.py`.

- Immediate return: child's Python value, or exception to parent execution.
- Later read-back: inapplicable — ordinary delegation is current work; any child-returned retained artifact requires its own consumer path.
- Delegated visibility: explicit selected inputs plus inherited scope; shared Python references can expose more than rendered text.
- Selection predicate: parent code calls invoke; RecursionLimit checks attributed absolute depth when installed.
- Invalidation or expiry: child's local conversation ends on return; no automatic merge of its transcript.
- Activation or effect: child can execute independently selected steps using its granted namespace.
- Evidence limits: raw-worker public entry and passed-closure fallback qualify parentage/cap claims; process-context propagation is not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> parent_scope=parent_scope,
> inputs=inputs,
> --- `src/jaz/_invoke_tool.py`

#### RT-RTE-hook-admission
Label: Hook-mediated admission and terminal validation

Endpoints/progression: caller activates hook → dispatcher event → effects veto or supply committed work, or transform completed results → next model turn or terminal caller outcome. Owner: host selects hook and callable; validator computation decides rejection; model revises after feedback. Human participation is activation/configuration unless the callback itself asks a human. Operating mode: open tasks with bounded retry tolerance if configured. Answer oracle: none intrinsic; a caller predicate/type check is not necessarily a reference answer. SRC-1, `src/jaz/hooks/builtin/repl_code_hooks.py`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/dispatcher.py`, `src/jaz/hooks/effects.py`.

Admission fields: trigger is committed code or candidate return; proposed change is executing that code or accepting that result. ValidateREPLCode rejection supplies Continue or Abort after the tolerance; ReturnType/ValidateReturn rejection transforms the result. Model instructions and validator feedback shape retries, but successful correction is not observed. Counters persist only per invoke and are cleaned at exit. Rejecting a return does not undo earlier code/tool side effects; no transaction rollback is established. Supplied invoke/exec paths and Complete backstops are distinguished in forcing case 4.

- Immediate return: admitted result, recoverable rejection text, or terminal exception.
- Later read-back: inapplicable — failure counters and feedback govern the current invocation; later trace use is a separate route.
- Delegated visibility: propagating hooks reach nested invokes; local hooks only this invoke.
- Selection predicate: validator raises, type predicate fails, or governance emits Abort; tolerance counts cumulative failures.
- Invalidation or expiry: per-invoke counters released on exit; active hook lifetime depends on activation channel.
- Activation or effect: admission effects are wired before execution or at result boundaries; no run demonstrates correction benefit.
- Evidence limits: arbitrary host callback/hook code is trusted; code validation does not constrain every host-side effect.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.validator(event.code)
> --- `src/jaz/hooks/builtin/repl_code_hooks.py`

#### RT-RTE-context-control
Label: Query filtering and observation abbreviation

Endpoints/progression: continuing exec output → protocol abbreviation → model-visible observation; hook message edits → committed query and optional persistent buffer replacement. Owner: deterministic protocol bounds and host-selected hook effects. Model can inspect history if reachable; no automatic summarizer is established by these seams. SRC-1, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`, `src/jaz/hooks/builtin/context_window.py`.

- Immediate return: edited query or abbreviated observation, not a separate task answer.
- Later read-back: persistent edits affect later queries in the same invocation; a later independent invocation receiving a summary would require an additional persistence/delivery route not established here.
- Delegated visibility: a child gets its own context; selected history can be passed as an ordinary input.
- Selection predicate: configured maximum output length/prefix ratio; hook-selected additions/drops and persistence flags.
- Invalidation or expiry: transient edits affect one query; persistent edits replace carried messages; underlying REPL history remains separately reachable unless unbound.
- Activation or effect: reduces/changes delivered context by construction; no observed accuracy or cost improvement.
- Evidence limits: truncation may omit error text; no automatic policy for choosing a summary or proving relevance was inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> messages[:] = apply_message_edits(
>     messages, edits.persistent_drops, edits.persistent_adds
> )
> --- `src/jaz/_agent.py`

#### RT-RTE-console-turn
Label: Console prompt and host execution

Endpoints/progression: console command/file/pipe/interactive input → host Python or sigil rewrite → chat closure → public invoke → result recording and display/assignment. Owner: user/script chooses input; runtime dispatches. Each build_namespace creates main/helper histories. Host-side Python executes outside PythonREPL policy; model work uses the invocation path. SRC-1, `src/jaz/console.py`.

- Immediate return: console result/output or nonzero/error path; prompt chat returns the invoke value.
- Later read-back: subsequent prompt turns receive the live conversation_history object once nonempty; helper receives transcript text.
- Delegated visibility: template interpolations and scope supply objects through invocation; full host namespace is not automatically a child namespace.
- Selection predicate: sigil or ordinary Python syntax; input mode; history nonemptiness selects history delivery.
- Invalidation or expiry: fresh namespace means fresh session histories; no automatic cross-session history-object restoration is established here.
- Activation or effect: later input delivery and host execution are wired; behavioral use of past turns is unobserved.
- Evidence limits: recorded failure objects may be live references; no session trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if history.turns:
>     extra["conversation_history"] = history
> --- `src/jaz/console.py`

#### RT-RTE-trajectory-replay
Label: Saved-response replay with live fallback

Endpoints/progression: loaded ATIF invocation tree → saved response queue associated with live invokes → LLMQuerySend supply → ordinary parse/exec/observation loop. Owner: host activates replay; code chooses queued responses or live completion. Model work is bypassed only while a response is supplied; tools/code still execute. Operating modes: replay and live continuation, optionally divergence-sensitive. Queue position and recorded expectations are replay references, not task-correctness answers. SRC-1, `src/jaz/hooks/builtin/replay.py`, `src/jaz/_agent.py`.

- Immediate return: supplied model response; eventual caller outcome still comes through the ordinary invoke loop.
- Later read-back: saved trace responses are consumed by later invocations under replay activation.
- Delegated visibility: child nodes follow recorded nested structure; an unrecorded child falls through live.
- Selection predicate: active node exists, response remains, divergence latch unset, and optional message-edit comparison does not diverge.
- Invalidation or expiry: queue exhaustion or divergence stops serving that node; extra child subtrees go live.
- Activation or effect: supplied responses skip provider calls but not execution; no demonstrated cost saving or faithful task replay in this analysis.
- Evidence limits: not offline-only; full trace conversion, divergence comparison and concurrent task ownership were not audited end to end.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if node.is_exhausted:
>     # This invoke has no more saved responses — go live.
>     return []
> --- `src/jaz/hooks/builtin/replay.py`

#### RT-RTE-settings-admission
Label: Helper proposal and console settings admission

Endpoints/progression: `%` request plus redacted configuration/reference/source/transcript text → bounded leaf helper invoke → tagged answer or code tuple → display or confirmation → host namespace exec. Owner: user proposes goal; model proposes content and tag; human can veto code by answering other than y/yes; runtime enforces TTY and tag branches. Operating mode: open settings/help requests, not a controlled improvement experiment. Answer oracle: no reference answer; type checking constrains tuple shape and model-switch ping tests connectivity, not task quality. SRC-1, `src/jaz/console.py`.

Admission fields: helper guidance separates questions from actions and asks for returned tuples. It receives an explicitly constructed PythonREPL with imports/writes denied and package-tree read access, not the full console namespace. Confirmation admits arbitrary Python into the host namespace. Non-TTY code proposals raise rather than silently skipping; answers print without execution. Confirmed code may change live components, tools or namespace; persistence occurs only if the snippet calls a writer, such as switch_model. switch_model pings first, then configures and attempts to store backend/model; a persistence failure can leave a session-only change. Startup reload gives stored configuration later authority. Rejection leaves the proposed snippet unapplied. Generic exec has no atomic rollback if partially executed; helper history records confirmation, not proof of successful execution. This is a human-admitted production-configuration/capability channel, not automatic product-source improvement. Direct user Python/manual file editing is a distinct authorized input path and does not pass the helper gate.

- Immediate return: printed answer, discarded proposal, executed host snippet, or raised error.
- Later read-back: helper exchange history informs later helper requests; persisted backend/model is reloaded by later console startup.
- Delegated visibility: helper gets transcript/configuration text and package read grant; confirmed code gets host namespace authority.
- Selection predicate: returned answer/code tag; TTY test; y/yes confirmation; successful ping for switch_model specifically.
- Invalidation or expiry: unconfirmed code is discarded; settings can be overwritten/repaired; no automatic rollback of confirmed arbitrary Python.
- Activation or effect: gate and live configuration/persistence calls are wired; no actual admitted change or benefit observed.
- Evidence limits: sandbox resistance is not proven; helper docstrings retain older protected-key terminology, so enforcement assessment follows constructed components and reachable inputs instead.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> answer = input("Run this? [y/N] ").strip().lower()
> if answer not in {"y", "yes"}:
>     remember(applied=False)
>     print("%: discarded — nothing was changed.")
>     return
> --- `src/jaz/console.py`

> exec(compile(snippet, "<jaz-settings>", "exec"), namespace)
> --- `src/jaz/console.py`

#### RT-RTE-workflow-emission
Label: Execution-to-Python workflow materialization

Endpoints/progression: observed invocation/query/REPL events → context and iteration records → Python function/package files with child-call substitutions and main blocks. Owner: host activates WorkflowReplay; code emits artifacts without per-artifact human approval. Natural-language guidance influences original model code; emitted code is symbolic Python on disk. SRC-1, `src/jaz/hooks/builtin/workflow_replay.py`.

Admission fields: trigger is hook events; proposed/admitted content is event-derived iteration code. Recoverable errors get try/except wrappers; terminal code is emitted as-is. Finalization also runs on abnormal invoke exits, so a generated package is not a success certificate. The hook stashes REPLExecEnter code rather than reading post-edit committed source at Exit, which limits equivalence when code-editing hooks coexist. No semantic evaluator or rejection gate is established in the inspected emitter; no automatic installation into JAZ's live machinery follows from writing files. Rollback is external artifact removal/replacement, not a transaction established here. Operating mode is automatic materialization of an open task; no expected-answer oracle.

- Immediate return: passive hook returns empty effects; main invocation returns independently.
- Later read-back: generated main/function/package is intended for later Python execution; actual execution and equivalence are unobserved.
- Delegated visibility: recorded child invocations become emitted functions/packages and ordered replacement calls.
- Selection predicate: runnable REPL events with Completed payloads contribute iterations; invoke exit finalizes even partial work.
- Invalidation or expiry: files remain until externally changed/removed; emitter does not establish a validity lease.
- Activation or effect: durable code emission is wired; executing the artifact is a separate admission/effect boundary.
- Evidence limits: object reconstruction, generated imports and all call-shape rewrites are not exhaustively audited; emitted code does not demonstrate safe or equivalent replay.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> case REPLExecEnter(invoke_id=invoke_id, code=code):
>     # Stash this turn's code (only present on the runnable-code branch).
>     ctx = self.contexts.get(invoke_id)
>     if ctx:
>         ctx._pending_code = code
> --- `src/jaz/hooks/builtin/workflow_replay.py`

> program_file.write_text(final_content)
> --- `src/jaz/hooks/builtin/workflow_replay.py`

### Claims

#### RT-CLM-repl-policy
Label: Scoped REPL policy rather than complete isolation

Claimed operation: the constructor describes deny-all default imports and file access; compiler and wrapped builtins enforce configured policy for their consumers. This is supported for ordinary configured execution but not a universal all-effects isolation claim. Host tools, supplied results, initial builtin-name overwrite and granted child ConfigOverride are distinct forcing paths detailed above. SRC-1, `src/jaz/repl/python_repl.py`, `src/jaz/repl/permissions.py`, `src/jaz/repl/compiler.py`, `src/jaz/_library/swe.py`.

> allowed_imports: Import allow-list. ``None`` applies the fail-closed default
>     (deny all); ``["*"]`` is the explicit allow-all.
> --- `src/jaz/repl/python_repl.py`

- guarantee strength: policy
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-code
Label: Prompt-mediated action selection

Consumer: configured model, then Python compiler/executor. Channel: rendered system/input text → model-produced Python source. Force: natural-language instruction at the model, symbolic execution authority after admission; neither text delivery nor compilation establishes compliance with the task. Horizon: one invocation and its selected children, longer only through explicit persistence/read-back. Evidence: SRC-1, `src/jaz/templates/system_prompt.jinja2`, `src/jaz/protocol/code_only.py`, `src/jaz/_agent.py`; execution and format passages above.

#### RT-BAP-hook-effects
Label: Host extension effect authority

Consumer: dispatcher and Agent. Channel: active hook event callbacks and returned typed effects. Force: software control over committed inputs/messages/code, supplied responses/results, transforms and Abort; not merely advice except when an effect only adds prompt text. Horizon: local invocation or propagating activation extent. It admits capability/control changes from trusted host extension code without per-effect human approval. Evidence: SRC-1, `src/jaz/hooks/dispatcher.py`, `src/jaz/hooks/effects.py`, `src/jaz/_agent.py`; [RT-RTE-hook-admission](#rt-rte-hook-admission) supplies the validator passage and scope.

#### RT-BAP-settings-load
Label: Persisted console model authority

Consumer: console startup and later invoke configuration. Channel: backend/model settings on disk → load/build_config → configure → provider selection. Force: symbolic configuration, changing which component handles later work; not evidence that model weights changed. Horizon: sessions after successful persistence until overwrite. Host/user editing and confirmed snippets can choose settings; switch_model adds a connectivity probe, not an improvement evaluator. Evidence: SRC-1, `src/jaz/console.py`, `src/jaz/user_settings.py`; [RT-RTE-settings-admission](#rt-rte-settings-admission).

> partials = load_user_settings()
> --- `src/jaz/console.py`

> jaz.configure(**build_config(partials, resolvers=_CONSOLE_RESOLVERS))
> --- `src/jaz/console.py`

## Annotations

none
