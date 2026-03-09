---
description: Comparable knowledge/agent systems tracked for evolving ideas, convergence signals, and borrowable patterns
type: index
---

# Related Systems

External systems doing similar work — knowledge management for AI agents, context engineering, structured note-taking. We track these not just to borrow ideas but to watch how they evolve. Convergence across independent projects is a stronger signal than any single design argument.

## Systems

- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — skill-based context engineering reference library loaded as agent guidance; strong on operational patterns, no learning theory
- [Ars Contexta](./arscontexta.md) — Claude Code plugin that generates knowledge systems from conversation; ancestor of our KB, upstream source for link semantics and title-as-claim. Includes the "Agentic Note-Taking" article series (@molt_cornelius) — first-person agent testimony from inside the system
- [Thalo](./thalo.md) — custom plain-text language with grammar, types, validation, and LSP; makes the same programming-theory bet we do but with full compiler formalization
  - [Thalo entity types compared to commonplace document types](./thalo-type-comparison.md) — detailed type mapping showing gaps (supersedes links, source status tracking) and borrowable patterns
- [ClawVault](./clawvault.md) — TypeScript memory system with scored observations, session handoffs, and reflection pipelines; has a working workshop layer where we have theory, strongest source of borrowable patterns for ephemeral knowledge
- [CrewAI Memory](./crewai-memory.md) — unified vector-memory for agent crews with LLM-driven scope inference, composite scoring, and consolidation; sophisticated retrieval infrastructure but no learning theory, treating memory as plumbing rather than a knowledge medium
- [Siftly](./siftly.md) — Next.js + SQLite ingestion system with deterministic-first enrichment, resumable stage markers, and hybrid retrieval; strongest reference so far for high-volume source loading patterns
- [sift-kg](./sift-kg.md) — LLM-powered document-to-knowledge-graph pipeline with schema discovery, human-gated entity resolution, and interactive visualization; strongest reference for extraction-first knowledge construction and confidence aggregation

## Patterns Across Systems

Most systems here (ours, Ars Contexta, Thalo, ClawVault, Agent-Skills) independently converge on:
- **Filesystem over databases** — plain text, version-controlled, no lock-in
- **Progressive disclosure** — load descriptions at startup, full content on demand
- **Start simple** — architectural reduction outperforms over-engineering

The divergences are more revealing:
- **Storage model** — Siftly uses SQLite and CrewAI uses LanceDB (embedded vector database) as operational substrates, while the others keep files as the primary storage interface. CrewAI is the furthest from filesystem-first: memories are opaque vector records, not readable files
- **Grounding discipline** — cognitive psychology (arscontexta) vs programming theory (commonplace, thalo) vs empirical operational patterns (Agent-Skills)
- **Formalization level** — custom DSL (thalo) vs YAML conventions (commonplace) vs prose instructions (Agent-Skills)
- **Self-referentiality** — only our KB is simultaneously a knowledge system and a knowledge base about knowledge systems

## Open Questions

- Does convergence on filesystem-first indicate a durable pattern, or a phase that will be outgrown?
- Should high-volume ingestion in a file-first KB adopt a small operational database layer for stage state and indexing?
- Will the programming-theory grounding produce better systems than the psychology grounding, or will they converge?
- Are there systems we're missing that take a fundamentally different approach?
