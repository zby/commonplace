---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "AgentFly's ordinary question-to-answer workflow through serial planner–executor delegation, MCP calls and bounded planner recovery."
run-id: AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
---

# AgentFly workflow report

## Workflow account

This account selects the ordinary CLI workflow in `client/agent.py`. It is representative because this single shipped driver connects request intake, planning, task execution, tool dispatch, replanning and printed delivery. It does not combine the interactive driver with benchmark judgment or training. The representative workflow can perform multiple tasks and tool calls, but a particular request can also terminate on the first planner reply. The account characterizes implementation, not an observed successful run (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)).

Inspection for this member read all of SRC-1 `client/agent.py`, including the prompts, backend, message trimming, client and CLI. This adds complete workflow inspection within the existing boundary, not a new source. Executable control flow supplies implementation evidence; prompt wording supplies requested behavior. No target code, model provider or tool was executed. External service behavior and successful end-to-end completion remain uninspected.

### Intake and delegation

The operator supplies a question and optional file path and chooses model names and server scripts through CLI arguments, or enters a question interactively. Python creates a UUID for each query. It launches the selected scripts through MCP stdio, discovers their tools and maps tool names to sessions. Duplicate names reject connection rather than silently choosing a server. The question, UUID and file path become user-message text; the file path is not itself loaded into the planner by this driver. Tool schema discovery occurs before the query history is reset (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)).

Python, not either model, owns progression. The planner receives its system prompt and shared conversation, with no tools supplied to its backend call. It proposes a JSON plan containing task IDs and descriptions, or claims completion with a `FINAL ANSWER:` prefix. Python parses the plan and delegates tasks serially in the returned order. Each task's executor conversation contains the executor system prompt, the shared history including the plan and any preceding task results, and a user message naming that task. This is delegation between model invocations owned by one coroutine, not independently scheduled worker processes (SRC-1, `client/agent.py`; [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history), [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance)).

### Tool work and the return handoff

The executor receives the advertised tool schemas and either returns nonempty text or emits calls. Python treats nonempty content as task completion before checking calls. Otherwise it decodes each call's arguments, looks up the named MCP session and awaits the tool. The server receives the tool name and arguments, not the whole planner conversation. The executor receives stringified MCP content in a task-local tool message correlated with the call ID. It may make further calls before returning text. The task loop has no iteration bound; an empty reply with neither content nor calls does not advance it (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)).

Only the executor's final task text is appended as a task result to shared history. The raw tool conversation stays task-local. Later tasks and the next planner invocation therefore receive an executor-mediated account, not independent access to every tool response. Executor context trimming can also remove older messages. These transformations limit what later model decisions can verify; delivery of a result summary does not establish that it faithfully represents the underlying tool output (SRC-1, `client/agent.py`; [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history)).

### Verification, rejection and recovery

After every task in a plan finishes, Python rebuilds the planner input from shared history. The planner is asked to decide whether the answer is complete and otherwise supply remaining work. Despite the prompt saying the planner will receive a result after each task, the executable loop calls it again only after the entire plan has run. The result messages reach later executors sooner than they reach a new planner decision (SRC-1, `client/agent.py`).

>             planner_msgs = [{"role": "system", "content": META_SYSTEM_PROMPT}] + self.shared_history
>         return meta_content.strip()
> --- `client/agent.py`

The planner's completion judgment is model interpretation, not a semantic acceptance test. The driver checks a text prefix and JSON decoding; it does not consult a reference answer, independent critic or per-step human approver. The benchmark's separate answer judge belongs to another entry path and is not a gate on this workflow (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution), [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)).

One explicit failure path is malformed planner output. Parsing or extracting the `plan` field returns a planner-error string immediately, rather than retrying the plan or asking the model to repair it:

>             try:
>                 tasks = json.loads(_strip_fences(meta_content))["plan"]
>             except Exception as e:
>                 return f"[planner error] {e}: {meta_content}"
> --- `client/agent.py`

This catches decoding and plan-field extraction errors, not every malformed task shape: subsequent iteration and task-key access occur outside that handler. Malformed tool arguments, unknown tool names and MCP call exceptions likewise have no task-loop repair handler here. Provider calls separately retry up to three attempts with exponential waits. Cleanup closes acquired contexts after the main query block, but server connection precedes that block. Neither retry nor cleanup rolls back completed tool effects. A planner can request more work after receiving task results, but that afforded recovery is not evidence of reliable correction or compensating actions (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)).

### Delivery and its limits

A planner reply beginning with `FINAL ANSWER:` returns the stripped suffix. At most three planner cycles occur; exhaustion instead returns the last planner text, which may still be a plan. This outer bound does not bound tasks, inner executor iterations or external latency. The CLI prints every normally returned string under the same final-answer label, including a planner-error string or exhausted plan:

> async def run_single_query(client: HierarchicalClient, question: str, file_path: str):
>     answer = await client.process_query(question, file_path, str(uuid.uuid4()))
>     print("\nFINAL ANSWER:", answer)
> --- `client/agent.py`

Thus delivered means returned to the caller and printed, not independently accepted as correct or complete. A propagated exception prevents this normal print path. Ordinary history is current-query state and is reset for the next query; this selected workflow does not itself admit its plan as a durable case. Durable case admission and retriever training remain separate shipped workflows, not hidden delivery requirements for the interactive path (SRC-1, `client/agent.py`; [RT-RTE-query-execution](runtime.md#rt-rte-query-execution), [RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)).

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

#### On [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)

- Workflow selection: The ordinary shipped CLI path joins intake, serial delegation, tool-result handoff, replanning and printed delivery without borrowing the benchmark's judge.
- Delegation boundary: The planner proposes tasks; Python orders execution; the executor proposes tool calls or task completion; registered MCP sessions perform calls. The handoff to the next planner occurs after all tasks in the current plan.
- Verification boundary: Parsing and prefix checks govern progression. Model completion judgment has no independent answer oracle on this entry path.
- Recovery boundary: Provider retries and session cleanup are implemented; malformed plan parsing returns error text without repair, while task/tool exceptions can escape. A replacement plan can request additional work but does not undo prior effects.
- Delivery boundary: Normal return is printed even when it is error text or an exhausted plan. Completion and correctness are not guaranteed by that label.
