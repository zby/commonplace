# Run system analyses without a supervising agent

## Commission

The operator opened this workshop on **2026-11-07** to move the mechanical
outer steps of `analyse-agentic-system` into a Python command. The requested
workshop contains this framing and an [implementation and fixture-test
plan](./plan.md). The operator subsequently authorized one Sol worker to
implement, test and commit the change, followed by parent verification and
local repairs. If substantial rearchitecture is needed, the parent may revert
the implementation, revise the plan and commission a fresh worker, for at most
three implementation attempts. This does not authorize live analysis runs,
campaign launches, integration of analysis publications or evidence cleanup.
[Execution record](./execution.md) tracks assignments.
[Parent acceptance](./parent-review.md) records the independent review, three
local repairs and the complete passing test run. Attempt 1 is accepted for
deterministic execution mechanics; live-provider behavior remains untested.

The intended operator experience is one command for one supplied system, or a
URL list with bounded concurrency, without a supervising agent preparing,
starting and monitoring each run. The existing Python analysis workflow and
its Workjig-backed analyst/verifier launches remain the execution mechanism.
Removing the supervising agent does not mean removing workflow orchestration
or the model-dependent analysis roles.

## Required outcome

A single-system command should validate its input, prepare an isolated,
commit-bound worktree, invoke that worktree's analysis command environment,
wait for completion and report the recorded result and advisory audit outcome.
A batch command should apply the same lifecycle to an explicit input list,
keep durable target/worktree/run bindings, bound concurrent analyses and
reconcile interrupted execution before starting more work.

Implemented interface (adopted in [ADR 125](../../reference/adr/125-analysis-commands-own-preparation-and-bounded-queues.md));
see the [command reference](../../reference/commands.md#commonplace-analysis) for options:

```text
commonplace-analysis analyse <repository-url>
commonplace-analysis batch <url-list> --concurrency 4
```

The skill becomes a thin discovery/invocation/reporting adapter. The command
must also work when no LLM reads the skill. Input validation, execution
requirements and operator-visible results cannot depend on an agent remembering
prose instructions.

Preserve separate authorization for integration and cleanup. Preparation,
acquisition, publication and audit retain their existing guards. Uncertain
effects, unsettled workers, ambiguous sources and exhausted analysis budgets
remain explicit stops; convenience must not silently convert them into retries
or success. Resume existing runs under their recorded method/profile rather
than allocating replacements.

## Starting evidence

The system already has most of the inner execution machinery:

- `src/commonplace/cli/analysis.py`: prepare, run/resume, inspect and explicit
  recovery/integration commands.
- `src/commonplace/lib/agentic_analysis/preparation.py`: prepared worktrees,
  command binding and method checks.
- `src/commonplace/lib/agentic_analysis/workflow.py`: role sequencing,
  corrections, publication and advisory audit invocation.
- `src/commonplace/headless/jobs.py`: Commonplace's worker/attempt policy over
  Workjig records and launches.
- [Current analysis skill](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md):
  the mechanical steps currently performed by the caller.
- [ADR 119](../../reference/adr/119-analysis-workers-launch-through-workjig.md):
  division of responsibility between Commonplace and Workjig.

**Fake-harness execution already exists in Commonplace.**
`tests/commonplace/headless/test_jobs.py` exercises a scripted subprocess
through the Workjig-backed job layer. The slow workflow suite in
`tests/commonplace/agentic_analysis/test_workflow.py` injects a `Harness` that
runs a Python fixture executable, with local Git acquisition and generated
members passing the real checks. Shared setup is in
`tests/commonplace/agentic_analysis/execution_fixtures.py`.

These inspected tests establish an existing route for deterministic workers;
they were not run as part of opening this workshop. Do not infer that Workjig
exports a dedicated mock-harness API or that in-process monkeypatches will
reach a newly prepared subprocess. Establish the supported injection surface
and cross-process delivery in phase 0 of the plan before proposing new runtime
features.

## Scope, coupling and decisions

The [gist-system expansion workshop](../karpathy-gist-system-expansion/README.md)
is the motivating consumer. It owns discovery and its URL queue; this workshop
owns the full command automation, batch execution and fixture-test plan.
There is no dependency on an implementation from another session. Neither
workshop authorizes execution of the other's campaign. Its Tuesday-morning
goal (2026-11-10, operator's intended timezone
not yet fixed) motivates avoiding a second scheduler, but is not permission
to skip fixtures, weaken acceptance or launch paid work. No delivery-duration
estimate is established here.

Implement one single-system command lifecycle around the existing
Workjig-backed workflow, then make batch execution consume that lifecycle.
Do not reimplement analyst roles or create independent authorities for whether
a run or worker is active. Whether an outer Workjig launch record is useful
remains a design choice to resolve against its pinned API and the actual
recovery requirements. Fixture scenarios select outputs by role and attempt;
they do not require separate production worker profiles for each role.

Four simultaneous analyses is the motivating batch setting, not four total
model workers: each analysis currently permits up to three role workers.
Specify both limits visibly. Provider capacity, disk/inodes and external
worktree placement need a preflight decision before a substantial real batch.
No existing evidence directory is owned for cleanup.

Method changes must be committed before new prepared runs use them. Check
current writer ownership and method state when implementation is commissioned;
do not stage or amend another session's edits. Retain existing runs' method
bindings unchanged. Broader model routing belongs to the
[runner execution profiles workshop](../runner-execution-profiles/README.md),
not this work.

## Closure

Close when the single-system and batch commands are implemented under an
explicit implementation commission, the skill and command reference agree,
fixture tests demonstrate completion and interruption/recovery without model
credentials, and the operator has the evidence needed to authorize a real
pilot. A live pilot is a separate commission, not a prerequisite to claiming
only deterministic test coverage. Record remaining semantic-quality and real
provider limits explicitly. Promote adopted contracts and durable decisions,
then remove this workshop and its active entry.
