---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "AREX-Skill memory comparison for retained guidance, session summaries and workflow replay, with unresolved extension and construction alternatives."
run-id: AAS-2026-10-19-arex-skill-089a5ed7476f-01
source-identity: https://github.com/VectorSpaceLab/AREX-Skill
reviewed-boundary: ac3fe1afa80fb9a09775ecfb2b6cc3ba850a2db6
memory-comparison:
  version: 2
  scope: >-
    Accumulated or revised repository guidance and its routing/admission metadata;
    retained project instructions; session messages, selection metadata, default
    and extension-supplied compaction/branch checkpoints, custom entries and
    injected messages; workflow result journals, diagnostic history and saved-script
    alternatives; retained QA/recovery reports used in review and refinement.
    Includes unresolved extension payloads and incompletely inspected maintenance,
    export, task-evaluation and workflow-authoring paths. Static shipped resources
    alone, current tool grants, temporary worker context without later consumption,
    external-host ingestion and external provider parameter/storage internals are
    excluded. No system-complete memory inventory is established by the accepted records.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Managed guidance, routing/index and management state, and retained project instruction files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-routing-metadata, memory.md#mem-obj-project-context, runtime.md#rt-rte-library-update]
              note: "Operative trees and bookkeeping are filesystem objects; Git source acquisition does not establish repo as the runtime memory substrate."
          records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-routing-metadata, memory.md#mem-obj-project-context, runtime.md#rt-rte-library-update]
          note: "Storage is resolved for these parts independently of their initialization or content validity."
        - scope: "Session tree, checkpoints, custom-state envelopes and message entries"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-compaction-summary, memory.md#mem-obj-custom-entry, memory.md#mem-rte-session-retention]
              note: "JSONL is a file encoding; deferred flush means disk durability is conditional."
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-session-metadata, memory.md#mem-obj-custom-entry, memory.md#mem-rte-session-retention]
              note: "Memory-only SessionManager and in-memory tree indexes are separately supported."
          records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, memory.md#mem-obj-custom-entry, memory.md#mem-rte-session-retention]
          note: "Opaque extension content does not make the enclosing JSONL/in-memory storage unknown."
        - scope: "Workflow journal/snapshots/diagnostics and QA/recovery output artifacts"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-workflow-journal, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-qa-records, epistemic.md#epi-obj-recovery-report]
              note: "Run JSON, diagnostic snapshots and evaluator JSON/JSONL persist on disk."
          records: [memory.md#mem-obj-workflow-journal, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-qa-records, epistemic.md#epi-obj-recovery-report]
          note: "This resolves the named retained artifacts, not every saved script or specialized evaluator artifact."
        - scope: "Additional saved-script, export, refresh and task-specific retained parts"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-rte-workflow-context, memory.md#mem-rte-workflow-resume, epistemic.md#epi-rte-refine-guidance]
          note: "The records leave full machinery, recovery and revision paths incomplete; their substrate inventory cannot be closed from these witnesses."
      records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-custom-entry, memory.md#mem-obj-workflow-journal, epistemic.md#epi-rte-refine-guidance]
      note: "Files and in-memory storage are supported locally; the partial-loop inventory prevents complete enumeration."
    representational_form:
      assessment: partial
      units:
        - scope: "Skill/reference prose and retained project directions at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-project-context, runtime.md#rt-bap-skill-guidance]
              note: "Bodies and reference prose affect the consumer through interpretation, not fixed execution rules."
          records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-project-context, runtime.md#rt-bap-skill-guidance]
          note: "Bundled executable scripts are a separate part."
        - scope: "Bundled scripts, routing/index and management metadata, session selection metadata and checkpoint boundaries"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-routing-metadata, memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, runtime.md#rt-rte-library-update]
              note: "Localized fields and scripts have fixed computational interpretations; symbolic encoding does not certify their correctness."
          records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-routing-metadata, memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, runtime.md#rt-rte-library-update]
          note: "Only inspected structural parts are classified; arbitrary details are excluded from this unit."
        - scope: "Textual session content, default summary prose, workflow diagnostic text and evaluator feedback"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-recovery-report]
              note: "Text remains natural language even when wrapped as a user message or truncated for display."
          records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-recovery-report]
          note: "This does not classify media internals or arbitrary worker return values."
        - scope: "Session envelopes, workflow cache structure, diagnostic fields, QA normalized strings/scores and recovery predicates"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-workflow-journal, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-qa-records, epistemic.md#epi-obj-recovery-report]
              note: "IDs, hashes, roles, normalized tokens and numeric metrics have localized fixed consumers; scalar numbers are not parametric representations."
          records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-workflow-journal, memory.md#mem-obj-agent-history, epistemic.md#epi-obj-qa-records, epistemic.md#epi-obj-recovery-report]
          note: "Classifies structure and metric consumption, not semantic contents of arbitrary result JSON."
        - scope: "Media/tool payload internals, arbitrary custom data/details, extension checkpoint content and full workflow return values"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-session-messages, memory.md#mem-obj-custom-entry, memory.md#mem-obj-compaction-summary, memory.md#mem-obj-workflow-journal]
          note: "Readable summaries and symbolic envelopes do not determine the forms of opaque payloads."
      records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-custom-entry, memory.md#mem-obj-workflow-journal, epistemic.md#epi-obj-qa-records]
      note: "Natural-language and symbolic parts are established; opaque alternatives and remaining partial-loop parts prevent completeness. External model weights are not retained memory in this scope."
    lineage:
      assessment: partial
      units:
        - scope: "Managed graphs acquired through import or official-library installation"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update]
              note: "The runtime acquires a staged tree or source snapshot; acquisition does not resolve its initial authorship."
          records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update]
          note: "Known admission lineage is local to these transfer paths."
        - scope: "Default compaction/branch summaries and compact workflow diagnostic history"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history]
              note: "Conversation/tool history feeds summary production or diagnostic reduction."
          records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history]
          note: "Default producers are resolved; extension substitutes are separate. Diagnostic extraction alone does not establish trace learning."
        - scope: "QA normalized/metric fields and computed recovery predicates/decision"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [epistemic.md#epi-rte-qa-normalization, epistemic.md#epi-rte-qa-scoring, epistemic.md#epi-rte-recovery-check, epistemic.md#epi-rte-recovery-decision]
              note: "Programs derive these fields from supplied inputs by fixed transformations and comparisons."
          records: [epistemic.md#epi-rte-qa-normalization, epistemic.md#epi-rte-qa-scoring, epistemic.md#epi-rte-recovery-check, epistemic.md#epi-rte-recovery-decision]
          note: "Original answer truth and evidence provenance remain outside this derived-field unit."
        - scope: "Agent-authored/revised guidance requested by repository and paper verification"
          assessment: partial
          findings:
            - value: authored
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Procedures assign writing and revision to an agent; no concrete artifact's construction lineage is observed."
            - value: trace-extracted
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Requested revisions draw on native/usability results and feedback, but actual derivation and retained reasons are not traced."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
          note: "The requested paths are supported; initial drafts and individual generated propositions have unresolved derivation."
        - scope: "Initial skill/project-file contents, extension substitutes/data and arbitrary workflow results/checkpoint replies"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-repo-skills, memory.md#mem-obj-project-context, memory.md#mem-obj-custom-entry, memory.md#mem-obj-workflow-journal, memory.md#mem-rte-workflow-resume]
          note: "Model/tool work and callback/default alternatives are described, but their content-specific origins are not resolved. No single display or producer label supplies complete lineage."
      records: [runtime.md#rt-rte-repo-import, epistemic.md#epi-rte-summary-generation, epistemic.md#epi-rte-qa-scoring, workflow.md#wf-rte-repo-verification, memory.md#mem-obj-custom-entry]
      note: "Known transfers and derivations coexist with unknown initial provenance, extension branches and uninspected specialized paths."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Installed skill bodies and retained project directions at later model requests"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [runtime.md#rt-bap-skill-guidance, memory.md#mem-obj-project-context]
              note: "Skill bodies and project text direct model behavior through context, without guaranteeing compliance."
          records: [runtime.md#rt-bap-skill-guidance, memory.md#mem-obj-project-context]
          note: "Instruction force is not runtime enforcement of the prose."
        - scope: "Session messages/default summaries at later model requests and diagnostic snippets at human display"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-rte-session-retention, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history]
              note: "History supplies context and diagnostics supply reference information; user-role summaries are not automatically standing system directions."
          records: [memory.md#mem-rte-session-retention, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-agent-history]
          note: "Metadata and excluded bash results are not universally delivered as knowledge."
        - scope: "Retained history and prior summaries consumed by default summarizers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [epistemic.md#epi-rte-summary-generation, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation]
              note: "Experience feeds automatic production of retained continuation guidance; this is update-consumer authority, distinct from the output's knowledge authority."
          records: [epistemic.md#epi-rte-summary-generation, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation]
          note: "Behavior-shaping summary production is implemented, not evidence of improved capacity."
        - scope: "Session branch/boundary metadata and workflow journal at reconstruction/replay consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-workflow-resume]
              note: "Selected leaf/kept-entry state chooses the input window; cached matching-prefix results select reuse rather than live invocation."
          records: [memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-workflow-resume]
          note: "A symbolic replay effect does not require model interpretation of cached prose."
        - scope: "Runtime routing metadata and durable source/digest state at admission/update checks"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-routing-metadata, epistemic.md#epi-rte-import-check, runtime.md#rt-rte-library-update]
              note: "Retained identity, assignment and digest fields are checked for admissibility/consistency."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-import-check, runtime.md#rt-rte-library-update]
              note: "Failed identity/integrity or conflict conditions reject the ordinary transaction; caller force and alternative paths limit the veto."
            - value: routing
              basis: wired
              records: [runtime.md#rt-rte-library-update]
              note: "Durable source/digest state selects later update/no-op/conflict handling, not a scientific truth decision."
          records: [memory.md#mem-obj-routing-metadata, epistemic.md#epi-rte-import-check, runtime.md#rt-rte-library-update]
          note: "Classifies the consumed retained fields, not the entire static validator program as memory."
        - scope: "Router pages at the model's repository-selection step"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-routing-metadata, runtime.md#rt-rte-skill-delivery]
              note: "Natural-language area/family pages guide capability-based selection of repository roots and sub-skills."
            - value: ranking
              basis: claimed
              records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-obj-routing-metadata]
              note: "The recorded policy compares likely areas and asks for the smallest useful repository set; relative priority is model-mediated, not observed scoring."
          records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-obj-routing-metadata]
          note: "Policy-level selection does not establish exercised relevance or an embedding index."
        - scope: "Retained verification/recovery results and feedback at revision controllers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-recovery-decision, epistemic.md#epi-rte-refine-guidance]
              note: "Controllers are instructed to inspect reports and disclosed limitations as evidence for continuation."
            - value: learning
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Feedback is prescribed input to durable guidance revision; executed evidence-responsive updates are not established."
            - value: routing
              basis: claimed
              records: [epistemic.md#epi-rte-recovery-decision, epistemic.md#epi-rte-refine-guidance]
              note: "Retained accept/refine results tell the controller whether to revise or finalize; script exit status is not automatic deployment."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-recovery-decision, epistemic.md#epi-rte-refine-guidance]
          note: "These are the recorded report-to-controller effects, not a blanket epistemic endorsement."
        - scope: "Arbitrary extension data, opaque worker outputs and untraced script/evaluator consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-obj-workflow-journal, memory.md#mem-rte-workflow-context, epistemic.md#epi-rte-refine-guidance]
          note: "Consumer-specific effects of opaque payloads and remaining paths cannot be inferred from storage or a readable preview."
      records: [runtime.md#rt-bap-skill-guidance, memory.md#mem-rte-session-retention, memory.md#mem-rte-workflow-resume, epistemic.md#epi-rte-import-check, epistemic.md#epi-rte-refine-guidance, memory.md#mem-obj-custom-entry]
      note: "Multiple forces coexist at distinct consumers. Unresolved consumers prevent exhaustive authority classification."
    write_agency:
      assessment: partial
      units:
        - scope: "Ordinary session append, default summary admission and workflow result/history persistence"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-session-retention, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation, memory.md#mem-rte-workflow-resume, memory.md#mem-obj-agent-history]
              note: "Software admits entries, generated summaries and live outputs without per-content human approval. User initiation or authorship is not admission control."
          records: [memory.md#mem-rte-session-retention, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation, memory.md#mem-rte-workflow-resume, memory.md#mem-obj-agent-history]
          note: "Default code paths are resolved; substitute payload production/control is separate."
        - scope: "Importer and official-library manager admission after caller request"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update, epistemic.md#epi-rte-import-check]
              note: "Programs admit passing staged trees/snapshots; overwrite/force flags do not authenticate a separate human content decision."
          records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update, epistemic.md#epi-rte-import-check]
          note: "This is the computational admission mechanism, not proof that a caller never obtained human approval."
        - scope: "Verification workflow's explicit default/exception approval and delegated auto-import policies"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification]
              note: "Default import and disclosed backend-limitation exceptions require an explicit informed user decision about the candidate."
            - value: automatic
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Delegated auto-import and model-directed repairs can proceed without a new per-content decision when the policy's conditions hold."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
          note: "Distinct policy alternatives remain claimed; they do not upgrade flag-level implementation to authenticated human approval."
        - scope: "QA metric and recovery report generation"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [epistemic.md#epi-rte-qa-scoring, epistemic.md#epi-rte-recovery-check, epistemic.md#epi-rte-recovery-decision]
              note: "Programs derive and write output records after invocation without per-field human admission."
          records: [epistemic.md#epi-rte-qa-scoring, epistemic.md#epi-rte-recovery-check, epistemic.md#epi-rte-recovery-decision]
          note: "Caller-selected thresholds and files do not make generated report admission manual."
        - scope: "Initial project/skill contents, extension replacements/custom state, checkpoint callback replies and saved-script replacement"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-project-context, memory.md#mem-obj-repo-skills, memory.md#mem-obj-custom-entry, memory.md#mem-rte-branch-navigation, memory.md#mem-rte-workflow-resume]
          note: "Human callback and headless default alternatives are not interchangeable. Content approval and initial/replacement control are not resolved by a generic caller or read API."
      records: [memory.md#mem-rte-session-retention, runtime.md#rt-rte-repo-import, workflow.md#wf-rte-repo-verification, memory.md#mem-obj-custom-entry, memory.md#mem-rte-workflow-resume]
      note: "Automatic implemented admission and manual/automatic policy alternatives are supported separately; opaque initialization and replacement paths remain unresolved."
    curation_operations:
      assessment: partial
      units:
        - scope: "Default conversation compaction and branch summarization"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation]
              note: "Selected history is compressed into retained continuation prose even though original entries remain. Fidelity is not certified."
            - value: evolve
              basis: wired
              records: [memory.md#mem-obj-compaction-summary, runtime.md#rt-rte-context-compaction]
              note: "Repeated compaction passes the previous summary for updating and replaces the active summary projection."
          records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, runtime.md#rt-rte-context-compaction]
          note: "Classifies implemented compression/update, not new-claim synthesis inferred from possible model error."
        - scope: "Workflow diagnostic history reduction"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-agent-history]
              note: "Entry/text budgets reduce raw conversation and tool material to compact diagnostic snippets."
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-agent-history]
              note: "Bounded history favors newest entries and drops older/excess text from the retained diagnostic representation."
          records: [memory.md#mem-obj-agent-history]
          note: "Diagnostic forgetting is local to this representation, not deletion of the original worker traces everywhere."
        - scope: "Managed guidance replacement and workflow cache reuse withdrawal"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update, memory.md#mem-rte-workflow-resume]
              note: "Overwrite/update revises installed entries; new live results replace journal entries at the same index."
            - value: invalidate
              basis: wired
              records: [memory.md#mem-rte-workflow-resume]
              note: "A changed/missing call terminates reuse of the retained matching prefix's successors without requiring wholesale history deletion."
          records: [runtime.md#rt-rte-repo-import, runtime.md#rt-rte-library-update, memory.md#mem-rte-workflow-resume]
          note: "Installation is not automatically consolidation; cache invalidation is not a truth judgment."
        - scope: "Evidence-directed repository and paper guidance repair"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Instructions call for revising failed or thin existing guidance and repeating focused checks."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
          note: "Doctrine supports requested revision, not observed repairs or novel claims."
        - scope: "Extension transformations, router-generator evidence projection and remaining specialized maintenance"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-obj-routing-metadata, memory.md#mem-obj-compaction-summary, epistemic.md#epi-rte-refine-guidance]
          note: "Opaque substitutes and untraced maintenance do not establish deduplication, synthesis or any other controlled operation. Index regeneration alone supplies none."
      records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-agent-history, memory.md#mem-rte-workflow-resume, workflow.md#wf-rte-repo-verification, memory.md#mem-obj-custom-entry]
      note: "Supported operations retain their implementation or policy basis; unresolved transformations prevent exhaustive operation coverage."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Explicit installed-skill invocation and model-directed router/file reads"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-skill-delivery, runtime.md#rt-bap-skill-guidance]
              note: "A named invocation or tool request asks for retained guidance; delivery fulfilling that request is not a second push."
          records: [runtime.md#rt-rte-skill-delivery, runtime.md#rt-bap-skill-guidance]
          note: "Installed/revised bodies qualify; unchanged static shipped files alone do not."
        - scope: "Automatic catalog/project-instruction loading and session branch/summary projection"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-obj-project-context, memory.md#mem-rte-session-retention, memory.md#mem-rte-branch-navigation]
              note: "Context construction automatically selects accumulated content for the next model request without a request for those particular retained parts."
          records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-obj-project-context, memory.md#mem-rte-session-retention, memory.md#mem-rte-branch-navigation]
          note: "An upstream session/branch choice supplies selection inputs but does not turn automatic context selection into a requested file read."
        - scope: "Workflow background completion and journal replay"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-workflow-context]
              note: "Completion/incomplete events select a report projection and inject a follow-up custom message into the foreground."
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-workflow-resume]
              note: "Resumed interpretation requests a call's result and receives a matching cached value instead of invoking a worker."
          records: [memory.md#mem-rte-workflow-context, memory.md#mem-rte-workflow-resume]
          note: "The unsolicited completion report and requested full cached value are different payloads and operations."
        - scope: "Controller review of retained verification/recovery feedback"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-recovery-decision, epistemic.md#epi-rte-refine-guidance]
              note: "Procedures direct controllers to inspect saved results and use feedback for the next refinement cycle."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-recovery-decision, epistemic.md#epi-rte-refine-guidance]
          note: "Instructed consumption is not observed report reading or an automatic file-watching pipeline."
        - scope: "Arbitrary extension state readers, saved-script/nested consumers, exports and remaining evaluator paths"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-rte-workflow-context, memory.md#mem-rte-workflow-resume, epistemic.md#epi-rte-refine-guidance]
          note: "The documented custom-state reload role affords a reader, but its actual selection/delivery direction and remaining consumers are not resolved."
      records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-rte-session-retention, memory.md#mem-rte-workflow-context, memory.md#mem-rte-workflow-resume, memory.md#mem-obj-custom-entry]
      note: "Both directions are supported at named operations; unresolved alternatives cannot be removed from the inventory."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Automatic skill catalog selection on resource load"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-skill-delivery]
              note: "Load/reload triggers role-eligibility and visibility filtering of retained skill descriptions. Availability is not task-targeted semantic retrieval."
          records: [runtime.md#rt-rte-skill-delivery]
          note: "Catalog names do not themselves prove identifier-matched push of skill bodies."
        - scope: "Session tree and checkpoint projection into subsequent model context"
          assessment: known
          findings:
            - value: identifier
              basis: wired
              records: [memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-session-retention, memory.md#mem-rte-branch-navigation]
              note: "Context rebuild follows selected leaf/parent IDs and firstKeptEntryId to select actual retained messages and summaries."
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-session-retention, memory.md#mem-rte-branch-navigation, runtime.md#rt-rte-context-compaction]
              note: "Context rebuilding additionally applies latest-summary/tail and exclusion/budget rules; these are not relevance or embedding judgments."
          records: [memory.md#mem-obj-session-metadata, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-session-retention, memory.md#mem-rte-branch-navigation, runtime.md#rt-rte-context-compaction]
          note: "Identifier targeting and coarse retention controls coexist; summarization generation is not an inferred selector over stored claims."
        - scope: "Automatic project-instruction loading and workflow completion-message projection"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-obj-project-context, memory.md#mem-rte-workflow-context]
              note: "Resource construction selects ancestor/global files; completion events supply a run whose report/verdict/summary fields or truncated fallback are chosen by fixed rules."
          records: [memory.md#mem-obj-project-context, memory.md#mem-rte-workflow-context]
          note: "A path or run ID alone is not evidence of identity-match selection of delivered parts. Neither route establishes semantic search."
        - scope: "Explicit skill reads, journal result requests and instructed report inspection"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-rte-workflow-resume, epistemic.md#epi-rte-refine-guidance]
          note: "These operations fulfill requests for retained material; push signal does not classify their request keys. Separate automatic selectors remain above."
        - scope: "Extension reload/custom-data consumers and remaining push alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-rte-workflow-context]
          note: "Unresolved selection/delivery prevents both a controlled push signal and a pull-only inapplicability conclusion."
      records: [runtime.md#rt-rte-skill-delivery, memory.md#mem-rte-session-retention, memory.md#mem-obj-project-context, memory.md#mem-rte-workflow-context, memory.md#mem-obj-custom-entry]
      note: "Known push operations establish coarse and identifier signals. Model-directed router pulls do not establish inferred-judgment push. Remaining push coverage is unresolved."
    trace_learning:
      assessment: partial
      units:
        - scope: "Default session compaction and default branch-summary generation with later model delivery"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [epistemic.md#epi-rte-summary-generation, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation, memory.md#mem-rte-session-retention]
              note: "History automatically produces retained continuation summaries consumed by later model invocations; human navigation initiation is not summary-content approval."
          records: [epistemic.md#epi-rte-summary-generation, runtime.md#rt-rte-context-compaction, memory.md#mem-rte-branch-navigation, memory.md#mem-rte-session-retention]
          note: "This write-route classification needs neither new knowledge nor measured improvement. Optional activation/cancellation does not negate implemented capacity."
        - scope: "Prescribed feedback-driven repository/paper guidance revision"
          assessment: partial
          findings:
            - value: "yes"
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance, runtime.md#rt-bap-skill-guidance]
              note: "Instructions ask agents to consume execution/usability feedback, revise durable guidance and expose it to later Researcher sessions without universal per-edit human approval."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance, runtime.md#rt-bap-skill-guidance]
          note: "Actual revisions, all feedback inputs and successful future dependence are not traced; manual deployment alternatives remain separate from automatic editing."
        - scope: "Extension compaction/branch substitutes, arbitrary custom state and workflow result/checkpoint alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-workflow-journal, memory.md#mem-rte-workflow-resume]
          note: "Opaque sources and consumers do not establish whether every alternative automatically produces a qualifying behavior-shaping artifact. Journal replay alone is retained-output reuse, not sufficient evidence of trace-fed transformation."
        - scope: "Diagnostic/raw-log-only retention and incompletely traced specialized update routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-agent-history, memory.md#mem-obj-session-messages, epistemic.md#epi-rte-refine-guidance]
          note: "Display and raw retention alone supply no qualifying learning witness. No accepted evidenced-absence record warrants a local no, and remaining specialized paths are incomplete."
      records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-rte-branch-navigation, workflow.md#wf-rte-repo-verification, memory.md#mem-obj-custom-entry, memory.md#mem-obj-agent-history]
      note: "A wired yes is supported; opaque alternatives and incomplete construction paths prevent complete coverage. No local or system-wide no is asserted."
    trace_source:
      assessment: partial
      units:
        - scope: "Original inputs to default compaction and branch-summary writes"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-session-messages, memory.md#mem-rte-branch-navigation]
              note: "Recorded conversational turns feed generated summaries, including prior-summary continuation."
            - value: tool-traces
              basis: wired
              records: [memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, memory.md#mem-obj-session-messages]
              note: "Tool-call/result material and file-operation records feed history text and derived file lists in retained summaries."
          records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-session-messages, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation]
          note: "Covers the recorded default conversation/tool inputs, not opaque extension details. Runtime message-end callbacks do not make the original conversational content event-streams."
        - scope: "Feedback inputs to prescribed verification/recovery guidance revision"
          assessment: partial
          findings:
            - value: tool-traces
              basis: claimed
              records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
              note: "Native execution/test failures and recovery-harness feedback are instructed inputs to guidance repair."
          records: [workflow.md#wf-rte-repo-verification, epistemic.md#epi-rte-refine-guidance]
          note: "Fresh-agent usability outputs, qualitative judgments and original candidate/evidence inputs are not all content-individuated; no complete trace-source union follows."
        - scope: "Extension-supplied checkpoints/custom data and unresolved workflow/specialized update alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-custom-entry, memory.md#mem-obj-compaction-summary, memory.md#mem-obj-workflow-journal, memory.md#mem-rte-workflow-resume, epistemic.md#epi-rte-refine-guidance]
          note: "Neither qualifying trace learning nor original inputs are settled for these alternatives. Opaque JSON, cached outcomes and event callbacks do not establish trajectories or event-stream sources."
      records: [epistemic.md#epi-rte-summary-generation, memory.md#mem-obj-compaction-summary, memory.md#mem-rte-branch-navigation, workflow.md#wf-rte-repo-verification, memory.md#mem-obj-custom-entry]
      note: "Session logs and tool traces are locally supported for qualifying writes. Unresolved provenance precludes completeness or axis-wide inapplicability."
---

# AREX-Skill memory profile

## Comparison rationale

The profile classifies accepted records, not the entire application's storage.
Installed or revised guidance qualifies when later discovery or body reads consume
it. Static bundled procedures alone do not establish accumulated memory. The
filesystem claim follows [MEM-OBJ-repo-skills](memory.md#mem-obj-repo-skills),
not the fact that the source was acquired from Git. Provider weights remain an
external component, not an inferred memory substrate.

The ten inventories remain partial. Known container storage does not determine
opaque payload form, lineage, admission or consumer force. In particular,
[MEM-OBJ-custom-entry](memory.md#mem-obj-custom-entry) distinguishes arbitrary
state/details from model-facing custom-message content.
[MEM-OBJ-workflow-journal](memory.md#mem-obj-workflow-journal) distinguishes the
full interpreter value from readable report previews. Remaining specialized
maintenance and script/evaluator paths have no complete accepted-record inventory;
no value is supplied merely from a filename or a coverage-table mention.

Default continuation summaries establish automatic trace-fed retention and later
consumption through [EPI-RTE-summary-generation](epistemic.md#epi-rte-summary-generation),
[RT-RTE-context-compaction](runtime.md#rt-rte-context-compaction) and
[MEM-RTE-branch-navigation](memory.md#mem-rte-branch-navigation). Their learning
force at the update consumer and knowledge force at the later model are separate.
This does not contradict an indeterminate epistemic content relation: intended
compression establishes the curation mechanism, not fidelity, new warranted
claims or improved future capacity. No synthesis value follows from possible
summarization error.

Diagnostic truncation in [MEM-OBJ-agent-history](memory.md#mem-obj-agent-history)
reduces retained content and preferentially forgets older material, but its
established consumer is display. Raw log retention and symbolic result replay
likewise do not automatically inherit the summary route's trace-learning value.
There are no accepted evidenced-absence records warranting a local trace-learning
negative. The supported wired positive survives in a derived union without
turning unresolved alternatives into known units.

Read-back separates automatic context supply from requested retrieval.
[RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) supports catalog push and
explicit body pull. Router-guided model judgment belongs to demand-driven reads,
not inferred-judgment push. Session projection actually matches retained tree
identities; catalog names and requested file paths alone do not establish that
signal. [MEM-RTE-workflow-context](memory.md#mem-rte-workflow-context) pushes a
fixed report projection at completion, whereas
[MEM-RTE-workflow-resume](memory.md#mem-rte-workflow-resume) returns a requested
cached value. Neither is an embedding retrieval mechanism.

Admission also has distinct layers. The software transactions in
[RT-RTE-repo-import](runtime.md#rt-rte-repo-import) and
[RT-RTE-library-update](runtime.md#rt-rte-library-update) admit content
computationally. The explicit approval alternatives in
[WF-RTE-repo-verification](workflow.md#wf-rte-repo-verification) support manual
agency only at the policy layer. Starting a workflow or supplying an overwrite
flag is not authenticated per-content human approval. Initial authorship and
extension replacement control remain unresolved.

Reconciliation supersedes the memory member's repository verification/revision
route with [WF-RTE-repo-verification](workflow.md#wf-rte-repo-verification).
All affected curation, agency and feedback classifications use that canonical
record. [EPI-RTE-refine-guidance](epistemic.md#epi-rte-refine-guidance) additionally
covers paper refinement and is not superseded. The graph and summary objects
with overlapping extents remain valid separate records; narrower text witnesses
do not resolve arbitrary details or all candidate lifecycle stages.

Source-read log: none. This classification used only the supplied accepted
members and reconciliation; no frozen source ambiguity required an additional
read. All warrants and evidence layers remain in the cited records. No observed
operation or causal benefit is inferred.
