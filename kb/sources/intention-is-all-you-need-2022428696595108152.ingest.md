---
description: "Frames structured shared intent as a control layer for human-agent work, bounded by governed state, active consumption, and verification."
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

The essay argues that enterprise software should move from organizing work around canonical business objects to organizing it around structured intentions: desired outcomes, constraints, assumptions, and evaluations that connect current context to human and agent action. It predicts that cheap agent execution will move the bottleneck toward defining and evaluating work, and proposes a self-closing observe, plan, act, evaluate, and adjust loop. The framing is useful for reasoning about objective-centered control, but its market forecast and autonomy claims should not be treated as evidence that such systems work or displace governed records.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay is a framing anchor for treating a shared objective as an operational control layer, not as another stored record: its promise rests on the intention being consumed by action selection and evaluation, as explained in [An action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md). Its structured-intent recipe also fits the commitment boundary in [An author should fix what the executor can't determine, not what it will](../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), while [Specification strategy should follow where understanding lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) qualifies the assumption that useful specificity is always available before execution. As practitioner corroboration, the essay supports the role shift described in [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../notes/increasing-computational-autonomy-relocates-human-effort.md); as a limitation, [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) explains why faster execution does not by itself close a reliable loop. Compared with [Palantir Ontology vs Decision Traces](palantir-ontology-vs-decision-traces.ingest.md), shared intention is a third organizing candidate beyond canonical ontology and workflow receipts, but the essay's own concession that records remain prerequisites keeps intention subordinate to governed state rather than replacing it.

## Extractable Value

1. **A shared objective is useful only as an active control interface.** The source's context-intention-action stack can be synthesized with the consumption-path note into a KB-relevant claim: an objective must bind current state, desired transition, authorized action selection, and outcome evaluation to affect an agent-operated system. [deep-dive]
2. **Structured intent separates commitments from runtime discretion.** Outcomes, constraints, assumptions, and evaluation criteria can be fixed while plans remain revisable, giving a concrete application of the existing boundary between what an author must determine and what an executor can determine from live context. [quick-win]
3. **Cheap execution relocates rather than removes human work.** The essay supplies a concise practitioner example of people moving toward environment design, intent specification, and feedback-loop judgment, but its evidential role should remain corroborative because it reports no measured labor outcome. [just-a-reference]
4. **Canonical state and raw context are complements, not substitutes.** The tension between letting agents read the uncompressed “territory” and retaining systems of record as prerequisites suggests a useful comparison with governed semantic layers and ontologies: broader context does not itself provide shared definitions, authority, or stable state. [deep-dive]
5. **The three-layer stack hides consequential orchestration choices.** Context, intention, and action name useful functions, but they leave policy form, scheduler placement, persistence, approvals, coordination guarantees, and return artifacts unspecified; the framing is therefore a checklist seed rather than an implementable architecture. [quick-win]

## Limitations (our opinion)

In our opinion, the essay's strongest claims are projections supported mainly by analogy, selected examples, and asserted practitioner experience. It provides no implementation, baseline, failure cases, or outcome measurements for an intention-centered system. Its coding example may not generalize to domains whose state is physical, institutionally contested, or expensive to verify. The claim that agents can work with the “territory” also understates the need for governed definitions and authoritative state, despite conceding that systems of record remain prerequisites. More specific intent cannot compensate for understanding that emerges only during execution, and a fast operational loop can amplify error unless a sufficiently discriminating verifier closes it, as [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) argues. Finally, an observe-plan-act-evaluate loop is not by itself evidence that the deployed system learns or improves its behavior-determining organization.

## Recommended Next Action

Draft a note provisionally titled “A shared objective is a control layer, not a record,” scoped to how agent-operated KBs bind objective artifacts to governed state, authorized action, and evaluation, using this ingest as conceptual framing rather than empirical support.
