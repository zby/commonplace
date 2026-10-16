---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "PrimeScientist runtime baseline: filesystem-backed research search, benchmark execution, scoring and plan admission at the frozen revision."
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
---

# PrimeScientist runtime report

## Runtime account

### Work and ordinary invocation

PrimeScientist controls repeated research-replication or code-optimization attempts. It changes the next plan and starting workspace using prior scores and artifacts; it does not implement the underlying coding agent's tool loop. The boundary's SRC-1 is the sole evidence source. All findings below concern inspected implementation or prompt requests at that revision. No execution trace or causal experiment was supplied, and no target was executed. Invocation success, actual skill use, proposal quality and budget savings remain unobserved. See [boundary](boundary.md#boundary-and-evidence).

An operator launches `run_search.py` directly or through a shipped shell launcher. The CLI chooses benchmark, task, worker and reflector model, evaluation budget, branching cap, depth, repeated attempts, pruning threshold and optional token/time/estimated-dollar limits. CLI defaults select FIRE-Bench, Codex, `gpt-5` for both worker and reflector, ten evaluations, two proposals, unlimited depth and one attempt per node. The Python function has different defaults for depth and reflector model; CLI argument forwarding, not those defaults, determines ordinary CLI operation. The operator supplies the task and initial controls, not per-proposal approval. SRC-1, `run_search.py`; the launcher ownership is established in `boundary.md`.

The driver loads the benchmark and a task-specific tree directory, creates ledgers, and reloads an existing root when `root/stats.json` exists. Otherwise it creates root state and asks a reflector to write `root/skill.md`. Initialization copies the task instruction and other-task insight files into the reflector's working directory. A successful reflector process is not proof that the root plan exists: the adapter checks it before execution. `--force_init` removes the root, ledgers, session file and reflector logs, but retains task-level instruction and insights. Initialization happens before the main loop's wall-clock timer and budget guard. SRC-1, `run_search.py`, `search/reflector.py`, `search/tree.py`.

The next-step owner is Python. It computes alpha from the minimum remaining token/time ratio, then calls the source-named `puct_select_leaf`, whose implementation is stochastic BAVT rather than a PUCT upper-confidence expression. Visited children receive weights based on Q; unvisited children use parent Q and the square root of P. Q is a running mean backpropagated from descendants, not simply the node's own measured packet score. A selected node without a packet is executed; a node with a packet is expanded. Search thus alternates symbolic selection with model-dependent plan construction and delegated coding. [RT-RTE-search-execution](#rt-rte-search-execution), [RT-RTE-plan-admission](#rt-rte-plan-admission). SRC-1, `search/tree.py`, `run_search.py`.

For an ordinary AutoLab attempt, the adapter stages the node plan, copies pristine task code into a fresh workspace, installs a native Codex skill file, prebuilds the verifier image, writes an optional build-check helper, and invokes Codex with the task instruction. The agent can edit and execute code through its external runtime. After it returns, the adapter builds/runs the task verifier, reads reward JSON, returns a packet and cost estimate, and the driver moves the winning log/workspace into the node directory. The driver either persists the packet and backpropagates the reward or score-prunes the child; it then writes ledgers. On a positive-Q parent with a retained sandbox, children instead start from the copied parent workspace. The workflow loop is sequential; `_run_node`'s comment about a thread pool is not evidence of parallel search scheduling. SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`.

FIRE-Bench follows the same driver ownership but dispatches a separate Python runner. Its fresh Codex path copies task data and utility code; its inherited path copies the parent sandbox, copies available `diff.py` and `changes.md`, refreshes the staged skill and API-key file, and prepends an inheritance notice. The dispatcher falls back to fresh execution when a selected agent lacks an inheritance runner. It sets a one-hour subprocess timeout and accepts task completion without requiring a zero subprocess exit. The adapter identifies run IDs from newly found logs rather than receiving a typed run result. A process failure with a log can therefore still proceed to evaluation. SRC-1, `benchmarks/fire_bench/__init__.py`, `benchmarks/fire_bench/run_agent.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

The terminal product is a retained tree, packets, logs, workspaces, result/cost ledgers and a printed best-Q summary. This is not automatic installation into production or a verified final scientific result. The tree's `best_node` searches nonhidden descendants using Q. Score-pruned nodes keep their packet and artifacts but disappear from normal selection. See [RT-RTE-score-evaluation](#rt-rte-score-evaluation). SRC-1, `run_search.py`, `search/tree.py`.

### Selected forcing cases and guarantees

Four source-inspected forcing cases bound the ordinary path. They are code-path analyses, not executed tests.

1. **Proposal exists but its requested provenance does not.** FIRE-Bench requests a generated `diff.py` to produce a complete plan. `_bootstrap_proposal` only requires that `skill.md` exists, defaults or clamps the numerical prior, and does not check completeness, size, scientific validity, whether the diff was run, or whether proposals are substantively different. Existing raw proposal directories are bootstrapped before any new reflector call. The owner is the driver; the enforcement point gives an existence invariant on proposals admitted through this bootstrap, not a semantic plan guarantee. Root initialization and manual filesystem state are alternate paths, so this invariant is not a universal tree-state guarantee. [RT-RTE-plan-admission](#rt-rte-plan-admission). SRC-1, `run_search.py`, `search/reflector.py`.

2. **Budget exhaustion during one delegated operation.** The driver checks ledger totals and elapsed time between steps and after results, not at each worker tool call. `n_runs` executes multiple agent/evaluator calls before returning and counts one accepted node packet as one evaluation. AutoLab's coding subprocess has no timeout here; FIRE-Bench's dispatcher has a one-hour timeout, not the remaining global budget. Reflector calls have their own timeout. A failed search execution does not increment `evals_done`; absent other limits it may repeatedly select an unrun failed node. Consequently the advertised hard dollar stop is a best-effort estimated-ledger policy, not an invariant preventing overspend or wall-clock overrun. Initial reflection is outside the loop's timer/guard. Required external contracts are complete cost reporting and subprocess/runtime cooperation; neither was observed. implementation conclusion status: wired. operation conclusion status: uninspected. SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/run_agent.py`, `search/reflector.py`.

3. **The same task plan under different effect envelopes.** FIRE-Bench host Codex requests `workspace-write`; Docker/enroot Codex instead request `danger-full-access` inside their external containers, with writable workspace and credential-directory mounts and model-service keys. AutoLab's agent and the reflector both request host `danger-full-access` and never ask for approval. AutoLab's container is the verifier, not the coding-agent containment boundary. OpenHands additionally mounts the Docker socket. Hence neither a directory called sandbox nor a verifier container establishes global agent confinement. Owners/enforcement points are respectively the external Codex runtime, external container/host configuration and Docker service. Guarantee strength: deployment guarantee only if those external contracts actually enforce the intended limits; source configuration alone is afforded, not an observed deployment guarantee. SRC-1, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py`, `benchmarks/autolab/__init__.py`, `search/reflector.py`.

4. **Linear baseline bypasses reflector/tree admission.** `run_vanilla.py` stages recent attempt history as the worker skill, starts from a best-so-far workspace, and keeps a new workspace only on strict score improvement. It does not use tree priors or reflector-written child plans. Its recovery replays consecutive saved iteration packets; gaps or malformed packets stop replay. This is a separate bounded-experiment mode, not proof that all retained state passes the tree's proposal gate. [RT-RTE-vanilla-retention](#rt-rte-vanilla-retention). SRC-1, `run_vanilla.py`.

Capability surface, current grants and isolation are different. The workflow grants a coding agent a workspace, instruction, staged skill and potentially provider keys; it grants the reflector shell-mediated access to the task tree and permission to write proposals. Current deployed filesystem/network grants and actual provider/tool availability are unobserved. Host callbacks, shell-spawned programs, direct model-service calls from task utilities and container services remain inside the effect surface available to their respective executors; the driver does not interpose a per-tool approval gate. External agent implementations are excluded by the boundary, so their internal tool lists, provider-native tools, compaction and scheduling cannot be exhaustively enumerated here. The inspected material alternates are fresh/inherited Codex, host/Docker/enroot, OpenHands, direct FIRE-Bench dispatcher and vanilla execution. These configurations do not all share a single enforcement point. SRC-1, `run_search.py`, `search/reflector.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/run_agent.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/openhands/run.py`.

### Context, continuity and added inspection

The reflector implementation contradicts its introductory fresh-session description: it stores a Codex session ID and requests `exec resume`, clearing saved state on a failed resume. This provides an external continuation path in addition to tree files; it does not establish what the resumed model window contains. Failed resume recovery itself can lose provider-side context. Separate worker invocations receive task instruction and skill/workspace material, while only artifacts, logs and evaluated packets cross back to the search driver. This resembles separate task frames with filesystem outputs escaping, not a shared model context. All host-managed compaction and automatic native-skill loading remain opaque. SRC-1, `search/reflector.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/agents/codex/run.py`.

The code produces a 100-head/500-tail log brief and hides the full log under `.log.log`. The deciding code keeps the task header and recent conclusion preferentially, omits middle tool/thinking lines, and leaves the full file reachable. Prompt instructions discourage rereading it; FIRE-Bench explicitly permits a full-log read when failure remains ambiguous. Hiding is not access denial. Prior session turns may also remain in a resumed context, so the brief is a controlled diagnostic delivery path rather than proof of bounded total context. SRC-1, `search/reflector.py`, `run_search.py`.

Additional implementation inspection beyond the boundary's initial scope covered driver retry/bootstrap/budget/CLI bodies, the complete tree and reflector modules, AutoLab staging/agent/Docker verifier bodies, FIRE-Bench adapter/dispatcher, Codex inheritance/context and host/container command construction, OpenHands dispatch, native-skill writer, vanilla replay/keep-revert bodies, and RAGChecker's scoring entry and model configuration. All are SRC-1 at the frozen revision. Most per-task test correctness, enroot build/evaluation helper bodies, utility model-service behavior and vendored RAGChecker internals remain uninspected. Those limits prevent exhaustive evaluator reliability, enroot equivalence, task-oracle correctness or downstream utility-call guarantees, not a bounded control-flow account.

## Shared records

### Components

#### RT-CMP-coding-model
Label: Worker coding model

Source-native identity: worker `model`/`LLM_MODEL` argument, default `gpt-5` in the search CLI, consumed by external Codex or OpenHands. Representational form: distributed-parametric. Storage substrate: external provider weights, not the tree filesystem. Parameters changing during operation: uninspected — this repository supplies invocation arguments, not provider internals or weight updates. Exact model version pinned: no immutable weight/deployment version is supplied. Mutable endpoint resolving to another model: possible and unresolved; a model name and configurable service endpoint do not freeze provider resolution. Fixed parameters cannot be inferred. SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/openhands/run.py`.

> "--model", model,
> "--config", "sandbox_mode=danger-full-access",
> "--ask-for-approval=never",
> --- `benchmarks/autolab/__init__.py`

#### RT-CMP-reflector-model
Label: Reflector coding model

Source-native identity: `reflector_model`, passed to Codex 0.121.0 by `_run_codex`. Representational form: distributed-parametric; storage substrate: external provider parameters. Parameters changing during operation: uninspected. Exact model version pinned: no; the client package version is pinned, not model weights. Mutable endpoint resolving to another model: unresolved and possible under external provider configuration. Its durable session and authored plans are separate from weights. SRC-1, `search/reflector.py`, `run_search.py`.

> REFLECTOR_CODEX_VERSION = "0.121.0"
> --- `search/reflector.py`

> "npx", "--yes", f"@openai/codex@{REFLECTOR_CODEX_VERSION}",
> "--model", model,
> "--config", "sandbox_mode=danger-full-access",
> "--ask-for-approval=never",
> --- `search/reflector.py`

#### RT-CMP-eval-model
Label: FIRE-Bench conclusion-extraction model

Source-native identity: `eval_model = "gpt-5.2"`, used through the evaluator's OpenAI client, including the extraction call in `eval_single_log`. Representational form: distributed-parametric; storage substrate: provider weights. Parameters changing during operation: uninspected. Exact model version pinned: no immutable provider revision. Mutable endpoint resolution: uninspected; the model alias can depend on provider resolution. This component transforms an agent narrative before scoring; it is not the task executor. SRC-1, `benchmarks/fire_bench/eval/RAGChecker/eval.py`.

> eval_model = "gpt-5.2"
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

#### RT-CMP-ragchecker-models
Label: RAGChecker extractor and checker

Source-native identity: `extractor_name` and `checker_name`, both `openai/gpt-4.1`. Representational form: distributed-parametric; storage substrate: external model parameters. Their exact versions are not pinned; operational parameter mutation and endpoint resolution are uninspected. Equal configured names do not establish a shared fixed provider instance. The extractor/checker roles are configured separately, but have the same evidence and mutability limits here. SRC-1, `benchmarks/fire_bench/eval/RAGChecker/eval.py`.

> evaluator = RAGChecker(
>     extractor_name="openai/gpt-4.1",
>     checker_name="openai/gpt-4.1",
>     batch_size_extractor=8,
>     batch_size_checker=8
> )
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

### Operative objects

#### RT-OBJ-skill
Label: Node skill plan

Source-native identity: node `skill.md`. Representational form: natural-language experimental or optimization instructions. Storage substrate: task-tree file, then benchmark staging file and agent-native skill file. Python checks existence and copies bytes; the external agent interprets the plan. The file may contain hypotheses and methods, but its name alone does not establish scientific warrant or content-directed criticism. SRC-1, `search/reflector.py`, `run_search.py`, `benchmarks/utils.py`.

> Your job — write ONE file into root/:
>   root/skill.md   (< 10 KB)
> --- `search/reflector.py`

#### RT-OBJ-stats
Label: Tree statistics

Source-native identity: `stats.json` containing visits, Q and P. Representational form: symbolic numeric fields with fixed Python selection/update rules, not model parameters. Storage substrate: one JSON file per node. Q accumulates descendant scores as a running average. SRC-1, `search/tree.py`.

> stats["visits"] = n + 1
> stats["Q"] = (q * n + f1) / (n + 1)
> self._write_stats(stats)
> --- `search/tree.py`

#### RT-OBJ-sandbox
Label: Retained run sandbox

Source-native identity: node `sandbox/` or baseline `best_sandbox`. Storage substrate: copied/moved filesystem tree. Representational form: executable files consumed symbolically by their runtimes; natural-language files have distinct model interpretation paths. This is a mixed container, not one homogeneous memory encoding. It is execution state and a possible subsequent attempt's starting code/data, not a containment guarantee. SRC-1, `run_search.py`, `run_vanilla.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

> print(f"[run_inherit] Seeding sandbox from {seed_path}")
> shutil.copytree(str(seed_path), str(sandbox_volume_path))
> --- `benchmarks/fire_bench/agents/codex/run_inherit.py`

### Routes

#### RT-RTE-search-execution
Label: Select, execute and retain a tree node

Endpoints: CLI/task state → selected node → benchmark runner → evaluator packet → tree/ledgers and printed summary. Owner: Python driver; task principal: launching operator, delegated executor: chosen external agent. State/context/action: selected plan and optional inherited workspace enter a separate worker invocation; filesystem/code changes and evaluation diagnostics return as artifacts. Computational selection and pruning decide progression. Humans choose initial task/options; no per-node veto is requested here. Operating mode: bounded repeated experiments with benchmark-specific answer oracle supplied by [RT-RTE-score-evaluation](#rt-rte-score-evaluation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `_run_node` returns node, best packet and primary score, or packet=None on failure.
- Later read-back: later selection reloads Q/P/packet existence; later reflection reads packets/plans/artifacts; children can copy a positive-Q parent's sandbox.
- Delegated visibility: worker receives task instruction, staged plan and fresh/inherited workspace; driver receives evaluation packet and artifact paths, not a shared agent context.
- Selection predicate: stochastic BAVT; run when selected node lacks packet, otherwise expand; best-of-n attempts chooses strict maximum primary score.
- Invalidation or expiry: optional score-pruning hides children; force-init clears run-specific state; no timed expiry shown for ordinary tree artifacts.
- Activation or effect: score controls persistence/pruning and future weights by Python rules; actual model compliance with skill is unobserved.
- Evidence limits: no run evidence; child inheritance uses positive aggregate Q and sandbox presence, not independently verified parent correctness.

Admission of code changes occurs by artifact retention and reuse, not production installation. A child may be hidden when its primary score is sufficiently below parent Q; its packet survives, and its score is not backpropagated. This rejects a search branch, not an unsafe action already executed. Recovery is partial filesystem resume rather than transactional checkpointing. SRC-1, `run_search.py`, `search/tree.py`.

> run_id = benchmark.run_agent(task, agent, model, run_env,
>                              env_override=env_override,
>                              node_dir=node.path)
> if run_id is None:
>     continue
> packet  = benchmark.evaluate(task, run_id)
> primary = benchmark.primary_score(packet)
> --- `run_search.py`

> if should_prune:
>     _prune_node(node, parent, primary, packet, prune_threshold)
>     # no backpropagate — pruned score must not drag parent Q down
> else:
>     node.write_packet(packet)
>     node.backpropagate(primary)
> --- `run_search.py`

#### RT-RTE-plan-admission
Label: Reflect and bootstrap successor plans

Endpoints: completed node plus other tree state → Codex reflector → filesystem proposals → bootstrapped children. Trigger: a selected node already has a packet and can be expanded/re-expanded. Proposed change: child task plan, prior rationale and optionally executable plan transformation. Owner/proposer: reflector agent; admission/next selection: driver. The launching human can externally edit files but no interactive proposal review is wired. Software can archive a missing-plan proposal or score-prune it after execution. Operating mode: bounded task experiments; improvement trigger: new result or all children pruned; answer oracle: subsequent benchmark score, not reflector judgment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reflector success/cost, then number of ready children from the retry wrapper.
- Later read-back: proposals persist as child plans/priors/stats; the next worker consumes the chosen plan; later reflector calls can read proposal rationale and scores.
- Delegated visibility: reflector sees tree filesystem and requested resumed session, selected node path and diagnostic pointers; FIRE-Bench child additionally receives available diff/changes files in inherited workspace.
- Selection predicate: bootstrap sorted visible unprocessed directories capped at requested count; a later BAVT traversal selects admitted children using P/Q.
- Invalidation or expiry: missing skill archives the proposal; two reflection attempts precede stopping; failed resumed process clears saved session state; score-pruned branches can trigger new proposals.
- Activation or effect: existence/prior checks produce selectable symbolic nodes; prompt requests diagnostic interpretation and materially different hypotheses, but compliance is unobserved.
- Evidence limits: plan quality, requested diff provenance and claimed criticism are not validated; retained rationale is requested, not established as actually authored or consulted in a run.

Guidance says to diagnose concrete verifier/runtime results, avoid tried approaches, distinguish setup errors from genuine low scores, and make different hypotheses rather than small variants. AutoLab requests compact incremental plans; FIRE-Bench requests a full self-contained plan generated through `diff.py`. What persists is plans, requested hypothesis/rationale/changes/risks, outcomes, diagnostics and session bookkeeping. It does not revise the shipped search policy or reflector prompt in this path. SRC-1, `search/reflector.py`, `run_search.py`, `benchmarks/fire_bench/__init__.py`.

> "hypothesis": "<the single concrete hypothesis this proposal tests>",
> "rationale": "<2-3 sentences: WHY you expect this to improve the score,
>                grounded in specific observations from packet.json /
>                log_brief.log / sandbox — cite file or section>",
> --- `search/reflector.py:264-267`

> if not child.skill_path.exists():
>     reason = "skill.md missing — reflector did not write it"
> --- `run_search.py`

> child.set_prior(estimate)
> return True
> --- `run_search.py`

Theory account, scoped to task-plan hypotheses rather than the method's own theory:

- theory-builder conditions 1–4: condition 1 conclusion status: afforded. Requested complete plans and localized hypothesis fields can formulate a whole theory-like unit; no supplied generated content establishes a particular theory.
- theory-builder conditions 1–4: condition 2 conclusion status: afforded. Staging and model interpretation provide a consumption path; delivery alone does not establish decisions depending on what a hypothesis says.
- theory-builder conditions 1–4: condition 3 conclusion status: claimed. Prompts request result-grounded diagnosis and different hypotheses; this does not demonstrate criticism assigning blame to a theory/test/data/auxiliary or a consequent revision.
- theory-builder conditions 1–4: condition 4 conclusion status: afforded. Files and resumed sessions can carry criticism into a next round, but no observed criticism-to-successor dependence establishes exercised iteration.
- Addressability: whole plan replacement and named hypothesis/rationale fields afford localized editing; individually stated assumptions and scope conditions in generated content are uninspected.
- Persistence: task-tree files survive rounds and process restarts; actual persistence of a formulated criticism and its later reader is unobserved.
- learning: uninspected — improved future capacity and causal benefit were not measured; retention and selection do not establish them.
- Reflection: wired at the operational representation level: completed attempts produce packets/logs/diffs that are presented to a reflector, whose admitted outputs can alter subsequent task plans. Model-mediated behavioral dependence is unobserved. This does not establish reflective revision of the shipped method texts.
- Reflective theory builder: uninspected — no supplied run shows method-text criticism meeting conditions 1–4.
- Autonomous theory builder: afforded — computation owns the internal proposal/admission/execution loop without per-content human approval, but the four theory operations are not established as exercised.

A dispositional improvement-directed self-change pathway exists over rounds of one task: outcome evidence is delivered to a proposer; retained plans and starting code can become later behavioral guidance. The objective is benchmark primary score, independently defined by the adapter. Exercised self-improvement remains unestablished: causal dependence of the update on evidence and of later operation on the update is unobserved, and successful improvement needs additional outcome evidence. Task-code improvement alone need not improve PrimeScientist's method. SRC-1, `search/reflector.py`, `run_search.py`.

#### RT-RTE-score-evaluation
Label: Evaluate an attempt and return primary score

Endpoints: completed run/workspace or log ID → benchmark evaluator → packet primary score. Owner: adapter/evaluator; driver decides branch admission, not the worker's own success narrative. Proposer: worker supplies code/narrative; decision: test machinery or model-backed comparison; human contribution: supplied benchmark reference/task tests, with their individual provenance/correctness uninspected. Operating mode: bounded benchmark trials. Answer oracle differs: AutoLab's task-specific test script and its references produce reward; FIRE-Bench uses `gt[task]` and `query[task]` as reference content for RAGChecker comparison.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON-like packet; primary score is AutoLab reward or FIRE-Bench F1, defaulting missing score to zero.
- Later read-back: driver stores packet and updates stats; later reflection receives score/diagnostic pointers; pruning records summarize rejected approaches.
- Delegated visibility: AutoLab verifier sees submitted code and mounted tests; FIRE-Bench scoring entry sees extracted log conclusion transformed into core idea plus task query/reference answer.
- Selection predicate: task/run-ID selects log or workspace; FIRE-Bench discovers new result files and attaches scores; node repeated runs retain the maximum.
- Invalidation or expiry: inapplicable — this route returns an evaluation; branch hiding and rerun/resume are driver responsibilities.
- Activation or effect: primary score numerically governs keep/prune/selection; no observed score reliability or scientific truth is established.
- Evidence limits: task-test correctness, conclusion extraction fidelity, provider judgment reliability and metric validity are not experimentally assessed.

The load-bearing guarantee is that this driver uses adapter primary score rather than the worker's unsupported success assertion. Owner/enforcement point: `_run_node` and `benchmark.primary_score`. Strength: protocol for the ordinary adapter return path, not truth invariant. Required external contract: verifier/reference correctness and faithful transformation/score attachment. Alternate `--skip_eval` returns a zero-score synthetic packet after setup without running the agent or evaluator, so it is explicitly not evaluated work. SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/__init__.py`, `benchmarks/fire_bench/eval/RAGChecker/eval.py`.

> raw_conclusion = extract_single_final_thought(log_path)
> core_idea = extract_core_idea(raw_conclusion, client, eval_model)
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

> "query": f"{query[task]}",
> "gt_answer": f"{gt[task]}",
> "response": f"{core_idea}",
> "retrieved_context": []
> --- `benchmarks/fire_bench/eval/RAGChecker/eval.py`

> reward_json = reward_dir / "reward.json"
> if not reward_json.exists():
>     print(f"  [docker] WARNING: reward.json not produced")
> --- `benchmarks/autolab/__init__.py`

#### RT-RTE-vanilla-retention
Label: Linear baseline keep or revert

Endpoints: prior iteration packets/best workspace → staged history → worker/evaluator → iteration packet and optional replacement best workspace. Owner: `run_vanilla`; proposer: worker; admission/veto: strict Python score comparison. Human contribution: task/options and benchmark assets, not approval of each code change. Operating mode: bounded linear experiments, same adapter answer oracles as tree search. Trigger: next iteration below caps; proposed change: code/workspace produced by worker with prior history guidance. Rejection ability: retain old `best_sandbox` on nonimprovement. Recovery: replay saved packets, reuse best workspace, abort after three consecutive no-run-ID failures; unsuccessful copy replacement can leave score bookkeeping ahead of reusable code.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved iteration result/action and final printed summary.
- Later read-back: history is reconstructed from earlier packets; kept best workspace seeds later attempts when positive best score and workspace exist.
- Delegated visibility: worker receives formatted history as skill plus task instruction and selected workspace; evaluator returns packet to driver.
- Selection predicate: retain new best only when score > best_score; no reflector or tree-prior selection.
- Invalidation or expiry: replace best workspace on improvement; replay stops at first missing/malformed sequential packet; no timed history expiry.
- Activation or effect: Python decides kept/reverted status and seed path; influence of history text on model actions is unobserved.
- Evidence limits: the copied workspace's correctness depends on evaluator; score/action packet persistence and workspace replacement are not transactional.

Guidance summarizes prior attempt scores/actions and asks the worker to improve under the same task. Code selects the last ten entries and truncates each summary to 400 characters before staging history; older packets remain on disk but this route does not inject them. The deciding agent is this fixed code rule, not the worker. It retains attempt records even when code is rejected. This is product-code admission, not admission of a revised framework or production machinery. SRC-1, `run_vanilla.py`.

> action = "kept" if score > best_score else "reverted"
> --- `run_vanilla.py`

> _commit(iter_sandbox, best_sandbox)
> print(f"  [commit] score {score:.4f} > prev best {best_score:.4f} → best_sandbox updated")
> --- `run_vanilla.py`

### Claims

#### RT-CLM-budget-stop
Label: Estimated dollar hard stop

Claimed operation: CLI help describes an estimated-dollar limit as a hard stop. Source: SRC-1, `run_search.py`. Implementation qualifies the claim: guard checks between whole operations, after initialization and repeated runs; it does not preempt every provider/tool effect or bound unreported costs. Guarantee strength: best effort. implementation conclusion status: wired. operation conclusion status: uninspected.

> help="Hard stop when estimated total $ (agent+reflector, per costs.tsv) exceeds this; 0=unlimited")
> --- `run_search.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-plan-worker
Label: Plan to coding worker

Consumer: external Codex/OpenHands agent. Channel: Codex native skill files with implicit invocation enabled; OpenHands inline instruction suffix. Force: model-interpreted guidance, not a Python-enforced research procedure. Horizon: selected worker invocation, with new staged material or inherited artifacts available to later attempts. File delivery is wired; actual loading and compliance are unobserved. SRC-1, `benchmarks/utils.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py`.

> "policy:\n"
> "  allow_implicit_invocation: true\n",
> --- `benchmarks/utils.py`

#### RT-BAP-score-selector
Label: Score to symbolic selector

Consumer: driver and BAVT traversal. Channel: primary score → backpropagated Q/P/visits JSON and packet existence. Force: fixed computational rules affect branch availability and stochastic sampling weights; correctness is not implied. Horizon: subsequent rounds and resumed task-tree runs. SRC-1, `run_search.py`, `search/tree.py`.

> weights = [_bavt_weight(ch, alpha, parent=node) for ch in children]
> node = random.choices(children, weights=weights, k=1)[0]
> --- `search/tree.py`

## Annotations

none
