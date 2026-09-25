---
description: "JEPA-Anything improves matched predictive tasks with orthogonal latent factors; its factor interventions qualify how Commonplace distinguishes accessible model channels from addressable theories."
source: https://arxiv.org/abs/2609.20800
captured: "2026-09-24"
ingested: "2026-09-25"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: dec3b39bca88a55db8c3b593f3222397362ffbf2af13d72c085922c4ed0a7a31
type: kb/sources/types/ingest-report.md
domains: [world-models, representation-learning, scientific-discovery]
learning_claims: true
---

# Ingest: JEPA-Anything: Learning Predictive Models across Different Worlds

## Classification

A research preprint presenting an architecture, mathematical properties, matched predictive evaluations, factor interventions, and scientific applications. Taoyong Cui and colleagues list affiliations including PhAI Labs and the Chinese University of Hong Kong. These are author-reported experiments; the retained paper does not establish independent replication or peer review.

## Summary

JEPA-Anything introduces orthogonal predictive factorization (OPF): separate predictors learn complementary latent target subspaces, whose predictions are recombined into a complete state. Domain-specific adapters, encoders, context–target relations, and base losses remain; the common element is the training principle. Against monolithic JEPA with those choices held fixed, the OPF bundle improves reported metrics across ten matched dynamics tasks and reduces single-intervention prediction error on Interventional Pong by 34.83%. Separate capacity-matched planning tests favor OPF on Walker2d and HalfCheetah but favor standard JEPA on Hopper. The paper also reports visual, cellular, clinical, and molecular prediction results. Factor masking shows that individual channels contribute to locomotion prediction and planning. A biological intervention receives experimental support, and a simulated orbital analysis recovers a known scaling law. For Commonplace, the strongest contribution is evidence that learned predictors can expose useful intervention points without establishing separately revisable explanatory commitments.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper supplies bounded evidence for [world-model assessment through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md). Held-out intervention combinations, repeated rollout, and real-environment planner returns test reuse beyond fitting familiar observations. The gains compare the OPF bundle with monolithic prediction within fixed domain interfaces; they do not establish that those interfaces are preferable to alternatives. The same source qualifies the note's categorical claim that nothing can be localized in a learned predictor: separate factor probes and masking expose functionally used channels. They do not identify a faulty explanatory commitment or demonstrate its selective repair.

The orbital example compares with [known-target discovery benchmarks](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) on the narrower issue of an externally supplied success criterion. Recovering the Keplerian exponent from simulated trajectories tests correspondence to an established law. It does not demonstrate autonomous selection and validation of an unknown law, and it is not the LLM reinvention protocol discussed by the note.

## Learning Claims (our opinion)

OPF learns encoder weights, target-space projectors, and factor predictors through gradient optimization. Its target encoder follows an exponential moving average of the online encoder. Alongside the inherited domain loss, factor prediction, orthogonality, factor activity, and online-encoder variance guide training. Factor identities emerge from prediction rather than being assigned causal or semantic labels. Ordinary representation evaluation discards the factor machinery and reads the encoder; rollout, planning, and factor analysis retain it. These consumption paths matter: better terminal readout alone does not demonstrate useful recursive dynamics.

The learned projectors can change which latent directions each branch represents. The decomposition is therefore partly learned, rather than a fixed semantic partition. However, observation adapters, context–target construction, encoder families, factor budgets, and domain readouts remain supplied by the experimenters. As in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), improvement within that space does not test alternatives outside it. The matched comparisons support the compound OPF treatment, not a separate causal attribution to every regularizer.

In Commonplace's terms, the reported training establishes parametric learning but does not establish [conjectural learning](../notes/definitions/conjectural-learning.md) by the predictive component. The paper does not show formulated theories guiding its choices and criticism of their content changing its later capacity. At the broader researcher–model–experiment boundary, the biological case reports hypothesis nomination and external testing, but does not document the subsequent revision or changed investigation policy sufficiently to settle that classification.

The factor interventions sharpen the comparison with [addressable theory](../notes/definitions/addressable-theory.md). A factor can be separately read and masked while remaining semantically underdetermined. That is meaningful access to a component of a distributed representation; it falls short of inspecting and revising what an explanatory part says. The evidence cautions against equating all latent models with complete lack of component access, while leaving claim-level diagnosis and repair unestablished. The paper explicitly places uncertainty-aware experiment choice, factor revision, and an integrated scientific investigation loop in future work.

## Extractable Value

1. **Separate access to latent channels from access to explanatory commitments.** In the four-factor locomotion models, masking each factor increases 20-step rollout error across three environments. HalfCheetah return declines in all five seeds for two factors and four of five seeds for the other two. This supports a more precise account of localization than an all-or-nothing contrast between predictors and theories; it does not show selective repair. [quick-win]
2. **Distinguish geometry, predictive usefulness, and downstream decisions.** Complete orthogonal coordinates permit stable state synthesis, but prediction error remains a separate quantity. The OPF bundle improves matched prediction within supplied domain interfaces, while the separate planning comparison includes a Hopper loss. These are distinct evidential steps when reusing a learned model as an evaluator. [just-a-reference]
3. **Retain the limits of scientific-discovery examples.** The orbital diagnostic recovers a known law; the biological result reports external support for one nominated intervention. Neither demonstrates the complete uncertainty, experiment-selection, revision, and transfer loop proposed in the paper's future work. [just-a-reference]

## Limitations (our opinion)

The exact decomposition theorem assumes a complete orthogonal basis. Its approximate counterpart bounds error amplification only under a stated orthogonality-residual condition. The geometry audit uses strict decomposition, exact factor coordinates, and transpose synthesis; predictive models use soft regularization and pseudoinverse synthesis. Near-perfect reconstruction in that audit is not near-perfect forecasting, and orthogonality does not establish causal disentanglement.

The strongest matched comparisons hold data, encoders, budgets, base losses, and readouts fixed while replacing monolithic prediction with the OPF bundle. Capacity matching addresses model size in specific experiments, but does not isolate all constituent mechanisms. Improved optimization or regularization remains a sufficient narrower explanation of gains than discovery of independently meaningful causal factors. The separate domain implementations do not demonstrate a jointly trained, aligned cross-domain model. Molecular results cover four systems and 100-step rollouts; they do not establish arbitrary-horizon stability.

The biological section names IL-18 plus NT5E/CD73 blockade and reports cell, three organoid, three tumor-fragment, and mouse evidence. It does not provide a sufficiently detailed nomination procedure, experimental methods, or complete uncertainty account to assess the discovery attribution fully. The orbital diagnostic is one analyzed simulated run. Clinical prediction uses a fixed patient-level UK Biobank split and more than 1,000 event risks, without establishing deployment performance. The full-paper text capture lacks some figure-only numerical values; this report relies on stated results and extracted tables. No implementation was inspected or executed, and no training or experimental outcome was reproduced.

## Recommended Next Action

Review the localization section of [World models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) against the factor-probe and masking evidence, distinguishing accessible predictive channels from diagnosis and selective revision of explanatory commitments.
