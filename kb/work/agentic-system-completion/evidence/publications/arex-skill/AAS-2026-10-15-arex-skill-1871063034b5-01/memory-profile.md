---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "AREX-Skill memory comparison of use-changed guidance, session checkpoints, workflow retention and evidence at the partial-loop boundary."
run-id: "AAS-2026-10-15-arex-skill-1871063034b5-01"
source-identity: "https://github.com/VectorSpaceLab/AREX-Skill"
reviewed-boundary: "ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6"
memory-comparison:
  version: 2
  scope: "Use-accumulated or changed installed operating graphs and access structures; session branches, compaction and branch summaries; workflow journals, diagnostic histories and saved scripts; retained verification/recovery artifacts and their consumers. Includes unresolved extension replacements, specialized construction/import/export and task-oriented update/consumer paths, and filesystem instructions only insofar as changed through use. Excludes unchanged shipped instructions, ordinary unretained current-run state, provider inference weights without a recorded use-driven update route, and uncaptured external-host deployments."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Installed or updated graph files, library access state and discovery projection"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operating-graph"
                - "runtime.md#rt-rte-graph-admission"
                - "runtime.md#rt-rte-library-update"
                - "memory.md#mem-obj-library-state"
              note: "Installed content and persisted access metadata are filesystem objects."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-skill-registry"
              note: "The eligible array is the access projection of retained skill files, not another durable graph store."
          records:
            - "runtime.md#rt-obj-operating-graph"
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "Recorded retained files and their in-process access structure are classified; initial shipped content is not treated as use-derived memory."
        -
          scope: "Session branches, default summaries and their reconstructed context"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
              note: "Persisted session entries retain messages and checkpoints."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
              note: "The same session abstraction supports in-memory storage and reconstructed messages."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Session files and the explicitly supported in-memory session alternative are both retained-object substrates."
        -
          scope: "Workflow journals, diagnostic snapshots and saved orchestration"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
                - "memory.md#mem-obj-agent-history"
              note: "Run JSON, diagnostic snapshots in persisted state and saved workflow JSON are filesystem retention."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-history"
              note: "Diagnostic callback snapshots are also held in workflow agent state."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "memory.md#mem-obj-agent-history"
          note: "JSON is encoding, not an extra substrate; diagnostic callback snapshots coexist with persisted state."
        -
          scope: "Retained verification and recovery evidence and reports"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Run-directory evidence and check/report outputs are retained files."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "Recorded report and evidence paths establish file storage, not authenticity."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "No recorded complete inventory covers all material write products or extension-specific state; no additional substrate or complete union can be established."
      records:
        - "runtime.md#rt-obj-operating-graph"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-library-update"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "memory.md#mem-obj-agent-history"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Positive file and in-process witnesses do not exhaust the partial-loop artifact. Provider inference parameters are outside this use-changed memory boundary, not classified as absent model-weight memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Installed guidance prose and description fields consumed by the model"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operating-graph"
                - "runtime.md#rt-rte-graph-admission"
                - "runtime.md#rt-rte-library-update"
                - "epistemic.md#epi-obj-skill-assertions"
                - "epistemic.md#epi-obj-skill-policy"
              note: "The model interprets operating assertions, imperatives and descriptions."
          records:
            - "runtime.md#rt-obj-operating-graph"
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
            - "epistemic.md#epi-obj-skill-assertions"
            - "epistemic.md#epi-obj-skill-policy"
          note: "Factual clauses and imperatives share natural-language form, not epistemic force."
        -
          scope: "Graph structure/scripts and library/registry metadata at fixed-rule consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operating-graph"
                - "runtime.md#rt-rte-graph-admission"
                - "runtime.md#rt-rte-library-update"
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-obj-skill-registry"
                - "runtime.md#rt-rte-skill-delivery"
              note: "Validators, discovery rules and script interpreters consume localized fields or executable syntax."
          records:
            - "runtime.md#rt-obj-operating-graph"
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "Frontmatter, links, flags and executable scripts are separate from interpreted prose."
        -
          scope: "Session messages and default checkpoint prose at later model calls"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
                - "memory.md#mem-bap-summary-context"
              note: "Reconstruction delivers messages and checkpoint text as model context."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
            - "memory.md#mem-bap-summary-context"
          note: "This unit covers readable textual parts only; symbolic branch controls are separate."
        -
          scope: "Session tree, retention boundaries and file-tracking metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Fixed reconstruction and file-tracking rules consume these localized fields."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Entry IDs and boundary/details fields used by reconstruction or later compaction are symbolic."
        -
          scope: "Journal index/hash envelope"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "Index, hash and prefix checks select a journal value."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "The replay envelope is distinct from its arbitrary result payload."
        -
          scope: "Journal result payload"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "A child may return textual output retained for replay."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "Text results are supported; arbitrary schema-shaped results are also admitted, and their semantics/form are not established by JSON."
        -
          scope: "Saved script/parameter fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
              note: "JavaScript and parameter metadata direct fixed-rule orchestration."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "The later executor consumes script, not just its display description."
        -
          scope: "Saved workflow description and diagnostic readable text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
                - "memory.md#mem-obj-agent-history"
              note: "Descriptions and diagnostic excerpts are readable prose."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "memory.md#mem-obj-agent-history"
          note: "Description and truncated diagnostic text are distinct from executable scripts and replay payloads."
        -
          scope: "Diagnostic role/kind/tool flags and recovery evidence fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-history"
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Diagnostic flags and evidence metrics/check results are localized symbolic fields."
          records:
            - "memory.md#mem-obj-agent-history"
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "Programmatic fields are separated from explanatory text."
        -
          scope: "Recovery evidence explanations and report prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Explanations and Markdown reporting are interpreted text."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "The bundle mixes structured fields and interpreted explanations."
        -
          scope: "Extension-supplied summary/details alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Readable summaries do not resolve the form of opaque details or alternative extension payloads."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Uninspected content and consumers prevent complete form enumeration; no parametric retained-memory finding follows from a provider being used."
      records:
        - "runtime.md#rt-obj-operating-graph"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-library-update"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "epistemic.md#epi-obj-skill-assertions"
        - "epistemic.md#epi-obj-skill-policy"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "memory.md#mem-obj-agent-history"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Mixed envelopes are split by operative part and consumer. Opaque journal data and extension details remain unresolved rather than being called symbolic solely because they serialize as JSON."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Creator construction of new operating guidance"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-graph-admission"
              note: "Creator instructions request grounded drafting of operating guidance."
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "epistemic.md#epi-obj-skill-policy"
            - "epistemic.md#epi-obj-skill-assertions"
          note: "Model drafting is requested, but particular graph inputs, transformations and initial provenance were not authenticated."
        -
          scope: "Published collection admission into managed storage"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-library-update"
              note: "The updater admits a selected upstream collection snapshot."
          records:
            - "runtime.md#rt-rte-library-update"
          note: "This is the local import derivation path, not a reconstruction of upstream authorship."
        -
          scope: "Default compaction and branch summary derivation"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Messages and tool activity are selected and summarized into later context."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Recorded default derivations consume session experience, including previous summaries; extension alternatives remain separate."
        -
          scope: "Session event retention and compact child diagnostic history"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-history"
              note: "The diagnostic formatter extracts bounded text/tool events from child activity."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-agent-history"
          note: "Session activity is recorded/extracted, but imported initial turns and every original author are not established."
        -
          scope: "Library inventory/digests and discovery projection"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-obj-skill-registry"
                - "runtime.md#rt-rte-skill-delivery"
              note: "Software derives inventory, digests and eligible listing from installed content."
          records:
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "This unit concerns derived access metadata, not original content authorship."
        -
          scope: "Saved workflow copied from a selected run"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
              note: "The selected run script is copied into reusable workflow storage."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "The save operation copies an existing script; original model/caller authorship and generic API input provenance remain unresolved."
        -
          scope: "Journal result origins and extension replacement provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Successful child results, defaults, human replies and arbitrary extension replacements have different possible origins; the records do not establish a uniform derivation for their consumed content."
        -
          scope: "Check outputs and final-report derivation"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Deterministic check results and final reports are computed/grouped from supplied artifacts."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "Implemented outputs derive from supplied case/evidence data, but original metric, gold-label and evidence provenance remains unauthenticated."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Initial graph provenance, specialized builders, benchmark paths and use-driven instruction edits remain uninspected; no complete lineage union is warranted."
      records:
        - "runtime.md#rt-rte-graph-admission"
        - "epistemic.md#epi-obj-skill-policy"
        - "epistemic.md#epi-obj-skill-assertions"
        - "runtime.md#rt-rte-library-update"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-obj-agent-history"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Local derivation paths do not resolve initial provenance. Authored guidance is retained at its claimed procedural layer; executable import does not upgrade that construction claim."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Installed imperative guidance at a later Researcher model"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-skill-policy"
                - "runtime.md#rt-bap-operating-guidance"
              note: "Operating procedures direct later task behavior."
          records:
            - "epistemic.md#epi-obj-skill-policy"
            - "runtime.md#rt-bap-operating-guidance"
          note: "Delivery gives interpreted standing directions, not enforcement of model compliance."
        -
          scope: "Installed factual clauses at the later model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-skill-assertions"
                - "runtime.md#rt-bap-operating-guidance"
              note: "Capability and prerequisite assertions inform task work."
          records:
            - "epistemic.md#epi-obj-skill-assertions"
            - "runtime.md#rt-bap-operating-guidance"
          note: "Assertions supply reference context without independent certification."
        -
          scope: "Saved orchestration script at the workflow executor"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
                - "runtime.md#rt-bap-operating-guidance"
              note: "Saved JavaScript controls workflow calls and orchestration choices. No authority value is inferred for an arbitrary graph script merely because it can execute."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "runtime.md#rt-obj-operating-graph"
            - "runtime.md#rt-bap-operating-guidance"
          note: "The recorded saved script controls workflow operations when invoked, not merely natural-language advice; individual graph-script effects remain uninspected."
        -
          scope: "Library access metadata at discovery and conflict consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-obj-skill-registry"
                - "runtime.md#rt-rte-skill-delivery"
              note: "Roles and visibility metadata select discovery scope and listing."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-rte-library-update"
              note: "Retained inventory and digests determine consistency/conflict acceptance."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-rte-library-update"
              note: "Conflict/digest failure vetoes the managed update; disabled invocation metadata excludes automatic listing."
          records:
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
            - "runtime.md#rt-rte-library-update"
          note: "Each finding names a distinct effect; constraints apply only to their recorded helper paths."
        -
          scope: "Raw messages and previous summaries at default summarization"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Trace material and prior checkpoints feed automatic durable summary updates."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Learning authority belongs to retained experience at its update consumer, separately from the output context authority."
        -
          scope: "Summary prose at subsequent model invocations"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-summary-context"
              note: "Summary text supplies prior decisions, progress and contextual information."
          records:
            - "memory.md#mem-bap-summary-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
          note: "The record establishes interpreted continuation context, not a semantic truth gate or proved reliance."
        -
          scope: "Session IDs and retention boundaries at context reconstruction"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-branch-summary"
              note: "Active leaf and compaction boundary select reconstructed entries."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-branch-summary"
          note: "Metadata chooses the input window rather than supplying factual warrant."
        -
          scope: "Journal hashes/index at replay selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "Index/hash/prefix state selects the returned retained value."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "The envelope selects live computation versus cached delivery."
        -
          scope: "Journal result at workflow-code consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "Replay delivers an arbitrary value; its schema or textual display does not establish whether the later code uses it as knowledge, routing, validation or another force."
        -
          scope: "Retained paper evidence at checks and disposition"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
              note: "Recorded targets, evidence fields and check booleans determine bounded recovery admissibility."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-final-report"
              note: "Saved command reports and final reports inform verifier/operator review."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "Checks consume supplied criteria/results; this is not a global graph-write gate."
        -
          scope: "Retained recovery feedback at proposed policy revision"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-obj-skill-policy"
              note: "The Creator is requested to use recovery feedback to revise durable workflow guidance."
          records:
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-obj-skill-policy"
          note: "Feedback-directed revision is doctrine, not observed semantic repair."
        -
          scope: "Diagnostic history at later consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-agent-history"
          note: "Diagnostics are persisted, but full UI/external consumers were not traced and no model read-back was established."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Uninspected extension consumers, individual scripts and specialized loops prevent complete authority classification; no ranking force is inferred merely from a description being available."
      records:
        - "epistemic.md#epi-obj-skill-policy"
        - "runtime.md#rt-bap-operating-guidance"
        - "epistemic.md#epi-obj-skill-assertions"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "runtime.md#rt-obj-operating-graph"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "runtime.md#rt-rte-library-update"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "memory.md#mem-obj-agent-history"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Authority is attached to the actual consumed part. Update learning, downstream knowledge/instruction, metadata routing and helper vetoes are independent paths, not a single system force."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Default compaction and branch-summary admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Software admits completed model summaries after cancellation/error checks."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "A human/client trigger or custom focus is not per-content approval of the generated summary."
        -
          scope: "Child journal, headless checkpoints, diagnostic snapshots and managed inventory admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
                - "memory.md#mem-obj-agent-history"
                - "runtime.md#rt-rte-library-update"
                - "memory.md#mem-obj-library-state"
              note: "Successful results/defaults, formatted history and inventory transformations are admitted by code."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
            - "memory.md#mem-obj-agent-history"
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
          note: "No explicit per-content human decision is required for these software admissions."
        -
          scope: "Interactive checkpoint reply admission"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "A human confirmation supplies the retained checkpoint reply."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "This unit is only the confirmation-callback branch, not headless defaults."
        -
          scope: "Command/UI save of a selected run script"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
              note: "The operator chooses a particular run/name for reusable retention."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "The explicit human selection supplies the content to retain, independently of original script authorship."
        -
          scope: "Generic save API and direct content writers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "runtime.md#rt-rte-graph-admission"
          note: "Generic caller identity and physical file writing do not establish a human content-selection decision."
        -
          scope: "Creator exact-spec/import/overwrite approvals"
          assessment: "partial"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-graph-admission"
              note: "The procedure requests exact-specification and separate import/overwrite approval."
          records:
            - "runtime.md#rt-rte-graph-admission"
          note: "Human content/destination approval is requested by doctrine, while the importer cannot authenticate an approver; bypass file writes remain separate."
        -
          scope: "Paper check/report output admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Helpers compute and persist result/report content without a per-result human approval gate."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "Starting a check is not deciding each output field."
        -
          scope: "Extension summary replacement control"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Extensions can replace content or cancel; their internal admission principal and content control are not recorded."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Initial instruction admission, specialized builders/importers and task-oriented content decisions remain uninspected; no human approval is inferred from a caller flag."
      records:
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-agent-history"
        - "runtime.md#rt-rte-library-update"
        - "memory.md#mem-obj-library-state"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "runtime.md#rt-rte-graph-admission"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Manual and automatic findings coexist at distinct admission mechanisms. Software I/O alone does not make a human-selected saved script automatic, and workflow initiation does not make generated summaries manual."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Default compaction and branch-summary transformations"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Selected session experience is compressed into continuation/exploration summaries."
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
              note: "Incremental compaction reads a previous summary and produces its updated checkpoint."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Classification follows selection/compression and incremental checkpoint rewriting, not claims of semantic faithfulness."
        -
          scope: "Diagnostic history reduction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-history"
              note: "The formatter keeps a reduced recent diagnostic representation, omitting thinking/nontext material."
          records:
            - "memory.md#mem-obj-agent-history"
          note: "Bounded extraction/truncation reduces retained session activity without establishing knowledge acceptance."
        -
          scope: "Managed collection replacement and withdrawal from future discovery"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-library-update"
              note: "Update replaces installed official content with a new inventory version."
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-library-update"
              note: "Previously managed entries absent from the new inventory are physically removed from the staged/live collection."
          records:
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
          note: "Removal from the operative collection is forgetting there, not retroactive removal of already supplied context."
        -
          scope: "Saved workflow overwrite"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
              note: "The save API overwrites the named retained workflow."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "An existing reusable script can be replaced by name; save is not automatic extraction of an improved program."
        -
          scope: "Paper-guidance feedback refinement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-paper-decision"
              note: "Refine feedback requests revision of relevant workflow guidance and module skills."
          records:
            - "epistemic.md#epi-rte-paper-decision"
          note: "The revision operation is requested, not an implemented semantic repair controller."
        -
          scope: "Opaque extension transformations and journal payload maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "Replacement content and cached-result semantics are not established; index rebuilding, hashing and collision checks alone do not establish curation."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Uninspected maintenance and graph content prevent complete enumeration; no dedup, promote, invalidate or synthesize finding follows from route names or structural validation alone."
      records:
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-obj-agent-history"
        - "runtime.md#rt-rte-library-update"
        - "memory.md#mem-obj-library-state"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "epistemic.md#epi-rte-paper-decision"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Deletion from an operative collection supplies local decay; incidental transaction backups do not establish a history-retaining invalidation design. No synthesis is inferred from possible summary errors or opaque model output."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested installed-skill bodies and explicit expansion"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-delivery"
              note: "Model read requests and explicit named skill commands request retained bodies."
          records:
            - "runtime.md#rt-rte-skill-delivery"
            - "runtime.md#rt-bap-operating-guidance"
          note: "This unit concerns newly admitted/updated material in later sessions, not shipped static instructions."
        -
          scope: "Automatically supplied eligible registry for installed/updated guidance"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-obj-skill-registry"
                - "runtime.md#rt-rte-skill-delivery"
              note: "Discovery supplies eligible names/descriptions/locations automatically."
          records:
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "The model need not request the descriptions supplied at prompt construction."
        -
          scope: "Requested saved session/branch reconstruction"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-foreground-task"
                - "runtime.md#rt-obj-session-context"
              note: "Caller selection of saved session/branch requests its reconstructed context."
          records:
            - "runtime.md#rt-rte-foreground-task"
            - "runtime.md#rt-obj-session-context"
          note: "Requested resumption is not counted as a second push merely because code returns messages."
        -
          scope: "Checkpoint injection on continuation and branch transfer"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
                - "memory.md#mem-bap-summary-context"
              note: "Host reconstruction supplies selected summaries and retained tail to later model calls."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
            - "memory.md#mem-bap-summary-context"
          note: "Within the continuation chain the next model does not request the particular retained summary."
        -
          scope: "Resume-journal request and automatic cache substitution"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "Resume explicitly loads saved script/args/journal."
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "The automatic index/hash/prefix selector supplies a prior value at a matching call."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "Explicit resume requests retained run state; call matching subsequently supplies a cached result instead of a fresh child/checkpoint."
        -
          scope: "Named saved-workflow invocation"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-saved-workflow"
                - "memory.md#mem-rte-saved-workflow"
              note: "Command invocation or named nested workflow requests the retained script."
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "Name lookup fulfills the command/nesting request rather than unsolicited script selection."
        -
          scope: "Saved paper evidence consumed by checks and final reporting"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-recovery-evidence"
                - "epistemic.md#epi-rte-native-checks"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-final-report"
              note: "Check/comparison/report consumers load supplied run-directory artifact paths."
          records:
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "The helper invocation requests the relevant saved evidence, not unsolicited model memory retrieval."
        -
          scope: "Diagnostic history and use-changed context-file alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-agent-history"
            - "memory.md#mem-obj-context-files"
          note: "No complete later diagnostic consumer or demonstrated use-driven context-file update chain was assessed."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Specialized later consumers and extension-specific delivery remain uninspected; known pull routes do not resolve those alternatives."
      records:
        - "runtime.md#rt-rte-skill-delivery"
        - "runtime.md#rt-bap-operating-guidance"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-foreground-task"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "memory.md#mem-obj-agent-history"
        - "memory.md#mem-obj-context-files"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-workflow-agent"
      note: "Directions classify operations within chains: a requested return remains pull, while an independent summary or cache selector can supply push. Static loading alone is excluded from use-derived read-back."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Automatic listing of eligible installed/updated skill metadata"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-library-state"
                - "runtime.md#rt-obj-skill-registry"
                - "runtime.md#rt-rte-skill-delivery"
              note: "Role and visibility availability filters choose a broad eligible listing, not semantic targeted retrieval."
          records:
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "Trigger: prompt/resource construction. Inputs: installed registry, mode/role and invocation visibility. Selected part: eligible descriptions/locations."
        -
          scope: "Checkpoint/tail supply at later model invocation"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-branch-summary"
              note: "Actual leaf/entry-ID boundary matches determine the reconstructed retained parts."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
              note: "Recent-tail and window/reserve budgets select retained material without semantic matching."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Trigger: continuation/reconstruction after compaction or branch transfer. Inputs: selected leaf, checkpoint first-kept identity and retention budgets. Selected part: checkpoint plus kept branch entries."
        -
          scope: "Automatic workflow-journal cache hit"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-journal-replay"
              note: "Actual index/hash equality selects the journal value delivered to workflow code."
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
          note: "Trigger: an agent/checkpoint call in resumed execution. Inputs: call index/hash and first-miss boundary. Selected part: the matching stored result."
        -
          scope: "Requested skill-body, named-workflow and evidence-file returns considered alone"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-delivery"
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "epistemic.md#epi-obj-recovery-evidence"
            - "epistemic.md#epi-rte-native-checks"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-final-report"
          note: "These operations fulfill requests; an address on a requested file does not establish identifier-based push. Their separate upstream push operations are classified above."
        -
          scope: "Other included push selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-files"
            - "runtime.md#rt-rte-workflow-agent"
          note: "Use-changed filesystem instructions, arbitrary extensions and specialized loops lack a complete retained-part selector account."
      records:
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "epistemic.md#epi-obj-recovery-evidence"
        - "epistemic.md#epi-rte-native-checks"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-final-report"
        - "memory.md#mem-obj-context-files"
        - "runtime.md#rt-rte-workflow-agent"
      note: "Positive coarse and identifier selectors are local. Semantic skill matching leads to a requested read, not automatically inferred-judgment push; neither embedding nor lexical push is established. Uninspected alternatives prevent complete signal coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Default compaction checkpoint and branch exploration summary"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
                - "memory.md#mem-bap-summary-context"
              note: "Automatic summaries are retained behavior-shaping continuation artifacts."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
            - "memory.md#mem-bap-summary-context"
          note: "The route qualifies architecturally even without observed improvement: traces feed automatic durable summaries delivered to later model invocations."
        -
          scope: "Extension-supplied summary alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "A replacement summary can be supplied, but its original trace input and production process remain opaque; the default writer cannot upgrade this branch."
        -
          scope: "Workflow journal and diagnostic retention"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
            - "memory.md#mem-obj-agent-history"
          note: "Raw logging alone is insufficient. The journal later supplies arbitrary workflow-code inputs, but their durable behavior-shaping semantics and the diagnostic later-consumer route are not established."
        -
          scope: "Paper feedback-directed skill refinement"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-obj-skill-policy"
                - "runtime.md#rt-bap-operating-guidance"
              note: "Doctrine requests model revision of durable workflow guidance from recovery feedback for later task use."
          records:
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-obj-skill-policy"
            - "runtime.md#rt-bap-operating-guidance"
          note: "A requested feedback-to-guidance update can qualify, but original feedback provenance, automatic versus approval-controlled admission and exercised later use are not fully recorded."
        -
          scope: "Saved orchestration, imported guidance and access metadata routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
            - "runtime.md#rt-obj-operating-graph"
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-library-update"
            - "memory.md#mem-obj-library-state"
            - "runtime.md#rt-obj-skill-registry"
            - "runtime.md#rt-rte-skill-delivery"
          note: "Saving a selected script, installing a source snapshot and computing metadata do not alone establish an automatic trace-fed behavior-shaping write; original construction/update provenance remains unresolved."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Individual graph histories, specialized builders, benchmark loops and use-driven instruction edits prevent a system-wide negative or complete qualifying-route inventory."
      records:
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-agent-history"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-obj-skill-policy"
        - "runtime.md#rt-bap-operating-guidance"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "runtime.md#rt-obj-operating-graph"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-library-update"
        - "memory.md#mem-obj-library-state"
        - "runtime.md#rt-obj-skill-registry"
        - "runtime.md#rt-rte-skill-delivery"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "The wired positive is summary continuation, not demonstrated improved capacity or exercised self-improvement. No local no is asserted without bounded absence records; opaque and uninspected alternatives remain visible."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Default compaction and branch-summary original inputs"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "User and assistant conversational turns feed summary production."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-session-context"
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-obj-branch-summary"
                - "memory.md#mem-rte-branch-summary"
                - "runtime.md#rt-rte-context-compaction"
              note: "Recorded tool requests, arguments, results and execution feedback also feed selected summary input."
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "Classification follows recorded content: conversational turns and tool requests/results, not the event-tree serialization label."
        -
          scope: "Extension-provided replacement checkpoint inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-session-context"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-obj-branch-summary"
            - "memory.md#mem-rte-branch-summary"
            - "runtime.md#rt-rte-context-compaction"
          note: "The consumed readable summary and opaque details do not establish the original source of the replacement writer."
        -
          scope: "Paper feedback-guidance refinement input"
          assessment: "partial"
          findings:
            -
              value: "tool-traces"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-paper-decision"
                - "epistemic.md#epi-rte-paper-checks"
                - "epistemic.md#epi-rte-native-checks"
              note: "The requested refinement uses validation/recovery execution feedback to revise durable guidance."
          records:
            - "epistemic.md#epi-rte-paper-decision"
            - "epistemic.md#epi-rte-paper-checks"
            - "epistemic.md#epi-rte-native-checks"
          note: "Execution checks and recovery feedback are requested inputs to revision; other plan/source/metric inputs are mixed and their original experiential provenance is not fully established."
        -
          scope: "Journal/diagnostic and saved-script qualifying-source alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-journal-replay"
            - "memory.md#mem-obj-agent-history"
            - "memory.md#mem-obj-saved-workflow"
            - "memory.md#mem-rte-saved-workflow"
          note: "These contain activity or script data, but the qualifying automatic learning route is unresolved; no trace source is assigned solely from their presence."
        -
          scope: "Included specialized import/export, individual graph and task-oriented update paths, use-changed filesystem instructions and extension-specific alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-graph-admission"
            - "runtime.md#rt-rte-workflow-agent"
            - "memory.md#mem-obj-context-files"
          note: "Uninspected trace-fed write alternatives prevent complete original-source coverage. No event-stream or trajectory value is inferred merely from event entries or workflow sequences."
      records:
        - "runtime.md#rt-obj-session-context"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-branch-summary"
        - "memory.md#mem-rte-branch-summary"
        - "runtime.md#rt-rte-context-compaction"
        - "epistemic.md#epi-rte-paper-decision"
        - "epistemic.md#epi-rte-paper-checks"
        - "epistemic.md#epi-rte-native-checks"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-journal-replay"
        - "memory.md#mem-obj-agent-history"
        - "memory.md#mem-obj-saved-workflow"
        - "memory.md#mem-rte-saved-workflow"
        - "runtime.md#rt-rte-graph-admission"
        - "runtime.md#rt-rte-workflow-agent"
        - "memory.md#mem-obj-context-files"
      note: "Session-logs and tool-traces are supported for the default summary writer. An unresolved alternative is not inapplicable merely because another route is known; no complete absence of other qualifying sources is established."
---

# AREX-Skill memory profile

## Comparison rationale

The accepted records support a concrete automatic trace-fed summary route, alongside imported instructions, human-selected reusable scripts and executable access metadata. These are different memory products. [MEM-OBJ-compaction](memory.md#mem-obj-compaction), [MEM-RTE-branch-summary](memory.md#mem-rte-branch-summary) and [MEM-BAP-summary-context](memory.md#mem-bap-summary-context) supply the raw-to-derived-to-later-model chain. Summary compression need not create new knowledge or preserve every reason to qualify as trace learning. This architectural finding does not establish exercised learning or improved performance.

Every axis remains partial. The inventory includes opaque alternatives rather than silently restricting the scope to the strongest default witness. In particular, [MEM-OBJ-journal](memory.md#mem-obj-journal) distinguishes arbitrary returned payloads from their inspected index/hash envelope; [MEM-OBJ-agent-history](memory.md#mem-obj-agent-history) distinguishes readable diagnostics from replay input. Neither a display summary nor JSON serialization classifies an opaque payload's form, authority or learning route. Extension-provided checkpoint alternatives remain separate from the inspected default summarizers.

[RT-RTE-graph-admission](runtime.md#rt-rte-graph-admission) separates requested drafting/approval from executable structural admission. Consequently authored guidance and human graph approval retain claimed bases, while [RT-RTE-library-update](runtime.md#rt-rte-library-update) supports wired source-snapshot import and metadata maintenance. [MEM-RTE-saved-workflow](memory.md#mem-rte-saved-workflow) supports manual content selection for command/UI saving but not a manual classification for every generic API caller. Imported lineage describes a local transfer into a retained store; it does not authenticate the original author.

The paper-specific contribution is not lost inside memory's locally uninspected paper inventory. [EPI-RTE-paper-decision](epistemic.md#epi-rte-paper-decision) adds feedback-directed guidance refinement at the doctrine layer; [EPI-RTE-paper-checks](epistemic.md#epi-rte-paper-checks) and [EPI-RTE-final-report](epistemic.md#epi-rte-final-report) add implemented evidence and reporting consumers. This supports local validation authority and requested learning/evolution without turning the generic importer into a scientific acceptance gate. Original evidence provenance and automatic admission of a particular refined graph remain unresolved.

Curation names transformations rather than commands. Incremental checkpoints consolidate experience and evolve prior checkpoints. Managed updates evolve operative content and remove withdrawn entries from future discovery; that removal is local decay, not a claim that earlier prompt copies or all backups disappear. [MEM-OBJ-library-state](memory.md#mem-obj-library-state) supports access control and conflict criteria, not scientific warrant. Retained traces at the summarizer have learning authority; summary text at the next model supplies knowledge/context. The two consumers are not collapsed into one authority claim.

Read-back is split into request and independent selection operations. A model-selected file read remains pull even when matching uses judgment. Automatically supplied registry entries use coarse eligibility; session reconstruction uses actual branch/entry identities and coarse window selection; [MEM-RTE-journal-replay](memory.md#mem-rte-journal-replay) uses index/hash identity for cache substitution. A requested filename alone does not establish identifier push. The known pull operations do not make unresolved push alternatives inapplicable.

Reconciliation establishes no duplicate supersessions. All citations therefore retain their declaring canonical record. Containers remain valid alongside separately declared summary, graph-policy and graph-assertion parts; their shared consumers do not erase differences in origin or force. Missing individual graph provenance, specialized importer/exporter and task-oriented coverage, extension write semantics and deployed consumption prevent stronger inventory assessments. No absence finding is manufactured from those gaps.

Source-read log: none. This classification used only the supplied accepted members and governing contracts; no frozen-source ambiguity required an additional source read. The profile adds neither records nor source evidence.
