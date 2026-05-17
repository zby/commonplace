---
description: "Memori review: SDK and cloud/BYODB memory layer that captures LLM turns, distills facts/triples/summaries, and injects recalled context"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-05-16"
---

# Memori

Memori, from Memori Labs, is an SDK and service-backed memory layer for LLM applications and agents. The inspected repository ships Python and TypeScript SDKs that wrap existing LLM clients, persist conversation turns, run augmentation that extracts durable memory records, retrieve relevant facts on later calls, and inject recalled context back into provider-specific prompt surfaces.

**Repository:** https://github.com/MemoriLabs/Memori

**Reviewed commit:** [57217f06be44abce87dfdb71b15c5f37fb741707](https://github.com/MemoriLabs/Memori/commit/57217f06be44abce87dfdb71b15c5f37fb741707)

**Last checked:** 2026-05-16

## Core Ideas

**The primary integration surface is LLM-call interception.** In Python, `Memori().llm.register(client)` selects provider-specific wrappers, replaces methods such as OpenAI chat completions and responses calls, and routes every invocation through a Memori `Invoke` wrapper ([memori/llm/_registry.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/_registry.py), [memori/llm/clients/direct.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/clients/direct.py), [memori/llm/invoke/invoke.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/invoke/invoke.py)). In TypeScript, the SDK registers Axon hooks before and after LLM calls to recall, persist, and augment without changing the calling application flow ([memori-ts/src/memori.ts](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori-ts/src/memori.ts)).

**Attribution is the memory boundary.** The SDK requires an entity identifier and optionally a process identifier; session IDs group conversation threads. These fields scope persistence, augmentation, and recall, and the public docs present entity/process/session as the central isolation model ([memori/__init__.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/__init__.py), [docs/memori-byodb/concepts/how-memory-works.mdx](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/docs/memori-byodb/concepts/how-memory-works.mdx)). This is a consumer-facing boundary, not a review or authority boundary: facts for an entity are reused across calls unless the caller changes attribution or deletes entity memory.

**Storage is either cloud service state or a BYODB schema.** Cloud mode posts messages and augmentation requests to Memori API endpoints, while BYODB mode initializes a storage manager over user-provided database connections and can build Memori tables locally ([memori/memory/_manager.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/_manager.py), [memori/memory/augmentation/_handler.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/augmentation/_handler.py), [memori/storage/_manager.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/_manager.py), [memori/storage/_builder.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/_builder.py)). The SQLite migration shows the core retained substrates: entities, processes, sessions, conversations, conversation messages, entity facts with embeddings, process attributes, graph subjects/predicates/objects, graph triples, and fact-to-conversation mentions ([memori/storage/migrations/_sqlite.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/migrations/_sqlite.py)).

**Augmentation distills traces into multiple symbolic memory records.** After a response, Python formats the original request/response into messages, persists the turn, and submits an augmentation input; BYODB augmentation sends selected messages plus prior summary to the augmentation API, parses returned facts, semantic triples, process attributes, and conversation summary, then schedules database writes ([memori/llm/pipelines/post_invoke.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/post_invoke.py), [memori/memory/augmentation/augmentations/memori/_augmentation.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/augmentation/augmentations/memori/_augmentation.py), [memori/memory/_struct.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/_struct.py)). The representational form is mixed: raw conversations are prose-plus-JSON traces, facts and summaries are prose, graph triples and process attributes are symbolic records, and fact embeddings are distributed-parametric retrieval aids.

**Recall combines dense and lexical activation, then injects memory as prompt context.** Local recall embeds the user query, searches entity facts, ranks candidates with cosine similarity plus a BM25-style lexical score, filters by relevance threshold, and formats facts and summaries into a `<memori_context>` block ([memori/memory/recall.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/recall.py), [memori/search/_core.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/search/_core.py), [memori/search/_lexical.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/search/_lexical.py), [memori/llm/pipelines/recall_injection.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/recall_injection.py)). Conversation history can also be prepended, with provider-specific sanitization for tool messages and system messages ([memori/llm/pipelines/conversation_injection.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/conversation_injection.py)).

**Agent traces are present but cloud-centered.** The Python `capture_agent_turn` path writes a user/assistant turn with optional assistant-side `trace`, posts a durable agent conversation turn, and sends a best-effort collector augmentation request; the TypeScript agent augmentation path mirrors this with project/session fields and optional trace/summary ([memori/agent.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/agent.py), [memori-ts/src/engines/augmentation.ts](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori-ts/src/engines/augmentation.ts)). The docs describe tool calls, decisions, workflow steps, and outcomes as trace inputs, but the open-source SDK mostly acts as capture, routing, and storage client for that agent-trace augmentation rather than exposing the cloud extractor implementation ([docs/memori-byodb/concepts/agent-trace-execution.mdx](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/docs/memori-byodb/concepts/agent-trace-execution.mdx)).

## Comparison with Our System

| Dimension | Memori | Commonplace |
|---|---|---|
| Primary purpose | Transparent memory middleware for LLM calls and agent integrations | Agent-operated methodology KB with durable notes, sources, instructions, ADRs, reviews, and validation |
| Storage substrate | Memori Cloud, user databases, conversation tables, fact tables, graph tables, embeddings, summaries | Git-tracked Markdown, schemas, source snapshots, generated indexes, review outputs, scripts |
| Representational form | Raw prose/JSON traces, prose facts and summaries, symbolic triples/attributes, embedding vectors | Mostly prose and structured frontmatter, with symbolic links, schemas, commands, and validation code |
| Lineage | Fact mentions can point back to conversations in BYODB tables, but extracted facts do not carry source citations, review state, or invalidation rules | Source-pinned notes, authored citations, replacement archives, status fields, validation, and review gates |
| Activation | Automatic pre-call retrieval and prompt injection through SDK wrappers or Axon hooks | `rg`, indexes, descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Context advice plus prompt/instruction injection; retrieval has ranking authority | Advice, instruction, routing, validation, review, and governance authority in inspectable artifacts |

Memori and commonplace agree that memory must activate before the next action. Memori is stronger on automatic runtime activation: after registration, LLM calls can be enriched without the caller explicitly querying a KB. Commonplace is stronger on inspectable accumulation: the remembered unit is usually a named artifact with type, status, links, citations, and review history.

The biggest architectural difference is the retained unit. Memori's durable behavior-shaping unit is often an extracted fact, summary, graph triple, process attribute, or raw conversation message. These are useful knowledge artifacts when retrieved as evidence or context. Once Memori injects them into a system prompt, instructions field, Google system instruction, or message prefix, they gain system-definition-artifact authority because they condition the next LLM call through an instruction-bearing channel ([memori/llm/pipelines/recall_injection.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/recall_injection.py), [memori-ts/src/engines/recall.ts](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori-ts/src/engines/recall.ts)). Commonplace assigns that stronger authority to instructions, skills, schemas, and commands only after curation.

Lineage is the main weakness for commonplace's purposes. Memori keeps raw conversation messages and, in local storage, records fact mentions that connect extracted facts to conversations. That is a real lineage hook. But the active fact itself is a compact extracted string with counters and timestamps, not a cited claim that explains source context, extraction confidence, contradiction policy, or retirement conditions ([memori/storage/drivers/sqlite/_driver.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/drivers/sqlite/_driver.py)). For personalization and assistant continuity this may be enough; for methodology knowledge and agent governance it is too thin.

Memori also treats prompt injection as a relevance policy, not as a governed promotion step. The injected context says to use the material only if relevant to the user's query, and the SDK filters by rank score threshold before injection ([memori/llm/pipelines/recall_injection.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/recall_injection.py)). There is no visible code-grounded review loop that promotes facts into stronger rules, demotes stale memories, resolves contradictions, or audits whether injected memories improved downstream behavior.

## Borrowable Ideas

**Use runtime wrappers as activation surfaces.** Worth borrowing for bounded workflows. Commonplace should not make every note auto-inject, but a task-specific wrapper could load a small, typed context bundle before a repeated workflow begins.

**Keep raw traces separate from distilled recall records.** Ready as analysis vocabulary. Memori's split between conversation messages, summaries, facts, graph triples, and prompt-injected context is exactly the split commonplace should preserve when building trace-derived workshop tools.

**Fact-to-conversation mention tables.** Borrow with stronger citations. Memori's `memori_entity_fact_mention` table is a useful lightweight lineage bridge; a commonplace version would need stable source links, extraction rationale, and invalidation state before promoted notes trust the extracted fact.

**Provider-specific injection adapters.** Useful for tools, not library notes. Memori's code handles OpenAI, Anthropic, Google, Bedrock, xAI, Agno, and LangChain surfaces differently. Commonplace can borrow the lesson that activation machinery must respect provider prompt shapes rather than assuming one message format.

**Do not borrow automatic fact promotion as-is.** Memori's augmentation is good for personalization and continuity, but commonplace's durable library should require review before extracted memories become instructions, schemas, or methodology claims.

## Trace-derived learning placement

**Trace source.** Memori consumes LLM interaction traces: user messages, assistant responses, provider metadata, session IDs, entity/process attribution, and in agent paths optional trace objects containing tool or execution context. The normal SDK trigger boundary is one completed wrapped LLM call; the agent path uses an explicit captured turn with project and session scope ([memori/llm/pipelines/post_invoke.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/llm/pipelines/post_invoke.py), [memori/agent.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/agent.py)).

**Extraction.** Extraction happens in Advanced Augmentation. The open-source code packages messages and metadata, calls the augmentation endpoint or Rust queue, parses returned facts, semantic triples, process attributes, and conversation summaries, embeds fact strings, and schedules writes ([memori/memory/augmentation/_handler.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/augmentation/_handler.py), [memori/memory/augmentation/augmentations/memori/_augmentation.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/memory/augmentation/augmentations/memori/_augmentation.py), [memori/_rust_core.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/_rust_core.py)). The extraction oracle is not fully inspectable in this repo: the SDK exposes payload handling and storage writes, while the semantic extractor appears service- or native-core mediated.

**Storage substrate.** Raw traces persist as cloud records or BYODB conversation/session/message rows. Distilled records persist as entity facts, process attributes, conversation summaries, graph triples, and embeddings in cloud or user databases. The TypeScript SDK routes local storage through a native engine and ORM-like storage manager; Python supports several SQL and document database families through migrations and driver registration ([memori/storage/migrations/_sqlite.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/migrations/_sqlite.py), [memori-ts/src/memori.ts](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori-ts/src/memori.ts), [memori/storage/_registry.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/_registry.py)).

**Representational form.** Raw conversations and agent turns are prose/JSON traces. Facts and summaries are prose knowledge artifacts. Semantic triples, process attributes, attribution IDs, and storage schemas are symbolic. Embeddings are distributed-parametric retrieval state. The operative part that changes the next model call is mixed: ranked symbolic/prose facts are formatted into an instruction-bearing prompt block.

**Lineage.** The strongest visible lineage is conversation to extracted memory. BYODB fact writes can record `conversation_id` in `memori_entity_fact_mention`, and fact retrieval can attach summaries from mentioned conversations ([memori/storage/drivers/sqlite/_driver.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/drivers/sqlite/_driver.py)). Lineage weakens after extraction: facts are deduplicated by generated uniqueness hashes, counters are incremented on repeated mentions, and the active prompt context does not include source-message IDs, confidence, contradiction status, or a regeneration rule.

**Behavioral authority.** Raw traces and stored facts have knowledge-artifact authority when used as evidence, context, or audit material. Search scores and embedding vectors have ranking authority because they decide which facts become active. The injected `<memori_context>` block has system-definition-artifact authority for the next LLM call because it is inserted into a system, instruction, or prepended history channel. Its explicit policy is relevance-gated use, not hard enforcement.

**Scope.** The normal scope is per entity, optionally narrowed by process and session; agent APIs add project/session filters. The system is designed for personalization and application memory across sessions, not for cross-repository methodology curation.

**Timing.** Capture happens inline around each LLM call. Persistence is synchronous enough to keep the conversation record, while augmentation is designed as background or queued work. Recall happens online before the next LLM provider call.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Memori is a deploy-time trace-to-artifact memory system with automatic prompt-time activation. It strengthens the survey's distinction between raw trace retention and distilled artifacts: Memori keeps conversations and traces as source material, but the active memories are extracted facts, summaries, triples, attributes, and embeddings. It also shows a high-authority injection pattern where distilled knowledge artifacts become temporary system-definition artifacts without a manual promotion gate.

## Takeaways

**Memori is a real trace-derived memory system.** It does not merely store chat logs. The implementation captures LLM turns, extracts durable facts/triples/summaries/process attributes, retrieves relevant records, and injects them into later calls.

**Its strongest mechanism is activation, not governance.** The SDK makes memory hard to forget once installed because recall runs before LLM calls. It does less to make each memory independently reviewable, citable, or retireable.

**The artifact stack needs separate labels.** A Memori "memory" can mean a raw conversation row, an extracted fact, a graph triple, a summary, an embedding vector, a search score, or an injected prompt block. These differ in storage substrate, representational form, lineage, and behavioral authority.

**Cloud mode hides the most interesting extractor.** The open-source code clearly shows capture, request routing, parsing, storage, retrieval, and injection. It does not fully expose the semantic extraction oracle behind Advanced Augmentation, especially for agent trace interpretation.

**The prompt-injection policy is lightweight.** Memori tells the LLM to use recalled context only if relevant, but the authority boundary is still a system or instruction channel. That is useful for personalization, but risky as a route for operational rules without review.

## Curiosity Pass

The surprising part is how conventional the durable schema is. Beneath the product surface, Memori is not primarily a novel model architecture; it is a careful middleware-plus-database system with messages, sessions, facts, embeddings, process attributes, graph triples, and summaries.

The simpler alternative would be explicit retrieval APIs only. Memori chooses transparent wrapping instead, which improves activation but makes memory authority easier to forget. A developer can call the LLM normally while memory is silently prepended and distilled after the fact.

The tool-trace story is partly stronger in docs than in visible source. The repository contains explicit trace fields and agent augmentation paths, but the reviewed code does not expose a local, inspectable policy for turning tool calls and outcomes into reusable rules. The source-grounded claim is therefore capture-and-route plus cloud/native extraction, not fully open rule learning.

The deduplication and counter model is pragmatic. Facts, graph triples, and process attributes are upserted by uniqueness hashes and mention counts rather than curated as claims with contradiction handling ([memori/storage/drivers/sqlite/_driver.py](https://github.com/MemoriLabs/Memori/blob/57217f06be44abce87dfdb71b15c5f37fb741707/memori/storage/drivers/sqlite/_driver.py)). That is a good fit for recurring user preferences, weaker for evolving technical truth.

## Open Questions

- What extraction prompt, model, or ruleset decides which conversations become facts, triples, summaries, and process attributes?
- How does Memori handle contradictory facts about the same entity beyond deduplication and recency/frequency counters?
- Can a user audit an injected fact back to the exact source turn and trace payload in cloud mode?
- Does agent trace augmentation produce only facts and summaries, or can it derive procedure-like memories from tool outcomes?
- How are stale facts retired when preferences, tools, or project conventions change?
- What evaluation checks whether injected memories improve downstream agent behavior rather than merely increasing recall volume?

## What to Watch

- Whether the extractor/oracle for Advanced Augmentation becomes locally inspectable.
- Whether fact records gain explicit source-message IDs, confidence, contradiction state, and retirement metadata.
- Whether agent trace execution starts producing higher-authority artifacts such as rules, playbooks, tests, or validators.
- Whether prompt injection gains stronger policy controls for untrusted or low-confidence memories.
- Whether BYODB and cloud modes converge on the same lineage and audit surfaces.

## Bottom Line

Memori is best read as deploy-time memory middleware: it turns LLM and agent traces into compact database records and automatically activates them before future calls. For commonplace, the borrowable lesson is not automatic promotion, but the trace split: keep raw turns, distilled facts, summaries, triples, embeddings, retrieval scores, and injected context as different artifacts with different authority. Memori solves activation better than governance; commonplace should borrow the activation discipline without giving unreviewed extracted facts durable rule authority.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Memori is a deploy-time trace-to-artifact system with automatic prompt-time activation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Memori's conversations, facts, triples, embeddings, and prompt context need separate substrate, form, lineage, and authority labels.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: stored facts, summaries, and raw traces advise or evidence later behavior.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: injected recall context gains instruction-channel authority for the next LLM call.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Memori's central strength is automatic activation through LLM wrappers.
