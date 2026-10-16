---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "SAGE memory: paired function transfer, persistent evaluation records, alternative selectors, expert traces and parameter retention."
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
source-identity: https://github.com/amazon-science/SAGE
reviewed-boundary: "3c9244e82244abb1adc5467ee601a03ba0f433a0"
---

# SAGE memory report

## Boundary and evidence

This report covers SAGE's shipped memory and working-context mechanisms at the boundary's frozen commit. It includes training's paired dictionaries and reward-to-weight path, evaluation's function records and all four selectors, predefined loading, expert scenario accumulation and trace-to-SFT conversion, checkpoint recovery, the optional response cache, and the registered full-code retry agent's context selection. It excludes upstream AppWorld storage/evaluator internals, provider internals and external training machinery, as the [boundary](boundary.md) does. These exclusions prevent independent conclusions about environment isolation, test adequacy and full training/checkpoint correctness. No target was executed and no run artifacts were supplied.

Direct reads below are SRC-1 implementation evidence; prompts and configurations also establish design intent. The supplied runtime records are cited rather than redeclared. New reads extend inspection within SRC-1, not its source identity. Source HEAD was checked against `3c9244e82244abb1adc5467ee601a03ba0f433a0`, and `git status --short` was empty.

| Operation / entry | Source path and inspection | Covering records or limit |
|---|---|---|
| CLI evaluation dispatch and configured runner | Direct: `patches/appworld/src/appworld/cli.py` dispatch, `patches/appworld/experiments/code/skill_library_agent/run.py`, `patches/appworld/experiments/configs/sage_test_normal.jsonnet` | [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop); one agent across its assigned task sequence, default selector, caching disabled |
| Training acquisition, install and world cleanup | Direct: `sage/llm_agent/app_world/app_world_env.py` extraction, initialization, close; supplied runtime for full turn orchestration | [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) |
| RL observation budget / rolling suffix | Direct: `sage/llm_agent/appworld_generation.py` observation processing and rolling state; supplied runtime for task transitions | [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout), annotations below |
| Evaluation extraction, pruning and append | Direct: complete `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py` and `patches/appworld/experiments/code/skill_library_agent/agent.py` | [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop) |
| Predefined read and default selector | Direct: same skill agent constructor/initializer | Same records; external file provenance and content are unknown; output-to-predefined promotion is not wired in the inspected constructor |
| Skill-vector selection | Direct: same skill agent | [MEM-OBJ-skill-embeddings](#mem-obj-skill-embeddings), [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model) |
| Query-vector / n-gram selection | Direct: same skill agent | [MEM-OBJ-query-list](#mem-obj-query-list), [MEM-OBJ-query-embeddings](#mem-obj-query-embeddings); restart metadata gap retained below |
| Expert admission, save and retry | Direct: base agent, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`, `patches/appworld/experiments/code/skill_library_agent/run_rollout.py` | [MEM-OBJ-rollout-functions](#mem-obj-rollout-functions), [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission) |
| Trace logging / response cache / provider tools | Direct: complete `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py` | [MEM-OBJ-expert-dataset](#mem-obj-expert-dataset), [MEM-RTE-response-cache](#mem-rte-response-cache); adapter exposes tools but inspected skill callers generate from messages, not registered tool dispatch |
| Expert trace transformation and SFT masking | Direct: complete `patches/appworld/extract_expert_dataset.py`, encoding section of `patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py`, full SFT YAML | [MEM-OBJ-expert-dataset](#mem-obj-expert-dataset), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission); raw examples and learned weights unavailable |
| RL weights / checkpoint retention | Direct save/load: `sage/verl/trainer/ppo/ray_trainer.py`; supplied runtime for reward/optimizer and worker implementation | [RT-CMP-actor-rollout](runtime.md#rt-cmp-actor-rollout), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) |
| Alternate registered agent / API selector | Direct: complete `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`, `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`; scoped search for registration, hooks and tool surfaces in the agent directory | [MEM-RTE-api-context](#mem-rte-api-context); wiring is an exposed alternate, not demonstrated deployment under the normal config |

The four-node launcher and backend-specific retention details beyond supplied runtime findings remain uninspected, not inaccessible. They prevent claims of identical behavior across all launch/backend combinations. Static demonstration tasks, prompts and API documentation are context inputs, not use-derived memory. Provider state is opaque: endpoint naming does not establish a persistent conversation store or its absence. See [RT-CMP-language-model](runtime.md#rt-cmp-language-model) and SRC-1, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.

## Core ideas

1. **The reusable result is code, not a conversation summary.** Training keeps imports and top-level function source from non-failing steps, indexed by name, then installs the entire matching dictionary in the paired fresh world. Evaluation extracts from retained source plus generated code history. Extracted source can preserve docstrings and comments within the function span, but not the surrounding assistant reasoning, observations, evaluator reasons or a structured rationale ledger. Model guidance and interpreter authority are separate consumers: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-BAP-function-execution](runtime.md#rt-bap-function-execution), [RT-BAP-function-guidance](runtime.md#rt-bap-function-guidance).
2. **Persistence has several unrelated horizons.** Training dictionaries expire at a rollout call; evaluation records survive across tasks in one agent and append to disk; constructor reload uses another directory; expert libraries reset per scenario; weights survive via later updates and checkpoints. Disk output does not itself establish restart delivery. The annotations and [MEM-OBJ-rollout-functions](#mem-obj-rollout-functions) keep these horizons distinct.
3. **Selectors operate on metadata as well as content.** Default evaluation uses scenario-derived task IDs, while alternatives rank function embeddings or task queries. Embeddings are numerical access material, not executed skill payloads. The default retains the first encountered name; extraction within a task replaces same-name content, but the accumulated list can contain older duplicates. Consequently, appending a revision is not general withdrawal of an older function. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`; [MEM-OBJ-query-list](#mem-obj-query-list), [MEM-OBJ-skill-embeddings](#mem-obj-skill-embeddings).
4. **Quality gates are path-specific.** Non-failing execution, default post-task extraction, previous-label gating and expert success-plus-definition-execution differ. None establishes semantic correctness on novel arguments. The prompt's reusable-function rules are requests, not enforced admission criteria. Counterexamples are imports explicitly retained despite the no-import instruction, and default extraction despite current-task failure. See [RT-CLM-function-rules](runtime.md#rt-clm-function-rules), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission).
5. **Trace-fed numerical updates are another retention path.** RL trajectories/outcomes feed advantages and weights; expert LM-call traces become filtered training examples and then supervised weights. Neither retained logs alone nor configured optimization proves improved competence. Reasons may remain in trace text but are not guaranteed to survive extraction, token cutoff or parameter encoding. See [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission), [MEM-OBJ-expert-dataset](#mem-obj-expert-dataset).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-skill-embeddings
Label: Skill embeddings

Part of: [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions)

This is the numerical selection part distinguished from the parent record's executable source. Source-native identity: `skill_embeddings`; representational form: distributed-parametric dense representations; substrate: CPU tensors and `skill_embeddings.pt`, with optional predefined input. Newly generated vectors derive from extracted function strings using [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model); predefined tensor lineage, encoder compatibility and row alignment are unresolved because their contents are not frozen. The encoder is not updated by this route. The selector receives task-instruction embedding similarity, scans descending ranks, considers at most six entries (including duplicate-name candidates), and concatenates only first-seen function names. There is no code-length budget in this selector and no threshold here. The tensor shapes selection; the selected source, not the tensor, reaches AppWorld and the model. Software encodes and appends on nonempty extraction; the operator's launch is not per-vector approval. The file is overwritten with the accumulated tensor; no semantic quality-based rollback is shown. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> skill_embeddings = self.retrieval_model.encode(functions_list)
> skill_embeddings = torch.from_numpy(skill_embeddings)
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

> s+=1
> if s>5:
>     break
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### MEM-OBJ-query-list
Label: Query list

Part of: [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions)

This is task-query access metadata, not function content. Source-native identity: `query_list`; substrate: agent list and an optional separately supplied predefined `query_list.jsonl` in query-embedding mode. Its symbolic task IDs associate natural-language task instructions with function records. Query-embedding and n-gram writes append the current instruction and task ID only after nonempty function extraction. These instructions originate in task inputs, not an invented model summary. Initial predefined authorship/admission are unknown. Subsequent appends are software-controlled without per-query human approval. Query embedding selects up to two query rows above threshold, then all matching task-ID functions with name deduplication; n-gram mode does the analogous top-two operation over lowercase whitespace bigram-set Jaccard scores. The selectors have no separate function-count or source-token cap. Their authority is access selection; functions have downstream execution/guidance authority. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> if self.retrieval_method=="ngram":
>     self.query_list.append({"task_id":world.task_id, "query":world.task.instruction})
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

The query-embedding branch also appends the instruction and task ID. The inspected writer saves query tensors but does not serialize `query_list`; the predefined loader requires both tensor and query-list files. N-gram initialization starts with an empty query list and does not load it from that predefined file. Thus same-process query reuse is wired, but a complete automatically produced restartable query index is not established. This is a bounded implementation finding, not a claim about external library preparation.

#### MEM-OBJ-query-embeddings
Label: Query embeddings

Part of: [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions)

Source-native identity: `query_embeddings`; form: distributed-parametric task-instruction vectors; substrate: CPU tensors and overwritten `query_embeddings.pt`, with optional predefined loading. Unlike [MEM-OBJ-skill-embeddings](#mem-obj-skill-embeddings), these encode instructions rather than functions and need [MEM-OBJ-query-list](#mem-obj-query-list) to map ranked positions to task IDs. New vectors use the unmodified query encoder in [RT-CMP-retrieval-model](runtime.md#rt-cmp-retrieval-model). Software admits vectors on nonempty extraction without per-content human review. Their consumer is instruction-similarity selection; they never execute as Python or become a readable summary of the function. Predefined provenance, positional compatibility and external editing controls are unknown; this prevents a correctness claim about restored indexes, not recognition of the implemented append/selection path. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> torch.save(self.query_embeddings.cpu(), world.base_output_directory+"/query_embeddings.pt")
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### MEM-OBJ-rollout-functions
Label: Expert rollout functions

Part of: [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission)

This object is a retained product inside the supplied expert route, not a second declaration of that route or of normal evaluation's list. Source-native identity: rollout subclass `skill_library_functions`, records with `idx`, `task_id`, `function`, `name`. Form: symbolic records carrying Python source (and interpreter-visible docstrings); substrate: scenario-local list, plus overwritten `output_misc_directory/skill_library_functions.jsonl` snapshots before later scenario tasks. Lineage: AST top-level functions/imports from that attempt's `code_list`, merged with previously admitted records by a name-derived key. No function embedding selector is involved. The later task executes and renders all accumulated functions. Raw outputs and surrounding reasoning are not retained in this object; they remain separate logs if logging is enabled. Software benchmark-success and fresh-world execution gates admit it; the model authors candidates and the operator starts/configures generation, without per-function approval. A failed attempt does not merge its candidate list. Resetting the next scenario withdraws the in-process library, not old files. SRC-1, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`.

> for skill in self.skill_library_functions:
>     self.retrieved_skills_prompt += skill['function'] + "\n\n\n"
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`

> with open(world.output_misc_directory+"/skill_library_functions.jsonl", "w", encoding="utf-8") as f:
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`

#### MEM-OBJ-expert-dataset
Label: Expert dataset

Part of: [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)

This object is the derived training corpus within the supplied route. Source-native identity: `appworld_expert_dataset.json`; substrate: overwritten JSON file under LLaMA-Factory data. The JSON schema is symbolic; contained user instructions, observations and assistant prose are natural-language material, while fenced Python is symbolic at execution but here tokenized as supervised text. Raw `lm_calls.jsonl` records hold provider arguments and response envelopes; the extractor takes each selected task's last call's input messages plus its assistant response, not every envelope or every separate call. Prior exchanges present in that last request survive subject to the agent's truncation and normalization. Complete scenarios and partial scenarios failing task three are selected from failure lists; messages containing the no-code marker are rejected. Code-fence normalization and whitespace edits are software transformations, not content criticism or human approval. See [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission) for gates, external machinery and launcher limits. SRC-1, `patches/appworld/extract_expert_dataset.py`, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.

> for scenario_id in complete_scenarios_list:
>     for task_id in [scenario_id+"_1", scenario_id+"_2", scenario_id+"_3"]:
>         with open(dataset_folder+"/tasks/"+task_id+"/logs/lm_calls.jsonl") as f:
>             for last_line in f:
>                 pass
>         last_line_data = json.loads(last_line)
>         messages = last_line_data["input"]["messages"]
>         messages.append({'role': 'assistant', 'content': last_line_data['output']['choices'][0]['message']['content']})
>         train_data_list.append({'messages': messages})
> --- `patches/appworld/extract_expert_dataset.py`

The later supervised processor applies token cutoff and label masks, not a verbatim memory reader. The shipped YAML specifies cutoff 12500, maximum 2000 samples and `prompt_turn_idx: 10`. Early assistant targets can remain context while being masked as training targets; later content can be cut. Resulting distributed-parametric weights are [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model), not individually addressable trace records. Neither reason preservation in weights nor benefit follows. SRC-1, `patches/LLaMA-Factory/src/llamafactory/data/processor/supervised.py`, `patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml`.

#### MEM-OBJ-llm-calls
Label: Completion response cache

Distinct from the trace corpus [MEM-OBJ-expert-dataset](#mem-obj-expert-dataset) and the supplied model [RT-CMP-language-model](runtime.md#rt-cmp-language-model): source-native identity is Joblib `cache` at `path_store.cache/llm_calls`, wrapping `cached_chat_completion`. Storage is external cache files managed by Joblib; retained values are symbolic response envelopes containing generated text, not training examples or updated weights. Content lineage is a prior successful provider result; cache matching uses function arguments. The normal config disables this branch; exposed generator construction defaults `use_cache=True`. Retention/eviction and exact hashing semantics depend on the external Joblib implementation and are not audited. SRC-1, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`, `patches/appworld/experiments/configs/sage_test_normal.jsonnet`.

> cache = Memory(os.path.join(path_store.cache, "llm_calls"), verbose=0)
> --- `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`

### Routes

#### MEM-RTE-response-cache
Label: Completion response cache

Distinct alternate return path inside the model adapter used by [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), not a duplicate task loop. A caller configures `use_cache`; the adapter chooses a cached or noncached function. With caching enabled, repeated matching arguments can return retained completion data to `generate`, which extracts assistant content for the agent. Owner: adapter plus external Joblib. Inputs include messages, model name, generation arguments and supplied tool specifications. Cache admission is software memoization of successful provider returns, with no content-quality oracle or human per-response approval; the model produced the original content. This is reuse, not a proposed semantic revision. SRC-1, `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`.

- Immediate return: provider-shaped response to `generate`, then assistant content, usage and finish reason to the agent.
- Later read-back: matching later adapter invocation may reuse [MEM-OBJ-llm-calls](#mem-obj-llm-calls) instead of calling the provider.
- Delegated visibility: adapter receives full request arguments; no cross-agent cache isolation guarantee is established.
- Selection predicate: `use_cache` selects branch; Joblib memoization matches cached function arguments. Normal evaluation explicitly sets false.
- Invalidation or expiry: uninspected — Joblib storage policy is external; no content-based withdrawal is implemented in this wrapper.
- Activation or effect: cached content can reach code extraction and AppWorld through the caller; cache hits and resulting behavior are unobserved.
- Evidence limits: exposed alternate, not active in the normal config; a mutable server behind an unchanged model name can make identity-based freshness unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.chat_completion = {
>     True: cached_chat_completion,
>     False: non_cached_chat_completion,
> }[use_cache]
> --- `patches/appworld/experiments/code/skill_library_agent/lite_llm_generator.py`

#### MEM-RTE-api-context
Label: Alternate API context selection

No counterpart in the supplied route declarations: this is the registered `simplified_full_code_reflexion` agent's model-selected API context, not the normal skill-library task loop. Its API predictor uses separate messages containing API descriptions, static demonstrations and the current task; its return is a filtered API-name list. The foreground code generator gets selected detailed docs, configured demonstration solutions and the actual task, not the predictor conversation. Code filters predictions to allowed APIs, caps predicted additions at 16 by default, adds supervisor APIs, then includes demo-required APIs when assembling docs. The API-doc rendering compresses parameters when configured and removes path/method fields. Retrying later appends stacktrace and retrial prompt; it is ordinary current-task accumulation, not an acquired long-term criticism store. Owner: agent code chooses framing, predictor model proposes APIs, code vets membership and sizes, task-solving model proposes Python. Operator supplies demo IDs and templates; no per-prediction human approval is wired. Operating mode: bounded task/retry execution. There is no reference-answer oracle for predicted API relevance; membership in documentation is the filter. SRC-1, `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`, `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`.

- Immediate return: selected names plus cost from predictor to foreground agent; then generated Python for AppWorld.
- Later read-back: inapplicable — selected names and static demonstrations are current-task context, not material acquired across use; optional completion caching is separately recorded.
- Delegated visibility: predictor receives descriptions and demonstrations; foreground receives selected docs and names, not predictor messages or hidden processing.
- Selection predicate: model proposes names; allowed-name filter and default 16-name cap plus supervisor additions; code unions demo APIs before detailed-doc selection.
- Invalidation or expiry: base `initialize` resets task messages; predictor calls construct fresh prompts, and foreground stores task-local selected APIs. Static demos remain configured inputs.
- Activation or effect: filtered context is wired to generation; predicted coverage, retry success and active use under the normal config are unobserved.
- Evidence limits: implementation affords a different context route; externally loaded demos and prompts are not all frozen as content artifacts, and filtering is not a guarantee of sufficient API coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.messages = header_messages + demo_messages + test_input_messages
> --- `patches/appworld/experiments/code/skill_library_agent/full_code_reflexion.py`

> predicted_apis = unique(predicted_apis)
> return predicted_apis, output["cost"]
> --- `patches/appworld/experiments/code/skill_library_agent/api_predictor.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-skill-libraries](runtime.md#rt-obj-skill-libraries)

Lineage is model-generated action source after non-failure checking, not an abstract summary inferred by a second model. Each top-level `FunctionDef` retains its source span plus each import's starting source line; global assignments, ordinary top-level calls and conversation reasoning are not copied into the dictionary. Decorators preceding the `def` and multiline-import continuation are not guaranteed by this extraction algorithm. This limits self-containment and faithful module transfer. Function bodies/docstrings remain readable, but no retained test result or adoption reason accompanies each dictionary entry. Same-name replacement is software curation within one pair; launch/configuration is not per-function human approval. The raw source and output remain in trajectory data for a different consumer. SRC-1, `sage/llm_agent/app_world/app_world_env.py`.

> func_code = "\n".join(import_lines + lines[start_lineno:end_lineno])
> function_bodies.append(func_code)
> --- `sage/llm_agent/app_world/app_world_env.py`

#### On [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions)

Normal evaluation re-extracts retrieved definitions except in skill-embedding mode, then merges generated task code by name before appending records. Re-saving a retrieved function under the current task ID changes association metadata without proving new authorship, new meaning or current-task validation. The accumulated agent list is append-only in this writer, unlike the within-task last-definition-wins merge. Default selection's first encountered name can therefore hide a later revision. Predefined content is read as JSON without a content approval gate here; who supplied, edited or approved those external artifacts is unresolved. AppWorld executes selected source before the model consumes it, making that loader a capability admission surface rather than merely a citation source. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`.

> if self.retrieval_method!="skill_embedding":
>     try:
>         functions, names = extract_functions_from_code(self.retrieved_skills_prompt)
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### On [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)

Read-back is automatic supply at second-subtask initialization: code selects the matching dictionary by pair position, concatenates all values without relevance ranking or a skill-specific size cap, executes them, then renders surviving text into the initial task prompt. The current second-task instruction does not select individual functions. Source trust is inherited from generated code and output markers, not provenance validation. The retained definitions have symbolic authority at the interpreter and interpreted guidance at the model; actual use remains unobserved. Failed install suppresses prompt text on an unsuccessful response, not dictionary contents or already attempted world effects. An exception path prints failure without guaranteed suppression. SRC-1, `sage/llm_agent/app_world/app_world_env.py`.

> if "Execution successful." not in response["output"]:
>     retrieved_skills_prompt = ""
> --- `sage/llm_agent/app_world/app_world_env.py`

#### On [RT-RTE-paired-rollout](runtime.md#rt-rte-paired-rollout)

Working-context control is code-owned. Each subtask has its own world and model input; the first context is discarded as a live task frame while selected definitions escape through the dictionary. Trajectories still return to training; they are not injected as the next task's conversation. Per-sample isolation keeps other agent samples' contexts out. The frame analogy fits the selected-input/returned-function boundary, but transfer is source by value: first-world Python globals are not dereferenceable from the second world.

RL observation processing keeps the leading `max_obs_length` characters, adds a display-truncation marker and optional reminder, and deactivates a sample if tokenized next input would overflow `max_prompt_length`. Rolling-state construction also bounds input to a suffix. These are truncation/termination controls, not model-written summaries; no summary or automatic reload of removed observation tails is produced by these methods. There is an available `truncate_input` method in the environment, but scoped search found its definition only, not a call in that file; it is not used here as proof of live history compaction. SRC-1, `sage/llm_agent/appworld_generation.py`, `sage/llm_agent/app_world/app_world_env.py`.

> if prompt_response_length[i] + observation_length > self.config.max_prompt_length:
>     new_active_mask[i] = 0
>     next_obs_with_special_tokens[-1] = ""
> --- `sage/llm_agent/appworld_generation.py`

> "input_ids": new_input_ids[:, -max_len:],
> --- `sage/llm_agent/appworld_generation.py`

#### On [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop)

Default read-back is code-triggered on task initialization, not a model tool request. It scans scenario `_1` records before `_2`, tests substring membership in recorded task IDs and deduplicates names. Therefore it is not exact task-ID equality. No explicit selector token budget limits total retained source. Alternatives and their distinct gates are in the object records above. Selected definitions execute before their exact-success-string gate controls prompt inclusion; rejection does not delete stored candidates. The supplied runtime's gate description is supported, including its previous-task label qualification.

Failed-step pruning removes the last `code_list` entry when its output is processed on a subsequent model step; it does not remove that assistant message from `messages`. Thus extraction history and model-visible history differ. The final execution's output may never pass through this pruning method if the outer loop ends immediately. This prevents the claim that ordinary evaluation only admits non-failing code, even independently of current-task success gating. At initialization messages/code list reset, but the library list survives; old turns do not cross tasks except through extracted source or independently loaded artifacts. Observation text is hard-truncated to 12000 characters, with reminder, while messages otherwise accumulate. Merely storing `max_prompt_length` does not enforce a history budget in this next-step method. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`.

> if "Execution failed." in last_execution_output_content and len(self.code_list)!=0:
>     del self.code_list[-1]
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

#### On [RT-RTE-expert-admission](runtime.md#rt-rte-expert-admission)

The expert path does not apply normal evaluation's failed-step deletion. Its extractor parses every retained code entry, replacing same-name definitions within the attempt. Benchmark success and fresh-world definition execution then gate merging [MEM-OBJ-rollout-functions](#mem-obj-rollout-functions). A definition-only test can miss a function-body failure until invocation, so an admitted library is not a set of individually validated capabilities. Retry creates a fresh task frame; previous accepted scenario functions remain available. Scenario reset removes that in-process supply. The snapshot writer precedes the next task, so a file can be a checkpoint of prior accepted functions rather than the final library after the current task. SRC-1, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`.

#### On [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

This is automatic trace-fed retention in parameters: generated trajectories plus external task outcomes and lexical reuse counts reach numerical optimization; later rollout inference reads changed weights. The update is software-controlled, without per-update human content approval; operator launch and hyperparameters are separate. A lexical name hit is not proof that a function was called or that reuse caused success. Raw outcomes guide optimization without persisting an addressable reason for an individual weight change. Source passages and statuses are in the supplied record.

Checkpoint write/read adds a recovery horizon, not conversation memory. Driver saves actor, optional critic and dataloader state, and a latest-iteration tracker. It chooses latest local checkpoint in auto mode or the configured resume path; HDFS load raises `NotImplementedError`. Worker save receives configured retention counts (or one for the deprecated remove-previous flag). Resume can delete local checkpoint material according to configuration. This does not reconstruct interrupted AppWorld worlds or their dictionaries. Checkpoint availability is not quality-based adoption or rollback. SRC-1, `sage/verl/trainer/ppo/ray_trainer.py`.

> dataloader_state_dict = self.train_dataloader.state_dict()
> torch.save(dataloader_state_dict, dataloader_local_path)
> --- `sage/verl/trainer/ppo/ray_trainer.py`

#### On [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission)

The durable trace-to-behavior chain is raw LM calls → selected message corpus [MEM-OBJ-expert-dataset](#mem-obj-expert-dataset) → cutoff/masked supervised tokens → weights → operator-selected later inference/RL. The last edge is configured only after an operator chooses the model path; the RL placeholder is not an automatic promotion. Ground-truth demonstration text, benchmark tasks, model-authored code/prose and environment output are mixed trace origins, not all model-produced experience. Initialization of actual datasets/weights and their quality remain unknown, while subsequent extraction/masking are inspectable. No trace-reason ledger is created by the extractor, although assistant prose present in the selected messages can survive.

## Write side

The acquisition/admission distinctions above matter: the model writes candidate Python; AST code mechanically selects functions/imports; failure strings, label predicates or expert verification determine admission at different boundaries; physical JSONL/tensor I/O does not itself establish human control. Evaluation's normal config enables skills and omits `use_label`, whose default is false. Predefined JSONL and tensors are another admission path with unresolved external authorship/control. Loading them is not evidence of human curation. SRC-1, `patches/appworld/experiments/configs/sage_test_normal.jsonnet`, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`; [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).

Maintenance is mechanical: same-name replacement within extraction/dictionaries, append to accumulated evaluation records, re-association with task IDs, index encoding, expert merge, trace filtering, token masking and numerical optimization. Their evidence supports these transformations, not general meaning improvement. Rejection or expiry acts locally: omitted code candidates, failed expert attempts, cleared prompt text, new rollout dictionaries, new scenario libraries and checkpoint retention. The inspected evaluation writer/initializer does not implement an identifier-based withdrawal that purges older list records and their matching vectors together. This bounded observation prevents a claim of coherent library-wide deletion, not a claim about absent external administration. SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`; [MEM-OBJ-skill-embeddings](#mem-obj-skill-embeddings), [MEM-OBJ-query-embeddings](#mem-obj-query-embeddings).

Compaction was specifically challenged: functions are derived from action source, not summaries of conversation meaning; observation cropping loses tails; the retry agent appends feedback; the SFT extractor selects and normalizes traces. These routes retain different products and later consumers. None of the inspected methods warrants labeling the system's shared mechanism as semantic history summarization. This is limited to the paths inventoried, not an absence claim about opaque providers.

## Read-back

There are three distinct deliveries. First, initialization automatically supplies retained source to the interpreter and then conditionally to a model prompt: paired dictionaries, default scenario selection, vector/query/n-gram alternatives, and all expert-scenario functions. The model can choose whether to call a shown function, but it does not initiate the library lookup. Second, later training generation consumes parameters changed through RL or SFT, with checkpoint loading as a separate recovery path. Third, optional adapter caching returns retained responses to an identical-argument call rather than injecting a skill. Selection and authority are recorded beside each actual consumer, not inferred from file existence.

Evaluation output JSONL is durable, but construction reads `./predefined_skill_library/skill_library_functions.jsonl`; no inspected automatic copy/read from the output path closes restart reuse. Query metadata persistence has its additional gap. Expert snapshots likewise have an inspected writer and an in-process consumer, not a demonstrated restart loader. These limits coexist with wired later-task read-back. See [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [MEM-OBJ-query-list](#mem-obj-query-list), [MEM-OBJ-rollout-functions](#mem-obj-rollout-functions); SRC-1, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent_rollout.py`.

## Integration issues

- No supplied record needs a supported value correction from these reads. The following are scope refinements, not replacements: ordinary evaluation pruning is delayed and can miss the final step; default matching uses substring membership; installation exceptions differ from unsuccessful responses. Their consequences are retained in the route annotations. [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install).
- The registered full-code retry agent is an additional context-control route outside the runtime's selected routes. Reconciliation should retain it as an alternate, not as the normal SAGE skill path. [MEM-RTE-api-context](#mem-rte-api-context). Its external demo contents and deployment remain unobserved; no library acquisition claim follows.
- Query-index restart integrity remains unresolved: the writer saves vectors but not the query-list file required by the predefined query loader, and n-gram mode does not load that list. External preparation may supply it, but is not frozen. This prevents complete automatic restart claims. [MEM-OBJ-query-list](#mem-obj-query-list), [MEM-OBJ-query-embeddings](#mem-obj-query-embeddings).
- Predefined function/vector provenance, compatibility and editing authority are unresolved; vector rows may depend on external alignment. Preserve known subsequent transformations without asserting trusted initial content. [MEM-OBJ-skill-embeddings](#mem-obj-skill-embeddings), [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions).
- Appending new evaluation functions is not a universal supersession mechanism because first-name deduplication can select older records. A coherent edit/delete protocol is not established in the inspected writer. [RT-OBJ-skill-library-functions](runtime.md#rt-obj-skill-library-functions), [RT-RTE-evaluation-loop](runtime.md#rt-rte-evaluation-loop).
- Backend checkpoint completeness and actual trace-to-weight-to-behavior dependence remain unobserved. Supplied code-grounded paths support retention wiring, not benefit or exercised self-improvement. [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-RTE-sft-admission](runtime.md#rt-rte-sft-admission).
- Possible duplicates: none identified after comparison. Numerical access parts refine the supplied evaluation container, expert retained functions and dataset are products inside supplied routes, and cache/API-context records name distinct omitted surfaces. The declared `Part of` relations make those containments explicit; no supersession is proposed.

## Limitations and checks

All conclusions are bounded source inspection at SRC-1, not observed operation. Actual library artifacts, generated traces, model weights and provider/Joblib internals are unavailable in the frozen source set; available alternate backend/launcher details were not exhaustively read. These prevent empirical claims of reuse, correctness, safe execution, restart completeness and causal learning benefit. Source HEAD/clean-tree checks and the supplied contracts were rechecked; no additional source or prior analysis was used. Adversarial checks specifically examined imports versus prompt rules, final-step pruning, alternative selectors, predefined load versus output write, expert versus ordinary gates and cache-disabled versus exposed adapter branches.

Deterministic validation: the required `commonplace-run validate-output` invocation passed with “Member content check passes; invocation residue not checked.” This checks structure and quotation occurrence, not claim support or job acceptance.
