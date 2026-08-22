---
description: "Explores candidate signals, calibration experiments, authority levels, and workflow placements for evaluating maintainability in agent-generated code"
type: kb/types/note.md
traits: [has-external-sources, has-comparison]
tags: [learning-theory, llm-reliability, evaluation]
---

# Brainstorming: maintainability oracles for agentic development

This is a seedling about two coupled design questions:

1. How could we construct an oracle that discriminates maintainable from merely correct agent-generated code?
2. How should that oracle participate in planning, implementation, review, and later learning without turning noisy proxies into hard gates?

The starting conjecture is that [weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md). Tests exert strong selection pressure on immediate correctness; maintainability is delayed, distributed across later changes, and judged through weaker signals. A stronger oracle might change which candidates survive without requiring the generator to acquire new design knowledge.

Nothing below is a finished scoring model or development method. The purpose is to expose the design space, name the experiments it needs, and separate ideas that usually get collapsed into “add another review agent.”

## What would the oracle evaluate?

“Maintainability” is too loose to score directly. Style conformity, low complexity, and reviewer approval are possible evidence, but none is the target. A more operational target is:

> Given a distribution of plausible future changes, how much effort, dispersion, regression risk, and new structural debt does this implementation impose?

This makes maintainability relational and counterfactual: code is maintainable *for some future change distribution*, not in isolation. A compact function can be harder to change than a longer explicit one; duplication can be cheaper than an abstraction when the duplicated cases will evolve independently; a dependency that looks clean locally can make the next cross-cutting change expensive. So the oracle needs a declared horizon and change distribution — without them it risks measuring conformity to a design aesthetic rather than future change cost.

## Candidate evidence surfaces

No single signal below is a maintainability oracle. Each observes a different projection of the target and carries a different gaming surface.

| Evidence surface | Candidate signals | What it can discriminate | Characteristic blind spot |
|---|---|---|---|
| Hard correctness | compilation, tests, types, schemas, mutation testing | behavior preserved under specified cases | says little about the cost of later changes |
| Structural rules | dependency direction, cycles, forbidden imports, API boundaries, ownership constraints | violations of known architectural commitments | encodes yesterday's architecture and can punish legitimate change |
| Static proxies | complexity, duplication, coupling, churn, file or symbol dispersion | suspicious shapes correlated with change difficulty | Goodharting; thresholds are language- and codebase-specific |
| Change-relative analysis | predicted files touched, call-graph impact, interface growth, migration surface | blast radius of the proposed change | predicts from the present graph, not unknown future requirements |
| Process evidence | design alternatives considered, explicit premises, execution traces, rejected approaches | whether maintainability-relevant reasoning occurred | legible reasoning can be wrong or ceremonial |
| Model judgment | rubric scoring, pairwise design comparison, perspective reviews, adversarial probes | soft semantic distinctions static tools cannot express | correlated model priors, position bias, fluent rationalization |
| Human judgment | blinded pairwise review, expert veto, disagreement, confidence | tacit codebase and domain knowledge | expensive, inconsistent, and often uncalibrated against later outcomes |
| Longitudinal outcomes | later edit time, files touched, regression rate, rework, incidents, rollback, architectural drift | realized cost under actual subsequent changes | arrives late and reflects team/process effects beyond the original patch |
| Synthetic futures | repeated-change tasks, requirement perturbations, held-out feature sequences | response to controlled future changes | the synthetic change distribution may not match production |

The most interesting oracle may combine *leading* evidence available before merge with *lagging* evidence that later recalibrates it. A static rule can make an immediate decision; future change cost can tell us whether that rule deserved authority.

## Distinctions the design must preserve

### Correctness gate versus maintainability ranking

Maintainability should normally compare candidates that already satisfy required behavior; otherwise a beautiful incorrect patch can outrank a correct ugly one. A two-stage design — hard correctness eligibility, then maintainability comparison — keeps the two objectives from compensating for each other by accident. Some maintainability constraints are non-compensable anyway: a forbidden dependency or an irreversible migration deserves a veto rather than a ranking penalty. The system likely needs both gates and preferences.

### Activation versus judgment

A review can fail in two ways: the model never considers a relevant concern, or it considers the concern and judges badly. [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md), and direct probes can elicit failures that generic self-review misses, which is what [maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) supply through perspectives, checklists, and adversarial questions.

Those mechanisms improve coverage, but coverage is not discrimination. An oracle also needs evidence that a surfaced concern separates better from worse patches rather than merely generating plausible criticism.

### Oracle strength versus target alignment

A check can be reliable and still measure the wrong target. The [Huxley-Gödel Machine](../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) finds that immediate benchmark performance can mis-rank an agent's long-run lineage productivity. A maintainability oracle can fail the same way: an exact complexity threshold may be a hard oracle for its metric while remaining a weak oracle for future change cost. Every proposed signal therefore needs two tests:

- Does it discriminate its stated observable reliably?
- Does that observable predict the maintainability target and time horizon we care about?

### Selection evidence versus diagnostic evidence

A scalar score may choose the better candidate without teaching the next agent why it was better. [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md): improving both the proposals and the oracle itself takes diffs, traces, violated constraints, reviewer disagreements, and later outcomes. The development system should therefore retain enough evidence to audit a decision and mine new checks from escaped failures, not only the final score.

## Possible oracle architectures

### Veto stack

Run ordered checks and reject on any load-bearing violation: correctness, security, irreversible migrations, architectural boundaries, then human escalation. This is easy to reason about and suits strong narrow checks, but it cannot express tradeoffs among soft qualities, and false positives become blocking.

### Weighted composite score

Normalize signals and combine them into one score used to rank or accept patches. Convenient for optimization, but weights conceal disagreements and allow compensation: excellent naming could numerically offset a dependency violation. Correlated signals can also create an illusion of independent evidence. A composite should not gain authority until its components and their correlations have been calibrated.

### Quality profile or Pareto frontier

Keep dimensions separate — correctness, change locality, architectural fit, review confidence, context cost — and compare candidates by dominance or an explicit tradeoff policy. This preserves information and makes conflicts visible, but still requires a later decision rule. It may be the better research representation until there is enough evidence to justify scalar weights.

### Pairwise comparison

Ask which of two correct implementations would be easier and safer to change under named future scenarios. Pairwise judgment may be easier than absolute scoring, but position bias, instability, and cyclic preferences must be measured. The existing [pairwise soft-oracle brainstorming](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) supplies a calibration ladder rather than assuming pairwise is stronger.

### Escalation classifier

Do not attempt to score maintainability globally. Predict whether the automated evidence is sufficient for this change; accept covered low-risk cases and escalate the remainder. This aligns with [warranted autonomy being bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md). Its difficult failure is false confidence: the classifier must discriminate cases outside its own competence.

These architectures compose. A practical system might use hard vetoes, maintain a profile for advisory comparison, and let an escalation classifier decide when a human must judge unresolved dimensions.

## Constructing a composite oracle

A possible experimental ladder:

1. **Declare the target.** Choose a codebase, change distribution, time horizon, and observable cost. Avoid starting from convenient metrics.
2. **Collect candidate episodes.** Preserve task, starting revision, alternative correct patches, design artifacts, review traces, and later outcomes.
3. **Establish reference judgments.** Use blinded expert pairwise review, repeated-change performance, or both. Record disagreement rather than forcing false consensus.
4. **Measure each signal alone.** Estimate discrimination, stability, cost, latency, coverage, and failure clusters. Binary checks need TPR and FPR; ranking checks need pairwise consistency and correlation with reference orderings.
5. **Measure dependence.** Determine whether signals fail on the same patches. Five correlated model reviewers are not five independent checks.
6. **Build competing composites.** Compare veto stacks, learned rankers, explicit weighted scores, and Pareto policies on a development split.
7. **Test out of sample.** Hold out repositories, time periods, requirement families, and architectural regimes. A repository-specific oracle may be useful, but its domain must be explicit.
8. **Run in shadow mode.** Produce recommendations without changing merge authority; compare predictions with human review and later outcomes.
9. **Grant narrow authority.** Gate only the change classes where discrimination and false-positive cost are acceptable. Escalate the rest.
10. **Recalibrate from misses.** Convert escaped regressions, expensive later edits, and bad blocks into new examples, revised probes, or retired signals.

The sequencing principle comes from [evaluation automation being phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — observe real failures, specify evaluators, calibrate them, and only then automate — and the amplification condition from [error correction](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md): weak checks help when they discriminate and their errors are sufficiently decorrelated.

## Incorporating the oracle into development methods

The oracle should not appear only as a final PR bot. Different evidence becomes available at different decision surfaces.

### Before implementation: define the quality target

- Classify the change by consequence, uncertainty, and expected architectural reach.
- State which future changes or invariants matter.
- Record architectural vetoes and acceptable tradeoffs.
- Ask the model for alternative designs and predicted blast radii, not only one plan.

This is oracle construction at task scale: the team decides what maintainability means *for this change* before inspecting an implementation.

### During program design: compare projections cheaply

- Compare call graphs, file-tree diffs, types, interfaces, and data-flow sketches.
- Run perspective probes: maintainer, operator, migration author, security reviewer, future feature author.
- Preserve rejected alternatives and reasons so implementation review can test whether the chosen mechanism survived.

Part II of [Why Software Factories Fail](https://x.com/dexhorthy/status/2081058573556306030) places human judgment at these surfaces. The possible extension is to treat the artifacts as oracle inputs whose predictive value can later be measured, rather than as planning ceremony.

### During implementation: shorten and instrument the span

- Work in vertical slices that produce end-to-end evidence.
- Run hard checks continuously.
- Record which architectural constraints and maintainability probes fired.
- Review small diffs when uncertainty or oracle disagreement is high.

Short spans reduce the cost of an imperfect oracle; they do not make it stronger. Keeping that distinction prevents a workflow improvement from being mistaken for automated discrimination.

### At review: separate evidence, decision, and authority

- Present a quality profile with source evidence, not only a verdict.
- Show check disagreement and uncertainty.
- Compare against an alternative when possible.
- Make clear which findings block, advise, or trigger human review.
- Preserve human overrides with reasons for later calibration.

[Agentic Code Reasoning](../sources/agentic-code-reasoning.ingest.md) suggests that semi-formal premises and execution traces can improve soft code verification, but it also leaves a nontrivial error rate — structured reasoning is a candidate evidence generator, not automatic authority.

### After merge: collect delayed labels

- Attribute later rework, regressions, dispersed edits, and constraint violations back to prior decisions where possible.
- Re-run predicted blast radius against realized change surface.
- Sample apparently successful changes to detect silent proxy gaming.
- Update failure taxonomies and question sets from escaped cases.

[SlopCodeBench](../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) is an early practitioner instance of this design: incrementally revealed requirements force each later checkpoint to exercise the structure left by earlier ones, while held-out black-box tests provide a delayed accumulated-defect signal. Horthy's small run is evidence that the surface can distinguish trajectories, not evidence that strict pass or static slop metrics are sufficient maintainability oracles; generating delayed evidence does not by itself justify transferring review authority from humans to the benchmark.

The [Eval Engineering workflow](../sources/towards-automating-eval-engineering-2079976006644072796.ingest.md) offers a useful pattern here: mine production traces into reproducible tasks, inspect verifier trajectories, and keep the user involved while the target is still being specified.

## A minimal pilot

The ladder narrows to something tractable without building a universal score. Take one actively maintained repository and one recurring class of medium-sized changes. For each task, have the same model produce two or three behaviorally correct candidates under different planning or design prompts. Apply the hard correctness checks first, then collect a profile of structural signals and perspective-based reviews, and have experienced maintainers compare the candidates blind and state the future-change risks they expect. Give each accepted implementation one or more held-out follow-up changes, measuring files touched, regressions, tool steps, and reviewer rework. Finally, ask which pre-merge signals predicted the human ordering and the realized follow-up cost, and run the surviving signal set in shadow mode on new changes before granting it any blocking authority.

This tests the motivating conjecture directly: can stronger selection over candidates from the same generator improve later change performance without changing model weights?

## Parallel application to agent-operated KBs

Code maintainability is one instance of a delayed quality. Commonplace has the same shape: deterministic validation strongly selects structural conformance, while explanatory-reach, connection value, and synthesis quality have weaker oracles. The existing [quality-signals brainstorming](./quality-signals-for-kb-evaluation.md) explores structural, semantic, metamorphic, and agent-use signals for that domain.

The two cases could inform each other. Code supplies executable and longitudinal outcomes; the KB supplies explicit type contracts, review criteria, and inspectable knowledge artifacts. A general result worth eventual promotion would concern how composite oracles for delayed qualities are constructed and assigned authority — not a code-specific metric.

## Open Questions

- Which future-change distribution makes a maintainability benchmark realistic without leaking the intended design?
- Can repository history provide labels, or does it confound code quality with team skill, urgency, and organizational structure too heavily?
- Are pairwise judgments more discriminating than scalar rubrics after controlling for position bias and instability?
- Which static signals add independent information after architectural constraints and human review are known?
- How should vetoes, preferences, and uncertainty interact without collapsing into one gameable score?
- Can model diversity provide meaningful decorrelation, or must checks differ in evidence and method rather than model identity?
- How should the system detect that its oracle is driving convergence toward a locally clean but globally brittle style?
- What delayed outcomes should invalidate or retire an oracle component?
- Which parts of the workflow should remain human-owned even if patch-level maintainability discrimination becomes strong?

---

Relevant Notes:

- [Weakly discriminated qualities tend to be underselected](./weakly-discriminated-qualities-tend-to-be-underselected.md) — grounds: the selection mechanism that motivates building a stronger maintainability oracle
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: positions hard checks, soft judges, delayed outcomes, and human judgment as different verification surfaces
- [Evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — mechanism: failure observation and calibration must precede automated optimization
- [Error correction works with above-chance oracles and decorrelated checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — mechanism: conditions under which heterogeneous weak checks can amplify
- [Elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) — enables: supplies and maintains the probes needed to activate relevant failure knowledge
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — contrasts: selection scores and improvement evidence are separate requirements
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — exemplifies: staged calibration of one candidate judgment method
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — compares: parallel composite-oracle design space for semantic KB quality
- [005-quality-check placement](../reference/adr/005-quality-check-placement.md) — evidenced-by: existing workflow placement based on determinism, cost, and false-positive tolerance
- [Why Software Factories Fail: Benchmarking the new frontier](../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) — evidenced-by: a bounded practitioner benchmark of incrementally revealed requirements, strict accumulated passes, and deterministic maintainability proxies
