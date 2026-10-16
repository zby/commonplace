---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Reflexion's ordinary HumanEval Python workflow from benchmark request through test feedback, diagnosis, revision and JSONL delivery."
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
reviewed-boundary: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
---

# Reflexion workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the ordinary programming Reflexion strategy, narrowed to HumanEval Python. It exposes a complete parent-code chain from task selection to candidate generation, local checking, diagnosis, revision and durable result. Unlike UCS scheduling or remote LeetCode grading, its consequential control branches are visible in the frozen parent source. It illustrates repeated model calls coordinated by software, not a hierarchy of delegated agents. The mechanism is already identified by [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt) and [RT-RTE-code-execution](runtime.md#rt-rte-code-execution); this member supplies a selective workflow account and annotations rather than redeclaring those routes.

Evidence is SRC-1 implementation at the [boundary](boundary.md)'s frozen revision. The shipped launcher requests HumanEval Python, GPT-4, one pass and two iterations (SRC-1, `programming_runs/run_reflexion.sh`). This is a source-supported intended invocation, not demonstrated execution. The runtime's inspected unconditional UCS import prevents treating the shipped CLI as launchable without its unavailable dependency. This report traces what the ordinary strategy implements conditional on reaching it; it does not silently assume the import gap is repaired. No target code, providers or tests were executed, and no saved results were used as observed-run evidence.

### Request, task ownership and generation handoffs

1. **Operator to driver.** CLI arguments supply dataset path, strategy, language, model, budgets and log location. `main` loads JSONL and passes these settings to the selected strategy. A dataset item supplies the function request (`prompt`), callable name (`entry_point`) and reference evaluator (`test`). The local process owns the loop; the model does not choose which benchmark item to attempt or authorize another iteration (SRC-1, `programming_runs/main.py`, `programming_runs/reflexion.py`; [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)).
2. **Driver to test generator.** At each pass the driver asks for internal tests from the task prompt, with a limit of one. Python keeps generated lines containing `assert`, filters them by syntax and samples up to that limit. These are model-authored provisional expectations, not the benchmark oracle. Syntax filtering checks parseability, not whether an assertion expresses the specification. An empty retained list is possible and the Python executor initializes its pass flag to true before iterating; no internal assertion then needs to succeed (SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/py_generate.py`, `programming_runs/generators/generator_utils.py`, `programming_runs/executors/py_executor.py`).
3. **Driver to implementation generator.** The first candidate receives the function request and static Python/code-block instructions. Its generation is a separate call from test generation. The generator parses returned code into a candidate string, which the driver installs as the current implementation and records before checking it. No independent worker receives a task package or possesses a separate acceptance decision (SRC-1, `programming_runs/generators/generator_utils.py`; [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl)).

The test-selection transformation is explicit:

> all_tests = parse_tests(output)  # type: ignore
> valid_tests = [test for test in all_tests if is_syntax_valid(test)]
>
> return sample_n_random(valid_tests, max_num_tests)
> --- `programming_runs/generators/generator_utils.py`

The driver fixes those selected tests throughout the current pass:

> tests_i = gen.internal_tests(item["prompt"], model, 1)
> --- `programming_runs/reflexion.py`

These handoffs are calls into adapters and an executor, not agent delegation. The model receives separately assembled requests; it is not given the driver's counters, success-control authority or complete accumulated log. For GPT-4's chat path, a successor receives static examples, previous code, current internal-test feedback, the latest reflection and the original function request as explicitly constructed messages. The entire reflections list is not replayed. The corresponding implementation and executable authority boundaries are retained in [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt) and [RT-BAP-executable-code](runtime.md#rt-bap-executable-code) (SRC-1, `programming_runs/generators/generator_utils.py`).

### Verification, rejection and recovery

**Internal failure is the normal revision trigger.** The executor runs each selected assertion with the candidate, then returns a pass Boolean, textual feedback and per-test outcomes. Feedback separates passing assertions from failing assertions with observed output or error descriptions. This checks the model's chosen tests, not general correctness. Execution happens before the correctness label; failure is not a veto on arbitrary program effects. Python shares executor globals and timeout handling is not a sandbox or general rollback mechanism, as documented by [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) (SRC-1, `programming_runs/executors/py_executor.py`).

If the initial candidate fails internally and an iteration remains, the driver supplies candidate and feedback to a separate diagnosis call. The Python instruction asks why the implementation is wrong and requests a short hint rather than new code. The driver retains that returned text without testing its explanation or requiring human approval. It then sends previous code, feedback, latest hint and the task request to a successor generation. Thus computation both proposes the diagnosis and admits the replacement. There is no per-content human veto in this inspected strategy. Actual diagnostic validity and model reliance on the hint remain unobserved; the runtime's theory assessments are not upgraded by this workflow trace (SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/py_generate.py`, `programming_runs/generators/generator_utils.py`; [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)).

**Reference evaluation has a different consequence.** An internally passing initial candidate is evaluated against the benchmark test and the outer pass loop breaks even if reference evaluation rejects it. That rejection supplies only a Boolean to the driver, not diagnostic reference feedback to a successor. The runtime retains the decisive branch quote in [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt). Consequently increasing the pass budget does not guarantee another attempt after this particular rejection (SRC-1, `programming_runs/reflexion.py`).

For a revised candidate, internal success or the last permitted iteration triggers reference evaluation. Acceptance marks the task solved; rejection ends the inner loop. If another pass remains, the driver generates new internal tests and a fresh simple candidate rather than revising from the reference failure. At the shipped one-pass/two-iteration settings, an initial internal failure allows one diagnosis and one successor. That successor is reference-evaluated even if it still fails internally. The benchmark evaluator executes candidate plus dataset test and calls `check(entry_point)`; exceptions map to false. This is the supplied benchmark's verdict under the executor's semantics, not a universal correctness proof (SRC-1, `programming_runs/reflexion.py`, `programming_runs/executors/py_executor.py`).

The revised-candidate branch retains the distinction between attempt completion and acceptance:

> if is_passing or cur_iter == max_iters - 1:
>     is_passing = exe.evaluate(
>         item["entry_point"], cur_func_impl, item["test"], timeout=10)
>     if is_passing:
>         item["solution"] = cur_func_impl
>         is_solved = True
>         num_success += 1
>     break
> --- `programming_runs/reflexion.py`

Recovery is therefore bounded candidate retry, not restoration of previous effects or a verified explanation. Budgets require external calls to return; they do not establish wall-clock termination. Unhandled generation, parsing or write failures are not covered by a task-level checkpoint/recovery handler in the inspected strategy (SRC-1, `programming_runs/reflexion.py`; [RT-RTE-code-execution](runtime.md#rt-rte-code-execution)).

### Delivery and later restart

A task is delivered when the driver appends a JSONL row containing the original task fields, `is_solved`, all recorded implementations, internal-test feedback, reflections and the last candidate as `solution`. This happens whether or not reference evaluation accepted the candidate. The function returns no program object; `main` prints the log path after strategy completion. Thus the delivered artifact is an experiment result row, possibly a failed program, not an assured correct implementation (SRC-1, `programming_runs/reflexion.py`, `programming_runs/main.py`; [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl)).

Restart uses the number of existing result rows to skip the same number of dataset entries. It does not compare task IDs or reload a partial task's candidate and reflections. It assumes compatible dataset ordering and output naming. A failure before append leaves that task available for a fresh attempt, not continuation of its interrupted diagnostic context. A written unsolved row is still skipped. Logs are retention and positional completion bookkeeping, not a cross-task reflection consumer (SRC-1, `programming_runs/utils.py`; [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)).

> for i, item in enumerate(dataset):
>     # skip items that have been processed before
>     if i < count:
>         continue
>     yield i, item
> --- `programming_runs/utils.py`

This member independently inspected the full ordinary driver, CLI, launcher, JSONL/resume utility, Python generator, shared generation utilities and Python executor. These paths were already included in the supplied runtime's coverage; no additional source or execution layer is introduced. Other task families, strategy variants, opaque provider behavior and missing dependencies retain their boundary/runtime limits. Nothing here establishes that an attempt ran successfully, that a diagnosis was accurate, or that reflection caused better results.

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

#### On [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Workflow-specific handoff: the Python path requests at most one syntax-filtered internal assertion per pass, then reuses that set for all revisions in the pass. Successor context contains only the latest hint and feedback alongside previous code, static examples and the task request; the accumulated result lists remain driver-side. The host owns every transition. Internal failure permits diagnosis; reference rejection of an internally passing initial candidate breaks the outer loop. Reference rejection of a revised candidate permits only a new pass if its budget remains. Delivery is JSONL append irrespective of `is_solved`. Restart skips persisted rows positionally and does not restore interrupted task context. These findings are supported in the Workflow account above (SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`, `programming_runs/utils.py`).

#### On [RT-RTE-code-execution](runtime.md#rt-rte-code-execution)

Workflow-specific verification boundary: internal checking supplies detailed textual feedback to diagnosis, whereas benchmark evaluation supplies only a Boolean to scheduling. Neither gate reviews the diagnosis itself. Python benchmark acceptance executes the dataset test and invokes `check` on the requested entry point. A false verdict rejects the correctness label, not necessarily delivery, and does not restore program effects. Source-only evidence cannot establish safe execution or successful recovery (SRC-1, `programming_runs/executors/py_executor.py`, `programming_runs/reflexion.py`).
