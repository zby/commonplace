---
source: https://arxiv.org/html/2606.01444v1
description: Category-theoretic framework for agentic scientific discovery systems that models artifact states as copresheaves and distinguishes retrieval, search, and discovery as structurally different operations — grounded in a materials-science case study.
captured: 2026-06-06
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Self-Revising Discovery Systems for Science

Author: Fiona Y. Wang, Markus J. Buehler (MIT)
Source: https://arxiv.org/html/2606.01444v1
Date: 2026

## Abstract

Scientific discovery involves more than generating answers—it requires revising the representational framework itself. This paper develops a category-theoretic framework for agentic discovery systems in materials science, where artifact states are modeled as copresheaves and discovery manifests as verified regime transitions using Kan extensions. The work distinguishes retrieval, search, and discovery as structurally different operations and instantiates the framework through two systems: Builder/Breaker (protein mechanics under Minimum Description Length gates) and CategoryScienceClaw (a typed knowledge-computation graph for mechanics research).

## Key Contributions

1. **Formal semantics for typed artifacts**: System states are copresheaves mapping artifact types to populations; provenance is captured as the category of elements.

2. **Discovery as regime transition**: Unlike search within fixed schemas, discovery changes admissible types and operations through verified transitions with Kan-extension transport.

3. **Quantitative MDL case study**: Builder/Breaker discovers "mode-conditioned compliance"—a new interaction type expressing protein flexibility through collective deformation participation.

4. **Categorical implementation layer**: CategoryScienceClaw materializes schemas, skills, gates, and discourse as typed objects and morphisms in a self-revising knowledge graph.

## Framework Components

- **Schema category** 𝒮_b: artifact types and allowed operations
- **Copresheaf** I_t: current artifact populations
- **Verified regime transition** u: 𝒮_b → 𝒮_b': preserves old evidence while enabling new types
- **Gates/verifiers**: MDL, AIC, peer review determine commitment
- **Kan obstruction**: isolated new types receive no transported content

## Scientific Implications

The framework formalizes how mechanistic insights guide AI design—tracking invariants, testing failure modes, and distinguishing novel structure from reparameterization mirror both good mechanical modeling and principled discovery systems.
