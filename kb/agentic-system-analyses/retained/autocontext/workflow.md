---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Autocontext workflow account: Python scenario generation from operator request through role handoffs, tournament rejection, persistence and run delivery."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
---

# Autocontext workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a bounded Python saved-scenario run, using the standard generation path rather than tree exploration, RLM or the alternate full role-pipeline engine. It is selected because it connects the shipped operator entry, multiple model roles, executable evaluation, rejection/retry, retained artifacts and terminal delivery within one source-supported chain. The referent is already declared as [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation); this member adds workflow-specific findings rather than allocating another identity.

Evidence is static implementation in SRC-1 at the revision fixed by [the boundary](boundary.md). No target command, model call, test or scenario was executed, and no archived result was inspected. Implementation is wired; operation remains uninspected. This workflow does not represent all product surfaces: the npm loop, task-output revision, training and kernel campaigns have different policies, as the runtime member explains. In particular, generating a role report is not evidence that its advice was correct or improved later behavior.

Added inspection covers SRC-1, `autocontext/src/autocontext/agents/orchestrator_helpers.py` (role dependencies and output assembly), `autocontext/src/autocontext/loop/stage_helpers/tournament_prep.py` (retry handoff), `autocontext/src/autocontext/harness/pipeline/gate.py` (score-delta decision), and `autocontext/src/autocontext/loop/tournament_helpers.py` (accepted state update). It also checks ordering, review, persistence, exception handling and terminal output in `autocontext/src/autocontext/loop/generation_pipeline.py`, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/loop/generation_runner.py` and `autocontext/src/autocontext/agents/orchestrator.py`. These are implementation evidence within the existing registered source, not an additional source or observed run.

### Request, scheduling and delegation

The operator's saved-scenario request supplies the scenario and iteration bound. The CLI resolves it and invokes the runner; run setup and reentry are established by [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation), SRC-1, `autocontext/src/autocontext/cli.py` and `autocontext/src/autocontext/loop/generation_runner.py`. The runner, not a foreground model, schedules generations. It passes a generation context to the pipeline and carries returned score, rating, narrative and hints forward. Run identity and generation index associate role output, matches and recovery records.

Knowledge setup precedes role dispatch and active-context routing. Selected playbook, tools, lessons, prior analysis, trajectory, scenario contract and observations enter role prompts; ablation and budget controls can remove material. [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) supplies the context-delivery evidence and limits. This handoff is selected context, not the complete stored corpus or a guarantee about the external host's conversation state. SRC-1, `autocontext/src/autocontext/loop/generation_pipeline.py` and `autocontext/src/autocontext/loop/stages.py`.

The orchestrator first obtains competitor text, then translates that text to the strategy mapping consumed by execution. Only after translation does it dispatch the support-role helper. SRC-1, `autocontext/src/autocontext/agents/orchestrator.py`. The executable strategy boundary is [RT-OBJ-strategy](runtime.md#rt-obj-strategy); generated prose is not itself the ordinary tournament input.

The support-role dependency is explicit: the coach receives this generation's analyst output, added to its own prompt. The non-RLM helper uses a feedback DAG with at most two workers; architect execution is cadence-controlled. SRC-1, `autocontext/src/autocontext/agents/orchestrator_helpers.py`:

> if role == "coach":
>     user, system = _coach_turn(prompt, completed["analyst"].content)
> --- `autocontext/src/autocontext/agents/orchestrator_helpers.py`

> results = PipelineEngine(feedback_dag(), run_role, max_workers=2).execute(
>     {"analyst": prompts.analyst, "coach": prompts.coach, "architect": architect_prompt},
>     on_role_event=notify,
> )
> --- `autocontext/src/autocontext/agents/orchestrator_helpers.py`

Output assembly parses role returns into analysis, playbook, lessons, hints, tool specifications and harness specifications, while retaining role executions. The analyst-to-coach passage crosses back as text, not as a new system-level grant. Crucially, these support roles run before this generation's tournament. They must not be described as reviewing the completed current tournament in this standard path. Later review and persistence consume tournament state separately. SRC-1, `autocontext/src/autocontext/agents/orchestrator_helpers.py` and `autocontext/src/autocontext/loop/generation_pipeline.py`.

### Verification and rejection

After agent generation, the pipeline offers configured repair, leakage, staged-validation, prevalidation, probe and refinement stages before the tournament. These are conditional branches, not mandatory universal checks. The tournament stage delegates execution to the supervisor and obtains a scored evaluation summary. Scenario-specific validation/scoring is the evaluation basis, not a universally correct answer oracle. The gate chooses strategy progression; it does not prove the coach's proposed instruction caused a gain. SRC-1, `autocontext/src/autocontext/loop/generation_pipeline.py`, `autocontext/src/autocontext/loop/stages.py`; see [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation).

For the basic backpressure gate, code compares best-score improvement against a configured minimum. A passing delta advances; insufficient improvement retries while budget remains, then rolls back. This is the basic gate's policy, not an exhaustive account of trend-aware, novelty, cost or holdout adjustments. SRC-1, `autocontext/src/autocontext/harness/pipeline/gate.py`:

> if delta >= self.min_delta:
>     return GateDecision(decision="advance", delta=delta, threshold=self.min_delta, reason="score improved")
> --- `autocontext/src/autocontext/harness/pipeline/gate.py`

In the non-rapid retry path, the tournament stage records a recovery marker and invokes a helper with current strategy, tournament, prior best and attempt count. The helper builds competitor feedback from the failed evaluation, including the improvement threshold, then calls competitor and translator again. It does not rerun the entire support-role sequence. Non-code revisions must pass scenario action validation before replacing the current strategy; code strategies follow a separate branch. Missing agents/prompts or a caught retry exception leave the old strategy in place. SRC-1, `autocontext/src/autocontext/loop/stages.py` and `autocontext/src/autocontext/loop/stage_helpers/tournament_prep.py`:

> except Exception:
>     logger.debug("retry-learning competitor re-invocation failed", exc_info=True)
> return current_strategy
> --- `autocontext/src/autocontext/loop/stage_helpers/tournament_prep.py`

The tournament stage owns retry/backoff and exhaustion, not the model. On rollback, the outcome helper preserves previous best and Elo; only advance changes those fields. This does not restore every file or reverse already executed external effects. SRC-1, `autocontext/src/autocontext/loop/tournament_helpers.py`:

> if gate_decision == "advance":
>     updated_previous_best = max(previous_best, tournament.best_score)
>     updated_elo = tournament.elo_after
> --- `autocontext/src/autocontext/loop/tournament_helpers.py`

### Separate admission and post-evaluation review

Context-candidate evaluation occurs after the tournament and before stagnation handling, controller gate override, optional consultation, skeptic review, curator review and persistence. Therefore the strategy gate is neither the final decision-maker on every retained artifact nor a substitute for context admission. [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) supplies the matched-evaluation, deferred recovery and activation-check evidence. Its incumbent/candidate protocol must not be projected onto all direct writes. SRC-1, `autocontext/src/autocontext/loop/generation_pipeline.py`.

Curator review is itself conditional: it returns without a playbook assessment if there is no curator, feedback is ablated, the generation is not advancing, the proposal is empty or the current playbook is empty/sentinel. When invoked, the curator receives current and proposed playbooks, trajectory, recent analysis and configured harness/skeptic context. It can clear the proposed playbook or replace it with merged content. Rejection can also roll back harness files under the enabled inheritance settings. This is a model-backed quality judgment, not proof of factual or causal validity. SRC-1, `autocontext/src/autocontext/loop/stages.py`:

> if curator_decision.decision == "reject":
>     ctx.outputs = dataclasses.replace(ctx.outputs, coach_playbook="")
> --- `autocontext/src/autocontext/loop/stages.py`

The operator initiates the run and may supply supported controller overrides. Computation schedules ordinary internal calls and gates. These facts do not establish per-edit human approval; configured playbook approval is a separate persistence option. Neither the internal role names nor a successful tournament establish autonomous theory building or the truth of generated lessons; actual explanatory content was not inspected here.

### Persistence, failure recovery and delivered result

Persistence stores match scores, validation errors, strategy JSON and replay data in SQLite, upserts a completed generation, and writes metrics and analyst/coach/architect artifacts. Legacy playbook publication is restricted to advance with no active bundle, and can return pending approval. [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion) retains the exact guard passage. Retained reports and selected guidance can later reach new role calls through [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery); delivery does not establish model reliance. SRC-1, `autocontext/src/autocontext/loop/stages.py`.

A generation can complete with a rollback decision: completion records the attempted workflow, not acceptance of every proposal. Conversely, an exception after partial writes is not an atomic undo. The runner records the generation failed, emits failure, and re-raises. Its final safety net changes a still-running generation to failed/stalled. Retrying a failed generation can first resume pending context evaluation, as established by [RT-RTE-context-promotion](runtime.md#rt-rte-context-promotion). SRC-1, `autocontext/src/autocontext/loop/generation_runner.py`:

> # Post-unwind safety net: if the pipeline exited without
> # persisting a terminal status, mark the generation failed.
> --- `autocontext/src/autocontext/loop/generation_runner.py`

Normal delivery is the runner's returned summary plus durable artifacts and terminal events, not a coach message declaring success. The runner marks a non-stopped run completed and flushes writes. A stopped run does not additionally emit the completed receipt. Terminal receipts count durable completed generations, whereas the returned summary counts generations completed by this invocation. SRC-1, `autocontext/src/autocontext/loop/generation_runner.py`:

> # Terminal receipts report the run's durable progress; RunSummary keeps this invocation's count.
> --- `autocontext/src/autocontext/loop/generation_runner.py`

CLI rendering of the summary is supplied by [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation). This establishes the delivery contract and failure routing in source, not an observed successful delivery, exercised retained-context influence or successful improvement.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-scenario-generation](runtime.md#rt-rte-scenario-generation)

Workflow-specific findings: standard support roles precede the current tournament; the coach receives analyst text through its user/flat prompt. A strategy retry re-invokes competitor and translator rather than replaying all support roles. Basic score-gate rollback preserves incumbent score/rating state, not arbitrary effects. Curator rejection can suppress a legacy playbook proposal without making the generation incomplete. Delivery distinguishes this invocation's summary count from durable terminal progress. The account above retains SRC-1 implementation passages and their bounded coverage; operation remains uninspected.
