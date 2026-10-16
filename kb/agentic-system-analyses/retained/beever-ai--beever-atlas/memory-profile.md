---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Beever Atlas memory comparison: retained conversation-derived knowledge, wiki/control state, QA recall and recovery at the frozen source boundary."
run-id: "AAS-2026-10-15-beever-atlas-10a3512c094c-01"
source-identity: "https://github.com/Beever-AI/beever-atlas"
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
memory-comparison:
  version: 2
  scope: "Included: accumulated normalized messages; extracted facts/provenance/vectors and graph registry; topic/channel summaries; wiki content, cache, archives and curation controls; HTTP and reused MCP dialogue; retained ingestion checkpoints; use-modified model routing and retained evaluation/feedback state. Included unresolved alternatives: import/media origins, full compiler/modules/auto-builder, reconsolidation, migration and alternate adapters, dependency-owned session transformations and diagnostic consumers. Excluded: static shipped prompts, ordinary current-invocation working state, external clients' memory policies and provider-owned model weights/internal training."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Normalized channel messages, HTTP chat history, wiki page/cache/version objects and ingestion recovery checkpoints"
          assessment: "known"
          findings:
            -
              value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-wiki-page"
                - "runtime.md#rt-obj-session-state"
              note: "MongoDB collections retain these objects; document encoding does not make them relational tables or files."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-obj-session-state"
          note: "The accepted records identify MongoDB persistence for these operative parts, including the memory annotation on checkpointed runtime state."
        -
          scope: "Retained fact prose, fact metadata, text vectors, topic/channel summaries and searchable QA history"
          assessment: "known"
          findings:
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atomic-fact"
                - "memory.md#mem-obj-fact-metadata"
                - "memory.md#mem-obj-text-vector"
                - "memory.md#mem-obj-topic-cluster"
                - "memory.md#mem-obj-chat-history"
              note: "Weaviate/vector-store records retain prose, metadata, dense vectors and summaries, not only an ephemeral query embedding."
          records:
            - "memory.md#mem-obj-atomic-fact"
            - "memory.md#mem-obj-fact-metadata"
            - "memory.md#mem-obj-text-vector"
            - "memory.md#mem-obj-topic-cluster"
            - "memory.md#mem-obj-chat-history"
          note: "Classification follows the inspected vector-backed retained parts."
        -
          scope: "Persisted graph entities and relationships"
          assessment: "known"
          findings:
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-entity"
              note: "Nodes and relationships are persisted in the graph store and consumed by consolidation/wiki gathering."
          records:
            - "memory.md#mem-obj-graph-entity"
          note: "Graph persistence is established; adapter parity remains a separate unresolved alternative."
        -
          scope: "MCP conversation state reused by a later turn"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-ask"
                - "runtime.md#rt-obj-session-state"
              note: "Principal-namespaced ADK sessions survive individual MCP calls within the process."
          records:
            - "runtime.md#rt-rte-mcp-ask"
            - "runtime.md#rt-obj-session-state"
          note: "Only later-turn session reuse is included; ordinary current-run state is excluded."
        -
          scope: "Persisted model routing assignments and drift reports"
          assessment: "known"
          findings:
            -
              value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-model-assignment"
                - "epistemic.md#epi-obj-drift-report"
              note: "Assignments and optional drift reports are written to MongoDB for subsequent resolution or aggregation."
          records:
            - "runtime.md#rt-bap-model-assignment"
            - "epistemic.md#epi-obj-drift-report"
          note: "Configuration accumulated through use and retained diagnostic objects are included, not model weights."
        -
          scope: "Entity-registry backing details, alternate storage adapters, migration snapshots and all archived/shared copies"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-text-vector"
            - "memory.md#mem-obj-graph-entity"
            - "memory.md#mem-rte-channel-withdrawal"
          note: "The records locate these included parts but do not classify every backing object or backend alternative. No extra substrate is inferred."
      records:
        - "memory.md#mem-obj-channel-messages"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-obj-session-state"
        - "memory.md#mem-obj-atomic-fact"
        - "memory.md#mem-obj-fact-metadata"
        - "memory.md#mem-obj-text-vector"
        - "memory.md#mem-obj-topic-cluster"
        - "memory.md#mem-obj-graph-entity"
        - "runtime.md#rt-rte-mcp-ask"
        - "runtime.md#rt-bap-model-assignment"
        - "epistemic.md#epi-obj-drift-report"
        - "memory.md#mem-rte-channel-withdrawal"
      note: "The inventory covers messages, derived knowledge, controls, conversation/recovery state and diagnostics. Positive substrate witnesses do not establish backend or archive completeness."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source message prose; fact prose; graph names/descriptions; summary prose; wiki markdown/render content; retained user/assistant dialogue"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "memory.md#mem-obj-atomic-fact"
                - "memory.md#mem-obj-graph-entity"
                - "memory.md#mem-obj-topic-cluster"
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-chat-history"
              note: "These parts affect extraction, maintenance or answering through model/human interpretation."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-obj-atomic-fact"
            - "memory.md#mem-obj-graph-entity"
            - "memory.md#mem-obj-topic-cluster"
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-chat-history"
          note: "Content paths are separated from their access and control fields."
        -
          scope: "Message scheduling fields, fact access/lifecycle fields, graph node/edge identities, summary membership, wiki controls/schema, chat ownership and checkpoint stage keys"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "memory.md#mem-obj-fact-metadata"
                - "memory.md#mem-obj-graph-entity"
                - "memory.md#mem-obj-topic-cluster"
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-obj-session-state"
              note: "Localized identifiers and structured controls have fixed consumer rules for lookup, exclusion, grouping and stage skipping."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-obj-fact-metadata"
            - "memory.md#mem-obj-graph-entity"
            - "memory.md#mem-obj-topic-cluster"
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-obj-session-state"
          note: "Mixed objects contribute this finding only through their symbolic operative parts."
        -
          scope: "Persisted fact text vectors and entity name vectors"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-text-vector"
              note: "Dense distributed numerical representations supply similarity and dedup inputs; they are not provider weights."
          records:
            - "memory.md#mem-obj-text-vector"
          note: "Dense representation is classified independently of the vector/graph substrate."
        -
          scope: "Retained model assignments and drift-report metrics"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-model-assignment"
                - "epistemic.md#epi-obj-drift-report"
              note: "Consumer mappings, endpoint identifiers and localized metric fields have fixed resolver/aggregation semantics."
          records:
            - "runtime.md#rt-bap-model-assignment"
            - "epistemic.md#epi-obj-drift-report"
          note: "A floating-point metric is not distributed-parametric merely because it is numerical."
        -
          scope: "Full compiler/module payload consumption, alternative checkpoint variants and dependency-owned MCP compaction"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-obj-session-state"
            - "runtime.md#rt-rte-mcp-ask"
          note: "Records do not resolve every included payload or dependency transformation; readable display fields cannot classify an untraced consumed part."
      records:
        - "memory.md#mem-obj-channel-messages"
        - "memory.md#mem-obj-atomic-fact"
        - "memory.md#mem-obj-graph-entity"
        - "memory.md#mem-obj-topic-cluster"
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-fact-metadata"
        - "runtime.md#rt-obj-session-state"
        - "memory.md#mem-obj-text-vector"
        - "runtime.md#rt-bap-model-assignment"
        - "epistemic.md#epi-obj-drift-report"
        - "runtime.md#rt-rte-mcp-ask"
      note: "Natural-language, symbolic and dense numerical parts are split by consumption. Full compiler and dependency alternatives remain unresolved; provider parameters and static prompts are excluded."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Normalized source-message acquisition"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "memory.md#mem-clm-import-admission"
                - "runtime.md#rt-rte-message-ingestion"
              note: "Platform, signed push and file commit supply external material to durable message stores."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-clm-import-admission"
            - "runtime.md#rt-rte-message-ingestion"
          note: "Acquisition lineage is known; ultimate authorship and whether each input is an agent trace remain unresolved."
        -
          scope: "Conversation-derived fact/graph artifacts and successor topic/channel summaries and wiki content"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-message-ingestion"
                - "memory.md#mem-rte-summary-retention"
                - "runtime.md#rt-rte-wiki-maintenance"
              note: "Recorded conversations feed extraction; selected facts and graph enrichment feed retained summaries and wiki updates."
          records:
            - "runtime.md#rt-rte-message-ingestion"
            - "memory.md#mem-rte-summary-retention"
            - "runtime.md#rt-rte-wiki-maintenance"
          note: "The recorded conversation-derived route supports this lineage. Imported non-conversation alternatives and full compiler transformations are not thereby classified."
        -
          scope: "Generated HTTP answer retained in QA history"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-qa-answer"
                - "runtime.md#rt-rte-dashboard-ask"
              note: "QA generates query-conditioned answer prose that is then persisted; it is not solely a copied source message."
          records:
            - "epistemic.md#epi-obj-qa-answer"
            - "runtime.md#rt-rte-dashboard-ask"
          note: "Authored describes generated answer composition, not human admission or warranted truth."
        -
          scope: "Generated fact embeddings and checkpoint copies of completed-stage outputs"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-text-vector"
                - "runtime.md#rt-cmp-embedding-model"
                - "runtime.md#rt-obj-session-state"
              note: "Embedding maps text into dense vectors; checkpoint serialization retains selected prior stage artifacts without authoring a compact narrative."
          records:
            - "memory.md#mem-obj-text-vector"
            - "runtime.md#rt-cmp-embedding-model"
            - "runtime.md#rt-obj-session-state"
          note: "Known derivation paths coexist with unresolved existing-vector provenance and retry-provider alternatives."
        -
          scope: "Computed retained drift metrics"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-drift-comparison"
                - "epistemic.md#epi-obj-drift-report"
              note: "Distance/statistical computations derive retained evaluation metrics from compared output strings."
          records:
            - "epistemic.md#epi-rte-drift-comparison"
            - "epistemic.md#epi-obj-drift-report"
          note: "This is a computational derivation, not new authored team knowledge."
        -
          scope: "Ultimate initial message authorship, preexisting vector provenance, caller-authored controls/assignments and untraced full-builder alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-obj-text-vector"
            - "memory.md#mem-rte-wiki-refresh"
            - "runtime.md#rt-rte-page-curation"
            - "runtime.md#rt-rte-model-assignment"
          note: "Source labels and authenticated caller identities do not establish author/derivation provenance for every retained part."
      records:
        - "memory.md#mem-obj-channel-messages"
        - "memory.md#mem-clm-import-admission"
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "epistemic.md#epi-obj-qa-answer"
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-obj-text-vector"
        - "runtime.md#rt-cmp-embedding-model"
        - "runtime.md#rt-obj-session-state"
        - "epistemic.md#epi-rte-drift-comparison"
        - "epistemic.md#epi-obj-drift-report"
        - "memory.md#mem-rte-wiki-refresh"
        - "runtime.md#rt-rte-page-curation"
        - "runtime.md#rt-rte-model-assignment"
      note: "Known import, extraction, composition and computational derivations remain local. Initial provenance and alternative compiler paths prevent a complete lineage inventory."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Message/fact/graph/summary/wiki content at extraction, consolidation, wiki generation and QA/human consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "memory.md#mem-obj-atomic-fact"
                - "memory.md#mem-obj-graph-entity"
                - "memory.md#mem-obj-topic-cluster"
                - "memory.md#mem-rte-knowledge-retrieval"
              note: "Retained content supplies source evidence, reference or context to these consumers."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-obj-atomic-fact"
            - "memory.md#mem-obj-graph-entity"
            - "memory.md#mem-obj-topic-cluster"
            - "memory.md#mem-rte-knowledge-retrieval"
          note: "Knowledge authority is advisory/contextual; it does not establish source truth or model compliance."
        -
          scope: "Retained conversation evidence and derived facts at automatic fact/summary/wiki update consumers"
          assessment: "partial"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-message-ingestion"
                - "memory.md#mem-rte-summary-retention"
                - "runtime.md#rt-rte-wiki-maintenance"
                - "memory.md#mem-rte-knowledge-retrieval"
              note: "Retained conversational experience feeds durable behavior-shaping fact/summary/page artifacts used in later answering and maintenance."
          records:
            - "runtime.md#rt-rte-message-ingestion"
            - "memory.md#mem-rte-summary-retention"
            - "runtime.md#rt-rte-wiki-maintenance"
            - "memory.md#mem-rte-knowledge-retrieval"
          note: "Learning authority is at the update consumer; downstream output knowledge authority is a different path. No capacity improvement is claimed."
        -
          scope: "Fact prose/vectors, name vectors and fact quality scores at retrieval, dedup candidate selection and summary context ordering"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-text-vector"
                - "memory.md#mem-obj-fact-metadata"
                - "memory.md#mem-rte-knowledge-retrieval"
                - "memory.md#mem-rte-summary-retention"
              note: "Retained content/features affect relative retrieval priority, similarity candidates and quality-sorted top-fact selection."
          records:
            - "memory.md#mem-obj-text-vector"
            - "memory.md#mem-obj-fact-metadata"
            - "memory.md#mem-rte-knowledge-retrieval"
            - "memory.md#mem-rte-summary-retention"
          note: "Fixed ranking code still gives retained scoring inputs ranking authority."
        -
          scope: "Fact invalidation and supersession fields at guarded retrieval/consolidation consumers"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-bap-fact-lifecycle"
                - "epistemic.md#epi-rte-fact-supersession"
              note: "Persisted lifecycle fields cause deterministic exclusion on participating semantic/hybrid and consolidation branches."
          records:
            - "memory.md#mem-bap-fact-lifecycle"
            - "epistemic.md#epi-rte-fact-supersession"
          note: "BM25 and explicit superseded/ID reads remain counterexamples to universal exclusion."
        -
          scope: "Retained page curation controls at incremental maintainer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-page-curation"
                - "runtime.md#rt-rte-page-curation"
              note: "Manual/frozen state prevents the covered automatic rewrite from running."
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-page-curation"
                - "runtime.md#rt-rte-page-curation"
              note: "Auto/manual/frozen state selects the covered automatic, deferred or skipped update path."
          records:
            - "runtime.md#rt-bap-page-curation"
            - "runtime.md#rt-rte-page-curation"
          note: "These forces apply at the incremental consumer, not all full-refresh writers."
        -
          scope: "Retained rejected entity pairs at cosine dedup admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-dedup"
              note: "The rejected-pair registry supplies a criterion checked before cosine-tier merging."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-dedup"
              note: "A matched rejected pair vetoes the cosine-tier merge."
          records:
            - "epistemic.md#epi-rte-entity-dedup"
          note: "Exact-name collisions bypass this registry lookup; the veto is branch-specific."
        -
          scope: "Checkpoint stage identity, persisted model assignments and message extraction status at their later executors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-state"
                - "runtime.md#rt-bap-model-assignment"
                - "runtime.md#rt-rte-message-ingestion"
              note: "Checkpoint state selects skipped stages, assignments select model endpoints, and pending status selects later extraction work."
          records:
            - "runtime.md#rt-obj-session-state"
            - "runtime.md#rt-bap-model-assignment"
            - "runtime.md#rt-rte-message-ingestion"
          note: "This is selection of operations/input windows, not retained natural-language instruction."
        -
          scope: "Retained HTTP dialogue and searchable prior answers at subsequent QA model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-rte-dashboard-ask"
              note: "Earlier content is supplied as prior conversation or requested past QA evidence."
          records:
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-rte-dashboard-ask"
          note: "Only dialogue content is reconstructed by the HTTP loader; stored thinking/tool traces are not all supplied."
        -
          scope: "Feedback/drift downstream adoption, complete module payload consumers, and dependency-managed session transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-clm-evaluation-authority"
            - "epistemic.md#epi-rte-drift-comparison"
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-rte-mcp-ask"
          note: "Retained reports do not establish instruction, learning or other force at an untraced later consumer. Full consumer inventory is unresolved."
      records:
        - "memory.md#mem-obj-channel-messages"
        - "memory.md#mem-obj-atomic-fact"
        - "memory.md#mem-obj-graph-entity"
        - "memory.md#mem-obj-topic-cluster"
        - "memory.md#mem-rte-knowledge-retrieval"
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-obj-text-vector"
        - "memory.md#mem-obj-fact-metadata"
        - "memory.md#mem-bap-fact-lifecycle"
        - "epistemic.md#epi-rte-fact-supersession"
        - "runtime.md#rt-bap-page-curation"
        - "runtime.md#rt-rte-page-curation"
        - "epistemic.md#epi-rte-entity-dedup"
        - "runtime.md#rt-obj-session-state"
        - "runtime.md#rt-bap-model-assignment"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-clm-evaluation-authority"
        - "epistemic.md#epi-rte-drift-comparison"
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-rte-mcp-ask"
      note: "Separate retained parts and actual consumers support knowledge, learning, ranking, enforcement, validation and routing. Static shipped instructions are outside scope; no instruction finding is inferred from delivery alone."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Derived fact/graph admission, summary retention, incremental wiki updates and generated full-build persistence"
          assessment: "partial"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-message-ingestion"
                - "epistemic.md#epi-rte-quality-admission"
                - "epistemic.md#epi-rte-entity-dedup"
                - "memory.md#mem-rte-summary-retention"
                - "runtime.md#rt-rte-wiki-maintenance"
                - "epistemic.md#epi-rte-builder-retention"
              note: "Models propose and software gates/parsers/persistence admit derived artifacts without an explicit human decision on each retained content item."
          records:
            - "runtime.md#rt-rte-message-ingestion"
            - "epistemic.md#epi-rte-quality-admission"
            - "epistemic.md#epi-rte-entity-dedup"
            - "memory.md#mem-rte-summary-retention"
            - "runtime.md#rt-rte-wiki-maintenance"
            - "epistemic.md#epi-rte-builder-retention"
          note: "Initiating sync/refresh is not per-content human approval; full compiler branch coverage remains incomplete."
        -
          scope: "HTTP dialogue/answer persistence and selected-stage checkpoint saves"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-qa-answer"
                - "runtime.md#rt-rte-dashboard-ask"
                - "runtime.md#rt-obj-session-state"
              note: "Software writes generated/history content and whitelisted intermediate artifacts for later QA/retry consumption."
          records:
            - "epistemic.md#epi-obj-qa-answer"
            - "runtime.md#rt-rte-dashboard-ask"
            - "runtime.md#rt-obj-session-state"
          note: "Known host-owned writes are separate from the human or computational origin of user messages."
        -
          scope: "Fact supersession and drift-report storage"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-supersession"
                - "epistemic.md#epi-rte-drift-comparison"
              note: "Threshold code mutates lifecycle fields and comparator code writes diagnostic metrics without per-result operator approval."
          records:
            - "memory.md#mem-rte-fact-supersession"
            - "epistemic.md#epi-rte-drift-comparison"
          note: "Software admission is established even though actual execution is unobserved."
        -
          scope: "Initial raw acquisition, file upload/commit, curation/structural changes, purge and model-assignment requests"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-clm-import-admission"
            - "memory.md#mem-obj-channel-messages"
            - "runtime.md#rt-rte-page-curation"
            - "memory.md#mem-rte-channel-withdrawal"
            - "runtime.md#rt-rte-model-assignment"
          note: "Explicit caller selection is established, but caller identity is not enough to decide human versus software admission. No manual value is inferred."
        -
          scope: "Remaining compiler/auto-builder, embedding-migration and retry-provider admission variants"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-wiki-refresh"
            - "memory.md#mem-obj-text-vector"
            - "runtime.md#rt-obj-session-state"
          note: "Inspected automatic witnesses do not resolve all alternative admission mechanisms."
      records:
        - "runtime.md#rt-rte-message-ingestion"
        - "epistemic.md#epi-rte-quality-admission"
        - "epistemic.md#epi-rte-entity-dedup"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "epistemic.md#epi-rte-builder-retention"
        - "epistemic.md#epi-obj-qa-answer"
        - "runtime.md#rt-rte-dashboard-ask"
        - "runtime.md#rt-obj-session-state"
        - "memory.md#mem-rte-fact-supersession"
        - "epistemic.md#epi-rte-drift-comparison"
        - "memory.md#mem-clm-import-admission"
        - "memory.md#mem-obj-channel-messages"
        - "runtime.md#rt-rte-page-curation"
        - "memory.md#mem-rte-channel-withdrawal"
        - "runtime.md#rt-rte-model-assignment"
        - "memory.md#mem-rte-wiki-refresh"
        - "memory.md#mem-obj-text-vector"
      note: "Automatic derived-content and host-retention mechanisms are supported. Initial/caller-origin decisions and incompletely inspected writers prevent complete agency classification."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Retained conversations to standing facts, and selected member facts to retained topic/channel summaries"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-message-ingestion"
                - "memory.md#mem-obj-atomic-fact"
                - "memory.md#mem-rte-summary-retention"
              note: "Extraction reduces retained conversation content to standing facts; summarization compresses selected facts into a reduced retained representation."
          records:
            - "runtime.md#rt-rte-message-ingestion"
            - "memory.md#mem-obj-atomic-fact"
            - "memory.md#mem-rte-summary-retention"
          note: "The implemented extract/summary routes support consolidation; unknown fidelity does not by itself establish synthesis."
        -
          scope: "Incremental wiki section update"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-maintenance"
              note: "New fact context revises affected sections of an existing retained page while preserving untouched sections."
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
          note: "Known merge/save behavior does not classify every full-build alternative."
        -
          scope: "Entity reconciliation against retained prior identities and registry"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-dedup"
                - "memory.md#mem-obj-graph-entity"
              note: "Normalized-name/cosine matching merges aliases/properties and rewrites relationship endpoints to canonical identities."
          records:
            - "epistemic.md#epi-rte-entity-dedup"
            - "memory.md#mem-obj-graph-entity"
          note: "Implemented merging supports dedup despite possible mistaken coreference; ambiguous fallback is not a model judgment."
        -
          scope: "Temporal fact supersession"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-supersession"
                - "memory.md#mem-bap-fact-lifecycle"
              note: "Old facts remain retained with invalidation/successor fields that withdraw reliance at guarded consumers."
          records:
            - "memory.md#mem-rte-fact-supersession"
            - "memory.md#mem-bap-fact-lifecycle"
          note: "This is bounded withdrawal, not full erasure; ordinary BM25 can still return an invalid fact."
        -
          scope: "Channel hard purge"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-withdrawal"
              note: "Successful covered deletion forgets retained knowledge/history rather than merely hiding a page or resetting extraction state."
          records:
            - "memory.md#mem-rte-channel-withdrawal"
          note: "Decay here uses the controlled forgetting sense, not an inferred time-based decay policy. Partial failures and archives bound erasure."
        -
          scope: "Complete full-build semantic transformations, reconsolidation, migration and diagnostic-driven revision alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-wiki-refresh"
            - "memory.md#mem-rte-summary-retention"
            - "memory.md#mem-obj-text-vector"
            - "memory.md#mem-clm-evaluation-authority"
            - "epistemic.md#epi-rte-compiler-retry"
          note: "No uniform synthesize/promote or additional operation follows from a route name, generated prose, index rebuild or a requested repair. Untraced transformations remain unresolved."
      records:
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-obj-atomic-fact"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "epistemic.md#epi-rte-entity-dedup"
        - "memory.md#mem-obj-graph-entity"
        - "memory.md#mem-rte-fact-supersession"
        - "memory.md#mem-bap-fact-lifecycle"
        - "memory.md#mem-rte-channel-withdrawal"
        - "memory.md#mem-rte-wiki-refresh"
        - "memory.md#mem-obj-text-vector"
        - "memory.md#mem-clm-evaluation-authority"
        - "epistemic.md#epi-rte-compiler-retry"
      note: "The inventory retains concrete consolidation, revision, deduplication, invalidation and forgetting mechanisms. Compiler semantics and alternative maintenance routes prevent a complete operation classification."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested facts, provenance, summaries, wiki pages and past QA through QA tools/API/MCP"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-knowledge-retrieval"
              note: "A model/caller requests retained material; embedding/reranking fulfills that request rather than creating an independent push."
          records:
            - "memory.md#mem-rte-knowledge-retrieval"
          note: "The inspected requested tool family is resolved; granular selector internals remain a separate included limitation."
        -
          scope: "HTTP prior-dialogue assembly into a fresh QA turn"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dashboard-ask"
                - "memory.md#mem-obj-chat-history"
              note: "Host automatically loads a session tail and injects it into context without a model request for those messages."
          records:
            - "runtime.md#rt-rte-dashboard-ask"
            - "memory.md#mem-obj-chat-history"
          note: "An upstream supplied session identity determines the automatic selection input; only content from up to ten stored messages is replayed."
        -
          scope: "Event-driven incremental wiki completion input"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-maintenance"
              note: "The event chain selects new facts/current page and supplies them to the maintainer without a maintainer retrieval request."
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
          note: "Push is into the maintenance consumer, not unsolicited knowledge injection into every future QA turn."
        -
          scope: "Summary context production from dirty/touched clusters"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-retention"
              note: "Code selects retained active high-quality member facts and graph context for the summarizer automatically."
          records:
            - "memory.md#mem-rte-summary-retention"
          note: "The context builder caps fetched members and selected facts before supplying the model."
        -
          scope: "Checkpoint restoration into a fresh retry session"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-state"
                - "runtime.md#rt-rte-message-ingestion"
              note: "Processor reloads whitelisted retained outputs automatically and seeds a new attempt before executing stages."
          records:
            - "runtime.md#rt-obj-session-state"
            - "runtime.md#rt-rte-message-ingestion"
          note: "Known processor retries do not establish cross-worker-job checkpoint reuse."
        -
          scope: "MCP dependency-owned context reuse/compaction details, granular tool payload routes, full compiler/module and migration consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-ask"
            - "memory.md#mem-rte-knowledge-retrieval"
            - "memory.md#mem-rte-wiki-refresh"
            - "memory.md#mem-obj-text-vector"
          note: "Known requested and automatic deliveries do not completely resolve every included later-consumer operation."
      records:
        - "memory.md#mem-rte-knowledge-retrieval"
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-obj-session-state"
        - "runtime.md#rt-rte-message-ingestion"
        - "runtime.md#rt-rte-mcp-ask"
        - "memory.md#mem-rte-wiki-refresh"
        - "memory.md#mem-obj-text-vector"
      note: "Pull tool fulfillment coexists with automatic history, maintenance, summary and recovery supply. Included dependency/compiler alternatives retain unresolved coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "HTTP history push on a new turn"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dashboard-ask"
                - "memory.md#mem-obj-chat-history"
              note: "Trigger: HTTP question; selector input: supplied session plus user/channel provenance; selected part: matching session message tail."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dashboard-ask"
                - "memory.md#mem-obj-chat-history"
              note: "After session matching, an availability/error check and last-ten-message cap bound the automatically supplied dialogue content."
          records:
            - "runtime.md#rt-rte-dashboard-ask"
            - "memory.md#mem-obj-chat-history"
          note: "Session identity actually selects delivered dialogue; the tail budget is a distinct coarse selection operation."
        -
          scope: "Incremental maintainer event push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-maintenance"
                - "runtime.md#rt-bap-page-curation"
              note: "Trigger: memory-change/settlement event; selector input: channel/page and truly-new fact IDs against last_facts_seen; selected parts: affected current page and new fact records."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-maintenance"
                - "runtime.md#rt-bap-page-curation"
              note: "Curation/dirty-state and update availability gate whether maintenance context is supplied."
          records:
            - "runtime.md#rt-rte-wiki-maintenance"
            - "runtime.md#rt-bap-page-curation"
          note: "Identifier matching and coarse eligibility are separate selector contributions; routing implementation is not inferred semantic judgment."
        -
          scope: "Summary-model context push"
          assessment: "partial"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-retention"
              note: "Trigger: touched/dirty cluster; selector input: retained cluster membership IDs; selected parts: fetched member facts."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-summary-retention"
              note: "Active/superseded checks, quality-score ordering and top-20 cap filter fetched members before model delivery."
          records:
            - "memory.md#mem-rte-summary-retention"
          note: "Graph enrichment is included in the route, but a complete targeting inventory for every enrichment branch is unresolved."
        -
          scope: "Checkpoint restoration push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-state"
                - "runtime.md#rt-rte-message-ingestion"
              note: "Trigger: processor retry; selector input: sync_job_id and batch_num; selected parts: matching persisted whitelisted completed-stage outputs."
          records:
            - "runtime.md#rt-obj-session-state"
            - "runtime.md#rt-rte-message-ingestion"
          note: "The memory and workflow annotations establish matching and restoration, not cross-tick equivalence."
        -
          scope: "Full compiler/auto-builder, granular delivery alternatives and dependency-managed MCP session selection"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-wiki-refresh"
            - "memory.md#mem-rte-knowledge-retrieval"
            - "runtime.md#rt-rte-mcp-ask"
          note: "Untraced automatic delivery/selection alternatives cannot be made inapplicable by a known pull route. Query embeddings and lexical MMR on requested reads are not push signals."
      records:
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-wiki-maintenance"
        - "runtime.md#rt-bap-page-curation"
        - "memory.md#mem-rte-summary-retention"
        - "runtime.md#rt-obj-session-state"
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-rte-wiki-refresh"
        - "memory.md#mem-rte-knowledge-retrieval"
        - "runtime.md#rt-rte-mcp-ask"
      note: "Signals classify actual automatic supply operations, not identifiers or embeddings used only in pull retrieval. Included alternatives prevent exhaustive push-selector coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Retained conversation messages through automatic fact/graph extraction and later summary/wiki/QA consumers"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-messages"
                - "runtime.md#rt-rte-message-ingestion"
                - "memory.md#mem-rte-summary-retention"
                - "memory.md#mem-rte-knowledge-retrieval"
              note: "Recorded conversational activity feeds automatic production of durable extracted artifacts that later consumers receive as knowledge/context."
          records:
            - "memory.md#mem-obj-channel-messages"
            - "runtime.md#rt-rte-message-ingestion"
            - "memory.md#mem-rte-summary-retention"
            - "memory.md#mem-rte-knowledge-retrieval"
          note: "The recorded conversation-derived branch qualifies without weight training or demonstrated improvement. Non-conversation imported alternatives retain source uncertainty."
        -
          scope: "HTTP recorded question/context through generated retained answer and later QA context/search"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-qa-answer"
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-rte-dashboard-ask"
              note: "Session activity feeds generated answer content, which automatic history persistence retains and later turns or QA search consume."
          records:
            - "epistemic.md#epi-obj-qa-answer"
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-rte-dashboard-ask"
          note: "This finding concerns the generated durable answer artifact, not raw log retention alone. Stored tool/thinking fields are not all replayed."
        -
          scope: "Other import/media content origins, alternative full compilers/checkpoints and feedback/evaluation-driven updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-rte-wiki-refresh"
            - "runtime.md#rt-obj-session-state"
            - "memory.md#mem-clm-evaluation-authority"
            - "epistemic.md#epi-rte-qa-grading"
          note: "No complete bounded negative is supported. Unresolved sources or downstream update consumers prevent classifying all included writes as qualifying or nonqualifying."
      records:
        - "memory.md#mem-obj-channel-messages"
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-rte-summary-retention"
        - "memory.md#mem-rte-knowledge-retrieval"
        - "epistemic.md#epi-obj-qa-answer"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-rte-wiki-refresh"
        - "runtime.md#rt-obj-session-state"
        - "memory.md#mem-clm-evaluation-authority"
        - "epistemic.md#epi-rte-qa-grading"
      note: "Positive automatic trace-to-durable-artifact-to-later-consumer chains coexist with unresolved writes. No system-wide no or capacity-improvement claim is made."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "HTTP QA generation/history route, conversational-turn input"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-dashboard-ask"
                - "memory.md#mem-obj-chat-history"
                - "epistemic.md#epi-obj-qa-answer"
              note: "Recorded user/assistant dialogue from QA work sessions is reintroduced into generation; resulting answers persist for later context/search."
          records:
            - "runtime.md#rt-rte-dashboard-ask"
            - "memory.md#mem-obj-chat-history"
            - "epistemic.md#epi-obj-qa-answer"
          note: "This classifies the conversational source component, not every live tool result or attachment in a mixed QA prompt."
        -
          scope: "Platform/pushed/imported messages feeding extraction and downstream summary/wiki routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-channel-messages"
            - "memory.md#mem-clm-import-admission"
            - "runtime.md#rt-rte-message-ingestion"
          note: "The records establish normalized conversations and potentially mixed human/bot/imported content, not the original trace origin of each input. A channel/event adapter label cannot establish event-streams or agent session-logs."
        -
          scope: "Tool-result/attachment origins in persisted QA generation, alternative import/media/compiler/checkpoint inputs and evaluator-driven updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-dashboard-ask"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-rte-wiki-refresh"
            - "runtime.md#rt-obj-session-state"
            - "memory.md#mem-clm-evaluation-authority"
          note: "Persisted tool trace display fields alone do not prove that a qualifying update consumed recorded tool-traces; full mixed-source lineage and later diagnostic consumers remain unresolved."
      records:
        - "runtime.md#rt-rte-dashboard-ask"
        - "memory.md#mem-obj-chat-history"
        - "epistemic.md#epi-obj-qa-answer"
        - "memory.md#mem-obj-channel-messages"
        - "memory.md#mem-clm-import-admission"
        - "runtime.md#rt-rte-message-ingestion"
        - "memory.md#mem-rte-wiki-refresh"
        - "runtime.md#rt-obj-session-state"
        - "memory.md#mem-clm-evaluation-authority"
      note: "Session-log input is supported for the QA conversational component. Original extraction and mixed tool/import content is not fully recorded, so no event-stream/tool-trace/trajectory union is inferred from serialization or labels."
---

# Beever Atlas memory profile

## Comparison rationale

This profile classifies the accepted records only. All positive findings are
implementation wiring, not observed activation or causal benefit. Each axis is
partial because the retained inventory explicitly includes incompletely traced
alternatives. Known local units do not close those alternatives.

The reconciliation supersedes only the duplicate contradiction-model component
with [MEM-CMP-contradiction-detector](memory.md#mem-cmp-contradiction-detector).
Neither provider-owned component is an accumulated-memory object in this scope,
so that amendment changes no positive value. Valid containers and their parts
remain separately available: the extraction route, callback admission and
persisted fact/graph parts are not replacement identities.

Dense retained vectors are parametric representations, not model weights.
MongoDB document collections are service objects, not an inferred relational
store. The retained registry and alternate adapters remain included without
inventing extra substrates from the overall runtime's dependency list. See
[MEM-OBJ-text-vector](memory.md#mem-obj-text-vector) and
[MEM-OBJ-graph-entity](memory.md#mem-obj-graph-entity).

Push and pull are operations, not whole-system labels. Tool requests remain
pull even when an embedding or lexical reranker selects returned facts. Host
history injection, event-maintenance context and retry restoration are separate
automatic supply operations. Their identity matches and coarse eligibility or
budget filters are retained separately. See
[MEM-RTE-knowledge-retrieval](memory.md#mem-rte-knowledge-retrieval),
[RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask),
[RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) and
[RT-OBJ-session-state](runtime.md#rt-obj-session-state), including the supplied
memory/workflow annotations on those runtime referents.

Retained experience can have learning authority at an update consumer while
the derived artifact has knowledge authority at later answering. This mapping
asserts the wired trace-fed artifact route, not improved future capacity,
training, reflection or self-improvement. Raw log retention alone is not the
positive witness: the qualifying QA path includes generated retained answers
and later consumption. Original platform/import origins and mixed tool inputs
remain unresolved rather than being labelled event streams from their adapter.
See [EPI-OBJ-qa-answer](epistemic.md#epi-obj-qa-answer),
[MEM-OBJ-chat-history](memory.md#mem-obj-chat-history) and
[RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion).

Consolidation describes the implemented extraction/reduction and summary
routes; uncertain semantic fidelity does not establish synthesis. The
narration qualifier-removal example does not turn a faithfulness defect into a
synthesize finding. Full compiler semantics remain unresolved. Decay denotes
forgetting by covered hard purge, not a claimed age-based downweighting rule.
See [MEM-RTE-summary-retention](memory.md#mem-rte-summary-retention),
[EPI-RTE-narration-rewrite](epistemic.md#epi-rte-narration-rewrite),
[MEM-RTE-wiki-refresh](memory.md#mem-rte-wiki-refresh) and
[MEM-RTE-channel-withdrawal](memory.md#mem-rte-channel-withdrawal).

Coverage limits matter independently of evidence strength. Caller-selected
imports, curation and model changes do not prove human admission. Compatibility
wiki overlay is not proof that rewritten sections reach every consumer. Fact
invalidation excludes on guarded branches but not ordinary BM25 fallback.
Diagnostics do not establish an untraced rating-to-policy loop. See
[MEM-CLM-import-admission](memory.md#mem-clm-import-admission),
[RT-RTE-page-curation](runtime.md#rt-rte-page-curation),
[MEM-OBJ-wiki-page](memory.md#mem-obj-wiki-page),
[EPI-RTE-fact-supersession](epistemic.md#epi-rte-fact-supersession) and
[MEM-CLM-evaluation-authority](memory.md#mem-clm-evaluation-authority).

### Source-read log

No frozen-source files were read for this profile. Classification used the
supplied accepted reports and reconciliation; no new records, quotations or
evidence were added.
