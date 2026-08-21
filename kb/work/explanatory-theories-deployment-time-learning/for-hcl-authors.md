# An invitation to the HCL authors

> **Status:** This is an exploratory response from the Commonplace project. It asks whether techniques tested by Harness Continual Learning in controlled task streams could help a deployed system learn from real-world tasks. That transfer is our proposal, not a claim made or tested in the HCL paper. We have not contacted the authors, and no response or endorsement is implied.

## Why HCL matters to this workshop

Our [source analysis of HCL](../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) reads it as making a consequential system boundary explicit under controlled conditions: persistent harness state around frozen model weights can itself become a sequential learning object. An optimizer proposes a revised harness, an evaluator can reject it, and historical retention is an explicit condition of commitment.

Our thesis is a transfer claim. We want evidence from real-world task execution—outcomes, feedback, failures, and later consequences—to train the deployed system by driving proposals and selection over retained harness state. We call that target setting **deployment-time learning**. HCL's isolated candidates, retention checks, validity checks, and atomic commitment offer techniques for governing those behavior-changing writes. We do not classify HCL's controlled experiments themselves as deployment-time learning or treat them as evidence that the transfer succeeds.

HCL's evaluator requires current-task improvement, historical retention, and validity. Historical loss counts sampled anchors that the incumbent solves and the candidate newly fails. Even when the permitted loss is zero, the guarantee therefore applies to that finite sample rather than to every possible behavior. HCL's textual budget sweep also illustrates how proposal–historical-anchor checks can grow with task history, although the paper does not report a production cost or show that the approach is infeasible.

This combination motivates our question: could an explicit theory of system behavior with genuine [explanatory-reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) improve the search for harness changes, selection among candidates, and acquisition of costly evidence? Would retaining and revising that theory help later episodes more than reconstructing one on the spot?

## The proposed extension

HCL already asks a frozen LLM to move from execution evidence to a candidate harness edit: it analyzes the outcome and context, identifies components to revise, and generates alternatives. The paper does not expose an explicit system theory between those objects. Its Abstract Memory retains scoped guidance, but the experiments do not establish that guidance as an explanatory theory or show that candidate search consumes it as one.

Our extension inserts an explicit, criticizable working theory `tau_n` between evidence and action. It can diagnose the failure, identify an intervention locus, generate and prioritize candidate changes, and predict their intended gains. For system state `S` and candidate `Delta` under prediction boundary `Omega`, it can also derive `I_tau(S, Omega, Delta)`: claims or beliefs about which behavioral functions and evaluation obligations may change. A mapping connects those obligations to procedures capable of observing them, and an evidence-acquisition policy decides which procedures are worth selecting, constructing, validating, and running.

In the first treatment, the LLM constructs `tau_n` on the spot and the experiment records it before candidate generation or evidence selection. This tests whether an explicit intermediate theory helps within one episode. A separate lifecycle treatment begins with a retained `T_n`, checks that later calls retrieve and instantiate it as the episode's working `tau_n`, and applies an independent gate to any proposed `T_{n+1}`. A harness edit can work for the wrong stated reason, so harness acceptance cannot double as theory acceptance.

Causal reasoning is an important special case because the question concerns the consequences of a proposed change. It is not the umbrella theory class, and causal vocabulary does not establish explanatory-reach. Structural proofs, compositional models, semantic explanations, and learned predictors can support other parts of the projection. Their claimed explanatory-reach must likewise survive withheld effects, premise changes, and rival explanations rather than only fit earlier diffs.

The working path is:

`evidence + system state -> working theory -> candidate search and prioritization -> benefit and impact projections -> select or generate evidence -> candidate decision`

`outcomes and audits -> theory assessment -> retain, revise, or reject the theory`

This does not treat HCL's four mutable harness parts as a validated explanatory decomposition or causal graph. They are an engineering partition. A theory can improve search if it supplies useful guidance within or beyond the predefined component order, and local evaluation becomes plausible only when a candidate is sparse in a matching decomposition, dependencies and authority paths are explicit, and its downstream impact closure is small. The theory's claimed explanatory-reach is a claim for audits to test, not a premise granted by naming it.

[SPADE](../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) suggests a further experimental factor: the policy might adapt or synthesize an executable evaluation procedure rather than only select a stored anchor. [A separate invitation to the SPADE authors](./for-spade-authors.md) develops that bridge.

## What selective evaluation would change

Selective evaluation cannot retain HCL's full-set acceptance semantics unchanged. If only some anchors are run, the system cannot make an unqualified claim about losses over all anchors. It must leave omitted obligations unknown, still execute the full check, or define a different gate over observed evidence plus a declared residual-risk condition.

The third option introduces theory and projection error as well as modeled residual risk. A false premise, wrong boundary, missing dependency, invalid derivation, bad probability, wrong loss model, or distribution shift could invalidate the reason for omitting evidence. The selector also observes mostly the checks it chooses to run, so harmful effects among omitted checks can remain hidden. Randomized exploration, always-run sentinels, periodic full-suite audits, delayed monitoring, and projections recorded before evidence selection are possible controls, but none is validated here.

## A discriminating experiment

The first comparison would isolate candidate search: hold the task evidence, model, candidate budget, and full evaluator fixed, then compare direct evidence-to-candidate proposal inspired by HCL, proposal after constructing a fresh working theory, and proposal after instantiating a working theory from a retained theory. Evaluator-only anchors and outcomes would remain hidden until candidate generation and pre-evidence prioritization were frozen. A second comparison would use a fixed candidate pool and fixed evidence to test theory-guided candidate choice. A third would hold candidates and the commitment rule fixed while comparing full registered-set evaluation, budget-matched sampling, diff similarity, deterministic structure, explicit causal models, and mixed explanatory-theory selection. Only then would an end-to-end phase combine the roles or add SPADE-inspired procedure generation.

The comparisons would measure viable candidates found per proposal and dollar, best candidate within budget, proposal diversity, candidate-selection regret, current gains, full-suite regressions, evaluator cost, harmful misses, detection coverage, projection calibration or deductive soundness, held-out retention, and later surprises. A repeated stream would compare matched raw history without an explicit theory, a fresh theory reconstructed each episode, a working theory instantiated from a frozen retained theory, and a working theory instantiated from a separately gated revisable theory. Generated procedures would add construction, validity-filtering, containment, execution, and reuse costs.

## Questions for the HCL authors

Your view would be especially useful on these questions:

- Which parts of HCL's optimizer–evaluator–commitment loop do you expect to transfer from controlled task streams to evidence generated by real-world tasks, and what would break first?
- What are the measured evaluator costs, and how do they scale with anchors, candidates, and stream length?
- How local do you expect the behavioral effects of typical harness candidates to be?
- Does the optimizer currently produce or consume any explicit rationale, diagnosis, or self-model that is not visible in the paper's harness state? If so, is it retained across interactions?
- What explanations do you already rely on when anticipating the effects of harness changes, and what candidate change would falsify them?
- Which influence or non-influence claims, if any, could be defended through causal mechanisms, dependency or authority structure, invariants or proofs, compositional program structure, semantic contracts, or learned prediction?
- Could the historical evaluation surface itself be adapted or generated for each candidate, rather than only accumulated as fixed anchors, and what would keep that generator from overfitting the gate?
- How might omitted checks be audited well enough to reveal harmful misses and calibrate impact projections?
- Which model, runtime, outer-capability, evaluator, or environment boundaries held fixed in HCL would you treat as revisable in a broader system?

These questions arise from the proposed extension. They are not claims that the HCL paper was obliged to answer.

The [full explanatory-theories and deployment-time-learning workshop](./README.md) develops the HCL reading, the coupled theory- and harness-change loops, the on-the-spot versus retained-theory distinction, changed acceptance semantics, adaptive procedure-generation option, reach-assessment and audit problems, and staged experimental comparison. We would welcome criticism of the proposal, especially where it misreads HCL, grants a system theory unearned explanatory-reach, or assumes a form of behavioral locality that harness revisions do not support.
