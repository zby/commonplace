---
description: A machine-checked property mark on an artifact may only license skipping a recomputable step; no consumer's correctness may depend on its presence
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance, context-engineering]
status: current
---

# A declared mark is an accelerator, never a load-bearing wall

When a knowledge artifact declares a machine-checked property — a tag-readme's `complete: true` ("every member is linked here") or `covered_by` ("the listed children cover this tag") — no consumer's correctness may depend on the mark being present. There must always be an independent query path that recovers the same information regardless of any mark. In Commonplace that path is the scoped `rg` membership sweep. The mark only saves work and adds trust: it *licenses skipping a step*, it never *replaces the ground truth*.

This is a constraint on what a mark is allowed to mean, derived from a sharp asymmetry between the two ways a mark can be wrong.

## The asymmetry that forces the rule

A mark makes a claim about the world. It can be true or false, present or absent. Two of the four combinations are failure modes, and they are not symmetric.

- **Unmarked-but-true is harmless.** An artifact that *is* complete but does not declare `complete` costs an exhaustive consumer one query it did not strictly need — it runs the `rg` sweep and finds nothing missing. Wasted work, correct outcome.
- **Marked-but-false is catastrophic.** An artifact that declares `complete` while members are missing tells every exhaustive consumer to *stop looking* while items are still out there. This is the [stale-indexes failure](./stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: presence of a trusted-but-stale claim suppresses the fallback search entirely, so the missing items become invisible rather than merely hard to find.

The cost of a false negative (no mark) is a bounded, recoverable query. The cost of a false positive (wrong mark) is silent, unbounded incorrectness. Because the downside is one-sided and severe, a declared mark must be **machine-enforced or not exist** — there is no safe middle where a human or agent maintains the claim by hand and consumers trust it.

## Why an independent query path is the precondition

The rule only holds because the marked information is independently recoverable. The mark is a cache over a computation (the membership query); the ground truth is the computation. If there were no way to recompute membership without the mark, the mark would be load-bearing by necessity, and then enforcing it would not be enough — its absence would also break consumers, collapsing the asymmetry above.

So the design sequence is: first guarantee the query path, then add the mark as an optimization on top of it. A mark added without a recovery path is a wall pretending to be an accelerator.

## Design consequences

1. **Marks degrade gracefully.** Dropping a mark costs consumers one query, not correctness. This is what makes a growth-driven lifecycle exit cheap: when a `complete` tag-readme grows past its weight gate, it simply drops the mark and readers fall back to the `rg` sweep — no migration of dependents, no broken consumers. A design where dropping the mark broke things would resist the exit and accumulate stale claims.

2. **Never write the unenforced prose version of a checkable claim.** "This list is complete" or "these children cover the tag" written as prose, with no validator behind it, is the catastrophic state with none of the protection — it earns the trust of exhaustive consumers while decaying silently. If a claim is checkable, either enforce it as a mark or do not assert it at all.

3. **Consumers treat marks as skip-one-call optimizations and record the skips.** An exhaustive consumer reading `complete: true` skips exactly one query (the by-tag sweep for that tag) and notes that it did so. Recording the skip keeps the decision auditable and reversible: if the mark is later found false, every consumer that trusted it can be identified by what it skipped.

## Scope

The argument needs three things and nothing more: a property that is machine-checkable, an independent path that recovers the same information, and at least one consumer that acts on the property exhaustively (stops looking once satisfied). Where all three hold — completeness marks, coverage marks, freshness stamps, "validated" flags, cache-hit markers — the rule applies. It is the general form of "a cache must never be the only copy."

---

Relevant Notes:

- [stale-indexes-are-worse-than-no-indexes](./stale-indexes-are-worse-than-no-indexes.md) — grounds: the marked-but-false case is exactly the trusted-stale-artifact trap, in its sharpest form
- [026-tag-readme-type-with-completeness-and-coverage-marks](../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — evidence: the shipped `complete`/`covered_by` marks on the tag-readme type instantiate this rule (enforced, with `rg` as the recovery path)
