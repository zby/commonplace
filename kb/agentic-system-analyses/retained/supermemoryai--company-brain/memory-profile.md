---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Company Brain memory comparison across hosted company/style knowledge, retained instructions, local access state and later continuation/research consumers at the frozen worker revision."
run-id: "AAS-2026-10-14-company-brain-30a9e8cfaeca-01"
source-identity: "https://github.com/supermemoryai/company-brain"
reviewed-boundary: "ef8a45ef3aed97b32599c7d8007edefab6d14e9a"
memory-comparison:
  version: 2
  scope: "Included: submitted/derived hosted company and agent-self content, entity cache, extraction settings, channel spool/batches and observer carry, local tags/node/generation/cursor state, mutable skills/workspace directions, investigation checkpoints and retained approval continuations, scheduled payloads, research draft/sent history and human read routes. Optional sandbox continuity and opaque provider parts remain included unresolved alternatives. Excluded: static shipped instructions as memory objects, ordinary untransformed live turn accumulation, inference weights without an evidenced accumulated-memory update, external connected-application state, and transient reception feedback not persisted by the inspected administrative routes."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Submitted documents, derived text rows, entity cache and agent-self notes"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-document"
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-obj-agent-style"
                - "runtime.md#rt-rte-entity-web"
              note: "Local adapters submit and later request these hosted objects."
          records:
            - "memory.md#mem-obj-brain-document"
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-obj-agent-style"
            - "runtime.md#rt-rte-entity-web"
          note: "The operative application-facing objects are hosted service objects; this does not identify the provider database or embedding store."
        - scope: "Hosted extraction settings"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-config"
                - "memory.md#mem-rte-profile-provision"
              note: "Provisioning updates retained remote container-tag settings."
          records:
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
          note: "Remote container settings are the retained configuration surface, not the shipped policy file."
        - scope: "Channel spool/cluster batch, observer carry/cursor, tags/node mappings/generation, skills, investigation and approval snapshots, research drafts/sent history"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-obj-memory-index"
                - "runtime.md#rt-obj-brain-skill"
                - "memory.md#mem-obj-thread-investigation"
                - "runtime.md#rt-rte-approval-resume"
                - "epistemic.md#epi-obj-research-draft"
              note: "These records identify SQL-backed tables and serialized rows."
          records:
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-obj-memory-index"
            - "runtime.md#rt-obj-brain-skill"
            - "runtime.md#rt-obj-workspace-prompt"
            - "memory.md#mem-obj-thread-investigation"
            - "runtime.md#rt-rte-approval-resume"
            - "epistemic.md#epi-obj-research-draft"
          note: "DO SQL and organization Durable Object persistence establish relational retained state. JSON encodings are not separate substrates; no SQLite implementation is asserted from SQL alone."
        - scope: "Workspace-prompt persistence below the organization Durable Object API"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-workspace-prompt"
            - "runtime.md#rt-rte-instruction-admission"
          note: "The record identifies a Durable Object persistence boundary but not its physical store. The prompt is not included in the SQL finding above solely because other DO objects use SQL."
        - scope: "Scheduled payload storage"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-scheduled-task"
          note: "agent.schedule retains the payload, but the accepted record does not identify its underlying substrate."
        - scope: "Hosted embeddings, extraction/versioning internals and internal access structures"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-clm-service-curation"
          note: "The service is opaque. Neither vector, graph nor model-weights follows from an embedding request or graph display."
        - scope: "Optional reused sandbox workspace"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Scoped reuse is included as continuity; provider filesystem lifetime and persistence are not established. No files substrate is inferred for durable memory."
      records:
        - "memory.md#mem-obj-brain-document"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-obj-agent-style"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-obj-channel-batch"
        - "memory.md#mem-obj-memory-index"
        - "runtime.md#rt-obj-brain-skill"
        - "runtime.md#rt-obj-workspace-prompt"
        - "memory.md#mem-obj-thread-investigation"
        - "runtime.md#rt-rte-approval-resume"
        - "epistemic.md#epi-obj-research-draft"
        - "runtime.md#rt-rte-instruction-admission"
        - "runtime.md#rt-rte-scheduled-task"
        - "memory.md#mem-clm-service-curation"
        - "runtime.md#rt-rte-sandbox-work"
      note: "The inventory covers hosted documents, derived rows, extraction settings, local indexes, observer state, instructions, continuation state, schedules and research history. Their named stores are classified; opaque service representations and optional sandbox lifetime remain unresolved."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Document/derived-memory/style text and source references interpreted by later models or humans"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-document"
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-bap-retained-context"
                - "memory.md#mem-rte-human-readers"
              note: "Selected text supplies later context and human displays."
          records:
            - "memory.md#mem-obj-brain-document"
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-bap-retained-context"
            - "memory.md#mem-rte-human-readers"
          note: "The readable retained content is natural language, distinct from its IDs and liveness fields."
        - scope: "Tag/node descriptions at model navigation consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-rte-requested-recall"
              note: "Tag labels/descriptions and outlines enter model-interpreted navigation context."
          records:
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-rte-requested-recall"
          note: "Readable labels/descriptions inform model navigation independently of symbolic relation keys."
        - scope: "Cached canonical entity, aliases and domain fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-entity-web"
              note: "Canonical/alias/domain fields are parsed and cached for subsequent entity resolution."
          records:
            - "runtime.md#rt-rte-entity-web"
          note: "Parsed localized JSON fields identify the cached entity and matching lookup reference; this does not classify uninspected provider representations."
        - scope: "Raw channel text, curated clusters and carried observer note tail"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
              note: "Distillation interprets messages; subsequent observation interprets prior notes."
          records:
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
          note: "Raw and derived text share an encoding, not a provenance or downstream consumer."
        - scope: "Standing skill/workspace bodies and scheduled task instruction"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-brain-skill"
                - "runtime.md#rt-obj-workspace-prompt"
                - "runtime.md#rt-rte-scheduled-task"
              note: "Stored playbooks, workspace directions and later task instructions reach model contexts."
          records:
            - "runtime.md#rt-obj-brain-skill"
            - "runtime.md#rt-obj-workspace-prompt"
            - "runtime.md#rt-rte-scheduled-task"
          note: "Instructions are model-interpreted text, not executable access policy."
        - scope: "Checkpoint answer/goal/tool excerpts, compacted conversation and research body/history snippets"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-thread-investigation"
                - "runtime.md#rt-rte-context-boundary"
                - "epistemic.md#epi-obj-research-draft"
                - "memory.md#mem-bap-retained-context"
              note: "Later continuation/planning/review can interpret the retained text."
          records:
            - "memory.md#mem-obj-thread-investigation"
            - "runtime.md#rt-rte-context-boundary"
            - "epistemic.md#epi-obj-research-draft"
            - "memory.md#mem-bap-retained-context"
          note: "Literal excerpts and summaries are by-value text; digests cannot recover evicted originals."
        - scope: "IDs, liveness/bucket/tag fields, index relations, generation/cursors, checkpoint status/digests, instruction visibility, schedule timing/scope and research status/flags"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-obj-thread-investigation"
                - "runtime.md#rt-obj-brain-skill"
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-scheduled-task"
                - "epistemic.md#epi-obj-research-draft"
              note: "Host code matches IDs, filters flags, follows relations and evaluates status/time values."
          records:
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-obj-thread-investigation"
            - "runtime.md#rt-obj-brain-skill"
            - "runtime.md#rt-rte-context-boundary"
            - "runtime.md#rt-rte-scheduled-task"
            - "epistemic.md#epi-obj-research-draft"
          note: "These localized fields have code-defined selection, eligibility or navigation effects. Text labels are separately interpreted."
        - scope: "Extraction-context text at its remote extractor and bucket keys at local readers"
          assessment: "partial"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-profile-config"
                - "memory.md#mem-rte-profile-provision"
              note: "entityContext supplies intended extraction instructions."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-config"
                - "memory.md#mem-rte-style-recall"
              note: "Recognized bucket keys determine which returned notes enter local style facets."
          records:
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
          note: "Local configuration assembly is inspected; remote interpretation is requested, not inspected."
        - scope: "Hosted embeddings and other opaque consumed provider representations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-derived-memory"
          note: "No retained numerical representation is inspectable. parametric is not established from a declaration of embedding alone."
        - scope: "Optional sandbox contents"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Command/file capability does not establish the form of durable retained workspace memory."
      records:
        - "memory.md#mem-obj-brain-document"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-obj-agent-style"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-rte-human-readers"
        - "memory.md#mem-obj-memory-index"
        - "memory.md#mem-rte-requested-recall"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-obj-channel-batch"
        - "runtime.md#rt-obj-brain-skill"
        - "runtime.md#rt-obj-workspace-prompt"
        - "runtime.md#rt-rte-scheduled-task"
        - "memory.md#mem-obj-thread-investigation"
        - "runtime.md#rt-rte-context-boundary"
        - "epistemic.md#epi-obj-research-draft"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Text and symbolic retained parts are separated at their consumers. Hosted numerical representations and the detailed sandbox contents remain unresolved; inference weights are excluded because no accumulated weight memory is established."
    lineage:
      assessment: "partial"
      units:
        - scope: "Raw public-channel spool"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-rte-channel-curation"
              note: "External channel messages enter the SQL spool."
          records:
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-rte-channel-curation"
          note: "Slack activity is retained before distillation; it is not an authored company-fact ledger."
        - scope: "Interactive capture and channel/style derived notes"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-handoff"
                - "memory.md#mem-obj-brain-document"
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
              note: "Model/software routes turn conversation/tool observations into retained documents or style notes."
          records:
            - "runtime.md#rt-rte-knowledge-handoff"
            - "memory.md#mem-obj-brain-document"
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-agent-style"
          note: "The inspected producer paths extract selected durable content from conversational activity. This classifies the application producer, not every hosted derived row."
        - scope: "Research-summary documents and entity identification cache"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-brain-document"
                - "runtime.md#rt-rte-entity-web"
              note: "Web research content enters the acquisition paths."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-entity-web"
              note: "Provider result is parsed into canonical entity/alias/domain cache content, not a retained identification rationale."
          records:
            - "memory.md#mem-obj-brain-document"
            - "runtime.md#rt-rte-entity-web"
          note: "External web input and model-generated summaries/identifications are supported; complete summarization and evidence provenance remain unresolved."
        - scope: "Hosted derived memories and embeddings"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-clm-service-curation"
              note: "Extraction from submitted documents is the declared service derivation path."
          records:
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-clm-service-curation"
          note: "Document IDs attribute derivation but cannot reconstruct the extractor or embedding provenance."
        - scope: "Registered tag/node relations and profile configuration assembled from fixed policy plus organization/person/channel fields"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-rte-node-splitting"
                - "memory.md#mem-obj-profile-config"
                - "memory.md#mem-rte-profile-provision"
              note: "Accepted-write registration, partitioning and context builders construct retained metadata/configuration."
          records:
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-rte-node-splitting"
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
          note: "These parts are software/model-compiled access or extraction structures, not inferred facts simply because they accompany facts."
        - scope: "Skill and workspace instruction content supplied or approved by an operator, plus model-mediated prompt replacement"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-admission"
                - "memory.md#mem-rte-config-edit"
              note: "Explicit editing/save paths author retained standing guidance."
          records:
            - "runtime.md#rt-rte-instruction-admission"
            - "memory.md#mem-rte-config-edit"
          note: "Authored lineage includes both human-supplied text and model-authored approved/replaced directions. Admission is classified separately."
        - scope: "Investigation checkpoint and approval/continuation compacted messages"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-thread-investigation"
                - "memory.md#mem-rte-investigation-recall"
                - "runtime.md#rt-rte-context-boundary"
              note: "Deterministic construction retains selected conversational/tool experience."
          records:
            - "memory.md#mem-obj-thread-investigation"
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-rte-context-boundary"
          note: "Selected answers, tool excerpts and message heads derive from prior work rather than an external static playbook."
        - scope: "Research draft body and review trail"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "epistemic.md#epi-obj-research-draft"
                - "epistemic.md#epi-rte-draft-check"
              note: "Draft turn returns transformed reply and selected tool trail for storage."
            - value: "authored"
              basis: "afforded"
              records:
                - "workflow.md#wf-rte-draft-delivery"
              note: "Reviewer editing can replace pending body text before publication."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "epistemic.md#epi-obj-research-draft"
            - "epistemic.md#epi-rte-draft-check"
          note: "The retained product crosses an isolated work-turn boundary; later human edits add another derivation path."
        - scope: "Initial hosted settings/content, initial local instructions and schedule instruction provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-profile-config"
            - "runtime.md#rt-rte-instruction-admission"
            - "runtime.md#rt-rte-scheduled-task"
          note: "Known subsequent writers do not establish initial provenance; the scheduler record supplies a model-selected payload, not its complete derivation."
        - scope: "Optional sandbox accumulated contents"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Workspace reuse does not inventory retained files or their derivation paths."
      records:
        - "memory.md#mem-obj-channel-batch"
        - "memory.md#mem-rte-channel-curation"
        - "runtime.md#rt-rte-knowledge-handoff"
        - "memory.md#mem-obj-brain-document"
        - "memory.md#mem-obj-agent-style"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-clm-service-curation"
        - "memory.md#mem-obj-memory-index"
        - "memory.md#mem-rte-node-splitting"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "runtime.md#rt-rte-instruction-admission"
        - "memory.md#mem-rte-config-edit"
        - "memory.md#mem-obj-thread-investigation"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-research-draft"
        - "epistemic.md#epi-obj-research-draft"
        - "epistemic.md#epi-rte-draft-check"
        - "runtime.md#rt-rte-scheduled-task"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Known document, observer, continuation and instruction paths coexist with unresolved initialization, hosted derivation/embedding provenance, scheduler payload derivation and sandbox contents."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Selected document/derived text and research history at later answering/planning models and human readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-retained-context"
                - "memory.md#mem-rte-requested-recall"
                - "memory.md#mem-rte-ambient-recall"
                - "memory.md#mem-rte-human-readers"
              note: "Model/human consumers receive selected text as evidence or reference."
          records:
            - "memory.md#mem-bap-retained-context"
            - "memory.md#mem-rte-requested-recall"
            - "memory.md#mem-rte-ambient-recall"
            - "memory.md#mem-rte-human-readers"
          note: "Facts and past outputs supply reference/context; history also guides avoidance of repeated topics, without a factual acceptance criterion."
        - scope: "Cached entity identification at later reference-resolution consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-entity-web"
              note: "A later matching reference can receive the current-generation cached identification."
          records:
            - "runtime.md#rt-rte-entity-web"
          note: "Canonical identification supplies reusable reference knowledge; parse validity is not truth validation."
        - scope: "Style facets, workspace prompt, loaded skill body and scheduled instruction at later model invocations"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-rte-style-recall"
                - "runtime.md#rt-bap-standing-instructions"
                - "runtime.md#rt-rte-scheduled-task"
              note: "Stored directions enter later model contexts."
          records:
            - "memory.md#mem-rte-style-recall"
            - "runtime.md#rt-bap-standing-instructions"
            - "runtime.md#rt-rte-scheduled-task"
          note: "These standing directions request voice, workflow or task behavior; they are not executable enforcement."
        - scope: "Retained channel spool and prior observer carry at durable-note update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
                - "runtime.md#rt-rte-knowledge-handoff"
              note: "Distillation/observation uses retained messages or prior notes to produce later-consumed memory."
          records:
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-agent-style"
            - "runtime.md#rt-rte-knowledge-handoff"
          note: "Recorded activity/experience feeds durable behavior-shaping content. This update-consumer force is separate from knowledge/instruction at the output consumer."
        - scope: "Tag key/label/description/use counts and returned similarity inputs at recall prioritizers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-rte-requested-recall"
                - "epistemic.md#epi-rte-brain-selection"
              note: "Retained tags/counts and returned memory scores influence relative selection priority."
          records:
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-rte-requested-recall"
            - "epistemic.md#epi-rte-brain-selection"
          note: "Lexical matches and usage counts rank retained metadata; local sorting consumes service scores without establishing how the service computed them."
        - scope: "Node mappings, observation cursors, identity scope, skill visibility and stored schedule timing/destination at host selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-rte-investigation-recall"
                - "runtime.md#rt-obj-brain-skill"
                - "runtime.md#rt-rte-scheduled-task"
              note: "Host rules follow retained identity/scope/mapping/cursor/time state."
          records:
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-obj-brain-skill"
            - "runtime.md#rt-rte-scheduled-task"
          note: "These retained fields select input windows, accessible parts, operations or destinations; merely unconsumed metadata has no classified force."
        - scope: "Stored reset epoch, memory liveness flags, skill status/scope and draft status at admission/read gates"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-rte-memory-withdrawal"
                - "runtime.md#rt-obj-brain-skill"
                - "workflow.md#wf-rte-draft-delivery"
              note: "Current-generation/liveness/status criteria decide whether writes, reads or sends are admissible."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-index"
                - "memory.md#mem-obj-derived-memory"
                - "memory.md#mem-rte-memory-withdrawal"
                - "runtime.md#rt-obj-brain-skill"
                - "workflow.md#wf-rte-draft-delivery"
              note: "Local predicates block stale writes, dead-memory delivery, invisible skills and nonpending sends."
          records:
            - "memory.md#mem-obj-memory-index"
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-rte-memory-withdrawal"
            - "runtime.md#rt-obj-brain-skill"
            - "workflow.md#wf-rte-draft-delivery"
          note: "Retained criteria determine admissibility and implement local vetoes. Service-wide authorization and deletion do not follow."
        - scope: "Investigation checkpoint and approval-resume retained excerpts at restored turn state/model"
          assessment: "partial"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-approval-resume"
                - "memory.md#mem-rte-investigation-recall"
              note: "Bounded retained prior work supplies continuation context/state."
          records:
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-rte-context-boundary"
            - "runtime.md#rt-rte-approval-resume"
          note: "Resume consumption is inspected; investigation state is restored but its full final rendering remains uninspected."
        - scope: "Extraction context at hosted extractor"
          assessment: "partial"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-profile-config"
                - "memory.md#mem-rte-profile-provision"
              note: "Retained context is intended as standing extraction guidance."
          records:
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
          note: "Provisioning is wired, but actual remote interpretation, criteria and transformations are opaque."
        - scope: "Research draft evidence/length flags at reviewer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-draft-check"
                - "epistemic.md#epi-obj-research-draft"
              note: "Stored flags inform review without forcing refusal."
          records:
            - "epistemic.md#epi-rte-draft-check"
            - "epistemic.md#epi-obj-research-draft"
          note: "Advisory diagnostic text is not a machine-enforced acceptance criterion."
        - scope: "Optional reused sandbox memory and other opaque provider-state consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
            - "memory.md#mem-obj-derived-memory"
          note: "No accepted record inventories authority for internal embeddings or accumulated sandbox files."
      records:
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-rte-requested-recall"
        - "memory.md#mem-rte-ambient-recall"
        - "memory.md#mem-rte-human-readers"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-rte-style-recall"
        - "runtime.md#rt-bap-standing-instructions"
        - "runtime.md#rt-rte-scheduled-task"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-agent-style"
        - "runtime.md#rt-rte-knowledge-handoff"
        - "memory.md#mem-obj-memory-index"
        - "epistemic.md#epi-rte-brain-selection"
        - "memory.md#mem-obj-channel-batch"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-obj-brain-skill"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-rte-memory-withdrawal"
        - "workflow.md#wf-rte-draft-delivery"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-approval-resume"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "epistemic.md#epi-rte-draft-check"
        - "epistemic.md#epi-obj-research-draft"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Authority is assigned to a retained part at an actual consumer. Knowledge, instructions, learning inputs, selectors and controls differ. Remote extractor effects, some checkpoint rendering and sandbox consumption remain unresolved; none establishes compliance or benefit."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Interactive/resumed knowledge capture, channel clusters and style notes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-handoff"
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
              note: "Completed-turn/observer writes have no per-document human decision."
          records:
            - "runtime.md#rt-rte-knowledge-handoff"
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-agent-style"
          note: "Model/software admits each retained proposal subject to software guards; humans do not approve each one."
        - scope: "Profile provisioning, tag/node registration and partitioning, entity cache, checkpoint/compaction and scheduled payload admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-profile-provision"
                - "memory.md#mem-rte-node-splitting"
                - "runtime.md#rt-rte-entity-web"
                - "memory.md#mem-rte-investigation-recall"
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-scheduled-task"
              note: "Subsequent software/model retention lacks a per-output operator approval gate."
          records:
            - "memory.md#mem-rte-profile-provision"
            - "memory.md#mem-rte-node-splitting"
            - "runtime.md#rt-rte-entity-web"
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-rte-context-boundary"
            - "runtime.md#rt-rte-scheduled-task"
          note: "These admitted outputs are selected by host/model code, even when a user starts the workflow or supplies input fields."
        - scope: "Requester-approved skill creation and human-supplied HTTP prompt/settings edits"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-admission"
              note: "Requester scope/content approval or authorized editor-supplied replacement admits the retained instruction."
          records:
            - "runtime.md#rt-rte-instruction-admission"
          note: "The decision approves or supplies the retained content itself, unlike merely initiating a turn."
        - scope: "Model-mediated admin configuration replacement"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-config-edit"
              note: "Model-supplied prompt/settings are admitted by schema/admin checks without a per-text approval card."
          records:
            - "memory.md#mem-rte-config-edit"
          note: "Execution role validation does not approve the proposed text separately."
        - scope: "Research draft insertion"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "epistemic.md#epi-rte-draft-check"
              note: "Nonempty completed products pass reset/ownership guards into review storage."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "epistemic.md#epi-rte-draft-check"
          note: "Starting the round is not approving each generated draft."
        - scope: "Reviewer pending-body editing, dismissal and explicit send decision"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "workflow.md#wf-rte-draft-delivery"
              note: "Reviewer can edit/dismiss/withhold publication and chooses the retained body for sending."
          records:
            - "workflow.md#wf-rte-draft-delivery"
          note: "Human editing/replacement and publication selection are separately available; actual reviewer behavior is unobserved."
        - scope: "Approved forget apply"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
              note: "needsApproval gates non-dry-run forgetting."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Preview is automatic discovery; the apply decision is requester-gated and affects retained reliance."
        - scope: "Stale-generation/aspect cleanup"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Stale retained documents are selected for deletion without a per-document operator decision."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Software cleanup is distinct from human-gated forget and externally called reset."
        - scope: "Debug-turn capture, exposed reset caller, initial hosted/local content and provider-internal admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-debug-capture"
            - "memory.md#mem-rte-memory-withdrawal"
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-obj-derived-memory"
          note: "Generic debug principal does not establish human content control; reset caller and initial content control are not established; hosted internal admission is opaque."
        - scope: "Optional sandbox durable-content admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Capability execution and reuse do not establish per-content admission control for a durable memory inventory."
      records:
        - "runtime.md#rt-rte-knowledge-handoff"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-agent-style"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-rte-node-splitting"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-scheduled-task"
        - "runtime.md#rt-rte-instruction-admission"
        - "memory.md#mem-rte-config-edit"
        - "runtime.md#rt-rte-research-draft"
        - "epistemic.md#epi-rte-draft-check"
        - "workflow.md#wf-rte-draft-delivery"
        - "memory.md#mem-rte-memory-withdrawal"
        - "memory.md#mem-rte-debug-capture"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-obj-derived-memory"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Known automatic and manual admissions coexist. Human authorship of source messages, starting research or holding an admin role is not per-content approval. Initial settings, external reset control and debug caller control remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Channel distillation, bounded style carry, checkpoint construction and message compaction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-rte-investigation-recall"
                - "runtime.md#rt-rte-context-boundary"
              note: "Retained messages/notes/experience become bounded clusters, carry, checkpoints or conversation excerpts."
          records:
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-rte-context-boundary"
          note: "These select/compress existing activity or prior text for later context. Possible semantic defects do not themselves establish creation of a new claim."
        - scope: "Persisted checkpoint trajectory selection"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-thread-investigation"
                - "memory.md#mem-rte-investigation-recall"
              note: "Checkpoint construction retains up to six deduplicated recent entries."
          records:
            - "memory.md#mem-obj-thread-investigation"
            - "memory.md#mem-rte-investigation-recall"
          note: "Deduplication applies to retained recent trajectory entries, not merely a transient search result list."
        - scope: "Instruction replacement, active skill update and reviewed pending draft body replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-admission"
                - "memory.md#mem-rte-config-edit"
              note: "Stored skills and workspace prompt can be updated/replaced."
            - value: "evolve"
              basis: "afforded"
              records:
                - "workflow.md#wf-rte-draft-delivery"
              note: "Reviewer can replace a pending draft body without regenerating evidence."
          records:
            - "runtime.md#rt-rte-instruction-admission"
            - "memory.md#mem-rte-config-edit"
            - "workflow.md#wf-rte-draft-delivery"
          note: "These revise existing retained content; they do not establish automatic evidence-based factual correction."
        - scope: "Forgotten/liveness filtering and local generation invalidation"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
                - "memory.md#mem-obj-derived-memory"
              note: "Forgotten/nonlatest/expired rows are excluded; generation change blocks old producers and clears local observation/index state."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
            - "memory.md#mem-obj-derived-memory"
          note: "Current reliance is withdrawn locally while surviving source documents or other history may remain. Complete service erasure is not established."
        - scope: "Investigation idle expiry and bounded checkpoint retention"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-investigation-recall"
                - "memory.md#mem-obj-thread-investigation"
              note: "Six-hour idle TTL deletes/omits expired retained investigation state."
          records:
            - "memory.md#mem-rte-investigation-recall"
            - "memory.md#mem-obj-thread-investigation"
          note: "Expiry removes an old checkpoint, and bounded retention forgets older experience; no improved recall is inferred."
        - scope: "Hosted extraction, duplicate merging, supersession, inferred patterns and transient horizons"
          assessment: "partial"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-clm-service-curation"
              note: "Extraction policy requests updating existing memory when new facts supersede it."
            - value: "dedup"
              basis: "claimed"
              records:
                - "memory.md#mem-clm-service-curation"
              note: "Downstream extractor is assigned duplicate merging rather than local proof of merging."
            - value: "decay"
              basis: "claimed"
              records:
                - "memory.md#mem-clm-service-curation"
              note: "Transient forget horizons are requested; local expiry filtering does not prove how the horizons were assigned."
            - value: "synthesize"
              basis: "claimed"
              records:
                - "memory.md#mem-clm-service-curation"
              note: "Shared policy permits inferred repeated patterns beyond directly stated facts; no concrete novel output is supplied."
          records:
            - "memory.md#mem-clm-service-curation"
            - "memory.md#mem-obj-derived-memory"
          note: "These are requested provider transformations, not inspected implementations. Exact content semantics and provider adherence remain unknown."
        - scope: "Topic split, tag registration and extraction-config refresh as controlled curation operations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-node-splitting"
            - "memory.md#mem-rte-profile-provision"
            - "memory.md#mem-obj-memory-index"
          note: "The established changes concern organization/configuration, not consolidation, promotion or synthesis of retained claims. Same-text metadata patches do not establish evolve of factual text."
        - scope: "Complete research-summary transformation and optional sandbox maintenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-brain-document"
            - "runtime.md#rt-rte-sandbox-work"
          note: "The full summarization pipeline and durable sandbox maintenance are not inspected; neither operation absence nor semantic synthesis is established."
      records:
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-agent-style"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-rte-context-boundary"
        - "memory.md#mem-obj-thread-investigation"
        - "runtime.md#rt-rte-instruction-admission"
        - "memory.md#mem-rte-config-edit"
        - "workflow.md#wf-rte-draft-delivery"
        - "memory.md#mem-rte-memory-withdrawal"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-clm-service-curation"
        - "memory.md#mem-rte-node-splitting"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-obj-memory-index"
        - "memory.md#mem-obj-brain-document"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Known local transformations and claimed remote operations remain distinct findings. Topic splitting alone is not one of these controlled transformations of claim content. Hosted semantics, full acquisition summaries and sandbox maintenance remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Semantic/tag/tree memory tools, skill load and human recent/export/graph requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-requested-recall"
                - "runtime.md#rt-rte-instruction-admission"
                - "memory.md#mem-rte-human-readers"
              note: "Consumer chooses query/tag/path/skill/page/export and receives selected retained material."
          records:
            - "memory.md#mem-rte-requested-recall"
            - "runtime.md#rt-rte-instruction-admission"
            - "memory.md#mem-rte-human-readers"
          note: "Returning requested material is pull, not an additional push merely because code delivers it."
        - scope: "Ambient and style context, workspace directions and visible skill index"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ambient-recall"
                - "memory.md#mem-rte-style-recall"
                - "runtime.md#rt-bap-standing-instructions"
              note: "Invocation-triggered selectors supply bounded profiles, standing text and visible metadata."
          records:
            - "memory.md#mem-rte-ambient-recall"
            - "memory.md#mem-rte-style-recall"
            - "runtime.md#rt-bap-standing-instructions"
          note: "Compute independently supplies these retained parts before the foreground model requests them."
        - scope: "Later observation supplies persisted channel batch/spool or prior style carry to update consumers"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
              note: "Owned callback selects a pending batch or prior carried note for distillation/observation."
          records:
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-agent-style"
          note: "Callback supply is automatic; the foreground answering model does not request these retained inputs."
        - scope: "Principal/thread checkpoint restoration and approval continuation"
          assessment: "partial"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-investigation-recall"
              note: "Later nonephemeral compute automatically restores the matching checkpoint."
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-approval-resume"
                - "runtime.md#rt-rte-context-boundary"
              note: "Requester approval continuation reloads the specified bounded retained conversation."
          records:
            - "memory.md#mem-rte-investigation-recall"
            - "runtime.md#rt-rte-approval-resume"
            - "runtime.md#rt-rte-context-boundary"
          note: "Checkpoint restoration is independent context supply; approval interaction requests a specified continuation. Full investigation rendering remains unresolved."
        - scope: "Scheduled instruction callback"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scheduled-task"
              note: "Alarm callback supplies retained task instructions to a fresh compute turn."
          records:
            - "runtime.md#rt-rte-scheduled-task"
          note: "Stored timing independently starts later execution; any memory tool calls within that execution are separate pull routes."
        - scope: "Research planning history and explicit stored-draft publication"
          assessment: "partial"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "memory.md#mem-bap-retained-context"
              note: "Planning receives prior sent/pending body snippets without a model request for each."
            - value: "pull"
              basis: "wired"
              records:
                - "workflow.md#wf-rte-draft-delivery"
              note: "Reviewer-selected draft ID requests publication of its stored body."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "memory.md#mem-bap-retained-context"
            - "workflow.md#wf-rte-draft-delivery"
          note: "Stored bodies automatically guide planning; explicit send requests delivery of a selected body. Full history storage/selection horizon is not completely inspected."
        - scope: "Entity cache lookup"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-entity-web"
              note: "Known current-generation entity is returned for a supplied reference."
          records:
            - "runtime.md#rt-rte-entity-web"
          note: "Calling entity resolution requests the matching retained identification; the web fallback is acquisition rather than another memory read direction."
        - scope: "Remote extractor use of stored context/configuration and internal memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
            - "memory.md#mem-obj-derived-memory"
          note: "Settings are submitted, but remote later selection/delivery operations are not traced in accepted records."
        - scope: "Optional reused sandbox durable state"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Provider lifetime and subsequent workspace-content consumption remain uninspected."
      records:
        - "memory.md#mem-rte-requested-recall"
        - "runtime.md#rt-rte-instruction-admission"
        - "memory.md#mem-rte-human-readers"
        - "memory.md#mem-rte-ambient-recall"
        - "memory.md#mem-rte-style-recall"
        - "runtime.md#rt-bap-standing-instructions"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-agent-style"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-rte-approval-resume"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-scheduled-task"
        - "runtime.md#rt-rte-research-draft"
        - "memory.md#mem-bap-retained-context"
        - "workflow.md#wf-rte-draft-delivery"
        - "runtime.md#rt-rte-entity-web"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-obj-derived-memory"
        - "runtime.md#rt-rte-sandbox-work"
      note: "The inventory includes requested model/human returns and independently supplied context. Both pull and push are wired; remote extraction consumption, complete checkpoint rendering, history selection and sandbox persistence retain local limits."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Ambient profile supply to current turn"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ambient-recall"
              note: "Actual person/channel tag matches select delivered retained rows, not merely catalog IDs."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ambient-recall"
                - "memory.md#mem-obj-derived-memory"
              note: "Candidate caps, recent/liveness/bucket eligibility, tagged baseline and text shortening limit untargeted supply."
          records:
            - "memory.md#mem-rte-ambient-recall"
            - "memory.md#mem-obj-derived-memory"
          note: "Trigger is compute invocation. Selector uses readable scopes, asker/mentioned-person/channel identifiers and bucket/liveness/tag eligibility; retained outputs are short derived-memory text plus a topic outline."
        - scope: "Style facet supply"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-style-recall"
              note: "Matching asker tags select person-specific retained notes."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-style-recall"
              note: "Non-person availability, recognized bucket eligibility and recent candidate cap supply a bounded baseline."
          records:
            - "memory.md#mem-rte-style-recall"
          note: "Trigger is invocation; selector inputs are asker tag, agent-self container, recognized bucket keys and live recent 80 rows; selected parts are grouped style-note texts."
        - scope: "Standing workspace text and visible skill index"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-standing-instructions"
                - "runtime.md#rt-rte-instruction-admission"
              note: "Available workspace directions and visible active skill metadata are supplied as standing context."
          records:
            - "runtime.md#rt-bap-standing-instructions"
            - "runtime.md#rt-rte-instruction-admission"
            - "runtime.md#rt-obj-brain-skill"
          note: "Trigger is later context assembly. Workspace availability and active/visible scope select standing text/index metadata. Requested body load is not a push signal."
        - scope: "Checkpoint restoration"
          assessment: "partial"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-investigation-recall"
              note: "Thread/principal identity matches select the restored checkpoint."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-investigation-recall"
              note: "TTL, schema and nonephemeral eligibility can suppress otherwise matching context."
          records:
            - "memory.md#mem-rte-investigation-recall"
          note: "Trigger is later compute; exact thread and principal tuple match select a retained checkpoint, with six-hour TTL/schema checks. Full downstream rendering remains uninspected."
        - scope: "Channel batch/spool and prior observer carry supply"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
              note: "Owned channel/thread observer state selects its corresponding retained batch/carry."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-agent-style"
              note: "Oldest pending window, character/message caps and bounded carried tail limit selected input."
          records:
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
          note: "Trigger is owned observation callback. Scope/cursor and oldest bounded pending batch select retained messages/clusters; the style observer receives its bounded prior-note tail."
        - scope: "Scheduled callback supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scheduled-task"
              note: "Timing and availability gates supply the due retained instruction."
          records:
            - "runtime.md#rt-rte-scheduled-task"
          note: "Trigger is stored time/cron. Callback receives its retained payload; workspace/org/entitlement gates bound execution. No topical semantic selector is established."
        - scope: "Research planner history supply"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "memory.md#mem-bap-retained-context"
              note: "Available bounded prior-body lists are supplied to planning rather than selected by an embedding query."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "memory.md#mem-bap-retained-context"
          note: "Trigger is a new round; selector supplies prior sent/pending bodies normalized to 240-character heads. Complete history-selection criteria/horizon remain unresolved."
        - scope: "Requested semantic/tag/tree/skill/human/entity/approval/draft returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-requested-recall"
            - "memory.md#mem-rte-human-readers"
            - "runtime.md#rt-rte-instruction-admission"
            - "runtime.md#rt-rte-entity-web"
            - "runtime.md#rt-rte-approval-resume"
            - "workflow.md#wf-rte-draft-delivery"
          note: "These operations fulfill an explicit consumer request. Their lexical/semantic/identifier query predicates are not push-signal findings."
        - scope: "Remote bucket assignment, embedding-based alternatives and extraction-context consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-derived-memory"
            - "memory.md#mem-obj-profile-config"
            - "memory.md#mem-rte-profile-provision"
          note: "Local matching of returned keys is known; opaque production/selection of provider payloads is not thereby classified as inferred-embedding or inferred-judgment."
        - scope: "Optional sandbox state supply"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
          note: "Reuse lacks an inspected durable-content selector."
      records:
        - "memory.md#mem-rte-ambient-recall"
        - "memory.md#mem-obj-derived-memory"
        - "memory.md#mem-rte-style-recall"
        - "runtime.md#rt-bap-standing-instructions"
        - "runtime.md#rt-rte-instruction-admission"
        - "runtime.md#rt-obj-brain-skill"
        - "memory.md#mem-rte-investigation-recall"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-channel-batch"
        - "memory.md#mem-obj-agent-style"
        - "runtime.md#rt-rte-scheduled-task"
        - "runtime.md#rt-rte-research-draft"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-rte-requested-recall"
        - "memory.md#mem-rte-human-readers"
        - "runtime.md#rt-rte-entity-web"
        - "runtime.md#rt-rte-approval-resume"
        - "workflow.md#wf-rte-draft-delivery"
        - "memory.md#mem-obj-profile-config"
        - "memory.md#mem-rte-profile-provision"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Signals classify automatic supply, not requested retrieval queries. Identifier targeting and coarse eligibility/budgets coexist; provider bucket/embedding decisions and complete history/continuation/sandbox alternatives remain unresolved."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Interactive/resumed memory capture and channel distillation"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-handoff"
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-brain-document"
                - "memory.md#mem-bap-retained-context"
              note: "Trace-fed documents/clusters become durable later-consumed behavior-shaping knowledge."
          records:
            - "runtime.md#rt-rte-knowledge-handoff"
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-brain-document"
            - "memory.md#mem-bap-retained-context"
          note: "Conversation/tool activity feeds automatic durable text admission and later answering/planning context. Humans authoring inputs or requesting work do not make admission manual."
        - scope: "Public-thread style observation and carried notes"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-style"
                - "memory.md#mem-rte-style-recall"
                - "epistemic.md#epi-rte-style-generation"
                - "epistemic.md#epi-rte-style-admission"
              note: "Stored generalized notes and derived style facets shape later context, without weight updates or observed benefit."
          records:
            - "memory.md#mem-obj-agent-style"
            - "memory.md#mem-rte-style-recall"
            - "epistemic.md#epi-rte-style-generation"
            - "epistemic.md#epi-rte-style-admission"
          note: "Human interaction evidence and carried notes feed automatic retained guidance delivered to later turns."
        - scope: "Approval conversation compaction"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-approval-resume"
              note: "Bounded by-value continuation context is automatically trace-produced and later consumed."
          records:
            - "runtime.md#rt-rte-context-boundary"
            - "runtime.md#rt-rte-approval-resume"
          note: "Automatic reduction of conversation/tool traces is retained in resume storage and supplied to a later invocation; deterministic reshaping still qualifies."
        - scope: "Investigation checkpoint"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-investigation-recall"
                - "memory.md#mem-obj-thread-investigation"
              note: "Prior answer/tool experience becomes a durable checkpoint for later matching decision state."
          records:
            - "memory.md#mem-rte-investigation-recall"
            - "memory.md#mem-obj-thread-investigation"
          note: "Automatic trace-fed save and later state restoration are wired. Full final rendering remains uninspected, so coverage is partial rather than a claim of every excerpt influencing the model."
        - scope: "Research draft/history production"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "epistemic.md#epi-rte-draft-check"
                - "memory.md#mem-bap-retained-context"
              note: "Trace-derived retained body/history guides subsequent drafting and novelty avoidance."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "epistemic.md#epi-rte-draft-check"
            - "memory.md#mem-bap-retained-context"
          note: "Automatic retention follows an isolated work turn, and prior bodies reach later planning. Full history storage/selection horizon is unresolved; send approval is separate from generation/storage."
        - scope: "Human-approved skill admission, human HTTP editing and explicit reviewer replacement/publication"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-instruction-admission"
            - "workflow.md#wf-rte-draft-delivery"
          note: "These separately classified mechanisms require human content decisions, so they are not automatic trace-fed admissions. This is not an evidenced no for the system."
        - scope: "Fixed-policy/field-based extraction provisioning and index repartition"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-profile-provision"
            - "memory.md#mem-rte-node-splitting"
          note: "Known transformations use policy/organization fields or retained documents to configure access/extraction; the records do not establish a trace-fed durable behavioral update at these mechanisms."
        - scope: "Model-mediated standing configuration and scheduled instruction derivation, debug caller and hosted internal extraction"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-config-edit"
            - "runtime.md#rt-rte-scheduled-task"
            - "memory.md#mem-rte-debug-capture"
            - "memory.md#mem-obj-derived-memory"
          note: "Automatic configuration/schedule admissions exist, but recorded provenance does not settle which inputs are traces; generic debug principal and opaque hosted transformations prevent complete classification."
        - scope: "Optional sandbox and other evaluator-driven durable revisions"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
            - "memory.md#mem-obj-derived-memory"
            - "epistemic.md#epi-rte-draft-check"
          note: "No accepted record traces a retained sandbox/evaluator-feedback update to a durable later behavior-shaping artifact. Live administrative feedback interpretation is not such a write."
      records:
        - "runtime.md#rt-rte-knowledge-handoff"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-brain-document"
        - "memory.md#mem-bap-retained-context"
        - "memory.md#mem-obj-agent-style"
        - "memory.md#mem-rte-style-recall"
        - "epistemic.md#epi-rte-style-generation"
        - "epistemic.md#epi-rte-style-admission"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-approval-resume"
        - "memory.md#mem-rte-investigation-recall"
        - "memory.md#mem-obj-thread-investigation"
        - "runtime.md#rt-rte-research-draft"
        - "epistemic.md#epi-rte-draft-check"
        - "runtime.md#rt-rte-instruction-admission"
        - "workflow.md#wf-rte-draft-delivery"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-rte-node-splitting"
        - "memory.md#mem-rte-config-edit"
        - "runtime.md#rt-rte-scheduled-task"
        - "memory.md#mem-rte-debug-capture"
        - "memory.md#mem-obj-derived-memory"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Automatic trace-fed retained outputs have later consumers, establishing wired capacity rather than improved behavior. No system-wide no is asserted. Unresolved provider routes, scheduler/configuration provenance and sandbox continuity prevent complete coverage."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Interactive/resumed knowledge capture"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-handoff"
                - "memory.md#mem-obj-brain-document"
              note: "Conversation content feeds automatically retained subject documents."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-handoff"
                - "memory.md#mem-obj-brain-document"
              note: "Tool observations can feed the model-authored retained synthesis."
          records:
            - "runtime.md#rt-rte-knowledge-handoff"
            - "memory.md#mem-obj-brain-document"
          note: "Original inputs include conversational turns and model/tool observations from agent work; these precede hosted extraction."
        - scope: "Channel durable-cluster and public-thread style writes"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-channel-curation"
                - "memory.md#mem-obj-channel-batch"
                - "memory.md#mem-obj-agent-style"
              note: "Bounded HUMAN/bot-context conversational records feed distillation and style generation."
          records:
            - "memory.md#mem-rte-channel-curation"
            - "memory.md#mem-obj-channel-batch"
            - "memory.md#mem-obj-agent-style"
          note: "Original Slack conversational messages/reactions expressed in messages are session logs. Their spool timestamps do not change origin into environmental event streams."
        - scope: "Approval continuation compaction"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-approval-resume"
              note: "Recorded conversation turns feed bounded continuation messages."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-boundary"
                - "runtime.md#rt-rte-approval-resume"
              note: "Tool-call/result structures and bounded outputs survive compaction."
          records:
            - "runtime.md#rt-rte-context-boundary"
            - "runtime.md#rt-rte-approval-resume"
          note: "Retained message array includes conversation and tool requests/results, not a dereferenceable raw-result archive."
        - scope: "Investigation checkpoint source"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-thread-investigation"
                - "memory.md#mem-rte-investigation-recall"
              note: "Last answer/goal and answer-derived evidence come from the work conversation."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-thread-investigation"
                - "memory.md#mem-rte-investigation-recall"
              note: "Bounded native call inputs/outputs/statuses feed retained checkpoint entries."
          records:
            - "memory.md#mem-obj-thread-investigation"
            - "memory.md#mem-rte-investigation-recall"
          note: "Prior answer and tool-input/output excerpts are inspected source kinds. No linked state/action/outcome experience beyond tool records is established merely by the trajectory label."
        - scope: "Research draft body and review/history trail"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "epistemic.md#epi-obj-research-draft"
              note: "Completed draft-turn reply becomes retained later planning content."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-draft"
                - "epistemic.md#epi-rte-draft-check"
              note: "Selected executed tool/argument trail can enter retained draft material; the record does not guarantee evidence-producing tools for every body."
          records:
            - "runtime.md#rt-rte-research-draft"
            - "epistemic.md#epi-rte-draft-check"
            - "epistemic.md#epi-obj-research-draft"
            - "memory.md#mem-bap-retained-context"
          note: "Work-turn output and selected tool trail are supported; complete source mixtures and history selection remain unresolved. A tool-free retained draft remains possible."
        - scope: "Manual content decisions and nontrace provisioning/index operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-instruction-admission"
            - "workflow.md#wf-rte-draft-delivery"
            - "memory.md#mem-rte-profile-provision"
            - "memory.md#mem-rte-node-splitting"
          note: "No qualifying automatic trace-fed write is established within these specifically bounded mechanisms. Their exclusion is local, not a complete system-negative trace finding."
        - scope: "Schedule/configuration/debug and hosted opaque alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-scheduled-task"
            - "memory.md#mem-rte-config-edit"
            - "memory.md#mem-rte-debug-capture"
            - "memory.md#mem-obj-derived-memory"
          note: "Their qualifying trace-write status or original source mixture remains unresolved. They cannot be made inapplicable by another route being nontrace."
        - scope: "Optional sandbox trace sources and uninspected evaluator-driven revision"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-sandbox-work"
            - "epistemic.md#epi-rte-draft-check"
          note: "The records do not inventory original input to any qualifying retained sandbox/evaluation update."
      records:
        - "runtime.md#rt-rte-knowledge-handoff"
        - "memory.md#mem-obj-brain-document"
        - "memory.md#mem-rte-channel-curation"
        - "memory.md#mem-obj-channel-batch"
        - "memory.md#mem-obj-agent-style"
        - "runtime.md#rt-rte-context-boundary"
        - "runtime.md#rt-rte-approval-resume"
        - "memory.md#mem-obj-thread-investigation"
        - "memory.md#mem-rte-investigation-recall"
        - "runtime.md#rt-rte-research-draft"
        - "epistemic.md#epi-rte-draft-check"
        - "epistemic.md#epi-obj-research-draft"
        - "memory.md#mem-bap-retained-context"
        - "runtime.md#rt-rte-instruction-admission"
        - "workflow.md#wf-rte-draft-delivery"
        - "memory.md#mem-rte-profile-provision"
        - "memory.md#mem-rte-node-splitting"
        - "runtime.md#rt-rte-scheduled-task"
        - "memory.md#mem-rte-config-edit"
        - "memory.md#mem-rte-debug-capture"
        - "memory.md#mem-obj-derived-memory"
        - "runtime.md#rt-rte-sandbox-work"
      note: "Sources follow original content, not adapter labels. Known conversational and tool activity feeds qualifying writes. No event-streams or trajectories finding follows merely from Slack timestamps or a trajectory field name; unresolved input mixtures and opaque alternatives prevent a complete list."
---

# Company Brain memory profile

## Comparison rationale

This profile classifies accepted records, not new source observations. The scoped inventory is the union of the material memory mechanisms recorded in the supplied reports. Every axis retains unresolved service state and relevant available-but-uninspected alternatives instead of treating an inspected local route as a complete system inventory. All positive implementation findings concern wiring or affordances. There is no supplied observed run or causal experiment.

### Objects and provider limits

A submitted document, the hosted derived text, local access metadata and a later rendered summary are different operative parts. [MEM-OBJ-brain-document](memory.md#mem-obj-brain-document) and [MEM-OBJ-derived-memory](memory.md#mem-obj-derived-memory) support service-object storage at the application interface. They do not establish vector storage or a parametric representation of an embedding. SQL-backed retained objects support rdbms without assuming an unrecorded SQLite engine. The workspace-prompt and schedule records do not identify their physical persistence implementation, so those units remain unresolved even though persistence itself is wired.

Extraction policy has a known local provisioning route but an opaque later remote consumer. Its instruction authority and semantic curation requests retain claimed bases. [MEM-CLM-service-curation](memory.md#mem-clm-service-curation) supports requested duplicate merging, supersession, transient forgetting and pattern inference; none becomes a wired remote transformation from the strength of local submission or liveness filtering. Topic splitting changes access organization and same-text metadata, not necessarily one of the controlled claim-curation operations. [MEM-RTE-node-splitting](memory.md#mem-rte-node-splitting) retains partial-update and tag-normalization limits.

### Admission, authority and trace-fed reuse

Approval is specific to a mechanism. [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission) establishes requester-approved skills and editor-supplied HTTP text; [MEM-RTE-config-edit](memory.md#mem-rte-config-edit) establishes a separate model-mediated admin writer without that per-text decision. Generated research drafts are automatically stored; reviewer replacement and explicit publication are separate human decisions under [WF-RTE-draft-delivery](workflow.md#wf-rte-draft-delivery). Generic debug caller identity does not resolve human control under [MEM-RTE-debug-capture](memory.md#mem-rte-debug-capture).

Knowledge delivered to an answering model, directions delivered as standing guidance, and retained experience used at a durable update consumer carry separate authority findings. Raw channel spools and carried style state can be learning inputs at distillation/observation, while the resulting content supplies knowledge or instruction downstream. Stored tags/counts/scores influence ranking; mappings/cursors/timing route operations; generation/status/liveness criteria validate and veto eligibility. No inference treats every descriptive tag as a factual warrant or every instruction as executable enforcement.

Automatic trace-fed document/style production, deterministic conversation compaction and checkpoint construction retain behavior-shaping content for later invocations. These satisfy trace_learning at the wired-capacity layer without weight changes, demonstrated improvement or a mandatory novel claim. Research output reuse is also retained history for later planning, but its complete source mixture and selection horizon remain partial. The schedule/configuration records do not by themselves settle qualifying trace provenance. A route not established as trace-fed is not a system-wide negative. No accepted bounded-absence record warrants a trace_learning no union.

Sources are classified by origin: Slack conversational messages are session logs, including when stored with timestamps or processed by an observer. Actual tool requests/results support tool-traces. The field called trajectory does not alone establish trajectories as linked state/action/outcome experience. Imported web information and static extraction instructions do not become event streams merely because software processes them.

### Selection and chains

[MEM-RTE-ambient-recall](memory.md#mem-rte-ambient-recall) and [MEM-RTE-style-recall](memory.md#mem-rte-style-recall) independently supply context. Person/thread identity matching is targeted push selection; liveness, candidate caps, available baseline and recognized buckets are coarse selection. [MEM-RTE-requested-recall](memory.md#mem-rte-requested-recall), skill load, entity lookup and human readers fulfill requests, so their semantic/lexical query mechanisms do not automatically establish inferred push signals. Approval-triggered restoration fulfills a request for a specified continuation; independent checkpoint reload is a distinct push operation. The schedule callback independently starts execution, whereas a reviewer's draft-ID send requests delivery. Automatic history supply to planning remains separate from that requested send.

An inspected readable display does not resolve the opaque selected provider payload or embedding provenance. Restoring an investigation checkpoint establishes later state reuse, but [MEM-RTE-investigation-recall](memory.md#mem-rte-investigation-recall) leaves complete final rendering unresolved. Such local gaps survive positive findings.

### Canonicalization and source-read log

The supplied reconciliation resolves three duplicate identities. Style-object classifications cite [MEM-OBJ-agent-style](memory.md#mem-obj-agent-style), not the superseded epistemic style object. Partition classifications cite [MEM-RTE-node-splitting](memory.md#mem-rte-node-splitting), not the superseded epistemic partition route. Publication/editing classifications cite [WF-RTE-draft-delivery](workflow.md#wf-rte-draft-delivery), not the superseded epistemic sender. Those supersessions change citation identity, not the analysts' warrants. Distinct combined routes and their parts remain distinct.

Administrative reception acquisition/framing/interpretation under [EPI-RTE-outcome-acquisition](epistemic.md#epi-rte-outcome-acquisition), [EPI-RTE-outcome-frame](epistemic.md#epi-rte-outcome-frame) and [EPI-RTE-admin-consumption](epistemic.md#epi-rte-admin-consumption) establishes an operative feedback consumer, but no automatic persisted criticism or planning-policy update. Its transient outcome payload is excluded from the retained-object inventory; retained sent references and body history remain included. This does not turn missing episodes into absent criticism or erase implemented feedback consumption.

Additional frozen-source reads: none. All classification warrants come from the supplied accepted records and their annotations; no source fact was added or report verification reopened.
