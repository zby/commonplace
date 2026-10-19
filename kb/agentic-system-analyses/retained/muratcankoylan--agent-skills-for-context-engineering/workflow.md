---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agent Skills for Context Engineering research-to-skill workflow: queued source, delegated evaluation, readiness, rejection and reviewable delivery."
run-id: AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01
reviewed-boundary: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
---

# Agent Skills for Context Engineering workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is external research to a reviewable skill change. It was selected because it maintains the target's published instructions and connects persistent source evidence, delegated judgment, deterministic checks and human publication authority. It is a shipped protocol with executable recording and advancement tools, not an observed successful autonomous run. The [boundary](boundary.md) fixes SRC-1; no target execution was performed.

This account extends SRC-1 inspection with the complete `researcher/runbooks/autonomous-research-loop.md`, `researcher/rubrics/content-curation.md` and `researcher/scripts/validate_run.py`, and the retrieval-through-closure functions in `researcher/scripts/research_loop.py`. Rubric and runbook passages supply doctrine/design; Python branches supply implementation evidence. Other rubrics, the novelty algorithm, repository validator internals and actual PR/merge execution are not traced here. Their correctness or operation cannot be inferred from calls to them.

### Request, work selection and delegation

A human asks an agent to find research and turn it into repository changes. The runbook gives that agent a manual initialization entry point, source registry, accepted mechanism registry and rubrics. It declares scoring surfaces locked and evaluations/proposals/drafts editable. These are instructions, not demonstrated filesystem restrictions. SRC-1, `researcher/runbooks/autonomous-research-loop.md`.

The conservative scheduled entry point instead advances one action per invocation: initialize from a queued source, later retrieve, then park for judgment. [RT-RTE-research-step](runtime.md#rt-rte-research-step) establishes work selection, file outputs, repeated reload and fetch-failure recovery. The scheduler does not invoke a judge model; the next-step owner is an external human or agent. This is a file-mediated handoff, not evidence of a running multi-agent conversation.

The handoff supplies the run directory, queue/source pointers, raw evidence where fetched, evaluation draft, proposal scaffold and recorded state. The prescribed evaluator reads the rubrics and source evidence, not merely the scheduler's `retrieved` label. The baseline records that manual retrieval can record that label without a file; the label is therefore insufficient evidence of complete retrieval. SRC-1, `researcher/scripts/research_loop.py`; [RT-RTE-research-step](runtime.md#rt-rte-research-step).

### Judgment, proposal and checks

[WF-RTE-source-triage](#wf-rte-source-triage) describes the evaluator's substantive accept/reject policy. A passing or reviewable source yields a mechanism summary, evidence, candidate skill impact and limitations. An agent or human then applies the skill/harness rubric, drafts a proposal and run-local mechanism proposals, checks novelty before changing published skills, and conditionally compares competing drafts. These are runbook requirements; this report does not establish their automatic enforcement. SRC-1, `researcher/runbooks/autonomous-research-loop.md`.

Recording a completed evaluation and recording a proposal are separate CLI actions. `mark_evaluated` reads a completed JSON file and records its verdict; `mark_proposed` checks for the proposal path and sets state. These functions do not themselves perform substantive evaluation. The novelty action invokes another script, stores its result and any caller-supplied human-review rationale, then records state. Consequently recorded progress is not equivalent to accepted content. SRC-1, `researcher/scripts/research_loop.py`.

The protocol next prepares repository edits, deterministic validation and PR notes. [WF-RTE-run-readiness](#wf-rte-run-readiness) establishes the inspected run-level checks. Repository validation is a separate subprocess whose internals remain uninspected here. The recording functions do not impose an ordered transaction: notably, `pr-ready` writes supplied summary/test-plan/risks and sets state without invoking validation. SRC-1, `researcher/scripts/research_loop.py`.

### Rejection and recovery

A concrete rejection path is a failed source gate: the evaluator records `REJECT` with the gate and stops. For an active run, run readiness rejects a completed evaluation bearing `REJECT`; it also rejects a non-retrieved evaluation. This connects a prescribed semantic rejection to a later symbolic check, provided the evaluator records the verdict truthfully. It is not a semantic re-evaluation of the source by code. SRC-1, `researcher/rubrics/content-curation.md`, `researcher/scripts/validate_run.py`; [WF-RTE-source-triage](#wf-rte-source-triage), [WF-RTE-run-readiness](#wf-rte-run-readiness).

The external agent or human owns recovery from failed judgment or drafting. The runbook routes invalid evaluation JSON and weak relevant evidence to human review, asks for an alternate-URL retry after fetch failure, and prefers no published change while sources conflict. These are prescribed actions, not evidence of an implemented retry/judge service. Closure records accepted, rejected, reference-only or abandoned rationale; the conservative step driver later reaps closed runs. SRC-1, `researcher/runbooks/autonomous-research-loop.md`, `researcher/scripts/research_loop.py`; [RT-RTE-research-step](runtime.md#rt-rte-research-step).

Mechanism admission is separate from published skill editing. [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion) establishes registry/ledger append, rejection recording, nonempty reviewer text and default readiness checking. It also establishes supported `allow-unready`, weaker closed-state checks and nontransactional multi-record appends. Neither reviewer text nor passing readiness authenticates human approval. Failed partial promotion needs external intervention rather than a demonstrated automatic rollback.

### Delivery and interruption boundary

The delivered product of the agent's protocol is reviewable repository changes with PR summary, test plan and unresolved risks, not a merged or host-activated skill. The runbook makes the final publication authority explicit:

> The user rule remains binding: do not push anything to GitHub without explicit approval.
> --- `researcher/runbooks/autonomous-research-loop.md`

> 13. Prepare PR summary and test plan, but do not merge.
> --- `researcher/runbooks/autonomous-research-loop.md`

These instructions constrain the intended agent, but the inspected tools do not enforce remote credentials or human merge control. Closing a run as accepted also does not prove publication. Later installation and host loading belong to [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), whose operation remains uninspected.

For interruption, compaction or model handoff, the runbook directs the current agent to update the thread with the best candidate, evaluation paths, rejected candidates/reasons, risks and next action. This is a prescribed context-transfer summary, not an implemented automatic compactor. Whether a successor actually receives or follows it is unobserved. SRC-1, `researcher/runbooks/autonomous-research-loop.md`.

> Before context compaction, interruption, or model handoff, update the run thread with:
> --- `researcher/runbooks/autonomous-research-loop.md`

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-source-triage
Label: Source gate triage

Endpoints: retrieved source plus content-curation rubric to evaluator-authored JSON verdict/evidence, then proposal work or rejection. Owner: external agent or human applies natural-language guidance; symbolic JSON carries its result. Compared with [RT-RTE-research-step](runtime.md#rt-rte-research-step), this is the subsequent judgment handoff, not deterministic queue advancement. Compared with [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion), it judges sources before mechanism admission rather than appending registry records. SRC-1, `researcher/rubrics/content-curation.md`, `researcher/runbooks/autonomous-research-loop.md`.

- Immediate return: prescribed completed evaluation JSON or recorded rejection; invalid JSON goes to human review.
- Later read-back: recorded evaluation is consumed by later CLI recording and run-readiness invocations; actual execution is unobserved.
- Delegated visibility: evaluator is instructed to receive source evidence and rubric; later reviewers receive evaluation paths and limitations.
- Selection predicate: mechanism specificity, implementable artifacts, beyond-basics scope and source verifiability gates, then weighted scoring and override rules.
- Invalidation or expiry: runbook requires upstream refresh for long-running work; no automatic expiry is established here.
- Activation or effect: intended permission to proceed with proposal work, or stop/review; model compliance remains unobserved.
- Evidence limits: rubric and runbook are doctrine/design, not an implemented semantic judge or supplied evaluation trace.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Decision roles: agent or human proposes the evaluation and applies scores; a human can explicitly override a failed gate. Operating mode: open research requests. Answer oracle: none supplied; rubric criteria and thresholds are normative policy, not reference answers. The objective is admitting useful implementable research, not modifying the rubric while scoring. Evaluation JSON, evidence, summary, impact and limitations persist; no software rollback for mistaken judgment is established.

> If any gate fails, record `REJECT` with the failed gate and stop.
> --- `researcher/rubrics/content-curation.md`

#### WF-RTE-run-readiness
Label: Run readiness checking

Endpoints: run directory state, evaluation, proposal, novelty result and PR notes to findings JSON and process exit status. Owner: `RunValidator` uses fixed Python predicates over JSON fields and text. This is distinct from [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion): promotion consumes this checker, while standalone validation also prepares reviewable changes without performing admission. SRC-1, `researcher/scripts/validate_run.py`, `researcher/scripts/research_loop.py`.

- Immediate return: findings/summary with `ok`, exit zero when no errors and one otherwise; wrapper stores reports and sets validated state on success.
- Later read-back: stored reports support later review; promotion invokes the checker again rather than trusting only the stored report.
- Delegated visibility: caller receives findings and run-local report files; this route does not invoke a reviewer model.
- Selection predicate: active runs check queue, completed source evaluation, proposal placeholders/content, novelty, PR notes and any closure; closed runs check state and closure instead.
- Invalidation or expiry: recomputed on invocation; no general evidence freshness check is implemented in this inspected file.
- Activation or effect: reports validation findings and can block default promotion; it neither edits a skill nor publishes changes.
- Evidence limits: structural/content predicates do not establish source truth, substantive rubric compliance or authenticated approval; closed-state and override alternatives limit the gate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Decision roles: caller supplies documents; code decides these readiness predicates and rejects errors; human semantic review is external. Mode: deterministic checking of an open research run. Answer oracle: none; expected field values and text markers are checks, not task reference outcomes. Rejection leaves repair to caller. The change trigger and admission belong to proposal/promotion, not this checker; reports persist rather than changing proposed content.

> if data.get("decision", {}).get("verdict") == "REJECT":
>             self.error(completed[0], "rejected source cannot produce publish-ready changes")
> --- `researcher/scripts/validate_run.py`

> if verdict != "pass" and not data.get("human_review_rationale"):
>             self.error(path, "non-pass novelty verdict requires human_review_rationale")
> --- `researcher/scripts/validate_run.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-step](runtime.md#rt-rte-research-step)

Workflow role: supplies the file-based handoff to [WF-RTE-source-triage](#wf-rte-source-triage). Parked status is a request for external judgment, not completion of that judgment. The runbook's thread handover is the prescribed bridge across interruption; scheduler state alone does not establish successor context delivery.

#### On [RT-RTE-mechanism-promotion](runtime.md#rt-rte-mechanism-promotion)

Workflow role: registry admission is an intermediate result, distinct from delivered repository edits and a human-approved push/merge. [WF-RTE-run-readiness](#wf-rte-run-readiness) expands the semantics of its default readiness dependency, without strengthening the baseline's qualified gate guarantee.
