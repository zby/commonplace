---
description: "Meta's V-JEPA 2 announcement grounds action-conditioned latent prediction, model-predictive robot control, and the stated limits of its physical-reasoning evidence."
source: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
captured: "2026-08-31"
capture: trafilatura
capture_scope: full-source
genre: tool-announcement
snapshot_sha256: d6f00c9bb65b90bb7b5e2ced711972dc491db9f9800846dd145e53e335c42463
ingested: "2026-08-31"
occasion: "Split a legacy source review that combined two source URLs and analysis into one snapshot and ingest pair per primary source."
type: kb/sources/types/ingest-report.md
domains: [world-models, robot-planning, physical-reasoning]
---

# Ingest: Meta's V-JEPA 2 world model and physical-reasoning benchmarks

## Classification

This is an official tool and model announcement: it explains the released model and benchmarks, selects headline results, and presents Meta's intended interpretation rather than a complete scientific argument.
Author: Meta AI, the organization that developed and released V-JEPA 2 and the three benchmarks.

## Summary

Meta presents V-JEPA 2 as a 1.2-billion-parameter video world model trained first without actions on more than one million hours of video and one million images, then action-conditioned on 62 hours of robot data. For robot control, its encoder represents current and image-specified goal states while its predictor imagines candidate-action consequences; model-predictive control ranks those consequences by goal proximity, executes one action, and replans. Meta reports zero-shot transfer to its lab robots and 65%--80% success on pick-and-place tasks with unseen objects and environments, while its three released benchmarks expose large remaining gaps in physical plausibility, paired video reasoning, and causal video question answering. Read this account for the public system shape, headline evidence, and admitted boundaries, not for enough experimental detail to judge the claimed state of the art independently.

## Quotes

No source quotes have been retained yet.

## Connections Found

This announcement is the URL-specific public evidence anchor for [World models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md): it describes candidate-action prediction, goal-distance ranking, replanning, and deployment shifts, while also reporting substantial benchmark gaps. It also supplies a concrete implementation case for [An action model matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md), because the learned predictor affects behavior through receding-horizon model-predictive control. Its empirical gains occur inside a fixed decomposition: video and action histories condition an encoder-predictor model; candidate robot controls are the composable responses; the learned hypothesis class maps latent state and actions to predicted latent states; and the architecture, training stages, control interface, embedding-distance objective, visual subgoals, planner, and benchmark partitions remain outside the effective update space. The results support the compound configuration in the reported settings but do not isolate those fixed choices.

## Extractable Value

1. **Replace the blog half of the combined V-JEPA 2 evidence record with a source-specific anchor.** This ingest gives the existing world-model note a durable target for Meta's public claims about action-conditioned prediction, unseen deployment settings, and model-predictive control without conflating them with a second primary URL. [quick-win]
2. **Use the controller as a concrete consumption-path example.** The predictor is behaviorally consequential because its imagined action outcomes are ranked against a goal and consumed by a re-planning loop, directly instantiating the KB's distinction between a stored model and a model-mediated action pathway. [quick-win]
3. **Keep the robot-control evidence inside its tested update space.** The reported success can support the encoder-predictor-plus-controller configuration, but it does not establish that the fixed action basis, latent goal distance, hand-specified visual subgoals, or receding-horizon planner is necessary or preferable. [deep-dive]
4. **Treat the benchmark designs as evaluation references, not as general physical understanding tests.** Paired plausible/implausible videos, minimal-change question pairs, and causal or counterfactual questions offer reusable test shapes, while the announcement does not establish their coverage of physical reasoning as a whole. [just-a-reference]
5. **Record the admitted single-timescale boundary beside the reach claim.** Meta identifies hierarchical temporal and spatial planning as future work, which limits how far the reported short-horizon and visually decomposed tasks can support claims about general planning. [quick-win]

## Limitations (our opinion)

The author is also the model and benchmark vendor, so the announcement favors headline comparisons and does not provide the technical detail, full baselines, uncertainty, failure cases, or matched ablations needed to judge its state-of-the-art claims independently. The robot results do not separate what was learned from what was fixed: the action interface, candidate generation, embedding-distance score, model-predictive controller, and human-provided visual subgoals are part of the treatment. An ablation would support only the choice it varied; none reported here establishes that this decomposition is the right one. Zero-shot deployment on new lab objects and environments is therefore evidence for transfer within the reported setup, not for arbitrary robot embodiments, long-horizon tasks, causal understanding, or general physical reasoning. The account itself says prediction operates at one timescale, and the 65%--80% range leaves material failures unexplained.

## Recommended Next Action

Update [World models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) so its V-JEPA 2 claim links to this URL-specific ingest instead of the legacy combined review.
