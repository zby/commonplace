---
description: Comparable knowledge/agent systems tracked for evolving ideas, convergence signals, and borrowable patterns
type: index
---

# Related Systems

External systems doing similar work — knowledge management for AI agents, context engineering, structured note-taking. We track these not just to borrow ideas but to watch how they evolve. Convergence across independent projects is a stronger signal than any single design argument.

**Two coverage tiers.** Systems with open-source repos get the deep path: clone the repo, read the code, write a review note here. Systems known only from a README or paper get the lightweight path: snapshot a single page into `kb/sources/`, run `/ingest`, and the ingest report is the coverage. The [comparative review](./agentic-memory-systems-comparative-review.md) synthesises across both tiers. Database-backed memory systems (Mem0, Graphiti, Letta, A-MEM, AgeMem) currently have only lightweight coverage via ingest reports in `kb/sources/`.

## Systems

- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — skill-based context engineering reference library loaded as agent guidance; strong on operational patterns, no learning theory
- [Ars Contexta](./arscontexta.md) — Claude Code plugin that generates knowledge systems from conversation; ancestor of our KB, upstream source for link semantics and title-as-claim. Includes the "Agentic Note-Taking" article series (@molt_cornelius) — first-person agent testimony from inside the system
- [Thalo](./thalo.md) — custom plain-text language with grammar, types, validation, and LSP; makes the same programming-theory bet we do but with full compiler formalization
  - [Thalo entity types compared to commonplace document types](./thalo-type-comparison.md) — detailed type mapping showing gaps (supersedes links, source status tracking) and borrowable patterns
- [ClawVault](./clawvault.md) — TypeScript memory system with scored observations, session handoffs, and reflection pipelines; has a working workshop layer where we have theory, strongest source of borrowable patterns for ephemeral knowledge
- [CrewAI Memory](./crewai-memory.md) — unified vector-memory for agent crews with LLM-driven scope inference, composite scoring, and consolidation; sophisticated retrieval infrastructure but no learning theory, treating memory as plumbing rather than a knowledge medium
- [Siftly](./siftly.md) — Next.js + SQLite ingestion system with deterministic-first enrichment, resumable stage markers, and hybrid retrieval; strongest reference so far for high-volume source loading patterns
- [sift-kg](./sift-kg.md) — LLM-powered document-to-knowledge-graph pipeline with schema discovery, human-gated entity resolution, and interactive visualization; strongest reference for extraction-first knowledge construction and confidence aggregation
- [Letta](../../sources/letta-memgpt-stateful-agents.ingest.md) — agent-self-managed three-tier memory hierarchy using OS analogy (main context ≈ RAM, archival ≈ disk, recall ≈ conversation log); strongest existing exemplar of the agent-self-managed agency model *(lightweight coverage only — ingest report, no repo review)*
- [Mem0](../../sources/mem0-memory-layer.ingest.md) — two-phase add pipeline (extract facts + LLM-judged CRUD reconciliation); purest production example of automated accretion-without-synthesis in the surveyed systems *(lightweight coverage only — ingest report, no repo review)*
- [Graphiti](../../sources/graphiti-temporal-knowledge-graph.ingest.md) — temporally-aware knowledge graph with bi-temporal edge invalidation; strongest counterexample to files-first architecture and strongest temporal model in the surveyed systems *(lightweight coverage only — ingest report, no repo review)*
- [Cognee](./cognee.md) — pipeline-first knowledge engine (add/cognify/memify/search) with Pydantic-schema graph extraction, poly-store backends (graph + vector + relational), and multi-tenancy; strongest database-side counterexample to files-first architecture, but treats knowledge as a data engineering problem rather than a curation problem
- [Spacebot](./spacebot.md) — Rust concurrent agent framework with code-level symbolic scheduling (cortex), context-forking branches, typed memory with graph edges and hybrid search; cleanest production implementation of the bounded-context orchestration model among reviewed systems
- [Decapod](./decapod.md) — Rust governance kernel for AI coding agents with proof-gated completion, workspace isolation, and 120+ embedded constitution documents; strongest reference for hard-oracle verification in agent workflows, though constitution claims transformation where the code primarily relocates
- [Hindsight](./hindsight.md) — biomimetic agent memory with LLM-driven fact extraction, four-way parallel retrieval (semantic + BM25 + graph + temporal), auto-consolidation into observations, and agentic reflection; strongest production evidence that three-space memory separation yields measurable retrieval gains (LongMemEval SOTA)
- [Napkin](./napkin.md) — Obsidian-vault CLI with `NAPKIN.md` pinned context, TF-IDF overview maps, agent-shaped search defaults, and pi-based auto-distill; strongest reference for adapting a mainstream human note substrate into an agent-facing memory interface
- [SAGE](./sage.md) — BFT-branded agent memory with CometBFT consensus, Ed25519 signing, application-level validators (sentinel, dedup, quality, consistency), confidence decay, and AES-256-GCM encryption; the consensus framing is ceremony around a deterministic validation pipeline in single-node mode, but the validation gate pattern and domain-scoped RBAC are genuinely useful
- [getsentry/skills](./getsentry-skills.md) — Sentry's shared skills repo with a skill-writer meta-skill that codifies the skill creation process: source-driven synthesis with depth gates, labeled iteration, description-as-trigger optimization, and the Agent Skills cross-tool spec; strongest reference for how to systematically create and improve agent skills
- [Fintool](../../sources/lessons-from-building-ai-agents-for-financial-services-2015174818497437834.ingest.md) — AI agent for professional investors; S3-first with derived PostgreSQL, markdown skills with copy-on-write shadowing, ~2000 eval test cases; strongest production-scale evidence for filesystem-first at commercial grade *(lightweight coverage only — ingest report, no repo review)*
- [Pi Self-Learning](./pi-self-learning.md) — pi extension with automatic task-end reflection, scored learnings index, and context injection; purest implementation of the automated mistake-extraction loop, but the reflection pipeline primarily relocates rather than transforms
- [Nuggets](./nuggets.md) — Pi-coupled personal memory assistant with local HRR nugget files, chat-channel scheduling, and a MEMORY.md promotion bridge; strongest reference so far for tiny file-backed scratch memory, though the promotion loop is only partially wired
- [OpenViking](./openviking.md) — ByteDance/Volcengine's context database with filesystem-paradigm virtual directories, L0/L1/L2 tiered loading, hierarchical recursive retrieval, and session-driven memory extraction; first production system to make progressive disclosure a native storage primitive, but the "filesystem" is a metaphor over a database, not actual files
- [Autocontext](./autocontext.md) — closed-loop control plane for iterative agent improvement via multi-role orchestration (competitor/analyst/coach/architect), tournament evaluation, accumulated playbooks, and MLX distillation; strongest reference for automated iterative learning loops, but context "compilation" is concatenation with budget-aware trimming, not transformation

## Patterns Across Systems

Most systems here (ours, Ars Contexta, Thalo, ClawVault, Agent-Skills) independently converge on:
- **Filesystem over databases** — plain text, version-controlled, no lock-in
- **Progressive disclosure** — load descriptions at startup, full content on demand
- **Start simple** — architectural reduction outperforms over-engineering
- **Trace-derived learning** — [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) broadens the comparison beyond pi-adjacent session mining to include artifact-learning and weight-learning systems fed by live traces and trajectories

The divergences are more revealing:
- **Storage model** — Cognee uses a poly-store (graph + vector + relational with pluggable backends), Siftly uses SQLite, CrewAI uses LanceDB (embedded vector database), Hindsight uses PostgreSQL+pgvector, and SAGE uses SQLite+BadgerDB (personal) or PostgreSQL+pgvector (multi-node) as operational substrates, while the others keep files as the primary storage interface. OpenViking occupies a novel middle position: it presents a filesystem interface (`viking://` URIs, `ls`/`read`/`find` operations) but the substrate is AGFS + vector index — filesystem as metaphor, not mechanism. Cognee, Hindsight, CrewAI, and SAGE are the furthest from filesystem-first: memories are opaque database records, not readable files
- **Agent-facing UX** — Napkin is the clearest example of treating CLI output itself as part of the memory architecture: hidden scores, match-only snippets, and next-step hints are all tuned for model behavior rather than human browsing. Most other systems focus on storage and retrieval internals but leave the interaction layer human-shaped
- **Grounding discipline** — cognitive psychology (arscontexta) vs programming theory (commonplace, thalo) vs empirical operational patterns (Agent-Skills)
- **Formalization level** — custom DSL (thalo) vs YAML conventions (commonplace) vs prose instructions (Agent-Skills)
- **Governance stance** — most systems treat governance as advisory (instructions the agent should follow); Decapod enforces governance with hard gates (validation must pass, VERIFIED requires proof-plan); SAGE enforces with cryptographic gates (signed transactions, validator quorum, RBAC clearance levels) — two very different enforcement models, both structurally enforced rather than instructed
- **Access control** — SAGE has structured multi-agent RBAC (clearance levels, domain-scoped permissions, on-chain agent identity); Cognee has relational ACLs with tenant isolation and per-dataset permissions; most other systems either have no access control or rely on filesystem permissions
- **Self-referentiality** — only our KB is simultaneously a knowledge system and a knowledge base about knowledge systems

## Open Questions

- Does convergence on filesystem-first indicate a durable pattern, or a phase that will be outgrown?
- Should high-volume ingestion in a file-first KB adopt a small operational database layer for stage state and indexing?
- Will the programming-theory grounding produce better systems than the psychology grounding, or will they converge?
- Are there systems we're missing that take a fundamentally different approach?

## Other tagged notes <!-- generated -->
