---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "FrameCode-VibeWork workflow account: an authorized multi-package project change, package review, regression rejection and plan closeout."
run-id: AAS-2026-11-08-framecode-vibework-d38fb53e8013-01
reviewed-boundary: "847cdcedc02d08531961c8367f4e2ddb2dc392f1"
---

# FrameCode-VibeWork workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a standard, plan-governed project change with independent work packages and explicit delegation authority. It was selected because the entry-point change flow and orchestrator explicitly share an active plan, acceptance criteria, regression checks and a main-agent closeout owner. This is one connected prescribed workflow, not evidence that any particular project ran it. Its sequential fallback and regression rejection path expose consequential decisions that a happy-path capability list would conceal. The source supplies governance instructions interpreted by an external host, not an FCVW model scheduler. [RT-RTE-governed-change](runtime.md#rt-rte-governed-change), [RT-RTE-work-packages](runtime.md#rt-rte-work-packages).

Evidence is SRC-1 at the frozen revision. Added doctrine/design coverage comprises full reads of `FCVW/PLANNING.md`, `FCVW/REGRESSION_GUARDS.md` and `FCVW/skills/governance-validator/SKILL.md`; `AGENTS.md` and `FCVW/skills/orchestrator/SKILL.md` were reinspected in full. No target execution, host trace or experiment was performed or supplied. All delivery, review and recovery described below are prescribed behavior, not observed compliance. New details annotate the existing change and package routes rather than redeclaring their identities.

### Request to reviewable work contract

A user supplies the project change request. The host reads the entry point, selects applicable context, checks related active/pending plans and creates or resumes one plan for the logical change batch. It records scope, exact affected boundaries, acceptance criteria, priority/risk, preservation checks and rollback, then moves the plan into `in_progress/` before implementation. The plan is a persisted work contract, not a transcript of every command. Its Markdown body guides interpretation; schema/status fields also have deterministic validation consumers. The chosen workflow uses the standard plan, not the read-only or trivial-prose exceptions. [RT-RTE-governed-change](runtime.md#rt-rte-governed-change); SRC-1, `AGENTS.md`, `FCVW/PLANNING.md`.

Context routing supplies policies and project-specific references; optional retrieval returns references/excerpts rather than ensuring the host reads all mandatory content. A plan's `context_files` cannot cancel hard event triggers. Thus the handoff into execution depends on the host reading the routed material, not merely receiving a valid retrieval response. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery); SRC-1, `AGENTS.md`.

### Coordinator to package owner

The main agent loads the orchestrator, inspects the active plan for independent work, and checks other in-progress plans for scope collisions. It can delegate only with current authority, exposed subagent tools, non-overlapping scopes and a reason to expect measured time or review-quality benefit. Risk or domain count alone does not justify a delegation layer. Without the necessary conditions it uses one executor, recording why; sequential packages are optional when useful for dependencies. No benefit measurement or delegation is established by the instruction itself. [RT-RTE-work-packages](runtime.md#rt-rte-work-packages); SRC-1, `FCVW/skills/orchestrator/SKILL.md`.

Each package names the shared plan and affected files, required skill, behavior to preserve, validation evidence and rollback note. Domain agents must load their own skill. The smallest safe package goes first. Exact scope and soft-lock instructions constrain intended behavior, but FCVW does not allocate isolated contexts or enforce filesystem ownership. Worker input inheritance, tool permissions, transcript visibility and return serialization belong to the external host and remain uninspected. The plan's required Orchestration block retains execution mode, packages, collision checks and deferrals; it is not proof of actual launch or completed review. [RT-RTE-work-packages](runtime.md#rt-rte-work-packages); SRC-1, `FCVW/skills/orchestrator/SKILL.md`.

### Package return to verification

The main agent reviews every returned result against the plan acceptance criteria and shared regression criteria. A worker declaring success cannot itself close the plan. Product-specific acceptance criteria and preservation evidence are the comparison basis; no universal expected-answer oracle is shipped for arbitrary project work. The coordinator remains responsible for validation, changelog and closure. This is host-mediated product admission in an open request workflow, not autonomous candidate selection. [RT-RTE-work-packages](runtime.md#rt-rte-work-packages), [RT-RTE-governed-change](runtime.md#rt-rte-governed-change).

Regression review asks whether existing consumers and behavior survived, not only whether the requested feature works. Before implementation the plan identifies those consumers, consulted contracts, proportional checks, any needed baseline and rollback. Before completion, pending results must become `pass`, `fail`, `blocked` or reasoned `not_applicable`, with reproducible evidence. These result labels are source-native plan outcomes, not observations made by this analysis. The detailed rejection conditions and recovery obligations are retained in the change-route annotation below. SRC-1, `FCVW/REGRESSION_GUARDS.md`, `FCVW/PLANNING.md`.

For structural closeout the governance-validator skill adds structure/schema/route/ownership checking and interpretation of findings. It explicitly does not substitute for application runtime tests or establish semantic correctness from syntax checks. Its optional script is executable support, while deciding remediation remains a host responsibility. [RT-RTE-local-checks](runtime.md#rt-rte-local-checks) separately describes the inspected local verification driver; the selected workflow does not require pretending that driver was run. SRC-1, `AGENTS.md`, `FCVW/skills/governance-validator/SKILL.md`.

### Rejection, recovery and delivery

A package or overall result can fail review despite passing its new-feature test. Pending/generic Regression impact, insufficient blast-radius evidence, an undocumented failing/unavailable check, unrelated scope changes or required but unapproved rollback failure block prescribed completion. The main agent owns review and authorized rework; FCVW has no demonstrated automatic repair loop. Gate failure calls for splitting, reducing, deferring or obtaining required approval before editing. A bypass requires named authority and bounded risk handling, not silence. Confirmed regression can lead to a troubleshooting record, a reusable regression note and a strengthened replay/guardrail linked to the plan and version record. Practical verification should show that guardrail failing on the regressed state and passing on the corrected state. These are requested recovery steps, not evidence of an exercised recurrence-prevention loop. SRC-1, `FCVW/PLANNING.md`, `FCVW/REGRESSION_GUARDS.md`; see the annotation on [RT-RTE-governed-change](runtime.md#rt-rte-governed-change).

Delivery is a reviewable repository outcome: scoped edits, decided acceptance, concise reproducible validation, final regression results or explicit bounded limitations, a changelog fragment for application work (framework release record for FCVW work), and a plan whose status agrees with its directory. Plans may instead be discontinued. The orchestrator requires every package to be validated or explicitly deferred and warns that delegation does not turn partial work into completion; deferral does not waive overall acceptance or regression gates. A user-facing final-message format, commit/push requirement or deployment-success condition is not established by the inspected workflow. SRC-1, `AGENTS.md`, `FCVW/PLANNING.md`, `FCVW/skills/orchestrator/SKILL.md`.

This delivery boundary is a protocol, not an invariant enforced across all host writes. The optional hook checks described in [RT-RTE-hook-lifecycle](runtime.md#rt-rte-hook-lifecycle) do not match edits to plan scope and have shell/stop bypasses. Successful completion, actual independent contexts and achieved review-quality or time improvements remain unobserved.

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

#### On [RT-RTE-work-packages](runtime.md#rt-rte-work-packages)

Workflow selection and handoff detail: independent work under one active plan connects delegation to review and closeout. Scope, required skill, preservation behavior, evidence and rollback are supplied per package. Authority and real tools are prerequisites, not a scheduler provision. Main-agent review is the return boundary; isolated model frames and the exact information crossing back are host-specific and uninspected. SRC-1, `FCVW/skills/orchestrator/SKILL.md`.

> 4. For each work package, define:
>    - exact files in scope;
>    - required skill;
>    - behavior to preserve;
>    - validation evidence;
>    - rollback note.
> 5. Execute or delegate the smallest safe package first.
> 6. Review each result against the plan acceptance criteria.
> 7. Do not close the plan until all packages are validated or explicitly deferred.
> --- `FCVW/skills/orchestrator/SKILL.md`

> Exit when every package has one owner, collision checks pass, results are reviewed against shared acceptance and regression criteria, and deferred or failed packages are explicit. Delegation does not convert partial work into plan completion.
> --- `FCVW/skills/orchestrator/SKILL.md`

#### On [RT-RTE-governed-change](runtime.md#rt-rte-governed-change)

Workflow rejection and recovery: the coordinator must reject incomplete preservation evidence even when the new feature succeeds. A failing or unavailable check can be handled only with explicit limitation, residual risk, owner and decision; this is not an unconditional demand that every possible check pass. Human approval is specifically required at R5, not for every package/content change. Failed gates lead to scope reduction, deferral or required approval; rollback is a plan procedure, not automatic reversion. SRC-1, `FCVW/REGRESSION_GUARDS.md`, `FCVW/PLANNING.md`.

> - Evidence is below the plan's risk level or does not cover the identified blast radius.
> - A failing or unavailable check has no limitation, residual risk, owner, and decision.
> --- `FCVW/REGRESSION_GUARDS.md`

> A bypass requires named authority, justification, expiry or review date, residual risk, and follow-up. Silence, a passing new-feature test, or “works on my machine” is not a pass.
> --- `FCVW/REGRESSION_GUARDS.md`

> If a gate fails, split, reduce, defer, or obtain the required approval before editing.
> --- `FCVW/PLANNING.md`

Confirmed-regression recovery requests diagnosis, reusable retention where appropriate, and stronger prevention rather than another duplicate note. No exercised update or future improvement is inferred. SRC-1, `FCVW/REGRESSION_GUARDS.md`.

> 3. identify the missing or failed guardrail;
> 4. add or strengthen a replay check, policy, contract, or watcher;
> 5. link the plan and application or framework release record;
> 6. validate that the new guardrail fails on the regressed state and passes on the corrected state when practical.
> --- `FCVW/REGRESSION_GUARDS.md`

Workflow terminal condition: accepted work and evidence remain linked in repository records; changing the plan's status alone is insufficient. SRC-1, `FCVW/PLANNING.md`.

> - acceptance criteria are decided;
> - required validation ran and evidence is concise but reproducible;
> - applicable regression checks have final results and no blocking Regression gate remains;
> - gaps and residual risks are explicit;
> - rollback remains possible or irreversibility was approved;
> - changelog/release record exists;
> - status and directory agree.
> --- `FCVW/PLANNING.md`

Structural verification is supplementary, not a product oracle. The skill requests authorized corrections and rerunning the same scope, while retaining baseline findings and residual risks. SRC-1, `FCVW/skills/governance-validator/SKILL.md`.

> - claiming semantic correctness from syntax checks alone;
> --- `FCVW/skills/governance-validator/SKILL.md`

> 5. Report exact file and rule for every finding.
> 6. Apply only authorized, plan-scoped corrections and rerun the same checks.
> --- `FCVW/skills/governance-validator/SKILL.md`
