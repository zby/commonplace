# Rationale and grounds boundary adjudication

**Status:** completed and implemented by ADR 060.

**Date:** 2026-07-28

## Decision

The 20 active `rationale` edges outside the confirmed rationale-dependency cohort and all 38 off-pattern `grounds` edges now have concrete successor decisions. None should be removed: each still carries a specific reader need once separated from the overloaded label.

| boundary population | `rests-on` | `evidenced-by` | `is-evidence-for` | `implements` | `compares-with` | remove | total |
|---|---:|---:|---:|---:|---:|---:|---:|
| non-R `rationale` | 0 | 15 | 2 | 2 | 1 | 0 | 20 |
| off-pattern `grounds` | 8 | 20 | 10 | 0 | 0 | 0 | 38 |
| **total** | **8** | **35** | **12** | **2** | **1** | **0** | **58** |

Together with the 114 R rows already approved by the [direction review](./rationale-label-direction-review.md), the migration has 122 `rests-on` successors: 114 direct successors plus 8 off-pattern `grounds` corrections. Four concurrent note→note edges arrived after this adjudication, so the implementation leaves 276 canonical `grounds` rows untouched for their own vocabulary evaluation.

The classification test is the assertion made at the authored edge:

- `source rests-on target` when a design, description, rule, or type contract depends on a theoretical claim;
- `source evidenced-by target` when an assertion or description points to a corroborating, qualifying, or boundary record;
- `source is-evidence-for target` when a source analysis or external-system observation points to the assertion it bears on;
- `source implements target` when a concrete decision realizes a reference-level architecture or contract;
- `source compares-with target` when the useful journey is comparison along a named design boundary.

Line numbers below identify the reviewed baseline. Migration must reconcile source/target tuples rather than trust line numbers after edits.

## Non-R rationale ledger

| current edge(s) | successor | adjudication |
|---|---|---|
| `kb/agentic-systems/claude-code-dynamic-workflows.md:70` | `is-evidence-for` | The feature analysis feeds back as evidence for the target design stance; the stance did not motivate the analysis artifact. |
| `kb/sources/goedel-machines-schmidhuber.ingest.md:134` | `is-evidence-for` | The source is an existence proof bearing on the target claim. |
| `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md:99` | `evidenced-by` | ADR 042 records the decision that qualifies and narrows the source assertion. |
| retired theory-side text-contract definition, former line 57 | `evidenced-by` | ADR 042 was the decision record supporting the definition's then-open profile set. |
| `kb/reference/adr/045-source-genre-is-a-single-open-field-on-the-snapshot.md:53` | `implements` | The ADR's concrete mechanism realizes the target's type-owned-semantics boundary. |
| `kb/reference/adr/058-directional-identifiers-use-source-as-subject.md:57` | `implements` | The directional-identifier decision preserves and realizes ADR 019's collection-owned authorization architecture. |
| `kb/reference/collections-and-types.md:87-91` | `evidenced-by` | The five ADRs are decision records corroborating the shipped architecture this reference page describes. |
| `kb/reference/link-vocabulary.md:186-190` | `evidenced-by` | The five ADRs are the decision history supporting and bounding the current catalogue. |
| `kb/reference/proposals/factored-dependency-pairs-for-review-freshness.md:58` | `evidenced-by` | ADR 038 is the shipped instance demonstrating the factoring pattern the proposal generalizes. |
| `kb/reference/proposals/generalized-validation-invalidation-and-imperative-extension.md:83` | `compares-with` | The proposal and current architecture differ on the named collection-ownership boundary; neither implements nor theoretically grounds the other. |
| `kb/reference/text-contract-profiles.md:106` | `evidenced-by` | ADR 042 records the decision that opened and seeded the catalogue. |
| `kb/reference/types/adr.md:69` | `evidenced-by` | The reference trace supplies the observed change-candidate stream supporting the type's instrumentation requirement. |

This accounts for 20 edges: the two five-edge rows each conserve five distinct source/target tuples.

## Off-pattern grounds ledger

### Reclassify as evidenced-by (20)

These source assertions or descriptions point to observations, cases, sources, or records that corroborate, qualify, or bound them:

- `kb/agent-memory-systems/thalo-type-comparison.md:164` — external Toulmin source supporting the comparison's decomposition;
- `kb/notes/continual-learning-open-problem-is-behaviour-not-knowledge.md:34` — reviewed-system survey supporting the claimed split;
- `kb/notes/agentic-systems-interpret-underspecified-instructions.md:144`;
- `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md:38,40`;
- `kb/notes/definitions/constraining.md:92`;
- `kb/notes/ephemeral-computation-prevents-accumulation.md:67`;
- `kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md:99`;
- `kb/notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md:45`;
- `kb/notes/oracle-strength-spectrum.md:84`;
- `kb/notes/process-structure-and-output-structure-are-independent-levers.md:48`;
- `kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md:37`;
- `kb/notes/structured-prompt-gains-do-not-establish-distribution-selection.md:40,41,42`;
- `kb/notes/structured-output-is-easier-for-humans-to-review.md:23`;
- `kb/notes/title-as-claim-enables-traversal-as-reasoning.md:78`;
- `kb/notes/writing-styles-are-strategies-for-managing-underspecification.md:52`;
- `kb/notes/commitment-not-derivation-creates-new-ground-truth.md:86` — the current registered lineage semantics bound the theoretical argument;
- `kb/notes/two-context-boundaries-govern-collection-operations.md:70` — ADR 003 is a shipped case exhibiting the asserted boundary;
- `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md:154` — ADR 009 is the decision record for the vocabulary this ADR says remains unchanged.

The external target at `rlm-has-the-model...:37` uses evidence semantics in this run. Its phrase says the note “abstracts” the walkthrough, but promoting it to formal lineage would require the separate lineage classification and carrier rules; this adjudication does not pre-empt that workshop.

### Reclassify as is-evidence-for (10)

These source analyses point from an observation or source to the claim or descriptive analysis it bears on:

- `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md:52` — the A-MEM source bears on the comparative review that includes it;
- `kb/sources/context-engineering-ai-agents-oss.ingest.md:32`;
- `kb/sources/creative-thinking-by-claude-shannon.ingest.md:32,36,40,46`;
- `kb/sources/eric-evans-ai-components-deterministic-system.ingest.md:37`;
- `kb/sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md:33,39,41`.

The nine source→note rows do not assert target-side provenance merely because some context phrases say “derived” or “precursor.” They assert where the reviewed source bears on current claims. Any formal lineage edge must be decided under the lineage workshop's maintenance semantics.

### Reclassify as rests-on (8)

These system-definition or descriptive artifacts point to theoretical claims that explain their design or reading:

- `kb/reference/adr/018-types-are-path-references-to-instruction-docs.md:157`;
- `kb/reference/adr/019-collection-owned-link-vocabulary.md:97`;
- `kb/reference/adr/020-theoretical-default-contrasts-mechanism.md:122`;
- `kb/reference/definitions/collection.md:39`;
- `kb/reference/tag-readme-trace-as-self-improving-loop.md:36`;
- `kb/reference/where-change-candidates-come-from-in-commonplace.md:36`;
- `kb/types/type-spec.md:70,72`.

The type-spec rows follow the same semantic relation as its current `rationale` row at line 71. Their missing collection contract is an authorization-surface problem, not a reason to preserve label drift.

## Authorization consequences

Most decisions already fit their source collection's current destination authorization once the new labels are adopted. Three deltas need explicit handling in the migration:

1. `kb/agentic-systems/ → kb/notes/` must authorize `is-evidence-for` for the single Claude Code row.
2. `kb/sources/ → kb/agent-memory-systems/` must authorize `is-evidence-for` for the A-MEM row.
3. `kb/types/` needs an explicit outbound-link governance decision before its three theoretical dependencies can become `rests-on`; silently borrowing `kb/reference/` authorization would leave the current contract gap intact.

The `rests-on` migration must replace `rationale` authorization on the affected cross-register pairings rather than add a permanent synonym. No contract should be widened to accept off-pattern `grounds`, and the canonical note→note cohort remains unchanged until its own evaluation chooses a source-as-subject identifier.

## Migration handoff

The semantic gate for the scoped `rests-on` migration is now satisfied. Its mutable tuple ledger is:

- 114 active R `rationale` edges → `rests-on`;
- 8 off-pattern `grounds` edges → `rests-on`;
- 20 non-R `rationale` edges → the decisions above;
- 30 remaining off-pattern `grounds` edges → the evidence decisions above;
- 276 note→note `grounds` edges → excluded unchanged for the later `grounds` migration, including four canonical rows added after review.

Migration conserved all 172 adjudicated tuples (114 + 8 + 20 + 30), kept the five disposition buckets mutually exclusive, and separately accounted for the 276 deferred `grounds` tuples. The decision and implementation are recorded in [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md).
