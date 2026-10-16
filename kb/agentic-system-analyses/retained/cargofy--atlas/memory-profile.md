---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "ATLAS memory comparison: retained knowledge, operational records, progress metadata, browser replay and opaque alternatives at the frozen revision."
run-id: "AAS-2026-10-12-atlas-b28ea1ea613f-01"
source-identity: "https://github.com/cargofy/ATLAS"
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
memory-comparison:
  version: 2
  scope: "Included: use-created or changed Markdown knowledge and its path index, operational database payloads, extraction logs, connector/module checkpoints, browser conversation text/display metadata, and changed configuration insofar as it routes their acquisition or consumption. Provider-internal retention/context maintenance and unavailable external-module memory remain opaque included alternatives. Excluded: static shipped prompts, schema descriptions, unchanged setup instructions, external MCP-host memory, transient current-request tool blocks except as inputs to retained chat findings, nonpersisted derived query/diagnostic results, and model weights not established as accumulated ATLAS memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Markdown knowledge, attribution and contradiction parts; maintained path index"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "memory.md#mem-obj-contradiction-block"
              note: "Knowledge text is written to the shared host filesystem and subsequently read/indexed."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-contradiction-block"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-knowledge-edit"
          note: "Filesystem wiring resolves this store, not deployed mounts or survival."
        - scope: "Operational payloads, extraction-log rows and connector/module checkpoints on shipped entry points"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Both entry points initialize SQLite; its configured file or :memory: mode is still SQLite."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "runtime.md#rt-obj-atlas-db"
              note: "The source-defined :memory: fallback retains database state in process memory rather than a disk file."
          records:
            - "memory.md#mem-obj-record-payloads"
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
            - "runtime.md#rt-obj-atlas-db"
          note: "Both source-wired storage configurations are retained; the available PostgreSQL method is not a shipped bootstrap path."
        - scope: "Browser conversational text and display metadata"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
              note: "An ES-module singleton retains messages across navigation."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "No reload or cross-device persistence is established."
        - scope: "Changed memory-operation configuration reloaded by later startup or current consumers"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-reload"
              note: "Replacement YAML is written to config.yml and later reloaded."
          records:
            - "runtime.md#rt-rte-config-reload"
          note: "Only changed configuration affecting retained-data acquisition and consumption is included, not every shipped setting."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; storage substrate cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; storage substrate remains unresolved."
      records:
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-contradiction-block"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-rte-knowledge-edit"
        - "memory.md#mem-obj-record-payloads"
        - "memory.md#mem-obj-extract-log"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-obj-atlas-db"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-chat-tools"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "The files, SQLite variants, browser array and changed configuration cover the recorded local stores. Opaque provider and external-module alternatives prevent complete storage enumeration."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Knowledge assertions, attribution and contradiction warnings at model/human file consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "memory.md#mem-obj-contradiction-block"
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-rte-knowledge-edit"
              note: "Markdown text is interpreted as context, evidence and warnings by models or humans."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-contradiction-block"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-knowledge-edit"
          note: "Paths and dispatch envelopes are separated from file prose."
        - scope: "Knowledge paths and accumulated file index at discovery and selection consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-rte-knowledge-enrichment"
              note: "Literal paths address files; fixed code builds the index and scores path matches."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-rte-knowledge-enrichment"
          note: "A symbolic address is not the representational form of its addressed contents."
        - scope: "Operational IDs, fields, relations and JSON at SQL/JavaScript consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "epistemic.md#epi-rte-field-mapping"
              note: "Localized fields and equality/filter/mapping rules determine query and update behavior."
          records:
            - "memory.md#mem-obj-record-payloads"
            - "epistemic.md#epi-rte-field-mapping"
          note: "This consumption path is distinct from embedded free-text interpretation."
        - scope: "Operational embedded free text delivered as query evidence to model/human consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "runtime.md#rt-rte-chat-tools"
              note: "Embedded text in returned records can be interpreted by a model or human."
          records:
            - "memory.md#mem-obj-record-payloads"
            - "runtime.md#rt-rte-chat-tools"
          note: "The textual part does not make fixed SQL predicates natural-language computation."
        - scope: "Extraction-log hash, counts, errors and timestamps; connector/module checkpoint predicates"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Fixed predicates consume hashes, timestamps, IDs and JSON markers."
          records:
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
            - "runtime.md#rt-rte-extraction-summary"
          note: "Rendered log metadata becomes text only at the separate enrichment consumption path."
        - scope: "Extraction metadata rendered for the knowledge model"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
              note: "Filename, counts and time are rendered into a text summary supplied to enrichment."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-knowledge-enrichment"
          note: "The summary is not an opaque original-document payload or fact reconstruction."
        - scope: "Browser role/content history at provider consumption"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "Replayed user/assistant text is interpreted by the provider."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "Prior tool logs are excluded from this projection."
        - scope: "Browser role/display metadata and changed YAML routing configuration at fixed consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
                - "runtime.md#rt-rte-config-reload"
              note: "Role filtering and model/source configuration are consumed by fixed JavaScript rules."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
            - "runtime.md#rt-rte-config-reload"
          note: "Display previews do not classify the omitted prior tool payload at a later provider."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; form of retained material cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; form of retained material remains unresolved."
      records:
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-contradiction-block"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-chat-tools"
        - "memory.md#mem-obj-record-payloads"
        - "epistemic.md#epi-rte-field-mapping"
        - "memory.md#mem-obj-extract-log"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Mixed stores are split by operative part and consumption path. External model computation is parametric, but no accepted record establishes accumulated model weights as ATLAS memory; opaque retention cannot be upgraded to that value."
    lineage:
      assessment: "partial"
      units:
        - scope: "Explicit browser-authored knowledge and model-authored chat-save content"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-edit"
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-obj-knowledge"
              note: "Human editor content and chat-generated findings can be written to the shared file store."
          records:
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
          note: "This resolves those production paths, not the initial deployed KB or every generic API caller."
        - scope: "Knowledge compiled from raw text or extracted entities through the enrichment engine"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
                - "runtime.md#rt-rte-file-extraction"
              note: "The model transforms supplied text/entity summaries and selected files into mechanically admitted updates."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
            - "runtime.md#rt-rte-file-extraction"
          note: "Compilation provenance is wired even though semantic preservation, novelty and accuracy are indeterminate."
        - scope: "Knowledge derived from extraction-processing logs"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-obj-knowledge"
              note: "Recorded processing metadata feeds model-produced files subsequently eligible for chat/engine reads."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-obj-knowledge"
          note: "Original input is the extraction outcome metadata, not reconstructed document entities."
        - scope: "Operational imported and mapped records"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-import"
                - "memory.md#mem-obj-record-payloads"
              note: "Seed/connector records enter the retained database through mapping and upsert."
          records:
            - "runtime.md#rt-rte-record-import"
            - "memory.md#mem-obj-record-payloads"
            - "epistemic.md#epi-rte-field-mapping"
          note: "Field mapping can change interpretation; imported lineage is not preserved source warrant."
        - scope: "Operational model-extracted document records"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-file-extraction"
                - "memory.md#mem-obj-record-payloads"
              note: "A model converts document text into structured record candidates before software admission."
          records:
            - "runtime.md#rt-rte-file-extraction"
            - "memory.md#mem-obj-record-payloads"
          note: "No record establishes that all documents are activity traces; trace-extracted lineage is not inferred for this entire route."
        - scope: "Generated extraction logs and derived connector/module checkpoints"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Processing outcomes and module/connector runs generate retained metadata and progress markers."
          records:
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
          note: "These paths resolve generation, not the origin of an externally supplied initial checkpoint."
        - scope: "Browser history: directly supplied user turns and returned assistant/error text"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "User input and returned reply/error text populate the source-defined initially empty array."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "This is raw conversation retention, not a generated summary."
        - scope: "Initial operational KB/database content and generic API-supplied content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-record-payloads"
            - "runtime.md#rt-rte-knowledge-edit"
          note: "Deployment content/history and API caller provenance are unavailable. Known subsequent transformations cannot resolve initial lineage."
        - scope: "Changed YAML content supplied by generic configuration callers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-reload"
          note: "The replacement path is known, but caller identity and content derivation are not; authored versus imported/compiled provenance is unresolved."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; lineage cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; lineage remains unresolved."
      records:
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-chat-tools"
        - "runtime.md#rt-obj-knowledge"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-rte-file-extraction"
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-extract-log"
        - "runtime.md#rt-rte-record-import"
        - "memory.md#mem-obj-record-payloads"
        - "epistemic.md#epi-rte-field-mapping"
        - "memory.md#mem-obj-progress-state"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "The recorded authored, imported, compiled and trace-derived paths coexist. Initial content, generic callers and opaque alternatives prevent a complete provenance classification."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained knowledge prose and conflict warnings delivered to chat, enrichment and editor"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "memory.md#mem-obj-contradiction-block"
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-rte-knowledge-edit"
              note: "File contents and unresolved conflict warnings supply reference/context to models and human readers."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-contradiction-block"
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-knowledge-edit"
          note: "No trusted-source parser promotes arbitrary file prose into standing instruction or enforcing invalidation."
        - scope: "Retained knowledge text and paths at lexical enrichment selection"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "runtime.md#rt-rte-knowledge-enrichment"
              note: "Topic-path and content-keyword matches determine relative file scores."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "runtime.md#rt-rte-knowledge-enrichment"
          note: "Retained features influence ranking despite the fixed, unlearned scoring algorithm."
        - scope: "Retained knowledge context at automatic file-update generation"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-knowledge"
                - "runtime.md#rt-rte-knowledge-enrichment"
              note: "Existing selected files feed a model update that produces durable files for later consumers."
          records:
            - "runtime.md#rt-obj-knowledge"
            - "runtime.md#rt-rte-knowledge-enrichment"
          note: "Authority at this update consumer is separate from knowledge authority at subsequent readers; no improved capacity is claimed."
        - scope: "Operational payloads at query/model consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "runtime.md#rt-rte-chat-tools"
              note: "Returned rows supply indexed evidence to the calling model or host."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "runtime.md#rt-rte-mcp-query"
              note: "Retained JSON text supplies token-substring scores for ranked query results."
          records:
            - "memory.md#mem-obj-record-payloads"
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-rte-mcp-query"
          note: "Fixed result rules do not endorse source truth or establish an external host action."
        - scope: "Extraction-log hash/error/timestamp at processing and scheduled-enrichment selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-rte-extraction-summary"
                - "runtime.md#rt-rte-file-extraction"
              note: "Stored outcome metadata selects the next processing/enrichment input window."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-rte-file-extraction"
              note: "An existing hash causes extraction to skip unless force is passed, even for a failed prior extraction."
          records:
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-extraction-summary"
            - "runtime.md#rt-rte-file-extraction"
          note: "The enforced skip is not a factuality check or content acceptance criterion."
        - scope: "Extraction-log metadata at durable knowledge-update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-rte-extraction-summary"
                - "runtime.md#rt-rte-knowledge-enrichment"
              note: "Retained processing experience feeds automatic Markdown production for later chat/enrichment use."
          records:
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-extraction-summary"
            - "runtime.md#rt-rte-knowledge-enrichment"
          note: "This learning authority names the update path, not demonstrated improvement."
        - scope: "Connector/module checkpoints at next acquisition and maintenance invocation"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-progress-state"
                - "runtime.md#rt-rte-record-import"
                - "runtime.md#rt-rte-extraction-summary"
              note: "Retained cursors/modified-time/hash markers determine subsequent sources and input windows."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-progress-state"
              note: "Present hash or matching modified-time markers make built-in acquisition code skip processing."
          records:
            - "memory.md#mem-obj-progress-state"
            - "runtime.md#rt-rte-record-import"
            - "runtime.md#rt-rte-extraction-summary"
          note: "Markers influence fixed control flow, not model compliance; cursor failure semantics remain consequential."
        - scope: "Replayed browser history at subsequent chat model"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "Prior text supplies conversation context; earlier tool evidence is not included."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "History is not a verified evidence ledger or automatically revised standing guidance."
        - scope: "Changed acquisition/model configuration at current and later retained-data operations"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-reload"
              note: "Changed registry/source settings select model destinations and connector inputs."
          records:
            - "runtime.md#rt-rte-config-reload"
          note: "Old module references can survive reload, preventing universal immediate routing propagation."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; actual retained-part consumer and force cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; actual retained-part consumer and force remains unresolved."
      records:
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-contradiction-block"
        - "runtime.md#rt-rte-chat-tools"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-rte-knowledge-edit"
        - "memory.md#mem-obj-record-payloads"
        - "runtime.md#rt-rte-mcp-query"
        - "memory.md#mem-obj-extract-log"
        - "runtime.md#rt-rte-extraction-summary"
        - "runtime.md#rt-rte-file-extraction"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-record-import"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Knowledge, ranking, learning, routing and enforced skips are independently wired at named consumers. Static prompt/schema rules are excluded, so their instruction/validation force is not attributed to accumulated memory. Unknown provider/plugin consumers prevent a complete authority inventory."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Engine and scheduled-metadata knowledge admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-rte-extraction-summary"
              note: "Model proposals pass mechanical checks and reach the writer without per-content human approval."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-extraction-summary"
          note: "Starting enrichment or supplying text does not make returned updates manually admitted."
        - scope: "Chat save_knowledge admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
              note: "A model tool call directly admits replacement content through Atlas."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
          note: "No human content approver intervenes."
        - scope: "Browser editor save/delete admission"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-edit"
                - "runtime.md#rt-obj-knowledge"
              note: "An editor user explicitly supplies/edits and saves or deletes the retained file."
          records:
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-obj-knowledge"
          note: "This warranted human decision is confined to the browser route."
        - scope: "Generic direct KB API content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-obj-knowledge"
          note: "The same endpoint accepts generic callers; no record resolves a human decision versus software admission on this alternative."
        - scope: "Mapped/imported and model-extracted record admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-record-import"
                - "runtime.md#rt-rte-file-extraction"
                - "memory.md#mem-obj-record-payloads"
              note: "Software/model validation and upsert admit rows without per-record human approval."
          records:
            - "runtime.md#rt-rte-record-import"
            - "runtime.md#rt-rte-file-extraction"
            - "memory.md#mem-obj-record-payloads"
          note: "An explicit seed load or user upload initiates automatic subsequent admission."
        - scope: "Pipeline-log and built-in checkpoint admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Software derives and adopts outcome/log/checkpoint values without per-marker human approval."
          records:
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
          note: "Checkpoint use is not substituted for its evidenced generated-write mechanism."
        - scope: "Returned browser assistant/reply-error retention"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "The browser appends returned text without separate content approval."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "Software retention differs from explicit editor adoption."
        - scope: "Browser user-turn retention"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "The user explicitly supplies the text sent and retained as a user turn."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "User control over this content does not extend to returned replies or tool saves."
        - scope: "Administrative record pruning"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-record-pruning"
              note: "Age/status SQL predicates decide individual removals; a caller does not approve each row."
          records:
            - "memory.md#mem-rte-record-pruning"
          note: "Human initiation of cleanup is not manual per-row admission/withdrawal."
        - scope: "Initial retained content and generic changed-configuration admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-record-payloads"
            - "runtime.md#rt-rte-config-reload"
          note: "Initial deployment control and generic configuration caller identity are unavailable; manual/automatic cannot be assigned."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; write/admission agency cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; write/admission agency remains unresolved."
      records:
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-rte-extraction-summary"
        - "runtime.md#rt-rte-chat-tools"
        - "runtime.md#rt-obj-knowledge"
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-record-import"
        - "runtime.md#rt-rte-file-extraction"
        - "memory.md#mem-obj-record-payloads"
        - "memory.md#mem-obj-extract-log"
        - "memory.md#mem-obj-progress-state"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "memory.md#mem-rte-record-pruning"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Automatic model/software routes and explicit browser human decisions are distinct findings. Generic callers and initial/opaque admissions remain unresolved rather than inheriting another route’s agency."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Engine append, existing-path create and contradiction insertion on retained knowledge"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
                - "memory.md#mem-obj-contradiction-block"
                - "epistemic.md#epi-rte-contradiction-marking"
              note: "Appending/inserting warnings revises existing entries; create can replace an existing file."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-obj-contradiction-block"
            - "epistemic.md#epi-rte-contradiction-marking"
          note: "A contradiction warning revises retained prose but does not withdraw current reliance while retaining a version history."
        - scope: "Direct full-file KB replacements and deletion"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-edit"
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-obj-knowledge"
              note: "Editor/API and chat saves can replace existing retained content."
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-edit"
                - "runtime.md#rt-obj-knowledge"
              note: "Deletion forgets files for future discovery/read; earlier delivered context is not retracted."
          records:
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
          note: "Physical forgetting is decay, not historical invalidation."
        - scope: "ID-matched operational record replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-record-payloads"
                - "runtime.md#rt-rte-record-import"
                - "runtime.md#rt-rte-file-extraction"
              note: "Upsert replaces an existing record payload with new data."
          records:
            - "memory.md#mem-obj-record-payloads"
            - "runtime.md#rt-rte-record-import"
            - "runtime.md#rt-rte-file-extraction"
          note: "Replacement revises an entry; ID collision checks alone are not semantic deduplication."
        - scope: "Age/status-based operational row removal"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-record-pruning"
              note: "Pruning physically removes old closed shipments/related rows and expired rates."
          records:
            - "memory.md#mem-rte-record-pruning"
          note: "This removal does not invalidate derived Markdown or preserve a retired historical entry."
        - scope: "Reprocessing extraction-log entries"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extract-log"
              note: "Reprocessing replaces log fields and processed timestamp for a retained hash."
          records:
            - "memory.md#mem-obj-extract-log"
          note: "This is revision of retained outcome metadata, not merging near-duplicate facts."
        - scope: "Model-requested duplicate avoidance in enrichment"
          assessment: "partial"
          findings:
            - value: "dedup"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
              note: "The prompt requests skipping already-present information; no semantic admission check verifies that operation."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
          note: "Only requested duplicate avoidance is established. Actual content transformation cannot be classified without model outputs; it is not upgraded by wired file I/O."
        - scope: "Semantic consolidation or synthesis in model-generated enrichment and chat saves"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-extraction-summary"
            - "runtime.md#rt-rte-chat-tools"
          note: "No recorded input/output instance establishes reduction of existing claims or creation of a claim absent from inputs. Model opacity does not establish synthesis; first-ten-entity acquisition is not automatically consolidation of retained memory."
        - scope: "Checkpoint changes, raw conversation retention and changed routing settings as semantic curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-progress-state"
            - "memory.md#mem-obj-messages"
            - "runtime.md#rt-rte-config-reload"
          note: "Their recorded control/retention mechanisms do not establish a controlled semantic curation operation; pointer updates, acquisition and replay are not deduplication or consolidation by name."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; curation operation cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; curation operation remains unresolved."
      records:
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-contradiction-block"
        - "epistemic.md#epi-rte-contradiction-marking"
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-chat-tools"
        - "memory.md#mem-obj-record-payloads"
        - "runtime.md#rt-rte-record-import"
        - "runtime.md#rt-rte-file-extraction"
        - "memory.md#mem-rte-record-pruning"
        - "memory.md#mem-obj-extract-log"
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-progress-state"
        - "memory.md#mem-obj-messages"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Wired entry revision and forgetting coexist with claimed deduplication and unresolved model transformations. No accepted record supports enforced contradiction invalidation, promotion or synthesized new claims; the axis remains partial rather than declaring those values absent."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Engine relevant-file selection and provider delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
              note: "Once enrichment starts, software automatically selects and supplies retained whole files without the provider requesting those files."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
          note: "Explicit upstream workflow initiation does not make this selection a requested file return."
        - scope: "Chat automatic knowledge path-index delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-obj-knowledge"
              note: "Every chat invocation receives the current retained-file path inventory automatically."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
          note: "The index is selected/coarse availability metadata, not all file contents."
        - scope: "Chat requested full-file/tree/data reads and editor file reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-rte-knowledge-edit"
                - "memory.md#mem-obj-record-payloads"
              note: "Model or human requests a path/tree/data query and receives its retained result."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-rte-knowledge-edit"
            - "memory.md#mem-obj-record-payloads"
          note: "Returning a requested file is not another push just because code delivers it."
        - scope: "Browser automatic history projection into a later chat invocation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "On another send, software supplies the retained user/assistant history as context."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "The current new user message is not itself read-back; earlier tool-result payloads are omitted."
        - scope: "Scheduled automatic extraction-log selection and input delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Scheduled code selects eligible logs and supplies their metadata for model update without a per-entry consumer request."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
          note: "Cursor selection is an upstream operation distinct from engine selection of knowledge files."
        - scope: "Built-in acquisition accessors and next-run checkpoint reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-progress-state"
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-rte-file-extraction"
                - "runtime.md#rt-rte-record-import"
              note: "Processing code explicitly requests retained hash/ID/cursor values before fixed skip/fetch predicates."
          records:
            - "memory.md#mem-obj-progress-state"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-file-extraction"
            - "runtime.md#rt-rte-record-import"
          note: "These storage requests return control data to actual later software consumers."
        - scope: "Later current/startup configuration reload"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-reload"
              note: "Startup/reload explicitly loads retained configuration for routing consumers."
          records:
            - "runtime.md#rt-rte-config-reload"
          note: "Reload does not automatically refresh every already-constructed module reference."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; read-back operations cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; read-back operations remains unresolved."
      records:
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-obj-knowledge"
        - "runtime.md#rt-rte-chat-tools"
        - "runtime.md#rt-rte-knowledge-edit"
        - "memory.md#mem-obj-record-payloads"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-extract-log"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-file-extraction"
        - "runtime.md#rt-rte-record-import"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Recorded local routes establish both push and pull. Unknown provider and plugin alternatives remain included and prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Enrichment push of selected knowledge contents"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
              note: "Trigger is incoming text/extraction enrichment; topic/path and keyword/content substring scores select positive-scoring full files."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
              note: "The same selector applies five-file/character availability limits; the first oversized file can exceed its nominal budget."
          records:
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
          note: "Lexical targeting and coarse budget filtering are separate aspects of the same push. No actual identity equality match or embedding selector is established."
        - scope: "Chat automatic retained-path inventory push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-obj-knowledge"
              note: "At chat invocation, the full sorted Markdown path index is supplied by availability, with no targeted relevance predicate."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
          note: "Literal identifiers in catalog entries do not establish identifier-based push selection."
        - scope: "Browser prior user/assistant text push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-messages"
                - "memory.md#mem-rte-conversation-replay"
              note: "Another send triggers role filtering of all accumulated conversation text, not relevance or identity targeting."
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "Role projection excludes previous tool logs; no explicit history-size budget is recorded."
        - scope: "Scheduled metadata push to enrichment"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
                - "memory.md#mem-obj-progress-state"
              note: "Timer/manual sync selects successful logs newer than a cursor, oldest first and batch-limited; filename heuristics supply a topic for the downstream lexical selector."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "memory.md#mem-obj-progress-state"
          note: "Eligibility/time/window filters do not become identifier or inferred-judgment signals. Downstream knowledge selection is classified separately."
        - scope: "Requested knowledge/tree/database/checkpoint/configuration read returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-rte-knowledge-edit"
            - "memory.md#mem-obj-record-payloads"
            - "memory.md#mem-obj-progress-state"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-config-reload"
          note: "These operations fulfill explicit consumer requests; push signal does not classify a requested literal-path or ID read."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; push selection signal cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; push selection signal remains unresolved."
      records:
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-obj-knowledge"
        - "runtime.md#rt-rte-chat-tools"
        - "memory.md#mem-obj-messages"
        - "memory.md#mem-rte-conversation-replay"
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-extract-log"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-knowledge-edit"
        - "memory.md#mem-obj-record-payloads"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Coarse availability/window selection and inferred lexical targeting are wired. Pull-specific signals are inapplicable locally, but unresolved push alternatives prevent axis inapplicability or complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Scheduled extraction-log-to-Markdown update and later file consumer"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
                - "runtime.md#rt-rte-knowledge-enrichment"
                - "runtime.md#rt-obj-knowledge"
              note: "Automatic processing-metadata-fed writes produce retained knowledge eligible for later chat/enrichment consumption."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
          note: "This qualifying trace-fed artifact route requires neither new facts nor observed accuracy/improvement; actual execution remains unobserved."
        - scope: "Built-in trace-derived progress checkpoints at later acquisition consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-progress-state"
                - "runtime.md#rt-rte-record-import"
                - "runtime.md#rt-rte-extraction-summary"
              note: "Connector/module outcomes automatically produce durable hash/modified-time/cursor artifacts whose later reads change input selection and skip behavior."
          records:
            - "memory.md#mem-obj-progress-state"
            - "runtime.md#rt-rte-record-import"
            - "runtime.md#rt-rte-extraction-summary"
          note: "Derived control artifacts shape later behavior. This is distinct from retaining raw logs and from learned parameters or improved acquisition capacity."
        - scope: "Chat-generated saved findings from submitted history/current tool feedback"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
                - "runtime.md#rt-obj-knowledge"
              note: "The model consumes history/tool results, can automatically save derived findings, and later chats/engines can read those files."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "runtime.md#rt-obj-knowledge"
            - "memory.md#mem-rte-conversation-replay"
          note: "The trace-fed save branch is wired. A save may instead contain other supplied content; actual proposal provenance and content are unavailable, so this finding does not classify every chat save as trace learning."
        - scope: "Raw browser conversation retention and replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "The recorded mechanism retains and replays raw text rather than establishing a qualifying derived artifact. No canonical bounded-absence record warrants a resolved local no; the separate chat-save branch and opaque provider compaction cannot be excluded by this raw-replay account."
        - scope: "Entity/raw-text enrichment and operational document extraction with unspecified original input provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-file-extraction"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "memory.md#mem-obj-record-payloads"
          note: "The original documents/text are not established as activity traces for every route. Durable outputs are known, but qualifying trace-fed origin and any mixed inputs cannot be completely classified."
        - scope: "Generic API/editor/configuration content histories and initial content"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-rte-config-reload"
            - "runtime.md#rt-obj-knowledge"
          note: "Manual browser adoption is known locally; generic caller provenance and any trace-derived automatic alternative are unavailable."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; qualifying automatic trace-fed write and later consumer cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; qualifying automatic trace-fed write and later consumer remains unresolved."
      records:
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-extract-log"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-record-import"
        - "runtime.md#rt-rte-chat-tools"
        - "memory.md#mem-rte-conversation-replay"
        - "memory.md#mem-obj-messages"
        - "runtime.md#rt-rte-file-extraction"
        - "memory.md#mem-obj-record-payloads"
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-config-reload"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Qualifying scheduled metadata, derived progress and trace-fed chat-save branches establish positive existence. Raw replay supplies no qualifying positive or canonical bounded-absence warrant. Unknown origins/provider/plugins prevent a complete yes/no inventory; positive existence is not demonstrated learning benefit."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original processing-outcome input to scheduled log-derived knowledge"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-extraction-summary"
                - "memory.md#mem-obj-extract-log"
              note: "Discrete extraction runtime outcomes record filename/counts/time/errors; successful metadata entries feed automatic retained knowledge updates."
          records:
            - "runtime.md#rt-rte-extraction-summary"
            - "memory.md#mem-obj-extract-log"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-obj-knowledge"
          note: "Serialization into prose does not turn these processing events into source document facts or session logs."
        - scope: "Original connector/module run outcomes used to derive retained progress controls"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-progress-state"
                - "runtime.md#rt-rte-record-import"
                - "runtime.md#rt-rte-extraction-summary"
              note: "Processing and synchronization outcomes generate markers/cursors used by the next run."
          records:
            - "memory.md#mem-obj-progress-state"
            - "runtime.md#rt-rte-record-import"
            - "runtime.md#rt-rte-extraction-summary"
          note: "The qualifying source is runtime acquisition/maintenance experience, not imported document contents or a linked multi-step trajectory."
        - scope: "Trace-fed chat-save branch inputs"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
                - "memory.md#mem-rte-conversation-replay"
              note: "Submitted recorded user/assistant turns enter the model context from which saved findings can be produced."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-tools"
              note: "Current-run requested tool results and execution errors feed model continuation, which can save findings for later file consumers."
          records:
            - "runtime.md#rt-rte-chat-tools"
            - "memory.md#mem-rte-conversation-replay"
            - "runtime.md#rt-obj-knowledge"
          note: "Both trace content types are wired inputs; their use in a particular saved file and any mixed non-trace provenance are unavailable. Previous tool logs omitted by browser replay do not support later-session tool-trace delivery."
        - scope: "Raw browser replay write"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-messages"
            - "memory.md#mem-rte-conversation-replay"
          note: "Raw session-log retention alone does not establish a qualifying learning write. Without a canonical bounded-absence warrant for trace learning, source inapplicability cannot be concluded; the original input of any qualifying alternative remains unresolved."
        - scope: "Document/entity/raw-text enrichment input origins and generic automatic content alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-file-extraction"
            - "runtime.md#rt-rte-knowledge-enrichment"
            - "runtime.md#rt-rte-knowledge-edit"
            - "runtime.md#rt-rte-config-reload"
            - "memory.md#mem-obj-record-payloads"
          note: "No recorded origin classifies all included text/documents or generic caller content. Event, session, tool and static imported content cannot be universally distinguished."
        - scope: "Provider-internal accumulated state and context maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-llm-client"
            - "runtime.md#rt-rte-chat-tools"
          note: "Provider retention, caching and compaction are opaque; original qualifying trace input cannot be classified from the non-training client interface."
        - scope: "Additional retained state of unavailable external modules"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-lifecycle"
            - "memory.md#mem-obj-progress-state"
          note: "ModuleContext permits additional state and native effects, but external implementations are unavailable; original qualifying trace input remains unresolved."
      records:
        - "runtime.md#rt-rte-extraction-summary"
        - "memory.md#mem-obj-extract-log"
        - "runtime.md#rt-rte-knowledge-enrichment"
        - "runtime.md#rt-obj-knowledge"
        - "memory.md#mem-obj-progress-state"
        - "runtime.md#rt-rte-record-import"
        - "runtime.md#rt-rte-chat-tools"
        - "memory.md#mem-rte-conversation-replay"
        - "memory.md#mem-obj-messages"
        - "runtime.md#rt-rte-file-extraction"
        - "runtime.md#rt-rte-knowledge-edit"
        - "runtime.md#rt-rte-config-reload"
        - "memory.md#mem-obj-record-payloads"
        - "runtime.md#rt-cmp-llm-client"
        - "runtime.md#rt-rte-module-lifecycle"
      note: "Recorded runtime events and chat session/tool-feedback inputs have local warrants. These values describe qualifying writes, not all imported data. Unresolved qualifying routes and the lack of a resolved raw-replay learning absence keep the axis partial."
---

# ATLAS memory profile

## Comparison rationale

The comparison follows the accepted local object and route inventory, not all runtime storage. [MEM-OBJ-record-payloads](memory.md#mem-obj-record-payloads), [MEM-OBJ-extract-log](memory.md#mem-obj-extract-log) and [MEM-OBJ-progress-state](memory.md#mem-obj-progress-state) are distinct database parts. [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge) remains their separate filesystem counterpart; [MEM-OBJ-messages](memory.md#mem-obj-messages) is browser memory. Dynamic configuration is included only at its recorded later memory-operation routing consumers in [RT-RTE-config-reload](runtime.md#rt-rte-config-reload). Static schemas and chat instructions are not accumulated memory. Nonpersisted query calculations and developer diagnostic returns do not add stores or learning routes; see [EPI-RTE-derived-results](epistemic.md#epi-rte-derived-results) and [EPI-RTE-evaluator-tools](epistemic.md#epi-rte-evaluator-tools).

Reconciliation supersedes the duplicate epistemic contradiction object with [MEM-OBJ-contradiction-block](memory.md#mem-obj-contradiction-block). All classification citations use that canonical object; [EPI-RTE-contradiction-marking](epistemic.md#epi-rte-contradiction-marking) remains a distinct insertion route. The supersession changes no value. Conflict prose supplies a warning to readers, not an enforced withdrawal of either assertion. A returned applied flag can follow a missing-target no-op; neither that flag nor a model request for duplicate avoidance upgrades a transformation to observed execution. [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge) also prevents treating add-only policy as a universal preservation invariant.

Selection and requested return are different operations. [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) pushes lexically selected full files into an update prompt. [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools) pushes an availability index but pulls requested contents. A literal path on that pull or in the index does not establish identifier-targeted push. [MEM-RTE-conversation-replay](memory.md#mem-rte-conversation-replay) pushes retained role/content history while omitting prior tool-result evidence. Coarse filtering remains separate from lexical targeting and from actual content delivery.

Trace learning is a write-and-later-consumer classification, not a performance verdict. [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary) transforms retained runtime metadata into possible durable knowledge; it does not reconstruct extracted entities from counts. [MEM-OBJ-progress-state](memory.md#mem-obj-progress-state) also records automatically derived outcome checkpoints whose later use changes acquisition selection. Those generated control artifacts meet the trace-fed behavior-shaping boundary independently of natural-language knowledge. Raw log/history retention alone does not. The chat-save branch has a wired history/tool-feedback-to-file-to-later-reader chain in [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools); actual saved content and mixed input provenance remain unresolved. The raw-replay account does not supply a canonical bounded-absence warrant, so it establishes neither a resolved local no nor trace-source inapplicability. The positive union retains the separately warranted yes branches. None of these findings establishes improved future capacity or provider parameter training.

All axes remain partial because local positive witnesses do not resolve unavailable external module memory or provider-private retention/context management. [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle) and [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) bound these alternatives without classifying them from process capabilities or numerical model computation alone. Initial deployment content, generic caller identity, actual model outputs and semantic transformations remain local uncertainties. Known store wiring does not resolve those distinct lineage, agency or transformation questions. All positive implementation mappings are wired unless explicitly limited to claimed duplicate avoidance; no supplied record supports observed or causal memory benefit.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no frozen-source ambiguity required a direct source read. No records or new evidence were added.
