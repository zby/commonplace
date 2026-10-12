---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Agent-R runtime baseline: environment-driven MCTS, revision-data admission and evaluation at the frozen repository revision."
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
reviewed-boundary: "82fcc1ca7873b460949ed49022146dd988c32e31"
---

# Agent-R runtime report

## Runtime account

Agent-R ships an offline data-building plane and an environment-action evaluator, not an implemented closed training service. The declared work is to recover successful trajectories from erroneous ones, construct timely revision examples, and repeat training. The executable paths are `mcts_collection.py`, `path_collection.py`, and `eval.py`. The first writes search trees; the second consumes them and attempts to export conversations; the third loads a configured actor and measures environment reward. Training and checkpoint promotion remain a documented external step. See [RT-CLM-iterative-training](#rt-clm-iterative-training), [RT-RTE-tree-collection](#rt-rte-tree-collection), [RT-RTE-revision-export](#rt-rte-revision-export) and [RT-RTE-agent-evaluation](#rt-rte-agent-evaluation). Evidence is SRC-1 implementation and README design, within [the frozen boundary](boundary.md). No execution trace, generated dataset or experimental comparison was supplied; actual activation and benefit are unobserved.

### Ordinary collection invocation

A caller starts the Python collection driver with `TASK`, `MODEL_DIR`, sampling and tree-budget environment variables, an environment-server URL, an index range and a model-name label. `TASK` selects an imported adapter. `FuncCallOffline` loads vLLM and a tokenizer from `MODEL_DIR`; the CLI model name labels calls and output directories but does not select the local weights. The model proposes text actions; software, rather than the model, owns the next branch, environment reset, execution and persistence. The task server supplies both the initial instruction (`env.conversation_start`) and observations. FastChat constructs user/assistant messages starting with that instruction, `Ok.`, and the initial observation. WebShop/TextCraft indices exclude test tasks and indices outside the clean-training list; SciWorld uses the server's task indices instead. Existing collection output files suppress another collection attempt. These are bounded curricula, not open user requests (SRC-1, `mcts_collection.py`, `mcts_utils/llm_server.py`).

The search root holds a copied conversation, recent-action history and an environment-client reference. For each configured iteration the search expands a node once, generates `N_GEN` responses serially, then follows the shared selector. Terminal children propagate their environment score through ancestors; nonterminal children with zero visits have priority, and ties are randomly selected. Otherwise selection uses average accumulated value plus the exploration term. Terminal nodes are skipped, and a parent becomes terminal when all children are terminal. These fixed symbolic rules select successors; model interpretation proposes actions. See [RT-RTE-tree-collection](#rt-rte-tree-collection).

Each candidate generation first trims a copy of the conversation for the model call. It then restores the full node conversation for the new stored node, resets the shared client to the task index, replays prior actions, parses the model response and performs one new environment action. WebShop/TextCraft accept `Action 1:`, `Action:`, or the response's final line and strip a leading numbered-list prefix. The resulting reward, done flag and state create a child; negative reward becomes zero and marks a disaster/terminal child. Observations have newlines and tabs flattened. Model response, action, observation and cumulative statistics are serialized recursively by mmengine to `mcts_result/{Task}/{model_name}/search_results_{idx}.json` (SRC-1, `mcts_utils/webshop/mcts_ws.py`, `mcts_utils/textcraft/mcts_tc.py`, `mcts_utils/mcts_raw.py`, `mcts_collection.py`). The immediate product is a tree, not a single committed solution or a trained model.

The effect boundary is the external environment's `reset`/`step` interface and the caller's filesystem. Search siblings share one client: reset/replay, not environment snapshots or parallel isolated workers, reconstructs branch state. Equivalent reconstruction therefore requires repeatable reset and transitions and exclusive use of the client; the external server implementation is outside this evidence boundary. The inspected drivers provide no per-action human approval or grant negotiation. This does not imply that environment actions can execute arbitrary host code: their effective capabilities depend on the external server. The Python process can load model artifacts and write files under its host permissions; no deployed isolation envelope was supplied (SRC-1, `mcts_collection.py`, all three adapters).

### Alternate and forcing routes

Four forcing cases bound the account rather than generalizing from WebShop alone:

1. **SciWorld action substitution.** Collection and evaluation call `findValidActionNew` before the new action's `step`. The helper combines environment-valid actions with hard-coded door actions, removes selected focus actions and uses exact matching or token overlap. It is not a guaranteed validity gate: with no positive overlap its fallback retains the proposed action and merely sanitizes it. Replay steps and WebShop/TextCraft bypass this helper. Moreover, histories contain action-observation strings, whereas subtraction operates on whole valid-action strings; this is not reliable last-three-action suppression. See [RT-RTE-sciworld-action](#rt-rte-sciworld-action). Evidence: SRC-1, `mcts_utils/sciworld/mcts_sci.py`, `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/llm_server.py`.
2. **Revision-export threshold failure.** The driver expresses ranking and high/low pair admission, but `ALPHA` and `BETA` are unconverted environment strings compared with floats. Reaching either relevant comparison raises a Python type error; README shell exports cannot turn them into numeric values. Some inputs return earlier, so this is not a claim that every invocation fails. If the code's type defect were corrected, `--revise 0` would bypass model critique and `--data_type good` would bypass paired revision construction. The shipped pair selector also compares all distinct paths, not only adjacent siblings. Thus the README's same-parent account is not an enforced selection condition. See [RT-RTE-revision-export](#rt-rte-revision-export).
3. **Evaluation without search.** `eval.py` calls a sequential rollout directly, not MCTS or the verifier. The test input path is missing in the frozen tree. Its existence check omits the `MODEL_TYPE` suffix used by the writer, so it is not a reliable resume check for the actual result. `perform_test_revise` additionally permits a supplied response prefix to be executed before continuation; its prefix is outside the continuation step counter. See [RT-RTE-agent-evaluation](#rt-rte-agent-evaluation).
4. **Alternative provider call.** `FuncCall` can make Azure/OpenAI chat calls using caller-supplied credentials and deployment name, but the three CLI paths instantiate `FuncCallOffline`. The API wrapper is an injectable alternate call surface, not an automatically selected provider or observed production route. It retries exceptions immediately more than 100,000 times and eventually returns integer `-1`, which is not a valid response string for downstream parsers. See [RT-RTE-provider-alternate](#rt-rte-provider-alternate).

### Guarantees and enforcement scope

**Search-budget controls:** owner is the adapter search/generation code; enforcement points are `range(iterations)` and the child's `depth + 1 > max_depth` terminal predicate. Guarantee strength: invariant for those control-flow predicates under successful execution, not a wall-clock or provider-call guarantee. The strict greater-than check admits an action at depth `max_depth + 1`; the collection CLI's `--max_steps` is parsed but not used. Direct evaluation, supplied-prefix evaluation and arbitrary library calls are not covered by the tree budget. External contracts include terminating model calls and environment steps. Implementation conclusion status: wired. Operation conclusion status: uninspected. Evidence: SRC-1, `mcts_collection.py`, all adapters; the collection record retains the enforcement passage.

**Context-length control:** owner is the caller-side loop before model inference; guarantee strength: best effort. It measures tokenized `str(conv)`, not necessarily the provider's exact message serialization, and deletes fixed message positions. Search then stores the untrimmed node context. With an oversized remaining prompt, deletion can stop making progress; search additionally indexes `conv.messages[4]` after deletion. Thus no unconditional fit or successful termination guarantee follows. Evaluation uses a related deletion loop; revision critique counts whitespace-separated words and removes six characters per iteration instead. See the collection and revision routes. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: tokenizer/provider agreement and a removable history sufficient to fit. Evidence: SRC-1, all adapters, `mcts_utils/llm_server.py`, `path_collection.py`.

**Reward/validity controls:** owner is the external environment for actual transitions and scoring, and Agent-R for score handling and SciWorld substitution. Guarantee strength: best effort for validity, invariant for the inspected negative-score branch. These do not establish a security permission boundary, correctness of environment rewards or reliability of the model verifier. New SciWorld actions are covered by substitution, while replay and the other task adapters are alternate paths. Implementation conclusion status: wired. Operation conclusion status: uninspected. External contract: accurate environment validity/state/reward responses (SRC-1, adapter files and `mcts_utils/sciworld/eval_utils_sw.py`).

**Recovery and admission:** collection skips existing files and saves only after search returns; it supplies no incremental search checkpoint or transactional write. Revision export appends rows and offers no per-row approval or deduplication gate. Evaluation persists only at rollout completion. Exceptions in local inference/environment calls are not recovered by those drivers. The API retry loop is a distinct, narrow recovery mechanism and supplies no environment rollback. Model replacement is caller-controlled through a subsequent `MODEL_DIR` load; the repository supplies no optimizer, checkpoint validation gate or automated promotion loop. See [RT-ABS-training-machinery](#rt-abs-training-machinery). Model mutability is separately stated in the component records.

Inspection repeated the full three drivers, all three MCTS adapters, `mcts_utils/mcts_raw.py`, `mcts_utils/llm_server.py` and README. The bounded SciWorld read covered the entire `findValidActionNew` function within `mcts_utils/sciworld/eval_utils_sw.py` through line 166; later auxiliary functions remain uninspected. No new source or evidence layer is introduced. Available task-JSON contents and method graphics were not used to establish task coverage or performance. External provider internals, server semantics, training ingestion and successful runtime behavior remain unresolved.

## Shared records

### Components

#### RT-CMP-func-call-offline
Label: FuncCallOffline local actor and verifier

Source-native `FuncCallOffline` wraps a vLLM `LLM` and an AutoTokenizer. Representational form: distributed-parametric model weights; storage substrate: caller-selected `MODEL_DIR` artifacts loaded into inference memory. Its tokenizer and sampling configuration are symbolic controls. Parameters are not updated by the inspected inference wrapper. Exact checkpoint version is not pinned by this repository; `MODEL_DIR` can point to a different model between process initializations. No mutable remote endpoint is used on this path, but the directory's provenance/content is caller-controlled. Provider/model internals are uninspected. The same class supplies actor generation and, in a separately started revision process, verifier judgments; matching model weights between stages are not enforced by `model_name`. Evidence: SRC-1, `mcts_utils/llm_server.py`, `mcts_collection.py`, `path_collection.py`, `eval.py`.

> self.llm = LLM(model=os.environ["MODEL_DIR"], dtype="half")
> --- `mcts_utils/llm_server.py`

> self.sampling_params = SamplingParams(temperature=float(os.environ["TEMP"]), max_tokens=500, stop=["<|eot_id|>"])
> --- `mcts_utils/llm_server.py`

#### RT-CMP-func-call
Label: FuncCall API model alternative

Source-native `FuncCall` addresses an externally hosted distributed-parametric model through an Azure/OpenAI deployment name. Storage substrate and exact weights are opaque provider state. No parameter update is requested in this wrapper; server-side changes are uninspected. Exact model version is not pinned, and the caller-selected API base/deployment may resolve to another model. This component is available to injected calling objects rather than selected by the shipped CLIs. Evidence: SRC-1, `mcts_utils/llm_server.py`.

> openai.api_base = os.environ["OPENAI_API_BASE"]
> openai.api_type = "azure"
> openai.api_version = os.environ["OPENAI_API_VERSION"]
> --- `mcts_utils/llm_server.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-tree-collection
Label: Environment-scored tree collection

Endpoints: CLI task selection → local actor → reset/replay/new environment step → tree expansion/selection/backpropagation → JSON tree. Owner: collection driver and task-specific `ExtendedMCTS`; proposer: [RT-CMP-func-call-offline](#rt-cmp-func-call-offline); successor decision: symbolic MCTS selector. Caller chooses task range/model/budgets and can stop the process, but does not approve each child. Bounded curriculum: clean training indices minus test indices for WebShop/TextCraft, server-provided task iterations for SciWorld. Answer oracle: external task environment reward/done, used as scoring and termination signals; reference solutions are not delivered to the actor. Reward correctness is uninspected. Current context is natural-language instruction/history; counters, tree structure, parsing and score propagation are symbolic in process memory.

- Immediate return: Search returns control to the driver, which saves a recursive tree; no selected final action sequence is returned by search.
- Later read-back: `path_collection.py` reloads saved trees for revision-data construction; later agent inference does not directly load them in the inspected evaluator.
- Delegated visibility: Model receives converted conversation messages, not MCTS statistics; external server receives reset/task ID and replay/new action strings.
- Selection predicate: Expand once; deduplicate exact response text after execution; favor unvisited nonterminal children, otherwise value/exploration score with random ties.
- Invalidation or expiry: Existing filename suppresses collection; no freshness/version check or automatic expiry. Caller can remove/replace artifacts outside this route.
- Activation or effect: Generated strings are parsed into environment steps and terminal rewards update ancestors; persistence-to-export wiring is visible, exercised activation is unobserved.
- Evidence limits: External reset determinism and exclusive client use are assumed; no run evidence. Duplicate generations may already have executed before deduplication.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `mcts_collection.py`, `mcts_utils/webshop/mcts_ws.py`, `mcts_utils/textcraft/mcts_tc.py`, `mcts_utils/sciworld/mcts_sci.py`, `mcts_utils/mcts_raw.py`.

> for action in node.recent_actions:
>     action_temp = action[0]
>     _ = self.env.step(action_temp)
> --- `mcts_utils/webshop/mcts_ws.py`

> is_terminal=node.depth + 1 > self.generate_cfg.max_depth or is_terminal
> --- `mcts_utils/webshop/mcts_ws.py`

> if child.visits == 0:
>     score = float('inf')  # Prioritize unvisited nodes
> else:
>     score = child.puct
> --- `mcts_utils/mcts_raw.py`

#### RT-RTE-sciworld-action
Label: SciWorld proposed-action substitution

Endpoints: actor action string → `findValidActionNew` → server `step`; owner: SciWorld adapter/evaluation helper. Model proposes; symbolic exact-match/token-overlap code decides the replacement. Environment supplies validity candidates, inventory and look-around, not an expected task answer. Caller starts the bounded task rollout; no human veto per action. This helper changes actions, not capabilities or model parameters. Its natural-language strings are consumed both by fixed lexical matching and by the external task interpreter.

- Immediate return: One action string to the caller for immediate execution.
- Later read-back: Executed actions/observations enter current history and collection trees; persisted-tree consumption is in [RT-RTE-tree-collection](#rt-rte-tree-collection).
- Delegated visibility: Helper receives proposed action, environment-derived action set/look/inventory and recent history; model is not asked to approve substitutions.
- Selection predicate: Exact valid candidate first; otherwise greatest positive token overlap, with candidate ordering by string length and final nonalphanumeric sanitization.
- Invalidation or expiry: Action set is obtained for the current state each call; no durable cache is written here.
- Activation or effect: Replaces the action sent to `step` when matching rules select another candidate; effect on successful completion remains unobserved.
- Evidence limits: Hard-coded door additions and unchanged zero-overlap fallback prevent an all-actions-valid guarantee. Replay and other task adapters bypass this helper.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `mcts_utils/sciworld/mcts_sci.py`, `mcts_utils/sciworld/eval_utils_sw.py`, `mcts_utils/llm_server.py`.

> topValue = 0.0
> topAction = predictions[0]
> --- `mcts_utils/sciworld/eval_utils_sw.py`

> new_action = findValidActionNew([new_action], current_env, current_env.get_look_around(), current_recent_actions)
> --- `mcts_utils/sciworld/mcts_sci.py`

#### RT-RTE-revision-export
Label: Ranked-path critique and conversation admission

Endpoints: caller-selected tree files → positive-root/terminal-leaf filtering → ranked high/low pairs → optional model critique → synthetic revision conversation → append-only JSONL. Owner: `path_collection.py`. Trigger is a separate CLI invocation over numerically sorted JSON filenames; advertised min/max/step options do not slice that list. Proposed change: training examples, not live actor weights. Computational decisions filter root/leaf scores and optional critique; caller supplies thresholds and mode but no per-content approval. No reference answer is supplied to the verifier: it receives task description, preceding action/observation text and current action/observation, then judges usefulness. Environment reward supplies path ranking, a separate outcome signal.

Operating modes: `good` exports high paths; paired mode with `--revise 0` splices complete low/high paths without critique; `centric` with revision uses the local model to find the first judgment lacking `good` or `uncertain`. The prompt asks for reasons and a categorical judgment. Model text can stop/truncate the bad prefix; software always adds a stock self-correction thought and `Action: wait`, then appends the good continuation while omitting an initially identical response prefix. The wait observation `ok.` is fabricated by construction, not a fresh environment transition. Critique reasons persist as `revise_feedback`, not as the actor's generated correction rationale. No formulated method theory is revised here; action-specific judgment and synthetic corrective examples do not by themselves establish theory-builder conditions.

- Immediate return: Appends records with `revise_log` and, in paired mode, high/low logs and critique feedback; successful output is conditional on reaching past the threshold defects.
- Later read-back: README intends these conversations for external Xtuner training; actual optimizer ingestion and later checkpoint consumer are not wired in the captured code.
- Delegated visibility: Verifier gets a word-count-truncated action/observation prompt, not tree statistics or the successful path; the JSONL stores conversations and optional feedback.
- Selection predicate: Positive root; terminal childless leaves sorted by average value; all ordered distinct pairs with an intended score gap and high-leaf threshold. No same-parent restriction.
- Invalidation or expiry: Append mode without deduplication, expiry or per-row invalidation; repeated invocation can duplicate any rows that reach the writer.
- Activation or effect: Model judgments can delimit the erroneous prefix; software adds a fixed revision cue and loss flags. Actual weight changes and behavioral activation are unobserved and not implemented by this route.
- Evidence limits: Comparisons of floats to environment strings fail when reached. No output examples were supplied; this report establishes the source construction and its defects, not successful data export.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection: nonpositive roots and intended score predicates reject examples; verifier controls truncation but is not a correctness-certifying admission gate. The `good` mode returns without critique. Recovery/rollback: no transactional export or automatic rollback; caller would need to curate/rebuild/remove rows. Proposal guidance: `prompt_template` requests usefulness judgments; `revision_thoughts` supplies stock admissions of error. What persists is training conversation plus source path logs and model feedback, not a newly learned runtime policy. Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`.

> if i != j and node_avg_value(leaf_paths[i][-1]) - node_avg_value(leaf_paths[j][-1]) > os.environ["BETA"]
> --- `path_collection.py`

> if float(high_path[-1].value) <= os.environ["ALPHA"]:
>     continue
> --- `path_collection.py:219-220`

> if "good" in judgement.lower() or "uncertain" in judgement.lower():
>     revise_path.append(node)
> --- `path_collection.py`

> bad_log.append({"role": "assistant", "content": f"Thought: {revision_thought}\nAction: wait", "loss": True})
> bad_log.append({"role": "user", "content": "ok."})
> --- `path_collection.py`

#### RT-RTE-agent-evaluation
Label: Direct actor rollout and supplied-prefix alternative

Endpoints: test-task IDs and configured actor → repeated action/observation interaction → scored result JSON. Owner: `eval.py` and `perform_test`; proposer: local model; continuation decision: symbolic loop using step counter, server done and negative reward. Operating mode is bounded benchmark evaluation, not search. Answer oracle: external environment reward/done, not reference action trajectories. Principal is the caller; no per-action approval. Model receives natural-language conversation messages, trimmed at fixed positions; environment sees the suffix after `Action:`. SciWorld invokes the substitution route. `perform_test_revise` is an available helper with caller-supplied response strings executed before model continuation, not a CLI-selected route.

- Immediate return: Score, task/model label, continuation step count and message state saved under `test_result/{Task}/{model_name}_{MODEL_TYPE}`; prefix helper writes under `revise_result` and preserves a separate full history during continuation.
- Later read-back: inapplicable — the inspected evaluator writes result files but no later consumer of those results is shipped in the three drivers.
- Delegated visibility: Model gets current conversation; server gets each action. Supplied-prefix helper executes caller content without requiring a new model proposal.
- Selection predicate: Test IDs from `test_id/{Task}_test.json`; loop stops on max continuation steps, server done or negative reward. No MCTS successor ranking or critique.
- Invalidation or expiry: Existing-file skip checks a path without `MODEL_TYPE`, whereas the writer includes it; no reliable result freshness/expiry check.
- Activation or effect: Direct environment steps and final reward persistence; no evidence of revision-trained superiority or an actually completed evaluation.
- Evidence limits: Referenced test directory is absent. Prefix actions are not counted by the continuation budget and do not short-circuit their supplied loop on done; external environment behavior is uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery: no local provider/environment exception recovery; result is written only at completion. Evidence: SRC-1, `eval.py`, `mcts_utils/llm_server.py`.

> temp = read_json(f"test_id/{Task}_test.json")
> --- `eval.py`

> new_action = agent_response.split('Action:')[-1].strip()
> --- `mcts_utils/llm_server.py:107-107`

> dir_path = f"test_result/{Task}/{model_name}_{model_type}"
> --- `mcts_utils/llm_server.py`

#### RT-RTE-provider-alternate
Label: Injected API inference and retry

Endpoints: supplied messages/model-name → Azure/OpenAI chat call → first returned choice text. Owner: `FuncCall`; component: [RT-CMP-func-call](#rt-cmp-func-call). Fixed symbolic control selects the `gpt` branch; model interprets messages. Credentials and endpoint configuration are caller inputs. No provider-native tool/function invocation or parameter update is requested in this inspected wrapper.

- Immediate return: First choice content, or integer `-1` after the exception retry limit.
- Later read-back: inapplicable — wrapper writes no retained state; a consuming search/evaluation caller would own any persistence.
- Delegated visibility: Remote provider receives supplied messages and deployment name; provider-side retention is uninspected.
- Selection predicate: API branch is selected by `gpt` substring in the supplied name; shipped CLI drivers instead instantiate the local wrapper.
- Invalidation or expiry: inapplicable — no local response cache or checkpoint is maintained.
- Activation or effect: API response can supply action/critique text when a caller injects this wrapper; no shipped CLI activation or observed call was supplied.
- Evidence limits: Unsupported model-name branches and repeated exceptions can fail to provide a usable string; endpoint internals and remote policy are outside the frozen source.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Recovery scope: immediate exception retry only, no backoff or environment reconciliation. Evidence: SRC-1, `mcts_utils/llm_server.py`, and offline instantiation in all three drivers.

> if ind > 100000:
>     return -1
> ind += 1
> continue
> --- `mcts_utils/llm_server.py`

### Claims

#### RT-CLM-iterative-training
Label: Claimed iterative self-training

Claimed operation: actor-guided identification of the first error, splice to an adjacent successful path, training and iterative refinement of error correction/dataset construction. Source: SRC-1, `README.md`, doctrine/design. The code implements tree generation and a partly defective data-construction route, not the full claimed loop. Its unrestricted distinct-path pairing does not enforce same-parent adjacency. The documented optimizer/configuration and checkpoint admission machinery are absent from the tracked artifact; no successful training or improvement evidence was supplied.

- design conclusion status: claimed
- operation conclusion status: uninspected

> Starting from it, we splice it with the adjacent correct path, which shares the same parent node in the tree.
> --- `README.md`

The passage above is part of a longer README line; it states intent, not an executable invariant. The introduction describes the framework as iterative self-training. For that named self-improvement claim, the assessment boundary is the captured builder plane plus its proposed later actor, horizon is collection → export → retraining → later deployment, and objective is better task completion/reward independently of any particular update. Link 1 is source-level score/judgment-driven determination of examples, qualified by export defects. Link 2 (change of own parameters/other deployed organization), link 3 (changed checkpoint entering a live authority path) and link 4 (later behavior causally depending on that update) are unestablished. This supports a declared improvement-directed design, not exercised self-improvement or successful learning. Action critique is requested; reliable reflective behavior and autonomous completion of training/admission are not established. These limits do not negate the inspectable action-generation and tree-selection capacities.

### Evidenced absences

#### RT-ABS-training-machinery
Label: Missing shipped training and promotion machinery

- implementation conclusion status: absent

Searched boundary: the complete tracked tree at SRC-1 revision `82fcc1ca7873b460949ed49022146dd988c32e31`, enumerated with `git ls-tree -r --name-only HEAD` after confirming HEAD. Query: advertised `xtuner_config/` and `llama3_8b_instruct_full_alpaca_e3_copy.py`, and training/checkpoint-promotion entry paths. The tree contains only the three drivers, MCTS/model/task utilities, task JSONs, docs/assets and housekeeping; no advertised training directory/configuration is present. README explicitly delegates training to Xtuner. This supports bounded absence of shipped optimizer/configuration/promotion code, not absence of the external project's capabilities or of a training run elsewhere. It prevents an implementation-grounded closed-loop improvement conclusion. Evidence: SRC-1, `README.md`, tracked-tree inventory recorded in the boundary.

> cd xtuner_config/
> NPROC_PER_NODE=${ARNOLD_WORKER_GPU} NNODES=${ARNOLD_WORKER_NUM} PORT=${ARNOLD_WORKER_0_PORT} ADDR=${ARNOLD_WORKER_0_HOST} NODE_RANK=${ARNOLD_ID} xtuner train llama3_8b_instruct_full_alpaca_e3_copy.py --deepspeed deepspeed_zero2
> --- `README.md`

### Behavioral-authority paths

#### RT-BAP-model-action
Label: Model response to environment action

Consumer: adapter `_generate` or evaluation rollout. Channel: chat response parsed into an action string; SciWorld may substitute another string. Force: executable task-environment action, not merely displayed advice; restricted by actual server capabilities and done/budget handling, not human approval. Horizon: current rollout/search branch. Source-native thought text and instructions are natural language interpreted by the model; extraction and task dispatch are symbolic rules. Evidence: SRC-1, `mcts_utils/webshop/mcts_ws.py`, `mcts_utils/textcraft/mcts_tc.py`, `mcts_utils/sciworld/mcts_sci.py`, `mcts_utils/llm_server.py`; route details in [RT-RTE-tree-collection](#rt-rte-tree-collection) and [RT-RTE-agent-evaluation](#rt-rte-agent-evaluation).

> step_output = current_env.step(new_action)
> --- `mcts_utils/webshop/mcts_ws.py`

#### RT-BAP-verifier-prefix
Label: Verifier judgment to exported erroneous prefix

Consumer: `revise_worst_path`. Channel: returned judgment text after `Judgement:`, lowercased and substring-tested. Force: chooses whether to continue collecting the bad prefix or break at the current step; not a verified truth assertion, parameter update or deployment approval. Horizon: one candidate conversation, retained in JSONL if the export path succeeds. Reasons persist as feedback but the inserted actor revision cue comes from static strings. Human intervention is batch configuration rather than per-example admission. Evidence: SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`, with exact decision passage in [RT-RTE-revision-export](#rt-rte-revision-export).

## Annotations

none
