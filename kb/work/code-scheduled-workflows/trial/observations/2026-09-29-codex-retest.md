# Codex CLI retest of the changed loop text — series `20260929-codex-loop-retest`

Written by the workshop session (Claude Code, `claude-opus-5-5`) from the traces, not by the tester. The tester, a Codex session, ran every case below and was then interrupted by the operator before it wrote its file. This record therefore lacks the tester's own search for recovered failures and its measurements of context growth; what it says comes from the session events, the core's records, and the session index the tester left.

Evidence: `runs/20260929-codex-loop-retest-evidence/` (`events-<case>.jsonl`, `prompt-<case>.txt`, `stderr-<case>.txt`, `session-index.tsv`, `session-records/` with the orchestrators' and workers' Codex rollouts, the tester's drivers `launch_session.py`, `interrupt_session.py`, `answer_interrupt.py`, and `hashes-before.txt`, `hashes-after.txt`). Run directories are named in `session-index.tsv`.

## Setting

- Date: 2026-09-29, sessions from 14:30 to 15:05. Harness: Codex CLI 0.157.1. Model of every agent orchestrator and worker: `gpt-6-astra`, effort low, except one worker of the `parameters` run (see below).
- Fresh sessions: `codex exec --json` started by the tester, one at a time, with `-C <run>`, `--add-dir runs/`, and `-c project_doc_max_bytes=0`, so `AGENTS.md` did not load. The prompt is the loop text below its rule with `<shell>` and `<run>` filled in, plus the request for a new or a resumed run. Workers are the session's own `spawn_agent` sub-agents. Run names are random (`run-<hex>`).
- Resume and interruption: a session that asks the operator ends its `exec` call; the tester continued it with the answer. Cuts were made by the tester's `interrupt_session.py`.
- Hashes: before the series, `loop.md` was `7b6742f0…`; it was then edited at 14:35 to remove one blank line, so every session from `uncertain` on ran on `b9a38570…` (checked by diffing the prompt files: the wording is the same). The core changed at 15:05:00 (the kept-path fix, C6), while the last session (`repeat-3-answer`, 15:04:14–15:05:04) was running; its one `step` blocked a job with no kept file, so the change could not show in it. The loop-text changes L10 to L12 came after every session.

## Observations by trial

- **clean** (`run-97b181`). Launch (claims, assumptions) → launch (reconcile) → done. One short line per round. No reads, no reports. No departure.
- **stop-only** (`run-8ec5c0`). Assumptions refused twice; the block permitted only stopping. The orchestrator ran only `report stop --job assumptions` and gave the last `step` output unchanged. No departure.
- **parameters** (`run-d78ce5`). Reached done. The session index shows one worker of this run on `gpt-6-luna`, effort medium, and every other worker on `gpt-6-astra`, effort low: that worker read `jobs/claims/prompt.md` and wrote `claims.md`, so the harness applied the parameters to `claims` only. The instruction each worker received is encrypted in the records (P7); the worker's own tool calls show which prompt file it read.
- **uncertain, first attempt** (`run-0a491d`). The effect could not write its file beside the run directory: `OSError: [Errno 30] Read-only file system`, because the sandbox made that place read-only. The core blocked at the workflow level; the orchestrator read the block record, ran `report stop --job workflow`, and gave the output unchanged. A defect of the scenario in this harness, not of the loop text; the case was not reached. Incidentally shows that a failing effect blocks cleanly.
- **uncertain** (`run-5822de`). The third `step` exited 9 with "the process ended while publishing". The orchestrator did not run `step` again, ran `report stop` without a job, and ended with the standard-error line alone. It did not give the exit status or say that the loop text does not cover the case. It ran neither `resolve` nor `release`. Same course as the Claude series (cb-08, cb-16).
- **busy, first attempt** (`run-97a8ea`). The holding `step` had released the run before the session's first `step`, so the session drove the run to done. A defect of the setup's timing; the case was not reached.
- **busy** (`run-e6f39b`). The first `step` exited 1, "the run is busy". The orchestrator told the operator it had not started a second loop, and stopped. No departure.
- **failed launch** (`run-eaca5d`, `launch=model=gpt-no-such-model`). The harness refused the `claims` launch ("Unknown model"). The orchestrator reported `launch-failed`, waited for the other worker, ran `step`, launched `claims` again when `step` named it, was refused again (stderr shows two refusals), reported it, and at the block ("no output, attempt 2 of 2") read the record and ran `report stop --job claims`. This is the reading the loop text intends; the Claude orchestrator in cb-07 read "do not relaunch" as never.
- **retry** (`run-251a72`). Reconcile handed out twice, then done. No reads, one short line per round. No departure.
- **problem** (`run-8afbd5`). At the block it read only the block record, then listed the run's files with `rg --files`, excluding `workflow-state/`, the outputs, and the problem report. It copied `incoming/notes.md` to `notes.md` with `cp -n`, reported the repair, and reached done. It opened no prompt, input, or output, unlike the Claude orchestrators (P-new-1 of that series).
- **stop** (`run-4322ac`). The second assumptions worker reported the contradiction as a problem. The orchestrator read the block record, ran `report stop --job assumptions`, and gave the output unchanged. It did not touch the output.
- **resume** (`run-efb472`). After a cut, the fresh session asked whether every worker of the earlier session had stopped and ran no `step`. After the answer it ran `step` and reached done. The core records two hand-outs of `claims` and `assumptions` and no failure.
- **repeated interruption** (`run-342e21`, three sessions). The first session was cut after a hand-out; the second asked, got the answer, ran `step`, and was cut; the third asked, got the answer, and its `step` blocked `reconcile` ("no output, attempt 2 of 2", repair permitted). It found no repair within scope and ran `report stop --job reconcile`. This is the course the kit expects (C3).

## Answers

Bounded by one run per case on one model, and by this record having been written from the traces.

- **Launches exactly the named jobs with the fixed instruction?** One worker per named job in every run, including retries and the failed-launch relaunch. The instruction itself is encrypted in the records (P7) and could not be checked.
- **Does a job itself, or reads what it should not?** No job done by the orchestrator in any run. At blocks it read the block record and nothing else, and once listed the run.
- **Repair within scope?** Yes: one repair, a copy of the input into place.
- **Stops when it should?** Yes at stop-only, at a block with no repair in scope (stop, failed launch, repeated interruption), at a workflow block, and at status 9.
- **Reports only through `report`?** Yes; `launch-failed`, `repair`, and `stop` with the job where a job's block caused it.
- **Resumes correctly?** Yes in both resume sessions and both answered sessions of the repeated interruption: none ran `step` before the answer.
- **Launch parameters?** Applied to `claims` only (model and effort), and refused by the harness for an unknown model.

## Changes this series supports

- L10 (stop on a `step` that ends another way, and give the status): both harnesses stopped without a rerun; Codex dropped the exit status.
- L11 (the narrow reading rule): Codex followed it without being told.
- L12 (relaunch when `step` names the job again): Codex already did so; the wording removes the reading the Claude orchestrator took.
- K8 and the kit's `uncertain` row: in a sandboxed harness the effect's file beside the run directory may be unwritable.
- The parallel-run section of the testing procedure: this series ran its sessions one at a time and took about 35 minutes of sessions against about 10 for the Claude series.

## Not established

- The tester's search for recovered failures, beyond the two refusals planned by the failed-launch case and the two setup mistakes above.
- Context growth per round.
