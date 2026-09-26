---
type: types/note.md
description: "Mem0’s synchronous OSS memory uses additive extraction and internal context reuse, with separate caller-directed corrections and route-specific retrieval limits."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-26-mem0-02
source-identity: https://github.com/mem0ai/mem0
reviewed-revision: 94c3fe9f238f3dbf29c9ce98643bd71eb13077cd
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-26-mem0-02/result.md
analysis-result-sha256: b4a541c5e6a90e37dbb0115bf9e230c41c5fc635023b519a57c447d4b7ffabd1
---

# Mem0 synchronous OSS memory

Evidence basis: source code, active prompts and the shipped OSS example at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, inspected on 2026-09-26. No live model run or causal comparison was performed.

Mem0’s synchronous Python memory subsystem turns supplied conversation into retained text and makes that text available to later extraction and caller-requested retrieval. Before inferred add, it selects ten existing vector memories and ten recent SQLite messages under the supplied identity scope. It sends both to its extraction model, stores eligible new facts, records history and attempts entity indexing. This internal reuse is wired; an external chat application consuming requested memories is documented and afforded. The enclosing agent remains outside the library boundary. See the [extraction implementation](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L881) and [OSS consumer example](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/README.md#L204).

The active inferred-write path only adds memories, despite an API docstring that also promises automatic update/delete decisions. Existing text helps extraction avoid duplicates and resolve references. Explicit caller-directed update and delete provide replacement and withdrawal. The procedural branch separately summarizes supplied agent execution history into an ordinary searchable text memory; it does not install an executable skill. Both derived forms can become later extraction context. See the [active additive prompt](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/configs/prompts.py#L468) and [procedural creation](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L2007).

The retained objects have distinct roles: Qdrant holds text and access representations; SQLite history records old/new values and mutation events; a separate SQLite window supplies recent conversational context; entity records supply linked-ID ranking boosts. Automatic context selection uses identity matching and embeddings. Public search additionally uses conditional lexical/entity scoring over a bounded semantic candidate pool. It does not add lexical-only hits missing from that pool. The prompt requests related-memory links, but the write path does not retain those model-produced links; entity associations are computed separately. The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-26-mem0-02/result.md) retains the supporting objects, routes, quotations and per-value evidence.

Maintenance has local limits. Expiration hides records from public search/list by default, while direct get and internal extraction retrieval can still receive them. Identity fields resist reassignment through metadata, but memory text remains editable and identifier-only operations do not establish deployed authorization. Raw and procedural creation bypass recent-message saving and initial entity indexing. Primary writes, history and index maintenance do not share a transaction; secondary failures or an uninitialized entity store can leave incomplete maintenance. These are source-visible possibilities, not observed corruption.

The implementation supports automatic trace-derived memory with subsequent reuse. Default procedural guidance affords per-task continuation, while the task horizon of ordinary extraction and custom prompts remains undetermined. The comparison therefore keeps task scope partial. No retained execution tests dependence on recalled content, so recall faithfulness is not determinable here. Structural admission, similarity and storage establish operational eligibility, not factual acceptance. A method-criticism-and-revision loop and improved capacity caused by that criticism are not established.

## Scope

This review covers synchronous textual `Memory` operations with default Qdrant/OpenAI adapters, SQLite, and conditional NLP/BM25 support. AsyncMemory, other providers, optional reranker internals, vision, server/cloud implementation, other integrations, evaluation packages and enclosing agents are excluded. Provider internals and exact model parameters remain uninspected. Results cannot establish whole-product completeness, deployment isolation, faithful extraction, answer activation or measured benefit.
