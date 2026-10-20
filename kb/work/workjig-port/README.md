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

## Mapping settled by reading both codebases

These are the consumer-side changes the port implies. They are findings, not
frozen method; execution may find a better cut.

- `Run.ask` becomes `Run.call(Request)`; `gather` becomes `run.parallel`.
  Corrections, budgets, checks, `accept` and `log.jsonl` stay in Commonplace;
  Workjig has no artifact directory or event log by design.
- **Identity.** Today's answers are keyed by content alone. Workjig needs a
  stable `call_id` plus request material, and the material includes timeout,
  launch allowance, retry policy and worker argv. Call ids derive from role
  and round; a changed timeout or profile relaunches instead of replaying.
- **Budget accounting.** Timeouts and incomplete results are counted from
  `result.launches` statuses instead of the failure log. A re-ask after a
  settled failure needs a new call id, since a settled call replays its
  recorded outcome.
- **Worker commands.** Profiles are harness, model, effort and free flags.
  Build `CommandWorker` argv from the profile in Commonplace; Workjig's adapter
  factories cover a narrower set. Argv enters the request hash as the profile
  enters today's key.
- **Problem reporting.** Workers write `problem.json` with `kind` and
  `message` instead of free-text `problem.md`; the `Problem` path and role
  instructions follow.
- **Provenance.** Served model and session come from Workjig's
  `parse_evidence` over each launch's `stdout.log`; nothing persists them yet.
- **Recovery in the CLI.** A rerun after a kill stops on
  `UncertainLaunchError` until `acknowledge_stopped` is called. `inspect` or
  `reset` needs an affordance for that.
- **Run layout.** Readers of `answers/` and `attempts/` move to `run.json` and
  `launches/`; `log.jsonl` stays.
- **Usage limits and parallel rounds** keep today's behaviour: the same
  substring policy, and parallel workers in one shared worktree.

## Open items and how they return to decision

- **Dependency form.** Path dependency, git dependency or a published package.
  Decide before the user-level editable tool is re-synced; the choice gates
  INSTALL.md. Workjig has not published and has not registered a name.
- **Escalating backoff.** ADR 118 relaunches after 30 then 120 seconds;
  `RetryPolicy` has one fixed delay. A fixed delay is acceptable for the
  first port. Ask Workjig only if the production run shows a relaunch where
  the delay mattered.
- **Persisted harness evidence.** Workjig could attach parsed evidence to the
  launch record. Consumer-side parsing is acceptable for the first port;
  revisit if provenance code grows past a helper.
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
