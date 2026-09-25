---
description: "Controlled advice experiments separate answer-ownership bias from excessive confidence updating, qualifying confidence-based review and suggesting a test of reviewer context."
source: https://www.nature.com/articles/s42256-026-01217-9.pdf
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
doi: "10.1038/s42256-026-01217-9"
genre: scientific-paper
snapshot_sha256: 9da909aa43c57d1d76d8557e2ccc04790a206c241edd9c17e1fd4e2047f5fb82
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [llm-reliability, confidence-calibration, context-engineering]
learning_claims: true
---

# Ingest: Competing Biases underlie Overconfidence and Underconfidence in LLMs

## Classification

A peer-reviewed experimental article in *Nature Machine Intelligence*, published 22 April 2026. It manipulates prior-answer visibility and synthetic advice, measures answer changes and token-derived confidence, and compares updates with a Bayesian observer. Dharshan Kumaran and colleagues are affiliated with Google DeepMind, Google Research and UCL; Google DeepMind funded the study. This is controlled behavioral evidence, with computational modelling, rather than a demonstration of an agent review system.

## Summary

In two-stage multiple-choice tasks, displaying a model's own earlier answer generally increased its confidence and reduced answer changes, while opposing advice produced confidence updates larger than the paper's Bayesian benchmark. The main Gemma 3 12B latitude experiment varied answer visibility, advice direction and stated advisor accuracy across 36 conditions. Mean answer-change rates were 13.1% with the answer shown and 34.0% with it hidden; in the hidden conditions, observed-to-Bayesian update ratios were 2.17 for opposing advice and 1.29 for supporting advice. These measurements concern probability assigned to the initially chosen option, even when the final answer differs. The advisor was fictitious, and its reliability was supplied in the prompt. Additional models and four-choice factuality and mathematics tasks showed related patterns; attributing the displayed answer to another model removed the measured ownership effect in one control. The contribution for Commonplace is a bounded reason to validate confidence under the context where it will be used, and a design for testing answer-attribution effects. It does not establish that hiding prior work improves open-ended review.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is evidence for the validation boundary in [generation confidence does not by itself certify soundness](../notes/generation-confidence-does-not-by-itself-certify-soundness.md). Within its multiple-choice, synthetic-advice setup, token-derived probabilities change with answer visibility and advice even after initial calibration. That supports checking confidence under the intended consumption context; it establishes neither a universal inverse association with correctness nor an internal readout of truth. It also compares with [reliability dimensions](../notes/reliability-dimensions-map-to-oracle-hardening-stages.md): discrimination, initial calibration and conformity to a prescribed update rule answer different evaluation questions.

The ownership control is a narrower comparison with [context contamination below compliance reasoning](../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md). Attribution changes the effect of an earlier answer on subsequent judgment, suggesting that who appears to have endorsed content can matter alongside what the content says. The experiment does not test explicit refusal, prose stance drift or the quality of independent critiques, so it cannot supply evidence for those parts of the note.

## Learning Claims (our opinion)

The source studies adaptation within a decision: a model receives a question, optionally its earlier answer, and an assigned recommendation with a stated reliability, then chooses again. Its weights and answer interface stay fixed. The main procedure is stateless; the experimenter reconstructs the information available at the second call. The fitted Bayesian regression model is the researchers' model of this behavior, not a theory the answering LLM develops or revises.

Against the [theory-builder](../notes/definitions/theory-builder.md) conditions, the tested arrangement fails condition 4: the procedure is stateless, and nothing from one decision is kept for another. The earlier answer and the advice are stated and change the second answer, which meets conditions 1 and 2 for them. Condition 3 is not shown: the advice supplies an alternative and a reliability claim rather than a reason identifying an error, and changing an answer after disagreement is not evidence that the model criticized what its first answer says. The paper measures responsiveness and deviations from its normative benchmark, not durable improvement. Its useful contribution is a warning that both attachment to one's answer and excessive deference to contradiction can distort a revision process before any learning claim is assessed.

As [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) distinguishes, results inside a supplied interface do not select that interface. These experiments vary visibility, attribution and advice within a fixed choice-and-confidence procedure. They do not compare it with source-backed criticism, tool verification, alternative confidence representations or a persistent revision workflow. Transfer of the researchers' fitted model from SimpleQA to GSM-MC supports predictive reuse across those task families, not superiority of the fixed interface.

## Extractable Value

1. **Validate confidence after the context changes.** The ownership and synthetic-advice interventions provide a concrete empirical qualification for the existing generation-confidence note: calibration before advice does not establish validity of confidence after advice or exposure to an earlier answer. The result concerns answer-token probabilities in bounded tasks, not every confidence report. [quick-win]
2. **Separate endorsement from evidence in a review experiment.** A Commonplace test could hold a draft and its source material constant while varying whether a prior verdict is absent, attributed to the reviewing agent, or attributed to another reviewer. Measure correction quality as well as expressed confidence. The paper motivates this comparison through its attribution control; it supplies no result for Commonplace review quality. [experiment]
3. **Measure resistance and overreaction separately.** Within the paper's fixed multiple-choice procedure, answer visibility and opposing advice can push confidence in different directions. A single aggregate answer-change rate can therefore conceal different failure modes. Retain the neutral-advice control and distinguish probability of the original option from confidence in the final choice when reusing the method. [experiment]

## Limitations (our opinion)

The normative comparison depends on using calibrated initial confidence as a prior and the stated advisor accuracy as the required conditional likelihood. There was no real advisor whose errors, dependence on the answering model, or reliability could be checked. In deployment, a claimed accuracy is not automatically the conditional evidence needed for the same Bayesian update. The study therefore establishes behavior under stipulated advice, not optimal integration of real reviewers' judgments.

The reported Gemma calibration used 40,000 held-out latitude questions and a fixed scaling temperature of 3.3, with residual expected calibration error of 0.09. This does not guarantee calibration after every contextual intervention or on every task. The paper's assurance that calibration rules out calibration artifacts is stronger than that evidence. Its over/underconfidence score measures deviation from the ideal observer, not ordinary calibration against observed correctness; the extracted equation also has a sign convention that appears inconsistent with the surrounding interpretation, so exact signed values should not be reused without checking the original presentation.

The controls weaken pure copying and a simple preference for in-context over stored information as explanations. They establish a behavioral attribution effect, not the proposed human-like drive for self-consistency. The suggested RLHF explanation was not tested against matched training conditions. The adjusted opposing-advice effect with the initial answer visible subtracts an average visibility effect, so its interpretation depends on that additive adjustment. Supporting advice was not uniformly unbiased: even the main Gemma result reports a ratio above one.

Models used short completions, mostly stateless calls, and constructed choice sets. Task difficulty differed across models, preventing a clean ranking of their susceptibility. Repeating the same questions across conditions does not create independent question samples. The o1-preview results lack confidence measurements. Additional factuality and mathematics tests broaden the evidence beyond latitude questions but do not establish generality to open-ended reasoning or autonomous revision.

The capture contains the main article; separately linked supplementary material was not captured. Some control details and transfer analyses are therefore available only through the article's summaries. No implementation was inspected or executed for this ingest. The paper releases figure and regression code but states that complete experiment execution depends on proprietary inference infrastructure; this analysis is not a reproduction.

## Recommended Next Action

Update [generation confidence does not by itself certify soundness](../notes/generation-confidence-does-not-by-itself-certify-soundness.md) with this bounded example of context-sensitive confidence, keeping the answer-token measurement, synthetic-advisor assumptions and distinction between initial calibration and subsequent updating beside the claim.
