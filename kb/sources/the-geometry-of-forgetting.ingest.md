---
description: Embedding-memory paper arguing that interference and low effective dimensionality, not time decay, drive forgetting and false recall in similarity retrieval.
source_snapshot: the-geometry-of-forgetting.md
ingested: "2026-04-09"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, retrieval-architecture, forgetting, learning-theory]
---

# Ingest: The Geometry of Forgetting

Source: the-geometry-of-forgetting.md
Captured: 2026-04-09
From: https://arxiv.org/html/2604.06222v1

## Classification

Type: scientific-paper — arXiv preprint with controlled experiments, quantitative comparisons to human-memory benchmarks, explicit methods, and citations.
Domains: agent-memory, retrieval-architecture, forgetting, learning-theory
Author: Sambartha Ray Barman, Andrey Starenky, Sophia Bodnar, Nikhil Narasimhan, and Ashwin Gopinath — startup-affiliated authors plus an MIT-affiliated corresponding author; useful signal, but for this KB the experimental design matters more than author prestige.

## Summary

The paper argues that several canonical memory phenomena can emerge from retrieval geometry rather than from specifically biological machinery. Using embedding-based memory simulations, the authors claim that human-like forgetting is driven primarily by interference from competing memories rather than by passive temporal decay, that production embedding models are much more interference-prone than their nominal dimensionality suggests because their effective dimensionality is low, and that false memories can arise directly from semantic clustering in raw embedding space without any special engineering. Their broader thesis is that any system organizing information by meaning and retrieving by proximity inherits these tradeoffs: semantic usefulness, interference, and false recall come from the same geometry.

## Connections Found

The connection report found the strongest fit in the KB's memory-architecture cluster:

1. **[flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md)** — **grounds**: the paper provides a concrete mechanism for why flat embedding memories can degrade. Competitor density plus low effective dimensionality turns accumulation into interference, making "search pollution" a retrieval problem rather than just a folder-hygiene problem.

2. **[the fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md)** — **extends**: the comparative review maps the design space of agent memory systems; this paper adds a first-principles reason why vector-first, accumulation-heavy systems can become fragile as they scale.

3. **[memory-management-policy-is-learnable-but-oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md)** — **grounds**: AgeMem and other memory-policy systems treat forgetting as a policy problem. This paper explains why such a policy is structurally necessary: similarity-based memory does not stay neutral under growth.

4. **[knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md)** — **extends**: the paper offers a concrete candidate mechanism for activation failure in embedding systems: relevant items can remain stored yet lose the competition inside a crowded semantic neighborhood.

5. **[agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md)** and **[session-history-should-not-be-the-default-next-context](../notes/session-history-should-not-be-the-default-next-context.md)** — **grounds / extends**: both notes argue that accumulation is not free. This source sharpens that argument by showing a retrieval-space failure mode rather than only an organizational one.

Overall fit: the source does not mainly add another "memory system" to the survey. It adds a mechanistic explanation for why unrestricted semantic memory can become self-defeating and therefore why memory policy, separation, and loading discipline matter.

## Extractable Value

1. **Low effective dimensionality makes vector-memory interference a structural risk, not an edge case.** The paper's strongest transferable claim is not the human-memory analogy but the observation that production embedding models can behave as though they have only ~16 effective dimensions. If that is even roughly true in agent-memory settings, then accumulation without separation or strong filtering is predictably interference-prone. High reach: this explains *why* flat vector memory gets worse as it grows. [quick-win]

2. **Forgetting policy is load-bearing because similarity retrieval has a built-in crowding failure mode.** The paper turns "maybe we should prune memory" into a structural claim: competitor memories can change retrieval behavior even when the target memory is still present. High reach: this grounds forgetting, filtering, or typed separation as design necessities rather than optimization polish. [quick-win]

3. **False recall may be the cost of semantic usefulness, not just a bug to patch.** The source's most surprising claim is that false memories emerge from raw semantic geometry with no additional machinery. If this generalizes, then systems that maximize semantic clustering for retrieval are also manufacturing lure-like confusions by design. High reach: it frames mitigation as a tradeoff frontier rather than "remove the bug and keep all the capability." [deep-dive]

4. **Vector averaging is a destructive compression move when retrieval depends on angular distinctions.** The discussion's "vector averaging fallacy" is highly relevant to agent memory and summary pipelines: compressing nearby memories into centroids may erase the distinctions retrieval needs. Medium-to-high reach: it challenges a common architectural instinct in memory systems, conversation summarizers, and database deduplication. [experiment]

5. **The paper offers a useful continuum from fully emergent to boundary-condition-dependent phenomena.** DRM-style false memories require no extra conditions in their setup; forgetting requires competitors; spacing effects require specific noise and distractor regimes. Medium reach: this is a good way to sort which observed behaviors are likely fundamental to a retrieval architecture and which are tuning-sensitive. [just-a-reference]

6. **Activation failure may partly be retrieval competition, not only missing cues.** This is the best synthesis opportunity with the KB's activation-gap note: stored knowledge can fail to surface because semantically adjacent alternatives win the race. Medium reach: it suggests that some "the model didn't think of it" failures are actually architecture-sensitive retrieval failures. [experiment]

## Limitations (our opinion)

The paper's strongest results come from synthetic or highly controlled retrieval setups, not from production agent-memory systems. That matters. Claims about vector databases, RAG systems, or long-term agent memory are partly inference from the reported geometry rather than direct evaluation on real hybrid systems with lexical filters, metadata constraints, rerankers, or type-separated stores. In KB terms, this is similar to the caution in [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md): a mechanism shown in one regime may transfer, but the transfer is not automatic.

The paper is also strongest where it shows *that* certain signatures can be reproduced, weaker where it implies it has isolated the uniquely correct explanation. "Decay alone does not produce forgetting in this system" is more limited than "decay is not a real cause of forgetting" because the result depends on their chosen retrieval rule, decay kernel, noise model, and benchmark setup. Likewise, the DRM result shows that semantic clustering is sufficient to reproduce one kind of false recall in embeddings, not that the full phenomenology of human false memory has been explained.

The biological comparison can also flatter the story. The closest matches are selective: forgetting exponent and DRM false alarms. The paper itself reports larger mismatches for spacing and tip-of-tongue, and several of its most striking claims rest on approximate correspondence rather than tight quantitative fit. This weakens any strong "single unified memory theory" reading.

Finally, the bridge from "nominal dimensionality is misleading" to "every vector database will eventually forget" is rhetorically stronger than the evidence shown here. The low effective-dimensionality result is important, but it is measured on specific models and corpora. For KB purposes, the robust extractable claim is narrower: embedding geometry can create interference risk severe enough that separation, filtering, or alternative retrieval constraints become architecturally relevant.

## Recommended Next Action

Write a note titled **"Low effective dimensionality makes vector memory interference a structural risk"** connecting to [flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md), [the fundamental split in agent memory is not storage format but who decides what to remember](../agent-memory-systems/agentic-memory-systems-comparative-review.md), and [knowledge-storage-does-not-imply-contextual-activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md). The note would argue that vector-memory fragility is not just an empirical nuisance of current systems but a predictable consequence of low effective dimensionality plus similarity-based retrieval, which is why forgetting policy and memory separation belong in the core architecture.
