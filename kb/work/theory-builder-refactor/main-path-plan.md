# Main-path plan: put the definitions on the externally tested case

> **Status:** Workshop plan, 2026-09-17, revised the same day after Astra's
> review ([mailbox request](../../messages/20260917T122132Z-astra-fable-main-path-plan-revisions.md)).
> The tentative-theory rename is committed as `b7520224`, so the earlier
> waiting condition is cleared. The revision reorders the work so the
> concrete Commonplace case tests the definitions before their rewrite is
> committed, makes the boundary about external assessment rather than about
> who investigates, replaces renewal-as-guarantee with an evaluation
> protocol, and keeps deferred questions marked open. The operator authorized
> revision and implementation on 2026-09-17. Steps 1 and 2 may create workshop
> drafts; edits to the existing definitions follow their episode checks.
> Steps 1–6 are now implemented as workshop drafts and assessments. Library
> promotion uses only adopted conclusions, as specified in step 7; no
> consuming-project run or workshop closure is claimed.

## Purpose

Concentrate the research program on one main path, the
[externally tested theory builder](./externally-tested-theory-builder.md),
and keep the general case as a boundary that tells an agent when a claim has
left the main path. The operator chose this on 2026-09-17 after the
definitions review found that the general definitions exist to replace what
the special case's evidence interface supplies from outside.

The selected [ingests](./ingest-plan-from-astra-review.md) provide examples
and limits, not a general theorem about successful systems. Benchmark studies
can assess outcomes without establishing the truth of their internal
explanations; architecture papers such as AutoRA specify evidence acquisition
without evaluating every deployment. The main path is chosen because its
outcomes can be assessed outside the builder and compared with a
human-staffed builder under declared conditions.

## Decisions this plan applies

Operator direction of 2026-09-17, in the order given:

1. The externally tested theory builder is the main path. The general case
   is kept as a fence: a list of what a builder must supply for itself when
   a claim lacks external assessment, with open questions marked open.
2. The workshop uses Popper's tentative theory as a borrowed
   term, with the structure left in the theory-refinement definition and
   the policy clauses moved to
   [theory retention and use](./theory-retention-policy.md). Done in
   `b7520224`. The later library migration follows the
   [KB adoption plan](./tentative-theory-kb-adoption-plan.md), which
   preserves source wording and provenance.
3. Commonplace's product is a knowledge base built for consuming projects.
   Commonplace is then a [software house](../../notes/definitions/software-house.md)
   whose product is its KB and supporting software, and its evidence
   interface is that product's use.

The research target's fixed model weights remain a constraint on the
target, not on the general definitions, which still admit weight learning.

### Where the boundary sits

The fence is about who warrants an outcome, not about who investigates.
Diagnosing an evaluator or retrieval failure, constructing a hypothesis
about the builder's own machinery, choosing an experiment, or requesting a
user test all stay inside the main path while the consequences of the
resulting change still face the declared external assessment. That
reflective work is the mechanism the research program investigates, and it
must not be sent outside by definition. A claim leaves the main path when
the claim being made has no external assessment of its consequences, for
example a methodology note retained on the builder's own judgment of its
worth. Active versus passive evidence acquisition is a separate dimension of
the interface, recorded as a field, not a boundary.

The operator's remark that the system "does not need to make open-ended
experiments" is read here as an experiment constraint, to be stated in the
first evaluation's protocol if a passive stream is chosen, not as a
definitional exclusion of active testing. If the operator intended the
stronger reading, this is the place to say so.

## Decisions still open

The implementation uses separate sufficiency and comparative hypotheses,
doctrine-edit counts as a diagnostic, and reflection as a separate
condition. These are the working choices used to make the revised proposal
reviewable, not a claim that the workshop conclusions have been adopted for
the library. The [README](./README.md#goal) states the resulting hypotheses.
The definition changes remove categorical Gödel-machine exclusions and do
not assume seed closure.

The first consuming project, exact models, budgets, task population,
reliability target, comparison margin, and horizon remain run choices.
Their absence blocks a scored evaluation, not protocol drafting. The
[Commonplace protocol](./commonplace-evidence-protocol.md) records them.
Reflection remains a causal mechanism claim requiring its own evidence;
a retained prompt or successful agent program does not by itself establish
or refute a two-way self-theory connection.

Library destinations and conclusions await adoption under step 7. The
refinement-interface closing condition remains open even after the workshop
implementation below.

## Implementation state

| Step | Result |
|---|---|
| 1. Observable Commonplace protocol | [Drafted](./commonplace-evidence-protocol.md); run parameters explicit and unfilled. |
| 2. Episodes | [Three constructed cases](./main-path-episodes.md); no empirical results. |
| 3. Definitions and general-case obligations | Five drafts revised against the episodes; [general obligations](./general-case-obligations.md) separated by claim and use. |
| 4. Boundary cases | [Eleven cases assessed](./boundary-case-assessment.md), with primary-source checks and access limits. |
| 5. Conjecture | [Working hypotheses restated](./README.md#goal); sufficiency, comparison, and reflection evidence separated. |
| 6. Review and inventory | [Seven review rows and fourteen artifact dispositions](./implementation-review.md) recorded. |
| 7. Promotion and migration | Conditional on adoption; not executed. Workshop closure also requires condition 3 to be satisfied or explicitly revised. |

The steps below record the implementation requirements and their remaining
conditions. The implementation review owns the final dispositions where an
early candidate change was narrowed by the episodes or source checks.

## Step 1: draft the Commonplace arrangement as an observable protocol

New workshop file. Judgment work; not delegated. Declaring an interface does
not establish that it exists, so the draft specifies an arrangement someone
could observe, with each field either filled or marked as depending on the
consuming project.

- **Product:** the KB delivered to the consuming project, at a named
  version, with its validators, skills, and indexes.
- **Tasks and judges:** who supplies the tasks, who judges outputs, and
  what they see. Judges assess outputs against the task contract; they may
  inspect evidence the task requires. The same person as the Commonplace
  operator is permitted while that act stays distinct from judging a note.
  A different judge reduces role ambiguity without guaranteeing unbiased
  or statistically independent assessment.
- **Evidence of consumption:** what shows the consumer's agents used the KB
  on a task, since a task can succeed or fail without the KB being
  consulted. This is part of the protocol, not a later caveat.
- **Feedback channel:** what returns to the builder, in what form, and how
  long after the task.
- **Evaluation protocol**, per the
  [adaptive-data-analysis ingest](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md):
  how tasks are sampled, which feedback revision may consume, what is
  reserved for assessment and never fed back, and what population and
  horizon the claim covers. Renewal of the task stream is one contribution
  to this protocol and is recorded as a property; it is not a substitute for
  the protocol, because new users can accept the same misleading proxy and
  a changing task mix can move the apparent score. A final reserved
  assessment remains untouched until the tested candidate
  is frozen. Adaptive reuse instead requires a specified information-release
  protocol, sampling assumptions, and enforced budget; a budget declaration
  alone supplies no validity guarantee.
  Binary feedback does not by itself transfer the paper's guarantees to
  arbitrary streams of user judgments.
- **Outcome versus attribution.** A rejected output is a failure of the
  combined task, consumer, and KB arrangement. It does not falsify a
  particular note or show the KB made the result worse. Any claim that the
  KB caused a difference uses matched interventions, the same task with and
  without the KB or across KB versions, with task, consumer, and resource
  conditions held comparable. Attribution to a note, and then to the
  methodology that produced the note, are two further steps, each needing
  its own evidence; the
  [training article](../../articles/the-software-house-as-the-unit-of-training.md)
  owns the second.

Record two inventory consequences. The
[side conjecture](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
is unnecessary as a premise of this experiment, because Commonplace is taken
as a software house from the start; its general conditional claim about
other theory builders is untouched, and its disposition is keep on that
basis. The
[bootstrapping article](../../articles/bootstrapping-the-first-automated-software-house.md)
describes the seed of this house, so its disposition is keep.

## Step 2: draft the episodes

Same file or a companion. Three episodes, each stated with starting
repertoire, task, budget, what came back through the interface, what the
builder did, and what would count as the episode's result.

1. **Product revision.** Operation contradicts a product theory in the KB;
   the builder locates and revises it; later tasks test the revision under
   the protocol.
2. **Reflective revision.** External work exposes a machinery problem, for
   example retrieval never surfacing the relevant note. The builder revises
   its self-theory, that revision guides a machinery change, and subsequent
   external work tests the change. Matched interventions on the retained
   commitment strengthen the causal attribution but do not replace the
   [reflective definition's](./reflective-theory-builder.md) two-way
   connection; both are required. This episode is inside the main path.
3. **A claim that leaves the main path.** The builder retains a methodology
   note whose consequences never face the interface, on its own judgment of
   the note's worth. The episode shows what the fence should make the
   builder say, and which general-case obligation it has taken on.

## Step 3: revise the definitions against the episodes

Only after steps 1 and 2. The edits below are candidates to test against the
episodes, not settled worker tasks; any that the episodes do not support is
dropped or changed here first. One commit when settled.

**theory-builder.md**

- Add an *Evidence interface* section beside the boundary and the seed: a
  declared parameter of every builder, with the fields of step 1 plus
  whether acquisition is passive or active. Declare it as competence plus
  applicability assumptions, per the
  [knowledge-engineering ingest](../../sources/knowledge-engineering-principles-and-methods.ingest.md),
  and as a first-class artifact, per the
  [UPML ingest](../../sources/upml-framework-for-knowledge-system-reuse.ingest.md).
- Replace the extension section with one criterion: an extension is
  capability the seed's machinery did not deliver on a stated demand under
  a stated budget, shown against a comparable seed baseline under that
  budget, and evidenced by a later episode that consumed it. A seed failure
  on one run followed by a success does not establish it. This is a bounded
  comparative claim; it does not prove the seed could not have done it.
  Drop the artifact-diff rule and the exclusion of changes to existing
  slots; the [GEPA ingest](../../sources/gepa-reflective-prompt-evolution.ingest.md)
  reports performance gains through revisions to existing prompt slots.
  This motivates permitting such revisions; it does not prove an absolute
  limit of the seed. Weight changes face the same capability criterion,
  assessed through probes of their effects.
- Leave the Gödel-machine classification under review, as `b7520224`
  records. Do not replace the theory-clause exclusion with a categorical
  exclusion based on where utility is represented; step 4 assesses it.

**externally-tested-theory-builder.md**

- Keep the three supplied items. Add that an evaluation in the main path
  declares the interface fields and the evaluation protocol of step 1.
  Renewal is recorded as an interface property that contributes to the
  protocol. Remove any inference that new tasks or real users absorb the
  objective-preservation problem; the retention policy's
  [objective clause](./theory-retention-policy.md#the-objective-clause)
  still applies, and the marker-deletion example motivates checking
  objective preservation, not a claim that users would catch it.
- Record active acquisition as a field, not as a departure from the main
  path.
- Split the Commonplace boundary case in two. Commonplace consuming its own
  methodology is not externally tested, for the reasons the current case
  gives. Commonplace as a house whose product is a KB is a candidate for the
  main path under the step 1 protocol, and becomes an instance when that
  protocol is observed.
- Rewrite the Darwin Gödel Machine case to distinguish an experiment's
  limited horizon from invalid evaluation. Use the
  [DGM ingest](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
  to distinguish staged within-benchmark search from untouched cross-benchmark
  transfer; use ADAS only for its own evaluation. Adaptive overfitting is a
  concern requiring a protocol, not a reported degradation in ADAS.

**autonomous-theory-builder.md**

- Remove the *The objective* section. Its content already lives in the
  retention policy's objective clause, which states that what supplies the
  comparison level depends on the evidence interface and does not follow
  from autonomy alone. The
  [AERA ingest](../../sources/bounded-recursive-self-improvement.ingest.md)
  is the case showing a protected objective is a design choice; it does
  not by itself decide AERA's outcome-assessment boundary.

**reflective-theory-builder.md**

- Add the evidence standard from episode 2: an episode in which external
  work exposes a machinery problem, the self-theory is revised, the
  revision guides a machinery change, and later external work tests it,
  with matched interventions strengthening attribution. Keep the
  definition's causal requirements beside it.

**resource-bounded-ideal-interpreter.md**

- Move it out of the main-path comparison: in the main path an
  interpretation error and a theory error can each cause a failed product,
  and the outcome comparison does not need the split. This is a deferral,
  not a resolution. Interpreter fidelity, completion versus abstention, and
  the guarantee for completed interpretation stay open questions listed in
  the fence. Replace "budget exhaustion is the only failure" with a class
  declaration in the style of the
  [bounded-optimality ingest](../../sources/provably-bounded-optimal-agents.ingest.md):
  program language, architecture, objective, environment class, resource
  model, horizon. The
  [semantic-work record](./semantic-work-and-the-ideal-interpreter.md)
  stays as the argument record.

**New: general-case-obligations.md** (the fence)

One document listing what a builder must supply for itself when a claim
lacks external assessment, each with the drafts and ingests that bear on it
and its open questions marked open:

1. A rule for what counts as a contradiction and what support licenses each
   use. Owner: [theory-retention-policy.md](./theory-retention-policy.md).
2. A comparison level for an objective change when no acceptance arrives
   from outside. Owners: the retention policy's objective clause and the
   [Gödel-machine comparison](./goedel-machine-comparison.md).
3. Attribution of a failure between interpreting a theory and the theory.
   Owner: the interpreter, with its open fidelity questions.

Plus the fence rule: a claim whose consequences do not face the declared
external assessment has left the main path and must say so. It does not
thereby become wrong; it takes on the corresponding obligation and its
unresolved questions. Reasoning about a failure, choosing what to test, or
revising the self-theory does not by itself cross the fence.

**README.md**

- Operator-direction entry for the three decisions and the boundary
  reading above.
- Reading order: theory builder, externally tested theory builder, the two
  conditions, tentative theory with the retention policy, the fence, the
  interpreter as argument record.
- The review table keeps all seven rows. Step 6 gives each a disposition.

## Step 4: reassess the boundary cases

After step 3. Replace the earlier expected-verdict table with an assessment
per case, answering four questions separately, because fixed objectives,
internal utility representations, designer-supplied criteria, and external
outcome assessment are not interchangeable, and the same architecture can
occupy different positions in different deployments:

1. What is the declared system boundary in the deployment described?
2. What evaluation was observed, and who judged it?
3. What evidence did the system have access to, and under what protocol?
4. Does the system hold continuing responsibility for the theories?

The [completed assessment](./boundary-case-assessment.md) replaces the
provisional verdict table. It distinguishes AERA's S1 experiment from
Thórisson's general proposal and separates Commonplace's note review from
the proposed downstream house. In particular:

- FORTE's retained quotations establish its supplied-example task; the
  absent paired snapshot prevents checking the broader experimental account.
- The Gödel snapshot identity is verified, while deployment classification
  remains open. A formal construction is not an observed outcome study.
- DGM's staged search and untouched cross-benchmark transfer support
  different claims. ADAS's ARC test-based selection must not be described
  as untouched assessment for every comparison.
- Meta-AQUA retains and repairs knowledge across stories within a run;
  finite duration does not erase that responsibility. GEPA's principal
  study and its target-task kernel-search extension have different protocols.

Acceptance: every row answers the four questions from the deployment's
evidence, and no row rests on a categorical property alone. Unknown or
unavailable evidence stays explicit.

## Step 5: restate the conjecture

The [README](./README.md#goal) now states sufficiency and comparison
separately. It scopes an area to a consuming project's domain with an
interface that can be declared and observed. Doctrine edits, authorship, and
internal interventions diagnose automated continuation; outcomes and costs
assess the hypotheses. Reflection stays a separate mechanism claim. These
are working draft choices for later adoption, not experimental findings.

## Step 6: review dispositions

The [implementation review](./implementation-review.md#seven-review-rows)
records all seven dispositions. The interpreter is deferred from outcome
comparison; seed capability and bootstrap remain empirical questions;
extension and evidence-interface criteria are revised without claiming they
have been met. Tentative status is separated from policy. Autonomy does not
determine objective governance, and objective preservation remains inside
the main path. Gödel-machine classification remains deployment-dependent.

These distinctions replace the earlier expected-verdict table. A completed
specification, a resolved conceptual conflict, and evidence of successful
operation are reported separately.

Closing condition 3, the theory-refinement interface material, is not
satisfied by declaring the interface or citing AutoRA's role split. The
[refinement-interface investigation](./theory-refinement-interface.md)
concerns how derive, compare, locate, revise, and evaluate work and which
classical results transfer; that stays open and is not moved into the fence.

## Step 7: promotion, dispositions, migration

After the operator adopts their conclusions and destinations, promote
theory builder, externally tested theory builder, and the two conditions
into `kb/notes/definitions/`; tentative theory to the destination the
[adoption plan](./tentative-theory-kb-adoption-plan.md) settles, which may
be a section of theory refinement; the fence as a note. Then the inventory
dispositions: the three software-house articles are the main path; the
side conjecture and bootstrapping article keep, per step 1; the universal
theory manipulator and the original proposal retire. Then execute the
adoption plan's migration, preserving source wording, verbatim occasions,
and provenance as it requires, and record the outcome in the migration
commits before closing. Promotion and migration follow the adoption plan's
explicit trigger. Close the workshop only when its closing conditions are
satisfied or the operator explicitly revises them; leaving condition 3 open
does not count as satisfying it. Implementation authorization permits the
workshop drafts and reviews without turning untested claims into results.

## Execution notes

- **Ordering.** Steps 1 and 2 first, in the main session. Step 3 only after
  the episodes exist. Source checks for step 4 can run alongside per-file
  drafting; integrate the assessments against the revised definitions before
  steps 5 and 6. Step 7 retains its adoption condition.
- **Workers.** No workers until step 3 is settled. Then per-file edits may
  go to fresh workers with this plan and the episodes as the handoff; the
  fence document and the README stay in the main session.
- **Verification.** `commonplace-validate` on each exact changed path; the
  installed validator does not accept a bare workshop subdirectory as a
  target. `git diff --check`. No pytest: Markdown only.
- **Commits.** Plan, protocol, and episodes together; the five definition
  revisions with the boundary assessment and general-case obligations; then
  the README and implementation review. Use
  `Workshop: kb/work/theory-builder-refactor`. No amends; other sessions
  commit concurrently.
- **Write scope.** This directory only until step 7.
