# Link-label audit

## Question

The link-relationship vocabulary is declared in two places that already disagree, and the corpus drifts further from both. What should the canonical vocabulary be — prune drift to match declared rules, or expand declared rules to absorb used-and-useful labels the corpus has invented?

Pursued under a soft-rules stance: no validation yet, deviations treated as data.

## Where the vocabulary is declared

- [ADR 009](../../reference/adr/009-link-relationship-semantics.md) — five labels: `extends`, `grounds` (also `foundation`), `contradicts`, `enables`, `exemplifies` (also `example`). Declared stable; expansion requires an explicit decision.
- Per-register outbound tables in `kb/notes/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/instructions/COLLECTION.md`, `kb/agent-memory-systems/COLLECTION.md`.
- Aggregated by `cp-skill-compile-collections` into [`kb/reports/collection-topology.md`](../../reports/collection-topology.md).

**Existing schism.** The aggregated matrix adds labels ADR 009 does not list: `since`, `because`, `qualifies`, `evidence`, `derived-from`, `rationale`, `justification`, `reference`, `composition`, `cross-reference`, `see-also`, `supersedes`, `procedure`. Some are prose connectors (`since`, `because`) that belong to the inline-link grammar rather than the typed-footer vocabulary; others (`supersedes`, `qualifies`) look like genuine relationship types ADR 009 never adopted.

**Corpus drift (spot check).** Off-vocabulary labels observed in real footer annotations so far: `foundation`, `sharpens`, `mechanism`, `complements`, `splits from`, `clarifies`, `parent index`, `extracted from`, `acknowledges`. Some feel load-bearing (`foundation`, `sharpens`); others look like localized prose that could fold into `extends`.

## Theory we're accountable to

From [`linking-theory.md`](../../notes/linking-theory.md): link quality is decision-cost reduction per token of context consumed. A label earns its place if it lets an agent decide follow/skip differently than an adjacent label would. Vocabulary size is a trade-off — too few loses discrimination, too many inflates authoring cost. Linking-theory flags this as an open question: *"Is the vocabulary the right one?"*

Related:
- [ADR 009](../../reference/adr/009-link-relationship-semantics.md) — the decision under examination.
- [title-as-claim-enables-traversal-as-reasoning](../../notes/title-as-claim-enables-traversal-as-reasoning.md) — claim titles plus typed links make traversal read as a reasoning chain; label choice affects whether the chain parses.
- [link-strength-is-encoded-in-position-and-prose](../../notes/link-strength-is-encoded-in-position-and-prose.md) — position and prose carry commitment level; footer-label taxonomy composes with the position axis rather than replacing it.

## Plan

1. **Extract the corpus.** Throwaway `python3` script walking `kb/**/*.md`, pulling every `- [title](path) — <label>[:/] …` annotation from footer sections. Classify source collection and target collection from paths. Write results to `kb/reports/link-vocabulary.md` (machine-managed, overwritten on rerun).
2. **Categorize labels per edge.** For each (source register → target register) row, list observed labels with frequency; flag in-ADR-009, in-matrix, or off-vocab.
3. **Cluster off-vocab labels.** Group synonyms and near-synonyms by inferred meaning; identify candidates to promote, prune, or fold.
4. **Write up findings here.** What the drift reveals about gaps in ADR 009 and the matrix; tie results back to linking-theory predictions.
5. **Decide.** One of:
   - Update ADR 009 (or supersede it) to absorb labels the corpus validates.
   - Tighten COLLECTION.md linking tables and examples so authors drift less.
   - Accept drift as signal; leave rules soft and revisit later.

## What closes this workshop

- `kb/reports/link-vocabulary.md` exists and reflects the current corpus.
- Findings doc in this workshop summarises the categorized drift and ties it to linking-theory.
- A decision is recorded — as an ADR update, a COLLECTION.md edit, or a note that soft rules remain by choice.
