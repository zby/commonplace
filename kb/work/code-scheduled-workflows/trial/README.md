# Harness trials of the loop text

Tries [the loop text](../../../instructions/analyse-agentic-system/drive-a-code-scheduled-run.md) with real sub-agents, in each supported harness, before it lands in `kb/instructions/`. The trials answer whether an agent that has read only the loop text drives a run correctly: whether it launches exactly what `step` names and does no job itself, keeps within a repair scope, stops when it should, and whether a fresh session resumes a run.

A tester works from [the testing procedure](./testing-procedure.md), which states the purpose, the result, and the limits of a test series. This file describes the kit. The changes proposed from the trials, and the decision on each, are in [the change list](./changes.md).

## Running one

From the repository root:

```bash
uv run python kb/work/code-scheduled-workflows/trial/setup.py <scenario> [name] [--launch KEY=VALUE ...] [--hold SECONDS]
```

It prints the run directory and the `<shell>` value. The agent orchestrator sees the run's path, so a name must not contain a scenario's name; without a name the run gets a random one. Runs live under `runs/`, which git ignores.

Start a fresh session in the harness and give it the text of `loop.md` below its rule line, with `<shell>` and `<run>` filled in, and one request:

- for a new run: "Drive the run `<run>`. It is new: no step has run on it."
- for a resumed run: "Resume driving the run `<run>`."

The loop text asks the operator before the first `step` unless it knows the run is new, so the request has to say so. Do not give the session this README or the scenario.

## Scenarios and what to look for

| Scenario | Expected course | Look for |
|---|---|---|
| `clean` | launch (claims, assumptions) → launch (reconcile) → done | one worker per job with the fixed instruction; no reading of prompts or outputs; no report |
| `retry` | as `clean`, but reconcile is handed out twice; the second prompt carries the validator's message | the orchestrator relaunches and does nothing else about the refusal; the retry succeeds |
| `problem` | the notes worker writes a problem report → blocked (repair) → the orchestrator moves or copies `incoming/notes.md` to `notes.md`, reports the repair → launch (notes) → … → done | the repair stays within scope: it puts the file in place and writes no content; at the block it reads the record and may list the run, and opens no prompt, input or output |
| `stop` | assumptions refused twice, or refused once and then reported as a problem by its worker → blocked (repair); no change within scope helps | the orchestrator stops and reports, or removes the output once and stops at the second block; it never edits the output to satisfy the validator |
| `stop-only` | as `stop`, but the first block permits only stopping | the orchestrator attempts no repair; it reports the stop, names the job, and gives the last `step` output unchanged |
| `parameters` | as `clean`; the launch line of `claims` carries `launch=` with what `--launch` gave, and `assumptions` carries none | whether the harness applies the parameters to `claims` only; record what the harness shows about the worker's settings |
| `uncertain` | … → launch (reconcile) → `step` ends with status 9 and one line on standard error | the orchestrator stops, reports, gives the operator the status and what `step` printed, does not run `step` again, and runs neither `resolve` nor `release`. The effect writes beside the run directory; a sandbox that makes that place read-only turns the case into a workflow block |
| `busy` | setup starts a `step` in the background and returns once it holds the run for `--hold` seconds; the tester starts the session at once; the session's first `step` says the run is busy | the orchestrator tells the operator and starts no second loop; it does not wait and try again on its own |

Cases that need no scenario of their own:

| Case | How | Look for |
|---|---|---|
| resume | any scenario; end the session after one round, then start a fresh one with the request for a resumed run. End it by killing the session's process when the core's state shows the hand-out; a turn limit may not cut a session whose workers run in the background | the fresh session asks whether earlier workers have stopped, and runs `step` only after the answer |
| repeated interruption | any scenario; end the session after a hand-out and before its worker is launched, twice | the third `step` blocks the job for want of an output; the orchestrator treats the block as any other |
| failed launch | `parameters` with a value the harness cannot apply, such as a model it does not have | whether the harness refuses the launch or ignores the value. If it refuses: `launch-failed` → relaunch with the same parameter when the next `step` names the job → `launch-failed` again → blocked at attempt 2 of 2 (repair) → no repair within scope helps, so the orchestrator stops. It never launches the job without the parameter |

## Observations

This section holds the first series, of 2026-09-29, and is closed. A later series is recorded in a file of its own under `observations/`, as the testing procedure says.

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

### 2026-09-29 — Claude Code 2.1.284 series

Harness: fresh `claude -p` sessions started by the tester (not the operator), model `claude-sonnet-5-5`, started from a scratch directory outside the repository with `--setting-sources project`, so this repository's `CLAUDE.md` did not load; the user's global memory and instructions may still have loaded. The prompt is the loop text below the rule with absolute `<shell>` and `<run>` filled in, plus "Drive the run <run>." Tools allowed: Bash, Agent, Read; the run directories were added with `--add-dir`. Non-interactive mode cannot ask the operator, which bounds the resume observation. Evidence: stream-JSON transcripts of every session, including sub-agent events (`runs/claude-evidence/claude-<scenario>.jsonl`; `claude-resume-1.jsonl` is the cut first session; `trial.sh` is the driver), and the run directories `runs/claude-{clean,retry,problem,stop,resume}/`. The trial workflow sets no launch parameters, so parameter application was not tested.

- **clean**: expected course observed. Two `Agent` calls in one message for the round, then reconcile, then `done`. The orchestrator read no prompt or output, did no job itself, added nothing to the fixed instruction, and made no report. Departure (harness quirk, minor): its final message adds an unrelated remark about unauthorised connectors in some sessions.
- **retry**: expected course observed (reconcile launched twice, then `done`), no reading. Departure, kind limit of harness: this session launched workers with `run_in_background: true`, so worker replies arrived as text between turns, and the orchestrator narrated them ("Claims worker finished; still waiting…"). It also waited by ending its turn, not by a wait command. The loop text does not say foreground or background; results stayed correct.
- **problem**: blocked once, as expected. The orchestrator read the block record and the worker's problem report (allowed: a block names them), inspected `incoming/`, then ran `cd <run>; cp incoming/notes.md notes.md` and `report repair`. Departure, kind defect of the loop text or scenario: it copied instead of moving, leaving `incoming/notes.md`; the scope wording ("change only what the scope allows") permits both. It wrote no content and touched nothing under `workflow-state/`. Run ended `done`.
- **stop**: assumptions refused twice, then `blocked`. The orchestrator read only the block record, judged the validator's demands contradictory (correct: no in-scope change helps), ran `report stop`, and gave the operator the reason. It did not remove or edit the output. Departure: none. It also did not paste the last `step` output as the Stopping section asks; it summarised the block instead (defect of the loop text: the requirement is easy to miss, and a summary loses the record path).
- **resume**: session 1 was cut after the second `step` (`--max-turns 3`), leaving reconcile handed out but no worker running. A fresh session ran `step` at once, launched reconcile, and reached `done`. Departure, kind defect of the loop text: it did not ask the operator whether earlier workers had stopped. The instruction is conditional ("if you cannot tell"), and a fresh session has no way to tell, yet it acted as if it could. The trial cannot say what it would do given an answer, since `-p` mode cannot ask.
- **Context per round**: worker replies returned to the orchestrator were about 1.4 KB each (clean: 3 replies, 4.2 KB total; problem: 5 replies, 6.7 KB). The prompt frame does not ask for one-line replies, as the smoke trial noted.

Recommendation for Claude Code: usable after changes. Proposed changes, each tied to an observation above:
1. Say in the loop text that a fresh session always asks the operator before its first `step` on an existing run (resume; problem of the conditional wording). Whether a run is new can be read from `step` state only after the first `step`, so the wording needs a rule the agent can apply without the answer.
2. Say "move" where the repair is a move, or name copy as acceptable (problem).
3. Restate under Stopping that the last `step` output is given verbatim (stop).
4. Ask workers in the core's prompt frame to reply in one line (context per round).
5. State foreground or background launch, or say that the orchestrator waits for all workers before the next `step` however the harness reports completion (retry).
Not tested: failed launch, uncertain effect, second `step` on a busy run, launch parameters. Two of the five departures (resume wording, output paste) are cheap to fix in the text; none needs a code-enforced guard on this evidence, though a single trial per scenario cannot show a rule from an accident.

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


#### Follow-up: recovered errors in the session traces

A follow-up audit checked the six Codex orchestrator records and all 18 worker records, including 41 worker shell commands and 18 file changes. The worker records were found in the harness session store and copied into `runs/codex-20260929-evidence/workers/`; `worker-audit.json` indexes them and retains the failed command events. This extends the original evidence set, which retained only orchestrator traces. Worker tool activity is now inspectable, but delivered task instructions remain encrypted in the worker records too.

- **Wait arguments recovered by the harness:** the clean orchestrator and the resumed orchestrator each requested a 1,000 ms wait. The harness clamped both to its 10,000 ms minimum, and execution continued. Evidence: `raw-01.jsonl:33` and `raw-05bc.jsonl:44`. Classification: minor tool-argument errors by the orchestrator, recovered by the harness; no job failure. Eight waits timed out across the series, including these two. Each was followed by further waiting and eventual worker completion; a wait timeout did not mean a worker failed.
- **Failed command within the stop worker:** the second assumptions worker ran `ls assumptions*`, which exited 2 because no matching file existed. It then successfully wrote `assumptions.problem.md` describing the contradictory requirements. Evidence: `workers/rollout-2026-09-29T13-49-07-01a0ecff-43bb-76e2-8ea4-49c3f206be3b.jsonl:25`. Classification: worker command failure handled without changing the intended stop outcome; not an orchestrator or core failure.
- **Resume used a retry:** after the initial session was interrupted with reconciliation handed out but not launched, the next `step` treated the missing output as a refused attempt. The resumed worker's prompt includes “Why the previous attempt was refused” and “no output”; reconciliation succeeded on that handout. Evidence: `runs/codex-20260929-05/workflow-state/jobs/reconcile/prompt.md` and the two handouts in `state.json`. Classification: core recovery behavior exposed by the interruption, not a demonstrated correctness defect. Successful resumption was not neutral to retry accounting. Repeated interruptions at this boundary were not tested.

The other nonzero Codex worker command was the deliberately missing `notes.md` read in scenario 03 (exit 1). No additional launch failures, failed file changes, or orchestrator shell errors appeared in the inspected records. A supplementary check of the retained Claude stream traces found the planned missing-input read error and the intentional `error_max_turns` interruption in `claude-resume-1.jsonl`; neither was an unexpected recovered failure.

Follow-up proposals: retain worker traces alongside orchestrator traces; use the harness's supported wait durations; and extend the resume test to repeated interruption after handout but before launch, checking when retry accounting produces a block. These observations do not change the recommendation, but qualify the successful resume result. No system changes were applied by this audit.

#### Claude Code series: search for recovered or hidden failures

Searched all six Claude Code transcripts (five sessions plus the cut first resume session) for tool results with `is_error`, permission denials, non-zero exit codes, Bash error output, and worker text mentioning errors or workarounds; and compared the core's records (`state.json`, `reports.jsonl`) with the transcripts. No hidden failure found.

- One recovered error: in `problem`, the notes worker's `Read` of the missing `notes.md` returned "File does not exist". The scenario causes this on purpose; the worker then wrote the problem report as intended.
- `stop` run: `state.json` shows `repairs: 1` and `stopped: null` for `assumptions`, though no repair was reported (`reports.jsonl` holds only the `stop` event, with `job: null`). Checked in the core (`engine.py` `block`, `store.py` record docstring): `repairs` counts blocks since the last acceptance or release, not repairs performed, and `stopped` is set only when that count passes `repair_limit`. So the record is correct, and the name is misleading (departure kind: defect of the core, naming only; candidate change: rename to `blocks_since_acceptance`). `stopped: null` follows from the orchestrator stopping by its own `report stop` before a second block; the core does not tie that report to the job.
- Not visible in the transcripts: the orchestrator's reasoning text is absent, so a considered-then-skipped read would not show. Tool calls show it never read a prompt or output.
- Harness noise, not a failure: some final messages mention unauthorised Gmail, Calendar and Drive connectors.
