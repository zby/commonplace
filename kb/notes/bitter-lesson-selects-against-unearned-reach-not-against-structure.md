---
description: "A case-level conjecture that using an inspectable requirement-to-objective proxy beyond its assessed scope may cause a method to lose to computation-scalable search or learning on the same objective and regime"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources, synthesis]
tags: [learning-theory, constraining]
---

# Unsupported proxy scope may explain a structured method's loss under scaling

The [captured secondary summary of the bitter lesson](../sources/wikipedia-bitter-lesson.ingest.md) reports a long-run tendency for computation-scalable search or learning to outperform methods based on domain-specific understanding. The record does not identify unsupported proxy scope as the selected property or test explicit structure as a losing category.

This note instead proposes a case-level Commonplace conjecture. When a method exposes an inspectable requirement-to-objective commitment, using that proxy beyond its assessed scope may cause the method to lose to computation-scalable search or learning evaluated on the same objective and regime. A loss supports that diagnosis only when the boundary crossing and proxy mismatch, rather than explicit structure or another implementation or evaluation difference, explain the result.

## The possible failure is in the proxy link

Let `R` be a structured requirement or invariant implemented in service of a larger objective `O`. When `R` is a proxy, exact conformance to `R` does not establish that `R` serves `O`; [exact implementation and requirement warrant are different links](./exact-implementation-does-not-validate-a-requirement.md). This distinction concerns the proxy relation. It does not deny the correctness of a constitutive requirement inside its declared boundary.

Here, **unsupported scope** means using the proposed mechanism or invariant beyond the shifts, interventions, cases, or formal domain that assessed it. It does not mean merely human-designed, explicit, complex, locally exact, or later defeated. [Reach-assessment warrants only the mechanism and range it actually tests](./definitions/reach-assessment.md): proof reaches across its formalized domain, while predictive fit reaches across the tested shift class. Because [explanatory-reach requires a mechanism to constrain what should happen as its premises change](./first-principles-reasoning-selects-for-explanatory-reach-over.md), a compatible loss is not confirmation while rival explanations remain live.

The conjectured mechanism has four links:

1. A method implements `R` for `O`, but conformance to `R` does not settle the warrant for `R -> O`.
2. Bounded assessment can validate local conformance or fit while leaving behavior outside its range unconstrained.
3. A later regime outside that boundary can expose the unconstrained behavior and a failure on `O`.
4. If computation-scalable search or learning succeeds on the same `O` and in the same regime while the structured method fails because of the proxy mismatch, it wins that comparison.

Only the fourth link establishes comparative selection. A shift can expose failure without a successful comparator, and a benchmark loss can show an outcome without identifying its cause. Composing the four links gives a plausible causal path.

## IRM witnesses a bounded scope failure

In [the captured IRM result](../sources/rosenfeld-risks-of-invariant-risk-minimization.ingest.md), non-linear featurizers in a Gaussian latent-variable structural equation model permit a predictor that is near-optimal for the penalized IRM objective and near-identical to the optimal invariant predictor on the training distribution. When the test environment's mean is sufficiently far from the training means, the predictor instead behaves like the ERM solution on most test points. The construction puts its deviant behavior in a region with little training probability mass. The IRM penalty scales with the square of that rare-region mass and is exponentially small in the environmental dimension, so the training objective provides little leverage over the behavior exposed by the shifted test environment.

In Commonplace's terms, this construction is a formal witness that local objective fit can outrun warranted scope. It does not give an exact optimizer or exact training-distribution identity, a result for linear featurizers or arbitrary distributions, or a comparison in which increasing compute selects the predictor out. It therefore supports the third link in one qualified model, not the fourth.

## DomainBed supplies an outcome, not its cause

[DomainBed](../sources/in-search-of-lost-domain-generalization.ingest.md) compared nine baseline domain-generalization algorithms on seven multi-domain datasets under three model-selection criteria. Within those datasets and implementations, carefully implemented ERM achieved state-of-the-art performance. That result is compatible with a structured method losing a comparison, but the record does not attribute the outcome to unsupported scope. Dataset choice, implementation, model selection, and other benchmark-specific explanations remain live.

The record also does not establish that every compared algorithm made an explicit reach claim or that the IRM construction explains DomainBed. DomainBed therefore supplies neither the proxy and assessed boundary nor the boundary-crossing and causal-attribution evidence needed to instantiate the full mechanism.

## A supporting case must isolate the mechanism

A case supports the conjecture only if it identifies:

1. the structured requirement or invariant `R` and the larger objective `O` it proxies;
2. the evidence, intervention, shift class, or formal domain that bounds `R`'s assessed scope;
3. a new regime outside that boundary;
4. failure on `O` attributable to the proxy mismatch after checking implementation, integration, resource, dataset, and model-selection alternatives; and
5. computation-scalable search or learning that succeeds on the same `O` and in the same regime.

Missing any item leaves the result compatible with the conjecture but does not support it as the explanation. A case refutes the diagnosis if the proxy's assessed or proved boundary already covers the alleged new regime, no boundary crossing occurred, the structured method still achieved `O`, the comparator failed, or another implementation or evaluation difference explains the loss. Evidence that isolates explicitness itself, rather than proxy mismatch, as the causal disadvantage also refutes this diagnosis for that case.

## Scope and open question

The listed evidence does not isolate explicit structure as a causal disadvantage. Unsupported scope can also afflict learned or opaque commitments; this conjecture focuses on methods with inspectable `R`-for-`O` commitments because their requirements and boundaries can be examined, not because opacity earns scope. The IRM construction and DomainBed result do not complete the four-link mechanism, establish a historical or statistical tendency, or show that scale generally selects against unsupported scope.

Failure to condemn structure as a category supplies no inverse guarantee. The evidence does not show that adequately assessed structure necessarily survives scaling or that scalable learning converges on the same structure. It also remains open whether assessed-scope mismatch can be identified prospectively with enough reliability to predict comparative scaling outcomes.
