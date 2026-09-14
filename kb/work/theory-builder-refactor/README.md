# Workshop: refactor the research program around the theory builder

## Goal

Refactor the research program around a new autonomous learning paradigm whose
learner is a **reflective theory builder**.

The builder's primary work is to develop and revise explicit, fallible theories
about externally supplied subjects. That work also tests the adequacy of the
builder's current theory-building machinery. When a failure is attributed to
that machinery, the builder can revise a theory of its own theory-building
organization and change the machinery used for later theory work.

The target is a theory builder of fallible theories, whose interpretive roles
are specified against a resource-bounded ideal interpreter, meeting two
independent conditions: **reflective** (it refines a theory of its own
theory-building machinery) and **autonomous** (every internal theory-building
role is computational, with the autonomy warranted by its evaluators).
Extension of the machinery is not a third condition; it is the quantity the
research question measures: under a stated budget, how far can the builder
extend its seed, and does retaining useful extensions make later advances
easier? Commonplace today is a reflective, non-autonomous instance; the
operator still performs diagnosis, admission, and successor selection.

Automatic theory refinement, fallible theories, and, in the Gödel machine,
reflection with autonomy and in-principle extension are prior art. The
proposed advance is the combination over fallible theories: external theory
work, reflective revision of the theory builder, and extension warranted by
evidence rather than proof, at a cost comparable to a human-staffed builder.

Whether sufficiently broad theory building requires the system to become a
[software house](../../notes/definitions/software-house.md) is now a side
conjecture, not a premise or load-bearing consequence of the learning paradigm.

## Operator direction

Commissioned by the operator on 2026-09-09; reframed on 2026-09-10 around
reflective theory building, with software-house capability a side conjecture.
On 2026-09-14 the operator directed that definitions come first, removed the
theory-family requirement, and made fixed models optional. The later
interpreter discussion replaced open-endedness as a separate condition with
the question of extension under a resource budget.

The current working abstraction idealizes faithful interpretation while
leaving conceptual development resource-dependent and fallible. The operator's
question is how far a builder can proceed beyond its available knowledge and
procedures, not merely whether it can produce a new result. The proposed
warrant closure of the seed remains contested. The most recent discussion
also distinguishes independence from axioms from algorithmic undecidability:
a builder may investigate new axioms without treating their adoption as a
proof from its previous assumptions.

The five definition drafts were rewritten in commit `991e5bf7`. They are the
current candidates, not accepted library definitions. This cleanup gives them
one reading order and records conflicts still requiring substantive review.

## Read the current definitions in this order

1. [Resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md)
   — faithful interpretation, attempted conceptual development, starting
   knowledge and procedures, and a computational budget.
2. [Fallible theory](./fallible-theory.md) — the current candidate account of
   warrant, retention, and revision. Its additional policy clauses require
   review before they can define fallibility generally.
3. [Theory builder](./theory-builder.md) — the persistent system, its boundary,
   seed, internal roles, and the proposed measure of extension.
4. [Reflective theory builder](./reflective-theory-builder.md) — revision of a
   causally connected theory of the builder's own machinery.
5. [Autonomous theory builder](./autonomous-theory-builder.md) — computational
   performance of every internal role; reliability remains separately assessed.

## Supporting work

- [Semantic work and the ideal interpreter](./semantic-work-and-the-ideal-interpreter.md)
  owns the semantic-work definition, rationale, mathematical stress tests,
  and unresolved specification questions. The separate interpreter file owns
  the current interpreter definition.
- [Gödel-machine comparison](./goedel-machine-comparison.md) owns the comparison
  of proof-governed switching with empirical theory-guided revision. Its
  cautions need reconciling with the stronger exclusions in the definitions.
- [Theory refinement as an interface](./theory-refinement-interface.md) owns
  the investigation of derive, compare, locate, revise, and evaluate. It
  requires reconciliation with the interpreter's role and established
  refinement literature before promotion.

## Earlier drafts and argument records

These files supply material to assess, not a second set of current definitions
or an edit plan to execute unchanged.

| File | Remaining use |
|---|---|
| [Warrant-bounded proposal](./proposal-warrant-bounded-open-endedness.md) | Argument record for the contested closure claim, evaluator revision, and the conjecture that reflection lowers search cost. Its old edit list is superseded. |
| [Original theory-builder proposal](./theory-builder-proposal.md) | Recover useful role mappings and discriminating cases; its theory-family and open-endedness framing is superseded. |
| [Universal theory manipulator](./universal-theory-manipulator.md) | Earlier formal limit case; assess whether anything is needed beyond the Gödel-machine comparison before retiring it. |
| [Interface note draft](./note-draft-theory-refinement-is-an-interface.md) | Candidate prose for the interface investigation; merge useful material into its eventual output rather than promote both accounts. |

## Next review: reconcile the definitions

The next pass should resolve these specific conflicts before expanding the
formalization or promoting definitions. The entries below identify review
questions; they do not silently adopt replacements for the current drafts.

| Issue | What must be resolved |
|---|---|
| Interpreter's scope and guarantees | The interpreter says budget exhaustion is its only failure, but conceptual development may fail and scope is conditional. Specify the guarantee for completed interpretation separately from discovery, and assess completion as well as fidelity so abstention cannot make evaluation vacuous. |
| Extension and model weights | The builder requires an artifact diff and excludes changes to existing slots, while both the builder and interpreter permit learning in weights. Define extension through demonstrated capability under a stated budget; settle how artifacts and probes establish the change. |
| Fallibility and warrant policy | Distinguish the property of being fallible from the proposed policy for retaining and consuming claims. The cited [warrant note](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) permits joint model or conjunction support. Check the draft's per-claim-only rule, always-untested-scope claim, and assertion that warranted revisions automatically chain. Distinguish actual warrant from an evaluator's judgment of it. |
| Objectives and closure | The autonomy draft infers that removing people prevents licensed objective change, while the comparison leaves this disputed. The [objective note](../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md) distinguishes an outside comparison level from the system boundary and reports no terminal-objective revision in Commonplace. Establish what follows before using seed closure as a definition premise. |
| Gödel-machine boundary cases | Reconcile the claim that its axioms are retained by proof and never revised against evidence with the comparison's account of observations and licensed axiom changes. Separate initial assumptions, proof-governed switching, and empirical adequacy; do not make an exclusion depend on unsupported impossibility claims. |

After that review, work through one bounded positive case and one failure
case using the semantic-work checks. Specify the starting repertoire, task,
budget, completed result, proposed extension, and grounds for retaining it.
Use existing work on belief revision, belief bases, truth maintenance, and
formal learning to check the proposed concepts before claiming novelty.
Source checks must distinguish convergence guarantees from current warrant.
The experiment workshop below continues to own comparative experiment design.

## What closes the workshop

1. The definitions of theory builder, reflective theory builder, autonomous
   theory builder, fallible theory, and resource-bounded ideal interpreter
   are accepted into `kb/notes/definitions/`, or the operator declines them
   with a recorded reason. Fallible theory needs the AGM and formal-learning
   ingests first, under closing condition 3.
2. The research-program articles are given dispositions under the new ordering:
   autonomous reflective theory building is the learning target; software-house
   capability is a side conjecture.
3. The theory-refinement interface material is reconciled with the established
   theory-refinement literature without claiming the generic refinement loop,
   fallibility, or revision search as new.
4. Every artifact in the inventory below has a disposition: reframe, keep, or
   decline. Reframes are executed in their own commits, not in this workshop.

## Inventory of artifacts the reorder touches

Dispositions are recorded here as they are decided. Earlier proposals supply
possible changes, not settled instructions for the library.

| Artifact | Current head | Disposition |
|---|---|---|
| `kb/articles/automated-software-houses-with-fixed-llms.md` | software house first | open; side-conjecture candidate |
| `kb/articles/bootstrapping-the-first-automated-software-house.md` | software house first | open |
| `kb/articles/the-software-house-as-the-unit-of-training.md` | house is the trained unit; theory refinement is the mechanism | open; learning-paradigm framing should move to reflective theory builder |
| `kb/articles/nearest-existing-constructions-to-a-witness-house.md` | witness-house lens | open |
| `kb/notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md` | software-house consequence | keep as conditional side conjecture; wording still needs reconciliation |
| `kb/notes/definitions/theory-refinement.md` | machinery departure, with remaining family wording | reframed 2026-09-09; second pass pending to align family wording with the accepted extension definition |
| `kb/notes/definitions/software-house.md` | complete persistent producer | keep; no longer the head of the research program |
| `kb/notes/definitions/codification.md` | the natural-language to symbolic crossing | keep unchanged |
| `kb/notes/universal-software-factory-needs-a-declared-universality-axis.md` | four universality axes | keep; supplies the rule that *universal* needs a declared axis |
| `kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md` | house needs procedures per theory | open; useful machinery-gap analysis, but not every new family must require new code |
| `kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md` | carries a factory-to-house TODO | open |
| `kb/notes/broad-software-demands-create-pressure-for-agentic-factory-development.md` | carries a factory-to-house TODO | open |
| `kb/sources/goedel-machines-schmidhuber.ingest.md` | pinned to a `pdf-read` snapshot whose hash matches no existing file; page-based citations | keep for the comparison; verify the retained snapshot and repair the ingest references before promotion |
| `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md` | reads the machine as a change loop; carries "snapshot required" markers | keep; resolve source markers and assess which formal limits transfer to the proposed builder |

## Evaluation boundary

Evidence is the local KB at commit `c4ef2e2e` plus the two classical
theory-refinement ingests (EITHER, FORTE), and from 2026-09-09 the full-text
snapshot of the Gödel machine paper (arXiv cs/0309048 v5) under
`kb/sources/.snapshots/`. The 2026-09-10 reframing also uses the literature
check recorded in the operator session: fallible theories, generic theory
refinement, and search over candidate revisions are prior art. The workshop
therefore treats the autonomous reflective composition as the research target,
not those ingredients individually. The 2026-09-14 semantic-work document
also records direct sources for the mathematical and logical stress tests.
The retained literature checks for the new definitions remain incomplete.

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

Write scope while open: this directory only. Library edits happen in separate
commits once a disposition is recorded above.
