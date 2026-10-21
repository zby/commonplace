---
description: "One process runs an analysis as a Python workflow over headless harness launches: the plan is role data, control flow is code, attempts are recorded executions cached by content, verdicts are applied in code; the artifact-run engine is retired"
type: reference/types/adr.md
status: accepted
---

# 118 — Analyses run as a workflow over headless harnesses

**Status:** accepted
**Date:** 2026-10-19
**Supersedes:** [ADR 113](./113-artifact-runs-execute-declared-plans-with-pinned-judgments.md): the engine, its plan model, the advance command, hand-outs, judgments, engine-derived coverage, the run-state layout and the core/consumer boundary. Role-scoped draft validation (`commonplace-validate <draft> --artifact <dir> --role <role>`) stays as decided there.
**Amends:** [ADR 117](./117-plans-derive-their-structural-jobs-from-the-type.md): the plan no longer expands into check and apply jobs, and nothing is a judgment input; the compact plan as method data, the verification protocol, the prompt composed from `name = value` lines and the prompt section, and the rule-ownership rules stay. [ADR 114](./114-directory-types-declare-what-a-role-verifies.md): a `verifies` relation is settled by code applying the verifying role's verdict to the subjects it was handed, not by a recorded judgment with a scope. [ADR 101](./101-open-analysis-runs-through-workflow-start.md): opening runs at the start of `commonplace-analysis run`, in the same process, before any worker. [ADR 106](./106-merge-analysis-publications-from-isolated-worktrees.md): the integration command is `commonplace-analysis integrate`; run identifiers and the guarded merge are unchanged.
**Amended by:** [ADR 119](./119-analysis-workers-launch-through-workjig.md) (2026-10-21): workers launch through Workjig; launches are reserved durably and acknowledged after an interruption, relaunches wait a fixed 30 seconds, a failing launch's problem file is its result, and usage limits are read from the harness's terminal event.

## Context

ADR 113 moved the analysis schedule from prose into an engine so that a
run would resume from disk and every verdict would name the versions it
rested on. It kept the coordinating agent: a conversation that called
`commonplace-run advance`, received hand-outs, launched a worker per
hand-out and reported the results. Everything the engine did served that
shape. With one execution thread a step program is simple: replay the
script and every model job is either recorded or the next one to hand out.
With several attempts open at once it is not: the shared run state needs
rules for which round an attempt belongs to, inputs that change while it
runs, results reported late or twice, and workers known to have stopped.
The engine's readiness rules, attempt closing, hand-out validation, run
lock and reset machinery existed to enforce them, and the operator's
checks of a harness had to cover nested coordination (`check-subagent-
harness`, two layers). The coordinator also loaded the origin checkout's
startup files, so `prepare` guarded the origin's startup files and refused
a HEAD behind `main`.

Every harness now has a headless mode that takes a prompt, runs a worker
to completion without interaction and returns: `claude -p`, `codex exec`
and `pi -p`. Phase 0 of the port (2026-10-18) found the unattended flags
each needs, how each reports a usage limit, and that each records the
model actually used. A worker is then a subprocess call that returns its
outputs, and one Python process can own a run's control flow. The forces
that would recur if this were reverted: a run whose control flow is spread
over a conversation and a disk state machine needs consistency machinery
for every open attempt, and a worker route that depends on what the
launching session loaded needs guards on that session.

## Decision

**One process runs an analysis.** `commonplace-analysis run` executes
the workflow in `commonplace.lib.agentic_analysis.workflow`: opening and
acquisition, the boundary, the runtime report, the three lens reports in
parallel, reconciliation, the report check and report verification with
its correction cascade, the memory profile and its verification, the
synthesis and its verification, assembly and publication, in that order
as ordinary calls. The cascade is explicit: a verifier's refusal leads to
the corrections of the authors it refused, their checks, a re-check of
every report against the corrected ones, reconciliation again when its
inputs changed, then the verifier again, under ADR 108's budgets held as
counters. A run lock refuses a second process. A rerun of a stopped or
interrupted run replays from the answer cache and continues.

**Workers are headless launches.** A worker is one launch of the run's
profile's harness in its headless mode, in the prepared worktree, with
the flags that let it read, write and run commands unattended. Its prompt
is the instruction to follow, `name = value` lines and the rendered
prompt section (ADR 117); its outputs are files it writes. The model the
harness records as used is the model the publication's provenance names.

**An attempt is a recorded execution of a job.** Each answer is cached
under a key of the prompt, the digests of the inputs supplied, the output
names and the profile; a rerun with the same key is the recorded answer.
A check's rejection, a verifier's correction, a re-ask after an input
changed, and a launch that timed out or left outputs incomplete each
spend one attempt of the job's budget. A launch that exits nonzero is
relaunched at most twice, after 30 and 120 seconds, with the failed
launch's outputs kept aside; a third nonzero exit, like a usage limit,
stops the run as an environment failure and spends no attempt. A
process killed between a launch and its record leaves that work
unrecorded, and the rerun repeats it. Budgets bound the evidence a run
records, not the executions that ever occurred.

**Checks and verdicts are applied in code, against snapshots.** Every
candidate is checked by the analysis's own checks (draft validation in its
role, the frozen source, declared checks, correction answers) against the
accepted members as they stood when the round began, so a parallel
round's outcome does not depend on completion order. A verifying role's
document is applied to the subjects it was handed: each is accepted or
refused with the verdict's blockers and limits, and verdict-dependent
findings refuse a subject whatever the blockers say. No judgment record,
scope or coverage state exists; before assembly the workflow asserts that
every required member's current bytes passed its check.

**The plan is role data.** The plan file lists the roles with their
instruction, outputs, reads, attempt budget, criteria groups, declared
checks and feedback, plus the type, the frozen-source role, the prompt
section and the criteria groups. Code jobs, verified-by declarations and
refusal inputs are not declared; the workflow knows them.

**The environment is pinned on the worktree side only.** A run belongs to
one prepared worktree: HEAD equals the preparation commit, the tree is
clean apart from run state, the running package equals the method commit
and the worktree's startup instructions are the committed ones. The
workflow asserts these at start and on every rerun and relies on them for
cache replay; a changed environment is a new run. `prepare` no longer
checks the origin's startup files or refuses a HEAD behind `main`:
nothing the launching session loaded reaches a worker.

**Declined requirements.** The port declines, bindingly, so that later
robustness work does not restore the machinery: several controllers
advancing one run; workers reporting asynchronously to a coordinator;
resuming an engine run with the new code; cancelling a parallel group at
its first failure; automatic recovery from every operational failure
(the run stops, the operator repairs and reruns); exact attempt counts
across an abrupt interruption; and a general scheduler or coverage state
in the workflow. Publication keeps its lock, exact manifests, destination
checks and journal reconciliation: simplification stops at the
publication boundary.

**Lifecycle and batches.** The commands are `commonplace-analysis
prepare`, `run`, `inspect`, `reset` and `integrate`; `run` exits 0 on a
completed run (a published artifact, or a blocked or out-of-scope result
kept local), 2 on a stop the operator can act on and 1 on a failure. A batch is a shell loop over prepare-and-run per system. The
Pi coordinator agent, the run driver and `commonplace-run` are deleted.

**Engine runs are not migrated.** Each engine worktree carries an
editable install of its own pinned source, so its run stays inspectable
and integrable from inside that worktree with that worktree's commands.
The new `prepare` refuses a revision without the workflow module (before
`03abc9185`), since it probes that module; an older method is rerun from
an existing worktree of its revision.

The words are workflow, run, worker, launch, attempt (a recorded
execution), answer cache, profile and harness. Engine, plan expansion,
hand-out, coordinator, judgment and coverage are retired, with the
vocabulary drift test that enforced them over the engine (ADR 116); the
job instructions live under `jobs/`.

## Considered alternatives

**Keep the engine, drive it from a headless loop.** A driver would still
close attempts, reconcile open ones and validate hand-outs; the
parallelism machinery stays because the engine's state model assumes it.
The engine survey (2026-10-18) counted about 3,000 lines serving that
model against about 1,000 of domain logic that already took plain values.

**A small declarative layer instead of a script.** Held as the return
point after phase 3: if the script exceeded about 600 lines of control
flow or needed readiness or coverage state beyond the call stack. It did
not; the cascade fit explicit calls.

**Harness-native workflows or the Agent SDK.** Pi's extensions on the
subscription hit the extra-usage billing wall and the sanctioned routes
bill per token; the SDK runs a worker through the same headless mode
this decision uses, with nothing the subprocess route lacks. The headless
commands are the covered programmatic route in every harness.

**Keep the coordinator agent for batches.** It existed to run the skill
inside a delegated session; with `run` a single command, a loop is
smaller and the harness checks lose their second layer.

**Migrate unfinished engine runs.** 76 engine runs were unfinished or
unintegrated at retirement, 32 of them published in their worktree but
not on `main`. Migration would mean reading engine records into the new
cache for runs whose worktrees already hold working engine code; declined.

**Durable launch ownership for exact attempt counts.** It would record a
launch before it starts and reconcile on rerun, which is the engine's
open-attempt machinery again. The evidence a run records is bounded by
the budgets either way.

**Names.** `jobs-engine/` for the instructions was the engine's; `jobs/`
is the workflow's word for a role's or code's unit of work. The moved
modules keep their names in the analysis package; the engine's
`worktree.py` became `preparation.py` beside the lifecycle's `worktree.py`.

## Consequences

The decision reaches behaviour through three consumers. The analysis
skill binds the operator's session to `commonplace-analysis prepare`,
`run`, `inspect` and `integrate`. The workflow consumes the plan file and
the worker profiles. The validator consumes `--artifact` and `--role` and
binds run identity from the run's `parameters.json`. The batch scripts
call the same commands per system.

Evidence. The pilot (2026-10-19) ran Dynamic Cheatsheet on the production
profile and published at the engine's cost: 11 attempts, 0 corrections,
no failed launch, 39:56 wall against the engine's 39:40 to 46:52 on the
same system, profile and source revision; its members agree with the
engine's on every classification and consequential claim and differ in
record count and unit judgments as the model's variance does. The
comparison is operational context, not a controlled experiment: one run
per route, and the kept deviations and the model's variance are not
separated. The fake-harness tests cover what the pilot did not exercise:
the correction cascade over two authors, an exhausted budget, relaunches,
an interrupted run, resume, reset and integration. The first pilot
attempt stopped on a missing working manifest, which the workflow now
writes at start. The published attempt ran at `2b70d329d`, before two
defects found in review were fixed (a relaunch could accept a failed
launch's outputs; a correction round's checks read members its siblings
were changing); neither could affect a run with no failed launch and no
correction round.

Limits. One production run on one harness; Claude and Codex are
supported by phase 0's probes and the fake-harness tests, not by a
production run. The relaunch policy has no observed failure behind it.
Four deviations from the engine's behaviour are kept: a stop before corrections at a verifier's last attempt, the
criteria superset in checks, the refusal body handed without
frontmatter, and reconciliation's fresh asks spending its budget. The
manifest records the model as the harness reports it, without Pi's
provider prefix. A worker's self-validation (ADR 105) stays a convenience
the workflow does not depend on. The re-check's correction branch, where
a member fails against a corrected sibling and is re-asked, is exercised
by no fake-harness scenario yet.
