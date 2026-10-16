---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "beads_rust workflow: caller-led discovery, atomic claim, external implementation, gated closure and Git delivery."
run-id: AAS-2026-10-16-beads-rust-e82d5506d2ff-01
reviewed-boundary: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
---

# beads_rust workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped standard agent workflow: discover ready work, inspect and claim an issue, implement outside the tracker, close with evidence, check queue impact, export and publish through Git. It was selected because the source explicitly connects these steps, rather than because separate capabilities could hypothetically be combined. The fuller skill adds inspection, evidence and publication to the integration guide's five-step outline (SRC-1: `docs/AGENT_INTEGRATION.md`, `.claude/skills/br/SKILL.md`). Its purpose is caller-led project work coordinated through retained issue state, not autonomous execution by br.

Evidence is SRC-1 at the frozen revision registered in [boundary.md](boundary.md#source-register). Additional doctrine/design inspection covers the standard workflow and claim instructions in `docs/AGENT_INTEGRATION.md`, the session-ending and full-workflow sections of `.claude/skills/br/SKILL.md`, and the embedded workflow/session checklist in `src/cli/commands/agents.rs`. Implementation inspection checks close-evidence construction and rejection in `src/cli/commands/close.rs`; the other implementation mechanisms use the supplied runtime records. No target execution or host trace was supplied or generated. The result establishes shipped instructions and wired admission mechanisms, not successful delivery, agent compliance or productivity benefit.

### Request, selection and responsibility handoffs

The starting request is an external caller's decision to take project work from the queue. The source does not supply an authenticated commissioning principal or a particular user conversation. The agent asks `br ready --json`, then uses `br show <id> --json` to inspect its choice. The full workflow says to pick the highest-priority ready work, but that is guidance to the caller, not an enforced scheduling policy (SRC-1: `.claude/skills/br/SKILL.md`). Ready returns a filtered issue projection; it does not reserve work or carry the full retained description and dependencies. The show step is therefore an explicit additional context request, not a delegated worker context ([RT-RTE-ready-query](runtime.md#rt-rte-ready-query)).

The caller next sends the selected issue ID and actor attribution to `br update --actor "$ACTOR" <id> --status in_progress --claim`. The transactional claim operation sets assignee and status and can reject stale or conflicting eligibility. This hands a mutation request to tracker code, not an implementation task to a newly launched agent. The same external caller remains responsible for implementation. Other callers discover ownership by reading committed issue state ([RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue)). The integration guide recommends this stronger path; the installed blurb instead calls a plain status update a claim. The latter does not inherit the assignment precondition of `--claim` ([RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle)).

The work step is explicitly external implementation. br retains status and can accept newly discovered tasks with a `discovered-from` dependency, but the guide's instruction to create them does not establish that discovery or follow-up occurred (SRC-1: `docs/AGENT_INTEGRATION.md`; [RT-RTE-create-issue](runtime.md#rt-rte-create-issue)). No implementation executor, worker launch, file-reservation service or reviewer handoff is established by this selected workflow. Model choice, tool permissions, coding tests and actual task acceptance remain host/project responsibilities, not tracker guarantees.

### Verification, rejection and recovery

The full workflow requests closure with a reason such as an implementation commit reference. That is caller-supplied evidence, not proof that the referenced implementation satisfies the task (SRC-1: `.claude/skills/br/SKILL.md`). Close code assembles its evidence from the close reason, retained description/design/acceptance criteria/notes, closing actor and, when required, the previous in-progress actor (SRC-1: `src/cli/commands/close.rs`). Policy consumers decide which configured checks apply; neither the record's acceptance-criteria field nor a commit string is an independent answer oracle.

A concrete rejection path is closure-policy failure without explicit bypass. The command returns a policy violation naming the issue and violations before admitting that planned closure:

> if !evaluated_gates.violations.is_empty() && !args.bypass_policy {
>                 let summary = summarize_violations(&evaluated_gates.violations);
>                 return Err(BeadsError::PolicyViolation {
>                     issue_id: id.clone(),
>                     summary,
>                     violations: evaluated_gates.violations,
>                 });
>             }
> --- `src/cli/commands/close.rs`

Recovery belongs to the caller: address the unmet condition and request closure again, or deliberately use a reasoned bypass where policy permits it. This describes available choices, not an automatic repair loop. The storage transition checks, CLI override and post-commit auxiliary metadata have different strengths; a metadata error can occur after closure has committed. Reopening is a later state change, not automatic rollback or retrospective proof of correctness ([RT-RTE-close-issue](runtime.md#rt-rte-close-issue)).

Earlier in the workflow, a ready snapshot may become stale before claim. Claim rejection requires reloading/reconsidering the issue rather than treating ready output as a lease ([RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue)). At the end, database mutation and JSONL export are separate effects. A flush problem does not prove the preceding mutation failed; the caller must distinguish retained issue state from export state instead of blindly repeating a mutation ([RT-RTE-create-issue](runtime.md#rt-rte-create-issue)). No observed recovery attempt is established here.

### Completion and delivered result

After closing, the full workflow asks the agent to query ready and blocked work again, making changed queue state available to a later decision (SRC-1: `.claude/skills/br/SKILL.md`). This is re-querying retained state, not an automatic continuation or worker scheduler.

Three terminal boundaries must remain separate: closure commits tracker status; `br sync --flush-only` exports issue state to JSONL; external Git commands commit and publish files. The selected protocol's delivery criterion extends to Git publication and an up-to-date status check, but br's closure/export returns do not establish that criterion ([WF-CLM-session-delivery](#wf-clm-session-delivery)). The blurb and skill differ in checklist details; the blurb's staging order is not evidence that every changed file reaches the commit. Actual staged content and remote delivery remain unobserved.

Explicit final export is a conservative session step. It does not resolve the shipped skill's inaccurate universal statement that sync is never automatic: wired mutation paths already attempt auto-flush ([RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync)). Installed instructions can ask future agents to follow the protocol, but loading and compliance are external ([RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions)). The supported workflow is thus a sequence coordinated by caller decisions and persisted issue transitions, with conditional software rejection points, not a source-proven end-to-end delivery guarantee.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-session-delivery
Label: Session delivery criterion

Claimed operation: before ending a session, the caller should export issue state, commit it through Git, push and check that the workspace is up to date with origin. Source: SRC-1, `.claude/skills/br/SKILL.md`. This is doctrine/design governing an external caller, not an implementation guarantee or observed publication.

> git pull --rebase
> br sync --flush-only
> git add .beads/ && git commit -m "Update issues"
> git push
> git status  # MUST show "up to date with origin"
> --- `.claude/skills/br/SKILL.md`

Closest supplied record: [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle), which records the retrieve–work–close–export cycle from the installed blurb. The distinct claim here is the skill's external Git delivery/verification criterion, not a second declaration of the same tracker route. [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions) describes the blurb's host-dependent authority; neither record establishes that a host performed publication.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ready-query](runtime.md#rt-rte-ready-query)

Workflow role: candidate discovery, followed by caller inspection and choice. A later claim must recheck eligibility; the discovery return is not the handoff of reserved implementation work.

#### On [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue)

Workflow role: ownership coordination before external implementation. Rejection returns responsibility to the caller to reload or choose other work; it does not reschedule a worker automatically.

#### On [RT-RTE-close-issue](runtime.md#rt-rte-close-issue)

Workflow role: conditional tracker acceptance after caller-reported implementation. This terminal state is weaker than verified task correctness or published Git delivery; the latter remains a separate caller step under [WF-CLM-session-delivery](#wf-clm-session-delivery).
