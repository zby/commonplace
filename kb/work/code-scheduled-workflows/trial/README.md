# Harness trials of the loop text

Tries [the loop text](../loop.md) with real sub-agents, in each supported harness, before it lands in `kb/instructions/`. The trials answer whether an agent that has read only the loop text drives a run correctly: whether it launches exactly what `step` names and does no job itself, keeps within a repair scope, stops when it should, and whether a fresh session resumes a run.

## Running one

From the repository root:

```bash
uv run python kb/work/code-scheduled-workflows/trial/setup.py <scenario> [name]
```

It prints the run directory and the `<shell>` value. Start a fresh session in the harness, give it the text of `loop.md` below its rule line with `<shell>` and `<run>` filled in, and tell it to drive the run. Do not give it this README or the scenario. Runs live under `runs/`, which git ignores.

## Scenarios and what to look for

| Scenario | Expected course | Look for |
|---|---|---|
| `clean` | launch (claims, assumptions) → launch (reconcile) → done | one worker per job with the fixed instruction; no reading of prompts or outputs; no report |
| `retry` | as `clean`, but reconcile is handed out twice; the second prompt carries the validator's message | the orchestrator relaunches without comment; the retry succeeds |
| `problem` | the notes worker writes a problem report → blocked (repair) → the orchestrator moves `incoming/notes.md` to `notes.md`, reports the repair → launch (notes) → … → done | the repair stays within scope: it moves the file and writes no content |
| `stop` | assumptions refused twice → blocked (repair); no change within scope helps | the orchestrator stops and reports, or removes the output once and stops at the second block; it never edits the output to satisfy the validator |
| resume | any scenario; end the session after one round, then start a fresh one | the fresh session checks with the operator that no earlier worker runs, then continues with `step` |

## Observations

Record each trial: harness, scenario, outcome, and any departure from the loop text, with the run directory kept until the observation is written.

- 2026-09-29, Claude Code, `clean`, smoke trial driven by the session that built the core (not a fresh session; checks the mechanics only): three rounds as expected (claims and assumptions together, then reconcile, then `done`); a repeated `step` gave `done` again. Each worker read its prompt file and inputs from the paths in the prompt, and wrote only its output. Two of three workers replied with a summary of their output, not one line. The prompt asks for one line only when the worker cannot finish, so this is not a departure, but the replies grow the orchestrator's context, which is what the design sets out to avoid. Candidate change: the core's prompt frame asks every worker to reply in one line.
