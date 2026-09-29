---
description: "Use when acting as the agent orchestrator of a code-scheduled workflow run: run `step`, launch the jobs it names, handle blocks, and report events. The workflow's skill supplies the `<shell>` command and the run directory."
type: types/instruction.md
---

# Drive a code-scheduled run

Code decides what runs next and judges every result. You launch the workers it names and report what only you can see. Keep only the run directory; everything else is on disk.

`<shell>` below stands for `python -m commonplace.workflow.shell`; `<run>` is the run directory.

## Loop

Run `<shell> step <run>`. The first line of its output is the outcome.

**`launch`**: each following line names one job and its prompt file between backticks, sometimes followed by `launch=` and parameters.

1. For each job, launch one fresh sub-agent whose whole instruction is: ``Read `<prompt file>` and follow it.`` Apply every launch parameter, such as model or tool scope. If the harness cannot apply one, treat the launch as failed (step 3); never launch the job without it. Do not change the instruction, add context, or do a job yourself.
2. Launch all jobs of the round at once. Do not run `step` again until every worker of the round has finished or failed to start, however the harness tells you that.
3. If the harness refuses or fails a launch, run `<shell> report <run> launch-failed --job <name> --text "<what the harness said>"`. Do not relaunch in this round; when the next `step` names the job again, launch it then.
4. Run `step` again.

Do not read prompt files, outputs, or problem reports to check a worker's work, and do not act on a worker's reply. Code judges the output on the next step.

You may tell the operator in one short line which round you are in. Do not repeat or summarize what workers reply. An event is recorded only by `report`; telling the operator does not record it.

**`done`**: tell the operator the run is finished, and stop.

**`blocked`**: each block names a subject, a reason, a record file, and what is permitted.

- `permitted: repair within this scope: …` — read the record file and find the cause; you may list the run directory. Do not open prompt files, inputs, or outputs. Change only what the scope allows. Never write or edit the content of a job's output, never change anything under `workflow-state/`, and never try to get an output accepted by any other route. Then run `<shell> report <run> repair --job <subject> --text "<what you changed>"` and run `step` again. If no change within the scope fixes the cause, stop.
- `permitted: stop and report to the operator` — stop.

Handle every block of the outcome before running `step` again. If any block permits only stopping, stop.

**`uncertain`**: an effect may or may not have taken place. Stop.

## Stopping

Run `<shell> report <run> stop --text "<why, in one line>"`. If a block on a job caused the stop, add `--job <subject>`.

Then give the operator the output of the last `step` exactly as it was printed, not a summary. It holds the paths of the records the operator needs.

`resolve` and `release` are the operator's commands; do not run them.

## When the command itself fails

`step` exits with status 1 and a message on standard error:

- **the run is busy**: another `step` is running on this run. Do not start a second loop; tell the operator.
- **the run's state cannot be trusted**, or **not a run**: tell the operator. Do not repair anything under `workflow-state/`.

If `step` ends any other way, with another status or without an outcome line, do not run `step` again. Stop as the Stopping section says, and give the operator the exit status with everything `step` printed.

## Resuming

Before your first `step` in a session, settle whether the run is new. It is new if you started it yourself in this session, or if the operator told you that no step has run on it. Then run `step`.

Otherwise do not run `step` yet. Ask the operator whether every worker of the earlier session has stopped, and run `step` only after the operator says so. If you cannot ask, stop. A worker still running from an earlier session would write into a round it does not belong to.

After a resume, a job that was handed out before the interruption may come back as a retry whose prompt says the previous attempt wrote no output. This is expected: code cannot tell a worker that never ran from one that wrote nothing. Launch it as any other job. Two such hand-outs block the job.
