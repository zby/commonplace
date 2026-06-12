---
description: GBrain is Commonplace's closest category sibling — same component inventory (markdown KB, types, links, skills, maintenance cycle, promotion), opposite answers on where authority lives — and its popularity validates the category while obsoleting the RAG-strawman pitch
type: kb/types/note.md
traits: []
tags: []
status: seedling
---

# GBrain is the category sibling, not just a reviewed memory system

The [GBrain review](../../agent-memory-systems/reviews/gbrain.md) classifies it as an agent memory system, but its own analysis shows more: "partly a memory service and partly an agent-operating-system package." Component for component, GBrain is the closest sibling Commonplace has in the reviewed corpus — closer than any of the other ~16 systems — and it is popular (Garry Tan's project). Positioning has to account for it.

## The isomorphism

| Commonplace | GBrain |
|---|---|
| Markdown KB, git-canonical | Markdown "brain repo" + Postgres/PGLite active store |
| Type system (type specs + JSON schemas) | Schema packs, page types |
| Collections with COLLECTION.md contracts | Sources with source scoping |
| Authored, labeled links | Typed edge tables + automatic link extraction |
| Curated indexes + rg navigation | Hybrid keyword/vector/graph/reranker search |
| 9 promoted cp-skill-* skills | 43-skill skillpack + installer protocol |
| Review gates + acceptance ledger (SQLite) | Lint gates, take grading, calibration, eval capture |
| Review sweeps, maintenance instructions | Dream cycle (runCycle phase graph) |
| Workshop → note promotion; seedling → current | Facts → takes → concepts/patterns promotion |
| commonplace-* CLI | CLI + MCP operations layer |

Shared stance: prose files as operational artifacts, skills as the adoption mechanism, background maintenance that promotes accumulation into stronger artifacts, promotion paths with authority gradients.

## The divergences — these are the positioning axes

1. **Where authority lives.** GBrain's behavior-shaping substrate is the database; markdown is a write-through facade (its review notes much behavior-shaping state lives only in tables). In Commonplace every behavior-shaping artifact is a git-diffable file; the only DB is a bookkeeping ledger. Review and rollback are ordinary diffs versus a trusted runtime surface.
2. **Retrieval philosophy.** GBrain inserts a service between agent and knowledge (embeddings, RRF, rerankers, caches, pushed `_meta` facts). Commonplace inserts nothing: the harness's agent is the retrieval engine (rg, curated indexes, authored links). "No standalone app" is a stance, not a roadmap gap.
3. **Write discipline and epistemics.** GBrain captures ambiently (signal detector on every inbound message) and extracts automatically, with per-claim review its own reviewer calls uneven; units are facts/takes with confidence numbers. Commonplace writes are deliberate, typed, register-aware, validated, review-gated; units are contestable claims. GBrain optimizes recall of what happened; Commonplace optimizes trustworthiness of what is claimed.
4. **Learning-loop oracle.** SkillOpt mutates instructions behind machine benchmarks and held-out gates; Commonplace's gate-learning design holds the oracle at human-accepted edits.
5. **Product shape.** GBrain is an installable runtime (daemon, MCP transport, OAuth, queues). Commonplace is a methodology plus a thin deterministic CLI inside the harness you already trust.

## Consequences for the pitch

- **The category is validated — the RAG strawman is obsolete.** [The knowledge layer for AI agents](./the-knowledge-layer-for-ai-agents.md) contrasts against RAG ("retrieval gives you recall, not reasoning"). GBrain also has markdown, links, skills, and synthesis; a reader who knows GBrain will not be moved by the RAG contrast. The differentiation that survives GBrain is where authority lives and how knowledge earns trust.
- **The comparative review's flagship finding is the frame.** "The fundamental split is who decides what to remember": GBrain answers *the system decides, continuously*; Commonplace answers *the methodology decides, with review*. That line positions both systems honestly in one sentence and reuses the showcase asset ([related-systems-as-showcase](./related-systems-as-showcase.md)).
- **Candidate framings to test:** "the knowledge layer your agents can audit"; "git-native, review-gated knowledge — every change to what your agents believe is a diff"; service-native vs git-native as the category split (GBrain anchors one pole, Commonplace the other).
- **The audiences may genuinely differ.** GBrain serves capture-everything personal/team memory; Commonplace serves teams whose knowledge must be *right* (methodology, design decisions, claims with provenance). "Both" is not a weakness if named: capture-side system feeding a review-gated library is a plausible composition story, not a rivalry.

## Open questions

- Does the GBrain comparison belong in public positioning (named head-to-head) or only as an internal frame? A respectful named comparison piggybacks on its popularity but invites rebuttal on infrastructure features we lack by design.
- Is "agent memory system" the wrong shelf for GBrain in our own corpus — should `kb/agentic-systems/` carry a whole-system analysis of it (the review covers memory; the operating-system half, skillpack adoption protocol, and dream-cycle orchestration are agentic-system territory)?
- GBrain's borrowable ideas (freshness/lineage gates on generated context, maintenance as a phase graph) are also *positioning* evidence: adopting them while keeping git-native authority demonstrates the stance rather than asserting it.
