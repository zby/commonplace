---
description: "Meta's V-JEPA 2 article and paper page ground action-conditioned world models as predictors for planning in new physical environments"
type: kb/sources/types/source-review.md
tags: [world-models, predictive-modeling, robotics]
---

# Meta V-JEPA 2 action-conditioned world model

**Sources:** https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/ and https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/

## Key Points

- Meta describes V-JEPA 2 as a video-trained world model for understanding, prediction, planning, and robot control in new environments.
- The article defines world-model capability in action terms: a world model should predict how the world will evolve and how it will change if an agent takes an action, then support planning action sequences toward a goal.
- V-JEPA 2 uses an encoder that maps video to embeddings and a predictor that outputs predicted embeddings conditioned on what is to be predicted.
- The training story separates actionless pretraining from action-conditioned robot-data training. After the second phase, the predictor accounts for candidate actions and can be used for control.
- The reported robot-control setup uses image goals, predicts consequences for candidate actions, ranks actions by distance to the goal embedding, and replans with model-predictive control.
- The publication page summarizes V-JEPA 2-AC as a latent action-conditioned world model trained with less than 62 hours of robot video and deployed zero-shot on Franka arms in two labs.

## Relevance to the KB

This source is the cleanest grounding for [World models assess reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md). It gives the missing third route next to prose semantic judgment and [formal symbolic reach assessment](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md): a distributed-parametric artifact can support reach assessment when its action-conditioned predictions are evaluated across the intervention or shift class the commitment claims to cover.

## Limitations

The evidence is domain- and task-shaped: video understanding, short-horizon physical prediction, and robot manipulation. It does not show general semantic reach assessment and does not identify causal structure in Pearl's sense. The benchmark gaps Meta reports also matter: learned world models can be useful reach-assessment substrates without being reliable world simulators across all physical reasoning cases.
