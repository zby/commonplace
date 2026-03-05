---
description: A deterministic transformation adds zero classical information but can make structure accessible to bounded observers — this reframe connects distillation and discovery depth as instances of the same gap.
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: seedling
---

# Information value is observer-relative because extraction requires computation

Classical information theory says a deterministic transformation of data produces no new information. Restructure a document, reorder training examples, extract a lemma from two proofs — Shannon entropy doesn't change. Yet these operations are obviously valuable. The gap is that classical theory assumes unbounded computation. For a bounded observer — an LLM with finite context and depth, a human with finite attention — a deterministic rearrangement can make previously inaccessible structure visible.

[Epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) (Finzi et al., 2026) gives this gap a name: the difference between the information present in data and the information a computationally bounded observer can extract. Naming the gap is useful because the KB has several notes that describe it operationally without recognising they're talking about the same thing.

## Where the gap shows up

**Distillation.** [Distillation](./distillation.md) takes a body of reasoning and extracts a focused artifact shaped by a context budget and a use case. Classically, this is lossy compression — it discards information. But for the target reader (a bounded agent), the distillate can be more valuable than the source, because the restructuring makes structure accessible that was present but unreachable within the reader's budget. Multiple distillations of the same source aren't redundant — each targets a different bound, so each makes different structure accessible.

**Discovery depth.** [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) identifies three depths of connection — shared feature, shared structure, generative model — and observes that recognition cost scales with depth. This is the same gap viewed from the other side. The structure connecting two notes is present in both from the start. A shallow observer (keyword search) can't see it. A deeper observer (an LLM reasoning about mechanism) can. The discovery hierarchy is a hierarchy of how much computation is needed to see structure that was always there.

## Measurement

Beyond naming the gap, the epiplexity paper offers a cheap estimation technique: **prequential coding** — the area under the loss curve above final loss. This measures how much learnable structure a bounded observer (a model) extracts from data as it trains. Two arrangements of the same content that yield different areas have different extractable structure for that observer.

This could be a practical tool. Compare two distillations of the same source by measuring how much structure a model extracts from each. Compare two orderings of the same context window. The measurement is a byproduct of normal training or fine-tuning — no extra infrastructure needed.

## Open Questions

- Is "bounded information extraction" genuinely one phenomenon, or are distillation and discovery two phenomena that happen to share a surface shape? Distillation is deliberate restructuring for a known audience. Discovery is finding structure you didn't know was there. The gap concept connects them, but the operations are quite different.
- Has anyone applied prequential coding to compare prompt or context arrangements in practice?

---

Relevant Notes:
- [distillation](./distillation.md) — instance: distillation is restructuring that makes structure accessible to bounded observers
- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: the recognition cost hierarchy reflects how much computation is needed to see structure that's already there

- [structure-activates-higher-quality-training-distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — source: names and formalises the gap between present information and extractable information

Topics:
- [learning-theory](./learning-theory.md)
