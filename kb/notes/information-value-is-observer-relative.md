---
description: The value of information depends on the observer — prior knowledge, computational capacity, tools, and goals determine what they can extract. Grounds distillation, discovery, and context arrangement as observer-relative operations.
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Information value is observer-relative

The same information has different value for different observers. A chess grandmaster and a beginner look at the same game notation — the grandmaster extracts strategic themes, preparation choices, and novelties; the beginner sees legal moves. An encrypted message is noise for Eve and a structured pattern for Bob. A domain fact is actionable for an expert and meaningless for a newcomer who lacks the context to interpret it.

This is not just about difficulty. The observers are not seeing the same thing at different speeds — they are extracting different structure from the same data. What makes information valuable is not a property of the data alone but of the data-observer pair: the observer's prior knowledge, computational capacity, available tools, and goals. The grandmaster extracts preparation choices from the game notation not just because she *can* see them but because competitive play makes them *relevant*.

Classical information theory doesn't capture this. Shannon entropy measures surprise given a probability model. Kolmogorov complexity measures the shortest program that generates the data. Neither depends on who is doing the observing. Reorder training examples — entropy doesn't change, yet the reordered sequence may teach a model more. Distil a body of reasoning into a focused note — entropy decreases, information is discarded, yet the result may be more valuable to a bounded reader. Classical theory describes data as an object; observer-relativity describes data as a relationship.

## Why this matters for the KB

The primary reader of this KB is an agent operating under [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — every token loaded must earn its place. Observer-relativity means the same content can have different value depending on how it's arranged, what the agent already has in context, and what tools it brings.

**[Distillation](./distillation.md) creates value** by reshaping knowledge for a specific observer. Classically this is lossy compression — it discards information. But for the target reader, the distillate can be more valuable than the source because it makes previously unreachable structure accessible. Multiple distillations of the same source aren't redundant — each targets a different observer.

**[Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) cost is observer-relative.** The data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. A shallow observer (keyword search) sees shared features; a deeper observer sees shared structure.

**[Reverse-compression](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) is the failure mode.** Expanding text without adding extractable structure — more tokens, same value for the reader. Observer-relativity is what makes this a real failure, not just verbosity: the expanded text carries more classical information but no more usable structure.

**Naming reduces extraction cost.** [Minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — the set of names that maximally reduces extraction cost for a bounded observer — is an optimization over the observer-relative gap. Once a structure has a name, recognizing instances becomes cheap.

## Open Questions

- Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?
- Is the agent the only important reader? Humans read the KB too — during review, when directing inquiry, when evaluating quality — and the KB is published on the web for external readers. Should we optimize for the agent observer, human readers, or some compromise? And what should we assume about the agent — a frontier model with strong reasoning, or a weaker model that needs more scaffolding? The answer shapes what counts as "accessible structure."

---

Relevant Notes:

- [distillation](./distillation.md) — instance: restructuring that makes structure accessible to bounded observers
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: recognition cost scales with abstraction depth
- [reverse-compression is the failure mode where LLM output expands without adding information](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) — instance: expansion that adds tokens without making more structure accessible
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — instance: the vocabulary that maximally reduces extraction cost for a bounded observer
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — related formalization: epiplexity captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity
- [epiplexity-eli5](../work/information-measures/epiplexity-eli5.md) — examples: encrypted messages, shuffled textbooks, and chess notation illustrating observer-relative structure
