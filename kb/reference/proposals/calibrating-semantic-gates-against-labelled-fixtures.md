---
description: "Proposal: require non-leaking known-case regression before a semantic gate can advance, and reserve live detection-rate claims for separately sampled field calibration"
type: ../types/design-proposal.md
tags: [kb-maintenance]
traits: [has-external-sources]
---

# Calibrating semantic gates against labelled fixtures

A semantic gate is a natural-language criterion handed to an LLM reviewer, which returns PASS / WARN / FAIL. Authoring one is cheap; knowing whether it detects the failure it names is not. A plausible-sounding gate can systematically miss the defect on real notes or over-flag clean ones. The miss direction is self-concealing: a criterion that never fires produces articulate, well-quoted, individually plausible reviews that are observationally identical to a healthy gate running over a clean corpus. No downstream signal arrives because the gate's job was to provide that signal.

This proposal separates two evidence grades that the current system lacks. Every gate first gets a non-leaking, human-labelled **known-case regression suite**. Failing a known case is enough to reject or quarantine the gate; passing every known case is necessary but not sufficient to trust it. Estimating live detection and false-alarm rates is a separate **field-calibration study** over independently sampled and labelled deployment cases. The distinction prevents a convenient regression set from acquiring statistical authority it has not earned.

The gate is an oracle. Per [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), an oracle is worth compounding only when it separates the classes that matter; fluent verdicts do not demonstrate that separation. Known fixtures test whether the gate catches specified failures. Field calibration estimates how often those failures and false alarms occur in operation. Together, they provide the concrete evidence substrate for the "per-gate precision/recall history" that [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) names as a lifecycle requirement but does not build.

## Current state (as of 2026-07-12)

Shipped:

- Semantic gates are individual markdown files at `kb/instructions/review-gates/{lens}/{name}.md`, with type `review-gate` (the `semantic` lens lives under `.../semantic/`). Each carries a `## Failure mode` and a `## Test` that selects PASS / WARN / FAIL / ERROR.
- Most gates carry inline `## Example (pass)` and `## Example (fail)` blocks. These are **illustrative, singular, and never executed** — they orient a reviewer inside the prompt; nothing runs the gate against them or checks that it decides them correctly.
- Reviews are partitioned by model: a review or freshness baseline under one `--model-partition` does not satisfy freshness for another (see [review system](../README-REVIEW-SYSTEM.md#concepts)).

Precedent (sibling repo `epistack-casebooks`, `kb/work/post-commonplace-upgrade/track-a/`): a collection-conformance criterion was authored, shipped, and trusted for three days even though its central limb had a zero firing rate against known positives. It was ruled MET in 12/12 blind reviews, including reviews of both known-drifted notes, and produced articulate output throughout. In one afternoon, a four-note labelled sample (two drifted, two clean, three blind reviewers each) exposed both inert limbs. The rewritten criterion separated perfectly on the same sample: drifted WARN 3/3 and clean PASS 3/3 — an in-sample number, per that track's `calibration/REPORT.md`. Two distinct failure mechanisms surfaced: a reviewer accepting a violation's locally available excuse, and a reviewer silently substituting a computable proxy for a criterion it could not evaluate from one artifact. Nothing readable in the twelve reviews distinguished the inert limbs from working ones.

Not shipped:

- Any executable labelled fixture set for a gate, known-case regression result, or field estimate of per-gate detection and false-alarm rates.
- Any gate lifecycle state beyond existence — no notion of a gate that is authored but not yet trusted.
- Any regression signal when a gate's text, or its model partition, changes.

The inline pass/fail examples are the germ of a known-case suite. The first step promotes them from illustrations to an executed smoke test; independently labelled fixtures then turn that smoke test into a regression suite. Neither step alone produces a field-calibrated gate.

## What a fixture is

A fixture is a `(note snapshot, expected flag state)` pair scoped to one gate:

- **Known positive** — a note the gate should flag. Expected flag state: `flag`, satisfied by WARN or FAIL.
- **Known negative** — a note the gate should pass. Expected flag state: `no flag`, satisfied only by PASS.

The binary state measures detection, not severity. A fixture may separately record an expected WARN or FAIL when severity matters, but that check is not part of the binary hit rate. A false negative is a known positive that receives PASS; a known-case false alarm is a known negative that receives WARN or FAIL. Both are defects in the gate run, not the fixture note.

## Where fixtures come from

Four sources, in rough order of cost:

1. **The gate's own inline examples.** The existing `## Example (fail)` is a labelled positive; `## Example (pass)` is a labelled negative. Harvesting them is nearly free and gives every gate a two-fixture floor — but a confounded one. Because the examples are embedded in the gate file, they appear in the criterion prompt the reviewer reads. A gate deciding its own inline examples correctly demonstrates recognition, not detection. The examples serve as a smoke test: a gate that fails even these is broken outright. Trust-grade calibration needs fixtures that the criterion text does not contain.
2. **Real review history.** Agreed live WARNs and FAILs are positive candidates; agreed PASSes are negative candidates. A criterion-focused human adjudication must label the snapshot independently before it becomes a fixture. This matters most for negatives: agreement with an absence is weaker evidence than confirmation of a witnessed defect, and notes the gate passed must be sampled deliberately to expose false negatives.
3. **Accepted-edit before/after pairs.** These are fixture candidates, not labels. Before inclusion, an independent judgment must establish that the pre-edit snapshot instantiates the named failure mode and the post-edit snapshot does not. This is the same capture format that [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) mines. However, [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md): acceptance alone establishes neither gate attribution nor post-edit cleanliness.
4. **Hand-authored adversarial cases.** Deliberately constructed near-misses that probe the gate's boundary — the note that is one clause away from the failure mode. A useful positive must be *locally defensible*: it ships with the same alibi a real violation would (a nearby citation, a plausible framing, a hedging parenthetical). A crude positive that any reviewer catches inflates measured detection without testing the case that matters — in the precedent incident, the violation that slipped through was precisely the one whose excuse was true.

[Netflix's production LLM-judge lifecycle](../../sources/lifecycle-llm-judge-recommendation-explanations.ingest.md) provides an external analogue for assembling this regression corpus. Its launch benchmark held roughly 900 rationale-labelled examples near class balance (about 54% fail), including expert-authored failures and LLM-synthesized boundary cases. Weekly additions were subsampled to preserve that balance. The balance makes both classes visible to regression, while the boundary cases probe failures that ordinary production sampling rarely surfaces. The authors explicitly do not treat the resulting agreement metrics as live defect rates.

A Commonplace fixture corpus should therefore report the positive and negative counts for each gate and identify which fixtures probe a known boundary. It need not copy Netflix's class ratio. It must show that neither class nor the hard cases disappeared behind production prevalence.

## What known-case regression measures

Run the gate against the labelled set and score its known-case hit rate, `P(flag | known positive)`, and known-case false-alarm rate, `P(flag | known negative)`. WARN and FAIL both count as a flag. Aggregate accuracy is not useful: with mostly clean fixtures, an always-PASS gate scores high and detects nothing. The minimum bar is separation on the known set, with the gate flagging positives materially more often than negatives.

Because the gate is an LLM, one run does not settle even a fixed fixture. Repeated runs estimate fixture-conditional response rates and expose intermittently inert criteria. They do not repair selection bias or estimate population TPR/FPR. A failing rate can block the gate; a passing rate says only that the current gate clears the current known cases under the recorded judging configuration.

## What field calibration adds

Field calibration defines a deployment population and independently samples notes from it, including notes the gate passes. Human adjudicators label gate applicability and defect presence without treating the gate's verdict as ground truth. Repeated or prospectively held-out evaluation can then estimate population TPR and FPR, treating defect presence and gate flagging as the positive class, with uncertainty appropriate to the sample size.

This is the stronger "judge calibration before automation" step that [evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) places ahead of trusting an automated evaluator. Its sampling frame, labelling protocol, minimum positive and negative counts, interval method, and stopping rule remain design choices; without them, the result remains known-case regression rather than field calibration.

The Netflix analogue uses a separate weekly sample of about 300 production explanations. It holds the proportions of three judge outcomes fixed from week to week, gives extra weight to new catalog items, and sends every item to at least three human raters. The majority label is the reference. Each judge metric must remain at least as high as the mean individual-rater metric minus two standard deviations across raters, both on the full sample and on new titles alone. This pattern adds three candidate safeguards: stable outcome strata for time comparison, a shift-sensitive slice, and an alert band relative to measured human disagreement.

Those safeguards are shapes, not portable constants. Fixed strata support comparable weekly measurements but do not reproduce deployment prevalence; a Commonplace study must say whether it estimates a stratified monitoring cohort or reweights results to the deployment population. The sample count, strata, high-drift slice, and human-relative band all need local warrant. In Netflix's system, crossing the band would trigger rubric re-tuning, followed by manual promotion with the previous rubric retained for rollback. That branch has never fired in production. The paper therefore evidences a live monitoring loop, not successful recovery from detected drift.

## Judging-configuration dependence

A regression or calibration result belongs to the judging configuration that produced it. At minimum, that configuration includes the gate snapshot, fixture or field-sample snapshot, model partition, rendered prompt and system instructions, sampling settings, and repetition protocol. A result under one model partition does not transfer to another, just as a review under one partition does not satisfy freshness for another.

Editing the gate or changing partitions must rerun the known-case suite; changes to other recorded configuration components must invalidate the result when they can change verdict behavior. This is the regression trigger the current system lacks: today a gate edit stales the notes it reviews, but nothing re-checks that the edited gate still detects its own positives. The general invalidation rule follows [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md).

## Free choices (deliberately unresolved)

- **Fixture storage.** Options: a `## Fixtures` section inside the gate file; a sibling `{name}.fixtures/` directory; or a fixture store outside the gate file entirely. The first option keeps the labelled set hashed into the criterion text, so editing it fires `criterion-changed` like any gate edit. It also couples fixtures to the freshness mechanism for free. However, render-time stripping is then mandatory, not polish: any fixture the reviewer can see in the criterion prompt is spent as a test (see the inline-example confound above), in addition to bloating the prompt.
- **Regression threshold.** Must the gate flag 100% of known positives and pass 100% of known negatives, or clear a rate bar across repeated runs? A hard rule is simple but brittle; a rate bar needs a cutoff and uncertainty treatment.
- **Field sampling.** Should a monitoring sample follow deployment prevalence, hold gate-outcome strata fixed for comparability, or deliberately weight a shift-sensitive slice? A stratified sample must state whether its metrics describe that monitoring cohort or are reweighted to the deployment population.
- **Field threshold.** What sample sizes, interval bounds, and relative costs of false negatives and false positives justify a trust decision? A human-disagreement-relative alert band is one option, but its formula and rater count need local validation. This cannot be reduced to the regression threshold.
- **Blocking vs advisory.** Does known-case failure prevent a gate from writing trusted freshness baselines, or only annotate them? Passing remains necessary but not sufficient; activation may require field evidence or an explicit human risk decision. Either route demands the `candidate → active` distinction that [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) also needs.
- **Recovery and rollback.** If regression or field monitoring triggers a gate rewrite, what must pass before the replacement can become active? The candidate path is to rerun non-leaking regression, stage the replacement for human promotion, and retain the previous judging configuration for rollback. The operator, rollback trigger, and retention period remain open.
- **Corpus scope.** One fixture set per gate, or a shared cross-gate corpus each gate is scored against? Per-gate is simpler; a shared corpus surfaces gates that fire on each other's positives (double-flagging).
- **Repetition budget.** How many runs per fixture, and at what partition, are needed before the rate is trusted? This is a cost knob traded against confidence in the measured gap.
- **Virtual criteria.** Type- and collection-conformance assays use a spec or `COLLECTION.md` as their criterion side rather than an authored gate file; their applicability and fixture scope may require a different substrate.

## Adoption criteria

Adopt the known-case layer when a worked case shows the loop paying off: at least one independently labelled, non-leaking fixture exposes a real false negative or false alarm that author review and inline examples missed, and the chosen storage does not leak fixture content into the live review prompt. Treat passing known cases as a regression precondition, not evidence of live accuracy.

Adopt field calibration as a trust signal only after a worked case defines a deployment sample, labels it independently, reports uncertainty, and demonstrates that the result changes a gate lifecycle decision. Without such a case, this stays a proposal: the point is evidence that changes whether a gate is operated, not a testing ritual.

Treat a recovery branch as demonstrated only after a deliberate rehearsal or live alert exercises re-evaluation, manual promotion, and rollback. A deployed monitor that has never crossed its threshold shows that observation is operating; it does not show that the response path works.

## Risks

- **Fixture overfitting.** A gate tuned until it passes its own fixtures may only detect those fixtures. Untouched holdouts or prospective cases guard the regression claim; only sampled field cases support population claims.
- **Label drift.** The human label is the oracle; if the failure mode is genuinely contested, the fixtures encode one reading and calibration measures conformance to it, not correctness.
- **Cost.** Repeated LLM runs per fixture, partition, and gate edit are not free; without a repetition budget and trigger discipline, calibration can cost more tokens than the reviews it protects.
- **False confidence.** A gate that clears a small known set can still miss the failure mode on absent note shapes. The lifecycle must not let a green regression result masquerade as field calibration.
- **Replication is not a substitute.** Running more blind reviewers per note guards against reviewer variance, not against a defective criterion: replicas of a criterion that asks the wrong question converge on the same wrong answer. In the precedent incident, three independent reviewers each located the offending sentence and excused it in near-identical words. Only a labelled positive distinguishes consensus from correctness.

---

Relevant Notes:

- [error correction works with above-chance oracles and decorrelated checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rests-on: a gate is an oracle worth trusting only when TPR > FPR; calibration is the measurement of that gap
- [evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — rests-on: judge calibration precedes trusting an automated evaluator
- [an accepted edit verifies the change, not the rule](../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — rests-on: fixtures mined from accepted edits are instance-verified, not proof of generalization
- [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — rests-on: identifies which changes must invalidate retained regression and calibration evidence
- [reasoning production is not reasoning evaluation](../../notes/reasoning-production-is-not-reasoning-evaluation.md) — rests-on: conclusion-agreement substitution supplies an adversarial fixture family for a self-concealing evaluator failure
- [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — rests-on: calibration is a hardening step for a soft LLM oracle
- [gate learning from accepted edits](./gate-learning-from-accepted-edits.md) — see-also: this proposal supplies the detection-rate measurement that proposal's lifecycle assumes
- [trajectory-aware evaluation of transforming agent workflows](./trajectory-aware-evaluation-of-transforming-agent-workflows.md) — see-also: a sibling labelled and repeated evaluator design at workflow-trajectory scope
- [The Lifecycle of LLM-as-a-Judge for Large-Scale Recommendation Explanations](../../sources/lifecycle-llm-judge-recommendation-explanations.ingest.md) — evidenced-by: production analogue for class-balanced boundary fixtures, fixed-stratum field monitoring, human-relative alerts, and a manual recovery path whose drift trigger remains unexercised
- [Improving AI Skills with autoresearch & evals-skills](../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) — evidenced-by: practitioner use of a hand-scored mini set to check a judge before automated optimization
- [review system](../README-REVIEW-SYSTEM.md) — part-of: the assay/gate model and model-partition rule this design extends
