# Audit: validation, freshness, and executable behavior

## Deterministic validation

The validator's oracle is warranted where truth is mechanically available from repository state:

- frontmatter and schema shape;
- type resolution and allowed values;
- path and Markdown-link existence;
- exact quote/source matching within the verifier's declared rules;
- generated-index and tag-README marks that can be recomputed;
- naming and bounded metadata constraints.

These checks can reject invalid candidates because their decision procedure is inspectable and repeatable. They do not establish title quality, explanatory adequacy, attribution correctness beyond explicit source matching, or semantic truth. The `cp-skill-convert` correction restores that boundary in the authoring layer.

## Freshness

Freshness state is evidence applicability, not artifact acceptance. Baseline keys, note revisions, criterion revisions, status computation, integrity checks, acknowledgements, retirements, and transitions retain a history of what was reviewed against what. This is a direct cumulative dependency: later review-selection decisions consume retained prior baselines rather than merely encountering a changed environment.

Two boundaries remain deliberate:

1. Prompt/process dependencies are not fully represented in review freshness; see [review-and-fix-loop](./review-and-fix-loop.md).
2. Theory-to-instruction lineage and collection contracts are not ordinary review-pair dependencies. The repository already has proposals for factored dependencies and collection-as-artifact freshness. Until a wider substrate exists, the cluster's future digest needs explicit `operationalized-from` lineage and managed-staleness correspondence checks.

These boundaries should not be hidden by broadening a hash indiscriminately. Each dependency needs a named consumer and transition semantics.

## Mutation and retention

Relocation, initialization, snapshot, promotion-candidate, and full-pass commands alter retained repository state or prepare guarded changes. Their strongest protections are explicit target resolution, version checks, dry-run/report stages, and human confirmation for semantically destructive outcomes. The code does not infer that every retained change is an improvement; it records or applies an authorized operation.

That distinction matters for the cluster: **retention is an operative event, not evidence of beneficial direction**. Improvement membership additionally requires a warranted evaluation and the declared comparison horizon.

## Search surfaces

Target selectors, promotion-candidate generation, extraction helpers, indexes, and tag marks increase search range and addressability. They are valuable even when noisy because downstream evaluation can filter candidates. The same reasoning supports automating semantic problem-noticing before automating semantic acceptance.

## Cumulativity contact test

The profile note's environment-mediated exclusion survives the code audit:

- Freshness baselines directly affect whether a later review is selected or considered current, so they are retained state consumed by the improvement process.
- Generated tag/index marks directly affect retrieval and validation, so they are retained organizational state.
- A prior edit that merely changes the text later encountered by an otherwise unchanged process is not cumulative by that fact alone; the environment carries the effect, not a retained improvement mechanism.

No amendment to the profile note is warranted from these cases.

## Verification expectations

The audit's applied changes are documentation and instruction-contract changes. They require deterministic instruction validation, type validation, diff hygiene, and focused tests for validation/scaffolding behavior. They do not change executable schemas or database migrations.
