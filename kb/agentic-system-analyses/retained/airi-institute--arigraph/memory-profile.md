---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'AriGraph memory profile: game/QA retained state, baseline context stores and partially assessed
  alternate/provider retention.'
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
source-identity: https://github.com/AIRI-Institute/AriGraph
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
memory-comparison:
  version: 2
  scope: Includes attempt/task-local facts, episodes, numerical access metadata, history, feedback plans,
    summary/full-history/smart-RAG baselines, snapshots and logger outputs; Hypergraph thesis/event/index
    and incompletely recorded inherited spatial state; auxiliary ObservedGraph and caller JSON alternatives;
    unresolved provider-internal experience retention at the adapter boundary. Excludes static shipped
    instructions, fixed model weights as such, current-only temporary action/answer proposals and diagnostic-only
    evaluation accumulators, external paper/site and bytecode-only variants. No restart persistence or
    external deployment is presumed.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Game/QA facts, episodes, history, baseline stores and feedback plans
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - memory.md#mem-obj-history
          - memory.md#mem-obj-observations
          - memory.md#mem-obj-summary
          - memory.md#mem-obj-rag-observations
          - memory.md#mem-obj-rag-metadata
          - runtime.md#rt-obj-plan
          note: Python lists, dictionaries, tuples and strings retain state within attempts/tasks.
        records: *id001
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Graph dense caches and episode vectors
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-graph-embeddings
          note: NumPy arrays and PyTorch tensors are retained in the process.
        records: *id002
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Game episode snapshots and score histories
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id003
          - memory.md#mem-obj-episodic-snapshots
          note: Historical copies accumulate in Python lists; no checkpoint replay is established.
        records: *id003
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Shipped append-only text logs
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-logs
          note: Shipped drivers append textual observations, decisions and metrics to Logger files.
        records: *id004
        note: The text logging branch is wired in shipped drivers; later reload, activation and benefit
          are not inferred.
      - scope: Unused JSON serialization capability
        assessment: known
        findings:
        - value: files
          basis: afforded
          records:
          - memory.md#mem-obj-logs
          - memory.md#mem-abs-state-readers
          note: Logger offers replacement JSON file writes as an API capability; no inspected shipped
            Python call to to_json was found, and the payload is not a known graph checkpoint.
        records:
        - memory.md#mem-obj-logs
        - memory.md#mem-abs-state-readers
        note: File storage is afforded by the inspected method, not wired by a shipped caller. Payload
          form, provenance, admission control and later consumption remain unresolved.
      - scope: Hypergraph thesis/entity/event objects and incidence/vector fields
        assessment: known
        findings:
        - value: in-memory
          basis: afforded
          records: &id005
          - memory.md#mem-obj-hypergraph-content
          - memory.md#mem-obj-hypergraph-index
          - runtime.md#rt-rte-hypergraph-update
          note: The alternate API retains dictionaries and local object fields, not a demonstrated external
            graph service.
        records: *id005
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Auxiliary ObservedGraph retained network graph
        assessment: known
        findings:
        - value: graph
          basis: afforded
          records: &id006
          - memory.md#mem-obj-observed-graph
          - memory.md#mem-rte-observed-update
          note: NetworkX MultiDiGraph stores entity/label edges for fixed graph mutation and display.
        records: *id006
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: &id015
        - runtime.md#rt-rte-hypergraph-update
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete storage
          inventory classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: &id016
        - runtime.md#rt-cmp-gpt-agent
        - runtime.md#rt-cmp-llama-agent
        note: The adapters expose requests, not provider experiential state or its storage substrate.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - memory.md#mem-obj-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-summary
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-obj-plan
      - memory.md#mem-obj-graph-embeddings
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Recorded local and file stores are classified. The undeclared inherited Hypergraph store and
        opaque provider retention prevent a complete inventory; numerical encoding is not a vector-database
        substrate.
    representational_form:
      assessment: partial
      units:
      - scope: Facts and episode/history text consumed by interpreting models
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id001
          note: Serialized fact labels, episodes, histories, summaries and plan text supply model-interpreted
            content.
        records: *id001
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Fact endpoint/spatial structure and episodic/history exact identities and ordering
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - memory.md#mem-obj-history
          - memory.md#mem-obj-observations
          note: Fixed navigation, association, membership and slicing consumers use localized structures,
            independently of model interpretation.
        records: *id007
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Graph dense episode and cache representations
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id008
          - memory.md#mem-obj-graph-embeddings
          note: Distributed numerical encodings support similarity; their readable text keys do not explain
            those vectors.
        records: *id008
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG importance/step fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - memory.md#mem-obj-rag-metadata
          note: Parsed integers and step fields are fixed ranking inputs.
        records: *id009
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG stored dense vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id010
          - memory.md#mem-obj-rag-metadata
          note: Stored observation/old-plan embeddings supply cosine-similarity input.
        records: *id010
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Snapshot content, association fields and vectors
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - memory.md#mem-obj-episodic-snapshots
          note: Copies retain episode text.
        - value: symbolic
          basis: wired
          records: *id011
          note: Copies retain exact association keys and numeric ranking metadata.
        - value: parametric
          basis: wired
          records: *id011
          note: Copies retain dense tensors, without an established later reader.
        records: *id011
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Log text and metric displays
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records: &id012
          - memory.md#mem-obj-logs
          note: Text logging retains observation and decision displays.
        - value: symbolic
          basis: wired
          records: *id012
          note: Metrics are localized numeric fields rendered to files.
        records: *id012
        note: The text logging branch is inspected. Arbitrary caller JSON payload form is not established;
          it cannot inherit the displayed text classification.
      - scope: Hypergraph thesis and event names
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id013
          - memory.md#mem-obj-hypergraph-content
          note: The API returns thesis sentences and original event text.
        records: *id013
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph incidence structure and dense fields
        assessment: known
        findings:
        - value: symbolic
          basis: afforded
          records: &id014
          - memory.md#mem-obj-hypergraph-index
          note: Hashed IDs and parent/child links support fixed traversal and overlap.
        - value: parametric
          basis: afforded
          records: *id014
          note: Dense event vectors supply similarity scores.
        records: *id014
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Auxiliary observed edges
        assessment: known
        findings:
        - value: symbolic
          basis: afforded
          records: *id006
          note: Fixed endpoint, label and substring rules mutate and display graph edges.
        records: *id006
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete form/consumption-path
          classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its operative representational
          form. Static model weights are excluded; this uncertainty does not assert that a provider memory
          write exists.
      records:
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - memory.md#mem-obj-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-summary
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-obj-plan
      - memory.md#mem-obj-graph-embeddings
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - runtime.md#rt-rte-hypergraph-update
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Text, fixed structure and dense numerical parts remain distinct. Arbitrary JSON, the incomplete
        alternate spatial inventory and provider retention remain unresolved.
    lineage:
      assessment: partial
      units:
      - scope: Game extracted facts and raw retained episodes
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id017
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - runtime.md#rt-rte-game-memory
          note: Extraction and episode retention originate in game observations, not a human-authored
            memory entry.
        records: *id017
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Movement-derived main-graph relations
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id018
          - memory.md#mem-obj-triplets
          - runtime.md#rt-rte-game-memory
          note: Fixed direction mapping compiles reciprocal edges from location changes and the previous
            action; world truth is not established.
        records: *id018
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: QA paragraph content and extracted facts
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id019
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - runtime.md#rt-rte-qa-cycle
          note: Dataset paragraphs enter the task memory from external content.
        - value: other-compiled
          basis: wired
          records: *id019
          note: Model extraction produces normalized facts from those imported static paragraphs; they
            are not game traces.
        records: *id019
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Recent/full/smart-RAG observation and action stores
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id020
          - memory.md#mem-obj-history
          - memory.md#mem-obj-observations
          - memory.md#mem-obj-rag-observations
          note: Driver activity is retained as cleaned observations and selected actions.
        records: *id020
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Summary and feedback plan replacement
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id021
          - memory.md#mem-obj-summary
          - runtime.md#rt-obj-plan
          - runtime.md#rt-rte-summary-cycle
          note: The initial plan/summary strings are shipped seeds, not learned outputs.
        - value: trace-extracted
          basis: wired
          records: *id021
          note: Later responses derive from current observations, retained history and previous context.
        records: *id021
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Graph/smart-RAG vectors, importance and snapshots
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id022
          - memory.md#mem-obj-graph-embeddings
          - memory.md#mem-obj-rag-metadata
          - memory.md#mem-obj-episodic-snapshots
          - runtime.md#rt-cmp-retriever
          note: Inference creates numerical access metadata and code copies current episode state.
        records: *id022
        note: Local derivation is inspected. Exact upstream checkpoint/tokenizer provenance is unpinned
          and cannot be reconstructed from the vectors.
      - scope: Hypergraph thesis/event names and access structures
        assessment: partial
        findings:
        - value: other-compiled
          basis: afforded
          records: *id005
          note: The API extracts supplied content, embeds names and constructs hashed incidence links.
        records: *id005
        note: The supplied observation-to-state derivation is known; original caller input provenance
          and deployed use are uninspected, so trace or imported origin is not assigned universally.
      - scope: Auxiliary observed-graph input provenance
        assessment: not-determinable
        findings: []
        records: *id006
        note: Caller-supplied full graph/replacement state has unresolved provenance; fixed subsequent
          mutations do not settle initial lineage.
      - scope: Driver text log copies
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id023
          - memory.md#mem-obj-logs
          note: Software records observations, model decisions and runtime metrics.
        records: *id023
        note: Shipped text logging has known activity origin. The unused arbitrary JSON payload capability
          has unresolved caller lineage.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete complete
          lineage classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its experience lineage.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - runtime.md#rt-rte-game-memory
      - runtime.md#rt-rte-qa-cycle
      - memory.md#mem-obj-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-summary
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-summary-cycle
      - memory.md#mem-obj-graph-embeddings
      - memory.md#mem-obj-rag-metadata
      - memory.md#mem-obj-episodic-snapshots
      - runtime.md#rt-cmp-retriever
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Known derivation paths do not settle caller input provenance or upstream model provenance.
        Seeds and static paragraph acquisition remain separate from game experience.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected facts/episodes at game planner/action and QA answer models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id024
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - runtime.md#rt-bap-memory-decisions
          note: Delivered strings supply informational context; receipt does not establish truth or activation.
        records: *id024
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Retained game facts at extraction/replacement update models
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id025
          - memory.md#mem-obj-triplets
          - runtime.md#rt-rte-game-memory
          note: Previously selected facts serve as extraction examples and maintenance inputs to an automatic
            experience-fed durable fact update.
        records: *id025
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Retained fact/episode text and episode vectors at relevance selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id026
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - memory.md#mem-obj-graph-embeddings
          - runtime.md#rt-rte-game-memory
          - runtime.md#rt-rte-qa-cycle
          note: Text is re-embedded for semantic scoring; extraction associations and stored episode vectors
            affect episode priority.
        records: *id026
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Spatial triples at path/exploration software
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id027
          - memory.md#mem-obj-triplets
          - runtime.md#rt-rte-graph-navigation
          note: Spatial relations select a navigation path and graph-derived exploration inputs; dispatch
            is not a truth check.
        records: *id027
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Recent history and full/smart-RAG text at planner/action models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id028
          - memory.md#mem-obj-history
          - memory.md#mem-obj-observations
          - memory.md#mem-obj-rag-observations
          note: Prior observations/actions are delivered as historical context.
        records: *id028
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Recent observation exclusion list at episodic filter
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id029
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-game-memory
          note: Exact-string membership excludes matching episodes from delivery; inventory mismatch prevents
            reliable recent-window suppression.
        records: *id029
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Summary at planner/action models and next summarizer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id030
          - memory.md#mem-obj-summary
          - runtime.md#rt-rte-summary-cycle
          note: The current summary supplies a situation account to decision models.
        - value: learning
          basis: wired
          records: *id030
          note: The retained previous summary feeds the next automatic trace-fed replacement.
        records: *id030
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Feedback plan at later model requests
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id031
          - runtime.md#rt-obj-plan
          - runtime.md#rt-bap-plan-decisions
          note: Retained goals and priorities guide entity, exploration, planning and action roles.
        - value: ranking
          basis: wired
          records: *id031
          note: Its dense encoding influences episodic relevance.
        - value: learning
          basis: wired
          records: *id031
          note: The previous plan feeds the next experience-responsive whole-plan update.
        records: *id031
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG numeric metadata at software ranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id032
          - memory.md#mem-obj-rag-metadata
          - runtime.md#rt-rte-smart-rag
          note: Step/importance/similarity fields alter relative selection priority, without model-facing
            factual force.
        records: *id032
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph names/incidence/event vectors at API retrieval
        assessment: partial
        findings:
        - value: ranking
          basis: afforded
          records: *id005
          note: Retained thesis names, child overlaps and event vectors influence returned subsets; ascending
            event sorting is not highest-score-first delivery.
        records: *id005
        note: API selection force is inspected; external planner consumption and its authority are uninspected.
      - scope: Snapshots/logs at possible later consumers
        assessment: uninspected
        findings: []
        records: &id052
        - memory.md#mem-obj-logs
        - memory.md#mem-obj-episodic-snapshots
        - memory.md#mem-abs-state-readers
        note: No shipped snapshot replay or log-reload behavioral consumer is established. External consumption
          and arbitrary JSON consumers are not inspected; mere retention grants no authority.
      - scope: Auxiliary observed graph at later behavioral consumers
        assessment: uninspected
        findings: []
        records: *id006
        note: Mutation/display is available, but no shipped later agent or model consumer establishes
          an authority path.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete consumer/authority
          classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its behavioral authority.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - runtime.md#rt-bap-memory-decisions
      - runtime.md#rt-rte-game-memory
      - memory.md#mem-obj-graph-embeddings
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-graph-navigation
      - memory.md#mem-obj-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-summary
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-obj-plan
      - runtime.md#rt-bap-plan-decisions
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-abs-state-readers
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Knowledge, learning, instruction, ranking, routing and a bounded exact-match enforcement path
        have local warrants. Static prompt rules and current-run parser criteria are excluded; they do
        not classify retained memory as validation. Unresolved auxiliary consumers prevent complete authority
        coverage.
    write_agency:
      assessment: partial
      units:
      - scope: Game/QA admission, recent/full/smart-RAG appends, summary and plan replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id033
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - memory.md#mem-obj-history
          - memory.md#mem-obj-observations
          - memory.md#mem-obj-summary
          - memory.md#mem-obj-rag-observations
          - memory.md#mem-obj-rag-metadata
          - runtime.md#rt-obj-plan
          - runtime.md#rt-rte-game-memory
          - runtime.md#rt-rte-qa-cycle
          - runtime.md#rt-rte-summary-cycle
          - runtime.md#rt-rte-smart-rag
          note: Models/software admit retained content without a separate human decision on each item;
            starting/configuring a script is not manual memory admission.
        records: *id033
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Graph vectors and episode snapshot writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id034
          - memory.md#mem-obj-graph-embeddings
          - memory.md#mem-obj-episodic-snapshots
          note: Software computes numerical state and copies dictionaries on update.
        records: *id034
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Shipped text logger admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id035
          - memory.md#mem-obj-logs
          note: Drivers/models supply recorded content and software appends it without per-entry approval.
        records: *id035
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph content/vector/link admissions
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records: *id005
          note: Model proposals and parsed/software additions are admitted without per-item operator review
            in the API mechanism.
        records: *id005
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: ObservedGraph caller-supplied initialization/replacement and mutation
        assessment: not-determinable
        findings: []
        records: *id006
        note: Generic caller identity does not distinguish a human decision supplying/replacing retained
          content from computational admission.
      - scope: Unused arbitrary JSON logger payload admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-logs
        note: File replacement capability is inspected, but caller control of arbitrary content is unresolved
          and no shipped call exists.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete separate
          spatial-store admission coverage classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its write control. Static
          model weights are excluded; this uncertainty does not assert that a provider memory write exists.
      records:
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - memory.md#mem-obj-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-summary
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-game-memory
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-graph-embeddings
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Computational admission is positive on inspected shipped routes and Hypergraph internals.
        Unknown generic caller control is not manual or automatic by default; authored seed provenance
        does not change automatic run admission.
    curation_operations:
      assessment: partial
      units:
      - scope: Main graph normalized duplicate suppression
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id036
          - memory.md#mem-obj-triplets
          - epistemic.md#epi-rte-triplet-parsing
          note: Normalized equal triplets are suppressed as duplicate fact content, beyond merely assigning
            an object ID.
        records: *id036
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Game fact replacement/withdrawal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id037
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - epistemic.md#epi-rte-removal-parsing
          - runtime.md#rt-rte-game-memory
          note: Model-proposed old-fact removals plus new admissions revise the live fact pool, without
            a validated replacement transaction.
        - value: invalidate
          basis: wired
          records: *id037
          note: Deletion withdraws live semantic reliance while historical episode text and extraction
            associations survive.
        records: *id037
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Main recent-history slicing
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id038
          - memory.md#mem-obj-history
          note: The bounded last-five history drops older retained entries from that store; it does not
            invalidate graph episodes.
        records: *id038
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Summary baseline replacement
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id039
          - memory.md#mem-obj-summary
          - runtime.md#rt-rte-summary-cycle
          note: The model combines/compresses retained history and prior summary into a reduced situation
            account.
        - value: evolve
          basis: wired
          records: *id039
          note: Each response replaces the prior retained summary.
        records: *id039
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Feedback plan replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id040
          - runtime.md#rt-obj-plan
          - runtime.md#rt-rte-game-cycle
          note: The entire retained task plan is revised using new context and the previous plan.
        records: *id040
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG retained-entry recency contribution
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id041
          - memory.md#mem-obj-rag-metadata
          - runtime.md#rt-rte-smart-rag
          note: A recency-decay score downweights older retained entries during selection; it is not storage
            eviction.
        records: *id041
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph thesis withdrawal
        assessment: partial
        findings:
        - value: invalidate
          basis: afforded
          records: *id005
          note: Deleting thesis objects and incidence links withdraws that live thesis while parent event
            text remains historical content.
        records: *id005
        note: The removal/link transformation is inspected. Uninspected original input and downstream
          callers prevent extending this to universal memory maintenance.
      - scope: Auxiliary observed-state revision
        assessment: known
        findings:
        - value: evolve
          basis: afforded
          records: *id006
          note: Fixed methods remove old edge state and add replacement state.
        records: *id006
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Arbitrary logger JSON replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-logs
        note: Overwriting a file does not establish a semantic curation operation over its unknown payload.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete spatial-store
          maintenance classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its curation. Static model
          weights are excluded; this uncertainty does not assert that a provider memory write exists.
      records:
      - memory.md#mem-obj-triplets
      - epistemic.md#epi-rte-triplet-parsing
      - memory.md#mem-obj-obs-episodic
      - epistemic.md#epi-rte-removal-parsing
      - runtime.md#rt-rte-game-memory
      - memory.md#mem-obj-history
      - memory.md#mem-obj-summary
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-game-cycle
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Implemented memory transformations establish dedup, evolve, invalidate, consolidate and decay
        on named routes. Acquisition, index construction and hash collisions alone add no curation finding.
        Indeterminate semantic fidelity does not establish synthesis, and wiring does not establish improvement.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested game/QA fact and episode retrieval
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id042
          - runtime.md#rt-rte-game-memory
          - runtime.md#rt-rte-qa-cycle
          note: Shipped drivers request retained facts/text; automatic ranking inside the request does
            not make delivery unsolicited push.
        records: *id042
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Main graph navigation/exploration reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id043
          - runtime.md#rt-rte-graph-navigation
          - memory.md#mem-obj-triplets
          note: Driver operations request path or graph-derived exit content from retained spatial facts.
        records: *id043
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Driver-supplied recent/full history, feedback plan and summary
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id044
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-full-history
          - runtime.md#rt-obj-plan
          - runtime.md#rt-rte-summary-cycle
          note: The driver inserts retained context into later model invocations without a model request
            for those retained parts.
        records: *id044
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG context construction
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id045
          - runtime.md#rt-rte-smart-rag
          note: On each decision round the driver automatically selects and supplies retained text/action
            pairs to planner/action requests.
        records: *id045
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Hypergraph requested read API
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records: &id046
          - runtime.md#rt-rte-hypergraph-update
          note: A caller can request the update/retrieval method and receive retained thesis/event text.
        records: *id046
        note: API return is afforded; downstream behavioral delivery and deployment are not established.
      - scope: Auxiliary state access, snapshots and log/JSON later consumption
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-observed-graph
        - memory.md#mem-rte-observed-update
        - memory.md#mem-obj-logs
        - memory.md#mem-obj-episodic-snapshots
        - memory.md#mem-abs-state-readers
        note: Display/access capabilities and no shipped snapshot replay do not identify external later
          requests or unsolicited delivery.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete spatial
          read-back classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its read-back direction.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - runtime.md#rt-rte-game-memory
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-graph-navigation
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-full-history
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-rte-smart-rag
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-abs-state-readers
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Pull and push occur on different chains. Requested graph delivery is not counted again as
        push. Opaque and undeployed alternatives prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: History, summary and plan context pushes
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id047
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-full-history
          - runtime.md#rt-rte-summary-cycle
          - runtime.md#rt-obj-plan
          note: 'Trigger: each driver decision round. Selector: availability/current plan or summary,
            and full or bounded recent history. Selected part: the whole current retained string or history
            window.'
        records: *id047
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG ranked text/action push
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records: &id048
          - runtime.md#rt-rte-smart-rag
          - memory.md#mem-obj-rag-metadata
          - memory.md#mem-obj-rag-observations
          note: 'Trigger: decision round. Current observation/old-plan embedding is compared with stored
            vectors to select retained text/action pairs.'
        - value: inferred-judgment
          basis: wired
          records: *id048
          note: Model-derived retained importance scores contribute to selecting those pairs.
        - value: coarse
          basis: wired
          records: *id048
          note: Step-based recency and the separately indexed recent-entry expression also select retained
            pairs; the expression includes the oldest entry at index zero.
        records: *id048
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Completely inspected requested game/QA/navigation branches
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-game-memory
        - runtime.md#rt-rte-qa-cycle
        - runtime.md#rt-rte-graph-navigation
        note: These branches fulfill explicit caller requests rather than push. Embedding selection within
          a pull request is not a push signal.
      - scope: Hypergraph API and possible downstream delivery
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hypergraph-update
        note: The requested return is known, but downstream use is not assessed; no inferred push signal
          is assigned to event ranking.
      - scope: Auxiliary/log/snapshot possible pushes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-observed-graph
        - memory.md#mem-rte-observed-update
        - memory.md#mem-obj-logs
        - memory.md#mem-obj-episodic-snapshots
        - memory.md#mem-abs-state-readers
        note: No recorded external push operation supplies a trigger, selector and selected retained part.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete spatial
          push selection classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its push selector. Static
          model weights are excluded; this uncertainty does not assert that a provider memory write exists.
      records:
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-full-history
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-rag-metadata
      - memory.md#mem-obj-rag-observations
      - runtime.md#rt-rte-game-memory
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-graph-navigation
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-abs-state-readers
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Known push routes use coarse windows and smart-RAG embedding/judgment inputs. No identifier
        push is inferred from dictionary/hash IDs. Pull-only local inapplicability cannot settle unknown
        alternatives.
    trace_learning:
      assessment: partial
      units:
      - scope: Game observation-to-fact/episode update with later planner/action consumption
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id049
          - runtime.md#rt-rte-game-memory
          - memory.md#mem-obj-triplets
          - memory.md#mem-obj-obs-episodic
          - runtime.md#rt-bap-memory-decisions
          note: Automatic game experience writes retained derived facts whose later selected content shapes
            decision context within the attempt.
        records: *id049
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Summary and feedback-plan experience-fed replacement
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id050
          - runtime.md#rt-rte-summary-cycle
          - memory.md#mem-obj-summary
          - runtime.md#rt-obj-plan
          - runtime.md#rt-rte-game-cycle
          note: Retained history/observations feed automatic replacement artifacts consumed by later model
            roles; cross-restart storage and measured benefit are not required.
        records: *id050
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG experience-fed importance and vectors
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id051
          - runtime.md#rt-rte-smart-rag
          - memory.md#mem-obj-rag-metadata
          note: Automatic trace-derived numeric metadata persists and shapes selection for later planner/action
            contexts.
        records: *id051
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: QA static paragraph admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-qa-cycle
        note: The recorded route extracts static paragraphs and terminates answer metrics diagnostically.
          No canonical bounded-absence record establishes local no for qualifying trace-fed writes, so
          a negative classification is withheld.
      - scope: Full-history raw trace append alone
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-full-history
        - memory.md#mem-obj-observations
        note: The recorded mechanism retains raw observation/action text rather than a derived artifact.
          Raw context delivery does not establish yes, and no canonical bounded-absence record warrants
          local no.
      - scope: Hypergraph thesis/event API
        assessment: not-determinable
        findings: []
        records: *id005
        note: Automatic derivation is available, but original caller trace provenance and qualifying later
          behavioral consumption are not established.
      - scope: Auxiliary observed graph and arbitrary JSON content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-observed-graph
        - memory.md#mem-rte-observed-update
        - memory.md#mem-obj-logs
        note: Caller control/provenance and later behavioral consumption are unresolved; mutation or file
          I/O alone does not establish the qualifying chain.
      - scope: Snapshot and text log external learning consumers
        assessment: uninspected
        findings: []
        records: *id052
        note: These retain traces/copies without shipped replay. External trace-fed learning writes using
          them have not been inspected.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete spatial
          trace-to-later-consumer chain classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its trace-fed updates.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - runtime.md#rt-rte-game-memory
      - memory.md#mem-obj-triplets
      - memory.md#mem-obj-obs-episodic
      - runtime.md#rt-bap-memory-decisions
      - runtime.md#rt-rte-summary-cycle
      - memory.md#mem-obj-summary
      - runtime.md#rt-obj-plan
      - runtime.md#rt-rte-game-cycle
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-full-history
      - memory.md#mem-obj-observations
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-abs-state-readers
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: The derived system union includes yes on supported routes. QA/raw-history routes lack canonical
        bounded-absence records for local no and remain unresolved rather than producing a system-wide
        negative. Trace learning here is retained behavior-shaping transformation, not demonstrated capacity
        improvement.
    trace_source:
      assessment: partial
      units:
      - scope: Game fact extraction and current observation input to summary/plan updates
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id053
          - runtime.md#rt-rte-game-memory
          - runtime.md#rt-rte-summary-cycle
          - runtime.md#rt-rte-game-cycle
          note: Environmental observations/feedback are discrete game-state events admitted to automatic
            derived-memory writes, not conversational session logs.
        records: *id053
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Movement-linked facts and multi-step summary/plan inputs
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records: &id054
          - memory.md#mem-obj-triplets
          - runtime.md#rt-rte-game-memory
          - runtime.md#rt-rte-summary-cycle
          - runtime.md#rt-obj-plan
          - memory.md#mem-obj-history
          note: Previous action/location and resulting location, or ordered observation/action history
            across rounds, provide linked states/actions/outcomes to the qualifying update.
        records: *id054
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: Smart-RAG importance/vector production
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id055
          - runtime.md#rt-rte-smart-rag
          - memory.md#mem-obj-rag-observations
          - memory.md#mem-obj-rag-metadata
          note: The original current environmental observation feeds automatic rating/embedding production.
            A pre-action tuple is not by itself an evaluated multi-step trajectory.
        records: *id055
        note: The cited records identify the retained part, implemented path and consumers within this
          unit; operation and benefit are not inferred.
      - scope: QA and raw-only full-history mechanisms
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-qa-cycle
        - runtime.md#rt-rte-full-history
        note: The recorded static paragraph extraction and raw-only append establish no positive qualifying
          trace source. Without a canonical bounded-absence warrant for local trace learning, source inapplicability
          cannot be asserted.
      - scope: Hypergraph possible trace-fed caller route
        assessment: not-determinable
        findings: []
        records: *id005
        note: Original caller content and a qualifying later behavioral consumer are not recorded; an
          API argument named observation does not establish environmental events.
      - scope: Auxiliary graph/JSON possible qualifying writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-observed-graph
        - memory.md#mem-rte-observed-update
        - memory.md#mem-obj-logs
        note: Unknown caller provenance/control and later consumption prevent classifying original learning
          input.
      - scope: Logs/snapshots as possible external learning inputs
        assessment: uninspected
        findings: []
        records: *id052
        note: No external qualifying learning write was inspected; stored activity alone does not establish
          its trace source.
      - scope: Hypergraph inherited movement-triplet state beyond its recorded insertion
        assessment: not-determinable
        findings: []
        records: *id015
        note: The runtime records reciprocal movement additions but leaves the relation to thesis/event
          state and later consumers unassessed. The missing separate part record prevents complete spatial
          qualifying trace source classification; it is not silently excluded.
      - scope: Unresolved provider-internal experience retention behind the generation adapters
        assessment: uninspected
        findings: []
        records: *id016
        note: The adapters expose requests, not provider experiential state or its original trace input.
          Static model weights are excluded; this uncertainty does not assert that a provider memory write
          exists.
      records:
      - runtime.md#rt-rte-game-memory
      - runtime.md#rt-rte-summary-cycle
      - runtime.md#rt-rte-game-cycle
      - memory.md#mem-obj-triplets
      - runtime.md#rt-obj-plan
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-smart-rag
      - memory.md#mem-obj-rag-observations
      - memory.md#mem-obj-rag-metadata
      - runtime.md#rt-rte-qa-cycle
      - runtime.md#rt-rte-full-history
      - memory.md#mem-obj-hypergraph-content
      - memory.md#mem-obj-hypergraph-index
      - runtime.md#rt-rte-hypergraph-update
      - memory.md#mem-obj-observed-graph
      - memory.md#mem-rte-observed-update
      - memory.md#mem-obj-logs
      - memory.md#mem-obj-episodic-snapshots
      - memory.md#mem-abs-state-readers
      - runtime.md#rt-cmp-gpt-agent
      - runtime.md#rt-cmp-llama-agent
      note: Original environmental events and linked game experience establish local source values. No
        session-log or tool-trace source is inferred from prompt wrapping, text serialization or ordinary
        environmental dispatch. Unknown qualifying writes remain unresolved.
---

# AriGraph memory profile

## Comparison rationale

This profile classifies retained objects and actual consumption paths, not the whole runtime's permissions or every model component. All ten axes are partial because included alternatives remain unresolved. Local known units retain positive implementation evidence without upgrading opaque alternatives. The basis is wired for shipped local routes and afforded for alternate library mechanisms. No finding upgrades delivery to activation or attributed scores to causal benefit.

### Inventory and reconciliation limits

The reconciliation supersedes the epistemic triplet, episode-text and summary declarations with [MEM-OBJ-triplets](memory.md#mem-obj-triplets), [MEM-OBJ-obs-episodic](memory.md#mem-obj-obs-episodic) and [MEM-OBJ-summary](memory.md#mem-obj-summary). Those canonical objects carry the corresponding values here. The Hypergraph thesis/event container is not superseded; its content and index parts are classified separately using [MEM-OBJ-hypergraph-content](memory.md#mem-obj-hypergraph-content) and [MEM-OBJ-hypergraph-index](memory.md#mem-obj-hypergraph-index).

The unresolved inherited Hypergraph spatial-store omission is retained as an included unresolved unit on every axis. [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) supports movement-derived insertion but explicitly leaves its relation to the other state unassessed. This profile neither invents the missing object record nor assigns that alternate store to the main ContrieverGraph object. A complete inventory needs the declaring analysts' additional record and consumer account. The omission can be stated faithfully as a limit here; it prevents every axis from becoming system-complete.

[MEM-RTE-observed-update](memory.md#mem-rte-observed-update) leaves generic caller admission, initial provenance and downstream consumption unresolved. [MEM-OBJ-logs](memory.md#mem-obj-logs) distinguishes known text logging from arbitrary caller JSON. Storage findings separate wired append-only text logging from afforded replacement JSON writes; the unused JSON capability cannot inherit the shipped text branch's basis, and displayed text cannot classify its unknown serialized payload. [MEM-ABS-state-readers](memory.md#mem-abs-state-readers) bounds the lack of shipped snapshot replay and accessor calls, not all external consumption. Provider internals remain uninspected under [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent) and [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent); this profile does not assert an experiential provider store exists.

### Mapping choices

Process-local retention can shape later invocations without surviving process restart. Dense vectors are parametric representational form, not evidence of a vector-service substrate or model-weight training: [MEM-OBJ-graph-embeddings](memory.md#mem-obj-graph-embeddings). Their local derivation is known while upstream checkpoint provenance remains limited by [RT-CMP-retriever](runtime.md#rt-cmp-retriever).

Game facts and static QA paragraph extraction have different origins. Game-derived facts are trace-extracted; dataset text is imported and its extraction is other-compiled. [MEM-OBJ-triplets](memory.md#mem-obj-triplets) also records deterministic spatial compilation, which does not prove the inferred relation is true. The indeterminate semantic edges in [EPI-RTE-triplet-parsing](epistemic.md#epi-rte-triplet-parsing) and the extraction account do not justify a synthesis finding. Summary consolidation describes the implemented reduced-memory transformation, not guaranteed faithful meaning preservation: [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle).

Authority belongs to each actual consumer. Old retained facts and prior summaries feed automatic memory updates (learning), selected text supplies decision context (knowledge), plan priorities guide later roles (instruction), vectors/text/importance influence relative selection (ranking), and spatial edges select navigation (routing). These paths are separately warranted by [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions), [RT-BAP-plan-decisions](runtime.md#rt-bap-plan-decisions), [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation) and [MEM-OBJ-rag-metadata](memory.md#mem-obj-rag-metadata). The recent exclusion list has an exact-match veto, but its inventory-augmented strings need not match pre-inventory episode keys: [MEM-OBJ-history](memory.md#mem-obj-history), [MEM-OBJ-obs-episodic](memory.md#mem-obj-obs-episodic). No validation authority is inferred from static parser criteria or diagnostic answer metrics.

Requested graph retrieval is pull, including its internal automatic selectors. Separately, drivers push histories, current summaries/plans and selected smart-RAG entries into model requests. [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag) supports embedding and retained model-importance selectors plus coarse recency/recent-entry selection; dictionary/hash identities alone establish no identifier push. Unknown external delivery cannot become inapplicable merely because an inspected API returns requested content.

Qualifying automatic game fact, summary, plan and smart-RAG metadata writes retain behavior-shaping outputs for later consumption. This is trace learning under the comparison contract, not demonstrated improvement. The source is environmental events or linked game experience, not session conversation merely because the model receives messages. The inspected QA route instead extracts static paragraphs, and full history only appends raw traces: [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle), [RT-RTE-full-history](runtime.md#rt-rte-full-history). Neither route has a canonical bounded-absence record warranting local no; both remain not-determinable without cancelling other routes' yes. Library APIs without recorded original trace content and later behavioral consumers remain unresolved.

### Source reads and checks

No source checkout reads were performed. Classification uses only the supplied records and reconciliation; no records, quotations or evidence were added. Deterministic validation is reported by the required invocation check, not taken as evidence of analytical completeness.
