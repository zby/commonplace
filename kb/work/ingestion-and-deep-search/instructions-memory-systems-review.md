# Instructions: Comparative Review of Agentic Memory Systems

## Goal

Produce a comparative review of five agentic memory systems — Mem0, Graphiti, Cognee, Letta (MemGPT), and A-MEM — plus the four filesystem-first systems already documented as related systems (Ars Contexta, Thalo, ClawVault, Agent Skills for Context Engineering, and our own commonplace system).

The review should identify the **key architectural dimensions** along which these systems vary, place each system on those dimensions, and surface the design trade-offs that matter for anyone building an agent knowledge system.

This is NOT a summary of each system. Each ingest report already has that. This is a **cross-cutting comparison** that reveals what the design space looks like.

## Inputs

Read ALL of the following documents:

### New ingest reports (the four we just produced)
1. `kb/sources/mem0-memory-layer.ingest.md`
2. `kb/sources/graphiti-temporal-knowledge-graph.ingest.md`
3. `kb/sources/cognee-knowledge-engine.ingest.md`
4. `kb/sources/letta-memgpt-stateful-agents.ingest.md`

### Previously ingested source
5. `kb/sources/a-mem-agentic-memory-for-llm-agents.ingest.md`

### Existing related system notes
6. `kb/notes/related-systems/arscontexta.md`
7. `kb/notes/related-systems/thalo.md`
8. `kb/notes/related-systems/clawvault.md`
9. `kb/notes/related-systems/agent-skills-for-context-engineering.md`

### Current related systems index (for context on existing patterns)
10. `kb/notes/related-systems/related-systems-index.md`

## Questions to answer

1. **What are the key architectural dimensions?** The ingest reports independently surfaced several: storage unit (facts vs notes vs graph triplets), memory agency (self-managed vs external API), link structure (none vs untyped vs typed), temporal model (none vs timestamps vs bi-temporal), curation operations (append-only vs LLM-judged CRUD vs evolution). Are there others? Refine and finalize the dimension set.

2. **Where does each system sit on each dimension?** Place all 9-10 systems (Mem0, Graphiti, Cognee, Letta, A-MEM, Ars Contexta, Thalo, ClawVault, Agent Skills, commonplace) on the dimension matrix. Be specific — don't just say "graph-based", say what kind of graph and why it matters.

3. **What convergences emerge?** The related-systems-index already notes convergence on filesystem-over-databases, progressive disclosure, start-simple. Do the new four systems confirm or break these patterns? (Spoiler: they break them — Graphiti, Cognee, and Mem0 are all database-first.)

4. **What divergences are most revealing?** The filesystem-first vs database-first split is the most obvious. But are there deeper ones? The agency question (who decides what to remember) seems fundamental. The curation question (what happens to old knowledge) also seems important.

5. **What does this mean for KB design?** Given the full landscape, what are the strongest signals about where our system should go? What are we missing? What have we gotten right?

## Output spec

Save the review as: `kb/sources/agentic-memory-systems-comparative-review.md`

Structure:
- Title as a claim (what the review found, not "Comparative Review of...")
- A dimension matrix (table or structured list placing each system)
- Convergences section
- Divergences section
- Implications for KB design
- No frontmatter needed — this is a workshop output, not a KB note

Write concisely. The review should be readable in 5 minutes, not 20.
