---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Hyperagents memory: executable lineage, evaluation archives, selective editor access, prediction reuse and Genesis checkpoints."
run-id: AAS-2026-10-14-hyperagents-dd9d501b160c-01
source-identity: https://github.com/facebookresearch/Hyperagents
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
---

# Hyperagents memory report

## Boundary and evidence

The memory boundary follows the shipped improvement plane, its task evaluators and its archive consumers at SRC-1, commit 59a68f672dfb92c74aeb7e61535d776fb36e172d. Included material comprises executable diffs, generation metadata, predictions, reports, chat and episode logs, generated reward code, training configurations and policy checkpoints. The initial model conversations are fresh frames, not conversations resumed from saved Markdown. Those frames still expose durable filesystem effects. Source inspection establishes implementation and declared intent; it supplies neither an observed archive nor a demonstrated performance gain. [The boundary](boundary.md) defines dependencies and exclusions.

Direct inspection added or rechecked the following paths at SRC-1. Supplied runtime findings remain provisional where not directly rechecked. External provider state, external grader/training algorithms and uncaptured experiment logs are not inspectable retained evidence here. Their behavior, initialization provenance and quantitative effects remain unknown; known shipped transformations are described independently.

| Entry or operation | Source path and inspection | Coverage and limit |
|---|---|---|
| Bootstrap and resume | Direct `utils/gl_utils.py` setup/archive readers; supplied `generate_loop.py` resume | [RT-OBJ-metadata](runtime.md#rt-obj-metadata), [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle). Initial outputs are copied; content approval/provenance is not established. |
| Editor, runner and lineage replay | Direct `meta_agent.py`, `generate_loop.py` editor and cleanup blocks; supplied `run_meta_agent.py`, `utils/git_utils.py` replay/diff findings | [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch), [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission). Replayed changes have executable authority, not merely retrieval status. |
| Editor archive delivery, no_archive and only_ensemble | Direct `generate_loop.py` copy/pruning and editor dispatch | [MEM-RTE-archive-delivery](#mem-rte-archive-delivery). Filesystem delivery is wired; model inspection of contents is only afforded. |
| Tool dispatch, viewing, editing and undo | Direct `agent/tools/__init__.py`, `agent/llm_withtools.py`, bounded `agent/tools/edit.py`; supplied Bash details | [RT-RTE-model-tools](runtime.md#rt-rte-model-tools) annotation. Edit undo is process-local; disk effects can cross invocations. Generated tools can change the surface. |
| Per-task frames and raw logs | Direct `task_agent.py`, `agent/base_agent.py`, `domains/harness.py` | [MEM-OBJ-chat-history](#mem-obj-chat-history), [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation). No saved-history replay in these initial agents. |
| Tabular prediction checkpoints, report, proof-grader input | Direct `domains/harness.py`, `domains/report.py` | [MEM-OBJ-predictions](#mem-obj-predictions), [MEM-OBJ-report](#mem-obj-report), [MEM-RTE-prediction-reuse](#mem-rte-prediction-reuse). External proof grader internals and reference validity remain outside inspected evidence. |
| Parent scoring and invalidation | Direct `utils/gl_utils.py` score and selector functions, `generate_loop.py` cleanup; supplied selector retries | [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection), [RT-BAP-selector-flags](runtime.md#rt-bap-selector-flags). A veto does not erase the archived node. |
| Optional ensemble and editable selector | Direct `ensemble.py`; scoped searches `select_next_parent.py`, `utils/run_ensemble.py`, `utils/run_select_next_parent.py`; supplied wrapper findings | [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers). Full archive access differs from pruned editor access; default ensemble reads saved answers. |
| DGM diagnosis and alternative prompt delivery | Direct `baselines/dgm/utils.py`, editor `baselines/dgm/coding_agent.py`, host dispatch | [MEM-RTE-dgm-diagnosis](#mem-rte-dgm-diagnosis). Trace-to-derived-instruction path exists, but inspected retry call is malformed. |
| BALROG episodes | Direct bounded `domains/balrog/evaluator.py` episode loop and persistence | [MEM-OBJ-episode-log](#mem-obj-episode-log), [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects). Environment-maintained context is supplied to each frame; its complete derivation is not inspected. |
| Genesis reward, rollout training, configurations and evaluation | Direct bounded `domains/genesis/evaluator.py`, `domains/genesis/genesis_train/rl_trainer.py`, `domains/genesis/genesis_eval/rl_eval.py` | [MEM-OBJ-reward-function](#mem-obj-reward-function), [MEM-OBJ-cfgs](#mem-obj-cfgs), [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner). Dependency checkpoint payload and optimizer details remain opaque. |
| Polyglot results and reuse | Direct bounded `domains/polyglot/harness.py` existing-result branch; scoped persistence searches; supplied execution findings | [MEM-OBJ-episode-log](#mem-obj-episode-log), [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects). Existing JSON skips rerun without a version test in that branch. |
| Independent replay evaluation | Direct `domains/run_eval.py` scheduling, result copy and cleanup | [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch), [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects). Existing output directory skips evaluation; this path does not certify generation eligibility. |
| Analysis and transfer consumers | Scoped searches `analysis/plot_progress.py`, `analysis/visualize_archive.py`, `analysis/transfer_utils.py` | Saved-score/archive/lineage reads feed plots and transfer selection. Detailed transfer replay and plotting transformations uninspected; no claim of model consumption or transfer benefit. |
| Opaque provider memory | Supplied `agent/llm.py` inference findings | [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models). API inference and model identifiers do not establish provider-side writes, compaction or weight learning. |

## Core ideas

1. **The strongest retained influence is executable lineage.** The host reconstitutes a parent from ordered patches. Future task/editor imports execute that code. Logs and README guidance instead require model interpretation after a read. The authority difference is established by [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) versus [RT-BAP-tool-guidance](runtime.md#rt-bap-tool-guidance), not by calling both an archive.
2. **Retained results have several consumers.** A report shapes numerical parent eligibility/weighting; a prediction can become the ensemble answer; a chat log can be evidence for optional DGM diagnosis. These are distinct paths, not one general memory query. SRC-1, `utils/gl_utils.py`, `ensemble.py`, `baselines/dgm/utils.py`; records below retain the different parts.
3. **Context selection happens before model access.** Normal archive delivery prunes filesystem copies by name, not meaning. Fresh editor/task frames do not import prior conversations. A foreground model may request a file/range through tools, whose formatted result can be clipped. No archive-wide token budget is enforced by this copy mechanism. [MEM-RTE-archive-delivery](#mem-rte-archive-delivery) and the tool annotation delimit what is selected versus actually received.
4. **Rejection changes access policy, not necessarily retained content.** Failed or nonimproving nodes can remain in archive snapshots. Metadata invalidation can block parent or selector reuse while their reports and traces remain available to other consumers. Starting-node exceptions and fallback defeat a universal successful-evaluation admission claim. SRC-1, `utils/gl_utils.py`, `generate_loop.py`; [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection), [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-predictions
Label: Tabular task predictions

Source-native identity: `predictions.csv`, containing dataset rows and a prediction column. Storage substrate: evaluation output directories, with container-to-host copies. Representational form: symbolic CSV row/key structure; answer and task text are natural-language or task-specific symbolic payloads. Lineage: dataset rows plus `TaskAgent.forward` outputs, periodically and finally saved by the harness. This is distinct from [RT-OBJ-metadata](runtime.md#rt-obj-metadata): it stores answers/input content rather than archive membership or eligibility flags. It is an output part of [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation), not a replacement for that route.

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Consumers: the report interprets answers against references; a later harness merges predictions by question ID to skip work; the initial ensemble retrieves one saved answer; proof grading can turn a retained prediction into a `Response` input. Content reuse is not model-weight adaptation. Physical writes are software-controlled, with model authorship of answers; starting the harness does not approve each answer. Bootstrap files have unresolved per-content provenance. SRC-1, `domains/harness.py`, `domains/report.py`, `ensemble.py`.

> dataset = dataset.merge(
>     existing_df[[question_id_col, "prediction"]], on=question_id_col, how="left"
> )
> --- `domains/harness.py`

> dataset["Response"] = dataset["prediction"].copy()
> --- `domains/harness.py`

#### MEM-OBJ-report
Label: Saved evaluation report

Source-native identity: domain evaluation `report.json`, including `overall_accuracy`, counts and passed/failed question IDs in the tabular report. Storage substrate: generation/evaluation output directories. Representational form: symbolic JSON aggregates and identifiers; not the raw answer or explanation of a change. Lineage: normalized predictions matched against dataset references, then aggregated; domain-specific alternatives derive summaries from environment/training/test outcomes. The host may normalize or discount scores again. Distinct from [RT-OBJ-metadata](runtime.md#rt-obj-metadata), which controls access rather than storing the evaluation outcome. Closest supplied route is [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation); this object also covers report consumers of the specialized domains in [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects), so no single containment relation is asserted.

Consumers: host and editable parent selection, default ensemble, optional DGM diagnosis and analysis scripts. Software admits report writes from computed outcomes without per-report human approval. Reports support bounded outcome comparison, not independent certification of edited evaluator dependencies or successful machinery improvement. SRC-1, `domains/report.py`, `utils/gl_utils.py`, `ensemble.py`, `baselines/dgm/utils.py`; specialized-domain report production is supplied by [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects).

> df["match"] = df[ground_truth_key] == df["prediction"]
> --- `domains/report.py`

> per_domain_scores.append(score)
> --- `utils/gl_utils.py`

#### MEM-OBJ-chat-history
Label: Saved chat history

Source-native identity: `meta_agent_chat_history.md`, per-task `chat_history_{question_id}.md`, and specialized task chat logs. Storage substrate: log files in editor/evaluation output directories. Representational form: textual logged inputs, model outputs and tool results; prose payload plus serialized calls. These are raw interaction traces, not a curated summary or a provider-internal reasoning record. Logger writes are automatic; the model authors responses, not log admission. `AgentSystem` clears its selected log on construction. Distinct from [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch): evidence of the interaction versus the executable result. The ordinary editor persistence is supplied by [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission).

Later consumers: optional file inspection through archive delivery and a selected failed-entry log read by DGM diagnosis. Initial `MetaAgent` and `TaskAgent` do not deserialize the saved trace as message history. Their output may contain reasons, but code patches have no required causal link to those reasons or automatic rationale consumer. SRC-1, `agent/base_agent.py`, `agent/llm_withtools.py`, `domains/harness.py`, `meta_agent.py`, `task_agent.py`, `baselines/dgm/utils.py`.

> logging(f"Tool output: {repr(tool_msg)}")
> --- `agent/llm_withtools.py`

> with open(chat_history_file, 'w') as f:
>     f.write('')
> --- `agent/base_agent.py`

#### MEM-OBJ-episode-log
Label: Specialized episode and test artifacts

Source-native identity: BALROG per-episode CSV/JSON/images, Genesis train/eval logs and summary JSON, Polyglot per-instance JSON/test output/patch. Storage substrate: specialized evaluation directories. Representational forms are separated by part: symbolic outcomes/counters/IDs and CSV columns; natural-language observations, stdout and model logs; image payloads; executable solution patches. These are a container of evidence and results with different consumers, not a single derived knowledge object. Closest supplied record is [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects); none of its specialized persisted output parts is separately declared there.

Part of: [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

Lineage: environment transitions, subprocess outputs or worktree/test execution. Software writes logs and summaries; action validation and test/train completion gates are not human content approval. Summary/report consumers aggregate outcomes; copied artifacts afford later editor inspection. DGM explicitly reads failed BALROG episode CSV/chat records or Genesis evaluation text. Polyglot reads an existing result JSON to return without execution. Images and detailed test text have no separately demonstrated model read-back in inspected initial code. SRC-1, `domains/balrog/evaluator.py`, `domains/genesis/evaluator.py`, `domains/polyglot/harness.py`, `baselines/dgm/utils.py`.

> csv_writer.writerow(["Step", "Action", "Reasoning", "Observation", "Reward", "Done"])
> --- `domains/balrog/evaluator.py`

> if out_fname.exists():
>     print(f"Skipping existing entry {instance_id}")
>     with open(out_fname) as f:
>         result = json.loads(f.read())
>     return result
> --- `domains/polyglot/harness.py`

#### MEM-OBJ-reward-function
Label: Generated reward function

Source-native identity: `reward_function_{episode_idx:02d}.py`. Storage substrate: Genesis output directory; later provided as a path to training/evaluation. Representational form: symbolic executable Python, distinct from the natural-language model response from which code is extracted. Lineage: task/default reward guidance → task model response → extraction → saved code. It is a material product part of the supplied domain-effects route, not the outer lineage patch or the trained policy.

Part of: [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

Admission: software extraction and save, then subprocess success determines whether evaluation follows. No per-code human approval in this caller. It shapes the training environment/reward computation, while the trained parameters shape later policy actions. Reasons may remain in the raw model log but are not required in code or consumed by the trainer. Invalid extraction/training and timeout paths can prevent evaluation without establishing deletion of the saved code. SRC-1, `domains/genesis/evaluator.py`; [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).

> code_str = self.extract_code_str(response)
> --- `domains/genesis/evaluator.py`

> self.save_reward_function(code_str, rwd_func_path)
> --- `domains/genesis/evaluator.py`

#### MEM-OBJ-cfgs
Label: Saved Genesis configurations

Source-native identity: `cfgs.pkl`. Storage substrate: training log directory. Representational form: symbolic configuration objects encoded with pickle, not a readable summary and not the distributed-parametric checkpoint. Lineage: environment configuration and shipped training configuration saved before `runner.learn`. Admission: automatic software serialization, not a human content gate. Evaluation deserializes the four configurations and passes `train_cfg` to `OnPolicyRunner`; reward configuration is separately supplied by path. Distinct from [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner): its configuration rather than its parameters. It is a retained part of the Genesis training/evaluation route.

Part of: [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

The policy checkpoint's payload remains dependency-controlled and opaque; the saved configuration is evidence of runner setup, not an exact model-version pin. SRC-1, `domains/genesis/genesis_train/rl_trainer.py`, `domains/genesis/genesis_eval/rl_eval.py`.

> env_cfg, obs_cfg, command_cfg, train_cfg = pickle.load(open(config_path, "rb"))
> --- `domains/genesis/genesis_eval/rl_eval.py`

### Routes

#### MEM-RTE-archive-delivery
Label: Prior archive delivery

Part of: [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle)

Endpoints/progression: host starts another generation → copies previous output tree into `/tmp/` → filename pruning → passes resulting path to runner → editor may inspect files through tools. Owner: host copy rules select the filesystem view; foreground model chooses any subsequent reads. Retained input includes prior code diffs, metadata, train reports, logs and predictions. Persistence is the original host output directory; pruning changes the container copy, not that archive. This is a delivery subroute, distinct from the enclosing generation cycle and not a second declaration of editor admission. SRC-1, `generate_loop.py`, `meta_agent.py`.

- implementation conclusion status: wired
- model-consumption conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Copied archive path used as `--evals_folder`.
- Later read-back: Later editor invocations can request surviving past files; the initial instruction does not insert those files or the supplied path as model text.
- Delegated visibility: Container filesystem receives a pruned tree; tool outputs supply requested contents to a provider call, not an unsolicited full archive prompt.
- Selection predicate: Normal copy removes current generation, val/test-named directories/files, repository-named directories and bytecode. no_archive copies only the parent without this pruning; only_ensemble additionally copies a fixed archive under agent_archive.
- Invalidation or expiry: Removed container-copy parts remain in the host archive; no semantic certification, retention horizon or archive-wide token quota is implemented by these rules.
- Activation or effect: Tools can expose selected historical evidence; actual use to determine a code update is unobserved.
- Evidence limits: Filename filters do not establish held-out secrecy for every payload. Filesystem visibility, tool delivery and model compliance are separate.

> # Copy the whole tree into the container in one go
> copy_to_container(
>     container, source_path=prev_eval_path, dest_path=container_prev_eval_path
> )
> --- `generate_loop.py`

The fresh instruction and ignored `eval_path` are witnessed by [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission). Optional selector/ensemble delivery is different: [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers) receives the full copied archive rather than this ordinary pruned editor view.

#### MEM-RTE-prediction-reuse
Label: Retained prediction reuse

Part of: [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Endpoints/progression: direct/resumed harness invocation → existing predictions read → merge by question ID → skip completed rows → persist combined CSV. Owner: harness software, with no new model proposal or human per-answer decision for reused rows. Context/state effect: previous answers replace computation; the current task agent's code may have changed without an inspected cache-version test. This subroute differs from the enclosing prediction/scoring loop by its no-new-task-call branch. SRC-1, `domains/harness.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Harness output folder containing reused and newly generated predictions.
- Later read-back: The reused CSV reaches the report and possibly ensemble or proof-grader consumers.
- Delegated visibility: Reused rows do not enter a fresh task frame; retained answers instead pass directly into combined output.
- Selection predicate: Existing non-NA prediction or completed question ID; dataset subset/head limit and keyed merge bound reused rows.
- Invalidation or expiry: No code/model hash condition in the inspected skip branch; output replacement/deletion is possible outside this branch, not an automatic semantic invalidation policy.
- Activation or effect: A retained answer suppresses a later agent call and can affect scores. Operation and accuracy of reused content are unobserved.
- Evidence limits: Reuse is not a derived behavior rule or evidence of learning; incorrect/stale retained answers can be reused.

> if (
>     pd.notna(row["prediction"]) or row[question_id_col] in completed_ids
> ):  # pyright: ignore
>     continue
> --- `domains/harness.py`

#### MEM-RTE-dgm-diagnosis
Label: DGM trace diagnosis

Endpoints/progression: optional baseline selected → host chooses domain/failed entry from parent's saved results → formats current code plus report, task and log → model diagnosis → JSON extraction → implementation/problem text → coding-agent invocation → diff-saving route. Owner: host selects evidence; provider model proposes plan and code; host software parses/adopts the generated instruction. No per-proposal human approval. This is an alternative input-production route for [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission), not that route's code-admission gate. SRC-1, `baselines/dgm/utils.py`, `baselines/dgm/coding_agent.py`, `generate_loop.py`.

The mode is a bounded failed-case diagnosis followed by an open code-edit request. References are saved benchmark outcomes used to select failures, not an oracle for whether the diagnosis is correct. Guidance requests a general improvement rather than an instance-specific fix. Raw report/task/log origins are mixed: dataset/reference material, model interactions, and environment/subprocess outcomes. The derived implementation instruction carries only selected fields; the full diagnosis is logged. This is trace-fed instruction production with a later editor consumer, not evidence that retained reasons improve future capacity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Repository summary plus implementation_suggestion and problem_description extracted from model JSON.
- Later read-back: The derived statement reaches a new coding-agent model conversation via CLI; resulting diff can enter ordinary lineage replay. Diagnosis prompt/response are logged, but no automatic future reread of their full rationale is established.
- Delegated visibility: Model diagnosis receives parent code and selected failure evidence, not all archive content; editor receives the derived statement. Log/task/report prefixes are capped at 250000/100000/100000 characters respectively; code text has no corresponding cap in this function.
- Selection predicate: Random domain; tabular failure ID or domain-specific nonperfect outcome. Genesis branch reads eval.log; BALROG reads a chosen failed episode CSV/chat pair. Successful/failure provenance of saved input is not independently verified.
- Invalidation or expiry: JSON extraction exceptions attempt bounded retries, but the inspected recursive call omits root_dir and misaligns required arguments. A faithful success/recovery guarantee is therefore prevented.
- Activation or effect: Derived plan is inserted into the coding agent's instruction; actual evidence-shaped revision and benefit remain unobserved. Ordinary diff/import/evaluation gates apply to the code result.
- Evidence limits: Diagnosis labels do not establish content-directed criticism of a formulated theory. Extraction preserves two actionable text fields but does not require preserving challenged claim, blame or rationale in code. The report makes no theory-builder or successful-learning determination from this route.

> md_log = md_log[:250000]
> task_info = repr(task_info)[:100000]
> report = repr(report)[:100000]
> --- `baselines/dgm/utils.py`

> implementation_suggestion=response_json["implementation_suggestion"],
> problem_description=response_json["problem_description"],
> --- `baselines/dgm/utils.py`

> return get_problem_statement(output_dir, gen_id, domains, max_attempts=max_attempts-1)
> --- `baselines/dgm/utils.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-model-patch](runtime.md#rt-obj-model-patch)

Memory consumers split between future Python execution and possible text inspection. Ordered metadata paths reconstruct the executable lineage; they are access/lineage metadata, not the source code itself. Raw chat logs are a separate retained carrier of possible reasons. No required patch-to-reason linkage or rationale reread is established by supplied replay/diff evidence. Runtime's minimum passages and [RT-BAP-code-replay](runtime.md#rt-bap-code-replay) supply the executable consumer; optional model inspection is bounded by [MEM-RTE-archive-delivery](#mem-rte-archive-delivery). Physical host cleanup can discard worktree edits after saving a patch without withdrawing that saved lineage.

#### On [RT-OBJ-metadata](runtime.md#rt-obj-metadata)

Lineage: host updates per-generation flags/paths, appends archive snapshots containing current generation and full ID list, then later readers load the last snapshot. It is access/control metadata rather than archived answer content. Writes and invalidation are software-controlled; caller/operator choice of a run is not per-node approval. Original bootstrap report approval is unknown independently of later updates. SRC-1, `utils/gl_utils.py`, `generate_loop.py`.

> metadata.update(data_update)
> --- `utils/gl_utils.py`

Archive membership and permission differ: [RT-BAP-selector-flags](runtime.md#rt-bap-selector-flags) supplies the veto path. Initial nodes bypass the ordinary validity check, and candidate exhaustion falls back to the first archive node. Numeric score processing discounts staged evaluations and can choose max(agent, ensemble), so later consumers do not necessarily receive raw report scores unchanged. SRC-1, `utils/gl_utils.py`; [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection).

#### On [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner)

The retained numerical result is a dependency-produced local model checkpoint, not its displayed metrics or `cfgs.pkl`. Shipped trainer config requests PPO rollouts and checkpoint intervals; actual optimizer state, initialization and checkpoint payload remain uninspected. Parameters are intended to change in training. Exact learned parameters are not pinned in this source revision; local replacement or checkpoint choice can alter evaluation. The later reader is wired: construct runner from saved config → load model_{ckpt}.pt → get inference policy → call policy on observations and step the environment. This is an alternative retained form alongside generated executable reward code, not weight adaptation of the provider LLM. SRC-1, `domains/genesis/genesis_train/rl_trainer.py`, `domains/genesis/genesis_eval/rl_eval.py`.

> actions = policy(obs)
> obs, rews, dones, infos = env.step(actions, step_count=step_count)
> --- `domains/genesis/genesis_eval/rl_eval.py`

Trace-fed numerical adaptation is wired through the external training runner, but raw-to-weight transformation details and improved capacity attribution are not established here. Evaluation metrics are derived symbolic displays, not readable policy content. Config serialization occurs before learning; subsequent policy read-back requires an actual checkpoint supplied by the dependency. No produced checkpoint is frozen in this run.

#### On [RT-RTE-model-tools](runtime.md#rt-rte-model-tools)

Working-context control: model decides requested absolute file/range; edit tool code formats the result and caps it at 10000 characters, keeping first/last halves. Disk content remains reachable through another range view or Bash. This truncates one output, not prior conversation turns and not the archive on disk. Process-local FileHistory stores prior file content for undo; it is not serialized into cross-process retained memory. Initial tool loading imports modules before checking grants, so an empty callable grant does not establish import-effect isolation. SRC-1, `agent/tools/edit.py`, `agent/tools/__init__.py`.

> return content[:max_length // 2] + "\n<response clipped>\n" + content[-max_length // 2:]
> --- `agent/tools/edit.py`

The supplied runtime tool-loop passages establish the forty-call default and accumulated message delivery. Direct `agent/llm_withtools.py` inspection shows the output-context retry adds an error request; it does not summarize or trim history. This is not evidence about opaque provider-side compaction.

#### On [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Task-frame control: harness supplies selected formatted row, creates a new agent, and discards returned history while retaining prediction and log. Initial TaskAgent starts msg_history empty on every forward call, including successive environment calls. This resembles a selected-input frame popped after its return, but logs, shell/file side effects and arbitrary imported code break a pure return-only boundary. SRC-1, `domains/harness.py`, `task_agent.py`.

> new_msg_history = chat_with_agent(instruction, model=self.model, msg_history=[], logging=self.log)
> --- `task_agent.py`

#### On [RT-RTE-domain-effects](runtime.md#rt-rte-domain-effects)

BALROG passes environment observation context and previous response to each fresh initial TaskAgent frame. Invalid-action feedback may be prefixed into the next observation's long_term_context; the label alone establishes neither an agent memory store nor complete history. Raw episode CSV Reasoning is set to an empty string in the inspected loop. Genesis retains generated code, configs, checkpoints and outcome displays separately. Polyglot result JSON reuse suppresses execution; independent `domains/run_eval.py` skips an entire existing output directory, even though directory existence alone is not a success/version check. SRC-1, `domains/balrog/evaluator.py`, `domains/genesis/evaluator.py`, `domains/polyglot/harness.py`, `domains/run_eval.py`.

> response_str, _ = agent.forward(inputs)
> action = env.check_action_validity(response_str)
> reasoning = ""
> --- `domains/balrog/evaluator.py`

## Write side

Bootstrap copies precomputed evaluations and selected repository content under software rules; operator workflow initiation does not establish per-content approval or trustworthy initial reports. Thereafter host/model/software agencies are traceable. The model proposes edits through tools, the runner saves a diff, and host nonempty-diff/import/evaluation conditions govern downstream reuse, not human approval or a requirement to beat the parent. [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission) retains the gates, guidance and limits. Dynamic tool modules, selector and ensemble edits can inherit through the same patch channel; provider weights do not change by that channel.

Raw task/model/environment traces become saved logs and outcomes. Tabular reports transform predictions/reference rows into aggregate scores and failed IDs; host score readers further normalize and discount them. [MEM-OBJ-report](#mem-obj-report) records the derived result. DGM is the explicit trace-to-instruction alternative: selected failure traces → model diagnosis → extracted implementation text → later editor → potentially retained executable patch. Full reasons remain in logs if written; automatic downstream code execution does not reread them. Ordinary archive access only affords such a model transformation. [MEM-RTE-dgm-diagnosis](#mem-rte-dgm-diagnosis) prevents conflating these paths.

Genesis has another trace-fed result: simulated experience reaches an external training runner intended to update numerical policy parameters, and evaluation loads its checkpoint. Dependency internals prevent a complete provenance/optimizer account but do not erase the wired checkpoint consumer. Reward-code generation and saved configuration are separate mechanisms with different forms and checks. [MEM-OBJ-reward-function](#mem-obj-reward-function), [MEM-OBJ-cfgs](#mem-obj-cfgs), [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).

Maintenance and withdrawal are local. Edit-tool undo uses process-local previous file text. Worktree reset/clean and container cleanup attempt restoration after results are saved. Copy pruning removes context only from another container's view. Parent failure writes a veto flag; selector failure disables that code-source node and retries. Neither action necessarily deletes patches, predictions, raw traces or archive snapshots. Old predictions, Polyglot results and existing replay directories can bypass new work without inspected version invalidation. SRC-1, `agent/tools/edit.py`, `generate_loop.py`, `utils/gl_utils.py`, `domains/harness.py`, `domains/polyglot/harness.py`, `domains/run_eval.py`; [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers).

## Read-back

- **Executable lineage:** schedule/selected parent → metadata patch list → ordered replay → later Python imports/task/editor code. Consumer force is execution, not advice; saved patches need not contain the reasons for edits. [RT-BAP-code-replay](runtime.md#rt-bap-code-replay).
- **Search control:** generation completion/resume → host or editable selector reads IDs, flags, scores and child links → parent ID → next lineage replay. This automatically selects code, not a historical passage for a model. Permission and staged score transformations apply before consumption; fallback is not a quality certificate. [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection), [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers).
- **Model-readable history:** automatic copy/prune exposes prior artifacts, but foreground model/tool requests choose what text enters the frame. Initial eval_path is not interpolated. Edit view clipping and DGM prefix budgets are distinct from a total model-context budget. [MEM-RTE-archive-delivery](#mem-rte-archive-delivery), [MEM-RTE-dgm-diagnosis](#mem-rte-dgm-diagnosis).
- **Saved answers:** keyed cache reuse suppresses new task calls; ensemble chooses a high-scoring archived node on requested split, then a question-ID row from its CSV. The first selection is performance-based; the second is an identifier lookup. Default ensemble delivery is the answer itself, not a new model prompt. Proof grading instead formats stored answers as new task inputs. SRC-1, `ensemble.py`, `domains/harness.py`, `domains/report.py`; [MEM-RTE-prediction-reuse](#mem-rte-prediction-reuse).
- **Numerical policy:** training writes dependency checkpoints; separate evaluator loads selected model/config and calls inference on observations. Metrics do not substitute for loading parameters. [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).
- **Analysis:** plots read archive snapshots, parent links and scores. Scoped analysis searches establish those readers, but no automatic plot-to-model feedback or benefit is asserted. SRC-1, `analysis/plot_progress.py`, `analysis/visualize_archive.py`, `analysis/transfer_utils.py`.

All cross-invocation consumers above are source-supported routes or explicit affordances. Current conversation accumulation and static tool descriptions are context supply, not trace-derived retained memory. Provider hidden state is uninspected, not absent.

## Integration issues

1. **Additional recovery limit:** [MEM-RTE-dgm-diagnosis](#mem-rte-dgm-diagnosis) exposes a malformed recursive retry call in SRC-1, `baselines/dgm/utils.py`: required root_dir is omitted and positional values shift. This qualifies the supplied runtime's broad DGM-path account in [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission); it does not deny the initial successful diagnosis branch or establish an observed failure.
2. **Container/output parts:** new prediction, episode, reward and configuration objects are declared as material parts of supplied runtime routes. Report and chat-history objects span multiple runtime paths and are distinct from metadata/patch objects. No new record can replace a supplied referent after comparison; no possible duplicate remains. Their separation is consequential because reports, raw traces, executable code and numerical checkpoints have different checks and consumers.
3. **Unresolved provenance and trust:** bootstrap file approval and original evaluation provenance are unknown, while later software transformations are known. External benchmark/reference, proof-grader and training-dependency validity remain uninspected. This prevents an authoritative quality or learning conclusion from [MEM-OBJ-report](#mem-obj-report) or [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).
4. **Unresolved activation:** copied-history inspection, evidence-shaped ordinary editing and successful improvement remain unobserved. The DGM derived statement is explicitly delivered, unlike ordinary history, but no trace authenticates a content-responsive successful revision. [MEM-RTE-archive-delivery](#mem-rte-archive-delivery), [MEM-RTE-dgm-diagnosis](#mem-rte-dgm-diagnosis), [RT-CLM-recursive-improvement](runtime.md#rt-clm-recursive-improvement).
5. **Remaining included detail:** checkpoint payload/optimizer state, full environment-context derivation, specialized report transformations and detailed transfer consumers are not fully inspected. Known outputs/readers remain retained above; these limits prevent complete trace provenance, numerical-policy reconstruction and transfer-benefit claims. [MEM-OBJ-episode-log](#mem-obj-episode-log), [MEM-OBJ-report](#mem-obj-report), [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).

## Limitations and checks

Source HEAD was rechecked as 59a68f672dfb92c74aeb7e61535d776fb36e172d and git status returned no changes. The supplied runtime and boundary identities match this report's run-id/reviewed-boundary. All additional inspections were source text at SRC-1; no target code, tests, examples, providers or services were executed. Mandatory invocation, member types, worker rules, collection and records contract were read completely, recovering bounded continuations. No external source or prior characterization was introduced.

No supplied observed-run or causal-experiment evidence establishes activation, benefits, dependable recovery or adversarial evaluation integrity. Readable logs are not complete private model processing; dependency-controlled checkpoint payloads and provider retention remain unknown. The coverage table retains available but uninspected material instead of asserting absence.

Validation: the required validate-output command passed the member content check. Its complete result states that invocation residue was not checked and that this is not job acceptance or claim support. Deterministic form and quotation checks do not establish analytical correctness.
