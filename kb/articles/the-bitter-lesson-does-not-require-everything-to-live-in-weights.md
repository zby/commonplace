---
description: "Separates the Bitter Lesson's production-method claim from a weights-only rule and locates the scaling burden in computational production of task-specific specialization"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
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

But describing Commonplace as handcrafting a theory before computation begins
would also be wrong. The present process already uses a language model and tools
to retrieve project knowledge, search over candidate formulations and system
changes, criticize alternatives, run checks, and retain revisions. The operator
currently supplies much of the sparse high-level selection signal about whether
a claim fits the larger theory and intended system.

This article therefore makes one narrow rebuttal and then states a research
strategy.

The rebuttal is that the Bitter Lesson does not imply that every learned result
must live in model weights. It constrains how useful structure is produced and
selected, not only how the result is represented.

The strategy is more tentative. Commonplace uses a computationally assisted,
theory-guided human-agent loop as a live selection environment because the
global fit of a claim inside an evolving system does not yet have a complete
fixed evaluator. The immediate task is to make its computational search more
effective and to turn recurring operator judgments into reusable learning and
credit-assignment machinery. This is the first approach being tried, not a
defense that it must be right.

## The narrow rebuttal: production method is not representation

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
describes a recurring pattern: methods built around human knowledge tend to
lose, over time, to general search and learning methods that exploit increasing
computation. Hand-designed visual features and game-playing knowledge were
useful for a time, but more general computational methods eventually found
better behavior.

The relevant contrast is the **production method**. Did designers supply the
task-specific, behavior-shaping content, or did a computational learning method
determine and retain it from evidence? Generating and selecting candidates is
one such method; direct evidence-responsive updates are another.

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

- what computational evidence-to-update determination already occurs;
- where a path exposes rejectable candidates, what proposes and rejects them;
- which update, evaluation, selection, and credit judgments remain human and
  why;
- how recurring judgments can become evaluators or update machinery;
- how target-specific decomposition choices can be challenged as claimed reach
  widens;
- whether additional computation improves useful learning rather than merely
  producing more activity or candidates; and
- which alternative learning methods provide a fair comparison.

The project's answer to the Bitter Lesson is therefore not the label but the
prediction the label commits it to, and which it can be held to: computation
will acquire the task-specific specialization required as claimed reach widens
instead of requiring people to construct it anew. Fixed general
learning machinery may persist. The Bitter Lesson is a standing pressure on
that prediction and the source of its failure conditions.

## True claims do not automatically form a useful theory

A theory-mediated learner must ask whether a claim is warranted over its stated
scope and whether it fits the larger working theory well enough to improve
operation and revision. These are different questions. A true claim can be
irrelevant or badly placed; a false claim can appear useful because the current
implementation already assumes it.

Global fit has no complete fixed evaluator here. It is exposed through changed
search and recovery, comparisons with rival or ablated theories, later demands,
repair cost, and transfer. The live system can therefore provide an
[initial selection environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
but not a truth oracle. Independent factual and formal checks, preregistered
predictions, held-out demands, and transfer tests remain necessary to prevent
the working theory from becoming self-sealing.

## Computation already participates in the loop

The present Commonplace process is not a manual design phase waiting for future
automation. A model already retrieves and interprets retained artifacts,
generates and criticizes competing formulations, proposes experiments and
repository changes, runs bounded checks through tools, and writes accepted
revisions into state that guides later calls.

The
[2026-08-30 Commonplace revision record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
is a direct example. The model read many Commonplace artifacts, synthesized a
review and candidate changes, received operator corrections about the Bitter
Lesson framing, revised the theory and repository, and used the revised state in
later turns.

At a boundary that includes the operator, model, knowledge base, and tools, this
is a human-inclusive theory-mediated learning loop with computational search and
artifact retention. At a boundary excluding the operator, global-fit selection
and final acceptance remain outside the computational subsystem.

The distinction is therefore not computation versus no computation. It is
between computational theory-guided search with sparse human high-level
selection and a process whose in-scope learning decisions, updates, and credit
assignment become computational and responsive to additional compute.

Reading and citing retained artifacts supports a mediation claim, but it does
not quantify how load-bearing they were. A matched run with the artifacts
withheld, replaced, or reduced to an information-matched record would provide a
stronger causal estimate.

## The bootstrap grows learning machinery

Human judgment remains in the loop where global fit is not yet represented or
reliably evaluated. That remaining work should be treated as a description of
missing computational learning machinery, not as a protected source of
intelligence.

When a judgment recurs and its scope stabilizes, it can be operationalized as a
methodology, test, validator, learned critic, search objective, episode schema,
or program. The computationally updatable surface then grows. The intended
bootstrap is not "handcraft now, learn later." It is **computational learning
while constructing better machinery for update, evaluation where needed, and
credit assignment**.

The relevant progress measures are whether:

- additional computation improves proposal, criticism, comparison, diagnosis,
  and recovery;
- retained theory improves those operations relative to appropriate controls;
- recurring operator corrections are captured and reused;
- the marginal human judgment required per useful revision falls;
- the learning machinery can challenge target-specific decomposition choices;
  and
- the same process transfers beyond the cases and domains that produced it.

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

## The bootstrap must outgrow its supplied specialization

The hand-designed vision and game-playing approaches in Sutton's comparison
encoded object-level competence for predefined problem classes. Their
computation operated inside features, heuristics, and decompositions that the
method did not learn to replace.

Commonplace differs only if the theories, schemas, methods, evaluators, and
decomposition choices that carry required task-specific competence become
computationally producible or challengeable over the reach being claimed.
Editable files are not enough. An agent may rewrite a prompt while every
important target-specific decision remains fixed human design.

The long-run criterion is not competence in several predefined
domains. A system with ten hand-built ontologies and ten special update
procedures is still a bundle of predefined solutions. As claimed scope widens,
computation must increasingly determine and retain the task-specific theory,
representations, methods, and checks that new demands require instead of
receiving another bespoke human design. The retained specialization must affect
later work beyond the episode that first exposed the need; otherwise a one-off
repair can masquerade as a general learning method.

This does not require the system to derive its own values or revise every fixed
component. Objectives, commitments, grants of authority, general learning
methods, runtimes, exact interfaces, resource controls, and trusted kernels can
remain supplied. The scaling question concerns computational production of
empirical and procedural specialization for the claimed demand class.

No current carrier is promised survival. A future model may absorb a theory,
collapse a representational boundary, or replace a validator with a cheaper
learned mechanism. But carrier replacement is a possibility, not the criterion.
The bootstrap succeeds when computational production displaces recurring human
construction of required task-specific specialization. General machinery may
persist where its warrant and demonstrated reach support it, since [machinery
persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).

## What Commonplace currently establishes

Commonplace establishes that retained theory can participate in computational
search inside a human-agent system and can condition later work. It does not
yet establish a general autonomous learner. People still choose objectives,
judge much global fit, assign blame, construct or approve evaluators, authorize
consequential changes, and repair failures beyond represented coverage.

The current position therefore has four levels:

1. The Bitter Lesson does not impose a weights-only representational rule.
2. Theory-mediated learning is a serious conjecture worth testing.
3. Commonplace already implements computational theory-guided search with
   human-assisted high-level selection.
4. Whether that process can use increasing computation to improve selection,
   reduce marginal human judgment, transfer beyond anticipated domains, and
   beat more direct alternatives remains open.

Only the first level is a rebuttal. The other three are empirical descriptions
and research commitments.

## Tests that can change the strategy

The [research program](./a-research-program-for-learning-software-factories.md#current-evidence-and-next-tests)
specifies the immediate theory intervention and the prospective instrumentation
of the current human-agent loop. For the Bitter Lesson strategy, those results
must additionally show that more computation improves downstream search rather
than candidate volume, that recurring human judgments become reusable selection
machinery, and that the marginal human contribution falls without hidden losses
in quality or warrant.

A later experiment can probe transfer beyond supplied specialization. Before
outcomes are known, declare the demand class, evidence protocol, acceptance
relation, coverage, novelty rule, and human-intervention boundary. Introduce
tasks or an area not used to design the artifact ontology or improvement
procedure. Track which theories, representations, methods, checks, and evaluator
components computation produces, whether they become operative, and whether
they help on independently selected later demands. Broader support requires
repeated transfer without a new bespoke human architecture.

The strategy loses in a tested regime when system use becomes self-confirming,
retained theory makes no causal difference, additional computation does not
improve useful search or selection, human judgment grows with the corpus, each
domain needs a new ontology and oracle, required task-specific decomposition
remains human supplied, or a more direct method performs better at comparable
total cost.

## A prediction to be judged, not a vindication

The Bitter Lesson does not require everything to live in weights. It does
require useful complexity to be earned through methods that exploit search,
learning, evidence, and computation rather than protected as designer
knowledge.

That requirement does not vindicate Commonplace. It tells us how to judge it.
The project is testing whether a computationally assisted, theory-guided
human-agent system can improve its search and grow its learning machinery:
using retained project theory as operative context, exposing global fit through
system-building consequences, and progressively converting recurring human
judgments into evaluators, methods, schemas, and code. Its prediction is that
the process will increasingly produce the task-specific specialization it needs
instead of receiving a new human-built solution for each covered demand. It
makes no prediction that every fixed general component must replace itself.

This is a first construction strategy. It should be retained only while it helps
build a more general learning process than the one that produced it.

The [bootstrap note](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
states the conditional compatibility, why the condition is satisfiable, and
the failure criteria. The
[response-portfolio note](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md)
separates the narrow rebuttal from the broader research commitments.
