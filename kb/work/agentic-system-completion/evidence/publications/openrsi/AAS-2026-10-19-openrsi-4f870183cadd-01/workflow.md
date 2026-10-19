---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenRSI workflow account: generation-mode MLE program search from configured task request through repair, selection and artifact delivery."
run-id: AAS-2026-10-19-openrsi-4f870183cadd-01
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI workflow report

## Workflow account

### Selection and evidence boundary

This account selects Evo's generation-mode MLE search because it connects a shipped driver, model proposals, execution feedback, bounded repair and final output in one implementation. It does not join Gym construction, SFT and RL into a fictitious automatic end-to-end training workflow. Those are separate entry paths in [RT-RTE-gym-build](runtime.md#rt-rte-gym-build), [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) and [RT-RTE-rl-training](runtime.md#rt-rte-rl-training). The frozen boundary remains the [boundary member](boundary.md)'s complete artifact, partial loop.

All additional source inspection is SRC-1 implementation evidence at the reviewed commit: `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` operator handoffs, `debug_cycle`, generation search and return; and `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py` final selection, stop guards, output and cleanup. No search, model call, deployment or training was executed. The account establishes coordination wiring, not delivered historical results or measured improvement.

### Request and delegation

The request is a configured benchmark run, not a free-form conversation. As traced in [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation), the evaluation driver turns task/data, model and resource settings into prepare/runner configuration. Its task/sample child creates the task adapter, solver and restored journal. Task/sample identity scopes a search; node identities and parent edges scope candidate ancestry. The software scheduler, not a foreground model, owns the next-step decision.

In generation zero the solver drafts candidates. Later generations sample parents and an operator using population policy, temperature and configured crossover/fresh-draft probabilities. Draft, improve and crossover are model roles, not independent supervisors that can change the outer workflow. Improve receives task description, journal, selected parent, current step, remaining time and data preview through `execute_op_plan_code`; debug similarly receives its failed parent. These calls return plan, code and operator metrics and create new nodes rather than modifying the parent in place (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`). The configured operator model family and its unresolved exact weights are [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm).

These are selected operator call contexts, not evidence that each model sees the whole journal or host process. Prompt assembly and role-specific filtering remain as bounded by the runtime baseline; this account does not infer exact transmitted tokens from function arguments alone. Candidate code crosses a different handoff: `task.step_task` receives extracted source, and the adapter supplies code, task data location, resource/split and timeouts to remote execution. It returns execution output and scoring metadata. That execution authority is already recorded in [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution).

### Verification, admission and repair

The evaluator/parser, not the proposing model alone, normally determines whether a candidate is buggy and which metric selection uses. However, execution feedback is not a universal independent holdout oracle: the runtime traces finite sandbox fitness, optional printed-score trust, analyzer fallback and test-score substitution in [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation). The external sandbox/task metric contract remains a dependency, not independently authenticated truth.

A nonbuggy child enters the generation's candidate list. A buggy child enters [WF-RTE-debug-cycle](#wf-rte-debug-cycle); repair proposals must pass the same execution/parser path. Successful repair contributes only the last repaired node to the generation's solutions. Exhausted repair discards that individual from the generation. Discarding a candidate is not the same as erasing its journal evidence or rolling back external execution effects. Repeated recognized failures can request a fresh draft. Generation zero seeds islands; later generations call population admission/migration policy. The journal and population therefore have different roles: recording attempts is not identical to approving them as reusable population members (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`).

> if fixed_metric is not None:
>                         fixed_node = debug_path[-1]  # Get the last node (the fixed one)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

No per-candidate human approval is established in this path. The caller selects the task, models, budget and policy; models propose; software interprets feedback, schedules repairs and admits candidates. Neither passing these checks nor surviving selection demonstrates that an improvement plan is true or that a candidate is scientifically valid.

### Stop, recover and deliver

Generation search updates effective elapsed time, increments generation state and checkpoints before checking time/step termination. The runner additionally wraps all four proposal operators with a stop guard based on task stop, effective elapsed budget, optional wall budget and step count. A `StopSearch` exception is handled by saving a checkpoint and selecting the best available journal node. This is explicit budget recovery, not a catch-all successful-completion handler; unrelated errors are not thereby converted into delivered solutions (SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`). Resume and journal reconciliation are part of [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation); crash-atomic multi-file restoration is not established.

The runner reselects after search rather than blindly trusting the solver's returned node. For MLE it chooses the maximum node metric among non-root, nonempty-code candidates with a selection score. If no such scored candidate exists, it makes a seeded random selection among available code-bearing candidates; if none exist, it returns no node. Thus the filename `valid_code_final.py` does not certify successful verification. See the workflow annotation on [RT-RTE-final-submit](runtime.md#rt-rte-final-submit).

Delivery here means filesystem artifacts and task statistics, not proven external acceptance. The runner writes selected source (or an empty string with no node) to `valid_code_final.py`, and task-transformed source to `submit_code.py`. Enabled final submission calls `evaluate_code(best_code, phase="test")` for the configured repeats and writes per-attempt logs/feedback. It evaluates `best_code`, not the text just written to `submit_code.py`. Disabled final submission skips that loop and writes skip messages; earlier search execution is unaffected, as established in [RT-RTE-final-submit](runtime.md#rt-rte-final-submit). Statistics are then written. Cleanup calls `task.close` and stops logging in a `finally` block, preserving an earlier exception if cleanup also fails. Neither code export nor a test-call attempt proves a successful test result.

> best_code = best_node.code if best_node is not None else ""
>         (output_dir / "valid_code_final.py").write_text(best_code, encoding="utf-8")
>         submit_code = task.build_submit_code(best_code)
>         (output_dir / "submit_code.py").write_text(submit_code, encoding="utf-8")
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

The asynchronous alternate is deliberately not substituted for this trace: [RT-RTE-evo-async](runtime.md#rt-rte-evo-async) has separate sampling/commit locks and in-flight work semantics. This account establishes neither equivalent ordering nor stronger cancellation guarantees for that mode.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-debug-cycle
Label: Generation-mode debug cycle

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

This is the bounded repair subroute of the supplied generation search, not another declaration of the whole search. Endpoints: buggy node → debug operator → task execution/parser → repaired node or exhausted path → generation admission/discard. Software owns iteration and rejection; the configured debug model proposes replacement plan/code. The trigger is parser-marked bugginess. Task description, parent code/output through the operator path, remaining budget and data preview guide the proposal. The task evaluator/parser is the same conditional oracle as the parent route, not an extra independent verifier. Operating mode is bounded repair within benchmark search. No per-repair human veto is wired in the inspected function. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, supplies implementation evidence.

- Immediate return: updated task state, full debug path and repaired metric, or a null repaired metric when no attempt succeeds.
- Later read-back: with experience enabled the initial buggy node and evaluated attempts are appended during repair; otherwise the caller appends the returned debug path. The journal can be checkpointed and selected nodes can supply later proposal context; detailed memory admission is outside this subroute assessment.
- Delegated visibility: the debug call receives task description, journal, selected failed parent, current step, remaining budget and data preview through operator plumbing; the executor receives extracted candidate code, not a grant to change solver policy.
- Selection predicate: parser-marked nonbuggy status sets the repaired metric and stops repair; the caller uses a non-null repaired metric to admit the final repaired node to the generation list. Other population checks still follow.
- Invalidation or expiry: maximum debug depth bounds attempts; accumulated execution time is checked after an unsuccessful evaluated attempt against max_debug_time; execution/parsing exceptions inside the evaluation try block break the cycle. These checks are not a hard pre-attempt wall-time guarantee.
- Activation or effect: code wires new proposal nodes to execution and parsing, then success or discard; operational activation and benefit are not observed.
- Evidence limits: the debug proposal itself occurs before the local evaluation try block; that handler does not establish recovery from every operator error. No transactional rollback of executor effects, metric trust guarantee or reliable repair is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery changes the next candidate rather than reverting the environment. The returned failure path remains available for journaling; rejection from the generation does not mean the failure never persisted.

> except Exception as e:
>                 self.logger.error(f"Error during debug step execution/parsing: {e}", LogEvent.SOLVER)
>                 break  # Break the debug cycle on execution/parsing error
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> if not current_debug_node.is_buggy:
>                 fixed_metric = current_debug_node.metric.value
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-final-submit](runtime.md#rt-rte-final-submit)

Workflow-specific delivery qualification: final selection can fall back to code without a valid selection score. In the MLE branch, scored candidates are ranked by node metric; otherwise nonempty candidate source is selected with a task/sample/seed-derived random generator. With no candidate, export uses an empty string. This prevents interpreting output filenames or mere export as successful verification. The fallback is software-owned and does not ask a model or human to approve the final candidate. SRC-1 implementation evidence: `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`.

> if candidate_nodes:
>         stable_candidates = sorted(candidate_nodes, key=_node_sort_key)
>         rng = random.Random(f"{seed}:{task_name}:{sample_index}:final_select")
>         selected = rng.choice(stable_candidates)
>         setattr(selected, "_final_selection_source", "random_no_valid")
>         return selected
>     return None
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`
