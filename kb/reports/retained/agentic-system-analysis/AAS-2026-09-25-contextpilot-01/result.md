---
type: types/agentic-system-analysis-result.md
description: "Code-grounded analysis of ContextPilot's inference context control and trace-fed training path, with bounded memory and epistemic findings"
run-id: AAS-2026-09-25-contextpilot-01
system: ContextPilot
run-date: '2026-09-25'
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: 782cbb6611fb610c4cf6fafda6022b7e89cae191
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  scope: Use-accumulated inference and training notes, plans, histories, context replacements, relation/access
    caches, branch replay state, imported wrong-answer retry records and repository-trained actor parameters/checkpoints.
    Covers default FSM and base alternatives, conditional embeddings/compression and callable nondefault memory
    methods. Excludes ordinary incoming corpus/search indexes, static prompts, external SDK internals and externally
    pretrained weights.
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values:
      - files
      - graph
      - in-memory
      - model-weights
      - vector
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-3
      - OBJ-4
      - RTE-3
      note: Task dictionaries, adjacency graph and optional dense vectors, retained context, imported retry files
        and learned checkpoint files; excludes imported corpus indexes and provider internals.
    representational_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - parametric
      - symbolic
      records:
      - OBJ-5
      - OBJ-6
      - OBJ-7
      - OBJ-8
      - OBJ-3
      - OBJ-4
      note: Readable notes, plans and summaries coexist with IDs, masks, scores, token arrays and learned actor
        parameters. Numeric embedding arrays are access representations, not an additional claim of model learning.
    lineage:
      assessment: known
      basis: wired
      values:
      - imported
      - other-compiled
      - trace-extracted
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Agent derives notes, plans and summaries from the interaction; code compiles graph/access structures
        and checkpoints; retry records arrive through an external file. Static human-authored prompts are outside
        scope.
    behavioral_authority:
      assessment: known
      basis: wired
      values:
      - enforcement
      - instruction
      - knowledge
      - learning
      - ranking
      - routing
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Content advises the task model; plans/retry hints instruct; graph scores rank; memory occupancy/read-review
        state routes tool availability; edit masks enforce payload inclusion; rollout tensors train the actor.
    write_agency:
      assessment: known
      basis: wired
      values:
      - automatic
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-2
      note: Writers are model tool calls and runtime/trainer transformations. Source uses manual summary to mean
        model-supplied summary; no human memory editor is wired in these routes.
    curation_operations:
      assessment: known
      basis: afforded
      values:
      - consolidate
      - decay
      - evolve
      records:
      - RTE-5
      - RTE-7
      - RTE-9
      note: Summaries/compression reduce active retained context; deletion forgets payloads or entries; append/overwrite
        revises entries. No semantic near-duplicate merger, promotion, or truth-based invalidation is established.
    read_back_direction:
      assessment: known
      basis: wired
      values:
      - pull
      - push
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-10
      - RTE-2
      - RTE-3
      note: Task model requests entries; runtime supplies catalogs, selected history and automatic recovery reads;
        training selector supplies retained branch state to continuation workers.
    read_back_signal:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-8
      - RTE-10
      - RTE-3
      note: 'Known partial mapping: coarse catalog/recency supply, identifier matches for history replacement
        and retry sample selection, lexical/entity and optional embedding neighbors during automatic recovery.
        Training branch replay additionally ranks numeric context/entropy sensitivity, which has no exact controlled
        signal value; cannot assert a complete value set for the full scope.'
    trace_learning:
      assessment: known
      basis: wired
      values:
      - 'yes'
      records:
      - RTE-5
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Automatic trace-derived notes/plans/summaries persist to subsequent task turns; a supplied prior-answer
        record becomes retained retry guidance for the same task; sampled trajectories also produce learned actor
        parameters. Raw logging alone is not the basis.
    trace_source:
      assessment: known
      basis: wired
      values:
      - tool-traces
      - trajectories
      records:
      - RTE-5
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Read-tool observations and assistant/tool interaction histories feed retained task guidance; complete
        and partial rollouts feed rewards and actor updates; imported wrong-answer trajectory records feed retry
        guidance.
    learning_scope:
      assessment: known
      basis: wired
      values:
      - per-task
      - cross-task
      records:
      - RTE-5
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Per-item fresh agent and per-rollout AgentData establish task-local guidance; the actor updated from
        query groups is reused across training tasks. Wrong-answer retry stays within the same task across attempts.
        Session IDs alone are not used as evidence.
    learning_timing:
      assessment: known
      basis: wired
      values:
      - online
      - staged
      records:
      - RTE-5
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Notes/plans/context substitutions and generated retry hints affect the next attempt or turn online;
        collected and rewarded trajectories train parameters in successive rollout/update stages.
    distilled_form:
      assessment: known
      basis: wired
      values:
      - natural-language
      - parametric
      - symbolic
      records:
      - RTE-5
      - RTE-7
      - RTE-8
      - RTE-2
      - RTE-3
      note: Qualifying retained guidance includes prose, structured relation records/access and edit state derived
        from traces, and trained parameters; raw snapshot token arrays alone do not establish distillation.
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records:
      - CLM-4
      note: No retained execution evidence testing answer dependence on recalled content was inspected; README
        performance claims and snapshot mechanics tests cannot establish this. This is not a claim that no such
        experiment exists outside the frozen inspected boundary.
---

# ContextPilot — exact analysis

## Run identity

Run: `AAS-2026-09-25-contextpilot-01`; source cutoff 2026-09-25.

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/contextpilot.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/memory-report.md`

**Memory analysis report SHA-256:** `47da38196b2d8734b30b72e3a8192f156bd439d64c81a94323cb9565d94656dd`

## Boundary and evidence

ContextPilot is an enclosing runtime for long-context question answering, with a linked builder/training plane. Whole-system means repository-owned ContextPilot responsibilities: evaluator launcher, inference loop, state-machine wrapper, document tools, context and memory editing, ContextPilot-specific partial rollout/reward assignment and its parameter-update/checkpoint interfaces. Generic vendored verl features beyond those consumed by the supplied ContextPilot recipe are not claimed as ContextPilot mechanisms. Distributed GPU kernels, remote model implementations, external Elasticsearch implementation, data collection/label validity, supplied model weights and paper experiments are excluded. Those exclusions prevent a deployment isolation guarantee, immutable model-identity assertion, independent oracle validation, or measured performance conclusion.

Purpose: independently characterize what the source wires and where memory, feedback and epistemic authority act. The only external evidence is `https://github.com/Tencent/ContextPilot` at `782cbb6611fb610c4cf6fafda6022b7e89cae191`. Repository-only source allowlist; no paper, prior analysis, ingest prose or current worktree supplies evidence. Code-grounded assessment with documented claims kept separate. No experiment was performed.

## Source register

| source ID | kind / stable identity | revision / layer | inspected scope and anchors | access gaps and conclusion prevented |
|---|---|---|---|---|
| SRC-1 | Git, `https://github.com/Tencent/ContextPilot` | `782cbb6611fb610c4cf6fafda6022b7e89cae191`; implementation | `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `infer/src/hf_test_runner.py`, `infer/src/hf_score_fns.py`, `infer/tools/context-shaper_tools.json`; ContextPilot agent-loop, reward, advantage, worker and trainer interfaces under `train/verl/`, launch scripts | no live services, model weight artifacts, LFS data contents or executed training; implemented paths are not observed benefits |
| SRC-2 | Git, `https://github.com/Tencent/ContextPilot` | same full revision; doctrine/design and separately reported operation | `README.md:36-43,120-161`, `infer/README.md:43-95`, `train/README.md:111-151`, `infer/configs/fsm_plan_bm25_mc_prompt.txt:1-28` | reported improvement lacks candidate-linked experiment evidence in this pass |

Operational access root: `/home/zby/llm/commonplace/related-systems/Tencent--ContextPilot`. All evidential reads used full-commit `git --no-replace-objects show`, scoped grep or tree listing. Truncated broad discovery output was not treated as evidence; cited ranges were delivered in bounded reads. Commit-pinned source URLs and exact quotations below are the durable evidence anchors.

## Shared records

### Components

CMP-1 — ContextPilot and ContextPilotFSM own serial model/tool execution and mutable session state. Symbolic Python control, in-memory histories and configured tool schemas. Implementation conclusion status: wired. Source: SRC-1 `infer/src/contextpilot.py:2148-2298,3432-3634`, `infer/src/contextpilot_fsm.py:826-1445`.

CMP-2 — task language model, distributed-parametric, called through OpenAI-compatible endpoint using model alias and worker-rank endpoint selection. Inference parameter-update conclusion status: uninspected for provider internals; the inspected client issues generation calls, not weight updates. Exact-version identity conclusion status: uninspected: configured alias `ContextPilot` and operator-supplied checkpoint do not pin immutable weight bytes. Training changes this actor through CMP-3, separately below. Source: SRC-1 `infer/src/contextpilot.py:2181-2230,2646-2688`, `infer/configs/openai_endpoint_1x_nonthinking.json:1-11`.

CMP-3 — ContextPilot-specific RL pipeline atop verl: asynchronous training tool loop, partial branches, subtree credit, GRPO group normalization, actor optimizer and checkpoint interfaces. Symbolic coordination and distributed-parametric actor state. Parameter changes during training conclusion status: wired; exact initial/final parameter identity and actual operation conclusion status: uninspected. Actor model is operator-selected `MODEL_PATH`; the code performs gradient updates and sends current tensors into rollout workers. Source: SRC-1 `train/verl/workers/actor/dp_actor.py:267-285,440-490`, `train/verl/workers/fsdp_workers.py:632-665,795-806`, `train/sh/run_qwen3-8b_longbenchv2.sh:166-198`.

> await self.rollout.update_weights(per_tensor_param, peft_config=peft_config, base_sync_done=self.base_sync_done)
> --- `train/verl/workers/fsdp_workers.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

CMP-4 — configured answer judge, distributed-parametric, receives supplied question/reference/prediction for open-ended training and supported evaluation tasks. This is a separate evaluator role, not evidence of a pinned independent model. Version identity and provider parameter changes conclusion statuses: uninspected. Source: SRC-1 `train/verl/utils/reward_score/statelm_qa.py:95-160`; SRC-2 `infer/README.md:43-48`.

CMP-5 — superseded combined auxiliary-model seed (embedding/reranking/compression), split into CMP-6, CMP-7 and CMP-8; no operative aggregate identity or finding relies on this record.

CMP-6 — optional embedding endpoint, configured model or default `text-embedding-3-small`; embeddings serve document retrieval and memory relation scoring. The call interface is wired when credentials/configuration enable it; exact parameters/version and provider changes are uninspected. Source: SRC-1 `infer/src/contextpilot.py:887-897,1002-1047`.

CMP-7 — optional cross-encoder reranker interface to configured `/rerank`, consumes formatted query and candidate documents and sorts returned relevance scores. Interface conclusion status: wired; availability to the default catalog and memory relevance are separately scoped in the specialist findings. Model identity, internals and parameter updates conclusion statuses: uninspected. Source: SRC-1 `infer/src/contextpilot.py:1129-1193`.

CMP-8 — compression endpoint called using configured identifier or `LLMLingua-2`, a name that does not establish its actual architecture/weights. Receives original text and requested retained percentage via chat completions; independent random-word fallback is nonparametric. Interface conclusion status: wired. Exact model version, fidelity and provider changes conclusion statuses: uninspected. Source: SRC-1 `infer/src/contextpilot.py:2693-2760`; memory route covers fallback admission and later delivery.

### Operative objects

OBJ-1 — question and attached corpus, imported natural-language task inputs with symbolic sample IDs, labels and chunk access structures. Labels belong to evaluator input; ordinary actor invocation receives question/document rather than `correct_ans`. Acquired data's truth and benchmark validity remain uninspected. Source: SRC-1 `infer/src/hf_test_runner.py:285-320,365-400`.

OBJ-2 — proposed final answer, natural-language task response in `finish` arguments/tool result, or fallback last undeleted assistant text after an incomplete run. Stored as evaluation output and consumed by scoring; extraction is not proof the model reached a valid answer. Source: SRC-1 `infer/src/contextpilot.py:3618-3634`, `infer/src/hf_test_runner.py:379-425`.

> for msg in reversed(self.full_history):
>     if msg.get("role") == "tool" and msg.get("tool_name") == "finish":
>         content = msg.get("content", {})
>         if isinstance(content, dict) and "final_answer" in content:
>             return content.get("final_answer")
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

OBJ-3 — training trajectories/snapshots, response masks, parent-node lineage, sensitivity values and terminal/subtree rewards. Symbolic arrays/metadata plus decoded natural-language interaction content; used to replay branches and construct training rows. Reward means derive from selected descendant terminals, not independent judgments of every intermediate claim. Source: SRC-1 `train/verl/experimental/agent_loop/statelm_agent_loop.py:1414-1503,1578-1684`, `train/verl/experimental/agent_loop/agent_loop.py:652-708,780-810`.

OBJ-4 — updated actor parameters and checkpoint bundle. Distributed-parametric weights, symbolic trainer/dataloader state and optional optimizer, on GPU/process memory and files. Parameters affect later rollout generations; persisted model state can be loaded on resume, but default `[model,extra]` omits optimizer state and cannot establish exact optimizer-continuation equivalence. Source: SRC-1 `train/verl/trainer/ppo/ray_trainer.py:888-991`, `train/sh/run_qwen3-8b_longbenchv2.sh:109-110,226-227`; SRC-2 `train/README.md:148-151`.

OBJ-5 — structured memories and simple notes. In-memory keyed dictionaries hold full_content and summary. Structured entries additionally carry entities/episodes as normalized text, relation dictionaries, source chunk/message lists and timestamps. Simple notes lack these provenance fields. These are model-derived content with knowledge authority; plans may also carry guidance in history. SRC-1 `infer/src/contextpilot.py:202-221,617-675,710-745`. Training equivalents are SRC-1 `train/verl/tools/statelm_tools.py:534-668` and `train/verl/tools/contextpilot_memory.py:472-567`.

>     def __init__(self):
>         self.notes = {}
>         self.simple_notes = {}
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

OBJ-6 — access structures over structured memories. Cached signatures, optional normalized float vectors and symmetric scored adjacency are distinct from content. The signatures derive from entities, facets, dates, relations and a text signature; scores affect related-entry ranking. SRC-1 `infer/src/contextpilot.py:388-429,460-615,887-909`. Stored edge explanations contain lexical/entity/time/relation overlap; numeric vector_sim is stored on the edge but omitted from the returned relation_reason. Reindexing compares a changed entry against all other retained entries, so it reduces repeated query-time work while write cost still grows with retained entries. Training constructs the same caches, including reindexing when a memory wrapper is recreated: SRC-1 `train/verl/tools/contextpilot_memory.py:20-31,320-406,450-495`.

OBJ-7 — raw history, plans and active context overlays. full_history retains user/assistant/tool records and model-authored plan arguments. Integer-keyed delete, summary, truncation, compression and restoration metadata control rendering. Derived prose replacements are retained independently of raw content and later delivered; raw history and masks must not be confused with their rendered display. SRC-1 `infer/src/contextpilot.py:2259-2272,2499-2555,2592-2619,2783-2947,2963-2982`.

OBJ-8 — training branch state and inference snapshots. Inference snapshots are captured payload lists and can be written with full history and overlay maps to JSON; no inference reload consumer was found in the inspected runner. Training branch objects, however, are consumed directly by resampling workers. They retain notes, histories, masks, prompt arrays, document references and branch metadata. SRC-1 `infer/src/contextpilot.py:3666-3693`; `train/verl/experimental/agent_loop/statelm_agent_loop.py:675-788,1285-1302`. Readable text does not replace the token-array and mask payload.

>         branch_data.full_history = copy.deepcopy(agent_data.full_history)
>         branch_data.deleted_msg_ids = copy.deepcopy(agent_data.deleted_msg_ids)
>         branch_data.msg_id_counter = agent_data.msg_id_counter
>         branch_data.had_delete_operation = agent_data.had_delete_operation
>         branch_data.had_tool_failure = agent_data.had_tool_failure
>         branch_data.had_format_violation = agent_data.had_format_violation
>         branch_data.memories = copy.deepcopy(agent_data.memories)
>         branch_data.notes = branch_data.memories
>         branch_data.simple_notes = copy.deepcopy(agent_data.simple_notes)
>         branch_data.summarized_msg_ids = copy.deepcopy(agent_data.summarized_msg_ids)
>         branch_data.truncated_msg_ids = copy.deepcopy(agent_data.truncated_msg_ids)
>         branch_data.compressed_msg_ids = copy.deepcopy(agent_data.compressed_msg_ids)
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

### Routes

RTE-1 — shipped per-question FSM inference. Implementation conclusion status: wired. Operator supplies checkpoint/tokenizer, endpoint, dataset and recipe; evaluation defaults select `--version fsm`. Worker assigns sample via locked shared counter or rank stride, derives question/document, creates a new agent/state manager, then executes serial model/tool turns. The symbolic FSM owns tool eligibility; the model proposes arguments and choice among allowed tools. States guide analyze, plan, index, search, evidence reading, note/memory writing, cleanup, review, finish. The caller gets a final active payload; logger extracts OBJ-2 and saves records. Source: SRC-1 `infer/scripts/eval_task.sh:128-145`, `infer/src/hf_test_runner.py:245-320,348-425`, `infer/src/contextpilot_fsm.py:114-174,826-1180,1351-1445`.

The tool list is filtered before model call and returned action checked again against `allowed_names`; forbidden actions return an error instead of execution. This is a local invariant on that dispatch branch. It is not a universal least-privilege or state-sequence guarantee: missing matching tool schemas explicitly fall back to the entire configured catalog; base loop RTE-4 has weaker enforcement. Model calls can use native tool output or configured textual `<tool_call>` parsing, both reaching the same FSM check; multiple calls are reduced to the first. The default 18-tool catalog exposes document, note, memory, planning and context-edit operations; deployment isolation of Python/extensions/services is uninspected, rather than asserted from that catalog.

> if action not in allowed_names:
>     result = {
>         "error": f"Tool '{action}' is not allowed in FSM state "
>                  f"'{self._fsm_state.name}'. "
>                  f"Allowed tools: {allowed_names}. "
>                  f"Please call one of the allowed tools."
>     }
> --- `infer/src/contextpilot_fsm.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

> filtered = [t for t in self.tools if t["function"]["name"] in names]
> if not filtered:
>     print(f"    [FSM-WARN] No tools matched for state {state.name}, "
>           f"falling back to full tool set.")
>     return self.tools
> --- `infer/src/contextpilot_fsm.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Guidance is shipped natural-language QA policy, including preserving role/temporal qualifiers, checking direction of a relation, alternate count searches and chronological supersession; these are instructions to the actor, not runtime semantic checks. The `plan` tool checks only that model-supplied `strategy` is nonempty; the model's tool arguments carry the actual plan, and a short success response advances control. It does not invoke a second planner. Programmatic evidence thresholds count distinct read chunks; they do not test whether evidence warrants the final answer. Plan content can formulate tentative expectations, but actual theory formulation, operative semantic use, content-directed criticism and criticism-attributable capacity improvement are uninspected without candidate-linked traces. Its separately accessible strategy text affords addressability; no observed criticism follows from its label.

> strategy = params.get("strategy") if isinstance(params, dict) else None
> if not isinstance(strategy, str) or not strategy.strip():
>     return {
>         "error": "plan tool requires a non-empty 'strategy' argument "
>                  "containing your reflection and next-step plan."
>     }
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Recovery: bounded API retries except non-429 client errors; overflow can trigger deletion then retry; state-specific retries can auto-read top search result, auto-delete eligible context or complete mandatory note read after API failure. Persistent invalid optional review/no-tool behavior can force finish or terminate. Turn/search thresholds request finish at allowed review state; the while condition has an S7 extension, so configured numbers are not a universal hard deadline. The final answer is not verified before return. External effects are model/embedding/compression/reranking requests, Elasticsearch indexing/search and local result files, within separately configured service/host permissions. No multiagent handoff is needed for ordinary inference; evaluator workers run independent questions. Memory records below specify later read-back, invalidation and scope. No activation or benefit is observed here.

RTE-2 — training branch exploration, reward assignment and actor update. Implementation conclusion status: wired. Activation is conditional: the registry selects dataset `agent_name`, otherwise configured `default_agent_loop`, whose shipped generic value is `single_turn_agent`. The ContextPilot class registers as `statelm_tool_agent`; the external transformed dataset was not inspected, so the supplied recipe's actual selection is uninspected. This finding preserves the implemented route without assuming every training invocation reaches it. Sources: SRC-1 `train/verl/experimental/agent_loop/agent_loop.py:1006-1008,1097-1116`, `train/verl/experimental/agent_loop/statelm_agent_loop.py:451-455`, `train/verl/trainer/config/rollout/rollout.yaml:207-208`.

> if "agent_name" not in batch.non_tensor_batch:
>     default_agent_loop = config.agent.default_agent_loop
>     batch.non_tensor_batch["agent_name"] = np.array([default_agent_loop] * len(batch), dtype=object)
> --- `train/verl/experimental/agent_loop/agent_loop.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

 Human operator supplies model, training/validation data, budget and judge endpoint. Bounded benchmark curriculum mode, not autonomous open-world objective discovery. Trigger: scheduled training iterations. Model generates tool actions under the shipped task prompt, the training loop captures pre-action state, then computes sensitivity from context-length change plus post-observation versus initial uncertainty. Query-global sorting selects highest sensitivity branches under budget; semaphore bounds simultaneous branches; branch failures are excluded without aborting the query. Training reruns the generating loop from cloned pre-action state; the explored object is an alternative continuation, not a verified isolated causal intervention. Sources: SRC-1 `train/verl/experimental/agent_loop/statelm_agent_loop.py:1285-1322,1533-1684`, `train/verl/experimental/agent_loop/agent_loop.py:780-956`.

> branch_point["sensitivity"] = (
>     float(getattr(self, "contextpilot_context_weight", 1.0))
>     * float(branch_point.get("context_delta", 0.0))
>     + float(getattr(self, "contextpilot_entropy_weight", 1.0)) * entropy_delta
> )
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Oracle: dataset-supplied expected answer. Multiple choice uses string-based matching; open-ended scoring gives question, reference answer and prediction to CMP-4, with lowercase exact-match fallback on judge failure. Reward adds format and separately implemented tool/budget penalties. The oracle decides task-target match, not correctness of all stored notes, plan explanations or compression. Descendant terminal rewards are associated to prefix nodes and averaged; snapshots lacking terminal descendants are dropped. The dedicated advantage estimator sums token scores, normalizes by mean/std across query UID and broadcasts through the response mask. Parent numerical lineage and mask checks enforce training structure, not epistemic acceptance of intermediate statements. Sources: SRC-1 `train/verl/utils/reward_score/statelm_qa.py:95-160,182-211`, `train/verl/experimental/agent_loop/agent_loop.py:625-708`, `train/verl/trainer/contextpilot/adv.py:23-72`.

> rewards = node_to_rewards.get(str(node_id), []) if node_id is not None else []
> if rewards:
>     assigned_reward = float(np.mean(rewards))
>     terminal_count = len(rewards)
>     output.reward_score = assigned_reward
> else:
>     assigned_reward = None
>     terminal_count = 0
>     output.reward_score = None
>     output.extra_fields["contextpilot_drop_from_training"] = True
> --- `train/verl/experimental/agent_loop/agent_loop.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

> if is_mcq_question:
>     is_correct = has_valid_finish_tool_call and (
>         (predicted.strip() == ground_truth) or (predicted.strip().startswith(f"{ground_truth}."))
>     )
> else:
>     is_correct = has_valid_finish_tool_call and llm_judge_answer(predicted, ground_truth, question)
> --- `train/verl/utils/reward_score/statelm_qa.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Admission: the training worker constructs policy loss from scored samples and current probabilities; backward/optimizer changes actor weights. Nonfinite gradient norm vetoes the step; validation is scheduled after update, not an inspected improvement-before-admission gate. Parameters are delivered to rollout workers and saved periodically; resume selects latest or operator path, while HDFS resume is explicitly unsupported here. Checkpoints give recovery capability; no automatic performance-regression rollback was established by these inspected update/save/load interfaces. Source: SRC-1 `train/verl/trainer/ppo/ray_trainer.py:1255-1317,943-991`, `train/verl/workers/actor/dp_actor.py:267-285,440-490`, `train/verl/workers/fsdp_workers.py:632-665,795-806`.

> if not torch.isfinite(grad_norm):
>     print(f"WARN: rank {torch.distributed.get_rank()} grad_norm is not finite: {grad_norm}")
>     self.actor_optimizer.zero_grad()
> else:
>     self.actor_optimizer.step()
> --- `train/verl/workers/actor/dp_actor.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

The persisted change is parameters and training lineage, not an individually stated theory of context management. Individual semantic claims in parameters are not determinable here. Formulation, operative theory use, content-directed criticism and capacity improvement attributable to criticism all have conclusion status uninspected. Reward optimization is wired direct policy adaptation. Read-back to a subsequent rollout and restored model use are wired; actual changed behavior, persistent benefit or unseen-task improvement uninspected. Invalidation: sample admission flags and parameter replacement, checkpoint retention configuration; task-to-task horizon through actor weights. Immediate output is training metrics/checkpoints, later consumer is rollout/inference model, with operator-selected deployment. Model/provider weights external to the training actor are excluded from this update claim.

>                     if self.config.trainer.critic_warmup <= self.global_steps:
>                         with marked_timer("update_actor", timing_raw, color="red"):
>                             batch.meta_info["multi_turn"] = self.config.actor_rollout_ref.rollout.multi_turn.enable
>                             actor_output = self.actor_rollout_wg.update_actor(batch)
>                         actor_output_metrics = reduce_metrics(actor_output.meta_info["metrics"])
> --- `train/verl/trainer/ppo/ray_trainer.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>   default_agent_loop: single_turn_agent
> --- `train/verl/trainer/config/rollout/rollout.yaml` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

RTE-3 — evaluation recording/scoring and optional failed-sample retry. Implementation conclusion status: wired. Trigger: returned answer or caught agent exception; worker still saves result with supplied reference and diagnostic payload, flushes JSONL. Choice scorer applies permissive extraction/matching and writes scores; judge-backed tasks have separately configured evaluator. Score is a report, not a block on the already returned answer. A selected failed-samples file can restrict reruns and inject the prior wrong answer with an instruction to try another approach; this is outcome feedback, not supplied correct answer to the task actor. Operator owns invocation and file provenance; that provenance is uninspected. Source: SRC-1 `infer/src/hf_test_runner.py:281-294,362-425`, `infer/src/hf_score_fns.py:185-267`; SRC-2 `infer/README.md:43-48,89-95`.

> if retry_with_hint and failed_samples_map and sample_id in failed_samples_map:
>     wrong_ans = failed_samples_map[sample_id].get("wrong_answer", "")
>     if wrong_ans:
>         retry_hint = f"\n\n[Note: A previous attempt answered \"{wrong_ans}\" which was incorrect. Please try a different approach and search more thoroughly.]"
> --- `infer/src/hf_test_runner.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Later read-back: resume skips completed IDs rather than reconstructing active memory; explicit retry uses selected wrong-answer text. Evidence horizon per named sample/retry run. No automatic quality-based promotion of a deployed checkpoint is established by these evaluation interfaces. Their data and metrics can inform an operator; causal improvement from a retry is uninspected. Reference correctness/license stays benchmark-bound.

RTE-4 — base ContextPilot loop alternate. Implementation conclusion status: wired. Any evaluator `version` other than exact `fsm` selects base class. Same core state/tools/provider, without FSM sequencing. Payload hides searches after search budget and restricts to finish after turn target, but dispatch validates against all configured `self.tool_names`, not the currently filtered list. A provider returning a configured but omitted tool can therefore reach execution here. This is a source-level enforcement distinction, not an executed exploit. Native and text-fallback outputs both reach that branch. Hard while-turn bound exists, with within-turn retry/recovery exceptions; final answer fallback and local persistence match RTE-1/RTE-3. No additional memory storage is implied. Source: SRC-1 `infer/src/hf_test_runner.py:21-40`, `infer/src/contextpilot.py:3107-3123,3432-3614`.

> if action not in self.tool_names:
>     result = {"error": f"Tool '{action}' not found."}
> else:
>     try:
>         if action == "plan":
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

RTE-5 — model-authored note retention and requested read. Trigger: CMP-2 tool call after document reads. Producer: CMP-2; storage writer: StateManager or training memory helper. Input: selected observations/current interaction; output: OBJ-5 plus rebuilt OBJ-6. Retention: current agent/rollout, with optional logging. Consumer: later CMP-2 readNote/loadMemory calls and RTE-6. Pull selector: exact key; structured reads also request at most max_related adjacent entries, default five. Authority: knowledge for content, ranking for related candidates, routing for FSM store-dependent tool menus. Status: wired. SRC-1 `infer/src/contextpilot.py:617-745,1946-1991`; `infer/src/contextpilot_fsm.py:91-112,164-209,779-791`; training counterpart `train/verl/tools/statelm_tools.py:534-668`.

>     def read_note(self, key, max_related=5):
>         note = self.notes.get(str(key))
>         if note is None:
>             return {"error": f"Memory '{key}' not found!"}
>         return {
>             "memory": deepcopy(note),
>             "directly_related_memories": self._related_memories(key, max_related=max_related),
>         }
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Admission and maintenance: model tool arguments are automatically normalized and stored; new writes at the same key replace prior content without versioned history. Updates append, overwrite or physically remove entries and rebuild/remove graph edges. Exact relation dictionaries/source IDs may be deduplicated, without a semantic duplicate-memory test. The shipped prompt asks for useful findings and correct relationship/temporal qualifiers; it does not grant source-proven claims. Optional reason/evidence prose survives in full-entry reads, but no mandatory rationale field guarantees it. Source: SRC-1 `infer/src/contextpilot.py:617-703`; SRC-2 `infer/configs/fsm_plan_bm25_mc_prompt.txt:5-12,19-28`. Rejection is structural/missing-key or invalid-mode behavior, not an established truth gate. Recovery from overwrite/delete is not an inspected version-rollback path. Effect persists within this question/rollout and its continuations; subsequent read/update determines salience.

Theory fields: model-authored statement formulation afforded, actual formulation uninspected; supplied statements' operative semantic use uninspected, content-directed criticism uninspected, resulting revision/changed reliance uninspected, criticism-attributable improved capacity uninspected. Runtime delivery/edit effects are wired independently. Structured fields and addressable keys expose separately editable content; that partial addressability does not establish an explanatory theory.

RTE-6 — automatic catalog supply. Every inference payload construction reads all current key/summary pairs and appends them to the first user message. Training rendering does the same. Trigger: next payload/render; selection: whole available stores; budget: no per-store or per-catalog truncation in these methods. Later consumer: task model via user-message context. Direction: push; signal: coarse. Status: wired. SRC-1 `infer/src/contextpilot.py:705-708,747-749,2462-2483`; `train/verl/experimental/agent_loop/statelm_agent_loop.py:128-188,839-862`.

>         external_memory_summary = (
>             f"\n\n<external_memory>\n## Available Memories\n"
>             f"{self.state_manager.get_notes_summary()}"
>             f"\n</external_memory>"
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>                 if inject_retry_hint and idx == 0 and self._retry_hint:
>                     text += self._retry_hint
>                 text += (external_context_summary if idx == 0 else "")
>                 messages.append({"role": "user", "content": text})
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

RTE-7 — context transformation and replay. Model tool calls select an assistant/tool message by ID, then delete, extract an exact span, provide a summary or request external compression. Runtime cleanup also selects old search/read/plan messages. Overlay maps persist to all subsequent payload builds; consumer CMP-2 receives the selected replacement or original message. Automatic assembly uses ID matches, with coarse chronological budget filtering. Content is advisory; overlay membership enforces inclusion. Requested restoration is a callable affordance, not advertised in the shipped catalog. Source and status: wired editing/replay, afforded restoration; SRC-1 `infer/src/contextpilot.py:2499-2505,2592-2619,2783-2947,2985-3068,3207-3316`; `infer/src/contextpilot_fsm.py:414-525`. Training equivalents render overlays into tokenized prompts after tool boundaries: SRC-1 `train/verl/tools/statelm_tools.py:744-827,893-939`; `train/verl/experimental/agent_loop/statelm_agent_loop.py:1843-1887`.

>                 replacement_text = None
>                 if msg_id in self.deleted_msg_ids:
>                     replacement_text = STUB_MESSAGE
>                 elif msg_id in self.summarized_msg_ids:
>                     replacement_text = self.summarized_msg_ids[msg_id]
>                 elif msg_id in self.truncated_msg_ids:
>                     replacement_text = self.truncated_msg_ids[msg_id]
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>             restored_from = []
>             if msg_id_int in self.deleted_msg_ids:
>                 self.deleted_msg_ids.discard(msg_id_int)
>                 restored_from.append("deleteContext")
>             if msg_id_int in self.truncated_msg_ids:
>                 self.truncated_msg_ids.pop(msg_id_int, None)
>                 restored_from.append("truncateContext")
>             if msg_id_int in self.summarized_msg_ids:
>                 self.summarized_msg_ids.pop(msg_id_int, None)
>                 if msg_id_int in self.compressed_msg_ids:
>                     restored_from.append("compressContext")
>                 else:
>                     restored_from.append("summarizeContext")
>             self.compressed_msg_ids.discard(msg_id_int)
>             self.restorable_msg_ids.discard(msg_id_int)
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>             try:
>                 compressed_body = self._compress_context_with_llmlingua2(text, compression_rate)
>             except Exception as exc:
>                 fallback_used = True
>                 error_message = f"{type(exc).__name__}: {exc}"
>                 compressed_body = self._fallback_compress_text(text, compression_rate)
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>         sampled_indices = sorted(random.sample(range(len(words)), keep_count))
>         return " ".join(words[i] for i in sampled_indices)
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

>             summary = "[Original long context has been summarized to the following message to save space.]\nSummarized Content: \n" + summary
> 
>             self.summarized_msg_ids[int(msg_id)] = summary
>             self.compressed_msg_ids.discard(int(msg_id))
> 
>             self.restorable_msg_ids.add(int(msg_id))
>             return {"status": "success", "msg_id": int(msg_id), "summary_length": len(summary)}
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Admission: exact message ID and allowed role, with FSM eligibility where applicable; truncation requires literal start/stop strings, whereas supplied summary needs supported role/non-null content. Remote compression output is accepted as replacement; failure falls back to random words in original order. Runtime membership maps determine later replacement, not a semantic-fidelity check. Original full_history persists but restoration requires eligibility, and restoreContext is omitted from the default tool catalog. Token-window deletion directly marks deleted IDs without restoring eligibility, so not every hidden message is recoverable through that tool. The first-user catalog can remain large even after all assistant turns are removed. Source: SRC-1 `infer/src/contextpilot.py:2705-2760,2783-2947,3273-3279`; source catalog `infer/tools/context-shaper_tools.json:1-484`.

Guidance: static context-budget instructions and model judgment of relevant content, with retained plan strategy optionally giving progress/gaps/reasons in tool-call arguments. Strategies are read back until hidden. Relation_reason describes linkage, not why the content is true. Generated summaries/plans are possible theory-bearing content with formulation afforded; actual formulation, operative theoretical use, criticism, criticism-driven revision and resulting capacity gain remain uninspected separately. Automatic replacement and later contextual delivery are wired. Invalidation is active-view removal/replacement, not epistemic refutation. No demonstrated behavioral activation is inferred.

RTE-8 — partial-rollout capture, selection and continuation. Producer: training loop captures pre-action checkpoint and cloned AgentData, and stores context-length delta plus subsequent model uncertainty. Automatic selector ranks sensitivity within a query's retained-snapshot budget, then sends selected branch state to continuation workers. Consumer: the resumed generation loop and RTE-2 training pipeline. Persistence: in-memory for that query's branching/reward stage; optional dumps are not required for replay. Form: natural-language contents plus symbolic execution state. Status: wired. SRC-1 `train/verl/experimental/agent_loop/statelm_agent_loop.py:1568-1658,1780-1807,1893-1904`; `train/verl/experimental/agent_loop/agent_loop.py:780-810,842-873`. This is push by an automatic numeric selector, not a model's requested memory read.

>         initial_snapshot_count = sum(len(outputs) for outputs in selected_by_run.values())
>         remaining_budget = max(0, int(self._cp_snapshot_budget) - initial_snapshot_count)
>         ranked = sorted(
>             candidates,
>             key=lambda item: float(item[0].get("sensitivity", float("-inf"))),
>             reverse=True,
>         )
>         partial_branch_budget = remaining_budget // 5
>         selected_candidates = ranked[:partial_branch_budget]
> --- `train/verl/experimental/agent_loop/agent_loop.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Distinct memory annotation of RTE-2, not a second training-update executor. Raw state copying and replay are memory use, not alone distilled learning; qualifying trained artifacts and feedback guidance are described on RTE-2 and other writes. Activation requires selected training loop/dataset/config as on RTE-2. Branches inherit copies of task memory; their normalized reward row is OBJ-3, separately from replayable OBJ-8. Return is trajectory output; branch failure and cleanup are bounded by RTE-2 and the source's finally cleanup, not a cross-process recovery guarantee.

RTE-9 — mergeNotes. The base dispatcher can call the implementation, but the shipped catalog does not advertise it and no automatic caller was established. It concatenates existing summaries/full contents, removes inputs and their graph caches, writes a minimal merged record and does not reindex that output. Source provenance, structured fields and timestamps are not carried over. Status: afforded; do not characterize as semantic deduplication or novel synthesis. SRC-1 `infer/src/contextpilot.py:679-703,1993-1998,2949-2951`; SRC-2 `infer/tools/context-shaper_tools.json:1-484` (complete catalog inspected).

>         if notes_to_merge:
>             merged_key = new_key or "_".join([note[0] for note in notes_to_merge])
>             existing_summary = new_summary or "  ".join([note[1] for note in notes_to_merge])
>             merged_content = "\n".join([note[2] for note in notes_to_merge])
> 
>             self.notes[merged_key] = {"summary": str(existing_summary), "full_content": str(merged_content)}
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Admission requires an explicit method/tool-capability request supplying keys. Missing entries are ignored by collection; if any selected entries remain, their concatenated text is written and source entries removed. No semantic comparison, truth gate or versioned rollback is established in this function. Current callable consumers require a configured catalog/host enabling the method; default model invocation is not wired to it. Content is non-ampliative concatenation except a caller-supplied new summary whose semantics remain uninspected. Formulated theory or criticism is not established by this operation; optional reasons may be lost alongside structured provenance. The source-native force is mutation of the task memory store.

RTE-10 — automatic mandatory read after model API failure. In FSM note/memory review states, failed generation triggers deterministic selection of the last inserted key, execution of readNote/loadMemory, and insertion of synthetic assistant/tool records for the next turn. Consumer: CMP-2; persistence: current history. This is push despite using the same tool implementation as requested pull. Selection is coarse recency plus key lookup; the memory variant also automatically includes related entries scored by deterministic overlap and optional embeddings. Status: wired. SRC-1 `infer/src/contextpilot_fsm.py:980-1034`; related-entry scoring SRC-1 `infer/src/contextpilot.py:460-615`.

>                     if mandatory_action is not None:
>                         if mandatory_store:
>                             key = str(list(mandatory_store.keys())[-1])
>                             auto_params = {"key": key}
>                             auto_result = self._execute_tool(mandatory_action, auto_params)
> --- `infer/src/contextpilot_fsm.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

This deterministic recovery is conditional on API failure in mandatory review state and store nonemptiness. The host, not the model, chooses the key; empty store advances to review. Returned content becomes synthetic tool context and flags advance the FSM. Store insertion order is not necessarily latest semantic update. Successful delivery is the criterion, without an answer oracle or content-acceptance decision. Neighbor summaries inherit their memory source limits; no observed model activation or efficacy is established.

### Claims

CLM-1 — context planning, structured memory and soft offloading produce stronger performance with compact working context. Reported-operation conclusion status: claimed, SRC-2 `README.md:36-43`. Memory/control implementation can be checked; actual comparative outcomes and component effects remain uninspected. No primary experimental run is part of this boundary.

> ContextPilot extends context management with planning, structured memory, and
> soft context offloading. Its context-aware partial rollout focuses exploration
> on sensitive context-editing decisions, while fine-grained credit assignment
> trains intermediate snapshots using the outcomes of their downstream
> branches.
> --- `README.md` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

CLM-2 — fine-grained credit for sensitive context-editing decisions. Design conclusion status: claimed; implemented arithmetic/branching conclusion status: wired, via RTE-2. Sensitivity selects sampled pre-action continuations; mean subtree rewards license an optimization signal, not causal attribution to the correctness of each stored statement. Source: SRC-2 `README.md:37-40`; SRC-1 `train/verl/experimental/agent_loop/agent_loop.py:652-708,780-810`, `train/verl/trainer/contextpilot/adv.py:23-72`.

CLM-3 — procedure names such as review, plan and long-term memory require path-specific interpretation. `plan` validates nonempty strategy; mandatory review can be completed by automatic loading after API failure; semantic comparison against the original document is policy rather than a demonstrated guarantee. Source: SRC-1 `infer/src/contextpilot.py:2963-2982`, `infer/src/contextpilot_fsm.py:992-1034`; SRC-2 `infer/configs/fsm_plan_bm25_mc_prompt.txt:9-12,27-28`. These controls are wired; semantic warrant and benefit remain uninspected. Memory horizon comes from actual object lifecycle below, not this vocabulary.

CLM-4 — faithfulness and outcome evidence. SRC-2 `README.md:36-43` claims more compact context and stronger benchmark performance. The inspected snapshot tests assert state/token/mask mechanics, not answer dependence on recalled claims: SRC-1 `train/tests/experimental/agent_loop/test_contextpilot_partial_rollout.py:57-112`. Neither was executed here, and no retained dependence experiment was inspected. This prevents an observed or causally supported faithfulness classification; it does not negate the wired learning and delivery paths.

### Evidenced absences

No parent-origin ABS record: missing deployment, semantic and causal evidence is retained as a limitation, not a claim that no such behavior can occur. Specialist bounded absence records, if warranted, are integrated below.

None added: inventory-level catalog omissions and uninspected runtime outcomes remain explicitly bounded on their affected records, without a system-wide absence claim.

### Behavioral-authority paths

BAP-1 — inference dispatch: CMP-1 consumes configured schemas, FSM state, returned tool name/arguments and budget state; symbolic checks enforce local admission, static prompt instructs CMP-2, tool responses supply task evidence. Horizon current question; RTE-1 and RTE-4 distinguish enforced available set from offered schemas. Source: SRC-1 `infer/src/contextpilot_fsm.py:1092-1180`, `infer/src/contextpilot.py:3514-3529`; SRC-2 `infer/configs/fsm_plan_bm25_mc_prompt.txt:1-28`.

BAP-2 — training feedback: CMP-3 consumes descendant rewards and normalized response-mask advantage through optimization loss. Force learning/ranking over training samples and parameters; horizon successive rollouts, checkpoints and selected deployments. This operational force grants no universal epistemic authority to intermediate notes or explanations. SRC-1 RTE-2 anchors.

BAP-3 — external evaluation: score file and per-sample annotations can inform operator comparison; programmatic effect in optional failed-sample selection and retry hint, but no inspected production admission gate. Horizon evaluator output plus requested rerun; reference answer is authoritative only for the declared benchmark metric. SRC-1 RTE-3 anchors.

BAP-4 — task model reads OBJ-5 full entries and OBJ-6 related summaries through requested key calls (RTE-5), or receives automatic recovery read (RTE-10). Force knowledge, with scored neighbors ranking; current question/rollout horizon. Source-native reasons and source pointers are retained assertions, not validated evidence.

BAP-5 — task model receives all current note/memory catalogs through first-user context, RTE-6; force knowledge and routing through available-key decisions, not relevance endorsement. Horizon later turns while store entries exist.

BAP-6 — active payload renderer consumes keyed overlays over OBJ-7, RTE-7; force enforcement of inclusion/replacement. Task model consumes resulting prose as evidence or instruction. Horizon later payloads; old captured snapshots retain their earlier view.

BAP-7 — training continuation worker consumes selected OBJ-8 clone through RTE-8, then RTE-2 uses descendant results; force routing/ranking over exploration and learning only at the subsequent actor update. Horizon same-query branching then cross-task actor reuse.

BAP-8 — optional merge consumer mutates OBJ-5 through RTE-9; force memory content/availability change, no epistemic endorsement. Scope task store under enabled method interface. SRC-1 anchors inherited from these canonical routes.

## Runtime account

Ordinary invocation is the task launcher selecting a checkpoint/tokenizer, default tool/prompt configurations, OpenAI-compatible generation endpoint and Elasticsearch. Dataset adapters extract question and document; per-item fresh agent starts the FSM sequence. Model decisions are nested within symbolic state eligibility and deterministic recovery. Tools acquire corpus evidence, write selected material and edit active context. The result may be `finish` answer or fallback text after incomplete execution; evaluator persists it and applies its own answer metric. Parallel evaluator workers coordinate question assignment, not shared reasoning. Optional endpoint sharding maps worker rank modulo configured endpoints; it does not establish equal model identity across them.

The available default catalog has 18 named document/memory/context functions; actual grants at a turn are the filtered subset, except full-catalog fallback. Callable optional methods and modified catalogs are separate paths. There is no source-based claim of global tenant isolation or secure execution of arbitrary caller-supplied Python imports: launcher/configuration authority belongs to the operator and host. Training is a separate bounded curriculum with GPU/service dependencies. It changes the actor through sampled continuations and reward-based optimization; rollout budgets limit exploration, not the truth of every generated claim.

Forcing cases, statically inspected:

| case | consequence / enforcement and limit | records |
|---|---|---|
| model returns hidden tool | FSM rejects outside `allowed_names`; base loop checks only configured catalog; missing state schemas can expose full catalog | RTE-1, RTE-4 |
| context exceeds token window | earliest eligible assistant/tool pairs stubbed; if no eligible assistant remains it breaks and returns possibly over-limit payload; provider overflow recovery may delete more or return error | CMP-1 and integrated memory routes |
| partial snapshot has no terminal descendants | flagged drop rather than fabricated reward; branch failure excluded; group budget caps retained training rows, not a quality guarantee | RTE-2 |
| open-ended training judge fails | fallback lowercase exact comparison changes criterion; parameter update can proceed from that reward, bounded by numerical-gradient veto rather than demonstrated semantic correctness | RTE-2 |

Token-budget owner is the host renderer; guarantee strength best effort because exhaustion can return an oversized payload. Source: SRC-1 `infer/src/contextpilot.py:3207-3316`.

> if asst_idx is None:
>     print("[TOKEN_WINDOW] No more assistant turns available to stub.")
>     break
> --- `infer/src/contextpilot.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Judge fallback source: SRC-1 `train/verl/utils/reward_score/statelm_qa.py:145-160`.

> except Exception as e:
>     logger.warning("LLM judge error: %s", e)
>     pred_normalized = prediction.lower().strip()
>     gt_normalized = ground_truth.lower().strip()
>     return pred_normalized == gt_normalized
> --- `train/verl/utils/reward_score/statelm_qa.py` @ `782cbb6611fb610c4cf6fafda6022b7e89cae191`

Execution disposition: no dynamic check planned. Considered an FSM rejection fixture, compressor-failure run and small training rollout. Static branches suffice to characterize the local admission/return behavior; live runs would require unprovided endpoint/services/model/data/GPU configuration and would not establish broader efficacy. No check was attempted and no negative runtime finding is inferred from nonexecution.

## Lens scoping

### Memory/context scope

Full depth. Trigger SRC-2 CLM-1 plus SRC-1 StateManager, context transformations, branch snapshots and checkpoints. Scope includes use-accumulated notes, histories, context edits, relation/access structures, training snapshots and learned actor state; separates imported corpus from derived memory. Default FSM/base alternatives, training continuation and optional interfaces are included with distinct evidence strengths. Frozen input and fresh specialist govern classifications; external pretrained/provider-internal state, uninspected remote services and diagnostic-only bytes are excluded from asserted memory semantics.

### Epistemic scope

Full depth. Trigger OBJ-2 answer production, derived memory and RTE-2 score-driven policy update. Assess imported corpus/labels, plan/note/summary transformation, operational checks, answer scoring, branch reward derivation, parameter update and recovery. Not a full audit of every vendored verl feature or external benchmark label. No candidate-linked primary outcome or model-weight probe; semantic preservation, individual theoretical content and causal improvement cannot be inferred from code paths alone. Standalone epistemic procedure executed locally as sparse overlay on canonical records.

## Lens outputs

### Memory/context lens

The specialist inventories OBJ-5 task content, OBJ-6 access structures, OBJ-7 history/overlays/plans and OBJ-8 replay/snapshot state, alongside OBJ-3 training rows, OBJ-4 learned parameters and the imported retry record on RTE-3. The implemented note library is external to the model prompt but task-local in the evaluator: a fresh agent is created per sample. The actor-training path can carry updates across tasks; its activation is conditional on dataset/configuration selecting the registered ContextPilot loop. Reusing an agent object's run method is not evidence of a supported cross-task note library because counters reset while stores/history can remain.

Normal full-entry reads are pull. Appended related summaries remain part of the requested result. Automatic catalogs and active context assembly are push; API-failure recovery separately makes a host-selected read and its neighbor selection push. Optional embeddings can influence the memory graph even though document-vector tools are absent from the default catalog. Reranking inspected here acts on imported document candidates and contributes no extra memory-ranking route. Deprecated enable_graph/M-Flow is ignored while the internal relation graph remains implemented; those are different mechanisms.

Context compaction is included as a learning write when a trace-fed summary/compression replacement persists and reaches later calls. RTE-5 derived notes/plans, RTE-7 continuation replacements and RTE-3 transformed prior-outcome hints supply per-task online guidance; RTE-2 supplies staged cross-task parameter updates, with RTE-8 branch memory feeding that process. Raw logging/copying alone is not classified as distilled learning. Stored natural language, structured relation/edit fields and learned parameters support the reported form union. Static prompts and incoming corpus indexes are outside it.

All fourteen comparison axes preserve the specialist's scope and weakest-basis aggregation. Callable merge lowers curation support to afforded; known operations are consolidation, decay and evolution at their stated meanings, not semantic dedup or claim synthesis. Complete read-back signal is not determinable: inference has known coarse/identifier/lexical/optional embedding selectors, while numeric context/entropy sensitivity for branch replay lacks an exact controlled mapping. Faithfulness tested is separately not determinable, CLM-4. Neither uncertainty is a blocker or a negative efficacy finding.

### Epistemic lens

#### 1. Source-and-claim boundary

ContextPilot at the reviewed commit; supplied SRC-1 implementation and SRC-2 doctrine/reported claims are the entire source register. Scope is the declared repository-owned inference and conditional training arrangement. Assessed families: acquisition of task evidence, answer production, plan/note/summary transformations, read selection, context-view mutation, operational gates, answer scoring, descendant-reward derivation, policy adaptation and replay/recovery. Excluded remote internals, uninspected dataset/weight contents and generic framework routes prevent whole-deployment claims, reference truth guarantees and achieved-learning conclusions. Question: what content is produced, what checks warrant reliance, and what changes behavior? Consequential claims are CLM-1, CLM-2 and CLM-3; CLM-4 limits dependence evidence. No actual candidate-linked run is available.

#### 2. Epistemic-object inventory

The table overlays canonical identities; source/producer/consumer/form/storage remain as registered. All rows are implementation-backed possibilities, not observed candidate contents.

| object/part | candidate truth-apt content / role | lineage and warrant limit |
|---|---|---|
| OBJ-1 corpus/labels | source statements and benchmark expected answers | acquisition/import; source truth and annotation validity uninspected; actors receive corpus while evaluators receive labels |
| OBJ-2 answer | assertion answering the supplied question | model-generated from selected context; possible retrieval, deduction or conjecture cannot be determined for all outputs |
| OBJ-3 reward/mask/lineage rows | arithmetic subtree mean and grouping claims within defined data; tokens can contain embedded assertions | derived metadata follows supplied scores; scores inherit evaluator limits, not blanket warrant for all token content |
| OBJ-4 parameters/checkpoint | no individuated truth-apt candidate established by inspection | learned policy and restoration state; probing would be needed to identify semantic claims |
| OBJ-5 structured memories | facts, relations, episodes and source/evidence assertions | model supplies content; normalization/source-field retention does not verify claims or citations |
| OBJ-5 simple notes | freely stated findings or procedural guidance | same model-derived input, with fewer structured provenance fields |
| OBJ-6 access caches/edges | similarity/linkage scores and reasons, not truth of remembered content | deterministic overlap/optional vector computation; reasons explain linkage, not evidential validity |
| OBJ-7 raw history | acquired tool observations and model assertions | preserves execution content; logging does not validate embedded claims |
| OBJ-7 plan strategy | procedural intentions plus possible factual progress/gap assertions | model-supplied and later readable, content-preservation/criticism not established by nonempty-string gate |
| OBJ-7 replacement prose | supplied summary or compressor-produced account of a prior message | semantic preservation indeterminate; random-word fallback can omit qualifiers; raw source persists separately |
| OBJ-7 masks/views | no candidate claim in the edit-membership set itself | symbolic inclusion policy acts on payload without deciding truth |
| OBJ-8 replay state/snapshots | acquired history/prompt state with embedded content inherited from originals | copying and replay preserve data structures, not a new warrant for their claims |

#### 3. Authority-route ledger

All rows use canonical consumer/channel/horizon and source anchors from the named route and BAP records. Every row's architectural status is `implemented` except the explicitly afforded catalog-dependent branch whose underlying method is also implemented but activation is conditional. No observed candidate state or behavioral effect is inferred. Conditions below are activation/selection conditions; content and operational licenses differ.

| route/function | architectural status | target and content/update relation | condition/evaluator domain; timing and result | epistemic license / implemented force and limit |
|---|---|---|---|---|
| RTE-1: content transformation | implemented | OBJ-2 and OBJ-7 plan; truth-apt transformation: indeterminate | CMP-2 generates from current task context on turn | candidate answer/progress claim or prescription; BAP-1 delivers selected tool action, no truth warranty |
| RTE-1: check/evidence production | implemented | tool name, message target, nonempty plan; no content change | FSM/syntax checks before dispatch; permitted/error | establishes local admissibility only; not sufficient evidence or correct planning |
| RTE-1: disposition/acceptance | implemented | action; non-truth-apt policy/content update: next execution state | allowed-name check and state transitions; rejected action not executed | operational admission, BAP-1; fallback full catalog narrows state-order guarantee |
| RTE-1: operational admission/selection/consumption | implemented | OBJ-2 final answer; no content change | finish or terminal extraction after limits/errors | answer returned even without answer-verification gate; result availability is not epistemic acceptance |
| RTE-4: operational admission/selection/consumption | implemented | selected tool; no content change | configured-name check, not offered-name check | broader operational grant on alternate path; BAP-1, no extra truth license |
| RTE-3: check/evidence production | implemented | OBJ-2; no content change | benchmark reference and string/LLM metric after return | score is benchmark-relative match, not validation of generating explanations or context retention |
| RTE-3: retention | implemented | answers/scores/traces; no content change | output files on each evaluated item | inspectable record, BAP-3 operator evidence; not post-acceptance integration |
| RTE-3: content transformation | implemented | prior wrong-answer record to retry hint; truth-apt transformation: non-ampliative reshaping | configured failed file and exact sample match | preserves supplied assertion of failure, adds procedural search instruction; file verdict is trusted |
| RTE-3: operational admission/selection/consumption | implemented | retained retry hint; no content change | next requested attempt user-context insertion | BAP-3/BAP-1 instructs another approach for same task; improvement unobserved |
| RTE-5: content transformation | implemented | OBJ-5 entry; truth-apt transformation: indeterminate | model selects observations and states facts/relations/summary | may reshape, derive or conjecture; no content-specific claim check established |
| RTE-5: check/evidence production | implemented | write/update structure; no content change | normalization, key/mode checks | data-shape license only; pointer/prose evidence may remain unsupported |
| RTE-5: disposition/acceptance | implemented | OBJ-5 store mutation; non-truth-apt policy/content update: store membership | accepted writer invocation overwrites/appends/removes | operational memory admission, BAP-4; not epistemic acceptance of entry |
| RTE-5: retention | implemented | OBJ-5 plus OBJ-6 caches; no additional content change | current task/rollout dictionary and reindex | available for later reliance; old overwritten content not separately versioned |
| RTE-5: operational admission/selection/consumption | implemented | requested full entry and related summaries; no content change | task-model key request, neighbor ranking | BAP-4 knowledge/ranking; similarity and successful delivery do not warrant factual use |
| RTE-6: operational admission/selection/consumption | implemented | all key/summary pairs; no content change | next payload, complete available catalog | BAP-5 automatic presence, no relevance or truth endorsement; no catalog-specific bound |
| RTE-7: content transformation | implemented | OBJ-7 summary/compression; truth-apt transformation: indeterminate | model-supplied text or external compressor/random fallback | preservation not established; copied exact span retains only selected passage's warrant |
| RTE-7: check/evidence production | implemented | target eligibility and literal bounds; no content change | role/ID/FSM and start/stop membership checks | proves a selectable span/target, not semantic completeness |
| RTE-7: disposition/acceptance | implemented | active overlay; non-truth-apt policy/content update: payload membership | edit admitted, maps altered, optional restoration clears maps | BAP-6 governs subsequent visible context; deletion is not refutation |
| RTE-7: retention | implemented | raw history plus overlays; no additional content change | retain originals and selected replacement/mask | recovery capability is partial/catalog dependent, not content acceptance |
| RTE-7: operational admission/selection/consumption | implemented | rendered history/replacement; no content change | ID matching and chronological budget cleanup before call | BAP-6 replaces delivered content; observed activation and faithfulness unresolved |
| RTE-8: lineage/freshness/recovery | implemented | OBJ-8 branch clone; truth-apt transformation: non-ampliative reshaping | pre-action copy and selected continuation | execution-state lineage, not renewed truth of embedded assertions |
| RTE-8: operational admission/selection/consumption | implemented | chosen branch state; no content change | numeric sensitivity budget plus loop-selection prerequisite | BAP-7 chooses exploration input; sampled contrast not causal proof of an intermediate claim |
| RTE-9: content transformation | implemented | merged OBJ-5; truth-apt transformation: non-ampliative reshaping | callable merge concatenates selected entries; caller summary is indeterminate | text combination drops structured provenance; no semantic dedup/novel warrant |
| RTE-9: disposition/acceptance | implemented | task store; non-truth-apt policy/content update: replace source entries | nonempty selected set under enabled method | BAP-8 mutates membership, catalog default does not advertise it |
| RTE-10: operational admission/selection/consumption | implemented | latest inserted key and related summaries; no content change | API failure in mandatory review and nonempty store | BAP-4 host-selected evidence delivery; success advances review without semantic checking |
| RTE-2: check/evidence production | implemented | terminal answer/format/budget; no content change | reference match or judge plus penalties | criterion-specific reward; oracle source truth and judge quality uninspected |
| RTE-2: content transformation | implemented | OBJ-3 subtree mean/advantage; truth-apt transformation: entailed derivation | descendant linkage, arithmetic mean and query normalization | exact arithmetic scope only, given input scores; not causal credit or theory validation |
| RTE-2: disposition/acceptance | implemented | eligible training rows; non-truth-apt policy/content update: sample selection | branch/range/mask checks; missing descendants dropped | BAP-2 admits optimization samples, not acceptance of embedded text |
| RTE-2: behavior/policy adaptation | implemented | OBJ-4; non-truth-apt policy/content update: actor parameters | scored loss, gradient clipping and finite-norm step | BAP-2 learning force across subsequent rollouts; capacity gain remains unobserved |
| RTE-2: retention | implemented | OBJ-4 checkpoint; no content change | scheduled save of configured contents | recoverable model state, not a quality-selected successor |
| RTE-2: lineage/freshness/recovery | implemented | OBJ-4 restored state; no content change | latest/explicit checkpoint path and contents | restored parameters/dataloader; default optimizer omission limits exact continuation |

RTE-1/RTE-4 checks act before task effects; RTE-3 scoring acts after answer return; RTE-2 reward acts before gradient update, while validation/checkpoint scheduling follows it. These time/order differences prevent assigning one system-wide evaluator or admission guarantee. Truth of an intermediate note is not established by answer success, related-entry score, format pass or nonfinite-gradient veto. No ledger retention row asserts lifecycle integration after epistemic acceptance.

#### 4. Per-object lifecycle disposition

OBJ-1: truth-apt transformation acquisition/import on RTE-1/RTE-2 inputs; discovery lifecycle not applicable to importing documents/reference answers. Their origin and correctness require external evidence. OBJ-2: transformation indeterminate among extractive reshaping, entailed answer and ampliative conjecture. RTE-1 generation and RTE-3/RTE-2 answer checks are implemented, but the semantic class and derivation/criticism cannot be determined without a particular candidate. Observed candidate state: no instance observed. Possible benchmark acceptance is scoped to an expected-answer criterion; no candidate-linked post-acceptance integration was observed.

OBJ-3: score/advantage metadata is an entailed arithmetic derivation on RTE-2 within its explicit inputs and numerical conventions; discovery lifecycle not applicable. Embedded trajectory claims retain their original unresolved status. No lifecycle record for OBJ-4: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-2. No individually stated proposition is inferred from unprobed parameter tensors.

OBJ-5: transformation indeterminate on RTE-5 among preserving source content, deriving a relation and making a new claim. Source pointers and text retain lineage hints; runtime normalization/admission/read-back do not settle preservation or entailment. RTE-9 concatenation is non-ampliative for copied text; optional replacement summary remains indeterminate, and provenance loss limits later warrant assessment. Observed candidate state: no instance observed. Candidate-linked source passages, proposed relations, criticisms and ensuing reliance would be needed to assign an ampliative lifecycle.

OBJ-6: access metadata is an entailed computation under symbolic overlap/vector-score definitions, with model-vector semantics uninspected; discovery lifecycle not applicable to calculating scores. Linkage reasons do not derive truth of the linked claims. OBJ-7 raw records are acquisition/import; plan/summary/compressor text is indeterminate between faithful reshaping, unsupported omission and new interpretation. Exact-span extraction is non-ampliative selection and retains only that selected passage's scope. No lifecycle record for OBJ-7 edit-membership masks: no candidate truth-apt output for this object part; relevant direct-adaptation or update routes: RTE-7. Semantic checks of replacement content are not established by syntactic eligibility. OBJ-8 copying/replay is non-ampliative reshaping/restoration on RTE-8, so discovery lifecycle not applicable; inherited embedded assertions receive no new warrant.

For all potential ampliative candidates in OBJ-2, OBJ-5 and OBJ-7: content-producing interfaces are implemented, but semantic conjecture classification, derived consequence, content-directed test, epistemic acceptance and post-acceptance lifecycle integration have architectural status not determinable at that semantic level and observed candidate state no instance observed. This does not erase implemented operational scoring/admission. It prevents upgrading available code paths into observed theory criticism or criticism-driven improvement.

#### 5. System-claim versus route comparison

| claim | doctrine/reported operation | implemented support | observed/causal evidence and bounded conclusion |
|---|---|---|---|
| CLM-1 | README reports stronger performance with compact context | RTE-5, RTE-6, RTE-7, RTE-8 and RTE-2 connect memory/editing/training | no run/intervention here; mechanism wired, aggregate gain claimed |
| CLM-2 | sensitive-decision exploration and fine-grained credit | RTE-8 numeric sensitivity selection; RTE-2 descendant mean/query-normalized learning signal | no observed matched contrast; proxy exploration/credit arithmetic supported, isolated causal action effect uninspected |
| CLM-3 | plan/review/long-term-memory wording suggests substantive capabilities | RTE-1 string validation, RTE-5 task-local stores, RTE-10 deterministic delivery | those local functions are implemented; semantic review, safe cross-task library and warranted explanations not established |
| CLM-4 | faithfulness gap bounds broader efficacy reading | test-source mechanics and retained comparison uncertainty | no executed dependence evidence; not a proved absence of faithful recall |

#### 6. Bounded conclusion

The system acquires task documents and retains model-derived interpretations with explicit access and context control. It can keep source pointers and raw messages while presenting only summaries, but some mutation branches lose provenance and some hidden originals lack advertised restoration. No transformation grants universal warrant to its output. Answer labels/judges license benchmark-relative scores; intermediate-memory truth remains a separate question.

Training directly adapts a policy using selected continuations and outcome-derived advantages. Its arithmetic and admission mechanics are inspectable, while causal contribution of a particular edit and improved future capacity are unobserved. Theory-bearing text and editable fields afford formulation/revision; an actual operative theory's content-directed criticism and benefit remain uninspected. This is a route-level account of evidence, retention and adaptation, not a single epistemic grade.


## Reconciliation

The fresh specialist report matches the frozen input SHA-256 `4bbdc67e80b2043d23f8468b3b476035b660f1479e3512b2a9b0ee57be5572a4`, method SHA-256 `7e86ed242caadc095d7f20ccd7fcbcb837b9d62e94fca50656b782c65cb0d675` and source revision. All material findings are retained here. Parent source-checked canonical seed additions OBJ-3, OBJ-4, RTE-2 and RTE-3 reached the specialist through coordination; the input bytes did not change. Specialist rechecked those records against primary source. No independent convergence claim follows from shared anchors.

| proposal | canonical record | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-5 | adopted at stated scope/status |
| MEM-OBJ-2 | OBJ-6 | adopted at stated scope/status |
| MEM-OBJ-3 | OBJ-7 | adopted at stated scope/status |
| MEM-OBJ-4 | OBJ-8 | adopted at stated scope/status |
| MEM-RTE-1 | RTE-5 | adopted at stated scope/status |
| MEM-RTE-2 | RTE-6 | adopted at stated scope/status |
| MEM-RTE-3 | RTE-7 | adopted at stated scope/status |
| MEM-RTE-4 | RTE-8 | adopted at stated scope/status |
| MEM-RTE-5 | RTE-9 | adopted at stated scope/status |
| MEM-RTE-6 | RTE-10 | adopted at stated scope/status |
| MEM-CLM-1 | CLM-4 | adopted at stated scope/status |

All eight integration issues are resolved: content/access/history/replay identities stay distinct; replay state overlaps emitted training rows only through an explicit conversion; generic inference and training executor ownership is preserved; default catalog versus callable affordances retained; metadata loss, compressor fallback, restoration eligibility and token exhaustion preserved; per-task notes distinct from cross-task weights; both comparison uncertainties retained; dataset-dependent training activation attached to the route and profile interpretation. CMP-5 superseded by three separately identified auxiliary-model records. Parent added generic admission/return/theory-status fields without upgrading memory findings. No unresolved conflict or source-access blocker remains. Source quotes are retained once on supporting records; duplicate overlapping passages from the report are subsumed there.

## Bounded synthesis

ContextPilot connects use-accumulated evidence to later task calls through explicit context and memory control, then offers a separate trace-fed parameter-learning path. Its defining operational feature is the combination of model-supplied content with symbolic sequencing and deterministic recovery. A model can select what to remember and how to summarize, while the runtime can force a read or remove earlier context. The implementation does not make every edit or retrieval an autonomous model decision.

Training makes context decisions consequential through alternative continuations, subtree reward means and actor updates. This is a wired route toward improved context management across tasks. Whether it actually improves capacity, preserves relevant memory faithfully, or produces the reported benchmark gains remains uninspected here. The comparison's trace-learning field describes the qualifying writes/updates; it does not by itself establish criticism of an operative formulated theory.

Reflection conclusion status: wired at the inference/training control boundary. Representations of the system's current messages, note availability, selected history and context usage are updated as those aspects change; model or symbolic operations mediated by those representations alter later context and behavior. Revising a self-theory of the theory-building organization is uninspected. Dispositional self-improvement conclusion status: wired for the feedback-driven actor-training arrangement relative to the supplied QA reward and training/checkpoint horizon. Occurrent self-improvement and achieved favorable improvement conclusion statuses: uninspected; no actual updated actor's later operation or interventional benefit was observed.

Conjectural learning conclusion status: uninspected. Source exposes possible theory-bearing text in plans, factual notes and answers, with later consumption and revision affordances. No instance-linked formulated theory, content-directed criticism and improved capacity attributable to holding it open to criticism is established. Parametric policy adaptation is directly evidenced as an implemented update mechanism, without interpreting its contents as individuated theories.

The decisive follow-up evidence would be task-linked raw and edited context, retained facts and predictions, exact loaded model/checkpoint identity, actual descendant outcomes, and matched interventions isolating memory content or editing choices. Those would test whether compactness preserves needed evidence and whether improved outcomes reflect the proposed mechanism. No product ranking or Commonplace transfer is inferred.

## Limitations

| limitation | affected records | inspected boundary | conclusion prevented | resolving evidence |
|---|---|---|---|---|
| no runtime/training experiment | CLM-1, CLM-2, RTE-1, RTE-2 | source/docs only | observed benefits or causal component contribution | retained runs and matched interventions |
| externally supplied model/data identity | CMP-2, CMP-3, CMP-4, OBJ-1 | config/service interfaces | exact weight fixity, independent reference truth | model digests and pinned benchmark provenance |
| alternative control paths | RTE-1, RTE-4 | FSM/base/configurable catalogs | universal workflow or grant guarantee | deployment-specific catalog/profile and executed route evidence |
| transformed-content semantics | memory routes and OBJ-2 | construction/check interfaces | faithful preservation or theory criticism | candidate-linked content and tests |
| external services and generic vendored framework | CMP-3, CMP-6, CMP-7, CMP-8 | selected interfaces only | end-to-end deployment isolation, arbitrary framework guarantees | frozen dependent implementations and deployment validation |
| training loop activation | RTE-2, CMP-3 | registry, generic default and launcher; external dataset uninspected | assurance supplied data selects ContextPilot loop | pinned transformed dataset agent_name and resolved config |
| checkpoint contents and rollout selection | RTE-2, OBJ-3, OBJ-4 | recipe and save/load/update code | exact optimizer continuation, isolated causal action credit | complete checkpoint/config and controlled run |

## Verification and blockers

### Semantic verification

Verified frozen source identity, input/method/report byte identities, canonical mapping and per-route evidence strengths. Sources separate implementation from reported outcomes; no primary run or provider internals were imported. Material alternatives include FSM/default catalog, base loop, catalog-dependent callable merge/restore/document-vector methods, conditional memory embeddings/compressor fallback, per-task inference, wrong-answer retry and selected training-loop activation.

Integrated memory scope matches objects and routes. All qualifying trace-fed writes are retained: notes/plans RTE-5 with history, replacement summaries/compression RTE-7, retry guidance RTE-3 and parameter learning RTE-2 fed by replay RTE-8. Online per-task plus staged cross-task horizons, tool traces/trajectories, and natural-language/symbolic/parametric outputs agree across dependent axes. Raw logs and imported corpus indexes do not independently justify learned memory. Access graph/vectors concern accumulated notes, distinct from document search.

Selectors distinguish requested entry/neighbor pull, whole-catalog push, keyed overlay assembly, retry sample match and deterministic mandatory review. Numeric branch sensitivity remains explicitly outside a complete controlled signal classification; no strongest-value substitution was made. Faithfulness tested remains not determinable. Callable affordances do not become default wiring. Actor training is conditional on registry selection; numerical veto and checkpoint restoration do not establish favorable improvement or complete optimizer continuation.

Admitting routes name guidance, proposer, decision/veto/recovery and oracle limits. Plans and source/evidence prose may retain reasons, but linkage scores, successful reads, answer matches and parameter updates are not upgraded into content-directed criticism or accepted theories. Object lifecycle dispositions keep acquisition, arithmetic derivation, indeterminate transformations and policy updates separate. Reflection and dispositional adaptation wiring are distinct from unobserved actual self-improvement and conjectural learning. No semantic blocker remains.

### Deterministic validation

Exact target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-contextpilot-01/result.md`. `commonplace-validate --full` passed cleanly with no errors or warnings.

### Blockers

None.
