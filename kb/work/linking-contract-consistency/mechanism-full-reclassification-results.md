# Full mechanism reclassification results

**Date:** 2026-07-29

**Status:** complete; replacement evidence ledger passes its pre-registered stability rule; maintainer adjudication still required before vocabulary adoption or migration.

**Protocol:** [full mechanism reclassification protocol](./mechanism-full-reclassification-protocol.md)

**Frozen surface:** [manifest TSV](./mechanism-full-reclassification-manifest.tsv)

**All boundary records:** [387-vote TSV](./mechanism-full-reclassification-votes.tsv)

## Result

The replacement run is usable: 127/129 rows (98.4%) have a stable 2/3-or-better majority, above the pre-registered 90% floor. 101 rows (78.3%) are unanimous, 26 (20.2%) have a 2/3 contested majority, and 2 (1.6%) are UNSTABLE.

The stable replacement ledger contains 65 EX, 40 OP, 18 OTHER, and 4 EN rows. The EX and OP cohorts are both large, cross-file, and highly reproducible: EX spans 58 source artifacts with 56 unanimous rows; OP spans 33 source artifacts with 31 unanimous rows. Both classes occur in active `mechanism` and deferred-`grounds` origins. The full run therefore restores a strong evidential case for an explanatory/operational distinction while replacing the prior row assignments.

This result does not adopt `explained-by` or `operates-through`. Under the protocol, the 26 contested rows require explicit maintainer adjudication before migration, the two unstable rows have no successor candidate, and EN/OTHER rows remain outside either proposed successor.

## Acceptance and distribution

| measure | count | share | rule/readout |
|---|---:|---:|---|
| Stable majority | 127/129 | 98.4% | pass: ≥90% |
| Unanimous | 101/129 | 78.3% | reproducible candidate dispositions |
| Contested 2/3 | 26/129 | 20.2% | maintainer adjudication required |
| UNSTABLE | 2/129 | 1.6% | no successor candidate |

### Majority by origin

| origin | EX | OP | EN | OTHER | UNSTABLE | total |
|---|---:|---:|---:|---:|---:|---:|
| `mechanism` | 37 | 33 | 2 | 8 | 2 | 82 |
| `grounds-deferred` | 28 | 7 | 2 | 10 | 0 | 47 |
| **total** | **65** | **40** | **4** | **18** | **2** | **129** |

### Reproducibility by majority class

| majority class | stable rows | source artifacts | unanimous | contested |
|---|---:|---:|---:|---:|
| EX | 65 | 58 | 56 | 9 |
| OP | 40 | 33 | 31 | 9 |
| EN | 4 | 3 | 2 | 2 |
| OTHER | 18 | 18 | 12 | 6 |

## Rebaseline and attrition

The frozen current surface is 129 tuples: 82 active `mechanism` edges and 47 surviving members of the exact deferred-`grounds` cohort. All 129 source and target artifacts resolved at dispatch, all received three votes, and a post-run tuple check found no runtime deletion or movement.

Relative to the prior 128-row review, all 79 old active-`mechanism` tuples remain and three new active tuples arrived. Two of the 49 deferred-`grounds` tuples disappeared before dispatch, leaving 47. These two are pre-dispatch attrition and were excluded rather than silently retained:

- prior EX: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md` → `kb/notes/definitions/reflective-system.md`;
- prior OP: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md` → `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`.

The three additions and all line movements are recorded in the protocol and manifest.

## Comparison with the prior review

| prior disposition | EX | OP | EN | OTHER | UNSTABLE | total |
|---|---:|---:|---:|---:|---:|---:|
| EX | 29 | 5 | 0 | 6 | 0 | 40 |
| OP | 25 | 33 | 0 | 11 | 2 | 71 |
| EN | 6 | 1 | 3 | 0 | 0 | 10 |
| X | 2 | 1 | 0 | 0 | 0 | 3 |
| P | 1 | 0 | 0 | 0 | 0 | 1 |
| E | 0 | 0 | 0 | 1 | 0 | 1 |
| NEW | 2 | 0 | 1 | 0 | 0 | 3 |

On the 111 surviving rows previously assigned EX or OP, only 62 (55.9%) retain the same majority. Direct EX↔OP reversal affects 30 (27.0%), boundary movement to EN/OTHER affects 17 (15.3%), and 2 (1.8%) are unstable. Prior EX reproduces on 29/40 rows; prior OP reproduces on 33/71.

The full run therefore confirms the blind sample’s central finding: the old 41/72 row ledger is not an adoption or migration basis. It also adds the evidence the sample could not provide: after every row is classified with k=3 and explicit counterfactuals, two substantial reproducible cohorts remain.

### New rows

| ID | edge | votes | majority | status |
|---|---|---|---|---|
| F032 | `kb/notes/reflection-buys-addressability.md:68 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md` | EN/EN/EX | EN | contested |
| F068 | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:70 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md` | EX/EX/EX | EX | unanimous |
| F091 | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:57 → kb/notes/llm-context-is-a-homoiconic-medium.md` | EX/EX/EX | EX | unanimous |

## Evidence for and against retaining the split

### For

- EX and OP are not marginal residue: 65 and 40 stable rows respectively, spanning 58 and 33 source artifacts.
- The distinction survives origin changes. EX includes 37 active-`mechanism` and 28 deferred-`grounds` rows; OP includes 33 and 7.
- The most reproducible cores are large: 56 unanimous EX rows and 31 unanimous OP rows.
- Classifier counterfactuals repeatedly produce different maintenance consequences: rejecting an EX target reopens the source explanation; changing an OP target reopens interface, behavior, or operational fit.
- One broad current candidate would be false for a material cohort: `explained-by` would misstate literal execution paths, while `operates-through` would misstate explanatory principles.

### Against and limits

- The old `mechanism` surface is not binary: 18 stable OTHER rows, 4 EN rows, and 2 unstable rows require other treatment.
- Twenty-six stable rows are only 2/3 majorities. The protocol deliberately withholds them from automatic migration.
- OTHER is a coarse catch-all in this run. Its rationales must be mapped to exact existing relations or prose during adjudication; an OTHER majority is not itself a successor label.
- The three classifiers per row were fresh isolated contexts but all reported the Codex/GPT-5 family. The run measures context-level independence, not cross-model-family agreement.
- The four-class prompt tests this boundary, not every neighbouring registered label simultaneously. Exact mapping to `extends`, `exemplifies`, `premised-on`, evidence labels, or removal still requires adjudication where relevant.

## Reader and revision consequences

- **EX candidate:** source is `explained-by` target. Follow when the reader needs the account or principle that explains why/how the source occurs. Rejecting or materially revising the target prompts re-reading the source causal argument; it does not by itself assert an implementation change.
- **OP candidate:** source `operates-through` target. Follow when the reader needs the actual process, component, control path, artifact, or rule producing the source effect. Changing the target prompts interface, behavioral, or operational-fit review.

The full run supports taking these two consequences back to maintainer adjudication as distinct registered relations. It does not settle the spellings or authorize the one reference→notes pairing. Those remain maintainer choices.

## Exact cohorts

- **EX unanimous (56):** `F001`, `F002`, `F003`, `F007`, `F008`, `F009`, `F011`, `F012`, `F016`, `F017`, `F018`, `F019`, `F021`, `F022`, `F023`, `F024`, `F029`, `F036`, `F039`, `F049`, `F056`, `F058`, `F059`, `F064`, `F065`, `F067`, `F068`, `F069`, `F073`, `F074`, `F075`, `F078`, `F079`, `F081`, `F082`, `F083`, `F087`, `F089`, `F090`, `F091`, `F093`, `F096`, `F097`, `F098`, `F099`, `F100`, `F101`, `F105`, `F106`, `F110`, `F114`, `F117`, `F120`, `F123`, `F126`, `F128`
- **EX contested (9):** `F026`, `F027`, `F035`, `F040`, `F044`, `F050`, `F052`, `F063`, `F071`
- **OP unanimous (31):** `F004`, `F005`, `F010`, `F014`, `F020`, `F025`, `F033`, `F034`, `F037`, `F038`, `F041`, `F045`, `F047`, `F054`, `F055`, `F060`, `F061`, `F070`, `F072`, `F076`, `F077`, `F084`, `F085`, `F108`, `F109`, `F118`, `F121`, `F124`, `F125`, `F127`, `F129`
- **OP contested (9):** `F013`, `F046`, `F053`, `F057`, `F086`, `F104`, `F111`, `F116`, `F119`
- **EN unanimous (2):** `F094`, `F107`
- **EN contested (2):** `F032`, `F092`
- **OTHER unanimous (12):** `F015`, `F030`, `F031`, `F043`, `F051`, `F062`, `F066`, `F095`, `F103`, `F112`, `F113`, `F122`
- **OTHER contested (6):** `F006`, `F042`, `F048`, `F080`, `F088`, `F102`
- **UNSTABLE (2):** `F028`, `F115`

## Per-row replacement ledger

Votes are `class/confidence`. Full boundary-test answers and justifications for every vote are in the linked 387-vote TSV.

| ID | origin | source → target | prior | A | B | C | majority | status |
|---|---|---|---|---|---|---|---|---|
| F001 | `mechanism` | `kb/notes/stale-self-description-conceals-its-own-staleness.md:70 → kb/notes/reflection-buys-addressability.md` | OP | EX/high | EX/medium | EX/high | EX | unanimous |
| F002 | `grounds-deferred` | `kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:36 → kb/notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md` | P | EX/high | EX/high | EX/high | EX | unanimous |
| F003 | `mechanism` | `kb/notes/raw-accumulation-does-not-create-usable-memory.md:31 → kb/notes/constraining-and-extraction-both-trade-generality-for-reliability.md` | EX | EX/medium | EX/medium | EX/medium | EX | unanimous |
| F004 | `mechanism` | `kb/notes/links-encode-conditional-possibilities-not-obligations.md:107 → kb/notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md` | OP | OP/high | OP/medium | OP/high | OP | unanimous |
| F005 | `mechanism` | `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:102 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F006 | `mechanism` | `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:51 → kb/notes/false-positive-generation-is-filtered-before-retention.md` | EX | OTHER/medium | OTHER/medium | OP/medium | OTHER | **contested** |
| F007 | `grounds-deferred` | `kb/notes/runtime-structure-determines-governance-control-surfaces.md:56 → kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F008 | `mechanism` | `kb/notes/the-framework-is-often-larger-than-the-durable-contribution.md:63 → kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | X | EX/high | EX/high | EX/medium | EX | unanimous |
| F009 | `mechanism` | `kb/notes/pointer-design-tradeoffs-in-progressive-disclosure.md:80 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP | EX/medium | EX/medium | EX/medium | EX | unanimous |
| F010 | `mechanism` | `kb/notes/commitment-not-derivation-creates-new-ground-truth.md:92 → kb/notes/progressive-constraining-commits-only-after-patterns-stabilize.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F011 | `mechanism` | `kb/notes/design-for-the-first-time-human-except-on-access-cost.md:28 → kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | OP | EX/medium | EX/medium | EX/medium | EX | unanimous |
| F012 | `grounds-deferred` | `kb/notes/scenario-decomposition-drives-architecture.md:86 → kb/notes/skills-derive-from-methodology.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F013 | `mechanism` | `kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:58 → kb/notes/axes-of-artifact-analysis.md` | OP | OP/high | EX/medium | OP/high | OP | **contested** |
| F014 | `mechanism` | `kb/notes/definitions/context-engineering.md:64 → kb/notes/llm-context-is-composed-without-scoping.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F015 | `mechanism` | `kb/notes/the-framework-is-often-larger-than-the-durable-contribution.md:62 → kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` | OP | OTHER/medium | OTHER/high | OTHER/high | OTHER | unanimous |
| F016 | `grounds-deferred` | `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:56 → kb/notes/llm-context-is-composed-without-scoping.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F017 | `grounds-deferred` | `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md:38 → kb/notes/definitions/system-definition-artifact.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F018 | `grounds-deferred` | `kb/notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:47 → kb/notes/definitions/representational-form.md` | EX | EX/high | EX/high | EX/medium | EX | unanimous |
| F019 | `mechanism` | `kb/notes/verifiable-subroles-before-reviewer-identity.md:58 → kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` | EN | EX/high | EX/high | EX/high | EX | unanimous |
| F020 | `mechanism` | `kb/notes/the-practical-scheduler-is-the-host-language.md:66 → kb/notes/agent-is-a-tool-loop.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F021 | `grounds-deferred` | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:70 → kb/notes/text-testing-framework.md` | OP | EX/high | EX/high | EX/medium | EX | unanimous |
| F022 | `mechanism` | `kb/notes/verifiable-subroles-before-reviewer-identity.md:60 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | OP | EX/high | EX/medium | EX/high | EX | unanimous |
| F023 | `grounds-deferred` | `kb/notes/increasing-computational-autonomy-relocates-human-effort.md:59 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F024 | `mechanism` | `kb/notes/frontloading-spares-execution-context.md:56 → kb/notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md` | EX | EX/high | EX/medium | EX/medium | EX | unanimous |
| F025 | `mechanism` | `kb/notes/llm-context-is-composed-without-scoping.md:75 → kb/notes/agent-statelessness-means-the-context-engine-should-inject-context.md` | OP | OP/high | OP/medium | OP/high | OP | unanimous |
| F026 | `grounds-deferred` | `kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md` | OP | OTHER/medium | EX/medium | EX/medium | EX | **contested** |
| F027 | `mechanism` | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | OP | OTHER/medium | EX/high | EX/high | EX | **contested** |
| F028 | `mechanism` | `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:60 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | OP | OP/high | EX/medium | OTHER/high | UNSTABLE | **UNSTABLE** |
| F029 | `mechanism` | `kb/notes/session-history-should-not-be-the-default-next-context.md:82 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP | EX/medium | EX/medium | EX/medium | EX | unanimous |
| F030 | `grounds-deferred` | `kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:64 → kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` | EX | OTHER/medium | OTHER/high | OTHER/high | OTHER | unanimous |
| F031 | `mechanism` | `kb/notes/design-for-the-first-time-human-except-on-access-cost.md:26 → kb/notes/feasibility-is-the-heaviest-forks-net-load.md` | OP | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F032 | `mechanism` | `kb/notes/reflection-buys-addressability.md:68 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md` | NEW | EN/high | EN/medium | EX/high | EN | **contested** |
| F033 | `mechanism` | `kb/notes/feasibility-is-the-heaviest-forks-net-load.md:38 → kb/notes/session-history-should-not-be-the-default-next-context.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F034 | `mechanism` | `kb/notes/bounded-context-orchestration-model.md:92 → kb/notes/llm-context-is-composed-without-scoping.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F035 | `grounds-deferred` | `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → kb/notes/bounded-context-orchestration-model.md` | OP | OP/high | EX/high | EX/medium | EX | **contested** |
| F036 | `mechanism` | `kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:69 → kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F037 | `mechanism` | `kb/notes/structure-inference-needs-capture-at-the-decision-surface.md:37 → kb/notes/spec-mining-as-codification.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F038 | `grounds-deferred` | `kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:64 → kb/notes/llm-context-is-composed-without-scoping.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F039 | `grounds-deferred` | `kb/notes/reverse-compression-is-when-llm-output-expands-without-adding.md:43 → kb/notes/information-value-is-observer-relative.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F040 | `mechanism` | `kb/notes/retrieval-failure-is-reflection-failure.md:40 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | EX | EX/high | EX/high | OP/medium | EX | **contested** |
| F041 | `mechanism` | `kb/notes/entropy-management-must-scale-with-generation-throughput.md:31 → kb/notes/spec-mining-as-codification.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F042 | `grounds-deferred` | `kb/notes/semantic-review-catches-content-errors-that-structural-validation.md:49 → kb/notes/text-testing-framework.md` | OP | OTHER/high | OP/medium | OTHER/high | OTHER | **contested** |
| F043 | `mechanism` | `kb/notes/bounded-context-orchestration-model.md:97 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F044 | `mechanism` | `kb/notes/error-messages-that-teach-are-a-constraining-technique.md:28 → kb/notes/frontloading-spares-execution-context.md` | OP | OP/high | EX/high | EX/high | EX | **contested** |
| F045 | `mechanism` | `kb/notes/feasibility-is-the-heaviest-forks-net-load.md:36 → kb/notes/frontloading-spares-execution-context.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F046 | `grounds-deferred` | `kb/notes/codify-versus-llm-decision-heuristics.md:120 → kb/notes/ephemeral-computation-prevents-accumulation.md` | EX | OP/medium | OP/high | EX/high | OP | **contested** |
| F047 | `mechanism` | `kb/notes/definitions/context-engineering.md:63 → kb/notes/instruction-specificity-should-match-loading-frequency.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F048 | `grounds-deferred` | `kb/notes/llm-context-is-composed-without-scoping.md:72 → kb/notes/instruction-specificity-should-match-loading-frequency.md` | OP | OTHER/high | OTHER/high | OP/medium | OTHER | **contested** |
| F049 | `mechanism` | `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md:60 → kb/notes/llm-context-is-a-homoiconic-medium.md` | OP | EX/high | EX/high | EX/medium | EX | unanimous |
| F050 | `mechanism` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → kb/notes/verifiability-gradient.md` | OP | OTHER/high | EX/medium | EX/medium | EX | **contested** |
| F051 | `grounds-deferred` | `kb/notes/definitions/reach-assessment.md:66 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | EX | OTHER/high | OTHER/medium | OTHER/medium | OTHER | unanimous |
| F052 | `mechanism` | `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:84 → kb/notes/oracle-strength-spectrum.md` | EX | EX/medium | OTHER/medium | EX/high | EX | **contested** |
| F053 | `mechanism` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:49 → kb/notes/deploy-time-learning-is-the-missing-middle.md` | OP | OP/medium | EX/medium | OP/high | OP | **contested** |
| F054 | `mechanism` | `kb/notes/verifiable-subroles-before-reviewer-identity.md:62 → kb/notes/structured-output-is-easier-for-humans-to-review.md` | OP | OP/high | OP/medium | OP/high | OP | unanimous |
| F055 | `mechanism` | `kb/notes/stale-self-description-conceals-its-own-staleness.md:71 → kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md` | OP | OP/medium | OP/high | OP/medium | OP | unanimous |
| F056 | `grounds-deferred` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:39 → kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F057 | `grounds-deferred` | `kb/notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → kb/notes/frontloading-spares-execution-context.md` | OP | OP/high | OP/medium | OTHER/high | OP | **contested** |
| F058 | `grounds-deferred` | `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:28 → kb/notes/llm-generation-relaxes-goals-where-human-writing-stalls.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F059 | `grounds-deferred` | `kb/notes/reflection-makes-retained-lessons-second-order.md:49 → kb/notes/reflection-buys-addressability.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F060 | `mechanism` | `kb/notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md:63 → kb/notes/scenario-decomposition-drives-architecture.md` | OP | OP/medium | OP/medium | OP/medium | OP | unanimous |
| F061 | `mechanism` | `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:46 → kb/notes/reflection-makes-retained-lessons-second-order.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F062 | `mechanism` | `kb/notes/task-fitted-structure-costs-cross-task-reuse.md:71 → kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md` | EX | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F063 | `grounds-deferred` | `kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | EN | EX/medium | EX/high | EN/medium | EX | **contested** |
| F064 | `mechanism` | `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:28 → kb/notes/llm-context-is-a-homoiconic-medium.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F065 | `grounds-deferred` | `kb/notes/an-action-model-matters-only-through-its-consumption-path.md:24 → kb/notes/axes-of-artifact-analysis.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F066 | `grounds-deferred` | `kb/notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md:72 → kb/notes/oracle-strength-spectrum.md` | E | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F067 | `mechanism` | `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:59 → kb/notes/reflection-makes-retained-lessons-second-order.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F068 | `mechanism` | `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:70 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md` | NEW | EX/high | EX/high | EX/high | EX | unanimous |
| F069 | `mechanism` | `kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md:70 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F070 | `mechanism` | `kb/notes/reflection-makes-retained-lessons-second-order.md:53 → kb/notes/retrieval-failure-is-reflection-failure.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F071 | `mechanism` | `kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EN | OTHER/high | EX/high | EX/high | EX | **contested** |
| F072 | `grounds-deferred` | `kb/notes/llm-context-is-a-homoiconic-medium.md:45 → kb/notes/methodology-enforcement-is-constraining.md` | EX | OP/high | OP/high | OP/high | OP | unanimous |
| F073 | `mechanism` | `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md:91 → kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md` | OP | EX/medium | EX/medium | EX/medium | EX | unanimous |
| F074 | `mechanism` | `kb/notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md:45 → kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F075 | `mechanism` | `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md:36 → kb/notes/methodology-enforcement-is-constraining.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F076 | `mechanism` | `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:46 → kb/notes/definitions/codification.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F077 | `mechanism` | `kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:60 → kb/notes/retrieval-failure-is-reflection-failure.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F078 | `mechanism` | `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md:56 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EN | EX/high | EX/high | EX/high | EX | unanimous |
| F079 | `mechanism` | `kb/notes/methodological-and-computational-closure-track-different-changes.md:80 → kb/notes/reflection-buys-addressability.md` | OP | EX/medium | EX/high | EX/high | EX | unanimous |
| F080 | `grounds-deferred` | `kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` | OP | OTHER/high | EX/high | OTHER/high | OTHER | **contested** |
| F081 | `mechanism` | `kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md:38 → kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F082 | `mechanism` | `kb/notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md:59 → kb/notes/llm-generation-confidence-tracks-typicality-not-soundness.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F083 | `grounds-deferred` | `kb/notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:49 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F084 | `mechanism` | `kb/notes/feasibility-is-the-heaviest-forks-net-load.md:37 → kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | OP | OP/medium | OP/medium | OP/high | OP | unanimous |
| F085 | `mechanism` | `kb/notes/definitions/context-engineering.md:65 → kb/notes/agents-navigate-by-deciding-what-to-read-next.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F086 | `mechanism` | `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:59 → kb/notes/definitions/constraining.md` | OP | EX/high | OP/high | OP/high | OP | **contested** |
| F087 | `mechanism` | `kb/notes/deploy-time-learning-is-the-missing-middle.md:56 → kb/notes/llm-context-is-a-homoiconic-medium.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F088 | `grounds-deferred` | `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:44 → kb/notes/process-structure-and-output-structure-are-independent-levers.md` | OP | OTHER/medium | OTHER/high | EX/medium | OTHER | **contested** |
| F089 | `grounds-deferred` | `kb/notes/llm-context-is-composed-without-scoping.md:78 → kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F090 | `grounds-deferred` | `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:49 → kb/notes/reasoning-production-is-not-reasoning-evaluation.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F091 | `mechanism` | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:57 → kb/notes/llm-context-is-a-homoiconic-medium.md` | NEW | EX/high | EX/high | EX/high | EX | unanimous |
| F092 | `grounds-deferred` | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EN | EN/high | EN/high | EX/high | EN | **contested** |
| F093 | `grounds-deferred` | `kb/notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md:73 → kb/notes/synthesis-is-not-error-correction.md` | EX | EX/medium | EX/medium | EX/high | EX | unanimous |
| F094 | `grounds-deferred` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md` | EN | EN/high | EN/high | EN/high | EN | unanimous |
| F095 | `grounds-deferred` | `kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:61 → kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md` | OP | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F096 | `mechanism` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:191 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | EN | EX/high | EX/high | EX/high | EX | unanimous |
| F097 | `grounds-deferred` | `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:66 → kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F098 | `grounds-deferred` | `kb/notes/automated-synthesis-is-missing-good-oracles.md:58 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | X | EX/high | EX/high | EX/high | EX | unanimous |
| F099 | `grounds-deferred` | `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:63 → kb/notes/stale-indexes-are-worse-than-no-indexes.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F100 | `mechanism` | `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:48 → kb/notes/opacity-is-a-scale-threshold.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F101 | `mechanism` | `kb/notes/spec-mining-as-codification.md:59 → kb/notes/oracle-strength-spectrum.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F102 | `grounds-deferred` | `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:59 → kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md` | OP | EX/medium | OTHER/high | OTHER/high | OTHER | **contested** |
| F103 | `mechanism` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:50 → kb/notes/definitions/codification.md` | OP | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F104 | `mechanism` | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → kb/notes/ephemeral-computation-prevents-accumulation.md` | EX | OP/high | EX/high | OP/high | OP | **contested** |
| F105 | `mechanism` | `kb/notes/false-positive-generation-is-filtered-before-retention.md:69 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F106 | `grounds-deferred` | `kb/notes/reasoning-production-is-not-reasoning-evaluation.md:43 → kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` | EX | EX/high | EX/medium | EX/medium | EX | unanimous |
| F107 | `mechanism` | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | EN | EN/high | EN/high | EN/high | EN | unanimous |
| F108 | `grounds-deferred` | `kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md:50 → kb/notes/spec-mining-as-codification.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F109 | `mechanism` | `kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:81 → kb/notes/codify-versus-llm-decision-heuristics.md` | EX | OP/high | OP/high | OP/high | OP | unanimous |
| F110 | `grounds-deferred` | `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:30 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | OP | EX/high | EX/high | EX/high | EX | unanimous |
| F111 | `mechanism` | `kb/notes/reflective-coverage-is-graded-across-representational-forms.md:100 → kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md` | OP | OP/high | OP/medium | OTHER/high | OP | **contested** |
| F112 | `mechanism` | `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:54 → kb/notes/verifiability-gradient.md` | EX | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F113 | `grounds-deferred` | `kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:62 → kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` | EX | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F114 | `grounds-deferred` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:188 → kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F115 | `mechanism` | `kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md:46 → kb/notes/spec-mining-as-codification.md` | OP | OP/high | OTHER/high | EX/medium | UNSTABLE | **UNSTABLE** |
| F116 | `mechanism` | `kb/notes/bounded-context-orchestration-model.md:90 → kb/notes/frontloading-spares-execution-context.md` | X | OTHER/medium | OP/high | OP/high | OP | **contested** |
| F117 | `grounds-deferred` | `kb/notes/frontloading-spares-execution-context.md:53 → kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F118 | `mechanism` | `kb/notes/enforcement-without-structured-recovery-is-incomplete.md:69 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | OP | OP/high | OP/medium | OP/high | OP | unanimous |
| F119 | `grounds-deferred` | `kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → kb/notes/frontloading-spares-execution-context.md` | OP | OP/medium | EX/high | OP/high | OP | **contested** |
| F120 | `mechanism` | `kb/notes/raw-accumulation-does-not-create-usable-memory.md:32 → kb/notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F121 | `mechanism` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:48 → kb/notes/ephemeral-computation-prevents-accumulation.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F122 | `mechanism` | `kb/notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md:61 → kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md` | OP | OTHER/high | OTHER/high | OTHER/high | OTHER | unanimous |
| F123 | `mechanism` | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md:62 → kb/notes/indirection-is-costly-in-llm-instructions.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F124 | `mechanism` | `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md:35 → kb/notes/session-history-should-not-be-the-default-next-context.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F125 | `mechanism` | `kb/notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md:63 → kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md` | OP | OP/high | OP/high | OP/high | OP | unanimous |
| F126 | `grounds-deferred` | `kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md:55 → kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | EX | EX/high | EX/high | EX/high | EX | unanimous |
| F127 | `mechanism` | `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md:190 → kb/notes/evaluation-automation-is-phase-gated-by-comprehension.md` | EN | OP/high | OP/high | OP/high | OP | unanimous |
| F128 | `mechanism` | `kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:112 → kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md` | EN | EX/high | EX/medium | EX/high | EX | unanimous |
| F129 | `grounds-deferred` | `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:46 → kb/notes/bounded-context-orchestration-model.md` | EX | OP/high | OP/high | OP/high | OP | unanimous |

## Contested and unstable diagnostics

Every non-unanimous row is repeated here with the three classifier justifications. The full counterfactual records remain in the vote TSV.

### F006 — OTHER (contested), prior EX

`kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:51 → kb/notes/false-positive-generation-is-filtered-before-retention.md`

- A — OTHER/medium: The target categorizes the failure but does not explain or implement the rationale-specific causal chain.
- B — OTHER/medium: The source analogizes an unassessed rationale to false-positive acceptance, but its wrong-premise mechanism is self-contained.
- C — OP/medium: The target's evaluation-and-retention control path is how an unassessed revision acquires force, though the source also gives a self-contained error account.

### F013 — OP (contested), prior OP

`kb/notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:58 → kb/notes/axes-of-artifact-analysis.md`

- A — OP/high: Artifact analysis is a concrete ontology through which heterogeneous retained artifacts become typed verification targets.
- B — EX/medium: The target is the conceptual ontology that explains the heterogeneous authority paths the source says verification must distinguish.
- C — OP/high: The target is the classification artifact through which heterogeneous verification targets can be typed.

### F026 — EX (contested), prior OP

`kb/notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md`

- A — OTHER/medium: The target situates the phenomenon but does not supply its specific causal account or control path.
- B — EX/medium: The target supplies the broader uncoordinated-composition account under which the observed drift is contamination from absent isolation.
- C — EX/medium: The target generalizes the observed stance drift as contamination caused by composition without a scoping guarantee.

### F027 — EX (contested), prior OP

`kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → kb/notes/deploy-time-learning-is-the-missing-middle.md`

- A — OTHER/medium: The target names the learning category into which Tendril falls but does not explain why the compared systems chose different persistence boundaries.
- B — EX/high: The target explains how cross-session executable artifacts constitute deploy-time behavior change.
- C — EX/high: Deploy-time learning explains why Tendril's retained generated capability is durable behavior change rather than ordinary memory.

### F028 — UNSTABLE (unstable), prior OP

`kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:60 → kb/notes/deploy-time-learning-is-the-missing-middle.md`

- A — OP/high: Deploy-time artifact updates are the operational path by which a rejected interpretation becomes a lasting behavior change.
- B — EX/medium: Deploy-time learning explains how a rejected interpretation retained in an instruction or test can alter later-session behavior.
- C — OTHER/high: The target names the broader adaptation timescale into which the source's persistent correction falls.

### F032 — EN (contested), prior NEW

`kb/notes/reflection-buys-addressability.md:68 → kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md`

- A — EN/high: The target gives the change-topology conditions under which selective revision and rollback actually remain local.
- B — EN/medium: The target supplies the applicability conditions under which selective revision and related addressability advantages remain local.
- C — EX/high: The target causally bounds the payoff by explaining how edit and validation locality arise.

### F035 — EX (contested), prior OP

`kb/notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → kb/notes/bounded-context-orchestration-model.md`

- A — OP/high: The target specifies the scheduler and bounded-call control path whose selection logic is lifted into the compiled workflow.
- B — EX/high: The target explains the choose-next-step structure whose symbolic extraction the source calls compilation.
- C — EX/medium: The target explains the coordination structure whose selection logic is lifted into a persistent symbolic artifact.

### F040 — EX (contested), prior EX

`kb/notes/retrieval-failure-is-reflection-failure.md:40 → kb/notes/stale-indexes-are-worse-than-no-indexes.md`

- A — EX/high: The target explains how an authoritative stale index makes missing knowledge invisible by stopping the fallback search.
- B — EX/high: A seemingly exhaustive but incomplete index explains how discovery is suppressed and the reflective causal wire silently breaks.
- C — OP/medium: A trusted incomplete index is the artifact that literally suppresses fallback discovery and breaks retrieval.

### F042 — OTHER (contested), prior OP

`kb/notes/semantic-review-catches-content-errors-that-structural-validation.md:49 → kb/notes/text-testing-framework.md`

- A — OTHER/high: The target classifies the checks as Level B but is not the mechanism that performs them.
- B — OP/medium: The target is the testing process artifact that the source operationalizes as a Level B semantic-review layer.
- C — OTHER/high: The target supplies a testing taxonomy and catalogue into which the source places its checks, not an explanation or operative mechanism.

### F044 — EX (contested), prior OP

`kb/notes/error-messages-that-teach-are-a-constraining-technique.md:28 → kb/notes/frontloading-spares-execution-context.md`

- A — OP/high: A teaching error message performs frontloading by delivering the remediation instead of making the agent derive it.
- B — EX/high: Frontloading explains why inserting the known remediation into the error channel removes repeated runtime diagnosis work.
- C — EX/high: Frontloading explains why inserting the fix avoids an in-context diagnosis step.

### F046 — OP (contested), prior EX

`kb/notes/codify-versus-llm-decision-heuristics.md:120 → kb/notes/ephemeral-computation-prevents-accumulation.md`

- A — OP/medium: The target's discard path literally produces the no-accumulation cost used by the heuristic.
- B — OP/high: Generate, execute, and discard is the literal operating path that makes the leave-for-LLM side lose cross-run accumulation.
- C — EX/high: The target explains the structural cost of leaving work ephemeral: useful patterns cannot accumulate across runs.

### F048 — OTHER (contested), prior OP

`kb/notes/llm-context-is-composed-without-scoping.md:72 → kb/notes/instruction-specificity-should-match-loading-frequency.md`

- A — OTHER/high: The target organizes progressive disclosure, while the source diagnoses absent local scope and prescribes fresh frames; neither produces the other.
- B — OTHER/high: The target is a policy for reducing always-loaded material, not the cause, control path, or prerequisite of flat context.
- C — OP/medium: The loading hierarchy is the operational policy that selects which instruction bodies enter the otherwise global context.

### F050 — EX (contested), prior OP

`kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → kb/notes/verifiability-gradient.md`

- A — OTHER/high: The target supplies placement vocabulary rather than the test-gated promotion mechanism.
- B — EX/medium: The verifiability gradient explains why test-gated promotion makes a reusable strategy cheaper and safer to trust.
- C — EX/medium: The verifiability gradient explains why tested promotion can support tighter trust and reuse than ephemeral code.

### F052 — EX (contested), prior EX

`kb/notes/technical-constraints-make-kb-objective-choice-engineering.md:84 → kb/notes/oracle-strength-spectrum.md`

- A — EX/medium: Oracle strength explains why descriptive, prescriptive, and theoretical objectives admit different degrees and costs of verification.
- B — OTHER/medium: The target names grades used to describe profile-specific judges but does not produce or causally explain their differing evidence surfaces.
- C — EX/high: Oracle strength is the general principle explaining differences among profile-specific judges.

### F053 — OP (contested), prior OP

`kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:49 → kb/notes/deploy-time-learning-is-the-missing-middle.md`

- A — OP/medium: Test-gated promotion of recurring scheduler fragments is a concrete deploy-time learning loop through durable repository artifacts.
- B — EX/medium: The target gives the general account under which promoting tested control fragments into a durable repository constitutes cross-session learning.
- C — OP/high: Test-gated strategy promotion is literally a deploy-time learning loop over durable artifacts.

### F057 — OP (contested), prior OP

`kb/notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → kb/notes/frontloading-spares-execution-context.md`

- A — OP/high: Frontloading literally produces the source-dependent, use-shaped artifact for which the source note requires lineage.
- B — OP/medium: Frontloading is a literal artifact-production path that can hide source material from the consumer while preserving a maintenance dependency on it.
- C — OTHER/high: The target supplies an illustrative production mode, not the explanation, operating path, or prerequisite for change-time lineage signaling.

### F063 — EX (contested), prior EN

`kb/notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → kb/notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

- A — EX/medium: The target explains how retained traces and failure detail let a learner infer mechanisms and boundaries instead of learning only from outcomes.
- B — EX/high: The target explains how preserved traces and diagnostics let a learner infer the condition that bounds a lesson.
- C — EN/medium: Diagnostic evidence is a necessary available input to boundary formation, while the source supplies the abstraction rule itself.

### F071 — EX (contested), prior EN

`kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`

- A — OTHER/high: The target addresses how to mitigate weak selection, not why weakly discriminated qualities are underselected.
- B — EX/high: The target explains when several weak quality checks can exert stronger selection pressure together.
- C — EX/high: The target explains when multiple partial quality checks can overcome weak individual discrimination instead of amplifying shared blind spots.

### F080 — OTHER (contested), prior OP

`kb/notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`

- A — OTHER/high: The target locates the note's artifact-quality triad inside a broader memory-system decomposition rather than causing or enabling it.
- B — EX/high: The target explains why discoverability, composability, and trust cover remembered material while memory remains a crosscutting system concern.
- C — OTHER/high: The target situates the source's remembered-material triad inside a broader storage, activation, and learning stack.

### F086 — OP (contested), prior OP

`kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:59 → kb/notes/definitions/constraining.md`

- A — EX/high: Constraining provides the general semantic mechanism by which a correction rules out future readings.
- B — OP/high: Constraining is the literal operation by which a rejected interpretation becomes a durable instruction test.
- C — OP/high: Constraining is the process through which a rejected interpretation becomes a durable narrowing of future behavior.

### F088 — OTHER (contested), prior OP

`kb/notes/reasoning-production-is-not-reasoning-evaluation.md:44 → kb/notes/process-structure-and-output-structure-are-independent-levers.md`

- A — OTHER/medium: The target offers an analogous distinction between process and result structure, but it does not cause the production-evaluation gap.
- B — OTHER/high: The target helps name a process-versus-result distinction but neither produces nor explains the evaluator's conclusion-agreement failure.
- C — EX/medium: The general independence principle explains why a correct destination cannot verify the submitted route.

### F092 — EN (contested), prior EN

`kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md`

- A — EN/high: Verification availability is the condition that permits automation of the re-derive-and-compare branch; otherwise the copy must be omitted.
- B — EN/high: Verification availability is the necessary condition separating enforceable checked copies from the omission-only case.
- C — EX/high: Verification cost explains the boundary between enforceable copies and judgment-heavy managed staleness.

### F102 — OTHER (contested), prior OP

`kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:59 → kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`

- A — EX/medium: The target supplies the general security account that the source refines into authorization bound to exact content and use.
- B — OTHER/high: The source develops one security boundary and borrows rollback vocabulary from the triad; the triad does not cause that boundary.
- C — OTHER/high: The target supplies the larger security and sovereignty framing that the source specializes into an authorization-to-force boundary.

### F104 — OP (contested), prior EX

`kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → kb/notes/ephemeral-computation-prevents-accumulation.md`

- A — OP/high: Ephemeral generate-execute-discard is the operational path that gives RLM simplicity while preventing cross-run accumulation.
- B — EX/high: The target explains how discarding generated orchestration removes lifecycle burden and simultaneously prevents cross-run learning.
- C — OP/high: Discarding task-local code is the literal process that separates RLM's nonaccumulating boundary from Tendril's persistence.

### F111 — OP (contested), prior OP

`kb/notes/reflective-coverage-is-graded-across-representational-forms.md:100 → kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md`

- A — OP/high: The target supplies a concrete interface-level transfer path across neural and symbolic implementations while leaving authority and lineage separate.
- B — OP/medium: The target is a concrete interface path across neural and symbolic implementations, while coverage, authority, and lineage remain separate obligations.
- C — OTHER/high: Unified calling is one cross-form mapping affordance, not an explanation or requirement for reflective coverage.

### F115 — UNSTABLE (unstable), prior OP

`kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md:46 → kb/notes/spec-mining-as-codification.md`

- A — OP/high: The ADR directly adopts spec mining's observe-stability-then-codify rule as the operational trigger for promoting a script.
- B — OTHER/high: Moving an existing symbolic script into a packaged command reuses spec mining's stability signal but is not itself behavior-to-spec codification.
- C — EX/medium: Spec mining explains why repeated unchanged core logic is evidence that an ad hoc script is ready for durable command promotion.

### F116 — OP (contested), prior X

`kb/notes/bounded-context-orchestration-model.md:90 → kb/notes/frontloading-spares-execution-context.md`

- A — OTHER/medium: Frontloading is a one-step instance subsumed by the iterative model, not a dependency or mechanism that produces the whole model.
- B — OP/high: Frontloading is the literal one-step scheduler action that removes already-solvable work before a bounded LLM call.
- C — OP/high: Frontloading is the one-step scheduling path that the orchestration loop generalizes.

### F119 — OP (contested), prior OP

`kb/notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → kb/notes/frontloading-spares-execution-context.md`

- A — OP/medium: The target supplies the precompute-and-insert operation that build-time configuration injection performs.
- B — EX/high: Frontloading explains why pre-resolving installation values saves live execution context.
- C — OP/high: Frontloading is the literal operational process used by build-time and session-start configuration injection.

## Classifier provenance

Requested model: no explicit override; each pass used a fresh default Codex collaboration subagent in an isolated context. Actual model information reported by each pass follows verbatim:

| batch | pass | reported model information |
|---:|---|---|
| 1 | A | Codex agent based on GPT-5. |
| 1 | B | Codex agent based on GPT-5. |
| 1 | C | Codex agent based on GPT-5. |
| 2 | A | Codex, an agent based on GPT-5; no more specific model identifier was exposed. |
| 2 | B | Codex agent based on GPT-5; exact model identifier is not exposed. |
| 2 | C | Codex, based on GPT-5. |
| 3 | A | Codex agent based on GPT-5; no more specific model identifier was exposed in this run. |
| 3 | B | Codex, based on GPT-5. |
| 3 | C | Codex, based on GPT-5; the exact model identifier was not exposed. |
| 4 | A | Codex agent based on GPT-5. |
| 4 | B | Codex agent based on GPT-5. |
| 4 | C | Codex agent based on GPT-5; exact deployed model identifier not exposed. |

No stronger provider, checkpoint, or parameter provenance was exposed, so none is claimed.

## Changed paths and verification

This run adds:

- `mechanism-full-reclassification-protocol.md`;
- `mechanism-full-reclassification-manifest.tsv`;
- `mechanism-full-reclassification-votes.tsv`;
- `mechanism-full-reclassification-results.md`.

It changes no corpus edge, collection contract, catalogue entry, ADR, durable instruction, or prior workshop result. The result, protocol, manifest, and vote ledger are checked for completeness and whitespace; the Markdown artifacts are validated with `commonplace-validate`.
