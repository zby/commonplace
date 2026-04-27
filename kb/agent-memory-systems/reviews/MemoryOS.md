---
description: "MemoryOS review: hierarchical conversational memory that promotes user/assistant dialogue traces into short-term buffers, mid-term sessions, long-term profiles, and retrievable knowledge"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# MemoryOS

MemoryOS is BAI-LAB's Python implementation of a "memory operating system" for personalized conversational agents. The code is not an operating-system substrate in the low-level sense; it is a layered conversational memory library plus MCP server that stores user/assistant turns, condenses them into topical sessions, extracts user profile and knowledge entries, retrieves relevant memories for response generation, and optionally backs the vector surfaces with ChromaDB.

**Repository:** https://github.com/BAI-LAB/MemoryOS

**Reviewed commit:** 8688d5128901a88a70a3ba961de8705a6cdab4c0

**Commit URL:** https://github.com/BAI-LAB/MemoryOS/commit/8688d5128901a88a70a3ba961de8705a6cdab4c0

## Core Ideas

**Memory is a three-layer personal conversation store.** The PyPI implementation creates per-user JSON files for short-term turns, mid-term sessions, and long-term user memory, plus an assistant-specific long-term JSON file. `Memoryos.__init__` wires `ShortTermMemory`, `MidTermMemory`, two `LongTermMemory` instances, an `Updater`, and a `Retriever`; `add_memory(...)` always writes a user input / agent response pair into the short-term buffer first ([memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/memoryos.py), [short_term.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/short_term.py)).

**Short-term overflow triggers LLM condensation into mid-term sessions.** When the short-term deque reaches capacity, `Updater.process_short_term_to_mid_term()` pops old QA pairs, asks an LLM whether adjacent pages are continuous, asks for a short meta-summary, then asks for up to two topic summaries with keywords. Each summary is used to create or merge a mid-term session, with page embeddings attached to the original turns ([updater.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/updater.py), [utils.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/utils.py), [prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/prompts.py)).

**Mid-term memory is a heat-ranked session heap.** A session stores a summary, keywords, normalized summary embedding, detail pages, visit count, interaction length, recency, and `H_segment`. Search embeds the query, runs FAISS inner-product search over session summaries, filters pages by dot product, increments visit/access counters, recomputes heat, and returns page-level matches. Capacity pressure evicts the least frequently accessed session rather than the coldest session in the heat heap ([mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/mid_term.py)).

**Long-term memory separates profile from knowledge.** A hot mid-term segment triggers parallel LLM calls: one rewrites the complete user profile from unanalyzed pages plus the previous profile; the other extracts "User Private Data" and "Assistant Knowledge". User knowledge and assistant knowledge are stored as individual embedded deque entries with timestamps, while the user profile is stored as a replacement string in `user_profiles` ([memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/memoryos.py), [long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/long_term.py), [prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/prompts.py)).

**Retrieval is parallel fan-out across memory layers.** `Retriever.retrieve_context(...)` concurrently searches mid-term pages, user long-term knowledge, and assistant long-term knowledge. `get_response(...)` then builds a prompt from short-term history, retrieved historical pages, the raw user profile, retrieved user knowledge, retrieved assistant knowledge, current conversation metadata, relationship, and the query before calling the configured OpenAI-compatible model. The response is written back as a new memory turn, closing the online loop ([retriever.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/retriever.py), [memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-pypi/memoryos.py)).

**The integration surface is library plus MCP, with a ChromaDB variant.** The MCP server initializes one global `Memoryos` instance from JSON config and exposes `add_memory`, `retrieve_memory`, and `get_user_profile` tools over FastMCP. The ChromaDB implementation replaces JSON/FAISS storage with persistent Chroma collections for mid-term summaries/pages and long-term knowledge, while keeping profile and session metadata in a sidecar JSON file ([server_new.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-mcp/server_new.py), [storage_provider.py](https://github.com/BAI-LAB/MemoryOS/blob/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-chromadb/storage_provider.py), [memoryos-chromadb](https://github.com/BAI-LAB/MemoryOS/tree/8688d5128901a88a70a3ba961de8705a6cdab4c0/memoryos-chromadb)).

## Comparison with Our System

| Dimension | MemoryOS | Commonplace |
|---|---|---|
| Primary substrate | JSON files, FAISS over in-file embeddings, optional ChromaDB collections | Markdown files in git |
| Memory atom | Conversation page, topical session, profile string, knowledge entry | Typed note, source, instruction, ADR, review, index |
| Creation trigger | Online dialogue turns and buffer thresholds | Deliberate authoring, ingest, review, or promotion |
| Distillation target | Personal profile and retrievable facts | Inspectable knowledge artifacts and stronger operating procedures |
| Retrieval | Embedding search over sessions/pages/knowledge, plus recent context | `rg`, indexes, descriptions, authored links, reports, explicit reading |
| Governance | Capacity thresholds, heat, LFU eviction, LLM extraction prompts | Type specs, validation, semantic review, link contracts, git history |
| Agent integration | Python API, response generator, FastMCP tools | Repository-native skills, CLI commands, markdown artifacts |

MemoryOS is stronger where the problem is a single assistant remembering a single user's conversation history. It has an online write path, a response generation path, and a simple MCP surface that can be called by agent clients. Commonplace does not try to keep a personal chat memory hot in a response loop.

Commonplace is stronger where memory must be inspectable, source-grounded, collaboratively maintained, and reusable across agents. MemoryOS stores distilled strings and embeddings, but not source citations, review state, contradiction handling, provenance links from a long-term fact back to the exact dialogue pages, or a promotion path from "the user said X" into a governed artifact with status and relationships.

The core divergence is that MemoryOS treats memory as personalization state for generation. Commonplace treats memory as context-engineering infrastructure: artifacts that make future work discoverable, trusted, composable, activatable, and maintainable. MemoryOS can remind an assistant what a user likes; it does not provide a general method for turning repeated agent work into notes, instructions, validations, or compiled operating surfaces.

## Borrowable Ideas

**Separate recency buffer, session memory, and durable profile.** Ready as a conceptual pattern. Commonplace already separates workshop state, notes, references, and instructions; MemoryOS is a useful reminder that retrieval surfaces should differ by timescale and update frequency rather than treating all memory as one flat store.

**Use heat to decide when to distill, not just what to retrieve.** Worth borrowing for future review or promotion queues. MemoryOS triggers long-term extraction when a mid-term segment is hot enough, combining interaction length, visits, and recency. A commonplace analogue could prioritize which workshop artifacts or logs deserve distillation.

**Keep assistant knowledge distinct from user knowledge.** Ready as a vocabulary distinction, though not as a new store today. MemoryOS explicitly separates facts about the user from facts/capabilities about the assistant, which maps to the difference between domain knowledge and agent self-description.

**Expose memory operations through MCP without hiding the substrate.** Useful if commonplace later offers read/write memory services to non-repo clients. The MemoryOS MCP tools are simple and operationally direct: add a turn, retrieve memories, read profile. The borrowable part is the narrow command surface, not the global singleton implementation.

**Make response generation write back to memory.** Needs a constrained use case. The loop is powerful for personalization, but commonplace should be careful: automatic write-back from every answer would create review debt unless paired with provenance, triage, and promotion rules.

## Trace-derived learning placement

**Trace source.** MemoryOS qualifies as trace-derived learning. The raw trace is a stream of user/assistant dialogue pairs, including timestamps and optional current-turn metadata. In the PyPI path, `get_response(...)` also writes the generated answer back into memory, so deployment conversations become future training material for the same memory store.

**Extraction.** The extraction stack has two stages. First, short-term overflow asks LLM prompts to detect continuity, write page meta-info, and produce topic summaries/keywords for mid-term sessions. Second, hot mid-term sessions trigger LLM profile rewriting and knowledge extraction into user-private facts and assistant-knowledge facts. The oracle is the configured OpenAI-compatible LLM plus threshold logic around short-term capacity and mid-term heat.

**Substrate class.** The raw substrate is structured JSON dialogue pages. The distilled substrate is mostly prose plus vectors: session summaries, page meta-info, profile strings or profile JSON in the Chroma variant, knowledge-entry strings, timestamps, and embeddings. The Chroma path adds database collections, but the learned artifact is still natural-language memory rather than code, tests, or model weights.

**Role.** The role is mixed. Retrieved pages and knowledge entries are knowledge memory: they give the generator facts to condition on. The user profile and assistant knowledge are closer to system-definition memory because they are injected into the prompt as persona and behavioral context, but MemoryOS does not promote them into explicit rules, skills, or validation checks.

**Scope.** Scope is per configured user and assistant. The system has no cross-project or cross-agent governance layer; a memory store is selected by `user_id`, `assistant_id`, and data path.

**Timing.** Learning is online during deployment. Short-term to mid-term promotion happens when the short-term buffer is full; mid-term to long-term promotion happens when the hottest session exceeds the configured heat threshold. `force_mid_term_analysis()` provides a manual testing/maintenance trigger.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), MemoryOS sits in the prose-memory branch: traces are distilled into prompt-visible profile, summaries, and facts. It strengthens the survey's distinction between knowledge memory and system-definition memory because the same dialogue trace produces both retrievable facts and profile/persona context, but it also shows the governance weakness of direct prose promotion without review or source-linked confidence.

## Curiosity Pass

MemoryOS's OS metaphor is mostly organizational. The implemented mechanisms are familiar memory-management analogues -- hierarchy, capacity, heat, eviction, and retrieval -- but there is no scheduler, isolation boundary, permission model, transaction log, or durable artifact lifecycle comparable to an operating system.

The profile update is intentionally lossy. In the PyPI implementation, `gpt_user_profile_analysis(...)` returns a complete updated profile string and `update_user_profile(..., merge=False)` replaces the old profile. That can reduce redundancy, but it means a bad extraction can overwrite prior profile state without an audit trail or confidence model.

The ChromaDB variant looks like an alternate implementation rather than a thin storage backend. It changes profile shape toward JSON, adds keyword extraction calls in more places, stores page metadata through Chroma plus JSON backups, and exposes explicit save-on-exit behavior. That improves scalability, but also makes behavioral parity with the PyPI path something to verify rather than assume.

The MCP surface retrieves memory but does not expose curation. A client can add memories and read retrieved context/profile data, but it cannot approve, reject, edit, link, supersede, or trace a long-term fact back through a review workflow. For personal chat memory that may be acceptable; for agent-operated knowledge bases it is the missing control plane.

## What to Watch

- Whether MemoryOS adds provenance from long-term profile/knowledge entries back to the exact source dialogue pages and extraction prompt output.
- Whether the MCP server gains curation tools: list candidates, delete or correct entries, inspect source pages, approve profile updates, and export memory.
- Whether the ChromaDB implementation becomes the canonical path or remains a parallel variant with different semantics.
- Whether evaluation moves beyond LoCoMo answer quality into memory lifecycle properties: stale fact handling, contradiction repair, privacy deletion, and profile drift.
- Whether profile and assistant knowledge become governed system-definition artifacts rather than prompt text updated by an LLM.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: MemoryOS is an online prose-memory system that distills conversation traces into profile and knowledge prompt context.
- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: MemoryOS couples storage with an activation path into response prompts.
- [agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) - contrasts: MemoryOS improves conversational recall but has thin trust and governance surfaces.
- [distillation](../../notes/definitions/distillation.md) - grounds: MemoryOS compresses raw dialogue into summaries, profile text, and concise facts for future generation.
- [files-not-database](../../notes/files-not-database.md) - contrasts: the PyPI path is file-backed, while the ChromaDB path moves retrieval state into a database-backed substrate.
