---
description: "Read-only semantic evaluation of active mechanism edges and grounds rows deferred to mechanism review"
type: kb/types/instruction.md
---

# Mechanism label direction review

**Status:** complete semantic evaluation; no corpus edge, collection contract, catalogue entry, ADR, durable instruction, or prior workshop result was changed.

**Date:** 2026-07-28
**Requested model:** Luna, as requested by the parent dispatch.
**Executing model:** current Codex runtime (GPT-5 family as exposed to this session). No Luna dispatch or runtime identity was available, so this review makes no stronger Luna provenance claim.

## Recommendation

Choose outcome 2: split the current cohort into two source-as-subject relations where the corpus supplies two different reader decisions.

1. Adopt **`explained-by`** for the broad explanatory relation:

   > **source claim or phenomenon `explained-by` explanatory target**

   Reader need: understand why or how the source claim operates by reading the target's explanatory account. The target may be a theoretical claim, but the edge does not assert that the target is a premise, evidence, or implementation.

2. Adopt **`operates-through`** for the narrower operational relation:

   > **source phenomenon or capability `operates-through` process, component, or operational artifact target**

   Reader need: inspect the process or component through which the source literally produces its behavior or effect. This is stronger than “the target explains it”: changing the target's operation calls for an operational/interface review of the source.

3. Leave **10 prerequisite-shaped rows** explicitly unresolved between the still-directionally unsettled `enables` and `precondition` vocabularies. Do not silently assign either identifier.

Of the 128 in-scope rows, 41 are explanatory, 72 operational, 10 prerequisite-shaped, 3 extension/exemplification, 1 premise, and 1 evidence. The two old origins are not semantically identical: 19 active `mechanism` rows are explanatory and 51 operational, while the deferred `grounds` rows contain 22 explanatory and 21 operational rows plus the boundary residue. The old `mechanism` identifier therefore cannot be renamed in place, and the deferred `grounds` rows cannot be migrated merely because their coarse review bucket says mechanism.

## Governing test and method

I applied [ADR 020](../../reference/adr/020-theoretical-default-contrasts-mechanism.md)'s “by what operation?” distinction, the source-as-subject invariant from [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md), and the `rests-on` boundary in [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-are-reclassified.md). I also read the current [link vocabulary](../../reference/link-vocabulary.md), relevant collection contracts, the [directional grammar](./directional-label-grammar.md), the [grounds direction review](./grounds-label-direction-review.md), and the [grounds boundary adjudication](./grounds-label-boundary-adjudication.md).

The positive mutable surface was rebaselined as active registered footer links in `kb/notes/`, `kb/reference/` excluding `proposals/archive/`, `kb/instructions/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, active source analyses/ingests, and `kb/types/`. It includes:

- every active `mechanism` footer;
- exactly the rows classified as mechanism-like by the grounds direction review and left deferred by the grounds boundary adjudication;
- no other active `grounds` row.

A one-shot scanner resolved every target before classification, accepted ordinary and bold footer forms, required one Markdown link before each `— mechanism:`, `-- mechanism:`, `— grounds:`, or `-- grounds:` marker, and reported no unsupported syntax on the active surface. The temporary scanner was not retained. Local context was read for all rows; full source and target artifacts were opened for representative explanatory, operational, prerequisite, evidence, and same-file cases.

## Inventory and exclusions

### All registered old-label rows

| origin | active mutable | generated reports | workshop history | archived proposals | all registered |
|---|---:|---:|---:|---:|---:|
| `mechanism` | 79 | 159 | 53 | 0 | 291 |
| `grounds` | 285 | 1,637 | 178 | 1 | 2,101 |

No immutable source snapshot contributed a registered row. Ordinary prose, quotations, and unregistered examples were not counted.

### Evaluation surface and scope exclusions

| origin/scope | source→destination | rows | source files | treatment |
|---|---|---:|---:|---|
| active `mechanism` | notes→notes | 78 | 55 | in scope |
| active `mechanism` | reference→notes | 1 | 1 | in scope; authorization gap to review later |
| deferred `grounds` | notes→notes | 49 | 39 | in scope; origin preserved |
| **positive surface** |  | **128** | **86 across both origins** | complete ledger below |
| active `grounds` not deferred | notes→notes | 229 | — | excluded from this review; already adjudicated or outside the mechanism bucket |
| active `grounds` not deferred | sources→notes | 7 | — | excluded; evidence drift, not mechanism review |
| generated/workshop/archive rows | by origin above | 2,028 | — | excluded historical/generated material |

The current active `grounds` total is 285: 278 notes→notes and 7 sources→notes. The 49 deferred rows are a subset of the 278 note→note rows, so they must not be added to the 285 as new tuples. The positive surface is 79 + 49 = 128.

## Semantic dispositions

The final classes are mutually exclusive. `EX` and `OP` are the two candidate successors. `EN` records a prerequisite-shaped assertion without deciding between the unresolved labels. The remaining classes are exact reclassifications into existing relations.

| code | disposition | mechanism origin | deferred grounds origin | total | successor/test |
|---|---|---:|---:|---:|---|
| EX | explanatory claim | 19 | 22 | 41 | candidate `explained-by` |
| OP | operational mechanism | 51 | 21 | 72 | candidate `operates-through` |
| EN | enabling condition or prerequisite | 7 | 3 | 10 | later `enables`/`precondition` adjudication; no silent assignment |
| X | extension or exemplification | 2 | 1 | 3 | existing `extends` or `exemplifies` |
| P | premise dependence | 0 | 1 | 1 | `premised-on` |
| E | evidence | 0 | 1 | 1 | `is-evidence-for` |
| R | `rests-on` dependency | 0 | 0 | 0 | no source design/rule/description dependency in this surface |
| D | definition, implementation, comparison/navigation | 0 | 0 | 0 | no exact case requiring these classes |
| removal | 0 | 0 | 0 | no row earns removal |
| unresolved beyond EN | 0 | 0 | 0 | every row has a best current class |
| **total** |  | **79** | **49** | **128** | reconciles exactly |

### Boundary tests

- **EX / `explained-by`:** the target is an explanatory account or general principle answering why/how the source phenomenon occurs. Rejecting or revising the target prompts re-reading the source's causal argument, not automatically changing an implementation.
- **OP / `operates-through`:** the target is a process, component, control path, artifact, or operational rule through which the source effect is produced. A target change prompts an interface, behavior, or operational fit review.
- **EN / prerequisite:** the target is a condition that must be available, true, or completed for the source claim/process to work. The corpus does not yet decide whether the source asserts “the target enables the source” or “the source has the target as a precondition”; the current identifiers are directionally inconsistent or unauthorized in this pairing.
- **P / `premised-on`:** the target is a premise whose rejection reopens the source's truth or applicability. The single deferred row is not mechanism-like after full review.
- **E / evidence:** the source observation bears on the target assertion without implying target-side uptake. The single deferred row is a telemetry note pointing at an oracle claim.
- **X / `extends` or `exemplifies`:** the source develops or instantiates the target rather than using it as its causal mechanism.
- **`rests-on`:** reserved for source design, rule, description, procedure, or system-definition artifacts whose target's rejection triggers reconsideration. No positive row meets that test.

## Candidate outcomes

### `explained-by` as one broad successor

**For:** 41 rows directly ask the reader to understand why or how a source claim works. It completes `source explained-by target` naturally, avoids the old target-role grammar, and is broad enough for explanatory theory without asserting deductive entailment or evidential support.

**Against:** it would overgeneralize the 72 OP rows. “Explains” is often used in ordinary prose for a component that actually performs the operation; a single successor would erase the maintenance difference between revising an explanation and changing the process through which behavior occurs.

### `operates-through` as one narrow successor

**For:** 72 rows name a process, component, or operational artifact that does the work: scoped sub-agents, frontloading, compaction, retrieval, codification, error-correction loops, and similar paths. `source operates-through target` is source-subject and makes the operational landing map explicit.

**Against:** it is false for target claims such as the verification boundary, oracle theory, epiplexity, or the bitter-lesson boundary. It would make readers inspect an implementation path where the source actually needs an explanatory account.

### Split — recommended

The two cohorts produce different follow/skip decisions. A reader can skip an explanatory target when the mechanism is already understood but cannot skip the operational target when implementing, debugging, or tracing the source effect. Likewise, a target change has different maintenance consequences: EX requires causal-argument review; OP requires process/interface review. The nine same-file cases show both signals often coexist and do not collapse into one authoring decision.

The split is principled only if `operates-through` stays narrow. It must not become a synonym for “has a mechanism section,” “is related to the process,” or “the target is useful background.” If the operational target is merely a theory explaining the process, use `explained-by`; if it is a literal execution path or component, use `operates-through`.

### Reclassify or retire with no successor

Reclassification is required for 16 rows outside the two successors: 10 EN, 3 X, 1 P, and 1 E. Retirement is not suitable for EX or OP: 113 rows repeat a stable reader need across 95 source files. Connective prose remains appropriate for weak one-off links, but formal labels earn their cost for this cohort.

## Same-file comparison

All nine files that author both active `mechanism` and deferred `grounds` were inspected. They are not a privileged sample; they are a drift diagnostic.

| source file | active `mechanism` edges | deferred `grounds` edges | comparison |
|---|---|---|---|
| `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md` | `abstract-an-experience...` | `first-principles...`; `diagnostic-richness...` | mechanism/process target versus explanatory premise and evidence prerequisite |
| `kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md` | `evaluation-automation...`; `error-correction...` | `weakly-discriminated...` | operational checks versus explanatory selection pressure |
| `kb/notes/frontloading-spares-execution-context.md` | `frontloading-is-partial-evaluation...` | `agent-context-is-constrained...` | explanation of the technique versus explanatory context boundary; both were historically called mechanism/grounds by different local needs |
| `kb/notes/llm-context-is-composed-without-scoping.md` | `agent-statelessness...` | `instruction-specificity...`; `scheduler-llm-separation...` | literal context-injection path versus operational scoping/binding explanations; the old distinction is not stable enough to infer from label alone |
| `kb/notes/llm-executed-methodologies-are-metacircular-interpreters.md` | `methodology-enforcement...` | `system-definition-artifact...` | enforcement gradient is operational/explanatory; target artifact explains behavioral force |
| `kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md` | `constraining...`; `deploy-time-learning...` | `llm-context-is-composed...` | concrete constraining and persistence paths versus the context substrate they depend on |
| `kb/notes/orchestration-strategies-and-run-state-have-opposite-persistence.md` | `ephemeral...`; `deploy-time...`; `codification`; `verifiability-gradient` | `bounded-context-orchestration...` | operational promotion path versus the explanatory `select`/`K` model |
| `kb/notes/reflection-makes-retained-lessons-second-order.md` | `retrieval-failure...` | `reflection-buys-addressability...` | retrieval path versus addressability premise/operation |
| `kb/notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` | `reflection-makes...`; `false-positive...` | `reasoning-production...` | revision operations versus explanatory production/evaluation distinction |

The overlap demonstrates why source-file co-occurrence cannot define the boundary: several files use `mechanism` for both explanatory principles and literal operational paths, while `grounds` sometimes names an explanation, a prerequisite, or a premise. The row-level assertion must decide.

## Prerequisite rows held for later adjudication

These exact rows are `EN`; they must not be silently written as `enables` or `precondition` in a later mechanism migration:

- `mechanism` `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38` → `notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `mechanism` `notes/brainstorming-maintainability-oracles-for-agentic-development.md:190` → `notes/evaluation-automation-is-phase-gated-by-comprehension.md`
- `mechanism` `notes/brainstorming-maintainability-oracles-for-agentic-development.md:191` → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/enforcement-without-structured-recovery-is-incomplete.md:69` → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:112` → `notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `mechanism` `notes/verifiable-subroles-before-reviewer-identity.md:58` → `notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`
- `mechanism` `notes/verifiable-subroles-before-reviewer-identity.md:60` → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81` → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `grounds-deferred` `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64` → `notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `grounds-deferred` `notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61` → `notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

The unresolved vocabulary is a direction problem, not a reason to call every operational prerequisite a mechanism. A later `enables`/`precondition` review should compare the literal assertions and collection authorizations before migration.

## Exact disposition ledger

Every positive-surface tuple appears once below. The origin token preserves whether the live footer used `mechanism` or was deferred from `grounds`.

### EX — explanatory claim (41)

- `mechanism` `notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md:70 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `mechanism` `notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:69 → notes/weakly-discriminated-qualities-tend-to-be-underselected.md`
- `mechanism` `notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md:62 → notes/indirection-is-costly-in-llm-instructions.md`
- `mechanism` `notes/false-positive-generation-is-filtered-before-retention.md:69 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `mechanism` `notes/frontloading-spares-execution-context.md:56 → notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md`
- `mechanism` `notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md:59 → notes/llm-generation-confidence-tracks-typicality-not-soundness.md`
- `mechanism` `notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md:45 → notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`
- `mechanism` `notes/llm-executed-methodologies-are-metacircular-interpreters.md:36 → notes/methodology-enforcement-is-constraining.md`
- `mechanism` `notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md:38 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `mechanism` `notes/raw-accumulation-does-not-create-usable-memory.md:31 → notes/constraining-and-extraction-both-trade-generality-for-reliability.md`
- `mechanism` `notes/raw-accumulation-does-not-create-usable-memory.md:32 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `mechanism` `notes/retrieval-failure-is-reflection-failure.md:38 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `mechanism` `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:52 → notes/ephemeral-computation-prevents-accumulation.md`
- `mechanism` `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:54 → notes/verifiability-gradient.md`
- `mechanism` `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:51 → notes/false-positive-generation-is-filtered-before-retention.md`
- `mechanism` `notes/task-fitted-structure-costs-cross-task-reuse.md:71 → notes/orchestration-strategies-and-run-state-have-opposite-persistence.md`
- `mechanism` `notes/technical-constraints-make-kb-objective-choice-engineering.md:81 → notes/codify-versus-llm-decision-heuristics.md`
- `mechanism` `notes/technical-constraints-make-kb-objective-choice-engineering.md:84 → notes/oracle-strength-spectrum.md`
- `mechanism` `notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:48 → notes/opacity-is-a-scale-threshold.md`
- `grounds-deferred` `notes/a-consumption-channel-delivers-force-without-the-history-that.md:78 → notes/definitions/reflective-system.md`
- `grounds-deferred` `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:63 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `grounds-deferred` `notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:66 → notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`
- `grounds-deferred` `notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md:49 → notes/stale-indexes-are-worse-than-no-indexes.md`
- `grounds-deferred` `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:39 → notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`
- `grounds-deferred` `notes/brainstorming-maintainability-oracles-for-agentic-development.md:188 → notes/weakly-discriminated-qualities-tend-to-be-underselected.md`
- `grounds-deferred` `notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md:55 → notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md`
- `grounds-deferred` `notes/codify-versus-llm-decision-heuristics.md:120 → notes/ephemeral-computation-prevents-accumulation.md`
- `grounds-deferred` `notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md:62 → notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md`
- `grounds-deferred` `notes/definitions/reach-assessment.md:66 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `grounds-deferred` `notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md:64 → notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`
- `grounds-deferred` `notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md:47 → notes/definitions/representational-form.md`
- `grounds-deferred` `notes/frontloading-spares-execution-context.md:53 → notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md`
- `grounds-deferred` `notes/increasing-computational-autonomy-relocates-human-effort.md:59 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `grounds-deferred` `notes/llm-context-is-a-homoiconic-medium.md:45 → notes/methodology-enforcement-is-constraining.md`
- `grounds-deferred` `notes/llm-executed-methodologies-are-metacircular-interpreters.md:38 → notes/definitions/system-definition-artifact.md`
- `grounds-deferred` `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:46 → notes/bounded-context-orchestration-model.md`
- `grounds-deferred` `notes/reasoning-production-is-not-reasoning-evaluation.md:43 → notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`
- `grounds-deferred` `notes/reverse-compression-is-when-llm-output-expands-without-adding.md:43 → notes/information-value-is-observer-relative.md`
- `grounds-deferred` `notes/runtime-structure-determines-governance-control-surfaces.md:56 → notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`
- `grounds-deferred` `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:49 → notes/reasoning-production-is-not-reasoning-evaluation.md`
- `grounds-deferred` `notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md:73 → notes/synthesis-is-not-error-correction.md`

### OP — operational mechanism (72)

- `mechanism` `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:102 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `mechanism` `notes/bounded-context-orchestration-model.md:92 → notes/llm-context-is-composed-without-scoping.md`
- `mechanism` `notes/bounded-context-orchestration-model.md:97 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `mechanism` `notes/commitment-not-derivation-creates-new-ground-truth.md:92 → notes/progressive-constraining-commits-only-after-patterns-stabilize.md`
- `mechanism` `notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:28 → notes/llm-context-is-a-homoiconic-medium.md`
- `mechanism` `notes/decomposition-heuristics-for-bounded-context-scheduling.md:91 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `mechanism` `notes/definitions/context-engineering.md:63 → notes/instruction-specificity-should-match-loading-frequency.md`
- `mechanism` `notes/definitions/context-engineering.md:64 → notes/llm-context-is-composed-without-scoping.md`
- `mechanism` `notes/definitions/context-engineering.md:65 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `mechanism` `notes/deploy-time-learning-is-the-missing-middle.md:56 → notes/llm-context-is-a-homoiconic-medium.md`
- `mechanism` `notes/design-for-the-first-time-human-except-on-access-cost.md:26 → notes/feasibility-is-the-heaviest-forks-net-load.md`
- `mechanism` `notes/design-for-the-first-time-human-except-on-access-cost.md:28 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `mechanism` `notes/enforcement-without-structured-recovery-is-incomplete.md:69 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/entropy-management-must-scale-with-generation-throughput.md:31 → notes/spec-mining-as-codification.md`
- `mechanism` `notes/error-messages-that-teach-are-a-constraining-technique.md:28 → notes/frontloading-spares-execution-context.md`
- `mechanism` `notes/feasibility-is-the-heaviest-forks-net-load.md:36 → notes/frontloading-spares-execution-context.md`
- `mechanism` `notes/feasibility-is-the-heaviest-forks-net-load.md:37 → notes/agents-navigate-by-deciding-what-to-read-next.md`
- `mechanism` `notes/feasibility-is-the-heaviest-forks-net-load.md:38 → notes/session-history-should-not-be-the-default-next-context.md`
- `mechanism` `notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md:61 → notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`
- `mechanism` `notes/links-encode-conditional-possibilities-not-obligations.md:107 → notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md`
- `mechanism` `notes/llm-context-is-composed-without-scoping.md:75 → notes/agent-statelessness-means-the-context-engine-should-inject-context.md`
- `mechanism` `notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md:35 → notes/session-history-should-not-be-the-default-next-context.md`
- `mechanism` `notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:59 → notes/definitions/constraining.md`
- `mechanism` `notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:60 → notes/deploy-time-learning-is-the-missing-middle.md`
- `mechanism` `notes/methodological-and-computational-closure-track-different-changes.md:80 → notes/reflection-buys-addressability.md`
- `mechanism` `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:48 → notes/ephemeral-computation-prevents-accumulation.md`
- `mechanism` `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:49 → notes/deploy-time-learning-is-the-missing-middle.md`
- `mechanism` `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:50 → notes/definitions/codification.md`
- `mechanism` `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md:51 → notes/verifiability-gradient.md`
- `mechanism` `notes/pointer-design-tradeoffs-in-progressive-disclosure.md:80 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `mechanism` `notes/reflection-makes-retained-lessons-second-order.md:53 → notes/retrieval-failure-is-reflection-failure.md`
- `mechanism` `notes/reflective-coverage-is-graded-across-representational-forms.md:100 → notes/unified-calling-conventions-enable-bidirectional-refactoring.md`
- `mechanism` `notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md:53 → notes/deploy-time-learning-is-the-missing-middle.md`
- `mechanism` `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md:46 → notes/reflection-makes-retained-lessons-second-order.md`
- `mechanism` `notes/session-history-should-not-be-the-default-next-context.md:82 → notes/theory-and-methodology-form-a-two-layer-execution-system.md`
- `mechanism` `notes/spec-mining-as-codification.md:59 → notes/oracle-strength-spectrum.md`
- `mechanism` `notes/stale-self-description-conceals-its-own-staleness.md:70 → notes/reflection-buys-addressability.md`
- `mechanism` `notes/stale-self-description-conceals-its-own-staleness.md:71 → notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md`
- `mechanism` `notes/structure-inference-needs-capture-at-the-decision-surface.md:37 → notes/spec-mining-as-codification.md`
- `mechanism` `notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md:60 → notes/llm-context-is-a-homoiconic-medium.md`
- `mechanism` `notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md:46 → notes/definitions/codification.md`
- `mechanism` `notes/the-framework-is-often-larger-than-the-durable-contribution.md:62 → notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md`
- `mechanism` `notes/the-practical-scheduler-is-the-host-language.md:66 → notes/agent-is-a-tool-loop.md`
- `mechanism` `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:59 → notes/reflection-makes-retained-lessons-second-order.md`
- `mechanism` `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md:60 → notes/retrieval-failure-is-reflection-failure.md`
- `mechanism` `notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md:63 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `mechanism` `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md:63 → notes/scenario-decomposition-drives-architecture.md`
- `mechanism` `notes/verifiable-subroles-before-reviewer-identity.md:60 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/verifiable-subroles-before-reviewer-identity.md:62 → notes/structured-output-is-easier-for-humans-to-review.md`
- `mechanism` `notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md:58 → notes/axes-of-artifact-analysis.md`
- `mechanism` `reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md:46 → notes/spec-mining-as-codification.md`
- `grounds-deferred` `notes/a-consumption-channel-delivers-force-without-the-history-that.md:76 → notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`
- `grounds-deferred` `notes/a-consumption-channel-delivers-force-without-the-history-that.md:77 → notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`
- `grounds-deferred` `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:70 → notes/text-testing-framework.md`
- `grounds-deferred` `notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md:64 → notes/llm-context-is-composed-without-scoping.md`
- `grounds-deferred` `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:28 → notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`
- `grounds-deferred` `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:30 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `grounds-deferred` `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:40 → notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md`
- `grounds-deferred` `notes/always-loaded-context-mechanisms-in-agent-harnesses.md:89 → notes/frontloading-spares-execution-context.md`
- `grounds-deferred` `notes/an-action-model-matters-only-through-its-consumption-path.md:24 → notes/axes-of-artifact-analysis.md`
- `grounds-deferred` `notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md:45 → notes/frontloading-spares-execution-context.md`
- `grounds-deferred` `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:58 → notes/bounded-context-orchestration-model.md`
- `grounds-deferred` `notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md:61 → notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`
- `grounds-deferred` `notes/context-contamination-operates-below-an-agents-compliance-reasoning.md:57 → notes/agent-orchestration-needs-coordination-guarantees-not-just.md`
- `grounds-deferred` `notes/evaluation-automation-is-phase-gated-by-comprehension.md:50 → notes/spec-mining-as-codification.md`
- `grounds-deferred` `notes/llm-context-is-composed-without-scoping.md:72 → notes/instruction-specificity-should-match-loading-frequency.md`
- `grounds-deferred` `notes/llm-context-is-composed-without-scoping.md:78 → notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`
- `grounds-deferred` `notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md:56 → notes/llm-context-is-composed-without-scoping.md`
- `grounds-deferred` `notes/reasoning-production-is-not-reasoning-evaluation.md:44 → notes/process-structure-and-output-structure-are-independent-levers.md`
- `grounds-deferred` `notes/reflection-makes-retained-lessons-second-order.md:49 → notes/reflection-buys-addressability.md`
- `grounds-deferred` `notes/scenario-decomposition-drives-architecture.md:86 → notes/skills-derive-from-methodology.md`
- `grounds-deferred` `notes/semantic-review-catches-content-errors-that-structural-validation.md:49 → notes/text-testing-framework.md`

### EN — enabling condition or prerequisite (10)

- `mechanism` `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:38 → notes/abstract-an-experience-only-when-you-can-state-the-boundary.md`
- `mechanism` `notes/brainstorming-maintainability-oracles-for-agentic-development.md:190 → notes/evaluation-automation-is-phase-gated-by-comprehension.md`
- `mechanism` `notes/brainstorming-maintainability-oracles-for-agentic-development.md:191 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md:56 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `mechanism` `notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md:112 → notes/warranted-autonomy-is-bounded-by-oracle-domain.md`
- `mechanism` `notes/verifiable-subroles-before-reviewer-identity.md:58 → notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`
- `mechanism` `notes/weakly-discriminated-qualities-tend-to-be-underselected.md:81 → notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`
- `grounds-deferred` `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md:64 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`
- `grounds-deferred` `notes/abstract-an-experience-only-when-you-can-state-the-boundary.md:61 → notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`
- `grounds-deferred` `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:40 → notes/diagnostic-richness-constrains-outer-loop-learning-quality.md`

### X — extension or exemplification (3)

- `mechanism` `notes/bounded-context-orchestration-model.md:90 → notes/frontloading-spares-execution-context.md`
- `mechanism` `notes/the-framework-is-often-larger-than-the-durable-contribution.md:63 → notes/conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`
- `grounds-deferred` `notes/automated-synthesis-is-missing-good-oracles.md:58 → notes/the-boundary-of-automation-is-the-boundary-of-verification.md`

### P — premise dependence (1)

- `grounds-deferred` `notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md:36 → notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md`

### E — evidence (1)

- `grounds-deferred` `notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md:72 → notes/oracle-strength-spectrum.md`

## Inverse and incoming-pattern decision

The current labels are upstream-pointing and fan out toward explanatory or operational targets. Reciprocal authoring is not required. The mechanism surface contains no repeated inverse journey that would justify a registered inverse such as `explains` or `is-operated-by`; incoming links remain derived on demand. `operates-through` has no formal inverse in this review. A target may independently curate a `see-also`, `contains`, or other edge if its own reader need warrants it.

## Authorization and later migration consequences

No authorization surface changes here. `kb/notes/COLLECTION.md` authorizes `mechanism` for notes→notes but does not authorize `explained-by` or `operates-through`; a later migration would replace the old label with the adopted successors and update the shared catalogue, notes contract, and authoring guidance together. It must preserve origin labels in the grounds migration ledger until every deferred row receives its final successor.

The one reference→notes `mechanism` row is currently outside the reference contract's listed labels and needs a source-contract decision. The 49 deferred grounds rows are currently authorized as grounds by the notes contract, but their successors may be `explained-by`, `operates-through`, an existing label, or a later prerequisite relation. No contract should be widened merely to preserve current drift.

A later migration must rebaseline again, conserve exact source→target tuples by origin, and independently reconcile old labels, excluded rows, and deferred prerequisite rows. This review does not authorize or plan those mutations.

## Surprises and procedure improvements

- **The old `mechanism` corpus is not one operational class:** 19 of 79 active rows are explanatory claims, so a lexical source-subject rename would create false `operates-through` assertions.
- **The deferred `grounds` bucket contains real mechanism-shaped drift but also boundary residue:** 22 explanatory and 21 operational rows are joined by 10 prerequisite-shaped, one premise, and one evidence row. The origin label is essential for later tuple conservation, not semantic privilege.
- **Same-file co-occurrence is informative but not decisive:** all nine overlap files contain both labels, but their local pairs do not expose one stable lexical rule. Classification must read the assertion and target function.
- **A reference→notes mechanism row remains:** active `mechanism` is not confined to notes→notes; source collection authorization must be checked in the later migration.
- **Parser coverage:** ordinary and bold footer forms parsed cleanly with no active syntax failures. Nested-parenthesis targets and link-like prose remain fixtures needed before promoting a reusable parser.

## Confidence and reversal evidence

**Confidence: high (0.81) for the EX/OP split and for rejecting one broad successor; moderate (0.67) for the exact spelling `operates-through`, and low-to-moderate (0.58) for the unresolved EN boundary.** Evidence includes the complete 128-row resolved inventory, full reads of representative source/target pairs, the nine same-file comparison, and the explicit operational/explanatory distinction in ADR 020.

Reverse the split if a blind second classification cannot distinguish “the target is the explanatory account” from “the target is the process/component through which the effect occurs” without source-specific prose, or if maintainers find that changing an OP target never triggers a distinct operational/interface review. Prefer one successor only if a single assertion template excludes both overclaiming causation and collapsing process identity into explanation. Resolve EN before migration if a source-subject test establishes one direction for `enables` or `precondition` across these rows.

## Changed paths and verification

Changed path: `kb/work/linking-contract-consistency/mechanism-label-direction-review.md`. No corpus, contract, catalogue, ADR, durable instruction, or prior workshop result was changed. The pre-existing `README.md`, work item, and grounds boundary adjudication remain untouched.

The review was generated from read-only inventories. Validation, exact ledger reconciliation, and `git diff --check` are the final checks after writing this file. No unrelated test or validation failure was observed during this semantic evaluation.
