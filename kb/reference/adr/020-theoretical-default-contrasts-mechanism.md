---
description: "Adds `contrasts` and `mechanism` to the theoretical-register default template on corpus evidence, and declares the directional-asymmetry principle that governs how the theoretical vocabulary is authored and read."
type: ../types/adr.md
tags: []
status: accepted
---

# 020-Link vocabulary: add contrasts and mechanism; declare directional asymmetry

**Status:** accepted
**Date:** 2026-04-19
**Extends:** [ADR-009](./009-link-relationship-semantics.md)
**Depends on:** [ADR-019](./019-collection-owned-link-vocabulary.md)

**Scope.** This ADR's additions land in the theoretical-register default template (recorded in the catalogue at [`link-vocabulary.md`](../link-vocabulary.md)) and are adopted by collections whose `COLLECTION.md` includes them in its authorised sets. Cross-register labels (`rationale`, `evidence`, `procedure`, `operates-on`, `defined-in`) are a separate concern handled by the catalogue and selected per destination in each `COLLECTION.md`; this ADR does not speak to them.

## Context

ADR 009 adopted a five-label vocabulary (`extends`, `grounds`/`foundation`, `contradicts`, `enables`, `exemplifies`/`example`) and committed to slow, evidence-driven expansion.

A one-off audit extracted every `- [title](path) — label:` footer annotation across `kb/**/*.md` (3420 matches, 32 source/target register pairs, 236 distinct labels). The extraction was done with a throwaway Python script that walked the KB and classified labels by source/target collection; the script has since been retired, with the snapshot it produced preserved at [`kb/reports/link-vocabulary.md`](../../reports/link-vocabulary.md) as evidence. Most off-vocabulary labels fold into existing ADR 009 aliases — `sharpens`/`refines`/`clarifies` collapse into `extends`'s "refines" sense; `applies`/`instance` into `exemplifies`; `motivates` into `grounds`; `tension` into `contradicts`. Two candidates survive with genuine semantic daylight.

### `contrasts` occupies a slot no ADR 009 label covers

Authors use `contrasts` (~150 occurrences) to name a difference between peers *without claiming either is wrong*: "ACE performs bullet-level operations with helpful/harmful counters on an addressable playbook; Dynamic Cheatsheet performs whole-document rewrite on an unaddressable blob." Neither is incorrect — they sit on different points of a named axis. `contradicts` is too strong (implies conflict forcing resolution); `exemplifies` and `extends` are directional when the relationship is peer-level.

The `agent-memory-systems/` reviews rely on `contrasts` to map the landscape of similar-but-different systems (descriptive → descriptive: 47, descriptive → theoretical: 77). Folding it into `contradicts` would mislead readers arriving expecting resolution and getting parallel design choices instead.

### `mechanism` is distinct from `grounds`

`grounds` answers *"on what premises?"* — the target is the theoretical or evidential base. `mechanism` answers *"by what operation?"* — the target is the operational principle or machinery that makes the source's claim work.

Register usage reinforces the split. `grounds` is a cross-register upward move: ~71% of its occurrences terminate in a theoretical note, with sources in every register (descriptive → theoretical: 18, source → theoretical: 23, managed → theoretical: 7, workshop → theoretical: 3, theoretical → theoretical: 80, etc.). `mechanism` stays within the theoretical layer: 31 theoretical→theoretical, 18 workshop→workshop, 4 workshop→theoretical, zero uses with descriptive, source, or managed as the *source*.

Decision-cost argument from [`linking-theory.md`](../../notes/linking-theory.md): a reader following `grounds` wants to verify the claim's justification; a reader following `mechanism` wants to understand how the claim operates. Different reader needs, different follow/skip choices.

### ADR 009 has an implicit directional rule worth stating

The audit also surfaced that ADR 009's vocabulary is directionally asymmetric by design: most labels point *upstream* from source to target, one target typically has many downstream users linking up, and the inverse view is the auto-computed backlinks view rather than a manually-maintained set of forward edges. Leaving this implicit risks future label proposals drifting toward "every forward needs a paired backward" — which doesn't match the fan-out structure and would impose maintenance load that doesn't scale.

## Decision

### Additions

Add two labels to the theoretical-register default template. Collections adopting that template (currently `kb/notes/`) will surface these for authoring; collections with their own declared grammar pick them up only if their `COLLECTION.md` authors opt in.

- **contrasts** — names a difference between peers on a specified axis, without claiming either is wrong. Self-dual.
- **mechanism** — target is the operational principle or machinery that makes the source's claim work. Upstream-pointing (target is more operationally fundamental than source).

### Directional asymmetry principle

The vocabulary splits into two classes by directional shape. New label proposals must fit one of these shapes.

**Asymmetric labels (forward-authored, backward-derived; 1:many fan-out):**

| label | forward semantics |
|---|---|
| `extends` | source builds on target |
| `grounds` (also `foundation`) | target is source's theoretical / evidential base |
| `enables` | target is source's operational prerequisite |
| `exemplifies` (also `example`) | source is a concrete instance of target |
| `mechanism` | target is source's operational engine |

Each label points *upstream* (toward more fundamental, more general, or more foundational content). Each upstream note typically accumulates many incoming links — so the upstream note cannot, and should not, maintain forward links back to all of them. The forward edge from the downstream side is the canonical representation. The upstream view is the auto-computed backlinks view ([backlinks.md](../../notes/backlinks.md)).

**Symmetric labels (self-dual; either end may author):**

| label | forward semantics |
|---|---|
| `contradicts` | A conflicts with B ⟺ B conflicts with A |
| `contrasts` | A and B differ on axis X ⟺ same from B's vantage |

These are pair-level relationships with low fan-out. Both ends may legitimately mark them from their own vantage without creating clutter.

### Curated back-links remain allowed

Upstream notes *may* link downstream selectively — to index a canonical application, to pin a key example, to flag a known tension. This is editorial curation, not inverse-duty. It does not scale with fan-out and is a conscious per-note decision.

### Label folds (theoretical defaults)

The audit surfaced off-vocabulary labels that fold cleanly into existing theoretical-default labels or aliases. These are recorded so authors drifting toward them are redirected:

- `sharpens`, `refines`, `clarifies` → `extends` (covers "builds on, adds a dimension to, refines")
- `motivates` → `grounds`
- `applies`, `instance`, `application` → `exemplifies`
- `complements`, `consequence`, `sibling` → `extends` or `see-also` for pure navigation
- `tension`, `challenges` → `contradicts`

Not folded: `rationale` and `justification` are **kept distinct** in the catalogue as cross-register labels (descriptive / prescriptive → theoretical, with the reader-need *"why does this design/rule exist?"*). They do not collapse into `grounds`, which is intra-theoretical.

## Consequences

### Easier

- **Review landscape mapping.** The descriptive register can now name peer differences accurately without overloading `contradicts` or stretching `extends`.
- **Operational-vs-epistemic distinction.** Readers following `mechanism` and readers following `grounds` get different kinds of support, matching different decision needs.
- **Future label decisions.** The directional-asymmetry principle gives a test: does the proposed label fit an asymmetric (upstream-pointing) or symmetric (pair-level) shape? If neither, it's probably a synonym or a prose hedge.

### Harder

- **Vocabulary is now seven, not five.** Authoring cost is slightly higher; picking the right label requires slightly more discrimination.
- **`contrasts` vs `contradicts` boundary.** Authors must distinguish "differs on an axis" from "conflicts with". Test: if the reader would follow the link expecting to resolve a disagreement, the label is `contradicts`; if expecting to understand the neighbour's shape, it is `contrasts`.
- **`mechanism` vs `grounds` boundary.** Both are upstream-pointing. Test: if the reader would follow to *verify* the claim's justification, the label is `grounds`; if to *understand how it works* operationally, it is `mechanism`.

### Not changing

- ADR 009's decisions for the theoretical default remain in force; this ADR extends rather than supersedes.
- Backlinks remain auto-computed; upstream notes are not required to carry forward links back to their users.
- Per-destination outbound blocks in each `COLLECTION.md` are updated separately to list the new labels on edges where they fire.

### Update discipline

The operational distillation of this vocabulary lives in the [`link-vocabulary.md`](../link-vocabulary.md) catalogue, which `COLLECTION.md` authors consult when authoring outbound rules. Authoritative per-source rules live in each `COLLECTION.md`'s outbound-linking section. Note writers and the connect skill read only the collection's `COLLECTION.md` — they do not read the catalogue. Any future change to ADR 009 or ADR 020 that touches the theoretical default **must** re-sync the catalogue *and* any `COLLECTION.md` files whose authorised labels reflect the change, in the same edit.

---

Relevant Notes:

- [ADR 009 — link relationship semantics](./009-link-relationship-semantics.md) — extended by this ADR; its five-label core stays canonical
- [ADR 019 — collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) — depends-on: this ADR's additions land inside the architecture ADR 019 specifies
- [linking theory](../../notes/linking-theory.md) — grounds: the decision-cost model this vocabulary instantiates
- [link-vocabulary report](../../reports/link-vocabulary.md) — frozen audit snapshot the analysis behind this decision was derived from
- [backlinks](../../notes/backlinks.md) — the inverse-view mechanism that makes directional asymmetry workable
