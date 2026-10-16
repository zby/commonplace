---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of Atomic: retained corpus, derived access state, conversation replay, wiki candidates/history, report products and changed control state."
run-id: "AAS-2026-10-12-atomic-f98683232831-01"
source-identity: "https://github.com/kenforthewin/atomic"
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
memory-comparison:
  version: 2
  scope: "Included: accumulated atoms/chunks/vectors/tags, conversation text and trace metadata, live/pending/archived wiki parts, report findings/provenance, changed prompts/configuration, derived graph/control state and their shipped admission/maintenance/later-consumer alternatives. Client mappings, task/cache/lease state, alternate backends/strategies, reset/withdrawal and backup paths remain included but incompletely inspected. Excluded: static shipped instructions/assets, current-run-only tool registries/citation ledgers and ephemeral retrieval scores, external provider weights/state and external MCP host internals; benchmark metrics without a production update consumer are not production memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Atoms excluding separately classified report findings"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atoms"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atoms"
              note: "StorageBackend also supplies PostgreSQL atom storage; this identifies its substrate, not audited adapter parity."
          records:
            - "memory.md#mem-obj-atoms"
          note: "Database retention is recorded for this operative part; adapter transaction and cleanup guarantees are not inferred."
        -
          scope: "Atom text chunks: inspected SQLite storage and unresolved alternative backend branches"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atom-chunks"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-atom-chunks"
          note: "SQLite is the inspected storage witness. The record identifies database chunk rows but does not settle the included alternative backend substrate inventory; complete SQLite-only classification is prevented."
        -
          scope: "Tag hierarchy and associations: inspected SQLite storage and unresolved alternative backend branches"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-tags"
          note: "SQLite is the inspected storage witness. Alternative database branches remain included, with PostgreSQL merge application uninspected; their substrate coverage is unresolved rather than excluded by this finding."
        -
          scope: "Conversation text and stored tool/citation metadata: inspected SQLite storage and unresolved alternative backend branches"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-chat-history"
          note: "The inspected branch retains chat tables in SQLite. The accepted record does not complete the alternative backend inventory for text and trace metadata; no complete SQLite-only object classification follows."
        -
          scope: "Live wiki prose and citations: inspected SQLite storage and unresolved alternative backend branches"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "SQLite publication storage is inspected. Included PostgreSQL/wiki alternatives are not fully classified in the accepted account; the positive branch witness cannot resolve the whole live-object substrate inventory."
        -
          scope: "Pending wiki candidates and acceptance metadata: inspected SQLite storage and unresolved StorageBackend alternatives"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-wiki-proposals"
          note: "The SQLite branch supplies a positive witness, while the record's StorageBackend proposal storage leaves its full adapter inventory unresolved. Candidate database retention does not establish complete SQLite-only coverage."
        -
          scope: "Historical wiki checkpoints: inspected SQLite archive and unresolved PostgreSQL branch"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-wiki-versions"
          note: "SQLite archive rows are directly inspected; the record explicitly leaves PostgreSQL archive semantics uninspected. That included branch remains unresolved for substrate classification as well as parity; only the SQLite positive is asserted."
        -
          scope: "Report prose, provenance and citations: inspected SQLite storage and unresolved PostgreSQL branch"
          assessment: "partial"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report-findings"
              note: "Inspected retained database rows are the substrate; table structure and text encoding are separate dimensions."
          records:
            - "memory.md#mem-obj-report-findings"
          note: "SQLite retains finding prose/provenance/citations in the inspected transaction. The included PostgreSQL implementation remains uninspected; this witness does not complete the object-wide substrate inventory."
        -
          scope: "Retained chunk vectors and their search indexes: inspected database/vector branch and unresolved alternative backends"
          assessment: "partial"
          findings:
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-embeddings"
                - "memory.md#mem-rte-atom-enrichment"
              note: "Persisted dense vectors are queried by vector search."
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-embeddings"
                - "memory.md#mem-rte-atom-enrichment"
              note: "The inspected database retains chunk/vector state."
          records:
            - "memory.md#mem-obj-chunk-embeddings"
            - "memory.md#mem-rte-atom-enrichment"
          note: "Vectors are stored access state, not service-side model weights. Vector and SQLite findings classify the inspected branch; included alternative database/vector storage is not completely located by the accepted records."
        -
          scope: "Derived graph edges and centroids"
          assessment: "partial"
          findings:
            -
              value: "graph"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-state-maintenance"
              note: "Persisted edge structure organizes retained corpus access."
          records:
            - "runtime.md#rt-rte-state-maintenance"
          note: "The dispatch record establishes derived graph retention but does not completely locate every adapter representation."
        -
          scope: "Changed prompts and configuration"
          assessment: "partial"
          findings:
            -
              value: "kv"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
              note: "Retained settings map keys to prompt and operational values."
          records:
            - "runtime.md#rt-rte-settings-change"
          note: "Registry/global/per-database setting routes establish key/value retention without fully classifying every physical adapter."
        -
          scope: "Task ledger, report cache, dirty markers, client mappings, import/reset and backup alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-state-maintenance"
            - "runtime.md#rt-rte-capture-write"
            - "memory.md#mem-obj-atoms"
          note: "Accepted records leave physical storage and retained-part inventory of these included alternatives incompletely inspected. Static shipped files, current-run registries/ledgers and excluded provider weights are not added as memory substrates."
      records:
        - "memory.md#mem-obj-atoms"
        - "memory.md#mem-obj-atom-chunks"
        - "memory.md#mem-obj-tags"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-wiki-proposals"
        - "memory.md#mem-obj-wiki-versions"
        - "memory.md#mem-obj-report-findings"
        - "memory.md#mem-obj-chunk-embeddings"
        - "memory.md#mem-rte-atom-enrichment"
        - "runtime.md#rt-rte-state-maintenance"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-rte-capture-write"
      note: "Positive database, vector, graph and key/value witnesses do not resolve all shipped client/control/backup state or physical backend alternatives."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Atoms excluding separately classified report findings"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atoms"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atoms"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-atoms"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Atom text chunks"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atom-chunks"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atom-chunks"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-atom-chunks"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Tag hierarchy and associations"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-tags"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Conversation text and stored tool/citation metadata"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-chat-history"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Live wiki prose and citations"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Pending wiki candidates and acceptance metadata"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-wiki-proposals"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Historical wiki checkpoints"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-wiki-versions"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Report prose, provenance and citations"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report-findings"
              note: "Prose, names, descriptions or excerpts are interpreted by readers/models."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report-findings"
              note: "Identifiers, links and metadata have fixed consumer interpretations."
          records:
            - "memory.md#mem-obj-report-findings"
          note: "The record splits readable retained content from localized identifiers, ordering, links, status or citation fields."
        -
          scope: "Chunk embeddings at vector comparison"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-embeddings"
              note: "Dense chunk vectors supply distributed numerical retrieval representations."
          records:
            - "memory.md#mem-obj-chunk-embeddings"
          note: "Dense representations distribute information numerically; they are not weights."
        -
          scope: "Graph maintenance products"
          assessment: "partial"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-state-maintenance"
              note: "Retained edge relations and completion/watermark state have fixed software consumers."
          records:
            - "runtime.md#rt-rte-state-maintenance"
          note: "Edges are localized relations; centroid numerical detail remains unresolved."
        -
          scope: "Retained prompts and executable configuration selection"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
              note: "Changed custom chat prefix supplies later system prose."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
              note: "Provider and strategy settings select executable branches."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-bap-chat-prompt"
          note: "Natural-language prompt interpretation differs from fixed key/value routing."
        -
          scope: "Uninspected client mappings, task/cache payloads, backups and alternative strategy products"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-atoms"
            - "memory.md#mem-obj-wiki-articles"
          note: "No complete operative payload inventory is recorded; visible summaries do not classify unseen contents."
      records:
        - "memory.md#mem-obj-atoms"
        - "memory.md#mem-obj-atom-chunks"
        - "memory.md#mem-obj-tags"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-wiki-proposals"
        - "memory.md#mem-obj-wiki-versions"
        - "memory.md#mem-obj-report-findings"
        - "memory.md#mem-obj-chunk-embeddings"
        - "runtime.md#rt-rte-state-maintenance"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-bap-chat-prompt"
      note: "Text, symbolic fields and dense vectors are kept separate by operative path; unresolved auxiliary and alternative payloads prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Atom admission paths before derived products"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atoms"
                - "runtime.md#rt-rte-capture-write"
                - "runtime.md#rt-rte-atom-mutation"
              note: "Capture/direct import admits external content."
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-atom-mutation"
              note: "The model proposes new or edited atom prose."
          records:
            - "memory.md#mem-obj-atoms"
            - "runtime.md#rt-rte-capture-write"
            - "runtime.md#rt-rte-atom-mutation"
          note: "External capture/import and model-authored mutation are established paths; initial authorship and client alternatives remain unresolved."
        -
          scope: "Chunk text"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-atom-chunks"
              note: "Fixed segmentation compiles retained atom content into slices."
          records:
            - "memory.md#mem-obj-atom-chunks"
          note: "This records the subsequent derivation, not otherwise unknown initial content provenance."
        -
          scope: "Retained chunk vectors"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunk-embeddings"
              note: "The configured embedding service derives numerical access state from chunk text."
          records:
            - "memory.md#mem-obj-chunk-embeddings"
          note: "This records the subsequent derivation, not otherwise unknown initial content provenance."
        -
          scope: "Tags and associations"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
              note: "Generated tag applications and merge operations compile corpus categorization."
          records:
            - "memory.md#mem-obj-tags"
          note: "This records the subsequent derivation, not otherwise unknown initial content provenance."
        -
          scope: "Wiki version snapshots"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Software copies prior live prose and citation state into an archive."
          records:
            - "memory.md#mem-obj-wiki-versions"
          note: "This records the subsequent derivation, not otherwise unknown initial content provenance."
        -
          scope: "Recorded user/assistant conversation text"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-rte-chat-turn"
              note: "User turns enter from the caller."
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-rte-chat-turn"
              note: "The model generates retained assistant answers."
          records:
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-rte-chat-turn"
          note: "User text is acquired and assistant text generated; identity of every initial author is not established."
        -
          scope: "Saved-answer Markdown"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-answer-save"
              note: "An interaction answer and its citation metadata are converted into a retained derivative; this lineage alone does not settle admission agency."
          records:
            - "memory.md#mem-rte-answer-save"
          note: "The deterministic helper derives ordinary corpus prose from recorded answer/citation/question material."
        -
          scope: "Live wiki synthesis"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
                - "runtime.md#rt-rte-wiki-admission"
              note: "Configured model/strategy drafts synthesized or updated prose."
          records:
            - "memory.md#mem-obj-wiki-articles"
            - "runtime.md#rt-rte-wiki-admission"
          note: "The model authors a product from selected chunks; unresolved strategies and inherited source provenance are not upgraded."
        -
          scope: "Pending wiki draft"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
                - "runtime.md#rt-rte-wiki-admission"
              note: "Configured model/strategy drafts synthesized or updated prose."
          records:
            - "memory.md#mem-obj-wiki-proposals"
            - "runtime.md#rt-rte-wiki-admission"
          note: "The model authors a product from selected chunks; unresolved strategies and inherited source provenance are not upgraded."
        -
          scope: "Report final prose"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "A separate model final pass writes the retained finding."
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "The final pass consumes the recorded research message/tool transcript before the finding is retained."
          records:
            - "runtime.md#rt-rte-report-finding"
            - "memory.md#mem-obj-report-findings"
          note: "Model authorship and research-transcript derivation coexist; original seeded corpus provenance remains mixed."
        -
          scope: "Initial prompts/configuration, client state, graph derivation and alternative imports"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-atoms"
          note: "Caller identity, endpoint model name and supplied scope do not determine initial or alternative derivation paths."
      records:
        - "memory.md#mem-obj-atoms"
        - "runtime.md#rt-rte-capture-write"
        - "runtime.md#rt-rte-atom-mutation"
        - "memory.md#mem-obj-atom-chunks"
        - "memory.md#mem-obj-chunk-embeddings"
        - "memory.md#mem-obj-tags"
        - "memory.md#mem-obj-wiki-versions"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-rte-answer-save"
        - "memory.md#mem-obj-wiki-articles"
        - "runtime.md#rt-rte-wiki-admission"
        - "memory.md#mem-obj-wiki-proposals"
        - "runtime.md#rt-rte-report-finding"
        - "memory.md#mem-obj-report-findings"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-rte-state-maintenance"
      note: "Known derivations coexist with unresolved initial content, imported embeddings and client/strategy provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Selected atom/chunk prose at chat/wiki/report consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-corpus-evidence"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Tool/source text supplies reference and evidence to generating models."
          records:
            - "memory.md#mem-bap-corpus-evidence"
            - "memory.md#mem-rte-corpus-retrieval"
          note: "Requested evidence supplies context rather than enforced directions."
        -
          scope: "Conversation text at later chat invocation"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "runtime.md#rt-rte-chat-turn"
              note: "Prior turn text supplies conversational context to the next provider request."
          records:
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-rte-chat-turn"
          note: "Role/content replay is established; historical tool-call metadata is not replayed."
        -
          scope: "Live wiki prose"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-articles"
              note: "Retained prose is returned for interpretation as product/candidate/history context."
          records:
            - "memory.md#mem-obj-wiki-articles"
          note: "Authority belongs to this actual reader path, not automatically to every possible model consumer."
        -
          scope: "Report finding prose"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report-findings"
              note: "Retained prose is returned for interpretation as product/candidate/history context."
          records:
            - "memory.md#mem-obj-report-findings"
          note: "Authority belongs to this actual reader path, not automatically to every possible model consumer."
        -
          scope: "Wiki candidate prose at requesting reviewer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
              note: "Retained prose is returned for interpretation as product/candidate/history context."
          records:
            - "memory.md#mem-obj-wiki-proposals"
          note: "Authority belongs to this actual reader path, not automatically to every possible model consumer."
        -
          scope: "Historical wiki prose at requesting version reader"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Retained prose is returned for interpretation as product/candidate/history context."
          records:
            - "memory.md#mem-obj-wiki-versions"
          note: "Authority belongs to this actual reader path, not automatically to every possible model consumer."
        -
          scope: "Corpus text and vectors at query ranking"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-corpus-retrieval"
                - "memory.md#mem-obj-atoms"
                - "memory.md#mem-obj-chunk-embeddings"
              note: "Keyword/vector/hybrid retrieval ranks retained content using its text and dense representations."
          records:
            - "memory.md#mem-rte-corpus-retrieval"
            - "memory.md#mem-obj-atoms"
            - "memory.md#mem-obj-chunk-embeddings"
          note: "Scored retained features influence relative priority even though fixed code supplies the scoring policy."
        -
          scope: "Tag membership and hierarchy at scope selector"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Tags select corpus scope for later retrieval."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tags"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Require/exclude predicates veto delivery of ineligible corpus entries on this scoped search route."
          records:
            - "memory.md#mem-obj-tags"
            - "memory.md#mem-rte-corpus-retrieval"
          note: "Membership changes eligibility under include/require/exclude predicates."
        -
          scope: "Proposal base ID/timestamp at acceptance"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
                - "runtime.md#rt-rte-wiki-admission"
              note: "Retained base identity/time determine whether a pending candidate still conforms to the live base."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
                - "runtime.md#rt-rte-wiki-admission"
              note: "A stale base refuses acceptance."
          records:
            - "memory.md#mem-obj-wiki-proposals"
            - "runtime.md#rt-rte-wiki-admission"
          note: "The stale-base gate is structural admissibility, not factual acceptance."
        -
          scope: "Retained custom chat prefix at system-message consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
              note: "Stored custom prefix supplies later chat system directions."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-bap-chat-prompt"
          note: "The changed prefix has standing guidance force, not guaranteed compliance."
        -
          scope: "Retained custom tagging prompt at tagging system-message consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "memory.md#mem-rte-atom-enrichment"
              note: "The memory annotation establishes that tagging_prompt replaces the stock tagging system prompt supplied to the configured tagging provider."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "memory.md#mem-rte-atom-enrichment"
          note: "Retained changed guidance directs subsequent tag production; model compliance and classification correctness remain unobserved."
        -
          scope: "Configuration and retained report/maintenance control markers"
          assessment: "partial"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-rte-state-maintenance"
                - "runtime.md#rt-rte-report-finding"
              note: "Stored configuration, task status and source-window watermark steer later operations."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-rte-state-maintenance"
            - "runtime.md#rt-rte-report-finding"
          note: "Settings choose branches and report watermarks choose later source windows; detailed lease/cache consumers remain unresolved."
        -
          scope: "Recorded report research transcript at durable final-product writer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "Recorded research experience feeds automatic production of a durable behavior-shaping finding."
          records:
            - "runtime.md#rt-rte-report-finding"
            - "memory.md#mem-obj-report-findings"
          note: "The final writer consumes research messages/tool results and retains prose reused by later readers; no benefit is established."
        -
          scope: "Graph/centroid details, unconsumed citation metadata, client/backup state and alternate strategy consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-wiki-articles"
            - "memory.md#mem-obj-atoms"
          note: "No stronger consumer/force inventory is recorded; metadata retention alone grants no authority."
      records:
        - "memory.md#mem-bap-corpus-evidence"
        - "memory.md#mem-rte-corpus-retrieval"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-obj-wiki-articles"
        - "memory.md#mem-obj-report-findings"
        - "memory.md#mem-obj-wiki-proposals"
        - "memory.md#mem-obj-wiki-versions"
        - "memory.md#mem-obj-atoms"
        - "memory.md#mem-obj-chunk-embeddings"
        - "memory.md#mem-obj-tags"
        - "runtime.md#rt-rte-wiki-admission"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-bap-chat-prompt"
        - "runtime.md#rt-rte-state-maintenance"
        - "runtime.md#rt-rte-report-finding"
        - "memory.md#mem-rte-atom-enrichment"
      note: "Local knowledge, instruction, ranking, routing, validation, enforcement and research-update learning paths coexist; chat and tagging have distinct retained instruction consumers. No blanket force is assigned to every stored object."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model create/edit handler"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-atom-mutation"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "runtime.md#rt-rte-atom-mutation"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Single-atom chunk/vector/tag admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-enrichment"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "memory.md#mem-rte-atom-enrichment"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Ordinary model tag-merge application"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tag-compaction"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "memory.md#mem-rte-tag-compaction"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Wiki candidate persistence"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "memory.md#mem-obj-wiki-proposals"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Prior wiki snapshot admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-versions"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "memory.md#mem-obj-wiki-versions"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Direct/immediate wiki publication"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "runtime.md#rt-rte-wiki-admission"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Report final finding admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "runtime.md#rt-rte-report-finding"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Scheduled graph/access-state refresh"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-state-maintenance"
              note: "Workflow initiation or settings choice does not make downstream derived admission manual."
          records:
            - "runtime.md#rt-rte-state-maintenance"
          note: "Software/model admits each derived write without an independent per-content operator approval in this inspected mechanism."
        -
          scope: "Core/MCP/import/client initial capture; caller edits/settings; explicit tag pairs; reviewed wiki promotion; saved-answer invocation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-write"
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-rte-wiki-admission"
            - "memory.md#mem-rte-tag-compaction"
            - "memory.md#mem-rte-answer-save"
          note: "Generic caller identity and uninspected UI do not establish an explicit human content decision or exclude one. Physical software I/O does not resolve control."
      records:
        - "runtime.md#rt-rte-atom-mutation"
        - "memory.md#mem-rte-atom-enrichment"
        - "memory.md#mem-rte-tag-compaction"
        - "memory.md#mem-obj-wiki-proposals"
        - "memory.md#mem-obj-wiki-versions"
        - "runtime.md#rt-rte-wiki-admission"
        - "runtime.md#rt-rte-report-finding"
        - "runtime.md#rt-rte-state-maintenance"
        - "runtime.md#rt-rte-capture-write"
        - "runtime.md#rt-rte-settings-change"
        - "memory.md#mem-rte-answer-save"
      note: "Automatic derived admissions are wired. Manual admission is not asserted without a recorded human decision; unresolved caller-controlled branches remain included."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing atom edit"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-atom-mutation"
              note: "Model edits change an existing atom after shape/concurrency checks."
          records:
            - "runtime.md#rt-rte-atom-mutation"
          note: "The compare/update route revises retained content without implying factual improvement."
        -
          scope: "SQLite tag merge application"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tag-compaction"
              note: "The inspected merge removes a selected duplicate category and moves its associations to the winner."
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tag-compaction"
              note: "Merged taxonomy combines existing classifications into a reduced category structure."
          records:
            - "memory.md#mem-rte-tag-compaction"
          note: "Winner absorbs associations and children while loser is deleted; semantic equivalence remains unverified and PostgreSQL is unresolved."
        -
          scope: "Live wiki replacement with prior-history archive"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-obj-wiki-versions"
              note: "Published generation/update replaces the existing live article."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-obj-wiki-versions"
              note: "Archived prior prose remains historical rather than the current live article."
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "memory.md#mem-obj-wiki-versions"
          note: "Replacement revises a retained product and removes the old version from current live reliance while keeping history."
        -
          scope: "Wiki/report semantic generation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "runtime.md#rt-rte-report-finding"
            - "epistemic.md#epi-obj-generated-prose"
          note: "Generation is wired but no individuated output/premises decide whether claims are merely compressed or new. A request to synthesize products does not establish the controlled synthesize operation or consolidation."
        -
          scope: "Alternative tag backends, chunk/re-embedding transforms, saved-answer semantic reductions, resets, withdrawal and other maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-atom-enrichment"
            - "memory.md#mem-rte-answer-save"
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-atoms"
          note: "Index rebuilds, chunk segmentation and acquisition alone do not establish a controlled curation operation. Detailed transformations and retained-history withdrawal are unresolved."
      records:
        - "runtime.md#rt-rte-atom-mutation"
        - "memory.md#mem-rte-tag-compaction"
        - "runtime.md#rt-rte-wiki-admission"
        - "memory.md#mem-obj-wiki-versions"
        - "runtime.md#rt-rte-report-finding"
        - "epistemic.md#epi-obj-generated-prose"
        - "memory.md#mem-rte-atom-enrichment"
        - "memory.md#mem-rte-answer-save"
        - "runtime.md#rt-rte-state-maintenance"
        - "memory.md#mem-obj-atoms"
      note: "Implemented revision/category merging/history withdrawal are distinct from semantically unresolved generation. No synthesize, decay or promote value is inferred from requests, status or command names."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested query/ID corpus and live-product readers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-corpus-retrieval"
                - "epistemic.md#epi-rte-generated-delivery"
              note: "Queries, requested IDs and line windows retrieve retained text for requesting consumers."
          records:
            - "memory.md#mem-rte-corpus-retrieval"
            - "epistemic.md#epi-rte-generated-delivery"
          note: "Consumer asks for retained material; formatting and response delivery do not add another push."
        -
          scope: "Requested pending-candidate and archived-version readers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-proposals"
                - "memory.md#mem-obj-wiki-versions"
              note: "Tag/version requests return retained review or archive content."
          records:
            - "memory.md#mem-obj-wiki-proposals"
            - "memory.md#mem-obj-wiki-versions"
          note: "Caller explicitly requests retained candidate/history material."
        -
          scope: "Automatic history selection inside a new requested chat turn"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-obj-chat-history"
              note: "Conversation ID reloads role/content history, budget selection supplies it to the next provider invocation."
          records:
            - "runtime.md#rt-rte-chat-turn"
            - "memory.md#mem-obj-chat-history"
          note: "The request asks for a new answer, not retained historical text; software independently supplies selected old message content."
        -
          scope: "Initial report source batch before research tools"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
              note: "Manual or scheduled report trigger leads fixed source selection to inject retained snippets into research context."
          records:
            - "runtime.md#rt-rte-report-finding"
          note: "Software resolves scope/window/cap and supplies source snippets; later model-requested research reads remain pull."
        -
          scope: "Research-selected corpus chunks supplied to wiki synthesis"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Research selections automatically populate the synthesis source context."
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "memory.md#mem-rte-corpus-retrieval"
          note: "Research selects chunks for a later synthesis consumer without that consumer requesting the retained chunks; budget filtering precedes delivery."
        -
          scope: "Retained prompt and selected tag-tree supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
                - "memory.md#mem-rte-atom-enrichment"
              note: "Chat/tagging triggers select effective prompt and eligible taxonomy for provider delivery."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-bap-chat-prompt"
            - "memory.md#mem-rte-atom-enrichment"
          note: "The provider does not request these retained settings/taxonomy; host assembles guidance/context."
        -
          scope: "Alternative wiki strategies, client automatic supplies and remaining maintenance/cache consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-atoms"
          note: "Uninspected selection/delivery alternatives remain included; known pull readers cannot establish a pull-only system."
      records:
        - "memory.md#mem-rte-corpus-retrieval"
        - "epistemic.md#epi-rte-generated-delivery"
        - "memory.md#mem-obj-wiki-proposals"
        - "memory.md#mem-obj-wiki-versions"
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-report-finding"
        - "runtime.md#rt-rte-wiki-admission"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-bap-chat-prompt"
        - "memory.md#mem-rte-atom-enrichment"
        - "runtime.md#rt-rte-state-maintenance"
        - "memory.md#mem-obj-atoms"
      note: "Both requested returns and automatic provider supplies exist. A requested enclosing workflow does not turn each internal automatic context selection into pull."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "History push on next chat turn"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-obj-chat-history"
              note: "Conversation identity matches the stored history delivered to the provider."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-obj-chat-history"
              note: "Order and budget filtering drop older groups while preserving mandatory first/latest groups."
          records:
            - "runtime.md#rt-rte-chat-turn"
            - "memory.md#mem-obj-chat-history"
          note: "Trigger: new turn. Input: requested conversation ID plus ordered retained groups and token estimates. Selected part: old role/content text."
        -
          scope: "Initial report-source push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
              note: "Scope/window/cap and token availability filter the seeded batch."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
              note: "Configured tag/report identities select the source scope and report-specific input window."
          records:
            - "runtime.md#rt-rte-report-finding"
          note: "Trigger: manual/scheduled report. Input: configured tag/kind/time/source cap and watermark; selected part: retained source snippets. Packing keeps a first-item exception."
        -
          scope: "Prompt/taxonomy push to chat/tagging"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
                - "memory.md#mem-rte-atom-enrichment"
              note: "Setting key and target-branch identity select effective guidance/taxonomy."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-change"
                - "runtime.md#rt-bap-chat-prompt"
                - "memory.md#mem-rte-atom-enrichment"
              note: "Enabled/status/provider availability and input-length filtering bound supplied content."
          records:
            - "runtime.md#rt-rte-settings-change"
            - "runtime.md#rt-bap-chat-prompt"
            - "memory.md#mem-rte-atom-enrichment"
          note: "Trigger: chat or tagging operation. Inputs: effective setting keys and configured target tree/status. Selected parts: retained custom prompt and eligible tag hierarchy."
        -
          scope: "Research chunk selection for later wiki synthesis"
          assessment: "known"
          findings:
            -
              value: "inferred-judgment"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Research model chooses chunks from the session before the synthesis consumer."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Selected chunk indices identify the parts supplied to synthesis."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-admission"
                - "memory.md#mem-rte-corpus-retrieval"
              note: "Ordered token-budget trimming can omit later selected chunks."
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "memory.md#mem-rte-corpus-retrieval"
          note: "Trigger: completed research. Input: retained search results and model-selected session chunk indices; selected parts: retained corpus chunks delivered to synthesis."
        -
          scope: "Remaining wiki strategies, report seed ordering, alternate client/maintenance pushes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-admission"
            - "runtime.md#rt-rte-report-finding"
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-atoms"
          note: "Known keyword/vector request retrieval does not itself establish lexical/embedding push. Alternate selectors and retained payload coverage remain unresolved."
      records:
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-report-finding"
        - "runtime.md#rt-rte-settings-change"
        - "runtime.md#rt-bap-chat-prompt"
        - "memory.md#mem-rte-atom-enrichment"
        - "runtime.md#rt-rte-wiki-admission"
        - "memory.md#mem-rte-corpus-retrieval"
        - "runtime.md#rt-rte-state-maintenance"
        - "memory.md#mem-obj-atoms"
      note: "Actual identity matches, budget/scope filters and research judgments classify inspected automatic supplies. No query embedding or identifier on a catalog alone is promoted to push selection."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Report research transcript to automatic durable finding and later product readers"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "Automatic trace-fed final prose production establishes this local qualifying route."
          records:
            - "runtime.md#rt-rte-report-finding"
            - "memory.md#mem-obj-report-findings"
          note: "Research messages/tool results feed a separate final writer; structural checks admit the durable finding consumed by later chat/MCP/search. No improvement or weight update is required."
        -
          scope: "Saved-answer content admission and its later enrichment"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-answer-save"
            - "memory.md#mem-rte-atom-enrichment"
          note: "The answer-derived artifact and later consumers are wired, but caller UI/per-save human content control is unresolved; no independent unconditional automatic trace-write verdict is assigned."
        -
          scope: "Other imported session content, client paths, alternative wiki/maintenance and evaluator-fed updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-atoms"
            - "memory.md#mem-obj-chat-history"
            - "runtime.md#rt-rte-state-maintenance"
            - "epistemic.md#epi-rte-retrieval-scoring"
          note: "Raw conversation retention, non-summary truncation and diagnostic scores do not by themselves supply a qualifying derived update. Remaining route coverage prevents bounded system absence."
      records:
        - "runtime.md#rt-rte-report-finding"
        - "memory.md#mem-obj-report-findings"
        - "memory.md#mem-rte-answer-save"
        - "memory.md#mem-rte-atom-enrichment"
        - "memory.md#mem-obj-atoms"
        - "memory.md#mem-obj-chat-history"
        - "runtime.md#rt-rte-state-maintenance"
        - "epistemic.md#epi-rte-retrieval-scoring"
      note: "A local report trace-to-product chain supports yes. Missing client/admission and alternate-route facts preclude complete coverage; no unsupported local or system-wide no is asserted."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Original inputs to report final-product trace-fed writer"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "The recorded agent research conversation in outcome.messages supplies the final writer."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-report-finding"
                - "memory.md#mem-obj-report-findings"
              note: "The research transcript includes requested tool actions and returned evidence used by the final writer."
          records:
            - "runtime.md#rt-rte-report-finding"
            - "memory.md#mem-obj-report-findings"
          note: "Recorded research conversational messages and tool results reach the final pass together with static instructions and corpus snippets. Source snippets are not traces merely because represented as messages."
        -
          scope: "Saved-answer route and mixed original capture/client/alternative-update inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-answer-save"
            - "memory.md#mem-obj-atoms"
            - "runtime.md#rt-rte-state-maintenance"
          note: "Saved answer originates in conversation, but qualifying automatic admission remains unresolved. No recorded full source-content inventory permits event-stream/trajectory claims or complete trace-source enumeration."
      records:
        - "runtime.md#rt-rte-report-finding"
        - "memory.md#mem-obj-report-findings"
        - "memory.md#mem-rte-answer-save"
        - "memory.md#mem-obj-atoms"
        - "runtime.md#rt-rte-state-maintenance"
      note: "Known research conversation/tool content is retained beside mixed corpus provenance and unresolved qualifying alternatives. No adapter label or scheduler event alone establishes a trace source."
---

# Atomic memory profile

## Comparison rationale

All findings classify the accepted records, not new source evidence. Reconciliation makes no supersessions: wiki articles remain a valid container, while pending proposals and archived versions keep their distinct consumer and admission units. Their knowledge-at-reader paths do not grant automatic live-model authority. The current-run CitationLedger and ToolRegistry are excluded from accumulated memory; selected persisted citations are included with their products.

Database retention does not imply vector encoding is symbolic or vectors are provider weights. Dense chunk embeddings map to parametric form and vector substrate. PostgreSQL atom support gives a relational substrate witness but does not settle the substrate inventory of every other retained part. Chunk, tag, conversation, wiki live/candidate/archive, report and vector storage units retain their inspected positive findings with partial coverage: their included alternative backend branches are not completely classified by the accepted records. This is a substrate-coverage limit, independently of transaction or cleanup parity. No SQLite-only complete classification of those object-wide inventories is asserted.

Requested corpus reads are pull. History supplied automatically to a model producing a new turn, report source seeding and host-selected prompts/taxonomy are push operations within a requested enclosing workflow. This operation-level distinction follows the profile type; it does not turn the report's descriptive phrase about no independent unsolicited history push into a pull-only classification. Wiki research chooses retained chunks for another synthesis consumer; identity, model judgment and subsequent coarse budget filtering are separate selectors. Query-driven keyword/vector retrieval remains pull and does not alone establish lexical/embedding push.

Automatic model-derived admissions are distinct from unresolved generic caller control. The saved-answer helper does not prove human per-save consent or exclude it. No manual finding is inferred from a user-facing surface or workflow initiation. Similarly, archive reads do not establish human checkpoint replacement. Static default prompts are not accumulated memory, while changed retained prompt values supply standing instruction authority. The retained custom tagging prompt separately supplies instructions to the tagging provider, not only to chat; its path is classified below alongside the chat-prefix path.

Tag merging supports category deduplication/consolidation; existing atom/wiki revision supports evolve. Archived prior wiki prose loses current live reliance while remaining historical, supporting invalidate on that replacement path. No command name or request alone establishes decay, promote or semantic synthesis. The accepted epistemic generation records leave wiki/report output semantics indeterminate; neither controlled synthesize nor consolidation is therefore established for those generation units.

The report route records a final writer consuming research messages and tool results, automatic durable finding admission and later product readers. That local chain supports trace learning and learning authority at the writer independently of knowledge authority at downstream readers. Its session/tool origins coexist with nontrace source snippets and unresolved original corpus provenance. It neither establishes improved capacity nor attributes model-weight learning. Raw chat retention, context truncation and diagnostic evaluator metrics are not independent qualifying derived updates merely because they record activity. Saved-answer and remaining alternative admission paths retain their uncertainty rather than becoming bounded negatives.

Every axis remains partial because the accepted record inventory explicitly leaves included client, adapter, strategy and maintenance alternatives unresolved. Positive existence warrants are not complete-value assertions. No supplied evidenced-absence record warrants a system-wide negative. Wiring is not observed activation or causal benefit. The generated-product reader's numeric deletion can also remove assertion content; product knowledge authority therefore describes delivered context, not faithful semantics or transitive source truth.

The coarse mixed representational-form units retain supported existence findings, not complete part-level consumer equivalence. Conversation role/content reaches provider replay while attached tool/citation metadata has separate storage readers; wiki candidate prose reaches review while base IDs/timestamps reach freshness checks. Withhold part-level and consumption-path comparisons that assume every field in either mixed unit reaches one consumer or receives one interpretation.

Supporting distinctions: [MEM-RTE-tag-compaction](memory.md#mem-rte-tag-compaction), [MEM-RTE-answer-save](memory.md#mem-rte-answer-save), [MEM-OBJ-wiki-proposals](memory.md#mem-obj-wiki-proposals), [MEM-OBJ-wiki-versions](memory.md#mem-obj-wiki-versions), [RT-RTE-report-finding](runtime.md#rt-rte-report-finding), [EPI-OBJ-generated-prose](epistemic.md#epi-obj-generated-prose), [EPI-RTE-generated-delivery](epistemic.md#epi-rte-generated-delivery) and [EPI-RTE-retrieval-scoring](epistemic.md#epi-rte-retrieval-scoring).

Source-read log: none. All classification warrants come from the supplied accepted members and their annotations; no source ambiguity required a new read. No analyst records, quotations or evidence were added.
