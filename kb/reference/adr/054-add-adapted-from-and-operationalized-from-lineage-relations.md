---
description: "Adds adapted-from and operationalized-from lineage relations, amending ADR 053's no-successor-term decision with the composite operation it left unnamed"
type: ../types/adr.md
tags: []
status: accepted
---

# 054-Add adapted-from and operationalized-from lineage relations

**Status:** accepted
**Date:** 2026-07-18

## Context

[ADR 053](./053-retire-distillation-without-a-successor-term.md) retired `distillation` with deliberately no successor technical term, on the reasoning that the KB's link grammar (`derived-from`/`abstracted-from`) already carried the maintenance-relevant boundary and a bare successor word would fail the minimality bar. Its own Consequences section named the resulting gap: "the KB's most common composite operation — consumer-directed selection plus reshaping — no longer has a one-word name."

The `adaptation-lineage-vocabulary` workshop's migration audit found that gap was real, not hypothetical. Writers filled it with unauthorized ad-hoc synonyms — "condense"/"condensing" reintroduced as an unacknowledged peer operator in four notes, and a separately coined "Extraction" successor term — inside the same migration that retired `distillation` for exactly this failure mode ("the control trap can recur under any future attractive label," per ADR 053's own risk note); neither term made it into ADR 053, the migration plan, or `AGENTS.md`'s vocabulary list. Separately, the audit found the migration's own flagship `derived-from` case (`skills-derive-from-methodology.md`, cited from ~15 other notes) argues itself into the claim-preserving bucket while its own text admits "a different person reading the same methodology would produce a meaningfully different skill" — evidence of judgment-shaped reworking, not strict derivation.

## Decision

Introduce two lineage relations, alongside `derived-from`/`abstracted-from`, to name this composite operation without reopening ADR 053's other three decisions:

- **`adapted-from`** / `Adapted into:` — the general relation for consumer-directed selection-plus-reshaping that is neither claim-preserving (`derived-from`) nor claim-amplifying (`abstracted-from`). Truth condition, test, and maintenance consequence: [link-vocabulary.md](../link-vocabulary.md).
- **`operationalized-from`** / `Operationalized into:` — a narrower, flat authoring-time *alternative* to `adapted-from` (never a stacked child edge) for the methodology → procedure pairing specifically, where the target adds ordering, defaults, or stopping conditions the source doesn't fix, without new substantive claims.

`derived-from` is clarified, not changed in substance: its authorization is tested per source→destination pairing against its entailment condition, declared in the source's `COLLECTION.md` — not banned by register, and not assumed available either.

Recording direction: the persisted edge is always the source-side footer. Authorization sits with the *source* collection's `COLLECTION.md`, per [ADR 019](./019-collection-owned-link-vocabulary.md)'s existing outbound-link architecture — `link-vocabulary.md` is a palette, not itself authoritative.

`generated-from` (canonical artifact → mechanically-reproducible projection) was considered and deliberately not minted: no live case of a *persisted* artifact needs it yet.

ADR 053's other three decisions are unchanged: "derive" stays ordinary English with no vocabulary entry; ampliative traffic still routes through the discovery lifecycle; `distillation` still survives only in external-system and historical-ADR senses.

Implemented: catalogue rows and full lineage-semantics section in [link-vocabulary.md](../link-vocabulary.md); `operationalized-from` authorized in `kb/notes/COLLECTION.md` for its `kb/instructions/` destination (the one pairing with live corpus evidence — `adapted-from` stays unauthorized everywhere until a real case identifies its actual source collection); the four-way lineage-tracking test in `cp-skill-write/SKILL.md`; the hyphenated-identifier-vs-prose convention in `AGENTS.md` (this repo's terms) and `AGENTS.md.template` (generic, no hardcoded terms).

## Consequences

- **Easier:** the composite operation ADR 053 left unnamed now has two relations with distinct maintenance semantics; corpus cases like `skills-derive-from-methodology.md` can be correctly classified as judgment-shaped rather than forced into `derived-from` or left to accumulate ad hoc synonyms.
- **Harder:** four lineage tests to learn instead of two. Mitigated by keeping `cp-skill-write`'s own statement terse (names the four headings, defers the actual tests to `link-vocabulary.md`) rather than inlining every test at the write path.
- **Corpus corrections (execution-plan §4, complete):** `skills-derive-from-methodology.md` and `write-instruction.md` reclassified — the audit showed the latter has *two* distinct provenance stories (repeated practice → `abstracted-from`, methodology → `operationalized-from`), not one mislabeled edge; `kb/work/lineage-mechanisms/`'s six "ad-hoc distillation" passages resolved per case, not by blanket substitution; a corpus-wide `Derived into:` sweep for methodology→procedure targets; the Finding 1 ("condense"/"condensing") and Finding 2 (trace-rework language, probe-checklist wording) reconciliations; `constraining.md` and `context-engineering.md` updated. The reported 70+ generated "Extraction" footers could not be reproduced — no emitter exists in `scripts/`, `src/`, or `kb/instructions/`, and the cited commit's diff is unrelated rename/backlink maintenance — so no generator fix was made; the claim is retained in `migration-audit-findings.md` as an unreproduced historical report, not acted on further.
- **Risk:** the same recurrence risk ADR 053 named — and it recurred within the very migration that fixed the last instance. Considered and rejected a write-time gate in `cp-skill-write` against this: the actual failure was ordinary-English peer-operator words ("condense," "Extraction"), which no fixed check can catch prospectively since the next escape word isn't known in advance, and the hyphenated-identifier discipline this ADR extends was never what failed. Enforcement stays with periodic audit — the same mechanism that caught this instance.
