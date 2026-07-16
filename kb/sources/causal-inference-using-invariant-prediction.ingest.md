---
description: "Invariant prediction grounds reach assessment by treating cross-environment invariance as evidence for causal predictors rather than fitted correlations"
source_snapshot: "kb/sources/causal-inference-using-invariant-prediction.md"
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, invariance, reach-assessment]
---

# Ingest: Causal inference using invariant prediction

Source: [causal-inference-using-invariant-prediction.md](./causal-inference-using-invariant-prediction.md)
Captured: 2026-07-16
From: <https://arxiv.org/abs/1501.01332>

## Classification

Genre: scientific-paper -- a methodological causal-inference paper with assumptions, procedure, confidence statements, robustness discussion, and empirical studies. The genre recorded on the snapshot is correct.
Domains: causal-inference, invariance, reach-assessment
Author: Jonas Peters, Peter Buehlmann, and Nicolai Meinshausen; high authority signal in statistical causal inference and invariant prediction.

## Summary

The paper asks what distinguishes causal prediction from non-causal prediction under interventions or environment changes. Its answer is invariance: the conditional distribution of a target given its direct causes should remain stable across suitable environments, while non-causal predictors can fail under intervention. The method collects models whose predictions are invariant across experimental settings and gives confidence intervals for causal relationships under stated assumptions. For this KB, it is the cleanest source for turning "reach" into a formal causal obligation: a candidate mechanism must survive the relevant intervention or environment-shift test.

## Connections Found

This source directly supports [reach assessment](../notes/definitions/reach-assessment.md) and [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md): it gives a specific formal signal for assessing whether a proposed causal commitment reaches beyond the distribution that fitted it. It also grounds the structured-shift premise in [Reflection may improve sample efficiency under structured shifts](../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md), because it makes "stable mechanism across environments" statistically explicit.

## Extractable Value

1. **Invariance is a reach test** -- A mechanism's predicted relation should persist across environments or interventions. That maps cleanly onto reach assessment as a check on generality beyond fitted cases. [quick-win]
2. **Reach can be confidence-bounded** -- The paper's confidence intervals show that formal reach assessment need not be all-or-nothing proof; statistical causal methods can attach error control to causal claims. [experiment]
3. **Structured shifts need causal structure** -- The source sharpens the existing structured-shifts note by distinguishing shifts where direct-cause mechanisms remain stable from arbitrary off-distribution shifts. [quick-win]
4. **Non-causal predictors can be brittle exactly where reach matters** -- The paper gives the local failure mode: a predictor may work observationally and fail when variables are intervened on. [just-a-reference]

## Limitations (our opinion)

The method is assumption-dependent and environment-dependent. It is strongest when multiple environments or interventions are available and when the invariance assumptions match the data-generating process. It does not make arbitrary observational data sufficient for causal inference, and it does not solve the prose version of reach assessment. The KB should use it as a formal exemplar, not as a universal reach oracle.

## Recommended Next Action

Use this source as the strongest grounding for the invariance example in [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md), and consider a later narrow update to [Reflection may improve sample efficiency under structured shifts](../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md) to cite the local ingest instead of only the external arXiv link.
