---
source: https://arxiv.org/abs/2202.05262
description: ROME paper — factual associations in GPT localize to mid-layer feed-forward modules and can be directly edited via rank-one weight updates, evidence that factual knowledge is stored as identifiable, editable computation rather than diffuse distributed representation.
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: ./types/snapshot.md
---

# Locating and Editing Factual Associations in GPT

Author: Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov
Source: https://arxiv.org/abs/2202.05262
Date: February 10, 2022 (v5: January 13, 2023)

**Paper ID:** arXiv:2202.05262

**Venue:** NeurIPS 2022

## Overview

This research examines how transformer language models store and retrieve factual information, demonstrating that "factual associations correspond to localized, directly-editable computations."

## Key Contributions

The researchers developed a causal intervention method to pinpoint neuron activations that influence factual predictions. Their findings revealed that middle-layer feed-forward modules play a crucial role in processing factual information when handling subject tokens.

## Methodology

The team introduced **Rank-One Model Editing (ROME)**, a technique that modifies feed-forward weights to update specific factual associations. Testing on a zero-shot relation extraction task showed ROME performed comparably to existing methods while offering advantages in maintaining both specificity and generalization on counterfactual assertions.

## Significance

The work suggests that "direct manipulation of computational mechanisms may be a feasible approach for model editing," providing insights into how language models encode and can be modified regarding factual knowledge.

## Resources

- **Code & Dataset:** Available at rome.baulab.info
- **Paper Length:** 35 pages, 30 figures
- **Classification:** cs.CL, cs.LG
