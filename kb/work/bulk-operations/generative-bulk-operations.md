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

## The shared prerequisite: structure specs bigger than a document

Both cases produce a **document set** — a structured collection of documents with a shape of its own:

- the code wiki's output *is* a document set (pages + index + link structure);
- the deep search's output is a ranked report over per-pair judgment records — the records are the members, the report is the derived index. Same shape, thinner.

Commonplace's type surface currently specifies single documents. A document-set spec would additionally fix:

1. **Membership rule** — which member documents must exist: fixed members plus corpus-derived members (a function that enumerates the corpus: one page per module, one judgment per surviving candidate).
2. **Member types** — the per-document contract each member follows (this part the existing type system already covers).
3. **Cross-member obligations** — required links between members, terminology consistency, non-overlap of coverage.
4. **Derived views** — the index or matrix regenerated from the members.
5. **Set-level validation** — completeness of membership, link resolution across members, index coverage. Deterministic once the spec exists.
6. **Lineage to the corpus** — the member→sources mapping recorded at generation time, so refresh targets are computable from a corpus diff.

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

## Relation to the workshop

This likely splits into its own direction — "compound artifacts / document-set specs" is a type-system question, not only a bulk-operations question. But the dependency runs one way: generative bulk operations cannot be sharded, validated, or refreshed without a set spec, while the set spec is useful even without bulk execution (a human-authored wiki still benefits from set-level validation). If the direction spins off, this workshop keeps the pipeline/economics questions and consumes the spec as an input contract.

## Open questions

- Minimal spec shape: is a document-set spec a new type kind under `kb/types/`, an extension of `COLLECTION.md`, or a standalone manifest (a `systems.csv` generalization)?
- How declarative can the membership rule be? "One page per module" needs a corpus enumerator — code, or agent judgment recorded as a committed target list?
- For funnels: which prefilter tiers are deterministic commands and which are cheap agent passes, and where is the cut recorded so the recall trade-off is auditable ("candidates dropped at tier 1" is part of the run record)?
- Calibration at merge: rubric-in-packet vs comparative re-ranking pass vs both — when is each proportional?
- Set-level lineage format: where does the member→sources mapping live so a corpus diff can be turned into a refresh target list mechanically?
