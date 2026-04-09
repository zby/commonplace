---
source: https://arxiv.org/html/2604.06222v1
description: Embedding-space account of human-like forgetting and false memory — interference, low effective dimensionality, and semantic clustering reproduce classic memory effects.
captured: 2026-04-09
capture: pdf-read
type: academic-paper
---

# The Geometry of Forgetting

Author: Sambartha Ray Barman, Andrey Starenky, Sophia Bodnar, Nikhil Narasimhan, Ashwin Gopinath
Source: https://arxiv.org/html/2604.06222v1
PDF: https://arxiv.org/pdf/2604.06222v1
Date: 2026-03-27
DOI: https://doi.org/10.48550/arXiv.2604.06222

## Abstract

Why do we forget? Why do we remember things that never happened? The conventional answer points to biological hardware. We propose a different one: geometry. Here we show that high-dimensional embedding spaces, subjected to noise, interference, and temporal degradation, reproduce quantitative signatures of human memory with no phenomenon-specific engineering. Power-law forgetting (`b = 0.460 ± 0.183`, human `b ≈ 0.5`) arises from interference among competing memories, not from decay. The identical decay function without competitors yields `b ≈ 0.009`, fifty times smaller. Time alone does not produce forgetting in this system. Competition does. Production embedding models (nominally 384-1,024 dimensions) concentrate their variance in only `~16` effective dimensions, placing them deep in the interference-vulnerable regime. False memories require no engineering at all: cosine similarity on unmodified pre-trained embeddings reproduces the Deese-Roediger-McDermott false alarm rate (`0.583` versus human `~0.55`) with zero parameter tuning and no boundary conditions. We did not build a false memory system. We found one already present in the raw geometry of semantic space. These results suggest that core memory phenomena are not bugs of biological implementation but features of any system that organizes information by meaning and retrieves it by proximity.

## Overview

The paper argues that several canonical features of human memory can emerge from similarity-based retrieval in embedding space rather than from specifically biological mechanisms. The authors model memories as contextually enriched embeddings retrieved by cosine similarity, then study how noise, temporal weighting, competitor density, and semantic clustering produce forgetting, false memories, spacing effects, and partial-retrieval states.

## Main Results

### Interference, not decay, produces forgetting

Using an Ebbinghaus-style simulation, the authors show that temporal decay alone produces an almost flat forgetting curve (`b ≈ 0.009`). Holding the decay function fixed while adding 10,000 distractors raises the exponent to `b = 0.460 ± 0.183`, close to the human reference value. Their claim is that forgetting in this setup is driven primarily by retrieval competition, not by trace dissolution.

### Effective dimensionality matters more than nominal dimensionality

The paper reports a "dimensionality illusion": several production embedding models advertised at 384-1,024 dimensions have effective dimensionality around 16 when measured by participation ratio. In the interference experiments, this low effective rank places them in a regime where nearby competitors can collapse retrieval quality despite high nominal dimensionality.

### False memories emerge from semantic clustering

Using the Deese-Roediger-McDermott word-list paradigm, the authors show that raw cosine similarity on pre-trained embeddings can reproduce a critical-lure false alarm rate of `0.583`, close to the human reference value of about `0.55`. Their interpretation is that false memories are not specially engineered failures but a direct consequence of organizing related concepts into nearby regions of semantic space.

### Spacing effects and tip-of-tongue states also appear

Under age-dependent noise and heavy distractor load, long-spaced repetitions outperform massed repetitions with the expected ordering: long > medium > short > massed. The paper also reports tip-of-tongue-like cases where the correct item ranks highly but not first. The authors explicitly frame these as more boundary-condition-dependent than the DRM-style false-memory result.

### Exploratory results extend the geometric story

The paper includes exploratory analyses of persistent-homology structure in the memory manifold and lightweight cross-modal alignment between text and image encoders. These are presented as descriptive extensions consistent with the broader geometric thesis rather than as central evidence for the forgetting claim.

## Discussion

The discussion generalizes the empirical results into a design claim: biological and artificial memory systems may share failure modes because both operate under low effective dimensionality, semantic clustering, noise, and competition. For artificial retrieval systems, the paper argues that vector databases and agent memories built on current embeddings are likely operating in an interference-vulnerable regime, and that common compression practices like averaging nearby vectors are geometrically destructive because they erase angular distinctions needed for retrieval.

The authors also propose a continuum from fully emergent phenomena to boundary-condition-dependent ones. DRM-style false memories sit at the "fully emergent" end because they require no added boundary conditions. Forgetting sits in the middle because it requires competitors. Spacing effects sit further toward the contingent end because they require specific noise and distractor regimes.

## Limitations Discussed By The Authors

- The experiments use English-language data only.
- The tip-of-tongue operationalization may be looser than the human phenomenological criterion.
- The spacing result depends on chosen noise and distractor parameters.
- The forgetting exponent matches human values but shows higher variance across seeds than human data.
- The strongest claims are demonstrated in synthetic retrieval setups rather than in production hybrid retrieval systems.
- Alternative decay functions, noise models, retrieval rules, languages, and hybrid architectures remain to be tested.

## Methods Snapshot

- Open-weight models only: Qwen2.5-7B for answer generation, MiniLM and BGE variants for embeddings, CLIP for image embeddings.
- Forgetting simulation: 1,000 facts over 30 simulated days with 10,000 distractors and power-law temporal weighting.
- Interference experiments: same-article versus cross-article distractors, PCA projections to varying dimensions, and age-proportional noise.
- False-memory experiment: all 24 published DRM word lists with threshold sweeps over cosine similarity.
- Spacing experiment: 100 facts with three repetitions across four spacing schedules under age-dependent noise.
- Effective dimensionality measured with participation ratio over PCA eigenvalues.

