---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LHTB workflow account: LangChain migration from terminal task delegation through isolated grading, rejection, repair and persisted delivery."
run-id: AAS-2026-10-15-lhtb-a0548ba4edbf-01
reviewed-boundary: "7ca0cacea9bf6a0694eaad7306bed794eaaaabce"
---

# LHTB workflow report

## Workflow account

### Selection and evidence

The representative workflow is the single-instruction `langchain-version-migration` task executed by Terminus-2 through the bundled Harbor trial loop. It is representative because it connects an explicit multi-part work product, terminal execution, a declared artifact boundary, independent grading and continued repair. “Multi-step” here means successive migration, checking and repair actions, not Harbor's separate `task.has_steps` branch. The task ships a single instruction and enables continuation; the solver chooses its own action sequence. This is not a multi-agent planning team.

The account uses SRC-1 at the [frozen boundary](boundary.md#boundary-and-evidence). Additional implementation inspection covers `tasks/langchain-version-migration/{task.toml,instruction.md,tests/test.sh,tests/test_outputs.py}` and the continuation, artifact-transfer and finalization portions of `harbor/src/harbor/trial/trial.py`. The test file was inspected selectively: reward construction, sequential gate progression, replay comparison, memory follow-up and final API gate. Helper correctness, every dynamic-config assertion, image contents and execution remain uninspected. The instruction is doctrine/design evidence; the launcher, grader and trial supply implementation evidence. Nothing here establishes an executed migration, reliable repair or comparative benefit.

### Request and delegation

An operator selects the task, agent, environment and budgets through the job configuration. The shipped full-suite caller includes the original task root and selects Terminus-2; job-to-trial scheduling is established by [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution). This trace follows that agent/task combination, not a claim that the example was run. The task's own timeout is 5,400 seconds; the full-suite example can override it to 10,800 seconds. The effective budget therefore belongs to resolved launch configuration, not solely the instruction (SRC-1, `tasks/langchain-version-migration/task.toml`, `configs/examples/full_benchmark_2.0.yaml`).

The task author delegates migration of `/app` to the solving agent. The supplied instruction names the target version, offline wheelhouse, metadata, modern APIs, stable CLI/API behavior, replay compatibility and dynamic configuration requirements. It supplies helpful commands, not an enforced execution plan. The task requests `langchain==1.3.4`, preserved multi-turn behavior and modern agent construction; these are workload requirements, not capabilities of Harbor itself (SRC-1, `tasks/langchain-version-migration/instruction.md`).

> Inspect
> the installed packages and project metadata, then migrate to the target runtime
> while preserving CLI/API behavior and replay compatibility.
> --- `tasks/langchain-version-migration/instruction.md`

Harbor sets up and health-checks the environment, then hands task text and environment access to the selected agent. Terminus-2 formats the task with terminal state; the model proposes commands, while parser/tmux code executes them and returns observations. This handoff grants operational workspace access, not a restricted migration API. No per-command human gate is wired in the inspected loop; failed commands or later edits need not undo prior mutations. See [RT-OBJ-task-instruction](runtime.md#rt-obj-task-instruction) and [RT-RTE-terminal-actions](runtime.md#rt-rte-terminal-actions).

### Work, completion and verifier handoff

The solver can inspect, edit, install from the wheelhouse and run its own checks. Source wiring does not establish that it actually follows the suggested order. Long interactions can replace model-visible history through summarization or overflow recovery; [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) establishes that context handoff, not faithful preservation of every migration constraint.

The model's confirmed completion ends an agent phase, not necessarily the trial. With continuation enabled, Harbor owns the decision to grade and resume. In same-conversation mode, ordinary interim grading requires `confirmed_task_complete`; other termination reasons break that loop. With default restarted phases, Harbor calls `run()` again after rejection and Terminus-2 creates a new Chat. Files survive in the same agent environment in either case, but conversation retention differs. These alternatives are established by [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation).

The migration task selects separate verification. Harbor creates a verifier environment and transfers declared metadata, source, configs, prompt registry, data and replay-output paths at their original container locations, plus the convention artifact channel. It does not clone arbitrary installed state from the solver environment. Transfer errors warn rather than proving submission completeness; the task launcher separately rejects missing required paths. See [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution) and [WF-RTE-migration-grading](#wf-rte-migration-grading).

This distinction matters for acceptance: the verifier reinstalls the submitted metadata and source in its own environment. An agent-side dependency installation alone cannot satisfy that reconstruction. Conversely, the inspected launcher checks the verifier's reconstructed active environment, not directly the solver's live installed environment. It deletes transferred replay output before recomputing results. The submitted replay file is therefore not the answer oracle.

### Rejection and repair

The task-owned grader compares reconstructed behavior with fixtures and programmatic checks. Harbor consumes its reward; the continuation predicate accepts `reward >= 1.0`. Sequential gate failures can retain partial reward, but do not satisfy that predicate. A first failing gate stops the inspected test progression, so its partial reward is not a complete diagnosis of all remaining defects. The task author supplies reference outcomes; code decides pass/continue; the model chooses repair actions. No human adjudication of each rejection is required. See [WF-RTE-migration-grading](#wf-rte-migration-grading).

The instruction promises isolated grading with binary rejection. That promise is not universal over the bundled implementation. Same-conversation mode constructs a fixed rejection turn, retaining Chat and tmux. Default restarted mode reads `migration_details.json` or scalar reward and appends feedback to the original instruction. Thus the task text alone does not establish a diagnostic-free run. This discrepancy is already bounded by [RT-CLM-grader-isolation](runtime.md#rt-clm-grader-isolation); it is not resolved by the existence of a differently hardened drop-in runtime.

A source-supported failure path is an offline installation failure: the launcher writes zero reward and a setup failure message. If grading returns normally, Harbor rejects that outcome; with time remaining, it resumes or restarts the agent according to mode. A verifier timeout has its own trial handler that supplies another continuation instruction. Prior workspace mutations remain available for repair; neither branch restores a known-good submission. Process freezing, user restoration and hiding grader outputs are trial responsibilities, with the bundled isolation limits stated in the runtime member (SRC-1, `tasks/langchain-version-migration/tests/test.sh`, `harbor/src/harbor/trial/trial.py`; [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation)).

### Delivery and exhaustion

An interim full pass breaks continuation, but the outer single-task path still performs final verification unless disabled. Agent timeout or nonzero exit is recorded and can likewise lead to final verification of the current workspace. Other errors can instead reach exception finalization. Therefore a completion signal, interim pass, final reward and persisted trial are distinct events (SRC-1, `harbor/src/harbor/trial/trial.py`).

> if not self.config.verifier.disable and not self._task.has_steps:
> --- `harbor/src/harbor/trial/trial.py`

Delivery at the harness boundary is a returned and persisted TrialResult with rewards, errors, timings and artifact locations, after attempted collection and cleanup; it need not be a successful task result. Artifact collection is best effort, so persisted metadata does not certify a complete exported project. Completed outcomes can later enter job aggregation/reconciliation, whereas an interrupted model conversation is not restored by job restart. See [RT-OBJ-trial-result](runtime.md#rt-obj-trial-result), [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution) and [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery). No observed run closes the gap between this source-supported delivery protocol and successful migration.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-migration-grading
Label: Migration reconstruction and grading

Part of: [RT-RTE-verifier-execution](runtime.md#rt-rte-verifier-execution)

This is the task-specific reconstruction and answer-checking part of the generic verifier route, not a second declaration of Harbor's verifier transport. Its endpoints are transferred `/app` project paths and the reward/details files consumed by Harbor. Task-authored shell/Python code owns reconstruction, checks and reward writing. Its symbolic rules consume source, metadata, fixture records and computed outputs; task text guides the solver separately. SRC-1 implementation evidence: `tasks/langchain-version-migration/tests/test.sh`, `tasks/langchain-version-migration/tests/test_outputs.py`; submission selection is declared in `tasks/langchain-version-migration/task.toml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reward text plus migration-details JSON, or launcher failure with zero reward; Harbor parses the reward into a VerifierResult.
- Later read-back: Saved rewards feed later job aggregation; in restarted continuation the details failure can reach a later solver invocation through the runtime feedback reader. Same-conversation mode instead sends a fixed rejection without these details.
- Delegated visibility: The verifier receives selected project paths and its own test package; the solver's whole environment and Chat are not transferred. Private fixture comparisons occur in the verifier, not in the ordinary solver prompt.
- Selection predicate: The task selects separate verification and declares submission artifacts; the launcher invokes its migration test, which checks gates sequentially and stops on first failure.
- Invalidation or expiry: The launcher removes prior replay output, legacy output and selected package caches, then reinstalls from submitted metadata. Verifier-environment teardown is owned by Harbor; agent workspace edits are not rolled back.
- Activation or effect: Grading writes a numeric reward and details; these can drive another agent phase or termination. No executed repair or semantic benefit is observed.
- Evidence limits: Fixture provenance, exhaustive helper correctness, deployed image contents and successful reconstruction are unestablished. Inspectable comparisons establish an implemented oracle, not scientific validity or immunity to adversarial submissions.

The agent proposes the revised project through workspace changes. The task author supplies expected behavior and the test sequence. Launcher checks reject missing submission paths and failed installation; test assertions reject gate failures; Harbor makes the continuation decision from reward. No per-submission human approval is wired here. This is bounded benchmark evaluation with repair triggered by failed verification, not an update to Harbor's own machinery. Recovery preserves the workspace for another attempt; there is no generic rollback or oracle validating each edit before execution.

> if ! python -m pip install -e . pytest==8.4.1 > /logs/verifier/install.log 2>&1; then
>   fail_setup "offline installation from submitted metadata failed"
> fi
> --- `tasks/langchain-version-migration/tests/test.sh`

> # Never grade stale replay output copied from an old image or an earlier phase.
> rm -rf /app/outputs/legacy
> rm -f /app/outputs/replay_results.jsonl
> --- `tasks/langchain-version-migration/tests/test.sh`

The inspected checks compare answer and routing fixtures, public/private replay outputs, a session follow-up and public API behavior, alongside runtime/source structure gates. They are task reference outcomes, not the model's self-assessment. Gate failure writes fractional progress before raising; successful completion writes one. Partial reward does not contradict the instruction's requirement of all gates for a pass, but it does show that scoring is not limited to binary numbers.

> def _partial_reward(details: dict) -> float:
>     gates = details.get("gates", {})
>     passed = sum(1 for v in gates.values() if v is True)
>     return round(passed / TOTAL_GATES, 4)
> --- `tasks/langchain-version-migration/tests/test_outputs.py`

> details["gates"]["replay_private"] = actual_private == expected_private
> if actual_private != expected_private:
>     _fail(details, "private replay output does not match golden")
> --- `tasks/langchain-version-migration/tests/test_outputs.py`

> details["failure"] = None
> _write_reward(1.0, details)
> --- `tasks/langchain-version-migration/tests/test_outputs.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-verifier-continuation](runtime.md#rt-rte-verifier-continuation)

Workflow role: rejection transfers control back to the solver, not to a separate critic/repair team. Handoff content depends on continuation mode: retained conversation plus fixed rejection versus a new Chat with original task and diagnostic-bearing feedback. Neither handoff restores prior files or guarantees a successful repair. The migration instruction's binary-only promise must therefore be read with this route's implementation-specific limits.

#### On [RT-RTE-trial-execution](runtime.md#rt-rte-trial-execution)

Workflow role: delivery means a finalized outcome at the harness boundary, not necessarily an accepted migration. Interim acceptance does not replace the outer final-verification path. Task-level failure can still yield a delivered result carrying errors and reward; final artifact completeness remains qualified by best-effort collection.
