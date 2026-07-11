---
description: "The value of separating knowledge, self, and operational memory is that each has a different lifecycle — accumulation, slow evolution, and high churn; whether the Tulving mapping adds explanatory power beyond different retention policies is open"
type: kb/types/note.md
tags: [learning-theory, agent-memory]
---

# Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative

Source: [Cornelius, Agentic Note-Taking #19: Living Memory](https://x.com/molt_cornelius/status/2025408304957018363)

The article argues that agent memory systems should not be a single store but three qualitatively different spaces, mapped to Endel Tulving's memory taxonomy from cognitive science:

| Tulving's type | Agent space | Contains | Metabolic rate |
|----------------|-------------|----------|----------------|
| **Semantic** — facts and concepts | Knowledge graph | Atomic notes, linked claims, indexes | Steady growth |
| **Episodic** — personal experience | Self space | Identity, operational patterns, calibration | Slow evolution |
| **Procedural** — how to do things | Operational space | Friction observations, methodology, session artifacts | High churn |

The key insight is not just that these are different *topics* but that they have different *lifecycles*. Knowledge accumulates and rarely gets deleted. Self-knowledge evolves slowly through accumulated experience. Operational artifacts churn — they arrive raw, consolidate, and either graduate to knowledge or get archived.

The article claims that conflating these spaces produces three failure modes: operational debris polluting knowledge search, identity scattering across ephemeral logs, and insights trapped in session state. Whether these failures actually manifest at practical scale is an [open empirical question](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md).

The mapping to Tulving is suggestive but may be decorative. The practical value could reduce to simpler advice: separate persistent knowledge from transient working files, and give them different retention policies. Whether the cognitive science analogy adds explanatory power beyond that remains to be seen.

---

Relevant Notes:

- [three-space memory separation predicts measurable failure modes](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — observational protocol for testing whether the separation actually helps
- [deploy-time-learning](./deploy-time-learning-is-the-missing-middle.md) — the three timescales framework; graduation from operational to knowledge space is a form of codification
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — operationalizes metabolic rates: per-type recency decay in note scoring formalizes the intuition that knowledge and operational content age differently
- [agentic memory systems comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — validates: evaluates the three-space taxonomy's analytical utility across 11 systems; uses the knowledge/self/operational split as the framework for comparing agency models and retention policies
- [memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — challenges: AgeMem separates memory by access pattern (persistent LTM vs active STM), not content type, and its unified RL-trained management outperforms independent optimization — evidence against structural isolation of memory spaces
