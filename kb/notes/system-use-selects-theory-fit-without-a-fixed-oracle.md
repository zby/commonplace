---
description: "A claim can be true without fitting a working theory; the current human-agent loop already uses computation guided by retained knowledge, while live system use supplies an initial selection environment for global fit"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, evaluation]
---

# System use is an initial selection environment when theory fit lacks a fixed oracle

The current Commonplace loop is already computational. A language model reads
retained project artifacts, searches and synthesizes candidate claims and
changes, compares formulations, and writes accepted revisions back into the
knowledge base. The operator currently supplies much of the high-level selection
signal about whether a claim fits the larger theory and intended system.

The missing capability is therefore not computation in general. It is a more
reusable, discriminating, and increasingly computational way to select global
theory fit and assign credit when consequences are distributed or delayed.

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

## The current loop is computational theory-guided search

The absence of a complete global-fit oracle does not confine computation to
narrow regions with formal tests. Computation already carries much of the wider
search:

- language models retrieve and interpret retained project knowledge;
- they generate competing claims, decompositions, explanations, and system
  designs;
- they search for evidence and counterexamples;
- they compare formulations and identify contradictions or missing distinctions;
- they propose experiments, ablations, and repository changes;
- programs and tools check local consequences, references, tests, and traces;
  and
- accepted revisions become inputs to later computational work.

The [2026-08-30 Commonplace revision record](./evidence/commonplace-revision-used-theory-guided-computational-search.md)
is a concrete example. The model read many Commonplace artifacts, synthesized a
review and candidate revisions, received sparse operator corrections about the
Bitter Lesson framing, revised the theory and repository, and then used the
revised state in later turns.

At the boundary that includes the operator, model, knowledge base, and tools,
this is a human-inclusive theory-mediated learning loop. At a boundary excluding
the operator, global-fit selection and final acceptance remain exogenous. The
important unresolved transition is therefore from **computational search with
human-assisted high-level selection** toward a process in which more of that
selection and credit assignment is supplied by reusable computational machinery.

Reading the artifacts and citing them is strong mediation evidence, but it does
not quantify how load-bearing they were. A matched run with the artifacts
withheld, replaced, or reduced to an information-matched record would provide a
stronger causal estimate.

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

## The bootstrap grows selection machinery, not computation from zero

The bootstrap should not be described as "handcraft now, add computation
later." Computation is already present in retrieval, interpretation, proposal,
criticism, comparison, editing, testing, and retention. The present bottleneck is
that the operator still supplies many sparse, project-level judgments for which
no sufficiently discriminating reusable evaluator exists.

Those judgments should be treated as evidence about missing selection machinery.
When one recurs and its scope becomes clearer, the system can operationalize it
as a methodology, test, validator, learned critic, search objective, episode
schema, or program. That expands the part of the loop over which computation can
both propose and select changes.

The relevant progress measure is not whether computation appears in the loop.
It is whether:

- additional computation improves proposal, criticism, comparison, and recovery;
- retained theory improves that computation relative to appropriate controls;
- recurring operator corrections are captured and reused;
- the marginal human judgment required per useful revision falls; and
- the resulting machinery transfers beyond the cases and domains that produced
  it.

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
criterion, when retained theory makes no causal difference, when additional
computation does not improve search or selection, when human global judgment
does not fall, when every new domain needs a bespoke theory and evaluator, or
when a more direct computational method achieves better results at comparable
total cost.

## Scope

- The claim concerns selection among empirical and procedural claims used to
  build a system. Objectives, commitments, and grants of authority may remain
  externally supplied.
- "Initial" matters. System-building consequences are a starting selection
  environment, not a promise that human holistic judgment remains permanently
  necessary.
- The current loop is already computational. "Bootstrap" names the effort to
  improve the search-and-selection process and extend its revision surface, not
  a pre-computational phase.
- No single scalar is assumed to capture global fit. A portfolio of causal,
  predictive, operational, and transfer evidence may still support increasingly
  automated selection.
- The current absence of a complete oracle is a statement about this program's
  state, not a proof that no general evaluator can exist.

## Open Questions

- Which aspects of theory fit can be operationalized now without encoding the
  current theory as the evaluator?
- What intervention best measures how much retained Commonplace knowledge changes
  LLM search relative to an information-matched record?
- Which recurring system-level judgments should be converted first into tests,
  validators, learned critics, or search objectives?
- How should inference-time compute, tool use, human correction, and retained
  artifacts be accounted for in an end-to-end comparison?
- What baselines would show that theory-guided bootstrapping uses increasing
  computation more effectively than direct end-to-end search?

---

Relevant Notes:

- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: requires computational search where selection criteria permit it without imposing a weights-only representation
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: states the minimum machinery required for the initial environment to produce learning
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — grounds: identifies the system-level consequences through which project-theory fit can become visible
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — grounds: supplies the conditional reason to try explicit theory as the first working state
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why the initial selection environment must eventually challenge its own representational choices
- [Choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — contrasts: separates candidate validity from system-relative promotion value, a neighbouring decomposition that should not be conflated with truth versus global theory fit
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — grounds: bounds what successful use of one whole configuration can warrant about its theory beyond the context that produced it
- [Weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — mechanism: explains why selection enriches locally checkable qualities more strongly than global coherence when their operative oracles discriminate unequally
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — extends: develops recurring operator corrections into maintained checks that improve later selection within calibrated domains
