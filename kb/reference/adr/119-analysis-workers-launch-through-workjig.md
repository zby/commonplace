---
description: "Analysis workers launch through Workjig, the runtime extracted from the headless port: Commonplace keeps every launch decision, attempt count and verdict; Workjig keeps the durable launch record; the replayed step program is not pursued"
type: reference/types/adr.md
status: accepted
---

# 119 — Analysis workers launch through Workjig

**Status:** accepted
**Date:** 2026-10-21
**Amends:** [ADR 118](./118-analyses-run-as-a-workflow-over-headless-harnesses.md): the launch, relaunch, usage-limit and interruption rules below replace the corresponding parts of "An attempt is a recorded execution of a job" and the declined durable launch ownership; the workflow as one process, the plan as role data, checks applied in code, the pinned worktree and the other declined requirements are unchanged.

## Context

ADR 118 made a worker a subprocess launch owned by one Python process and
left the launch mechanics in `commonplace.headless`: fresh output
directories per launch, backoff, a problem file read beside an exit
status, usage-limit detection by substring, and an answer cache keyed by
content. None of that is about analyses. On 2026-10-19 the operator had
the base extracted as a standalone package with no Commonplace imports,
with the sibling project Treadle as its predecessor; the extraction became
Workjig, released on PyPI as 0.1.0 on 2026-10-20. Keeping a second copy
of the mechanics in this tree would mean two implementations of one
result protocol, tested twice and drifting.

Two forces decide what the base is, and would recur if this were
reverted. The workflow stays ordinary Python that calls workers and makes
control-flow decisions from their results, so the runtime must journal
results, not control position
([the practical scheduler is the host language](../../theory/the-practical-scheduler-is-the-host-language.md)).
And a durable result must not promise more than it can: a key over the
prompt, the inputs and the profile cannot show that ambient files, tools
or configuration stayed unchanged, so results are scoped to one run in one
prepared worktree and the caller keeps that environment pinned.

## Decision

**Workjig is the runtime under the workflow.** `workjig>=0.1.0` is a
runtime dependency installed from PyPI and pinned by `uv.lock`, so
prepared worktrees install the same runtime wherever they live.
`commonplace.headless` is a consumer layer: it turns a worker profile
into a Workjig command worker with the harness's machine-readable output,
reads the served model from each launch's retained output, and keeps
`ask`, `checked`, `accept`, `log` and `gather` over `workjig.Run`. A
run's records live under its `calls/`.

**Commonplace keeps every launch decision.** Each request is one Workjig
call named after its job. `ask` grants one launch at a time by raising
the call's launch ceiling, so the attempt count stays in Commonplace: a
rerun walks the recorded launches and counts them again, and a rerun
after a usage limit approves the recorded stop. Only a call that cannot
launch again, after a dismissed answer or a malformed problem file,
continues under the next identity, `<job>#1`. `gather` stays, since
parallel rounds run checks and corrections, not single requests. This
rests on Workjig's separation of execution controls from work identity.

**A launch is reserved durably.** Workjig records a launch before it
starts, and a run whose controller stopped with a launch unsettled does
not resume until the operator acknowledges that the old worker stopped:
`commonplace-analysis acknowledge <run> <launch>`. This replaces ADR
118's rule that a kill between a launch and its record leaves the work
unrecorded and repeated. `commonplace-analysis retry <run> <job> [--key]`
dismisses a worker problem or one answer, replacing deletion of a cache
file; the next `run` asks that job again without spending an attempt.

**Three launch rules change.** Relaunches after a nonzero exit wait 30
seconds each, not 30 then 120. A problem file written by a failing launch
is that launch's result: Workjig reads the problem before the exit
status, where the old layer relaunched and kept the problem as evidence.
A usage limit is read from the harness's terminal event or a
`usage_limit` problem, no longer from a substring of either stream.

**Inline paths are the caller's responsibility.** Workjig writes the task
verbatim and lists the input and output paths in a frame below it, minted
per launch. The `name = value` lines of ADR 117 refer to inputs by name
and let the frame resolve them; no Workjig change was requested.

## Considered alternatives

**Keep the launch mechanics in this tree.** Lost on duplication: the
extraction's acceptance cases (a failed launch leaving partial outputs
that a retry cannot inherit, explicit outcomes for missing outputs and
exhausted budgets after a restart, the concurrency bound, opposite
completion orders of sibling outputs) belong with the mechanics, and
Commonplace would carry them a second time.

**Let Workjig own retries under its policy.** The attempt count and ADR
108's budgets would move into the runtime. Raising the ceiling one launch
at a time is what lets Workjig's retry policy and Commonplace's budgets
coexist with every launch decision in the workflow.

**A replayed step program as the standalone module.** Explored in the
step-program demo (2026-10-14): an ordinary function replayed from the
top on every step, with computed jobs and external jobs memoized by
content, so an edited job misses, an unedited one hits, and the issued
prompts form the task queue; in build-system terms a monadic build with
constructive traces and a restarting scheduler, the agent being the
executor. It was not extracted. The direct-harness base needs no replay:
the workflow is one process whose call stack is the schedule, and Workjig
journals results under content keys with the same tolerance of edits. The
demo's unbuilt parts, a worker reporting failure or refusal, recording
which worker and model answered, and locking between a step and a fill,
are what Workjig's result protocol and durable reservation supply. Its
pairing with a job queue stays undecided and unneeded: no consumer has
workers pulling from a queue. The demo was deleted with its workshop and
is recoverable from git history.

**Escalating backoff in Workjig.** Not requested. Ask only if a
production run shows a relaunch where the delay mattered.

**Decline the stronger recovery guarantee, as ADR 118 did.** ADR 118
declined durable launch ownership as the engine's open-attempt machinery
returning. Workjig's reservation is one record per launch and one
acknowledgement per unsettled launch, not readiness state, and the exact
attempt count it buys serves Commonplace too. The earlier decline is
narrowed, not reversed.

## Consequences

The workflow module consumes `commonplace.headless` as before. The
analysis skill and the command reference bind the operator to `retry`
and `acknowledge`. uv consumes the dependency and the lock;
`pyproject.toml` exempts Workjig from the lock's seven-day
`exclude-newer` window, and a user-level uv config with its own window
needs `--exclude-newer-package workjig=false` on `uv tool install` until
a release is a week old. `INSTALL.md` needs no step. Consumer tests that
only exercised launch mechanics moved to Workjig's acceptance suite; the
fake-harness suites keep ADR 118's behavioural assertions. Commonplace
documentation may now name Workjig; the reservation that held until the
port landed is lifted.

Evidence. One production run on the production profile,
`AAS-2026-10-20-dynamic-cheatsheet-523b6948294d-01` (pi-sol, method
`14fa721`), against the ADR 118 pilot
`AAS-2026-10-19-dynamic-cheatsheet-2390eec63b75-01`: 11 launches each,
no failures or corrections, 37:26 against 39:56 wall; classifications
and consequential claims agree, and the differences are of the kind the
pilot showed against the engine runs (`kb/log.md`, 2026-10-20). One
tiny ask through each real harness (Claude Code, Pi, Codex) delivered
and recorded the served model. Workjig's own decision records hold the
runtime's reasoning; this record keeps what Commonplace decided.

Limits. One run per route, operational context rather than a controlled
trial. The production run exercised no relaunch, usage stop, `retry` or
`acknowledge`; those rest on the fake-harness suites and Workjig's
acceptance tests. Claude and Codex are supported by the tiny asks and
the suites, not by a production run. The port follows Workjig's main
branch; a release that changes the result protocol is a new decision.
The ADR 118 pilot stays published in its worktree and not integrated,
independently of this decision.
