# Changes proposed from the trials

One list of every change proposed so far to the loop text, the core, the kit, and the way of testing. Each entry names where it came from, a recommendation, and the operator's decision. The operator decides; an entry marked open has no decision yet.

Maintained by the session that holds the workshop, not by testers. A tester proposes changes in an observation file and refers to entries here by their label.

Sources: the two series and their follow-up audits in [the kit's README](./README.md#observations), both of 2026-09-29, and the design conversation of the same day. "Claude" and "Codex" below name those series.

## Loop text

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| L1 | Resume: if you did not start this run in this session, ask the operator before the first `step` whether earlier workers have stopped. If you cannot ask, stop. | Claude resume did not ask; Codex 05 asked. The present rule applies "if you cannot tell", and a fresh session acted as if it could. | Accept. An unattended session then cannot resume a run. | open |
| L2 | Stopping: give the operator the output of the last `step` unchanged. | Claude stop summarised it and lost the record path; Codex 04 reproduced it. | Accept. | open |
| L3 | Waiting: do not run `step` until every worker of the round has finished or failed to start, however the harness reports that. Name no mechanism. | Claude retry launched workers in the background and ended its turn to wait. | Accept. | open |
| L4 | Commentary: allow one short remark per round; do not repeat or summarize workers' replies; state that an event reaches disk only through `report`. | Codex 02 and 03, and Claude retry, narrated progress. The loop text is silent on it. | Accept. | open |
| L5 | Stop report: name the job when a block on a job caused the stop. | Claude follow-up: the stop report has no job, so the core's records do not tie it to `assumptions`. | Accept. Low priority. | open |
| L6 | Resume: say that a job handed out before the interruption may come back as a retry that reports "no output". | Codex follow-up: the resumed reconcile prompt carried a refusal for a worker that never ran. | Accept, as the wording that goes with C3. | open |
| L7 | Repair: say "move" where the repair is a move. | Claude problem copied the file; Codex 03 moved it. | Decline. Both are within scope and neither writes content. See K1. | open |
| L8 | Waiting: use the wait durations the harness supports. | Codex follow-up: two waits of 1,000 ms were raised to the harness's minimum. | Decline. The loop text names no harness, and the run was not affected. | open |

## Core

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| C1 | Prompt frame: ask every worker to reply in one line, not only a worker that cannot finish. | Smoke trial; Claude context per round: replies of about 1.4 KB each. | Accept. The frame is outside the input state, so no accepted job reopens. | open |
| C2 | Rename the record field `repairs`, which counts blocks since the last acceptance or release, not repairs made. | Claude follow-up: `repairs: 1` on a job that nobody repaired. | Accept. Low priority. | open |
| C3 | A hand-out whose worker was never launched counts as a failed attempt when the run resumes. Decide whether to keep this. | Codex follow-up: resume used up one attempt. Code cannot tell a worker that was never launched from one that wrote nothing. | Keep the behaviour, state it (L6), and test repeated interruption (K7). Two interruptions at this point would block the job. | Keep: two hand-outs without an output block the job, whatever the cause (operator, 2026-09-29). |
| C4 | Add a test of an effect that writes only inside the run directory, with the recognizer that checks for its file. | Design conversation: the definition of an effect now covers results that cannot be reproduced; the only test effect publishes outside the run. | Accept. | open |
| C5 | Correct the test section heading "Steps with effects outside the run directory". | Same. | Accept. | open |

## Kit

| Label | Change | Source | Recommendation | Decision |
|---|---|---|---|---|
| K1 | `problem`: expect the file to be moved or copied. | Claude problem; L7. | Accept. | open |
| K2 | `stop`: expect the block after two refusals, or after one refusal and a worker's problem report. | Codex 04: the second worker reported the contradiction. | Accept. | open |
| K3 | `retry`: drop "without comment" from what to look for. | Codex 02. The loop text has no such rule until L4 is decided. | Accept. | open |
| K4 | Add a case that reaches a block permitting only stopping. | Neither series reached one; both stopped at a block that still permitted repair. | Accept. A definition with a repair limit of zero reaches it at the first block. | open |
| K5 | Add a case whose jobs carry launch parameters. | Both series: the kit sets none, so whether a harness applies them is unknown. | Accept. | open |
| K6 | `setup.py`: give a run a name that does not contain the scenario, when the tester passes none. | Claude runs were named `claude-stop`, `claude-retry` and so on, and the agent orchestrator saw the path. The Codex runs were numbered. | Accept. It also qualifies the Claude observations: the path may have cued the behaviour, most of all in `stop`. | open |
| K7 | Add cases for a failed launch, an uncertain effect, a second `step` on a busy run, and a session interrupted more than once before a worker's launch. | Both series list these as not tested. | Accept, in the order the second series finds most useful. | open |

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

## Not yet shown by any trial

- A block that permits only stopping (K4).
- Launch parameters (K5).
- A failed launch, an uncertain effect, a busy run, repeated interruption (K7).
- The instruction delivered to workers in Codex (P7).
- Any case more than once, or on a second model. Every case ran once per harness, on `claude-sonnet-5-5` and on `gpt-6-astra`.
