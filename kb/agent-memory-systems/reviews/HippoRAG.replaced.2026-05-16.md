---
description: "Graph-augmented RAG library that stores document chunks, OpenIE triples, entity/fact embeddings, and an igraph PageRank retrieval graph; strong on associative retrieval, thin on governance and agent memory lifecycle"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: []
status: outdated
last-checked: "2026-04-27"
---

# HippoRAG

> Replaced 2026-05-16. See [HippoRAG](./HippoRAG.md) for the current review.

HippoRAG is OSU NLP Group's Python research library for "long-term memory" as graph-augmented retrieval: documents are embedded, converted by OpenIE into entities and triples, connected into an `igraph` graph, and retrieved through fact scoring, LLM reranking, dense passage scoring, and Personalized PageRank. The repository at https://github.com/OSU-NLP-Group/HippoRAG is an implemented RAG/memory framework for QA over new corpora, not a general agent workspace or self-maintaining knowledge base.

**Repository:** https://github.com/OSU-NLP-Group/HippoRAG

**Reviewed commit:** https://github.com/OSU-NLP-Group/HippoRAG/commit/d437bfb1805278b81e20c82357ed3f7d90f14901

## Core Ideas

**Memory is an indexed corpus graph.** The README frames HippoRAG 2 as a memory framework that improves factual memory, sense-making, and associativity for LLM retrieval. In code, the durable memory substrate is a save directory split by LLM and embedding model; each instance stores passage, entity, and fact embedding tables plus an `igraph` pickle under that model-specific working directory. The core constructor creates `chunk_embeddings`, `entity_embeddings`, and `fact_embeddings` stores, loads or initializes `graph.pickle`, and uses `openie_results_ner_{llm}.json` as the durable extraction cache. See [README.md](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/README.md), [HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), and [embedding_store.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/embedding_store.py).

**OpenIE turns chunks into graph material.** Indexing first inserts raw documents into the chunk embedding store, then runs NER and triple extraction for missing chunks, saves OpenIE results, normalizes triples, embeds entities and facts, and uses the extracted subjects/objects to create entity/entity and passage/entity edges. The OpenAI OpenIE path prompts for named entities, then prompts for triples constrained by those entities; the vLLM offline path batches the same two-stage extraction. This is real transformation from text to structured retrieval artifacts, but the artifact target is still generic OpenIE triples rather than curated claims or instructions. See [openie_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_openai.py) and [openie_vllm_offline.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_vllm_offline.py).

**The graph mixes semantic triples, passage links, and synonymy edges.** `add_fact_edges()` counts symmetric entity/entity edges from extracted triples. `add_passage_edges()` links passage nodes to entities appearing in their triples. `add_synonymy_edges()` performs KNN over entity embeddings and adds high-similarity entity/entity edges above a configured threshold. `augment_graph()` then writes nodes and weighted edges into igraph. The resulting graph is not a knowledge graph with typed predicates preserved as first-class edges; it is a weighted retrieval graph whose topology is induced from facts, passage membership, and embedding-similarity synonymy. See [HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py).

**Retrieval is a four-signal pipeline.** Query-time retrieval embeds the query for facts and passages, scores facts by query/fact embedding similarity, uses `DSPyFilter` to ask an LLM which candidate triples remain relevant, assigns weights to entity nodes from the surviving facts, adds dense passage scores as passage-node weights, and runs Personalized PageRank to rank passages. If reranking leaves no facts, it falls back to dense passage retrieval. This makes "associative memory" a query-time graph diffusion mechanism, not an autonomous memory-writing loop. See [HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py) and [rerank.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/rerank.py).

**Incremental add/delete exists, but lifecycle is mechanical.** `index()` only processes missing chunks unless forced from scratch, and `delete()` removes requested documents from OpenIE JSON, embedding stores, and graph vertices, while preserving triples and entities still supported by undeleted chunks. The OpenAI test exercises reloading an indexed instance, adding new docs, and deleting them. That is useful operational lifecycle for a retrieval index, but not governance: there is no review state, authority model, contradiction handling, provenance beyond stored passages and hashes, or promotion path from retrieved evidence into stronger artifacts. See [tests_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/tests_openai.py).

**Integration is Python-library and experiment-script first.** Packaging exposes `hipporag` as a Python package with heavyweight ML dependencies: PyTorch, Transformers, vLLM, OpenAI, LiteLLM, GritLM, NetworkX, igraph, Pydantic, and boto3. The public surface is constructing `HippoRAG`, calling `index()`, `retrieve()`, and `rag_qa()`, or running dataset scripts over HotpotQA, MuSiQue, and 2WikiMultiHopQA. It supports OpenAI-compatible APIs, Azure, Bedrock, and local vLLM/offline paths, but there is no CLI memory daemon, MCP server, editor integration, or agent-native write/read protocol. See [setup.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/setup.py), [requirements.txt](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/requirements.txt), and [main.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/main.py).

## Comparison with Our System

| Dimension | HippoRAG | Commonplace |
|---|---|---|
| Primary substrate | Parquet embedding tables, OpenIE JSON, igraph pickle, SQLite LLM/embedding caches | Markdown files in git |
| Knowledge unit | Chunk, entity string, extracted triple, weighted graph node/edge | Typed note, source, instruction, ADR, index, or review |
| Construction | Automated OpenIE and embedding-index construction from documents | Human+agent writing, distillation, linking, validation |
| Retrieval | Fact similarity + LLM fact filter + dense passage scores + PPR | `rg`, indexes, descriptions, authored links, semantic reports, explicit reading decisions |
| Memory lifecycle | Add missing chunks; delete chunks and unsupported entities/triples | Status, supersession, review gates, source citations, collection contracts |
| Agent integration | Python API and benchmark scripts | Repo conventions, skills, CLI commands, assistant instructions |
| Governance | Config flags, deterministic hashes, evaluation scripts | Type specs, validation, semantic review, git history, link vocabulary |

**Where HippoRAG is stronger.** It gives a concrete associative retrieval mechanism over a corpus. Commonplace mostly relies on authored links, lexical search, and agent judgment; HippoRAG can derive a graph automatically and use PPR to spread query evidence from facts and passages through related entities. For large QA corpora where the desired behavior is "find the support passages," that is a stronger retrieval algorithm than plain file navigation.

**Where commonplace is stronger.** Commonplace treats memory as maintainable symbolic knowledge. Its artifacts carry roles, status, source links, review state, and relationship semantics; HippoRAG's artifacts are retrieval structures optimized for ranking passages. A HippoRAG triple can improve recall, but it does not explain its authority, relation semantics, lifecycle, contradiction state, or intended downstream use. Commonplace is also agent-native: an agent can read, edit, validate, and promote artifacts using ordinary repository operations. HippoRAG is a library an application calls.

**The deepest divergence is the meaning of "memory."** HippoRAG uses memory to mean non-parametric, persistent, associative access to a corpus. Commonplace uses memory to mean behavior-changing context engineering: durable artifacts that help future agents decide what to load, trust, revise, enforce, or codify. HippoRAG is relevant to the retrieval/activation layer; it has little to say about curation, governance, artifact authority, or long-running agent work.

## Borrowable Ideas

**Graph diffusion as a derived retrieval layer.** A commonplace analogue would keep markdown as source of truth but build a disposable graph over note titles, descriptions, links, extracted entities, and source references, then use PageRank-style expansion when lexical search finds only part of a neighborhood. *Needs a use case first - current navigation failures are more often about authoring and indexing discipline than graph search.*

**Separate fact embeddings from passage embeddings.** HippoRAG embeds triples and passages separately, then combines them only at retrieval time. Commonplace could similarly separate claim-level retrieval handles from note-body retrieval handles, especially for structured claims and source notes. *Ready as an evaluation idea, not an implementation priority.*

**LLM fact filtering before graph traversal.** `DSPyFilter` constrains graph activation by asking an LLM to keep only query-relevant candidate triples. For commonplace, a selector could similarly filter candidate notes or links before expensive expansion. *Needs care - an LLM filter is useful only if its decisions are inspectable or benchmarked.*

**Mechanical delete semantics for derived artifacts.** HippoRAG's delete path preserves triples/entities still supported by undeleted chunks and removes only unsupported derived state. That is a useful pattern for any generated index: removal should be source-support aware, not just file-name aware. *Ready to borrow for generated indexes and reports if deletion becomes a real workflow.*

## Curiosity Pass

**The graph is typed less richly than the extraction output.** OpenIE extracts subject-predicate-object triples, but graph edges are weighted links among entity nodes and passage nodes. The predicate is embedded as a fact string and used for fact scoring/reranking, not preserved as a typed graph relation. That may be the right retrieval tradeoff, but it means HippoRAG is less of a semantic KG system than the terminology suggests.

**"Long-term memory" mostly means persistent retrieval indexes.** The durable artifacts can survive process restarts and incremental updates, but they do not adapt policy, write lessons, summarize experience, or change an agent's operating instructions. Even if retrieval performance is excellent, the memory effect is bounded to better evidence selection for QA.

**The LLM reranker is powerful but hard to govern.** `DSPyFilter` can remove irrelevant facts before graph search, which is important for precision. But it returns no durable judgment record beyond a runtime log dictionary and no confidence beyond `None`. If the filter makes a bad choice, the system has no review surface for learning from that choice.

**The implementation is research-library shaped.** The main HippoRAG path is usable, but adjacent surfaces show research roughness: `StandardRAG` includes an `ipdb.set_trace()` in initialization, and the benchmark scripts carry dataset-specific assumptions. That does not weaken the central algorithm, but it matters if someone evaluates the repo as deployable memory infrastructure.

## What to Watch

- Whether future HippoRAG versions preserve predicates as first-class graph relations or keep using triples mainly as embedded fact strings.
- Whether the project adds provenance, source spans, contradiction handling, or trust scoring for extracted triples.
- Whether associative retrieval is exposed through an agent-native surface such as MCP, a local service, or file-backed derived indexes.
- Whether their benchmarks isolate the marginal value of each signal: dense passages, fact embeddings, LLM fact filtering, synonymy edges, and PPR.
- Whether "continual learning" remains non-parametric corpus indexing or grows into experience-derived lessons, policies, or agent behavior changes.

---

Relevant Notes:

- [knowledge-storage-does-not-imply-contextual-activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: HippoRAG's value is specifically an activation mechanism over stored corpus artifacts, not storage alone.
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: HippoRAG pays indexing and graph-construction cost so query-time context can be smaller and more relevant.
- [distillation](../../notes/definitions/distillation.md) - contrasts: HippoRAG distills documents into OpenIE triples and embeddings for retrieval, while commonplace distillation aims at inspectable behavior-changing artifacts.
- [files-not-database](../../notes/files-not-database.md) - contrasts: HippoRAG's primary substrate is generated tables and graph files, not human-readable source artifacts.
- [agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - contrasts: HippoRAG improves discoverability of support passages but does not supply the composability and trust surfaces expected from an agentic KB.
