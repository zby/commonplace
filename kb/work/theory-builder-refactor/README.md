# Workshop: refactor the research program around the theory builder

## Goal

Define a training methodology for an
[externally tested theory builder](./externally-tested-theory-builder.md).
Training develops its instructions, knowledge, tools, and orchestration as
natural-language and symbolic artifacts while model weights stay fixed.
Commonplace producing a KB and supporting software for consuming projects
is the proposed first arrangement. Downstream outcomes assess the main
claim; internal approval of a note does not substitute for that assessment.

The conjecture has two separately testable parts. This is the working
framing used to implement the [main-path plan](./main-path-plan.md), pending
adoption of the workshop conclusions.

> **Sufficiency hypothesis.** A training methodology expressed in
> natural-language and symbolic form is
> [actionable](../../notes/definitions/actionable-methodology.md) for a
> computational operator using fixed weights from currently public models.
> Without people performing its internal theory-building roles or designing
> a new learning method for each area, the builder develops, retains, and
> uses theories and procedures across declared practical areas. Its later
> work meets a reliability target under a stated budget and external
> assessment protocol. An area is a consuming project's domain with an
> interface that can be declared and observed.

> **Comparative hypothesis.** Under matched demands and declared resources,
> this methodology produces useful capability gains over the frozen seed
> and a baseline that searches the raw records without the learned
> methodology. Its downstream reliability is comparable to a human-staffed
> builder's under a margin set before assessment. The computational
> comparisons use the same fixed-model constraint and account for both
> adaptation and task costs.

> **Reflection hypothesis.** A builder whose machinery changes pass through
> a causally connected self-theory acquires extensions that a matched
> builder without one does not, under the same demands, budget, and
> external assessment. Better downstream outcomes alone do not test this;
> the records of a [reflective episode](./main-path-episodes.md#2-reflective-machinery-revision)
> and a matched builder that retains content without a self-theory do.

None of the hypotheses promises success on every problem or within every
budget. The [protocol](./commonplace-evidence-protocol.md) records the
project, reliability target, comparison margin, task population, and budgets
that must be fixed before a run. No run is reported here. A result on one
project supports that assessed scope; breadth requires multiple declared
areas and evidence about transfer between them.

For this conjecture, “currently publicly available” means available as of
2026-09-17. An assessment must declare the model versions it uses and keep
their weights fixed. Public availability includes hosted models; it does not
require open weights. Model-weight updates and later model releases are
excluded from the assessment. The particular models remain to be selected;
this is a constraint on the research target, not on the general definition
of a theory builder.

The unit being trained is the theory builder. Its learned changes are
retained in instructions, knowledge, tools, and orchestration, in
natural-language and symbolic
[representational forms](../../notes/definitions/representational-form.md).
The methodology governs how experience and evaluation produce these changes
and how their effect on later work is assessed. This is the training process
the workshop aims to define; fixed model weights constrain where learning is
retained. Both the methodology and its learned results have these artifact
forms, and the methodology itself can be revised through this process.

Doctrine edits per new area, with authorship and cost, are a diagnostic of
automated continuation. A human supplying an internal role counts as an
intervention during that run. Neither a low edit count nor a machine-written
change establishes useful learning. Outcome comparisons, retained changes,
and later consumption must establish
[extension](./theory-builder.md#extension). *Methodology* names the content;
*Commonplace doctrine* names the standing instructions a worker inherits with
binding force.

The system that executes the methodology is a
[theory builder](./theory-builder.md) of
[tentative theories](./tentative-theory.md).
[Autonomy](./autonomous-theory-builder.md) concerns who performs its internal
roles. [Reflection](./reflective-theory-builder.md) is a separate mechanism
condition: a causally connected self-theory guides machinery changes, and
the changes update that theory. Whether that mechanism pays is the
reflection hypothesis above. The research target requires both conditions;
the reflective episode's records supply the evidence that the path is
exercised.

The work combines specification with bootstrap through use. Declare the
evidence interface and comparison first, then let substantive tasks expose
product and machinery problems. Retained changes are assessed on later
work. Internal diagnosis and targeted experiments remain in this path;
their cost and evidence exposure are recorded. An
[ideal interpreter](./resource-bounded-ideal-interpreter.md) is no longer a
prerequisite of the outcome comparison. Its proposed attribution guarantees
remain open.

Commonplace today is the human-inclusive starting system, not an autonomous
instance demonstrated under the proposed protocol. This repository's
instructions, collection contracts, type specs, review system, and skills
supply its seed methodology. The
[boundary assessment](./boundary-case-assessment.md) separates prior systems'
reported evaluations from claims about persistence, reflection, and external
assessment that their evidence does not settle. The research concerns the
methodology's composition and performance, not novelty of generic theory
refinement or tentative theories.

Whether sufficiently broad theory building requires the system to become a
[software house](../../notes/definitions/software-house.md) remains a side
conjecture, not a premise or load-bearing consequence.

The software-house articles supply the main-path case and its witness
protocol. The general definitions and
[general-case obligations](./general-case-obligations.md) remain because
external outcomes do not warrant every internal theory or use beyond the
assessed scope. These obligations concern particular claims and uses;
reasoning about a failure does not move the whole builder outside the main
path.

## Operator direction

Commissioned by the operator on 2026-09-09; reframed on 2026-09-10 around
reflective theory building, with software-house capability a side conjecture.
On 2026-09-14 the operator directed that definitions come first, removed the
theory-family requirement, and made fixed models optional. The later
interpreter discussion replaced open-endedness as a separate condition with
the question of extension under a resource budget.

The 2026-09-14 working abstraction idealized faithful interpretation while
leaving conceptual development resource-dependent and fallible. The operator's
question is how far a builder can proceed beyond its available knowledge and
procedures, not merely whether it can produce a new result. The proposed
warrant closure of the seed remains contested. The most recent discussion
also distinguishes independence from axioms from algorithmic undecidability:
a builder may investigate new axioms without treating their adoption as a
proof from its previous assumptions.

The five definition drafts were rewritten in commit `991e5bf7`. They remained
workshop candidates; the main-path implementation below supersedes that
version of the drafts without promoting them to library definitions.

Later on 2026-09-14, after a parallel session reframed the target as a
broadly applicable learning methodology in natural-language and symbolic
form, the operator directed that the workshop goal be revised first. The
goal then stated the conjecture, its two rivals, its empirical measure, and
the two development routes; the definitions are its vocabulary, and
reflection and extension are its mechanisms rather than its target.

On 2026-09-15 the operator asked why the workshop grew more complicated than
the articles. The finding: the articles' software house has an evidence
interface that supplies the falsifier, the objective, and an independent
outcome level. The corresponding general obligations now sit in the
retention-policy draft, its objective clause, and the ideal interpreter. The operator
directed that the general case be kept, because it shows the difficulties,
and a special case added for the simplified situation. That special case is
the externally tested theory builder.

Also on 2026-09-15 the operator supplied an external literature review of
the reframing and asked for an independent judgement and an ingest list. The
[ingest plan](./ingest-plan-from-astra-review.md) records both. Its three
proposals for the conjecture (split sufficiency from comparison, demote the
doctrine-edit count to a diagnostic, remove the Gödel-machine exclusions and
closure claims from the definitions) were initially left unapplied. The
main-path implementation below now uses them as its working framing. On
2026-09-17, all fifteen listed sources were ingested. The
operator supplied Hansson's full-text PDF to resolve the final access
blocker. The ingest plan links all reports. The source inputs for the
definitions review below are ready.

Also on 2026-09-17, the operator asked to add Thórisson's seed-programming
paper and Nivel et al.'s bounded recursive self-improvement paper after both
were ingested. The [additional source record](./ingest-plan-from-astra-review.md#additional-seed-learning-sources--2026-09-17)
links their reports and identifies questions for the seed, reflection,
autonomy, and extension review. Adding these inputs does not adopt the
definition changes proposed during the search.

Later on 2026-09-17, the operator constrained the central question to weights
pinned to currently public models. The goal above applies that constraint to
the research target, superseding the earlier optional treatment there. The
general definitions still admit builders that change weights.
The operator then clarified that the purpose is to define a new training
methodology: training changes instructions, knowledge, tools, and
orchestration in natural-language and symbolic artifacts. The fixed-weight
constraint excludes model-weight updates, not training of the builder.

The operator then selected **tentative theory**, Popper's established term,
for use throughout this workshop. The [vocabulary entry](./tentative-theory.md)
uses the retained schema passage and the newly ingested full
[*Conjectures and Refutations*](../../sources/popper-conjectures-and-refutations.ingest.md#quotes).
The [retention-policy draft](./theory-retention-policy.md) now owns the
proposed conditions on reliance, objective preservation, and revision
sequences; these are not clauses defining tentativeness. The broader
conclusions remain under review. The
[KB adoption plan](./tentative-theory-kb-adoption-plan.md) schedules the
terminology change outside this workshop only after those conclusions are
adopted.

On 2026-09-17 the operator authorized revision and implementation of the
[main-path plan](./main-path-plan.md). The implementation puts external
assessment first, keeps internal investigation and active probes within that
path, and separates outcome evidence from attribution. The working conjecture
splits sufficiency from comparison, treats doctrine edits as a diagnostic,
and keeps reflection separate from extension. These drafting choices make
the proposal reviewable; library adoption remains a later step. The first
consuming project remains unselected. The
[implementation review](./implementation-review.md) records the seven review
outcomes, artifact dispositions, and the unresolved refinement-interface
closing condition.

Later on 2026-09-17 the operator supplied an external review (ChatGPT) of
the published workshop and adopted two of its recommendations: reflection
is stated as a subordinate falsifiable hypothesis beside sufficiency and
comparison, and the theory-refinement definition's stipulation that the
three loop properties define *theory* is narrowed at promotion to what
refinement requires of a theory's representation, with *addressable theory*
naming a theory that supplies them (recorded in the
[adoption plan](./tentative-theory-kb-adoption-plan.md#1-establish-the-durable-vocabulary-destination)).
The review's other points were already applied by the main-path
implementation, or declined: autonomy stays inside the head conjecture,
since separating it would make the conjecture true of Commonplace today.

## Read the current definitions in this order

1. [Theory builder](./theory-builder.md) — persistent responsibility, the
   boundary and seed, declared evidence interface, and capability extension.
2. [Externally tested theory builder](./externally-tested-theory-builder.md)
   — the main path, scoped external assessment, and its limits. Read the
   [Commonplace protocol](./commonplace-evidence-protocol.md) and
   [three constructed episodes](./main-path-episodes.md) for the proposed case.
3. [Reflective theory builder](./reflective-theory-builder.md) and
   [autonomous theory builder](./autonomous-theory-builder.md) — separate
   causal and role conditions; neither alone establishes improvement.
4. [Tentative theory](./tentative-theory.md) — Popper's borrowed term. The
   [retention-policy draft](./theory-retention-policy.md) separately owns
   proposed conditions on support and use.
5. [General-case obligations](./general-case-obligations.md) — what remains
   to establish when a particular claim or use lacks external assessment.
6. [Resource-bounded ideal interpreter](./resource-bounded-ideal-interpreter.md)
   — a deferred attribution specification with open fidelity, completion,
   abstention, and realizability questions.

## Supporting work

- [Main-path plan](./main-path-plan.md) records the authorized sequence and
  its completion state. The [implementation review](./implementation-review.md)
  owns the final review dispositions and remaining promotion conditions.
- [Commonplace evidence protocol](./commonplace-evidence-protocol.md) owns
  the proposed downstream comparison, records, and unfilled study parameters.
  [Main-path episodes](./main-path-episodes.md) check the concepts against
  constructed product repair, machinery repair, and unsupported broader use.
- [Boundary-case assessment](./boundary-case-assessment.md) separates each
  deployment's boundary, reported judging, evidence access, and continuing
  responsibility, with verified source identities and access limits.
- [Theory retention and use](./theory-retention-policy.md) owns the policy
  questions separated from the borrowed vocabulary, including objective
  preservation and warrant for revision sequences.
- [KB adoption plan](./tentative-theory-kb-adoption-plan.md) owns the later
  terminology migration, its adoption trigger, candidate inventory, source
  fidelity exceptions, and validation requirements.
- [Semantic work and the ideal interpreter](./semantic-work-and-the-ideal-interpreter.md)
  owns the semantic-work definition, rationale, mathematical stress tests,
  and unresolved specification questions. The separate interpreter file owns
  the current deferred specification.
- [Gödel-machine comparison](./goedel-machine-comparison.md) owns the comparison
  of proof-governed switching with empirical theory-guided revision. Its
  cautions inform the deployment-specific boundary assessment; its argument
  record is not an independent deployment result.
- [Theory refinement as an interface](./theory-refinement-interface.md) owns
  the investigation of derive, compare, locate, revise, and evaluate. It
  requires reconciliation with the interpreter's role and established
  refinement literature before promotion.
- [Ingest plan from the Astra review](./ingest-plan-from-astra-review.md)
  owns the judgement of the external literature review and the prioritized
  source list and ingest status: introspective multistrategy learning, EURISKO,
  adaptive data analysis, problem-solving-method construction, automated
  science, belief bases, and the contemporary rivals. Its additional-source
  section records the later seed-programming and bounded self-improvement
  ingests and their workshop review questions.

## Earlier drafts and argument records

These files supply material to assess, not a second set of current definitions
or an edit plan to execute unchanged.

| File | Remaining use |
|---|---|
| [Warrant-bounded proposal](./proposal-warrant-bounded-open-endedness.md) | Argument record for the contested closure claim, evaluator revision, and the conjecture that reflection lowers search cost. The retention policy points here for the closure argument; it stays until that claim has a disposition. |

The original theory-builder proposal, the universal theory manipulator, and
the interface note draft were retired in the 2026-09-17 cleanup: their
role mappings and discriminating cases are absorbed into the boundary rule
and the boundary-case assessment, the Gödel-machine comparison carries the
proof-governed contrast, and the interface investigation is the single
account for closing condition 3. All three remain in git history.

## Definition review dispositions

The main-path implementation reviewed all seven issues. Details and evidence
limits are in the [implementation review](./implementation-review.md#seven-review-rows).
A revised criterion is a design decision, not proof that a builder meets it.

| Issue | Current disposition |
|---|---|
| Interpreter's scope and guarantees | Deferred from the outcome comparison; scoped specification revised, fidelity and completion questions open. |
| Seed and bootstrap claims | Open empirical question; frozen-seed comparison specified, no run performed. |
| Extension and model weights | Capability criterion revised with budgets, seed comparison, retention, and later consumption; demonstrations pending. Fixed weights constrain this research target only. |
| Tentative status and retention policy | Vocabulary separation complete; support thresholds, joint support, and adaptive revision-sequence questions remain in the policy draft. |
| Objectives and closure | Autonomy no longer determines objective governance. Seed closure is not a premise; objective preservation and proxy validity remain obligations in the main path. |
| Evidence interface | Declaration and proposed protocol implemented; first consuming-project observation pending. |
| Gödel-machine boundary cases | Categorical exclusions removed; source-specific assessment recorded, deployed qualification remains open. |

The [three episodes](./main-path-episodes.md) check the distinctions against
specified repertoires, tasks, budgets, feedback, and candidate results. They
are constructed cases. The refinement-interface investigation remains open;
its task-level descriptions must be separated from implementation guarantees
before promotion. The experiment workshop below continues to own its
component-comparison design.

## What closes the workshop

1. The definitions of theory builder, reflective theory builder, autonomous
   theory builder, resource-bounded ideal interpreter, and externally tested
   theory builder, together with the borrowed tentative-theory vocabulary,
   receive library destinations or are declined with a recorded reason.
   The vocabulary may be a short section of theory refinement rather than a
   separate definition. Retention-policy obligations receive explicit
   dispositions informed by the completed ingests; none are promoted merely
   by accepting the term.
2. The research-program articles are given dispositions under the new ordering:
   the learning-methodology conjecture is the head of the program, the theory
   builder is the system that executes it, and the software house supplies
   the chosen externally assessed case. Whether other broad builders must
   become software houses remains a side conjecture.
3. The theory-refinement interface material is reconciled with the established
   theory-refinement literature without claiming the generic refinement loop,
   fallibility, or revision search as new.
4. Every artifact in the linked inventory has a disposition: reframe, keep, or
   decline. Reframes are executed in their own commits, not in this workshop.
5. After adoption, execute the [KB terminology plan](./tentative-theory-kb-adoption-plan.md)
   and record its changed files and justified exceptions in the migration
   commits before closing this workshop.

## Inventory of artifacts the reorder touches

The [implementation review's inventory](./implementation-review.md#inventory-dispositions)
records dispositions for all fourteen artifacts. It keeps the software-house
articles as the chosen case and bootstrap route, preserves the general
conditional side conjecture, and bounds the later reframes to actual
whole-producer terminology. The source check resolves the old Gödel snapshot
identity warning; deployment classification is a separate open question.

These dispositions do not by themselves execute library reframes. The
[adoption plan](./tentative-theory-kb-adoption-plan.md) controls the later
terminology migration, including source wording and provenance exceptions.

## Evaluation boundary

Evidence is the local KB at commit `c4ef2e2e` plus the two classical
theory-refinement ingests (EITHER, FORTE), and from 2026-09-09 the full-text
snapshot of the Gödel machine paper (arXiv cs/0309048 v5) under
`kb/sources/.snapshots/`. The 2026-09-10 reframing also uses the literature
check recorded in the operator session: tentative theories, generic theory
refinement, and search over candidate revisions are prior art. The workshop
therefore treats the autonomous reflective composition as the research target,
not those ingredients individually. The 2026-09-14 semantic-work document
also records direct sources for the mathematical and logical stress tests.
The retained evidence now also includes the fifteen completed ingests and
the two seed-learning ingests linked in the [source record](./ingest-plan-from-astra-review.md).
The main-path review uses these sources with the limits recorded in the
[boundary assessment](./boundary-case-assessment.md). Further source checks
remain necessary for the internal refinement-interface investigation.
The tentative-theory entry also uses the Popper 1966 essay's retained schema
and the full-book ingest of *Conjectures and Refutations*. Retained passages
in the latter support provisional acceptance, continuing tentativeness, and
the limits of fault localization.

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
commits after the conclusions and destinations are adopted, using the
recorded dispositions. The operator's 2026-09-17
grounding request additionally authorizes the bounded quote append in the
Popper ingest; it does not start the wider terminology migration.
