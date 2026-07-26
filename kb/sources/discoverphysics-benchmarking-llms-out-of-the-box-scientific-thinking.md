---
source: https://arxiv.org/abs/2605.26087
description: Benchmark testing whether LLM agents can discover novel physics laws in simulated worlds with exotic physics through iterative experimentation, rather than recalling known physics — best agents solve only about half the worlds and struggle with latent structure discovery.
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking

Author: Matt L. Wiemann, Lindsay M. Smith, Peter Melchior, Siddharth Mishra-Sharma, Andrew Gordon Wilson, Pavel Izmailov, Carolina Cuesta-Lázaro
Source: https://arxiv.org/abs/2605.26087
Date: 25 May 2026

## Abstract

This paper introduces DiscoverPhysics, an interactive benchmark designed to assess whether large language models can genuinely reason scientifically or merely recall established knowledge. The benchmark tasks LLM agents with discovering the laws of motion in simulated worlds that deliberately deviate from our universe's physics.

### Key Features

The benchmark includes 22 distinct worlds governed by various exotic physics phenomena including:
- Screened and fractional-power gravity
- Multi-species particle couplings
- Hidden dark-matter-like particles
- Non-coordinate-free physics
- Time-varying interactions

Agents must "propose several rounds of experiments, observe raw trajectory data" and submit both natural language explanations and Python implementations of the inferred physical laws.

### Findings

Evaluation across eleven frontier models revealed:
- Strongest agents pass only approximately half the worlds
- Consistent failures occur when discovering latent structures
- Open-source models significantly underperform commercial variants
- Strong predictive accuracy doesn't guarantee quality conceptual explanations
- Successful understanding requires hypothesis refinement through well-designed experimentation

The research demonstrates that this benchmark effectively probes long-horizon reasoning and experimental design capabilities in LLMs.
