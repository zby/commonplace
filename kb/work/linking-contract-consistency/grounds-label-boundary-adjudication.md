# Grounds label boundary adjudication

**Status:** maintainer decision complete for the premise, evidence, extension/specialization, and mixed cohorts; 49 mechanism candidates remain deferred to the mechanism-label evaluation.

## Decision

Accept `premised-on` as the source-as-subject successor for the coherent premise relation:

> **theoretical assertion source `premised-on` premise target**

The reader follows the target to verify a premise on which the source's truth or applicability depends. The relation is asymmetric and has no registered inverse. Rejection of the target reopens the source assertion; this differs from `rests-on`, where rejection of the target triggers reconsideration of a design, rule, description, procedure, or system-definition artifact.

Reject `is-grounded-in` because it does not exclude evidence, mechanism, or design dependence; reject `follows-from` because it implies stronger entailment than the corpus warrants; reject generic `depends-on` because it erases the reader decision. Do not merge with `rests-on` and do not retire the premise relation.

The direction review's 160 P rows become `premised-on`. Exact adjudication below moves eight additional rows from its coarse X/D classes into the same relation, producing 168 accepted premise tuples. The 49 M rows are not assigned to the still-inconsistent `mechanism` identifier: their successor depends on a review of that label's full corpus.

## Reconciled disposition

| disposition | rows | status |
|---|---:|---|
| `premised-on` | 168 | accepted: 160 P rows plus 8 X/D corrections below |
| `extends` | 23 | accepted exact successor |
| `defined-in` | 13 | accepted exact successor |
| `exemplifies` | 12 | accepted exact successor |
| `is-evidence-for` | 9 | accepted exact successor: 2 notes→notes and 7 sources→notes |
| `evidenced-by` | 8 | accepted exact successor |
| remove | 1 | accepted: weak navigation edge does not earn a notes→notes `see-also` authorization |
| mechanism evaluation | 49 | deferred without successor |
| **active total** | **283** | reconciles to the direction review baseline |

One adjudicated row is removed. The 233 exact successor dispositions, 1 removal, and 49 deferred mechanism candidates are mutually exclusive.

## Exact evidence dispositions

Evidence direction follows the assertion, not the source collection. A target case bearing on the source becomes `evidenced-by`; a source case bearing on the target becomes `is-evidence-for`.

| source edge | target | successor |
|---|---|---|
| `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:73` | `notes/reflection-buys-addressability.md` | `evidenced-by` |
| `notes/epiplexity-by-example-what-entropy-and-complexity-miss.md:154` | `notes/information-value-is-observer-relative.md` | `is-evidence-for` |
| `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:70` | `notes/definitions/representational-form.md` | `evidenced-by` |
| `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:71` | `notes/definitions/reflective-system.md` | `evidenced-by` |
| `notes/reflective-coverage-is-graded-across-representational-forms.md:92` | `notes/an-action-model-matters-only-through-its-consumption-path.md` | `evidenced-by` |
| `sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md:52` | `notes/oracle-strength-spectrum.md` | `is-evidence-for` |
| `sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md:28` | `notes/human-writing-structures-transfer-to-llms-because-failure-modes.md` | `is-evidence-for` |
| `sources/meyerson-maker-million-step-llm-zero-errors.ingest.md:33` | `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | `is-evidence-for` |
| `sources/towards-a-science-of-ai-agent-reliability.ingest.md:30` | `notes/reliability-dimensions-map-to-oracle-hardening-stages.md` | `is-evidence-for` |
| `sources/towards-a-science-of-ai-agent-reliability.ingest.md:32` | `notes/oracle-strength-spectrum.md` | `is-evidence-for` |
| `sources/towards-a-science-of-ai-agent-reliability.ingest.md:34` | `notes/operational-signals-that-a-component-is-a-relaxing-candidate.md` | `is-evidence-for` |
| `sources/towards-a-science-of-ai-agent-reliability.ingest.md:42` | `notes/constraining-and-extraction-both-trade-generality-for-reliability.md` | `is-evidence-for` |

## Exact extension and specialization dispositions

The review's X class was intentionally coarse. `extends` means the source develops or specializes the target argument; `exemplifies` means the source is a worked instance of the target's more general shape. One X row is a premise dependency rather than either.

| source edge | target | successor |
|---|---|---|
| `notes/a-knowledge-base-should-support-fluid-resolution-switching.md:51` | `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | `extends` |
| `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:68` | `notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` | `extends` |
| `notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:62` | `notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md` | `exemplifies` |
| `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:67` | `notes/learning-theory-README.md` | `exemplifies` |
| `notes/an-accepted-edit-verifies-the-change-not-the-rule.md:32` | `notes/spec-mining-as-codification.md` | `extends` |
| `notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md:45` | `notes/deploy-time-learning-is-the-missing-middle.md` | `exemplifies` |
| `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:60` | `notes/llm-frameworks-should-keep-the-tool-loop-optional.md` | `exemplifies` |
| `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:61` | `notes/information-value-is-observer-relative.md` | `extends` |
| `notes/constraining-and-extraction-both-trade-generality-for-reliability.md:40` | `notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` | `extends` |
| `notes/false-positive-generation-is-filtered-before-retention.md:67` | `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` | `extends` |
| `notes/feasibility-is-the-heaviest-forks-net-load.md:33` | `notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md` | `extends` |
| `notes/feasibility-is-the-heaviest-forks-net-load.md:34` | `notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` | `extends` |
| `notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md:61` | `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` | `exemplifies` |
| `notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md:44` | `notes/reflective-coverage-is-graded-across-representational-forms.md` | `extends` |
| `notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md:50` | `notes/automated-synthesis-is-missing-good-oracles.md` | `exemplifies` |
| `notes/methodology-enforcement-is-constraining.md:57` | `notes/verifiability-gradient.md` | `exemplifies` |
| `notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md:37` | `notes/information-value-is-observer-relative.md` | `exemplifies` |
| `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:67` | `notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md` | `extends` |
| `notes/reflective-coverage-is-graded-across-representational-forms.md:91` | `notes/definitions/reflective-system.md` | `extends` |
| `notes/short-composable-notes-maximize-combinatorial-discovery.md:53` | `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | `premised-on` |
| `notes/skills-derive-from-methodology.md:75` | `notes/theory-and-methodology-form-a-two-layer-execution-system.md` | `exemplifies` |
| `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:105` | `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md` | `exemplifies` |
| `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:54` | `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md` | `extends` |

## Exact mixed-class dispositions

The review's D class combined distinct reader needs. The exact successors below prefer `defined-in` for terminology, `extends` for a developed argument, `exemplifies` for an instance, the evidence pair for worked cases, and `premised-on` for truth dependencies. The one weak navigation edge with no stronger assertion is removed rather than widening notes→notes `see-also`.

| source edge | target | successor |
|---|---|---|
| `notes/a-knowledge-base-should-support-fluid-resolution-switching.md:47` | `notes/link-following-and-search-impose-different-metadata-requirements.md` | `extends` |
| `notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md:66` | `notes/definitions/actionable-methodology.md` | `defined-in` |
| `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:92` | `notes/definitions/actionable-methodology.md` | `defined-in` |
| `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:97` | `notes/definitions/self-improving-system.md` | `exemplifies` |
| `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:100` | `notes/definitions/behavioral-authority.md` | `defined-in` |
| `notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:70` | `notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` | `extends` |
| `notes/an-action-model-matters-only-through-its-consumption-path.md:25` | `notes/definitions/behavioral-authority.md` | `defined-in` |
| `notes/an-action-model-matters-only-through-its-consumption-path.md:26` | `notes/definitions/representational-form.md` | `defined-in` |
| `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:43` | `notes/skills-derive-from-methodology.md` | `evidenced-by` |
| `notes/brainstorming-maintainability-oracles-for-agentic-development.md:189` | `notes/oracle-strength-spectrum.md` | `extends` |
| `notes/commitment-not-derivation-creates-new-ground-truth.md:87` | `notes/definitions/discovery-lifecycle.md` | `defined-in` |
| `notes/commitment-not-derivation-creates-new-ground-truth.md:89` | `notes/theory-and-methodology-form-a-two-layer-execution-system.md` | `extends` |
| `notes/commitment-not-derivation-creates-new-ground-truth.md:94` | `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` | `extends` |
| `notes/definitions/actionable-methodology.md:51` | `notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` | `is-evidence-for` |
| `notes/definitions/operative-change.md:35` | `notes/definitions/behavioral-authority.md` | `defined-in` |
| `notes/definitions/reach-assessment.md:59` | `notes/definitions/representational-form.md` | `defined-in` |
| `notes/linking-theory.md:88` | `notes/agents-navigate-by-deciding-what-to-read-next.md` | `premised-on` |
| `notes/linking-theory.md:89` | `notes/title-as-claim-enables-traversal-as-reasoning.md` | `premised-on` |
| `notes/linking-theory.md:90` | `notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md` | `premised-on` |
| `notes/linking-theory.md:91` | `notes/title-as-claim-makes-overlap-between-notes-visible.md` | `premised-on` |
| `notes/links-encode-conditional-possibilities-not-obligations.md:106` | `notes/linking-theory.md` | `exemplifies` |
| `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:29` | `notes/methodological-and-computational-closure-track-different-changes.md` | `extends` |
| `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:30` | `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` | remove |
| `notes/only-explicit-retention-is-durable-writable-and-addressable.md:47` | `notes/reflection-buys-addressability.md` | `extends` |
| `notes/only-explicit-retention-is-durable-writable-and-addressable.md:48` | `notes/reflective-coverage-is-graded-across-representational-forms.md` | `extends` |
| `notes/parametric-reproduction-cannot-replace-an-authoritative-record.md:40` | `notes/only-explicit-retention-is-durable-writable-and-addressable.md` | `extends` |
| `notes/pointer-design-tradeoffs-in-progressive-disclosure.md:77` | `notes/agents-navigate-by-deciding-what-to-read-next.md` | `premised-on` |
| `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:46` | `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` | `premised-on` |
| `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:51` | `notes/reflective-coverage-is-graded-across-representational-forms.md` | `extends` |
| `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:48` | `notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md` | `evidenced-by` |
| `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:50` | `notes/unified-calling-conventions-enable-bidirectional-refactoring.md` | `evidenced-by` |
| `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:48` | `notes/definitions/reach-assessment.md` | `defined-in` |
| `notes/self-improvement-is-relative-to-a-declared-objective.md:62` | `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md` | `evidenced-by` |
| `notes/stale-self-description-conceals-its-own-staleness.md:66` | `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` | `extends` |
| `notes/technical-constraints-make-kb-objective-choice-engineering.md:79` | `notes/definitions/system-definition-artifact.md` | `defined-in` |
| `notes/technical-constraints-make-kb-objective-choice-engineering.md:80` | `notes/definitions/representational-form.md` | `defined-in` |
| `notes/the-self-improving-system-definition-classifies-its-boundary-cases.md:48` | `notes/definitions/self-improving-system.md` | `defined-in` |
| `notes/title-as-claim-enables-traversal-as-reasoning.md:73` | `notes/agents-navigate-by-deciding-what-to-read-next.md` | `premised-on` |
| `notes/world-models-assess-explanatory-reach-through-action-conditioned.md:27` | `notes/definitions/representational-form.md` | `defined-in` |

## Authorization consequences

A later migration replaces `grounds` with `premised-on` for notes→notes and uses already-authorized `extends`, `exemplifies`, `defined-in`, and `evidenced-by` pairings. It must additionally decide one demonstrated authorization delta rather than forcing those rows into a weaker existing label:

- authorize `is-evidence-for` for notes→notes (2 rows); sources→notes is already authorized.

The weak notes→notes `see-also` candidate is removed. Do not add that pairing to the notes contract.

The 49 mechanism candidates create no authorization decision yet. Do not retain `grounds` as a synonym after their successor is adjudicated, and do not migrate them to `mechanism` merely because that is their semantic review bucket.

## Migration readiness

`premised-on` and the 74 non-mechanism boundary rows are adjudicated. A complete `grounds` migration plan remains blocked on one semantic input: exact dispositions for the 49 M rows after the active `mechanism` corpus is reviewed. Rebaseline all cohorts before implementation; the counts above describe this adjudication baseline, not a future execution lock.
