---
description: "Causal-learn grounds the observational-causal-discovery route to reach assessment, with the important limitation that discovery is assumption-relative"
source: https://arxiv.org/abs/2307.16405
captured: "2026-07-16"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 24949c68e81336636e8db27e8e67aeb210754100cb3fe6d50dca3d0de44aa8e9
ingested: "2026-07-16"
type: kb/sources/types/ingest-report.md
domains: [causal-inference, causal-discovery, reach-assessment]
---

# Ingest: Causal-learn: Causal Discovery in Python

## Classification

An arXiv/JMLR-style software paper describing an open-source Python library and surveying causal-discovery method families. The genre recorded on the snapshot is correct.
Author: Yujia Zheng, Biwei Huang, Wei Chen, Joseph Ramsey, Mingming Gong, Ruichu Cai, Shohei Shimizu, Peter Spirtes, and Kun Zhang; strong authority signal from researchers associated with modern causal-discovery tooling and the Tetrad/py-why ecosystem.

## Summary

The paper presents `causal-learn`, a Python library for causal discovery. Its relevant point for this KB is not the library API itself but the taxonomy it makes concrete: causal relations can be inferred from observational data through constraint-based, score-based, functional-causal-model, and latent-variable methods, each relying on explicit assumptions such as conditional independence, causal sufficiency or latent-confounder handling, score choices, functional form, and noise structure. It therefore grounds the claim that observational causal discovery exists, while also blocking the stronger and false claim that observations alone contain causality without assumptions.

## Claims

- **Claim (paraphrase):** Causal-learn is a Python library spanning constraint-based, score-based, functional-causal-model, and latent-variable causal-discovery methods; these methods infer structure from observational data only under algorithm-specific assumptions and often identify an equivalence class rather than a unique graph.
  - **Source extract (verbatim):** Causal discovery aims at revealing causal relations from observational data, which is a fun- damental task in science and engineering. We describe causal-learn, an open-source Python library for causal discovery. This library focuses on bringing a comprehensive collection of causal discovery methods to both practitioners and researchers.
  - **Source location:** Abstract.
  - **Source extract (verbatim):** Current strategies for causal discovery can be broadly classified into constraint-based, score-based, functional causal models-based, and methods that recover latent variables. Constraint-based and score-based methods have been employed for causal discovery since the 1990s, using conditional independence relationships in data to uncover information about the underlying causal structure. Algorithms such as Peter-Clark (PC) (Spirtes et al., 2000) and Fast Causal Inference (FCI) (Spirtes et al., 1995) are popular, with PC assuming causal sufficiency and FCI handling latent confounders.
  - **Source location:** Section 1, method-family overview.
  - **Source extract (verbatim):** PC is a classical and widely-used algorithm with consistency guarantee under independent and identically distributed (i.i.d.) sampling assuming no latent confounders, the faithfulness assumption, and the causal Markov condition, which has been extensively applied in many fields.
  - **Source location:** Section 2.1, constraint-based methods.
  - **Scope:** The library and method families documented in the 2023 software paper; the concrete assumptions quoted are for PC, while other included algorithms have different conditions.
  - **Confidence:** High for the library coverage and the paper's stated assumptions and output boundaries.
  - **Limitation:** Providing implementations does not validate the causal truth of a discovered graph. Observational discovery remains assumption-relative, and several methods return only a Markov equivalence class or possible latent-confounder structure.

## Connections Found

This source is a technical basis for [reach assessment](../notes/definitions/reach-assessment.md) and [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). It supplies the concrete "causal theories from observations under assumptions" part of the causal route. It also compares with [DoWhy's assumptions paper](./dowhy-expressing-and-validating-causal-assumptions.ingest.md), which covers assumption declaration and validation after or alongside graph discovery, and with [invariant prediction](./causal-inference-using-invariant-prediction.ingest.md), which gives one specific invariance-based discovery strategy.

## Extractable Value

1. **Observational causal discovery is real but assumption-loaded** -- Useful correction to the reach-assessment note: the exception to "empirical testing alone is not reach assessment" is not raw observation, but observation plus causal-discovery assumptions and criteria. [quick-win]
2. **Method family vocabulary** -- Constraint-based, score-based, functional-causal-model, and latent-variable discovery name the main formal routes a future system might expose as explicit causal-theory learners. [just-a-reference]
3. **Concrete system example** -- A causal-learning system can be built out of existing libraries, not only hypothesized. That matters for the user's question about examples of systems that can infer causal theories. [quick-win]
4. **Boundary against overclaiming** -- Many methods output equivalence classes or partial causal information; this prevents the KB from treating "causal discovery" as full graph recovery by default. [quick-win]

## Limitations (our opinion)

As a scientific/software paper, it is strongest as method and implementation coverage, not as evidence that any particular causal discovery result is correct in a given domain. The paper surveys algorithm families and exposes APIs; it does not remove the need to choose assumptions, test sensitivity, and interpret outputs conservatively. For reach assessment, its value is grounding the existence of formal causal-discovery machinery, not proving that such machinery can validate arbitrary retained lessons.

## Recommended Next Action

Keep this as the primary source citation for the observational-causal-discovery clause in [Formal symbolic systems assess reach only through causal and proof obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md); do not promote a separate note unless the KB later needs a taxonomy of causal-discovery algorithms.
