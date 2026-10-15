---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: OpenSage memory comparison for retained sandbox files, session context, checkpoints and shipped
  benchmark handoffs, with opaque alternatives retained.
run-id: AAS-2026-10-14-opensage-291d1ed79d37-01
source-identity: https://github.com/opensage-agent/OpenSage
reviewed-boundary: 54d64702e18d195c8f0fed711c6db5dc1d62ab29
memory-comparison:
  version: 2
  scope: Use-accumulated sandbox wiki/TODO/pins/findings and tool-output files; session trajectories,
    compaction/tool summaries, retained hook/image parts; dynamic definitions/instructions and checkpoint
    selectors; shipped exploration/vulnerability handoffs, evaluation traces and retained scores/grades.
    Includes unresolved ADK service/provider retained state, live retention, trainer checkpoint/update
    and custom-extension/remaining benchmark alternatives. Excludes static shipped root/maintenance instructions,
    ordinary inference weights without a retained update, task-source code graphs and repository data
    not shown to accumulate through use, and external implementation bodies; their included interfaces
    remain uncertain.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Sandbox wiki, task notes, pins, saved outputs/findings; host trajectories, selectors, definitions
          and vulnerability checkpoints
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-traj
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-obj-pinned
          - memory.md#mem-obj-todo
          - memory.md#mem-obj-knowledge-files
          - memory.md#mem-obj-tool-output
          - memory.md#mem-obj-tool-summary
          - memory.md#mem-obj-checkpoint-selectors
          - memory.md#mem-obj-findings
          - memory.md#mem-obj-vulnerability-findings
          - runtime.md#rt-obj-agent-definition
          - runtime.md#rt-obj-agent-instruction
          note: Records identify sandbox Markdown/output files and host JSON/TOML checkpoints; serialization
            format is not a substrate.
        records: *id001
        note: Records identify sandbox Markdown/output files and host JSON/TOML checkpoints; serialization
          format is not a substrate.
      - scope: Live event/compaction state, pending hook/image parts and restored objects
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-traj
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-obj-hook-context
          - memory.md#mem-obj-image-parts
          - memory.md#mem-rte-checkpoint-resume
          note: These retained parts also reside in process session events and pending lists; persistence
            is conditional.
        records: *id002
        note: These retained parts also reside in process session events and pending lists; persistence
          is conditional.
      - scope: Evaluation traces and retained DevOps grades
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - runtime.md#rt-rte-evaluation-rollout
          - workflow.md#wf-rte-devops-grading
          - epistemic.md#epi-obj-solved-score
          note: Exported traces, score.json and grade files have later evaluation/report consumers.
        records: *id003
        note: Exported traces, score.json and grade files have later evaluation/report consumers.
      - scope: Constructed ADK memory service handle
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - memory.md#mem-cmp-memory-service
          note: The record establishes dependency-owned process memory, not its payload encoding or a
            consumer route.
        records: *id004
        note: The record establishes dependency-owned process memory, not its payload encoding or a consumer
          route.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: &id011
        - memory.md#mem-cmp-memory-service
        - runtime.md#rt-rte-live-runner
        - runtime.md#rt-rte-evaluation-rollout
        - memory.md#mem-rte-hook-retention
        note: Provider caches, learned checkpoints and extension-specific retained storage are not classified
          by a service name or integration handle.
      records:
      - memory.md#mem-obj-traj
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-obj-pinned
      - memory.md#mem-obj-todo
      - memory.md#mem-obj-knowledge-files
      - memory.md#mem-obj-tool-output
      - memory.md#mem-obj-tool-summary
      - memory.md#mem-obj-checkpoint-selectors
      - memory.md#mem-obj-findings
      - memory.md#mem-obj-vulnerability-findings
      - runtime.md#rt-obj-agent-definition
      - runtime.md#rt-obj-agent-instruction
      - memory.md#mem-obj-hook-context
      - memory.md#mem-obj-image-parts
      - memory.md#mem-rte-checkpoint-resume
      - runtime.md#rt-rte-evaluation-rollout
      - workflow.md#wf-rte-devops-grading
      - epistemic.md#epi-obj-solved-score
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - memory.md#mem-rte-hook-retention
      note: The inventoried file/process stores are supported; opaque alternatives and incomplete extension/benchmark
        inspection prevent complete substrate enumeration.
    representational_form:
      assessment: partial
      units:
      - scope: Wiki/TODO/pin/finding text; dynamic instruction; compacted/tool-summary text; hook text;
          vulnerability descriptions
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-knowledge-files
          - memory.md#mem-obj-todo
          - memory.md#mem-obj-pinned
          - memory.md#mem-obj-findings
          - runtime.md#rt-obj-agent-instruction
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-obj-tool-summary
          - memory.md#mem-obj-hook-context
          - memory.md#mem-obj-vulnerability-findings
          note: Model-interpreted prose is distinct from the wrappers and fixed-rule selectors.
        records: *id005
        note: Model-interpreted prose is distinct from the wrappers and fixed-rule selectors.
      - scope: Trajectory call/state envelope, range/branch metadata, definition/checkpoint selectors,
          structured vulnerability fields and reduction tags
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-traj
          - memory.md#mem-obj-compacted-content
          - runtime.md#rt-obj-agent-definition
          - memory.md#mem-obj-checkpoint-selectors
          - memory.md#mem-obj-vulnerability-findings
          - memory.md#mem-obj-tool-summary
          note: Localized fields have fixed serialization, selection, parsing or reconstruction rules.
        records: *id006
        note: Localized fields have fixed serialization, selection, parsing or reconstruction rules.
      - scope: Consultation reasoning and critique/audit advice
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - epistemic.md#epi-obj-critique-idea
          - epistemic.md#epi-obj-assumption-audit
          - epistemic.md#epi-obj-validation-reasoning
          note: Returned advice can be retained in caller event history under the runner contract; no
            pooled decision warrant.
        records: *id007
        note: Returned advice can be retained in caller event history under the runner contract; no pooled
          decision warrant.
      - scope: Parsed validation decisions and benchmark decision fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - epistemic.md#epi-obj-validation-decision
          - epistemic.md#epi-obj-solved-score
          - epistemic.md#epi-obj-vulnerability-match
          - workflow.md#wf-rte-devops-grading
          note: Boolean/enumeration/count fields are consumed by fixed parsers and report aggregation.
        records: *id008
        note: Boolean/enumeration/count fields are consumed by fixed parsers and report aggregation.
      - scope: Retained benchmark explanations
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - epistemic.md#epi-obj-judge-reasons
          - epistemic.md#epi-obj-match-reason
          note: Explanation consumers interpret text independently of score predicates.
        records: *id009
        note: Explanation consumers interpret text independently of score predicates.
      - scope: Image MIME/part wrapper
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id010
          - memory.md#mem-obj-image-parts
          - memory.md#mem-rte-image-retention
          note: The fixed-rule wrapper is not the consumed binary image or a visual summary.
        records: *id010
        note: The fixed-rule wrapper is not the consumed binary image or a visual summary.
      - scope: Image rejection notice delivered to the model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: *id010
          note: Readable rejection text tells the model to resubmit smaller images; it is interpreted
            guidance, not the fixed-rule MIME/part wrapper or a visual summary.
        records: *id010
        note: The recorded rejection notice is model-interpreted text. This classification excludes
          both the symbolic wrapper and opaque binary payload.
      - scope: Retained binary image payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-image-parts
        note: The opaque image bytes are neither shown to be natural-language, symbolic semantic content
          nor distributed-parametric memory. A readable notice cannot classify them.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: ADK payload forms, provider retained numerical state and trainer checkpoints are not inspected.
          Ordinary inference weights are not use-accumulated memory merely because models consume it.
      records:
      - memory.md#mem-obj-knowledge-files
      - memory.md#mem-obj-todo
      - memory.md#mem-obj-pinned
      - memory.md#mem-obj-findings
      - runtime.md#rt-obj-agent-instruction
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-obj-tool-summary
      - memory.md#mem-obj-hook-context
      - memory.md#mem-obj-vulnerability-findings
      - memory.md#mem-obj-traj
      - runtime.md#rt-obj-agent-definition
      - memory.md#mem-obj-checkpoint-selectors
      - epistemic.md#epi-obj-critique-idea
      - epistemic.md#epi-obj-assumption-audit
      - epistemic.md#epi-obj-validation-reasoning
      - epistemic.md#epi-obj-validation-decision
      - epistemic.md#epi-obj-solved-score
      - epistemic.md#epi-obj-vulnerability-match
      - workflow.md#wf-rte-devops-grading
      - epistemic.md#epi-obj-judge-reasons
      - epistemic.md#epi-obj-match-reason
      - memory.md#mem-obj-image-parts
      - memory.md#mem-rte-image-retention
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      - memory.md#mem-rte-hook-retention
      note: Mixed text and fixed-rule parts are separated; binary and opaque payloads prevent complete
        form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Framework seed, checkpoint metadata and code-selected prefixes
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-obj-todo
          - memory.md#mem-obj-knowledge-files
          - memory.md#mem-obj-checkpoint-selectors
          - memory.md#mem-rte-output-reduction
          note: Software creates generic seed/control metadata and deterministic prefixes; these are not
            authored knowledge or learned weights.
        records: *id012
        note: Software creates generic seed/control metadata and deterministic prefixes; these are not
          authored knowledge or learned weights.
      - scope: Use-derived history compaction, tool reduction and explore quota fallback
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-rte-output-reduction
          - memory.md#mem-rte-explore-handoff
          note: Models extract retained context from recorded user/model/tool history; prefix alternatives
            are separately compiled.
        records: *id013
        note: Models extract retained context from recorded user/model/tool history; prefix alternatives
          are separately compiled.
      - scope: Agent-written wiki/task/pin content
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records: &id014
          - memory.md#mem-rte-wiki-maintenance
          note: The maintenance affordance asks the foreground agent to write reusable entries and task
            notes.
        records: *id014
        note: The maintenance affordance asks the foreground agent to write reusable entries and task
          notes.
      - scope: Dynamic child instructions
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id015
          - runtime.md#rt-obj-agent-instruction
          - runtime.md#rt-rte-create-subagent
          note: The caller supplies instruction text and builder policy is appended; caller human identity
            is not inferred.
        records: *id015
        note: The caller supplies instruction text and builder policy is appended; caller human identity
          is not inferred.
      - scope: Tool-obtained image payloads and retained executed hook output
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id016
          - memory.md#mem-obj-image-parts
          - memory.md#mem-obj-hook-context
          note: Content enters retention from tools/commands; this says neither its ultimate provenance
            nor that it is a trace.
        records: *id016
        note: Content enters retention from tools/commands; this says neither its ultimate provenance
          nor that it is a trace.
      - scope: Initial non-seed wiki/pin content and per-hook/image source provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-pinned
        - memory.md#mem-obj-knowledge-files
        - memory.md#mem-obj-hook-context
        - memory.md#mem-obj-image-parts
        note: Records establish some local admission/derivation paths, not every initial writer, image
          origin or hook output derivation.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: External learned state and additional benchmark/extension derivations remain uninspected.
      records:
      - memory.md#mem-obj-todo
      - memory.md#mem-obj-knowledge-files
      - memory.md#mem-obj-checkpoint-selectors
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-wiki-maintenance
      - runtime.md#rt-obj-agent-instruction
      - runtime.md#rt-rte-create-subagent
      - memory.md#mem-obj-image-parts
      - memory.md#mem-obj-hook-context
      - memory.md#mem-obj-pinned
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      - memory.md#mem-rte-hook-retention
      note: Known derivation paths do not resolve initial or opaque provenance; imported static shipped
        instructions alone are excluded from accumulated memory.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained summary and vulnerability descriptions at later model consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id017
          - memory.md#mem-bap-summary-authority
          - memory.md#mem-rte-findings-resume
          note: Context/advice supplies information; delivery is not compliance or truth acceptance.
        records: *id017
        note: Context/advice supplies information; delivery is not compliance or truth acceptance.
      - scope: Wiki, task notes and findings at explicit future file readers
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id018
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-obj-todo
          - memory.md#mem-rte-finding-admission
          note: Policy documents future agent readers; exposed finding-file reads afford reference use
            without proving deployed activation.
        records: *id018
        note: Policy documents future agent readers; exposed finding-file reads afford reference use without
          proving deployed activation.
      - scope: Finding and contradiction text at internal peer-delivery consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id019
          - epistemic.md#epi-rte-finding-delivery
          note: The inspected ordinary broadcast branch supplies advisory text; its internal wiring does
            not upgrade unresolved shipped invocation.
        records: *id019
        note: The inspected ordinary broadcast branch supplies advisory text; its internal wiring does
          not upgrade unresolved shipped invocation.
      - scope: Retained dynamic instruction at spawned/rebuilt child model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id020
          - runtime.md#rt-bap-dynamic-instruction
          - runtime.md#rt-obj-agent-instruction
          note: Saved full_instruction supplies standing directions, unlike the static maintenance policy
            excluded here.
        records: *id020
        note: Saved full_instruction supplies standing directions, unlike the static maintenance policy
          excluded here.
      - scope: Pinned operational directions and retained hook guidance at later model history
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id021
          - memory.md#mem-obj-pinned
          - memory.md#mem-obj-hook-context
          - memory.md#mem-rte-hook-retention
          note: These recorded guidance parts carry interpreted directions; arbitrary command output is
            not upgraded to instruction.
        records: *id021
        note: These recorded guidance parts carry interpreted directions; arbitrary command output is
          not upgraded to instruction.
      - scope: Recorded older user/model/tool history at summary-update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id022
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-rte-output-reduction
          - memory.md#mem-rte-explore-handoff
          note: Recorded experience feeds automatic production of retained behavior-shaping context; downstream
            summary knowledge is a different effect.
        records: *id022
        note: Recorded experience feeds automatic production of retained behavior-shaping context; downstream
          summary knowledge is a different effect.
      - scope: Previous findings at duplicate-check admission consumer
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id023
          - epistemic.md#epi-rte-finding-check
          - epistemic.md#epi-rte-finding-write
          note: Prior text supplies duplicate criteria; the interpreted DUPLICATE_OF result vetoes addition.
            This does not validate truth.
        - value: enforcement
          basis: wired
          records: *id023
          note: Prior text supplies duplicate criteria; the interpreted DUPLICATE_OF result vetoes addition.
            This does not validate truth.
        records: *id023
        note: Prior text supplies duplicate criteria; the interpreted DUPLICATE_OF result vetoes addition.
          This does not validate truth.
      - scope: Retained checkpoint/definition/range selectors and vulnerability stage fields
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id024
          - memory.md#mem-rte-checkpoint-resume
          - runtime.md#rt-rte-create-subagent
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-rte-findings-resume
          note: IDs, metadata and finding presence select restored state, capabilities, history ranges
            or next task stage.
        records: *id024
        note: IDs, metadata and finding presence select restored state, capabilities, history ranges or
          next task stage.
      - scope: Retained benchmark decision fields at report/scoring consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id025
          - epistemic.md#epi-rte-cybench-disposition
          - epistemic.md#epi-rte-vulnerability-comparison
          - workflow.md#wf-rte-devops-grading
          note: Scores and parsed grade/match fields determine reported relative task performance; no
            learned ranking policy is inferred.
        records: *id025
        note: Scores and parsed grade/match fields determine reported relative task performance; no learned
          ranking policy is inferred.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: Authority of opaque service state, trained parameters and arbitrary retained extension output
          cannot be resolved from transport alone.
      records:
      - memory.md#mem-bap-summary-authority
      - memory.md#mem-rte-findings-resume
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-obj-todo
      - memory.md#mem-rte-finding-admission
      - epistemic.md#epi-rte-finding-delivery
      - runtime.md#rt-bap-dynamic-instruction
      - runtime.md#rt-obj-agent-instruction
      - memory.md#mem-obj-pinned
      - memory.md#mem-obj-hook-context
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-rte-explore-handoff
      - epistemic.md#epi-rte-finding-check
      - epistemic.md#epi-rte-finding-write
      - memory.md#mem-rte-checkpoint-resume
      - runtime.md#rt-rte-create-subagent
      - epistemic.md#epi-rte-cybench-disposition
      - epistemic.md#epi-rte-vulnerability-comparison
      - workflow.md#wf-rte-devops-grading
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      note: Distinct consumers retain distinct forces. Static root/memory policy is excluded; knowledge,
        instruction and learning are not interchangeable.
    write_agency:
      assessment: partial
      units:
      - scope: Software seeds, checkpoints, dynamic-definition admission, compaction and tool reduction
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id026
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-rte-checkpoint-resume
          - runtime.md#rt-rte-create-subagent
          - runtime.md#rt-rte-history-compaction
          - memory.md#mem-rte-output-reduction
          note: Software/model admission has no per-content human decision; workflow startup is not manual
            admission.
        records: *id026
        note: Software/model admission has no per-content human decision; workflow startup is not manual
          admission.
      - scope: Finding append/suppression, hook/image retention and benchmark handoffs/grades
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id027
          - epistemic.md#epi-rte-finding-write
          - memory.md#mem-rte-hook-retention
          - memory.md#mem-rte-image-retention
          - memory.md#mem-rte-explore-handoff
          - memory.md#mem-rte-findings-resume
          - workflow.md#wf-rte-devops-grading
          note: Code/model accepts content under local predicates, not explicit operator approval of each
            retained item.
        records: *id027
        note: Code/model accepts content under local predicates, not explicit operator approval of each
          retained item.
      - scope: Foreground-agent wiki/TODO/pin writes
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records: &id028
          - memory.md#mem-rte-wiki-maintenance
          note: The named model-directed maintenance branch admits its own text through granted file tools.
        records: *id028
        note: The named model-directed maintenance branch admits its own text through granted file tools.
      - scope: Other filesystem writers, initial non-seed content and externally replaced checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-pinned
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-findings-resume
        note: Generic writer identity and the possibility of file replacement do not prove a manual decision
          or automatic replacement mechanism.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: External trainer acceptance and custom extension write controls are uninspected.
      records:
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-rte-checkpoint-resume
      - runtime.md#rt-rte-create-subagent
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-rte-output-reduction
      - epistemic.md#epi-rte-finding-write
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-rte-image-retention
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-findings-resume
      - workflow.md#wf-rte-devops-grading
      - memory.md#mem-obj-pinned
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      note: Automatic routes are positive; no recorded explicit per-content human decision supports manual.
        Unresolved writers prevent an automatic-only conclusion.
    curation_operations:
      assessment: partial
      units:
      - scope: Older retained history and saved/reduced tool content
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id029
          - memory.md#mem-obj-compacted-content
          - runtime.md#rt-rte-history-compaction
          - memory.md#mem-rte-output-reduction
          note: Selected claims are compressed into a summary or preview; original raw records may remain.
            Fidelity defects do not imply synthesis.
        records: *id029
        note: Selected claims are compressed into a summary or preview; original raw records may remain.
          Fidelity defects do not imply synthesis.
      - scope: Explore quota-exception trace summary
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id030
          - memory.md#mem-rte-explore-handoff
          note: Selected truncated trace is compressed into a handoff; ordinary final-text copying is
            not a second curation transformation.
        records: *id030
        note: Selected truncated trace is compressed into a handoff; ordinary final-text copying is not
          a second curation transformation.
      - scope: New duplicate finding suppressed against retained prior findings
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id031
          - epistemic.md#epi-rte-finding-check
          - epistemic.md#epi-rte-finding-write
          note: Model-mediated near-duplicate admission suppresses redundant content; this is not automatic
            retraction of an old contradicted finding.
        records: *id031
        note: Model-mediated near-duplicate admission suppresses redundant content; this is not automatic
          retraction of an old contradicted finding.
      - scope: Requested stale wiki correction/removal
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id032
          - memory.md#mem-rte-wiki-maintenance
          - epistemic.md#epi-clm-knowledge-policy
          note: Policy requests revising entries or removing them and index lines. These remain claimed
            operations, not proof of performed curation.
        - value: decay
          basis: claimed
          records: *id032
          note: Policy requests revising entries or removing them and index lines. These remain claimed
            operations, not proof of performed curation.
        records: *id032
        note: Policy requests revising entries or removing them and index lines. These remain claimed
          operations, not proof of performed curation.
      - scope: Finding contradiction analysis and other model-written content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-findings
        - epistemic.md#epi-rte-finding-check
        note: No concrete output establishes synthesis, entailed revision, promotion or invalidation;
          contradiction exposure alone does not withdraw prior reliance.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: Extension/trainer transformations and remaining benchmark retention are not completely inventoried.
      records:
      - memory.md#mem-obj-compacted-content
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-rte-explore-handoff
      - epistemic.md#epi-rte-finding-check
      - epistemic.md#epi-rte-finding-write
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-clm-knowledge-policy
      - memory.md#mem-obj-findings
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      - memory.md#mem-rte-hook-retention
      note: Implemented consolidation/dedup coexist with policy-only revision/forgetting and opaque alternatives.
        Primary-key checks, acquisition and structural resume sanitation alone add no curation value.
    read_back_direction:
      assessment: partial
      units:
      - scope: Wiki/TODO/full tool-output and shared finding file requests
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id033
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-obj-todo
          - memory.md#mem-obj-tool-output
          - memory.md#mem-rte-finding-admission
          note: A named later agent requests file contents; a delivered path alone is not content retrieval.
        records: *id033
        note: A named later agent requests file contents; a delivered path alone is not content retrieval.
      - scope: Requested resume, child continuation/inheritance and explicit history consultation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id034
          - memory.md#mem-rte-checkpoint-resume
          - runtime.md#rt-rte-directed-child
          - memory.md#mem-rte-history-consultation
          note: Requests select retained sessions/history. Their requested returns are not separate push
            operations.
        records: *id034
        note: Requests select retained sessions/history. Their requested returns are not separate push
          operations.
      - scope: History folding/pin embedding, reduced-response future history, retained hook/image delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id035
          - runtime.md#rt-rte-history-compaction
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-rte-output-reduction
          - memory.md#mem-rte-hook-retention
          - memory.md#mem-rte-image-retention
          note: Automatic selectors supply retained context without a content-retrieval request, conditional
            on plugins and later invocation.
        records: *id035
        note: Automatic selectors supply retained context without a content-retrieval request, conditional
          on plugins and later invocation.
      - scope: Finding broadcast and benchmark explore/findings next-agent handoffs
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id036
          - epistemic.md#epi-rte-finding-delivery
          - memory.md#mem-rte-explore-handoff
          - memory.md#mem-rte-findings-resume
          note: Code supplies selected prior results to peer/main/PoC context; a configured stage request
            does not make automatic prompt inclusion a file pull.
        records: *id036
        note: Code supplies selected prior results to peer/main/PoC context; a configured stage request
          does not make automatic prompt inclusion a file pull.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: Constructing an ADK memory service does not establish retrieval; live/provider/trainer and
          custom-extension later routes remain uninspected.
      records:
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-obj-todo
      - memory.md#mem-obj-tool-output
      - memory.md#mem-rte-finding-admission
      - memory.md#mem-rte-checkpoint-resume
      - runtime.md#rt-rte-directed-child
      - memory.md#mem-rte-history-consultation
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-rte-image-retention
      - epistemic.md#epi-rte-finding-delivery
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-findings-resume
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      note: Both requested retrieval and automatic supply occur in distinct operations. Opaque alternatives
        prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Later history fold selects compaction markers and original events
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id037
          - memory.md#mem-obj-compacted-content
          - runtime.md#rt-rte-history-compaction
          note: Later context construction uses timestamp-range/ordering and branch/invocation matching
            to select delivered retained parts; range selection is separate from identity matching.
        - value: identifier
          basis: wired
          records: *id037
          note: Later context construction uses timestamp-range/ordering and branch/invocation matching
            to select delivered retained parts; range selection is separate from identity matching.
        records: *id037
        note: Later context construction uses timestamp-range/ordering and branch/invocation matching
          to select delivered retained parts; range selection is separate from identity matching.
      - scope: Successful compaction appends current pinned file and output/history plugins supply retained
          context
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id038
          - memory.md#mem-obj-pinned
          - memory.md#mem-rte-output-reduction
          - memory.md#mem-rte-hook-retention
          - memory.md#mem-rte-image-retention
          note: Triggers are successful compaction, eligible tool result/later history, hook matcher/queued
            content and image request construction. Availability, nonempty text, length and image-size
            budgets select retained parts; file IDs alone are not targeted push.
        records: *id038
        note: Triggers are successful compaction, eligible tool result/later history, hook matcher/queued
          content and image request construction. Availability, nonempty text, length and image-size budgets
          select retained parts; file IDs alone are not targeted push.
      - scope: Tool-summary model selects retained context according to inferred task intent
        assessment: known
        findings:
        - value: inferred-judgment
          basis: wired
          records: &id039
          - memory.md#mem-rte-output-reduction
          note: Threshold triggers summarization; recent retained events and tool arguments supply inferred
            intent for selected summary content; deterministic prefix branch remains coarse.
        records: *id039
        note: Threshold triggers summarization; recent retained events and tool arguments supply inferred
          intent for selected summary content; deterministic prefix branch remains coarse.
      - scope: Finding peer broadcast and benchmark handoff selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id040
          - epistemic.md#epi-rte-finding-delivery
          - memory.md#mem-rte-explore-handoff
          - memory.md#mem-rte-findings-resume
          note: Nonduplicate branch broadcasts to all peers; enabled explore selects final/fallback text;
            resume/nonempty findings supplies structured content. No semantic ranking or matched content
            identity is established.
        records: *id040
        note: Nonduplicate branch broadcasts to all peers; enabled explore selects final/fallback text;
          resume/nonempty findings supplies structured content. No semantic ranking or matched content
          identity is established.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: Selectors for opaque service/live/provider/trainer/extension pushes are uninspected. Pull
          file names or checkpoint IDs do not establish identifier-based push.
      records:
      - memory.md#mem-obj-compacted-content
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-obj-pinned
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-rte-image-retention
      - epistemic.md#epi-rte-finding-delivery
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-findings-resume
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      note: Push signals have local triggers and retained targets. No inferred lexical/embedding signal
        is supported, but missing inspection is not their absence.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic history summary retained in compaction events and delivered on subsequent folded-history
          invocation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id041
          - runtime.md#rt-rte-history-compaction
          - memory.md#mem-obj-compacted-content
          - memory.md#mem-bap-summary-authority
          note: User/model/tool traces produce durable continuation context; later-consumer wiring establishes
            the axis without observed improvement.
        records: *id041
        note: User/model/tool traces produce durable continuation context; later-consumer wiring establishes
          the axis without observed improvement.
      - scope: Automatic tool-response summary/prefix retained in events and consumed by later model/history
          consultation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id042
          - memory.md#mem-rte-output-reduction
          - memory.md#mem-obj-tool-summary
          - memory.md#mem-rte-history-consultation
          note: Tool execution feedback plus recent session history produces retained context, including
            deterministic preview alternatives.
        records: *id042
        note: Tool execution feedback plus recent session history produces retained context, including
          deterministic preview alternatives.
      - scope: Explore quota-exception trace-to-summary-to-main-agent chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id043
          - memory.md#mem-rte-explore-handoff
          note: Recorded exploration turns/tool responses feed automatic summary construction, prompt
            admission and later main-agent consumption.
        records: *id043
        note: Recorded exploration turns/tool responses feed automatic summary construction, prompt admission
          and later main-agent consumption.
      - scope: Wiki/pin authored entries, finding comparison, hooks/images, raw checkpoints/exports and
          ordinary final-text handoffs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-finding-admission
        - memory.md#mem-rte-hook-retention
        - memory.md#mem-rte-image-retention
        - memory.md#mem-rte-checkpoint-resume
        - memory.md#mem-rte-explore-handoff
        - runtime.md#rt-rte-evaluation-rollout
        note: Use-derived content or raw retention alone does not establish a trace-fed transformation
          into behavior-shaping material for every branch; actual content origins and downstream updates
          are unresolved. No bounded absence record licenses no.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: External parameter updates, live retention and extension-specific trace-fed routes remain
          uninspected.
      records:
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-obj-compacted-content
      - memory.md#mem-bap-summary-authority
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-obj-tool-summary
      - memory.md#mem-rte-history-consultation
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-rte-finding-admission
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-rte-image-retention
      - memory.md#mem-rte-checkpoint-resume
      - runtime.md#rt-rte-evaluation-rollout
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      note: Qualifying summary routes establish yes locally, not improved capacity or a complete learning
        inventory. Unresolved routes are not converted into no.
    trace_source:
      assessment: partial
      units:
      - scope: History-compaction original window
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id044
          - memory.md#mem-obj-compacted-content
          - runtime.md#rt-rte-history-compaction
          note: Recorded user/model turns and tool calls/responses are rendered into the qualifying summary
            request; serialization as events adds no event-stream source.
        - value: tool-traces
          basis: wired
          records: *id044
          note: Recorded user/model turns and tool calls/responses are rendered into the qualifying summary
            request; serialization as events adds no event-stream source.
        records: *id044
        note: Recorded user/model turns and tool calls/responses are rendered into the qualifying summary
          request; serialization as events adds no event-stream source.
      - scope: Tool-reduction model branch
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id045
          - memory.md#mem-rte-output-reduction
          note: Original tool result and recent conversational events inform the durable derived response.
        - value: session-logs
          basis: wired
          records: *id045
          note: Original tool result and recent conversational events inform the durable derived response.
        records: *id045
        note: Original tool result and recent conversational events inform the durable derived response.
      - scope: Tool-reduction deterministic preview branch
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id046
          - memory.md#mem-rte-output-reduction
          note: Prefix extraction consumes the raw tool response; it does not consume recent history through
            a model summary.
        records: *id046
        note: Prefix extraction consumes the raw tool response; it does not consume recent history through
          a model summary.
      - scope: Explore quota fallback
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id047
          - memory.md#mem-rte-explore-handoff
          note: Selected recorded text, arguments and tool responses from exploration feed the summary
            delivered to the main agent.
        - value: tool-traces
          basis: wired
          records: *id047
          note: Selected recorded text, arguments and tool responses from exploration feed the summary
            delivered to the main agent.
        records: *id047
        note: Selected recorded text, arguments and tool responses from exploration feed the summary delivered
          to the main agent.
      - scope: Potential trace-fed wiki/findings/hook/benchmark content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-finding-admission
        - memory.md#mem-rte-hook-retention
        - memory.md#mem-rte-findings-resume
        note: These branches lack complete qualifying-update/original-input facts. A timestamp or callback
          label does not prove event-streams; successive turns alone do not prove trajectories.
      - scope: Included ADK service/provider state, live retention, external trainer and extension-specific
          alternatives
        assessment: uninspected
        findings: []
        records: *id011
        note: External training input provenance and additional extension/live write sources are uninspected.
      records:
      - memory.md#mem-obj-compacted-content
      - runtime.md#rt-rte-history-compaction
      - memory.md#mem-rte-output-reduction
      - memory.md#mem-rte-explore-handoff
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-rte-finding-admission
      - memory.md#mem-rte-hook-retention
      - memory.md#mem-rte-findings-resume
      - memory.md#mem-cmp-memory-service
      - runtime.md#rt-rte-live-runner
      - runtime.md#rt-rte-evaluation-rollout
      note: Every established summary learning route retains its mixed original inputs. No system-wide
        inapplicability or exhaustive trace-source union is justified.
---

# OpenSage memory profile

## Comparison rationale

All ten axes are partial. Positive file/context routes do not close the inventory of service payloads, live retention, trainer updates or extension-specific alternatives. A missing deployed run limits observation and benefit, not the wired summary routes. The profile classifies the accepted records only; no target source was read.

Reconciliation supersedes the epistemic shared-findings object and reduced-response object with [MEM-OBJ-findings](memory.md#mem-obj-findings) and [MEM-OBJ-tool-summary](memory.md#mem-obj-tool-summary), and its reduction route with [MEM-RTE-output-reduction](memory.md#mem-rte-output-reduction). Those canonical citations govern the corresponding values. The finding check/write/delivery records remain distinct functions, so their internal wired evidence does not upgrade the afforded shipped invocation of [MEM-RTE-finding-admission](memory.md#mem-rte-finding-admission).

Compaction and tool reduction are consolidation even when originals remain on disk or semantic fidelity fails. The summary-update consumers receive recorded experience; later agents receive derived context. This supports learning authority at the update consumer and knowledge at the later model, without proving improved capacity. The qualifying trace-learning chain is automatic trace-fed production, retention and later invocation, not merely checkpointing or exporting raw logs. [MEM-OBJ-compacted-content](memory.md#mem-obj-compacted-content) retains non-cumulative range replacement and unchecked rationale preservation; these limits remain beside the wired positive.

Read-back direction describes operations, not an entire chain. Requested resume/history consultation is pull; later automatic history folding and benchmark prompt inclusion are push. The branch/range selector in [MEM-OBJ-compacted-content](memory.md#mem-obj-compacted-content) supports identifier and coarse signals separately. A requested checkpoint path or a saved-output file ID does not independently support targeted push. The binary payload in [MEM-OBJ-image-parts](memory.md#mem-obj-image-parts) remains unclassified by form. The symbolic MIME/part wrapper and natural-language rejection notice occupy separate known units: [MEM-RTE-image-retention](memory.md#mem-rte-image-retention) establishes the notice's interpreted request to resubmit smaller images. Neither unit classifies the binary payload.

Policy-requested wiki revision/removal stays claimed. [EPI-RTE-finding-write](epistemic.md#epi-rte-finding-write) implements duplicate suppression, not withdrawal of an older contradicted claim or truth acceptance. Retained previous findings supply validation and an enforced admission veto, while broadcast supplies advice. Structural checkpoint parsing and image request filtering do not automatically imply retained validation criteria or curation.

Retained benchmark grades and scores have downstream reporting/ranking consumers, distinct from ordinary agent memory and from trainer learning. [WF-RTE-devops-grading](workflow.md#wf-rte-devops-grading) reads stored grades into aggregate lists without sending failure back for policy revision. External checkpoint selection and parameter updates remain uninspected in [RT-RTE-evaluation-rollout](runtime.md#rt-rte-evaluation-rollout). Static root policy and ordinary provider inference weights are not counted as accumulated memory.

The partial lineage inventory does not enumerate the caller-finding and appended-analysis derivations in [MEM-OBJ-findings](memory.md#mem-obj-findings) and [EPI-RTE-finding-write](epistemic.md#epi-rte-finding-write), or the model-generation/parsing/serialization path in [MEM-OBJ-vulnerability-findings](memory.md#mem-obj-vulnerability-findings) and [MEM-RTE-findings-resume](memory.md#mem-rte-findings-resume). Withhold object-complete lineage comparisons for these parts; the emitted witnesses do not establish that coverage.
