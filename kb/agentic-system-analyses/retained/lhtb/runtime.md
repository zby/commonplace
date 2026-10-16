---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LHTB runtime baseline: terminal task execution, continuation, hidden verification and alternate Harbor integration paths at the frozen revision."
run-id: AAS-2026-10-15-lhtb-a0548ba4edbf-01
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
---

# LHTB runtime report

## Runtime account

### What the workflow does and what this evidence establishes

LHTB supplies terminal problems and a modified Harbor evaluation workflow. Its consequential work is to give a selected agent task instructions and a sandbox, let the agent change the task workspace, grade the resulting work, and retain trial results. Continuation can convert an agent's early completion into another attempt within the budget. It does not make the harness itself a general problem-solving model. Task-local programs remain workloads, not automatically harness capabilities. The frozen scope and external dependency limits are in [boundary](boundary.md#boundary-and-evidence).

All implementation findings below use SRC-1 at the boundary's revision. Added implementation inspection covers agent factory dispatch, installed Codex invocation, Chat and the LiteLLM Responses transport, the 0.20.x replacement module's continuation loop, and the task-specific verifier launcher, as well as further portions of job reconciliation, trial execution and Terminus-2 context management. The patch guide is doctrine/design evidence; its shell snippets were not executed. Neither target execution nor providers were invoked. Wiring is inspectable; actual activation, deployed containment, comparative performance and benefits of continuation or summarization remain unobserved.

### An ordinary shipped invocation

The example caller is `harbor run -c configs/examples/full_benchmark_2.0.yaml`. Its operator selects Docker, four concurrent trials, one attempt, Terminus-2 with `openai/gpt-4.1`, a 10,800-second agent override and both task roots (SRC-1, `configs/examples/full_benchmark_2.0.yaml`). `run` aliases job start; the CLI builds a job, checks host-environment access and awaits its execution (SRC-1, `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/cli/jobs.py`). Job reconciliation matches saved trial configurations and submits remaining configurations to its queue under a task group (SRC-1, `harbor/src/harbor/job.py`). This is independent trial coordination, not evidence of agents exchanging knowledge.

The trial writes configuration and identity, builds/starts and health-checks its environment, sets the task's agent user and sets up the selected agent. For a single-instruction task it invokes the agent; timeout or nonzero agent exit can still lead to final verification and artifact collection. Finalization attempts environment shutdown and writes the result before emitting END. See [RT-RTE-trial-execution](#rt-rte-trial-execution) and [RT-RTE-job-recovery](#rt-rte-job-recovery).

Terminus-2 creates a Chat and formats the task instruction with current terminal output. Configured MCP descriptors and a discovered skills section can augment that instruction; these are model-visible descriptions, not independent permission checks. The model chooses analysis, plan, command keystrokes, durations and completion intent. The parser converts the response into command objects; execution sends those keystrokes to the existing tmux session and returns bounded terminal output. Code owns parsing, duration bounds, timeout handling and completion confirmation; the remote model owns the proposed next action. There is no per-command operator approval in this inspected execution loop. The effect boundary is the selected environment under its effective user, not a restricted command vocabulary. See [RT-RTE-terminal-actions](#rt-rte-terminal-actions) and [RT-CMP-terminus-model](#rt-cmp-terminus-model).

The completion signal is not the answer oracle. Terminus-2 asks for confirmation and returns after a second completion indication. When continuation is enabled, Harbor decides whether to verify and continue. The task-owned test package supplies the reference outcome; Harbor runs it and parses its reward file. The continuation full-pass predicate is numeric `reward >= 1.0`, not an inspection of the agent's explanation. The final result includes metrics, errors, rewards, timing and artifact paths; it does not certify that all task requirements were substantively met. See [RT-RTE-verifier-continuation](#rt-rte-verifier-continuation) and [RT-RTE-verifier-execution](#rt-rte-verifier-execution).

### Material routes and forcing cases

Four forcing cases prevent stronger generalizations:

1. **Fresh conversation versus same conversation.** In the bundled 0.7-based trial, continuation defaults to repeated `run()` invocations in the same environment. Terminus-2 resets per-run state and creates a new Chat on each `run()`. With `HB_CONTINUE_MODE=same_conversation`, the trial requires a resume method and reuses Chat and tmux; only confirmed completion ordinarily triggers interim verification. Unexpected stopping reasons terminate that loop. Thus “continue until timeout” describes a protocol, not an unconditional liveness invariant. Timed process-reward mode additionally requires this same-conversation path and an ephemeral-log environment; mounted environments are rejected. Its checkpoint pauses permit grading during the run, and its budget measures active agent segments rather than simply wall time. Source: SRC-1, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/agents/terminus_2/terminus_2.py`; [RT-RTE-verifier-continuation](#rt-rte-verifier-continuation).
2. **Shared versus separate verifier.** Shared grading uploads tests into the agent environment. The trial tries to freeze tmux descendants and remove tests before resuming, but freezing and scrubbing errors only warn in the bundled implementation. Non-ephemeral providers may retain grader logs to avoid destroying bind-mounted results. Separate grading creates another environment with its own tests and transfers only configured artifacts plus the convention artifacts channel; transfer failures warn rather than establishing a complete snapshot. This is stronger separation by construction, not proof that deployed sandboxes cannot communicate. Source: SRC-1, `harbor/src/harbor/trial/trial.py`; [RT-CLM-grader-isolation](#rt-clm-grader-isolation).
3. **Alternate agents and host extensions.** Factory dispatch can select installed agents or dynamically import an agent class. The inspected Codex adapter explicitly disables its CLI approvals and sandbox; it does not inherit Terminus-2's parser or completion protocol. Shell commands can start subprocesses and use installed/network capabilities according to the environment. Consequently the Terminus-2 loop is not a universal enforcement point for all agents, shell-side model calls or custom extension behavior. Source: SRC-1, `harbor/src/harbor/agents/factory.py`, `harbor/src/harbor/agents/installed/codex.py`; [RT-RTE-agent-dispatch](#rt-rte-agent-dispatch).
4. **Different installed Harbor.** The shipped Daytona wrapper resolves an external Harbor executable and targets Harbor >=0.19. The patch guide provides a whole-module 0.20.x replacement. That replacement defaults to binary verifier feedback for restarted phases, explicitly allows diagnostic mode, and fails when process freezing fails. These differ from the bundled trial's default diagnostic-instruction branch and best-effort freezing. No installed-runtime identity or parity is established by the wrapper's presence. Source: SRC-1, `scripts/daytona_cleanup/run_daytona_eval.sh`, `harbor/skills/apply-lhtb-patches/PATCH.md`, `harbor/patches/single_step.py.harbor-0.20.0`; [RT-RTE-runtime-patching](#rt-rte-runtime-patching).

Multi-step execution is another shipped branch: it runs setup, optional health checks, a step agent invocation and step verification, relocates per-step logs, collects artifacts, and can abort remaining steps on exceptions or a configured minimum reward. It aggregates according to the task's multi-step strategy rather than passing through the single-task continuation loop. Terminus-2's per-`run()` reset explicitly accounts for reuse across steps. Source: SRC-1, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/agents/terminus_2/terminus_2.py`; [RT-RTE-trial-execution](#rt-rte-trial-execution).

### Controls, guarantees and limits

Capability surface, configured grants and deployment isolation are separate. The capability surface includes arbitrary terminal keystrokes, installed agent CLIs, configured MCP endpoints and host-loaded extension classes. In the example, the current selection is Terminus-2 in Docker; the migration task separately requests no internet and no MCP servers and chooses its users/resources through task configuration. Those declarations are not an inspection of a running container, image or network policy. Provider-native tools and arbitrary callbacks inside uninspected providers or custom imports cannot be assumed to share the inspected parser controls. The direct summarization model call also bypasses Chat, though its returned text is used as context rather than executed as shell commands. Source: SRC-1, `configs/examples/full_benchmark_2.0.yaml`, `tasks/langchain-version-migration/task.toml`, `harbor/src/harbor/agents/factory.py`, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

| Load-bearing guarantee | Owner and enforcement | Strength and coverage | External contract and conclusion limits |
|---|---|---|---|
| A parsed command duration is at most 60 seconds | Terminus-2 parser adapter uses `min(parsed_cmd.duration, 60)` | Invariant for that command field, not subprocess lifetime or whole-task runtime | tmux send/wait semantics are separate; installed/custom agents are alternate paths. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Continued work stops at a budget or full verifier pass | Trial loop uses remaining-time checks, `asyncio.wait_for` and reward predicate | Protocol for single-task continuation; errors, stop reasons, unsupported resume and multi-step paths qualify it | Requires agent/provider cancellation and verifier behavior. Not a deployed hard wall-clock limit across teardown and grading. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Hidden grading material is not used as ordinary agent feedback | Same-conversation formatter emits fixed rejection; shared cleanup and separate grading reduce exposure | Binary message construction is an invariant of that formatter. Environmental hiding is best effort in bundled shared mode, not universal isolation | Requires provider filesystem/process/network containment; default restarted branch can supply diagnostics, and mounted logs may remain visible. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-CLM-grader-isolation](#rt-clm-grader-isolation). |
| Completed trials survive job restart | Job validates matching config, reloads trial result files and schedules unmatched trials | Protocol at job reconciliation, not resumable in-flight model execution | Requires readable, consistent files; incomplete trial directories are removed. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-job-recovery](#rt-rte-job-recovery). |

The duration and budget controls are code controls over one route, not proof of safe actions. The task's grading oracle is distinct from operating-system permission enforcement. These conclusions survive the forcing cases only at the scopes stated above.

### Working context and change admission

Terminus-2 limits terminal observations by keeping the first and last portions and omitting the middle. When estimated free tokens fall below the configured threshold, it calls a summary/question/answer sequence, replaces the old conversation with a small handoff frame and resets the provider response chain. Context-overflow recovery first removes recent turn pairs; it then attempts full summarization, a short direct model call, or task-plus-screen fallback. The removed content is not automatically reachable by reference merely because trajectory files exist. See [RT-RTE-context-handoff](#rt-rte-context-handoff). This establishes model-mediated working-context replacement, not faithful memory or improved capacity; detailed memory revision findings belong to the memory member.

The ordinary task solver automatically admits command effects into its task workspace without per-change human approval. The hidden grader can veto a pass/continuation decision, not undo the workspace mutation. This is work-product revision, not by itself self-improvement of LHTB. Runtime changes have a different path: an operator or maintenance agent follows the patch guide to replace installed runtime code, with a backup in the provided recipe and no software gate authenticating the change. Factory imports likewise grant configured code execution, not safe automatic capability synthesis. These admission mechanisms are separated in [RT-RTE-terminal-actions](#rt-rte-terminal-actions), [RT-RTE-agent-dispatch](#rt-rte-agent-dispatch) and [RT-RTE-runtime-patching](#rt-rte-runtime-patching). No supplied execution evidence shows an evidence-responsive runtime modification being deployed and causally affecting a subsequent run.

## Shared records

### Components

#### RT-CMP-terminus-model
Label: Terminus-2 task and summarization model

The source-native component is the `_llm` selected by Terminus-2 from model name and backend configuration. Its operative content is distributed-parametric; parameters reside behind the selected service/backend, not in the repository. The same component is used for task turns and the inspected summarization helper. No parameter-update operation is present in these call paths; provider-side mutation and training are uninspected. Exact weights/version are not pinned by the example's `openai/gpt-4.1` name. A configurable API endpoint or provider alias can resolve to different model implementations. This is configuration-level identity, not immutable parameter identity. Source: SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `configs/examples/full_benchmark_2.0.yaml`, `harbor/src/harbor/llms/lite_llm.py`.

> response: LLMResponse = await self._llm.call(
>             prompt=prompt,
>             message_history=message_history,
>             **self._llm_call_kwargs,
>         )
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

The ordinary Chat call passes history and a previous-response identifier. On the Responses path a non-null identifier sends only the new prompt, relying on the external service to retain the chain. That provider state is opaque, not an independently inspectable second model. Its persistence and deletion guarantees are not established here (SRC-1, `harbor/src/harbor/llms/chat.py`, `harbor/src/harbor/llms/lite_llm.py`).

#### RT-CMP-agent-factory
Label: AgentFactory dispatch

`AgentFactory` is symbolic Python source on disk, loaded into the Harbor host process. Its fixed dispatch rules select registered classes or import a configured module and class; its own source is fixed at the reviewed commit. This component is not distributed-parametric. Dynamically selected agents can introduce further opaque models whose parameter identity, mutability and provider retention are uninspected; they must not inherit the model findings above. Source: SRC-1, `harbor/src/harbor/agents/factory.py`.

> module = importlib.import_module(module_path)
> --- `harbor/src/harbor/agents/factory.py`

### Operative objects

#### RT-OBJ-trial-result
Label: TrialResult and saved configuration

The source-native trial result is symbolic Pydantic/JSON state persisted in the trial directory, alongside configuration, exception information and logs. It identifies task, agent, run timings, reward and outcome metadata; job reconciliation later consumes saved config/result files. Narrative error text is carried within it, but matching, reward extraction and scheduling use fixed code rules. It is not a certified answer, a saved Chat checkpoint or evidence of learned model parameters. Source: SRC-1, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/job.py`.

> self._trial_paths.result_path.write_text(self.result.model_dump_json(indent=4))
> --- `harbor/src/harbor/trial/trial.py`

#### RT-OBJ-task-instruction
Label: Task instruction at the model consumer

The task instruction is natural-language content read from the selected task and formatted with terminal state into a model prompt. Its storage substrate is the task file and then process/remote conversation state. It acquires force through model interpretation, not a symbolic requirement checker. MCP descriptions and skill descriptions can be appended to it. Repeated-run continuation may append verifier feedback to the original instruction; same-conversation mode appends a rejection turn instead. Source: SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/trial/trial.py`.

> initial_prompt = self._prompt_template.format(
>             instruction=augmented_instruction,
>             terminal_state=terminal_state,
>         )
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

### Routes

#### RT-RTE-trial-execution
Label: Job-to-trial execution and finalization

The operator initiates CLI job start; job/queue code owns trial scheduling and the trial owns environment setup, user switching, selected agent invocation, verification and finalization. Identities include task ID/checksum, trial name, source and agent info in the result. Configuration is symbolic policy; task text is model guidance. Source: SRC-1, `harbor/src/harbor/cli/main.py`, `harbor/src/harbor/cli/jobs.py`, `harbor/src/harbor/job.py`, `harbor/src/harbor/trial/trial.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TrialResult to the job after attempted cleanup; CLI prints aggregated job results.
- Later read-back: Saved results/configuration enter job recovery through [RT-RTE-job-recovery](#rt-rte-job-recovery); no restored in-flight agent conversation is established.
- Delegated visibility: Agent receives task instruction and environment access; verifier receives its tests and configured environment/artifacts, not the job's entire host state by default.
- Selection predicate: Job task/agent configurations select a trial; task.has_steps selects multi-step instead of the single-instruction branch; verifier.disable suppresses final grading.
- Invalidation or expiry: Environment deletion follows configuration; saved host results remain until external removal or recovery policy changes them.
- Activation or effect: Code invokes environment/agent/verifier effects and writes structured outcomes; successful operation is not observed.
- Evidence limits: External images/providers and installed execution state are not captured; queue retry details and every integration are not exhaustively audited.

For the multi-step branch, code owns ordered progression and minimum-reward veto; task authors supply step instructions, tests and thresholds. The agent proposes task mutations. Human involvement is at task/config authorship and launch, not a required per-step judgment. Operating mode is a bounded benchmark, with task-specific answer oracles executed by the verifier. Abort on exception and reward thresholds supplies recovery by stopping remaining steps, not rollback of earlier workspace changes.

> if not self.config.verifier.disable and not self._task.has_steps:
> --- `harbor/src/harbor/trial/trial.py`

> failure = _min_reward_failure(rewards, step_cfg.min_reward)
> --- `harbor/src/harbor/trial/trial.py`

#### RT-RTE-terminal-actions
Label: Model response to terminal workspace mutation

Terminus-2 calls [RT-CMP-terminus-model](#rt-cmp-terminus-model), parses its response and sends each command's keystrokes to tmux. The model proposes and selects commands; runtime code applies parser rules, bounds the command wait and owns the next observation. No human veto is wired into this inspected loop. Actions can edit files, run programs and launch subprocesses under the environment user. Guidance is the task, terminal observations and prompt protocol, not proof of compliance. Source: SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded terminal output, timeout feedback and parsing feedback become the next model observation.
- Later read-back: Task files survive within the environment for later commands/phases; durable cross-run agent reuse is uninspected, and ordinary turn accumulation alone is not retained learning.
- Delegated visibility: Shell and its children inherit effective environment/user capabilities; this route contains no generic sub-agent isolation boundary.
- Selection predicate: Parsed command list from the model; completion requires confirmation, and episode/budget controls can terminate the loop.
- Invalidation or expiry: Workspace lifetime follows environment lifecycle; a command's effects are not expired by ending its wait.
- Activation or effect: Parsed keystrokes are sent for execution, so the effect surface is the shell, not just a declarative plan.
- Evidence limits: No executed commands or approval traces were supplied; correctness and containment of actual effects remain unobserved.

Admission: a model-selected command is admitted automatically once parsed. The workspace is a task product; command failure, subsequent edits or environment deletion can replace it, but the route has no general transactional rollback. The hidden verifier can reject the result, not veto each prior command. Operating mode is bounded task solving. The verifier is the external answer oracle for pass decisions; the model's own judgment is not an oracle. This route does not establish revisions to the harness's own organization or a theory-builder cycle: it requests analysis and planning, but no specific formulated theory, content-directed criticism or retained iterative theory revision is evidenced by source wiring alone.

> duration_sec=min(parsed_cmd.duration, 60),
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> await session.send_keys(
>                     command.keystrokes,
>                     block=False,
>                     min_timeout_sec=command.duration_sec,
>                 )
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

#### RT-RTE-verifier-continuation
Label: Interim verification and agent continuation

Task configuration and an available agent timeout enable the bundled trial loop. Trial code decides continuation and uses verifier rewards as an answer oracle. The model proposes completion or further work but cannot itself set a passing reward through the completion flag. Task authors provide the oracle/test behavior; no human approval is required on each rejection. Source: SRC-1, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/agents/terminus_2/terminus_2.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full pass exits the loop; failure supplies another instruction or rejection turn while budget permits.
- Later read-back: Same-conversation mode retains Chat/tmux; restarted mode retains environment files but Terminus-2 creates a new Chat. Context replacement is separately traced in [RT-RTE-context-handoff](#rt-rte-context-handoff).
- Delegated visibility: Same-conversation rejection exposes failure and remaining-time metadata, not detailed grader text by construction; restarted mode can format verifier-derived diagnostics. Filesystem exposure is a separate issue.
- Selection predicate: continue_until_timeout plus timeout; HB_CONTINUE_MODE chooses same-conversation; in that mode confirmed_task_complete triggers ordinary interim grading, while other stop reasons break. Process-reward configuration selects checkpoint grading and requires compatible agent/environment methods.
- Invalidation or expiry: Agent wall deadline, active-time budget in process mode, full pass, errors and other stopping conditions terminate continuation.
- Activation or effect: A rejected phase can cause another model invocation with the current workspace; no successful repair or benefit is observed.
- Evidence limits: The default restarted and same-conversation routes are distinct; checkpoint timing and preservation of hidden results are source-grounded, not execution-tested here.

Operating mode: bounded benchmark repair, with timeout/checkpoint triggers. The admitted change is another phase's task-workspace revision; no human content gate or automatic workspace rollback is provided. The test package can veto stopping on apparent completion through the reward predicate. Unsuccessful work remains available for later repair. The loop does not itself establish content-directed criticism of a formulated theory; binary rejection supplies no claim-level blame.

> same_conversation = continue_until and (
>             os.environ.get("HB_CONTINUE_MODE", "").strip().lower()
>             == "same_conversation"
>         )
> --- `harbor/src/harbor/trial/trial.py`

> return float(reward) >= 1.0
> --- `harbor/src/harbor/trial/trial.py`

> if same_conversation and reason != "confirmed_task_complete":
> --- `harbor/src/harbor/trial/trial.py`

#### RT-RTE-verifier-execution
Label: Task-owned grading in shared or separate environments

Trial code chooses shared/separate mode and calls Verifier. In shared mode Verifier uploads the task tests. In separate mode the trial creates a verifier environment, resets its verifier output directory, transfers convention/configured artifacts and invokes Verifier with tests already in the image. Fixed code parses reward JSON or text. The task package owns expected answers and scoring; the harness owns execution and result transport. Source: SRC-1, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/verifier/verifier.py`, `tasks/langchain-version-migration/task.toml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: VerifierResult containing parsed rewards, or an error for missing/empty/unparseable reward output.
- Later read-back: Rewards enter saved trial/job outcomes and interim continuation decisions; hidden checkpoint records are not ordinary model input by this route.
- Delegated visibility: Separate verifier receives declared artifacts at original container paths and shared convention artifacts, but omits the default agent-log mount. Explicit agent-log artifacts can still be configured.
- Selection predicate: Effective task/step verifier mode, tests package and configured artifacts; JSON reward takes precedence over text when present.
- Invalidation or expiry: Separate environment is stopped after a pass attempt; shared tests/output hiding depends on provider and cleanup success.
- Activation or effect: Task test script runs under effective verifier user and its reward is parsed; this supplies a programmatic outcome, not proof of a scientifically correct oracle.
- Evidence limits: Image contents and task oracle validity are not audited exhaustively; artifact transfer can fail with warnings, so a selected path is not a guaranteed faithful snapshot.

The migration task declares separate verification and a list of source/config/data/output artifacts. A contrasting task launcher invokes a private judge and attempts dense reward extraction, falling back to exit-code reward. That establishes task-local reference-outcome computation, not a universal expected-answer format (SRC-1, `tasks-2.0/acoustic_beamforming_peak__01/tests/test.sh`). No model oracle is required by this inspected launcher. Other graders may differ.

> skip_tests_upload=True,
> --- `harbor/src/harbor/trial/trial.py`

> if self._trial_paths.reward_json_path.exists():
>             rewards = self._parse_reward_json()
>         elif self._trial_paths.reward_text_path.exists():
>             rewards = self._parse_reward_text()
> --- `harbor/src/harbor/verifier/verifier.py`

#### RT-RTE-context-handoff
Label: Terminal filtering and model-mediated context handoff

Terminus-2 code chooses context management by terminal-output length, estimated free tokens and overflow exceptions. It limits terminal output, and proactive summarization obtains a summary, questions from a reduced view and answers from the fuller history. It replaces Chat history and resets the server response chain; answers enter as the next handoff prompt. These are natural-language transformations consumed by the model, stored in memory and associated trajectory files. Source: SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/llms/chat.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filtered observation or handoff prompt plus subagent trajectory references; subsequent foreground call uses the replacement context.
- Later read-back: Model-produced summary/question/answer material reaches a later invocation within the run. Raw trajectory retention alone does not show model reload.
- Delegated visibility: Summary and answer calls receive fuller history; question generation receives the task, summary and current terminal view. Calls return text, not independently executing terminal workers.
- Selection predicate: Output exceeds byte bound; free tokens fall below proactive threshold; or provider raises ContextLengthExceededError with summarization enabled.
- Invalidation or expiry: History replacement removes prior turns from active Chat. Overflow first removes recent pairs; successful reset invalidates the previous response chain. No automatic raw-history reload route is established.
- Activation or effect: Code changes the next call's context; whether meaning is preserved or decisions improve is unobserved.
- Evidence limits: Model compliance, summary fidelity, full provider state erasure and successful recovery at actual limits are unobserved. Memory-specific revisions and lineage are left to the memory member.

Admission: code automatically installs model-produced handoff text without human review; runtime models propose summaries/questions/answers, while code owns triggering and replacement. No answer oracle validates semantic fidelity. Fallbacks attempt a full summary, then a short direct model call using task and screen tail, then task-plus-screen without an extra model call. These are recovery choices, not restoration of omitted history. This resembles an isolated call frame for the question subcall, but the full-history calls copy context and the foreground replacement retains selected text by value; trajectory references are not transparent memory pointers. The route does not establish a retained criticism/revision cycle for a theory.

> chat._messages = [
>             chat.messages[0],
>             {"role": "user", "content": question_prompt},
>             {"role": "assistant", "content": model_questions},
>         ]
>         chat.reset_response_chain()
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

> # Remove the most recent pair of messages (user + assistant)
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

#### RT-RTE-job-recovery
Label: Completed result reload and remaining-trial selection

Job code consumes [RT-OBJ-trial-result](#rt-obj-trial-result) and saved configurations. It refuses a changed job configuration, removes directories without result files, reloads completed trials, and matches them to planned configurations. This is symbolic state reconciliation, not agent reflection or conversation recovery. Source: SRC-1, `harbor/src/harbor/job.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reconstructed existing statistics and remaining trial configurations for scheduling.
- Later read-back: Prior trial outcomes affect what runs after restart and aggregated reward/statistics output.
- Delegated visibility: Job scheduler sees saved outcomes; no delivery of previous trials' contents to a new solving model is established.
- Selection predicate: Existing job configuration must equal the requested configuration; completed trial configs must match planned configs.
- Invalidation or expiry: Directories lacking result files are deleted; changed job configs are rejected, and unmatched existing trials cause an error.
- Activation or effect: Completed work can be skipped while unmatched work is scheduled; no preservation of in-flight computations is implied.
- Evidence limits: Crash consistency, filesystem integrity and all retry paths were not experimentally tested; a parseable file is not authenticated execution evidence.

This successor selection is performed by code under a bounded job specification. The saved configuration is the matching reference, not a task answer oracle; no human admission of each recovered result is required. Recovery admits prior completed outcomes to aggregation without improving the solver itself.

> if not trial_paths.result_path.exists():
>                 shutil.rmtree(trial_paths.trial_dir)
> --- `harbor/src/harbor/job.py`

> raise FileExistsError(
>                 f"Job directory {self.job_dir} already exists and cannot be "
>                 "resumed with a different config."
>             )
> --- `harbor/src/harbor/job.py`

#### RT-RTE-agent-dispatch
Label: Installed agent and dynamic capability admission

Operator/caller configuration selects a registered agent or import path. [RT-CMP-agent-factory](#rt-cmp-agent-factory) imports and instantiates the selected class on the host. The inspected installed Codex adapter then executes an external CLI inside the selected environment. Source: SRC-1, `harbor/src/harbor/agents/factory.py`, `harbor/src/harbor/agents/installed/codex.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Agent instance to the trial; installed-agent execution yields logs/context through its adapter.
- Later read-back: inapplicable — dispatch itself installs no trace-derived knowledge; installed agents' independent retention is uninspected.
- Delegated visibility: Imported class receives logs path, model name, resolved environment and kwargs; Codex receives the task and configured tools/skills and runs outside Terminus-2's parser.
- Selection predicate: Registered name takes precedence when valid; otherwise configured import_path can select arbitrary installed module/class.
- Invalidation or expiry: Configuration can choose another agent in a later job; module loading has no general unload/rollback transaction here.
- Activation or effect: Configuration admits executable host code, and installed CLI commands can act inside the environment.
- Evidence limits: Only Codex is inspected as a concrete installed-agent forcing case; other agents and opaque CLI/model internals are not generalized from it.

Admission trigger is launch configuration, not model-generated plugin approval. Caller authorship may be human or software; source alone does not establish a human review gate. Import syntax, lookup and constructor errors reject invalid choices; they do not vet code safety. Recovery is correcting config or replacing the installation, not an automatic rollback. No answer oracle approves a capability; operating mode is configured benchmark execution. Provider-native tools, extension callbacks and shell-side services need their own coverage before any shared guarantee can be asserted.

> "--dangerously-bypass-approvals-and-sandbox "
> --- `harbor/src/harbor/agents/installed/codex.py`

#### RT-RTE-runtime-patching
Label: Installed Harbor patch admission

The shipped patch guide instructs an operator or maintenance agent to back up and replace an installed 0.20.x module, or port the current implementation to other versions. It warns against using the historical diff alone. This is natural-language procedural guidance and symbolic replacement code on disk, not an automatically verified update service. Source: SRC-1, `harbor/skills/apply-lhtb-patches/PATCH.md`, `harbor/patches/single_step.py.harbor-0.20.0`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: The recipe prints patch-marker checks after replacing code; that output is not evidence the recipe was executed.
- Later read-back: Future installed Harbor invocations can import the replaced module, changing continuation, feedback and hardening policy.
- Delegated visibility: Maintenance actor needs filesystem write authority over the installed Harbor package; benchmark-solving agents are not granted it by this guide alone.
- Selection predicate: Version-specific recipe or manual port; the guide directs use of current source/drop-in rather than the original historical diff.
- Invalidation or expiry: Recipe copies the original to a backup; restoring that file is possible but no automatic rollback is wired. Later installation can supersede the patch.
- Activation or effect: Installing and later importing replacement code can change production machinery. Actual installation, import and behavior change are unobserved.
- Evidence limits: This path does not prove parity of the vendored runtime, drop-in and installed wrapper target; no source-supported deployment trace closes that gap.

The maintenance actor proposes/edits and decides admission; shell copy performs physical installation. No software review gate or per-update human identity is established. The guidance says the phase loop alone can reintroduce leaks and describes grader-hiding checks. Those requests do not establish completed checks. Operating mode is version-bounded maintenance; no task answer oracle validates the port. The independent objective is reference evaluation semantics and grader isolation, but evidence-responsive update determination, live installation and subsequent causally dependent operation are not observed. Thus this is an afforded machinery-change route, not demonstrated self-improvement or a theory-builder cycle.

> cp "$PKG/trial/single_step.py" "$PKG/trial/single_step.py.bak"
> cp harbor/patches/single_step.py.harbor-0.20.0 "$PKG/trial/single_step.py"
> --- `harbor/skills/apply-lhtb-patches/PATCH.md`

The replacement's rejection policy is materially different from the default bundled restarted branch:

> mode = os.environ.get("HB_VERIFIER_FEEDBACK_MODE", "binary").strip().lower()
> --- `harbor/patches/single_step.py.harbor-0.20.0`

> "HB_VERIFIER_FEEDBACK_MODE=diagnostic exposes verifier-derived "
>                 "details to the agent; results are not benchmark-comparable"
> --- `harbor/patches/single_step.py.harbor-0.20.0`

### Claims

#### RT-CLM-grader-isolation
Label: Grader hiding and binary feedback hardening

The shipped patch guide claims grader hardening is required alongside continuation. The implementation supplies multiple enforcement points rather than a single universal gate. Shared mode uploads tests into the agent's own environment; best-effort process-tree freezing and test/log cleanup reduce exposure. Separate mode moves grading into a distinct environment. Same-conversation rejection contains no diagnostic text; default restarted continuation can read migration details or scalar reward and format them into the instruction. Binary prompt construction therefore does not imply hidden-material isolation over all routes. Source: SRC-1, `harbor/skills/apply-lhtb-patches/PATCH.md`, `harbor/src/harbor/trial/trial.py`, `harbor/src/harbor/verifier/verifier.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: best effort

Owner: Harbor trial/verifier code; task authors choose separate mode and artifact boundaries. Covered paths: interim/final verification routed through those classes, subject to provider and mode conditions. Alternate paths: mounted shared logs, processes outside tmux descendants, failed cleanup, direct filesystem access, explicit artifact paths, installed/custom agents and the version-specific drop-in. Required external contract: provider filesystem/process/network isolation and faithful image/test provisioning. The deployed isolation envelope is uninspected, so universal confidentiality and benchmark comparability are not established. The drop-in's fail-closed freezing does not retroactively strengthen the bundled code.

> Best effort: never fail a trial from here.
> --- `harbor/src/harbor/trial/trial.py`

> "Provider %r may bind-mount %s; grader logs cannot be cleared "
>                 "without risking result destruction.",
> --- `harbor/src/harbor/trial/trial.py`

> It documents the original 0.7.0 phase loop, but predates binary feedback, process
> freezing, and verifier-log scrubbing. **Do not apply it by itself for scored runs.**
> --- `harbor/skills/apply-lhtb-patches/PATCH.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-task-guidance
Label: Task and continuation guidance to solver

Consumer: the task-solving model. Channel: initial task/terminal prompt and later observation, handoff or rejection turns. Force: natural-language interpretive guidance; command effects occur only after the response is parsed/executed. Horizon: turns and continuation phases of one trial; restarted phases reintroduce the instruction but do not preserve Terminus-2 Chat automatically. Context transformations can replace prior guidance-bearing state. Source: SRC-1, `harbor/src/harbor/agents/terminus_2/terminus_2.py`, `harbor/src/harbor/trial/trial.py`; [RT-OBJ-task-instruction](#rt-obj-task-instruction), [RT-RTE-context-handoff](#rt-rte-context-handoff).

> "Continue working on this task from where the previous agent left off."
> --- `harbor/src/harbor/agents/terminus_2/terminus_2.py`

#### RT-BAP-runtime-module
Label: Replacement runtime code to future trial control

Consumer: installed Harbor importing the replacement module. Channel: package-file replacement followed by future process import. Force: executable symbolic control over phase scheduling, feedback policy and grading hardening. Horizon: later invocations using that installation until another replacement; actual adoption is unobserved. This differs from task guidance: the maintained module controls execution rather than merely asking the model to behave differently. Source: SRC-1, `harbor/skills/apply-lhtb-patches/PATCH.md`, `harbor/patches/single_step.py.harbor-0.20.0`; [RT-RTE-runtime-patching](#rt-rte-runtime-patching).

> Note this is the whole module, not a diff: if you have other local modifications to
> `single_step.py` they will be overwritten.
> --- `harbor/skills/apply-lhtb-patches/PATCH.md`

## Annotations

none
