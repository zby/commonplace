---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Amanuensis workflow report: a requested subsystem survey from scoped delegation through adversarial revision and conspectus delivery."
run-id: AAS-2026-11-08-amanuensis-b3a8e3e53488-01
reviewed-boundary: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
---

# Amanuensis workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped `survey [subsystem]` route. It is selected because it joins scoped reading, optional phase delegation, evidence admission, adversarial correction and publication in one explicit coordinator procedure. It is not reconstructed from unrelated tool capabilities. The baseline is [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle); the workflow-specific adversarial subroute is [WF-RTE-adversarial-review](#wf-rte-adversarial-review). This account describes requested model behavior and inspected implementation, not a successfully executed survey. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/subsystem-survey.md`.

Added SRC-1 coverage comprises the complete subsystem-survey, scope, adversarial and packaging references; the opening structural and concern-process sections of `phase-2-structural.md` and `phase-3-concerns.md`; `mcp-server/src/tools/findings.ts`'s status-update handler; and `requireOverturnEvidence` in `mcp-server/src/invariants.ts`. These supply doctrine/design and implementation respectively. No receipts, target executions or external sources support operational claims here. Host scheduling and actual phase-agent inputs remain outside the inspected implementation.

### Request, orientation and handoff

The coordinator first binds and verifies the chat workspace through `get_project_info`, checks autoprogress, and identifies cold or warm state. A named subsystem controls scope; warm state and current status determine the next phase rather than restarting all reading. Unreachable MCP or workspace mismatch stops the workflow. A changed canonical HEAD prompts change detection. These are model-facing instructions backed by the narrower binding enforcement in [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), not guarantees that a host obeys every instruction. SRC-1: `.claude/skills/amanuensis/SKILL.md`.

The subsystem procedure then starts a survey session, captures one survey SHA and prescribes an artifact lock around each phase. The handoff supplies the phase reference, subsystem ID, session ID, SHA and instruction to write through MCP rather than modifying source. The lock is coordination bookkeeping, not proven filesystem exclusion; see [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch). Optional Task-tool workers isolate reading contexts; inline fallback retains the coordinator context. This is not a distinct authenticated user or service session for every phase agent. SRC-1: `.claude/skills/amanuensis/references/subsystem-survey.md`.

> Prefer dispatching the phase as a Task-tool subagent so its reading
> context is isolated. Give it:
>
> - The phase's reference file (e.g. `references/phase-1-scope.md`).
> - The subsystem id and session id.
> - The survey-session SHA.
> - A reminder to write everything through the MCP tools — never to the
>   workspace source.
> --- `.claude/skills/amanuensis/references/subsystem-survey.md`

The phase is asked to return a one-line summary, while durable work goes into the conspectus. Thus the return value is not the complete work product: later phases retrieve ledger, claims, findings and prose from persistent state. The source prescribes keeping Phase 2 reading out of Phase 3 reasoning context, but it does not implement host compaction, automatic frame removal or exact model context assembly. The static phase references are selectively loaded; they are not accumulated experience. SRC-1: `.claude/skills/amanuensis/SKILL.md`; [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill).

### From file scope to challenged conclusions

Phase 1 records a file ledger with inclusion rationales, vocabulary and seam stubs. It excludes method-body reading at that stage. Phase 2 consumes that ledger to map types, state, flows, concurrency and the subsystem's side of seam contracts. Scope expansion must be recorded rather than silently sampled. Phase 3 consumes examined-file state and the structural artifact, then evaluates active concerns, recording evidence before dispositions. Its instructions explicitly return incomplete structural work to the coordinator rather than proceeding on a partial map. SRC-1: `.claude/skills/amanuensis/references/phase-1-scope.md`, `.claude/skills/amanuensis/references/phase-2-structural.md`, `.claude/skills/amanuensis/references/phase-3-concerns.md`.

> - Read the subsystem survey artifact (`<id>-<slug>.md`) for the
>   structural map. **If it's missing or incomplete, stop and return to
>   the coordinator** — concern work on a partial structural summary is
>   the largest source of false confidence in the methodology.
> --- `.claude/skills/amanuensis/references/phase-3-concerns.md`

The coordinator requests status advances after handback. Record prerequisites can refuse the advance, but acceptance is not an oracle for architectural truth. Runtime inspection also establishes that the ordered prerequisite walk is bypassed from `deferred`, although explanation discharge into `mapped` remains separate. Consequently this account does not treat every mapped subsystem as proof of completed challenge. SRC-1: `mcp-server/src/invariants.ts`, `mcp-server/src/tools/subsystems.ts`; [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) and the runtime account's status-admission forcing case.

Phase 4 reverses the direction of inquiry: it tries to overturn findings and structural claims, examines compensating mechanisms and records explicit challenge outcomes. It also passes code-contradicted explanation sentences to packaging through field notes. Its accepted result can be a ruled-out finding, restricted scope, quality adjustment or survival; no prescribed number of overturns is required. The model judges evidence; the server imposes narrower custody/shape checks. Details and the checked rejection path are in [WF-RTE-adversarial-review](#wf-rte-adversarial-review). SRC-1: `.claude/skills/amanuensis/references/phase-4-adversarial.md`.

### Recovery and delivery

A rejected status advance is the coordinator's recovery responsibility, not an invitation for human phase approval:

> A status-advance `ToolError` is not a human gate. Diagnose the missing
> deliverable, re-run the phase once with the deficiency made explicit, and if
> it still cannot advance, mark the subsystem `deferred` with the exact gap and
> continue to the next independent unit.
> --- `.claude/skills/amanuensis/SKILL.md`

Ambiguous judgments instead become open questions with a working assumption. Server loss stops work with the last durable checkpoint surfaced. Resume uses stored status and active-session dispatch history, not restoration of the interrupted model's private reasoning. An unauthorized destructive action requires a snapshot and stop; an already explicit user request can authorize that operation. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/subsystem-survey.md`; [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle).

Packaging belongs to the coordinator, not a fifth phase worker. It updates navigation prose, registers and rehashes artifacts, reads explanations against the concern/adversarial results, revises or confirms them (or explicitly declines a slot), and materializes views. `unfilled_slots` must be filled and rerendered or reported with discharge instructions; the reference says publication proceeds either way. Open slots are therefore visible incompleteness, not automatically a publication rejection. SRC-1: `.claude/skills/amanuensis/references/phase-5-packaging.md`.

> An empty list means every slot is
> recorded or declined. The render is published whichever you choose, so a row
> you leave open is a fact to report and not a reason to stop.
> --- `.claude/skills/amanuensis/references/phase-5-packaging.md`

Publication verification compares generated views to retained source truth; it does not establish that the surveyed code was interpreted correctly. The intended human handoff is the exact returned `html_entrypoint`, accompanied by counts, contradictions, remaining linchpin dependencies, questions and explanation decisions. The portable Markdown companion and durable database/prose remain distinct outputs. The materialization route has options that disable verification or bypass clean staging, so the phase reference's read-back language is not an unconditional implementation guarantee. SRC-1: `.claude/skills/amanuensis/references/phase-5-packaging.md`; [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication).

The final sequence also has a source-level ordering limit: the packaging reference closes the session before advancing to mapped and committing the final gate. As the runtime reports, `end_session` clears the active context while `commit_phase_gate` requires one. The literal final checkpoint cannot simply be presumed successful; a reopened session or corrected ordering is needed. This account retains that limit rather than silently repairing the shipped procedure. SRC-1: `.claude/skills/amanuensis/references/phase-5-packaging.md`, `mcp-server/src/tools/project.ts`, `mcp-server/src/tools/storage-history.ts`; [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle).

A named-subsystem request ends after its packaging summary; a repository-wide inferred scope continues to the next priority unit. This defines prescribed delivery, not observed receipt, reliable model compliance or demonstrated benefit. SRC-1: `.claude/skills/amanuensis/references/phase-5-packaging.md`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-adversarial-review
Label: Adversarial survey review

Part of: [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle)

This is the challenge-and-revision subroute of the supplied survey container, not a duplicate of its whole request-to-publication identity. Endpoints: stored findings, dispositions, current subsystem-prefixed claims and explanations → phase reviewer → evidence, status/history updates, artifact entries and summary → coordinator packaging. Owner: phase agent or inline coordinator proposes and judges; server handlers can veto structurally invalid writes. Human contribution is the initiating request and possible redirection, not required per-target approval. Operating mode: open subsystem survey with a bounded review target set. No supplied expected-answer oracle; inspected code and evidence are the examination material. Guidance seeks actual compensating mechanisms, not speculative balance. SRC-1: `.claude/skills/amanuensis/references/phase-4-adversarial.md`.

Admission/recovery: an overturn is instructed to attach disproving evidence first, then change finding status and disposition, preserving rather than deleting the finding. `update_finding_status` requires an active session and concerns depth, calls `requireOverturnEvidence`, and transactionally appends a resolution event with the update. The helper checks that evidence attached to the finding was created in the current session. It does not computationally determine that the evidence disproves the conclusion, nor check the attachment role in this query. The semantic verdict remains model-mediated. A rejected write can be retried after evidence is recorded and linked. These are knowledge-record changes, not edits to surveyed source or model weights. SRC-1: `mcp-server/src/tools/findings.ts`, `mcp-server/src/invariants.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Handler returns previous status and resolution state; phase instructions require a one-line verdict/claim-outcome summary and unreached claim keys for the coordinator.
- Later read-back: Preserved finding and resolution history, claim outcomes, artifact entries and field notes remain available; packaging is instructed to read notes that contradict explanation sentences.
- Delegated visibility: Reviewer receives phase instructions and survey identities, then retrieves stored targets and source evidence; coordinator receives summary and can read retained results, not a promised full worker transcript.
- Selection predicate: Confirmed bugs, linchpin-dependent dispositions, acceptable dispositions supported only by call-path context, all current subsystem-prefixed claims, and subsystem purpose/account.
- Invalidation or expiry: Findings can be ruled out or scope-restricted; claim invalidation/supersession is prescribed for overturned/stale claims; history remains rather than being silently deleted.
- Activation or effect: Accepted finding-status writes change SQLite status and append resolution events; prescribed packaging uses explanation criticisms. Actual model compliance and resulting published accuracy are unobserved.
- Evidence limits: Implementation establishes a current-session attachment check, not semantic disproof. Claim invalidation/supersession is described here from the phase instructions, not independently retraced through those handlers. No execution trace establishes exercised review or better outcomes.

> - **`overturned`** — first attach the disproving evidence
>   (`add_evidence` for Claim B, then
>   `attach_evidence_to_finding(..., role="compensating")`), *then*
>   `update_finding_status(finding_id, status="ruled-out")` and
>   `set_disposition` with `classification="ruled-out"`.
> --- `.claude/skills/amanuensis/references/phase-4-adversarial.md`

> requireOverturnEvidence(ctx.db, findingId, sessionId, row.status, status);
> --- `mcp-server/src/tools/findings.ts`

> `SELECT COUNT(*) AS n
>          FROM finding_evidence fe
>          JOIN evidence e ON e.id = fe.evidence_id
>         WHERE fe.finding_id = ? AND e.session_id = ?`
> --- `mcp-server/src/invariants.ts`

> if (row.n === 0) {
>     throw new ToolError(
>       `cannot overturn finding ${findingId} to 'ruled-out': no new evidence was attached ` +
>         `in this session. Overturning requires evidence, not vibes — record the disproving ` +
>         `evidence with add_evidence, link it via attach_evidence_to_finding, then re-try the ` +
>         `status change. A reclassification with no new evidence is recorded as an open ` +
>         `question, not applied.`,
>     );
>   }
> --- `mcp-server/src/invariants.ts`

The error's open-question wording is guidance: this inspected helper throws; it does not itself insert an open-question row. This route establishes a rejected transition and prescribed retry, not an automatically completed recovery.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle)

Workflow-specific division of labor: Phases 1–4 can be delegated, while the packaging reference explicitly reserves Phase 5 for the coordinator. Summaries carry progress across host context boundaries; durable records carry the substantive work into later phases. The coordinator owns deficient-phase retry and deferral, publication handoff and continued scheduling. The final checkpoint ordering caveat prevents treating the prescribed end-to-end sequence as proven executable without adjustment. SRC-1: `.claude/skills/amanuensis/references/subsystem-survey.md`, `.claude/skills/amanuensis/references/phase-5-packaging.md`.

> Phase 5 of a per-subsystem survey runs in the **coordinator** — not as
> a separate phase agent.
> --- `.claude/skills/amanuensis/references/phase-5-packaging.md`
