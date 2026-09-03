---
description: "A hand-crafted starting state fits the Bitter Lesson only if scalable learning displaces the task- and family-specific production knowledge it supplies as claimed reach widens"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning, foundations]
---

# A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it

The title states a **compatibility condition**: a hand-crafted starting state
fits the Bitter Lesson only if computation acquires the required task- or
family-specific production knowledge from permitted evidence rather than
requiring people to construct it for every new demand. *Family-specific* here
means specific to a class of related demands — a demand class — not to a single
task. The condition is not a defense of hand-crafted bootstrapping and not a
claim that this is the only way to build a general learner.

[The Bitter Lesson selects production methods rather than representational
forms](./the-bitter-lesson-selects-production-methods-not-representational.md).
It therefore does not rule out theories, instructions, tests, schemas, or
programs that are themselves produced and selected through learning. That
blocks a categorical weights-only objection. It does not show that starting by
constructing those artifacts manually is the right scaling strategy.

Calling present artifacts a bootstrap cannot answer the Bitter Lesson by itself.
A promised path beyond hand-crafting is cheap. The strategy must either show that
search and evidence progressively take over useful production or concede that a
more direct computational method is better.

## A bootstrap can seed the process that outgrows its starting knowledge

What makes the condition satisfiable is the difference between a bootstrap and
a scaffold. A scaffold is discarded once the product stands; a prototype is
thrown away and rebuilt. A bootstrap is the running system itself, using its
current theory and machinery to guide the search that produces later versions.
The task- or family-specific production knowledge it starts with can therefore
be displaced while the system persists. Complete self-replacement is neither
the mechanism nor the criterion: fixed general machinery may continue when its
scope and warrant support the reach being claimed, since [machinery persists
by warrant rather than by position in a reflective
loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
Which components those are is stated below.

The hand-designed features in Richard Sutton's examples were neither: they
were built as the solution, and the method never learned to replace them.
Bootstrap content
is compatible only when it does not remain an expanding source of target
competence. For a declared reach, the compatibility condition therefore becomes
a prediction: computation will acquire the required task- or family-specific
knowledge from permitted evidence rather than requiring people to construct it
for every new demand. The failure conditions below are what would refute that
prediction.

## The Bitter Lesson creates immediate pressure to use computation

If theory-mediated learning is a sound conjecture, the lesson still recommends
using computation as early as possible to search over theories, methods,
programs, and evaluation machinery. It gives no reason to complete a
hand-designed theory first and automate it afterward.

The practical limitation is selection. Computational proposal is already easy:
a model can generate many candidate claims and architectures. Learning requires
a test that discriminates among them. Some parts of the problem have such tests:
formal consequences, factual evidence, local consistency, program tests,
bounded benchmarks, and later operational outcomes. Other parts do not yet have
a complete fixed oracle.

In particular, a claim can be true without fitting the larger working theory.
It can be irrelevant, redundant, badly scoped, or placed at the wrong level of
abstraction. Conversely, a false claim can appear useful because the current
implementation already assumes it. [When global theory fit lacks a fixed oracle,
use in building the system is an initial selection
environment](./system-use-selects-theory-fit-without-a-fixed-oracle.md).

This evaluator gap is a reason for the first strategy, not an exemption from the
lesson.

## The first strategy is to grow the selection environment through use

Commonplace begins with a live human-agent system rather than a theory written in
isolation. Claims are retained, interpreted, and used to make concrete design,
repair, and evaluation decisions. Their fit can then be exposed through
consequences such as:

- whether they change proposal, diagnosis, backtracking, or recovery;
- whether their predictions survive later evidence;
- whether changes guided by them preserve organization across later demands;
- whether rival or ablated theories produce worse decisions;
- whether they reduce repair and human intervention; and
- whether their useful structure transfers beyond the episode that produced
  them.

These are imperfect, distributed, and delayed signals. They are nevertheless
more discriminating than judging the theory only as prose. They turn the system
under construction into an initial environment for selecting which claims and
methods deserve to persist.

The strategy must use computation inside this loop immediately. Candidate
claims, rival syntheses, counterexamples, local derivations, experiments,
ablations, trace analysis, and bounded artifact revisions can all be generated
or searched computationally now. Human judgment remains where global fit is not
yet captured well enough, but it should be recorded as missing selection
machinery rather than treated as the permanent solution.

When a judgment recurs and its scope stabilizes, it can become a methodology,
test, validator, learned critic, search objective, or program. That expands the
surface on which computational proposal and selection can operate. The
bootstrap is therefore not "handcraft now, learn later." It is an attempt to
**learn while constructing the machinery that makes more learning selectable**.

## Compatibility still requires outgrowing the starting structure

The hand-designed vision and game-playing approaches in Sutton's comparison put
designer knowledge into the intended object-level solution for a predefined
problem class. Their computation operated inside features, heuristics, and
decompositions that the method did not learn to replace.

The present strategy differs only if the theories, schemas, representations,
methods, evaluators, and decomposition choices that carry required task- or
family-specific competence can be computationally acquired or challenged.
Editable files are not enough. A model may rewrite a prompt while every
important target-specific choice about what may change and how it is judged
remains fixed human design.

The long-run criterion is whether learning can acquire the family-specific
production knowledge required as claimed reach widens, not competence in several
predefined domains. A system with ten hand-built ontologies and ten specialized
update procedures is still a bundle of predefined solutions. The stronger
process constructs the required family schema or model, representations,
methods, evaluators, and checks for a new area without a person supplying that
knowledge either wholesale or piecemeal.

This criterion does not require the system to invent its own objective.
Objectives, commitments, and grants of authority may remain supplied. The claim
concerns how required empirical and procedural knowledge is produced and revised
in pursuit of them. Nor does it require every general algorithm, metalanguage,
runtime, or trusted kernel to modify itself. Whether supposedly general
machinery hides target-specific assumptions is an empirical scope question.

## This is not a uniqueness claim

End-to-end reinforcement learning, evolutionary search, self-play, learned world
models, or future weight-updating systems may discover useful global
organization without selecting explicit claims one at a time. The strategy does
not yet have grounds to say that theory-guided bootstrapping is necessary.

It is the first approach being tried because explicit claims may provide
addressable working state when feedback is sparse or delayed and when later
changes preserve some causal structure. They may support more targeted search,
diagnosis, and rescoping than undifferentiated behavioral adaptation. That is a
conditional sample-efficiency conjecture, not a settled advantage.

The appropriate comparison is therefore strategic rather than defensive:

- Does theory-guided construction make better use of available computation than
  direct search under the same total budget?
- Does human construction of required task-specific knowledge fall as the
  claimed demand class widens?
- Do recurrent judgments become operational selection machinery?
- Does the process transfer beyond domains and decompositions anticipated by its
  designers?

## Failure conditions

The strategy loses in a tested regime when:

- system use becomes a self-confirming test of the theory already embodied in
  the system;
- claims remain artisanal and computational search stays peripheral;
- each new domain requires a bespoke ontology and evaluator;
- human global judgment and maintenance grow with the corpus;
- task-specific decomposition or evaluation choices remain human supplied while
  the system claims reach beyond them;
- interventions on retained theory make no causal difference; or
- a more direct learning method achieves better results at comparable total
  cost.

Current Commonplace evidence supports a useful human-assisted environment for
trying this strategy. It does not establish a scalable learning method with
broad production reach or show that the strategy is better than its
alternatives.

## Scope

- Conditional compatibility belongs to a declared production path, not to an
  artifact class or a stated intention.
- The current absence of a complete global-fit oracle does not imply that one
  cannot be learned or constructed.
- System-building consequences test fit and causal usefulness; they do not
  replace independent truth, validity, or scope checks.
- No current carrier is promised survival. Learned functions may migrate into
  weights, code, other artifacts, or future substrates.
- A fixed component may remain justified because it implements a general method
  over the declared reach, because changing it is outside the objective, or
  because revision is unsafe or uneconomic. Its fixedness must not be
  misreported as learned, and hidden task knowledge must not be misreported as
  general machinery.

## Open Questions

- Which aspects of global theory fit can already be operationalized without
  encoding the present theory into the evaluator?
- Which recurring human judgments should become the first learned or programmed
  selection machinery?
- What baseline best compares theory-guided construction with direct
  computational search?
- What sequence of tasks or domains would distinguish acquired production reach
  from a broad but predefined ontology?

---

Relevant Notes:

- [System use is an initial selection environment when theory fit lacks a fixed oracle](./system-use-selects-theory-fit-without-a-fixed-oracle.md) — grounds: explains why live system construction is the first selection environment rather than a defense of manual production
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: supplies the narrow compatibility argument while preserving the scaling burden
- [Machinery persists by warrant, not position in a reflective loop](./machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — extends: applies the production requirement recursively to the selection machinery
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — mechanism: states the minimum loop that turns proposals into retained learning
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — grounds: explains why editable object-level artifacts do not establish general learning
- [Theory-mediated learning may improve sample efficiency under structured shifts](./theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — grounds: supplies the conditional reason to try explicit theory as working state
- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](./evidence/commonplace-revision-used-theory-guided-computational-search.md) — evidenced-by: bounds the current human-assisted case, where retained theory guided computational search but operator selection and missing ablation prevent a scalable-outgrowth conclusion
- [Open-ended improvement must allocate search before decisive evaluation is available](./open-ended-improvement-allocates-search-before-evaluation.md) — grounds: explains why computational search allocation must begin before global-fit evidence can license adoption
- [A repeatable operative path keeps a redesign class open to revision](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — extends: turns the requirement that starting machinery remain challengeable into a causal test for whether a redesign class stays revisable after one transition
- [Broad software demands create pressure for agentic factory development](./broad-software-demands-create-pressure-for-agentic-factory-development.md) — extends: states the acquisition and reach burden without a premature domain-extensibility definition
