---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Cortex memory profile: dual-store knowledge, vectors, usage-derived tiers and requested reuse at the frozen revision."
run-id: "AAS-2026-10-17-cortex-3da14ce55a2b-01"
source-identity: "https://github.com/abbacusgroup/cortex"
reviewed-boundary: "a51c2209eb6d26812c19c97aaade3cb64ccfc23c"
memory-comparison:
  version: 2
  scope: "Accumulated Cortex document bodies/raw Markdown, summaries, symbolic metadata, graph objects/entities/relationships, SQLite vectors, access counters/tier changes, query trail, persisted weight and temporal-version capabilities, import dedup markers and whole-store archive recovery; their admission, maintenance and later service/internal consumers. Excludes shipped static prompts/ontology/inference rules, provider weights/state, external host conversation memory, current-response diagnostics and unretained synthesis narratives."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Document text, summaries, classification metadata, embeddings, access keys, query log, persisted weight coefficients and document-row versions"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-tier"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-obj-query-log"
                - "memory.md#mem-obj-retrieval-weights"
                - "memory.md#mem-obj-document-versions"
              note: "These retained parts reside in SQLite tables/config values; vectors are BLOBs, not a separate vector database."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-tier"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-obj-document-versions"
          note: "The accepted part inventory identifies the SQLite location of each part, including dormant weight/history capabilities."
        - scope: "Graph identities, entities, assertions, mentions and descriptive properties"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-relationships"
              note: "Oxigraph retains graph objects and edges; duplicated text properties do not change the substrate."
          records:
            - "memory.md#mem-obj-relationships"
          note: "Graph state is a separate retained part from content-authoritative SQLite."
        - scope: "Operator-created whole-store backup and restoration artifact"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-knowledge"
              note: "Restore consumes an archive containing stores and replaces local store files."
          records:
            - "runtime.md#rt-rte-maintain-knowledge"
          note: "This is whole-store recovery, not an additional graph/vector service."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-tier"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-obj-relationships"
        - "runtime.md#rt-rte-maintain-knowledge"
      note: "The scoped inventory comprises accumulated dual-store parts and their archive recovery route. External provider internals, static packaged rules/prompts and current-response dictionaries are excluded, not counted as unknown memory stores."
    representational_form:
      assessment: "known"
      units:
        - scope: "Bodies, raw Markdown, titles, summaries and descriptive graph-property text at host or synthesis-model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-relationships"
                - "runtime.md#rt-rte-retrieve-context"
              note: "Humans/models interpret prose; body and summary delivery differ."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-retrieve-context"
          note: "Includes graph descriptive values, not just text stored in SQLite."
        - scope: "IDs, typed graph predicates, classification/filter metadata, access counters, query-event structure, weights and version metadata at fixed-code consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-tier"
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-obj-query-log"
                - "memory.md#mem-obj-retrieval-weights"
                - "memory.md#mem-obj-document-versions"
              note: "Localized identifiers, predicates, coefficients and fields receive fixed query/comparison semantics."
          records:
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-tier"
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-obj-document-versions"
          note: "Historical row payloads also contain prose, covered separately; dormant weight coefficients are symbolic, not trained parameters."
        - scope: "Stored embedding vectors at cosine-similarity consumption"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
              note: "Dense distributed numerical representations determine semantic candidate similarity, independently of provider weights."
          records:
            - "memory.md#mem-obj-embeddings"
          note: "The controlled value covers distributed representations; provider model parameters are outside the accumulated-memory boundary."
        - scope: "Query strings and historical document prose inside otherwise structured logs/checkpoints"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-log"
                - "memory.md#mem-obj-document-versions"
              note: "Queries and old title/content/summary fields retain text interpreted as text, despite JSON/row envelopes."
          records:
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-document-versions"
          note: "Encoding the envelope as JSON does not erase mixed operative forms."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-relationships"
        - "runtime.md#rt-rte-retrieve-context"
        - "memory.md#mem-obj-tier"
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-obj-embeddings"
      note: "The inventory splits prose, fixed symbolic interpretation and dense vector consumption. No opaque provider payload is an included retained Cortex memory part."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller-supplied document and summary paths"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-capture-pipeline"
              note: "Explicit supplied content/summary is retained through caller authoring paths; this does not authenticate an author or establish human approval."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-capture-pipeline"
          note: "Known admission path, not complete upstream provenance."
        - scope: "Markdown/frontmatter and legacy-row import paths"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "runtime.md#rt-rte-direct-import"
              note: "Imported files/rows and associated tags/wiki-links supply retained content."
          records:
            - "memory.md#mem-obj-documents"
            - "runtime.md#rt-rte-direct-import"
          note: "Import is known; original authoring and any prior transformations are unresolved."
        - scope: "Internal summary/fallback, embedding generation, entity resolution, enrichment and fixed-rule graph derivation"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-tier"
                - "runtime.md#rt-rte-capture-pipeline"
                - "epistemic.md#epi-rte-rule-retention"
              note: "Software/model transformations derive retained parts from admitted content; fixed-rule edges are retained products, not imported rules."
          records:
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-tier"
            - "runtime.md#rt-rte-capture-pipeline"
            - "epistemic.md#epi-rte-rule-retention"
          note: "Known subsequent derivations do not resolve source text authorship, embedding-model training provenance or semantic faithfulness."
        - scope: "Access counters, last-access stamps and promoted tier from read/positive-feedback activity"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-rte-access-promotion"
              note: "Runtime use is reduced to persistent counts/time and a possible tier update."
          records:
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-rte-access-promotion"
          note: "Activity-to-metadata derivation is wired; per-event reasons are discarded."
        - scope: "Raw search-query history"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-log"
              note: "Hybrid search records query parameters and selected IDs for later diagnostic trail reads."
          records:
            - "memory.md#mem-obj-query-log"
          note: "This lineage finding does not itself establish trace learning."
        - scope: "Old document-row versions and backup copies"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-document-versions"
                - "runtime.md#rt-rte-maintain-knowledge"
              note: "Snapshot/backup routes copy retained state to historical representations."
          records:
            - "memory.md#mem-obj-document-versions"
            - "runtime.md#rt-rte-maintain-knowledge"
          note: "Copy provenance is known at this step; source-content provenance remains inherited and unresolved."
        - scope: "Nondefault retrieval-weight initialization"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "The setter persists supplied coefficients, but accepted records do not identify a production supplier or their derivation. No controlled lineage is established."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-direct-import"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-relationships"
        - "memory.md#mem-obj-tier"
        - "epistemic.md#epi-rte-rule-retention"
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-document-versions"
        - "runtime.md#rt-rte-maintain-knowledge"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Positive derivation paths coexist with unresolved upstream document/model provenance and weight initialization; a known transformer does not close those gaps."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Body, summary and descriptive graph content delivered to requesting humans/agents and internal synthesis input"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-relationships"
                - "runtime.md#rt-rte-retrieve-context"
                - "runtime.md#rt-bap-knowledge-delivery"
              note: "Retained prose supplies reference/context to callers and selected summaries supply model input; host obedience is not established."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-retrieve-context"
            - "runtime.md#rt-bap-knowledge-delivery"
          note: "Tool-result content is informational, not standing host instruction."
        - scope: "Document lexical content, vectors, graph connectivity and created-at metadata in hybrid retrieval"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-tier"
                - "runtime.md#rt-rte-retrieve-context"
              note: "FTS, cosine similarity, graph connections and recency alter candidate priority under fixed scoring code."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-tier"
            - "runtime.md#rt-rte-retrieve-context"
          note: "Tier/access_count and persisted weight setters are not silently added to this ranking consumer."
        - scope: "Type/project/entity/relationship metadata at filters, dossiers, diagnostics and inference selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tier"
                - "memory.md#mem-obj-relationships"
                - "runtime.md#rt-rte-retrieve-context"
                - "memory.md#mem-rte-issue-delivery"
                - "epistemic.md#epi-rte-rule-derivation"
              note: "Retained labels, mentions and predicates select candidate sets, diagnosis matches and graph derivation inputs."
          records:
            - "memory.md#mem-obj-tier"
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-retrieve-context"
            - "memory.md#mem-rte-issue-delivery"
            - "epistemic.md#epi-rte-rule-derivation"
          note: "This is scope/input selection; the static rule bodies themselves are not accumulated memory."
        - scope: "Retained object identities and importer dedup markers at admission checks"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-relationships"
                - "runtime.md#rt-rte-direct-import"
                - "epistemic.md#epi-rte-structure-check"
              note: "Existing endpoints and prior import hash/title state determine admissibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-relationships"
                - "runtime.md#rt-rte-direct-import"
                - "epistemic.md#epi-rte-structure-check"
              note: "Missing endpoints and duplicate-import matches cause software to skip candidate writes."
          records:
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-direct-import"
            - "epistemic.md#epi-rte-structure-check"
          note: "These retained criteria have actual reject/skip consumers, unlike unconsumed metadata. Static schemas/transport policy are excluded."
        - scope: "Access metadata at promotion, and promoted tier at subsequent enrichment"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-tier"
              note: "Retained experience counters feed a durable tier update; no parameter training or measured improvement follows."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-tier"
              note: "Count threshold selects promotion; retained reflex tier selects enrichment preservation rather than reclassification."
          records:
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-obj-tier"
          note: "The update consumer and later tier-preservation consumer have distinct effects. Tier presentation is informational, not a ranking coefficient."
        - scope: "Query-log entries at diagnostic trail consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-query-log"
              note: "Admin/dashboard trail reads supply past queries and result IDs for inspection."
          records:
            - "memory.md#mem-obj-query-log"
          note: "No automatic policy update is attributed to raw log display."
        - scope: "Persisted weight coefficients and historical row versions without shipped later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-obj-document-versions"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "Library get/read APIs do not establish an actual ranking, instruction, validation or recovery consumer. Their behavioral authority cannot be classified from these records."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-relationships"
        - "runtime.md#rt-rte-retrieve-context"
        - "runtime.md#rt-bap-knowledge-delivery"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-tier"
        - "memory.md#mem-rte-issue-delivery"
        - "epistemic.md#epi-rte-rule-derivation"
        - "runtime.md#rt-rte-direct-import"
        - "epistemic.md#epi-rte-structure-check"
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Actual consumer effects are classified separately. Dormant persisted weights/history prevent complete consumer-authority coverage; no instruction priority is inferred from prose and no learning benefit from usage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Per-content decision supplying original capture/edit/classification fields"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-pipeline"
            - "runtime.md#rt-rte-maintain-knowledge"
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
          note: "Generic caller identity does not establish an explicit human decision or autonomous caller admission; upstream content control remains unresolved."
        - scope: "Importer mapping, dedup and per-item admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-direct-import"
              note: "Code selects/skips/maps input rows/files without a per-item human approval decision."
          records:
            - "runtime.md#rt-rte-direct-import"
          note: "An operator starting import is not manual admission of each mapped object; upstream file authorship remains separate."
        - scope: "Internal normalization, embedding replacement, link/entity admission, enrichment and inferred-edge writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-pipeline"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-tier"
                - "epistemic.md#epi-rte-metadata-admission"
                - "epistemic.md#epi-rte-rule-retention"
              note: "Software/model admission writes transformed parts without explicit approval of each result."
          records:
            - "runtime.md#rt-rte-capture-pipeline"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-tier"
            - "epistemic.md#epi-rte-metadata-admission"
            - "epistemic.md#epi-rte-rule-retention"
          note: "Includes optional model branches and deterministic rules; source-level wiring is not observed execution."
        - scope: "Read/feedback-derived counters and tier writes; query logging; before-update row snapshots"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-query-log"
                - "memory.md#mem-obj-document-versions"
              note: "Code writes these retained artifacts as consequences of activity/update, without a separate content approval."
          records:
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-document-versions"
          note: "Caller action triggers the workflow but does not manually approve generated counts, logs or snapshots."
        - scope: "Explicit whole-store replacement by restore"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-knowledge"
              note: "The operator-triggered restore explicitly replaces retained stores with the selected archive."
          records:
            - "runtime.md#rt-rte-maintain-knowledge"
          note: "This separately evidenced replacement decision does not make ordinary pipeline admissions manual."
        - scope: "Nondefault weight-content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "Setter/reset APIs and absent shipped adaptation callers leave the decision supplying nondefault values unresolved."
      records:
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-maintain-knowledge"
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-direct-import"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-relationships"
        - "memory.md#mem-obj-tier"
        - "epistemic.md#epi-rte-metadata-admission"
        - "epistemic.md#epi-rte-rule-retention"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Automatic transformations and an explicit operator replacement coexist with unresolved generic-caller content decisions and weight initialization. Neither entry channel nor physical I/O establishes manual agency."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Importer duplicate exclusion"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-direct-import"
              note: "Hash/title checks prevent repeat retention of matching imported content."
          records:
            - "runtime.md#rt-rte-direct-import"
          note: "This is content-level import dedup, not merely a generated object-ID collision check."
        - scope: "Internal model summary of retained body"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-rte-capture-pipeline"
                - "epistemic.md#epi-rte-metadata-generation"
              note: "The implemented route requests a short account of already retained text for later briefing."
          records:
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-rte-capture-pipeline"
            - "epistemic.md#epi-rte-metadata-generation"
          note: "The summary request affords reduction of existing claims. No actual output establishes faithful consolidation versus added claims; caller summaries and title fallback are separate paths."
        - scope: "Explicit edit/classify and successful vector replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-maintain-knowledge"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-embeddings"
              note: "Existing row fields and per-ID vectors can be replaced; this does not guarantee coordinated summary/vector/graph refresh."
          records:
            - "runtime.md#rt-rte-maintain-knowledge"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-embeddings"
          note: "Update route is implemented; correctness and freshness of all related parts are not established."
        - scope: "Access-threshold and enrichment tier changes"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-tier"
              note: "Ten accumulated accesses can raise tier to reflex; enrichment can raise archive to recall when summary/confidence qualify."
          records:
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-obj-tier"
          note: "Promotion is durable salience metadata, not physical migration or learned scoring."
        - scope: "Recency weighting and exposed inactivity-tier adjustment"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-tier"
                - "runtime.md#rt-rte-retrieve-context"
              note: "Created-at age downweights retained entries in hybrid retrieval."
            - value: "decay"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-abs-adaptation-wiring"
              note: "The exposed inactivity adjustment can demote old reflex entries, but no shipped scheduled caller is established."
          records:
            - "memory.md#mem-obj-tier"
            - "runtime.md#rt-rte-retrieve-context"
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "Wired recency scoring and afforded inactivity maintenance retain separate bases."
        - scope: "Model-derived relationship/property meaning and other potentially novel retained claims"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-relationships"
            - "epistemic.md#epi-rte-metadata-generation"
            - "epistemic.md#epi-rte-metadata-admission"
          note: "Model outputs are not supplied; whether they add claims absent from inputs cannot be decided. No synthesis operation is established merely by a route name or a transient narrative."
      records:
        - "runtime.md#rt-rte-direct-import"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-rte-capture-pipeline"
        - "epistemic.md#epi-rte-metadata-generation"
        - "runtime.md#rt-rte-maintain-knowledge"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-tier"
        - "runtime.md#rt-rte-retrieve-context"
        - "memory.md#mem-abs-adaptation-wiring"
        - "memory.md#mem-obj-relationships"
        - "epistemic.md#epi-rte-metadata-admission"
      note: "Supported curation is not a complete semantic operation inventory: model transformations remain indeterminate. Additive inference, index rebuild and snapshots alone do not imply synthesis, consolidation or invalidation; deleting current content is not evidenced history-preserving withdrawal."
    read_back_direction:
      assessment: "known"
      units:
        - scope: "Requested search/context/read/list/graph/export, dossier and synthesis input selection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-retrieve-context"
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-tier"
              note: "A requesting caller supplies query/topic/ID/scope; code fulfills that request with selected retained material."
          records:
            - "runtime.md#rt-rte-retrieve-context"
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-tier"
          note: "The ranking/projection operations are inside a requested chain, not additional unsolicited deliveries."
        - scope: "Requested status/reason alerts and diagnostic query trail"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-issue-delivery"
                - "memory.md#mem-obj-query-log"
              note: "Status/reason and trail consumers explicitly request the findings/log material."
          records:
            - "memory.md#mem-rte-issue-delivery"
            - "memory.md#mem-obj-query-log"
          note: "Proactive wording does not establish an unsolicited notification route."
        - scope: "Internal reloads for capture processing, inference and access/tier maintenance"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-pipeline"
                - "runtime.md#rt-rte-maintain-knowledge"
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-relationships"
                - "memory.md#mem-obj-tier"
                - "memory.md#mem-obj-access-count"
              note: "Invoked processing asks the stores for current objects, relationships and metadata; those values guide the requested operation."
          records:
            - "runtime.md#rt-rte-capture-pipeline"
            - "runtime.md#rt-rte-maintain-knowledge"
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-obj-relationships"
            - "memory.md#mem-obj-tier"
            - "memory.md#mem-obj-access-count"
          note: "No independent context-injection selector is established for these requested processing reads."
        - scope: "Temporal-version and persisted-weight getter capabilities"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-document-versions"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "Read methods exist but no shipped later consumer is found. They are inventory capabilities, not alternate established read-back directions."
      records:
        - "runtime.md#rt-rte-retrieve-context"
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-relationships"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-tier"
        - "memory.md#mem-rte-issue-delivery"
        - "memory.md#mem-obj-query-log"
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-maintain-knowledge"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Accepted records inventory the shipped consumers as request-driven and explicitly distinguish dormant APIs from routes. External host injection and hypothetical library wiring are excluded. No independent push operation is established in this assessed service boundary."
    read_back_signal:
      assessment: "inapplicable"
      units:
        - scope: "All established requested delivery and processing-read chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-retrieve-context"
            - "memory.md#mem-rte-issue-delivery"
            - "memory.md#mem-obj-query-log"
            - "runtime.md#rt-rte-capture-pipeline"
            - "runtime.md#rt-rte-maintain-knowledge"
            - "memory.md#mem-rte-access-promotion"
          note: "The assessed chains are pull: query/ID/budget inputs select requested material, not independent push deliveries. Therefore no push selector signal applies."
        - scope: "Dormant weight/history getter APIs"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-document-versions"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "No established later read-back route exists for these capabilities, so no push selection operation exists to classify."
      records:
        - "runtime.md#rt-rte-retrieve-context"
        - "memory.md#mem-rte-issue-delivery"
        - "memory.md#mem-obj-query-log"
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-maintain-knowledge"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Inapplicable to this completely assessed direction inventory: all established read-back chains are pull, and the remaining inventoried getters have no shipped consumer. IDs and lexical/embedding selectors on a request are not push signals."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Successful read/positive-feedback activity to access counters, tier promotion and later briefing/enrichment"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-rte-access-promotion"
                - "memory.md#mem-obj-tier"
              note: "Automatic activity-fed writes produce persistent tier/control metadata read by later consumers; this qualifies without new knowledge or measured gain."
          records:
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-rte-access-promotion"
            - "memory.md#mem-obj-tier"
          note: "Raw event reasons are not preserved; count/tier adaptation is wired, not observed benefit."
        - scope: "Automatic content-to-summary/vector/link routes with generic captured/imported source material"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-capture-pipeline"
            - "runtime.md#rt-rte-direct-import"
            - "epistemic.md#epi-rte-metadata-generation"
          note: "Inputs can be ordinary documents; no accepted record establishes whether particular retained inputs are session/tool/environment traces. A qualifying trace-fed route cannot be asserted or excluded for all these inputs."
        - scope: "Query-log retention and weight/history capabilities without an automatic update-consumer bridge"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-obj-document-versions"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "Raw diagnostic logging and unchanged snapshots alone do not qualify; searched absence of the shipped adaptation bridge prevents treating helper names as automatic training. No system-wide negative follows."
      records:
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-tier"
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-relationships"
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-direct-import"
        - "epistemic.md#epi-rte-metadata-generation"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Access-derived adaptation supplies a positive witness. Generic content provenance leaves other possible trace-fed transformations unresolved; raw query retention and unwired weight helpers do not upgrade that witness to measured learning."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Read and positive-feedback tool interactions consumed by access/tier update"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-count"
                - "memory.md#mem-rte-access-promotion"
              note: "Successful tool reads and feedback requests supply the recorded interaction signal converted to counts/tier."
          records:
            - "memory.md#mem-obj-access-count"
            - "memory.md#mem-rte-access-promotion"
          note: "Original source is tool-use/relevance activity, not conversational messages inferred from the MCP adapter. Human/model origin of the relevance judgment is unresolved but does not change the recorded tool-interaction source."
        - scope: "Possible trace-bearing generic documents consumed by automatic summary/vector/link processing"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-relationships"
            - "runtime.md#rt-rte-capture-pipeline"
            - "runtime.md#rt-rte-direct-import"
          note: "No source-content record identifies conversational logs, tool traces, event streams or linked state/action/outcome experience in these generic inputs. Missing original input content prevents classification."
        - scope: "Raw query trail and dormant nonqualifying capabilities"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-query-log"
            - "memory.md#mem-obj-retrieval-weights"
            - "memory.md#mem-obj-document-versions"
            - "memory.md#mem-abs-adaptation-wiring"
          note: "No qualifying automatic durable behavior-update route is established here; diagnostic retention alone has no trace-learning source classification."
      records:
        - "memory.md#mem-obj-access-count"
        - "memory.md#mem-rte-access-promotion"
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-embeddings"
        - "memory.md#mem-obj-relationships"
        - "runtime.md#rt-rte-capture-pipeline"
        - "runtime.md#rt-rte-direct-import"
        - "memory.md#mem-obj-query-log"
        - "memory.md#mem-obj-retrieval-weights"
        - "memory.md#mem-obj-document-versions"
        - "memory.md#mem-abs-adaptation-wiring"
      note: "Tool-interaction source is supported for access adaptation, but generic document provenance prevents a complete trace-source inventory. No event-stream or session-log value follows merely from timestamps, session_id fields or import wrappers."
---

# Cortex memory profile

## Comparison rationale

This profile classifies accepted records, not a running installation. All positive implementation findings are wired unless an individual finding is only afforded. No observed operation or causal benefit is supplied. The inventory follows the retained parts in [MEM-OBJ-documents](memory.md#mem-obj-documents), [MEM-OBJ-summary](memory.md#mem-obj-summary), [MEM-OBJ-relationships](memory.md#mem-obj-relationships), [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings), [MEM-OBJ-tier](memory.md#mem-obj-tier), [MEM-OBJ-access-count](memory.md#mem-obj-access-count), [MEM-OBJ-query-log](memory.md#mem-obj-query-log), [MEM-OBJ-retrieval-weights](memory.md#mem-obj-retrieval-weights) and [MEM-OBJ-document-versions](memory.md#mem-obj-document-versions). Recovery and importer admission are separately covered by [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge) and [RT-RTE-direct-import](runtime.md#rt-rte-direct-import).

SQLite vector BLOBs establish SQLite storage and distributed-parametric form, not a separate vector substrate or retained model weights. Symbolic coefficient JSON is not distributed-parametric learning. Dormant weight/history getters remain in the inventory without invented ranking or historical-recovery consumers. The missing shipped bridge is bounded by [MEM-ABS-adaptation-wiring](memory.md#mem-abs-adaptation-wiring).

Requested context ranking, dossier matching, synthesis selection and alerts are pull operations, even when code chooses the returned subset. Their identifiers, lexical scores and embeddings therefore do not establish push-signal values. This distinction follows [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context) and [MEM-RTE-issue-delivery](memory.md#mem-rte-issue-delivery). It says nothing about integrations outside the reviewed service boundary.

Retained counts feed automatic promotion, while the promoted tier is later displayed and preserved by enrichment. The update input has learning authority; its downstream effects are informational and branch-selecting, not a demonstrated hybrid-ranking improvement. This is a wired trace-learning witness under the profile definition, independent of the stronger learning-benefit claim qualified in [MEM-CLM-learning-scope](memory.md#mem-clm-learning-scope). Generic documents may or may not contain traces. Their unresolved original content prevents a system-wide negative or complete trace-source assessment. Query-log retention alone is not another qualifying learning route.

The summary branch requests compression of retained content, so consolidation is afforded; no actual model output establishes faithful reduction or synthesis of a new retained claim. Model-derived relationship meaning remains indeterminate. The transient period narrative is excluded from retained curation, as [EPI-RTE-period-synthesis](epistemic.md#epi-rte-period-synthesis) establishes. Explicit revisions are evolution; deletion and additive supersession do not establish a universal history-preserving invalidation policy.

Reconciliation supersedes the epistemic summary with [MEM-OBJ-summary](memory.md#mem-obj-summary), epistemic access adaptation with [MEM-RTE-access-promotion](memory.md#mem-rte-access-promotion), and epistemic state diagnostics with [MEM-RTE-issue-delivery](memory.md#mem-rte-issue-delivery). All profile citations use these canonical targets. Distinct epistemic generation, checking and rule-retention records remain available for their separate functions. These identity resolutions do not upgrade fidelity, acceptance, operation or benefit.

No frozen source files were read for this classification. The supplied accepted members and their record passages supply the warrants; no new records, quotations or evidence were added.
