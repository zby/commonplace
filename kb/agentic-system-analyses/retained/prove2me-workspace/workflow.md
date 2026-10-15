---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Prove2Me_workspace workflow account: source-to-public-mission proposal, blind statement read-back, human launch and moderator correction at the frozen commit."
run-id: AAS-2026-10-14-prove2me-workspace-187ef30582c9-01
reviewed-boundary: "38e12f9d215cb103a0f9173ec230a614fcd93b61"
---

# Prove2Me_workspace workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **formalizing a supplied mathematical source into a public mission**. It is selected because the captain playbook connects request, draft construction, delegated audit, human comparison, software compilation, moderator review and delivery in one explicit sequence. It is not assembled from unrelated capabilities. The canonical route is [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit). Existing compiled-project upload is a different entry route, [RT-RTE-project-upload](runtime.md#rt-rte-project-upload), not a prerequisite of this sequence. SRC-1, `references/mission_captain.md`.

This account is doctrine/design evidence at the frozen revision in [boundary.md](boundary.md). This worker read `references/mission_captain.md` and `references/mission_auditor.md` fully and directly; these deepen coverage already supplied by the runtime, rather than add a new source. The artifact ships instructions, not the enclosing agent scheduler or service implementation. No agent episode, API transaction or compilation was executed. The sequence establishes a prescribed workflow, not demonstrated successful coordination. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`.

### 1. Human request becomes a dependency-ordered draft

The human supplies the source and intended goal. The captain must first identify the exact page/theorem and understand the section's assumptions. The captain then selects field tags, creates a private proposal, searches for already-published matches, and drafts only missing definitions and theorems. Existing faithful matches become reference items. The draft includes a goal identified by `main_item_id`, a dependency-first `item_order`, and milestone text attached to supporting theorem items. The proposal's environment is set once, not separately for each item. These are choices by the foreground agent under a source-faithfulness policy, not decisions by a shipped planner. SRC-1, `references/mission_captain.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

Draft storage is not verification. New theorem/definition items are mutable text, and reference items point to immutable published declarations. Local compilation is instructed before handoff, but formal well-formedness does not decide whether the source was faithfully translated. The captain's criterion explicitly excludes weakening a statement to make its proof easier. SRC-1, `references/mission_captain.md`; [RT-CLM-verification-boundary](runtime.md#rt-clm-verification-boundary).

> - **nothing is verified at upload** — compile and iterate locally, then re-upload.
> --- `references/mission_captain.md`

### 2. Captain delegates literal read-back, not source-faithfulness judgment

For each draft declaration the captain is instructed to launch an independent auditor in a fresh context. The handoff consists only of the declaration's code, its preamble and the auditor playbook. Informal statement, source, mission pitch and captain intent must stay out. This selects an intentionally narrower input than the captain's own context: the auditor is to render what the artifact says without being prompted toward its intended meaning. The host must implement the fresh context; the repository does not demonstrate actual isolation. SRC-1, `references/mission_auditor.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

> - the Lean code of the declaration: its `formal_statement` (or the definition's code), plus the `preamble` it depends on;
> - this file.
> --- `references/mission_auditor.md`

The required return is self-contained mathematical prose covering binders, assumptions, nonstandard definitions, logical strength and edge cases. It is not an acceptance verdict. The auditor does not receive the reference outcome needed to assess source equivalence; the human receives both intent and this literal testimony. Whether the supplied code/preamble actually includes enough custom-definition context for complete expansion is not established by an execution trace. SRC-1, `references/mission_auditor.md`.

> 7. **No judgment, no advocacy.** Do not assess whether the formalization is correct, faithful, or well-designed, and do not defend it. Discrepancies are for the human auditor to find by comparing your read-back with the stated intent.
> --- `references/mission_auditor.md`

Only the returned read-back is prescribed to cross back into the proposal, with `readback_model` attribution. This is a requested per-item context frame, not evidence of a host eviction or compaction algorithm. The retained result is [RT-OBJ-readback](runtime.md#rt-obj-readback), which becomes a later human/moderator input. Read-back is strongly recommended but optional API content, so the documented service gate does not establish mandatory independent audit of every item. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`.

### 3. Human comparison precedes compile-and-publish

The captain hands the human a clean ordered proposal and points them to the website review page. The human compares each statement, especially definitions, with the intended mathematics using the attached read-back. Confirmation and submission are assigned to the human; they can withhold launch. The auditor supplies testimony, the captain proposes code and corrections, and the human performs the intent comparison. This separates semantic review from compilation. SRC-1, `references/mission_captain.md`; [RT-CLM-human-gate](runtime.md#rt-clm-human-gate).

At **Submit Proposal**, the documented service invokes the normal contribution mechanisms on drafts in dependency order. Successfully compiled drafts become immutable published declarations. Once all drafts compile, the public proposal enters `In review`. This is publication of library artifacts, not yet delivery of an approved public mission. SRC-1, `references/mission_captain.md`; [RT-RTE-content-publish](runtime.md#rt-rte-content-publish).

> A draft that passes compilation becomes an **immutable** published theorem/definition — from then on it behaves like a reference item of the proposal. If any draft fails to compile, the whole submit fails; once all drafts compile, the proposal is sent to the moderators.
> --- `references/mission_captain.md`

The software gate can reject compilation; it does not certify informal source equivalence or solve the new theorem. The account does not infer transactional rollback of earlier successful publications when a later item fails: the quoted contract says submission fails but supplies no backend trace of atomicity. The human must relay launch feedback so the captain can fix failed drafts. SRC-1, `references/mission_captain.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

### 4. Moderator acceptance delivers the mission, not a proof

For the selected public path, a moderator approves or requests changes. Approval produces `Reviewed`, a live public mission whose milestone list comes from the proposal. Thus delivery is a public attack path with a formal goal, supporting declarations and curated milestones. It is not a guarantee that the goal has been proved. The later solver loop is [RT-RTE-solver-proof](runtime.md#rt-rte-solver-proof), with conditional decompositions in [RT-RTE-reduction-proof](runtime.md#rt-rte-reduction-proof). SRC-1, `references/mission_captain.md`.

After launch the captain remains responsible for milestone faithfulness and link attestation, while solvers attack the frontier. Milestone order is a suggested attack order, not a shipped task scheduler. The milestone playbook explicitly says there is no dependency tracking for that list; this must not be confused with the theorem reduction graph. Link replacements and reasons feed the later solver history-consumption path [RT-BAP-milestone-guidance](runtime.md#rt-bap-milestone-guidance). No actual solver reliance is observed. SRC-1, `references/mission_captain.md`.

> - **Order matters.** `sort_order` is the intended reading/attack order. There's no dependency tracking yet, so encode prerequisites in the statements themselves.
> --- `references/mission_captain.md`

Private launch is a material alternate: the same human confirmation and compile-and-publish steps lead immediately to `Private`, without moderator review. This bounds the public acceptance account rather than contradicting it. Direct contribution and upload-first routes do not inherit this proposal's launch gate. SRC-1, `references/mission_captain.md`; [RT-CLM-human-gate](runtime.md#rt-clm-human-gate).

### Rejection and recovery ownership

Before launch, the captain can revise draft statements locally and update their stored fields. Changes invalidate prior human confirmation, and statement changes require another independent read-back. This prevents treating an old testimony as evidence about a successor declaration by protocol; actual invalidation enforcement and rerunning remain unobserved. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`.

> Because you changed what your human would audit, **editing a draft item clears any prior confirmation** — it must be re-confirmed before launch. `DELETE` returns `204` and drops the item from `item_order`.
> --- `references/mission_captain.md`

A moderator send-back moves the proposal to `Changes requested`. The captain must read both the latest overall review and per-item flags before correcting it. Published declarations cannot be edited: the captain adds a corrected draft under a new name, removes the superseded reference, optionally deprecates a bad declaration they created, and updates goal/milestone links. Wrapper metadata can be edited directly. The human re-confirms changed items and resubmits; subsequent review adds another retained round. This is successor construction, not rollback of publication. SRC-1, `references/mission_captain.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit), [RT-RTE-content-publish](runtime.md#rt-rte-content-publish).

> Flags stay attached to their theorems and reports stay in `reviews` permanently — the history is the record, so old feedback below the newest entry is normal, not a standing objection.
> --- `references/mission_captain.md`

This establishes a prescribed content-directed correction loop with distinct recovery owners: auditor reruns supply fresh testimony, captain repairs the artifact and links, human authorizes another submission, and moderator re-evaluates public admission. No supplied example demonstrates that the comparison detected a mismatch or that a correction improved later performance. The bounded conclusions are coordination and correction contracts, not reliable independence, learned capacity or exercised autonomous theory construction. SRC-1, `references/mission_captain.md`, `references/mission_auditor.md`; [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit).

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

#### On [RT-RTE-proposal-audit](runtime.md#rt-rte-proposal-audit)

Workflow selection: representative request-to-public-mission sequence because one playbook connects all consequential handoffs, rather than leaving delivery to an unrelated capability.

Handoff roles: captain transfers deliberately restricted code context to auditor; auditor returns testimony rather than a verdict; captain transfers the ordered proposal and testimony to human; human comparison and submission precede software compilation and moderator review. The enclosing host owns actual context isolation and execution.

Delivery criterion: `Reviewed` marks delivery of the public mission and its curated attack path. Earlier item publication is a distinct intermediate result; no proof of the goal is required by this workflow's terminal criterion.

Recovery distinction: draft edits require fresh testimony and human confirmation; moderator rejection after publication requires replacement declarations and link retargeting, not in-place statement repair. The documented whole-submit compile failure does not establish rollback atomicity for previously successful items.

#### On [RT-OBJ-readback](runtime.md#rt-obj-readback)

Workflow verification role: literal statement testimony reaches the human comparison gate and later moderator review. Its independence depends on withholding source intent at the captain-to-auditor handoff, and its relevance depends on rerunning after statement edits. It is not the source-equivalence oracle or a formal acceptance certificate.
