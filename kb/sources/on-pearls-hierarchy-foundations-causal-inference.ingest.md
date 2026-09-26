---
description: "Pearl's causal hierarchy explains why observationally equivalent models can disagree about interventions, bounding how retained causal rivals can guide evidence search."
source: https://causalai.net/r60.pdf
captured: "2026-09-26"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d4e114a31a636b08527907d4612ab6b29e0fc5d3a7adf321fe192d8a295db142
ingested: "2026-09-26"
occasion: "Explain how retaining competing causal theories can guide the search for evidence that distinguishes them when current observations do not."
type: types/ingest-report.md
domains: [causal-inference, causal-models, experiment-design]
learning_claims: true
---

# Ingest: On Pearl’s Hierarchy and the Foundations of Causal Inference

## Classification

A mathematical research chapter, retained as Technical Report R-60, revised March 2021. It develops definitions, theorem statements, proof sketches, and constructed examples rather than reporting an empirical comparison. Authors Elias Bareinboim and Juan D. Correa are affiliated with Columbia University; Duligur Ibeling and Thomas Icard with Stanford University. Their contribution concerns the formal foundations of causal inference.

## Summary

The chapter derives Pearl's three causal layers—observation, intervention, and counterfactuals—from structural causal models, which specify mechanisms and a distribution over background conditions. Its Causal Hierarchy Theorem establishes that collapse of these layers is measure zero under the stated encoding of finite, recursive models: complete knowledge at a lower layer generally leaves higher-layer questions unresolved. Constructed pairs of models demonstrate agreement on observations with disagreement on interventions, and agreement on all interventions with disagreement on counterfactuals. The graphical treatment then explains how partial causal knowledge can support particular cross-layer inferences. It develops causal Bayesian networks with and without latent confounding and derives do-calculus from their interventional constraints. The result is an assumption-relative account of what causal questions available evidence can answer, rather than a claim that observational data are useless for causal inference.

## Quotes

No source quotes have been retained yet.

## Connections Found

The source provides a formal basis for the assumption boundary in [Causal and proof obligations are two formal routes to assessing explanatory-reach](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md). For the occasion, its particular value is explaining why retaining observationally equivalent causal rivals can matter: their intervention predictions may disagree even when further samples from the same observational distribution cannot distinguish them. Using those disagreements to select evidence is our KB application of the examples, not an evaluated retention method from the paper.

It also supplies a comparison for [A retained-theory intervention isolates one surface, not the whole program theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md). The paper's intervention replaces designated mechanisms while preserving the others and the background distribution. Whether a KB manipulation realizes that contrast remains a separate design question. Effect identification then concerns agreement among models compatible with the assumptions and evidence, not recovery of a unique complete theory.

## Learning Claims (our opinion)

The source studies what causal information can be inferred from available data plus assumptions. It does not present a learner that autonomously acquires and revises its causal assumptions. Its principal mechanism is to constrain the class of compatible structural models, then establish whether those models agree on a target quantity. This sharpens our distinction between using a theory and learning one: deriving an effect from a supplied graph consumes causal knowledge but does not validate or revise that graph.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), the evidence differs by condition. **Localized content** is explicit in equations, causal graphs, and their assumptions. **Consumption** is demonstrated mathematically: those assumptions determine which inferences are licensed. **Content-directed criticism** appears in the authors' countermodels refuting claims that lower-layer agreement suffices for higher-layer agreement; this is methodological argument, not evidence of a deployed critic. **Iteration** is advocated in the introductory account of scientific inquiry, but the chapter does not document an operational revision loop or retained testing history shaping successive learner rounds. Persistence across runs or problems is likewise not evaluated. The paper therefore supplies tools a theory builder could use, without establishing a complete implementation or improved future action from retaining rival theories.

The connection to [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) is specifically about information limits. Even exact recovery of an observational distribution can leave intervention predictions underdetermined. Increasing estimator capacity alone does not supply the missing causal restrictions or experimental evidence. This is distinct from failing to represent a candidate model: the rival models may both be expressible. The chapter fixes its modeled variables and recursive structural semantics; it does not test whether those choices adequately represent a particular KB system.

## Extractable Value

1. **Turn retained disagreement into an evidence question.** Example 7 constructs models with the same observational distribution but different recovery probabilities under treatment: one predicts one-half, another three-quarters. For the KB, retaining both models could preserve a concrete reason to seek intervention evidence rather than more observational fit. Record the shared evidence, the disputed mechanism, and a feasible intervention on which predictions differ. That workflow is a target-side proposal supported by the formal example, not a measured benefit of retention. [quick-win]

2. **Check whether the proposed evidence could separate the rivals.** The same example constructs another pair agreeing on observational and interventional distributions while giving opposite answers to a counterfactual attribution question. Experiments over those modeled variables cannot distinguish that pair by their population distributions alone. This bounds the occasion: a retained disagreement can expose a missing assumption or a need to change what is measured without guaranteeing an available decisive test. [quick-win]

3. **Ask for agreement on the decision-relevant effect, not a unique theory.** Definition 17 makes effect identification relative to a causal graph and a positive observational distribution: every compatible model must give the same target effect. Multiple mechanisms may remain unresolved even when an action's effect is identified. Conversely, a supplied graph with latent confounding may still leave the effect unresolved, as Example 12 demonstrates. This gives the KB a precise way to distinguish unresolved theory from unresolved action consequences. [quick-win]

## Limitations (our opinion)

The theorem concerns finite endogenous variables with finite domains and recursive structural models. Its measure-zero claim uses an encoding of equivalence classes of models; it is not an empirical estimate of how frequently deployed systems require new experiments. It concerns collapse of whole layers, so it must not be read as saying that every individual higher-layer question is unanswerable from lower-layer data plus justified assumptions.

The constructed treatment examples are demonstrations of logical possibility. They are not clinical studies or comparisons of real AI and human physicians. The chapter neither measures the benefit of retaining rival theories nor supplies a procedure for ranking experiments by cost, precision, or expected information. A disagreement must concern distinguishable distributions under a feasible intervention before it can guide such an experiment. Finite-sample uncertainty and the credibility of the causal assumptions remain additional problems.

Causal identification does not justify the supplied variables, graph, or intervention semantics. As the [formal-assessment note](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) emphasizes, an internally valid inference can still misrepresent the intended claim. Nor does a result for one specified mechanism replacement test alternative system decompositions.

The complete captured chapter refers several proofs and constructions to appendices in a separately cited version. Those appendices are not present here. Text extraction also loses graphical structure and some mathematical typography, so exact diagram-dependent derivations require consulting the original PDF.

## Recommended Next Action

Extend [the causal route in the formal-assessment note](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md#the-causal-route) with one worked pair of observationally equivalent causal rivals, showing the intervention that separates their predictions and the boundary where interventionally equivalent rivals require additional assumptions or evidence beyond the existing intervention distributions.

---

Abstracted into:

- [Competing causal theories can guide distinguishing experiments](../notes/competing-causal-theories-can-guide-distinguishing-experiments.md) — applies intervention semantics and causal non-identifiability to retaining rivals for KB evidence selection; the noisy binary example and design consequence are the note's construction
