---
description: "Separates the narrow claim that the Bitter Lesson does not impose a weights-only rule from the provisional strategy of using live system construction to grow computational search and evaluation over explicit theories and machinery"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/when-global-theory-fit-lacks-a-fixed-oracle-use-in-building-the-system-is-an-initial-selection-environment.md
  - kb/notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
---

# The Bitter Lesson does not require everything to live in weights

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples and disputed scaling assumptions are welcome through the repository's issue tracker.

The Bitter Lesson creates a serious problem for systems built from explicit
theories, prompts, tests, schemas, and programs. Calling those artifacts a
bootstrap does not solve it. A future path toward learning is easy to promise;
the historical challenge is whether useful structure is actually found through
methods that exploit increasing computation.

This article makes one narrow rebuttal and then states a research strategy.

The rebuttal is that the Bitter Lesson does not imply that every learned result
must live in model weights. It constrains how useful structure is produced and
selected, not only how the result is represented.

The strategy is more tentative. Commonplace is trying theory-guided
bootstrapping because the global fit of a claim inside an evolving system does
not yet have a complete fixed evaluator. The live system under construction is
used as an initial selection environment, while computational proposal, local
testing, comparison, and revision begin immediately. This is the first approach
being tried, not a defense that it must be right.

## The narrow rebuttal: production method is not representation

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
describes a recurring pattern: methods built around human knowledge tend to
lose, over time, to general search and learning methods that exploit increasing
computation. Hand-designed visual features and game-playing knowledge were
useful for a time, but more general computational methods eventually found
better behavior.

The relevant contrast is the **production method**. Did designers specify the
behavior-shaping content, or did search and learning generate and select it from
evidence?

Hold representation fixed and vary production. An engineer can write one
prompt, while an optimizer generates and selects another. Both results are
natural-language artifacts, but their production differs. An expert can set one
dense controller vector, while gradient descent learns another in the same
parameterization. Both results are numerical state, but again their production
differs.

Representation still affects scaling. It determines the search space, the
available update operators, the difficulty of credit assignment, and the cost
of checking dependencies. But the Bitter Lesson alone does not establish a
weights-only rule. Programs, theories, tests, and other explicit artifacts can
in principle be products and working state of search and learning.

That is only conceptual room. It is not evidence that a large heterogeneous
artifact system can learn efficiently.

## Calling something a bootstrap is not a defense

Every learning system begins with supplied structure: objectives,
representations, algorithms, environments, or update machinery. The fact that a
component was initially hand-crafted does not settle whether it is compatible
with the Bitter Lesson. The decisive question is what useful production remains
hand-crafted as the system develops.

A bootstrap account becomes empty when it says only that present theories and
methods might someday be learned. It becomes substantive when it identifies:

- what computational search can already propose;
- what evidence can reject candidates;
- which decisions remain human and why;
- how recurring judgments can become evaluators or update machinery;
- how the current decomposition itself can be challenged; and
- which alternative learning methods provide a fair comparison.

The workshop should therefore not present bootstrapping as its successful
answer to the Bitter Lesson. The Bitter Lesson is a standing pressure on the
strategy and a source of failure conditions.

## True claims do not automatically form a useful theory

A theory-mediated learner must evaluate at least two properties of a claim.

First, is the claim true, valid, or otherwise warranted over its stated scope?
Some claims admit direct factual checks, formal derivations, consistency tests,
controlled experiments, or bounded benchmarks.

Second, does the claim fit the larger working theory and help the system act and
revise coherently? That question is relational. A true claim can be irrelevant,
redundant, badly scoped, or placed at the wrong level of abstraction. A false
claim can appear useful because the current implementation already assumes it.

No current automatic evaluator fully decides whether a candidate claim belongs
in the larger causal picture, what it should replace, or whether it will
continue to guide coherent modification after later demands arrive. This does
not make global fit untestable. It means that the evidence is distributed and
delayed rather than supplied by one complete local oracle.

A claim's fit becomes visible through consequences such as:

- whether it changes proposal, diagnosis, backtracking, or recovery;
- whether its predictions survive independent evidence;
- whether modifications guided by it preserve organization across later
  demands;
- whether replacing or withholding it changes the result;
- whether it reduces search, repair, or human intervention relative to rival
  formulations; and
- whether its useful structure transfers beyond the episode that produced it.

The live system can therefore act as an
[initial selection environment](../notes/when-global-theory-fit-lacks-a-fixed-oracle-use-in-building-the-system-is-an-initial-selection-environment.md).
Claims earn provisional standing by making a counterfactual difference to
building, operating, or repairing the system and by surviving the consequences
of that use.

System use is not a truth oracle. A self-consistent system can reinforce its own
mistakes. Independent factual and formal checks, rival theories, preregistered
predictions, ablations, held-out demands, and transfer tests are needed to keep
the selection environment from becoming self-sealing.

## Computation should enter at the beginning

The absence of a complete global evaluator does not justify handcrafting a full
theory before applying computation. It determines which parts of search can be
trusted first.

Models and programs can already be used to:

- generate competing claims, theories, decompositions, and designs;
- search sources and construct counterexamples;
- check references, local consistency, entailments, and formal consequences;
- propose experiments and run bounded evaluations;
- perform theory-withholding and theory-replacement ablations;
- analyze traces and delayed outcomes for possible credit; and
- search over artifacts inside regions with sufficiently discriminating tests.

Human judgment remains in the loop where global fit is not yet represented or
reliably evaluated. That remaining work should be treated as a description of
missing selection machinery, not as a protected source of intelligence.

When a judgment recurs and its scope stabilizes, it can be operationalized as a
methodology, test, validator, learned critic, search objective, or program. The
computationally searchable surface then grows. The intended bootstrap is not
"handcraft now, learn later." It is **learning while constructing the machinery
that makes more learning selectable**.

## Why try explicit theory first?

The positive conjecture is not that natural language is immune to absorption.
It is that explicit project theory may be useful working state when feedback is
sparse or delayed and when a new demand preserves some of the old causal
structure.

A named assumption, purpose, or scope condition can guide candidate generation,
interpret failure, and support targeted rescoping. Under a structured shift,
changing one addressable theory component may need fewer observations than
relearning behavior without an intermediate model. This is a sample-efficiency
hypothesis, not an established general advantage.

Explicit theory also imposes costs. It must be retrieved, interpreted,
maintained, reconciled, and connected to evidence. A plausible explanation can
be mistaken for a causal one. An artifact boundary can make credit assignment
worse rather than better. The conjecture earns support only when theory
interventions improve search, recovery, transfer, or revision cost after those
costs are counted.

Other first strategies remain live. End-to-end reinforcement learning,
evolutionary search, self-play, learned world models, or future weight-updating
systems may discover useful organization without evaluating explicit claims one
by one. The program should compare against them rather than claim that no other
route exists.

## The bootstrap must be able to outgrow itself

The hand-designed vision and game-playing approaches in Sutton's comparison
encoded object-level competence for predefined problem classes. Their
computation operated inside features, heuristics, and decompositions that the
method did not learn to replace.

Commonplace differs only if its present theories, methods, validators, schemas,
programs, artifact types, routing, and evaluators remain challengeable.
Editable files are not enough. An agent may rewrite a prompt while every
important decision about what may change and how it is judged remains fixed
human design.

The long-run criterion is **domain-extensibility**, not competence in several
predefined domains. A system with ten hand-built ontologies and ten special
update procedures is still a bundle of predefined solutions. A
domain-extensible process must eventually construct the project-specific
theory, representations, methods, and checks needed for a new area without a
person first supplying another complete domain model.

This does not require the system to derive its own values. Objectives,
commitments, and grants of authority can remain supplied. The scaling question
concerns production of empirical and procedural competence.

No current carrier is promised survival. A future model may absorb a theory,
collapse a representational boundary, or replace a validator with a cheaper
learned mechanism. The bootstrap succeeds by improving the production path, not
by preserving today's files.

## What Commonplace currently establishes

Commonplace is a live human-agent environment for trying the strategy. A model
can work across natural-language and symbolic artifacts. Project theory can be
retained and routed into later work. Stable conclusions can become
instructions, validators, schemas, or code. Failures can lead to revisions in
both the knowledge base and some of its machinery.

This is useful, but it is not yet a general learner. People still choose
objectives, identify many reusable claims, judge much of their global fit,
assign blame, choose representations, construct or approve evaluators,
authorize consequential changes, and repair failures beyond represented
coverage.

The current position therefore has four levels:

1. The Bitter Lesson does not impose a weights-only representational rule.
2. Theory-mediated learning is a serious conjecture worth testing.
3. Theory-guided construction of a live system is the first strategy for
   bootstrapping the missing selection machinery.
4. Whether that strategy becomes scalable, reduces human judgment, transfers
   beyond anticipated domains, and beats more direct alternatives remains open.

Only the first level is a rebuttal. The others are research commitments.

## Tests that can change the strategy

The immediate experiment should test whether prepared project theory is actually
load-bearing. Hold model, tools, repository state, budget, and acceptance fixed;
compare correct theory, an information-matched record without theory-level
organization, theory withheld, and plausible but wrong theory over sequential
programming demands with delayed consequences.

Measure candidate generation, preservation of architectural commitments,
diagnosis, backtracking, recovery, collateral regressions, later-demand
performance, and human intervention. Correct theory should help most where the
later demand preserves the structure it names. Wrong theory should produce
predictable negative transfer. Withholding theory should particularly damage
recovery if the conjecture is right.

A later experiment must test the bootstrap strategy itself. Introduce a domain
that was not used to design the artifact ontology or improvement procedure.
Track which claims, methods, checks, and evaluator components are produced by
computational search; which judgments remain human; whether repeated judgments
become reusable machinery; and whether the process transfers again without a
new bespoke architecture.

The strategy loses in a tested regime when system use becomes self-confirming,
computational search remains peripheral, human judgment grows with the corpus,
each domain needs a new ontology and oracle, the decomposition remains outside
revision, or a more direct method performs better at comparable total cost.

## The research program, not the defense

The Bitter Lesson does not require everything to live in weights. It does
require useful complexity to be earned through methods that exploit search,
learning, evidence, and computation rather than protected as designer
knowledge.

That requirement does not vindicate Commonplace. It tells us how to judge it.
The project is testing whether a live, theory-guided human-agent system can grow
its own selection machinery: beginning with computational proposal and local
checks, using system-building consequences where global fit lacks a fixed
oracle, and progressively converting recurring judgments into evaluators,
methods, and code.

This is a first construction strategy. It should be retained only while it helps
build a more general learning process than the one that produced it.

The [bootstrap note](../notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md)
states the conditional compatibility and failure criteria. The
[response-portfolio note](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md)
separates the narrow rebuttal from the broader research commitments.
