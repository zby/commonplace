# Recurring task runner

## Goal

Run recurring KB tasks unattended through one heartbeat: a system cron tick
starts one Workjig run that launches one headless harness session, which
reads the recurring task directory, runs the tasks that are due, commits each
task's declared paths separately, and exits. Nothing in the interactive
harness schedules or relays anything, and the runner holds no per-task
schedule.

Posed by the operator on 2026-10-23, in the conversation that separated two
underexplored areas: artifact lifecycles and many-agent collaboration.
Recurring tasks were identified as the obvious need in both. The operator set
standing constraints on what the runner may automate and how it runs:

- **Automatic tasks mostly do obvious work.** A recurring task classifies,
  flags, measures or reports. It does not make judgment calls that the
  library would have to defend later.
- **Every automatic change is easily reversible.** Each task's run ends in
  one commit that `git revert` undoes whole. No automatic change touches a
  surface whose reversal would need a relocation, a redirect or a
  re-extraction.
- **No worktrees or branches.** Runs happen in the operator's checkout on the
  current branch. The operator judged that merging creates as much chaos as
  it prevents, and that the start should be experiments with easy tasks.
- **Tasks isolate themselves.** Isolation is a property of the task, not of
  the runner: a task declares the paths it writes, stays inside them, and
  only those paths are staged for its commit. Other sessions' uncommitted
  work is never swept into a task commit.
- **One heartbeat, not one cron entry per task.** The operator chose the
  heartbeat on 2026-10-23 after checking how other systems dispatch
  recurring work; the evidence is below. Adding a task means adding a
  runbook, not editing cron.

## Why a heartbeat, and which kind

Analysed systems split on one fact: whether a long-lived session exists that
keeps its conversation context between triggers (a resident session, in this
workshop's usage; the term is local). Where one exists, a periodic prompt into
it lets the model dispatch from a checklist, because the state is already in
context: OpenClaw's HEARTBEAT.md, Prime Agent's injected heartbeat prompt
([report verification](../../agentic-system-analyses/retained/primeintellect-ai--prime-agent/report-verification.md)),
Coral's manager tick that interrupts the live agent
([heartbeat feedback](../../agentic-system-analyses/retained/human-agent-society--coral/runtime.md#rt-rte-heartbeat-feedback)).
Where none exists, code dispatches one run per job: Phantom's scheduler
([runtime](../../agentic-system-analyses/retained/ghostwright--phantom/runtime.md)),
AgentOS's database-coordinated poller
([review](../../agentic-systems/reviews/agno-agentos.md)), PAL's startup cron
jobs ([runtime](../../agentic-system-analyses/retained/agno-agi--pal/runtime.md)).
OpenClaw and Prime Agent carry both and route by the same rule: batchable
periodic checks go to the heartbeat; exact times, isolation from the main
context or a different model go to per-job cron.

Commonplace has no resident session, so its heartbeat is the bounded variant
the repo-centric stack ingest describes
([ingest](../../sources/building-a-repo-centric-modular-agent-stack-2085784422339768686.ingest.md)):
reconcile state from files, select bounded work, act, record, exit.
Continuity lives in the task logs, not in a model context.

Three costs come with the heartbeat, and the design answers each:

- **Due-ness as a model judgment** would let a drifted run skip or repeat a
  task. So the runner computes the due set in code, from each log's last run
  date against the runbook's cadence, and injects that list into the prompt.
  The model executes; it does not decide what is due.
- **A shared session** means one task's failure or usage limit ends the rest
  of the tick, and all tasks share one model and effort. Accepted for easy
  tasks. Per-task commits keep reversibility per task.
- **Growth.** Any task that later needs isolation, an exact time or its own
  model wants a per-task launch. That path is the known successor, not the
  first design, and it reuses the same runbooks.

## Starting state

- A recurring task format already exists: a stable runbook plus an appended
  log, with [review-explanatory-reach](../../tasks/recurring/review-explanatory-reach.md)
  as its only instance. Its log records zero runs. The runbook has never had a
  launcher, which is the evidence that a role record without a launcher is a
  label.
- The launch runtime exists. [ADR 118](../../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)
  and [ADR 119](../../reference/adr/119-analysis-workers-launch-through-workjig.md)
  put analysis workers on Workjig through `src/commonplace/headless/`, with
  Claude, Codex and Pi profiles, a run lock, usage-limit detection and durable
  launch records. The runner is glue over these, not a second runtime. The
  analysis workflow's prepared worktrees are not reused here.
- The theory this rests on: [the practical scheduler is the host language](../../theory/the-practical-scheduler-is-the-host-language.md)
  (cron plus Python decide what is due; the model does the task),
  [knowledge storage does not imply contextual activation](../../theory/knowledge-storage-does-not-imply-contextual-activation.md)
  (a runbook nobody launches and a log nobody reads are both inert),
  [periodic KB hygiene should be externally triggered](../../theory/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md)
  (the heartbeat is that external trigger, kept out of routing), and
  [the boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md)
  (which is why unattended tasks are limited to obvious, reversible work).

## Order of work

The operator reordered the workshop on 2026-10-23: first write tasks that
can run unattended and test them by hand; only then build the heartbeat
around what the tests show. A runner designed before any task has run would
fix the runbook format, the scope check and the prompt from guesses.

**Phase 1: tasks and hand launches.** Two runbooks now carry `Cadence`,
`Write scope` and `Consumer` sections, and one of them a `Batch` section:
[review-explanatory-reach](../../tasks/recurring/review-explanatory-reach.md)
(ten notes per run, so run N+1 depends on run N's reviewed list) and
[workshop-dormancy-report](../../tasks/recurring/workshop-dormancy-report.md)
(git age per workshop; observes only). Each is launched by hand with
[launch-prompt.md](./launch-prompt.md) as the prompt of a headless session,
once per harness that matters, and judged on four points: did the run stay
inside its write scope; did it produce exactly one commit with the required
subject; did the second run of the reviewer use the first run's reviewed
list; is the output something the operator actually reads. Record each
launch in [launches.md](./launches.md): date, task, harness and model, the
flags used, commit hash or failure, and the four judgments.

The harness flags are part of the test. A headless Claude Code or Codex
session needs permission to write and to run `git add` and `git commit`
without prompts; the narrowest flag set that lets the run complete is the
one the heartbeat will later use, and is recorded with the launch.

**Phase 2: the heartbeat.** Starts only after both tasks have two clean hand
launches. Items 1, 3 and 4 below are its design; items 2, 5, 6 and 7 are
settled or revised by phase 1. The `task-recurring` type template is
updated with the new sections after the format has survived the launches,
not before.

## What the workshop must resolve

1. **The entry point.** One command, in the style of `commonplace-analysis`,
   with no task argument: read every runbook under `kb/tasks/recurring/`,
   compute the due set from logs and cadences, exit quietly when nothing is
   due, otherwise build one prompt listing the due tasks with their runbooks
   and log tails, launch one Workjig call in the checkout, and record the
   run. Whether this is a new `commonplace-heartbeat` command or a subcommand
   of `commonplace-analysis` is open.
2. **The runbook format.** Each runbook declares its cadence, its write
   scope and its consumer in a form the runner can read. Both first runbooks
   now carry these as sections; phase 1 decides whether sections suffice or
   frontmatter fields are needed for the due-set computation.
3. **The cron contract.** Cron runs with a minimal environment. The wrapper
   must set PATH to the user-level uv tool and HOME to where the harness
   login state lives, or every tick fails silently. Each tick starts a fresh
   run; a tick never resumes, because ADR 119 makes an unsettled launch wait
   for operator acknowledgement and cron cannot acknowledge. The run lock
   makes an overlapping tick exit at once. A usage limit ends the tick with a
   record, not a retry loop; the due set is recomputed next tick, so missed
   tasks are not lost.
4. **Self-isolation and the shared checkout.** The run shares the checkout
   with whatever interactive sessions are open. The task's declared write
   scope is the whole isolation mechanism. In the heartbeat the model commits
   each task by staging its declared paths explicitly; the runner checks
   after the run that no commit and no leftover change lies outside the
   union of due scopes, logs any violation, and leaves the operator to
   revert. Whether a task should be skipped when its scope already has
   uncommitted changes is open; the first runs will show how often that
   occurs.
5. **The consumer.** Each recurring task names what reads its output: the
   operator reviewing the commit, a review bundle, or a mailbox message. A
   task whose only output is its own log is admitted only while the log is
   what the operator reads; the explanatory-reach log shows where an unread
   log ends.
6. **Admission test for a task.** A task is automatic only if its run is
   obvious and reversible in the operator's sense above. The operable form is
   the declared write scope plus the one-commit-per-task rule. Shared
   surfaces such as navigation lists and indexes are outside any first task's
   scope.
7. **Retained task state.** The log is the task's memory. The discriminating
   question is whether run N+1 behaves differently because of what run N
   wrote. If it does not, the log is ceremony and a plain prompt would do.
   The first two runs of the first task answer this.

## First tasks

Start with tasks whose write scope is one file they own. The explanatory-reach
reviewer is the first: it classifies and flags, and writes only its log. A
second candidate is a workshop dormancy report: read git age under
`kb/work/`, list workshops untouched past a threshold with their last commit,
and write the result to a report file the task owns. It does not edit the
active workshops list; demoting entries is a later task once the report has
been read a few times and the threshold has settled.

## Evaluation boundary

In scope: the heartbeat command and cron wrapper; the runbook format with
cadence, write scope and consumer; the due-set computation; the after-run
scope check and one-commit-per-task rule; the first tasks and their first
runs as evidence; how often unattended runs collide with interactive
sessions.

Out of scope: harness-side scheduling (routines, hooks, in-harness cron);
worktrees, branches and merge handling; per-task launches, recorded as the
successor path only; agent identity beyond the task name and its log;
cross-session messaging, which stays with the mailbox; any task that edits
library content, type specs, instructions, navigation or indexes; per-role
model routing, which [runner-execution-profiles](../runner-execution-profiles/README.md)
owns.

## What closes the workshop

Phase 1 closes when both tasks have two clean hand launches recorded in
`launches.md`. The workshop closes when a cron tick has run the heartbeat at least twice with the first task due and
without operator involvement, each task run ended in one commit confined to
the task's declared paths, a tick with nothing due exited without a launch,
the second run demonstrably read the first run's log, and the operator has
kept or reverted at least one result. Durable outcomes then go to: an ADR
for the heartbeat's launch and authority rules, an instruction for authoring
a recurring task under the admission test, and a reference page for the
command. The workshop is deleted after extraction.
