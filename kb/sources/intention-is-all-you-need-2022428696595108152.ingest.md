---
description: "Treats shared intent as the purpose input to human-agent coordination; through Naur, intention seeds system theory rather than replacing it."
source: https://x.com/matt_slotnick/status/2022428696595108152
captured: "2026-08-25T11:05:08.259238+00:00"
capture: xdk
genre: conceptual-essay
snapshot_sha256: a1cf7562376bb3ad4e832a0560b7ece4313a0149103a0d0b0172c4d304a6396c
ingested: "2026-08-25"
type: kb/sources/types/ingest-report.md
domains: [agent-orchestration, specification, verification, enterprise-systems]
status_id: 2022428696595108152
conversation_id: 2022428696595108152
post_count: 1
---

# Ingest: Intention Is All You Need

## Classification

This is a conceptual essay: it advances an architectural and market thesis through analogy and projection rather than reporting a controlled study or a documented implementation.
Author: @matt_slotnick offers a practitioner-style enterprise-software perspective and mentions personal experience, but the captured source provides no independent credentials or empirical provenance.

## Summary

The essay argues that enterprise software should move from organizing work around canonical business objects to organizing it around structured intentions: desired outcomes, constraints, assumptions, and evaluations that connect current context to human and agent action. It predicts that cheap agent execution will move the bottleneck toward defining and evaluating work, and proposes a self-closing observe, plan, act, evaluate, and adjust loop. Read through Naur's theory-building account, intention is the first-order purpose input to a theory: it states what the system is supposed to accomplish, while the theory must connect that purpose to the world, design choices, and coherent future modification. The framing is useful for reasoning about objective-centered coordination, but its market forecast and autonomy claims should not be treated as evidence that such systems work or displace governed records.

## Quotes

No source quotes have been retained yet.

## Connections Found

Compared with [Programming as Theory Building](programming-as-theory-building.ingest.md), the essay begins one layer later. Naur makes situated theory the basis of programming: it maps between affairs in the world and program structure, justifies design choices, and supports coherent responses to novel demands. In our synthesis, records and context describe what is, intention states what ought to become true, and theory explains why and how a system can bridge that gap. Slotnick's contribution is to make intention—the first-order purpose input to theory-building—a shared organizational artifact around which humans and agents coordinate. Intention therefore constrains the theory but is not itself the theory, a plan, or a sufficient control mechanism.

For an agent-operated KB, [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) supplies the bridge from Naur's human-held theory to an LLM-plus-artifact system: retained artifacts preserve addressable parts of the theory and the model interprets them. The resulting intention becomes operational only when a consumption path binds it to action selection and evaluation, as explained in [An action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md). Its structured form also fits the commitment boundary in [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), while [Specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) qualifies the assumption that useful specificity is always available before execution. As practitioner corroboration, the essay supports the role shift described in [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../notes/increasing-computational-autonomy-relocates-human-effort.md); as a limitation, [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) explains why faster execution does not by itself close a reliable loop. Compared with [Palantir Ontology vs Decision Traces](palantir-ontology-vs-decision-traces.ingest.md), shared intention is a purpose-bearing coordination surface above canonical ontology and workflow receipts, but the essay's own concession that records remain prerequisites keeps it dependent on governed state.

## Extractable Value

1. **Intention is a first-order input to system theory, not a substitute for it.** Desired outcomes and constraints state what the system is supposed to accomplish; theory connects that purpose to current reality, design choices, and coherent future modifications. Slotnick adds the organizational claim that this input should be shared across human-agent coordination. [just-a-reference]
2. **Structured intent separates commitments from runtime discretion.** Outcomes, constraints, assumptions, and evaluation criteria can be fixed while plans remain revisable, giving a concrete application of the existing boundary between what an author must determine and what an executor can determine from live context. [quick-win]
3. **Cheap execution relocates rather than removes human work.** The essay supplies a concise practitioner example of people moving toward environment design, intent specification, and feedback-loop judgment, but its evidential role should remain corroborative because it reports no measured labor outcome. [just-a-reference]
4. **Canonical state and raw context are complements, not substitutes.** The tension between letting agents read the uncompressed “territory” and retaining systems of record as prerequisites suggests a useful comparison with governed semantic layers and ontologies: broader context does not itself provide shared definitions, authority, or stable state. [deep-dive]
5. **The three-layer stack hides consequential orchestration choices.** Context, intention, and action name useful functions, but they leave policy form, scheduler placement, persistence, approvals, coordination guarantees, and return artifacts unspecified; the framing is therefore a checklist seed rather than an implementable architecture. [quick-win]

## Limitations (our opinion)

In our opinion, the essay's strongest claims are projections supported mainly by analogy, selected examples, and asserted practitioner experience. It provides no implementation, baseline, failure cases, or outcome measurements for an intention-centered system. Its coding example may not generalize to domains whose state is physical, institutionally contested, or expensive to verify. The claim that agents can work with the “territory” also understates the need for governed definitions and authoritative state, despite conceding that systems of record remain prerequisites. More fundamentally, its context-intention-action stack omits the theory-building step that relates purpose to domain, design, and modification: a structured intention tells the system what outcome to pursue, not why a proposed system or plan is coherent. More specific intent cannot compensate for understanding that emerges only during execution, and a fast operational loop can amplify error unless a sufficiently discriminating verifier closes it, as [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) argues. Finally, an observe-plan-act-evaluate loop is not by itself evidence that the deployed system learns or improves its behavior-determining organization.

## Recommended Next Action

Retain this ingest as the retrieval point for the relationship between shared intention and Naurian theory-building until concrete Commonplace design work creates a reason to promote the distinction.
