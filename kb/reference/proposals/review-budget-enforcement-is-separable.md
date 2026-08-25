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

`semantic/grounding-alignment` caps link-following at five and says nothing about
exceeding it. In practice reviewers pass while disclosing — review job 8051
returned PASS having opened five of nine links and naming the four it left
unopened. So today's behavior is **advisory with an honesty requirement**,
established by convention rather than by the gate.

Sizing is being added as measurement only, changing no verdict. That leaves the
enforcement question open without blocking anything.

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

## Adoption criteria

Decide after the measurement in the sibling proposal reports what reviews
actually cost and how often a reviewer would exceed a derived budget. If
exceedance is rare, A is sufficient and the rest is machinery for a case that
does not arise. If it is common, the choice between B, C, and D matters and the
data will say which.

Do not adopt C without also deciding where the run's setting is recorded. A
verdict whose meaning depends on an unrecorded flag is worse than either fixed
answer.
