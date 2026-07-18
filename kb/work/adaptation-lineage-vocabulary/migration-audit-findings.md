# Migration audit findings

Corpus evidence for the workshop's [migration audit](./README.md#migration-audit), gathered by two independent sub-agent passes over the distillation-retirement commit range. Anchors are commit + path; classify, don't mechanically revert.

## Finding 1 — "condense/condensing" reintroduced as an unacknowledged 4th operator

Commit `593c60af` mechanically swapped `distill(ation)` → `condense/condensing` in several places where the surrounding sentence lists it as a **peer operator** to Constrain/Discover/Prune — i.e., exactly the general "conversion" slot the old term held, now under a new label with no citation, no definition, and no review tracking:

- `kb/notes/raw-accumulation-does-not-create-usable-memory.md:20` — "**Constraining** ... **Condensing** reshapes diffuse material ... **Discovery** ... **Pruning** ..."
- `kb/notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md:35` — "the operators (codify, relax, constrain, condense)"
- `kb/notes/treat-continual-learning-as-substrate-coevolution.md:55` — same operator-list pattern
- `kb/notes/deploy-time-learning-is-the-missing-middle.md:34` — "Two operators drive the updates: constraining ... and condensing"

This is the exact recurrence ADR 053's Consequences section warned about ("the control trap can recur under any future attractive label") — it happened inside the same migration, unreviewed, because "condense" reads as ordinary English and slipped past the write-time uniqueness check.

Related: commit `f7aac9e6` separately coined **"Extraction"** as a capitalized, defined successor term (own comparison-table row) for the SEL-dominant sense of old distillation, then propagated it across 70+ generated backlink footers corpus-wide. Same underlying gap — a real operation lost its name and something informal filled the slot — different word, different commit, same unreconciled state. Neither "extraction" nor "condense" is in ADR 053, the migration plan's four-part decision, or AGENTS.md's vocabulary list.

## Finding 2 — the same operation classified inconsistently across files

Two cases where structurally identical content got opposite DER/AMP treatment because no single classification pass reconciled cross-file references:

1. **Trace re-extraction language.** `kb/notes/agent-memory-requirements/preserve-evidence-without-loading-history.md:305,311,320` and `serve-multiple-consumers.md:333`: "redistillation" of raw session traces into reusable artifacts → **"re-derivation"** (asserts strong entailment-preservation). But `kb/reference/commonplace-agent-memory-gap-plan.md:1822`, same concept → **"re-abstraction"** (correctly ampliative).
2. **Probe-generation from logged failures.** `kb/notes/elicitation-requires-maintained-question-generation-systems.md:1016`, checklist step "Distill updates" → **"Condense updates"** — but the step is instance→rule generalization (AMP), not compression. The cross-reference to the identical lifecycle step in `kb/notes/open-domain-memory-retention-needs-a-declared-output-spec.md:1261` → "...log-misses/**abstract**/prune..." (correct AMP treatment).

## Finding 3 — the migration's flagship "derive" case may itself be judgment, not derivation

`kb/notes/skills-derive-from-methodology.md` (replacing `skills-derive-from-methodology-through-distillation.md`) is cited from ~15 other notes as the paradigm case of entailment-preserving reshaping. Its own body states the skill "adds no substantive claims the methodology does not already support" (the derivation bar) — then two paragraphs later: "A different person reading the same methodology would produce a meaningfully different skill... the process requires judgment." Output that varies meaningfully by author is the third, ungoverned case (selects sources, packages judgment) — see Finding 4 — not strict derivation. This note argues itself into the DER bucket while its own evidence sits closer to the third case.

## Finding 4 — the original "ad-hoc distillation" term survives untouched and untracked

`kb/work/lineage-mechanisms/` (README.md, current-practices-and-theory.md, model-provenance.md, storage-weight-across-cases.md, general-lineage-refresh-state-design.md) still defines and uses "ad-hoc distillation" as a stable term meaning "selects sources, packages judgment" — this is exactly the third operation this workshop needs to name (candidate: `adapted-from`). It was never migrated, renamed, or flagged in ADR 053's Consequences/deferred list (which only names the agent-memory-systems type-spec, kb/sources, and the crystallized-reasoning coinage as deferred). Treat as untracked deferral, not settled ground.

## Lower-confidence, worth a second look

- `kb/notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md:204` — "**Derivation** and implementation often connect the profiles" — capitalized, unlinked, uncited on first use; reads like a proper-noun successor term rather than ordinary English.
- `kb/notes/definitions/context-engineering.md:757` — "Reshaping recorded knowledge ... producing derived views, summaries, and handoff artifacts — is the main operation" — dilutes "derived" to cover the whole context-engineering operational core, most of which is authored summarization judgment, not entailment-preservation.

## Confirmed clean (no mislabeling found)

- The 16 `derived-from` → `abstracted-from` lineage-edge flips in `4175dbb3` — each genuinely marks a claim generalizing beyond a single cited source, matching the commit's stated reasoning.
- `757d6daa`'s retirement of `distillation-is-transformation-not-selection.md` — its load-bearing claim (trace→rule adds a condition clause and rationale, i.e. ampliative not derivation) was correctly preserved into `abstract-an-experience-only-when-you-can-state-the-boundary.md`.
- `9e252b41`'s derived-from/abstracted-from gloss fix in both COLLECTION.md files — correct, matches link-vocabulary semantics.

## What this evidences for the workshop's evaluation boundary

Findings 1–4 together are direct evidence for the `methodology → skill/checklist/gate` and `session state/trace → summary/handoff` rows of the [evaluation boundary table](./README.md#evaluation-boundary): both rows predicted judgment/selection pressure that "derive" doesn't cover, and the corpus shows writers reaching for ad hoc, uncoordinated fixes ("condense," "extraction," "re-abstraction," lingering "ad-hoc distillation") instead of a named third relation.

## Coverage note

Two sub-agent passes covered: `f7aac9e6`, `4175dbb3`, `757d6daa`, `9e252b41` (read in full) and `593c60af` (the large Wave 2/3 commit). Not yet audited for the same failure class: `b35ea92c`, `c7cc78f4`, `4c0c3cf8`, `b0b775c7`.
