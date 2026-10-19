---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Autogenesis workflow account: Gateway task submission, actor delegation, optional verification, corrective rounds and final delivery."
run-id: AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped Gateway → MetaAgent → actor → MetaAgent → Gateway task path. It is representative because it serves ordinary substantial user requests without requiring a generated capability or a precompiled Workflow. The account traces its source-supported sequence, not a particular successful task. Actor execution, verification and correction are conditional model choices; they are not a mandatory fixed pipeline. The capitalized source term Workflow denotes a separate reusable-program mechanism, covered in [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution), not a prerequisite for the path selected here.

Evidence is SRC-1 at the revision fixed in [boundary.md](boundary.md). Inspected implementation for this account: `autogenesis/gateway/service.py` task submission and execution; `autogenesis/protocol/server.py` delegation/escalation; `autogenesis/agent/types.py` capability dispatch, background action completion, round completion, conclusion and preparation; `autogenesis/agent/actor/meta_agent.py` orchestration seams and guards. Inspected doctrine/design: `autogenesis/prompt/default/meta_agent.html`, especially context rules and response protocol. These reads extend or confirm the baseline's coverage within SRC-1; no additional source, execution trace or experiment is introduced. None of the target's code or tests was executed. The source therefore establishes responsibilities and available paths, not successful decomposition, verification or recovery in operation.

### 1. Admit the request and assign its execution context

A Gateway client supplies task content, session and optional files/conversation. Submission rejects empty content and files whose resolved paths fall outside the session workspace. It binds session roots, resolves or creates a conversation, submits a queued user task, updates session/conversation records and publishes submission. The immediate return contains task and conversation IDs, not the finished deliverable. SRC-1: `autogenesis/gateway/service.py`.

The queued handler then binds runtime roots and synchronizes grants, uses the conversation ID for the agent context when available, publishes start, and invokes `meta_agent` with task content, files, capabilities and public task ID. Conversation identity scopes memory and budgets; session workspace resources remain shared. This is the entry portion of [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), not a new route identity.

### 2. Choose and delegate substantial work

The prompt asks MetaAgent first to decide whether any orchestration is necessary. Directly answerable tasks should finish immediately. For substantial repository work it instead requires an initial actor delegation, normally `code_agent` for implementation or `general_agent` for analysis. This requirement is natural-language guidance to the model, not an independently enforced actor-first gate. SRC-1: `autogenesis/prompt/default/meta_agent.html`.

> - ONCE you have decided the task needs real work on the repository, your first execution
>   action MUST dispatch an actor sub-agent (`code_agent` for implementation, `general_agent`
>   for analysis/research). Direct tools are limited to one atomic lookup or control
>   operation; they are not a replacement for delegating the task. This rule governs HOW to
>   do work that is needed — it does not make work needed.
> --- `autogenesis/prompt/default/meta_agent.html`

MetaAgent exposes registered agents as callable capabilities. The foreground model chooses their names, tasks, files and optional allowlists; code performs the dispatch. Calls in one action batch run concurrently, while dependent work must wait for a later model turn. There is no separate plan scheduler enforcing a complete decomposition. [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) supplies the loop and concurrency evidence; [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) supplies the handoff evidence.

At delegation, protocol code creates a new child context ID linked to the parent's runtime ref. It supplies the explicit task, existing file paths, optional target and effective capability lists. It does not pass the parent's complete conversation. The actor owns its own model/tool loop. This keeps child reasoning and intermediate action history out of the foreground window, but does not isolate shared filesystem effects. The returned parent action value is the successful child's message, not its full Response data or trace. SRC-1: `autogenesis/protocol/server.py`, `autogenesis/agent/types.py`; [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation).

### 3. Consume results and decide whether verification is needed

Each action posts its outcome back to the agent inbox. After a batch drains, code records action evidence, posts the step, copies errors into corrective context, increments the step and either advances or concludes. The next MetaAgent decision can therefore depend on completed results and blockers. This machinery does not itself decide that a deliverable satisfies the task. SRC-1: `autogenesis/agent/types.py`; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution).

The prompt tells MetaAgent to compare a successful child result with remaining acceptance conditions and avoid redoing already-proven work. Verification is another model-selected delegation: for a substantial concrete unproven claim, dispatch a verifier; for a live UI, dispatch `browser_agent` with the exact deployed URL and a concrete interaction script, then use browser evidence in review. A final `reviewer_agent` round is strongly recommended for substantial deliverables. These are supplied instructions, not evidence that a browser or reviewer actually ran. SRC-1: `autogenesis/prompt/default/meta_agent.html`.

> **Review before finishing (strongly recommended).** For any substantial run (where a sub-task produced a real deliverable), before you call `done_tool` you SHOULD dispatch `reviewer_agent` in a final round to verify the work hands-on (for a UI deliverable, run `browser_agent` first so the reviewer has browser evidence). Act on its verdict — if it finds the task incomplete or defective, keep working (fix defects, or evolve the missing capability) and only then finish; if it passes, call `done_tool`. Skip the review only for trivial Q&A with no real deliverable.
> --- `autogenesis/prompt/default/meta_agent.html`

The user supplies the objective and any acceptance conditions; MetaAgent proposes verification tasks and interprets returned messages. A reviewer can report defects, but no reviewer verdict is consumed as a hard completion veto in the inspected terminal path. Generic model judgment is not a reference-answer oracle. Task-specific commands or browser observations could provide evidence if actually performed; none is supplied here. The workflow remains open-request driven rather than a fixed benchmark curriculum.

### 4. Recover from rejection, blockage or repeated work

A child Response with `success=false` is rejected by parent dispatch as an exception rather than accepted as a successful action. Background action handling packages errors for the round; the next foreground turn can change strategy, delegate corrective work or finish partially. SRC-1: `autogenesis/agent/types.py`.

> if not resp.success:
>     raise RuntimeError(resp.message or f"Sub-agent {route[1]!r} failed")
> --- `autogenesis/agent/types.py`

A reported deliverable defect is different: the prompt asks MetaAgent to decide whether the same actor can fix it with existing capabilities. The default is another corrective actor task. Capability evolution is requested only for missing means or recurring structural failure, not every weak attempt. That optional branch is already established by [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission); this account does not claim it occurred or that evaluator approval is mandatory admission.

A blocked child can escalate through the parent-ref link. Protocol code sends the typed escalation and waits up to 300 seconds; missing parent or timeout returns graceful-stop guidance. MetaAgent's focused model turn extracts a matching `reply_tool` argument and resumes the waiter without dispatching arbitrary new work in that special turn. Recovery ownership is split: protocol code owns rendezvous/timeout, the parent model supplies guidance, and the child must act on the returned text. No successful unblock is observed. SRC-1: `autogenesis/protocol/server.py`, `autogenesis/agent/actor/meta_agent.py`; [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation).

Two inspected guards also constrain recovery. The base Agent consults `no_progress_hook`; after three blocked no-progress proposals it concludes with `done=False`. MetaAgent additionally detects identical serialized action batches after the base guard permits them: it skips the first repetition with corrective feedback, and a further repetition concludes explicitly incomplete but sets `run.done=True`. These are distinct branches, not an unconditional promise that every repeated call executes three times. Neither branch undoes existing filesystem or external effects. SRC-1: `autogenesis/agent/types.py`, `autogenesis/agent/actor/meta_agent.py`.

### 5. Deliver a result without mistaking lifecycle completion for correctness

Normally MetaAgent synthesizes the child results in a `done_tool` call. Dispatch recognizes that tool as the completion signal; after round completion, conclusion cancels stragglers, emits stop hooks, builds/finalizes a Response, resolves the caller's pending reply and removes run state. The Response's message is the final result. The Gateway publishes the serialized Response in `task.completed` whenever the awaited agent call returns normally. It emits `task.failed` for a raised exception and `task.cancelled` for cancellation. SRC-1: `autogenesis/agent/types.py`, `autogenesis/gateway/service.py`; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution).

> response = await agent_task
> payload = response.model_dump(mode="json") if hasattr(response, "model_dump") else {"result": str(response)}
> await self._publish("task.completed", payload, session_id=session_id,
>                     conversation_id=conversation_id, task_id=record.task.id)
> --- `autogenesis/gateway/service.py`

Delivery here means the result has reached the Gateway event channel and returned to its task handler, not that a user received, accepted or independently verified it. The baseline's success calculation and MetaAgent's explicitly incomplete terminal branch prevent treating either Response success or the completion-event name as proof of goal satisfaction. The prompt also describes a fallback concatenation of results; the inspected base loop instead nudges text-only turns, so that doctrine sentence is not used to establish an alternative delivery mechanism. SRC-1: `autogenesis/prompt/default/meta_agent.html`; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution).

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

#### On [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)

Workflow-specific verification role: MetaAgent decides when a remaining concrete claim requires a verifier and whether to accept a returned review. The prompt's browser checks and strongly recommended final review supply a requested verification policy, not a mandatory gate before completion. Corrective ownership remains with the foreground model through subsequent dispatches; errors can also produce partial delivery. Gateway event completion records normal return, not a separate acceptance judgment. Source passages and implementation anchors appear in the workflow account above.

#### On [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

Workflow-specific handoff consequence: each corrective or verification delegation must carry a self-contained task and the relevant files or deployed URL; earlier actor history does not automatically accompany it. The prompt explicitly requests the exact deployed URL for browser verification. Escalation is the distinct bounded waiting path for a blocked child, not a new full-context handoff. No observed trace establishes that a selected verifier received sufficient evidence or that its criticism changed the next round.
