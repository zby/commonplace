# An invitation to the HCL authors

> **Status:** This is an exploratory response from the Commonplace project. It asks whether techniques tested by Harness Continual Learning in controlled task streams could help a deployed system learn from real-world tasks. That transfer is our proposal, not a claim made or tested in the HCL paper. We have not contacted the authors, and no response or endorsement is implied.

## Why HCL matters to this workshop

Our [source analysis of HCL](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) reads it as making a consequential system boundary explicit under controlled conditions: persistent harness state around frozen model weights can itself become a sequential learning object. An optimizer proposes a revised harness, an evaluator can reject it, and historical retention is an explicit condition of commitment.

Our thesis is a transfer claim. We want evidence from real-world task execution—outcomes, feedback, failures, and later consequences—to train the deployed system by driving proposals and selection over retained harness state. We call that target setting **deployment-time learning**. HCL's isolated candidates, retention checks, validity checks, and atomic commitment offer techniques for governing those behavior-changing writes. We do not classify HCL's controlled experiments themselves as deployment-time learning or treat them as evidence that the transfer succeeds.

HCL's evaluator requires current-task improvement, historical retention, and validity. Historical loss counts sampled anchors that the incumbent solves and the candidate newly fails. Even when the permitted loss is zero, the guarantee therefore applies to that finite sample rather than to every possible behavior. HCL's textual budget sweep also illustrates how proposal–historical-anchor checks can grow with task history, although the paper does not report a production cost or show that the approach is infeasible.

This combination motivates our question: could a revisable theory of system behavior with genuine [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) derive candidate-specific impact projections well enough to decide which costly evidence is worth acquiring?

## The proposed extension

We propose separating a retained system theory `T` from the candidate-specific impact projection `I_T(S, Delta)` it supports. `T` represents relevant parts of the system's behavior-generating organization under a declared boundary `S`: mechanisms, authority and consumption paths, invariants, program structure, semantic contracts, learned action-conditioned predictions, or a mixture. Given candidate `Delta`, the projection contains theory-derived claims or beliefs about which behavioral functions and evaluation obligations may change. A mapping connects those obligations to procedures capable of observing them, and an evidence-acquisition policy decides which procedures are worth selecting, constructing, validating, and running.

Causal reasoning is an important special case because the question concerns the consequences of a proposed change. It is not the umbrella theory class, and causal vocabulary does not establish explanatory-reach. Structural proofs, compositional models, semantic explanations, and learned predictors can support other parts of the projection. Their claimed explanatory-reach must likewise survive withheld effects, premise changes, and rival explanations rather than only fit earlier diffs.

The working path is:

`candidate + system state + system theory -> impact projection -> evaluation obligation -> select or generate procedure -> validate -> execute -> decide`

This does not treat HCL's four mutable harness parts as a validated explanatory decomposition or causal graph. They are an engineering partition. Local evaluation becomes plausible only when a candidate is sparse in a matching decomposition, dependencies and authority paths are explicit, and its downstream impact closure is small. The workshop's main hypothesis is therefore mixed: enforced structure can supply conservative bounds; broader causal, semantic, or predictive reasoning can derive effects inside and beyond those bounds; and probabilities can represent unresolved uncertainty. The theory's claimed explanatory-reach is a claim for audits to test, not a premise granted by naming it.

[SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) suggests a further experimental factor: the policy might adapt or synthesize an executable evaluation procedure rather than only select a stored anchor. [A separate invitation to the SPADE authors](./for-spade-authors.md) develops that bridge.

## What selective evaluation would change

Selective evaluation cannot retain HCL's full-set acceptance semantics unchanged. If only some anchors are run, the system cannot make an unqualified claim about losses over all anchors. It must leave omitted obligations unknown, still execute the full check, or define a different gate over observed evidence plus a declared residual-risk condition.

The third option introduces theory and projection error as well as modeled residual risk. A false premise, wrong boundary, missing dependency, invalid derivation, bad probability, wrong loss model, or distribution shift could invalidate the reason for omitting evidence. The selector also observes mostly the checks it chooses to run, so harmful effects among omitted checks can remain hidden. Randomized exploration, always-run sentinels, periodic full-suite audits, delayed monitoring, and projections recorded before selection are possible controls, but none is validated here.

## A discriminating experiment

A first comparison could use a fixed, recorded candidate set and score full registered-set evaluation, budget-matched sampled anchors, diff-similarity selection, deterministic dependency-and-authority selection, explicit causal-model selection, and mixed explanatory-theory selection. Held-out change families, controlled changes to load-bearing premises, and rival theories that disagree on unseen candidates would test explanatory-reach rather than only familiar-case fit. A second factor could compare selection from a fixed procedure registry with non-adaptive synthesis and SPADE-inspired adaptive procedure generation.

The comparison would measure evaluator cost, harmful misses, detection coverage, projection calibration or deductive soundness, current gains, held-out retention, and later surprises. Generated procedures would add separate construction, validity-filtering, containment, execution, and reuse costs. An online comparison would also need repeated runs or another way to separate selector quality from trajectory divergence, because different commitment decisions produce different later harness states.

## Questions for the HCL authors

Your view would be especially useful on these questions:

- Which parts of HCL's optimizer–evaluator–commitment loop do you expect to transfer from controlled task streams to evidence generated by real-world tasks, and what would break first?
- What are the measured evaluator costs, and how do they scale with anchors, candidates, and stream length?
- How local do you expect the behavioral effects of typical harness candidates to be?
- What explanations do you already rely on when anticipating the effects of harness changes, and what candidate change would falsify them?
- Which influence or non-influence claims, if any, could be defended through causal mechanisms, dependency or authority structure, invariants or proofs, compositional program structure, semantic contracts, or learned prediction?
- Could the historical evaluation surface itself be adapted or generated for each candidate, rather than only accumulated as fixed anchors, and what would keep that generator from overfitting the gate?
- How might omitted checks be audited well enough to reveal harmful misses and calibrate impact projections?
- Which model, runtime, outer-capability, evaluator, or environment boundaries held fixed in HCL would you treat as revisable in a broader system?

These questions arise from the proposed extension. They are not claims that the HCL paper was obliged to answer.

The [full theory-guided selective-evaluation workshop](./README.md) develops the HCL reading, provisional theory-and-impact model, changed acceptance semantics, adaptive procedure-generation option, reach-assessment and audit problems, and experimental comparison. We would welcome criticism of the proposal, especially where it misreads HCL, grants a system theory unearned explanatory-reach, or assumes a form of behavioral locality that harness revisions do not support.
