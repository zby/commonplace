# Workshop: build the code orchestrator

- **Posed:** 2026-09-29, by the operator's direction.
- **Design:** [Code-scheduled workflows](../../reference/proposals/code-scheduled-workflows.md). Read it first; this file does not repeat the model.
- **Closes when:** the core module passes the tests listed below, the first analysis definition has run through it (that work belongs to [analysis-offload-to-code](../analysis-offload-to-code/README.md)), and the interface changes that definition forced are made. Then the proposal becomes an ADR and archives, the commands are described in `kb/reference/`, the agent orchestrator's loop text lands in `kb/instructions/`, and this workshop is deleted.

## Goal

Build the core of the proposal as a module that can be tested on its own: a program runs a workflow definition, keeps all run state on disk, executes every step it can, and stops only where it needs a sub-agent. The agent orchestrator launches the jobs the program names and runs it again.

The purpose is to get as close to a code scheduler as a harness without one permits. The operator expects harnesses to adopt code scheduling of their own, so the definition should read like a native workflow script and the machinery that exists only because code cannot launch sub-agents should stay small.

## Boundary

In scope:

- the core: the `step` and `report` commands, the asynchronous `agent()` call with wait, the job record, input-matched acceptance, the blocked and uncertain-state outcomes;
- small test definitions and a test driver that plays the agent orchestrator by writing scripted outputs;
- the agent orchestrator's loop text, written once and tried in each supported harness with a test definition.

Out of scope:

- the analysis workflow definition, its job split, its prompts and validators, and the offload backlog items. These belong to [analysis-offload-to-code](../analysis-offload-to-code/README.md);
- a second workflow, repair jobs, staggered progress, and code-side launching in Claude Code. The proposal lists them as later options.

## Decided (operator, 2026-09-29)

- The core is a module separate from the analysis code. It does not import analysis code.
- It is built before the batch 01 rerun, so the rerun tests it together with the offload backlog.
- Error recovery: code retries a failed job once, carrying the validator's message. After that `step` returns a blocked outcome and the agent orchestrator repairs within the scope the definition declares.
- The agent orchestrator does not write or edit the content of a job's output. This is the analysis workflow's repair scope; the core only carries the scope a definition declares.
- The agent orchestrator reports listed events only: a failed launch, a repair, a stop.
- `report` is a command separate from `step`. `step` takes the run and nothing else.
- The code is separate from the earlier code: it imports nothing from the analysis, review or freshness code, and they import nothing from it until the analysis definition is written.
- Tests come first. Each behaviour is stated as a test before the code that provides it.
- The code is object oriented, and the command shell is separate from the objects. The shell parses arguments and prints; every behaviour is reachable, and tested, through the objects without the shell.

## What the tests must show

None of these tests uses a model or the analysis package.

1. Pending jobs on two independent paths are returned in one round.
2. A wait on an accepted output continues at replay. A second `step` on an unchanged run returns the same result as the first.
3. A job's identity does not depend on the order in which paths run.
4. Changing a declared input's bytes makes an accepted job pending again.
5. An output is refused when an input changed between hand-out and completion.
6. Changing an accepted output's bytes makes the job pending again.
7. An output that fails its validator is not accepted. The job is handed out once more with the validator's message, and a second failure gives a blocked outcome.
8. At the attempt limit the blocked outcome permits only stopping.
9. A missing output makes `step` name the job again.
10. A problem report written where the output would go is read by `step`.
11. A report is stored and appears in the failure record. No report causes an acceptance. A run completes when every report is omitted.
12. When the process ends after a step's outside effect and before the effect is recorded, the next `step` recognizes the effect or stops with the uncertain-state outcome. It does not repeat the effect.

Test 12 uses a test step with an outside effect. Making the real publisher recognizable after an interruption is a change to analysis code and belongs to the offload workshop.

## Left to the build

The builder chooses these from what the code and tests show, answerable to the goal and the tests above:

- how acceptance, hand-out, failure and report records are laid out in the run directory;
- what `step` prints per job beyond the prompt path and launch parameters;
- command and module names. "Job" already means a review job, so names should keep the two apart;
- how much of a report is fixed form.

## What "asynchronous" means here

The drafted API uses explicit handles in ordinary synchronous code, with no asynchronous library and no coroutines. It awaits the operator's review.

- `agent()` names a job and returns a handle at once. The job is handed out at the end of the step whether or not the definition waits on it.
- `wait()` on a job that is not accepted ends the path that called it, for this step.
- `parallel()` runs independent paths one after another. Each runs to its end or to its first such wait, so every path gets to name its jobs.

The reason is that a wait on a pending job cannot be satisfied inside the process: the worker runs only after the process has exited. A path that stops is therefore not continued later; the next `step` runs the definition from the top. Coroutines exist to continue a stopped path, which this design does not do, so ending the path is enough. "Asynchronous" names one property: naming a job is separate from waiting for it.

Where a later runtime lets code launch sub-agents, `wait()` blocks and `parallel()` runs its paths concurrently. The definition keeps its form.

The interface stays open to change until the first analysis definition has used it. That definition includes parallel lenses, reconciliation and a correction cycle, which are the cases expected to show how much machinery the runner needs.

## Constraints

- **One writer per output.** Recovery after a lost session requires the earlier session's workers to have stopped. The core does not support overlapping attempts.
- **Method paths.** Publication requires the running package to equal the method commit. New commands join what must be committed before an analysis run opens, so land them between batches.
- **Tests.** `uv run pytest`, all passing.
- **No retained compatibility and no unused features.** A gap found during the build is written down here or in the proposal, not implemented ahead of need.

## Coupling

- [analysis-offload-to-code](../analysis-offload-to-code/README.md) — depends-on: its build order starts from this core, and its first definition is the test of this interface
- [agentic-analysis-output-documents](../agentic-analysis-output-documents/README.md) — see-also: owns the set and publication contracts that the analysis definition will call
- [runner-execution-profiles](../runner-execution-profiles/README.md) — see-also: defines the model and effort choices that a job's launch parameters would carry; the core emits them as data and does not choose them

## Log

- 2026-09-29: workshop opened. Nothing built.
- 2026-09-29: the API is drafted as stubs in `src/commonplace/workflow/` (`job.py`, `engine.py`, `shell.py`), with docstrings that state the behaviour and no implementation. 69 tests in `tests/commonplace/workflow/` state the guarantees against that API, with a scripted agent orchestrator in `definitions.py`. The tests are skipped by default and run with `COMMONPLACE_WORKFLOW_TESTS=1 uv run pytest tests/commonplace/workflow`; all but the import check fail until the core is implemented. Next: operator review of the API and tests, then implementation.
