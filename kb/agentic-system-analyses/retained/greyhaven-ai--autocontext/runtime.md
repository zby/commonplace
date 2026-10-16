---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Autocontext runtime baseline: scenario generations, task revision, context admission, host execution and model/code improvement at the frozen repository revision."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
---

# Autocontext runtime report

## Runtime account

### Evidence and claimed work

This is static implementation inspection of SRC-1 at the revision in [the boundary](boundary.md). No target command, test, example, provider, service or hardware experiment was executed. No archived run result was inspected. Implementation conclusions below do not establish exercised improvement, reliable model compliance or benefit. The source's central claim is recorded in [RT-CLM-agent-improvement](#rt-clm-agent-improvement).

Autocontext is principally an improvement plane, with several non-equivalent executors and admission policies. Its model calls propose strategies, explanations, instructions and sometimes executable source. Software evaluates outputs, retains artifacts and can change what a later model invocation receives or which local model it uses. The product is not one agent loop with one universal approval or sandbox gate.

### Ordinary shipped invocation

For a saved game-like scenario, Python `autoctx run <scenario> --iterations N` enters `cli.run`. It resolves the scenario, performs preflight unless bypassed, and calls `GenerationRunner.run`. Agent-task scenarios instead take the task route. The CLI can also launch a local interactive server beside the loop; run ID, scenario name, generation index and role identify nested work. The calling operator supplies the task and configuration, not necessarily each proposed edit. SRC-1, `autocontext/src/autocontext/cli.py`.

[RT-RTE-scenario-generation](#rt-rte-scenario-generation) follows the ordinary scenario path end to end. The runner creates or reopens a SQLite run, hydrates score/rating history, seeds scenario tools, optionally restores prior knowledge and enters generations. Knowledge setup constructs a seeded observation and loads context. Role execution generates competitor prose, translates a strategy, and obtains analyst, coach and architect output. Tournament execution supplies scores, validation results and replays; a code gate selects advance/retry/rollback. Retry can call the competitor again with failure context. Candidate context has its own evaluation boundary, followed by stagnation handling, optional consultation/skeptic review, curator handling and persistence. Terminal CLI output is a run summary or JSON containing run identity, generations, score and Elo. SQLite and per-generation artifacts outlive that summary.

The current strategy is a symbolic object at the executor interface, not the model's prose. Scenario-specific executable code is a distinct consumption path. See [RT-OBJ-strategy](#rt-obj-strategy). The decision policies are fixed code plus configured thresholds and model-interpreted instructions; model-backed proposals and curator judgments must not be confused with deterministic validation.

### Forcing cases and guarantee limits

Four selected challenges materially change the interpretation of the ordinary route:

1. **Strategy advance is not context-edit evidence.** Python persistence withholds legacy coach-playbook publication when an active bundle exists. Candidate admission separately evaluates a bundle against its incumbent and can defer the generation. [RT-RTE-context-promotion](#rt-rte-context-promotion) records this scoped fail-closed boundary.
2. **The npm loop is not the same admission policy.** Its support-role path accepts structured coach text through a guard and optional curator, then writes or stages it. The inspected call to support roles is after lifecycle persistence, without a local `advance` predicate. This defeats a product-wide inference that every playbook update has matched-context causal evaluation. [RT-RTE-npm-generation](#rt-rte-npm-generation).
3. **Evaluation limits do not imply universal tool isolation.** Python scenario execution defaults to `LocalExecutor`; executable strategies branch to Monty, while ordinary scenario execution uses process workers with a thread fallback. Direct API, Claude CLI, persistent Pi RPC, local shell workspaces and imported extensions have different boundaries. [RT-RTE-runtime-dispatch](#rt-rte-runtime-dispatch) records the authority differences. In particular, a local workspace's shell fallback is not a grant-only command allowlist.
4. **Parameter changes and machinery changes are shipped paths.** Training revises `train.py`, trains checkpoints and can auto-activate the terminal accepted model. Its deterministic mode uses summary-derived trials; adaptive mode requires a trial executor. Ambient promotion has another policy and rejects placeholder-only evaluation. Kernel evolution uses an independent benchmark decision policy rather than merely maximizing a prompt score. See [RT-RTE-training-experiments](#rt-rte-training-experiments), [RT-RTE-ambient-promotion](#rt-rte-ambient-promotion) and [RT-RTE-kernel-evolution](#rt-rte-kernel-evolution).

These are counterexamples to overly broad guarantees, not evidence that all alternate paths are unsafe or equivalent. Inspected source enumerates direct provider calls, subprocess agents, durable RPC, local shell, imported extension code, scenario workers and remote-executor seams. Provider-native tool internals, enclosing-host permissions, production deployment isolation and individual remote-provider execution protocols remain uninspected. No deployed grant set or isolation envelope was supplied.

### Context, delegation and return

Knowledge setup supplies playbook, tools, lessons, latest analysis, reports, hints, dead ends, trajectory, observations and scenario contract. Feedback ablation removes much of the retained context. A context budget preferentially trims selected components while protecting hints and dead ends; actual prompt assembly can also use semantic compaction. Structural role isolation is conditional: only safe role splits and capable clients receive separate system/user channels, and mutations or hook rewrites can disable the split. Thus neither all retained text reaching a model nor all such text having system authority is established. [RT-RTE-context-assembly](#rt-rte-context-assembly) and [RT-BAP-context-delivery](#rt-bap-context-delivery).

The ordinary orchestrator makes distinct role calls and returns assembled role outputs. Its pipeline alternative uses a role DAG with at most two workers; RLM has a separate branch. This resembles separate call frames with selected inputs and returned outputs, but the analogy is limited: runtime-session wrappers or persistent hosts can retain conversation outside the immediate role frame. The Pi persistent RPC adapter explicitly keeps a child process and disallows concurrent requests. No evidence here establishes host compaction policy, complete delegated context, or automatic destruction of every role's prior state. SRC-1, `autocontext/src/autocontext/agents/orchestrator.py`, `autocontext/src/autocontext/runtimes/pi_rpc.py`.

### Additional shipped surfaces and bounded coverage

All entries below remain inside the whole-system boundary. They are not attributed to an excluded application. This report adds implementation coverage beyond the boundary's initial inspection, particularly executor branches, prompt budgeting, extension loading, training admission and kernel lifecycle. All new paths retain SRC-1; none supplies observed-run evidence.

| Surface | Runtime role and coverage limit |
| --- | --- |
| Plain-language solve | `autocontext/src/autocontext/knowledge/solver.py` dispatches generated scenarios by interface: agent tasks and artifact editing go to task-like execution; game-like scenarios construct a `GenerationRunner`. Scenario creation and package-quality algorithms are not fully inspected. |
| Bounded task revision | [RT-RTE-task-revision](#rt-rte-task-revision) separates judge-guided output revision from scenario tournaments and from updates to the harness itself. |
| HTTP, MCP and SDK | Included entry seams are identified in the boundary. This report does not re-audit their complete authorization, cancellation or persistence semantics. Starting a tool/job does not establish human approval of its content. |
| Pi extension | SRC-1, `pi/src/index.ts`, registers judge/improve and other tools, dynamically loads `autoctx` at invocation, and returns truncated text plus structured details. Its improve handler constructs `SimpleAgentTask` and `ImprovementLoop` with caller-supplied rubric and bounds. Abort checks surround the awaited loop; this alone does not prove interruption of its inner provider request. The implementation of enclosing Pi is not frozen. |
| Mission executor | SRC-1, `autocontext/src/autocontext/mission/executor.py`, checks active status and budgets, invokes the supplied step executor, records failures/blocked states, then verifies between steps until success, budget exhaustion or iteration cap. The callback owns the actual work; a mission status is not an independent correctness oracle. Full mission verifier implementation remains uninspected. |
| TypeScript control plane | SRC-1, `ts/src/control-plane/promotion/decide.ts`, computes a deterministic recommendation from supplied metrics, integrity/track/quarantine checks, optional ablation, safety, quality, cost and latency. Safety regressions force failure; no-baseline success recommends shadow. This is a recommendation function, not itself a deployment write. Full callers and rollout enforcement remain uninspected. |
| Session memory, skills, packages and maintenance | Included producers and consumers are named in the boundary. Detailed revision, selection, expiry, import/export and session consolidation semantics are left to the memory account; this report makes no universal gate claim about them. |
| Remote/GPU paths | SRC-1, `autocontext/src/autocontext/execution/supervisor.py`, enforces prepared-fixture identity at its interface. The Prime executor exposes task-identified and remote-requirement variants in `autocontext/src/autocontext/execution/executors/primeintellect.py`; only signatures/search passages were inspected here. End-to-end remote ledger, provisioning and attestation guarantees are not established by this report. |

Available but uninspected material is not an access gap or evidence of absence. In particular, this baseline does not establish Python/TypeScript parity, security of Monty or containers, remote exactly-once effects, efficacy of shipped studies, or complete admission coverage of every maintenance command.

## Shared records

### Components

#### RT-CMP-role-models
Label: Role generation and evaluation models

Source-native identity: configured competitor, translator, analyst, coach, architect, curator and judge models. Representational form: distributed-parametric inference behind client/provider interfaces. Storage substrate: external provider state or local model/checkpoint files; provider internals and exact weights are not inspected.

SRC-1, `autocontext/src/autocontext/agents/orchestrator.py`, resolves role/provider/model settings and wraps clients, including scenario-bound local routing; `autocontext/src/autocontext/runtimes/direct_api.py` calls provider completion. Parameters are not updated inside these inspected inference calls. That does not exclude training elsewhere. Exact model versions are not pinned by this repository revision: settings and default aliases select them, and a mutable endpoint can resolve to another model. The Claude adapter even permits a fallback alias. Hosted serving mutability remains externally controlled.

> result = self._provider.complete(
>     system_prompt=sys_prompt,
>     user_prompt=prompt,
>     model=self._model,
> )
> --- `autocontext/src/autocontext/runtimes/direct_api.py`

#### RT-CMP-training-checkpoints
Label: Trainer-produced local checkpoints

Source-native identity: backend checkpoints published as `TrainingCompletionOutput` and registered models. Representational form: distributed-parametric weights or adapters; symbolic metadata is a separate registry consumption layer. Storage substrate: backend checkpoint directories and model-registry artifacts under the knowledge root. SRC-1, `autocontext/src/autocontext/training/runner.py`.

Parameters change during training experiments, not ordinary role completion. Exact parameter versions are not supplied by this analysis's source pin: runtime-produced checkpoint paths, metadata, base-model selection and registry records determine them. Active registry bindings and serving endpoints can change the model used on later calls. A registry ID or path alone is not proof of immutable weight content. Publication/activation is wired, not observed serving.

> record = publish_training_output(
>     completion,
>     registry,
>     artifacts_root=settings.knowledge_root,
>     auto_activate=True,
> )
> --- `autocontext/src/autocontext/training/runner.py`

### Operative objects

#### RT-OBJ-strategy
Label: Scenario strategy at the execution boundary

Source-native identity: `ExecutionInput.strategy`, copied from `ctx.current_strategy`. Representational form: symbolic mapping consumed by scenario/executor code; generated prose is translated before this boundary. Storage substrate: in-process mapping, serialized strategy JSON in match records and generation artifacts. SRC-1, `autocontext/src/autocontext/execution/supervisor.py`, `autocontext/src/autocontext/loop/stages.py`.

A mapping carrying `__code__` changes executor path to generated source execution; source then has executable authority, not merely advisory prompt authority. This is why a JSON strategy interface does not imply all strategy values are inert data.

> if "__code__" in strategy:
>     from autocontext.execution.executors.monty import MontyExecutor
> --- `autocontext/src/autocontext/execution/executors/local.py`

### Routes

#### RT-RTE-scenario-generation
Label: Python scenario generation and strategy selection

Endpoints: CLI/operator or shipped caller → `GenerationRunner` → pipeline/roles → supervisor/tournament → gate → artifacts and run summary. Owner: runner code owns next-generation scheduling; orchestrator owns role dispatch; scenario and gate code own scoring and selection. Context/state/effects: seeded observation, retained context, translated strategy, score/rating history, matches, replays and role output. The role models are [RT-CMP-role-models](#rt-cmp-role-models).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `RunSummary`; CLI renders a table or JSON, while generation events expose intermediate progress.
- Later read-back: next generations load knowledge and trajectory; reentry hydrates durable SQLite state; optional cross-run inheritance restores a prior snapshot when a playbook is missing.
- Delegated visibility: role-specific prompts and selected predecessor output reach model calls; raw provider/host session internals are uninspected.
- Selection predicate: scenario interface, generation count, exploration mode, gate result and configured retry limits; completed run reentry can be a no-op.
- Invalidation or expiry: reentry validates scenario/runtime compatibility; failed generations are recorded; runtime changes require the runner's explicit allowance.
- Activation or effect: strategies are executed and scored; advance/retry/rollback updates runtime selection state. Model use of advice and measured benefit are unobserved.
- Evidence limits: static normal-path and retry/persistence inspection, not a full audit of every optional exploration, repair, probe, holdout or consultation branch.

Decision roles and mode: bounded generations and configured exploration/retry curricula. Models propose; code translates, evaluates and selects; curator can reject/merge a proposed playbook, subject to bypass conditions. The interactive controller can pause/stop and provide gate control on supported paths. Starting the run is not per-edit human approval. The answer oracle is scenario-specific scoring/validation, not necessarily a reference answer; no universal oracle is established. Guidance includes scenario rules, evaluation criteria, playbook and failure feedback. Replays and role artifacts persist; memory-content revisions are not assessed here.

SRC-1, `autocontext/src/autocontext/cli.py`, `autocontext/src/autocontext/loop/generation_runner.py`, `autocontext/src/autocontext/loop/generation_pipeline.py`, `autocontext/src/autocontext/loop/stages.py`.

> if attempt > settings.max_retries:
>     gate_decision = "rollback"
>     break
> --- `autocontext/src/autocontext/loop/stages.py`

Recovery is durable status plus reentry, not atomic rollback of all external effects. Generation exceptions record a failed generation and re-raise. A final safety net marks still-running generation rows failed. SQLite recovery markers, event receipts and trace artifacts expose decisions but do not independently authenticate successful provider or external work.

#### RT-RTE-context-promotion
Label: Matched context-candidate admission

Endpoints: candidate digest in generation context → promotion coordinator/evaluator/store → active bundle/routing, or deferred/negative outcome. Owner: `ContextBundlePromotionCoordinator`; pipeline invokes the boundary after tournament. Proposed change: retained context bundle, potentially including routing. Models supply context proposals elsewhere; code comparison and optional auditors/campaign control admit them.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: evaluation event/result, routing update when promoted, or `ContextBundleEvaluationDeferred` on failed/incomplete/review-held evaluation.
- Later read-back: active bundle is read in knowledge setup; a failed generation resumes one pending candidate before generating new work.
- Delegated visibility: evaluator receives candidate/incumbent context; detailed evaluator/provider isolation internals are not fully inspected here.
- Selection predicate: coordinator and candidate digest must both exist; matching evaluation, lifecycle, evaluator-plan, staleness, optional audit and false-promotion authorization govern promotion.
- Invalidation or expiry: stale candidates and evaluator-plan mismatch can block admission; more than one pending candidate prevents ambiguous resume.
- Activation or effect: store promotion must yield the evaluated active digest; routing is applied through the orchestrator. This is installation wiring, not observed downstream compliance or benefit.
- Evidence limits: no paired trials or supplied execution outcomes inspected; statistical guarantees depend on evaluator correctness and comparison assumptions, not merely the presence of the gate.

SRC-1, `autocontext/src/autocontext/loop/context_bundle_evaluation.py`, `autocontext/src/autocontext/context_bundles/promotion.py`, `autocontext/src/autocontext/loop/stages.py`.

> if coordinator is None or digest is None:
>     return
> --- `autocontext/src/autocontext/loop/context_bundle_evaluation.py`

> except Exception as exc:
>     logger.warning("context bundle matched evaluation failed closed", exc_info=True)
> --- `autocontext/src/autocontext/loop/context_bundle_evaluation.py`

> if active is None or active.digest != digest:
>     raise RuntimeError("context bundle promotion did not activate the evaluated candidate")
> --- `autocontext/src/autocontext/loop/context_bundle_evaluation.py`

Guarantee owner/enforcement: the boundary function and coordinator enforce a **protocol** for candidates going through them, with implementation conclusion status wired and operation conclusion status uninspected. They do not cover direct artifact writes, TypeScript support-role writes, training activation or arbitrary imported code. Optional audit can return review/pause; this is not mandatory human approval. Incumbent preservation/deferred resume supplies recovery before admission; rollback after a successfully promoted bundle was not traced here. Mode: bounded matched evaluation with optional campaign control. Oracle: evaluator results on fixture/seed pairs, not an assumed correct answer. Guidance/proposal content lives in the bundle and remains for the memory/epistemic accounts to assess.

The counterexample to using tournament success as context-edit warrant is explicit:

> coach_playbook=(
>     outputs.coach_playbook
>     if gate_decision == "advance" and ctx.active_context_bundle_digest is None
>     else ""
> ),
> --- `autocontext/src/autocontext/loop/stages.py`

#### RT-RTE-context-assembly
Label: Role-context selection and channel separation

Endpoints: knowledge setup and scenario contract → prompt preparation/budget → role calls. Owner: code selects components and channels; hooks may transform inputs; models interpret the resulting text. Representational form: natural-language instruction/reference bodies, with symbolic selection metadata and prompt-channel assignments. Files remain outside the model window unless selected and copied in.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `PromptBundle`, optional split parts and selection/compaction telemetry.
- Later read-back: knowledge is loaded afresh for subsequent generations; ledger/selection persistence is wired. Complete semantic-compaction reload behavior is uninspected here.
- Delegated visibility: separate role prompts contain selected observations and knowledge; structural split applies only to safe roles and capable clients, otherwise flat prompts are used.
- Selection predicate: feedback ablation, runtime context budget, component caps/trim order, scenario-contract trust and hook/mutation effects.
- Invalidation or expiry: prompt parts are dropped after harness mutation or trusted-field hook rewrite; trimming affects delivered copies rather than deleting source files.
- Activation or effect: components enter model inputs; reliable compliance or improved decisions remain unobserved.
- Evidence limits: token budgets use approximate estimation; prompt-budget code is not a guarantee about the complete host conversation window or provider tokenizer.

SRC-1, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/loop/stage_helpers/semantic_benchmark.py`, `autocontext/src/autocontext/prompts/context_budget.py`, `autocontext/src/autocontext/agents/orchestrator.py`.

> _PROTECTED = frozenset({"hints", "dead_ends"})
> --- `autocontext/src/autocontext/prompts/context_budget.py`

> ctx.parts = None if active_harness_mutations else prompt_parts
> --- `autocontext/src/autocontext/loop/stages.py`

Working-context control: code preferentially trims reports, evidence/notebook material, experiment/research/environment text, trajectory, analysis, tools, lessons, then playbook; hints/dead ends are protected. Truncation retains a prefix and marker, not a semantic pointer. Unselected original files remain reachable to repository/runtime facilities, but this report does not establish automatic on-demand recovery of every removed passage. Role isolation keeps unrelated role work out of each call; assembled return values cross back. RLM and opaque-host compaction are separate, incompletely inspected alternatives.

#### RT-RTE-task-revision
Label: Judge-guided task-output revision

Endpoints: CLI agent-task/solve task-like dispatch → `ImprovementLoop` → task evaluator and revision method → best output/result. Owner: loop code controls iteration and thresholds; task implementation owns generation/revision and evaluation. Models evaluate rubric content and propose revised text; optional external verifier and revision-feedback callback supply separate checks/feedback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `ImprovementResult` with best output/score/round, threshold state, termination reason and metadata; final event accompanies return.
- Later read-back: revision feedback and prior output reach subsequent rounds in the invocation; cross-run retained knowledge depends on the caller and is not established by `ImprovementLoop` alone.
- Delegated visibility: task evaluator receives output, state and optional reference/concept/calibration inputs; revision receives judge feedback; callbacks may add objective-verification context.
- Selection predicate: configured rounds, quality/dimension thresholds, parse-failure handling, verifier vetoes, plateau/no-change logic and evaluator comparability.
- Invalidation or expiry: content/context fingerprints cache evaluations; missing required targets force a zero score; changed evaluator epoch can rebaseline earlier comparison state.
- Activation or effect: a revised external output is selected and returned; it is not automatically a change to the harness's own organization.
- Evidence limits: no supplied task result or actual verifier run; judge instructions establish requested assessment, not factual correctness.

Mode: bounded revision of an open caller task. Oracle: optional caller reference context and external verifier; rubric judgment alone is not an answer oracle. Humans supply task/rubric/configuration; computation performs internal rounds without a demonstrated per-revision human veto. Source evidence: SRC-1, `autocontext/src/autocontext/execution/improvement_loop.py`, `autocontext/src/autocontext/execution/judge.py`, `autocontext/src/autocontext/knowledge/solver.py`.

> missing_targets = [target for target in self.required_targets if target not in current_output]
> cached_verdict = None if missing_targets else verdict_cache.get(fingerprint)
> --- `autocontext/src/autocontext/execution/improvement_loop.py`

Guidance is the task, rubric, optional reference and accumulated feedback. Round output, best output and result metadata persist at least for the computation; durable caller persistence is separate. Rejection/recovery keeps best output and last good feedback rather than requiring every later revision to succeed. The source's loop docstring describes failed rounds as not counting, but the inspected implementation iterates `range(1, self.max_rounds + 1)`; do not infer unbounded free replacement rounds from that prose.

#### RT-RTE-npm-generation
Label: TypeScript generation and playbook admission

Endpoints: npm shipped runner/caller → provider completions and tournament lifecycle → journal/support roles → artifact-store playbook. Owner: `GenerationRunner`, lifecycle workflow and store. Analyst/coach calls run concurrently; optional curator can reject or merge. Guidance includes current playbook, task/scenario and tournament summary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: finalized run result or stopped/failed result, events and persisted generation journal.
- Later read-back: runner prompt construction reads the scenario playbook; support reports and dead ends provide further retained inputs.
- Delegated visibility: provider-role completion receives built role prompts; support-role output is stored separately in SQLite/artifacts and support log.
- Selection predicate: support call follows lifecycle persistence; structured markers, playbook guard, optional curator and `requireApproval` govern the inspected playbook write path.
- Invalidation or expiry: pending content blocks replacement while approval is required; nonapproval live write removes stale pending content. Detailed playbook-version rollback is uninspected.
- Activation or effect: write is live immediately unless approval is required; then it is staged for explicit approval/rejection. Delivery and actual influence on later calls are distinct.
- Evidence limits: no observed npm run; no matched-context candidate evaluation is established for this support-role path, and no parity with Python is inferred.

SRC-1, `ts/src/loop/generation-runner.ts`, `ts/src/knowledge/artifact-store.ts`. Bounded generation mode; model coach proposes, guard/code and optional curator decide; configured pending approval adds a content-admission step but caller identity alone does not establish a human actually performed it. Oracle is scenario evaluation where configured, not an expected answer for the new playbook.

> await this.runSupportRoles(runId, lifecycle.generation, lifecycle.finalizedAttempt);
> --- `ts/src/loop/generation-runner.ts`

> if (!opts.requireApproval) {
>   this.writePlaybook(scenarioName, content);
> --- `ts/src/knowledge/artifact-store.ts`

Guarantee owner/enforcement: `writeOrStagePlaybook` implements a **policy** at that method, implementation conclusion status wired and operation conclusion status uninspected. Direct `writePlaybook`, hook-modified writes and other mechanisms are alternate paths, not covered by that approval branch. A public direct writer is a concrete counterexample to universal approval. The curator is conditional on enabled state and a nonempty prior playbook. Format/guard acceptance does not demonstrate the new instruction is true or causally useful.

Theory boundary for the two playbook routes: no concrete generated playbook or criticism was inspected. The system requests guidance and revisions, but this does not establish that a resulting artifact formulates an explanatory theory. Theory-builder conditions 1–4: condition 1 conclusion status uninspected; condition 2 conclusion status uninspected; condition 3 conclusion status uninspected; condition 4 conclusion status uninspected. Addressability, retained rationale, learning, reflection, reflective theory building and autonomous theory building are uninspected for actual playbook content. Storage and iterative plumbing do not substitute for those independent conditions. Persistence wiring reaches later rounds/runs; exercised self-improvement and successful improvement remain unestablished without downstream causal evidence.

#### RT-RTE-runtime-dispatch
Label: Provider, subprocess, shell and extension effect boundaries

Endpoints: role/task caller → direct API or agent runtime; workspace caller → local shell or explicit command callback; extension reference → imported module/register callback. Owners: configured adapter and enclosing host/OS. Symbolic settings choose the route; models receive natural-language prompts and may exercise host tools where granted.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: completion/`AgentOutput`, command result, registered hooks, or runtime failure.
- Later read-back: optional agent sessions can retain conversation; persistent Pi RPC keeps its process for queue/state operations. Complete host retained-state semantics are uninspected.
- Delegated visibility: prompt/system/feedback and configured workspace reach the subprocess/host; imported extension code executes in the Python process, not in a model-only role frame.
- Selection predicate: provider/runtime settings, tools/permission/session configuration, workspace command match and extension refs select behavior.
- Invalidation or expiry: runtime timeouts/budgets, process close, session settings and workspace cleanup have route-specific scope; they are not one universal deadline or revocation mechanism.
- Activation or effect: direct provider returns text; subprocess tools and shell can have OS effects; imported code can register hooks or execute arbitrary module initialization within process authority.
- Evidence limits: no deployed permissions, live grant inventory, host tool implementation or sandbox audit; capability and configured adapter defaults are not the actual grant set of a running installation.

SRC-1, `autocontext/src/autocontext/runtimes/direct_api.py`, `autocontext/src/autocontext/runtimes/claude_cli.py`, `autocontext/src/autocontext/runtimes/pi_rpc.py`, `autocontext/src/autocontext/runtimes/workspace_env.py`, `autocontext/src/autocontext/extensions/loader.py`, `autocontext/src/autocontext/execution/executors/local.py`.

> permission_mode: str = "bypassPermissions"
> --- `autocontext/src/autocontext/runtimes/claude_cli.py`

> if self._config.tools is not None:
>     args.append(f"--tools={self._config.tools}")
> --- `autocontext/src/autocontext/runtimes/claude_cli.py`

The adapter's `None` tools setting leaves host defaults, whereas an empty string explicitly requests no tools. Neither this option nor output schema validates every host side effect. Direct API completion does not traverse Claude's tool/permission options.

> if granted is not None:
>     return granted
> result = run_bounded_process(
>     command,
>     cwd=host_cwd,
>     env={**default_shell_env(), **dict(exec_options.env)},
>     shell=True,
>     timeout_ms=exec_options.timeout_ms,
> )
> --- `autocontext/src/autocontext/runtimes/workspace_env.py`

Thus command grants provide named-command handling on this local implementation, not denial of all unmatched shell commands. File-path root checks do not by themselves confine that shell's OS authority. Imported extensions are another bypass of model-tool controls:

> spec.loader.exec_module(module)
> --- `autocontext/src/autocontext/extensions/loader.py`

Change admission for extensions: configured refs propose module/callable/file code, the loader imports/invokes it, and failure can stop loading; no per-content evaluator or rollback is established at this loader. Effects persist in the process/hook bus and potentially elsewhere under extension authority. These are operator/configuration inputs, not evidence of autonomous extension invention.

Scenario execution has yet another limit. `LocalExecutor` attempts process memory limits but suppresses limit-setting errors, and on `PermissionError` uses threads. Timeout uses `future.result`/cancel under an executor context; cancelling a running future does not establish that work has stopped, and context shutdown can wait. Guarantee strength: **best effort** for this local resource-control interpretation; implementation conclusion status wired, operation conclusion status uninspected. Owner: local executor/OS. It does not cover external agent subprocesses or remote workers, and its external contract includes POSIX resource support and worker termination behavior. Monty's code path is distinct and its internal security boundary is uninspected here.

#### RT-RTE-training-experiments
Label: Training-source revision, checkpoint selection and publication

Endpoints: `TrainingRunner.run` → workspace/template and baseline → proposed `train.py` → backend subprocess → promotion decision → keep/discard → model publication. Owner: runner and training promotion code. A model client proposes source under program/model/source/recent-results guidance; code owns execution, stop limits, selection and checkpoint registry writes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `TrainingResult` with accepted/discarded experiment results, checkpoint and optional published model ID.
- Later read-back: later experiments read current source and recent outcomes; publication supplies model registry/base-model metadata for scenario-bound serving.
- Delegated visibility: proposal receives training context; backend subprocess executes training source; actual GPU/provider internals are uninspected.
- Selection predicate: first successful experiment establishes a baseline; deterministic promotion uses summary-derived trial input, while adaptive promotion needs an executor; terminal accepted challenger is published rather than the maximum unpaired score.
- Invalidation or expiry: stop budgets cap experiments; discard uses training Git state and removes candidate checkpoint; decision artifacts remain. Full crash recovery is not audited.
- Activation or effect: proposed executable training machinery is run before keep/discard; selected checkpoint is published with `auto_activate=True`. Inference routing and parameter changes are represented separately in [RT-CMP-training-checkpoints](#rt-cmp-training-checkpoints).
- Evidence limits: no training execution, observed checkpoint or serving result; acceptance and registry activation do not prove useful learned capacity or subsequent exercise.

SRC-1, `autocontext/src/autocontext/training/runner.py`, `autocontext/src/autocontext/training/promotion_confirmation_runner.py`. Mode: bounded experiments with deterministic/adaptive variants. Oracle: backend evaluation summary or supplied trial executor, not a universal expected-answer service. Humans select configuration/data/backends; code/model perform proposals and keep/discard without a per-experiment human approval step in the inspected loop. Rejection restores candidate state through `TrainingGitState`, not arbitrary side effects of executed source.

> (self.work_dir / "train.py").write_text(proposed_source, encoding="utf-8")
> self._git_commit(f"experiment {experiment_index}")
> --- `autocontext/src/autocontext/training/runner.py`

> if settings.promotion_mode == "adaptive":
>     if executor is None:
>         return _missing_executor_artifact(settings, incumbent_id, challenger_id, protocol)
> --- `autocontext/src/autocontext/training/promotion_confirmation_runner.py`

This route changes machinery and numerical parameters, unlike merely revising an external answer. It affords improvement-directed self-change within the training/serving system, but evidence-to-update, installation, later authority and exercised causal dependence must be distinguished: the last link is unobserved. It establishes neither successful self-improvement nor learning benefit from the source alone. No theory-builder assessment of generated training programs is made; their actual explanatory content is uninspected.

#### RT-RTE-ambient-promotion
Label: Charter-controlled ambient model promotion

Endpoints: daemon stage factory → ingest/curate/advise/train/evaluate/promote → shared registry and optional serving manifest. Owner: charter policy and stage implementations. Trigger: stage cycle with candidate evaluation metadata. Proposed change: active model binding for a target/role, not a playbook overwrite.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stage counts/events including approval-required, anchor-mismatch or activated receipts.
- Later read-back: train/evaluate/promote share a model registry; serving manifest maps scenario/role to target/artifact for later resolution.
- Delegated visibility: configured native-run/agent-output/OTel sources feed stages; exact redaction/curation and training internals were not inspected in this route.
- Selection predicate: candidate state, target, real candidate generation, drift-clean flag, current anchor, highest eligible score, incumbent comparison and charter approval policy.
- Invalidation or expiry: changed evaluation fingerprint can cause later reevaluation; mismatched incumbent anchor prevents auto-promotion; full probation rollback executor remains uninspected.
- Activation or effect: probation metadata records previous active model; optional bridge writes before registry activation, then the incumbent is demoted and retained as rollback target.
- Evidence limits: no daemon cycle or independent model comparison observed. Stage wiring does not establish that advice or training is effective.

SRC-1, `autocontext/src/autocontext/ambient/stage_factory.py`, `autocontext/src/autocontext/ambient/promote.py`. Mode: charter-scoped maintenance; code proposes the highest eligible candidate and decides admission; approval-required policy emits and returns rather than activating. Oracle: scores judged under an anchor model/evaluation suite, not ground truth by virtue of being an anchor. Guidance includes charter, target selector and evaluator metadata. State retained includes registry evaluation and probation records.

> if eval_meta.get("from_candidate_generation") is not True:
>     return False
> --- `autocontext/src/autocontext/ambient/promote.py`

> self.registry.activate(best.artifact_id)
> --- `autocontext/src/autocontext/ambient/promote.py`

The optional advice review gate is not universally fail-closed: factory failure to construct its provider leaves it disabled. This is a separate policy from promotion, whose own real-generation check rejects placeholder scores. No one gate should be projected across stages.

#### RT-RTE-kernel-evolution
Label: Benchmark-gated kernel-source evolution

Endpoints: single-use runner under advisory path lock → baseline evaluation → generated candidate/receipt → benchmark and optional confirmation → decision/champion artifacts. Owner: host configuration, benchmark evaluator and `KernelDecisionPolicy`; model/code generator proposes source. Source and receipts are symbolic executable artifacts; numerical performance results feed fixed decision rules.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: kernel evolution result/summary or baseline/integrity/cancellation error.
- Later read-back: champion/source and history guide later proposals; durable manifests/journal/summary support resume, including returning an already-complete summary.
- Delegated visibility: evaluator gets candidate and incumbent plus expected scope/baseline/protocol identity; adaptive proposals receive disclosed primary feedback rather than detailed confirmation results.
- Selection predicate: proposal caps, valid baseline, receipt/source digest agreement, stop checks, benchmark eligibility, deterministic promotion gates and optional confirmation.
- Invalidation or expiry: changed source after durable generation receipt raises integrity error; protocol mismatch makes baseline ineligible; runner instances are single-use.
- Activation or effect: accepted source becomes champion within this kernel campaign; downstream deployment beyond the campaign is not established here.
- Evidence limits: lifecycle and policy branches inspected, not benchmark hardware runs, all confirmation internals or performance results. Artifact receipts do not independently prove hardware execution.

SRC-1, `autocontext/src/autocontext/kernel_evolution/runner.py`, `autocontext/src/autocontext/kernel_evolution/runner_lifecycle.py`. Mode: bounded benchmark experiment campaign. Oracle: benchmark correctness/reference machinery supplied by evaluator, not LLM judgment; full oracle provenance is uninspected. Humans configure baseline, caps and protocols; generator proposes, fixed policy rejects/accepts, and stop controls can veto dispatch. Failed baseline stops; rejected candidates do not displace incumbent. Persistent artifacts support recovery but no universal rollback of paid external work is asserted.

> if candidate.artifact_digest != generation_result.artifact_digest:
>     raise KernelIntegrityError("candidate source changed after its generation receipt was persisted")
> --- `autocontext/src/autocontext/kernel_evolution/runner_lifecycle.py`

> reasoning=disclosed_feedback,
> --- `autocontext/src/autocontext/kernel_evolution/runner_lifecycle.py`

This is a consequential working-context filter: confirmation evidence is retained for audit, while the next adaptive proposal is deliberately given primary feedback only. The complete confirmation record is not the model-visible training signal. The policy remains independent of the scalar prompt score. No generated kernel theory or criticism was supplied, so numerical selection is not classified as content-directed theory criticism.

### Claims

#### RT-CLM-agent-improvement
Label: Product claim of retained agent improvement

Claimed operation: goal-driven attempts against evaluation retain useful lessons, discard dead ends and leave context/training artifacts for subsequent work. Source: SRC-1, `README.md`, doctrine/design, not observed operation.

> autocontext is a harness for agent improvement. Give it a goal, it runs the task against evaluation, keeps the useful lessons, discards dead ends, and leaves traces, reports, playbooks, datasets, and optional local-model training artifacts for the next run.
> --- `README.md`

The inspected routes wire attempts, evaluation, persistence and some later consumers. The adjectives useful and self-improving require separate operational/causal evidence not supplied here. External output improvement, retained instruction change, checkpoint training and kernel optimization remain distinct pathways.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-context-delivery
Label: Retained guidance into role decisions

Consumer: competitor/support-role models. Channel: selected playbook, hints, tools, reports and lessons copied into constructed role prompts, sometimes as untrusted user reference rather than system instruction. Force: interpretive guidance, not an execution invariant; symbolic selection/channel code controls delivery, not model compliance. Horizon: later generation calls and, where knowledge is retained/restored, later runs on the scenario. SRC-1, `autocontext/src/autocontext/loop/stages.py`, `autocontext/src/autocontext/agents/orchestrator.py`, `ts/src/loop/generation-runner.ts`.

> current_playbook=playbook,
> available_tools=tool_context,
> operational_lessons=skills_context,
> --- `autocontext/src/autocontext/loop/stages.py`

The wiring is [RT-RTE-context-assembly](#rt-rte-context-assembly), not proof of activation or benefit. Tool specification text is not itself a callable grant: setup separately derives names from artifact-store installed tools. Executable source admission and model-registry activation in the runtime/training/kernel routes have different force and must not be collapsed into this advisory channel.

## Annotations

none
