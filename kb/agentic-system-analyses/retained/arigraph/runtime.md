---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AriGraph runtime baseline: shipped game decisions, navigation, QA, alternative memory consumers and their control limits at the frozen commit."
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
---

# AriGraph runtime report

## Runtime account

### Boundary and evidence basis

AriGraph is an external memory mechanism inside shipped game and QA drivers, not the owner of every agent decision. The [boundary](boundary.md#boundary-and-evidence) includes those drivers and their alternative memory baselines. SRC-1 supplies inspected implementation, authored instructions and attributed run artifacts. No target code, provider call or experiment was executed for this report. Implementation wiring does not establish model compliance or benefit. The README's performance claims are retained in [RT-CLM-memory-performance](#rt-clm-memory-performance), not treated as replicated results.

Coverage here includes full reads of the main game, QA, full-history, summary, smart-RAG, human and graph-evaluation drivers; agent and graph sources; both nonempty prompt modules; embedding and graph-search utilities; the TextWorld wrapper; bounded reads of `utils/utils.py` (parsing/logging and observation/episodic ranking), `src/contriever.py` (Contriever forward path), and the first 65/35 lines respectively of the game/QA logs. These are SRC-1 at the frozen revision, not new sources. Other assets, task contents, support training utilities and remaining logs are not reassessed here. Their uninspected contents prevent exhaustive task and aggregate-performance conclusions, not the source-native control trace below.

### Ordinary game invocation

The operator edits module-level parameters and supplies an API key before invoking `pipeline_arigraph.py`. The shipped defaults select `hunt_hard`, one attempt, 150 outer steps, five recent observations/actions, two episodic memories, CPU retrieval and exploration enabled. General extraction/entity/exploration requests use `gpt-4o`; planning and action requests use `gpt-4-0125-preview`. Module initialization creates the environment, logger and separate model wrappers; `run()` owns progression. Those wrappers are synchronous roles, not remote delegated workers with separate coordination protocols (SRC-1, `pipeline_arigraph.py`, `agents/parent_agent.py`). See [RT-RTE-game-cycle](#rt-rte-game-cycle).

Each attempt resets TextWorld, seeds a text plan, clears recent history and location state, and constructs a fresh ContrieverGraph. Each outer step strips observation prefixes, normalizes text, appends the first-step task instructions, obtains inventory and records the current location. A model receives the current observation and previous plan to propose entities and retrieval depths. Graph update extracts facts, requests deletion of outdated facts, adds facts and derived spatial connections, retrieves older facts/episodes and retains the new observation. Inventory is appended to the current observation **after** graph update. Thus the graph admission request is not identical to the later planner input. The graph retains the pre-inventory observation as the episode key, while the driver appends the inventory-augmented string to its recent `observations` list. The post-top-k exact-string filter therefore does not ensure suppression of episodes corresponding to that recent window; selected episodes still reach planner/action context. The memory interface is captured in [RT-RTE-game-memory](#rt-rte-game-memory); detailed memory-object identity and revision assessment are left to the memory analyst (SRC-1, `pipeline_arigraph.py`, `graphs/contriever_graph.py`).

An exploration model interprets the previous plan; the driver treats any response containing `True` as positive. This supplies unexplored-exit text to later planning/action requests. The driver obtains TextWorld admissible actions, conditionally expands cooking actions, and adds synthetic `go to` commands for known locations. The planner gets the goal, five-step history, current observation/inventory, retrieved facts/episodes and previous plan. Its returned text replaces the plan without local semantic validation. The action model receives these materials plus the new plan and action list. The driver parses `action_to_take`, defaults to `look` on parsing/key errors, and transforms cooking actions. It does **not** test membership in the supplied action list (SRC-1, `pipeline_arigraph.py`, `prompts/system_prompts.py`).

Execution is either one `env.step(action)` or a memory-derived sequence of directional steps for `go to`, described in [RT-RTE-graph-navigation](#rt-rte-graph-navigation). TextWorld supplies feedback, score and completion; cleaning substitutes reward calculated from environment-fact differences. The next outer iteration receives the returned observation and retains the previous action. Navigation's intermediate observations are logged but not each admitted through the memory update. Completion is checked at the next outer iteration; otherwise the outer step budget ends the attempt. `run()` has no final answer object or explicit success return: observations, decisions, rewards, estimated costs and timings are logged. Costs use hard-coded token prices, not model-specific billing; wall time and counters provide observability, not performance guarantees (SRC-1, `pipeline_arigraph.py`, `utils/textworld_adapter.py`, `utils/utils.py`).

### Four forcing cases and guarantee limits

1. **A well-formed off-list action.** The instruction says to choose only from possible actions, but the parser accepts any `action_to_take` value. The effect boundary then relies on TextWorld's external command semantics. The guarantee owner is the action prompt/model; enforcement is a natural-language policy, not an application invariant. JSON-object mode is an API request, not a local action-schema or allowlist check. Direct action paths in the alternative drivers and human input likewise reach `env.step` without that check (SRC-1, `pipeline_arigraph.py`, `pipeline_fullhist.py`, `pipeline_summary.py`, `pipeline_smartrag.py`, `interactive_human_games.py`). Implementation conclusion status: wired. Compliance operation conclusion status: uninspected. Required external contract: provider formatting behavior and environment command interpretation.

> You may choose actions only from the list of possible actions. You must choose strictly one action.
> --- `prompts/system_prompts.py`

> action_json = json.loads(action0)
> action = action_json["action_to_take"]
> --- `pipeline_arigraph.py`

2. **A location-to-location deletion proposal.** ContrieverGraph's deletion method skips a triplet whose two endpoints are in the supplied location set. Owner: graph implementation. Enforcement point: `delete_triplets`. Strength: invariant of that method under supplied membership, not a guarantee that all spatial knowledge is true or immutable. QA avoids deletion entirely; Hypergraph deletes theses by name under another method without this location guard. Caller-controlled locations and direct mutable Python state are outside the guard's promise (SRC-1, `graphs/contriever_graph.py`, `graphs/hypergraph.py`). Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: caller's location identities are accurate.

> if triplet[0] in locations and triplet[1] in locations:
>     continue
> --- `graphs/contriever_graph.py`

3. **A synthetic navigation action.** `go to` is handled by substring recognition and graph path computation, not the action-list policy. The driver can issue several environment commands under one outer step, stops on environment completion and reports aggregate reward. `max_steps` is a driver-owned invariant on outer iterations, not a bound of 150 environment actions, tokens, seconds or provider expenditure. Required external contract: graph directions correspond to executable commands; TextWorld returns feedback/completion. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `pipeline_arigraph.py`, `graphs/parent_graph.py`).

> for hidden_step, hidden_action in enumerate(path):
>     observation, reward_, done, info = env.step(hidden_action)
> --- `pipeline_arigraph.py`

4. **QA ingestion instead of game maintenance.** Paragraphs enter through `update_without_retrieve`, whose replacement block is commented out. This challenges a system-wide claim that every admission reconciles stale facts. A task reset prevents intentional cross-task memory carryover; it does not validate paragraph truth or guarantee successful QA. The optional local LLaMA adapter also ignores the `jsn` argument as a formatting control, so OpenAI's JSON-mode request cannot be generalized to all model paths (SRC-1, `musique_test_big.py`, `graphs/contriever_graph.py`, `agents/llama_agent.py`). See [RT-RTE-qa-cycle](#rt-rte-qa-cycle).

The selected forcing cases are source traces, not executed adversarial tests. Provider errors, malformed entity dictionaries, nonstring actions, zero-length navigation paths and dependency compatibility were not experimentally exercised. Action parse fallback and graph path error-to-text handling are narrow recovery mechanisms. The model wrappers have no local retry/approval logic in their inspected `generate` bodies; imported `sleep` is not a retry mechanism. SDK-internal retries remain outside the frozen implementation evidence (SRC-1, `agents/parent_agent.py`, `graphs/parent_graph.py`).

### Alternate consumers, admission and authority

QA clears the graph per question, admits paragraphs, obtains question entities, retrieves facts and texts, generates an answer and computes metrics against dataset answers. A non-dictionary entity result records failure and skips answering, but a literal-parse exception occurs before that type check and is not caught. The HotpotQA loader returns strings whereas `run()` expects paragraph/question/answer mappings; the declared branch is therefore not established as a working equivalent of MuSiQue. For a non-LLaMA QA model, `load_setup` passes `graph_model` to the QA wrapper, not the separately supplied `qa_model`. Mixed-model configuration labels do not establish the actual provider selected (SRC-1, `musique_test_big.py`).

The full-history baseline supplies all previous observations/actions; summary supplies a model-replaced summary plus bounded recent history; smart-RAG selects raw past observations/actions using recency, model-assigned importance and embedding similarity. Each has its own entry script and owns an attempt-local retention loop, not an alternative backend automatically selected by the AriGraph driver. See [RT-RTE-full-history](#rt-rte-full-history), [RT-RTE-summary-cycle](#rt-rte-summary-cycle), and [RT-RTE-smart-rag](#rt-rte-smart-rag). The human driver constructs model/graph helpers but `run()` directly obtains console actions; helper presence does not demonstrate model participation. See [RT-RTE-human-play](#rt-rte-human-play) (SRC-1, the four named driver paths).

Hypergraph implements thesis/entity/event retention and model-directed removal with another retrieval/ranking route, but none of the inspected root callers instantiates it. Its method is an available interface, not an observed deployed alternate; see [RT-RTE-hypergraph-update](#rt-rte-hypergraph-update). The fact-replacement evaluator intends to compare model removals against before/after environment facts, but its local variable initialization, LazyGraph client setup and missing scoring call prevent treating it as operational validation; see [RT-RTE-graph-evaluation](#rt-rte-graph-evaluation) (SRC-1, `graphs/hypergraph.py`, `pipeline_graph_evaluation.py`, `graphs/lazy_graph.py`).

Computational admission of retained facts and summary text is immediate after model/parsing transformations; launching a script is not human approval of each item. Humans choose task/configuration and authored prompts; the human-play route supplies each environment action. No inspected driver admits model-proposed source-code, prompt-template, model-weight or tool-installation changes. The bounded unused-reflexion finding is [RT-ABS-reflex-invocation](#rt-abs-reflex-invocation), not a claim that memory replacement cannot shape future decisions.

The runtime's current grant surface is TextWorld action strings, graph-state mutation, provider requests and local logging performed by Python code. Models return text; inspected adapters do not pass provider-native tools or shell executors. The **process** nevertheless needs filesystem access, network access for providers/model loading and environment dependencies. No deployed sandbox/isolation envelope is supplied; host permissions cannot be inferred from this limited model-facing surface. Dense embedding state and remote/local language models have distinct mutability limits in [RT-CMP-gpt-agent](#rt-cmp-gpt-agent), [RT-CMP-retriever](#rt-cmp-retriever), and [RT-CMP-llama-agent](#rt-cmp-llama-agent) (SRC-1, `agents/parent_agent.py`, `agents/llama_agent.py`, `utils/contriever.py`, `graphs/parent_graph.py`).

Supplied logs show attributed step-one game extraction/plan/action and one QA extraction/retrieval/answer/metric sequence. The QA log explicitly reports a nonexact answer. They support bounded recorded operation, not reproduction at the current driver defaults, successful activation of every retrieved unit, aggregate scores or causal benefit (SRC-1, `logs/hunt_arigraph.txt`, `logs/musique_gpt.txt`).

## Shared records

### Components

#### RT-CMP-gpt-agent
Label: GPTagent and graph chat-completion adapter

Source-native identity: GPTagent and TripletGraph each hold an OpenAI client, model identifier, system prompt and cost counter. Form: the inaccessible model is distributed-parametric; model identifiers and wrapper control are symbolic; prompt strings are natural-language inputs. Substrate: remote provider service plus Python process state. The adapters issue fresh system/user messages rather than retaining a provider conversation ID. Provider-internal storage and parameter updates are uninspected. No local parameter-training operation appears in these request paths. Exact weights are not pinned by source: named provider models, including dated names, are service-resolved identifiers and the external endpoint can change implementation. This component covers entity selection, extraction, replacement, exploration, planning, action, importance and answering in inspected callers (SRC-1, `agents/parent_agent.py`, `graphs/parent_graph.py`, `pipeline_arigraph.py`, `musique_test_big.py`).

> response = chat_completion.choices[0].message.content
> --- `agents/parent_agent.py`

#### RT-CMP-retriever
Label: Retriever and Contriever embedding model

Source-native identity: `Retriever` loads `facebook/mcontriever` and its tokenizer, executes Contriever forward pooling and dot-product searches. Form: distributed-parametric weights and derived dense embeddings, with symbolic threshold/top-k control. Substrate: local PyTorch model/tensors, with some embeddings converted to NumPy in graph caches. Inspected embedding/search paths are inference under `torch.no_grad`; they do not train weights. Embedding cache contents change as text is admitted. The exact weight/tokenizer revision is not pinned; `from_pretrained` can resolve a changed upstream artifact at a later initialization. There is no serving endpoint for embedding calls after loading; upstream download resolution is mutable. External weight provenance and actual deterministic behavior are uninspected (SRC-1, `utils/contriever.py`, `src/contriever.py`, `graphs/contriever_graph.py`).

> embedder = Contriever.from_pretrained("facebook/mcontriever").to(device)
> tokenizer = AutoTokenizer.from_pretrained("facebook/mcontriever")
> --- `utils/contriever.py`

#### RT-CMP-llama-agent
Label: LLaMAagent and LLaMAContrieverGraph local generation

Source-native identity: the QA setup loads a Transformers text-generation pipeline for `Undi95/Meta-Llama-3-70B-Instruct-hf`; LLaMAagent and LLaMAContrieverGraph render chat templates and slice generated text. Form: distributed-parametric local model plus natural-language messages. Substrate: local model/device memory and tokenizer state. No operational weight update appears in these generation bodies. Exact model/tokenizer revision is not pinned; loading by repository name can resolve different artifacts in a later setup, although an already loaded pipeline is not an independently mutable remote serving endpoint. The adapters can accept an externally supplied pipeline; that pipeline's exact identity is then caller-controlled. Provider/checkpoint internals are uninspected. Sampling uses a 2048-new-token ceiling, temperature and top-p; `jsn` is accepted but not used to enforce JSON (SRC-1, `agents/llama_agent.py`, `graphs/contriever_graph.py`, `musique_test_big.py`).

> max_new_tokens=2048,
> eos_token_id=terminators,
> do_sample=True,
> temperature=t,
> top_p=0.9,
> --- `agents/llama_agent.py`

### Operative objects

#### RT-OBJ-plan
Label: plan0 task plan

Source-native identity: `plan0`, initially a driver-authored string and thereafter planner-returned text. Form: natural-language goals/reasons presented inside requested JSON; downstream models interpret its content, rather than a fixed planner executing the JSON fields. Substrate: attempt-local Python string and append-only textual logs. Lineage: initial task goal, then previous plan, selected memory, observations/inventory and recent history. It is fed back to retrieval-entity and exploration requests and the next planner, and to the current action selector. The driver replaces the whole string, without a content gate or persisted restart reload. The prompt instructs retention of unfinished subgoals; that is model policy, not a locally enforced invariant. Task-plan modification is not by itself evidence of formulated explanatory theory criticism (SRC-1, `pipeline_arigraph.py`, `prompts/system_prompts.py`).

> plan0, cost_plan = agent_plan.generate(prompt, jsn=True, t=0.2)
> log("Plan0: " + plan0)
> return plan0
> --- `pipeline_arigraph.py`

#### RT-OBJ-system-prompts
Label: Shipped extraction, maintenance and decision prompts

Source-native identity: prompt constants in `prompts/prompts.py` and `prompts/system_prompts.py`. Form: natural-language instructions, even where they request symbolic output syntax. Substrate: tracked Python source strings, rendered into model requests. These are static shipped guidance, not read-back of experience. Maintainers edit them; inspected drivers do not overwrite them. Their requested behavior includes conservative replacement, hypothesis wording, subgoal preservation, exploration and action-list selection. The unused reflexion constant has a different wiring status from the used maintenance prompts (SRC-1, both prompt paths).

> If you think you haven’t some crucial knowledges about the game, explore new areas and items.
> --- `prompts/system_prompts.py`

### Routes

#### RT-RTE-game-cycle
Label: Ariadne observation to plan and action

Endpoints/progression: operator-started `run()` → environment reset → entity selection → graph update → exploration decision → planner → action selector → parser → environment execution → feedback/next outer step. Owner/next-step principal: synchronous driver; separate GPTagent instances implement model decision roles, not independent coordinating principals. Context/state: goal, previous plan, bounded history, current observation/inventory, selected facts/episodes, known locations and possible actions. Executor/effect boundary: Python dispatcher into TextWorld; no general-purpose model tool executor. SRC-1, `pipeline_arigraph.py`, `agents/parent_agent.py`, `utils/textworld_adapter.py`.

- Immediate return: each model returns text and estimated cost; environment execution returns observation, reward, done and info; `run()` produces logs rather than a returned final answer.
- Later read-back: previous plan, bounded history and graph-derived memory reach subsequent requests in the same attempt; no graph/plan restart reload is wired here.
- Delegated visibility: inapplicable — synchronous model roles receive constructed messages, not delegated worker state.
- Selection predicate: model entity scores guide retrieval depth; substring `True` selects exploration; model proposes a plan/action using supplied context; driver branches on `go to`.
- Invalidation or expiry: history is sliced to five default steps; plan is replaced; fresh attempt resets graph, plan and histories; done or outer-step budget stops progression.
- Activation or effect: wiring delivers retained material to decision models and dispatches selected actions; individual memory-caused behavioral changes are unestablished.
- Evidence limits: provider compliance and live environment success uninspected; the supplied game-log sample shows attributed plan/action output, not current-default reproduction or causal benefit.
- implementation conclusion status: wired
- operation conclusion status: observed

Observed status is scoped to the retained step-one sequence, not the whole contemporary configuration. Proposer/decider: model roles for entities, exploration, plan and action; driver owns parsing and dispatch. Human control: configuration/start, not per-action approval. Veto: parse failure defaults to `look`, but off-list well-formed strings are not vetoed. Answer oracle: no expected plan/action answer is supplied to these models; environment reward and completion are outcome signals, not a reference-answer selector. Operating mode: bounded goal-directed game episode. Plan-change trigger: new observation/memory; admission: whole planner response replaces `plan0`; guidance is the static planner prompt; rollback: no previous-plan restoration logic beyond sending the previous string in the next request.

> history.append(f"Observation: {observation}\nAction taken: {action}")
> history = history[-n_prev:]
> --- `pipeline_arigraph.py`

#### RT-RTE-game-memory
Label: Game observation memory interface

Endpoints/progression: game driver observation/previous plan → extraction → associated-old-fact filtering → replacement proposal/parser → deletion/addition → retrieval and episode retention → planner/action context. Owner: ContrieverGraph under the driver. Computational model proposes facts/removals; code parses/normalizes and applies them. No per-content human decision. Natural-language observations and fact labels coexist with symbolic triplet structure and numerical embeddings, rather than one uniform form. SRC-1, `graphs/contriever_graph.py`, `pipeline_arigraph.py`, `utils/retriever_search_drafts.py`, `utils/utils.py`.

- Immediate return: associated older fact strings and top episodic observation strings.
- Later read-back: new facts and the observation enter attempt-local stores used by later retrieval/model invocations; selection need not deliver every admitted item.
- Delegated visibility: inapplicable — memory returns to the calling driver, with no remote worker visibility protocol.
- Selection predicate: extraction and removal models use rendered prompts; old-fact candidate selection uses endpoint association/filtering; fact retrieval uses entity queries/depths, top six and 0.75 threshold; episodes combine fact overlap and plan embedding ranking, then apply an exact-string membership filter against supplied `observations` after top-k. This removes matching strings without replenishing the selection, not necessarily recent-window episodes: stored pre-inventory keys differ from the driver's inventory-augmented recent strings.
- Invalidation or expiry: parsed deletion proposal removes matching nonprotected facts; both-location facts are skipped; duplicate additions are suppressed; new attempt constructs a new graph.
- Activation or effect: model output mutates memory; selected older content is supplied to later planner/action requests; actual correctness and content-caused action changes remain unestablished.
- Evidence limits: no fact-truth oracle or semantic validator; malformed extraction can drop fragments; replacement parser does not verify the proposed replacement's truth or admission; detailed memory curation remains for the memory member.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission trigger/change: each observation proposes facts/removals and retains an episode. Decider/veto: model proposes removals; code rejects absent triplets and protects both-location endpoints, but does not independently adjudicate semantic contradiction. Guidance: conservative same-aspect replacement instructions, static prompts and previous selected facts as extraction examples. Persists: facts, episode texts and embeddings, not model reasoning. Rejection/rollback: local guard/parse omissions, no transactional rollback; reset discards the attempt. Answer oracle: none in update. Operating mode: within a bounded game, not an independently scored update experiment.

> predicted_outdated = parse_triplets_removing(response)
> self.delete_triplets(predicted_outdated, locations)
> --- `graphs/contriever_graph.py`

The implemented filter and the driver ordering below establish the mismatch, not successful recent-window exclusion (SRC-1). Episode retention uses the same pre-inventory `observation` supplied to `update`, as shown in the retention passage that follows.

> top_episodic = top_k_obs(top_episodic_dict, k=topk_episodic)
>
> top_episodic = [item for item in top_episodic if item not in observations]
> --- `graphs/contriever_graph.py`

> subgraph, top_episodic = graph.update(observation, observations, plan=plan0, prev_subgraph=subgraph, locations=list(locations), curr_location=observation_processing(env.curr_location).lower(), previous_location=previous_location, action=action, log=log, items1 = items, topk_episodic=topk_episodic)
> observation += f"\nInventory: {inventory}"
> --- `pipeline_arigraph.py`

> observations.append(observation)
> observations = observations[-n_prev:]
> --- `pipeline_arigraph.py`

> self.obs_episodic[observation] = obs_value
>
> self.obs_episodic_list.append(deepcopy(self.obs_episodic))
> self.top_episodic_dict_list.append(top_episodic_dict)
> --- `graphs/contriever_graph.py`

#### RT-RTE-graph-navigation
Label: Synthetic go-to graph navigation

Endpoints/progression: action string → `process_action_get_reward` → `find_path`/spatial graph → directional commands → TextWorld feedback. Owner: driver executes; TripletGraph derives the path. State is symbolic locations/edges and a path list, not another language-model decision. SRC-1, `pipeline_arigraph.py`, `graphs/parent_graph.py`.

- Immediate return: aggregate step reward, final hidden-step observation, done and info; path failure returns diagnostic observation text.
- Later read-back: final observation reaches the next graph update and recent history; intermediate hidden observations are logged, not individually sent through graph admission.
- Delegated visibility: inapplicable — navigation is local synchronous execution.
- Selection predicate: substring `go to`; destination parsed after `go to `; breadth-first path over recognized spatial edges among known locations.
- Invalidation or expiry: path list is temporary; next navigation recomputes from current graph/location; graph facts can change through separate update methods.
- Activation or effect: one model action can cause multiple environment steps without another planner request; completion breaks hidden-step execution.
- Evidence limits: path correctness depends on admitted graph relations and external environment semantics; empty-path and malformed navigation strings are not experimentally tested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

No oracle selects the path against a reference route. Unknown/disconnected destinations or caught path exceptions produce explanatory text instead of a general rollback. The parser/dispatcher does not bound hidden-step count by the outer budget.

> if not isinstance(path, list):
>     observation = path
> --- `pipeline_arigraph.py`

#### RT-RTE-qa-cycle
Label: Paragraph memory to QA and metrics

Endpoints/progression: fixed-seed sample of up to 200 tasks → clear graph → admit task paragraphs without replacement → model question entities → retrieval → answer generation → token/EM metrics and logs. Owner: QA driver; graph and agent roles return to it. Natural-language question/text/fact labels reach the answer model; symbolic parsing/scoring and numerical embeddings support selection. SRC-1, `musique_test_big.py`, `graphs/contriever_graph.py`, `agents/llama_agent.py`.

- Immediate return: textual answer from `get_answer`; aggregate running metrics are logged, not returned by `run()`.
- Later read-back: paragraph facts/text are admitted before later retrieval/answer invocations within that task; reset prevents intentional carryover into the next task.
- Delegated visibility: inapplicable — synchronous provider/local generation roles, not delegated workers.
- Selection predicate: model-selected question entities/depths drive semantic retrieval; question embedding and retrieved-fact overlap rank episodic texts; default top-k is two.
- Invalidation or expiry: `graph.clear()` at each task; admission does not run game-style deletion; paragraph entries otherwise survive until reset.
- Activation or effect: retrieved content is delivered to an answer request; sampled log records an answer and metrics, without isolating memory's causal contribution.
- Evidence limits: HotpotQA loader/consumer shapes disagree; non-LLaMA QA branch uses graph_model; true answers score output after generation and do not gate memory admission.
- implementation conclusion status: wired
- operation conclusion status: observed

Observation is bounded to SRC-1's supplied QA sample. Admission: extraction model proposes facts, code accepts parsed/normalized facts and stores paragraph text; no human per-paragraph approval or semantic rejection. Guidance: same extraction template as game, with empty examples. Recovery: non-dict items skip a task, but parse/API errors are not caught locally; reset, not rollback, restores task isolation. Answer oracle: dataset `task["answer"]`, provided by local data, used by post-answer metrics only. Operating mode: bounded fixed-seed evaluation batch, not metric-fed model/memory optimization.

> for task in tasks:
>     graph.clear()
>     for text in task["paragraphs"]:
>         triplets, episodic = graph.update_without_retrieve(text["paragraph_text"], [], log)
> --- `musique_test_big.py`

> Direct answer: Rabbi Dovber Schneuri
> TRUE ANSWER: Dovber Schneuri
> F1: 0.8, RECALL: 1.0, PRECISION: 0.6666666666666666, EXACT MATCH: 0.0
> --- `logs/musique_gpt.txt`

#### RT-RTE-full-history
Label: Full-history game baseline

Endpoints/progression: reset → observation → planner/action using complete previous observations/actions → environment step → append and next round. Owner: `pipeline_fullhist.py`; GPTagent models choose plan/action, code dispatches. Retained observation/action text is natural-language content in a Python list, supplied by string interpolation. SRC-1, `pipeline_fullhist.py`.

- Immediate return: model plan/action and environment feedback; driver writes reward/cost/time logs.
- Later read-back: all appended observations/actions are delivered to subsequent planning/action invocations in the same attempt.
- Delegated visibility: inapplicable — local sequential roles.
- Selection predicate: full accumulated list, no retrieval ranking or history slicing in this route.
- Invalidation or expiry: reset per attempt; plan replaced each round; done or step budget ends processing.
- Activation or effect: prior text is delivered to decision models, with no isolated content-activation evidence.
- Evidence limits: provider context-window behavior and performance unobserved; no graph navigation dispatcher in this driver.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: driver appends observation/action without per-content human approval; model replaces plan under the shared planner instructions. There is no history rejection/rollback gate; restart resets it. Mode: bounded game. Oracle: environment outcomes, not expected decision answers; model proposes and code parses actions with `look` fallback rather than an allowlist veto.

> observations.append(f"\nObservation: {observation}\nAction taken: {action}")
> --- `pipeline_fullhist.py`

#### RT-RTE-summary-cycle
Label: Model-maintained summary game baseline

Endpoints/progression: observation/inventory + bounded history + previous summary → summary model → planner/action → environment → next summary. Owner: summary driver. Summary is natural-language text in an attempt-local Python string and logs. SRC-1, `pipeline_summary.py`, `prompts/system_prompts.py`.

- Immediate return: replacement summary, plan/action and environment feedback; logs are terminal artifacts.
- Later read-back: accepted summary reaches current planner/action and next summary invocation; bounded history separately reaches those roles.
- Delegated visibility: inapplicable — synchronous model roles.
- Selection predicate: model summarizes supplied previous summary, current observation and five-step default history; no independent content selector/gate.
- Invalidation or expiry: summary wholly replaced each step, recent history sliced; attempt reset seeds `Yet nothing`.
- Activation or effect: replacement text is immediately delivered as decision context; fidelity and behavioral activation unobserved.
- Evidence limits: prompt requests accurate useful compression, not a deterministic information-preservation guarantee or demonstrated benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: each observation triggers the model's revised summary, directly assigned by software; no human review or semantic veto. Guidance: static summary system prompt and prior summary. Persists: summary text and recent observation/action history, not a critique record. Recovery: attempt reset; no rollback to a previous summary on semantic error. Mode/oracle: bounded game, no expected summary/reference outcome fed to summary admission. Plan/action roles share the model-policy and parse-fallback limits of the ordinary driver.

> summary = get_summary(hist_obs, observation, summary)
> --- `pipeline_summary.py`

> summary, cost = agent_summary.generate(prompt, t = 0.6)
> log("Summary: " + summary)
> return summary
> --- `pipeline_summary.py`

#### RT-RTE-smart-rag
Label: Recency importance similarity game baseline

Endpoints/progression: current observation/old plan embedding → rank stored observations → planner/action → model importance rating → append observation/step/rating/embedding/action → environment feedback. Owner: smart-RAG driver; model rates importance, code computes rank. Stored text/action is natural-language; metadata/indexes are symbolic; dense embeddings are numerical. Substrate: attempt-local tuples/list and tensors/NumPy arrays. SRC-1, `pipeline_smartrag.py`, `utils/contriever.py`.

- Immediate return: selected previous observation/action strings, plan/action, importance score and environment feedback.
- Later read-back: appended tuple is available to later retrieval, whose selected text/action reaches planner/action; rating itself acts through rank rather than direct prompt delivery.
- Delegated visibility: inapplicable — no worker delegation.
- Selection predicate: top n by summed min-max-normalized recency decay, model importance and cosine similarity; union with separately indexed recent entries and deduplication.
- Invalidation or expiry: observation list grows within attempt and resets next attempt; no deletion or importance revision is wired.
- Activation or effect: ratings/embeddings affect software selection and selected text is delivered to decision models; resulting action improvement unobserved.
- Evidence limits: recent-entry expression uses `observations[-i]` starting at zero, so first appended entry is included rather than a pure last-n slice; model score parsed as first digit sequence without range validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: software appends raw observation/action and a model-proposed importance score; humans only configure/start. Guidance asks integer importance 1–10 relative to the plan; parser enforces neither the range nor the rationale. Rejection/recovery: empty digit output can raise; no rollback/retry. Mode: bounded game; no importance answer oracle or metric-fed update. Plan admission uses unchanged planner guidance and whole-response replacement.

> best_idx = np.argsort(minmax(time_scores) + minmax(importance_scores) + minmax(relative_scores))[-n:]
> --- `pipeline_smartrag.py`

#### RT-RTE-human-play
Label: Console-selected game action

Endpoints/progression: observation/inventory/action list → console input → optional cooking normalization → environment step → log/next observation. Owner/decider: human chooses each action; driver dispatches it. Human-readable text and action strings are interpreted by human/environment respectively. SRC-1, `interactive_human_games.py`.

- Immediate return: environment observation/reward/done/info and textual logs.
- Later read-back: inapplicable — run does not update/retrieve its constructed graph or feed accumulated experience to model requests; prior action is displayed with the next observation.
- Delegated visibility: inapplicable — direct human input, not worker delegation.
- Selection predicate: unrestricted console entry rather than model selection from displayed actions.
- Invalidation or expiry: environment reset per attempt; next input replaces prior action.
- Activation or effect: human string is passed to `env.step` after cooking conversion; helper planner/action functions are not called by this loop.
- Evidence limits: graph/model construction does not establish their operational participation; human policy and action validity unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: bounded interactive game. Human proposes/decides; no separate approval oracle or software allowlist veto. This path is not per-content human approval of AriGraph memory writes, because those writes are not invoked here.

> action = input("Action that you choose: ")
> --- `interactive_human_games.py`

#### RT-RTE-hypergraph-update
Label: Hypergraph thesis event alternate interface

Endpoints/progression: caller observation/history/plan/entities → thesis extraction → associated-thesis replacement proposal → deletion/add → semantic and event retrieval → result. Owner: Hypergraph method; no shipped root driver call found in inspected roots. Natural-language thesis/event names, symbolic hashed link structures and numerical embeddings occupy distinct operative parts in local dictionaries. SRC-1, `graphs/hypergraph.py`, `utils/retriever_search_drafts.py`, `prompts/prompts.py`.

- Immediate return: older retrieved thesis names and selected episodic event texts.
- Later read-back: admitted theses/events are available to subsequent method invocations; no inspected shipped driver establishes their later delivery to planner/action.
- Delegated visibility: inapplicable — local method interface.
- Selection predicate: extraction model, one-step entity BFS for removal candidates; semantic thesis search top five/0.75/depth; event score combines overlap and plan similarity.
- Invalidation or expiry: model-name deletion removes theses and parent/child links; normalization helper called `clear` is not a zero-argument reset equivalent to ContrieverGraph.clear.
- Activation or effect: supplied caller can update/retrieve graph; downstream behavioral use is not established by an entry-point trace.
- Evidence limits: available implementation, not an established deployed alternative; event ranking uses ascending argsort before prefix top-k, so higher-score-first intent must not be assumed. The thesis/event account is not an exhaustive inventory of alternate-API storage: this method also adds reciprocal spatial facts to inherited triplet storage when location changes under a non-`go to` action. The relation of that navigation state to thesis/event state is not assessed here; no shipped navigation/planner use of Hypergraph is established (SRC-1, `graphs/hypergraph.py`).
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission trigger: new observation; model proposes named theses/removals, software applies parsed removals then adds normalized content. No per-item human review or independent semantic oracle. Guidance asks conservative same-property replacement; supplied history excludes already-seen event texts after sorting. Persisted material: theses/entities/events and embeddings, not replacement rationale. Recovery/veto: nonexistent names ignored; no thesis-deletion location protection or transactional rollback. Mode: caller-supplied, uninspected deployment; guidance describes game maintenance. The extraction prompt is concatenated rather than formatted, leaving its literal observation placeholder alongside appended input.

> self.delete_thesises(predicted_outdated)
> self.add(new_thesises_raw, observation)
> --- `graphs/hypergraph.py`

> if "go to" not in action:
>     if curr_location != previous_location:
>         new_triplets_raw = [[curr_location, previous_location, {"label": find_direction(action)}],
>                             [previous_location, curr_location, {"label": find_opposite_direction(action)}]]
>         self.add_triplets(new_triplets_raw)
> --- `graphs/hypergraph.py`

#### RT-RTE-graph-evaluation
Label: Intended fact-replacement evaluator

Endpoints/progression intended: walkthrough action → before/after environment facts → new facts → model removals → compare with actual removed facts. Owner: evaluator script; LazyGraph provides model interface inheritance. Symbolic environment-fact differences serve as the intended reference outcome, distinct from model judgment. SRC-1, `pipeline_graph_evaluation.py`, `graphs/lazy_graph.py`.

- Immediate return: intended removal predictions and recall/precision logs; successful execution not established.
- Later read-back: inapplicable — no evaluated revision is installed into a later game decision route.
- Delegated visibility: inapplicable — local evaluator.
- Selection predicate: fixed environment walkthrough and association to changed-fact endpoints; no successor selection gate.
- Invalidation or expiry: intended graph reconstruction each step from true environment facts; score arrays are module-local.
- Activation or effect: intended diagnostics only, not a production admission path.
- Evidence limits: `run` reads done/info without initialization; local graph assignment does not update the global graph used by get_predict; LazyGraph initializes no client; compute_scores is not called and its counter assignments lack global declarations.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Proposer: model predicts removals. Intended oracle/provider: TextWorld ground-truth fact differences. Human contribution: task/model/walkthrough setup, not per-result judging. Mode: bounded evaluation. No admission, rejection, rollback or improvement feedback to production is wired. Source defects prevent using this script as evidence that the conservative replacement policy was reliably validated, not a conclusion about all evaluation evidence in the repository.

> true_outdated = [clear_triplet(triplet) for triplet in full_graph if triplet not in full_graph_new]
> --- `pipeline_graph_evaluation.py`

### Claims

#### RT-CLM-memory-performance
Label: Claimed memory performance and scalability

Claimed operation: AriGraph improves RAG game performance, surpasses compared baselines and scales to larger environments; README also reports QA comparisons. Source: SRC-1, `README.md`, doctrine/design and reported operation. The tables are attributed aggregate reports. Inspected drivers/log samples do not isolate the causal contribution of individual memory mechanisms or reproduce those scores.

> This agent markedly surpasses all pre-existing baselines in these scenarios and showcases exceptional scalability in more expansive environments.
> --- `README.md`

### Evidenced absences

#### RT-ABS-reflex-invocation
Label: No reflex-prompt invocation in inspected consumers

- implementation conclusion status: absent

Searched boundary: frozen revision e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2; root game/baseline/QA/human/evaluation drivers, `agents/`, `graphs/`, `prompts/`, `utils/` and `src/contriever.py`. Query: `reflex_prompt`, combined with source reads of entry-point progression. Only the definition in `prompts/prompts.py` matches. This supports absence of a wired invocation of that **named prompt** in those paths; it prevents attributing its three-sentence inefficiency analysis to the running game/QA loop. It does not establish absence of opaque model reasoning, other possible reflection mechanisms, or behavior-shaping retained facts/plans. SRC-1, `prompts/prompts.py`, `pipeline_arigraph.py`, `musique_test_big.py`.

> reflex_prompt = '''You are a learner in system of AI agents which play in text games. Your task is to find useful patterns in observations and explain it for future usage. Namely, you should find the unefficiency in previous behaviour and the patterns that can help to avoid this unefficiency.
> --- `prompts/prompts.py`

### Behavioral-authority paths

#### RT-BAP-memory-decisions
Label: Retrieved memory to game and QA decisions

Consumer: game planner/action models and QA answer model. Channel: user-message context containing selected fact strings and episodic text. Force: model-interpreted informational input, not an enforced instruction or verified truth; it can affect decisions but delivery alone does not show actual activation. Horizon: later invocations within an attempt/task; no shipped graph restart reload is established. Associated routes: [RT-RTE-game-memory](#rt-rte-game-memory) and [RT-RTE-qa-cycle](#rt-rte-qa-cycle). SRC-1, `pipeline_arigraph.py`, `musique_test_big.py`.

> Relevant facts from your memory: {subgraph}
>
> Relevant texts from your memory: {episodic}
> --- `musique_test_big.py`

#### RT-BAP-plan-decisions
Label: Plan to retrieval exploration and action

Consumer: entity selector, exploration selector, next planner and action selector. Channel: interpolated `plan0` in model requests and plan embedding in episodic ranking. Force: model-interpreted goal/priority guidance; dense similarity supplies numerical selection influence. Horizon: current and subsequent steps of the same attempt. Whole planner response can alter the priorities later models receive, without proving they obey the priority hierarchy or improve task performance. Source/identity: [RT-OBJ-plan](#rt-obj-plan), SRC-1, `pipeline_arigraph.py`, `graphs/contriever_graph.py`, `agents/parent_agent.py`.

> observed_items, _ = agent.item_processing_scores(observation, plan0)
> --- `pipeline_arigraph.py`

#### RT-BAP-action-dispatch
Label: Selected action text to environment commands

Consumer: driver dispatcher and TextWorld wrapper. Channel: parsed action string or direct console input. Force: software-dispatched environment command; graph navigation expands it into several commands. Horizon: immediate environment step(s), whose feedback can later change retained context. Provider-native tool invocation is not the channel. External environment owns whether a command has a valid task effect; no local action-list invariant is established. SRC-1, `pipeline_arigraph.py`, `utils/textworld_adapter.py`, `interactive_human_games.py`.

> obs, new_score, done, infos = self.env.step(action)
> --- `utils/textworld_adapter.py`

## Annotations

none
