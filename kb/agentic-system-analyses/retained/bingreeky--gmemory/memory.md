---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "GMemory memory: task-document replay, graph-mediated selection, rule revision and transient workflow context at the frozen source boundary."
run-id: AAS-2026-10-15-gmemory-a2192cc823f7-01
source-identity: https://github.com/bingreeky/GMemory
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
---

# GMemory memory report

## Boundary and evidence

This report covers the whole shipped memory-to-task loop in [boundary](boundary.md), using SRC-1 at the declared revision. Included surfaces are current task context, Chroma task documents, the persisted task graph, insight text and access metadata, extraction/diagnosis, rule operations, merging, outcome credit, role projection, and the three workflow consumers. The CLI and launcher select these paths; they are not model tools. Comparator memory implementations remain excluded. External provider state, dependency internals, benchmark resources and uncaptured live services prevent conclusions about actual model behavior, retrieval quality or simulator correctness.

Direct source reads cover the entire `mas/memory/mas_memory/GMemory.py`, `mas/memory/common.py`, `mas/memory/mas_memory/memory_base.py`, `tasks/mas_workflow/format.py`, `tasks/run.py`, `mas/module_map.py`, `mas/utils.py`, `mas/agents/base.py`, `run_mas.sh`; the GMemory prompt definitions in `mas/memory/mas_memory/prompt.py`; and the consumer ranges in the table. These add implementation and doctrine/design evidence under the existing SRC-1, not a new source or observed execution. Runtime findings supply the generation backend, environment outcome interpretation, and orchestration details not independently audited here. No target code was executed. No access gap was encountered in these source reads.

| Entry or memory operation | SRC-1 paths and inspection basis | Coverage and limit |
|---|---|---|
| Shell/CLI/module dispatch and restart | Direct: `run_mas.sh`, `tasks/run.py`, `mas/module_map.py`, `mas/memory/mas_memory/GMemory.py` | One reused memory object; Chroma, pickle and JSON reload. [RT-RTE-task-retention](runtime.md#rt-rte-task-retention), [MEM-OBJ-task-layer](#mem-obj-task-layer). No deployed store snapshot supplied. |
| Current task, agent-message recording, save and summarize | Direct: `mas/memory/mas_memory/memory_base.py`, `mas/memory/common.py` | [MEM-OBJ-mas-message](#mem-obj-mas-message), [MEM-OBJ-state-chain](#mem-obj-state-chain), [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip). Text and graph differ; attempted deletion is ineffective. |
| Retrieval, graph expansion, similarity, model reranking | Direct: `mas/memory/mas_memory/GMemory.py` | Annotation on [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery). Graph candidates can be replaced by fallback searches. Actual results uninspected. |
| Extraction, digit removal, key steps, failure explanation | Direct: `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py` GMemory sections | Annotation on [RT-RTE-task-retention](runtime.md#rt-rte-task-retention). Requests do not establish faithful condensation or correct diagnosis. |
| Rule operations, sampling, rejection, score pruning and backward | Direct: `mas/memory/mas_memory/GMemory.py`, GMemory prompts | [MEM-OBJ-insights-rule](#mem-obj-insights-rule), [MEM-OBJ-insights-metadata](#mem-obj-insights-metadata), annotation on [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance). No semantic validation or retained versions in these routines. |
| Cluster-based merge, separate admission path | Direct: `mas/memory/mas_memory/GMemory.py`, merge prompts | [MEM-RTE-cluster-merge](#mem-rte-cluster-merge). Numbered-list parsing bypasses operation checks. |
| AutoGen replay and optional projection | Direct: `tasks/mas_workflow/autogen/autogen.py` schedule and projector; formatter | [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance). Failed examples omitted, rule credit uses raw cached strings. |
| DyLAN replay and local frames | Direct: `tasks/mas_workflow/dylan/dylan.py` schedule; supplied neuron/reset account | [RT-RTE-dylan-actions](runtime.md#rt-rte-dylan-actions). Saves but omits backward. Full helper bodies not independently audited; no exhaustive critique-context claim. |
| MacNet replay and temporal history | Direct: `tasks/mas_workflow/macnet/graph_mas.py` schedule, `tasks/mas_workflow/macnet/node.py` storage/selection/execute; supplied helper account | [MEM-OBJ-node-memory](#mem-obj-node-memory), [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions). Actual graph realization uninspected. |
| Projection API with optional trajectory | Direct: `mas/memory/mas_memory/GMemory.py` and projector prompts; schedule call-site search | API affords trajectory-conditioned projection; inspected schedule calls pass only insights and role. No shipped later consumer of a trajectory-conditioned projection established. |
| Logs, evaluation and initialization | Direct: GMemory logging and JSON loading; supplied [RT-RTE-autogen-actions](runtime.md#rt-rte-autogen-actions) outcome account and runtime log-header limits | `insights.log` records maintenance prompts/responses, but no automatic replay of that log was found in the inspected GMemory routines. Recorder/log bodies and dataset contents not fully audited; no authenticated GMemory run or benefit claimed. Existing local file authorship/approval is unknown. |
| Opaque model/embedding state | Supplied [RT-CMP-gpt-chat](runtime.md#rt-cmp-gpt-chat), [RT-CMP-embedding-func](runtime.md#rt-cmp-embedding-func); direct embedding wrapper | Mutable name-based model resolution and no local training path as supplied. Provider learning, weights and hidden retention remain uninspected. |

The direct CLI/module reads and GMemory method inventory expose library operations beyond the primary retrieval route: `add_memory`, `project_insights`, `backward`, `clear_insights`, clustering and rule merging. The base `update_memory` is a no-op, not an additional working update mechanism. Shipped schedules call retrieval/save directly; there is no provider-native tool route in the supplied runtime account. This is a source-bounded inventory, not an audit of every imported dependency (SRC-1, `mas/memory/mas_memory/memory_base.py`, `mas/module_map.py`; [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

## Core ideas

1. **The main retained unit is a task document, not merely a graph.** Its task name is embedded/searchable page content; descriptions, trajectories, labels and serialized extras/state graphs are metadata. Solvers receive readable description/key-step/trajectory text, not the whole serialized agent-message graph. Maintenance has different readers of the same records ([MEM-OBJ-mas-message](#mem-obj-mas-message), [MEM-OBJ-state-chain](#mem-obj-state-chain)).
2. **Rule text and rule access metadata have different authority.** Models interpret the rule strings. Code uses positive task associations to select rules and scores to keep or discard them. Negative associations are retained but not subtracted by the inspected insight selector. The scalar score is not its retrieval relevance score ([MEM-OBJ-insights-rule](#mem-obj-insights-rule), [MEM-OBJ-insights-metadata](#mem-obj-insights-metadata)).
3. **Feedback produces several derived forms, not one faithful compressed memory.** Save-time extraction keeps model key steps and failure diagnoses. Success-rule synthesis consumes key steps; comparison consumes detailed trajectories and failure explanations. The negative-step deletion attempt does not mutate the backing chain. Serialized chain reconstruction additionally loses visibility of its last completed state through the chain view ([MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip), annotation on [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)).
4. **Selection has count budgets, not a demonstrated token budget.** Retained examples and rules are selected at task start and reused at later action steps. `summarize` concatenates current text; it does not compact it. Role projection is another model transformation and can produce an empty list. Guidance is advisory user-message content, not an enforced action policy ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance)).
5. **Automatic revision has more than one admission mechanism.** Operation parsing/index checks govern ADD/EDIT/REMOVE/AGREE. Merge instead clears and reconstructs the rule collection from numbered output. Neither source path establishes semantic correctness, improved future capacity or observed activation ([RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [MEM-RTE-cluster-merge](#mem-rte-cluster-merge)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-mas-message
Label: MASMessage task text and derived extras

Source-native identity: `MASMessage.task_main`, `task_description`, `task_trajectory`, and `extra_fields` entries `clean_traj`, `key_steps`, `fail_reason`. Representational form: natural-language content, with JSON serialization of extras; `label` is a separate symbolic outcome selector. Storage substrate: mutable current-task Python object and copied Chroma document metadata, with `task_main` as page content. Lineage: task/environment descriptions, model actions, observations and appended final environment feedback; then reconstructed trajectory, digit-stripped cleaned text, model key steps and optional model diagnosis. The readable examples omit `clean_traj`, `fail_reason` and serialized agent messages; maintenance reads the latter two derived text fields through separate builders. Authority: examples guide later solver proposals, key steps guide successful-rule synthesis, and failure reasons guide comparative synthesis. These are interpretations of experience, not environment-certified explanations. Initial Chroma contents and any external edits are uninspected; normal in-process additions are software admitted, not human-approved per record.

This object is a retained payload produced by [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) and consumed by [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) and [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), not a duplicate route. SRC-1, `mas/memory/common.py`, `mas/memory/mas_memory/GMemory.py`, `tasks/mas_workflow/format.py`.

> "task_trajectory": mas_message.task_trajectory,
> "label": mas_message.label,
> "extra_fields": json.dumps(mas_message.extra_fields),
> "state_chain": StateChain.to_str(mas_message.chain_of_states)
> --- `mas/memory/common.py`

> history: list[str] = [f'task{i}:\n' + task.task_description + task.get_extra_field('key_steps') for i, task in enumerate(success_trajectories)]
> --- `mas/memory/mas_memory/GMemory.py`

#### MEM-OBJ-state-chain
Label: StateChain interaction graph payload

Source-native identity: `StateChain._chain_of_states`, containing NetworkX directed graphs. Representational form: symbolic node/edge/action/reward structure with natural-language `AgentMessage` payloads (agent/system/user instruction and response), not a dense learned graph. Storage substrate: Python graphs serialized as node-link JSON inside Chroma metadata. Lineage: scheduler-created agent nodes and upstream edges, environment action/observation/reward per completed state; a trailing open graph is excluded by the public view. The serialized form is inspectable JSON, not an opaque model state. The later formatter displays trajectory/key steps rather than full graph messages. Loaded graph reconstruction exists, but ordinary solving does not establish replay of every stored prompt/reasoning node. Its raw graph contents are not effectively pruned by the attempted extraction deletion; see [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip).

This is a different operative part of the retained document from [MEM-OBJ-mas-message](#mem-obj-mas-message); no supplied object counterpart exists. Related route: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention). SRC-1, `mas/memory/common.py`, `mas/memory/mas_memory/GMemory.py`.

> agent_message_dict: dict = asdict(agent_message)
> node_id = self._generate_node_id(agent_message.agent_name)
> current_state.add_node(node_id, **agent_message_dict)
> --- `mas/memory/common.py`

#### MEM-OBJ-task-layer
Label: TaskLayer query graph

Source-native identity: `TaskLayer.graph`. Representational form: symbolic task-name nodes, similarity-weighted edges and numerical cluster IDs, not natural-language insight arguments or trained weights. Storage substrate: NetworkX graph and `task_layer_graph.pkl`, loaded at construction. New task names obtain up to ten Chroma neighbors; code calls `1 - distance` similarity and adds edges at 0.7. Actual metric calibration depends on Chroma. Query expansion uses nearest task names and hop-limited graph traversal; merge uses clusters computed from task-name embeddings. This access structure differs from the interaction graphs and rule text. No explicit persisted insight-edge graph is instantiated by the inspected `InsightsManager`; its relationships are dictionary lists. The “three-tier graph” description should not make these encodings interchangeable.

The graph is a selector within [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) and [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), not their duplicate. Normal additions and clustering are software admissions; existing pickle authorship is unknown and trusted local loading is required. Graph write precedes task-document write, so a failed add can leave a node without its corresponding new record. SRC-1, `mas/memory/mas_memory/GMemory.py`.

> self.graph.add_edge(task_main, neighbor, weight=similarity)
> --- `mas/memory/mas_memory/GMemory.py`

> neighbours = nx.single_source_shortest_path_length(self.graph, node, cutoff=hop).keys()
> related_nodes.update(neighbours)
> --- `mas/memory/mas_memory/GMemory.py`

#### MEM-OBJ-insights-rule
Label: InsightsManager rule text

Source-native identity: each `insights_memory` dictionary's `rule` string. Representational form: localized natural-language advice, possibly causal explanations as requested by shipped prompts. Storage substrate: list of dictionaries in process and `insights.json`. Lineage: empty list if no loaded JSON; otherwise unknown preexisting file origin; subsequent rules derive from sampled success key steps or success/failure trajectory comparisons, accepted operations, and cluster merges. Models author changes; software admits them through different paths. Human launch/configuration is not per-rule approval. Rule text is editable/replacable at list positions; assumptions and scope inside a string lack separately enforced structure.

Consumers: later rule-maintenance model calls, retrieval-return/optional role-projection, and solver user prompts. Maintenance can change future rule content; solving receives advice, not code or a hard constraint. Rule persistence carries across tasks/restarts, but actual influence and benefit remain uninspected. Causal wording may persist inside a rule; separate operation reasons and criticism arguments are not fields of the retained rule. Maintenance prompt/response logs retain more text but are not replayed by the inspected selector.

This is the content object transformed by [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), not a second declaration of that route. Source: SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`; downstream force is supplied by [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance).

> self.persist_file: str = os.path.join(self.working_dir,f'{self.namespace}.json')
> self.insights_memory: list[dict] = load_json(self.persist_file) or []
> --- `mas/memory/mas_memory/GMemory.py`

#### MEM-OBJ-insights-metadata
Label: Insight scores and task associations

Source-native identity: `score`, `positive_correlation_tasks`, `negative_correlation_tasks` alongside rule text. Representational form: symbolic/numerical access and survival metadata. Storage substrate: the same Python dictionaries and `insights.json`, distinct from their natural-language payload. Lineage: ADD initializes score 2 and associates all relative tasks positively, including a failed task in comparison; EDIT and AGREE increase score and positive associations; REMOVE lowers score and appends negative associations. Backward adds +1 or -2 to substring-matched retrieved raw rules. Merge resets metadata rather than preserving this history.

Actual consumer: `_find_related_insights` counts positive-name membership; `query_insights_with_score` counts matching rules across four nearby successes, two failures and the current query. It does not rank by the stored scalar score or subtract negative associations. `clear_insights` uses score > 0 for survival. Thus positive association means linkage under this update algorithm, not independently validated positive causal contribution. No human approval is wired for subsequent metadata changes. Related but not duplicate of [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance); no supplied object counterpart. SRC-1, `mas/memory/mas_memory/GMemory.py`.

> score: int = sum(task in rule.get('positive_correlation_tasks', []) for task in task_mains)
> if score >= threshold:
>     rule_set.append((rule, score, idx))
> --- `mas/memory/mas_memory/GMemory.py`

> self.insights_memory = [self.insights_memory[i] for i in range(len(self.insights_memory))
>                         if self.insights_memory[i]['score'] > 0]
> --- `mas/memory/mas_memory/GMemory.py`

#### MEM-OBJ-node-memory
Label: MacNet Node temporal history

Part of: [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions)

The object is the retained in-process state of that route, not the whole route. Source-native identity: `Node._memory['inputs']` and `['outputs']`. Representational form: natural-language input/output strings in ordered symbolic lists. Storage substrate: reused workflow's Python objects, not Chroma or a restart checkpoint. Lineage: each `_update_memory` appends first current input/output from solving nodes; automatic admission is an append without semantic approval. Only the latest predecessor output crosses a temporal edge; archived inputs are not selected by that getter. History can cross tasks because schedule reset does not call `clear_state`, as established in the supplied record. A process restart loses this history; no reload route is established. Guidance reaches later node proposals, not a hard action filter. Actual edge realization and behavioral activation remain uninspected. SRC-1, `tasks/mas_workflow/macnet/node.py`, `tasks/mas_workflow/macnet/graph_mas.py`.

> self._memory['inputs'].append(self._input[0])
> self._memory['outputs'].append(self._output[0])
> --- `tasks/mas_workflow/macnet/node.py`

### Routes

#### MEM-RTE-state-roundtrip
Label: StateChain serialization roundtrip

Part of: [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

This is the task-retention route's graph serialization/reconstruction part, not the full admission route. Endpoints/progression: completed-state view → JSON graph list in task metadata → `from_str` replacement of backing list → completed-state view of reconstructed chain. Owner: `StateChain` serializers and `MASMessage` adapters. Relevant content is [MEM-OBJ-state-chain](#mem-obj-state-chain), separate from the display trajectory.

- Immediate return: JSON string on write; reconstructed `StateChain` on read.
- Later read-back: task retrieval and maintenance deserialize metadata into `MASMessage`; subsequent chain iteration uses the reconstructed view. The normal solver formatter instead consumes separately retained trajectory/key-step text.
- Delegated visibility: serialized graph can contain recorded prompts and actions, but ordinary solver replay does not deliver the full graph; no additional deployed graph consumer is established.
- Selection predicate: `chain_of_states` excludes the final backing-list element on every access, assuming an open state; `to_str` iterates that view, while `from_str` installs only serialized completed states without adding a new open state.
- Invalidation or expiry: loaded iteration consequently hides the last serialized completed state; repeated serialization of a loaded chain can lose another visible state. Separately, `pop_state` pops a sliced list, leaving backing state unchanged.
- Activation or effect: structural reconstruction differs from the recorded chain; this does not prove loss of the last displayed action because `task_trajectory` is separately stored.
- Evidence limits: static Python list/property reasoning, not a reproduced roundtrip or observed downstream error; no source repair is made.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and oracle: code serializes/deserializes automatically under task save/retrieval, without human selection or model proposal; this is a representation conversion, not a content-quality evaluation. Recovery: no restorative roundtrip check appears in these functions. SRC-1, `mas/memory/common.py`.

> def pop_state(self, idx: int) -> nx.Graph:
>     if idx >= len(self.chain_of_states) or idx < -len(self.chain_of_states):
>         raise ValueError('Index out of range.')
>     return self.chain_of_states.pop(idx)
> --- `mas/memory/common.py`

> @property
> def chain_of_states(self) -> list[nx.Graph]:
>     return self._chain_of_states[:-1]
> --- `mas/memory/common.py`

> def from_str(state_chain_str: str) -> "StateChain":
>     state_chain = StateChain()
>     state_chain._chain_of_states = [json_graph.node_link_graph(state_data) for state_data in json.loads(state_chain_str)]
>     return state_chain
> --- `mas/memory/common.py`

#### MEM-RTE-cluster-merge
Label: Cluster-based insight merge

Part of: [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)

This part has a different admission check and metadata reset from ordinary rule operations. Endpoints/progression: every twentieth saved task → task-name embeddings and FINCH cluster IDs → positively associated rules per cluster → model numbered-list synthesis → clear/rebuild insight list → JSON → later rule retrieval and revision. Owner: `InsightsManager.merge_insights` and `TaskLayer.cluster_tasks`. SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`.

- Immediate return: merged rule list internally; persisted replacement of insight dictionaries on completion.
- Later read-back: ordinary insight selection, projection, solving and subsequent maintenance consume replacement strings/associations after this write, including reload from JSON.
- Delegated visibility: merger sees batches of rule strings, not raw trajectories or historical criticism logs. Solvers later see selected/projected merged strings without source-to-output rationale.
- Selection predicate: rules positively associated with tasks in a computed cluster; batches of ten. Code computes `actual_num = len(batch) // 3`, then requests `actual_num//3` outputs, effectively a floor by nine and zero for batches smaller than nine. This is a requested count, not an enforced output cap.
- Invalidation or expiry: clears old in-memory rules and rebuilds score 2, positive associations to every task in that cluster and empty negative associations. Rules without selected associations do not survive by a separate carry-forward path here.
- Activation or effect: replaces future eligible guidance and its access metadata; numbered-list output, including an empty parsed list, is accepted without the operation-parser checks.
- Evidence limits: clustering dependency semantics/model compliance are uninspected; no claim that merging preserves meaning, improves guidance or was exercised. Empty embeddings can fail before the clustering try block.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposer/decider/veto: task count invokes code; model proposes consolidated advice; numbered-list parser and rebuild code admit it, with no human veto or semantic oracle. The prompts require strict dependence on inputs and no invented information, but no validator checks that contract. This path bypasses `_parse_rules` punctuation/banned-word checks and `_update_rules` duplicate/index checks. Rollback/recovery: old list is cleared and JSON overwritten without a versioned restore mechanism in these routines. It retains replacement text/metadata and merge logs, not per-output justifications. Guidance content, persistence and interpretation are supplied by [MEM-OBJ-insights-rule](#mem-obj-insights-rule); this part does not independently establish any theory-builder condition beyond the supplied assessment on its parent route.

> actual_num: int = len(batch) // 3
>
> user_prompt = GMemoryPrompts.merge_rules_user_prompt.format(
>     current_rules='\n'.join(batch),
>     limited_number=actual_num//3
> )
> --- `mas/memory/mas_memory/GMemory.py`

> self.insights_memory.clear()
> --- `mas/memory/mas_memory/GMemory.py`

> 'rule': rule,
> 'score': 2,
> 'positive_correlation_tasks': list(related_task_mains),
> 'negative_correlation_tasks': list()
> --- `mas/memory/mas_memory/GMemory.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)

Memory curation correction: `_extract_mas_message` attempts to remove negative-reward states from a deep copy, but `StateChain.pop_state` mutates a property-produced slice. The backing states remain. Therefore the supplied record's statement that negative states are removed is unsupported by the called implementation. A successful `task_trajectory` is reconstructed from all completed states, including those the attempted deletion leaves behind; failure preserves the original trajectory. The `clean_traj` field then removes all digits, potentially conflating object identifiers and numeric observations, not just simplifying a display. Model key-step generation receives this cleaned reconstruction; failure diagnosis receives it too. No content-quality gate checks their output. Trace origin combines dataset/environment descriptions, observations/rewards, model actions, and recorded prompts; later extras are model-authored interpretations (SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/common.py`; [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip)).

> trajectory = re.sub(r'\d+', '', trajectory)
> mas_message_copy.add_extra_field('clean_traj', trajectory)
> --- `mas/memory/mas_memory/GMemory.py`

Final feedback is appended to task description before copying, so later examples and synthesis can include the past task's outcome feedback. The method returns the current original context, not the transformed stored copy. Graph insertion occurs before checking label validity or writing the Chroma task document; the label predicate is boolean-equivalence, not strict type checking. These facts limit claims of coherent rejection and faithful retained views. Normal content admission is software-triggered and model-assisted; external initialization of existing stores remains unknown rather than being assumed human-controlled (SRC-1, `mas/memory/mas_memory/memory_base.py`, `mas/memory/mas_memory/GMemory.py`).

#### On [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)

Selection refinement: the retrieval API doubles requested success/failure/insight counts for candidate gathering, then cosine-filters and model-reranks successful task candidates. If graph expansion yields fewer than a requested category count, its list is assigned the label-filtered similarity search result rather than augmented. The subsequent `if doc not in true_tasks_doc` loop tests membership in that very list and adds nothing; the same pattern exists for failed tasks. Thus graph expansion is not guaranteed to contribute final candidates in every retrieval. Insight selection independently uses four successful and two failed neighbors plus the query; it counts positive task-name associations rather than rule scalar scores. Threshold for task cosine similarity does not become an insight truth threshold (SRC-1, `mas/memory/mas_memory/GMemory.py`).

> true_tasks_doc = self.main_memory.similarity_search(
>     query=query_task, k=successful_topk, filter={'label': True}
> )
> for doc in true_tasks_doc:
>     if doc not in true_tasks_doc:
>         true_tasks_doc.append(doc)
> --- `mas/memory/mas_memory/GMemory.py`

Budget and delivery: CLI defaults are one successful example, zero failed examples, three insights, threshold 0 and hop 1, not the API defaults. All three schedules discard failed-task returns. Count slicing limits example/rule numbers, not text length or total tokens. Key steps accompany detailed trajectories rather than replacing them. Retrieval happens at task start; that selected material is reused while `summarize` adds the entire current trajectory. Optional role projection creates transient numbered-list text with no persistence write in that method. Its parser can return [] without throwing, defeating the exception fallback; role dictionaries with an empty value deliver no rules rather than falling back to raw strings. The optional trajectory-conditioned API branch is afforded but not called by inspected schedules (SRC-1, `tasks/run.py`, all three schedule paths listed in coverage, `mas/memory/mas_memory/GMemory.py`, `tasks/mas_workflow/format.py`).

#### On [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)

Storage and lineage: sampled stored records can reach multiple update consumers. Success-only synthesis reads task descriptions plus `key_steps`; comparison reads detailed success/failure trajectories plus model `fail_reason`. Existing rules are supplied as numbered text. `finetune_insights` is text/data revision, not model-weight training. Ordinary operations and score-based pruning affect [MEM-OBJ-insights-rule](#mem-obj-insights-rule) and [MEM-OBJ-insights-metadata](#mem-obj-insights-metadata); [MEM-RTE-cluster-merge](#mem-rte-cluster-merge) separately resets them. Human launch and prompt authorship do not approve each generated update (SRC-1, `mas/memory/mas_memory/GMemory.py`).

Index qualification: operation mapping first validates numbered positions, but AGREE subsequently resolves the rule by substring text rather than using its validated number. `_retrieve_rule_index` returns -1 on a miss; Python indexing can then credit the last rule, not the numbered one. This is a counterexample to reading the parser/index checks as guaranteeing intended target admission. REMOVE only lowers score and records negative links; surviving positive links can continue selecting that rule. EDIT changes text in place and retains old associations. After task save/maintenance, AutoGen/MacNet backward uses previously cached raw rule strings and substring matching: a changed or merged rule can fail to match, or more than one rule can match. Outcome credit does not demonstrate that an agent followed the credited rule (SRC-1, `mas/memory/mas_memory/GMemory.py`).

> elif operation_type == 'AGREE':
>     rule_index: int = self._retrieve_rule_index(operation_rule_text)
>     rule_data: dict = self.insights_memory[rule_index]
>     rule_data['score'] += 1
> --- `mas/memory/mas_memory/GMemory.py`

> def _retrieve_rule_index(self, operation_rule_text: str) -> int:
>
>     for idx, insight in enumerate(self.insights_memory):
>         if insight['rule'] in operation_rule_text:
>             return idx
>     return -1
> --- `mas/memory/mas_memory/GMemory.py`

Reasons can survive in causal rule wording, `fail_reason`, and maintenance logs, but ordinary solving reads selected rule strings and examples, not the maintenance argument log. The supplied theory-builder/learning assessments remain limited independently: software revision and subsequent delivery do not establish content-directed criticism, actual dependence or improved capacity. Household/object-state assumptions in the diagnosis and success prompts also apply when the same memory implementation is selected for other benchmarks; source inspection does not validate that generalization (SRC-1, `mas/memory/mas_memory/prompt.py`; supplied theory assessment on this record).

#### On [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions)

Memory-specific substrate and lineage are separated in [MEM-OBJ-node-memory](#mem-obj-node-memory). Append history is independent of persisted GMemory and its task reset. Latest-output temporal selection has a one-output-per-predecessor budget, while storage lists can grow. Delivery is natural-language upstream context, not an editable persisted strategy rule. No admission based on task correctness governs those appends (SRC-1, `tasks/mas_workflow/macnet/node.py`, `tasks/mas_workflow/macnet/graph_mas.py`).

## Write side

**Acquisition and admission.** Each shipped schedule records proposed actions/agent messages and environment outcomes, then saves either success or failure. Environment labels decide outcome classification; models author key steps and failure explanations. No human supplies or approves each derived item. Existing file initialization is a separate unknown: loading JSON/pickle or Chroma does not identify its author or approval process. Current-task initialization remains known even when persistent-store provenance is unknown ([MEM-OBJ-mas-message](#mem-obj-mas-message), [MEM-OBJ-task-layer](#mem-obj-task-layer), annotation on [RT-RTE-task-retention](runtime.md#rt-rte-task-retention)).

**Raw-to-derived-to-consumer.** Raw task text, agent messages and environment traces enter the copied task document. Attempted state deletion leaves the chain unchanged; cleaned trajectory removes digits. The model emits key steps and, for failures, a diagnosis. Later solving receives description, key steps and detailed successful trajectory. Successful-rule synthesis consumes key steps, while comparison consumes detailed trajectories and failure reasons. Their admitted rule strings then reach maintenance, role projection and solver prompts. This is a concrete trace-fed behavior-shaping pathway, not proof of better future behavior. Raw message graphs and cleaned text remain separately retained; storing them does not make them all visible in later solver prompts ([MEM-OBJ-state-chain](#mem-obj-state-chain), [MEM-OBJ-mas-message](#mem-obj-mas-message), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)).

**Maintenance, rejection and withdrawal.** Normal operation output is rejected for unrecognized shape, missing final period, selected banned words, duplicate substring or invalid position, subject to the AGREE caveat above. These checks do not evaluate correctness. Scores determine physical rule pruning; REMOVE can leave a live rule. Merge bypasses those operation checks, clears old rules and resets metadata. Outcome backward can prune rules after task save, except DyLAN omits backward. There is no task-document expiry or coordinated task/graph withdrawal in the inspected GMemory routines; this does not imply the underlying database lacks deletion APIs. File writers overwrite rather than retain versions. Cross-store writes are not transactional, and external restoration is uninspected ([RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [MEM-RTE-cluster-merge](#mem-rte-cluster-merge), [MEM-OBJ-task-layer](#mem-obj-task-layer); SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/utils.py`).

**Checkpoint forms.** The persisted task graph is a pickle checkpoint of an access graph; Chroma metadata holds task/interaction records; JSON holds current rules and associations. They are not interchangeable checkpoints of a full workflow. The serialization route's missing-open-state issue affects loaded graph views, not separately retained display text. MacNet temporal lists have no inspected restart checkpoint ([MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip), [MEM-OBJ-node-memory](#mem-obj-node-memory)).

## Read-back

The ordinary pull chain is schedule-start task query → code/model selectors → successful task displays and raw rules → optional role projection → user-message formatter → later agent invocation. No independent unsolicited selector pushes guidance while an agent is idle. Code automatically performs retrieval after a task begins; this does not turn query-conditioned selection into an autonomous push service. Task identifiers and association lists are actual selector inputs, not merely filenames. Dense embeddings support retrieval but do not supply a separate textual rationale. Rule scores govern survival; positive associations govern relevance. The inspected consumers are concrete shipped schedules, not hypothetical API callers ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [MEM-OBJ-insights-metadata](#mem-obj-insights-metadata)).

Maintenance has its own read-back: count thresholds sample stored tasks, choose related rules and feed synthesis/comparison models. Merge reads selected rule text and changes what later task retrieval can deliver. Persisted causal clauses may accompany advice, but no inspected selector reconstructs a rule from its historical criticism log. Failure traces are ignored by solver schedule retrieval yet consumed by comparison; failure is not globally excluded from learning inputs ([RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [MEM-RTE-cluster-merge](#mem-rte-cluster-merge)).

Working-context control is distinct from durable memory. `Agent.response` creates fresh system/user message pairs; the full current task text is supplied by value, without hidden per-agent chat accumulation. Solving/helper frames forward selected answer/critic strings rather than an entire private call history. DyLAN clears local caches per environment step per the supplied runtime account. MacNet separately forwards latest predecessor outputs, potentially across tasks. Static examples and role/dataset instructions are shipped context, not read-back learned through use. The stack-frame analogy fits fresh calls with selected inputs and returned text, but there is no model-window pointer into an external graph: only text delivered into that call can be interpreted, and later store access must be performed by the Python selectors. Contexts are not sandboxed processes, and there is no demonstrated token-aware trim/compaction mechanism in these inspected routes (SRC-1, `mas/agents/base.py`, `mas/memory/mas_memory/memory_base.py`, `tasks/mas_workflow/format.py`; [RT-RTE-dylan-actions](runtime.md#rt-rte-dylan-actions), [RT-RTE-macnet-actions](runtime.md#rt-rte-macnet-actions)).

## Integration issues

1. **Correction to negative-step removal.** [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) says negative-reward states are removed. The `StateChain` property/pop implementation leaves backing states intact. [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip) provides the counterexample. Reconciliation must not characterize the persisted task as reward-pruned, although model-requested key-step filtering remains a distinct afforded transformation.
2. **Loaded graph view differs from saved graph.** [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip) documents last-state invisibility after `from_str`. It limits full interaction-graph fidelity, not replay of the separately stored trajectory. The magnitude of practical downstream impact remains unknown without a concrete consumer/run.
3. **Target-check qualification.** [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance) establishes index checks but should not imply safe intended targeting: AGREE can resolve -1 by text and update the last rule. The annotation retains the source witness and consequence. No observed erroneous rule update is claimed.
4. **Selection qualifications.** [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) is broadly supported, with fallback replacing graph candidate lists, CLI/API defaults differing, and rule selection independent of scalar survival scores. [MEM-OBJ-insights-metadata](#mem-obj-insights-metadata) separates the last distinction. No graph contribution in every invocation or rule-truth filter should be inferred.
5. **Parts, not duplicate declarations.** [MEM-RTE-cluster-merge](#mem-rte-cluster-merge) is a separately checked part of the supplied maintenance route. [MEM-RTE-state-roundtrip](#mem-rte-state-roundtrip) is a serialization part of the supplied retention route. [MEM-OBJ-node-memory](#mem-obj-node-memory) is state within the supplied MacNet route. Other new records are payload/access objects used across routes, not replacements for those routes. No possible same-referent duplicate remains after this comparison.
6. **Initialization, dependency and run unknowns.** Prior Chroma/JSON/pickle contents, actual selected guidance, model/embedding versions, graph realization, dependency metrics and authenticated operation are uninspected. The trajectory-conditioned projector is an API branch without an inspected shipped caller. These prevent conclusions about actual use, fidelity, causality or benefit, not the known subsequent transformations. Scope and evidence remain those of SRC-1.

## Limitations and checks

The checkout HEAD was rechecked as `7b581c51d993bd600df14691d101d7e601040cc6`; source `git status --short` was empty. Source identity remains the supplied canonical repository. This job used the supplied member/worker/record contracts and the prepared command path; it did not amend method files, run the target or install dependencies. Findings are implementation/design findings. No claimed observed activation, semantic preservation, improved capacity or causal benefit follows from parsing, persistence and delivery alone. Available but uninspected log/data/helper details and external dependencies remain bounded in the coverage table rather than being called absent.

Validation: the prescribed `commonplace-run validate-output` invocation passed its member content check. It reported that invocation residue was not checked; this is not job acceptance or claim support.
