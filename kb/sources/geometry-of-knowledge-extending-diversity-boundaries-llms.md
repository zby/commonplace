---
source: https://arxiv.org/html/2507.13874v2
description: Proposes a plug-in latent-conditioning framework that traverses semantic manifolds to expand LLM generation diversity without fine-tuning, with empirical gains on NoveltyBench and the Alternative Uses Test.
captured: 2026-04-23
capture: web-fetch
type: kb/sources/types/snapshot.md
tags: [academic-paper]
---

# Geometry of Knowledge Allows Extending Diversity Boundaries of Large Language Models

Author: Mateusz Bystroński, Doheon Han, Nitesh V. Chawla, Tomasz Kajdanowicz
Source: https://arxiv.org/html/2507.13874v2
Date: 2025 (arXiv preprint 2507.13874v2)

## Abstract

The paper proposes that semantic knowledge organizes along structured manifolds, enabling exploration to expand LLM generation diversity. By traversing continuous latent representations and conditioning generation through these vectors, the method systematically increases the model's reachable semantic range without parameter modification. The framework constructs conditioning distributions from diverse anchor generations and uses xRAG-style projection for embedding-space conditioning.

## Key Contributions

- Identifies structural limitations in prompt and agent-based diversity methods, showing variance bounds from finite conditioning contexts
- Introduces a plug-in latent-conditioning framework using continuous semantic exploration without fine-tuning
- Provides topological analysis explaining why VAE-style methods misalign with clustered LLM geometry
- Demonstrates substantial gains on NoveltyBench and Alternative Uses Test (AUT)

## Method Overview

**Continuous Semantic Conditioning:** The approach adds a continuous latent variable z in semantic embedding space. An encoder produces dense representations, and latent variables modulate context construction via multimodal projection into the LLM's token embedding space, enabling conditioning "directly in the language semantic space" without model modifications.

**Exploration Strategy:** Rather than VAEs (which require fine-tuning and face topological misalignment), the method uses anchor-based exploration. Initial diverse outputs are embedded into semantic space, forming discrete anchors. New vectors are sampled through interpolation and perturbation of these anchors, creating a continuous latent region supporting geometric search.

## Experimental Results

**NoveltyBench:** The method consistently outperforms baselines across generation budgets (10–30 samples), uncovering new semantic classes while maintaining high utility scores. At k=30, the approach achieves 16.65 distinct outputs versus 13.60 for G2 guidance.

**AUT (Divergent Thinking):** Latent-space exploration reaches Top-1 originality of 4.99 — approaching the practical upper bound of 5 — compared to 4.93 for G2 and 4.58 for multi-agent discussion.

## Limitations

- Lacks explicit low-quality or out-of-distribution generation detection beyond heuristic realignment
- Uses simplistic fixed-range linear interpolation ignoring local embedding geometry
- Depends heavily on anchor quality and embedding stack; robustness across different LLMs unexplored
