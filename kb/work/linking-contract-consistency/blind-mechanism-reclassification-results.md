# Blind mechanism reclassification results

**Date:** 2026-07-29

**Status:** complete read-only test; reversal evidence against the reviewed EX/OP disposition ledger; no migration or adjudication performed.

**Protocol:** [blind mechanism reclassification test](./blind-mechanism-reclassification-test.md)

## Verdict

The tested split does **not** survive its pre-registered thresholds. All 39 EX/OP rows had a stable majority, but majority agreement with the review was only 30/39 (76.9%), below the required 80%, and direct EX↔OP reversal affected 7/39 rows (17.9%), above the required <15%. Direct reversal was the dominant failure (7 rows versus 2 boundary-to-EN/OTHER disagreements), so this is the protocol's reversal-evidence outcome, not an indeterminate middle result.

Do not adopt or migrate the reviewed 41/72 `explained-by` / `operates-through` split from this ledger. The high blind stability shows that the supplied class definitions were usable; the unreproduced object is the prior row-level boundary application. The recommended next evidence step is to redesign that application test, reclassify the full candidate surface with k≥3 samples per row, and retest before maintainer adjudication. If no second classification round is wanted, the protocol's alternative is one broad successor with the prerequisite and OTHER rows adjudicated separately.

## Pre-registered threshold reading

| criterion | observed | threshold | result |
|---|---:|---:|---|
| Stable EX/OP majority | 39/39 (100.0%) | ≥90% | pass |
| Majority agrees with review | 30/39 (76.9%) | ≥80% | **fail** |
| Direct EX↔OP reversal | 7/39 (17.9%) | <15% | **fail** |

## Aggregate

| cohort | rows | stable majority | unanimous | majority matches review |
|---|---:|---:|---:|---:|
| EX/OP test cohort | 39 | 39 (100.0%) | 34 (87.2%) | 30 (76.9%) |
| EN boundary probes | 10 | 10 (100.0%) | 4 (40.0%) | 5 (50.0%) |
| all rows | 49 | 49 (100.0%) | 38 (77.6%) | 35 (71.4%) |

### Majority confusion matrix

| review disposition | EX majority | OP majority | EN majority | OTHER majority | UNSTABLE |
|---|---:|---:|---:|---:|---:|
| EX | 20 | 1 | 0 | 0 | 0 |
| OP | 6 | 10 | 0 | 2 | 0 |
| EN | 5 | 0 | 5 | 0 | 0 |

Among the 39 test rows, the nine majority disagreements comprise 7 direct EX↔OP reversals, 2 boundary disagreements to OTHER, and 0 unstable rows. At vote level, review-EX rows received 59 EX, 3 OP, 0 EN, and 1 OTHER votes; review-OP rows received 18 EX, 30 OP, 1 EN, and 5 OTHER votes. Direct opposite-class votes therefore account for 21/117 votes, against seven boundary-class votes.

### EN boundary probes

All 10 EN rows were stable, but only 5/10 had an EN majority and only 4/10 were unanimous. The 30 votes were 13 EN, 16 EX, 1 OP, and 0 OTHER. This is evidence for the later prerequisite-family review: half of the rows preclassified as EN read instead as explanatory under the blind definitions. Per protocol it neither saves nor sinks the EX/OP split.

## Sample and attrition

The sample is unchanged: EX ledger positions 1, 3, 5, …, 41 (21 rows); OP positions 1, 5, 9, …, 69 (18 rows); and all 10 EN rows. All 49 source and target artifacts existed and every registered edge was still present, so attrition is zero and no denominator changed. One edge moved without changing its tuple: OP position 53, `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md` → `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`, from baseline line 77 to current line 59.

To keep the ledger strata blind, classifier inputs used neutral S01–S49 IDs in a SHA-256-derived order; this changed presentation order only, not sample selection. Each classifier saw only the listed source and target artifacts and the four pre-registered class definitions.

## Per-row vote ledger

Votes are `class/confidence`. `review position` names the disposition and one-based position in the prior review's exact ledger; it was revealed only during scoring.

| ID | review position | origin | source → target | A | B | C | majority | match |
|---|---:|---|---|---|---|---|---|---|
| S19 | EX-01 | `mechanism` | `kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md:70 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX/high | EX/high | EX/high | EX | yes |
| S47 | EX-03 | `mechanism` | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md:62 → kb/notes/indirection-is-costly-in-llm-instructions.md` | EX/high | EX/high | EX/high | EX | yes |
| S09 | EX-05 | `mechanism` | `kb/notes/frontloading-spares-execution-context.md:56 → kb/notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md` | EX/high | EX/high | EX/high | EX | yes |
| S21 | EX-07 | `mechanism` | `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md:45 → kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | EX/high | EX/high | EX/high | EX | yes |
| S26 | EX-09 | `mechanism` | `kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md:38 → kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | EX/high | EX/high | EX/high | EX | yes |
| S46 | EX-11 | `mechanism` | `kb/notes/raw-accumulation-does-not-create-usable-memory.md:32 → kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | EX/high | EX/high | EX/high | EX | yes |
| S38 | EX-13 | `mechanism` | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → kb/notes/ephemeral-computation-prevents-accumulation.md` | EX/high | EX/high | EX/high | EX | yes |
| S03 | EX-15 | `mechanism` | `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:51 → kb/notes/false-positive-generation-is-filtered-before-retention.md` | EX/high | EX/high | EX/high | EX | yes |
| S42 | EX-17 | `mechanism` | `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:81 → kb/notes/codify-versus-llm-decision-heuristics.md` | OP/high | OP/high | OP/high | OP | **no** |
| S36 | EX-19 | `mechanism` | `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:48 → kb/notes/opacity-is-a-scale-threshold.md` | EX/high | EX/high | EX/high | EX | yes |
| S35 | EX-21 | `grounds-deferred` | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:63 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | EX/high | EX/high | EX/high | EX | yes |
| S27 | EX-23 | `grounds-deferred` | `kb/notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:49 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | EX/high | EX/high | EX/high | EX | yes |
| S44 | EX-25 | `grounds-deferred` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:188 → kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` | EX/high | EX/high | EX/high | EX | yes |
| S12 | EX-27 | `grounds-deferred` | `kb/notes/codify-versus-llm-decision-heuristics.md:120 → kb/notes/ephemeral-computation-prevents-accumulation.md` | EX/high | EX/high | EX/high | EX | yes |
| S14 | EX-29 | `grounds-deferred` | `kb/notes/definitions/reach-assessment.md:66 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | EX/medium | OTHER/medium | EX/medium | EX | yes |
| S06 | EX-31 | `grounds-deferred` | `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:47 → kb/notes/definitions/representational-form.md` | EX/high | EX/high | EX/high | EX | yes |
| S08 | EX-33 | `grounds-deferred` | `kb/notes/increasing-computational-autonomy-relocates-human-effort.md:59 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX/high | EX/high | EX/high | EX | yes |
| S05 | EX-35 | `grounds-deferred` | `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md:38 → kb/notes/definitions/system-definition-artifact.md` | EX/medium | EX/high | EX/medium | EX | yes |
| S39 | EX-37 | `grounds-deferred` | `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:43 → kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` | EX/high | EX/high | EX/high | EX | yes |
| S04 | EX-39 | `grounds-deferred` | `kb/notes/runtime-structure-determines-governance-control-surfaces.md:56 → kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md` | EX/high | EX/high | EX/high | EX | yes |
| S32 | EX-41 | `grounds-deferred` | `kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md:73 → kb/notes/synthesis-is-not-error-correction.md` | EX/high | EX/high | EX/high | EX | yes |
| S02 | OP-01 | `mechanism` | `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:102 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP/high | OP/high | OP/high | OP | yes |
| S18 | OP-05 | `mechanism` | `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:28 → kb/notes/llm-context-is-a-homoiconic-medium.md` | EX/high | EX/high | EX/high | EX | **no** |
| S29 | OP-09 | `mechanism` | `kb/notes/definitions/context-engineering.md:65 → kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | OP/high | OP/high | OP/high | OP | yes |
| S45 | OP-13 | `mechanism` | `kb/notes/enforcement-without-structured-recovery-is-incomplete.md:69 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | OP/high | OP/high | OP/high | OP | yes |
| S28 | OP-17 | `mechanism` | `kb/notes/feasibility-is-the-heaviest-forks-net-load.md:37 → kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | OP/high | OP/high | OP/high | OP | yes |
| S10 | OP-21 | `mechanism` | `kb/notes/llm-context-is-composed-without-scoping.md:75 → kb/notes/agent-statelessness-means-the-context-engine-should-inject-context.md` | OP/high | OP/high | OP/high | OP | yes |
| S25 | OP-25 | `mechanism` | `kb/notes/methodological-and-computational-closure-track-different-changes.md:80 → kb/notes/reflection-buys-addressability.md` | EX/high | EN/high | EX/medium | EX | **no** |
| S13 | OP-29 | `mechanism` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → kb/notes/verifiability-gradient.md` | OTHER/medium | OTHER/high | EX/medium | OTHER | **no** |
| S11 | OP-33 | `mechanism` | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | EX/medium | EX/medium | EX/high | EX | **no** |
| S01 | OP-37 | `mechanism` | `kb/notes/stale-self-description-conceals-its-own-staleness.md:70 → kb/notes/reflection-buys-addressability.md` | EX/high | EX/high | EX/high | EX | **no** |
| S22 | OP-41 | `mechanism` | `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:46 → kb/notes/definitions/codification.md` | OP/high | OP/high | OP/high | OP | yes |
| S23 | OP-45 | `mechanism` | `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:60 → kb/notes/retrieval-failure-is-reflection-failure.md` | OP/medium | OP/high | OP/high | OP | yes |
| S15 | OP-49 | `mechanism` | `kb/notes/verifiable-subroles-before-reviewer-identity.md:62 → kb/notes/structured-output-is-easier-for-humans-to-review.md` | OP/high | OP/high | OP/high | OP | yes |
| S37 | OP-53 | `grounds-deferred` | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:59 (baseline 77) → kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` | OTHER/medium | OTHER/medium | EX/medium | OTHER | **no** |
| S43 | OP-57 | `grounds-deferred` | `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:30 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX/high | EX/high | EX/high | EX | **no** |
| S16 | OP-61 | `grounds-deferred` | `kb/notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → kb/notes/frontloading-spares-execution-context.md` | OP/high | OP/medium | OP/medium | OP | yes |
| S41 | OP-65 | `grounds-deferred` | `kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md:50 → kb/notes/spec-mining-as-codification.md` | OP/high | OP/high | OP/high | OP | yes |
| S30 | OP-69 | `grounds-deferred` | `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:44 → kb/notes/process-structure-and-output-structure-are-independent-levers.md` | EX/medium | OTHER/medium | EX/high | EX | **no** |
| S40 | EN-01 | `mechanism` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | EN/medium | EN/high | EX/medium | EN | yes |
| S48 | EN-02 | `mechanism` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:190 → kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md` | EN/high | EN/high | OP/medium | EN | yes |
| S34 | EN-03 | `mechanism` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:191 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EX/high | EN/high | EX/high | EX | **no** |
| S24 | EN-04 | `mechanism` | `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md:56 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EX/high | EX/high | EX/high | EX | **no** |
| S49 | EN-05 | `mechanism` | `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:112 → kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md` | EX/high | EX/high | EX/high | EX | **no** |
| S07 | EN-06 | `mechanism` | `kb/notes/verifiable-subroles-before-reviewer-identity.md:58 → kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` | EX/high | EX/high | EX/high | EX | **no** |
| S20 | EN-07 | `mechanism` | `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EX/high | EN/high | EX/high | EX | **no** |
| S31 | EN-08 | `grounds-deferred` | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX/high | EN/high | EN/high | EN | yes |
| S17 | EN-09 | `grounds-deferred` | `kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | EX/medium | EN/high | EN/medium | EN | yes |
| S33 | EN-10 | `grounds-deferred` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | EN/high | EN/high | EN/high | EN | yes |

## Diagnostic classifier rationales

Rationales are retained for every non-unanimous row and every row whose majority did not reproduce the review. Unanimous matching rows remain fully represented by their votes above.

### S01 — review OP-37; majority EX

`kb/notes/stale-self-description-conceals-its-own-staleness.md:70 → kb/notes/reflection-buys-addressability.md`

- A — EX/high: Reflection's addressability principle explains why a retained self-claim can be found and selectively revised.
- B — EX/high: Reflection's addressability account explains how a retained commitment becomes selectively revisable; it is not the synchronization operation itself.
- C — EX/high: Reflection explains why retaining a claim in a readable self-representation makes selective revision addressable.

### S07 — review EN-06; majority EX

`kb/notes/verifiable-subroles-before-reviewer-identity.md:58 → kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`

- A — EX/high: Per-instance discrimination explains why aggregate review quality cannot justify automating a bundled reviewer role.
- B — EX/high: The discrimination principle explains why aggregate review quality cannot justify automation when unsupported findings cannot be identified per instance.
- C — EX/high: Per-instance discrimination explains why aggregate review accuracy cannot justify automating a bundled reviewer role.

### S11 — review OP-33; majority EX

`kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → kb/notes/deploy-time-learning-is-the-missing-middle.md`

- A — EX/medium: The deploy-time-learning account explains why cross-session capability registration is durable behavioral adaptation rather than transient context use.
- B — EX/medium: The deploy-time-learning account explains why persisting an online-registered capability across sessions constitutes durable behavioral change.
- C — EX/high: Deploy-time learning explains why retaining a generated capability across sessions constitutes a durable behavior-change loop.

### S13 — review OP-29; majority OTHER

`kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → kb/notes/verifiability-gradient.md`

- A — OTHER/medium: The target supplies a placement scale for describing the promotion's hardening, not its cause, operating path, or required precondition.
- B — OTHER/high: The target is a descriptive placement scale used to characterize promotion as hardening; it neither performs nor enables the promotion gate.
- C — EX/medium: The verifiability gradient explains the loose-to-deterministic movement that a tested promotion gate is intended to enforce.

### S14 — review EX-29; majority EX

`kb/notes/definitions/reach-assessment.md:66 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`

- A — EX/medium: The boundary-statability argument explains why natural-language reach assessment requires a judgment capability beyond mechanical boundary matching.
- B — OTHER/medium: The target is the motivating precursor that exposes an unresolved boundary-judgment problem; it does not explain or execute reach-assessment.
- C — EX/medium: The boundary-statability account explains why judging a natural-language commitment's scope is a substantive capability rather than mechanical matching.

### S17 — review EN-09; majority EN

`kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

- A — EX/medium: The diagnostic-richness principle explains how preserved failure evidence makes a lesson's applicability boundary inferable.
- B — EN/high: Inspectable, diagnostically rich failure evidence must survive for a learner to recover the directive and applicability boundary needed for abstraction.
- C — EN/medium: Inspectable diagnostic evidence must survive processing for the abstraction step to recover the failure boundary carried by directive feedback.

### S18 — review OP-05; majority EX

`kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:28 → kb/notes/llm-context-is-a-homoiconic-medium.md`

- A — EX/high: Homoiconicity explains how readable retained content can be consumed as instruction and thereby change behavior.
- B — EX/high: Homoiconicity explains how readable natural-language artifacts can enter context as behavior-shaping instruction rather than only inert data.
- C — EX/high: Homoiconicity explains how readable text can function as executable instruction rather than remaining only stored data.

### S20 — review EN-07; majority EX

`kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`

- A — EX/high: The target explains when weak checks can yield a stronger composite: positive discrimination plus sufficiently decorrelated errors.
- B — EN/high: Above-chance discrimination and sufficiently decorrelated errors must hold before heterogeneous weak checks can amplify into a stronger composite oracle.
- C — EX/high: The error-correction account explains how discriminative, decorrelated weak checks can combine into a stronger composite oracle.

### S24 — review EN-04; majority EX

`kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md:56 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`

- A — EX/high: The TPR-over-FPR amplification account explains why discrimination, rather than aggregate accuracy or calibration, controls automation.
- B — EX/high: The TPR-over-FPR amplification account explains why discrimination, rather than calibration or aggregate accuracy, determines whether repeated checking can help.
- C — EX/high: The error-correction theory explains why amplification depends on discrimination, expressed as TPR exceeding FPR, rather than aggregate accuracy.

### S25 — review OP-25; majority EX

`kb/notes/methodological-and-computational-closure-track-different-changes.md:80 → kb/notes/reflection-buys-addressability.md`

- A — EX/high: Reflection's addressability account explains why explicit retained inputs and criteria can be delivered to later deciding processes.
- B — EN/high: Addressable representation must be available before a later computational decider can receive, inspect, and apply retained inputs or criteria.
- C — EX/medium: Reflection's addressability account explains how retained inputs and criteria become available to later deciding processes.

### S30 — review OP-69; majority EX

`kb/notes/reasoning-production-is-not-reasoning-evaluation.md:44 → kb/notes/process-structure-and-output-structure-are-independent-levers.md`

- A — EX/medium: The independence of process and output structure supplies the general reason that destination correctness and route validity require separate checks.
- B — OTHER/medium: The target supplies a parallel conceptual distinction between result shape and reasoning process, not a cause, prerequisite, or review operation for answer-reconstruction bias.
- C — EX/high: The process/output-structure distinction explains why reasoning-path validity and final-result correctness require separate checks.

### S31 — review EN-08; majority EN

`kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md`

- A — EX/high: The verification-boundary principle explains why enforce-or-omit is available only when a cheap deterministic comparison oracle exists.
- B — EN/high: A cheap deterministic oracle able to re-derive and compare the copy must exist for the checked branch; without it only omission is safe.
- C — EN/high: A cheap deterministic verifier must be available to re-derive and compare a copy before the source's checked branch is safe; otherwise only omission remains.

### S34 — review EN-03; majority EX

`kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:191 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`

- A — EX/high: The target explains the discrimination and decorrelation conditions under which heterogeneous weak maintainability checks can amplify.
- B — EN/high: Genuine discrimination and sufficiently independent failure modes must hold before heterogeneous weak maintainability checks can amplify.
- C — EX/high: The amplification theory explains when heterogeneous weak maintainability checks can jointly yield a stronger oracle.

### S37 — review OP-53; majority OTHER

`kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:59 (baseline 77) → kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`

- A — OTHER/medium: The target supplies the broader authority-lineage risk frame and rollback vocabulary, but it neither causes nor implements the authorization-bypass channel.
- B — OTHER/medium: The target provides the broader authority-plus-lineage risk framing and rollback vocabulary that the source develops, rather than the source's causal or operating mechanism.
- C — EX/medium: The four-field risk account explains the authority-plus-lineage security conjunction that the source develops into an authorization boundary.

### S40 — review EN-01; majority EN

`kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`

- A — EN/medium: A statable applicability boundary is an additional condition that must hold before a process-verified episode can safely become a transferable rule.
- B — EN/high: A trustworthy abstraction requires a statable applicability boundary; process verification supplies evidence toward that prerequisite but does not replace it.
- C — EX/medium: The boundary-statability principle explains why transferring a rule requires checking its mechanism rather than merely confirming one successful outcome.

### S42 — review EX-17; majority OP

`kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:81 → kb/notes/codify-versus-llm-decision-heuristics.md`

- A — OP/high: The codify-versus-LLM heuristics are an operational decision rule for choosing the representational lever inside the constrained objective space.
- B — OP/high: The codify-versus-LLM heuristics are the concrete decision rule used to allocate a sub-objective between symbolic code and model judgment.
- C — OP/high: The codify-versus-LLM heuristics are the operational decision rule used to place a sub-objective on the symbolic or interpreted side.

### S43 — review OP-57; majority EX

`kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:30 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md`

- A — EX/high: The verification-boundary principle explains why prose discovery lacks an automatic oracle and therefore retains a human judge.
- B — EX/high: The verification-boundary principle explains why prose discovery lacks an automatic oracle and therefore leaves human judgment load-bearing in the adversarial loop.
- C — EX/high: The verification-boundary principle explains why prose discovery lacks an automatic oracle and must retain a judging function elsewhere in the loop.

### S48 — review EN-02; majority EN

`kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:190 → kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md`

- A — EN/high: Failure comprehension, specification, and judge calibration must be completed before automated optimization can safely receive authority.
- B — EN/high: Failure observation, specification, and judge calibration must be completed before automated optimization can safely receive authority.
- C — OP/medium: The comprehension-to-specification-to-generalization sequence is the stage-gated operating rule for introducing automated optimization safely.

### S49 — review EN-05; majority EX

`kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:112 → kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md`

- A — EX/high: The oracle-domain principle explains why criticism can warrant unattended validation only over cases its evaluator can discriminate.
- B — EX/high: Oracle-domain theory explains why judgment-heavy criticism can warrant unattended validation only over cases its evaluator can reliably discriminate.
- C — EX/high: Oracle-domain theory explains why criticism can warrant unattended validation only over cases its evaluator can discriminate reliably.

## Classifier provenance

Requested model: no explicit override; three fresh default Codex collaboration subagents, each in an isolated context. Actual model information reported by each pass:

- A: Codex, based on GPT-5.
- B: Codex, based on GPT-5.
- C: Codex, based on GPT-5.

No stronger provider, checkpoint, or parameter provenance was exposed, so none is claimed.

## Changed paths

This test writes only `kb/work/linking-contract-consistency/blind-mechanism-reclassification-results.md`. It changes no corpus edge, collection contract, catalogue entry, ADR, durable instruction, or prior workshop result.
