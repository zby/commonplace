---
description: "Proposal: cap a review gate's link-following by bytes loaded rather than by number of links, so the budget measures the resource it protects and needs no evidence-class rules"
type: ../types/design-proposal.md
tags: []
---

# Review link budget measured in bytes

`semantic/grounding-alignment` limits how much linked material a reviewer may
open. It expresses that limit as a count of links. The resource it protects is
the material actually loaded, and links are a poor proxy for it: they vary by
two orders of magnitude in size, and the same artifact linked twice costs
nothing the second time.

## Current state (as of 2026-08-25)

The gate says:

> For linked notes and ordinary linked sources, read the linked material and
> follow at most five links in total. For a direct link to a tracked
> `kb/sources/<slug>.ingest.md`, use one of these two routes: …

Three defects follow from counting links, all observed rather than predicted:

- **Occurrences are counted, not artifacts.** 239 of 314 linked notes (76%)
  repeat a link target, and 45 carry more than five occurrences across five or
  fewer distinct targets — the worst at 11 occurrences over 5 targets. A
  reviewer exhausts its budget for no saving.
- **The number is unexamined.** Five appears inherited rather than derived.
  Measured: the `(snapshot required)` route in review job 8051 loaded a 128 KB
  snapshot ≈ 32k tokens inside an 88k-token job covering the gate, the note, and
  all five links. Corpus snapshots run 23 KB median, 112 KB p90, 456 KB max.
  Following links is not the expensive operation the cap appears to assume.
- **Scope is ambiguous.** The cap is stated for "linked notes and ordinary
  linked sources"; ingests are then introduced as a separate category without
  saying whether they draw on the same budget. Job 8051's reviewer assumed they
  do. On the note it reviewed — 4 ingest links and 5 internal — that assumption
  cost exactly four unchecked internal links, where the other reading would have
  covered the whole note.

Editing the gate stales 775 review pairs as `criterion-changed`.

## The proposal

Express the budget in bytes of linked material loaded, and keep it global across
every link kind.

This is a simplification, not an addition. Each defect above dissolves rather
than needing its own rule:

- **Repeated links stop mattering.** Material already loaded costs no further
  bytes, so no distinct-artifact counting rule is needed.
- **Heterogeneous sizes are priced correctly.** Five 3 KB snapshots and five
  456 KB snapshots stop being the same budget.
- **No evidence classes.** A reviewer holding a byte budget spends it where it is
  most informative without a rule ranking source links above internal ones. An
  earlier sketch proposed exactly such a ranking; a byte cap makes it
  unnecessary, and one fewer classification rule is worth more than a marginally
  better default ordering.

## Forces

**Bytes are a proxy too, and the second-order question is what the cap protects.**
If it protects context, bytes are close to right. If it protects reviewer
attention, ten small artifacts may cost more than one large one, and a count is
the better proxy. This proposal assumes context; that assumption should be stated
and can be wrong.

**Bytes are not tokens, and the ratio moves with content.** Equation-heavy
snapshots, tables, and code tokenize far worse than prose. A byte figure will
under-price exactly the sources whose extraction artifacts already cause trouble.

**A reviewer must size before opening.** Under a count, budgeting needs no
lookahead. Under a byte cap the reviewer has to check sizes first, which is cheap
but must be stated, or the rule is unfollowable in the order a reviewer works.

**Partial reads complicate the accounting.** The Quotes route reads one section,
not a whole ingest. Whether the budget charges the artifact or the portion read
changes the arithmetic and needs deciding.

**Disclosure matters more than the number.** Job 8051 passed while naming the
four links it did not open, which is what keeps a sampled verdict honest. Any
budget must keep that requirement; a larger budget without disclosure would be
worse than a smaller one with it.

## Options

**A. Byte cap, global.** Replaces the count outright. Operativity: one gate-file
edit; the reviewer sizes candidates, spends the budget, discloses what it
skipped.

**B. Token cap.** Prices the real constraint rather than a proxy for it, at the
cost of a figure a reviewer cannot compute without a tokenizer.

**C. Keep the count, fix only the counting.** Cheapest, and leaves the number
unexamined and heterogeneity unpriced.

**D. Byte cap plus a floor on artifacts.** Guarantees a minimum breadth so one
large snapshot cannot consume everything. More machinery; only worth it if a
worked case shows a single artifact starving a review.

## Adoption criteria

Adopt when a byte figure can be derived from measured reviews rather than
chosen — the same move [ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md)
made for description length, replacing a ceiling that had "inherited an earlier
full-index cost concern" with an allowance set by a retrieval assay.

Whatever ships, land the counting rule, the number, and the scope question in one
edit. They are three changes to one file, and each pass stales 775 pairs.
