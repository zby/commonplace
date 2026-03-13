---
description: Pre-training acquires both structural priors (evolution's role in humans) and world knowledge in one pass — making it and in-context learning intermediate on the evolution-to-reaction spectrum
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# LLM learning phases fall between human learning modes rather than mapping onto them

Human cognition has a hierarchy of adaptation timescales: evolution (species-level), long-term learning (years of experience), short-term learning (within a task or day), and immediate reaction (reflexive response). LLM training phases don't align with any one of these — they fall at intermediate positions on the spectrum.

[Dario Amodei](https://www.dwarkesh.com/p/dario-amodei-2) frames this clearly: "We should think of pre-training — and for that matter, RL as well — as something that exists in the middle space between human evolution and human on-the-spot learning. And we should think of the in-context learning that the models do as something between long-term human learning and short-term human learning."

## Why pre-training is between evolution and learning

Humans arrive with extensive evolutionary priors — specialized brain regions, sensory integration, motor programs, social cognition circuitry. The brain is not a blank slate. These priors were selected over millions of years and don't need to be individually learned.

LLMs start as random weights. Pre-training must do double duty: it acquires both the kinds of structural priors that evolution gives humans (syntax, basic reasoning patterns, common-sense physics) *and* the kinds of world knowledge that humans acquire through experience (facts, procedures, domain expertise). This is why pre-training is intermediate — it's more like learning than evolution (it happens in one "lifetime" of training), but more like evolution than learning (it shapes the basic cognitive architecture, not just the knowledge available to an already-formed mind).

## Why in-context learning is between long-term and short-term

Human long-term learning produces durable changes — you remember how to ride a bicycle, you internalize a programming language. Human short-term learning is ephemeral — working memory for the current task.

In-context learning splits the difference. It can handle surprisingly complex adaptation within a session (few-shot learning, instruction following, extended reasoning chains), which is more than short-term human learning typically achieves. But it's ephemeral — nothing persists across sessions. A human who spent hours working through a problem retains something. An LLM retains nothing once the context window closes.

## Deploy-time learning as a further intermediate

The KB's [three-timescale framework](./deploy-time-learning-the-missing-middle.md) adds deploy-time learning — adaptation through repo artifacts that are durable and inspectable but don't change weights. This is another phase that falls between human modes. It's durable like long-term human learning, but it works through external artifacts rather than internalized change. It resembles cultural evolution — knowledge accumulated in books, tools, and institutions rather than in individual minds — more than it resembles individual human learning.

## Why the non-mapping matters

The temptation is to find 1:1 correspondences: training = education, in-context = working memory, etc. These analogies are useful heuristics but become misleading when taken literally, because:

1. **Training conflates evolution and learning.** Treating pre-training as "education" misses that it also builds the basic cognitive architecture. A human educated in physics still has the same sensory cortex as one who wasn't. A model trained on physics has different weights at every layer.

2. **In-context conflates learning and retrieval.** Human short-term memory mostly *retrieves* from long-term stores. LLM in-context "learning" is doing something different — it's conditioning the model's entire distribution, not accessing a separate store.

3. **No LLM analogue for embodied procedural learning.** Humans learn through physical practice in ways that have no LLM counterpart. Riding a bicycle changes the cerebellum; no amount of text about bicycles produces an equivalent.

The implication for knowledge system design: rather than mapping agent memory to human memory taxonomies (the [Tulving mapping](./three-space-agent-memory-maps-to-tulving-taxonomy.md) is a partial example), we should work from the actual properties of each LLM phase. The [human-LLM differences note](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) already argues for evaluating each convention individually rather than wholesale adopting human analogies — the Amodei spectrum shows why this is necessary at the level of learning mechanisms themselves, not just at the level of document conventions.

## Open Questions

- Where does RLHF/RLAIF fall on the spectrum? It's post-pre-training but pre-deployment, and it shapes behavioral tendencies rather than factual knowledge — closer to socialization than to either evolution or learning?
- As models get larger, does pre-training shift toward the "evolution" end (acquiring more structural priors) or the "learning" end (acquiring more specific knowledge)?
- Does the intermediate position of in-context learning explain why few-shot prompting works so well? It's leveraging a mode that has more capacity than short-term human memory but less than long-term human learning — a sweet spot that humans don't have a clean analogue for.

---

Sources:

- [Dario Amodei — "We are near the end of the exponential"](../sources/dario-amodei-we-are-near-the-end-of-the-exponential.md) — the spectrum framing: pre-training between evolution and learning, in-context between long-term and short-term

Relevant Notes:

- [deploy-time learning: the missing middle](./deploy-time-learning-the-missing-middle.md) — extends: adds deploy-time as a fourth phase that also falls between human modes; the three-timescale framework is the KB's version of the spectrum Amodei describes
- [human-LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — foundation: argues for evaluating each convention individually; this note extends the argument to learning mechanisms themselves
- [three-space agent memory maps to Tulving's taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — tension: the Tulving mapping is a human-to-LLM analogy of exactly the kind this note warns about, though it may still be useful if taken as suggestive rather than structural
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: Simon's definition of learning as capacity change applies regardless of which human mode a phase maps to
- [structure activates higher-quality training distributions](./structure-activates-higher-quality-training-distributions.md) — example: structured templates leverage the properties of pre-training specifically (what distributions were seen), not any human learning analogy
