---
type: types/agentic-system-analysis-result.md
description: 'LHTB bundled Harbor single-step continuation: outcome-derived instructions,
  external verifier gating and conditional isolation with a documentation mismatch'
run-id: AAS-2026-09-25-lhtb-01
system: LHTB
run-date: '2026-09-25'
result-disposition: complete
target-class: orchestration mechanism
boundary-kind: subsystem-only
reviewed-boundary: d78f5eb52ad754c5ee9154741af73130a85a65b8
analysis-cutoff: '2026-09-25'
evidence-tier: code-grounded
memory-comparison:
  axes:
    behavioral_authority:
      assessment: not-determinable
      basis: null
      note: Instruction at agent boundary and scheduler enforcement/validation are
        established; actual force of arbitrary project payloads and diagnostics in
        excluded consumers prevents a complete union.
      records:
      - BAP-1
      - BAP-2
      - OBJ-1
      values: []
    curation_operations:
      assessment: not-determinable
      basis: null
      note: Metric addition, raw log concatenation and access scrubbing do not establish
        semantic consolidation or invalidation. Whether opaque project material undergoes
        memory curation is not determinable at this interface.
      records:
      - OBJ-1
      - OBJ-2
      - RTE-5
      values: []
    distilled_form:
      assessment: not-determinable
      basis: null
      note: Same-conversation and fallback guidance are natural-language. Restart
        guidance can embed arbitrary failure strings or a serialized diagnostic object;
        their opaque payload prevents a complete representation set across both branches.
      records:
      - RTE-7
      - OBJ-4
      values: []
    faithfulness_tested:
      assessment: known
      basis: wired
      note: Inspected evidence is source and static tests only; no retained execution
        test of dependence on recalled content was supplied or run.
      records:
      - ABS-1
      values:
      - 'no'
    learning_scope:
      assessment: known
      basis: wired
      note: The same Trial task instruction/environment and its attempts bound this
        route; no cross-trial guidance store is involved.
      records:
      - RTE-7
      values:
      - per-task
    learning_timing:
      assessment: known
      basis: wired
      note: Derived guidance is produced between failed attempts while the same task
        is still running.
      records:
      - RTE-7
      values:
      - online
    lineage:
      assessment: not-determinable
      basis: null
      note: Trace-extracted continuation and compiled telemetry are established; project
        payload authoring/import and opaque agent-produced metadata derivations are
        not determined.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      values: []
    read_back_direction:
      assessment: known
      basis: wired
      note: Harness requests verifier files/results; automatic continuation supplies
        outcome-derived text to the next agent call; configured artifact transfer
        supplies retained files to verification. Agent-internal retrieval is excluded.
      records:
      - RTE-3
      - RTE-4
      - RTE-7
      values:
      - pull
      - push
    read_back_signal:
      assessment: known
      basis: wired
      note: Continuation supplies latest outcome without relevance search (coarse).
        Configured artifact.source paths identify files selected automatically for
        the verifier. Fixed feedback fallback by file existence does not imply semantic
        matching.
      records:
      - RTE-3
      - RTE-4
      values:
      - coarse
      - identifier
    representational_form:
      assessment: not-determinable
      basis: null
      note: Natural-language instruction and symbolic bookkeeping are visible, but
        arbitrary project files, diagnostic strings and metadata prevent a complete
        form set. JSON containers do not classify payloads.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      values: []
    storage_substrate:
      assessment: known
      basis: wired
      note: Visible project/log files and host artifact files plus phase context and
        instruction variables; external provider/model storage is excluded.
      records:
      - OBJ-1
      - OBJ-2
      - OBJ-3
      - OBJ-4
      values:
      - files
      - in-memory
    trace_learning:
      assessment: known
      basis: wired
      note: Automatic verifier-event-to-instruction transformation is retained across
        the phase boundary and delivered to a later agent call; qualifies under the
        continuation-context rule, without learned parameters, new theory, or proven
        improvement.
      records:
      - RTE-7
      values:
      - 'yes'
    trace_source:
      assessment: known
      basis: wired
      note: Verifier completion/failure/timeout events and phase/time fields feed
        the derived guidance. Optional raw diagnostic payloads are carried through,
        not learned trajectories.
      records:
      - RTE-7
      values:
      - event-streams
    write_agency:
      assessment: known
      basis: wired
      note: Scoped orchestration writes and maintenance run automatically after task
        launch. No manual memory editor/adoption route is exposed by this mechanism;
        supplied task authoring is outside accumulated memory.
      records:
      - RTE-2
      - RTE-3
      - RTE-4
      - RTE-5
      - RTE-6
      values:
      - automatic
  scope: Bundled Harbor single-step continue-until-timeout cross-phase project files,
    AgentContext, verifier artifacts, derived feedback, artifact transfer and result
    retention; restart and same-conversation, shared and separate verifier branches,
    process rewards disabled. Concrete agent/model, provider and test internals excluded.
---

# LHTB bundled continuation mechanism

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-lhtb-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/lhtb.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-25-lhtb-01/memory-report.md`

**Memory analysis report SHA-256:** 23bc96d57b1d17ea8c42e9dcdeeb410be81db9043f497cffcd0af5ae333f7a55

## Boundary and evidence

Target class: orchestration mechanism. Boundary kind: subsystem-only. Selected executable is the bundled Harbor single-step trial continuation with HB_PROCESS_REWARD unset. Includes initial/single-shot branch, restart versus same-conversation continuation, shared versus separate verifier, consumed setup, reward/feedback, visibility and finalization helpers. Excludes timed process-reward checkpoints, multi-step task route, concrete agents/models and provider implementations, task-specific solutions/test criteria, newer 0.20 drop-in patch module, launchers and benchmark rankings.

Code-grounded at d78f5eb52ad754c5ee9154741af73130a85a65b8, inspected 2026-09-25. Sole allowlist https://github.com/zli12321/LHTB using commit-addressed Git at `/home/zby/llm/commonplace/related-systems/zli12321--LHTB`. No worktree or prior analysis evidence. No target runtime, model call, container, dependency installation or benchmark was executed. Repository declarations are claimed evidence, not observed runs.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | https://github.com/zli12321/LHTB | d78f5eb52ad754c5ee9154741af73130a85a65b8 | implementation | bundled trial single-step continuation and consumed contracts | `harbor/src/harbor/trial/trial.py:182-297,358-463,531-687,867-1173,1174-1240,1279-1528,2001-2105`; `harbor/src/harbor/verifier/verifier.py:38-220`; `harbor/src/harbor/models/task/config.py:79-92`; `harbor/src/harbor/models/agent/context.py:8-34`; `harbor/src/harbor/agents/base.py:111-136`; `harbor/src/harbor/environments/base.py:239-254,472-491`; `harbor/src/harbor/models/trial/paths.py:35-42,181-210`; `harbor/tests/unit/test_continue_until_timeout.py:14-77`; `harbor/tests/unit/test_trial_same_conversation.py:11-36,59-129` | concrete agent/provider/task semantics excluded; no benchmark or universal isolation conclusion |
| SRC-2 | Git | https://github.com/zli12321/LHTB | d78f5eb52ad754c5ee9154741af73130a85a65b8 | doctrine/design | descriptions of bundled continuation and isolation | `README.md:19-59`; `harbor/README.md:20-60` | claims checked against live bundled implementation, not substituted patch code |

## Shared records

### Components

CMP-1 — Trial scheduler and phase/result aggregation. Symbolic implementation resolves timeouts, invokes configured agent, calls verifier and decides continuation. Source-wired. No independent model inside this selected scheduler. SRC-1 `harbor/src/harbor/trial/trial.py:358-461,867-1173`.

CMP-2 — Supplied concrete BaseAgent behind run/setup and optional resume_after_verifier_rejection. Source-wired delegation only; actual model identity, parameter fixity/change and internal reasoning/context each uninspected. Configured agent/model descriptors are not an exact weights pin. Selected mechanism does not implement training, but excluded agents may differ. SRC-1 `harbor/src/harbor/trial/trial.py:397-414,912-968`. Supplied concrete agent behind BaseAgent. Implementation conclusion status: afforded. SRC-1 `harbor/src/harbor/agents/base.py:111-136` defines run instruction/environment and output context. SRC-1 `harbor/src/harbor/trial/trial.py:912-917` explicitly rejects same-conversation without callable resume support. Concrete model invocation, conversation serialization, compaction and retained-file reads are uninspected and excluded.

>         Runs the agent in the environment. Be sure to populate the context with the
>         results of the agent execution. Ideally, populate the context as the agent
>         executes in case of a timeout or other error.
> --- `harbor/src/harbor/agents/base.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

CMP-3 — Verifier adapter and configured environment provider. Test script supplied by task author acts as outcome oracle; hidden assertions/reference solutions and any LLM judge internals excluded. Adapter uploads/executes/parses rewards, not a semantic proof checker for arbitrary tasks. Provider capabilities/mount/exec API establish requested controls only. Source-wired. SRC-1 `harbor/src/harbor/verifier/verifier.py:89-220`.

### Operative objects

OBJ-1 — Retained project/environment files. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:409-425,943-968,1396-1486` retains the same environment object across calls and explicitly selects artifact paths for separate verification. Storage is files, potentially with opaque code, natural language or binary content. Agent writes are outside the orchestrator implementation; no mandatory memory schema or reason-retention contract is imposed. Availability to the agent is established; actual rereading is not. Temporary transfer copies and final collected artifacts are derivatives of these files, not learned summaries.



OBJ-2 — AgentContext and aggregate trial result. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/models/agent/context.py:8-34`; SRC-1 `harbor/src/harbor/trial/trial.py:182-232,1017-1026,1148-1172,1235-1239`. In-memory context holds token counts, cost, rollout details and arbitrary metadata; JSON persists the result. Restart merges counts, concatenates raw rollout records and uses later metadata values except designated integer counters; same-conversation shares one context. Termination metadata is operative for scheduling; other fields are telemetry unless a concrete consumer proves otherwise. Opaque rollout/metadata payload form and agent-side uses remain unknown.

>     merged_rollouts: list = []
>     if accumulated.rollout_details:
>         merged_rollouts.extend(accumulated.rollout_details)
>     if phase.rollout_details:
>         merged_rollouts.extend(phase.rollout_details)
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

>                 if same_conversation:
>                     aggregated = phase_context
>                     self.result.agent_result = phase_context
>                 else:
>                     aggregated = _merge_agent_contexts(aggregated, phase_context)
>                     self.result.agent_result = aggregated
> 
>                 if not continue_until:
>                     break
>                 reason = phase_context.metadata.get("termination_reason")
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

OBJ-3 — Verifier rewards and diagnostic artifacts. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/verifier/verifier.py:59-87,191-220`; SRC-1 `harbor/src/harbor/models/trial/paths.py:35-42,181-210`. Reward is structured numeric data used by the scheduler; diagnostic files are external test output with only selected formats recognized for feedback. JSON reward takes precedence over text reward in verification; restart feedback instead prefers `migration_details.json`, then `reward.txt`, then fixed fallback. Thus displayed feedback need not reproduce the reward object used by the acceptance predicate. Files are host-retained through mount or download; this is not an immutable phase history.

>         if self._trial_paths.reward_json_path.exists():
>             rewards = self._parse_reward_json()
>         elif self._trial_paths.reward_text_path.exists():
>             rewards = self._parse_reward_text()
>         else:
>             raise RewardFileNotFoundError(
>                 f"No reward file found at {self._trial_paths.reward_text_path} or {
>                     self._trial_paths.reward_json_path
>                 }"
>             )
> --- `harbor/src/harbor/verifier/verifier.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

OBJ-4 — Outcome-derived continuation instruction. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:245-297,1091-1113,1124-1140,952-967`. Produced automatically after rejection or verifier timeout; retained in the loop's instruction variable and delivered to a subsequent call. Restart retains original task text plus derived phase/time/failure guidance and optional diagnostic payload. Same-conversation retains binary rejection, phase/time and directions to inspect current work. The new text states the immediate reason to continue (non-pass); it omits the hidden test rationale in same-conversation. Restart may preserve a failure reason string, but no explanation of why the verifier is right is required. Delivery of this reason is wired; the concrete agent's reading/activation is not observed.

> def _format_same_conversation_rejection(*, phase: int, remaining_sec: int) -> str:
>     """Return a binary rejection turn with no verifier-derived details."""
>     return (
>         "Your submitted solution did not pass verification. No verifier details, "
>         "test output, or hidden requirements are available. Continue working from "
>         "the current terminal and conversation state. Re-read the original "
>         "requirements, inspect your implementation, and run your own focused "
>         f"checks before submitting again. This is continuation {phase}; "
>         f"approximately {remaining_sec} seconds remain."
>     )
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

### Routes

RTE-1 — Setup/initial invocation. Trial config chooses task, agent, provider and timeout overrides/caps/multipliers. Setup creates environment, healthchecks, changes default user and sets up agent. Environment timeout retries twice; agent setup has timeout and explicit Windows-support gate. Initial run receives task instruction, same environment and an AgentContext. Conclusion status: wired. Provider setup/model installation effects remain external contracts. SRC-1 `harbor/src/harbor/trial/trial.py:381-457,531-584,2001-2036`.

Setup and first run. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:381-425,531-583,918-968,2019-2036`. Task config selects agent/environment and resolved timeout; original task instruction initializes the current instruction. Environment and agent setup precede all phases. No cross-task memory import is established here.



RTE-2 — Phase loop and completion. continue_until requires task flag and finite agent timeout. With HB_CONTINUE_MODE=same_conversation, missing callable resume API raises before execution; first call is run, later calls pass user_prompt to resume on continuous context. Default restart calls run again with a fresh phase context on the same agent/environment; this code alone does not establish concrete conversation reset/preservation. Restart metrics merge; same mode shares context. Clock budget bounds awaited agent phase, with time spent in interim verification counted against later remaining wall time. It is not a hard total trial timeout: verifier/setup/finalization have separate budgets. Source-wired. SRC-1 `harbor/src/harbor/trial/trial.py:867-988,1017-1025,1074-1147`.

>         resume_agent = getattr(self._agent, "resume_after_verifier_rejection", None)
>         if same_conversation and not callable(resume_agent):
>             raise RuntimeError(
>                 "HB_CONTINUE_MODE=same_conversation requires an agent that "
>                 "implements resume_after_verifier_rejection()"
>             )
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

Single-shot exits after one agent call. Same-conversation continuation only verifies after metadata termination_reason confirmed_task_complete; another stop reason breaks. Successful reward gate or nonpositive remaining time breaks; timeout raises AgentTimeoutError and final verification may still run. Timeout branch can record partial contexts but does not roll back work. No human review selects continuation. Execution owner is supplied agent; veto comes from scheduler budget/oracle. The oracle selects current artifact acceptance, not an improved successor agent.

Phase execution and retention. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:918-1026,1074-1084,1148-1172`. Producer is the supplied agent; scheduler retains phase metrics and termination metadata. Restart calls `run` with new context, same-conversation calls resume with shared context. Clock/config/termination reason determine whether a later phase exists. Raw rollout aggregation has no inspected route that supplies merged rollouts back to the model as history.

>                 phase_context = (
>                     continuous_context
>                     if continuous_context is not None
>                     else AgentContext()
>                 )
>                 active_budget_timeout = False
>                 if self._process_reward_tracker is not None:
>                     self._process_reward_tracker.start_segment()
>                 try:
>                     if same_conversation and agent_started:
>                         await asyncio.wait_for(
>                             resume_agent(
>                                 user_prompt=instruction,
>                                 context=phase_context,
>                             ),
>                             timeout=remaining,
>                         )
>                     else:
>                         await asyncio.wait_for(
>                             self._agent.run(
>                                 instruction=instruction,
>                                 environment=self._environment,
>                                 context=phase_context,
>                             ),
>                             timeout=remaining,
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

RTE-3 — Interim/final verification. Shared mode uploads task tests and executes them in agent environment under verifier user. Separate mode creates a fresh verifier environment per call, resets its logs, transfers implicit artifacts for nonmounted target and configured artifacts at the same paths, then executes baked tests with skip_tests_upload. Transfer errors can warn/continue; artifact closure is not proved. Reward JSON takes priority over text; text parses float; missing/empty/malformed reward errors. Gate checks reward key>=1.0 only, not all reward fields or script exit status. Conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:235-242,585-604,1360-1528`; `harbor/src/harbor/verifier/verifier.py:59-87,132-220`.

> def _verifier_passed(result: VerifierResult | None) -> bool:
>     if result is None or not result.rewards:
>         return False
>     reward = result.rewards.get("reward", 0)
>     try:
>         return float(reward) >= 1.0
>     except (TypeError, ValueError):
>         return False
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

Final verification is separately invoked after agent execution unless config.verifier.disable; interim continuation code does not consult that flag. Thus disabling final verification does not disable interim checks for this selected continuation path. Final verifier timeout retries twice; arbitrary parse/runtime errors propagate to trial exception handling. SRC-1 `harbor/src/harbor/trial/trial.py:1184-1216,2038-2058`.

Verification and selected artifact transfer. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:585-604,1174-1216,1279-1331,1359-1528`. Shared verification uses existing environment; separate verification creates a fresh environment per pass, transfers configured artifacts at their source paths, then tears it down. The selector is automatic at verification, with configured source-path identity as input; no semantic selection or content budget is present. Implicit artifacts are copied for non-mounted targets, otherwise shared via mount. Agent-log mount omission does not prohibit an explicitly configured trajectory artifact. Verifier reads its output reward files on request. Final verification is invoked separately when enabled: SRC-1 `harbor/src/harbor/trial/trial.py:2051-2062`.

>         Always copies (explicitly) every artifact in
>         ``task.config.artifacts + self.config.artifacts + step_cfg.artifacts``
>         from the agent env to the verifier env at the same in-container
>         path. Configured artifacts are explicit user intent, so paths under
>         ``/logs/agent`` (e.g. trajectories) are honored — they're not
>         filtered out.
> 
>         The implicit ``/logs/artifacts`` transfer is only needed when the
>         target env is non-mounted; when both envs bind-mount the same host
>         directory (Docker), the artifacts are already visible to the
>         verifier via the shared mount.
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

RTE-4 — Derived feedback and later invocation. Same-conversation mode constructs a binary rejection with phase/time and calls resume. Restart mode reads migration_details.json failure or truncatedJSON, else reward.txt, else generic failure text; it inserts this feedback alongside original instruction before another run. This is live source behavior, despite binary-only default claims in CLM-1. No HB_VERIFIER_FEEDBACK_MODE gate is present on this read/format branch. Source-wired; activation/benefit unobserved. SRC-1 `harbor/src/harbor/trial/trial.py:245-297,1127-1140`.

>                 phase += 1
>                 if same_conversation:
>                     instruction = _format_same_conversation_rejection(
>                         phase=phase,
>                         remaining_sec=max(0, int(remaining)),
>                     )
>                 else:
>                     feedback = _read_verifier_feedback(self._trial_paths.verifier_dir)
>                     instruction = _format_continue_instruction(
>                         base_instruction,
>                         phase=phase,
>                         remaining_sec=max(0, int(remaining)),
>                         feedback=feedback,
>                     )
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

On interim timeout, it still constructs failure/continue text, with detailed timeout notice in restart mode. An infrastructure timeout is therefore not a proven failed solution; wording should not upgrade its meaning. The loop permits revisions to artifacts, but no content-directed theory criticism or comparison of improved capacity is required.

Feedback selection and delivery. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:245-297,1091-1140,952-967`. Harness pulls retained host diagnostics only for restart; it returns a nonempty failure string without length cap, else pretty JSON limited to 4000 characters, else raw reward text without length cap, else a fixed fallback. Continuation pushes the resulting latest guidance into `instruction` or `user_prompt` automatically. Same-conversation pushes only the binary-derived template. The remaining time is captured before interim verification; it is approximate and may overstate the later available time. No general token budget or semantic relevance selector is implemented.

> def _read_verifier_feedback(verifier_dir: Path) -> str:
>     details_path = verifier_dir / "migration_details.json"
>     if details_path.exists():
>         try:
>             data = json.loads(details_path.read_text())
>             failure = data.get("failure")
>             if isinstance(failure, str) and failure.strip():
>                 return failure.strip()
>             return json.dumps(data, indent=2)[:4000]
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

>     reward_path = verifier_dir / "reward.txt"
>     if reward_path.exists():
>         try:
>             return f"Verifier reward: {reward_path.read_text().strip()}"
>         except OSError:
>             pass
> 
>     return (
>         "Verification failed. Continue fixing the migration until all verifier "
>         "gates pass or the agent timeout elapses."
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

RTE-5 — Verifier visibility control. Shared Linux mode scans /proc for tmux descendants, sends STOP before interim verification and CONT afterward. Errors log warnings; signal script suppresses per-process kill errors. Separate mode and non-Linux return without this signaling. Cleanup resets tests directory; it clears/recreates verifier logs only for named ephemeral providers daytona/e2b. Other providers warn that bind-mounted logs cannot be cleared without destroying results. No universal isolation or fail-closed guarantee follows. Source-wired best effort. SRC-1 `harbor/src/harbor/trial/trial.py:81-114,625-687,1086-1122`.

>         if provider in _EPHEMERAL_LOG_PROVIDERS:
>             remove_dirs.append(env_paths.verifier_dir)
>             create_dirs.append(env_paths.verifier_dir)
>         else:
>             self._logger.warning(
>                 "Provider %r may bind-mount %s; grader logs cannot be cleared "
>                 "without risking result destruction.",
>                 provider or "<unknown>",
>                 env_paths.verifier_dir,
>             )
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

Default agent mount list includes verifier logs as well as agent logs/artifacts. Separate verifier omits agent-log bind, but the selected default agent mount function still includes verifier-log host path without checking separate mode. Thus a separate environment alone does not prove agent invisibility of verifier results on mounted providers. Custom additive agent mounts are also allowed; verifier environment excludes those additive mounts. No claim of exploited leakage is made. SRC-1 `harbor/src/harbor/trial/trial.py:1279-1331,1360-1394`.

>         base: list[ServiceVolumeConfig] = [
>             ServiceVolumeConfig(
>                 type="bind",
>                 source=self._trial_paths.verifier_dir.resolve().absolute().as_posix(),
>                 target=str(env_paths.verifier_dir),
>             ),
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

Grader visibility maintenance. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:83-114,625-686,1086-1122,1279-1331`. Shared mode requests STOP/CONT on Linux tmux descendants, not all environment processes. Tests are reset; verifier logs are reset only for the recognized ephemeral providers. Other providers retain logs to avoid destroying mounted results. Exceptions are logged and continuation proceeds; reset/exec interfaces do not establish provider-level guarantees. Separate mode bypasses shared scrub/signalling, yet default agent mounts include the verifier host directory. There is no wired blanket promise that separate mode hides that mount from the agent.



RTE-6 — Retain/finalize. Trial stores configuration/result metadata, agent metrics/rollout details, exception messages, downloaded logs and configured artifacts. After execution it populates agent context from agent logs when supported, runs final verification and collects artifacts; errors/cancellation still attempt collection. Cleanup shield-stops environment with configured delete flag then writes result JSON and invokes END hooks. Some cleanup failures are warnings/exception metadata. Source-wired retention; next trial does not automatically receive these records on inspected route. SRC-1 `harbor/src/harbor/trial/trial.py:182-232,1218-1270,2001-2105`.

Final retention and cleanup. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:1218-1269,1781-1798,1833-1909,1990-2105`. Logs are collected or made host-readable, empty context may be populated by an external installed-agent helper, generated logs may be uploaded for final verification, artifacts are collected, environment stop honors configured deletion, and result JSON is written. Artifact copies/manifests and results are operator/debugging output; later cross-task agent adoption is not wired in this boundary. Retained result JSON is not evidence that all conversation contents survive or that all downloads succeed.

>         self.result.finished_at = datetime.now(timezone.utc)
> 
>         self._trial_paths.result_path.write_text(self.result.model_dump_json(indent=4))
> 
>         await self._invoke_hooks(TrialEvent.END)
> --- `harbor/src/harbor/trial/trial.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

RTE-7 — Trace-transformation route, refining OBJ-4 and RTE-4. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:245-297,1091-1140,943-968`. Raw input is the current verification outcome/timeout event, optional retained diagnostics and phase/time state. Automatic formatter writes a derived continuation instruction, retains it beyond the verifier invocation in the loop variable, and a later phase delivers it to the named agent run/resume consumer. This satisfies the method's trace-fed continuation-context rule: retention spans attempts within one task; disk persistence is not required by that rule. Same-conversation, restarted rejection and timeout alternatives are all included. Immediate non-pass reason is retained and supplied; causal explanation of the failure is optional/absent, and reason activation remains unobserved. There is no automatic criticism and revision of a retained explanatory theory demonstrated here, so this classification does not establish conjectural learning.



### Claims

CLM-1 — Docs claim binary rejection by default, no verifier-derived details, process freezing and cleared shared mounted diagnostics (SRC-2 `README.md:27-59`; `harbor/README.md:27-45`). Status: claimed. Bundled source supports same-conversation binary messages and conditional best-effort freezing/cleanup, while restart feedback and mounted log paths have narrower guarantees. This result assesses bundled harbor/src code, not historical patches or newer drop-in module; no claimed equivalence between them.

> - `HB_VERIFIER_FEEDBACK_MODE` defaults to `binary`. The maintainer-only
>   `diagnostic` mode restores detailed feedback for debugging, but those runs are not
>   benchmark-comparable.
> - The agent is frozen during every interim pass. Separate verifiers do not expose
>   their log mount to the agent; shared mounted verifiers snapshot diagnostics to a
>   host-only phase directory and clear the live mount before thawing.
> --- `harbor/README.md` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

### Evidenced absences

ABS-1 — Bounded absence of observed faithfulness evidence. Conclusion status: absent. SRC-1 `harbor/tests/unit/test_continue_until_timeout.py:14-77` and `harbor/tests/unit/test_trial_same_conversation.py:11-36,59-129` contain static assertions about thresholds, formatting, context reuse and calls with fake agents. These tests were not run and do not test a real agent's dependence on recalled content. No retained runtime probe was provided within the authorized evidence boundary. This does not claim that the repository or its authors have never tested anything elsewhere.

>     async def resume_after_verifier_rejection(self, *, user_prompt, context):
>         self.resume_calls += 1
>         assert context is self.initial_context
>         assert user_prompt.startswith(
>             "Your submitted solution did not pass verification."
>         )
> --- `harbor/tests/unit/test_trial_same_conversation.py` @ `d78f5eb52ad754c5ee9154741af73130a85a65b8`

### Behavioral-authority paths

BAP-1 — Continuation instruction or resume user_prompt directs supplied agent to continue within same environment. System/user prompt placement inside concrete agent is uninspected. Force is instruction at scheduler/agent interface, horizon later phase; whether content changes reasoning is unobserved. Guidance authority at the agent interface. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:270-297,952-967` delivers generated text as task instruction or user prompt. Force at the interface is instruction, not a binding rule that the model must obey. A restarted diagnostic payload enters that instruction without an inspected escaping, provenance-separation or adoption review layer. Actual model interpretation is uninspected.

BAP-2 — Reward key/time/phase/termination metadata guide scheduler gating, artifact paths guide transfer, and config selects modes/users. Executable validation/routing applies at these exact consumers; oracle numerical acceptance is not general epistemic authority. Scheduler acceptance and route authority. Implementation conclusion status: wired. SRC-1 `harbor/src/harbor/trial/trial.py:235-242,872-878,918-941,1074-1084,1124-1125`. Reward at least one determines success; task flag, timeout and agent termination metadata gate routes. These structured values enforce scheduling and validation rather than confer epistemic warrant on a proposed explanation.

## Runtime account

Caller selects task/config and Trial.create loads it; Trial.run writes config, starts environment, healthchecks and sets up agent. Initial agent run produces workspace changes and context metadata. In continued single-step mode, the scheduler invokes interim verifier on completion, restores user state and attempts cleanup/thaw, checks reward and either stops or delivers derived feedback for another invocation. It then performs separate final verification/collection/cleanup, returns TrialResult and retains result/log artifacts. Selected external task verifier supplies the outcome test; correctness of its assertions and environment isolation is not independently observed.

Static forcing cases: same-conversation without resume API fails early; reward absent/nonnumeric fails completion gate; interim timeout generates continuation if later budget permits; shared visibility cleanup failure warns and resumes; final verification disabled still permits interim; mounted provider retains a verifier-log mount. No dynamic check planned. A container/model run is unnecessary to establish these branches and would not prove all task verifiers or providers safe. No dependencies/services/credentials were used.

Capability surface includes delegated agent execution, arbitrary task verifier shell, environment file transfers and configured hooks. Grants come from caller/task config, default user and provider; no internal human approval guards every shell change. Sandbox and agent/provider safety are external implementation/deployment contracts. Shared verification explicitly mutates same environment; separate transfer is an alternative with a distinct evidence interface. Multi-step/processreward modes and newer patch module are excluded functional systems, not silently folded into this guarantee.

Revisions: external agent proposes artifact changes; task verifier provides an independently supplied outcome criterion, scheduler decides stop/resume, and budget can veto further attempts. No selected route compares agent variants or installs new harness machinery. Instructions urge self-checking, but whether they express an operative formulated theory, formulate content criticism, revise reliance or improve future capacity is uninspected for concrete agents. Bounded trial experiments do not imply open-ended autonomous improvement.


| Route | Immediate return and later consumer | Selection, expiry, visibility and effect limits |
|---|---|---|
| RTE-1 | Environment/agent/context ready, then first run | Static config/task selects; no accumulated cross-task import; setup errors terminate/retry as stated |
| RTE-2 | Phase context and artifact effects; scheduler then possible next agent call | Task flag/time/reward/termination; latest phase input replaced; shared environment exposed, actual conversation semantics excluded |
| RTE-3 | Parsed reward; scheduler and optional feedback | Current host filenames/configured artifact source paths; freshness external, transfer best effort; no universal secrecy |
| RTE-4 | Derived instruction; next run/resume | Latest rejection/timeout and diagnostic fallback; variable replaced next failure; no guaranteed activation, arbitrary diagnostic cap gaps |
| RTE-5 | Process/directory state change; subsequent work | Mode/platform/provider controls coverage; reset/signalling best effort; no semantic memory invalidation established |
| RTE-6 | TrialResult and retained files; operator/hook | Configured artifact/log destinations, deletion config; later agent ingestion outside boundary; cleanup may fail |
| RTE-7 | Outcome-derived guidance retained beyond verification for next agent call | Per-task phase/time, coarse latest event; reasons sometimes retained, reason activation unobserved; no cross-task horizon |

## Lens scoping

### Memory/context scope

Full lens: cross-phase workspace persistence, context aggregation/resume contract, feedback construction and verifier-artifact visibility are consequential. Include restart/same-conversation, shared/separate, single-shot comparator; omit processreward, multistep, concrete agent/provider/task internals. Passive host telemetry must remain distinct from later model consumption.

### Epistemic scope

Full lens on externally supplied verifier authority and artifact acceptance, feedback-as-evidence, revision permission and leakage bounds. A test outcome can warrant a bounded acceptance without proving a theory of the solution or improved agent capability.

## Lens outputs

### Memory/context lens


Acquisition happens when the agent changes environment files, supplies context fields, and the verifier produces reward/log artifacts. Exact internal production of project content and explanations is excluded. The orchestrator automatically compiles metrics and snapshots/copies selected artifact files; these operations preserve measurements or bytes, not new semantic claims. It then transforms a current failed verification event into OBJ-4. The output is retained for the next attempt and may be replaced on the next failure. No all-phase explanatory memory store or semantic adoption editor is exposed.

RTE-7 is the qualifying transformation: event and optional diagnostic files → derived continuation text → later run/resume input. Both normal rejection and verifier timeout produce that route. Same-conversation does not preserve diagnostic reasons; it preserves only the rejection reason for continuing. Restart includes a failure string when present, but can instead carry arbitrary serialized diagnostics or generic fallback. No route is observed to use those reasons for diagnosis; only delivery is established. The instruction variable survives across attempts within one Trial task, which establishes per-task online scope without relying on a session identifier.

Withdrawal here is principally visibility control in RTE-5 and environment cleanup in RTE-6. Deleting copied tests or hiding logs is not automatically semantic invalidation, decay or forgetting of a learned memory. Metric summation and rollout concatenation are likewise not evidence of memory consolidation. Opaque project edits prevent a complete curation classification.



The named harness consumer pulls host feedback files and parsed reward data. The scheduler automatically supplies derived feedback to the next agent call without an agent request; this is push. It selects the current outcome, so the signal is coarse. Configured artifact paths select precise retained files for automatic transfer to the verifier, supporting identifier-based push; those are identity selectors, not a claim that every pathname is an index. Shared filesystem availability alone is neither a demonstrated agent pull nor automatic context supply.

Same-conversation supplies one shared context object to the optional resume method; this is interface delivery, not proof that its rollout records represent or restore conversation history. Restart supplies fresh per-phase context while retaining the same environment and agent object. Finalization can upload generated agent logs for verification, but no concrete task-specific log-reading behavior is inferred. Operator result availability supplies no later agent retrieval route.

The only explicit feedback content cap is the 4000-character serialized-JSON fallback; failure strings, reward text and original task instruction are not bounded there. The elapsed-time deadline bounds execution, not context volume. Same-conversation context budget, history trimming and model activation are outside scope.



Known axis sets cover the visible orchestration boundary. Storage is files plus in-memory state; the externally provided model/provider stores are excluded. Write agency is automatic for the scoped writes. Direction combines requested harness reads with automatic supply to agent/verifier; selection combines coarse current-event guidance with configured file identity. The final comparison must retain these consumer distinctions rather than call all persistence retrieval.

Representation, lineage, authority and curation remain not-determinable where the included project/diagnostic/metadata payloads are opaque. Visible symbolic wrappers do not resolve those payloads. RTE-7 establishes trace learning under the method's deliberately broader operational definition, not a claim of learning new facts, model training, theory formation or improvement. Its source is verification event data, scope per-task and timing online across all qualifying alternatives. Distilled form remains not-determinable across diagnostic branches because arbitrary embedded content may accompany the known natural-language template. Raw rollouts alone do not qualify as another learning route. ABS-1 supports faithfulness tested = no within this evidence set; test names do not supply an observed result.


### Epistemic lens

1. Boundary: bundled single-step scheduling at frozen commit; no actual candidate artifacts, test outcomes or model actions observed. CLM-1 claims binary-only/isolated feedback, with source-supported qualifications on RTE-4, RTE-5.

2. Objects: workspace artifacts can encode executable solutions, plans or opaque data; their formulation/semantic content uninspected. Verifier reward is an assertion produced by task-authored checks, with numerical operational authority. Diagnostic text and continuation prompt can convey criticisms but this generic code does not establish what claim any diagnostic refutes. AgentContext metrics are not an epistemic record merely because they are retained.

3. Authority ledger:

| Function | Architectural status | Candidate/evaluator/admission | Warrant limit |
|---|---|---|---|
| RTE-1, RTE-2 agent run | implemented delegation | external agent proposes artifact revisions | actual formulated theory/internal criticism uninspected |
| RTE-3 verifier | implemented | task-author tests inspect candidate environment/artifacts | test relevance, coverage and truthful isolation outside selected evidence |
| RTE-2 stop gate | implemented | reward>=1.0 grants phase completion | scalar acceptance is no proof of all requirements or improved capacity |
| RTE-4 feedback | implemented | outcome/diagnostic transformed to later instruction | binary rejection carries no specific refutation; timeout is not candidate failure proof |
| RTE-5 evidence interface | implemented best effort | prevent grader access through selected process/paths | incomplete path/platform coverage; no universal hidden-oracle guarantee |
| RTE-6 retention | implemented | result/log/metrics retained for operator | retention alone adds no candidate warrant or agent readback |

4. Lifecycle: artifact proposal→external check→stop/resume is implemented; actual candidate state no instance observed. Whether artifact expresses an ampliative conjecture and whether a failed check criticizes its content are uninspected. Supplied tests are an answer oracle only in their task-defined domain; they may assess concrete outputs without explanatory theory. No attributable increase in future capacity was measured. Same artifact being revised after rejection does not alone establish conjectural learning.

5. Claim comparison: source supports continued work and an operational external test, but the claimed binary-only default does not cover restart path. Provider-specific cleanup and mounts narrow isolation. Source comments about historical leakage are reported claims and are not reproduced experiments here.

6. Bounded conclusion: an outcome-gated continuation harness whose epistemic strength depends on task-test validity and evidence separation. Distinguish mechanical acceptance from trustworthy candidate warrant and capacity improvement; no system-wide grade is assigned.

## Reconciliation

Verified complete report identity, frozen pin/input/method and report hash above. Mapped MEM-RTE-1 → RTE-7; MEM-ABS-1 → ABS-1. RTE-7 refines the trace transformation in RTE-4 without reassigning its identity. All seven integration issues adopted: trace-fed per-task online instruction route preserved separately from conjectural learning; faithfulness negative bounded to commissioned evidence; binary-only documentation conflicts with restart source; cleanup/provider/mount coverage remains qualified; context is opaque metrics/output, not proved conversation; project/diagnostic representation, lineage, authority and curation remain uncertain; acceptance reward and feedback use different file precedence without synchronized-phase freshness guarantee. Coordinator independently found source/docs and conditional-cleanup differences; independent convergence does not strengthen evidence beyond wiring. No substantive conflict remains.

## Bounded synthesis

The strongest supported contribution is a repeatable opportunity to revise artifacts under an external verifier and bounded time, with source-visible feedback and persistence choices. It does not make early agent self-completion authoritative. Its source/documentation mismatch and conditional grader controls materially constrain what a benchmark result from this exact bundle would mean.

Conjectural learning and self-improvement each remain uninspected: repeated trials and retained feedback do not establish an operative theory criticized for content with improved future capacity. Reflection is wired narrowly where the scheduler records phase/time/context termination state and changes its continuation behavior; a reflective theory builder is not established. Concrete candidate/verifier traces, feedback-activation experiments and provider-specific isolation/fault checks would change distinct conclusions.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence needed |
|---|---|---|---|---|
| Concrete agents/providers/tasks excluded | CMP-2, CMP-3 | interfaces only | exact models, conversation semantics, oracle validity or deployment isolation | pinned implementations and candidate-linked traces |
| Cleanup is conditional/best effort | RTE-5 | Linux tmux and provider-specific dirs | universal grader secrecy | platform/provider failure and exposure tests |
| Source/docs differ | CLM-1, RTE-4 | bundled live trial code | advertised binary-only default | corrected executable path or distinct pinned module analysis |
| No dynamic evidence | RTE-2, RTE-3 | static calls/gates | benchmark benefit, faithful feedback activation, improved capability | controlled retained runs |
| Diagnostic freshness | OBJ-3, RTE-3, RTE-4 | reward and feedback precedence differ; no universal pre-pass host purge | synchronized immutable phase history | task-writer/provider freshness evidence |
| Opaque memory payloads | OBJ-1, OBJ-2, OBJ-4 | arbitrary project/metadata/diagnostics | complete form, lineage, authority or curation set | concrete payload and consumer inspection |

## Verification and blockers

### Semantic verification

Checked selected configuration excludes processreward/multistep; restart/same-chat and shared/separate alternatives retained; completion gate/oracle/timeout distinctions; final-verifier-disable boundary; feedback and mount guarantees against live code, not README abridgment. All seven routes/four objects integrated; static task text excluded from accumulated-memory claim. Read-back pull is harness-requested reward/diagnostic reads, coarse push is latest derived rejection guidance, identifier push selects configured artifact.source paths at verification and supplies files to the verifier. Environment availability does not prove agent pull. RTE-7 qualifies trace learning from verification events to later instruction: per-task, online, event-streams; opaque diagnostic payload prevents complete distilled-form set. Raw metric/rollout aggregation is not substituted as another learning route. No training, formulation, criticism, activation or improvement inferred from that axis. Profile accounts for restart/same-conversation and shared/separate alternatives; unavailable concrete internals and included opaque payloads retain explicit uncertainty. ABS-1 concerns supplied evidence only; no repository-wide absence claim.

### Deterministic validation

Full result validation and guarded pinned-source quotation/anchor checks follow integration.

### Blockers

none
