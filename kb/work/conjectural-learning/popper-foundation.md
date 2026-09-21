# Popperian support for the current approach

The [current direction](./definition-decision-record.md#settled-decisions) has direct Popperian
support for articulation and criticism-guided action. An effect of criticism
on the system's capacity for future action is our operational condition;
observed action provides evidence of that capacity. This grounds the simplification;
it does not demonstrate the implementation's effectiveness.

## Direct support and its limits

Six of the eight retained extracts in [Epistemology Without a Knowing Subject](../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes)
support the following reading of the 1968 publication:

| Part of the approach | Source support | Attribution boundary |
|---|---|---|
| Articulate theories so they can be criticized | §4, p. 346: descriptive language provides an object for critical discussion; p. 347: scientists try to eliminate false theories in their stead | A direct epistemic reason for articulation, not a requirement for a repository, separately editable parts, or a formal consumer |
| Work with theories before symbolic formalization | §6, p. 360: mathematical growth includes criticism of guesses and informal proofs, with linguistic formulation | Supports informal critical argument; does not imply that unarticulated states suffice for scientific discussion |
| Let criticism affect the work that guides action | §9, p. 370: feedback between ourselves and our work can be amplified by self-criticism; p. 371: understanding objective contents influences action | Philosophical support for the relation; our causal-use tests must establish it in a particular system |
| Carry the effect into the capacity for future action | §3, p. 342 distinguishes potential intelligibility from actual understanding | Objective availability alone does not establish learning by a particular system. Commonplace requires a capacity of the system as it stands, which needs a process that would consume the content, and specifies the evidence of use needed for that attribution |

These are different attribution questions: whether content qualifies as
objective knowledge, and whether a particular system has learned through
using it. Popper's discussion of feedback and self-criticism already includes
the learner. His account of mutual criticism (§4, p. 347) does not by itself
require an independent critic in every instance of learning. How much
decorrelating a critic from a proposer helps remains an empirical question.

Thus articulation is partly inherited, rather than wholly our addition to
Popper. We specify how to establish causal use and persistence of criticism's
effects. Retaining a theory and reconstructing it from retained, formulated
criticisms are implementation approaches; our preference for the former rests
on the efficiency conjecture in the companion note. Records containing only
inputs and outcomes supply a comparison of retained content. Indexed traces
can instead implement retained theories and criticisms. The
[definition draft](./definitions/conjectural-learning.md) distinguishes content
and use, not storage format. None of these passages supplies
fixed-model sufficiency or a result for records versus retained theories.

## Existing primary-source context

The following locators retain the earlier reading of the broader argument;
detailed checking requires the paired snapshots. Computational consequences
remain our inferences.

**Problems, tentative solutions, criticism, new problems.**
[A Realist View of Logic, Physics, and History](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md),
printed pp. 3–5, gives `P1 → TT → EE → P2`, including competing conjectures.
Critical discussion compares how proposals solve their problems and is broader
than error elimination. The outcome can be new problems rather than a repaired
theory. Popper extends the schema to behaviour and biological evolution.

**Tentativeness does not prescribe a software artifact.**
[Conjectures and Refutations](../../sources/popper-conjectures-and-refutations.ingest.md),
Chapter 1, IV–V, pp. 45–48, treats conjectured regularities as preceding their
testing and discusses unconscious, inborn expectations. VI–VII, pp. 49–51,
contrasts dogmatic adherence with readiness to modify or abandon conjectures.
Chapter 15, section 1, p. 313, calls a theory a tentative solution to a problem.
These passages support a broader account than symbolic objects stored
outside model weights; they do not establish that any particular neural update implements it.

**Objective content is not storage outside the weights.** *Realist View*, section 2,
distinguishes mental processes from logical relations among their products.
A theory's implications exceed its author's understanding. That independence
is different from storage outside model weights; the software embodiment
question does not settle Popper's ontology of objective knowledge.

**Criticism exceeds empirical falsification.** *Conjectures and Refutations*,
Chapter 1, II, pp. 37–39, distinguishes empirical-science demarcation from
meaningfulness. Untestable proposals need not be meaningless, but cannot
thereby claim empirical support. *Realist View* also discusses different
critical traditions and standards. A statistical test is therefore too narrow
as the sole criticism mechanism for the general account.

**Background assumptions are revisable, provisionally.** *Conjectures and
Refutations*, Chapter 10, XV–XVI, pp. 238–239, permits questioning background
knowledge and replacing problems while rejecting the practical possibility of
challenging every assumption simultaneously. A failed test may implicate a
whole theoretical system without uniquely identifying the faulty part.
Piecemeal criticism does not entail a small syntactic edit.

**Test survival is provisional; revision must expose new consequences.**
Chapter 1, pp. 36–38, criticizes reinterpretations that remove testability.
Chapter 10, XVII–XIX, pp. 240–243, discusses test severity and independently
testable consequences beyond the facts used to construct a successor. It
distinguishes promising theories from new empirical successes. Even an early
refutation can yield new facts and problems; progress nevertheless needs
empirical successes too.

Storage, edit interfaces, fixed weights, budgets, and permissions are design
choices. None becomes a Popperian requirement by being useful to our system.

## Compression and induction belong to the implementation layer

[Schmidhuber's compression-progress framework](../../sources/driven-by-compression-progress.ingest.md)
rewards improvements in compressing the same history. Solomonoff induction
instead supplies an ideal Bayesian predictor over computable environments;
the exact predictor is incomputable
([Schmidhuber 2009, Appendix A.8](https://arxiv.org/html/0812.4360v2)).
Neither requires formulated criticism of what a theory says, and
[conjectural learning](./definitions/conjectural-learning.md) requires
neither. Its ontology identifies operative tentative theories and the
persisted effects of criticism, not a compression objective or an inductive
prior.

At the implementation layer, compression progress can guide conjecture
generation and experiment selection. Computable predictors inspired by
Solomonoff can support prediction and search. A compression score or posterior
probability alone does not supply the criticism our definition requires.
Using these mechanisms does not require adopting inductive confirmation as
the foundation of learning. Whether they help is an empirical question.

The [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md)
gives compression an engineering motivation: retained state can exceed what
any one call can use. Derived theories and task-facing views may save
context and repeated inference without replacing raw records retained when
economical. Context savings are not by themselves evidence of improved data
compression. Storage policy and the choice of compression measure remain
implementation decisions.
