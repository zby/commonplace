---
description: "Adopts source-as-subject grammar for directional link identifiers and replaces evidence with evidenced-by and is-evidence-for"
type: ../types/adr.md
tags: []
status: accepted
---

# 058-Directional identifiers use the source as subject

**Status:** accepted
**Date:** 2026-07-28
**Amends:** [ADR 020](./020-theoretical-default-contrasts-mechanism.md)

## Context

Commonplace names every Markdown edge from the artifact containing the link (the source) to the linked artifact (the target), but its directional identifiers have mixed grammatical voices. Identifiers such as `extends`, `part-of`, and `derived-from` read as `source <label> target`; others describe the target's role and silently reverse the sentence. The old `evidence` label made the failure concrete: collection contracts and 207 active footer edges used one asymmetric identifier for both assertion→observation and observation→assertion journeys.

Corpus review established that both journeys help readers. Assertion→observation lets a reader inspect corroboration, qualification, or boundary evidence. Observation→assertion maps a source or review into the claims it bears on, including cases where the target has not cited or incorporated it. Twenty-six active edges used this inverse journey, nineteen without a target-side return edge, so removing it or requiring reciprocity would discard authored information.

## Decision

Every directional relationship identifier must complete the assertion `source <label> target`, with the source artifact as grammatical subject. Omitted helper verbs remain acceptable when they do not swap endpoints (`part-of`, `defined-in`, `derived-from`). Each catalogue entry must state a source→target assertion template as well as its reader need. Pre-existing identifiers that fail this invariant retain their declared semantics only as explicit migration debt; they are migrated in separate, scoped runs rather than being silently reinterpreted.

The ambiguous `evidence` identifier is retired and replaced by an inverse pair:

- `source evidenced-by target` — the target observation or source bears on the source assertion as corroboration, qualification, or boundary evidence;
- `source is-evidence-for target` — the source observation or review bears materially on the target assertion, without claiming that the target already cites, incorporates, or accepts it.

Both relationships are asymmetric. Either direction is authored only when its own reader journey is useful. One edge never creates an obligation to author, preserve, or remove its inverse.

The shared catalogue, every affected `COLLECTION.md`, current authoring guidance, and all mutable active old-label footers change together. Source→destination authorizations follow actual honest uses, including evidence-bearing theoretical notes, shipped type/reference artifacts, and external sources; collection profile alone does not decide whether a target can bear evidence.

Operativity path: `cp-skill-write` and `cp-skill-connect` load each source collection's `COLLECTION.md` with binding force; collection authors consult the shared catalogue; current examples teach the same pair; and the migrated footer corpus makes readers encounter the new grammar in use.

## Considered alternatives

**Keep `evidence` for assertion→observation and add `evidence-for` for the inverse.** Rejected because the pair still mixes a target-role noun with an apparently source-subject predicate. Without the invariant, `source evidence-for target` remained open to the same endpoint confusion.

**Redefine `evidence` as direction-neutral.** Rejected because the underlying relationship is not self-dual. “The claim points to evidence” and “the source bears on the claim” create different assertions and maintenance signals even when both edges happen to be useful.

**Remove observation→assertion edges.** Rejected because the 26-edge cohort recurs across source ingests, source reviews, and an external-system review. Most lack a reciprocal edge, demonstrating an independent source-side landing-map need rather than accidental mirroring.

**Require reciprocal pairs.** Rejected because authoring is selective by reader need. Mandatory mirroring would add maintenance load and would falsely imply target-side uptake in source-side cases recorded precisely before that uptake occurs.

**Migrate every identifier that fails the invariant now.** Rejected to keep semantic review bounded. `grounds`, `enables`, `mechanism`, `rationale`, `procedure`, and `precondition` require their own corpus and neighboring-label audits; this decision makes their state visible without changing their meaning or edges in the evidence migration.

## Consequences

Readers can interpret both new identifiers directly from source to target, and ingestion can record where evidence lands without pretending the target already uses it. Collection contracts now authorize the pair on every source→destination path in the migrated corpus. Reciprocal links remain curated rather than generated.

The vocabulary temporarily contains older identifiers whose declared semantics fail the adopted grammar. That inconsistency is deliberate migration debt, not permission for new identifiers to use target-role voice. Each later directional-label migration must preserve edge conservation, independently review inverse journeys, and update its contracts and corpus together.

---

Relevant Notes:

- [ADR 019 — collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) — rationale: collection contracts remain the authoritative per-source authorization surface
- [ADR 020 — directional asymmetry](./020-theoretical-default-contrasts-mechanism.md) — amended-by: retains selective asymmetric authoring while this decision fixes identifier grammar
- [Link vocabulary](../link-vocabulary.md) — implements: catalogue assertion templates and reader needs for the adopted pair
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) — rationale: each authored direction must satisfy an independent reader need
