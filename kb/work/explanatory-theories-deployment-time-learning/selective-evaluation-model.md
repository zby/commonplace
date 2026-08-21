# Theory-mediated selective evaluation

> **Status:** Working model. This note explains how a working theory could guide which evaluation evidence to acquire for one candidate change. It does not provide a validated selection policy or a safety guarantee. The comparisons are in the [experiment design](./experiment-design.md).

Running every available evaluation after every change may be too expensive. The proposed alternative uses a working theory to predict which parts of the system a candidate can affect, then acquires evidence where the predicted effects justify its cost. The theory may instead conclude that the candidate has broad effects and recommend nearly the full evaluation set. Selectivity may result from the reasoning; it is not itself the objective.

This is one role in the broader [theory-mediated improvement loop](./theory-mediated-improvement-loop.md). The central question here is narrower: how does a theory yield a candidate-specific evidence choice, and what can acceptance honestly claim when some evidence is not acquired?

## From change to evidence

Four levels must remain distinct. A **behavioral function or relation** is something the system does or must preserve. An **evaluation obligation** is a decision-relevant claim about the candidate, such as “this change does not impair tool selection for these inputs.” An **evaluation procedure** produces evidence relevant to an obligation. A **commitment rule** determines whether the resulting evidence and unresolved uncertainty warrant accepting the candidate.

Predicting that a function may change does not by itself identify a valid way to observe that change. One obligation may have several procedures, and one procedure may bear on several obligations.

Let `S` be the current system state, `Omega` the assumptions that bound the prediction, `Delta` the candidate understood as a semantic change rather than merely a text diff, and `tau` the working theory. The candidate-specific impact projection

`I_tau(S, Omega, Delta)`

states which obligations may be affected, which appear unaffected and on what grounds, and which remain unresolved. It is derived from the theory but is not the theory itself: the same theory can yield different projections for different candidates, and a sound theory can still be misapplied.

The reasoning chain is:

```text
working theory tau + (system S, boundary Omega, candidate Delta)
    → impact projection I_tau over evaluation obligations
    → map relevant obligations to valid procedures
    → choose procedures based on cost, possible harm, and risk tolerance
    → observed evidence + unresolved obligations
    → bounded candidate decision
```

These are stages of reasoning, not a required storage schema.

## Not running a check has different meanings

Before commitment, selective evaluation records how each obligation was handled:

1. **Shown irrelevant.** The obligation does not apply to this candidate within a soundly established boundary.
2. **Discharged without its usual procedure.** A proof, enforced invariant, or stronger substitute evidence establishes the obligation.
3. **Tested.** A valid procedure is executed and produces usable evidence about the obligation.
4. **Left unresolved.** The obligation remains applicable, but the policy omits it under uncertainty.

Only the fourth case creates an evidence gap by omission. A test may still yield uncertain evidence, but that is measurement uncertainty rather than an unobserved obligation. Cost cannot make an obligation irrelevant or establish that it is satisfied. It can influence whether to acquire evidence or accept a declared residual risk.

This distinction also keeps “check” and “obligation” from collapsing into one object. Not running a familiar check may be justified when another route discharges its obligation. Conversely, executing a procedure does not discharge anything if that procedure cannot observe the claimed effect.

## What can support an impact projection

A projection may draw on enforced dependency and authority paths, formal causal models, invariants or proofs, semantic explanations, and learned action-conditioned predictions. Causal theory is one route, not the umbrella.

A hard exclusion requires sound entailment within a boundary whose relevant structure is complete. An absent edge in an incomplete dependency map supports only an assumption-relative omission, not a hard exclusion. Semantic or probabilistic projections can support risk-aware prioritization, but fluency or confidence does not prove non-influence. The theory's claimed scope therefore remains subject to [reach-assessment](../../notes/definitions/reach-assessment.md). Diff similarity is a useful baseline or prior; it becomes theory-like only when it identifies why the resemblance should preserve consequences.

## Acceptance and blind spots

The evidence policy should consider evaluation cost, possible loss if a harmful effect is missed, procedure validity, and risk tolerance. At its simplest, it acquires evidence when the expected loss from leaving an obligation unresolved exceeds the cost of obtaining reliable evidence. Hard constraints and non-negotiable obligations must be declared before this tradeoff.

Passing the selected procedures supports only the obligations those procedures validly assess, together with any obligations discharged by sound reasoning. If an applicable obligation remains unresolved, the system can acquire more evidence, reject the candidate, or accept it under an explicit residual-risk rule. It cannot honestly report the omitted obligation as passed.

Any residual-risk claim is conditional on the whole chain. **Theory error** can start from a false premise. **Application error** can retrieve or apply the wrong theory. **Projection error** can derive the wrong consequences. **Measurement error** can map an obligation to an invalid procedure or rely on an unreliable executor or judge. Reporting only the modeled risk hides these additional ways the omission can fail.

Selection also biases what the system learns about its selector. If it observes results mostly for the checks it predicted would matter, misses outside that surface remain hidden. For uncertainty-based omissions, independent audits must therefore sample obligations the policy would omit. Those audits test the impact projection and selection policy; a pass on self-selected evidence does not establish the theory's explanatory-reach.

## Claim to test

The useful claim is not that theory always reduces the number of evaluations. It is that theory-guided selection may lower the **total cost of reaching a candidate decision** while staying within a declared harmful-miss or residual-risk bound. Total cost includes constructing and checking the theory, mapping obligations to procedures, synthesizing and validating new procedures when needed, executing them, and auditing omitted regions.

This gain is most plausible when a change has bounded consequences that the theory represents correctly. A good theory may instead reveal broad impact and eliminate the expected saving; a bad theory may save calls by hiding regressions. The [experiment design](./experiment-design.md) turns these possibilities into comparisons with full evaluation and non-theory baselines.
