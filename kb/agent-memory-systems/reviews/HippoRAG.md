---
description: "HippoRAG review: graph-based RAG over corpus documents with OpenIE triples, parquet embedding stores, igraph PageRank retrieval, and pull-only QA"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# HippoRAG

HippoRAG is the OSU NLP Group's Python framework for graph-based retrieval-augmented generation. The reviewed codebase implements HippoRAG 2: it indexes supplied corpus documents into passage, entity, and fact stores, builds an entity/passage graph, uses query-time fact filtering plus personalized PageRank to rank passages, and optionally feeds the selected passages into an LLM QA prompt. Although the README uses long-term-memory language, the implementation is a corpus indexing and retrieval system, not an agent-session memory learner.

**Repository:** https://github.com/OSU-NLP-Group/HippoRAG

**Reviewed commit:** [d437bfb1805278b81e20c82357ed3f7d90f14901](https://github.com/OSU-NLP-Group/HippoRAG/commit/d437bfb1805278b81e20c82357ed3f7d90f14901)

**Last checked:** 2026-06-02

## Core Ideas

**The central retained substrate is an indexed document corpus.** `HippoRAG.index(docs)` inserts the input strings into a chunk embedding store, runs OpenIE for missing chunks, embeds extracted entities and facts, builds graph edges, and saves the graph for later retrieval ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)). The quick start shows the same lifecycle: create a `HippoRAG` object, call `index(docs=docs)`, then call `retrieve` or `rag_qa` on explicit queries ([README.md](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/README.md)).

**OpenIE turns passages into graph candidates, not reviewed knowledge.** The online OpenIE path first prompts for named entities, then prompts for RDF-like triples conditioned on those entities, parses JSON-ish responses, filters malformed triples, and stores passage-level extraction metadata ([src/hipporag/information_extraction/openie_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/information_extraction/openie_openai.py), [src/hipporag/prompts/templates/ner.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/templates/ner.py), [src/hipporag/prompts/templates/triple_extraction.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/templates/triple_extraction.py)). These triples are behavior-shaping because they seed retrieval, but their authority is ranking support, not asserted KB truth.

**The storage layout is local files under `save_dir`.** Each LLM/embedding pair gets a working directory, and the `EmbeddingStore` persists chunk, entity, and fact records as `vdb_<namespace>.parquet` files with hash IDs, content, and embeddings ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/embedding_store.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/embedding_store.py)). OpenIE results are saved as JSON under `save_dir`, the graph is saved as `graph.pickle` in the model-specific working directory, and LLM calls can be cached in SQLite ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py), [src/hipporag/llm/openai_gpt.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/llm/openai_gpt.py)).

**Retrieval combines fact recognition, dense passage scores, and graph propagation.** `retrieve` encodes each query twice, once for fact matching and once for passage matching, scores fact embeddings, asks the reranker to keep relevant candidate triples, and then either runs graph search or falls back to dense passage retrieval when no facts survive ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)). Graph search turns selected fact entities and dense passage scores into reset weights, runs igraph personalized PageRank, and returns top passage texts. This is a strong retrieval policy, but it is still activated by an explicit query.

**The LLM reranker is a query-time system-definition artifact.** `DSPyFilter` loads a saved or default few-shot prompt, asks the LLM to select relevant facts from candidate triples, parses the `fact_after_filter` field, and maps generated selections back to candidate facts ([src/hipporag/rerank.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/rerank.py), [src/hipporag/prompts/filter_default_prompt.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/prompts/filter_default_prompt.py)). The retained prompt demos and instructions have ranking authority; the LLM output itself is not retained as a new memory artifact.

**Context efficiency is top-k retrieval plus QA truncation, not progressive disclosure.** The main controls are `linking_top_k`, `retrieval_top_k`, `passage_node_weight`, `damping`, and `qa_top_k` in `BaseConfig` ([src/hipporag/utils/config_utils.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/utils/config_utils.py)). `qa` feeds only `query_solution.docs[:qa_top_k]` into the answer prompt, while retrieval can rank up to hundreds of passages before that final narrowing ([src/hipporag/HippoRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/HippoRAG.py)). This manages volume, but complexity is hidden inside scores, graph propagation, and reranker behavior rather than exposed as navigable intermediate context.

## Artifact analysis

**Corpus chunks.** The storage substrate is local parquet in `chunk_embeddings/vdb_chunk.parquet`, keyed by MD5-derived chunk IDs. The representational form is mixed: prose passage text plus distributed-parametric embeddings and symbolic hash IDs. Lineage is imported from caller-supplied `docs`; duplicate detection is content-hash based, and regeneration follows `force_index_from_scratch` or changed input text. Behavioral authority is knowledge-artifact authority when chunks are read as evidence, and ranking authority when their embeddings participate in retrieval.

**OpenIE entities and triples.** Entities and facts persist as parquet embedding stores, while the extraction record persists as JSON under `save_dir` when `save_openie` is true. Their representational form is mixed: prose-like extracted strings/triples, symbolic IDs and JSON fields, and embeddings. Lineage is derived from corpus chunks through NER and triple-extraction prompts; a changed passage, extraction prompt, LLM, or force flag invalidates them. Behavioral authority is system-definition artifact authority for retrieval because these extracted facts select graph entry points and PageRank reset weights. They are not promoted into reviewed claims.

**The igraph retrieval graph.** The graph is stored as `graph.pickle` in the model-specific working directory. Its representational form is symbolic weighted graph structure over passage and entity nodes, with weights derived from extracted triples, passage-entity links, and embedding-based synonymy edges. Lineage is compiled from chunk hashes, entity/fact stores, OpenIE output, and graph-construction parameters. Behavioral authority is ranking and routing: it decides which passages are likely to reach the QA context, but it does not by itself instruct the model what to believe.

**Prompt and configuration policy.** Prompt templates, the default DSPy rerank prompt, query embedding instructions, and `BaseConfig` parameters live in source files and optional saved prompt JSON. Their representational form is prose plus symbolic parameters. Lineage is authored code or caller configuration. Behavioral authority is system-definition artifact authority: these artifacts control extraction, fact filtering, graph weighting, retrieval breadth, and QA context size.

**Caches and evaluation outputs.** LLM responses are cached in SQLite, and dataset runs produce outputs under `outputs/` and reproduction directories. These are derived accelerators or experiment artifacts, not canonical memory. They have storage substrate value for reproducibility and cost control, but their behavioral authority is indirect unless a run reuses them for future indexing or inference.

There is no implemented promotion path from retrieved passages or extracted triples into stronger governed artifacts such as validated rules, instructions, schemas, or reviewable notes. The system can add or delete documents through API calls, but that mutates the retrieval substrate rather than promoting learned behavior.

## Comparison with Our System

| Dimension | HippoRAG | Commonplace |
|---|---|---|
| Primary retained artifact | Corpus chunks, OpenIE triples/entities, embeddings, graph pickle, prompts, config | Typed Markdown artifacts, source snapshots, instructions, indexes, schemas, review outputs |
| Storage substrate | Local `outputs/` files: parquet stores, JSON OpenIE results, igraph pickle, SQLite LLM cache | Git-tracked files plus generated indexes and validation/review reports |
| Representational form | Mixed prose, symbolic graph/config, and distributed-parametric embeddings | Mostly prose and symbolic metadata, with validators and generated indexes |
| Lineage | Content hashes, force-rebuild flags, prompt/model/config choices, evaluation scripts | Source citations, frontmatter, collection contracts, git history, replacement archives |
| Read-back | Explicit query-driven retrieval and QA | Agent/user pull through `rg`, indexes, links, skills, and review workflows |
| Authority | Ranking, context selection, and QA prompt assembly | Knowledge artifacts plus stronger system-definition artifacts: instructions, schemas, validators, gates |

HippoRAG is stronger than Commonplace at algorithmic multi-hop retrieval over a large unreviewed corpus. Its graph and PageRank machinery can surface passages whose usefulness depends on entity bridges rather than lexical proximity alone. Commonplace is stronger at governed retention: artifacts carry type, status, source, review, validation, and link semantics, so a future agent can inspect why an artifact has authority and when it should be revised.

The key divergence is what "memory" means. HippoRAG uses memory in the RAG sense: non-parametric retained corpus structure that helps the model answer later questions. Commonplace uses memory as retained artifacts with explicit behavioral authority and lifecycle. HippoRAG's graph can improve recall, but it does not decide that a new method note, instruction, or validator should exist.

HippoRAG's context engineering is efficient but opaque. The system keeps only top-ranked facts and passages moving toward the QA prompt, then truncates to `qa_top_k`. That avoids loading the full corpus, but the agent does not get a progressive map, source-quality state, or authored navigation trail. The ranking stack is useful for retrieval, less useful for an agent that must justify why a remembered artifact should guide a workflow.

Read-back: pull-only - a caller invokes `retrieve`, `retrieve_dpr`, `rag_qa`, or `rag_qa_dpr`; the reviewed repository does not implement a relevance-gated host hook that pushes memories into an agent before action.

### Borrowable Ideas

**Graph propagation as a generated retrieval layer.** Worth borrowing only if Commonplace grows a search layer over notes and sources. The analogue would be a generated graph or embedding index tied back to canonical artifacts, with clear invalidation and no claim of source-of-truth authority.

**Keep extracted facts below authored claims.** Ready as a design rule. HippoRAG's triples are useful for finding passages but too weak to stand as reviewed knowledge. Commonplace should preserve that split for any OpenIE or LLM-extracted relation layer: extraction can route attention before it can govern behavior.

**Expose retrieval budgets as policy, not magic defaults.** HippoRAG's `linking_top_k`, `retrieval_top_k`, and `qa_top_k` make context volume explicit. Commonplace search and review commands should continue making selection budgets visible, especially when generated indexes mediate what an agent sees.

**Use a baseline path beside the graph path.** HippoRAG keeps dense passage retrieval as both a standard RAG baseline and a fallback when fact reranking yields no usable facts. A Commonplace search layer should likewise retain cheap lexical or direct retrieval when graph/ranker signals fail.

**Do not borrow opaque PageRank authority into governance.** PageRank is useful ranking machinery, but it is not a validator, reviewer, or promotion oracle. Commonplace can use such scores to order candidates, but stronger behavioral authority still needs reviewable artifacts and checks.

## Curiosity Pass

**The "memory" label is aspirational from a KB-governance perspective.** The implementation remembers indexed documents and graph structure, but it does not learn from agent sessions, produce durable lessons, or promote retrieval results into system-definition artifacts.

**OpenIE output is both powerful and fragile.** A single extraction error can affect fact embeddings, entity nodes, graph edges, and PageRank seeds. The code filters malformed triples but does not validate extracted claims against source spans or contradiction checks.

**`StandardRAG` contains a debugging breakpoint.** The baseline class imports `ipdb` and calls `ipdb.set_trace()` during initialization, which makes it look unsuitable as a production baseline without patching ([src/hipporag/StandardRAG.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/src/hipporag/StandardRAG.py)). The main HippoRAG path does not depend on that class for the quick-start API.

**The graph is local and inspectable only at the implementation level.** The pickle, parquet stores, and JSON OpenIE results are files, which is good for reproducibility. But the user-facing API returns ranked documents, not a navigable explanation of the path from query facts through graph nodes to passages.

**Incremental updates are content-hash driven.** Tests exercise indexing, reload, incremental additions, and deletion ([tests_openai.py](https://github.com/OSU-NLP-Group/HippoRAG/blob/d437bfb1805278b81e20c82357ed3f7d90f14901/tests_openai.py)). The deletion path removes chunks and some orphaned entities/facts, but the review did not verify graph correctness after complex repeated updates from code alone.

## What to Watch

- Whether future HippoRAG releases expose source-span provenance for triples, because that would make extracted graph facts more reviewable without changing their ranking role.
- Whether retrieval explanations become first-class outputs, especially paths from selected facts to PageRank-weighted passages.
- Whether the project adds agent/session trace ingestion; that would change the trace-derived tag decision only if it produces durable behavior-shaping artifacts from those traces.
- Whether host integrations add pre-action, relevance-gated memory injection; that would change the push-activation decision only if the push path is implemented, not just documented.
- Whether incremental deletion and rebuild logic gets deterministic tests for graph edge cleanup, since stale graph edges would silently affect ranking authority.
- Whether `StandardRAG` is cleaned up as a usable baseline, because baseline quality affects how strongly HippoRAG's graph improvements can be interpreted.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: HippoRAG stores a rich graph and embedding substrate, but future action still depends on explicit query-time retrieval.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: HippoRAG automates extraction and ranking, not governed synthesis, promotion, or durable instruction learning.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved passages and corpus chunks advise later answers as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: extraction prompts, rerank prompts, graph construction, embeddings, and retrieval budgets route and rank later behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - relates: HippoRAG is a context-selection system over an indexed corpus, with top-k and PageRank policies controlling what reaches the QA prompt.
