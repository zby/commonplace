---
description: "Extends ADR 009 by promoting `contrasts` and `mechanism` into the link relationship vocabulary on corpus evidence, and explicitly declares the directional-asymmetry principle that governs how the vocabulary is authored and read."
type: kb/reference/types/adr.md
tags: []
status: proposed
---

# 018-Link vocabulary: add contrasts and mechanism; declare directional asymmetry

**Status:** proposed
**Date:** 2026-04-19
**Extends:** [ADR-009](../../reference/adr/009-link-relationship-semantics.md)

## Context

ADR 009 adopted a five-label vocabulary (`extends`, `grounds`/`foundation`, `contradicts`, `enables`, `exemplifies`/`example`) and committed to slow, evidence-driven expansion.

The [link-label audit](./findings.md) extracted every `- [title](path) — label:` footer annotation across `kb/**/*.md` (3420 matches, 32 source/target register pairs, 236 distinct labels). Most off-vocabulary labels fold into existing ADR 009 aliases — `sharpens`/`refines`/`clarifies` collapse into `extends`'s "refines" sense; `applies`/`instance` into `exemplifies`; `motivates` into `grounds`; `tension` into `contradicts`. Two candidates survive with genuine semantic daylight.

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

Promote two labels to the canonical vocabulary, bringing the total to seven:

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

### Label folds

The audit surfaced off-vocabulary labels that fold cleanly into existing canonical labels or aliases. These are recorded so authors drifting toward them are redirected rather than the vocabulary being extended:

- `sharpens`, `refines`, `clarifies` → `extends` (covers "builds on, adds a dimension to, refines")
- `motivates`, `rationale`, `justification` → `grounds`
- `applies`, `instance`, `application` → `exemplifies`
- `complements`, `consequence`, `sibling` → `extends` or `see-also` for pure navigation
- `tension`, `challenges` → `contradicts`

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

- ADR 009 remains canonical; this ADR extends rather than supersedes.
- Backlinks remain auto-computed; upstream notes are not required to carry forward links back to their users.
- The per-collection outbound tables in `COLLECTION.md` files are updated separately to list the new labels on edges where they fire.

### Update discipline

The operational distillation of this vocabulary is embedded inside `kb/instructions/cp-skill-write/SKILL.md` rather than living in a standalone library doc (to avoid drift from canon). Any future change to ADR 009 or ADR 018 that touches the vocabulary **must** re-sync that embedded section as part of the same edit.

---

Relevant Notes:

- [ADR 009 — link relationship semantics](../../reference/adr/009-link-relationship-semantics.md) — extended by this ADR; its five-label core stays canonical
- [linking theory](../../notes/linking-theory.md) — grounds: the decision-cost model this vocabulary instantiates
- [link-label-audit findings](./findings.md) — full analysis behind this decision
- [backlinks](../../notes/backlinks.md) — the inverse-view mechanism that makes directional asymmetry workable
