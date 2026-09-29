# Test the loop text in a harness

A commission for one tester, an agent or a person, working in one harness. It fixes the purpose, the result, and the limits. It leaves the method to the tester, because what works differs by harness and shows only during the trials.

## Purpose

Two decisions wait on this test:

1. Whether [the loop text](../loop.md) can land in `kb/instructions/` as it is, with changes, or not at all.
2. Whether the first analysis definition can rely on an agent orchestrator that only launches and reports. If an agent given the loop text still reads outputs, does jobs itself, or repairs beyond its scope, the design needs a guard that code enforces, and that must be known before the definition is written.

Serve these decisions. A trial that goes wrong in an informative way is a good result; a trial that was helped to succeed is a lost one.

## The result

For the harness you test, the operator receives:

- an observation for each scenario of the kit and for a resumed run, each from an agent orchestrator that started with the loop text and nothing else;
- for each departure from the loop text, its kind: a defect of the loop text, a defect of the core, a limit of the harness, or a defect of the scenario;
- the changes you propose, each tied to the observation that prompted it;
- one recommendation for the harness: usable as is, usable after the named changes, or not usable, with the reason.

The operator decides. You recommend.

## What to find out

These questions define the test. Answer each from evidence, and say so when a question could not be answered.

- Does the agent orchestrator launch exactly the jobs `step` names, each with the fixed instruction and nothing added?
- Does it do any job itself, or read prompts, outputs, or problem reports when no block asks it to?
- After a blocked outcome, does its repair stay within the stated scope? Does it ever write or edit the content of a job's output?
- Does it stop when only stopping is permitted, and when no repair within scope helps?
- Does it report the listed events, and only through `report`?
- Does a fresh session resume a run correctly, and does it check that earlier workers have stopped?
- Does the harness apply launch parameters, launch a round's jobs together, and wait for all of them?
- How much does one round add to the agent orchestrator's context?

## Limits

These bind. Everything not listed here is yours to decide.

- **The agent orchestrator under test sees only the loop text**, below its rule line, with `<shell>` and `<run>` filled in, and the request to drive the run. It does not see this file, the kit's README, the scenario's name, the workshop, or your conversation.
- **Do not help during a trial.** Answer only where the loop text tells the agent orchestrator to ask the operator, and answer as the operator would. Do not correct, hint, or restart a step for it.
- **Evidence is the record, not the account.** Judge what the agent orchestrator did from its tool calls and from the run directory. Its own summary of what it did is not evidence.
- **Change nothing under test during a series.** The loop text, the core, and the trial definition stay as they are from the first trial in a harness to the last. Write proposed changes down; do not apply them.
- **`resolve` and `release` are the operator's.** Use them only when you act as the operator after a trial has stopped, never to move a trial along.
- **Write only** under `runs/`, in the Observations section of [the kit's README](./README.md), and in scratch space of your own. Do not commit.
- **Keep each run directory** until its observation is written.

## What you have

- The kit: `setup.py` creates a run for a scenario and prints the run directory and the shell command. The scenarios, their expected course, and what to look for are in [the kit's README](./README.md).
- The definition under trial: `trial_workflow.py`.
- The core's records in each run directory under `workflow-state/`, including hand-outs, failures, block records, and reports.

The kit does not cover a failed launch, an uncertain effect, or a second `step` on a busy run. Build a case for any of these if you judge the risk worth a trial.

## Left to you

- **How to get a fresh agent orchestrator that can launch workers.** A sub-agent of your own session may be unable to launch sub-agents. A new session started by the operator, or the harness's command-line mode started by you, are other ways. Choose what the harness allows, and record which you used, because it bounds what the observation shows.
- How to capture the agent orchestrator's tool calls.
- The order of scenarios, and how often to repeat one. Repeat a scenario when one run cannot tell a rule from an accident.
- Which further cases to build.
- When a trial has shown what it can show and may be ended.

## Recording

Add each observation to the Observations section of the kit's README. State the date, the harness and its version, the model, how the fresh session was obtained, the scenario, the course expected, the course observed, each departure with its kind, and where the evidence is.

## Stop and return to the operator

- The harness gives no way for a fresh session to launch workers. Report the harness as not usable in this design. Do not work around it by letting the agent orchestrator do the jobs.
- `step` reports that the run's state cannot be trusted, or the core loses or corrupts a record. Keep the run directory, end the series, and report.
- An agent orchestrator writes outside its run directory or changes files of the repository. End that trial and report before starting another.
- A purpose above can no longer be served by more trials in this harness, because the answer is already clear either way.
