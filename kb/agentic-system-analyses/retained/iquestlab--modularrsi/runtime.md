---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ModularRSI runtime baseline: module-library evolution, gated generation admission and later solver consumption at the frozen release."
run-id: AAS-2026-10-18-modularrsi-4218ceff5530-01
reviewed-boundary: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
---

# ModularRSI runtime report

## Runtime account

### Work and evidence basis

ModularRSI changes executable harness strategies, not model weights. Its released improvement plane samples task executions, diagnoses selected trajectories, constructs module candidates, filters them and makes promoted libraries available to subsequent solver tasks. Evaluation consumes an explicitly selected library without running the improvement loop. The accuracy and transfer claims are source-reported results, not results of this inspection; see [RT-CLM-harness-improvement](#rt-clm-harness-improvement).

This account uses SRC-1 at the boundary's frozen commit. Added implementation coverage includes the installed module library loader, baseline loop/tools/context/verification, editor file-tool checks, candidate gate branches, portfolio ranking, promotion/rebase rules, confirmation, staging and verifier execution. The exact files appear in the records below. Source prompt passages are doctrine/design evidence of requests; callers and guards are implementation evidence. No target code, tests or model calls were executed. Individual bundled evaluation trials were not inspected here. Operation, activation in supplied runs and causal benefit remain uninspected in this member; that does not negate architectural wiring.

### Ordinary evolution invocation

An operator configures model, endpoint, credentials, support dataset, environment, module lock and workload, then launches `scripts/evolve.sh`. The launcher validates its configuration and invokes Phase0. Phase0 resolves local support tasks and passes a locked-module experiment to `run_online_evo`. The ordinary defaults select up to two implementation lanes and repeated solver attempts. This is a bounded task curriculum, not an open-ended request to improve anything. The operator supplies the objective and resources, not approval of each content change (SRC-1, `scripts/evolve.sh`, `src/harbor/agents/terminus_2_modular/self_evo/phase0.py`).

The driver snapshots the installed modules into `gen_0`, seeds the archive, starts from the latest generation, validates inherited bundle pins and builds a reproducible shuffled task queue. Resume checks recorded task-index/name alignment; mismatch moves progress aside and reruns rather than silently combining task orders. Each launched task group captures its generation at launch. Roll zero dynamically selects a bundle; later rolls replay that bundle from a private snapshot. Task subprocesses run through Harbor, producing trajectories and trial-level verifier rewards. See [RT-RTE-solver-task](#rt-rte-solver-task) and [RT-RTE-bundle-selection](#rt-rte-bundle-selection).

Completion counts trigger a background reflection window. Solver launches continue while one reflection runs; pending summaries can therefore exceed the nominal cadence and include stragglers from earlier generations. Bundle identities in trajectories preserve which variants produced evidence, but do not make the collected comparisons randomized experiments. The driver measures completed solver groups during reflection. Editor admission has its own event-loop semaphore, default two; this limits endpoint pressure rather than granting permission to modify content (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py`).

Reflection routes selected tasks to separate investigator sessions, persists findings, feeds the backlog/evidence path, ranks open proposals and gives each implementer only its own proposal and supporting findings. Independent staging trees share a parent, not mutable files. Candidate admission combines software checks, model review and crash/activation sanity runs. Passing candidates become numbered generations. The driver updates `current_gen` to the newest promotion; later launches consume it. Cross-epoch confirmation can retire variants from ordinary dynamic selection. See [RT-RTE-generation-change](#rt-rte-generation-change).

### Solver invocation and effect boundary

`evaluate.sh` instead launches Harbor with `terminus-2-modular`, the released `generations/merged_active/gen_0/modules` directory by default, and composer scope `all`. The installed agent shim calls installed kernel orchestration. Orchestration loads Python modules, chooses five strategies and optional helper tools, constructs a chat/model client, initializes tools and observation, and delegates turn ownership to the selected agent-loop implementation. The baseline loop calls the model, parses commands, executes them, captures observations, records steps and asks the selected verification module whether to stop. Its completion decision is distinct from Harbor's later task verifier reward. Context compression is another model-client route, not terminal execution: see [RT-RTE-context-handoff](#rt-rte-context-handoff).

Capability surface, current grants and isolation must not be conflated. A solver has shell-like command access through its supplied task environment; helpers execute Python callbacks with a module context. The editor has an action dispatcher instead of a terminal and runs locally with `environment=None`. Its file tools limit normal read/write actions, but validation and library discovery execute candidate Python in the host process. Docker/E2B task isolation does not thereby isolate candidate imports or local editor infrastructure. The actual deployed credentials, mounts, network access and provider behavior are not established by these callers (SRC-1, `src/harbor/agents/terminus_2_modular/modules/tools/baseline.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py`, `src/harbor/agents/terminus_2_modular/library.py`).

### Three forcing cases and scoped guarantees

1. **Review failure is not necessarily veto.** An explicit structured reject blocks admission, but a reviewer timeout or exception returns `passed=True`. Missing structured verdicts initially pass through and feed a circuit breaker; the timeout/exception returns precede that accounting. Thus “every promoted change was approved by review” is not an invariant. Owner: evolution gate driver. Enforcement: `review_edit` and the subsequent `review.passed` branch. Strength: best effort. Required external contract: reviewer/provider availability and meaningful verdict compliance. Implementation conclusion status: wired. Operation conclusion status: uninspected. Evidence and repair consequences are in [RT-RTE-generation-change](#rt-rte-generation-change).

2. **No-shell editor actions do not establish safe candidate execution.** Normal edit/create/edit-lines actions check paths, the module lock, foundation filenames and staging containment. However, the `validate` action invokes smoke, and smoke/library discovery import arbitrary candidate Python; helpers are later Python callbacks too. The frozen-kernel rule is a tool-mediated write policy for supported actions, not a process security boundary against hostile code. Owner: editor tool dispatcher for file actions; host for Python execution. Enforcement: `_write_allowed`, `_safe_resolve`, `_is_off_limits`; no equivalent candidate-code isolation is established by these guards. Strength: policy. Required external contract: trusted candidate code or additional host isolation. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-BAP-module-execution](#rt-bap-module-execution).

3. **Successful forced execution does not imply normal selection or improvement.** Sanity uses a private forced pin to exercise the changed variant and checks activation evidence plus code crashes. A separate routing probe asks whether ordinary selection would choose it, but never gates. Candidate task failure and infrastructure timeout are not by themselves code-break rejection; parent reward is logged, not an admission threshold. Owner: evolution gate driver. Enforcement: required-activation and `_is_code_break` logic. Strength: protocol for the configured battery, not a quality invariant. Required external contract: task environment, tracer and provider yield interpretable evidence. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-generation-change](#rt-rte-generation-change).

The alternate-path check includes ordinary chat, direct composer/evidence calls, direct summarization calls, local editor validation, helper callbacks, shell/environment execution, static/cached/forced bundle paths and generation replay. These are enough to reject a universal review, isolation or quality guarantee. Provider-native tool execution and arbitrary deployment extensions were not independently audited; this account makes no all-provider or all-extension guarantee. Shipped variant bodies are executable alternatives, not constrained implementations of the baseline's stopping policy. The released `combined_robust` variant, for example, overrides helper dispatch and blocks a specific heredoc pattern while delegating other execution to baseline; it does not turn the command surface into a general allowlist (SRC-1, `generations/merged_active/gen_0/modules/tools/combined_robust.py`).

## Shared records

### Components

#### RT-CMP-lite-llm
Label: Configured LiteLLM-backed models

Identity: the distributed-parametric provider models reached through `LiteLLM`. Orchestration builds the solver client from model name, API base, credentials and runtime options. Editors use the same configurable model-name interface; the composer and evidence pass construct additional direct clients; summarization reuses the chat's model. These are roles of configurable provider components, not evidence of independently trained local models (SRC-1, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/self_evo/run_editor.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`, `src/harbor/agents/terminus_2_modular/self_evo/evidence_pass.py`, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`).

Representational form: distributed-parametric model state. Storage substrate: external provider service; weights and provider-side persistence are inaccessible in this boundary. For each of solver, editor/investigator/reviewer, composer, evidence and summarization roles: the inspected path invokes inference, not parameter updates; provider-side parameter changes during operation are uninspected. Exact weight versions are not pinned by these constructors. A mutable endpoint/model alias can resolve to another implementation; its actual stability is uninspected. The release pin freezes client code, not served weights. User-supplied model information controls client context/cost assumptions, not weight identity.

> return LiteLLM(
>         model_name=params["model_name"],
>         api_base=params.get("api_base"),
> --- `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`

### Operative objects

#### RT-OBJ-module-library
Label: Executable module library

Source-native identity: `ModuleLibrary`, constructed from installed modules or a generation's `modules/` tree. Representational form: symbolic Python implementations, registration names and factory parameters. Storage substrate: source files copied into numbered generation directories and an in-process registry. This record covers executable strategies; descriptive text consumed by the composer is a distinct part below. It does not declare findings about editor-memory revisions.

The five slots are agent loop, observation, context management, tools and verification. `tool_helper` is an additional subset-selected capability surface passed through tools parameters, not a sixth bundle slot. Path discovery executes every eligible Python file before calling its registration function, so even a variant not selected for execution may already have import-time effects. Failed imports are logged and excluded; availability of a name is not proof that its intended mechanism later runs (SRC-1, `src/harbor/agents/terminus_2_modular/library.py`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`).

> register_fn = getattr(mod, "register", None)
>             if callable(register_fn):
>                 try:
>                     register_fn(lib)
> --- `src/harbor/agents/terminus_2_modular/library.py:165-168`

#### RT-OBJ-module-description
Label: Module descriptions presented to selection

Source-native identity: `ModuleInfo.description` supplied by module registration. Representational form: natural-language content interpreted by the composer model, distinct from the executable factory above. Storage substrate: Python string literals, then catalog text in a model request. Scope and lineage: descriptions accompany installed or evolved variants; the composer filters candidates before constructing the catalog. A description's claim about a capability is not execution evidence (SRC-1, `src/harbor/agents/terminus_2_modular/library.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`).

> "There is no reward signal — judge from the descriptions and the task.\n\n"
> --- `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`

### Routes

#### RT-RTE-solver-task
Label: Solver task execution and verifier return

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: orchestration populates `AgentContext` metrics and attempts a trajectory dump; Harbor writes trial results; the evolution task runner returns task, scalar reward or error.
- Later read-back: evolution consumes retained trajectories and rewards through the generation-change route; evaluation outputs alone do not establish a future update.
- Delegated visibility: selected modules receive `ModuleCtx`, runtime state and shared resources; the solver model receives formatted task/observations, prior chat and tool results, not the whole archive by default.
- Selection predicate: operator-selected task and library; dynamic/static/cache bundle choice determines module implementations; parsed model commands determine tool actions.
- Invalidation or expiry: turn cap, terminal death, model-call failure or completion can end a task; context replacement can discard turns; task-environment lifetime belongs to Harbor and its configured backend.
- Activation or effect: baseline dispatch sends keystrokes into the task terminal or runs registered helper callbacks; the alternate `tmux_xml` implementation calls `env.exec` directly. These are wired effects, not inspected run observations.
- Evidence limits: baseline trace establishes the ordinary skeleton, not identical behavior of all evolved variants; external task payloads and provider internals are unfrozen. No bundled task execution was audited here.

Trigger/principal: public evaluation launch or an evolution task-runner subprocess acting for the operator. Identities include task/session ID, generation path, bundle names and helper names; orchestration's initial state uses `gen_0`, so the loaded path and recorded bundle are more informative than treating that state label as lineage proof. Next-step owner: selected loop, with model-produced command choices and software parsing/termination. Form: natural-language task/chat plus symbolic commands, state and Python policies. Context control includes [RT-RTE-context-handoff](#rt-rte-context-handoff). Executor: task environment for terminal commands, local Python for module/helper callbacks. No per-command human approval step is wired in the inspected baseline execution path. This is a scoped finding about these callers, not a claim about every Harbor integration.

> await session.send_keys(
>                 call.keystrokes,
>                 block=False,
>                 min_timeout_sec=call.duration_sec,
>             )
> --- `src/harbor/agents/terminus_2_modular/modules/tools/baseline.py`

The baseline parses each response, allows one malformed-response retry before ending on a second consecutive parse error, records all tool results, captures observation and checks verification. The baseline verifier requires repeated model completion signals; it does not independently test task correctness. Harbor's verifier separately uploads task tests, executes the configured test script and parses reward JSON/text. That task-provided reference outcome is the answer oracle used by evolution's curriculum, not the model's self-assessment (SRC-1, `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py`, `src/harbor/agents/terminus_2_modular/modules/verification/baseline.py`, `src/harbor/verifier/verifier.py`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py`).

> if consec >= self.required:
>             return True, f"task_complete confirmed {consec} consecutive times"
> --- `src/harbor/agents/terminus_2_modular/modules/verification/baseline.py`

Recovery is bounded rather than transactional: model queries have retry/overflow handling; tools return errors; orchestration attempts teardown, metrics aggregation and dump in `finally`, logging failures. A subprocess timeout or nonzero return becomes a task error. Successful baseline termination is not proof of successful verifier reward. Sources: SRC-1, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py`.

#### RT-RTE-bundle-selection
Label: Per-task module selection and replay

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: a five-slot `ModuleBundle`, with helper names in tools parameters; composer-only mode records selection and returns before solver execution.
- Later read-back: promoted executable files and descriptions reach subsequent library loads; cache-read mode or private K-roll snapshots replay prior bundle choices.
- Delegated visibility: the dynamic picker receives task text and a filtered module catalog; it does not receive verifier rewards as its selection signal. Actual selected helper names are recorded after tools initialization where introspectable.
- Selection predicate: skip retired/excluded archive entries and editor-only variants, deduplicate declared niche cells, honor foundation pins, and vary only the locked type unless scope is `all`; validate returned names against offered choices. Helpers begin as the active subset and model output can exclude offered names.
- Invalidation or expiry: dynamic choice is per task; archive retirement affects ordinary later dynamic selection. Static replay, explicit pins and cache-read choice are alternate paths and do not rerun the full dynamic filter. Cache files are keyed by instruction hash, not by a library revision in the inspected format.
- Activation or effect: accepted names choose instantiated Python strategies; delivered descriptions can influence a model choice, but description-specific activation and efficacy are uninspected.
- Evidence limits: fallback is implemented, not proof that every fallback bundle loads in every externally supplied tree. Forced selection proves neither ordinary routing nor benefit.

Owner/policy/form: software filters and pins bound a model's natural-language catalog judgment; software validates the resulting symbolic names. No human selects each bundle in the ordinary driver. Operating modes: dynamic task matching, fixed static/editor composition, cache replay, composer-only precomputation and private forced sanity/K-roll replay. Answer oracle: inapplicable — this selector requests judgment from descriptions and task, without a reference answer. A failed or malformed picker response retains defaults and the helper inclusion default; an outer composer exception attempts pinned defaults (SRC-1, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`).

> if multi or helper_infos:
>             picked, dropped = await self._llm_pick(
>                 instruction, multi, base, helper_infos
>             )
>             for t, name in (picked or {}).items():
>                 if t in multi and any(i.name == name for i in multi[t]):
>                     chosen[t] = name
> --- `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`

This is successor strategy selection inside a run, not weight training. Its retained authority is described by [RT-BAP-module-execution](#rt-bap-module-execution) and [RT-BAP-description-selection](#rt-bap-description-selection).

#### RT-RTE-generation-change
Label: Contrastive diagnosis through generation admission

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: findings/proposals and per-lane gate outcomes; a window may promote zero, one or two generations and reports the newest promoted path.
- Later read-back: persisted findings support later proposal briefs; promoted modules are loaded by later tasks; archive statuses affect routing, and retained progress restores unfinished reflection inputs. Detailed memory transformations belong to the memory analyst.
- Delegated visibility: each investigator receives selected task summaries, permitted raw trajectories and staged code; each implementer receives its own proposal/evidence, with long findings truncated and missing support explicitly marked. Review receives diff, intent and reward-omitting summaries in a disposable copy. Delegated histories do not merge wholesale into the solver chat.
- Selection predicate: task routing chooses diagnoses; portfolio selects open incumbent/novelty proposals by attempts, age, breadth of task/window support and deterministic tie-break; gates filter constructed changes. An empty lane need not be filled.
- Invalidation or expiry: failed candidates are discarded; implementation-class rejection can receive one second build from the parent with the repair brief. Rebase conflicts reject the second candidate; tree-wide checks rerun after successful rebase. Lease recovery handles unfinished proposal attempts before reselection.
- Activation or effect: promotion renames staging into a numbered generation, archive synchronization is attempted, and the driver changes the library path used for later launches. This establishes a live self-change path, not observed dependence of later task behavior on a specific edit.
- Evidence limits: no full training trace or individual change efficacy was inspected. Model diagnosis/review compliance and causal improvement are uninspected. Admission is not a measured reward-improvement threshold.

Trigger/principal/owner: completed support tasks trigger the driver; software routing/portfolio selects work; investigator and implementer models propose explanations and code; software gates and reviewer verdicts can veto; the operator launches/configures the experiment but no per-content human approval is required by this shipped path. Guidance asks for a module-local counterfactual connecting observed divergence to an outcome, rejects unfounded tweaks, and separates a wrong direction from a bad implementation. The evidence-bearing proposed change is executable strategy, possibly including added helper capability, not production-kernel or model-weight revision. Sources: SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/portfolio.py`, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`, `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`.

> **Do NOT invent a marginal `{locked}` tweak just to have a
>      finding: a change that would not move the outcome is a regression waiting to
>      happen — no culprit is the correct, productive answer.**
> --- `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`

Admission progression: explicit commit with edits; smoke (syntax/import/library/bundle/discovery/static contracts) with bounded repair; action-shape and niche checks; model review; required-variant identification; forced-activation and crash sanity. Action checking is fail-open on internal error. Review accepts only an executed structured verdict as a substantive decision, not prose; nevertheless timeout/exception returns pass, and a missing verdict can pass until the breaker trips. Partial file dropping is disabled by the current review result even though downstream handling remains. Sanity rejects code crashes or missing required activation, not every failed task. A normal-routing probe is observational and never gates. Sanity-crash repair occurs after review; the repaired tree is smoke-checked and retried in the sanity loop without returning to the earlier reviewer/action/niche stages in this function. Thus even a non-skipped review does not establish review of the final repaired bytes. These branches qualify the stronger top-of-file comments (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/smoke_tests.py`).

> return _ReviewResult(
>             passed=True, verdict="skipped", reason="review timed out (infra)"
>         )
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> out.editor_n_edits += repaired.n_edits
>             out.files_changed = _changed(staging_modules)
>             # loop: re-run the sanity tasks on the repaired staging
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

> # parent_mean is the batch's IN-SAMPLE reward on the CURRENT gen — recorded
>     # for the evolution log as a reference only, never used to gate.
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

If two lanes pass, incumbent-first promotion is the default. The second lane is rebased; byte-identical diff permits reuse of change-local review, not tree-wide smoke/activation/routing results. Atomic rename is a filesystem transition, not a transaction with archive sync: sync failure leaves the generation standing. Confirmation later compares shared-task variant rates with baseline (defaults: at least three shared tasks, delta below minus 0.34) and marks regressors superseded; helper confirmation compares presence/absence. This is best-effort selection retirement, not deletion or complete restoration of all generation state, and it is not a randomized attribution study (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`, `src/harbor/agents/terminus_2_modular/self_evo/promotion.py`, `src/harbor/agents/terminus_2_modular/self_evo/staging.py`, `src/harbor/agents/terminus_2_modular/self_evo/confirm.py`).

> if on_promote is not None:
>         try:
>             on_promote(promoted, parent_gen, result)
>         except Exception as exc:
>             _logger.warning(
>                 "archive sync after promoting %s failed (the generation stands): %s",
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

Answer oracle and mode: bounded repeated support-task curriculum uses task verifier rewards to identify pass/fail contrast; investigators can use earlier passing trajectories or diagnose without a pass. The editor's file tools block named reward/answer-bearing trial files, while diagnosis instructions intentionally provide scalar verdicts. Reviewer prompts omit those rewards and ask for mechanism/overfit judgment. The sanity battery uses held-out task execution but gates crash/activation, not a reference solution's improvement score. Unfrozen datasets prevent an independent contamination assessment. Repair instructions may carry crash evidence; the driver log's blanket claim that the editor never sees held-out tasks is therefore not established merely by the support-path split (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/trajectory_analysis.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`).

Theory account: the source asks for explicit causal hypotheses and counterfactual criticism of harness behavior. Lane briefs expose the behavioral delta and causal hypothesis, not just a score. Findings, proposal support, repair briefs, outcomes and executable strategies can persist. A finding may instead be only a local observation; not every stored item is a theory. The following architectural assessments do not assert that a supplied model actually formulated a sound explanation.

> delta=proposal.behavioral_delta or "(not stated)",
>         why=proposal.causal_hypothesis or "(not stated)",
> --- `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`

- theory-builder conditions 1–4: condition 1 conclusion status: afforded. Named hypothesis/delta units and whole code strategies provide localized expression; actual generated theory content is uninspected here.
- theory-builder conditions 1–4: condition 2 conclusion status: wired. Brief construction supplies hypothesis content to implementers and review supplies intent plus diff; semantic dependence/compliance in actual model decisions remains uninspected.
- theory-builder conditions 1–4: condition 3 conclusion status: afforded. Instructions request evidence-directed counterfactual diagnosis and review separates proposal from implementation blame; structured repair briefs can redirect a second build. Actual content-directed criticism is uninspected; scores alone would not suffice.
- theory-builder conditions 1–4: condition 4 conclusion status: wired. Findings feed proposals and later briefs; implementation-class rejection feeds a second build; subsequent tasks can use promoted code. Iterated criticism of an actual formulated theory remains uninspected.
- Addressability: proposal fields, support findings and separately named module variants are inspectable/revisable units; arbitrary internal model assumptions remain opaque.
- Persistence: generation libraries and proposal/findings state can cross windows and resume; the released evaluation freezes a product rather than continuing that improvement loop.
- learning: improved future capacity and causal attribution are uninspected. Retention plus later consumption does not prove benefit.
- Reflection: implementation conclusion status: wired. Trajectories represent selected bundles, module calls and outcomes; those representations enter diagnosis and can change later harness code. Accurate self-diagnosis is uninspected.
- Reflective theory builder: conclusion status: uninspected. The module-improvement pathway does not by itself show that its own investigative/editor method texts undergo content-directed criticism and revision.
- Autonomous theory builder: conclusion status: afforded. Computation supplies diagnosis, proposal selection, implementation, review and promotion within the configured curriculum; reliable performance of every internal theoretical operation is not established.
- Self-improvement: dispositional improvement-directed self-change is wired within the builder-plus-solver boundary over successive task launches. Objective: task success, with efficiency secondary. Evidence is supplied to determine edits; promotion changes the system's own harness; later launches have a live executable authority path. Link 4, subsequent operation causally depending on a particular change, is uninspected here. Exercised self-improvement and successful improvement therefore remain unestablished independently of the README's attributed results.

#### RT-RTE-context-handoff
Label: Context compression and summarization subagents

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: replacement chat/handoff prompt and summarization trajectory references; the loop feeds the handoff to its next model call.
- Later read-back: summary-derived content enters subsequent invocations within the same task; this is retained context, not merely an unused log. Cross-task summary reuse is not established by this route.
- Delegated visibility: summary and answer calls receive selected history; the questions call receives task, summary and terminal information. Separate direct calls do not mutate foreground history until explicit replacement; only their outputs cross back.
- Selection predicate: code estimates remaining context and compares a proactive threshold; context-length exceptions trigger forced compression. The configured `enable_summarize` can disable it.
- Invalidation or expiry: old turns are removed from active chat by unwinding/replacement; recorded trajectories remain separate artifacts. Full-summary failure has shorter-summary/truncation fallbacks; exact removed information need not survive the handoff.
- Activation or effect: baseline replacement installs a compact question exchange and passes answer content as a continuation prompt; later model behavior dependent on particular retained details is uninspected.
- Evidence limits: this traces installed baseline wiring, not every released context-management variant or observed successful recovery. Summary fidelity and benefit are uninspected.

Owner/form/state: software triggers compression; model calls produce natural-language summary/questions/answers; symbolic replacement controls what remains in the window. The model component is [RT-CMP-lite-llm](#rt-cmp-lite-llm). This resembles isolated frames with selected inputs and output-only returns, but outputs are copied text, not dereferenceable pointers into an external heap. There is no automatic reload of an omitted turn established by the baseline handoff; saved trajectory references alone do not establish that reload (SRC-1, `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`, `src/harbor/agents/terminus_2_modular/modules/agent_loop/baseline.py`).

> chat._messages = [
>             chat.messages[0],
>             {"role": "user", "content": question_prompt},
>             {"role": "assistant", "content": model_questions},
>         ]
>         chat.reset_response_chain()
> --- `src/harbor/agents/terminus_2_modular/modules/context_mgmt/baseline.py`

### Claims

#### RT-CLM-harness-improvement
Label: Generalizable harness improvement claim

Claimed operation: use independent execution experience to improve the five-part harness and transfer gains to unseen tasks/domains/models. SRC-1, `README.md`, reports Terminal-Bench accuracy rising from 47.57% to 52.43% for its stated model and describes frozen downstream evaluation. Claim conclusion status: claimed. The implementation records above establish a change-and-consumption mechanism, not reproduction or component-level causal attribution of those numbers.

> Modern agent capability depends not only on the foundation model, but also on
> the harness that controls interaction, observations, context, tools, and task
> completion. ModularRSI decomposes this harness into five evolvable modules:
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-module-execution
Label: Retained Python becomes runtime behavior

Consumer: library loader, factories and selected module/helper methods. Channel: generation `modules/` files supplied through `modules_root`. Force: Python execution, first at discovery/import and later at instantiation and method calls. Horizon: next load/task and later generation consumers, unless files/status/selection change. This is stronger than prompt guidance; the code can determine parsing, context, command dispatch and stopping. Import-time execution precedes variant selection, so dynamic filtering is not an import sandbox (SRC-1, `src/harbor/agents/terminus_2_modular/library.py`, `src/harbor/agents/terminus_2_modular/self_evo/smoke_tests.py`).

> mod = importlib.util.module_from_spec(spec)
>             sys.modules[synthetic_name] = mod
>             try:
>                 spec.loader.exec_module(mod)
> --- `src/harbor/agents/terminus_2_modular/library.py`

The normal editor write boundary rejects frozen files, foundation basenames and writes outside staging, with a tools lock also allowing `tool_helper`. These checks mediate file actions; they do not constrain arbitrary effects of a subsequently imported Python body. The stale orchestration header's statement that orchestration itself is evolvable is not the release's operative mutation surface: the installed shim imports installed orchestration, and staging copies modules only (SRC-1, `src/harbor/agents/terminus_2_modular/agent.py`, `src/harbor/agents/terminus_2_modular/self_evo/staging.py`, `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`).

> if Path(rel_path).name in ("baseline.py", "active_bundle.json"):
>         return False
> --- `src/harbor/agents/terminus_2_modular/modules/tools/editor_file_tools.py`

#### RT-BAP-description-selection
Label: Descriptions influence executable selection

Consumer: dynamic composer model, then symbolic bundle-name validation and instantiation. Channel: filtered catalog text built from module descriptions plus task text. Force: advisory natural-language interpretation followed by executable selection within offered names; not guaranteed compliance with the descriptions' intended triggers. Horizon: current task's choice and later tasks that reload retained descriptions. Cache/static/forced paths can bypass fresh interpretation. This is distinct from the Python authority path because the text consumer can misinterpret or fall back without changing the stored implementation (SRC-1, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`; passage in [RT-OBJ-module-description](#rt-obj-module-description)).

## Annotations

none
