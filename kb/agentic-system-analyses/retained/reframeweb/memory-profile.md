---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "ReframeWeb memory profile covering graph guidance and history, linked instructions, checkpoint/recovery inputs, saved startup configuration and retained evidence at the frozen commit."
run-id: "AAS-2026-10-14-reframeweb-cff918d7eb1e-01"
source-identity: "https://github.com/jubjub727/ReframeWeb"
reviewed-boundary: "318987dcde9a016f8e3db819ed9a73abf6b3ad81"
memory-comparison:
  version: 2
  scope: "Included: retained graph guidance/preferences, sessions/messages/locators, instruction/task links and task/provider/startup configuration; tool histories and derived later-invocation summaries; directory/checkpoint locators, retained workspace/recovery bytes, image evidence and private startup-result evidence, including unresolved provenance, payload and later-consumer alternatives. Excluded: shipped static prompts/instructions before use-time adoption, transient orchestration/attempt controls as independent durable memory, provider model weights and hidden Codex/provider compaction, arbitrary native Store/UI internal state without demonstrated agent-memory delivery, and benchmark metrics as an automatic production updater. External exclusions do not resolve unknown included initialization or native maintenance."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Guidance, preferences, session/conversation content, instruction bodies, filesystem locators, task receipts and saved Store/task configuration in the graph"
          assessment: "known"
          findings:
            - value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-instruction-memory"
                - "memory.md#mem-obj-filesystem-memory"
                - "memory.md#mem-obj-task-history"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-rte-application-publish"
              note: "Graph membership, task links, conversation relations and saved reference structures are consumed by later host routes."
          records:
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-task-history"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-application-publish"
          note: "These are operative graph nodes and relations, not the checkpoint bytes they identify."
        - scope: "Configured local SurrealKV backing for graph context collections"
          assessment: "known"
          findings:
            - value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-memory"
              note: "The recorded database configuration names local SurrealKV."
          records:
            - "memory.md#mem-obj-context-memory"
          note: "This is the local backing alternative; the graph organization remains a separate finding."
        - scope: "Configured remote graph database physical backing"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-memory"
          note: "The adapter establishes remote graph storage, but no accepted record establishes its underlying physical substrate. This does not add vector or service-object storage."
        - scope: "Checkpoint and recovery backing store"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-store"
              note: "workspace.sqlite3 stores workspace metadata."
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-store"
              note: "blobs and sessions directories retain checkpoint payloads and recovery files."
          records:
            - "memory.md#mem-obj-workspace-store"
          note: "Native Store layout identifies both metadata database and payload/session directories."
        - scope: "Derived summary retained between producer and later completion/retry invocation"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
                - "epistemic.md#epi-obj-output-summary"
              note: "Summary values are retained in invocation state and supplied to subsequent model calls."
          records:
            - "memory.md#mem-rte-history-summary"
            - "epistemic.md#epi-obj-output-summary"
          note: "The later-consumer summary occupies current BAML values, not a demonstrated cross-session summary index."
        - scope: "Screenshot originals/previews and private candidate result.json"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-obj-test-result"
              note: "Workspace verification-evidence retains images; fixture-root result.json retains test evidence."
          records:
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-obj-test-result"
          note: "Both records identify filesystem retention independently of graph locators."
        - scope: "Registered mutable directory payload backing"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-workspace-store"
          note: "A directory path is wired as a materialization source, but the records do not classify every backing implementation or contained artifact."
      records:
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-obj-filesystem-memory"
        - "memory.md#mem-obj-task-history"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-rte-application-publish"
        - "memory.md#mem-obj-workspace-store"
        - "memory.md#mem-rte-history-summary"
        - "epistemic.md#epi-obj-output-summary"
        - "epistemic.md#epi-obj-rendered-evidence"
        - "epistemic.md#epi-obj-test-result"
      note: "Graph content, local/remote database adaptation, checkpoint/recovery storage and evidence files are classified. The remote database backing and mutable-directory contents prevent a complete physical-substrate inventory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Guidance/preferences, conversation/session prose, instruction bodies and locator display prose at model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-instruction-memory"
                - "memory.md#mem-bap-linked-instructions"
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-rte-project-locator"
              note: "Titles, descriptions, messages and instructions supply interpreted context or standing directions."
          records:
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-bap-linked-instructions"
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-rte-project-locator"
          note: "The model interprets prose; symbolic JSON wrappers are classified separately."
        - scope: "Graph identity, roles, collection/task relations, filesystem dependency manifests and saved startup/task configuration"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-instruction-memory"
                - "memory.md#mem-obj-filesystem-memory"
                - "memory.md#mem-obj-workspace-store"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-rte-application-publish"
              note: "IDs, roles, relevance flags, dependencies, startup references and tool/model selections have fixed-rule consumers."
          records:
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-workspace-store"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-application-publish"
          note: "Fixed host rules resolve these localized fields."
        - scope: "Raw tool history and derived completion summary"
          assessment: "partial"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-history"
              note: "Call/task/attempt IDs and outcome status have localized fields."
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
              note: "Action-history summarizer emits prose consumed by completion checking."
          records:
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-history-summary"
          note: "Call/outcome metadata and rendered summary prose are resolved; arbitrary JSON result/artifact bodies may carry other forms."
        - scope: "Checkpoint and directory payloads materialized for tasks or executable startup"
          assessment: "partial"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-store"
                - "memory.md#mem-bap-linked-instructions"
              note: "Retained instruction content supplies model-interpreted text in prepared workspaces."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-store"
                - "runtime.md#rt-rte-saved-store"
              note: "Source/executable artifacts and their fixed-rule startup references are operative symbolic parts."
          records:
            - "memory.md#mem-obj-workspace-store"
            - "memory.md#mem-bap-linked-instructions"
            - "runtime.md#rt-rte-saved-store"
          note: "Instruction prose and source/executable artifacts are supported parts, but opaque binaries and arbitrary files prevent a complete form inventory."
        - scope: "Image-path/MIME/dimension metadata and candidate-test status/error fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-obj-test-result"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Path/MIME/dimension and test-status fields are interpreted by program rules."
            - value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-obj-test-result"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Error descriptions are human/model-interpreted text."
          records:
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "This unit excludes actual image scene content."
        - scope: "Full PNG/JPEG scene content at later visual inference"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "The record establishes image observations but not a controlled representational form for their semantic content; numerical byte encoding alone does not establish parametric form."
      records:
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-bap-linked-instructions"
        - "memory.md#mem-rte-context-reload"
        - "memory.md#mem-rte-project-locator"
        - "memory.md#mem-obj-filesystem-memory"
        - "memory.md#mem-obj-workspace-store"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-rte-application-publish"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-history-summary"
        - "epistemic.md#epi-obj-rendered-evidence"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-panel-evidence"
      note: "Text and fixed-rule metadata are separable. Images and arbitrary checkpoint/tool payloads are not classified from display summaries. No recorded retained model-weight payload establishes parametric memory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Model-proposed guidance admitted to five decision collections"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-guidance-review"
                - "memory.md#mem-obj-context-memory"
              note: "Decision-layer observations become reviewed title/description guidance during requests."
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "memory.md#mem-obj-context-memory"
          note: "The memory annotation establishes an observation-to-retained-guidance derivation, not all initial collection provenance."
        - scope: "Recorded human/validation messages, tool receipts and generated locator metadata"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-project-locator"
              note: "Host callback activity, tool outcomes and verified/saved project activity produce retained records."
          records:
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-project-locator"
          note: "These host writes record activity; this lineage does not by itself establish trace learning."
        - scope: "Action-history reduction to completion summary"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
                - "memory.md#mem-obj-task-history"
              note: "The summarizer extracts a reduced account of recorded tool activity."
          records:
            - "memory.md#mem-rte-history-summary"
            - "memory.md#mem-obj-task-history"
          note: "The summary derives from rendered recorded actions, with fidelity unobserved."
        - scope: "Caller-authored project locator description"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-project-locator"
              note: "The locator route accepts caller-authored descriptive content alongside generated verification/provenance fields."
          records:
            - "memory.md#mem-rte-project-locator"
          note: "Descriptive prose is separately supplied by the caller; its authorship does not settle human admission agency."
        - scope: "Application instruction file imported into retained instruction memory"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-application-publish"
                - "memory.md#mem-obj-instruction-memory"
              note: "Application instruction content is acquired from the publication source file."
          records:
            - "runtime.md#rt-rte-application-publish"
            - "memory.md#mem-obj-instruction-memory"
          note: "The shipped publisher reads instructions.md and publishes instruction memories; original authorship remains separate."
        - scope: "Graph import via standalone old-to-target database merge"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-memory-migration"
              note: "Source records are preserved into a different target database."
          records:
            - "memory.md#mem-rte-memory-migration"
          note: "This is an explicit afforded maintenance route, not observed migration."
        - scope: "Pre-existing guidance/preferences, arbitrary session content, instruction initialization and original workspace payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-workspace-store"
          note: "Records do not determine who first supplied these parts or their full derivations. The user-authored root label does not prove actual authored lineage for all instruction entries."
        - scope: "Assembled task root AGENTS.md and materialized checkpoint composition"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-bap-linked-instructions"
                - "memory.md#mem-obj-instruction-memory"
                - "memory.md#mem-obj-filesystem-memory"
                - "memory.md#mem-obj-workspace-store"
                - "runtime.md#rt-rte-saved-store"
              note: "Task preparation assembles retained linked bodies; dependency resolution combines referenced source material."
          records:
            - "memory.md#mem-bap-linked-instructions"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-workspace-store"
            - "runtime.md#rt-rte-saved-store"
          note: "These are compiled delivery artifacts rather than independently mined lessons."
        - scope: "Screenshot original and generated lossy preview"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Native-returned PNG enters the retained workspace evidence files."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Resize, white composition and JPEG encoding generate the model preview."
          records:
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Original rendering is acquired from native output; preview is derived from the acquired image."
        - scope: "Private startup test result"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-test-result"
                - "epistemic.md#epi-rte-candidate-startup"
              note: "Startup and cleanup observations produce persisted result fields."
          records:
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-candidate-startup"
          note: "Program observations generate fixture evidence rather than an accepted general lesson."
      records:
        - "runtime.md#rt-rte-guidance-review"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-project-locator"
        - "memory.md#mem-rte-history-summary"
        - "runtime.md#rt-rte-application-publish"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-rte-memory-migration"
        - "memory.md#mem-obj-workspace-store"
        - "memory.md#mem-bap-linked-instructions"
        - "memory.md#mem-obj-filesystem-memory"
        - "runtime.md#rt-rte-saved-store"
        - "epistemic.md#epi-obj-rendered-evidence"
        - "epistemic.md#epi-rte-panel-evidence"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-candidate-startup"
      note: "Known proposal, receipt, publication and import derivations coexist with unknown initial content and arbitrary payload provenance. A generated or copied artifact is not thereby trace-extracted."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Guidance text at later decision-layer model prompts"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-guidance-review"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-rte-context-reload"
              note: "Reloaded guidance directs task choice, search, breadth, relevance and composition."
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-rte-context-reload"
          note: "Reusable decision guidance provides standing directions, without guaranteed compliance."
        - scope: "Retained tool history at the action-summary update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-history-summary"
              note: "The summarizer consumes retained tool outcomes to produce a behavior-shaping summary retained for later completion/retry invocations."
          records:
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-history-summary"
          note: "This learning authority belongs to the recorded-history input at summary production, not transient guidance candidates. The summary's later knowledge authority is classified separately; cross-session retention and improved capacity are not established."
        - scope: "Decision observations as retained inputs at the guidance-update consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "epistemic.md#epi-rte-guidance-check"
            - "epistemic.md#epi-obj-candidate-entry"
          note: "Candidates are transient staged groups; the records establish no retained decision-observation input delivered to review. Stored guidance is supplied, but no separately supported learning force for it is established. The trace-learning write positive does not establish this input authority."
        - scope: "Conversation/session/preference context and tool history at later relevance, composition and summary models"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-rte-graph-selection"
                - "memory.md#mem-rte-history-summary"
              note: "Remembered assertions, preferences and receipts supply model context or reference."
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-rte-graph-selection"
                - "memory.md#mem-rte-history-summary"
              note: "Retained candidate prose and metadata influence the relevance model's relative selection of candidates."
          records:
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-rte-graph-selection"
            - "memory.md#mem-rte-history-summary"
          note: "Context and evidence are distinct from enforced task permissions."
        - scope: "Linked instruction bodies at direct task execution and Codex preparation"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-instruction-memory"
                - "memory.md#mem-bap-linked-instructions"
              note: "Appended bodies and assembled root AGENTS.md supply standing execution directions."
          records:
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-bap-linked-instructions"
          note: "Prose interpretation is not permission enforcement."
        - scope: "Graph identities, relevance flags and filesystem dependencies at host selection/materialization"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-filesystem-memory"
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-rte-graph-selection"
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-rte-memory-migration"
              note: "Collection/session bindings, relevance flags and dependency IDs determine delivery scope and materialized inputs."
          records:
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-rte-graph-selection"
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-rte-memory-migration"
          note: "The consumed fields select memory input and preparation sources."
        - scope: "Saved task tool grants and Store activation/reference configuration at dispatch and guest checks"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-application-publish"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-bap-store-callback"
                - "runtime.md#rt-obj-tool-attempt"
              note: "Saved task/provider/startup metadata select executor, operation inputs and next-launch artifacts."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-application-publish"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-bap-store-callback"
                - "runtime.md#rt-obj-tool-attempt"
              note: "Saved grants and current revision bindings permit or reject covered tool/guest operations."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-application-publish"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-bap-store-callback"
                - "runtime.md#rt-obj-tool-attempt"
              note: "Expected retained content and saved references are criteria for admitting Store/task metadata changes."
          records:
            - "runtime.md#rt-rte-application-publish"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-bap-store-callback"
            - "runtime.md#rt-obj-tool-attempt"
          note: "Only retained grant/configuration parts are included; transient attempt state is not a new durable corpus."
        - scope: "Stored instruction body at guarded instruction replacement"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-node-curation"
                - "memory.md#mem-obj-instruction-memory"
              note: "Current instruction text must match expected text before replacement."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-node-curation"
                - "memory.md#mem-obj-instruction-memory"
              note: "A concurrent-content mismatch vetoes the replacement."
          records:
            - "memory.md#mem-rte-node-curation"
            - "memory.md#mem-obj-instruction-memory"
          note: "The expected-text comparison uses retained content as an admission criterion, independently of downstream instruction force."
        - scope: "Retained source files supplied as editable task workspace inputs"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-store"
                - "memory.md#mem-obj-filesystem-memory"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-rte-codex-task"
              note: "Retained files provide task context and reference material in the prepared workspace."
          records:
            - "memory.md#mem-obj-workspace-store"
            - "memory.md#mem-obj-filesystem-memory"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-codex-task"
          note: "This covers inspected materialization for later task work, not every opaque payload or startup executable effect."
        - scope: "Retained image evidence at subsequent model turns"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-rendered-evidence"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Selected original/preview images inform the next model inference."
          records:
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Rendering is advisory visual evidence, not a universal success oracle."
        - scope: "Derived action summary at completion/retry consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
              note: "Outcome assertions inform subsequent completion and retry decisions."
          records:
            - "memory.md#mem-rte-history-summary"
          note: "The summary supplies outcome context; completion verdicts are separate consumers and not retained-summary enforcement."
        - scope: "Arbitrary checkpoint/directory payloads and private test/report evidence beyond their immediate caller"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-workspace-store"
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-candidate-startup"
          note: "Executable startup and model-visible instructions are classified above. Other payload effects and mandatory later production report consumption are not established."
      records:
        - "runtime.md#rt-rte-guidance-review"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-rte-context-reload"
        - "epistemic.md#epi-rte-guidance-check"
        - "epistemic.md#epi-obj-candidate-entry"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-graph-selection"
        - "memory.md#mem-rte-history-summary"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-bap-linked-instructions"
        - "memory.md#mem-obj-filesystem-memory"
        - "memory.md#mem-rte-memory-migration"
        - "runtime.md#rt-rte-application-publish"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-bap-store-callback"
        - "runtime.md#rt-obj-tool-attempt"
        - "memory.md#mem-rte-node-curation"
        - "memory.md#mem-obj-workspace-store"
        - "runtime.md#rt-rte-codex-task"
        - "epistemic.md#epi-obj-rendered-evidence"
        - "epistemic.md#epi-rte-panel-evidence"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-candidate-startup"
      note: "Authority follows the consumed retained part, not a uniform memory role. Retained tool history has learning force at summary production; transient guidance proposals do not establish a retained-observation learning consumer. Advice, standing directions, selector inputs and saved controls differ. Guidance-update input authority, opaque payloads and durable test-report consumers remain incompletely resolved."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Reviewed candidate guidance admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-guidance-review"
              note: "Review-model and software admission governs the retained guidance batch."
          records:
            - "runtime.md#rt-rte-guidance-review"
          note: "Models propose/keep; code intersects IDs and persists without a per-content human decision."
        - scope: "Human/validation reply recording, tool outcome recording, history summarization, image persistence and startup-result generation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-memory"
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-history-summary"
                - "epistemic.md#epi-rte-panel-evidence"
                - "epistemic.md#epi-rte-candidate-startup"
              note: "Callbacks, receipt writers, summarizer and evidence programs admit these generated parts."
          records:
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-history-summary"
            - "epistemic.md#epi-rte-panel-evidence"
            - "epistemic.md#epi-rte-candidate-startup"
          note: "Host/model production and admission is not replaced by human approval of each recorded object."
        - scope: "Human browser UI exact-content edits and confirmed deletion"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-node-curation"
              note: "A human using the shipped UI chooses the content or confirms deletion."
          records:
            - "memory.md#mem-rte-node-curation"
          note: "The record distinguishes this UI branch from arbitrary HTTP callers; no interaction was observed."
        - scope: "Schema-driven locator visibility update"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-migration"
              note: "apply_schema changes matching locator flags by software predicate."
          records:
            - "memory.md#mem-rte-memory-migration"
          note: "Automatic migration is distinct from caller-controlled graph import."
        - scope: "Direct browser API edits, assigned Store instruction edits, project locator/save calls, graph import and Store/application publication"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-node-curation"
            - "memory.md#mem-rte-project-locator"
            - "memory.md#mem-rte-memory-migration"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-application-publish"
          note: "Generic caller identity and invocation alone do not establish explicit human content approval or exclude it. Their guards are known, but per-content admission control is unresolved."
        - scope: "Initial preferences, guidance, arbitrary sessions, instructions and directory/checkpoint source content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-workspace-store"
          note: "Known later writers do not settle initialization agency."
      records:
        - "runtime.md#rt-rte-guidance-review"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-history-summary"
        - "epistemic.md#epi-rte-panel-evidence"
        - "epistemic.md#epi-rte-candidate-startup"
        - "memory.md#mem-rte-node-curation"
        - "memory.md#mem-rte-memory-migration"
        - "memory.md#mem-rte-project-locator"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-rte-application-publish"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-obj-filesystem-memory"
        - "memory.md#mem-obj-workspace-store"
      note: "Known computational admissions and exact-content browser UI decisions coexist with unspecified generic API/script callers and unresolved initialization. Workflow initiation does not settle those mechanisms."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Recorded action history to reduced completion summary"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
                - "memory.md#mem-obj-task-history"
              note: "The summarizer reduces retained actions into a completion account of their existing outcomes."
          records:
            - "memory.md#mem-rte-history-summary"
            - "memory.md#mem-obj-task-history"
          note: "The raw history remains separately graph-backed; no new durable general claim is required for this reduction."
        - scope: "Graph content and attached instruction replacement; application task edits; locator visibility migration"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-node-curation"
                - "memory.md#mem-rte-memory-migration"
                - "runtime.md#rt-rte-application-publish"
              note: "PATCH/guarded replacement revise entries; application publication edits existing task prompts/grants; schema migration revises locator visibility fields."
          records:
            - "memory.md#mem-rte-node-curation"
            - "memory.md#mem-rte-memory-migration"
            - "runtime.md#rt-rte-application-publish"
          note: "Each revises an existing retained part rather than only adding or rebuilding an index."
        - scope: "Browser deletion of node and incident relations"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-node-curation"
              note: "Confirmed graph deletion removes the retained node and its incident edges from later delivery."
          records:
            - "memory.md#mem-rte-node-curation"
          note: "Deletion forgets this graph memory; it does not establish history-preserving invalidation or reclamation of checkpoint bytes."
        - scope: "Guidance review and arbitrary candidate semantics"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "epistemic.md#epi-rte-guidance-check"
          note: "The reviewer is asked for distinct durable lessons, but kept-ID filtering neither merges duplicates nor proves synthesis, consolidation or promotion of existing retained content."
        - scope: "Native workspace retention/blob cleanup and arbitrary payload maintenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-workspace-store"
          note: "Uninspected cleanup leaves prevent a complete forgetting/maintenance classification."
        - scope: "Model composition semantics and visual-preview reduction relative to controlled curation vocabulary"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-graph-selection"
            - "epistemic.md#epi-obj-rendered-evidence"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Composition fidelity is unresolved; lossy image resizing is established but does not by itself establish one of the claim-level curation operations."
      records:
        - "memory.md#mem-rte-history-summary"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-node-curation"
        - "memory.md#mem-rte-memory-migration"
        - "runtime.md#rt-rte-application-publish"
        - "runtime.md#rt-rte-guidance-review"
        - "epistemic.md#epi-rte-guidance-check"
        - "memory.md#mem-obj-workspace-store"
        - "memory.md#mem-rte-graph-selection"
        - "epistemic.md#epi-obj-rendered-evidence"
        - "epistemic.md#epi-rte-panel-evidence"
      note: "Implemented summary reduction, retained-entry edits and graph deletion support positives. Guidance review criteria do not establish deduplication or synthesis; native cleanup and content-dependent transformations remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Graph search and history rendering requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-graph-selection"
                - "memory.md#mem-rte-history-summary"
              note: "Host retrieval fulfills model search plans and summarizer history requests."
          records:
            - "memory.md#mem-rte-graph-selection"
            - "memory.md#mem-rte-history-summary"
          note: "A consumer requests stored material by search plan or task history ID; fulfilling that request is pull."
        - scope: "Automatic cycle context reload"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-obj-session-memory"
              note: "Automatic loaders supply retained guidance, preferences and current non-relevance/session conversation context."
          records:
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
          note: "Cycle start supplies collections and acceptance-bound session/conversation context without an individual memory request."
        - scope: "Relevance selection within requested graph retrieval"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-graph-selection"
              note: "Kept-ID selection supplies a filtered retained context to the composer."
          records:
            - "memory.md#mem-rte-graph-selection"
          note: "The relevance model automatically selects retained candidates for composition; the upstream requested retrieval remains pull."
        - scope: "Task-linked instructions, selected project files, retry workspace and startup artifact supply"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-bap-linked-instructions"
                - "memory.md#mem-obj-filesystem-memory"
                - "memory.md#mem-obj-workspace-store"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-rte-codex-task"
              note: "Host preparation and startup automatically supply explicit task/Store-linked bodies, files and configuration."
          records:
            - "memory.md#mem-bap-linked-instructions"
            - "memory.md#mem-obj-filesystem-memory"
            - "memory.md#mem-obj-workspace-store"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-codex-task"
          note: "Task/startup triggers select associated retained material rather than a new consumer query for every delivered part."
        - scope: "Derived completion summary and newest-eight retained image supply"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Summary replaces raw history for completion; completed-image selector attaches recent images to next inference."
          records:
            - "memory.md#mem-rte-history-summary"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Later completion/visual model invocations receive selected retained representations automatically."
        - scope: "Private test result.json, arbitrary workspace payloads and benchmark-report later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-candidate-startup"
            - "memory.md#mem-obj-workspace-store"
            - "epistemic.md#epi-rte-benchmark-checks"
          note: "Return/storage capability alone does not establish all later invocation routes."
      records:
        - "memory.md#mem-rte-graph-selection"
        - "memory.md#mem-rte-history-summary"
        - "memory.md#mem-rte-context-reload"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-bap-linked-instructions"
        - "memory.md#mem-obj-filesystem-memory"
        - "memory.md#mem-obj-workspace-store"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-rte-codex-task"
        - "epistemic.md#epi-rte-panel-evidence"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-candidate-startup"
        - "epistemic.md#epi-rte-benchmark-checks"
      note: "Requested history/graph retrieval and automatic memory supply coexist within chains. Private result-file later use and arbitrary workspace/provider consumers remain unresolved, so known routes are not a complete read-back inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Cycle-start guidance/preference collection supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-obj-context-memory"
              note: "Whole decision collections are supplied without content-specific targeting."
          records:
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-obj-context-memory"
          note: "Trigger is a BAML cycle; selector input is collection membership; selected parts are all returned entries. Timestamp ordering is not a numerical budget."
        - scope: "Cycle-start session/conversation supply"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-obj-session-memory"
              note: "Current session/conversation identity matches select delivered context."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-reload"
                - "memory.md#mem-obj-session-memory"
              note: "relevance_required and role filters omit whole classes of retained parts."
          records:
            - "memory.md#mem-rte-context-reload"
            - "memory.md#mem-obj-session-memory"
          note: "Trigger is context loading; acceptance-bound IDs select the current records, with relevance flags and role filters further bounding parts."
        - scope: "Relevance-model candidate selection for composer"
          assessment: "known"
          findings:
            - value: "inferred-judgment"
              basis: "wired"
              records:
                - "memory.md#mem-rte-graph-selection"
              note: "The relevance model selects retained messages, preferences and locator/context parts for composition."
          records:
            - "memory.md#mem-rte-graph-selection"
          note: "Trigger is retrieval completion; model examines request plus candidate text/metadata and keeps candidate IDs. IDs encode its decision rather than replacing semantic judgment."
        - scope: "Task/selected-Store associations and next-launch startup selection"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-bap-linked-instructions"
                - "memory.md#mem-obj-filesystem-memory"
                - "runtime.md#rt-rte-saved-store"
                - "runtime.md#rt-rte-codex-task"
              note: "Task links, selected Store IDs, filesystem dependencies and startup membership identify supplied retained parts."
          records:
            - "memory.md#mem-bap-linked-instructions"
            - "memory.md#mem-obj-filesystem-memory"
            - "runtime.md#rt-rte-saved-store"
            - "runtime.md#rt-rte-codex-task"
          note: "Task execution/preparation and Host launch trigger actual link/reference resolution. Selected identity matches determine delivered instructions, checkpoint sources and executable startup artifacts."
        - scope: "Completion summary delivery and image attachment window"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-summary"
                - "epistemic.md#epi-rte-panel-evidence"
              note: "Attempt-stage supply and newest-eight image filtering select retained parts by availability/type/recency rather than semantic relevance."
          records:
            - "memory.md#mem-rte-history-summary"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Attempt completion supplies its derived summary; before next model turn completed observations/image MIME and newest-eight availability filter selected originals/previews."
        - scope: "Other workspace payload/evidence-report delivery selectors"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-workspace-store"
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-candidate-startup"
          note: "The records do not establish a later selector for all included retained payloads; no pull-only inapplicability follows."
      records:
        - "memory.md#mem-rte-context-reload"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-rte-graph-selection"
        - "memory.md#mem-bap-linked-instructions"
        - "memory.md#mem-obj-filesystem-memory"
        - "runtime.md#rt-rte-saved-store"
        - "runtime.md#rt-rte-codex-task"
        - "memory.md#mem-rte-history-summary"
        - "epistemic.md#epi-rte-panel-evidence"
        - "memory.md#mem-obj-workspace-store"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-candidate-startup"
      note: "Each supported signal names a push selector. Search requests are pull even when lexical hints determine the requested results; relevance-model selection supplies a separate inferred-judgment push. Other retained evidence/payload delivery remains unresolved."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Decision-layer observation to reviewed durable guidance to later decision prompt"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-guidance-review"
                - "memory.md#mem-obj-context-memory"
                - "memory.md#mem-rte-context-reload"
              note: "Automatic observation-fed proposal/review writes behavior-shaping guidance for later turns."
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-rte-context-reload"
          note: "The memory annotation explicitly establishes this qualifying automatic trace-fed guidance architecture. No accepted factual generalization or improved capacity is implied."
        - scope: "Recorded action history to retained completion/retry summary"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-history-summary"
              note: "Automatic trace-fed summary production shapes later completion/retry context under the shared summary read-back definition."
          records:
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-history-summary"
          note: "The summary replaces raw retained action history at a later consumer invocation within the request. Its attained retention horizon is that later invocation, not a demonstrated cross-session summary index."
        - scope: "Verified/saved locator admission and later relevance consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-project-locator"
            - "memory.md#mem-obj-session-memory"
          note: "Activity/provenance is retained and later selected, but per-content human control and whether this is a qualifying automatic behavior-shaping update are unresolved."
        - scope: "Initial guidance/preferences/session content and arbitrary checkpoint/instruction update histories"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-workspace-store"
            - "memory.md#mem-rte-node-curation"
            - "runtime.md#rt-rte-application-publish"
          note: "No complete automatic trace-fed derivation is established for these alternatives. Known instruction delivery does not supply the missing update provenance."
        - scope: "Private startup test evidence and retained screenshots beyond evidence supply"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-candidate-startup"
            - "epistemic.md#epi-rte-panel-evidence"
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-obj-rendered-evidence"
          note: "These establish evidence retention and advisory context, not a recorded automatic trace-to-derived behavior-shaping update for every evidence part. No bounded absence record supports a local no."
      records:
        - "runtime.md#rt-rte-guidance-review"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-rte-context-reload"
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-history-summary"
        - "memory.md#mem-rte-project-locator"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-obj-workspace-store"
        - "memory.md#mem-rte-node-curation"
        - "runtime.md#rt-rte-application-publish"
        - "epistemic.md#epi-rte-candidate-startup"
        - "epistemic.md#epi-rte-panel-evidence"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-obj-rendered-evidence"
      note: "Qualifying reviewed decision guidance and within-request retained summary supply are wired, not observed improvement. Image/log retention alone is insufficient. Generic locator control, initial content and arbitrary payload updates prevent a complete positive/negative inventory."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original recorded actions feeding the qualifying completion-summary write"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-task-history"
                - "memory.md#mem-rte-history-summary"
              note: "Recorded action inputs/outputs and tool outcomes are the original trace content for this summary."
          records:
            - "memory.md#mem-obj-task-history"
            - "memory.md#mem-rte-history-summary"
          note: "The history render feeds tool requests/results/outcome activity into summary production."
        - scope: "Original decision observations feeding reviewed guidance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-guidance-review"
            - "epistemic.md#epi-rte-guidance-check"
            - "epistemic.md#epi-obj-candidate-entry"
          note: "Observed interaction is the requested source, but the records do not identify its original content as conversational turns, discrete events, tool traces or linked trajectories. The reviewer receives candidate/stored text without a separate trace argument."
        - scope: "Potential locator, initial-content, instruction/checkpoint and evidence-derived learning inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-project-locator"
            - "memory.md#mem-obj-context-memory"
            - "memory.md#mem-obj-session-memory"
            - "memory.md#mem-obj-instruction-memory"
            - "memory.md#mem-obj-workspace-store"
            - "epistemic.md#epi-obj-test-result"
            - "epistemic.md#epi-rte-panel-evidence"
          note: "Qualifying automatic learning writes are unresolved for these parts. Their activity or import labels cannot establish controlled trace_source values."
      records:
        - "memory.md#mem-obj-task-history"
        - "memory.md#mem-rte-history-summary"
        - "runtime.md#rt-rte-guidance-review"
        - "epistemic.md#epi-rte-guidance-check"
        - "epistemic.md#epi-obj-candidate-entry"
        - "memory.md#mem-rte-project-locator"
        - "memory.md#mem-obj-context-memory"
        - "memory.md#mem-obj-session-memory"
        - "memory.md#mem-obj-instruction-memory"
        - "memory.md#mem-obj-workspace-store"
        - "epistemic.md#epi-obj-test-result"
        - "epistemic.md#epi-rte-panel-evidence"
      note: "The qualifying history-summary input is recorded tool activity. The guidance route qualifies, but its original observation content is not classified by the accepted records; candidate narration is not a separate interaction trace. Other potential routes retain their qualification uncertainty."
---

# ReframeWeb memory profile

## Comparison rationale

### Boundary and evidence strength

The profile classifies retained operative parts, not every place the enclosing
runtime stores a value. Graph organization and local KV backing coexist;
checkpoint bytes have SQLite metadata and filesystem payloads. Locator display
prose does not classify file bytes, and symbolic image descriptors do not classify
the rendered scene. See [MEM-OBJ-context-memory](memory.md#mem-obj-context-memory),
[MEM-OBJ-workspace-store](memory.md#mem-obj-workspace-store), and
[EPI-OBJ-rendered-evidence](epistemic.md#epi-obj-rendered-evidence).

The supplied reconciliation makes no supersession. Containers and their declared
parts therefore retain separate canonical citations. Findings use implementation
warrants except the standalone import's afforded invocation. No observation or
causal experiment upgrades the mechanisms to exercised operation, reliable
compliance, factual acceptance or beneficial learning.

### Admission, transformation and force

Human exact-content browser edits support manual agency; unspecified API/script
callers do not. Automatic message/receipt generation and computational guidance
review retain their independent positive warrants. Initial preference or instruction
labels do not settle actual content admission. See
[MEM-RTE-node-curation](memory.md#mem-rte-node-curation),
[RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review), and
[RT-RTE-application-publish](runtime.md#rt-rte-application-publish).

The summary is consolidation of retained action history, not demonstrated novel
knowledge. Guidance review's request for distinct durable lessons is not an
implemented duplicate merge or evidence of synthesis. Graph deletion supports
forgetting, while uninspected blob cleanup prevents a complete lifecycle inventory.
Retained tool history has learning force at the summarizer that produces the
later-invocation completion/retry summary; the summary has knowledge force at
those later consumers. Guidance proposals, by contrast, are transient staged
candidates, not established read-back of retained decision observations. The
review also receives stored guidance, but the records do not establish a separate
learning force for that input. The guidance route's architectural trace-learning
positive and its output's later instruction force do not supply that missing
input-authority warrant. None implies observed improved capacity. See
[MEM-OBJ-task-history](memory.md#mem-obj-task-history),
[MEM-RTE-history-summary](memory.md#mem-rte-history-summary),
[EPI-OBJ-candidate-entry](epistemic.md#epi-obj-candidate-entry),
[EPI-RTE-guidance-check](epistemic.md#epi-rte-guidance-check), and
[MEM-RTE-node-curation](memory.md#mem-rte-node-curation).

Saved controls can route, validate and enforce. Their effects do not come from the
instruction prose. Current expected text vetoes a conflicting replacement; saved
task grants and activation bindings govern covered operations. No universal effect
monitor is inferred. See [RT-RTE-saved-store](runtime.md#rt-rte-saved-store),
[RT-OBJ-tool-attempt](runtime.md#rt-obj-tool-attempt), and
[MEM-BAP-linked-instructions](memory.md#mem-bap-linked-instructions).

### Requested retrieval and automatic supply

Requested graph/history retrieval is pull. Automatic context reload, model relevance
selection, explicit-link materialization and next-inference image attachment are
push operations within their respective chains. Lexical search hints establish the
requested retrieval selector, not a separate inferred-lexical push. The model's
kept IDs represent semantic judgment; explicit task/Store identity matches instead
select associated retained parts without that relevance decision. See
[MEM-RTE-graph-selection](memory.md#mem-rte-graph-selection),
[MEM-RTE-context-reload](memory.md#mem-rte-context-reload), and
[EPI-RTE-panel-evidence](epistemic.md#epi-rte-panel-evidence).

### Trace qualification and unresolved origin

The optional observation-to-guidance write qualifies architecturally. Its review
interface does not establish the original trace's controlled source category.
Candidate narration cannot replace a missing original-input fact. The action-summary
route has a recorded tool-history input and a later completion/retry consumer.
Under the shared contract, replacement summaries retained for a later invocation
are memory even within one request; this positive is bounded to that horizon and
does not claim cross-session summary retrieval. See
[RT-RTE-guidance-review](runtime.md#rt-rte-guidance-review),
[EPI-RTE-guidance-check](epistemic.md#epi-rte-guidance-check), and
[MEM-RTE-history-summary](memory.md#mem-rte-history-summary).

Unknown initialization, arbitrary payload forms, generic-caller control and
uninspected maintenance/later-consumer alternatives remain in the axis inventories.
They cannot be dropped to turn a wired witness into complete coverage. No local or
system-wide trace-learning negative is asserted without a bounded absence record;
therefore trace_source is not made inapplicable by raw-log or evidence-only routes.

### Source-read log

No frozen-source file was read for this mapping. All classifications derive from
the supplied accepted records and their annotations. No records, quotations or
source evidence were added, and report verification was not reopened.
