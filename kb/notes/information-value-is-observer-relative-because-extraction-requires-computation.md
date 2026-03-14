---
description: Classical information measures miss accessibility — transforms that preserve or reduce Shannon entropy can make structure visible to bounded observers. Connects distillation and discovery as instances of the same computational-bounds gap.
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Information value is observer-relative because extraction requires computation

Classical information theory measures what's present in data, not what a particular observer can extract from it. Reorder training examples — Shannon entropy doesn't change, yet the reordered sequence may teach a model more. Distil a body of reasoning into a focused note — entropy decreases, information is discarded, yet the result may be more valuable to a bounded reader than the original. Classical theory misses what changed: the accessibility of structure to a computationally bounded observer.

This applies at every level. A bounded learner can't find a regularity that requires more computation than its budget allows. A fact has little value for an observer who lacks the prior knowledge to act on it. A well-ordered textbook and a shuffled one contain the same information classically, but a student extracts far more from the ordered version. The gap between what's present and what's extractable is always relative to the observer.

## Where the gap shows up in the KB

**Distillation.** [Distillation](./distillation.md) takes a body of reasoning and extracts a focused artifact shaped by a context budget and a use case. Classically, this is lossy compression — it discards information. But for the target reader, the distillate can be more valuable than the source because it makes previously unreachable structure accessible. Multiple distillations of the same source aren't redundant — each targets a different observer, so each makes different structure accessible.

**Discovery.** [Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) identifies three depths of connection — shared feature, shared structure, generative model — and observes that recognition cost scales with depth. The data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. A shallow observer (keyword search) sees shared features; a deeper observer (an LLM reasoning about mechanism) sees shared structure.

Both are instances of observer-relative value, though the operations are quite different. Distillation is deliberate restructuring for a known audience. Discovery is recognizing structure you didn't know was there. Whether these are two aspects of one phenomenon or two phenomena that share a surface shape is an open question.

## Open Questions

- The title claims extraction requires "computation," but the fact case is about prior knowledge, not compute budget. Is there a unifying framing, or are these genuinely different mechanisms that both produce observer-relativity?

---

Relevant Notes:

- [distillation](./distillation.md) — instance: restructuring that makes structure accessible to bounded observers
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: recognition cost scales with abstraction depth, readable as computational bounds on extraction
- [reverse-compression is the failure mode where LLM output expands without adding information](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) — instance: expansion that adds tokens without making more structure accessible
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — instance: the vocabulary that maximally reduces extraction cost for a bounded observer entering a domain
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — related formalization: epiplexity captures the pattern-extraction aspect of observer-relativity (learnable structure a bounded model extracts from sequential data) but does not cover fact-level value
- [epiplexity-eli5](../work/information-measures/epiplexity-eli5.md) — examples illustrating observer-relative structure through encrypted messages, shuffled textbooks, and chess notation
