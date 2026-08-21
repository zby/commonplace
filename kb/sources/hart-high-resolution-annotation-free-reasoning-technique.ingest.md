---
description: "HART hardens final-answer feedback for visual evidence selection by withholding alternative image access, while residual shortcuts bound the transfer to KB context routing"
source_snapshot: "hart-high-resolution-annotation-free-reasoning-technique.md"
ingested: "2026-08-21"
type: kb/sources/types/ingest-report.md
domains: [reinforcement-learning, context-selection, oracle-theory, multimodal-reasoning]
---

# Ingest: HART: High-Resolution Annotation-Free Reasoning Technique through a Closed-loop Framework

Source: [hart-high-resolution-annotation-free-reasoning-technique.md](./hart-high-resolution-annotation-free-reasoning-technique.md)
Captured: 2026-08-21
From: https://arxiv.org/abs/2602.23615

## Classification

Genre: scientific-paper -- an arXiv v3 preprint that specifies a reinforcement-learning method, pilot study, benchmark comparisons, grounding evaluation, and ablations.
Domains: reinforcement-learning, context-selection, oracle-theory, multimodal-reasoning
Author: Eight Nanjing University researchers. The paper gives concrete prompts, objectives, data splits, baselines, and results across several visual benchmarks, but this ingest did not inspect its advertised code or reproduce the experiments.

## Summary

HART trains a large multimodal model to select question-relevant regions from a downsampled image without bounding-box supervision. Its key intervention crops the predicted high-resolution regions, withholds the full image, and asks the model to answer from the crops alone. This makes answer correctness more informative about whether the selected regions contain sufficient evidence. AP-GRPO then gives larger policy updates and smaller KL penalties to correct crop-only answers, followed by supervised fine-tuning with the full image visible. The paper reports that correct answers paired with incorrect grounding fall from 36.5% to 21.5% for Qwen2.5-VL-7B and from 63.8% to 55.9% for InternVL3-8B in its pilot. Its trained Qwen2.5-VL-7B system reaches 62.4% on MME-RealWorld-Lite versus 42.3% for the base model and 43.7% on TreeBench versus 37.0%, while AP-GRPO improves measured grounding by 25.2 and 11.7 percentage points over the base model on TreeBench and Visual CoT.

## Connections Found

HART is a bounded empirical anchor for [feedback-trained memory management's oracle dependence](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md): it redesigns an execution context so a downstream outcome better discriminates an earlier selection decision. Applying this mechanism to textual KB routing is our inference, not the paper's result. Its crop-only trial also exemplifies the intervention route in [a checked outcome licenses retaining an episode, not abstracting its explanation](../notes/checked-outcome-licenses-episode-retention-not-abstraction.md), while the remaining correct-answer/incorrect-grounding cases keep the claim inside the [available oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md). HART usefully contrasts with [VAIR](./an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md), which exposes answer correctness as non-discriminating for reasoning validity, and [CEDAR-GRPO](./cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md), which adds explicit process rewards instead of changing causal access to evidence. Its experimental interpretation rests on both the [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and the rule that [an experiment identifies only its actual contrast](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

## Extractable Value

1. **Alternative evidence paths can be withheld to make an outcome oracle more discriminating** -- HART does not obtain a stronger grounding label for training. It changes what the answerer can see, so success depends more strongly on the selected crops. The transferable hypothesis is that a KB context selector could be tested under selected-context-only execution rather than receiving credit while the full corpus or broad context remains available. That transfer requires its own experiment. [experiment]

2. **Selection fidelity should be measured conditional on successful outcomes** -- HART's most revealing statistic is not answer accuracy alone but the rate of incorrect grounding among correct answers. A context-routing evaluation should likewise ask how often a successful task used an irrelevant or insufficient selection, because aggregate task success can conceal shortcuts and unused context. [experiment]

3. **Oracle hardening can change the execution environment instead of only changing the judge** -- VAIR and the current oracle notes emphasize verifier discrimination; HART adds a complementary design move: restrict causal access so an existing outcome check bears more directly on the intermediate choice. This suggests isolation and negative-control interventions as part of selector evaluation. [deep-dive]

4. **Residual shortcut success marks the self-verification boundary** -- Even after the crop-only intervention, 21.5% and 55.9% of correct pilot answers retain incorrect grounding under the paper's metric. HART therefore strengthens a soft proxy rather than creating a direct grounding oracle. That distinction prevents its self-verification language from authorizing route-level conclusions outside the measured setting. [quick-win]

5. **Sufficiency, necessity, and attribution remain separate** -- Answering from selected crops provides evidence that the crop set was sufficient for that response. It does not show that the crops were necessary, that every selected region mattered, or that the emitted reasoning faithfully used them. Question-only, shuffled-crop, and targeted ablation controls would test those stronger claims. [experiment]

6. **The result is learning inside a fixed visual-evidence decomposition** -- Behaviour can condition on a question, downsampled full image, predicted boxes, cropped regions, and answer feedback; it can compose bounding-box and answer tokens through the model policy. The learned mapping changes through AP-GRPO and supervised fine-tuning. Bounding boxes, cropping, the two-stage prompts, binary answer reward, model families, data split, benchmark taxonomies, and most of the training schedule remain fixed. The ablations support their varied optimizer stages and `k` settings, not the ROI decomposition as a universal evidence-routing design. [just-a-reference]

## Limitations (our opinion)

The paper's strongest claim is narrower than “annotation-free grounding verification.” Training uses no bounding-box labels, but grounding evaluation still relies on Visual CoT and TreeBench boxes plus a chosen overlap threshold. During training, AP-GRPO observes binary answer correctness and treats a correct crop-only answer as evidence of good grounding. Lucky guesses, question priors, oversized crops, or irrelevant visual cues can preserve the answer without faithful localization. The paper's own residual mismatch rates show that this proxy remains imperfect.

The claim that higher mutual information between localization and response correctness demonstrates stronger “causal dependency” is too strong. Mutual information is associational. Withholding the full image is a meaningful intervention on information access, but crop sufficiency still does not establish necessity, per-region attribution, or reasoning-path faithfulness. The paper does not report question-only, shuffled-crop, matched-area random-crop, or targeted region-removal controls that would distinguish those alternatives.

The effective update space is fixed around a visual ROI pipeline. Inputs are a downsampled image and question for localization, then selected high-resolution crops and the question for the crop-only answer; later supervised fine-tuning restores the full image. Available operations are box emission, fixed cropping, and token generation. The policy can learn mappings among those surfaces, but cannot revise the evidence representation, crop operator, prompt decomposition, reward target, or task taxonomy. Improvements within that space do not validate those fixed choices for text retrieval or agent-operated KB routing.

The empirical evidence is point-estimate evidence from a preprint. It uses a small set of base-model families, one principal training corpus, fixed data splits, and no reported repeated-training uncertainty or significance analysis. Several evaluations are multiple-choice, where answer correctness can be less discriminating than in open-ended work. The method bundles the crop-only loop, AP-GRPO weighting, supervised fine-tuning, and their order; its ablations vary important pieces but do not isolate every adjacent choice. The repository was not inspected and no training or evaluation was executed, so implementation and outcome claims remain paper-only.

Finally, transfer from image-region selection to KB context routing is our analogy. Textual artifacts have authorship, entailment, cross-document dependencies, and misleading-but-plausible content that bounding-box overlap does not model. A selected-note-only success could still come from model priors or reconstructed knowledge. HART motivates a routing experiment; it does not establish a KB design rule.

## Recommended Next Action

Update [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) with one explicitly conjectural experiment: compare broad-context and selected-context-only execution for a textual selector, add question-only, shuffled-selection, and targeted-removal controls, and measure both task success and selection fidelity before treating HART's visual intervention as evidence for KB routing.
