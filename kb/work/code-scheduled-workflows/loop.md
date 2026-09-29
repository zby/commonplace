# Draft: the agent orchestrator's loop text

Draft for trial in each supported harness. When the workshop closes, this text lands in `kb/instructions/`, or in the first workflow's skill if it is still the only one. Everything below the rule is the text an agent orchestrator receives.

---

# Drive a code-scheduled run

Code decides what runs next and judges every result. You launch the workers it names and report what only you can see. Keep only the run directory; everything else is on disk.

`<shell>` below stands for `python -m commonplace.workflow.shell`; `<run>` is the run directory.

## Loop

Run `<shell> step <run>`. The first line of its output is the outcome.

**`launch`**: each following line names one job and its prompt file between backticks, sometimes followed by `launch=` and parameters.

1. For each job, launch one fresh sub-agent whose whole instruction is: ``Read `<prompt file>` and follow it.`` Apply the launch parameters the harness can apply, such as model or tool scope. Do not change the instruction, add context, or do a job yourself.
2. Launch all jobs of the round at once, then wait until every worker has finished or failed to start.
3. If the harness refuses or fails a launch, run `<shell> report <run> launch-failed --job <name> --text "<what the harness said>"`. Do not relaunch; the next step names the job again.
4. Run `step` again.

Do not read prompt files, outputs, or problem reports to check a worker's work, and do not act on a worker's reply. Code judges the output on the next step.

**`done`**: tell the operator the run is finished, and stop.

**`blocked`**: each block names a subject, a reason, a record file, and what is permitted.

- `permitted: repair within this scope: …` — read the record file, find the cause, and change only what the scope allows. Never write or edit the content of a job's output, never change anything under `workflow-state/`, and never try to get an output accepted by any other route. Then run `<shell> report <run> repair --job <subject> --text "<what you changed>"` and run `step` again. If no change within the scope fixes the cause, stop.
- `permitted: stop and report to the operator` — stop.

Handle every block of the outcome before running `step` again. If any block permits only stopping, stop.

**`uncertain`**: an effect may or may not have taken place. Stop.

## Stopping

Run `<shell> report <run> stop --text "<why, in one line>"`, then give the operator the output of the last `step`. `resolve` and `release` are the operator's commands; do not run them.

## When the command itself fails

`step` exits with status 1 and a message on standard error:

- **the run is busy**: another `step` is running on this run. Do not start a second loop; tell the operator.
- **the run's state cannot be trusted**, or **not a run**: tell the operator. Do not repair anything under `workflow-state/`.

## Resuming

A fresh session resumes a run by running `step`, but only once the earlier session's workers have stopped. A worker still running from an earlier session would write into a round it does not belong to. If you cannot tell whether they have stopped, ask the operator before the first `step`.
