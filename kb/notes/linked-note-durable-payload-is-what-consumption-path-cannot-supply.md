---
description: "Retain the recognition anchor and rationale the intended consumption path cannot reliably supply — an enforced path can carry the anchor itself; reconstructable framework recap factors into the linked artifact, tested by downstream effects"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering]
---

# A linked note's durable payload is what its consumption path cannot reliably supply

A framework can occupy much of an author's working context without being the durable contribution of a particular case note. When intended consumers can reconstruct the framework from a linked artifact, the note should retain what the case adds: the recognition condition, the mapping to a problem type, the operation to perform, local facts, and any rationale unavailable elsewhere. Keep framework exposition or derivation inline only when the link cannot supply needed accessibility, disambiguation, warrant, provenance, or fidelity. The retention duty is relative to the intended consumption path: where an enforced path — a template that forces the condition, a validator that fires on it, a routing rule that applies the mapping — reliably supplies the recognition itself, the note need not repeat it, and what remains to retain is whatever that path cannot reliably supply.

The framework's size during writing is therefore a poor guide to what the finished note should contain. The boundary is [observer-relative](./information-value-is-observer-relative.md): it depends on what intended consumers can reconstruct faithfully, activate at the point of use, and verify when they dispute the mapping.

## Recognition can be the durable contribution

When a linked note applies a familiar framework to a particular case, its recognition anchor can take this form:

> When **this observable condition** occurs, treat **this apparent task** as **this named kind of problem**, and use the corresponding framework to **perform this operation**.

The linked framework supplies the shared concepts. The condition, mapping, and operation preserve the case-specific recognition that neither the consumer nor an enforced consumption path can reliably supply. But a framework address is not a substitute for a local reason. When the mapping is contestable or its reasoning cannot be recovered from a named source, retain the decisive premise, evidence edge, provenance pointer, or authoritative interpretation. [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md); familiarity with the generic framework cannot restore rationale that was never recorded.

## Place shared framework once; retain unrecoverable local reasons

The rule changes where material lives; it does not delete that material from the graph. A framework shared across many cases belongs in an artifact of its own, since [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md). Each case note keeps its recognition anchor and links to the shared treatment. This split works when the fuller treatment serves a conditional reader need. Content every intended reader needs still belongs inline because [links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md).

Compression cuts in the wrong direction when it preserves generic exposition but drops the condition, mapping, local fact, or framework address. The address and recognition condition matter because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). Without the cue, reconstructable knowledge may never affect action.

Omission is safe only when its effects can be tested and the omitted material can be recovered from a named source. If either condition fails, retain compact explanation or provenance now. Adding it after an observed miss works only when the omission is reversible; otherwise “grow on demand” discovers the loss too late.

## Examples

- **Cue only — heterogeneous parts activate ontology.** When proposed parts do not all stand in the same relation to the whole, identify the task as ontology design and distinguish entity kinds and parthood relations before enumerating components. Consumers who can reconstruct the framework from that address do not need an ontology tutorial inline.
- **Cue plus local fact — a timeout activates idempotency.** When a charge precedes acknowledgement, retain both the idempotency mapping and that system-specific ordering. Generic retry guidance is reconstructable; the duplicate-charge boundary is not.
- **Relation only — two systems share a mechanism.** When differently named systems both precompute a stable part of a later reasoning task, retain the comparison, shared mechanism, and consequences. The contribution is the edge, not a recap of either endpoint.

## Test the retained boundary behaviorally

Semantic inspection alone cannot establish whether a framework name is an adequate address. Following the rule to [evaluate memory by effects, not by existence](./agent-memory-requirements/evaluate-memory-by-effects.md), first define the required downstream effects: correct activation and task behavior, plus auditability or fidelity when the note promises them. Then compare representative behavior with three inputs: the framework name alone, the name plus the recognition anchor, and the fuller restatement or derivation. The first comparison tests the cue's contribution; the second tests the recap's. If the name plus anchor preserves the full version's effects and the omitted material remains recoverable, the recap was scaffolding for that consumer population. If behavior degrades or checking becomes impossible, retain the missing explanation, example, evidence, or rationale.

The boundary varies with the model, task, and consumer population. The test establishes a validity window, not a timeless compression.

---

Relevant Notes:

- [Information value is observer-relative](./information-value-is-observer-relative.md) — grounds: consumer knowledge, capacity, tools, and goals determine which parts of the active framework add value when retained
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — mechanism: generic guidance can be reconstructed at read time while the artifact carries the task-specific result of prior reasoning
- [Recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — mechanism: the contribution may be the recognized relation rather than either already-known endpoint
- [Ingest: Lessons from Building AI Agents for Financial Services](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — evidenced-by: a bounded practitioner report says some simple tasks moved from detailed step-by-step skills to short instructions as models improved, while the same system retained company-specific fiscal-period normalization and tests; treating this system-level contrast as evidence about durable model-facing payload is local analysis because the source does not say where the normalization enters the model's consumption path
- [Seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md) — evidenced-by: a seven-artifact audit where live source supplied exact facts while discovery cues and cross-component relations remained the durable payload
