---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LHTB memory report: Terminus-2 handoffs, retained evaluation artifacts, post-run analysis and outcome-driven scheduling."
run-id: AAS-2026-10-15-lhtb-a0548ba4edbf-01
source-identity: "https://github.com/zli12321/lhtb"
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
---

# LHTB memory report

## Boundary and evidence

The memory boundary follows LHTB's evaluation workflow, not every independent Harbor application. It includes working-context replacement, same-workspace continuation, opaque provider conversation state, trajectories, hidden checkpoint results, result recovery, post-run interpretation and exposed export/upload consumers. Task-local memory/RAG programs are workloads; their internal stores are not attributed to Harbor. The boundary's task and external-dependency limits remain in force: [boundary](boundary.md#boundary-and-evidence).

All source findings below use SRC-1 at the reviewed commit. Direct inspection added Terminus-2 filtering, skills discovery, reset, summarization, overflow and trajectory writing; Chat and the LiteLLM Responses adapter; trial feedback, cleanup and process checkpoints; CLI dispatch, trace-export controls, sweep selection, analysis/check operations; analysis prompts/backend, viewer endpoints, upload implementation and trace continuation traversal. Runtime findings supply the rest of trial orchestration, agent dispatch, artifact transfer, job recovery and maintenance. These are implementation and, for prompts, doctrine/design evidence. No target execution or provider call was performed. Source inspection establishes wiring, not faithful summaries, actual repair, learning benefit or deployed confidentiality.

| Operation / retained surface | Source paths in SRC-1 | Coverage and conclusion limits |
|---|---|---|
| Terminal observation filtering; proactive and reactive context reduction | `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/llms/chat.py` | Direct reads; [MEM-OBJ-handoff-context](#mem-obj-handoff-context), annotation on [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). |
| Remote response chain | `harbor/src/harbor/llms/lite_llm.py` | Direct adapter read; annotation on [RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model). Service retention/deletion and internal representation remain opaque. |
| Skills/MCP and terminal actions | `harbor/src/harbor/agents/terminus_2/terminus_2.py` | Direct skills/initial-prompt reads plus [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions). Metadata discovery is automatic; full skill body consumption is model-selected shell access, not guaranteed loading. |
| Restarted versus resumed continuation, diagnostic and binary rejection | `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/agents/terminus_2/terminus_2.py` | Direct feedback/reset/resume reads plus [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation). No cross-trial solver-memory import established. |
| Workspace, separate verifier artifact transfer and final collection | `harbor/src/harbor/trial/trial.py` | Supplied [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions), [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution), [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution); collection internals not exhaustively inspected. Transfer warnings prevent guaranteed-complete-snapshot claims. |
| Hidden timed/final checkpoint storage and cleanup | `harbor/src/harbor/trial/trial.py` | Direct reads; [MEM-OBJ-process-reward](#mem-obj-process-reward), [MEM-RTE-checkpoint-retention](#mem-rte-checkpoint-retention). Source hiding is not deployment assurance. |
| Trajectory alternatives and later viewer/export reads | `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/viewer/server.py`, `harbor/src/harbor/cli/traces.py`, `harbor/src/harbor/utils/traces_utils.py` | Direct reads/searches; [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-RTE-artifact-access](#mem-rte-artifact-access). Complete per-format normalization and multimodal handling not audited; no downstream training consumer established. |
| Completed-result reload and outcome-driven sweeps | `harbor/src/harbor/job.py`, `harbor/src/harbor/cli/sweeps.py` | Supplied [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery); direct sweep selection read, [MEM-RTE-sweep-selection](#mem-rte-sweep-selection). Singular reward-key compatibility is unresolved. |
| Trial/job analysis, cached summaries, viewer analysis requests | `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/analyze/analyzer.py`, `harbor/src/harbor/analyze/backend.py`, `harbor/src/harbor/analyze/prompts/analyze.txt`, `harbor/src/harbor/viewer/server.py` | Direct reads/searches; [MEM-RTE-trial-analysis](#mem-rte-trial-analysis), [MEM-OBJ-analysis](#mem-obj-analysis), [MEM-CMP-analysis-model](#mem-cmp-analysis-model). This is a separate model-dependent read-back route, not foreground solver continuation. |
| Task quality check | `harbor/src/harbor/analyze/checker.py` | Direct read. Static task files and rubric enter a separate read-tools model call; source does not wire its output back into task editing. Not itself trace-derived solver memory. |
| Upload CLI and streaming hook | `harbor/src/harbor/cli/upload.py`, `harbor/src/harbor/cli/jobs.py`, `harbor/src/harbor/upload/uploader.py` | Direct searches and upload-method read; [MEM-RTE-artifact-access](#mem-rte-artifact-access). Remote database/storage internals, actual sharing and deletion uninspected. |
| Alternate agents, host imports, installed-runtime replacement | `harbor/src/harbor/agents/factory.py`, `harbor/src/harbor/agents/installed/codex.py`, `harbor/skills/apply-lhtb-patches/PATCH.md`, `harbor/patches/single_step.py.harbor-0.20.0` | Supplied [RT-RTE-agent-dispatch](runtime.md#rt-rte-agent-dispatch), [RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching). Alternative agent/CLI context stores and actual installed replacement remain uninspected, not absent. |
| Published result figures | `assets/make_figures_2.0.py` | Direct search plus boundary findings: separate CSV inputs for final reward and reward-over-time. No inspected end-to-end derivation from checkpoint JSONL to published CSV; no causal benefit inference. |
| Task-specific knowledge, task generations, images and external providers | `tasks/`, `tasks-2.0/` | Included as evaluation inputs/products through supplied runtime records, not a uniform memory implementation. Per-task curation, embedding lineage and opaque image internals uninspected; no all-task memory characterization. |

CLI dispatch was checked for material alternatives rather than treating Terminus-2 as the only consumer. Source searches of the Terminus-2/Chat paths for hooks and tool registration did not reveal a separate memory-tool registry there; this is not a repository-wide absence finding. The concrete analysis backend exposes Read/Glob/Grep; the foreground agent instead has terminal access. Streaming upload is a host-side trial-end hook, not a solver memory retrieval tool. SRC-1, `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/cli/jobs.py`, `harbor/src/harbor/analyze/backend.py`.

## Core ideas

1. **Derived handoff text, not a transparent archive.** Three model calls transform the conversation into summary, questions and answers. The next foreground call receives those by value after history replacement. Old trajectory files are audit artifacts, not automatically dereferenced memory. [MEM-OBJ-handoff-context](#mem-obj-handoff-context), [MEM-OBJ-trajectory](#mem-obj-trajectory).
2. **Workspace persistence and conversational persistence differ.** Restarted Terminus-2 phases make a new Chat while retaining the environment. Same-conversation resume preserves Chat and tmux. A failed grader decision changes what happens next but does not roll back unsuccessful workspace edits. [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation), [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions).
3. **Evaluation evidence has several consumers with different authority.** Rewards can control continuation or task scheduling; trajectories and verifier output can later guide an analysis model; cached analysis guides aggregation and human display. None of these automatically gives prior trials to the task-solving model. [MEM-RTE-checkpoint-retention](#mem-rte-checkpoint-retention), [MEM-RTE-sweep-selection](#mem-rte-sweep-selection), [MEM-RTE-trial-analysis](#mem-rte-trial-analysis).
4. **Admission is automatic at the content boundary.** Handoff text and schema-valid analysis are installed without a per-content human gate. Requests for comprehensive or evidence-based interpretation are guidance, not semantic validation. Provider/model opacity and schema checks cannot establish correctness. [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff), [MEM-RTE-trial-analysis](#mem-rte-trial-analysis).

## Shared records

### Components

#### MEM-CMP-analysis-model
Label: Analysis backend model

The source-native model is the configured `model` passed through `normalize_model_name` to Claude Agent SDK. It is distinct from [RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model): another call stack, provider interface and read-only analysis role, not the terminal solver's `_llm`. Its operative form is distributed-parametric, behind the service. Exact weights/version are not pinned; configuration aliases can resolve to another model. These paths contain calls, not parameter updates; provider-side changes, storage and internal reasoning remain uninspected. The SDK conversation is also external state whose compaction/lifetime is not established by this wrapper. SRC-1, `harbor/src/harbor/analyze/backend.py`.

> options = ClaudeAgentOptions(
>         permission_mode="bypassPermissions",
>         allowed_tools=tools,
>         cwd=cwd,
>         model=normalize_model_name(model),
>         add_dirs=list(add_dirs) if add_dirs else [],
>     )
> --- `harbor/src/harbor/analyze/backend.py`

### Operative objects

#### MEM-OBJ-handoff-context
Label: Summary, questions and answers handoff context

Natural-language content in the foreground Chat's process-memory list, submitted to the remote model and also represented in logs. Lineage is task text, prior model turns, terminal observations and current screen, transformed by the same model component as the solver. It is not a separate learned parameter store or independently validated knowledge base. This object is distinct from the static task instruction [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction): it is derived through use and replaces accumulated context. Its producing route is [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).

Summary generation sees remaining history and a request for major actions, findings, problems/resolutions and current status. Question generation sees only task, summary and screen, with an empty message history; answer generation sees remaining history plus the summary exchange and questions. The resulting foreground history keeps its first message, question prompt (including summary/screen) and generated questions; generated answers arrive as the next user prompt. Thus the reasons for earlier decisions may survive if the model includes them, but no exact rationale retention is enforced. Later solver calls interpret this content as guidance; semantic compliance and benefit are unobserved. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

> questions_response, questions_trajectory_ref = await self._run_subagent(
>             prompt=question_prompt,
>             message_history=[],
>             steps=questions_steps,
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> answers_message_history = chat.messages + [
>             {"role": "user", "content": summary_prompt},
>             {"role": "assistant", "content": summary_response.content},
>         ]
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

The history replacement passage is retained by [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). The reset severs use of the old response identifier, not proven service-side deletion.

#### MEM-OBJ-trajectory
Label: ATIF trajectory and continuation files

Symbolic JSON structure on host disk carries natural-language observations, model content and optional reasoning, alongside symbolic commands, metrics and file/session references. These parts have different consumers: inspection/analysis interprets text; export traversal follows filename fields. Subagent `extra.summary` is a human-readable event label, not the generated summary payload. The actual subagent turns live in their own trajectory file. This object has no identical supplied counterpart: [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result) stores outcomes/configuration, not the trajectory; [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) names the producing transformation.

The source dumps trajectory after episodes and in run/resume finalization. Default non-linear history retains a combined event sequence; linear-history mode splits continuation files and records `continued_trajectory_ref`. Subagent files retain copied context plus their own exchange; save errors are logged while a reference is still returned. Episode prompt/response files and optional `all_messages` metadata provide further displays, not authenticated full conversation checkpoints. `all_messages` copies the current Chat after reductions, not necessarily all historical messages. Raw-response versus parsed-trajectory options also change what is displayed. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

> if self._store_all_messages:
>             metadata["all_messages"] = copy.deepcopy(self._chat.messages)
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> return SubagentTrajectoryRef(
>             session_id=session_id,
>             trajectory_path=str(trajectory_path.name),
>             extra={"summary": summary_text},
>         )
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

Later consumers are viewer file responses, trace export and the afforded file reads of the analysis model. These uses do not restore foreground Chat automatically. See [MEM-RTE-artifact-access](#mem-rte-artifact-access) and [MEM-RTE-trial-analysis](#mem-rte-trial-analysis).

#### MEM-OBJ-process-reward
Label: Hidden process-reward records and snapshots

Symbolic JSONL/JSON on host disk stores checkpoint timing, task/trial identity, reward values, CTRF summary/source, error and artifact paths. Timed checkpoint directories additionally copy verifier artifacts and, when present, `agent/trajectory.json`. A final checkpoint writes a final record using the final verifier directory; it is not the same snapshot procedure as a timed checkpoint. The records are derived evaluation metadata, not model-authored task knowledge. Raw verifier/trajectory snapshots remain separate evidence. This object is distinct from but partly copied into agent-result metadata within [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result); it is not wholly contained there because external snapshot files and JSONL exist separately. SRC-1, `harbor/src/harbor/trial/trial.py`.

> # Keep hidden checkpoint scores outside /logs/{agent,verifier,artifacts},
>         # all of which may be visible inside the live sandbox.
>         log_path = self.trial_dir / "process_reward.jsonl"
> --- `harbor/src/harbor/trial/trial.py`

> trajectory_path = self._trial_paths.agent_dir / "trajectory.json"
>         if trajectory_path.is_file():
>             shutil.copy2(trajectory_path, checkpoint_dir / "trajectory.json")
> --- `harbor/src/harbor/trial/trial.py`

Paths are access metadata, not the referenced payload. No source passage here establishes that a copied primary trajectory includes every continuation/subagent file. The hidden scores are not delivered in the checkpoint continuation turn; [MEM-RTE-checkpoint-retention](#mem-rte-checkpoint-retention) separates code control from model visibility.

#### MEM-OBJ-analysis
Label: Trial and job analysis files

Natural-language trial summary and check explanations live inside symbolic schema-constrained `analysis.json`, with `analysis.md` as a textual rendering. Job analysis retains trial results and an aggregated narrative. These host-disk artifacts derive from model interpretation of trial/task evidence, then model aggregation of trial summary/check text. They are distinct from the outcome in [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result); neither schema validation nor a check's pass/fail label certifies correctness. SRC-1, `harbor/src/harbor/analyze/analyzer.py`, `harbor/src/harbor/analyze/prompts/analyze.txt`.

> trial_dir.joinpath("analysis.json").write_text(
>             result.model_dump_json(indent=2), encoding="utf-8"
>         )
> --- `harbor/src/harbor/analyze/analyzer.py`

Later consumers are cached analysis invocations, job aggregation, viewer display and operators. No inspected route delivers these files into the task solver's next trial. Reasons can persist in check explanations and reach aggregation; the aggregate receives those rendered checks and summaries, not the complete raw trajectory. See [MEM-RTE-trial-analysis](#mem-rte-trial-analysis).

### Routes

#### MEM-RTE-checkpoint-retention
Label: Hidden checkpoint retention

Part of: [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation)

This is the storage/visibility branch of [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation), distinct from its full continuation controller. Trial code runs interim grading, copies evidence, appends the hidden record and then hides shared grader artifacts. It uses the live verifier result to stop on pass or resume with a result-free progress message. SRC-1, `harbor/src/harbor/trial/trial.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: VerifierResult or recorded error; host checkpoint JSON and JSONL persisted.
- Later read-back: Copied record enters saved agent-result metadata; checkpoint files remain for later inspection. A deployed reader of the JSONL or checkpoint snapshot is uninspected; the continuation controller consumes the live verifier return, not a demonstrated reload of that file.
- Delegated visibility: Timed checkpoint continuation receives elapsed/remaining active time and snapshot notice, not scores or grader details through that prompt.
- Selection predicate: Configured process-reward tracker and checkpoint due; timed snapshot copies current verifier directory and primary trajectory when present; final recording requires final verifier timing/result.
- Invalidation or expiry: Existing timed checkpoint directory is removed before replacement; visible verifier artifacts are scrubbed/reset subject to mode/provider. Host checkpoint records persist independently.
- Activation or effect: Code records outcomes and can continue or stop work; actual writing, confidentiality and behavioral effects unobserved.
- Evidence limits: External sandbox isolation is not inspected; exported/published reward-over-time lineage and a later JSONL reader are not established.

Admission is automatic software recording, with task tests supplying the answer oracle and runtime code deciding continuation. No per-record human approval or semantic review is wired. Failed verification does not withdraw workspace edits. These records are evaluation retention, not by themselves a trace-fed update to future solver knowledge.

> (checkpoint_dir / "checkpoint.json").write_text(
>             json.dumps(record, indent=2, ensure_ascii=False) + "\n"
>         )
> --- `harbor/src/harbor/trial/trial.py`

> "terminal state. A periodic progress snapshot was recorded, but no grading "
>         "result or hidden-test information is available. Inspect your own work and "
> --- `harbor/src/harbor/trial/trial.py`

#### MEM-RTE-trial-analysis
Label: Retained trial analysis and aggregation

CLI `analyze`, or a viewer analysis request, selects trial/job directories. Analyzer supplies task paths and guidance to [MEM-CMP-analysis-model](#mem-cmp-analysis-model), exposing Read/Glob/Grep. The model is asked to inspect outcome, trajectory and verifier evidence, evaluate criteria and retain explanations. Pydantic validates returned structure before [MEM-OBJ-analysis](#mem-obj-analysis) is written. This is a new route beyond [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery): it interprets traces rather than merely reconciling completed configurations. SRC-1, `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/analyze/analyzer.py`, `harbor/src/harbor/analyze/backend.py`, `harbor/src/harbor/analyze/prompts/analyze.txt`, `harbor/src/harbor/viewer/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured trial analysis or error; job aggregation returns narrative plus trial analyses and reports failed analyses separately.
- Later read-back: Existing analysis.json is reused unless overwrite is requested. Job aggregation receives each trial's summary and rendered check explanations, including cached results. Viewer endpoints read saved analysis for operators.
- Delegated visibility: Analysis call can read the trial directory and task directory when available; absent task path changes guidance to infer requirements from trajectory/test output. Aggregate call receives summary/check text and has no file tools.
- Selection predicate: Caller selects trial/job path, optional passing filter, prompt/rubric/model and overwrite; the analysis model selects individual file reads. There is no inspected token-budget selection policy in this wrapper; structured calls set max_thinking_tokens to 10000.
- Invalidation or expiry: Cached trial file is accepted by existence plus schema parsing unless overwrite. Job cache is reused when all trials were cached and a job cache exists. No evidence-sensitive freshness invalidation is established by these checks.
- Activation or effect: Source wires trace interpretation to persisted analysis and later aggregation/display; whether the model actually reads all relevant evidence or produces correct judgments is unobserved.
- Evidence limits: SDK context management and exact model identity are opaque; no inspected execution or downstream solver adoption establishes capacity improvement.

Authorship is computational; admission is automatic after schema validation, not human approval or an answer oracle. Criteria shape the proposal; a prompt requesting evidence is not a truth gate. Invalid structure raises an error rather than installing that result. Overwrite permits replacement; no automatic semantic rollback is wired. The operating mode is bounded post-run evaluation. This is trace-fed natural-language derivation with later model consumption, but its schema labels do not establish claim-directed criticism or improved solving capacity.

> if not overwrite and cached.exists():
>             return AnalyzeResult.model_validate_json(cached.read_text())
> --- `harbor/src/harbor/analyze/analyzer.py`

> Trial files:
> - result.json — trial outcome, reward, exception info
> - agent/trajectory.json — the agent's full action history
> - verifier/test-stdout.txt (if exists) — test output
> - exception.txt (if exists) — failure details
> --- `harbor/src/harbor/analyze/prompts/analyze.txt`

> f"  Summary: {r.summary}\n"
>                 f"  Checks:\n{r.format_checks_text()}"
> --- `harbor/src/harbor/analyze/analyzer.py`

The prompt's “full action history” label is qualified by trajectory segmentation, representation options and omitted material. It requests a read, not proof of complete evidence access.

#### MEM-RTE-sweep-selection
Label: Outcome-driven sweep selection

The hidden `sweeps run` path repeats jobs and reads their saved results to remove successful tasks from subsequent sweeps. This differs from configuration-matching recovery in [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery). SRC-1, `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/cli/sweeps.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated remaining_tasks list and sweep progress; optional export follows the jobs.
- Later read-back: Prior trial result files affect the next sweep's job task list, not its model's conversation.
- Delegated visibility: Scheduler reads result metadata; optional caller-provided per-task hints enter agent kwargs, but this path does not derive those hints from traces.
- Selection predicate: Parsed verifier_result.reward exists and converts to float greater than zero; task identity comes from task configuration in hinted mode or result/name in ordinary mode.
- Invalidation or expiry: A task with any qualifying success is removed for remaining sweeps; the loop stops if no tasks remain or the sweep count ends.
- Activation or effect: Code submits jobs on remaining tasks; whether current result schemas satisfy the singular reward key is unresolved, so task-dropping effectiveness is not established.
- Evidence limits: No observed sweep and no schema-compatibility audit; do not conflate this greater-than-zero predicate with continuation's full-pass threshold.

Software supplies proposal and decision under the caller's bounded sweep settings; tests/results provide the success proxy. There is no per-task human admission gate. Parse/read/cast errors are reported and leave success unrecognized; rerunning with corrected data/config is the available external recovery. What persists is outcome data, not revised solver knowledge. The reference outcome is task verification, but the sweep's scalar field and threshold are its own policy.

> vr = obj.get("verifier_result")
>                             reward = vr.get("reward") if isinstance(vr, dict) else None
>                             if reward is not None and float(reward) > 0.0:
>                                 succeeded_by_task.add(task_name)
>                                 break
> --- `harbor/src/harbor/cli/sweeps.py`

#### MEM-RTE-artifact-access
Label: Retained artifact access and export

Viewer, traces export and upload are separate access operations over the same retained files, not new solver-context restore APIs. Viewer returns selected trial/step JSON or verifier output; exporter traverses continuation filenames and selects episodes; uploader packages trial material and a direct primary trajectory object. The common admission is caller/configured software access, not content revision approval. No supplied route describes these consumers in detail; closest is persistence in [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution). SRC-1, `harbor/src/harbor/viewer/server.py`, `harbor/src/harbor/cli/traces.py`, `harbor/src/harbor/utils/traces_utils.py`, `harbor/src/harbor/upload/uploader.py`, `harbor/src/harbor/cli/jobs.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Viewer JSON/text; exporter dataset rows/counts; uploader remote archive/trajectory paths and outcome metadata.
- Later read-back: Explicit file reads serve operator display/export; uploader provides remote persistence/access paths. Training or a solver's subsequent import is uninspected, not implied by dataset formatting.
- Delegated visibility: Viewer selects a trial and optional step; export can include subagents and opt-in instruction/verifier metadata; upload has separate remote storage and sharing controls whose deployed permissions remain uninspected.
- Selection predicate: Caller path, trial/step and export options; export main traversal follows continued_trajectory_ref, with all/last episode selection. Upload skips an already-uploaded trial ID; run streaming hook can initiate upload at trial end without a later user request.
- Invalidation or expiry: Missing files or malformed JSON yield consumer-specific failure/empty results. Missing continuation target stops traversal. Remote deletion/retention and all normalization behavior are uninspected.
- Activation or effect: Code delivers or copies retained material; no evidence shows later task behavior or parameter updates depending on exports/uploads.
- Evidence limits: Viewer primary-trajectory response is not evidence it recursively loads every continuation. Full exported-row fidelity, remote platform consumers and execution are uninspected.

> trajectory_path = root / "agent" / "trajectory.json"
>         if not trajectory_path.exists():
>             return None
> --- `harbor/src/harbor/viewer/server.py`

> # Handle "last" episode filter
>     if episodes == "last":
>         all_conversations = [all_conversations[-1]]
> --- `harbor/src/harbor/utils/traces_utils.py`

> if await self.db.trial_exists(trial_result.id):
>                 return TrialUploadResult(
>                     trial_name=trial_result.trial_name,
>                     task_name=trial_result.task_name,
>                     reward=primary_reward,
>                     skipped=True,
>                 )
> --- `harbor/src/harbor/upload/uploader.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-analysis-guidance
Label: Trial analysis to aggregate guidance

Consumer: the job-analysis model. Channel: prompt interpolation of per-trial summaries and check explanations. Force: natural-language interpretive input, not executable control or a truth oracle. Horizon: a subsequent aggregation invocation, including reuse across analysis commands through cached files. The downstream operator can read the resulting narrative, but acceptance or corrective action is not established. This differs from [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance), whose consumer solves the benchmark. Source passage and lineage are in [MEM-RTE-trial-analysis](#mem-rte-trial-analysis); SRC-1, `harbor/src/harbor/analyze/analyzer.py`.

## Annotations

#### On [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff)

The proactive selector compares estimated free tokens with a configurable threshold (default 8000); its input is current Chat content and model context limit. Terminal filtering independently retains first/last portions under a default 10000-byte content bound, omitting the middle; the marker itself adds bytes. These controls select by size/position, not truth, source reliability or task relevance. Summarization is enabled by default but can be disabled; the threshold alone is not a hard prompt-size guarantee. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

> if free_tokens < self._proactive_summarization_threshold:
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

Reactive overflow preferentially removes the most recent pairs until its estimated target free space is met, not the oldest turns. It resets the response chain and then attempts the full three-call handoff. If full summarization fails, the short model fallback sees task plus the last 1000 screen characters; ultimate fallback uses task plus that screen tail without a model transformation. Crucially those latter branches construct a new prompt but do not explicitly install a fresh three-message Chat: they submit through the remaining unwound Chat. Thus they are not necessarily complete history replacement. This qualifies the runtime's compressed “fallback” account without contradicting the successful full-handoff route. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/llms/chat.py`.

> chat._messages = chat.messages[:-2]
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> summary_prompt = f"{original_instruction}\n\nSummary: {short_llm_response.content}"
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> llm_response = await chat.chat(
>                     summary_prompt,
>                     logging_path=logging_path,
>                     **self._llm_call_kwargs,
>                 )
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

The automatic producer/admission chain is raw task/observations/model turns → model summary/questions/answers → replacement context → later foreground invocation. [MEM-OBJ-handoff-context](#mem-obj-handoff-context) retains the lineage. Code owns trigger and installation; the model chooses content; no per-content human veto or semantic oracle intervenes. Failure handling attempts fallbacks, not recovery of every removed turn. Summary rationale is requested, not guaranteed retained. The isolated question call resembles a separate call frame: selected inputs enter, returned questions escape. Full-history summary/answer calls copy history; foreground keeps text by value. Trajectory references are not heap pointers available for automatic dereference by the solver. Raw history can remain on disk without a designated automatic reload route.

#### On [RT-CMP-terminus-model](runtime.md#rt-cmp-terminus-model)

The response identifier is symbolic access metadata in Chat, not a readable summary of remote state. The Responses adapter sends only the new prompt when this identifier exists; otherwise it builds history plus prompt. Remote chain persistence, internal encoding and deletion remain opaque. Reset means the next request sends the locally selected history; it does not request deletion of the prior provider chain. SRC-1, `harbor/src/harbor/llms/chat.py`, `harbor/src/harbor/llms/lite_llm.py`.

> if previous_response_id is not None:
>                 # Server-side state chaining: only send the new prompt
>                 responses_kwargs["previous_response_id"] = previous_response_id
>                 responses_kwargs["input"] = prompt
> --- `harbor/src/harbor/llms/lite_llm.py`

#### On [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction)

Skill metadata is selected by scanning SKILL.md files under the configured sandbox directory and parsing name/description, then appended as an XML catalog with absolute locations. The body is not automatically injected by that mechanism. A later model-selected terminal read can bring it into observations; this is an afforded retrieval channel, not evidence any body was read. Initialization/approval of those files and MCP endpoints is unresolved; the catalog itself supplies no trust authentication. Static skills are not trace-derived memory merely because they are available. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

> provides the absolute path so the model can ``cat`` the file to activate
>         a skill.
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

#### On [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation)

Restarted `run()` constructs a new Chat, whereas `resume_after_verifier_rejection()` requires the existing Chat/live tmux and re-enters with `reset_context=False`. Both retain the environment's workspace, but only the latter directly retains conversational content. Diagnostic feedback preferentially reads migration_details.json failure text, otherwise truncated JSON, then reward.txt or fixed failure text; same-conversation feedback is fixed binary rejection plus phase/time. These channels differ from hidden score retention and filesystem leakage. SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/trial/trial.py`.

> self._chat = Chat(self._llm, interleaved_thinking=self._interleaved_thinking)
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> if isinstance(failure, str) and failure.strip():
>                 return failure.strip()
>             return json.dumps(data, indent=2)[:4000]
> --- `harbor/src/harbor/trial/trial.py`

## Write side

The main automatic trace-fed behavior-shaping write is context handoff: observed/model interaction material becomes [MEM-OBJ-handoff-context](#mem-obj-handoff-context), then enters the next solver call through [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). The source requests findings, resolutions and status but provides no retained justification guarantee and no semantic acceptance test. Model content is adopted automatically. This establishes a derived-memory route, not faithful compression or improved capacity.

Task-workspace edits have another admission mechanism: parsed model commands take effect without per-edit human approval. Verification can reject stopping but does not undo those changes. Cleanup/environment deletion controls their lifetime; a later phase can inspect/repair them. Source and limits are [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions) and [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation). This is retained work product, not necessarily reusable task knowledge.

Host trajectory/result/checkpoint writes use automatic software admission. They preserve raw or structured evidence separately from model-derived content. [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-RTE-checkpoint-retention](#mem-rte-checkpoint-retention), [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result). Trial analysis adds a second trace-fed transformation: a model proposes explanations, schema validation admits them to files, and later aggregation consumes them. A schema rejects malformed output but cannot veto unsupported interpretation. [MEM-RTE-trial-analysis](#mem-rte-trial-analysis).

Maintenance is not uniformly human-curated. Caller identity and prior review of tasks, skills, prompts, hints and configured extensions are not established from their existence. Known subsequent transformations remain automatic despite that initialization uncertainty. Runtime replacement has a separately afforded maintenance actor and future import consumer, not a solver-authorized autonomous update service: [RT-RTE-runtime-patching](runtime.md#rt-rte-runtime-patching).

Withdrawal also differs by surface. Chat reduction removes active context; trajectory files need not be deleted. Shared verifier cleanup removes tests and, for ephemeral-log providers, verifier outputs, but warns on failure; non-ephemeral logs may remain to protect mounted host results. Host checkpoint snapshots are retained separately. Job recovery deletes directories without result files. These are local lifecycle rules, not global forgetting or provider deletion. SRC-1, `harbor/src/harbor/trial/trial.py`; [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery).

## Read-back

- **Automatic within-run supply:** Size-triggered handoff installs selected natural-language context without a foreground retrieval request. Inputs include remaining history, task and screen; the selection is a mixture of code-triggered reduction and model content choice. No fixed output token budget or semantic completeness guarantee is established. [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).
- **Model-requested access:** Terminal reads can select task/workspace/skill files. A filename identifies a requested resource; it is not evidence of semantic search. No dedicated embedding retrieval route is established for the harness from those accesses. [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions), annotation on [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction).
- **Code read-back:** Job recovery reads saved outcomes/configs; sweeps use result values for task selection. Their behavioral authority is scheduling, not model instruction or learned parameters. [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery), [MEM-RTE-sweep-selection](#mem-rte-sweep-selection).
- **Later model read-back:** Post-run analysis requests file inspection; cache reload can supply prior analysis to aggregation. Aggregation selects summary/check fields, not full raw evidence. This supports a separate retained interpretation chain, not proof the requested file reads occurred. [MEM-RTE-trial-analysis](#mem-rte-trial-analysis), [MEM-BAP-analysis-guidance](#mem-bap-analysis-guidance).
- **External access/persistence:** Viewer/export/upload consume files through explicit operations or a configured trial-end hook. Exported datasets and remote objects are not demonstrated deployed training/solver consumers. [MEM-RTE-artifact-access](#mem-rte-artifact-access).

## Integration issues

1. **Context-fallback qualification:** The full handoff replaces history, but short/ultimate fallbacks submit their task/screen prompt through unwound Chat without explicit full replacement. Reconciliation should retain this distinction when using [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff). Evidence: its annotation and SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`. This prevents classifying all overflow outcomes as the same checkpoint form.
2. **Additional consumers, not contradictions:** [MEM-RTE-trial-analysis](#mem-rte-trial-analysis), [MEM-RTE-sweep-selection](#mem-rte-sweep-selection) and [MEM-RTE-artifact-access](#mem-rte-artifact-access) extend the supplied baseline beyond recovery/foreground continuation. Source dispatch includes them; excluding them would incorrectly equate retained evaluation material with unused logs. Their run-time activation remains unobserved.
3. **Possible overlap:** [MEM-RTE-checkpoint-retention](#mem-rte-checkpoint-retention) overlaps the storage/visibility branch of [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation), but does not replace its loop identity. [MEM-OBJ-process-reward](#mem-obj-process-reward) overlaps metadata contained in [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result), while naming separate host files/snapshots as well. Other new objects/components have distinct identities stated at their declarations; no proposed supersession.
4. **Sweep schema uncertainty:** The inspected selector reads singular verifier_result.reward and uses >0, unlike the full-pass continuation predicate. [MEM-RTE-sweep-selection](#mem-rte-sweep-selection) retains the literal consumer. Without tracing compatible production output, successful filtering on current ordinary trial results is unresolved; do not assert it from the sweep's label.
5. **Trace completeness and trust:** The analysis prompt calls primary trajectory the full history, but segmented/subagent/parsed alternatives and save failures qualify that label. [MEM-OBJ-trajectory](#mem-obj-trajectory), [MEM-RTE-trial-analysis](#mem-rte-trial-analysis). There is no inspected authenticity or semantic freshness gate for cached interpretation; cached file existence can outlive changed evidence.
6. **Unclosed external and task paths:** Alternate agent retention, SDK/provider compaction/deletion, per-task memory workload internals, full trace-export normalization, remote platform consumers and checkpoint-to-published-CSV derivation remain uninspected or external as specified in the coverage table. These prevent universal memory-policy, exported-fidelity, cross-trial solver-learning and measured-benefit conclusions; they do not negate the positive handoff/analysis routes.

## Limitations and checks

The checkout HEAD was rechecked as 7ca0cacea9bf6a0694eaad7306bed794eaaaabce and its status was clean. The supplied run/source identities and complete prompt, types, boundary, runtime, collection, worker rules and records contract were read; bounded reads recovered the range tails. Inspection stayed at SRC-1 and used no prior target analysis, target execution or delegated agent. Two exploratory searches named nonexistent files and returned status 2; their results were not treated as absence evidence, and subsequent reads used the actual dispatched implementation paths.

Presence, delivery and automatic installation are source-grounded where stated; actual semantic activation and benefit remain unobserved. No claim of model-weight learning, faithful memory, universal grader secrecy or successful self-improvement follows from retained files or connected calls. The source-bounded uncertainties are retained above rather than represented as evidenced absences.

Validation: invocation-specific validate-output passed the member content check. The validator states that invocation residue is not checked and that this is not job acceptance or claim support.
