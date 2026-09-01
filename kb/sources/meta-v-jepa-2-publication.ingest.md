---
description: "Meta's V-JEPA 2 abstract reports video benchmarks and zero-shot robot planning, while leaving the planner and fixed design choices unexamined."
source: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
captured: "2026-08-31"
capture: trafilatura
capture_scope: abstract
genre: scientific-paper
snapshot_sha256: 50aa2c2d74c1a2a0faf0a027f53c78e9e7411e39c00a4174dc9c8167585d02c8
ingested: "2026-08-31"
occasion: "Split a legacy source review that combined two source URLs and analysis into one snapshot and ingest pair per primary source."
type: kb/sources/types/ingest-report.md
domains: [world-models, self-supervised-learning, robot-planning]
---

# Ingest: V-JEPA 2 publication abstract

## Classification

This is a scientific-paper abstract on Meta's research publication page. It reports benchmark and robot-deployment results but does not expose the full paper's methods or evidence.
Author: Adrien Bardes and the V-JEPA 2 coauthors provide the primary research-team account; publication by Meta supplies institutional provenance but also an interest in presenting the strongest results.

## Summary

The abstract presents V-JEPA 2 as a self-supervised world model pretrained without actions on more than one million hours of video and images, then adapted into an action-conditioned model with less than 62 hours of robot video. It reports strong video-understanding and anticipation benchmarks, video question-answering results after language-model alignment, and zero-shot image-goal pick-and-place deployment on Franka arms in two labs without environment-specific data, task-specific training, or rewards. Read it as the primary source for those headline claims, not for the architecture, planning procedure, experimental controls, or breadth of physical-world generalization.

## Quotes

No source quotes have been retained yet.

## Connections Found

The abstract is a narrow technical basis and boundary for [World models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md): it supports the reported action-conditioned post-training and cross-lab zero-shot deployment conditions, but not the note's fuller account of imagined action consequences, scoring, or replanning. Its strongest role is to anchor the paper-page deployment summary while limiting claims that require the full paper or a more detailed release source.

## Extractable Value

1. **Separate primary-source identity for the paper-page claims** -- The abstract can replace the legacy combined review as the durable basis for the paper authors' benchmark and deployment summary without attributing a second source's mechanism details to this URL. [quick-win]
2. **A concrete transfer test for an action-conditioned predictor** -- Deployment on Franka arms in two labs, without data collected in those environments, is a context-bound instance of testing a learned predictor under an environment shift rather than only on its training observations. [just-a-reference]
3. **A sharply asymmetric data regime** -- The reported combination of more than one million hours of general video and less than 62 hours of robot video is a useful data point for discussing broad observational pretraining followed by limited action-conditioned adaptation. [just-a-reference]
4. **Evidence inside a fixed effective update space** -- The results show that the selected latent model, action conditioning, planner, image-goal objective, robot embodiment, and task setup worked together in the reported deployments; the abstract reports no comparison that isolates whether those fixed choices were necessary or preferable. [deep-dive]
5. **A clear source boundary for later grounding** -- Benchmark definitions, baselines, uncertainty, task success rates, action parameterization, planning details, and ablations require a full-paper observation rather than this abstract. [quick-win]

## Limitations (our opinion)

The abstract-only capture prevents checking experimental protocols, baseline comparability, variance, deployment success criteria, failure cases, or the mechanisms behind the headline results. The two-lab Franka deployment is meaningful evidence of transfer within a narrow embodiment and pick-and-place regime, not evidence for arbitrary physical reasoning. The learner could condition on large-scale video and image histories, limited robot trajectories, actions during post-training, and image goals, but the abstract does not specify the composable action set or the mappings the model and planner could express. The latent representation, architecture, action parameterization, planner, objective, datasets, embodiment, and task partition remain fixed outside the reported learning space. Because no matched ablation varies those choices here, success inside that space does not validate the decomposition itself, as explained in [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). The authors' and publisher's institutional interest also makes the abstract a selective presentation rather than an independent evaluation.

## Recommended Next Action

Revise [World models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) so this ingest supports only the publication abstract's action-conditioned post-training and zero-shot deployment conditions, while fuller planner-mechanism claims remain grounded in the separately captured release source.
