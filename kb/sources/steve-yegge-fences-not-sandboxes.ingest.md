---
description: "Practitioner report of a software factory where incident-driven rules become mechanical enforcement and a dedicated officer maintains the resulting governance corpus."
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

Yegge reports operating a software factory of roughly 50–60 agents whose accumulated clarifications, human verdicts, incident responses, and recurring practices became a constitution-like body of rules and enforcement mechanisms. He describes a lifecycle from custom, to advisory or warning, to written law, and finally to programs that refuse or flag disallowed actions; “fences” are these policy-boundary refusals, not security barriers against a malicious actor. After uncurated growth left obsolete rulings in the corpus, he created Frog, a dedicated officer assigned to consolidate cancelled rulings and address other overlooked work. The account is most useful as a concrete case of natural-language governance, retained deployment-time adaptation, and the maintenance burden created by behavior-shaping artifacts. Its claim that capable agents should be governed by fences instead of sandboxes should be read as a proposal for cooperative agents in one unusually expensive, domain-specific deployment, not as evidence that capability containment is obsolete.

## Quotes

- **Source extract (verbatim):** Over time, my "rulings" and "verdicts" became a body of case law. Every daily incident postmortem led to new rulings and new doctrine.
  - **Source location:** “The Rise of Rule of Law,” paragraph beginning “Over time, my ‘rulings’ and ‘verdicts’...”

- **Source extract (verbatim):** Once I popped the hood, I saw that they hadn't been curating it, just growing it. It had a lot of cruft — for instance, old rulings that were obsolete or had changed.
  - **Source location:** “The Rise of Rule of Law,” paragraph beginning “Did they do a good job of all this?”

- **Source extract (verbatim):** I minted a new Officer seat, Frog (Head of Wheelhouse Law), and put Frog to work on folding successive cancelled rulings, and a whole bunch of other stuff the agents had overlooked. It's a work in progress.
  - **Source location:** “The Rise of Rule of Law,” paragraph beginning “I minted a new Officer seat, Frog...”

- **Source extract (verbatim):** Wheelhouse has a whole system just for the lifecycle of rules/laws: proposing, evaluating, ratifying, enacting, enforcing, measuring, amending, and retiring them.
  - **Source location:** “The Rise of Rule of Law,” paragraph beginning “But on the whole, it was already a pretty solid system.”

## Connections Found

This source is a bounded practitioner anchor for [Legal drafting solves the same problem as context engineering](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) and [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md): it reports replaceable agents coordinating through text, while incidents and human verdicts become later-consumed doctrine, rules, gates, and programs. Its incident-to-law path also compares with [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../notes/theory-and-methodology-form-a-two-layer-execution-system.md): recurring operational judgments become narrower rules and then enforcement, while later evidence can amend or retire them.

Frog makes a dedicated refinement function visible inside that path. Consolidating cancelled rulings without losing their intended constraints plausibly requires the program-specific interpretation described by [Holding a program theory means sustaining coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md). The source does not expose Frog's reasoning or an explicit theory, so this is an architectural comparison rather than evidence that Frog is a demonstrated theory-holder. The source is also a maintenance witness for [Maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md), because the reported governance corpus accumulated obsolete rulings before it received a dedicated curator.

As a counterpoint to [Claude Fable 5 Made Most of My Agent Scaffolding Obsolete](./claude-workstream-kit-fable-agent-scaffolding.ingest.md), the account suggests that stronger models can reduce scaffolding used to compensate for weak task execution while increasing governance used to coordinate many capable workers. [Swamp](../agentic-systems/reviews/swamp.md) limits the source's substitution claim: its inspected control plane combines policy checks and approval gates with deployment isolation, showing that behavioral governance and capability containment answer different threat models.

## Extractable Value

1. **Textual doctrine can carry program-specific state across replaceable executions** -- The reported offices, jurisdiction, precedents, and constitution give the KB's legal-drafting parallel a concrete operational case: durable text lets new executions inherit authority and prior decisions without relying on one holder's memory. Yegge realizes this with many agents, but the retained-state mechanism does not depend on agent count. [quick-win]

2. **Operational feedback can harden across representational forms** -- Wheelhouse reportedly moves repeated violations from custom and warnings into authoritative text and then mechanical refusal or alerting. This is a useful deployment-time adaptation pattern because evidence changes later behavior without a model-weight update. [quick-win]

3. **Governance fences and security sandboxes solve different problems** -- A fence assumes an agent will honor a policy refusal; a sandbox limits available capabilities even when software or instructions are untrusted. Keeping that distinction explicit prevents a cooperative-governance case from being generalized into a containment claim. [quick-win]

4. **Behavior-shaping artifacts create their own maintenance load** -- The reported corpus of 450 legal artifacts contained obsolete and misclassified rulings, prompting a dedicated curation role and lifecycle for amendment and retirement. This is a bounded practitioner example of governance growth requiring separate detection and repair capacity. [just-a-reference]

5. **Frog may make theory refinement a dedicated system function** -- Frog's consolidation work sits between operational evidence and a governed lifecycle for amendment and retirement. Preserving intended behavior while revising its rule representation is consistent with a theory-holder role, but the source does not establish that Frog maintains an explicit theory. [deep-dive]

6. **Governance may be domain-grown rather than transplantable** -- Yegge presents Wheelhouse's rules as accumulated from one product's decisions, incidents, infrastructure, and human relationships. That cautions against copying the resulting rule corpus while preserving the reusable lifecycle for growing one locally. [just-a-reference]

## Limitations (our opinion)

This is a first-person report about one unusually resourced system. The capture provides no repository inspection, execution traces, controlled comparison, or independent measurements, so the throughput, artifact counts, behavioral effects, and model-judgment claims remain self-reported. The source also cannot isolate governance as the cause of the reported outcomes from model capability, token spend, operator attention, infrastructure investment, or the product's existing history.

The legal framing is suggestive but not itself an explanation of effectiveness. Shared terms such as constitution, jurisdiction, and case law do not establish that Wheelhouse reproduces the institutions that make human law work, and the report does not compare this design against a simpler policy-and-validation system. Its own account of obsolete rulings and rapid machinery growth shows that retained rules can preserve mistakes as well as learning.

The Frog passage establishes a maintenance assignment, not an explicit program theory. It supplies no prompt, retained self-model, reasoning trace, before-and-after rule revision, or causal evidence that Frog's interpretation changes later modification. Frog could be a theory-holder, an interpreter of theory distributed across Yegge and the artifact corpus, or a curator applying supplied criteria. The theory-refinement reading is therefore our architectural hypothesis.

The “fences, not sandboxes” conclusion assumes cooperative agents that respect a refusal. It does not address prompt injection, compromised tools, malicious extension code, credential exfiltration, or other cases where capabilities must remain structurally unavailable. Model-grade analogies and forecasts about imminent adoption are also rhetorical, model-specific, and not supported by an evaluation design.

## Recommended Next Action

Ingest a primary Wheelhouse artifact that exposes Frog's instructions or rule revisions as evidence for evaluating whether Frog performs the theory-holder functions in [Holding a program theory means sustaining coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).
