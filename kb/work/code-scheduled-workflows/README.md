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
2. A wait on an accepted output continues at replay. A second `step` on a finished run reports it finished again. `step` without worker activity consumes a round: attempts increase and the job ends blocked.
3. A job's identity does not depend on the order in which paths run.
4. Changing a declared input's bytes makes an accepted job pending again.
5. An output is refused when an input changed between hand-out and completion.
6. Changing an accepted output's bytes makes the job pending again.
7. An output that fails its validator is not accepted. The job is handed out once more with the validator's message, and a second failure gives a blocked outcome.
8. At the attempt limit the blocked outcome permits only stopping.
9. A missing output makes `step` name the job again.
10. A problem report, written to a path beside the output, is read by `step`. It blocks at once, and the report and any output beside it are moved into the state directory, so a flagged output is never accepted and the report does not block again after the repair.
11. A report is stored and appears in the failure record. No report causes an acceptance. A run completes when every report is omitted.
12. When the process ends after an effect and before the effect is recorded, the next `step` establishes what took place. An effect that took place in full is not repeated, one that did not begin is run, and one that took place in part gives the uncertain-state outcome. A missing or failing recognizer also gives that outcome.
13. A completed effect whose inputs have changed stops the run. It is not repeated, and the run does not report itself finished.
14. Changing a job's launch parameters makes an accepted job pending again.
15. A path owned by two jobs is refused before any job is handed out. Each job owns its output and its problem report; no job may write into the state directory.
16. Tests 12 and a whole run are repeated with every step in its own interpreter, with a file-backed effect and an abrupt exit.
17. The operator resolves an uncertain effect as completed or as absent, and the run continues. A step gives one outcome, the first that applies of uncertain, blocked, launch, done; an uncertain outcome carries the blocks found with it. An uncertain step changes no job's state and counts no attempt or repair.
18. A file that is refused, or an accepted output that someone changed, is moved into the state directory and kept.
19. Two jobs are the same task when prompt, output, inputs and launch parameters agree. The validator is not compared and is not part of the input state; it runs whenever the job is judged, so a changed validator reopens an accepted output it now refuses, with a full set of attempts. Within one step, the first declaration of a job supplies its validator. The input state uses the prompt as the definition gives it, and holds no absolute path of the run directory.
20. Attempts are counted per hand-out. The retry limit starts over after a blocked outcome and after an acceptance. A refusal of a never-accepted output for a changed input counts as a failed attempt; an accepted job reopened by a changed input or output gets a full set of attempts.
21. An error raised by an effect blocks on `workflow`; the next step asks the recognizer what took place.
22. Failures of steps that code executes are counted by the place where the error was raised: the innermost frame in the definition's own files, so an error inside a shared helper or the standard library is counted at the definition's line that called it. Two unrelated failing steps each get their repair.
23. A `step` in another process, while one is running on the run, is refused, and the shell returns 1 saying the run is busy. The lock is an operating-system file lock, so it ends with its process; a second step within one process is not specified. Malformed shell arguments exit with status 2.
24. A block that permits only stopping ends what the agent orchestrator may do, not the run. The operator releases a stopped job or the stopped `workflow`; it is tried again with its attempts and repairs starting over, and accepted outputs of other jobs are untouched.
25. The block on an effect whose inputs changed is judged anew in every step. It goes away when the inputs are restored, or when the operator records the effect as completed or as absent.
26. An effect stays owed after the definition stops calling it. When the definition runs to its end, a completed effect it did not reach gives a stop-only block and a started one gives the uncertain outcome; a step that ends at a wait checks nothing. The operator lets the effect stand (completed) or withdraws it (absent).
27. `workflow` is reserved and cannot name a job.
28. A step that ends before its records are written changes none of them: the next step sees the run as it was. Only an effect's start and completion are written while the definition runs.
29. State records that are missing, unreadable or of another format version raise an error from `step` and from the shell; they are never read as an ordinary outcome, and no effect is repeated.
30. A job may not declare as an input the output of a job named in the same step and not accepted, nor its own output or problem report.
31. The default repair scope forbids changing anything under the state directory.
32. Recovery of an unfinished move does not move a later file with the same bytes: an existing kept copy is the receipt of a finished move.
33. A job whose input is the output of a job named in the same step and not accepted is refused, whether the reader is pending or accepted, and whichever of the two is named first. An accepted consumer's `wait` therefore cannot pass while its producer is pending.

An effect is a step that code executes and that must run once, because it changes the world outside the run or because its result cannot be reproduced; the proposal's vocabulary defines it against a job and a mechanical step. The tests on effects use a test effect that publishes files to a directory outside the run. Making the real publisher recognizable after an interruption is a change to analysis code and belongs to the offload workshop.

## Left to the build

The builder chooses these from what the code and tests show, answerable to the goal and the tests above:

- how acceptance, hand-out, failure and report records are laid out in the run directory;
- what `step` prints per job beyond the prompt path and launch parameters;
- command and module names. "Job" already means a review job, so names should keep the two apart;
- how much of a report is fixed form;
- how to test a process ending inside the step's own commit (between prompt files, the rename, and the moves). The tests end a step before its commit; ending one inside it needs fault injection that depends on how the records are written.

## What "asynchronous" means here

The drafted API uses explicit handles in ordinary synchronous code, with no asynchronous library and no coroutines. It awaits the operator's review.

- `agent()` names a job and returns a handle at once. The job is handed out at the end of the step whether or not the definition waits on it.
- `wait()` on a job that is not accepted ends the path that called it, for this step.
- `parallel()` runs independent paths one after another. Each runs to its end or to its first such wait, so every path gets to name its jobs.

The reason is that a wait on a pending job cannot be satisfied inside the process: the worker runs only after the process has exited. A path that stops is therefore not continued later; the next `step` runs the definition from the top. Coroutines exist to continue a stopped path, which this design does not do, so ending the path is enough. "Asynchronous" names one property: naming a job is separate from waiting for it.

Where a later runtime lets code launch sub-agents, `wait()` blocks and `parallel()` runs its paths concurrently. The definition keeps its form.

The interface stays open to change until the first analysis definition has used it. That definition includes parallel lenses, reconciliation and a correction cycle, which are the cases expected to show how much machinery the runner needs.

## Constraints

- **One writer per output.** Recovery after a lost session requires the earlier session's workers to have stopped. The core does not support overlapping attempts. The rule covers declared inputs too: code compares an input at hand-out and at judgment, so a change undone while the worker ran goes unseen.
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
- 2026-09-29: a review of the API found six gaps; all are taken up in the stubs and tests, with no implementation. Effects are tied to their inputs and stop the run when those change. Recognition has three outcomes (completed, absent, unknown). Launch parameters are part of a job's input state. Each job owns its output and problem report paths. `step` is documented as consuming a round. Three tests run every step in its own interpreter. 87 tests, all skipped by default.
- 2026-09-29: a second review found ten points where behaviour was unstated or stated only in tests; all are taken up in the stubs and tests. New in the API: `Orchestrator.resolve` and the shell's `resolve` for the operator, `Uncertain.blocks`, `Job.same_task_as`, `RunBusy`. `Context.params` is removed; parameters are on the definition. 117 tests, all skipped by default. The tests added since the implementation was removed have never run against an implementation, so they may hold errors of their own.
- 2026-09-29 (operator): a stopped run can be continued. The rule that it cannot was added in the second review's revision without a reason that holds: the repair limit bounds the agent orchestrator, not the run, and ending the run would discard accepted outputs. New in the API: `Orchestrator.release` and the shell's `release`; `resolve` also applies to a completed effect whose inputs changed. 128 tests.
- 2026-09-29: a third review found six points where docstrings and tests disagreed or the behaviour was loose; all are taken up in the stubs and tests. A problem report and any output beside it are moved when they block. Attempts are counted per hand-out, reset on acceptance, and a reopened job is not charged an attempt. An uncertain step counts nothing. Failures are placed at the definition's own line. The lock test now runs across two processes instead of nesting a step, and the shell's busy and usage exit codes are stated. 131 tests.
- 2026-09-29: a fourth review (Astra) found three gaps; all are taken up in the stubs and tests. An effect the definition no longer reaches is checked at the definition's end instead of escaping the check. The validator runs whenever a job is judged, so a changed validation policy reopens outputs it refuses; callables are still not compared. `workflow` is a reserved job name. 139 tests.
- 2026-09-29: the design was checked against the failure modes the review and freshness system has handled, without copying its design. Taken up: the step writes its records in one atomic commit after the definition finishes (effect records excepted); state that cannot be trusted raises `StateError` instead of reading as an ordinary outcome; a job may not read an unaccepted job's output or its own; the repair scope excludes the state directory. Documented as limits: an input changed and restored during a round, and the core's prompt frame outside the input state. 148 tests.
- 2026-09-29: the core is implemented in `src/commonplace/workflow/` (`job.py`, `engine.py`, `store.py` for the on-disk records, `shell.py`). The tests run by default; the `COMMONPLACE_WORKFLOW_TESTS` gate is removed. 151 tests pass: the 148 above and three added for gaps found in review of the implementation. (1) An error raised by an effect ends its path, so a broad catch in the definition cannot hide the block. (2) An absolute input path inside the run directory is recorded relative to it, so a moved run keeps its acceptances. (3) A stopped `workflow` gives Uncertain when an effect is started and not recorded, keeping the order uncertain, blocked, launch, done; the definition does not run while `workflow` is stopped. Choices left to the build:
  - Records: the layout is in `store.py`'s module docstring. `state.json` holds every job's record and is replaced whole by each step. It is written twice when a step moves files: once with the moves it owes, and once with none after they are done. Without the second write, a later step would repeat a listed move and take away a new output that has the same bytes.
  - `step` prints the outcome line, then one line per job with its name, prompt path and launch parameters as JSON. A blocked outcome lists subject, reason, record path, and what is permitted.
  - Names: the package is `commonplace.workflow`, and the shell is `python -m commonplace.workflow.shell`. No `commonplace-*` console script is registered yet. A new command widens the method paths, so it lands between batches.
  - Reports are free text with a fixed event and an optional job.
  - The step's own commit (prompt files, the state rename, the moves) is not tested with fault injection. Moves are checked by hash, and the second state write clears them.
  - A blocked step still judges every outstanding hand-out and counts its failure; it hands nothing out. On the next step, a job with no hand-out outstanding has the output in place judged against the input state of its last hand-out. This is how a repair gets a valid output accepted, and why an output that the definition never handed out is not.
  Next: the agent orchestrator's loop text, tried in each harness with a test definition; then the first analysis definition in [analysis-offload-to-code](../analysis-offload-to-code/README.md).
- 2026-09-29: Codex found two gaps in the pre-implementation design; a test for each failed against the implementation before its fix. (1) Recovering a move re-ran any listed move whose source still had the recorded bytes, so a replacement output identical to an archived one could be archived again. The kept copy's path is unique, so an existing target now counts as the move having finished. (2) The dependency guard checked only pending consumers at the end of the step. A consumer reached through a wait on another job could be accepted against its producer's old output while the producer was pending, and an effect after its `wait` could run. The guard now runs in `agent()` when the second job of the pair is named, and covers accepted consumers. Residual limit, stated in the docstring: when an accepted consumer is named and waited on before its producer is named, anything the definition does between the two calls runs before the refusal. Tests 32 and 33; 153 tests.
- 2026-09-29: the agent orchestrator's loop text is drafted in [loop.md](./loop.md), against the shell's actual output lines. Next: try it in Claude Code and Codex with a test definition and real sub-agents, covering a clean run, a validator retry, a problem report, a repair, a stop, and a fresh session resuming a run.
- 2026-09-29: the harness trial kit is in [trial/](./trial/README.md): a definition with four scenarios (clean, retry, problem, stop), a setup script, and a plan with what to look for. Writing it showed that a worker was not told where its inputs are; the prompt frame now lists the declared inputs' absolute paths, outside the input state. A smoke trial of `clean` in this session passed; the real trials need a fresh session given only the loop text, in Claude Code and in Codex.
- 2026-09-29 (operator): a mechanical step and an effect are told apart by whether the step can be replayed, not by where it writes. An effect is a step that must run once, for either of two reasons: it changes the world outside the run, or its result cannot be reproduced. Freezing sources is split: resolving the revision is an effect, fetching the recorded commit's objects is a mechanical step. Only the vocabulary and the docstrings changed; `ctx.effect` already ignores where `do` writes.
- 2026-09-29: [the testing procedure](./trial/testing-procedure.md) commissions a tester for one harness. It fixes the two decisions the test serves, the result the operator receives, and the limits on the tester; it leaves to the tester how to obtain a fresh agent orchestrator, how to capture its tool calls, and which further cases to build. No trial has been run under it yet.
- 2026-09-29: the first series ran in Claude Code and in Codex, five cases each, once each. Both testers recommend the loop text as usable after changes, and neither saw an agent orchestrator do a job, read an output unasked, or edit an output. [The change list](./trial/changes.md) consolidates what both proposed with the amendments from the design conversation: 8 for the loop text, 5 for the core, 7 for the kit, all awaiting the operator's decision. [The testing procedure](./trial/testing-procedure.md) is revised with 10 findings about testing itself; testers now write to files of their own under `trial/observations/`. Nothing under test has been changed.
