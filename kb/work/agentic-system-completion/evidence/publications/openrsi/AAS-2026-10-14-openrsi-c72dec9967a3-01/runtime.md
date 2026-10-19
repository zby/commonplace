---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenRSI runtime baseline: task construction, operator training and executable search at the frozen OpenMLE release."
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI runtime report

## Runtime account

### What runs, and what does not follow from the release

OpenRSI ships an improvement plane, not one autonomous process that repeatedly rebuilds and deploys itself. Its consequential work is to build executable MLE tasks, produce and select program-generation experience, train program-evolution operators, and compose those operators into evaluated program search. The independently runnable stages and their external dependencies are fixed by [boundary](boundary.md). The source's broader training-to-search ambition is recorded separately in [RT-CLM-meta-evolution](#rt-clm-meta-evolution). This report establishes implementation wiring, not successful execution, activation of any particular experience, or causal gains.

The ordinary invocation traced here is the shipped MLE-Bench adapter: `OpenMLE-Evo/scripts/evaluate_airaevo.py` writes preparation and runner YAML, runs `examples/mle_bench/build_tasks.py`, and runs `examples/mle_bench/runner.py`. The runner creates a separate subprocess for each task/sample, with task-level concurrency control. `single_task_runner.py` constructs a task, operator configurations and the evolutionary solver, reloads its checkpoint, and runs search. The concrete paths in this paragraph are under `OpenMLE-Evo/third_party/aira-evo/` unless already fully qualified. SRC-1, `OpenMLE-Evo/scripts/evaluate_airaevo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`.

In that invocation, the configuration supplies model and sandbox endpoints, task packages, score direction and budgets. It does not supply each next program. Code chooses an operator and parents; a model proposes Python; the task dispatches that Python for execution; evaluation feedback becomes a node metric and informs later selection. Search ends with selected code and retained statistics, not an automatically deployed new operator model. The route and its decision roles are [RT-RTE-evolution-search](#rt-rte-evolution-search); the executor and score contract are [RT-RTE-sandbox-evaluation](#rt-rte-sandbox-evaluation). The model clients are [RT-CMP-generic-llm](#rt-cmp-generic-llm).

### Ordinary search, coordination and return

The solver holds a journal of nodes and a population of solution islands. The initial generation drafts programs. Later generations sample an island, select parents and choose Improve, Draft or Crossover under configured probabilities and a temperature schedule. Each candidate is evaluated before it becomes a usable solution. Buggy nodes enter a bounded Debug cycle. Non-buggy solutions compete for island admission; the comparison is to island average fitness, not necessarily to the best program or the selected parent. Initialization and empty islands have different admission behavior. This matters: the executable predicate is weaker than the nearby source comment about improving overall island fitness. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`; [RT-RTE-evolution-search](#rt-rte-evolution-search).

Operator prompts are constructed per call. For example, Improve receives task and data descriptions, selected parent code, sanitized or unsanitized execution output according to configuration, budgets, packages and optional preview and experience memory. It does not automatically receive every past model conversation. `GenericLLM` renders system/user templates and records prompt messages, completion text and usage. This is an explicit input-selection mechanism, not a general chat-history compactor. Runtime construction of selected context is established; retained-memory transformation and revision are left to the memory analyst. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/generic_llm.py`.

The journal and solver checkpoint permit continuation. The runner separately supports skipping a task/sample when required output files and a non-null submit score exist. These are different decisions: skip-completed checks output completeness, while solver resume reloads search state. A checkpoint is not an atomic deployment transaction: state and journal are written separately, and the search code reconciles a mismatched step count with journal length. The shipped single-task runner also reconciles orphaned step directories against checkpoint progress. SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

On termination the single-task runner selects an available node and writes `valid_code_final.py` and `submit_code.py`. If enabled, final submission evaluates selected code again, potentially repeatedly. NatureBench can skip final submission and use a search-stage aggregate score; a final score is therefore not universally an independent post-search test. Source-grounded output selection and this forcing case appear in [RT-RTE-naturebench-execution](#rt-rte-naturebench-execution). SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`.

### Three forcing cases and the guarantees they limit

1. **An alternate evaluator can change what counts as fitness.** `SandboxMLEBenchTask` distinguishes legacy, self-validation, method1 and method2 protocols. In self-validation mode a configuration switch can select a model-printed validation score rather than sandbox validation. The solver can also use its analysis model when deterministic metadata cannot resolve a result, and `use_test_score` overrides the chosen metric. Thus “execution-grounded” does not mean one universal trusted answer channel. The decisive passage and responsibility split are in [RT-RTE-sandbox-evaluation](#rt-rte-sandbox-evaluation).
2. **An alternate search scheduler changes time and admission.** Async steady-state search launches work against selected workers/sandbox URLs and serializes commits. It may reject a completed evaluation after a stop condition becomes true. Generation mode checks budgets at coarser points; the shipped runner adds pre-operator guards. None of these checks preempts an in-flight model request. [RT-RTE-async-search](#rt-rte-async-search) scopes the guarantee.
3. **An alternate execution path changes isolation.** Gym can use an explicitly constrained Docker/Podman worker for generated preparation code, but its non-isolated preparation path imports and invokes that code directly. Evo's NatureBench path separately permits local Python, local Docker and remote SCM Docker. The sandbox worker launcher uses resource limits and read-only dataset mounts, but also writable shared subtrees and `seccomp=unconfined`. These are not equivalent grants. [RT-RTE-gym-build](#rt-rte-gym-build), [RT-RTE-naturebench-execution](#rt-rte-naturebench-execution) and [RT-BAP-execution-authority](#rt-bap-execution-authority) describe the actual effect boundaries.

Two load-bearing controls therefore have bounded strength:

| Control | Owner and enforcement point | Strength and coverage | Alternate path / required external contract | Status |
| --- | --- | --- | --- | --- |
| Stop issuing/committing search work at configured limits | Runner's `guard_operator_call`; async solver's stop and commit checks | policy; pre-call checks and commit-time rejection, not strict total wall-clock preemption | Bare generation solver has generation-end checks; model requests and subprocess/service shutdown require their own deadlines and working external clients | implementation conclusion status: wired; operation conclusion status: uninspected |
| Constrain generated Gym preparation code in isolated mode | `process_runner._container_command`, invoked by `NodeExecutor.prepare_single_competition` | deployment guarantee conditional on selecting isolated mode and a correctly configured container runtime/image | Direct import branch is not covered; Evo/NatureBench have separate executors and mounts; runtime, image and host permissions are external prerequisites | implementation conclusion status: wired; operation conclusion status: uninspected |

Sources for this table are SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Gym/openmle_gym/process_runner.py`, `OpenMLE-Gym/builder_core/utils/nodes.py`. Minimum passages are retained in the corresponding route records below. Neither row is a demonstrated security or availability guarantee.

The capability surface includes arbitrary generated Python and shell execution through the selected backend, dynamically imported task metrics, model calls and model-triggered Gym inspection tools. The **current grant set** depends on endpoint credentials, mounts, executable selection, resource configuration and mode. The **deployed isolation envelope** is unobserved. A finite tool list does not bound the authority of separately generated Python, and configuring an API key is not per-program human approval. SRC-1, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/builder_core/utils/chat.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`; [RT-BAP-execution-authority](#rt-bap-execution-authority).

### Admission beyond the search population

Gym admits task artifacts: description, preparation code, prepared files and a metric module. Compilation and file validation are local checks; metric-generation success alone is not proof that the metric measures the intended task. Its output later becomes executable evaluation machinery, as [RT-OBJ-metric](#rt-obj-metric) and [RT-RTE-gym-build](#rt-rte-gym-build) show.

The SFT pipeline admits selected traces into a training dataset. A separate launcher consumes that dataset under SFT loss and writes model checkpoints; the vendored train loop updates rollout weights after actor training. The RL launchers instead bind source-native generation/reward hooks to an external SLIME installation, with synchronous and fully async rollout modes. Its program database can retain explicitly invalid categories for analysis, so database membership is not equivalent to a positive training example or trusted reusable solution. These paths are [RT-RTE-sft-training](#rt-rte-sft-training) and [RT-RTE-rl-training](#rt-rte-rl-training); their mutable components are [RT-CMP-training-models](#rt-cmp-training-models). No automatic promotion from one training checkpoint into the Evo serving endpoint was established in the inspected drivers. The actual deployed model identity and historical replacement procedure remain unresolved, rather than inferred from the project's cycle diagram.

### Added coverage and remaining limits

All source-dependent statements below use SRC-1 at the boundary commit, as implementation unless explicitly called doctrine/design or reported operation. Additional inspection beyond the boundary's initial trace covered: Gym `builder_core/utils/{nodes,chat}.py`, graph, build worker dispatch and isolated container command; Evo `examples/mle_bench/{base_task,single_task_runner,runner}.py`, `examples/nature_bench/base_task.py` local/Docker/SCM dispatch and evaluation, `scripts/evaluate_airaevo.py`, searches of the NatureBench and local drivers, operator Improve, client dispatcher/GenericLLM and LiteLLM configuration, solver generation, async commit, fitness parsing and island admission; SFT selection pipeline, SFT rollout and vendored training loop; RL generation/DB admission, training wrapper, launch hook wiring and fully async rollout symbols. These are additions to inspection coverage, not new sources or observations.

The smallest forcing set was the three cases above. Not audited end to end: every provider implementation, sandbox API/router authorization and queue race, remote SCM provisioning, the upstream RL trainer, metadata-pipeline internals, every skill/prompt, or all task-quality evaluation branches. These available-but-uninspected branches prevent a universal enforcement or exhaustive mechanism claim. External task data, weights, serving/runtime deployments and historical training artifacts remain outside the evidence. No target code, tests or services were executed; no supplied observed-run or causal-experiment source is registered. Successful operation, particular memory activation and improvement benefit therefore remain unobserved.

## Shared records

### Components

#### RT-CMP-generic-llm
Label: GenericLLM operator clients

Source-native identity: the Draft, Improve, Debug, Crossover and Analyze `GenericLLM` instances, plus optional rich-memory summary client, created by `Evolutionary.setup_operators`. They are independently configurable client roles, not evidence of different weights. Representational form: distributed-parametric model behind a symbolic API client; natural-language messages are inputs, not the parameters. Storage substrate: external provider/serving memory and weight files, inaccessible in this evidence set; local configuration and usage records are ordinary Python/file data. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/generic_llm.py`.

- Parameters during inspected inference: no parameter-update operation in the inspected operator/client path; provider-side changes remain uninspected.
- Exact version pinned: not established. Client configuration names `model_id`, provider and `base_url`, rather than a weight digest.
- Mutable endpoint: yes, the configurable service URL/model name can resolve to another model without changing this checkout; actual service replacement is unobserved.
- Backends: dispatcher affords OpenAI, LiteLLM and GDM; full provider implementations are not all audited. Schema/function-call arguments passed through GenericLLM do not by themselves establish provider-native tool execution.

> self.model = client_cfg.model_id
> self.base_url = client_cfg.base_url
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/backends/lite_llm.py`

> rich_memory_summary_llm = (
>     GenericLLM(self.cfg.operators["rich_memory_summary"])
>     if prompt_memory_enabled(self.cfg)
>     and "rich_memory_summary" in self.cfg.operators
>     else None
> )
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

#### RT-CMP-openai-provider
Label: Gym OpenAILLMProvider

Source-native identity: `NodeExecutor.llm_provider` and `llm_provider_tools`; both wrap `ChatOpenAI`, the latter with the graph's tool bindings. Representational form: distributed-parametric remote generation consumed through natural-language prompts and symbolic tool-call dispatch. Storage substrate: external provider, with local environment/configuration selecting model and endpoint. Parameters do not change through the inspected Gym client; provider-internal mutation is uninspected. Exact weight version is not pinned by this path. The configurable `base_url` and model alias permit endpoint replacement. This is distinct from [RT-CMP-generic-llm](#rt-cmp-generic-llm): different client construction and Gym consumers, not an assertion of different model parameters. SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`, `OpenMLE-Gym/builder_core/utils/chat.py`.

> self.llm = ChatOpenAI(
>     model=self.model,
>     api_key=self.api_key,
>     base_url=self.base_url,
>     max_tokens=5000
> ).bind_tools(tools or [])
> --- `OpenMLE-Gym/builder_core/utils/chat.py`

#### RT-CMP-training-models
Label: Actor and rollout models

Source-native identity: actor/optional critic models and SGLang rollout engines managed by the SFT vendored SLIME train loop; the RL wrapper separately expects upstream training machinery. Representational form: distributed-parametric. Storage substrate: allocated GPU/host memory and model checkpoints; checkpoint contents are not supplied. Parameters change during training by design: actor training is followed by rollout weight updates. Initial weights come from operator-configured checkpoint paths, not the Git revision. Exact parameter versions and historical lineage are unresolved. RL generation uses a mutable SGLang router endpoint; SFT deployment into later Evo serving is not established. Do not infer upstream RL trainer internals from the SFT copy. SRC-1, `OpenMLE-ERL/SFT/slime/train.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/train_with_patch.py`.

> else:
>     ray.get(actor_model.async_train(rollout_id, rollout_data_ref))
> --- `OpenMLE-ERL/SFT/slime/train.py`

> offload_train()
> if args.offload_rollout:
>     ray.get(rollout_manager.onload_weights.remote())
> actor_model.update_weights()
> --- `OpenMLE-ERL/SFT/slime/train.py`

### Operative objects

#### RT-OBJ-metric
Label: Task metric module

Source-native identity: generated task `utils/metric.py`, distinct from the candidate solution and from training/search scores. Representational form: symbolic Python specifying executable validation/scoring; storage substrate: task-package filesystem, dynamically imported by the sandbox metric worker. Gym writes it after extracting and compiling model output. A downstream worker locates a locally defined class exposing `evaluate` and `validate_submission`. Thus a model-generated artifact can become evaluation machinery; compilation is not semantic validation. SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`.

> _, metric_code = self._clean_code_output(response.content)
> compile(metric_code, str(metric_file), "exec")
> atomic_write_text(metric_file, metric_code)
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

> spec = importlib.util.spec_from_file_location("utils.metric", metric_file_path)
> metric_module = importlib.util.module_from_spec(spec)
> assert spec.loader is not None  # 为类型检查提供保障
> spec.loader.exec_module(metric_module)
> --- `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`

### Routes

#### RT-RTE-evolution-search
Label: Evolutionary program search

Endpoints and progression: operator-supplied task/configuration → runner/task subprocess → `Evolutionary.search` → Draft/Improve/Crossover → task execution → result parsing and possible Debug → journal/islands → next generation → selected code. Owner: runner owns task lifecycle; solver code owns scheduling and admission; models propose code and optionally analyze execution. Identities include task name, sample epoch, generation, node and parent IDs, with checkpoint/journal correspondence. Representational form: symbolic scheduling, Python programs and metric comparisons, plus natural-language proposal/analysis prompts. SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

- Immediate return: updated task state and best code/node; runner writes final code, statistics and submission feedback.
- Later read-back: journal/checkpoint reload reconstructs the search population; optional operator memory is supplied from journal-derived nodes. Detailed memory revisions belong to the memory report.
- Delegated visibility: each model receives constructed operator data, not the whole runner process; evaluation receives extracted Python and the selected task/data configuration.
- Selection predicate: first generation drafts; later code samples parents/operator under configuration. Non-buggy evaluated programs are eligible; nonempty-island admission compares score to average island fitness with task-specific direction, not a universal parent-improvement test.
- Invalidation or expiry: island capacity evicts weakest members; failed Debug paths need not become solutions; generation/time/step limits stop search. Journal history can outlive island membership.
- Activation or effect: selected parents and feedback are passed into later proposal prompts; program behavior and actual model reliance are unobserved. Code chooses the next operator and executes the returned program through the task backend.
- Evidence limits: static source wiring only; no task execution, endpoint identity or improved score established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and roles: computation proposes/samples/selects within a bounded task experiment; the operator supplies task and configuration, not a per-candidate approval in this path. Code can reject invalid candidates or island admission, and an operator can stop/reconfigure the workflow. The answer oracle is the configured evaluator/metric contract, with analysis-model fallback and score-source exceptions in [RT-RTE-sandbox-evaluation](#rt-rte-sandbox-evaluation). Guidance includes task description, code/output feedback and optional experience. Prompted consistency is not an enforced invariant. Rejected candidates can remain in history. Recovery uses checkpoints and existing nodes, rather than a transactional undo of externally executed code.

> if current_island.size == 0:
>     improvement_condition = True  # Always add to an empty island
> elif fitness_score is None:
>     improvement_condition = False  # A solution with None fitness never improves an island
> else:
>     improvement_condition = (self.lower_is_better and fitness_score <= island_avg_fitness_score) or (
>         not self.lower_is_better and fitness_score >= island_avg_fitness_score
>     )
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> Propose exactly one improvement idea that is different from the previously explored improvement ideas.
> Keep the evaluation method consistent across iterations.
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml`

This establishes a request for distinct changes and consistent evaluation, not content-directed scientific criticism or reliable compliance. No theory-builder, learning or exercised self-improvement conclusion is assigned from score selection alone.

#### RT-RTE-sandbox-evaluation
Label: Sandbox execution and fitness feedback

Endpoints and progression: task action/code → `SandboxMLEBenchTask` → authenticated CPU/GPU sandbox HTTP client → controller/dispatcher → worker shell execution and metric evaluation → score/log payload → task fitness → solver result parsing. Owner: task client owns request/protocol selection; dispatcher owns worker session polling/deadlines; task metric and external dataset supply the scoring contract. State includes job/session IDs, task data path, validation/test phase, status and timing. Representational form: symbolic requests, executable Python and scalar metrics; natural-language logs and analysis are separate inputs. SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`, `OpenMLE-Gym/openmle-sandbox/node_controller/task_dispatcher/task_dispatcher.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`.

- Immediate return: status, raw/clear logs, feedback, score fields, job and timing metadata, then task fitness and execution result.
- Later read-back: evaluator outputs enter journal nodes/checkpoint through the search route; evaluator HTTP delivery itself is an immediate return, not independent proof of memory activation.
- Delegated visibility: sandbox receives code, task data directory, resource, phase/split and deadlines; model Analyze receives selected code/output through its operator path, not the external provider's internals.
- Selection predicate: phase/protocol selects score interpretation; deterministic finite validation fitness normally overrides analysis. Self-validation can explicitly trust model-printed validation score; missing deterministic evidence can trigger model analysis.
- Invalidation or expiry: client job/wait deadlines, dispatcher cancellation and shell-session cleanup; failure metadata can make a node buggy. External service behavior is a prerequisite, not proven by the client.
- Activation or effect: evaluation fields determine node validity and fitness used by subsequent search; actual execution and metric correctness are unobserved.
- Evidence limits: inspected client/protocol and dispatcher mechanisms, not deployed authorization, worker image internals or benchmark truth. The metric contract is task-relative, not an expected natural-language answer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: models propose programs; task/solver code decides score source and validity; Analyze supplies fallback judgment, not an answer oracle by itself. Operator configuration can change protocol, `trust_model_validation_score` and `use_test_score`; no per-candidate human veto is required in the inspected call chain. Operating mode is bounded executable task evaluation. Its answer oracle is task-specific metric/data/reference outcome supplied by task packages and external datasets, not a universal independent adjudicator.

> if trust_model_score:
>     selection_score = model_final_validation_score
>     selection_score_source = (
>         "model_final_validation_score"
>         if model_final_validation_score is not None
>         else "model_final_validation_score_missing"
>     )
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/base_task.py`

> if self.cfg.use_test_score:
>     test_score = aux_eval_info.get("score", None)
>     aux_eval_info["validation_score"] = response["metric"]
>     response["metric"] = test_score
>     self.logger.info(f"Using Test score: {test_score}")
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

Deadline guarantee: owner is dispatcher, enforcement is polling followed by `controller.kill`, strength is best effort because controller/network response and actual descendant termination are external contracts. It covers sessions routed through this helper, not direct local NatureBench or Gym imports.

> if remaining is not None and remaining <= 0:
>     controller.kill(session_id)
>     print(f"[sandbox-http] job {job_id} session {session_id} timeout")
>     raise SandboxCommandTimeoutError(
>         session_id,
>         f"Job {job_id} exceeded timeout while executing command.",
>         view=SandboxResultWrapper(last_snapshot),
>     )
> --- `OpenMLE-Gym/openmle-sandbox/node_controller/task_dispatcher/task_dispatcher.py`

#### RT-RTE-async-search
Label: Async steady-state search

Endpoints and progression: `execution_mode=async_steady_state` → worker-specific work items → concurrently generated/evaluated candidates → locked commit → evolving islands/journal → next work item. Owner: solver code, not worker models, owns operator choice and commit acceptance. State includes attempt/generation IDs, parent-selection traces, worker/GPU/sandbox identity and shared search counters. The selected worker can call native task async execution or a thread fallback to `step_task`. This is a scheduler alternative to [RT-RTE-evolution-search](#rt-rte-evolution-search), not another model agent with an independent mandate. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

- Immediate return: committed node or rejected commit; the overall search returns selected code/state.
- Later read-back: accepted commits enter the same journal/checkpoint mechanism and later island selection.
- Delegated visibility: work item carries selected parents/operator and assigned worker sandbox URL; fallback copies task state before evaluation.
- Selection predicate: no available solutions forces Draft; otherwise configured parent/operator sampling applies, with Crossover disabled when insufficient parents. Commit rejects work after stop conditions and only admits non-buggy candidates to the database when requested.
- Invalidation or expiry: effective-time, optional wall-time, step and attempt limits; periodic checkpoint commits. A finished candidate can be rejected after budget exhaustion.
- Activation or effect: commits update later parent pools; concurrency changes which evaluations can complete and be admitted. No performance benefit is measured here.
- Evidence limits: source scheduling/locking inspected, not race-free distributed execution, throughput or externally enforced deadlines.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision/admission roles and mode: bounded multiworker task search; code proposes the next work item, models propose code, task evaluation supplies fitness, and code can veto commit. Human contribution is initial configuration and stopping, not inspected per-commit approval. Oracle is the selected task backend, not concurrency itself. Guidance and rollback are inherited operationally from operator inputs and journal recovery, not inferred from the route's name.

> async with commit_lock:
>     if self._should_stop_async_search(
>         task=task,
>         include_attempt_limit=False,
>     ):
>         return False
>     self._append_evaluated_node(node)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

Budget guarantee: policy owned by solver at scheduling/commit checks; it does not cancel every in-flight external effect. The separate shipped runner wraps operator calls before entry:

> def wrapped(*operator_args: Any, **operator_kwargs: Any) -> Any:
>     if should_stop_search():
>         raise StopSearch("Search budget reached.")
>     return fn(*operator_args, **operator_kwargs)
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

#### RT-RTE-naturebench-execution
Label: NatureBench execution alternatives

Endpoints and progression: NatureBench/local adapter configuration → shared runner with `NatureBenchTask` → attempt workspace and candidate preflight → local Python, local Docker or remote SCM Docker → evaluation service → aggregate-improvement payload → shared search selection. Owner: task adapter chooses execution and service contract; model proposes candidate Python. Representational form: symbolic execution/configuration and aggregate scores, plus natural-language task guidance and logs. SRC-1, `OpenMLE-Evo/scripts/evaluate_naturebench.py`, `OpenMLE-Evo/scripts/run_naturebench_local.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`.

- Immediate return: annotated execution/evaluation payload, including aggregate and possibly clipped selection score, workspace and attempt index.
- Later read-back: shared search records these results; no independent durable memory mechanism is inferred merely from attempt directories.
- Delegated visibility: candidate gets selected task data/output environment; evaluator receives output directory; local execution grants host-process authority whereas Docker grants configured mounts and optional GPUs.
- Selection predicate: execution mode dispatches local, SCM or local Docker; preflight failure bypasses execution/evaluation. Aggregate-improvement is the task's score basis. Final-submit configuration can reuse search-stage result rather than require a new test invocation.
- Invalidation or expiry: candidate execution timeout, local process-group termination or Docker cleanup paths; GPU wait can be exempt from search budget. External evaluator/service and remote-host enforcement are unverified.
- Activation or effect: executes generated program and feeds the aggregate into selection. Local mode is a material alternative to claims that every generated program is sandbox-contained.
- Evidence limits: local/dispatch/Docker and evaluation aggregation inspected; remote SCM infrastructure and external NatureBench evaluator are not captured. Correctness of hidden reference outcomes is unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Roles and oracle: code selects modes and candidates; model writes programs; external task evaluator supplies reference-based aggregate outcomes. Human/operator selects environment/task, with no per-program approval shown here. Bounded task experiment, not an open-ended autonomous deployment loop. Rejection is preflight, execution failure and normal search admission; recovery is attempts/checkpoint, not undo of arbitrary filesystem/network effects.

> if self.execution_mode == "local":
>     return self._run_local_solution(
>         code, workspace=workspace, output_dir=output_dir
>     )
> if self._uses_scm():
>     return self._run_scm_docker_solution(code, attempt=attempt)
> --- `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`

> process = subprocess.Popen(
>     self._local_python_command(str(run_path)),
>     cwd=workspace,
>     env=self._solution_env(output_dir),
>     stdout=subprocess.PIPE,
>     stderr=subprocess.PIPE,
>     text=True,
>     start_new_session=os.name == "posix",
> )
> --- `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`

> "Final submit skipped; using the best search-stage NatureBench "
> "aggregate_improvement recorded during exploration."
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

#### RT-RTE-gym-build
Label: Gym task construction and artifact admission

Endpoints and progression: supplied competition slug/build options → per-task process → compiled LangGraph → download/copy/web information/perception tools → description → generated preparation and retries → metric generation → task result. Owner: graph/router code owns progression; Gym models generate descriptions and executable scripts. Identities: batch, competition slug and task filesystem layout. Context is stage-specific: graph reset nodes return empty messages, while preparation explicitly retains and selects a short recent preparation history. Representational form: natural-language descriptions/prompts, symbolic tools/code and stage flags. SRC-1, `OpenMLE-Gym/openmle_gym/build.py`, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/builder_core/utils/nodes.py`.

- Immediate return: machine-readable task success/errors and generated package files; task workers return normalized results to the batch caller.
- Later read-back: prepared task package and metric can be consumed by evaluator/search; preparation retry reads selected previous messages. Specific cross-run memory revision is not assessed here.
- Delegated visibility: perception is bound to directory listing, CSV summary, text/Markdown reading and save tools with configured task paths. Generated preparation has a separate execution grant; isolated mode mounts explicit read/write paths.
- Selection predicate: routers inspect stage flags; preparation retries while retry budget permits; `Next` conjoins required stage-success flags. Metric admission compiles then writes model output, not a semantic proof or universal quality gate.
- Invalidation or expiry: preparation recreates target directories; failure decrements retries; per-task process timeout bounds the worker. Optional raw deletion is conditioned on success and a retained file-info placeholder.
- Activation or effect: scripts prepare public/private task files and supply future scoring machinery. Actual package construction/use is unobserved.
- Evidence limits: graph, script admission and relevant execution modes inspected; not every quality-check command or metadata mechanism. Source supports local checks, not task correctness or security of arbitrary generated code.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: operator supplies competitions/options and can stop/reconfigure; model proposes script content; code compiles, writes, executes preparation and validates expected files, with error-fed retries. No per-content human approval occurs in this inspected path. Guidance includes sample scripts, task description and prior preparation feedback. Persisted content includes `prepare.py`, `metric.py`, prepared data and `prepares.json`. Recovery regenerates/cleans directories; it is not restoration of every prior artifact. Operating mode is bounded task construction. Expected file layout is a local preparation check; downstream task metric is the scoring oracle, not a separately verified answer oracle for whether the model invented the right metric.

> response = self.llm_provider.query(
>     [query[0]] + self.todo["prepares"][-2:] + [query[1]]
> )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

The isolated command requires Docker/Podman and `OPENMLE_GYM_ISOLATED_IMAGE`, runs non-root, drops capabilities, disallows network, makes the root read-only and mounts declared paths. Its guarantee is conditional on selecting this path and a functioning host/container contract. The non-isolated branch directly imports/invokes preparation and is not covered.

> "--network",
> "none",
> "--read-only",
> "--pids-limit",
> "128",
> --- `OpenMLE-Gym/openmle_gym/process_runner.py`

> else:
>     prepare_func = self.get_prepare_function(comp_id)
>     if prepare_func is None:
>         raise ValueError("No prepare function found, code inexecutable")
>     prepare_func(
>         self.structure.raw_dir(comp_id),
>         self.structure.public_dir(comp_id),
>         self.structure.private_dir(comp_id)
>     )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

#### RT-RTE-sft-training
Label: SFT dataset admission and training

Endpoints and progression: scored search outputs/source prompts → collection → token-length filter → validation/test-gap annotation/filter → top-k per task → alignment dataset → separately launched SFT rollout/tokenization → actor training → checkpoints and rollout weight updates. Owner: data pipeline rules own dataset admission; launcher/operator chooses paths and hyperparameters; trainer owns numerical updates. Representational form: natural-language/code conversation content, symbolic filters/masks and distributed-parametric trained result. SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`, `OpenMLE-ERL/SFT/slime/train.py`.

- Immediate return: selection statistics/output paths; training yields saved checkpoints and numerical training state, not an automatically deployed search endpoint.
- Later read-back: SFT data buffer feeds selected conversation messages into token/loss-mask construction; saved model can be loaded later. Exact historical checkpoint-to-Evo serving handoff is unresolved.
- Delegated visibility: training consumes tokenized sample messages and masks; rollout engines receive updated actor weights. Intermediate selection controls which traces reach that consumer.
- Selection predicate: pipeline requires scored/feedback-success collection, token limit, relative-gap filter, per-task top-k and reward deduplication. Values and source metadata are operator-configured; these proxies are not independent proof of reusable improvement.
- Invalidation or expiry: rejected rows are excluded from selected dataset; launcher checkpoints periodically. It disables optimizer/RNG saving, limiting exact resumability; no automatic quality-regression rollback is established in the inspected loop.
- Activation or effect: supervised loss drives actor updates; trainer pushes weights to rollout engines. Improvement benefit and later deployment are unobserved.
- Evidence limits: pipeline-to-consumer wiring and trainer control flow, not full corpus lineage, weight diffs, exact optimizer semantics or training results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/roles: computation filters examples and performs updates; human/operator chooses inputs, thresholds and launch, not inspected per-example approval. The bounded curriculum uses task scores and validation/test-gap metadata as selection evidence; there is no universal expected-answer oracle for generated program text. Guidance is source conversation content and execution feedback retained in examples. Rejection can occur at dataset selection; recovery uses saved checkpoints but exact state replay is limited by save options. Models change parameters via [RT-CMP-training-models](#rt-cmp-training-models). This supports an implemented improvement-directed parameter-update pathway, not exercised self-improvement: the later live serving and causal dependence links are not established.

> collected, collect_stats = collect_sft_rows(
>     run_dir=config.run_dir,
>     source_parquet=config.source_parquet,
>     rejection_policy="accept_scored",
>     min_reward=0.0,
>     require_feedback_success=True,
> )
> --- `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`

> --rollout-function-path slime.rollout.sft_rollout.generate_rollout
> --prompt-data "${DATA_PATH}"
> --- `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`

> messages = sample.prompt
> tools = sample.metadata.get("tools", None)
> 
> token_ids, loss_mask = MASK_GENERATOR.get_loss_mask(messages, tools=tools)
> --- `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py`

#### RT-RTE-rl-training
Label: RL generation, reward and program admission

Endpoints and progression: RL launcher → patched external trainer → `generate_mle.generate` → search-selected parent/operator context → SGLang generation → `reward_func` execution/scoring/reward → sample metadata and conditional ProgramDatabase admission → trainer hook return. Sync scripts use upstream default barrier rollout; async scripts select `fully_async_rollout.generate_rollout_fully_async`. Owner: launch configuration, search code and reward hook split control; external SLIME owns optimizer/update scheduling. Representational form: natural-language/code prompts, symbolic sample/reward/database metadata, distributed-parametric actor updates delegated to external training machinery. SRC-1, `OpenMLE-ERL/RL/scripts/run_openmle_rl_sync_single_node.sh`, `OpenMLE-ERL/RL/scripts/run_openmle_rl_async_single_node.sh`, `OpenMLE-ERL/RL/train_with_patch.py`, `OpenMLE-ERL/RL/generate_mle.py`.

- Immediate return: generated `Sample`, then scalar final reward with metadata/logging; invalid or unsuccessful code can have a different storage fate from its training reward.
- Later read-back: subsequent generation calls ask the search algorithm to select parents from ProgramDatabase; explicit snapshot API persists that database. Upstream training consumption of reward is configured but not independently traced through the unavailable RL trainer.
- Delegated visibility: group members can share selected parent/context through a guarded cache; generation receives augmented system/user messages and task metadata. SGLang router resolves the live model.
- Selection predicate: search algorithm chooses task parents/mode; reward logic maps outcomes; database storage permits status 200 or categories `hack`, `no_verify`, `hack_verify`. Database inclusion is not trust or success certification.
- Invalidation or expiry: group parent-selection cache deletes after expected accesses; generation-abort/retry and snapshots offer recovery surfaces. Full async cancellation/staleness and upstream optimizer recovery remain uninspected.
- Activation or effect: retained programs are available to later parent selection; reward is returned to the trainer hook. Actual weight updates or reuse in a run are not observed in this source-only analysis.
- Evidence limits: RL hooks and launch wiring inspected; upstream SLIME, actual models/corpora and historical runs unavailable. SFT vendored training code is not substituted for upstream RL behavior.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/roles: models propose programs; search code chooses contexts; reward/database code decides stored categories and returns training signal. Human/operator supplies training data/configuration and launch, with no inspected per-program approval. Mode is bounded task-conditioned RL, with synchronous or fully async scheduling. Task execution/metric outcome supplies the reward reference; heuristic invalid-code categories are not answer oracles. Guidance includes task description, parent program and feedback. Program metadata, snapshots and trained checkpoints are distinct persistence channels; detailed database curation belongs to the memory analysis. Recovery is hook/engine dependent, not a universal rollback or automatic deployment gate.

> should_store_program = status_code == 200 or code_category in {"hack", "no_verify", "hack_verify"}
> if should_store_program:
>     program_id = db.add(program)
> --- `OpenMLE-ERL/RL/generate_mle.py`

> --custom-generate-function-path generate_mle.generate
> --custom-rm-path generate_mle.reward_func
> --- `OpenMLE-ERL/RL/scripts/run_openmle_rl_sync_single_node.sh`

The wrapper attempts logger/rollout patches but catches failures and continues. Therefore a launcher naming a patch is not an invariant that the patch was active:

> print(f"[TRAIN_WITH_PATCH] Warning: Failed to load rollout patch: {e}")
> --- `OpenMLE-ERL/RL/train_with_patch.py`

### Claims

#### RT-CLM-meta-evolution
Label: Training improvers for search

Claimed operation: search produces experience, experience enters training, and trained models return to search/evaluation; the first release presents this as bounded meta-evolution, not solved general RSI. Evidence layer: doctrine/design and reported operation only. Runtime wiring in this report supports separately runnable stages and parameter-update/serving interfaces. It does not close historical or causal links between a particular retained trace, trained weights, deployed endpoint and later outcomes. SRC-1, `README.md`.

> Search produces experience, experience enters training, and trained models return to search and evaluation.
> --- `README.md`

> OpenRSI begins with Meta-Evolution—training the improver itself in bounded, executable domains—without claiming that general recursive self-improvement has been solved.
> --- `README.md`

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-execution-authority
Label: Generated program and metric execution

Consumer: selected task execution backend and metric worker. Channel: generated Python is written/imported or passed through shell/subprocess/container execution; task `metric.py` is dynamically imported. Force: executable authority within the selected process/container/worker grants, not advisory prose. Horizon: one execution for candidate code, repeated task evaluations for retained metric modules. SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`, `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py`.

The capability surface is broad Python execution, independently of the finite perception tools. Deployment determines data mounts, GPU access, network and writable shared paths. The sandbox launch script weakens any blanket inference of isolated per-task ephemeral storage:

> --security-opt seccomp=unconfined \
> --name "$CONTAINER_NAME" \
> -p "$HOST_IP:$HOST_PORT:8080" \
> --gpus "device=$GPU_DEVICE" \
> -v "$NFS_MOUNT:$CONTAINER_WORKSPACE:ro" \
> -v "$NFS_MOUNT/mlsandbox:$CONTAINER_WORKSPACE/mlsandbox:rw" \
> -v "$NFS_MOUNT/mlsandbox_dev:$CONTAINER_WORKSPACE/mlsandbox_dev:rw" \
> -v "$NFS_MOUNT/mlsandbox_3:$CONTAINER_WORKSPACE/mlsandbox_3:rw" \
> -v "$LOCAL_SCRATCH_HOST_ROOT:$LOCAL_SCRATCH_CONTAINER_ROOT:rw" \
> --- `OpenMLE-Gym/openmle-sandbox/node_workers/sandbox_builder/start_sandboxes.sh`

This is implementation/deployment configuration evidence, not an observed escape or a claim that every task receives every host resource. See the distinct grants in [RT-RTE-gym-build](#rt-rte-gym-build) and [RT-RTE-naturebench-execution](#rt-rte-naturebench-execution).

#### RT-BAP-operator-guidance
Label: Operator proposal guidance

Consumer: operator model behind GenericLLM. Channel: rendered system/user messages containing task, prior code, feedback, optional selected experience and static guidance. Force: model-interpreted instructions; delivery is wired, compliance unobserved. Horizon: each proposal call, with journal-derived inputs across later rounds and checkpoint continuation. This is distinct from executable authority: Python does not become an effect until the task backend executes it. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/generic_llm.py`.

> if memory:
>     improve_data["memory"] = memory
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`

The proposal route consumes both static guidance and selected use-derived inputs. This establishes neither reliable semantic criticism nor that any delivered memory altered a particular completion.

## Annotations

none
