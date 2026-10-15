---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Hyperagents runtime baseline: code-editing generations, task evaluation, lineage replay and optional selection/ensemble execution at the frozen revision."
run-id: AAS-2026-10-14-hyperagents-dd9d501b160c-01
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
---

# Hyperagents runtime report

## Runtime account

### Evidence and consequential work

Hyperagents ships an outer search over code-modified task agents and their generating machinery. A host Python driver owns generation identities, prepares a root repository, replays a selected parent's patches, runs its editor, evaluates the edited task agent, saves artifacts, and selects the next parent. The initial editor asks a provider model to modify code through local Python tools. The archive can subsequently supply executable changes to that editor itself, to task agents, to tools, and optionally to selection or ensemble code. These are implemented pathways, not observed improvement. SRC-1 supplies implementation and doctrine/design only; no execution or causal experiment is registered in [the boundary](boundary.md). See [RT-RTE-generation-cycle](#rt-rte-generation-cycle), [RT-RTE-editor-admission](#rt-rte-editor-admission), and [RT-CLM-recursive-improvement](#rt-clm-recursive-improvement).

Added implementation inspection under SRC-1 includes `agent/base_agent.py`, detailed tool loading and Bash behavior in `agent/tools/__init__.py` and `agent/tools/bash.py`, path/output controls in `agent/tools/edit.py`, Git diff/reset internals in `utils/git_utils.py`, generation CLI and helper details in `generate_loop.py` and `utils/gl_utils.py`, container networking/mount configuration in `utils/docker_utils.py`, task loading/checkpointing in `domains/harness.py`, label scoring in `domains/report.py`, paper-review input formatting in `domains/paper_review/utils.py`, bounded task-action/training reads in `domains/balrog/evaluator.py` and `domains/genesis/evaluator.py`, RL entry points in `domains/genesis/genesis_train/rl_trainer.py` and `domains/genesis/genesis_eval/rl_eval.py`, Polyglot task execution in `domains/polyglot/harness.py`, replay in `domains/run_eval.py`, and the DGM editor in `baselines/dgm/coding_agent.py`. These are files at the same registered revision, not new sources. Provider implementations, full environment/grader internals and dependency training algorithms remain outside inspected implementation. No target code was executed.

### Ordinary invocation: one paper-review generation

An operator invokes `generate_loop.py --domains paper_review` after preparing initial evaluations. The CLI defaults to ten generations, `only_agent`, ten evaluation workers and `score_child_prop` selection; these differ from some callable-function defaults. The host identifies a run by timestamp or supplied ID and generations by `initial` or integers. `setup_initial_gen` copies initial reports and a filtered repository, writes a generated README, and commits the root. On resume it instead reuses the saved root commit and loads the last archive snapshot. That host code, not the model, determines the loop schedule (SRC-1, `generate_loop.py`, `utils/gl_utils.py`).

The selected parent contributes its ordered previous/current patch list. The host creates a container with the root repository mounted read-write, applies those patches and commits the reconstructed state. Previous-generation outputs are copied under `/tmp/`; normal archive delivery removes the current generation, validation/test-named artifacts, copied repositories and bytecode. These removals are filename rules, not semantic inspection of all hidden evaluation content. `no_archive` uses a different delivery path: it copies only the parent directory without this pruning routine. The ordinary editor receives a fresh model message history. Importantly, the initial `MetaAgent.forward` accepts `eval_path` and `iterations_left` but does not interpolate either into its instruction: discoverability of the copied archive or README through shell/file tools is not direct delivery of its contents to the model (SRC-1, `generate_loop.py`, `meta_agent.py`).

The editor's response is parsed for textual `<json>` calls. Host code dispatches the first valid call per turn, by name, to the tools granted by `tools_available='all'`; it sends the result back as text until no call is parsed, the count limit is reached, or an exception occurs. Tools operate in the editor process/container environment. A malformed final response can terminate this loop without editing. The initial task agent, by contrast, uses the same call helper with the default empty grant and expects a `response` field. Both use provider inference via LiteLLM; model weights are not modified by these calls. See [RT-RTE-model-tools](#rt-rte-model-tools) and [RT-CMP-provider-models](#rt-cmp-provider-models).

After the editor returns, `run_meta_agent.py` attempts to restore `domains/` to its base commit and saves a Git diff including untracked files. A nonempty saved diff enables evaluation; import checks test whether the editor/task classes can be imported, not their behavioral correctness. For paper review, the harness dynamically loads the edited `TaskAgent`, supplies a fresh instance per dataset row, and passes paper text without the outcome label through the shipped formatter. The model's answer becomes a prediction. The report compares normalized strings to the CSV's `outcome` column. Worker futures run concurrently, with periodic CSV checkpoints; existing non-NA predictions are skipped on reuse. See [RT-RTE-task-evaluation](#rt-rte-task-evaluation).

Staged evaluation permits full evaluation only when all staged domain scores are present and positive, unless explicitly skipped. Evaluation exceptions set `run_eval` false. The driver saves metadata, appends the generation to the archive regardless of its eligibility, and may invalidate a parent whose editor failed. It plots retained scores/lineage and selects the next parent. The terminal return is the output-directory path, not a final deployed winner. Neither archive membership nor `valid_parent` means improvement over the parent (SRC-1, `generate_loop.py`, `utils/gl_utils.py`; [RT-RTE-parent-selection](#rt-rte-parent-selection)).

### Four forcing cases and alternate entry paths

1. **A changed evaluator dependency or tool.** Restoring/filtering `domains/` does not stop edits to `agent/`, `utils/`, `run_meta_agent.py`, or arbitrary shell writes. Replayed code can execute on Python import, before a tool grant is checked. Thus the intended evaluation boundary is a path policy, not an adversarial integrity guarantee. Direct `run_meta_agent.py` also has no outer generation timeout or Docker requirement. [RT-RTE-editor-admission](#rt-rte-editor-admission) and [RT-BAP-code-replay](#rt-bap-code-replay) bound this claim.
2. **Failure or absent scores.** The host selector skips ineligible ordinary nodes but always treats starting nodes as candidates for its metadata check and falls back to `archive[0]` with zero score if no scored candidate survives. In `generate`, `valid_parent` also accepts `meta_patch_files is not None` as an alternative to successful score loading. CLI `meta_patch_files` defaults to an empty list, so this condition is broader than 'external nonempty patches supplied'. A failed/nonimproving generation is still archived. Therefore neither successor selection nor admission universally requires independently successful evaluation (SRC-1, `generate_loop.py`, `utils/gl_utils.py`).
3. **Editable parent selection and ensemble consumption.** When enabled, selection is executed from the latest archive node whose `can_select_next_parent` flag permits it, not necessarily from the parent chosen for task performance. Its stdout's last line identifies the next parent. Exceptions disable that node's selector and retry an earlier eligible lineage, with bounded retries. The shipped editable selector uses uniform random choice among scored candidates and has no fallback. Its CLI accepts fewer domains than the outer driver. The optional ensemble runs inherited `ensemble.py` in a separate container, but its default behavior is to return an existing prediction from the highest-scoring archived agent for the requested split—not call a task model. This can use validation/test scores for selection on those splits; it is not evidence of unseen-split generalization (SRC-1, `generate_loop.py`, `select_next_parent.py`, `utils/run_select_next_parent.py`, `ensemble.py`, `utils/run_ensemble.py`; [RT-RTE-optional-consumers](#rt-rte-optional-consumers)).
4. **Different task effect boundaries.** BALROG validates an action string and steps an environment; Genesis extracts generated Python reward code and launches RL training/evaluation subprocesses; Polyglot executes a task agent against `/testbed`, captures its patch, restores test state and runs tests. The initial task agent has no tool grant, so the Polyglot caller's patch-saving contract alone does not make the initial agent a code editor. The inspected Polyglot nonempty-patch path also calls `log_container_output(exec_result, raise_error=False)` although its imported shared function has no such parameter; that path can raise rather than classify the test exit as intended. These observations limit successful-operation claims, not source-native capacities elsewhere (SRC-1, `domains/balrog/evaluator.py`, `domains/genesis/evaluator.py`, `domains/polyglot/harness.py`, `utils/docker_utils.py`, `task_agent.py`; [RT-RTE-domain-effects](#rt-rte-domain-effects)).

Other shipped entries matter to coverage. `domains/run_eval.py` performs independent patch replay and test-subset evaluation, skips an existing output directory, copies results out, and cleans its temporary root; it does not apply generation eligibility checks. `run_task_agent.py` directly loads a task agent and saves a worktree diff. The domain harness itself can directly load a file or module without a container. `no_selfimprove` executes the editor from a copied `DONOTTOUCH` repository while changing the main repository; DGM substitutes `coding_agent.py` and supplies a problem statement from the baseline utilities. DGM still uses the model/tool editor and diff-saving/reset path. External host callbacks, provider-native tool execution and remote worker runtimes are not established by these inspected routes; generated Python/shell code can introduce other paths, whose behavior is not bounded by the initial template's grant list (SRC-1, `generate_loop.py`, `domains/run_eval.py`, `run_task_agent.py`, `domains/harness.py`, `baselines/dgm/coding_agent.py`).

### Guarantees and working-context controls

| Control and owner | Enforcement point and strength | Covered path, alternate paths and required contract | Conclusion statuses |
|---|---|---|---|
| Initial tool grant; call helper | Name lookup and positive call-count check; invariant for dispatch through the unchanged helper | Ordinary initial editor: all shipped tools, default forty calls, one per response. Initial task: empty grant. Tool modules are imported even for empty grants; shell subprocesses, direct Python calls and edited helpers do not inherit this check. Requires ordinary Python/import behavior. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Domain-change exclusion; runner/replay utilities | Post-edit Git reset and replay diff filter; best effort | Reset runs after the editor, not before its effects. Reset helper catches checkout/clean errors. Replay filters diff blocks, but dependencies outside `domains/` remain editable. Polyglot's own replay does not use this filter. Requires Git/patch semantics and intact helper code. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Process duration; generation host | Shell `timeout` plus checked Docker exec status; protocol | Six hours for editor, five hours for normal harness, three hours for normal report; direct scripts lack these outer controls. Bash itself has a 120-second sentinel wait, not a proven process-tree kill. Requires OS timeout and Docker exec behavior. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Cleanup; generation host | `finally` reset/clean/container cleanup; best effort | Normal generation and optional wrappers attempt cleanup; reset failure can itself interrupt subsequent cleanup. Read-write mount means effects have already reached the host's prepared root. Not a transaction or containment proof. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Execution isolation; deployment | Docker/Podman configuration; no claimed guarantee established by this review | Host networking and writable bind mount are explicit, with GPU access conditional on Genesis. Direct harness/runner routes have no shipped enclosing container. Effective security requires external deployment/OS/provider contracts not inspected. | implementation conclusion status: wired; deployment conclusion status: uninspected |

These rows do not assert exercised enforcement. The narrow dispatch control has the following witness:

> tool_uses = tool_uses if multiple_tool_calls else tool_uses[:1]
> --- `agent/llm_withtools.py`

The deployment envelope is materially broader than the tool description's claim that Bash lacks internet access:

> "network_mode": "host",
> "volumes": {
>     os.path.abspath(repo_path): {"bind": f"/{REPO_NAME}", "mode": "rw"}
> },
> --- `utils/docker_utils.py`

SRC-1, `agent/tools/bash.py` describes persistent shell state, but `tool_function_call` constructs a new `BashSession` per call. Filesystem effects can persist; shell variables/cwd are not explicitly carried across sessions. This distinction defeats a stronger cross-call session-state claim.

Context control is not just accumulated history. The initial editor and every initial task call start with `msg_history=[]`; whole task frames are discarded after the returned prediction/history. This resembles selected inputs entering a frame and a return value escaping, but tool filesystem effects and saved logs escape too. The normal archive-copy prune rules preferentially keep training artifacts and remove held-out/current/copy material before tool access. Edit-tool formatting clips long output to its first and last halves with a marker; material is omitted from that result, not deleted from disk, and the tool exposes range views for reloading. The LLM helper otherwise accumulates text turns and tool outputs; its 'output context exceeded' retry requests another response rather than summarizing prior history. No inference about provider-side compaction follows (SRC-1, `meta_agent.py`, `task_agent.py`, `agent/llm_withtools.py`, `agent/llm.py`, `agent/tools/edit.py`, `generate_loop.py`).

## Shared records

### Components

#### RT-CMP-provider-models
Label: Provider inference models

Source-native identity: model strings in `agent/llm.py`, agent instances' `model`, and domain/runner overrides. Representational form: distributed-parametric provider models. Storage substrate: opaque external provider weights; the repository retains names/configuration, not weights. SRC-1, `agent/llm.py`, `agent/base_agent.py`, `domains/paper_review/utils.py`, `run_task_agent.py`.

The ordinary meta runner defaults to `anthropic/claude-sonnet-4-5-20250929`; the paper-review adapter requests `gpt-4o`; Polyglot overrides the editor to Claude 3.5 and its task runner to `o3-mini`. These call sites do not update parameters. Exact provider weight versions are not pinned by hashes: a dated API identifier is not a locally verifiable weight pin. Mutable aliases/endpoints may resolve to another implementation under an external provider contract. Provider routing, training and hidden retained state remain uninspected. Generated code can replace the call policy; that is code mutation, not evidence of weight adaptation.

> response = litellm.completion(**completion_kwargs)
> --- `agent/llm.py`

#### RT-CMP-policy-runner
Label: Genesis trained policy

Source-native identity: Genesis `OnPolicyRunner` and `model_{args.ckpt}.pt`. Representational form: distributed-parametric policy. Storage substrate: local checkpoint files plus in-process runner tensors; dependency algorithm internals are not inspected. Parameters are intended to change during the shipped training call; evaluation loads a chosen checkpoint and requests an inference policy. Exact initial/learned parameter version is not frozen by SRC-1, which contains no run-produced weights. This is a local checkpoint path, not an API endpoint alias; overwriting/reselecting that file can change the loaded model. SRC-1, `domains/genesis/genesis_train/rl_trainer.py`, `domains/genesis/genesis_eval/rl_eval.py`.

> runner.learn(
>     num_learning_iterations=args.max_iterations, init_at_random_ep_len=True
> )
> --- `domains/genesis/genesis_train/rl_trainer.py`

> runner.load(resume_path)
> --- `domains/genesis/genesis_eval/rl_eval.py`

### Operative objects

#### RT-OBJ-model-patch
Label: Agent lineage patch

Source-native identity: `model_patch.diff`, metadata `prev_patch_files` and `curr_patch_files`. Representational form: symbolic Git/unified diff containing executable Python and potentially natural-language literals; downstream consumption differs between Python execution and model interpretation. Storage substrate: generation output directories and reconstructed Git worktrees. This record covers executable replay; specialists can separately establish retained text/evidence parts. `diff_versus_commit` captures tracked changes and untracked files; replay applies ordered patches then commits state. SRC-1, `run_meta_agent.py`, `utils/git_utils.py`, `utils/gl_utils.py`.

> model_patch = diff_versus_commit(args.git_dir, args.base_commit)
> --- `run_meta_agent.py`

#### RT-OBJ-metadata
Label: Generation control metadata

Source-native identity: per-generation `metadata.json` and `archive.jsonl`. Representational form: symbolic JSON flags, identifiers, paths and archive snapshots. Storage substrate: host output directory. Metadata can veto candidate parent eligibility or editable-selector reuse; archive snapshots drive resume and selection. Archive append is not an acceptance of success. SRC-1, `generate_loop.py`, `utils/gl_utils.py`.

> archive.append(new_node)
> --- `utils/gl_utils.py`

#### RT-OBJ-readme
Label: Generated improvement instructions

Source-native identity: root `README.md` produced by `get_readme_description`. Representational form: natural-language instructions. Storage substrate: generated root worktree and inherited lineage; not automatically inserted in the initial model message. It tells an editor to inspect code/evaluations and enhance agent-generation mechanisms; optional text directs ensemble optimization and non-greedy parent selection. Consumption requires a subsequent read by model/tools, which is afforded but not observed. SRC-1, `utils/gl_utils.py`, `meta_agent.py`.

> Given a fixed archive of agents, optimize the performance of the ensemble without modifying the individual agents. The archive of agents is provided in `/tmp/agent_archive/`. You can edit and improve the ensemble logic in `ensemble.py`.
> --- `utils/gl_utils.py`

### Routes

#### RT-RTE-generation-cycle
Label: Host generation cycle

Endpoints/progression: operator CLI → root setup/resume → parent replay → editor → evaluation → metadata/archive append → plotting → next parent; host `generate_loop` owns progression and run/gen IDs. State/effects: writable prepared root, per-generation output directories, Docker jobs and logs. Computation schedules bounded generations over benchmark tasks; the operator chooses domains, limits and baseline, not each code change. See [RT-RTE-editor-admission](#rt-rte-editor-admission), [RT-RTE-task-evaluation](#rt-rte-task-evaluation), [RT-RTE-parent-selection](#rt-rte-parent-selection). SRC-1, `generate_loop.py`, `utils/gl_utils.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Output-directory path after the scheduled generations.
- Later read-back: Resume reads the last archive snapshot and saved root; successive generations replay metadata-listed lineage patches and expose past evaluations.
- Delegated visibility: Editor container receives a reconstructed repository and copied prior artifacts; harness workers receive domain-specific task inputs.
- Selection predicate: Host parent selector or optional inherited selector; staged scores gate fuller evaluation, not archive append.
- Invalidation or expiry: Failed parent-editor execution can mark that parent invalid; no fixed archive expiry in this loop.
- Activation or effect: Executable replay and task invocation are wired; model use of historical evidence and exercised behavioral changes remain unobserved.
- Evidence limits: No supplied run closes the loop or demonstrates recovery/improvement; bootstrap assumes precomputed initial outputs.

> archive = update_and_save_archive(output_dir, archive, new_node=current_genid)
> --- `generate_loop.py`

#### RT-RTE-editor-admission
Label: Model code edit and admission

Endpoints/progression: host launches `run_meta_agent.py` against inherited code → model/tool edit → domain reset → diff save → host nonempty-diff/import checks → evaluation and metadata. Principal proposing changes: provider model operating through Python tool dispatch; host code decides evaluation/eligibility. There is no per-content human approval in this inspected route. Trigger: selected parent plus remaining-generation schedule. Proposed changes include task code, editor code, tool code and optional selectors/ensemble. Admission is not contingent on exceeding parent score. Host exceptions/nonempty-diff/import checks can reject evaluation; replay also rejects failing patch commands via checked exec logging. Recovery uses root reset/clean and preserved lineage; it is best effort, not atomic rollback. SRC-1, `meta_agent.py`, `run_meta_agent.py`, `generate_loop.py`, `utils/gl_utils.py`, `utils/git_utils.py`.

Guidance: initial imperative to modify any code, tool descriptions and potentially the generated README; the initial editor does not directly use its `eval_path` or remaining-iterations arguments. What persists: code diff, chat log, metadata and evaluation artifacts. Operating mode: open-ended code proposal within a finite benchmark-generation budget. Answer oracle: domain evaluation outcomes, not the editor's judgment; no oracle checks the correctness of the generating machinery itself. No formulated criticism trace is supplied, so this route does not assert a theory-builder finding.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Runner saves a diff; `MetaAgent.forward` itself has no explicit result return.
- Later read-back: Saved lineage is replayed into future task/editor containers; previous outputs are copied for possible inspection.
- Delegated visibility: Model can use all loaded tools on the process-visible filesystem/environment; copied history is not guaranteed model-visible content.
- Selection predicate: Diff must be nonempty for normal edited-agent evaluation; imports must succeed; `valid_parent` combines `run_eval` with score existence or non-None meta patches.
- Invalidation or expiry: Exceptions set evaluation false; parent-editor failure can veto parent reuse; root reset/clean attempt restoration.
- Activation or effect: Edited task code is invoked in evaluation; later inherited editor/tool code can execute on replay/import. No observed activation is supplied.
- Evidence limits: Path restoration is not adversarial isolation; editable helper dependencies can undermine intended policies; no successful improvement established.

> instruction = f"Modify any part of the codebase at `{repo_path}`."
> --- `meta_agent.py`

> metadata["valid_parent"] = metadata["run_eval"] and (eval_successful or meta_patch_files is not None)
> --- `generate_loop.py`

#### RT-RTE-model-tools
Label: Textual model tool loop

Endpoints/progression: agent instruction → LiteLLM completion → regex/JSON parsing → registered function dispatch → textual tool output → next completion. Owner: unchanged Python helper controls parsing/dispatch/count; model chooses calls/content. Natural-language descriptions guide decisions, symbolic parsed keys select functions, distributed-parametric inference supplies responses. Initial editor grants all tools; initial task grants none. Dynamic extension: tool-directory Python modules are imported and eligible modules with `tool_info`/`tool_function` are registered; generated file changes can alter the next process's capability surface. No separate remote delegation protocol is implemented in this helper. SRC-1, `agent/llm_withtools.py`, `agent/llm.py`, `agent/tools/__init__.py`, `agent/tools/bash.py`, `agent/tools/edit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accumulated message-history list, not a separate verified tool-success result.
- Later read-back: inapplicable — ordinary history is current invocation state; persistent file/code effects are covered by the edit/replay route.
- Delegated visibility: Each provider call receives accumulated text turns plus tool descriptions/results; Bash inherits process environment and edits use absolute filesystem paths.
- Selection predicate: Valid `<json>` blocks with tool_name/tool_input; first call only by default, registered-name lookup; positive max_tool_calls defaults to forty.
- Invalidation or expiry: Loop stops on no parsed call/count limit; tool errors become text; completion exceptions propagate with limited configured retry classes.
- Activation or effect: Registered function execution can run arbitrary shell commands or edit files; callable grant does not constrain shell-created subprocesses.
- Evidence limits: No provider-native tool route inspected; no demonstrated model compliance with formatting, successful edits, persistence of shell variables or effective network restriction.

> module = importlib.import_module(module_name)
> --- `agent/tools/__init__.py`

> bash_session = BashSession()
> --- `agent/tools/bash.py`

#### RT-RTE-task-evaluation
Label: Tabular task prediction and scoring

Endpoints/progression: edited `TaskAgent` file/module → per-row instance → domain formatter → model response extraction → predictions CSV → label report → host score reader. Owners: harness schedules futures/checkpoints; task code/model proposes answers; report computes scores; host decides fuller evaluation/candidates. Ordinary paper-review oracle: dataset outcome labels, provided by shipped CSV data and omitted by formatter from task input. Reference correctness/provenance is not established by implementation. Operating mode: bounded benchmark evaluation, with staged/full phases. SRC-1, `domains/harness.py`, `task_agent.py`, `domains/report.py`, `domains/paper_review/utils.py`, `generate_loop.py`, `utils/gl_utils.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Prediction and history from task agent; harness returns its output folder; report returns JSON and path.
- Later read-back: Existing non-NA predictions skip repeated work; report scores feed later parent/ensemble decisions and copied evaluation history.
- Delegated visibility: Fresh task instance receives formatted task inputs, not the entire retained archive; current initial task histories do not cross rows.
- Selection predicate: Dataset subset/head sample limit; existing prediction skips; staged scores must all exceed zero to run full evaluation unless skip flag set.
- Invalidation or expiry: Exceptions propagate from futures; missing/unparseable/NaN scores map to None at the host reader; prediction reuse has no inspected code-version invalidation.
- Activation or effect: Answers become CSV cells, then normalized string-match scores; this does not establish evaluator robustness or improved future behavior.
- Evidence limits: Importable arbitrary code can do more than the initial task template; no per-task run evidence or causal comparison supplied.

> inputs = format_input_dict(row)
> prediction, _ = agent.forward(inputs)
> --- `domains/harness.py`

> df["match"] = df[ground_truth_key] == df["prediction"]
> --- `domains/report.py`

#### RT-RTE-parent-selection
Label: Host archive parent selection

Endpoints/progression: archive IDs + metadata + saved domain scores → candidate map → chosen parent ID → next replay. Owner/decision: host `select_parent`; no model decision or per-choice human veto. Starting nodes bypass metadata-validity checks. Per-domain scores use validation if defined, otherwise train; staged results are discounted, and `type='max'` considers agent and ensemble scores. Modes: random/latest/best/score-proportional/score-and-child-count-proportional. CLI defaults to the last. Oracle: previously computed benchmark outcome scores; no expected next-parent answer. Trigger: bootstrap/resume and each generation completion. This chooses exploration lineage, not a proof of improvement. SRC-1, `utils/gl_utils.py`, `generate_loop.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Chosen generation ID.
- Later read-back: Selected generation's patch paths are read to reconstruct the next invocation; selection also reads prior scores and child links.
- Delegated visibility: Next editor receives chosen code lineage, not the selector's whole candidate calculation as model context.
- Selection predicate: Eligible metadata plus complete scores; fallback first archive node when none survive; method-dependent random/score/child weighting.
- Invalidation or expiry: Metadata flags can veto ordinary nodes; missing scores remove candidates except fallback; no automatic expiry horizon.
- Activation or effect: Changes which executable lineage enters the next container; no observed selection benefit.
- Evidence limits: Same score means neither correct generating code nor expected long-term gains; no observed search trajectories.

> if not candidates:
>     # Get the first initial node as the only candidate
>     candidates[archive[0]] = 0.0
> --- `utils/gl_utils.py`

#### RT-RTE-optional-consumers
Label: Inherited selector and ensemble execution

Endpoints/progression: operator enables editable-selection or ensemble mode → host reconstructs selected lineage in a separate container → inherited Python selector/ensemble reads copied archive → stdout/result files return to host. Owner: host wrappers schedule/retry; inherited code decides ID or answer. These are distinct consumers sharing container/replay infrastructure, not a single acceptance gate. Source-native initial selector uniformly samples scored valid candidates; initial ensemble selects best saved domain score for the requested split and returns that agent's saved answer. SRC-1, `generate_loop.py`, `select_next_parent.py`, `utils/run_select_next_parent.py`, `ensemble.py`, `utils/run_ensemble.py`.

Admission account: editor can propose changes to the optional files under README guidance; normal diff/replay admission applies. Host controls whether this capability is exposed. Editable-selector failure disables `can_select_next_parent` for its code-source node and retries; ensemble failure yields None scores. Human contribution is mode selection, not code approval. Selector's task is exploration; ensemble's is bounded evaluation over existing predictions. Oracles are retained scores and report reference labels, not model opinions. Rollback for selector is earlier eligible code lineage; ensemble has no demonstrated semantic rollback. README guidance persists in the generated root, while code and results persist in lineage/output files.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selector's last stdout line becomes parent ID; ensemble wrapper returns scores and copies prediction/report files.
- Later read-back: Full copied archive/scores/answers feed these consumers; their resulting scores can feed later selection.
- Delegated visibility: Separate container receives copied archive including held-out outputs; it is not the pruned ordinary editor view.
- Selection predicate: Selector code-source node is latest can_select_next_parent; default candidate choice uniform among valid scored nodes; ensemble chooses highest score on requested split.
- Invalidation or expiry: Selector exceptions veto code-source node and retry at most the configured bound; ensemble exceptions return missing scores.
- Activation or effect: Inherited code determines next parent or reuses an archived prediction. No fresh task-agent call in the initial ensemble.
- Evidence limits: Changed code can replace defaults; CLI-domain mismatch and stdout parsing limit robustness; no demonstrated held-out generalization or benefit.

> return random.choice(list(candidates.keys()))
> --- `select_next_parent.py`

> match = df.loc[df["question_id"] == question_id, "prediction"]
> --- `ensemble.py`

#### RT-RTE-domain-effects
Label: Environment, reward code and worktree effects

Endpoints/progression: domain dispatcher → specialized task-agent caller → action/environment step, generated reward code/RL subprocess, or Polyglot worktree diff/tests → saved episode/test artifacts → domain report/score reader. Owners: shipped evaluators schedule episodes; task model proposes action/code; environment validation/test/training code determines effects and outcomes. Modes: bounded episodes or per-instance benchmark trials. Oracles: environment progress/reward, robot evaluation metrics, or test exit outcome; external environment/test validity is not established. No per-output human admission appears in the inspected callers. SRC-1, `domains/harness.py`, `domains/balrog/evaluator.py`, `domains/genesis/evaluator.py`, `domains/polyglot/harness.py`, `run_task_agent.py`.

Reward-code admission: generated response is extracted and saved as `reward_function_*.py`; training receives its path. Extraction may reject formatting; subprocess failure/timeout prevents subsequent evaluation. Generated code is not human-approved. RL parameters change in the training invocation and are later loaded from checkpoints, as [RT-CMP-policy-runner](#rt-cmp-policy-runner) records. Guidance includes task description, environment path and default reward-function text; response/code and train/evaluation logs persist. This is task-specific production machinery generation, not proof of the outer editor's success. Polyglot restores a test commit and reapplies solution changes before running tests; error paths save failure artifacts. BALROG validates strings before environment stepping; invalid actions can trigger feedback in later observations.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Environment transition/action outcome, reward-code/training result, or patch/test-result artifacts depending on domain.
- Later read-back: Policy checkpoints load for evaluation; episode/test reports feed host scores and copied historical evidence.
- Delegated visibility: BALROG receives instruction/observation/previous action; Genesis receives task/default code/path; Polyglot receives problem/worktree/test-description/model inputs and explicit API credentials in exec environment.
- Selection predicate: BALROG validity rules choose applied action; Genesis evaluates only after successful training; Polyglot distinguishes empty patch before testing nonempty changes.
- Invalidation or expiry: Episode limits/termination; training subprocess timeout; test-state restore; artifact-specific code/version invalidation remains uninspected.
- Activation or effect: Action is passed to env.step; generated reward path is passed to RL training; Polyglot runs the task agent and tests modified solutions. Successful effects unobserved.
- Evidence limits: Dependency training/provider/environment internals uninspected; Polyglot nonempty-test path has an incompatible logging keyword; no capacity gains or reliable execution demonstrated.

> obs, reward, terminated, truncated, info = env.step(action)
> --- `domains/balrog/evaluator.py`

> if train_log["training_success"]:
>     eval_log = self.run_rl_eval(task, episode_idx, seed, rwd_func_path=rwd_func_path)
> --- `domains/genesis/evaluator.py`

> log_container_output(exec_result, raise_error=False)
> --- `domains/polyglot/harness.py`

### Claims

#### RT-CLM-recursive-improvement
Label: Recursive improvement objective

Claimed operation: retained code/evaluations should guide changes to the framework's own generating mechanisms. Source: generated README doctrine/design, SRC-1, `utils/gl_utils.py`. The implemented replay/edit path supports a dispositional improvement-directed self-change claim over later generations of one host run, within the whole-system boundary. Objective: downstream task performance, specified independently of the proposed code change. Evidence-responsive update determination is requested/afforded, not established for actual model decisions; code replay supplies a live executable authority path but no supplied subsequent execution demonstrates causal dependence. Thus exercised self-improvement and successful improvement remain unestablished, independently of any specialist assessment of learning/reflection/theory-building. Archive membership and score selection alone close neither claim.

> To enable continuous improvement, the system should look at its code repository and the provided path to previously generated agents and their evaluation results, and then edit and enhance its own mechanisms for generating agents.
> --- `utils/gl_utils.py`

#### RT-CLM-bash-description
Label: Bash tool network and session description

Claimed operation: Bash tool description promises no internet and persistent command/discussion state. SRC-1, `agent/tools/bash.py` supplies doctrine/design, while its implementation creates a new session per tool call and container setup uses host networking. Filesystem persistence is plausible under the mount; persistent shell variables or effective network denial are not established. This is a scoped mismatch between description and enforcement, not evidence that a network call occurred.

> * You don't have access to the internet via this tool.
> --- `agent/tools/bash.py`

> * State is persistent across command calls and discussions with the user.
> --- `agent/tools/bash.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-code-replay
Label: Inherited executable code authority

Consumer: future Python imports/editor/task execution and optional selectors/ensemble. Channel: saved diff → host metadata patch list → `patch -p1` → reconstructed worktree → Python execution. Force: executable authority, including import-time effects; not advisory prompt text. Horizon: subsequent generations and resume/replay while lineage files remain available. SRC-1, `utils/gl_utils.py`, `generate_loop.py`, `domains/harness.py`. [RT-OBJ-model-patch](#rt-obj-model-patch) is its retained executable carrier; [RT-RTE-editor-admission](#rt-rte-editor-admission) explains admission limits.

> spec.loader.exec_module(mod)
> --- `domains/harness.py`

#### RT-BAP-selector-flags
Label: Metadata-controlled reuse

Consumer: host parent selection and editable-selector code-source choice. Channel: `metadata.json` reads of `valid_parent`/`can_select_next_parent`. Force: symbolic filtering/veto under source-native special cases and fallback, not unconditional score certification. Horizon: later rounds and resumed runs. SRC-1, `utils/gl_utils.py`, `generate_loop.py`; [RT-OBJ-metadata](#rt-obj-metadata), [RT-RTE-parent-selection](#rt-rte-parent-selection).

> if not valid_parent:
>     continue
> --- `utils/gl_utils.py`

#### RT-BAP-tool-guidance
Label: Model-readable tool and repository guidance

Consumer: provider model through tool-use prompt; potentially editor reading generated README. Channel: tool descriptions prepended to each completion and file contents returned by tools. Force: interpreted instructions, not reliable compliance or network enforcement. Horizon: current tool conversation; README can persist across generations if read. SRC-1, `agent/llm_withtools.py`, `utils/gl_utils.py`, `meta_agent.py`; [RT-OBJ-readme](#rt-obj-readme). Delivery of README or copied historical results is not observed.

> system_msg = f"{get_tooluse_prompt([tool['info'] for tool in all_tools])}\n\n"
> --- `agent/llm_withtools.py`

## Annotations

none
