---
description: "MemoryOS review: hierarchical JSON/Chroma memory with trace summarization, profile extraction, FAISS retrieval, and MCP tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# MemoryOS

MemoryOS, from BAI-LAB, is an open-source memory layer for personalized AI agents. At the reviewed commit it ships several near-duplicate Python implementations: a PyPI-style package, an MCP server wrapper, a ChromaDB-backed variant, a playground, and evaluation scripts. The core system stores user/assistant turns as short-term memory, promotes evicted turns into summarized mid-term sessions, derives user profiles and knowledge entries from hot sessions, retrieves relevant memory with embeddings and thresholds, and can generate a response with recalled memory assembled into the prompt.

**Repository:** https://github.com/BAI-LAB/MemoryOS

**Reviewed commit:** [1d717060350931af33d1d0dc3d4e50a72c125a48](https://github.com/BAI-LAB/MemoryOS/commit/1d717060350931af33d1d0dc3d4e50a72c125a48)

**Last checked:** 2026-06-02

## Core Ideas

**The advertised architecture is a three-layer personal memory stack.** The README describes short-term, mid-term, and long-term persona memory, and the PyPI implementation wires those modules in `Memoryos.__init__()` as `ShortTermMemory`, `MidTermMemory`, user `LongTermMemory`, assistant `LongTermMemory`, an `Updater`, and a `Retriever` ([README](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/README.md), [memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). Short-term memory is a bounded deque of QA pairs saved to JSON; mid-term memory is session summaries plus page records; long-term memory stores a user profile, user knowledge, and assistant knowledge ([short_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/short_term.py), [mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py), [long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/long_term.py)).

**Promotion is capacity- and heat-triggered.** `add_memory()` writes a QA pair to short-term memory, but first moves old turns into mid-term memory when the short-term deque is full. The updater asks an LLM whether adjacent pages are continuous, generates page meta summaries, asks for at most two topic summaries, and inserts the pages into an existing or new mid-term session by summary embedding and keyword similarity ([memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [updater.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/updater.py), [prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). Mid-term sessions carry visit count, interaction length, recency, heat, LFU counters, page embeddings, and page links.

**Long-term memory is distilled from hot mid-term sessions.** After each add, MemoryOS checks the hottest mid-term session. When heat crosses `mid_term_heat_threshold`, it analyzes unanalyzed pages in parallel: one LLM call updates the complete user profile from the previous profile plus the new pages, while another extracts user private knowledge and assistant knowledge. Accepted lines are appended into long-term user or assistant knowledge stores with embeddings, and analyzed pages are marked so the session is not repeatedly distilled ([memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [utils.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/utils.py), [prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)).

**Retrieval is bounded and parallel, but not deeply governed.** `Retriever.retrieve_context()` concurrently searches mid-term pages, user long-term knowledge, and assistant long-term knowledge. Mid-term search embeds the query, uses FAISS inner-product search over session summaries, filters by segment and page thresholds, and returns the top scored pages up to `retrieval_queue_capacity`. Long-term knowledge search embeds the query and returns top-k entries over FAISS indexes built from stored knowledge embeddings ([retriever.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/retriever.py), [mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py), [long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/long_term.py)). Context efficiency is therefore thresholded top-k selection plus fixed short-term history, not progressive disclosure or a typed context budget.

**Read-back has both explicit tools and a pre-call wrapper.** The MCP server exposes `add_memory`, `retrieve_memory`, and `get_user_profile` tools, so an agent can pull memory deliberately through MCP ([server_new.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-mcp/server_new.py)). The library-level `get_response()` path is stronger: it retrieves pages and knowledge before calling the LLM, formats short-term history, retrieved mid-term pages, user profile, user knowledge, assistant knowledge, and conversation metadata into the system/user prompt pair, then stores the new interaction after generation ([memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)).

**The ChromaDB variant swaps storage substrate but keeps the same artifact model.** `memoryos-chromadb` replaces JSON-plus-FAISS persistence with a `ChromaStorageProvider` that stores mid-term summaries/pages and user/assistant knowledge in persistent Chroma collections, while preserving JSON metadata for short-term memory, user profiles, session metadata, access frequency, heap state, and page backups ([storage_provider.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/storage_provider.py), [memoryos-chromadb/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/memoryos.py)). This improves deployment options, but the reviewable behavior-shaping artifacts remain the same: trace pages, summaries, profiles, knowledge entries, embeddings, thresholds, and prompt templates.

## Artifact analysis

- **Storage substrate:** `vector` — JSON files in `users/<user_id>/short_term.json`, or Chroma variant metadata
- **Representational form:** `prose` `symbolic` `parametric` — Prose turns, summaries, profiles, knowledge entries, and prompts; symbolic ids, timestamps, metadata, thresholds, counters, and tool schemas; embeddings/FAISS or Chroma vector retrieval state
- **Lineage:** `authored` `trace-extracted` — Authored prompts, thresholds, capacities, schemas, and update policies operate over raw interaction traces that are summarized and distilled into mid-term and long-term memory
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — Retrieved memory acts as advisory context; prompts and wrapper code instruct prompt assembly; embeddings, thresholds, heat, and top-k parameters route and rank memory; trace promotion and extraction form the learning path

**Short-term QA pairs.** Storage substrate: JSON files in `users/<user_id>/short_term.json`, or Chroma variant metadata. Representational form: structured rows with prose `user_input`, `agent_response`, and timestamps. Lineage: raw interaction traces inserted by `add_memory()` or through the MCP `add_memory` tool; invalidated by deque capacity, migration to mid-term, or storage deletion. Behavioral authority: advisory context when `get_response()` includes the whole short-term history in the next prompt; source material for later mid-term summaries.

**Mid-term sessions and pages.** Storage substrate: JSON `mid_term.json` with session dictionaries and page records, or Chroma mid-term collections plus metadata backups. Representational form: mixed prose summaries/pages, symbolic ids, page links, heat/visit/LFU/recency counters, keywords, and distributed-parametric embeddings. Lineage: derived from evicted short-term traces by LLM continuity checks, meta-summary generation, multi-topic summarization, embedding, and similarity-based session insertion. Behavioral authority: knowledge artifacts when retrieved as historical pages; ranking/routing artifacts through embeddings, thresholds, heat, and access counters; source material for long-term profile and knowledge extraction.

**Long-term user profile and knowledge stores.** Storage substrate: JSON `long_term_user.json` and `long_term_assistant.json`, or Chroma user/assistant knowledge collections plus profile metadata. Representational form: prose profile text, prose knowledge bullets, timestamps, and embeddings. Lineage: trace-extracted from unanalyzed hot mid-term pages by LLM prompts; exact source spans, prompt/model versions, confidence, and reviewer acceptance state are not retained per knowledge item. Behavioral authority: advisory personalization context and response background; embeddings and top-k search give the stored items ranking authority over what reaches the prompt.

**Prompts, thresholds, capacities, and update policies.** Storage substrate: repository Python modules, runtime constructor/config values, and MCP config JSON. Representational form: prose prompts plus symbolic parameters: capacities, thresholds, `top_k`, heat formula constants, embedding model names, and MCP schema. Lineage: authored system-definition artifacts. Behavioral authority: instruction, extraction, routing, ranking, and prompt-assembly authority over future memory creation and read-back.

**MCP tool outputs and generated response prompts.** Storage substrate: ephemeral MCP responses and LLM call messages assembled by `get_response()`. Representational form: structured JSON for MCP; assembled prose sections for model calls. Lineage: derived at query time from the current query, stored short/mid/long memories, metadata, and retrieval thresholds. Behavioral authority: MCP output is advisory context for the calling agent; `get_response()` prompt assembly is stronger pre-action context because recalled memory is already inside the model call before the model answers.

**Evaluation scripts and LoCoMo data.** Storage substrate: `eval/` Python scripts and JSON data. Representational form: symbolic experiment code, datasets, prompts, retrieval queues, and answer-generation flows. Lineage: derived from benchmark conversations and the same memory modules. Behavioral authority: evaluation evidence for retrieval/answering claims, not runtime authority over user agents ([eval](https://github.com/BAI-LAB/MemoryOS/tree/1d717060350931af33d1d0dc3d4e50a72c125a48/eval)).

Promotion path: MemoryOS has an operational promotion path from raw QA traces to mid-term summaries/pages, then to long-term profile and knowledge entries, then to recalled prompt context. It does not promote extracted memory into reviewed rules, tests, validators, or typed instructions; stronger authority comes from the wrapper that injects recalled material into a prompt, not from governance over the memory itself.

## Comparison with Our System

| Dimension | MemoryOS | Commonplace |
|---|---|---|
| Primary purpose | Runtime personal memory for an AI assistant or MCP-connected agent | Git-native methodology KB for agent-operated knowledge bases |
| Canonical retained artifacts | QA pairs, session summaries/pages, user profile, user/assistant knowledge, embeddings | Typed Markdown notes, instructions, ADRs, reviews, source snapshots, indexes, reports |
| Storage substrate | JSON files, FAISS in-memory indexes rebuilt from embeddings, optional ChromaDB collections | Repository files plus generated indexes, validation reports, and review-run reports |
| Write path | Automatic trace capture, LLM summarization, heat-triggered profile/knowledge extraction | Human/agent-authored artifacts, source snapshots, explicit review and validation |
| Read-back | MCP pull tools plus library wrapper that injects retrieved memory into an LLM prompt | Mostly explicit pull via `rg`, indexes, links, skills, and loaded instructions |
| Governance | Thresholds, capacities, prompts, simple schemas, benchmark scripts | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

MemoryOS is closer to an application memory subsystem than to a governed knowledge base. It is valuable when the goal is to let a chatbot remember recent interaction state, profile traits, and distilled personal facts with little operator friction. Commonplace is stronger where durable memory must be inspectable, source-grounded, versioned, and deliberately promoted into behavioral authority.

The most important difference is that MemoryOS collapses memory maintenance into runtime heuristics. Capacity pressure, heat, embedding similarity, LLM extraction prompts, and prompt assembly decide what is retained and reused. Commonplace keeps those decisions visible as files, type specs, validation runs, review artifacts, and diffs. MemoryOS makes personalization cheap; Commonplace makes memory authority reviewable.

**Read-back:** `both` — MCP tools are pull, but `get_response()` implements an instance-targeted, embedding-selected memory push from the receiving model's perspective by retrieving relevant memory before the model call and inserting it into the generated system/user prompt

### Borrowable Ideas

**Use heat as a candidate-prioritization signal, not as authority.** Ready for workshops. Commonplace could use access frequency, recency, and interaction length to rank candidate notes or review targets, but should not let heat alone promote a memory into instructions or validators.

**Keep short-term, mid-term, and long-term as lifecycle states.** Ready as vocabulary. MemoryOS's layers are less important as storage locations than as lifecycle stages: raw turn buffer, summarized working memory, and distilled standing knowledge. Commonplace can use that framing for workshop artifacts without adopting automatic promotion.

**Borrow explicit assistant/user knowledge separation.** Needs a use case first. The split between user profile, user private knowledge, and assistant knowledge is useful for personalization systems; in Commonplace it would translate to separating operator preferences, project facts, and agent self-description.

**Treat page chains and meta summaries as navigational aids.** Ready for exploratory work. Conversation-page links and compact meta summaries could help preserve continuity in workshop logs, but they need source spans and expiry before becoming library artifacts.

**Do not borrow profile extraction without lineage.** MemoryOS updates a complete user profile from hot sessions, but the stored profile lacks source-span provenance and acceptance review. In Commonplace, an analogous extractor should produce candidates with citations, not directly rewrite durable notes.

**Use ChromaDB as an optional retrieval cache only.** Needs a concrete search layer. The Chroma variant shows how vector storage can accelerate search while JSON metadata remains available; Commonplace should keep Markdown as the source of truth if it adds a vector cache.

## Write-side placement

**Write agency:** `manual` `automatic` — `add_memory()` and MCP `add_memory` provide an explicit write interface, while `get_response()` and the update path automatically store QA traces, promote evicted turns, update profiles, and extract long-term knowledge.

**Curation operations:** `consolidate` `evolve` `synthesize` `decay` `promote` — short-term turns are summarized into mid-term pages, the complete user profile is updated from prior profile plus new pages, private/assistant knowledge entries are extracted from hot sessions, bounded deques/LFU/capacity limits forget or evict, and heat-triggered analysis promotes mid-term traces toward long-term profile and knowledge state.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — MemoryOS consumes user/assistant QA conversation traces, timestamps, optional metadata, page chains, retrieval visits, and benchmark conversation records.

**Learning scope:** `per-project` — The review evidence scopes retained memory per user and assistant under `users/<user_id>` and `assistants/<assistant_id>` or equivalent Chroma collection names.

**Learning timing:** `online` `staged` — Each `add_memory()` can update short-term traces online, while short-to-mid promotion and heat-triggered long-term extraction happen as staged steps around writes.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation produces prose summaries, profile text, and knowledge entries, plus symbolic metadata/counters/thresholds and embedding-backed retrieval state.

**Trace source.** MemoryOS qualifies as trace-derived. Raw signals are user/assistant QA pairs written through the library or MCP server, timestamps, optional metadata, page chains, retrieval visits, and benchmark conversations.

**Extraction.** The first extraction step moves full short-term turns into mid-term page objects, then LLM prompts decide continuity, meta summaries, and topic summaries. The second extraction step runs when a mid-term session becomes hot: LLM prompts update the user profile and extract user private knowledge plus assistant knowledge. The oracle is the configured chat model plus prompt templates; the code filters empty or `"None"` outputs but does not include a reviewer, confidence score, or source-span check.

**Four fields.** The raw stage is short-term QA trace data: prose plus timestamps and optional metadata in JSON/Chroma metadata. The distilled stage is mixed prose-symbolic-distributed state: mid-term summaries/pages, profile text, knowledge entries, embeddings, heat/access counters, and retrieval thresholds. Raw traces mostly carry source/context authority; distilled artifacts gain advisory context authority and ranking authority when retrieval selects them for a later prompt.

**Scope and timing.** Scope is per user and assistant, with file paths under `users/<user_id>` and `assistants/<assistant_id>` or equivalent Chroma collection names. Timing is online and staged: each `add_memory()` can trigger short-to-mid promotion before insertion, then heat-triggered long-term extraction after insertion; `get_response()` performs retrieval before generation and writes the new turn afterward.

**Survey placement.** MemoryOS belongs in the trace-to-profile and trace-to-knowledge-entry family. It strengthens the survey distinction between memory extraction and contextual activation: extracted profiles and knowledge become behavior-shaping only when the response wrapper or an agent pulls them back into context.

## Read-back placement

**Direction.** MemoryOS is both pull and push. MCP `retrieve_memory` and `get_user_profile` are explicit pull tools. The library `get_response()` path is push from the receiving model's perspective because retrieval happens before the model call and recalled memory is placed into the prompt. This is implemented as a response-wrapper API surface rather than MCP hook wiring; callers get push activation when they delegate the answer generation path to MemoryOS.

**Read-back signal:** `coarse` `inferred / embedding` — The wrapper includes short-term history and the raw user profile coarsely, and uses query embeddings over FAISS or Chroma-backed memory for instance-targeted recall.

**Faithfulness tested:** `no` — The review found retrieval and answering evaluation scripts, but no with/without ablation proving pushed memory changes downstream model behavior or agent actions.

**Targeting and signal.** The engineered memory push is `instance` targeted: `get_response(query)` uses the current query as the instance payload. Its selector is `inferred / embedding`, not an identifier match: the code embeds the query, runs FAISS inner-product search over mid-term session summaries/pages and long-term knowledge entries, then filters by segment/page/knowledge thresholds and top-k capacities. Short-term history and the raw user profile are included by the wrapper without semantic selection, so those inclusions are coarse context inside the same pre-call path.

**Injection point.** Retrieval and prompt assembly happen before the final LLM response, so memory can change the next answer. The new QA pair is written after generation as write-side maintenance for later turns. Heat-triggered profile and knowledge extraction can also run after a write and shape later retrieval.

**Selection, scope, and complexity.** Selection is bounded by short-term capacity, `retrieval_queue_capacity`, `top_k_sessions`, `top_k_knowledge`, similarity thresholds, mid-term heat, LFU eviction, and long-term knowledge capacity. Context complexity is moderate: the prompt can include recent history, historical pages with meta info, user profile text, user knowledge, assistant knowledge, and metadata in one assembled call, but it does not load the whole store.

**Authority at consumption.** Retrieved memory is advisory context. It enters the LLM call through system and user prompt templates, so the wrapper has system-definition authority over prompt construction, while the memory items themselves remain knowledge artifacts. Effective authority is not verified from code.

**Faithfulness.** I found evaluation scripts for retrieval and answering, but not a with/without ablation proving that pushed memory reliably changes model behavior or improves agent actions under the MCP integrations. The push mechanism is structurally implemented; precision, recall, and downstream use remain runtime claims.

**Other consumers.** Human developers and operators consume MemoryOS through JSON/Chroma storage files, MCP tool results, the playground, benchmark scripts, and README/docs. Those surfaces help inspect counts and outputs, but they do not provide Commonplace-style review status or promotion decisions.

## Curiosity Pass

**The "operating system" metaphor is mostly an architecture metaphor.** The code implements useful lifecycle stages, thresholds, and storage variants, but not isolation, permissions, transactional governance, or kernel-like policy enforcement.

**The strongest implementation is small and direct.** The PyPI path is a compact Python runtime around JSON, embeddings, LLM prompts, and FAISS. The Chroma and MCP directories largely repackage the same memory model.

**Heat is doing two jobs.** It prioritizes what to analyze, and it indirectly decides which traces become long-term persona state. That is efficient, but it mixes salience with trust.

**Lineage is weaker than the memory hierarchy.** The system knows which pages were analyzed and when entries were recorded, but profile and knowledge entries do not retain exact source turns, extraction prompt versions, model versions, or reviewer decisions.

**MCP integration does not by itself create push.** The MCP server exposes retrieval and profile tools; automatic activation depends on a host choosing to call them. The push evidence comes from `get_response()`, not from the MCP server alone.

## What to Watch

- Whether MemoryOS starts storing source turn ids, source spans, extraction prompts, model names, and confidence/review status per profile or knowledge item; that would make trace-derived lineage much more auditable.
- Whether MCP clients add hook-level automatic recall before prompts; that would move the MCP integration from pull tooling toward deployed push activation.
- Whether the ChromaDB implementation becomes the canonical path rather than a parallel variant; that affects whether MemoryOS should be described as JSON-first or vector-store-first.
- Whether evaluations add with/without memory ablations for generated responses and agent tasks, not only retrieval-and-answer benchmark scores.
- Whether hot-session profile extraction gets curation or rollback controls; without them, profile drift remains the main governance risk.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: MemoryOS derives summaries, profiles, and knowledge entries from conversation traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: MemoryOS storage only affects behavior when retrieved through tools or prompt assembly.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: MemoryOS requires separating raw traces, summaries, profile text, knowledge entries, embeddings, and prompt policies by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: QA traces, retrieved pages, profile text, and knowledge entries mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, thresholds, capacities, retrieval code, and MCP schemas configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: MemoryOS turns conversation traces into durable summaries, profiles, and knowledge entries through LLM extraction.
