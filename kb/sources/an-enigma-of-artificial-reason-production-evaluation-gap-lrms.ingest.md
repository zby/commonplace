---
description: "VAIR paper showing large reasoning models can solve math problems while failing to evaluate invalid reasoning that reaches correct answers"
source: https://arxiv.org/abs/2606.01462
captured: "2026-06-17"
capture: web-fetch
genre: scientific-paper
snapshot_sha256: 82dc985d2a279bf02e0f3e3727eb0001a1c435eee3fb7b2838d1fd216c869b17
ingested: "2026-06-17"
type: kb/sources/types/ingest-report.md
domains: [evaluation, oracle-theory, reasoning, llm-reliability]
---

# Ingest: An Enigma of Artificial Reason

## Classification

ArXiv preprint with benchmark construction, model and human experiments, process-reward-model evaluation, representation probes, causal patching, and limitations.
Author: NUS/MIT/SMART-affiliated authors; credibility comes from the concrete benchmark design, human comparison, and mechanistic analyses, but it remains preprint-tier evidence.

## Summary

Sun, Yeo, Solar-Lezama, and Tan introduce VAIR, a math-reasoning evaluation set where solutions contain trivial reasoning flaws while preserving the correct final answer. This separates answer correctness from reasoning validity. The paper reports that frontier large reasoning models solve the underlying problems almost perfectly and handle controls where answer validity matches reasoning validity, but can collapse toward chance when grading VAIR solutions; humans show only a much smaller gap. The authors argue that answer confirmation bias explains the failure: models often re-solve the problem, confirm the answer, and then overlook or rationalize invalid steps. Linear probes and causal patching on open-weight LRMs support the mechanism by showing answer-token representations can corrupt reasoning-validity representations and shift both verdicts and verbalized evaluation behavior. The appendix extends the warning to process reward models, which also degrade on valid-answer-invalid-reasoning cases.

## Claims

- **Claim (paraphrase):** On VAIR's math-grading task, six frontier large reasoning models remained strong at solving and at grading controls where answer validity matched reasoning validity, but degraded when trivial reasoning flaws led to a valid final answer; their verbalized evaluations frequently independently solved for the answer and then blindly endorsed or rationalized flawed steps.
  - **Source extract (verbatim):** In order to control for this potential confound, we construct the Valid-Answer-Invalid-Reasoning (VAIR) dataset: A set of math question-solution pairs with invalid reasoning steps — steps that do not follow from either the previous steps or the question premises — but valid answers. By testing LRMs on how they evaluate VAIR solutions, we prevent the use of answer correctness or validity as a correlate for reasoning quality: If LRMs simply solve the problem directly and check that the answer matches, they will fail to detect invalid reasoning.
  - **Source location:** Section 2, “Evaluating the Evaluation of Reasoning.”
  - **Source extract (verbatim):** We evaluate six frontier LRMs (Claude Sonnet 4.6, Claude Opus 4.7, DeepSeek R1, GPT 5, GPT 5.4, and Gemini 3.1 Pro) across our four sub-tasks. For the production task, accuracy is measured by answer correctness. For the evaluation tasks, we use a coarse-grained assessment, considering a model’s grade as correct if it is equal to 3 for flawless solutions, and less than 3 for a flawed solution.
  - **Source location:** Section 2.3, “The Production-Evaluation Gap in LRMs.”
  - **Source extract (verbatim):** Overall Comparison. As expected, all evaluated models are highly capable at reasoning production, achieving solution accuracies of 94.7% or above. LRMs also achieve high evaluation accuracy on the VAVR ( >= 91.9%) and IAIR ( >= 95.8%) controls, where answer validity perfectly correlates with reasoning validity. In such cases producing the right answer can easily substitute for evaluating the validity of each step, and LRMs continue to perform well. However, performance collapses on the VAIR dataset, where valid answers are no longer a signal of correct reasoning. Evaluation accuracy drops as low as 47.9% for GPT 5.4 and 52.5% for GPT 5. Even the strongest performer, Gemini 3.1 Pro, experiences a significant performance drop to 78.6% accuracy.
  - **Source location:** Section 2.3, overall comparison; mathematical line breaks normalized.
  - **Source extract (verbatim):** We find pronounced demonstrations of an answer confirmation bias in two ways: First, on a large fraction of VAIR solutions, models evaluate solutions by engaging in Independent Solving, producing their own answer to confirm it against the solutions (Figure 5(a)). Second, LRMs also display Blind Endorsement or Forced Rationalization of flawed reasoning steps towards the confirmed valid answer (Figure 5(d)), with this behavior disappearing when answers are invalid (Figure 5(e)).
  - **Source location:** Section 3.1, aggregate chain-of-thought analysis.
  - **Scope:** Six named frontier LRMs on the paper's math production task and three grading conditions; the workflow labels come from an LLM annotation scheme with a small manual agreement check.
  - **Confidence:** High for the benchmark's controlled answer/reasoning dissociation and reported accuracy gap; moderate for the verbalized workflow characterization, which the authors themselves do not treat as conclusive causal evidence.
  - **Limitation:** The result concerns math-solution grading, not episode abstraction or KB review generally. It shows that answer correctness can fail as a proxy for reasoning validity, but does not establish that every evaluator reconstructs an answer or that a valid trace faithfully records the producing computation.

## Connections Found

The connect pass saved [an-enigma-of-artificial-reason-production-evaluation-gap-lrms.connect.md](../reports/connect/sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.connect.md). It found the source belongs in the KB's evaluation and oracle-theory cluster. The strongest connections are [Oracle strength spectrum](../notes/oracle-strength-spectrum.md), [Error correction works with above-chance oracles and decorrelated checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [The augmentation-automation boundary is discrimination not accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), and [The boundary of automation is the boundary of verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md): VAIR is a concrete case where final-answer validity is an attractive but non-discriminating verifier for reasoning validity. The paper also supports [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md) by cleanly separating final answer correctness from step validity, qualifies [Human writing structures transfer to LLMs because failure modes overlap](../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) by showing both overlap and divergence between human and LRM reasoning evaluation, and gives evidence for [Evaluation automation is phase-gated by comprehension](../notes/evaluation-automation-is-phase-gated-by-comprehension.md) because the PRM appendix warns that automatically derived process labels may inherit answer-confirmation bias.

## Extractable Value

1. **Answer correctness can be a high-accuracy, low-discrimination oracle for reasoning validity** -- This sharpens the KB's TPR/FPR framing: a verifier can appear strong on ordinary controls while failing exactly when the answer and reasoning-validity signals are decoupled. That is new evidence for the oracle-strength and automation-boundary notes. [quick-win]
2. **Reasoning production and reasoning evaluation need separate capability surfaces** -- The paper gives a clean benchmark where stronger solution production does not imply stronger process evaluation. This directly supports writing or updating a note that treats "can solve" and "can grade the reasoning" as different system requirements. [quick-win]
3. **Evaluator error correlation can arise from the same answer-reaching training signal used by generators** -- The PRM result matters for error-correction design: a nominally separate process evaluator may still share the generator's outcome bias if its labels or training objective are answer-outcome-derived. This limits naive "add a judge" architectures. [experiment]
4. **Process-validity benchmarks should decouple output validity from reasoning validity** -- VAIR's construction is a reusable test pattern for soft-oracle hardening: hold the final answer fixed while perturbing the reasoning path. The pattern is relevant beyond math wherever the system can reach a valid output through invalid justification. [experiment]
5. **Human-overlap arguments need per-failure-mode boundaries** -- Humans also degrade on VAIR compared with controls, but far less than LRMs. That supports the KB's failure-mode-transfer methodology while warning against treating human and LLM reasoning safeguards as identical. [just-a-reference]
6. **Mechanistic probes can distinguish verbalized critique from underlying evaluator state** -- The paper's CoT analysis alone would be weak for our purposes, but the probe and patching analyses make the source more useful as evidence about internal answer-validity contamination. [deep-dive]

## Limitations (our opinion)

This should not be treated as settled evidence about all reasoning domains. The benchmark is mathematical, where answer validity and step validity can be sharply separated and manually verified; real KB review, source ingestion, design critique, and scientific reasoning often have messier validity conditions. The model names and results are also point-in-time claims from a 2026 preprint, and several "frontier" model versions are not locally reproducible from the snapshot. The mechanistic work is restricted to open-weight models up to 20B parameters, so the causal account is stronger as a plausible mechanism than as proof about closed frontier systems. Finally, VAIR is adversarial by design: it demonstrates a failure mode, not base-rate prevalence in ordinary agent work. The most transferable lesson is the verifier-design pattern, not the exact performance numbers.

## Recommended Next Action

Write a note titled "Reasoning production is not reasoning evaluation" in `kb/notes/`, connecting [The augmentation-automation boundary is discrimination not accuracy](../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [Process structure and output structure are independent levers](../notes/process-structure-and-output-structure-are-independent-levers.md), and [Semantic review catches content errors that structural validation cannot](../notes/semantic-review-catches-content-errors-that-structural-validation.md). The note should argue that agent systems need explicit evaluators for process validity instead of relying on successful answer production as a proxy.
