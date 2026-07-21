---
description: "Agents reproduce active framework content, but the durable contribution is usually the recognition that the situation fits the framework; default to minimal prose plus a framework link"
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering]
---

# The framework is often larger than the durable contribution

An agent writing about a situation that fits a familiar framework has that framework active — loaded into context or activated in weights — and active knowledge tends to leak into the artifact. The strongest case is discovery: an authoring agent uses a large body of familiar knowledge to derive a small contribution and reproduces the derivation. But no derivation is required; an agent that merely names framework X tends to pad the artifact with X's details. Either way, a future consumer with access to the same parametric knowledge can reconstruct the framework; what changed was the recognition that this situation is an instance of it.

The size of what was active during writing is therefore a poor guide to retained size. The framework content explains what the author drew on, but only the parts future consumers cannot reliably reconstruct or activate must survive. Which parts those are remains [observer-relative](./information-value-is-observer-relative.md).

## Recognition can be the durable contribution

When an artifact applies a familiar framework to a particular case, the durable contribution may be only:

> When **this observable condition** occurs, treat **this apparent task** as **this named kind of problem**, and use the corresponding framework to **perform this operation**.

The framework name addresses knowledge the consumer can reconstruct; the condition, mapping, and operation preserve what it did not reliably supply. Repeating the framework adds value only when it supplies something the name cannot: accessibility, disambiguation, warrant, or fidelity.

By that same measure, framework content — or the derivation that produced the contribution — must remain wherever it carries one of those values — when it is evidence the consumer must be able to check, when the consumer cannot reconstruct it, or when a particular version or interpretation has authority. Stripping a derivation always trades away auditability: a claim without its reasoning must be taken on trust. Participating in discovery does not make every part of the reasoning path part of the discovery, but reconstructability alone does not make warrant or exactness expendable.

## Minimal by default, grown on demand

Reconstructability is not the only reason to compress. A note records one case, and what the case contributes is the recognition — the cue, the mapping, the local fact. The framework behind it is shared across many notes, so it belongs in an artifact of its own, linked rather than re-taught inline, since [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md). The write-time default is therefore minimal prose with a link standing where the framework recap would have gone: the graph carries the reconstructable load structurally, so no single note has to.

Minimal means minimal background, not minimal anchor. The dangerous compression cuts in the wrong direction: it drops the condition, mapping, or local fact — the case's actual contribution — while framework prose survives, or it drops the framework link entirely. The link matters because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md): the name and cue are what trigger the consumer's reconstruction, and without them it fails silently. The anchor — framework name, link, and recognition condition — costs one line and is non-negotiable; the tutorial is what gets cut.

The default is also the cheaper one to correct. Adding a missing warrant or example when a consumer demonstrably misses it — a failed behavioral test, a real miss in use — is cheap and targeted. Trimming a bloated note later is expensive: it means re-deriving the boundary between scaffolding and load-bearing material, the judgment the behavioral test below exists to settle. And at write time the consumer population is unknown: over-retention bakes in an assumption about a weak reader who may never arrive, while minimal-plus-linked defers the decision to read time, when the actual consumer is present. Grow on demand, not on imagination.

## Examples

### Cue only: heterogeneous parts activate ontology

Suppose a description of a reflective system puts software components, functional roles, processes, retained artifacts, and levels of description into one list of "parts." A capable agent already knows ontology. The useful note preserves the diagnostic connection:

> When proposed parts do not all stand in the same relation to the whole, treat the task as ontology design: distinguish entity kinds and parthood relations before enumerating components.

Ontology was needed to derive the rule, but consumers that can reconstruct it from the name do not need the tutorial repeated.

### Cue plus local fact: a timeout activates idempotency

Suppose a service charges a card and times out before acknowledging success. A software agent already knows idempotency, but it cannot infer the system-specific ordering. The project note should retain both the cue—treat retries as an idempotency problem—and the local fact that the irreversible action precedes acknowledgement. Generic distributed-systems guidance can be reconstructed; the duplicate-charge risk and relevant operation boundary cannot.

### Relation only: two systems share a mechanism

Suppose two systems use different terminology but both precompute a stable part of a later reasoning task and insert the result into a bounded call. The consumer may know both systems and understand partial evaluation without recognizing the relation between them. The note should retain the comparison, shared mechanism, and consequences, not teach either system or partial evaluation again. The contribution is the edge, not either endpoint.

## Test the retained boundary behaviorally

For an agent consumer, semantic inspection cannot establish whether a framework name is an adequate address. Compare representative behavior with the name alone, the name plus a recognition condition, and the fuller framework restatement or derivation. If a smaller form preserves the contribution's effect, the removed material was scaffolding; if behavior degrades, the missing explanation, example, or warrant belongs in the retained result.

The boundary varies with the model, task, and consumer population. The test establishes a validity window, not a timeless compression.

---

Relevant Notes:

- [Information value is observer-relative](./information-value-is-observer-relative.md) — grounds: consumer knowledge, capacity, tools, and goals determine which parts of the active framework add value when retained
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: retrievable knowledge may still require a situation-specific cue before it affects action
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — mechanism: generic guidance can be reconstructed at read time while the artifact carries the task-specific result of prior reasoning
- [Conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — mechanism: the discovery may be the instance relation rather than either already-known endpoint
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — grounds: shared frameworks live as their own composable artifacts, so each note carries only its case's contribution
