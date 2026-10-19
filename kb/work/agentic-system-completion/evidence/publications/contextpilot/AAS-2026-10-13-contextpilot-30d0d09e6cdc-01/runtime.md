---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ContextPilot runtime baseline: FSM and ordinary document-QA inference, context control, and reinforcement-learning admission at the frozen commit."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot runtime report

## Runtime account

### Boundary and evidence strength

ContextPilot performs long-document question answering by letting a model select document retrieval, retention, context editing and answer-submission operations. Its shipped improvement plane trains the policy that selects those operations. This account covers the whole-system boundary in [boundary](boundary.md), not a general-purpose agent host. All findings below use SRC-1 at the frozen revision. Implementation and shipped instructions establish wiring and requests; no target execution, provider invocation, benchmark or training run was performed or supplied. Activation, reliability and gains remain unobserved.

Added implementation inspection beyond the boundary's initial coverage includes the tool schema, runner's sample/output loop, ordinary/FSM dispatch and exception handling, context rendering/editing and token-window loop, training state handlers and branch allocator, terminal scorer, GRPO estimator, actor optimizer and rollout weight-transfer passages. Paths are cited at their findings below. Source-native instructions are doctrine/design evidence, not instructions to this analyst. No extra source is introduced.

### Ordinary shipped invocation

The evaluation launcher selects `--version fsm`; `_import_contextpilot` selects `ContextPilotFSM` for that value and the ordinary `ContextPilot` otherwise. The runner partitions samples among processes, derives sample identity from `_id`, `id` or row position, obtains document/question/reference through configured conversion functions, constructs a new agent for each sample, applies client controls and invokes `run`. Resume skips IDs already recorded; retry-with-hint can inject the prior wrong answer and its attributed incorrectness. That is evaluator feedback supplied to a fresh agent, not an automatic reload of its old note store (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`).

> last_payload = agent.run(question, max_turns_to_fail=max_turns_to_fail)
> --- `infer/src/hf_test_runner.py`

The sample runner is the initiating principal; there is no separately authenticated model identity. The agent owns a document-bound tool library, fresh state manager and history. Worker rank can select an endpoint from an endpoint list. The model identity is a request string, not a frozen weight digest. Numeric message IDs identify editable history; tool-call IDs associate calls and results; chunk IDs address indexed document pieces; memory/note keys address retained findings; Elasticsearch requests filter on the current document ID (SRC-1, `infer/src/contextpilot.py`). The model component is [RT-CMP-vllm-client](#rt-cmp-vllm-client).

The default FSM path is [RT-RTE-fsm-inference](#rt-rte-fsm-inference). It requests length analysis, an initial plan, indexing, search, a post-search plan, chunk reads, saved findings, cleanup, saved-content review, and ultimately `finish`. The configured tool list lacks `buildEmbedding`, so the default path skips that optional state. The model proposes queries, reads, saved text and final answers. Code owns legal next-step sets and state transitions; `plan` only validates a nonempty model-written strategy. It does not call a separate planner. Search supplies ranked chunk IDs, highlighted fragments and section hints; subsequent chunk reads supply full selected passages. Search is bounded evidence selection, not proof of full-document coverage (SRC-1, `infer/tools/context-shaper_tools.json`, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`).

At each invocation, prompt construction takes the static system instructions, first user question with currently available memory/note summaries, and rendered history. A store read returns selected content as a tool result. Cleanup changes what later calls receive without necessarily deleting the originals in process memory. The runtime context owner and controls are [RT-OBJ-full-history](#rt-obj-full-history) and [RT-RTE-context-control](#rt-rte-context-control). Detailed memory revisions belong to the memory member; runtime establishes the write/read/render junction, not memory correctness or cross-session durability.

On successful `finish`, the loop stops. The returned value of `run` is a payload, not simply the answer. For prediction selection, the runner receives `final_answer` from `logger.save_final_result`: that logger scans tool messages in reverse order for a truthy `content.final_answer`, without checking the tool name, and substitutes `"No final answer found."` if none exists. The runner uses this value in the inference result and JSONL prediction with sample/worker metadata. It catches sample exceptions and still attempts result recording, so recording need not establish protocol completion. Ordinary assistant prose is not this prediction handoff's fallback. The separate `_extract_final_answer` helper prefers a `finish` tool result and otherwise takes the latest undeleted assistant text; it supplies `save_trajectory`'s snapshot answer, not the runner's benchmark prediction (SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`).

> res_file, final_answer = logger.save_final_result(agent, question, correct_ans, meta_info)
> --- `infer/src/hf_test_runner.py`

> for msg in reversed(full_history):
>     if msg.get("role") == "tool":
>         final_answer = msg.get("content", {}).get("final_answer")
>         if final_answer:
>             break
> if not final_answer:
>     final_answer = "No final answer found."
> --- `infer/src/contextpilot.py`

### Controls, forcing cases and their limits

The capability surface is broader than the default grant. `ToolLibrary` includes optional semantic/hybrid search, embeddings, reranking and note merging; `_execute_tool` also implements restoration. The default JSON grants 18 named functions: planning, analysis, indexing, budget checking, chunk reads, keyword search, memory/note write/read/update, four cleanup forms and finish. `restoreContext` is implemented but not granted in that JSON. The FSM further narrows this set per state. Python callers and configurable tool JSON are trusted configuration surfaces, not a sandbox. Source dispatch is not evidence of deployed process/network isolation; OpenAI-compatible services and Elasticsearch remain external contracts (SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`, `infer/src/contextpilot_fsm.py`).

Three forcing cases qualify load-bearing guarantees:

1. **Wrong-state action and alternate entry.** The FSM checks the parsed action against `allowed_names` before normal dispatch, independently of the provider's tool-choice compliance. But when no configured tool matches a state it returns the full configured set, and the ordinary entry checks global tool membership rather than FSM legality. Direct Python `_execute_tool` calls also lack FSM sequencing. Therefore legal-step rejection is a local FSM enforcement property, not a universal workflow guarantee. Provider-native tools, arbitrary host callbacks, shell tools and remote agent delegation are not part of the inspected default schema; no claim extends to provider internals or arbitrary extensions (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`; [RT-CLM-fsm-gating](#rt-clm-fsm-gating), [RT-RTE-ordinary-inference](#rt-rte-ordinary-inference)).
2. **No tool call, empty search and provider failure.** Required tool choice is requested, not assumed. Repeated no-tool responses cause nudges, selected deterministic reads/deletions, finish-only requests or termination. Empty searches can advance directly to best-effort review/finish. API failure during mandatory note/memory review can cause deterministic latest-key read-back; other API failures return an error-bearing payload. Hard termination and the logger's failure placeholder prevent an unconditional guarantee of a grounded `finish` answer; recording a prediction does not establish that `finish` succeeded. Mandatory review also means a successful reader call, not demonstrated incorporation of every saved fact (SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`).
3. **Oversized context and training alternate.** Inference's token-window routine can exhaust eligible history while still above the requested limit. It returns the remaining payload rather than rejecting it. Training instead proactively selects productive read/search-result deletions, then terminates and flags budget violations if necessary. Its state machine is generation/tool processing, not the inference FSM; passing the training schema to tokenization does not impose the inference action schedule. Neither route proves successful completion under context pressure (SRC-1, `infer/src/contextpilot.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`; [RT-RTE-context-control](#rt-rte-context-control), [RT-RTE-training-rollout](#rt-rte-training-rollout)).

These are source-traced countercases, not executed experiments. No adversarial provider trace, extension deployment, interrupted checkpoint recovery or cross-sample contamination test was observed.

### Improvement and change admission

The training launcher binds input Parquet files, model path, tool config, system prompt, rollout settings, `contextpilot_grpo` and the QA scorer. The asynchronous loop creates per-trajectory state, renders context and generates via the serving manager. Management actions emit snapshots; sensitivity-ranked branch continuations give additional terminal outcomes. Rewards are propagated by snapshot ancestry before the estimator normalizes within query groups. The actor then receives advantages, backpropagates policy loss and updates parameters; worker code transfers parameters into rollout serving and the trainer saves/reloads checkpoints (SRC-1, `train/sh/run_qwen3-8b_longbenchv2.sh`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`, `train/verl/workers/actor/dp_actor.py`, `train/verl/workers/fsdp_workers.py`). Decision ownership, oracles and recovery are recorded separately in [RT-RTE-branch-credit](#rt-rte-branch-credit) and [RT-RTE-policy-update](#rt-rte-policy-update).

This is an implemented improvement-directed parameter-change pathway, not observed successful learning. Its objective is answer correctness with format/tool/budget penalties, independently specifiable from any particular weight update. Within training rounds, trace-derived rewards are wired to update determination, parameters are the system's own decision machinery, and rollout weight transfer supplies a later behavioral-authority path. Without an execution trace, subsequent operation causally depending on a particular update is not established; exercised self-improvement and beneficial capacity change are therefore unestablished. Nothing here establishes content-directed criticism of a formulated theory, reflection or an autonomous theory builder. The retained policy change is numerical; plan prose and static rules do not by themselves establish those separate properties.

The inspected product/capability configuration surfaces are caller-selected prompt and tool files plus model/checkpoint paths. They let an operator replace instructions, grants or weights; they are not evidence that the QA model edits product source, approves deployment or enlarges its own tool registry. This report does not infer human per-content approval of model-generated notes or parameter updates from the human's launching the workflow (SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`).

## Shared records

### Components

#### RT-CMP-vllm-client
Label: Inference policy endpoint

Source-native identity: `vllm_client` and `model_name` in `ContextPilot`. Representational form: distributed-parametric policy behind an OpenAI-compatible API. Storage substrate: external serving/model memory, not the Python client's configuration dictionary. Inference code sends messages/tools and sampling parameters; it does not update policy weights. Exact parameters are not pinned by the source revision; `MODEL_ID` and endpoint configuration can resolve to different weights, including endpoint-list selection by worker rank. Mutable endpoint replacement is possible; provider internals and actual deployed fixity are uninspected. Evidence: SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`.

> self.model_name = (
>     vllm_config.get("MODEL_ID", "ContextPilot")
> )
> --- `infer/src/contextpilot.py`

#### RT-CMP-actor-module
Label: Training actor and rollout policy

Source-native identity: `actor_module`, actor optimizer and rollout weight recipient. Representational form: distributed-parametric tensors. Substrate: worker model/device memory and configured checkpoint storage. Parameters change during training when finite gradients permit the optimizer step; inference-serving weights receive transfers. Exact initial weights are not pinned: launcher requires a configurable `MODEL_PATH`; checkpoints are run products, not supplied frozen weights. The in-run rollout recipient is explicitly mutable. Whether a separately deployed inference endpoint uses a trained checkpoint is uninspected, not implied by the actor update. Evidence: SRC-1, `train/sh/run_qwen3-8b_longbenchv2.sh`, `train/verl/workers/actor/dp_actor.py`, `train/verl/workers/fsdp_workers.py`.

> self.actor_optimizer.step()
> --- `train/verl/workers/actor/dp_actor.py`

#### RT-CMP-judge-answer
Label: Open-ended QA judge

Source-native identity: `llm_judge_answer`. Representational form: distributed-parametric model judgment, parsed into a symbolic correctness value. Substrate: external endpoint selected by `OPENAI_BASE_URL` and `OPENAI_MODEL`. Its parameters are not updated by this scorer. Exact version is not pinned, and mutable endpoint/model configuration can resolve to another model; provider internals remain uninspected. It receives the reference answer, prediction and question, so this is an answer oracle in the training evaluation mode, not merely the policy's self-judgment. Multiple-choice scoring is a separate symbolic branch. Evidence: SRC-1, `train/verl/utils/reward_score/statelm_qa.py`.

> model_name = os.environ.get("OPENAI_MODEL")
> --- `train/verl/utils/reward_score/statelm_qa.py`

#### RT-CMP-llmlingua2
Label: Optional compression endpoint

Source-native identity: `_compress_context_with_llmlingua2`. Representational form: distributed-parametric external text transformation. Storage substrate: external service; output text is stored locally as a context replacement. This route sends no weight updates. Exact model weights are not pinned; endpoint JSON supplies the address and `MODEL_ID`, defaulting to `LLMLingua-2`, and can resolve to another service/model. The name does not establish the deployed service's architecture. Failure falls back to local text compression rather than proving the model transformation succeeded. Evidence: SRC-1, `infer/src/contextpilot.py`.

> model_id = cfg.get("MODEL_ID", "LLMLingua-2")
> --- `infer/src/contextpilot.py`

### Operative objects

#### RT-OBJ-full-history
Label: Full history and prompt view

Source-native identity: `full_history` with message IDs, cleanup sets/maps and snapshots. Substrate: per-agent Python lists/dictionaries/sets; snapshots/results can be serialized by logging methods and the runner. Operative parts differ: natural-language question, assistant prose, tool-result text and replacement summaries receive consequences through model interpretation; symbolic roles, IDs, call names and cleanup membership determine fixed rendering/dispatch. Originals remain in history when rendering substitutes stubs or summaries. `restorable_msg_ids` is distinct from mere presence in `deleted_msg_ids`; token-window deletion does not by itself grant the explicit restore tool. Evidence: SRC-1, `infer/src/contextpilot.py`.

> STUB_MESSAGE = "Content has been deleted to save space."
> --- `infer/src/contextpilot.py`

#### RT-OBJ-system-prompt
Label: Shipped QA instructions

Source-native identity: `fsm_plan_bm25_mc_prompt.txt` and the training `contextpilot_system_prompt.txt`, with the same inspected workflow wording. Representational form: natural language. Storage substrate: versioned text files, loaded into model-visible system messages; training also accepts a configured prompt-file path. They direct evidence search, saved findings, cleanup and answer submission. Their presence establishes requested behavior, not semantic compliance. Evidence: SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/configs/contextpilot_system_prompt.txt`, `infer/src/contextpilot.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`.

> Final answers must be submitted with `finish`; do not answer in plain text outside the tool call.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

### Routes

#### RT-RTE-fsm-inference
Label: FSM inference invocation

Endpoints/progression: evaluation sample → new `ContextPilotFSM` → rendered messages → model → first parsed tool call → allowed-name/key/message validation → Python executor → result/history → transition and next model call → finish or failure. Owner: runner for sample scheduling and files; FSM for state and legal transitions; model for semantic proposals. The default operating mode is bounded benchmark QA, not open-ended improvement. The supplied reference answer is logged for evaluation, not passed as an ordinary answer oracle to the policy. Retry-with-hint may supply the previously judged wrong answer. Human selection of task/configuration is separate from per-action software admission. SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool results return into the loop; `run` returns the final constructed payload. Runner saves the answer returned by `logger.save_final_result`, which selects the latest truthy tool-result `final_answer` or the failure placeholder, not the assistant-prose fallback of `_extract_final_answer`.
- Later read-back: Saved findings' summaries are injected into subsequent first-user-message renderings; allowed `readNote`/`loadMemory` calls return selected entries as new tool results. Old agent stores are not passed to the fresh per-sample constructor.
- Delegated visibility: No separate planner agent; the model receives rendered context, and local tools receive parsed arguments/state. External policy service receives the payload, not the agent's entire unrendered store.
- Selection predicate: State-specific tool set; successful search chunk candidates, read-count/evidence-ready thresholds, keyed store lookup and cleanup message-ID sets govern progression.
- Invalidation or expiry: Per-sample fresh construction resets state; cleanup alters future prompt views; normal termination calls document cleanup. General uncaught failure cleanup is not proven for every inference path.
- Activation or effect: Valid calls execute retrieval, retention, cleanup or final-answer production; read delivery is wired, semantic use and answer quality unobserved.
- Evidence limits: No executed invocation or API-compliance evidence. Empty tool matches fall back to full configured tools; repeated failures can terminate without finish. Logger recording can emit a failure placeholder and does not validate protocol completion.

Admission of retained findings: model proposes natural-language content and symbolic key/provenance arguments; software admits through available tools and store methods without a per-write human approval step in this path. Trigger is the model's write/update call under the shipped evidence-saving instructions. Invalid/disallowed calls return errors; later model updates can revise content. Detailed store-specific replacement/deletion/recovery semantics remain for the memory analyst rather than being inferred from successful dispatch.

> if action not in allowed_names:
>     result = {
>         "error": f"Tool '{action}' is not allowed in FSM state "
> --- `infer/src/contextpilot_fsm.py`

#### RT-RTE-ordinary-inference
Label: Ordinary inference alternate

Endpoints: non-FSM runner selection → `ContextPilot.run` → unrestricted configured-tool loop → executor/history → answer or stop. Owner: ordinary loop; model chooses progression. It lacks the state-specific schedule of [RT-RTE-fsm-inference](#rt-rte-fsm-inference). Current-tools filtering affects model requests; dispatch checks `self.tool_names`, not current-state legality. Operating mode and reference-answer separation are the same bounded QA mode; model proposes and software dispatches, with no independent answer-based veto before answer emission. Evidence: SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool response into history and final payload from `run`; runner records the answer returned by the shared logger's truthy tool-result scan or failure placeholder, not `_extract_final_answer`'s assistant-prose fallback.
- Later read-back: The shared payload builder delivers saved summaries and explicit store-read results on later calls; cleanup replacements persist across calls in this agent.
- Delegated visibility: Same local tool and external model boundaries as the FSM; no independently isolated sub-agent context is created.
- Selection predicate: Global configured tool membership; turn count, search-limit nudge and no-tool retry counters alter subsequent requests rather than imposing the FSM sequence.
- Invalidation or expiry: Fresh sample state and normal document cleanup; explicit edits and overflow recovery change prompt visibility.
- Activation or effect: Dispatch permits configured retention/retrieval/edit/finish actions without requiring the FSM's prerequisite chain. Search count activates a payload nudge; it is not a universal hard search prohibition.
- Evidence limits: No execution. Similar tool names do not give this path the FSM's enforcement guarantees; direct Python executor calls are another trusted bypass of sequencing.

> if action not in self.tool_names:
>     result = {"error": f"Tool '{action}' not found."}
> --- `infer/src/contextpilot.py`

#### RT-RTE-context-control
Label: Inference prompt editing and recovery

Endpoints: foreground model edit call or host size/overflow trigger → history ID selection → delete/truncate/summary/compression maps → `_build_api_payload` → next model invocation. Owner: runtime for rendering and automatic eviction; model for explicitly supplied summary or selected spans/IDs; optional compressor for text transformation. Context is reconstructed by value, not exposed as dereferenceable pointers. Original history remains reachable to host code. Unlike an isolated sub-agent frame, edits affect a shared agent history view and may leave a summary, stub or selected text; memory summaries remain injected. Evidence: SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Explicit edits report status/target/length; automatic paths rebuild the payload and may retry the provider.
- Later read-back: Summary/compression replacements reach later invocations at the edited message position; deletion delivers a stub. The explicit restore implementation clears edit markers for eligible IDs so the original is rendered again, but it is not granted by the default schema.
- Delegated visibility: Compressor receives selected message text only; it does not own the foreground tool loop. Historical snapshots are separate copies and are not retroactively rewritten.
- Selection predicate: Explicit message ID and role checks; truncate locates start/stop strings; FSM restricts cleanup targets; token-window control evicts earliest eligible assistant/tool pairs, while provider-overflow recovery targets read context.
- Invalidation or expiry: Explicit restoration clears applicable markers and eligibility; fresh agent resets maps. Automatic token-window stubbing does not itself add restore eligibility. Model-supplied replacements have no independent factual expiry check here.
- Activation or effect: Changed prompt bytes and reduced/replaced context are wired; reduced token count, retained evidence sufficiency and beneficial decisions are not observed. Local compressor failures trigger a fallback and expose that fact in the result.
- Evidence limits: Token-window enforcement stops when no eligible assistant remains, even if still oversized. The original question/system instructions and injected summaries can themselves exceed the limit. Service-side token limits and tokenizer agreement remain external dependencies.

Trigger/proposal/admission: explicit model edits or host limit checks propose a changed future prompt; software validates role/ID and applies markers, without human content approval. Invalid spans/IDs are rejected. Summary content is model supplied, not independently warranted. Original-history retention and the optional restore route support bounded recovery; a hard model-visible token cap is not an invariant.

> if asst_idx is None:
>     print("[TOKEN_WINDOW] No more assistant turns available to stub.")
>     break
> --- `infer/src/contextpilot.py`

#### RT-RTE-training-rollout
Label: Training trajectory context loop

Endpoints: training batch raw prompt/document → `AgentData`/`DocStateManager` → prompt tokens → serving manager → parsed calls → configured tools/state mutation → context rebuild/snapshot → continuation or termination. Owner: `StatelmToolAgentLoop`; model proposes calls, software parses, looks up and executes them. The model sees the training system prompt, summary lists and rendered history, not the inference FSM's dynamic action sets. Request UUID identifies a trajectory; message IDs and snapshot-node/prefix IDs identify edits and credit ancestry. Operating mode: bounded training/evaluation curriculum configured by Parquet data and rollout budgets. The policy receives the problem/document; the downstream scorer receives the reference answer. Evidence: SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tool responses and trajectory/snapshot outputs, including flags used by reward computation; finish terminates before appending its tool result to history, leaving the assistant call available for scoring.
- Later read-back: Rendered memory/note summaries and edited history reach future generations; writing/editing/retrieval boundaries can close a training segment and reconstruct the next prompt. Detailed retention semantics remain with the memory member.
- Delegated visibility: Tools execute in the worker executor with trajectory state; serving manager receives tokens. This is not isolation of a semantic subtask in a separately prompted helper agent.
- Selection predicate: Tool parser and registry, maximum processed calls, context/turn/model-length budgets. Automatic deletion ranks up to eight large read/search candidates plus the protected latest read, simulates token lengths and chooses a reducing candidate, relaxing latest-read protection only if necessary.
- Invalidation or expiry: Per-trajectory state; document cleanup has bounded waits and warnings; branch ownership avoids deleting a parent's shared document. Nonreducing deletion cannot make progress and budget violations terminate.
- Activation or effect: Tool operations alter current context and create training-credit boundaries. No-tool responses terminate with format violation instead of the inference loop's retry protocol; overlong observations are not exposed as silently truncated next prompts.
- Evidence limits: No supplied rollout. Budget/format/error signals do not prove recovery, correctness or inference-FSM compliance. Worker-executor concurrency is not a deployed security boundary.

Knowledge/context changes are admitted by tool execution, not human per-item approval. Foreground model proposals use the static prompt guidance; host reclamation proposes synthetic deletions based on token measurements. Invalid tool lookup/JSON becomes an error response. Originals and edit maps bound possible reconstruction, but this account does not assume inference's explicit restore capability in the training tool registry.

> logger.info("[ContextPilot] No tool call was emitted; terminating the trajectory")
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

#### RT-RTE-branch-credit
Label: Partial rollout selection and credit

Endpoints: parent pre-action state → context-change/next-generation entropy measurements → query-global branch ranking → cloned partial continuations → terminal scoring → ancestry-indexed mean rewards → selected training rows. Owner: agent-loop worker. Computation proposes branches from model management actions and decides allocation by sensitivity, not by a human selecting each branch. A branch reruns from cloned pre-action state; it is not a claim that deleting a context item alone caused a reward difference. Evidence: SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/utils/reward_score/statelm_qa.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Branch trajectory outputs and terminal/snapshot reward metadata to the trainer, not answers delegated back to the foreground QA loop.
- Later read-back: Trace-derived rewards feed the parameter update route [RT-RTE-policy-update](#rt-rte-policy-update); raw branch logs alone are not later agent knowledge.
- Delegated visibility: Branches clone history, memory and context-control state; document-index ownership can remain shared read-only until replacement. Only selected trajectory/credit data crosses into training, not a helper-agent textual report.
- Selection predicate: Weighted absolute relative context-size change plus entropy delta; remaining query snapshot budget determines branch allocation. Continuations are semaphore-limited; descendants contribute by prefix-node ancestry, and rows without terminal descendants are dropped.
- Invalidation or expiry: Branch exceptions yield an empty excluded continuation rather than aborting the query; branch document replacements are cleaned in finally. Snapshots without terminal reward lineage are marked to drop.
- Activation or effect: Terminal reward is delivered as the mean over each snapshot's terminal descendants; GRPO then compares retained rows within query identity. Benefit from sensitivity ranking is unobserved.
- Evidence limits: No observed entropy, branches, rewards or counterfactual comparison. Selection metrics and ancestry averaging do not identify a fine-grained causal contribution of one context action.

Answer oracle and mode: bounded supervised-answer QA. Multiple-choice compares extracted finish content with the reference letter or letter prefix; open-ended answers invoke [RT-CMP-judge-answer](#rt-cmp-judge-answer), with normalized exact equality as the inspected exception fallback. The scorer adds a format penalty; agent-loop reward computation also handles tool/budget flags. Expected answers come from dataset reward metadata, not independent discovery by the policy. Humans supply/configure the curriculum and external judge; software computes scores and accepts/drops training rows. Branch failure and missing terminal evidence can veto rows; reference correctness itself is not independently validated in this run.

> assigned_reward = float(np.mean(rewards))
> --- `train/verl/experimental/agent_loop/agent_loop.py`

> is_correct = has_valid_finish_tool_call and llm_judge_answer(predicted, ground_truth, question)
> --- `train/verl/utils/reward_score/statelm_qa.py`

#### RT-RTE-policy-update
Label: Policy update and checkpoint admission

Endpoints: rewarded trajectory rows → query-relative advantages → actor policy loss/backpropagation → optimizer → rollout weight transfer → checkpoint/save/reload. Owner: Ray trainer and actor/rollout workers. Guidance: static tool-use prompt and configured correctness/format/budget objective; what persists is updated numerical policy and selected checkpoint/recovery state, not an explicit criticism of a method theory. Human operators select model/data/configuration and may stop/change a run; computation determines each update, with no inspected per-update human approval. Evidence: SRC-1, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`, `train/verl/workers/actor/dp_actor.py`, `train/verl/workers/fsdp_workers.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Actor metrics and updated worker parameters; checkpoint calls persist configured actor/optional critic state, data-loader state and latest-step marker.
- Later read-back: Updated weights are transferred into rollout serving; resume loads actor/optional critic and data-loader state for subsequent training. An inference deployment consuming those checkpoints is uninspected.
- Delegated visibility: Trainer sends batch/advantages to worker groups; rollout receives parameter tensors. It does not receive human-readable diagnoses of individual memory errors through this path.
- Selection predicate: Configured estimator, response mask, query grouping, optimizer/loss controls and critic-warmup threshold; nonfinite gradient norm skips optimizer step. Validation is periodic measurement, not an inspected mandatory promote-only-if-better gate.
- Invalidation or expiry: Configurable checkpoint retention can remove older saves; launcher defaults retain one actor checkpoint. Resume can be disabled, automatic or explicit path; remote HDFS load is explicitly unsupported. Reload restores only configured contents; default launcher checkpoint contents do not promise full optimizer-state recovery.
- Activation or effect: Numerical decision parameters can change and enter later rollout serving. Successful learning and causally update-dependent later behavior are unobserved; saved checkpoints are not proof of deployment.
- Evidence limits: Source traces wiring through actor step and weight transfer, not an exercised training run or beneficial change. External data/model/compute and judge contracts are not frozen outcomes.

Admission account: training-step completion proposes changed parameters through gradient computation. Finite-gradient checks can reject a step; otherwise optimizer update is admitted without a separate quality-approval gate in the inspected trainer path. Periodic checkpoints permit configured recovery, not transactional rollback of every update. No automatic code/tool-capability rewrite follows from this route. Learning remains unestablished at the improved-capacity level; the implemented pathway is trace-responsive parameter adaptation, with the evidence and exercise limits stated above.

> await self.rollout.update_weights(per_tensor_param, peft_config=peft_config, base_sync_done=self.base_sync_done)
> --- `train/verl/workers/fsdp_workers.py`

### Claims

#### RT-CLM-fsm-gating
Label: State-local tool constraints

Claimed operation: each turn presents state-allowed tools and can require a tool call. Owner: `ContextPilotFSM`; enforcement points: allowed-tool construction, provider request and pre-execution action rejection. Guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. Covered path: normal FSM dispatch with a nonempty configured match. Alternatives: empty-match full-set fallback, ordinary loop, direct executor call, training loop and host recovery actions. External contract: provider must return usable calls to make progress; local rejection does not require compliant provider choice but cannot compel a successful answer. Evidence: SRC-1, `infer/src/contextpilot_fsm.py`; routes [RT-RTE-fsm-inference](#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](#rt-rte-ordinary-inference), [RT-RTE-training-rollout](#rt-rte-training-rollout).

> if not filtered:
>     print(f"    [FSM-WARN] No tools matched for state {state.name}, "
>           f"falling back to full tool set.")
>     return self.tools
> --- `infer/src/contextpilot_fsm.py`

The claim is deliberately weaker than semantic evidence sufficiency, successful finish, universal review or a security sandbox. Its fallback witness prevents extending the normal-path schedule to every caller configuration.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: QA instruction delivery

Consumer: inference policy and training rollout policy. Channel: system-message text from [RT-OBJ-system-prompt](#rt-obj-system-prompt), plus tool descriptions and available-summary lists in rendered input. Force: natural-language guidance interpreted by a model, distinct from symbolic dispatcher rejection. Horizon: subsequent calls in a task and fresh tasks loading the same configured files. Text recommends retrieval, selective retention and cleanup; faithful obedience and correctness are not guaranteed. Evidence: SRC-1, `infer/src/contextpilot.py`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`.

> {"role": "system", "content": self.system_prompt}
> --- `infer/src/contextpilot.py`

#### RT-BAP-rollout-weights
Label: Updated policy serving authority

Consumer: rollout generation model. Channel: parameter tensors transferred by worker code from [RT-CMP-actor-module](#rt-cmp-actor-module). Force: distributed-parametric determination of generated token distributions, not optional textual advice. Horizon: later rollout generations after synchronization; checkpoint reload can extend training recovery across processes/runs, subject to saved contents. It is wired authority, not evidence that any particular update was exercised or improved outcomes. Evidence: SRC-1, `train/verl/workers/fsdp_workers.py`, `train/verl/trainer/ppo/ray_trainer.py`; passage retained in [RT-RTE-policy-update](#rt-rte-policy-update).

## Annotations

none
