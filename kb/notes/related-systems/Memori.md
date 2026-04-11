---
description: "Python/TypeScript SDK plus MCP/cloud memory layer that intercepts LLM calls, mines conversations and agent traces into facts/triples/summaries, and injects filtered recall context"
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-11"
---

# Memori

Memori is a Memori Labs memory SDK and hosted memory service for LLM applications and agents. The inspected repository contains a Python SDK, a TypeScript SDK, cloud/BYODB documentation, benchmark docs, and integration shells for OpenClaw and MCP-style clients. Its concrete loop is: intercept LLM calls, persist conversation turns under entity/process/session attribution, run background augmentation to extract durable facts, semantic triples, summaries, process attributes, and sometimes trace-aware agent memory, then recall filtered facts and conversation context into later prompts.

**Repository:** https://github.com/MemoriLabs/Memori

## Core Ideas

**Attribution is the main scoping primitive.** Memori does not rely on one global memory namespace. Both SDKs attach memory to an `entity_id`, optional `process_id`, and `session_id`. The Python schema creates `memori_entity`, `memori_process`, `memori_session`, `memori_conversation`, and `memori_conversation_message` records; the cloud and MCP flows send the same attribution shape to API endpoints. This is a simple but important separation: the same user can carry memory across processes, while a process can still narrow recall.

**The SDK wraps the LLM client rather than asking the application to call memory manually.** The Python wrapper replaces provider methods with `Invoke` classes that run recall injection before the original LLM call and post-response persistence/augmentation afterward. The TypeScript SDK uses `@memorilabs/axon` hooks in the same before/after pattern. That makes Memori more like prompt middleware than a standalone memory database: the application keeps using its OpenAI, Anthropic, Gemini, Agno, LangChain, or Pydantic AI client while Memori mutates the request/response path around it.

**Recall injects compact facts and optional history, not raw full context.** Python local recall embeds the query, searches entity facts, ranks by dense similarity plus lexical score when query text is available, filters by `recall_relevance_threshold`, then appends a `<memori_context>` block to the system prompt or provider-specific instruction field. Cloud recall can also return prior conversation messages, which the SDK prepends before the current messages. This is a pragmatic context-efficiency move: the prompt receives selected fact strings and summaries, not the whole conversation archive.

**Storage is database-backed and pluggable in Python, hosted-service-backed in TypeScript.** The Python SDK can run in cloud mode or BYODB mode. BYODB supports SQLAlchemy, DB-API, Django, MongoDB, and multiple SQL dialect drivers, with migrations for conversations, entity facts, process attributes, and a subject-predicate-object knowledge graph. The TypeScript SDK is thinner: it calls Memori Cloud endpoints for recall, persistence, and augmentation, and uses Axon for client interception. So the repo contains more inspectable storage mechanics for Python than for TypeScript.

**BYODB does not mean fully local augmentation in the inspected code.** This is the main README-vs-code boundary. In Python BYODB mode, conversation rows and extracted outputs are written into the user's database, and embeddings are generated locally. But `AdvancedAugmentation.process(...)` still sends normalized conversation messages and metadata to `sdk/augmentation` through `Api.augmentation_async(...)` before writing returned facts/triples/summaries locally. BYODB is a local storage boundary, not a fully local extraction boundary, unless the hosted augmentation API is replaced by a custom endpoint.

**The learned artifact is structured service memory, not editable knowledge.** Memori promotes conversation traces into entity facts, semantic triples, process attributes, conversation summaries, and in the TypeScript integration path an `agent/augmentation` payload that can include `trace` and `summary`. These are symbolic artifacts, but they live as database rows or hosted API state rather than as human-editable notes. The system favors automatic accumulation and compact recall over curation, explicit argument structure, and reviewable link semantics.

**The benchmark framing is context structuring over raw retrieval.** The LoCoMo docs present Memori's strongest claim as a memory-structuring claim: extract semantic triples plus conversation summaries, retrieve a small prompt footprint, and approach full-context accuracy. The reported results are useful directional evidence, especially the explicit temporal-reasoning weakness, but the benchmark pipeline is partly docs-side evidence; the open repo lets us inspect SDK/storage/retrieval mechanics more directly than the hosted extraction engine itself.

## Comparison with Our System

| Dimension | Memori | Commonplace |
|---|---|---|
| Primary substrate | Hosted API memory plus Python database rows for BYODB | Markdown files in git |
| Source trace | LLM request/response turns, cloud conversation history, optional agent trace payloads | Human+agent edits, notes, source snapshots, workshop artifacts |
| Learned artifact | Facts, triples, summaries, process attributes, cloud memories | Notes, links, instructions, indexes, ADRs |
| Recall surface | Automatic prompt injection and MCP/SDK recall tools | Agent-driven navigation via descriptions, indexes, links, and search |
| Curation model | Mostly automated extraction/dedup/update inside service logic | Human+agent review, semantic links, status, validation |
| Storage governance | Entity/process/session scoping; database-backed deletion in BYODB | Git history, file paths, frontmatter, validation gates |
| Inspectability | SQL/API/dashboard level; hosted extraction opaque | Every artifact is directly readable and diffable |
| Context strategy | Compact fact/summary injection into prompts | Progressive disclosure through note descriptions and explicit links |

Memori is stronger on turnkey integration. Wrapping existing LLM clients and exposing MCP/OpenClaw-style flows is the right product shape for applications that want memory without rebuilding their agent loop. The attribution triple is also a clean low-friction answer to cross-user and cross-workflow memory pollution.

Commonplace is stronger on knowledge quality and inspectability. A Memori fact can be recalled, but it does not explain why it matters, how it relates to adjacent claims, or whether it has matured beyond extraction. A Commonplace note costs more to create, but it can carry evidence, counterclaims, link semantics, and review state.

The systems also sit on different sides of the storage-substrate tradeoff. Memori's database/service shape is appropriate for high-throughput personalization memory. Commonplace's file shape is appropriate when the methodology itself must be inspectable and refactorable by agents. In the terms of [substrate class, backend, and artifact form](../substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md), Memori still produces symbolic artifacts; the difference is that the backend is a service/database and the artifact form is fact/triple/summary records rather than markdown arguments.

Memori belongs in the trace-derived learning survey as a service-owned trace-to-symbolic-memory system. Its weakest trace-derived form is ordinary conversation mining; its stronger agent-facing form is the TypeScript integration path that can send `trace` and `summary` to an agent augmentation endpoint.

## Borrowable Ideas

**Entity/process/session attribution as a minimum memory scope.** Ready to borrow as a design pattern. If Commonplace ever adds runtime memory tools or workshop capture APIs, this three-axis scope is a useful floor: who the memory is about, which process produced it, and which session it came from.

**Automatic prompt injection with a relevance caveat.** Ready to borrow only for generated context, not for library notes. Memori's `<memori_context>` wrapper explicitly tells the model to use recalled facts only when relevant. That is a small but useful guard for any future agent-facing retrieval output.

**Fact summaries linked back to source conversations.** Needs a use case first. Memori's `memori_entity_fact_mention` table and summary attachment path preserve a bridge from compact fact to conversation-level context. A workshop capture system could use the same two-layer shape: atomic extracted claim plus source-turn summary.

**Read barrier after background writes.** Ready to borrow if we build async capture. Memori's augmentation manager and DB writer run in the background but provide `wait()` for scripts. The general pattern is useful: keep writes non-blocking during the main turn, but expose an explicit drain point before the process exits or before recall depends on the new material.

**MCP usage skill as behavioral policy around a weak tool contract.** Ready to borrow as a reminder, not as code. The docs' Memori MCP skill says when to recall, when to augment, and what not to store. That recognizes a real problem: memory tools need call policy, not just tool schemas.

## Curiosity Pass

**"Memory from what agents do" is partly implemented and partly service-bound.** The TypeScript integration can send a `trace` object and summary to `agent/augmentation`, and the OpenClaw docs describe before/after lifecycle hooks. That is more than ordinary chat-memory framing. But the inspectable repo does not show the server-side agent augmentation algorithm, so the strongest "execution trace" claim is an API contract, not a locally inspectable extraction mechanism.

**BYODB transforms the storage boundary more than the extraction boundary.** The docs present BYODB as local ownership, and the local migrations are real. But the advanced augmentation path still posts conversation messages to Memori's API and writes the response locally. The property produced is local persistence and queryability of extracted memory, not fully self-contained local processing.

**The knowledge graph is real but recall is still fact-first.** The schema and drivers implement subjects, predicates, objects, graph rows, mention counts, and deduplication. Local recall, however, searches `entity_fact` embeddings and formats fact strings plus summaries. The graph improves stored structure and direct SQL inspection, but the code path reviewed does not use graph traversal as a primary recall mechanism.

**Embedding defaults look inconsistent across docs and code.** The docs say recall uses `all-mpnet-base-v2` with 768 dimensions; the Python `Config` default is `all-MiniLM-L6-v2`. This may be a documentation lag or a cloud/BYODB distinction, but it matters because retrieval quality claims depend on the actual embedding model.

**The strongest mechanism is middleware placement, not the memory taxonomy.** Facts, preferences, rules, skills, triples, and summaries are common categories across memory systems. Memori's distinct move is the integration path: intercept provider calls, inject recall before the LLM sees the request, persist and augment after the response, and make that work across SDKs and MCP clients.

**The ceiling is automatic extraction quality.** Even if the storage, recall threshold, and prompt wrapper work perfectly, Memori still depends on the hosted augmentation engine to decide what becomes durable. That is fine for preferences and simple user facts, but it is not a substitute for the explicit review loop needed for durable methodology notes.

## What to Watch

- Whether the hosted augmentation engine becomes inspectable or replaceable enough for BYODB users to verify privacy and extraction quality
- Whether agent-trace augmentation becomes a documented, public contract beyond the TypeScript integration payload shape
- Whether graph traversal affects recall, or whether the graph remains mostly a storage/observability layer around fact retrieval
- Whether the embedding-model mismatch between docs and Python config gets resolved
- Whether MCP memory policy stays prompt-compliance-based or gains stronger client-side guardrails against storing secrets, transient task logs, and one-off progress updates
- Whether benchmark claims remain reproducible from public artifacts as the cloud extraction engine evolves

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Memori is a service-owned conversation/agent-trace-to-symbolic-memory case that should be placed alongside other live-session trace-mining systems
- [Substrate class, backend, and artifact form are separate axes that get conflated](../substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: Memori's database/API backend does not make its learned state a separate substrate class; the learned outputs are still symbolic artifacts
- [Distillation](../definitions/distillation.md) — contrasts: Memori extracts compact facts/triples/summaries from conversations, but does not provide the stronger curation and synthesis discipline this KB expects from durable notes
- [Context efficiency is the central design concern in agent systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — exemplifies: Memori invests in prompt-footprint reduction by injecting selected facts and summaries instead of raw conversation history
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — contrasts: Memori exposes memory through SQL/API/dashboard surfaces, while Commonplace keeps the primary learned artifacts directly inspectable as files
- [Mem0 Memory Layer](../../sources/mem0-memory-layer.ingest.md) — compares: both use automated extraction into external memory records, but Memori's inspected repo foregrounds SDK interception, entity/process/session scoping, and conversation-summary attachment
