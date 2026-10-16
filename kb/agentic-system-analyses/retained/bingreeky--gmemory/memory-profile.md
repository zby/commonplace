---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "GMemory memory comparison: task documents, query graph, reusable rules and temporal histories at the frozen revision."
run-id: "AAS-2026-10-15-gmemory-a2192cc823f7-01"
source-identity: "https://github.com/bingreeky/GMemory"
reviewed-boundary: "7b581c51d993bd600df14691d101d7e601040cc6"
memory-comparison:
  version: 2
  scope: "Included: accumulated task payloads and interaction graphs, Chroma task access vectors, persisted task-query graph, rule text and association/survival metadata, automatic extraction/revision/merge and their later consumers, MacNet cross-task temporal histories, unresolved initialization and opaque provider retention. Excluded: comparator memories, shipped static instructions/examples as such, ordinary untransformed current-task accumulation, model weights with no evidenced use-driven update, and benchmark/provider dependency internals beyond the recorded opaque-state limits."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Task text, extras and interaction graphs in current objects and Chroma documents"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "memory.md#mem-obj-state-chain"
              note: "Current and copied task objects hold text and structured states."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "runtime.md#rt-cmp-embedding-func"
              note: "Chroma retains task documents with embedding-supported access; no underlying SQL engine is classified."
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-state-chain"
            - "runtime.md#rt-cmp-embedding-func"
          note: "Text metadata and serialized interaction graphs are parts of one retained task document; JSON encoding alone does not establish a file substrate."
        - scope: "Task-query access graph"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
              note: "NetworkX task nodes and weighted edges are operative access structure."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
              note: "The graph is persisted and reloaded as task_layer_graph.pkl."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
              note: "The loaded graph is a process object."
          records:
            - "memory.md#mem-obj-task-layer"
          note: "Covers query graph, not interaction-graph JSON or a hypothetical insight-edge graph."
        - scope: "Rule text and access/survival metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "memory.md#mem-obj-insights-metadata"
              note: "insights.json persists current rule dictionaries."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "memory.md#mem-obj-insights-metadata"
              note: "Loaded dictionaries supply rule and metadata consumers."
          records:
            - "memory.md#mem-obj-insights-rule"
            - "memory.md#mem-obj-insights-metadata"
          note: "Current JSON and in-process list are evidenced; no version archive is inferred."
        - scope: "MacNet temporal input/output histories"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Reused Node objects retain appended history across task boundaries when temporal edges are used."
          records:
            - "memory.md#mem-obj-node-memory"
          note: "No restart checkpoint is established for these lists."
        - scope: "Opaque endpoint retention and any provider-side memory substrate"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "memory.md#mem-obj-mas-message"
        - "memory.md#mem-obj-state-chain"
        - "runtime.md#rt-cmp-embedding-func"
        - "memory.md#mem-obj-task-layer"
        - "memory.md#mem-obj-insights-rule"
        - "memory.md#mem-obj-insights-metadata"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Positive units cover task documents, access graph, rules and temporal history. Hidden endpoint retention remains unresolved; dependency internals do not justify sqlite or rdbms values."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Task descriptions, action/observation text, extracted key steps and failure diagnosis at model and formatter consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "runtime.md#rt-rte-task-retention"
              note: "Models interpret trajectory text and derived extras."
          records:
            - "memory.md#mem-obj-mas-message"
            - "runtime.md#rt-rte-task-retention"
          note: "Includes readable derived content, not the symbolic wrapper."
        - scope: "Interaction graph nodes/edges, task labels, task-query graph and rule metadata at fixed-code consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-state-chain"
                - "memory.md#mem-obj-task-layer"
                - "memory.md#mem-obj-insights-metadata"
              note: "Code interprets graph structure, labels, associations and scalar survival scores by fixed rules."
          records:
            - "memory.md#mem-obj-state-chain"
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-metadata"
          note: "Numerical graph weights and scalar scores are localized algorithm inputs, not learned weights."
        - scope: "Task-index dense embeddings at similarity consumers"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embedding-func"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Dense distributed numerical representations support task similarity selection."
          records:
            - "runtime.md#rt-cmp-embedding-func"
            - "runtime.md#rt-rte-memory-delivery"
          note: "The encoder component is distinct from its retained task-index vectors; model acquisition provenance remains unresolved."
        - scope: "Rule strings at maintenance, projection and solving consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "runtime.md#rt-bap-retained-guidance"
              note: "Rule meaning is interpreted by models; advisory delivery is not executable enforcement."
          records:
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-bap-retained-guidance"
          note: "Covers persisted rule text and its downstream textual consumption, not metadata."
        - scope: "MacNet retained outputs and ordered history at temporal forwarding"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Later nodes interpret predecessor output strings."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Ordered history and predecessor links determine which latest string is forwarded."
          records:
            - "memory.md#mem-obj-node-memory"
          note: "Separates interpreted content from fixed selection structure."
        - scope: "Opaque endpoint retention and any provider-side memory form"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "memory.md#mem-obj-mas-message"
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-state-chain"
        - "memory.md#mem-obj-task-layer"
        - "memory.md#mem-obj-insights-metadata"
        - "runtime.md#rt-cmp-embedding-func"
        - "runtime.md#rt-rte-memory-delivery"
        - "memory.md#mem-obj-insights-rule"
        - "runtime.md#rt-bap-retained-guidance"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Mixed text, structure and dense vectors remain separate operative paths; opaque provider accumulation prevents complete coverage."
    lineage:
      assessment: "partial"
      units:
        - scope: "Task payload acquisition and automatic derivation"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
              note: "Dataset/environment descriptions and observations enter retained task payloads."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "runtime.md#rt-rte-task-retention"
              note: "Recorded task activity is reconstructed and used to generate cleaned trajectory, key steps and failure explanations."
          records:
            - "memory.md#mem-obj-mas-message"
            - "runtime.md#rt-rte-task-retention"
          note: "These paths coexist inside the payload; initial Chroma content and external edits are not covered by these positives."
        - scope: "Task-query graph and rule association/survival metadata generated by code"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
                - "memory.md#mem-obj-insights-metadata"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "Software derives task edges, clusters, scores and associations from documents and update outcomes."
          records:
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-metadata"
            - "runtime.md#rt-rte-insight-maintenance"
          note: "Classifies subsequent construction, not provenance of a preexisting pickle or JSON file."
        - scope: "Subsequent rule generation and revision from task experience"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "Success summaries and comparative task traces feed reusable rules."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "memory.md#mem-rte-cluster-merge"
              note: "Cluster merging derives replacement rules from previously retained rules."
          records:
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-rte-cluster-merge"
          note: "Model authorship is not explicit human authorship; derived paths do not identify preexisting rule origins."
        - scope: "MacNet temporal histories"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Scheduler appends prior node invocation inputs and outputs for later forwarding."
          records:
            - "memory.md#mem-obj-node-memory"
          note: "The stored strings originate in workflow activity; this does not alone establish durable trace learning."
        - scope: "Initial Chroma, pickle and JSON content and external replacement provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-rule"
          note: "Existing store authorship and approval are uninspected; neither authored nor imported is assigned merely from loading a file."
        - scope: "Task-index embedding provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-embedding-func"
            - "runtime.md#rt-rte-memory-delivery"
          note: "The named encoder is not revision pinned, and existing vector generation provenance is uninspected; complete lineage cannot be established."
        - scope: "Opaque endpoint retention and any provider-side memory lineage"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "memory.md#mem-obj-mas-message"
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-task-layer"
        - "memory.md#mem-obj-insights-metadata"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-rule"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-cmp-embedding-func"
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Known subsequent derivations coexist with unresolved initial content, vector provenance and endpoint state. Imported static prompt bodies are excluded except where actually recorded into task payloads."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Readable successful examples and rule advice at solving agents"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "memory.md#mem-obj-insights-rule"
                - "runtime.md#rt-bap-retained-guidance"
              note: "Examples and advisory rules supply reference/context through user messages, not standing host directives or action vetoes."
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-bap-retained-guidance"
          note: "No instruction value is inferred from the word rule; actual consumption is advisory."
        - scope: "Task experience and existing rules at rule-update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-mas-message"
                - "memory.md#mem-obj-insights-rule"
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-rte-cluster-merge"
              note: "Retained experience and rules feed durable revision of later behavior-shaping guidance."
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-rte-cluster-merge"
          note: "Update authority is separate from downstream advice and does not establish improved capacity."
        - scope: "Task names/vectors, query graph and positive rule associations at selectors"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
                - "memory.md#mem-obj-insights-metadata"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Similarity, model relevance and association counts influence priority."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Task-query graph neighborhoods determine candidate scope."
          records:
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-metadata"
            - "runtime.md#rt-rte-memory-delivery"
          note: "Survival scalar is not the rule relevance score; negative associations are not subtracted by the selector."
        - scope: "Retained rule scores at survival pruning"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-metadata"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "Only positive-score rules survive clear_insights."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-metadata"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "The retained score supplies the admissibility criterion checked by pruning."
          records:
            - "memory.md#mem-obj-insights-metadata"
            - "runtime.md#rt-rte-insight-maintenance"
          note: "This criterion controls survival, not semantic truth or action correctness."
        - scope: "Existing retained rule strings at duplicate rejection"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "epistemic.md#epi-rte-rule-disposition"
              note: "Existing strings supply the substring duplicate criterion for ordinary operation admission."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "epistemic.md#epi-rte-rule-disposition"
              note: "Duplicate checks can reject proposed additions through the ordinary operation path."
          records:
            - "memory.md#mem-obj-insights-rule"
            - "epistemic.md#epi-rte-rule-disposition"
          note: "Merge is a different gate; AGREE targeting is not guaranteed by numeric checks."
        - scope: "MacNet temporal predecessor outputs at later nodes"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Latest prior outputs supply natural-language upstream context, not an action filter."
          records:
            - "memory.md#mem-obj-node-memory"
          note: "Archived inputs not selected by that getter have no evidenced downstream authority."
        - scope: "Opaque endpoint retention and any provider-side memory authority"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "memory.md#mem-obj-mas-message"
        - "memory.md#mem-obj-insights-rule"
        - "runtime.md#rt-bap-retained-guidance"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-task-layer"
        - "memory.md#mem-obj-insights-metadata"
        - "runtime.md#rt-rte-memory-delivery"
        - "epistemic.md#epi-rte-rule-disposition"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Authority is classified per actual consumer: learning, advice, selection and survival differ. Unconsumed metadata receives no force; hidden provider effects remain uninspected."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Normal task capture, extraction and graph/index construction"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-retention"
                - "memory.md#mem-obj-task-layer"
              note: "Schedulers and memory code admit task activity and derived content without per-item operator approval."
          records:
            - "runtime.md#rt-rte-task-retention"
            - "memory.md#mem-obj-task-layer"
          note: "Launch/configuration does not make subsequent content admission manual."
        - scope: "Ordinary rule operations, score updates and pruning"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-obj-insights-metadata"
              note: "Software triggers model proposals and admits changes through parser/update code."
          records:
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-obj-insights-metadata"
          note: "Model authorship and software admission are distinct from human approval."
        - scope: "Cluster merge replacement"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cluster-merge"
              note: "Code clears and rebuilds the rule list from parsed model output."
          records:
            - "memory.md#mem-rte-cluster-merge"
          note: "The separate numbered-list gate also has no per-content human veto."
        - scope: "MacNet temporal appends"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Workflow appends inputs and outputs without semantic approval."
          records:
            - "memory.md#mem-obj-node-memory"
          note: "No task-success admission condition governs these appends."
        - scope: "Preexisting stores and external replacement admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-rule"
          note: "Loading existing Chroma/pickle/JSON identifies neither a human decision nor software admission of that initial content. Manual cannot be inferred."
        - scope: "Opaque endpoint retention and any provider-side memory admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-task-layer"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-metadata"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-node-memory"
        - "memory.md#mem-obj-mas-message"
        - "memory.md#mem-obj-insights-rule"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "All inspected normal writes are automatic; initialization and external replacement control remain unresolved. No manual write witness is supplied."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Model key-step extraction from retained task activity"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-task-retention"
                - "memory.md#mem-obj-mas-message"
              note: "The wired extraction consumer requests condensed salient steps; semantic compression by the opaque model is afforded, not verified."
          records:
            - "runtime.md#rt-rte-task-retention"
            - "memory.md#mem-obj-mas-message"
          note: "Digit erasure and failed reward pruning do not prove faithful compression. No synthesized new proposition is established."
        - scope: "Ordinary existing-rule text replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-rule"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "EDIT replaces an existing retained rule string in place."
          records:
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-rte-insight-maintenance"
          note: "Actual semantic quality and particular output content remain unobserved."
        - scope: "Score decrements and positive-score pruning"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-metadata"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "REMOVE and negative backward credit downweight survival and can physically forget nonpositive-score rules."
          records:
            - "memory.md#mem-obj-insights-metadata"
            - "runtime.md#rt-rte-insight-maintenance"
          note: "Removal need not be immediate. This is not history-preserving invalidation or relevance-score ranking."
        - scope: "Cluster-based model merge"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-cluster-merge"
              note: "Selected retained rule batches are supplied for reduced input-based guidance; faithful semantic combination remains afforded."
          records:
            - "memory.md#mem-rte-cluster-merge"
          note: "Clear/rebuild and metadata reset are wired. No accepted output proves synthesis, near-duplicate removal or preservation."
        - scope: "Semantic novelty of generalized guidance and projected variants"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-insights-rule"
            - "runtime.md#rt-rte-insight-maintenance"
            - "epistemic.md#epi-obj-projected-insights"
          note: "Accepted records leave semantic relations indeterminate. Requested generality does not establish synthesize; substring admission checks do not themselves merge or remove retained near duplicates."
        - scope: "Opaque endpoint retention and any provider-side memory curation"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-mas-message"
        - "memory.md#mem-obj-insights-rule"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-metadata"
        - "memory.md#mem-rte-cluster-merge"
        - "epistemic.md#epi-obj-projected-insights"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Text replacement and survival downweighting are wired; model consolidation is a distinct affordance. No promote, invalidate, dedup or synthesize value is established by route names or requests alone."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Task-start retrieval request through returned examples/rules and optional projection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-delivery"
                - "runtime.md#rt-bap-retained-guidance"
              note: "The schedule requests task-conditioned retained material; formatting that requested result is not a second push."
          records:
            - "runtime.md#rt-rte-memory-delivery"
            - "runtime.md#rt-bap-retained-guidance"
          note: "Covers all three shipped solving schedules; failed example returns are discarded."
        - scope: "Count-triggered maintenance selection of retained tasks and existing rules"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-rte-cluster-merge"
              note: "Automatic count thresholds sample retained experience and supply selected tasks/rules to update consumers without their requesting those items."
          records:
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-rte-cluster-merge"
          note: "Ordinary synthesis/comparison and cluster merge are later model consumers distinct from task-query return."
        - scope: "MacNet temporal predecessor delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
                - "runtime.md#rt-rte-macnet-actions"
              note: "Graph traversal automatically supplies latest retained predecessor outputs to later node calls."
          records:
            - "memory.md#mem-obj-node-memory"
            - "runtime.md#rt-rte-macnet-actions"
          note: "Conditional on temporal edges and nonempty history; ordinary current-step accumulation is not counted as persistent task retrieval."
        - scope: "Opaque endpoint retention and any provider-side memory read-back"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-bap-retained-guidance"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-rte-macnet-actions"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Pull at solving retrieval coexists with automatic maintenance and temporal delivery. Provider hidden later-consumer paths remain uninspected."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Maintenance sampled-task selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
              note: "Saved-task count triggers sampling of five points and associated experience."
            - value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-layer"
                - "runtime.md#rt-rte-insight-maintenance"
              note: "Nearby tasks and task-name embedding clusters determine maintenance inputs."
          records:
            - "memory.md#mem-obj-task-layer"
            - "runtime.md#rt-rte-insight-maintenance"
          note: "Trigger is saved task count; inputs are sampled stored tasks/task names; selected parts are task records or rule batches. Opaque FINCH/model behavior does not become observed selection."
        - scope: "Maintenance related-rule selection"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insights-metadata"
                - "memory.md#mem-rte-cluster-merge"
              note: "Positive task-name association membership selects retained rules for related tasks/clusters."
          records:
            - "memory.md#mem-obj-insights-metadata"
            - "memory.md#mem-rte-cluster-merge"
          note: "Actual task-name matches select rule text; names are not merely catalog labels."
        - scope: "MacNet latest temporal predecessor context"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
                - "runtime.md#rt-rte-macnet-actions"
              note: "Temporal predecessor identity selects whose stored output is delivered."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-memory"
              note: "Nonempty history and latest-position choice select one output per predecessor."
          records:
            - "memory.md#mem-obj-node-memory"
            - "runtime.md#rt-rte-macnet-actions"
          note: "Trigger is node execution; inputs are predecessor links/history; selected part is the latest retained output, not archived inputs."
        - scope: "Task-query pull chain"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-memory-delivery"
          note: "Push-signal classification is inapplicable to this fully identified request/return operation. Task embedding and model reranking here are pull selectors, not extra push signals."
        - scope: "Opaque endpoint retention and any provider-side memory push selection"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "memory.md#mem-obj-task-layer"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-metadata"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-rte-macnet-actions"
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Signals classify only actual push operations. Pull relevance judgments are not counted; unresolved provider delivery prevents globally inapplicable or complete signal coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic task-derived extras retained for later prompts and update consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-retention"
                - "memory.md#mem-obj-mas-message"
              note: "Recorded actions and outcomes feed automatic key-step/diagnosis writes retained in Chroma and consumed by later solving or rule generation."
          records:
            - "runtime.md#rt-rte-task-retention"
            - "memory.md#mem-obj-mas-message"
          note: "Durable derived context qualifies without observed improvement; raw graph retention alone is not the warrant."
        - scope: "Automatic rule generation, ordinary revisions and cluster replacement"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-obj-insights-rule"
                - "memory.md#mem-rte-cluster-merge"
              note: "Experience-derived inputs produce durable reusable rule artifacts supplied to later maintenance and solving."
          records:
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-obj-insights-rule"
            - "memory.md#mem-rte-cluster-merge"
          note: "Merge consumes trace-derived rules indirectly; this is text/data revision, not weight training."
        - scope: "MacNet temporal history as qualifying durable learned artifact"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-node-memory"
          note: "In-process append/forward is established, but no restart checkpoint or durable transformed artifact is established. This is not a system-wide no."
        - scope: "Externally initialized content and replacement route"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-task-layer"
            - "memory.md#mem-obj-insights-rule"
          note: "Original input, admission control and qualifying trace-to-artifact chain of existing stores are uninspected."
        - scope: "Opaque endpoint retention and any provider-side memory trace-fed writes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-mas-message"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-rule"
        - "memory.md#mem-rte-cluster-merge"
        - "memory.md#mem-obj-node-memory"
        - "memory.md#mem-obj-task-layer"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "The inspected durable task-derived and rule routes support yes. Other routes remain local unknowns; fixed client-side model wrappers do not establish a system-wide no."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Task-derived key steps and failure diagnosis"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-retention"
                - "memory.md#mem-obj-mas-message"
              note: "Linked task actions, observations, rewards and final outcomes feed extraction and diagnosis."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-retention"
                - "memory.md#mem-obj-mas-message"
              note: "Executed environment action requests and returned observations/rewards supply execution feedback within those trajectories."
          records:
            - "runtime.md#rt-rte-task-retention"
            - "memory.md#mem-obj-mas-message"
          note: "Dataset descriptions are mixed imported context, not an additional trace category. Stored AgentMessage prompts do not establish session-log consumption by the derived-text generator."
        - scope: "Reusable rule generation and later revisions"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-obj-insights-rule"
              note: "Success key steps and comparative success/failure trajectories retain the origin in multi-step task experience."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-insight-maintenance"
                - "memory.md#mem-obj-mas-message"
              note: "Comparative detailed trajectories and failure diagnosis originate in executed environment actions and feedback."
          records:
            - "runtime.md#rt-rte-insight-maintenance"
            - "memory.md#mem-obj-insights-rule"
            - "memory.md#mem-obj-mas-message"
          note: "Merge inherits trace origins through rules rather than consuming new raw sessions; provenance of any initial rules is unresolved."
        - scope: "MacNet temporal append route"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-node-memory"
          note: "A qualifying durable learning route is not established for these lists, so source classification is not determined rather than globally inapplicable."
        - scope: "Initial store contributions to qualifying writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-mas-message"
            - "memory.md#mem-obj-insights-rule"
          note: "Initial records/rules can enter maintenance, but their original input and trace provenance are uninspected; no session-logs or event-streams value is inferred from serialization."
        - scope: "Opaque endpoint retention and any provider-side memory trace sources"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-gpt-chat"
          note: "Provider hidden retention and changes are uninspected. The client model-name string is not evidence of accumulated provider memory; no controlled value or absence is inferred."
      records:
        - "runtime.md#rt-rte-task-retention"
        - "memory.md#mem-obj-mas-message"
        - "runtime.md#rt-rte-insight-maintenance"
        - "memory.md#mem-obj-insights-rule"
        - "memory.md#mem-obj-node-memory"
        - "runtime.md#rt-cmp-gpt-chat"
      note: "Recorded multi-step experience and environment execution feedback support the positive source values. Unknown initialization/provider inputs prevent complete enumeration; ordinary recorded prompts alone do not add session-logs."
---

# GMemory memory profile

## Comparison rationale

The profile distinguishes content from access structures and follows the accepted records, not a reconstructed execution. Task documents support both readable examples and update inputs; the task-query graph is a different graph from recorded interaction graphs. Rule text supplies advice at solving consumers and learning input at update consumers, while associations rank candidates and scalar scores govern survival ([MEM-OBJ-mas-message](memory.md#mem-obj-mas-message), [MEM-OBJ-task-layer](memory.md#mem-obj-task-layer), [MEM-OBJ-insights-metadata](memory.md#mem-obj-insights-metadata), [RT-BAP-retained-guidance](runtime.md#rt-bap-retained-guidance)). No retained static system prompt is classified as learned instruction.

The two duplicate epistemic rule objects resolve to [MEM-OBJ-insights-rule](memory.md#mem-obj-insights-rule) and [MEM-OBJ-insights-metadata](memory.md#mem-obj-insights-metadata). Their supersessions affect rule form, storage, lineage and authority citations, not the underlying values. Key steps and failure explanations remain distinct consumed parts within task payloads. The stale attribution of effective reward pruning in memory's correction request does not warrant a curation value: the current [RT-RTE-task-retention](runtime.md#rt-rte-task-retention) and [MEM-RTE-state-roundtrip](memory.md#mem-rte-state-roundtrip) both establish that attempted deletion leaves backing states unchanged. The attribution discrepancy does not prevent classification of their agreed mechanism.

Model extraction and merging afford consolidation, while semantic novelty and preservation remain unresolved. EDIT supplies wired evolution and score decrement/pruning supplies decay. Requested causal generality does not prove synthesis, and rejection of a proposed duplicate does not itself deduplicate retained entries ([RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [MEM-RTE-cluster-merge](memory.md#mem-rte-cluster-merge), [EPI-RTE-rule-disposition](epistemic.md#epi-rte-rule-disposition)). The same distinction prevents upgrading requested consolidation to observed model behavior.

Task-query fulfillment is pull, including its requested delivery into prompts. Count-triggered maintenance instead supplies automatically selected retained inputs to new update invocations; temporal edges likewise supply prior node output without a content request from that node. These push paths explain the identifier, embedding and coarse signals without relabeling every relevance selector as push ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance), [MEM-OBJ-node-memory](memory.md#mem-obj-node-memory)). A task name supplies an identifier signal only where membership actually selects delivered material.

Trace learning is an architectural write-route classification here, not a claim of improved capacity. Automatic trace-derived task extras and reusable rules persist for later consumers. Their originating multi-step task trajectories also contain executed environment action requests and results. Recorded agent prompts are not sufficient to add session-log extraction, and describing environmental feedback as a stream would not alone establish an additional source value ([RT-RTE-task-retention](runtime.md#rt-rte-task-retention), [MEM-OBJ-mas-message](memory.md#mem-obj-mas-message), [RT-RTE-insight-maintenance](runtime.md#rt-rte-insight-maintenance)). MacNet's in-process forwarding remains distinct from these durable transformed artifacts.

Initial-store origin and approval, vector provenance and opaque provider retention remain explicit unresolved units rather than inferred manual authorship, training or absence. Opaque model state is not positively classified as use-accumulated model weights merely because the backend is parametric ([RT-CMP-gpt-chat](runtime.md#rt-cmp-gpt-chat), [RT-CMP-embedding-func](runtime.md#rt-cmp-embedding-func)). These limits prevent complete-value claims but do not weaken inspected automatic writes. No operation, improvement or causal benefit is inferred from wiring.

Source-read log: none. This classification used only the supplied members and contracts; it added no source evidence and reopened no report verification.
