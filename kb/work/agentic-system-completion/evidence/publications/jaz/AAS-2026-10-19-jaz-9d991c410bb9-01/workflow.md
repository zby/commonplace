---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "JAZ workflow account: recursive per-item processing, parent aggregation and typed delivery at the frozen release."
run-id: AAS-2026-10-19-jaz-9d991c410bb9-01
reviewed-boundary: "0803d4971be785e95b80054b02259664d70fa3da"
---

# JAZ workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is the README's recursive per-item processing request: a caller supplies `items=data`, asks the parent to delegate each item and combine the results, requires a list return, and activates `RecursionLimit(max_depth=3)`. It was selected because one shipped example connects delegation, aggregation, a return contract and depth governance. It is a documented workflow backed by executable machinery, not a supplied successful run. Neither the concrete dataset nor what “process” means for each item is specified. No claim about substantive answer correctness follows. SRC-1, `README.md`, `src/jaz/_invoke_tool.py`, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/hooks/builtin/recursion_limit.py`.

> For each item, use jaz.invoke to process it.
> Combine and return the results.
> --- `README.md`

The source example says `jaz.invoke`, but the shipped agent-facing primitive and system prompt use bare `invoke`. The account follows that actual binding, not an assumption that the framework module is automatically available in the agent namespace. This is a documentation/binding distinction, not evidence that the example failed in operation. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/templates/system_prompt.jinja2`; [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state).

> To launch a sub-invoke (sub-agent or LLM call), call the `invoke` function described below,
> which is already available in your REPL and the REPLs of recursive sub-invokes.
> --- `src/jaz/templates/system_prompt.jinja2`

This member adds implementation inspection of the recursive tool's handoff and context rebasing, the sync loop's terminal dispatch, ReturnType's feedback/backstop, and RecursionLimit's install/depth decisions. It also inspects the README example and system prompt as doctrine/design. All are SRC-1 at the boundary revision. No target execution or external service calls were performed; no observed-run or causal evidence was supplied. Existing runtime records cover these referents, so workflow-specific findings are annotations rather than duplicate declarations.

### 1. Caller to coordinating parent

The caller defines the task and grants the item object. Its positional `ReturnType(list)` constrains this invocation; its surrounding RecursionLimit context propagates to descendants. These are different lifetimes: the child does not automatically inherit the parent's local list contract. Any child-specific return contract would need to be supplied separately. The example does not supply a child schema, expected per-item answer, or reference aggregate. SRC-1, `README.md`, `src/jaz/_invoke_tool.py`; [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke), [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission).

The parent model receives the task and descriptions of bound inputs, then proposes Python code. JAZ parses and admits that code through the ordinary execution path. The request to delegate each item is model-facing guidance, not a deterministic map scheduler: the implementation does not force the parent to make exactly one child call per item or preserve item order. Those would require inspected generated code or a stronger caller validator. SRC-1, `README.md`, `src/jaz/_agent.py`; [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop).

### 2. Parent to child, then child to parent

When parent code calls bound `invoke`, the parent chooses the child's task, item and any tools through explicit keyword arguments. Each keyword becomes a named child REPL value and a rendered prompt description. Inherited scope is an additional channel. The parent transcript and its other ordinary inputs are not automatically copied. The runtime supplies invocation identity, depth, configuration and propagating hooks; the child runs a separate message/REPL loop. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/invoke.py`; [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke).

The child chooses its own code until it returns a Python value or raises. The bound call returns that value directly to the parent's executing Python, allowing parent code to collect values and construct the requested aggregate. This is a same-process function handoff, not a remote-worker job, durable queue or mandatory review stage. The parent does not automatically receive the child's full working transcript. Shared mutable input references can nevertheless expose effects beyond the returned value. SRC-1, `src/jaz/_invoke_tool.py`, `src/jaz/_agent.py`; [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke), [RT-OBJ-repl-state](runtime.md#rt-obj-repl-state).

No fixed scheduling policy is established for the example: serial versus concurrent child work and exception-handling choices depend on generated parent code. The traced baseline is the synchronous call/return primitive; the source request alone does not demonstrate how any model decomposed it. SRC-1, `README.md`, `src/jaz/_invoke_tool.py`.

### 3. Rejection and recovery

Depth governance acts before deeper work, not as a final-quality review. With the example's cap of three, an attributed depth-three child can work but loses the built-in recursive primitive; an attributed invocation above the cap is aborted. RecursionLimit must be installed through a propagating context, as in the example. Raw-worker attribution limits remain those of [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke); this is not a universal recursion bound over arbitrary host calls. SRC-1, `src/jaz/hooks/builtin/recursion_limit.py`, `src/jaz/_invoke_tool.py`.

> if event.depth == self.max_depth:
>     return [DisableRecursion()]
> --- `src/jaz/hooks/builtin/recursion_limit.py`

Return verification is separate. If the parent proposes a non-list terminal value, ReturnType converts the candidate Return into Continue carrying the type error. The model receives this feedback and owns the attempt to construct a valid replacement. The example does not configure `max_failures`; the default never escalates type mismatches by count. This permits another attempt but does not promise eventual correction or bounded termination. An explicitly configured tolerance instead produces a terminal error once failures exceed it. SRC-1, `src/jaz/hooks/builtin/return_hooks.py`; [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission).

> result=Continue(
>     output=summarize_exception(error), exception=error
> )
> --- `src/jaz/hooks/builtin/return_hooks.py`

A wrong-typed final Return introduced after the per-execution check is checked again at InvokeComplete and can become a terminal Raise rather than another model retry. Child exceptions return through parent execution; whether parent code catches one is not fixed by the workflow. Return rejection does not undo already performed item/tool mutations. No transactional recovery is established by these validators. SRC-1, `src/jaz/hooks/builtin/return_hooks.py`, `src/jaz/_agent.py`; [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission).

### 4. Aggregation and delivery

The parent, not a separate integrator, constructs the combined value. For the shown invocation, delivery means the finalized Return passes through completion transforms and its Python payload reaches the caller's `result` assignment. A terminal Raise instead propagates an exception; merely generating code or obtaining child results is not delivery. SRC-1, `README.md`, `src/jaz/_agent.py`; [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop).

> final_result = span.get_result()
> match final_result:
>     case Return():
>         return final_result.return_value
>     case Raise():
>         raise final_result.exception
> --- `src/jaz/_agent.py:1115-1120`

A list-shaped result is not proof that every item was processed, aggregation preserved correspondence, children answered correctly, or useful work occurred. The shown workflow has no substantive answer oracle and no per-child human approval. The caller supplies task, grants and governance; software enforces depth and type; models select processing and aggregation code. This is an open-request workflow, not a bounded evaluation experiment. Later persistence, workflow-package generation and replay are separate optional routes, not required delivery steps for this example. SRC-1, `README.md`, `src/jaz/hooks/builtin/return_hooks.py`; [RT-RTE-trajectory-replay](runtime.md#rt-rte-trajectory-replay), [RT-RTE-workflow-emission](runtime.md#rt-rte-workflow-emission).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-recursive-invoke](runtime.md#rt-rte-recursive-invoke)

Workflow role: delegation and local reintegration. In the selected example the coordinating parent chooses item-level child instructions and grants, then consumes returned values to assemble the aggregate. The inherited depth cap governs children, while the root's local list contract does not. No fixed work partition, item-completeness check or separate integrator is supplied by the example. Source evidence and the binding caveat are retained in Workflow account.

#### On [RT-RTE-hook-admission](runtime.md#rt-rte-hook-admission)

Workflow role: root result-shape verification. The caller proposes the list contract; ReturnType computes acceptance, can reject a non-list, and provides model-visible feedback for recoverable mismatches. No reference-answer oracle is configured. The parent model owns correction; terminal backstop failures instead return responsibility to the caller through an exception. The shown default has no mismatch-count cutoff, and rejection supplies no rollback of previous effects. Source passages are retained in Workflow account.

#### On [RT-RTE-agent-loop](runtime.md#rt-rte-agent-loop)

Workflow role: request-to-result execution and final delivery. Child completion is intermediate; root completion after hook transforms determines whether the caller receives a Python value or exception. Typed completion is narrower than semantic task acceptance. The example's decomposition request is guidance, not an enforced plan; successful execution and aggregate correctness remain unobserved.
