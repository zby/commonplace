# Validation

Exploring how to make validation a reliable part of the KB workflow. The current state: `/validate` checks structure, semantic review exists as a separate instruction, and neither runs automatically.

## Design Space

**When to validate:**
- On demand (`/validate`) — current state, relies on agent remembering
- After writing — WRITING.md now instructs this, but still depends on agent compliance
- Periodic revalidation of changed notes — catch regressions, drift
- At commit time — natural "done" signal, but hard to configure universally
- Via hooks on Write/Edit — most automatic, but noisy on intermediate edits

**What to validate:**
- Structural (hard oracle) — frontmatter, enums, link health. Fast, deterministic, rarely fails in practice because agents already know the conventions
- Semantic (soft oracle) — enumeration completeness, grounding alignment, internal consistency. Where the real value is. Requires LLM judgment, expensive
- Cross-note consistency — contradiction detection, redundancy. Most expensive, corpus-level

**How to validate:**
- LLM skill (`/validate`) — current approach for everything, including deterministic checks
- Deterministic script — for hard-oracle checks, milliseconds, could run as hook
- Combined — script for structure, LLM for semantics

## Open Questions

- What's the right granularity for semantic validation on write? Full semantic review is expensive; a lighter "quick semantic check" (just description quality + internal consistency) might be the sweet spot for routine use.
- Should `/validate` absorb the semantic review, or should they stay separate skills with different cost profiles?
- Is periodic revalidation (e.g. `/validate recent` on a schedule) more practical than per-write hooks?
- The auto-commit hook disaster taught us that automating judgment-requiring operations backfires. But semantic validation is read-only (doesn't modify files). Does that change the calculus?
- What would a "validation gate" pattern look like in practice — multiple independent checks with quorum (borrowed from SAGE review)?

## Experiments to Run

1. **Merge semantic review into `/validate`** — run both structural and semantic checks in one invocation. Measure: does the combined output actually catch real problems? Is the latency acceptable?
2. **Write-time hook with structural-only checks** — fast deterministic script, warning-only. Measure: is it useful or just noise on intermediate edits?
3. **Periodic batch revalidation** — `/validate recent` after a work session. Measure: does it catch things that per-note validation misses (cross-note issues, regressions)?

## Related Notes

- [deterministic-validation-should-be-a-script](../../notes/deterministic-validation-should-be-a-script.md) — the hard/soft oracle split for validation checks
- [semantic-review-catches-content-errors-that-structural-validation-cannot](../../notes/semantic-review-catches-content-errors-that-structural-validation-cannot.md) — the four semantic checks and their text-testing-pyramid placement
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — the enforcement gradient (instruction → skill → hook → script)
- [enforcement-without-structured-recovery-is-incomplete](../../notes/enforcement-without-structured-recovery-is-incomplete.md) — what happens after validation fires
- [SAGE review](../../notes/related-systems/sage.md) — validation gate pattern (multiple independent checks with quorum)
