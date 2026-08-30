---
description: "A claim can be true without fitting a working theory; when no fixed oracle captures that relational fit, using claims to build and revise a live system provides an initial consequence-bearing selection environment"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, evaluation]
---

# When global theory fit lacks a fixed oracle, use in building the system is an initial selection environment

A theory-mediated system is built from claims, but two different questions must
be asked about each claim:

1. **Is the claim true or otherwise warranted over its stated scope?**
2. **Does the claim fit the larger working theory well enough to improve the
   system's operation and revision?**

The first question may admit empirical checks, formal derivations, source
review, contradiction tests, or bounded benchmarks. The second is relational.
It depends on the system's objective, the other retained claims, the
representation and decomposition in use, and the decisions the theory is meant
to guide.

A true claim can be irrelevant, redundant, too weak, badly scoped, or placed at
the wrong level of abstraction. A false or overgeneral claim can appear useful
for a while because it happens to support the current implementation. Truth and
fit therefore cannot be collapsed into one test.

## Global fit has no complete fixed oracle here

For a narrow program transformation, a test suite may provide a useful selection
criterion. For an open-ended project theory, no current automatic evaluator
fully decides whether a candidate claim belongs in the larger causal picture,
which other claims it should displace, or whether its abstraction will continue
to guide coherent modification after later demands arrive.

This is not a claim that global fit is untestable. It is a claim about the form
of the available test. Fit is exposed through a distributed and delayed set of
consequences rather than one complete local oracle. These consequences include:

- whether the claim changes proposal, diagnosis, or recovery rather than merely
  being cited;
- whether predictions and derived expectations survive contact with evidence;
- whether modifications guided by it preserve the system's organization across
  later demands;
- whether it helps distinguish a bad candidate from a bad underlying theory;
- whether it reduces search, repair, or human intervention relative to rival
  formulations; and
- whether its usefulness transfers when the task or domain changes while the
  relevant structure remains.

The live system under construction can therefore serve as an **initial selection
environment**. A claim earns provisional standing not merely by sounding
coherent, but by making a counterfactual difference to building, operating, or
repairing the system and by surviving the consequences of that use.

## Use does not replace independent truth tests

"It helped build the system" is not sufficient evidence that a claim is true.
A system can reward its own misconceptions, overfit to its present architecture,
or make a claim appear indispensable because earlier design choices already
assume it.

The use test must therefore be paired with independent checks wherever they are
available and with designs that can expose self-confirmation:

- compare rival claims or theories rather than only accepting or rejecting one;
- withhold, replace, or perturb the claim and observe whether the work changes;
- record predictions before outcomes are known;
- use held-out demands and delayed operational consequences;
- distinguish evidence about the claim from evidence about the implementation
  built around it; and
- test transfer beyond the cases that shaped the current theory.

System-building evidence tests **fit and causal usefulness**. Empirical, formal,
and source evidence test **truth, validity, or warranted scope**. Neither can
silently substitute for the other.

## Computational search should begin before the global oracle is complete

The absence of a complete test for global fit does not justify postponing
computation. It determines where computational search can initially be trusted.
From the beginning, computation can be used to:

- generate competing claims, decompositions, and system designs;
- retrieve evidence and search for counterexamples;
- check local consistency, entailments, references, and formal consequences;
- construct and run bounded experiments and ablations;
- compare predictions with traces and delayed outcomes;
- identify repeated human judgments that may be made explicit; and
- search over artifacts inside regions with sufficiently discriminating tests.

The remaining global judgment can initially be human-assisted and
consequence-based. When a judgment recurs and its scope becomes clearer, the
system can operationalize it as a methodology, test, validator, learned critic,
or program. That expands the part of the search space over which computation can
propose and select changes. The bootstrap is therefore not "handcraft now,
learning later." It is an attempt to **grow the selection machinery while using
it**.

## This is a first strategy, not a uniqueness claim

The argument does not establish that explicit theory-guided bootstrapping is the
only route to a general learner. End-to-end reinforcement learning,
evolutionary search, self-play, learned world models, or future weight-updating
systems may discover globally useful organization without evaluating explicit
claims one by one.

The narrower conjecture is that explicit theories are a promising first working
state when feedback is sparse or delayed, changes preserve some causal
structure, and the evaluator cannot yet fully formalize what a coherent system
must preserve. Addressable claims may let the process use weak evidence for
more targeted search and revision. That possible sample-efficiency advantage
must be tested rather than assumed.

The strategy loses in a tested regime when system use becomes a self-sealing
criterion, when human global judgment does not fall, when every new domain needs
a bespoke theory and evaluator, when claim interventions make no causal
difference, or when a more direct computational method achieves better results
at comparable total cost.

## Scope

- The claim concerns selection among empirical and procedural claims used to
  build a system. Objectives, commitments, and grants of authority may remain
  externally supplied.
- "Initial" matters. System-building consequences are a starting selection
  environment, not a promise that human holistic judgment remains permanently
  necessary.
- No single scalar is assumed to capture global fit. A portfolio of causal,
  predictive, operational, and transfer evidence may still support increasingly
  automated selection.
- The current absence of a complete oracle is a statement about this program's
  state, not a proof that no general evaluator can exist.

## Open Questions

- Which aspects of theory fit can be operationalized now without encoding the
  current theory as the evaluator?
- What intervention best distinguishes a true but badly integrated claim from a
  false claim that happens to support the current implementation?
- Which recurring system-level judgments should be converted first into tests,
  validators, learned critics, or search objectives?
- What baselines would show that theory-guided bootstrapping uses computation
  more effectively than direct end-to-end search?

---

Relevant Notes:

- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — motivates: requires computational search where selection criteria permit it without imposing a weights-only representation
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: states the minimum machinery required for the initial environment to produce learning
- [Holding a program theory means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md) — applies: identifies the system-level consequences through which project-theory fit can become visible
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — motivates: supplies the conditional reason to try explicit theory as the first working state
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — limits: explains why the initial selection environment must eventually challenge its own representational choices
