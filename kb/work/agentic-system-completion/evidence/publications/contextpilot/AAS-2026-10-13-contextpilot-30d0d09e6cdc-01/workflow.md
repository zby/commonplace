---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ContextPilot workflow account: the shipped FSM document-QA path from sample handoff through retention, cleanup, review and saved prediction."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is one evaluation sample processed by the shipped FSM inference path, [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference). It was selected because the evaluation launcher chooses it and its connected implementation covers request intake, evidence search, retained findings, prompt cleanup, review and answer recording. This is a single policy coordinating local tools under a software state machine, not a delegation tree of independently prompted agents. The ordinary inference and training routes are alternatives, not stages joined onto this workflow (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/contextpilot_fsm.py`; [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)).

All findings concern implementation or shipped doctrine at the revision in [boundary](boundary.md). No execution, answer correctness or successful recovery is observed. Additional workflow inspection covers state/tool selection, transitions, API-failure handling and termination in `infer/src/contextpilot_fsm.py`; sample construction and output writes in `infer/src/hf_test_runner.py`; and logger serialization and answer extraction in `infer/src/contextpilot.py`, all SRC-1. Those inspected passages extend coverage within the registered source, not its evidence layers.

### Request, planning and retrieval handoffs

The runner converts a dataset sample into document, question, reference answer and metadata, constructs a fresh agent with endpoint, prompt, tools and sampling configuration, applies caller controls, then calls `run(question, ...)`. The reference answer is handed to the result logger after inference; it is not an ordinary policy input. Retry-with-hint is a distinct feedback mode: a prior wrong answer and its attributed incorrectness can be supplied to the fresh agent, without reloading the previous agent's findings (SRC-1, `infer/src/hf_test_runner.py`; [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference)).

The model proposes semantic choices; the FSM owns which choices are legal next. With the default configured capabilities, successful analysis leads to planning, indexing and search; the optional embedding state is skipped when its tool is unavailable. A successful nonempty search supplies candidate chunks, resets the cycle's read bookkeeping and requires another plan before reading. The `plan` action is the same policy submitting strategy text, not an independent planner executing a delegated assignment. Search and chunk reads are local tool calls; the model receives their rendered results, while the external policy service does not receive the entire unrendered Python state (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`; [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference)).

### Evidence retention and cleanup

The FSM's readiness test is structural, not a factual verdict. It compares distinct chunk IDs read in the cycle against the smaller of two and the available-candidate count, and limits ordinary read calls per cycle. Once this threshold is met, it exposes finding-write/update actions. This establishes an evidence-access prerequisite, not that the chunks answer the question or that the saved text faithfully represents them (SRC-1, `infer/src/contextpilot_fsm.py`).

> evidence_ready = len(self._read_chunk_ids_this_cycle) >= min_read_chunks
> --- `infer/src/contextpilot_fsm.py`

> if evidence_ready:
>     names.update({"memorize", "updateMemory", "note", "updateNote"})
> --- `infer/src/contextpilot_fsm.py`

The foreground policy supplies finding content and keys; software dispatch and store methods admit the writes without a human approving each finding. A successful write resets the applicable review-satisfied flag. The FSM then requires cleanup of the cycle's read-result messages and deletion of the finding-write assistant message. When accumulated counts warrant it, search-result cleanup and plan-message cleanup intervene first. Legal cleanup targets are tracked message IDs, not arbitrary claims selected by a critic. The state machine waits for successful operations before advancing (SRC-1, `infer/src/contextpilot_fsm.py`; [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-context-control](runtime.md#rt-rte-context-control)).

This ordering moves evidence into saved findings before removing bulky history from the model-visible view. Deletion, truncation, summarization or compression changes later prompt construction; originals can remain in host history. Subsequent calls receive available finding summaries, and explicit keyed reads return selected stored content. This is in-task read-back, not established cross-session memory durability. The default tool schema does not grant the implemented restore capability, so retaining an original in Python does not imply that the policy can restore it through the default grant (SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`; [RT-OBJ-full-history](runtime.md#rt-obj-full-history), [RT-RTE-context-control](runtime.md#rt-rte-context-control)).

### Review, acceptance and recovery

After cleanup, the next review state first requires a note read if notes were written and still exist, then a memory load if memories were written and still exist. One error-free read of the relevant type satisfies that type's gate. This does not require reading every stored key, validating the finding against the original document, or demonstrating its use in the answer. Once in optional review, the policy may search again, read more evidence or submit `finish` (SRC-1, `infer/src/contextpilot_fsm.py`).

> elif old == FSMState.S6_REQUIRE_READ_NOTE:
>     if tool_name == "readNote" and "error" not in result:
>         self._note_review_satisfied = True
>         self._fsm_state = self._next_review_state()
> --- `infer/src/contextpilot_fsm.py`

Rejection is local protocol enforcement: a wrong-state tool is rejected before ordinary execution, and invalid keys or message IDs can cause errors or correction attempts. The provider's required-tool request alone does not enforce this. Conversely, empty state/tool matches fall back to the configured full tool set; ordinary inference bypasses the FSM schedule. Therefore the sequence is not a universal invariant across configurations or entry points (SRC-1, `infer/src/contextpilot_fsm.py`; [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating)).

A concrete recovery path handles provider failure during mandatory review. The runtime, not a separate recovery agent, selects the latest available key, executes the required store read directly, appends a synthetic assistant call and tool result, and invokes the transition handler. If the store is empty, it advances to optional review. This can repair protocol progress without model participation in the read selection; it cannot establish semantic review or correct answering (SRC-1, `infer/src/contextpilot_fsm.py`).

> key = str(list(mandatory_store.keys())[-1])
> auto_params = {"key": key}
> auto_result = self._execute_tool(mandatory_action, auto_params)
> --- `infer/src/contextpilot_fsm.py`

Other bounded exits prevent treating this sequence as guaranteed completion. Repeated empty searches can switch directly to best-effort optional review. Repeated no-tool responses can trigger a deterministic top-ranked chunk read, context deletion, finish-only requests or eventual termination, depending on the state. Consecutive tool errors can terminate the loop. Provider failure outside recoverable review can return an error-bearing history after clearing the current document. These are inspected branches, not observed recoveries (SRC-1, `infer/src/contextpilot_fsm.py`; [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference)).

### What counts as delivered

There are two distinct boundaries: protocol completion and caller-side recording. A successful `finish` produces a `final_answer` tool result, marks the FSM done and stops the loop; normal exit clears the current document and returns a constructed API payload. No independent answer-correctness veto precedes this exit. Human configuration and downstream evaluation are not per-answer approval gates (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`; [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference)).

The runner then records a final-result JSON, an inference trace containing history and snapshots, and a flushed JSONL prediction. The runner catches exceptions from `agent.run` and still attempts those recording steps. Recording can therefore represent failure rather than protocol completion (SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`).

Crucially, the runner uses `ExecLogger.save_final_result` to obtain its prediction. That method scans tool messages for a truthy `final_answer`, otherwise saving the literal failure placeholder below. The agent's separate `_extract_final_answer` can fall back to assistant prose, but that is not the JSONL answer-selection method at this handoff. This limits the runtime account's extraction-fallback discussion: it must not be read as establishing assistant-prose fallback in the runner's saved prediction (SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`).

> if not final_answer:
>     final_answer = "No final answer found."
> --- `infer/src/contextpilot.py`

> res_file, final_answer = logger.save_final_result(agent, question, correct_ans, meta_info)
> --- `infer/src/hf_test_runner.py`

Thus delivery in this workflow means the caller has written the selected answer or failure placeholder and associated artifacts. It does not mean an evaluator accepted the answer, that a successful `finish` necessarily occurred, or that recovery preserved sufficient evidence. File-writing failures themselves are not converted into a stronger durable-delivery guarantee by the inspected code.

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

#### On [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference)

Workflow-specific verification: read-count readiness, legal action checks, cleanup-target checks and keyed store reads govern progression. They do not independently judge evidence sufficiency or final-answer correctness. The normal cleanup-to-review handoff requires one successful read per applicable saved-content type, not exhaustive review of each key.

Workflow-specific recovery: code may substitute a deterministic latest-key read after provider failure in mandatory review; repeated empty searches and other failure exits qualify the normal sequence. There is no independent helper-agent return to integrate.

Workflow-specific delivery: distinguish the agent's payload return and internal answer helper from the runner's `ExecLogger.save_final_result` selection and subsequent artifact writes. In the runner path, missing tool-result answers become `No final answer found.`, not an assistant-prose fallback. The source passages and evidence limits are retained in the workflow account above (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`).
