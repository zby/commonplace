---
description: "MemoryOS review: hierarchical conversational memory that stores dialogue traces, condenses sessions, extracts profile and knowledge records, and injects retrieved context"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# MemoryOS

MemoryOS, from BAI-LAB, is a Python memory layer for personalized conversational agents. The inspected repository implements a short-term buffer for recent user/assistant turns, a mid-term session store that condenses and ranks older turns, long-term user and assistant knowledge stores, a retrieval/generation path, an MCP server, and a ChromaDB-backed variant. Its "memory OS" metaphor is implemented as tiered conversational storage and update policy, not as a general operating-system substrate.

**Repository:** https://github.com/BAI-LAB/MemoryOS

**Reviewed commit:** [1d717060350931af33d1d0dc3d4e50a72c125a48](https://github.com/BAI-LAB/MemoryOS/commit/1d717060350931af33d1d0dc3d4e50a72c125a48)

**Last checked:** 2026-05-16

## Core Ideas

**The core unit of capture is a user/assistant turn.** The PyPI implementation initializes per-user `short_term.json`, `mid_term.json`, `long_term_user.json`, and per-assistant `long_term_assistant.json` files, then wires short-term, mid-term, long-term, updater, and retriever modules through `Memoryos.__init__` ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). `add_memory(...)` writes each user input and agent response as a timestamped QA pair into a bounded deque persisted as JSON ([memoryos-pypi/short_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/short_term.py)).

**Short-term overflow triggers LLM condensation into mid-term sessions.** When the short-term buffer is full, the updater pops old QA pairs, asks an LLM whether adjacent pages are continuous, generates meta summaries, asks for up to two topic summaries with keywords, embeds the pages, and either merges them into an existing session or creates a new one ([memoryos-pypi/updater.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/updater.py), [memoryos-pypi/utils.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/utils.py), [memoryos-pypi/prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). Mid-term sessions retain both prose summaries and the original dialogue pages, so the distilled view does not fully replace the raw trace.

**Mid-term memory is a heat-ranked, embedding-searchable session store.** A session records summary text, summary keywords, summary embedding, dialogue pages with page embeddings, recency, visit count, interaction length, access count, and `H_segment`. Retrieval builds a FAISS inner-product index over session summaries, filters matched pages by embedding similarity, increments visit/access counters, recomputes heat, and evicts least-frequently-used sessions when capacity is exceeded ([memoryos-pypi/mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py)).

**Hot sessions are distilled into long-term profile and knowledge records.** When the hottest mid-term session crosses the heat threshold, MemoryOS runs profile analysis and knowledge extraction in parallel over unanalyzed pages. The profile path rewrites the complete user profile; the knowledge path extracts user private knowledge and assistant knowledge, then stores entries with timestamps and embeddings ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-pypi/long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/long_term.py), [memoryos-pypi/prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). The derivation chain is visible in code, but individual long-term records do not carry source page IDs, confidence, contradiction state, or invalidation rules.

**Retrieval fans out across memory layers before generation.** `Retriever.retrieve_context(...)` concurrently searches mid-term pages, user long-term knowledge, and assistant long-term knowledge; `get_response(...)` then formats short-term history, historical pages, user profile, user knowledge, assistant knowledge, metadata, relationship, and current query into prompt messages before calling an OpenAI-compatible model and writing the answer back as a new turn ([memoryos-pypi/retriever.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/retriever.py), [memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). Memory therefore has a closed online loop: generate, store, condense, retrieve, and generate again.

**The integration surfaces are library, MCP, playground, and ChromaDB variants.** The MCP server initializes one configured `Memoryos` instance and exposes `add_memory`, `retrieve_memory`, and `get_user_profile` tools for agent clients ([memoryos-mcp/server_new.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-mcp/server_new.py)). The ChromaDB variant replaces JSON-plus-FAISS vector storage with persistent Chroma collections for mid-term summaries/pages and long-term knowledge while keeping profile, short-term, heap, and session metadata in a JSON sidecar ([memoryos-chromadb/storage_provider.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/storage_provider.py), [memoryos-chromadb/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/memoryos.py), [memoryos-chromadb](https://github.com/BAI-LAB/MemoryOS/tree/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb)).

## Comparison with Our System

| Dimension | MemoryOS | Commonplace |
|---|---|---|
| Primary purpose | Personalized conversational memory for a user/assistant pair | Agent-operated methodology KB for durable knowledge, instructions, reviews, and validation |
| Storage substrate | JSON files, deques, FAISS built at query time, ChromaDB collections, MCP config | Git-tracked Markdown, schemas, source snapshots, generated indexes, review outputs, scripts |
| Representational form | Raw dialogue prose, prose summaries/profile/facts, symbolic JSON fields, embeddings/vector indexes | Typed prose and frontmatter, symbolic links/schemas/commands, generated indexes, validation code |
| Lineage | Raw pages remain in mid-term sessions, but extracted profile/knowledge records lack mandatory source IDs or review state | Source-pinned artifacts, authored citations, replacement archives, statuses, validation, and review gates |
| Activation | Online retrieval and prompt injection before response generation or via MCP retrieval tools | `rg`, indexes, descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Retrieved memories advise generation; profile/assistant knowledge and context blocks condition the next prompt | Advice, instruction, routing, validation, review, and governance authority are separated by artifact type |

MemoryOS and commonplace agree that retained state matters only when it can change later behavior. MemoryOS is stronger in online activation for a single assistant: once installed, new turns flow through capture, condensation, retrieval, and prompt construction. Commonplace is stronger in inspectable accumulation: retained claims, instructions, and reviews are named artifacts with type contracts, source links, status, validation, and replacement history.

The key difference is governance. MemoryOS promotes dialogue traces into profile text and knowledge strings automatically when heat thresholds fire. Those records are useful knowledge artifacts when retrieved as context or evidence. When inserted into the response prompt, especially assistant knowledge and relationship/persona context, they acquire temporary system-definition-artifact authority because they shape the next model call through an instruction-bearing channel ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-pypi/prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). Commonplace reserves stronger authority for curated instructions, skills, schemas, commands, and reviewed notes.

The strongest borrowable design axis is tiering by timescale and update cost. MemoryOS distinguishes fresh turns, condensed sessions, durable profile, durable user knowledge, durable assistant knowledge, and vector retrieval state. Commonplace uses a different substrate, but the same artifact-analysis vocabulary applies: raw dialogue traces, summaries, knowledge entries, embeddings, retrieved context, and injected prompt blocks should not all be called "memory" without naming storage substrate, representational form, lineage, and behavioral authority.

## Borrowable Ideas

**Use heat as a distillation trigger.** Worth borrowing for workshops or review queues. MemoryOS does not distill every turn into durable profile state; it waits until session heat combines visits, interaction length, and recency. A commonplace analogue could prioritize which logs, work notes, or repeated warnings deserve promotion review.

**Keep profile-like knowledge separate from conversation evidence.** Ready as vocabulary. MemoryOS's user profile, user knowledge, assistant knowledge, mid-term pages, and raw short-term history have different trust and authority levels. Commonplace should keep the same separation when building trace-derived tools.

**Expose narrow memory operations through MCP.** Useful when a repo-backed KB needs to serve non-repo clients. MemoryOS's MCP surface is deliberately small: add a memory, retrieve memory, get profile. A commonplace surface would need stronger typing and authorization, but the command shape is practical.

**Do not borrow automatic promotion as library policy.** MemoryOS's LLM extraction is appropriate for personalization. It is too weak for methodology claims, operational instructions, or validation rules unless paired with source-linked review, contradiction handling, and retirement.

## Trace-derived learning placement

**Trace source.** MemoryOS qualifies as trace-derived learning. The source trace is a stream of user/assistant dialogue pairs with timestamps, plus optional current-turn metadata in generation and MCP entry points. In the generation path, MemoryOS stores its own generated response back into memory, so deployment conversations become future memory evidence ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-mcp/server_new.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-mcp/server_new.py)).

**Extraction.** Extraction has two stages. Short-term overflow converts raw turns into mid-term pages, continuity links, meta summaries, topic summaries, keywords, and embeddings. Hot mid-term sessions then trigger profile rewriting and knowledge extraction into user private knowledge and assistant knowledge ([memoryos-pypi/updater.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/updater.py), [memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). The oracle is mostly the configured LLM plus prompt templates and numeric thresholds, not human review.

**Storage substrate.** Raw short-term turns persist in JSON or Chroma metadata. Mid-term sessions persist as JSON session records in the PyPI path, with embeddings stored in JSON and FAISS indexes rebuilt for search. The ChromaDB path stores session summaries, page vectors, user knowledge, and assistant knowledge in persistent collections while retaining operational metadata in a JSON file ([memoryos-pypi/mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py), [memoryos-chromadb/storage_provider.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/storage_provider.py)). Long-term user profiles are JSON/metadata records; long-term knowledge records are embedded prose entries.

**Representational form.** Raw dialogue and generated summaries are prose. Session IDs, timestamps, links, heat fields, thresholds, heap state, JSON structures, and MCP tool schemas are symbolic. Embeddings and vector collections are distributed-parametric retrieval state. The behavior-shaping operative part is mixed: prose memories and profiles are selected by symbolic thresholds and vector similarity, then formatted into prompt text.

**Lineage.** Lineage is strongest at the mid-term layer because sessions keep original pages beside summaries and page IDs. It weakens at long-term extraction: profile and knowledge entries preserve timestamps but not mandatory links back to source pages, extraction prompt versions, confidence, contradiction handling, or regeneration policy. The ChromaDB variant stores text and timestamps for knowledge entries, but it does not add richer provenance ([memoryos-pypi/long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/long_term.py), [memoryos-chromadb/long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/long_term.py)).

**Behavioral authority.** Raw turns, mid-term pages, summaries, and knowledge entries are knowledge artifacts when used as evidence, context, or personalization hints. Embeddings and similarity thresholds have ranking authority because they choose what becomes active. Prompt-formatted profile, assistant knowledge, historical memory, and current metadata become temporary system-definition artifacts for the next generation call because they are injected through the system/user prompt construction path.

**Scope.** The default scope is one configured user and assistant, with separate filesystem paths or Chroma collections per identity. MCP exposes that configured memory instance to external clients; it is not a cross-project knowledge governance system.

**Timing.** Capture and response generation are online. Short-term-to-mid-term migration occurs when the short-term capacity is reached. Long-term extraction occurs when a mid-term session becomes hot enough or when forced manually. Retrieval occurs immediately before generation or MCP retrieval response.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), MemoryOS is an online trace-to-profile and trace-to-fact memory system with automatic prompt-time activation. It strengthens the survey split between raw trace retention and distilled retained artifacts: the same conversation trace can remain as a page, become a session summary, update a user profile, produce user/assistant knowledge records, and influence prompt construction through retrieved context.

## Takeaways

**MemoryOS is a real trace-derived conversational memory system.** It captures dialogue turns, condenses them into sessions, extracts profile and knowledge records, retrieves relevant history, and feeds selected records into later generation.

**Its central strength is activation.** MemoryOS is built around the path from remembered material to the next response. The MCP variant also makes memory callable by agent clients without requiring them to understand the internal storage layout.

**The retained artifacts need separate labels.** A MemoryOS "memory" can be a raw QA turn, a mid-term page, a session summary, a user profile, a user knowledge string, an assistant knowledge string, an embedding, a Chroma record, a retrieval score, or injected prompt context. These differ in substrate, form, lineage, and authority.

**Governance is thin after extraction.** The system keeps enough raw material to make mid-term sessions understandable, but long-term profile and knowledge records are not source-cited, reviewed, contradicted, retired, or promoted through typed authority levels.

**The OS metaphor should be treated as an architecture metaphor.** The code implements hierarchy, capacity, heat, eviction, update, retrieval, and generation. It does not implement a permission model, transaction log, validated promotion lifecycle, or general retained-artifact governance layer.

## Curiosity Pass

The most interesting mechanism is not ChromaDB or FAISS; it is the heat threshold that decides when a mid-term segment becomes important enough for long-term extraction. That is closer to an attention and promotion policy than a storage feature.

The simpler alternative would be a flat vector store over all turns. MemoryOS gets more useful behavior by separating recent history, session summaries, user profile, user knowledge, and assistant knowledge. The tradeoff is more moving parts and more places where lineage can be lost.

The prompt construction path is more authoritative than it first appears. Retrieved memories are not merely displayed to a user; they are placed into prompts that condition the model's next answer. That authority boundary is not governed by review or confidence metadata.

## Open Questions

- Should extracted long-term profile and knowledge records keep source page IDs, extraction prompt versions, and confidence metadata?
- How should MemoryOS handle contradictions when a user's preferences or facts change?
- Does heat-based extraction improve downstream behavior compared with scheduled or retrieval-time extraction?
- Can assistant knowledge safely condition future responses when it is extracted from prior assistant behavior rather than curated capability documentation?
- Should MCP writes be scoped, audited, or permissioned when multiple clients can add memory?
- How does the ChromaDB path preserve parity with the JSON/FAISS path as schemas and prompts evolve?

## What to Watch

- Whether long-term records gain explicit provenance, confidence, and retirement fields.
- Whether the MCP server adds multi-user authorization or audit surfaces.
- Whether profile and knowledge extraction become evaluable against downstream response quality.
- Whether ChromaDB becomes the primary implementation rather than a parallel variant with sidecar metadata.
- Whether MemoryOS adds a promotion path from conversational facts into stronger rules, tools, or validation artifacts.

## Bottom Line

MemoryOS is best read as online personalization memory for conversational agents: it turns dialogue traces into tiered summaries, profile text, knowledge entries, embeddings, and retrieved prompt context. Commonplace should borrow the tiering discipline and heat-triggered distillation idea, but not the automatic promotion boundary. For durable agent-operated knowledge, extracted memories need source-linked lineage, review, contradiction handling, and explicit authority before they become instructions or governed library artifacts.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: MemoryOS turns dialogue traces into session summaries, profile records, knowledge entries, embeddings, and prompt-visible context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: MemoryOS's raw turns, summaries, profile, knowledge entries, embeddings, and prompt blocks need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: stored dialogue, summaries, and knowledge entries advise later generation.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected profile and memory context gain instruction-channel authority for the next model call.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: MemoryOS couples storage with an online prompt activation path.
