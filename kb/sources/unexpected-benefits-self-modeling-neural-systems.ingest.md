---
description: "Auxiliary prediction of a network's own activations reduces complexity proxies, providing a bounded comparison between causal self-modeling and readable retained theories."
source: https://arxiv.org/abs/2407.10188
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: b399ab548400d1d9a1cf08a15a7497b05eaf7d79db04f9be7e889cb3727ff6b8
ingested: "2026-09-25"
type: types/ingest-report.md
domains: [self-modeling, neural-networks, regularization, learning-theory]
learning_claims: true
---

# Ingest: Unexpected Benefits of Self-Modeling in Neural Systems

## Classification

An experimental machine-learning paper testing whether predicting internal activations changes a network's complexity. The captured work is arXiv v2 from July 2024, including supplemental methods. Vickram N. Premakumar and colleagues are affiliated with AE Studio and Princeton; AE Studio funded the research. The broader account of social cognition is a proposed interpretation of the experiments.

## Summary

The authors add an auxiliary output that predicts selected hidden activations while a network learns classification. Crucially, both the prediction and its target depend on trainable weights: reducing prediction error can change the system being modeled. Across MNIST perceptrons, a modified ResNet18 on CIFAR-10, and a simple embedding-based IMDB classifier, this joint objective produces narrower classifier-output weight distributions and lower estimated local learning coefficients, called RLCT in the paper, relative to classification-only controls. The auxiliary outputs are removed before complexity measurement, leaving matched classifier structures. Stronger auxiliary weights usually strengthen the effect, but excessive weights impair small MNIST networks and invalidate their complexity estimates. These are results within supplied architectures and activation targets, without a matched comparison to other regularizers or auxiliary targets. Accuracy generally stays similar or falls slightly, with small IMDB gains. Improved cooperation and predictability by other agents remain hypotheses.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source is a bounded comparison for [Reflection buys addressability](../notes/reflection-buys-addressability.md): a numerical self-model can influence retained weights without supplying readable commitments or selective criticism of what they claim. Its complexity results concern jointly trained activation prediction within fixed architectures, so they do not establish the advantages of addressable retention. Under the [reflective-system definition](../notes/definitions/reflective-system.md), the relevant candidate boundary includes the network, captured activations, loss computation, and optimizer. That boundary contains a path from represented internal state through prediction error to changed weights; the pruned classifier alone does not retain that demonstrated path. This also makes the paper a concrete comparison for [graded reflective coverage](../notes/reflective-coverage-is-graded-across-representational-forms.md): selected activations enter the representation and weight updates change them, while architecture, target selection, and the training objective remain supplied conditions.

## Learning Claims (our opinion)

The learning mechanism is joint optimization of classification cross-entropy and mean-squared activation-prediction error. Unlike predicting a fixed external label, the auxiliary task can become easier by changing its target. This gives the source its useful causal hypothesis: pressure to model an internal state may reshape that state. The experiments support a change in complexity proxies under that compound intervention. They do not isolate target adaptation as the cause, because they do not compare it with a version that blocks gradients through the targets.

The specified training loop is not a [theory builder](../notes/definitions/theory-builder.md). It changes weights in response to numerical errors: no unit in the network says anything (condition 1), and the gradient update is not criticism of stated content (condition 3). The activation vector is a representation of internal state, but it states nothing that criticism could argue with, so it is not an [addressable theory](../notes/definitions/addressable-theory.md). This is a limit on the demonstrated mechanism, not a claim that weight-based systems cannot formulate theories. The study helps keep causal self-representation separate from semantic addressability.

Following [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the adaptable quantities here are weights within supplied architectures. The experiment varies auxiliary loss weight and some network widths, but it does not learn which internal aspects to represent or which prediction objective to use. The result supports the tested intervention under those choices; it does not establish their superiority. Lower complexity estimates also do not by themselves show increased capacity for future action, especially where classification accuracy falls.

## Extractable Value

1. **A self-model can change its own target.** Jointly trainable activation predictions and targets provide a concrete mechanism by which self-modeling could restructure a system. The observed proxy reductions support the compound treatment, while a target-gradient ablation is needed to isolate this explanation. This is more specific than a general claim that describing a system improves it. [experiment]
2. **Causal self-representation and readable retention need separate evidence.** The training path is a useful boundary case for the existing reflection notes: internal-state prediction can affect later behavior without demonstrating criticism or selective revision of retained claims. [quick-win]
3. **Complexity reduction is a context-bound result.** Three classification tasks and ten seeds per variant support lower proxy complexity within the tested architectures and objectives. They provide a reference for regularization through activation prediction, not evidence of fewer deployed parameters, faster inference, or better cooperation. [just-a-reference]

## Limitations (our opinion)

The main comparison adds an auxiliary prediction task to classification-only training. There is no matched comparison with conventional weight regularization, a generic auxiliary task, or an activation-prediction variant with fixed targets. Ordinary regularization effects are therefore a plausible simpler account, and the contribution of making one's own targets easier to predict remains unresolved. Width and auxiliary-weight sweeps do not test alternative self-representations.

Both complexity measures require care. A narrower final-layer weight distribution is not direct evidence of removable parameters. RLCT is estimated locally using stochastic gradient Langevin dynamics with qualitatively selected hyperparameters. The supplement reports low MALA acceptance rates and uncertainty about the effect of learning-rate scheduling. High auxiliary weights in small MNIST networks fail to reach suitable classification-loss critical points, undermining the associated estimates. Lower estimated complexity should not be treated as a universal improvement when task accuracy deteriorates.

The retained recipe also has unresolved inconsistencies: CIFAR training is described as 150 epochs while results and captions use 250; supplemental localization prose gives 1000 for MNIST/CIFAR while the ResNet calibration caption gives 100. The IMDB RLCT caption uses epoch 250 while accuracy uses epoch 500. Code is described as available on request; no implementation was inspected or executed for this ingest. These details constrain reproducibility without negating the reported comparisons.

The tasks are small classification settings, not language-model agents, KB maintenance, or multi-agent collaboration. No experiment measures whether another agent can better predict the trained network. The biological and clinical extrapolations receive no direct evidence from these experiments.

## Recommended Next Action

Review [Reflection buys addressability](../notes/reflection-buys-addressability.md) against this numerical self-modeling case to sharpen the boundary between causal self-representation and readable retained commitments.
