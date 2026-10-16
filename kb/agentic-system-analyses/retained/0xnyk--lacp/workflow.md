---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LACP workflow account: the planner-to-reviewer team protocol, its token handoff, rejection recovery and recorded completion."
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
---

# LACP workflow report

## Workflow account

The representative workflow is the shipped **Deterministic Team Workflow** for “Add OAuth auth.” It was selected because the runbook names a request and an ordered planner/developer/verifier/tester/reviewer sequence, and executable code implements its handoff checks and final state. It is a manually driven coordination protocol, not an automatic team of agents. The canonical route is [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance). This account extends that route's workflow-specific interpretation rather than declaring a duplicate (SRC-1, `docs/runbook.md`, `bin/lacp-workflow-run`).

Evidence is static implementation and doctrine/design at the [frozen boundary](boundary.md#boundary-and-evidence). Additional coverage comprises the complete `bin/lacp-workflow-run` and `scripts/ci/test-workflow-run.sh`, the deterministic-team section of `docs/runbook.md`, and the workflow dispatcher branch in `bin/lacp`, all under SRC-1. The test script is inspected implementation of checks, not an observed test result. No target code was executed. Actual agent participation, successful OAuth implementation, verification quality and delivered product remain uninspected.

### Request and initial handoff

The operator invokes `lacp workflow-run init` with task and optional project; the dispatcher executes the workflow command (SRC-1, `bin/lacp`, `bin/lacp-workflow-run`). Initialization creates a run directory under the knowledge root's `data/workflows`, containing a shared `CONTEXT.md` with run ID, project, task and an empty Notes section, plus `state.json`. JSON output returns run ID and directory. State begins at planner, with all stages pending and a required plan-act contract whose token is null.

> "status": "in_progress",
> "current_stage": "planner",
> --- `bin/lacp-workflow-run`

No agent is launched or assigned this context by the inspected command. The caller must arrange who does each role's work, how the task/context reaches them and how their result returns. `CONTEXT.md` is prepared text, not proof of model consumption. `advance` reloads JSON state, not that context file. The subsequent handoffs are therefore recorded stage eligibility and caller-provided decisions, not an established transport of plans, code or test evidence (SRC-1, `bin/lacp-workflow-run`; [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance)).

### Planning and development

The caller advances planner with actor `planner` and an optional note. Approval is the default decision. Code checks stage order and actor-string equality, then issues a token derived from run ID, task, current timestamp and note. It retains token, issuance coordinates and optional evidence note; it neither requires nor evaluates a plan document (SRC-1, `bin/lacp-workflow-run`).

> plan_act["evidence_note"] = note or None
> stage["plan_token_issued"] = token
> --- `bin/lacp-workflow-run`

Developer advancement normally requires the same token. The caller can obtain it from `status --json` and pass it with `--plan-token`. This bridges a persisted planner transition to permission to record developer completion; it does not constrain which implementation was made or validate correspondence to a plan. `--allow-unplanned true` explicitly bypasses the token requirement and is recorded. Actor names do not authenticate principals, so distinct role labels establish neither independent agents nor human approvals (SRC-1, `bin/lacp-workflow-run`; runtime's retained role/token evidence in [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance)).

The runbook's developer line omits the token and would encounter the default contract refusal. The shipped test instead reads the token before developer advancement. This is a concrete instruction/implementation mismatch, not evidence that the workflow succeeded in operation (SRC-1, `docs/runbook.md`, `scripts/ci/test-workflow-run.sh`).

> bin/lacp workflow-run advance --run-id "$run_id" --stage developer --actor developer
> --- `docs/runbook.md`

> plan_token="$("${ROOT}/bin/lacp-workflow-run" status --run-id "${run_id}" --json | jq -r '.contracts.plan_act.token')"
> --- `scripts/ci/test-workflow-run.sh`

### Verification and final delivery

After developer approval, current stage becomes verifier, then tester, then reviewer. These three stages are marked as requiring approval, but caller decision values supply the verdict; the command does not run tests, inspect a diff or require result evidence. All stages permit rejection, and omission of `--decision` means approve. The role owner can supply a veto through `reject`; code enforces the transition constraints, not the truth of that judgment. Human versus computational authorship of each decision is unresolved, and this route supplies no expected-answer oracle (SRC-1, `bin/lacp-workflow-run`; [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance)).

> {"name": "verifier", "owner_role": "verifier", "requires_approval": True, "status": "pending"},
> {"name": "tester", "owner_role": "tester", "requires_approval": True, "status": "pending"},
> {"name": "reviewer", "owner_role": "reviewer", "requires_approval": True, "status": "pending"},
> --- `bin/lacp-workflow-run`

Reviewer approval changes current stage to `done` and run status to `completed`. History records timestamp, stage, actor, decision, note, provided token and override flag. The terminal deliverable supplied by this command is persisted completion state and command output, not a verified OAuth implementation, merged change or returned agent synthesis (SRC-1, `bin/lacp-workflow-run`).

> else:
>     state["current_stage"] = "done"
>     state["status"] = "completed"
> --- `bin/lacp-workflow-run`

The harness's configured execution/verification route is separate: [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) describes actual runner completion and verification checks. Nothing in the inspected workflow command calls that harness. Joining the two would invent an automatic completion check for this team protocol (SRC-1, `bin/lacp-workflow-run`).

### Rejection and recovery

A missing or wrong developer token raises an error before history/state are written. Wrong actor or out-of-order stage likewise fails before a transition. Recovery from these protocol errors is caller resubmission with the accepted actor, stage and token, or deliberate use of the override; there is no automatic recovery agent (SRC-1, `bin/lacp-workflow-run`, `scripts/ci/test-workflow-run.sh`).

> if not provided_plan_token:
>     raise SystemExit("plan->act contract violation: missing --plan-token for developer stage")
> if provided_plan_token.strip() != expected_token:
>     raise SystemExit("plan->act contract violation: invalid --plan-token for developer stage")
> --- `bin/lacp-workflow-run`

An explicit rejection differs: it persists rejected stage status, blocked run status and a history entry, keeps the same current stage, prints decision JSON and exits 2. With shell `set -e`, the Python failure exits before the following shell status-rendering block. The caller can later approve the same stage because no blocked-state guard prevents this. Such approval completes that stage and advances, but does not restore run status to `in_progress`; `blocked` remains until final reviewer approval sets `completed`. Therefore status alone can continue reporting blocked during resumed progression (SRC-1, `bin/lacp-workflow-run`).

> if decision == "reject":
>     stage["status"] = "rejected"
>     state["status"] = "blocked"
> --- `bin/lacp-workflow-run`

> if decision == "reject":
>     raise SystemExit(2)
> --- `bin/lacp-workflow-run`

No product rollback or reassignment is performed in this branch. A reject note can retain a reason, but the command does not deliver it to a developer, reopen an earlier completed stage or verify that a correction was made. External participants own that recovery. The inspected test covers wrong actor, missing/wrong token, successful transition sequence and explicit bypass, but not this reject/reapprove behavior; those are static branch findings rather than observed recovery (SRC-1, `bin/lacp-workflow-run`, `scripts/ci/test-workflow-run.sh`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance)

Workflow-specific delivery criterion: final reviewer approval records `done`/`completed`; it does not establish a delivered software result. The selected OAuth example requires a token handoff missing from the runbook but supplied by the source test. Rejection preserves the current stage for resubmission, while intermediate approval after rejection leaves run status blocked until final approval. The Workflow account retains the supporting passages and distinguishes caller-owned task recovery from code-owned transition recovery (SRC-1, `bin/lacp-workflow-run`, `docs/runbook.md`, `scripts/ci/test-workflow-run.sh`).
