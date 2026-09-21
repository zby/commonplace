---
description: "Definition — conjectural learning is learning in which formulated tentative theories are operative in the learning system: used, criticized for what they say, with the result changing the system's capacity for future action"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Conjectural learning

**Conjectural learning** is learning in which tentative theories are
formulated, operative objects within the learning system: the system uses
them, criticizes what they say, and carries the result of that criticism
into its capacity for future action. It is Popper's process of conjecture and
criticism under two conditions:

1. **A formulated theory is operative.** A
   [tentative theory](./tentative-theory.md) is formulated in language,
   natural or formal, and is on the causal path of the system's decisions
   through what it says: a difference in its content that matters to a
   decision changes that decision
   ([operative change](../../../notes/definitions/operative-change.md)).
2. **Criticism of what the theory says changes the system's capacity for
   future action.** Criticism here means an attempt to find an error: an argument,
   or a test of a stated consequence, aimed at something the theory says, and
   itself formulated in language. When the criticism counts against the
   theory, the theory is revised or replaced in response. When it survives,
   the testing result can change how the system would rely on it or choose
   further tests without changing its content or tentative status. The
   grounds extend only to what the test actually challenged. In both cases
   the result must change what the system would later do; recording a result
   alone does not establish that effect.

The unit is the whole learning system, with a declared boundary that includes
its participating people and services. Prompts, files, code, tests, records,
and model weights can all be internal parts. Location inside or outside the
weights, formulated or latent content, and the system boundary are separate
distinctions. Fixed weights are a study condition, not a definitional one.

Learning is an improvement in the system's capacity for future action: what the
system as it stands would do when an occasion arises. The occasion need not
have arisen; observed action provides evidence of the capacity. Action
includes developing and testing further theories, and decisions about what
to rely on or investigate next. The improvement must be attributable to the
persisted effect of criticism. Exercising the process without that
improvement is an attempt to learn. Individual criticisms and revisions can
fail within a process that does produce learning.

The effect can persist in retained theories and their testing records, or in
retained criticisms used to reconstruct theories. Indexed traces can retain
these objects; separate theory documents are not required.

The process is Popper's schema for the growth of knowledge,
`P1 → TT → EE → P2`: a problem, a tentative theory, attempted error
elimination, and a new problem
([Popper 1966](../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md#quotes)).
*Conjectural* is Popper's own word for the status of theories, which "remain
essentially tentative, or conjectural, or hypothetical"
([Conjectures and Refutations, Chapter 1](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
It does not mean speculative or unsupported.

## Relation to Popper

The definition narrows Popper's process as follows, retaining his schema,
tentative status, criticism broader than empirical testing, and selection
rather than instruction:

| | Popper covers | Conjectural learning keeps |
|---|---|---|
| Form | Dispositions, expectations, and habits as well as formulated theories | Theories formulated in language |
| Elimination | All error elimination, from the death of the carrier to conscious criticism | Criticism of what the theory says |

Popper's criterion for objective knowledge does not require actual use by a
particular system. Attributing learning to a system requires more than
available content: the theory must guide its decisions, and criticism must
change its capacity for future action. Observed action provides evidence of
that capacity. Commonplace specifies these attribution conditions. Popper also describes
self-criticism and feedback between people and their work
([1968, §9](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes));
the distinction concerns what establishes learning by this system.

Commonplace's choice of research arrangement and its three conjectures are
stated in
[Commonplace studies conjectural learning through retained theories](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md).

## Scope

- **Persistence follows the claim.** A claim identifies the action the
  improved capacity is for and the evidence of improvement. If it claims
  that the capacity remains available at a later time, the effect of
  criticism must persist to that time. Conjectural learning adds no minimum
  duration.
- **Observer access is an evidence question.** A model may formulate and
  criticize conjectures in language that no observer sees. Where evidence
  does not establish formulation, criticism, causal use, or improvement,
  membership remains unestablished. Opacity alone establishes neither
  presence nor absence. Membership does not require that it has been
  demonstrated. The companion's
  [evidence discussion](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#evidence)
  describes how to investigate it.
- **Improvement does not require a faultless theory.** A theory can remain
  mistaken in some respects while supporting an improved capacity for
  future action. A revision that merely changes behavior does not by itself
  establish learning.
  Whether this approach outperforms alternatives is a further question,
  conjectured in the companion note and in
  [learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md).
- **Addressability is a stronger property, not a condition.** An
  [addressable theory](./addressable-theory.md) lets criticism name the part
  that probably caused a failure, and lets a revision act on that part. The
  KB conjectures that this pays and builds for it, but a theory that is
  criticized and replaced whole still qualifies.
- **Revision need not be small.** Criticism may change a core assumption, a
  representation, an auxiliary assumption, a test, the problem, or learning
  machinery, and the successor may be bold.
- **The subject and the machinery are unrestricted.** The theory may describe
  a subject outside the system or its own organization. The latter is
  reflective only when the self-representation is causally connected to the
  system it describes; see
  [reflective system](../../../notes/definitions/reflective-system.md). A
  model, a program, or a mixture may apply and criticize the theory. A
  persistent system responsible for developing and revising addressable
  theories is a [theory builder](../../../notes/definitions/theory-builder.md);
  conjectural learning alone does not establish those additional conditions.

## Exclusions and boundary examples

These examples show where the term applies and where it does not. Some also
serve as experimental baselines; a baseline can lie on either side of the
boundary. The inside cases assume that the stated process improves the
system's capacity for future action; without improvement they describe
attempts to learn.

- **A theory criticized and replaced whole.** Inside when the criticism
  bears on its content and the replacement would guide later action. Separately
  editable parts are not required.
- **Reconstruction from retained criticisms.** Inside when formulated
  criticisms and their results would guide reconstruction and use of a
  theory when needed. The assembled theory need not itself persist.

- **A fixed theory.** Outside: a formulated theory guides decisions and is never
  criticized. Fixed instructions left uncriticized are one example. No effect
  of criticism exists to persist. This is the frozen-seed baseline of the
  [testing supplement](../../../articles/testing-the-theory-refinement-program.md#the-hypotheses).

- **A theory built while reasoning and then discarded.** Inside if
  formulated criticism changes the system's capacity for future action, before
  the theory is discarded or through a retained result afterward. Outside if
  the theory is merely applied and nothing learned from criticism changes
  that capacity.
- **Records retaining only inputs and outcomes.** These supply evidence for
  reconstruction without retaining formulated conjectures or criticism.
  This is a comparison of retained content, not a claim about what the
  reconstructor does. Traces that preserve conjectures and criticism belong
  with retained theories or criticisms; an index can make them directly
  addressable for future use.
- **Black-box optimization of prompts and programs.** Variants are generated
  and selected by outcome alone. A proposer may read the variants, but no
  formulated reason for a failure bears on what a variant says. Real systems
  fall between this case and conjectural learning. The test is whether a
  stated reason bears on what the theory says.
- **Weight adaptation alone.** Something persists, but by stipulation nothing
  is formulated, so there is nothing to criticize, replace, or inspect on its
  own. A system whose weights adapt and whose formulations are unknown is a
  different case, and it stays unclassified.
- **Proof-only revision under an uncriticized theory.** A formulated theory
  guides decisions and licenses revisions only by proof from premises that,
  by stipulation, are never criticized. This arrangement is outside because
  criticism is absent. Proof-governed switching is a feature of the
  [Gödel machine](../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md);
  that feature alone does not establish the absence of criticism elsewhere
  in a system. Deductive criticism can qualify.

- **A stored theory or record that nothing would consume.** No process in the
  system would consume it, so it is not on the causal path of decisions and
  adds no capacity. A theory that a process would consume when an occasion
  arises is not this case. See
  [a representation matters only through its consumption path](../../../notes/an-action-model-matters-only-through-its-consumption-path.md).
  As a baseline it is the same system run without the theory.

## Misuse Cases

- Opposing *criticism* to *selection*. For Popper all learning is selection:
  criticism eliminates, and the successor is a new conjecture. Black-box
  optimization differs in what eliminates and what it acts on: a score acting
  on whole variants, whereas criticism is an argument acting on claims.
- Counting as criticism an outcome score that only ranks variants, or
  counting a system as a conjectural learner because it retains prose about
  its subject or itself.

---

Relevant Notes:

- [Tentative theory](./tentative-theory.md) — defined-in: the status of the theory that guides decisions
- [Addressable theory](./addressable-theory.md) — extends: the stronger structural property the KB conjectures pays
- [Commonplace studies conjectural learning through retained theories](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md) — extends: the chosen research arrangement and its three conjectures
- [Reflective theory refinement needs interpretation, retention, and independent read-back](../../../notes/reflective-theory-refinement-needs-interpretation-and-retention.md) — extends: the evidence ladder for the parts of the process
