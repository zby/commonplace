---
description: Generative Agents memory SDK with five-type decay, six-phase dream cycles, entity graph, Hebbian reinforcement, and clinamen anomaly retrieval; richest trajectory-to-lesson loop reviewed
type: related-system
tags: [related-systems]
traits: [has-comparison, has-external-sources]
status: current
last-checked: "2026-03-24"
---

# Cludebot

Cludebot ([sebbsssss/cludebot](https://github.com/sebbsssss/cludebot)) is an open-source TypeScript SDK and MCP server providing persistent memory for AI agents, built by Sebastien Sim. Originally created as the memory system for an autonomous AI agent on X ([@Cludebot](https://x.com/Cludebot)), the core is published as the `clude-bot` npm package. It implements the Stanford Generative Agents scoring formula (Park et al. 2023), extends it with type-specific decay, entity knowledge graphs, multi-phase dream cycles, action-outcome learning, and anomaly retrieval. Three deployment modes: hosted API (zero-setup), self-hosted Supabase + pgvector, and local JSON file (`~/.clude/memories.json`). MIT licensed.

**Repository:** https://github.com/sebbsssss/cludebot

## Core Ideas

**Five memory types with type-specific decay rates.** Memories are classified into `episodic` (0.93/day), `semantic` (0.98/day), `procedural` (0.97/day), `self_model` (0.99/day), and `introspective` (0.98/day). Decay is applied per 24h cycle, and each type's rate reflects how quickly that kind of knowledge loses relevance. Retrieval also applies a knowledge-type boost: semantic memories get +0.15, procedural +0.12, self_model +0.10, episodic +0.0. This means distilled knowledge structurally outranks raw events in recall scoring, independent of query relevance.

**Hybrid retrieval with six scoring signals.** The recall pipeline runs: (1) query expansion via a fast LLM (Llama 3.2 3B via OpenRouter, 3s timeout), (2) parallel vector search at both memory-level and fragment-level via pgvector HNSW, (3) parallel metadata-filtered keyword search + BM25 full-text search, (4) knowledge-seed injection (curated factual memories always compete in scoring), (5) entity-aware expansion (direct entity recall + co-occurring entity memories), (6) bond-typed graph traversal following strong links (causes > supports > resolves > elaborates). All signals are merged into a composite score: `(w_recency * recency + w_relevance * relevance + w_importance * importance + w_vector * vector_similarity + w_graph * graph_boost) * decay_factor`. Vector similarity dominates at weight 4.0; keyword relevance and importance share 2.0 each; recency is 1.0; graph boost is 1.5.

**Granular fragment decomposition for sub-memory retrieval.** Each stored memory is decomposed into semantic fragments: summary, content chunks (split at sentence boundaries), and a tag-context fragment that wraps tags and concepts into natural language. Each fragment gets its own embedding and is stored in a `memory_fragments` table. Fragment-level vector search runs in parallel with memory-level search, and the highest similarity score per memory (across all fragments) is used. This enables precise matching on parts of a long memory that the summary alone might miss.

**Six-phase dream cycle with event-driven triggering.** The dream cycle fires when accumulated importance exceeds a threshold (event-driven, Park et al. 2023) or every 6 hours (cron fallback). Six phases run sequentially: (1) **Consolidation** -- generates focal-point questions from recent episodic memories, retrieves relevant memories per question, and produces evidence-linked semantic insights with cop-out detection (discards "Good question..." responses). (2) **Compaction** -- finds old (7+ day), faded (decay < 0.3), low-importance (< 0.5) episodic memories, groups by concept, summarizes groups into semantic memories with evidence links, marks originals as compacted. (3) **Reflection** -- reviews self-model memories with evidence citations. (4) **Contradiction resolution** -- finds unresolved `contradicts` links, resolves them, accelerates decay on the weaker memory. (5) **Action learning** -- analyzes action-outcome pairs, generates procedural strategies. (6) **Emergence** -- introspective synthesis, optionally posted to X.

**Action learning closes the action-outcome-lesson loop.** Three components: an Action Logger that records what the agent did with reasoning and trigger context; an Outcome Tracker that revisits actions and records results with sentiment (positive/negative/neutral) and numeric scores; and a Strategy Refiner that groups action-outcome pairs by feature, identifies patterns (>60% negative outcomes = caution rule, >70% positive = reinforce), and uses Claude to generate procedural memory rules. Successful strategies are reinforced via Hebbian boosting (+0.05 importance per relevant positive outcome). Social outcomes are tracked by fetching tweet engagement metrics after 6+ hours.

**Entity knowledge graph with auto-extraction and co-occurrence.** Entities (person, project, concept, token, wallet, location, event) are extracted from memory content via rule-based heuristics (Twitter handles, Solana addresses, token tickers, capitalized multi-word names) and stored in a dedicated `entities` table with embeddings. Entity mentions link entities to memories with salience scores based on position and frequency. Co-occurring entities (mentioned in the same memory) automatically get `co_mentioned` relations. The graph supports entity-based recall ("Tell me about Seb"), entity co-occurrence expansion in retrieval, and visualization for the dashboard.

**Clinamen -- anomaly retrieval as structured serendipity.** Named after Lucretius' concept of atomic swerve, `find_clinamen` retrieves high-importance memories with low relevance to the current context. The divergence score is `importance * (1 - vectorSimilarity)`. Filters require importance >= 0.6, vector similarity < 0.35, and age >= 24 hours. Falls back to importance-only with randomized selection when embeddings are unavailable. Exposed as an MCP tool for agents to surface unexpected connections.

**Progressive disclosure via summaries-then-hydration.** The `recallSummaries()` + `hydrate()` pattern returns lightweight `MemorySummary` objects (no content field) first, letting the consumer select which memories to fully load. Dream cycle consolidation uses this pattern internally -- summaries for focal-point generation, full content only for deep analysis.

**Hebbian co-retrieval reinforcement.** When memories are recalled together, their access counts increment, decay factors reset, and association links between co-retrieved memories are strengthened. This creates a positive feedback loop: memories that are useful together become increasingly likely to be recalled together. An anti-confabulation gate differentiates internal sources (reflections, dreams, consolidations) from external sources (user interactions, imports), applying reduced reinforcement to internally generated memories.

## Comparison with Our System

| Dimension | Cludebot | Commonplace |
|---|---|---|
| Storage substrate | Supabase (PostgreSQL + pgvector) or local JSON file | Filesystem-first; notes are markdown files under version control |
| Memory taxonomy | episodic / semantic / procedural / self_model / introspective (flat enum with decay rates) | note / structured-claim / adr / index / related-system (typed with templates and structural expectations) |
| Write path | SDK call with optional LLM importance scoring, fire-and-forget embedding + entity extraction + auto-linking + on-chain commit | Human writes markdown; zero infrastructure required |
| Retrieval | Six-signal hybrid: vector + keyword + BM25 + tag + entity graph + bond traversal | `rg` keyword search + description scanning + tag filtering + qmd hybrid search |
| Consolidation | Automated dream cycle with LLM-driven focal points, compaction, and contradiction resolution | Manual: human writes notes, `/connect` discovers relationships |
| Learning loop | Closed: action → outcome → lesson (procedural memory from action-outcome patterns) | Open: human observes, writes notes, distills into instructions |
| Graph model | Entity knowledge graph (auto-extracted) + memory association bonds (10 typed link types) | Standard markdown links with explicit relationship semantics (extends, foundation, contradicts, enables, example) |
| Decay model | Type-specific exponential decay applied per 24h cycle + access-based reinforcement | Manual `status` field (current/outdated/speculative) |
| Inspectability | Opaque without API/SQL access (self-hosted) or dashboard (hosted); local mode stores JSON | Fully inspectable: every note is a readable file |
| Anomaly surfacing | Clinamen: explicit anti-relevance retrieval for lateral thinking | No equivalent mechanism |

**Where cludebot is stronger.** The learning loop. The action logger → outcome tracker → strategy refiner pipeline is the most complete trajectory-to-lesson system among reviewed systems. It closes the loop: the agent acts, measures results, generates procedural rules, and reinforces successful strategies. Dream cycle consolidation with focal-point questions and compaction handles knowledge lifecycle without human intervention. Clinamen is genuinely novel -- no other reviewed system has an explicit mechanism for structured serendipity.

**Where commonplace is stronger.** Knowledge structure. Cludebot's memories are flat text blobs with a type enum, tags, and optional links. There are no structural templates, no compositional hierarchy, no index navigation. Our type system with templates, link semantics with explicit relationships, tag indexes with curated sections, and progressive disclosure through directory structure provide organizational depth that cludebot's flat storage cannot match. And inspectability -- every piece of knowledge is a readable file with version history.

**The fundamental trade-off.** Cludebot invests in automation (LLM-driven consolidation, automatic decay, Hebbian reinforcement, entity extraction) at the expense of knowledge structure. Commonplace invests in knowledge structure (types, links, indexes, methodology) at the expense of automated lifecycle management. Cludebot's memories age and consolidate without human attention; commonplace's notes accumulate without automated curation.

## Borrowable Ideas

**Clinamen anomaly retrieval** -- the divergence formula (`importance * (1 - similarity)`) is a clean, implementable heuristic for surfacing unexpected connections. When we eventually build automated connection suggestions beyond what `/connect` does today, this "structured serendipity" pattern could complement the relevance-based approach. *Needs a use case first* -- our KB is small enough that manual browsing catches most cross-cutting connections. At 500+ notes, explicit anti-relevance search becomes valuable.

**Cop-out detection in LLM-generated content** -- the `COPOUT_PATTERNS` regex array that catches "Good question..." and "Let me think about that..." before storing dream cycle outputs. This is a simple, effective quality gate for any LLM-generated knowledge artifact. *Ready to borrow* -- could be added to semantic review or any automated note-generation pipeline. Trivial to implement.

**Action-outcome-lesson pipeline as a model for operational learning** -- the three-phase structure (log what happened → measure results → extract rules) is a clean decomposition of the learning problem. We don't have automated outcome tracking, but the conceptual framework maps to our manual process: the agent acts (writes a note), the human evaluates (reviews quality), and lessons are distilled (into writing instructions). Making this loop more explicit and tracked could improve our methodology refinement. *Needs a use case first* -- requires an automated evaluation pipeline we don't have.

**Event-driven processing triggered by importance accumulation** -- instead of fixed-interval dream cycles, cludebot accumulates importance scores from stored memories and triggers reflection when a threshold is exceeded. This is a smarter scheduling heuristic than pure cron: process when there's enough material to process. If we ever build automated maintenance sweeps, importance-accumulation triggering is better than "every N hours." *Needs a use case first.*

**Fragment-level embedding for sub-memory retrieval** -- decomposing notes into semantic fragments (summary, content chunks, tag context) and embedding each separately would improve search precision for our longer notes. A search for a specific concept mentioned in one paragraph of a long note could match the fragment even if the whole-note embedding doesn't rank highly. *Needs a use case first* -- requires vector search infrastructure we don't currently use for primary retrieval.

## Curiosity Pass

**What property does the five-type taxonomy claim to produce?** Differential decay and retrieval boosting -- episodic events fade fast, knowledge persists. The code confirms this: `DECAY_RATES` and `KNOWLEDGE_TYPE_BOOST` are real constants applied in `scoreMemory()` and `decayMemories()`. The taxonomy genuinely shapes behavior, not just naming. However, the type is assigned by the caller at `store()` time, not inferred from content. An agent storing a factual observation as `episodic` instead of `semantic` will see it decay at 0.93/day instead of 0.98/day -- the classification accuracy depends entirely on the storing agent's judgment.

**Does the dream cycle transform data or just relocate it?** Consolidation genuinely transforms: LLM generates focal-point questions from episodic summaries, retrieves relevant memories across types, and produces new semantic insights with evidence links. The output is structurally different from the input -- a one-sentence insight linked to source memories, stored as a new semantic memory. Compaction also transforms: groups of old episodic memories become a single semantic summary. Contradiction resolution transforms: it resolves conflicting memories and adjusts decay. The dream cycle is one of the more genuinely transformative automated processes among reviewed systems.

**What's the simpler alternative to entity extraction?** The entity extraction is rule-based regex (Twitter handles, Solana addresses, capitalized multi-word names). It could be replaced by storing user-provided tags as the entity surface and skipping the auto-extraction entirely. The auto-extraction's accuracy is limited -- it catches `@handles` and `$TICKERS` well but will miss most conceptual entities. The entity graph's main value comes from co-occurrence relations (entities mentioned together), which requires extraction. For a non-social-bot use case, manual entity tagging would be more accurate.

**What could Hebbian co-retrieval reinforcement actually achieve, even if it works perfectly?** It strengthens associations between memories that are frequently useful together. The ceiling is path-dependent attention: early co-retrievals lock in link strengths that bias future retrievals. The anti-confabulation gate (reduced reinforcement for internally generated memories) partially addresses the risk of self-reinforcing dream outputs, but doesn't eliminate it. A memory that appears in many dream cycle consolidations will still accumulate access-count-driven importance boosts. The system trades exploration (finding new connections) for exploitation (strengthening known ones).

**The social-bot heritage shapes the entire architecture.** The concept ontology (`market_event`, `holder_behavior`, `whale_activity`, `price_action`, `engagement_pattern`) is Solana crypto-trading specific. The entity types include `token` and `wallet`. The outcome tracker measures tweet engagement. The emergence phase posts to X. The on-chain commit writes memory hashes to Solana. Adapting cludebot for a different domain requires stripping this social-bot layer and rebuilding the concept ontology -- the memory primitives underneath are domain-general, but the concrete implementation is deeply coupled to the social-bot use case.

**The local mode is surprisingly capable for its simplicity.** The local store (`~/.clude/memories.json`) implements keyword scoring, importance/decay filtering, Hebbian access reinforcement, and even clinamen -- all without a database, embeddings, or LLM calls. It uses atomic file writes (write to `.tmp`, rename) for crash safety. This is a credible minimal memory system in under 400 lines. The trade-off: no vector search, no entity graph, no dream cycles, no compaction.

## What to Watch

- **Does the action-learning loop produce durable procedural improvements?** The strategy refiner generates rules from action-outcome patterns, but these rules are just text memories subject to decay. Do they actually change agent behavior, or do they fade before being recalled in the right context?
- **Will the concept ontology generalize beyond crypto social bots?** The current ontology is narrow. If cludebot gets adoption for non-crypto agents, the ontology will need to become pluggable. How this evolves will show whether the architecture is genuinely domain-general.
- **Fragment-level retrieval precision at scale.** With thousands of memories, does fragment decomposition actually improve retrieval accuracy vs. whole-memory embedding? The overhead is significant (3-5x more embeddings per memory).
- **Confabulation spirals in self-reinforcing dream outputs.** Dream-generated semantic memories are recalled during future dream cycles. The internal-source dampening partially gates this, but the feedback loop is structurally present. Does memory quality degrade over many dream cycles?

---

Extends [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) -- cludebot's action → outcome → lesson pipeline is the most complete trajectory-to-rule artifact-learning loop among reviewed systems, with social-engagement outcome measurement as a concrete oracle.

Contrasts [inspectable substrate not supervision defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) -- cludebot's Supabase storage is opaque without API/SQL mediation; the local JSON mode is the closest it gets to inspectable substrate, and even that requires parsing structured JSON rather than reading prose.

Extends [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) -- the strategy refiner learns procedural rules from action-outcome patterns, with tweet engagement as the oracle; the oracle's quality (engagement != correctness) bounds the quality of learned strategies.

Extends [CLAW learning loops must improve action capacity not just retrieval](../claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- cludebot's action learning pipeline goes beyond retrieval into genuine action-capacity improvement: it generates procedural rules ("When X, do Y") from observed outcomes, not just retrieves better memories.

Exemplifies [constraining and distillation both trade generality for reliability speed and cost](../constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) -- dream cycle consolidation distils (episodic → semantic insights), compaction distils (old episodic groups → summaries), and the concept ontology constrains (freeform text → structured labels); both arms are present.

Contrasts [ephemeral computation prevents accumulation](../ephemeral-computation-prevents-accumulation.md) -- cludebot is maximally anti-ephemeral: every interaction stores a memory, dreams generate more memories, and compaction creates summary memories; nothing is discarded, only decayed or compacted.

`#related-systems` `#memory-architecture` `#learning-theory`
