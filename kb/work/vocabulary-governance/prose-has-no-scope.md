# Prose has no scope (promoted)

**Status (2026-07-17): promoted.** The theory now lives in [vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — the corpus-scale no-scope argument, the silent-composition failure, the prevention-over-scoping remedy, the position-in-a-schema analysis, the multi-word-coinage naming rule, and the load-bearing-polysemy caveat all live there. This file keeps only what is workshop-specific: evidence pointers the note cannot link, decisions the thread produced, and the open policy work this workshop still owns.

## Evidence (kb/work links the note cannot carry)

- [distillation-usage-audit.md](../theory-methodology-derivation/distillation-usage-audit.md) — the 464-instance sweep: scope leakage observed at corpus scale, and the cost benchmark for checking a captured common word (semantic audit) vs a coined compound (lexical search)
- the distillation control trap (thread closed 2026-07-17; its control-regime diagnostic is now the classifying question in `kb/reference/link-vocabulary.md`) — the operational cost of one misresolved sense: an artifact borrowing a maintenance regime its control story doesn't support
- [migration-plan.md](../theory-methodology-derivation/migration-plan.md) — the thread's conclusions enacted: minimality constraint, no-successor-term end state, and the naming decisions below

## Decisions this thread produced

- **One term, one sense, corpus-wide** — the uniqueness invariant, enforced at write time; adopted as the reading of "collision handling" for this workshop's candidate model (imports, qualified names, and shadowing have no prose implementation).
- **Multi-word coinages as the default naming rule** for technical terms (operator, 2026-07-17).
- **`discovery lifecycle`** adopted as the migration's incoming technical term — the compound, not bare "discovery" — applying the naming rule to the migration's own Wave 0.

## Flagged tangent (parked for the policy pass)

**"prose"** is itself a captured common word in KB-technical use — a representational-form category, already on the outward-docs exclusion list. Same exposure class as distillation, but its technical sense sits close to the ordinary one, so misresolution may be low-consequence. Suggests the policy pass wants a graded exposure test — how far apart are the senses, and what rides on resolving them? — rather than a binary common-word rule.

## Open policy work (this workshop)

- Where to encode the naming rule: the vocabulary-policy output of this workshop, `cp-skill-write`'s naming guidance, or both.
- Write-time enforcement of the uniqueness invariant: the candidate mechanisms (reserved-term registry, slot-escape lint, coinage collision screen, naming-review gate, clausal-binding link check) are now collected in [write-time vocabulary collision controls](../../reference/proposals/write-time-vocabulary-collision-controls.md); this workshop keeps the policy question of where the controls read their term list from.
- Whether collection-local vocabulary is compatible with the invariant at all (safe only for terms that cannot co-load with a colliding sense, or are coined so collision is impossible).
