---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Claude Workstream Kit workflow: the shipped three-session greeting-script scenario, bounded delegation, held gates and local archival delivery."
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
reviewed-boundary: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
---

# Claude Workstream Kit workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped greeting-script acceptance scenario: create a workstream in one session, implement two tasks through worker/verifier delegation in another, then approve and close in a third. It is selected because a single executable driver connects these stages, supplies concrete acceptance criteria and inspects the retained result. This is not a workflow assembled from unrelated capabilities. The driver is [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver); its constituent model-mediated operations are [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet) and [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle).

Added workflow inspection read the complete frozen `tests/va3-acceptance.sh`, `.claude/skills/workstream-work/SKILL.md`, `.claude/agents/worker.md`, `.claude/agents/verifier.md`, `.claude/skills/workstream-close/SKILL.md` and `.claude/skills/workstream-extract/SKILL.md`. SRC-1 supplies implementation evidence for the driver and doctrine/design for the model instructions. No driver, target, test or model was executed. Successful handoffs and delivered artifacts therefore remain unobserved. Comments describing earlier runs are attributed reports, not this analysis's observations.

### 1. Request, setup and creation handoff

The test maintainer starts the shell driver. It creates a fresh temporary Git repository, installs the kit from the checkout and commits the installation before calling Claude Code. Each model call uses `claude -p --dangerously-skip-permissions`; the scenario therefore does not test ordinary interactive permission grants. Claude Code owns actual model execution and subagent invocation. SRC-1, `tests/va3-acceptance.sh`; see the execution boundary in [RT-CMP-claude](runtime.md#rt-cmp-claude).

Session A receives the purpose, type/name, three deletion criteria and initial backlog. The product must be `scripts/hello.sh` printing the prescribed greeting with exit 0, a passing `test/smoke.sh`, and both files committed. The backlog names two Build tasks and an unchecked user checkpoint. The prompt tells the model to read the creation skill, templates and state rule, treats the supplied interview answers as review approval, and requests committed state. The shell then checks that the workstream file exists and that implementation has not auto-started. These checks establish the evaluator's intended separation between approving a plan and starting work; without a run they do not establish compliance. SRC-1, `tests/va3-acceptance.sh`.

The persistent handoff to Session B is repository state, not Session A's conversation: [RT-OBJ-active](runtime.md#rt-obj-active) selects the resume target and [RT-OBJ-workstream](runtime.md#rt-obj-workstream) holds tasks and criteria. The next prompt explicitly requires both files to be read. Host reload wiring is separately described by [RT-RTE-session-reload](runtime.md#rt-rte-session-reload); the scenario need not rely on that hook alone for detailed task delivery.

### 2. Work selection and bounded implementation

Session B receives a request to work the Build phase, derive and state its goal, delegate both implementation tasks, verify before acceptance, cite evidence, stop at the unchecked gate and commit work/state. It is explicitly a substitute for, not an exercise of, the native interactive goal mechanism:

> this non-interactive session stands in for the /goal session, so proceed under that condition.
> --- `tests/va3-acceptance.sh`

In ordinary operation the work skill first rechecks task premises against real artifacts, including scope, destination, previous closures and competing live ownership. It then derives a resumable critical-path unit and leaves goal arming to the user. That policy is [RT-RTE-work-goal](runtime.md#rt-rte-work-goal). The fixture supplies a narrow two-task unit and unattended authorization; its source does not show how any actual model resolved these preliminary checks. SRC-1, `.claude/skills/workstream-work/SKILL.md`, `tests/va3-acceptance.sh`.

The foreground model owns packet construction and scheduling. Each worker must receive the objective, file scope, verification command and stop conditions; originating specifications must be passed verbatim rather than paraphrased. The packet defines the allowed edits and expected result, while the worker returns changed files, actual verification output and adjacent findings. A fresh verifier receives the same specification, independently reads files and reruns verification, and returns PASS/FAIL with per-requirement evidence. These handoff contracts are already established in [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet), not new workflow referents.

Verification is sequenced to avoid mistaking the next worker's edits for scope creep in the preceding packet:

> Run it after the packet's worker has finished and before the NEXT packet's worker starts, or scope any "X is the only new file" check to named paths
> --- `.claude/skills/workstream-work/SKILL.md`

The foreground model, not the verifier, admits task completion. It is instructed to verify returned findings and limitations and attach evidence before checking a task. The host implements separate agent contexts; the kit specifies selected inputs and compact returns, not an independently inspected context-isolation mechanism. SRC-1, `.claude/skills/workstream-work/SKILL.md`, `.claude/agents/worker.md`, `.claude/agents/verifier.md`.

### 3. Verification, rejection and recovery

A malformed packet must return immediately for missing information; out-of-scope work must return to the orchestrator rather than expand its own authority. In-scope verification failure has a bounded repair path:

> If verification fails and the fix is within scope, iterate up to twice; then stop and report the failure honestly. A truthful failure report is a successful packet outcome.
> --- `.claude/agents/worker.md`

The verifier diagnoses gaps but does not repair the reviewed work:

> Verdict format: PASS or FAIL, then per-requirement findings, each citing its evidence (file:line, command output). For FAIL, name the specific gap, not a general impression.
> --- `.claude/agents/verifier.md`

Thus a failed worker or rejected result returns control to the foreground model. The work skill permits committed blocker evidence instead of forcing success, with scoped commits supporting reversibility. It does not prescribe an automatic unlimited verifier-failure loop. User gates remain user decisions; these are model-facing policies rather than software-enforced vetoes over every file write. SRC-1, `.claude/skills/workstream-work/SKILL.md`; [RT-RTE-work-goal](runtime.md#rt-rte-work-goal), [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet).

After Session B, the shell independently runs the smoke test, checks that the Build gate remains unchecked and checks the completed second task's note block for an evidence-shaped string. These are narrow output checks. They do not mechanically establish that both requested worker packets and fresh verifiers actually ran, or that every cited commit substantiates its claim. The prompt requests those operations; the assertions are not a delegation transcript oracle. SRC-1, `tests/va3-acceptance.sh`.

### 4. Closure authorization and archival handoff

Session C's prompt supplies the user's Build-gate approval and conditional closure approval: every deletion criterion must genuinely have evidence. It asks for narrative and criterion evidence in output, completion tasks, extraction and archival. Unlike ordinary interactive closure, this scenario supplies the approval contribution before the model presents its evidence. Unsatisfied criteria still require stopping. SRC-1, `tests/va3-acceptance.sh`; [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle).

The close skill owns the narrative, criteria gate and archive sequence; it calls the extract skill to disposition Learnings/Open Questions, verify their destinations and move durable artifacts outside `.state/`. This skill call is a procedural handoff, not evidence of a separate spawned agent. For this throwaway scenario the prompt narrows extraction to applying locally or dropping with rationale, never cross-project handoff. Closure additionally checks inbound dependencies and repoints live references before deleting their old home. SRC-1, `.claude/skills/workstream-close/SKILL.md`, `.claude/skills/workstream-extract/SKILL.md`, `tests/va3-acceptance.sh`.

The archival order matters: set `status: done` and append the ledger entry; commit that final record; annotate `ws/greeting-script`; remove the directory; reset ACTIVE.md only if it points there; then commit again. The tag retains the closed record while the working tree retains the deliverable. Remote publication is a separate user gate under the close skill, not implied by a local tag or closure approval. A repository with no remote skips that push. The temporary fixture initializes a local repository without adding a remote; this scenario's terminal product is local. SRC-1, `.claude/skills/workstream-close/SKILL.md`, `tests/va3-acceptance.sh`.

### 5. Delivery verdict and held path

The shell checks for the archive tag, `status: done` in its snapshot, a ledger entry, directory removal, reset pointer, clean working tree and a still-passing deliverable. This makes delivery broader than a final chat claim: the scenario expects usable committed work and a resolvable local archive after removal of live state. It still samples specific patterns rather than proving exhaustive extraction or semantic correctness. SRC-1, `tests/va3-acceptance.sh`.

A gate-held closure is treated separately from successful archival. The code classifies it from a remaining workstream directory and non-`None` content under ACTIVE.md Blockers. It marks archive assertions HELD rather than executing their normal checks; other checks, including clean tree and surviving deliverable, still run. Final precedence is failures → exit 1, otherwise held → exit 2, otherwise all checks pass → exit 0. The held predicate identifies a recorded hold, not whether that hold was substantively justified. SRC-1, `tests/va3-acceptance.sh`.

The logs and fixture remain for maintainer inspection. The driver prints closing observations, because assertions alone can miss guidance defects reported in the model's output. Its comments request inspection before deleting the fixture; that is an evidence-to-maintainer handoff, not automatic admission of changes into the kit. Source inspection establishes this recovery and review opportunity, not that anyone used it or that future behavior improved. SRC-1, `tests/va3-acceptance.sh`; [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver).

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

#### On [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet)

Workflow sequencing: in the selected scenario Session B must delegate both Build tasks and verify before accepting. The work skill sequences each packet's verification before the next worker, unless scope checks name paths narrowly enough to avoid interference. Worker failure can end in an honest bounded return; verifier failure supplies a gap for foreground disposition, not a self-executing repair. Source instructions establish the requested progression, not exercised delegation.

#### On [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)

Workflow authorization: the fixture pre-supplies creation approval and later Build-gate approval, with closure approval conditional on criterion evidence. Its extraction destination policy is local application or explicit dropping, not handoff. Local archival is the selected terminal path; publication remains a separate decision where a remote exists.

#### On [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver)

Workflow acceptance limit: artifact assertions do not independently validate all requested worker/verifier handoffs. The held predicate distinguishes recorded nonterminal closure from archive success without judging the gate's merits. Preserved model output and temporary history enable subsequent maintainer investigation; their existence alone does not establish that investigation or downstream admission occurred.
