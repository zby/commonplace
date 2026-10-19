---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Autogenesis workflow account: delegated shopping-site implementation, deployment, browser verification, advisory review and delivery."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped shopping-site request: build a React storefront, deploy it, verify its live interactions, repair defects and return the result. It was selected because its acceptance conditions require more than generating files: deployment supplies a URL, browser checks supply interaction evidence, and the orchestrator must decide whether to continue. SRC-1, `examples/tasks/online_shop_site.html`, supplies the request as doctrine/design, not a completed episode:

> "Done" means the live site genuinely works and looks good when a real user drives it in
> a browser:
> --- `examples/tasks/online_shop_site.html`

This is a source-supported intended workflow over implemented delegation and tool dispatch, not a reconstructed execution trace. No request submission, site, browser session, review verdict or successful delivery was supplied. The [boundary](boundary.md) fixes the source and revision. Additional inspection covers SRC-1, `examples/tasks/online_shop_site.html`, `configs/meta_agent.py`, `autogenesis/prompt/default/meta_agent.html`, `autogenesis/protocol/server.py`, `autogenesis/agent/actor/reviewer_agent.py`, `autogenesis/prompt/default/reviewer_agent.html`, and the deploy/redeploy handler in `autogenesis/tool/default/deploy.py`. Python handlers provide implementation evidence; task and prompt text provide design evidence. Deployment-manager internals and browser-environment execution were not inspected here; no deployment isolation or actual browser success is inferred.

### Request, implementation and deployment

1. **Intake.** A client can submit the task through the Gateway. Submission returns task/conversation IDs before execution. The worker selects MetaAgent; the runtime owns the agent reference, mailbox and reply future. This implemented entry and terminal bookkeeping are established in [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task). The example task is an input specification, not evidence that Gateway automatically loads that particular file.
2. **Delegate implementation.** The MetaAgent prompt directs real repository work first to an actor, specifically code_agent for implementation. It directs self-contained tasks rather than a JSON plan. The shipped configuration includes code_agent, browser_agent and reviewer_agent (SRC-1, `configs/meta_agent.py`). The model chooses the decomposition, task text and timing; there is no fixed shopping-site graph. A plausible compliant first handoff supplies the storefront requirements and workspace paths to code_agent; no exact handoff payload is claimed as observed.
3. **Separate child work, shared effects.** [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) establishes the fresh child context, optional allowlists, runtime invocation and return message. The child does not inherit the full parent transcript. File arguments are filtered to paths that exist; absent paths therefore cannot be assumed delivered (SRC-1, `autogenesis/protocol/server.py`). The parent must pass acceptance criteria and relevant results in task text/files. Context separation does not isolate shared workspace effects. Action completions return through the parent's mailbox; dependent browser/reviewer work belongs in a later round, not in the same concurrent batch as implementation.
4. **Deploy and retain the actual URL.** The deployment tool passes a DeployRequest to deployment_manager. Its handler classifies a record as successful when status is running, and returns the URL in its message plus the serialized record. This establishes an information handoff, not working checkout or image loading (SRC-1, `autogenesis/tool/default/deploy.py`). The browser handoff must carry that exact URL, not an inferred port. Deployment may be selected by the parent or by an appropriately equipped actor; the inspected evidence does not mandate a unique agent owning that call.

### Verification, rejection and recovery

The next phase is [WF-RTE-ui-verification](#wf-rte-ui-verification): browser evidence followed, when dispatched, by advisory review. The task's acceptance criteria cover search/filtering, relevant recommendations, cart totals, checkout confirmation, persistent orders and visual/browser quality. These are reference requirements, not a supplied expected-answer oracle or deterministic scorer.

The model must interpret browser findings. Broken images or checkout failures should cause a repair delegation, then another deployment/verification cycle. The default recovery is to fix the product with existing capabilities. The prompt distinguishes this from evolving a missing capability; its decision guidance and the actual extension-admission limits are already recorded in [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance) and [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission). This account does not claim that a storefront defect exercised self-improvement.

There is also a concrete negative-review path without any demonstrated site defect: if only curl/bundle evidence is provided, the reviewer prompt directs a low verification score and a continue recommendation. MetaAgent then owns recovery, not the reviewer. A reviewer verdict is returned text, not a software veto. Neither its recommendations nor browser evidence are required by the inspected generic completion mechanism. Budget/constraint/no-progress stops can terminate earlier; even a success classification need not mean the task was completed, as the repeated-batch countercase in [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) shows.

### Delivery boundary

Under the task contract, delivery means a deployed URL whose actual browser behavior meets the acceptance conditions. Under the runtime protocol, normal completion is MetaAgent's done_tool result, synthesized into a Response and published through Gateway task completion. Those are different boundaries: task.completed indicates return, not independent acceptance. The prompt even permits finishing with an honest partial result. No automatic final storefront acceptance test was established. A returned URL, running deployment or positive reviewer recommendation alone does not establish this workflow's successful delivery.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-ui-verification
Label: UI verification handoff

Part of: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)

This is the product-verification phase within the general Gateway task route, not a second generic delegation mechanism. It uses [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) for browser/reviewer calls. Distinct scope: the URL/evidence handoffs, advisory acceptance criteria and product-repair decision, rather than child allocation itself.

Endpoints and progression: deployment result → parent-issued browser task at the exact URL → browser findings → optional reviewer task with original requirements/artifacts/browser evidence → advisory verdict → parent repair delegation or done_tool. Owner: MetaAgent chooses each handoff and whether to finish; child models choose their local checks. State includes workspace artifacts, deployed URL, child return messages and any evidence files explicitly supplied. SRC-1, `autogenesis/prompt/default/meta_agent.html`, `autogenesis/prompt/default/reviewer_agent.html`, `autogenesis/agent/actor/reviewer_agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: the generic child route returns the child's message to the parent; review is an advisory text verdict rather than a parsed completion gate.
- Later read-back: browser evidence files and returned findings can be supplied in a subsequent reviewer task; actual retention, complete replay and later consumption of an episode are uninspected.
- Delegated visibility: concrete URL, acceptance script, selected task/files and evidence, not the full parent or sibling transcript; browser evidence must cross the handoff explicitly.
- Selection predicate: parent model selects available browser_agent/reviewer_agent; prompts require real-browser UI checking and strongly recommend final substantial-task review, but the generic dispatcher does not require either before completion.
- Invalidation or expiry: a repair or redeploy can invalidate prior browser findings; redeploy may change the URL. No automatic stale-verdict invalidation was established in the inspected prompt and handlers. Generic agent budgets and runtime cleanup bound child work.
- Activation or effect: can supply evidence for a parent decision and lead to product repair/redeployment; actual compliance, repairs and changed decisions are unobserved.
- Evidence limits: instructions establish requested checking, not exercised verification. Reviewer uses the standard agent loop and cannot veto the parent's completion through its verdict alone. Browser implementation and deployment internals were not inspected here.

The parent proposes work and decides whether the product is ready. The browser agent reports observations; the reviewer judges them against requirements. Humans may supply requirements or inspect the product, but no human per-repair approval is required by this route. Operating mode: open user task with concrete acceptance checks, not a fixed benchmark. Answer oracle: no independent reference outcome supplied; requirements and requested browser observations guide model judgment. Trigger for repair is a reported mismatch. What changes and persists is the workspace product and deployment, not necessarily the runtime's own capabilities. Rejection is an advisory continue/evolve recommendation. Recovery is parent-directed rework; deploy_tool provides redeploy and stop operations, but this phase establishes no automatic artifact rollback or transactional undo of checkout interactions.

Minimum source witnesses, SRC-1:

> **You MUST put the EXACT deployed URL (from the deploy result, e.g. `http://localhost:3000/`) in its `task`**
> --- `autogenesis/prompt/default/meta_agent.html`

> **If the only evidence is a curl 200 / reading the bundle, the UI is UNVERIFIED** — score Verification ≤ 2 and recommend `continue` (instruct MetaAgent to dispatch `browser_agent` to drive the acceptance flow).
> --- `autogenesis/prompt/default/reviewer_agent.html`

> Its verdict is advisory: MetaAgent reads it and
>     decides.
> --- `autogenesis/agent/actor/reviewer_agent.py`

> ok = rec.status.value == "running"
> --- `autogenesis/tool/default/deploy.py:84-88`

> - `redeploy`: tear down and rebuild a site from its stored request (URL may change). Args: `site_id`.
> --- `autogenesis/tool/default/deploy.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation)

Workflow-specific handoff constraint: the implementation, browser check and review are separate contexts, so no complete cross-worker evidence transfer follows merely from their execution in one parent task. Acceptance requirements, the actual URL and browser evidence must be selected into later child tasks. This makes the parent's evidence packaging consequential. It does not alter the runtime record's generic identity, success handling or permission limits.
