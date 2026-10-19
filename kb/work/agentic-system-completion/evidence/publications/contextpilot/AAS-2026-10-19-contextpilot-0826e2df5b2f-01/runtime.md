---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ContextPilot runtime baseline: FSM document QA, context editing, alternate caller and reward-driven training at the frozen revision."
run-id: AAS-2026-10-19-contextpilot-0826e2df5b2f-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot runtime report

## Runtime account

ContextPilot ships a model-directed document-QA loop and a separate reinforcement-learning plane. The ordinary evaluation script selects the finite-state controller (FSM); it is not the only supported caller. The controller decides which tool names can execute, while the model supplies queries, plans, memory content and the answer. Context editing changes later model input without necessarily deleting the underlying history. Training credits intermediate snapshots using descendant answers and sends selected, scored trajectories to actor updates. These are implementation findings, not observed operation or demonstrated benefit (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/contextpilot_fsm.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/ppo/ray_trainer.py`).

The evidence boundary and source identity are those of [boundary](boundary.md). All source citations below are SRC-1 at that member's frozen commit. Added implementation inspection covers the detailed FSM dispatch/recovery paths, base-class invocation, context transformations and output extraction; training state cloning, tool dispatch, terminal scoring, snapshot credit and actor-update/checkpoint consumers. No target, test, example, model or service was executed. There are no supplied observed-run or causal-experiment sources. Exact weights, deployed permissions, benchmark outcomes and operational reliability remain unobserved.

### Ordinary shipped invocation

The trigger is an operator launching an evaluation task with model/tokenizer and dataset configuration. `eval_task.sh` supplies dataset-specific adapters, the maintenance prompt and tool schema, default queue scheduling and `--version fsm`. Workers claim independent sample indices (or use stride scheduling), derive a stable sample ID, skip completed IDs when resume is enabled, extract document/question/reference, and construct a **fresh agent per sample**. The reference answer goes to result/scoring artifacts, not to the ordinary `agent.run(question, ...)` call. A retry mode can supply a previous wrong answer and its incorrectness, so oracle isolation is mode-specific, not universal. See [RT-RTE-document-qa](#rt-rte-document-qa) (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`).

The model client uses an OpenAI-compatible endpoint, optional rank-based endpoint selection and configurable model ID. The initial prompt describes the task; the original question receives an appended inventory of memory/note keys and summaries. Each turn reconstructs the model payload from history and edit masks. The FSM progresses through analysis, optional plan, indexing, optional embedding construction, search, post-search plan, reading, saving, cleanup, review and finish. Exact progression depends on configured tools, successful results and counters; an empty-search threshold can jump to best-effort review. `plan` does not call an independent planner: it validates a nonempty model-authored `strategy` and returns success (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

The Python controller owns the next invocation and effect boundary. Model output is parsed into one action and arguments; the FSM keeps only the first of multiple native tool calls. It rejects a name outside the current allowed set before local execution, validates selected context IDs and store keys, catches tool exceptions, records successful calls/results and advances state. Search reads the supplied document index through external Elasticsearch; optional semantic/hybrid alternatives involve embedding/reranking services. A model-directed call is not arbitrary shell or a provider-executed tool: local Python dispatch owns the inspected effects. The deployed OS/container/network isolation of that Python process is not established (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

The working context is deliberately non-monotonic. Model-selected edits target messages; deterministic cleanup and token-window rules can remove material without a fresh model choice. Original history stays in process while model input substitutes stubs, selected text or summaries; saved memory summaries remain visible and full entries can be read later. This resembles retaining a backing store with a filtered view, not a stack frame that destroys the original content. Context IDs have explicit restore semantics only where marked restorable; they are not automatically dereferenced pointers. See [RT-RTE-context-edit](#rt-rte-context-edit) and [RT-OBJ-context-masks](#rt-obj-context-masks). Memory-content revision details are left to the memory analyst (SRC-1, `infer/src/contextpilot.py`).

Finish yields a `final_answer` tool result. The returned value of `run` is a rebuilt payload, **not** the answer string. The logger extracts an answer from history, writes final/result artifacts and the driver writes one JSONL record with sample ID, answer, reference and metadata. Normal completion clears the document index. Resume means skipping recorded sample IDs, not reconstructing their agent memory. Output extraction can fall back to undeleted assistant prose after an incomplete run; an output answer alone therefore does not establish successful `finish` or compliance with the review protocol (SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`).

### Controls and selected forcing cases

Four forcing cases materially qualify the ordinary path:

1. **Supported base-class caller.** The runner defaults to `version="v4"` and imports `ContextPilot` for non-FSM versions. Its dispatch checks configured names, not FSM state or the currently offered subset. A configured `finish` can execute without the FSM's review sequence. This is a supported alternate implementation path, not a hypothetical provider exploit: [RT-RTE-base-inference](#rt-rte-base-inference) (SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`).
2. **Incomplete configuration and emergency progression.** FSM tool filtering returns the full configured set when its filtered set is empty. The consumer then treats that full set as allowed. Thus state restriction is conditional on a matching configured tool; it is not a universal invariant over custom tool schemas. The empty-search path also permits review without a successful evidence cycle. Search-count force-finish is delayed until S7, rather than an exact hard cap on all search calls (SRC-1, `infer/src/contextpilot_fsm.py`).
3. **Overflow and API failure.** Token-window pruning exhausts eligible turns and can still return an oversized payload; its name is not a hard fit guarantee. API overflow recovery attempts further deletion. In mandatory-review states, an exhausted API retry can deterministically read the newest saved key, record the synthetic call and transition. That establishes store delivery to the next context if it runs, not relevant review by the model. Other API failures can return early; repeated no-tool/tool errors can terminate without an answer. See [RT-CLM-fsm-controls](#rt-clm-fsm-controls) (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`).
4. **Training and partial branches.** Training has a different asynchronous state machine and tool registry, not the inference FSM. Branches clone histories, memory dictionaries and edit state; their document managers can share a document ID with nonownership flags. Their outcomes feed scalar credit rather than becoming subagent prose injected into a foreground QA answer. Training therefore cannot inherit the inference FSM's review guarantee or be described as fully independent backend isolation: [RT-RTE-training-rollout](#rt-rte-training-rollout) (SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

The capability surface is configurable tool schemas plus implemented Python handlers and remote model/retrieval requests. The current grant set is the configured schema filtered by the active controller, except for the documented fallbacks above. The isolation envelope is an external deployment responsibility: inspected source does not establish sandboxed tool execution. No claim is made about all possible host callbacks, extension classes or bundled verl framework routes. Deprecated graph arguments are ignored by the inspected inference constructor; they do not establish live graph delegation (SRC-1, `infer/src/contextpilot.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

### Change admission and improvement plane

Within QA, the model proposes retained facts/summaries and the software admits keyed writes without per-content human approval. Those writes affect later context; semantic truth is not checked by successful admission. Model proposals also replace selected context views. These are knowledge/context changes, not product-code installation (SRC-1, `infer/src/contextpilot.py`).

The training launcher selects a bounded LongBench-v2 curriculum, actor checkpoint, tool configuration, fixed prompt, snapshot budget and reward function. Training's internal state machine generates tool calls, records context-management/retrieval boundaries, and returns snapshots/terminals plus branch points. Worker reward assignment computes terminal outcomes before downsampling and credits snapshots with the mean of descendant terminal rewards; snapshots lacking terminal descendants are dropped. The estimator normalizes scores by query UID; the trainer computes advantages, updates actor parameters and periodically validates/saves. Validation metrics are not an inspected admission veto before each actor update. The saved model and dataloader state permit subsequent resume; checkpoint retention can limit rollback history. See [RT-RTE-actor-update](#rt-rte-actor-update) and [RT-CMP-actor-model](#rt-cmp-actor-model) (SRC-1, `train/sh/run_qwen3-8b_longbenchv2.sh`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`).

This is a wired reward-responsive parameter-update pathway. It is not evidence of improved capacity, exercised self-improvement or theory criticism. The independent objective is QA correctness subject to format/budget penalties. Reference answers supply an oracle in training; a model judge is used for open-ended comparison, while MCQ uses a fixed match rule. Formulated maintenance instructions persist as static guidance; the inspected update changes parameters, not those instructions. Lower-level optimizer implementation, rollout-weight synchronization, model export and deployment selection were not traced here, preventing a complete claim that a particular trained successor reached inference production (SRC-1, `train/verl/utils/reward_score/statelm_qa.py`, `train/verl/trainer/ppo/ray_trainer.py`).

## Shared records

### Components

#### RT-CMP-actor-model
Label: ContextPilot actor model

The QA policy is distributed-parametric model state supplied through the configurable inference model/endpoint and training `actor_rollout_ref.model.path`. Storage is external inference service/GPU state and, for training, checkpoint files. Inference code requests generations but contains no per-turn parameter update; training explicitly invokes actor updates. Exact weight versions are not frozen by SRC-1: a path/model ID is not a digest. A mutable inference endpoint can resolve to another model; provider internals and actual deployment version are uninspected. The training checkpoint is mutable across steps; lower-level synchronization to rollout workers is not established by this record (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`, `train/verl/trainer/ppo/ray_trainer.py`).

> resp = self.vllm_client.chat.completions.create(**body_kwargs)
> --- `infer/src/contextpilot_fsm.py`

> actor_output = self.actor_rollout_wg.update_actor(batch)
> --- `train/verl/trainer/ppo/ray_trainer.py`

#### RT-CMP-judge-model
Label: Open-ended answer judge

Distributed-parametric comparison service, addressed through `OPENAI_MODEL` and an OpenAI endpoint in training scoring. Parameters are not changed by the inspected scorer; exact weights are not pinned, and a mutable endpoint may resolve differently. Internals, executed judgments and their reliability are uninspected. Ground truth is an input to judgment, not produced by the judge. MCQ uses symbolic matching instead (SRC-1, `train/verl/utils/reward_score/statelm_qa.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`).

> is_correct = has_valid_finish_tool_call and llm_judge_answer(predicted, ground_truth, question)
> --- `train/verl/utils/reward_score/statelm_qa.py`

#### RT-CMP-compression-model
Label: LLMLingua-2 compression endpoint

Optional distributed-parametric compressor invoked by `compressContext`, stored behind an OpenAI-compatible service addressed through a separate configuration file. The inspected request changes no weights; the exact version is not pinned and the endpoint can resolve to another implementation. The model label does not prove native LLMLingua-2 behavior: the caller sends a text-generation instruction to compress. Exceptions fall back to random word sampling. Provider internals and activation are uninspected (SRC-1, `infer/src/contextpilot.py`).

> "content": "Compress the user's text. Return only the compressed text, with no explanation.",
> --- `infer/src/contextpilot.py`

#### RT-CMP-embedding-provider
Label: Optional embedding provider

Optional distributed-parametric text-to-vector service used by semantic search and memory similarity indexing; vectors are numerical arrays cached in process. The inspected code does not train provider parameters. Exact provider weights are not pinned; model/endpoint configuration can resolve differently. Reranking is another optional numerical/model-service path; its version, internals and operation likewise remain external and unobserved. Neither is required by the ordinary BM25 configuration, and this record does not assert exhaustive coverage of their ranking behavior (SRC-1, `infer/src/contextpilot.py`).

### Operative objects

#### RT-OBJ-full-history
Label: Full history and snapshots

`full_history` and `snapshots` hold natural-language question, assistant content and tool-result text inside symbolic role/message/tool-call envelopes. The text is consumed by the policy model; role and ID fields are consumed by Python payload assembly. Substrate is per-agent Python lists/dictionaries, with JSON trajectory copies written by logging. The envelope is not itself learned knowledge. Stored snapshots reflect particular payload constructions, not independently authenticated provider receipts (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `infer/src/hf_test_runner.py`).

> "full_history": self._sanitize_for_json(self.full_history),
> --- `infer/src/contextpilot.py`

#### RT-OBJ-context-masks
Label: Context edit masks

Symbolic sets/maps `deleted_msg_ids`, `truncated_msg_ids`, `summarized_msg_ids`, `compressed_msg_ids` and `restorable_msg_ids` control how history appears in later payloads. They live in the agent process and can be serialized to trajectory JSON. Replacement strings are natural-language content; mask membership and precedence are fixed Python rules. Explicit restore clears edit entries only for authorized restorable IDs. Token-window stubbing does not itself add IDs to `restorable_msg_ids`, unlike explicit delete, so restoration coverage differs by producer (SRC-1, `infer/src/contextpilot.py`).

> if msg_id in self.deleted_msg_ids:
>     tool_replacement = STUB_MESSAGE
> elif msg_id in self.summarized_msg_ids:
>     tool_replacement = self.summarized_msg_ids[msg_id]
> elif msg_id in self.truncated_msg_ids:
>     tool_replacement = self.truncated_msg_ids[msg_id]
> --- `infer/src/contextpilot.py`

### Routes

#### RT-RTE-document-qa
Label: FSM document QA invocation

Endpoints: evaluation script/worker sample to model/tool iterations to result JSONL. Owner: worker and `ContextPilotFSM.run`; model proposes actions, Python gates and executes them. Context/state/effects: question, document index, per-sample history, FSM counters, note inventories and answer artifacts. Symbolic tool/state selection wraps natural-language decisions. Operating mode: open QA within a bounded benchmark driver. The ordinary run has no reference-answer oracle in its model input; the separate retry mode can supply a wrong answer plus correctness feedback. Humans select inputs/configuration and can interrupt; there is no per-tool approval prompt (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`, `infer/src/contextpilot_fsm.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rebuilt model payload; result extraction separately returns an answer string to the logger and writes per-sample artifacts.
- Later read-back: Model-written notes/summaries reach subsequent turn payloads; explicit readNote/loadMemory results can expose full entries. JSONL resume only skips completed IDs in the inspected caller.
- Delegated visibility: Configured model service receives the rebuilt payload and filtered schemas; Elasticsearch receives document indexing/search requests. This is service use, not a separate autonomous delegate.
- Selection predicate: Worker scheduling and sample ID select tasks; model chooses query/action/key inside the currently allowed schema; Python validates allowed names and selected parameters.
- Invalidation or expiry: Per-sample agent is recreated; document index cleanup runs on normal/handled exits. Interruptions or external service failure do not imply successful cleanup.
- Activation or effect: Successful tool calls mutate local state or retrieve evidence and shape later payloads; executed behavioral consequences and answer correctness are unobserved.
- Evidence limits: Source wiring only; no live services or benchmark payload execution. Custom schemas and non-FSM callers require the qualifications in RT-CLM-fsm-controls.

> --resume False --version fsm
> --- `infer/scripts/eval_task.sh`

> last_payload = agent.run(question, max_turns_to_fail=max_turns_to_fail)
> --- `infer/src/hf_test_runner.py`

> if action not in allowed_names:
> --- `infer/src/contextpilot_fsm.py`

Admission of within-trajectory knowledge: model supplies keys/content/summary; Python accepts new values or append/overwrite/delete operations, rejects missing keys/invalid modes where checked, and exposes inventories on the next payload. Guidance asks saving useful evidence and preserving qualifiers; it supplies no semantic truth gate. No per-content human veto or automatic semantic rollback is wired in these methods; a subsequent model update can overwrite/delete. Details and guarantees of memory-content revision remain for the memory analyst (SRC-1, `infer/src/contextpilot.py`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`).

> self.simple_notes[str(key)] = {"summary": str(summary), "full_content": str(content)}
> --- `infer/src/contextpilot.py`

#### RT-RTE-context-edit
Label: Context view editing and recovery

Endpoints: model cleanup request or code threshold to message masks to subsequent model payload. Owner: inference controller; model proposes explicit targets/replacement text, code validates roles/IDs and can independently choose oldest turns. Context effects include deletion stubs, span truncation, model-supplied summaries, optional compression and explicit restoration. This is current-run context management plus retained replacement content when reused in later invocations, not removal of the underlying history (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success/error with affected message ID and, for compression, fallback metadata; actual replacement appears when the payload is rebuilt.
- Later read-back: Replacement text or stubs persist across subsequent turn payloads; summaries and separately saved entries can survive removal of raw evidence from the visible window.
- Delegated visibility: Optional compressor receives selected message text; ordinary model sees the transformed payload, not all raw history. No subagent frame is created.
- Selection predicate: Model supplies msg_id plus span/summary/rate; FSM limits cleanup IDs in selected states. Token-window logic instead picks earliest eligible assistant/tool pairs; API overflow recovery targets reclaimable evidence.
- Invalidation or expiry: Explicit restore clears masks for restorable IDs; new masks can supersede a view by precedence. Process lifetime bounds in-memory state; automatic token-window deletion has no equivalent explicit restorable marking in that method.
- Activation or effect: Payload assembly substitutes content; the original remains in history. This wires altered context delivery, not successful preservation of meaning or improved answers.
- Evidence limits: Compression is lossy and fallback sampling is not semantic summarization. Token accounting can exhaust eligible messages without fitting. No measured context savings or quality effects were supplied.

Admission: model-authored summary or span is accepted after existence/role checks and FSM-specific ID validation, not a semantic review. Code admits masks directly; compressor errors admit sampled words rather than vetoing the edit. Guidance is the fixed cleanup workflow; rollback uses original history through explicit restore where authorized (SRC-1, `infer/src/contextpilot.py`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`).

> self.summarized_msg_ids[int(msg_id)] = summary
> --- `infer/src/contextpilot.py`

> sampled_indices = sorted(random.sample(range(len(words)), keep_count))
> --- `infer/src/contextpilot.py`

> if asst_idx is None:
>     print("[TOKEN_WINDOW] No more assistant turns available to stub.")
>     break
> --- `infer/src/contextpilot.py`

#### RT-RTE-base-inference
Label: Non-FSM inference path

Endpoints: runner's non-FSM version to `ContextPilot.run` to the same underlying tools and result writers. Owner: base Python loop. Model proposes all next actions; configured-name membership is the execution check. State-dependent review ordering is not inherited. Operating mode is the same QA driver with optional retry feedback, not a separate training oracle (SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rebuilt payload or early API-failure payload, with answer extracted separately from history.
- Later read-back: Same note inventories, explicit reads and context-mask substitutions as the shared base implementation; no cross-sample store reload was established.
- Delegated visibility: Same configured provider payload boundary as FSM inference, but without its state-dependent grant sequence.
- Selection predicate: Runner version selects class; base dispatch checks action against self.tool_names, rather than current_tools or FSM state.
- Invalidation or expiry: Fresh per-sample object and handled-exit document cleanup; no-tool retries remove the unsuccessful assistant/snapshot and re-prompt.
- Activation or effect: Configured tools can execute without FSM review ordering. A search limit activates a nudge, not an execution denial.
- Evidence limits: Reachable source branch, not demonstrated bypass execution; the exact configured tool set determines which actions are possible.

> if action not in self.tool_names:
>     result = {"error": f"Tool '{action}' not found."}
> --- `infer/src/contextpilot.py`

> self._search_limit_nudge_active = True
> --- `infer/src/contextpilot.py`

#### RT-RTE-training-rollout
Label: Training rollout and partial continuations

Endpoints: training sample/raw_prompt/document to asynchronous `AgentState` loop, tools and trajectory outputs/branch points. Owner: StateLM agent-loop implementation plus worker scheduler. Model proposes tool calls; registry lookup and tool handlers execute them. Code clones partial branches, scores their terminals and cleans up document state. Training uses the separate configured prompt and tool registry, not the inference FSM's gate. The model policy is [RT-CMP-actor-model](#rt-cmp-actor-model) (SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MultiTrajectoryAgentLoopOutput containing snapshots/terminals, branch points and retained agent state for worker use; branches return terminal-marked trajectories.
- Later read-back: Cloned memory/edit state enters descendant generations; selected snapshot outputs become training inputs in RT-RTE-actor-update.
- Delegated visibility: Branches copy model-visible history, memory and masks. They do not exchange free-form reports with a foreground agent; document backend identity can be shared while local mutable dictionaries are copied.
- Selection predicate: ContextPilot/partial-rollout configuration enables branching; context-management and retrieval boundaries supply snapshots; worker selects/downsamples outputs under configured budgets. Exact scheduler ranking behavior is not fully traced here.
- Invalidation or expiry: Branch cleanup closes managers with ownership-sensitive document clearing; errors attempt cleanup. Length/turn violations can terminate trajectories rather than expose a truncated observation.
- Activation or effect: Separate continuations yield terminal rewards for ancestor credit; no exercised branching, parallel speedup or quality benefit was observed.
- Evidence limits: Async loop and clone/return paths inspected; lower-level Ray scheduling, backend isolation and every tool's internal behavior are not established by this route.

Operating mode: bounded training/validation curriculum, with machine-generated continuations and dataset-provided answer oracle at reward time. Humans choose training data/model/budgets and launch the run, not individual branch contents. Scalar scoring admits credit, not theories or approved textual knowledge (SRC-1, `train/sh/run_qwen3-8b_longbenchv2.sh`, `train/verl/utils/reward_score/statelm_qa.py`).

> branch_data.memories = copy.deepcopy(agent_data.memories)
> branch_data.notes = branch_data.memories
> branch_data.simple_notes = copy.deepcopy(agent_data.simple_notes)
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

> cloned._doc_id = getattr(doc_state_manager, "_doc_id", None)
> cloned._owns_doc_id = False
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

#### RT-RTE-actor-update
Label: Snapshot credit and actor update admission

Endpoints: terminal/snapshot trajectories to reward assignment, filtered training rows, query-relative advantages, actor update and periodic checkpoint. Owner: agent-loop worker and PPO trainer. Proposed change: numerical actor parameters learned from rollouts. The policy proposes actions; code and reward services determine credit; optimizer/trainer admit updates without a per-update human approval or inspected validation-score veto. Humans supply the curriculum, reference outcomes, checkpoint and configuration. MCQ matching and open-ended judging are different answer-oracle consumers (SRC-1, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`, `train/verl/utils/reward_score/statelm_qa.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- benefit conclusion status: uninspected
- Immediate return: Assigned reward metadata and advantages; actor worker returns update metrics; periodic checkpoint writes model-related state and data-loader position.
- Later read-back: Trainer resume loads actor and available dataloader state. Parameter reuse is wired at checkpoint load, but this inspection does not close model export/deployment and rollout synchronization paths end to end.
- Delegated visibility: Reward worker receives response tokens plus reference-bearing sample metadata; open-ended judge receives prediction, reference and question. Distributed actor workers receive the training batch.
- Selection predicate: Snapshot node IDs match descendant terminal prefix IDs; rewards are averaged before trajectory limiting. Missing descendant terminals cause snapshot drops. Remaining scores are normalized by query UID and response masks select trained tokens.
- Invalidation or expiry: Checkpoint retention limits saved predecessors; resume can be disabled, automatic or explicit-path. HDFS load explicitly raises NotImplementedError; local dataloader absence restarts that data state. No semantic rollback criterion was established.
- Activation or effect: update_actor is called after advantage computation; periodic validation records metrics after updates. Actual weight changes, later behavioral dependence and successful improvement remain unobserved.
- Evidence limits: Source-wired learning machinery is not measured learning. External judge behavior, lower-level optimizer details, exact retained weights and production adoption remain uninspected.

> assigned_reward = float(np.mean(rewards))
> --- `train/verl/experimental/agent_loop/agent_loop.py`

> output.extra_fields["contextpilot_drop_from_training"] = True
> --- `train/verl/experimental/agent_loop/agent_loop.py:652-674`

> advantages = scores.unsqueeze(-1) * response_mask
> --- `train/verl/trainer/contextpilot/adv.py`

Admission/rejection/recovery: configured format failures and tool/budget failures penalize rewards; missing continuations veto snapshot training rows. Otherwise the trainer follows configured optimization steps, not a separate content approval. Checkpoint load provides numerical recovery, not evidence of reverting a bad scientific theory. Guidance consists of the static maintenance prompt, tool schemas and reward objective; retained products are parameters, checkpoints, metrics and optional trajectories. Reward scores select numerical updates rather than localizing and criticizing prompt claims (SRC-1, `train/verl/utils/reward_score/statelm_qa.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/ppo/ray_trainer.py`).

Learning: improved future QA capacity is the intended objective; improvement and attribution are uninspected. For a dispositional self-change assessment, the boundary is the training actor across training steps and checkpoint resume, not all inference deployment. Objective-bearing rewards are wired to update determination, and parameter updates target the policy's own organization. The inspected source does not establish exercised update-to-later-behavior dependence or causal improvement; it therefore supports no exercised self-improvement conclusion. This qualification does not negate the implemented reward-responsive update capacity.

### Claims

#### RT-CLM-fsm-controls
Label: Conditional FSM and context controls

Claimed operation: the FSM overlay exposes only tools legal at the current state; prompt guidance requires saving, cleanup, relevant review and final submission through finish. Owner: `ContextPilotFSM`; enforcement: schema filtering plus runtime allowed-name rejection and selected ID/key validation. Strength: protocol, with invariant name rejection only relative to the **computed** allowed set. Implementation conclusion status: wired. Operation conclusion status: uninspected. Semantic compliance is a policy request, not a code invariant. External contracts include model/API tool-call formatting, tokenizer accounting and tool-schema completeness (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`).

> """FSM overlay that exposes only the tools legal at the current agent state."""
> --- `infer/src/contextpilot_fsm.py`

Coverage: FSM parsed native calls and enabled textual fallback reach its allowed-name check; multiple native calls are reduced to one. Limits: unmatched-state schemas return all configured tools; the base caller and training registry do not pass that gate. Required tool_choice is configurable and does not replace dispatch validation. Force-finish and error exits do not guarantee successful semantic review or an answer (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

> if not filtered:
>     print(f"    [FSM-WARN] No tools matched for state {state.name}, "
>           f"falling back to full tool set.")
>     return self.tools
> --- `infer/src/contextpilot_fsm.py`

Token-window strength: best effort, not invariant. The controller returns its current payload even after no eligible assistant turns remain. Final-answer strength: protocol; logger extraction falls back to visible assistant text, so a written answer is not an oracle for protocol completion (SRC-1, `infer/src/contextpilot.py`).

> for msg in reversed(self.full_history):
>     if msg.get("role") == "assistant" and msg.get("msg_id") not in self.deleted_msg_ids:
> --- `infer/src/contextpilot.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-policy
Label: Prompt and retained context to policy

Consumer: inference policy model. Channel: system maintenance prompt, user-appended note/memory inventory and selected tool results/replacement text. Force: natural-language guidance/evidence, not executable authorization; symbolic state admission is separately enforced by Python. Horizon: repeated turns of one QA sample; JSON logging does not by itself extend knowledge reuse across samples. Context delivery is wired; content compliance, activation and benefit are unobserved (SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

> text += (external_context_summary if idx == 0 else "")
> --- `infer/src/contextpilot.py`

#### RT-BAP-reward-actor
Label: QA reward to actor parameters

Consumer: advantage estimator and actor update worker, with later actor checkpoint load. Channel: terminal scores, ancestor snapshot credit, query-relative numerical advantages and response masks. Force: computational training signal; unlike prompt text it directly supplies the update machinery. Horizon: training steps and checkpoint resume; export to a production inference service remains untraced. Wired update authority does not establish successful optimization or later exercised dependence (SRC-1, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`).

> self.actor_rollout_wg.load_checkpoint(
>     actor_path, del_local_after_load=self.config.trainer.del_local_ckpt_after_load
> )
> --- `train/verl/trainer/ppo/ray_trainer.py`

## Annotations

none
