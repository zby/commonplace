---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Meta-n runtime baseline: evaluated recursive injections, native and external solving, admission gates and bounded controls."
run-id: AAS-2026-10-14-meta-n-18c23b6f8bb4-01
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
---

# Meta-n runtime report

## Runtime account

### Work and evidence

Meta-n builds task-solving chains by asking a model to generate Python preprocessing and helper source from evaluated solver traces. Its objective is higher task scores, not changes to model weights. The shipped CLI and benchmark callers are part of this improvement plane. All implementation findings below use SRC-1 at the frozen revision. No target invocation, test, provider request or experiment was executed or supplied as run evidence. Wiring does not establish activation, reliable compliance or improvement.

The model's instruction makes the objective and proposed change explicit:

> Given the execution traces and context of the system below you, produce code that improves its performance — specifically, that raises the MEAN CONTINUOUS SCORE across tasks. Treat a higher score as the goal even on tasks that already "pass": most tasks here are scored on a 0.0–1.0 continuum, not pass/fail. You do NOT solve tasks directly — you write code that helps the solver below you perform better.
> --- `meta_n/core/prompts.py`

This is design evidence, not proof that generated interventions generalize. Implemented scores can also be negative; aggregation filters non-finite scores rather than enforcing the prompt's typical range (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/archive.py`).

Additional implementation inspection beyond the boundary's initial excerpts covered `meta_n/core/solver.py`, `meta_n/core/agentic_solver.py`, `meta_n/core/code_library.py`, `meta_n/core/verified_code.py`, `meta_n/core/llm_client.py`, `meta_n/utils/safety.py`, `meta_n/utils/context_manager.py`, `meta_n/core/external_agents/injection.py`, `meta_n/core/external_agents/budget.py`, selected OpenHands/Terminus backend branches, `scripts/oh_runner.py`, and selected CO-Bench/classification subprocess consumers. These are additional paths within SRC-1, not additional sources. Upstream SDK policy and deployed Docker isolation remain external contracts. Setup scripts, all benchmark-specific algorithms and the post-run analysis utilities were not exhaustively audited; no conclusion here depends on their completeness.

### Ordinary native invocation

A representative ordinary path is the shipped `meta-n --tasks <json> --use-archive` CLI with native solving. Archive mode is required: a bare custom-task invocation without `--use-archive` is rejected before client construction or task loading. The bundled benchmark configuration enables archive mode by default; disabling that configuration also requires explicit `--use-archive` (SRC-1, `meta_n/main.py`). The operator supplies task descriptions, optional verification scripts, model/provider configuration and search options. `main.py` loads tasks, chooses bash plus `LocalExecutor`, constructs `LLMClient`, Ω and `EvolutionaryOrchestrator`, calls `run(..., resume=args.resume, run_config=run_config)`, and saves the result. Benchmark branches instead choose family-specific adapters/executors and Python, bash or OpenEvolve solution formats. This path is [RT-RTE-native-solve](#rt-rte-native-solve), not a sandboxed benchmark guarantee (SRC-1, `meta_n/main.py`).

> if not getattr(args, "use_archive", False):
>     console.print(
>         "[red]Error: --use-archive is required (the linear orchestrator has "
>         "been retired). The bundled benchmark config enables it by default; "
>         "pass --use-archive explicitly if you also pass --benchmark-config "
>         "none or run with bare --tasks.[/red]"
>     )
>     return 1
> --- `meta_n/main.py`

After valid archive configuration, the fresh-run baseline has candidate identity `gen0_seed`, depth 1 and no injection unless a seed library was supplied. Code owns scheduling. It generates one solver response per task, extracts executable source, executes it and produces a `Trace`. Tasks fan out under a semaphore; full evaluation gathers with `return_exceptions=True`, turns non-cancellation faults into failed traces, and computes finite-score aggregates. A seeded library changes the seed to a deeper candidate and routes it through the chain builder. Optional repeated evaluation chooses a median-scoring trace while accounting for all repeats' token usage. The return is an evaluated `Candidate`, not just the model's answer (SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

Subsequent generations use [RT-RTE-chain-admission](#rt-rte-chain-admission). Candidate IDs encode generation, parent slot and child slot; parent IDs preserve lineage. The archive first filters extendable candidates, then selects parents using elites and rank-normalized fitness plus UCB exploration. Ω receives sampled traces, selected prior code, task descriptions, score comparisons and optional inspiration. It returns parsed `InjectedCode`; code constructs a child chain by appending the injection. Model interpretation proposes strategies and code; software owns execution, comparison, vetoes and continuation.

Native composition is nested but not a recursive cascade of independent model agents. Each `MetaLayer` executes its preprocessing and passes context to its inner solver. A normal inner layer returns source rather than executing it. The outermost layer stages the merged helper library and executes the resulting source. Later layers override earlier helper names. Only the outermost layer gets the configured retry loop. Preprocessing executes deepest-first; textual emissions can condition shallower preprocessing via `outer_context`. Turning off that inter-layer input does not remove accumulated guidance from the final solver prompt (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/evolutionary_orchestrator.py`).

> script, reasoning, tokens = await self.inner_solver.solve(task, context)
> script = self._prepend_library(self._maybe_deploy_verified_helper(script))
> return script, reasoning, tokens, context, False
> --- `meta_n/core/meta_layer.py`

Failed local execution can trigger bounded self-debug retries; the layer keeps the best score, not necessarily the last attempt. Search stops on configured iteration/depth limits, patience or external-spine budget headroom. It reports best-chain and per-task-best/oracle results, may assemble a frozen routing candidate, and optionally evaluates stored solutions or reconstructed chains on adapter test splits. Those are distinct terminal products; an oracle assembled from several chains is not evidence that any single chain achieved its score (SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

### Durable continuation and other consumers

Evaluated candidates are saved immediately. Each candidate directory contains its summary, traces and the full injected chain; prompt/response sidecars and telemetry expose request lineage where available. Checkpoints carry loop state, RNG state, usage and admission bars. Resume rebuilds the archive, restores RNG and counters, and skips completed candidate IDs. Invalid or empty checkpoint reconstruction falls back to fresh search. Configuration drift is warned and recorded, but current resumed values win; resume is not exact replay under immutable configuration. Candidate files are ordinary writes, so checkpointing and idempotent IDs do not establish an atomic multi-file transaction (SRC-1, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`, `meta_n/core/evolutionary_orchestrator.py`).

Archive traces and code reach later Ω invocations; chains reach later solves. The runtime admission records below name this horizon without duplicating the memory analyst's storage/revision account. Test-split consumers are also material alternate paths: oracle test evaluation re-executes per-task-best stored scripts, whereas chain test evaluation can obtain test tasks and call the reconstructed solver again. They are not all routed through the generation gate or helper-verification gate (SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

### Selected forcing routes and control coverage

Four forcing cases bound the account:

1. **Host execution despite sandbox language.** Custom tasks use `LocalExecutor`; preprocessing always uses host-side Python execution; native CO-Bench/classification solve evaluation includes separate host Python processes and injected `llm()`/`llm_batch()` callbacks. A process timeout or a scratch namespace is not OS isolation. [RT-CLM-host-boundary](#rt-clm-host-boundary) distinguishes these paths.
2. **`verified_code` without a value oracle.** The fallback verifier keeps every Python helper unverified. Even with a real verifier, dependency closure can restore a sibling that failed as an entry point; preprocessing and bash helpers pass through. [RT-RTE-helper-verification](#rt-rte-helper-verification) is not a universal proof of safe or correct injected code.
3. **Alternate next-step owners.** Native agentic mode uses repeated model-generated actions and observations; external-spine mode bypasses native `MetaLayer` composition. OpenHands receives a system suffix and a terminal/file-editor tool grant; Terminus 2 folds injection into instruction context. [RT-RTE-agentic-loop](#rt-rte-agentic-loop) and [RT-RTE-external-spine](#rt-rte-external-spine) have different controls and return contracts.
4. **Frozen scores versus fresh execution.** Consolidation inherits non-focus traces without re-solving; Ω_merge assembles stored winners with no new evaluation. Native `MetaLayer` can execute a frozen task script without any model call or retry. The external injection mapper instead consumes preprocessing/libraries, not that native frozen-script shortcut. [RT-RTE-frozen-routing](#rt-rte-frozen-routing) does not establish cross-backend replay parity.

The capacity surface therefore includes model-written Python/bash, host Python preprocessing, host subprocesses, optional inner provider calls, SDK terminal/file editing, and adapter/environment callbacks. Current grants are configuration-specific; no actual deployment grant or environment was supplied. OpenHands' inspected standalone runner grants terminal and file editor, disables browser registration and does not include sub-agent tools. Its default host-runner branch and opt-in container branch differ materially. Even its container path mounts writable workspace/run directories and passes the provider key; it is not the verifier's network-disabled container. Upstream tool execution and Docker isolation require their own contracts (SRC-1, `scripts/oh_runner.py`, `meta_n/core/external_agents/backends/openhands.py`).

### Load-bearing guarantees

| Guarantee and owner | Enforcement and strength | Covered paths; counterpaths and external contract | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|
| Generation quality gate; orchestrator | `gate_tasks > 0` and no focus task invokes `_gate_check`; policy | Sampled tasks only. Default floor-off mode passes on first success clearing relative score threshold; missing baseline is liveness-only. Optional floor scans for veto. Consolidation, disabled gate, seed, downstream repair and frozen assembly are not the same gate. Depends on evaluator scores/success semantics. | wired | uninspected |
| Preprocessing screening; shared pipeline | AST blocklist, thread join timeout and string-result check; best effort | Shared by native, agentic and external injection. Abandoned daemon thread is not killed. Task deep-copy failure falls back to a shared reference. Does not screen final solver source or establish a Python security sandbox. | wired | uninspected |
| Helper value check; orchestrator/verifier | Real verifier invokes network-disabled, read-only/resource-bounded Docker runner and trusts returned JSON; protocol | Python helpers under enabled verification with a real family oracle. Pass plus status-derived sandbox bit stamps names, not authenticated helper execution. Stub keeps all; dependencies can be restored; bash/preprocessing bypass it. Requires trustworthy runner output and Docker/image/oracle correctness. | wired | uninspected |
| Budget admission; `LLMClient`/external `CostGuard` | Outer client checks cap before each request attempt; spine checks before admission and after lease wait; policy | Native/shared helper requests through the client and metered external returns. In-flight spend may overshoot; hard-killed/opaque results can undercount. No external per-run USD kill. Arbitrary generated shell/provider access is not covered by the client wrapper. | wired | uninspected |
| External fault containment; solver/lease | Guarded plan build and lease body, time envelope, degraded trace and telemetry; protocol | Cancellation deliberately propagates; telemetry creation precedes guarded plan build. Requires backend/provider teardown and recoverable metrics. Not an invariant that every fault everywhere produces a complete record. | wired | uninspected |
| Native custom-task timeout; `LocalExecutor` | Child process group kill plus bounded pipe drain; protocol | Bash and verification subprocess paths. Escaped sessions/descendants need not die. Does not limit host filesystem/network effects. | wired | uninspected |

Evidence for these bounds is retained in the linked route/claim records below. No approval mechanism here should be read as per-candidate human approval: operators configure/start/resume the bounded experiment; models propose content and code admits it. Human review before deployment into some separate production system is outside the shipped admission path inspected here.

## Shared records

### Components

#### RT-CMP-llm-client
Label: Shared outer model client

Source-native identity: `LLMClient` and configurable `LLMConfig`; Ω generation, native solving, native agentic turns and summaries use it. Representational form: distributed-parametric inference behind a symbolic API; messages are natural-language/source text, not parameters. Storage substrate: remote provider/deployment state, outside this checkout. Parameters changing during operation: no inspected training/update call; upstream changes uninspected. Exact version pinned: no immutable weights revision established by a configured model/deployment name. Mutable endpoint can resolve another model: unresolved provider-side mapping; base URL and model are operator configurable. Provider internals remain uninspected (SRC-1, `meta_n/core/llm_client.py`).

> response = await self._client.chat.completions.create(
>     model=self.config.model,
>     messages=messages,
>     extra_body=eff_extra_body,
>     **temperature_kwargs,
>     **token_kwargs,
>     **seed_kwargs,
> )
> --- `meta_n/core/llm_client.py`

#### RT-CMP-inner-llm
Label: Generated-solver model callbacks

Source-native identity: `llm` and `llm_batch` closures supplied to native benchmark solve namespaces. Distinct invocation responsibility from [RT-CMP-llm-client](#rt-cmp-llm-client), not proof of distinct weights: main-process closures can share the client; subprocess closures lazily create a client from the configuration. Representational form: distributed-parametric model inference exposed by symbolic callable interfaces. Storage substrate: remote provider state, plus ephemeral callback/tracker state. Parameters changing during operation: no callback training operation inspected. Exact version pinned: not established. Mutable endpoint remapping: provider-side resolution uninspected; inherited configuration is not an immutable weights pin (SRC-1, `meta_n/core/llm_helpers.py`, `meta_n/integrations/co_bench.py`, `meta_n/integrations/text_classification.py`).

> config = LLMConfig(**config_dict)
> _client_holder["client"] = LLMClient(config)
> --- `meta_n/core/llm_helpers.py`

#### RT-CMP-external-backend
Label: SDK-managed model inference

Source-native identity: OpenHands/Terminus 2 backend model calls. This is the external model invocation responsibility, not a claim that both backends share one parameter set. Representational form: distributed-parametric provider inference; symbolic SDK control and tool interfaces. Storage substrate: provider models and SDK process state. Parameters changing during operation: no Meta-n training call in the inspected bridges; SDK/provider internals uninspected. Exact version pinned: configured model identifier and dependency locks do not pin weights. Mutable endpoint remapping: possible through configured API base/model; actual resolution uninspected. External spend and inference bypass the outer client's per-request accounting; returned metrics are folded later (SRC-1, `meta_n/core/external_agents/budget.py`, `scripts/oh_runner.py`, `scripts/t2_runner.py`).

> * **OpenHands** reports a *native* USD figure (litellm's ``accumulated_cost``)
>   because its LLM calls go through its own litellm client, never meta-n's
>   ``LLMClient``. That USD is appended to the ledger verbatim via
>   :meth:`CostTracker.record_usd` (``cost_basis="native_usd"``).
> --- `meta_n/core/external_agents/budget.py`

### Operative objects

#### RT-OBJ-pre-process
Label: InjectedCode preprocessing source

Source-native identity: `InjectedCode.pre_process`. Representational form: symbolic Python whose execution emits natural-language `additional_context`; the source and its emission have different consumers. Storage substrate: in-process objects and saved injection JSON. Host execution is screened, not sandboxed. The emitted string reaches native solver context or external prompt suffix. It may embody inspectable strategy rules; delivery alone does not establish model compliance (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/external_agents/injection.py`).

> namespace = {
>     "task": task_view,
>     "additional_context": additional_context,
>     "outer_context": next_outer,
> }
> --- `meta_n/core/meta_layer.py`

#### RT-OBJ-code-library
Label: Injected helper source

Source-native identity: `InjectedCode.code_library` and `code_library_bash`, grouped as the merged library container, not as identical verification classes. Representational form: symbolic Python/bash source; function signature/docstring advertising is model-interpreted text. Storage substrate: injection objects/JSON, native prepended source or external staged helper files. Later layers overwrite same-name helpers. Python and bash checks differ; [RT-RTE-helper-verification](#rt-rte-helper-verification) assesses the Python-only value gate (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/code_library.py`, `meta_n/core/external_agents/injection.py`).

> for ic in injected_codes:
>     merged_py.update(ic.code_library)
>     merged_bash.update(ic.code_library_bash)
> return merged_py, merged_bash
> --- `meta_n/core/meta_layer.py`

#### RT-OBJ-rationale
Label: Generated rationale

Source-native identity: `InjectedCode.rationale`. Representational form: natural-language explanation requested from Ω. Storage substrate: parsed objects and durable injection JSON/response sidecars. It is displayed and included in later Ω context-stack formatting, not directly executed as helper code. No supplied rationale instance demonstrates formulated criticism or explanatory reach (SRC-1, `meta_n/core/prompts.py`, `meta_n/core/omega.py`, `meta_n/core/run_persistence.py`).

> ```rationale
> <your reasoning about what patterns you see and what improvements to make>
> ```
> --- `meta_n/core/prompts.py`

#### RT-OBJ-task-solution-map
Label: Frozen per-task source map

Source-native identity: `InjectedCode.task_solution_map`. Representational form: symbolic task-ID-to-script mapping. Storage substrate: synthesized injection object/JSON built from per-task-best traces. Native consumption bypasses prompting, library prepend and retries for a matching task. Its provenance is evaluated stored scripts, not a fresh Ω proposal. Identity-specific dispatch should not be confused with the prompt's instruction to generalize preprocessing across task structure (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/meta_layer.py`).

> frozen = self.injected_code.task_solution_map.get(task.task_id)
> if frozen:
>     return frozen, "frozen Ω_merge winner (no re-solve)", 0, additional_context, True
> --- `meta_n/core/meta_layer.py`

### Routes

#### RT-RTE-native-solve
Label: Native solve and execute

Valid archive-enabled CLI configuration (`--use-archive` explicitly for bare custom tasks, or enabled by benchmark configuration) → operator/adapter tasks → `Layer1Solver` → provider completion → extracted script → selected executor → `Trace`; orchestrator owns scheduling and aggregation. Natural-language problem/context is interpreted by the model, extraction and execution are symbolic control. LocalExecutor runs bash on the host; benchmark executors can evaluate Python functions and use inner model callbacks. Local verification is a supplied script whose zero exit is the reference outcome; benchmark answer oracles are adapter-specific evaluators/data, not the proposal model. Operating mode: bounded task evaluation inside search. Local retries are an optional outer-layer debug loop with evaluator feedback; no per-script human veto is wired (SRC-1, `meta_n/main.py`, `meta_n/core/solver.py`, `meta_n/core/base_executor.py`, `meta_n/core/meta_layer.py`, `meta_n/core/evolutionary_orchestrator.py`).

- Immediate return: script/reasoning/tokens from `solve`; evaluated trace/tokens from outer `execute` or orchestrator dispatch.
- Later read-back: saved traces and source can supply later Ω generation, inspiration, frozen routing and test evaluation.
- Delegated visibility: provider sees rendered task and context; selected executor sees script/task; ordinary nested layers return source without executing it.
- Selection predicate: language metadata selects template/extractor; candidate depth, agentic flag and spine predicate select dispatch.
- Invalidation or expiry: invocation-local prompt state ends with solve; traces persist under candidate identity without automatic content expiry.
- Activation or effect: generated source is passed to the selected executor; retry guidance reaches another model call when low score triggers configured retries.
- Evidence limits: implementation only; solver correctness, verification-script validity and deployed host privileges unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if success and task.verification_script:
>     success = await self._verify(task.verification_script, timeout=10)
> --- `meta_n/core/base_executor.py`

#### RT-RTE-chain-admission
Label: Trace-fed chain generation and selection

Archive candidate → sampled Ω request → parsed injection → child chain → optional gate → full evaluation → archive and later parent selection. Ω proposes; orchestrator/Archive decide. Software can skip empty injections, reject gate failures, filter helpers and bar particular per-task-best promotions. Operators choose configuration and can restart with changed values; inspected admission needs no per-content human decision. Answer oracle: adapter evaluator or supplied verification outcome produces scores/success; archive per-task-best is a selection aggregate, not an independent expected-answer oracle. Operating mode: bounded experiment/curriculum over supplied tasks, triggered by each generation (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/archive.py`, `meta_n/core/omega.py`).

Admission is not simply “only improvements survive.” Full-evaluated children are archived even when worse; breedable filtering has seed/elite exemptions and fallbacks. Optional non-adoption bars alter the per-task-best index, not candidate mean or history. Gate passes on one clearing sample unless a floor requires scanning; it cannot warrant all-task non-regression.

- Immediate return: parsed injection from Ω and evaluated child candidate; gate failure returns traces for possible repair rather than an admitted child.
- Later read-back: accepted candidate traces and full injected chains feed later Ω calls, chain solves and resumed selection.
- Delegated visibility: Ω sees sampled/truncated views, task summaries, scores and optional inspiration; solver consumes full live chain, not only Ω's truncated view.
- Selection predicate: depth eligibility and breedable pool, elite reservation/weighted sampling, optional gate, finite-score aggregation and separate per-task-best ranking.
- Invalidation or expiry: configured max depth/iterations/patience halt breeding; retained candidates have no automatic expiry. Same-name helper overrides affect later chains, not prior candidate identity.
- Activation or effect: constructed child chain is evaluated before ordinary archive admission; later selection can reuse its strategy and helpers.
- Evidence limits: runtime source establishes this update capacity, not successful model proposals, actual criticism, generalization or causal score improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposed change/guidance: each breeding step asks Ω to improve score using traces, prior injections and the fixed objective/generalization instructions. Persisted results are executable/textual interventions, rationale and outcomes, not changed model parameters. Recovery: earlier candidates remain available; gate-rejected children are not mutated into their repairs; resume restores archive state. There is no inspected automatic rollback of effects already incurred during generated execution.

> child = Candidate(
>     candidate_id=child_id,
>     parent_id=parent.candidate_id,
>     iteration=iteration,
>     depth=child_depth,
>     injected_codes=parent.injected_codes + [injected],
>     temperature_used=temperature,
>     total_tokens=omega_tokens,
> )
> --- `meta_n/core/evolutionary_orchestrator.py`

> if protect is None:
>     return True, gate_n, gate_traces
> --- `meta_n/core/evolutionary_orchestrator.py`

Theory account: executable strategy rules can state localized candidate guidance; model calls are asked to infer patterns and revise interventions, but a score comparison is not itself content-directed criticism. Guidance applied is the fixed Ω method prompt; derived/revised material is candidate code and rationale. That fixed method prompt is not automatically revised by this route.

- theory-builder conditions 1–4: condition 1 implementation conclusion status: afforded — a whole preprocessing rule or helper unit can express a strategy; actual generated theory content uninspected. Condition 2 implementation conclusion status: wired — Python rule contents determine emitted context and helper execution; model dependence on prose alone remains unobserved. Condition 3 conclusion status: claimed — requests for failure-pattern analysis/revision do not establish a criticism naming claim, result and blame in an actual output. Condition 4 conclusion status: afforded — retained revised chains can shape later rounds; iteration of content-directed criticism remains unobserved.
- Addressability: preprocessing/helper units and same-name replacements are inspectable and revisable; model weights are not. Fine-grained assumptions/rationale structure depends on unsupplied generated content.
- Persistence: interventions and rationale survive rounds and disk resume of the experiment; portable deployment/benefit across new problems unestablished.
- learning: wired capacity to retain behavior-shaping changes; improved future capacity and attribution unestablished without outcomes and a comparison.
- Reflection: source affords a representation-mediated feedback path from solver traces/injections to subsequent candidate organization; actual faithfulness and exercised feedback unobserved.
- Reflective theory builder: uninspected — fixed method texts are not revised through this route; content-directed criticism of its method is not established.
- Autonomous theory builder: uninspected — computation owns proposal, comparison and continuation, but that does not establish all theory-builder operations occurred.
- Self-improvement: dispositional, improvement-directed self-change is wired within the bounded Meta-n experiment, whose independently stated objective is higher task score. Trace evidence shapes the Ω request; chain organization is replaced/extended; preprocessing and helpers have live consumers. Subsequent execution causally depending on a particular change (link 4), and successful improvement, are unestablished. This is not exercised self-improvement or an attribution to model-weight learning.

#### RT-RTE-helper-verification
Label: Python helper filtering and adoption

Enabled verification → family verifier → kept Python helpers plus dependency closure → chain builder. Software owns admission and per-task-best bars; the model proposes helper content. Oracle: real family held-out value harness when supplied by adapter, otherwise none. Stub model-independent pass-through is not a value oracle. Operating mode: optional bounded helper test before injection, distinct from full candidate evaluation (SRC-1, `meta_n/core/verified_code.py`, `meta_n/core/evolutionary_orchestrator.py`).

- Immediate return: possibly replaced injection and `sandbox_verified_names`, the helper-name set stamped when verifier `passed` and `ran_in_sandbox` are both true; this is check-result metadata, not authenticated helper-call evidence.
- Later read-back: stamped verified names survive in injection records and inform later override-aware non-adoption checks.
- Delegated visibility: verifier gets candidate source, prior sources and sibling helpers; solver gets staged source and filtered descriptions, not a complete correctness proof.
- Selection predicate: enabled flag, nonempty Python library, verifier pass result, then transitive dependency closure; stamped advertised-but-syntactically-uncalled helpers can bar fresh task best promotion. The stamp depends on a status-derived bit and trusted JSON, not independently proven helper execution.
- Invalidation or expiry: same-name unverified overrides clear previous verification in the merged live-name accounting; no general time-based expiry.
- Activation or effect: kept helpers enter solver staging; native foster-adoption wording requests calls, optional deploy fallback can replace authored Python solve source with a wrapper.
- Evidence limits: preprocessing/bash are not value-verified; stub-kept and restored dependencies need not individually pass; source scanning measures syntactic call evidence, not runtime call proof. Real-harness value warrant is conditional on trustworthy runner output: last-line JSON is parsed without first rejecting a nonzero process return code, and the sandbox bit does not independently authenticate helper execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The real harness differs from the stub, but its result channel does not establish the stronger provenance suggested by the source's “genuinely verified” comments. `_docker_run_json` accepts the last nonempty stdout line as JSON without first rejecting a nonzero return code. `ran_in_sandbox` is derived from whether returned status differs from `exec_error`; timeout/no-JSON can retain true. The orchestrator stamps a name only on pass plus that bit. Thus best-index bars use implemented check/stamping metadata. A passing value assessment remains conditional on authentic runner measurements; neither authenticated helper execution nor an exploit is established here (SRC-1, `meta_n/core/verified_code.py`, `meta_n/core/evolutionary_orchestrator.py`).

> result = json.loads(last)
> --- `meta_n/core/verified_code.py`

> ran_in_sandbox = result.get("status") != "exec_error"
> passed = bool(self.success_predicate(result))
> --- `meta_n/core/verified_code.py`

> if res.passed:
>     kept[name] = source
>     if res.ran_in_sandbox:
>         sandbox_verified.add(name)
> --- `meta_n/core/evolutionary_orchestrator.py`

Trigger/change/guidance: Ω helper proposal under `verified_code`; fixed verifier/test harness supplies admission criteria. Verifier failures can drop helpers; dependency restoration limits rejection strength. Recovery retains the original archived lineage; the local pending injection is filtered before building a child. No per-helper human approval is implemented here. Deploy fallback is native-layer-specific, Python-only and conditional on staged helpers; it is not an external SDK guarantee.

> return VerifyResult(
>     passed=True,
>     evidence="no held-out harness (stub) — kept UNVERIFIED",
>     ran_in_sandbox=False,
> )
> --- `meta_n/core/verified_code.py`

> for dep in called:
>     if dep not in kept:
>         kept[dep] = injected.code_library[dep]
>         frontier.append(dep)
> --- `meta_n/core/evolutionary_orchestrator.py`

#### RT-RTE-agentic-loop
Label: Native action observation loop

`use_agentic` replaces native nested solver execution with `AgenticSolver`: preprocessing/library guidance → conversation → parsed model code → executor → observation → repeat → best trace. Code owns turn limits, parsing, score tracking and compaction triggers; the model selects proposed next code and completion signals. Context/state is a per-task message list, reasoning log, best trace and usage counters. Grant is generated source through the selected executor, not a native API tools list. Oracle remains the executor's benchmark/verification outcome, distinct from model completion assertions. Operating mode: bounded task experiment (SRC-1, `meta_n/core/agentic_solver.py`).

- Immediate return: best evaluated trace and total model tokens; `solve` can invoke this loop and return raw winning source instead.
- Later read-back: prior-work summary replaces aged-out messages for subsequent turns; final trace enters candidate persistence and later Ω calls.
- Delegated visibility: compaction model receives removed conversation text; foreground turn receives first message, summary and last four messages. No sub-agent worker launch is needed for this compaction call.
- Selection predicate: 85% chars/4 context estimate triggers summarization; 95% estimate stops before the next call; max turns and optional real-token spend cap also bound the loop.
- Invalidation or expiry: old message bodies leave the model window after successful summary; no per-task reload route is wired here. Invocation frame ends on return.
- Activation or effect: source is executed and evaluation feedback reaches later model turns; summary replaces context if returned successfully.
- Evidence limits: compaction fidelity and actual strategy changes unobserved; heuristic context budget is not a provider token invariant or a USD cap.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery includes parse-error feedback, caught call/summary errors, two-stage completion checks and best-trace retention. These are protocol choices, not reliable model completion guarantees. Per-task frames keep other tasks' current conversation out; only returned traces/counters escape into the enclosing search. The frame analogy does not imply reference-following access to removed turns (SRC-1, `meta_n/core/agentic_solver.py`).

> return [
>     first,
>     {
>         "role": "user",
>         "content": f"## Prior work summary\n{summary}",
>     },
>     *keep,
> ], summ_tokens
> --- `meta_n/core/agentic_solver.py`

#### RT-RTE-external-spine
Label: External agent lifecycle

Shared spine predicate selects external OpenHands/Terminus 2, or adapter-advertised builtin; this branch precedes agentic/native chain construction. Candidate injection → `InjectionMapper` plan → cost admission → lease/provision → helper staging → backend run → metric collection → solution extraction → scorer → trace and telemetry. Orchestrator owns task scheduling; SDK model/tool loop owns next actions inside each backend run. External run IDs, candidate/task identities, phase/repeat and lease workspaces distinguish concurrent evaluation. Plans carry symbolic helper files and natural-language prompt prefix/suffix, not native nested-layer execution (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/external_agents/solver.py`, `meta_n/core/external_agents/injection.py`).

- Immediate return: evaluated trace; OpenHands/Terminus return zero outer tokens, with agent usage tracked separately; builtin spine returns its native outer token count.
- Later read-back: durable trace/telemetry and copied logs remain available to archive consumers; model-visible read-back is the later Ω trace path, not reuse of the SDK conversation demonstrated here.
- Delegated visibility: backend gets instruction, prompt, workspace handle, limits and log directory. OpenHands suffix reaches `AgentContext`; Terminus combines suffix/prefix into instruction context. Staged helper availability differs from model adoption.
- Selection predicate: shared spine/backend/adapter predicate, budget headroom, semaphore lease and injection staging checks; scorer supplies task result.
- Invalidation or expiry: environment/lease teardown removes scratch working state; durable logs are copied before reaping where available.
- Activation or effect: backend tools can edit/execute in the chosen environment; helper staging and prompt supply are wired but helper use/benefit is unobserved.
- Evidence limits: no SDK or Docker run evidence; no universal container boundary, USD ceiling or equivalence of suffix/prefix semantics across backends.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Oracle: family scorer/evaluator, not the SDK's assertion of completion alone. Operating mode: bounded task trials within candidate search. Software admits each run after cost checks; human contribution is configuration/start, not per-action approval shown in these wrappers. Default standalone OpenHands tools are terminal and file editor, without browser or sub-agent tools. Host mode can shell outside its scratch directory; opt-in Docker mode changes that envelope but retains writable bind mounts and provider connectivity. Capability is broad execution; the grant and deployed isolation must be assessed separately.

> tools = [Tool(name=TerminalTool.name), Tool(name=FileEditorTool.name)]
> --- `scripts/oh_runner.py`

> ctx = AgentContext(system_message_suffix=suffix) if suffix else None
> --- `scripts/oh_runner.py`

> if not self.sandbox:
>     if self.provider_env_var and self._api_key:
>         env[self.provider_env_var] = self._api_key
>     argv = [self._py, self._runner, *self._runner_flags(
>         ctx, ws, instr_f, suffix_f, res_f, self.api_base or ""
>     )]
>     return argv, env, ""
> --- `meta_n/core/external_agents/backends/openhands.py`

Failure recovery: guarded plan/lease faults become degraded traces; cancellation propagates. Outer wall envelope exceeds backend hard timeout plus grace, preserving normal timeout metrics when possible. SDK/backend teardown remains an external contract. Admission rechecks after waiting do not reserve an exact maximum cost for all in-flight work.

#### RT-RTE-within-refine
Label: Gate-failure injection repair

Failed gate → optional `OmegaEngine.refine` → new repaired injection/candidate → re-gate → full evaluation/archive if passing. Trigger requires enabled within-layer refinement, nonempty injection, non-focus candidate and depth at least 2. Ω proposes repair; code can veto empty/still-failing output. Reference outcome is the same evaluator/gate, not an independent repair oracle. Operating mode: one bounded extra error-correction attempt, not an open-ended editor (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/omega.py`).

- Immediate return: repaired candidate or none, with spend accounted even on rejection.
- Later read-back: admitted repaired chain and SelfRepairEvent can survive subsequent search and persistence.
- Delegated visibility: Ω sees failing gate traces, buggy injection, lower chain, score comparisons and fixed repair directive; missing failure traces prevent the repair call.
- Selection predicate: feature flag and gate-failure conditions, then re-gate acceptance; rejected original is not archived by this branch.
- Invalidation or expiry: original rejected proposal is not overwritten; earlier admitted parents remain recoverable.
- Activation or effect: a passing repaired chain is evaluated and can enter future selection.
- Evidence limits: requesting bug repair is not evidence that the model diagnosed the correct cause or produced content-directed criticism.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/change/guidance: replace the newest buggy layer under a fixed fix-the-bug directive; software reuses the gate and helper filtering, no per-repair human approval. Persisted material is code/rationale/outcomes and repair metadata. Theory properties inherit no proof from the label “self-repair”: localized proposal capacity is afforded, consumption wired, criticism claimed, criticism iteration unobserved; learning or exercised self-improvement is not demonstrated. Recovery is retention of prior admitted candidates, not reversal of already executed effects.

> prompt = self._refine_directive(prev_injection, mean_before) + "\n\n" + base_prompt
> --- `meta_n/core/omega.py`

#### RT-RTE-downstream-repair
Label: Intermediate layer repropagation

Enabled post-admission repropagation at depth at least 3 → selected intermediate depth → Ω regeneration using full-chain failures and higher-layer feedback → same-depth replacement in a new chain → full evaluation/archive. Ω proposes; code selects target depth and classifies result. Unlike within-layer repair, the nonempty evaluated variant is archived even without improved mean; the accepted event flag is not an archive veto. Oracle is evaluator score comparison. Operating mode: bounded additional experiment after an admitted child's failure/plateau trigger (SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

- Immediate return: new repropagation candidate or none for empty/unavailable target, and token spend.
- Later read-back: old and new chains plus classified SelfRepairEvent persist for subsequent selection and inspection.
- Delegated visibility: Ω gets lower-chain context, full-chain traces and above-layer injections; attribution is contaminated by those above layers rather than a clean intervention on one cause.
- Selection predicate: feature flag, depth and `_should_repropagate`, chosen intermediate target; mean comparison classifies acceptance after evaluation.
- Invalidation or expiry: replaces one unit only in the new candidate; old child remains unchanged and archived.
- Activation or effect: reconstructed chain is evaluated through selected native/agentic/spine solver builder.
- Evidence limits: no observed repair or attribution; showing higher-layer feedback does not prove successful blame localization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposed change is one intermediate injection, guided by fixed error-correction instructions and downstream context. Software filters helpers, rejects empty regeneration, and retains nonempty evaluated results; no human per-change approval. Persisted code and trace/event evidence allow later rounds, not proof of theory criticism. Condition 1 strategy-unit capacity is afforded; condition 2 executable consumption wired; condition 3 requested criticism claimed; condition 4 iteration of actual criticism unobserved. Addressability is at injection/helper unit level. Persistence reaches rounds/resume; learning, autonomous/reflective theory building and successful self-improvement remain unestablished independently.

> new_chain = below + [new_injection] + above
> --- `meta_n/core/evolutionary_orchestrator.py`

#### RT-RTE-frozen-routing
Label: Consolidation and frozen winner consumption

Per-task-best index → inherited non-focus traces or assembled `merge_oracle` → saved source map → native task-ID dispatch. Software, not Ω, assembles the merge. Consolidation asks Ω to focus on one task while inheriting the rest; the merged product joins winners from different lineages without a new model call/evaluation. The archive “oracle” is the achieved per-task-best aggregate, not an expected-answer provider. Operating mode: bounded experiment with frozen reuse and optional terminal assembly (SRC-1, `meta_n/core/evolutionary_orchestrator.py`, `meta_n/core/meta_layer.py`, `meta_n/core/archive.py`).

- Immediate return: precomputed traces during consolidation; synthesized candidate/map at merge; matching native task returns frozen script and zero model tokens before execution.
- Later read-back: persisted map can reconstruct native dispatch; retained traces also support test re-execution.
- Delegated visibility: native matched task bypasses the solver model entirely; external mapper does not implement this map shortcut.
- Selection predicate: focus task chooses fresh work; merge needs multiple tasks and distinct winning sources plus optional range-relative gap test; native consumption requires matching task ID and nonempty script.
- Invalidation or expiry: copied winners keep stored source; stochastic execution, changed task/evaluator/environment can invalidate reproduction of the recorded score, with no freshness proof here.
- Activation or effect: native executor receives frozen source without prepend/retry; assembly itself has no fresh execution effect.
- Evidence limits: stored mean is by construction, not a new observed result; unseen-task generalization and external-backend dispatch parity are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/change/guidance: index selection and deterministic assembly admit a routing capability; code rejects degenerate/insufficient maps, retains contributing candidates and excludes maps from future breeding. No model-generated rationale or per-map human approval is needed; fixed algorithm guides assembly. Rollback is selecting retained earlier candidates, not undoing task effects.

> if was_frozen:
>     trace = await self.executor.execute(exec_script, task)
>     trace.depth = self.depth
>     trace.reasoning = reasoning
>     trace.duration_s = time.time() - start
>     return trace, 0
> --- `meta_n/core/meta_layer.py`

### Claims

#### RT-CLM-host-boundary
Label: Sandbox scope is path-specific

Claimed operation: prompt doctrine describes helper execution in a sandbox, but implemented host paths prevent a whole-system sandbox guarantee. Owner/enforcement: executor/environment choice supplies process/container boundaries; safety module only screens some host code. Guarantee strength: best effort for screening, deployment guarantee only conditional on actual external container/OS configuration. Covered paths: preprocessing blocklist and host helper smoke tests, LocalExecutor timeout, native benchmark subprocesses, optional backend containers. Alternate paths: generated solver source, bash helpers, host SDK terminal tools and inner provider callbacks do not share one universal screening point (SRC-1, `meta_n/utils/safety.py`, `meta_n/core/meta_layer.py`, `meta_n/core/base_executor.py`, `meta_n/core/code_library.py`, `meta_n/integrations/text_classification.py`, `meta_n/integrations/co_bench.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> Host-exec reality: ``smoke_test_function`` (and the pre_process pipeline in
> meta_layer.py) exec model-emitted code in the meta-n HOST process, gated only
> by this static validation plus a wall-clock bound — not by the Docker sandbox.
> --- `meta_n/utils/safety.py`

> except Exception:  # non-deepcopyable metadata — degrade to shared reference
>     logger.warning("pre_process: task deep-copy failed; sharing live task")
>     task_view = task
> --- `meta_n/core/meta_layer.py`

The copy fallback prevents an unconditional read-only-task invariant. Abandoning a timed-out thread returns control but does not terminate that thread. Static AST checks also are not a complete security boundary; no attack was executed to assess exploitability.

#### RT-CLM-budget-bound
Label: Budget controls bound admission and proven spend

Claimed operation: daily budget and token/turn limits bound selected requests and dispatch, not every generated action's true cost. Owner: client/CostGuard for ledger admission, backend runners for time/token constraints. Guarantee strength: policy plus bounded execution protocols. Covered paths and limits: shared client checks before retries; spine admission and after-wait headroom check; external metrics folded after backend returns. Provider-native SDK requests bypass client checks; killed/unparseable external results can omit real spend. Arbitrary generated direct network/provider code is not compelled to call the supplied helper. External contract: truthful/recoverable usage and pricing plus provider/SDK stop semantics (SRC-1, `meta_n/core/llm_client.py`, `meta_n/core/external_agents/budget.py`, `meta_n/core/external_agents/solver.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> Because tasks run concurrently under ``Semaphore(parallel)`` and spend is only
> recorded at run end, up to ``parallel`` in-flight runs admitted against the same
> pre-record total can still overshoot the cap by at most that many runs; there is
> no in-run USD kill to clip an individual over-spending run. This is the honest,
> documented bound — not a hard per-run stop.
> --- `meta_n/core/external_agents/budget.py`

The documented number-of-in-flight-runs bound is not a fixed dollar bound. Failed metric recovery additionally limits the ledger to proven spend; source documentation is not newly observed cost behavior.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Preprocessing and helper advertisement authority

Consumer: native solver or external SDK model. Channel: additional-context text, system suffix or instruction prefix and helper signature/docstring descriptions. Force: model-interpreted guidance, including foster-adoption requests; delivery is not mandatory compliance. Horizon: current solve, repeated trials and later rounds/resume through retained chain reuse. Ω also consumes retained rationale/prior injections to propose successors. Consumer-visible filtering differs from the live full chain: Ω sampling drops selected traces/old layers but does not delete them from solver organization (SRC-1, `meta_n/core/omega.py`, `meta_n/utils/context_manager.py`, `meta_n/core/solver.py`, `meta_n/core/external_agents/injection.py`).

> while len(result) > 1 and total > budget:
>     victim = result.pop(0)
>     dropped.append(victim)
>     total -= self._estimate_injected_code_tokens(victim)
> --- `meta_n/utils/context_manager.py`

This is working-context control by a code rule, not criticism or removal of obsolete capability. Ω retains at least the newest layer even when oversized; estimates and section budgets are not a proof that the complete rendered request fits the provider window. Full-chain execution can include material invisible to its next improvement proposal.

#### RT-BAP-executable-injection
Label: Helper and frozen-source authority

Consumer: selected executor or SDK workspace interpreter/tool. Channel: native prepended Python/bash, staged external helper files, deterministic deployment wrapper or native frozen-script map. Force: executable source determines effects when invoked; staging/advertising alone does not prove invocation. Horizon: evaluated candidate trials, subsequent solves and persisted/resumed chains. Source-native admission and capability changes are in [RT-RTE-chain-admission](#rt-rte-chain-admission), [RT-RTE-helper-verification](#rt-rte-helper-verification) and [RT-RTE-frozen-routing](#rt-rte-frozen-routing), with path-specific isolation limits (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/code_library.py`, `meta_n/core/external_agents/injection.py`).

> for name, source in safe_py.items():
>     staged[f"helpers/{name}.py"] = source
> --- `meta_n/core/external_agents/injection.py`

## Annotations

none
