# Implement an independent headless workflow base

Build a standalone Python package that runs ordinary workflow code against
headless harnesses, records delivered results and supports bounded retries
and resumption without Commonplace or an orchestrator agent.

Commissioned as a plan by the operator on 2026-10-19. The operator explicitly
requires implementation independent of the work in
`/home/zby/llm/commonplace-headless`. The
[responsibility matrix](./responsibility-matrix.md) supplies the ownership
boundary. The operator authorized implementation on 2026-10-19 with Sol
workers and parent review. This does not authorize changing live installations
or publishing a package externally.

## Independence and scope

Implement against the contract below and independent acceptance tests. No
phase waits for the headless branch, imports its code, requires its tests,
or assumes its rollout succeeds. Existing experiments may inform later review,
but neither their APIs nor their behavior are the specification.

Treadle is the operator-named predecessor. Package naming and repository
placement remain open; decide them at setup without making compatibility
with Treadle's earlier step-program protocol a requirement. Use a standalone
package directory and its own dependency/test environment. If placed in
Treadle, preserve unrelated work and record which existing project instructions
apply before writing. Do not modify the headless branch or Commonplace runtime
as part of implementation.

The first release targets local headless subprocesses on Linux. It needs no
Git repository in its execution directory. It includes no KB types, artifact
publication, worktree preparation, environment pinning, containers, managed
hosting, general scheduler, daemon or orchestrator-agent command protocol.
Do not add Temporal or Pydantic AI merely because the predecessor used them.

## Initial execution contract

These are proposed implementation defaults within the agreed scope. Resolve
any contradiction exposed by the independent example before stabilizing the
API; record the change and its acceptance consequence here.

- A **run** has a caller-selected record directory and working directory.
  One controller owns its records at a time. Opening a run does not certify
  the working environment; the caller maintains conditions for valid reuse.
- A **call** has a caller-supplied stable identity, task text, named input
  contents, required and optional output names, worker configuration and
  execution limits. Reuse requires both the same call identity and matching
  declared request material. Different identities can request independent
  executions of identical prompts.
- A **launch** is one invocation of a harness process. Every launch has fresh
  input, prompt and output paths. Retries never collect an earlier launch's
  files. Runtime-managed names must remain inside their assigned directories;
  this does not sandbox the worker's other actions.
- A **delivered result** retains the output contents, request identity and
  available execution provenance. A successful exit without required outputs
  is incomplete. A worker's explicit inability to finish is a separate
  outcome. Neither a successful exit nor cached delivery means content passed
  the caller's checks.
- Completed result records are committed atomically. Missing or corrupt
  records fail visibly; they are not silently interpreted as accepted output.
  Result identity covers named inputs, task, outputs and worker configuration;
  it does not cover undeclared filesystem reads or ambient configuration.
- The workflow reruns ordinary control flow and reuses delivered results
  within this run. Its checks run again against caller-selected snapshots.
  Changes to workflow logic or its ambient environment can require a new run.
  Cross-run reuse is outside scope.

### Attempts, stopping and interruption

Start with one launch per call unless the caller explicitly supplies a larger
limit and a bounded retry policy. Distinguish execution retries from content
corrections: a correction is a new workflow call carrying prior content and
feedback, bounded by the workflow's own loop.

Persist a launch reservation before starting the process. Each reservation
spends one launch allowance, even if interruption leaves it uncertain whether
the process started. This conservative rule bounds starts without promising
exact execution counts. Recorded timeouts and incomplete outputs spend their
reservation; budget consumption survives restart. Do not silently classify
every nonzero exit as transient. Recognized usage limits stop without an
automatic relaunch; retain the reservation and reason.

On normal completion or handled timeout, collect or terminate owned processes
as appropriate before returning. For parallel groups, wait for all calls to
settle before reporting group failure; first-failure cancellation is deferred.
Test process-group cleanup, including children that outlive their leader.

An unresolved launch reservation after abrupt controller loss stops automatic
resume. Report the launch evidence and require the operator to establish that
the old worker has stopped before explicitly allowing another launch within
the remaining allowance. Do not guess process ownership from a reused PID.
Specify a small recovery operation at phase 3; no distributed recovery or
exactly-once side-effect guarantee is intended. Workers that perform external
effects require caller-owned safeguards.

## Implementation phases

Each phase produces a reviewable change and evidence for its stated exit
condition. Later phases may reshape provisional interfaces; do not carry
compatibility shims without a consumer.

### 1. Package skeleton and executable contract

Create the standalone package, test setup and a small design document carrying
the execution contract. Define plain request, worker, result and failure
records. Keep module boundaries around harness invocation, run storage and
workflow helpers; choose names from their responsibilities rather than the
old engine's internals.

Build a deterministic fake harness executable that reads the actual supplied
prompt, consumes named files and writes outputs. It must support deliberate
failure, partial output, delay and worker-reported problems. It is a test
fixture, not an alternative production execution path.

Exit: a test launches this subprocess in a temporary directory without Git or
Commonplace, receives one output and identifies the process invocation that
produced it. The package can be installed into a fresh environment.

### 2. One reliable call

Implement request rendering, fresh launch directories, required-output
collection, explicit outcomes, process timeout handling and provenance
collection. Treat unavailable harness evidence as unknown. Separate command
construction from process execution so adapter behavior can be tested without
real model calls.

Exit: tests distinguish successful delivery, missing output, worker problem,
nonzero exit and timeout. A failed launch that leaves outputs or a problem
file cannot contaminate a later successful launch. Collected content is tied
to the correct invocation. Output-name escape attempts are rejected.

### 3. Run records, bounded retries and resume

Implement the run lock, request identity, atomic result storage, launch
reservations and explicit recovery for unresolved reservations. Add bounded
execution retry/backoff with injectable timing for tests. Keep execution
records authoritative; a readable event log may explain them but must not
silently disagree about whether a result is reusable.

Exit: a restarted process reuses completed results, preserves spent allowances
and rejects concurrent controllers. Inject interruption before launch, during
execution, before result commit and after commit. Each restart either reuses
a committed result or reports the documented uncertainty; it never resets a
budget or silently adopts an unrecorded output. Changed declared inputs miss
reuse; different call identities remain independent.

### 4. Ordinary workflow composition

Add bounded parallel execution and an example workflow with two independent
file-producing jobs followed by a combining job. The example uses a caller
check and a bounded correction loop, and resumes after a deliberate stop.
It snapshots sibling contents before checks whose result depends on them.

Keep correction construction in the example initially. Extract a generic
check-and-retry helper only if the example shows useful repeated mechanics;
it must accept caller checks and feedback construction without interpreting
Markdown refusals, types or domain verdicts.

Exit: opposite worker completion orders produce the same declared comparison
inputs and acceptance decisions. Tests establish the launch limit, successful
resume without duplicate completed work, and exhaustion of both launch and
workflow correction budgets. No scheduler state is introduced to implement
branches or loops.

### 5. Real headless adapters

Target Codex, Claude Code and Pi, adding them one at a time. At implementation
time, inspect the installed CLI's help and authoritative documentation for
invocation, noninteractive behavior, configuration loading and available
execution evidence. Do not copy unverified flags from an old experiment.

Adapters translate the same request/result contract. Model and permission
choices remain explicit caller configuration. Record tested CLI versions and
the evidence each adapter can retain. Do not overwrite user credentials or
project settings to make a probe pass.

Exit per adapter: a bounded real invocation reads a supplied input, writes a
named output and returns attributable evidence; repeating the call reuses its
record without another model launch. Test failure parsing with captured or
synthetic fixtures and distinguish that coverage from observed real failures.
An unavailable harness or credential blocks only that adapter's support claim,
not the package or other adapters. Do not deliberately exhaust usage quotas.

### 6. Independent release acceptance

Build and install the package into a clean environment outside its checkout.
Run the ordinary-file example and deterministic acceptance suite there.
Document the public call contract, supported harnesses, caller responsibilities,
retry accounting, resume/recovery operations and absence of environment
isolation. Document how task prompts expose file paths to each worker.

Exit: the standalone package and example satisfy the matrix without
Commonplace installed, a Git checkout, or the headless branch. Record test
coverage and real-adapter limitations. Prepare the release artifact; publishing
it externally is a separate action. Commonplace integration is a later
consumer project and is not this release's acceptance gate.

## Decisions and stop conditions

- At setup, record the selected package home and project instructions before
  mutations. If placement would replace an existing implementation or collide
  with another worker, return that placement decision to the operator while
  continuing contract work in this workshop.
- At phase 3, demonstrate the interruption contract with process-level tests
  before building higher-level convenience APIs. If it needs a daemon or
  general scheduler, return the recovery requirement for reconsideration.
- At phase 4, use the example to decide whether the check helper earns a place
  in the base. Do not add it solely to resemble the headless branch.
- At phase 5, narrow supported adapters to observed capabilities rather than
  broadening permissions or claiming untested compatibility.

Record completed phases, decisions, inspected versions and exact validation
commands in this workshop until package documentation becomes their durable
home. A failed probe narrows a support claim or reopens the named contract;
it does not authorize adding excluded infrastructure.
