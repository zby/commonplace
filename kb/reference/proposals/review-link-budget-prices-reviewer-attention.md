---
description: "Proposal: price a review gate's link-following by a two-term attention heuristic — per-artifact plus per-byte — computed by a sizing command rather than estimated by the reviewer"
type: ../types/design-proposal.md
tags: []
---

# Review link budget prices reviewer attention

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

**The resource is reviewer attention** (operator decision, 2026-08-25), not
context. That settles the question the first draft left open, and it rules out
both pure measures: a count ignores that a 456 KB paper costs more than a 3 KB
post, and a byte total ignores that each additional artifact carries its own act
of orientation regardless of size.

So price attention with two terms — a fixed cost per distinct artifact opened,
plus a marginal cost per byte read:

    attention ≈ α · (distinct artifacts) + β · (bytes read)

The shape is not invented for this purpose. It is the switching-plus-scanning
structure of a patch model: a between-artifact cost paid on each move and a
within-artifact cost proportional to what is consumed. The ratio α/β is the whole
design question, and it is what a worked corpus must supply.

Both defects the first draft fixed survive this change, because they were
consequences of counting links rather than of the measure chosen. Repeated links
still cost nothing extra — they resolve to one artifact. Heterogeneous sizes are
still priced, through β. And no evidence-class ranking is needed: a reviewer
holding a two-term budget spends it where it informs, without a rule ordering
source links above internal ones.

## Sizing belongs in code, not in the reviewer's head

A reviewer cannot apply this by estimation, and should not try. The budget needs
a deterministic sizing command that resolves a target's links and prices them,
so the reviewer spends a computed budget instead of guessing at one.

Three properties matter more than the interface:

- **Dedupe in code, not by rule.** Resolve links to targets and charge each
  distinct artifact once. This removes the occurrence-counting defect
  mechanically rather than asking an instruction to describe it.
- **Charge whole files in V1; partial reads are a TODO.** The obvious refinement
  is route-aware charging — under ADR 073 a Quotes-route ingest is read only for
  its `## Quotes` section, and a `(snapshot required)` link charges a snapshot
  rather than the ingest. V1 does not do this. It charges the resolved file.

  The cost is known and accepted: whole-file charging **over-prices the Quotes
  route**, which exists precisely to be the cheap one, and under-prices a
  snapshot link by charging the ingest instead of the larger snapshot it
  actually opens. Both are corrections in the same direction as more precision,
  so a later refinement tightens the figure without inverting any decision made
  under it. Deriving α and β from whole-file measurements first also gives the
  partial-read version a baseline to be measured against.
- **Price, do not choose.** The command reports per-link cost and the total; it
  does not decide what to read. Which links carry a target's load-bearing claims
  is judgment, and moving it into code would be the classification rule this
  proposal exists to avoid.

That split keeps the deterministic half deterministic and leaves the semantic
half to the gate, matching how the review system already separates selection from
judgment.

## Forces

**The α/β ratio is the design, and it is unmeasured.** At β→0 this is today's
count; at α→0 it is the first draft's byte cap. Everything interesting is
between, and nothing in the corpus yet says where. A ratio chosen rather than
derived would reproduce the inherited-number problem this proposal is trying to
retire.

**Bytes are not tokens, and the ratio moves with content.** Equation-heavy
snapshots, tables, and code tokenize far worse than prose. A byte figure will
under-price exactly the sources whose extraction artifacts already cause trouble.

**Sizing must precede reading, which is why it is a command.** Under a count,
budgeting needs no lookahead. Under any size-sensitive measure the reviewer must
know costs before opening anything — unworkable as a mental step, routine as a
tool call.

**Partial reads complicate the accounting.** The Quotes route reads one section,
not a whole ingest. Whether the budget charges the artifact or the portion read
changes the arithmetic and needs deciding.

**Disclosure matters more than the number.** Job 8051 passed while naming the
four links it did not open, which is what keeps a sampled verdict honest. Any
budget must keep that requirement; a larger budget without disclosure would be
worse than a smaller one with it.

## Options

**A. Two-term heuristic with a sizing command.** The proposal above. Operativity:
one new command, one gate-file edit stating the budget and requiring the command.

**B. Per-artifact count with a size ceiling.** Keep counting artifacts, but refuse
any single artifact over some size. Cruder, no ratio to derive, and it forbids
rather than prices — a 456 KB source that genuinely carries the claim becomes
unreadable instead of expensive.

**C. Byte total alone.** The first draft. Simplest, and mispriced now that the
resource is attention.

**D. Keep the count, fix only the counting rule.** Cheapest; leaves the number
unexamined and heterogeneity unpriced.

## Adoption criteria

Adopt when α, β, and the budget can be derived from measured reviews rather than
chosen — the same move [ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md)
made for description length, replacing a ceiling that had "inherited an earlier
full-index cost concern" with an allowance set by a retrieval assay.

Whatever ships, land the counting rule, the number, and the scope question in one
edit. They are three changes to one file, and each pass stales 775 pairs.
