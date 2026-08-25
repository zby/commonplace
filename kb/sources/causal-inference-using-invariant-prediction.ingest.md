---
description: "Invariant prediction grounds reach assessment by treating cross-environment invariance as evidence for causal predictors rather than fitted correlations"
source: https://arxiv.org/abs/1501.01332
captured: "2026-07-16"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: b59816fe93710bfdaedc94306ff6a127ed1c6c4961b100bc735371bac9343c27
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, invariance, reach-assessment]
---

# Ingest: Causal inference using invariant prediction

## Classification

A methodological causal-inference paper with assumptions, procedure, confidence statements, robustness discussion, and empirical studies. The genre recorded on the snapshot is correct.
Author: Jonas Peters, Peter Buehlmann, and Nicolai Meinshausen; high authority signal in statistical causal inference and invariant prediction.

## Summary

The paper asks what distinguishes causal prediction from non-causal prediction under interventions or environment changes. Its answer is invariance: the conditional distribution of a target given its direct causes should remain stable across suitable environments, while non-causal predictors can fail under intervention. The method collects models whose predictions are invariant across experimental settings and gives confidence intervals for causal relationships under stated assumptions. For this KB, it is the cleanest source for turning "reach" into a formal causal obligation: a candidate mechanism must survive the relevant intervention or environment-shift test.

## Quotes

- **Source extract (verbatim):** Here, we propose to exploit this invariance of a prediction under a causal model for causal inference: given different experimental settings (for example various interventions) we collect all models that do show invariance in their predictive accuracy across settings and interventions. The causal model will be a member of this set of models with high probability. This approach yields valid confidence intervals for the causal relationships in quite general scenarios. We examine the example of structural equation models in more detail and provide sufficient assumptions under which the set of causal predictors becomes identifiable.
  - **Source location:** Abstract.
- **Source extract (verbatim):** Another main advantage of our methodology is that we do not need to know how the experimental conditions arise or which type of interventions they induce. We only assume that the intervention does not change the conditional distribution of the target given the causal predictors (no intervention on the target or a hidden confounder): it is simply a device exploiting the grouping of data into blocks, where every block corresponds to an experimental condition e ∈ E.
  - **Source location:** Section 1.2, “New contribution.”
- **Source extract (verbatim):** Generic method for invariant prediction 1) For each set S ⊆ {1, . . . , p}, test whether H0,S (E) holds at level α (we will discuss later concrete examples).
  - **Source location:** Section 3, first step of the generic method; the following displayed equation defines the intersection estimator.
- **Source extract (verbatim):** The confidence sets thus have the correct (conservative) coverage. The estimator of the causal predictors will, with probability at least 1 − α, not erroneously include non-causal predictors. Note that the statement is true for any set of experimental or intervention settings. In the worst case, the set Ŝ(E) might be empty but the error control is valid nonetheless.
  - **Source location:** Section 3, explanation following Theorem 1.

## Connections Found

This source directly supports [reach assessment](../notes/definitions/reach-assessment.md) and [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md): it gives a specific formal signal for assessing whether a proposed causal commitment reaches beyond the distribution that fitted it. It also grounds the structured-shift premise in [Theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), because it makes "stable mechanism across environments" statistically explicit.

## Extractable Value

1. **Invariance is a reach test** -- A mechanism's predicted relation should persist across environments or interventions. That maps cleanly onto reach assessment as a check on generality beyond fitted cases. [quick-win]
2. **Reach can be confidence-bounded** -- The paper's confidence intervals show that formal reach assessment need not be all-or-nothing proof; statistical causal methods can attach error control to causal claims. [experiment]
3. **Structured shifts need causal structure** -- The source sharpens the existing structured-shifts note by distinguishing shifts where direct-cause mechanisms remain stable from arbitrary off-distribution shifts. [quick-win]
4. **Non-causal predictors can be brittle exactly where reach matters** -- The paper gives the local failure mode: a predictor may work observationally and fail when variables are intervened on. [just-a-reference]

## Limitations (our opinion)

The method is assumption-dependent and environment-dependent. It is strongest when multiple environments or interventions are available and when the invariance assumptions match the data-generating process. It does not make arbitrary observational data sufficient for causal inference, and it does not solve the natural-language route to reach assessment. The KB should use it as a formal exemplar, not as a universal reach oracle.

## Recommended Next Action

Use this source as the strongest grounding for the invariance example in [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md), and consider a later narrow update to [Theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) to cite the local ingest instead of only the external arXiv link.
