---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ExpeL's checkpointed trajectories, retry reflections, counter-maintained insights and evaluation context retrieval at its frozen source boundary."
run-id: AAS-2026-10-14-expel-efd908f05069-01
source-identity: https://github.com/LeapLabTHU/ExpeL
reviewed-boundary: e41ec9a24823e7b560c561ab191441b56d9bcefc
---

# ExpeL memory report

## Boundary and evidence

This member covers training trajectory admission, retry reflection, extraction and rule maintenance, checkpoint/cache restoration, evaluation retrieval, task-context reset, and persisted-log inspection. SRC-1 is the Git source declared in boundary.md. Direct inspection covered `agent/expel.py`, `agent/reflect.py`, `memory/episode.py`, `train.py`, `prompts/templates/human.py`, `configs/agent/expel.yaml`, `tools/visualize_logs.py`; material ranges in `agent/react.py`, `agent/base.py`, `eval.py`, `insight_extraction.py`, and `utils.py`; and repository searches for auxiliary critique callers and retained-state consumers. Implementation and doctrine/design are distinct evidence layers. Supplied runtime records establish the model/embedding dispatch and external adapter boundary; they are not observed execution.

No model calls, target execution, generated insight payloads, saved checkpoint corpus or controlled comparisons were supplied or performed. Provider internals, dependency-managed embedding provenance, and external benchmark services are excluded as in the boundary; these prevent operational and quality conclusions, not source-level tracing. Static shipped examples and method prompts affect context but are not use-derived read-back. There is no newly registered source.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Limits and prevented conclusion |
|---|---|---|---|
| Training admission and task advance | `train.py`, `agent/expel.py`, `memory/episode.py` | Direct reads; [MEM-OBJ-trial-history](#mem-obj-trial-history), annotation on [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) | No actual classified trajectories; reward classification does not certify every statement in a trace. |
| Retry reflection, input trimming and frame discard | `agent/reflect.py`, `agent/react.py`, `agent/base.py` | Direct reads; [MEM-OBJ-reflections](#mem-obj-reflections), training annotation | No generated reflection or behavior trace; scratchpad target excludes other reflection messages. |
| Extraction, operation parsing, counter updates and fold cache | `agent/expel.py`, `insight_extraction.py`, `prompts/templates/human.py` | Direct reads; [MEM-OBJ-rule-items](#mem-obj-rule-items), [MEM-OBJ-rule-counts](#mem-obj-rule-counts), rule-admission annotation | Generality and truth are requested, not mechanically established; fold filtering caveats below. |
| Restore, resume and direct attribute replacement | `utils.py`, `agent/react.py`, `train.py`, `eval.py`, `insight_extraction.py` | Direct reads; checkpoint annotation, [MEM-OBJ-analysis-logs](#mem-obj-analysis-logs) | No observed replay or trusted-file provenance; no transactional recovery claim. |
| Evaluation prompt refresh and similarity alternatives | `agent/expel.py`, `agent/react.py`, `configs/agent/expel.yaml` | Direct reads; [MEM-OBJ-retrieval-docs](#mem-obj-retrieval-docs), evaluation annotation | Unsupported reflection strategy and branch edge cases prevent uniform strategy claims. |
| Model and embedding components | `models/llm.py`, `memory/__init__.py` | Supplied [RT-CMP-gpt-wrapper](runtime.md#rt-cmp-gpt-wrapper), [RT-CMP-embedder](runtime.md#rt-cmp-embedder) | Not reread here; weight identity and provider state remain uninspected. |
| Auxiliary critiques and explicit history clearing | `agent/expel.py`, `prompts/templates/human.py` | Direct reads/searches; [MEM-OBJ-critiques](#mem-obj-critiques), [MEM-RTE-auxiliary-critique](#mem-rte-auxiliary-critique) | Shipped template dispatch lacks required auxiliary keys; successful invocation/later behavior-shaping use not established. |
| Persisted log evaluator | `tools/visualize_logs.py`, `utils.py` | Direct driver and persistence reads; [MEM-RTE-log-inspection](#mem-rte-log-inspection) | Reporting consumer, not a rule rejection gate; aggregation helper internals not exhaustively audited. |
| Benchmark adapters and dataset oracle | `envs/`, `data/` | Supplied [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) and boundary coverage | Dataset records and service internals not inspected here; no outcome authenticity/quality conclusion. |

## Core ideas

ExpeL retains two materially different inputs to later acting: successful trial demonstrations and revised natural-language rules. Failed trials feed comparison-based extraction but do not enter the ordinary demonstration store. Retry reflections provide a third, task-local path. Their archived copies are not automatically equivalent to extracted rules ([MEM-OBJ-trial-history](#mem-obj-trial-history), [MEM-OBJ-reflections](#mem-obj-reflections); SRC-1: `agent/expel.py`, `agent/reflect.py`).

Rule text has model-interpreted authority; counters and operation indices have fixed Python meanings. ADD starts at two, AGREE increases, EDIT changes text and increases, REMOVE decreases, and nonpositive rules disappear from the current pool. A REMOVE request therefore need not immediately withdraw a rule. Counters express update history, not calibrated correctness. Rules reach later critique and evaluation prompts without requiring that their historical reasons accompany them ([MEM-OBJ-rule-items](#mem-obj-rule-items), [MEM-OBJ-rule-counts](#mem-obj-rule-counts), annotation on [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission); SRC-1: `agent/expel.py`).

Retrieval selects a task-associated demonstration, not necessarily the trajectory segment whose embedding matched. Code chooses the shortest trajectory by character length after document ranking. All successful histories, plus shipped examples, supply the candidate pool; extraction's fold exclusion is not also a fold exclusion on this read path. Same-task filtering only excludes the current task. This limits what "held-out evaluation" establishes ([MEM-OBJ-retrieval-docs](#mem-obj-retrieval-docs), evaluation annotation; SRC-1: `agent/expel.py`, `eval.py`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-trial-history
Label: Successful and failed trial history

Source-native identity: `succeeded_trial_history` and `failed_trial_history`, dictionaries of task-keyed lists of `Trajectory` objects. Storage: agent RAM and nested contents of driver pickle snapshots. Form: natural-language task/thought/action/observation strings, with symbolic task keys, list organization and parsed partitions. `_trajectory` is the log-derived text; `_observations`, `_actions`, `_thoughts` and `_steps` are parsed views, not independent source evidence. These are retained traces, not a model-generated generalization. Origin mixes configured task text, actor output, external observations and outcome classification. Training `next_task` admits them computationally based on success and retry/task progression; workflow startup and overwrite confirmation are not per-trace approval. Whole task success is not a truth filter on each contained observation (SRC-1: `agent/expel.py`, `memory/episode.py`, `train.py`).

No operative-object counterpart is supplied. This is retained material produced/consumed by [RT-RTE-training-loop](runtime.md#rt-rte-training-loop), [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) and [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context), not a replacement for those routes. Consumers: critic sees selected success/failure text as evidence for updates; evaluator retrieves success demonstrations. Failed-only tasks do not provide success/failure pairs to `create_rules`; unsuccessful histories remain stored. Direct attribute restore bypasses original classification. Delivery to a model is interpretive evidence/demonstration authority, not action enforcement.

> self.succeeded_trial_history[self.task].append(trajectory)
> --- `agent/expel.py`

> self._observations, self._actions, self._thoughts = [], [], []
> --- `memory/episode.py`

#### MEM-OBJ-reflections
Label: Retry reflections and archived reflection copies

Source-native identity: `reflections`, `formatted_reflection`, `past_reflections` and `Trajectory._reflections`. Form: generated natural-language retry guidance; task/list associations are symbolic access metadata. Storage: active agent lists/strings, copied into trajectories and dictionary checkpoints. Raw input is a failed task's trial plus shipped reflection instructions/examples; output is derived model text. The formatting function prepares that text for another attempt. `past_reflections` appends the most recent reflection when available; it is an archive, not the full retry prompt. Later retry acting consumes formatted reflection, while vectorstore construction can create reflection documents from successful trajectory objects. No shipped reader of `past_reflections` was found in searched drivers/agent/tools; that does not deny arbitrary library callers. New-task reset clears active reflections; retained histories/copies survive (SRC-1: `agent/reflect.py`, `agent/expel.py`, `memory/episode.py`).

No object counterpart supplied; distinct retained parts supporting [RT-RTE-training-loop](runtime.md#rt-rte-training-loop) and [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context). The model authors ordinary content, code admits it without semantic veto; testing `input()` changes authorship to caller-supplied text. There is no separately retained structured reason/support relation for each reflection claim. Actual theoretical content is uninspected.

> self.reflections.append(reflection)
> self.formatted_reflection = self.format_reflections(self.reflections)
> --- `agent/reflect.py`

> self.past_reflections[self.task].append(self.reflections[-1])
> --- `agent/expel.py`

#### MEM-OBJ-rule-items
Label: Rule text and fold caches

Source-native identity: `rule_items`, text members of `rule_items_with_count`, formatted `rules`, and `cache_rules[cache_fold]`. Form: natural-language rule units; list/fold/index organization is symbolic. Storage: in-memory strings/lists/dictionaries and local pickle snapshots. Lineage: selected trial pairs or success groups plus existing rules and shipped critique guidance → model operation proposals → parser/updater → revised list → numbered acting text or cached fold list. Cached lists copy current text, not counters or a per-rule reason graph. The same text is delivered as existing rules to a later critic and as benchmark guidance to an evaluator; these are different authorities. Its content may express general claims, but no actual generated payload establishes every item as a theory. No supplied object counterpart; the material supports [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) and [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting) (SRC-1: `agent/expel.py`, `prompts/templates/human.py`).

Software admits syntactically accepted model operations; no per-rule human approval is shown. Restore and cache loading can replace delivered rules without re-running critique or checking counter history. A missing cache entry delivers an empty rule string. Logs retain trials and proposal text separately, but the acting rule template receives the formatted rule text, not those logs. Withdrawal from the current pool is not erasure of old snapshots or previously copied cache entries.

> self.cache_rules[cache_fold] = list(self.rule_items)
> --- `agent/expel.py`

> self.rules = '\n'.join([f'{i}. {item}' for i, item in enumerate(self.cache_rules.get(load_cache_fold, []), 1)])
> --- `agent/expel.py`

#### MEM-OBJ-rule-counts
Label: Rule retention counters

Source-native identity: integer counts in `rule_items_with_count`. Form: symbolic `(rule text, count)` organization with numeric updater semantics, not an embedding or probability. Storage: list tuples in RAM/checkpoints. Lineage: ADD initializes 2; AGREE/EDIT increment; REMOVE decrements by 1, or by 3 when `list_full` is true. Nonpositive counts are removed and survivors sorted descending. Counters determine retention/order; acting receives the resulting order rather than numeric counters. No supplied object counterpart; distinct from [MEM-OBJ-rule-items](#mem-obj-rule-items) because fixed software decisions, invalidation and downstream visibility differ. Closest supplied route is [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) (SRC-1: `agent/expel.py`).

> rules.append((operation_rule_text, 2))
> --- `agent/expel.py`

Removal/filter/sort passages are retained in the supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission). They support retention policy, not substantive verification. Removal proposal and actual disappearance are separate events; restoration can resurrect old state.

#### MEM-OBJ-retrieval-docs
Label: Retrieval documents and task-associated display trajectories

Source-native identity: `docs`, `combined_history`, `keys2task`, `vectorstore`. Storage: rebuilt RAM document lists, dictionaries and FAISS store; histories remain reachable through checkpoints. Form: document text is natural language; `type`, `task`, `env_name` metadata and lookup mappings are symbolic; dependency-created embeddings/index numerical state are distributed-parametric. Dense encoding is not the readable display trajectory. No supplied object counterpart; [RT-CMP-embedder](runtime.md#rt-cmp-embedder) owns model fixity, while [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context) owns the consumer route (SRC-1: `agent/expel.py`, supplied runtime).

Lineage: all success histories and shipped fewshots → re-parsed/stripped task/action/thought/step/reflection keys → documents → embeddings. FAISS is reconstructed during prompt refresh; the read path does not train embedding parameters. Initialization provenance of shipped examples is outside use-derived trace origin; runtime success histories mix model and environment text. Stored `keys2task` mappings are not the final selector: selected document task metadata locates histories, and code delivers that task's shortest trajectory. Thus a selected key's source trial and displayed trial may differ. Shipped list examples can replace a same-key history through dictionary update. WebShop filtering tests each task's first trajectory, though eventual delivery selects its shortest trajectory. Relevance and quality remain unobserved.

> combined_history = dict(self.succeeded_trial_history)
> --- `agent/expel.py`

> idx, shortest_fewshot = sorted(enumerate([traj.trajectory for traj in self.combined_history[fewshot_doc.metadata['task']]]), key=lambda x: len(x[1]))[0]
> --- `agent/expel.py`

#### MEM-OBJ-analysis-logs
Label: Persisted trial and critique logs

Source-native identity: driver `log`, `true_log`, extraction `all_logs`/`critique_summary_log`, and checkpoint `dicts`. Storage: local `.txt`, `_true.txt`, `.pkl` files; dictionaries include text and selected state. Form: natural-language logs plus symbolic state/resume indices and containers. Pickle contents can include nested `Trajectory` instances even though top-level snapshot selection filters attribute types. These are not opaque model weights. `log_history` extracts a task/interaction view; `include_all=True` includes assembled instruction/example context, so displayed task logs and full prompt logs are not interchangeable (SRC-1: `agent/base.py`, `train.py`, `agent/expel.py`, `utils.py`).

No supplied object counterpart; this material is output/input of [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore), extraction resume and [MEM-RTE-log-inspection](#mem-rte-log-inspection). Critique logs keep selected trial text, model operations and current rule/counter display. They retain evidence of requested edits but are not a structured, exhaustive rationale per rule, and ordinary acting does not read them. Admission is driver-controlled physical I/O, not semantic approval. `.pkl` loading trusts provenance and can replace attributes; text statistics have reporting authority, not model instruction authority.

> pickle.dump(dicts, f)
> --- `utils.py`

> return all_history
> --- `agent/base.py`

#### MEM-OBJ-critiques
Label: Auxiliary critique dictionaries

Source-native identity: `critiques`, `all_success_critiques`, `all_fail_critiques`. Form: model-authored natural-language lists under symbolic task/group keys. Storage: agent dictionaries, eligible for dictionary snapshots when present. Intended lineage: trial pairs, grouped successful traces, or repeated failures → `prompt_critique` → split lines → removal of parenthesized substrings and empty entries. This normalization differs from `create_rules`' operation-based maintenance. No supplied object counterpart; related to but not the rule pool of [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission). Actual resulting content and operation are uninspected (SRC-1: `agent/expel.py`).

> self.all_fail_critiques = {}
> --- `agent/expel.py`

The shipped dictionary supplies only existing-rule compare/success templates, preventing a claim that these auxiliary functions work under standard driver wiring. Search of agents, prompts, tools and three drivers found their definitions but no shipped calls. Later behavioral consumer is unestablished; storage/afforded critique generation alone is not trace-fed learning into acting.

### Routes

#### MEM-RTE-auxiliary-critique
Label: Auxiliary critique generation

Endpoints: explicit library caller → `task_critique`, `success_critique`, or `failure_critique` → `prompt_critique` → normalized critique dictionaries. Owner: caller triggers; code selects traces; model proposes text or testing caller supplies it; code admits nonempty normalized lines. State/effect: auxiliary dictionaries, not `rule_items`. This is a distinct library surface, not a duplicate of [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission). Caller identity/initial approval is unspecified, not assumed human. Benchmark classifications select inputs, but there is no independent critique answer oracle. Intended mode is offline trace critique; successful execution is not established with shipped templates (SRC-1: `agent/expel.py`, `prompts/templates/human.py`).

- Immediate return: `task_critique(return_log=True)` affords a text log; otherwise state mutation, with no rule-admission return.
- Later read-back: uninspected — dictionaries can be checkpointed, but no shipped acting/rule-extraction reader is established.
- Delegated visibility: inapplicable — synchronous model/caller invocation, not a delegated worker.
- Selection predicate: Task pairs require success; success grouping selects training IDs and first success; failure critique requires more than one failed trajectory.
- Invalidation or expiry: Success/failure critique dictionaries are replaced on calls; per-task critiques extend and normalize; no inspected temporal expiry.
- Activation or effect: Afforded dictionary mutation; behavioral authority at a later consumer unestablished.
- Evidence limits: No shipped caller found; auxiliary template keys absent in supplied HUMAN_CRITIQUES; no generated payload or observed operation.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Failure critique checks 13000 tokens, then removes a random selection or one longest/shortest trajectory once; it does not loop until a strict global budget is met. Normalization strips parentheses and empty lines, not semantic validation. Theory assessment is uninspected because no functioning shipped invocation/payload establishes formulated criticism; model processing opacity is not evidence of its absence. No durable behavior-shaping output route is established here.

> HUMAN_CRITIQUES = dict(
>     compare_existing_rules=human_existing_rules_critique,
>     all_success_existing_rules=human_all_success_existing_rules_critique,
> )
> --- `prompts/templates/human.py`

#### MEM-RTE-log-inspection
Label: Persisted log inspection

Endpoints: caller/configured log path → `tools/visualize_logs.py` → text loader → task parser/statistics → plots/printed summaries. Owner: caller chooses file/configuration, Python computes reports. Context/state: persisted task log, benchmark, task count and reporting modes; effects are plots and terminal summaries. Distinct from [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore): it consumes text without restoring agent state (SRC-1: `tools/visualize_logs.py`, `utils.py`).

- Immediate return: Printed summaries and optionally saved plot; no actor invocation.
- Later read-back: Persisted task log reaches an independently invoked reporting consumer.
- Delegated visibility: inapplicable — local reporting, no delegated worker.
- Selection predicate: Configured path/run name selects the log; benchmark/run-name conditions select statistic modes, not relevance-ranked memory.
- Invalidation or expiry: Consumer does not revise source memory; file overwrite remains controlled by the writer.
- Activation or effect: Statistics/plots inform an operator if inspected; no automatic rule rejection/rollback path is wired.
- Evidence limits: No log corpus or report output observed; selected aggregation helpers not exhaustively audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> out = load_trajectories_log(path=cfg.log_path, run_name=cfg.run_name, load_dict=False)
> log = out['log']
> --- `tools/visualize_logs.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-training-loop](runtime.md#rt-rte-training-loop)

Memory parts: [MEM-OBJ-trial-history](#mem-obj-trial-history) and [MEM-OBJ-reflections](#mem-obj-reflections). Training snapshots follow `next_task`, so stored history survives active-context clearing. Trace origin combines task inputs, generated thoughts/actions and benchmark/service observations; outcome signals govern success/failure partitioning, not semantic curation of every line (SRC-1: `train.py`, `agent/expel.py`).

Reflection has a separate context assembled from shipped methods/examples and the previous trial. Code trims the longest trial messages to the prefix before `:` plus `...` until their joined token count is at most 12000. This is deletion/truncation, not a model summary, and excludes system/examples from that target. The derived reflection crosses into the next acting attempt as formatted natural-language guidance; its actual behavioral influence is unobserved. Reflection prompt and acting prompt resets isolate attempts/tasks; archives remain reachable through trajectories/checkpoints. This resembles dropping a task frame while selected values escape, but delivery is by-value text, not a live reference (SRC-1: `agent/reflect.py`, `agent/react.py`).

> lines[ind]  = line.split(':')[0] + ': ...'
> --- `agent/reflect.py`

> while self.token_counter(''.join(lines)) > 12000:
> --- `agent/reflect.py`

#### On [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission)

Retained input/output parts are [MEM-OBJ-trial-history](#mem-obj-trial-history), [MEM-OBJ-rule-items](#mem-obj-rule-items), [MEM-OBJ-rule-counts](#mem-obj-rule-counts) and [MEM-OBJ-analysis-logs](#mem-obj-analysis-logs). Existing rules and selected trials enter a separate critique prompt; ordinary reflection archives do not feed this shipped `create_rules` path. It performs compare and success extraction, not the auxiliary failure-only critique. The method requests generally applicable rules without trial mentions, so contextual derivation is deliberately omitted from delivered guidance; logs remain separately retained and resume uses them, but acting does not reload them as reasons (SRC-1: `agent/expel.py`, `prompts/templates/human.py`).

Direct reads qualify fold selection: compare extraction uses `idx2task[training_id]`, but success extraction uses dictionary enumeration positions `idx in training_ids`, not `task2idx[task]`. Equality of dictionary order to task indices is not enforced here and can change through resumed/caller-restored state. Therefore held-out task exclusion in the success phase is conditional on that alignment, not an unconditional invariant. The loop redundantly rebuilds success groups for each training ID before consuming the last group construction. No observed effect is asserted (SRC-1: `agent/expel.py`).

> for idx, task in enumerate(self.succeeded_trial_history):
>     if idx in training_ids and len(self.succeeded_trial_history[task]) > 0:
> --- `agent/expel.py`

Counter maintenance removes current pool entries only after count exhaustion. Parser requests and prompt budgets do not enforce generality, independent support, hard rule-count limits or global prompt token sufficiency. Cached fold lists and older checkpoints can still contain withdrawn/edited text. Fresh extraction clears working rule text/counters, resumed extraction reuses state; current output reaches next critique and later actor, but a restored cache bypasses semantic reevaluation. The supplied runtime theory/learning limits remain: localized revision and iterative delivery are afforded/wired, actual formulated criticism and beneficial future capacity are unobserved.

#### On [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context)

[MEM-OBJ-retrieval-docs](#mem-obj-retrieval-docs) separates selected embeddings/documents from delivered demonstrations. The trigger is Python prompt refresh before acting calls, not an actor-issued memory query. Inputs are task/latest thought/action/step, strategy, environment type and loaded success history. Code supplies selected examples automatically; software chooses what arrives, actor interprets it. Candidate count is `num_fewshots * buffer_retrieve_ratio`; eventual output count is at most `num_fewshots`. Per-demonstration trajectory tokens must fit `max_fewshot_tokens`, but the task prefix and other prompt parts are outside that check. `BaseAgent.is_truncated` checks full context at 15800 tokens; this is a stop test, not compaction (SRC-1: `agent/expel.py`, `agent/base.py`, `agent/react.py`).

> fewshot_docs = self.vectorstore.similarity_search(queries[query_type], k=self.num_fewshots*self.buffer_retrieve_ratio)
> --- `agent/expel.py`

Delivery replaces the first message containing the old fewshot string, then collapse concatenates adjacent message types. It does not semantically summarize or preserve a source pointer. Training and strategy `none` skip dynamic retrieval but not static examples. `no_rules` removes rule supply, not retrieved demonstrations. Rule delivery/experience authority are already [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting) and [RT-BAP-fewshots-acting](runtime.md#rt-bap-fewshots-acting).

Fold distinction: the candidate pool begins from all success histories, without the `training_ids` exclusion used for extraction. Same-task and duplicate-task filters are not fold filters. This prevents interpreting extraction fold exclusion as isolation of all retrieved evidence. Reranker `task` sorts thought documents by similarity to task text; `random` shuffles a similarity-retrieved environment-filtered subset, not the entire corpus. Reflection documents exist, but `reflection_similarity` has no final dispatch branch. These details qualify selector labels (SRC-1: `agent/expel.py`, `eval.py`).

#### On [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore)

Memory persists through selected top-level attribute dictionaries containing nested text and trajectories, not through an exported persistent FAISS index. Objects excluded by type (model wrapper, embedder, environment, template/parser callables) are rebuilt by drivers; dictionaries/lists can still retain nested objects. Physical file writes separately overwrite log, pickle and optional full-log files. Loading unpickles then sets fields outside each driver's exclusion list, so initialization from current files/configuration and subsequent state replacement are separate controls (SRC-1: `train.py`, `eval.py`, `insight_extraction.py`, `utils.py`, `agent/react.py`).

> dicts.append({k: deepcopy(v) for k, v in react_agent.__dict__.items() if type(v) in [list, set, str, bool, int, dict, Count] and k not in ['openai_api_key', 'llm']}) # not saving complicated objects
> --- `train.py`

Admission: the caller selects a local checkpoint and workflow; software accepts restored fields without per-rule/trajectory truth checks. A trusted caller may supply/edit replacement state, but the generic `load_checkpoint` API does not establish that the principal is human. Training resume and evaluation/extraction have different exclusion lists. Cached rules and resume markers allow bypassing fresh transformation. Historical reason text may remain in logs while later acting sees only restored rule strings/demonstrations; persistence alone establishes no successful read-back or causal effect.

## Write side

Acquisition and admission are separate. Operator configuration/tasks and shipped method text initialize the system. Ordinary model output authors acting/reflection/critique text, benchmark adapters supply observations/outcomes, and code classifies and retains trials. Direct testing input and checkpoint replacement are alternate content supply mechanisms, not proof of human approval of ordinary memory ([MEM-OBJ-trial-history](#mem-obj-trial-history), [MEM-OBJ-reflections](#mem-obj-reflections), checkpoint annotation; SRC-1: `agent/expel.py`, `agent/reflect.py`, `agent/react.py`, `train.py`).

Trace-fed derived updates have two wired later-use chains: failed trial → trimmed reflection input → generated reflection → retry acting; and success/failure pairs or success groups → proposed rule operations → retained rule text/counters → next critique and later evaluation acting. Raw trace retention alone is not the latter transformation. Auxiliary critique normalization has no established later behavior-shaping consumer and shipped-template incompatibility, so it is not silently counted as another working rule-learning path ([MEM-RTE-auxiliary-critique](#mem-rte-auxiliary-critique); SRC-1: `agent/expel.py`, `prompts/templates/human.py`).

Maintenance and rejection: parser formatting checks, substring duplicate checks, EDIT-to-AGREE conversion and positive-count filtering are computational gates. Prompt requests for generality and operation limits are not equivalent to these gates. REMOVE decrements, rather than necessarily deletes; fresh extraction resets current pool, cache load chooses frozen copied text, and restoration may bring back older rules. None of these paths performs an inspected held-out-content validation gate before rule admission. Outcome reporting does not automatically withdraw poor rules ([RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [MEM-RTE-log-inspection](#mem-rte-log-inspection); SRC-1: `agent/expel.py`, `eval.py`, `tools/visualize_logs.py`).

An explicit library `prepare_new_eval` clears success/failure dictionaries, but no call was found in the searched shipped drivers; it does not clear all rule/cache/archive fields. New-task reset discards active frames, while existing history/checkpoint files survive. Historical snapshots/logs may retain removed material, with no automatic file expiry or semantic rollback established in the inspected persistence/update code. External model/provider state remains opaque (SRC-1: `agent/expel.py`, `agent/reflect.py`, `utils.py`).

> def prepare_new_eval(self) -> None:
>     self.succeeded_trial_history = {}
>     self.failed_trial_history = {}
> --- `agent/expel.py`

## Read-back

- Retry guidance: failure triggers separate reflection; retained reflection list is formatted and inserted before the next task attempt. Selected derived text, not the full prior acting frame, crosses into retry authority. Archives remain reachable but archived `past_reflections` has no established shipped direct read consumer ([MEM-OBJ-reflections](#mem-obj-reflections), training annotation; SRC-1: `agent/reflect.py`, `agent/expel.py`).
- Insight updates: extraction foreground driver selects trial IDs; critic receives selected trial text and existing rules. Counters govern preservation/order; changed text becomes another round's existing rules. Resume reloads selected state and extraction log rather than re-deriving everything ([RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), rule-admission annotation; SRC-1: `agent/expel.py`, `insight_extraction.py`).
- Acting rules: evaluation driver selects cache/extraction; full formatted current rules reach the human-message template unless `no_rules`. No query-based selection within rule text and no accompanying historical reason graph are shown. FEVER's MANDATORY prose still relies on interpretation, not a Python veto ([MEM-OBJ-rule-items](#mem-obj-rule-items), [RT-BAP-rules-acting](runtime.md#rt-bap-rules-acting); SRC-1: `prompts/templates/human.py`, `agent/expel.py`).
- Demonstrations: automatic selector retrieves by current task/interaction state, filters/reranks, chooses task-associated shortest eligible traces and replaces fewshots. This is retained success-history read-back mixed with static shipped examples. Per-unit token checks and count limits do not guarantee global context sufficiency. No actor query tool/hook registration is needed for this path; the inspected entry point is `prompt_agent`'s refresh call ([MEM-OBJ-retrieval-docs](#mem-obj-retrieval-docs), evaluation annotation; SRC-1: `agent/react.py`, `agent/expel.py`).
- Reporting: explicit operator/caller log selection sends stored text to local statistics, not to the actor and not to a semantic admission gate ([MEM-RTE-log-inspection](#mem-rte-log-inspection); SRC-1: `tools/visualize_logs.py`).

## Integration issues

1. Qualify the supplied rule-admission/evaluation statements about fold exclusion. Drivers exclude evaluation IDs for extraction, but success grouping compares dictionary enumeration indices to task IDs. Exclusion depends on alignment not enforced by that body. Retrieval independently uses all successes with only current-task/duplicate exclusion. This affects claims about held-out evidence isolation, not proof that contamination occurred in an actual run ([RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission), [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context), [MEM-OBJ-retrieval-docs](#mem-obj-retrieval-docs); SRC-1: `agent/expel.py`, `eval.py`).
2. Auxiliary critique functions are distinct from the working `create_rules` path. Their absent required template keys under shipped HUMAN_CRITIQUES and lack of shipped callers prevent treating them as wired additional maintenance/read-back routes. Custom callers/templates may afford them; their later consumers remain unresolved ([MEM-RTE-auxiliary-critique](#mem-rte-auxiliary-critique), [MEM-OBJ-critiques](#mem-obj-critiques); SRC-1: `agent/expel.py`, `prompts/templates/human.py`).
3. Reflection documents and `past_reflections` are retained, but configured reflection similarity is unsupported in the final selector and no direct archive reader was found. Retention does not establish active reflection retrieval at evaluation ([MEM-OBJ-reflections](#mem-obj-reflections), [RT-RTE-evaluation-context](runtime.md#rt-rte-evaluation-context); SRC-1: `agent/expel.py`, `configs/agent/expel.yaml`).
4. No new declaration duplicates a supplied referent after comparison: new objects identify material consumed/produced by supplied routes, and the two new routes cover auxiliary critique and text-only reporting. Runtime components and behavioral-authority paths are cited, not re-declared. No supersession is proposed.
5. Generated content, exact provenance of restored state, retrieval behavior under all alternate strategies, successful restoration/replacement and actual capacity improvement remain unobserved. Logs can retain operations/evidence but are not a demonstrated per-rule rationale model or actor input. These local unknowns prevent quality, causal benefit and universal branch-correctness claims ([MEM-OBJ-analysis-logs](#mem-obj-analysis-logs), [MEM-OBJ-rule-items](#mem-obj-rule-items), [RT-RTE-checkpoint-restore](runtime.md#rt-rte-checkpoint-restore); SRC-1: `agent/expel.py`, `utils.py`).

## Limitations and checks

The source checkout HEAD was rechecked as e41ec9a24823e7b560c561ab191441b56d9bcefc with clean Git status; identity matches the supplied boundary and source register. Governing prompt, job, member/input types, collection, worker rules and record contract were read completely, including bounded continuation reads. Inspected source methods and searches support architectural conclusions only. Available dataset records, model internals and aggregation helper details were not exhaustively inspected; no operation or causal experiment is implied.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed: "Member content check passes; invocation residue not checked. This is not job acceptance or claim support." The check does not establish semantic correctness, operational success or causal benefit.
