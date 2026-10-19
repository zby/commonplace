---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "sift-kg memory comparison: retained document-derived knowledge, discovered guidance, review controls and later-consumer routes."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
source-identity: https://github.com/juanceresa/sift-kg
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
memory-comparison:
  version: 2
  scope: >-
    Per-document extraction results; discovered domain guidance; saved graph entities,
    provenance and relation support; merge proposals and relation-review controls;
    community assignments and labels; entity descriptions and narrative; generated
    presentation/export copies; their admission, maintenance and later consumption.
    Includes internal model-input selection as well as caller-facing retrieval.
    Excludes static shipped skills/domains/configuration, transient document summaries,
    chunk windows and vectors, dependency/model weights, external provider retention
    and the host agent's independently managed session memory. These excluded runtime
    parts are not asserted to be absent.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Extraction JSON, discovered YAML, review YAML, communities, descriptions and narrative"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
              note: "Named retained artifacts are filesystem files; JSON/YAML are encodings, not extra substrates."
          records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
          note: "These seven records inventory the non-graph primary retained artifacts."
        - scope: "Retained graph entity/provenance and canonical relation-support state"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support]
              note: "graph_data.json persists graph state between invocations."
            - value: graph
              basis: wired
              records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support]
              note: "NetworkX MultiDiGraph is the operative loaded graph substrate, not a separate vector store."
          records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support]
          note: "The two graph parts share persistence but retain different content and aggregation rules."
        - scope: "Generated HTML and export copies"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-view-export]
              note: "Requested HTML, JSON, GraphML, GEXF and CSV outputs are saved reader artifacts."
            - value: sqlite
              basis: wired
              records: [runtime.md#rt-rte-view-export]
              note: "SQLite is an additional supported export substrate, not the primary graph store."
          records: [runtime.md#rt-rte-view-export]
          note: "Export formats are covered by the accepted presentation route; external readers are not characterized."
      records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-rte-view-export]
      note: "Inventory covers the named retained artifacts and generated copies. Transient Python wrappers and externally managed weights are not additional accumulated memory objects."
    representational_form:
      assessment: known
      units:
        - scope: "Names, evidence, contexts, schema descriptions, proposal reasons, themes, descriptions and narrative at interpreting readers/models"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions]
              note: "These retained text parts reach model, review, retrieval or presentation consumers through language interpretation."
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-narrative]
              note: "Whole-narrative semantic reading is afforded to external readers; no later programmatic semantic consumer is established."
          records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative]
          note: "Textual content is distinct from its enclosing typed structures; narrative's afforded reader does not acquire wired uptake from the sidecars."
        - scope: "Typed extraction/cache metadata, graph identities/edges/support, domain constraints, statuses, sidecar keys and export structure at fixed-code consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, runtime.md#rt-rte-view-export]
              note: "Localized keys, relationships, numerical metadata and control fields have fixed software interpretations. Numeric confidence is not parametric memory."
          records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, runtime.md#rt-rte-view-export]
          note: "Symbolic and natural-language parts coexist without making the retained graph distributed-parametric."
      records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-rte-view-export]
      note: "The retained inventory has text and fixed-rule structure; excluded transient embeddings and external weights do not classify these files as parametric."
    lineage:
      assessment: known
      units:
        - scope: "Document assertions carried into extraction evidence, contexts and names"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-document-extraction, runtime.md#rt-rte-document-extraction]
              note: "External document content supplies the retained assertions; unknown source truth does not obscure the acquisition path."
          records: [memory.md#mem-obj-document-extraction, runtime.md#rt-rte-document-extraction]
          note: "Classifies documentary origin, not verbatim fidelity, raw-document retention or the documents' upstream authorship."
        - scope: "Model-produced extraction interpretations, discovered definitions, resolution reasons and derived prose/themes"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-narrative-generation]
              note: "Models formulate retained content from selected inputs; authored does not mean human-approved or semantically novel."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-narrative-generation]
          note: "All named generative paths are wired; their individual outputs and semantic fidelity remain unobserved."
        - scope: "Aggregated extraction/graph/support, code-generated proposals/flags/statuses, community membership and presentation copies"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-view-export, memory.md#mem-obj-relation-support, memory.md#mem-obj-communities]
              note: "Software derives durable structured parts from documents, retained records or reviewer decisions, not agent execution traces."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-view-export, memory.md#mem-obj-relation-support, memory.md#mem-obj-communities]
          note: "Includes non-model derivations and copy/format paths, not dependency embedding provenance."
        - scope: "Explicit human schema replacement and interactive review decisions"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [runtime.md#rt-rte-schema-discovery]
              note: "The recorded edit/replace surface affords human-authored discovered guidance."
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-review-application]
              note: "Interactive choices become retained status content; generic direct file writers are not thereby authenticated humans."
          records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-review-application]
          note: "The alternative human paths remain distinct from automatic generation."
      records: [memory.md#mem-obj-document-extraction, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-view-export, memory.md#mem-obj-relation-support, memory.md#mem-obj-communities]
      note: "Coverage concerns in-boundary derivation paths, not factual warrant or pre-import source history. Mixed imported, authored and compiled parts retain their separate warrants."
    behavioral_authority:
      assessment: known
      units:
        - scope: "Extraction/graph/support, descriptive sidecars, community labels and proposal reasons at model, reviewer and reader consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, runtime.md#rt-rte-graph-retrieval, runtime.md#rt-rte-view-export]
              note: "Retained assertions, contexts and reasons supply reference/context, not guaranteed truth, to actual consumers."
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-narrative]
              note: "Narrative can inform an external reader; existence testing alone is not semantic consumption."
          records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-rte-graph-retrieval, runtime.md#rt-rte-view-export]
          note: "Reason strings inform review but do not themselves enforce surgery."
        - scope: "Retained discovered-domain descriptions and symbolic constraints at extraction/build"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-obj-discovered-domain, runtime.md#rt-bap-domain-guidance]
              note: "Reloaded natural-language definitions direct later extraction; model compliance remains unobserved."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-discovered-domain, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-graph-build]
              note: "Configured symbolic canonical/type rules drive fixed graph transformations rather than advisory text alone."
          records: [memory.md#mem-obj-discovered-domain, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-graph-build]
          note: "Neither semantic schema adequacy nor universal rejection of out-of-schema content follows from these effects."
        - scope: "Extraction cache metadata and saved community/cache state selecting subsequent work"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, memory.md#mem-obj-document-extraction, memory.md#mem-obj-communities, runtime.md#rt-rte-narrative-generation]
              note: "Model/domain/chunk metadata selects reuse versus processing; themed-label cache selects bypass of detection/naming."
          records: [runtime.md#rt-rte-document-extraction, memory.md#mem-obj-document-extraction, memory.md#mem-obj-communities, runtime.md#rt-rte-narrative-generation]
          note: "These are operation-selection effects, not evidence that cached content is current."
        - scope: "Retained names/aliases and graph adjacency at lookup and narration priority selection"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-graph-retrieval, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-graph-data]
              note: "Stored names/aliases affect matching and stored topology determines ambiguous-match degree order and narration's top-entity priorities."
          records: [runtime.md#rt-rte-graph-retrieval, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-graph-data]
          note: "Fixed ranking code still consumes retained ranking inputs; no learned ranking policy is implied."
        - scope: "Merge and relation-review statuses at surgery admission"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
              note: "CONFIRMED status and existing node IDs determine eligibility for merge application."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
              note: "Nonconfirmed proposals cannot enter surgery; rejected relation statuses cause matching-edge removal."
          records: [runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
          note: "Operational status control is not factual acceptance, a retrieval quarantine or confirmed-variant insertion."
      records: [memory.md#mem-obj-document-extraction, memory.md#mem-obj-discovered-domain, memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, memory.md#mem-obj-communities, memory.md#mem-obj-entity-descriptions, memory.md#mem-obj-narrative, runtime.md#rt-bap-domain-guidance, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-graph-retrieval, runtime.md#rt-rte-view-export]
      note: "Covers actual retained-part consumers, not the static skill's authority or an inferred learning effect from mere persistence."
    write_agency:
      assessment: partial
      units:
        - scope: "Extraction, discovery, build, proposal generation, threshold review, surgery and narration/export admissions"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-view-export]
              note: "Software/model decisions admit specific retained outputs without a per-content human decision; starting the workflow does not make them manual."
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-view-export]
          note: "Automatic threshold decisions are separate from interactive decisions even when software writes both to YAML."
        - scope: "Interactive human review and explicit human schema replacement"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-review-application]
              note: "A human explicitly approves/rejects remaining proposals, supplying the retained status."
            - value: manual
              basis: afforded
              records: [runtime.md#rt-rte-schema-discovery]
              note: "Users can edit or replace discovered guidance; this is a separate admission alternative from automatic discovery."
          records: [runtime.md#rt-rte-review-application, runtime.md#rt-rte-schema-discovery]
          note: "No exercised human decision or universal approval requirement is claimed."
        - scope: "Generic direct file editing/replacement outside the explicitly human paths"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
          note: "Direct YAML replacement is an included alternative but file-writer identity does not establish human versus software admission."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-view-export, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
      note: "Both manual and automatic witnesses survive; unidentified alternate writers prevent complete agency classification."
    curation_operations:
      assessment: partial
      units:
        - scope: "Aggregation and deduplication of retained extraction/graph content and confirmed merge surgery"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application]
              note: "Entity/source/attribute and relation-support aggregation combine existing retained claims into reduced graph representations."
            - value: dedup
              basis: wired
              records: [runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application]
              note: "Pre-dedup collapses near-identical names and confirmed surgery removes duplicate members."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, runtime.md#rt-rte-review-application]
              note: "Existing entity attributes, representative evidence and incident edges are revised in place."
          records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application]
          note: "These are implemented transformations, not guarantees that proposed identity equivalences are true."
        - scope: "Rejected relation application with retained review decision"
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [memory.md#mem-obj-relation-review, runtime.md#rt-rte-review-application]
              note: "Rejected triples are withdrawn from the current graph while the rejection control remains in YAML; rebuild can restore extraction-derived edges."
          records: [memory.md#mem-obj-relation-review, runtime.md#rt-rte-review-application]
          note: "This is bounded operational withdrawal, not versioned graph history or coordinated sidecar retraction."
        - scope: "Conditional undefined TRAVELED_FROM normalization to TRAVELED_TO"
          assessment: known
          findings:
            - value: synthesize
              basis: wired
              records: [epistemic.md#epi-rte-relation-normalization]
              note: "The recorded countermodel establishes a new destination claim not entailed by the retained origin claim under the named conditions."
          records: [epistemic.md#epi-rte-relation-normalization]
          note: "Specific implemented mapping only; no observed incident or blanket synthesis classification of normalization."
        - scope: "Model-produced narrative/descriptions/themes and their style rewrites over retained graph/context"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-narrative-generation, epistemic.md#epi-rte-style-rewrite]
          note: "Recorded intent is summarization/preservation, but paired semantic evidence does not settle consolidation versus new claims for model outputs. Style rewriting replaces current-generation prose before persistence; the records do not establish loading and revising an existing retained prose entry, so this unit does not establish evolve."
      records: [memory.md#mem-obj-graph-data, memory.md#mem-obj-relation-support, memory.md#mem-obj-relation-review, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, epistemic.md#epi-rte-relation-normalization, epistemic.md#epi-rte-style-rewrite]
      note: "Supported graph aggregation, revision, withdrawal and conditional synthesis remain positive; unresolved model transformations prevent a complete curation inventory. Acquisition, rebuild alone and confidence arithmetic are not separate curation operations."
    read_back_direction:
      assessment: known
      units:
        - scope: "Requested query/search/topology/info, direct small-graph reading and view/export"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-graph-retrieval, memory.md#mem-rte-project-info, runtime.md#rt-rte-view-export]
              note: "The caller requests saved material; code selection and stdout/file delivery fulfill that request."
            - value: pull
              basis: afforded
              records: [runtime.md#rt-bap-agent-skill, memory.md#mem-obj-narrative]
              note: "The host may request/read the whole small graph; external readers may read the saved narrative."
          records: [runtime.md#rt-rte-graph-retrieval, memory.md#mem-rte-project-info, runtime.md#rt-rte-view-export, runtime.md#rt-bap-agent-skill, memory.md#mem-obj-narrative]
          note: "Session-start instructions are not an implemented push scheduler."
        - scope: "Automatic retained-input supply within extraction/build, resolution, narration and application"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation]
              note: "On stage invocation software supplies reusable domain/cache, retained extraction, selected graph and status material to subsequent consumers without those consumers requesting those retained parts."
          records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation]
          note: "Internal selected-input supply is separate from the upstream caller's workflow request and from requested CLI return delivery."
      records: [runtime.md#rt-rte-graph-retrieval, memory.md#mem-rte-project-info, runtime.md#rt-rte-view-export, runtime.md#rt-bap-agent-skill, memory.md#mem-obj-narrative, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation]
      note: "Both caller-facing pull and internal push are covered. No automatic injection into an external host session is established."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Stage-triggered domain/cache/extraction reload and structural/cap-limited graph payload supply"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-narrative-generation]
              note: "Stage entry triggers selection by file availability/configuration, errored-document exclusion, type/batch boundaries, degree and caps; selected definitions/extractions/graph subsets feed code or model consumers."
          records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-narrative-generation]
          note: "Structural and availability filters are not semantic relevance judgments or identifiers merely because files have names."
        - scope: "Narration description-context joins and application status-to-graph matching"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction, runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
              note: "During description generation normalized entity-name equality selects retained contexts; application matches retained canonical/member IDs and rejected endpoint/type triples to graph parts."
          records: [runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction, runtime.md#rt-rte-review-application, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review]
          note: "These are actual retained-part joins, not requested filenames. Name-only joins can conflate same-name entities."
        - scope: "Optional embedding-clustered resolution batches"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [runtime.md#rt-rte-entity-resolution, runtime.md#rt-cmp-sentence-transformer]
              note: "Resolution invocation with embeddings enabled encodes retained names/aliases and clusters them to select candidate batches delivered to the resolution model."
          records: [runtime.md#rt-rte-entity-resolution, runtime.md#rt-cmp-sentence-transformer]
          note: "Fallback sorted batches are covered by coarse selection; embeddings are transient selection inputs, not durable vector memory."
        - scope: "Dependency-internal SemHash selection feeding canonical graph construction"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-cmp-sem-hash, runtime.md#rt-rte-graph-build]
          note: "Similarity-based pre-dedup affects which retained names survive, but internal representations/selection details remain uninspected; its model label alone does not establish a complete push-signal classification."
      records: [runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-entity-resolution, runtime.md#rt-rte-narrative-generation, runtime.md#rt-rte-review-application, memory.md#mem-obj-document-extraction, memory.md#mem-obj-merge-proposals, memory.md#mem-obj-relation-review, runtime.md#rt-cmp-sentence-transformer, runtime.md#rt-cmp-sem-hash]
      note: "Signals classify automatic selected-input supply, not exact-ID or substring requests at the pull interface. The dependency-internal selector prevents complete coverage."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Document extraction/discovery, retained graph maintenance, review and narration writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction]
          note: "The records establish document-fed transformations and decision metadata, not a qualifying automatic trace-fed durable update. They do not carry a bounded absence finding covering all possible document content and review-feedback origins, so a controlled no is not asserted."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-graph-build, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction]
      note: "Neither persistence nor schema-conditioned behavior alone establishes trace learning. No yes witness or sufficiently bounded no warrant is available in these accepted records."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Original inputs to any qualifying trace-fed write within the retained-memory routes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction]
          note: "No qualifying trace-fed route is established and document-content origin is not exhaustively typed as session logs, tool traces, events or trajectories. Unknown qualification is not inapplicability."
      records: [runtime.md#rt-rte-document-extraction, runtime.md#rt-rte-schema-discovery, runtime.md#rt-rte-review-application, runtime.md#rt-rte-narrative-generation, memory.md#mem-obj-document-extraction]
      note: "A complete bounded absence of trace learning would license inapplicable; the recorded limitations do not establish that stronger premise."
---

# sift-kg memory profile

## Comparison rationale

The comparison concerns retained artifacts and their consumers, not every stateful component in the runtime. Files carry the primary durable state. The loaded graph is also an operative graph substrate; SQLite belongs only to the export branch. Dependency weights, transient resolution vectors and the first-chunk summary are not additional retained memory stores. The summary supplies current-document context without a retained checkpoint field, as [MEM-OBJ-document-extraction](memory.md#mem-obj-document-extraction) records.

Documentary import, model formulation and fixed-code compilation coexist in the same pipeline. These lineage values do not assert that a model preserves meaning. In particular, the conditional origin-to-destination rewrite supports synthesis through its recorded non-entailment argument, whereas the semantic class of general model prose remains unresolved. See [EPI-RTE-relation-normalization](epistemic.md#epi-rte-relation-normalization) and [EPI-RTE-style-rewrite](epistemic.md#epi-rte-style-rewrite). The latter supports replacement of current-generation prose before persistence, not revision of an existing retained prose entry. It therefore does not establish prose-memory evolution; the separately supported graph-entry evolution remains unchanged.

Authority follows the consumed part. Proposal reasons inform a reviewer; statuses determine surgery eligibility and removals. Cached configuration and labels select future work. Graph content and adjacency affect relative priority even though the ranking algorithm is fixed. Discovered guidance supplies standing instructions and code-consumed constraints; this is not evidence of learning from agent traces. See [MEM-OBJ-merge-proposals](memory.md#mem-obj-merge-proposals), [MEM-OBJ-relation-review](memory.md#mem-obj-relation-review), [MEM-OBJ-communities](memory.md#mem-obj-communities) and [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance).

The caller-facing interface is pull. Internal automatic payload selection is a separate push operation: narration supplies selected retained graph/context to its completion model, and resolution supplies selected identity batches. The host's request to start a stage does not itself request every retained part later supplied to those consumers. Exact-ID lookup requested by a host is not identifier-based push; the name-equality context join inside narration is. Optional embedding clustering remains separate from the opaque SemHash branch. See [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval), [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation), [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) and [RT-CMP-sem-hash](runtime.md#rt-cmp-sem-hash).

Reconciliation supersedes the epistemic domain object with [MEM-OBJ-discovered-domain](memory.md#mem-obj-discovered-domain); all classifications use that canonical identity. Its other object groupings remain valid containers alongside the narrower memory parts. The unresolved info-route attribution does not license extending [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval): this profile uses [MEM-RTE-project-info](memory.md#mem-rte-project-info) for info and does not depend on the disputed structural-results attribution.

The accepted records do not establish a qualifying automatic trace-fed write or a complete bounded absence across all imported content. Trace axes therefore retain uncertainty rather than converting lack of an established route into a system-wide no. Likewise, anonymous direct writers do not become human merely because YAML is editable. No classification asserts exercised host uptake, semantic accuracy or causal benefit.

Source-read log: none. This member classifies supplied accepted records only; no frozen-source file or reference profile was read. The supplied previous output was read as the refusal-correction baseline.
