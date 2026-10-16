---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OS-Copilot workflow account tracing the shipped FRIDAY request through dependency handoffs, execution, repair and delivery limits."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
---

# OS-Copilot workflow report

## Workflow account

### Selection and evidence

This account selects the ordinary FRIDAY workflow entered through `quick_start.py`. Its default request is to copy text files containing “agent” from the document directory into an “agents” folder. This shipped caller joins planning, prerequisite-result transfer, host execution, judgment and recovery in one implemented path. It therefore provides a stronger workflow witness than joining separate examples. The model chooses the actual decomposition; no particular sequence of file-discovery, reading and copying nodes is asserted to have occurred (SRC-1, `quick_start.py`; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)).

The evidence is implementation at the revision fixed in [boundary](boundary.md), not an execution trace. No target program, test, model call or service was run. This inspection checked `quick_start.py`, the full agent and planner control flow in `oscopilot/agents/friday_agent.py` and `oscopilot/modules/planner/friday_planner.py`, and generation, execution, judgment and repair in `oscopilot/modules/executor/friday_executor.py`. This adds workflow scrutiny of prerequisite payloads, cycle handling and replan insertion within SRC-1; it adds no source or observed-operation evidence. Provider compliance, actual filesystem changes and task correctness remain unobserved.

### Request to executable work

The caller supplies task text and configuration and constructs FridayAgent with planner, retriever, executor and ToolManager. FridayAgent remains the next-step owner throughout. Its method calls divide responsibilities inside one process; they do not launch autonomous workers or grant separate agent principals. The initiating request is the human contribution, not approval of each generated program ([RT-RTE-task-execution](runtime.md#rt-rte-task-execution)).

At each `run`, the agent clears its plan and inner monologue. Retrieval first supplies relevant retained-tool descriptions. The planner model receives those descriptions together with the task, OS version, API descriptions and working-directory listing. Its JSON output proposes named subtasks, types and dependencies. Fixed planner code builds the graph and topologically orders incomplete nodes. The agent pops nodes sequentially; a dependency graph here is not evidence of concurrent execution ([RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph); SRC-1, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/agents/friday_agent.py`).

For each node, the agent passes its description and direct prerequisites to execution. The prerequisite handoff contains each dependency's description and stored return value, not its entire execution history or a delegated worker transcript. For Python, a separate description-based retrieval supplies up to three retained code examples. The generator receives this selected code, prerequisite JSON, task name and description, OS version and working directory. Retrieved tools guide new code generation rather than being called automatically by the retriever ([RT-BAP-tool-context](runtime.md#rt-bap-tool-context); SRC-1, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/modules/executor/friday_executor.py`).

The executor extracts a generated program and, for Python, an invocation. It appends a `result=` invocation and print markers before dispatching to Env. Program output/error and directory information return as execution state; the agent retains the original candidate, node type, description, output and selected examples in ExecutionState. These are host-execution handoffs, not a worker-return protocol. The effect boundary is the caller's host environment, not an independently demonstrated sandbox ([RT-RTE-task-execution](runtime.md#rt-rte-task-execution)).

### Verification and rejection

For Python, Shell and AppleScript nodes, FridayAgent sends the code, node description, execution evidence and successor requirements to the executor's model judge. The judge receives at most the first 999 output characters when output exceeds 1000 characters; repair receives the full output. Thus the execution record and the verification input need not contain the same evidence. Task text, errors and directory listings guide judgment; no expected-answer oracle is supplied. The judge is a best-effort semantic check, not an independent file-content comparison ([RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair); SRC-1, `oscopilot/modules/executor/friday_executor.py`).

The returned status controls progression. `Amend` withholds completion and delegates candidate revision to another executor model call; `Replan` delegates prerequisite generation to the planner model. Any other initial status takes the completion branch. The repair loop, in contrast, requires `Complete` for successful repair and raises on an otherwise unrecognized judge status after error-free execution. This asymmetry prevents treating status parsing as a uniform three-value acceptance check (SRC-1, `oscopilot/agents/friday_agent.py`; [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)).

QA and API are possible nodes in this same workflow, but bypass this code-judgment branch. QA returns model text. API generates and executes Python through the API environment alias without Python's invocation wrapper. Both are marked complete by the agent's alternative branch. A workflow containing such nodes therefore cannot inherit a claim that every output or program passed the judge ([RT-RTE-api-qa](runtime.md#rt-rte-api-qa)). No selected plan or run establishes whether this default request actually uses those types.

### Recovery and resumed handoffs

On `Amend`, FridayAgent owns a bounded repair loop. The reviser receives the current candidate, description, full output/error, directories, critique and prerequisite payload. The replacement is executed immediately. If execution still reports an error, the next attempt remains `Amend`; otherwise the model judges the replacement. `Complete` releases a successful result, `Replan` transfers recovery to planning, and exhaustion leaves the subtask incomplete and stops the outer task loop. No intervening human veto or rollback of prior host effects is established ([RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)).

On `Replan`, critique becomes the retrieval query and the planner's recovery reason. The planner also receives the failed node's name/description, retrieved descriptions and current directory listing. The payload is not the whole original graph or execution transcript. Parsed new nodes are inserted, the last new node becomes an additional prerequisite of the current task, and the planner rebuilds the incomplete-node order. The agent continues without marking the failed node complete. This can return control to that node after new work, but there is no global replan-attempt bound in the inspected loop (SRC-1, `oscopilot/modules/planner/friday_planner.py`; [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)).

Structural planning failure has a separate limit: topological sorting can leave a partial queue while returning a cycle diagnostic. Its callers do not enforce that diagnostic as a task failure. Queue exhaustion therefore does not prove that all planned nodes were completed; see the graph annotation below. Missing initial JSON instead calls `sys.exit`, and ordinary exceptions inside task execution are printed before the task loop breaks (SRC-1, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/agents/friday_agent.py`). These exits do not share a typed failure product.

### Result delivery and optional retention

On accepted completion, the agent copies the node result into `inner_monologue.result`, stores the result and selected examples on the graph node, and marks that node complete. Later dependent generators receive the selected prerequisite payload described above. This is the consequential return handoff within the workflow. It does not independently establish that a file operation achieved the user's intent (SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/planner/friday_planner.py`; [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph)).

A completed Python node whose judge score meets the configured threshold also enters automatic tool admission. This is a future-use side effect, not the user's delivered file-copy result. The supplied runtime establishes a candidate-identity defect: successful repair updates score/result but not the outer code variable subsequently stored. Thus a workflow can hand a repaired result to successors while offering the original candidate for retention. Retention does not certify that the persisted candidate passed the successful execution ([RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission)).

For the selected request, delivery would mean the requested filesystem effects, accompanied by printed/logged results; the source alone does not establish those effects occurred. `run` returns no explicit final answer or typed success/failure object. Its last accepted result is accessible in the inner monologue, but is neither necessarily a synthesis of all node results nor evidence of whole-task verification. The UI caller surfaces process/log output rather than supplying an independent task oracle. Normal queue exhaustion, repair failure and a caught exception can all reach the end of `run`. Consequently a normal method return is not a dependable delivery acknowledgment ([RT-RTE-task-execution](runtime.md#rt-rte-task-execution); SRC-1, `oscopilot/agents/friday_agent.py`).

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

#### On [RT-OBJ-tool-graph](runtime.md#rt-obj-tool-graph)

Workflow-specific handoff: direct prerequisite descriptions and return values are serialized for the next invocation. The payload does not include predecessor candidate code or critique automatically. SRC-1, `oscopilot/modules/planner/friday_planner.py`:

> for task in self.tool_graph[current_task]:
>     task_info = {
>         "description" : self.tool_node[task].description,
>         "return_val" : self.tool_node[task].return_val
>     }
>     pre_tasks_info[task] = task_info
> --- `oscopilot/modules/planner/friday_planner.py`

Workflow termination limit: `topological_sort` builds `sub_task_list` incrementally and returns this diagnostic on a cycle; `decompose_task` and `replan_task` call it without checking its return. Cyclic work can remain outside the queue, so the agent's queue-empty condition is weaker than graph completion. This is source control-flow evidence, not an observed malformed plan or a claim that ordinary plans are cyclic. SRC-1, `oscopilot/modules/planner/friday_planner.py`:

> if len(self.sub_task_list) == len(graph):
>     print("topological sort is possible")
> else:
>     return "Cycle detected in the graph, topological sort not possible."
> --- `oscopilot/modules/planner/friday_planner.py`

#### On [RT-RTE-feedback-repair](runtime.md#rt-rte-feedback-repair)

Workflow-specific recovery handoff: replanning inserts new prerequisites rather than rolling back the failed node's prior effects. Its last inserted node becomes a dependency of the current task, then incomplete nodes are reordered. The existing route's owner/status and evidence limits still apply. SRC-1, `oscopilot/modules/planner/friday_planner.py`:

> last_new_task = list(new_task_json.keys())[-1]
> self.tool_graph[current_task].append(last_new_task)
> --- `oscopilot/modules/planner/friday_planner.py`

#### On [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Workflow-specific delivery boundary: acceptance releases result text to the next dependent invocation and updates the accessible last result. Neither this update nor a normal `run` return is a whole-task acceptance oracle. SRC-1, `oscopilot/agents/friday_agent.py`:

> if isTaskCompleted:
>     self.inner_monologue.result = result
>     self.planner.update_tool(tool_name, result, relevant_code, True, node_type)
> return isTaskCompleted, isReplan
> --- `oscopilot/agents/friday_agent.py`
