---
description: GBrain is Commonplace's closest category sibling — same component inventory (markdown KB, types, links, skills, maintenance cycle, promotion), opposite answers on where authority lives — and its popularity validates the category while obsoleting the RAG-strawman pitch
type: kb/types/note.md
traits: []
tags: []
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

## The frame that does NOT work

"The system decides vs the methodology decides" collapses on inspection: a methodology *is* a deciding system, because prose is executable by LLMs — Commonplace's own vocabulary says so (instructions, gates, and COLLECTION contracts are system-definition artifacts consumed with binding force). Both GBrain and Commonplace are systems that mix code and prose. The honest differences are the five placement axes above, which compress to:

- **GBrain: code writes, prose reads.** The write path is codified (extraction, consolidation, ranking in TypeScript with embedded LLM calls); consumption is prose-advised (skills tell the host agent what to do).
- **Commonplace: prose writes, code checks.** Writing and navigation are prose-executed (conventions, contracts); checking is codified (validators, schemas, review ledger).

Plus locus (own daemon vs inside your harness), admission polarity (default-ingest vs default-exclude), revision semantics (numeric decay/supersession vs dialectical contestation), and oracle (machine benchmarks vs human acceptance). Full descriptive treatment: [GBrain as an agentic system](../../agentic-systems/gbrain.md).

## Consequences for the pitch

- **The category is validated — the RAG strawman is obsolete.** [The knowledge layer for AI agents](./the-knowledge-layer-for-ai-agents.md) contrasts against RAG ("retrieval gives you recall, not reasoning"). GBrain also has markdown, links, skills, and synthesis; a reader who knows GBrain will not be moved by the RAG contrast. The differentiation that survives GBrain is the placement axes — especially "prose writes, code checks" and "runs inside the harness you already trust."
- **Candidate framings to test:** "the knowledge layer your agents can audit"; "git-native, review-gated knowledge — every change to what your agents believe is a diff"; "no second runtime — your harness is the engine."
- **The planned capture layer changes the story from rivalry to composition.** Commonplace intends to add a capture-everything layer (decision 2026-06-12), borrowing heavily from GBrain's write side: signal detection, fact extraction with provenance, validity/supersession metadata, consolidation phases, durable background jobs. The differentiating move is keeping the existing promotion boundary: ambient capture lands in a default-ingest layer with expiry and provenance, and only review-gated promotion crosses into the library. That is GBrain's write machinery feeding Commonplace's trust machinery — adopt their capture, keep our oracle.

## Open questions

- Does the GBrain comparison belong in public positioning (named head-to-head) or only as an internal frame? A respectful named comparison piggybacks on its popularity but invites rebuttal on infrastructure features we lack by design.
- Capture-layer design questions to work out before borrowing: where the capture collection lives (workshop-like? its own register?), what expiry and provenance it carries, whether capture writes are agent-mediated (signal-detector-style skill) or service-mediated (we have no daemon — does Minions-style durable background work need a Commonplace answer, or is the harness's own scheduling enough?), and what the promotion gate from capture to library reuses from the review system.
- GBrain's borrowable ideas (freshness/lineage gates on generated context, maintenance as a phase graph) are also *positioning* evidence: adopting them while keeping git-native authority demonstrates the stance rather than asserting it.
