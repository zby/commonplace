---
description: Each COLLECTION.md owns its outbound-linking rules per destination collection, selecting from a shared authoring catalogue; the connect and write skills read COLLECTION.md directly, and the compiled register-by-register topology is retired
type: ../types/adr.md
tags: []
status: accepted
---

# 019-Collection-owned link vocabulary with per-destination outbound rules

**Status:** accepted
**Date:** 2026-04-22
**Extends:** [ADR-009](./009-link-relationship-semantics.md), [ADR-017](./017-collection-md-is-the-register-convention-boundary.md)

## Context

ADR 009 adopted a small universal link vocabulary (`extends`, `grounds`, `contradicts`, `enables`, `exemplifies`). ADR 017 made `COLLECTION.md` the register convention boundary, including outbound-linking rules. In the year since, three pressures accumulated against the "one universal vocabulary per register, narrowed per edge" arrangement:

1. **Per-destination needs diverge within a register.** `kb/notes/ → kb/reference/` and `kb/notes/ → kb/agent-memory-systems/` both target descriptive collections, but the reader-needs differ: the first wants architecture grounding and operational context, the second wants per-system evidence for theoretical claims. A register-to-register rule can't distinguish them.
2. **The compiled topology drifted.** `cp-skill-connect` reads `kb/reports/collection-topology.md`, a register × register matrix built by `cp-skill-compile-collections` from each `COLLECTION.md`'s outbound table. The compiled form loses per-destination fidelity and lags the source files.
3. **Label theory is weak.** The [link-label audit](../../notes/links-encode-conditional-possibilities-not-obligations.md) finds that labels earn their place only when they name a specific reader-need. A single universal vocabulary commits every collection to the same reader-need taxonomy regardless of what its readers actually want; per-destination rules let collections experiment.

A label-by-label audit (closed out in this ADR and the catalogue) retrofitted every label in the current and proposed vocabularies against the reader-need test. Results: drop `cross-reference` (no specific need); merge `rationale` + `justification` into `rationale` (same need, source register recoverable from the graph); fold `describes` into `part-of` or `see-also` per case. The corpus the audit ran on is the [link-vocabulary report](../link-vocabulary.md).

## Decision

`COLLECTION.md` owns outbound-linking rules for its source collection, organised **per destination collection**. A shared catalogue at `kb/reference/link-vocabulary.md` gives `COLLECTION.md` authors a palette of labels to pick from.

### Three layers, collection-owned

- **Collection grammar** — `COLLECTION.md`, authoritative and self-contained. Outbound-linking section is organised per destination: one block per destination collection the source may link to. Each destination block declares (a) search guidance for agents prospecting link targets, and (b) authorised labels with collection-specific reader-need context.
- **Authoring resource** — [`link-vocabulary.md`](../link-vocabulary.md): label catalogue plus authoring guidance for `COLLECTION.md` authors. Note writers do not read it; the connect skill does not read it.
- **Type-specific overrides** — only for specialised types that genuinely diverge from the collection convention (`definition`, `index`, `adr`). Owned by the type definition, not `COLLECTION.md`.

### Collection, not register, is the anchor

Register groupings in the catalogue are advisory — they help an author find labels that match a source's shape. Authoritative rules live in each source's `COLLECTION.md`. For the writer authoring a note there is one source of truth: the `COLLECTION.md` of their collection. No upward traversal. Role stays a read-time concern and doesn't anchor anywhere.

### Per-destination organisation

Outbound blocks are grouped by destination collection. Each destination block serves two consumers:

1. **The connect skill** — a concrete map of where to prospect for link targets and what labels it may propose.
2. **Note writers** — authoritative list of labels and reader-needs for links to that destination.

Per-destination rules enable fine-grained experimentation: `kb/notes/ → kb/reference/` can diverge from `kb/notes/ → kb/agent-memory-systems/`, even though both destinations share the descriptive register.

### Labels must name reader-needs

Every label in an authorised set must pass the articulation test: *"a reader who would follow this label is one who [wants to / needs to] ___."* Labels that describe document relationships without naming a reader-need are weaker and should be cut or replaced. See [links-encode-conditional-possibilities-not-obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) for the theory.

Audit outcomes applied to the library drafts:

- Drop: `cross-reference`.
- Merge: `rationale` + `justification` → `rationale`. Source register is recoverable from the authoring collection.
- Fold: `describes` → `part-of` or `see-also` per case.

### Consumer skills read `COLLECTION.md` directly

- **`cp-skill-connect`** reads the source `COLLECTION.md`, enumerates destination blocks, applies each block's search guidance when prospecting, and labels candidates from the destination's authorised set. No compiled topology. Candidates that pass the articulation test but lack an authorised label are reported as off-authorisation signal for the collection author.
- **`cp-skill-write`** reads the source `COLLECTION.md`'s outbound rules as the authoritative label and reader-need reference. The skill teaches the link mechanics (position, articulation test, label grammar) but does not embed a label list.

### Retirements

- `kb/reports/collection-topology.md` — compiled matrix, obsolete under per-destination.
- `cp-skill-compile-collections` — its only consumer retires.
- The embedded five-label list in `cp-skill-write/SKILL.md` — replaced by a pointer to `COLLECTION.md`.

## Consequences

### Easier

- **Fine-grained experimentation.** A collection can differentiate how it links to two destinations of the same register without editing a global vocabulary.
- **Single source of truth per collection.** Writers and the connect skill read one file. No matrix, no catalogue lookup, no writing-skill embedded vocabulary to keep in sync.
- **Live reads remove drift.** No compile step between the rules and the skills that use them.
- **Off-authorisation as signal.** Connect reports candidates that don't fit any authorised label, which gives the collection author a concrete driver for extending the authorisation. The authorisation boundary becomes a designed surface rather than an accident.

### Harder

- **Each `COLLECTION.md` gets longer.** A destination block per active destination plus the search guidance and label table is more text than a single outbound table covering all destinations at register granularity.
- **New collections need up-front design.** A fresh collection can't fall back on a register-level default; it must declare its outbound destinations explicitly. The catalogue cushions this by suggesting starter sets.
- **Consistency across collections is softer.** Two collections linking to the same destination may authorise different labels. This is intentional — experimentation is the point — but readers crossing collection boundaries may see different vocabularies for apparently similar edges.
- **Parsing `COLLECTION.md`.** The connect and write skills rely on model interpretation of the outbound section rather than a structured schema. If parsing becomes brittle, a later ADR may introduce a machine-readable block; for v1 the live-read + model interpretation is the trade.

### Not changing

- ADR 009's core vocabulary remains the theoretical default; `kb/notes/` adopts it (extended by ADR 020) via its `COLLECTION.md`.
- ADR 017's boundary — `COLLECTION.md` owns register conventions — stands; this ADR specifies the internal structure of the outbound-linking section that `COLLECTION.md` owns.
- Type definitions (`definition`, `index`, `adr`) remain free to override collection conventions for types whose linking behaviour genuinely differs.
- The articulation test, inline-vs-footer positions, and path-must-resolve rules are unchanged.

## Relevant Notes

- [ADR-009: link relationship semantics](./009-link-relationship-semantics.md) — foundation: the core vocabulary that this ADR scopes per collection
- [ADR-017: COLLECTION.md is the register convention boundary](./017-collection-md-is-the-register-convention-boundary.md) — foundation: the convention boundary this ADR specifies the internal structure of
- [ADR-020: theoretical-default additions — contrasts and mechanism](./020-theoretical-default-contrasts-mechanism.md) — extends ADR 009 within the theoretical default template this ADR scopes
- [Links encode conditional possibilities, not obligations](../../notes/links-encode-conditional-possibilities-not-obligations.md) — grounds: the reader-need theory the label discipline rests on
- [Register](../../notes/definitions/text-contract.md) — defined-in: content-mode groupings used to organise the catalogue
- [link-vocabulary.md](../link-vocabulary.md) — the catalogue that COLLECTION.md authors consult
