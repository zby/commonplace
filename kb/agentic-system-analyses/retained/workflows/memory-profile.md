---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Claude Code dynamic workflows memory comparison: saved outputs, reusable orchestration, populated prefixes and use-changed controls at the workflows-2026-10-14 capture."
run-id: "AAS-2026-10-14-workflows-f9c2f80a3a94-01"
source-identity: "https://code.claude.com/docs/en/workflows"
reviewed-boundary: "workflows-2026-10-14"
memory-comparison:
  version: 2
  scope: "Use-accumulated run/reusable workflow scripts and their embedded tasks/criteria, saved worker results including research claims, populated prompt-prefix caches, use-changed consent/guidelines/opt-in settings, and their admission, maintenance and later-consumer paths. Includes unresolved worker-context, usage-wait checkpoint and progress/tool-trace retention alternatives named in accepted records. Excludes shipped static bundled/plugin instructions as such, ordinary same-run variables and current-output filtering as such, general external project-file versioning, provider model parameters/training and general host compaction not established within the workflow capture. Plugin copies of task-generated or revised reusable scripts remain included; their admission details are unresolved."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Run and saved project/personal/plugin script artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-rte-script-admission"
              note: "Session and reusable script copies are retained files."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-rte-script-admission"
          note: "Documented .js file locations classify the operative artifact, not every loader implementation."
        - scope: "Locally retained agent results"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-run-replay"
              note: "Completed outputs are saved in the local session directory for replay."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
          note: "The record names local session-directory storage; serialization is separate."
        - scope: "Cloud retained results"
          assessment: "known"
          findings:
            - value: "service-object"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-run-replay"
              note: "Cloud session conversation history retains completed results across VM reclamation."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
          note: "The documented conversation-history service object is classified without claiming its physical backing store."
        - scope: "Populated prompt-prefix cache"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "Opaque provider/request-cache infrastructure does not identify a controlled physical or logical storage substrate; no vector, kv or model-weights value is inferred."
        - scope: "Use-changed consent, guideline and opt-in settings"
          assessment: "partial"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
              note: "Persisted user settings include user-choice controls."
            - value: "in-memory"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
              note: "Session-only ultracode configuration is session state, separate from persistent settings."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "User settings files and session state are described; exact named-consent and managed administrative backing remain unknown."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Storage cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-rte-script-admission"
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "The documented inventory includes run/reusable scripts, saved results, populated prefixes and use-changed settings. Files and cloud service objects are supported; provider cache infrastructure, administrative consent storage and alternative checkpoints remain unresolved."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Retained script control flow, literal metadata and embedded output constraints at runtime/loader/validator consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "epistemic.md#epi-obj-output-schema"
                - "epistemic.md#epi-rte-schema-check"
              note: "JavaScript and schema rules determine execution and structural checking."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "epistemic.md#epi-obj-output-schema"
            - "epistemic.md#epi-rte-schema-check"
          note: "These localized rules have symbolic consumers."
        - scope: "Retained script task prompts at worker-model consumer"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-bap-agent-prompts"
              note: "Embedded prompts provide model-interpreted task guidance."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-bap-agent-prompts"
          note: "Interpreted task meaning is not made symbolic by JavaScript serialization."
        - scope: "Saved worker-result prose and research propositions at reader/model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "epistemic.md#epi-obj-research-claims"
              note: "Prose findings and cited claims are interpreted content."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "epistemic.md#epi-obj-research-claims"
          note: "This unit covers the readable prose part, not all result encoding."
        - scope: "Saved structured worker values at script consumer"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-agent-orchestration"
              note: "Returned structured fields become JavaScript values for branching and input construction."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-agent-orchestration"
          note: "Schema-shaped JSON and filenames are consumed by fixed script operations; semantic truth remains separate."
        - scope: "Prefix tool interfaces and system instructions as supplied to later matching requests"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
              note: "Tool definitions supply structured interfaces."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
              note: "System-prompt text supplies interpreted guidance."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "Delivered prefix parts have distinct forms; this does not classify cache encoding."
        - scope: "Opaque stored prefix encoding"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "No record establishes whether the provider retains text, numerical representations or another form."
        - scope: "Use-changed settings at launch and authoring consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Scoped consent and opt-in/disable keys govern fixed control decisions."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-clm-runtime-limits"
              note: "A retained size guideline reaches foreground Claude as advice."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
            - "runtime.md#rt-clm-runtime-limits"
          note: "Control keys and interpreted size advice are separate consumption paths."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Representational form cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "epistemic.md#epi-obj-output-schema"
        - "epistemic.md#epi-rte-schema-check"
        - "runtime.md#rt-bap-agent-prompts"
        - "runtime.md#rt-obj-agent-results"
        - "epistemic.md#epi-obj-research-claims"
        - "runtime.md#rt-rte-agent-orchestration"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-clm-runtime-limits"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Readable code, task text, result content and control state are classified separately. Cache encoding, progress payloads and checkpoint alternatives prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        - scope: "Task-generated scripts and human/Claude revisions"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-rte-script-admission"
              note: "Claude writes task-specific orchestration; users or Claude author revisions."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-rte-script-admission"
          note: "Foreground model authorship and separately described human/model edits establish an authored path."
        - scope: "Worker-produced results including research content"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-agent-orchestration"
              note: "Workers generate task answers."
            - value: "imported"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-research-claims"
                - "epistemic.md#epi-rte-research-acquisition"
              note: "External source material enters research and supplies cited report content; this does not make every final proposition imported verbatim."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "epistemic.md#epi-obj-research-claims"
            - "epistemic.md#epi-rte-research-acquisition"
          note: "Model-backed task products and external acquisition are documented; every initial input and semantic derivation is not identified."
        - scope: "Populated tools/system prefix"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
                - "memory.md#mem-rte-prefix-reuse"
              note: "The reusable prefix is assembled from matching request configuration rather than extracted task findings."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "Matching requests build a reusable prefix, but provenance of all tool/system content and provider representation is unresolved."
        - scope: "Human-chosen retained consent and settings"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Retained control choices and authoring preferences are explicitly supplied."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "The records name human or organizational choices, not extraction of experience."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Lineage cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-rte-script-admission"
        - "runtime.md#rt-obj-agent-results"
        - "epistemic.md#epi-obj-research-claims"
        - "epistemic.md#epi-rte-research-acquisition"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Known authorship and processing derivation do not resolve all initial sources, prefix provenance or opaque checkpoint paths. No trace-extracted origin is inferred merely from task execution."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Retained script control flow at workflow runtime"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-bap-script-control"
              note: "Symbolic orchestration selects subsequent operations and inputs."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-bap-script-control"
          note: "The script selects workers, branches and returned values."
        - scope: "Embedded retained task text at worker model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-bap-agent-prompts"
              note: "Saved task guidance directs future worker invocations."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-bap-agent-prompts"
          note: "Prompt delivery supplies task directions, not guaranteed compliance."
        - scope: "Retained script schema criteria at validator/runtime admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-output-schema"
                - "epistemic.md#epi-rte-schema-check"
              note: "Schema constraints determine whether outputs conform."
            - value: "enforcement"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-output-schema"
                - "epistemic.md#epi-rte-schema-disposition"
              note: "The consumed criterion can block contradictory calls or reject persistently invalid outputs."
          records:
            - "epistemic.md#epi-obj-output-schema"
            - "epistemic.md#epi-rte-schema-check"
            - "epistemic.md#epi-rte-schema-disposition"
          note: "Only embedded reusable criteria are included; ephemeral schema state is excluded."
        - scope: "Saved result content at replayed script and downstream reader"
          assessment: "partial"
          findings:
            - value: "routing"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-run-replay"
                - "runtime.md#rt-rte-agent-orchestration"
              note: "Replayed structured values can select later calls and their inputs."
            - value: "knowledge"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-agent-results"
                - "epistemic.md#epi-obj-research-claims"
              note: "Readable findings and cited research content supply task context or reference rather than standing directions."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
            - "epistemic.md#epi-obj-research-claims"
          note: "The documented generic and example consumers establish routing/context; arbitrary saved/plugin consumer effects are not enumerated."
        - scope: "Replay compatibility state at result tracker"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-run-replay"
              note: "Retained run state selects reused prefix versus rerun suffix."
          records:
            - "runtime.md#rt-rte-run-replay"
          note: "Prior start order, completion/failure and prompt matching determine which saved values remain reusable."
        - scope: "Cached delivered tools/system prefix at matching worker"
          assessment: "partial"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
                - "memory.md#mem-rte-prefix-reuse"
              note: "Reused system-prompt instructions reach a later matching worker request."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "System guidance is established; complete tool definitions and provider payload effects are not exposed."
        - scope: "Retained consent/disable/opt-in control at launch evaluator"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Retained consent and disabling controls permit or suppress launches within their documented routes."
            - value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Opt-in state changes selection of workflow execution."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "Controls govern workflow permission and launch surfaces, not factual acceptance."
        - scope: "Retained size guideline at foreground script author"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-clm-runtime-limits"
              note: "The guideline tells Claude the target scale for future authored workflows."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-clm-runtime-limits"
          note: "Advice remains advisory even when persisted."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Behavioral authority cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-bap-script-control"
        - "runtime.md#rt-bap-agent-prompts"
        - "epistemic.md#epi-obj-output-schema"
        - "epistemic.md#epi-rte-schema-check"
        - "epistemic.md#epi-rte-schema-disposition"
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "epistemic.md#epi-obj-research-claims"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-clm-runtime-limits"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Authority is assigned at actual retained-part consumers. Opaque cache representation, worker context and administrative details prevent an exhaustive authority union; no learning or ranking force follows merely from retention."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Runtime persistence of generated run script and completed worker outputs"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-obj-agent-results"
                - "runtime.md#rt-rte-run-replay"
              note: "Runtime stores run artifacts and tracks completed outputs without per-item human admission."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
          note: "Starting or approving execution is not approval of each retained content item."
        - scope: "Operator save and direct human edits of reusable scripts"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-script-admission"
              note: "Explicit operator decisions admit or replace reusable content."
          records:
            - "runtime.md#rt-rte-script-admission"
          note: "A human selects the run/location to save or supplies edited content."
        - scope: "Claude-authored requested script edits"
          assessment: "partial"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-script-admission"
              note: "Claude can supply revisions without a documented separate per-content approval gate."
          records:
            - "runtime.md#rt-rte-script-admission"
          note: "Requesting edits alone does not document human approval of each resulting content revision; direct-file edit control is not fully specified."
        - scope: "Prefix cache population"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
                - "memory.md#mem-rte-prefix-reuse"
              note: "Software/provider admission populates matching request prefixes."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "Settings controlling TTL do not supply individual cached content."
        - scope: "Explicit human consent and preference/configuration choices"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Yes approval and user-chosen settings explicitly admit retained control content."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "This unit covers specified operator choices rather than every administrative pathway."
        - scope: "Plugin installation/admission and administrative settings backing"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-script-admission"
            - "memory.md#mem-obj-workflow-settings"
          note: "Separate installation and administrative admission details are outside the recorded contract; generic tooling identity does not resolve content control."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Write agency cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "runtime.md#rt-rte-script-admission"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Admission mechanisms are separated from authorship and I/O. Positive manual and automatic routes are supported, but plugin admission, managed configuration and alternative checkpoints are unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Replay validity maintenance over saved worker outputs"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-run-replay"
              note: "First failed or changed-prompt slot invalidates its saved suffix, including completed later agents."
          records:
            - "runtime.md#rt-rte-run-replay"
          note: "The validity decision withdraws reuse, without establishing physical deletion."
        - scope: "Human/Claude revision of saved orchestration"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-script-admission"
              note: "Edits replace saved script content used in later invocations."
          records:
            - "runtime.md#rt-rte-script-admission"
          note: "Editing revises an existing retained entry; improvement and automatic experience extraction are not implied."
        - scope: "Prompt cache expiry"
          assessment: "partial"
          findings:
            - value: "decay"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
                - "memory.md#mem-rte-prefix-reuse"
              note: "TTL ends availability of cached prefix content for subsequent reuse."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "A five-minute or one-hour lifetime bounds reuse; additional eviction operations and physical cleanup are unspecified."
        - scope: "Worker-result and research-report semantic transformations over retained memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-agent-results"
            - "epistemic.md#epi-obj-research-claims"
            - "epistemic.md#epi-rte-report-disposition"
            - "epistemic.md#epi-rte-result-filter"
          note: "Report filtering and current-array truthiness selection act on task output, not a demonstrated maintenance operation over retained memory. No consolidate, dedup or synthesize finding follows from the route names or claimed report synthesis."
        - scope: "Consent/settings maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "Choices persist, but complete replacement, revocation and retirement transformations are not specified."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Curation cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-rte-run-replay"
        - "runtime.md#rt-rte-script-admission"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "runtime.md#rt-obj-agent-results"
        - "epistemic.md#epi-obj-research-claims"
        - "epistemic.md#epi-rte-report-disposition"
        - "epistemic.md#epi-rte-result-filter"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Recorded logical invalidation and content revisions support positives at doctrine level. Cache TTL is a forgetting contract, not inspected eviction. Semantic transformations of retained outputs and alternative checkpoints remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Operator/Claude request for saved script invocation or run-file inspection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-workflow-script"
                - "runtime.md#rt-rte-script-admission"
              note: "Named invocation and explicit run-file inspection request retained material."
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-rte-script-admission"
          note: "The requested artifact is returned or loaded; command naming alone does not establish identifier-based push."
        - scope: "Replay request and automatic completed-prefix substitution"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-run-replay"
              note: "Human/Claude relaunch requests recovery of the retained run."
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
          note: "Completed-prefix selection and substitution fulfill the requested recovery of retained run results. The request need not name each value; automatic compatibility selection does not establish a separate push operation."
        - scope: "Automatic matching-prefix reuse on later worker request"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-prompt-cache"
                - "memory.md#mem-rte-prefix-reuse"
              note: "A matching later first request automatically reuses a sibling-populated tools/system prefix."
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "The worker initiates its task request; the cache selector supplies retained prefix processing without a request for sibling memory."
        - scope: "Persistent control and guideline supply to later launch/authoring"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
                - "runtime.md#rt-clm-runtime-limits"
              note: "Persisted scoped control choices and guideline advice reach later evaluators or foreground authoring."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
            - "runtime.md#rt-clm-runtime-limits"
          note: "Settings are automatically read in the documented launch/startup/next-prompt channels."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Read-back direction cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-rte-script-admission"
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-clm-runtime-limits"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Named loading, inspection and relaunch requests coexist with automatic selectors supplying retained parts. Full worker context and usage-wait reload routes remain unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Requested completed-result recovery during replay"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-run-replay"
            - "runtime.md#rt-obj-agent-results"
          note: "Replay is pull: prior order, prompt equality and failure state select reusable results within the requested recovery. Read-back signal classifies push selection, so it is inapplicable to this completely assessed requested-return unit, not to the whole partial axis."
        - scope: "Automatic prefix-cache reuse"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-prefix-reuse"
                - "memory.md#mem-obj-prompt-cache"
              note: "Configuration identity matching selects the delivered/reused tools/system prefix; hold timing and TTL are availability conditions, not semantic selectors."
          records:
            - "memory.md#mem-rte-prefix-reuse"
            - "memory.md#mem-obj-prompt-cache"
          note: "Trigger is a later matching worker first request or staggered fan-out release. Model, effort, agent type, tools, schema and working-directory identity select the cached prefix."
        - scope: "Named/project consent control delivery at launch"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
              note: "Workflow and project identity select the consent state used for that launch."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "Trigger is named launch evaluation. Workflow/project scope identities select applicable retained consent."
        - scope: "Global/user/session settings and next-prompt size advice"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-workflow-settings"
                - "runtime.md#rt-rte-workflow-launch"
                - "runtime.md#rt-clm-runtime-limits"
              note: "Configured scope and availability supply general control state or advice rather than content-targeted retrieval."
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
            - "runtime.md#rt-clm-runtime-limits"
          note: "Startup, launch or next-authoring prompt triggers availability of applicable global/session controls and guideline."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Push selection signal cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-rte-run-replay"
        - "runtime.md#rt-obj-agent-results"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-clm-runtime-limits"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-rte-agent-recovery"
      note: "Actual push selectors are classified independently of upstream requests. No embedding or semantic retrieval signal is supported; opaque checkpoint and inherited-context selectors remain unresolved."
    trace_learning:
      assessment: "not-determinable"
      units:
        - scope: "Automatic saved task-output production and replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
            - "runtime.md#rt-rte-agent-orchestration"
          note: "Durable outputs and a later script consumer are documented, but complete original inputs and a trace-fed behavior-shaping derivation are not established. Task products are not automatically traces or learned methods."
        - scope: "Generated/saved/revised workflow scripts"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-rte-script-admission"
          note: "Durable orchestration can affect later behavior; the records do not establish automatic extraction or revision from activity traces. Human-selected saves do not alone prove a bounded no."
        - scope: "Automatic populated prompt cache"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
          note: "Reuse of tools/system prefixes is not recorded extraction of experience; opaque provider population details prevent a bounded absence claim."
        - scope: "Use-changed consent and settings"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-workflow-settings"
            - "runtime.md#rt-rte-workflow-launch"
          note: "Explicit human choices are supported, not an automatic trace-fed update; complete alternative administrative updates are unresolved."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Qualifying trace learning cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "runtime.md#rt-rte-agent-orchestration"
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-rte-script-admission"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-workflow-launch"
        - "runtime.md#rt-rte-agent-recovery"
      note: "No accepted record establishes a qualifying automatic trace-fed durable behavior-shaping update and its later consumer, or a bounded absence across all included routes. Lack of demonstrated improvement is not the reason for withholding yes."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Potential saved-output trace-fed derivations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-agent-results"
            - "runtime.md#rt-rte-run-replay"
            - "runtime.md#rt-rte-agent-orchestration"
            - "epistemic.md#epi-obj-research-claims"
          note: "Original input inventory is incomplete and no qualifying write is established. Cloud conversation-history storage does not turn result provenance into session-logs; tools being used does not prove recorded tool-traces feed the update."
        - scope: "Potential script-revision trace inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-workflow-script"
            - "runtime.md#rt-rte-script-admission"
          note: "Task requests and editability do not establish consumption of session logs, tool traces or trajectories by an automatic durable update."
        - scope: "Potential prefix/settings trace inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-prompt-cache"
            - "memory.md#mem-rte-prefix-reuse"
            - "memory.md#mem-obj-workflow-settings"
          note: "Configuration-derived prefix reuse and human controls do not identify original trace content for a qualifying write."
        - scope: "Included worker context, usage-wait checkpoint and progress/tool-trace retention alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-orchestration"
            - "runtime.md#rt-rte-agent-recovery"
            - "runtime.md#rt-obj-agent-results"
          note: "The records do not establish the retained payload or later reload route for these alternatives; Trace origin cannot be completely classified. A partial tool-result display is not the consumed payload."
      records:
        - "runtime.md#rt-obj-agent-results"
        - "runtime.md#rt-rte-run-replay"
        - "runtime.md#rt-rte-agent-orchestration"
        - "epistemic.md#epi-obj-research-claims"
        - "runtime.md#rt-obj-workflow-script"
        - "runtime.md#rt-rte-script-admission"
        - "memory.md#mem-obj-prompt-cache"
        - "memory.md#mem-rte-prefix-reuse"
        - "memory.md#mem-obj-workflow-settings"
        - "runtime.md#rt-rte-agent-recovery"
      note: "A completely assessed absence of qualifying trace learning is not established, so this axis cannot be inapplicable. Task tools, conversation storage and displayed calls do not by themselves establish trace inputs to a qualifying update."
---

# Claude Code dynamic workflows memory profile

## Comparison rationale

All positive findings have a claimed basis. The accepted records derive from doctrine/design in the frozen documentation capture, not inspected implementation, execution or causal evidence; see [RT-RTE-run-replay](runtime.md#rt-rte-run-replay) and [MEM-RTE-prefix-reuse](memory.md#mem-rte-prefix-reuse). Complete classification of a narrow documented unit does not upgrade its evidence strength. The axis notes retain unresolved included alternatives rather than using one documented route as a complete system inventory.

Reconciliation supplies no supersessions. The runtime result container and its research-claim part remain separately usable, as do script control and embedded task guidance. Cache prefixes are not worker-result memory. Their identity and configuration matching do not establish semantic relevance, shared findings or provider parameter learning. The scope includes settings only where choices persist or change through use, not the entirety of shipped configuration.

Read-back distinguishes requested returns from independent automatic supply. A named script requested by the consumer is pull; a filename alone does not justify identifier push. Relaunch likewise requests recovery of retained run results. Selection and substitution of the compatible completed prefix fulfill that request, without requiring a separate request for each value. Order, prompt equality and failure state govern reuse but establish neither another push operation nor a replay push-signal finding. Cache and scoped-control supply independently retain their push and matching-signal classifications. Availability, TTL and hold budgets do not become semantic selection signals. These distinctions rest on [RT-RTE-run-replay](runtime.md#rt-rte-run-replay), [MEM-RTE-prefix-reuse](memory.md#mem-rte-prefix-reuse) and [MEM-OBJ-workflow-settings](memory.md#mem-obj-workflow-settings).

Logical suffix invalidation, script revision and prefix expiry are distinct curation routes. None proves consolidation, synthesis of a novel retained claim or improved future capacity. Research-report synthesis is a source-native label, not evidence that its propositions are absent from its inputs. Current-result truthiness filtering is not, by itself, maintenance over retained memory; see [EPI-RTE-result-filter](epistemic.md#epi-rte-result-filter) and [EPI-RTE-report-disposition](epistemic.md#epi-rte-report-disposition).

No positive trace-learning classification is supported by the accepted records. No local or system-wide no is asserted either: the members declare no bounded absence record, original worker input coverage is incomplete, and usage-wait checkpoints and raw tool/transcript retention remain unresolved. Automatic result persistence and later replay establish durable task-output reuse, not automatically a qualifying trace-fed derivation. If a later retained continuation summary were established, its trace-fed write and later consumer would need their own classification; transcript discard in one restart route cannot exclude that alternative. See [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results), [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery) and [RT-RTE-script-admission](runtime.md#rt-rte-script-admission).

Source-read log: no frozen source was read for this profile. All classifications use supplied accepted records and annotations. No evidence or record was added, and report verification was not reopened.
