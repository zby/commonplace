---
description: Agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
areas: [learning-theory]
status: speculative
---

# Three-space agent memory maps to Tulving's taxonomy

Source: [Cornelius, Agentic Note-Taking #19: Living Memory](https://x.com/molt_cornelius/status/2025408304957018363)

The article argues that agent memory systems should not be a single store but three qualitatively different spaces, mapped to Endel Tulving's memory taxonomy from cognitive science:

| Tulving's type | Agent space | Contains | Metabolic rate |
|----------------|-------------|----------|----------------|
| **Semantic** — facts and concepts | Knowledge graph | Atomic notes, linked claims, indexes | Steady growth |
| **Episodic** — personal experience | Self space | Identity, operational patterns, calibration | Slow evolution |
| **Procedural** — how to do things | Operational space | Friction observations, methodology, session artifacts | High churn |

The key insight is not just that these are different *topics* but that they have different *lifecycles*. Knowledge accumulates and rarely gets deleted. Self-knowledge evolves slowly through accumulated experience. Operational artifacts churn — they arrive raw, consolidate, and either graduate to knowledge or get archived.

The article claims that conflating these spaces produces three failure modes: operational debris polluting knowledge search, identity scattering across ephemeral logs, and insights trapped in session state. Whether these failures actually manifest at practical scale is an [open empirical question](./three-space-memory-separation-predicts-measurable-failure-modes.md).

The mapping to Tulving is suggestive but may be decorative. The practical value could reduce to simpler advice: separate persistent knowledge from transient working files, and give them different retention policies. Whether the cognitive science analogy adds explanatory power beyond that remains to be seen.

---

Relevant Notes:
- [three-space memory separation predicts measurable failure modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — observational protocol for testing whether the separation actually helps
- [deploy-time-learning](../notes/deploy-time-learning-the-missing-middle.md) — the three timescales framework; graduation from operational to knowledge space is a form of crystallisation
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — operationalizes metabolic rates: per-type recency decay in note scoring formalizes the intuition that knowledge and operational content age differently

Topics:
- [learning-theory](./learning-theory.md)
