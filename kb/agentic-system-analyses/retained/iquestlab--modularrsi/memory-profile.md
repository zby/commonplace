---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of ModularRSI: accumulated improvement evidence, executable generations, selection/recovery state and same-task continuation at the frozen release."
run-id: "AAS-2026-10-18-modularrsi-4218ceff5530-01"
source-identity: "https://github.com/IQuestLab/ModularRSI"
reviewed-boundary: "b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9"
memory-comparison:
  version: 2
  scope: "Includes accumulated raw trials and derived findings/proposals, proposal/disposition/lease state, manifests and journals, evolved executable generations and descriptions, archive/cached bundle access structures, progress/history recovery, and retained same-task summary/scrollback read-back. Includes unresolved historical initialization, additional memory mechanisms inside uninspected released strategy alternatives, unestablished manifest/cross-module receiving paths, and any accumulated provider-side state behind inspected endpoints. Excludes static shipped skill/instruction catalogs, unfrozen external task contents and model weights considered solely as static inference machinery; neither static storage nor API use alone establishes accumulated memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Persisted trials, findings/proposals/control ledgers, manifests, journals, archives, generation source, cache and progress/history files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "memory.md#mem-obj-finding-record"
                - "memory.md#mem-obj-proposal-record"
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-obj-implementation-record"
                - "memory.md#mem-obj-editor-memory"
                - "memory.md#mem-obj-archive-entry"
                - "runtime.md#rt-rte-bundle-selection"
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
                - "epistemic.md#epi-obj-trial-summary"
              note: "Numbered directories and JSON/JSONL, Python, trial and cache files retain the material across later consumers."
          records:
            - "runtime.md#rt-obj-module-library"
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-rte-bundle-selection"
            - "memory.md#mem-rte-progress-resume"
            - "memory.md#mem-rte-history-contrast"
            - "epistemic.md#epi-obj-trial-summary"
          note: "These named retained objects have file-backed storage. JSON/Python are encodings, not distinct substrates; repository distribution does not establish a Git-backed memory write mechanism."
        - scope: "Active module registry, folded proposal objects and retained same-task chat/summary and scrollback state"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "memory.md#mem-obj-proposal-record"
                - "runtime.md#rt-rte-context-handoff"
                - "runtime.md#rt-rte-solver-task"
              note: "Library registry, folded records, replacement chat and bounded observation history reside in process memory."
          records:
            - "runtime.md#rt-obj-module-library"
            - "memory.md#mem-obj-proposal-record"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "These are process-local retained/access parts, distinct from their file backing. Same-task replacement summaries count because another invocation consumes them."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "runtime.md#rt-obj-module-library"
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-obj-implementation-record"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-obj-archive-entry"
        - "runtime.md#rt-rte-bundle-selection"
        - "memory.md#mem-rte-progress-resume"
        - "memory.md#mem-rte-history-contrast"
        - "epistemic.md#epi-obj-trial-summary"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Files and process-memory parts are established for the named inventory. Uninspected variants and provider state prevent complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Finding/proposal rationale, generated descriptions, journal change text and model-generated continuation content at text consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-finding-record"
                - "memory.md#mem-obj-proposal-record"
                - "runtime.md#rt-obj-module-description"
                - "memory.md#mem-obj-editor-memory"
                - "runtime.md#rt-rte-context-handoff"
              note: "Models interpret diagnoses, proposed deltas/hypotheses, catalog prose and retained continuation text; journal change strings are also retained language."
          records:
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
            - "runtime.md#rt-obj-module-description"
            - "memory.md#mem-obj-editor-memory"
            - "runtime.md#rt-rte-context-handoff"
          note: "This unit covers the language-bearing parts, not surrounding IDs, status or executable factories."
        - scope: "Executable modules, fixed-rule metadata, trial summary fields, manifests and cached bundle specifications"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-obj-archive-entry"
                - "memory.md#mem-obj-implementation-record"
                - "runtime.md#rt-rte-bundle-selection"
                - "memory.md#mem-rte-progress-resume"
                - "epistemic.md#epi-obj-trial-summary"
              note: "Python factories/methods, eligibility/status/lease fields, checkpoint markers and bundle names have localized symbolic interpretation."
          records:
            - "runtime.md#rt-obj-module-library"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-obj-archive-entry"
            - "memory.md#mem-obj-implementation-record"
            - "runtime.md#rt-rte-bundle-selection"
            - "memory.md#mem-rte-progress-resume"
            - "epistemic.md#epi-obj-trial-summary"
          note: "Code and typed IDs/fields are symbolic at their fixed-rule consumers; prose inside these envelopes belongs to the separate language unit."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "runtime.md#rt-obj-module-description"
        - "memory.md#mem-obj-editor-memory"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-obj-module-library"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-obj-archive-entry"
        - "memory.md#mem-obj-implementation-record"
        - "runtime.md#rt-rte-bundle-selection"
        - "memory.md#mem-rte-progress-resume"
        - "epistemic.md#epi-obj-trial-summary"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Both language and symbolic operative parts are established. No numerical model representation is inferred for the accumulated-memory boundary from use of a model API."
    lineage:
      assessment: "partial"
      units:
        - scope: "Selected trial fields and trace excerpts retained for diagnosis and restored investigation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-trial-summary"
                - "epistemic.md#epi-rte-summary-extraction"
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
              note: "Fixed extraction takes rewards, identities and selected messages from recorded trials; persisted/restored summaries preserve selected trace-derived material."
          records:
            - "epistemic.md#epi-obj-trial-summary"
            - "epistemic.md#epi-rte-summary-extraction"
            - "memory.md#mem-rte-progress-resume"
            - "memory.md#mem-rte-history-contrast"
          note: "This unit covers extraction of recorded activity, not the origin or truth of external task contents."
        - scope: "Model-authored diagnosis, proposal text, edited implementations and their descriptions on the live improvement path"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-finding-record"
                - "memory.md#mem-obj-proposal-record"
                - "memory.md#mem-rte-evidence-brief"
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-rte-generation-change"
              note: "Investigators author findings; routing/editing models supply proposal content and module source, including registration text."
          records:
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-rte-evidence-brief"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
          note: "The shipped live producer is identified. This does not reconstruct how the released initial library was trained."
        - scope: "Generated same-task continuation summary and QA handoff"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Retained summary/answer content is generated from surviving session history for subsequent calls."
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Separate model calls author the summary, questions and answers; outputs are copied into continuation context."
          records:
            - "runtime.md#rt-rte-context-handoff"
          note: "Model production from selected chat is wired; semantic fidelity is not established."
        - scope: "Software-built access/control representations: bundle cache, archive serialization, proposal state, manifests and progress/history maps"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bundle-selection"
                - "memory.md#mem-obj-archive-entry"
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-obj-implementation-record"
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
              note: "Software constructs serialized selection, eligibility, lineage, build and recovery representations from existing objects and results."
          records:
            - "runtime.md#rt-rte-bundle-selection"
            - "memory.md#mem-obj-archive-entry"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-rte-progress-resume"
            - "memory.md#mem-rte-history-contrast"
          note: "These representations compile selections, metadata and prior results under deterministic software rules; this does not resolve provenance of every embedded text field."
        - scope: "Installed/source baseline copied into the live driver initial generation"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-rte-generation-change"
              note: "The driver snapshots the existing installed library into gen_0 and seeds its archive before live evolution."
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
          note: "This is the known local acquisition path, separate from unresolved historical authorship and training provenance before release."
        - scope: "Initial released generation and sanitized ancestral metadata before the inspected live driver"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
          note: "The initial source is available, but complete historical derivation and training admission are unavailable. A parent name or shipped source file does not establish the origin of its content."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "epistemic.md#epi-obj-trial-summary"
        - "epistemic.md#epi-rte-summary-extraction"
        - "memory.md#mem-rte-progress-resume"
        - "memory.md#mem-rte-history-contrast"
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-rte-evidence-brief"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-rte-generation-change"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-rte-bundle-selection"
        - "memory.md#mem-obj-archive-entry"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-obj-implementation-record"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Live authored, trace-extracted and software-compiled derivations are supported. Initial released provenance, variant alternatives and provider memory remain unresolved; no complete lineage union is claimed."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained findings, historical trial evidence and causal hypotheses at investigator/implementer update consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-rte-history-contrast"
                - "memory.md#mem-obj-finding-record"
                - "memory.md#mem-obj-proposal-record"
              note: "Selected evidence and causal rationale provide reference/context for investigation and implementation."
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-rte-history-contrast"
                - "runtime.md#rt-rte-generation-change"
              note: "Retained execution experience feeds automatic module-strategy generation and admission for later tasks."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-rte-history-contrast"
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
          note: "Split evidence/reference use from the trace-fed durable-update use. Delivery is wired, but compliance, correct causality and benefit are unobserved."
        - scope: "Retained proposed behavioral delta at the assigned implementer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-record"
                - "memory.md#mem-rte-evidence-brief"
              note: "The retained delta/action/target supplies the editor its assigned behavioral change."
          records:
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-rte-evidence-brief"
          note: "The brief specifies the intervention to implement, rather than merely furnishing background evidence."
        - scope: "Proposal eligibility, dispositions and lease state at software selection/recovery consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-bap-backlog-control"
              note: "State and leases select which proposal or recovery operation proceeds."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-bap-backlog-control"
              note: "Attempts, age, task/window breadth and stable jitter determine relative proposal priority."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-state"
                - "epistemic.md#epi-rte-finding-disposition"
              note: "Non-open states and terminal disposition IDs suppress otherwise eligible future routing."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-state"
                - "epistemic.md#epi-rte-finding-disposition"
              note: "Placed/terminal identity sets are retained eligibility criteria checked before admitting supplied findings into new routing work."
          records:
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-bap-backlog-control"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "These are fixed-rule effects, not the semantic authority of a rationale stored beside them."
        - scope: "Archive statuses, niche/identity fields and bundle replay at subsequent composition"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-entry"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Archive identity/niche and replayed names select available implementations and bundle destinations."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-entry"
                - "runtime.md#rt-rte-bundle-selection"
                - "epistemic.md#epi-rte-paired-confirmation"
              note: "Retired/excluded status removes variants from ordinary dynamic choices, best-effort on archive read."
          records:
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-rte-bundle-selection"
            - "epistemic.md#epi-rte-paired-confirmation"
          note: "Archive veto is scoped to ordinary dynamic selection. Replay/static/forced paths and import effects are not universally revoked."
        - scope: "Retained module descriptions at the dynamic composer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-description"
                - "runtime.md#rt-bap-description-selection"
              note: "Descriptions supply task-relevant capability/context assertions to the model."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-description-selection"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Model interpretation of the catalog and task determines which executable strategy names are chosen."
          records:
            - "runtime.md#rt-obj-module-description"
            - "runtime.md#rt-bap-description-selection"
            - "runtime.md#rt-rte-bundle-selection"
          note: "Catalog capability prose is advisory input; software validates returned names but does not validate the descriptions as true."
        - scope: "Retained executable generation at the loader and baseline runtime policy consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-bap-module-execution"
                - "runtime.md#rt-rte-solver-task"
              note: "Selected strategy implementations determine command/helper dispatch and continuation operations."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-module-execution"
                - "runtime.md#rt-rte-solver-task"
              note: "Loaded verifier/stopping and tool-dispatch code can permit or end runtime actions."
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-bap-module-execution"
            - "runtime.md#rt-rte-solver-task"
          note: "Python is consumed as implementation, not classified as natural-language instruction. These supported effects do not enumerate the force of every uninspected variant."
        - scope: "Checkpoint and historical-pass access state at resumed scheduling and diagnosis"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
              note: "Retained indices, cooldowns, reflection boundaries and task-to-pass paths select work and evidence windows."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
              note: "Restored summary content and reconstructed passing-trial evidence enter later investigation."
          records:
            - "memory.md#mem-rte-progress-resume"
            - "memory.md#mem-rte-history-contrast"
          note: "Identity/alignment and progress fields have software force; associated summary text separately supplies investigation context."
        - scope: "QA continuation at the next solver invocation"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Summary and answers supply remembered task state and context."
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Generated continuation content is passed as a handoff prompt for continued work."
          records:
            - "runtime.md#rt-rte-context-handoff"
          note: "At the next solver invocation the retained handoff supplies context/guidance, not an evidenced parameter or durable-artifact update. Its automatic production separately qualifies for trace learning; that does not give the output learning authority at downstream inference. No activation or improved performance is observed."
        - scope: "Outcome journals, unused compact-history display and manifest consumer details beyond supplied promotion wiring"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-abs-editor-readback"
            - "memory.md#mem-obj-implementation-record"
          note: "Journal writes and manifest helper APIs do not establish a consequential later content consumer. Missing consumer wiring prevents assigning additional authority to those payloads."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-rte-evidence-brief"
        - "memory.md#mem-rte-history-contrast"
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-bap-backlog-control"
        - "epistemic.md#epi-rte-finding-disposition"
        - "memory.md#mem-obj-archive-entry"
        - "runtime.md#rt-rte-bundle-selection"
        - "epistemic.md#epi-rte-paired-confirmation"
        - "runtime.md#rt-obj-module-description"
        - "runtime.md#rt-bap-description-selection"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-bap-module-execution"
        - "runtime.md#rt-rte-solver-task"
        - "memory.md#mem-rte-progress-resume"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-implementation-record"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Authority is classified at named consumers, independently of admission agency and benefit. Journal/manifest consumer limits, alternative strategies and provider state prevent full coverage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Shipped live finding/proposal admission and deterministic state, manifest, archive, journal, progress/history maintenance"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-finding-record"
                - "memory.md#mem-obj-proposal-record"
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-obj-implementation-record"
                - "memory.md#mem-obj-archive-entry"
                - "memory.md#mem-obj-editor-memory"
                - "memory.md#mem-rte-progress-resume"
                - "memory.md#mem-rte-history-contrast"
                - "memory.md#mem-rte-evidence-brief"
              note: "Models generate content and software parses, records, selects or revises it without individual human admission."
          records:
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-archive-entry"
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-rte-progress-resume"
            - "memory.md#mem-rte-history-contrast"
            - "memory.md#mem-rte-evidence-brief"
          note: "The shipped software/model callers are identified, not inferred from a generic API caller. Operator launch is not per-content approval."
        - scope: "Edited-module deployment through gates and generation promotion"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-generation-change"
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-bap-module-execution"
              note: "Model edits, software checks, reviewer result and promotion decide deployment without a human approving each change."
          records:
            - "runtime.md#rt-rte-generation-change"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-bap-module-execution"
          note: "Reviewer judgment and software guards are computational admission; fail-open and repair qualifications remain attached to the route."
        - scope: "Summary/QA replacement and bundle-cache write on inspected paths"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Software budget/overflow or cache-write rules retain model continuation content and selected bundle state."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-bundle-selection"
          note: "Workflow configuration initiates these paths but does not decide each retained output."
        - scope: "Historical admission of initial released module content and ancestry"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-rte-generation-change"
          note: "Sanitized initial history does not establish whether content admission involved per-item human decisions. Neither automatic nor manual is assigned to this initialization."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-obj-implementation-record"
        - "memory.md#mem-obj-archive-entry"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-rte-progress-resume"
        - "memory.md#mem-rte-history-contrast"
        - "memory.md#mem-rte-evidence-brief"
        - "runtime.md#rt-rte-generation-change"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-bap-module-execution"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-rte-bundle-selection"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Automatic live writes are wired. Historical initialization control, uninspected strategy alternatives and provider admission remain unresolved; no manual write is inferred from workflow launch."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Model continuation production from retained chat and selected evidence summaries"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "epistemic.md#epi-rte-summary-extraction"
              note: "Summarization and selected-field extraction compress retained activity into smaller later-consumed representations."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "epistemic.md#epi-rte-summary-extraction"
          note: "Compression/extraction reduces existing recorded content; summary fidelity and any extra generated assertions remain unchecked. The known finding is the implemented reduction path, not a proof of semantic preservation."
        - scope: "Same-intervention linking into existing retained proposals"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-semantic-checks"
                - "epistemic.md#epi-rte-finding-disposition"
                - "memory.md#mem-obj-proposal-record"
              note: "Model sameness judgment and software linkage avoid creating a separate proposal for an intervention judged already represented."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-proposal-record"
                - "memory.md#mem-obj-proposal-state"
                - "epistemic.md#epi-rte-finding-disposition"
              note: "Support links and proposal events revise the retained intervention record and its state."
          records:
            - "memory.md#mem-obj-proposal-record"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-rte-evidence-brief"
            - "epistemic.md#epi-rte-semantic-checks"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "The implemented first-match link merges support under an existing intervention; it does not delete duplicate raw finding rows or prove semantic equivalence."
        - scope: "Existing strategy revision and admitted candidate deployment"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-rte-generation-change"
              note: "The live editor can modify an existing strategy before admission."
            - value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-generation-change"
              note: "Passing retained staging trees become numbered generations available to later solver launches."
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
          note: "This unit concerns the implemented existing-entry edit and promotion paths, not a claim that every generated variant is a modification."
        - scope: "Archive retirement and terminal proposal/finding withdrawal while history remains"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-entry"
                - "memory.md#mem-obj-proposal-state"
                - "epistemic.md#epi-rte-paired-confirmation"
                - "epistemic.md#epi-rte-finding-disposition"
              note: "Superseded archive states and terminal dispositions prevent ordinary current reuse while retaining historical material."
          records:
            - "memory.md#mem-obj-archive-entry"
            - "memory.md#mem-obj-proposal-state"
            - "epistemic.md#epi-rte-paired-confirmation"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "Withdrawal changes current reliance rather than erasing source or logs; replay alternatives remain."
        - scope: "Requested causal conjecture about a counterfactual intervention"
          assessment: "known"
          findings:
            - value: "synthesize"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-contrast-finding"
                - "memory.md#mem-rte-evidence-brief"
              note: "The diagnosis contract requests a proposed intervention effect not entailed by the original execution outcomes."
          records:
            - "epistemic.md#epi-obj-contrast-finding"
            - "memory.md#mem-rte-evidence-brief"
          note: "The investigator is asked for a causal claim beyond the compared unchanged-code outcomes. Actual generated novel claims are uninspected; this is an afforded transformation, not an observed or guaranteed result."
        - scope: "Additional semantic operations in unchecked generated summaries/findings and opaque manifest/journal consumer paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-abs-editor-readback"
            - "memory.md#mem-obj-implementation-record"
          note: "No actual input/output comparison determines all semantic changes; a compact formatter without a consuming route does not establish active curation. Further operations cannot be classified from names alone."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "runtime.md#rt-rte-context-handoff"
        - "epistemic.md#epi-rte-summary-extraction"
        - "memory.md#mem-obj-proposal-record"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-rte-evidence-brief"
        - "epistemic.md#epi-rte-semantic-checks"
        - "epistemic.md#epi-rte-finding-disposition"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-rte-generation-change"
        - "memory.md#mem-obj-archive-entry"
        - "epistemic.md#epi-rte-paired-confirmation"
        - "epistemic.md#epi-obj-contrast-finding"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-implementation-record"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Implemented reduction, linking, revision, deployment and withdrawal coexist with an afforded conjecture operation. No exhaustive operation inventory, guaranteed synthesis or independent benefit is established."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Reflection selection and automatic brief delivery after completed support work"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-rte-history-contrast"
                - "memory.md#mem-rte-progress-resume"
              note: "Completion/resume triggers routing, historical contrast lookup and proposal-support delivery to the next isolated consumer."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-rte-history-contrast"
            - "memory.md#mem-rte-progress-resume"
          note: "The driver selects accumulated evidence for fresh investigator/implementer contexts, rather than answering a solver request for memory."
        - scope: "Later generation load and dynamic description/catalog selection"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-rte-bundle-selection"
                - "runtime.md#rt-bap-description-selection"
                - "memory.md#mem-obj-archive-entry"
              note: "Task setup automatically loads the chosen generation and delivers candidate descriptions for composition."
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-bundle-selection"
            - "runtime.md#rt-bap-description-selection"
            - "memory.md#mem-obj-archive-entry"
          note: "Launching the task is not a foreground model request for each retained strategy or description. Software supplies filtered catalog and selected retained strategy parts."
        - scope: "Summary/QA handoff and retained scrollback delivery on inspected baseline/selected observation paths"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "runtime.md#rt-rte-solver-task"
              note: "The next call receives the derived continuation or selected retained pane/history content without requesting that memory."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Budget/overflow and observation capture are automatic selectors of retained material for a later model invocation."
        - scope: "Editor archive, trace and file reads of accumulated content"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-solver-task"
                - "memory.md#mem-obj-archive-entry"
              note: "Editor file/archive actions return requested retained material within allowed read roots."
          records:
            - "runtime.md#rt-rte-solver-task"
            - "memory.md#mem-obj-archive-entry"
            - "memory.md#mem-rte-history-contrast"
          note: "This unit is the request/return operation: model-selected path/range or archive type/lineage requests are fulfilled on demand. Static skill bodies are excluded from this use-acquired inventory."
        - scope: "Bundle-cache read and forced/K-roll replay into a later solver task"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bundle-selection"
              note: "Configured replay loads cached or captured names for the next task/roll without a solver-model request."
          records:
            - "runtime.md#rt-rte-bundle-selection"
          note: "The driver-selected mode automatically reconstructs and supplies a stored strategy choice; this is separate from the requested editor-file return."
        - scope: "Compact editor-history and evolution-log read-back in searched shipped callers"
          assessment: "absent"
          findings: []
          records:
            - "memory.md#mem-abs-editor-readback"
            - "memory.md#mem-obj-editor-memory"
          note: "Bounded absence is caller wiring in src/ and scripts/, not a denial of the formatter capability or arbitrary external use."
        - scope: "Additional manifest and cross-module handoff consumer routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-proposal-state"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "Retained helper-accessible records/handoff files do not establish the receiving consumer. Additional direction cannot be assigned."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-rte-evidence-brief"
        - "memory.md#mem-rte-history-contrast"
        - "memory.md#mem-rte-progress-resume"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-rte-bundle-selection"
        - "runtime.md#rt-bap-description-selection"
        - "memory.md#mem-obj-archive-entry"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-rte-solver-task"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-obj-implementation-record"
        - "memory.md#mem-obj-proposal-state"
        - "epistemic.md#epi-rte-finding-disposition"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Both request-driven editor pull and driver/context push are wired. Journal wiring has a local absence; unresolved consumer and variant/provider paths prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Reflection proposal portfolio and task-history scheduling push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-obj-proposal-state"
                - "memory.md#mem-rte-progress-resume"
              note: "Fixed eligibility and scalar age/support/cooldown policies select work without a semantic query over full retained content."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-obj-proposal-state"
            - "memory.md#mem-rte-progress-resume"
          note: "Trigger: completed work or resume. Inputs: retained state, attempts, age, task/window breadth, cooldown and deterministic tie-break. Selected part: eligible proposal/evidence and pending investigation work."
        - scope: "Referenced-finding and earlier-passing-trial push into fresh investigation/implementation"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-rte-history-contrast"
              note: "Actual identity matches retrieve referenced findings and task-matched historical pass evidence for automatic delivery."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-rte-history-contrast"
          note: "Trigger: selected proposal or task lacking a current pass. Inputs: proposal finding IDs or exact task identity. Selected part: matched finding bodies or the stored passing-trial referent, subject to display/revalidation limits."
        - scope: "Archive and active-generation filtering/load push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-entry"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Status/type/niche and editor-only availability filtering bounds the catalog."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Bundle/pin names select actual retained module factories and helper implementations to deliver to the runtime."
          records:
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-bundle-selection"
          note: "Trigger: task setup/composition. Inputs: current generation, archive status/type/niche and explicit pin identities. Selected parts: eligible library entries/catalog and named strategy implementations."
        - scope: "Dynamic model selection of retained strategy catalog entries"
          assessment: "known"
          findings:
            - value: "inferred-judgment"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bundle-selection"
                - "runtime.md#rt-bap-description-selection"
              note: "The composer model judges task-to-description fit before validated names choose retained strategies."
          records:
            - "runtime.md#rt-rte-bundle-selection"
            - "runtime.md#rt-bap-description-selection"
          note: "Trigger: multiple eligible choices/helper catalog. Inputs: task text and retained descriptions. Selected parts: offered variant/helper names and their implementations. No reward or embedding retrieval is established."
        - scope: "Cache replay push selected by task-instruction hash"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bundle-selection"
              note: "Instruction hash matches a cache filename; retained bundle names then resolve selected strategies."
          records:
            - "runtime.md#rt-rte-bundle-selection"
          note: "Trigger: cache-read mode. Input: instruction SHA-256. Selected part: matching persisted bundle payload, then its named implementations. A real identity lookup occurs, not merely an identifier in a display."
        - scope: "Compression and bounded retained-observation push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "runtime.md#rt-rte-solver-task"
              note: "Budget, tail and stale-output rules select the retained portion supplied to later invocations."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Trigger: low context/overflow or observation capture. Inputs: token budget, tail positions and stale/current output policy; selected parts: surviving chat, summary/handoff and bounded scrollback. Model summary production is a transformation, not itself proof of a semantic memory-retrieval selector."
        - scope: "Requested editor-file and archive-return operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-solver-task"
            - "memory.md#mem-obj-archive-entry"
          note: "Signal classifies push selection only. These request/return operations are pull; their path/type arguments are not an additional identifier push finding."
        - scope: "Compact journal read-back in searched callers"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-abs-editor-readback"
          note: "No wired delivery/selection route exists in the searched shipped callers, so there is no push selector to classify for that bounded route."
        - scope: "Unestablished manifest and cross-module receiving consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-proposal-state"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "Neither a consumer direction nor actual push selector is established; known pull elsewhere cannot make these alternatives inapplicable."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-rte-evidence-brief"
        - "memory.md#mem-obj-proposal-state"
        - "memory.md#mem-rte-progress-resume"
        - "memory.md#mem-rte-history-contrast"
        - "memory.md#mem-obj-archive-entry"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-rte-bundle-selection"
        - "runtime.md#rt-bap-description-selection"
        - "runtime.md#rt-rte-context-handoff"
        - "runtime.md#rt-rte-solver-task"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-implementation-record"
        - "epistemic.md#epi-rte-finding-disposition"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Coarse, identifier and model-judgment push selectors are supported at distinct operations. Pull-only local returns are inapplicable locally, not a system-wide signal absence."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Primary trace diagnosis through retained proposal/brief to admitted executable module and later solver"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "runtime.md#rt-rte-generation-change"
                - "runtime.md#rt-obj-module-library"
                - "runtime.md#rt-bap-module-execution"
              note: "Solver execution evidence enters automatic diagnosis/edit/admission; promoted Python is a live later-task behavior artifact."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-obj-finding-record"
            - "memory.md#mem-obj-proposal-record"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
            - "runtime.md#rt-bap-module-execution"
          note: "Automatic trace-fed production yields a durable behavior-shaping library consumed on later tasks. This controlled yes concerns the write/consumer route, not improved capacity, faithful diagnosis or exercised causal self-improvement."
        - scope: "Automatic session-history compression into later-call continuation"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Recorded session turns feed generated retained continuation context delivered to the next solver call."
          records:
            - "runtime.md#rt-rte-context-handoff"
          note: "The retained summary/QA result survives replacement and reaches another invocation within the same task; cross-task reuse is not required. Fallback differences do not erase the shared QA witness."
        - scope: "Outcome-fed archive eligibility revision"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-archive-entry"
                - "epistemic.md#epi-rte-paired-confirmation"
                - "runtime.md#rt-rte-bundle-selection"
              note: "Regression screening writes superseded archive state that shapes future strategy selection."
          records:
            - "memory.md#mem-obj-archive-entry"
            - "epistemic.md#epi-rte-paired-confirmation"
            - "runtime.md#rt-rte-bundle-selection"
          note: "Recorded task/bundle/reward experience automatically changes durable selection status, which later ordinary composition consumes. Descriptive confirmation is not randomized causal evidence."
        - scope: "Initial released-library training and historical admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-rte-generation-change"
          note: "The live update route does not reconstruct whether each initial released entry was automatically learned from traces. Sanitized history prevents a complete initial learning classification."
        - scope: "Compact editor-history and evolution-log feedback through searched shipped callers"
          assessment: "known"
          findings:
            - value: "no"
              basis: "wired"
              records:
                - "memory.md#mem-abs-editor-readback"
                - "memory.md#mem-obj-editor-memory"
              note: "No compact-index invocation or evolution-log read into an editor was found in the bounded shipped caller search."
          records:
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-abs-editor-readback"
          note: "The absence is bounded to the searched src/ and scripts/ journal-feedback path, not all learning or arbitrary external consumers. Outcome retention and an unused formatter do not close a later-consumer chain."
        - scope: "Manifest and cross-module handoff additional receiving paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-proposal-state"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "Trace-derived recording alone is insufficient. Helper-accessible records and handoff files do not establish receiving consumers or complete absence of qualifying updates."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-rte-evidence-brief"
        - "memory.md#mem-obj-finding-record"
        - "memory.md#mem-obj-proposal-record"
        - "runtime.md#rt-obj-module-library"
        - "runtime.md#rt-rte-generation-change"
        - "runtime.md#rt-bap-module-execution"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-archive-entry"
        - "epistemic.md#epi-rte-paired-confirmation"
        - "runtime.md#rt-rte-bundle-selection"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-implementation-record"
        - "memory.md#mem-obj-proposal-state"
        - "epistemic.md#epi-rte-finding-disposition"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Three qualifying automatic trace-fed routes support yes. The bounded journal-feedback no remains local. Initial history, additional consumer paths, variant and provider uncertainties retain partial coverage; yes and incomplete coverage each independently prevent a system-wide no."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Primary execution-evidence-to-module update: linked solver attempts and tool/environment feedback"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evidence-brief"
                - "memory.md#mem-rte-history-contrast"
                - "runtime.md#rt-rte-generation-change"
              note: "Linked task attempts, module/command activity and outcomes supply the diagnosed multi-step experience."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-solver-task"
                - "memory.md#mem-rte-evidence-brief"
                - "runtime.md#rt-rte-generation-change"
              note: "Recorded terminal/tool execution and feedback within the permitted solver traces feed diagnosis and durable code change."
          records:
            - "memory.md#mem-rte-evidence-brief"
            - "memory.md#mem-rte-history-contrast"
            - "runtime.md#rt-rte-solver-task"
            - "runtime.md#rt-rte-generation-change"
          note: "Original input is recorded task execution, not the JSON envelope of the derived finding. Pass/fail and historical comparisons retain linked work/outcome information; unfrozen task text alone is not a trace source."
        - scope: "Same-task generated continuation from retained conversational history"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Recorded conversational history is the original input to the generated continuation."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
              note: "Selected history and terminal screen carry tool execution/observation feedback into the retained handoff."
          records:
            - "runtime.md#rt-rte-context-handoff"
          note: "The summary/answer calls consume surviving prior turns, including tool/terminal material, not a claimed complete full-history source. Unwound turns need not contribute."
        - scope: "Outcome confirmation updating archive selection policy"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-paired-confirmation"
            - "memory.md#mem-obj-archive-entry"
            - "epistemic.md#epi-obj-trial-summary"
          note: "Confirmation consumes extracted task/bundle/reward tuples, not an established linked sequence of states, actions and outcomes. The accepted records establish no controlled original-input source value for this consumer; neither richer diagnosis inputs nor trial identity supplies the missing trajectory warrant. Its automatic durable status update and later selection consumer remain established independently of source classification."
        - scope: "Initial released-library learning inputs and sanitized ancestry"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archive-entry"
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-generation-change"
          note: "No complete original training input inventory survives in accepted records. Neither trajectory provenance nor other source classes can be assigned to each initial entry."
        - scope: "Compact editor-history and evolution-log feedback through searched shipped callers"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-editor-memory"
            - "memory.md#mem-abs-editor-readback"
          note: "The bounded caller absence leaves no qualifying trace-learning chain on this local route; original source classification for learning is consequently inapplicable, not an absence of raw outcome inputs."
        - scope: "Additional possible trace-fed updates behind manifest and cross-module receiving paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-implementation-record"
            - "memory.md#mem-obj-proposal-state"
            - "epistemic.md#epi-rte-finding-disposition"
          note: "Without a qualifying write-to-later-consumer chain for these additional alternatives, original trace sources cannot be classified or declared inapplicable as a complete absence."
        - scope: "Additional retained objects and update/consumer mechanisms inside uninspected released strategy alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-obj-module-library"
            - "runtime.md#rt-rte-context-handoff"
            - "runtime.md#rt-rte-solver-task"
          note: "Baseline and selected alternatives do not enumerate all executable variant bodies. Their additional accumulated-memory mechanisms, if any, are uninspected; no complete inventory or negative follows."
        - scope: "Accumulated provider-side state, if any, behind configured inference endpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-lite-llm"
          note: "Clients invoke inference, but provider persistence and parameter changes are inaccessible. No provider-side accumulated-memory value or absence is established. Static weights alone are not classified as a use-acquired memory."
      records:
        - "memory.md#mem-rte-evidence-brief"
        - "memory.md#mem-rte-history-contrast"
        - "runtime.md#rt-rte-solver-task"
        - "runtime.md#rt-rte-generation-change"
        - "runtime.md#rt-rte-context-handoff"
        - "epistemic.md#epi-rte-paired-confirmation"
        - "memory.md#mem-obj-archive-entry"
        - "epistemic.md#epi-obj-trial-summary"
        - "runtime.md#rt-obj-module-library"
        - "memory.md#mem-obj-editor-memory"
        - "memory.md#mem-abs-editor-readback"
        - "memory.md#mem-obj-implementation-record"
        - "memory.md#mem-obj-proposal-state"
        - "epistemic.md#epi-rte-finding-disposition"
        - "runtime.md#rt-cmp-lite-llm"
      note: "Session logs, tool traces and trajectories are supported on named qualifying writes. No event-stream value is inferred merely from serialized ledger events or timestamps. Initial, additional-consumer, variant and provider inputs remain unresolved."
---

# ModularRSI memory profile

## Comparison rationale

The principal accumulated behavior artifact is the executable generation, not the optional editor-history display. The library is file-backed symbolic strategy, while its registration descriptions are language interpreted by a separate composer. Findings and proposals retain reasons upstream; the solver does not automatically receive those reasons. These distinctions support different form, lineage and consumer-authority findings rather than one classification for everything stored in Python or JSON. See [RT-OBJ-module-library](runtime.md#rt-obj-module-library), [RT-OBJ-module-description](runtime.md#rt-obj-module-description), [MEM-RTE-evidence-brief](memory.md#mem-rte-evidence-brief) and [MEM-OBJ-proposal-record](memory.md#mem-obj-proposal-record).

All findings remain at their recorded evidence layers. In particular, causal synthesis is afforded by investigator instructions; no actual newly formulated diagnosis was inspected. Consolidation describes the reduction route, not a fidelity guarantee. The epistemic account's indeterminate semantic relation for generated summaries prevents claiming that every summary is only reshaping; it does not remove the wired compression operation. Same-intervention linking is deduplication of proposed work through support merging, not erasure of raw findings. See [EPI-OBJ-contrast-finding](epistemic.md#epi-obj-contrast-finding), [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) and [EPI-RTE-finding-disposition](epistemic.md#epi-rte-finding-disposition).

Trace learning uses this profile's automatic trace-fed write criterion, not demonstrated future improvement. Diagnosis-to-code, continuation summarization and outcome-fed archive retirement have qualifying later consumers. Their experience can have learning authority at an evidenced update consumer while output code, guidance or eligibility state has a different downstream force. In particular, QA continuation has knowledge and instruction authority at the next solver inference call, not learning authority: that call is not evidenced to update parameters or another durable behavior-shaping artifact. Wiring does not establish that a particular change was exercised or beneficial. Original source classes follow the content actually consumed: conversational turns, tool feedback and linked multi-step task experience, not the fact that ledger rows are serialized as events. The primary diagnosis route supports trajectories independently; confirmation's task/bundle/reward tuples do not establish that source. Confirmation's trace-source unit is therefore not-determinable, without withdrawing its qualifying automatic archive update or borrowing the diagnosis route's richer input. See [MEM-RTE-evidence-brief](memory.md#mem-rte-evidence-brief), [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff), [EPI-RTE-paired-confirmation](epistemic.md#epi-rte-paired-confirmation) and [RT-RTE-generation-change](runtime.md#rt-rte-generation-change).

Read-back distinguishes driver-selected pushes from editor-requested returns. An exact task/finding/cache match establishes identifier selection only where it actually selects a delivered retained part; a path on a requested file is not an extra push signal. Model catalog judgment is a separate selector from coarse archive eligibility and budget clipping. Static skill catalogs are outside this accumulated-memory inventory, so the uninspected optional solver skill-injection path does not become a finding about learned instructions. See [MEM-RTE-history-contrast](memory.md#mem-rte-history-contrast), [MEM-RTE-evidence-brief](memory.md#mem-rte-evidence-brief), [RT-RTE-bundle-selection](runtime.md#rt-rte-bundle-selection) and [RT-RTE-solver-task](runtime.md#rt-rte-solver-task).

Reconciliation supplies no supersessions; no value changes identity through an amendment. Its retained editor-memory ambiguity prevents concluding automatic journal-to-editor delivery. The profile uses the bounded absence of searched caller wiring and separately preserves positive journal retention, rather than treating a formatter as a live consumer. It also keeps manifest and cross-module receiving routes unresolved. Retryable findings are not classified as scheduled future work merely because they remain nonterminal; already-open proposal reuse is independently wired. See [MEM-ABS-editor-readback](memory.md#mem-abs-editor-readback), [MEM-OBJ-editor-memory](memory.md#mem-obj-editor-memory), [MEM-OBJ-implementation-record](memory.md#mem-obj-implementation-record) and [EPI-RTE-finding-disposition](epistemic.md#epi-rte-finding-disposition).

Each axis is partial because the included unresolved parts cannot be erased by an inspected baseline witness. Missing initial training/admission history limits lineage, write agency and trace origins; uninspected strategy bodies limit exhaustive mechanism coverage; provider persistence remains opaque. Static model weights are not assigned parametric memory, model-weights storage or learning merely because inference uses them. The searched journal-feedback path has a bounded local trace-learning no, but there is no complete learning-inventory negative and no supported system-wide no. Derived unions may retain the positive findings and their bases, but cannot turn them into complete-value statistics. See [MEM-OBJ-archive-entry](memory.md#mem-obj-archive-entry), [RT-OBJ-module-library](runtime.md#rt-obj-module-library), [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) and [RT-CMP-lite-llm](runtime.md#rt-cmp-lite-llm).

Source-read log: none. This classification uses only the supplied accepted members and their annotations; no frozen-source files were newly read, no evidence was added and report verification was not reopened.
