---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "REM memory comparison of retained episodes, derived access state and conditional semantic stores at the frozen revision."
run-id: "AAS-2026-10-14-rem-a81fdc774400-01"
source-identity: "https://github.com/satyammistari/REM"
reviewed-boundary: "935e8be0a1fca5b23dbabfe16c48b562c1cd24cc"
memory-comparison:
  version: 2
  scope: "Retained episode descriptions, parser metadata, envelope/access feedback, reusable embedding cache, episode vectors and temporal topology; semantic SQL facts/provenance/lifecycle fields, Qdrant vectors/payload and graph storage capabilities, their proposed automatic admission and known later read routes. Includes generic caller provenance and initial semantic population as unresolved alternatives. Excludes unchanged provider weights, static shipped prompts/code, auth/config/queue plumbing, current request-local candidate objects as retained memory, benchmark reporting files and the enclosing host context window. Candidate computations remain relevant only to proposed retained writes and bounded nonretention findings."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Episode raw text, parsed interpretation, envelope and access feedback in PostgreSQL"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-retrieval-count"
                - "runtime.md#rt-rte-episode-write"
              note: "The write service stores the row; later SQL reload and ranking consume its parts."
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-retrieval-count"
            - "runtime.md#rt-rte-episode-write"
            - "memory.md#mem-rte-memory-listing"
          note: "The named episode parts share one SQL substrate; store success remains conditional and unobserved."
        - scope: "Episode search vectors and cached episode/query embeddings"
          assessment: "known"
          findings:
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "runtime.md#rt-rte-episode-write"
              note: "Episode vectors are upserted to Qdrant and searched later."
            - value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Redis retains embedding results for reuse with a 24-hour TTL."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Dense encoding is not the substrate. These two retained copies have distinct consumers."
        - scope: "Episode temporal identity/topology in Neo4j"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-graph"
                - "runtime.md#rt-rte-episode-write"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Episode nodes and predecessor edges support later one-hop expansion."
          records:
            - "memory.md#mem-obj-memory-graph"
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-context-retrieve"
          note: "The retained part is topology, not SQL raw content."
        - scope: "Semantic SQL representation and Qdrant payload/vector representation"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-semantic-control"
                - "runtime.md#rt-abs-writeback-routes"
              note: "SQL insertion and listing capabilities exist without the worker admission endpoint."
            - value: "vector"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-semantic-control"
                - "epistemic.md#epi-obj-semantic-result"
              note: "Qdrant can retain semantic vectors and payload facts for the inspected retrieval consumer."
          records:
            - "memory.md#mem-obj-semantic-control"
            - "memory.md#mem-obj-memory-vector"
            - "epistemic.md#epi-obj-semantic-result"
            - "runtime.md#rt-abs-writeback-routes"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Substrate coverage is resolved despite unknown initial population; this does not assert synchronized SQL/vector state."
        - scope: "Semantic compression nodes and edges"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-memory-graph"
              note: "Neo4j helper methods expose semantic-node and compression-link storage without an active semantic admission caller."
          records:
            - "memory.md#mem-obj-memory-graph"
            - "runtime.md#rt-abs-writeback-routes"
          note: "This is a library affordance rather than populated semantic provenance."
      records:
        - "memory.md#mem-obj-raw-content"
        - "memory.md#mem-obj-episode-interpretation"
        - "memory.md#mem-obj-retrieval-count"
        - "runtime.md#rt-rte-episode-write"
        - "memory.md#mem-rte-memory-listing"
        - "memory.md#mem-obj-memory-vector"
        - "runtime.md#rt-rte-context-retrieve"
        - "memory.md#mem-obj-memory-graph"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
        - "runtime.md#rt-abs-writeback-routes"
      note: "The record inventory covers retained SQL, vector/cache and graph parts, including intended semantic representations. Provider weights, fixed source prompts, queues, request-local candidates and benchmark report files are outside the memory scope; unknown contents do not make the named substrates unknown."
    representational_form:
      assessment: "known"
      units:
        - scope: "Episode raw descriptions and interpreted intent displayed as context"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-episode-interpretation"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Text is retained and interpreted or displayed as episode context; downstream host use is not observed."
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "runtime.md#rt-rte-context-retrieve"
          note: "This unit concerns text consumption, not the complete mixed SQL row."
        - scope: "Episode IDs, timestamps, outcome/parse fields, access counts, vector payload IDs and graph topology"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-episode"
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-retrieval-count"
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-memory-graph"
              note: "Localized fields are consumed by fixed admission, grouping, filtering, ranking and temporal expansion rules."
          records:
            - "runtime.md#rt-obj-episode"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-retrieval-count"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Parsed entity names and labels can be linguistic, but their field-level selector use is symbolic. Unconsumed fields carry no implied authority."
        - scope: "Episode vectors and reusable embedding cache entries"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
              note: "Dense numerical representations spread similarity information across coordinates rather than stating readable facts."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Parametric describes dense encoding, not trained local weights."
        - scope: "Semantic fact payload and SQL fact text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-semantic-control"
                - "epistemic.md#epi-obj-semantic-result"
              note: "Stored fact text can be listed or returned as learned-fact context when the stores are populated."
          records:
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
            - "runtime.md#rt-rte-context-retrieve"
          note: "The fact representation is inspectable even though originating instances and admission are unknown."
        - scope: "Semantic vectors, provenance/lifecycle fields and compression topology"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-memory-vector"
              note: "Semantic vector capability retains dense selection state."
            - value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-semantic-control"
                - "memory.md#mem-obj-semantic-lineage"
                - "memory.md#mem-obj-memory-graph"
              note: "SQL source IDs, lifecycle flags and graph links have localized schema/helper handling, distinct from fact text."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-semantic-control"
            - "memory.md#mem-obj-semantic-lineage"
            - "memory.md#mem-obj-memory-graph"
            - "runtime.md#rt-abs-writeback-routes"
          note: "The intended numerical and symbolic parts are resolved as forms, not credited as actively maintained provenance."
      records:
        - "memory.md#mem-obj-raw-content"
        - "memory.md#mem-obj-episode-interpretation"
        - "runtime.md#rt-rte-context-retrieve"
        - "runtime.md#rt-obj-episode"
        - "memory.md#mem-obj-retrieval-count"
        - "memory.md#mem-obj-memory-vector"
        - "memory.md#mem-obj-memory-graph"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
        - "memory.md#mem-obj-semantic-lineage"
        - "runtime.md#rt-abs-writeback-routes"
      note: "The declared inventory splits text, localized fields/topology and dense vectors. No retained opaque provider payload is identified beyond excluded provider model weights; the records establish these encodings without establishing deployed content."
    lineage:
      assessment: "partial"
      units:
        - scope: "Episode content supplied through host save hooks and source-authored seed/benchmark examples"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "runtime.md#rt-rte-host-integration"
              note: "Adapters import serialized human/user and assistant exchanges into REM."
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-rte-benchmark-evaluation"
              note: "Seed and benchmark drivers supply source-authored synthetic descriptions, not authenticated agent experience."
          records:
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-host-integration"
            - "memory.md#mem-rte-benchmark-evaluation"
          note: "These evidenced producer paths are distinct; software admission does not make their original authorship automatic or human-approved."
        - scope: "Generic caller episode content before admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-episode-write"
          note: "Caller identity does not establish original authorship, imported provenance or relation to actual activity."
        - scope: "Parser-derived episode metadata and defaults"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-raw-content"
                - "runtime.md#rt-rte-host-integration"
              note: "On the serialized session branch the parser extracts interpretation from interaction descriptions."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode-interpretation"
                - "runtime.md#rt-rte-episode-write"
              note: "Software defaults and structured field handling supply metadata independently of successful model extraction."
          records:
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-host-integration"
            - "runtime.md#rt-rte-episode-write"
          note: "Known derivation mechanisms do not certify semantic fidelity or authenticate generic input origin."
        - scope: "Episode vectors, cached embeddings, temporal topology and access counters"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-memory-graph"
                - "memory.md#mem-obj-retrieval-count"
                - "runtime.md#rt-rte-episode-write"
                - "epistemic.md#epi-rte-retrieval-feedback"
              note: "Embedding inference and software ID/topology/count operations derive access structures; none is an authored explanatory fact."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
            - "memory.md#mem-obj-retrieval-count"
            - "runtime.md#rt-rte-episode-write"
            - "epistemic.md#epi-rte-retrieval-feedback"
          note: "REM-side derivation is known. Provider training provenance is excluded, not inferred from returned embeddings."
        - scope: "Intended trace-derived semantic facts and code-attached provenance"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "runtime.md#rt-clm-memory-loop"
                - "memory.md#mem-obj-semantic-candidate"
                - "runtime.md#rt-rte-worker-consolidation"
              note: "The declared durable semantic loop extracts recurring facts from episodes, but admission is disconnected."
            - value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-semantic-lineage"
                - "runtime.md#rt-rte-worker-consolidation"
              note: "Code attaches full-cluster source IDs/counts before the attempted store write."
          records:
            - "runtime.md#rt-clm-memory-loop"
            - "memory.md#mem-obj-semantic-candidate"
            - "memory.md#mem-obj-semantic-lineage"
            - "runtime.md#rt-rte-worker-consolidation"
            - "runtime.md#rt-abs-writeback-routes"
          note: "The candidate derivation is inspectable; identity with a retained semantic instance and actual extraction versus novel generalization remain unresolved."
        - scope: "Initial or administratively populated semantic SQL, Qdrant and graph contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
          note: "No stored instance, initialization provenance or administrative content control is supplied; these cannot be classified as engine-derived merely from their field names."
      records:
        - "memory.md#mem-obj-raw-content"
        - "runtime.md#rt-rte-host-integration"
        - "memory.md#mem-rte-benchmark-evaluation"
        - "runtime.md#rt-rte-episode-write"
        - "memory.md#mem-obj-episode-interpretation"
        - "memory.md#mem-obj-memory-vector"
        - "memory.md#mem-obj-memory-graph"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-rte-retrieval-feedback"
        - "runtime.md#rt-clm-memory-loop"
        - "memory.md#mem-obj-semantic-candidate"
        - "memory.md#mem-obj-semantic-lineage"
        - "runtime.md#rt-rte-worker-consolidation"
        - "runtime.md#rt-abs-writeback-routes"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
      note: "Known episode producers and subsequent derivations coexist with unknown generic content provenance and initial semantic population. Request-local engine/helper candidates are not silently counted as retained facts."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Episode raw content and domain/intent labels at server context construction and conditional later prompt consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-episode-interpretation"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Go formats retained raw content and labels as reference context for a requesting direct HTTP consumer."
            - value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-context-injection"
                - "runtime.md#rt-rte-host-integration"
              note: "A host can supply returned context to an answering model; nonempty ordinary SDK results fail before adapter delivery."
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "runtime.md#rt-rte-context-retrieve"
            - "runtime.md#rt-bap-context-injection"
            - "runtime.md#rt-rte-host-integration"
          note: "Context advice does not become standing instruction or enforced privilege through system-prompt placement."
        - scope: "Retained session descriptions at automatic metadata/vector production"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-memory-vector"
                - "runtime.md#rt-rte-host-integration"
                - "runtime.md#rt-rte-episode-write"
              note: "Retained interaction experience supplies durable interpretation and selection artifacts used in later processing."
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "runtime.md#rt-rte-host-integration"
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-context-retrieve"
          note: "This is the update-consumer force, separate from raw text knowledge at the prompt consumer; improved capacity is not established."
        - scope: "Episode vectors, timestamps and retrieval counts at retrieval ranking; temporal IDs at context expansion"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-retrieval-count"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Retained vectors, recency and access counts affect candidate ordering and relative priority."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-graph"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Retained temporal topology selects neighbor episode IDs to reload as additional inputs."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-retrieval-count"
            - "memory.md#mem-obj-memory-graph"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Fixed ranking code still gives its retained inputs ranking authority; graph input selection is not causal inference."
        - scope: "Retained domain/intent at maintenance grouping and raw episodes at intended durable semantic update"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-episode-interpretation"
                - "runtime.md#rt-rte-worker-consolidation"
              note: "Domain and intent select extraction input groups when lowercase serialization is compatible."
            - value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw-content"
                - "runtime.md#rt-clm-memory-loop"
                - "runtime.md#rt-rte-worker-consolidation"
              note: "The declared durable abstraction loop would use retained experience to create future context, but shipped persistence does not complete it."
          records:
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-clm-memory-loop"
            - "runtime.md#rt-rte-worker-consolidation"
            - "runtime.md#rt-abs-writeback-routes"
          note: "The selector and proposed update are separate effects. PascalCase fetched episodes defeat intended grouping; direct compatible dictionaries do not repair persistence."
        - scope: "Semantic vector/payload at search ranking and server context consumption"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "epistemic.md#epi-obj-semantic-result"
                - "runtime.md#rt-rte-context-retrieve"
              note: "If populated, retained semantic vectors determine similarity ordering on the implemented search route."
            - value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-semantic-result"
                - "runtime.md#rt-rte-context-retrieve"
              note: "If populated, payload fact/confidence text supplies server-returned reference context without a SQL lifecycle recheck."
            - value: "knowledge"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-semantic-result"
                - "runtime.md#rt-bap-context-injection"
              note: "Direct HTTP context can be supplied to a later host prompt; actual host use is unobserved."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "epistemic.md#epi-obj-semantic-result"
            - "runtime.md#rt-rte-context-retrieve"
            - "runtime.md#rt-bap-context-injection"
            - "memory.md#mem-obj-semantic-control"
          note: "Consumer effects are inspectable despite unknown stored content. Confidence and learned-fact labels establish no independent validation authority."
        - scope: "Initial semantic content at unidentified prior admission/update consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
            - "memory.md#mem-obj-memory-graph"
          note: "Unknown administrative provenance and control prevent classifying any prior learning, instruction, validation or enforcement effect. SQL withdrawal flags and unused graph/provenance fields do not establish one."
      records:
        - "memory.md#mem-obj-raw-content"
        - "memory.md#mem-obj-episode-interpretation"
        - "runtime.md#rt-rte-context-retrieve"
        - "runtime.md#rt-bap-context-injection"
        - "runtime.md#rt-rte-host-integration"
        - "memory.md#mem-obj-memory-vector"
        - "runtime.md#rt-rte-episode-write"
        - "memory.md#mem-obj-retrieval-count"
        - "memory.md#mem-obj-memory-graph"
        - "runtime.md#rt-clm-memory-loop"
        - "runtime.md#rt-rte-worker-consolidation"
        - "runtime.md#rt-abs-writeback-routes"
        - "epistemic.md#epi-obj-semantic-result"
        - "memory.md#mem-obj-semantic-control"
      note: "The recorded consumers establish knowledge, learning, ranking and routing on distinct paths. No blanket instruction, enforcement or validation finding is inferred from fixed code, authentication, confidence or unconsumed flags; unknown initial semantic update consumers keep this axis partial."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Structural episode admission, host exchange serialization and synthetic driver submission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-write"
                - "runtime.md#rt-rte-host-integration"
                - "memory.md#mem-rte-benchmark-evaluation"
              note: "Software submits, filters and admits episodes without a per-content human veto; starting the host/driver is not manual admission."
          records:
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-host-integration"
            - "memory.md#mem-rte-benchmark-evaluation"
          note: "This classifies admission, not the original author of the supplied text."
        - scope: "Generic caller supplying or replacing initial episode content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-episode-write"
          note: "The caller may be a person or software; there is no recorded explicit human content decision supporting manual agency."
        - scope: "Parse-field admission, embedding cache/vector writes, graph derivation and access-counter updates"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-memory-graph"
                - "memory.md#mem-obj-retrieval-count"
                - "runtime.md#rt-rte-episode-write"
                - "epistemic.md#epi-rte-retrieval-feedback"
              note: "Models propose interpretation and software admits fields, derives stores and updates counts without human approval."
          records:
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
            - "memory.md#mem-obj-retrieval-count"
            - "runtime.md#rt-rte-episode-write"
            - "epistemic.md#epi-rte-retrieval-feedback"
          note: "Wired conditional software mechanisms remain automatic even when dependency failure prevents a particular write."
        - scope: "Worker-proposed semantic admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-worker-consolidation"
                - "memory.md#mem-obj-semantic-candidate"
                - "runtime.md#rt-abs-writeback-routes"
              note: "Software/model filtering and HTTP attempts contain no per-content operator gate, but registered durable admission is missing."
          records:
            - "runtime.md#rt-rte-worker-consolidation"
            - "memory.md#mem-obj-semantic-candidate"
            - "runtime.md#rt-abs-writeback-routes"
          note: "Agency of the proposed mechanism is known; this is not a successful semantic write."
        - scope: "Initial or administrative semantic SQL, Qdrant and graph population"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
          note: "No admission principal or human approval/replacement decision is supplied for externally present contents."
      records:
        - "runtime.md#rt-rte-episode-write"
        - "runtime.md#rt-rte-host-integration"
        - "memory.md#mem-rte-benchmark-evaluation"
        - "memory.md#mem-obj-raw-content"
        - "memory.md#mem-obj-episode-interpretation"
        - "memory.md#mem-obj-memory-vector"
        - "memory.md#mem-obj-memory-graph"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-rte-retrieval-feedback"
        - "runtime.md#rt-rte-worker-consolidation"
        - "memory.md#mem-obj-semantic-candidate"
        - "runtime.md#rt-abs-writeback-routes"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
      note: "Automatic mechanisms are supported without converting human authorship or workflow launch into manual admission. Generic supply and initial semantic population remain unresolved; no manual positive is established."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Retrieval recency weighting of retained episodes"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-retrieve"
              note: "Increasing age lowers the recency component of episode ranking without deleting the row."
          records:
            - "runtime.md#rt-rte-context-retrieve"
            - "memory.md#mem-obj-retrieval-count"
          note: "Decay is downweighting at the later selector, not expiry of raw text."
        - scope: "Access-frequency salience update"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-count"
                - "epistemic.md#epi-rte-retrieval-feedback"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Automatic retrieval-count increments raise the capped bonus available to later ranking."
          records:
            - "memory.md#mem-obj-retrieval-count"
            - "epistemic.md#epi-rte-retrieval-feedback"
            - "runtime.md#rt-rte-context-retrieve"
          note: "The operation raises salience, not storage tier or measured quality."
        - scope: "Semantic consolidation requested over retained episode samples"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-clm-memory-loop"
                - "memory.md#mem-obj-semantic-candidate"
                - "runtime.md#rt-rte-worker-consolidation"
              note: "The declared loop and extraction prompt request a reduced reusable representation of episode claims."
          records:
            - "runtime.md#rt-clm-memory-loop"
            - "memory.md#mem-obj-semantic-candidate"
            - "runtime.md#rt-rte-worker-consolidation"
            - "runtime.md#rt-abs-writeback-routes"
            - "epistemic.md#epi-rte-pattern-extraction"
          note: "Implemented generation requests do not establish actual claim-preserving consolidation or synthesis in unknown outputs; durable admission is missing. This positive retains only the design warrant."
        - scope: "Declared self-evolving semantic memory and first-class forgetting"
          assessment: "partial"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "epistemic.md#epi-clm-recursive-memory"
              note: "The README claims self-evolving memories, but the engine does not revise semantic predecessors."
            - value: "decay"
              basis: "claimed"
              records:
                - "epistemic.md#epi-clm-recursive-memory"
              note: "First-class forgetting is declared while fine-grained policies remain a roadmap item."
          records:
            - "epistemic.md#epi-clm-recursive-memory"
            - "memory.md#mem-abs-memory-withdrawal"
            - "epistemic.md#epi-abs-semantic-withdrawal"
          note: "These are claims, not wired replacement, forgetting or consumer-effective invalidation. Missing loops remain beside their claimed values."
        - scope: "Initial semantic content and any prior maintenance; alternative callable candidate generation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
            - "epistemic.md#epi-rte-compressor-helper"
            - "memory.md#mem-cmp-compressor"
          note: "Unknown semantic history and absent durable helper consumers prevent classifying prior curation. Helper clipping and numeric sanitation alone establish none of dedup, evolve, invalidate or synthesize."
      records:
        - "runtime.md#rt-rte-context-retrieve"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-rte-retrieval-feedback"
        - "runtime.md#rt-clm-memory-loop"
        - "memory.md#mem-obj-semantic-candidate"
        - "runtime.md#rt-rte-worker-consolidation"
        - "runtime.md#rt-abs-writeback-routes"
        - "epistemic.md#epi-rte-pattern-extraction"
        - "epistemic.md#epi-clm-recursive-memory"
        - "memory.md#mem-abs-memory-withdrawal"
        - "epistemic.md#epi-abs-semantic-withdrawal"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
        - "epistemic.md#epi-rte-compressor-helper"
        - "memory.md#mem-cmp-compressor"
      note: "Known recency decay and count promotion coexist with claimed semantic consolidation/evolution/forgetting and unresolved content transformations. Index rebuilds, extraction labels, schema flags and reset attempts do not establish further implemented curation."
    read_back_direction:
      assessment: "known"
      units:
        - scope: "Query retrieval of episode context, semantic payload and their selection structures"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-retrieve"
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-memory-graph"
                - "memory.md#mem-obj-retrieval-count"
                - "epistemic.md#epi-obj-semantic-result"
              note: "A host/direct HTTP request initiates selection and return of retained material; vector/graph/ranking operations fulfill that request."
          records:
            - "runtime.md#rt-rte-context-retrieve"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-memory-graph"
            - "memory.md#mem-obj-retrieval-count"
            - "epistemic.md#epi-obj-semantic-result"
            - "runtime.md#rt-rte-host-integration"
          note: "Automatic selection inside requested retrieval is not a separate push. SDK failures limit one delivery path, not the direct HTTP pull."
        - scope: "SQL list/get requests by direct clients, maintenance and benchmark clients"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-listing"
                - "runtime.md#rt-rte-worker-consolidation"
                - "memory.md#mem-rte-benchmark-evaluation"
              note: "Callers request retained rows by identity or chronology; the worker explicitly fetches its input page."
          records:
            - "memory.md#mem-rte-memory-listing"
            - "runtime.md#rt-rte-worker-consolidation"
            - "memory.md#mem-rte-benchmark-evaluation"
            - "memory.md#mem-obj-semantic-control"
          note: "Scheduled maintenance requests episodes rather than supplying unsolicited retained context. Nonempty SDK typed reload fails."
        - scope: "Embedding cache reuse and access-feedback reload within a subsequent requested operation"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vector"
                - "memory.md#mem-obj-retrieval-count"
                - "runtime.md#rt-rte-episode-write"
                - "runtime.md#rt-rte-context-retrieve"
              note: "A subsequent embed/write/retrieve operation requests a cache value or rehydrated counter; this is internal requested reuse."
          records:
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-retrieval-count"
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-context-retrieve"
          note: "The inventory includes access state as well as displayed content; no additional unsolicited delivery is recorded."
      records:
        - "runtime.md#rt-rte-context-retrieve"
        - "memory.md#mem-obj-memory-vector"
        - "memory.md#mem-obj-memory-graph"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-obj-semantic-result"
        - "runtime.md#rt-rte-host-integration"
        - "memory.md#mem-rte-memory-listing"
        - "runtime.md#rt-rte-worker-consolidation"
        - "memory.md#mem-rte-benchmark-evaluation"
        - "memory.md#mem-obj-semantic-control"
        - "runtime.md#rt-rte-episode-write"
      note: "The memory report inventories query retrieval, chronological/identity reload, host hooks, maintenance fetches and cache/feedback reuse. All inspected retained-material deliveries fulfill requests. Disconnected semantic writes and unknown initial provenance do not make the implemented read direction unknown; request-local candidates and result reports are excluded."
    read_back_signal:
      assessment: "inapplicable"
      units:
        - scope: "All included query, list/get, maintenance-fetch and internal cache/feedback read-back operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-retrieve"
            - "memory.md#mem-rte-memory-listing"
            - "runtime.md#rt-rte-host-integration"
            - "runtime.md#rt-rte-worker-consolidation"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-retrieval-count"
          note: "The completely assessed direction inventory is pull-only. Query embeddings, agent IDs and chronological limits are selectors within requested returns, not signals for a push."
      records:
        - "runtime.md#rt-rte-context-retrieve"
        - "memory.md#mem-rte-memory-listing"
        - "runtime.md#rt-rte-host-integration"
        - "runtime.md#rt-rte-worker-consolidation"
        - "memory.md#mem-obj-memory-vector"
        - "memory.md#mem-obj-retrieval-count"
      note: "No included read-back unit has an unsolicited retained-material delivery operation. Signals classify push only; identifier filtering and embedding ranking on pull do not supply identifier or inferred-embedding positives."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Recorded host exchanges automatically transformed into retained parse metadata and vectors with later selector/display consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-memory-vector"
                - "runtime.md#rt-rte-episode-write"
                - "runtime.md#rt-rte-host-integration"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Serialized session turns feed automatic derivation and durable admission of metadata/vectors reused by later ranking, grouping or context construction."
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "runtime.md#rt-rte-episode-write"
            - "runtime.md#rt-rte-host-integration"
            - "runtime.md#rt-rte-context-retrieve"
          note: "This chain has inspected conditional persistence and later consumers; no observed activation, truthful extraction or improvement is implied. Host SDK prompt delivery need not succeed for internal ranking reuse."
        - scope: "Retrieval activity automatically updating durable access counts for later ranking"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-count"
                - "epistemic.md#epi-rte-retrieval-feedback"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Retrieval selection events feed software count updates whose retained result changes future ranking."
          records:
            - "memory.md#mem-obj-retrieval-count"
            - "epistemic.md#epi-rte-retrieval-feedback"
            - "runtime.md#rt-rte-context-retrieve"
          note: "Durable behavior-shaping feedback qualifies without model training or an independent outcome oracle."
        - scope: "Shipped engine/helper candidate outputs and task HTTP semantic admission at the registered Go endpoints"
          assessment: "known"
          findings:
            - value: "no"
              basis: "wired"
              records:
                - "runtime.md#rt-abs-writeback-routes"
                - "runtime.md#rt-rte-worker-consolidation"
                - "runtime.md#rt-rte-direct-consolidation"
                - "epistemic.md#epi-rte-compressor-helper"
              note: "The bounded router inspection establishes no semantic admission endpoint for the task; direct and helper computations retain no output themselves. This shipped branch lacks the durable write required for trace learning."
          records:
            - "runtime.md#rt-abs-writeback-routes"
            - "runtime.md#rt-rte-worker-consolidation"
            - "runtime.md#rt-rte-direct-consolidation"
            - "epistemic.md#epi-rte-compressor-helper"
            - "memory.md#mem-obj-semantic-candidate"
          note: "The negative is resolved only for these shipped candidate-to-retention paths. It does not cover administrative loading, an added external writer, the declared future loop, or the separate metadata/vector and feedback positives."
        - scope: "Proposed automatic durable semantic extraction from episode traces"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-clm-memory-loop"
                - "runtime.md#rt-rte-worker-consolidation"
                - "memory.md#mem-obj-raw-content"
                - "memory.md#mem-obj-semantic-candidate"
              note: "The source claims the trace-fed durable semantic loop; the inspected task only attempts its missing admission."
          records:
            - "runtime.md#rt-clm-memory-loop"
            - "runtime.md#rt-rte-worker-consolidation"
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-semantic-candidate"
            - "runtime.md#rt-abs-writeback-routes"
            - "runtime.md#rt-abs-worker-bridge"
          note: "Claimed trace learning is not a wired complete write-and-later-consumer chain. Correctly shaped direct inputs enable candidates, not retention."
        - scope: "Generic episode derivation inputs and externally initialized semantic contents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
          note: "Generic descriptions may be traces or authored static examples; initial semantic population has no producer/input history. Neither a universal yes nor a system-wide no follows."
      records:
        - "memory.md#mem-obj-raw-content"
        - "memory.md#mem-obj-episode-interpretation"
        - "memory.md#mem-obj-memory-vector"
        - "runtime.md#rt-rte-episode-write"
        - "runtime.md#rt-rte-host-integration"
        - "runtime.md#rt-rte-context-retrieve"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-rte-retrieval-feedback"
        - "runtime.md#rt-rte-direct-consolidation"
        - "epistemic.md#epi-rte-compressor-helper"
        - "memory.md#mem-obj-semantic-candidate"
        - "runtime.md#rt-clm-memory-loop"
        - "runtime.md#rt-rte-worker-consolidation"
        - "runtime.md#rt-abs-writeback-routes"
        - "runtime.md#rt-abs-worker-bridge"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
      note: "Wired session-derived metadata/vector learning and event-fed ranking feedback coexist with bounded local no and a claimed semantic loop. Unknown trace origin and initial semantic writes keep coverage partial; local no is retained even though the derived system union has yes. Raw logging without a derived write is outside the qualifying update inventory."

    trace_source:
      assessment: "partial"
      units:
        - scope: "Host conversation branch of automatic metadata/vector derivation"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-content"
                - "runtime.md#rt-rte-host-integration"
                - "memory.md#mem-obj-episode-interpretation"
                - "memory.md#mem-obj-memory-vector"
                - "runtime.md#rt-rte-episode-write"
              note: "LangChain/AutoGen save human/user and assistant turn strings; those recorded conversational turns are the original derivation input."
          records:
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-host-integration"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "runtime.md#rt-rte-episode-write"
          note: "These adapters do not supply full tool history or linked state/action/outcome trajectories. The wrappers are not additional event-stream sources."
        - scope: "Automatic access-count update"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-count"
                - "epistemic.md#epi-rte-retrieval-feedback"
                - "runtime.md#rt-rte-context-retrieve"
              note: "Discrete retrieval selection activity is the original input to the durable count update, not a conversational log."
          records:
            - "memory.md#mem-obj-retrieval-count"
            - "epistemic.md#epi-rte-retrieval-feedback"
            - "runtime.md#rt-rte-context-retrieve"
          note: "This is runtime access feedback, not verified task outcomes or tool execution traces."
        - scope: "Claimed durable semantic extraction on recorded host exchanges"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "claimed"
              records:
                - "runtime.md#rt-clm-memory-loop"
                - "runtime.md#rt-rte-worker-consolidation"
                - "memory.md#mem-obj-raw-content"
                - "runtime.md#rt-rte-host-integration"
              note: "The intended durable semantic route can use stored conversational exchanges."
          records:
            - "runtime.md#rt-clm-memory-loop"
            - "runtime.md#rt-rte-worker-consolidation"
            - "memory.md#mem-obj-raw-content"
            - "runtime.md#rt-rte-host-integration"
            - "runtime.md#rt-abs-writeback-routes"
          note: "The original session branch is identified, but semantic persistence is disconnected and generic episode origins remain unresolved."
        - scope: "Generic description inputs and initially populated semantic memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-content"
            - "memory.md#mem-obj-episode-interpretation"
            - "memory.md#mem-obj-memory-vector"
            - "memory.md#mem-obj-semantic-control"
            - "epistemic.md#epi-obj-semantic-result"
          note: "Original content may be activity records, synthetic examples or static knowledge. Unknown history prevents tool-traces, trajectories or another source classification for this branch."
        - scope: "Shipped engine/helper candidate outputs and task HTTP semantic admission at the registered Go endpoints"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-abs-writeback-routes"
            - "runtime.md#rt-rte-worker-consolidation"
            - "runtime.md#rt-rte-direct-consolidation"
            - "epistemic.md#epi-rte-compressor-helper"
          note: "The corresponding trace-learning unit has bounded absence of a qualifying durable semantic write on these shipped paths. Its original inputs do not establish a trace source for completed learning."
      records:
        - "memory.md#mem-obj-raw-content"
        - "runtime.md#rt-rte-host-integration"
        - "memory.md#mem-obj-episode-interpretation"
        - "memory.md#mem-obj-memory-vector"
        - "runtime.md#rt-rte-episode-write"
        - "memory.md#mem-obj-retrieval-count"
        - "epistemic.md#epi-rte-retrieval-feedback"
        - "runtime.md#rt-rte-context-retrieve"
        - "runtime.md#rt-clm-memory-loop"
        - "runtime.md#rt-rte-worker-consolidation"
        - "runtime.md#rt-abs-writeback-routes"
        - "memory.md#mem-obj-semantic-control"
        - "epistemic.md#epi-obj-semantic-result"
        - "runtime.md#rt-rte-direct-consolidation"
        - "epistemic.md#epi-rte-compressor-helper"
      note: "Each qualifying wired route retains its original source: conversation turns or discrete retrieval activity. Generic input and semantic history remain unknown. Synthetic examples and static prompts are not traces merely because they are encoded as episodes."
---

# REM memory profile

## Comparison rationale

The profile separates an operative retained part from the mechanism that proposes it. Episode text, metadata, vectors, temporal topology and access counts have conditional wired persistence and later consumers. Semantic schema and storage helpers are capabilities; a generated candidate is not a retained semantic instance. Unknown semantic population therefore limits lineage and admission control without obscuring the known storage encodings and conditional read consumers. See [MEM-OBJ-semantic-control](memory.md#mem-obj-semantic-control), [MEM-OBJ-memory-vector](memory.md#mem-obj-memory-vector), [MEM-OBJ-memory-graph](memory.md#mem-obj-memory-graph), [EPI-OBJ-semantic-result](epistemic.md#epi-obj-semantic-result) and [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes).

The reconciliation supersedes the epistemic raw-content and parse-fields records with [MEM-OBJ-raw-content](memory.md#mem-obj-raw-content) and [MEM-OBJ-episode-interpretation](memory.md#mem-obj-episode-interpretation). Their source-truth and semantic-fidelity limits survive; these identity supersessions do not strengthen any finding. The candidate container, candidate text, attached lineage, SQL representation and retrieved payload remain distinct. No retained payload is classified as engine-produced solely because the names match. See [MEM-OBJ-semantic-candidate](memory.md#mem-obj-semantic-candidate), [MEM-OBJ-semantic-lineage](memory.md#mem-obj-semantic-lineage) and [EPI-OBJ-semantic-result](epistemic.md#epi-obj-semantic-result).

A host requests read-back. Automatic ranking within that request is not a second push operation. Listing, worker fetches and cache reuse also fulfill requests. Thus read-back signal is inapplicable across the named direction inventory, not unknown merely because no SDK handoff succeeds. Go constructs context for a direct HTTP consumer, but ordinary nonempty SDK results fail required timestamp conversion before either adapter delivers context. Knowledge authority at server construction and conditional host consumption remains distinct from successful host activation. See [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [MEM-RTE-memory-listing](memory.md#mem-rte-memory-listing), [RT-RTE-host-integration](runtime.md#rt-rte-host-integration) and [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).

Trace learning here means an automatic activity-fed write with a durable behavior-shaping result and later consumer, not demonstrated improvement. Session-derived metadata and vectors have later selection consumers; retrieval events produce durable counters used by the reranker. These are different original sources and different update mechanisms. Retaining raw messages alone is not that transformation. Direct consolidation and the alternative compressor return candidates without retaining them. The claimed semantic loop stays claimed because its automatic durable admission is disconnected. Local negative units do not erase supported positive routes or justify a system-wide negative. See [MEM-OBJ-episode-interpretation](memory.md#mem-obj-episode-interpretation), [MEM-OBJ-memory-vector](memory.md#mem-obj-memory-vector), [EPI-RTE-retrieval-feedback](epistemic.md#epi-rte-retrieval-feedback), [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation), [EPI-RTE-compressor-helper](epistemic.md#epi-rte-compressor-helper) and [RT-CLM-memory-loop](runtime.md#rt-clm-memory-loop).

Recency weighting is decay because it downweights retained episodes. Count feedback is promotion because it raises their later salience. Requested semantic abstraction receives only a claimed consolidation finding: model outputs and their preservation of claims are not supplied, and the task does not complete persistence. The broader self-evolving and forgetting claims retain their own design-level findings, not the wired witness from count feedback. No synthesize finding follows from epistemically indeterminate model output, and no invalidate finding follows from unused lifecycle flags or attempted reset. See [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [MEM-OBJ-retrieval-count](memory.md#mem-obj-retrieval-count), [EPI-RTE-pattern-extraction](epistemic.md#epi-rte-pattern-extraction), [EPI-CLM-recursive-memory](epistemic.md#epi-clm-recursive-memory) and [MEM-ABS-memory-withdrawal](memory.md#mem-abs-memory-withdrawal).

Unknown generic caller origin prevents a complete lineage or trace-source inventory. Unknown initial semantic admission prevents manual/automatic and prior authority conclusions for that branch. No operator decision is inferred from workflow launch or source authorship. Static provider weights and shipped extraction guidance are excluded from accumulated memory, while returned dense embeddings remain included. No observed or causal basis is assigned: no execution evidence is supplied. See [MEM-OBJ-raw-content](memory.md#mem-obj-raw-content), [MEM-OBJ-semantic-control](memory.md#mem-obj-semantic-control), [RT-RTE-episode-write](runtime.md#rt-rte-episode-write) and [RT-CMP-embed-service](runtime.md#rt-cmp-embed-service).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required a direct source read, and no incumbent or reference profile was consulted.
