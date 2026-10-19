---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ContextPilot workflow account: shipped FSM document QA through evidence retention, cleanup, review, rejection recovery and result delivery."
run-id: AAS-2026-10-19-contextpilot-0826e2df5b2f-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot workflow report

## Workflow account

The representative workflow is the evaluation script's FSM document-QA path, [RT-RTE-document-qa](runtime.md#rt-rte-document-qa). It was selected because it connects the shipped request driver, model/tool decisions, evidence retention, context cleanup and artifact writers. It is not a composite of the separate training and inference controllers. The frozen source and exclusions are those in [boundary](boundary.md). Additional inspection in this member covers FSM transition, rejection and retry bodies and the runner's post-run artifact handoff. These are implementation passages from SRC-1, not observed execution; no successful answer, relevant review or reliability result is established (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/hf_test_runner.py`).

### Request and handoffs

An operator selects the model, dataset and limits; the evaluation worker selects a sample and constructs a fresh agent. The worker hands the question to `run`, with the supplied document available through the agent's document manager. The reference answer is reserved for the result/scoring side in ordinary mode; the supported retry mode can supply incorrect-answer feedback. The policy service receives rebuilt history, the question with saved-entry inventory, and currently offered tool schemas. These are service handoffs, not delegation to an independent planner or autonomous search agent. Python owns subsequent invocations and local tool dispatch; the model authors plans, retrieval queries, store content and the final answer ([RT-RTE-document-qa](runtime.md#rt-rte-document-qa), SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

The ordinary configured progression analyzes the document, accepts a nonempty plan, builds the index, searches, plans over results, and reads chunks. Optional embedding construction and post-read planning depend on configuration. A successful search supplies retrieved chunks and resets the cycle's read bookkeeping. Successful reads register tool-message IDs and the chunk IDs already read. Thus the handoff from retrieval to reading carries concrete candidates and controller bookkeeping, not just a free-form report. Each applicable transition checks the tool result; for example (SRC-1, `infer/src/contextpilot_fsm.py`):

> elif old == FSMState.S2_5_PENDING_PLAN:
>     if tool_name == "plan" and "error" not in result:
>         self._fsm_state = FSMState.S3_SEARCHED
> --- `infer/src/contextpilot_fsm.py`

### Retention, cleanup and review

After reading, the model can continue reading, edit read context, or save/update a note or memory. A successful save marks the relevant store as needing review and captures the read-result IDs and invoking assistant ID as cleanup targets. Accumulated search/plan counts can require earlier search-result or plan cleanup first. Read-result cleanup then proceeds until its target set is empty; deletion of the save invocation leads to the next required review state. This wiring makes retained content available before raw evidence is removed from later payloads. It does not verify that the saved content adequately replaces that evidence (SRC-1, `infer/src/contextpilot_fsm.py`; [RT-RTE-context-edit](runtime.md#rt-rte-context-edit)).

Successful `readNote` or `loadMemory` marks the respective review requirement satisfied. Review can return to search or reading, starting another evidence cycle, or proceed to `finish`. A successful read is a protocol event, not proof that the model understood or checked the entry. The model receives transformed history rather than every original message; full history and saved entries can remain reachable behind masks. The context mechanism therefore differs from an isolated subagent frame whose entire intermediate history is discarded on return ([RT-OBJ-context-masks](runtime.md#rt-obj-context-masks), [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls), SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`).

### Rejection and recovery

The controller can reject an action outside the computed allowed set before execution, reject store keys or cleanup IDs, and convert execution exceptions into tool errors. These checks concern protocol and object validity, not answer correctness. On ordinary non-ID tool errors it queues the failed assistant/tool pair as pending error context, rather than retaining it in normal history/snapshots, and lets the model try again. At the configured consecutive-error limit it records the failure and exits. Recovery ownership is therefore split: Python selects the retry/termination mechanism; the model usually proposes the replacement action (SRC-1, `infer/src/contextpilot_fsm.py`).

> self._pending_error_messages.append(assistant_entry)
> self._pending_error_messages.append(tool_entry)
> self.ctx_counter -= 2
> print(f"    [FSM] Error result NOT recorded in full_history/snapshots.")
> --- `infer/src/contextpilot_fsm.py`

Recovery can weaken the ordinary review story. Repeated empty searches jump to best-effort review without a successful evidence cycle. An invalid optional store/restore request in S7 switches to finish-only mode rather than demanding repair of that request. API failure during mandatory review can trigger deterministic store reads; that is delivery by code, not demonstrated model review. An unmatched configured schema falls back to the full tool set, and the supported non-FSM caller does not enforce the FSM sequence. Consequently, this workflow's order is conditional, not a guarantee for every supported invocation ([RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls), [RT-RTE-base-inference](runtime.md#rt-rte-base-inference), SRC-1, `infer/src/contextpilot_fsm.py`).

### Completion and delivered result

On successful `finish`, the controller records its tool result, marks DONE and leaves the loop. `run` returns a rebuilt payload, not the answer string. The worker separately asks the logger to extract/write the final result, writes the inference artifact, and creates the sample's JSONL record. The final result handoff explicitly includes the reference answer, outside ordinary model inference (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/hf_test_runner.py`):

> res_file, final_answer = logger.save_final_result(agent, question, correct_ans, meta_info)
> --- `infer/src/hf_test_runner.py`

There are therefore two completion criteria: protocol completion through `finish`, and driver delivery through result artifacts. They need not coincide. The worker catches an exception from `run` and still enters artifact writing; answer extraction can fall back to assistant prose after an incomplete run. Artifact presence alone does not establish successful FSM completion or a correct answer. Normal/handled cleanup clears the document index, while resume skips recorded sample IDs rather than reconstructing their agent memories. Actual writes, cleanup success and answer quality remain unobserved ([RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls), SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`).

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

#### On [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)

Workflow role: representative request-to-delivery route. The consequential checkpoints are tool-result-dependent advancement, retention before cleanup, store-review events and final artifact extraction. Verification accepts protocol events, not semantic correctness. Recovery may retry, synthesize a mechanical operation, force best-effort finishing or terminate; driver delivery can still occur after an incomplete agent run. The workflow account above establishes these additional handoff details from SRC-1, `infer/src/contextpilot_fsm.py` and `infer/src/hf_test_runner.py`, without changing this route's identity or its uninspected operation status.
