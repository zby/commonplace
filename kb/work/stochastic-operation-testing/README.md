# From live operation to controlled testing and debugging

Posed by the operator on 2026-11-14 during a discussion of review orchestration, freshness and connect. The operator commissioned this workshop to develop the distinction between permissive live maintenance and controlled repeated trials, and investigate relevant literature. This is a research and design commission, not authorization to implement a runner, change freshness semantics, or launch paid trials.

## Goal

Design the KB so that ordinary operational observations can become controlled tests and debugging cases, with workflows and provenance as the main design surfaces. Freshness is a policy that consumes provenance to decide when another operation is worthwhile, not the whole record-keeping mechanism. Ordinary maintenance should supply useful evidence for controlled investigation without requiring every operation to execute against an isolated, fully captured KB.

The intended result is a practical route from an observed maintenance failure to a controlled fixture, diagnosis and a tested repair. This architecture applies both to deterministic programs interacting with changing environments and to model-dependent operations. Where execution remains variable, repeated trials should measure a distribution of outcomes rather than demand identical outputs. Retain enough distinctions that a future implementation does not confuse freshness, answer replay, input recovery and experimental control.

## General pattern and stochastic application

The operator broadened the framing on 2026-11-14:

> Run normally with affordable observability; turn selected incidents into controlled, retained test environments.

Environmental control and execution variability are separate dimensions. A deterministic program can be hard to reproduce when files, databases, network responses or concurrent activity change. An isolated fixture makes those conditions explicit and recoverable. If behavior remains variable within that boundary, repeated trials become part of evaluation rather than evidence that the fixture is useless.

The architecture is therefore not specifically stochastic: lightweight ordinary provenance, comprehensive experimental capture, independent trial state and retained evidence. Stochastic KB operations are the main application; they add requirements for outcome distributions, uncertainty and probabilistic regression criteria.

A controlled reproducer need not replicate the entire original environment. It must preserve the conditions relevant to the failure. Capture the accessible experimental environment comprehensively while those conditions are unknown; reduce the fixture only when evidence supports removing inputs without losing the failure mode. A frozen fixture that removes a necessary concurrent interaction is not an adequate reproducer.

## Research lead and architectural focus

The operator endorsed this research lead on 2026-11-14:

> Experimental design for measurement and repair comparison; statistical debugging for failure localization; testing-oracle research for deciding what the measurements mean.

Keep this as a methodological lead, not a mandatory literature-review phase or a conclusion already established. The architectural split follows from the different retention costs and purposes of ordinary operation and controlled investigation. Design the workflow and provenance boundary and a concrete pilot first; consult incident-reproduction, test-fixture and statistical methods where specific design or inference questions remain unresolved. The aim is to design Commonplace to support these activities, not merely to write a testing procedure alongside an unchanged system.

- **Workflows:** determine how operation boundaries, execution records, input capture, traces, state reset and replay controls can support comparable trials and failure localization. The review-only subset applies these requirements through Workjig; broader application is deferred.
- **Provenance and freshness:** determine what each operation records about how its result was produced. Freshness consumes that record to decide which changes warrant another run; debugging and experiments consume it to reconstruct and compare executions. Keep scheduling a rerun distinct from recovering inputs or reusing an old answer. Do not make approximate freshness imply exact reproducibility.
- **Evaluation:** determine how a failure is recognized and how changes in its frequency are interpreted. The KB must retain enough evidence to question the evaluator as well as the operation.

The object of model-dependent debugging is a behavioral tendency under stated conditions, not just one bad output. Repeated trials test whether a repair improves the outcome distribution. Individual traces help locate mechanisms. Systematic bias, harmful tail behavior and deterministic implementation defects remain distinguishable; variation among acceptable outputs is not itself a bug.

## First application: the review-only subset

The operator selected the review-only subset as the focused first application on 2026-11-14. That implementation is complete under [ADR 132](../../reference/adr/132-review-atoms-retain-observations-behind-current-results.md); the [review architecture](../../reference/review-architecture.md) owns its execution and retention boundary. The [acceptance record](../../reports/retained/review-atom-acceptance-20261115/README.md) retains the four-kind live check and final fixture/replay evidence, including the differing tool and trust environments. This is machinery acceptance, not judgment calibration.

This parent workshop retains the general testing principles and trial evidence. Do not make the review subset implement edits, stops, full improvement compositions or a general coordinator framework first. Broader reuse is a later decision informed by the working subset.

## Retention differs between ordinary runs and controlled trials

The operator clarified the design direction on 2026-11-14: comprehensive retention is impractical for ordinary maintenance, but is a requirement to aim for in controlled trials. This is the reason for the split, not merely a choice between optional logging levels.

- **Ordinary maintenance:** keep lightweight provenance identifiers for the target, operation, KB revision and execution configuration as appropriate. Do not require a complete input archive. Identifiers may resolve through Git or other retained storage, but hashes alone cannot recover missing content. An ordinary run need not become exactly reconstructable.
- **Controlled trials:** retain the actual fixture and as much execution evidence as possible: tracked and non-Git input content, effective instructions and prompts, configuration and software identities, tool requests and responses, traces, intermediate artifacts, final outputs and evaluation records. Retain failing and successful trials. Record capture gaps and inaccessible provider details rather than claiming complete control.

A shared immutable fixture can serve several trials; each trial still needs independent mutable state and separately attributable outputs. More complete retention does not require duplicating identical bytes. Privacy, credentials and external-source retention rules remain binding; completeness is not permission to retain secrets or publish private source copies.

This is an asymmetric retention policy over one provenance concept, not a requirement to make ordinary maintenance as expensive as an experiment. Moving from an ordinary observation to a controlled fixture may establish a new, documented baseline rather than reconstruct the first run exactly. Trial records should make later investigation and comparison recoverable to the extent technically and operationally possible.

## Concrete provenance and fixture design

The selected starting point—KB commit plus retained exact target, execution identity and explicit self-contained run-local operational inputs—is implemented in the [review machinery](../../reference/review-architecture.md). A second state repository and automatic dependency traversal are not prerequisites. The reconstruction trial retained here and the later [fixture acceptance](../../reports/retained/review-atom-acceptance-20261115/README.md) support content reconstruction without establishing complete harness isolation. Future work here concerns controlled evaluation and its remaining evidence gaps, not another implementation of the same runner.

## Operator direction and starting hypothesis

The conversation established these design intentions:

- Ordinary maintenance may run in a changing checkout. Its record can carry qualified provenance rather than claim an exact snapshot of every input.
- Review and connect both consume live context beyond their explicit target and instructions. Broad context discovery is central to connect, not a new category of reproducibility problem.
- A Git revision can anchor a controlled reconstruction of tracked content. It does not capture dirty files, ignored source snapshots or `kb/reports/state/`.
- Controlled trials should fix the available input environment, give each trial independent writable state, and make new model calls rather than replay old answers.
- The first live failure need not be reconstructed exactly. The aim is to reproduce its failure mode under a retained configuration, then measure and investigate it.
- Stronger capture and isolation should be available for investigation and calibration without becoming mandatory overhead for every maintenance operation.

**Working hypothesis, not an established result:** recurring procedure failures can be exposed by repeated execution against controlled fixtures derived from ordinary observations. This could let normal maintenance remain permissive while supporting useful regression tests and comparisons of procedures, models and execution methods.

Recurrence is conditional. A fixture that omits a necessary input or concurrent change may never expose the original failure. Rare failures, dependent trials and provider changes also weaken an inference from repeated success. Failure to reproduce leaves the explanation unresolved.

## Starting evidence and distinctions

[Review architecture](../../reference/review-architecture.md) separates result files from execution-run records. Durable results hash the selected note parts and criterion; linked context is outside that freshness boundary. Run records capture launch inputs but do not establish a complete immutable evidence environment. [Connect](../../instructions/cp-skill-connect/SKILL.md) searches titles, descriptions, bodies and links and produces candidate reports without authoring links.

Freshness answers whether selected inputs changed or an operation merits repetition. It does not certify exhaustive review, correctness or exact reproducibility. A read-file manifest alone cannot account for newly added candidates or changed search results.

| Concept | Question |
|---|---|
| Maintenance freshness | Is another operation worth scheduling? |
| Provenance | What do we know about the circumstances of this result? |
| Input recovery | Can we recover the content available to a run? |
| Answer replay | Can an execution reuse an already paid answer? |
| Controlled repetition | Can independent trials start from the same declared environment? |
| Failure diagnosis | Which requirement, instruction, model behavior or environment condition explains the failure? |

A worktree isolates the trial from the main checkout but does not prevent its own workers from editing inputs. A snapshot of starting state must not be contaminated by previous trials. A fixed local environment does not pin all hosted inference internals. State the controlled boundary rather than promising that only model sampling can vary.

## Questions to resolve

1. Does the minimal ordinary provenance design above meet actual consumers' needs, and which operations require exceptions? Settle capture, execution identity and ownership before committing to a schema.
2. How should freshness work for operations with open-ended discovery? Distinguish target changes from corpus-change signals and useful rerun schedules. Decide what dirty checkout markers can and cannot establish.
3. What belongs in a controlled fixture? Include accessible operational state and ignored sources where relevant, not just the positive reads of one trial. Distinguish deliberate empty state from missing evidence.
4. Which failures require controlled concurrent edits, tool responses or scheduling rather than a static fixture? Determine when boundary mocks are useful and what they exclude from an end-to-end claim.
5. How do we classify failures and evaluate repairs? Separate instruction inadequacy, instruction violation, acceptable variation, environmental failure and evaluator disagreement. A lower disagreement rate is not necessarily an improvement.
6. What trial counts, stopping rules and uncertainty statements fit the decision? Separate searching for one failing configuration from estimating its failure frequency and estimating prevalence across realistic tasks.
7. What must be retained to compare a repair with the incumbent? Preserve unsuccessful trials and denominators; distinguish diagnostic fixtures selected for failure from held-out evaluation cases.
8. Which protections remain necessary in permissive maintenance? In particular, do not confuse allowing changing context with permission to overwrite concurrent target edits or apply a finding without checking its relevant current evidence.

The first pilot is [gate verdict stability on unchanged text](./pilot-gate-verdict-stability.md), approved by the operator on 2026-11-14. It works under an operator assumption set the same day: review verdicts can be made stable, and the improvement procedure is designed on that assumption. The pilot measures and locates present instability; it does not decide whether re-review stays in the procedure.

The [commit-plus-note reconstruction trial](./provenance-reconstruction-trial.md) ran on the operator's approval on 2026-11-14. Its [results](./provenance-reconstruction-results.md) demonstrate two independent fixtures from a commit and an actually uncommitted target, with exact captured input matches and two new review calls costing about $0.50. The harness advertised additional tools in the second launch, so the exercise establishes content reconstruction, not full execution-environment equivalence. No new runtime code was needed.

The [literature map](./literature-map.md) records starting sources and unverified leads. Source findings may revise the hypothesis; the workshop does not presume novelty.

## Evaluation boundary

The application is agent-operated KB maintenance, initially illustrated by review and connect, including deterministic components and their environmental interactions. General incident-reproduction and experimental methods matter only where they change how these operations are recorded, tested or debugged. The workshop does not attempt a general software-debugging framework.

No paid experiment is authorized by this framing. A proposed pilot must state its failure criterion, fixture boundary, evaluator, trial budget, stopping rule and decision consequence before seeking authorization. If the criterion cannot distinguish an unwanted but permitted output from a violated requirement, resolve or retain that ambiguity rather than compute a misleading success rate.

For a later authorized trial, use independent initial state and output locations; record actual model calls separately from retries, cached answers, infrastructure errors and excluded runs. A workflow's successful recovery and its first-attempt failure rate are different measures. When judging is model-dependent, assess evaluator error rather than treating a verdict as ground truth.

## Coordination

- [Review on Workjig](../review-on-workjig/README.md) owns the existing workflow work. The completed review-unification slice supplies the first shared-execution implementation. Extension beyond the review subset is deferred.
- [Artifact freshness and referential checks](../artifact-freshness-and-referential-checks/README.md) contains historical store-era designs. Reconcile against ADR 127 before reuse; do not revive the deleted generic store by implication.
- [Unattended processing failure modes](../unattended-processing-failure-modes/README.md) owns its behavior catalogue and countermeasures. This workshop develops the live-observation-to-controlled-test method rather than duplicating that catalogue.
- [LLM debugging diagnosis](../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) already distinguishes specification gaps, instruction violations and run-to-run variation. Extend or operationalize it where warranted instead of writing a parallel general account.
- [One improvement procedure over atomic instructions](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) requires every atom to be testable alone and each run to leave a typed directory. That run directory stores the start text as a commit and hash and cites review results by hash, so it is a concrete ordinary-run record for question 1. The proposal owns the run type; this workshop may recommend what the record needs for later controlled investigation.
- [Decision lifecycle and evidence](https://github.com/zby/commonplace/blob/142bff37aeaf7728a0c5cf9f3cd1c225598ba565/kb/work/decision-lifecycle-evidence/README.md) holds the [first run](https://github.com/zby/commonplace/blob/142bff37aeaf7728a0c5cf9f3cd1c225598ba565/kb/work/decision-lifecycle-evidence/first-run.md) of that procedure. Its re-review is a live observation of the problem posed here: verdicts moved on passages the run did not edit, so one re-review could not separate the effect of a fix from run-to-run variation. It is a candidate source for a pilot fixture.
- [Higher-order check evaluation](../higher-order-check-evaluation/README.md) owns calibration of one review operation over repeated rounds. It is an existing consumer of fixtures, independent trial state and denominators. Take its practice as evidence before designing a parallel one.
- [Authority grades and learning from operator decisions](../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md) requires a discriminating check tested on retained and fresh examples before a grade moves. That matches the split in question 7 between diagnostic fixtures selected for failure and held-out evaluation cases. The proposal owns the grade decision; this workshop supplies the test method.

## Evaluation cases requested after the focused writing-tool comparison

The operator requested these additions after discussing the focused writing-tool
comparison. They are requirements to carry into later test design, not measured
benefits, changes to live procedures, or authorization for model trials.

### Missing-fact and supplied-fact pairs

Test whether an edit operation both avoids unsupported additions and uses evidence
when it is available. Retain paired cases with the same finding and target passage:

- **Necessary fact absent:** the authorized inputs cannot support the requested
  specificity. The appropriate response identifies the missing fact and leaves
  the substantive choice open, rather than inventing a mechanism or measurement.
- **Necessary fact supplied:** the authorized inputs supply that fact and permit
  a minimal repair. Repeating the question or declining the edit without another
  reason is an avoidable deferral, not successful caution.

Label the expected response under the operation's actual authority; supplied facts
do not authorize a reserved claim change. Report unsupported additions and avoidable
deferrals separately. Keep both members together when splitting cases and treating
related cases as independent units for analysis: a fact twin is not another
independent task. These cases test a specific behavior, not live failure prevalence.

### Earned-use controls for detectors

For each new or revised stylistic detector under evaluation, retain a clear failure,
a legitimate use of the same construction, and a near-miss where the available
context changes whether the construction is justified. A phrase or syntax match
alone must not determine the expected finding. Record why the evidence earns the
legitimate use and what the failure lacks.

Examples embedded in the criterion are useful smoke tests, not independent
calibration. Use separate cases to assess discrimination, and retain contested
labels rather than treating the evaluator's verdict as ground truth. Coordinate
with the existing [gate-calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)
instead of creating a parallel calibration policy.

### Evaluate retained diagnostic probes

The [review-operation design entry](https://github.com/zby/commonplace/blob/142bff37aeaf7728a0c5cf9f3cd1c225598ba565/kb/work/decision-lifecycle-evidence/review-operation-overlaps.md#agreed-direction-retain-diagnostic-probes-in-review-results)
records the agreed direction for recording concrete probe outputs in result bodies.
This workshop owns their evaluation, not a duplicate retention specification.
Assess separately whether the probe faithfully represents the passage and its
context, and whether the resulting finding is correct. Include consequential
cleared candidates when testing false-positive restraint. A recorded probe or
valid result format alone does not establish judgment quality.

## Bookkeeping and next decisions

Keep framing and research reasoning here. Keep full external copies in private source snapshots, not this workshop. Literature leads are not evidence until inspected and grounded. Future run outputs belong under `kb/reports/state/`; retained research evidence follows the reports collection contract. Record fixture identity, configuration changes and evaluation decisions with any authorized trial so failed attempts remain visible.

The next deliverable is a concrete workflow/provenance design and bounded pilot protocol, not a broad literature review or generalized runner implementation. Choose the capture boundary from the pilot's needs, then use targeted literature checks for unresolved questions about measurement, diagnosis or inference. If evidence undermines the proposed split, retain the counterexample and revise the framing before building machinery.

## What closes the workshop

- Targeted methodological checks resolve the pilot's consequential measurement and diagnosis questions, or explicitly retain their limits. A broad literature survey and a novelty claim are not closing requirements.
- The ordinary-record versus controlled-fixture boundary is specified with honest recovery and freshness claims.
- Concrete workflow and provenance design decisions explain how Commonplace supports measurement, failure localization and repair comparison, including lightweight identifiers for ordinary runs and extensive content and execution retention for controlled trials. Freshness is specified as a consumer of provenance; proposed changes and deliberately unchanged behavior are distinguished.
- A bounded pilot has either been authorized and evaluated, or explicitly declined with the remaining uncertainty recorded. No implementation claim follows from a paper design alone.
- Decisions and supported insights are extracted into the existing debugging theory, operational instructions, reference or an ADR as appropriate; unneeded infrastructure is explicitly deferred.
- The workshop is then removed and its active-list entry deleted.
