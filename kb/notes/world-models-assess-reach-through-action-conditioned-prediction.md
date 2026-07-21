---
description: "Learned world models can assess reach when action-conditioned predictions are tested across the interventions or shifts a commitment claims"
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [foundations, computational-model, self-improving-systems]
---

# World models assess reach through action-conditioned prediction

[Reach assessment](./definitions/reach-assessment.md) is not limited to prose judgment or formal symbolic proof. A learned predictive world model can assess reach when a candidate commitment's claimed generality is represented as predicted consequences under actions, interventions, or environment shifts, and those predictions are tested against the class of changes the commitment claims to cover.

This is a distributed-parametric route. The retained artifact is not a theorem, causal graph, or prose explanation; it is a learned representation plus predictor. Its reach is visible when the predictor continues to support correct anticipation or control outside the exact observations that fitted it.

LeCun's JEPA line is close to this route. Meta's [V-JEPA article](../sources/meta-v-jepa-world-model.source-review.md) frames the predictor as an early physical world model: it predicts masked video regions in an abstract representation space rather than reconstructing pixels. Meta's [V-JEPA 2 account](../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md) makes the reach-assessment shape more explicit: after action-conditioned training, the predictor can imagine consequences of candidate robot actions, score them against a goal, and replan in new environments.

That is not the same as [formal symbolic systems assessing reach through causal and proof obligations](./formal-systems-can-assess-reach-through-causal-and-proof-obligations.md). A formal symbolic route checks consequences inside an explicit causal model, theorem, invariant, or proof obligation. A learned world-model route probes a latent predictor by asking whether its action-conditioned rollouts keep working under specified interventions or shifts.

The [formalization boundary](./formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) reappears here in a different [representational form](./definitions/representational-form.md): a world model can support reach assessment only as far as its learned state, action conditioning, training distribution, and evaluation regime cover the intended claim. A model that predicts familiar videos, or succeeds on one robot setting, has not thereby assessed reach for arbitrary physical reasoning. The reach enters through the counterfactual test surface: what happens when the agent considers an action, shift, or unseen setting the commitment says should still be covered?

So world models belong beside causal/proof obligations, not inside them. If a system's commitment is stored as prose, semantic judgment is still needed. If it is stored as a symbolic causal or proof artifact, formal machinery can carry the assessment. If it is stored as a learned predictive artifact, action-conditioned prediction and shift testing can carry part of the assessment.

---

Relevant Notes:

- [Reach assessment](./definitions/reach-assessment.md) — extends: adds the distributed-parametric route through learned predictors
- [Representational form](./definitions/representational-form.md) — grounds: the prose/symbolic/distributed-parametric split that decides which assessment route is available
- [Formal symbolic systems assess reach only through causal and proof obligations](./formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) — contrasts: symbolic route through explicit causal/proof obligations rather than learned latent prediction
- [Reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) — evidence: reusable structure matters when generalizing under shifts
- [Meta V-JEPA world-model framing](../sources/meta-v-jepa-world-model.source-review.md) — evidence: LeCun/JEPA framing of latent predictive world models
- [Meta V-JEPA 2 action-conditioned world model](../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md) — evidence: action-conditioned prediction used for planning and control
- [Why AI systems don't learn and what to do about it](../sources/why-ai-systems-dont-learn-and-what-to-do-about-it.ingest.md) — evidence: broader LeCun/Dupoux/Malik architecture where observational world modeling and action learning interact
