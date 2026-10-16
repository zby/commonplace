---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Agent-R memory: scored search-tree read-back, synthetic revision conversations and lossy dataset conversion, with training consumers unresolved."
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
source-identity: "https://github.com/ByteDance-Seed/Agent-R"
reviewed-boundary: "82fcc1ca7873b460949ed49022146dd988c32e31"
---

# Agent-R memory report

## Boundary and evidence

Agent-R retains environment-interaction trees for a separate revision-data invocation. It does not ship an implemented route from that dataset through training back to a later actor. This report stays within the builder/improvement plane and partial loop fixed by [the boundary](boundary.md). The registered source is SRC-1 at commit `82fcc1ca7873b460949ed49022146dd988c32e31`. Source reads establish implementation; README establishes design. No observed-run or causal-experiment evidence was supplied.

Included surfaces are all three task adapters, tree serialization/reloading, path selection and critique, synthetic conversations and their metadata, exposed dataset conversion and context helpers, evaluation result retention, progress/storage helpers, and actor/verifier context supply. Static prompts and unchanged weights are contextual inputs, not accumulated experience read-back. External environment state, FastChat internals, provider retention, checkpoint provenance and Xtuner ingestion are outside the captured implementation. Their unknown contents prevent conclusions about initialization trust, complete trajectories, actual training and later capacity.

Direct reads covered the full `mcts_collection.py`, `path_collection.py`, `eval.py`, `mcts_utils/mcts_raw.py`, `mcts_utils/llm_server.py`, all three adapters, `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/sciworld/data_utils_sw.py`, and `README.md`. These include auxiliary surfaces beyond the runtime's initial reads. The supplied runtime is cited where its records already describe the same route. HEAD and a clean source worktree were checked; the complete tracked-path inventory and searches across Python definitions/calls checked alternate storage, prompt, progress, rewrite, prefix and cleanup surfaces. The tree contains no separate tool registry or hook dispatch; the three drivers and exposed Python functions are the inspected invocation boundary.

| Entry point or operation | Source paths (SRC-1) and inspection basis | Covering records or explicit limit |
|---|---|---|
| Collect, deduplicate, backpropagate and save trees | Direct: `mcts_collection.py`, `mcts_utils/mcts_raw.py`, `mcts_utils/webshop/mcts_ws.py`, `mcts_utils/textcraft/mcts_tc.py`, `mcts_utils/sciworld/mcts_sci.py` | [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection); [MEM-OBJ-extended-node](#mem-obj-extended-node); [MEM-OBJ-node-statistics](#mem-obj-node-statistics) |
| Reload, rank, filter and synthesize revision examples, including good-only and no-critique modes | Direct: `path_collection.py`, `mcts_utils/llm_server.py`; supplied runtime independently rechecked | [RT-RTE-revision-export](runtime.md#rt-rte-revision-export); separate conversation, loss and feedback records below; threshold defect prevents successful nonempty CLI export |
| Convert exported examples to conversation JSON | Direct: `mcts_utils/llm_server.py`, `rewrite` and callers searched in all Python files | [MEM-RTE-dataset-rewrite](#mem-rte-dataset-rewrite); callable operation, no shipped invocation or trainer wiring |
| Actor context pruning and replay | Direct: all adapters and `mcts_utils/llm_server.py` | Annotations on collection/evaluation; current-run deletion is not a retained summary |
| Evaluate and execute caller-supplied prefix | Direct: `eval.py`, `mcts_utils/llm_server.py` | [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation); [MEM-OBJ-final-result](#mem-obj-final-result); prefix origin and any durable source are unspecified |
| SciWorld demonstration/history prompt composers and instance builders | Direct: full `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/sciworld/data_utils_sw.py`; callers searched | [MEM-CMP-context-helpers](#mem-cmp-context-helpers); no shipped retrieval/durable-memory caller established |
| Generic readers/writers, replication and progress | Direct: `mcts_utils/llm_server.py`; callers searched | [MEM-OBJ-progress-file](#mem-obj-progress-file); helpers afford storage/replication, not autonomous maintenance or a later consumer |
| Checkpoint initialization and alternate API | Direct: `mcts_utils/llm_server.py` and drivers; supplied runtime | [RT-CMP-func-call-offline](runtime.md#rt-cmp-func-call-offline), [RT-CMP-func-call](runtime.md#rt-cmp-func-call); parameter lineage and remote retained state opaque |
| Training and subsequent actor adoption | Direct README plus tracked inventory; supplied runtime | [RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery); intended Xtuner role only; ingestion, mask handling, parameter update and admission unestablished |
| Task-ID JSONs and method graphics | Available but contents uninspected | Drivers' file usage inspected; no conclusions about complete benchmark membership, original curation or diagram-specific behavior |

## Core ideas

1. **Experience is retained as a tree, not a reusable textual rule.** Natural-language responses and observations remain alongside symbolic branch/score metadata. A later builder reads both, but the verifier receives selected action/observation text rather than the whole tree or reward statistics. [MEM-OBJ-extended-node](#mem-obj-extended-node) and [MEM-OBJ-node-statistics](#mem-obj-node-statistics) separate these consumers.
2. **Revision content and its rationale are different outputs.** Critique can delimit a low-path prefix. Software then inserts a stock correction thought and fabricated wait exchange, followed by a high-path continuation. Reasons survive as sidecar feedback, not as the inserted actor rationale. The exposed converter drops those reasons and the loss flags. [MEM-OBJ-revise-log](#mem-obj-revise-log), [MEM-OBJ-revise-feedback](#mem-obj-revise-feedback) and [MEM-RTE-dataset-rewrite](#mem-rte-dataset-rewrite) trace this distinction.
3. **Context shortening is deletion, not semantic compaction.** Search trims a model-call copy, then stores the untrimmed history; ordinary evaluation trims the state it ultimately saves. Prefix evaluation keeps a second full history. None of these inspected loops produces a summary for later invocation. See the route annotations, grounded in SRC-1, the three adapters and `mcts_utils/llm_server.py`.
4. **Retained examples do not close the learning loop.** Training is declared externally, and the export thresholds fail when reached. The source demonstrates an intended trace-to-training-material transformation, not successful training, deployment, or improved future capacity. [RT-RTE-revision-export](runtime.md#rt-rte-revision-export) and [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training) supply the controlling evidence and limits.

## Shared records

### Components

#### MEM-CMP-context-helpers
Label: SciWorld context helper functions

Source-native `compose_prompt_to_nextactions`, `compose_prompt_to_plan`, `clean_history`, `compose_instance_v1` through `compose_instance_v5` (including `v1_1`), and object/place accumulators are exposed Python functions. Storage substrate: caller-owned lists, strings and dictionaries in process memory. Prompt text and demonstrations are natural language for hypothetical model interpretation; action formalization, history filtering and windows are symbolic transformations. No counterpart after comparison with the runtime records: [RT-RTE-sciworld-action](runtime.md#rt-rte-sciworld-action) covers a different function and its actual `step` consumer.

The composers receive demonstrations from the caller; they do not retrieve them or establish their origin. Next-action context takes the first one or two demos, filters history against the first demo's action types and uses the final `k` cleaned entries (default 10). Planning uses the first demo and cleaned observations, restricted to the final 15 in lite mode. Instance variants expose previous actions/observations, score, inventory and optional seen objects/places; v3 uses five history entries, v4/v5 ten. The seen-object accumulator removes oldest objects above its default limit of 20. These are curation/context-supply capabilities, not evidence that any durable experience is read back in the shipped drivers. Human selection, persistence and actual consumer authority remain unspecified. `get_model_output` affords tokenizer-truncated inference on supplied input, but no shipped caller links these composed prompts to it.

Evidence: SRC-1, `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/sciworld/data_utils_sw.py`; definitions and call-site search across all tracked Python files. No observed activation.

> prompt_to_next_actions += history[-k:]
> --- `mcts_utils/sciworld/eval_utils_sw.py`

> while len(objects) > limit:  # recent seen objects, only keep M = 20
>     objects.pop(0)
> --- `mcts_utils/sciworld/data_utils_sw.py`

### Operative objects

#### MEM-OBJ-extended-node
Label: ExtendedNode interaction content
Part of: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)

This object is the retained interaction-content part of the collection route, not another route declaration. Source-native `ExtendedNode` stores `state`, `llm_response`, `action`, `obs` and `recent_actions`. Storage substrate: a FastChat conversation and Python fields during collection, then recursive JSON under `mcts_result/{Task}/{model_name}/search_results_{idx}.json`. Form: model thoughts and observations are natural language; role/content framing and replay action strings have symbolic consumer rules. There is no embedding or opaque compressed payload in this inspected representation. Text remains readable rather than being a display summary of another payload.

Lineage mixes externally supplied instructions/observations, actor responses and software normalization. New observations have tabs/newlines replaced with spaces. SciWorld may replace the action while retaining the actor response, so the response and executed action need not agree. WebShop/TextCraft recent actions are two-element sequences; SciWorld serializes action-observation strings. SciWorld critique splits those strings by comma, making observations containing commas a further possible parsing failure. Original environment contents and checkpoint lineage are uninspected.

Consumers: current branch reset/replay uses recent actions; the later revision builder loads the tree, uses the root message state and individual responses/observations, and feeds selected action/observation text to a verifier. Loaded `state` is a list of message mappings, not a recreated FastChat conversation; the loader rebuilds children but not parent links or environment clients. It supports the builder's traversal, not a demonstrated resumable search checkpoint. Authority: evidence and generation inputs at the builder/verifier, not a direct later evaluator policy. Source trust is inheritance from external task responses and actor text; collection supplies no independent provenance certification.

Evidence: SRC-1, all three adapter paths above, `mcts_utils/mcts_raw.py`, `path_collection.py`; container route supplied by runtime.

> 'state': self.state.to_openai_api_messages(),
> 'children': [child.to_dict() for child in self.children]
> --- `mcts_utils/webshop/mcts_ws.py`

> node = ExtendedNode(**data)
> node.children = [dict_to_node(child) for child in children_data]
> return node
> --- `mcts_utils/webshop/mcts_ws.py`

#### MEM-OBJ-node-statistics
Label: ExtendedNode score and tree metadata
Part of: [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)

This is the separately consumed symbolic part of the same JSON tree: visits, cumulative value, prior, stored `puct_value`, depth, terminal flag, environment score, disaster flag and child structure. Substrate: Python node fields, then recursive JSON. Lineage: environment reward/done plus fixed search updates; negative scores become zero with disaster/terminal flags. A negative score's magnitude is not retained as `env_score`. Cumulative value is not a certified correctness probability.

During search, node statistics control branch selection. Later `path_collection.py` uses positive root value, terminal childless leaves and leaf average value for ranking/pairing; the high-path threshold separately tests cumulative leaf value. Verifier prompts do not include these statistics. Loader omission of parent reconstruction makes stored `puct_value` a recorded number rather than proof of reconstructed live search dynamics. Authority is software successor/example selection; the environment is the outcome oracle, with its correctness outside the source boundary. Distinct from [MEM-OBJ-extended-node](#mem-obj-extended-node): different consumers and representational rules within the same container.

Evidence: SRC-1, `mcts_utils/mcts_raw.py`, the three adapters, `path_collection.py`.

> def node_avg_value(node):
>     return node.value / node.visits if node.visits > 0 else 0.0
> --- `path_collection.py`

#### MEM-OBJ-revise-log
Label: Revision conversation content
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Source-native `revise_log` is a derived conversation, stored in Python message mappings and then appended as JSONL under the selected output directory. Natural-language operative content consists of root context, low-path responses/observations, a sampled stock correction thought with `Action: wait` and fabricated `ok.`, then high-path responses/observations. Role/order fields are symbolic framing. It is not a fresh observed environment trajectory: successful continuation is spliced without validating compatibility with the bad prefix's reached state. The pairing has no same-parent requirement, as the container route establishes.

In paired mode optional verifier judgment determines prefix length; without critique the full low path is used. Initial identical response text is skipped in the high continuation. In `good` mode there is no synthetic correction or bad prefix. Thus trace origin is mixed: environment interaction, model generation and shipped template content. Automatic construction, not per-example human editing/approval, authors the derived artifact; caller identity and any outside curation remain unresolved.

Consumer: `rewrite` reads this field; external Xtuner training is intended by README, with actual ingestion unknown. Authority at `rewrite` is conversion input, not model behavior. No shipped inference driver reads this dataset directly. Retained corrective wording does not establish a reliable agent diagnosis or a parameter update. Distinct material content part of the runtime export route; loss flags and feedback below have different consumer paths.

Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`, `README.md`; exact construction passages supplied by [RT-RTE-revision-export](runtime.md#rt-rte-revision-export).

#### MEM-OBJ-loss-flags
Label: Revision conversation loss fields
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Source-native `loss` fields are symbolic booleans on exported assistant messages; substrate is the same Python mappings/JSONL as `revise_log`. Lineage is software construction: low-path assistant messages receive false, correction cue and good continuation receive true. They express intended training selection rather than natural-language instruction. No inspected trainer consumes them; the exposed `rewrite` conversion omits them. Their behavioral authority is therefore unestablished at an optimizer and not inferred from their name. Distinct from conversation content and critique reasons because conversion preserves the former but drops these fields.

Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`.

> bad_log.append({"role": "assistant", "content": node.llm_response, "loss": False})
> --- `path_collection.py`

> good_log.append({"role": "assistant", "content": node.llm_response, "loss": True})
> --- `path_collection.py`

#### MEM-OBJ-revise-feedback
Label: Revision feedback and source-path sidecars
Part of: [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Source-native `revise_feedback`, `high_log`, `low_log`, `task_description`, `task_num` and `revise` preserve diagnostics and partial lineage in paired JSONL rows. Textual path logs and full verifier responses/reasons are natural language; task identifiers, mode flags and extracted judgment framing are symbolic. Storage is process mappings/lists and JSONL. Feedback records each inspected action/observation and judgment; no-critique mode stores an empty string, while good-only output omits these paired sidecars.

The model's judgment has immediate authority over prefix truncation through [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix). Its retained reasons are not copied into the revision cue, and no subsequent reader of this feedback field is established in the tracked Python code. `rewrite` uses only `revise_log`; it omits the sidecars. Source path logs preserve text, not complete tree identity, score history, model checkpoint provenance or a checked causal explanation of failure. Retention of reasons is therefore real but their later use is not established.

Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`; existing authority record cited rather than duplicated.

> revise_feedback.append({
>     "revision_feedback": response,
>     "action": node.action,
>     "obs": node.obs,
>     "judgement": judgement
> })
> --- `path_collection.py`

#### MEM-OBJ-final-result
Label: Evaluation final_result
Part of: [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation)

Source-native `final_result` holds task/model label, final environment score, continuation step count and message state. Substrate: Python dictionary and JSON under `test_result` or the exposed prefix helper's `revise_result`. Natural-language content is the surviving conversation; labels/count/score/framing are symbolic evaluation metadata. Ordinary evaluation saves its already-pruned `conv`; `perform_test_revise` saves a separate `history`, preserving full continuation content despite pruning the inference conversation. These are different retained trace completeness conditions, not alternative summary formats.

Lineage: external initial instruction/observations, actor responses and, for the helper, caller-supplied prefix responses. Prefix provenance is unspecified; the helper does not itself fetch retained examples. No later consumer of these result files is established in the shipped drivers. They provide result-storage capability, not training feedback read-back. Configured `model_name` is a label, not a pinned checkpoint identity. No overlap with the tree-content object beyond similar message encoding.

Evidence: SRC-1, `eval.py`, `mcts_utils/llm_server.py` and the supplied evaluation route.

> "state": history.to_openai_api_messages(),
> --- `mcts_utils/llm_server.py`

#### MEM-OBJ-progress-file
Label: Optional progress_file integer

Source-native `progress_file` in `get_last_processed_index`/`update_progress` is symbolic access metadata: a decimal index in a caller-selected text file. It is not task knowledge or model context. A caller can overwrite/read the index; initialization returns zero for a missing/empty file. No caller appears in the inspected drivers, so this is an exposed storage capability, not a wired resume mechanism. Admission is the supplied index through physical file I/O; human authorship/approval is unspecified. No counterpart after comparison with [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection), whose existing-output check is a different recovery mechanism.

Evidence: SRC-1, `mcts_utils/llm_server.py`, complete Python call-site search.

> def update_progress(progress_file, index):
>     """Update the last processed index in the progress file."""
>     with open(progress_file, 'w', encoding='utf-8') as f:
>         f.write(str(index))
> --- `mcts_utils/llm_server.py`

### Routes

#### MEM-RTE-dataset-rewrite
Label: Revision dataset conversation rewrite

Endpoints: caller-supplied dataset rows → `rewrite` field/position extraction → conversation JSON file. Owner: `mcts_utils/llm_server.py` function. Trigger is a library call, not any of the shipped CLIs. Proposed change is output format and content selection, not actor weights. Software decides extraction; caller supplies input and destination, with per-content human decision unresolved. No answer oracle or model participates. Mode is deterministic dataset conversion. Guidance is fixed positional mapping; it neither diagnoses correctness nor verifies the exported role order. Distinct identity from [RT-RTE-revision-export](runtime.md#rt-rte-revision-export): it consumes that route's content but is not called within that route.

- Immediate return: Writes JSON through `save_json`; implicit Python return has no conversation payload.
- Later read-back: uninspected — a caller can supply retained JSONL rows using exposed readers, but no shipped caller or trainer is linked to this output.
- Delegated visibility: No model/provider receives anything here; the file holds only conversation fields extracted from `revise_log`.
- Selection predicate: All supplied rows; positions 0/1/2 become system/input/output, then positions 3 onward become alternating input/output pairs. An unmatched trailing entry is omitted.
- Invalidation or expiry: Output is overwritten with file mode `w`; no content-version check, expiry or row-specific withdrawal.
- Activation or effect: Converts natural-language conversation content into a different symbolic wrapper; drops role/loss fields and paired diagnostics. No parameter update or exercised downstream behavior established.
- Evidence limits: Arbitrary input structure is not validated; no supplied output or invocation trace; trainer use and mask semantics remain unresolved.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission/rejection: there is no semantic admission gate in this converter; malformed short logs can fail indexing. The caller could replace inputs or rerun to replace the output, but no automatic rollback/transaction is supplied. This is a derivative of trace-fed material, not an independently demonstrated durable learning update. Its output retains conversation text rather than the verifier's reasons or explicit training mask.

Evidence: SRC-1, `mcts_utils/llm_server.py`; full definition and call-site search.

> revise_log = data["revise_log"]
> temp = {
>     "system": revise_log[0]["content"],
>     "input": revise_log[1]["content"],
>     "output": revise_log[2]["content"],
> }
> --- `mcts_utils/llm_server.py`

> final_dataset.append({"conversation": conversation})
>
> save_json(final_dataset, output_path)
> --- `mcts_utils/llm_server.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)

Memory consumers: a later revision CLI loads persisted trees; the actor receives current branch conversation rather than stored tree statistics. Its selector begins with a caller-selected input directory and all numerically sorted JSON filenames, not task-semantic retrieval. The builder then selects leaves using reward metadata. This is requested batch pull, not unsolicited context injection; task IDs label files rather than proving content-targeted retrieval.

Context budget: all adapters count tokenized `str(conv)` against `max_len - 60`, remove positions 4:6, and sometimes 2:4. The model receives the resulting message conversion. Search subsequently copies the full node state again, so the durable tree contains material omitted from the actor call. This restores storage, not model visibility. The loop can stop making progress or index past available messages; no unconditional budget fit follows. Evidence: SRC-1, all three adapters and `path_collection.py`.

> prompt = conv.to_openai_api_messages()
> agent_response = self.calling.llm_func(prompt, self.model_name)
> ind = 1
> disaster = False
> agent_response = agent_response.strip()
> conv = deepcopy(node.state)
> --- `mcts_utils/webshop/mcts_ws.py`

#### On [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Read-back/curation: root and leaf filtering consume the tree's symbolic statistics, while critique gets a task description from `low_path[-1].state[3]["content"]`, preceding low-path actions/observations, and the current action/observation. It does not get the successful alternative or scores. Provenance of that fixed message position depends on the external initial conversation/template. The prompt calls every supported task a science task, even WebShop/TextCraft; that wording does not certify domain-specific evaluation.

Budget: only preceding action/observation text is shortened, using whitespace word count and six-character deletion. Task description and current action/observation are added afterward; no total tokenizer budget is enforced. This can cut text within a semantic unit and provides no retained summary. The intended subsequent consumer is external training, not a direct actor memory lookup. Retained reasons have no established later reader; conversion omits them. Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`.

> while len(action_obs_prompt.split()) > max_len - 60:
>     action_obs_prompt = action_obs_prompt[6:]  # Truncate prompt if too long
> --- `path_collection.py`

#### On [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation)

Memory retention: ordinary evaluation deletes history directly from the conversation later saved in `final_result`. Prefix evaluation creates `history = deepcopy(conv)` before continuation and appends new responses/observations to both histories, but prunes only `conv`. The full stored trace is not automatically delivered back to the actor. No summary/compaction result is retained. Supplied prefix input affords immediate context/action continuation; a retained-source read-back route remains unspecified. Evidence: SRC-1, `mcts_utils/llm_server.py`, `eval.py`.

## Write side

**Acquisition and tree admission.** The environment supplies initial instructions and state; the actor authors response strings. Caller control over task range, weights and budgets is not per-content approval. Software admits children after generation, removes exact duplicate responses only after their environment steps, and backpropagates terminal scores. The driver saves the final recursive tree after search returns. The existing filename check suppresses recollection without checking model/source freshness. These transformations retain raw interaction text plus derived statistics, not a distilled reusable method. See [MEM-OBJ-extended-node](#mem-obj-extended-node), [MEM-OBJ-node-statistics](#mem-obj-node-statistics) and [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection); SRC-1, `mcts_collection.py`, all adapters and `mcts_utils/mcts_raw.py`.

**Revision admission and transformation.** A separate invocation reads trees, rejects nonpositive roots and intends to apply gap/high-path thresholds. Software selects pairs; the optional verifier proposes usefulness judgments, whose string test controls prefix length rather than correctness certification. As shipped, string-valued `ALPHA`/`BETA` cause reached numeric comparisons to fail; this qualifies every claim of export, including good-only mode. No same-parent or environment-compatible-splice gate is implemented. JSONL append occurs only after the selected construction completes. There is no per-example approval, deduplication, automatic expiry or row-specific rejection after writing in this driver. Unknown outside curation remains unknown. [RT-RTE-revision-export](runtime.md#rt-rte-revision-export) retains the exact threshold and construction evidence; SRC-1, `path_collection.py`.

The intended trace-fed chain is environment/actor interactions → scored tree → selected path text and optional critique → derived training conversation. Its inspectable durable behavior-shaping target is the dataset, conditional on successful export; a later optimizer/actor chain is only declared. Reasons are stored separately; the actor correction text is static. The exposed converter retains text but drops reasons and loss flags, so rationale cannot be assumed to survive every checkpoint form. [MEM-OBJ-revise-log](#mem-obj-revise-log), [MEM-OBJ-loss-flags](#mem-obj-loss-flags), [MEM-OBJ-revise-feedback](#mem-obj-revise-feedback) and [MEM-RTE-dataset-rewrite](#mem-rte-dataset-rewrite) separate those forms.

**Maintenance, rejection and withdrawal.** Within the directly inspected drivers/functions, collection has completion-only saving, export appends, rewrite/evaluation overwrite, and progress writes overwrite an optional index. Caller file deletion/replacement is possible under host permissions but is not a shipped curation/withdrawal workflow. Dataset replication (`expand_dataset`) repeats supplied entries; generic readers/writers provide physical I/O, not semantic admission. No call connects progress helpers to collection or rewrite to training. No automatic propagation from evaluation results into a revised dataset or checkpoint was found in the complete Python call-site inspection. This is a bounded wiring limit, not proof that operators never do so externally. Evidence: SRC-1, the three drivers and `mcts_utils/llm_server.py`; evaluation record [MEM-OBJ-final-result](#mem-obj-final-result).

## Read-back

The only shipped cross-invocation retained-content consumer established here is the revision builder's pull from persisted search trees. The CLI chooses a directory; filesystem enumeration selects JSON files; leaf metadata selects paths; optional critique sees a truncated low-path text subset; software emits a new conversation. Selection is batch reward filtering, not a query-conditioned knowledge lookup. Material authority differs at each consumer: tree scores select examples, action/observation text informs model judgment, judgment text controls prefix extent, and content becomes an intended training input. The relevant supplied routes and object records above bound actual wiring and threshold failures (SRC-1, `path_collection.py`).

Within collection/evaluation, accumulated history reaches subsequent model calls in the same rollout. It remains ordinary current-run context, not an independently retained read-back mechanism under the contract. Pruning does not create a summary. Static verifier prompts and revision thoughts guide construction without being updated by use. Auxiliary SciWorld composers and prefix evaluation accept caller data but establish no storage-to-later-invocation route by themselves. `rewrite` is an exposed consumer operation on supplied rows, not deployed trainer wiring. There is no automatic push selector that supplies independent retained experience to the shipped evaluator (SRC-1, all adapters, `mcts_utils/llm_server.py`, `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/sciworld/data_utils_sw.py`).

The README names external Xtuner training as the intended next consumer. Neither its actual input schema, loss-mask behavior nor the resulting checkpoint's later consumption is captured. Later `MODEL_DIR` initialization permits caller-selected weights but does not identify them as a trained derivative of this run. These limits preserve the distinction between dataset curation, persistent experience, future learning capacity and exercised improvement; [RT-CMP-func-call-offline](runtime.md#rt-cmp-func-call-offline), [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training) and [RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery) provide the boundary evidence.

## Integration issues

- **No correction to a supplied fact.** Direct inspection corroborated the runtime's export type defects, distinct-path pairing, static revision cue, context deletion and incomplete training loop. Additional qualifications concern actual material reaching consumers rather than changed route identity.
- **Part ownership, not duplicate declarations.** Interaction text and score metadata are parts of [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection); conversation content, loss flags and feedback are parts of [RT-RTE-revision-export](runtime.md#rt-rte-revision-export); evaluation results are part of [RT-RTE-agent-evaluation](runtime.md#rt-rte-agent-evaluation). Their different consumers require separate objects, not replacement of the valid route containers. Context/progress helpers and dataset rewrite have no identical supplied counterpart.
- **Alternate conversion loses training metadata.** [MEM-RTE-dataset-rewrite](#mem-rte-dataset-rewrite) omits [MEM-OBJ-loss-flags](#mem-obj-loss-flags) and [MEM-OBJ-revise-feedback](#mem-obj-revise-feedback). SRC-1, `mcts_utils/llm_server.py`, proves the field extraction; no caller establishes that this is the actual training path. Reconciliation must not attribute the JSONL's loss/rationale semantics to every proposed training input.
- **Stored tree is not a complete environment/search checkpoint.** [MEM-OBJ-extended-node](#mem-obj-extended-node) loads message dictionaries and children without parent/environment reconstruction; stored numerical metadata in [MEM-OBJ-node-statistics](#mem-obj-node-statistics) has different live/reloaded semantics. SRC-1, all adapter loaders. The builder's consumption is supported; resumed search is not.
- **SciWorld content alignment and parsing remain conditional.** Executed action can differ from actor response; recent action-observation strings can contain commas that defeat critique unpacking. SRC-1, `mcts_utils/sciworld/mcts_sci.py`, `path_collection.py`; [MEM-OBJ-extended-node](#mem-obj-extended-node). No run samples establish incidence. Export correctness cannot be inferred from serialized text alone.
- **Auxiliary consumers and initialization remain unresolved.** No shipped caller establishes retained demonstration delivery for [MEM-CMP-context-helpers](#mem-cmp-context-helpers), index-driven recovery for [MEM-OBJ-progress-file](#mem-obj-progress-file), or retained origin for the prefix helper. SRC-1, full Python call-site search at the reviewed commit. External initial instruction content and checkpoint lineage are uninspected. These prevent expanded memory/trust conclusions, not the supported tree-to-builder path.
- **Training and benefit remain unclosed.** External ingestion, mask interpretation, checkpoint acceptance and later actor behavior require evidence not supplied; the threshold failure further prevents claiming a successful nonempty export. [RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery), [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), SRC-1, `README.md`, `path_collection.py`. No trained memory authority or improved capacity is established.

## Limitations and checks

Source and method identity were rechecked against the supplied boundary, member types and record contract. The registered source HEAD equals the reviewed commit; reads used that checkout without target execution, dependency installation or provider calls. Available JSON membership data and graphics were not inspected; this prevents dataset-coverage and diagram-specific conclusions. No additional source ID or evidence layer was introduced. Direct helper reads extend inspected coverage without changing the frozen boundary.

The analysis searched for countercases before concluding: good-only/no-critique modes against the critique account; full retained node state and prefix history against a blanket pruning claim; exposed rewrite and SciWorld prompt functions against a CLI-only inventory; and stored field selection against an assumption that reasons/masks reach training. All resulting distinctions and unresolved consumers are retained above.

Deterministic validation: the assigned member/artifact/role check passed with no findings. This establishes structural and quotation checks only, not source interpretation, successful export, observed memory activation, or demonstrated benefit.
