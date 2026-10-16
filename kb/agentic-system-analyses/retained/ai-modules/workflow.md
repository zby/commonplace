---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ai-modules workflow account: delegated task readiness repair from user request through frozen handoffs, verification, recovery and delivery."
run-id: AAS-2026-10-14-ai-modules-a7044d5627d2-01
reviewed-boundary: "0cf0227c416f75a79d7317f603a209a63e7a3c8f"
---

# ai-modules workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `task_auto_check`: a user asks the foreground agent to make one existing task implementation-ready without building its described work. It was selected because one shipped procedure explicitly connects delegation, retained handoffs, candidate rejection, controlled writes, post-write verification and terminal reporting. This is the same route declared in [RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair), not a new route assembled from unrelated skills. The delivered product is a repaired task or a bounded stop report, not implemented software (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

The account uses doctrine/design in the frozen Git source. Complete new inspection covers `plugins/ai_dev/agents/auto_drift_task.md`, `plugins/ai_dev/agents/auto_reviewer_task.md` and `plugins/ai_dev/skills/task_check/SKILL.md`; it also rechecks the complete auto-check procedure, gate and verifier definitions. These extend inspection within SRC-1, not the source boundary. No target, test, helper or provider was executed, and no retained execution trace was inspected. Therefore the workflow is an instruction-level coordination contract; successful delegation, isolation, recovery and delivery remain unobserved. The base task hub's full checklist and linter implementation were not independently inspected here, so this account describes their calling and authority interfaces rather than certifying their exhaustive checks (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/skills/task_check/SKILL.md`).

### Request, orientation and freeze

The user supplies one task path or unambiguous name, optionally a positive round cap, creation-time intent or attestation of deliberate intent change. The foreground agent owns orchestration. It reads the task and base/check skills, discovers the task directory and accepts only `open`, `checked` or `ready`. Later lifecycle statuses stop before mutation. A host with no spawn mechanism also stops before freeze; offering a manual check does not authorize performing the missing helper inline ([RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair); SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

Freeze records the complete task byte-for-byte, title/Goal and optional creation intent, optional attestation, initial lint findings and a current-file baseline. The task-stem relay directory is cleared at the start and retained at the end. Thus evidence remains inspectable after delivery but is replaced by the next same-stem run; it is not a cumulative experience store ([RT-OBJ-relay-files](runtime.md#rt-obj-relay-files)). The foreground agent writes helper prompts before dispatch and saves completed returns verbatim. Each handoff points to admitted files rather than summarizing them or prescribing a verdict (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

> A prompt carries no digest, paraphrase, expected verdict, preference, merge instruction, or criterion or repair supplied by the orchestrator. When the orchestrator has a repair idea, send it to `auto_reviewer_task` as an emergent stance beside the standing stances.
> --- `plugins/ai_dev/skills/task_auto_check/SKILL.md`

### Consequential handoffs and decisions

| Handoff | Supplied inputs and receiver responsibility | What crosses back and who acts next |
| --- | --- | --- |
| Foreground → drift helper | Task, frozen intent, project root, base skill and optional attestation. Recover last-commit intent, including rename history when needed, and compare working title/Goal for broadening. | `clean`, `low_confidence_clean`, `drift` or `unassessable`, with baseline and comparison evidence. Foreground proceeds only on the two clean classes; drift goes to the user without automatic reconciliation. |
| Foreground → gate | Task, check/base skills, project root, frozen intent and optional refuted-citation file. Apply `task_check`, not another readiness score. Exclude prior returns and other relay/session state. | Full check report followed by structured status, prior status, updated timestamp, checklist, issues and isolation evidence. `task_check` writes only status/updated. Foreground verifies the post-gate file baseline and inspects isolation before using the assessment. |
| Foreground → stance reviewers | Task, gate issue reference or recorded repeated-link finding, frozen intent, stance and base repair rule. Propose minimal issue-specific repairs, not edits. | Proposal, reason and intent check, or split/no-proposal/unassessable result. Foreground unions proposals; agreement counts do not select a winner. |
| Foreground → proposal verifier | Current task, gate return, every reviewer return, frozen intent and complete frozen task. Check issue resolution, evidence, minimum sufficient scope, charter and commitment fidelity. | Non-overlapping exact anchors/replacements with edit IDs; rejected and human-routed proposals with reasons. Foreground applies approved edits only. |
| Foreground → delta verifier | Task, zero-context apply diff, proposal approval, acted-on lint output and frozen task. Check actual changed lines, not merely approved intentions. | Hunk licenses or unmapped lines; approved IDs applied or missing; clean/failed/unassessable audit. Foreground iterates only after a clean audit, otherwise follows the restore/stop policy. |

These handoffs are specified in SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_drift_task.md`, `plugins/ai_dev/agents/auto_gate_task.md`, `plugins/ai_dev/agents/auto_reviewer_task.md` and `plugins/ai_dev/agents/auto_verifier_task.md`. They request distinct helper contexts; the host supplies actual spawn, context assembly and tools. Read-only role metadata is not independent proof of host enforcement ([RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-RTE-deploy-artifacts](runtime.md#rt-rte-deploy-artifacts)).

The initial drift check is deliberately narrower than generic semantic change detection: narrowing/refinement can classify clean, uncommitted tasks can classify low-confidence clean, and an attestation can make broadening human-owned. It does not certify all historical intent preservation. The subsequent proposal check additionally reads the whole frozen task to prevent quiet deletion or narrowing of existing commitments; the two checks have different comparison bases (SRC-1, `plugins/ai_dev/agents/auto_drift_task.md`, `plugins/ai_dev/agents/auto_verifier_task.md`).

> Attestation. When `attested_intent` is supplied and covers a broadening in the title or Goal, treat that broadening as human-owned and return `clean`. Name the attestation the classification relied on in `## Classification evidence`.
> --- `plugins/ai_dev/agents/auto_drift_task.md`

### Acceptance, rejection and controlled application

The gate judges readiness against task/check rules and repository evidence. Its report must precede the structured verdict; all verified issues must survive condensation. Acceptance coverage requires explicit promise-to-proof pairing, not file existence alone. The foreground consumes the verdict rather than recomputing readiness. A reported out-of-bounds gate read triggers one fresh replacement using the same admitted-input prompt; persistent contamination stops. The isolation line is helper-reported evidence, not an independently monitored read trace (SRC-1, `plugins/ai_dev/agents/auto_gate_task.md`, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

A ready verdict does not always end verification. Two prescribed signatures trigger citation-mode refutation: the first gate moving `open` to `ready` with no issues and all checklist lines clean, or ready on the last permitted gate call. The verifier reads the cited spans in place. Refuted rows are saved and fed back as readiness issues to a re-gate; the verifier itself does not stamp checked. Other ready results receive no citation challenge. At the cap the last-call exception permits one citation step and one re-gate, but no further body repair. Recorded repeated-link findings can receive a separate bounded repair round even after ready, without a new status write or gate call (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_verifier_task.md`).

> Apply the same reject-by-default stance to a gate citation: keep a `clean` claim only when the cited span, read in place in the cited artifact, settles the checklist item the claim was written for, and refute it when the span is absent, says something other than the claim, or establishes only an existence fact for an item the gate's own contract holds that existence checks cannot clear.
> --- `plugins/ai_dev/agents/auto_verifier_task.md`

Reviewers cannot implement the task or write repairs. The proposal verifier can reject or narrow a proposed edit and route deletion/narrowing of frozen commitments to a human, subject to explicit refresh and interaction-supersession exceptions. Structural splits, invalidated premise and unresolved substantive choices likewise remain human-owned. A dead premise is not automatically rewritten or deferred. The user decides whether to prove, re-scope, defer or reject the affected work ([RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair); SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`, `plugins/ai_dev/agents/auto_reviewer_task.md`, `plugins/ai_dev/agents/auto_verifier_task.md`).

Before application, the foreground freshly reads the target and compares it with its last-established baseline, saves pre-apply bytes and checks charter compatibility. It applies approved exact replacements in ID order, requiring one anchor match, changes updated and performs authorized mechanical lint fixes. This is a prompt-governed optimistic concurrency check, not a file lock: another write between read and replacement remains possible. Delta verification then licenses every changed line against approved edits, updated or named mechanical findings, and verifies every approved edit landed (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

### Failure, recovery and delivery

A source-supported rejection path is a failed delta audit. An unmapped change or missing approved edit makes the foreground restore the saved pre-apply task, reapply the approved group and audit once more. A second audit failure restores again, performs mechanical finalization and delivers a stuck report. A failed/unassessable delta invocation instead restores and enters helper-failure handling, which skips finalization. Every corrective write remains subject to the fresh-read concurrency guard; divergence stops rather than authorizing overwrite of another change. These are requested task-local recovery operations, not whole-project rollback or demonstrated restoration (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

> The next `<gate>` runs only after a clean delta audit.
> --- `plugins/ai_dev/skills/task_auto_check/SKILL.md`

For ordinary failed spawn, interrupted execution or invalid helper output, the foreground retries the identical prompt once; the narrowly specified near-instant boilerplate spawn-echo signature earns two retries. A deliberate unassessable result skips retry. Persistent failure stops with no improvised helper result and asks the user to fix deployment, explicitly choose a degraded route or abandon. If no reply can arrive, that question is terminal output, not an automatic fallback ([RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair); SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

Ordinary ready/no-fix/structural/cap exits perform mechanical lint finalization independently of proposal verification. The foreground filters directory-wide findings to the target, applies only the permitted mechanical set, surfaces judgment calls and reruns lint. It does not rerun readiness afterward. Drift, invalidated premise, concurrent modification and helper-failure exits skip finalization. Consequently a delivered stop can intentionally retain lint findings; neither lint cleanliness nor verifier approval alone is a readiness oracle (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

Delivery means returning the final task status and stop reason with gate movements, logical-round and physical-invocation counts, citation challenges, repair approvals/rejections, human decisions, delta/lint evidence, exact verification commands and retained relay path. Ready recommends `task_implement`; other exits name the corresponding user action. The default cap is five rounds with a positive user override and the bounded last-call exception. Reporting does not itself audit, finish, archive, commit or release the task's described implementation. Its later work contract reaches implementation through [RT-BAP-task-guidance](runtime.md#rt-bap-task-guidance), but this source inspection establishes no exercised improvement in readiness or later implementation quality (SRC-1, `plugins/ai_dev/skills/task_auto_check/SKILL.md`).

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

#### On [RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair)

Workflow-specific acceptance boundary: readiness belongs to the gate; approval belongs to the proposal verifier; fidelity of landed changes belongs to delta verification; the foreground remains the writer and recovery owner. These are separate judgments, not independent known-good answer oracles. The workflow uses an open user-selected task, bounded computational review and explicit human veto over consequential intent/disposition choices. A successful delivered ready report recommends the next sibling but does not run it.

Workflow-specific recovery limit: pre-apply restoration is conditioned on a fresh baseline match and covers the task file, not project-wide state. Terminal helper-failure reporting can be a question with no continuation. The report's counts distinguish logical steps from physical retries and isolation replacements, preserving the bounded workflow's accountability without claiming observed execution.
