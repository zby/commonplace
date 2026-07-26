---
source: https://arxiv.org/abs/2010.05761
description: First formal analysis of the IRM objective — shows it can fail catastrophically unless test data are sufficiently similar to training data, and offers no gain over ERM in non-linear regimes
captured: 2026-07-26
capture: web-fetch
genre: scientific-paper
type: kb/sources/types/snapshot.md
---

# The Risks of Invariant Risk Minimization

Author: Elan Rosenfeld, Pradeep Ravikumar, Andrej Risteski
Source: https://arxiv.org/abs/2010.05761
Date: v1 October 12, 2020; v2 (ICLR 2021 camera-ready) March 27, 2021

Subject categories: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Machine Learning (stat.ML)

## Abstract

The authors provide the first formal analysis of classification using the invariant risk minimization (IRM) objective and related methods. In linear settings, they establish when optimal solutions succeed or fail to identify the invariant predictor. They demonstrate that IRM can fail catastrophically unless the test data are sufficiently similar to the training distribution — the very problem it aimed to address. They conclude these methods offer no improvement over standard empirical risk minimization in non-linear regimes.

## Body

Content below is extracted from the ar5iv HTML rendering of the paper
(<https://ar5iv.labs.arxiv.org/html/2010.05761>) on the same capture date.

### Setup

A structural equation model with Gaussian latent variables:

- label `y ∈ {±1}` drawn with probability `η`
- invariant (causal) features `z_c ~ N(y·μ_c, σ_c² I)`
- environmental (spurious) features `z_e ~ N(y·μ_e, σ_e² I)`, whose parameters vary by environment
- observation `x = f(z_c, z_e)` for injective `f`

`μ_c`, `σ_c²`, and `f` are held constant across environments; only `μ_e` and `σ_e` vary.
`E` denotes the number of training environments and `d_e` the dimension of the
environmental feature space.

### Linear regime

The paper establishes a threshold in the number of training environments. When
`E > d_e`, any IRM-feasible linear featurizer paired with an invariant classifier
must place zero weight on the environmental features, so the invariant predictor is
recovered. When `E ≤ d_e`, there exists a feasible linear predictor that uses only
environmental features and attains lower risk than the optimal invariant predictor —
so the IRM objective does not prefer the invariant solution. Generalization in the
`E ≤ d_e` case requires an additional assumption that the ERM-optimal classifier over
the non-invariant features is reasonably aligned with its optimum across all training
environments; where the environmental correlation with the label reverses at test
time, the learned predictor reaches near-zero accuracy.

### Non-linear regime

For non-linear featurizers the authors construct a predictor that is near-optimal
under the penalized IRM objective and near-identical to the optimal invariant
predictor on the training distribution, yet reduces to the ERM solution on most test
points once the test environment's mean is sufficiently far from the training means.
The construction partitions environmental feature space into a region `B` containing
most training mass, where the predictor uses invariant features, and its complement
`Bᶜ`, rare under training, where it uses the ERM solution. The IRM penalty incurred
scales with the squared probability mass of the rare region and is exponentially small
in `d_e`, so the objective sees the construction as an attractive solution.

The authors state the consequence directly: IRM fails unless the test data are
sufficiently similar to the training distribution — precisely the problem it was
intended to solve.

### Experiments and conclusion

Synthetic experiments sample from the paper's model and fit a predictor with the IRM
objective, confirming the theoretical predictions (Appendix C.2). The authors conclude
that existing approaches to invariant causal prediction for high-dimensional latent
variable models do not cleanly achieve their stated objective, that IRM offers no real
advantage over ERM unless the number of training environments exceeds the
environmental feature dimension, and that invariant prediction warrants more formal
treatment in future work.
