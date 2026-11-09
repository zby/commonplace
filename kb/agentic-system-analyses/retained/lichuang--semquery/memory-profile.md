---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "semquery memory comparison: persisted document retrieval, maintenance metadata, edited configuration and opaque component alternatives."
run-id: "AAS-2026-11-09-semquery-b21559990932-01"
source-identity: "https://github.com/lichuang/semquery"
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
memory-comparison:
  version: 2
  scope: "Use-admitted document chunks, lexical/vector access structures, ownership/freshness metadata, retained diagnostic logs, acquired caches and externally replaced saved configuration, with their default write/maintenance/later-consumer routes and unresolved injected alternatives. Excludes external document authorship as a shipped operation, downstream hosts, unchanged shipped prompt/default semantics, transient query rankings, prompts, answers and per-call inference contexts. Original provenance and opaque payloads remain local uncertainties, not exclusions that manufacture complete coverage."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Default retained corpus text, FTS terms, vectors and control/access metadata"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-vec-chunks"
                - "memory.md#mem-obj-document-paths"
              note: "All four parts reside in the reopened SQLite workspace; sqlite-vec is also a vector access structure."
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vec-chunks"
              note: "Persistent dense vectors are consumed by cosine-distance recall."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "memory.md#mem-obj-document-paths"
          note: "Inspected default storage is covered; the vector finding does not replace its SQLite substrate."
        -
          scope: "Saved externally replaceable configuration, diagnostic logs and acquired model-cache artifacts"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-system-prompt"
                - "memory.md#mem-obj-semq-log"
                - "runtime.md#rt-cmp-fast-embed"
                - "runtime.md#rt-cmp-fast-reranker"
                - "runtime.md#rt-cmp-gguf-llm"
              note: "Saved TOML, rotated logs and hub-cached model files are filesystem objects."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
            - "memory.md#mem-obj-semq-log"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "Only durable artifacts are classified, not transient parsed objects or inference contexts."
        -
          scope: "Caller-injected storage and provider-managed retained state"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-index-admission"
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "The extension interfaces establish replacements, not their deployed substrate or complete retained-state inventory."
      records:
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-vec-chunks"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-system-prompt"
        - "memory.md#mem-obj-semq-log"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-config-admission"
      note: "Default retained objects are accounted for; unknown injected implementation state prevents complete inventory coverage."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Retained chunk text at human/model consumption, saved replacement system text and diagnostics"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-system-prompt"
                - "memory.md#mem-obj-semq-log"
              note: "Text has consequences through human or model interpretation; diagnostic retention alone is not an automatic consumer route."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-system-prompt"
            - "memory.md#mem-obj-semq-log"
          note: "Static shipped default prompt text is excluded; a saved externally edited replacement is included."
        -
          scope: "Lexical access text, IDs, associations, maintenance metadata and symbolic configuration"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-document-paths"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-vec-chunks"
              note: "Fixed software rules consume segmented terms, identifiers, hashes, model specifications and numeric controls; vector IDs are symbolic, distinct from dense values."
          records:
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-document-paths"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-vec-chunks"
          note: "Localized fixed-rule fields are separate from natural-language chunks and distributed numerical state."
        -
          scope: "Retained dense chunk vectors and acquired model parameters"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vec-chunks"
                - "runtime.md#rt-cmp-fast-embed"
                - "runtime.md#rt-cmp-fast-reranker"
                - "runtime.md#rt-cmp-gguf-llm"
              note: "Dense representations and parameter-bearing cached models use distributed numerical form."
          records:
            - "memory.md#mem-obj-vec-chunks"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "Form is established without authenticating exact deployed model versions."
        -
          scope: "Injected component payloads and unsupplied cached tokenizer contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-admission"
            - "memory.md#mem-obj-document-paths"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "Their operative encodings are not established by configured names or model-version rows."
      records:
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-system-prompt"
        - "memory.md#mem-obj-semq-log"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-vec-chunks"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
        - "runtime.md#rt-rte-config-admission"
      note: "Known mixed parts remain separate; opaque alternative payloads prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Document slices acquired through readers"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "runtime.md#rt-rte-index-admission"
              note: "Retained slices originate in externally supplied documents, not semquery answer or execution traces."
          records:
            - "memory.md#mem-obj-chunks"
            - "runtime.md#rt-rte-index-admission"
          note: "Source extraction can lose structure; imported does not mean source truth or faithful original-file offsets."
        -
          scope: "Lexical, numerical and index metadata derivatives"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-vec-chunks"
                - "memory.md#mem-obj-document-paths"
                - "runtime.md#rt-rte-index-admission"
              note: "Code segments text, computes embeddings/hashes and constructs associations and successful-index baselines."
          records:
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "memory.md#mem-obj-document-paths"
            - "runtime.md#rt-rte-index-admission"
          note: "This names the inspected derivation path, not authenticated embedding-model provenance."
        -
          scope: "Saved configuration replacements and acquired model artifacts"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-system-prompt"
                - "runtime.md#rt-cmp-fast-embed"
                - "runtime.md#rt-cmp-fast-reranker"
                - "runtime.md#rt-cmp-gguf-llm"
              note: "Externally supplied controls/guidance and hub-acquired model files enter local retained state."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "External authorship and model training provenance remain unknown; imported lineage does not resolve those earlier paths."
        -
          scope: "Diagnostic retention"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semq-log"
              note: "Logger writes event, timing and error diagnostics from operation; these remain raw diagnostics, not learned guidance."
          records:
            - "memory.md#mem-obj-semq-log"
          note: "Origin in runtime activity is distinct from a qualifying trace-learning consumer."
        -
          scope: "Initial corpus authorship, exact embedding provenance and injected derivatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "Known extraction and import cannot identify original authors, actual loaded artifacts or custom derivation procedures."
      records:
        - "memory.md#mem-obj-chunks"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-vec-chunks"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-system-prompt"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
        - "memory.md#mem-obj-semq-log"
        - "runtime.md#rt-rte-config-admission"
      note: "Imported and compiled paths are supported, but initial and opaque provenance is not complete."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained chunk text supplied to search callers and chat context"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "runtime.md#rt-rte-hybrid-search"
                - "runtime.md#rt-rte-answer-generation"
              note: "Selected chunks provide reference/context for an answer; delivery is subject to suffix truncation."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "runtime.md#rt-rte-hybrid-search"
              note: "Raw retained chunk text is input to optional cross-encoder reranking."
          records:
            - "memory.md#mem-obj-chunks"
            - "runtime.md#rt-rte-hybrid-search"
            - "runtime.md#rt-rte-answer-generation"
          note: "Ranking and contextual use are different consumers; neither establishes factual acceptance or compliance."
        -
          scope: "Lexical terms and retained dense vectors at recall"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-vec-chunks"
                - "runtime.md#rt-rte-hybrid-search"
              note: "FTS terms and dense representations influence candidate priority before fusion."
          records:
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "runtime.md#rt-rte-hybrid-search"
          note: "No standing instruction or learned ranking policy is inferred from these inputs."
        -
          scope: "Maintenance metadata and symbolic saved controls"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-paths"
                - "memory.md#mem-obj-config"
                - "runtime.md#rt-rte-index-admission"
                - "runtime.md#rt-rte-config-admission"
              note: "Hashes, baselines and registrations select skip/reindex/cleanup scope; saved model and numeric controls select components and processing budgets."
          records:
            - "memory.md#mem-obj-document-paths"
            - "memory.md#mem-obj-config"
            - "runtime.md#rt-rte-index-admission"
            - "runtime.md#rt-rte-config-admission"
          note: "This classifies actual decision inputs, not a truth validator or universal access-control gate."
        -
          scope: "Externally replaced system-prompt text at GGUF inference"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-system-prompt"
                - "runtime.md#rt-rte-config-admission"
                - "runtime.md#rt-rte-answer-generation"
              note: "Saved literal system text supplies model-interpreted directions, conditional on surviving token truncation."
          records:
            - "memory.md#mem-obj-system-prompt"
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-rte-answer-generation"
          note: "The static default is not use-derived memory; a retained edited replacement has this wired route."
        -
          scope: "Diagnostic update consumers and opaque injected components"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semq-log"
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "No diagnostic-to-policy consumer is recorded; arbitrary injected consumer force is unknown. Parameter-bearing caches do not themselves establish an experience-update consumer."
      records:
        - "memory.md#mem-obj-chunks"
        - "runtime.md#rt-rte-hybrid-search"
        - "runtime.md#rt-rte-answer-generation"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-vec-chunks"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-config"
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-config-admission"
        - "memory.md#mem-obj-system-prompt"
        - "memory.md#mem-obj-semq-log"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
      note: "Supported knowledge, instruction, ranking and routing paths coexist with unresolved alternative consumers; no blanket learning authority is inferred."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Default extraction, chunk/vector/FTS admission, metadata maintenance and diagnostic writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-vec-chunks"
                - "memory.md#mem-obj-document-paths"
                - "memory.md#mem-obj-semq-log"
              note: "Software admits retained parts after workflow initiation without per-content human approval."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "memory.md#mem-obj-document-paths"
            - "memory.md#mem-obj-semq-log"
          note: "A user choosing add is not approving each extracted chunk or derived value."
        -
          scope: "Hub cache acquisition and automatic default config-file creation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-admission"
                - "memory.md#mem-obj-config"
                - "runtime.md#rt-cmp-fast-embed"
                - "runtime.md#rt-cmp-fast-reranker"
                - "runtime.md#rt-cmp-gguf-llm"
              note: "Software resolves/cache-loads artifacts and creates default configuration when missing."
          records:
            - "runtime.md#rt-rte-config-admission"
            - "memory.md#mem-obj-config"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "Automatic persistence is distinct from use-derived prompt revision; static default semantics are excluded from memory claims."
        -
          scope: "External document/config replacement and custom implementation admissions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
            - "runtime.md#rt-rte-config-admission"
          note: "Generic external author/caller identity does not establish an explicit human decision on each retained content item; manual is not warranted."
      records:
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-vec-chunks"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-semq-log"
        - "runtime.md#rt-rte-config-admission"
        - "memory.md#mem-obj-config"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
        - "memory.md#mem-obj-system-prompt"
      note: "Known automatic transformations do not resolve external initialization and replacement control."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Default shared-chunk deduplication"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-clm-chunk-lineage"
              note: "Content-hash reuse, INSERT OR IGNORE and many-to-many ownership collapse identical retained text."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-clm-chunk-lineage"
          note: "Deduplication is implemented; it does not preserve occurrence-specific byte ranges."
        -
          scope: "Default document withdrawal and orphan cleanup"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-document-paths"
                - "memory.md#mem-obj-fts-chunks"
                - "memory.md#mem-obj-vec-chunks"
              note: "Explicit removal and missing-file sweep forget solely owned indexed parts by unlinking and orphan deletion."
          records:
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-document-paths"
            - "memory.md#mem-obj-fts-chunks"
            - "memory.md#mem-obj-vec-chunks"
            - "memory.md#mem-clm-empty-retention"
          note: "This is deletion-based forgetting, not temporal downweighting or history-preserving invalidation. Shared chunks and skipped-empty files can remain; prefix sweep has a separate safety limit."
        -
          scope: "Externally edited controls/text and custom maintenance transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-rte-index-admission"
          note: "Replacement surfaces and injected traits do not establish which controlled transformations actually occur there; no implemented semantic synthesis is inferred from a route name."
      records:
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-clm-chunk-lineage"
        - "memory.md#mem-obj-document-paths"
        - "memory.md#mem-obj-fts-chunks"
        - "memory.md#mem-obj-vec-chunks"
        - "memory.md#mem-clm-empty-retention"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-system-prompt"
        - "runtime.md#rt-rte-config-admission"
      note: "Deduplication and forgetting are supported. Extraction, chunk slicing, primary-key checks alone and index rebuilding do not add consolidation, synthesis or promotion; opaque external transformations remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested corpus search/ask and requested maintenance/status operations"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-hybrid-search"
                - "runtime.md#rt-rte-answer-generation"
                - "runtime.md#rt-rte-index-admission"
                - "memory.md#mem-obj-document-paths"
              note: "Consumers request search/answer or maintenance; automatic selection and delivery fulfill those requests."
          records:
            - "runtime.md#rt-rte-hybrid-search"
            - "runtime.md#rt-rte-answer-generation"
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-document-paths"
          note: "The chain does not become push merely because code selects requested hits. Maintenance reads use accumulated hashes and links."
        -
          scope: "Saved configuration/cache loading at a later CLI open or lazy initialization"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-admission"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-system-prompt"
                - "runtime.md#rt-cmp-fast-embed"
                - "runtime.md#rt-cmp-fast-reranker"
                - "runtime.md#rt-cmp-gguf-llm"
              note: "The CLI/Engine requests saved configuration and model artifacts while opening or ensuring components."
          records:
            - "runtime.md#rt-rte-config-admission"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "This is loading requested retained inputs, not independent unsolicited passage delivery."
        -
          scope: "Diagnostic later consumers and custom component delivery policies"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semq-log"
            - "runtime.md#rt-rte-config-admission"
          note: "Operator access is potential only, and injected implementations have no established read-back policy."
      records:
        - "runtime.md#rt-rte-hybrid-search"
        - "runtime.md#rt-rte-answer-generation"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-document-paths"
        - "runtime.md#rt-rte-config-admission"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-system-prompt"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
        - "memory.md#mem-obj-semq-log"
      note: "Concrete routes are pull; no independently unsolicited route is established. Opaque alternatives prevent a complete pull-only boundary."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "Concrete requested corpus, maintenance, configuration and cache routes"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-hybrid-search"
            - "runtime.md#rt-rte-answer-generation"
            - "runtime.md#rt-rte-index-admission"
            - "memory.md#mem-obj-document-paths"
            - "runtime.md#rt-rte-config-admission"
          note: "Recorded operations fulfill requests rather than independently push memory. Query lexical/embedding scores are pull selectors, not push-signal findings."
        -
          scope: "Opaque injected routes and potential diagnostic consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-admission"
            - "memory.md#mem-obj-semq-log"
          note: "No qualifying push selection is established or boundedly excluded; no trigger/input/selected-part tuple can be classified."
      records:
        - "runtime.md#rt-rte-hybrid-search"
        - "runtime.md#rt-rte-answer-generation"
        - "runtime.md#rt-rte-index-admission"
        - "memory.md#mem-obj-document-paths"
        - "runtime.md#rt-rte-config-admission"
        - "memory.md#mem-obj-semq-log"
      note: "No controlled push-signal value is supported. A known requested search cannot make the unresolved alternatives inapplicable."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Default indexing, answer, diagnostic and configuration chains"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-index-admission"
            - "runtime.md#rt-rte-answer-generation"
            - "memory.md#mem-obj-semq-log"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-system-prompt"
          note: "Records describe document-fed representation writes, transient answers and raw logs, not a qualifying automatic trace-fed durable behavior-shaping update. No canonical evidenced-absence record licenses a local no."
        -
          scope: "Injected implementations, external configuration revision and opaque provider internals"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "No trace-fed update input, retained output and later consumer chain is established for these alternatives."
      records:
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-answer-generation"
        - "memory.md#mem-obj-semq-log"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-system-prompt"
        - "runtime.md#rt-rte-config-admission"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
      note: "No qualifying yes is supported and no evidenced-absence record supports no. Fixed inference parameters and absent observed improvement cannot substitute for either warrant."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Default diagnostic and document-derived writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semq-log"
            - "runtime.md#rt-rte-index-admission"
            - "runtime.md#rt-rte-answer-generation"
          note: "Raw diagnostic origin does not classify a learning source without a qualifying trace-fed update. Document ingestion alone does not establish any controlled trace origin."
        -
          scope: "External/injected or opaque update inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-admission"
            - "runtime.md#rt-cmp-fast-embed"
            - "runtime.md#rt-cmp-fast-reranker"
            - "runtime.md#rt-cmp-gguf-llm"
          note: "No qualifying write or original trace content is established; neither serialization nor configured model names resolves it."
      records:
        - "memory.md#mem-obj-semq-log"
        - "runtime.md#rt-rte-index-admission"
        - "runtime.md#rt-rte-answer-generation"
        - "runtime.md#rt-rte-config-admission"
        - "runtime.md#rt-cmp-fast-embed"
        - "runtime.md#rt-cmp-fast-reranker"
        - "runtime.md#rt-cmp-gguf-llm"
      note: "Qualifying learning inventory is unresolved, so trace source is not globally inapplicable and no trace-source positive is warranted."
---

# semquery memory profile

## Comparison rationale

This profile classifies accepted records, not a new source inspection. Reconciliation establishes no supersessions; the original declaring-member citations remain canonical. No source files were read for this profile, and no evidence or records were added.

The operative corpus is split into text, lexical terms, dense vectors and symbolic access/maintenance state. SQLite and vector storage coexist: a vector access structure is not a different claim about the physical database. Dense vectors are distributed-parametric representations, not model weights; the retained chunk text separately supplies reference content and reranker input. See [MEM-OBJ-chunks](memory.md#mem-obj-chunks), [MEM-OBJ-fts-chunks](memory.md#mem-obj-fts-chunks), [MEM-OBJ-vec-chunks](memory.md#mem-obj-vec-chunks) and [MEM-OBJ-document-paths](memory.md#mem-obj-document-paths).

Automatic selection within a requested search or ask is pull, not a second push operation. Thus lexical and embedding relevance signals are not asserted on the push-only signal axis. Concrete configuration/cache loads also fulfill component requests; unknown custom delivery mechanisms remain separate rather than borrowing their coverage. The recorded selector and context budget do not establish complete model visibility: GGUF can discard leading formatted tokens. See [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) and [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation).

The use-produced metadata has routing force at maintenance consumers. Content hashes and baseline specifications select processing rather than checking the truth of document claims. Similarly, citation filtering acts on transient answer metadata, not on a retained memory admission criterion; it adds no validation or enforcement finding for the memory inventory. See [MEM-OBJ-document-paths](memory.md#mem-obj-document-paths) and [EPI-RTE-marker-check](epistemic.md#epi-rte-marker-check).

Deduplication is implemented through shared text identity. Withdrawal supplies deletion-based forgetting, not history-preserving invalidation. These classifications retain the limits of shared ownership, stale empty-content transitions and differing cleanup predicates; they do not claim reliable mirroring or successful deletion in a run. Forced reembedding and rebuilds alone do not establish semantic consolidation or synthesis. See [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [MEM-CLM-chunk-lineage](memory.md#mem-clm-chunk-lineage) and [MEM-CLM-empty-retention](memory.md#mem-clm-empty-retention).

External saved configuration replacements can provide standing instructions, but unchanged shipped guidance is not accumulated memory. The wired consumer supports instruction authority conditionally on such a replacement, not observed editing or compliance. Unknown human involvement cannot be relabelled manual merely because the CLI has an operator. The automatic document admission mechanism is independently known. See [MEM-OBJ-config](memory.md#mem-obj-config), [MEM-OBJ-system-prompt](memory.md#mem-obj-system-prompt) and [RT-RTE-index-admission](runtime.md#rt-rte-index-admission).

No accepted evidenced-absence declaration covers the learning inventory. Reports' bounded statements that answers are not written back and logs are not used for automatic policy revision therefore do not license a controlled trace-learning "no". Nor does raw diagnostic retention establish "yes". Opaque injected implementations and external revisions remain unresolved, and trace source cannot be marked globally inapplicable. Exact model identity, tokenizer contents and initial authorship also remain local gaps, not reasons to discard known transformation findings. See [MEM-OBJ-semq-log](memory.md#mem-obj-semq-log), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [RT-CMP-fast-embed](runtime.md#rt-cmp-fast-embed), [RT-CMP-fast-reranker](runtime.md#rt-cmp-fast-reranker) and [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm).

All positive findings describe wiring. No observed consumer compliance, retrieval quality, improved capacity or causal benefit is inferred. Known form or substrate does not authenticate artifact provenance, and known automatic writes do not resolve every external admission decision.
