---
description: "How agents navigate a Commonplace KB using control-plane pointers, rg, titles/descriptions, indexes, links, connect reports, and possible future search layers"
type: kb/types/note.md
status: current
---

# Navigation

Commonplace navigation is a progressive disclosure stack. Agents should usually start with the cheapest surface that can answer the routing question, then load higher-resolution artifacts only when the cheaper surface justifies it.

## Current Stack

| Layer | What it provides | When to use it |
|---|---|---|
| `AGENTS.md` | Always-loaded goals, scope boundaries, key indexes, commands, and routing conventions | Cold start and task routing |
| `rg` | Cheap lexical search over files | Exact names, phrases, vocabulary, commands, and local evidence |
| Scoped `rg` listings | Path-plus-description slices for a tag or collection, computed on demand | Enumerate candidates in a collection or tag without loading a complete inventory |
| Curated indexes | Topic-organized entry points with short context phrases | Entering a known area such as links, architecture, or related systems |
| Descriptions | Fixed retrieval filters for individual artifacts | Decide whether a search or index hit is worth opening |
| Links | Local navigation with authored relationship context | Follow a premise, rationale, implementation, definition, or related artifact from an already-loaded source |
| `cp-skill-connect` reports | Deeper candidate discovery plus articulation testing | When a note needs graph integration beyond obvious links |
| Full artifact reads | Complete argument, procedure, source, or reference detail | Only after the pointer layer identifies a likely target |

`rg` is the current cheap retrieval layer. It is not ranked like BM25, but it fills the same first-pass role at the present KB size: quickly surface lexical candidates without invoking an inference pipeline.

Descriptions are the important middle layer. They are not decorative summaries; they are fixed, agent-facing filters between lexical search and full reads. A good description lets an agent scan five plausible hits and decide which one to open. This is why validation requires descriptions and why scoped listings and build-time indexes are built from them.

Curated indexes are the collection-scale version of the same idea: grouping and context phrases where the order and headings carry extra routing signal. A directory's curated head is its `README.md`; a tag's curated head is its `<tag>-README.md` (type `tag-readme`), small by type contract.

A tag-README may declare two validator-enforced frontmatter marks (ADR 026): `complete: true` — the README links every note carrying the tag, so a reader can skip the by-tag `rg` recipe below for that tag; `covered_by: [children]` — every tagged note carries a listed child tag, so a reader can trust the README's typed routing ("which kind of X is this?"). Both are accelerators, never load-bearing: scoped `rg` always recovers membership regardless of any mark — full semantics in [mark-semantics.md](./mark-semantics.md).

## Complete listings are build-time only

Complete generated listings — per-collection `dir-index.md` pages and per-tag generated tails — are not committed and are not on any agent read path. They are materialized at mkdocs build time for the published site, where human readers skim and Ctrl-F them sublinearly ([ADR 025](./adr/025-complete-generated-indexes-are-build-time-only.md)). An agent reads a file whole, so a complete inventory costs linear context for whichever consumer can least afford it; the agent path is the curated head plus a scoped `rg` listing over the slice it needs.

### Scoped listing recipes

By tag — path plus description for every note carrying a tag:

```bash
rg -l '^tags:.*\bTAG\b' kb/notes/ --glob '*.md' \
  | xargs -r rg -N --no-heading '^description:\s*' -r ''
```

The `xargs -r` guard matters: a tag matching zero files would otherwise make `rg` run with no path arguments and search the whole repo.

One known blind spot: the by-tag pattern only matches the corpus-standard inline form (`tags: [a, b]`); a note using block-style YAML tags is invisible to it (the validator's checks parse YAML and are not affected). Keep tags inline when authoring.

By keyword or whole collection — descriptions under any scope:

```bash
rg '^description:' kb/<collection>/ --glob '*.md'
rg -l '<keyword>' kb/<collection>/ --glob '*.md' \
  | xargs -r rg -N --no-heading '^description:\s*' -r ''
```

These return `path + description`; the path stands in for the title during triage. Open the candidate body only after a description earns it.

Links are narrower and richer. They do not replace search; they work after the agent already has local context. The surrounding prose or footer label should explain why following the target helps from this source.

## Scaling Shape

The current stack works because the KB is still small enough that `rg`, curated indexes, and descriptions fit the agent's effective working process. Growth creates two separate pressures:

1. **The core must stay scannable.** High-signal notes, reference docs, and indexes should remain small enough for agents to browse as a map. Larger source collections, archives, transcripts, and long reviews can live outside the core and be reached through explicit links or search.
2. **Search may need ranking.** When lexical results become too noisy or vocabulary mismatch becomes common, the system may need search stronger than `rg`.

These are complementary. A small curated core keeps reasoning and routing cheap. Better retrieval improves access into larger or less-curated text bases.

## Possible Future Layers

Near-term search improvement should probably be ranked lexical search: BM25 over titles, descriptions, paths, and bodies, with filters for collection, type, status, and path. This keeps the behavior inspectable and cheap while improving result ordering.

Semantic search is useful for vocabulary mismatch: cases where the agent asks with different words than the artifact uses. It should return candidates with titles, descriptions, paths, and matched passages rather than opaque answers, so the agent can still decide what to open.

Hybrid search can combine both: lexical precision for exact terms, semantic recall for paraphrase, and structural filters from frontmatter. The output should remain a candidate list, not a replacement for authored descriptions, indexes, and links.

Task-aware retrieval can come later if usage demands it. The mode should come from caller context when available: exact lookup, evidence search, related-note discovery, source lookup, contradiction search, or narrative synthesis. Query length alone is a weak routing signal for agents.

## Boundary

Navigation is not the same as linking. Navigation covers the whole path an agent uses to find what to read. Linking is the authored graph layer inside that path: labels, reader needs, and articulation tests for outbound edges.

---

Relevant Notes:

- [Storage](./storage-architecture.md) - part-of: authored markdown is the source of truth while generated indexes are rebuildable navigation artifacts
- [Collections and types](./collections-and-types.md) - part-of: collection conventions and type specs define where agents look before writing or linking
- [Link vocabulary and linking approach](./link-vocabulary.md) - part-of: the link-specific layer inside the broader navigation stack
- [Agent memory coverage](./agent-memory-coverage.md) - part-of: summarizes discoverability surfaces and current gaps across the shipped system
- [Link-following and search impose different metadata requirements](../notes/link-following-and-search-impose-different-metadata-requirements.md) - rationale: search, links, and indexes require different pointer metadata
- [Pointer design tradeoffs in progressive disclosure](../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) - rationale: descriptions, query-time search, and link phrases occupy different cost/specificity/reliability positions
- [Two context boundaries govern collection operations](../notes/two-context-boundaries-govern-collection-operations.md) - rationale: collections have both full-text and title-plus-description scan boundaries
- [Design for the first-time human, except on access cost](../notes/design-for-the-first-time-human-except-on-access-cost.md) - rationale: complete listings are routed to the consumer whose access mode makes them cheap — build-time pages for humans, scoped queries for agents
