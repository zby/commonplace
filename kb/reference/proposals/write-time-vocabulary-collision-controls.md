---
description: "Proposal: mechanical controls for the one-term-one-sense invariant — reserved-term registry, slot-escape lint, coinage collision screen, naming-review gate, and clausal-binding link check"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance]
---

# Write-time vocabulary collision controls

The KB's vocabulary invariant — no unqualified term carries two load-bearing senses across co-loadable artifacts — is currently held by writer discipline and manual `rg` audits. Nothing mechanical prevents a new note from capturing a term that already carries a different technical sense, reintroducing a retired term, or using a registered identifier outside its declared slot. This proposal holds the candidate mechanical controls, ordered roughly from cheapest and deterministic to most semantic, with the sequencing choice open.

## Current state (as of 2026-07-18)

- **Vocabulary bindings live in three prose surfaces, none machine-readable as a registry:** the always-loaded `AGENTS.md` Vocabulary section (ADR 022), definition notes under `kb/notes/definitions/` and `kb/reference/definitions/`, and the registered hyphenated identifiers documented in `kb/reference/link-vocabulary.md`.
- **`commonplace-validate` knows nothing about term senses.** It checks frontmatter validity, schema constraints, link health, and required sections; it has no list of reserved strings and no notion of a retired term.
- **The review system can run semantic gates** over `(note, criterion)` pairs through the assay pipeline — a naming gate would ride existing machinery rather than requiring new infrastructure.
- **Retirement is recorded only in prose history.** `distillation` was retired without a successor term (ADR 053); nothing flags its reintroduction.
- **The write path has a cheap duplicate check but no sense-collision check.** `cp-skill-write` screens for duplicate notes, not for captured terms; the `kb/work/vocabulary-governance/` workshop names extending it as open work.
- The theory — the invariant, the risk model, and the device ranking these controls would enforce — lives in [load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md).

## The design space

1. **Reserved-term registry.** A machine-readable mapping of reserved token → defining artifact, with a status field (`active` / `retired`). Uniqueness becomes a deterministic validation error: two definitions claiming one token fail, and a retired token reappearing as a new definition is flagged. This is the substrate the other controls read; without it each control needs its own term list.
2. **Slot-escape lint.** A deterministic check that registered hyphenated identifiers (`derived-from`, `abstracted-from`, …) appear only in their declared slots — link labels, frontmatter keys and values — and not in unscoped body prose. Needs a mention-vs-use escape (backticked mentions in documentation are legitimate), which keeps the check simple: flag unbackticked occurrences outside declared slots.
3. **Coinage collision screen.** A write-path step (or small command) that, given a candidate term, runs the exact-string sweep across co-loadable collections, reports match sites, and flags the high-noise profile of a common bare word — frontloading the manual audit into the moment the term is introduced, when changing the name is still free.
4. **Naming-review gate.** A review criterion applied to notes that introduce or bold a technical term: does the term collide with a registered sense, and is the load-bearing sense carried by an approved device (schema slot, rare compound, linked clause frame)? Semantic, so it runs as an assay, not in the validator.
5. **Clausal-binding link check.** For grammar-scoped predicates such as `actionable`: sweep occurrences of the bare word, lexically prefilter those near the designated subject noun, and semantically review the residue to confirm every technical predication carries its definition link. This is the only control that checks the weakest admissible device, and the most expensive per run.

## Free choices

- **Registry form.** A central file (cheap to load whole, one more surface to drift) versus a `term:` frontmatter field on definition notes that the validator aggregates (binding lives next to the definition, registry is derived not authored). Either way the `AGENTS.md` Vocabulary section becomes checkable against it — generated from it, or hand-curated with a consistency check.
- **Enforcement point per control.** Validator (deterministic: registry uniqueness, retirement, slot-escape), review gate (semantic: naming review, clausal link check), or write-skill step (advisory: collision screen). The split by check type is the likely shape, but a control could move — e.g. the collision screen could harden from advisory to gating.
- **Binary versus graded reservation.** A binary reserved-word rule is simple; the `vocabulary-governance` workshop flagged that exposure is graded — `prose` is a captured common word whose technical sense sits close to the ordinary one, so misresolution is low-consequence. A registry could carry an exposure grade that tunes how hard the checks fire.
- **Scope.** This repo only, or shipped through `commonplace-init` so consuming KBs get the machinery with their own registries — which requires the controls to read policy, not hardcode this repo's terms (the constraint the `vocabulary-governance` workshop owns).

## Adoption criteria

- Introducing a new technical term takes one screen invocation and one registry entry; violations of registered-token uniqueness and retirement are caught at validation with no LLM cost.
- Semantic checks ride the existing review pipeline as criteria, not new infrastructure.
- Total friction stays below the manual audit it replaces — if writers route around the registry, retire it rather than escalate it.

## Risks

- **Registry drift.** A registry the validator does not cross-check against definition notes becomes a second, possibly wrong, vocabulary surface — worse than prose alone. The cross-check is not optional.
- **Over-formalization.** Most words are not load-bearing; a check that nags on ordinary polysemy teaches writers to ignore it. The load-bearing filter has to live in the registry (only registered terms fire checks), not in the checker's judgment.
- **Low term-introduction rate.** New technical terms arrive rarely; heavy machinery may never pay back. The collision screen (option 3) is self-serve and nearly free, so it sequences first regardless; the registry earns adoption only if slot-escape or retirement violations actually occur.

---

Relevant Notes:

- [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) — rationale: the invariant, risk model, and device ranking these controls would mechanically enforce
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rationale: the collision screen frontloads the corpus audit to the moment of naming, when the answer is cheapest to act on
