---
description: "Frozen audit snapshot of link-relationship labels used across KB footer annotations. Generator script retired; kept as the corpus evidence behind ADR 020 (theoretical-default additions: contrasts, mechanism)."
type: note
---

# Link vocabulary audit

Footer-annotation labels grouped by `(source register → target register)`. ADR 009 vocabulary: `contradicts, enables, example, exemplifies, extends, foundation, grounds`. Status column: `adr+matrix` (declared in both), `adr-only`, `matrix-only`, or `off-vocab`.

- Footer-shaped link lines matched: **3419**
- With a label-shaped prefix: **2308**
- Unlabelled (prose-only annotations): **1111**

## theoretical → theoretical  (n = 1187)

Matrix vocabulary for this edge: `because, contradicts, extends, qualifies, since`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 361 | off-vocab | `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` → `./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` |
| `extends` | 138 | adr+matrix | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./title-as-claim-enables-traversal-as-reasoning.md` |
| `foundation` | 128 | adr-only | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./first-principles-reasoning-selects-for-explanatory-reach-over.md` |
| `grounds` | 80 | adr-only | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./an-agentic-kb-maximizes-contextual-competence-through-discoverable.md` |
| `enables` | 42 | adr-only | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./deploy-time-learning-is-the-missing-middle.md` |
| `exemplifies` | 32 | adr-only | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./skills-derive-from-methodology-through-distillation.md` |
| `mechanism` | 31 | off-vocab | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` → `./indirection-is-costly-in-llm-instructions.md` |
| `context` | 22 | off-vocab | `kb/notes/agent-is-a-tool-loop.md` → `./tool-loop-index.md` |
| `applies` | 16 | off-vocab | `kb/notes/agentic-systems-interpret-underspecified-instructions.md` → `./underspecification-and-indeterminism-complicate-programming-for.md` |
| `instance` | 15 | off-vocab | `kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md` → `./skills-derive-from-methodology-through-distillation.md` |
| `sharpens` | 15 | off-vocab | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` → `./effective-context-is-task-relative-and-complexity-relative-not-a.md` |
| `motivates` | 14 | off-vocab | `kb/notes/agent-is-a-tool-loop.md` → `./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md` |
| `complements` | 13 | off-vocab | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` → `./knowledge-storage-does-not-imply-contextual-activation.md` |
| `consequence` | 13 | off-vocab | `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md` → `./tool-loop-index.md` |
| `parallel` | 12 | off-vocab | `kb/notes/agent-statelessness-means-the-context-engine-should-inject-context.md` → `../notes/instructions-are-typed-callables.md` |
| `contrasts` | 10 | off-vocab | `kb/notes/axes-of-substrate-analysis.md` → `./memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `example` | 9 | adr-only | `kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md` → `./generate-instructions-at-build-time.md` |
| `complementary` | 7 | off-vocab | `kb/notes/human-writing-structures-transfer-to-llms-because-failure-modes.md` → `./structure-activates-higher-quality-training-distributions.md` |
| `develops` | 7 | off-vocab | `kb/notes/automating-kb-learning-is-an-open-problem.md` → `./automated-synthesis-is-missing-good-oracles.md` |
| `tension` | 7 | off-vocab | `kb/notes/evolving-understanding-needs-re-distillation-not-composition.md` → `./short-composable-notes-maximize-combinatorial-discovery.md` |
| `parallels` | 6 | off-vocab | `kb/notes/automated-synthesis-is-missing-good-oracles.md` → `./memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `refines` | 6 | off-vocab | `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` → `./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` |
| `synthesis` | 6 | off-vocab | `kb/notes/automating-kb-learning-is-an-open-problem.md` → `./the-boundary-of-automation-is-the-boundary-of-verification.md` |
| `application` | 5 | off-vocab | `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md` → `./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md` |
| `related` | 5 | off-vocab | `kb/notes/llm-code-boundaries-are-natural-checkpoints.md` → `./definitions/constraining.md` |
| `constrains` | 4 | off-vocab | `kb/notes/entropy-management-must-scale-with-generation-throughput.md` → `./automating-kb-learning-is-an-open-problem.md` |
| `contrast` | 4 | off-vocab | `kb/notes/evolving-understanding-needs-re-distillation-not-composition.md` → `./storing-llm-outputs-is-constraining.md` |
| `distinguishes` | 4 | off-vocab | `kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md` → `./interpretation-errors-are-failures-of-the-interpreter.md` |
| `evidence` | 4 | off-vocab | `kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md` → `./llm-context-is-composed-without-scoping.md` |
| `synthesizes` | 4 | off-vocab | `kb/notes/brainstorming-how-to-enrich-web-search.md` → `./link-following-and-search-impose-different-metadata-requirements.md` |
| `background` | 3 | off-vocab | `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` → `./definitions/codification.md` |
| `boundary` | 3 | off-vocab | `kb/notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md` → `./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` |
| `boundary-case` | 3 | off-vocab | `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md` → `./rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md` |
| `co-equal-mechanism` | 3 | off-vocab | `kb/notes/definitions/constraining.md` → `./distillation.md` |
| `component-view` | 3 | off-vocab | `kb/notes/bounded-context-orchestration-model.md` → `./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` |
| `motivation` | 3 | off-vocab | `kb/notes/bounded-context-orchestration-model.md` → `./context-efficiency-is-the-central-design-concern-in-agent-systems.md` |
| `parent-area` | 3 | off-vocab | `kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md` → `./llm-interpretation-errors-index.md` |
| `qualifies` | 3 | matrix-only | `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` → `./brainstorming-how-reach-informs-kb-design.md` |
| `sibling` | 3 | off-vocab | `kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md` → `./interpretation-errors-are-failures-of-the-interpreter.md` |
| `bounded-by` | 2 | off-vocab | `kb/notes/agentic-systems-interpret-underspecified-instructions.md` → `./interpretation-errors-are-failures-of-the-interpreter.md` |
| `clarifies` | 2 | off-vocab | `kb/notes/access-burden-and-transformation-burden-are-independent-query.md` → `./effective-context-is-task-relative-and-complexity-relative-not-a.md` |
| `complicates` | 2 | off-vocab | `kb/notes/bounded-context-orchestration-model.md` → `./agentic-systems-interpret-underspecified-instructions.md` |
| `concretizes` | 2 | off-vocab | `kb/notes/claw-learning-is-broader-than-retrieval.md` → `./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` |
| `connects` | 2 | off-vocab | `kb/notes/entropy-management-must-scale-with-generation-throughput.md` → `./methodology-enforcement-is-constraining.md` |
| `cost-model` | 2 | off-vocab | `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md` → `./context-efficiency-is-the-central-design-concern-in-agent-systems.md` |
| `deepens` | 2 | off-vocab | `kb/notes/reliability-dimensions-map-to-oracle-hardening-stages.md` → `./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` |
| `example-source` | 2 | off-vocab | `kb/notes/skills-derive-from-methodology-through-distillation.md` → `./title-as-claim-enables-traversal-as-reasoning.md` |
| `explains` | 2 | off-vocab | `kb/notes/axes-of-substrate-analysis.md` → `./system-definition-artifacts-are-crystallized-reasoning-under-context.md` |
| `formalizes` | 2 | off-vocab | `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` → `./bounded-context-orchestration-model.md` |
| `frame` | 2 | off-vocab | `kb/notes/readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md` → `./treat-continual-learning-as-substrate-coevolution.md` |
| `intensified-by` | 2 | off-vocab | `kb/notes/agentic-systems-interpret-underspecified-instructions.md` → `./context-efficiency-is-the-central-design-concern-in-agent-systems.md` |
| `intensifies` | 2 | off-vocab | `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md` → `./llm-context-is-a-homoiconic-medium.md` |
| `narrows` | 2 | off-vocab | `kb/notes/automated-synthesis-is-missing-good-oracles.md` → `./automating-kb-learning-is-an-open-problem.md` |
| `one-mechanism` | 2 | off-vocab | `kb/notes/constraining-and-distillation-both-trade-generality-for-reliability.md` → `./definitions/constraining.md` |
| `operationalizes` | 2 | off-vocab | `kb/notes/entropy-management-must-scale-with-generation-throughput.md` → `./maintenance-operations-catalogue-should-stage-distillation-into.md` |
| `operator` | 2 | off-vocab | `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` → `./definitions/distillation.md` |
| `operators` | 2 | off-vocab | `kb/notes/readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md` → `./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` |
| `overlaps` | 2 | off-vocab | `kb/notes/frontloading-spares-execution-context.md` → `./indirection-is-costly-in-llm-instructions.md` |
| `parallel-case` | 2 | off-vocab | `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` → `./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` |
| `parent-framing` | 2 | off-vocab | `kb/notes/capability-placement-should-follow-autonomy-readiness.md` → `./agents-md-should-be-organized-as-a-control-plane.md` |
| `situates` | 2 | off-vocab | `kb/notes/spec-mining-as-codification.md` → `./specification-strategy-should-follow-where-understanding-lives.md` |
| `speculative` | 2 | off-vocab | `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` → `./process-structure-and-output-structure-are-independent-levers.md` |
| `supports` | 2 | off-vocab | `kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md` → `./indirection-is-costly-in-llm-instructions.md` |
| `adjacent-mechanism` | 1 | off-vocab | `kb/notes/selector-loaded-review-gates-could-let-review-revise-learn-from.md` → `./automated-tests-for-text.md` |
| `adjacent-method` | 1 | off-vocab | `kb/notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md` → `./prompt-ablation-converts-human-insight-to-deployable-framing.md` |
| `amplification` | 1 | off-vocab | `kb/notes/spec-mining-as-codification.md` → `./error-correction-works-above-chance-oracles-with-decorrelated-checks.md` |
| `amplifies` | 1 | off-vocab | `kb/notes/llm-context-is-composed-without-scoping.md` → `./llm-context-is-a-homoiconic-medium.md` |
| `architectural-remedy` | 1 | off-vocab | `kb/notes/interpretation-errors-are-failures-of-the-interpreter.md` → `./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md` |
| `belongs-to` | 1 | off-vocab | `kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md` → `./observability-index.md` |
| `boundary-condition` | 1 | off-vocab | `kb/notes/quality-signals-for-kb-evaluation.md` → `./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md` |
| `broader-context` | 1 | off-vocab | `kb/notes/tool-loop-index.md` → `./agent-orchestration-occupies-a-multi-dimensional-design-space.md` |
| `certifies` | 1 | off-vocab | `kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md` → `./any-symbolic-program-with-llm-calls-is-a-select-call-program.md` |
| `challenges` | 1 | off-vocab | `kb/notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` → `./memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `complement` | 1 | off-vocab | `kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md` → `./spec-mining-as-codification.md` |
| `complementary-response` | 1 | off-vocab | `kb/notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md` → `./agent-statelessness-means-the-context-engine-should-inject-context.md` |
| `conceptual-foundation` | 1 | off-vocab | `kb/notes/underspecification-and-indeterminism-complicate-programming-for.md` → `./agentic-systems-interpret-underspecified-instructions.md` |
| `concession` | 1 | off-vocab | `kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md` → `./stateful-tools-recover-control-by-becoming-hidden-schedulers.md` |
| `confirms` | 1 | off-vocab | `kb/notes/scenario-decomposition-drives-architecture.md` → `./instruction-specificity-should-match-loading-frequency.md` |
| `contextualises` | 1 | off-vocab | `kb/notes/enforcement-without-structured-recovery-is-incomplete.md` → `./reliability-dimensions-map-to-oracle-hardening-stages.md` |
| `contradicts` | 1 | adr+matrix | `kb/notes/brainstorming-how-reach-informs-kb-design.md` → `./link-graph-plus-timestamps-enables-make-like-staleness-detection.md` |
| `convention` | 1 | off-vocab | `kb/notes/tool-loop-index.md` → `./agent-is-a-tool-loop.md` |
| `core-framing` | 1 | off-vocab | `kb/notes/computational-model-index.md` → `./agentic-systems-interpret-underspecified-instructions.md` |
| `core-theory` | 1 | off-vocab | `kb/notes/tags-index.md` → `./foundations-index.md` |
| `counterposition` | 1 | off-vocab | `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` → `./stateful-tools-recover-control-by-becoming-hidden-schedulers.md` |
| `definition` | 1 | off-vocab | `kb/notes/learning-theory-index.md` → `./definitions/distillation.md` |
| `definition-and-spectrum` | 1 | off-vocab | `kb/notes/learning-theory-index.md` → `./definitions/constraining.md` |
| `depends-on` | 1 | off-vocab | `kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md` → `./types-give-agents-structural-hints-before-opening-documents.md` |
| `detects` | 1 | off-vocab | `kb/notes/entropy-management-must-scale-with-generation-throughput.md` → `./quality-signals-for-kb-evaluation.md` |
| `determines` | 1 | off-vocab | `kb/notes/enforcement-without-structured-recovery-is-incomplete.md` → `./oracle-strength-spectrum.md` |
| `distribution-selection` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./structure-activates-higher-quality-training-distributions.md` |
| `driver` | 1 | off-vocab | `kb/notes/definitions/distillation.md` → `../agent-statelessness-makes-routing-architectural-not-learned.md` |
| `elaborates` | 1 | off-vocab | `kb/notes/execution-indeterminism-is-a-property-of-the-sampling-process.md` → `./agentic-systems-interpret-underspecified-instructions.md` |
| `enables-enforcement` | 1 | off-vocab | `kb/notes/document-types-should-be-verifiable.md` → `./automated-tests-for-text.md` |
| `enforcement` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./type-system-enforces-metadata-that-navigation-depends-on.md` |
| `escalation-path` | 1 | off-vocab | `kb/notes/maintenance-operations-catalogue-should-stage-distillation-into.md` → `./deterministic-validation-should-be-a-script.md` |
| `exemplifies-exclusion` | 1 | off-vocab | `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` → `./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md` |
| `existing-approximation` | 1 | off-vocab | `kb/notes/llm-context-is-composed-without-scoping.md` → `./unified-calling-conventions-enable-bidirectional-refactoring.md` |
| `exploratory-decomposition` | 1 | off-vocab | `kb/notes/foundations-index.md` → `./charting-the-knowledge-access-problem-beyond-rag.md` |
| `extended-from` | 1 | off-vocab | `kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md` → `./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` |
| `extensibility` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./directory-scoped-types-are-cheaper-than-global-types.md` |
| `extracted` | 1 | off-vocab | `kb/notes/charting-the-knowledge-access-problem-beyond-rag.md` → `./access-burden-and-transformation-burden-are-independent-query.md` |
| `extracted-from` | 1 | off-vocab | `kb/notes/access-burden-and-transformation-burden-are-independent-query.md` → `./charting-the-knowledge-access-problem-beyond-rag.md` |
| `failure-mode-transfer` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./human-writing-structures-transfer-to-llms-because-failure-modes.md` |
| `feeds` | 1 | off-vocab | `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` → `./spec-mining-as-codification.md` |
| `formalisation` | 1 | off-vocab | `kb/notes/definitions/context-engineering.md` → `../bounded-context-orchestration-model.md` |
| `generalises` | 1 | off-vocab | `kb/notes/indirection-is-costly-in-llm-instructions.md` → `./frontloading-spares-execution-context.md` |
| `generalizes` | 1 | off-vocab | `kb/notes/methodology-enforcement-is-constraining.md` → `./spec-mining-as-codification.md` |
| `grounds-the-framing` | 1 | off-vocab | `kb/notes/quality-signals-for-kb-evaluation.md` → `../notes/oracle-strength-spectrum.md` |
| `implication` | 1 | off-vocab | `kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover.md` → `./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md` |
| `lever` | 1 | off-vocab | `kb/notes/deploy-time-learning-is-the-missing-middle.md` → `./context-efficiency-is-the-central-design-concern-in-agent-systems.md` |
| `limits` | 1 | off-vocab | `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` → `./unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md` |
| `locates` | 1 | off-vocab | `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` → `./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` |
| `mapped` | 1 | off-vocab | `kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md` → `./definitions/constraining.md` |
| `meta` | 1 | off-vocab | `kb/notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md` → `./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` |
| `method` | 1 | off-vocab | `kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` → `./spec-mining-as-codification.md` |
| `mirrors` | 1 | off-vocab | `kb/notes/methodology-enforcement-is-constraining.md` → `./instruction-specificity-should-match-loading-frequency.md` |
| `models` | 1 | off-vocab | `kb/notes/frontloading-spares-execution-context.md` → `./bounded-context-orchestration-model.md` |
| `navigation` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./types-give-agents-structural-hints-before-opening-documents.md` |
| `operational-extension` | 1 | off-vocab | `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` → `./maintenance-operations-catalogue-should-stage-distillation-into.md` |
| `operationalises` | 1 | off-vocab | `kb/notes/a-knowledge-base-should-support-fluid-resolution-switching.md` → `./agents-navigate-by-deciding-what-to-read-next.md` |
| `operationalization` | 1 | off-vocab | `kb/notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md` → `./alexander-patterns-and-knowledge-system-design.md` |
| `orthogonal-mechanism` | 1 | off-vocab | `kb/notes/definitions/codification.md` → `./distillation.md` |
| `parallel-framing` | 1 | off-vocab | `kb/notes/verifiability-gradient.md` → `./oracle-strength-spectrum.md` |
| `parent-frame` | 1 | off-vocab | `kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` → `./readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md` |
| `parent-index` | 1 | off-vocab | `kb/notes/agentic-systems-interpret-underspecified-instructions.md` → `./learning-theory-index.md` |
| `parent-mechanism` | 1 | off-vocab | `kb/notes/definitions/codification.md` → `./constraining.md` |
| `phase-transition` | 1 | off-vocab | `kb/notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md` → `./definitions/codification.md` |
| `positions` | 1 | off-vocab | `kb/notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md` → `./definitions/constraining.md` |
| `potential-solution` | 1 | off-vocab | `kb/notes/automated-synthesis-is-missing-good-oracles.md` → `./quality-signals-for-kb-evaluation.md` |
| `practical-plan` | 1 | off-vocab | `kb/notes/treat-continual-learning-as-substrate-coevolution.md` → `./readable-substrate-loop-is-the-tractable-unit-for-continual-learning.md` |
| `practical-rules` | 1 | off-vocab | `kb/notes/computational-model-index.md` → `./decomposition-heuristics-for-bounded-context-scheduling.md` |
| `prerequisite` | 1 | off-vocab | `kb/notes/quality-signals-for-kb-evaluation.md` → `./document-types-should-be-verifiable.md` |
| `reference-framework` | 1 | off-vocab | `kb/notes/document-system-index.md` → `./text-testing-framework.md` |
| `reframes-agile` | 1 | off-vocab | `kb/notes/learning-theory-index.md` → `./changing-requirements-conflate-genuine-change-with-disambiguation.md` |
| `related-consequence` | 1 | off-vocab | `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` → `./subtasks-that-need-different-tools-force-loop-exposure-in-agent.md` |
| `related-mechanism` | 1 | off-vocab | `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` → `./stateful-tools-recover-control-by-becoming-hidden-schedulers.md` |
| `related-pattern` | 1 | off-vocab | `kb/notes/backlinks.md` → `./generate-instructions-at-build-time.md` |
| `remedy` | 1 | off-vocab | `kb/notes/interpretation-errors-are-failures-of-the-interpreter.md` → `./error-correction-works-above-chance-oracles-with-decorrelated-checks.md` |
| `reviewability` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./structured-output-is-easier-for-humans-to-review.md` |
| `risk-mitigation` | 1 | off-vocab | `kb/notes/spec-mining-as-codification.md` → `./operational-signals-that-a-component-is-a-relaxing-candidate.md` |
| `same-principle` | 1 | off-vocab | `kb/notes/mcp-bundles-stateless-tools-with-stateful-runtime.md` → `./indirection-is-costly-in-llm-instructions.md` |
| `scope-condition` | 1 | off-vocab | `kb/notes/selector-loaded-review-gates-could-let-review-revise-learn-from.md` → `./automating-kb-learning-is-an-open-problem.md` |
| `seedling` | 1 | off-vocab | `kb/notes/links-index.md` → `./linking-theory.md` |
| `sequencing-heuristic` | 1 | off-vocab | `kb/notes/computational-model-index.md` → `./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md` |
| `shared-structure` | 1 | off-vocab | `kb/notes/automated-synthesis-is-missing-good-oracles.md` → `./synthesis-is-not-error-correction.md` |
| `source` | 1 | off-vocab | `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` → `./alexander-patterns-and-knowledge-system-design.md` |
| `special-case` | 1 | off-vocab | `kb/notes/session-history-should-not-be-the-default-next-context.md` → `./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` |
| `specializes` | 1 | off-vocab | `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` → `./agent-statelessness-means-the-context-engine-should-inject-context.md` |
| `sub-area` | 1 | off-vocab | `kb/notes/document-system-index.md` → `./type-system-index.md` |
| `suggestive-parallel` | 1 | off-vocab | `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` → `./definitions/constraining.md` |
| `target-form` | 1 | off-vocab | `kb/notes/maintenance-operations-catalogue-should-stage-distillation-into.md` → `./skills-are-instructions-plus-routing-and-execution-policy.md` |
| `test` | 1 | off-vocab | `kb/notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md` → `./first-principles-reasoning-selects-for-explanatory-reach-over.md` |
| `unifying-theory` | 1 | off-vocab | `kb/notes/foundations-index.md` → `./an-agentic-kb-maximizes-contextual-competence-through-discoverable.md` |
| `universality` | 1 | off-vocab | `kb/notes/bounded-context-orchestration-model.md` → `./any-symbolic-program-with-llm-calls-is-a-select-call-program.md` |
| `verification` | 1 | off-vocab | `kb/notes/type-system-index.md` → `./document-types-should-be-verifiable.md` |

## workshop → workshop  (n = 546)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 241 | off-vocab | `kb/work/README.md` → `./gate-refactor/README.md` |
| `extends` | 55 | adr-only | `kb/work/review-revise-gated/baseline.md` → `./agent-orchestration-occupies-a-multi-dimensional-design-space.md` |
| `grounds` | 45 | adr-only | `kb/work/review-revise-gated/baseline.md` → `./the-chat-history-model-trades-context-efficiency-for-implementation.md` |
| `exemplifies` | 44 | adr-only | `kb/work/review-revise-gated/baseline.md` → `./ad-hoc-prompts-extend-the-system-without-schema-changes.md` |
| `one-mechanism` | 38 | off-vocab | `kb/work/revise-autoreason/learning-is-not-only-about-generality.md.20260414-080526/current_a.md` → `./definitions/constraining.md` |
| `foundation` | 27 | adr-only | `kb/work/review-revise-gated/baseline.md` → `./llm-context-is-composed-without-scoping.md` |
| `applies` | 24 | off-vocab | `kb/work/revise-autoreason/system-definition-artifacts-are-crystallized-reasoning-under-context.md.20260418-220035/current_a.md` → `./continual-learning-open-problem-is-behaviour-not-knowledge.md` |
| `operator` | 24 | off-vocab | `kb/work/revise-autoreason/system-definition-artifacts-are-crystallized-reasoning-under-context.md.20260418-220035/current_a.md` → `./definitions/distillation.md` |
| `mechanism` | 18 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `./no-universal-distillation-preserves-all-task-relevant-structure.md` |
| `phase-transition` | 12 | off-vocab | `kb/work/revise-autoreason/system-definition-artifacts-are-crystallized-reasoning-under-context.md.20260418-220035/current_a.md` → `./definitions/codification.md` |
| `special-case` | 5 | off-vocab | `kb/work/review-revise-gated/baseline.md` → `./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md` |
| `tension` | 5 | off-vocab | `kb/work/review-revise-gated/baseline.md` → `./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` |
| `parallel-lower-bound` | 2 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `./exact-retrieval-over-semantically-opaque-items-requires-linear.md` |
| `companion-result` | 1 | off-vocab | `kb/work/agent-complexity-theory/few-calls-require-width-and-long-chains-require-verification.md` → `./adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` |
| `exactness-lower-bound` | 1 | off-vocab | `kb/work/agent-complexity-theory/few-calls-require-width-and-long-chains-require-verification.md` → `./no-universal-distillation-preserves-all-task-relevant-structure.md` |
| `four-layer-proposal` | 1 | off-vocab | `kb/work/agent-memory-design/README.md` → `./explore-layered-architecture.md` |
| `operationalizes` | 1 | off-vocab | `kb/work/harness-taxonomy-convergence/runtime-structure-determines-governance-control-surfaces.md` → `./structure-governance-matrix.md` |
| `setup` | 1 | off-vocab | `kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md` → `./anatomy-of-an-llm-application.md` |
| `target` | 1 | off-vocab | `kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md` → `./llm-frameworks-should-keep-the-tool-loop-optional.md` |

## descriptive → theoretical  (n = 406)

Matrix vocabulary for this edge: `evidence, grounds, rationale`

| Label | Count | Status | Example |
|---|---|---|---|
| `exemplifies` | 97 | adr-only | `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md` → `../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` |
| `contrasts` | 77 | off-vocab | `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md` → `../../notes/automating-kb-learning-is-an-open-problem.md` |
| `<unlabelled>` | 57 | off-vocab | `kb/agent-memory-systems/reviews/arscontexta.md` → `../../notes/title-as-claim-enables-traversal-as-reasoning.md` |
| `extends` | 44 | adr-only | `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md` → `../../notes/link-following-and-search-impose-different-metadata-requirements.md` |
| `sharpens` | 40 | off-vocab | `kb/agent-memory-systems/reviews/Memori.md` → `../../notes/axes-of-substrate-analysis.md` |
| `foundation` | 18 | adr-only | `kb/agent-memory-systems/reviews/auto-harness.md` → `../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md` |
| `grounds` | 18 | adr+matrix | `kb/agent-memory-systems/reviews/CORAL.md` → `../../notes/bounded-context-orchestration-model.md` |
| `complicates` | 11 | off-vocab | `kb/agent-memory-systems/reviews/autocontext.md` → `../../notes/deploy-time-learning-is-the-missing-middle.md` |
| `frames` | 5 | off-vocab | `kb/agent-memory-systems/reviews/browzy-ai.md` → `../../notes/deploy-time-learning-is-the-missing-middle.md` |
| `converges` | 4 | off-vocab | `kb/agent-memory-systems/reviews/claude-context-guard.md` → `../../notes/instruction-specificity-should-match-loading-frequency.md` |
| `parallels` | 4 | off-vocab | `kb/agent-memory-systems/reviews/CORAL.md` → `../../notes/methodology-enforcement-is-constraining.md` |
| `convergence` | 3 | off-vocab | `kb/agent-memory-systems/reviews/archie.md` → `../../notes/files-not-database.md` |
| `warns` | 3 | off-vocab | `kb/agent-memory-systems/reviews/CORAL.md` → `../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` |
| `contradicts` | 2 | adr-only | `kb/agent-memory-systems/reviews/binder.md` → `../../notes/files-not-database.md` |
| `contrast-lens` | 2 | off-vocab | `kb/agent-memory-systems/reviews/playground.md` → `../../notes/files-not-database.md` |
| `enables` | 2 | adr-only | `kb/agent-memory-systems/reviews/siftly.md` → `../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` |
| `example` | 2 | adr-only | `kb/agent-memory-systems/reviews/cludebot.md` → `../../notes/automated-synthesis-is-missing-good-oracles.md` |
| `partially-maps` | 2 | off-vocab | `kb/agent-memory-systems/reviews/openviking.md` → `../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` |
| `tests` | 2 | off-vocab | `kb/agent-memory-systems/reviews/hindsight.md` → `../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md` |
| `aligns` | 1 | off-vocab | `kb/agent-memory-systems/reviews/llm-wiki.md` → `../../notes/files-not-database.md` |
| `analogizes` | 1 | off-vocab | `kb/agent-memory-systems/reviews/skillnote.md` → `../../notes/instruction-specificity-should-match-loading-frequency.md` |
| `analogy` | 1 | off-vocab | `kb/agent-memory-systems/reviews/playground.md` → `../../notes/oracle-strength-spectrum.md` |
| `contextualizes` | 1 | off-vocab | `kb/agent-memory-systems/reviews/skillnote.md` → `../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md` |
| `contrast` | 1 | off-vocab | `kb/agent-memory-systems/source-only/trajectory-informed-memory-generation.md` → `../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `implements` | 1 | off-vocab | `kb/reference/adr/011-notes-must-be-accessible-to-external-readers.md` → `../../notes/COLLECTION.md` |
| `partially-exemplifies` | 1 | off-vocab | `kb/agent-memory-systems/reviews/skillnote.md` → `../../notes/deploy-time-learning-is-the-missing-middle.md` |
| `predicts` | 1 | off-vocab | `kb/agent-memory-systems/reviews/crewai-memory.md` → `../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md` |
| `primary-analysis-note` | 1 | off-vocab | `kb/agent-memory-systems/source-only/agemem.md` → `../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `suggests` | 1 | off-vocab | `kb/agent-memory-systems/reviews/crewai-memory.md` → `../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` |
| `synthesizes` | 1 | off-vocab | `kb/agent-memory-systems/reviews/thalo.md` → `../../notes/underspecification-and-indeterminism-complicate-programming-for.md` |
| `tension` | 1 | off-vocab | `kb/agent-memory-systems/reviews/context-constitution.md` → `../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md` |
| `trades-off-against` | 1 | off-vocab | `kb/agent-memory-systems/reviews/skillnote.md` → `../../notes/files-not-database.md` |

## descriptive → descriptive  (n = 376)

Matrix vocabulary for this edge: `cross-reference, see-also, supersedes`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 128 | off-vocab | `kb/agent-memory-systems/README.md` → `./reviews/ace.md` |
| `extends` | 63 | adr-only | `kb/agent-memory-systems/reviews/CORAL.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `contrasts` | 47 | off-vocab | `kb/agent-memory-systems/reviews/Awesome-Agent-Memory.md` → `../agentic-memory-systems-comparative-review.md` |
| `compares` | 44 | off-vocab | `kb/agent-memory-systems/reviews/CORAL.md` → `./autocontext.md` |
| `sibling` | 24 | off-vocab | `kb/agent-memory-systems/reviews/Zikkaron.md` → `./hindsight.md` |
| `source-inspected-instance` | 20 | off-vocab | `kb/agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md` → `./reviews/napkin.md` |
| `decision` | 18 | off-vocab | `kb/reference/architecture.md` → `./adr/014-scripts-as-python-package-one-tree-model.md` |
| `sharpens` | 5 | off-vocab | `kb/agent-memory-systems/reviews/agent-r.replaced.2026-04-12.md` → `./reflexion.md` |
| `refined` | 3 | off-vocab | `kb/reference/adr/014-scripts-as-python-package-one-tree-model.md` → `./008-stdlib-only-core-scripts.md` |
| `shipped-architecture` | 3 | off-vocab | `kb/reference/control-plane-goals.md` → `./architecture.md` |
| `boundary` | 2 | off-vocab | `kb/agent-memory-systems/reviews/atomic.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `converges` | 2 | off-vocab | `kb/agent-memory-systems/reviews/claude-context-guard.md` → `./agent-skills-for-context-engineering.md` |
| `cross-system-placement` | 2 | off-vocab | `kb/agent-memory-systems/source-only/agemem.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `grounds` | 2 | adr-only | `kb/reference/collections-and-types.md` → `./adr/012-types-for-structure-traits-for-review.md` |
| `axis-placement` | 1 | off-vocab | `kb/agent-memory-systems/reviews/openviking.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `closest-sibling` | 1 | off-vocab | `kb/agent-memory-systems/reviews/synapptic.replaced.2026-04-12.md` → `./pi-self-learning.md` |
| `comparison-frame` | 1 | off-vocab | `kb/agent-memory-systems/reviews/playground.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `enables` | 1 | adr-only | `kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md` → `./007-reports-directory-for-generated-snapshots.md` |
| `foundation` | 1 | adr-only | `kb/reference/adr/013-skills-first-delivery-with-core-local-type-split.md` → `./006-two-tree-installation-layout.md` |
| `frames` | 1 | off-vocab | `kb/agent-memory-systems/reviews/pal.md` → `../trace-derived-learning-techniques-in-related-systems.md` |
| `gap` | 1 | off-vocab | `kb/agent-memory-systems/reviews/thalo.md` → `../../reference/adr/009-link-relationship-semantics.md` |
| `orientation` | 1 | off-vocab | `kb/reference/README.md` → `./collections-and-types.md` |
| `parallel` | 1 | off-vocab | `kb/reference/adr/011-notes-must-be-accessible-to-external-readers.md` → `./009-link-relationship-semantics.md` |
| `parallels` | 1 | off-vocab | `kb/agent-memory-systems/reviews/engraph.md` → `./cocoindex.md` |
| `scenario-derived-architecture` | 1 | off-vocab | `kb/reference/README.md` → `./scenario-architecture.md` |
| `superseded` | 1 | off-vocab | `kb/reference/adr/014-scripts-as-python-package-one-tree-model.md` → `./006-two-tree-installation-layout.md` |
| `superseded-decision` | 1 | off-vocab | `kb/reference/type-loading.md` → `./adr/002-inline-global-types-in-writing-guide.md` |

## managed → managed  (n = 173)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `extends` | 46 | adr-only | `kb/reports/bundle-reviews/review-run-1714/bundle-output.md` → `./underspecification-and-indeterminism-complicate-programming-for.md` |
| `<unlabelled>` | 42 | off-vocab | `kb/reports/connect/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.connect.md` → `../../notes/why-notes-have-types.md` |
| `exemplifies` | 19 | adr-only | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` |
| `foundation` | 15 | adr-only | `kb/reports/reviews/kb__notes__agent-is-a-tool-loop/structural__bullet-capitalization.claude-opus-4-6.md` → `./bounded-context-orchestration-model.md` |
| `sharpens` | 14 | off-vocab | `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/current_a.md` → `./substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md` |
| `validates` | 14 | off-vocab | `kb/reports/revise-autoreason/deploy-time-learning-is-the-missing-middle.md.20260413-195941/current_a.md` → `../sources/context-engineering-ai-agents-oss.ingest.md` |
| `rejected` | 6 | off-vocab | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/related-systems/cludebot.md` |
| `direct-match` | 5 | off-vocab | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` |
| `candidate` | 3 | off-vocab | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `decision` | 2 | off-vocab | `kb/reports/bundle-reviews/review-run-1865/bundle-output.md` → `./adr/006-two-tree-installation-layout.md` |
| `superseded` | 2 | off-vocab | `kb/reports/bundle-reviews/review-run-1854/bundle-output.md` → `./adr/006-two-tree-installation-layout.md` |
| `compares` | 1 | off-vocab | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/related-systems/xMemory.md` |
| `context` | 1 | off-vocab | `kb/reports/reviews/kb__notes__agent-is-a-tool-loop/structural__bullet-capitalization.claude-opus-4-6.md` → `./tool-loop-index.md` |
| `contrasts` | 1 | off-vocab | `kb/reports/connect/notes/databricks-memory-scaling-ai-agents.connect.md` → `../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `direct-conceptual-match` | 1 | off-vocab | `kb/reports/connect/notes/scaling-managed-agents-decoupling-brain-from-hands.connect.md` → `../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` |
| `grounds` | 1 | adr-only | `kb/reports/connect/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.connect.md` → `../../notes/learning-is-not-only-about-generality.md` |

## source → theoretical  (n = 166)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `exemplifies` | 57 | adr-only | `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` → `../notes/oracle-strength-spectrum.md` |
| `<unlabelled>` | 27 | off-vocab | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `../notes/learning-theory-index.md` |
| `grounds` | 23 | adr-only | `kb/sources/adam-mastroianni-infinite-midwit.ingest.md` → `../notes/the-boundary-of-automation-is-the-boundary-of-verification.md` |
| `extends` | 19 | adr-only | `kb/sources/adam-mastroianni-infinite-midwit.ingest.md` → `../notes/automated-synthesis-is-missing-good-oracles.md` |
| `reference-material` | 6 | off-vocab | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `../notes/tags-index.md` |
| `validates` | 6 | off-vocab | `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` → `../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md` |
| `contradicts` | 5 | adr-only | `kb/sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md` → `../notes/constraining-during-deployment-is-continuous-learning.md` |
| `contrasts` | 5 | off-vocab | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |
| `enables` | 4 | adr-only | `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` → `../notes/spec-mining-as-codification.md` |
| `complements` | 3 | off-vocab | `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` → `../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` |
| `extends-by-analogy` | 3 | off-vocab | `kb/sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md` → `../notes/structure-activates-higher-quality-training-distributions.md` |
| `applies` | 1 | off-vocab | `kb/sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` → `../notes/definitions/distillation.md` |
| `challenges` | 1 | off-vocab | `kb/sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` → `../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` |
| `complements-methodology` | 1 | off-vocab | `kb/sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md` → `../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md` |
| `formalizes` | 1 | off-vocab | `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` → `../notes/methodology-enforcement-is-constraining.md` |
| `foundation` | 1 | adr-only | `kb/sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` → `../notes/learning-is-not-only-about-generality.md` |
| `parallels` | 1 | off-vocab | `kb/sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md` → `../notes/definitions/constraining.md` |
| `refines` | 1 | off-vocab | `kb/sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md` → `../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md` |
| `source` | 1 | off-vocab | `kb/sources/purdue-owl-toulmin-argument.ingest.md` → `../notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md` |

## theoretical → source  (n = 141)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `exemplifies` | 25 | adr-only | `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` → `../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md` |
| `<unlabelled>` | 22 | off-vocab | `kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md` → `../sources/induction-bias-sequence-models-ebrahimi-2026.md` |
| `evidence` | 20 | off-vocab | `kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md` → `../sources/multi-agent-memory-computer-architecture-perspective.ingest.md` |
| `grounds` | 17 | adr-only | `kb/notes/agentic-systems-interpret-underspecified-instructions.md` → `../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` |
| `source` | 12 | off-vocab | `kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` → `../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy.ingest.md` |
| `extends` | 11 | adr-only | `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md` → `../sources/slate-moving-beyond-react-and-rlm.ingest.md` |
| `validates` | 6 | off-vocab | `kb/notes/agents-md-should-be-organized-as-a-control-plane.md` → `../sources/context-engineering-ai-agents-oss.ingest.md` |
| `primary-evidence` | 3 | off-vocab | `kb/notes/entropy-management-must-scale-with-generation-throughput.md` → `../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md` |
| `context` | 2 | off-vocab | `kb/notes/elicitation-requires-maintained-question-generation-systems.md` → `../sources/towards-a-science-of-ai-agent-reliability.md` |
| `academic-paper` | 1 | off-vocab | `kb/notes/learning-theory-index.md` → `../sources/a-mem-agentic-memory-for-llm-agents.md` |
| `complement` | 1 | off-vocab | `kb/notes/elicitation-requires-maintained-question-generation-systems.md` → `../sources/professional-software-developers-dont-vibe-they-control.md` |
| `complements` | 1 | off-vocab | `kb/notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md` → `../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` |
| `contradicts` | 1 | adr-only | `kb/notes/files-not-database.md` → `../sources/graphiti-temporal-knowledge-graph.ingest.md` |
| `contradicts-source` | 1 | off-vocab | `kb/notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md` → `../sources/the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of.ingest.md` |
| `counterexample` | 1 | off-vocab | `kb/notes/skills-derive-from-methodology-through-distillation.md` → `../sources/skill-synthesis-materializing-knowledge-as-skills-2032179291031.ingest.md` |
| `empirical-counterpoint` | 1 | off-vocab | `kb/notes/links-index.md` → `../sources/a-mem-agentic-memory-for-llm-agents.md` |
| `empirical-evidence` | 1 | off-vocab | `kb/notes/llm-interpretation-errors-index.md` → `../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md` |
| `enables` | 1 | adr-only | `kb/notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md` → `../sources/purdue-owl-toulmin-argument.md` |
| `example` | 1 | adr-only | `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` → `../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md` |
| `formalizes` | 1 | off-vocab | `kb/notes/methodology-enforcement-is-constraining.md` → `../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` |
| `origin` | 1 | off-vocab | `kb/notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` → `../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology.ingest.md` |
| `practitioner-evidence` | 1 | off-vocab | `kb/notes/knowledge-storage-does-not-imply-contextual-activation.md` → `../sources/the-second-brain-trap-2041486539067154753.ingest.md` |
| `practitioner-validation` | 1 | off-vocab | `kb/notes/links-index.md` → `../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md` |
| `provides-framework` | 1 | off-vocab | `kb/notes/enforcement-without-structured-recovery-is-incomplete.md` → `../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md` |
| `refines` | 1 | off-vocab | `kb/notes/operational-signals-that-a-component-is-a-relaxing-candidate.md` → `../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md` |
| `related-formalization` | 1 | off-vocab | `kb/notes/information-value-is-observer-relative.md` → `../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md` |
| `responds-to` | 1 | off-vocab | `kb/notes/in-context-learning-presupposes-context-engineering.md` → `../sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md` |
| `sharpens-scope` | 1 | off-vocab | `kb/notes/vibe-noting.md` → `../sources/the-flawed-ephemeral-software-hypothesis.ingest.md` |
| `sibling` | 1 | off-vocab | `kb/notes/deploy-time-learning-is-the-missing-middle.md` → `../sources/the-flawed-ephemeral-software-hypothesis.ingest.md` |
| `validates-from-inside` | 1 | off-vocab | `kb/notes/title-as-claim-enables-traversal-as-reasoning.md` → `../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md` |
| `validates-goodhart-risk` | 1 | off-vocab | `kb/notes/quality-signals-for-kb-evaluation.md` → `../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md` |
| `warning-case` | 1 | off-vocab | `kb/notes/definitions/distillation.md` → `../../sources/large-language-model-agents-are-not-always-faithful-self.ingest.md` |

## managed → theoretical  (n = 123)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 85 | off-vocab | `kb/reports/connect/reference/available-types.connect.md` → `../../../notes/why-notes-have-types.md` |
| `extends` | 13 | adr-only | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../notes/synthesis-is-not-error-correction.md` |
| `evidence` | 7 | off-vocab | `kb/reports/connect/sources/everything-you-need-to-know-about-llm-memory.connect.md` → `../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` |
| `grounds` | 7 | adr-only | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` |
| `exemplifies` | 6 | adr-only | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md` |
| `contrasts` | 2 | off-vocab | `kb/reports/connect/sources/into-the-unknown-self-learning-large-language-models.connect.md` → `../../../notes/treat-continual-learning-as-substrate-coevolution.md` |
| `qualifies` | 2 | off-vocab | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md` |
| `parallels` | 1 | off-vocab | `kb/reports/connect/sources/into-the-unknown-self-learning-large-language-models.connect.md` → `../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md` |

## workshop → theoretical  (n = 95)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 49 | off-vocab | `kb/work/agent-memory-design/README.md` → `../../notes/knowledge-storage-does-not-imply-contextual-activation.md` |
| `extends` | 8 | adr-only | `kb/work/agent-complexity-theory/few-calls-require-width-and-long-chains-require-verification.md` → `../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` |
| `consequence` | 7 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `../../notes/decomposition-heuristics-for-bounded-context-scheduling.md` |
| `foundation` | 6 | adr-only | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `../../notes/bounded-context-orchestration-model.md` |
| `mechanism` | 4 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `../../notes/llm-context-is-composed-without-scoping.md` |
| `grounds` | 3 | adr-only | `kb/work/harness-taxonomy-convergence/runtime-structure-determines-governance-control-surfaces.md` → `../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md` |
| `boundary` | 2 | off-vocab | `kb/work/agent-complexity-theory/exact-retrieval-over-semantically-opaque-items-requires-linear.md` → `../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md` |
| `clarifies` | 2 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `../../notes/effective-context-is-task-relative-and-complexity-relative-not-a.md` |
| `exemplifies` | 2 | adr-only | `kb/work/harness-taxonomy-convergence/runtime-structure-determines-governance-control-surfaces.md` → `../../notes/semantic-review-catches-content-errors-that-structural-validation.md` |
| `instance` | 2 | off-vocab | `kb/work/agent-complexity-theory/exact-retrieval-over-semantically-opaque-items-requires-linear.md` → `../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` |
| `scope` | 2 | off-vocab | `kb/work/agent-complexity-theory/adaptive-dependencies-force-width-reopening-or-sequential-rounds.md` → `../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md` |
| `background` | 1 | off-vocab | `kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md` → `../../notes/bounded-context-orchestration-model.md` |
| `context` | 1 | off-vocab | `kb/work/agent-complexity-theory/no-universal-distillation-preserves-all-task-relevant-structure.md` → `../../notes/bounded-context-orchestration-model.md` |
| `contrasts` | 1 | off-vocab | `kb/work/tool-loop-control/anatomy-of-an-llm-application.md` → `../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` |
| `framework-comparison` | 1 | off-vocab | `kb/work/paper-bounded-context-orchestration/outline-v2.md` → `../../notes/tool-loop-index.md` |
| `next-step` | 1 | off-vocab | `kb/work/tool-loop-control/a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md` → `../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` |
| `prior-framing` | 1 | off-vocab | `kb/work/tool-loop-control/llm-frameworks-should-keep-the-tool-loop-optional.md` → `../../notes/tool-loop-index.md` |
| `protocol-boundary` | 1 | off-vocab | `kb/work/paper-bounded-context-orchestration/outline-v2.md` → `../../notes/session-history-should-not-be-the-default-next-context.md` |
| `strongest-local-analogue` | 1 | off-vocab | `kb/work/philosophy-borrowing/speech-acts.md` → `../../notes/instructions-are-typed-callables.md` |

## theoretical → descriptive  (n = 66)

Matrix vocabulary for this edge: `derived-from, evidence, exemplifies`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 21 | off-vocab | `kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` → `../reference/available-types.md` |
| `current-state` | 11 | off-vocab | `kb/notes/architecture-index.md` → `../reference/control-plane-goals.md` |
| `evidence` | 5 | matrix-only | `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md` → `../agent-memory-systems/agentic-memory-systems-comparative-review.md` |
| `exemplifies` | 4 | adr+matrix | `kb/notes/agent-orchestration-needs-coordination-guarantees-not-just.md` → `../agent-memory-systems/reviews/tracecraft.md` |
| `grounds` | 4 | adr-only | `kb/notes/axes-of-substrate-analysis.md` → `../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md` |
| `contrasts` | 3 | off-vocab | `kb/notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable.md` → `../agent-memory-systems/reviews/sift-kg.md` |
| `extends` | 3 | adr-only | `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md` → `../reference/available-types.md` |
| `example` | 2 | adr-only | `kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` → `../agent-memory-systems/reviews/autocontext.md` |
| `implication` | 2 | off-vocab | `kb/notes/claw-learning-is-broader-than-retrieval.md` → `../reference/available-types.md` |
| `converges` | 1 | off-vocab | `kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured.md` → `../agent-memory-systems/thalo-type-comparison.md` |
| `counterexample` | 1 | off-vocab | `kb/notes/axes-of-substrate-analysis.md` → `../agent-memory-systems/reviews/cognee.md` |
| `decision` | 1 | off-vocab | `kb/notes/linking-theory.md` → `../reference/adr/009-link-relationship-semantics.md` |
| `enables` | 1 | adr-only | `kb/notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md` → `../../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md` |
| `production-evidence` | 1 | off-vocab | `kb/notes/definitions/distillation.md` → `../../agent-memory-systems/reviews/getsentry-skills.md` |
| `refines` | 1 | off-vocab | `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` → `../agent-memory-systems/reviews/arscontexta.md` |
| `sharpens` | 1 | off-vocab | `kb/notes/automating-kb-learning-is-an-open-problem.md` → `../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md` |
| `source` | 1 | off-vocab | `kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md` → `../agent-memory-systems/reviews/arscontexta.md` |
| `taxonomy` | 1 | off-vocab | `kb/notes/type-system-index.md` → `../reference/available-types.md` |
| `tests` | 1 | off-vocab | `kb/notes/files-not-database.md` → `../agent-memory-systems/reviews/tracecraft.md` |
| `validates` | 1 | off-vocab | `kb/notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md` → `../agent-memory-systems/agentic-memory-systems-comparative-review.md` |

## descriptive → source  (n = 29)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `evidence` | 8 | off-vocab | `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md` → `../../sources/large-language-model-agents-are-not-always-faithful-self.ingest.md` |
| `<unlabelled>` | 6 | off-vocab | `kb/agent-memory-systems/README.md` → `../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md` |
| `compares` | 5 | off-vocab | `kb/agent-memory-systems/reviews/Memori.md` → `../../sources/mem0-memory-layer.ingest.md` |
| `contrasts` | 4 | off-vocab | `kb/agent-memory-systems/reviews/expel.md` → `../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md` |
| `grounds` | 4 | adr-only | `kb/agent-memory-systems/reviews/context-constitution.md` → `../../sources/continual-learning-in-token-space.ingest.md` |
| `source-coverage` | 2 | off-vocab | `kb/agent-memory-systems/source-only/agemem.md` → `../../sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` |

## source → source  (n = 25)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 7 | off-vocab | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `./agentic-note-taking-23-notes-without-reasons-202689418851669643.ingest.md` |
| `contrasts` | 4 | off-vocab | `kb/sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md` → `./a-mem-agentic-memory-for-llm-agents.ingest.md` |
| `complements` | 3 | off-vocab | `kb/sources/convexbench-can-llms-recognize-convex-functions.ingest.md` → `meyerson-maker-million-step-llm-zero-errors.ingest.md` |
| `extends` | 3 | adr-only | `kb/sources/adam-mastroianni-infinite-midwit.ingest.md` → `./when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md` |
| `contradicts` | 1 | adr-only | `kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651.ingest.md` → `./the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of.ingest.md` |
| `converges` | 1 | off-vocab | `kb/sources/paulsen-maximum-effective-context-window-mecw.ingest.md` → `convexbench-can-llms-recognize-convex-functions.ingest.md` |
| `different-agency-models` | 1 | off-vocab | `kb/sources/cognee-knowledge-engine.ingest.md` → `letta-memgpt-stateful-agents.md` |
| `opposite-agency-models` | 1 | off-vocab | `kb/sources/mem0-memory-layer.ingest.md` → `letta-memgpt-stateful-agents.md` |
| `opposite-memory-units` | 1 | off-vocab | `kb/sources/cognee-knowledge-engine.ingest.md` → `mem0-memory-layer.md` |
| `opposite-schema-philosophies` | 1 | off-vocab | `kb/sources/cognee-knowledge-engine.ingest.md` → `a-mem-agentic-memory-for-llm-agents.md` |
| `sibling` | 1 | off-vocab | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `./agentic-memory-learning-unified-long-term-and-short-term.ingest.md` |
| `synthesizes` | 1 | off-vocab | `kb/sources/convexbench-can-llms-recognize-convex-functions.ingest.md` → `agentic-code-reasoning.ingest.md` |

## managed → descriptive  (n = 22)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 16 | off-vocab | `kb/reports/connect/reference/available-types.connect.md` → `../../../reference/type-loading.md` |
| `cross-reference` | 3 | off-vocab | `kb/reports/connect/reference/available-types.connect.md` → `../../../reference/architecture.md` |
| `extends` | 2 | adr-only | `kb/reports/connect/sources/everything-you-need-to-know-about-llm-memory.connect.md` → `../../../agent-memory-systems/agentic-memory-systems-comparative-review.md` |
| `evidence` | 1 | off-vocab | `kb/reports/connect/sources/externalization-in-llm-agents-unified-review.connect.md` → `../../../agent-memory-systems/agentic-memory-systems-comparative-review.md` |

## managed → source  (n = 11)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 7 | off-vocab | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric.ingest.md` |
| `contrasts` | 1 | off-vocab | `kb/reports/connect/sources/into-the-unknown-self-learning-large-language-models.connect.md` → `../../../sources/continual-learning-in-token-space.md` |
| `cross-reference` | 1 | off-vocab | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md` |
| `extends` | 1 | adr-only | `kb/reports/connect/sources/everything-you-need-to-know-about-llm-memory.connect.md` → `../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.report-automation-quality.md` |
| `source-to-source-connection` | 1 | off-vocab | `kb/reports/connect/sources/autoreason-self-refinement-that-knows-when-to-stop.connect.md` → `../../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md` |

## workshop → descriptive  (n = 11)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 10 | off-vocab | `kb/work/agent-memory-design/README.md` → `../../agent-memory-systems/agentic-memory-systems-comparative-review.md` |
| `five-labels` | 1 | off-vocab | `kb/work/link-label-audit/framing.md` → `../../reference/adr/009-link-relationship-semantics.md` |

## theoretical → schema  (n = 5)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 5 | off-vocab | `kb/notes/document-system-index.md` → `../types/note.md` |

## schema → schema  (n = 5)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 5 | off-vocab | `kb/types/definition.template.md` → `./related-note.md` |

## theoretical → workshop  (n = 4)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/notes/learning-theory-index.md` → `../work/information-measures/epiplexity-eli5.md` |
| `develops` | 1 | off-vocab | `kb/notes/bounded-context-orchestration-model.md` → `../work/paper-bounded-context-orchestration/outline-v2.md` |
| `examples` | 1 | off-vocab | `kb/notes/information-value-is-observer-relative.md` → `../work/information-measures/epiplexity-eli5.md` |
| `worked-example` | 1 | off-vocab | `kb/notes/prompt-ablation-converts-human-insight-to-deployable-framing.md` → `../work/curiosity-prompts/experiment-report.md` |

## descriptive → prescriptive  (n = 4)

Matrix vocabulary for this edge: `procedure`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 2 | off-vocab | `kb/reference/README.md` → `../instructions/REVIEW-SYSTEM.md` |
| `implements` | 2 | off-vocab | `kb/reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md` → `../../instructions/REVIEW-SYSTEM.md` |

## source → descriptive  (n = 4)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `extends` | 2 | adr-only | `kb/sources/multi-agent-memory-computer-architecture-perspective.ingest.md` → `../agent-memory-systems/agentic-memory-systems-comparative-review.md` |
| `grounds` | 2 | adr-only | `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md` → `../agent-memory-systems/agentic-memory-systems-comparative-review.md` |

## workshop → source  (n = 4)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 3 | off-vocab | `kb/work/paper-bounded-context-orchestration/outline-v2.md` → `../../sources/convexbench-can-llms-recognize-convex-functions.md` |
| `source` | 1 | off-vocab | `kb/work/information-measures/epiplexity-eli5.md` → `../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md` |

## workshop → prescriptive  (n = 4)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 4 | off-vocab | `kb/work/review-run-lifecycle/README.md` → `../../instructions/REVIEW-SYSTEM.md` |

## other → theoretical  (n = 2)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 2 | off-vocab | `kb/index.md` → `./notes/tags-index.md` |

## theoretical → prescriptive  (n = 2)

Matrix vocabulary for this edge: `evidence`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 2 | off-vocab | `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md` → `../instructions/connect/SKILL.md` |

## descriptive → schema  (n = 2)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 2 | off-vocab | `kb/reference/available-types.md` → `../types/note.md` |

## other → workshop  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/index.md` → `./work/README.md` |

## prescriptive → prescriptive  (n = 1)

Matrix vocabulary for this edge: `composition`

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/instructions/cp-skill-write/SKILL.md` → `./related-note.md` |

## theoretical → other  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md` → `../tasks/recurring/review-explanatory-reach.md` |

## schema → external  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/types/index.template.md` → `../../reference/adr/decision.md` |

## schema → descriptive  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `taxonomy-overview` | 1 | off-vocab | `kb/types/note.md` → `../reference/available-types.md` |

## schema → theoretical  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/types/note.md` → `../notes/document-types-should-be-verifiable.md` |

## workshop → other  (n = 1)

_No declared matrix vocabulary for this edge._

| Label | Count | Status | Example |
|---|---|---|---|
| `<unlabelled>` | 1 | off-vocab | `kb/work/system-documentation/framing.md` → `../../CLAUDE.md` |
