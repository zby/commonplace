---
description: "Definition — conjectural learning is Popper's process run by a system in which an addressable tentative theory guides decisions, criticism addresses the part it blames, and the effect persists across a declared horizon"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Conjectural learning

**Conjectural learning** is the learning paradigm in which a system
runs Popper's process of conjecture and criticism under two conditions:

1. **An addressable theory guides decisions.** A
   [tentative theory](./tentative-theory.md) is formulated in language,
   natural or formal, so that its assumptions, scope, and parts can be
   inspected and revised individually
   ([addressable theory](./addressable-theory.md)). It is on the causal path of the system's decisions through what
   it says: a theory of the same form with different content would lead to
   different decisions. Withholding the theory is not a sufficient test,
   because adding any text of that form can change behavior.
2. **Criticism addresses a part of the theory, and its effect persists
   across a declared horizon.** Arguments, and tests of the theory's stated
   consequences, bear on its content and name the part that probably caused
   the failure. The revision acts on that part, and what changes guides work
   beyond a stated boundary, such as the next episode or a later task. The
   blamed part is a candidate, not a verdict. The criticism is itself
   formulated in language, and it passes the same content test as the theory:
   a criticism with different content would lead to a different revision. An
   outcome score that only ranks variants is not criticism in this sense.

What the system has learned is the change in its later behavior that is
attributable to the persisted effect of criticism.

The effect can persist in two ways. The system may retain the theory itself
and revise or replace it, or it may retain the formulated criticisms and
reconstruct a theory from them when one is needed. Both are implementations
of the paradigm. Reconstruction from raw records, which hold traces and
outcomes but no criticism, is not: what persists there is evidence, and any
criticism is redone inside each episode. It is a separate comparison. The KB
prefers retaining the theory, on an efficiency conjecture stated under Scope
that is tested against both kinds of reconstruction.

The process is Popper's schema for the growth of knowledge,
`P1 → TT → EE → P2`: a problem, a tentative theory, attempted error
elimination, and a new problem
([Popper 1966](../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
The KB cites the schema and does not redefine it. *Conjectural* is Popper's
own word for the status of theories, which "remain essentially tentative, or
conjectural, or hypothetical"
([Conjectures and Refutations, Chapter 1](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
It does not mean speculative or unsupported.

## Position relative to Popper

Conjectural learning is a narrow part of the learning Popper describes, with
operational requirements he does not state. It does not dispute his account of
the rest.

**Taken as is.** The schema, the tentative status of every theory, criticism
that is broader than empirical test, and selection in place of instruction:
criticism eliminates, and a successor theory is a new conjecture, not
something the failure dictates.

**Narrowed.** Each row keeps one of the cases Popper covers.

| | Popper covers | Conjectural learning keeps | Why |
|---|---|---|---|
| Carrier | Dispositions, expectations, and habits as well as formulated theories | Theories formulated in language | Only a formulation gives criticism an object; this is his own point about rational criticism (1968, §4) |
| Structure | Any formulated theory; one that can only be replaced whole still counts | Addressable theories | Criticism needs a part to blame |
| Elimination | All error elimination, from the death of the carrier to "conscious criticism" (1968, §5.2, p. 351) | Criticism of what the theory says | A score that ranks variants does not engage the theory as a claim |
| Localization | A failed test may implicate a whole theoretical system; some cases identify the responsible hypotheses (*Conjectures and Refutations*, Chapter 10, XVI) | Criticism that names the probable cause | A failure that blames nothing leaves the successor unconstrained. A practical limit, not a claim that the other case cannot occur |
| Result | "As a rule" a new problem; knowledge grows even when no successor theory is accepted | An effect that persists and guides later work | A system's learning is observed in its later decisions |

**Added.** The theory's place on the causal path of a particular system's
decisions, the declared horizon, and the evidence for each. Popper requires
less for objective knowledge: a text that could be understood already counts,
read or not. We require actual use.

**Learning is observed in behavior, without instrumentalism.** The definition
locates what was learned in later decisions, because it describes an
engineered system. It does not treat theories as mere instruments for
prediction, a view Popper criticizes (*Conjectures and Refutations*, Chapter
3). What criticism bears on is what the theory says, and whether a theory
deserves its scope is judged separately, by
[reach-assessment](../../../notes/definitions/reach-assessment.md).

**Where we ask less than Popper.** He counts competing theories and mutual
criticism by argument among the indispensable means of scientific growth
([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
§4, p. 347). The definition does not require an independent critic: the same
model may propose and criticize, and then shares its blind spots with itself.
Independence of assessment is a separate condition, described in
[externally tested theory builder](../../../notes/definitions/externally-tested-theory-builder.md).

**Where a fixed interpreter departs from Popper's scientist.** His scientist
changes along with the theories: objective knowledge feeds back on the mind
that grasps it. With fixed weights that channel is closed, and each episode
reads the theory afresh. The articulated part must then carry all of the
learning, including what a person would absorb as tacit skill. Background
knowledge held in the weights also cannot be revised during the interval,
where Popper holds any background assumption open to challenge. It can be
criticized only by articulating a theory about the interpreter and retaining
that, which is the reflective case. The
[coevolution extension](#extension-coevolution) reopens the channel.

**Empirical.** Whether a model interprets a prose theory reliably enough to
apply and criticize it, whether the content of retained criticism carries
an effect beyond the form of the intervention, and whether retaining a
theory is cheaper than reconstructing one. The definition is neutral on all
three. On the second, controlled studies of code models have so far not
separated content from form: error content in prompts and in trained
adapters showed no advantage over placebo content
([PoPE](../../../sources/form-not-content-placebo-controlled-self-repair.ingest.md)),
and a full Popperian procedure showed none over its labels alone
([Scaffold, Not Vocabulary?](../../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md)).
Neither tested equivalence or a retained theory reused across tasks.

## The two levels

Popper runs the same schema at two levels. Without language, the tentative
theories are inborn expectations, dispositions, and habits, and error
elimination acts on the carrier itself: the organism perishes or is changed
together with its theory. With language, a formulated theory can be criticized
and discarded while its holder survives
([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
§4 and §§8–9).

A system built on a language model has both levels. The weights hold
dispositions formed by training, a process that changes the carrier. The
articulated part, which is prose, prompts, and code, holds formulated
theories. The model that reads them is the link between the two: in Popper's
words, "all our actions in the first world are influenced by our second-world
grasp of the third world" (§9, p. 371).

In the primary case the weights stay fixed and the articulated part carries
all of the learning. The KB does not deny learning at the other level; it
chooses the level where a theory can be criticized, replaced, and inspected
one at a time, and where a change in behavior can be attributed to a change
in text. Mapping the weights onto Popper's level without language is our
reading, not his claim.

## Extension: coevolution

The term extends to a system in which weights, prompts, and code evolve
together, provided the two conditions still hold: an addressable theory is on
the causal path of decisions, and the effect of criticism persists. The two
levels then shape each other. Content from criticized theories may be trained
into the weights, and changed weights read, apply, and criticize the theories
differently. This restores the feedback from formulated theories to the mind
that grasps them, which Popper's scientist has and the primary case closes.

The extension is admitted, not pursued: the KB's experiments hold the weights
fixed. Coevolution costs the clean attribution of the primary case, so a claim
about such a system says through which carrier the effect of criticism
persisted. Weight adaptation with no addressable theory on the causal path of
decisions stays outside the term.

## Scope

- **The horizon is declared, and the claim is relative to it.** A theory
  revised and reused within one episode supports a within-episode claim.
  The research program's claims concern horizons that cross episodes.
- **The term classifies by what is articulated and persists.** It makes no
  claim about what happens inside the machine. A model reading raw traces may
  criticize conjectures internally, as training may inside the weights; such
  criticism leaves nothing formulated to inspect, attribute an effect to, or
  criticize in turn, so it is outside the term without being denied.
  Membership is therefore checkable from artifacts: formulated criticisms
  that name parts of a theory, passing the content test.
- **Retention is compared with both kinds of reconstruction.** Three
  arrangements differ in how much of the work of conjecture and criticism
  persists. Raw records persist none of it: each episode regenerates the
  criticism and the theory. Retained criticisms persist the eliminations:
  each episode reassembles the theory. A retained theory persists the
  assembled result. The KB's efficiency conjecture is that cost at comparable
  decision quality falls in that order, because the earlier arrangements
  repeat interpretive and inferential work, and that bounded context widens
  the gaps, because the relevant records may not fit together and must first
  be retrieved, selected, or summarized. A retained theory has maintenance
  costs of its own and can go stale. A system that reconstructs from raw
  records may match or beat a conjectural learner; the term is not a success
  term, and that comparison is what the experiments measure. The two
  comparisons answer different questions. Against raw records: does
  formulated, persisted criticism buy anything? Against retained criticisms:
  does keeping the assembled theory buy anything more?
- **Not a success term.** A system that carries a mistaken theory forward is
  still a conjectural learner. Whether it improved anything is
  measured separately.
- **Addressing a part is not minimal revision.** The part blamed may be a
  core assumption, a representation, an auxiliary assumption, a test, the
  problem, or learning machinery, and its successor may be bold; most of the
  theory may change as a result. What the definition requires is that the
  change answers a criticism of something the theory says. A theory may also
  survive unchanged while the test result guides later inquiry across the
  declared horizon.
- **Fixed weights are the primary study condition.** Holding the weights
  fixed rules out updates to those parameters as the source of a change, so
  the articulated part must account for it. Declare which models stay fixed
  and for what interval, and the whole learner's boundary, including human
  contributions and external services. Fixed weights are not part of the
  definition; see the coevolution extension.
- **Any subject and machinery.** The theory may describe an external subject
  or the system's own organization; the second is the reflective case, which
  composes this term with [reflective system](../../../notes/definitions/reflective-system.md).
  A model, a program, or a mixture may apply and criticize the theory.
- **The carrier is separate.** The system that runs the process is a
  [theory builder](../../../notes/definitions/theory-builder.md), identified
  by responsibility and lineage.
- **A partial case is reportable at its own strength.** Evidence that a
  theory guided a decision, or that one criticism changed it, shows that
  part. The [evidence ladder](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md#evidence-forms-a-ladder)
  says what evidence each part needs.

## Separate comparisons

These arrangements may also run Popper's process. The research program
specifies each as its own comparison.

- **A theory built while reasoning and discarded after the decision.** It can
  guide that decision. Nothing of it persists across an episode-crossing
  horizon.
- **Reconstruction from raw records.** Traces, inputs, and outcomes are
  kept, and a theory is rebuilt from them when needed. Evidence persists
  across the horizon; the effect of criticism does not. The arrangement needs
  no criticism step at all: records are stored, retrieved, and handed to the
  model. Whether the model criticizes conjectures internally while rebuilding
  cannot be known from outside and does not change the classification. This
  is the primary comparison, because it tests whether formulated, persisted
  criticism buys anything over regeneration.
- **Black-box optimization of articulated text.** Variants of a prompt or
  program are generated and selected by outcome alone, as in score-driven
  prompt optimizers and evolutionary program search. The text is articulated,
  guides decisions, and persists, but nothing reads the variants as claims or
  records why a variant failed. Popper's scientific level adds "conscious
  criticism" to error elimination
  ([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
  §5.2, p. 351); this arrangement applies elimination alone to formulated
  theories. It is the natural baseline for the KB's central conjecture that
  criticism of content learns more from each failure. Systems lie on a range:
  the test is whether a stated reason bears on what the theory says.
- **Unaddressed revision.** A failure is observed, and may even be described,
  but no part of the theory is blamed for it; the theory is rewritten or
  regenerated whole. This differs from black-box optimization in that a
  reader does process the failure, and from conjectural learning in that the
  revision does not answer a criticism of any particular claim. The KB sets
  it aside as unlikely to be practical, not as impossible.
- **Weight adaptation.** Learning at the level without language: the carrier
  itself is changed. Something persists, but nothing is articulated, so there
  is no formulation to criticize, replace, or inspect on its own.

## Exclusions

- **A theory that is applied and never criticized**, such as fixed
  instructions. No effect of criticism exists to persist.
- **A stored theory or record nothing consumes.** It is not on the causal
  path of decisions, since
  [a representation matters only through its consumption path](../../../notes/an-action-model-matters-only-through-its-consumption-path.md).

## Misuse Cases

- Calling a system a conjectural learner because it retains prose
  about its subject or about itself. The term names a process on the causal
  path of decisions, not an artifact.
- Using *theory refinement* or *learning by theory refinement* for the
  paradigm. Those were the KB's earlier names, taken from the classical
  theory-refinement systems of machine learning. The systems remain a
  precedent for repairing an [addressable theory](./addressable-theory.md);
  the paradigm does not inherit their representation, operators, or
  preference for minimal change.
- Treating fixed weights as part of the definition. They are the primary
  study condition, and the coevolution extension lifts them.
- Opposing *criticism* to *selection*. For Popper all learning is selection
  and none is instruction: criticism eliminates, and the successor theory is
  a new conjecture, not something the failure dictates. The contrast with
  black-box optimization is what does the eliminating and what it acts on: a
  score acting on whole variants, or an argument acting on claims.
- Calling weight adaptation alone conjectural learning. Without an
  addressable theory on the causal path of decisions, the first condition
  fails.
- Reading the term as a claim that the paradigm works or beats the
  separate comparisons. That is the conjecture in
  [learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md).

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of the theory that guides decisions
- [Addressable theory](./addressable-theory.md) — defined-in: the structural property the first condition requires
- [Theory builder](../../../notes/definitions/theory-builder.md) — contrasts: the system that carries the process, defined by responsibility and not by whether or how it learns
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder for the parts of the process
- [Learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — extends: the payoff conjecture the definition stays neutral on
- [Popper, Epistemology without a knowing subject](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: language as the object of critical discussion
