---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Agentic Local Brain memory comparison of retained knowledge, derived representations, conversational context, access history, caches and archives at the frozen revision."
run-id: "AAS-2026-10-12-agentic-local-brain-f00cbd577178-01"
source-identity: "https://github.com/agent-creativity/agentic-local-brain"
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
memory-comparison:
  version: 2
  scope: "Includes collected document/metadata/chunk parts, mined entities/document vectors/relations/topics, topic wiki products and unresolved entity-card alternatives, conversation turns, reading events, retained results/confidence, mining status/history, local archives and their later consumers. Includes unresolved collector/maintenance/API alternatives and opaque provider accumulated state as coverage limits. Excludes static shipped prompts/configuration, code/install artifacts, development-agent/Trellis memory and external host state; does not substitute opaque provider model components for inspected accumulated memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Collected document files and knowledge metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-knowledge"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Chunk text, IDs and dense search vectors"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-chunks"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Entities, mentions and entity relations"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entities"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-entities"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Document embedding payloads and keys"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-embeddings"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-document-embeddings"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Cross-document relation rows"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-relations"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-document-relations"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Topic memberships, labels and centroids"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-topic-clusters"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Wiki article files and category/article metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "RAG sessions, turns and source dictionaries"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-conversations"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-rag-conversations"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Reading/search/RAG event rows"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reading-history"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "memory.md#mem-obj-reading-history"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Enhanced result cache including confidence"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "runtime.md#rt-rte-chat-query"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Mining progress and JSONL history"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "runtime.md#rt-rte-mining-run"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Locally retained backup archives and listing metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-backup-restore"
              note: "The recorded retained part uses this substrate; encoding is classified separately."
          records:
            - "runtime.md#rt-rte-backup-restore"
          note: "The cited record identifies this storage part and its retained read/write route."
        - scope: "Opaque generation, expansion, reranking and embedding provider state"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Calling records identify remote weights/services but not an inspected use-accumulated provider memory inventory. No model-weights or service-object finding is inferred for opaque accumulated state."
        - scope: "Untraced alternative collectors, entity-card production, tag/export and exposed API retention paths"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-rte-note-admission"
          note: "Accepted records leave alternative writers and active callers incompletely inspected; local positives do not enumerate their retained parts."
      records:
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-document-embeddings"
        - "memory.md#mem-obj-document-relations"
        - "memory.md#mem-obj-topic-clusters"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-reading-history"
        - "runtime.md#rt-rte-chat-query"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
        - "memory.md#mem-rte-note-admission"
      note: "Files, SQLite, vector storage and process-local retained state have wired witnesses. Remote accumulated state and untraced alternatives prevent complete coverage; source code and shipped prompt strings are not counted as memory substrates."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Document body, summary and user-note text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-knowledge"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Chunk text delivered to answers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-chunks"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Entity names, descriptions and source contexts"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entities"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-entities"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Topic labels and descriptions"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-topic-clusters"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Stored wiki prose and category descriptions"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Conversation question and assistant-answer text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-conversations"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-rag-conversations"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Recorded history query text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reading-history"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "memory.md#mem-obj-reading-history"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Cached answer/context prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
              note: "Text is interpreted as language by the recorded model or human consumer."
          records:
            - "runtime.md#rt-rte-chat-query"
          note: "This unit excludes adjacent IDs, timestamps and numerical payloads."
        - scope: "Knowledge IDs, paths, hashes, types and tag associations"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-knowledge"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Chunk IDs, indices and embedding references"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-chunks"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Entity types, endpoints, source IDs and counters"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entities"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-entities"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Document-vector keys and timestamps"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-embeddings"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-document-embeddings"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Relation endpoints, types, scores and shared-entity IDs"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-relations"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-document-relations"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Topic memberships and confidence fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-topic-clusters"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Wiki source/category/article IDs, versions and paths"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Conversation session, role, order and source dictionaries"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-conversations"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-rag-conversations"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Event action/time and knowledge IDs"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reading-history"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "memory.md#mem-obj-reading-history"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Cached confidence field"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-answer-confidence"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "epistemic.md#epi-obj-answer-confidence"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Mining progress/history status fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
              note: "Localized fields are consumed by fixed lookup, ordering, arithmetic or display rules."
          records:
            - "runtime.md#rt-rte-mining-run"
          note: "Numerical scores with localized arithmetic meaning are symbolic, not dense representations."
        - scope: "Chroma dense chunk embeddings"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
              note: "Dense numerical state distributes representation across vector dimensions."
          records:
            - "memory.md#mem-obj-chunks"
          note: "Serialization does not change dense representation into symbolic prose or model weights."
        - scope: "SQLite dense document embeddings in JSON or packed-byte encoding"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-embeddings"
              note: "Dense numerical state distributes representation across vector dimensions."
          records:
            - "memory.md#mem-obj-document-embeddings"
          note: "Serialization does not change dense representation into symbolic prose or model weights."
        - scope: "Retained topic centroids"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
              note: "Dense numerical state distributes representation across vector dimensions."
          records:
            - "memory.md#mem-obj-topic-clusters"
          note: "Serialization does not change dense representation into symbolic prose or model weights."
        - scope: "Archive payloads beyond their file container"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-backup-restore"
          note: "The archive walk records retention but does not enumerate every operative payload form."
        - scope: "Opaque provider accumulated payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Parametric model components are recorded, but opaque provider-side accumulated memory is not individuated or inspected."
        - scope: "Entity-card content and remaining collector/maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-knowledge"
          note: "Display and schema information do not resolve every alternative consumed payload."
      records:
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-topic-clusters"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-reading-history"
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-obj-document-embeddings"
        - "memory.md#mem-obj-document-relations"
        - "epistemic.md#epi-obj-answer-confidence"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Inspected mixed objects are split into text, fixed-rule fields and dense representations. Unknown archive/provider/alternative payloads prevent a complete inventory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Collected source body admitted through file and host-assisted acquisition"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
                - "runtime.md#rt-rte-file-admission"
              note: "Previously external source material enters retained local files."
          records:
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-rte-file-admission"
          note: "The path is known; original source authorship/authentication remains unresolved."
        - scope: "Generated summaries, tags, chunks, embeddings and mined entities/relations"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-file-admission"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-document-embeddings"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-document-relations"
              note: "Application transformations derive retained representations from collected material."
          records:
            - "runtime.md#rt-rte-file-admission"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-document-embeddings"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-document-relations"
          note: "Derivation is distinct from source acquisition and provider-weight provenance."
        - scope: "Topic memberships, centroids and generated labels"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
                - "epistemic.md#epi-rte-numeric-selection"
              note: "Mining derives topic state from document representations."
          records:
            - "memory.md#mem-obj-topic-clusters"
            - "epistemic.md#epi-rte-numeric-selection"
          note: "The recorded path is derivation, not conversational extraction; full label-provider details remain outside this unit."
        - scope: "Generated wiki article text and category metadata"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "runtime.md#rt-rte-wiki-compile"
              note: "A model proposes new article prose and organizational descriptions."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "runtime.md#rt-rte-wiki-compile"
              note: "The compiler generates, parses and renders a retained product from selected documents/entities."
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "runtime.md#rt-rte-wiki-compile"
          note: "These describe different stages of the recorded topic-article derivation, not proof of semantic novelty."
        - scope: "Automatically retained conversation turns and event rows"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-conversations"
                - "memory.md#mem-obj-reading-history"
                - "runtime.md#rt-rte-chat-query"
              note: "Interaction content and access activity are recorded as durable turns/events."
          records:
            - "memory.md#mem-obj-rag-conversations"
            - "memory.md#mem-obj-reading-history"
            - "runtime.md#rt-rte-chat-query"
          note: "This describes recording lineage and does not alone assert trace learning."
        - scope: "Generated assistant answer content retained in conversations/cache"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "The answer model proposes prose."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "Generated answers use selected retained context and, on applicable calls, previous turn text."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
          note: "Automatic generation/admission is distinct from authorship and factual acceptance."
        - scope: "Cached confidence metadata"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-answer-confidence"
                - "epistemic.md#epi-rte-confidence-metadata"
              note: "Fixed arithmetic compiles retrieval scores, source count and stage labels."
          records:
            - "epistemic.md#epi-obj-answer-confidence"
            - "epistemic.md#epi-rte-confidence-metadata"
          note: "No answer assertion enters the formula."
        - scope: "Mining history and archive copy paths"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
                - "runtime.md#rt-rte-backup-restore"
              note: "Mining history records maintenance activity."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
                - "runtime.md#rt-rte-backup-restore"
              note: "Backup archives mechanically package retained filesystem material."
          records:
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
          note: "Activity recording and mechanical archive compilation have separate local warrants."
        - scope: "Initial direct-note content, metadata-edit content and source-specific provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-note-admission"
            - "runtime.md#rt-rte-item-update"
            - "memory.md#mem-obj-knowledge"
          note: "Generic callers and manual_input labels do not establish human authorship or all original derivation paths."
        - scope: "Entity-card derivation, complete topic-label generation and opaque provider memory lineage"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-topic-clusters"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Topic-article derivation does not resolve the entity-card alternative or inaccessible provider provenance."
      records:
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-file-admission"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-document-embeddings"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-document-relations"
        - "memory.md#mem-obj-topic-clusters"
        - "epistemic.md#epi-rte-numeric-selection"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-rte-wiki-compile"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-reading-history"
        - "runtime.md#rt-rte-chat-query"
        - "epistemic.md#epi-obj-answer-confidence"
        - "epistemic.md#epi-rte-confidence-metadata"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-rte-note-admission"
        - "runtime.md#rt-rte-item-update"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Imported, authored, compiled and activity-recorded paths coexist. Initial content authorship, some alternative derivations and opaque provider provenance remain unresolved."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Document/chunk/entity/topic text and prior turns at expansion/answer models; articles at wiki readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-retained-context"
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-topic-clusters"
                - "memory.md#mem-obj-rag-conversations"
                - "memory.md#mem-obj-wiki-articles"
              note: "Selected language supplies context/reference rather than a truth oracle."
          records:
            - "memory.md#mem-bap-retained-context"
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-topic-clusters"
            - "memory.md#mem-obj-rag-conversations"
            - "memory.md#mem-obj-wiki-articles"
          note: "Knowledge authority names delivery for interpretation, not observed obedience or correctness."
        - scope: "Retained text and dense embeddings at lexical/semantic retrieval; topic/graph associations at selection"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-document-embeddings"
                - "memory.md#mem-obj-document-relations"
                - "memory.md#mem-obj-topic-clusters"
                - "runtime.md#rt-rte-chat-query"
                - "epistemic.md#epi-rte-numeric-selection"
              note: "Text matching, vector similarity and retained associations influence relative candidate priority."
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-document-embeddings"
            - "memory.md#mem-obj-document-relations"
            - "memory.md#mem-obj-topic-clusters"
            - "runtime.md#rt-rte-chat-query"
            - "epistemic.md#epi-rte-numeric-selection"
          note: "Ranking influence does not imply learned scoring policy or calibrated relevance."
        - scope: "Retained reading-event IDs/times and associated vectors/topics at recommendation/enrichment"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-selection"
                - "memory.md#mem-bap-event-selection"
              note: "Time-weighted vectors, topic bonuses and conditional recent-view boosts change candidate scores."
          records:
            - "memory.md#mem-rte-history-selection"
            - "memory.md#mem-bap-event-selection"
          note: "Transient user_profile is a consumer result, not an additional retained object."
        - scope: "Article source-ID/category state at recompilation selection"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "epistemic.md#epi-rte-category-recompilation"
              note: "Prior compiled IDs compared with current IDs select compilation work."
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "epistemic.md#epi-rte-category-recompilation"
          note: "This selects work, not factual acceptance or a universal freshness check."
        - scope: "Session/order fields at history loading; cache keys/TTL at result reuse"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-rag-conversations"
                - "runtime.md#rt-rte-chat-query"
              note: "Retained identity/order or cache state selects which history/result is reused."
          records:
            - "memory.md#mem-obj-rag-conversations"
            - "runtime.md#rt-rte-chat-query"
          note: "Actual deployed reuse remains unobserved."
        - scope: "Retained topic centroids at subsequent document classification"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-topic-clusters"
                - "epistemic.md#epi-rte-numeric-selection"
              note: "Nearest retained centroid selects a topic assignment."
          records:
            - "memory.md#mem-obj-topic-clusters"
            - "epistemic.md#epi-rte-numeric-selection"
          note: "Classification updates and future use are wired, not demonstrated improved capacity."
        - scope: "Conversation experience at answer generation producing later-retained assistant turns"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
                - "memory.md#mem-bap-retained-context"
              note: "Prior conversation text feeds generation of durable answer text that later supplies context."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
            - "memory.md#mem-bap-retained-context"
          note: "This is the durable behavior-shaping artifact update path; downstream turns separately have knowledge authority. No parameter update or improvement is asserted."
        - scope: "Cached confidence and mining-history status at API/display consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-answer-confidence"
                - "runtime.md#rt-rte-mining-run"
              note: "Retained results/status supply advisory information to later callers."
          records:
            - "epistemic.md#epi-obj-answer-confidence"
            - "runtime.md#rt-rte-mining-run"
          note: "Confidence is advisory arithmetic metadata, not answer-truth probability or a veto."
        - scope: "Unconsumed user_notes, saved source dictionaries, archive payloads and remaining graph/topic consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-rag-conversations"
            - "runtime.md#rt-rte-backup-restore"
            - "memory.md#mem-obj-document-relations"
            - "memory.md#mem-obj-topic-clusters"
          note: "Storage or display alone cannot establish every behavioral force or downstream consumer."
        - scope: "Entity-card and opaque provider accumulated-memory consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Actual alternative consumption and effects are not recorded completely."
      records:
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-topic-clusters"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-document-embeddings"
        - "memory.md#mem-obj-document-relations"
        - "runtime.md#rt-rte-chat-query"
        - "epistemic.md#epi-rte-numeric-selection"
        - "memory.md#mem-rte-history-selection"
        - "memory.md#mem-bap-event-selection"
        - "epistemic.md#epi-rte-category-recompilation"
        - "epistemic.md#epi-obj-answer-confidence"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Knowledge, ranking, routing and a conversation-to-durable-answer learning path are locally supported. Static prompts/configuration and fixed program checks are excluded; no retained criterion is classified as instruction, validation or enforcement merely because code checks or deletes a row."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Missing metadata extraction and chunk/index admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-file-admission"
                - "memory.md#mem-rte-note-admission"
              note: "Software admits generated fields and indices without per-result human approval."
          records:
            - "runtime.md#rt-rte-file-admission"
            - "memory.md#mem-rte-note-admission"
          note: "The initiating caller may select inputs/flags; this does not make generated admission manual."
        - scope: "Mining entities/vectors/relations/topics and topic-article compilation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
                - "runtime.md#rt-rte-wiki-compile"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-document-embeddings"
                - "memory.md#mem-obj-document-relations"
                - "memory.md#mem-obj-topic-clusters"
              note: "Models/algorithms propose and software persists stage products without per-content approval."
          records:
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-wiki-compile"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-document-embeddings"
            - "memory.md#mem-obj-document-relations"
            - "memory.md#mem-obj-topic-clusters"
          note: "The web full-mode confirmation is not review of each output."
        - scope: "Conversation turn/cache and reading-event admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
                - "memory.md#mem-obj-reading-history"
                - "memory.md#mem-rte-history-selection"
              note: "Application records questions/answers/events or caches results on applicable paths."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
            - "memory.md#mem-obj-reading-history"
            - "memory.md#mem-rte-history-selection"
          note: "Cache hits, empty retrieval and save failures bound activation, not admission agency."
        - scope: "Topic centroid revision and title-cleanup admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-numeric-selection"
                - "epistemic.md#epi-rte-title-cleanup"
              note: "Software changes centroids or chooses title-group deletions without per-entry approval."
          records:
            - "epistemic.md#epi-rte-numeric-selection"
            - "epistemic.md#epi-rte-title-cleanup"
          note: "Starting maintenance is not manual admission of each resulting change."
        - scope: "Mining history and scheduled/archive packaging writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mining-run"
                - "runtime.md#rt-rte-backup-restore"
              note: "Program mechanically records progress/history and packages retained files."
          records:
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
          note: "Backup scheduling/selection is separate from subsequent archive admission."
        - scope: "Operator adoption of extracted backup material"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-backup-restore"
              note: "The restore route requires the operator to decide on placement/replacement of live state."
          records:
            - "runtime.md#rt-rte-backup-restore"
          note: "Manual adoption is distinct from automatic extraction; successful adoption is unobserved."
        - scope: "Initial file/note content, supplied metadata overrides, HTTP edits and requested withdrawal"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-file-admission"
            - "memory.md#mem-rte-note-admission"
            - "runtime.md#rt-rte-item-update"
            - "memory.md#mem-rte-item-withdrawal"
          note: "Generic CLI/HTTP caller identity does not establish an explicit human per-content decision; manual_input is only a source label."
        - scope: "Untraced collectors, entity-card, tag/export/reset and expiry admission mechanisms"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-wiki-articles"
            - "runtime.md#rt-rte-chat-query"
          note: "Inspected admission witnesses do not resolve all included alternatives."
        - scope: "Provider accumulated-memory admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "No accessible provider-side admission control is established."
      records:
        - "runtime.md#rt-rte-file-admission"
        - "memory.md#mem-rte-note-admission"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-wiki-compile"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-document-embeddings"
        - "memory.md#mem-obj-document-relations"
        - "memory.md#mem-obj-topic-clusters"
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-reading-history"
        - "memory.md#mem-rte-history-selection"
        - "epistemic.md#epi-rte-numeric-selection"
        - "epistemic.md#epi-rte-title-cleanup"
        - "runtime.md#rt-rte-backup-restore"
        - "runtime.md#rt-rte-item-update"
        - "memory.md#mem-rte-item-withdrawal"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Known software admission remains automatic regardless of workflow initiation. Manual backup adoption has its own operator decision. Generic caller identity and alternative/provider admissions remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Built-in summary selection over retained collected text"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-extractive-summary"
                - "runtime.md#rt-rte-file-admission"
              note: "Sentence selection/compression reduces existing source claims into metadata."
          records:
            - "epistemic.md#epi-rte-extractive-summary"
            - "runtime.md#rt-rte-file-admission"
          note: "Omission/truncation risks do not turn consolidation into synthesis."
        - scope: "Model summary/tag extraction and wiki merge request"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-file-admission"
                - "runtime.md#rt-rte-wiki-compile"
              note: "The generation guidance requests summaries and natural merging of retained source claims."
          records:
            - "runtime.md#rt-rte-file-admission"
            - "runtime.md#rt-rte-wiki-compile"
            - "epistemic.md#epi-rte-structural-checks"
          note: "Requested consolidation is supported at the guidance layer; semantic transformation of unknown generated outputs is indeterminate, so no wired synthesis or faithful consolidation is inferred."
        - scope: "Topic centroid/membership updates"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-numeric-selection"
                - "memory.md#mem-obj-topic-clusters"
              note: "Incremental assignment revises the retained centroid used by later classifications."
          records:
            - "epistemic.md#epi-rte-numeric-selection"
            - "memory.md#mem-obj-topic-clusters"
          note: "Running-average revision is implemented; this does not establish new truth-apt claims."
        - scope: "Recompiled topic article replacement/versioned metadata"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-compile"
                - "memory.md#mem-obj-wiki-articles"
                - "epistemic.md#epi-rte-category-recompilation"
              note: "Recompilation changes the retained article product under existing guidance."
          records:
            - "runtime.md#rt-rte-wiki-compile"
            - "memory.md#mem-obj-wiki-articles"
            - "epistemic.md#epi-rte-category-recompilation"
          note: "Same-ID text edits can miss the selector; source associations are not a criticism history."
        - scope: "Exact-title duplicate cleanup of retained webpage rows"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-title-cleanup"
              note: "Software retains the first same-title row and removes later ones within its bounded listing."
          records:
            - "epistemic.md#epi-rte-title-cleanup"
          note: "Operational duplicate criterion is title equality, not semantic equivalence; SQLite-only effects remain local."
        - scope: "Reading-history influence downweighting"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-selection"
                - "epistemic.md#epi-rte-history-recommendation"
              note: "Event age exponentially downweights its contribution to the recomputed preference proxy."
          records:
            - "memory.md#mem-rte-history-selection"
            - "epistemic.md#epi-rte-history-recommendation"
          note: "Raw events remain durable; the downweighting operates at their later scoring consumer."
        - scope: "Process-local retained result-cache expiry"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
              note: "TTL forgets cached results after their local lifetime."
          records:
            - "runtime.md#rt-rte-chat-query"
          note: "This is bounded cache forgetting, not document retention expiry."
        - scope: "HTTP withdrawal, conversation deletion/expiry, tag/export/reset and archive cleanup beyond inspected effects"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-item-withdrawal"
            - "runtime.md#rt-rte-chat-query"
            - "runtime.md#rt-rte-backup-restore"
            - "memory.md#mem-obj-knowledge"
          note: "Removal is recorded but history-retaining invalidation and all curation semantics are not established; physical deletion alone is not invalidate."
        - scope: "Entity-card synthesis, complete topic-label revisions and provider curation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-topic-clusters"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Generated labels/article output semantics and inaccessible provider transformations prevent complete controlled-operation classification."
      records:
        - "epistemic.md#epi-rte-extractive-summary"
        - "runtime.md#rt-rte-file-admission"
        - "runtime.md#rt-rte-wiki-compile"
        - "epistemic.md#epi-rte-structural-checks"
        - "epistemic.md#epi-rte-numeric-selection"
        - "memory.md#mem-obj-topic-clusters"
        - "memory.md#mem-obj-wiki-articles"
        - "epistemic.md#epi-rte-category-recompilation"
        - "epistemic.md#epi-rte-title-cleanup"
        - "memory.md#mem-rte-history-selection"
        - "epistemic.md#epi-rte-history-recommendation"
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-rte-item-withdrawal"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Consolidation guidance and deterministic compression, durable revision, bounded deduplication and downweighting/expiry are separate operations with separate bases. Generation named synthesis does not establish a novel claim; index rebuild or primary-key checks alone add no operation."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested knowledge retrieval: keyword/semantic, legacy/enhanced answering and mining input reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-file-admission"
                - "runtime.md#rt-rte-chat-query"
                - "runtime.md#rt-rte-legacy-query"
                - "runtime.md#rt-rte-mining-run"
              note: "The consumer requests retained knowledge/source material; internal selection fulfills that request."
          records:
            - "runtime.md#rt-rte-file-admission"
            - "runtime.md#rt-rte-chat-query"
            - "runtime.md#rt-rte-legacy-query"
            - "runtime.md#rt-rte-mining-run"
          note: "Requested delivery is not another push solely because selection/delivery is automatic."
        - scope: "Wiki article browsing, recommendation request, history/status and backup selection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-compile"
                - "memory.md#mem-rte-history-selection"
                - "runtime.md#rt-rte-mining-run"
                - "runtime.md#rt-rte-backup-restore"
              note: "Explicit requests select articles, recommendations, history/status or archives."
          records:
            - "runtime.md#rt-rte-wiki-compile"
            - "memory.md#mem-rte-history-selection"
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
          note: "Identifier-based GET and requested archive selection are addressing, not targeted push."
        - scope: "Automatic session-history supply to expansion/answer generation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "On a session query, the application loads and supplies prior turn text without a separate request for those retained turns."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
          note: "The outer question is requested; automatic contextual supply is a distinct operation within that chain, not a second push for the final answer return."
        - scope: "Automatic recent-view supply to enhanced-query enrichment"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-selection"
                - "runtime.md#rt-rte-chat-query"
              note: "Enrichment reads recent-view events and supplies their score influence inside an enabled query."
          records:
            - "memory.md#mem-rte-history-selection"
            - "runtime.md#rt-rte-chat-query"
          note: "The caller requests an answer, not those particular event records. Recommendation-list return itself remains pull."
        - scope: "Cache reuse fulfilling repeated single-turn query"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
              note: "A matching repeated query returns its cached result."
          records:
            - "runtime.md#rt-rte-chat-query"
          note: "Cache delivery fulfills the question request; no unsolicited delivery is inferred."
        - scope: "Entity-card, other API/maintenance consumers and provider-side delivery"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Untraced consumers/alternatives prevent an exhaustive request-versus-supply inventory."
      records:
        - "runtime.md#rt-rte-file-admission"
        - "runtime.md#rt-rte-chat-query"
        - "runtime.md#rt-rte-legacy-query"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-wiki-compile"
        - "memory.md#mem-rte-history-selection"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Both requested reads and automatic context supply occur within request chains. The absence of an independent unsolicited scheduler does not eliminate push operations inside those chains. Unknown alternatives prevent complete coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Session-history push: current query with session identity, recent-turn selector, formatted prior content"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "Session identity matches retained session turns to be supplied to expansion/answer models."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "Recent-turn count and 4000-character truncation filter the matched history by availability/order/budget."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
          note: "Identity selection and coarse truncation are separate operations; saved source dictionaries are not delivered history text."
        - scope: "Recent-view push to enrichment: enabled query, latest-view selector, event IDs supplying score inputs"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-selection"
              note: "The selector loads 20 recent views rather than semantically matching query meaning."
          records:
            - "memory.md#mem-rte-history-selection"
          note: "Matching chunk.source to viewed IDs conditionally boosts scores, but does not independently establish identity-selected delivered chunks; no identifier push finding is added for that boost."
        - scope: "Requested knowledge/wiki/recommendation/cache/status/archive returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-chat-query"
            - "runtime.md#rt-rte-wiki-compile"
            - "memory.md#mem-rte-history-selection"
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
          note: "These operations are pull; push-signal classification is inapplicable locally, not for the mixed overall boundary."
        - scope: "Alternative and provider-side push selection"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Trigger, selector inputs and selected retained parts remain uninspected for included opaque alternatives."
      records:
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-rte-history-selection"
        - "runtime.md#rt-rte-wiki-compile"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Session identity and coarse contextual selection support push findings. Semantic, lexical and model judgment used to fulfill requested retrieval are not automatically additional push signals. Unknown alternatives prevent complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic assistant-turn production/admission from conversational question/history to later model context"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
                - "memory.md#mem-bap-retained-context"
              note: "Recorded conversational input feeds answer generation; successful assistant-turn writes are durable and selected turn text reaches later expansion/answer calls."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
            - "memory.md#mem-bap-retained-context"
          note: "This qualifies as trace-fed durable behavior-shaping text, not merely keeping raw logs. No authored continuation summary, parameter training, activation or improved capacity is required or asserted."
        - scope: "Reading events to ephemeral recommendation profile/score boost"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reading-history"
            - "memory.md#mem-rte-history-selection"
          note: "The profile/reasons are recomputed, not durably written. Raw event persistence alone does not establish a qualifying derived update; no bounded absence record warrants a local no."
        - scope: "Mining-history status and archive routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
          note: "Status logging/archive copies do not establish durable trace-derived behavioral updates; absence of such updates is not a supplied bounded absence."
        - scope: "Collected documents, summary/mining/wiki routes with unresolved original trace content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-rte-file-admission"
            - "memory.md#mem-rte-note-admission"
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-wiki-compile"
          note: "Original inputs may include traces, but accepted records do not identify qualifying trace origins for these content routes."
        - scope: "Entity-card, remaining maintenance/collector and opaque provider trace-fed writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-topic-clusters"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "No complete inspection of these update/consumer chains is recorded."
      records:
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-reading-history"
        - "memory.md#mem-rte-history-selection"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-file-admission"
        - "memory.md#mem-rte-note-admission"
        - "runtime.md#rt-rte-wiki-compile"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-topic-clusters"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "A wired conversational-input to durable assistant-text to later-context route supports yes. Other raw logging, transient selection and opaque input routes remain unresolved, not system-wide no. This axis is not a claim of improved capacity."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Qualifying durable assistant-turn update from recorded conversational turns"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-query"
                - "memory.md#mem-obj-rag-conversations"
              note: "Prior user/assistant turn content is recorded conversation from earlier RAG work sessions and is used in later answer production."
          records:
            - "runtime.md#rt-rte-chat-query"
            - "memory.md#mem-obj-rag-conversations"
          note: "Classification follows conversational origin, not role labels or SQLite encoding; current user question is additional conversational input."
        - scope: "Mixed non-conversational answer context and other content-update trace origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-topic-clusters"
            - "runtime.md#rt-rte-chat-query"
          note: "Selected documents/entities/topics accompany session input, but original content origins are not fully recorded; additional event/tool/trajectory source values cannot be inferred."
        - scope: "Event-history routes without established durable derived update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reading-history"
            - "memory.md#mem-rte-history-selection"
          note: "Views/search actions are activity events, but no qualifying durable profile update is established; event-streams is not assigned from raw event storage alone."
        - scope: "Mining-history/archive, alternative content paths and opaque provider learning inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mining-run"
            - "runtime.md#rt-rte-backup-restore"
            - "memory.md#mem-obj-wiki-articles"
            - "runtime.md#rt-cmp-litellm-provider"
            - "runtime.md#rt-cmp-query-expander"
            - "runtime.md#rt-cmp-llm-reranker"
            - "runtime.md#rt-cmp-embedding-provider"
          note: "Trace-learning coverage is unresolved on these routes, so their trace_source cannot be declared inapplicable from another route or inferred from journal/status serialization."
      records:
        - "runtime.md#rt-rte-chat-query"
        - "memory.md#mem-obj-rag-conversations"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-topic-clusters"
        - "memory.md#mem-obj-reading-history"
        - "memory.md#mem-rte-history-selection"
        - "runtime.md#rt-rte-mining-run"
        - "runtime.md#rt-rte-backup-restore"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-cmp-litellm-provider"
        - "runtime.md#rt-cmp-query-expander"
        - "runtime.md#rt-cmp-llm-reranker"
        - "runtime.md#rt-cmp-embedding-provider"
      note: "Session-log content is supported on the qualifying conversational update. Mixed context origins and unresolved qualifying routes keep this axis partial; raw events/status alone establish no additional trace source."
---

# Agentic Local Brain memory profile

## Comparison rationale

The inventory follows retained parts and their later consumers, not the whole application's capability surface. Every finding is architectural wiring or explicitly labelled guidance, never observed deployment or causal benefit. The units preserve unknown remote/provider state and untraced alternatives rather than extending one inspected route to every caller.

Dense document vectors remain parametric representations even when serialized as JSON or packed float bytes in SQLite. Localized scores, IDs and membership fields are symbolic. Chunk vector storage uses the vector substrate; SQLite dense-vector rows do not become a separate vector database merely because they encode vectors. See [MEM-OBJ-chunks](memory.md#mem-obj-chunks), [MEM-OBJ-document-embeddings](memory.md#mem-obj-document-embeddings) and [MEM-OBJ-topic-clusters](memory.md#mem-obj-topic-clusters). Provider calling records do not identify provider-side accumulated memory, despite naming model components and service roles.

The imported document body, compiled representations and authored model text have different derivation stages. Generic caller identity cannot establish human authorship or manual admission. Generated missing metadata, mined products and conversation turns have automatic software admission; archive adoption separately requires an operator's replacement decision. See [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-item-update](runtime.md#rt-rte-item-update), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore) and [MEM-RTE-note-admission](memory.md#mem-rte-note-admission).

Requested knowledge/recommendation/article returns are pull. Inside an answer request, loading session-matched prior turns and automatically supplying recent-view influence are separate contextual push operations. No unsolicited scheduler is required for this distinction. The prior-turn push uses an actual session match and then coarse turn/budget filtering. Recent-view enrichment uses coarse event selection; its conditional ID-based score boost is not independently established as identity-selected delivery of chunks. These mappings use [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [MEM-OBJ-rag-conversations](memory.md#mem-obj-rag-conversations) and [MEM-RTE-history-selection](memory.md#mem-rte-history-selection), without turning every automatic retrieval selector into push.

The conversation chain supports a wired trace-learning witness: recorded turns enter generation, assistant prose is automatically retained on applicable paths, and later invocations receive selected prior text. The original trace source is conversational session content. This does not assert a continuation-summary mechanism, model training or improved capacity. Merely storing raw reading events does not close the same derived-artifact chain: the recommendation profile is transient. Consequently those units remain unresolved rather than supplying a system-wide negative. See [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [MEM-OBJ-rag-conversations](memory.md#mem-obj-rag-conversations), [MEM-BAP-retained-context](memory.md#mem-bap-retained-context) and [MEM-RTE-history-selection](memory.md#mem-rte-history-selection).

Consolidation has a deterministic sentence-selection witness and a separate model-guidance finding. Wiki wording requesting synthesis does not establish a new claim absent from inputs: generated semantics remain indeterminate. Recompilation and centroid updates establish revision of retained products; title cleanup establishes a bounded duplicate criterion. Reading-event time decay changes influence, not event deletion. See [EPI-RTE-extractive-summary](epistemic.md#epi-rte-extractive-summary), [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), [EPI-RTE-numeric-selection](epistemic.md#epi-rte-numeric-selection), [EPI-RTE-title-cleanup](epistemic.md#epi-rte-title-cleanup) and [MEM-RTE-history-selection](memory.md#mem-rte-history-selection). No synthesis finding is inferred from an unknown model output; deletion without demonstrated historical retention is not classified as invalidation.

Reconciliation supersedes the entity-object declaration in epistemic with [MEM-OBJ-entities](memory.md#mem-obj-entities); the profile therefore cites that canonical object. The valid article, answer/confidence and HTTP-withdrawal/title-cleanup containers retain distinct parts and are not collapsed. The budget disagreement between [RT-RTE-chat-query](runtime.md#rt-rte-chat-query) and [MEM-CLM-budget-scope](memory.md#mem-clm-budget-scope) prevents a universal budget guarantee, not the recorded history/retrieval existence findings. This profile retains the hierarchical/flat distinction and makes no whole-message cap claim.

All ten axes remain partial because their named inventories contain unresolved alternatives, origins or consumers. Positive findings are retained with their local evidence layers; no strongest witness upgrades unknown alternatives. Entity-card lineage, complete collector and maintenance paths, exact user-note/source-dictionary consumption, archive payload inventory, provider accumulated state and some topic/graph semantics prevent stronger assessments. No bounded absence record establishes a trace-learning no across those units.

Source-read log: none. Classification used only the supplied records and reconciliation; no source facts or quotes were added and no report verification was reopened.
