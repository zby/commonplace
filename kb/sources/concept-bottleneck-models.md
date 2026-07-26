---
description: Models that predict human-understandable concepts as an intermediate bottleneck before the final task prediction, so a human can intervene on a wrong concept at test time and correct downstream errors without retraining
source: https://arxiv.org/abs/2007.04612
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# Concept Bottleneck Models

Author: Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen Mussmann, Emma Pierson, Been Kim, Percy Liang
Source: https://arxiv.org/abs/2007.04612
Date: July 9, 2020 (v1); last revised December 29, 2020 (v3)
arXiv: 2007.04612 (cs.LG, stat.ML)

Comments: "Edited for clarity from the ICML 2020 version"

## Abstract

> We seek to learn models that we can interact with using high-level concepts: if the model did not think there was a bone spur in the x-ray, would it still predict severe arthritis? State-of-the-art models today do not typically support the manipulation of concepts like "the existence of bone spurs", as they are trained end-to-end to go directly from raw input (e.g., pixels) to output (e.g., arthritis severity). We revisit the classic idea of first predicting concepts that are provided at training time, and then using these concepts to predict the label. By construction, we can intervene on these concept bottleneck models by editing their predicted concept values and propagating these changes to the final prediction. On x-ray grading and bird identification, concept bottleneck models achieve competitive accuracy with standard end-to-end models, while enabling interpretation in terms of high-level clinical concepts ("bone spurs") or bird attributes ("wing color"). These models also allow for richer human-model interaction: accuracy improves significantly if we can correct model mistakes on concepts at test time.

## Body extraction

Extracted from the paper's full text (HTML rendering) after the initial abstract-page capture; covers setup, training variants, datasets, results, interventions, and stated caveats.

### Setup and training variants

The architecture is `f(g(x))`: `g` maps input `x` to a vector of human-provided concepts `c`, and `f` maps concepts to the target `y`. Three ways to fit the pair:

- **Independent bottleneck** — `g` and `f` trained separately, `f` on *true* concepts `c`. At test time `f` receives predicted concepts `ĉ`, so there is a train/test distribution mismatch.
- **Sequential bottleneck** — `g` trained first, then `f` trained on `g`'s predicted concepts, so `f` adapts to `g`'s error profile.
- **Joint bottleneck** — minimizes a weighted sum of task loss and concept loss with hyperparameter `λ`.

The paper positions these on a spectrum: the standard end-to-end model is `λ → 0`, and the sequential bottleneck is `λ → ∞`.

### Datasets and concept acquisition

- **OAI** (Osteoarthritis Initiative), x-ray grading: 36,369 knee radiographs, 10 clinical concepts (joint space narrowing, bone spurs, and others) assessed by radiologists. Concepts are annotated per instance, so images sharing an arthritis grade can differ in concept values.
- **CUB** (Caltech-UCSD Birds), bird identification: 11,788 photos, 200 species, 112 binary attributes (wing color, beak shape). Concepts are assigned at the *class* level by majority vote, assuming all birds of a species share attribute values.

### Accuracy

- OAI: sequential and joint bottlenecks reach RMSE ≈ 0.418 against the standard model's 0.441.
- CUB: the standard model is slightly better (0.175 error vs. 0.199–0.243), with the joint bottleneck closing most of the gap.

The paper reports that bottleneck models achieve both competitive task accuracy and high concept accuracy, with no apparent fundamental tradeoff on these two tasks.

### Test-time intervention

Interventions replace predicted concept values `ĉ_j` with ground-truth `c_j` and propagate through `f`.

- OAI: a held-out validation set fixes an intervention ordering by measuring each concept's individual improvement; concepts are then corrected in that order.
- CUB: related binary concepts are grouped (for example all wing-color variants) and intervened on as groups; binary logits are set to the 5th or 95th percentile, respecting visibility annotations.

Effect: on OAI, RMSE drops from above 0.4 to roughly 0.3 after only two concept corrections. Independent bottlenecks gain the most from intervention despite weaker pre-intervention accuracy.

### Stated caveats

- Intervention validity depends on alignment between predicted and true concepts; a model with poor concept accuracy need not benefit.
- Linear `c → y` maps handled interventions notably worse than nonlinear ones even when pre-intervention task and concept accuracies were similar.
- When `λ` is too small, joint models learn misaligned concept representations and intervention *increases* error.
- CUB's class-level concepts mask instance-level variation; occlusion and sexual dimorphism create concept violations intervention cannot fix.
- Sequential and joint models are trained on `ĉ → y` and face a distribution shift to `c → y` at intervention time.
- Conclusion drawn by the authors: task and concept accuracy alone are insufficient to predict how effective test-time intervention will be.

## Subject Classification

- Machine Learning (cs.LG)
- Machine Learning (stat.ML)

## Versions

- v1: July 9, 2020
- v2: July 19, 2020
- v3: December 29, 2020 (edited for clarity from ICML 2020)

**Access:** [PDF](https://arxiv.org/pdf/2007.04612) | [TeX Source](https://arxiv.org/src/2007.04612)
