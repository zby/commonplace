---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ReasoningBank memory: trace-derived advice, query-vector selection, system-message delivery and alternative admission limits."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
source-identity: "https://github.com/google-research/reasoning-bank"
reviewed-boundary: "ed80611788292ea739f1effd31f16c53823b8a0d"
---

# ReasoningBank memory report

## Boundary and evidence

This report covers the frozen SRC-1 repository at ed80611788292ea739f1effd31f16c53823b8a0d, including both shipped task-to-advice loops and their alternate memory surfaces. The source identity and scope are those of [boundary](boundary.md#boundary-and-evidence). HEAD and the clean checkout were rechecked before source inspection. Implementation and shipped instructions are the evidence layers; no observed run or causal experiment is supplied.

The memory scope includes task traces, evaluator output, induced advice, query embeddings, temporary delivery files, episode-local scratchpad/history, context shrinking, the scaling variant and the standalone induction script. Provider weights and internal processing, installed BrowserGym persistence, live benchmarks and operator-created initial bank/cache contents are not captured. These limits prevent claims about exact model state, initial content trust, successful execution, behavioral dependence and improvement. The frozen source is readable; uninspected ancillary code is not an access gap.

Direct source reads extended the supplied runtime account. The table distinguishes them from supplied findings. All paths below are SRC-1 commit-relative paths. Coverage is of memory responsibilities, not a complete audit of every vendored adapter.

| Entry point or operation | Source paths and evidence basis | Records or explicit limit |
|---|---|---|
| Web bank reload, top-one selection, file delivery | Direct: `WebArena/run.py`, `WebArena/memory_management.py`, `WebArena/agents/legacy/agent.py` | [MEM-RTE-web-retrieval](#mem-rte-web-retrieval), [MEM-OBJ-web-advice](#mem-obj-web-advice), [MEM-OBJ-delivery-text](#mem-obj-delivery-text) |
| Coding bank reload and system injection | Direct: `third_party/src/minisweagent/run/extra/swebench.py`, `third_party/src/minisweagent/memory/memory_management.py`, `third_party/src/minisweagent/agents/default.py` | [MEM-RTE-coding-retrieval](#mem-rte-coding-retrieval), [MEM-OBJ-coding-advice](#mem-obj-coding-advice) |
| Automatic query-cache initialization and append | Direct: both memory-management files above | [MEM-OBJ-query-cache](#mem-obj-query-cache); initialization of externally supplied nonempty caches remains unknown |
| Web feedback, trace extraction and advice append | Direct: `WebArena/induce_memory.py`, `WebArena/autoeval/evaluate_trajectory.py`, `WebArena/prompts/memory_instruction.py`; supplied evaluator construction | [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [MEM-OBJ-feedback](#mem-obj-feedback), [MEM-OBJ-lineage-ledger](#mem-obj-lineage-ledger) |
| Coding save, judge, generation and append | Direct: batch runner above, `third_party/src/minisweagent/run/utils/save.py`, `third_party/src/minisweagent/memory/instruction.py` | [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission), [MEM-OBJ-trajectory](#mem-obj-trajectory) |
| Scaling induction and read-back | Direct: `WebArena/induce_scaling.py`, `WebArena/utils/clients.py`, parallel instructions; launcher findings supplied | [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling); class invocation and return-shape issues prevent asserting a working combined-advice loop |
| AWM and Synapse alternatives; no-memory mode | Direct: mode branches in `WebArena/induce_memory.py`; pipeline supplied | [MEM-OBJ-web-advice](#mem-obj-web-advice), [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline); failure branches do not initialize appended content |
| Standalone induction CLI | Direct: `third_party/src/minisweagent/memory/induce_memory.py` | [MEM-RTE-standalone-induction](#mem-rte-standalone-induction); imports and arbitrary output destination leave executable invocation and later consumer unresolved |
| Registered CLI versus single-instance runner | Direct: `third_party/pyproject.toml`, `third_party/src/minisweagent/run/mini_extra.py`, `third_party/src/minisweagent/run/extra/swebench_single.py` | Batch dispatch matches supplied runtime. Single-instance path saves a trajectory but does not call the bank retrieval/admission loop in its inspected main function; no automatic advice read-back established there |
| Trajectory inspection by operator | Direct: `third_party/src/minisweagent/run/inspector.py` loading function; dispatch above | [MEM-OBJ-trajectory](#mem-obj-trajectory); display is not agent advice adoption |
| Re-evaluation output | Direct: `WebArena/reeval_memevol_prompt.py` | [MEM-OBJ-feedback](#mem-obj-feedback); separate score report, no bank rewrite or read-back shown |
| Episode scratchpad, filtering, shrinking and separate contexts | Direct: web agent and bounded ranges of `WebArena/agents/legacy/dynamic_prompting.py`, coding agent; output-template findings supplied | [RT-RTE-context-control](runtime.md#rt-rte-context-control); ordinary web runner disables scratchpad display, but optional agent flags expose it |
| Optional response memoization wrapper | Direct: `WebArena/agents/legacy/utils/llm_utils.py` ChatCached and `WebArena/agents/legacy/utils/chat_api.py` factory; targeted name/cache searches | Wrapper affords disk memoization of call/generate inputs at `~/llm-cache`; inspected task-model factory returns provider classes directly, not that wrapper. No shipped activation established; wrapper cache-key/expiry internals uninspected |
| Ancillary provider-native tools, remote executors, other interactive runners and vendored web agents | Supplied runtime inventory; scoped searches of mini/github issue runners, not full inspection | Included but not exhaustively inspected; no universal all-entry-point memory, safety, restoration or context-budget conclusion |

The root greeting executable, illustrations and dependency metadata do not supply additional retained-experience routes in the supplied boundary inventory. No source was added. Neither source labels such as "Updated Memory" nor prompt demands establish content revision or effective use.

## Core ideas

1. **Advice and retrieval keys have separate lifecycles.** Task-model traces and outcome labels feed an induction model; the resulting prose enters a JSONL bank. Query vectors enter a different JSONL cache before induction. Retrieval ranks cached prior queries, not advice content or evidential quality. A query key can therefore survive without any advice record. See [MEM-OBJ-query-cache](#mem-obj-query-cache) and both retrieval routes.
2. **The selected unit is a task record, not a verified memory item.** The ordinary callers request one cached query ID and then deliver every stored `memory_items` block from the first matching record. Blank-line splitting is not Markdown item parsing. Neither item count nor token length is enforced at this delivery boundary. Source passages are retained in [MEM-RTE-web-retrieval](#mem-rte-web-retrieval) and [MEM-RTE-coding-retrieval](#mem-rte-coding-retrieval).
3. **Trace-fed transformation changes the form of later input, not model parameters.** Induction is automatic admission of model-authored natural-language guidance. Failure reflection and generalization are requested, not validated. Advice goes into the next task's system message with relevance discretion; code does not turn it into an execution rule. Admission and behavioral authority are separately established in [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission) and [RT-BAP-system-memory](runtime.md#rt-bap-system-memory).
4. **Retained evidence is not necessarily delivered evidence.** Web bank rows keep thought/action history beside advice, but the task consumer receives advice only. Coding saves a separate transcript, including selected advice in its system message, then omits system messages from judging and induction. The judge's explanation is not passed on by the coding boolean interface. Reasons can appear in generated prose, but preservation and later use of reasons are not guaranteed by the item template.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-web-advice
Label: WebArena memory_items content

Source-native identity: `memory_items` inside website/mode-specific JSONL rows. Representational form: natural language, including model-interpreted procedural text and displayed action examples; substrate: local append-only JSONL bank. This is the content part, separate from row metadata in [MEM-OBJ-lineage-ledger](#mem-obj-lineage-ledger). Distinct from the supplied admission route [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), whose output it is, and the authority path [RT-BAP-system-memory](runtime.md#rt-bap-system-memory), whose input it becomes. No supplied object counterpart.

Lineage: default ReasoningBank mode derives advice from the task query, extracted agent think/action pairs and available autoevaluation explanation. Successful AWM mode derives workflows under a different prompt. Successful Synapse mode stores the formatted query/trajectory itself rather than summarizing it: a raw-derived demonstration alternative, not evidence that every bank row contains generalized reasoning. Action syntax inside stored strings is displayed to a model, not dispatched directly to BrowserGym. Its downstream authority is discretionary system-message advice. See [MEM-RTE-web-retrieval](#mem-rte-web-retrieval). SRC-1, `WebArena/induce_memory.py`.

> elif args.memory_mode == "synapse":
>     if ex['status'] == 'success':
>         generated_memory_item = trajectory
> --- `WebArena/induce_memory.py`

> "memory_items": generated_memory_item.split("\n\n"),
> --- `WebArena/induce_memory.py`

The split can separate headings, examples or paragraphs of one requested item; no item-structure validation follows. Source-native guidance requests concrete recovery procedures and avoidance of literal task strings. Actual conformity and generated rationale are uninspected. External initial bank contents, edits and their approval control are unknown; known subsequent append is software/model controlled.

#### MEM-OBJ-coding-advice
Label: Coding memory_items content

Source-native identity: `memory_items` in `./memory/{model.config.model_name}.jsonl`. Natural-language generated blocks stored on the local filesystem. Lineage is the problem statement plus the saved non-system message transcript under a success/failure instruction selected by the direct judge. Separate from the query/status/ID ledger and the saved raw trajectory. Distinct from [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission), which produces it, and from web advice, whose producer and bank namespace differ. No supplied object counterpart.

The generator splits response text, not a parsed memory-item schema. The next task delivers all blocks of one selected prior task to the task model as system advice; applicability remains the model's choice. No benchmark grade or semantic acceptance gate shapes that append. SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`; guidance in `third_party/src/minisweagent/memory/instruction.py`.

> response = response.text
> if verbose: print(response)
> return response.split("\n\n")
> --- `third_party/src/minisweagent/run/extra/swebench.py`

>   - You must first reflect and think why the trajectory failed, and then summarize what lessons you have learned or strategies to prevent the failure in the future.
> --- `third_party/src/minisweagent/memory/instruction.py`

The request to think about failure does not require retaining a distinct criticism or its blame assignment. Later read-back does not automatically include the raw transcript or judge prompt. Initial imported content and any external editing authority are unresolved, independently of known automatic writes.

#### MEM-OBJ-lineage-ledger
Label: Bank row identity and provenance fields

Source-native identities: `task_id`, `query`, `status`, web `think_list`, `action_list`, `template_id`. Storage: bank JSONL rows beside advice. Symbolic identity/status fields control joins or prompt choice; query and thought/action strings are natural-language/display material. The ledger is not the advice itself or a vector representation. Separate object parts have separate consumers: retrieval compares `task_id`; induction constructs the stored query/trace/status; current task delivery flattens only `memory_items`. These fields record coarse task lineage, not claim-level evidence or a verified justification.

No supplied object counterpart; associated producers are [RT-RTE-web-admission](runtime.md#rt-rte-web-admission) and [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission). Web persistence is witnessed in boundary's induction passage; coding persistence in boundary's lifecycle passage. SRC-1, `WebArena/induce_memory.py`, `third_party/src/minisweagent/run/extra/swebench.py`.

> "think_list": ex["think_list"],
> "action_list": ex["action_list"],
> "status": ex["status"],
> --- `WebArena/induce_memory.py`

The `template_id` comment says deduplication, but the inspected append and selector do not use it to deduplicate. Stored status does not filter retrieval. Scaling's proposed row omits status and trajectory fields, so ordinary-bank provenance must not be attributed to that output. Initial external row provenance is unknown.

#### MEM-OBJ-query-cache
Label: Cached query keys and dense embeddings

Source-native identity: cache row `id`, `text`, `embedding`, in web website/mode or coding model-named `_embeddings.jsonl` files. Storage: local JSONL and normalized tensors in RAM. Distinct operative parts: symbolic ID used for bank join; natural-language query text retained but not used by similarity scoring after load; dense numerical vector consumed by dot-product ranking. Vectors are distributed-parametric representations, not readable summaries of memory-item content. The numerical producer is already [RT-CMP-gemini-embedding](runtime.md#rt-cmp-gemini-embedding), optionally [RT-CMP-qwen-embedding](runtime.md#rt-cmp-qwen-embedding); this object is their cached output, not a duplicate model component.

Both selector copies load the prior cache, embed the current query, append it automatically, and only then rank the old snapshot using an instruction-wrapped query embedding. Code creates an empty cache if absent. Software admits vectors and keys without human per-query review. No task success or advice availability gates this write. Existing cache initialization, model provenance and manual maintenance are unknown; rows do not store an embedding model/version field. SRC-1, `WebArena/memory_management.py`, `third_party/src/minisweagent/memory/memory_management.py`.

> record = {
>     "id": task_id,
>     "text": cur_query,
>     "embedding": q_vec.squeeze(0).tolist(),
> }
> with open(cache_path, "a") as f:
>     f.write(json.dumps(record) + "\n")
> --- `WebArena/memory_management.py`

> scores = (instruct_vec @ cache_emb.T).squeeze(0) * 100.0  # (N,)
> id2score = list(zip(cache_ids, scores.tolist()))
> id2score.sort(key=lambda x: x[1], reverse=True)
> --- `WebArena/memory_management.py`

This is an experience-derived access index: numerical state changes future selection, while task models receive prose, not vectors. Gemini instruction-query scoring remains even when optional Qwen produced cached queries. Compatibility and exact provider version remain unestablished. Duplicate IDs can rank repeatedly; lookup takes the first bank match, not necessarily the newest appended advice. No transaction couples cache admission to bank admission.

#### MEM-OBJ-delivery-text
Label: Selected web memory text file

Source-native identity: `args.memory_path` / `flags.memory_path`. Natural-language text on the local filesystem, regenerated by the runner from selected advice. Distinct from the durable bank: it is overwritten with selected content or emptied on no match. It contains no query/status provenance wrapper beyond whatever generated content itself says. It is a delivery artifact, not a revised knowledge bank. Related supplied authority path: [RT-BAP-system-memory](runtime.md#rt-bap-system-memory); no object counterpart.

The web agent rereads the path for each action. Thus delivered advice can change between steps if an external writer or a concurrent scaling trial overwrites the shared file. That is an implementation exposure, not an observed race. SRC-1, `WebArena/run.py`, `WebArena/agents/legacy/agent.py`.

> with open(args.memory_path, "w") as f:
>     f.write("\n\n".join(mem_items) + "\n")
> --- `WebArena/run.py`

#### MEM-OBJ-trajectory
Label: Retained task trajectory artifacts

Source-native identities: web `step_*.pkl.gz`, `experiment.log`, `summary_info.json`, and coding `*.traj.json` with `messages`/`info`. Substrates: compressed Python serialization, local text and JSON files. Raw task observations/messages/actions are distinct from induced advice; role/step/status/config wrappers are symbolic access metadata, while model/environment text is interpreted content. Serialized web payloads are not opaque unreadable memory: induction unpickles them and extracts a narrow view. Full installed BrowserGym payload schema and persistence implementation are outside the captured implementation.

Distinct from supplied routes [RT-RTE-swe-task](runtime.md#rt-rte-swe-task) and [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), which write or consume them; no supplied object counterpart. Coding saver keeps the agent's messages, including the advice-bearing system message, plus configuration and exit information. Induction explicitly strips system messages; errors before agent construction can yield an empty saved message list. SRC-1, `third_party/src/minisweagent/run/utils/save.py`, `third_party/src/minisweagent/run/extra/swebench.py`.

> data["messages"] = agent.messages
> --- `third_party/src/minisweagent/run/utils/save.py`

Web induction skips unreadable or actionless steps, derives a fallback think string from saved chat output, and retains extracted think/action arrays in its bank. It does not pass full saved page observations to the ordinary induction prompt. SRC-1, `WebArena/induce_memory.py`.

The CLI inspector is a separate later human display consumer, not an automatic task-policy update:

> elif isinstance(data, dict) and "messages" in data:
>     self.messages = data["messages"]
> else:
>     raise ValueError("Unrecognized trajectory format")
>
> self.steps = _messages_to_steps(self.messages)
> --- `third_party/src/minisweagent/run/inspector.py`

Human display establishes an inspection affordance, not content editing or approval. Redo removes stale coding predictions/trajectory before execution; web output rename removes an existing task directory. Neither cleanup retracts already appended advice or cache rows, as distinguished in the supplied task routes.

#### MEM-OBJ-feedback
Label: Evaluation signals and explanations

Source-native identities: web model `_autoeval.json` rows (`gt`, `rm`, `thoughts`), saved summary reward, coding judge response reduced to boolean, and re-evaluation report rows (`old_score`, `new_score`, `reference`, `response`). Local JSON and host RAM; natural-language explanation plus symbolic label/number parts. These are feedback inputs or reports, not selected task advice. No supplied object counterpart; feedback-producing/consuming stages occur in [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission) and [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling).

Web saves explanation and model label separately from benchmark reward. Default induction reads `rm`, adds available `thoughts` to its model input, but does not persist a separate explanation field in the bank. `gt` chooses the prompt from cumulative reward instead. Coding returns a boolean based on the substring `success`; no judge reason is retained in its bank or forwarded to the generator. Neither label certifies correctness. SRC-1, `WebArena/autoeval/evaluate_trajectory.py`, `WebArena/induce_memory.py`, `third_party/src/minisweagent/run/extra/swebench.py`.

> trajectory += f"\n\nThe task {status_label} because: {autoeval_thoughts}"
> --- `WebArena/induce_memory.py`

> if "success" in response:
>     return True
> else:
>     return False
> --- `third_party/src/minisweagent/run/extra/swebench.py`

The separate re-evaluator writes a report at its supplied output path; its inspected main function does not rewrite `summary_info.json`, the bank or cache. Thus new grades are not automatically fed into retained advice or ordinary `gt` induction by this script. SRC-1, `WebArena/reeval_memevol_prompt.py`.

> output_path.write_text(json.dumps(rows, indent=2))
> --- `WebArena/reeval_memevol_prompt.py`

### Routes

#### MEM-RTE-web-retrieval
Label: Web cached-query advice retrieval
Part of: [RT-RTE-web-pipeline](runtime.md#rt-rte-web-pipeline)

This is the pipeline's retained-input selection/delivery part, not a redeclaration of the task/evaluator/admission loop. Trigger: memory-enabled `run.py` invocation. Owner: runner plus selector. Task intent and prior query cache → instruction-aware query embedding → similarity ranking → first bank match by ID → all advice blocks → overwritten text file → per-action system-message read. Provider computation and symbolic matching jointly select; no model validates the selected advice's truth. SRC-1, `WebArena/run.py`, `WebArena/memory_management.py`, `WebArena/agents/legacy/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected bank records, then memory text file contents; selector also appends the current query cache row.
- Later read-back: retained prior-query vectors and selected bank advice reach a later task-model invocation through system-message text.
- Delegated visibility: task model receives every memory_items block from a selected row, not the bank's stored query, trace/status fields or numerical scores.
- Selection predicate: caller requests n=1; descending normalized dot-product scores over the loaded prior cache, then first bank task_id match; no success, age, item-level relevance or quality filter.
- Invalidation or expiry: delivery file is overwritten or emptied; no automatic bank/cache expiry or withdrawal in this inspected chain.
- Activation or effect: file mutation and advisory system injection are wired; changed model choices, relevance-discussion compliance and benefit are uninspected.
- Evidence limits: stale unmatched top ID yields no advice without searching lower-ranked IDs; cache/bank drift, optional vector incompatibility and external initial contents prevent complete relevance/trust guarantees.

> top_ids = ordered_ids[:n]
> --- `WebArena/memory_management.py`

> for sid in top_ids:
>     # find the corresponding reasoning bank entry, with reasoning_bank["task_id"] == sid
>     for i, item in enumerate(reasoning_bank):
>         if item["task_id"] == sid:
>             out.append(reasoning_bank[i])
>             break
> return out
> --- `WebArena/memory_management.py`

The selector asks for relevant prior queries, not a known answer oracle. Operating mode is a bounded task sequence or direct configured runner invocation. Code chooses automatically; operator path/configuration is not per-content approval. No specific advice proposal or veto occurs on read-back. Budget is one prior record, not one item or a fixed token count. Web prompt shrinking happens before advice is appended to the system message, so it does not enforce a total advice-inclusive input budget ([RT-RTE-context-control](runtime.md#rt-rte-context-control)). This is host-triggered retrieval during a requested task, not an independent unsolicited memory push.

#### MEM-RTE-coding-retrieval
Label: Coding cached-query advice retrieval
Part of: [RT-RTE-swe-task](runtime.md#rt-rte-swe-task)

The distinct coding selection/delivery part: instance problem → model-named cache and bank snapshot → software-engineering instruction-query similarity → first matching task row → flattened memory_items → `DefaultAgent.run` system message. Owner: `process_instance`, coding selector and task agent. Trigger: each selected batch instance before agent-execution try. SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`, `third_party/src/minisweagent/memory/memory_management.py`, `third_party/src/minisweagent/agents/default.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected_memory string or empty string and an appended current-query cache row.
- Later read-back: a prior task's advice influences the supplied system context of the next selected coding instance; vectors remain selector-only state.
- Delegated visibility: all selected row memory_items are joined; task ID, stored query, outcome and raw trajectory are not delivered by this operation.
- Selection predicate: n=1 prior query by similarity under a software-engineering instruction, followed by first matching bank ID; no status or evidence-quality filtering.
- Invalidation or expiry: new task messages replace the prior task context; bank/cache advice has no automatic invalidation here.
- Activation or effect: optional relevance instruction and selected text are appended to the system message; downstream command dependence remains unobserved.
- Evidence limits: pre-try retrieval errors bypass normal agent recovery; multiple CLI workers lack shared bank/cache locking; bank model-name partition is not an exact model-version pin.

> for item in res:
>     for i in item["memory_items"]:
>         mem_items.append(i)
> selected_memory = "\n\n".join(mem_items)
> --- `third_party/src/minisweagent/run/extra/swebench.py`

Software selects; no human per-row approval, candidate-content veto or expected-answer oracle operates here. Mode: bounded batch instances. One record bounds selection count, not text length; no memory-specific truncation is inspected. System-context retention lasts the task's turns, while bank reload gives a cross-problem horizon. This is requested task setup with automatic selection, not foreground model-directed search or an unsolicited background push. Direct `DefaultAgent.run(selected_memory=...)` additionally affords caller-supplied text, but unspecified caller provenance alone establishes neither accumulated memory nor a human admission route.

#### MEM-RTE-standalone-induction
Label: Standalone web-log advice induction

This standalone script's intended transformation is distinct from [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission): despite its coding-package location, it reads web `experiment.log`, web task configurations and saved web rewards, not SWE-Bench agent message JSON. It also differs from [RT-RTE-web-admission](runtime.md#rt-rte-web-admission), which extracts compressed steps and adds available evaluator explanation. Trigger: explicit CLI with task, result directory and output path. Owner: standalone script. Parsed web log think/action pairs and query → saved reward → success/failure prompt → GenAI generation → blank-line blocks → arbitrary JSONL append. SRC-1, `third_party/src/minisweagent/memory/induce_memory.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended appended row with task/query, extracted think/action arrays, status, memory_items and template ID.
- Later read-back: uninspected — output_path is caller-selected and no caller wires that destination to a later bank reload in the inspected registration/runner paths.
- Delegated visibility: generator receives query and log-derived think/action text, not full page observations, saved prior system advice or evaluator explanation.
- Selection predicate: reward equal to 1 chooses success guidance, otherwise failure; uses first supplied result directory and named task.
- Invalidation or expiry: inapplicable — this append operation defines no expiry or replacement.
- Activation or effect: intended model-authored advice append; task-consumer delivery and changed behavior are not established.
- Evidence limits: `from memory.memory_management import select_memory` and `from instruction import ...` depend on launch/import context not established by the registered CLI; no observed invocation, generated artifact or later consumer is supplied.

> log_path = os.path.join(f, "experiment.log")
> think_list, action_list = extract_think_and_action(log_path)
> --- `third_party/src/minisweagent/memory/induce_memory.py`

> if ex['status'] == 'success':
>     generated_memory_item = llm_generate(trajectory, args, True, si=SUCCESSFUL_SI)
> else:
>     generated_memory_item = llm_generate(trajectory, args, True, si=FAILED_SI)
> --- `third_party/src/minisweagent/memory/induce_memory.py`

Proposal/admission: model authors; code accepts all generated blocks; the human supplies input/output paths, not content approval. Rejection is call/import/parse/I/O failure, not a semantic veto. No rollback is implemented by the append. Guidance requests extraction/generalization under success/failure instructions; it does not revise those instructions. `gt` uses an external saved benchmark reward, `autoeval` a saved model label, neither an inspected expected-answer oracle in the generation call. Mode is one explicitly named task, not open-ended autonomous exploration.

Theory-builder conditions 1–4: (1) afforded — prompt requests whole localized advice units; (2) uninspected — no later decision-dependent consumer; (3) uninspected — reflection request is not a supplied claim-directed criticism/revision artifact; (4) uninspected — no next round shaped by retained criticism is established. Addressability: blank-line units afforded, assumptions and scope structure uninspected. Persistence: append afforded, subsequent consumption horizon unresolved. Learning: improved future capacity and attribution uninspected. Reflection: trace-derived representation afforded, representation-to-behavior link unresolved. Reflective/autonomous theory builder: uninspected for the independent missing criticism, iteration and consumption links. No exercised self-improvement claim is made.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-web-admission](runtime.md#rt-rte-web-admission)

Memory-specific lineage: actionless/unreadable steps are omitted; the fallback think extractor can derive text from saved chat output. Default generation sees query, think/action reconstruction and available autoevaluation reason, not complete browser observations or the prior selected advice as a distinct input. The durable result is [MEM-OBJ-web-advice](#mem-obj-web-advice), with extracted trace/label ledger beside it. Authorship is model-side, physical I/O and admission are software-side. The operator starts/configures the workflow, not each item approval. No retained old-item revision or consolidation is established by the "Updated Memory" helper label. SRC-1, `WebArena/induce_memory.py`.

> if not action:  # skip empty action steps
>     continue
> think_list.append(think)
> action_list.append(action)
> --- `WebArena/induce_memory.py`

The requested at-most-three and non-overlap constraints are prompt policies, not gates. Available reasons can shape the generated prose, but no schema requires preserving reasons; raw stored traces do not ensure that later agent decisions receive them. Later delivery selects only memory_items, as [MEM-RTE-web-retrieval](#mem-rte-web-retrieval) establishes.

#### On [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission)

The separately saved trajectory can include the previously delivered advice in its system message, while the generator's view omits it. This prevents treating extraction as explicit criticism/revision of the selected prior item. Status is reduced to boolean; no explanation field goes into the new bank row. Durable content has query/ID/status linkage but no raw transcript copied into that row. SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`, `third_party/src/minisweagent/run/utils/save.py`.

> trajectory = "\n".join([m["content"] for m in messages if m["role"] != "system"])
> --- `third_party/src/minisweagent/run/extra/swebench.py`

Task-model prose, user task and formatted environment observations are mixed trace origin. Derived advice is automatically accepted and later selected as described in [MEM-RTE-coding-retrieval](#mem-rte-coding-retrieval). The coding prompt requests generalization; no semantic validator checks that it has removed literal strings or retained explanation.

#### On [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling)

Memory output-shape limit supplements the supplied wiring limits. The ordinary Gemini client returns a `(response, chat_completion)` tuple, whereas scaling assigns the entire call result to memory_items without splitting or unpacking. Its class-versus-instance call already prevents asserting completed induction; even after that defect alone were repaired, the inspected return contract would not match ordinary list-of-string delivery without another adaptation. No repaired execution is inferred. SRC-1, `WebArena/induce_scaling.py`, `WebArena/utils/clients.py`.

> generated_memory_item = client.one_step_chat(trajectories, system_msg=PARALLEL_SI, temperature=0.7)
> --- `WebArena/induce_scaling.py`

> response = chat_completion.text
> return response, chat_completion
> --- `WebArena/utils/clients.py`

The intended row keeps query/task/template, but no status, source trajectories or comparison rationale separately. Induction loads the same directory repeatedly and its selected status is not interpolated as a success/failure marker in the combined trajectory text. A claimed multi-trajectory self-contrast therefore does not establish distinct alternatives, dependable feedback or usable retained advice.

#### On [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Web working state is per-episode Python observation/action/memory/thought lists. A new MainPrompt reconstructs a view each action; truncation affects prompt elements, not those lists. Visible HTML/tree truncation drops trailing lines after shrink-call thresholds, appending an omission notice; History's shrink method delegates to each step, not an older-turn-first eviction policy. The optional `<memory>` scratchpad is model-authored episode state; the ordinary runner passes `use_memory=False`, so accumulated bank advice and scratchpad are different surfaces. SRC-1, `WebArena/agents/legacy/dynamic_prompting.py`, `WebArena/agents/legacy/agent.py`, `WebArena/run.py`.

> self._prompt = "\n".join(lines[:new_line_count])
> self._prompt += f"\n... Deleted {self.deleted_lines} lines to reduce prompt size."
> --- `WebArena/agents/legacy/dynamic_prompting.py`

> if self.flags.use_memory and self.memory is not None:
>     prompt += f"\n### Memory:\n{self.memory}\n"
> --- `WebArena/agents/legacy/dynamic_prompting.py`

No semantic summary checkpoint replaces the view in these inspected controls. Original observations remain in episode state and serialized artifacts; next-step reconstruction can start from the original data rather than the previous truncated text. Coding uses fresh per-task message frames, length-based head/tail observation formatting and possible explicit shell/file reads. Separate judge/induction calls get selected transcript text; only verdict/generated blocks escape to the driver. This resembles isolated frames, not pointer-based heap restoration: selected text is passed by value, and omitted observations are not automatically recoverable by a context pointer. Full restoration guarantees are not established.

#### On [RT-BAP-system-memory](runtime.md#rt-bap-system-memory)

Actual consumer receives natural-language advice, not dense vectors, lineage ledger or verified proof. Authority is advisory system-message placement for the task, mediated by model interpretation and relevance discretion. The web consumer rereads a file every step; coding embeds the selected string in the initial system message. Neither path validates the requested discussion of each item. Existing stored text is not sanitized or cross-checked for source truth at injection in these inspected paths. SRC-1, `WebArena/agents/legacy/agent.py`, `third_party/src/minisweagent/agents/default.py`. Delivery is established by the supplied record's passages, not demonstrated compliance.

## Write side

The ordinary chains are raw task activity → saved trace → outcome-selected induction prompt → model-derived advice → automatic bank append → later task system input. [RT-RTE-web-admission](runtime.md#rt-rte-web-admission) and [RT-RTE-swe-admission](runtime.md#rt-rte-swe-admission) own admission; object records above distinguish raw traces, outcome evidence, derived text and access metadata. Task queries contain external/operator benchmark input; trajectories mix model output with environment observations, so trace origin is not purely model reasoning. Provider-internal processing is opaque.

Admission controls are different from authorship. Models author advice; host code admits returned text with no semantic per-item veto. Missing calls, invalid inputs or failed I/O can prevent append, but these are not content evaluation. Initial nonempty banks/caches and manual edits have unresolved control. Empty-file creation and all inspected subsequent transformations remain known software writes. Source instructions ask for reflection, non-overlap and generalization; no source-grounded observation establishes that generated content met them.

Curation is primarily trace selection and generative extraction, not consolidation of existing records. AWM extraction and Synapse trace-copy modes retain different material; failure branches do not initialize the variable subsequently appended. Scaling intends contrast across trials but has repeated inputs, misleading outcome labeling, client invocation and output-shape limits. Standalone induction affords a further log-to-advice write, not a proven coding-bank integration.

Physical cleanup and epistemic withdrawal are distinct. Web destination replacement and coding redo delete task outputs/predictions, not matching bank/cache rows. Cache admission precedes any outcome or advice admission. Rejected/failed induction can therefore leave query keys that later outrank usable records; redo can append duplicate IDs whose bank lookup still chooses the first row. These are source-supported consequences of the cache write and lookup, not observed failures. Inspected append and retrieval files contain no automatic item expiration, quality rejection, bank-row replacement or coordinated rollback. That is a bounded account of these paths, not a repository-wide absence claim.

Reasons persist only where the producer includes them in generated prose or in separate raw/evaluation artifacts. Web retains extracted think/action arrays but the later task consumer gets only advice; evaluator explanation is an induction input, not a required bank field. Coding retains the raw message file but does not send judge rationale to induction. No alternative semantic compaction checkpoint was found in the inspected working-context controls; ordinary context shortening does not produce durable summarized memory.

## Read-back

[MEM-RTE-web-retrieval](#mem-rte-web-retrieval) and [MEM-RTE-coding-retrieval](#mem-rte-coding-retrieval) establish cross-task read-back rather than mere storage APIs. Each starts with a current task request, selects prior-query IDs computationally, looks up a bank record and delivers all its advice blocks. Numeric vectors shape selection; generated text reaches the task model through a system channel. Selection count is bounded, content size is not. Raw evidence and outcome metadata remain outside that automatic delivery.

The web file is a repeated per-step delivery channel and shared scaling mutable state; the coding string enters one fresh task message frame. Task-model discretion governs whether advice matters. No source execution establishes activation or improved future capacity. Model weights are separate supplied components, with no operational parameter update established.

Other consumers differ materially: the coding inspector displays saved trajectories to a human; web autoevaluation and induction reread saved task artifacts; re-evaluation writes standalone score reports. None of those alone establishes advice adoption or a changed task policy. Standalone output to an arbitrary path and `DefaultAgent.run` with unspecified caller-supplied selected text are storage/delivery affordances, not demonstrated later retained-experience routes. Optional ChatCached is likewise a memoization affordance without inspected task-loop activation.

## Integration issues

- **Scaling output contract addition.** [RT-RTE-web-scaling](runtime.md#rt-rte-web-scaling) already bounds operation because the client is not instantiated. Direct inspection adds the un-unpacked tuple output contract, incompatible with ordinary string-block delivery without adaptation. The evidence is the scaling annotation's two passages. Consequence: retain scaling admission/read-back as afforded, not a working distinct-trajectory advice loop. This is an addition, not a contradiction of the supplied status.
- **Alternative admission scope.** [MEM-RTE-standalone-induction](#mem-rte-standalone-induction) identifies the coding-package standalone script as a web-log transformation. Its imports, launch context and actual later bank consumer remain unresolved. Consequence: do not treat every file in the coding memory package as the coding batch lifecycle. No new source or scope change is needed.
- **Prompt items versus physical blocks.** [MEM-OBJ-web-advice](#mem-obj-web-advice), [MEM-OBJ-coding-advice](#mem-obj-coding-advice) and the retrieval records refine supplied references to memory items: blank-line units do not reliably correspond to requested Markdown items. Consequence: at-most-three prompt policy cannot establish a three-item or token budget at the consumer.
- **Cache/bank and cleanup independence.** [MEM-OBJ-query-cache](#mem-obj-query-cache), [MEM-OBJ-trajectory](#mem-obj-trajectory) and both retrieval records retain query-key writes before advice admission, first-record lookup and no coupled cleanup. These explain why deletion/redo or feedback errors do not automatically withdraw prior advice. No observed inconsistency is asserted.
- **Initial material and exact embeddings.** Initial nonempty bank/cache content, human control over it and cached model/version provenance remain unknown. [MEM-OBJ-query-cache](#mem-obj-query-cache) and the supplied embedding components support known transformation, not content authenticity, vector compatibility or numerical reproducibility.
- **Ancillary working-context/memoization paths.** Optional scratchpad is distinct from persistent advice; ChatCached activation and other adapters/runners are not exhaustively inspected. [RT-RTE-context-control](runtime.md#rt-rte-context-control) stays bounded to traced paths. Consequence: no universal context-budget, semantic-compaction or restoration conclusion.
- **Identity comparison.** New object declarations have no supplied object counterpart; both new retrieval declarations are explicit parts of supplied task routes, not duplicates. Standalone induction overlaps producer function with two supplied admission routes but has different inputs, entry point and unresolved destination; it is not a replacement. All reused supplied referents receive annotations. No possible duplicate requiring supersession was identified.

## Limitations and checks

All findings are bounded to SRC-1 at the supplied commit. Source identity was rechecked against HEAD and a clean checkout. Registered script dispatch was checked against the batch route and single-instance alternative; both selector implementations were read, rather than inferring one from the other. Strong claims were challenged with stale cache IDs, duplicate task IDs, Synapse trace-copy, no-memory mode, scaling wiring/output shape, omitted system messages and redo cleanup. These source cases prevent promoting declared generalized memory, complete provenance, item counts, rollback or exercised self-improvement into guarantees.

No target code, tests, examples or providers were executed. External services, initial imported memory, installed browser persistence and uninspected alternate runtimes limit coverage. There are no observed generated advice artifacts, downstream decision traces or interventions; successful operation, learning benefit and causal attribution remain uninspected independently of wired persistence and delivery.

Deterministic validation: the invocation-specific validate-output check passed. It establishes structure, permitted references, identity and quotation occurrence, not semantic correctness, successful operation or acceptance by reconciliation.
