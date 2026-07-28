# Rationale label direction review

**Status:** completed semantic review; no catalogue, contract, ADR, instruction, or corpus edge was changed.

**Date:** 2026-07-28

## Decision summary

The result is **split or reclassify**, not a bulk migration.

`rests-on` earns a distinct successor for the 114 active `rationale` edges classified **R — rationale dependency**. Their honest assertion is:

> The source design, description, procedure, rule, or system-definition artifact `rests-on` the target theoretical claim.

The label is asymmetric and source-to-target. It answers the cross-register reader question, “why does this design, rule, or description exist?”

Two `rationale` edges are actually **E — evidence** and should be considered with `is-evidence-for`; 18 are **N — navigation or another relation**, mostly reference-to-reference architecture/history edges. They must not be renamed to `rests-on` by default. No rationale edge required an A disposition after the local source, target, and context were read.

`grounds` remains a separate candidate relation for the theoretical note-to-note cohort: the source is an assertion and the target is a premise a reader follows to assess. The 38 off-pattern `grounds` edges are classification or authorization debt, not evidence that the two labels should be merged. Two files use both labels without a stable semantic contrast, which is evidence of drift at the boundary, not a reason to erase the distinction established by the recurring cohorts.

This review therefore recommends a later scoped migration of R edges to `rests-on`, preceded by explicit reclassification decisions for the E and N edges and by cleanup of off-pattern `grounds`. It does not authorize that migration.

## Governing test and method

I read [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md), [ADR 020](../../reference/adr/020-theoretical-default-contrasts-mechanism.md), [ADR 019](../../reference/adr/019-collection-owned-link-vocabulary.md), the [link vocabulary](../../reference/link-vocabulary.md), every live collection contract that names `rationale` or `grounds`, the evidence retrospective, and the rationale migration plan.

The positive mutable surface is every active registered footer edge in non-generated Markdown under `kb/notes/`, `kb/reference/` (excluding `proposals/archive/`), `kb/instructions/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/` analyses/ingests, and `kb/types/`. `kb/types/` was included to expose system-definition edges even though it has no collection-local `COLLECTION.md`.

The temporary corpus was `/tmp/rationale-grounds.tsv`. It has one row per matched `rationale` or `grounds` footer and the fields `label`, `source_path`, `source_collection`, `target_as_authored`, `resolved_target`, `destination_class`, `link_title`, `context_phrase`, `exclusion_bucket`, `semantic_disposition`, and `line`. The scan accepts both ordinary and bold footer links and resolves relative targets before classification.

### Inventory and exclusions

| label | all registered rows | active mutable | generated reports | archived proposals | inactive workshop history |
|---|---:|---:|---:|---:|---:|
| `rationale` | 189 | 134 | 43 | 9 | 3 |
| `grounds` | 2,106 | 310 | 1,617 | 1 | 178 |

No immutable source snapshot or separately classified frozen experiment/calibration artifact contributed an active row. Historical quotations and ordinary prose mentions were not registered edges and were retained as evidence rather than counted as migration candidates. Generated reports, archived proposals, and all workshop history were excluded from the mutable surface.

### Active source-to-destination inventory

| label | source → destination | edges | source files | contract status |
|---|---|---:|---:|---|
| `rationale` | reference → notes | 95 | 36 | authorized by `kb/reference/COLLECTION.md` |
| `rationale` | reference → reference | 16 | 8 | authorization gap |
| `rationale` | agentic-systems → notes | 9 | 3 | authorized |
| `rationale` | agent-memory-systems → notes | 5 | 4 | authorized |
| `rationale` | instructions → notes | 5 | 4 | authorized |
| `rationale` | notes → reference | 2 | 2 | authorization gap |
| `rationale` | sources → notes | 1 | 1 | authorized |
| `rationale` | types → notes | 1 | 1 | no collection contract |
| `grounds` | notes → notes | 272 | 135 | authorized by `kb/notes/COLLECTION.md` |
| `grounds` | notes → external | 15 | 13 | authorization gap |
| `grounds` | sources → notes | 9 | 7 | authorization gap; source contract names other labels |
| `grounds` | reference → notes | 6 | 6 | authorization gap |
| `grounds` | notes → reference | 2 | 2 | authorization gap |
| `grounds` | types → notes | 2 | 1 | no collection contract |
| `grounds` | agent-memory-systems → external | 1 | 1 | authorization gap |
| `grounds` | notes → agent-memory | 1 | 1 | authorization gap |
| `grounds` | reference → reference | 1 | 1 | authorization gap |
| `grounds` | sources → agent-memory | 1 | 1 | authorization gap |

The authorization result is separate from semantic classification. A valid reader relationship can still be off-contract; an authorized label can still be semantically misapplied.

## Rationale disposition ledger

The following ledger reconciles all 134 active `rationale` edges. Multiple edges on one source line are separated by semicolons. `R` means `rests-on` is the honest successor candidate; `E` means evidence; `N` means navigation, architecture/history, or another relation.

| source | resolved edge(s) at source line | disposition |
|---|---|---|
| `kb/agent-memory-systems/lightweight/fintool.md` | 74 → `notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md` | R |
| `kb/agent-memory-systems/lightweight/incremental-self-improvement.md` | 86 → `notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md`; 87 → `notes/oracle-strength-spectrum.md` | R |
| `kb/agent-memory-systems/review-framework-design.md` | 88 → `notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md` | R |
| `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md` | 768 → `notes/designing-agent-memory-systems.md` | R |
| `kb/agentic-systems/claude-code-dynamic-workflows.md` | 69 → `notes/the-practical-scheduler-is-the-host-language.md` | R |
| `kb/agentic-systems/claude-code-dynamic-workflows.md` | 70 → `notes/llm-frameworks-should-keep-the-tool-loop-optional.md` | E |
| `kb/agentic-systems/exo.md` | 94 → `notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md`; 95 → `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`; 96 → `notes/warranted-autonomy-is-bounded-by-oracle-domain.md`; 97 → `notes/definitions/reflective-system.md`; 98 → `notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md` | R |
| `kb/agentic-systems/gbrain.md` | 53 → `notes/the-practical-scheduler-is-the-host-language.md`; 54 → `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md` | R |
| `kb/instructions/composition-friction-gate.md` | 56 → `notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`; 57 → `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` | R |
| `kb/instructions/critique-note.md` | 48 → `notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md` | R |
| `kb/instructions/retire-artifact.md` | 139 → `notes/stale-indexes-are-worse-than-no-indexes.md` | R |
| `kb/instructions/review-gates/semantic/unearned-generality.md` | 53 → `notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md` | R |
| `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md` | 99 → `reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md` | N |
| `kb/notes/definitions/text-contract.md` | 57 → `reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md` | N |
| `kb/reference/adr/025-complete-generated-indexes-are-build-time-only.md` | 66 → `notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`; 67 → `notes/two-context-boundaries-govern-collection-operations.md`; 68 → `notes/feasibility-is-the-heaviest-forks-net-load.md`; 69 → `notes/index-curation-adds-orientation-that-generation-cannot-produce.md` | R |
| `kb/reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md` | 67 → `notes/stale-indexes-are-worse-than-no-indexes.md`; 68 → `notes/design-for-the-first-time-human-except-on-access-cost.md`; 69 → `notes/index-curation-adds-orientation-that-generation-cannot-produce.md`; 70 → `notes/frontloading-spares-execution-context.md`; 71 → `notes/feasibility-is-the-heaviest-forks-net-load.md` | R |
| `kb/reference/adr/028-design-proposals-live-in-reference-proposals.md` | 43 → `notes/design-proposals-differ-from-claims-in-kind-not-confidence.md` | R |
| `kb/reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md` | 56 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; 57 → `notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md` | R |
| `kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md` | 47 → `notes/progressive-constraining-commits-only-after-patterns-stabilize.md` | R |
| `kb/reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md` | 56 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |
| `kb/reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md` | 74 → `notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md` | R |
| `kb/reference/adr/044-user-verification-replaces-global-note-status.md` | 61 → `notes/definitions/representational-form.md` | R |
| `kb/reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md` | 53 → `reference/collections-never-own-frontmatter-semantics.md` | N |
| `kb/reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md` | 69 → `notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md`; 70 → `notes/knowledge-storage-does-not-imply-contextual-activation.md`; 71 → `notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md` | R |
| `kb/reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md` | 70 → `notes/document-types-should-be-verifiable.md` | R |
| `kb/reference/adr/058-directional-identifiers-use-source-as-subject.md` | 57 → `reference/adr/019-collection-owned-link-vocabulary.md` | N |
| `kb/reference/adr/058-directional-identifiers-use-source-as-subject.md` | 60 → `notes/links-encode-conditional-possibilities-not-obligations.md` | R |
| `kb/reference/agent-memory-coverage.md` | 56 → `notes/designing-agent-memory-systems.md` | R |
| `kb/reference/collections-and-types.md` | 87 → `reference/adr/012-types-for-structure-traits-for-review.md`; 88 → `reference/adr/017-collection-md-is-the-register-convention-boundary.md`; 89 → `reference/adr/019-collection-owned-link-vocabulary.md`; 90 → `reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md`; 91 → `reference/adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md` | N |
| `kb/reference/commonplace-agent-memory-gap-plan.md` | 125 → `notes/designing-agent-memory-systems.md` | R |
| `kb/reference/commonplace-as-a-reflective-system.md` | 63 → `notes/methodological-and-computational-closure-track-different-changes.md`; 64 → `notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md`; 65 → `notes/reflective-coverage-is-graded-across-representational-forms.md`; 66 → `notes/warranted-autonomy-is-bounded-by-oracle-domain.md`; 67 → `notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md`; 68 → `notes/stale-indexes-are-worse-than-no-indexes.md` | R |
| `kb/reference/commonplace-as-an-instrument.md` | 64 → `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md`; 65 → `notes/provenance-warrants-a-decompositions-scope-claim-use-earns-it.md`; 66 → `notes/self-improvement-is-relative-to-a-declared-objective.md`; 67 → `notes/increasing-computational-autonomy-relocates-human-effort.md`; 68 → `notes/history-has-one-chance-to-become-checkable.md`; 69 → `notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` | R |
| `kb/reference/commonplace-declared-frame.md` | 33 → `notes/methodological-and-computational-closure-track-different-changes.md` | R |
| `kb/reference/design-rationale-management.md` | 59 → `notes/design-proposals-differ-from-claims-in-kind-not-confidence.md`; 60 → `notes/first-principles-reasoning-selects-for-explanatory-reach-over.md`; 61 → `notes/progressive-constraining-commits-only-after-patterns-stabilize.md`; 62 → `notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` | R |
| `kb/reference/link-vocabulary.md` | 186 → `reference/adr/019-collection-owned-link-vocabulary.md`; 187 → `reference/adr/059-external-is-a-reserved-outbound-destination.md`; 188 → `reference/adr/009-link-relationship-semantics.md`; 189 → `reference/adr/020-theoretical-default-contrasts-mechanism.md`; 190 → `reference/adr/058-directional-identifiers-use-source-as-subject.md` | N |
| `kb/reference/link-vocabulary.md` | 191 → `notes/links-encode-conditional-possibilities-not-obligations.md`; 192 → `notes/theory-and-methodology-form-a-two-layer-execution-system.md`; 193 → `notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` | R |
| `kb/reference/proposals/a-reader-facing-banner-for-user-verification.md` | 81 → `notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md`; 82 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |
| `kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md` | 73 → `notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md`; 74 → `notes/theory-and-methodology-form-a-two-layer-execution-system.md`; 75 → `notes/evolving-understanding-needs-holistic-rewrite-not-composition.md`; 76 → `notes/an-accepted-edit-verifies-the-change-not-the-rule.md`; 77 → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`; 78 → `notes/llm-generation-relaxes-goals-where-human-writing-stalls.md`; 79 → `notes/the-boundary-of-automation-is-the-boundary-of-verification.md` | R |
| `kb/reference/proposals/backlink-surfacing.md` | 39 → `notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md` | R |
| `kb/reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md` | 97 → `notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md`; 98 → `notes/evaluation-automation-is-phase-gated-by-comprehension.md`; 99 → `notes/an-accepted-edit-verifies-the-change-not-the-rule.md`; 100 → `notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md`; 101 → `notes/reasoning-production-is-not-reasoning-evaluation.md`; 102 → `notes/oracle-strength-spectrum.md` | R |
| `kb/reference/proposals/channel-compiled-instruction-artifacts.md` | 89 → `notes/generate-instructions-at-build-time.md`; 90 → `notes/frontloading-spares-execution-context.md`; 91 → `notes/indirection-is-costly-in-llm-instructions.md`; 92 → `notes/definitions/operative-change.md`; 93 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |
| `kb/reference/proposals/checked-inline-blocks-for-shared-instruction-text.md` | 108 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; 109 → `notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md`; 110 → `notes/frontloading-spares-execution-context.md`; 111 → `notes/indirection-is-costly-in-llm-instructions.md` | R |
| `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md` | 58 → `reference/adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md` | N |
| `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md` | 57 → `notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md`; 59 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |
| `kb/reference/proposals/gate-learning-from-accepted-edits.md` | 72 → `notes/an-accepted-edit-verifies-the-change-not-the-rule.md`; 73 → `notes/spec-mining-as-codification.md`; 74 → `notes/instruction-specificity-should-match-loading-frequency.md`; 75 → `notes/methodology-enforcement-is-constraining.md`; 77 → `notes/llm-generation-relaxes-goals-where-human-writing-stalls.md` | R |
| `kb/reference/proposals/generalized-validation-invalidation-and-imperative-extension.md` | 83 → `reference/collections-never-own-frontmatter-semantics.md` | N |
| `kb/reference/proposals/generalized-validation-invalidation-and-imperative-extension.md` | 79 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; 84 → `notes/first-principles-are-inherited-constraints-not-design-choices.md` | R |
| `kb/reference/proposals/periodic-connect-report-mining.md` | 52 → `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md` | R |
| `kb/reference/proposals/tag-scope-is-declared-where-membership-claims-are-made.md` | 61 → `notes/stale-indexes-are-worse-than-no-indexes.md`; 62 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`; 63 → `notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md` | R |
| `kb/reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md` | 99 → `notes/reasoning-production-is-not-reasoning-evaluation.md`; 100 → `notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md` | R |
| `kb/reference/proposals/where-subtree-scoped-write-time-contracts-live.md` | 75 → `notes/why-directories-despite-their-costs.md`; 76 → `notes/methodology-enforcement-is-constraining.md` | R |
| `kb/reference/proposals/write-time-vocabulary-collision-controls.md` | 51 → `notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md`; 52 → `notes/frontloading-spares-execution-context.md` | R |
| `kb/reference/tag-readme-trace-as-self-improving-loop.md` | 37 → `notes/definitions/self-improving-system.md`; 38 → `notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`; 39 → `notes/warranted-autonomy-is-bounded-by-oracle-domain.md`; 40 → `notes/stale-indexes-are-worse-than-no-indexes.md` | R |
| `kb/reference/tag-readme-trace-observed-causal-connection.md` | 49 → `notes/definitions/reflective-system.md`; 51 → `notes/stale-indexes-are-worse-than-no-indexes.md` | R |
| `kb/reference/text-contract-profiles.md` | 106 → `reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md` | N |
| `kb/reference/types/adr.md` | 69 → `reference/where-change-candidates-come-from-in-commonplace.md` | N |
| `kb/reference/types/adr.md` | 68 → `notes/definitions/operative-change.md` | R |
| `kb/reference/validation-contract.md` | 83 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |
| `kb/sources/goedel-machines-schmidhuber.ingest.md` | 134 → `notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md` | E |
| `kb/types/type-spec.md` | 71 → `notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` | R |

The ledger counts are R=114, E=2, N=18. The two E cases are not ambiguous after reading their context: the Claude Code analysis says it “feeds back as evidence” (`kb/agentic-systems/claude-code-dynamic-workflows.md:70`), and the Gödel Machines ingest records an “existence proof” (`kb/sources/goedel-machines-schmidhuber.ingest.md:134`).

## Grounds comparison

### Intended note-to-note cohort

The 272 note-to-note edges repeatedly express a source assertion whose target is the premise, definition, mechanism, dependency, or argumentative basis a reader should inspect. Samples:

| cohort | sample | what the edge asks the reader to do |
|---|---|---|
| definition / membership | `kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md:97` → `definitions/self-improving-system.md` | check the target definition's membership condition |
| mechanism | `kb/notes/an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md:39` → `first-principles-reasoning-selects-for-explanatory-reach-over.md` | understand the mechanism that makes the argument work |
| empirical or worked support | `kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md:73` → `reflection-buys-addressability.md` | inspect the worked instance behind the assertion |
| dependency / premise | `kb/notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md:63` → `context-efficiency-is-the-central-design-concern-in-agent-systems.md` | verify the constraint the source argument depends on |
| argumentative boundary | `kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md:29` → `error-correction-works-above-chance-oracles-with-decorrelated-checks.md` | check the condition under which the stated filter has force |

These uses are broader than a narrow “formal premise” reading, but they remain within the same note-to-note action: assess the source assertion by following its theoretical basis. They do not describe a design artifact's motivating theory, which is the recurring R cohort.

### Every off-pattern pairing

All 38 off-pattern edges are listed below. Their existence is an authorization and classification signal, not a proposed contract change.

- **agent-memory-systems → external (1):** `kb/agent-memory-systems/thalo-type-comparison.md:164`.
- **notes → agent-memory (1):** `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:34`.
- **notes → external (15):** `kb/notes/agentic-systems-interpret-underspecified-instructions.md:144`; `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:38,40`; `kb/notes/definitions/constraining.md:92`; `kb/notes/ephemeral-computation-prevents-accumulation.md:67`; `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md:99`; `kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md:45`; `kb/notes/oracle-strength-spectrum.md:84`; `kb/notes/process-structure-and-output-structure-are-independent-levers.md:48`; `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md:37`; `kb/notes/structure-activates-higher-quality-training-distributions.md:37,38`; `kb/notes/structured-output-is-easier-for-humans-to-review.md:23`; `kb/notes/title-as-claim-enables-traversal-as-reasoning.md:78`; `kb/notes/writing-styles-are-strategies-for-managing-underspecification.md:52`.
- **notes → reference (2):** `kb/notes/commitment-not-derivation-creates-new-ground-truth.md:86`; `kb/notes/two-context-boundaries-govern-collection-operations.md:70`.
- **reference → notes (6):** `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md:157`; `kb/reference/adr/019-collection-owned-link-vocabulary.md:97`; `kb/reference/adr/020-theoretical-default-contrasts-mechanism.md:122`; `kb/reference/definitions/collection.md:39`; `kb/reference/tag-readme-trace-as-self-improving-loop.md:36`; `kb/reference/where-change-candidates-come-from-in-commonplace.md:36`.
- **reference → reference (1):** `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md:154`.
- **sources → agent-memory (1):** `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md:52`.
- **sources → notes (9):** `kb/sources/context-engineering-ai-agents-oss.ingest.md:32`; `kb/sources/creative-thinking-by-claude-shannon.ingest.md:32,36,40,46`; `kb/sources/eric-evans-ai-components-deterministic-system.ingest.md:37`; `kb/sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md:33,39,41`.
- **types → notes (2):** `kb/types/type-spec.md:70,72`.

The external-target cases are citations or source evidence, not theoretical premise links. The source-analysis cases map evidence into claims or compare systems. The reference/type cases use a cross-register “why” action despite lacking the note-to-note source shape; they are the clearest evidence that collection authorization and semantic classification have drifted together.

### Files using both labels

Only two active files author both labels:

1. `kb/reference/tag-readme-trace-as-self-improving-loop.md`: `:36` uses `grounds` for “why actor allocation is reported separately,” while `:37–40` use `rationale` for the definition and theoretical claims the trace is read against.
2. `kb/types/type-spec.md`: `:70` and `:72` use `grounds` for the inspection and checkability bases, while `:71` uses `rationale` for the derived-copy risk.

The first file does not expose a repeatable reader action separating the labels; both are “follow the theoretical basis of this reference reading.” The second similarly mixes “why” and “basis” in one system-definition artifact. These are reclassification candidates, not evidence that all note-to-note `grounds` edges are rationale edges.

## Candidate outcomes

| candidate | evidence for | evidence against | assessment |
|---|---|---|---|
| `rests-on` for `rationale` only | 114 edges across 48 source files complete `source rests-on theoretical target` honestly; the design/rule/description reader journey recurs in reference, instruction, agentic, agent-memory, and source surfaces | 20 of 134 rationale rows are evidence or non-rationale relation; a blind rename would misstate them | **Adopt as a scoped successor candidate**, pending a separate migration run |
| one successor for `rationale` + `grounds` | Source collection is visible and the generic sentence “source rests-on target” can be made to fit both cohorts; one label reduces vocabulary | the reader action differs before following: revisit a design/rule's motivating theory versus assess an assertion's premise; 272 note-to-note grounds edges form a stable cohort, while rationale is predominantly cross-register | **Reject** unless a later reader study shows source collection/context makes the distinction redundant |
| no successor | 18 rationale edges are better handled by existing relation labels or prose; some weak “why” links may not earn a formal edge | 114 repeated cross-register links have a concrete maintenance question and outperform an unlabelled citation; removing them loses the design-to-theory route | **Reject for the R cohort; apply locally to N/X cases** |
| split/reclassification | The corpus itself supplies three stable classes: R dependency, E evidence, and N architecture/navigation; off-pattern grounds add a fourth authorization-cleanup surface | it increases migration bookkeeping and leaves old labels temporarily visible | **Recommended outcome** |

## Assertion and neighboring-label boundary

For the R cohort, the recommended future assertion is:

> `[source artifact] rests-on [target theoretical claim] because [the target explains the design, rule, interpretation, or existence of the source].`

It is an asymmetric source→target relation. The target changing or being rejected triggers design/rule reconsideration, not automatic re-derivation and not merely a citation update.

Boundaries:

- `grounds`: `[source theoretical assertion] grounds [target?]` is not the adopted grammar; semantically, the note-to-note source follows its target to verify a premise. Its existing cohort should be migrated or renamed in its own scoped run, not silently folded into rationale.
- `evidenced-by`: an assertion points to an observation, source, or record that corroborates, qualifies, or bounds it.
- `is-evidence-for`: a source or review points to the assertion it materially bears on, without claiming target-side uptake. This is the correct comparison for the two E rationale rows and most source-side off-pattern grounds rows.
- lineage labels: use `derived-from`, `abstracted-from`, `adapted-from`, or `operationalized-from` only when the source materially generated or was transformed into the target under the registered maintenance regime.
- architecture/navigation: use the collection-authorized `implements`, `part-of`, `depends-on`, `see-also`, or connective prose only after the specific relation is identified. `rests-on` should not become a generic dependency label.

The source collection remains visible context, but it is not a substitute for the assertion. A reader should be able to decide whether to follow for design reconsideration, premise verification, or evidence inspection from the label plus context phrase.

## Ambiguities and counterfactual tests

No edge remains A after full local reading, but these are the highest-information near-ambiguous cases:

- `kb/agentic-systems/claude-code-dynamic-workflows.md:70` says the design stance “partially ships” and the analysis “feeds back as evidence there.” Changing the target note would update the assessment, not require redesigning the external feature: E.
- `kb/sources/goedel-machines-schmidhuber.ingest.md:134` calls the system an “existence proof” of a closed extreme. The source bears on the target claim; the target did not motivate the ingest report's existence: E.
- `kb/reference/tag-readme-trace-as-self-improving-loop.md:36–40` uses both labels in one theoretical reading. The local contexts do not preserve a reliable separate reader action: reclassify the `grounds` edge to the chosen cross-register relation if it remains formal.
- `kb/types/type-spec.md:70–72` does the same in a system-definition artifact. Its target notes explain the contract's inspection and checkability choices; the type surface has no collection contract, so the semantic result is separable from the authorization result.
- `kb/reference/link-vocabulary.md:186–190` and `kb/reference/adr/058-directional-identifiers-use-source-as-subject.md:57` use `rationale` for reference-to-reference architecture/history. The context is intelligible, but it is not the declared theoretical rationale relation: N.

## Guidance surfaces

| surface | current teaching | implication |
|---|---|---|
| ADR 020, especially its “not folded” clause | says `rationale` remains distinct from `grounds`, with rationale cross-register and grounds intra-theoretical | supports a scoped distinction, but predates the source-as-subject migration debt |
| ADR 058 | requires every new directional identifier to read `source <label> target`, while explicitly leaving `rationale` and `grounds` for later runs | makes `rests-on` a viable name but does not decide its corpus |
| `kb/reference/link-vocabulary.md` | defines `grounds` as premise verification and `rationale` as the claim a design/rule rests on, but its catalogue entry still describes the target role | current prose teaches the intended boundary while violating the new grammatical invariant |
| ADR 019 | already merged `rationale` and `justification` because source register is recoverable | precedent for avoiding synonyms; it does not collapse `grounds`, whose assertion cohort differs |
| collection contracts | reference, instructions, sources, agentic-systems, and agent-memory-systems authorize rationale to notes; notes authorize grounds to notes; off-pattern rows are not authorized | contracts encode the useful boundary, but active edges exceed it |
| `cp-skill-write` and `cp-skill-connect` | require reading the source contract, selecting an authorized label, and routing an unmatched candidate to off-authorization | no implementation change is needed for this read-only decision; a later migration must update their current examples/guidance |

## Migration and authorization consequences

No migration was performed. A future run must:

1. change the catalogue, contracts, ADR/guidance surfaces, and R edges together;
2. conserve the 114 R tuples exactly under `rests-on`;
3. reclassify the two E rows through `is-evidence-for` review and decide each of the 18 N rows individually;
4. handle all 38 off-pattern grounds rows separately, without treating authorization as semantic proof;
5. leave snapshots, generated reports, archived proposals, workshop history, ordinary prose, and reciprocal edges untouched;
6. add a deterministic check for source/destination authorization only after the chosen vocabulary is authoritative.

The 19 rationale authorization gaps are 16 reference→reference rows, 2 notes→reference rows, and 1 `kb/types/` row without a collection contract. The 38 grounds off-pattern rows are additional authorization gaps or unregistered type-surface uses. These are not reasons to edit contracts in this review; they are migration inputs for the maintainer.

## Confidence and reversal evidence

Confidence is **0.84** for the split/reclassify recommendation and **0.91** for the individual E/N classifications. The recommendation would reverse if either of these appears:

- a substantial new sample of `rationale` edges shows that the source is itself a theoretical assertion whose target is a premise, making the R/G boundary unstable;
- a controlled reader test shows that `rationale` versus `grounds` does not change follow/skip or maintenance decisions once the source collection and context phrase are visible;
- repeated cross-register `grounds` use demonstrates an independently useful reader journey that cannot be represented by `rests-on` or an evidence label;
- maintainers show that the 114 R edges are merely citations or historical explanations and do not cause design/rule reconsideration when their targets change.

## Provenance

This is a model-agnostic local corpus evaluation. No model-specific execution claim is made.
