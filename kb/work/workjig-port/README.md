# Reimplement the analysis workflow over Workjig

Posed 2026-10-20 by the operator: make Workjig, the standalone runtime at
`/home/zby/llm/workjig`, the execution layer under Commonplace's headless
analysis workflow, replacing `src/commonplace/headless/{jobs,harness}.py`.
Workjig was extracted from this work by
[headless-workflow-extraction](../headless-workflow-extraction/README.md);
that workshop closes when this one lands, and the staged package copy it still
holds under `package/` is deleted then.

Framing state: Workjig tracks its main branch; the port follows the current
head rather than a pinned commit. Commonplace at main after ADR 118, with the
workflow in `src/commonplace/lib/agentic_analysis/workflow.py` calling
`Run.ask`, `Run.checked` via `headless/corrections.py`, `gather` and
`Run.accept`.

## What closes the workshop

- The analysis workflow runs on Workjig with `commonplace.headless` reduced
  to a thin consumer layer or removed.
- The fake-harness suites under `tests/commonplace/headless/` and
  `tests/commonplace/agentic_analysis/` keep their behavioural assertions
  (correction cascade over two authors, exhausted budget, relaunches,
  interrupted run, resume, reset, integration), re-pointed at Workjig workers.
- One production analysis on the production profile, compared with the ADR 118
  pilot (`AAS-2026-10-19-dynamic-cheatsheet-2390eec63b75-01`): same
  classifications and consequential claims, attempt count and wall-clock in
  the same range. One run is operational context, not a controlled trial.
- The old runtime modules, the extraction workshop and its package copy are
  deleted; an ADR records the runtime dependency and amends ADR 118 where the
  guarantees changed; INSTALL.md gains the dependency step.

Until the last item lands, Workjig is not mentioned in any Commonplace
documentation outside this workshop (operator rule, 2026-10-20).

## Decisions already taken by the operator

- **Workjig's stronger recovery guarantee is accepted.** ADR 118 chose to
  repeat work after a kill; Workjig reserves each launch durably and blocks
  automatic resume until an operator acknowledges that the old worker stopped.
  This serves Commonplace too. The ADR is amended when the port lands, not
  before, and the difference is not raised with Workjig as a conflict.
- **Inline paths are the caller's responsibility.** Workjig writes `task`
  verbatim and lists input and output paths in a frame below it, minted per
  launch. The `name = value` lines (ADR 117) therefore refer to inputs by
  name and let the frame resolve them; no Workjig change is requested.
- **Review input to Workjig goes to its repository**, not into the KB:
  `docs/handoff-from-commonplace-2026-10-20.md` there carries the theory
  mapping with public-site links and no internal decision records.

## State of the port

Landed on main, 2026-10-20:

- **Dependency.** `workjig` is a runtime dependency through a uv path source
  (editable, `../workjig`). The project venv and the user-level editable tool
  both import the sibling checkout. The next `llm-commonplace` release is
  blocked until Workjig is on PyPI and the path source becomes a version pin.
- **Consumer layer.** `headless/harness.py` turns a profile into a
  `CommandWorker` with the harness's machine-readable output and its Workjig
  output protocol, and reads the served model from each launch's
  `stdout.log`. `headless/jobs.py` keeps `ask`, `checked`, `accept`, `log`
  and `gather` over `workjig.Run`; records live under the run's `calls/`.
- **Identity and budgets.** An ask is a chain of calls `<job>#<position>`.
  A timed-out, incomplete or malformed result spends an attempt and moves to
  the next position; a usage limit or environment failure inherited from an
  earlier run is skipped, so a rerun after the repair asks again. `gather`
  stays: parallel rounds run checks and corrections, not single requests.
- **Operator affordances.** `commonplace-analysis retry <run> <job> [--key]`
  dismisses a worker problem or an answer, replacing deletion of a cache
  file. `acknowledge <run> <launch>` settles a launch an earlier controller
  left unsettled. The skill and the command reference describe both without
  naming the runtime.
- **Verification.** The complete suite passes, the fake-harness suites
  included. One tiny ask through each real harness (Claude Code haiku, Pi
  and Codex on gpt-6-luna) delivered and recorded the served model.

Behaviour that differs from ADR 118, for the ADR that closes this workshop:

- **Timeout is part of request identity.** Resuming with a different
  `--timeout` asks every job again. The skill and command reference say to
  resume with the original timeout.
- **Fixed relaunch delay.** Relaunches wait 30 seconds each, not 30 then 120.
- **A problem written by a failing launch is the result.** Workjig reads the
  problem file before the exit status; the old layer relaunched and kept the
  problem as evidence.
- **Usage limits** are read from the harness's terminal event or a
  `usage_limit` problem, no longer from a substring of either stream.

## Open items and how they return to decision

- **Production comparison.** The next step: one analysis on the production
  profile, compared with the ADR 118 pilot. Run it from a fresh prepared
  worktree, at the operator's call, since it spends a production
  budget.
- **Escalating backoff.** Ask Workjig only if the production run shows a
  relaunch where the delay mattered.
- **Persisted harness evidence.** Consumer-side parsing is a helper per
  harness; revisit if provenance code grows past that.
- **Timeout identity.** If resuming with a longer timeout turns out to be a
  common repair, raise with Workjig whether the timeout belongs in request
  identity.
- **Pilot integration.** The ADR 118 pilot is published in its worktree but
  not integrated; that decision is independent of this port.

## Coordination

Work in the `headless-port` worktree at `/home/zby/llm/commonplace-headless`
if batch coordinators are running from the main checkout, since they execute
its `src/` live through the user-level tool; check with
`pgrep -af "bash-2|pi -p|commonplace-analysis"`. Land on main by fast-forward.
Workjig edits belong in its repository under its own AGENTS.md; this
workshop only consumes its public API.

## Bookkeeping

Keep run notes in this directory. Record each production comparison with its
run id and the Workjig and Commonplace commits it used. Extract durable
conclusions to the ADR and delete the workshop when the closing conditions
hold.

---

- [ADR 118](../../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md) — supersedes: the decision this port amends
- [ADR 117](../../reference/adr/117-plans-derive-their-structural-jobs-from-the-type.md) — depends-on: the prompt convention whose `name = value` lines now refer to inputs by name
- [The practical scheduler is the host language](../../notes/the-practical-scheduler-is-the-host-language.md) — rests-on: why the workflow stays ordinary Python and the runtime journals results rather than control position
- [headless-workflow-extraction](../headless-workflow-extraction/README.md) — supersedes: the extraction this port consumes
