# Grounds label direction review

**Status:** complete semantic evaluation; no corpus edge, collection contract, catalogue entry, ADR, or durable instruction was changed.

**Date:** 2026-07-28  
**Executing model:** current Codex runtime (GPT-5 family as exposed to this session). No Luna dispatch or runtime verification was available, so this review makes no Luna provenance claim.

## Recommendation

Adopt **`premised-on`** for the coherent theoretical premise relation, with the assertion:

> **theoretical assertion source `premised-on` premise target**

Its reader need is: *follow the target to verify the premise on which the source's truth or applicability depends*. The relation is asymmetric and source-as-subject. Do not create or require a formal inverse. A return edge is authored only when the target has its own reader need; the three reciprocal pairs in the current corpus do not establish an inverse-authoring obligation.

This is outcome 1 from the workshop brief, with mandatory semantic reclassification of non-premise rows before any later migration. It is not a bulk rename. Of 276 canonical note→note rows, 160 are premise dependencies; the other 116 should move to existing relations or be separately adjudicated. The seven newly live sources→notes rows are evidence mappings, not premise dependencies, and should be treated under `is-evidence-for` in a later cleanup.

The strongest rejected alternative is **`is-grounded-in`**. It is grammatical, but its ordinary reading covers evidence, mechanism, and design dependence as easily as premises; it would make the boundary with `rests-on` and `evidenced-by` harder to recover. `follows-from` overstates entailment, and `depends-on` is too broad. Merging with `rests-on` would erase a repeated maintenance decision: rejecting a premise calls for reassessing a theoretical assertion, while rejecting a `rests-on` target calls for reconsidering a design, rule, description, procedure, or system-definition artifact.

## Governing test and method

The evaluation applied the source-as-subject invariant from [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md), the `rests-on` boundary and deferred-cohort decision from [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-are-reclassified.md), and the prior [directional-label grammar](./directional-label-grammar.md), [rationale direction review](./rationale-label-direction-review.md), [boundary adjudication](./rationale-grounds-boundary-adjudication.md), and [migration retrospective](./rationale-label-migration-retrospective.md). I also read the current [link vocabulary](../../reference/link-vocabulary.md), [notes collection contract](../../notes/COLLECTION.md), the active source contract, and the [directional-label migration procedure](../../instructions/migrate-directional-link-label.md).

The positive mutable surface was rebaselined as active registered footer links in:

- `kb/notes/`;
- `kb/reference/`, excluding `proposals/archive/`;
- `kb/instructions/`;
- `kb/agent-memory-systems/`;
- `kb/agentic-systems/`;
- active source analyses and ingests in `kb/sources/`;
- `kb/types/`.

A one-shot scanner resolved every relative target before assigning its destination. It accepted ordinary and bold footer forms, required exactly one Markdown link before a `— grounds:` or `-- grounds:` marker, and reported no unsupported active syntax. It did not persist a parser or mutate the repository. Local context was read for every row; full source and target documents were opened for boundary cases including the worked-instance, evidence, comparison, and source-ingest rows cited below.

## Inventory and exclusions

| bucket | rows | treatment |
|---|---:|---|
| active mutable | 283 | semantic disposition ledger below |
| generated reports | 1,637 | excluded; generated review/prompt material |
| workshop history | 178 | excluded; historical working material under `kb/work/` |
| archived proposals | 1 | excluded; `kb/reference/proposals/archive/` |
| **all registered footer rows** | **2,099** | reconciles exactly |

No immutable source snapshot contributed a registered footer row in this scan. Ordinary prose, quoted migration text, and unregistered examples were not counted. The live count is therefore 283, not the 276 canonical baseline preserved by ADR 060: seven source-side rows have appeared since that migration's final reconciliation and must be handled as live drift.

### Active source→destination reconciliation

| source collection | destination | rows | source files | semantic treatment |
|---|---|---:|---:|---|
| notes | notes | 276 | 135 | canonical cohort; classify below |
| sources | notes | 7 | 4 | evidence-like off-pattern drift; later `is-evidence-for` cleanup |
| **total** |  | **283** | **139** |  |

The canonical cohort has 276 unique tuples from 135 source files to 119 target files. There are no duplicate tuples. Three unordered pairs author both directions (six directed edges); all other edges are one-way. The most-targeted premises are `context-efficiency...` (14), `warranted-autonomy...` (10), `the-boundary-of-automation...` (9), `first-principles-reasoning...` (9), and `oracle-strength-spectrum` (9). This concentration shows repeated premise verification, not a general-purpose citation convention.

## Semantic dispositions

The dispositions are mutually exclusive and classify the assertion actually made at the edge, not the authorization status.

| code | disposition | canonical rows | live rows including source drift | test |
|---|---|---:|---:|---|
| P | premise dependency | 160 | 160 | rejecting the target calls for reassessing the source assertion's truth or applicability |
| M | mechanism or explanation | 49 | 49 | target explains how the source claim operates; use `mechanism` where authorized |
| X | extension or specialization | 23 | 23 | source applies, specializes, instantiates, or develops target; use `extends`, `exemplifies`, or another precise relation |
| D | definition, lineage, comparison, or navigation | 39 | 39 | target supplies terminology, provenance, comparison, or orientation; use the matching existing relation |
| E | evidence | 5 | 12 | target is an observation/case supporting the source, or source observation bears on the target; use the evidence pair |
| R | `rests-on` dependency | 0 | 0 | no canonical note source is a design/rule/description/procedure/system-definition dependency |
| U | unresolved ambiguity | 0 | 0 | every row received a best supported disposition; boundary uncertainty is recorded below |
| **total** |  | **276** | **283** |  |

The 160 P rows are the coherent cohort. They repeatedly answer: “what premise should I inspect before trusting or applying this assertion?” They do not say that the target explains a mechanism, corroborates the assertion, or is a design dependency. The 116 non-P canonical rows are why a rename-only migration is unsafe.

### Category boundary

- **P vs `rests-on`:** P sources are theoretical assertions. If the target is rejected, the source's truth or applicability must be reassessed. `rests-on` is for a design, rule, description, procedure, or system-definition artifact whose construction or operation must be reconsidered.
- **P vs `evidenced-by` / `is-evidence-for`:** evidence changes the support record or landing map; it does not make the target a premise whose rejection directly reopens the source's claim. The source-side seven rows are clear `is-evidence-for` cases.
- **P vs `mechanism`:** a mechanism answers “how does this claim operate?” A premise answers “what must I verify before relying on this claim?” Several context phrases say “why,” so the target text—not that word alone—decides.
- **P vs `extends` / `exemplifies`:** an extension or specialization follows the target to see a developed or instantiated argument. It is not a premise check merely because the target is more general.
- **P vs definition, lineage, comparison, or navigation:** those edges solve terminology, maintenance/provenance, peer-comparison, or orientation needs. They do not warrant a premise successor.

## Candidate outcomes

### 1. Adopt `premised-on` — recommended

**For:** 160 repeated premise decisions, a direct source-subject grammar, and a reader need that remains stable across theoretical notes and definitions used as premises. `premised-on` avoids claiming deductive entailment while making the premise-checking journey explicit.

**Against:** the phrase is slightly less familiar than “grounded in,” and some P/M cases require semantic judgment. That is a migration-classifier issue, not evidence that the identifier is unstable.

**Adopted shape:**

- assertion: `theoretical assertion source premised-on premise target`;
- reader need: verify the target premise before relying on the source;
- direction kind: asymmetric, source-as-subject;
- inverse: none; reciprocal authoring remains independently need-driven.

### 2. Merge into `rests-on` — rejected

**For:** one source-subject grammar and fewer theoretical-shaped identifiers.

**Against:** the corpus preserves two different decisions. A P reader tests whether a theoretical assertion still holds or applies; a `rests-on` reader inspects the theory whose change would trigger redesign or rule reconsideration. The current `rests-on` contract explicitly excludes generic dependency and evidence. Merging would turn 160 premise checks into false design-dependency signals and would lose the reason a theoretical note points to another theoretical note.

### 3. Split/reclassify the cohort — required as a migration operation, not the primary naming outcome

**For:** 116 canonical rows already behave as mechanism, extension/specialization, definition/lineage/comparison/navigation, or evidence. Existing labels can express most of them more precisely, reducing vocabulary growth.

**Against:** reclassification alone leaves the 160-row premise cohort with the old source-reversing identifier. It is therefore necessary but not sufficient. The recommendation is “adopt `premised-on` for P, reclassify the rest,” rather than inventing a label for every current use.

### 4. Retire the formal relation in favor of connective prose — rejected

**For:** direct prose can explain a single local reason, and the theoretical vocabulary remains smaller.

**Against:** 160 edges recur across 135 source files and 119 targets, with concentrated high-value premises and three independently authored reciprocal pairs. A formal label gives connect/validation/maintenance a stable reader need; prose alone would make premise verification non-queryable and would conceal the distinction from mechanism and evidence. Use prose for weak or one-off cases after reclassification, not for this repeated cohort.

## Ledger

Each line below is one active tuple. Paths are `kb/`-relative; the line number identifies the authored footer and the target path is the resolved target identity. `P`, `M`, `X`, `D`, and `E` use the dispositions above. The seven source rows are included at the end and are not part of the canonical note→note cohort.

### P — premise dependency (160)

- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:73 → notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md`
- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:74 → notes/commitment-not-derivation-creates-new-ground-truth.md`
- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:75 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:72 → notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`
- `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:67 → notes/self-improvement-is-relative-to-a-declared-objective.md`
- `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:71 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:76 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md:58 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:56 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/access-burden-and-transformation-burden-are-independent-query.md:52 → notes/bounded-context-orchestration-model.md`
- `notes/access-burden-and-transformation-burden-are-independent-query.md:53 → notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`
- `notes/accumulation-counts-dependence-through-the-retained-result.md:56 → notes/self-improvement-is-relative-to-a-declared-objective.md`
- `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:29 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md:63 → notes/information-value-is-observer-relative.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:63 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:64 → notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:69 → notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:71 → notes/automating-kb-learning-is-an-open-problem.md`
- `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:37 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:39 → notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `notes/agent-orchestration-needs-coordination-guarantees-not-just.md:64 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md:111 → notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`
- `notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md:112 → notes/files-not-database.md`
- `notes/an-accepted-edit-verifies-the-change-not-the-rule.md:33 → notes/oracle-strength-spectrum.md`
- `notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:48 → notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
- `notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:50 → notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`
- `notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:51 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:53 → notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md`
- `notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md:57 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`
- `notes/bounded-context-orchestration-model.md:88 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md:31 → notes/oracle-strength-spectrum.md`
- `notes/codify-versus-llm-decision-heuristics.md:118 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:88 → notes/agentic-systems-interpret-underspecified-instructions.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:91 → notes/storing-llm-outputs-is-constraining.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:96 → notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`
- `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:59 → notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md`
- `notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:33 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md:28 → notes/history-has-one-chance-to-become-checkable.md`
- `notes/definitions/context-engineering.md:61 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/definitions/reach-assessment.md:65 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/definitions/reflective-system.md:75 → notes/definitions/actionable-methodology.md`
- `notes/definitions/self-improving-system.md:65 → notes/definitions/reflective-system.md`
- `notes/design-for-the-first-time-human-except-on-access-cost.md:24 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/design-for-the-first-time-human-except-on-access-cost.md:29 → notes/llm-context-is-a-homoiconic-medium.md`
- `notes/design-for-the-first-time-human-except-on-access-cost.md:30 → notes/agentic-systems-interpret-underspecified-instructions.md`
- `notes/directory-placement-is-total-frontmatter-classification-is-partial.md:52 → notes/why-notes-have-types.md`
- `notes/directory-placement-is-total-frontmatter-classification-is-partial.md:54 → notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md`
- `notes/evolving-understanding-needs-holistic-rewrite-not-composition.md:60 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/feasibility-is-the-heaviest-forks-net-load.md:35 → notes/llm-context-is-composed-without-scoping.md`
- `notes/first-principles-are-inherited-constraints-not-design-choices.md:57 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/first-principles-are-inherited-constraints-not-design-choices.md:58 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/first-principles-are-inherited-constraints-not-design-choices.md:59 → notes/short-composable-notes-maximize-combinatorial-discovery.md`
- `notes/first-principles-are-inherited-constraints-not-design-choices.md:60 → notes/directory-placement-is-total-frontmatter-classification-is-partial.md`
- `notes/first-principles-are-inherited-constraints-not-design-choices.md:61 → notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
- `notes/first-principles-reasoning-selects-for-explanatory-reach-over.md:51 → notes/programming-patterns-get-a-fast-pass-but-other-borrowed-ideas-must.md`
- `notes/first-principles-reasoning-selects-for-explanatory-reach-over.md:52 → notes/learning-is-not-only-about-generality.md`
- `notes/fix-what-the-executor-cant-determine-not-what-it-will.md:26 → notes/design-for-the-first-time-human-except-on-access-cost.md`
- `notes/fix-what-the-executor-cant-determine-not-what-it-will.md:29 → notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md`
- `notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md:53 → notes/commitment-not-derivation-creates-new-ground-truth.md`
- `notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:50 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md:57 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md:67 → notes/false-positive-generation-is-filtered-before-retention.md`
- `notes/increasing-computational-autonomy-relocates-human-effort.md:54 → notes/methodological-and-computational-closure-track-different-changes.md`
- `notes/increasing-computational-autonomy-relocates-human-effort.md:55 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md:61 → notes/instruction-specificity-should-match-loading-frequency.md`
- `notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md:63 → notes/raw-accumulation-does-not-create-usable-memory.md`
- `notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md:51 → notes/oracle-strength-spectrum.md`
- `notes/learning-is-not-only-about-generality.md:57 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/llm-context-is-composed-without-scoping.md:69 → notes/agentic-systems-interpret-underspecified-instructions.md`
- `notes/llm-generation-confidence-tracks-typicality-not-soundness.md:34 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md:42 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:31 → notes/definitions/self-improving-system.md`
- `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:33 → notes/false-positive-generation-is-filtered-before-retention.md`
- `notes/methodological-and-computational-closure-track-different-changes.md:79 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/methodological-and-computational-closure-track-different-changes.md:81 → notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md`
- `notes/methodological-and-computational-closure-track-different-changes.md:82 → notes/definitions/reflective-system.md`
- `notes/methodological-and-computational-closure-track-different-changes.md:84 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/methodological-and-computational-closure-track-different-changes.md:85 → notes/only-explicit-retention-is-durable-writable-and-addressable.md`
- `notes/pointer-design-tradeoffs-in-progressive-disclosure.md:78 → notes/agent-statelessness-makes-routing-architectural-not-learned.md`
- `notes/pointer-design-tradeoffs-in-progressive-disclosure.md:79 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/prompt-ablation-converts-human-insight-to-deployable-framing.md:63 → notes/oracle-strength-spectrum.md`
- `notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md:38 → notes/definitions/representational-form.md`
- `notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md:39 → notes/agentic-systems-interpret-underspecified-instructions.md`
- `notes/raw-accumulation-does-not-create-usable-memory.md:28 → notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`
- `notes/raw-accumulation-does-not-create-usable-memory.md:29 → notes/learning-is-not-only-about-generality.md`
- `notes/raw-accumulation-does-not-create-usable-memory.md:30 → notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:49 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md:54 → notes/self-improvement-is-relative-to-a-declared-objective.md`
- `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md:55 → notes/accumulation-counts-dependence-through-the-retained-result.md`
- `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md:56 → notes/reflection-buys-addressability.md`
- `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md:57 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/reflection-buys-addressability.md:68 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:45 → notes/only-explicit-retention-is-durable-writable-and-addressable.md`
- `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:48 → notes/session-history-should-not-be-the-default-next-context.md`
- `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:50 → notes/frontloading-spares-execution-context.md`
- `notes/retrieval-failure-is-reflection-failure.md:37 → notes/definitions/reflective-system.md`
- `notes/revising-an-improvement-objective-is-licensed-from-outside-it.md:58 → notes/self-improvement-is-relative-to-a-declared-objective.md`
- `notes/revising-an-improvement-objective-is-licensed-from-outside-it.md:60 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/revising-an-improvement-objective-is-licensed-from-outside-it.md:63 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/revising-an-improvement-objective-is-licensed-from-outside-it.md:64 → notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md`
- `notes/runtime-structure-determines-governance-control-surfaces.md:53 → notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`
- `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:45 → notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md`
- `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:47 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:50 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/self-improvement-is-relative-to-a-declared-objective.md:60 → notes/the-self-improving-system-definition-classifies-its-boundary-cases.md`
- `notes/self-improvement-is-relative-to-a-declared-objective.md:61 → notes/methodological-and-computational-closure-track-different-changes.md`
- `notes/self-improvement-is-relative-to-a-declared-objective.md:63 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/semantic-review-catches-content-errors-that-structural-validation.md:50 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `notes/session-history-should-not-be-the-default-next-context.md:78 → notes/the-chat-history-model-trades-context-efficiency-for-implementation.md`
- `notes/short-composable-notes-maximize-combinatorial-discovery.md:52 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/skills-are-instructions-plus-routing-and-execution-policy.md:94 → notes/instruction-specificity-should-match-loading-frequency.md`
- `notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md:106 → notes/information-value-is-observer-relative.md`
- `notes/specification-level-separation-recovers-scoping-before-it-recovers.md:33 → notes/llm-context-is-composed-without-scoping.md`
- `notes/specification-level-separation-recovers-scoping-before-it-recovers.md:36 → notes/oracle-strength-spectrum.md`
- `notes/specification-strategy-should-follow-where-understanding-lives.md:75 → notes/changing-requirements-conflate-genuine-change-with-disambiguation.md`
- `notes/stale-self-description-conceals-its-own-staleness.md:65 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `notes/stale-self-description-conceals-its-own-staleness.md:68 → notes/definitions/reflective-system.md`
- `notes/structure-inference-needs-capture-at-the-decision-surface.md:38 → notes/raw-accumulation-does-not-create-usable-memory.md`
- `notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md:38 → notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `notes/synthesis-is-not-error-correction.md:66 → notes/oracle-strength-spectrum.md`
- `notes/task-fitted-structure-costs-cross-task-reuse.md:67 → notes/first-principles-are-inherited-constraints-not-design-choices.md`
- `notes/task-fitted-structure-costs-cross-task-reuse.md:70 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:73 → notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:75 → notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:76 → notes/first-principles-are-inherited-constraints-not-design-choices.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:77 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:82 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:83 → notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md`
- `notes/the-chat-history-model-trades-context-efficiency-for-implementation.md:33 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:47 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/the-framework-is-often-larger-than-the-durable-contribution.md:60 → notes/information-value-is-observer-relative.md`
- `notes/the-framework-is-often-larger-than-the-durable-contribution.md:61 → notes/knowledge-storage-does-not-imply-contextual-activation.md`
- `notes/the-framework-is-often-larger-than-the-durable-contribution.md:64 → notes/short-composable-notes-maximize-combinatorial-discovery.md`
- `notes/the-practical-scheduler-is-the-host-language.md:64 → notes/bounded-context-orchestration-model.md`
- `notes/the-practical-scheduler-is-the-host-language.md:67 → notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md`
- `notes/the-self-improving-system-definition-classifies-its-boundary-cases.md:49 → notes/definitions/behavior-determining-organization.md`
- `notes/the-self-improving-system-definition-classifies-its-boundary-cases.md:50 → notes/definitions/operative-change.md`
- `notes/the-self-improving-system-definition-classifies-its-boundary-cases.md:51 → notes/definitions/evidence-bearing-on-an-improvement-objective.md`
- `notes/theory-and-methodology-form-a-two-layer-execution-system.md:69 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`
- `notes/theory-and-methodology-form-a-two-layer-execution-system.md:70 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/theory-and-methodology-form-a-two-layer-execution-system.md:71 → notes/learning-is-not-only-about-generality.md`
- `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:104 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:106 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:107 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:58 → notes/reflection-buys-addressability.md`
- `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:62 → notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md`
- `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:64 → notes/methodological-and-computational-closure-track-different-changes.md`
- `notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md:23 → notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md`
- `notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md:61 → notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md`
- `notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md:62 → notes/automating-kb-learning-is-an-open-problem.md`
- `notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md:65 → notes/oracle-strength-spectrum.md`
- `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md:59 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md:60 → notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`
- `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md:62 → notes/decomposition-heuristics-for-bounded-context-scheduling.md`
- `notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:56 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md:97 → notes/enforcement-without-structured-recovery-is-incomplete.md`
- `notes/warranted-autonomy-is-bounded-by-oracle-domain.md:43 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/warranted-autonomy-is-bounded-by-oracle-domain.md:44 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/weakly-discriminated-qualities-tend-to-be-underselected.md:78 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/weakly-discriminated-qualities-tend-to-be-underselected.md:79 → notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`

### M — mechanism or explanation (49)

- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:76 → notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:77 → notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`
- `notes/a-consumption-channel-delivers-force-without-the-history-that.md:78 → notes/definitions/reflective-system.md`
- `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:63 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:70 → notes/text-testing-framework.md`
- `notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`
- `notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:64 → notes/llm-context-is-composed-without-scoping.md`
- `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:28 → notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`
- `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:30 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:66 → notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`
- `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:36 → notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`
- `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → notes/frontloading-spares-execution-context.md`
- `notes/an-action-model-matters-only-through-its-consumption-path.md:24 → notes/axes-of-artifact-analysis.md`
- `notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:49 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:39 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`
- `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → notes/frontloading-spares-execution-context.md`
- `notes/automated-synthesis-is-missing-good-oracles.md:58 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/brainstorming-maintainability-oracles-for-agentic-development.md:188 → notes/weakly-discriminated-qualities-tend-to-be-underselected.md`
- `notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md:55 → notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md`
- `notes/codify-versus-llm-decision-heuristics.md:120 → notes/ephemeral-computation-prevents-accumulation.md`
- `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → notes/bounded-context-orchestration-model.md`
- `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:61 → notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:62 → notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md`
- `notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → notes/agent-orchestration-needs-coordination-guarantees-not-just.md`
- `notes/definitions/reach-assessment.md:66 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:64 → notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`
- `notes/evaluation-automation-is-phase-gated-by-comprehension.md:50 → notes/spec-mining-as-codification.md`
- `notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md:72 → notes/oracle-strength-spectrum.md`
- `notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:47 → notes/definitions/representational-form.md`
- `notes/frontloading-spares-execution-context.md:53 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/increasing-computational-autonomy-relocates-human-effort.md:59 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `notes/llm-context-is-a-homoiconic-medium.md:45 → notes/methodology-enforcement-is-constraining.md`
- `notes/llm-context-is-composed-without-scoping.md:72 → notes/instruction-specificity-should-match-loading-frequency.md`
- `notes/llm-context-is-composed-without-scoping.md:78 → notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`
- `notes/llm-executed-methodologies-are-metacircular-interpreters.md:38 → notes/definitions/system-definition-artifact.md`
- `notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:56 → notes/llm-context-is-composed-without-scoping.md`
- `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:46 → notes/bounded-context-orchestration-model.md`
- `notes/reasoning-production-is-not-reasoning-evaluation.md:43 → notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`
- `notes/reasoning-production-is-not-reasoning-evaluation.md:44 → notes/process-structure-and-output-structure-are-independent-levers.md`
- `notes/reflection-makes-retained-lessons-second-order.md:49 → notes/reflection-buys-addressability.md`
- `notes/reverse-compression-is-when-llm-output-expands-without-adding.md:43 → notes/information-value-is-observer-relative.md`
- `notes/runtime-structure-determines-governance-control-surfaces.md:56 → notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`
- `notes/scenario-decomposition-drives-architecture.md:86 → notes/skills-derive-from-methodology.md`
- `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:49 → notes/reasoning-production-is-not-reasoning-evaluation.md`
- `notes/semantic-review-catches-content-errors-that-structural-validation.md:49 → notes/text-testing-framework.md`
- `notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md:73 → notes/synthesis-is-not-error-correction.md`

### X — extension or specialization (23)

- `notes/a-knowledge-base-should-support-fluid-resolution-switching.md:51 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:68 → notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md`
- `notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:62 → notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md`
- `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:67 → notes/learning-theory-README.md`
- `notes/an-accepted-edit-verifies-the-change-not-the-rule.md:32 → notes/spec-mining-as-codification.md`
- `notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md:45 → notes/deploy-time-learning-is-the-missing-middle.md`
- `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:60 → notes/llm-frameworks-should-keep-the-tool-loop-optional.md`
- `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:61 → notes/information-value-is-observer-relative.md`
- `notes/constraining-and-extraction-both-trade-generality-for-reliability.md:40 → notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md`
- `notes/false-positive-generation-is-filtered-before-retention.md:67 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/feasibility-is-the-heaviest-forks-net-load.md:33 → notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`
- `notes/feasibility-is-the-heaviest-forks-net-load.md:34 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md:61 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md:44 → notes/reflective-coverage-is-graded-across-representational-forms.md`
- `notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md:50 → notes/automated-synthesis-is-missing-good-oracles.md`
- `notes/methodology-enforcement-is-constraining.md:57 → notes/verifiability-gradient.md`
- `notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md:37 → notes/information-value-is-observer-relative.md`
- `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:67 → notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md`
- `notes/reflective-coverage-is-graded-across-representational-forms.md:91 → notes/definitions/reflective-system.md`
- `notes/short-composable-notes-maximize-combinatorial-discovery.md:53 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `notes/skills-derive-from-methodology.md:75 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:105 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:54 → notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md`

### D — definition, lineage, comparison, or navigation (39)

- `notes/a-knowledge-base-should-support-fluid-resolution-switching.md:47 → notes/link-following-and-search-impose-different-metadata-requirements.md`
- `notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md:66 → notes/definitions/actionable-methodology.md`
- `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:92 → notes/definitions/actionable-methodology.md`
- `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:97 → notes/definitions/self-improving-system.md`
- `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:100 → notes/definitions/behavioral-authority.md`
- `notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md:70 → notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md`
- `notes/an-action-model-matters-only-through-its-consumption-path.md:25 → notes/definitions/behavioral-authority.md`
- `notes/an-action-model-matters-only-through-its-consumption-path.md:26 → notes/definitions/representational-form.md`
- `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:43 → notes/skills-derive-from-methodology.md`
- `notes/brainstorming-maintainability-oracles-for-agentic-development.md:189 → notes/oracle-strength-spectrum.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:87 → notes/definitions/discovery-lifecycle.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:89 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `notes/commitment-not-derivation-creates-new-ground-truth.md:94 → notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`
- `notes/definitions/actionable-methodology.md:51 → notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md`
- `notes/definitions/operative-change.md:35 → notes/definitions/behavioral-authority.md`
- `notes/definitions/reach-assessment.md:59 → notes/definitions/representational-form.md`
- `notes/linking-theory.md:88 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `notes/linking-theory.md:89 → notes/title-as-claim-enables-traversal-as-reasoning.md`
- `notes/linking-theory.md:90 → notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md`
- `notes/linking-theory.md:91 → notes/title-as-claim-makes-overlap-between-notes-visible.md`
- `notes/links-encode-conditional-possibilities-not-obligations.md:106 → notes/linking-theory.md`
- `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:29 → notes/methodological-and-computational-closure-track-different-changes.md`
- `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md:30 → notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`
- `notes/only-explicit-retention-is-durable-writable-and-addressable.md:47 → notes/reflection-buys-addressability.md`
- `notes/only-explicit-retention-is-durable-writable-and-addressable.md:48 → notes/reflective-coverage-is-graded-across-representational-forms.md`
- `notes/parametric-reproduction-cannot-replace-an-authoritative-record.md:40 → notes/only-explicit-retention-is-durable-writable-and-addressable.md`
- `notes/pointer-design-tradeoffs-in-progressive-disclosure.md:77 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:46 → notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`
- `notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md:51 → notes/reflective-coverage-is-graded-across-representational-forms.md`
- `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:48 → notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:50 → notes/unified-calling-conventions-enable-bidirectional-refactoring.md`
- `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:48 → notes/definitions/reach-assessment.md`
- `notes/self-improvement-is-relative-to-a-declared-objective.md:62 → notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md`
- `notes/stale-self-description-conceals-its-own-staleness.md:66 → notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:79 → notes/definitions/system-definition-artifact.md`
- `notes/technical-constraints-make-kb-objective-choice-engineering.md:80 → notes/definitions/representational-form.md`
- `notes/the-self-improving-system-definition-classifies-its-boundary-cases.md:48 → notes/definitions/self-improving-system.md`
- `notes/title-as-claim-enables-traversal-as-reasoning.md:73 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `notes/world-models-assess-explanatory-reach-through-action-conditioned.md:27 → notes/definitions/representational-form.md`

### E — evidence (12)

- `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:73 → notes/reflection-buys-addressability.md`
- `notes/epiplexity-by-example-what-entropy-and-complexity-miss.md:154 → notes/information-value-is-observer-relative.md`
- `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:70 → notes/definitions/representational-form.md`
- `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:71 → notes/definitions/reflective-system.md`
- `notes/reflective-coverage-is-graded-across-representational-forms.md:92 → notes/an-action-model-matters-only-through-its-consumption-path.md`
- `sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md:52 → notes/oracle-strength-spectrum.md`
- `sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md:28 → notes/human-writing-structures-transfer-to-llms-because-failure-modes.md`
- `sources/meyerson-maker-million-step-llm-zero-errors.ingest.md:33 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `sources/towards-a-science-of-ai-agent-reliability.ingest.md:30 → notes/reliability-dimensions-map-to-oracle-hardening-stages.md`
- `sources/towards-a-science-of-ai-agent-reliability.ingest.md:32 → notes/oracle-strength-spectrum.md`
- `sources/towards-a-science-of-ai-agent-reliability.ingest.md:34 → notes/operational-signals-that-a-component-is-a-relaxing-candidate.md`
- `sources/towards-a-science-of-ai-agent-reliability.ingest.md:42 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`

## Boundary cases and minimal quotations

These were the cases most likely to be mistaken for premise dependencies; the full source and target were read before disposition.

- `kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:73` → `reflection-buys-addressability.md` is **E**, not P: “the worked instance — addressability is pursued for expected advantages.” The target is an example bearing on the source's linking-claim analysis, not a premise the source asks the reader to verify.
- `kb/notes/epiplexity-by-example-what-entropy-and-complexity-miss.md:154` → `information-value-is-observer-relative.md` is **E**: “concrete examples for that formalization.” The examples corroborate/formalize the target relation; they do not operate as the source's premise.
- `kb/notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md:70-71` → `representational-form.md` and `reflective-system.md` are **E**: both are explicitly “worked instance[s]” of the warrant the source discusses.
- `kb/notes/reflective-coverage-is-graded-across-representational-forms.md:92` → `an-action-model-matters-only-through-its-consumption-path.md` is **E**: “the model-mediated action case” is a case bearing on the open coverage question.
- `kb/notes/false-positive-generation-is-filtered-before-retention.md:67` → `a-proposal-selection-loop...md` is **X**, because the local phrase says “the point it extends”; the source develops a target framework rather than merely checking its premise.
- `kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md:61` → `a-proposal-selection-loop...md` is **X**: the architecture is mapped onto the target decomposition, an instance/specialization journey.
- `kb/notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:48,50` → the two targets are **D** comparison cases: “supplies the ... side of the comparison,” not premises or mechanisms of the source's claim.
- `kb/notes/linking-theory.md:88-91` → navigation/maintenance targets are **D** despite carrying explanatory importance; their reader need is orientation and claim-surface inspection.
- `kb/sources/towards-a-science-of-ai-agent-reliability.ingest.md:30-42` → four source-side rows are **E**: “this source provides,” “direct empirical support,” “confirmed at scale,” and “operationalise[s]” all describe evidence landing on notes. They should not be treated as canonical note premises.

No row required `U` after these checks. “Why” in a context phrase was not sufficient to classify an edge as M: the deciding question was whether the target supplies a causal account or a premise to verify.

## Reciprocal and incoming pattern review

Only three unordered pairs author both directions under `grounds`:

- `agent-memory-is-a-crosscutting-concern...` ↔ `agent-memory-needs-discoverable...`;
- `first-principles-reasoning...` ↔ `learning-is-not-only-about-generality`;
- `real-self-improving-systems...` ↔ `self-improvement-is-relative...`.

That is six directed edges out of 276. The pattern shows that authors sometimes have independent reasons to land in both artifacts; it does not support an inverse relation or reciprocal-authoring rule. The proposed `premised-on` relation therefore has no formal inverse.

## Authorization and later-migration consequences

This review changes no authorization surface. Today `kb/notes/COLLECTION.md` authorizes `grounds` for notes→notes but does not authorize `premised-on`; a later migration would need to replace the old authorization with `premised-on` for the P cohort, update the shared catalogue and authoring guidance, and reconcile every changed collection contract together. It should not retain `grounds` as a synonym for the same pairing.

The 49 M rows should be assessed for `mechanism`; the 23 X rows for `extends`, `exemplifies`, or a narrower relation; and the 39 D rows for `defined-in`, lineage labels, `compares-with`/`contrasts`, or `see-also`. The five canonical E rows and seven source-side rows should be assessed under `evidenced-by` or `is-evidence-for` according to source direction. Any `rests-on` candidate would need a source artifact whose rejection triggers design/rule/description reconsideration; none was found in the canonical cohort.

A later migration must use a fresh positive-surface inventory, exact source→target tuple conservation, and an independent post-write reconciliation as required by the migration procedure. This review does not plan or authorize those edits.

## Surprises and procedure improvements

- **Baseline drift:** ADR 060's final 276-row canonical count is no longer the full active old-label surface; seven source-side rows appeared afterward. Rebaseline immediately before mutation, even when a previous migration recorded a final count.
- **Off-pattern drift returned quickly:** the seven rows are source-ingest evidence mappings and the source contract already has `is-evidence-for`; a later migration should scan for new old-label uses after every contract change.
- **The canonical cohort is semantically mixed:** 116/276 rows (42.0%) do not express premise verification. A migration plan that treats the canonical destination pair as semantic proof would repeat the rationale-run boundary error.
- **Reciprocity is rare:** six directed reciprocal edges are insufficient evidence for an inverse identifier. Keep inverse decisions separate from incoming-link density.
- **Parser coverage is adequate for this run but not yet reusable:** ordinary and bold footer forms parsed cleanly, but nested-parenthesis targets and link-like prose remain future fixtures before promoting a general corpus command.

## Confidence and reversal evidence

**Confidence: high (0.84) for the P/M/X/D/E boundary and for rejecting merge/retire; moderate (0.72) for the exact spelling `premised-on`.** The evidence is the complete 283-row resolved inventory, the 160-row repeated premise pattern, full reads of boundary cases, current authorization contracts, and the three reciprocal-pair check.

The recommendation should be reversed if a blind second classification finds that roughly 20% or more of P rows actually trigger design/rule reconsideration rather than truth/applicability reassessment, or if maintainers can state a stable source-subject assertion for `is-grounded-in` that excludes evidence, mechanism, and `rests-on` without a longer context gloss. A future migration dry run that cannot conserve the 160 P tuples, or a contract review showing that readers do not use premise edges to decide what to verify next, would also reopen the recommendation.

## Changed paths and verification

Changed path: `kb/work/linking-contract-consistency/grounds-label-direction-review.md`. No corpus, contract, catalogue, ADR, or durable instruction was changed. The input work item and the pre-existing `kb/work/linking-contract-consistency/README.md` modification were preserved.

The review and its execution packet pass `commonplace-validate`; `git diff --check` also passes. Tests were not run because this read-only workshop evaluation changes no executable or library surface.
