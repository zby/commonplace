---
description: "The production-method versus representational-form distinction answers only a narrow weights-only inference; theory-guided bootstrapping is a provisional first strategy under incomplete global evaluation, not a defense of continuing hand production"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [learning-theory, deploy-time-learning]
---

# The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal

[Sutton's Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
is the recurring observation that methods built around human knowledge tend to
lose to general search and learning methods that exploit increasing
computation. The workshop has accumulated several replies, but they answer
different questions.

Only one is needed for the **narrow form-only rebuttal**:
[production method and representational form are different
axes](./the-bitter-lesson-selects-production-methods-not-representational.md).
A theory, instruction, test, schema, or program can be produced and selected by
learning. Sutton's argument therefore does not imply that every learned result
must live in model weights.

That rebuttal establishes conceptual room for learned explicit artifacts. It
does not defend the present hand-crafted bootstrap, show that artifact learning
scales, or establish that Commonplace has found the right path.

## The bootstrap should be stated as a first strategy

The program currently has a reason to try theory-guided bootstrapping, but not a
proof that it is necessary or optimal.

A theory-mediated system must select among claims. Individual claims can often
be checked for factual truth, formal validity, local consistency, or bounded
predictive success. Those checks do not fully determine whether a claim fits a
larger working theory. Fit is relational: a true claim may be irrelevant,
redundant, badly scoped, or located at the wrong level of abstraction. A false
claim may appear useful because the current system already embodies it.

No present fixed evaluator fully decides whether a candidate claim improves the
large-scale causal picture used to build and modify the system. The first
strategy is therefore to use claims in a live system and expose them to the
consequences of building, operating, and repairing it. [When global theory fit
lacks a fixed oracle, use in building the system is an initial selection
environment](./system-use-selects-theory-fit-without-a-fixed-oracle.md).

This is not an argument for postponing computation. Candidate claims, rival
syntheses, counterexamples, local deductions, experiments, ablations, traces,
and revisions can be searched computationally from the beginning. Human
judgment remains where global fit is not yet adequately captured, but recurring
judgments should become tests, validators, learned critics, search objectives,
methods, or code. The strategy is to grow the selection machinery through use.

## What conditional compatibility requires

[A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow
it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
That is a necessary condition, not a strategic defense. The system must
increasingly acquire and revise the task- or family-specific knowledge required
for its claimed reach rather than merely apply a growing protected store of
hand-designed specializations. This condition does not require every fixed
general method or trusted component to become self-modifiable.

For each human-supplied artifact or production decision that carries
task-specific competence or an unsupported claim of reach, the program should
be able to say:

1. what computational proposal or search is already possible;
2. what evidence can currently reject candidates;
3. which judgment still requires a person and why;
4. how repeated judgments could become selection machinery;
5. what would allow any target-specific ontology, decomposition, or evaluator
   to be challenged; and
6. what alternative learning method should be used as a baseline.

The long-run criterion is **domain-extensibility**, not competence in several
predefined domains. A system with many hand-built ontologies remains a bundle of
predefined solutions. A domain-extensible process must eventually construct the
required family-specific schema or model, representations, methods, evaluators,
and checks for a new area without a person supplying that specialization either
wholesale or piecemeal.

## What the other arguments contribute

The remaining claims are useful as constraints, methods, or hypotheses. None
independently justifies the current strategy.

| Claim | Role | What it does not establish |
|---|---|---|
| [Selection removes unearned reach rather than structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) | Suggests that structure can survive when its scope is earned by refuting tests | That any current carrier or artifact layer will survive scaling |
| [Surviving absorption is a function-level question](./the-bitter-lesson-selects-production-methods-not-representational.md#why-the-form-axis-does-not-collapse-into-weights) | Explains why authority, interfaces, or checks may still be supplied somewhere | That natural-language or symbolic carriers are permanent |
| [Scaffolding can recur at a moving frontier](./scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) | Gives a conditional forecast when assigned difficulty rises with capability | That the current scaffolding is efficient or should be built manually |
| [Theory-mediated learning may improve sample efficiency](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) | Gives a reason explicit theories might help under structured shifts | That the advantage exists at system scale or beats direct search |
| [Codification and relaxing navigate the boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) | Supplies a method for hardening and retiring structure | That the method itself will become computationally produced |
| [Commitments create ground truth](./commitment-not-derivation-creates-new-ground-truth.md) and [reproduction does not transfer authority](./parametric-reproduction-cannot-replace-an-authoritative-record.md) | Explain why some governed current state remains supplied | A defense of hand-authored empirical competence |
| Use of Commonplace as an instrument | Exposes retrieval, coherence, and maintenance failures in the present decomposition | Proof that the decomposition or bootstrap strategy is right |

The absorption evidence remains a concession: functions may persist while every
current carrier disappears. The moving-frontier and sample-efficiency claims are
hypotheses. Commitments and authority explain externally supplied inputs, not a
protected semantic layer.

## Current position

The defensible position has four levels:

1. **Narrow compatibility:** the Bitter Lesson does not impose a weights-only
   representational rule.
2. **Working conjecture:** explicit theories may improve coherent search and
   revision under sparse or delayed feedback.
3. **First strategy:** use a live human-agent system as an initial selection
   environment while computational search and evaluation expand from the parts
   that already have discriminating tests.
4. **Open comparison:** test whether this route reduces human judgment,
   transfers beyond anticipated domains, and outperforms more direct learning
   approaches at comparable total cost.

Only the first level is a rebuttal. The other three are research commitments.
Calling all of them a defense would hide the main uncertainty.

## Failure conditions

The first strategy should be rejected or narrowed when:

- the system's own use rewards a self-confirming theory;
- truth checks and system-fit judgments cannot be kept distinct;
- computational search remains peripheral while human production grows;
- repeated human judgments do not become reusable selection machinery;
- every new domain requires a bespoke ontology and evaluator;
- interventions on explicit theory do not improve search, recovery, or later
  modification; or
- direct end-to-end, evolutionary, parametric, or other computational methods
  perform better at comparable total cost.

## Scope

- “Load-bearing” refers only to the narrow rejection of a form-only inference.
  It does not rank the practical importance of the other claims.
- The bootstrap is a path-relative strategy. An artifact may be learned on one
  path and hand-supplied on another.
- Objectives, commitments, and grants of authority may remain supplied; the
  scaling question concerns empirical and procedural competence.
- Fixed general learning methods, metalanguages, runtimes, exact interfaces,
  resource controls, and warranted kernels may remain. The burden falls on
  human-supplied task or family specialization and supposedly general machinery
  whose reach depends on hidden target-specific choices.
- The absence of a complete global-fit oracle is current and defeasible, not a
  proof that such an evaluator cannot be learned.

## Open Questions

- What computations can already search over theory without requiring a complete
  global evaluator?
- Which system-building consequences provide the least self-confirming evidence
  of theory fit?
- Which recurring global judgments should be operationalized first?
- What alternative first strategy gives the strongest comparison?

---

Relevant Notes:

- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: supplies the sole premise required for the narrow form-only rebuttal
- [System use is an initial selection environment when theory fit lacks a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — grounds: supplies the rationale for the first strategy without presenting it as a defense
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — grounds: states the conditional compatibility and failure burden
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: states what the strategy must progressively construct
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: keeps the initial artifact ontology inside the eventual challenge surface
- [Domain-extensible software factory](./definitions/domain-extensible-software-factory.md) — defined-in: makes the long-run reach test explicit without requiring universal self-replacement
