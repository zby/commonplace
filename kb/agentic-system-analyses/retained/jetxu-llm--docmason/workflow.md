---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "DocMason workflow account: a corpus question through canonical ask, grounded answering, bounded repair and delivered closure."
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
---

# DocMason workflow report

## Workflow account

The representative workflow is a user question answered from the published corpus through canonical `ask` and its `grounded-answer` inner workflow. It was selected because the shipped skills explicitly connect request routing, evidence selection, drafting, verification and delivery within one turn. This is not a constructed chain of unrelated tools. The account follows [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask), [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools) and their failure/refresh edges. Evidence is implementation and doctrine/design from SRC-1 at the frozen commit, not an observed successful answer. No target execution or tests were performed.

### Request and handoff

The host agent owns reasoning and user communication; DocMason does not schedule a separate model worker. The canonical skill instructs the host to open the hidden ask wrapper with the question, thin work brief and host/conversation/turn identity. The returned control state supplies the canonical answer path, active run, support contract, log context and selected inner workflow. Stable turn identity binds subsequent tools and closure ([RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn); SRC-1, `src/docmason/host_integration.py`, `skills/canonical/ask/SKILL.md`).

Only an `execute` handoff to `grounded-answer` starts this inner workflow. A workflow name is a responsibility boundary within the host protocol, not evidence that another isolated agent was launched:

> - Start only after canonical `ask` has already handed the live turn here with `status = execute` and `inner_workflow_id = grounded-answer`.
> - If the current turn is missing that ask-owned handoff, stop and route back to `ask`.
> --- `skills/canonical/grounded-answer/SKILL.md`

The handoff carries the work brief, resolved decisions, accepted scopes, reference resolution, source-scope policy, evidence requirements and support contract. The inner workflow must preserve these constraints rather than reopen decisions it does not own. It writes a short support ledger identifying source boundaries, required comparison sources, required evidence channels and the remaining repair allowance (SRC-1, `skills/canonical/grounded-answer/SKILL.md`). These are instructions for host judgment, not proof of compliance.

The selected path assumes a usable publication. If none exists, the ask contract routes to sync rather than inventing an answer. Usable but stale publication can support an answer with a freshness notice; genuinely necessary freshness may instead require a governed shared job. Confirmation/waiting keeps the same turn, and the contract prohibits bypass through raw sources or staging. The publication admission mechanism is already established in [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish); it is a prerequisite/alternate branch, not a mandatory rebuild for every question (SRC-1, `skills/canonical/ask/SKILL.md`).

### Evidence work and coordination

The host normalizes the question, retrieves published evidence, inspects the strongest bundles and preserves any exact source narrowing. Approximate or unresolved references must remain visible in the answer. Visual inspection follows when layout, diagrams, low-confidence text or render-only evidence materially affects the answer. Published text, structure and notes are considered before renders and governed escalation (SRC-1, `skills/canonical/grounded-answer/SKILL.md`). The support basis is explicit and separate from the four-state answer state; even this named workflow permits external, model-knowledge or mixed support where the canonical contract allows it. It does not imply universal KB grounding.

Working context is controlled by authored selection: compact retrieve/trace results are the default, while full nested JSON goes to a local file for selective inspection. The host decides when additional artifact details or renders are needed. This reduces requested payload, but does not establish eviction of earlier tool results, host compaction or a bounded model window. Local files and published artifacts remain available for later inspection ([RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools); SRC-1, `skills/canonical/grounded-answer/SKILL.md`).

The main agent remains responsible for shared mutation, publication and final integration. Read-only side research is permitted by [RT-BAP-canonical-skills](runtime.md#rt-bap-canonical-skills); isolated worker contexts and their actual return payloads are uninspected. Within the live answer path, the inner workflow explicitly requires sequential workspace commands:

>    - keep DocMason workspace commands sequential inside the same live answer path; do not overlap `retrieve`, `trace`, `sync`, `status`, or `validate-kb` while a lease-owning step is still running
> --- `skills/canonical/grounded-answer/SKILL.md`

If published evidence fails because of hard-artifact semantic gaps, `recommended_hybrid_targets` is the authorized narrowing entry into one governed Lane C refresh. A waiter reuses the shared result. After covered settlement, the host reretrieves and retraces the post-refresh evidence; a remaining boundary must be acknowledged rather than starting another refresh. Blocked settlement leads to `abstained + governed-boundary` by the authored contract ([RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh); SRC-1, `skills/canonical/grounded-answer/SKILL.md`). This is bounded recovery guidance plus implemented settlement/admission wiring, not demonstrated render comprehension or successful enrichment.

### Draft, verification and rejection

The host drafts the canonical answer under `runtime/answers/`, with scratch artifacts separate under `runtime/agent-work/`. The final grounding check traces the exact answer file. When several ask-owned sessions or plausible traces exist, the workflow keeps selected IDs in an artifact ledger and returns them to the main agent. With a single session and final trace, automatic hydration is permitted. The preferred structured `workflow_outcome` handoff carries workflow-owned support facts; the inner workflow returns the business answer, answer state, support basis and explicit support boundary to ask (SRC-1, `skills/canonical/grounded-answer/SKILL.md`).

Trace diagnoses support; it is not an independent answer oracle. The host must qualify contradictory or insufficient evidence and must not relabel partial/unresolved results as grounded. Repository admissibility can reject ownership, evidence/version binding and scope violations before commit ([RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate)). Thus host semantic judgment proposes the answer, trace supplies diagnostics, and the commit gate decides legal canonical admission. User initiation is not approval of each generated claim.

The inspected wrapper rejects duplicate committed turns, waiting states and forbidden truth overrides before completion. Supplied nonempty answer text is written to the canonical path; completion receives the selected artifact/support facts. Missing ask-owned trace may trigger automatic trace recovery and a completion retry when explicit IDs were not supplied. A repairable failure instead restores prepared state and returns an admissibility repair contract; a nonrepairable failure returns blocked with `user_reply_allowed` false and a noncanonical artifact path (SRC-1, `src/docmason/host_integration.py`; workflow-specific details in the annotation below).

The host, not the Python wrapper, performs semantic rewrite recovery. The authored contract limits it to a same-turn rewrite/retrace and one more finalize:

>    - if the first finalize attempt returns `status = execute` with a repairable `support_fulfillment`, keep the same turn open, do one contract-aware rewrite and retrace, then finalize once more
>    - do not open a second or unbounded repair loop; the second finalize attempt must close honestly
> --- `skills/canonical/ask/SKILL.md`

This is a protocol limit on host repair, not an established hard wrapper retry counter. The wrapper's internal missing-trace retry is a distinct mechanism and does not itself rewrite answer content. Neither mechanism demonstrates factual correctness or universal mediation of out-of-band host answers.

### Delivery

Inner-workflow completion is not final user delivery. Ask owns terminal closure after admissibility and canonical commit. The business text remains unchanged, with a separate concise completion line; governance detail is exposed for boundaries/blockers or explicit inspection rather than appended to copy-ready content. Final delivery is the answer or explicit boundary returned cleanly from that canonical turn, with linked logs and support state (SRC-1, `skills/canonical/ask/SKILL.md`; [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask)). The supplied runtime record retains the verbatim rule that only `completed` or `boundary` permits a final business reply. Waiting or blocked JSON is therefore not a delivered ordinary answer.

Persistence includes answer Markdown, turn/run ownership, linked retrieval sessions and traces. Later continuation reloads that state rather than relying only on chat adjacency. Actual return to a user, adherence to the repair limit, and resulting answer quality are unobserved. Host inference, permissions and isolation remain external; canonical checking does not prevent arbitrary host shell/file access or an ungoverned reply.

Additional SRC-1 inspection covered the complete `skills/canonical/grounded-answer/SKILL.md`, the routing-through-delivery portion of `skills/canonical/ask/SKILL.md`, and the full `finalize_canonical_ask` function in `src/docmason/host_integration.py`. These add doctrine/design and implementation coverage within the registered commit, not another source or observed-run layer. Other inner workflows and a complete refresh implementation audit were not selected; no exhaustive workflow or reliability conclusion follows.

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

#### On [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask)

Workflow recovery ownership: the wrapper can recover missing trace bindings without asking the host to redraft, but semantic repair returns to the host on the same turn. In `finalize_canonical_ask`, automatic recovery is conditional on `missing-ask-owned-trace` and absent explicit session/trace selections. It calls `_autotrace_finalize_ids` and retries completion with recovered IDs. Repairable admission errors build a repair contract and restore prepared state (SRC-1, `src/docmason/host_integration.py`):

>                 updates={
>                     "status": "prepared",
>                     "turn_state": "prepared",
>                     "noncanonical_answer_file_path": None,
>                     "admissibility_repair": repair_contract,
>                 },
> --- `src/docmason/host_integration.py`

Nonrepairable completion errors take a separate artifact-handling path before returning blocked:

>         quarantined_path = quarantine_noncanonical_answer_file(
>             paths,
>             conversation_id=conversation_id,
>             turn_id=turn_id,
>             retain_canonical=True,
>         )
> --- `src/docmason/host_integration.py`

This establishes an invoked quarantine handoff and returned path, not a full audit of the helper's file handling or crash durability. The host's one-rewrite limit and final-delivery restriction remain protocol obligations. No observed recovery, independent semantic oracle or guarantee over arbitrary host replies is established.
