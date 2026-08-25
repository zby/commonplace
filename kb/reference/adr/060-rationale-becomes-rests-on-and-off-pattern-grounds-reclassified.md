---
description: "Replaces rationale with source-as-subject rests-on, reclassifies every off-pattern grounds edge, and gives the global type surface collection-owned link authorization"
type: ../types/adr.md
tags: []
status: accepted
---

# 060-Rationale becomes rests-on and off-pattern grounds are reclassified

**Status:** accepted
**Date:** 2026-07-28
**Amends:** [ADR 019](./019-collection-owned-link-vocabulary.md), [ADR 020](./020-theoretical-default-contrasts-mechanism.md), and [ADR 058](./058-directional-identifiers-use-source-as-subject.md)

## Context

[ADR 058](./058-directional-identifiers-use-source-as-subject.md) requires every directional identifier to complete `source <label> target`. `rationale` instead names the target's role: its intended assertion is that a descriptive or prescriptive source rests on a theoretical target. `grounds` has the same grammatical defect, but its intended note→note premise-verification journey is distinct.

A corpus review classified all 134 active `rationale` edges: 114 are genuine design/rule dependencies, 2 are source-side evidence, and 18 are evidence or architecture/history relations. A separate adjudication classified the 38 `grounds` edges outside the canonical note→note cohort.

The review also exposed three authorization gaps: agentic-system analysis→note evidence, source analysis→agent-memory evidence, and three theoretical dependencies authored under `kb/types/`, which had no source collection contract.

## Decision

Retire the directional identifier `rationale` and adopt:

> `source rests-on target`

`rests-on` is asymmetric. It asserts that the source design, description, procedure, rule, or system-definition artifact depends on the target theoretical claim: rejecting or materially changing the target triggers reconsideration of the source. It is not a generic dependency, implementation, provenance, or evidence relation.

Keep the canonical note→note `grounds` cohort semantically distinct and unchanged in this migration. Its reader follows a theoretical assertion to assess its premise; its own source-as-subject identifier requires a later scoped review.

Every `rationale` edge and every off-pattern `grounds` edge is reclassified to the relation its assertion actually makes — `rests-on`, `evidenced-by`, `is-evidence-for`, `implements`, or `compares-with` — as individually adjudicated; none are removed.

Collection contracts replace `rationale` authorization with `rests-on` rather than retaining synonyms, gain `is-evidence-for` only where the source-side evidence journey was observed, and are not widened to authorize off-pattern `grounds`.

`kb/types/` becomes a collection by gaining a minimal `COLLECTION.md`. It remains the global type layer; the collection contract governs text-level authoring and outbound links, while each type spec and schema continue to own type semantics. This removes the missing-source-contract exception instead of making the self-referential root type authorize its own links.

Operativity path: `cp-skill-write` and `cp-skill-connect` load the source `COLLECTION.md`; collection authors consult the shared catalogue; type-spec authors now load `kb/types/COLLECTION.md`; and the migrated active footer corpus teaches the same assertions in use.

## Considered alternatives

**Rename every `rationale` edge to `rests-on`.** Rejected because 20 of 134 edges assert evidence, implementation, comparison, or decision history rather than theoretical dependency.

**Merge `rationale` and `grounds` into one identifier.** Rejected because 114 cross-register design/rule dependencies and 276 note→note premise-verification edges repeatedly create different follow and maintenance decisions. The 38 off-pattern `grounds` rows are drift, not evidence for merging.

**Authorize the live off-pattern `grounds` pairings.** Rejected because their assertions resolve cleanly to evidence or `rests-on`. Widening contracts would make historical drift authoritative.

**Let the root type spec authorize links for `kb/types/`.** Rejected because it would preserve a source-directory exception to collection-owned authorization and make a type contract govern its own routing. A minimal collection contract keeps type semantics and text/link governance separate.

**Remove weak boundary links.** Rejected after individual adjudication: every boundary edge has an articulated formal reader need under an existing or adopted relation.

Deciding forces were direct source-as-subject grammar, tuple conservation, stable reader journeys, and one authorization owner per source collection. The free choice was whether `kb/types/` should remain an exception; the migration resolves it in favor of uniform collection ownership.

## Consequences

Readers can interpret `rests-on` without silently reversing endpoints, and maintainers can distinguish design reconsideration from premise verification and evidence inspection. The canonical `grounds` cohort remains visible migration debt rather than being silently reinterpreted.

The global type layer now participates in collection routing and collection-conformance review. Adding or changing a global type must compose `kb/types/COLLECTION.md` with the type-spec contract, just as other authored artifacts compose collection and type contracts.

---

Relevant Notes:

- [Directional identifiers use the source as subject](./058-directional-identifiers-use-source-as-subject.md) — implements: the grammar invariant this migration applies
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) — rests-on: the independent reader-need test separating rationale, premise, and evidence journeys
- [Collection](../definitions/collection.md) — defined-in: the authoring-contract boundary now applied to the global type surface
