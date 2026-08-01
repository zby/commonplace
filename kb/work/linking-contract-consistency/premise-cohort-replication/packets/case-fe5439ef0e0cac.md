# Case packet

Neutral case identifier: case-fe5439ef0e0cac

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Theory-mediated self-improvement needs both interpretation and retention from one substrate

[Theory-mediated learning may improve sample efficiency under structured shifts] is indifferent to what its theories are about. A learner retaining a theory of how a market moves or what makes a build fail gets whatever the conjecture offers. Reflective self-improvement is the case where the retained theory is about the system's own operation and participates in the [causally connected self-representation] through which the system changes its own behavior.

That case does not inherit the conjecture automatically. It inherits it under three conditions, and the third is where most substrates fail:

1. **Membership.** The theory participates in the self-representation. Explicit domain knowledge can transfer beautifully without making any improvement pathway reflective — transfer is not reflection.
2. **Interpretation.** Something inside the boundary can say what the theory claims, derive its consequences, and judge whether its reach is genuine — [reach-assessment] applied to a theory about the system itself. [Reflection buys addressability], and addressability is a handle, not a judgment.
3. **Retention with separable parts.** The theory persists as an object whose content, assumptions, and applicability conditions are separately accessible, so that a failure can rescope it rather than only delete it.

Interpretation and retention are the pair that has to come from somewhere. A system satisfying membership and retention but not interpretation revises confidently in the wrong direction; one satisfying membership and interpretation but not retention re-derives its theory every episode and cannot accumulate.

## Self-directed theories arrive unformalized

Interpretation and retention could in principle be sourced separately and composed. In practice, what a system can say about its own operation resists the move that would make composition easy.

A formal pathway gets both cheaply inside a supplied language, because [formalization buys a mechanical acceptance test] — and pays for it with a language, variables, primitives, and acceptance criteria fixed in advance.

Theories about a system's own operation are mostly not yet in such a language. "This retrieval step surfaces the wrong artifact when the query names a type rather than a topic" is a claim about the system, with real consequences and a real scope, and no formal apparatus receives it. So the mechanical acceptance test is unavailable exactly where the reflective case needs one, and condition 2 has to be discharged over natural-language.

## Only a semantic interpreter over retained text supplies both

This is why the substrate matters rather than the architecture diagram. [Purely parametric retention exposes no scope], and the documented partial routes out of that fail differently but fail alike here: neither yields a self-directed theory that persists with its applicability conditions attached. Formal retention supplies both conditions inside a language the reflective case rarely has.

An LLM operating over retained text supplies both, and does so by division of labor: the weights are the semantic interpreter, competent over natural-language theories including natural-language about the system's own behavior; the retained artifact is the persistent, separately revisable object. Neither half is sufficient. A capable model with no retained artifact re-derives its theory each session — [and a theory nothing surfaces at the moment of need contributes nothing]. A retained artifact with no interpreter is a table of rules that reasons about nothing.

So the conjecture reaches reflective self-improvement on LLM-plus-artifact substrates specifically, not on reflective systems in general. That is a claim about what is currently available, not about what is possible: any substrate that supplied semantic competence over its own unformalized self-descriptions and retained them addressably would qualify equally.

## The retention half is what scale might absorb

The bitter lesson is not an objection to theory-mediated learning, [since what scale selects against is unearned reach rather than structure]. But it does bear on the division of labor above. If a sufficiently scaled model runs the same theory search implicitly in activations, with reach-assessment and revision happening inside a forward pass, then the retained artifact is scaffolding that compensates for a context window rather than a load-bearing part of the pathway. On that reading, condition 3 is a temporary engineering fact and the externalized theory disappears.

Nothing here rebuts that. What it predicts is where to look: the artifact earns its place only where persistence across sessions, selective rescoping of a *named* theory, and inspection by a process other than the one that formed it are doing work that a longer context would not do.

## Open Questions

- Whether satisfying the three conditions without a human is enough. Structurally it is already done: [Exo] edits its own prompts, tools, and executor, rebuilds, and restarts, with the source it edits being the organization that determines its behavior — so the conditions do not need the [Gödel machine], still unimplemented, or [Commonplace], which runs but is human-inclusive. What a running instance does not settle is condition 2 at strength: Exo's acceptance oracles are build success, tests, and observed behavior after restart, which reject a change that breaks and admit one that merely reasons worse. Whether anything in such a loop is assessing reach, rather than proposing changes that fail to crash, is the open part.
- Whether the closure question was ever the interesting one. It framed the human as the thing to remove, when what the human was supplying is the evaluator — [methodological and computational closure track different changes], and a loop can close computationally while its acceptance gate gets weaker.
- Whether a deliberately minimal toy pathway, built to be reflective and computationally closed from the start and sized to test the conjecture rather than to be useful, stays autonomous end to end — or whether the human reappears at a different point, designing its objective or judging its results.
- Whether self-directed theories are harder to reach-assess than domain theories, since the system evaluating the theory is the system the theory describes, and a flattering self-theory has no external oracle to contradict it.
- Whether condition 3's separable parts can be expressed at all in natural language, or whether natural-language theories are addressable only as indivisible documents — replaceable but not rescopable — which would collapse the advantage over wholesale replacement.

---

Relevant Notes:

## Artifact B

# Formal symbolic systems assess explanatory-reach only through causal and proof obligations

[Reach-assessment] is not intrinsically an LLM-only or natural-language-only capability. A formal symbolic system can contribute to it once the candidate commitment's claimed generality has been translated into an obligation the system can check — a causal mechanism that should survive interventions or environment shifts, an identifiable causal effect under stated assumptions, or a theorem over a formally specified domain.

The shift is from asking "does this sentence sound like a good generalization?" to asking "what formal consequence must hold if this generalization is genuine?" What such a check establishes is bounded by the translation that produced it, which the last section takes up.

## The causal route

Causal theories have explanatory-reach because they do not merely fit one observed distribution. A structural causal model states mechanisms whose implications extend to interventions and counterfactuals; [causal representation learning] frames this as the difference between statistical models of one distribution and causal models that represent distributions under possible interventions.

That is the route formal reach-assessment can use: a proposed commitment is accepted not because it predicts the training cases, but because the mechanism it asserts supports the intended intervention, counterfactual, or shift claims. [Invariant prediction] tests whether candidate predictors keep their predictive relation across environments — one that holds across environments A and B but breaks once C is included is flagged as non-invariant and excluded, rather than accepted on A/B fit alone. [Causal-learn], a Python library for causal discovery, collects algorithms that infer causal structure from observational data under method-specific assumptions. [DoWhy], a causal-inference library, makes the same boundary operational by requiring declared assumptions before identification, estimation, and partial validation or refutation tests.

So a system that learns by causal theories can have reach-assessment, but the warrant is assumption-relative. It must represent the candidate theory, the target intervention or counterfactual class, the discovery or identification assumptions, and the acceptance tests that distinguish mechanism from correlation. Three pieces of apparatus recur, and they are not the same kind of thing: causal sufficiency is an assumption (no relevant common causes go unobserved among the modeled variables), latent confounding is the failure mode when it does not hold, and do-calculus is the rule system for deriving intervention effects from a supplied graph. None of them justifies the graph and variables they range over.

## The proof route

Proof is a second route. If a candidate commitment can be expressed as a theorem, invariant, type property, model-checking obligation (exhaustively checking a property over the states or transitions of a formal model), or utility comparison over a specified domain, proof search can establish explanatory-reach across that domain. The result is genuine reach-assessment inside the model: the evaluator checks the claim's quantified consequence, not just sampled cases.

[Jürgen Schmidhuber's Gödel-machine proposal] is the useful placement example — a proof-gated host architecture in which a candidate self-rewrite is accepted only when the machine proves that switching now yields higher axiomatized utility than continuing proof search, under the current axioms and utility function.

So the [Gödel machine] fits here conditionally. Were its axioms to include the relevant causal assumptions and its utility function to reward correct intervention or counterfactual generalization, the proof gate could license adopting a causal-theory learner, graph, or inference rule. Without them it supplies the acceptance rule and not the assessment.

## The formalization boundary

The formal routes move judgment upstream rather than abolishing it. A proof shows a theorem follows from axioms, not that the variables, domain, or utility function represent the original claim; causal inference gives assumption-relative warrant, not validation of causal truth from observations alone. So a theorem over the wrong variables can pass every obligation while missing the intended commitment, and an invariant relation selected from narrow environments can look stable while tracking an artifact of sampling. These are failures in the translation from the natural-language claim to the formal obligation rather than failures of proof or do-calculus, [which is why warranted autonomy is bounded by oracle domain].

The invariance case has been worked out formally. [Rosenfeld, Ravikumar, and Risteski] analyse the invariant risk minimization objective inside a Gaussian structural equation model and construct a predictor that is near-optimal under the penalized objective and near-identical to the invariant predictor on training data, yet reverts to plain empirical risk minimization once the test environment drifts far enough: the obligation is discharged and the wrong commitment is recovered. The mechanism generalizes past IRM. The penalty that construction pays scales with the mass of the region where it misbehaves, and that region is rare in training — so an acceptance criterion evaluated on the distribution that produced the candidate can price bad off-distribution behaviour at nearly nothing.

The same analysis says when the route pays. In the linear regime it establishes a threshold in the number of training environments `E` against the dimension `d_e` of the environment-varying features: above it, any feasible linear featurizer must discard those features and the invariant predictor is recovered; at or below it, a predictor using only environmental features is feasible and attains lower risk. The causal route is therefore worth taking where genuine environments are plentiful relative to the spurious-feature dimension and the model class is restricted enough for feasibility to bite. Where they are not, it returns an answer carrying no more warrant than fitting would have.

Two limits keep this from proving more than it does. The result bounds the IRM objective and close relatives, not invariance-based causal inference generally, so it leaves [invariant prediction] as used above intact: Peters and colleagues analyse a hypothesis-testing procedure with confidence bounds, while the evasion constructed here is what optimizing over a rich hypothesis class admits. And that construction is an existence proof about what the objective permits, not evidence that gradient training finds such a solution — enough to show the obligation underdetermines the commitment, not that practitioners land there.

The natural-language case remains different. A natural-language claim whose reach has not been reduced to causal or proof obligations still needs semantic judgment about what it means and where it breaks. Current LLM-mediated review appears to supply some of that judgment, and this note does not explain why. The narrower point is what stands: once explanatory-reach is represented as formal obligations, symbolic systems can assess it inside their modeled domain — and the edge of that domain is fixed by a translation they do not check.

---

Relevant Notes:

## Under-review context phrase

what a supplied formal language buys and costs
