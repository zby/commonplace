---
description: "Design rationale and decision log for the agent-memory-systems review framework and comparison matrix — why reviews carry extractable lead tokens, why the matrix is one-hot, and why the review lifecycle is split into write-side and read-side."
type: kb/types/note.md
tags: [agent-memory]
status: current
---

# Review framework and comparison matrix: design and decisions

This collection reviews external agent-memory systems against a shared vocabulary so independent systems can be set side by side. Two artifacts carry that comparison: the per-system reviews under `reviews/`, written to the [review type spec](./types/agent-memory-system-review.md), and [`systems.csv`](./systems.csv), a matrix **parsed from the reviews** by `commonplace.lib.systems_matrix` (run via `scripts/build_systems_matrix.py`). This note records the motivations and the design decisions behind that machinery, so later changes start from the reasoning rather than re-deriving it.

It is a collection-scoped decision log, deliberately *not* a `kb/reference/adr/` record: those govern the shipped Commonplace system, whereas this governs how *this collection* reviews and compares external systems. The format is ADR-style (context / decision / consequences) for rigour.

## Why a parsed matrix at all

A prose-only survey cannot answer "how many systems do X", and a hand-maintained table drifts from the reviews it summarises. So the comparison data lives as **extractable lead tokens** in the review prose — `**Storage substrate:** \`sqlite\` — …` — where the controlled value leads its own justifying sentence, and a parser lifts the tokens into the matrix. Value and reasoning cannot drift apart, and the matrix rebuilds from the reviews on demand.

## Decisions

### D1 — One-hot indicator columns for multi-valued axes

**Context.** Early axes used a single value with a `mixed`/`both` escape hatch (`representational_form` was 81% `mixed`; `read_back_direction` had a `both` bucket). These buckets hid exactly the information the axis was meant to expose, and a system genuinely *is* several things at once (Zikkaron pushes by `coarse` *and* `identifier` *and* `inferred` selection simultaneously).

**Decision.** Encode every multi-valued axis as one-hot indicator columns — one column per controlled value, `1` present / `0` assessed-absent / blank not-assessed. Authors emit the *set* of backticked tokens; the parser one-hots whatever appears. Single-valued axes (`storage_substrate`) stay single; `rb_pull`/`rb_push` derive for free from the direction token.

**Consequences.** The `mixed`/`both` buckets are retired (forbidden by schema for representational form). Each value becomes independently sortable/filterable. The faithful retrofit authored ~9 tokens across each of 129 reviews. Blank-vs-`0` must be kept distinct so "not assessed" never reads as "assessed absent".

### D2 — Authored tokens, never mined

**Context.** The signal axis was first populated by mining the review prose. Zikkaron exposed the failure: its prose said "coarse session context" without backticking `coarse`, so mining recorded `sig_coarse=0` — wrong. At least 23 reviews under-counted `coarse` the same way.

**Decision.** The matrix is populated only from authored lead tokens; mining is abandoned. An applicable axis with no token is left blank and **flagged**, making the flag list the precise retrofit worklist. `not-determinable` is an explicit token for "the review genuinely cannot tell", distinct from a missing token.

**Consequences.** Faithfulness over completeness: a blank is honest, a guess pollutes. The parser lives in `commonplace.lib.systems_matrix` with unit tests and a converted-review fixture; the schema is cleaned to the live columns (no dead placeholders).

### D3 — Lifecycle split: write side vs read side

**Context.** The review had a strong **read-back** treatment and a strong **trace-derived learning** treatment, but maintenance/curation had no home — it was scattered across Lineage, the trace section, and Core Ideas prose. The gap surfaced concretely: ~24 reviews authored a "post-action read-back", but reading them showed the post-action leg was almost always *capture/consolidation* ("…for later turns"), not a read. Two arguments make "post-action read-back" a category error: (1) an LLM is stateless between calls, so any memory that reaches it is pre-(next-)invocation by construction; (2) more fundamentally, at retrieval the store holds all the information it has — nothing new and relevant arrives afterward except the agent's own output, so there is nothing to push later. What fires after the turn is **maintenance**, not a second read.

A second realisation sharpened the cut: when maintenance is **manual**, it *is* curation, and it runs through the same authoring channel as acquisition — so "acquire" and "maintain" are not separate phases. They share the write channel; what varies is agency (manual vs automatic) and operation.

**Decision.** Model the review as **write side** (everything that changes the store) and **read side** (read-back, which only serves it). The write side carries two axes — **agency** (`manual`/`automatic`) and **curation operations** — with **trace-derived learning** demoted to a sub-section (the automatic-from-traces case). Manual curation is recorded as `agency: manual` only; it has no separate mechanism (it is authoring on existing content), its provenance is Lineage `authored`, and its quality is an affordances question in Core Ideas. Read-back loses its pre/post "timing" axis: there is one injection point, pre-invocation; the read's *trigger* may be noted, but not a timing.

**Consequences.** Maintenance finally has a home (the curation-operations axis, D4). The `**Read-back timing:**` token and its `rb_pre_action`/`rb_post_action` columns are removed. The trace-derived learning material becomes a `### Trace-derived learning` sub-section under the required `## Write side` section. Rather than spawn a thin "no post-action read-back" note, read-back keeps its operational definition in this review spec and is *situated relative to activation* in [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md) (the storage→context step — necessary for activation but not the same as it); the no-post-action point is a corollary of that single pre-invocation injection point.

### D4 — Curation-operations vocabulary

**Context.** Giving maintenance a home revives the "curation operations" dimension the comparative review once listed and the matrix had dropped as "aspirational" — it was never aspirational, just homeless.

**Decision.** A seven-value controlled set, each a distinct design choice: `consolidate` (abstract a group), `dedup` (remove redundancy), `evolve` (modify an existing entry in place as neighbours arrive, A-MEM-style), `synthesize` (generate a new cross-entry insight — rare), `invalidate` (supersede on contradiction, keep history), `decay` (forget by age/capacity), `promote` (change tier/salience). Index/embedding rebuilds are access-structure upkeep, not content curation, and are excluded.

**Consequences.** `consolidate`/`evolve`/`synthesize` are kept distinct precisely so the matrix can show that consolidation is common while synthesis and evolution are rare — the comparative review's "everyone extracts, almost nobody synthesises" thesis becomes measurable. Pending: wiring these into the parser as one-hot columns and authoring them in the review retrofit.

### D5 — Matrix covers code-reviewed systems only

**Context.** Lightweight (doc-grounded) coverage is a lower evidence tier, and a comparison table is for *choosing* a system.

**Decision.** The matrix and its consumption table cover `code-grounded` systems only (the `source-tier` frontmatter value the build keys on); `doc-grounded` reviews under `lightweight/` are excluded from the contract and the build.

**Consequences.** Findings quantify the 129 code-grounded systems; doc-grounded coverage remains a landscape surface, not comparison data.

### D6 — One review type; evidence tier is a field, not a type

**Context.** There were two types — `agent-memory-system-review` (code-grounded) and `lightweight-review` (doc-grounded) — carrying the *same* comparison elements; the lightweight spec itself said its label was "about authority, not scope." The matrix already keyed inclusion on directory, not type (D5). Two specs that must say the same thing drifted: the write-side/read-side methodology update (D3) was applied to the code-grounded type but the lightweight type was forgotten. That forgetting is the signature of duplication that should be one artifact.

**Decision.** Collapse to a single `agent-memory-system-review` type with a required `source-tier: code-grounded | doc-grounded` frontmatter field as the one authority marker. Delete `lightweight-review.md` and its schema; make the merged spec's instructions **tier-neutral** so the doc-grounded deltas (claim-level evidence stance, document-not-repo source metadata, source-URL citations, promotion) are phrased inline for both tiers rather than in a separate section — the `source-tier` field is the only discriminator. **One equally-strict schema** for both tiers — doc-grounded reviews lean on `not-determinable` where sources are silent, which is authoring discipline, not a schema branch. Keep the `reviews/` vs `lightweight/` directory split as physical organisation only; the build keys on `source-tier`, not the path. The matrix `source_tier` value moves `repo-reviewed` → `code-grounded` to match the field.

**Consequences.** One source of truth for the methodology — the drift class of D3-vs-lightweight is eliminated. Promotion from doc- to code-grounded is now a field flip, not a type conversion. `source-tier` is required, so every review backfills it during the layout retrofit. Folding this in, the schema was also tightened to enforce what the spec already called required but didn't — `## Artifact analysis` and the `**Read-back:**` verdict. The directory split stays a convenience, no longer load-bearing.

### D7 — Targeting is the read-back signal; drop the `push_engineered` flag

**Context.** The matrix carried a `push_engineered` column (the `push-activation` tag echoed as a boolean) for "the system pushes *targeted*, relevance-gated memory, not a coarse always-load dump." But the **Read-back signal** axis already encodes exactly that: a `coarse` signal is generic recall; an `instance` signal (`identifier` or `inferred`) *is* a targeted push. So `push_engineered` was a second representation of the same fact — and `systems.csv` should carry each fact once.

**Decision.** Remove the `push_engineered` column and the `push-activation` tag. Targeting is read solely from the Read-back signal (`coarse` vs `instance`); the optional push-specific part inside the required `## Read-back` section triggers on direction (`push`/`both`), not a tag. No derived `targeted_push` column is stored either — the render table collapses the `sig_*` one-hots for display, but the normalized store keeps only the signal.

**Consequences.** One representation of targeting, nothing to author or over-tag separately. The build stops emitting `push_engineered`; review frontmatter keeps only `trace-derived` when that learning path applies. (The same normalization argument applies to the derived `rb_pull`/`rb_push` one-hots, kept for now as filter conveniences per D1 — revisit if normalization is tightened further.)

## Open follow-ons

- ~~**Review regeneration:** the structural retrofit (write-side heading, `source-tier`, timing removal) landed corpus-wide, but the prose-normalization pass that authored the write-side *tokens* over-tagged them — `synthesize` (the rare op) appeared on 88% of reviews, because a post-hoc axis cannot be back-filled faithfully from prose written before it existed. That approach was abandoned in favor of regenerating reviews from source.~~ — done (all 129 reviews regenerated via the `write-agent-memory-system-review` skill; the [`none` curation token](./types/agent-memory-system-review.md) later split assessed-absent from not-assessed, the gap the over-tagging had exposed).
- ~~Parser/matrix: add write-agency and curation-operation one-hot columns; drop `rb_pre_action`/`rb_post_action`~~ — done (`wa_*`/`op_*` columns carried; timing columns removed). Validator severity is now per-constraint, fail by default ([ADR-024](../reference/adr/024-schema-severity-is-per-constraint-fail-by-default.md)).
- ~~Theory note for "no post-action read-back"~~ — resolved by pinning `read-back` in the activation-gap note rather than adding a note.

---

Relevant Notes:

- [agentic-memory-systems-comparative-review](./agentic-memory-systems-comparative-review.md) — see-also: the synthesis this framework feeds
- [symbolic context engineering is bounded by symbol availability](../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) — rationale: grounds the read-back signal taxonomy and the single-injection-point argument
