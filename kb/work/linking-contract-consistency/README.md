# Linking contract consistency

## Purpose

Reconcile Commonplace's declared linking architecture with its live collection contracts, authoring procedures, validator, and reader surfaces. The immediate trigger is a cross-collection audit that found accepted decisions, shared vocabulary, collection-local rules, and executable procedures describing different systems.

Lineage-specific carrier, relation, and invalidation contradictions stay in the sibling [lineage mechanisms ledger](../lineage-mechanisms/current-contradictions.md). This workshop owns the remainder: navigation links, relationship-label direction outside lineage, collection grammar, reciprocal-link procedure, validation, and inbound-link delivery.

## Working files

- [Current link-authorization matrix](./current-authorization-matrix.md) — inventory of every live collection contract, its source→destination label authorizations, grammar shape, and cross-contract conflicts; ends with `evidence` as the first decision packet.
- [Evidence direction review](./evidence-direction-review.md) — corpus review of 26 source/review→note uses; establishes a real inverse reader journey while deferring its identifier to the whole-vocabulary grammar audit.
- [Directional label grammar](./directional-label-grammar.md) — candidate invariant that every directional identifier complete `source <label> target`, plus the initial pass/fail inventory and required audit procedure.
- [Evidence label migration plan](./evidence-label-migration-plan.md) — compact execution packet for adopting `evidenced-by` / `is-evidence-for`, migrating active contracts and edges, verifying conservation, and capturing lessons for the next label.
- [Evidence label migration retrospective](./evidence-label-migration-retrospective.md) — run-time surprise log, edge reconciliation, and mandatory add/remove/reorder/automate amendments for the next label plan.

## Confirmed contradictions

### ADR 009 still presents a global five-label vocabulary

[ADR 009](../../reference/adr/009-link-relationship-semantics.md) says every KB link must use one of five relationship types. The live architecture is collection-owned under [ADR 019](../../reference/adr/019-collection-owned-link-vocabulary.md), and current collections authorize many later labels. ADR 020 extends the theoretical defaults but does not qualify ADR 009's global sentence.

**Needed outcome:** amend, partially supersede, or explicitly scope ADR 009 so readers can tell which parts remain current.

### Required collection grammar and accepted working formats disagree

ADR 019 and the [shared authoring guide](../../reference/link-vocabulary.md#authoring-collection-link-rules) require one outbound block per destination collection, with search guidance and authorized labels. Several main collections instead use one scan paragraph plus a labels table. The [writing skill](../../instructions/cp-skill-write/SKILL.md#step-2---load-collection-conventions) already accepts per-destination blocks, a table, or prose.

**Needed outcome:** either make per-destination semantics the requirement while allowing multiple serializations, or migrate contracts and procedures to the stricter block form.

### Some writable collections have no complete outbound-link contract

The [article collection](../../articles/COLLECTION.md) deliberately permits in-prose links while forbidding footer labels, but it does not declare authorized destinations or formalize this as a specialized linking override. The illustrative [dialectical sample collection](../dialectical-sample/COLLECTION.md) requires source-span citations but has no outbound-link section at all.

**Needed outcome:** give each collection an operational grammar or an explicit exemption that writing and connect procedures know how to interpret.

### `evidence` is used against its declared direction

The shared catalogue describes `evidence` as asymmetric, theoretical → descriptive. The sources collection authorizes it from source analyses → notes, and the agent-memory collection authorizes a rare review → note use. Those may express a valid inverse reader need, but the same asymmetric identifier currently names both directions.

**Needed outcome:** choose a canonical direction, introduce an inverse label if both journeys matter, or redefine the label as a source-independent reader-need relation whose semantics genuinely survive inversion.

### `compares-with` has stale scope documentation

The shared catalogue calls `compares-with` specific to `kb/agent-memory-systems/`, while source and agentic-system contracts also authorize it.

**Needed outcome:** update its declared scope and decide whether it is now a general descriptive/source comparison relation.

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
