---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MerchantBench workflow tracing a queued ReAct store run through action admission, hook release and batch completion."
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
---

# MerchantBench workflow report

## Workflow account

### Selection and evidence

This account selects one queued job using the shipped `react_160k_compact_30k` bootstrap. It follows a complete task boundary: operator configuration, run creation, model-selected store operations, server verification, repeated simulation steps and terminal batch delivery. This is representative because it connects the shipped model-calling baseline to the batch driver's run lifecycle without assuming that an arbitrary submitted image implements ReAct. It does not combine hosted evaluation with batch completion: these are different consumers with different outputs ([RT-RTE-react-loop](runtime.md#rt-rte-react-loop), [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval), [WF-RTE-batch-runs](#wf-rte-batch-runs)).

The [boundary](boundary.md) supplies SRC-1 and the frozen revision. Additional inspection here covered the run-creation, scheduler and CLI completion branches in `scripts/run_batch.py`, the ReAct bootstrap selection/configuration in `env/web/runner.py`, and `_drive_step`, `_force_end_of_step` and `run` in `agent/baselines/react_160k_compact_30k.py`. These are implementation evidence, not observed runs. No target execution, provider call, passing test or empirical reliability result is established.

### Request and responsibility handoff

The operator supplies the queue and optional horizon, seed and parallelism overrides. The batch driver constructs a scenario and a run-creation request containing model selection, seed, bootstrap identity and `auto_start: True`. It receives a run ID, which becomes the status-polling identity. The registry starts progression and selects the ReAct bootstrap under its lifecycle lock. It passes the model selection and scenario horizon to the baseline launcher; the baseline configuration uses a 160,000-token context/compaction trigger and a 30,000-token retained suffix. This is process/task delegation by software, not model-directed sub-agent creation (SRC-1, `scripts/run_batch.py`, `env/web/runner.py`; [WF-RTE-batch-runs](#wf-rte-batch-runs)).

> elif bootstrap_agent == "react_160k_compact_30k":
>     self._spawn_react_160k_compact_30k(
>         run_id, bootstrap_base_url,
>         model=bootstrap_config.get("react_model"),
>         max_steps=int(scenario["run"]["horizon_steps"]))
> --- `env/web/runner.py`

The worker, not the model, owns simulated time. It exposes a decision hook after the simulator's transition. The baseline registers its identity and obtains observations and tool schemas. On first brief delivery it retains the scenario-derived system prompt. Each model request receives that guidance, rendered observation text, selected local history and schemas, not the entire server environment. The model chooses actions; the SDK carries assistant-format calls to the environment ([RT-RTE-react-loop](runtime.md#rt-rte-react-loop), [RT-OBJ-system-brief](runtime.md#rt-obj-system-brief), [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry)). These supplied records retain the supporting source passages. There is no independent planning or review agent on this selected route.

### Verification, feedback and continuation

The consequential verification point is server action admission, not a critic model. `/act` checks liveness, hook state, quota and the step header when supplied; dispatch checks tool grants and argument schemas before handlers perform store operations. Handlers may reject invalid product, price or capacity requests. The proposer is the foreground model; server code can veto execution; the operator does not approve each proposed action. This checks protocol/domain validity, not whether the merchant strategy is optimal. Outcomes feed subsequent observations rather than an expected-action answer key ([RT-RTE-act-gate](runtime.md#rt-rte-act-gate), [RT-CLM-http-controls](runtime.md#rt-clm-http-controls)).

Tool results return to the baseline and are appended to history for another model hop. Accepted listing/pricing changes affect later simulation. Rejection does not establish whole-batch rollback, and replay support is scoped to agent/step/call identity rather than arbitrary repeated intentions. The context-maintenance branch can remove earlier turns; asking the foreground model to save important information is not verified successful preservation ([RT-RTE-act-gate](runtime.md#rt-rte-act-gate), [RT-RTE-context-trim](runtime.md#rt-rte-context-trim)).

### Failure ownership

A concrete rejection path is a stale action: the SDK's step header can cause HTTP 425 after the environment advances. The ReAct client then discards the observation and any newly accumulated hops for that decision turn, returns from `_drive_step`, and re-enters its observation loop. This corrects local context accumulation; it does not roll back earlier accepted environment effects. Headerless clients do not obtain the same stale-step check (SRC-1, `agent/baselines/react_160k_compact_30k.py`; [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)).

> if status == 425:
>     # Stale step: env already advanced. Discard this turn's
>     # messages (observation + any hops) to prevent accumulation
>     # of duplicate observations on re-observe.
>     self.history = self.history[:history_len_before]
> else:
>     self._force_end_of_step(
>         f"[act-error] {type(e).__name__}: {e}"
>     )
> return
> --- `agent/baselines/react_160k_compact_30k.py:706-715`

Provider failure after retries, missing tool calls and exhausted hop budgets instead lead the client to attempt an end-of-step action. The attempt is not guaranteed to succeed: `_force_end_of_step` catches HTTP errors and resets pending compaction state when necessary. The worker has a hook timeout independently of that client fallback. Thus recovery favors releasing a stalled decision window, not proving that the omitted work was completed ([RT-RTE-react-loop](runtime.md#rt-rte-react-loop); SRC-1, `agent/baselines/react_160k_compact_30k.py`).

> except requests.HTTPError:
>     # /act failed (e.g., stale step). Reset compaction state so the
>     # reminder can be re-added on the next step instead of staying
>     # permanently pending and blocking future reminders.
>     if self.compaction_pending:
>         self.compaction_pending = False
>         self._pending_pre_assistant_messages = []
>         self.last_prompt_tokens = 0
> --- `agent/baselines/react_160k_compact_30k.py`

At the outer workflow level, the batch scheduler owns failure reporting. Creation or status-fetch failures stop queue filling and report still-active runs as abandoned; reporting those identities does not itself stop them. Stopped/error run states are recorded as failures. There is no automatic rerun in this inspected scheduler branch; intervention remains with its caller/operator ([WF-RTE-batch-runs](#wf-rte-batch-runs)).

### What counts as delivered

An end-of-step response closes only a decision window. The worker continues simulation and persistence; at the operating horizon or termination it drains outstanding orders without resuming ordinary agent decisions. The baseline exits on HTTP 410 or its configured step limit, but its process exit is not the batch success criterion ([RT-RTE-react-loop](runtime.md#rt-rte-react-loop)).

The batch scheduler accepts a job when status has `phase == "finished"`, provided the earlier stopped/error-state branch has not classified it as a failure. Its programmatic delivery is an input-ordered list of model, run ID and terminal status tuples. The CLI prints progress/dashboard locations and returns zero on aggregate success; it discards that returned list rather than writing a scored result file. If any run fails, `BatchRunError` carries completed results and failures; the CLI prints failures and returns one. Completion therefore establishes a lifecycle result, not successful merchant strategy or a wealth-based acceptance threshold. Hosted scoring is a separate route, not a hidden verification stage of this workflow (SRC-1, `scripts/run_batch.py`; [WF-RTE-batch-runs](#wf-rte-batch-runs), [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-batch-runs
Label: Batch run orchestration and completion

This route connects queue jobs to run creation, bounded parallel scheduling, status polling and caller delivery. Owner: `run_models` and its CLI caller. Endpoints: `POST /runs` and `GET /runs/{run_id}/status`. State is symbolic Python job dictionaries, active-run mappings, ordered result slots and failure lists; scenario/model/seed/bootstrap configuration determines the requested work. Source: SRC-1, `scripts/run_batch.py`, `env/web/runner.py`.

Distinct identity: [RT-RTE-react-loop](runtime.md#rt-rte-react-loop) is the inner decision loop, not the queue scheduler; [RT-RTE-other-clients](runtime.md#rt-rte-other-clients) covers alternate action/progression clients, not ordered batch result collection; [RT-RTE-hosted-eval](runtime.md#rt-rte-hosted-eval) owns Docker launch and scoring rather than this batch driver's result tuples. This orchestration spans launch, inner execution and completion; it is not a material part of exactly one supplied record.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Run creation returns a run ID; the scheduler returns ordered successful tuples only when no failures remain, otherwise raises BatchRunError carrying partial results and failures.
- Later read-back: inapplicable — this branch collects lifecycle results but implements no reuse of completed results to update or select an agent for later execution.
- Delegated visibility: The server receives the constructed scenario, seed, bootstrap identity/model and auto-start flag; the batch caller receives run status rather than model history. The ReAct process receives launch identity/configuration through the registry.
- Selection predicate: Normalized enabled jobs are scheduled while active count is below max_parallel; stopped/error state records failure before the finished-phase success branch.
- Invalidation or expiry: Terminal jobs leave the active mapping; creation/status-request failure stops queue filling and reports remaining active identities without automatically stopping their runs.
- Activation or effect: Run creation and status-based delivery are wired; actual launches, completed simulations and useful merchant decisions remain unobserved.
- Evidence limits: No supplied execution trace. The inspected CLI writes no result JSON and implements no merchant-performance acceptance gate, automatic retry or successor-policy update.

Decision roles: the operator chooses jobs/configuration; deterministic scheduler code allocates slots and classifies lifecycle success/failure. No model critic or human per-result approval is involved in this branch. Operating mode: configured bounded benchmark jobs. Answer oracle: server-reported lifecycle state/phase is used as completion evidence, not as an oracle for correct merchant actions. Recovery after an abandoned active run remains a caller/operator responsibility.

> if status.get("state") in {"stopped", "error"}:
>     failures.append({
>         "index": index,
>         "model": job["model"],
>         "run_id": run_id,
>         "status": status,
>     })
>     completed.append(index)
> elif status.get("phase") == "finished":
>     ordered_results[index] = (str(job["model"]), run_id, status)
>     completed.append(index)
> --- `scripts/run_batch.py`

> raise BatchRunError(
>     f"status request failed for {run_id}; stopped filling the queue",
>     failures=failures,
>     results=[result for result in ordered_results if result is not None],
> ) from exc
> --- `scripts/run_batch.py`

> except BatchRunError as exc:
>     print(str(exc), file=sys.stderr)
>     for failure in exc.failures:
>         print(json.dumps(failure, ensure_ascii=False, default=str), file=sys.stderr)
>     return 1
> return 0
> --- `scripts/run_batch.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-react-loop](runtime.md#rt-rte-react-loop)

Workflow role: owns model-directed work inside each decision hook, not outer batch acceptance. A release fallback is a liveness attempt, not completion verification. Worker progression and later terminal status remain separate handoffs.

#### On [RT-RTE-act-gate](runtime.md#rt-rte-act-gate)

Workflow verification role: software admission may reject a proposed operation, but accepts validity rather than strategic correctness. Tool results supply feedback for another foreground-model hop; they do not constitute an independent review verdict on the completed merchant task.

#### On [RT-RTE-context-trim](runtime.md#rt-rte-context-trim)

Workflow continuity role: history removal limits what crosses between later foreground invocations. Requested optional memory saving is not a mandatory handoff artifact whose successful creation gates continuation.
