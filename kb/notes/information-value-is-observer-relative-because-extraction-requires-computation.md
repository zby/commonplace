---
description: Classical information measures miss accessibility — transforms that preserve or reduce Shannon entropy can make structure visible to bounded observers. Connects distillation and discovery as instances of the same computational-bounds gap.
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: seedling
---

# Information value is observer-relative because extraction requires computation

Classical information theory measures what's present in data, not what a particular observer can extract from it. Reorder training examples — Shannon entropy doesn't change, yet the reordered sequence may teach a model more. Distil a body of reasoning into a focused note — entropy decreases, information is discarded, yet the result may be more valuable to a bounded reader than the original. In both cases, classical theory misses what changed: the accessibility of structure to a computationally bounded observer — an LLM with finite context and depth, a human with finite attention.

[Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) (Finzi et al., 2026) formalises this phenomenon. The framework decomposes information into time-bounded entropy (irreducible randomness given computational constraints) and epiplexity (structural patterns extractable within those constraints). Epiplexity measures what a bounded observer *can* extract; the gap between that and the total structure present is what classical theory ignores. This decomposition is useful because the KB has several notes that describe the gap operationally without recognising they're talking about the same thing.

## Where the gap shows up

**Distillation.** [Distillation](./distillation.md) takes a body of reasoning and extracts a focused artifact shaped by a context budget and a use case. Classically, this is lossy compression — it discards information. But for the target reader (a bounded agent), the distillate can be more valuable than the source, because the extraction makes structure accessible that was present but unreachable within the reader's budget. Multiple distillations of the same source aren't redundant — each targets a different bound, so each makes different structure accessible.

**Discovery depth.** [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) identifies three depths of connection — shared feature, shared structure, generative model — and observes that recognition cost scales with depth. Under the epiplexity lens, this is the same gap viewed from the other side: the data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. A shallow observer (keyword search) sees shared features; a deeper observer (an LLM reasoning about mechanism) sees shared structure. The discovery note itself frames this constructively — the general concept doesn't exist until posited — but the computational-bounds reading is compatible: what counts as extractable structure in fixed data depends on the observer's computational depth.

## Measurement

Beyond naming the gap, the epiplexity paper offers a cheap estimation technique: **prequential coding** — the area under the loss curve above final loss. This measures how much learnable structure a bounded observer (a model) extracts from data as it trains. Two arrangements of the same content that yield different areas have different extractable structure for that observer.

This could be a practical tool. Compare two distillations of the same source by measuring how much structure a model extracts from each. Compare two orderings of the same context window. The measurement is a byproduct of normal training or fine-tuning — no extra infrastructure needed.

## Open Questions

- Is "bounded information extraction" genuinely one phenomenon, or are distillation and discovery two phenomena that happen to share a surface shape? Distillation is deliberate restructuring for a known audience. Discovery is finding structure you didn't know was there. The gap concept connects them, but the operations are quite different.
- Has anyone applied prequential coding to compare prompt or context arrangements in practice?

---

Relevant Notes:

- [distillation](./distillation.md) — instance: distillation is restructuring that makes structure accessible to bounded observers
- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: recognition cost scales with abstraction depth, which the epiplexity lens reads as computational bounds on structure extraction

- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — instance: MVO is the vocabulary that maximally reduces extraction cost for a bounded observer entering a domain
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — source: names and formalises the gap between present information and extractable information

Topics:

- [learning-theory](./learning-theory.md)
