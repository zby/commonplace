# Wave 1 worksheet: the entangled cases

Working inventory for plan Wave 1, from a close read of the held-back files and the lineage-edge sweeps (2026-07-17). Authority: [migration-plan.md](./migration-plan.md). Coordination: the mechanical second wave (plan Wave 2 subset) is being executed separately from [obvious-distillation-cases.md](./obvious-distillation-cases.md) — do not touch its files from here.

## Already executed

- **`distillation-is-transformation-not-selection.md` retired** (`757d6daa`, operator decision). Its polemic target dissolved with the term; anti-mere-selection lives in the structure note, the condition-clause mechanism is inline in `abstract-an-experience`, substrate persistence in the structure note and `a-derived-copy…`. Backlinks repointed (two ingests cited it for ampliative evidence and now support `abstract-an-experience`); ADR 021's path mention is a syntax example, left as history.
- **COLLECTION.md gloss bug fixed** (`9e252b41`): both `kb/notes/COLLECTION.md` and `kb/reference/COLLECTION.md` glossed `derived-from` as "abstracted from" — writers were being instructed to mis-label. `abstracted-from` is now authorized alongside the corrected `derived-from` in both. One mislabel-in-waiting in `trace-extracted-memory…` open questions fixed with it.

- **`a-derived-copy…` fixed and gated** (`b35ea92c`): framing sentence split per the operator's correction — dependence and staleness machinery universal, copy identity and re-derive repair derived-only, judgment fidelity-or-support; "dependent" used as ordinary English umbrella, no coinage. Full gate battery ran: 39 pairs, 9 jobs, `claude-opus-4.8` partition — 38 pass, 1 warn (`sentence/clause-packing` on the new sentence), fixed by splitting; fix report in `kb/reports/fixes/`. Two side-findings for later: the collection-conformance pass flagged that the notes COLLECTION.md label table doesn't enumerate `kb/types/` as an `evidence` destination (table gap, not a violation); the `sentence-split` fix strategy is new, propose for the taxonomy on recurrence.

- **Retitle trio executed and renamed** (`f7aac9e6`): the tradeoff note ("Constraining and extraction…"), the lineage note ("Artifacts produced from sources need lineage recorded at the source" — first carrier of the `Derived into:` footer), and "Evolving understanding needs holistic rewrite, not composition"; follow-ons `task-fitted-structure` and the note-refinement proposal reworded; renames via `commonplace-relocate-note` with corpus-wide backlink rewrites and redirects. Gate run was cut short by the session limit after 29 all-bundle pairs on the tradeoff note — 4 warns, all fixed (framing mismatch in the table, two stock phrases, footer capitalization, missing `title-as-claim` trait). The other two notes gate at the next sweep under their new paths. **Sequencing lesson: rename before gating** — baselines key on `note_path`, so a post-gate rename orphans them; for remaining rewrites, relocate first, then gate.

## Semantic rewrites (review-gated unless noted)

| File | Entanglement | Treatment | Gate |
|---|---|---|---|

**Reclassified out of Wave 1** (nothing entangled remains; append to the staging file's second wave after the current mechanical batch completes): `minimum-viable-vocabulary…`, `information-value-is-observer-relative.md`, `legal-drafting…`. **Deferred to Wave 3**: `soft-bound-traditions…` (lists the term with definition links that break on deletion).

## The definition's salvage map (input to Wave 3 deletion)

`definitions/distillation.md` instance classification: methodology→skill derived; article→summary, caller-context→prompt, observations→summary derived/selection; workshop→note mixed; repeated-failures→gate and "notice patterns, then write" ampliative — the definition's own Scope list still teaches the boundary leak. Salvage before deletion:

- use-shaping / "distillate doesn't replace source" — already covered by the structure note; drop.
- the Faithful-Self-Evolvers behavioral-influence caveat — **needs a home**; the previously natural successor was the retired transformation note. Candidates: `knowledge-storage-does-not-imply-contextual-activation` or `claw-learning-loops…`. Decide at Wave 3.
- the constraining-orthogonality 2×2 — a line in `definitions/constraining.md`.
- ML-knowledge-distillation instance — excluded by the structure note; drop.

Deletion itself is the Wave 3 ADR moment (large `defined-in` backlink surface).

## Lineage-edge classification — executed (`4175dbb3`)

16 `derived-from` edges flipped to `abstracted-from` (self-identifying generalization lineage); three `Distilled into:` footers converted to `Abstracted into:` (the two persistence-boundaries synthesis feeds and the chat-history-model tradeoff). The four definitional syntheses keep `derived-from` (reflective-system ×2, self-improving-system, actionable-methodology ×2, reasoning-production — content worked out from the cited papers). Borderline calls classified abstracted-dominant per the bet doctrine: `goedel-machines` and `adaptation-agentic-ai-analysis` map their sources into KB frames the sources don't contain. The five confident `Derived into:` conversions are staged for the mechanical executor (staging file, fourth batch). Remaining semantic rewrites: `memory-management-policy` and `write-instruction` executed (`4c0c3cf8`); `semantic-review…` confirmed correct as quoted history.

## Execution notes

- Review gates per `kb/reference/README-REVIEW-SYSTEM.md` for the gated rows; batch the ungated edge flips separately.
- Validate per collection after each batch; separate commits with explicit paths.
- The edge flips are near-mechanical once the needs-read rows are settled: one read each, then label + context-phrase edits.
