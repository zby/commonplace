# Workshop: conjectural learning

## Intent

Replace the classical theory-refinement import with Popper's epistemic process
as the foundation of the paradigm in
[Learning by Theory Refinement with Fixed Models](../../articles/learning-by-theory-refinement-with-fixed-models.md),
and make the library simpler by doing so.

The library takes *theory refinement* in the established sense of Ourston and
Mooney and Richards and Mooney, then lifts that sense's limits by extension:
[the definition](../../notes/definitions/theory-refinement.md) departs from
the classical systems in machinery, form, and subject. The operator's judgment
is that the import buys nothing after those departures. Only the task
statement survives them, and the library pays for apparatus that manages the
import: the task/realization separation, the departures section, much of the
[three-lineages note](../../notes/reflective-theory-refinement-has-three-separate-lineages.md),
and a separate term for the loop because the borrowed name denotes one
operation.

Commissioned by the operator on 2026-09-19. All directions below are the
operator's, given the same day.

## Directions that changed the first formulation

- **Simplification, not a new ontology.** The first candidate defined a
  general “conjectural learning” with four roles and a coined *uptake*
  condition. It excluded almost nothing: nine of ten boundary cases were
  eligible or undetermined, and merely placing criticism in an LLM's context
  did not establish a lasting learning effect. Cite Popper's
  schema, which already has a name and an attribution, and define only what
  we add.
- **What we add.** An articulated tentative theory on the causal path of
  decisions, and an effect of criticism that persists across a declared
  horizon. The horizon replaces *uptake* as what separates learning from
  in-context reaction.
- **Articulation is partly Popper's.** His 1968 essay makes a language
  developed outside the body the object of critical discussion. He claims
  this for rational criticism, not for learning in general. See
  [Popper foundation](./popper-foundation.md).
- **Reconstruction splits in two, and we compare against both.** The first
  direction put all reconstruction from records inside the approach. Once
  criticism had to address the theory's content, a gap showed: raw traces
  hold no criticism, and we cannot know whether a model criticizes internally
  while rebuilding a theory from them. The term therefore classifies by what
  is articulated and persists, and claims nothing about the machine's
  insides, as with the weights. Reconstruction from retained criticisms stays
  inside; reconstruction from raw records is a separate comparison. It is the
  primary one: the operator's assessment is that regeneration from raw
  records is now the dominant approach, and it requires no criticism, so the
  comparison tests whether formulated, persisted criticism buys anything. The
  comparison with retained criticisms asks what the assembled theory adds.
  Retaining
  the theory is our preferred implementation on an efficiency conjecture:
  the three arrangements persist none, some, or all of the work of conjecture
  and criticism, cost at comparable decision quality should fall in that
  order, and bounded context should widen the gaps because the relevant
  records may not fit together. The claim is ours and untested. Compare by
  cost at comparable decision quality and by quality under matched budgets,
  counting retained-theory maintenance; vary context capacity or record
  volume. Within-episode discard and weight adaptation stay separately
  specified comparisons.
- **Only the articulated part evolves.** We do not oppose Popper's learning
  without language; our systems have that level too, in the model weights,
  which hold dispositions formed by training. We choose to evolve the
  articulated part: prose, prompts, and code. With fixed weights the
  articulated part must carry all of the learning, and background knowledge
  in the weights can be criticized only through a retained theory about the
  interpreter. Coevolution of weights, prompts, and code is an admitted
  extension of the term, with its own section in the draft: both conditions
  must still hold, and it reopens the feedback from theories to the
  interpreter that Popper's scientist has. It is not the primary goal.
- **Criticism must address the theory's content and a part of it.** The new
  papers showed that the draft admitted two cases we do not study.
  Black-box optimization of articulated text selects variants by outcome
  alone; nothing reads them as claims. Unaddressed revision processes a
  failure but blames no part and rewrites the theory whole. Both are separate
  comparisons. Conjectural learning therefore requires an addressable theory
  after all, and criticism that names the part that probably caused the
  failure. This requirement is ours, not Popper's, and is made on practical
  grounds. The causal-path test is also about content: a theory of the same
  form with different content must lead to different decisions, since
  placebo-controlled studies found form effects without content effects.
  For Popper all learning is selection, not instruction, so the contrast is
  what eliminates and what it acts on, not criticism against selection.
- **The name.** *Theory refinement* leaves the library altogether, so
  *learning by theory refinement* does not survive. The working replacement
  is **conjectural learning**, “or something similar”. It names our scoped
  paradigm, which is narrower than Popper's process and than the first
  candidate's use of the same words. *Conjectural* is Popper's word for
  tentative status, not a synonym for speculative.
- **Definitions first, migration later.**

## End state and acceptance

Stage 1, current: definition drafts in [definitions/](./definitions/), written
against the real `definition` type contract, for operator review. Stage 2: the
operator adopts, redirects, or declines them and settles the open decisions.
Stage 3, under a later commission: migration, from the
[parked notes](./migration-map.md).

The result must leave the library simpler than it found it:

- fewer definitions, or the same number with less departure and attribution
  apparatus, with an accounting at the migration stage;
- every retained classical element names what it buys; EITHER and FORTE are
  expected to survive only as a precedent for connecting a discrepancy to
  candidate repair locations;
- a new term enters only for a claim that cannot be stated without it;
- Popper's claims, our additions, and empirical questions stay
  distinguishable;
- the comparison of retention with reconstruction, the causal-use
  requirement, the evidence ladder, the whole-system learning boundary, and
  external-requirement authority keep their force.

Do not enrich the classical theory-refinement account as an intermediate step.

## Open decisions, for the operator

- The final form of the name.
- Merging the operation and loop definitions. The drafts assume the merge and
  supply no term for a single revision episode.
- Dropping the classical minimal-revision bias. The drafts drop it: the part
  a criticism blames may be a core assumption and its successor may be bold.
  No retained claim has yet been checked for dependence on the bias.

## Cautions carried from the first candidate

These are not in the drafts and still apply to later experiments and articles.

- Replacing or weakening a failed test requires grounds to doubt its
  measurement or relevance. Reformulating a problem cannot establish
  compliance with an unchanged external requirement; state who can authorize
  a changed requirement. The authority rule is our engineering constraint.
- A learner whose testing or revision machinery changes is not thereby a
  [reflective system](../../notes/definitions/reflective-system.md), which
  requires a causally connected self-representation.

## Bounds

- Write scope: this workshop, source captures and ingests with their
  connection reports, and the workshop index. Library, article, glossary, and
  code changes require a later commission.
- Retained quotes enter an ingest only through the grounding workflow.
- Peer workshops keep their commissions:
  [interface operations](../theory-refinement-interface/README.md),
  [component experiments](../explanatory-theories-deployment-time-learning/README.md),
  [outside experiment template](../first-downstream-run/README.md). Propose
  reinterpretations here.
- The worker may revise the drafts, choose further probes, and reorganize the
  workshop. The acceptance tests and the operator's directions do not move.

## Inputs

[Sources](./sources.md) records coverage and access limits.
[Popper foundation](./popper-foundation.md) holds the primary-source reading
and the attribution boundary. [Comparison](./comparison.md) assesses the
modern papers; it informs later experiment controls more than the
definitions. [Verification](./verification.md) records what was checked.

## Completion

The operator resolves the drafts and the open decisions; a later commission
migrates. Close the workshop under its collection contract once the result is
promoted or otherwise resolved.
