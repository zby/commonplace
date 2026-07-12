---
description: "RL paper formalizing environment-side artifacts as externalized memory and testing memory by capacity/performance counterfactuals."
source_snapshot: "artifacts-as-memory-beyond-agent-boundary.md"
ingested: "2026-06-30"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, learning-theory, situated-cognition, reinforcement-learning]
---

# Ingest: Artifacts as Memory Beyond the Agent Boundary

Source: artifacts-as-memory-beyond-agent-boundary.md
Captured: 2026-06-30
From: https://arxiv.org/abs/2604.08756

## Classification

Type: scientific-paper -- arXiv preprint with formal definitions, proofs, experiments, statistical tests, citations, and an empirical appendix.
Domains: agent-memory, learning-theory, situated-cognition, reinforcement-learning
Author: John D. Martin, Fraser Mince, Esra'a Saleh, and Amy Pajak; affiliations include Openmind Research Institute, University of Alberta, Cohere Labs Community, Universite de Montreal, Mila, and University of Pennsylvania.

## Summary

The paper formalizes a situated-cognition claim inside reinforcement learning: environment-side observations can function as memory when they reveal information about an agent's past. It defines artifacts as observations that imply prior observations, proves an artifact-reduction theorem showing such histories can be represented with fewer observations, and defines externalized memory by comparing performance and capacity between artifactual and artifactless environments. Gridworld experiments with Q-learning and DQN agents show spatial paths and landmarks can reduce the capacity needed to achieve comparable reward, sometimes unintentionally through the ordinary sensory stream rather than an explicit memory API.

## Connections Found

The source lands in the KB's agent-memory and learning-theory cluster. It supports [The adaptation survey corroborates memory requirements but misses artifact governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) by giving a primary formal case for "keep the model fixed, adapt the surrounding environment" as memory. It supports [Agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) and [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) because memory here is not a storage component; it is an effect of environment state, observation channel, policy, and task. It directly reinforces [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) by defining externalized memory through capacity/performance deltas. It also gives [Information value is observer-relative](../notes/information-value-is-observer-relative.md) a formal bounded-agent case: an artifact's value depends on what this agent can infer through this interface and task history.

## Extractable Value

1. **External memory is an agent-environment relation, not a storage location** -- High reach. The source sharpens the KB's memory boundary: a memory effect can arise when environment-side artifacts reduce internal representational burden, even without a conventional memory store. [quick-win]

2. **Effect-based memory evaluation can be made counterfactual** -- High reach. The paper's artifactual-vs-artifactless comparison gives a concrete evaluation shape for [effect-based memory evaluation](../notes/agent-memory-requirements/evaluate-memory-by-effects.md): hold agent design mostly fixed, vary the available memory-bearing artifact, and compare capacity required for matched performance. [experiment]

3. **Observer-relative information value has a clean RL instance** -- Medium-high reach. The artifact definition says an observation matters because it lets a bounded agent infer a past event under a particular interface. This gives the KB's observer-relative information note a more precise external source than general relevance-theory discussion. [quick-win]

4. **Situated artifacts are not automatically governed retained artifacts** -- High reach for KB design. Trails, landmarks, or paths can function as memory without provenance, authority, validation, or lifecycle controls; Commonplace-style retained artifacts add those governance properties when environment-side state must remain maintainable across future agent work. [deep-dive]

5. **Unintentional memory externalization is a real design risk/opportunity** -- Medium reach. Agents may exploit environmental traces without explicit memory objectives, which means memory effects can appear through ordinary tool/environment design. Harness and KB designers should look for implicit memory channels, not only named memory APIs. [experiment]

6. **The paper distinguishes memory effect from artifact existence** -- Medium reach. A visible path is not enough; the memory claim depends on capacity and reward comparisons against controls. That guards against over-labeling every persistent external object as "memory." [quick-win]

## Limitations (our opinion)

This is a preprint and the empirical domain is narrow: small simulated gridworld navigation with spatial paths, landmarks, and capacity-swept Q-learning/DQN agents. It does not test LLM agents, agentic coding harnesses, or knowledge-base artifacts directly. The formal artifact definition also uses total certainty about prior observations; the authors note that stochastic or action-encoding artifacts would require extensions. For Commonplace, the biggest transfer limit is governance: the paper shows that environment state can function as memory, but it does not address provenance, authority, review, lifecycle, or activation policies that [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) treats as necessary for maintained agent memory systems.

## Recommended Next Action

Write a note titled **External memory is an agent-environment relation, not a storage location**, connecting this source to [Agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md), [Information value is observer-relative](../notes/information-value-is-observer-relative.md), and [The adaptation survey corroborates memory requirements but misses artifact governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md).
