---
description: "Proposal: decide separately whether exceeding a review link budget fails a pair or only requires disclosure, and whether that behavior should be selectable rather than fixed"
type: ../types/design-proposal.md
tags: []
---

# Review budget enforcement is a separable decision

[Pricing a review link budget](./review-link-budget-prices-reviewer-attention.md)
proposes measuring what a reviewer opens. It does not settle what happens when a
reviewer would exceed the budget, and that question is independent: the same
measurement supports either answer.

## Current state (as of 2026-08-25)

ADR 079 selected option A for `semantic/grounding-alignment`. The gate now
budgets sixteen distinct linked artifacts, makes reaching the limit
non-verdict-bearing, and requires any unchecked material route to be named while
the verdict is scoped to inspected material. Available and consumed cost remain
telemetry rather than review identity.

The paired assay behind that decision found four mechanism-aligned findings that
the five-link instruction missed, all within sixteen artifacts. Failing on
exceedance would not have recovered them; raising the reading ceiling did.

## Disposition (2026-08-25)

Resolved for the current grounding criterion. Advisory disclosure is selected;
enforced failure, per-run selection, and a second hard ceiling are rejected for
now. [The bounded evidence](../../notes/evidence/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md)
records the outcome and the trigger for revisiting it. This proposal is ready
for archival after its inbound references are retired.

## The question

Does exceeding the budget make a pair FAIL, or does it remain a disclosure
obligation?

The two answers differ in what a verdict means. Under enforcement, a PASS
asserts the reviewer covered the artifact within budget. Under disclosure, a PASS
asserts the reviewer covered what it judged load-bearing and said what it did
not. Both are defensible; they are not the same claim, and a corpus of verdicts
means different things depending on which is in force.

## Forces

**Disclosure is what makes a sampled verdict honest**, and it already works
unprompted. Job 8051's reviewer named its four unopened links without being asked
to. Enforcement adds nothing there; it changes only what happens next.

**Enforcement can fail an artifact for being link-dense** rather than for being
wrong. A well-connected note that cites eight sources responsibly would fail a
budget an under-cited note passes, which inverts the incentive the KB wants.

**Advisory budgets erode.** A number nobody enforces drifts toward decoration,
and a reviewer under time pressure has no reason to respect it.

**A fixed choice may be wrong for different sweeps.** A broad `--all-gates` pass
over hundreds of notes and a targeted single-note review have different
tolerances for cost. That argues for selectability rather than a constant.

## Options

**A. Keep advisory, state it.** Write today's convention into the gate: exceed
the budget only with disclosure. Cheapest, changes no verdict, makes the existing
practice legible.

**B. Enforce: exceeding fails.** Strongest guarantee about what a PASS means.
Risks failing artifacts for density.

**C. Selectable per run.** A flag or partition setting choosing advisory or
enforcing. Fits the differing tolerances of sweeps versus targeted reviews, at
the cost of a verdict whose meaning depends on run configuration — which the
review store would then need to record, or the corpus becomes uninterpretable.

**D. Enforce a hard ceiling above an advisory budget.** Disclosure up to the
budget, failure past a larger limit. Two numbers instead of one, both needing
derivation.

## Earlier supersession candidate

[Exceeding a review budget splits the task](./exceeding-a-review-budget-splits-the-task.md)
proposes a third answer that dissolves this question: exceeding the budget
triggers decomposition into covering passes, so a verdict is neither sampled nor
failed. What survives here is the disclosure requirement — a pass should still
record what it covered — but as provenance rather than as the mechanism keeping a
sampled verdict honest.

The cap-lift assay rejected splitting for now, so the options became live and
option A was selected.

## Adoption criteria

Reopen only if sampled reviews at the sixteen-artifact ceiling produce material
tail divergences or disclosure proves insufficient to interpret their verdicts.
Do not adopt per-run selection without recording the setting in review identity.
