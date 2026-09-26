---
description: "Curated head for the review-system tag — LLM review of notes: gates and criteria, assays, verdict freshness and invalidation, review cost, and proposals for the review pipeline"
type: types/tag-readme.md
complete: true
---

# review-system

Semantic review of KB artifacts by an LLM: what a review can catch that validation cannot, when a review verdict goes stale, what reviews cost, and proposed changes to the review pipeline. The shipped system is described in [the review system reference](../reference/README-REVIEW-SYSTEM.md), which defines its concepts: an assay applies a criterion to a note; a gate is a closed-ended, verdict-kind criterion whose outcome is pass, warn, or fail; a freshness baseline records when a verdict still applies. Deterministic structural checks (schemas, links, required sections) are not review; they belong to the validation side of [document-system](./document-system-README.md). A child of [kb-maintenance](./kb-maintenance-README.md).

## What review checks and when verdicts go stale

- [Semantic review catches content errors that structural validation cannot](../notes/semantic-review-catches-content-errors-that-structural-validation.md) — why review exists beside validation: enumeration completeness, grounding drift, boundary cases, internal contradictions
- [A note is an atomic step relative to the check that reads it](../notes/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md) — sizes a note to one inference a reviewer can check in a single pass
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — which edits make a verdict stale: the note and the criterion count, the production process does not
- [Full improvement pass closure](../reference/full-improvement-pass-closure.md) — how the shipped full-improvement workflow reassays final note bytes, routes residual findings, and stops without claiming convergence
- [Single-artifact review bundles still cut Claude costs substantially](../notes/evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md) — cost evidence: the single-artifact bundle refactor held its savings after cache-aware price weighting

## Proposals: freshness and invalidation

- [Factored dependency pairs for review freshness](../reference/proposals/factored-dependency-pairs-for-review-freshness.md) — proposal to keep review dependencies as two-input pairs where that shape fits; decides how review targets with more than two inputs are handled
- [Collection-as-artifact freshness](../reference/proposals/collection-as-artifact-freshness.md) — proposal to register collection-maintenance targets with collection-text inputs, for casebook-wide staleness without per-file dependency edges
- [Generalized validation invalidation and imperative extension](../reference/proposals/generalized-validation-invalidation-and-imperative-extension.md) — proposal deciding when to generalize validator invalidation or imperative type extension: only after local cases prove reusable machinery

## Proposals: gates and review method

- [Calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — proposal to require known-case regression before a gate advances, and to keep live detection-rate claims for separate field calibration
- [Gate learning from accepted edits](../reference/proposals/gate-learning-from-accepted-edits.md) — proposal to mine gate candidates from accepted note edits with a promotion lifecycle; atomic gates shipped, the learning has not
- [Routine bilateral isolation for literature assessment](../reference/proposals/routine-bilateral-isolation-for-literature-assessment.md) — proposal deciding whether matched evidence should make bilateral isolation a routine control rather than a conditional diagnostic
- [Automated note refinement as a search over a fixed source bundle](../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) — proposal to refine from a source bundle that emits a set of notes, so split, drift, and kill become search outcomes rather than non-convergence

## Proposals: review machinery

- [Model partition registry](../reference/proposals/model-partition-registry.md) — proposal for a registry of model partitions for validation, aliases, and runner defaults, without making it the review identity
- [Review configuration object](../reference/proposals/review-configuration-object.md) — proposal for a ReviewConfig holding scan roots, gate and artifact locations, and database path, with project overrides
- [Structured-output codec for the review protocol](../reference/proposals/structured-output-codec-for-review-protocol.md) — proposal to make review output a pluggable codec: sentinel markdown now, schema-validated structured output when harnesses support it

## Related Tags

- [kb-maintenance](./kb-maintenance-README.md) — the parent: review is one of the detection mechanisms that keep the KB healthy
- [claims-and-grounding](./claims-and-grounding-README.md) — sibling: grounding is the most common thing a gate checks, and its evidence notes come from review runs
- [curation](./curation-README.md) — sibling: index and tag upkeep, which review does not judge
- [evaluation](./evaluation-README.md) — how LLM judgments are calibrated and trusted, which gates depend on
- [observability](./observability-README.md) — staleness signals and review telemetry
- [document-system](./document-system-README.md) — the deterministic validation that review complements
