# Commonplace's downstream evidence protocol

> **Status:** Proposed evaluation protocol, 2026-09-17. Tests the
> [adopted hypotheses](./README.md#adopted-hypotheses). No consuming-project run has been
> performed. Unfilled study parameters below must be fixed before assessment;
> this document is not evidence that Commonplace already meets the target.

## Claim and system boundary

Assess whether a Commonplace builder improves the KB and supporting software
delivered to a consuming project, and whether those changes improve later
consumer work under a declared budget. The main research comparison concerns
the builder's downstream performance. A claim about the truth or causal role
of a particular note requires additional evidence.

The builder includes its KB production, diagnosis, revision, evaluation,
selection, and machinery-maintenance roles. The consumer receives a versioned
KB release and performs project tasks. Task suppliers and output judges are
outside the builder while supplying demands and judging completed work.
Someone who diagnoses a note or writes the builder's repair is filling an
internal role, even if that person also supplies tasks in another interaction.

Commonplace's product is the delivered KB together with the validators,
skills, indexes, and other supporting software in that release. State
whether the release includes the builder's own diagnostic memory, its
methodology notes and revision history, or only the product KB. This is a
design variable, not a default: the
[WikiSkill ingest](../../sources/wikiskill-persistent-knowledge-for-skill-evolution.ingest.md)
reports lower performance when the solver could read the improvement wiki
during training, with the authors' hypothesis that direct use made the
traces less informative for later improvement. Continuing
responsibility for that release, with the consuming project's judgments
arriving from outside, is what makes Commonplace an
[externally tested theory builder](../../notes/definitions/externally-tested-theory-builder.md)
once observed. Whether producing software for others also makes it a
[software house](../../notes/definitions/software-house.md) is the
[side conjecture's](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md)
question, not a premise of this experiment; selecting this case neither
refutes nor proves it.

## Freeze before the first scored episode

| Field | Required declaration | Current state |
|---|---|---|
| Consuming project and area | Named project, task population, admissible demands, and exclusions | Operator selection pending; examples in the episode file are illustrative |
| Seed | Builder revision, initial KB release, tools, instructions, and who prepared them | Pin at run start; do not treat a later checkout as the original seed |
| Models | Exact versions and settings for builder and consumer, held fixed during each comparison | Must be publicly available as of 2026-09-17; versions not yet selected |
| Task supply | Who selects incoming tasks, inclusion rule, and how omitted or failed tasks are recorded | Consecutive eligible project demands is the proposed default |
| Outcome contract | Observable acceptance criteria per task and who may change them | Judge defines before seeing treatment results; changes start a separately reported objective period |
| Budget | Task and adaptation ceilings for compute, elapsed time, evidence, and internal human work | Values pending; same ceilings for compared conditions |
| Horizon | Number or duration of episodes, stopping rule, and minimum evidence for comparison | Values pending; no stopping when a desired score first appears |
| Reliability target | Required performance, uncertainty method, and allowed comparison margin | Set before scoring; no numerical threshold is implied by this protocol |
| Feedback | Fields, delay, and visibility to builder and consumer | Training feedback and final assessment separated below |
| Acquisition mode | Passive incoming demands plus any permitted targeted probes | Passive stream is the initial default; bounded diagnostic tests are allowed and charged |

Pin the completed declaration with the releases and episode records. A
change to models, population, objective, or budget changes the comparison's
scope and must be reported. Missing parameters prevent a scored claim, not
the design of the protocol or the illustrative episodes.

## Release, consumption, outcome, feedback

For each episode retain the task and acceptance contract, delivered KB and
software versions, consumer configuration, budget and usage, output, judge's
decision and reason, and the feedback returned to the builder. Record which
KB artifacts were actually retrieved or read before a consequential decision.
State in advance, per task, an expectation contract: which artifact the
consumer should consult, what trace would show it, and what a wrong-source
answer would look like. Score the trace against that contract. An installed
KB is not evidence of consultation; conformance to the expected pathway is
evidence of consultation, not of causal contribution, which the matched
interventions below establish.

Type task families by what the consumer must do with the delivered KB:
look up a retained commitment, re-execute a retained procedure, consult the
KB unprompted at the right moment under noise, and use a revised
commitment without the superseded one leaking. These are the four
capabilities [PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
tests. The third is the failure in
[episode 2](./main-path-episodes.md#2-reflective-machinery-revision); the
fourth is the consumer-side test of every theory revision the builder
ships.

Judges assess the work against the task contract, rather than accepting it
because a methodology note passed review. Mask the KB treatment where
practical. Judges may inspect output evidence when the task requires it;
the boundary concerns their role, not a blanket prohibition on seeing text.
A different person judging reduces role confusion but does not by itself
establish unbiased or statistically independent assessment.

Return ordinary operating failures and acceptance feedback to the builder
for diagnosis and revision. Internal tests, active probes, and experiments
can guide that revision. Their selection and cost are part of the record.
The final assessment of the claimed improvement follows the protocol below.

## Learning evidence and assessment evidence

Use incoming work and disclosed feedback for development. Before the final
comparison, freeze the candidate release and evaluate it on reserved tasks
whose outcomes have not guided its construction or selection. Once an
assessment result is used to choose or repair a candidate, treat it as
development feedback for that candidate's successors; reserve new evidence
for their final assessment.

This is the initial protocol choice, not a claim that fresh tasks remove
all dependence or measurement error. Record task relatedness, prior exposure,
selection, and changes in task mix. Any later switch to adaptive reuse of a
fixed holdout must specify its information-release mechanism, sampling
assumptions, and enforced budget. Merely naming a reuse budget or returning
one bit does not establish validity. The
[adaptive-evaluation source analysis](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
identifies the literature to check before such a change; this protocol does
not claim its theorems already apply to semantic judgments.

Externally supplied objectives can stay fixed across many tasks. New requests
may instantiate an objective without revising it. If acceptance requirements
change, assess performance within the declared periods and report the change;
do not credit an easier criterion as an improvement in the builder.

## Comparisons and what they establish

Use a frozen seed builder as the baseline for an extension claim. The
baseline for a retained change is the same later task run with that change
removed, under matched consumer, model, prompt, grader, and resource
conditions; the seed's score on an earlier task is calibration, not the
baseline, because a gain between tasks confounds the change with task
drift, model variance, and scoring noise.
[PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
separates the two and reports the matched gap as its primary quantity.
Repeat or counterbalance conditions as the study design requires. A single
seed failure followed by a candidate success does not establish a new
capability. Retained changes, their later consumption, and their measured
effect jointly support a bounded extension claim.

Add control runs that bound the alternative explanations of a gain: the
task with the retained state removed, with a distractor artifact that
resembles it, with a stale version of it, and with the wrong mechanism able
to supply the answer. A gain counts only if it clears what the controls
explain.

Declare, for each with-and-without-KB comparison, what the no-KB condition
knows. Removing the KB usually removes information the task needs, so that
comparison measures benefit and cannot measure the harm of stale or wrong
content. Measuring harm requires a condition in which current authoritative
evidence stays available to the consumer while the KB content varies. The
[Memory Trust Gap ingest](../../sources/the-memory-trust-gap.ingest.md)
separates these as its benefit and safety suites, and reports that a
consumer can read timestamps correctly and still follow a misleading recency
cue, so provenance metadata is tested with the consuming model, not assumed
to work.

For the comparative hypothesis, also assess direct search over the same raw
records without the learned methodology. Pin what each condition receives,
including any equivalent content available elsewhere. Keep models, admitted
tasks, and resource ceilings comparable; account for the cost of producing
and maintaining the methodology as well as later task execution. This tests
whether the retained methodology adds value beyond access to the records.

Use a human-staffed builder under the same demands and declared resources
for the practical reliability comparison. Record adaptation costs and every
human internal intervention separately from external task supply and
judging. Success with a person performing an internal role does not establish
autonomous continuation.

Record doctrine edits per area, their authors, and the roles they served as
a diagnostic of continuation. A low count is not a success measure: the
sufficiency hypothesis needs the declared outcome target, and the comparative
hypothesis needs its comparisons. A claim that reflection supplied the gain
also needs the self-theory and machinery records described in
[episode 2](./main-path-episodes.md#2-reflective-machinery-revision).

To claim that the KB caused a difference, compare matched runs with and
without the relevant KB content, or across pinned KB versions, while holding
consumer and task conditions comparable. Account for equivalent content
available through other records. To attribute a gain to a particular note or
theory, vary that commitment or its consumption path and state the predicted
effect in advance. To attribute it to the methodology that built the note,
compare the production process as well as the resulting artifact. The
[training article](../../articles/testing-the-conjectural-learning-program.md)
owns the existing component-comparison design.

## Outcomes and limits

Report accepted task outcomes together with failures, budget exhaustion,
abstentions, and missing feedback. Report coverage and cost beside accuracy;
success on a selected subset does not establish reliable continuation across
the admitted workload. A consumer rejection is evidence about the combined
task, consumer, and KB arrangement, not automatic refutation of a note.

The three [episodes](./main-path-episodes.md) test whether these distinctions
are expressible. They supply no measurements. The first actual run must
produce the versioned consumption and outcome records before Commonplace
can be classified as an observed instance under this protocol.
