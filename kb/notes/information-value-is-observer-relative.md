---
description: "Information value is observer-relative: prior knowledge, tools, compute, and goals determine extractable structure, grounding use-shaped reshaping and discovery."
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, discovery]
---

# Information value is observer-relative

What makes information valuable is not a property of the data alone but of the data-observer pair: the observer's prior knowledge, computational capacity, available tools, and goals all determine what they can extract.

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

Observer-relativity also determines resolution. The minimum required content of retained prose is the gap between what its target use requires and what its intended consumers can reliably contribute from parametric knowledge, loaded context, live inspection, tools, or reasoning. The gap may be:

- **Substance** the consumer lacks: facts, observations, arguments, or methods.
- **A connection the consumer will not reliably make:** a relation, recognition condition, or operation that activates otherwise familiar knowledge.
- **What reconstruction cannot preserve:** warrant, provenance, exact wording or membership, a governing version, or an authoritative local choice.

Reconstructability and activation are separate tests because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md). A model may explain a framework perfectly when asked yet fail to recognize the present situation as an instance of it. When its name reliably activates the framework, the artifact can retain the problem mapping rather than a tutorial; when exactness, evidence, or authority matters, the full content must remain or be reliably loadable.

For agent consumers, test resolution behaviorally: compare a bare name, a name plus recognition condition, and fuller content, then retain the least detail that preserves the intended effect. The result depends on the consumer population. A cue that resolves for one model may fail for another, while a compact agent-facing note may be opaque to a first-time human. Self-containedness therefore means supplying what intended consumers need, not reproducing everything relevant to the topic.

### How to present

Several KB conventions are optimizations for the agent observer:

- **[Title as claim](./COLLECTION.md)** — a claim title lets the agent extract the main point without loading the note. It is a precomputed view for the lowest-cost reading: scanning titles in an index.
- **Descriptions as retrieval filters** — the description field exists because the agent needs to decide relevance before reading the full note. A good description reshapes the note for the "should I read this?" decision.
- **[Short composable notes](./short-composable-notes-maximize-combinatorial-discovery.md)** — many short notes give more combinatorial coverage than few long ones for a reader with bounded context.
- **[Progressive refinement](./definitions/constraining.md)** — each level (text → note → structured-claim) adds structure that makes the content more extractable. A structured claim with Evidence/Reasoning/Caveats is more accessible to an agent than the same argument in prose.

More broadly, reshaping knowledge for a specific observer creates value. In information-theoretic terms this is lossy compression — it discards information. But for the target reader, the reshaped view can be more valuable than the source because it makes previously unreachable structure accessible. Multiple observer-shaped views of the same source aren't redundant — each targets a different observer.

### What observer-relativity doesn't help with

**[Discovery](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) cost is observer-relative** but not easily optimized — the data from which a connection could be inferred is present before anyone sees it, but extracting the pattern requires computation that scales with abstraction depth. [Naming](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) is the partial solution: once a structure has a name, recognizing instances becomes cheap.

**[Reverse-compression](./reverse-compression-is-when-llm-output-expands-without-adding.md) is the failure mode** — expanding text without adding extractable structure. More tokens, no more value for the reader.

## Open Questions

- Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?
- Is the agent the only important reader? Humans read the KB too — during review, when directing inquiry, when evaluating quality — and the KB is published on the web for external readers.
- What should we assume about the agent — a frontier model with strong reasoning, or a weaker model that needs more scaffolding? The answer shapes what counts as "accessible structure."

---

Relevant Notes:

- [theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — instance: a task-facing layer can make source structure more accessible to a bounded observer
- [conjecture is seeing the particular as an instance of the general](./conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md) — instance: recognition cost scales with abstraction depth
- [reverse-compression is the failure mode where LLM output expands without adding information](./reverse-compression-is-when-llm-output-expands-without-adding.md) — instance: expansion that adds tokens without making more structure accessible
- [minimum viable vocabulary](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — instance: the vocabulary that maximally reduces extraction cost for a bounded observer
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — instance: structured templates make structure accessible to autoregressive generation
- [Epiplexity paper](https://arxiv.org/html/2601.03220v1) — related formalization: epiplexity captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity
- [Epiplexity by example](./epiplexity-by-example-what-entropy-and-complexity-miss.md) — examples: encrypted messages, shuffled textbooks, and chess notation illustrating observer-relative structure
