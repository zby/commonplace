# Linking contract consistency

## Purpose

Reconcile Commonplace's declared linking architecture with its live collection contracts, authoring procedures, validator, and reader surfaces. The immediate trigger is a cross-collection audit that found accepted decisions, shared vocabulary, collection-local rules, and executable procedures describing different systems.

Lineage-specific carrier, relation, and invalidation contradictions stay in the sibling [lineage mechanisms ledger](../lineage-mechanisms/current-contradictions.md). This workshop owns the remainder: navigation links, relationship-label direction outside lineage, collection grammar, reciprocal-link procedure, validation, and inbound-link delivery.

## Working files

- [Pre-migration link-authorization matrix](./current-authorization-matrix.md) — historical inventory of collection contracts and cross-contract conflicts at the migration baseline; its old `evidence` rows are superseded by ADR 058.
- [Evidence direction review](./evidence-direction-review.md) — corpus review of 26 source/review→note uses; establishes a real inverse reader journey while deferring its identifier to the whole-vocabulary grammar audit.
- [Directional label grammar](./directional-label-grammar.md) — adopted invariant that every directional identifier complete `source <label> target`, plus the initial pass/fail inventory and remaining migration debt.
- [Evidence label migration plan](./evidence-label-migration-plan.md) — compact execution packet for adopting `evidenced-by` / `is-evidence-for`, migrating active contracts and edges, verifying conservation, and capturing lessons for the next label.
- [Evidence label migration retrospective](./evidence-label-migration-retrospective.md) — completed first-run reconciliation and the mandatory add/remove/reorder/automate amendments the next directional-label migration must explicitly accept or reject.
- [Rationale label migration plan](./rationale-label-migration-plan.md) — next-run packet: test `rests-on` against the live `rationale` corpus and `grounds`, then migrate only after the decision gate passes while exercising the retrospective amendments.
- [Rationale label migration retrospective](./rationale-label-migration-retrospective.md) — capture second-run surprises and decide whether the migration procedure is stable enough to promote.

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
