---
description: The value of information depends on the observer — prior knowledge, computational capacity, tools, and goals determine what they can extract. Grounds distillation, discovery, and context arrangement as observer-relative operations.
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Information value is observer-relative

The same information has different value for different observers. At the most basic level, a reader might simply not know a fact — a domain expert recognizes "use OAuth 2.0 with PKCE" as a specific security decision, while a newcomer lacks the context to act on it. This is obvious but already observer-relative: the value of the fact depends on what the reader brings.

The less obvious case is structure extraction. A chess grandmaster and a beginner look at the same game notation — the grandmaster extracts strategic themes, preparation choices, and novelties; the beginner sees legal moves. An encrypted message is noise for Eve and a structured pattern for Bob. The observers are not seeing the same thing at different speeds — they are extracting different structure from the same data.

What makes information valuable is not a property of the data alone but of the data-observer pair: the observer's prior knowledge, computational capacity, available tools, and goals. The grandmaster extracts preparation choices not just because she *can* see them but because competitive play makes them *relevant*.

## Prior work

Observer-relative information value is not a new idea. Several traditions have developed it independently:

- **Relevance theory** (Sperber & Wilson, 1986) — information is relevant when it connects with existing assumptions to yield cognitive effects. Relevance is defined relative to the individual's cognitive environment, not as a property of the message.
- **Value of information in decision theory** (Marschak, Radner) — information has value only if it changes a decision. Two agents facing different decisions assign different value to the same data, even with identical processing capacity.
- **Bounded rationality** (Simon) — decision-makers have limited computational capacity, so they satisfice rather than optimize. The value of information depends on processing capacity, not just content.
- **Bayesian decision theory** — the expected improvement from observing data depends on the observer's prior beliefs and utility function.

Classical information theory (Shannon, Kolmogorov) is the exception — it deliberately abstracts away the observer. Shannon entropy measures surprise given a probability model; Kolmogorov complexity measures the shortest generating program. Neither depends on who is observing. This abstraction is powerful for communication engineering but misses exactly what matters for knowledge systems: reorder training examples and entropy doesn't change, yet the reordered sequence may teach a model more.

**TODO:** This literature survey is from the agent's training data, not systematic. Revisit with deep search once that capability is operational — there are likely more relevant traditions (philosophy of information, situated cognition) and specific results worth ingesting.

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
