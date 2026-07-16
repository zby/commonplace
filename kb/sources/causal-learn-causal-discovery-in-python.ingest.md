---
description: "Causal-learn grounds the observational-causal-discovery route to reach assessment, with the important limitation that discovery is assumption-relative"
source_snapshot: "kb/sources/causal-learn-causal-discovery-in-python.md"
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, causal-discovery, reach-assessment]
---

# Ingest: Causal-learn: Causal Discovery in Python

Source: [causal-learn-causal-discovery-in-python.md](./causal-learn-causal-discovery-in-python.md)
Captured: 2026-07-16
From: <https://arxiv.org/abs/2307.16405>

## Classification

Genre: scientific-paper -- an arXiv/JMLR-style software paper describing an open-source Python library and surveying causal-discovery method families. The genre recorded on the snapshot is correct.
Domains: causal-inference, causal-discovery, reach-assessment
Author: Yujia Zheng, Biwei Huang, Wei Chen, Joseph Ramsey, Mingming Gong, Ruichu Cai, Shohei Shimizu, Peter Spirtes, and Kun Zhang; strong authority signal from researchers associated with modern causal-discovery tooling and the Tetrad/py-why ecosystem.

## Summary

The paper presents `causal-learn`, a Python library for causal discovery. Its relevant point for this KB is not the library API itself but the taxonomy it makes concrete: causal relations can be inferred from observational data through constraint-based, score-based, functional-causal-model, and latent-variable methods, each relying on explicit assumptions such as conditional independence, causal sufficiency or latent-confounder handling, score choices, functional form, and noise structure. It therefore grounds the claim that observational causal discovery exists, while also blocking the stronger and false claim that observations alone contain causality without assumptions.

## Connections Found

This source is a technical basis for [reach assessment](../notes/definitions/reach-assessment.md) and [Formal systems can assess reach through causal and proof obligations](../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md). It supplies the concrete "causal theories from observations under assumptions" part of the causal route. It also compares with [DoWhy's assumptions paper](./dowhy-expressing-and-validating-causal-assumptions.ingest.md), which covers assumption declaration and validation after or alongside graph discovery, and with [invariant prediction](./causal-inference-using-invariant-prediction.ingest.md), which gives one specific invariance-based discovery strategy.

## Extractable Value

1. **Observational causal discovery is real but assumption-loaded** -- Useful correction to the reach-assessment note: the exception to "empirical testing alone is not reach assessment" is not raw observation, but observation plus causal-discovery assumptions and criteria. [quick-win]
2. **Method family vocabulary** -- Constraint-based, score-based, functional-causal-model, and latent-variable discovery name the main formal routes a future system might expose as explicit causal-theory learners. [just-a-reference]
3. **Concrete system example** -- A causal-learning system can be built out of existing libraries, not only hypothesized. That matters for the user's question about examples of systems that can infer causal theories. [quick-win]
4. **Boundary against overclaiming** -- Many methods output equivalence classes or partial causal information; this prevents the KB from treating "causal discovery" as full graph recovery by default. [quick-win]

## Limitations (our opinion)

As a scientific/software paper, it is strongest as method and implementation coverage, not as evidence that any particular causal discovery result is correct in a given domain. The paper surveys algorithm families and exposes APIs; it does not remove the need to choose assumptions, test sensitivity, and interpret outputs conservatively. For reach assessment, its value is grounding the existence of formal causal-discovery machinery, not proving that such machinery can validate arbitrary retained lessons.

## Recommended Next Action

Keep this as the primary source citation for the observational-causal-discovery clause in [Formal systems can assess reach through causal and proof obligations](../notes/formal-systems-can-assess-reach-through-causal-and-proof-obligations.md); do not promote a separate note unless the KB later needs a taxonomy of causal-discovery algorithms.
