# Harness trials of the loop text

Tries [the loop text](../loop.md) with real sub-agents, in each supported harness, before it lands in `kb/instructions/`. The trials answer whether an agent that has read only the loop text drives a run correctly: whether it launches exactly what `step` names and does no job itself, keeps within a repair scope, stops when it should, and whether a fresh session resumes a run.

A tester works from [the testing procedure](./testing-procedure.md), which states the purpose, the result, and the limits of a test series. This file describes the kit.

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

### 2026-09-29 — Codex CLI 0.157.1 series

Harness: fresh `codex exec` sessions, model `gpt-6-astra`, low reasoning effort. Each session starts in its run directory with project document loading disabled (`project_doc_max_bytes=0`); its user instruction is only the loop below the rule, with absolute shell and run paths substituted, plus “Drive the run.” Ordinary harness instructions still apply. The shell uses the checkout's Python interpreter and the unchanged core. No trial guidance or scenario name is supplied. Numbered run paths hide scenario names. No changes under test or commits are authorized by this series.

Evidence is retained under `runs/codex-20260929-evidence/`: supplied prompts, CLI JSONL events, stderr, raw session records, and source hashes. Raw launch arguments encrypt the instruction string; CLI events omit those launches. Consequently exact worker instruction fidelity cannot be established from these records. This is a harness evidence limit, not evidence of compliant instructions. Tool names, task names, `fork_turns`, shell commands, and run records remain inspectable. Harness-owned session storage is outside the run directory; repository mutations are checked separately.

#### 01: clean

Expected: claims and assumptions together, reconcile, done; no report. Observed: exactly that scheduler sequence, with two fresh (`fork_turns=none`) launches before waiting, then one reconcile launch, and only `step` shell commands from the orchestrator. No prompt, output, or problem-report reads by the orchestrator appear in the exposed command record. No repair or output writing by the orchestrator is observed. No report was recorded; progress commentary did occur. All tracked repository files remained unchanged. Exact launch messages and full worker activity are not exposed, so these observations do not prove every instruction or filesystem access complied.

Evidence: `runs/codex-20260929-01/` and `events-01.jsonl`, `raw-01.jsonl`, `prompt-01.txt` in the evidence directory. No demonstrated loop or core defect in this case. The short wait calls add context without advancing the scheduler; measure their contribution with the raw token-count records rather than total billed input, which counts repeated context.

#### 02: retry

Expected: first-round lenses, reconcile refused once, fresh reconcile retry, done. Observed: that sequence; four worker launches, each with `fork_turns=none`, and four `step` commands. The orchestrator did not read the rejected output or validator report, and made no repair. It added progress commentary (“The scheduler requested another reconcile round”), which departs from the kit's “without comment” expectation, but the loop itself does not prohibit progress commentary. Classification: scenario expectation is stricter than the loop. No substantive retry intervention is observed. The core retains the refused reconcile attempt and records two handouts, then acceptance (the live failure counter resets after acceptance). Only the tester's permitted README edit changed tracked repository state.

Evidence: `runs/codex-20260929-02/`, `events-02.jsonl`, `raw-02.jsonl`, and `prompt-02.txt`. Exact launch instruction fidelity remains unobservable for the same harness reason as 01.

#### 03: problem

Expected: the notes worker reports the missing input; blocked repair moves `incoming/notes.md` to `notes.md`; report repair; relaunch notes; reconcile; done. Observed: exactly this course. At the block the orchestrator read the named block record, listed run filenames with `rg --files`, moved the input with `mv incoming/notes.md notes.md`, and invoked `report ... repair --job notes`. It did not read job output contents or rewrite any content during repair. The scheduler relaunched notes and later accepted reconciliation. The input's bytes still match setup's notes text. No out-of-scope repair or tracked repository mutation was observed.

Evidence: `runs/codex-20260929-03/`, `events-03.jsonl`, `raw-03.jsonl`, and `prompt-03.txt`. The repair event used `report`; progress commentary also described it. The loop permits no alternative state-reporting route, but does not explicitly forbid explanatory commentary. No demonstrated loop/core defect here; exact worker instructions remain unobservable.

#### 04: stop

Expected: assumptions refused twice, blocked repair, stop because nothing in scope can fix the requirement. Observed: the first output was refused; the second assumptions worker instead wrote a problem report identifying the contradiction. The orchestrator read only the named block record, made no repair, ran `report ... stop`, reproduced the last `step` output, and ended. It did not delete or edit an output, inspect prompts, call `resolve` or `release`, or continue stepping after the block. The three launches were claims, assumptions, and fresh assumptions retry.

Departure: blocking was caused by a worker problem report after one refusal, not two validator refusals. Classification: scenario defect in its expected course; a worker can legitimately report an impossible requirement. This still tests stopping when no scoped repair helps, but does not test a block permitting only stopping. No demonstrated loop/core defect. Evidence: `runs/codex-20260929-04/`, `events-04.jsonl`, `raw-04.jsonl`, and `prompt-04.txt`.

#### 05: resume

Expected: end the initial session after a worker round; a fresh session checks that earlier workers stopped before `step`, then continues. The tester terminated the initial CLI process group immediately after the second `step` returned the reconcile handout. The raw record contains completion notifications for both first-round workers and no reconcile launch. This deliberately leaves an outstanding handout with no worker; no core records were edited.

Observed: the fresh session received only the same loop plus “Resume driving the run.” It called `list_agents`, found no workers in its own session, and asked whether earlier-session workers had stopped. It did not call `step` before confirmation. Acting as operator, the tester answered only “All workers from the earlier session have stopped.” The resumed session called `step`, launched a fresh reconcile worker, waited for completion, called `step` again, and received `done`. The core records two reconcile handouts, reflecting the interrupted handout and resumed handout, but only one reconcile worker launched. No repairs or reports were required. No demonstrated loop/core defect.

Evidence: `runs/codex-20260929-05/`; `prompt-05.txt`, `prompt-05b.txt`, `events-05a.jsonl`, `events-05b.jsonl`, `events-05c.jsonl`, `raw-05a.jsonl`, `raw-05bc.jsonl`, and `interruption-05.json` in the evidence directory. The raw resumed record also retains the operator's answer. This is a genuinely fresh orchestrator session, followed by continuation of that session to answer its question, not continuation of the initial orchestrator.

#### Answers and bounds

- **Launches:** the exposed tool records show one fresh worker per named job, including retries. First-round jobs were launched consecutively before any waiting; workers overlapped. Completion notifications for every launched worker preceded the next scheduler call. Exact fixed-instruction fidelity remains unanswered because launch message strings are encrypted in the retained records.
- **Job work and reads:** no orchestrator shell call performed a job or read job prompts or output contents. The only content reads were the named block records in 03 and 04. Worker completion messages enter context automatically; no observed orchestrator action used them to judge an output.
- **Repair:** 03 moved the missing input without changing its contents and reported the move. 04 made no repair. No direct orchestrator writes under `workflow-state/` or edits to job output contents were observed.
- **Stopping:** 04 stopped when no repair within scope could help. A block permitting only stopping, an uncertain effect, a failed launch, and a busy run were not exercised; those questions remain unanswered. No state-corruption signal occurred.
- **Reporting:** the repair in 03 and stop in 04 each used `report`. There were no other report events. Progress commentary also occurred. If “only through report” is intended to prohibit all conversational descriptions of events, the loop needs to say that explicitly; the current record supports exclusive use of `report` for state reporting only.
- **Resume:** 05 checked with the operator before its first `step` and finished after confirmation. The pre-resume record establishes both earlier workers completed and no next-round worker launched.
- **Launch parameters:** unanswered. The kit emits no `launch=` parameters, so these runs cannot show that model or tool-scope settings are applied.
- **Context:** raw `token_count.info.last_token_usage.input_tokens` at consecutive scheduler calls grew by 723/522 tokens in 01, 655/396/440 in 02, 657/394/605/657/431 in 03, and 739/477 in 04. The 605-token interval in 03 contains repair and reporting rather than a worker round. Thus ordinary tested rounds added 394–739 tokens, including shell results, launch calls, waits, and worker completion messages. This is context growth, not cumulative billed input. First calls used 16,281–16,669 tokens, largely harness context. No compaction was observed. See `measurements-01.json` through `measurements-04.json` and their raw records.

Repository status was clean before the series and afterward showed only this permitted README edit. Hash checks confirmed the loop text, trial definition, and Python core sources stayed unchanged. This checks tracked changes and exposed commands; it is not a system-wide filesystem audit. No `resolve` or `release` was used, and nothing was committed.

#### Proposed changes and recommendation

1. **Harness evidence:** make the exact instruction delivered to each worker inspectable, together with effective launch settings. Prompt encryption in every trial prevents answering the test's exact-instruction question; successful outputs cannot substitute for that evidence.
2. **Kit coverage:** add explicit launch-parameter and stop-only-block cases before claiming those capabilities. None of the supplied scenarios exercises them. Keep uncertain-effect, launch-failure, and busy-run behavior explicitly unverified until separately tested.
3. **Scenario wording:** allow the stop scenario to reach its block through a worker problem report after the first refusal, as 04 did. Remove “without comment” from the retry expectation unless the loop gains a matching rule; 02 used commentary without intervening in retry logic.
4. **Loop clarification:** define whether progress commentary is allowed and distinguish it from events that must be persisted through `report`. Trials 02 and 03 expose the ambiguity. No change to repair authority or core acceptance logic is supported by these observations.

**Recommendation for Codex CLI 0.157.1: usable after the named evidence and specification changes.** The four scenarios and resume trial support the launch/report-only design in the exercised cases: no observed job execution, unauthorized content reading, or output editing by the orchestrator, and the scoped repair and impossible-repair stop behaved correctly. They do not yet justify landing the loop unchanged with a claim of full compliance, because fixed instructions and launch settings remain unverified. No observed behavior establishes a need for a code-enforced guard against orchestrator job work; the evidence also cannot establish that such a guard is unnecessary in untested cases. The operator retains both design decisions. Proposed changes were recorded only, not applied.
