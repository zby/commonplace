---
description: "What the complete and covered_by marks on tag-READMEs mean for consumers — accelerators over a recoverable query, never load-bearing; the asymmetry that forces machine enforcement, and the consumer/lifecycle behavior that follows"
type: kb/types/note.md
status: current
---

# Mark semantics

A mark is a machine-checked property a tag-README declares in frontmatter: `complete: true` ("every note carrying the tag is linked here") or `covered_by: [children]` ("every note carrying the tag also carries a listed child tag"). This document describes what the marks are allowed to mean — the rule every current and future mark must satisfy (decided in [ADR 026](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md); the per-mark maintenance contract lives on the type spec, `kb/types/tag-readme.md`).

**A mark is an accelerator, never a load-bearing wall.** No consumer's correctness may depend on a mark being present. The marked information is always independently recoverable — the scoped `rg` membership sweep ([navigation.md](./navigation.md)) recomputes it regardless of any mark — so a mark only saves work and adds trust: it *licenses skipping a step*, it never *replaces the ground truth*.

## The asymmetry that forces the rule

A mark can be true or false, present or absent. The two failure modes are not symmetric:

- **Unmarked-but-true is harmless.** A README that *is* complete but does not declare it costs an exhaustive consumer one query it did not strictly need — the `rg` sweep runs and finds nothing missing. Wasted work, correct outcome.
- **Marked-but-false is catastrophic.** A README declaring `complete` while members are missing tells every exhaustive consumer to *stop looking* while items are still out there — the [stale-indexes failure](../notes/stale-indexes-are-worse-than-no-indexes.md) in its sharpest form: a trusted-but-stale claim suppresses the fallback search entirely, so missing items become invisible rather than merely hard to find.

A false negative costs a bounded, recoverable query; a false positive costs silent, unbounded incorrectness. Because the downside is one-sided and severe, every mark is **validator-enforced** — there is no sanctioned state where a mark is maintained by hand and trusted by consumers.

The rule holds only because the recovery path exists first: the mark is a cache over the membership query, and the query is the ground truth — the scoped-`rg` path was guaranteed by [ADR 025](./adr/025-complete-generated-indexes-are-build-time-only.md) before the marks existed. A mark without a recovery path would be load-bearing by necessity — its *absence* would also break consumers. The design sequence is therefore: guarantee the query path, then add the mark as an optimization on top. This is the marks-specific instance of the general compiled-view requirement: a derived surface [must not drift into an independent source of truth](../notes/agent-memory-requirements/keep-compiled-views-aligned.md).

## Consumer and lifecycle behavior that follows

1. **Marks degrade gracefully.** Dropping a mark costs consumers one query, not correctness. This keeps the growth-driven lifecycle exit cheap: a `complete` README that outgrows its weight gate simply drops the mark and readers fall back to the `rg` sweep — no dependent migration, no broken consumers.

2. **The unenforced prose version of a checkable claim is never written.** "This list is complete" or "these children cover the tag" as prose, with no validator behind it, is the catastrophic state with none of the protection. A checkable claim is either enforced as a mark or not asserted at all.

3. **Consumers treat marks as skip-one-call optimizations and record the skips.** `cp-skill-connect` reading `complete: true` skips exactly one query (the by-tag sweep for that tag) and notes the skip in its discovery trace — keeping the decision auditable and reversible if a mark is later found false.

The same three-condition shape — a machine-checkable property, an independent recovery path, an exhaustive consumer that stops looking once satisfied — applies to any future mark (freshness stamps, validated flags), which is why the type spec constrains new marks to satisfy this rule. It is the general form of "a cache must never be the only copy."

---

Relevant Notes:

- [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent](../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the general theory the marks instantiate — enforce-or-omit for any derived copy of recomputable ground truth
- [stale-indexes-are-worse-than-no-indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) — rationale: the marked-but-false case is the trusted-stale-artifact trap, which is why marks are machine-enforced or absent
- [keep-compiled-views-aligned](../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — rationale: a mark is a compiled view over the membership query; that note states the general requirement (a rebuildable derivative must not become an independent source of truth, and stale views must be detectable) that this rule instantiates
- [026-tag-readme-type-with-completeness-and-coverage-marks](./adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) — part-of: the decision record that introduced the marks and this rule
- [025-complete-generated-indexes-are-build-time-only](./adr/025-complete-generated-indexes-are-build-time-only.md) — part-of: the decision that guaranteed the scoped-`rg` recovery path the marks depend on
- [maintain-curated-indexes](../instructions/maintain-curated-indexes.md) — procedure: declaring, fixing, and dropping marks when the validator flags a README
