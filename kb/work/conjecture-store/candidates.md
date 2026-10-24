# Candidate conjectures

Conjectures raised while planning the store, written in the draft type's
shape as plain text because the collection does not exist yet. Each becomes a
conjecture record at stage 0 seeding or is dropped.

## Every project builds its theory from its own choices plus general knowledge

- **Conjecture:** every project holds two kinds of commitments, choices it
  made and theory it built, and its working knowledge is theory stated with
  some variables bound to those choices and the rest to general knowledge.
  The transferable part of a project's knowledge is what survives when its
  choices are quantified out. Posed by the operator on 2026-10-24.
- **problem:** How should a knowledge system separate what a project
  believes because of what it chose from what it believes about any system?
- **Reach:** if true, the conjecture store and its two projections are a
  framework feature, not a Commonplace-local one: every consuming KB has its
  own choices (its ADRs, or decisions never written down) and its own theory
  (`kb/notes/`), and the same `choices` field sorts them. It also explains
  why Commonplace's theory collection has a high bar: it tries to hold only
  the quantified-out part, which is the smallest part of any project's
  working knowledge, so most of what a project knows has nowhere to go
  without a store for bound conjectures. It predicts that the bound/unbound
  split is relative to the system boundary: a choice made by a parent
  project is general knowledge to a subproject.
- **Analogues to check, not yet read for this purpose:** Carnap's external
  and internal questions (choosing a framework is a practical decision;
  questions inside it are theoretical), already touched in
  [philosophy borrowing](../philosophy-borrowing/carnap-explication.md);
  Lakatos's hard core and protective belt; architecture decision records as
  the practice that writes choices down without theory.
- **refuters:**
  - a project whose working knowledge cannot be factored this way: a claim
    that is neither about any system nor conditional on a nameable choice
  - a consuming KB where sorting by declared bindings misroutes most
    conjectures, because the choices cannot be named at the grain the
    arguments use
- **missing:** a second project, not Commonplace, whose working notes factor
  into bound and unbound claims when read with this lens
- **trigger:** `free variable|bound variable|residual selection|hard core`
  across `kb/`, and any consuming-project KB ingested into
  `kb/agentic-system-analyses/`
- **choices:** none; this is a theory conjecture

## Contradictions loaded into one context get silently averaged

- **Conjecture:** when an agent holds a claim and its contradiction in one
  context without structure that keeps them apart, its outputs drift toward
  a blend of the two rather than representing either. Carried from the
  deleted epistack menu (2026-07-08), where it justified separating the
  neutral map from the verdict layer and rejecting a case root that carries
  a bottom line; see [prior work](./prior-work-epistack.md).
- **problem:** Must rival conjectures and their criticism be kept
  structurally separate from the surface an agent writes from, or can one
  context hold both without distortion?
- **Reach:** if true, it is the mechanism behind three of the store's
  rules: rivals are separate records under one problem, the projection is
  computed rather than written into the store, and no conjecture is a
  premise. It also bears on review design generally: a reviewer given the
  verdict drifts toward it. If false, some of the separation is cheaper
  than assumed and could be relaxed.
- **refuters:**
  - the designed experiment run and showing no drift: one agent extends a
    neutral map from a case root that carries a bottom line, another from
    a verdict-free root, and the bottom-line arm's edits do not move toward
    the verdict
  - an agent shown two contradicting notes that reliably reports the
    contradiction instead of blending, across models and prompts
- **missing:** one run of the designed experiment, on any case with a
  stated bottom line and a neutral map
- **trigger:** `silently averag|averaged away|blend.*contradict` across
  `kb/`; any experiment record under `kb/theory/evidence/` whose arms differ
  by whether a verdict was in context
- **choices:** none; this is a theory conjecture

## Workflow engine rivals (design conjectures)

Extracted 2026-10-24 from ADR 113 (2026-10-09), ADR 118 (2026-10-19),
ADR 119 (2026-10-21) and the sibling Treadle repository (36 commits,
2026-10-15 to 10-18, with its own ADRs 000 and 009 to 013). The step-program
demo of 2026-10-14 that ADR 119 names was Treadle's starting design, not a
separate rival; the operator confirmed this on 2026-10-24. The option space
was mapped first in the proposal
[replaceable workflow orchestrators](../../reference/proposals/replaceable-workflow-orchestrators.md)
(2026-10-03). All five share one problem, repeated verbatim on each record
at seeding:

- **problem:** How should Commonplace run a multi-worker workflow so that a
  run survives interruption, each verdict records what it rested on, and
  workers launch through the harnesses people already pay for?

Bindings shared by every rival below, named once:

- `Commonplace is Python` — bare choice
- `workers run on subscription-billed harnesses, not API billing` — bare
  operator choice, stated in ADR 118
- `a run executes in a prepared worktree pinned to a commit` — ADR 118
- `every harness exposes a headless mode (claude -p, codex exec, pi -p)` —
  an environment fact, not a choice; its loss makes rival 5 moot

The unbound content extracted so far is one theory note,
[the practical scheduler is the host language](../../theory/the-practical-scheduler-is-the-host-language.md).
Its witnesses are the three same-profile run comparisons logged as METHOD
entries on 2026-10-09, 10-19 and 10-20, which nothing links to it yet.

### 1. A prose schedule run by the coordinating agent with sub-agents

- **Conjecture:** the workflow can be an instruction the coordinating agent
  follows, dispatching sub-agents, with run state in the conversation. The
  no-code route; the status quo before ADR 113 and still the route of the
  full pass, review batches and skill-dispatched workers.
- **Reach:** no engine to maintain; any harness with sub-agents runs it.
- **refuters:** a trace audit showing interpretation failures where the
  schedule was followed wrongly; a run lost with its conversation.
- **record:** criticism 2026-10-09, ADR 113 context: "the trace audit's
  failures were interpretation failures, and a run's state lived in one
  conversation" — refuter met for the analysis workflow. Still in use for
  smaller workflows, so scope is the open question, not the verdict.
- **missing:** a workflow size below which interpretation failures stay
  tolerable; nothing measures it.
- **trigger:** `interpretation failure|trace audit` across `kb/`; any
  runner-execution-profiles entry that moves a prose workflow to code.
- **choices:** the shared bindings minus the worktree one; plus `the
  harness provides an authorized sub-agent mechanism`.

### 2. A disk state machine advanced by a coordinator agent (artifact-run engine)

- **Conjecture:** a plan of jobs over a typed artifact's roles, advanced
  from disk by one command, with hand-outs to workers and verdicts pinned to
  input versions, gives resumable runs and exact provenance. ADR 113.
- **Reach:** every verdict names the versions it rested on; a run resumes
  from disk; the coordinator stays an agent.
- **refuters:** consistency machinery for open attempts exceeding the
  domain logic it serves; a second layer of harness checks for nested
  coordination.
- **record:** criticism 2026-10-18, engine survey cited in ADR 118: about
  3,000 lines serving the parallel-attempt state model against about 1,000
  of domain logic — refuter met. Superseded 2026-10-19; 76 unfinished runs
  left unmigrated. Belongs in `refuted/`.
- **missing:** nothing; the conjecture is closed unless a consumer needs
  several attempts open at once with shared state.
- **trigger:** `open attempt|readiness|hand-out` in new ADRs; a workflow
  whose attempts must share state across processes.
- **choices:** shared bindings plus `the coordinator is an agent in a
  conversation`.

### 3. The harness drives; the workflow reports its complete waiting frontier (Treadle)

- **Conjecture:** the workflow is ordinary Python whose control flow is the
  dependency structure, the harness drives it one step at a time, and each
  step returns the complete waiting frontier for the harness to dispatch and
  settle. Two mechanisms were tried for keeping state between steps, so the
  record has two phases:
  - *Replayed step program* (demo 2026-10-14; Treadle's first runner,
    2026-10-15): a short-lived command replays the script from the top
    against write-once recorded answers, memoized by content, so an edited
    step misses and an unedited one hits. A monadic build with constructive
    traces and a restarting scheduler, the agent as executor.
  - *Resident Temporal without per-step replay* (Treadle ADRs 009 and 011,
    2026-10-16 and 10-17): workflow state lives in Temporal history, a
    resident server and worker answer thin step commands, and a coordinator
    serializes steps. Designed and measured, not implemented.
- **Reach:** harness sub-agents stay usable because the harness, not the
  workflow, launches workers; an interactive orchestrator can watch and
  intervene mid-run; edits to the workflow are tolerated by content keys.
- **refuters:** the frontier, settlement, submission and claiming machinery
  costing more than a route that calls harnesses directly; a step slower
  than the operator tolerates (about one second, Treadle ADR 011); branch
  identity swapping answers between identical downstream calls when
  completion order changes.
- **record:**
  - criticism 2026-10-17, Treadle ADR 011: per-step replay dropped because
    Temporal history already provides it and startup costs 4 to 6 seconds a
    step — refuter met for the replay phase.
  - criticism 2026-10-18, Treadle's headless-workers research and README:
    "most of Treadle's machinery (frontier, settlement, coordinator,
    submit) is unnecessary for unattended work"; the author expects to use
    headless harnesses instead. Withdrawn on a complexity judgment, not
    refuted by a run. Treadle's own note keeps the harness-driven mode "for
    an interactive orchestrator supervising sub-agents".
  - criticism 2026-10-21, ADR 119: not extracted because the one-process
    workflow needs no replay and Workjig journals results under content
    keys with the same edit tolerance; "its pairing with a job queue stays
    undecided and unneeded".
  - Standing: `criticized`, not in `refuted/`. The binding below is what
    the headless route declined, so the conjecture is the live rival if
    that binding ever returns.
- **missing:** a workflow that needs an interactive orchestrator
  supervising sub-agents mid-run, or a run that must outlive its process or
  span machines; nothing unattended needs either.
- **trigger:** `complete frontier|waiting frontier|outlive.*process|
  durable execution|Temporal|job queue|workers pull` across `kb/` and the
  Workjig ADRs; any workflow record where a human intervened mid-run.
- **choices:** shared bindings plus `the harness drives and the workflow is
  its transmission` — bare, and the inversion ADR 118 reversed; the
  Temporal phase adds `an external durable-execution service is acceptable
  infrastructure` — bare.

### 4. Harness-native workflows or the Agent SDK

- **Conjecture:** the harness's own workflow facility or the vendor SDK runs
  the workers, so Commonplace owns no launch mechanics.
- **Reach:** nothing to maintain below the workflow.
- **refuters:** a billing wall when the facility bills per token or needs
  extra usage outside the subscription; a sandbox that cannot run the
  deterministic steps.
- **record:** criticism 2026-10-09 and 2026-10-19, ADR 113 and ADR 118: the
  native facility exists in one harness and its sandbox cannot run
  commands; Pi's extensions hit the extra-usage billing wall; the SDK uses
  the same headless mode with nothing the subprocess route lacks — refuters
  met under the subscription binding.
- **missing:** a harness whose native workflow runs commands and bills under
  the subscription.
- **trigger:** harness release notes ingested into `kb/sources/` mentioning
  workflow, sandbox command execution or subscription coverage.
- **choices:** shared bindings. Moot, not refuted, if the billing binding
  is dropped.

### 5. One Python process runs the workflow over headless harness launches (ADR 118, Workjig)

- **Conjecture:** the plan is role data, control flow is ordinary Python
  whose call stack is the schedule, a worker is a subprocess launch that
  returns its outputs, attempts are recorded executions cached by content,
  and verdicts are applied in code. The launch mechanics — fresh output
  directories, backoff, problem files beside exit status, usage-limit
  detection, the content-keyed answer cache, one durable reservation per
  launch — are not about analyses, so they live in Workjig, a package with
  no Commonplace imports, while every launch decision, attempt count and
  verdict stays in the workflow. ADR 118 (2026-10-19) adopted the route;
  ADR 119 (2026-10-21) extracted the mechanics for maintenance, with
  Workjig 0.1.0 on PyPI on 2026-10-20. The operator confirmed on 2026-10-24
  that the extraction is not a separate design.
- **Reach:** no consistency machinery for open attempts; harness checks lose
  their second layer; the workflow is testable without a model; one
  implementation of the result protocol, tested once, reusable by other
  workflows and projects.
- **refuters (the ADRs' own return points):** the script exceeding about
  600 lines of control flow, or needing readiness or coverage state beyond
  the call stack; a run that must outlive its process; a production
  relaunch where backoff delay mattered; retry policy and Commonplace's
  budgets conflicting in a run; a result reused across worktrees because
  the content key cannot see ambient configuration.
- **record:** witnesses 2026-10-19 and 2026-10-20, same-profile comparisons
  against the engine and across the runtime port, logged as METHOD entries;
  one source family (the analysis workflow on Dynamic Cheatsheet), so one
  independent witness.
- **missing:** a second workflow on the route, which is also a second
  consumer of Workjig; the review-on-workjig workshop is building one.
- **trigger:** `lines of control flow|readiness state|coverage state|
  relaunch.*delay|escalating backoff|retry policy` in ADRs, run records and
  `src/commonplace/headless`; any `import workjig` outside that package;
  the review-on-workjig workshop's first run record.
- **choices:** shared bindings plus `one process owns a run` — ADR 118 —
  and `the runtime journals results, not control position` — backed by the
  practical-scheduler theory note, the one binding in this set with a
  `because`.
