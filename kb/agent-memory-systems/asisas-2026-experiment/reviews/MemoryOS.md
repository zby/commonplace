---
description: "MemoryOS review: hierarchical conversational memory with trace-derived summaries, profiles, knowledge extraction, vector retrieval, and pre-call prompt assembly"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# MemoryOS

MemoryOS, from BAI-LAB, is a Python memory layer for personalized conversational agents. At the reviewed commit, it implements short-term dialogue capture, mid-term session condensation, long-term user and assistant memory, retrieval across those layers, an MCP server, a playground, and a ChromaDB-backed variant. Its operating-system metaphor is implemented as tiered conversational storage plus update and retrieval policies, not as a general OS substrate.

**Repository:** https://github.com/BAI-LAB/MemoryOS

**Reviewed commit:** [1d717060350931af33d1d0dc3d4e50a72c125a48](https://github.com/BAI-LAB/MemoryOS/commit/1d717060350931af33d1d0dc3d4e50a72c125a48)

**Source directory:** `related-systems/BAI-LAB--MemoryOS`

## Core Ideas

**Memory is tiered by conversational timescale.** The PyPI implementation initializes user-specific `short_term.json`, `mid_term.json`, and `long_term_user.json` files plus assistant-specific `long_term_assistant.json`, then wires `ShortTermMemory`, `MidTermMemory`, `LongTermMemory`, `Updater`, and `Retriever` through `Memoryos.__init__` ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). The short-term layer stores timestamped user/assistant QA pairs in a bounded deque persisted as JSON ([memoryos-pypi/short_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/short_term.py)).

**Short-term overflow condenses dialogue traces into mid-term sessions.** When the short-term buffer is full, `Updater.process_short_term_to_mid_term()` pops old QA pairs, asks LLM prompts to detect continuity, generate page meta summaries, and produce at most two topic summaries with keywords, then inserts the resulting pages into a mid-term session ([memoryos-pypi/updater.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/updater.py), [memoryos-pypi/prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). The raw dialogue pages remain inside the session, so condensation adds a navigable summary rather than fully replacing the trace.

**Mid-term memory is heat-ranked and embedding-searchable.** Each session stores summary text, keywords, summary embeddings, page embeddings, visit count, interaction length, recency, access count, and `H_segment`; search builds a FAISS inner-product index over session summaries and filters pages by embedding similarity ([memoryos-pypi/mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py)). Session retrieval mutates access statistics and recomputes heat, so read activity affects future update priority.

**Hot sessions are distilled into profile and knowledge records.** When the hottest mid-term session crosses `mid_term_heat_threshold`, MemoryOS analyzes unanalyzed pages in parallel: one path rewrites the user profile, while another extracts user private knowledge and assistant knowledge, then stores long-term entries with timestamps and embeddings ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-pypi/long_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/long_term.py), [memoryos-pypi/utils.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/utils.py)). The extraction oracle is the configured LLM plus prompt templates and numeric thresholds, not a human reviewer or a provenance-preserving validator.

**Read-back is implemented inside generation as well as exposed as tools.** `Retriever.retrieve_context()` searches mid-term pages, user knowledge, and assistant knowledge in parallel, while `Memoryos.get_response()` formats short-term history, retrieved pages, user profile, user knowledge, assistant knowledge, current metadata, relationship, and query into prompt messages before the LLM call; the generated response is then written back to memory ([memoryos-pypi/retriever.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/retriever.py), [memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). The MCP server exposes narrower `add_memory`, `retrieve_memory`, and `get_user_profile` tools for host clients ([memoryos-mcp/server_new.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-mcp/server_new.py)).

**Context efficiency is bounded by queues and top-k, not by token budgeting.** Retrieval caps pages through `retrieval_queue_capacity`, sessions through `top_k_sessions`, and knowledge through `top_k_knowledge`; short-term history and user profile are included wholesale in `get_response()` ([memoryos-pypi/retriever.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/retriever.py), [memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)). The system reduces context complexity by separating recent history, session pages, profile, user facts, and assistant facts, but it does not implement a token budget, progressive disclosure ladder, citation check, or faithfulness audit.

## Artifact analysis

- **Storage substrate:** `files` `vector` — The PyPI and MCP paths persist short-term, mid-term, and long-term memory as JSON files under the configured data path while rebuilding FAISS indexes at query time; the ChromaDB variant uses persistent Chroma collections for mid-term summaries/pages and long-term knowledge, with a JSON metadata sidecar for profile, short-term, heap, and session metadata ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-pypi/mid_term.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/mid_term.py), [memoryos-chromadb/storage_provider.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-chromadb/storage_provider.py)).
- **Representational form:** `prose` `symbolic` `parametric` — Dialogue turns, summaries, profiles, and knowledge strings are prose; ids, timestamps, page links, heat values, thresholds, JSON objects, MCP schemas, and prompt templates are symbolic; FAISS/Chroma vectors and sentence embeddings are parametric retrieval state.
- **Lineage:** `authored` `trace-extracted` — Prompts, code, configuration, and capacity policies are authored, while the durable memory content is extracted from user/assistant dialogue traces and later LLM outputs written back as new turns.
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — Stored pages, profiles, and facts are knowledge artifacts when retrieved; prompt templates and injected assistant knowledge can instruct the next model call; user/assistant ids, session/page links, and memory tiers route retrieval; embeddings and heap scores rank candidates; heat-triggered analysis and LLM extraction learn new retained records from traces.

**Short-term QA pairs.** These are raw dialogue trace artifacts: timestamped user input and assistant response records persisted in JSON or Chroma metadata. They are knowledge artifacts while retained as recent history, and they become source material for later condensation.

**Mid-term sessions and pages.** A session bundles a prose summary, summary keywords, summary embedding, page records, page embeddings, continuity links, meta summaries, visit counts, recency, and heat. The operative split matters: raw pages preserve trace evidence, summaries compact that evidence, embeddings rank it, and heat determines which sessions become candidates for long-term extraction.

**Long-term user and assistant records.** User profiles, user knowledge entries, and assistant knowledge entries are distilled from hot mid-term pages. In the JSON path, knowledge entries include text, timestamp, and embedding; in the Chroma path, knowledge is stored as Chroma metadata plus embeddings. These records are useful for personalization but weak on lineage: they do not preserve mandatory source page ids, extraction prompt version, confidence, contradiction state, or invalidation rule.

**Retrieval and generation prompt package.** The read path constructs an instruction-bearing prompt package from recent history, retrieved historical pages, profile text, retrieved user facts, retrieved assistant facts, current metadata, relationship, and query ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py), [memoryos-pypi/prompts.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/prompts.py)). At this point ordinary knowledge artifacts temporarily gain stronger behavioral force because they are inserted into the next model call.

**MCP tools.** The MCP server is a symbolic interface over one configured MemoryOS instance. `add_memory` changes the store, `retrieve_memory` returns short-term memory plus retrieved mid-term and long-term records, and `get_user_profile` exposes profile and optional knowledge records. This surface is pull-oriented for host agents even though the library's own `get_response()` method performs pre-call prompt assembly.

MemoryOS does have a promotion path from raw turns to summaries, profiles, and knowledge records. It does not promote extracted memories into stronger governed artifacts such as rules, validators, executable tools, or reviewed instructions.

## Comparison with Our System

| Dimension | MemoryOS | Commonplace |
|---|---|---|
| Primary purpose | Online personalization memory for conversational agents | Git-native methodology KB for agent-operated knowledge bases |
| Main retained artifact | QA turns, sessions, profiles, knowledge entries, embeddings | Typed Markdown notes, reviews, sources, instructions, ADRs, indexes |
| Write behavior | Automatic trace capture, condensation, heat-triggered extraction, capacity eviction | Authored and reviewed artifacts, validation, replacement history, explicit workflows |
| Retrieval | Embedding search plus prompt assembly and MCP tools | `rg`, authored links, indexes, collection contracts, skills, validation/review commands |
| Governance | Prompt templates, thresholds, demos, and benchmark scripts | Type specs, schemas, validation, semantic review, provenance expectations |
| Context assembly | Built into `get_response()` for one conversational assistant | Mostly explicit loading by agents and commands, with stronger artifact contracts |

MemoryOS and Commonplace agree that stored knowledge matters only when it can change later behavior. MemoryOS is stronger at the live conversational loop: capture a turn, condense older turns, extract profile/facts, retrieve relevant memory, build a prompt, generate, and store the new response. Commonplace is stronger at durable governance: artifacts have names, types, links, source expectations, validation, review records, and git history.

The main tradeoff is authority. MemoryOS lets LLM-derived profiles and facts shape future prompts soon after extraction. That is suitable for personalization memory, where recall throughput matters, but it is too weak for methodology claims or operational instructions unless a review layer adds source links, contradiction handling, and retirement policy.

The second tradeoff is context discipline. MemoryOS separates context by tier and caps retrieved pages, but it still includes profile and short-term history broadly and lacks token-budget reasoning. Commonplace currently relies more on explicit navigation and agent judgment; MemoryOS shows what a more automatic read-back layer can look like, but also why automatic memory needs stronger provenance.

### Borrowable Ideas

**Use heat as a distillation trigger.** A Commonplace analogue could prioritize logs, review warnings, or repeated work notes for promotion review when access, recency, and interaction length show they matter. Ready for workshop queues, but not for direct library-note rewriting.

**Keep timescale tiers separate.** MemoryOS distinguishes fresh turns, session summaries, durable profiles, user facts, assistant facts, and retrieval vectors. Commonplace should keep raw logs, distilled notes, generated indexes, and instruction artifacts equally distinct. Ready as vocabulary and as an implementation constraint for future trace tools.

**Expose narrow memory tools.** The MCP shape - add memory, retrieve memory, get profile - is simple enough for host clients. A Commonplace version would need typed inputs, provenance, and permissions, but the small surface is practical.

**Do not borrow automatic promotion without review.** MemoryOS extracts profile and knowledge records automatically from dialogue. Commonplace should route similar extraction through suggestions or workshop artifacts until source grounding and authority are reviewed.

## Write side

**Write agency:** `manual` `automatic` — Hosts and users can call library or MCP write methods to add conversation pairs, while MemoryOS automatically moves full short-term buffers into mid-term sessions, computes embeddings, merges pages into sessions, updates heat/access counters, extracts long-term profile and knowledge records from hot sessions, and evicts by capacity.

**Curation operations:** `consolidate` `evolve` `decay` — Short-term overflow condenses stored QA pairs into session summaries; insertion can append pages to an existing session and update heat/link metadata; bounded deques, LFU session eviction, knowledge capacity enforcement, and recency heat down-weighting remove or reduce older memory.

### Trace-derived learning

**Trace source:** `session-logs` — The source signal is stored user/assistant conversation pairs with timestamps. In the generation path, MemoryOS also writes its own generated response back into memory, making deployment conversations the continuing trace stream ([memoryos-pypi/memoryos.py](https://github.com/BAI-LAB/MemoryOS/blob/1d717060350931af33d1d0dc3d4e50a72c125a48/memoryos-pypi/memoryos.py)).

**Extraction.** Extraction is staged. First, short-term overflow converts dialogue turns into pages, continuity links, meta summaries, topic summaries, keywords, normalized embeddings, and mid-term sessions. Second, hot mid-term sessions trigger LLM profile analysis and knowledge extraction into user profile text, user private knowledge, and assistant knowledge. The oracle is the configured LLM under authored prompts plus thresholds and capacity policy; no code-grounded reviewer or source-faithfulness check accepts or rejects the generated facts.

**Learning scope:** `cross-task` — A user's profile and knowledge persist across later conversations rather than staying inside one task.

**Learning timing:** `online` — Writes, condensation triggers, heat updates, extraction, retrieval, generation, and write-back happen during normal use; `force_mid_term_analysis()` can manually lower the threshold for testing.

**Distilled form:** `prose` `symbolic` `parametric` — The durable outputs include prose summaries/profiles/facts, symbolic ids/timestamps/session metadata/heat fields, and embeddings or Chroma vectors.

MemoryOS strengthens the trace-learning distinction between raw trace retention and distilled retained artifacts. The same dialogue can remain as a short-term QA pair, become a mid-term page, contribute to a session summary, update a profile, add knowledge entries, produce embeddings, and later enter a prompt.

## Read-back

**Read-back:** `both` — MCP `retrieve_memory` and profile APIs are explicit pull interfaces, while `Memoryos.get_response()` retrieves retained memory and inserts it into prompt messages before the receiving model produces a response.

**Read-back signal:** `coarse` `identifier` `inferred / embedding` — Short-term history and profile context are broadly included for the configured user; user and assistant ids scope which stores are searched; mid-term pages and long-term knowledge are selected by query embeddings and similarity thresholds.

**Faithfulness tested:** `no` — The repository includes demos, LoCoMo evaluation scripts, and keyword-match tests, but the inspected code does not run with/without memory ablations, perturbation checks, or post-answer audits proving that injected memories were used faithfully.

The library generation path is pre-invocation read-back: `get_response()` calls `retrieve_context()`, formats the memory package, sends it to the model, and only then records the new response as a later write. The MCP server is different: it returns retrieved memory to a host agent, so whether that memory becomes push for the receiving model depends on the host's own orchestration.

Selection is bounded by result counts rather than token budget. `Retriever` keeps a heap of top mid-term pages up to `retrieval_queue_capacity`, searches user and assistant knowledge with configurable top-k values, and returns raw dicts for prompt formatting. Effective precision, recall, prompt dilution, and behavioral use are not verifiable from code alone.

## Curiosity Pass

**The ChromaDB path changes durability but not the memory contract.** It replaces JSON-plus-FAISS storage with persistent Chroma collections for vectors and keeps metadata in JSON, but the same trace-to-session-to-profile/fact loop remains.

**Session heat is both retrieval telemetry and learning priority.** Searching mid-term memory increments visit/access fields and recomputes heat, so recall can make a session more likely to be analyzed later. That is useful, but it also couples "retrieved often" with "should update profile/knowledge."

**Long-term lineage weakens at the exact point authority increases.** Mid-term sessions retain source pages; profile and knowledge records are more likely to shape future answers but do not carry source page references or confidence.

**MCP exposes retrieval, not response generation.** The advertised MCP integration can make memory available to clients, but the strongest automatic prompt assembly is in the PyPI/Chroma `get_response()` path, not in the MCP tools themselves.

**The evaluation code tests answer quality, not memory faithfulness.** The LoCoMo and comprehensive test paths check downstream answers and keyword presence, which is useful product evidence, but they do not isolate whether a particular memory record was faithfully used.

## What to Watch

- Whether source-page ids, extraction prompt versions, or confidence fields are added to long-term profile and knowledge records. That would materially improve lineage.
- Whether contradiction handling is implemented for changed user preferences or stale assistant knowledge. That would change the invalidation story.
- Whether MCP grows an automatic prompt-injection wrapper around host model calls. That would make the push side stronger and easier to classify independently of the host.
- Whether profile and knowledge extraction gains validators, human review, or with/without faithfulness tests. That would make automatic personalization safer as behavioral authority.
- Whether the benchmark suite compares memory-enabled and memory-disabled runs at the same prompt boundary. That would make the read-back effect more trustworthy.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - compares: MemoryOS turns conversational traces into session summaries, profile records, knowledge entries, embeddings, and prompt-visible context.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: MemoryOS's raw turns, summaries, profile, knowledge entries, vectors, and prompt packages require separate substrate, form, lineage, and authority labels.
- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: MemoryOS couples storage with a generation path that retrieves memory and assembles context before the model call.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: raw dialogue pages, summaries, profiles, and facts usually serve as evidence or advisory context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: prompt templates, retrieval policy, heat thresholds, and injected assistant knowledge can shape behavior with instruction, ranking, and learning force.
