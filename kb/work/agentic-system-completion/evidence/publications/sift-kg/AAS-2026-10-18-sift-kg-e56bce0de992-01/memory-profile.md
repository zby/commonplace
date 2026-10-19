---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "sift-kg memory comparison: document-derived caches, graph, reusable schema, decisions and generated sidecars."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
source-identity: https://github.com/juanceresa/sift-kg
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
memory-comparison:
  version: 2
  scope: >-
    Retained extraction records, graph assertions and support, discovered or replacement
    domain guidance, review decisions, communities, descriptions and narrative; their
    reconstruction, maintenance and later extraction, build, narration, retrieval,
    export and view consumers. Transient document summaries are included where later
    chunk invocations consume them. Unspecified public-API writes and opaque provider
    state remain unresolved alternatives, not additional established memory stores.
    Excludes shipped static skill and bundled schemas as accumulated memory, external
    host sessions and final answers, original document storage, and temporary embedding
    and clustering state not established as durable memory.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Extraction JSON, domain YAML, graph JSON, review YAML and generated sidecar/report files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-graph-data, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
              note: "The operative cross-invocation artifacts are serialized filesystem objects, not a database service."
          records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-graph-data, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
          note: "Records identify each local retained artifact and its persistence location."
        - scope: "Reloaded KnowledgeGraph and its retained relation/support parts"
          assessment: known
          findings:
            - value: graph
              basis: wired
              records: [runtime.md#rt-obj-graph-data, memory.md#mem-obj-relation-support]
              note: "NetworkX MultiDiGraph is the operative graph substrate; JSON is its persistent file boundary."
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-obj-graph-data]
              note: "Later stage invocations load and operate on process-resident graph state."
          records: [runtime.md#rt-obj-graph-data, memory.md#mem-obj-relation-support]
          note: "Graph and file findings describe distinct operative parts of one persistence/reload chain."
        - scope: "Parsed extraction/domain/decision/sidecar objects and first-chunk summary reused by later chunk calls"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, runtime.md#rt-rte-document-extraction]
              note: "Parsed objects and the within-job summary are resident process material; the summary is not a persisted summary field."
          records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, runtime.md#rt-rte-document-extraction]
          note: "The summary qualifies only at its later chunk-call consumers, not as an additional cross-session store."
        - scope: "Opaque provider-side state potentially accumulated through service use"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-client]
          note: "Provider-managed state and mutation are uninspected; no memory substrate, including model-weights or service-object, is established for this alternative."
      records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-graph-data, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-rte-document-extraction, runtime.md#rt-cmp-llm-client]
      note: "Local stores are identified; opaque provider state prevents complete coverage. JSON encoding alone does not establish kv, and temporary embeddings do not establish vector storage."
    representational_form:
      assessment: partial
      units:
        - scope: "Extraction/graph names, attributes, contexts and evidence interpreted by later models or readers; generated descriptions, themes, narrative and chunk summary"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-communities, memory.md#mem-obj-narrative, runtime.md#rt-rte-document-extraction]
              note: "Text carries interpreted source assertions or generated context, independently of JSON/YAML serialization."
          records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-communities, memory.md#mem-obj-narrative, runtime.md#rt-rte-document-extraction]
          note: "This unit is the interpreted text path, not its fixed-rule identity or topology path."
        - scope: "IDs, endpoints, type strings, counts, confidence, cache metadata, community memberships and review statuses at fixed-code consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-document-extraction, epistemic.md#epi-obj-graph-assertions, memory.md#mem-obj-relation-support, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities]
              note: "Localized fields drive matching, aggregation, grouping, admission and mutation rules. Names also operate symbolically when matched by fixed string rules."
          records: [memory.md#mem-obj-document-extraction, epistemic.md#epi-obj-graph-assertions, memory.md#mem-obj-relation-support, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities]
          note: "Numbers used as explicit scores/counts are symbolic here, not distributed-parametric memory."
        - scope: "Retained domain descriptions, hints and system context at extraction model prompts; review reasons/evidence at human display"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [epistemic.md#epi-obj-domain-guidance, runtime.md#rt-obj-review-files, runtime.md#rt-rte-review-decisions]
              note: "Guidance requests model interpretation; proposal reasons and evidence inform human interpretation."
          records: [epistemic.md#epi-obj-domain-guidance, runtime.md#rt-obj-review-files, runtime.md#rt-rte-review-decisions]
          note: "Delivery is wired; compliance or correctness is not observed."
        - scope: "Retained domain vocabulary, canonical names, endpoint types, symmetry and review flags at build/review consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [epistemic.md#epi-obj-domain-vocabulary, runtime.md#rt-bap-domain-guidance]
              note: "Selected normalization and review branches consume explicit configuration fields."
          records: [epistemic.md#epi-obj-domain-vocabulary, runtime.md#rt-bap-domain-guidance]
          note: "This separates executable vocabulary from interpreted guidance in the same YAML file."
        - scope: "Opaque provider-side accumulated state"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-client]
          note: "The service component is parametric, but its weights are not thereby established as memory accumulated by this workflow."
      records: [memory.md#mem-obj-document-extraction, runtime.md#rt-obj-graph-data, runtime.md#rt-obj-review-files, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, epistemic.md#epi-obj-domain-guidance, epistemic.md#epi-obj-domain-vocabulary, runtime.md#rt-cmp-llm-client]
      note: "Local interpreted and fixed-rule parts are classified separately; opaque service accumulation prevents complete coverage."
    lineage:
      assessment: partial
      units:
        - scope: "Document-derived summary, extraction records and discovered domain, followed by graph/support/community compilation and generated prose"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, epistemic.md#epi-rte-support-aggregation, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
              note: "Model transformations and deterministic compilation derive retained objects from documents or earlier artifacts, not recorded agent activity."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, epistemic.md#epi-rte-support-aggregation, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
          note: "Known derivation paths do not establish the original documents' authorship or semantic fidelity."
        - scope: "Resolution proposals and threshold-generated review dispositions"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-decisions]
              note: "Model identity comparison, deterministic heuristics and confidence policies produce retained proposals/statuses."
          records: [runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-decisions]
          note: "These are downstream graph-derived decisions, not trace extraction."
        - scope: "Human review dispositions and supported manual YAML edits"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-review-decisions, runtime.md#rt-obj-review-files]
              note: "A human key decision or explicit file edit supplies retained decision content."
          records: [runtime.md#rt-rte-review-decisions, runtime.md#rt-obj-review-files]
          note: "This classifies the supported path, not the unauthenticated provenance of every existing status."
        - scope: "Initial custom schema/content and unspecified direct graph API inputs"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-domain-config, memory.md#mem-obj-document-extraction, runtime.md#rt-obj-graph-data]
          note: "Caller-dependent original authorship and derivation are unspecified. Loading an existing artifact does not resolve its original lineage."
        - scope: "Opaque provider-side accumulation"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-client]
          note: "No provider-side memory provenance was inspected."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-decisions, memory.md#mem-obj-document-extraction, runtime.md#rt-obj-domain-config, runtime.md#rt-cmp-llm-client]
      note: "Known compilation and human-authored decisions coexist with unresolved initialization; ingestion alone does not establish trace-extracted lineage or imported standing instructions."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Graph assertions/support and extraction contexts at narration, graph query and human/agent display consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-agent-retrieval, memory.md#mem-obj-document-extraction, memory.md#mem-obj-relation-support]
              note: "Retained assertions and excerpts supply context/reference; query omits full mentions and node contexts."
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-agent-retrieval, runtime.md#rt-rte-narrative-generation]
              note: "Retained names/aliases and graph degree affect match priority and selected narrative entities/relations under fixed rules."
          records: [runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-agent-retrieval, memory.md#mem-obj-relation-support]
          note: "Ranking input needs no learned ranker; delivered knowledge is not independently certified or demonstrated uptake."
        - scope: "Description prose and community labels at search, view, export and topology consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-communities, memory.md#mem-rte-view-artifacts, memory.md#mem-rte-export-artifacts]
              note: "Actual load/join paths provide descriptions and meaningful labels; library and JSON exports need not join descriptions."
          records: [memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-communities, memory.md#mem-rte-view-artifacts, memory.md#mem-rte-export-artifacts]
          note: "Only recorded consumers are included; browser interaction is not observed."
        - scope: "Full narrative Markdown at optional external human/host file read"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-narrative]
              note: "The optional artifact affords reading, but no concrete automatic pipeline reload of its full prose is wired."
          records: [memory.md#mem-obj-narrative]
          note: "This weaker path is not upgraded by wired description consumers."
        - scope: "Retained domain guidance at later extraction prompts"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [epistemic.md#epi-obj-domain-guidance, runtime.md#rt-bap-domain-guidance]
              note: "Descriptions/hints/system context supply reusable extraction directions, not enforced model compliance."
          records: [epistemic.md#epi-obj-domain-guidance, runtime.md#rt-bap-domain-guidance]
          note: "Shipped static host skill text is excluded; discovered/replacement domain guidance is the accumulated part."
        - scope: "Retained domain vocabulary at canonical/fallback normalization and review-type checks"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [epistemic.md#epi-obj-domain-vocabulary, epistemic.md#epi-rte-relation-flagging]
              note: "Configured vocabulary/endpoint/review criteria assess selected conformity and review eligibility, not factual truth."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-obj-domain-config, epistemic.md#epi-rte-graph-cleanup]
              note: "Canonical/fallback and normalization fields cause actual graph changes where their conditions hold."
          records: [epistemic.md#epi-obj-domain-vocabulary, runtime.md#rt-obj-domain-config, epistemic.md#epi-rte-graph-cleanup, epistemic.md#epi-rte-relation-flagging]
          note: "Missing fallback and retained unfixable mismatches prevent a universal validation guarantee, not these local forces."
        - scope: "Extraction cache metadata and community assignments at reuse/grouping consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-communities, runtime.md#rt-rte-schema-discovery]
              note: "Retained metadata chooses reuse versus extraction/discovery; assignments and cached labels choose grouping and relabeling branches."
          records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-communities, runtime.md#rt-rte-schema-discovery]
          note: "Routing is local to operation/input selection, not inferred from merely storing an ID."
        - scope: "Review reasons/evidence at human display; retained statuses at apply selection and graph mutation"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-obj-review-files, runtime.md#rt-rte-review-decisions]
              note: "Reasons/evidence inform human review; the mutation engine does not execute their prose."
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-apply-decisions, runtime.md#rt-obj-review-files]
              note: "Retained CONFIRMED/REJECTED statuses provide criteria for permitted mutation candidates."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-apply-decisions]
              note: "The engine excludes unconfirmed merges and removes rejected relation keys; confirmed variants are not insertion commands."
          records: [runtime.md#rt-obj-review-files, runtime.md#rt-rte-review-decisions, runtime.md#rt-rte-apply-decisions]
          note: "These forces are separate from an evidence-consuming factual acceptance procedure."
        - scope: "Opaque provider state and unspecified direct-API downstream consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-llm-client, runtime.md#rt-obj-graph-data]
          note: "No actual additional memory consumer/effect is recorded; provider internals are uninspected."
      records: [runtime.md#rt-rte-agent-retrieval, runtime.md#rt-rte-narrative-generation, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-apply-decisions, memory.md#mem-obj-document-extraction, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-cmp-llm-client]
      note: "Local consumer forces are classified separately. No recorded trace-update consumer establishes learning authority; external and opaque alternatives remain unresolved."
    write_agency:
      assessment: partial
      units:
        - scope: "Extraction/discovery admission, graph build, proposal generation, confidence review, apply execution, narration and generated projections"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-decisions, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts]
              note: "Code/model admission proceeds without a per-content human decision. Starting a paid workflow is not manual content admission; apply automatically executes previously admitted decisions."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-decisions, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts]
          note: "This unit covers the implemented software-controlled paths, not every possible source of input files."
        - scope: "Human review keys and explicit operator YAML editing/replacement"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-review-decisions, runtime.md#rt-obj-review-files]
              note: "Explicit human approval/rejection or content edits supply retained decisions at their own admission mechanism."
          records: [runtime.md#rt-rte-review-decisions, runtime.md#rt-obj-review-files]
          note: "No attribution of every saved status to a human follows; automatic paths share the representation."
        - scope: "Initial caller-provided custom schemas/content and arbitrary graph mutation API admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-domain-config, runtime.md#rt-obj-graph-data, memory.md#mem-obj-document-extraction]
          note: "Generic caller identity does not determine human versus software control. A save API affords mutation without establishing its caller's admission mechanism."
        - scope: "Provider-side writes"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-cmp-llm-client]
          note: "Provider mutation/admission was not inspected."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-decisions, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, runtime.md#rt-obj-domain-config, runtime.md#rt-obj-graph-data, runtime.md#rt-cmp-llm-client]
      note: "Known manual and automatic mechanisms do not resolve unspecified initialization or provider control."
    curation_operations:
      assessment: partial
      units:
        - scope: "Canonical mention aggregation, entity deduplication and confirmed graph merges"
          assessment: known
          findings:
            - value: dedup
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-apply-decisions, memory.md#mem-obj-relation-support]
              note: "Implemented routes collapse duplicate entities or equal relation triples; resolve proposals alone are not this transformation."
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-relation-support, runtime.md#rt-rte-apply-decisions]
              note: "Canonical edges aggregate mentions/support into a single relation representation; merges combine retained node attributes/aliases and edges."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-relation-support, runtime.md#rt-rte-apply-decisions]
              note: "Existing edge support/confidence and canonical-node content are revised by aggregation and application."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-apply-decisions, memory.md#mem-obj-relation-support]
          note: "These transformations operate on retained entries; they do not imply independently verified identity."
        - scope: "Graph cleanup/pruning/rejection and retained prose style rewriting"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [epistemic.md#epi-rte-graph-cleanup, runtime.md#rt-rte-narrative-generation]
              note: "Existing relation labels/directions and phrase-flagged prose are revised. Style repair is not evidence of new claims or improved capability."
            - value: decay
              basis: wired
              records: [epistemic.md#epi-rte-graph-cleanup, runtime.md#rt-rte-apply-decisions]
              note: "Pruning and rejection forget selected graph entries by deletion; caches and independent prose may still retain source material."
          records: [epistemic.md#epi-rte-graph-cleanup, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation]
          note: "Deletion is not invalidate with retained history. Postprocess bypass means cleanup is conditional."
        - scope: "Semantic generation of narrative/descriptions/schema and unspecified caller/provider maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-schema-discovery, runtime.md#rt-obj-graph-data, runtime.md#rt-cmp-llm-client]
          note: "Recorded generation does not settle semantic preservation versus synthesis; arbitrary API and opaque provider transformations are not enumerated. No additional controlled operation is established for this unit."
      records: [memory.md#mem-obj-relation-support, runtime.md#rt-rte-apply-decisions, epistemic.md#epi-rte-graph-cleanup, runtime.md#rt-rte-narrative-generation, runtime.md#rt-cmp-llm-client]
      note: "Implemented consolidation, deduplication, revision and forgetting coexist with unresolved transformations. Indexing, acquisition, style prompts and confidence triage alone establish neither promotion nor synthesis."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Explicit graph query/topology/search, build/resolve/apply/narrate reloads, export and view requests"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-agent-retrieval, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts]
              note: "Caller-requested operations reload retained inputs and return the requested projection; delivery of that response is not a second unsolicited push."
          records: [runtime.md#rt-rte-agent-retrieval, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts]
          note: "Host session orientation remains a requested CLI read, even when prescribed by static skill text."
        - scope: "Optional full narrative file read by human/host"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-obj-narrative]
              note: "Optional file availability affords requested reading without establishing a wired host reload."
          records: [memory.md#mem-obj-narrative]
          note: "This route retains its weaker basis separately."
        - scope: "Reusable domain and first-chunk summary supplied automatically to later chunk model calls"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction]
              note: "Extraction code supplies cached domain guidance and the summary to later model invocations without a request by that model for those retained parts. This internal input assembly is distinct from requested CLI return."
          records: [runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction]
          note: "Wired prompt supply establishes direction, not model compliance or persistent summary storage."
        - scope: "Provider-side accumulated-state read-back and unspecified API consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-llm-client, runtime.md#rt-obj-graph-data]
          note: "No recorded chain resolves their request/selection/delivery operations."
      records: [runtime.md#rt-rte-agent-retrieval, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-narrative-generation, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts, memory.md#mem-obj-narrative, runtime.md#rt-cmp-llm-client]
      note: "Requested external reads and automatic internal context supply coexist. Opaque alternatives prevent complete directional coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic domain and document-summary supply at chunk-call construction"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-document-extraction]
              note: "Trigger is extraction/chunk invocation. Selector inputs are schema-free/cache/force settings and the current document's prepared summary; selected parts are the reusable domain and summary supplied broadly to chunks, not semantic query matches."
          records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-document-extraction]
          note: "A file path or document stem alone does not establish targeted identifier push; the recorded operation is availability/configuration-based context supply."
        - scope: "Requested query/topology/search/export/view and stage-input reload operations"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-agent-retrieval, memory.md#mem-rte-export-artifacts, memory.md#mem-rte-view-artifacts, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-narrative-generation]
          note: "These classified operations fulfill requests; exact IDs, substring matching and BFS here are pull selection, not push signals."
        - scope: "Opaque provider-state supply and unspecified external API consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-llm-client, runtime.md#rt-obj-graph-data]
          note: "Their direction and actual push selectors are not recorded, so they are not made inapplicable by known pull routes."
      records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-agent-retrieval, runtime.md#rt-cmp-llm-client]
      note: "Coarse internal supply is classified; no inferred-embedding push follows from temporary resolution clustering, and external pull identifiers do not establish identifier push."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Document extraction, schema discovery, graph compilation, decision review/application and output-fed prose correction"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-decisions, runtime.md#rt-rte-apply-decisions, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction]
          note: "These records establish document-derived and output-fed writes, not a qualifying activity/experience-trace-fed chain. No canonical evidenced-absence record warrants a local no; document ingestion and automatic revision alone warrant no yes."
        - scope: "Unspecified direct-API writes, unavailable host sessions and opaque provider-side updates"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-graph-data, runtime.md#rt-bap-host-skill, runtime.md#rt-cmp-llm-client]
          note: "Actual input provenance, automatic durable update and later consumer are not established. The static host skill and uninspected provider cannot close that chain."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-narrative-generation, runtime.md#rt-obj-graph-data, runtime.md#rt-cmp-llm-client]
      note: "No supported controlled finding exists. Neither a system-wide no nor yes follows; absence of run evidence is not absence of a route."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Original inputs to any qualifying automatic trace-fed write in the local document/graph/prose routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-narrative-generation]
          note: "Records identify documents and derived outputs, but no qualifying trace-learning write or original trace content. Document format alone does not classify session-logs, tool-traces, event-streams or trajectories."
        - scope: "Potential trace inputs of unspecified API, external host or opaque provider updates"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-graph-data, runtime.md#rt-bap-host-skill, runtime.md#rt-cmp-llm-client]
          note: "Original content/origin and qualifying update consumption are unknown; no complete bounded negative makes source inapplicable."
      records: [memory.md#mem-obj-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-narrative-generation, runtime.md#rt-obj-graph-data, runtime.md#rt-cmp-llm-client]
      note: "Unresolved learning coverage propagates to source coverage; imported documents must not be relabeled as activity events."
---

# sift-kg memory profile

## Comparison rationale

The comparison distinguishes filesystem persistence from the operative graph and
parsed process objects. It also separates symbolic graph/control fields from
interpreted assertions, excerpts and guidance. The same JSON or YAML container
can support both forms without making either a model-weight store. The optional
embedding encoder and its temporary cluster state do not establish accumulated
vector memory ([RT-OBJ-graph-data](runtime.md#rt-obj-graph-data),
[RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer)). Provider
state remains an explicitly unresolved alternative, not an asserted second
memory implementation ([RT-CMP-llm-client](runtime.md#rt-cmp-llm-client)).

The supported local lineage is compilation from documents and earlier artifacts,
plus human-authored review decisions. Initial custom content remains unresolved.
Software admission remains automatic even when a person starts the command;
human review keys and explicit edits are separate manual mechanisms
([MEM-OBJ-document-extraction](memory.md#mem-obj-document-extraction),
[RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions)). No evidence upgrades
wired routes to observed operation or causal benefit.

Authority follows actual consumption. Retained schema guidance instructs later
extraction; symbolic schema fields validate or enforce particular build/review
rules. Decision statuses validate executable choices and enforce graph changes.
Graph degree and names influence relative selection without requiring a learned
ranker. Reasons shown to a reviewer do not become engine-executed justifications
([RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance),
[EPI-OBJ-domain-vocabulary](epistemic.md#epi-obj-domain-vocabulary),
[RT-OBJ-review-files](runtime.md#rt-obj-review-files),
[RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval)).

Curation includes actual duplicate merging, support aggregation, revision and
deletion. Deleting a rejected graph relation is forgetting at that store, not
history-preserving invalidation or synchronized withdrawal from every artifact.
Rebuild can restore it from extraction caches. Generation and style correction
do not establish synthesis of a new claim; semantic preservation is locally
unsettled ([MEM-OBJ-relation-support](memory.md#mem-obj-relation-support),
[RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions),
[EPI-RTE-graph-cleanup](epistemic.md#epi-rte-graph-cleanup),
[RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)).

External retrieval is pull. Internal chunk-call construction automatically
supplies reusable domain guidance and the first-chunk summary, so that separate
consumer path is push. This does not reinterpret requested stdout as unsolicited
host delivery. Its recorded selection is coarse availability/configuration-based
supply, not embedding retrieval or targeted identity matching. The summary is
within-job retained context consumed by later calls, not a disk checkpoint
([RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval),
[RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery),
[RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance),
[RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)).

Trace learning remains not determinable. Document-derived reusable guidance is a
behavior-shaping artifact, but its recorded source is not established as an
activity trace. Output-fed prose repair likewise does not establish a recorded
experience-to-durable-update chain. There are no canonical absence declarations
to support a local negative, and no qualifying trace source is established.
Unknown API/provider alternatives cannot be discarded to derive a system-wide
negative ([MEM-OBJ-document-extraction](memory.md#mem-obj-document-extraction),
[RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery),
[RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation),
[RT-CMP-llm-client](runtime.md#rt-cmp-llm-client)).

Reconciliation supersedes the epistemic extraction-object and graph-support
identities with [MEM-OBJ-document-extraction](memory.md#mem-obj-document-extraction)
and [MEM-OBJ-relation-support](memory.md#mem-obj-relation-support). Those canonical
objects carry this profile's citations; their source-native identity resolution
changes no evidence strength or consumer force. The valid domain and graph
containers, their material parts, and the separately retained prose artifacts
remain distinct. The narrative's afforded reading is not upgraded by the wired
description sidecar route ([MEM-OBJ-narrative](memory.md#mem-obj-narrative),
[MEM-OBJ-entity-descriptions](memory.md#mem-obj-entity-descriptions)).

Source-read log: none. Classification used only the supplied accepted members
and reconciliation; no source ambiguity required a new frozen-source read.
