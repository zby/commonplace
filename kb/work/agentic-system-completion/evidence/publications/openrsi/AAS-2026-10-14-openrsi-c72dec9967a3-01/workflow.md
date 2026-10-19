---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenRSI workflow: MLE-Bench program search from configured task to evaluated candidate, bounded repair and retained final outputs."
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI workflow report

## Workflow account

### Selected workflow and evidence basis

The representative workflow is the shipped MLE-Bench evaluation invocation: an operator supplies tasks and search configuration; separate task processes search for programs; a selected program is written and optionally evaluated in the test phase. It was selected because it connects proposal, execution, verification, repair and delivery within one shipped call chain. It does not join the separately launched Gym, SFT and RL stages into an invented autonomous training cycle. The stage boundary and external dependencies remain those of [boundary](boundary.md).

The entry chain and shared search mechanism are established by [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search); score interpretation is established by [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation). This member adds inspection of final-node selection, final output writing, task-process failure handling and synchronous Debug progression. All additional evidence is SRC-1 implementation at the frozen commit, in `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` and `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`. No target execution or supplied execution trace establishes that any particular search completed or improved a program.

### Handoffs from request to evaluated proposals

1. **Operator to batch adapter and runner.** The adapter writes preparation/runner configuration and launches task preparation and the shipped runner. The runner assigns each task/sample its own output directory and task subprocess, under a concurrency semaphore. Each subprocess receives task-directory, output-directory, resolved-runner-config and sample-index arguments. The subprocess boundary separates task lifecycles; it is not a model delegation with an independent goal. SRC-1, `OpenMLE-Evo/scripts/evaluate_airaevo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`; [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search).
2. **Task process to solver and operator models.** The process constructs the task and solver and reloads retained search state. Solver code chooses the next operator and parents. Draft starts candidate production; later Improve and Crossover operate on selected prior candidates. The operator receives constructed task, parent and feedback inputs, not the whole batch process or an automatically accumulated conversation. Optional journal-derived experience can cross this handoff. Separate configurable clients do not establish separate model weights. See [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm) and [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance).
3. **Model to executor.** A proposal becomes a node containing plan, code, parent relationships and operator metrics. Extracted code goes through the task backend for execution. This is a change from model-interpreted guidance to executable authority, with the selected backend's grants, not a per-program human approval. See [RT-BAP-execution-authority](runtime.md#rt-bap-execution-authority).
4. **Evaluator to solver.** Execution feedback supplies validity and fitness. Deterministic validation normally supplies fitness, but the configured protocol can trust a model-printed validation score, and analysis can be a fallback. Thus acceptance is relative to a configured evaluator contract, not a universal independent correctness oracle. Non-buggy candidates compete for island admission against average island fitness; they need not improve the parent or beat the current best. These predicates and their retained passages are in [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation) and [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search).

### Repair, rejection and continuation

A buggy result transfers control to the solver's Debug cycle, not to a human reviewer. Debug receives the failed parent and selected context and proposes another program. The solver executes and parses that attempt before considering it fixed. The synchronous cycle stops on a non-buggy result, depth exhaustion, accumulated execution-time limit, or execution/parsing exception. This is bounded repair, not proof that the cause was correctly diagnosed. The workflow-specific details are annotated below on the existing search record.

The shipped runner also guards operator entry against search budgets. A `StopSearch` exception saves the checkpoint and proceeds to final selection from available history. These guards do not preempt an in-flight external call. The async scheduler additionally rejects commits after stop conditions, but that is an alternative scheduler rather than an extra stage of this synchronous trace; see [RT-RTE-async-search](runtime.md#rt-rte-async-search). Checkpoint/journal continuation is distinct from skipping an already completed task/sample, and neither undoes effects already produced by candidate execution.

### What delivery means

Delivery has three distinct observable interfaces in the implementation: final code artifacts, optional test-phase evaluation artifacts, and the batch runner's task status. None alone establishes a good solution. Final selection can fall back to a seeded random code-bearing journal node when no scored candidate qualifies. With no candidate, final code is empty. A task subprocess exiting zero is reported successful by the batch runner without rerunning the stricter resume-completeness predicate. These details are established in [WF-RTE-final-delivery](#wf-rte-final-delivery).

Consequently, file names such as `valid_code_final.py` do not certify validity. Test-phase evaluation, when enabled, supplies separate outcomes after selection; it is not a prerequisite to writing final code. Configured submission skipping removes even that fresh evaluation. The NatureBench search-score reuse exception is already established by [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution). External benchmark truth, successful sandbox operation, model compliance and improved performance remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-final-delivery
Label: Final selection and delivery

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

This is the terminal selection/output part of the supplied search route, not a replacement for its proposal/evaluation loop. Endpoints: journal after search or budget interruption → final-node selector → code files → optional test-phase evaluator → submission logs/statistics → subprocess result. Owner: `single_task_runner.py` owns selection and artifact writing; `runner.py` owns process outcome reporting. Context/state includes task, sample, seed, benchmark, journal and submission-repeat configuration. Symbolic selection rules operate on program strings, node metrics and filesystem artifacts. SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`.

- Immediate return: final validation/submission code, submission logs and task statistics on the normal path; parent runner receives process exit status and constructs a task-result object.
- Later read-back: strict resume reads required output files and `stat.json`; it skips a completed task/sample only when its completeness predicate and non-null submit score pass. Checkpoint reload is a separate earlier handoff.
- Delegated visibility: final evaluator receives selected code with `phase="test"`; parent runner observes process return code rather than re-evaluating the candidate.
- Selection predicate: MLE-Bench selects the maximum node metric among code-bearing non-root nodes with a selection score; otherwise seeded random selection chooses a code-bearing candidate, or returns no node. Optional final submission evaluates selected code for configured repeats. Strict resume checks code/stat files, submission logs and non-null score, with a NatureBench skip exception.
- Invalidation or expiry: no final quality veto is shown before writing code; absent node yields empty code. Process launch exceptions and nonzero exits produce failure reporting. Task/logger cleanup runs in `finally`; search checkpoints permit continuation, not rollback of generated program effects.
- Activation or effect: selected code is written to final files and, when enabled, evaluated again. File writing is wired; successful execution, later external use and benefit are unobserved.
- Evidence limits: inspected source controls and output predicates only. Zero subprocess exit is not evidence of valid output or a correct benchmark solution. Runtime deployments and task data remain external.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision and admission: code decides selection and writing; models previously proposed candidates. The operator supplies seed, task, budgets and submission settings, not per-final-program approval. The bounded experiment's oracle is the configured task evaluator when invoked, not the output filename or process exit. Search interruption triggers selection from existing history; no new model proposal is required. Guidance and feedback reside in earlier operator inputs, and persisted results here are code, logs and statistics, not updated model parameters.

The fallback deliberately permits delivery without a qualifying scored node:

> if candidate_nodes:
>     stable_candidates = sorted(candidate_nodes, key=_node_sort_key)
>     rng = random.Random(f"{seed}:{task_name}:{sample_index}:final_select")
>     selected = rng.choice(stable_candidates)
>     setattr(selected, "_final_selection_source", "random_no_valid")
>     return selected
> return None
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

Writing final code precedes optional test evaluation:

> best_code = best_node.code if best_node is not None else ""
> (output_dir / "valid_code_final.py").write_text(best_code, encoding="utf-8")
> submit_code = task.build_submit_code(best_code)
> (output_dir / "submit_code.py").write_text(submit_code, encoding="utf-8")
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

> submit_result = task.evaluate_code(best_code, phase="test")
> submit_results.append(submit_result)
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

The parent runner marks a nonzero return as failure; its normal return path reports success from process completion, separately from resume checking:

> if return_code != 0:
>     error = f"AIRA Dojo task failed: {task_name} (return_code={return_code})"
>     logging.error(error)
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`

> return {
>     "success": True,
>     "skipped": False,
>     "task_name": task_name,
>     "epoch_index": epoch_index,
>     "output_dir": str(output_dir),
>     "return_code": return_code,
>     "error": None,
> }
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

Workflow-specific repair handoff: synchronous `debug_cycle` passes the most recent failed node to Debug, evaluates extracted replacement code through `task.step_task`, and parses the result. It returns updated state, the full debug path and a fixed metric or `None`. A non-buggy result ends repair; otherwise configured depth/time limits bound further attempts. Execution/parsing exceptions break the cycle. Experience-enabled operation appends evaluated failed/repair nodes, so repair history and solution admission are different outcomes. This adds repair detail, not a new declaration for the same search route. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

> fixed_node_attempt = self._debug(current_debug_node)
> # Evaluate the attempt
> try:
>     state, eval_result = task.step_task(state, extract_code(fixed_node_attempt.code))
>     self.parse_eval_result(node=fixed_node_attempt, eval_result=eval_result)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> except Exception as e:
>     self.logger.error(f"Error during debug step execution/parsing: {e}", LogEvent.SOLVER)
>     break  # Break the debug cycle on execution/parsing error
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> if not current_debug_node.is_buggy:
>     fixed_metric = current_debug_node.metric.value
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

This is a source-wired recovery policy. It neither establishes reliable repair nor content-directed criticism of a formulated theory; no exercised learning or self-improvement conclusion is inferred from the loop.
