# Workshop: refactor the research program around the theory builder

## Goal

Refactor the research program around a new autonomous learning paradigm whose
learner is a **reflective theory builder**.

The builder's primary work is to develop and revise explicit, fallible theories
about externally supplied subjects. That work also tests the adequacy of the
builder's current theory-building machinery. When a failure is attributed to
that machinery, the builder can revise a theory of its own theory-building
organization and change the machinery used for later theory work.

The target is an **autonomous reflective theory builder**: the same loop with
all internal theory-building, diagnosis, evaluation, machinery-revision, and
successor-selection roles performed computationally. Commonplace is a current
human-inclusive instance of the broader pattern; the operator still performs
important roles in the reflective loop.

Automatic theory refinement and fallible theories are prior art. The proposed
advance is the autonomous combination: external theory work, reflective
revision of the theory builder, and acquisition of missing theory-building
machinery as new theory families expose limitations of the current machinery.

Whether sufficiently broad theory building requires the system to become a
[software house](../../notes/definitions/software-house.md) is now a side
conjecture, not a premise or load-bearing consequence of the learning paradigm.

## Who posed it

The operator, on 2026-09-09, from a summary of a ChatGPT discussion. The
summary proposed a four-level ladder: classical theory refinement, universal
theory refinement, automatic universal theory refinement, and a fourth rung
for refinement embedded in a closed action-and-consequence loop. The agent's
assessment in the same session found the ladder mixed two axes (role
allocation and loop closure), found *universal* unstable as a term, and found
that natural-language form alone does not make a theory refinable. The
workshop uses the KB's term, theory refinement, throughout; the summary's own
names are not carried in. The operator then commissioned this workshop: start from this
README, then write a proposal for the theory builder the program needs, under
whatever adjective fits, copying the good parts of the software-house
definition.

On 2026-09-10 the workshop direction changed: the research target became the
autonomous reflective theory builder described above, with external theory
refinement kept as the useful task and the test of whether the current
machinery has sufficient reach. Software-house capability was demoted to a
side conjecture.

## Working artifacts

- [Theory builder](./theory-builder.md) — minimal definition of the system that
  develops and revises theories for external subjects.
- [Reflective theory builder](./reflective-theory-builder.md) — adds a revisable
  theory of the builder's own theory-building organization and machinery
  change driven by that self-theory.
- [Autonomous reflective theory builder](./autonomous-reflective-theory-builder.md)
  — the target learner, with all internal roles computational.
- [Theory-builder proposal](./theory-builder-proposal.md) — the earlier draft
  around an open-ended automated theory builder; retained for material to
  reconcile with the new direction.
- [Universal theory manipulator](./universal-theory-manipulator.md) — earlier
  draft of a fully codified limit; no longer load-bearing and requires review
  before any promotion.
- [Theory refinement as an interface](./theory-refinement-interface.md) —
  working document: derive, compare, locate, revise, and evaluate as a useful
  decomposition of theory refinement; its relationship to the established
  theory-refinement literature still needs tightening.
- [Note draft: theory refinement is an interface of five operations](./note-draft-theory-refinement-is-an-interface.md)
  — candidate material for that reconciliation.

## What closes the workshop

1. The definitions of theory builder, reflective theory builder, and autonomous
   reflective theory builder are accepted into `kb/notes/definitions/`, or the
   operator declines them with a recorded reason.
2. The research-program articles are given dispositions under the new ordering:
   autonomous reflective theory building is the learning target; software-house
   capability is a side conjecture.
3. The theory-refinement interface material is reconciled with the established
   theory-refinement literature without claiming the generic refinement loop,
   fallibility, or revision search as new.
4. Every artifact in the inventory below has a disposition: reframe, keep, or
   decline. Reframes are executed in their own commits, not in this workshop.

## Inventory of artifacts the reorder touches

The proposal names how each would change. Dispositions are recorded here as
they are decided.

| Artifact | Current head | Disposition |
|---|---|---|
| `kb/articles/automated-software-houses-with-fixed-llms.md` | software house first | open; side-conjecture candidate |
| `kb/articles/bootstrapping-the-first-automated-software-house.md` | software house first | open |
| `kb/articles/the-software-house-as-the-unit-of-training.md` | house is the trained unit; theory refinement is the mechanism | open; learning-paradigm framing should move to reflective theory builder |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | witness-house lens | open |
| `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | software-house consequence | keep as conditional side conjecture; wording still needs reconciliation |
| `kb/notes/definitions/theory-refinement.md` | genus definition; departures listed as form, then subject | reframed 2026-09-09: machinery is the first departure, form its consequence, subject independent |
| `kb/notes/definitions/software-house.md` | complete persistent producer | keep; no longer the head of the research program |
| `kb/notes/definitions/codification.md` | the natural-language to symbolic crossing | keep unchanged |
| `kb/notes/universal-software-factory-needs-a-declared-universality-axis.md` | four universality axes | keep; supplies the rule that *universal* needs a declared axis |
| `kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md` | house needs procedures per theory | open; useful machinery-gap analysis, but not every new family must require new code |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md` | carries a factory-to-house TODO | open |
| `kb/notes/broad-software-demands-create-pressure-for-agentic-factory-development.md` | carries a factory-to-house TODO | open |
| `kb/sources/goedel-machines-schmidhuber.ingest.md` | pinned to a `pdf-read` snapshot whose hash matches no existing file; page-based citations | open; no longer needed to establish a universal-manipulator limit |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | reads the machine as a change loop; carries "snapshot required" markers | open |

## Evaluation boundary

Evidence is the local KB at commit `c4ef2e2e` plus the two classical
theory-refinement ingests (EITHER, FORTE), and from 2026-09-09 the full-text
snapshot of the Gödel machine paper (arXiv cs/0309048 v5) under
`kb/sources/.snapshots/`. The 2026-09-10 reframing also uses the literature
check recorded in the operator session: fallible theories, generic theory
refinement, and search over candidate revisions are prior art. The workshop
therefore treats the autonomous reflective composition as the research target,
not those ingredients individually.

## Coordination

- [commonplace-nearest-constructions](../commonplace-nearest-constructions/README.md)
  already treats Commonplace as three objects, the first of which is "the
  human-inclusive theory builder operating today". The definition proposed
  here should become the shared term for that object; do not fork a second
  sense.
- [explanatory-theories-deployment-time-learning](../explanatory-theories-deployment-time-learning/README.md)
  owns the experiments on theory use inside an improvement loop. This
  workshop does not redesign them; it only names where they sit on the
  loop-closure axis.
- [operator-led-article-clarification](../operator-led-article-clarification/README.md)
  edits the three articles for readability. Reframing their heads is a content
  change and must not be mixed into clarification commits.
- The work index lists a `reachability-working-paper-publication` workshop
  whose directory no longer exists. Not this workshop's problem; noted so a
  later triage does not look for it here.

Write scope while open: this directory only. Library edits happen in separate
commits once a disposition is recorded above.
