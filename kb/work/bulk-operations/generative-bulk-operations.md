# Generative bulk operations and document-set specs

The workshop README frames bulk operations as maintenance over artifacts that already exist in the KB: review reruns, migrations, validation sweeps, triage. Two motivating cases do not fit that frame, and analysing why exposes a missing prerequisite: a way to specify **structures bigger than a single document**.

## The two cases

### Code wiki

Given a codebase, produce a wiki: an architecture overview, one page per module, pages for cross-cutting concepts, a navigation index, and cross-links between pages. Bulk in the **write** direction — many derived documents from one corpus.

What makes it hard as a bulk operation:

- **Sharding requires the output structure first.** "Write a wiki for this repo" is unboundable; "write the page for module X, following this page type, linking per this contract" is a packet. The shard plan cannot be derived from the corpus alone — it needs a spec of what the wiki *is*.
- **Membership is partly fixed, partly corpus-derived.** Some pages are required unconditionally (overview, index, getting-started); others are a function of the corpus (one page per module, enumerated from the source tree). The spec must express both.
- **Cross-member obligations.** Pages must link to related pages; the index must cover every page; terminology must be consistent across pages. None of this is checkable per-document — it is validation of the *set*.
- **Set-level lineage.** Each page derives from an identifiable set of source files. When the code changes, the stale-page list is computable from the diff — but only if the page→sources mapping was recorded at generation time. This is the lineage-driven-refresh case family, at the level of a document set rather than a single artifact.

### Deep-similarity corpus search

Given a query document (a legal case, a patent claim), find documents in a large corpus that are similar in a deep sense — analogous reasoning, overlapping claim elements — not merely adjacent in embedding space. Bulk in the **read** direction: many judgments against one query.

What makes it hard as a bulk operation:

- **The pipeline is a funnel, not a flat map.** LLM judgment per candidate pair is expensive, so selection must be tiered: cheap recall stages (lexical search, vector similarity, metadata filters) narrow the corpus to candidates; the expensive precision stage (per-candidate deep comparison in a clean context) runs only on survivors. "Select" is not one stage with one oracle — it is a cascade with explicit recall/precision economics, where vector similarity is demoted from the answer to a prefilter.
- **The lens is parameterized by the query document.** Every worker compares its candidate against the same query. Re-reading the raw query per worker wastes context and invites drift; instead, distill the query once into a comparison brief (the claims, elements, and distinguishing features that matter) and frontload the brief into every packet — the [frontloading](../../notes/frontloading-spares-execution-context.md) pattern applied to a fan-out.
- **Merge needs calibration.** Similarity scores produced in independent contexts are not comparable; a rubric in the packet helps, and a final comparative re-ranking pass over the per-pair judgments may be needed. Merging is a judgment stage of its own, not concatenation.
- **The justification is the product.** A bare ranked list reproduces vector search's weakness: adjacency without reasons ("Notes Without Reasons" — links without articulated reasons degrade trust). Each surviving candidate must carry the articulated grounds of similarity: which elements map, which distinguish. The per-pair judgment records are durable artifacts, not intermediate scratch.
- **A preparation phase — bulk write of a semantic index.** If the corpus will be queried more than once, comparing raw documents per query wastes the same distillation work repeatedly. The alternative is a preparation phase: a bulk write producing one comparison-ready distillate per corpus document (extracted claim elements for patents, holdings and reasoning structure for cases), plus derived views over them. The per-query funnel then runs brief-against-distillate instead of raw-against-raw — cheaper tiers, and precision tiers that read structured representations instead of full documents. Preparation cost amortizes over queries, so a one-off search may not justify it; a standing corpus does. This is the LLM-era version of editorial indexing — legal headnotes and key-number taxonomies, patent classification codes — which were exactly a manual bulk write of comparison-ready structure over a corpus.

## The shared prerequisite: structure specs bigger than a document

Both cases produce a **document set** — a structured collection of documents with a shape of its own:

- the code wiki's output *is* a document set (pages + index + link structure);
- the deep search's output is a ranked report over per-pair judgment records — the records are the members, the report is the derived index. Same shape, thinner;
- the deep search's *preparation phase* output is a full-strength document set: one distillate per corpus document (corpus-derived membership), derived views over them, and lineage for refresh as the corpus grows.

The preparation phase dissolves the read/write dichotomy: the read-direction operation decomposes into a write-direction generative bulk operation (build the semantic index once) plus a per-query funnel over its members. A prepared corpus index and a code wiki are the same kind of object — both are document sets generated from a corpus; they differ only in the consumer (query-time comparison workers vs human/agent readers).

Commonplace's type surface currently specifies single documents. A document-set spec would additionally fix:

1. **Membership rule** — which member documents must exist: fixed members plus corpus-derived members (a function that enumerates the corpus: one page per module, one judgment per surviving candidate).
2. **Member types** — the per-document contract each member follows (this part the existing type system already covers).
3. **Cross-member obligations** — required links between members, terminology consistency, non-overlap of coverage.
4. **Derived views** — the index or matrix regenerated from the members.
5. **Set-level validation** — completeness of membership, link resolution across members, index coverage. Deterministic once the spec exists.
6. **Lineage to the corpus** — the member→sources mapping recorded at generation time, so refresh targets are computable from a corpus diff.

These six parts are requirements on the *information* that must be fixed somewhere, not a commitment to a schema — the solution space below covers representations from declarative specs to generator programs to mere exemplars.

This is a prerequisite for generative bulk operations, not a nice-to-have, because the spec is what each pipeline stage binds to:

| Stage | What the document-set spec supplies |
|---|---|
| Select | membership rule instantiated against the corpus = the target list |
| Shard | member type + owned output path = the packet contract; membership partition = collision boundaries |
| Execute | one member (or one derived view) per packet |
| Integrate | derived-view regeneration; cross-member obligation checks |
| Validate | set-level validation from the spec |
| Close | the set's lineage record becomes the refresh contract |

Note the inversion from the maintenance family: there, Select *finds existing artifacts*; here, Select *enumerates documents that ought to exist*. The target list is a list of obligations, not a list of inputs.

## Precedents already in the repo

The document-set idea is not speculative — the repo already operates one, implicitly:

- **`kb/agent-memory-systems/`** is a document set in everything but name: `systems.csv` is the membership registry, the `agent-memory-system-review` type is the member type, the comparative matrix and `systems-table.md` are derived views, and review reruns are the bulk refresh operation. The bulk operation works there precisely because the set structure was fixed first.
- **Collections (`COLLECTION.md`)** fix the authoring contract for a subtree but say nothing about required membership — a collection never *owes* a document. The document-set spec is the missing complement: a collection contract plus a membership rule.
- **tag-README marks (`complete`, `covered_by`)** are set-level validated claims over a membership rule ("every note carrying this tag is linked here") — an existing precedent for enforcing structure-level properties by code rather than trusting prose.

## Solution space — wider than types

The six-part spec above reads like a schema, which suggests a type-based solution. That is one point in a wider space; at the ideation stage the real question is *where the structure knowledge lives*, and the candidates span the [constraining](../../notes/definitions/constraining.md) spectrum:

- **Standing declarative spec** — a type, manifest, or `COLLECTION.md` extension: membership rule, member types, obligations, all validated by code. Strongest validation and refresh story; highest authoring cost; brittle when the right structure is not yet known.
- **Generator program** — the structure lives in code that enumerates the corpus and emits packets: the build-system shape. Membership rule = build rules, member→sources lineage = the dependency graph, refresh = incremental rebuild. Build systems solved set-level lineage decades ago; the LLM twist is that the "compiler" for each member is a judgment call, while enumeration and freshness stay deterministic.
- **Per-run plan artifact** — no standing spec at all: the operating agent derives a committed target list for this run (the relocation move-map and review selector JSON already work this way). The plan *is* the spec instance, consumed at close. Cheapest and most flexible; nothing is reusable and nothing guards the next run.
- **Exemplar** — fix the structure by one finished instance (a completed wiki for a small repo) and generate by analogy. Cheap to author, natural for agents, weakest to validate; good for one-offs and for discovering what the standing spec should later say.
- **Property-first** — specify only checkable set-level properties (every module discussed somewhere, every page reachable from the index, no two pages claiming the same scope) with no membership rule. Generation is free-form; validation sweeps plus fix loops converge the set. Corrective rather than constructive — tolerates emergent structure ([wikiwiki: lowest-friction capture, then progressive refinement](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md)).
- **Full regeneration** — treat the set as a compiled artifact: rebuild wholesale from the corpus plus retained judgment inputs instead of maintaining members. Freshness stops being a lineage problem and becomes a rebuild trigger; trades incrementality (and stability of member identity) for simplicity.

These compose rather than compete: a generator for enumeration, properties for cross-member obligations, an exemplar for member quality is a plausible stack. And the choice per case likely follows the usual codification trade-off — standing corpora with repeated refresh earn the codified end; one-off generations stay at plan-artifact or exemplar, with the exemplar route doubling as spec discovery.

## Relation to the workshop

This likely splits into its own direction — "how to fix structures bigger than a document" is a knowledge-representation question in its own right, not only a bulk-operations question. But the dependency runs one way: generative bulk operations cannot be sharded, validated, or refreshed without *some* answer from the solution space above, while that answer is useful even without bulk execution (a human-authored wiki still benefits from set-level properties). If the direction spins off, this workshop keeps the pipeline/economics questions and consumes the chosen mechanism as an input contract.

## Open questions

- Which mechanism from the solution space fits which case family, and what forces a case toward the codified end — refresh frequency, corpus size, number of consumers, or validation stakes?
- How declarative can the membership rule be? "One page per module" needs a corpus enumerator — code, or agent judgment recorded as a committed target list?
- For funnels: which prefilter tiers are deterministic commands and which are cheap agent passes, and where is the cut recorded so the recall trade-off is auditable ("candidates dropped at tier 1" is part of the run record)?
- Calibration at merge: rubric-in-packet vs comparative re-ranking pass vs both — when is each proportional?
- Set-level lineage format: where does the member→sources mapping live so a corpus diff can be turned into a refresh target list mechanically?
- Preparation economics and lens commitment: what query volume justifies building the semantic index, and what does the distillate spec fix — a distillate extracted for one comparison lens (claim overlap) may not serve another (infringement analysis), so the spec must name the lenses the index is built to serve?
