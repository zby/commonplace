---
description: "A falsification-first reporting proposal distinguishes statistical reanalysis from discriminating experiments, with a two-agent illustration that bundles goals and analytic specifications."
source: https://arxiv.org/abs/2604.22080
captured: "2026-09-19"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 1ff9c9766d80f54243e65d953d3b40e4c0f368891d35a4735eb52ca94cb6a00f
ingested: "2026-09-19"
occasion: "Assess 2026 computational implementations and evaluations of conjecture, criticism, revision, and persistence for a learning paradigm grounded directly in Popper; distinguish epistemic commitments, implementation choices, and demonstrated effects."
type: ingest-report
learning_claims: true
domains: [agentic-science, falsification, learning-theory, evaluation]
---

# Ingest: Sound Agentic Science Requires Adversarial Experiments

## Classification

An ICLR 2026 Agents in the Wild workshop position paper with a small empirical illustration and a proposed reporting standard. Authors Dionizije Fa (Entropic) and Marko Culjak (TakeLab, University of Zagreb) argue from scientific methodology and demonstrate agent-generated analyses; the paper does not evaluate its proposed standard.

## Summary

The authors argue that agents can generate plausible observational conclusions faster than scientists can experimentally challenge them. Their proposed falsification-first standard pairs each claim with targeted attempts to break it, a runnable analysis package, and designs for discriminating experiments. A two-agent illustration uses GPT-5.2-Codex through Codex CLI on NHANES 2017–2018 vitamin-D and depression data. One analysis reports a small significant negative association; the other reports no evidence of association. The prompts change both desired conclusions and required analytic specifications, including survey weighting, so the illustration shows divergent outputs under bundled instructions rather than isolating goal steering. The paper explicitly invokes Popper and distinguishes adversarial reanalysis of static databases from interventions capable of testing causal explanations. It supplies an epistemic and reporting proposal, not an implemented persistent learning loop or evidence that the proposal improves scientific outcomes.

## Quotes

No source quotes have been retained yet.

## Connections Found

For assessing a Popper-grounded learning paradigm, this source is a methodological counterpoint: arranging criticism is insufficient unless the tests can discriminate the claim being made. It compares with [the obligations of a claim without external assessment](../notes/a-claim-without-external-assessment-carries-three-obligations.md), particularly the distinction between an agent's internal assessment and an independently assessed outcome. Physical experiment access does not by itself supply that note's external objective or declared assessment boundary. The demonstration also illustrates [why an experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): changed goals, weighting, and other analytic requirements form a bundle. Its conflicting summaries cannot establish the effect of adversarial review, which was not tested.

## Learning Claims (our opinion)

The proposed mechanism redirects agents from supporting a desired conclusion toward generating alternative explanations, running checks for confounding or analytic artifacts, and designing interventions that could discriminate explanations. Criticism is made part of the research output. Revision and repeated experimental inquiry are anticipated, but the paper specifies no durable theory store, repair operators, retention policy, or subsequent consumption of revised theories.

Against the [theory-builder definition](../notes/definitions/theory-builder.md), this is a proposal for condition 3: it makes attempted refutation of a stated claim part of the research output. It specifies no system that meets the other conditions. Consumption of revised claims and iteration from criticism to a next conjecture (conditions 2 and 4) are left unspecified by the proposal, so they are unestablished rather than failed. The illustration fails condition 3, which decides the negative verdict for what was run: the two instructed analyses seek different conclusions and do not criticize each other; their divergence is not evidence of one system correcting a theory. It also fails condition 4: both analyses are one-shot, so no criticism shapes a next analysis, and no persistence grade is reached. No model-weight update or improvement is evaluated, so no learning claim arises.

The available update space matters. Agents can change analyses over supplied observational data, but those operations do not generate new intervention outcomes. This provides a concrete methodological instance of the concern in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): increased search within accessible analyses cannot automatically repair a missing evidence channel. This is our mapping of the argument, not an empirical comparison of static-data and laboratory-equipped learners. The useful addition is to require a stated relationship between a conjecture and what could contradict it; the source leaves the implementation and persistence of the learning loop open.

## Extractable Value

1. **Separate epistemic commitment from implemented learning.** The paper explicitly adopts attempted falsification as a scientific norm, but its implemented example produces two analyses and does not test correction, retention, or reuse. It belongs in a comparison as a methodological proposal with an illustration, not as demonstrated Popperian learning. [quick-win]
2. **Match the criticism channel to the claim.** Statistical robustness checks can challenge an observational result without settling its causal explanation. The proposed requirement to include targeted failure attempts and discriminating experiment designs supplies a concrete review question for theory-building systems, although the benefit of the reporting requirement is untested. [experiment]
3. **Retain the actual comparison.** Divergent NHANES summaries arise under prompts that jointly prescribe different goals and analytic choices. This is a useful teaching case for preventing a bundled result from being cited as evidence that goal wording alone induces selective analysis or that adversarial criticism improves conclusions. [quick-win]

## Limitations (our opinion)

The demonstration uses one dataset and two directed analyses, without repeated runs, matched neutral prompts, a human comparison, or a trial of the proposed reporting standard. Agent A is required to use survey weights and broader adjustment; Agent B is required to omit survey design and use minimal adjustment, with altered sample restrictions permitted. The prescribed differences offer a simpler explanation for the outputs than an independently demonstrated agent tendency to invent support. The Appendix B-agent goal also says vitamin D is not associated with *higher* depression burden, which does not cleanly oppose a negative association, although the main text describes a no-correlation goal.

A significant result in one specification and a nonsignificant result in another do not establish statistically incompatible effect estimates. Converted to the same exposure scale, the reported confidence intervals overlap. The paper therefore demonstrates divergent verbal conclusions, not a formal test that the estimated associations conflict. It does not establish a biomedical conclusion about vitamin D.

The paper's broad contrast between software verification and empirical science assumes meaningful software specifications and tests; their adequacy is itself a condition. Its stronger suggestion that experiments alone shrink scientific hypothesis space is not established by this illustration. Observational evidence can constrain claims under assumptions, while interventions also require interpretation and valid measurement. The useful boundary is what a test can discriminate, rather than the physical character of the test alone.

The discussion of POPPER and autonomous laboratories reports other work; neither implementation was inspected or reproduced for this ingest. No code was executed. The paper's near-zero-cost premise and expectation that end-to-end scientific automation will close the verification gap remain arguments, not measured findings. It provides no evaluation of long-term theory persistence or learning benefits.

## Recommended Next Action

Use this source as a methodological counterpoint in the planned comparison of 2026 Popper-grounded learning systems, classifying its falsification-first standard as a proposal and its two-agent example as a bundled analysis demonstration, with revision and persistence marked untested.
