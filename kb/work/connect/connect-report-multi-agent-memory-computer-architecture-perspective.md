# Connection Report: Multi-Agent Memory from a Computer Architecture Perspective

**Source:** [multi-agent-memory-computer-architecture-perspective](kb/sources/multi-agent-memory-computer-architecture-perspective.md)
**Date:** 2026-03-13
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (lines 1-169, all entries) — flagged candidates:
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — memory taxonomy for agents
  - [three-space-memory-separation-predicts-measurable-failure-modes](kb/notes/three-space-memory-separation-predicts-measurable-failure-modes.md) — memory separation testing
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — 11-system comparison across memory dimensions
  - [memory-management-policy-is-learnable-but-oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem's learned memory management
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — context as the scarce resource
  - [context-engineering](kb/notes/context-engineering.md) — routing, loading, scoping, maintenance
  - [llm-context-is-composed-without-scoping](kb/notes/llm-context-is-composed-without-scoping.md) — flat concatenation, no isolation
  - [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — agent-agent coordination patterns
  - [hindsight](kb/notes/related-systems/hindsight.md) — biomimetic agent memory
  - [sage](kb/notes/related-systems/sage.md) — consensus-based agent memory
  - [two-context-boundaries-govern-collection-operations](kb/notes/two-context-boundaries-govern-collection-operations.md) — hierarchy of context boundaries
  - [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — symbolic scheduling over bounded calls
  - [synthesis-is-not-error-correction](kb/notes/synthesis-is-not-error-correction.md) — multi-agent error amplification patterns
  - [crewai-memory](kb/notes/related-systems/crewai-memory.md) — agent crew memory
  - [cognee](kb/notes/related-systems/cognee.md) — pipeline-first knowledge engine
  - Rejected at index scan: claw-learning-is-broader-than-retrieval (tangential), spacebot (process architecture, not memory), clawvault (session lifecycle, not architecture analogy)

**Topic indexes:**
- Read [learning-theory-index](kb/notes/learning-theory-index.md) — Memory & Architecture section confirmed candidates; no additional finds
- Read [related-systems-index](kb/notes/related-systems/related-systems-index.md) — confirmed Hindsight, SAGE, Cognee, CrewAI as related memory systems; no new candidates

**Semantic search (via qmd):**
- query "multi-agent memory architecture hierarchy shared distributed consistency protocol cache" --collection notes -n 15:
  - [hindsight](kb/notes/related-systems/hindsight.md) (88%) — strong match, memory system architecture comparison
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) (56%) — strong match, memory system survey
  - [related-systems-index](kb/notes/related-systems/related-systems-index.md) (43%) — routing only
  - [sage](kb/notes/related-systems/sage.md) (41%) — memory consistency/consensus
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (40%) — memory taxonomy
  - [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) (33%) — multi-agent coordination but weak match; evaluated, kept
  - Below 33%: bitter-lesson-boundary, injectable-configuration, enforcement-without-structured-recovery, claw-learning — all surface overlap only, rejected

- query "multi-agent memory architecture hierarchy shared distributed consistency protocol cache" --collection sources -n 10:
  - [a-mem-agentic-memory-for-llm-agents](kb/sources/a-mem-agentic-memory-for-llm-agents.md) (50%) — agent memory with links
  - [mem0-memory-layer-ingest](kb/sources/mem0-memory-layer-ingest.md) (41%) — memory system
  - [towards-a-science-of-scaling-agent-systems](kb/sources/towards-a-science-of-scaling-agent-systems.md) (33%) — multi-agent coordination overhead
  - Below 30%: trajectory-informed memory, induction bias — rejected, different domains

- query "agent memory coherence scoping coordination shared state" --collection notes -n 15:
  - [llm-context-is-composed-without-scoping](kb/notes/llm-context-is-composed-without-scoping.md) (52%) — strong match, scoping as coherence mechanism
  - [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) (44%) — already flagged
  - [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) (38%) — already flagged
  - [sage](kb/notes/related-systems/sage.md) (35%) — consensus/consistency
  - [spacebot](kb/notes/related-systems/spacebot.md) (34%) — rejected, process architecture not memory consistency

**Keyword search:**
- grep "memory.*hierarchy|cache.*layer|shared.*memory|memory.*consisten" kb/notes/ — found agentic-memory-systems-comparative-review, sage, crewai-memory (all already flagged)
- grep "memory.*coherence|distributed.*memory|memory.*architecture" kb/ — found sources (self-match) and notes already flagged

## Connections Found

### Strong Connections

- [The fundamental split in agent memory is not storage format but who decides what to remember](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) — **extends**: The paper provides a complementary architectural lens to the comparative review's six-dimensional analysis. Where the review identifies agency model as the most consequential design choice, the paper reframes the same design space through computer architecture abstractions — shared vs. distributed memory paradigms, three-layer hierarchy (I/O, cache, memory), and consistency protocols. The paper's consistency challenge directly addresses what the review identifies as unsolved: no system combines high agency, high throughput, and high curation quality. The consistency models the paper calls for are precisely the missing coordination layer.

- [Three-space agent memory maps to Tulving's taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) — **extends** (status: speculative): The paper's three-layer hierarchy (I/O, cache, memory) is an independent decomposition of agent memory from a different tradition (computer architecture vs. cognitive science). The Tulving mapping splits by content type and lifecycle; the paper splits by access latency and capacity. Together they form a two-axis model: content type (what kind of knowledge) and hierarchy level (how fast/limited the storage). The paper's hierarchy could explain why the three-space separation matters operationally — different content types naturally have different cache/persistence characteristics.

- [LLM context is composed without scoping](kb/notes/llm-context-is-composed-without-scoping.md) — **grounds** (status: seedling): The paper's memory consistency challenge — "read-time conflict handling under iterative revisions" and "update visibility and ordering" — is the multi-agent version of the scoping problem this note identifies for single contexts. The flat context has no scoping; the multi-agent setting has no consistency protocol. Both are the same underlying problem (shared mutable state without coordination primitives) at different scales. The paper's proposed consistency models would serve as inter-agent scoping mechanisms, complementing the sub-agent lexical scoping this note proposes within a single agent.

- [Context efficiency is the central design concern in agent systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **extends**: The paper's three-layer memory hierarchy (I/O/cache/memory) is the multi-agent generalization of the single-agent context efficiency problem. The note identifies context as the single scarce resource with volume and complexity dimensions; the paper adds a third dimension: inter-agent coherence. A CPU has registers, cache, RAM, disk; an LLM has one context window — the paper argues multi-agent systems need the full hierarchy back, not just the single window.

- [SAGE](kb/notes/related-systems/sage.md) — **exemplifies**: SAGE's consensus-validated memory writes (signed transactions, four validators, quorum-based acceptance) are a concrete implementation of the memory consistency protocols the paper calls for. SAGE's memory lifecycle (proposed -> committed -> challenged/deprecated) and confidence decay model address "update visibility and ordering" — the paper's most urgent challenge. The paper provides the theoretical framing that makes SAGE's approach legible as a consistency model rather than just governance ceremony.

- [Hindsight](kb/notes/related-systems/hindsight.md) — **exemplifies**: Hindsight's four-way parallel retrieval (semantic + BM25 + graph + temporal) and two-level consolidation (facts -> observations -> mental models) is a concrete implementation of the paper's three-layer hierarchy. The retain pipeline acts as the I/O layer (ingestion), parallel retrieval is the cache layer (fast limited-capacity access), and PostgreSQL + pgvector storage is the memory layer (large-capacity persistent). Hindsight lacks the consistency protocols the paper identifies as critical — it's a single-agent system and has no mechanism for multiple agents to coordinate writes.

### Moderate Connections

- [Memory management policy is learnable but oracle-dependent](kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — **extends**: AgeMem's LTM/STM split (persistent store vs. active context) maps directly onto the paper's memory/cache layers. The paper argues this split needs principled protocols; AgeMem shows the policy for managing it (when to cache, when to persist) can be learned via RL, but only with task-completion oracles. The paper's protocol gap — no standardized cache sharing or memory access protocols — explains why AgeMem's learned policy doesn't transfer across systems.

- [Conversation vs prompt refinement in agent-to-agent coordination](kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — **extends** (status: seedling): The paper's shared vs. distributed memory paradigm maps onto this note's conversation vs. prompt refinement distinction. Conversation is shared memory — accumulated context visible to all participants, requiring coherence. Prompt refinement is distributed memory — each sub-agent gets an independent, curated context. The paper's consistency challenge (when does a write become visible to other agents?) is exactly the problem conversation-based coordination faces as context accumulates.

- [Two context boundaries govern collection operations](kb/notes/two-context-boundaries-govern-collection-operations.md) — **extends** (status: seedling): The paper's three-layer hierarchy (I/O, cache, memory) is the multi-agent generalization of this note's two-boundary model (full-text boundary, index boundary). The note describes how single-agent operations degrade as collections cross context boundaries; the paper describes how multi-agent operations need explicit hierarchy management for the same reason. The index boundary is the single-agent version of the paper's "cache layer."

- [Synthesis is not error correction](kb/notes/synthesis-is-not-error-correction.md) — **extends** (status: seedling): The paper's memory consistency challenge is load-bearing for why synthesis fails in multi-agent settings. Kim et al.'s 17.2x error amplification in independent agents is a consistency failure — agents with no shared state and no coherence protocol produce conflicting outputs that synthesis merges uncritically. The consistency protocols the paper calls for would provide the coordination layer that prevents this amplification.

**Bidirectional candidates** (reverse link also worth adding):
- [agentic-memory-systems-comparative-review](kb/notes/related-systems/agentic-memory-systems-comparative-review.md) <-> source — **extends**: The review provides the empirical landscape; the paper provides the architectural theory. Both would benefit from cross-reference.
- [three-space-agent-memory-maps-to-tulving-taxonomy](kb/notes/three-space-agent-memory-maps-to-tulving-taxonomy.md) <-> source — **extends**: Two independent decompositions of the same design space from different intellectual traditions.
- [llm-context-is-composed-without-scoping](kb/notes/llm-context-is-composed-without-scoping.md) <-> source — **grounds**: The paper provides the multi-agent extension that makes the single-agent scoping analysis more general.

## Rejected Candidates

- [context-engineering](kb/notes/context-engineering.md) — The paper's memory hierarchy and context engineering share vocabulary ("getting the right knowledge into a bounded context"), but the connection is too general. Every note about agent systems connects to context engineering at some level. No specific mechanism or insight transfers that isn't already captured through the context-efficiency and scoping connections.
- [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — Surface overlap: both involve scheduling and bounded resources. But the orchestration model is about symbolic scheduling over single bounded LLM calls, while the paper is about memory coordination across multiple agents. Different problems despite shared vocabulary.
- [crewai-memory](kb/notes/related-systems/crewai-memory.md) — CrewAI is a multi-agent memory system, but the existing note focuses on retrieval engineering and lacks the architectural depth needed for a meaningful connection. The connection would reduce to "both are about multi-agent memory" without articulating why.
- [cognee](kb/notes/related-systems/cognee.md) — Pipeline-first knowledge engine, but single-agent oriented. The paper's multi-agent consistency challenge doesn't apply to Cognee's architecture.
- [towards-a-science-of-scaling-agent-systems](kb/sources/towards-a-science-of-scaling-agent-systems.md) — The scaling paper discusses multi-agent coordination overhead and error amplification, but its focus is on task performance scaling, not memory architecture. The connection would be indirect — via synthesis-is-not-error-correction which already bridges them.
- [claw-learning-is-broader-than-retrieval](kb/notes/claw-learning-is-broader-than-retrieval.md) — Learning breadth vs. the paper's architectural memory model; no specific mechanism connects them.

## Index Membership

- [learning-theory-index](kb/notes/learning-theory-index.md) — Memory & Architecture section. The paper provides the computer architecture framing that complements the cognitive science framing (Tulving taxonomy) and the empirical system reviews already in this section. It introduces consistency protocols as a new concern not yet represented.
- [related-systems-index](kb/notes/related-systems/related-systems-index.md) — The paper isn't a system to track, but the "Patterns Across Systems" section could reference the paper's architectural taxonomy as a lens for comparing memory designs across systems.
- Not yet a member of any index.

## Synthesis Opportunities

**Memory architecture needs both a content-type axis and a hierarchy-level axis.** The three-space model (Tulving: semantic/episodic/procedural) splits memory by content type and lifecycle. The paper's three-layer model (I/O/cache/memory) splits by access characteristics and capacity. Neither is sufficient alone. A two-axis model would predict that different content types (knowledge, self, operational) have different optimal placements in the hierarchy (what should be cached vs. persisted vs. streamed). This could produce a note synthesizing three-space-agent-memory-maps-to-tulving-taxonomy and this paper into a unified memory taxonomy.

**Consistency is the multi-agent generalization of scoping.** The flat-context scoping problem (llm-context-is-composed-without-scoping) and the multi-agent consistency challenge (this paper) are the same structural problem at different scales: shared mutable state without coordination primitives. A synthesis note could argue that agent memory consistency and context scoping are instances of a general coordination problem, with sub-agent isolation and consistency protocols as solutions at different granularities.

## Flags

- No split candidate issues
- Tension: The paper assumes memory hierarchy is the right lens for agent memory, while the three-space model uses cognitive science. These are complementary but could conflict if they prescribe different architectural boundaries.
