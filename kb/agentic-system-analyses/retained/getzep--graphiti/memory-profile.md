---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Graphiti memory comparison covering retained graph content, selectors, vectors, summaries, the shipped conversation checkpoint and evaluation exports at the frozen revision."
run-id: "AAS-2026-10-12-graphiti-1d535ca565a4-01"
source-identity: "https://github.com/getzep/graphiti"
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
memory-comparison:
  version: 2
  scope: "Included: accumulated episode/entity/fact content, typed and temporal/lineage access parts, persisted graph embeddings, community and saga summaries/cursors, notebook conversation checkpoint, evaluation graph/results files, and their admission, maintenance and later-consumer routes. Other shipped example/evaluator, backend and consumer alternatives remain included as unresolved coverage. Excluded: static shipped prompts/rules/schema/configuration as memory objects, transient ingestion queues and current-call objects, external provider weights/internals, proprietary Zep and unregistered historical notebook outputs. Shipped MCP rules supply evidence of an afforded consumer role, not accumulated instructions."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Graphiti episodes, entity/fact text, attributes, identities, temporal fields, membership, vectors and community/saga state"
          assessment: "known"
          findings:
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-graph-metadata"
                - "memory.md#mem-obj-graph-embeddings"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
              note: "Driver persistence retains text, symbolic selectors and dense vectors on graph storage, independently of their encoding."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-obj-graph-embeddings"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
          note: "These operative retained parts are graph properties/relationships through driver writes; transient construction objects are not an additional retained store."
        -
          scope: "Evaluation baseline/candidate JSON exports and retained evaluation graph"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Baseline JSON is reloaded as typed results for later judgment."
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Graph-building evaluation also retains episodes/entities/edges through Graphiti."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "The comparison route serializes results locally and reloads baseline files; evaluation graph state is separately retained."
        -
          scope: "Notebook MemorySaver checkpoint"
          assessment: "partial"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "runtime.md#rt-rte-conversation-loop"
              note: "The notebook requests MemorySaver state keyed by thread for later model context, separately from graph memory."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Shipped code requests an in-process checkpointer; its exact internals and durability are outside the frozen source."
        -
          scope: "Remaining included backend/index serialization and other example/evaluator retained parts"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-obj-graph-embeddings"
            - "runtime.md#rt-rte-maintenance-writes"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Backend roundtrips and other included consumers/evaluators were not exhaustively traced; the inspected graph/file witnesses do not close the retained-object inventory."
      records:
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "memory.md#mem-obj-graph-metadata"
        - "memory.md#mem-obj-graph-embeddings"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-memory-saver"
        - "runtime.md#rt-rte-conversation-loop"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Graph, files and an in-process checkpoint are supported locally. Remaining included backend and consumer variants prevent complete inventory coverage. Provider weights, static prompts and admission queues are not accumulated knowledge stores in this scope."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Readable episode text, entity names/summaries, fact text, community names/summaries and saga summary at model/text consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "runtime.md#rt-bap-facts-context"
              note: "Text supplies extraction/summarization context and retrieved descriptions; the notebook formats edge.fact for its model."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "runtime.md#rt-bap-facts-context"
          note: "This unit is limited to the readable text parts, not JSON fields, typed attributes or vectors."
        -
          scope: "Graph UUIDs, groups, endpoints, lineage references, temporal fields, memberships and saga cursors at fixed code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-metadata"
                - "memory.md#mem-obj-saga-node"
                - "epistemic.md#epi-obj-saga-watermarks"
              note: "Fixed lookup, remapping, deletion and timestamp-filter rules consume localized IDs and dates."
          records:
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-obj-saga-node"
            - "epistemic.md#epi-obj-saga-watermarks"
          note: "Identity/temporal selector parts are separate from descriptive text."
        -
          scope: "Persisted entity/community name embeddings and fact embeddings at similarity selectors"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-embeddings"
                - "epistemic.md#epi-obj-edge-embedding"
                - "runtime.md#rt-rte-context-retrieval"
              note: "Dense numerical representations distribute selection information across vector coordinates."
          records:
            - "memory.md#mem-obj-graph-embeddings"
            - "epistemic.md#epi-obj-edge-embedding"
            - "runtime.md#rt-rte-context-retrieval"
          note: "Dense retained encodings are not provider weights or assistant-facing fact strings."
        -
          scope: "Caller JSON episodes and schema-dependent attributes"
          assessment: "partial"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "epistemic.md#epi-obj-entity-attributes"
              note: "Typed attribute keys/values and source typing have fixed schema/dispatch consumers."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "epistemic.md#epi-obj-entity-attributes"
              note: "Descriptive values and serialized source text can be interpreted by extraction models."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "epistemic.md#epi-obj-entity-attributes"
          note: "Typed fields have symbolic consumers and may contain textual values; field-level content and all schema variants remain unresolved."
        -
          scope: "Notebook checkpoint boundary and evaluation exports"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Checkpoint message payloads reach the model; exported descriptions reach the judge."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Thread/tool/state fields and serialized graph associations have structured consumers."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-conversation-loop"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Boundary records show structured messages and graph-result fields, but checkpoint internal encoding is uninspected."
        -
          scope: "Remaining included prompt/backend/consumer variants"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-graph-embeddings"
            - "runtime.md#rt-rte-maintenance-writes"
          note: "Untraced attribute and alternate consumer parts prevent exhaustive form coverage; readable display does not classify undisplayed numerical payloads."
      records:
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "runtime.md#rt-bap-facts-context"
        - "memory.md#mem-obj-graph-metadata"
        - "epistemic.md#epi-obj-saga-watermarks"
        - "memory.md#mem-obj-graph-embeddings"
        - "epistemic.md#epi-obj-edge-embedding"
        - "runtime.md#rt-rte-context-retrieval"
        - "epistemic.md#epi-obj-entity-attributes"
        - "memory.md#mem-obj-memory-saver"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-conversation-loop"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Text, symbolic selectors and dense parametric vectors coexist. Their consumers are split; opaque checkpoint internals and untraced mixed fields remain unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-supplied episodes, triplets and direct names/summaries"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "runtime.md#rt-rte-maintenance-writes"
              note: "Caller-supplied content enters episode or direct-write acquisition paths without Graphiti establishing its original warrant."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "runtime.md#rt-rte-maintenance-writes"
          note: "This classifies entry into Graphiti, not whether an upstream author was human or a model."
        -
          scope: "Notebook conversation-derived graph facts/summaries"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-entity-node"
              note: "Automatic conversation recording feeds extraction and summary generation; tool-returned facts can recirculate."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-entity-node"
          note: "The inspected producer captures latest human/tool/model state plus new response and processes it for later graph retrieval."
        -
          scope: "Entity summary appending, community reduction and saga folding from retained content"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
                - "epistemic.md#epi-rte-entity-summary"
              note: "Existing summaries, facts and linked episodes are transformed into subsequent retained descriptions."
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
            - "epistemic.md#epi-rte-entity-summary"
          note: "These derivation paths are known even though semantic fidelity is not established."
        -
          scope: "Graph identities, lineage associations, temporal selectors and saga watermarks"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-metadata"
                - "memory.md#mem-obj-saga-node"
                - "epistemic.md#epi-obj-edge-episodes"
              note: "Extraction/remapping and timestamp rules produce retained symbolic associations and selection state."
          records:
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-obj-saga-node"
            - "epistemic.md#epi-obj-edge-episodes"
          note: "Software/model attribution and timestamp policy construct these access parts; association is not authenticated source evidence."
        -
          scope: "Retained graph embeddings"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-embeddings"
                - "epistemic.md#epi-obj-edge-embedding"
              note: "Inspected embedding paths encode retained fact/name text through inference; this is not training graph-owned weights."
          records:
            - "memory.md#mem-obj-graph-embeddings"
            - "epistemic.md#epi-obj-edge-embedding"
          note: "Fact/name encoding is wired, but initial caller vectors and community-generation variants are not uniformly traced."
        -
          scope: "Evaluation exports"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Selected external dataset messages supply evaluation inputs."
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Dataset session messages are processed into graph results retained for later comparison."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Dataset acquisition and configured graph construction are distinct derivation steps."
        -
          scope: "Checkpoint conversation state"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "runtime.md#rt-rte-conversation-loop"
              note: "The notebook passes conversation message/state updates to its external checkpoint mechanism."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Conversation updates supply checkpointed messages, while framework initialization/reconstruction details are outside inspected implementation."
        -
          scope: "Initial authorship/derivation of generic caller content and remaining example/evaluator inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-graph-embeddings"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Generic caller identity and untraced inputs cannot establish authored content, initial vector provenance or an exhaustive set of derivation paths."
      records:
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "runtime.md#rt-rte-maintenance-writes"
        - "runtime.md#rt-rte-conversation-loop"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "memory.md#mem-rte-saga-summary"
        - "epistemic.md#epi-rte-entity-summary"
        - "memory.md#mem-obj-graph-metadata"
        - "epistemic.md#epi-obj-edge-episodes"
        - "memory.md#mem-obj-graph-embeddings"
        - "epistemic.md#epi-obj-edge-embedding"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-memory-saver"
      note: "Imported content, trace-extracted conversation results and other compiled derivatives have distinct local warrants. Known derivation does not resolve upstream authorship or initial embedding provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Episode/fact/summary text at extraction, resolution, summarization and notebook answer consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "runtime.md#rt-bap-facts-context"
                - "runtime.md#rt-rte-conversation-loop"
              note: "Retained descriptions supply evidence/context to extraction and summarization; fact strings supply reference context to the notebook model."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "runtime.md#rt-bap-facts-context"
            - "runtime.md#rt-rte-conversation-loop"
          note: "This names actual text consumers; exposure to an unspecified API caller is not additional behavioral activation."
        -
          scope: "Retained text and vectors at hybrid search and relevance reranking"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-graph-embeddings"
                - "runtime.md#rt-rte-context-retrieval"
              note: "Fact/name text, vector similarity and candidate passages influence which retained items are returned."
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-graph-embeddings"
            - "runtime.md#rt-rte-context-retrieval"
          note: "Ranking concerns relative retrieval priority, not truth acceptance."
        -
          scope: "Retained IDs, temporal/group selectors, memberships and saga cursor at selection/remapping consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-metadata"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
                - "epistemic.md#epi-obj-saga-watermarks"
              note: "Groups, endpoints, memberships and watermarks direct later selection and summarization windows."
          records:
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
            - "epistemic.md#epi-obj-saga-watermarks"
          note: "Code uses retained access state to choose scope, candidates and the next input window."
        -
          scope: "Retained episode references and temporal fields at deletion/date-filter consumers"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-metadata"
                - "memory.md#mem-clm-withdrawal-scope"
                - "epistemic.md#epi-rte-episode-removal"
                - "epistemic.md#epi-obj-edge-validity"
              note: "First episode references and mention counts determine deletion membership; supplied date filters exclude nonmatching retained results."
          records:
            - "memory.md#mem-obj-graph-metadata"
            - "memory.md#mem-clm-withdrawal-scope"
            - "epistemic.md#epi-rte-episode-removal"
            - "epistemic.md#epi-obj-edge-validity"
          note: "The force is conditional on invoking cleanup or a date-aware filter; no global current-truth-only enforcement is claimed."
        -
          scope: "Retained conversation episodes at automatic graph extraction and summary update"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "runtime.md#rt-rte-episode-ingestion"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
              note: "Automatically recorded experience feeds durable graph facts/descriptions that shape later model context."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-rte-episode-ingestion"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
          note: "Update-consumer force is distinct from the resulting facts’ knowledge force; no improvement or parameter training is implied."
        -
          scope: "Retained preferences/procedures at an external assistant following shipped MCP rules"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-memory-instructions"
              note: "Shipped rules tell an assistant to apply retrieved preferences and follow retrieved procedures as guidance."
          records:
            - "runtime.md#rt-bap-memory-instructions"
          note: "This is an afforded role only: host loading, tool-name mapping and compliance remain uninspected."
        -
          scope: "Retained evaluation reference results at model judge"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Reloaded baseline graph descriptions supply comparison reference to the judge."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Reference content is model-produced, not independently certified truth or production admission policy."
        -
          scope: "Checkpoint message/state at resumed notebook model"
          assessment: "partial"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "runtime.md#rt-rte-conversation-loop"
              note: "Accumulated conversation payloads are sent to the model as context."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Messages reach model context at the notebook boundary, while framework-internal selectors and effects remain uninspected."
        -
          scope: "Other included consumers, attribute-specific effects and checkpoint internals"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-maintenance-writes"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "The supplied records do not enumerate every later consumer/effect; these unresolved parts prevent a complete authority inventory."
      records:
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "runtime.md#rt-bap-facts-context"
        - "runtime.md#rt-rte-conversation-loop"
        - "memory.md#mem-obj-graph-embeddings"
        - "runtime.md#rt-rte-context-retrieval"
        - "memory.md#mem-obj-graph-metadata"
        - "memory.md#mem-rte-saga-summary"
        - "epistemic.md#epi-obj-saga-watermarks"
        - "memory.md#mem-clm-withdrawal-scope"
        - "epistemic.md#epi-rte-episode-removal"
        - "epistemic.md#epi-obj-edge-validity"
        - "runtime.md#rt-rte-episode-ingestion"
        - "runtime.md#rt-bap-memory-instructions"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-memory-saver"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Knowledge, ranking, routing, conditional enforcement, trace-update learning and afforded procedural instruction have separate consumers. No validation force is inferred from excluded static schemas; provider/host opacity is not upgraded by notebook wiring."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model/software extraction, resolution, embeddings, summary assignment and derived maintenance"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "runtime.md#rt-rte-bulk-ingestion"
                - "runtime.md#rt-rte-maintenance-writes"
                - "memory.md#mem-rte-saga-summary"
                - "epistemic.md#epi-rte-entity-summary"
                - "epistemic.md#epi-rte-attribute-extraction"
              note: "Generation, matching, truncation, field merging and persistence admit derived retained content without a shown human content-approval gate."
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "runtime.md#rt-rte-bulk-ingestion"
            - "runtime.md#rt-rte-maintenance-writes"
            - "memory.md#mem-rte-saga-summary"
            - "epistemic.md#epi-rte-entity-summary"
            - "epistemic.md#epi-rte-attribute-extraction"
          note: "A caller starts these operations; subsequent per-content admission is software/model-controlled."
        -
          scope: "Notebook post-response episode admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
              note: "Notebook code schedules mixed-origin episode content without per-response human approval."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
          note: "Scheduling is unconditional after each successful model response, including tool-call rounds, not just completed human turns."
        -
          scope: "Evaluation result export"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Graph-building results are serialized by the evaluator for later baseline reload."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Explicit evaluation invocation does not make software export a manual content decision."
        -
          scope: "Generic episode/direct object supply, explicit removal/clear and configuration of maintenance calls"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-rte-maintenance-writes"
            - "memory.md#mem-clm-withdrawal-scope"
          note: "Caller identity does not establish an explicit human decision supplying, approving, editing or replacing each retained item. Neither manual nor automatic content admission is established for this caller-controlled part."
        -
          scope: "Checkpoint admission mechanism inside MemorySaver"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Shipped code requests checkpointing, but the external framework admission mechanism was not inspected."
        -
          scope: "Remaining included example/evaluator admission alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-maintenance-writes"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "No complete per-content control inventory was retained for other shipped callers."
      records:
        - "runtime.md#rt-rte-episode-ingestion"
        - "runtime.md#rt-rte-bulk-ingestion"
        - "runtime.md#rt-rte-maintenance-writes"
        - "memory.md#mem-rte-saga-summary"
        - "epistemic.md#epi-rte-entity-summary"
        - "epistemic.md#epi-rte-attribute-extraction"
        - "runtime.md#rt-rte-conversation-loop"
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-clm-withdrawal-scope"
        - "memory.md#mem-obj-memory-saver"
      note: "Automatic derived admission and notebook recording are supported. Generic caller control, checkpoint admission internals and other shipped paths remain unresolved; no manual value is invented from explicit API invocation."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Entity/fact duplicate resolution"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "runtime.md#rt-rte-bulk-ingestion"
                - "epistemic.md#epi-rte-fact-comparison"
                - "epistemic.md#epi-rte-fact-disposition"
              note: "Resolution merges/reuses duplicate entity/fact identities and appends provenance to an existing edge."
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "runtime.md#rt-rte-bulk-ingestion"
            - "epistemic.md#epi-rte-fact-comparison"
            - "epistemic.md#epi-rte-fact-disposition"
          note: "Exact normalized fact/endpoints can reuse an edge; model comparisons also drive duplicate identity reuse."
        -
          scope: "Standing graph facts from retained episodes and summary reduction over retained descriptions"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "runtime.md#rt-rte-episode-ingestion"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
                - "epistemic.md#epi-rte-entity-summary"
              note: "Episode extraction retains standing graph claims; model summary branches, pairwise community reduction and saga folding reduce existing descriptions."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-rte-episode-ingestion"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
            - "epistemic.md#epi-rte-entity-summary"
          note: "Classification follows implemented reduction of existing content, not a proof that every generated sentence is faithful."
        -
          scope: "Existing entity attributes/summaries, communities and saga text"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
                - "epistemic.md#epi-rte-attribute-extraction"
                - "epistemic.md#epi-rte-entity-summary"
              note: "Summary assignment and typed-field merging update existing state; saga/community updates replace or extend prior descriptions."
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
            - "epistemic.md#epi-rte-attribute-extraction"
            - "epistemic.md#epi-rte-entity-summary"
          note: "Literal appending, overlay/replacement and summary updates revise existing retained entries."
        -
          scope: "Temporal fact withdrawal with historical retention"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-clm-withdrawal-scope"
                - "epistemic.md#epi-rte-fact-disposition"
              note: "Contradiction disposition withdraws current temporal reliance while retaining the old edge and its history."
          records:
            - "memory.md#mem-clm-withdrawal-scope"
            - "epistemic.md#epi-rte-fact-disposition"
          note: "Actual invalid_at/expired_at updates are supported; downstream filtering still depends on caller/recipe."
        -
          scope: "Explicit deletion, graph clear and destructive community removal"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-clm-withdrawal-scope"
                - "runtime.md#rt-rte-maintenance-writes"
                - "epistemic.md#epi-rte-episode-removal"
              note: "Physical deletion/clear removes selected retained material from future availability; no timed decay schedule is asserted."
          records:
            - "memory.md#mem-clm-withdrawal-scope"
            - "runtime.md#rt-rte-maintenance-writes"
            - "epistemic.md#epi-rte-episode-removal"
          note: "This forgets selected retained objects, not every derived summary or external checkpoint, and is not rollback."
        -
          scope: "Semantic novelty of model-generated facts, attributes and summaries"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-fact-extraction"
            - "epistemic.md#epi-rte-attribute-extraction"
            - "epistemic.md#epi-rte-entity-summary"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
          note: "Actual source/output comparisons are missing. These records do not establish a new claim absent from inputs, so synthesize is not asserted; the supported consolidation/evolution mechanisms remain."
        -
          scope: "Other included maintenance/prompt/backend variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-maintenance-writes"
            - "runtime.md#rt-rte-bulk-ingestion"
            - "memory.md#mem-obj-entity-node"
          note: "Untraced alternate transformations prevent an exhaustive operation set; no promote or additional operation is inferred from API names."
      records:
        - "runtime.md#rt-rte-episode-ingestion"
        - "runtime.md#rt-rte-bulk-ingestion"
        - "epistemic.md#epi-rte-fact-comparison"
        - "epistemic.md#epi-rte-fact-disposition"
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "memory.md#mem-rte-saga-summary"
        - "epistemic.md#epi-rte-entity-summary"
        - "epistemic.md#epi-rte-attribute-extraction"
        - "memory.md#mem-clm-withdrawal-scope"
        - "runtime.md#rt-rte-maintenance-writes"
        - "epistemic.md#epi-rte-episode-removal"
        - "epistemic.md#epi-rte-fact-extraction"
      note: "Deduplication, consolidation, evolution, historical invalidation and selected forgetting are wired. Semantic fidelity/novelty and remaining variants are unresolved; generation alone does not establish synthesis."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Library/REST/MCP query and direct retained-object returns"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-retrieval"
                - "epistemic.md#epi-rte-provenance-read"
                - "memory.md#mem-rte-saga-summary"
              note: "Search, UUID/recent-episode getters and requested saga summary responses fulfill consumer requests for retained content."
          records:
            - "runtime.md#rt-rte-context-retrieval"
            - "epistemic.md#epi-rte-provenance-read"
            - "memory.md#mem-rte-saga-summary"
          note: "A requesting caller selects retained material; returning that requested result is not another push."
        -
          scope: "Notebook graph search and automatic context assembly"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-bap-facts-context"
                - "memory.md#mem-obj-entity-edge"
              note: "Notebook/tool code explicitly requests query-selected facts from Graphiti."
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-bap-facts-context"
                - "memory.md#mem-obj-entity-edge"
              note: "At each chatbot invocation, automatic latest-message/center-node selection supplies retained user facts in the model system message."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "runtime.md#rt-bap-facts-context"
            - "memory.md#mem-obj-entity-edge"
          note: "Code requests graph facts, then supplies selected text to the model without a model request for those user facts; operations within one chain are distinct."
        -
          scope: "Prior episode/candidate and previous-summary supply inside ingestion and maintenance"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "runtime.md#rt-rte-bulk-ingestion"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-rte-saga-summary"
                - "memory.md#mem-obj-graph-metadata"
              note: "Ingestion automatically selects prior episodes/candidates; maintenance supplies retained summaries and selected episode windows to model processing."
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "runtime.md#rt-rte-bulk-ingestion"
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-rte-saga-summary"
            - "memory.md#mem-obj-graph-metadata"
          note: "The caller requests a write/update, not return of this context; internal selectors supply retained inputs to extraction or summarization consumers."
        -
          scope: "Evaluation baseline read and judge-context assembly"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Evaluation code explicitly reloads the retained baseline JSON."
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Evaluation code pairs baseline/candidate records and supplies the retained reference to the judge."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Reload and delivery to the judge are separate operations; the judge does not request a particular baseline object."
        -
          scope: "Checkpoint resumption and delivery of accumulated messages"
          assessment: "partial"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "runtime.md#rt-rte-conversation-loop"
              note: "At chatbot invocation, accumulated state messages accompany the system message without a separate model request."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Notebook code sends accumulated messages to the model; the external framework’s reload/selection operations are not inspected."
        -
          scope: "Other included example/consumer and checkpoint read-back alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-context-retrieval"
            - "runtime.md#rt-rte-maintenance-writes"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Existing request-driven graph returns do not close every later-consumer delivery path."
      records:
        - "runtime.md#rt-rte-context-retrieval"
        - "epistemic.md#epi-rte-provenance-read"
        - "memory.md#mem-rte-saga-summary"
        - "runtime.md#rt-rte-conversation-loop"
        - "runtime.md#rt-bap-facts-context"
        - "memory.md#mem-obj-entity-edge"
        - "runtime.md#rt-rte-episode-ingestion"
        - "runtime.md#rt-rte-bulk-ingestion"
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-graph-metadata"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-memory-saver"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Pull applies to requested graph/file reads; push applies to automatic context supply to a later model/update/judge consumer. This does not claim an independent unsolicited service notification or successful model activation. Unresolved alternatives prevent pull-only or exhaustive-direction conclusions."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Notebook user-fact context push"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-rte-context-retrieval"
                - "runtime.md#rt-bap-facts-context"
              note: "Hybrid fact search uses query/fulltext relevance to select retained facts."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-rte-context-retrieval"
                - "runtime.md#rt-bap-facts-context"
              note: "Semantic query similarity participates in hybrid fact selection."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "runtime.md#rt-rte-context-retrieval"
                - "runtime.md#rt-bap-facts-context"
              note: "The retained user center-node identity affects graph-distance selection of delivered facts, not merely a catalog label."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "runtime.md#rt-rte-context-retrieval"
            - "runtime.md#rt-bap-facts-context"
          note: "Trigger is chatbot invocation; latest message text and user center node select up to five edge.fact strings delivered in a system message."
        -
          scope: "Prior episode selection for extraction"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-graph-metadata"
              note: "Time/type/group/window filters select available recent episode context."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-graph-metadata"
              note: "Explicit previous episode UUIDs select delivered prior episodes by identity."
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-graph-metadata"
          note: "Trigger is ingestion. Time/source/group/saga and last_n select retained prior episode text; explicit prior UUIDs can replace temporal selection."
        -
          scope: "Graph candidate selection for extraction/resolution"
          assessment: "partial"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "runtime.md#rt-rte-context-retrieval"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-graph-embeddings"
              note: "Name/fact text matching and fulltext query selectors select retained candidates."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-episode-ingestion"
                - "runtime.md#rt-rte-context-retrieval"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "memory.md#mem-obj-graph-embeddings"
              note: "Persisted vectors influence semantic candidate selection."
          records:
            - "runtime.md#rt-rte-episode-ingestion"
            - "runtime.md#rt-rte-context-retrieval"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "memory.md#mem-obj-graph-embeddings"
          note: "Ingestion triggers candidate searches supplying retained entity descriptions and fact text to extraction/resolution consumers. Lexical and embedding selection are supported; subsequent identity/semantic judgments concern reuse and temporal disposition, not selection for push delivery. Optional cross-encoder search is not established on this ingestion push, and alternate recipes/provider selectors remain unresolved."
        -
          scope: "Saga summary and linked episode push to summarizer"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saga-summary"
                - "memory.md#mem-obj-saga-node"
                - "epistemic.md#epi-obj-saga-watermarks"
              note: "Saga identity and linked episode membership target the retained content supplied to summarization."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saga-summary"
                - "memory.md#mem-obj-saga-node"
                - "epistemic.md#epi-obj-saga-watermarks"
              note: "Created-time eligibility, oldest-first count and prompt budgets filter the delivered episode window."
          records:
            - "memory.md#mem-rte-saga-summary"
            - "memory.md#mem-obj-saga-node"
            - "epistemic.md#epi-obj-saga-watermarks"
          note: "Trigger is summarize_saga. Saga UUID/membership selects the retained summary/linked episodes; ingestion cursor, count and text/byte budgets bound the submitted window."
        -
          scope: "Entity/community retained-summary update inputs"
          assessment: "partial"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "epistemic.md#epi-rte-entity-summary"
              note: "Entity identity/name and membership associations target existing summaries for update."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "epistemic.md#epi-rte-entity-summary"
              note: "Size thresholds, callback eligibility and clustering bound which descriptions enter summary processing."
          records:
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "epistemic.md#epi-rte-entity-summary"
          note: "Trigger is an update/rebuild. Matching node names and community memberships identify inputs; not all cluster or callback variants are inspected."
        -
          scope: "Evaluation baseline push to judge"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Dataset/session limits and positional pairing select the retained comparison reference."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Trigger is candidate evaluation; selected dataset prefix and corresponding positional zip select retained baseline results for the judge, not authenticated identity matching."
        -
          scope: "Checkpoint message context push"
          assessment: "partial"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-saver"
                - "runtime.md#rt-rte-conversation-loop"
              note: "The configured thread ID selects the resumed conversation whose accumulated messages reach the model."
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Trigger is chatbot invocation; thread key selects conversation state at the notebook boundary; exact MemorySaver payload selection is opaque."
        -
          scope: "Remaining included selector recipes and consumer alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-retrieval"
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-maintenance-writes"
          note: "Other example routes, framework internals and all backend search variants remain untraced; known signals do not classify opaque alternatives."
      records:
        - "runtime.md#rt-rte-conversation-loop"
        - "runtime.md#rt-rte-context-retrieval"
        - "runtime.md#rt-bap-facts-context"
        - "runtime.md#rt-rte-episode-ingestion"
        - "memory.md#mem-obj-episodic-node"
        - "memory.md#mem-obj-graph-metadata"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "memory.md#mem-obj-graph-embeddings"
        - "memory.md#mem-rte-saga-summary"
        - "memory.md#mem-obj-saga-node"
        - "epistemic.md#epi-obj-saga-watermarks"
        - "memory.md#mem-obj-community-node"
        - "epistemic.md#epi-rte-entity-summary"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-memory-saver"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Signals describe automatic context selection, not every requested return. Each unit identifies its trigger, selector input and delivered retained part; direction uncertainty prevents a global inapplicable judgment."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Notebook automatic mixed-origin episode-to-graph-to-later-model chain"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "runtime.md#rt-rte-episode-ingestion"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-entity-edge"
                - "runtime.md#rt-bap-facts-context"
              note: "Automatic trace-fed graph extraction produces durable behavior-shaping knowledge for later model context; no parameter update or improved capacity is required."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-rte-episode-ingestion"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-entity-edge"
            - "runtime.md#rt-bap-facts-context"
          note: "The chain records latest human/tool/model state plus response, produces retained graph claims and later supplies selected facts to the conversational model. Scheduling/persistence success and benefit remain unobserved."
        -
          scope: "Evaluation dataset session processing into retained baseline/candidate graph"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
                - "runtime.md#rt-rte-episode-ingestion"
              note: "Trace-fed graph production retains derived descriptions consumed by a later model judgment."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
            - "runtime.md#rt-rte-episode-ingestion"
          note: "Recorded session messages feed automatic graph construction; retained descriptions later shape judge context, not automatic installation of a production winner."
        -
          scope: "Saga/entity/community summaries from generic caller episodes and retained descriptions"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
              note: "For the recorded notebook-session branch, derived descriptions can be updated from retained trace-fed facts and shape later extraction/summarization context."
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
          note: "Automatic transformations and later consumers are supported, but whether every original episode is an activity trace is unresolved."
        -
          scope: "Raw checkpoint-only retention"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-conversation-loop"
          note: "Recorded messages are retained and supplied as context, but external checkpoint internals establish no derived behavior-shaping update. Raw retention alone does not justify yes, and no bounded absence search warrants no."
        -
          scope: "Generic direct content writes and untraced shipped example/evaluator transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-maintenance-writes"
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Trace provenance and admission mechanisms are unresolved across remaining included paths; no system-wide no or complete qualifying-route enumeration is supported."
      records:
        - "runtime.md#rt-rte-conversation-loop"
        - "memory.md#mem-obj-episodic-node"
        - "runtime.md#rt-rte-episode-ingestion"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-entity-edge"
        - "runtime.md#rt-bap-facts-context"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "memory.md#mem-rte-saga-summary"
        - "memory.md#mem-obj-memory-saver"
        - "runtime.md#rt-rte-maintenance-writes"
      note: "Wired yes witnesses cover conversation-derived graph memory and dataset-session graph results, not exercised or beneficial learning. Generic origins, checkpoint transformation and other shipped paths keep axis coverage partial."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Notebook conversation graph-learning route"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "runtime.md#rt-bap-facts-context"
              note: "Recorded human/model conversational messages and newly generated model response content feed episode extraction."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "runtime.md#rt-bap-facts-context"
              note: "Post-tool latest messages record tool results, potentially retrieved graph facts, and feed the same automatic episode route."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
            - "runtime.md#rt-bap-facts-context"
          note: "Original content, not its unconditional user-name prefix, determines the source. No linked state/action/outcome trajectory is established."
        -
          scope: "Evaluation graph-learning route"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph-results"
                - "runtime.md#rt-rte-evaluation-comparison"
              note: "Recorded dataset session messages feed automatic graph construction before later baseline/candidate model consumption."
          records:
            - "memory.md#mem-obj-graph-results"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "The selected dataset contains multi-session messages; JSON graph exports are derived outputs, not the original source class."
        -
          scope: "Summary updates over the notebook-derived branch"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
              note: "Conversation-origin facts and retained episodes feed later summary production."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-loop"
                - "memory.md#mem-obj-episodic-node"
                - "memory.md#mem-obj-entity-node"
                - "memory.md#mem-obj-community-node"
                - "memory.md#mem-obj-saga-node"
                - "memory.md#mem-rte-saga-summary"
              note: "Tool-result-origin facts/episodes can feed later descriptions through the same retained graph path."
          records:
            - "runtime.md#rt-rte-conversation-loop"
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-entity-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "memory.md#mem-rte-saga-summary"
          note: "This unit only includes descriptions derived from the established notebook feed, not every caller episode."
        -
          scope: "Other qualifying possibilities in generic episodes, saga inputs and shipped examples"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-episodic-node"
            - "memory.md#mem-obj-community-node"
            - "memory.md#mem-obj-saga-node"
            - "runtime.md#rt-rte-maintenance-writes"
          note: "Generic source enums, timestamps and source descriptions do not establish original activity content. Remaining included example origins were not traced enough to assert event-streams, trajectories or complete source coverage."
        -
          scope: "Unresolved checkpoint and other evaluator trace-fed writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-memory-saver"
            - "runtime.md#rt-rte-evaluation-comparison"
          note: "Qualifying derived writes and their original inputs remain incompletely assessed; supported session/tool routes do not make alternatives inapplicable."
      records:
        - "runtime.md#rt-rte-conversation-loop"
        - "memory.md#mem-obj-episodic-node"
        - "runtime.md#rt-bap-facts-context"
        - "memory.md#mem-obj-graph-results"
        - "runtime.md#rt-rte-evaluation-comparison"
        - "memory.md#mem-obj-entity-node"
        - "memory.md#mem-obj-community-node"
        - "memory.md#mem-obj-saga-node"
        - "memory.md#mem-rte-saga-summary"
        - "runtime.md#rt-rte-maintenance-writes"
        - "memory.md#mem-obj-memory-saver"
      note: "Session logs and tool traces are positively supported on named routes. Adapter labeling does not add event-streams; unresolved original inputs and qualifying writes prevent a complete source inventory."
---

# Graphiti memory profile

## Comparison rationale

This comparison classifies accepted records, not fresh source evidence. All positive implementation findings are wired unless the unit explicitly identifies the afforded MCP assistant role. No observed or causal finding is available. Partial coverage is not weakened evidence: it names retained parts and alternatives whose inventory, admission, origin or consumer remains unresolved.

### Canonical identities and retained parts

Reconciliation supersedes the epistemic episode, entity, community and saga containers with [MEM-OBJ-episodic-node](memory.md#mem-obj-episodic-node), [MEM-OBJ-entity-node](memory.md#mem-obj-entity-node), [MEM-OBJ-community-node](memory.md#mem-obj-community-node) and [MEM-OBJ-saga-node](memory.md#mem-obj-saga-node). The profile cites these canonical containers. Epistemic attribute, summary and watermark parts remain separately usable; the broader edge/metadata/vector containers have different extents and were not superseded. Those retained parts supply the form, authority and lineage distinctions rather than an extra storage substrate.

Dense graph vectors are parametric encodings on graph storage, not graph-owned model weights. Inference-generated vectors support other-compiled lineage locally, while [MEM-OBJ-graph-embeddings](memory.md#mem-obj-graph-embeddings) leaves initial caller vectors and community variants unresolved. Readable MCP/evaluation displays omit vectors and cannot stand in for the numerical search payload.

### Direction and consumer force

A request-driven overall workflow can contain a push to a later consumer. [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval) returns material explicitly requested by library/service callers: that is pull. In [RT-RTE-conversation-loop](runtime.md#rt-rte-conversation-loop), notebook code requests facts, then automatically selects and inserts retained user facts into the model's system message. The model did not request those facts: this downstream operation is push. This distinction does not invent an unsolicited Graphiti service notification. Similarly, a write request triggers automatic prior-episode/candidate supply to extraction, and a saga update supplies previous text and cursor-selected episodes to a summarizer. Requested API delivery is not counted again as push.

Push signals retain actual selected parts. User/product center identities affect graph-distance selection; prior episode UUIDs replace temporal selection; saga identity/membership and cursor select its next episode window. Budget/count/time filtering is coarse even alongside identity selection. The ingestion push retains lexical and embedding signals, but no inferred-judgment finding. [EPI-RTE-fact-comparison](epistemic.md#epi-rte-fact-comparison) and [EPI-RTE-fact-disposition](epistemic.md#epi-rte-fact-disposition) establish judgments consumed for identity reuse and temporal disposition after candidate retrieval, not a judgment selector choosing retained parts for downstream push delivery. Optional cross-encoder capability in [RT-RTE-context-retrieval](runtime.md#rt-rte-context-retrieval) does not establish its use on this ingestion path. The unsupported judgment-signal finding is withdrawn; the wired semantic reconciliation mechanisms remain unchanged.

Authority is local to a consumer. Fact strings give the answering model knowledge; fact/name text and vectors give search ranking input; retained groups/cursors route selection; cleanup predicates and invoked date filters enforce exclusions. Automatically retained conversational experience gives the graph-update consumer learning input without granting factual truth. [RT-BAP-memory-instructions](runtime.md#rt-bap-memory-instructions) affords stronger instruction force for retrieved preferences/procedures only at an external host following those rules. Host loading, tool-name mapping and compliance are not wired by the service. Static rules and response schemas are outside the accumulated-memory inventory, so their enforcement/validation is not attributed to retained graph content.

### Curation and trace sources

Extraction of standing facts from retained episodes, summary reduction and saga folding support consolidation. Literal summary append and typed overlays/replacements support evolution; duplicate reuse supports deduplication. Model-generated descriptions do not by themselves prove synthesis of a claim absent from inputs. The semantic alternatives remain unresolved in [EPI-RTE-fact-extraction](epistemic.md#epi-rte-fact-extraction) and [EPI-RTE-entity-summary](epistemic.md#epi-rte-entity-summary), without negating the implemented reduction/update operations. Temporal invalidation retains history; physical deletion/clear forget selected content. Neither establishes complete retraction from summaries, checkpoint state or already delivered context; see [MEM-CLM-withdrawal-scope](memory.md#mem-clm-withdrawal-scope).

The notebook's qualifying graph-learning chain is automatic trace admission, extraction into durable descriptions and later retrieval into model context. It can consume human/model conversation and tool-result material, including recirculated facts. Its user-name prefix cannot make all inputs human session turns. Session-logs and tool-traces therefore remain separate positive source findings. No event-stream value follows merely from timestamps or message-source typing, and no trajectories value follows merely from a multi-step tool loop. The evaluation route also automatically derives retained graph results from recorded sessions for later model judgment; this is not an automatic production-successor installation or improved capacity claim.

[MEM-OBJ-episodic-node](memory.md#mem-obj-episodic-node) distinguishes single-path raw suppression from unchanged-content bulk writes. Bulk inputs can therefore remain available to later extraction and saga consumption even when single ingestion would suppress text. [MEM-RTE-saga-summary](memory.md#mem-rte-saga-summary) establishes recurrence but retains bounded selection/truncation and cursor limits; no losslessness is inferred. Generic callers, other example origins, checkpoint internals and remaining backend/consumer variants prevent system-complete trace-source, admission and authority conclusions. No local or global trace-learning no is invented without bounded absence records.

### Source-read log and checks

No frozen-source reread was needed. This member uses only the supplied accepted reports and reconciliation; it declares no records, quotes or new evidence. Structural validation checks the classification form and record references, not semantic completeness or observed operation.
