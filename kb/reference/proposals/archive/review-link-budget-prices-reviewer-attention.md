---
description: "Proposal: price a review gate's link-following by a two-term attention heuristic — per-artifact plus per-byte — computed by a sizing command rather than estimated by the reviewer"
type: ../types/design-proposal.md
tags: []
---

# Review link budget prices reviewer attention

`semantic/grounding-alignment` limits how much linked material a reviewer may
open. It now expresses that limit as a count of distinct resolved artifacts.
The resource it protects is reviewer attention, and artifact count remains an
incomplete proxy: linked material varies by two orders of magnitude in size.

## Current state (as of 2026-08-25)

ADR 079 selected an interim ceiling of sixteen distinct linked artifacts per
pair. Repeated links to one resolved target consume one slot; linked notes,
ordinary linked sources, and tracked ingests share the budget; and reaching it
does not itself change the verdict. The fixed target note and criterion do not
count. Offered and consumed cost already ride the prompt's resolved-link table
and `review_jobs.telemetry_json` without a schema change.

The ceiling is evidence-based but not an attention price. Across 337 measured
targets, p50 offered cost is 7 distinct artifacts and 67 KB, p90 is 16 and
148 KB, and the maximum is 35 and 355 KB. A paired twelve-note assay found four
mechanism-aligned findings that the five-link instruction missed, all reached by
6–16 artifacts; its 21–23-artifact tail passed under the uncapped criterion.
That justified the interim count while leaving the size term unresolved.

Two earlier defects are now closed. The former instruction counted link
occurrences even though 239 of 314 linked notes repeated a target, and it left
ingest applicability ambiguous. The live gate now deduplicates resolved targets
and states one global scope. What remains is heterogeneous attention cost: a
3 KB post and a 456 KB paper each consume one slot.

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
design question. A worked corpus can supply the inputs, but count-and-byte stop
points alone cannot identify the ratio: they need either an independent
attention outcome or a controlled comparison that varies packaging while
holding the evidence task constant.

The interim rule already makes repeated links cost nothing extra because they
resolve to one artifact. The proposed successor adds the missing size term
through β. No evidence-class ranking is needed: a reviewer holding a two-term
budget spends it where it informs, without a rule ordering source links above
internal ones.

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

**D. Keep the current count.** Cheapest. ADR 079 supplied a measured number and
fixed deduplication and scope, but heterogeneous artifacts remain unpriced.

## What must be decided before implementation

The measurement and enforcement plumbing is settled. Whole-file sizes appear in
the code-generated `resolved_links` table, and each pair reports distinct opened
paths plus a budget-or-sufficiency stop reason. Finalization prices those paths
and records the report in existing job telemetry. ADR 079 also fixed verdict
semantics: budget exhaustion alone is not failure, and unchecked material routes
are disclosed.

The blocking decision is now the proposal's substantive one: identify α/β and
the total budget from an independent attention outcome or a paired packaging
assay. The first capped pilot and the uncapped comparison do not do that. A
sufficiency stop varies with the note's evidence needs, while a count-budget stop
is fixed by policy; neither observation supplies the exchange rate.

Route-aware charging remains an implementation choice that may affect the
estimate. V1 whole-file pricing overcharges an ingest's Quotes route and
undercharges a snapshot route by pricing the linked ingest rather than the
derived snapshot. An identifying assay must either preserve that approximation
explicitly or measure the portions actually read.

## Adoption criteria

Adopt when α, β, and the budget can be derived from a measurement that actually
identifies their relative contribution — for example independent usage or
active-time telemetry, or a paired assay that keeps the evidence task fixed
while varying artifact count and bytes — rather than chosen from raw stop
points. This is the same move
[ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md)
made for description length, replacing a ceiling that had "inherited an earlier
full-index cost concern" with an allowance set by a retrieval assay.

If this proposal later replaces the interim count, land the price and its
criterion wording in one edit so review baselines stale once.
