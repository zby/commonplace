# Implement command-owned analysis execution and test it with fixtures

## Intent and acceptance

Move mechanical preparation, execution and reporting out of the supervising
agent and into Python. Add bounded batch execution using the same single-system
lifecycle. This workshop covers the whole change; no implementation or handoff
from another session is assumed.

The [README](./README.md) fixes authority and scope. The operator has authorized implementation, tests and commits under the
[execution record](./execution.md), including parent verification and up to
three fresh implementation attempts if substantial redesign is needed. This
is not permission to launch the campaign. Keep the existing Python analysis
workflow, verification rules and Workjig-backed worker launches. Do not build
a second implementation of the analyst roles.

Acceptance: one supplied system or explicit target list can be run without a
supervising model. Execution retains method/source bindings, accurate outcomes
and supported recovery. Interruption must not silently allocate replacement
analyses or relaunch potentially live workers. Integration and cleanup remain
separately authorized.

## Phase 0 — establish interfaces and reusable seams

Read the owning collection contract, method-maintenance instruction, design
brief, current skill and direct CLI/preparation/workflow/headless consumers.
Map every mechanical skill obligation to its code owner, and distinguish
operator decisions from automatable steps. Inspect current implementation
before editing; this plan does not freeze a stale interface.

Inspect the lockfile-pinned Workjig worker/command APIs and the existing fake
harness suites. Decide whether an outer command launch benefits from a Workjig
record or ordinary subprocess ownership with durable lifecycle bindings.
Do not introduce competing records of whether a run or worker is active.
No dedicated Workjig mock API is presumed. An upstream change, if genuinely
needed, requires separate repository authority.

Resolve the proposed command surface, source-input model, machine-readable
result schema, durable binding location, aggregate exit codes, resume behavior
and interruption policy before implementation. Provisional spellings:

```text
commonplace-analysis analyse <repository-url>
commonplace-analysis batch <url-list> --concurrency 4
```

Preserve supported local/snapshot source routes or obtain an explicit decision
about their interface; do not silently reduce the existing source model to
GitHub only. Preserve the current worker-profile default and explicit overrides.

**Decision point:** record a compact interface/seam map and any unresolved
consequential choice here before implementation. Prefer existing public seams;
do not scrape unstable files or console lines to avoid defining a needed API.

## Phase 1 — single-system command lifecycle

Implement under the later commission, with these responsibilities:

1. Validate the caller's source and options before effects. Do not infer a
   system from prior reports, ambient checkouts or triage conclusions.
2. Prepare an isolated worktree at the selected committed method. Preserve
   startup-file and branch-freshness checks, revision-selection authority,
   ready preparation records and command-environment binding.
3. Run the existing workflow in that worktree's command environment. Use
   subprocess argument arrays and explicit `cwd`/environment; do not import
   a second method version into a long-lived coordinator or use global
   `chdir` for concurrent targets. Keep the prepared environment unchanged.
4. Persist target, method, preparation/worktree and allocated run bindings at
   effect boundaries. Resolve the crash window between allocation and outer
   binding update with a supported allocation/discovery protocol. Parsing an
   unflushed run-ID message is not durable ownership.
5. Wait and return a machine-readable result plus an operator summary with
   receipt, disposition, evidence paths and advisory audit status/limits.
   Distinguish verified publication, local blocked/out-of-scope completion,
   analysis stop, command failure and interrupted/uncertain execution.
6. Support resuming the recorded run with its original method/profile and
   existing recovery interfaces. Do not automatically retry, acknowledge,
   integrate, clean up or replace stopped runs. Preserve failure evidence.

**Decision point:** demonstrate the complete single-system route with scripted
workers before adding batch scheduling. Resolve missing lifecycle interfaces
in their owning module rather than introducing another wrapper around them.

## Phase 2 — deterministic harness fixtures

Reuse the scripted harnesses in
`tests/commonplace/agentic_analysis/test_workflow.py` and
`tests/commonplace/headless/test_jobs.py`, with local-source/prepared-checkout
helpers in `tests/commonplace/agentic_analysis/execution_fixtures.py`.

Use **one fake harness for the run**, with a scenario selecting responses by
role and attempt. Separate step responses do not require separate production
worker profiles. Record fake execution honestly rather than reporting it as
a real served model.

```text
test creates temporary scenario + response generators
  → command receives test harness executable/configuration
  → workflow launches the scripted harness through Workjig
  → harness reads role, inputs and output paths from the real frame
  → harness selects the role/attempt response and writes requested outputs
```

Define and implement the smallest test injection seam that reaches newly
prepared subprocesses without bypassing binding or method checks. In-process
monkeypatches alone do not cross that boundary. A test-only executable/profile
adapter may suffice; a public production `--fake` option is not required.
Pass an absolute scenario path and independent per-run mutable state.

Scenarios cover success, verifier rejection/correction, worker problem,
missing output, nonzero exit, usage limit and delayed completion. Existing
valid-member generators can supply actual run IDs, source revisions and
references to earlier members. Fail on unexpected roles or attempts rather
than silently substituting a passing response.

Keep local Git acquisition, temporary checkouts, counters and barriers
independent per test. Reuse only immutable baselines; invalidate cached derived
fixtures when method inputs change. Mock model execution and remote acquisition,
not validators, binding checks or publication acceptance. Extract shared
fixture helpers only for demonstrated reuse, not a speculative fake-agent
framework.

## Phase 3 — bounded batch execution

Use one queue, not four fixed sublists. Call the single-system lifecycle;
do not duplicate preparation, workflow roles or recovery policy.

- Validate the explicit input list before effects. Normalize identities and
  define duplicate handling. Keep triage rationale outside analyst packets.
- Persist input identity and per-target method/worktree/run/status bindings.
  Enforce exclusive controller ownership; a second controller cannot claim
  the same pending targets.
- Bound simultaneous analyses; four is the motivating setting. Expose the
  separate per-analysis role-worker bound: four analyses with three workers
  each allow up to twelve role launches, not four overall.
- On restart, reconcile recorded effects and process ownership before claims.
  Missing PIDs alone do not establish that descendants stopped. Unknown or
  unsettled effects require operator attention, not automatic replacement.
- Allow independent targets to continue after an ordinary recorded analysis
  stop. Pause new launches on shared method/preparation failures or uncertain
  ownership. Do not add an automatic retry layer.
- Report pending, active, published, local-complete, stopped and
  operator-attention outcomes separately. A stopped target is not success.

Choose signal behavior explicitly: drain owned children after stopping new
claims, or terminate/reap owned process groups and retain unsettled records
for reconciliation. Test the chosen policy. Do not assume terminating the
controller terminates every child.

**Decision point:** establish restart, exclusive ownership and interruption
acceptance before a real batch. Storage/inodes, external worktree placement,
provider capacity and the committed method need preflight; fixtures do not
establish live capacity.

## Required consumer tests

Map these cases to existing coverage first. Reuse consumer tests rather than
duplicating Workjig's internal launch-mechanics suite.

| Case | Observation required / regression prevented |
| --- | --- |
| Complete single-system route | Actual command reaches fake workers through preparation and subprocess execution; real checks yield the correct method/profile/source/result/audit bindings. No model credentials or network. |
| Invalid input and preparation refusal | No analysis launch; failed preparation evidence retained; no automatic alternate revision or destination. |
| Local completion versus publication | Blocked/out-of-scope completion does not masquerade as retained publication. |
| Role-specific responses and correction | One harness supplies distinct step outputs and a verifier-triggered correction; real acceptance checks remain active. |
| Audit failure/skip | Audit limits reach the caller without turning the advisory audit into an acceptance gate. |
| Supported resume | Fresh controller resumes the same run; launch counters prove unchanged answered requests are replayed rather than launched again. |
| Crash around allocation | Interrupt after the effect and before binding update; restart discovers the existing allocation or stops as uncertain, never allocates blindly. |
| Unsettled child | No automatic acknowledgement/relaunch; owned process cleanup or draining follows the documented signal policy. |
| Environment binding | Prepared commands execute the pinned code; neither fixture injection nor resume silently changes method/profile. |
| Four-slot scheduling | At least five barrier-controlled targets show no more than four active analyses; a released slot starts the next target without waiting for unrelated long jobs. |
| Mixed outcomes | Publication, local completion, ordinary stop and uncertain effects retain distinct statuses and the declared continuation/exit policy. |
| Batch ownership and restart | Concurrent controller is refused; restart preserves completed bindings and reconciles active/uncertain items; duplicate inputs cannot create duplicate jobs. |
| Cross-target isolation | Opposite completion orders cannot swap receipts, logs, source identities or run/worktree bindings. |
| No implied integration or cleanup | Origin `main` is not merged/staged and worktrees remain after success or failure. |

Use representative complete-workflow fixtures for real wiring, with smaller
scripted command fixtures for scheduler/interruption permutations. Record the
layer each test exercises. A fake command alone does not establish that the
real command passes harness configuration into its child process.

## Phase 4 — skill, documentation and installation

Reduce the canonical skill to target selection, invocation, authority and
reporting unresolved decisions. It must not retain a second manual procedure
for the mechanical lifecycle. Update CLI help, command reference and affected
skill projection, installed stub, scaffold and package surfaces together.
Retain low-level recovery commands where consumers need them. Follow the
method-maintenance route for any required ADR or changed execution contract;
this plan does not adopt those contracts itself.

Follow [test selection](../../../tests/README.md): general plus affected analysis
and headless suites, including relevant slow end-to-end tests. Include docs
and installation consumers when their interfaces change; dependency/packaging
changes require the broader installation checks and editable-tool setup.
Validate KB changes, run lint and review the exact status/diff. Commit the
method before new prepared runs use it; do not change existing run bindings
or stage another writer's work.

## Pilot handoff and stopping point

Return actual command examples, result/resume contracts, fixture evidence,
remaining limitations and capacity/storage requirements. Deterministic tests
establish execution/recovery behavior, not analytical quality or real-provider
behavior. Obtain separate authorization for a small live pilot before the
gist campaign. Large-batch execution, integration and cleanup remain separate
operator decisions. Stop at unmet authority, environment or recovery requirements
rather than inventing a bypass to meet the calendar target.
