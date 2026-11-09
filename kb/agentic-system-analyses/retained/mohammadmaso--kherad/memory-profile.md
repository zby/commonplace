---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Kherad memory comparison of retained Git knowledge, relational retrieval state, saved conversations, specialist task content and administrator methods."
run-id: "AAS-2026-11-08-kherad-ac3e4da97ac6-01"
source-identity: "https://github.com/mohammadmaso/kherad"
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
memory-comparison:
  version: 2
  scope: "Retained raw sources, compiled concepts/index/log, copied source mirrors and historical versions; page/access metadata, search text/chunks/vectors; saved messages, specialist snapshots/drafts/replacements/uploads/statuses; administrator-admitted skills and their later consumers. Includes recorded acquisition, publication, restore, withdrawal, retrieval and replay alternatives. External provider/MCP retained state and dependency-level compaction remain unresolved where the records identify them. Excludes ephemeral pending maps as memory substrates, shipped static prompts, inference weights not shown to accumulate through use, and generic runtime configuration unrelated to these retained-content routes."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Raw sources, compiled concepts/index/log, source mirrors and version trees"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-compiled-docs"
                - "memory.md#mem-obj-source-mirror"
                - "memory.md#mem-rte-version-restore"
              note: "These operative Markdown objects persist as Git blobs, branches and history; repo describes their substrate rather than their Markdown encoding."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-compiled-docs"
            - "memory.md#mem-obj-source-mirror"
            - "memory.md#mem-rte-version-restore"
          note: "These operative Markdown objects persist as Git blobs, branches and history; repo describes their substrate rather than their Markdown encoding."
        -
          scope: "Page/access metadata, search projections, chunks/vectors, messages, specialist content and skills"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-chunk-content"
                - "memory.md#mem-obj-chunk-embedding"
                - "memory.md#mem-obj-message-parts"
                - "memory.md#mem-obj-session-content"
                - "runtime.md#rt-bap-session-skills"
              note: "Postgres stores these retained parts. pgvector is a column representation within the recorded relational substrate, not an independently recorded vector service."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-chunk-content"
            - "memory.md#mem-obj-chunk-embedding"
            - "memory.md#mem-obj-message-parts"
            - "memory.md#mem-obj-session-content"
            - "runtime.md#rt-bap-session-skills"
          note: "Postgres stores these retained parts. pgvector is a column representation within the recorded relational substrate, not an independently recorded vector service."
        -
          scope: "External provider-side and MCP retained state"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-message-parts"
          note: "Provider retention and remote payloads are opaque. Tool forwarding does not identify a retained object or its substrate; local storage findings do not classify them."
      records:
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-obj-compiled-docs"
        - "memory.md#mem-obj-source-mirror"
        - "memory.md#mem-rte-version-restore"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-chunk-content"
        - "memory.md#mem-obj-chunk-embedding"
        - "memory.md#mem-obj-message-parts"
        - "memory.md#mem-obj-session-content"
        - "runtime.md#rt-bap-session-skills"
        - "runtime.md#rt-rte-specialist-session"
      note: "Local retained content and access structures have recorded substrates. External provider/MCP retention is included as an unresolved alternative, not classified as local model weights."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source, mirror, compiled and session prose, conversation text, readable search chunks and skill instructions"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-source-mirror"
                - "memory.md#mem-obj-compiled-docs"
                - "memory.md#mem-obj-session-content"
                - "memory.md#mem-obj-message-parts"
                - "memory.md#mem-obj-chunk-content"
                - "memory.md#mem-obj-search-index"
                - "runtime.md#rt-bap-session-skills"
              note: "These parts reach human/model interpretation as text, not numerical weights or fixed-rule executable instructions."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-source-mirror"
            - "memory.md#mem-obj-compiled-docs"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-obj-message-parts"
            - "memory.md#mem-obj-chunk-content"
            - "memory.md#mem-obj-search-index"
            - "runtime.md#rt-bap-session-skills"
          note: "These parts reach human/model interpretation as text, not numerical weights or fixed-rule executable instructions."
        -
          scope: "Paths, page flags, frontmatter/access metadata, message selectors, session statuses and search token structures"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-compiled-docs"
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-session-content"
                - "memory.md#mem-obj-message-parts"
              note: "Localized metadata is interpreted by fixed application rules; prose parts of the same containers are classified separately."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-compiled-docs"
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-obj-message-parts"
          note: "Localized metadata is interpreted by fixed application rules; prose parts of the same containers are classified separately."
        -
          scope: "Stored embedding payload at cosine-distance consumer"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-embedding"
                - "memory.md#mem-rte-search-read"
              note: "Dense distributed numerical representations affect retrieval; readable chunk text is separate. Parametric here does not mean trained local model weights."
          records:
            - "memory.md#mem-obj-chunk-embedding"
            - "memory.md#mem-rte-search-read"
          note: "Dense distributed numerical representations affect retrieval; readable chunk text is separate. Parametric here does not mean trained local model weights."
        -
          scope: "Remote MCP content and provider-retained payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-message-parts"
          note: "Their encoding and later-consumption paths are not established by the accepted records."
      records:
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-obj-source-mirror"
        - "memory.md#mem-obj-compiled-docs"
        - "memory.md#mem-obj-session-content"
        - "memory.md#mem-obj-message-parts"
        - "memory.md#mem-obj-chunk-content"
        - "memory.md#mem-obj-search-index"
        - "runtime.md#rt-bap-session-skills"
        - "memory.md#mem-obj-chunk-embedding"
        - "memory.md#mem-rte-search-read"
        - "runtime.md#rt-rte-specialist-session"
      note: "Local prose, fixed-rule metadata and dense retrieval representations are separable. Opaque remote contents prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Administrator-supplied skills"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-admin-configuration"
                - "runtime.md#rt-bap-session-skills"
              note: "An administrator supplies and edits method text; no trace extraction is established for this path."
          records:
            - "runtime.md#rt-rte-admin-configuration"
            - "runtime.md#rt-bap-session-skills"
          note: "An administrator supplies and edits method text; no trace extraction is established for this path."
        -
          scope: "Raw/compiled content entering through uploads, specialist draft import or remote pull"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-document"
                - "runtime.md#rt-rte-source-authoring"
                - "runtime.md#rt-rte-remote-pull"
              note: "Import is a recorded acquisition path regardless of unresolved ultimate authorship."
          records:
            - "runtime.md#rt-rte-ingest-document"
            - "runtime.md#rt-rte-source-authoring"
            - "runtime.md#rt-rte-remote-pull"
          note: "Import is a recorded acquisition path regardless of unresolved ultimate authorship."
        -
          scope: "Local source-to-concept compilation, byte-copy mirrors, search projections, embedding outputs and session snapshot/recap derivations"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-indexer-compile"
                - "memory.md#mem-obj-source-mirror"
                - "memory.md#mem-rte-search-refresh"
                - "memory.md#mem-obj-session-content"
              note: "These are application/model derivations from selected content. The known derivation does not establish original source truth or exact embedding-model provenance."
          records:
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-obj-source-mirror"
            - "memory.md#mem-rte-search-refresh"
            - "memory.md#mem-obj-session-content"
          note: "These are application/model derivations from selected content. The known derivation does not establish original source truth or exact embedding-model provenance."
        -
          scope: "Automatically persisted conversational message parts"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-message-parts"
                - "runtime.md#rt-rte-bundle-chat"
                - "runtime.md#rt-rte-specialist-session"
              note: "Message retention is extracted from the conversation stream, including tool/display parts, not a compiled standing lesson."
          records:
            - "memory.md#mem-obj-message-parts"
            - "runtime.md#rt-rte-bundle-chat"
            - "runtime.md#rt-rte-specialist-session"
          note: "Message retention is extracted from the conversation stream, including tool/display parts, not a compiled standing lesson."
        -
          scope: "Initial corpus authorship, caller-supplied edits, remote upstream provenance and embedding-model training provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-rte-compiled-edit"
            - "memory.md#mem-obj-chunk-embedding"
            - "runtime.md#rt-cmp-embedding-model"
            - "runtime.md#rt-rte-remote-pull"
          note: "Generic caller identity and a configured embedding model leave these original derivation paths unresolved; known local transforms do not fill the gap."
      records:
        - "runtime.md#rt-rte-admin-configuration"
        - "runtime.md#rt-bap-session-skills"
        - "runtime.md#rt-rte-ingest-document"
        - "runtime.md#rt-rte-source-authoring"
        - "runtime.md#rt-rte-remote-pull"
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-obj-source-mirror"
        - "memory.md#mem-rte-search-refresh"
        - "memory.md#mem-obj-session-content"
        - "memory.md#mem-obj-message-parts"
        - "runtime.md#rt-rte-bundle-chat"
        - "runtime.md#rt-rte-specialist-session"
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-rte-compiled-edit"
        - "memory.md#mem-obj-chunk-embedding"
        - "runtime.md#rt-cmp-embedding-model"
      note: "Recorded authorship, imports and compilation paths coexist with unresolved initial corpus, numerical provenance and remote origins."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Source/mirror/compiled bodies, saved dialogue and effective session content at later model/editor reads"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-compiled-docs"
                - "memory.md#mem-obj-source-mirror"
                - "memory.md#mem-obj-session-content"
                - "memory.md#mem-rte-history-replay"
                - "memory.md#mem-rte-search-read"
                - "runtime.md#rt-bap-attached-pages"
              note: "These parts supply reference and context. Attachment preference does not convert factual page bodies into standing method instructions."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-compiled-docs"
            - "memory.md#mem-obj-source-mirror"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-rte-history-replay"
            - "memory.md#mem-rte-search-read"
            - "runtime.md#rt-bap-attached-pages"
          note: "These parts supply reference and context. Attachment preference does not convert factual page bodies into standing method instructions."
        -
          scope: "Retained skills at specialist instruction assembly"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-session-skills"
                - "runtime.md#rt-rte-admin-configuration"
              note: "The consumer is directed to apply skill text as its working method. Delivery does not establish compliance."
          records:
            - "runtime.md#rt-bap-session-skills"
            - "runtime.md#rt-rte-admin-configuration"
          note: "The consumer is directed to apply skill text as its working method. Delivery does not establish compliance."
        -
          scope: "Stored lexical index, chunk vectors and metadata at retrieval ordering/filter consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-chunk-embedding"
                - "memory.md#mem-rte-search-read"
              note: "Retained text features and vectors influence relative priority under fixed retrieval code; the algorithm need not itself be learned."
          records:
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-chunk-embedding"
            - "memory.md#mem-rte-search-read"
          note: "Retained text features and vectors influence relative priority under fixed retrieval code; the algorithm need not itself be learned."
        -
          scope: "Published mirror bytes/path inventory at compilation delta selection and directory at model navigation"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-mirror"
                - "runtime.md#rt-rte-indexer-compile"
                - "memory.md#mem-obj-compiled-docs"
              note: "Mirror differences choose full/delta/no-op work; the retained directory supplies navigation context for subsequent document choices."
          records:
            - "memory.md#mem-obj-source-mirror"
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-obj-compiled-docs"
          note: "Mirror differences choose full/delta/no-op work; the retained directory supplies navigation context for subsequent document choices."
        -
          scope: "Page access/deletion state and accepted/rejected edit statuses at gates and effective-body selection"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-session-content"
                - "memory.md#mem-rte-search-read"
                - "runtime.md#rt-rte-source-authoring"
              note: "Permissions/filter state and edit statuses determine eligible content. Rejected proposed bodies cannot become accepted overrides through the ordinary assembly path; manual saves remain separate."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-obj-session-content"
                - "memory.md#mem-rte-search-read"
                - "runtime.md#rt-rte-source-authoring"
              note: "Permissions/filter state and edit statuses determine eligible content. Rejected proposed bodies cannot become accepted overrides through the ordinary assembly path; manual saves remain separate."
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-rte-search-read"
            - "runtime.md#rt-rte-source-authoring"
          note: "Permissions/filter state and edit statuses determine eligible content. Rejected proposed bodies cannot become accepted overrides through the ordinary assembly path; manual saves remain separate."
        -
          scope: "Remote tool memory authority and trace-fed durable-update consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-obj-message-parts"
          note: "Remote consumers are opaque. Raw conversation retention and proposal persistence alone do not establish a learning-authority path from retained traces to a durable update."
      records:
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-obj-compiled-docs"
        - "memory.md#mem-obj-source-mirror"
        - "memory.md#mem-obj-session-content"
        - "memory.md#mem-rte-history-replay"
        - "memory.md#mem-rte-search-read"
        - "runtime.md#rt-bap-attached-pages"
        - "runtime.md#rt-bap-session-skills"
        - "runtime.md#rt-rte-admin-configuration"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-chunk-embedding"
        - "runtime.md#rt-rte-indexer-compile"
        - "runtime.md#rt-rte-source-authoring"
        - "runtime.md#rt-rte-specialist-session"
        - "memory.md#mem-obj-message-parts"
      note: "Retained content supplies knowledge, instructions, ranking, routing and admission criteria at distinct consumers. Remote effects and any trace-update learning consumer remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Indexer proposal/mirror commits, search derivation, conversation persistence and specialist draft/proposal admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-indexer-compile"
                - "memory.md#mem-rte-search-refresh"
                - "memory.md#mem-obj-message-parts"
                - "runtime.md#rt-rte-specialist-session"
                - "memory.md#mem-obj-session-content"
              note: "Software/model admits these retained parts without per-content human approval. Starting compilation or reindex does not make downstream admission manual."
          records:
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-rte-search-refresh"
            - "memory.md#mem-obj-message-parts"
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-session-content"
          note: "Software/model admits these retained parts without per-content human approval. Starting compilation or reindex does not make downstream admission manual."
        -
          scope: "Administrator skill edits and ordinary human MR publication decision"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-admin-configuration"
                - "runtime.md#rt-rte-review-merge"
                - "runtime.md#rt-bap-session-skills"
              note: "The administrator supplies method content; the ordinary reviewer explicitly approves/rejects publication. These decisions are separate from automatic proposal writes."
          records:
            - "runtime.md#rt-rte-admin-configuration"
            - "runtime.md#rt-rte-review-merge"
            - "runtime.md#rt-bap-session-skills"
          note: "The administrator supplies method content; the ordinary reviewer explicitly approves/rejects publication. These decisions are separate from automatic proposal writes."
        -
          scope: "Remote pull replacement after administrator trigger"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-remote-pull"
              note: "Software admits the configured remote tree without a per-document local approval decision; upstream remote authorship is not thereby resolved."
          records:
            - "runtime.md#rt-rte-remote-pull"
          note: "Software admits the configured remote tree without a per-document local approval decision; upstream remote authorship is not thereby resolved."
        -
          scope: "Generic caller raw saves/imports, compiled edits, version replacement and conflict resolutions; initial/remote content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-authoring"
            - "runtime.md#rt-rte-ingest-document"
            - "memory.md#mem-rte-compiled-edit"
            - "memory.md#mem-rte-version-restore"
            - "workflow.md#wf-rte-conflict-resolution"
            - "memory.md#mem-obj-source-pages"
          note: "These API mechanisms require authorized caller action, but the records explicitly do not establish a human decision for each supplied content body. Role permission or a route label alone cannot settle agency."
      records:
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-rte-search-refresh"
        - "memory.md#mem-obj-message-parts"
        - "runtime.md#rt-rte-specialist-session"
        - "memory.md#mem-obj-session-content"
        - "runtime.md#rt-rte-admin-configuration"
        - "runtime.md#rt-rte-review-merge"
        - "runtime.md#rt-bap-session-skills"
        - "runtime.md#rt-rte-remote-pull"
        - "runtime.md#rt-rte-source-authoring"
        - "runtime.md#rt-rte-ingest-document"
        - "memory.md#mem-rte-compiled-edit"
        - "memory.md#mem-rte-version-restore"
        - "workflow.md#wf-rte-conflict-resolution"
        - "memory.md#mem-obj-source-pages"
      note: "Software admissions and explicit administrator/reviewer decisions are supported. Generic authorized caller and remote authorship remain unresolved rather than being relabelled manual."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing compiled/source or effective section content revised through replacement paths"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-indexer-compile"
                - "memory.md#mem-rte-compiled-edit"
                - "memory.md#mem-obj-session-content"
              note: "Existing retained entries can be revised, including model-proposed and caller replacements. This does not imply semantic improvement."
          records:
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-rte-compiled-edit"
            - "memory.md#mem-obj-session-content"
          note: "Existing retained entries can be revised, including model-proposed and caller replacements. This does not imply semantic improvement."
        -
          scope: "Raw withdrawal and stale search-projection removal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-page-delete"
                - "memory.md#mem-obj-source-pages"
                - "memory.md#mem-rte-search-refresh"
              note: "Current reliance is withdrawn through live inventory/search filtering and stale projection deletion, while Git/history or derived copies can remain. This is bounded invalidation, not global erasure."
          records:
            - "epistemic.md#epi-rte-page-delete"
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-rte-search-refresh"
          note: "Current reliance is withdrawn through live inventory/search filtering and stale projection deletion, while Git/history or derived copies can remain. This is bounded invalidation, not global erasure."
        -
          scope: "Actual semantic effects of generated concepts/drafts and external maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-clm-source-fidelity"
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-compiled-docs"
          note: "No generated input/output pair decides whether compilation consolidates or creates a new claim. A command named compile and citation rewriting do not establish synthesis; remote maintenance is opaque."
      records:
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-rte-compiled-edit"
        - "memory.md#mem-obj-session-content"
        - "epistemic.md#epi-rte-page-delete"
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-rte-search-refresh"
        - "memory.md#mem-obj-compiled-docs"
        - "epistemic.md#epi-clm-source-fidelity"
        - "runtime.md#rt-rte-specialist-session"
      note: "Replacement and bounded withdrawal are implemented. The source-fidelity policy does not establish a controlled curation operation; unresolved semantic compilation effects and opaque alternatives prevent a complete inventory."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Model/user requested documents, search, sections/uploads, saved thread replay, editor/version reads and explicitly attached raw pages"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-search-read"
                - "memory.md#mem-rte-history-replay"
                - "memory.md#mem-rte-compiled-edit"
                - "memory.md#mem-rte-version-restore"
                - "memory.md#mem-obj-session-content"
                - "runtime.md#rt-bap-attached-pages"
              note: "These fulfil a consumer request for retained content. Automatic attachment assembly follows the user's explicit selection and is not an additional independent push."
          records:
            - "memory.md#mem-rte-search-read"
            - "memory.md#mem-rte-history-replay"
            - "memory.md#mem-rte-compiled-edit"
            - "memory.md#mem-rte-version-restore"
            - "memory.md#mem-obj-session-content"
            - "runtime.md#rt-bap-attached-pages"
          note: "These fulfil a consumer request for retained content. Automatic attachment assembly follows the user's explicit selection and is not an additional independent push."
        -
          scope: "Per-turn edit-status recap and compilation kickoff inventories/delta names"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-content"
                - "runtime.md#rt-rte-specialist-session"
                - "runtime.md#rt-rte-indexer-compile"
                - "memory.md#mem-obj-source-mirror"
              note: "Code supplies retained edit state and retained document/source baseline information without a separate model retrieval request."
          records:
            - "memory.md#mem-obj-session-content"
            - "runtime.md#rt-rte-specialist-session"
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-obj-source-mirror"
          note: "Code supplies retained edit state and retained document/source baseline information without a separate model retrieval request."
        -
          scope: "Default skill attachment selection, external SDK transformations and remote retained-content delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-session-skills"
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-message-parts"
          note: "Attached skills are loaded each turn but default-role versus explicit-attachment selection is not fully individuated. External transformations and remote consumers are not classified by the inspected pull routes."
      records:
        - "memory.md#mem-rte-search-read"
        - "memory.md#mem-rte-history-replay"
        - "memory.md#mem-rte-compiled-edit"
        - "memory.md#mem-rte-version-restore"
        - "memory.md#mem-obj-session-content"
        - "runtime.md#rt-bap-attached-pages"
        - "runtime.md#rt-rte-specialist-session"
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-obj-source-mirror"
        - "runtime.md#rt-bap-session-skills"
        - "memory.md#mem-obj-message-parts"
      note: "Requested document/search/history/attachment reads coexist with automatic task-context supply. External SDK/provider/MCP behavior remains unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Per-turn section-status recap and full compile inventory"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-content"
                - "runtime.md#rt-rte-specialist-session"
                - "runtime.md#rt-rte-indexer-compile"
              note: "Turn/run construction triggers supply of the session's status recap or bundle inventory; availability within the selected task scope is coarse selection, not semantic targeting."
          records:
            - "memory.md#mem-obj-session-content"
            - "runtime.md#rt-rte-specialist-session"
            - "runtime.md#rt-rte-indexer-compile"
          note: "Turn/run construction triggers supply of the session's status recap or bundle inventory; availability within the selected task scope is coarse selection, not semantic targeting."
        -
          scope: "Incremental compilation linked-document names"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-mirror"
                - "runtime.md#rt-rte-indexer-compile"
              note: "Compile trigger compares source bytes with retained mirrors; source/resource-link lookup selects related retained document names for kickoff. This is identifier matching of selected names, not an identifier merely attached to a requested file."
          records:
            - "memory.md#mem-obj-source-mirror"
            - "runtime.md#rt-rte-indexer-compile"
          note: "Compile trigger compares source bytes with retained mirrors; source/resource-link lookup selects related retained document names for kickoff. This is identifier matching of selected names, not an identifier merely attached to a requested file."
        -
          scope: "Default skill selection and external provider/MCP push alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-session-skills"
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-message-parts"
          note: "Records do not settle all unsolicited selection inputs or payloads. Requested semantic/keyword results cannot establish inferred push selection."
      records:
        - "memory.md#mem-obj-session-content"
        - "runtime.md#rt-rte-specialist-session"
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-obj-source-mirror"
        - "runtime.md#rt-bap-session-skills"
        - "memory.md#mem-obj-message-parts"
      note: "Signals are classified only for supported push operations, not for lexical/semantic search requested by the consumer. Other delivery branches retain uncertainty."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Local source compilation and search derivation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-indexer-compile"
            - "memory.md#mem-rte-search-refresh"
            - "memory.md#mem-obj-source-pages"
          note: "The recorded inputs are selected content, with mixed/unresolved origins. Model-produced source content alone does not establish that the qualifying write consumes traces; no complete negative is licensed either."
        -
          scope: "Saved conversations, specialist drafts/replacements and status recaps"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-message-parts"
            - "memory.md#mem-rte-history-replay"
            - "memory.md#mem-obj-session-content"
            - "runtime.md#rt-rte-specialist-session"
          note: "Raw replay is established, and automatic proposal persistence is established. Records do not identify a distinct automatic trace-fed durable update with its original trace input and later behavior-shaping consumption. A model output or task proposal is not by itself that chain."
        -
          scope: "Administrator methods, external provider updates, MCP and SDK compaction alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-admin-configuration"
            - "runtime.md#rt-bap-session-skills"
            - "runtime.md#rt-rte-specialist-session"
            - "runtime.md#rt-cmp-chat-model"
            - "memory.md#mem-obj-message-parts"
          note: "Manual method editing is not automatic trace learning. No bounded absence record covers all local or dependency alternatives; provider mutation and dependency compaction remain uninspected."
      records:
        - "runtime.md#rt-rte-indexer-compile"
        - "memory.md#mem-rte-search-refresh"
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-obj-message-parts"
        - "memory.md#mem-rte-history-replay"
        - "memory.md#mem-obj-session-content"
        - "runtime.md#rt-rte-specialist-session"
        - "runtime.md#rt-rte-admin-configuration"
        - "runtime.md#rt-bap-session-skills"
        - "runtime.md#rt-cmp-chat-model"
      note: "No accepted evidenced-absence record licenses a local or system-wide no. Recorded automatic writes do not fully establish an original trace-to-durable-behavior-shaping-output-to-later-consumer chain."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Compilation/search and specialist durable-update candidates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-pages"
            - "memory.md#mem-rte-search-refresh"
            - "memory.md#mem-obj-session-content"
            - "memory.md#mem-obj-message-parts"
            - "runtime.md#rt-rte-specialist-session"
          note: "Session dialogue is retained but its use as original input to a qualifying automatic durable update is not established in these records. Content imports and generated source provenance remain mixed; no trace-source value is inferred from serialization."
        -
          scope: "Provider/MCP/SDK update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-chat-model"
            - "runtime.md#rt-rte-specialist-session"
            - "memory.md#mem-obj-message-parts"
          note: "Original inputs to any external automatic update or compaction are not recorded, preventing classification rather than establishing absence."
      records:
        - "memory.md#mem-obj-source-pages"
        - "memory.md#mem-rte-search-refresh"
        - "memory.md#mem-obj-session-content"
        - "memory.md#mem-obj-message-parts"
        - "runtime.md#rt-rte-specialist-session"
        - "runtime.md#rt-cmp-chat-model"
      note: "Trace origin cannot be made inapplicable without a completely assessed absence of qualifying trace learning. Raw message storage does not by itself classify a learning route's original input."
---

# Kherad memory profile

## Comparison rationale

The profile separates retained Markdown from its access structures and consumers. Git is classified as a repository substrate, and Postgres/pgvector as relational storage. Dense chunk vectors have parametric representational form without being local model weights. Their actual force is ranking, whereas selected text supplies knowledge. The readable snippet is not a substitute for classifying its numerical selector. See [MEM-OBJ-chunk-embedding](memory.md#mem-obj-chunk-embedding), [MEM-OBJ-chunk-content](memory.md#mem-obj-chunk-content) and [MEM-RTE-search-read](memory.md#mem-rte-search-read).

Admission is mechanism-relative. Automatic proposal commits and projection writes coexist with explicit administrator method editing and ordinary human publication decisions. An authorized HTTP caller, remote-pull trigger or version choice does not establish per-content human approval. Default-branch publication is not a universal promotion finding or a factual-acceptance finding. See [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration), [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull) and [MEM-RTE-version-restore](memory.md#mem-rte-version-restore).

Reconciliation supersedes the epistemic compiled-edit route with [MEM-RTE-compiled-edit](memory.md#mem-rte-compiled-edit), and its version-restore route with [MEM-RTE-version-restore](memory.md#mem-rte-version-restore). Those are the canonical routes used here. Restore includes raw, legacy wiki and compiled OKF trees; the earlier raw framing cannot exclude compiled restoration. Combined epistemic object inventories do not supersede the memory member's separately classified raw sources, mirrors, concepts/index/log or session parts. No value is duplicated merely because two reports describe the same route.

Curation classifies implemented transformations, not requested behavior. Revision and bounded withdrawal have executable paths. The fidelity policy and proposal machinery do not establish source-to-concept consolidation, so no consolidation finding is emitted. This is a limitation of the accepted records' account of the semantic transformation, not a requirement for an observed run: an inspectable transformation could support a wired finding without execution evidence. Neither a compilation name nor a source URL establishes synthesis. The generated compilation/draft effects remain in the unresolved unit. Search rebuilds and embedding replacement are not independently labelled consolidation or deduplication. See [EPI-CLM-source-fidelity](epistemic.md#epi-clm-source-fidelity), [EPI-RTE-resource-rewrite](epistemic.md#epi-rte-resource-rewrite), [MEM-RTE-search-refresh](memory.md#mem-rte-search-refresh) and [EPI-RTE-page-delete](epistemic.md#epi-rte-page-delete).

Read-back separates requested retrieval from unsolicited task-state supply. Search similarity and keyword scoring do not become push signals merely because code selects results. Explicit page attachments and thread opening are requests. Per-turn edit recaps and compiler kickoff inventories are automatic supply; incremental resource lookup selects related document names, not necessarily complete document bodies. Coarse inventory supply and identifier-based delta targeting remain separate. See [MEM-RTE-search-read](memory.md#mem-rte-search-read), [MEM-RTE-history-replay](memory.md#mem-rte-history-replay), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages), [MEM-OBJ-session-content](memory.md#mem-obj-session-content), [MEM-OBJ-source-mirror](memory.md#mem-obj-source-mirror) and [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile).

The learning inventory is unresolved, not negative. Raw messages have a wired later replay route; retained proposals and method instructions also have consumers. Those facts alone do not establish the qualifying automatic trace-fed update. Initial corpus provenance, proposal-input lineage and provider/SDK alternatives remain incomplete in the accepted records, and no member declares an evidenced absence covering them. Consequently neither a local trace-learning "no" nor an inapplicable trace-source assessment is warranted. This is independent of whether retained content improves future capacity. See [MEM-OBJ-message-parts](memory.md#mem-obj-message-parts), [MEM-OBJ-session-content](memory.md#mem-obj-session-content), [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session) and [RT-BAP-session-skills](runtime.md#rt-bap-session-skills).

All positive classifications use implementation or declared-policy evidence, not observed operation or causal benefit. No frozen source files were reread: this mapping uses only the supplied accepted records and their annotations. Missing facts stay beside the affected units; opaque alternatives are not removed to manufacture complete coverage.
