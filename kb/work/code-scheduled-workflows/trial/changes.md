# Changes proposed from the trials

One list of every change proposed so far to the loop text, the core, the kit, and the way of testing. Each entry names where it came from, a recommendation, and the operator's decision. The operator decides; an entry marked open has no decision yet.

On 2026-09-29 the operator accepted every recommendation then listed. "Applied" below means the change is made; "declined" means the recommendation was to leave things as they are.

Maintained by the session that holds the workshop, not by testers. A tester proposes changes in an observation file and refers to entries here by their label.

Sources: the two series and their follow-up audits in [the kit's README](./README.md#observations), both of 2026-09-29, and the design conversation of the same day. "Claude" and "Codex" below name those series.

## Loop text

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| L1 | Resume: if you did not start this run in this session, ask the operator before the first `step` whether earlier workers have stopped. If you cannot ask, stop. | Claude resume did not ask; Codex 05 asked. The present rule applies "if you cannot tell", and a fresh session acted as if it could. | Accept. An unattended session then cannot resume a run. | Applied, with one addition: the run also counts as new when the operator says so. Without it an agent orchestrator would ask before the first step of every run it did not create, which includes every trial. |
| L2 | Stopping: give the operator the output of the last `step` unchanged. | Claude stop summarised it and lost the record path; Codex 04 reproduced it. | Accept. | Applied. |
| L3 | Waiting: do not run `step` until every worker of the round has finished or failed to start, however the harness reports that. Name no mechanism. | Claude retry launched workers in the background and ended its turn to wait. | Accept. | Applied. |
| L4 | Commentary: allow one short remark per round; do not repeat or summarize workers' replies; state that an event reaches disk only through `report`. | Codex 02 and 03, and Claude retry, narrated progress. The loop text is silent on it. | Accept. | Applied. |
| L5 | Stop report: name the job when a block on a job caused the stop. | Claude follow-up: the stop report has no job, so the core's records do not tie it to `assumptions`. | Accept. Low priority. | Applied. |
| L6 | Resume: say that a job handed out before the interruption may come back as a retry that reports "no output". | Codex follow-up: the resumed reconcile prompt carried a refusal for a worker that never ran. | Accept, as the wording that goes with C3. | Applied. |
| L7 | Repair: say "move" where the repair is a move. | Claude problem copied the file; Codex 03 moved it. | Decline. Both are within scope and neither writes content. See K1. | Declined. |
| L8 | Waiting: use the wait durations the harness supports. | Codex follow-up: two waits of 1,000 ms were raised to the harness's minimum. | Decline. The loop text names no harness, and the run was not affected. | Declined. |
| L9 | When `step` ends in a way the loop text does not name, such as a status other than 0 or 1 or no outcome line, run it once more; if it ends that way again, stop and tell the operator. | Found while building the `uncertain` case: the step in which an effect ends the process prints no outcome, and the loop text has no rule for it. Running `step` again is safe, because a step replays from the run's records. | Accept. Revised after the second series: decline, and replace with L10. | Declined (operator, 2026-09-29). |
| L10 | When `step` ends in a way the loop text does not name, stop: report the stop and give the operator the exit status and what `step` printed. Do not run `step` again. | Second series, both harnesses: at status 9 each stopped and did not run `step` again, which is safe; Codex's final message gave only the standard-error line. A `step` that crashed should reach the operator before it is run again. | Accept. | Applied. |
| L11 | Blocks: at a block, read the record and find the cause; the run directory may be listed; do not open prompt files, inputs, or outputs. A problem report is already quoted in the record. | Claude second series (P-new-1): at repair blocks the orchestrator also read the prompt, the source, and once an output. Codex read only the record and listed the run, leaving out outputs and `workflow-state/`. | Accept the narrow rule; Codex shows it can be followed. | Applied (operator, 2026-09-29). |
| L12 | Failed launch: "Do not relaunch in this round; when the next `step` names the job again, launch it then." | Claude second series (P-new-2), cb-07: it read "do not relaunch" as never, and reported a failed launch it had not tried. Codex relaunched as intended. | Accept. | Applied. |

## Core

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| C1 | Prompt frame: ask every worker to reply in one line, not only a worker that cannot finish. | Smoke trial; Claude context per round: replies of about 1.4 KB each. | Accept. The frame is outside the input state, so no accepted job reopens. | Applied. |
| C2 | Rename the record field `repairs`, which counts blocks since the last acceptance or release, not repairs made. | Claude follow-up: `repairs: 1` on a job that nobody repaired. | Accept. Low priority. | Applied: the field is `blocks_toward_limit`, and the record format is 2. A run directory written before the change is refused as untrusted state. |
| C3 | A hand-out whose worker was never launched counts as a failed attempt when the run resumes. Decide whether to keep this. | Codex follow-up: resume used up one attempt. Code cannot tell a worker that was never launched from one that wrote nothing. | Keep the behaviour, state it (L6), and test repeated interruption (K7). Two interruptions at this point would block the job. | Keep: two hand-outs without an output block the job, whatever the cause (operator, 2026-09-29). |
| C4 | Add a test of an effect that writes only inside the run directory, with the recognizer that checks for its file. | Design conversation: the definition of an effect now covers results that cannot be reproduced; the only test effect publishes outside the run. | Accept. | Applied: two tests. |
| C5 | Correct the test section heading "Steps with effects outside the run directory". | Same. | Accept. | Applied. |
| C6 | A block record names where each kept file now is, not only the directory it went to. | Claude second series: the record said a problem report "is moved under …/kept/", the kept name has a number prefix, and the orchestrator's read of the path it built failed twice. | Accept. | Applied, with a test. |

## Kit

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| K1 | `problem`: expect the file to be moved or copied. | Claude problem; L7. | Accept. | Applied. |
| K2 | `stop`: expect the block after two refusals, or after one refusal and a worker's problem report. | Codex 04: the second worker reported the contradiction. | Accept. | Applied. |
| K3 | `retry`: drop "without comment" from what to look for. | Codex 02. The loop text has no such rule until L4 is decided. | Accept. | Applied. |
| K4 | Add a case that reaches a block permitting only stopping. | Neither series reached one; both stopped at a block that still permitted repair. | Accept. A definition with a repair limit of zero reaches it at the first block. | Applied: scenario `stop-only`. |
| K5 | Add a case whose jobs carry launch parameters. | Both series: the kit sets none, so whether a harness applies them is unknown. | Accept. | Applied: scenario `parameters`, with `--launch` in setup. |
| K6 | `setup.py`: give a run a name that does not contain the scenario, when the tester passes none. | Claude runs were named `claude-stop`, `claude-retry` and so on, and the agent orchestrator saw the path. The Codex runs were numbered. | Accept. It also qualifies the Claude observations: the path may have cued the behaviour, most of all in `stop`. | Applied: a random name when none is given, and a name that contains a scenario's name is refused. |
| K7 | Add cases for a failed launch, an uncertain effect, a second `step` on a busy run, and a session interrupted more than once before a worker's launch. | Both series list these as not tested. | Accept, in the order the second series finds most useful. | Applied: scenarios `uncertain` and `busy`; a failed launch and a repeated interruption are cases of the tester's making, described in the kit's README. |
| K8 | Expectations: `uncertain` stops at the status 9 (L10); `problem` reads only the record at the block (L11); a failed launch is relaunched when the next `step` names the job (L12); cut a session for a resume by killing its process, not by a turn limit. | Claude second series (P-new-3, cb-11); the Codex retest's traces. | Accept. | Applied. |

## Testing

All entries here are applied in the revision of [the testing procedure](./testing-procedure.md) of 2026-09-29.

| Label | Change | Source |
|---|---|---|
| P1 | Each tester writes to a file of its own under `observations/`, not to the kit's README. | Two testers edited the README at once. |
| P2 | The run path must not name the scenario. | K6. |
| P3 | Keep out the instructions the harness loads by itself, and record what still loaded. | Claude: the user's own instructions may have loaded. Codex switched project documents off. |
| P4 | A resume is shown only by a session that can receive an answer. | Claude: the command-line mode cannot ask the operator. |
| P5 | Say where a session was cut. | Codex follow-up; C3. |
| P6 | Keep the workers' traces beside the agent orchestrator's. | Codex follow-up found them in the harness's session store. |
| P7 | Where the harness hides the instruction a worker received, leave the question unanswered and say so. | Codex: the instruction is encrypted in every record, the workers' included. No way around it is known. |
| P8 | Search the traces for failures that were recovered, and compare the core's records with the traces. | Both follow-up audits. |
| P9 | Record the hashes of the loop text, the core and the trial definition before and after a series. | Codex did so. |
| P10 | Read the change list before testing, and mark each proposal as new or as support for a listed entry. | The two series proposed overlapping changes. |
| P11 | Cut a session by killing its process when the core's state shows the hand-out; a turn limit may not cut a session whose workers run in the background. | Claude second series, cb-11. |

## Not yet shown by any trial

The kit has a case for each of the first three lines. None has run with an agent; each was driven once by hand, without a model, to check its course.

- A block that permits only stopping (K4).
- Launch parameters (K5).
- A failed launch, an uncertain effect, a busy run, repeated interruption (K7).
- The loop text with L10 to L12. The second series of each harness ran on L1 to L6 only.
- The instruction delivered to workers in Codex (P7).
- Any case more than once, or on a second model. Every case ran once per harness, on `claude-sonnet-5-5` and on `gpt-6-astra`.
