---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "GMemory runtime: shipped benchmark invocations, multi-agent action paths, retained-context delivery and automatic admission at the frozen revision."
run-id: AAS-2026-10-15-gmemory-a2192cc823f7-01
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
---

# GMemory runtime report

## Runtime account

### Work, entry and evidence

GMemory supplies remembered task examples and distilled rules to three shipped multi-agent benchmark workflows. The workflows choose textual environment actions, collect feedback, save task experience and, conditionally, revise reusable rules. The claimed improvement through experience is a design claim, not a result established here ([RT-CLM-evolving-memory](#rt-clm-evolving-memory)). The boundary is the whole shipped loop defined in [boundary](boundary.md), not just a retrieval library.

SRC-1 supplies implementation and doctrine/design evidence. All source paths below refer to its frozen commit. This pass additionally inspected the agent/reasoning adapters, workflow node/neuron helpers, task prompt formatter, dispatch, environment feedback adapters and memory maintenance code named in the records. No target code, examples, tests or provider calls were executed. Selected log headers in `logs/alfworld/autogen/qwen2.5-14b-instruct/total_task.log`, `logs/fever/autogen/qwen2.5-7b-instruct/total_task.log` and `logs/pddl/autogen/qwen2.5-7b-instruct/total_task.log` show retrieval settings and task starts, but those headers do not identify the memory implementation or authenticate the generating code/configuration. They are not used to establish exercised GMemory operation. Operation, activation and benefit remain uninspected in the conclusions below; this is not evidence that the implemented paths never operate.

The two shipped entry paths converge on `tasks/run.py`: `run_mas.sh` loads `.env` and selects ALFWorld, MacNet, `g-memory`, IO reasoning, 30 steps and a Qwen model string; the README also supplies direct Python examples. The CLI chooses benchmark, workflow, reasoning, memory, model, retrieval counts, threshold, hop radius and optional role projector. Module selection is a fixed Python map, not model-generated code. `--mas_memory` defaults to `none`, which is not a registered map key; a bare default invocation is therefore not the documented GMemory path. The README FEVER example uses `--mas_trials`, whereas the parser accepts `--max_trials`. These are source-visible entry limitations, not reproduced failures (SRC-1, `run_mas.sh`, `tasks/run.py`, `mas/module_map.py`, `README.md`).

One memory object and shared chat callable are built before dataset iteration. Storage is rooted at `./.db/<model-family>/<task>/<workflow>/<memory>` and reused if present. Each task loads the environment and few-shots, installs dataset instructions on hired agents, and calls the selected schedule. Results go to the recorder, with token counts and a price estimate after the dataset. Importing environment dispatch eagerly reads all four dataset inputs; selecting one benchmark does not isolate startup dependencies to that dataset (SRC-1, `tasks/run.py`, `tasks/envs/__init__.py`).

> build_mas(task_configs, reasoning_type, mas_memory_type, model_type)
> run_task(task_configs)
> --- `tasks/run.py`

### Ordinary invocation: AutoGen with GMemory

The ordinary trace is the documented ALFWorld/AutoGen command with an explicitly selected model and `g-memory`. Its principal is the operator starting a fixed benchmark run; within it the Python scheduler owns next steps. It is a bounded benchmark curriculum, not an open-ended assistant session. Agent names are scheduler identities (`solver`, `ground_truth`), not separate OS or provider-security principals. Each agent call supplies a system message plus a newly constructed user message to the same `ReasoningIO`/`GPTChat` stack ([RT-CMP-gpt-chat](#rt-cmp-gpt-chat), SRC-1, `tasks/run.py`, `mas/agents/base.py`, `mas/reasoning/reasoning_modules.py`).

1. The environment and task context reset. Retrieval selects successful tasks and insights; the returned failed-task list is discarded by all three schedules. Successful records become description, key steps and detailed trajectory. Insights may be projected to roles and are sliced to the configured count. This is selection and prompt construction, not guaranteed semantic obedience ([RT-RTE-memory-delivery](#rt-rte-memory-delivery)).
2. Each step rebuilds the user prompt from static examples, selected retained examples/rules, and current task description plus accumulated action/observation trajectory. `MASMemoryBase.summarize` concatenates text; it does not summarize or trim the history. Fresh agent calls have no hidden Agent conversation history in the inspected implementation. The full trajectory is copied into each new prompt; separate calls provide context frames, not process isolation (SRC-1, `mas/agents/base.py`, `mas/memory/mas_memory/memory_base.py`, `tasks/mas_workflow/format.py`).
3. The solver proposes an action. If it matches each of the preceding two actions, a second model persona is asked for an alternative. The final selected action is recorded as an agent node, normalized, executed by `env.step`, and added with observation/reward to the current task. The next step is code-selected, not a tool call chosen through provider-native function dispatch ([RT-RTE-autogen-actions](#rt-rte-autogen-actions)).
4. The outer loop ends on environment `done` or step exhaustion, provided inner generation returns. Final `feedback()` supplies the reward and success label, then the workflow saves the context and calls `backward(final_done)`. The schedule returns `(final_reward, final_done)`; the recorder logs results. Save and maintenance are synchronous before return, so their failure can prevent reporting a completed environment task ([RT-RTE-task-retention](#rt-rte-task-retention), [RT-RTE-insight-maintenance](#rt-rte-insight-maintenance)).

The purported `ground_truth` agent is not an answer oracle: it is another persona over the same reasoning callable. Actual task outcome evidence comes from environment adapters. ALFWorld returns its `done` flag as success; FEVER compares the proposed Finish label to the dataset answer after normalization; PDDL returns wrapper reward/done; ScienceWorld tracks configured subgoal regular-expression matches in observations. These are different operational success criteria, not interchangeable independent proofs of task correctness (SRC-1, `tasks/mas_workflow/autogen/autogen_prompt.py`, `tasks/envs/alfworld_env.py`, `tasks/envs/fever_env.py`, `tasks/envs/utils.py`, `tasks/envs/pddl_env/pddl_env.py`, `tasks/envs/sciworld_env.py`).

### Material alternates and forcing cases

Four forcing cases bound the baseline rather than presuming all consumers and retries equivalent.

| Case | Source-supported counterexample and consequence |
|---|---|
| Repeated action | AutoGen switches personas on textual repetition, not on a correctness test. A repeatedly valid action can trigger the switch, and a wrong but varying action need not. The helper prompt's characterization of the prior action as definitely wrong exceeds the code predicate. See [RT-RTE-autogen-actions](#rt-rte-autogen-actions). |
| Empty provider output | `GPTChat` can return an empty string after its retry loop. Each workflow's inner action loop executes `continue` for an empty answer before incrementing its retry counter. Thus finite provider attempts per call and a finite environment-step limit do not imply a finite task duration. Exceptions can exhaust action retries without a valid replacement action; code does not enforce a clean failed-action result. See [RT-CLM-bounded-recovery](#rt-clm-bounded-recovery). |
| DyLAN consumer | A layered neuron grid produces candidates, optionally critiques predecessors, may deactivate a model-ranked loser, and returns either a consensus answer or a decision-neuron answer. It saves completed tasks but does not call the post-task `backward`; shared save-time maintenance still applies. See [RT-RTE-dylan-actions](#rt-rte-dylan-actions). |
| MacNet later task | Node temporal outputs survive in the reused workflow object. The schedule resets environment and `MASMessage`, but does not call `Node.clear_state`; the next task can receive the preceding task's last temporal outputs when temporal edges exist. Per-task context reset is therefore not a whole-workflow isolation guarantee. See [RT-RTE-macnet-actions](#rt-rte-macnet-actions). |

DyLAN and MacNet are local sequential orchestration, not remote delegated workers in the inspected paths. Their helpers add selected upstream outputs and optional critic responses to fresh prompts. DyLAN resets neuron caches/edge weights each environment step and computes similarity-derived edge weights from embeddings. Its configured `learning_rate` does not by itself establish neural-weight training. MacNet traverses a spatial DAG, stores node input/output history and forwards only the latest temporal predecessor output. The final decision consumes graph outputs and the last constructed user message. Decision/ranking agents are not hired into the main teams and therefore do not receive the runner's per-task instruction installation through that team loop; their own prompts and supplied upstream material determine their context (SRC-1, `tasks/mas_workflow/dylan/dylan.py`, `tasks/mas_workflow/dylan/neuron.py`, `tasks/mas_workflow/macnet/graph_mas.py`, `tasks/mas_workflow/macnet/node.py`, `tasks/run.py`).

### Capability, grants and guarantees

The inspected action capability is text sent to a selected benchmark wrapper: simulated actions for ALFWorld/PDDL/ScienceWorld, and Search/Lookup/Finish for FEVER. FEVER Search can fetch Wikipedia over the network. The current grant set is the operator-selected environment plus model endpoint and local storage directories. Python imports, configuration reads, persistence and model calls execute under the launching process's ambient authority. Nothing in these inspected paths establishes a deployed container, OS sandbox or provider isolation envelope; third-party simulator internals and endpoint internals remain outside the account (SRC-1, `tasks/envs/__init__.py`, `tasks/envs/fever_env.py`, `tasks/envs/utils.py`, `mas/llm.py`, `mas/memory/mas_memory/GMemory.py`).

Material alternate model paths were inspected rather than assuming an Agent-only control point: solver and decision calls use `Agent.response`; critics call `Agent.reasoning` directly; memory ranking, extraction, projection and rule maintenance invoke the shared callable directly. `GPTChat` sends only messages and generation settings in its inspected request, with no provider-native tools field. Consequently, Agent system instructions and solver retry logic do not govern every model call. The shell launcher is an operator entry, not a model shell tool. Static module maps select installed Python classes; model-produced rule operations mutate data rather than installing executable extensions. This is a bounded account of inspected paths, not an exhaustive dependency security audit (SRC-1, `mas/agents/base.py`, `mas/llm.py`, `mas/module_map.py`, `tasks/mas_workflow/macnet/node.py`, `tasks/mas_workflow/dylan/neuron.py`, `mas/memory/mas_memory/GMemory.py`).

| Load-bearing expectation | Owner/enforcement, strength and coverage | Limit and conclusion status |
|---|---|---|
| Bounded environment action count | Workflow owns `range(env.max_trials)` and stops on `done`; symbolic policy, conditional on an iteration completing. Covers all three schedules' outer loops. | Inner retries and remote calls have separate contracts; there is no end-to-end deadline in the inspected wrapper. implementation conclusion status: wired. operation conclusion status: uninspected. |
| Bounded recovery | `GPTChat` caps its own attempt loop at five; workflow exception retries have separate counters. Best effort, not a task termination invariant. | Empty-output forcing case breaks the apparent workflow retry bound. Provider timeouts/behavior are external. See [RT-CLM-bounded-recovery](#rt-clm-bounded-recovery). |
| Role guidance follows retrieved memory | Formatter and optional projector deliver natural-language material; model owns interpretation. Policy/request, not invariant. | Projector can return a non-numbered answer parsed as an empty list without raising, so exception fallback does not ensure retained guidance survives. Alternate critic/decision contexts differ. implementation conclusion status: wired. operation conclusion status: uninspected. |
| Retained state survives restart coherently | Chroma plus explicit graph pickle and insight JSON writers/readers implement persistence. Protocol, not an atomic deployment guarantee. | Task graph is written before the Chroma task document, then rules may be changed; no cross-store transaction/rollback is provided in those routines. Pickle reload requires trusted local files. implementation conclusion status: wired. operation conclusion status: uninspected. |

The first two rows are grounded in SRC-1, `mas/llm.py` and all three schedule files; the guidance row in `tasks/mas_workflow/format.py` and `mas/memory/mas_memory/GMemory.py`; the persistence row in `mas/memory/mas_memory/GMemory.py`, `mas/memory/common.py` and `mas/utils.py`. Required external contracts are working model responses and usage metadata, compatible Chroma/NetworkX/SentenceTransformer behavior, writable trusted local storage and benchmark resources. No performance or reliability measurement is inferred. Token/price logging is observability, not admission control; the runner's final price arithmetic differs from `get_price`'s arithmetic and neither proves actual billing (SRC-1, `tasks/run.py`, `mas/llm.py`).

## Shared records

### Components

#### RT-CMP-gpt-chat
Label: GPTChat shared generation backend

Source-native identity: `GPTChat`, instantiated once by `build_mas` and shared with IO reasoning and GMemory. Representational form: distributed-parametric model behind a symbolic chat API, consuming natural-language messages. Storage substrate: remote OpenAI-compatible endpoint; provider weights/state are opaque, while the client stores a model-name string and API client locally. Parameters changing during operation: no local parameter-update path is present in these adapters; provider-side changes are uninspected. Exact version pinned: no, the CLI supplies a model name, not weight bytes or an immutable provider revision. Mutable endpoint can resolve to another model: yes, the base URL comes from the environment and the server's resolution of the string is outside source control. SRC-1, `mas/llm.py`, `tasks/run.py`, `mas/reasoning/reasoning_modules.py`.

> self.client = OpenAI(
>     base_url=URL,
>     api_key=KEY
> )
> --- `mas/llm.py`

#### RT-CMP-embedding-func
Label: EmbeddingFunc encoder

Source-native identity: `EmbeddingFunc`, used by retrieval and separately instantiated by DyLAN neurons. Representational form: distributed-parametric SentenceTransformer encoder; its outputs are dense numerical vectors consumed by similarity algorithms. Storage substrate: externally loaded model cached in the process by model-name key; vectors also support the Chroma store. Parameters changing during operation: inspected wrapper calls `encode`, not training or parameter mutation. Exact version pinned: no, `SentenceTransformer(self.model_type)` receives a model name without a revision argument. Mutable endpoint can resolve to another model: model acquisition/version resolution is delegated to the dependency/model source; no immutable revision enforcement is present in this wrapper, and actual cache contents are uninspected. This does not imply that every existing local cached model changes between invocations. SRC-1, `mas/utils.py`, `tasks/configs.yaml`, `tasks/mas_workflow/dylan/neuron.py`.

> if self.model_type not in _EMBEDDING_MODEL_CACHE:
>     _EMBEDDING_MODEL_CACHE[self.model_type] = SentenceTransformer(self.model_type)
> --- `mas/utils.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-memory-delivery
Label: Task memory to agent context

Endpoints/progression: task-main query → graph-expanded and similarity-filtered task candidates → model relevance ranking for successful tasks → formatted examples and selected insight strings → optionally role-projected strings → agent user prompt. Owner: GMemory performs selection; workflow owns projection choice, slicing and prompt delivery. Text examples/rules are natural-language content; graph links, labels, counts and numerical similarities supply symbolic/numerical selection. Current-run trajectory remains in the prompt independently of retained retrieval. SRC-1, `mas/memory/mas_memory/GMemory.py`, `tasks/mas_workflow/format.py`, all three schedule files.

- Immediate return: successful/failed MASMessage lists and insight strings; schedules ignore the failed list and construct example/rule text for agents.
- Later read-back: previously saved task experience and insights reach subsequent task schedules, including a process restart when stores reload; current-run trajectory concatenation is separate.
- Delegated visibility: hired solving agents receive selected examples/rules; critics receive supplied task/answer material; decision agents receive their helper's selected outputs and prompts, not necessarily the same full context.
- Selection predicate: label-filtered similarity and task-graph neighborhood expansion, threshold and top-k, then model ranking of successful trajectories; insights are ranked by positive task-association counts. Projected role lists are truncated.
- Invalidation or expiry: no read-time TTL in these routines; changing retrieval counts/threshold/role projection changes delivery, while rule pruning/merging can remove future candidates.
- Activation or effect: wires selected text into user messages; influence on model choices is unobserved.
- Evidence limits: dependency ranking semantics, actual retrieved contents and model compliance are not reproduced. Model relevance judgments are not answer oracles.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code filters and slices; the model proposes relevance scores and role paraphrases; no per-item human selector/veto is wired. Operating mode: benchmark-task retrieval at schedule start, not unsolicited delivery independent of a task query. Answer oracle: inapplicable — relevance ranking has no supplied expected correct ranking.

> top_k_insights = insights[:insight_topk]
> self.insights_cache = top_k_insights
>
> return top_success_task_trajectories, top_fail_task_trajectories, top_k_insights
> --- `mas/memory/mas_memory/GMemory.py`

> roles_rules[role] = self.meta_memory.project_insights(insights, role)
> --- `tasks/mas_workflow/autogen/autogen.py`

#### RT-RTE-autogen-actions
Label: AutoGen action selection and environment return

Endpoints/progression: operator task → solver response → optional repetition-triggered helper response → normalized environment action → observation/reward → next prompt or final feedback. Owner: AutoGen scheduler; model proposes text, code chooses helper escalation and executes the selected text in the configured environment. Symbolic scheduling controls natural-language proposals and context. State comprises local action history and current MASMessage. SRC-1, `tasks/mas_workflow/autogen/autogen.py`, `mas/agents/base.py`, `mas/memory/mas_memory/memory_base.py`.

- Immediate return: schedule returns final reward and success after saving and backward; each environment step returns observation/reward/done to the scheduler.
- Later read-back: completed context enters [RT-RTE-task-retention](#rt-rte-task-retention); within-task trajectory is rebuilt into later model invocations.
- Delegated visibility: helper sees the same selected task examples/rules and accumulated trajectory in its role-specific prompt, not private solver reasoning.
- Selection predicate: helper called when current action equals the previous two actions; otherwise solver action proceeds. Done or outer step exhaustion ends environment interaction.
- Invalidation or expiry: action history and task context are recreated per schedule; model call frames do not retain an Agent chat history.
- Activation or effect: selected text reaches `env.step`; source wiring does not show a successful action or memory-caused behavioral change.
- Evidence limits: the helper's name does not establish ground truth; finite retries do not guarantee termination on empty output, and environment/provider behavior remains external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: solver/helper model. Decider: code repetition predicate and environment adapter; no interactive human approval. Answer oracle: ALFWorld `done`, FEVER dataset answer, PDDL wrapper outcome or ScienceWorld subgoal feedback according to selected mode, not the helper. Operating mode: fixed dataset tasks with bounded outer environment steps; task failure triggers retention and potential memory maintenance rather than an automatic task restart.

> return len(action_history) >= 2 and current_action == action_history[-1] and current_action == action_history[-2]
> --- `tasks/mas_workflow/autogen/autogen.py`

> observation, reward, done = env.step(action)
> action_history.append(action)
> --- `tasks/mas_workflow/autogen/autogen.py`

#### RT-RTE-dylan-actions
Label: DyLAN layered candidate selection

Endpoints/progression: selected task context → layered neuron responses with predecessor outputs/optional critics → consensus test or final decision neuron → environment → feedback/save. Owner: DyLAN scheduler; neuron/critic/ranker/decision model calls propose text, code controls traversal and selection. Symbolic graph/cache state and embedding-derived edge weights are local process state, not neural parameter training. SRC-1, `tasks/mas_workflow/dylan/dylan.py`, `tasks/mas_workflow/dylan/neuron.py`.

- Immediate return: selected final action reaches environment, followed by final reward/done after save.
- Later read-back: save feeds shared task retention; predecessor output is forwarded within the layered invocation; saved examples may reach later tasks. No DyLAN post-save backward call is wired in this schedule.
- Delegated visibility: neurons get task prompt plus active upstream outputs and optional critic text; ranker/decision receive formatted candidate responses.
- Selection predicate: equality for two answers, otherwise count threshold based on layer size; model ranking can deactivate a loser when height exceeds two; lack of consensus invokes the decision neuron.
- Invalidation or expiry: each environment step reactivates neurons, clears cached answers and zeros edge weights; task context resets per schedule. Inactive outputs are omitted by the helper.
- Activation or effect: code passes the selected answer to environment action processing; whether consensus is correct or critiques help is unobserved.
- Evidence limits: rank-output length is checked but that does not validate every index; empty/inactive responses and retries can fail to progress. Actual layer execution and quality are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposers: neuron, critic and decision models. Deciders: scheduler consensus code, model rank order for elimination, decision model for non-consensus action. Human contribution: initial task/configuration, not candidate approval. Answer oracle: environment feedback only; consensus/ranking has no expected-answer oracle. Operating mode: fixed benchmark tasks and configured layer sizes, not a controlled experiment comparing graph interventions.

> if self._reach_consensus(col=col):
>     counter = Counter(answers)
>     most_common_answer, count = counter.most_common(1)[0]
>     return most_common_answer
> --- `tasks/mas_workflow/dylan/dylan.py`

> self.meta_memory.save_task_context(label=final_done, feedback=final_feedback)
>
> return final_reward, final_done
> --- `tasks/mas_workflow/dylan/dylan.py`

#### RT-RTE-macnet-actions
Label: MacNet spatial and temporal coordination

Endpoints/progression: task context plus spatial/current and temporal/prior node outputs → topologically ordered node calls → all-node decision call → environment → feedback/save/backward. Owner: MacNet scheduler. Spatial cycle checking and graph masks constrain code scheduling; critics and final action selection remain model-mediated. Node histories live in process memory and are separate from GMemory's persisted task stores. SRC-1, `tasks/mas_workflow/macnet/graph_mas.py`, `tasks/mas_workflow/macnet/node.py`.

- Immediate return: selected final action to environment and final reward/done after save/backward.
- Later read-back: latest temporal predecessor outputs reach later node invocations, including across tasks in the reused object when edges exist; persistent GMemory read-back follows the shared delivery route.
- Delegated visibility: spatial predecessors expose first current output; temporal predecessors expose latest recorded output; optional critic text is added to the next node prompt. Decision node receives solving-node outputs.
- Selection predicate: static/generated graph masks determine predecessor sets; zero-in-degree traversal determines order; decision model synthesizes action without an independent correctness gate.
- Invalidation or expiry: execute replaces current input/output; update_memory appends history. `clear_state` exists but is not called in inspected schedule/build/runner paths, so task-context initialization does not clear node histories.
- Activation or effect: final text is normalized and executed by environment; cross-task temporal delivery is architecturally reachable, not observed contamination or benefit.
- Evidence limits: actual graph realization and temporal-edge presence are not supplied. Graph cycle prevention does not establish action correctness or model isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposers: solver and critic models; final decision model proposes action. Decider: graph code schedules, final model chooses action, environment supplies outcome. No per-action human veto is wired. Answer oracle: selected benchmark feedback, not critic agreement. Operating mode: repeated benchmark tasks on one reused graph. Recovery inherits empty-response and exception limitations described above.

> history_outputs = predecessor._memory['outputs']
>
> if len(history_outputs) == 0:
>     continue
>
> predecessor_output = history_outputs[-1]
> --- `tasks/mas_workflow/macnet/node.py`

> self._update_memory()
> self._connect_decision_node()
> action = self._decision_node.execute(user_message, use_critic=False)
> self._disconnect_dicision_node()
> --- `tasks/mas_workflow/macnet/graph_mas.py`

#### RT-RTE-task-retention
Label: Completed task admission

Endpoints/progression: environment final feedback/label → current MASMessage → copied trajectory extraction, key-step generation and failure diagnosis when failed → task graph and Chroma document. Owner: workflow initiates save; GMemory performs model transformations and local writes. Natural-language trajectory/diagnosis and symbolic labels/serialized graph metadata have different downstream consumers; detailed memory-object revision findings are left to the memory analyst. SRC-1, `mas/memory/mas_memory/memory_base.py`, `mas/memory/mas_memory/GMemory.py`, `mas/memory/common.py`.

- Immediate return: saved task context to caller, then schedule reward/done if maintenance completes.
- Later read-back: Chroma task documents and task-layer graph support later task retrieval and maintenance sampling; extracted key steps enter formatted examples.
- Delegated visibility: extraction/diagnosis model sees task and the reconstructed trajectory after digit erasure, not a reward-pruned trajectory; later agents receive selected formatted task content, not necessarily all original agent-message graph fields.
- Selection predicate: every normal completed schedule saves, including failure; label must compare equal to True or False. The extraction loop attempts to remove negative-reward states, but `pop_state` pops a fresh slice rather than the backing list, so those states remain in the copied chain and reconstructed trajectory. Successful task trajectory is replaced by that reconstructed trajectory before digit erasure; `clean_traj` supplies the digit-erased version to key-step extraction and failure diagnosis.
- Invalidation or expiry: no explicit task expiry here; transformations affect the saved copy, and rule changes have separate admission. Save-time exceptions can leave partially updated stores.
- Activation or effect: writes retained data and makes it eligible for retrieval; successful future use is unobserved.
- Evidence limits: persistence calls are inspected, not executed; no cross-store consistency or reconstruction-quality guarantee follows from source alone.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: code initiates on final feedback; model supplies key steps and failure explanation; label is supplied by environment, not model. Code rejects non-boolean-equivalent labels but no per-content human approval or semantic quality gate is wired. Operating mode: trace-fed benchmark retention. Answer oracle: the environment's task outcome, not an expected correct condensation. Proposed change: new task document and graph participation. Guidance: extraction/diagnosis prompts. Rollback/recovery: these routines do not snapshot and transactionally restore graph plus Chroma plus insights; trusted files/dependencies must remain coherent. No executable product/capability update is performed by this route.

> self.current_task_context.label = label
> if feedback is not None:
>     self.current_task_context.task_description += f'\n- Environment feedback\n{feedback}\n'
> self.add_memory(self.current_task_context)
> --- `mas/memory/mas_memory/memory_base.py`

> if state_chain.get_state(state_id).graph.get('reward', 0) < 0:
>     state_chain.pop_state(state_id)
> --- `mas/memory/mas_memory/GMemory.py`

> return self.chain_of_states.pop(idx)
> --- `mas/memory/common.py`

> @property
> def chain_of_states(self) -> list[nx.Graph]:
>     return self._chain_of_states[:-1]
> --- `mas/memory/common.py`

> trajectory = re.sub(r'\d+', '', trajectory)
> mas_message_copy.add_extra_field('clean_traj', trajectory)
> --- `mas/memory/mas_memory/GMemory.py`

This correction follows the slice behavior also established in [MEM-RTE-state-roundtrip](memory.md#mem-rte-state-roundtrip). SRC-1, `mas/memory/common.py` and `mas/memory/mas_memory/GMemory.py`, support failed reward pruning independently of the model extraction, digit erasure, persistence and later-delivery mechanisms. This is static implementation reasoning, not a reproduced filtering failure.

#### RT-RTE-insight-maintenance
Label: Automatic rule admission and feedback

Endpoints/progression: newly saved task count → sampled successful/failed tasks and existing rules → model-proposed rule operations → parser/index/deduplication checks → score/text/association changes and pruning → insight JSON → later retrieval. Every twentieth saved record also triggers clustered rule merging. AutoGen/MacNet additionally adjust cached retrieved rule scores after save; DyLAN does not. Owner: GMemory/InsightsManager code; no separate human admission step. This record establishes the runtime mechanism, not a complete memory revision or epistemic assessment. SRC-1, `mas/memory/mas_memory/GMemory.py`, `mas/memory/mas_memory/prompt.py`, all three schedules.

- Immediate return: maintenance writes updated insight JSON synchronously; workflow then returns its environment result.
- Later read-back: later retrieval and maintenance read the changed rule text/associations; startup loads insight JSON and graph pickle.
- Delegated visibility: proposer sees selected task records, existing rules and, in comparative mode, model-generated failure reason; solver sees only later selected/projected rule strings.
- Selection predicate: default maintenance starts at five saved tasks and every fifth task, sampling five points with nearby successes/failures; model operations are parsed and filtered, indices mapped to global rule positions, scores pruned at nonpositive values. Merge uses task clusters. Backward matches cached insight text by substring.
- Invalidation or expiry: removal decreases score rather than immediately deleting; pruning keeps positive scores. Merge clears the old in-memory list and rebuilds rules with fresh scores/associations; no versioned rollback is wired here.
- Activation or effect: modifies retained guidance eligible for later prompts, not model parameters; causal change in later decisions remains unobserved.
- Evidence limits: parser acceptance is not truth validation; role projection can change content and backward credits cached raw rules rather than verified compliance. Requested generalized criticism and observed criticism are distinct.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: code count thresholds initiate software sampling; model proposes ADD/EDIT/REMOVE/AGREE; parser checks recognized operation shape, nonempty text ending in a period and banned words; update code rejects some duplicates/invalid indices. Human contribution is initial launch/configuration and editable shipped prompts, not per-rule approval. The nominal ten-rule threshold changes prompt suffix and removal strength; it is not a hard cap on ADD. Merging is a separate numbered-list generation path, not covered by operation-parser checks. External dependency: model output and storage availability. Recovery: no semantic veto, staged validation against future task performance, or automatic restoration of previous rule versions in these inspected routines. Answer oracle: no reference correct rule set; task outcome labels feed selection, while model-generated failure reasons are interpretations. Operating modes: success-only distillation, success/failure comparison, merge and task-outcome credit adjustment.

Guidance/theory account: shipped prompts request general principles with causal wording and criticism of failed trials. Existing rules are supplied for agreement, removal, editing or addition. What persists is rule text, score and positive/negative task associations; prompts/responses are also logged, but retrieval uses rule strings rather than replaying a retained criticism argument. This gives localized revisable guidance, not proof that its explanations are true or its revisions content-directed criticism of a formulated theory.

- theory-builder conditions 1–4: assessed independently below, within inspected rule maintenance and later solving, not provider internals.
- condition 1 conclusion status: afforded
  Individual natural-language rule strings can state whole generalized principles and can be replaced individually; actual retained theory contents were not supplied as authenticated runtime evidence.
- condition 2 conclusion status: afforded
  Proposer and solver are supplied rule content for interpretation, enabling content-dependent decisions; delivery alone does not show actual dependence.
- condition 3 conclusion status: claimed
  Prompts request critiques and operations against existing rules, but implementation does not require a stated challenged claim, result, blame placement and revision rationale. Model processing is opaque, not evidence of absent criticism.
- condition 4 conclusion status: afforded
  Revised rules are persisted and supplied to later rounds; whether a retained result of qualifying criticism shapes the next round is unobserved.
- Addressability: individual numbered rules and text replacements are exposed; assumptions and scope conditions within a rule have no separate enforced structure.
- Persistence: implementation reaches across tasks and process reload through JSON; achieved runtime horizon is unobserved.
- learning: later-action guidance capacity is wired, but improved capacity and attribution to this mechanism are not established by source inspection.
- Reflection: representations of task performance and strategies feed rule updates and can return to solver prompts; actual two-direction behavioral dependence remains unobserved.
- Reflective theory builder: not established; method-prompt texts are static here, while generated strategy rules need the independently unresolved criticism conditions above.
- Autonomous theory builder: software performs sampling, proposal calls, parsing and writes without internal human approval; that automation does not establish all theory-builder conditions or reliability.

> if self.memory_size >= self._start_insights_threshold and self.memory_size % self._rounds_per_insights == 0:
>     self.insights_layer.finetune_insights(self._insights_point_num)
> if self.memory_size % 20 == 0:
>     self.insights_layer.merge_insights()
> --- `mas/memory/mas_memory/GMemory.py`

> The insights you summarize must follow the "XXX, because XXX" format.
> --- `mas/memory/mas_memory/prompt.py:321-321`

> if text != '' and not any([w in text for w in banned_words]) and text.endswith('.'):
> --- `mas/memory/mas_memory/GMemory.py`

### Claims

#### RT-CLM-evolving-memory
Label: Claimed adaptation through hierarchical memory

Claimed operation: capture cross-task experiences and insights, retrieve them for later agents, then update the hierarchy to enable adaptation/improvement. Source: SRC-1, `README.md`. Implemented retention, retrieval and maintenance support the mechanism's availability, not successful improvement or causal benefit. No self-improvement attribution is made from delivery and persistence alone.

> As agents complete tasks, G-Memory updates its memory hierarchy with new interactions, enabling teams to adapt and improve over time.
> --- `README.md`

#### RT-CLM-bounded-recovery
Label: Apparent retry bound is not a task deadline

Claimed operation under assessment: finite retries and outer step counts could be read as bounded end-to-end work. The inspected code supports only separate attempt/step bounds. Owner: GPTChat and each schedule; guarantee strength: best effort. Covered paths: chat wrapper attempts and workflow exception counts. Alternate paths: empty-answer retries, direct memory calls and critic/decision calls do not share one outer solver counter. Required external contract: calls must return and produce useful answers; no deployed end-to-end deadline is established. SRC-1, `mas/llm.py`, `tasks/mas_workflow/autogen/autogen.py`, `tasks/mas_workflow/dylan/dylan.py`, `tasks/mas_workflow/macnet/graph_mas.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

The wrapper caps attempts at five and returns `""` on exhaustion; workflow empty-answer branches retry before advancing `tries`. These are implementation counterexamples to a global bound, not an observed hang.

> max_retries = 5
> wait_time = 1
> --- `mas/llm.py`

> action: str = solver.response(user_prompt, self.reasoning_config)
> if action == '':
>     continue
> action = env.process_action(action)
> break
> --- `tasks/mas_workflow/autogen/autogen.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-retained-guidance
Label: Retained guidance to solver action

Consumer: solver agents through the prompt formatter and optional role projector. Channel: selected successful task examples and rule strings embedded in user messages, below shipped system/dataset instructions in the chat role structure. Force: advisory natural-language guidance, not an executable policy or enforced action filter; the formatter explicitly invites reference to examples/insights. Horizon: later steps reuse the same selected material; later task schedules reselect from persisted experience and rules, including reload in a new process. Update consumers and downstream solving consumers differ: rule maintenance interprets existing rules to propose edits, whereas solvers interpret the delivered/projected strings to propose environment actions. Actual activation and benefit are unobserved. SRC-1, `tasks/mas_workflow/format.py`, `mas/agents/base.py`, `mas/memory/mas_memory/GMemory.py`.

> The following are insights gathered during the execution of similar tasks. You may refer to them during your task execution to improve problem-solving accuracy.
> --- `tasks/mas_workflow/format.py`

## Annotations

none
