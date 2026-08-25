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
design question. A worked corpus can supply the inputs, but count-and-byte stop
points alone cannot identify the ratio: they need either an independent
attention outcome or a controlled comparison that varies packaging while
holding the evidence task constant.

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

## What must be decided before implementation

Three blocking decisions; the rest an implementer determines.

**Settled by operator direction, 2026-08-25.** Decisions 1 and 3 below are
resolved; decision 2 is deferred to its own proposal. Both resolutions turn on
reuse: the measurement path needs no new storage and no new review semantics.

- **Sizes ride the existing link table.** `resolved_links` is already
  code-generated into every prompt; add a size column there rather than asking a
  reviewer to call anything. A standalone command may follow over the same
  sizing library, but the table is primary.
- **Measurement is recorded through existing telemetry.** `review_jobs` already
  carries `telemetry_json` for "opaque harness telemetry without making it review
  identity" — the right channel for what a review actually opened, with no
  schema change.
- **V1 records cost and enforces nothing.** The gate is untouched, no pairs stale,
  and review judgment and link-following policy do not change. The records are
  calibration inputs, but the cap does not move until an identifying assay can
  derive α, β, and the budget.
- **Measurement B shipped (2026-08-25).** Every pair is now asked to report the
  distinct pre-resolved artifacts it opened and whether budget or sufficiency
  stopped inspection. Finalization derives whole-file bytes, records complete
  and imperfect reports beside A in job telemetry, and removes the bookkeeping
  from retained review text.
- **The first 12-pair pilot did not identify `α / β` (2026-08-25).** All 12
  reports were complete, but nine opened exactly five artifacts. Eleven
  reviewers reported sufficiency, one reported budget at five, and one
  sufficiency report exceeded the cap at seven. A sufficiency point varies with
  the note's evidence needs; a budget point under the current gate is fixed by
  artifact count. Neither is an independent observation of attention cost.
  More capped reviews would repeat that confounding, so the budget remains open.
- **Verdict semantics are unchanged for now** — see
  [Review budget enforcement is a separable decision](./review-budget-enforcement-is-separable.md).

**1. Where sizes surface.** `review/protocol/prompt.py` already emits a
code-generated `resolved_links` table into every review prompt. A size column
there means the reviewer plans against costs it already holds and makes no tool
call — [frontloading](../../notes/frontloading-spares-execution-context.md)
applied exactly. A standalone command works outside the review pipeline but must
be remembered and spends a turn. Likely both, over one sizing library, but the
gate's wording depends on which is primary: "read the sizes in your link table"
and "run this command" are different instructions.

**2. What exceeding the budget means.** Today a reviewer over budget passes while
disclosing what it left unopened — job 8051 did exactly that. Under a computed
budget, is that still a PASS, or does exceeding become FAIL? This decides whether
the budget is guidance with an honesty requirement or an enforced limit, and the
two produce different verdicts on the same corpus.

**3. Whether V1 enforces anything at all.** The adoption criterion says derive α,
β, and the budget from measured reviews rather than choose them. Taken seriously,
V1 ships **measurement only**: sizing lands, reviews record what they cost, and
the gate is untouched. The gate edit and its 775-pair sweep then happen once,
against real numbers. The alternative is to ship a chosen budget now and correct
it later, which is the inherited-number failure this proposal exists to retire.
Recommended: measure first. It also means V1 changes no review behavior, which
should be said out loud rather than discovered.

Three smaller questions, cheap to settle but ambiguous if left:

- Does the target note and the criterion itself count against the budget, or only
  linked material? (Only linked material is the assumption throughout, unstated.)
- Is the budget per pair or per job? `--grouping note` puts several criteria over
  one note into one job, and each currently applies the cap independently.
- How is an unavailable target priced — a missing file, or a `(snapshot
  required)` link whose snapshot is absent? Sizing should report rather than
  error, since ADR 073 already makes the missing snapshot a gate FAIL.

An implementer determines the rest: command name and flags, output shape, whether
sizing lives in its own module, and the table's column layout. None of those
changes a decision made above.

## Adoption criteria

Adopt when α, β, and the budget can be derived from a measurement that actually
identifies their relative contribution — for example independent usage or
active-time telemetry, or a paired assay that keeps the evidence task fixed
while varying artifact count and bytes — rather than chosen from raw stop
points. This is the same move
[ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md)
made for description length, replacing a ceiling that had "inherited an earlier
full-index cost concern" with an allowance set by a retrieval assay.

Whatever ships, land the counting rule, the number, and the scope question in one
edit. They are three changes to one file, and each pass stales 775 pairs.
