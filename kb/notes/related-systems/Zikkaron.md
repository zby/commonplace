---
description: "MCP memory server for Claude Code: 26 neuroscience-branded subsystems implemented as heuristic Python without LLM calls — vocabulary over mechanism, but compaction hooks and WRRF retrieval fusion are genuinely borrowable"
type: note
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-03-22
---

# Zikkaron

**A persistent memory engine for Claude Code** built as an MCP server. Stores memories in a single SQLite file with FTS5 and `sqlite-vec` for vector search. Claims to be "built on computational neuroscience" — 26 subsystems, 23 MCP tools, 969 tests, Python 3.11+, v1.3.0.

**Repository:** https://github.com/amanhij/Zikkaron
**Status:** v1.3.0, actively maintained, published on PyPI, MIT license

## Core Ideas

**Neuroscience vocabulary as an organizing metaphor.** Every subsystem is named after a neuroscience concept: "predictive coding" write gate, "hippocampal replay" for compaction recovery, "engram allocation" for memory slots, "astrocyte consolidation" for background processing, "thermodynamic" heat decay for memory relevance. The README cites 14 papers (Nader 2000, Ramsauer 2021, McClelland 1995, etc.). This labeling creates a coherent narrative — but the question is whether the implementations actually model the cited phenomena or just borrow the names.

**Predictive coding write gate filters redundant writes.** Incoming memories are embedded and compared against existing memories by cosine similarity. Surprise = 1 - max_similarity. Memories below the surprisal threshold (default 0.4) are blocked. Bypass patterns exist for errors, decisions, and critical tags. A task-continuity tracker lowers the threshold when the user is actively working in the same directory. This is a useful mechanism — a novelty filter that prevents the database from accumulating redundant entries. The neuroscience framing (predictive coding, free energy minimization) adds no predictive power beyond "don't store duplicates."

**Heat-based temporal decay with heuristic importance scoring.** Every memory carries a `heat` float that decays over consolidation cycles. Importance is scored via keyword regex: error/exception terms (+0.2), decision keywords (+0.3), architecture keywords (+0.2), tag count (+0.1). No LLM is involved — this is pure pattern matching. The heuristic is honest about what it is: a content classifier based on surface patterns. The "thermodynamic" label adds no mechanism; a simpler "relevance score" description would be equivalent.

**Multi-signal retrieval fusion (WRRF).** The core retrieval pipeline fuses up to nine signals via Weighted Reciprocal Rank Fusion: vector similarity (sqlite-vec KNN), FTS5 BM25, Personalized PageRank over a knowledge graph, spreading activation, fractal hierarchy, Hopfield energy scoring, HDC encoding, successor representation navigation, and temporal matching. Each signal produces a ranked list; scores are fused as `WRRF_score(d) = sum(w_i / (k + rank_i(d)))`. An optional cross-encoder reranker refines the final ordering. Query analysis routes which signals to activate based on query type (e.g., temporal queries enable the temporal signal, open-domain queries expand via hardcoded topic expansions). This is genuinely sophisticated retrieval engineering — the fusion architecture itself is real and well-implemented.

**Hippocampal Replay for compaction resilience.** Claude Code shell hooks (`PreCompact`, `PostCompact`, `SessionStart`, `PostToolUse`) handle context lifecycle. Before compaction, a drain script saves the working state to SQLite. After compaction, a restore script reconstructs context from checkpoints, anchored memories, hot project memories, and recent actions. The `SessionStart` hook injects project context on every new session. The `PostToolUse` hook logs every tool call to an action log table. All hooks read/write SQLite directly — no server communication needed. This is a practical solution to a real problem (context loss during Claude Code compaction).

**Rate-distortion compression with three levels.** Memories age through three compression levels: full fidelity (<7 days), gist (7-30 days, key sentences + code snippets + entities), and tags (>30 days, one-line summary). Protected and semantic-store memories skip compression. Original content is archived before compression. The age thresholds are fixed defaults — the "rate-distortion optimal" framing cites Toth et al. 2020 but the implementation is a time-based rule with keyword extraction, not an information-theoretic optimization.

**Complementary Learning Systems: episodic vs. semantic stores.** Memories are classified as episodic (specific events with file paths, line numbers) or semantic (general patterns with decision/architecture keywords) via regex-based heuristics. Semantic memories resist compression and persist longer. Go-CLS consolidation only promotes patterns seen consistently across multiple sessions. This is a sensible two-tier architecture — frequent patterns graduate to durable storage.

**Engram allocation with competitive slots.** A fixed pool of "engram slots" with excitability scores. New memories go to the most excitable slot, creating automatic temporal linking (memories in the same slot are related). Lateral inhibition reduces neighboring slots' excitability. The mechanism produces temporal co-location without explicit linking — memories stored close in time share a slot. The excitability math (exponential decay with half-life, boost on use) is straightforward priority-queue behavior dressed in neuroscience vocabulary.

**No LLM in the default retrieval loop.** By default, all retrieval, scoring, compression, and consolidation is done with a 22MB sentence-transformer model (`all-MiniLM-L6-v2`), regex heuristics, and SQLite queries. No API calls at query time. (An optional COMET query expansion feature exists but is disabled by default.) This is a genuine architectural commitment — it means the system is fast, cheap, offline-capable, and deterministic. The benchmark claims (86.8% Recall@10 on LoCoMo, 96.7% on LongMemEval) are achieved without LLM-in-the-loop, which makes the engineering more interesting than if it were just throwing GPT-4 at retrieval.

**Benchmark-driven development with hardcoded expansions.** The `enrichment.py` module contains `HARDCODED_EXPANSIONS` mapping hobby terms to related concepts (camping -> outdoor_activity, nature, tent, hiking...) and a `_HYPERNYM_MAP` mapping specific entities to categories (Yellowstone -> national_park, Bach -> classical_music). The `retrieval.py` module has `_OPEN_DOMAIN_TOPIC_EXPANSIONS` and fact-pattern regexes tuned to LoCoMo question patterns. This is honest benchmark engineering — the system has been iteratively tuned to the evaluation datasets, not just generally good at retrieval.

## Comparison with Our System

| Dimension | Zikkaron | Commonplace |
|-----------|----------|-------------|
| Storage | SQLite (single file, WAL, FTS5, sqlite-vec) | Markdown files in git |
| Retrieval | 9-signal WRRF fusion, sentence-transformer embeddings | Agent-driven navigation via descriptions and links |
| Write control | Predictive coding surprisal gate | Human judgment (text -> seedling -> note) |
| Memory lifecycle | Heat decay, compression, archival — all automatic | Manual promotion with status field |
| Context injection | Frontloaded on session start + compaction hooks | Progressive disclosure via CLAUDE.md router |
| LLM involvement | None at runtime (embeddings only) | None at storage, LLM for authoring and retrieval |
| Learning theory | None — mechanisms are designed, not discovered | Explicit verifiability gradient, constraining/codification framework |
| Formalization | Code (26 Python modules) | Conventions (YAML frontmatter, templates, skills) |

**The storage model divergence is fundamental.** Zikkaron stores opaque memory records in SQLite. You interact with memories only through MCP tools. There is no human-readable file you can open, browse, edit, or link from another document. Our markdown-in-git model makes every note a first-class navigable document — agents and humans read the same artifacts. The trade-off: Zikkaron gets sophisticated automated retrieval (multi-signal fusion, heat decay, vector search); we get human-legible, version-controlled, tool-agnostic knowledge. This is the same [files-not-database](../files-not-database.md) divergence seen in Cognee, Hindsight, and other database-backed systems.

**Zikkaron automates what we keep deliberate.** Its write gate, heat decay, compression pipeline, and consolidation daemon automate the entire memory lifecycle. Memories are stored, aged, compressed, and promoted without human involvement. We deliberately keep promotion manual — [automating KB learning is an open problem](../automating-kb-learning-is-an-open-problem.md) — because we don't yet trust automated judgment for knowledge curation. Zikkaron's approach generates evidence about whether full automation works, but the benchmark numbers measure retrieval accuracy, not knowledge quality. A system can retrieve the right memories perfectly and still accumulate garbage if the write gate's novelty filter doesn't distinguish useful-novel from noisy-novel.

**Both solve the compaction problem, differently.** Zikkaron's hippocampal replay hooks drain and restore context around Claude Code compaction events — an automated safety net. We don't have an equivalent mechanism. Our model assumes the agent can re-navigate to needed context via CLAUDE.md routing, which works only if the agent is competent at navigation. Zikkaron's approach is more defensive and more reliable for weaker agents or unfamiliar codebases.

## Borrowable Ideas

**1. Compaction hooks as a standard pattern (ready now).** The `PreCompact` drain + `PostCompact` restore pattern is immediately useful for any Claude Code project. Even without the full Zikkaron stack, the idea of checkpointing working state before compaction and restoring it after could be implemented as lightweight shell hooks that write/read a markdown checkpoint file. We could implement this as a workshop layer artifact.

**2. Surprisal-based write filtering (needs use case).** The predictive coding gate's core idea — only store things that are novel relative to what you already know — is sound for high-volume automated capture. Not relevant for our current human-curated workflow, but would matter if we ever build automated ingestion. The task-continuity lowering (same directory + recent timeframe = lower threshold) is a nice refinement.

**3. Multi-signal retrieval fusion architecture (reference only).** The WRRF fusion pattern is well-engineered and worth studying if we ever move beyond rg-based retrieval. The key insight is that no single retrieval signal dominates — vector search, keyword search, graph traversal, and temporal matching each catch cases the others miss. But this is only relevant if we build retrieval infrastructure, which is not on our roadmap while the KB is small enough for agent-driven navigation.

**4. Tool call action logging (ready now).** The `PostToolUse` hook that logs every tool call to an action table is a simple, low-cost way to build a session activity record. Could inform later analysis of agent behavior patterns. The implementation is clean: stdlib-only Python, direct SQLite write, <100ms, background execution.

## Curiosity Pass

**What property does "predictive coding" claim to produce?** The claim is that the write gate implements predictive coding — the brain's mechanism for encoding only prediction errors. The implementation computes cosine similarity against existing memories and blocks writes below a threshold. This is a novelty filter. The neuroscience reference (Friston's active inference, Barron et al. on hippocampal prediction errors) describes hierarchical generative models that predict sensory input and propagate errors upward. Zikkaron's implementation is a flat nearest-neighbor similarity check — there is no hierarchical model, no prediction generation, no error propagation. The property produced (redundancy filtering) is real and useful. The mechanism name ("predictive coding") describes a far more complex process than what's implemented.

**Does the thermodynamic model transform data or relocate it?** Heat values are floats that decay multiplicatively each consolidation cycle and get boosted by access. Importance is scored by keyword regex. This is a weighted recency-frequency score with content heuristics — the standard information retrieval approach. The "thermodynamic" framing (temperature, heat, cooling) is a metaphor. No thermodynamic equations are computed; no partition functions, no entropy calculations, no free energy minimization. The data (a relevance score) is neither transformed nor relocated — it's computed from access patterns and content signals via standard formulas.

**What could Hopfield energy scoring achieve, even if it works perfectly?** The Hopfield module implements modern continuous Hopfield networks (Ramsauer et al. 2021): softmax(beta * X^T * query) where X is the stored pattern matrix. This is mathematically equivalent to single-head transformer attention. The implementation is correct — softmax, sparsemax, energy computation, pattern completion. But in the context of retrieval, it's one more similarity signal alongside vector search, FTS5, PPR, and spreading activation. The Hopfield energy adds a different similarity geometry (softmax attention vs. cosine distance), which could help when the embedding space doesn't separate patterns well. Whether this matters in practice depends on how often the Hopfield signal surfaces results that other signals miss — the benchmarks don't ablate this.

**What does the "engram allocation" mechanism achieve beyond a priority queue?** Engram slots have excitability that decays and boosts. New memories go to the most excitable slot. Memories in the same slot are "temporally linked." The effect: memories stored close in time co-locate. This is temporal bucketing — a simple partitioning scheme. The CREB-excitability framing (Josselyn & Frankland, Rashid et al.) describes molecular mechanisms of memory competition in neurons. The implementation is `argmax(excitability)` followed by `excitability *= boost`. The claimed property (temporal linking) is real but could be achieved with a timestamp-based grouping. The competitive allocation adds one thing a simple timestamp wouldn't: if you interleave two tasks, memories from the more active task (higher excitability from recent access) cluster together even if they're interleaved temporally. Whether this matters in practice is unclear.

**The benchmark hardcoding reveals the real engineering.** The most illuminating files aren't the neuroscience modules but `enrichment.py` and the retrieval query expansion code. Hardcoded mappings (camping -> outdoor_activity, Yellowstone -> national_park, "personality traits" -> "thoughtful, authentic, driven, caring") and pattern-specific regex (fact extraction patterns tuned to LoCoMo dialogue formats) show where the benchmark performance actually comes from: domain-specific feature engineering, not general neuroscience-inspired mechanisms. This isn't criticism — it's how real systems work. But it means the benchmark numbers reflect the union of general retrieval + dataset-specific tuning, not the neuroscience mechanisms alone.

## What to Watch

- **Usage evidence for automated lifecycle.** Does the fully automated memory lifecycle (gate + decay + compress + consolidate) produce good long-term knowledge, or does it accumulate noise that passing the write gate doesn't prevent? No evidence yet beyond retrieval benchmarks.
- **Benchmark overfitting vs. generalization.** The hardcoded expansions and pattern-specific tuning raise the question: how does Zikkaron perform on coding-session memories (its actual use case) vs. the conversational benchmarks it's been tuned against?
- **Hook ecosystem maturation.** The `PreCompact`/`PostCompact`/`SessionStart`/`PostToolUse` hook pattern is the most practically useful contribution. If Claude Code's hook system evolves, Zikkaron's approach to context lifecycle management could become a standard pattern.
- **Mechanism vs. vocabulary over time.** Will future versions deepen the neuroscience implementations (actual hierarchical predictive models, real thermodynamic optimization) or continue using them as organizing vocabulary for pragmatic heuristics?

---

Relevant Notes:

- [Hindsight](./hindsight.md) — sibling: both are database-backed memory systems with multi-signal retrieval fusion and biomimetic vocabulary; Hindsight uses LLM-driven extraction where Zikkaron uses heuristic-only extraction, making them complementary data points on the LLM-at-write-time trade-off
- [ClawVault](./clawvault.md) — sibling: both solve session lifecycle (handoffs, checkpoints, context restoration) and observation capture; ClawVault uses markdown files where Zikkaron uses SQLite, and ClawVault's observation types are more structured than Zikkaron's free-text memories
- [files-not-database](../files-not-database.md) — contrasts: Zikkaron's SQLite-only storage with no human-readable files is the opposite of our files-first commitment; the trade-off buys automated retrieval infrastructure at the cost of browsability and tool-agnosticism
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — contrasts: Zikkaron fully automates the memory lifecycle (write gate, decay, compression, consolidation) where we keep curation manual; their system generates evidence about whether automation works, but measures retrieval accuracy rather than knowledge quality
- [a-functioning-kb-needs-a-workshop-layer](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — extends: Zikkaron's compaction hooks (drain/restore/checkpoint) are concrete workshop-layer artifacts for session continuity that we lack
- [oracle-strength-spectrum](../oracle-strength-spectrum.md) — contrasts: Zikkaron's heuristic importance scoring (keyword regex) and surprisal gate (cosine similarity threshold) are weak oracles for knowledge quality — deterministic but low-precision; the neuroscience framing doesn't change the oracle strength
