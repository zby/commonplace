---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Ars Contexta memory profile: accumulated vault content, operational guidance, checkpoints and distinct later-consumer routes at the frozen commit."
run-id: "AAS-2026-10-12-arscontexta-f9e5f2f34166-01"
source-identity: "https://github.com/agenticnotetaking/arscontexta"
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
memory-comparison:
  version: 2
  scope: "Accumulated or revised domain notes and source archives; topic maps and inline navigation; queue/task findings; derivation/configuration and generated or revised live context, skills and templates; methodology/observations; session lifecycle and substantive handoff alternatives; task priorities, recommendation and diagnostic history; optional numerical search/index/cache parts and unresolved progress/history alternatives. Includes registered plugin and generated-template write/read-back branches separately. Excludes unchanged bundled methodology/presets/templates as static guidance, external host/model weight state, and transient warnings/answers without retained writers. External search implementation remains uninspected rather than inferred from readable hits."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Vault content, navigation, operational evidence, checkpoint files, queue and generated live instructions"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-topic-maps"
                - "memory.md#mem-obj-task-files"
                - "memory.md#mem-obj-derivation"
                - "memory.md#mem-obj-methodology"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-session-state"
                - "memory.md#mem-obj-session-log"
                - "memory.md#mem-obj-task-stack"
                - "memory.md#mem-obj-next-log"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-queue"
                - "runtime.md#rt-obj-claude-md"
              note: "The retained payloads and access structures reside in vault/project files."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-topic-maps"
            - "memory.md#mem-obj-task-files"
            - "memory.md#mem-obj-derivation"
            - "memory.md#mem-obj-methodology"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-session-state"
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-obj-task-stack"
            - "memory.md#mem-obj-next-log"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-queue"
            - "runtime.md#rt-obj-claude-md"
          note: "All these declared objects are filesystem files; Markdown, YAML and JSON are encodings, not distinct substrates."
        - scope: "Optional Git persistence of accumulated vault and instruction files"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-write-hooks"
              note: "The configured callback stages pending changes into a Git repository; failure is tolerated."
          records:
            - "runtime.md#rt-rte-write-hooks"
          note: "The registered commit callback establishes optional Git persistence. Copied skill versions and manual rollback establish file archival, not a separate repository mechanism."
        - scope: "Optional search index, embeddings and persisted search caches"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
          note: "The records identify numerical/index alternatives but do not inspect their storage. A readable search hit cannot establish vector, sqlite or service-object storage."
        - scope: "Stats-history snapshot and alternate builder/progress initialization"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "The YAML history writer and opaque tutorial-progress initialization are unresolved. Encoding and a named history file do not establish the full operative storage inventory."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-topic-maps"
        - "memory.md#mem-obj-task-files"
        - "memory.md#mem-obj-derivation"
        - "memory.md#mem-obj-methodology"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-obj-task-stack"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-obj-queue"
        - "runtime.md#rt-obj-claude-md"
        - "runtime.md#rt-rte-write-hooks"
        - "memory.md#mem-rte-note-maintenance"
        - "runtime.md#rt-clm-generation-paths"
      note: "The declared file and Git surfaces are classified. Optional numerical memory and unresolved history/progress alternatives prevent a complete substrate inventory. External model weights are outside accumulated target memory, not a positive model-weights finding."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Note arguments, map prose, task findings, derivation reasons, directives, source texts, working summaries and report/recommendation prose at interpretive readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-topic-maps"
                - "memory.md#mem-obj-task-files"
                - "memory.md#mem-obj-derivation"
                - "memory.md#mem-obj-methodology"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-session-log"
                - "memory.md#mem-obj-task-stack"
                - "memory.md#mem-obj-next-log"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-claude-md"
              note: "Later models or humans interpret the content as claims, reasons, context or directions."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-topic-maps"
            - "memory.md#mem-obj-task-files"
            - "memory.md#mem-obj-derivation"
            - "memory.md#mem-obj-methodology"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-obj-task-stack"
            - "memory.md#mem-obj-next-log"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-claude-md"
          note: "This unit covers semantic prose only; fixed-rule fields are classified separately."
        - scope: "Queue phase fields, lifecycle JSON, status/target metadata, configuration flags and host-facing generated metadata at fixed-rule consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "memory.md#mem-obj-derivation"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-task-stack"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-queue"
                - "runtime.md#rt-obj-claude-md"
              note: "Localized identifiers, statuses and configuration fields select phases, lifecycle records, conditions and host options."
          records:
            - "memory.md#mem-obj-session-state"
            - "memory.md#mem-obj-derivation"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-task-stack"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-queue"
            - "runtime.md#rt-obj-claude-md"
          note: "This unit excludes the surrounding argument and directive bodies."
        - scope: "Optional numerical search payload, embeddings and cache encoding"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
          note: "The record explicitly separates readable results from uninspected numerical memory; neither parametric nor symbolic encoding can be assigned to that payload from its display."
        - scope: "Opaque progress initialization and unresolved stats-history payload"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "A filename or format hint does not classify every operative part or consumption path."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-topic-maps"
        - "memory.md#mem-obj-task-files"
        - "memory.md#mem-obj-derivation"
        - "memory.md#mem-obj-methodology"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-obj-task-stack"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-obj-claude-md"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-obj-queue"
        - "memory.md#mem-rte-note-maintenance"
        - "runtime.md#rt-clm-generation-paths"
      note: "Prose and fixed-rule metadata are separated at their consumers. Uninspected numerical payloads and alternate history/progress parts prevent complete form coverage; the session model is an external component, not retained target memory."
    lineage:
      assessment: "partial"
      units:
        - scope: "User/manual domain notes and supplied captures"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-inbox"
              note: "Users can author notes and capture their own content; source-derived alternatives are separate."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-inbox"
          note: "This is the evidenced authoring/admission path, not the unknown initial corpus."
        - scope: "External source texts and research-service findings entering inbox/archive"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-rte-research-intake"
              note: "External texts and provider findings enter retained source files; provenance does not authenticate truth."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-rte-research-intake"
          note: "Acquisition is distinct from subsequent target-side themed writing."
        - scope: "Source-to-note extraction, task rationale and composition of configured instructions from bundled guidance"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reduce-content"
                - "memory.md#mem-obj-task-files"
                - "runtime.md#rt-rte-setup-generation"
              note: "Source extraction and feature/vocabulary composition produce retained successors from existing non-trace content."
            - value: "authored"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reduce-content"
              note: "The model supplies note reasoning, uncertainty and counterargument beyond merely copying a source."
          records:
            - "epistemic.md#epi-rte-reduce-content"
            - "memory.md#mem-obj-task-files"
            - "runtime.md#rt-rte-setup-generation"
          note: "The known transformation paths do not resolve semantic fidelity or every initial input."
        - scope: "Remember directives/observations and recorded phase/recommendation findings derived from work experience"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-obj-task-files"
                - "memory.md#mem-obj-next-log"
              note: "Corrections, session evidence, phase findings and recommendation activity are converted to durable operational material."
          records:
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-obj-task-files"
            - "memory.md#mem-obj-next-log"
          note: "Classification concerns derivation from activity, not proof of exercised learning."
        - scope: "Topic-map relationship prose and opening argument"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-topic-maps"
                - "epistemic.md#epi-obj-topic-maps"
                - "epistemic.md#epi-rte-reflect-use"
              note: "Human/agent curation writes relationship explanations and model-generated map openings."
          records:
            - "memory.md#mem-obj-topic-maps"
            - "epistemic.md#epi-obj-topic-maps"
            - "epistemic.md#epi-rte-reflect-use"
          note: "Authorship does not assert that the opening makes a novel or warranted claim."
        - scope: "Initial notes, goals/identity and presets versus user-derived initialization"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-obj-derivation"
          note: "The records preserve alternative initial sources but no installed artifacts settle their provenance."
        - scope: "Optional embeddings, stats-history and alternate generation provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "The numerical derivation, history writer and copied-versus-inherited deployment remain unresolved. Known source extraction cannot resolve these other paths."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-rte-research-intake"
        - "epistemic.md#epi-rte-reduce-content"
        - "memory.md#mem-obj-task-files"
        - "runtime.md#rt-rte-setup-generation"
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-obj-topic-maps"
        - "epistemic.md#epi-obj-topic-maps"
        - "epistemic.md#epi-rte-reflect-use"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-obj-derivation"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
      note: "Authored, imported, compiled and trace-extracted paths coexist. Initial corpus provenance, numerical derivation and alternate initialization/deployment are not resolved by those witnesses."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Notes, topic prose, sources, task findings and health/operational evidence at later knowledge-work and answering consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-bap-retained-content"
                - "memory.md#mem-rte-local-guidance"
                - "memory.md#mem-obj-health"
              note: "Reflect/reweave, ask, next and architect consume retained material as context, evidence or advice."
          records:
            - "memory.md#mem-bap-retained-content"
            - "memory.md#mem-rte-local-guidance"
            - "memory.md#mem-obj-health"
          note: "Knowledge authority is reference/context use, not acceptance as true."
        - scope: "Live generated context/skills and full accumulated methodology at later guidance consumers"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-bap-context-instructions"
                - "memory.md#mem-obj-methodology"
              note: "Live context/skills and methodology bodies supply standing operating directions."
            - value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-generated-orientation"
              note: "The generated hook affords full self/methodology delivery; its recent-methodology title channel does not deliver full directives."
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
              note: "Registered orientation prints full self/methodology when identity exists; this is not its three-line operational-note excerpt channel."
          records:
            - "runtime.md#rt-bap-context-instructions"
            - "memory.md#mem-obj-methodology"
            - "memory.md#mem-rte-generated-orientation"
          note: "Full bodies are distinct from recent title/header displays; host loading and model compliance are external."
        - scope: "Recent operational-methodology headers/titles and lifecycle state at session display consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
                - "memory.md#mem-obj-session-state"
              note: "The plugin supplies lifecycle status and recent metadata as orientation context."
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-generated-orientation"
              note: "Generated orientation supplies titles and current status as context."
          records:
            - "runtime.md#rt-rte-session-orientation"
            - "memory.md#mem-rte-generated-orientation"
            - "memory.md#mem-obj-session-state"
          note: "A display summary has only the force of the selected part, not the omitted directive."
        - scope: "Curated topic links, queue phases, derivation configuration, mined/status markers and user priority targets at selection consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-topic-maps"
                - "runtime.md#rt-obj-queue"
                - "memory.md#mem-obj-derivation"
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-rte-work-selection"
              note: "Links select traversal inputs, phases select worker procedures, configuration selects generated artifacts, and markers/status/priorities select subsequent work."
          records:
            - "memory.md#mem-obj-topic-maps"
            - "runtime.md#rt-obj-queue"
            - "memory.md#mem-obj-derivation"
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-rte-work-selection"
          note: "Routing names operation/input selection; it does not assert a compiled scheduler or universal withdrawal."
        - scope: "Configuration flags at automatic session tracking and Git callback gates"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
                - "runtime.md#rt-rte-write-hooks"
              note: "Retained session_capture/git settings permit or suppress automatic tracking/commit effects."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
                - "runtime.md#rt-rte-write-hooks"
              note: "The retained flags select enabled callback branches."
          records:
            - "memory.md#mem-obj-derivation"
            - "runtime.md#rt-rte-session-orientation"
            - "runtime.md#rt-rte-write-hooks"
          note: "Only configured hook operations are covered; content writes are not universally blocked."
        - scope: "Retained map framing, user priorities and recommendation history at relative-priority consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reflect-use"
                - "memory.md#mem-rte-work-selection"
                - "memory.md#mem-obj-next-log"
              note: "Map framing influences traversal; Current tasks override automatic signals and repeated recommendations lose priority."
          records:
            - "epistemic.md#epi-rte-reflect-use"
            - "memory.md#mem-rte-work-selection"
            - "memory.md#mem-obj-next-log"
          note: "This is priority influence, not an inspected numerical ranking implementation."
        - scope: "Retained configuration-dependent templates at note quality checking"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-config-refactor"
                - "epistemic.md#epi-rte-verify-check"
              note: "Regenerated templates/schema criteria are used to check candidate conformity."
          records:
            - "memory.md#mem-rte-config-refactor"
            - "epistemic.md#epi-rte-verify-check"
          note: "The unit covers regenerated domain criteria, not the bundled static kernel or transient warning output."
        - scope: "Session evidence, observations and recommendation history at durable guidance/update consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
                - "runtime.md#rt-rte-architecture-evolution"
                - "memory.md#mem-rte-work-selection"
              note: "Retained experience feeds directives, approved standing-guidance revisions and next-round behavior-shaping recommendation history."
          records:
            - "memory.md#mem-rte-friction-retention"
            - "runtime.md#rt-rte-architecture-evolution"
            - "memory.md#mem-rte-work-selection"
          note: "Learning authority is the update-consumer effect; it is independent of downstream instruction and measured improvement."
        - scope: "Numerical ranking inputs and unresolved history/progress consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "Search ranking implementation, stats-history production and alternate progress consumption remain uninspected; no force is assigned to unused metadata."
      records:
        - "memory.md#mem-bap-retained-content"
        - "memory.md#mem-rte-local-guidance"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-bap-context-instructions"
        - "memory.md#mem-obj-methodology"
        - "memory.md#mem-rte-generated-orientation"
        - "runtime.md#rt-rte-session-orientation"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-obj-topic-maps"
        - "runtime.md#rt-obj-queue"
        - "memory.md#mem-obj-derivation"
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-rte-work-selection"
        - "runtime.md#rt-rte-write-hooks"
        - "epistemic.md#epi-rte-reflect-use"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-rte-config-refactor"
        - "epistemic.md#epi-rte-verify-check"
        - "runtime.md#rt-rte-architecture-evolution"
        - "memory.md#mem-rte-note-maintenance"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-obj-session-log"
      note: "The actual readers distinguish knowledge, instruction, routing, ranking, validation, configured vetoes and learning-input authority. Opaque search/history/progress alternatives remain unresolved; post-Write warnings do not establish content enforcement."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Manual notes/captures, explicit remember guidance and user task-stack edits"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-rte-work-selection"
              note: "Users supply the retained content or explicitly order stack edits; explicit remember needs no second confirmation."
          records:
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-rte-work-selection"
          note: "Human content supply or direct editing orders are admission decisions, even when software performs I/O."
        - scope: "Contextual remember, interactive reweave and approved architecture/refactor/upgrade replacements"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-rte-config-refactor"
                - "runtime.md#rt-rte-architecture-evolution"
                - "runtime.md#rt-rte-skill-upgrade"
              note: "The user confirms interpreted corrections or approves/selects successor content before admission."
          records:
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-rte-config-refactor"
            - "runtime.md#rt-rte-architecture-evolution"
            - "runtime.md#rt-rte-skill-upgrade"
          note: "Each mechanism has its own explicit confirmation or replacement approval."
        - scope: "Reduce extracted-note admission under prescribed approval policy"
          assessment: "partial"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-reduce-admission"
              note: "The standalone and handoff reduce procedure explicitly requires approval of findings before files."
          records:
            - "epistemic.md#epi-rte-reduce-admission"
            - "runtime.md#rt-rte-source-processing"
          note: "Reduce requires approval, including handoff; dontAsk and initial extraction eligibility leave the wrapper path unresolved."
        - scope: "Learn filing, reflect links, handoff reweave, session mining and next condition/history writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-research-intake"
                - "epistemic.md#epi-rte-reflect-use"
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-rte-work-selection"
              note: "Model admission without a per-content human decision is specified on these routes."
          records:
            - "memory.md#mem-rte-research-intake"
            - "epistemic.md#epi-rte-reflect-use"
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-rte-work-selection"
          note: "Starting a command is not approval of each admitted finding, link or recommendation."
        - scope: "Lifecycle tracking, marker migration and broad post-Write Git persistence"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
                - "runtime.md#rt-rte-write-hooks"
              note: "Callbacks write lifecycle/marker state and commit pending content without approval dialogs."
          records:
            - "runtime.md#rt-rte-session-orientation"
            - "runtime.md#rt-rte-write-hooks"
          note: "Automatic physical persistence is separate from the original content admission mechanisms."
        - scope: "Initial goals/identity, working-summary admission, stats-history and alternate progress writer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
          note: "Instructions support human/model checkpoint alternatives but do not settle every admission control; installed initialization and opaque writers are unsupplied."
        - scope: "Optional numerical index/cache writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
          note: "No recorded provider write/admission mechanism establishes human versus software control."
      records:
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-rte-work-selection"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-rte-config-refactor"
        - "runtime.md#rt-rte-architecture-evolution"
        - "runtime.md#rt-rte-skill-upgrade"
        - "epistemic.md#epi-rte-reduce-admission"
        - "runtime.md#rt-rte-source-processing"
        - "memory.md#mem-rte-research-intake"
        - "epistemic.md#epi-rte-reflect-use"
        - "runtime.md#rt-rte-session-orientation"
        - "runtime.md#rt-rte-write-hooks"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
      note: "Both human-controlled and automatic admission exist. The approval/dontAsk conflict, initial content, summary alternatives and opaque writers prevent a universal write-agency classification."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Remember conversion of retained session evidence to scoped directives/observations and duplicate extension"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
              note: "Session evidence is selected and compressed into standing scoped guidance while raw input can remain."
            - value: "dedup"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
              note: "Equivalent guidance extends an existing directive instead of creating a duplicate."
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
              note: "Existing directives can be extended and replaced."
            - value: "invalidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-obj-methodology"
              note: "Old directives are marked superseded with successor pointers; withdrawal intent is retained, but a universal active-only read filter is not established."
          records:
            - "memory.md#mem-rte-friction-retention"
          note: "The inspected procedure specifies these transformations; it does not show successful execution."
        - scope: "Reweave note and reflect/map revision"
          assessment: "partial"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-note-maintenance"
                - "epistemic.md#epi-rte-reflect-use"
              note: "Existing note arguments, descriptions, links and map openings are revised."
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "epistemic.md#epi-rte-reflect-use"
            - "epistemic.md#epi-rte-reduce-content"
          note: "Revision is supported; new note/map propositions are semantically indeterminate, and synthesis opportunities are only flagged."
        - scope: "Confirmed operational-evidence triage and approved instruction replacement"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-architecture-evolution"
              note: "Confirmed triage can raise pending evidence into domain notes or canonical methodology."
            - value: "invalidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-architecture-evolution"
              note: "Archived/resolved dispositions remove items from pending/open reliance while preserving status/reason/target history."
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-architecture-evolution"
                - "runtime.md#rt-rte-skill-upgrade"
                - "memory.md#mem-rte-config-refactor"
              note: "Approved successors replace live context, skills, configuration or templates."
          records:
            - "memory.md#mem-obj-observations"
            - "runtime.md#rt-rte-architecture-evolution"
            - "runtime.md#rt-rte-skill-upgrade"
            - "memory.md#mem-rte-config-refactor"
          note: "Triage disposition and instruction succession are separate from epistemic acceptance."
        - scope: "User task withdrawal and next recommendation-history priority adjustment"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-task-stack"
                - "memory.md#mem-obj-next-log"
              note: "Drop removes a live task; repeated recommendations are downweighted in later selection."
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-work-selection"
              note: "Condition reconciliation updates targets and closes satisfied maintenance entries."
          records:
            - "memory.md#mem-obj-task-stack"
            - "memory.md#mem-rte-work-selection"
            - "memory.md#mem-obj-next-log"
          note: "Removal and downweighting have concrete live selectors, unlike mere archive existence."
        - scope: "Reduce content expansion, learn themed findings and map opening semantic novelty"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-reduce-content"
            - "memory.md#mem-rte-research-intake"
            - "epistemic.md#epi-obj-topic-maps"
            - "epistemic.md#epi-rte-reflect-use"
          note: "The accepted records cannot distinguish compression, entailed expansion and new conjecture for every produced part. A synthesis label or future-work flag does not prove an executed synthesize transformation."
        - scope: "Optional numerical-index transformations and unresolved alternate history/progress maintenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "Index rebuild requests and file-count freshness checks establish no curation operation by themselves; opaque branches remain included."
      records:
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-rte-note-maintenance"
        - "epistemic.md#epi-rte-reflect-use"
        - "epistemic.md#epi-rte-reduce-content"
        - "memory.md#mem-obj-observations"
        - "runtime.md#rt-rte-architecture-evolution"
        - "runtime.md#rt-rte-skill-upgrade"
        - "memory.md#mem-rte-config-refactor"
        - "memory.md#mem-obj-task-stack"
        - "memory.md#mem-rte-work-selection"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-rte-research-intake"
        - "epistemic.md#epi-obj-topic-maps"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-obj-session-log"
      note: "Consolidation, duplicate handling, revision, withdrawal, promotion and forgetting/downweighting have local procedural witnesses. Novelty-sensitive transformations and opaque maintenance are unresolved; archival or indexing alone is not a curation value."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested note/task/source/local-methodology reads, derivation rereads and advisory work-selection inputs"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-note-maintenance"
                - "memory.md#mem-rte-local-guidance"
                - "memory.md#mem-rte-work-selection"
                - "memory.md#mem-obj-task-files"
                - "memory.md#mem-obj-derivation"
                - "memory.md#mem-rte-research-intake"
                - "runtime.md#rt-rte-architecture-evolution"
              note: "Later invocations request files/search results, full bodies, checkpoints and retained evidence."
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-rte-local-guidance"
            - "memory.md#mem-rte-work-selection"
            - "memory.md#mem-obj-task-files"
            - "memory.md#mem-obj-derivation"
            - "memory.md#mem-rte-research-intake"
            - "runtime.md#rt-rte-architecture-evolution"
          note: "The consumer asks tools for retained material; returning the requested file is not an additional push."
        - scope: "Registered SessionStart unsolicited orientation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
              note: "Host event triggers automatic stdout supply to the session."
          records:
            - "runtime.md#rt-rte-session-orientation"
          note: "The callback selects existing goals/self bodies, recent headers and lifecycle JSON independently of a retained-content request."
        - scope: "Generated SessionStart unsolicited orientation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-generated-orientation"
              note: "Generated hook affords goals/self bodies, recent titles and previous lifecycle state as context."
          records:
            - "memory.md#mem-rte-generated-orientation"
          note: "This is the distinct generated-template route, not a proven installation."
        - scope: "Host-loaded accumulated context and lead-selected sibling content in worker prompts"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-bap-context-instructions"
                - "runtime.md#rt-rte-source-processing"
                - "runtime.md#rt-rte-parallel-claims"
              note: "Standing project context and selected same-batch sibling titles are supplied without a worker request for that material."
          records:
            - "runtime.md#rt-bap-context-instructions"
            - "runtime.md#rt-rte-source-processing"
            - "runtime.md#rt-rte-parallel-claims"
          note: "The lead selects sibling titles for workers before their own requested task/body reads."
        - scope: "Alternate copied/inherited delivery, optional search payload and unresolved summary/history/progress consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-obj-task-files"
          note: "Known pulls/pushes do not settle installed loading, opaque payload delivery, batch-summary consumption or all alternate progress/history routes."
      records:
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-rte-local-guidance"
        - "memory.md#mem-rte-work-selection"
        - "memory.md#mem-obj-task-files"
        - "memory.md#mem-obj-derivation"
        - "memory.md#mem-rte-research-intake"
        - "runtime.md#rt-rte-architecture-evolution"
        - "runtime.md#rt-rte-session-orientation"
        - "memory.md#mem-rte-generated-orientation"
        - "runtime.md#rt-bap-context-instructions"
        - "runtime.md#rt-rte-source-processing"
        - "runtime.md#rt-rte-parallel-claims"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-obj-session-log"
      note: "Requested reads and unsolicited hook/host/lead supplies coexist. Generated and registered deployment retain separate evidence bases; unresolved alternatives prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Plugin SessionStart file-existence, preferred-goals and recent-header selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-orientation"
              note: "Fixed file availability and recency/limit selection supply orientation context; session IDs do not establish targeted delivered-content matching."
          records:
            - "runtime.md#rt-rte-session-orientation"
            - "memory.md#mem-obj-session-state"
          note: "Trigger is SessionStart; selector inputs are availability, configured flags and mtime; retained parts are full goals/self, current JSON and five header excerpts."
        - scope: "Generated SessionStart file-existence and recent-title selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-generated-orientation"
              note: "Existence/recency gates and five-file budget afford non-semantic selection."
          records:
            - "memory.md#mem-rte-generated-orientation"
          note: "Trigger is SessionStart; selector inputs are file presence, self-versus-ops preference and mtime; selected parts are full self/goals, current state and five titles."
        - scope: "Lead supplies already-created sibling titles to reflect/reweave and parallel workers"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-processing"
                - "runtime.md#rt-rte-parallel-claims"
              note: "Actual same-batch matching selects delivered sibling parts."
            - value: "coarse"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-processing"
              note: "Create-completion eligibility limits siblings to already-created notes before identifier-selected delivery."
          records:
            - "runtime.md#rt-rte-source-processing"
            - "runtime.md#rt-rte-parallel-claims"
          note: "Trigger is worker-prompt construction; selector inputs include batch identity and completed create status; selected retained parts are sibling titles/task paths, not all bodies."
        - scope: "Automatic project context loading"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records:
                - "runtime.md#rt-bap-context-instructions"
                - "runtime.md#rt-obj-claude-md"
              note: "Standing context is selected through project loading rather than semantic query or identity matching of memories."
          records:
            - "runtime.md#rt-bap-context-instructions"
            - "runtime.md#rt-obj-claude-md"
          note: "Later session trigger supplies the live project context; requested skill loading is not used as an identifier-push witness."
        - scope: "Unresolved alternate loading/progress/history and opaque search supply"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-note-maintenance"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
          note: "Recorded requested search routes do not warrant inferred-embedding or inferred-lexical push. Missing selector/payload facts prevent classifying unresolved alternatives."
      records:
        - "runtime.md#rt-rte-session-orientation"
        - "memory.md#mem-obj-session-state"
        - "memory.md#mem-rte-generated-orientation"
        - "runtime.md#rt-rte-source-processing"
        - "runtime.md#rt-rte-parallel-claims"
        - "runtime.md#rt-bap-context-instructions"
        - "runtime.md#rt-obj-claude-md"
        - "memory.md#mem-rte-note-maintenance"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-obj-session-log"
      note: "Push signals are coarse availability/recency/state gates and actual batch-identifier matching. Lexical/semantic requested retrieval is pull, not proof of an inferred push signal; the axis is not pull-only inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Remember session mining without per-finding human admission, followed by directive/observation consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
                - "memory.md#mem-obj-methodology"
                - "memory.md#mem-obj-observations"
              note: "Model mining writes scoped behavior guidance or operational evidence with reasons, later read by ask/rethink."
          records:
            - "memory.md#mem-rte-friction-retention"
            - "memory.md#mem-obj-methodology"
            - "memory.md#mem-obj-observations"
          note: "This is a qualifying automatic trace-fed durable-guidance route at claimed basis, not a closed transcript-capture deployment."
        - scope: "Next automatic recommendation-history update and later anti-repetition consumer"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-work-selection"
                - "memory.md#mem-obj-next-log"
              note: "Recorded recommendation activity yields durable state/action/rationale, later used to alter recommendation priority."
          records:
            - "memory.md#mem-rte-work-selection"
            - "memory.md#mem-obj-next-log"
          note: "Generated recommendation history shapes a later invocation without per-entry human approval."
        - scope: "Automatic worker phase findings and later task-file consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-task-files"
                - "runtime.md#rt-rte-source-processing"
                - "runtime.md#rt-rte-parallel-claims"
              note: "Workers retain phase findings and revision experience which later workers read as context and guidance."
          records:
            - "memory.md#mem-obj-task-files"
            - "runtime.md#rt-rte-source-processing"
            - "runtime.md#rt-rte-parallel-claims"
          note: "The phase-worker chain is conditional on eligible work and model compliance; extraction approval remains a separate admission."
        - scope: "Session-summary/handoff alternatives and missing automatic substantive transcript producer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-clm-transcript-gap"
          note: "Substantive summaries could qualify if automatic, retained and later consumed, but the recorded human/model alternatives and JSON-only hooks do not resolve every writer."
        - scope: "Other diagnostic-history, alternate generation/progress and numerical updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-rte-note-maintenance"
          note: "The reports do not fully trace every automatic activity-fed write and later behavior-shaping consumer. No system-wide no or bounded local no is inferred."
      records:
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-obj-methodology"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-rte-work-selection"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-obj-task-files"
        - "runtime.md#rt-rte-source-processing"
        - "runtime.md#rt-rte-parallel-claims"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-clm-transcript-gap"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-rte-note-maintenance"
      note: "Qualifying procedural yes routes coexist with unresolved automatic summary/history/alternate updates. Trace learning here needs neither accepted new knowledge nor demonstrated improvement. JSON lifecycle retention alone is not a substantive learning witness."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Remember session-mining conversation and recorded tool-failure/action evidence"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
              note: "The selected Markdown session evidence includes conversational corrections and repeated user redirections."
            - value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-friction-retention"
              note: "The mining input also includes recorded agent/tool failures and action feedback used to derive directives or observations."
          records:
            - "memory.md#mem-rte-friction-retention"
          note: "The unit names the original qualifying content, not the session-mining adapter label; no automatic transcript producer is inferred."
        - scope: "Worker phase findings produced from recorded execution and revision feedback"
          assessment: "partial"
          findings:
            - value: "tool-traces"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-task-files"
                - "runtime.md#rt-rte-source-processing"
              note: "Retained phase findings include file/tool work and verification/revision feedback for later workers."
          records:
            - "memory.md#mem-obj-task-files"
            - "runtime.md#rt-rte-source-processing"
          note: "Tool/phase feedback is supported, but complete mixed input provenance across every phase is not recorded."
        - scope: "Next recommendation-history original source classification"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-next-log"
            - "memory.md#mem-rte-work-selection"
          note: "The qualifying activity-to-history-to-later-selection route is known, but the records do not identify conversational turns, tool records, discrete environmental events or linked state/action/outcome sequences as its complete original input."
        - scope: "Alternative substantive session summaries, diagnostic-history and numerical/progress trace origins"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-session-log"
            - "memory.md#mem-clm-transcript-gap"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-clm-generation-paths"
            - "memory.md#mem-rte-note-maintenance"
          note: "Writer control, original input and later consumer are unresolved for these alternatives. Their source cannot be made inapplicable using the known yes routes or the JSON/transcript mismatch."
      records:
        - "memory.md#mem-rte-friction-retention"
        - "memory.md#mem-obj-task-files"
        - "runtime.md#rt-rte-source-processing"
        - "memory.md#mem-obj-next-log"
        - "memory.md#mem-rte-work-selection"
        - "memory.md#mem-obj-session-log"
        - "memory.md#mem-clm-transcript-gap"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-clm-generation-paths"
        - "memory.md#mem-rte-note-maintenance"
      note: "Session conversation and tool-feedback sources support qualifying trace-fed writes. Other mixed/opaque origins remain unresolved. Lifecycle timestamps are not automatically event-stream learning, and a multi-step workflow alone does not establish trajectory input."
---

# Ars Contexta memory profile

## Comparison rationale

### Boundary and coverage

This profile classifies accumulated retained parts and their later consumers, not all runtime state. File storage does not classify an embedding payload, and natural-language display hits do not classify the numerical search state. The optional index and unresolved initialization/history alternatives remain included as uncertainties. Initial goals and note provenance are separate from known subsequent transformations. See [MEM-RTE-note-maintenance](memory.md#mem-rte-note-maintenance), [MEM-OBJ-session-log](memory.md#mem-obj-session-log) and [MEM-OBJ-health](memory.md#mem-obj-health).

All ten axes are partial. Each has supported positive findings, but the accepted records do not close its scoped inventory. This is not a statement that every local unit is unknown, nor that missing execution erases architectural witnesses. Claimed model procedures, afforded generated hooks and wired registered hooks retain separate findings. No observed or causally supported finding is asserted.

### Admission, transformation and force

Manual means a human decision supplies or approves the content. Explicit remember and user task edits satisfy that test; invoking mining, learn or next does not make their subsequent model-admitted content manual. Reduce approval remains a supported manual branch beside the unresolved dontAsk/selection edge, not a universal gate. See [MEM-RTE-friction-retention](memory.md#mem-rte-friction-retention), [MEM-RTE-work-selection](memory.md#mem-rte-work-selection), [EPI-RTE-reduce-admission](epistemic.md#epi-rte-reduce-admission) and [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).

Remember's session-to-directive reduction supports consolidation even if the input logs survive. Revision, supersession and triage promotion have different consumer effects. Superseding a directive records withdrawal intent, but does not establish suppression at every full-body or recency reader. A synthesis opportunity is not an implemented synthesis write; map-opening and source-to-note semantic transformations retain the records' indeterminacy. See [MEM-RTE-friction-retention](memory.md#mem-rte-friction-retention), [MEM-OBJ-methodology](memory.md#mem-obj-methodology), [EPI-RTE-reflect-use](epistemic.md#epi-rte-reflect-use) and [EPI-RTE-reduce-content](epistemic.md#epi-rte-reduce-content).

Learning authority belongs to experience at a durable update consumer; instruction or knowledge authority belongs to the output at a later consumer. Neither implies measured improvement. Configured callback gates establish narrowly scoped enforcement over their operations, not pre-write semantic enforcement. The retained regenerated templates' validation effect is separate from transient post-effect warnings. See [MEM-BAP-retained-content](memory.md#mem-bap-retained-content), [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks), [MEM-RTE-config-refactor](memory.md#mem-rte-config-refactor) and [EPI-RTE-verify-check](epistemic.md#epi-rte-verify-check).

### Later consumption and trace routes

Requested task, note and search reads are pull. The independent SessionStart supply is push. The plugin's recent three-line headers and generated hook's titles are coarse selection of display parts, not delivery of scoped directive bodies. Lead-selected sibling titles have an actual same-batch identifier match; workers' later requested full-file reads are a different operation. See [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation), [MEM-RTE-generated-orientation](memory.md#mem-rte-generated-orientation), [RT-RTE-source-processing](runtime.md#rt-rte-source-processing) and [RT-RTE-parallel-claims](runtime.md#rt-rte-parallel-claims).

The trace-learning yes findings describe automatic trace-fed durable context/guidance, not exercised learning or accepted new knowledge. Session mining, phase findings and recommendation-history updates keep their local warrants. The missing transcript producer limits automatic loop closure without negating the independently specified mining transformation. Substantive human/model handoff alternatives cannot be silently discarded or automatically upgraded. Next history has a qualifying update/consumer chain, but its original source does not receive an invented controlled trace-source value. See [MEM-RTE-friction-retention](memory.md#mem-rte-friction-retention), [MEM-OBJ-task-files](memory.md#mem-obj-task-files), [MEM-OBJ-next-log](memory.md#mem-obj-next-log), [MEM-CLM-transcript-gap](memory.md#mem-clm-transcript-gap) and [MEM-OBJ-session-log](memory.md#mem-obj-session-log).

### Canonical records and unresolved conflict

Reconciliation supersedes EPI-OBJ-methodology-notes with [MEM-OBJ-methodology](memory.md#mem-obj-methodology), EPI-RTE-learn-import with [MEM-RTE-research-intake](memory.md#mem-rte-research-intake), EPI-RTE-remember-policy with [MEM-RTE-friction-retention](memory.md#mem-rte-friction-retention), and EPI-RTE-ask-consumption with [MEM-RTE-local-guidance](memory.md#mem-rte-local-guidance). These substitutions affect object, lineage, authority, admission and later-consumer citations without upgrading their evidence. Narrower epistemic inbox, claim-note and map records remain valid alongside broader memory containers.

The remaining reflection-status disagreement between [MEM-RTE-note-maintenance](memory.md#mem-rte-note-maintenance) and [EPI-RTE-reweave-revision](epistemic.md#epi-rte-reweave-revision) does not resolve or negate the separately supported memory values. This profile assigns no common reflection verdict. Copied/inherited deployment, same-count search freshness, exact provenance fields, alternate command bodies and stats-history production retain their limits rather than being recast as absences. See [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths), [MEM-RTE-research-intake](memory.md#mem-rte-research-intake), [MEM-RTE-note-maintenance](memory.md#mem-rte-note-maintenance) and [MEM-OBJ-health](memory.md#mem-obj-health).

### Repository-substrate correction

The claimed repository finding for skill replacement is withdrawn. [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade) supports copied previous versions and manual rollback, not Git storage of those copies. Only [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks) warrants the remaining wired repository finding. Directory archival does not add a separately supported repository basis.

### Source-read log

No frozen-source file was read for this classification. Only the supplied reports, reconciliation, boundary and governing invocation contracts were read. All classification warrants resolve in canonical accepted records; this member adds no evidence or declarations.
