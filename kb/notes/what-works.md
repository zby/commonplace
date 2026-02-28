---
description: Patterns proven valuable in practice — prose-as-title, template nudges, frontmatter queries, semantic search via qmd, discovery-first, public/internal boundary
type: review
areas: [claw-design]
status: current
---

# What works

Patterns that have proven valuable in practice.

## Prose-as-title convention

Note titles that work as claims when linked make the graph self-documenting. "Since [[thin adapters reduce coupling between providers and runtime]]" reads as prose and tells you what the note argues without opening it. Titles-as-labels ("adapter notes", "runtime thoughts") destroy this property. The theory behind this — why [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — also identifies where it breaks: multi-claim documents (specs, frameworks) get topical titles because no single claim subsumes their content.

## Template fields as behavioral nudges

Template fields like `description:` and `type:` guide agents to supply metadata at the moment of creation. The agent fills in the template, hits the empty field, and naturally asks "what should this be?" This is more reliable than documentation rules that the agent reads at session start and forgets. The `areas: []` field nudges agents toward curated area indexes — though notes are discoverable via auto-generated directory indexes regardless.

## Discovery-first as creation constraint

Checking findability *before* saving prevents orphan accumulation. Four questions: Does the title work as a claim? Does the description add information beyond the title? Is this linked from at least one index? Can this be linked without dragging irrelevant context? If any answer is no, fix it before saving.

## Frontmatter as queryable structure

YAML frontmatter turns a directory of markdown files into a queryable collection. `rg '^areas:.*architecture' docs/notes/` finds all architecture notes. `rg '^description:.*runtime' docs/notes/` searches summaries without opening files. In practice, `areas` and `description` are the fields that get queried — `description` especially, because it lets you decide whether to read the full note without opening it.

## Semantic search via qmd

`rg` handles structured queries (frontmatter fields, known keywords), but discovering *conceptually related* notes requires semantic search. [qmd](https://github.com/qmdnotes/qmd) runs locally on GPU with embeddings + reranking — no API calls, no latency.

The knowledge base is indexed as collections (`notes`, `adr`, `meta`, `docs`). Three search modes complement each other:

- `qmd search "query"` — BM25 keyword search, fast, good for known terms
- `qmd vsearch "query"` — vector similarity, finds conceptual neighbors even with different vocabulary
- `qmd query "query"` — hybrid: query expansion + keyword + vector + reranking (recommended default)

In practice, `qmd query` with `--files` flag is the workhorse for `/connect` discovery — it finds candidates that `rg` misses because they use different terminology for the same concept. The two tools are complementary: `rg` for structured/exact queries, `qmd` for semantic/fuzzy discovery. Both tools embody the pattern described in [files beat a database](./files-not-database.md): files remain the source of truth while derived indexes (qmd's embeddings, rg's grep) provide capabilities files alone cannot.

Keeping the index current: `qmd update && qmd embed` re-scans and re-embeds changed files. Both are idempotent and fast.

## Public/internal boundary

Keeping knowledge system artifacts out of public docs (`docs/*.md`) prevents coupling. Public documentation has its own audience and conventions. Internal notes can evolve freely without worrying about external readers.

Topics:
- [claw-design](./claw-design.md)
