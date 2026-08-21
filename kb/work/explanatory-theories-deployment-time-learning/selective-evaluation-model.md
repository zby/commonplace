# A provisional theory-guided selective-evaluation model

> **Status:** This is an in-progress model. It identifies the objects and uncertainties that a selective-evaluation method would need; it does not specify a settled object model, objective, numerical policy, or acceptance rule.

Selective evaluation must distinguish two cases. A check may be **mechanically inapplicable** to a candidate, or it may remain **applicable but be omitted under uncertainty**. Only the first case narrows the applicable evaluation set. The second leaves an evidence gap and changes what acceptance can honestly mean. This model separates the objects needed to reason about that difference.

This is the evidence-acquisition slice of the broader [theory-mediated improvement loop](./theory-mediated-improvement-loop.md). A theory may also guide problem diagnosis, candidate search, and selection among candidate changes. Those uses must be tested separately before their joint effect is attributed to theory mediation.

The proposal grows out of the companion [reading of Harness Continual Learning (HCL)](./hcl-reading.md). In controlled task streams, HCL revises persistent harness state and applies regression checks before accepting candidate changes. This workshop asks whether those techniques can govern changes proposed from real-world task evidence. A theory that explains relevant parts of the system's behavior might then support candidate-specific impact projections and help choose which costly evidence to acquire. Its claimed explanatory-reach must itself undergo [reach-assessment](../../notes/definitions/reach-assessment.md): an explicit theory does not by itself justify omitting evidence or show that total evaluation cost will fall.

## Levels of evaluation reasoning

The first open questions are what the system theory should represent and how its consequences become a candidate-specific impact projection. For now, the model keeps four levels of evaluation reasoning separate:

1. A **behavioral function or relation** is something the system does or must preserve, such as parsing an objective, retrieving relevant experience, choosing a legal capability, routing a workflow, or satisfying an output contract.
2. An **evaluation obligation** is a decision-relevant claim about a candidate that warrants evidence, such as “this candidate does not newly break reliable tool selection for this class of inputs.”
3. An **evaluation procedure** is a concrete process that produces evidence relevant to an obligation: rerun an anchor, execute a validator, sample repeated outputs, run a simulation, or ask a judge.
4. An **acceptance criterion** turns the observed evidence and remaining uncertainty into a commitment decision.

These levels form a chain, but they are not interchangeable. HCL supplies concrete procedures and an acceptance criterion. This extension would add a system theory and a derivation from candidate change to affected functions or obligations, followed by a mapping to procedures capable of detecting those effects. Predicting that a function may change does not identify how to observe the change. Whether the primary registry should contain theory claims and assumptions, mechanisms or invariants, functions, obligations, or a layered combination remains open.

## Working objects

A compact working model represents this chain with eight provisional objects:

- `S` is the deployed system or harness state at the decision point.
- `Omega` is the prediction boundary. It includes the relevant assumptions about fixed model parameters, runtime and outer capabilities, environment, optimizer and evaluator configuration, decoding, authority, and routing—not only mutable harness state.
- `Delta` is the candidate understood as a semantic change rather than only a textual diff. It includes the changed artifact, its path to behavioral authority, and its activation conditions. The explicit causal route can additionally represent it as `do(Delta)`.
- `tau` is the scoped, assumption-bearing working theory available to the current episode. In an ephemeral treatment, an LLM constructs it on the spot and discards it after use. In a retained treatment, the episode produces `tau` by retrieving and applying `T_n` from prior state and may propose a separately gated revision to `T_{n+1}`. The experimental `tau` is an explicit, addressable natural-language, symbolic, programmatic, or mixed artifact whose content, assumptions, and applicability conditions remain criticizable. A latent or distributed-parametric computation can inform it or serve as a no-explicit-theory baseline, but does not satisfy that observability condition by itself. Calling `tau` explanatory does not establish explanatory-reach.
- `M` maps affected functions or obligations to procedures capable of observing them. It may retrieve an existing procedure or propose an adapted or newly synthesized one.
- `pi` is an evidence-acquisition policy. Given a candidate-specific impact projection, evaluation costs, possible losses, dependencies among evaluations, and risk tolerance, it chooses which procedures are worth selecting, constructing, validating, and executing.
- `G_H` is the harness- or system-change commitment rule. It states how observed and omitted candidate-evaluation obligations bear on accepting or rejecting `Delta`.
- `G_T` is the theory commitment rule. It uses theory-specific evidence, premise tests, rival-theory discrimination, and reach-assessment to retain, revise, or reject `T_n`; candidate acceptance does not settle that decision.

The derived object `I_tau(S, Omega, Delta)` is the impact projection supported by `tau` for this system state, candidate, and boundary. It may contain mechanically established non-influence, deterministic consequences, probabilistic beliefs, or explicitly unresolved effects. It is not the working or retained theory itself: one retained theory can produce different working theories and projections for different states and candidates, and a bad activation or derivation can fail even when some part of `T_n` is sound.

Together, the episode's `tau` and the candidate produce `I_tau`; `M` identifies ways to observe the projected effects; `pi` chooses what evidence to acquire; and `G_H` determines what that evidence warrants for the candidate:

`tau + (S, Omega, Delta) -> I_tau(S, Omega, Delta) -> obligations -> M -> pi -> evidence -> G_H`

`G_H` is the harness- or system-change commitment rule; it does not decide whether to retain the theory. A separate theory decision `G_T` must judge what the evidence warrants about `tau`, retained `T_n`, and their premises or scope. A working candidate can be supported by a false explanation, while a rejected candidate can still supply evidence that improves the theory.

HCL's permitted observed historical loss remains a distinct quantity. Evaluation budget and risk tolerance need different names and semantics. “Material harmful effect” also remains undefined until a design fixes the behavior variable, direction, magnitude threshold, prediction horizon, loss units, and aggregation across obligations. Until then, `tau`, `I_tau`, `pi`, and any residual-risk condition remain schematic and cannot license omission.

## Impact-derivation routes, baselines, and applicability

The impact question concerns the consequences of a proposed change, but the working or retained theory need not be a formal causal model. Several routes can produce all or part of `I_tau`, and mixed theories may compose them:

- **Deductive structural projection** follows enforced dependencies, authority paths, types, contracts, invariants, or non-interference arguments. It can justify a hard exclusion only when the boundary, structural completeness, and execution semantics make non-influence mechanically defensible.
- **Causal projection** represents the candidate as an intervention on explicit mechanisms. It may produce deterministic consequences or probabilistic beliefs under uncertainty about routing, context assembly, interpreter response, and sampling.
- **Semantic explanatory projection** reasons over a natural-language account of intent, authority, organization, and behavior. It can cover relations that have not been formalized, but its premises, scope, and consequence derivation require semantic reach-assessment rather than inheriting warrant from fluent explanation.
- **Learned predictive projection** uses an action-conditioned world model or other learned representation. It contributes explanatory-reach only insofar as its predictions survive the intervention or structured-shift class the theory claims to cover.
- **Diff similarity** reasons from resemblance to earlier changes. It remains a non-theory baseline or auxiliary prior unless it identifies the mechanism or invariant that makes the resemblance matter: similar text can have different force depending on where it is loaded, and dissimilar edits can reach the same function.

The conservative baseline is therefore candidate-relative applicability followed by full evaluation of the applicable set. Enforced structure may prove some obligations inapplicable; where it cannot, the baseline keeps them applicable. Probabilistic evidence selection over the remaining obligations is a candidate extension, not a substitute for an incomplete dependency account.

One hypothesis worth testing is a hybrid: use enforced structure to over-approximate the possibly affected obligations, then use causal, semantic, or learned predictive routes to reason about reachable or uncertain cross-effects. Unless the relevant structure is enforced and complete, an absent declared path supports only an assumption-relative exclusion. This investigation has no evidence yet that any theory-guided route predicts better or costs less than deterministic applicability, similarity, sampling, or full-evaluation baselines.

A fixed-input output diagnosis can refine downstream obligations once an input has been assembled. It cannot replace whole-harness impact analysis when an interface or router edit changes the assembled input or context upstream. This boundary comes from [LLM output deviation requires a three-way diagnosis](../../notes/llm-output-deviation-requires-three-way-diagnosis.md); it is not yet a validated routing policy.

## Evidence selection changes what acceptance means

A design must determine candidate-relative applicability and declare its non-negotiable constraints before cost enters the evidence-selection policy. HCL's validity checks span syntax, output-schema, tool-use, task, and environment checks. Cost alone cannot make any of them inapplicable.

The evidence-selection objective also remains unsettled. Candidates include expected harmful missed loss, observer-relative value of information, and a constrained ceiling on residual risk. Where `I_tau` supplies probabilities, a numerical policy would require them to be calibrated, along with commensurable loss and cost, a stated horizon, dependencies among evaluations, and explicit risk tolerance. Deductive claims require soundness checks rather than probability calibration. When a procedure must be synthesized, its cost includes construction and validation as well as execution. Evidence can also be valuable because it changes a decision, tests or revises the working or retained theory, or calibrates `I_tau`, as [Information value is observer-relative](../../notes/information-value-is-observer-relative.md) argues.

Mechanical exclusion and uncertain omission therefore support different commitment rules:

- If enforced, complete structure proves an obligation inapplicable to the candidate, the ordinary HCL-style criterion may be applied to the candidate-relative applicable set. The resulting warrant remains conditional on the non-influence proof and its boundary.
- If an applicable obligation is omitted under uncertainty, the system cannot claim that historical-anchor loss stayed within HCL's permitted budget across every anchor. At least three honest responses remain: leave the obligation unknown and refuse the corresponding warrant, execute the check, or define a new commitment rule over observed results plus a declared residual-risk condition.

Any residual-risk estimate is conditional on `S`, `tau`, `I_tau`, `Omega`, and the observed results. **Theory error**, **activation error**, and **projection error** are separate uncertainties: a false retained premise, wrong retrieval or task-local application, dishonest scope, missing edge, invalid consequence derivation, bad probability, wrong loss model, or distribution shift can invalidate the conditional estimate. Reporting only modeled residual risk would hide the uncertainty introduced by the theory and projection used to omit evidence.

Evidence selection also changes what the system observes. A selector mostly sees the checks it chooses to run, so false negatives among omitted checks can remain hidden while an adaptive-fit account appears to have explanatory-reach. Sentinels, randomized exploration, periodic full-suite audits, or delayed monitoring could expose such misses. Unless additional structural assumptions make it unnecessary, a reach-assessment and calibration protocol must deliberately observe some checks that the selector would otherwise omit, vary load-bearing premises, and test rival explanations on unseen change families. That protocol remains to be designed.

## Where a gain is plausible—and where it is not

The locality hypothesis is most plausible when a sparse change lands in a pre-existing decomposition that matches the evaluated functions, with explicit dependencies and a small downstream impact closure. Its advantage may disappear under dense shifts, incomplete authority or routing information, or broad prompt effects. The broader explanatory-reach hypothesis is not identical to locality: a sound theory may correctly derive that a superficially small change has broad consequences and recommend a nearly full evaluation set. A revisable theory may need fewer observations when a shift preserves the mechanism or invariant it names, but an overgeneralized theory can also produce broader negative transfer. [Theory-mediated learning may improve sample efficiency under structured shifts](../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) presents this only as a conditional conjecture, not as evidence that theory-guided selection will reduce HCL evaluation work.

A lower evaluation-call count alone establishes neither a full safety warrant nor a reduction in total cost. The warrant remains bounded by the procedures actually run, any mechanically justified exclusions, and the declared residual-, projection-, and theory-risk conditions. The linked [experiment design](./experiment-design.md) compares full evaluation and non-theory schedules with several theory-guided evidence-projection routes, including a causal variant, while treating adaptive procedure generation as a separate factor.
