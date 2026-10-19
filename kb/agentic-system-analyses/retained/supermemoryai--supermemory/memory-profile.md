---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Supermemory memory comparison across remote documents, graph facts/profiles, exact-file memory, adapter reuse and retained access state, with the engine opaque."
run-id: "AAS-2026-10-19-supermemory-1cc18c778c48-01"
source-identity: "https://github.com/supermemoryai/supermemory"
reviewed-boundary: "f81fad00e4bfc42610159cf6bd7bdb5fc4ca7cbe"
memory-comparison:
  version: 2
  scope: "Included: accumulated remote source documents/chunks and embeddings, extracted graph facts and eligibility/relations, profiles/aggregates, Claude exact-file documents, continuation display reuse, retained namespace/upload access state, their writes, maintenance and later consumers, including opaque engine and incompletely traced adapter/connector alternatives. Excluded: unchanged shipped prompts/package code, transient current-call payloads without later reuse, generation/extraction model weights not shown changed through memory use, external host machinery and uncaptured benchmark/plugin internals."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Remote documents, Claude file bodies and service-owned profile representation"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-file"
                - "memory.md#mem-rte-claude-file"
              note: "Exact-file reads and writes address remote document objects."
            - value: "service-object"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-obj-profile-summary"
              note: "Documents and profile objects are described as service-owned retained material."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-obj-claude-file"
            - "memory.md#mem-obj-profile-summary"
          note: "The service-object classification identifies the operative API-owned object, not its physical database."
        - scope: "Declared temporal graph and indexed dense representations"
          assessment: "partial"
          findings:
            - value: "graph"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-memory-facts"
                - "memory.md#mem-rte-engine-dreaming"
              note: "Atomic facts have retained temporal relations."
            - value: "vector"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-rte-engine-dreaming"
              note: "Dense representations and indexed chunks are declared in document processing."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-obj-memory-facts"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Logical graph/vector organization is declared; physical stores and the remaining engine state are inaccessible."
        - scope: "Wrapper-local retained display strings"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-memory-cache"
              note: "MemoryCache is an in-process LRU."
          records:
            - "runtime.md#rt-obj-memory-cache"
          note: "The LRU retains formatted memory across continuation invocations, not canonical durable facts."
        - scope: "Durable active namespace and upload capability state"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-space-state"
              note: "Actor-scoped Durable Object storage retains routing state and temporary upload records."
          records:
            - "runtime.md#rt-obj-space-state"
          note: "This includes retained access structures, not all runtime credentials or permissions."
      records:
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-obj-claude-file"
        - "memory.md#mem-obj-profile-summary"
        - "memory.md#mem-obj-memory-facts"
        - "memory.md#mem-rte-engine-dreaming"
        - "runtime.md#rt-obj-memory-cache"
        - "runtime.md#rt-obj-space-state"
      note: "Remote objects, graph/vector declarations, local reuse and durable access state are classified. Opaque engine physical storage prevents complete substrate coverage; local file paths do not establish files or repo storage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Document transcript/extracted text, fact text, profile prose and default cached context"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-memory-cache"
                - "runtime.md#rt-rte-vercel-call"
              note: "Formatted facts are retained and interpreted by the generation model."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-obj-memory-facts"
                - "memory.md#mem-obj-profile-summary"
              note: "Document text, extracted claims and profile summaries are declared textual products."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-obj-memory-facts"
            - "memory.md#mem-obj-profile-summary"
            - "runtime.md#rt-obj-memory-cache"
          note: "These readable parts are distinct from their metadata and numerical representations."
        - scope: "Claude file body as prose versus arbitrary command-supplied content"
          assessment: "partial"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-file"
                - "memory.md#mem-rte-claude-file"
              note: "The adapter stores and returns authored file prose to Claude."
          records:
            - "memory.md#mem-obj-claude-file"
            - "memory.md#mem-rte-claude-file"
          note: "Authored prose is supported, but arbitrary file instances need not be prose and no instance resolves their encoding."
        - scope: "Document/file identity, graph eligibility/relations, profile section identifiers and cache/namespace access state"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-file"
                - "runtime.md#rt-obj-memory-cache"
                - "runtime.md#rt-obj-space-state"
              note: "Paths, cache keys and namespace/capability values have fixed code consumers."
            - value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-obj-profile-summary"
              note: "Eligibility flags, edges and section identifiers govern service selection."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-obj-claude-file"
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-obj-profile-summary"
            - "runtime.md#rt-obj-memory-cache"
            - "runtime.md#rt-obj-space-state"
          note: "Fixed-rule identifiers and flags are separated from interpreted text."
        - scope: "Declared dense embeddings"
          assessment: "partial"
          findings:
            - value: "parametric"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "runtime.md#rt-cmp-local-embeddings"
              note: "Distributed numerical embeddings are distinct from readable chunks."
          records:
            - "memory.md#mem-obj-document-content"
            - "runtime.md#rt-cmp-local-embeddings"
          note: "Numerical dense representations are declared; their exact operative contents and remaining opaque engine representations are unresolved."
        - scope: "Other adapter payload transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
          note: "Detailed alternative Python and advanced adapter representations are not established by the accepted records."
      records:
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-obj-memory-facts"
        - "memory.md#mem-obj-profile-summary"
        - "runtime.md#rt-obj-memory-cache"
        - "memory.md#mem-obj-claude-file"
        - "memory.md#mem-rte-claude-file"
        - "memory.md#mem-obj-memory-state"
        - "runtime.md#rt-obj-space-state"
        - "runtime.md#rt-cmp-local-embeddings"
        - "memory.md#mem-clm-adapter-variants"
      note: "Mixed parts are split. Model weights used as machinery are excluded unless changed through memory use; their mere existence does not add memory form findings."
    lineage:
      assessment: "partial"
      units:
        - scope: "Submitted documents and continuing connector imports"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "memory.md#mem-rte-livekit-session"
              note: "Conversation text enters remote documents from host sessions."
            - value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-connector-sync"
                - "memory.md#mem-obj-document-content"
              note: "Files, URLs and connector content are acquired from outside the store."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-connector-sync"
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "memory.md#mem-rte-livekit-session"
          note: "This classifies the recorded acquisition paths, not every initial backend object."
        - scope: "Claude file creation/editing"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-file"
                - "memory.md#mem-rte-claude-file"
              note: "Commands directly create or replace file text."
          records:
            - "memory.md#mem-obj-claude-file"
            - "memory.md#mem-rte-claude-file"
          note: "Caller/model command authorship is distinct from human admission control."
        - scope: "Conversation-derived fact/profile route"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-engine-dreaming"
                - "runtime.md#rt-rte-vercel-call"
                - "memory.md#mem-rte-livekit-session"
              note: "Session transcripts feed extraction into facts and profiles."
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "runtime.md#rt-rte-vercel-call"
            - "memory.md#mem-rte-livekit-session"
          note: "This is the declared derivation path; extraction internals and observed provenance are not upgraded."
        - scope: "Non-trace document derivatives, cross-memory inferences, profile aggregates and local formatted displays"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-obj-memory-facts"
                - "memory.md#mem-obj-profile-summary"
                - "memory.md#mem-rte-engine-dreaming"
              note: "Chunking, cross-memory derivation and aggregate summaries transform retained source material."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-format"
                - "runtime.md#rt-obj-memory-cache"
              note: "Default formatting and deduplication produce the cached display string."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-obj-memory-facts"
            - "memory.md#mem-obj-profile-summary"
            - "epistemic.md#epi-rte-memory-format"
            - "runtime.md#rt-obj-memory-cache"
          note: "Compilation paths are supported, but mixed input provenance and embedding derivation are not completely resolved."
        - scope: "Initial engine contents and exact embedding provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Initialization control and actual embedding lineage are not recorded."
        - scope: "Alternative incompletely traced adapter derivations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
          note: "The records do not fully trace alternative payload transformations."
      records:
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-rte-connector-sync"
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "memory.md#mem-rte-livekit-session"
        - "memory.md#mem-obj-claude-file"
        - "memory.md#mem-rte-claude-file"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-obj-memory-facts"
        - "memory.md#mem-obj-profile-summary"
        - "epistemic.md#epi-rte-memory-format"
        - "runtime.md#rt-obj-memory-cache"
        - "memory.md#mem-clm-adapter-variants"
      note: "Imported, authored, trace-derived and other compiled parts coexist; known subsequent transformations do not resolve initialization or mixed provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Fact/profile/document text and exact file prose at later answering models"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-memory-context"
                - "memory.md#mem-rte-mcp-read"
                - "memory.md#mem-bap-file-reload"
                - "memory.md#mem-rte-livekit-session"
              note: "Later models receive retained assertions and reference prose through system, assistant or tool-result channels."
          records:
            - "runtime.md#rt-bap-memory-context"
            - "memory.md#mem-rte-mcp-read"
            - "memory.md#mem-bap-file-reload"
            - "memory.md#mem-rte-livekit-session"
          note: "Delivery supplies context, not reliable compliance or factual warrant."
        - scope: "Retained file guidance and preferences interpreted as directions"
          assessment: "partial"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-bap-file-reload"
                - "runtime.md#rt-bap-memory-context"
              note: "Retained prose can enter the model as interpretive instruction; it is not enforcement."
          records:
            - "memory.md#mem-bap-file-reload"
            - "runtime.md#rt-bap-memory-context"
            - "memory.md#mem-obj-claude-file"
          note: "Instructional force is supported for the content/guidance path, not every arbitrary file or factual assertion."
        - scope: "Retained conversation experience at the extraction/profile update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-rte-engine-dreaming"
                - "runtime.md#rt-rte-vercel-call"
                - "memory.md#mem-rte-livekit-session"
              note: "Session records feed automatic production of durable fact/profile context for later use."
          records:
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-engine-dreaming"
            - "runtime.md#rt-rte-vercel-call"
            - "memory.md#mem-rte-livekit-session"
          note: "The declared trace-to-durable-context update supplies learning authority independently of downstream knowledge authority."
        - scope: "Retained fact text and dense features at remote retrieval ranking"
          assessment: "partial"
          findings:
            - value: "ranking"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-memory-facts"
                - "memory.md#mem-obj-document-content"
                - "memory.md#mem-rte-engine-dreaming"
                - "memory.md#mem-rte-mcp-read"
              note: "Indexed facts/chunks and embeddings supply the remote ranked retrieval route."
          records:
            - "memory.md#mem-obj-memory-facts"
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-rte-mcp-read"
          note: "Search ranking consumes retained material, but exact scores/features and all backend rankers are opaque."
        - scope: "Active namespace at the default-space resolver"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-space-selection"
              note: "Retained active namespace selects later default tool and context scope."
          records:
            - "runtime.md#rt-bap-space-selection"
            - "runtime.md#rt-obj-space-state"
          note: "Explicit namespace can override this routing default."
        - scope: "Retained eligibility flags at search/review selection"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "claimed"
              records:
                - "memory.md#mem-bap-eligibility-selection"
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-rte-inference-review"
              note: "Forgotten state excludes retained facts from later search."
          records:
            - "memory.md#mem-bap-eligibility-selection"
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-rte-inference-review"
          note: "This is a documented search veto, not demonstrated service enforcement."
        - scope: "Retained upload capability at upload admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-space-state"
                - "runtime.md#rt-rte-upload-session"
              note: "Stored capability identity/expiry determine upload admissibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-space-state"
                - "runtime.md#rt-rte-upload-session"
              note: "Mismatched or expired capability state refuses forwarding."
          records:
            - "runtime.md#rt-obj-space-state"
            - "runtime.md#rt-rte-upload-session"
          note: "The stored token hash and expiry are admission criteria and a code-level veto, not content-truth criteria."
        - scope: "Opaque engine and incompletely traced alternative consumer effects"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-clm-adapter-variants"
          note: "Exact internal consumers and alternative effects cannot be exhaustively classified."
      records:
        - "runtime.md#rt-bap-memory-context"
        - "memory.md#mem-rte-mcp-read"
        - "memory.md#mem-bap-file-reload"
        - "memory.md#mem-rte-livekit-session"
        - "memory.md#mem-obj-claude-file"
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-rte-engine-dreaming"
        - "runtime.md#rt-rte-vercel-call"
        - "memory.md#mem-obj-memory-facts"
        - "runtime.md#rt-bap-space-selection"
        - "runtime.md#rt-obj-space-state"
        - "memory.md#mem-bap-eligibility-selection"
        - "memory.md#mem-obj-memory-state"
        - "memory.md#mem-rte-inference-review"
        - "runtime.md#rt-rte-upload-session"
        - "memory.md#mem-clm-adapter-variants"
      note: "Authority follows each actual consumer. Recorded knowledge, instruction, learning, ranking, routing and capability/eligibility controls are not a claim of observed dependence or improvement."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Automatic conversation submissions, voice capture and inspected hook submissions"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
                - "memory.md#mem-clm-adapter-variants"
              note: "Software admits eligible conversation text without individual human approval."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "runtime.md#rt-rte-python-context"
            - "memory.md#mem-rte-livekit-session"
            - "memory.md#mem-clm-adapter-variants"
          note: "Flags permit disabling these paths; starting a host request is not per-content approval."
        - scope: "Model-selected framework saves and Claude file commands"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-tool-loop"
                - "memory.md#mem-rte-claude-file"
              note: "A model can submit or replace retained content without human content approval."
          records:
            - "runtime.md#rt-rte-tool-loop"
            - "memory.md#mem-rte-claude-file"
          note: "The shipped model-driven routes admit proposed content through code/service checks."
        - scope: "Remote fact/profile extraction and connector sync"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-engine-dreaming"
                - "memory.md#mem-rte-connector-sync"
              note: "Engine and connector software decide individual extraction/import admission."
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-rte-connector-sync"
          note: "Authorization of acquisition scope is not approval of each resulting document or fact."
        - scope: "Interactive guided-save human editing/approval surface"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-mcp-save"
              note: "The intended draft/review experience permits a human to edit and approve exact content."
          records:
            - "runtime.md#rt-rte-mcp-save"
          note: "The memory annotation records an afforded human content decision, not an exercised or mandatory gate."
        - scope: "Generic MCP/HTTP saves, uploads, review and document maintenance callers; initial backend population"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-save"
            - "runtime.md#rt-rte-upload-session"
            - "memory.md#mem-rte-inference-review"
            - "memory.md#mem-rte-source-maintenance"
            - "memory.md#mem-obj-document-content"
          note: "Generic caller identity does not determine human versus software admission; initialization control is unknown."
        - scope: "Other adapter admission predicates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
          note: "Not all alternative write mechanisms are traced."
      records:
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "runtime.md#rt-rte-python-context"
        - "memory.md#mem-rte-livekit-session"
        - "memory.md#mem-clm-adapter-variants"
        - "runtime.md#rt-rte-tool-loop"
        - "memory.md#mem-rte-claude-file"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-rte-connector-sync"
        - "runtime.md#rt-rte-mcp-save"
        - "runtime.md#rt-rte-upload-session"
        - "memory.md#mem-rte-inference-review"
        - "memory.md#mem-rte-source-maintenance"
        - "memory.md#mem-obj-document-content"
      note: "Automatic wired and claimed paths coexist with an afforded manual path and unresolved generic callers. Neither human authorship nor physical API I/O decides agency."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Default retained-memory normalization/deduplication before cached context"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-memory-format"
                - "runtime.md#rt-obj-memory-cache"
              note: "Normalized variants merge with static/dynamic/search precedence."
          records:
            - "epistemic.md#epi-rte-memory-format"
            - "runtime.md#rt-obj-memory-cache"
          note: "This is exact-variant selection, not a semantic correctness check."
        - scope: "Claude file replacement and line/string editing"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-claude-file"
              note: "Update replacement and literal edits change retained file content."
          records:
            - "memory.md#mem-rte-claude-file"
          note: "Implemented edits revise an existing retained entry; rename is not atomic."
        - scope: "Declared session extraction and older-profile summarization"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-engine-dreaming"
                - "memory.md#mem-obj-profile-summary"
              note: "Standing fact extraction and older-memory aggregates reduce retained source content."
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-obj-profile-summary"
          note: "This is reduction of existing content, independent of whether raw messages remain."
        - scope: "Declared cross-memory inference"
          assessment: "known"
          findings:
            - value: "synthesize"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-memory-facts"
                - "epistemic.md#epi-rte-graph-dreaming"
              note: "Dreaming derives a new claim from patterns across memories."
          records:
            - "memory.md#mem-obj-memory-facts"
            - "epistemic.md#epi-rte-graph-dreaming"
          note: "The documented example adds a proposition not entailed by its stated inputs."
        - scope: "Declared graph update, expiry, withdrawal and review"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-engine-dreaming"
                - "memory.md#mem-rte-source-maintenance"
              note: "Graph updates and source reprocessing revise retained content."
            - value: "decay"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-engine-dreaming"
              note: "Temporary facts expire under declared time-based forgetting."
            - value: "invalidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-inference-review"
                - "memory.md#mem-rte-semantic-forget"
                - "memory.md#mem-obj-memory-state"
              note: "Forgotten facts leave search while rows/history remain."
            - value: "promote"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-inference-review"
                - "epistemic.md#epi-clm-review-facts"
              note: "Review approval raises an inferred item to confirmed status by clearing its inference flag."
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-rte-inference-review"
            - "memory.md#mem-rte-semantic-forget"
            - "memory.md#mem-rte-source-maintenance"
            - "memory.md#mem-obj-memory-state"
            - "epistemic.md#epi-clm-review-facts"
          note: "These are design-level transformations; request dispatch alone is not implemented remote curation."
        - scope: "Opaque additional engine maintenance and alternative adapter transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-clm-adapter-variants"
          note: "No exhaustive operation inventory is established; algorithms and propagation are unresolved."
      records:
        - "epistemic.md#epi-rte-memory-format"
        - "runtime.md#rt-obj-memory-cache"
        - "memory.md#mem-rte-claude-file"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-obj-profile-summary"
        - "memory.md#mem-obj-memory-facts"
        - "epistemic.md#epi-rte-graph-dreaming"
        - "memory.md#mem-rte-inference-review"
        - "memory.md#mem-rte-semantic-forget"
        - "memory.md#mem-rte-source-maintenance"
        - "memory.md#mem-obj-memory-state"
        - "epistemic.md#epi-clm-review-facts"
        - "memory.md#mem-clm-adapter-variants"
      note: "All supported transformations remain attached to their wired or claimed mechanisms. Indexing, primary-key checks, acquisition and mutation request names alone add no curation values."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit framework/MCP search, profile, document, context-prompt and Claude file requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-tool-loop"
                - "memory.md#mem-rte-mcp-read"
                - "runtime.md#rt-rte-mcp-context"
                - "memory.md#mem-rte-claude-file"
              note: "A consumer requests retained material and receives the selected result."
          records:
            - "runtime.md#rt-rte-tool-loop"
            - "memory.md#mem-rte-mcp-read"
            - "runtime.md#rt-rte-mcp-context"
            - "memory.md#mem-rte-claude-file"
          note: "Selection inside fulfillment does not turn a requested result into unsolicited supply."
        - scope: "Middleware and lifecycle context injection and continuation reuse"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
                - "runtime.md#rt-obj-memory-cache"
              note: "Code independently retrieves/reuses and supplies retained context before generation."
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
              note: "Within the chain, adapters request retained profile/search material from the API."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "runtime.md#rt-rte-python-context"
            - "memory.md#mem-rte-livekit-session"
            - "runtime.md#rt-obj-memory-cache"
          note: "A host model invocation triggers automatic memory supply without a model request for that material."
        - scope: "Connector downstream consumer contract"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-connector-sync"
              note: "Imported content is available through later requested search/profile routes."
          records:
            - "memory.md#mem-rte-connector-sync"
          note: "Sync writes automatically but does not independently deliver context to a model."
        - scope: "Other adapter and opaque engine delivery alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Untraced alternatives prevent complete direction coverage; no independent connector push is inferred."
      records:
        - "runtime.md#rt-rte-tool-loop"
        - "memory.md#mem-rte-mcp-read"
        - "runtime.md#rt-rte-mcp-context"
        - "memory.md#mem-rte-claude-file"
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "runtime.md#rt-rte-python-context"
        - "memory.md#mem-rte-livekit-session"
        - "runtime.md#rt-obj-memory-cache"
        - "memory.md#mem-rte-connector-sync"
        - "memory.md#mem-clm-adapter-variants"
        - "memory.md#mem-rte-engine-dreaming"
      note: "Both directions occur at different operations in a chain. Explicit MCP prompt requests are pull; automatic pre-model insertion is push. The complete read inventory remains unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic profile mode before model invocation"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
              note: "Profile-mode availability/mode selection supplies broadly scoped profile text."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
              note: "Configured namespace/tag matches the profile whose facts are delivered."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "runtime.md#rt-rte-python-context"
            - "memory.md#mem-rte-livekit-session"
          note: "Trigger is host generation/lifecycle; selector uses configured mode and namespace to supply static/dynamic profile content."
        - scope: "Vercel continuation cache hit before generation"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-memory-cache"
                - "runtime.md#rt-rte-vercel-call"
              note: "The actual compound cache-key match selects the delivered retained display string."
          records:
            - "runtime.md#rt-obj-memory-cache"
            - "runtime.md#rt-rte-vercel-call"
          note: "Trigger is a non-user continuation; namespace, conversation ID, mode and normalized latest-user text match a retained string."
        - scope: "Query-driven automatic recall"
          assessment: "partial"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "memory.md#mem-rte-livekit-session"
              note: "Namespace/tag scoping selects the retained population for automatic query recall."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "memory.md#mem-rte-livekit-session"
            - "memory.md#mem-rte-mcp-read"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Latest user text and namespace select retained query results, but remote semantic scoring cannot be decomposed into embedding, lexical or judgment mechanisms from these records."
        - scope: "Other push selectors and opaque ranking internals"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
            - "memory.md#mem-rte-engine-dreaming"
          note: "No accepted record resolves all alternative selector mechanisms; do not infer embedding selection merely from embedding storage."
      records:
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "runtime.md#rt-rte-python-context"
        - "memory.md#mem-rte-livekit-session"
        - "runtime.md#rt-obj-memory-cache"
        - "memory.md#mem-rte-mcp-read"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-clm-adapter-variants"
      note: "Signals classify automatic push selection, not requested file IDs or every API return. Coarse profile supply and actual identity matches are supported; inferred query-signal taxonomy remains unresolved."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Conversation-to-fact/profile automatic extraction and later context consumption"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
                - "memory.md#mem-rte-engine-dreaming"
                - "memory.md#mem-obj-profile-summary"
                - "runtime.md#rt-bap-memory-context"
              note: "Automatically admitted session traces produce durable fact/profile context for later answering consumers; no parameter update or demonstrated improvement is required."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "runtime.md#rt-rte-python-context"
            - "memory.md#mem-rte-livekit-session"
            - "memory.md#mem-rte-engine-dreaming"
            - "memory.md#mem-obj-profile-summary"
            - "runtime.md#rt-bap-memory-context"
          note: "Public capture/read wiring is inspected; the intervening durable derivative production is declared, so the complete qualifying chain remains claimed."
        - scope: "Model-authored exact files and generic remember calls"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-claude-file"
            - "runtime.md#rt-rte-tool-loop"
            - "memory.md#mem-rte-livekit-session"
          note: "Automatic write and later reload are wired, but a qualifying original trace-fed content derivation is not established for arbitrary saved text."
        - scope: "Connector and mixed document inputs to dreaming"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-connector-sync"
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Documents may contain activity records, but the accepted records do not resolve qualifying trace content for these alternatives."
        - scope: "Other adapter routes, initialization, opaque engine updates and evaluation feedback"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
            - "memory.md#mem-rte-engine-dreaming"
            - "runtime.md#rt-clm-engine-boundary"
          note: "Alternative trace-fed updates are not exhaustively assessed; no bounded absence record licenses a local or system-wide no."
      records:
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "runtime.md#rt-rte-python-context"
        - "memory.md#mem-rte-livekit-session"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-obj-profile-summary"
        - "runtime.md#rt-bap-memory-context"
        - "memory.md#mem-rte-claude-file"
        - "runtime.md#rt-rte-tool-loop"
        - "memory.md#mem-rte-connector-sync"
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-clm-adapter-variants"
        - "runtime.md#rt-clm-engine-boundary"
      note: "A declared qualifying session route supports yes without upgrading the opaque transformation to wired. Unresolved alternatives keep coverage partial; no negative is asserted."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Qualifying conversation-to-fact/profile route"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-vercel-call"
                - "runtime.md#rt-rte-openai-call"
                - "runtime.md#rt-rte-python-context"
                - "memory.md#mem-rte-livekit-session"
                - "memory.md#mem-rte-engine-dreaming"
              note: "User/assistant session transcripts feed the declared durable extraction route."
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "runtime.md#rt-rte-python-context"
            - "memory.md#mem-rte-livekit-session"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Original content is conversational turns, even when capture is triggered by an event callback."
        - scope: "Potential structured tool content in conversation submissions"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-vercel-call"
            - "runtime.md#rt-rte-openai-call"
            - "memory.md#mem-rte-engine-dreaming"
          note: "Conversion/filtering alternatives and remote consumption of qualifying tool records are unresolved; tool mentions in ordinary prose do not establish tool-traces."
        - scope: "Exact-file, connector, mixed document and opaque update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-claude-file"
            - "memory.md#mem-rte-connector-sync"
            - "memory.md#mem-obj-document-content"
            - "memory.md#mem-rte-engine-dreaming"
          note: "The original input to any additional qualifying learning write is not established; no event-streams or trajectories classification follows from callback labels or connector names."
        - scope: "Incompletely traced adapter/evaluation routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-adapter-variants"
            - "runtime.md#rt-clm-engine-boundary"
          note: "Remaining input transformations and durable feedback consumers are not covered by accepted records."
      records:
        - "runtime.md#rt-rte-vercel-call"
        - "runtime.md#rt-rte-openai-call"
        - "runtime.md#rt-rte-python-context"
        - "memory.md#mem-rte-livekit-session"
        - "memory.md#mem-rte-engine-dreaming"
        - "memory.md#mem-rte-claude-file"
        - "memory.md#mem-rte-connector-sync"
        - "memory.md#mem-obj-document-content"
        - "memory.md#mem-clm-adapter-variants"
        - "runtime.md#rt-clm-engine-boundary"
      note: "Session origin is supported for the declared learning chain. Mixed and opaque alternatives remain included; trace source is not inapplicable merely because other routes are unresolved."
---

# Supermemory memory profile

## Comparison rationale

The comparison separates service objects from their physical substrate. Remote exact-file documents have inspected API consumers, but the graph/vector engine is declared rather than inspected. Dense representations are not the graph display's layout coordinates. The readable fact/profile payload does not expose every retained relation or review field. See [MEM-OBJ-document-content](memory.md#mem-obj-document-content), [MEM-OBJ-memory-state](memory.md#mem-obj-memory-state), [MEM-CLM-graph-display](memory.md#mem-clm-graph-display) and [MEM-RTE-mcp-read](memory.md#mem-rte-mcp-read).

Every axis retains unresolved included alternatives. A known unit means the named path or part can be classified, not that it operated. The engine's physical storage, initialization, embedding provenance, exact ranking and extra maintenance remain unresolved. Alternative adapters are not presumed Vercel-equivalent; [MEM-CLM-adapter-variants](memory.md#mem-clm-adapter-variants) bounds those findings. Known declared operations coexist with opaque implementation, rather than being removed or upgraded by it.

Trace learning has a supported claimed session route: inspected capture and later context delivery surround declared automatic document-to-fact/profile production. The derivative is durable behavior-shaping context; new knowledge, parameter training and observed benefit are unnecessary for this classification. The same retained experience supplies learning authority at extraction, while its output supplies knowledge at the answering model. LiveKit callbacks do not change the original conversational content into an event-stream source. Arbitrary model-authored files and connector documents do not establish a trace source without recorded input provenance. See [MEM-RTE-engine-dreaming](memory.md#mem-rte-engine-dreaming), [MEM-RTE-livekit-session](memory.md#mem-rte-livekit-session), [MEM-RTE-claude-file](memory.md#mem-rte-claude-file) and [MEM-RTE-connector-sync](memory.md#mem-rte-connector-sync). No evidenced-absence record supports a local trace-learning negative; the derived system union supports only the claimed positive, not complete coverage.

Requested tool and MCP prompt returns are pull. Automatic middleware insertion is push downstream of an API pull. The push selector's namespace/profile and cache-key identity matches are distinct from unresolved remote semantic ranking. An embedding's existence does not establish which push selector uses it. See [RT-RTE-vercel-call](runtime.md#rt-rte-vercel-call), [RT-OBJ-memory-cache](runtime.md#rt-obj-memory-cache) and [RT-RTE-mcp-context](runtime.md#rt-rte-mcp-context).

Curation evidence is operation-specific. Local normalized deduplication and exact-file editing are wired; remote consolidation, conjectural synthesis, expiry, update, invalidation and confirmation promotion remain claimed. Review confirmation raises product status but does not establish evidence-consuming truth acceptance. Retained capability checks establish validation/enforcement only at upload admission, not content truth. See [EPI-RTE-memory-format](epistemic.md#epi-rte-memory-format), [MEM-RTE-inference-review](memory.md#mem-rte-inference-review), [EPI-CLM-review-facts](epistemic.md#epi-clm-review-facts) and [RT-RTE-upload-session](runtime.md#rt-rte-upload-session).

Supersessions affect the file and review citations: the canonical object/route are [MEM-OBJ-claude-file](memory.md#mem-obj-claude-file), [MEM-RTE-claude-file](memory.md#mem-rte-claude-file) and [MEM-RTE-inference-review](memory.md#mem-rte-inference-review), not their superseded epistemic counterparts. The broader epistemic graph object and narrower graph transformation remain valid containers/parts, not replacements for the memory objects or complete dreaming chain. This preserves arbitrary-file-content and review-acceptance limits without allocating records.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source reread, added evidence, target execution or report revision occurred.
