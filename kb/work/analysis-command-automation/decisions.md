# Interface and seam decisions

Inspected baseline: `a0c12bcd3d40eceb7cc088fe26500cc0ec6c0f26`.

## Ownership map

| Obligation | Owner / delivery |
| --- | --- |
| Explicit target, locator plausibility, local/document route, option validation | analysis CLI → automation intake; no acquisition probes |
| Committed method, startup files, branch freshness, isolated install | preparation API; coordinator records the chosen commit and destination before setup |
| Allocation crash window | worktree API: allocation-key journal under run state; allocation is idempotent, not another run request |
| Workflow roles, budgets, source guards, publication | existing workflow in a subprocess using the prepared command environment |
| Worker launch truth, unsettled reservations, acknowledgement | existing headless consumer over Workjig 0.3.1; not the batch status file |
| Receipt, stop, audit, evidence reporting | pinned child emits a structured result from inspect; coordinator retains it |
| Queue, bindings, exclusive controller, bounded analyses | automation module; single target is a one-item queue |
| Retry, acknowledgement, reset, integrate, removal | existing explicit commands / separate operator authority; never automatic |
| Profile and fake workers | one recorded run profile; executable shim on PATH emits real Pi protocol with fake model provenance; absolute scenario in inherited environment |

## Selected interface

- `analyse SOURCE`: remote repository locator by default. `--source-kind local`
  requires an existing absolute-resolved path; `--source-kind documents` requires
  explicit `--system` and `--source-identity`. These preserve the boundary-owned
  non-Git capture route. GitHub identities retain code-owned acquisition.
- `batch FILE --concurrency 4`: newline remote locator list or JSON list of
  target objects with `source`, optional `source-kind`, `system`,
  `source-identity`, `source-revision`. Reject normalized duplicate identities
  before effects; triage rationale is not accepted into packets.
- `resume CONTROLLER` resumes recorded bindings, not intake. Completed targets
  are reconciled, not rerun. Stopped runs resume only when explicitly selected
  with `--target IDENTITY`; pending targets may continue after reconciliation.
- `report CONTROLLER` is read-only. JSON schema `commonplace.analysis-controller.v1`
  includes target bindings and nested pinned-child inspection; human summary on
  stderr. Exit 0: all published/local; 2: ordinary stops; 1: command/preparation
  failures; 3: interrupted/operator attention or pending work.
- Default durable state: ignored `.commonplace/worktrees/controllers/<uuid>/`.
  `--state` and `--worktree-root` permit explicit external placement. Preparation
  destinations are selected and recorded before effects; never reused by retry.
- The selected commit and profile are validated before creating controller state.
  Default remains `pi-sol`, three role workers per analysis, 10800 seconds per
  launch. Four analyses permit twelve role workers, plus advisory auditors after
  their analyses finish. Concurrency is over whole analyses including audit.

## Recovery and process ownership

Use ordinary subprocess ownership, not an outer Workjig call. Workjig command
calls require output files and classify missing outputs as launch outcomes;
that would introduce another retry/acknowledgement authority around the same
workflow. Workjig remains the sole worker-launch authority.

Controller and target leases use POSIX advisory file locks. Pass each target
lease descriptor into its prepared child so an orphan child retains ownership
through the controller's death. Never infer settlement from missing PIDs.
SIGINT/SIGTERM stop new claims and drain existing children, without forwarding
signals to their independent sessions. Abrupt death leaves effect intents;
restart first checks leases, preparation/allocation journals, worker reservations
and audit status. Unknown preparation, missing allocation evidence, unsettled
workers and interrupted audits require operator attention and pause new claims.
No automatic acknowledgement, retry or replacement allocation. Explicit resume
may continue a discovered settled run, under the original method/profile. The
coordinator does not import the child's workflow version or change cwd.

## Direct API observations

Workjig 0.3.1 exposes `CommandWorker`, `Run.call`, `Run.unresolved_launches`,
`hold`, `busy`, and explicit `acknowledge_stopped`. Its harness cleans owned
process groups before settling launches; a controller death can leave reserved
or running launches. Commonplace's existing scripted workflow tests provide
member generators and a frame-reading harness. No upstream mock API is needed.
The production harness already resolves its executable from PATH and records
served models from protocol events, so cross-process fixture injection needs
no production fake option or per-role profile expansion.

Inspection found that preparation's skill-documented origin startup and
behind-default-branch checks were not called by `prepare_worktree`. ADR 118
had deliberately removed them. This commission explicitly requires those
checks; ADR 125 adopts the stricter intake policy and marks ADR 118 amended.
They are implemented in the preparation API with regressions. This is an
origin intake policy, not a claim that origin context reaches a worker.

## Limits before a pilot

Fixtures establish mechanics, not source interpretation, provider behavior or
capacity. POSIX local-filesystem locking is required; network filesystem lock
semantics are not established. Before a substantial live batch, the operator
must choose a committed method, provider capacity, disk/inode budget and
worktree placement. No automatic storage cleanup or live preflight probes.
Interrupted advisory audits and uncertain publication/acquisition effects
remain manual recovery cases. Automation neither clears them nor launches a
replacement audit/run. Older worktrees keep their original commands; new
controllers require a committed method carrying the new execution protocol.
The workshop stays open for independent parent review before closure.
