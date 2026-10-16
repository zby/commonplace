---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'HippoRAG memory profile: retained document/search state, compatibility metadata and response
  reuse at the frozen revision.'
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
source-identity: https://github.com/OSU-NLP-Group/HippoRAG
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
memory-comparison:
  version: 2
  scope: 'Included: imported passage content and metadata; extracted OpenIE rows; normalized entity/fact
    strings; passage/entity/fact vectors and access structures; source-aware graph; compatibility manifest;
    prepared-instance query-vector reuse; CacheOpenAI response replay; shipped StandardRAG, offline, MCP,
    reload and folder-maintenance routes. Alternative vector collections and uninspected provider caches/injected
    persistence retain their recorded limits. Excluded: static shipped prompts/skills and code as retained
    memory, external model weights and provider internals, general host state, ordinary current-call QuerySolution/IRCoT
    state and benchmark scores without a later retained consumer. Shipped fixtures/datasets do not establish
    trace provenance or observed operation.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Original passage and normalized entity/fact content rows in default stores
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-passage-text
          - memory.md#mem-obj-entity-text
          - memory.md#mem-obj-fact-text
          note: Parquet persistence and loaded mappings hold the retained strings.
        - value: in-memory
          basis: wired
          records: *id001
          note: Parquet persistence and loaded mappings hold the retained strings.
        records:
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        note: Default Parquet files reopen into process mappings; these are content parts, not model weights.
      - scope: Passage, entity and fact embedding arrays and their vector access structures
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-passage-embeddings
          - memory.md#mem-obj-entity-embeddings
          - memory.md#mem-obj-fact-embeddings
          note: Default Parquet columns and loaded dense arrays supply vector search.
        - value: vector
          basis: wired
          records: *id002
          note: Default Parquet columns and loaded dense arrays supply vector search.
        - value: in-memory
          basis: wired
          records: *id002
          note: Default Parquet columns and loaded dense arrays supply vector search.
        records:
        - memory.md#mem-obj-passage-embeddings
        - memory.md#mem-obj-entity-embeddings
        - memory.md#mem-obj-fact-embeddings
        note: Stored encoder outputs differ from encoder parameters; backend durability is not inferred.
      - scope: OpenIE rows, chunk metadata and compatibility manifest
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-openie-state
          - memory.md#mem-obj-chunk-metadata
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          note: Retained JSON is reopened into process structures for later operations.
        - value: in-memory
          basis: wired
          records: *id003
          note: Retained JSON is reopened into process structures for later operations.
        records:
        - memory.md#mem-obj-openie-state
        - memory.md#mem-obj-chunk-metadata
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        note: JSON files and loaded structures retain extraction, provenance and configuration state.
      - scope: Source-aware graph
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-graph-state
          note: Pickled graph reloads for PPR and source-sensitive maintenance.
        - value: graph
          basis: wired
          records: *id004
          note: Pickled graph reloads for PPR and source-sensitive maintenance.
        - value: in-memory
          basis: wired
          records: *id004
          note: Pickled graph reloads for PPR and source-sensitive maintenance.
        records:
        - memory.md#mem-obj-graph-state
        note: The pickle and operative igraph structure are both included.
      - scope: Alternative Qdrant, Chroma and Milvus content/vector collections
        assessment: partial
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-passage-text
          - memory.md#mem-obj-passage-embeddings
          - memory.md#mem-obj-entity-embeddings
          - memory.md#mem-obj-fact-embeddings
          note: Alternative collections retain vector/content search state through recorded backend interfaces.
        records:
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-passage-embeddings
        - memory.md#mem-obj-entity-embeddings
        - memory.md#mem-obj-fact-embeddings
        note: Accepted inventory records vector interfaces and reload caches, but not complete external
          persistence semantics or all operative backend parts.
      - scope: CacheOpenAI response table
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id006
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-response-reuse
          note: The cache table is in a local SQLite database.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: SQLite retains response messages and metadata independently of the index.
      - scope: Prepared-instance query embedding reuse
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-rte-retrieve-answer
          note: Prepared-instance query vectors survive for later requests.
        records:
        - runtime.md#rt-rte-retrieve-answer
        note: Memory annotation establishes query_to_embedding reuse and reset after mutation; no durable
          query-vector file is established.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Other cache substrates are not recorded. Accepted records inspect CacheOpenAI, not equivalent
          lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-entity-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-passage-embeddings
      - memory.md#mem-obj-entity-embeddings
      - memory.md#mem-obj-fact-embeddings
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-chunk-metadata
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - memory.md#mem-obj-graph-state
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-rte-retrieve-answer
      - runtime.md#rt-rte-standard-rag
      note: The default object inventory is classified; alternative vector collections have recorded vector
        interfaces but uninspected external database semantics, and other provider caches remain unresolved.
        Vector-store encoding does not establish an additional database category.
    representational_form:
      assessment: partial
      units:
      - scope: Passage text at extraction, QA and returned-context consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-passage-text
          note: Models interpret original passage content.
        records:
        - memory.md#mem-obj-passage-text
        note: The knowledge-bearing text is separate from its hash identity.
      - scope: Entity and fact strings at encoder/filter interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-entity-text
          - memory.md#mem-obj-fact-text
          note: Encoder and filter interpret meaningful labels and relations.
        records:
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        note: Lexical content has a model-interpreted path distinct from tuple/equality operations.
      - scope: Entity identity strings and fact tuple structure at fixed-rule consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: *id005
          note: Hashing, equality, tuple decoding and graph mapping use fixed rules.
        records:
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        note: Localized labels, tuple structure and identities are symbolic at these consumers.
      - scope: Dense passage/entity/fact and reused query vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-passage-embeddings
          - memory.md#mem-obj-entity-embeddings
          - memory.md#mem-obj-fact-embeddings
          - runtime.md#rt-rte-retrieve-answer
          note: Dense numerical state distributes the representation across coordinates.
        records:
        - memory.md#mem-obj-passage-embeddings
        - memory.md#mem-obj-entity-embeddings
        - memory.md#mem-obj-fact-embeddings
        - runtime.md#rt-rte-retrieve-answer
        note: Numerical representations, not trained parameter updates.
      - scope: OpenIE passage/entity/relation content interpreted by models
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-openie-state
          note: Saved rows retain meaningful passages and extracted lexical content.
        records:
        - memory.md#mem-obj-openie-state
        note: Content is separated from the saved row schema.
      - scope: OpenIE schema, graph, manifest, metadata and response-cache keys/metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-openie-state
          - memory.md#mem-obj-graph-state
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          - memory.md#mem-obj-chunk-metadata
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-response-reuse
          note: Fixed schema, identity, matching and numerical graph rules govern these paths.
        records:
        - memory.md#mem-obj-openie-state
        - memory.md#mem-obj-graph-state
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        - memory.md#mem-obj-chunk-metadata
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: Arbitrary metadata payload meaning is unresolved; this unit covers the recorded mapping/identity
          consumers only.
      - scope: CacheOpenAI retained raw message at parser and QA interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id006
          note: Retained model text is returned to extraction, filter or QA callers.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: The readable raw message is the actual replayed payload, not a display summary of opaque
          weights.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Consumed payload forms of other caches are not established. Accepted records inspect CacheOpenAI,
          not equivalent lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-entity-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-passage-embeddings
      - memory.md#mem-obj-entity-embeddings
      - memory.md#mem-obj-fact-embeddings
      - runtime.md#rt-rte-retrieve-answer
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-graph-state
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - memory.md#mem-obj-chunk-metadata
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-rte-standard-rag
      note: Mixed objects are split by operative path. Caller metadata has opaque internal content, and
        uninspected alternative caches prevent complete form enumeration.
    lineage:
      assessment: partial
      units:
      - scope: Original passage content and caller provenance metadata
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-passage-text
          - memory.md#mem-obj-chunk-metadata
          note: Caller strings/Chunks and metadata enter retained state.
        records:
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-chunk-metadata
        note: Imported means acquisition across the API boundary, not human authorship or authenticated
          source warrant.
      - scope: Extracted rows, normalized labels/facts, vectors and graph
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-openie-state
          - memory.md#mem-obj-entity-text
          - memory.md#mem-obj-fact-text
          - memory.md#mem-obj-passage-embeddings
          - memory.md#mem-obj-entity-embeddings
          - memory.md#mem-obj-fact-embeddings
          - memory.md#mem-obj-graph-state
          - runtime.md#rt-rte-index-state
          - runtime.md#rt-rte-offline-extraction
          - runtime.md#rt-rte-standard-rag
          note: Software/model stages derive search representations from supplied document content.
        records:
        - memory.md#mem-obj-openie-state
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        - memory.md#mem-obj-passage-embeddings
        - memory.md#mem-obj-entity-embeddings
        - memory.md#mem-obj-fact-embeddings
        - memory.md#mem-obj-graph-state
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        note: The derivation path is known; exact encoder weights and accuracy are not thereby known.
      - scope: Manifest and prepared-instance query vectors
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          - runtime.md#rt-rte-retrieve-answer
          note: Code assembles compatibility state and encodes queries.
        records:
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        - runtime.md#rt-rte-retrieve-answer
        note: Compatibility fields derive from configuration and reused vectors from query encoding.
      - scope: CacheOpenAI raw model responses
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: *id006
          note: A successful provider response is retained before downstream interpretation.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: Model output is compiled from an inference request; replay alone does not establish trace
          extraction.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Alternative cache production/provenance paths are not established. Accepted records inspect
          CacheOpenAI, not equivalent lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-chunk-metadata
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-entity-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-passage-embeddings
      - memory.md#mem-obj-entity-embeddings
      - memory.md#mem-obj-fact-embeddings
      - memory.md#mem-obj-graph-state
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - runtime.md#rt-rte-retrieve-answer
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      note: Known import and derivation paths do not establish human-authored lineage, trace origins for
        arbitrary input, or producer-weight provenance. No authored or trace-extracted value is inferred
        from generic caller identity or response logging.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Original passage content supplied to extraction and answering consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-passage-text
          - runtime.md#rt-rte-retrieve-answer
          note: Extraction and QA interpret retained source content as material for their tasks.
        records:
        - memory.md#mem-obj-passage-text
        - runtime.md#rt-rte-retrieve-answer
        note: Passages supply source material and answer context, not an enforced instruction hierarchy.
      - scope: Fact strings/vectors, passage vectors and graph at retrieval ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-entity-text
          - memory.md#mem-obj-fact-text
          - memory.md#mem-obj-passage-embeddings
          - memory.md#mem-obj-entity-embeddings
          - memory.md#mem-obj-fact-embeddings
          - memory.md#mem-obj-graph-state
          - runtime.md#rt-rte-retrieve-answer
          note: Candidate similarity, fact interpretation, passage weights and graph propagation influence
            priority.
        records:
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        - memory.md#mem-obj-passage-embeddings
        - memory.md#mem-obj-entity-embeddings
        - memory.md#mem-obj-fact-embeddings
        - memory.md#mem-obj-graph-state
        - runtime.md#rt-rte-retrieve-answer
        note: Fixed scoring code can give retained content ranking force without learning a ranking policy.
      - scope: Entity vectors at synonym-edge construction
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-entity-embeddings
          note: KNN similarity orders candidate synonym links before construction.
        records:
        - memory.md#mem-obj-entity-embeddings
        note: Retained similarity inputs affect which proposed connections receive threshold/top-k admission.
      - scope: OpenIE rows at rebuild/reuse/deletion and missing-key selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-openie-state
          - runtime.md#rt-rte-index-state
          - runtime.md#rt-rte-offline-extraction
          - runtime.md#rt-rte-standard-rag
          note: Existing extraction coverage and source mappings determine reuse, construction and removal
            scope.
        records:
        - memory.md#mem-obj-openie-state
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        note: Saved extraction and source mappings select work and input scope for later maintenance.
      - scope: Chunk source identifiers at MCP deletion targeting
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-chunk-metadata
          - runtime.md#rt-rte-mcp-tools
          note: Source-ID matching determines the deletion input set.
        records:
        - memory.md#mem-obj-chunk-metadata
        - runtime.md#rt-rte-mcp-tools
        note: Current source_id selects matching retained texts; metadata is not an authorization grant.
      - scope: Manifest compatibility fields at initialization/reuse checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id007
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          note: Retained configuration supplies compatibility criteria whose mismatch raises an error.
        - value: enforcement
          basis: wired
          records: *id007
          note: Retained configuration supplies compatibility criteria whose mismatch raises an error.
        records:
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        note: Equality/provenance criteria can veto incompatible state; this is not content truth validation.
      - scope: CacheOpenAI raw messages replayed to extraction/filter/QA
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: *id006
          note: Matching later inference callers receive retained message content.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: The retained output replaces fresh inference and supplies content to downstream interpretation,
          not standing instructions.
      - scope: Response-cache request keys and prepared query-vector access state
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-response-reuse
          - runtime.md#rt-rte-retrieve-answer
          note: Retained request identity selects the reusable response/vector path.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-retrieve-answer
        note: Exact matching chooses reuse versus generation; query vectors also influence retrieval ranking.
      - scope: Passages returned for enclosing-agent answering
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - runtime.md#rt-bap-plugin-skills
          note: Skill directs the host to answer from returned passages and cite sources.
        records:
        - memory.md#mem-obj-passage-text
        - runtime.md#rt-bap-plugin-skills
        - runtime.md#rt-rte-mcp-tools
        note: Wired server delivery and claimed host interpretation remain separate; host compliance is
          not upgraded.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Other retained cache parts and their actual downstream effects are not established. Accepted
          records inspect CacheOpenAI, not equivalent lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-passage-text
      - runtime.md#rt-rte-retrieve-answer
      - memory.md#mem-obj-entity-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-passage-embeddings
      - memory.md#mem-obj-entity-embeddings
      - memory.md#mem-obj-fact-embeddings
      - memory.md#mem-obj-graph-state
      - memory.md#mem-obj-openie-state
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - memory.md#mem-obj-chunk-metadata
      - runtime.md#rt-rte-mcp-tools
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-bap-plugin-skills
      note: Knowledge, ranking, routing and compatibility vetoes are local consumer effects. Static shipped
        skills/prompts are excluded as accumulated memory. Neither retained facts nor cached output establishes
        instruction or learning authority by itself.
    write_agency:
      assessment: partial
      units:
      - scope: Initial caller choice/admission of passages and metadata
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-chunk-metadata
        note: Generic caller identity does not show whether a human supplies, edits or approves each retained
          item.
      - scope: Extraction, structural admission, normalization, encoding, graph and manifest production
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-index-state
          - runtime.md#rt-rte-offline-extraction
          - runtime.md#rt-rte-standard-rag
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          - epistemic.md#epi-rte-triple-admission
          - epistemic.md#epi-rte-text-normalization
          note: Software/model stages admit derived content without per-relation human approval.
        records:
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        - epistemic.md#epi-rte-triple-admission
        - epistemic.md#epi-rte-text-normalization
        note: Human workflow initiation is distinct from these software/model admission decisions.
      - scope: Metadata replacement for repeated content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-chunk-metadata
        note: Replacement content is caller-supplied; no per-content human control fact is recorded.
      - scope: CacheOpenAI admission and prepared query-vector insertion
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-response-reuse
          - runtime.md#rt-rte-retrieve-answer
          note: No per-response or per-vector human approval intervenes.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-retrieve-answer
        note: Successful responses and query encodings are retained by code.
      - scope: Folder workflow conditional batch/refresh approval
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - workflow.md#wf-rte-folder-indexing
          note: Skill asks the user to approve large content batches and choose refresh of existing files.
        records:
        - workflow.md#wf-rte-folder-indexing
        note: Only the prescribed explicit confirmation/refresh decision is manual; actual host execution
          remains unobserved.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Admission control for other provider caches is not recorded. Accepted records inspect CacheOpenAI,
          not equivalent lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-chunk-metadata
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - epistemic.md#epi-rte-triple-admission
      - epistemic.md#epi-rte-text-normalization
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-rte-retrieve-answer
      - workflow.md#wf-rte-folder-indexing
      note: Automatic derived admission coexists with claimed conditional human approval. Direct caller
        content admission and metadata replacement stay unresolved; physical file writes do not settle
        agency.
    curation_operations:
      assessment: partial
      units:
      - scope: Extraction into retained source-linked OpenIE rows
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-openie-state
          - epistemic.md#epi-rte-openie-generation
          - runtime.md#rt-rte-index-state
          note: Retained passages feed extraction of reduced entity/relation material for later use.
        records:
        - memory.md#mem-obj-openie-state
        - epistemic.md#epi-rte-openie-generation
        - runtime.md#rt-rte-index-state
        note: The wired route reduces source content into an extracted search representation; lack of
          semantic fidelity does not establish synthesis.
      - scope: Triple uniqueness and normalization-driven duplicate removal
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - epistemic.md#epi-rte-triple-admission
          - epistemic.md#epi-rte-text-normalization
          - memory.md#mem-obj-entity-text
          - memory.md#mem-obj-fact-text
          note: Structural cleanup and normalized tuple equality remove duplicate relation entries.
        records:
        - epistemic.md#epi-rte-triple-admission
        - epistemic.md#epi-rte-text-normalization
        - memory.md#mem-obj-entity-text
        - memory.md#mem-obj-fact-text
        note: This exceeds mere missing-primary-key acquisition checks; duplicate triple tuples are explicitly
          removed.
      - scope: Existing chunk metadata replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-chunk-metadata
          note: An existing chunk mapping is overwritten with newly supplied metadata.
        records:
        - memory.md#mem-obj-chunk-metadata
        note: Repeated content can revise its existing provenance/access entry.
      - scope: Explicit source/text deletion of retained index content
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - runtime.md#rt-rte-index-state
          - runtime.md#rt-rte-offline-extraction
          - runtime.md#rt-rte-standard-rag
          - memory.md#mem-obj-graph-state
          - memory.md#mem-obj-openie-state
          note: Caller-directed removal forgets index content while preserving independently supported
            material.
        records:
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        - memory.md#mem-obj-graph-state
        - memory.md#mem-obj-openie-state
        note: Deletion forgets selected source contributions and unreferenced derivatives; it is not a
          retained-history invalidation or secure erasure.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Transformations of other provider cache entries are not established. Accepted records inspect
          CacheOpenAI, not equivalent lifecycles for every adapter or injection.
      records:
      - memory.md#mem-obj-openie-state
      - epistemic.md#epi-rte-openie-generation
      - runtime.md#rt-rte-index-state
      - epistemic.md#epi-rte-triple-admission
      - epistemic.md#epi-rte-text-normalization
      - memory.md#mem-obj-entity-text
      - memory.md#mem-obj-fact-text
      - memory.md#mem-obj-chunk-metadata
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - memory.md#mem-obj-graph-state
      - memory.md#mem-rte-response-reuse
      note: Consolidation, duplicate removal, metadata revision and explicit forgetting have separate
        warrants. Missing-hash skips, index rebuilds and synonym-edge construction alone do not add curation
        values. No synthesize value follows from possible extraction errors.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested retrieval/QA, dense baseline, IRCoT reads and MCP returns
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-retrieve-answer
          - runtime.md#rt-rte-standard-rag
          - runtime.md#rt-rte-ircot-retrieval
          - runtime.md#rt-rte-mcp-tools
          - memory.md#mem-obj-passage-text
          note: Callers request retained material or answers; internal retrieval fulfils that request.
        records:
        - runtime.md#rt-rte-retrieve-answer
        - runtime.md#rt-rte-standard-rag
        - runtime.md#rt-rte-ircot-retrieval
        - runtime.md#rt-rte-mcp-tools
        - memory.md#mem-obj-passage-text
        note: A question or explicit request triggers selection; copying selected context into requested
          QA is not another unsolicited push.
      - scope: Requested initialization/indexing/maintenance reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-index-state
          - runtime.md#rt-rte-offline-extraction
          - runtime.md#rt-rte-standard-rag
          - runtime.md#rt-obj-index-manifest
          - runtime.md#rt-clm-state-compatibility
          - memory.md#mem-obj-openie-state
          - memory.md#mem-obj-chunk-metadata
          - memory.md#mem-obj-graph-state
          note: Later instances and maintenance calls load the retained state needed by the requested
            operation.
        records:
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        - runtime.md#rt-obj-index-manifest
        - runtime.md#rt-clm-state-compatibility
        - memory.md#mem-obj-openie-state
        - memory.md#mem-obj-chunk-metadata
        - memory.md#mem-obj-graph-state
        note: Reopening an index or requesting maintenance consumes saved state as part of that explicit
          operation.
      - scope: CacheOpenAI inference replay and prepared query-vector reuse
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-response-cache
          - memory.md#mem-rte-response-reuse
          - runtime.md#rt-rte-retrieve-answer
          note: Retained response/vector is returned on a requested operation.
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-retrieve-answer
        note: A matching inference or query request triggers lookup; automatic hit delivery still fulfils
          a request.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Read-back direction of alternative provider caches is unresolved. Accepted records inspect
          CacheOpenAI, not equivalent lifecycles for every adapter or injection.
      records:
      - runtime.md#rt-rte-retrieve-answer
      - runtime.md#rt-rte-standard-rag
      - runtime.md#rt-rte-ircot-retrieval
      - runtime.md#rt-rte-mcp-tools
      - memory.md#mem-obj-passage-text
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-obj-index-manifest
      - runtime.md#rt-clm-state-compatibility
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-chunk-metadata
      - memory.md#mem-obj-graph-state
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      note: All established routes are pull. Uninspected adapter alternatives prevent a pull-only whole-boundary
        conclusion; no independent push is established by automatic selection within a requested return.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Assessed requested index/QA/MCP and cache-reuse chains
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-retrieve-answer
        - runtime.md#rt-rte-standard-rag
        - runtime.md#rt-rte-ircot-retrieval
        - runtime.md#rt-rte-mcp-tools
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: These are pull operations, so their similarity, model judgment and exact-digest selectors
          do not classify a push signal.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: An unresolved read-back direction cannot be treated as pull-only, so push selection inputs
          remain unresolved. Accepted records inspect CacheOpenAI, not equivalent lifecycles for every
          adapter or injection.
      records:
      - runtime.md#rt-rte-retrieve-answer
      - runtime.md#rt-rte-standard-rag
      - runtime.md#rt-rte-ircot-retrieval
      - runtime.md#rt-rte-mcp-tools
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      note: No push signal is established. Known pull selectors do not warrant identifier, inferred-embedding
        or inferred-judgment here; opaque alternative directions prevent axis-level inapplicability.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Document-derived durable index writes including arbitrary caller content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-openie-state
        note: Automatic extraction/encoding and later consumers are wired, but accepted records do not
          establish whether arbitrary admitted content contains qualifying activity/experience traces.
          Document knowledge is not automatically trace learning.
      - scope: CacheOpenAI raw-response replay
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        note: The recorded wrapper retains/replays raw inference output, which alone does not establish
          a qualifying transformation. No canonical bounded-absence record supports a controlled no finding;
          neither yes nor no is assigned.
      - scope: IRCoT thought accumulation and benchmark score reporting
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-ircot-retrieval
        - epistemic.md#epi-rte-metric-evaluation
        note: 'These parts fall outside retained-memory writes: thoughts remain ordinary current-call
          state and metric results have no recorded retained later-consumer route. They cannot establish
          a system-wide negative.'
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Trace-fed transformations and later consumers of alternative caches/injected writes are
          not established. Accepted records inspect CacheOpenAI, not equivalent lifecycles for every adapter
          or injection.
      records:
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-rte-ircot-retrieval
      - epistemic.md#epi-rte-metric-evaluation
      note: No controlled trace-learning value is established by the accepted records. Unresolved input
        origins, the absence of canonical bounded-negative records, and alternative writes prevent complete
        assessment; parameter fixity and lack of measured improvement are not substitutes for trace-route
        assessment.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Document-derived writes with unresolved original input content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-index-state
        - runtime.md#rt-rte-offline-extraction
        - runtime.md#rt-rte-standard-rag
        - memory.md#mem-obj-passage-text
        - memory.md#mem-obj-openie-state
        note: Without recorded trace provenance for admitted content, no session-logs, tool-traces, event-streams
          or trajectories source is established. Imported documents alone are insufficient.
      - scope: Raw cache replay, current-call IRCoT and benchmark reporting
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-response-cache
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-ircot-retrieval
        - epistemic.md#epi-rte-metric-evaluation
        note: No qualifying write/source is established for raw replay; current-call thoughts and reported
          metrics are not retained updates. Lack of a canonical bounded-negative trace-learning warrant
          prevents assigning the combined unit inapplicable. Raw inference output is not thereby a tool-traces
          learning source.
      - scope: Other provider response caches and arbitrary injected persistence implementations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-reuse
        - runtime.md#rt-rte-standard-rag
        note: Original inputs to any qualifying alternative write remain uninspected. Accepted records
          inspect CacheOpenAI, not equivalent lifecycles for every adapter or injection.
      records:
      - runtime.md#rt-rte-index-state
      - runtime.md#rt-rte-offline-extraction
      - runtime.md#rt-rte-standard-rag
      - memory.md#mem-obj-passage-text
      - memory.md#mem-obj-openie-state
      - memory.md#mem-obj-response-cache
      - memory.md#mem-rte-response-reuse
      - runtime.md#rt-rte-ircot-retrieval
      - epistemic.md#epi-rte-metric-evaluation
      note: Source is unresolved rather than globally inapplicable because the included document-input
        and adapter alternatives do not have a completely assessed negative trace-learning boundary.
---

# HippoRAG memory profile

## Comparison rationale

The profile classifies accepted retained parts and consumer paths, not all runtime storage. The default stores separate original text, normalized symbolic strings and dense numerical representations. Graph and vector values describe access structures as well as their file-backed persistence. A stored embedding is not a model-weight update. See [MEM-OBJ-passage-embeddings](memory.md#mem-obj-passage-embeddings), [MEM-OBJ-fact-text](memory.md#mem-obj-fact-text) and [MEM-OBJ-graph-state](memory.md#mem-obj-graph-state).

The reconciliation supersedes the duplicate epistemic passage object with [MEM-OBJ-passage-text](memory.md#mem-obj-passage-text). All passage classifications cite that canonical record. The OpenIE container, extracted relation content, normalized text, vectors and graph remain distinct; no other supersession changes a value. The profile declares no records and adds no source evidence.

Behavioral authority follows each consumer. Text supplies knowledge; stored vectors, facts and graph affect ranking; saved coverage and source mappings route later work; manifest fields provide compatibility criteria and an enforcing veto. Metadata returned for display is not an instruction or an authorization control. Raw response replay supplies prior content to a requesting inference consumer. Neither reuse nor retention itself establishes learning authority. See [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest), [MEM-OBJ-chunk-metadata](memory.md#mem-obj-chunk-metadata) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

Extraction consolidates source material into a reduced search representation. Its semantic reliability is a separate question: the accepted epistemic record leaves entailment indeterminate. That uncertainty does not turn extraction errors into synthesis. Deduplication is supported by explicit triple removal rather than solely by primary-key acquisition checks. Metadata replacement evolves an entry. Physical deletion is forgetting (decay), not invalidation retaining a criticism history, and does not imply cache erasure. See [EPI-RTE-openie-generation](epistemic.md#epi-rte-openie-generation), [EPI-RTE-triple-admission](epistemic.md#epi-rte-triple-admission), [EPI-RTE-text-normalization](epistemic.md#epi-rte-text-normalization) and [MEM-OBJ-chunk-metadata](memory.md#mem-obj-chunk-metadata).

Explicit conditional user approval in [WF-RTE-folder-indexing](workflow.md#wf-rte-folder-indexing) supports claimed manual admission at that checkpoint only. It does not upgrade host adherence to wired or make downstream model/software admission manual. Generic caller identity leaves initial content control unresolved. Exact producer weights and opaque adapter lifecycles also remain unresolved rather than inferred from a default witness.

Requested selection remains pull even where similarity scoring and model judgment automatically select the returned content. Exact request-key replay is likewise not identifier-based push. Alternative cache routes are not completely inspected, so the signal axis is not globally inapplicable. See [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

Trace-learning coverage is deliberately local. Raw response replay and current-call thought accumulation do not establish a qualifying derived trace-fed write. Arbitrary imported document content has no recorded trace-origin inventory; treating it as necessarily static or necessarily a session log would add evidence. No canonical bounded-absence record supports a controlled no finding, so the trace-learning axis remains not-determinable. The trace-source axis cannot inherit a system-wide negative. No observed operation, beneficial learning or causal improvement is claimed.

Source-read log: none. This classification used only the supplied accepted members and reconciliation; no target-source ambiguity required an additional read.
