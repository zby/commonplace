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
| `memory-management-policy-is-learnable-but-oracle-dependent.md` | the audit's collision: "selection and distillation" as a load-bearing contrasting pair in claim 1 | Reword the pair as retention judgment (what to remember) vs context-shaping (what to load); the old verb triple becomes plain verbs with links | quick, claim-1 only |
| `kb/instructions/write-instruction.md` | two provenance stories under one word: repeated-ops→procedure (abstraction; "can't distill what you haven't done" = recurrence evidence) vs procedure derived from methodology notes | Say both correctly and briefly (instruction register): abstract the stable core from repetition with its boundary, then work the procedure out from companion methodology where it exists; companion link becomes `derived-from`-shaped | light |
| `semantic-review-catches-content-errors…` | recounts the old three-operation framework as discovered history | Historical wording — keep the old term as quoted history; no reclassification | no |

**Reclassified out of Wave 1** (nothing entangled remains; append to the staging file's second wave after the current mechanical batch completes): `minimum-viable-vocabulary…`, `information-value-is-observer-relative.md`, `legal-drafting…`. **Deferred to Wave 3**: `soft-bound-traditions…` (lists the term with definition links that break on deletion).

## The definition's salvage map (input to Wave 3 deletion)

`definitions/distillation.md` instance classification: methodology→skill derived; article→summary, caller-context→prompt, observations→summary derived/selection; workshop→note mixed; repeated-failures→gate and "notice patterns, then write" ampliative — the definition's own Scope list still teaches the boundary leak. Salvage before deletion:

- use-shaping / "distillate doesn't replace source" — already covered by the structure note; drop.
- the Faithful-Self-Evolvers behavioral-influence caveat — **needs a home**; the previously natural successor was the retired transformation note. Candidates: `knowledge-storage-does-not-imply-contextual-activation` or `claw-learning-loops…`. Decide at Wave 3.
- the constraining-orthogonality 2×2 — a line in `definitions/constraining.md`.
- ML-knowledge-distillation instance — excluded by the structure note; drop.

Deletion itself is the Wave 3 ADR moment (large `defined-in` backlink surface).

## Lineage-edge classification

**`Distilled into:` footers — 10 real instances** (plus META prose mentions in `links-README.md` and the source-tracking note, reworded with their files):

| Source → target | Likely label | Confidence |
|---|---|---|
| `unified-calling-conventions` → rlm-tendril-llm-do synthesis | Abstracted into: | needs read |
| `rlm-has-the-model-write…` → same | Abstracted into: | needs read |
| `areas-exist-because…` → COLLECTION.md rules | Derived into: | quick confirm |
| `definitions/reach-assessment` → formal-systems split-out | Derived into: | high |
| `session-history-should-not…` → chat-history-model | Abstracted into: | needs read |
| `discovery-is-seeing…` → cp-skill-connect | Derived into: | medium |
| `first-principles-reasoning` → review-explanatory-reach task | Derived into: | high |
| `title-as-claim-exposes…` → COLLECTION.md checklist | Derived into: | high |

**`derived-from` edges — ~24 real edges; most must flip to `abstracted-from`.** The context phrases self-identify: "the concrete case this claim abstracts" (`compiling-coordination`), "this note generalizes from" (`full-identity-keys`), "first witnessed instance" (`orchestration-needs-privilege`), "the originating application, not independent evidence" (`directory-placement`), "the shipped instance whose generalization is this proposal's trigger" (two proposals + ADR 030), "source taxonomy this note translates" (`adaptation-agentic-ai-analysis`), plus `llm-generation-relaxes` ×2, `adversarial-loop` ×2, `structure-inference`, `active-work-state`, `goedel-machines`. Likely keepers as `derived-from` (definitional syntheses worked out from cited papers — needs read): `definitions/reflective-system` ×2, `definitions/self-improving-system`, `definitions/actionable-methodology` ×2, `reasoning-production` (or `evidence`).

## Execution notes

- Review gates per `kb/reference/README-REVIEW-SYSTEM.md` for the gated rows; batch the ungated edge flips separately.
- Validate per collection after each batch; separate commits with explicit paths.
- The edge flips are near-mechanical once the needs-read rows are settled: one read each, then label + context-phrase edits.
