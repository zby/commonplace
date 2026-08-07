# Linking contract consistency

## Purpose

Reconcile Commonplace's declared linking architecture with its live collection contracts, authoring procedures, validator, and reader surfaces. The immediate trigger is a cross-collection audit that found accepted decisions, shared vocabulary, collection-local rules, and executable procedures describing different systems.

Lineage-specific carrier, relation, and invalidation contradictions stay in the sibling [lineage mechanisms ledger](../lineage-mechanisms/current-contradictions.md). This workshop owns the remainder: navigation links, relationship-label direction outside lineage, collection grammar, reciprocal-link procedure, validation, and inbound-link delivery.

The sibling [linking foundations](../linking-foundations/README.md) workshop owns the deeper question of what an authored link represents and how philosophy, discourse theory, and cognitive science should shape the model. This workshop consumes those conclusions while retaining ownership of concrete contract reconciliation and migrations.

## Plan (handoff updated 2026-07-30)

This section is the takeover picture: what the foundations workshop delivered, and the resulting work queue in dependency order. Read it before touching any label.

### What the foundations workshop delivered

The hold this README previously implied — do not adopt or migrate `explained-by` / `operates-through` before the foundational questions settle — is lifted in substance. The foundations results this workshop now consumes (full argument in [competing link models](../linking-foundations/competing-link-models.md); evidence in the [generator retrodiction run](../linking-foundations/generator-retrodiction-run.md)):

- **The two-consumer registration test.** A label distinction earns a registered identifier iff it changes the reader's follow/skip decision or the revision consequence when the target changes. Every new or migrated catalogue entry should state both, plus a boundary test. This codifies what ADRs 058/060 already did implicitly.
- **Boundary tests, not a role ontology.** Endpoint-level ambiguity (artifact vs claim vs described process) is handled by per-identifier boundary tests; no source-role/target-role signature schema is needed.
- **Grammar strictness is the asset.** The normalized footer grammar is what made every audit and migration possible; keep it strict even while vocabulary stays collection-owned and loose.
- **Classify with k samples, never single runs.** The revision-consequence A/B showed single-run semantic classifications mislead at exactly the granularity migrations care about.
- **Three corpus-confirmed vocabulary gaps**, with evidence dossiers in the retrodiction run file: `elaborated-by` (reference→reference detail routing, ~18 sites), `is-enforced-by` and `is-consumed-by` (types→reference, 5 mislabeled edges plus ~11 missing-edge sites). One confirmed non-gap: the system-review collections' analogue relation toward reference is deliberate under-commitment — `see-also` stays.

### Work queue (dependency order)

1. **Completed: reclassify the mechanism surface** — the [blind test](./blind-mechanism-reclassification-results.md) reversed the first ledger, so the maintainer authorized a [full k=3 replacement](./mechanism-full-reclassification-results.md). That run retained the explanatory/operational distinction while replacing the row assignments.
2. **Mechanism ledger closed; premise ledger reopened** — the maintainer accepted `explained-by`, `operates-through`, and 87 unanimous rows at the full-run baseline, and the [42-row exact-boundary result](./mechanism-boundary-adjudication-results.md) settles the remaining mechanism rows. The [premise replication](./premise-cohort-replication/results.md) then returned `REOPENS` under its frozen gate: 44/49 sampled legacy-P rows were adverse. That result blocks migration from the premise ledger without itself proving that the premise relation is unusable or supplying replacement row labels.
3. **Phase A ready; phase B withdrawn** — the [premise/mechanism packet](./premise-mechanism-implementation-packet.md) and [374-row live manifest](./premise-mechanism-live-disposition-manifest.tsv) remain the exact pre-replication planning baseline. The packet's 82-row `mechanism` phase is independently ready for approval. Its 292-row `grounds` phase is not executable; the manifest's premise dispositions are provenance, not an approved migration ledger.
4. **Mechanism migration** — after packet approval, adopt `explained-by` / `operates-through`, scope ADR 009, and migrate the 82 active `mechanism` rows: 81 exact successors and one removal. Rebaseline before mutation; leave all 292 `grounds` rows unchanged in this phase.
5. **Calibrate the premise relation** — approve and run the [discriminability experiment](./premise-relation-discriminability-experiment.md). It separates semantic relation, formal registration, and insufficiency; includes known positive controls; and compares direct classification with the observer-to-mapper pipeline.
6. **Test corpus transport only after calibration** — if the instrument passes, freeze a new protocol over an untouched deterministic holdout from the 106 legacy-P rows not sampled by the replication. A successful transport result may justify a complete row-level replacement run; it cannot be copied directly into migration edits.
7. **Prerequisite family review** — review `enables` / `precondition` over their full corpus plus held prerequisite rows, including `F094`. This can proceed independently, but settling the hold no longer unlocks `grounds` retirement by itself.
8. **Rebuild and approve the grounds migration** — only after steps 5–7 support a distinguishable, registerable relation and a complete exact ledger should a fresh packet decide whether to adopt `premised-on`, add notes→notes `is-evidence-for`, and retire `grounds`.
9. **Gap authorizations** — maintainer decides registration of `elaborated-by` (reference contract) and `is-enforced-by`/`is-consumed-by` (types contract); agent drafts contract language, catalogue entries per the two-consumer test, and the site-fix lists from the dossiers.
10. **ADR 009 scoping amendment** — fold into step 4's ADR: ADR 009's vocabulary was the theory-collection seed, superseded in scope by ADR 019 and the seed-then-harvest model.
11. **Reference ADR-local label tail audit** — `decision` ×11, `foundation` ×6, `refines` ×5, `outcome`, `amended-by`, and a dozen singletons found live in reference→reference footers; check each against contract and type-override authorization.
12. **Standing items** (unordered, from the sections below): per-destination grammar serialization decision, the articles contract gap, the validator boundary, reciprocal-link operationalization, backlink surfacing.

### Operating rules for the takeover agent

- Semantic classification and adjudication evidence use k≥3 independent samples per row.
- Rebaseline every cohort before execution; review counts drift while work is in flight.
- No batch migration executes without a maintainer-approved plan; adjudications and authorizations are maintainer decisions — prepare packets, do not decide.
- New and migrated catalogue entries state reader need, revision consequence, and a boundary test.

## Working files

- [Pre-migration link-authorization matrix](./current-authorization-matrix.md) — historical inventory of collection contracts and cross-contract conflicts at the migration baseline; its old `evidence` rows are superseded by ADR 058.
- [Evidence direction review](./evidence-direction-review.md) — corpus review of 26 source/review→note uses; establishes a real inverse reader journey while deferring its identifier to the whole-vocabulary grammar audit.
- [Directional label grammar](./directional-label-grammar.md) — adopted invariant that every directional identifier complete `source <label> target`, plus the initial pass/fail inventory and remaining migration debt.
- [Evidence label migration plan](./evidence-label-migration-plan.md) — compact execution packet for adopting `evidenced-by` / `is-evidence-for`, migrating active contracts and edges, verifying conservation, and capturing lessons for the next label.
- [Evidence label migration retrospective](./evidence-label-migration-retrospective.md) — completed first-run reconciliation and the mandatory add/remove/reorder/automate amendments the next directional-label migration must explicitly accept or reject.
- [Rationale label evaluation](./evaluate-rationale-link-label.md) — read-only semantic review packet for deciding whether `rests-on` is distinct, should merge with `grounds`, should split, or should be retired before migration.
- [Rationale and grounds boundary adjudication](./rationale-grounds-boundary-adjudication.md) — implemented successor decisions for the 20 non-R `rationale` edges and all 38 off-pattern `grounds` edges, including authorization consequences.
- [Rationale label migration plan](./rationale-label-migration-plan.md) — completed execution packet for adopting `rests-on`, reclassifying boundary edges, and preserving the canonical `grounds` cohort.
- [Rationale label migration retrospective](./rationale-label-migration-retrospective.md) — second-run reconciliation, surprises, and procedure-promotion decision.
- [Grounds label evaluation](./evaluate-grounds-link-label.md) — Luna-ready read-only packet for deciding the successor and classifying every active canonical note→note `grounds` edge before any migration.
- [Grounds direction review](./grounds-label-direction-review.md) — complete 283-edge semantic inventory recommending `premised-on` for the 160-row premise cohort and reclassification of the remaining edges.
- [Grounds boundary adjudication](./grounds-label-boundary-adjudication.md) — accepts `premised-on`, assigns exact successors to 74 evidence/extension/mixed rows, and defers 49 mechanism candidates to the mechanism-label review.
- [Mechanism label evaluation](./evaluate-mechanism-link-label.md) — Luna-ready full-corpus packet covering both active `mechanism` edges and the 49 mechanism-like `grounds` rows deferred from adjudication.
- [Blind mechanism reclassification test](./blind-mechanism-reclassification-test.md) — runnable packet for the reversal evidence the mechanism review pre-registered: k-sampled blind EX/OP reclassification of a deterministic 49-row sample, with pre-registered survive/reverse thresholds; the last evidence input before the split's maintainer adjudication.
- [Blind mechanism reclassification results](./blind-mechanism-reclassification-results.md) — reversal evidence that rejected the first row-level EX/OP ledger and triggered a full replacement run.
- [Full mechanism reclassification results](./mechanism-full-reclassification-results.md) — 387-vote replacement ledger restoring the split while exposing 42 rows outside its accepted unanimous core.
- [Full mechanism adjudication](./mechanism-full-reclassification-adjudication-packet.md) — records maintainer acceptance of the split, spellings, 87 unanimous rows, and next read-only evidence work.
- [Mechanism boundary adjudication protocol](./mechanism-boundary-adjudication-protocol.md) — exact-choice k=3 protocol for the remaining 42 rows.
- [Mechanism boundary adjudication results](./mechanism-boundary-adjudication-results.md) — 126-vote exact ledger with 36 stable recommendations, six unstable rows, and conditional authorization consequences.
- [Grounds drift reclassification protocol](./grounds-drift-reclassification-protocol.md) — k=3 exact-choice protocol for the 21 live `grounds` additions absent from the direction-review baseline.
- [Grounds drift reclassification results](./grounds-drift-reclassification-results.md) — 63-vote ledger recording maintainer acceptance of 16 unanimous and five contested exact-majority dispositions, with no unstable rows and a complete 374-tuple current disposition count.
- [General experiment-design guardrails](./link-vocabulary-experiment-design.md) — context, isolation, leakage, independence, matched judgment axes, positive-control, and conclusion-bounding requirements for workshop experiments.
- [Premise-cohort replication instruction](./run-premise-cohort-replication.md) — frozen cohort, blindness, staged observation/mapping, and decision rules used by the completed Luna run.
- [Premise-cohort replication result](./premise-cohort-replication/results.md) — protocol-level `REOPENS` decision, narrow migration-hold conclusion, diagnostics, and post-run audit.
- [Premise-relation discriminability experiment](./premise-relation-discriminability-experiment.md) — proposed positive-control calibration separating semantic relation from registration and testing direct versus staged classification.
- [Premise and mechanism implementation packet](./premise-mechanism-implementation-packet.md) — phase A remains ready; phase B and its premise ledger are withdrawn pending calibration and corpus transport.
- [Premise and mechanism live disposition manifest](./premise-mechanism-live-disposition-manifest.tsv) — 374-row pre-replication planning baseline retained for tuple identity and decision provenance, not an executable phase-B ledger.
- [Reusable directional-label migration procedure](../../instructions/migrate-directional-link-label.md) — promoted mechanical core confirmed by the evidence and rationale runs; semantic classification remains label-specific.

## Confirmed contradictions

### ADR 009 still presents a global five-label vocabulary

[ADR 009](../../reference/adr/009-link-relationship-semantics.md) says every KB link must use one of five relationship types. The live architecture is collection-owned under [ADR 019](../../reference/adr/019-collection-owned-link-vocabulary.md), and current collections authorize many later labels. ADR 020 extends the theoretical defaults but does not qualify ADR 009's global sentence.

**Needed outcome:** amend, partially supersede, or explicitly scope ADR 009 so readers can tell which parts remain current.

### Required collection grammar and accepted working formats disagree

ADR 019, as extended by ADR 059's `external` destination, and the [shared authoring guide](../../reference/link-vocabulary.md#authoring-collection-link-rules) require per-destination semantics with search guidance and authorized labels. Several main collections serialize that contract as one scan paragraph plus a labels table rather than one block per destination. The [writing skill](../../instructions/cp-skill-write/SKILL.md#step-2---load-collection-conventions) already accepts per-destination blocks, a table, or prose.

**Needed outcome:** either make per-destination semantics the requirement while allowing multiple serializations, or migrate contracts and procedures to the stricter block form.

### Some writable collections have no complete outbound-link contract

The [article collection](../../articles/COLLECTION.md) now declares its unlabeled in-prose `external` surface, but its in-prose links into the KB still lack authorized local destinations. The illustrative [dialectical sample collection](../dialectical-sample/COLLECTION.md) now has an executable `evidenced-by` citation grammar and is no longer part of this gap.

**Needed outcome:** give each collection an operational grammar or an explicit exemption that writing and connect procedures know how to interpret.

### Resolved: `evidence` was used against its declared direction

The pre-migration catalogue described `evidence` as asymmetric, theoretical → descriptive, while source analyses and agent-memory reviews also used it toward notes. [ADR 058](../../reference/adr/058-directional-identifiers-use-source-as-subject.md) resolves the conflict with `evidenced-by` for assertion→observation and `is-evidence-for` for observation→assertion. Both directions remain independently authored reader aids.

**Outcome:** adopted, contract-authorized, and migrated; the [retrospective](./evidence-label-migration-retrospective.md) carries the reconciled corpus counts and next-run amendments.

### Resolved: `compares-with` had stale scope documentation

The shared catalogue called `compares-with` specific to `kb/agent-memory-systems/`, while live use and contracts spanned reference artifacts, sources, memory-system reviews, and agentic-system analyses.

**Outcome:** the catalogue now defines the source-as-subject assertion and declares the relation self-dual; reference and source contracts authorize the live pairings. Reciprocal authoring remains optional because each direction still needs its own reader need.

### Resolved: literal `any` conflicted with collection exclusions

`reference` and `sources` used `see-also | any` while separately excluding workshop or instruction destinations. ADR 059 now defines `any` literally, including `external`; those two library tables name their permitted destinations explicitly. Only the deliberately permissive workshop contract retains `any`.

### Resolved: `rationale` named the target rather than the source assertion

The old identifier meant “the target is the rationale for the source,” violating `source <label> target`; 20 of 134 active uses also belonged to evidence or architecture relations. Thirty-eight off-pattern `grounds` edges exposed the same boundary drift.

**Outcome:** [ADR 060](../../reference/adr/060-rationale-becomes-rests-on-and-off-pattern-grounds-reclassified.md) adopts `rests-on`, reclassifies every boundary edge, gives `kb/types/` a collection-owned link contract, and leaves 276 canonical note→note `grounds` edges for their own scoped migration.

## Enforcement and delivery gaps

### Deterministic validation checks link existence, not link contracts

`commonplace-validate` does not currently verify that a footer label is authorized for its source/destination pair, that an asymmetric label points the declared way, or that a writable collection supplies usable outbound rules. The contradictions above therefore validate cleanly.

**Question:** which parts are stable and syntactic enough to validate now, and which should remain collection-conformance review criteria until the vocabulary settles?

### Reciprocal-link policy is documented but only partially operationalized

The shared vocabulary now permits a reciprocal link when the reverse journey independently helps readers and rejects mandatory mirroring. `cp-skill-connect` already reports reverse-edge candidates, but the write/connect procedures do not explicitly test a proposed reciprocal edge against the separate reader need or distinguish it from lineage placement rules.

**Question:** is the articulation test sufficient, or should reciprocal candidates carry an explicit “independent reverse reader need” check in reports and authoring guidance?

### The inbound view remains a remembered query

There is no rendered backlink view and no dedicated command. Agents must remember to invert links with repository search; the [backlink-surfacing proposal](../../reference/proposals/backlink-surfacing.md) leaves both the web materialization and possible command open.

**Question:** does repeated operational need now justify a documented recipe, a `commonplace-backlinks` command, build-time web rendering, or some combination?

## Boundaries

In scope:

- current meaning and direction of non-lineage link labels;
- collection-level outbound grammar and specialized overrides;
- reciprocal-link and reverse-edge authoring procedure;
- semantic validation that can be deterministic;
- agent and human inbound-link surfaces;
- reconciliation or supersession of stale linking ADR language.

Out of scope:

- where derivation lineage is stored and how source change invalidates derivatives;
- generic freshness databases or merge-back event stores;
- general natural-language vocabulary governance beyond relationship labels;
- bulk migration of corpus links before the target semantics are decided.

## Closure

Close this workshop when:

1. accepted ADRs, the shared catalogue, collection contracts, and authoring skills describe one compatible linking model;
2. every writable collection has either a usable outbound-link contract or a declared, executable override;
3. every asymmetric label used across collections has an unambiguous direction;
4. reciprocal links and derived inbound views have distinct, operational procedures;
5. the validator boundary is explicit, with stable mechanical checks implemented or deliberately deferred;
6. any necessary corpus migration has a scoped plan and durable owners.

Expected outputs are an ADR amendment or superseding ADR, targeted collection-contract and skill edits, a validation proposal or implementation for stable rules, and a decision on the backlink-surfacing proposal.
