---
description: "Proposal: when a review's evidence exceeds one pass's capacity, decompose the review into covering passes and combine their outcomes, rather than sampling links or failing the artifact"
type: ../types/design-proposal.md
tags: []
---

# Exceeding a review budget splits the task

A budget on how much linked material one review pass may open has so far implied
one of two bad answers when the budget is exceeded: the reviewer **samples**, or
the pair **fails**. Sampling silently weakens what a PASS means. Failing punishes
an artifact for being well-cited.

There is a third answer, and it dissolves the question rather than answering it:
**when the evidence exceeds one pass, split the review into passes that together
cover it, and combine their outcomes.** Coverage is never traded away; only the
number of passes varies.

## Current state (as of 2026-08-25)

- A review pair is atomic. `review_pairs` records one outcome per
  `(note_path, criterion_path)` per review, and nothing in `finalization.py` or
  `batch.py` expresses partial coverage, subsets, or combination.
- `semantic/grounding-alignment` now budgets sixteen distinct linked artifacts
  globally and treats reaching the limit as disclosure rather than failure.
- Available-cost measurement shipped (`adbc1cc0`). Over 337 artifacts: p50 is 7
  distinct artifacts and 67 KB, p90 is 16 and 148 KB, max is 35 and 355 KB. **The
  selected ceiling covers the measured p90 offer**.
- Consumed-cost capture ships as soft per-pair telemetry. In a twelve-note
  capped-versus-uncapped assay, four mechanism-aligned findings appeared only
  after fuller reading reached 6–16 artifacts. The three uncapped tail cases
  offering 21–23 artifacts all passed.

## Disposition (2026-08-25)

Rejected for now by ADR 079. Raising the ceiling covers every divergent case in
the assay without adding partial-coverage, combination, or freshness semantics.
The assay supplies no divergent tail fixture above sixteen. It also cannot
validate or refute the severed-support hazard below because every capped
baseline was PASS. [The bounded evidence](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md)
records the result. This proposal is ready for archival after its inbound
references are retired.

## What splitting requires

**Decomposable coverage.** One logical judgment covered by N passes, combined
into one outcome: PASS only if every pass passes, FAIL if any fails, WARN
aggregating. That is a new concept in the review model, not a gate rule.

**A partition rule.** Which evidence each pass examines, chosen so the passes
together cover everything exactly once.

**Combination and freshness.** A pair's baseline must pin every pass that
contributed to it, or a stale subset silently validates a fresh verdict.

## The central hazard: joint support

The obvious partition is by link — pass one takes links 1–5, pass two takes 6–10.
**It is wrong, and quietly so.**

`grounding-alignment` judges whether cited material supports a claim. A claim
whose support spans several sources is supported *jointly*. Split those sources
across passes and neither pass sees the whole support, so each may fail a claim
that is in fact adequately grounded — a false FAIL produced by the split itself,
not by the artifact.

The corpus is full of such claims. Cohort work routinely found notes citing four
or five ingests for one argument, and the rollout's own unit of work was
deliberately *the claim use*, not the link, for exactly this reason.

So the partition must keep a claim's evidence together — it must be **by claim,
not by link**. Which is the difficulty: grouping links by the claim they support
is a semantic judgment, and the thing being budgeted is semantic judgment.

## Options

**A. Inventory then partition.** A cheap first pass identifies which links support
which claim; later passes each take whole claim-groups. This is the shape the
grounding rollout already used successfully — inventory claims first, then split
the work — and it keeps joint support intact. Costs one extra pass, and the
inventory pass is itself bounded because it reads the note, not the sources.

**B. Partition by link, accept severed support.** Mechanical and cheap. Produces
false FAILs on jointly supported claims, which is the failure mode least likely
to be recognized as an artifact of the process.

**C. One pass per claim.** Maximum isolation, no severing possible. Many passes on
a link-dense note, and repeated fixed cost since every pass re-reads the note.

**D. Overlapping passes.** Let claim-groups share links so no group is severed,
at the cost of re-reading shared evidence. Simplest correct partition if the
overlap is small; degenerates toward C when it is not.

## What this changes elsewhere

It largely supersedes
[Review budget enforcement is a separable decision](./review-budget-enforcement-is-separable.md).
That proposal asked whether exceeding a budget should fail or merely require
disclosure. Under splitting, exceeding does neither: it triggers decomposition.
The disclosure requirement remains valuable — a pass should still say what it
covered — but as provenance rather than as the thing that keeps a sampled verdict
honest, because verdicts stop being sampled.

It does not supersede the measurement work.
[Pricing the budget](./review-link-budget-prices-reviewer-attention.md) becomes
*more* load-bearing, because a split needs a sizing basis to decide where to cut,
and consumed cost is what says how large a pass can usefully be.

## Adoption criteria

Reopen when reviews at the sixteen-artifact ceiling produce material outcome
divergence in the tail, so a raised single pass no longer covers the observed
failure range.

Do not adopt any option before deciding how outcomes combine and how a pair's
freshness pins its passes. A split verdict whose provenance is unrecorded is
weaker than the sampled verdict it replaces, because it looks complete.
