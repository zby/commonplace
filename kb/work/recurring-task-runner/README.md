# Recurring task runner

## Goal

Run recurring KB tasks unattended: a system cron tick starts a Workjig run
that launches one headless harness session with a task's runbook, retains the
run, and delivers the result to something that reads it. Nothing in the
interactive harness schedules or relays anything.

Posed by the operator on 2026-10-23, in the conversation that separated two
underexplored areas: artifact lifecycles and many-agent collaboration.
Recurring tasks were identified as the obvious need in both. The operator set
standing constraints on what the runner may automate and how it runs:

- **Automatic tasks mostly do obvious work.** A recurring task classifies,
  flags, measures or reports. It does not make judgment calls that the
  library would have to defend later.
- **Every automatic change is easily reversible.** A run ends in one commit
  that `git revert` undoes whole. No automatic change touches a surface whose
  reversal would need a relocation, a redirect or a re-extraction.
- **No worktrees or branches.** Runs happen in the operator's checkout on the
  current branch. The operator judged that merging creates as much chaos as
  it prevents, and that the start should be experiments with easy tasks.
- **Tasks isolate themselves.** Isolation is a property of the task, not of
  the runner: a task declares the paths it writes, stays inside them, and
  the runner stages and commits only those paths. Other sessions' uncommitted
  work is never swept into a task commit.

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
  (cron plus Python decide; the model does the task),
  [knowledge storage does not imply contextual activation](../../theory/knowledge-storage-does-not-imply-contextual-activation.md)
  (a runbook nobody launches and a log nobody reads are both inert), and
  [the boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md)
  (which is why unattended tasks are limited to obvious, reversible work).

## What the workshop must resolve

1. **The entry point.** One command, in the style of `commonplace-analysis`,
   that takes a task name and does four things: build the prompt from the
   runbook and the log tail, launch one Workjig call in the checkout, check
   that the run wrote only inside the task's declared paths, and stage and
   commit exactly those paths. Whether this is a new `commonplace-recurring`
   command or a subcommand of `commonplace-analysis` is open.
2. **The cron contract.** Cron runs with a minimal environment. The wrapper
   must set PATH to the user-level uv tool and HOME to where the harness
   login state lives, or every tick fails silently. Each tick starts a fresh
   run; a tick never resumes, because ADR 119 makes an unsettled launch wait
   for operator acknowledgement and cron cannot acknowledge. The run lock
   makes an overlapping tick exit at once. A usage limit ends the tick with a
   record, not a retry loop.
3. **Self-isolation and the shared checkout.** The run shares the checkout
   with whatever interactive sessions are open. The task's declared write
   scope is the whole isolation mechanism, so the runner must enforce it:
   a run that touched anything outside its scope is discarded, its changes
   outside scope reverted file by file, and the violation logged. Whether a
   run should also refuse to start when the checkout has uncommitted changes
   inside its scope is open; the first runs will show how often that occurs.
4. **The consumer.** Each recurring task names what reads its output: the
   operator reviewing the commit, a review bundle, or a mailbox message. A
   task whose only output is its own log is admitted only while the log is
   what the operator reads; the explanatory-reach log shows where an unread
   log ends.
5. **Admission test for a task.** A task is automatic only if its run is
   obvious and reversible in the operator's sense above. The operable form is
   likely a declared write scope in the runbook, checked by the runner after
   the run, plus the single-commit rule. Shared surfaces such as navigation
   lists and indexes are outside any first task's scope.
6. **Retained role state.** The log is the task's memory. The discriminating
   question is whether run N+1 behaves differently because of what run N
   wrote. If it does not, the log is ceremony and a plain cron prompt would do.
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

In scope: the entry point and cron wrapper; the recurring task runbook
format, including write scope and consumer declarations; the write-scope
check and single-commit rule; the first tasks and their first runs as
evidence; how often unattended runs collide with interactive sessions.

Out of scope: harness-side scheduling (routines, hooks, in-harness cron);
worktrees, branches and merge handling; agent identity beyond the task name
and its log; cross-session messaging, which stays with the mailbox; any task
that edits library content, type specs, instructions, navigation or indexes;
per-role model routing, which [runner-execution-profiles](../runner-execution-profiles/README.md)
owns.

## What closes the workshop

A cron tick has run the first task at least twice without operator
involvement, each run ended in one commit confined to the task's declared
paths, the second run demonstrably read the first run's log, and the operator
has kept or reverted at least one result. Durable outcomes then go to: an ADR
for the runner's launch and authority rules, an instruction for authoring a
recurring task under the admission test, and a reference page for the
command. The workshop is deleted after extraction.
