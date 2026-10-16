---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "EvoOntology memory comparison: file-backed semantic guidance, task/workload reuse and lifecycle state, with unresolved InsightBench analytical history."
run-id: "AAS-2026-10-13-evoontology-f2d0c7992c6e-01"
source-identity: "https://github.com/ruc-datalab/EvoOntology"
reviewed-boundary: "c94389b764394379086ff25e50d0e0f4396167b4"
memory-comparison:
  version: 2
  scope: "Included: accumulated semantic version families and consumer-specific views; project/workload/task/trajectory records; evolution run/hypothesis/evaluation/source-reference parts; checkpoint/reminder metadata; annotations and explorer snapshots; unresolved InsightBench analytical-history/checkpoint and fallback-associated consumption alternatives. Excluded: shipped static skills/prompts/tool schemas, ordinary unretained per-call history and transient caches as storage, external host compaction/provider state, user databases and evaluator-service internals. Runtime views and caches are discussed only where they select retained content."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Five-family semantic versions, persistent task/trajectory files, workload catalog, lifecycle run/round parts, source pointers, checkpoint metadata and version reports/HTML"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-evaluation"
                - "epistemic.md#epi-rte-gate-aggregation"
                - "runtime.md#rt-bap-session-gate"
                - "memory.md#mem-obj-source-references"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "runtime.md#rt-obj-evolution-session"
              note: "Each declared durable object is persisted as workspace files. Local dataclasses and transient caches are runtime views, not an additional accumulated durable store."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "runtime.md#rt-obj-evolution-session"
          note: "Declared durable objects use workspace JSON, JSONL or HTML files. Semantic links encode a graph but do not establish a graph storage engine; numeric metrics do not establish model-weight storage."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its storage_substrate; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "runtime.md#rt-obj-evolution-session"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Known declared persistence is file-backed. External host/provider retention and user data are excluded, not classified as this memory substrate. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Semantic definitions, scopes, grounding assertions and query/join/filter cautions at model consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-bap-semantic-guidance"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
              note: "Root and local consumers deliver meanings, mappings, constraints and evidence assertions as model-readable guidance; block severity does not compel query refusal."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-bap-semantic-guidance"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
          note: "Stored prose and code-like guidance receive effects through interpretation rather than native execution."
        -
          scope: "Semantic IDs, links, aliases, lifecycle fields and lexical retrieval inputs at deterministic selectors"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-rte-semantic-retrieval"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
              note: "IDs, endpoints, target fields, active-state flags and token/name/alias comparisons govern access to retained parts."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-rte-semantic-retrieval"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
          note: "These localized fields have fixed parsing/matching/selection rules, separately from the meaning of delivered prose."
        -
          scope: "Question/answer/tool-result text, hypotheses, source-scope prose and report summaries at host or human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-source-references"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
              note: "Task text and answers, hypotheses/notes and annotation summaries remain interpretable text in persistent artifacts and requested returns."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
          note: "This covers recorded readable content and its delivery/availability, not the interpretation of every opaque evaluation case."
        -
          scope: "Task/version/provenance pointers, workload selectors, lifecycle status, numeric gate fields, checkpoint thresholds and report links/projections"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-evaluation"
                - "epistemic.md#epi-rte-gate-aggregation"
                - "runtime.md#rt-bap-session-gate"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
                - "memory.md#mem-obj-source-references"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "runtime.md#rt-obj-evolution-session"
              note: "Deterministic code uses IDs, counts, timestamps, score/verdict fields and links to select, gate or project retained objects."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "runtime.md#rt-obj-evolution-session"
          note: "Numeric observations have localized arithmetic consumers and are symbolic, not distributed-parametric representations."
        -
          scope: "Opaque caller-supplied evaluation case payloads and externally referenced raw artifacts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-evaluation"
            - "memory.md#mem-obj-source-references"
          note: "Path references are classified separately. The records do not resolve every pointed-to or opaque payload encoding and actual consumption; the display aggregate cannot classify those bodies."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its representational_form; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "runtime.md#rt-bap-semantic-guidance"
        - "memory.md#mem-rte-bird-guidance"
        - "memory.md#mem-rte-ddr-guidance"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-semantic-retrieval"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "runtime.md#rt-obj-evolution-session"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Mixed forms are split by consumer; external model weights and shipped static instructions are outside this accumulated-memory scope. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Builder/Evolver-authored semantic proposals and causal explanations"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "runtime.md#rt-rte-build-publication"
              note: "Build/Evolve assigns semantic proposals, explanation and patch design to the host model using authorized workload/data evidence."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "runtime.md#rt-rte-build-publication"
          note: "The prescribed model authoring route is established as instruction, not a witnessed production history for any actual populated object."
        -
          scope: "Caller-supplied workload questions, semantic lists, annotations, evaluation observations and trajectory-source entries"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "memory.md#mem-obj-evaluation"
                - "epistemic.md#epi-rte-gate-aggregation"
                - "runtime.md#rt-bap-session-gate"
                - "memory.md#mem-obj-source-references"
                - "runtime.md#rt-rte-version-override"
              note: "Supplied lists, questions, summaries and pointers enter durable local records without proving their original provenance."
          records:
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
            - "runtime.md#rt-rte-version-override"
          note: "APIs admit supplied content; imported lineage at admission does not identify the human or model that originally authored it."
        -
          scope: "Normalized task trajectories and history-derived workload questions/provenance"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Recorded observable task/tool activity is projected into trajectories; compatible history yields durable question/provenance entries."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "Trace derivation is known despite lossy normalization and unreliable BIRD version labels; those defects limit attribution, not existence of extraction."
        -
          scope: "Checkpoint/state metadata and explorer projections compiled from retained records"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "runtime.md#rt-obj-evolution-session"
              note: "Code derives threshold state, lifecycle metadata and version/workload/task/evaluation display projections."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "runtime.md#rt-obj-evolution-session"
          note: "Deterministic metadata and display compilation is distinct from host-authored explanation."
        -
          scope: "Initial thresholds, opaque evaluation cases and raw files behind generic references"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
          note: "The records do not resolve initial caller control or all original payload origins. Known summary/reference admission does not resolve underlying provenance."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its lineage; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "runtime.md#rt-rte-build-publication"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "memory.md#mem-obj-source-references"
        - "runtime.md#rt-rte-version-override"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "runtime.md#rt-obj-evolution-session"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Derivation paths coexist: content imported at an API may have a separately claimed authoring or wired trace-extraction route. No observed object provenance is asserted. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Semantic content at host/benchmark analysis models and report/task content at later readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-bap-semantic-guidance"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "runtime.md#rt-rte-task-execution"
              note: "Delivered definitions, grounding and caution text guide later analysis; explorer snapshots inform human review and saved tasks support resumption."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-bap-semantic-guidance"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "runtime.md#rt-rte-task-execution"
          note: "The effect is interpretive context/reference, not an enforced semantic rule or demonstrated compliance."
        -
          scope: "Retained semantic text and workload features at deterministic relevance/priority selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-rte-semantic-retrieval"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Root/local search scores retained text; workload origin, recency and topic diversity influence relative selection."
            -
              value: "ranking"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-ddr-guidance"
              note: "Optional manifest(task=...) ranks extras; the shipped manifest callers do not pass task and do not activate this filter."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-rte-semantic-retrieval"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "Ranking inputs need not themselves be a retained ranking policy. DDR optional task filtering is only a capability."
        -
          scope: "Active/lifecycle, task/version/source and checkpoint/run metadata at deterministic selection/continuation consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "runtime.md#rt-rte-version-override"
                - "runtime.md#rt-rte-task-execution"
                - "runtime.md#rt-obj-evolution-session"
                - "runtime.md#rt-rte-semantic-retrieval"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
              note: "Pointers/status/thresholds select semantic versions, workload/task inputs, reminder eligibility and lifecycle progression."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "runtime.md#rt-rte-version-override"
            - "runtime.md#rt-rte-task-execution"
            - "runtime.md#rt-obj-evolution-session"
            - "runtime.md#rt-rte-semantic-retrieval"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
          note: "These retained controls choose state, input windows and continuation routes; BIRD lacks the root lifecycle filter."
        -
          scope: "Stored gate protocol, round/candidate/status and supplied score/verdict/regression inputs at session acceptance"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation"
                - "epistemic.md#epi-rte-gate-aggregation"
                - "runtime.md#rt-bap-session-gate"
                - "runtime.md#rt-rte-evolution-admission"
              note: "Retained protocol and gate observations determine whether a candidate meets the session publication criterion."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evaluation"
                - "epistemic.md#epi-rte-gate-aggregation"
                - "runtime.md#rt-bap-session-gate"
                - "runtime.md#rt-rte-evolution-admission"
              note: "A nonpassing or malformed recorded gate and invalid lifecycle state refuse this route's publication."
          records:
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "runtime.md#rt-rte-evolution-admission"
          note: "Admissibility and enforced refusal coexist at this API. The inputs are not independently authenticated and alternate selector writes bypass the veto."
        -
          scope: "Retained task status/events and source/purpose/provenance fields at workflow admission guards"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Persisted events/status and source/split/purpose/provenance inputs are checked before completion or workload/task admission."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Finished-task status blocks later events and incompatible or invalid workload inputs are refused on scoped paths."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "Guards check event/completion shape and workload admissibility rather than authenticating externally supplied observations."
        -
          scope: "Task questions and retained traces at the automatic history-to-workload update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Eligible task history feeds question/provenance compilation into the catalog subsequently used by Builder/start_task."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "Learning authority here means input to a durable behavior-shaping update, not evidence of improved capacity."
        -
          scope: "Trajectories, hypotheses and rejected-round evidence at the instructed Evolver update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-source-references"
              note: "Persisted experience and rejected explanations are directed into subsequent attribution and candidate design."
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-source-references"
              note: "Previous explanations and referenced evidence are directed to later host diagnosis as context, not enforced standing rules."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-source-references"
          note: "The skill requires diagnosis and reuse, but actual content-dependent interpretation is unobserved."
        -
          scope: "Checkpoint-derived reminder at the SessionStart host-context channel"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
              note: "The unsolicited hook generates a short instruction to consider evolution when retained threshold state is due; host injection/compliance remains unobserved."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
          note: "The emitted reason/action instruction depends on accumulated checkpoint/trajectory metadata; it is not the static skill itself."
        -
          scope: "Opaque evaluation cases and file bodies behind source/artifact references"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
          note: "Gate fields and projected summaries have classified consumers; unspecified payload bodies do not establish further authority merely by being retained or pointed to."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its behavioral_authority; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "runtime.md#rt-bap-semantic-guidance"
        - "memory.md#mem-rte-bird-guidance"
        - "memory.md#mem-rte-ddr-guidance"
        - "memory.md#mem-rte-insight-guidance"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "runtime.md#rt-rte-task-execution"
        - "runtime.md#rt-rte-semantic-retrieval"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "runtime.md#rt-rte-version-override"
        - "runtime.md#rt-obj-evolution-session"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "memory.md#mem-obj-hypothesis"
        - "memory.md#mem-obj-source-references"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Authority is classified at actual consumers, separating learning at update inputs, knowledge at outputs, ranking and scoped vetoes. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Host-model Build/Evolve semantic proposal and patch admission under workflow authorization"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "runtime.md#rt-rte-build-publication"
              note: "Skills assign content production/revision to model work; this is a prescribed automatic route, not observed admission control in a deployment."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "runtime.md#rt-rte-build-publication"
          note: "The prescribed model computation has no mandatory per-content human approval. Starting or budgeting the workflow is not manual admission."
        -
          scope: "Trace projection, history-to-workload derivation, checkpoint recomputation and generated explorer snapshot"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
              note: "Deterministic recorders, history normalization/selection, reminder checks and renderer write derived artifacts and metadata."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
          note: "Code selects/projects/adopts derived content without per-content operator decisions; flags triggering a workflow do not make its internal admission manual."
        -
          scope: "Generic direct save/selector, configure/prepare supplied-content, annotation, hypothesis/round/evaluation/source-reference calls and original thresholds"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-version-override"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
          note: "Caller identity and per-content approval are unresolved. Physical software I/O alone cannot decide manual versus automatic admission; neither value is asserted for this alternative."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its write_agency; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "runtime.md#rt-rte-build-publication"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "runtime.md#rt-rte-version-override"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Prescribed model admission and implemented derivations are positive automatic routes. Generic administrative and initial supplied-content control remains distinct and unresolved; no explicit manual witness is recorded. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Trajectory preview extraction and history-to-workload reduction of retained task material"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Observable tool/message content is projected/truncated into durable trajectories, and compatible history is reduced to questions/provenance for later work."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "These routes reduce existing experience into retained observations or question/provenance catalog entries; losses do not establish invention of a new claim."
        -
          scope: "Workload catalog normalization and provenance merging"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Normalized question text merges duplicate entries/provenance and yields a persistent catalog."
          records:
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "This is a retained catalog transformation, unlike transient reply dedup or ID collision checks alone."
        -
          scope: "Host-directed revision of semantic entries and causal explanations"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
              note: "Diagnose/Attribute/Patch and critique direct revision of existing semantic content and attribution across rounds."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
          note: "Revision is prescribed; no actual candidate content or semantic transformation trace is supplied."
        -
          scope: "Direct replacement of named version content"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-version-override"
              note: "save_version permits replacing an existing named version; this affords content revision without the session gate."
          records:
            - "runtime.md#rt-rte-version-override"
          note: "The implemented replacement surface can revise retained entries, but the generic API does not establish which caller or actual content revision occurred."
        -
          scope: "Lifecycle withdrawal of semantic entries at filtered later readers"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-rte-semantic-retrieval"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
              note: "Changing an entry away from active/validated can withdraw later filtered delivery while retaining the version; a write exercising that change is not observed."
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-rte-semantic-retrieval"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
          note: "History remains stored; scoped readers stop reliance on non-active content. BIRD drops lifecycle state and InsightBench shortcut enforcement is uninspected, so withdrawal is not universal."
        -
          scope: "Semantic novelty, opaque caller evaluation bodies and original input transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "runtime.md#rt-rte-evolution-admission"
            - "epistemic.md#epi-rte-semantic-projection"
          note: "Recorded generation relations remain indeterminate; novel authored claims, decay and semantic synthesis are not established. Retention, selector publication and index/reply projection alone do not establish other curation operations."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its curation_operations; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "runtime.md#rt-rte-version-override"
        - "runtime.md#rt-rte-semantic-retrieval"
        - "memory.md#mem-rte-bird-guidance"
        - "memory.md#mem-rte-ddr-guidance"
        - "memory.md#mem-rte-insight-guidance"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "epistemic.md#epi-rte-semantic-projection"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Classifications follow the implemented reduction/merge or separately prescribed/afforded revision mechanism. Transient InsightBench response dedup is not persistent semantic curation; publication is not by itself tier promotion. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested root/plugin semantic resources/tools, shipped benchmark task setup/tools, workload/task reuse, status/resume/source requests and explorer rendering"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-semantic-retrieval"
                - "runtime.md#rt-rte-task-execution"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-rte-bird-guidance"
                - "memory.md#mem-rte-ddr-guidance"
                - "memory.md#mem-rte-insight-guidance"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
                - "memory.md#mem-obj-source-references"
                - "memory.md#mem-obj-version-report"
                - "memory.md#mem-rte-explorer-projection"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
              note: "Later requests load selected retained semantic/task/workload/run/reference/state content or generate a human-facing snapshot."
          records:
            - "runtime.md#rt-rte-semantic-retrieval"
            - "runtime.md#rt-rte-task-execution"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
          note: "Automatic selection inside a requested return does not make it unsolicited push. DDR task initialization is recorded as requested setup, not a separate event."
        -
          scope: "Host reads of persisted prior evidence, explanations and evolution reports during instructed diagnosis"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-source-references"
              note: "Durable records and explicit reuse instructions afford requested host reconstruction of prior evolution knowledge."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-source-references"
          note: "The skill directs reads and reuse; actual access to referenced bodies is not established by a pointer-return API."
        -
          scope: "Claude SessionStart checkpoint reminder"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
              note: "SessionStart selects eligible workspaces and due checkpoint/trajectory threshold state, then emits systemMessage/additionalContext for the host."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
          note: "No consumer request for retained material precedes the hook selector; the delivered material is a short state-derived reason/instruction, not whole trajectories."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its read_back_direction; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "runtime.md#rt-rte-semantic-retrieval"
        - "runtime.md#rt-rte-task-execution"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-rte-bird-guidance"
        - "memory.md#mem-rte-ddr-guidance"
        - "memory.md#mem-rte-insight-guidance"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Both requested later consumption and a checkpoint-derived unsolicited reminder are established; actual host injection and meaningful model use remain unobserved. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Claude SessionStart reminder selection from workspace availability and checkpoint/count/time metadata"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-rte-reminder-delivery"
              note: "Availability and threshold conditions select reminder delivery. A checkpoint task ID marks a counting boundary, not an identity match selecting delivered semantic or trace parts."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-rte-reminder-delivery"
          note: "Trigger is SessionStart; selector inputs are active.json presence, trajectory count since checkpoint and elapsed time; selected retained part is workspace/checkpoint eligibility metadata reduced to reason/action context."
        -
          scope: "Requested root/local semantic tools, task/workload/status/resume/reference and explorer routes"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-semantic-retrieval"
            - "runtime.md#rt-rte-task-execution"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-rte-bird-guidance"
            - "memory.md#mem-rte-ddr-guidance"
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-source-references"
            - "memory.md#mem-obj-version-report"
            - "memory.md#mem-rte-explorer-projection"
          note: "These are pull operations, including requested benchmark setup. Their ID/token/alias matching is not a push signal, and DDR optional task filtering is not invoked by shipped manifest callers."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its read_back_signal; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-rte-reminder-delivery"
        - "runtime.md#rt-rte-semantic-retrieval"
        - "runtime.md#rt-rte-task-execution"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-rte-bird-guidance"
        - "memory.md#mem-rte-ddr-guidance"
        - "memory.md#mem-rte-insight-guidance"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-obj-version-report"
        - "memory.md#mem-rte-explorer-projection"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "The established push uses coarse eligibility. Requested semantic lexical/ID selectors do not warrant inferred-lexical or identifier push classifications. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic history-to-workload question/provenance write followed by Builder/start_task consumption"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Eligible traces feed automatic durable question/provenance compilation; later preparation/start_task uses the catalog to shape task inputs."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
          note: "Qualifying durable behavior-shaping material is the catalog, not raw log retention alone. Its later task/build-input use is wired; improved capacity is unobserved."
        -
          scope: "Model-directed trace diagnosis to candidate semantic content and later semantic guidance"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
                - "memory.md#mem-obj-term"
                - "memory.md#mem-obj-mapping"
                - "memory.md#mem-obj-relation"
                - "memory.md#mem-obj-constraint"
                - "memory.md#mem-obj-evidence"
                - "runtime.md#rt-bap-semantic-guidance"
              note: "The Evolver is directed to turn retained task experience into revised durable ontology guidance for later tasks, without mandatory per-content human approval."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
            - "memory.md#mem-obj-term"
            - "memory.md#mem-obj-mapping"
            - "memory.md#mem-obj-relation"
            - "memory.md#mem-obj-constraint"
            - "memory.md#mem-obj-evidence"
            - "runtime.md#rt-bap-semantic-guidance"
          note: "The prescribed automatic host-model update is distinct from Python storage/gating. Candidate production from experience is instructed, and downstream selected semantic delivery is wired; no actual patch history is supplied."
        -
          scope: "Generic supplied-content updates and opaque evaluation/artifact inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-version-override"
            - "memory.md#mem-obj-evaluation"
            - "epistemic.md#epi-rte-gate-aggregation"
            - "runtime.md#rt-bap-session-gate"
            - "memory.md#mem-obj-source-references"
          note: "No recorded source-to-automatic-update-to-later-consumer chain resolves these alternatives. Raw retention, thresholds and gate scores alone do not establish a further qualifying trace-learning write, but no bounded absence record licenses no."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its trace_learning; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-obj-term"
        - "memory.md#mem-obj-mapping"
        - "memory.md#mem-obj-relation"
        - "memory.md#mem-obj-constraint"
        - "memory.md#mem-obj-evidence"
        - "runtime.md#rt-bap-semantic-guidance"
        - "runtime.md#rt-rte-version-override"
        - "memory.md#mem-obj-evaluation"
        - "epistemic.md#epi-rte-gate-aggregation"
        - "runtime.md#rt-bap-session-gate"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Quote yes as a string. This axis denotes automatic trace-fed durable updates, independently of the runtime learning conclusion about improved capacity. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Recorded tool activity consumed through trajectories by the instructed semantic-evolution update"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
              note: "Host diagnosis is instructed to use retained semantic/native tool requests and observations when designing durable semantic changes."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
          note: "Original content includes tool inputs/results, not conversational agent prose. Normalization removes chain-of-thought and does not preserve a complete session log."
        -
          scope: "Linked question, selected version, task events/status/outcome as experience for workload reuse and instructed evolution"
          assessment: "known"
          findings:
            -
              value: "trajectories"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-workload"
                - "memory.md#mem-rte-workload-reuse"
              note: "Eligible task-linked experience is the original history source for automatic persistent question/provenance reuse."
            -
              value: "trajectories"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-trace-retention"
                - "runtime.md#rt-rte-task-execution"
                - "memory.md#mem-obj-hypothesis"
                - "runtime.md#rt-rte-evolution-admission"
              note: "The prescribed Evolver uses task-linked question/activity/outcome experience for diagnosis and semantic revision."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-hypothesis"
            - "runtime.md#rt-rte-evolution-admission"
          note: "Trajectories retain task-linked activity and outcomes, although benchmark projections can lose ordering, native observations or correct version labels. Classification does not imply complete replay."
        -
          scope: "Opaque caller observations, generated/question provenance and referenced external logs used in qualifying update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-task-execution"
            - "memory.md#mem-obj-workload"
            - "memory.md#mem-rte-workload-reuse"
            - "memory.md#mem-obj-source-references"
            - "runtime.md#rt-rte-evolution-admission"
          note: "Known tool/task content does not resolve every original source. No recorded chain establishes session-logs or event-streams for the opaque alternative, and a task event serialization alone adds neither value."
        -
          scope: "Included InsightBench analytical-history/checkpoint payloads and fallback-associated later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-insight-guidance"
            - "memory.md#mem-rte-trace-retention"
            - "runtime.md#rt-rte-benchmark-tool-loop"
          note: "The accepted account explicitly retains an untraced recovery/history inventory beyond normalized trajectories. No canonical part/route declarations classify its trace_source; available evidence was not independently traced. This prevents complete boundary coverage, not the positive findings on inspected routes."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-trace-retention"
        - "runtime.md#rt-rte-task-execution"
        - "memory.md#mem-obj-hypothesis"
        - "runtime.md#rt-rte-evolution-admission"
        - "memory.md#mem-obj-workload"
        - "memory.md#mem-rte-workload-reuse"
        - "memory.md#mem-obj-source-references"
        - "memory.md#mem-rte-insight-guidance"
        - "runtime.md#rt-rte-benchmark-tool-loop"
      note: "Classify original content, not the trajectory filename or event adapter label. Known experience sources coexist with unresolved original inputs; trace source cannot be made inapplicable in this partial positive boundary. The included InsightBench recovery/history inventory remains unresolved; positives do not establish complete enumeration."
---

# EvoOntology memory profile

## Comparison rationale

The inventory is partial, not a file-store-only simplification of the whole system. The accepted memory account and reconciliation retain an undeclared InsightBench analytical-history/checkpoint and fallback-consumption inventory. Each axis keeps that included alternative unresolved rather than inferring its properties from normalized trajectories or ToolCallingChat frames. The relevant canonical records are [MEM-RTE-insight-guidance](memory.md#mem-rte-insight-guidance), [MEM-RTE-trace-retention](memory.md#mem-rte-trace-retention) and [RT-RTE-benchmark-tool-loop](runtime.md#rt-rte-benchmark-tool-loop). This missing inventory prevents complete classification; it does not defeat the scoped positives.

Reconciliation supersedes the five epistemic semantic-object declarations with [MEM-OBJ-term](memory.md#mem-obj-term), [MEM-OBJ-mapping](memory.md#mem-obj-mapping), [MEM-OBJ-relation](memory.md#mem-obj-relation), [MEM-OBJ-constraint](memory.md#mem-obj-constraint) and [MEM-OBJ-evidence](memory.md#mem-obj-evidence). All profile object citations use those canonical declarations. The valid [RT-OBJ-evolution-session](runtime.md#rt-obj-evolution-session) container remains alongside its hypothesis, evaluation and source-reference parts; containment does not upgrade their individual warrants.

Semantic JSON links are symbolic access structure, not a graph database. Gate numbers are symbolic observations, not learned parameters. Query/filter/connection strings at the analytical model supply knowledge through interpretation; they are not enforced native-query rules. Retained strings also serve as ranking inputs at fixed lexical selectors. Those independent effects are grounded in [RT-RTE-semantic-retrieval](runtime.md#rt-rte-semantic-retrieval), the five semantic families and the three consumer-specific guidance records. No universal withdrawal guarantee follows: [MEM-RTE-bird-guidance](memory.md#mem-rte-bird-guidance) drops lifecycle state, and [MEM-RTE-insight-guidance](memory.md#mem-rte-insight-guidance) retains a shortcut/binder inspection limit.

Admission control is classified at the content decision, not at disk I/O. The model-directed Build/Evolve route has automatic admission as a claimed method; deterministic trace/workload derivations supply wired automatic witnesses. Generic supplied-content APIs and initial thresholds remain not-determinable because no explicit per-content human decision is established. Their uncertainty is not erased by another route's automatic writer. See [RT-RTE-build-publication](runtime.md#rt-rte-build-publication), [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission), [RT-RTE-version-override](runtime.md#rt-rte-version-override) and [MEM-OBJ-checkpoint](memory.md#mem-obj-checkpoint).

Trace-fed workload reuse qualifies because it automatically retains questions/provenance derived from task experience and later shapes Builder/task inputs. The separate model-mediated trace-to-ontology route remains claimed at the update step even though persistence, publication and downstream guidance are wired. Neither classification establishes improved future capacity, successful causal attribution or exercised self-improvement. Raw trace retention alone does not qualify. Tool observations and task-linked experience support the stated source values; discarded agent prose does not establish a session-log learning route. Opaque supplied observations and reference bodies retain their origin limits. See [MEM-RTE-workload-reuse](memory.md#mem-rte-workload-reuse), [MEM-RTE-trace-retention](memory.md#mem-rte-trace-retention), [MEM-OBJ-hypothesis](memory.md#mem-obj-hypothesis) and [RT-RTE-evolution-admission](runtime.md#rt-rte-evolution-admission).

Curation distinguishes durable workload deduplication and trace consolidation from reply suppression. InsightBench's transient browse/resolve history is not persistent semantic curation. Semantic revision is prescribed, and direct named-version replacement affords revision, but neither supplies observed semantic novelty. Projection, publication and index selection do not alone establish synthesis, decay or promotion. The opaque transformation unit therefore retains uncertainty rather than declaring those operations absent. See [MEM-RTE-workload-reuse](memory.md#mem-rte-workload-reuse), [MEM-RTE-trace-retention](memory.md#mem-rte-trace-retention), [MEM-RTE-insight-guidance](memory.md#mem-rte-insight-guidance), [RT-RTE-version-override](runtime.md#rt-rte-version-override) and [EPI-RTE-semantic-projection](epistemic.md#epi-rte-semantic-projection).

Requested task setup remains pull, even when code chooses the supplied manifest. In particular, [MEM-RTE-ddr-guidance](memory.md#mem-rte-ddr-guidance) establishes that shipped callers omit the optional task argument; the optional relevance filter is afforded ranking, not wired task-targeted manifest delivery. The established unsolicited route is [MEM-RTE-reminder-delivery](memory.md#mem-rte-reminder-delivery). It uses coarse availability/count/time criteria and sends checkpoint-derived reason/action context. A checkpoint task pointer identifies the counting boundary, not an identity match selecting delivered semantic parts. Pull-only units are locally inapplicable to push signals, but do not make the partial system axis inapplicable.

No target source reads were performed for this classification. All warrants come from the supplied accepted records and their annotations, resolved through the supplied reconciliation. No observed run or causal experiment is claimed.
