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

Classical information theory (Shannon, Kolmogorov) is the exception — it deliberately abstracts away the observer. Shannon entropy measures surprise given a probability model; Kolmogorov complexity measures the shortest generating program. Neither depends on who is observing. This abstraction is powerful for communication engineering but misses what matters for knowledge systems: the same content in a different arrangement can teach more, even though nothing changed by classical measures.

**TODO:** This literature survey is from the agent's training data, not systematic. Revisit with deep search once that capability is operational — there are likely more relevant traditions (philosophy of information, situated cognition) and specific results worth ingesting.

## Why this matters for the KB

The idea is well-established in other fields. What's specific to our context is applying it to the design of an agent-operated knowledge base, where the primary reader is an agent under [bounded context](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — every token loaded must earn its place.

### What to keep

Observer-relativity shapes inclusion decisions. A note's value depends on whether the agent can connect it to what it already has in context — an isolated fact is worth less than a design principle that links to five other notes, because the principle creates extraction opportunities across sessions. This is why [KB goals](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) matter: they define what the observer is trying to do, which determines what counts as valuable.

### How to present

Several KB conventions are optimizations for the agent observer:

- **[Title as claim](../instructions/WRITING.md)** — a claim title lets the agent extract the main point without loading the note. This is a distillation targeting the lowest-cost reading: scanning titles in an index.
- **Descriptions as retrieval filters** — the description field exists because the agent needs to decide relevance before reading the full note. A good description is a distillation for the "should I read this?" decision.
- **[Short composable notes](./short-composable-notes-maximize-combinatorial-discovery.md)** — many short notes give more combinatorial coverage than few long ones for a reader with bounded context.
- **[Progressive refinement](./constraining.md)** — each level (text → note → structured-claim) adds structure that makes the content more extractable. A structured claim with Evidence/Reasoning/Caveats is more accessible to an agent than the same argument in prose.

More broadly, [distillation](./distillation.md) creates value by reshaping knowledge for a specific observer. In information-theoretic terms this is lossy compression — it discards information. But for the target reader, the distillate can be more valuable than the source because it makes previously unreachable structure accessible. Multiple distillations of the same source aren't redundant — each targets a different observer.

### What observer-relativity doesn't help with

**[Discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) cost is observer-relative** but not easily optimized — the data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. [Naming](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) is the partial solution: once a structure has a name, recognizing instances becomes cheap.

**[Reverse-compression](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) is the failure mode** — expanding text without adding extractable structure. More tokens, no more value for the reader.

## Open Questions

- Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?
- Is the agent the only important reader? Humans read the KB too — during review, when directing inquiry, when evaluating quality — and the KB is published on the web for external readers.
- What should we assume about the agent — a frontier model with strong reasoning, or a weaker model that needs more scaffolding? The answer shapes what counts as "accessible structure."

---

Relevant Notes:

- [distillation](./distillation.md) — instance: restructuring that makes structure accessible to bounded observers
- [discovery is seeing the particular as an instance of the general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: recognition cost scales with abstraction depth
- [reverse-compression is the failure mode where LLM output expands without adding information](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) — instance: expansion that adds tokens without making more structure accessible
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — instance: the vocabulary that maximally reduces extraction cost for a bounded observer
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [Epiplexity paper](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — related formalization: epiplexity captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity
- [epiplexity-eli5](../work/information-measures/epiplexity-eli5.md) — examples: encrypted messages, shuffled textbooks, and chess notation illustrating observer-relative structure
