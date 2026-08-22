---
description: "MDA splits scientific model discovery between LLM hypothesis proposal and Bayesian selection, improving interventional forecasts inside a fixed domain decomposition"
source: https://arxiv.org/abs/2608.09696v1
captured: "2026-08-12"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: c1052d16951c50545cb92113a2515726d5cffaa41fbbec43ab063c9de3d965d6
ingested: "2026-08-12"
type: kb/sources/types/ingest-report.md
domains: [scientific-discovery, bayesian-experiment-design, mechanistic-world-models, learning-theory]
---

# Ingest: Model Discovery Agent: LLM-assisted Bayesian Experiment Design

## Classification

An arXiv preprint that specifies a model-discovery method, introduces a benchmark, and reports controlled comparisons and ablations across three synthetic scientific domains.
Author: Kevin Murphy, Department of Computer Science, University of British Columbia. The paper gives unusually extensive method and benchmark detail, but it is a single-author preprint and has no independent replication in the captured record.

## Summary

The paper presents the Model Discovery Agent (MDA), which assigns open-ended mechanism proposal to an LLM while using sequential Monte Carlo to maintain parameter and structure posteriors, predictive checks to trigger new proposals, and Bayesian value of information to select experiments that discriminate between candidate models. It evaluates this split on FORCEBENCH physics, CHEMBENCH enzyme kinetics, and a new deterministic and stochastic NEURONBENCH. MDA generally reaches accurate held-out interventional forecasts and interpretable mechanisms with fewer experiments than free-form LLM agents or prior systems. The most informative results are more qualified than the headline: explicit model-based forecasting consistently helps, while value-of-information acquisition is not always better than LLM or random acquisition; stronger base models narrow the advantage; and stochastic neuron experiments show that a wrong likelihood can confidently select the wrong mechanism even when the candidate pool contains the truth.

## Connections Found

This source is an empirical anchor for [theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md): explicit, addressable mechanisms plus discriminating interventions reduce the target experiments needed for accurate forecasts, although the paper does not test reuse of a retained theory across a shift. It is also a worked instance of [formal symbolic systems assessing explanatory-reach through causal obligations](../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md), with marginal likelihood and held-out interventional prediction judging explicit forward models, and a useful contrast to the distributed-parametric route in [world models assess explanatory-reach through action-conditioned prediction](../notes/world-models-assess-explanatory-reach-through-action-conditioned.md).

Its limiting role is equally important. Under the lens of [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), MDA expands a candidate pool while keeping domain grammars, intervention spaces, likelihood families, summary representations, objectives, and benchmark worlds largely fixed. It therefore demonstrates active identification within those boundaries, not evidence that the enclosing decomposition is right. The simulator-known targets also leave it inside the reachability boundary described by [known-target discovery benchmarks show reachability, not discovery closure](../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md).

Among captured sources, MDA directly extends [DiscoverPhysics](./discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) by wrapping it as FORCEBENCH and replacing monolithic LLM inference with explicit Bayesian belief update and design. It complements [FALSIFYBENCH](./falsifybench-inductive-reasoning-rule-discovery-games.ingest.md), which measures whether an LLM chooses disconfirming probes, and [Can LLM Agents Infer World Models?](./can-llm-agents-infer-world-models-agentic-automata-learning.ingest.md), which exposes query-policy and evidence-use failures that MDA moves into formal machinery.

## Extractable Value

1. **Separate hypothesis proposal, belief update, and experiment selection.** MDA gives the LLM the task for which an open semantic prior is useful -- proposing mechanisms -- while assigning posterior update, rejection, and query choice to inspectable statistical procedures. This is a concrete architecture for avoiding the non-informative-query and evidence-integration failures seen in agentic automata learning without pretending that formal search can generate every scientific hypothesis. [deep-dive]

2. **Explicit mechanistic theories can buy experimental sample efficiency.** On authored physics, chemistry, and neuron worlds, model-based forecasting reaches accurate interventional predictions with fewer experiments than the compared free-form LLM pathways. This is direct evidence for the intermediate prediction in [theory-mediated learning](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), but not yet for its stronger claim about retaining and reusing a theory across a controlled shift. [experiment]

3. **Predictive fit and mechanism recovery need separate scores.** CHEMBENCH contains expressions with very low held-out error but the wrong symbolic mechanism, while FORCEBENCH shows that a free-form agent can name an exact law yet fail to compute accurate trajectories with it. Scoring both symbolic equivalence and interventional forecast accuracy prevents either surface from standing in for the other. [quick-win]

4. **The observation model is part of the discovery claim, not plumbing.** In stochastic NEURONBENCH, a deterministic likelihood confidently inverts the model ranking as channel noise grows. Particle filtering remains robust, while fixed and learned summaries are cheaper but discard different discriminating signals. The result operationalizes the formalization boundary: Bayesian correctness is conditional on the representations and likelihood supplied to it. [quick-win]

5. **Residual-triggered pool expansion is broader search, not unrestricted discovery.** MDA can notice that its current candidates fail and ask the LLM for another structure. Yet FORCEBENCH constrains force-law forms, CHEMBENCH supplies a mechanism grammar, and NEURONBENCH maps proposals into channel archetypes and protocol menus. This gives the KB a concrete case for distinguishing an expanding pool inside a meta-language from revising the schema that decides what hypotheses can exist. [quick-win]

6. **Do not assign the compound system's gain entirely to value-of-information acquisition.** In deterministic NEURONBENCH, VoI and LLM-designed experiments are similar; in the stochastic version, random acquisition is comparable in one analysis; and the strongest FORCEBENCH comparison changes both acquisition and forecasting. The paper supports the whole proposal-plus-inference-plus-design stack more strongly than it supports a universal advantage for VoI alone. [just-a-reference]

7. **Experiment efficiency and total efficiency are different ledgers.** MDA reduces interactions with the simulated world, but nested structure SMC, parameter SMC, particle filtering, CMA-ES, and simulator-trained summary networks can be computationally expensive. The learned-summary result shows a roughly four-order-of-magnitude per-decision speedup in one neuron setting, but does not make the headline experiment-count curves a full cost comparison. [just-a-reference]

## Limitations (our opinion)

The results show improvement inside a supplied effective update space. MDA can condition on the domain description, accumulated experiment history, residuals, predictive checks, and candidate simulations. It can compose LLM model proposals, Bayesian parameter and structure updates, experiment choices from a menu or bounded box, and several observation models. Its expressible mappings are nevertheless fixed by domain-specific forward-model grammars, priors, likelihoods, summaries, intervention variables, acquisition objectives, and submission rules. None of the main comparisons varies that whole decomposition. The CHEMBENCH ablation supports only the components it changes -- M-open exploration, CMA-ES optimization, and adaptive pool management -- and its intermediate configurations use one seed. It does not validate adjacent fixed choices or the decomposition as a whole.

All target mechanisms live in synthetic or simulator-backed worlds with known test interventions. This makes symbolic equivalence and forecast error hard to game, but removes problem selection, instrument construction, uncontrolled confounding, changing environments, and prospective scientific value. The result therefore supports active mechanism identification and reachability, not autonomous scientific discovery in the wild. Even the paper's “M-open” cases remain representable inside a domain scaffold built with knowledge of the benchmark family.

The baseline attribution is also compound. “MDA” usually combines Bayesian forecasting with VoI acquisition, while the “LLM agent” combines LLM forecasting with LLM acquisition. The paper contains useful partial ablations, but no single factorial study isolates proposal quality, posterior inference, forecast representation, acquisition policy, experiment-space design, and compute across every domain. A stronger Fable agent closes much of the FORCEBENCH gap, and the remaining advantage is strongest on numeric forecasting rather than exact symbolic recovery.

Finally, the work is a single-author preprint with small seed counts in several experiments and substantial reliance on author-created wrappers, priors, model libraries, and the new NEURONBENCH. Independent reproduction and evaluation on real experimental systems are absent. The paper is strong evidence about the behavior of this engineered stack on its benchmark ladder, but weak evidence for the universality of its scientific-discovery framing.

## Recommended Next Action

Revise [theory-mediated learning may improve sample efficiency under structured shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) to add MDA as evidence for its intermediate pathway -- explicit theory search plus intervention-based assessment reducing target observations -- while stating that MDA has no cross-shift retention arm and therefore does not yet test the note's decisive retained-theory reuse prediction.
