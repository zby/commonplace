---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Project Wiki memory profile: repository records, intake provenance, resumable review and task-directed later consultation."
run-id: "AAS-2026-11-08-project-wiki-b055e5c71dc7-01"
source-identity: "https://github.com/giodra96/project-wiki"
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
memory-comparison:
  version: 2
  scope: "Included: consuming-project canonical records and durable analysis, indexes/catalog/traceability, extracted and raw source provenance including opaque original payloads, mutable review/decision checkpoints, audit and maintenance history, project config/exclusions and installed/refreshed protocol blocks at their recorded later consumers. Excluded: shipped static skill/schema/templates as accumulated memory, ordinary unretained current-run context, unspecified external host/provider state and model weights. No populated wiki or host run is supplied."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Generated canonical pages, routing, sidecar, review state, audit history and project controls"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-requirement-evidence"
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-audit-history"
                - "memory.md#mem-obj-project-controls"
              note: "Markdown/YAML/JSON are project-local files; semantic production and use depend on host workflows."
            -
              value: "repo"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-requirement-evidence"
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-audit-history"
                - "memory.md#mem-obj-project-controls"
              note: "The containing project repository is the intended durable memory boundary, not a remote database."
          records:
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-wiki-routing"
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-requirement-evidence"
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-project-controls"
          note: "The memory inventory covers the generated file families and their later consumers."
        -
          scope: "Helper-published extraction, ledger and retained raw source archive, including optional opaque source copies"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-source-registry"
                - "runtime.md#rt-rte-source-intake"
              note: "Helpers persist snapshots, chunks and progress as local files; optional binary copies remain files regardless of encoding."
          records:
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-source-registry"
            - "runtime.md#rt-rte-source-intake"
          note: "Opaque source encoding does not make its substrate opaque."
      records:
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-wiki-routing"
        - "memory.md#mem-obj-intake-provenance"
        - "memory.md#mem-obj-review-progress"
        - "memory.md#mem-obj-requirement-evidence"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-project-controls"
        - "runtime.md#rt-rte-source-intake"
      note: "All included retained surfaces are local project/repository files. External host/provider storage is outside this memory boundary, not an unresolved alternative memory backend."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Canonical prose, routing descriptions, audit findings and blocking-review reasons at host/human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-audit-history"
                - "memory.md#mem-obj-review-progress"
              note: "Statements, explanations, routing summaries and reasons require agent or human interpretation."
          records:
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-wiki-routing"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-review-progress"
          note: "Content prose is distinguished from its IDs, links and statuses."
        -
          scope: "Extracted chunk text and free-text ledger notes delivered during review"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-chunks"
                - "epistemic.md#epi-obj-review-progress"
                - "runtime.md#rt-rte-source-intake"
              note: "View emits selected complete text; apply retains free-text notes alongside fixed fields."
          records:
            - "epistemic.md#epi-obj-chunks"
            - "epistemic.md#epi-obj-review-progress"
            - "runtime.md#rt-rte-source-intake"
          note: "This classifies the text and notes, not PDF/DOCX source internals."
        -
          scope: "Hashes, paths, chunk and record IDs, statuses, edge sets, config values and ignore patterns at fixed helper consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-requirement-evidence"
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-project-controls"
                - "epistemic.md#epi-rte-structure-check"
              note: "Fixed consumers compare bytes, fields, membership and edges or apply boolean/pattern rules."
          records:
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-requirement-evidence"
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-project-controls"
            - "epistemic.md#epi-rte-structure-check"
          note: "These rules do not establish semantic truth of prose."
        -
          scope: "Optional original document payloads and raw archived binary documents beyond extracted text"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-source-registry"
          note: "Source copies can contain opaque PDF/DOCX and nontext material. Recorded extraction/display does not classify every operative source part; no parametric or symbolic finding is inferred for the entire binary."
      records:
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-wiki-routing"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-review-progress"
        - "epistemic.md#epi-obj-chunks"
        - "epistemic.md#epi-obj-review-progress"
        - "runtime.md#rt-rte-source-intake"
        - "memory.md#mem-obj-intake-provenance"
        - "memory.md#mem-obj-requirement-evidence"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-project-controls"
        - "epistemic.md#epi-rte-structure-check"
      note: "Text and fixed-field parts are classified. Original binary/nontext payload form is not resolved by their text extraction."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Raw supplied documents and the text extracted from them"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-intake-provenance"
                - "epistemic.md#epi-rte-extract-source"
              note: "Source bytes enter from local supplied files; chunks carry imported assertions."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-intake-provenance"
                - "epistemic.md#epi-rte-extract-source"
              note: "Normalization, block formation and chunk wrappers are deterministic derivation, not model-authored truth."
          records:
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-intake-provenance"
            - "epistemic.md#epi-rte-extract-source"
          note: "Import and extraction are separate derivation stages; imported source warrant stays unknown."
        -
          scope: "Host-written canonical records, routing, evidence edges, reviews and audit prose"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-requirement-evidence"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-audit-history"
              note: "The host authors project-specific records and semantic metadata."
            -
              value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "runtime.md#rt-rte-note-update"
              note: "User/stakeholder notes and explicit product intent provide acquired content, distinct from host analysis."
          records:
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-wiki-routing"
            - "memory.md#mem-obj-requirement-evidence"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-audit-history"
            - "runtime.md#rt-rte-note-update"
          note: "Authorship does not imply human per-content approval."
        -
          scope: "Durable answer/task-derived record updates selected for later preflight"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-note-update"
                - "runtime.md#rt-rte-coding-cycle"
                - "memory.md#mem-obj-canonical-records"
              note: "The memory annotations trace task/chat outcomes through lasting-value or impact judgment into retained records and later context."
          records:
            - "runtime.md#rt-rte-note-update"
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-canonical-records"
          note: "This is a prescribed extraction path, not proof of a stored full transcript."
        -
          scope: "Generated structure, default metadata and installed protocol blocks"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-initialize-wiki"
              note: "The scaffold renders packaged contracts/templates into project structure."
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-project-protocol"
                - "memory.md#mem-obj-project-controls"
              note: "Host installation/refresh copies or adapts shipped blocks and defaults rather than learning them from experience."
          records:
            - "runtime.md#rt-rte-initialize-wiki"
            - "runtime.md#rt-bap-project-protocol"
            - "memory.md#mem-obj-project-controls"
          note: "The executable scaffold and prescribed instruction installation keep separate evidence layers."
        -
          scope: "Upstream origin of assertions and nontext material inside supplied source documents"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-intake-provenance"
          note: "Import lineage is established at the project boundary, but records do not resolve earlier authored versus compiled versus trace-derived origin of every source part."
      records:
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-intake-provenance"
        - "epistemic.md#epi-rte-extract-source"
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-wiki-routing"
        - "memory.md#mem-obj-requirement-evidence"
        - "memory.md#mem-obj-review-progress"
        - "memory.md#mem-obj-audit-history"
        - "runtime.md#rt-rte-note-update"
        - "runtime.md#rt-rte-coding-cycle"
        - "runtime.md#rt-rte-initialize-wiki"
        - "runtime.md#rt-bap-project-protocol"
        - "memory.md#mem-obj-project-controls"
      note: "Known local derivations do not determine upstream source provenance. No model-weight lineage is attributed to this file-memory system."
    behavioral_authority:
      assessment: "known"
      units:
        -
          scope: "Canonical content and retained source/review/audit prose at selected later host or human readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-audit-history"
              note: "Project intent, implementation descriptions, source evidence, reasons and history supply interpreted task or review knowledge."
          records:
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-audit-history"
          note: "Requirements express project intent as task knowledge, not automatically top-level runtime instructions."
        -
          scope: "Conversational task/chat answers at the host durable-answer update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-note-update"
                - "memory.md#mem-obj-canonical-records"
                - "runtime.md#rt-rte-coding-cycle"
              note: "The host consumes conversational experience in its lasting-value and representation judgment to produce durable canonical revisions or analysis for later preflight context."
          records:
            - "runtime.md#rt-rte-note-update"
            - "memory.md#mem-obj-canonical-records"
            - "runtime.md#rt-rte-coding-cycle"
          note: "The memory annotation on note-update establishes the automatic trace-fed update consumer and retained result. This learning force is distinct from downstream knowledge at the later coding reader; neither exercised use nor improved capacity is established."
        -
          scope: "Generated marked protocol at future host coding invocations"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-project-protocol"
              note: "The installed block supplies standing consultation/update directions, conditional on host loading."
          records:
            - "runtime.md#rt-bap-project-protocol"
          note: "Shipped static workflow bodies are excluded as memory; the installed/refreshed project block is the included downstream surface."
        -
          scope: "Indexes, catalog paths, traceability and persisted workflow markers at later task/review selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-audit-history"
                - "memory.md#mem-obj-requirement-evidence"
              note: "Indexes select relevant scope/pages; review markers support resumption; history can select sync baselines and edges lead to provenance."
          records:
            - "memory.md#mem-obj-wiki-routing"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-requirement-evidence"
          note: "These are scope/window/destination selectors, not evidence of numerical relevance ranking."
        -
          scope: "Retained source hashes/history, review states and evidence edges at helper decisions"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-review-progress"
                - "runtime.md#rt-rte-source-intake"
              note: "Historical source identity determines process/skip/review and persisted review state directs review operations."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-review-progress"
                - "memory.md#mem-obj-requirement-evidence"
                - "epistemic.md#epi-rte-ledger-check"
                - "epistemic.md#epi-rte-structure-check"
              note: "Retained identities, dispositions and reciprocal edges constrain structural admissibility."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-registry"
                - "runtime.md#rt-rte-source-intake"
                - "epistemic.md#epi-rte-ledger-check"
              note: "Hash/digest mismatch errors refuse local operations; these do not enforce semantic truth or lock the entire integration."
          records:
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-review-progress"
            - "memory.md#mem-obj-requirement-evidence"
            - "runtime.md#rt-rte-source-intake"
            - "epistemic.md#epi-rte-ledger-check"
            - "epistemic.md#epi-rte-structure-check"
          note: "Force is bounded to the documented helper consumers, not a universal canonical-write interlock."
        -
          scope: "Project config at the host automatic-write decision; ignore patterns at source helpers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-project-controls"
                - "runtime.md#rt-rte-coding-cycle"
              note: "Effective false/invalid config directs the host to suspend automatic assessment/writes, not explicit work."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-controls"
              note: "Ignore patterns select which sources named helper routes admit."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-controls"
                - "runtime.md#rt-rte-source-intake"
              note: "Named helper source filters suppress excluded reads; raw host filesystem access is not mediated."
          records:
            - "memory.md#mem-obj-project-controls"
            - "runtime.md#rt-rte-coding-cycle"
            - "runtime.md#rt-rte-source-intake"
          note: "Policy-mediated config force and executable source filtering remain separate."
      records:
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-intake-provenance"
        - "memory.md#mem-obj-review-progress"
        - "memory.md#mem-obj-audit-history"
        - "runtime.md#rt-bap-project-protocol"
        - "memory.md#mem-obj-wiki-routing"
        - "memory.md#mem-obj-requirement-evidence"
        - "memory.md#mem-obj-source-registry"
        - "runtime.md#rt-rte-source-intake"
        - "epistemic.md#epi-rte-ledger-check"
        - "epistemic.md#epi-rte-structure-check"
        - "memory.md#mem-obj-project-controls"
        - "runtime.md#rt-rte-coding-cycle"
        - "runtime.md#rt-rte-note-update"
      note: "The recorded retained-part consumers support these forces, including learning at the conversational-answer update consumer and knowledge at later task readers; no claim of compliance, benefit, ranking, or weight learning follows. Opaque originals have only the recorded source/provenance use, not an inferred hidden behavioral consumer."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Helper extraction, scaffold creation, pending-ledger initialization and structural ledger admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-initialize-wiki"
                - "runtime.md#rt-rte-source-intake"
                - "memory.md#mem-obj-review-progress"
              note: "Software admits structurally valid generated state without a human approving each retained content unit."
          records:
            - "runtime.md#rt-rte-initialize-wiki"
            - "runtime.md#rt-rte-source-intake"
            - "memory.md#mem-obj-review-progress"
          note: "A user starting init/update does not make the downstream software admissions manual."
        -
          scope: "Ordinary semantic integration, note/answer filing, impact updates, routing and metadata edits"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-note-update"
                - "runtime.md#rt-rte-coding-cycle"
                - "epistemic.md#epi-rte-content-admit"
                - "memory.md#mem-obj-wiki-routing"
                - "memory.md#mem-obj-requirement-evidence"
                - "memory.md#mem-obj-audit-history"
              note: "The host decides representation and normally admits conservative writes without per-claim human approval."
          records:
            - "runtime.md#rt-rte-note-update"
            - "runtime.md#rt-rte-coding-cycle"
            - "epistemic.md#epi-rte-content-admit"
            - "memory.md#mem-obj-wiki-routing"
            - "memory.md#mem-obj-requirement-evidence"
            - "memory.md#mem-obj-audit-history"
          note: "Explicit workflow authorization and automatic preference gating do not replace the actual admission decision."
        -
          scope: "Human-supplied sources/notes, explicit preference changes, blocking decisions and high-impact canonical maintenance"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-project-controls"
                - "epistemic.md#epi-rte-content-admit"
                - "epistemic.md#epi-rte-claim-withdraw"
              note: "An operator supplies selected source content/preferences or approves consequential choices before their retained effects."
          records:
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-project-controls"
            - "epistemic.md#epi-rte-content-admit"
            - "epistemic.md#epi-rte-claim-withdraw"
          note: "Conditional human approval is local, not a universal mandatory review stage."
        -
          scope: "Generic direct filesystem editing of controls or project records outside the prescribed request/approval mechanisms"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-project-controls"
            - "memory.md#mem-obj-canonical-records"
          note: "Files can be edited directly, but generic writer identity does not establish whether a human approved the specific content. That alternative prevents a complete agency classification."
      records:
        - "runtime.md#rt-rte-initialize-wiki"
        - "runtime.md#rt-rte-source-intake"
        - "memory.md#mem-obj-review-progress"
        - "runtime.md#rt-rte-note-update"
        - "runtime.md#rt-rte-coding-cycle"
        - "epistemic.md#epi-rte-content-admit"
        - "memory.md#mem-obj-wiki-routing"
        - "memory.md#mem-obj-requirement-evidence"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-project-controls"
        - "epistemic.md#epi-rte-claim-withdraw"
      note: "Both software/model admission and explicit human content decisions are supported; direct-edit control remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Host maintenance of existing canonical claims, questions, alerts, audit entries and verbose indexes"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-audit-history"
                - "runtime.md#rt-rte-explicit-reconcile"
              note: "Affected records are revised and ongoing audit entries can be extended under history-preservation rules."
            -
              value: "invalidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-canonical-records"
                - "memory.md#mem-obj-intake-provenance"
                - "epistemic.md#epi-rte-claim-withdraw"
              note: "Rejected/superseded extraction and stale canonical dispositions withdraw current reliance while preserving history."
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-audit-history"
                - "runtime.md#rt-rte-note-update"
                - "memory.md#mem-obj-canonical-records"
              note: "Durable answers are condensed into useful records; verbose index detail moves to linked pages and audit content stays compact."
          records:
            - "memory.md#mem-obj-canonical-records"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-intake-provenance"
            - "epistemic.md#epi-rte-claim-withdraw"
            - "runtime.md#rt-rte-explicit-reconcile"
            - "runtime.md#rt-rte-note-update"
          note: "These are instructed transformations over retained content, not helper-enforced semantic changes."
        -
          scope: "Inbox duplicate-history and byte-hash quarantine"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-registry"
                - "runtime.md#rt-rte-source-intake"
              note: "Duplicate skip/quarantine removes redundant inbox copies from processing using retained hash/history, not semantic similarity."
          records:
            - "memory.md#mem-obj-source-registry"
            - "runtime.md#rt-rte-source-intake"
          note: "This is a byte/process-history operation, not a semantic merge of claims."
        -
          scope: "Reviewed source information entering canonical use"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-intake-provenance"
                - "epistemic.md#epi-rte-content-admit"
                - "epistemic.md#epi-rte-canonical-retain"
              note: "Source-backed information moves from provenance/review state to canonical task use after the host admission procedure."
          records:
            - "memory.md#mem-obj-intake-provenance"
            - "epistemic.md#epi-rte-content-admit"
            - "epistemic.md#epi-rte-canonical-retain"
          note: "Promotion denotes changed tier of use, not a guarantee of warranted truth."
        -
          scope: "Meaning change in model-authored analysis and source-to-record synthesis"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-note-update"
            - "epistemic.md#epi-obj-analysis"
            - "epistemic.md#epi-rte-content-compare"
          note: "The route requests synthesis, but no concrete recorded candidate establishes a new claim absent from inputs versus compression or other derivation. Controlled synthesize cannot be established from its label."
      records:
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-intake-provenance"
        - "epistemic.md#epi-rte-claim-withdraw"
        - "runtime.md#rt-rte-explicit-reconcile"
        - "runtime.md#rt-rte-note-update"
        - "memory.md#mem-obj-source-registry"
        - "runtime.md#rt-rte-source-intake"
        - "epistemic.md#epi-rte-content-admit"
        - "epistemic.md#epi-rte-canonical-retain"
        - "epistemic.md#epi-obj-analysis"
        - "epistemic.md#epi-rte-content-compare"
      note: "Supported curation coexists with unresolved semantic transformation. Chunking/index rebuilding alone does not establish a curation value; no decay is inferred."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Automatic task preflight selection before ordinary coding/planning"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-cycle"
                - "memory.md#mem-obj-wiki-routing"
              note: "Task trigger activates host selection of relevant retained pages without a separate consumer request for those facts."
          records:
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-wiki-routing"
          note: "Trigger is a code task; selector is the host interpreting task plus routing/current context; delivered material is selected project knowledge."
        -
          scope: "Foreground requests for retained pages, review sections/chunks, full source, progress and explicit audit/history/sync context"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-cycle"
                - "runtime.md#rt-rte-source-intake"
                - "runtime.md#rt-rte-explicit-reconcile"
                - "memory.md#mem-obj-audit-history"
              note: "The agent requests linked records or retained evidence for the selected task/review; explicit investigation and reconciliation request retained state."
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-intake"
                - "memory.md#mem-obj-intake-provenance"
                - "memory.md#mem-obj-review-progress"
              note: "Inspect/view/audit helpers fulfill explicit intake-ID/section/chunk requests with retained source and state."
          records:
            - "runtime.md#rt-rte-coding-cycle"
            - "runtime.md#rt-rte-source-intake"
            - "runtime.md#rt-rte-explicit-reconcile"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-intake-provenance"
            - "memory.md#mem-obj-review-progress"
          note: "The file/tool return is a requested pull operation, not a second push simply because code prints it."
        -
          scope: "Repeated helper/host reads of retained preferences, source history and evidence metadata"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-project-controls"
                - "memory.md#mem-obj-source-registry"
                - "memory.md#mem-obj-requirement-evidence"
                - "epistemic.md#epi-rte-structure-check"
              note: "Named helper calls request current configuration/history/edges for filtering, preflight and validation."
          records:
            - "memory.md#mem-obj-project-controls"
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-requirement-evidence"
            - "epistemic.md#epi-rte-structure-check"
          note: "These metadata consumers are distinct from model ingestion of canonical prose."
      records:
        - "runtime.md#rt-rte-coding-cycle"
        - "memory.md#mem-obj-wiki-routing"
        - "runtime.md#rt-rte-source-intake"
        - "runtime.md#rt-rte-explicit-reconcile"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-intake-provenance"
        - "memory.md#mem-obj-review-progress"
        - "memory.md#mem-obj-project-controls"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-requirement-evidence"
        - "epistemic.md#epi-rte-structure-check"
      note: "The included consumers are the shipped task, review, investigation, maintenance and helper paths. No opaque independent delivery service is established in the records; external host-native compaction or injection is excluded."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "Task-triggered automatic preflight selecting canonical project pages"
          assessment: "known"
          findings:
            -
              value: "inferred-judgment"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-cycle"
                - "memory.md#mem-obj-wiki-routing"
              note: "Host interprets task relevance against root/section indexes and current context, choosing pages before work."
          records:
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-wiki-routing"
          note: "Trigger: ordinary code-related task with existing index. Inputs: task, current routing, already-read pages and fallback metadata. Selected retained parts: relevant canonical pages. Budget is qualitative, not token-enforced."
      records:
        - "runtime.md#rt-rte-coding-cycle"
        - "memory.md#mem-obj-wiki-routing"
      note: "This is the recorded push selector. Section/chunk IDs used by requested view and page paths used by requested reads are pull selectors, not identifier push. Mere availability of the root index is not a separately supported coarse selection mechanism."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic lasting-value filing of chat answers into retained canonical records/durable analysis for future preflight"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-note-update"
                - "runtime.md#rt-rte-coding-cycle"
                - "memory.md#mem-obj-canonical-records"
              note: "Task/chat answer flows through host value judgment to durable text and then later index-selected task context; human initiation is not per-answer admission."
          records:
            - "runtime.md#rt-rte-note-update"
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-canonical-records"
          note: "The memory annotation supplies the trace-fed write-to-later-consumer chain. It establishes an afforded pathway, not exercised use, improved capacity, or parameter training."
        -
          scope: "Other task-impact updates, imported source material and retained audit/review histories as potential trace-fed behavior-shaping writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-review-progress"
          note: "Code changes and history are retained, but records do not identify all original activity inputs or establish a qualifying automatic trace-to-durable-behavior chain for each alternative. Logging or review checkpointing alone cannot supply a local negative or positive."
      records:
        - "runtime.md#rt-rte-note-update"
        - "runtime.md#rt-rte-coding-cycle"
        - "memory.md#mem-obj-canonical-records"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-review-progress"
      note: "A supported chat-derived route gives yes while other included write families retain trace-qualification uncertainty. No evidenced-absence record supports any local or system-wide no; excluded provider-weight updates are not counted as an unresolved in-system backend."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Original conversational input to automatic durable-answer filing"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-note-update"
                - "memory.md#mem-obj-canonical-records"
              note: "The qualifying route transforms user notes/planning conversation and durable agent chat answers; origin is conversational activity even without retention of a full raw archive."
          records:
            - "runtime.md#rt-rte-note-update"
            - "memory.md#mem-obj-canonical-records"
          note: "Scope is the chat-derived qualifying write, not arbitrary imported static project instructions."
        -
          scope: "Original input mix of other task-impact/source-derived and history-derived candidate learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-coding-cycle"
            - "memory.md#mem-obj-source-registry"
            - "memory.md#mem-obj-audit-history"
            - "memory.md#mem-obj-review-progress"
          note: "Records do not establish recorded tool requests/results, linked state-action-outcome trajectories, or event streams as original inputs to each qualifying write. Artifact filenames, audit labels and task diffs do not resolve that origin."
      records:
        - "runtime.md#rt-rte-note-update"
        - "memory.md#mem-obj-canonical-records"
        - "runtime.md#rt-rte-coding-cycle"
        - "memory.md#mem-obj-source-registry"
        - "memory.md#mem-obj-audit-history"
        - "memory.md#mem-obj-review-progress"
      note: "Session origin is supported for the chat route. No blanket event-streams, tool-traces or trajectories value is inferred for opaque source histories or normal code changes."
---

# Project Wiki memory profile

## Comparison rationale

The inventory follows the memory report's generated artifacts and recorded later consumers, not all storage used by a host coding agent. Repository placement and local file persistence are both supported; Markdown/YAML/JSON describe encoding, not alternative storage services. Original source binaries remain included even though their full representational form and upstream derivation cannot be classified from extracted text ([MEM-OBJ-intake-provenance](memory.md#mem-obj-intake-provenance), [MEM-OBJ-source-registry](memory.md#mem-obj-source-registry)).

Reconciliation supersedes the epistemic sidecar duplicate with [MEM-OBJ-requirement-evidence](memory.md#mem-obj-requirement-evidence); this profile cites the canonical memory record. Chunk text, the ledger and canonical subfamilies remain valid contained parts, not replacements for their broader memory containers. Helper wiring never upgrades semantic integration, instruction installation or future host compliance to observed operation ([EPI-RTE-canonical-retain](epistemic.md#epi-rte-canonical-retain), [RT-BAP-project-protocol](runtime.md#rt-bap-project-protocol)).

Admission is classified at the decision, not physical I/O or workflow initiation. Normal host integration is automatic in the controlled sense; explicit human supply, preference selection and consequential approval are manual locally. Unspecified direct edits retain unresolved agency. Byte-level quarantine supports deduplication; canonical admission supports a higher tier of use. Requested synthesis does not establish a new claim absent from inputs, so that branch stays unresolved rather than receiving synthesize merely because the workflow calls its output synthesis ([EPI-RTE-content-admit](epistemic.md#epi-rte-content-admit), [EPI-OBJ-analysis](epistemic.md#epi-obj-analysis), [MEM-OBJ-project-controls](memory.md#mem-obj-project-controls)).

Automatic preflight and requested file delivery are different operations in one chain. Task-triggered host judgment supplies push selection; page/section/chunk requests are pull. An ID on a requested chunk establishes no identifier-based push. The recorded smallest-relevant-set budget does not establish host eviction, isolated context frames or a token limit ([RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle), [MEM-OBJ-wiki-routing](memory.md#mem-obj-wiki-routing), [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)).

The chat-answer route supports afforded trace learning because it automatically retains trace-derived material for later task context. At the update consumer, the host consumes conversational experience to decide lasting value and representation and produce durable canonical revisions or analysis; that is afforded learning authority. At the later coding reader, the resulting text supplies knowledge. These distinct consumer/effect paths are supported by the note-update record and its memory annotation, not inferred solely from the trace-learning yes. Neither force requires parameter training, a novel claim or demonstrated benefit. Other write families lack enough recorded trace-origin/qualification detail for a complete inventory. They therefore prevent a complete-value learning conclusion without suppressing the supported yes. No local no is authored: the reports declare no bounded-absence record for these alternatives. Task changes and audit filenames alone cannot establish tool-traces, event-streams or trajectories ([RT-RTE-note-update](runtime.md#rt-rte-note-update), [MEM-OBJ-canonical-records](memory.md#mem-obj-canonical-records), [MEM-OBJ-audit-history](memory.md#mem-obj-audit-history)).

No source files were read for this mapping; classification uses the supplied accepted records and their annotations. No records or evidence were added. All evidence remains implementation or doctrine/design; no supplied run or experiment warrants activation or benefit.

