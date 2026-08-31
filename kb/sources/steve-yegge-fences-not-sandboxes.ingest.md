---
description: "Practitioner report of a 50–60-agent software factory where incidents and human rulings mature into textual doctrine, policy fences, and mechanical enforcement."
source: https://yegge.ai/essays/fences-not-sandboxes/
captured: "2026-08-31"
capture: trafilatura
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 679cb9a1178431f431e4003eb303e4eb4dac76cecd26fa6b5888b88e1b89174d
ingested: "2026-08-31"
type: kb/sources/types/ingest-report.md
domains: [agent-governance, context-engineering, deploy-time-learning, kb-maintenance]
---

# Ingest: Fences, not Sandboxes

## Classification

This is primarily a practitioner report: it uses a first-person account of operating Wheelhouse to motivate a broader conceptual argument and forecast about multi-agent governance.
Author: Steve Yegge writes as Wheelhouse's operator and the person funding and directing the reported deployment, giving him direct access to the system and its operating incidents; the capture supplies no independent inspection or corroboration of his claims.

## Summary

Yegge reports operating a software factory of roughly 50–60 agents whose accumulated clarifications, human verdicts, incident responses, and recurring practices became a constitution-like body of rules and enforcement mechanisms. He describes a lifecycle from custom, to advisory or warning, to written law, and finally to programs that refuse or flag disallowed actions; “fences” are these policy-boundary refusals, not security barriers against a malicious actor. The account is most useful as a concrete case of natural-language governance, retained deployment-time adaptation, and the maintenance burden created by behavior-shaping artifacts. Its claim that capable agents should be governed by fences instead of sandboxes should be read as a proposal for cooperative agents in one unusually expensive, domain-specific deployment, not as evidence that capability containment is obsolete.

## Quotes

No source quotes have been retained yet.

## Connections Found

This source is a bounded practitioner anchor for [Legal drafting solves the same problem as context engineering](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) and [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): it reports replaceable agents coordinating through text, while incidents and human verdicts become later-consumed doctrine, rules, gates, and programs. It is also a maintenance witness for [Maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md), because the reported governance corpus accumulated obsolete rulings and required a dedicated curation role.

As a counterpoint to [Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](./claude-workstream-kit-fable-agent-scaffolding.ingest.md), the account suggests that stronger models can reduce scaffolding used to compensate for weak task execution while increasing governance used to coordinate many capable workers. [Swamp](../agentic-systems/swamp.md) limits the source's substitution claim: its inspected control plane combines policy checks and approval gates with deployment isolation, showing that behavioral governance and capability containment answer different threat models.

## Extractable Value

1. **Textual law can serve as multi-agent coordination state** -- The reported offices, jurisdiction, precedents, and constitution give the KB's legal-drafting parallel a concrete operational case: durable text lets replaceable agents inherit authority and prior decisions without relying on a holder's memory. [quick-win]

2. **Operational feedback can harden across representational forms** -- Wheelhouse reportedly moves repeated violations from custom and warnings into authoritative text and then mechanical refusal or alerting. This is a useful deployment-time adaptation pattern because evidence changes later behavior without a model-weight update. [quick-win]

3. **Governance fences and security sandboxes solve different problems** -- A fence assumes an agent will honor a policy refusal; a sandbox limits available capabilities even when software or instructions are untrusted. Keeping that distinction explicit prevents a cooperative-governance case from being generalized into a containment claim. [quick-win]

4. **Behavior-shaping artifacts create their own maintenance load** -- The reported corpus of 450 legal artifacts contained obsolete and misclassified rulings, prompting a dedicated curation role and lifecycle for amendment and retirement. This is a bounded practitioner example of governance growth requiring separate detection and repair capacity. [just-a-reference]

5. **Model-management scaffolding and organization-management governance may move in opposite directions** -- Read with the Fable scaffolding report, this source motivates a synthesis: stronger models may need fewer procedural proxies for performing one task while a larger population of capable agents needs more durable authority, coordination, and institutional memory. [deep-dive]

6. **Governance may be domain-grown rather than transplantable** -- Yegge presents Wheelhouse's rules as accumulated from one product's decisions, incidents, infrastructure, and human relationships. That cautions against copying the resulting rule corpus while preserving the reusable lifecycle for growing one locally. [just-a-reference]

## Limitations (our opinion)

This is a first-person report about one unusually resourced system. The capture provides no repository inspection, execution traces, controlled comparison, or independent measurements, so the throughput, artifact counts, behavioral effects, and model-judgment claims remain self-reported. The source also cannot isolate governance as the cause of the reported outcomes from model capability, token spend, operator attention, infrastructure investment, or the product's existing history.

The legal framing is suggestive but not itself an explanation of effectiveness. Shared terms such as constitution, jurisdiction, and case law do not establish that Wheelhouse reproduces the institutions that make human law work, and the report does not compare this design against a simpler policy-and-validation system. Its own account of obsolete rulings and rapid machinery growth shows that retained rules can preserve mistakes as well as learning.

The “fences, not sandboxes” conclusion assumes cooperative agents that respect a refusal. It does not address prompt injection, compromised tools, malicious extension code, credential exfiltration, or other cases where capabilities must remain structurally unavailable. Model-grade analogies and forecasts about imminent adoption are also rhetorical, model-specific, and not supported by an evaluation design.

## Recommended Next Action

Write a synthesis note titled `Strong models reduce model-management scaffolding but increase organization-management governance`, comparing this report with the Fable scaffolding and accumulated behavioral-rules ingests while using Swamp to preserve the distinction between policy governance and capability containment.
