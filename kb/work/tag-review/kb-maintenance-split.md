# Split of kb-maintenance into three children

Assignment list for the operator's review before it is applied. Every member
keeps `kb-maintenance` except the three dropped at the end. Paths relative to
`kb/`.

## review-system (15) — the review pipeline: gates, verdicts, freshness, protocol, cost

- notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
- notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md
- notes/semantic-review-catches-content-errors-that-structural-validation.md
- notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md
- reference/full-improvement-pass-closure.md
- reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md
- reference/proposals/collection-as-artifact-freshness.md
- reference/proposals/factored-dependency-pairs-for-review-freshness.md
- reference/proposals/gate-learning-from-accepted-edits.md
- reference/proposals/generalized-validation-invalidation-and-imperative-extension.md
- reference/proposals/model-partition-registry.md
- reference/proposals/review-configuration-object.md
- reference/proposals/routine-bilateral-isolation-for-literature-assessment.md
- reference/proposals/structured-output-codec-for-review-protocol.md
- reference/proposals/automated-note-refinement-as-search-over-source-bundle.md

## claims-and-grounding (12) — claims as units and what supports them: title as claim, modality, quotes, source grounding, ground truth

- notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md
- notes/title-as-claim-makes-overlap-between-notes-visible.md
- notes/claim-modality-is-the-inference-form-of-the-refuter.md
- notes/commitment-not-derivation-creates-new-ground-truth.md
- notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
- notes/superseded-choices-are-retained-superseded-beliefs-are-not.md
- notes/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md
- notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md
- notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md
- notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md
- notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md
- reference/proposals/write-time-vocabulary-collision-controls.md

## curation (14) — keeping the library navigable and healthy: indexes and tags, quality signals, hygiene, capacity, retirement

- notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md
- notes/index-completeness-does-not-determine-editorial-orientation.md
- notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md
- notes/notes-need-quality-scores-to-scale-curation.md
- notes/quality-signals-for-kb-evaluation.md
- notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md
- notes/maintenance-capacity-must-match-harmful-artifact-inflow.md
- notes/maintenance-operations-catalogue-should-stage-stable-procedures.md
- notes/cheap-adoption-and-weak-retirement-accumulate-cost.md
- notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md
- notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md
- reference/proposals/keyword-tags-without-heads.md
- reference/proposals/tag-maintenance-and-derived-browsing.md
- reference/proposals/periodic-connect-report-mining.md

## Kept on the parent head directly (6)

- notes/documentation-generates-the-system-rather-than-describing-it.md
- notes/domain-pricing-routes-an-exception-to-idealization-assessment.md
- notes/final-task-success-does-not-establish-intended-path-health.md
- notes/brainstorming-how-explanatory-reach-informs-kb-design.md
- notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md
- reference/proposals/a-reader-facing-banner-for-user-verification.md

## Dropped from kb-maintenance (3) — write-path proposals, not maintenance

- reference/proposals/per-artifact-write-briefs.md (keeps context-engineering)
- reference/proposals/deterministic-write-context-assembly.md (keeps context-engineering)
- reference/proposals/artifact-function-as-a-routing-field.md (keeps context-engineering, type-system)
