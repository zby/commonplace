---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "xMemory comparison profile of retained conversation memory, hierarchy maintenance and later retrieval at the frozen source boundary."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
source-identity: "https://github.com/hu-xiaobai/xMemory"
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
memory-comparison:
  version: 2
  scope: "Retained originals, episode title/content, semantic statements, provenance/access fields, embeddings, theme summaries/topology, semantic-kNN, diagnostic graph exports and original-message indexes; their admission, maintenance, update-consumer and shipped QA read-back routes. Includes unresolved generic input admission and injected storage/generator alternatives. Excludes static shipped prompts, inference model weights not updated by these routes, current-query NLL/prefix-KV state, and offline QA/metric artifacts with no memory-update consumer. Hidden provider retention remains uninspected, not presumed absent."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Filesystem episode/original/semantic objects, metadata and theme/kNN/vector companion artifacts"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-retrieval-vectors]
              note: "JSONL, JSON and NumPy persistence holds retained content and access structures; serialization does not change substrate."
          records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-memory-metadata, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-retrieval-vectors]
          note: "Covers the recorded local-file objects, not arbitrary injected repositories."
        - scope: "RAM repository alternatives, loaded memory dictionaries/caches and original-message lexical indexes"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-semantic-content, memory.md#mem-obj-original-index, memory.md#mem-obj-retrieval-vectors]
              note: "Process-owned objects retain content for later invocations within their owning process; this is not disk durability."
          records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-original-index, memory.md#mem-obj-retrieval-vectors]
          note: "Current-query scoring state is excluded; loaded accumulated memory and callable lexical indexes are included."
        - scope: "Chroma episode/semantic retrieval index"
          assessment: known
          findings:
            - value: vector
              basis: wired
              records: [memory.md#mem-obj-retrieval-vectors, runtime.md#rt-rte-baseline-search]
              note: "Chroma collections retain retrieval embeddings and associated documents. No underlying SQLite implementation is inferred."
          records: [memory.md#mem-obj-retrieval-vectors, runtime.md#rt-rte-baseline-search]
          note: "Optional theme-Chroma helpers do not establish mandatory theme synchronization."
        - scope: "HierarchicalMemoryGraph diagnostic export and reload"
          assessment: known
          findings:
            - value: graph
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "NetworkX holds typed nodes and edges; this graph is not the adaptive answer reader's substrate."
            - value: files
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "GEXF plus a NumPy companion persist the diagnostic graph and embeddings."
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "The NetworkX graph and embedding matrix also exist in process memory."
          records: [memory.md#mem-obj-memory-graph]
          note: "Graph representation and its physical persistence are both supported."
        - scope: "Injected repository/index implementations and hidden provider-retained state"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "Injection and remote endpoint boundaries do not reveal alternative memory substrates or provider retention."
      records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "The recorded default inventory supports files, RAM, vector and graph storage. Opaque alternatives prevent complete substrate coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Original conversational prose, episode title/content, semantic strings and theme summaries at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, runtime.md#rt-bap-memory-reader]
              note: "Text affects extraction, scoring and answering by model interpretation; themes reach scoring, not final answering."
          records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
          note: "This unit excludes symbolic envelopes and embeddings even when they share the same file."
        - scope: "IDs, timestamps, provenance, theme membership/neighbors, semantic-kNN and lexical index structures"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-original-index]
              note: "Localized fields, token structures and scalar adjacency are consumed by fixed selection/serialization rules."
          records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-original-index]
          note: "Times rendered to a model also provide contextual information; that does not turn the envelope into distributed parameters."
        - scope: "Retained search/theme embeddings and centroids"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-retrieval-vectors]
              note: "Dense representations spread numerical information across dimensions and feed similarity algorithms; these are not trained model-weight updates."
          records: [memory.md#mem-obj-retrieval-vectors]
          note: "Form is known even though immutable producing-model provenance and compatibility are not."
        - scope: "Diagnostic graph operative parts"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "Node IDs, levels and typed edges have fixed graph semantics."
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "Copied node text remains language for diagnostic interpretation, not final QA context."
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "The separate embedding payload is dense numerical representation."
          records: [memory.md#mem-obj-memory-graph]
          note: "The record distinguishes all three parts; a readable graph label does not classify its embedding payload."
        - scope: "Injected retained payloads and hidden provider state"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "Default display text and returned vectors do not reveal opaque alternative payload forms."
      records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-original-index, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-memory-graph, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "All three forms occur in inspected memory; unresolved alternative payloads prevent a complete union."
    lineage:
      assessment: partial
      units:
        - scope: "Admission of original conversation messages into retained episodes"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-original-messages, runtime.md#rt-rte-conversation-admission]
              note: "Caller or bundled dataset messages enter memory after formatting; import does not authenticate human authorship or external truth."
          records: [memory.md#mem-obj-original-messages, runtime.md#rt-rte-conversation-admission]
          note: "Classifies entry into xMemory, not the earlier provenance of captions or search text."
        - scope: "Episode condensation, semantic extraction and theme abstraction from conversation-derived retained material"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
              note: "Conversation traces feed summaries and statements, including themes derived through those statements. Prediction-correction is not evidence of new warranted knowledge."
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary]
          note: "Derivation path is known despite unverified semantic fidelity and current-batch theme refresh."
        - scope: "Code-generated access/provenance fields, embeddings/centroids, topology, kNN, graph export and lexical indexes"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index]
              note: "Code serializes, embeds, combines or indexes existing material into access structures and derived containers. Copied graph prose retains its upstream trace lineage."
          records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index]
          note: "This is the local compilation path, not the provenance of the external embedding model."
        - scope: "Upstream message supplements, immutable embedding provenance and injected initial content"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-cmp-embedding-client, runtime.md#rt-rte-provider-admission, memory.md#mem-obj-retrieval-vectors]
          note: "Recorded generic input and mutable model endpoints leave earlier provenance unresolved; no manual authored-memory path is inferred."
      records: [memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, memory.md#mem-obj-memory-metadata, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-theme-topology, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "Imported traces, trace extraction and local compilation coexist. Known local production does not settle opaque initialization or earlier embedding/input provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Originals, episode prose and semantic statements at final answering; theme prose at adaptive scoring"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-memory-reader, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-original-messages, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
              note: "Retained prose supplies model-interpreted context/evidence, not enforced truth or standing host instructions. Themes only supply scoring context."
          records: [runtime.md#rt-bap-memory-reader, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-theme-summary]
          note: "Delivery is wired; compliance, beneficial influence and factual correctness remain unobserved."
        - scope: "Retained conversations/episodes/statements consumed to produce durable episode, semantic and theme material"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-comparison-extraction]
              note: "Retained experience feeds updates to durable artifacts that shape later prediction, selection and answering. This is update-consumer authority, not demonstrated improved capacity."
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-semantic-admission, memory.md#mem-obj-semantic-content]
              note: "Prior statement contents also supply subject-matter context to prediction before comparison/extraction."
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-comparison-extraction]
          note: "Update authority is separate from downstream knowledge authority; no parameter update is required."
        - scope: "Retained prose, vectors, lexical structures and weighted adjacency at retrieval/representative selection"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-semantic-knn, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content]
              note: "Text/embeddings and adjacency affect relative retrieval priority even though ranking rules are fixed."
          records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-semantic-knn]
          note: "The unspecified final callers of standalone original-message helpers do not establish another final-model path."
        - scope: "Stored owner/source IDs and theme membership at scope and candidate selection"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, runtime.md#rt-rte-adaptive-reader]
              note: "Namespace and source links select stores/episodes; membership selects eligible semantic scope. This does not authenticate the owner."
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-theme-topology, runtime.md#rt-rte-adaptive-reader]
              note: "Membership filters enforce which candidates enter the adaptive context assembly stage, not what the final model believes."
          records: [memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, runtime.md#rt-rte-adaptive-reader]
          note: "Unconsumed confidence and revision counters receive no authority merely because they persist."
        - scope: "Prior same-type semantic content/embeddings at duplicate checking and insertion"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition, memory.md#mem-obj-retrieval-vectors]
              note: "Retained comparators determine conformity to the nonduplication criterion, not truth."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition]
              note: "Similarity above threshold causes the save loop to skip a candidate; caught check errors fail open."
          records: [epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition]
          note: "Validation and enforced insertion veto are distinct effects of the same retained comparison material."
        - scope: "Diagnostic graph interpretation and unspecified helper/injected consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission]
          note: "A diagnostic reader exists, but the records do not establish a further behavior-shaping model/update consumer for every graph part or arbitrary helper caller."
      records: [runtime.md#rt-bap-memory-reader, runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-memory-metadata, memory.md#mem-obj-theme-topology, memory.md#mem-obj-retrieval-vectors, memory.md#mem-obj-semantic-knn, epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission]
      note: "Knowledge, update learning, ranking, routing, validation and context/insertion enforcement have distinct consumers. No retained standing-instruction path is established; opaque alternatives remain unresolved."
    write_agency:
      assessment: partial
      units:
        - scope: "Dataset formatting and automatic episode/original, semantic, vector/index, theme and graph admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-semantic-disposition]
              note: "Models propose text and software admits it and builds access structures without an explicit human decision over each retained item."
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-semantic-disposition]
          note: "An operator starting construction or selecting maintenance timing does not make subsequent content admission manual."
        - scope: "Generic incoming content supply, explicit withdrawal and arbitrary injected implementation admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-conversation-admission, memory.md#mem-rte-memory-withdrawal, runtime.md#rt-rte-provider-admission]
          note: "Generic caller identity leaves human control unresolved. Selecting a startup model is not an explicit human edit or approval of accumulated memory."
      records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-semantic-disposition, memory.md#mem-rte-memory-withdrawal, runtime.md#rt-rte-provider-admission]
      note: "Automatic generation/admission is established locally. No positive manual memory admission is established by caller identity or human workflow initiation."
    curation_operations:
      assessment: partial
      units:
        - scope: "Episode condensation and semantic extraction from retained conversational material"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, epistemic.md#epi-rte-comparison-extraction, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content]
              note: "The implemented routes compress/select conversational claims into summaries or standing statement strings while retaining originals. Fidelity defects would not alone make this synthesis."
            - value: dedup
              basis: wired
              records: [epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition]
              note: "Near-duplicate semantic candidates are removed from admission by same-type cosine comparison with retained statements."
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, epistemic.md#epi-rte-comparison-extraction, epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition]
          note: "Append-oriented extraction does not establish replacement of a contradicted statement or synthesis of a new claim."
        - scope: "Theme summary regeneration, structural split/merge and diagnostic graph node updates"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary]
              note: "Theme summarization reduces selected retained statement text to high-level summaries; current-batch refresh may omit older members."
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-memory-graph]
              note: "Existing summaries/membership are revised and existing graph nodes can update text/embeddings. This does not imply reliable semantic correction."
          records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-memory-graph]
          note: "Structural merge is not automatically semantic deduplication, and index construction alone adds no curation value."
        - scope: "Explicit owner/episode deletion in affected retained stores"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-memory-withdrawal]
              note: "Administrative deletion forgets affected retained content. It is not age-driven automatic decay or history-preserving invalidation."
          records: [memory.md#mem-rte-memory-withdrawal]
          note: "Forgetting is local: hierarchy files, independent reader caches and running writers prevent a global withdrawal guarantee."
        - scope: "Uninspected backend maintenance, numerical corners and injected transformations"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-provider-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-retrieval-vectors]
          note: "The records do not enumerate every alternative transformation or establish every possible controlled operation."
      records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, epistemic.md#epi-rte-comparison-extraction, epistemic.md#epi-rte-duplicate-check, epistemic.md#epi-rte-semantic-disposition, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, memory.md#mem-obj-memory-graph, memory.md#mem-rte-memory-withdrawal, runtime.md#rt-rte-provider-admission]
      note: "Consolidation, duplicate rejection, local revision and forgetting are wired. Prediction-correction and hierarchy names alone establish neither synthesis nor promotion; alternatives prevent a complete operation inventory."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Facade/baseline/lightweight search and shipped adaptive question answering"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader]
              note: "Caller/reader requests retained material with namespace and query; subsequent selection, hydration and requested delivery remain one pull chain."
          records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader]
          note: "Automatic query ranking is not a separate unsolicited push."
        - scope: "Episode-event semantic continuation, selected prior statements into prediction and statements into theme summarization"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
              note: "Automatic update selectors supply accumulated episode/statement material to later generation calls without those model consumers requesting it. This is update-context supply, not unsolicited foreground-agent delivery."
          records: [runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
          note: "A driver may initiate maintenance; automatic selection and model delivery within that update remain separate operations from the upstream operator request."
        - scope: "Diagnostic graph reload and operator-invoked visualization"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-memory-graph]
              note: "A later requested diagnostic load consumes the persisted graph, not the final answer model."
          records: [memory.md#mem-obj-memory-graph]
          note: "No automatic graph-to-answer push is inferred."
        - scope: "Standalone original-message helper callers and injected/hidden-provider read-back"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "Callable search capability alone supplies no additional later consumer; opaque alternatives have no recorded complete delivery chain."
      records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "Requested retrieval is pull; automatic prepared-input supply to update models is push. Unknown helper/injected consumers prevent complete direction coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Prior semantic statement selection for automatic prediction calls"
          assessment: known
          findings:
            - value: inferred-embedding
              basis: wired
              records: [runtime.md#rt-rte-semantic-admission, memory.md#mem-obj-semantic-content]
              note: "New episode title/content triggers a vector query; similarity threshold and count select retained statement text supplied to prediction."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-semantic-admission, memory.md#mem-obj-semantic-content]
              note: "Without vector search, a sampled capped pool is reduced by list position; error fallback takes the final configured count. This is not established chronological recency."
          records: [runtime.md#rt-rte-semantic-admission, memory.md#mem-obj-semantic-content]
          note: "The memory annotation on the runtime route supplies both alternatives and their default count limit."
        - scope: "Episode-created task reload into semantic generation"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-conversation-admission]
              note: "The episode-created event schedules an owner/episode-ID task that reloads retained episode material for extraction; identity selects the delivered episode rather than merely labeling a catalog."
          records: [runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-conversation-admission]
          note: "Cold start supplies episode content; comparison can supply original messages."
        - scope: "Maintenance selection of statement text for theme summaries"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology]
              note: "Maintenance triggers selection of member semantic IDs present in the supplied text dictionary and delivers matching statement strings to the summarizer."
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary]
              note: "The new incremental batch limits available statement text before membership matching; old member text can be unavailable to refresh."
          records: [runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology]
          note: "Availability and actual ID matching are separate selection inputs, not proof of complete membership coverage."
        - scope: "Requested baseline/adaptive/diagnostic pull operations"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-memory-graph]
          note: "This axis classifies push selectors; lexical, embedding and judgment ranking within these requested pull chains is not an additional push signal."
        - scope: "Unknown helper/injected/provider delivery alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "Unknown direction and later consumers prevent either a positive push-signal classification or an inapplicability conclusion."
      records: [runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, memory.md#mem-obj-theme-topology, runtime.md#rt-rte-baseline-search, runtime.md#rt-rte-adaptive-reader, memory.md#mem-obj-memory-graph, memory.md#mem-obj-original-index, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "Recorded update pushes use embedding, identity and coarse availability/order selection. The whole axis is not inapplicable because pull-based QA coexists with update pushes and unresolved alternatives."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic episode summaries, semantic extraction/comparison and downstream theme updates"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, epistemic.md#epi-rte-comparison-extraction]
              note: "Recorded conversational turns automatically produce retained summaries/statements and derivative themes; later prediction, selection/scoring and answers consume them. Raw logging alone is not the warrant."
          records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary]
          note: "This is the profile's durable trace-fed write meaning. It establishes neither improved capacity nor parameter training, source faithfulness or successful operation."
        - scope: "Arbitrary injected generators/storage and hidden provider update paths"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "No complete write/retention/later-consumer chain is recorded for opaque alternatives; the known positive does not classify them."
      records: [runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, memory.md#mem-obj-episode-content, memory.md#mem-obj-semantic-content, memory.md#mem-obj-theme-summary, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "There is a wired positive trace-fed memory route, while alternative update coverage remains unresolved. No system-wide negative follows from inference-only model calls or offline scores lacking feedback."
    trace_source:
      assessment: partial
      units:
        - scope: "Conversational turns feeding episode and semantic writes, with their downstream theme derivation"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-original-messages, runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission]
              note: "Original role/content/time messages are recorded conversational turns. Theme derivation through statements retains that original trace source rather than creating a new event-stream source."
          records: [memory.md#mem-obj-original-messages, runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission]
          note: "An episode_created scheduling event is not the substantive trace input; no tool-trace or trajectory classification is inferred from it."
        - scope: "Caption/search-text supplements, arbitrary caller message provenance and opaque injected/provider learning inputs"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-conversation-admission, memory.md#mem-obj-original-messages, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
          note: "The records describe incorporated captions and search text but do not establish recorded tool requests/results, environmental event streams or linked action/outcome trajectories as their origin. Unknown alternative writes also leave their original inputs unresolved."
      records: [memory.md#mem-obj-original-messages, runtime.md#rt-rte-conversation-admission, runtime.md#rt-rte-semantic-admission, runtime.md#rt-rte-hierarchy-admission, runtime.md#rt-rte-provider-admission, runtime.md#rt-cmp-embedding-client]
      note: "Session-log input is positively established for the inspected qualifying writes; mixed supplements and opaque alternatives prevent an exclusive or complete source inventory."
---

# xMemory memory profile

## Comparison rationale

The profile classifies the accepted records, not an execution. All positive findings are **wired**: the retained members supply implementation witnesses but no observed run or causal experiment. Partial assessments preserve named alternative mechanisms and provenance gaps rather than downgrading those positive witnesses.

The memory inventory separates prose, symbolic access fields and dense vectors even when they share a file. [MEM-OBJ-retrieval-vectors](memory.md#mem-obj-retrieval-vectors) supports parametric *representation*, not a model-weights storage finding or a parameter-training claim. [MEM-OBJ-memory-graph](memory.md#mem-obj-memory-graph) supports a separate diagnostic graph/file/RAM substrate; the adaptive reader consumes theme and kNN files instead. Generic injected repositories and provider state remain unresolved rather than inheriting default classifications from readable results.

The reconciliation supersedes the epistemic originals, semantic-content and theme-summary duplicates with [MEM-OBJ-original-messages](memory.md#mem-obj-original-messages), [MEM-OBJ-semantic-content](memory.md#mem-obj-semantic-content) and [MEM-OBJ-theme-summary](memory.md#mem-obj-theme-summary). Its owner-deletion supersession resolves to [MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal). This profile cites those canonical declarations. The broader memory episode/title, topology and vector records remain valid alongside narrower epistemic parts; overlap is not a second independent witness.

Retained text has different authority at different consumers. It supplies knowledge to answering and scoring through [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader). Retained experience also feeds durable updates through [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission) and [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), supporting learning authority at those update consumers. Neither this authority nor the positive trace-learning classification asserts improved capacity. Similarity comparators have a different role: [EPI-RTE-duplicate-check](epistemic.md#epi-rte-duplicate-check) and [EPI-RTE-semantic-disposition](epistemic.md#epi-rte-semantic-disposition) establish validation plus an insertion veto, not truth acceptance. Persisted confidence without a consuming rule supplies no additional authority.

Requested QA remains pull throughout ranking, expansion, hydration and return. Automatic supply of retained inputs to later update-model invocations is a different operation: episode-event continuation supplies an identified episode, prediction receives selected prior statements, and theme summarization receives selected member strings. Those are push units within update chains, not a claim of unsolicited foreground-agent delivery. The annotations on [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission) and [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission), together with [MEM-OBJ-theme-summary](memory.md#mem-obj-theme-summary), establish embedding, fallback availability/order and identity selectors. Query-time NLL judgment in [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) is not counted as a push signal merely because code delivers requested results.

Consolidation is classified from the implemented condensation/extraction routes, not a claim of semantic equivalence. [EPI-RTE-comparison-extraction](epistemic.md#epi-rte-comparison-extraction) leaves entailment versus ampliation unresolved, so it cannot establish synthesis. Theme regeneration supports local evolution even though it can omit old member text. Explicit deletion supports local forgetting, not history-preserving invalidation or complete disappearance from all consumers; [MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal) retains the residual-file/cache and concurrent-writer limits.

The positive trace-learning route is conversation-to-retained-summary/statement-to-later-consumer, not raw log storage or offline benchmark feedback. Its original conversational turns support session-logs. Captions and search text have insufficient recorded origin for tool-traces or other additional source values. [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation) and [EPI-RTE-lexical-evaluation](epistemic.md#epi-rte-lexical-evaluation) describe post-answer reports without an automatic memory-revision consumer; those artifacts are excluded from this accumulated-memory comparison boundary. [EPI-OBJ-predicted-episode](epistemic.md#epi-obj-predicted-episode) and [EPI-OBJ-entropy-score](epistemic.md#epi-obj-entropy-score) are transient computation, not independently retained learning artifacts.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required a direct source read.
