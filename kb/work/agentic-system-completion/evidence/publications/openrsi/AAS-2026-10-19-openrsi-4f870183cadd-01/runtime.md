---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenRSI runtime baseline: Gym task construction, Evo program search and ERL training handoffs at the frozen release."
run-id: AAS-2026-10-19-openrsi-4f870183cadd-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI runtime report

## Runtime account

### What runs, and what is not established

OpenRSI ships an improvement plane rather than one continuously self-modifying agent. Gym constructs executable task packages; Evo searches over candidate programs using model operators and execution feedback; ERL provides supervised and reinforcement-learning paths for the operators. The boundary remains **complete artifact, partial loop**, as supplied in [boundary](boundary.md). All source evidence below is SRC-1 at the frozen commit. Executable passages supply implementation evidence; README passages supply intent or attributed reports. No target execution, provider call, training run or experiment was performed. Wiring is not observed activation, trustworthy scoring, measured benefit or a historical lineage from trained checkpoint to deployed operator.

The release's bounded claim is retained as [RT-CLM-meta-evolution](#rt-clm-meta-evolution). Its reported asynchronous training validation is [RT-CLM-training-validation](#rt-clm-training-validation), not an observed run in this analysis. The runtime changes external candidate programs and can train operator weights; those are different change targets and different admission mechanisms. No evidence here closes the exercised self-improvement chain from objective evidence through changed operator weights to subsequent behavior causally dependent on those changes.

### Entry paths and one ordinary invocation

An ordinary Evo MLE invocation starts in `OpenMLE-Evo/scripts/evaluate_airaevo.py`. The configured input data, sandbox resource/URL, first configured model, generation kwargs, budgets and solver options become prepare/runner YAML files. The driver launches the shipped task builder and runner with `check=True`. The runner starts one `single_task_runner.py` process per task/sample under concurrency coordination. The child constructs `SandboxMLEBenchTask`, obtains task information, constructs `Evolutionary`, and calls `load_checkpoint()` before search. Thus the shipped driver and checkpoint reader are inside this runtime, not external application responsibilities (SRC-1, `OpenMLE-Evo/scripts/evaluate_airaevo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`).

The ordinary generation loop is [RT-RTE-evo-generation](#rt-rte-evo-generation): code chooses draft/improve/crossover, a model proposes plan/code, task execution returns output and fitness, code marks validity/bugginess, debug may propose repairs, and population policy admits successors. The journal is checkpointed and final candidate code is exported. Task/sample identity, node/parent identity and checkpoint state are distinct. A model does not own the outer loop or directly decide every admission.

The task adapter sends candidate source, data directory, resource class, evaluation split, priority and timeouts to a configured sandbox. It selects a CPU/GPU API key, uses an HTTP client with TLS verification enabled by default, and returns job identity, logs, scores and timings. Both synchronous and asynchronous `step_task` emit the selected fitness and validity payload. A remote response is therefore an external execution contract, not direct local proof that a valid ML experiment occurred (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`). The shipped sandbox dispatcher supports shell and legacy Jupyter paths, cancellation checks, deadlines, submission-file checks, and a separate evaluation command reading `data/private/test_answer.csv` and `utils/metric.py`. The worker's metric reader imports the task metric module. That is an executable task-supplied oracle, not an independent universal correctness oracle (SRC-1, `OpenMLE-Gym/openmle-sandbox/node_controller/task_dispatcher/task_dispatcher.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`).

After search, the per-task runner reselects the best available node, writes `valid_code_final.py` and `submit_code.py`, and conditionally requests test-phase evaluation. An important forcing case is [RT-RTE-final-submit](#rt-rte-final-submit): false `final_submit_enabled` yields the empty range `range(1, 1)`, so the runner does not call test evaluation. This excludes final test calls on this runner path, not earlier search evaluations or direct adapter calls.

Other shipped entry paths remain distinct:

- `openmle-task build` defaults to dry-run; `--execute` enables task construction. Its graph downloads, copies, scrapes, perceives through tools, describes, generates/executes preparation code, generates a metric and returns a task result: [RT-RTE-gym-build](#rt-rte-gym-build). `prepare-input`, `overview`, `metric-check`, `evaluate` and `leaderboard` are additional CLI surfaces, not all covered by the build dry-run gate (SRC-1, `OpenMLE-Gym/openmle_gym/cli.py`).
- Evo's asynchronous steady-state search changes scheduling and commit semantics, not just throughput: [RT-RTE-evo-async](#rt-rte-evo-async).
- NatureBench replaces the MLE sandbox adapter with workspace-based local/Docker/SCM execution and an evaluation service: [RT-RTE-naturebench-execution](#rt-rte-naturebench-execution).
- SFT rollout/data selection/training and RL sync/async launchers are operator-training paths, not on-by-default stages of every Evo invocation: [RT-RTE-sft-training](#rt-rte-sft-training), [RT-RTE-rl-training](#rt-rte-rl-training).

### Selected guarantees and challenges

Three forcing investigations were selected because they change what later analysts can safely infer.

1. **Isolation is option- and route-specific.** Gym's `isolated` generated-code branch requests a networkless, read-only, non-root container with explicit writable mounts, dropped capabilities and resource limits. The build coordinator itself always uses process mode; the option is passed inward to preparation. The default preparation branch imports and calls generated Python in that child process. Metric generation only compiles and writes source; later metric-check executes it. Owner: Gym process runner and caller. Enforcement point: `_container_command`, only when selected. Guarantee strength: deployment guarantee, conditional on a suitable image/runtime/kernel and the exact mounts. Covered path: selected isolated prepare/metric workers. Alternate paths: default process mode, direct local preparation/module loading, and independent Evo remote execution. implementation conclusion status: wired. operation conclusion status: uninspected. Neither a deployment nor blanket confinement is established (SRC-1, `OpenMLE-Gym/openmle_gym/process_runner.py`, `OpenMLE-Gym/openmle_gym/build.py`, `OpenMLE-Gym/builder_core/utils/nodes.py`, `OpenMLE-Gym/openmle_gym/metric_validation.py`).
2. **Execution-grounded selection is not always deterministic evaluator-only selection.** Both MLE step variants forward selected fitness to `parse_eval_result`. With experience disabled, the analyzer model is called for every node, then finite validation fitness overrides it. With experience enabled, finite fitness bypasses the analyzer; deterministic failure gets a failure response; otherwise analysis falls back to the model. `use_test_score` can then replace the metric with auxiliary `score`. The self-valid task protocol can optionally trust the model's printed validation score. Owner: task adapter plus evolutionary parser. Enforcement point: protocol score annotation, fitness emission, then parser. Guarantee strength: policy. Required external contract: trustworthy sandbox status/metric and correct task data/metric implementation. implementation conclusion status: wired. operation conclusion status: uninspected. A claim that every selection is a trusted independent holdout result would be false for supported configured paths (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`).
3. **Final-submit false suppresses the runner's final test loop, not all evaluation.** The option producer, runner's false branch, loop bounds and both task consumers were inspected. The false loop is empty because Python's upper bound is exclusive. NatureBench's explicit final-submit configuration can reach this branch. The adapters themselves accept test requests without receiving the flag, so the control belongs to the runner rather than the executor API. No supported alternate caller bypass of the runner's decision is demonstrated here. Owner: per-task runner. Enforcement point: loop bound. Guarantee strength: invariant within this runner branch; external contract: ordinary Python range semantics. implementation conclusion status: wired. operation conclusion status: uninspected. See [RT-RTE-final-submit](#rt-rte-final-submit).

Capability surface, actual grants and deployed isolation must remain separate. Gym binds four perception tools, but generated Python is a wider execution surface. The actual process inherits the host environment; isolated prepare/metric containers do not forward the credential allowlist. Evo MLE workers are granted remote API credentials and a task directory; NatureBench can run local Python, Docker or SSH-mediated Docker. The sandbox startup script uses `seccomp=unconfined`, read-only dataset mounting plus several writable shared mounts, and CPU/memory limits. Those flags differ from Gym's isolated runner and do not establish a deployed isolation envelope. No target run or deployment configuration was supplied (SRC-1, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/openmle_gym/process_runner.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/sandbox_builder/start_sandboxes.sh`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`).

### Coverage added and remaining limits

Beyond the boundary's initial reads, this member inspected Gym graph/nodes/model adapter/build process runner and CLI; Evo generic model dispatch, LiteLLM configuration, improve operator, generation and asynchronous search, scoring, final-submission producer/consumer branches, MLE and selected NatureBench execution paths; sandbox dispatcher execution/evaluation sections and worker container flags; SFT generation-loop control, composable data pipeline, evolutionary selection and message finalization, training launcher and vendored SFT rollout consumer; RL sync/async patch wrappers, generation/reward/admission sections, and async launcher hooks. These are additional SRC-1 implementation coverage, not new sources.

Not established: full Gym metadata/quality-evaluation semantics, complete NatureBench evaluator/preflight/security behavior, every sandbox router/controller recovery path, every SFT parallel/evolutionary collection and selection variant, all RL reward-shaping combinations, async queue staleness/weight synchronization correctness, and optimizer internals of the external RL SLIME checkout. Those are available-but-uninspected mechanisms or external limits, not evidenced absences. Memory revision and detailed experience-store inventories belong to the memory analyst; the runtime records only the handoffs needed to explain execution. Exact provider weights, initial training lineage and deployment artifacts remain unavailable under the frozen boundary. No performance or security certification follows from this account.

## Shared records

### Components

#### RT-CMP-openai-llm-provider
Label: Gym OpenAILLMProvider

Source-native identity: `OpenAILLMProvider` in SRC-1, `OpenMLE-Gym/builder_core/utils/chat.py`. Distributed-parametric inference model, reached through LangChain `ChatOpenAI`; parameters reside behind a configured endpoint, not in this repository. API/base URL/model come from configuration or arguments. Parameters are not updated by this adapter during task construction; exact weights/version are not pinned here. A mutable endpoint/model alias can resolve to another model; provider internals and deployed mapping are uninspected. Natural-language messages and tool schemas are inputs, not the model's storage form.

> self.llm = ChatOpenAI(
>             model=self.model,
>             api_key=self.api_key,
>             base_url=self.base_url,
>             max_tokens=5000
>         ).bind_tools(tools or [])
> --- `OpenMLE-Gym/builder_core/utils/chat.py`

#### RT-CMP-generic-llm
Label: Evo GenericLLM operator models

Source-native identity: separate draft, improve, debug, crossover, analyze and optional rich-memory-summary clients instantiated by `setup_operators`. Distributed-parametric models behind configured API endpoints; source stores symbolic client configuration and natural-language templates, not their weights. The inspected Evo loop changes programs/journal, not these parameters. Exact versions are not immutably pinned by the client constructor; mutable endpoints can serve different weights. This is an operator family with independently configured calls, not evidence that every role uses one exact model. Provider internals are uninspected (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/generic_llm.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/backends/utils.py`).

> self.model = client_cfg.model_id
>         self.base_url = client_cfg.base_url
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/backends/lite_llm.py`

GenericLLM admits explicit-message calls as well as template-built calls. The direct-message and `no_user_message` branches still use the LLM concurrency limiter, but bypass some prompt assembly. That is a template-coverage limit, not evidence of a security bypass.

#### RT-CMP-sft-model
Label: SFT actor model

The SFT launcher selects external `MODEL_PATH` and converted `REF_LOAD_PATH`, distributed-parametric checkpoints on caller-supplied storage; training outputs numerical checkpoints under `OUTPUT_DIR`. Parameters are intended to change during training, unlike Evo inference. Exact weights/digests are not supplied, so training provenance and subsequent deployment identity are unresolved. The inspected SFT rollout consumes local tokenizer/model assets with `trust_remote_code=True`; this adds caller-selected model code to the execution boundary. No mutable serving endpoint is required by that rollout consumer; a later inference endpoint's mapping is uninspected (SRC-1, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`).

> --loss-type sft_loss
>   --loss-mask-type "${LOSS_MASK_TYPE}"
>   --calculate-per-token-loss
>   --disable-compute-advantages-and-returns
>   --debug-train-only
> --- `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`

#### RT-CMP-rl-model
Label: RL actor and SGLang rollout model

The RL integration uses distributed-parametric actor/rollout models supplied by an external training environment. Parameters are intended to change during optimizer training; the release reports synchronization to SGLang, but that synchronization is not an observed run here. Generation targets the configured SGLang router rather than a frozen checkpoint hash. Exact initial/deployed weights are unpinned in this evidence, and a mutable router can resolve to changed serving state. Actor/serving correspondence and provider internals are uninspected; the external RL SLIME optimizer is outside SRC-1 (SRC-1, `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh`, `OpenMLE-ERL/RL/README.md`).

> state = GenerateState(args)
>     url = f"http://{args.sglang_router_ip}:{args.sglang_router_port}/generate"
> --- `OpenMLE-ERL/RL/generate_mle.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-gym-build
Label: Gym task construction and generated-code admission

Endpoints/progression: CLI `build` → `build_tasks` → one bounded child process per slug → compiled LangGraph → task package and result. Caller supplies slug list, output root, credentials/model configuration and execution option. Code owns download/copy/scrape routing, perception tool continuation and retry decisions; the model supplies descriptions and preparation/metric source. The graph's tool node exposes directory listing, CSV summary, text reading and save. These calls do not bound what subsequently generated Python can do (SRC-1, `OpenMLE-Gym/openmle_gym/cli.py`, `OpenMLE-Gym/openmle_gym/build.py`, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/builder_core/utils/nodes.py`).

Admission: `--execute` starts the workflow, not per-content approval. Preparation source is extracted, compiled, atomically written, then run. Failure decrements retries and supplies recent failure/code context to another model invocation. Metric source is compiled and written, without an execution-based semantic correctness gate in `Metric`. File-validation and phase flags decide build success. Code can reject failed construction; no per-generated-file human veto is wired in these methods. Recovery is bounded retries and failure reporting, not transactional rollback of all filesystem effects. Guidance is the shipped sample scripts, generated description, task information and recent preparation feedback. Code, package files and preparation trace persist. Natural-language guidance and symbolic Python have distinct consumers.

- Immediate return: task_result plus batch success/failure summary and captured child stdout/stderr.
- Later read-back: recent preparation feedback/code is resupplied on retry; task package files are intended inputs to later evaluation/input preparation. Full memory lifecycle is left to the memory analyst.
- Delegated visibility: perception tools receive their named arguments; generated preparation receives raw/public/private paths; isolated mode mounts only selected paths, while process mode has host-process access.
- Selection predicate: valid/unique task names, configured MLE-Bench skip and limit; phase routers inspect task flags and retry count.
- Invalidation or expiry: retry exhaustion ends construction; failed preparation recreates selected output directories; successful delete_raw requires nonempty fileinfo before deleting raw data.
- Activation or effect: implementation writes Python and package data and calls preparation; actual writes, model compliance and package quality are unobserved.
- Evidence limits: no built task or construction run supplied; compile success and expected-file presence do not certify metric correctness or isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: bounded task-construction workflow. Answer oracle: preparation file checks and phase flags, not a reference solution proving the generated task faithful. Model proposes; software admits; caller can choose options or stop the run, but individual human approval is not established. Context control: preparation explicitly selects only the last two `prepares` messages between system and current request; earlier trace remains in state/file rather than automatically in that model call. This resembles a selected call frame, not a pointer-following memory heap.

> response = self.llm_provider.query(
>                 [query[0]] + self.todo["prepares"][-2:] + [query[1]]
>             )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

> compile(metric_code, str(metric_file), "exec")
>             atomic_write_text(metric_file, metric_code)
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

The option reaches a concrete consumer: `build_tasks` forwards execution mode through `_run_all` to graph/node construction. `_run_all` itself uses process mode. `prepare_single_competition` checks `code_execution_mode == "isolated"`; its else branch loads/calls the function directly. The isolated command requests `--network none`, read-only root, non-root UID/GID, dropped capabilities and explicit mounts. Default process mode instead copies `os.environ` (SRC-1, `OpenMLE-Gym/openmle_gym/process_runner.py`).

> else:
>                 prepare_func = self.get_prepare_function(comp_id)
>                 if prepare_func is None:
>                     raise ValueError("No prepare function found, code inexecutable")
>                 prepare_func(
>                     self.structure.raw_dir(comp_id),
>                     self.structure.public_dir(comp_id),
>                     self.structure.private_dir(comp_id)
>                 )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

#### RT-RTE-evo-generation
Label: Evo generation-mode program search

Endpoints: driver task/sample process → evolutionary operators → MLE execution adapter → evaluator → parser → journal/population → selected code. Code owns the next-step policy: initial drafts, then temperature/fitness-conditioned parent/operator selection, optional fresh drafts, crossover and migration; buggy nodes enter bounded debug cycles. Models propose program text and analyzer summaries. Representational forms are symbolic executable code/config/fitness and natural-language task, plans, feedback and prompts. State includes task budget, solver generation/step, node parentage, islands and journal (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`).

- Immediate return: solver returns task state, best node code and node; runner writes final artifacts.
- Later read-back: journal checkpoint reloads on task resume; improve/debug/crossover receive selected earlier programs and feedback. Memory revisions and summary maintenance are not assessed here.
- Delegated visibility: each operator receives assembled role-specific prompt values, not the whole host process state; remote execution receives candidate code and configured data path/resource/split.
- Selection predicate: generation/temperature/operator policy selects parents; parsing marks buggy nodes; population methods and journal best-node selection use metric direction and configured policy.
- Invalidation or expiry: debug/step/generation/time limits terminate work; failed individuals may be discarded; resume restores journal and reconciles step count with its length.
- Activation or effect: candidate source reaches `task.step_task`; parsed results determine debug and population branches in implementation. No actual search activation or improvement is observed.
- Evidence limits: external execution/metric trust, finite-fitness interpretation, model compliance, complete population policy and empirical benefit are not established by source wiring alone.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: generated code is an external work product, not an automatic replacement of runtime machinery. The source extractor retries malformed outputs but after exhaustion returns text without a guarantee of valid code. Execution and parser validity/metric checks then gate success. Checkpoints retain journal/state; no guarantee of atomic multi-file checkpoint transactions is established. Proposal guidance includes shipped operator templates, task/data descriptions, selected previous code/output, packages and remaining budget. Program and result records persist; detailed experience-memory revision belongs elsewhere. No per-candidate human decision appears in this inspected loop. Answer oracle is the configured task evaluator where fitness exists, with the analyzer/model-score alternatives below. Operating mode: bounded benchmark search with multiple scoring protocols.

> state, eval_result = task.step_task(state, extract_code(child_node.code))
>                 self.parse_eval_result(child_node, eval_result)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> # Fall back to the legacy analyze operator only when sandbox metadata
>             # cannot deterministically provide a metric or failure state.
>             response = run_legacy_analyze()
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

Scoring challenge: the parser consumes finite `VALIDATION_FITNESS`; with experience off it first invokes analysis, while experience on can avoid analysis. Missing metadata can reach model analysis. The task's self-valid protocol uses printed validation score only when `trust_model_validation_score` is true, otherwise sandbox scores. Both sync and async step methods forward selected fitness; `use_test_score` is another downstream substitution. These branches disprove universal evaluator-only scoring, but do not establish any observed cheating or score error (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`).

> if self.cfg.use_test_score:
>             test_score = aux_eval_info.get("score", None)
>             aux_eval_info["validation_score"] = response["metric"]
>             response["metric"] = test_score
>             self.logger.info(f"Using Test score: {test_score}")
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

#### RT-RTE-evo-async
Label: Evo asynchronous steady-state alternate

Same search objective and operators as [RT-RTE-evo-generation](#rt-rte-evo-generation), but distinct orchestration: `search` dispatches to `search_async_steady_state`; worker specs assign sandbox URLs; sampling and committing use separate locks. Each work item captures attempt/generation, operator, parents and worker identity. Generation is derived from attempt count, not a barrier over a completed generation. Commit adds an evaluated node under lock, optionally admits it to islands and checkpoints at configured commit intervals (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`).

- Immediate return: after gathering/cancelling workers and saving a final checkpoint, state and best code return.
- Later read-back: shared journal persists and restores the candidate population; selected parent nodes feed later worker invocations.
- Delegated visibility: each worker gets its work item's selected parent list, copied task state, and assigned sandbox URL; adapter fallback can use `to_thread(task.step_task, ...)` when no async method exists.
- Selection predicate: fresh draft if population is empty or parent selection raises RuntimeError; crossover is disabled without enough parents; successful nonbuggy commits may enter population.
- Invalidation or expiry: stop checks, attempt/time/step limits, worker retry exhaustion and cancellation end work; commit can reject completed work after a stop condition.
- Activation or effect: source wires concurrent proposal/evaluation and serial commit; no observed scheduling, race-freedom or speedup is claimed.
- Evidence limits: does not establish strict budgets for all in-flight external work, crash-atomic checkpoints, or equivalent ordering/results to generation mode.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision owner: software sampling/commit policy; model proposes code; no per-commit human veto appears. Operating mode: bounded steady-state search. Oracle and admission content match the selected task adapter/parser, not an additional independent evaluator. Guidance/persisted material match the operator inputs and journal above. Retry uses bounded exponential backoff; finally cancels pending tasks and checkpoints, not a proven rollback of remote effects.

> if hasattr(task, "step_task_async"):
>             return await task.step_task_async(
>                 dict(state),
>                 code,
>                 sandbox_base_url=sandbox_url,
>             )
>         return await asyncio.to_thread(task.step_task, dict(state), code)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

#### RT-RTE-naturebench-execution
Label: NatureBench local, Docker and SCM execution

Endpoints: shared Evo solver → dynamically loaded NatureBench task class → per-attempt workspace/run.py → selected executor → evaluation service → aggregate score/feedback. The caller selects execution mode and deployment paths; code creates attempts, runs preflight, executes and evaluates. Candidate source is symbolic Python; service feedback/task guidance is natural language plus symbolic status/score. Mode dispatch supports local process, remote SCM Docker, and default Docker. It is not the MLE HTTP sandbox path (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`).

- Immediate return: status, aggregate-derived selection score, logs, attempt index, workspace and timing enter the shared solver result schema.
- Later read-back: candidate/feedback can enter the shared journal and subsequent operator prompts; per-attempt workspaces remain filesystem artifacts, with full cleanup policy uninspected.
- Delegated visibility: candidate gets task problem data and output workspace; Docker mounts problem read-only and workspace writable, and receives an evaluation-service URL. SCM supplies remote workspace and deployment configuration.
- Selection predicate: configured benchmark chooses this task adapter; preflight success enables execution and service evaluation, otherwise an explicit failure payload returns.
- Invalidation or expiry: execution timeouts and solver limits apply; local/Docker/SSH recovery internals were only partly inspected, so complete cancellation guarantees are uninspected.
- Activation or effect: Python is executed locally or via Docker/remote Docker and the service response is annotated for selection; no run or deployment is observed.
- Evidence limits: external service truth, task data provenance, full preflight policy and remote isolation remain unestablished; local mode is a supported alternate, not evidence of Docker confinement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Software decides executor/admission; model supplies candidate; human contributes deployment/configuration rather than demonstrated per-candidate approval. Operating mode: bounded benchmark experimentation. Answer oracle: external NatureBench evaluation service, not model judgment alone; its complete implementation and ground truth are uninspected here. Proposal guidance is task/public prompts, data analysis and task-family guidance forwarded into solver context. Admission means entering search results/population, not changing the evaluation service. Rollback is no stronger than separate attempt workspace and executor timeout/recovery wiring.

> if self.execution_mode == "local":
>             return self._run_local_solution(
>                 code, workspace=workspace, output_dir=output_dir
>             )
>         if self._uses_scm():
>             return self._run_scm_docker_solution(code, attempt=attempt)
> --- `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`

#### RT-RTE-final-submit
Label: Final submission option and conditional test call

Producer/consumer chain: `_should_run_final_submit` returns false for nonpositive repeats; for NatureBench it also consumes the nested runner/task final-submit setting. The main runner assigns the resulting Boolean, writes skip messages when false, and executes zero test-phase iterations when false. Both MLE and NatureBench `evaluate_code` implementations perform evaluation without receiving that Boolean, so exclusion is enforced at the runner, not the adapter API. NatureBench's configurable false setting is a supported reachable input. MLE's constructor converts zero repeats to one, so the helper's nonpositive-repeat branch alone is not proof that MLE zero disables submission (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`).

- Immediate return: skip logs and eventual task statistics when false; submit results/logs from enabled attempts otherwise.
- Later read-back: uninspected — exported statistics may be consumed later, but no retained-memory conclusion is required for this option-control finding.
- Delegated visibility: when called, task adapter receives best_code and phase=test, not final_submit_enabled.
- Selection predicate: best available node selection precedes export; final_submit_enabled determines whether the final test loop is entered as well as repetition and output interpretation.
- Invalidation or expiry: configured repeat count and executor deadlines bound enabled attempts; false yields an empty range.
- Activation or effect: runner wiring suppresses final test calls when false but still exports code; no execution trace is supplied.
- Evidence limits: exact returned scores and runtime cost are unobserved; adapter APIs do not enforce this runner option, and earlier search evaluation is unaffected. No supported alternate caller bypass is demonstrated.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: code selects a best available candidate and schedules test calls; models supplied candidates earlier; no new human approval is requested here. Operating mode/oracle: post-search benchmark test using the selected adapter's evaluator, not another improvement proposal. No organization change is admitted by this route.

> for attempt_index in range(
>             1,
>             (int(task.submit_repeats) + 1) if final_submit_enabled else 1,
>         ):
>             submit_result = task.evaluate_code(best_code, phase="test")
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

#### RT-RTE-sft-training
Label: SFT trajectory selection and supervised operator training

Endpoints: generated/scored rollout artifacts → separately invoked selectors/finalizers → caller-chosen training dataset → launcher → vendored SLIME SFT rollout/loss → output checkpoints. This is a multi-entry pipeline, not proof that every training dataset passed every selector. The composable data producer calls collection with accept_scored/feedback success, token length, relative gap and per-task top-k filtering. Evolutionary selection separately reconstructs root/debug-descendant segments and compares endpoint scores with parent scores; finalization deduplicates normalized messages and filters full-message token length. The launcher accepts an arbitrary caller-supplied JSONL/Parquet path, not a signed selection artifact (SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`, `OpenMLE-ERL/SFT/scripts/sft_data_selection/select_evolutionary.py`, `OpenMLE-ERL/SFT/scripts/sft_data_selection/finalize_messages.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`).

- Immediate return: selection scripts write datasets/reports; training targets checkpoint output rather than answering the original ML task.
- Later read-back: vendored SFT rollout reads message samples from data_buffer; numerical checkpoints are intended later model assets, but a specific trained checkpoint reaching an Evo endpoint is not traced.
- Delegated visibility: each training sample supplies messages and optional tools to the loss-mask generator; actor training receives token IDs, response lengths and masks, not all raw rollout files.
- Selection predicate: path-specific gates above; launcher requires dataset/model/checkpoint paths, minimum row count and intentional existing-output override; it does not enforce those prior semantic selection gates.
- Invalidation or expiry: dataset regeneration/finalization is explicit; output-directory guard prevents accidental reuse unless overridden. Exact optimizer restart fidelity is uninspected; launcher omits optimizer/RNG saves.
- Activation or effect: SFT consumer tokenizes retained conversations and computes loss masks; launcher selects sft_loss and training-only mode. Actual weight updates and improved operator capacity are unobserved.
- Evidence limits: exact final corpus/model weights are not bundled; selected code ranges establish separate gates and consumer wiring, not full historical corpus lineage or all rollout variants.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller selects data/model/output and initiates training; software filters candidates, while the optional evolutionary causal-inheritance machinery is not fully assessed here. Starting training does not prove human editing/approval of every example. Proposed change is operator parameters. Training objective/loss and selected demonstrations guide it; checkpoints persist. Software can reject missing/oversized/unqualified data in the corresponding selection path; final deployment approval, rollback and endpoint replacement are uninspected. Operating mode: bounded offline supervised curriculum. Answer oracle: upstream execution scores/reference outcomes where selection uses them; SFT rollout itself sets reward to zero and trains from stored messages, not fresh execution.

> token_ids, loss_mask = MASK_GENERATOR.get_loss_mask(messages, tools=tools)
> --- `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`

> sample.tokens = token_ids
>         sample.response_length = response_length
>         sample.reward = 0
>         sample.loss_mask = loss_mask[-response_length:]
> --- `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`

Working-context control: batch generation can stop when accepted-target or max-generated is reached; the controller changes generation count, not a model's existing context. Token filtering can reject an entire example rather than compress its reasoning. These are distinct from automatic conversational summarization (SRC-1, `OpenMLE-ERL/SFT/tts_search/services/generation_loop.py`, `OpenMLE-ERL/SFT/scripts/sft_data_selection/finalize_messages.py`).

#### RT-RTE-rl-training
Label: RL generation, reward, program admission and training handoff

Endpoints: sync/async launcher → patch wrapper → external SLIME train/train_async → custom generate/reward hooks → SGLang and sandbox → reward/sample metadata and ProgramDatabase → training environment. The async launcher names `fully_async_rollout.generate_rollout_fully_async`, `generate_mle.generate` and `generate_mle.reward_func`. Both wrappers pin local import roots and execute the expected train file; patch import failures warn and continue. Async refuses fallback to `/root/slime`. These wrappers are production-machinery changes installed at startup, not a model rewriting the trainer (SRC-1, `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh`, `OpenMLE-ERL/RL/train_with_patch.py`, `OpenMLE-ERL/RL/train_async_with_patch.py`).

Generation validates message input shape, chooses/caches parents and mode, sends prompt tokens to SGLang, and records response tokens/logprobs/loss mask. Reward extracts code, optionally requires validation-score-print syntax, calls a model-based hack checker, and sends eligible candidates to direct/proxy sandbox execution. It computes configured score mappings, parent-relative shaping and metadata; categorized invalid programs can persist for analysis. Abort handling can provide empty response/sentinel reward to unblock group coordination rather than silently dropping the sample (SRC-1, `OpenMLE-ERL/RL/generate_mle.py`).

- Immediate return: generation returns a populated Sample; reward hook returns final_reward for training, with scores/status/reward views in metadata.
- Later read-back: stored programs are available to later generation parent selection; checkpoint consumption/weight synchronization depends on the external RL training environment and is not traced to a later Evo deployment.
- Delegated visibility: SGLang receives constructed prompt/token data; sandbox receives extracted candidate code and task context; hack checker receives candidate content. No per-sample human approval is established.
- Selection predicate: code category and optional self-validation policy gate sandbox eligibility; insertion occurs for HTTP 200 or hack/no_verify/hack_verify categories, not only positive-scoring successful programs.
- Invalidation or expiry: abort/retry sentinels, configured sandbox timeout caps, cache/group coordination and database snapshots support recovery; exact async staleness/eviction and external trainer restart semantics remain uninspected.
- Activation or effect: source wires execution feedback into reward and ProgramDatabase admission; optimizer/serving updates are integration intent plus author-reported operation, not independently observed here.
- Evidence limits: external RL SLIME is unregistered/uninspected; judge errors, complete reward combinations, numerical optimizer behavior and reliable improvement are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: models propose candidate code and judge suspected hacking; code owns category routing, reward arithmetic and insertion; caller supplies deployment/training inputs and launch decisions. Operating modes include training and evaluation, with evaluation documented in generate as forcing draft mode; complete evaluation selection semantics are not asserted. Answer oracle: sandbox execution/task scoring where used; a judge classification is not an expected-answer oracle. Guidance includes operator/task prompts, parent code/results and configured reward objective. Proposed changes are candidate programs and ultimately operator parameters; database admission and optimizer update are separate gates. Explicit invalid categories can be retained without being approved as successful work. Training rollback/deployment substitution remain external/uninspected.

> should_store_program = status_code == 200 or code_category in {"hack", "no_verify", "hack_verify"}
>     if should_store_program:
>         program_id = db.add(program)
> --- `OpenMLE-ERL/RL/generate_mle.py`

> except Exception as e:
>     print(f"[TRAIN_ASYNC_WITH_PATCH] Warning: Failed to load rollout patch: {e}")
>     import traceback
> 
>     traceback.print_exc()
> --- `OpenMLE-ERL/RL/train_async_with_patch.py`

Guarantee owner: wrapper/import and hook code. Enforcement points: local trainer-file existence and explicit async fallback refusal are hard path checks; successful patch installation is not guaranteed because failure is nonfatal. Guarantee strength: best effort for patch application. Required external contract: compatible pinned SLIME, SGLang, model and sandbox deployments. implementation conclusion status: wired. operation conclusion status: uninspected.

### Claims

#### RT-CLM-meta-evolution
Label: Bounded Meta-Evolution claim

Claimed operation: train the improver in bounded executable domains, not a demonstrated solution to general recursive self-improvement. Source: SRC-1, `README.md`, doctrine/design. Routes above establish architecture/integration, not general self-improvement or empirical success.

> OpenRSI begins with Meta-Evolution—training the improver itself in bounded, executable domains—without claiming that general recursive self-improvement has been solved.
> --- `README.md`

#### RT-CLM-training-validation
Label: Author-reported async RL validation

Claimed operation: a single-node asynchronous profile restored checkpoints, completed two optimizer steps, synchronized serving weights and evaluated on eight H200 GPUs. Source: SRC-1, `OpenMLE-ERL/RL/README.md`, reported operation only. No inspected trace or independently registered run supports upgrading this claim to observed behavior in this analysis.

> The released single-node asynchronous profile completed real checkpoint restore, two rollout-and-optimizer steps, post-step weight synchronization to SGLang, and evaluation on eight H200 GPUs. This validates the released path end to end; it is not a claim of exact paper reproduction.
> --- `OpenMLE-ERL/RL/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-candidate-execution
Label: Generated program becomes executable action

Consumer: Gym preparation loader/worker, Evo task executor, or NatureBench executor. Channel: generated source written/imported or passed as task action. Force: symbolic Python execution after path-specific compile/preflight/execution checks; natural-language prompts only shape the proposal and do not constrain Python's complete capability surface. Horizon: current preparation attempt or candidate evaluation, with selected source reusable through journal/package outputs. This path is wired, not observed, and does not imply runtime self-modification (SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`).

> run_path = workspace / "run.py"
>         run_path.write_text(code, encoding="utf-8")
> --- `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py:846-912`

#### RT-BAP-training-parameters
Label: Retained demonstrations and rewards shape operator parameters

Consumer: SFT loss-mask/training path or external RL trainer. Channel: selected stored messages become supervised tokens/masks; rollout reward and logprobs become RL training inputs. Force: intended numerical parameter update, distinct from model interpretation of parent/experience text. Horizon: checkpoint lifetime and later inference only if a resulting model is actually installed/served. SFT input wiring and RL integration are inspected; an exact produced checkpoint's subsequent behavioral effects are not. No self-improvement success is attributed from storage or loading alone (SRC-1, `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/RL/generate_mle.py`).

> sample.metadata["base_reward"] = shaped_base_reward
>         sample.metadata["final_reward"] = final_reward
> --- `OpenMLE-ERL/RL/generate_mle.py:1800-1860`

The route accounts distinguish programs, retained input/outcome records and parameters from formulated explanatory theories. Plans, analyzer summaries and feedback are delivered, but this member does not infer content-directed theoretical criticism, reliable learning, reflective theory building or autonomy from their labels, scores or persistence. Those independent properties require separate content and operation evidence; no theory-builder conclusion is declared here.

## Annotations

none
