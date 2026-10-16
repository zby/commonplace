---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Exocomp memory comparison: retained conversations, project records, local extensions and unresolved external stores at the frozen revision."
run-id: "AAS-2026-10-14-exocomp-692bb27c35f9-01"
source-identity: "https://github.com/cookiengineer/exocomp"
reviewed-boundary: "b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251"
memory-comparison:
  version: 2
  scope: "Included: accumulated planner/contractor message records and returned Inquire summaries; requirement Behavior and source-derived declaration/status views; bug descriptions/status and changelog descriptions/indexing metadata; project-local role templates/grants and skill bodies/dependencies/scripts with catalog, loaded-state and separate body-consumption routes; diagnostic snapshots; page/answer content retained in messages; recorded restore and operator-display routes. Unresolved included alternatives: initial project-content provenance/control, provider-private retention, arbitrary program-created memory, cross-restart loaded-skill bookkeeping and pending-wait reload. Excluded: static shipped role instructions/grants as standalone memory, unchanged external model weights, production binaries and arbitrary product files except source supplying requirement reconstruction, ordinary live-process/HTTP state with no later retained-memory consumer, external dependency implementations and generated frontend deployment behavior."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Planner and collected contractor messages"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "Recovery JSON retains the raw conversation."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "Agent.Messages holds accumulated records for later consumers."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
          note: "Agent arrays and recovery JSON retain the recorded messages."
        -
          scope: "Inquire retained tool-result summary"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "The summary can be serialized with caller messages."
            -
              value: "in-memory"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "The admitted summary remains in caller message state."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
          note: "If invoked through Session, the returned summary enters messages and can survive backup."
        -
          scope: "Requirement behavior and declaration/status view"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-rte-requirement-update"
              note: "Pending specifications and source-derived declarations use project files."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-rte-requirement-update"
              note: "The merged Requirements.contents map supplies tool/UI consumers."
          records:
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-obj-requirement-declaration"
            - "memory.md#mem-rte-requirement-update"
          note: "Pending JSON and source files back the freshly merged map; implemented true status is regenerated rather than archived."
        -
          scope: "Bug description, identity/fixed status and changelog entries"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Project JSON persists reports and change events."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Tool maps retain content and selection metadata."
          records:
            - "memory.md#mem-obj-bug-description"
            - "memory.md#mem-obj-bug-status"
            - "memory.md#mem-obj-changelog-entry"
            - "memory.md#mem-rte-project-records"
          note: "Each report part is stored in project JSON and a tool map."
        -
          scope: "Project-local role templates"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "Role YAML is the persistent source."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "Registered templates survive for later same-process lookup."
          records:
            - "memory.md#mem-rte-role-discovery"
          note: "Project YAML is reread at construction and registered in the process map."
        -
          scope: "Skill bodies/dependencies/scripts, catalogs and loaded objects"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "SKILL.md and Go scripts remain on disk."
            -
              value: "in-memory"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Catalog, loaded objects and separately inserted message bodies retain operative parts."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Grant-dependent skill capacity has separate file/catalog/loaded/body parts; no default activation is inferred."
        -
          scope: "Diagnostic request/response snapshots"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-debug-snapshot"
              note: "Fixed-name snapshot files retain raw request/response material."
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "The diagnostic boundary is filesystem JSON; no automatic inference consumer is established."
        -
          scope: "Cross-restart loaded-skill bookkeeping"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-loading"
            - "memory.md#mem-rte-session-recovery"
          note: "Message-body recovery does not establish persistence or reload of loaded_skills; its cross-restart substrate is not determinable."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes their storage substrate. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-obj-agent-messages"
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-obj-requirement-declaration"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-obj-bug-description"
        - "memory.md#mem-obj-bug-status"
        - "memory.md#mem-obj-changelog-entry"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "The records inventory filesystem/in-process retained surfaces and their readers. Provider-private retention, arbitrary program stores and restored extension bookkeeping prevent complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Conversation/report prose and answer prose retained in messages, excluding format-selected page payloads"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "epistemic.md#epi-rte-human-answers"
                - "epistemic.md#epi-rte-website-fetch"
                - "memory.md#mem-bap-retained-content"
              note: "Retained conversation and tool-result prose provides interpreted context."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "epistemic.md#epi-rte-human-answers"
            - "epistemic.md#epi-rte-website-fetch"
            - "memory.md#mem-bap-retained-content"
          note: "This unit covers conversational/report and answer prose, not page-format alternatives or message routing fields."
        -
          scope: "Natural-language page text retained in Session messages and supplied as later context"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-website-content"
                - "epistemic.md#epi-rte-website-fetch"
              note: "The page-text alternative supplies natural-language content for model interpretation."
          records:
            - "epistemic.md#epi-obj-website-content"
            - "epistemic.md#epi-rte-website-fetch"
          note: "The accepted object record distinguishes page text from format-selected HTML/Markdown serialization. This unit includes only the page-text part; serialization is classified separately. Retention does not establish extraction fidelity."
        -
          scope: "Symbolic HTML/Markdown page serialization retained in Session messages and supplied as later context"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-website-content"
                - "epistemic.md#epi-rte-website-fetch"
              note: "The accepted object record identifies format-selected HTML/Markdown serialization as symbolic material."
          records:
            - "epistemic.md#epi-obj-website-content"
            - "epistemic.md#epi-rte-website-fetch"
          note: "This unit covers the serialization part of the returned page payload, independently of the page's natural-language text. Fetch retains the format-selected conversion in tool messages eligible for later backup/restore; this is not a claim of factual validation or complete parser inspection."
        -
          scope: "Inquire returned summary prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
              note: "The summary is model-produced prose supplied for interpretation."
          records:
            - "runtime.md#rt-rte-agent-inquire"
          note: "A requested condensation result can be retained and interpreted as later caller context."
        -
          scope: "Message roles, tool calls, IDs and tool-name fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "Localized message roles and tool structures have fixed dispatch/report-selection rules."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
          note: "Envelope fields remain separate from prose; complete private model reasoning is unavailable."
        -
          scope: "Requirement Behavior, bug Description and changelog Description"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-changelog-entry"
              note: "Models and operators interpret specifications and reported events/defects."
          records:
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-obj-bug-description"
            - "memory.md#mem-obj-changelog-entry"
          note: "These prose parts are not the source declaration, status flag or duplicate key."
        -
          scope: "Requirement declaration/status, bug identity/status and changelog indexing metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-obj-changelog-entry"
              note: "Parsing, persistence filtering, visibility and exact duplicate/date rules consume these parts."
          records:
            - "memory.md#mem-obj-requirement-declaration"
            - "memory.md#mem-obj-bug-status"
            - "memory.md#mem-obj-changelog-entry"
          note: "Go syntax, booleans, keys, dates and event types have localized program consumers."
        -
          scope: "Project-local role prompt bodies"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "Local prompts supply interpreted guidance."
          records:
            - "memory.md#mem-rte-role-discovery"
          note: "Later same-process lookup exposes prompt prose; fresh-child execution remains limited."
        -
          scope: "Skill bodies at separate helper/bare-name consumer"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Injected body text supplies model-interpreted instructions."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Ordinary qualified Load does not deliver this body; the helper path is afforded."
        -
          scope: "Local role grants"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
                - "runtime.md#rt-obj-role-grants"
              note: "Grant arrays have fixed admission consumers."
          records:
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-obj-role-grants"
          note: "Registered grants participate in later same-process toolset construction."
        -
          scope: "Skill dependencies/script maps and Go scripts"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Dependency predicates and host program execution consume these parts."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Metadata and source have fixed check, selection and execution consumers rather than prose instruction force."
        -
          scope: "Diagnostic snapshots: envelopes and readable payloads"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-debug-snapshot"
              note: "Serialized request/response structures preserve localized fields."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-debug-snapshot"
              note: "Snapshots include textual request/response payloads."
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "The record distinguishes envelope from payload; neither establishes a numerical checkpoint."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes their operative form or consumption path. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-obj-agent-messages"
        - "epistemic.md#epi-rte-human-answers"
        - "epistemic.md#epi-rte-website-fetch"
        - "epistemic.md#epi-obj-website-content"
        - "memory.md#mem-bap-retained-content"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-rte-session-recovery"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-obj-bug-description"
        - "memory.md#mem-obj-changelog-entry"
        - "memory.md#mem-obj-requirement-declaration"
        - "memory.md#mem-obj-bug-status"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-obj-role-grants"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Text and fixed-rule structures are classified by operative consumption path, not by JSON encoding. Page text and symbolic HTML/Markdown serialization are separately included format-selected parts, not a uniformly natural-language payload. Opaque provider/program payloads remain unresolved; external model weights are not accumulated local memory."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Planner turn accumulation and parent collection of child stdout"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
              note: "Session turns and child stdout activity are captured as message records."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
          note: "This unit is the recording path, not model training or initial project authorship."
        -
          scope: "Inquire returned summary"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
              note: "Summary derivation extracts/condenses a recorded agent session."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-obj-agent-messages"
          note: "The derivation selects recorded child user/assistant prose; original transcript remains available."
        -
          scope: "Source-derived requirement declaration/status"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-rte-requirement-update"
              note: "AST extraction builds declaration/status views from project Go source."
          records:
            - "memory.md#mem-obj-requirement-declaration"
            - "memory.md#mem-rte-requirement-update"
          note: "Source scanning is not a trace-fed adaptation; behavior is empty in reconstructed entries."
        -
          scope: "Bug Add and explicit changelog description authoring"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Explicit report/event arguments provide authored description content."
          records:
            - "memory.md#mem-obj-bug-description"
            - "memory.md#mem-obj-changelog-entry"
            - "memory.md#mem-rte-project-records"
          note: "Authored describes explicit caller-supplied reports, not human versus model authorship; report admission is wired."
        -
          scope: "Direct-method requirement Behavior authoring"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-rte-requirement-update"
              note: "Direct definition supplies authored behavior content."
          records:
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-rte-requirement-update"
          note: "Ordinary Define* dispatch is blocked; direct methods accept caller-supplied prose."
        -
          scope: "Reload/import of project reports and local roles; page/answer acquisition into messages"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-recovery"
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-rte-project-records"
                - "memory.md#mem-rte-role-discovery"
                - "epistemic.md#epi-rte-website-fetch"
                - "epistemic.md#epi-rte-human-answers"
              note: "File parsing and external acquisition bring existing content into operative memory."
          records:
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-role-discovery"
            - "epistemic.md#epi-rte-website-fetch"
            - "epistemic.md#epi-rte-human-answers"
          note: "Import does not authenticate initial authorship or source warrant."
        -
          scope: "Skill catalog import and requested adoption"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Discovery imports local skill files and later requests adopt their content."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Original file authorship is unknown; catalog/loaded/helper acquisition paths are afforded."
        -
          scope: "Diagnostic snapshots"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-debug-snapshot"
              note: "Snapshots record inference request/response activity."
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "Raw adapter-stage request/response capture has a known recording path, not evaluated derivation."
        -
          scope: "Initial report/source/role/skill content and initial recovered transcript provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-obj-requirement-declaration"
            - "memory.md#mem-obj-bug-description"
            - "memory.md#mem-obj-changelog-entry"
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-rte-skill-loading"
            - "memory.md#mem-rte-session-recovery"
          note: "Records explicitly leave arbitrary project authorship/provenance unresolved; known reload and derivation do not determine initial origins."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes initial or internal derivation provenance. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-obj-agent-messages"
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-obj-requirement-declaration"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-obj-bug-description"
        - "memory.md#mem-obj-changelog-entry"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-rte-role-discovery"
        - "epistemic.md#epi-rte-website-fetch"
        - "epistemic.md#epi-rte-human-answers"
        - "runtime.md#rt-rte-skill-loading"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Known recording/import/derivation paths coexist with unknown initial authorship. A restored record does not establish how its initial content was written; all such alternatives stay included."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Recovered conversation and requested project reports/page/answer content at later model or operator"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-retained-content"
                - "memory.md#mem-rte-session-recovery"
                - "memory.md#mem-rte-project-records"
                - "memory.md#mem-rte-operator-display"
                - "epistemic.md#epi-rte-website-fetch"
                - "epistemic.md#epi-rte-human-answers"
              note: "Later inference and human inspection receive retained conversational/report content as context."
          records:
            - "memory.md#mem-bap-retained-content"
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-operator-display"
            - "epistemic.md#epi-rte-website-fetch"
            - "epistemic.md#epi-rte-human-answers"
          note: "Content is reference/context/advice; delivered answers do not certify truth or approval."
        -
          scope: "Surviving requirement Behavior at model/UI readers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-rte-requirement-update"
                - "epistemic.md#epi-obj-specification"
              note: "Surviving behavior specifies intended task behavior for model interpretation."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-rte-requirement-update"
                - "epistemic.md#epi-obj-specification"
              note: "The same retained specification is reference material for requested inspection."
          records:
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-rte-requirement-update"
            - "epistemic.md#epi-obj-specification"
          note: "Behavior describes requested policy, while declarations/status describe source structure; ordinary new Define* admission is not wired."
        -
          scope: "Recovered system-role content and local role prompt at same-process template/model consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
                - "memory.md#mem-rte-role-discovery"
                - "runtime.md#rt-bap-role-prompt"
              note: "Standing prompt content supplies model-interpreted directions."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-bap-role-prompt"
          note: "Recovered system content retains instruction priority; local registration reaches later same-process lookup, not established fresh-child execution."
        -
          scope: "Skill body at separate helper/bare-name insertion consumer"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Inserted skill body supplies standing directions to later model requests."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Only this alternative supplies the body at system priority; qualified Load delivers a generic notice."
        -
          scope: "Child prose at Inquire update and returned summary at caller"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "epistemic.md#epi-rte-inquire-projection"
              note: "Recorded child prose feeds production of a durable behavior-shaping context artifact."
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "epistemic.md#epi-rte-inquire-projection"
              note: "Returned summary supplies advisory context on later caller inference."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-obj-agent-messages"
            - "epistemic.md#epi-rte-inquire-projection"
          note: "Automatic retained summary production uses recorded experience; this authority is distinct from demonstrated improved capacity."
        -
          scope: "Bug fixed-status at List/Search filter"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-rte-project-records"
                - "epistemic.md#epi-rte-bug-closure"
              note: "IsFixed applies an enforced visibility veto at tool readers."
          records:
            - "memory.md#mem-obj-bug-status"
            - "memory.md#mem-rte-project-records"
            - "epistemic.md#epi-rte-bug-closure"
          note: "The flag excludes descriptions from model tool lists but not whole-map operator JSON."
        -
          scope: "Requirement IsImplemented at pending writer and source-first file/symbol keys at merge"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-rte-requirement-update"
                - "epistemic.md#epi-rte-requirement-refresh"
              note: "True status excludes entries from JSON and occupied source keys refuse same-key saved Behavior."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-requirement-declaration"
                - "memory.md#mem-rte-requirement-update"
                - "epistemic.md#epi-rte-requirement-refresh"
              note: "File/symbol identity determines the merge destination and which source/saved part supplies a view."
          records:
            - "memory.md#mem-obj-requirement-declaration"
            - "memory.md#mem-rte-requirement-update"
            - "epistemic.md#epi-rte-requirement-refresh"
          note: "Consumed status and keys enforce omission/precedence; they do not validate required behavior."
        -
          scope: "Changelog retained description/type/file/symbol at duplicate admission and Date at List ordering"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Existing tuple content determines whether a proposed event duplicates a retained entry."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "An equal tuple vetoes duplicate admission."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Retained dates order changelog descriptions for List consumption."
          records:
            - "memory.md#mem-obj-changelog-entry"
            - "memory.md#mem-rte-project-records"
          note: "Duplicate metadata is an admission criterion; retained dates determine relative display order."
        -
          scope: "Admitted local-role grants at toolset and HasMethod consumer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
                - "runtime.md#rt-obj-role-grants"
              note: "Retained grant arrays participate in permitting/refusing tool or program effects."
          records:
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-obj-role-grants"
          note: "Only later same-process Agent/tool construction is established for registered templates; fresh-child role execution is not inferred."
        -
          scope: "Loaded skill dependency/script state at Load and Execute consumers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Dependency metadata supplies compatibility criteria for loaded-state admission."
            -
              value: "enforcement"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Checks and loaded membership permit/refuse skill admission and script execution."
            -
              value: "routing"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Loaded script identity selects the executable content for Execute."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Dependencies admit loaded-state changes; loaded-name/script/runtime checks govern execution independently of body injection."
        -
          scope: "Diagnostic snapshots at any future automatic model consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "Storage is recorded but no automatic next-inference consumer is established; therefore no authority at such a consumer is determinable."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes later consumers and behavioral effects. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-bap-retained-content"
        - "memory.md#mem-rte-session-recovery"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-operator-display"
        - "epistemic.md#epi-rte-website-fetch"
        - "epistemic.md#epi-rte-human-answers"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-rte-requirement-update"
        - "epistemic.md#epi-obj-specification"
        - "memory.md#mem-obj-agent-messages"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-bap-role-prompt"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-agent-inquire"
        - "epistemic.md#epi-rte-inquire-projection"
        - "memory.md#mem-obj-bug-status"
        - "epistemic.md#epi-rte-bug-closure"
        - "memory.md#mem-obj-requirement-declaration"
        - "epistemic.md#epi-rte-requirement-refresh"
        - "memory.md#mem-obj-changelog-entry"
        - "runtime.md#rt-obj-role-grants"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Authorities attach to consumed parts and effects. Known local routes do not establish compliant models, correct reports, successful persistence or forces inside opaque stores."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Turn/child-output recording, backup and recovery-content admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
                - "epistemic.md#epi-rte-human-answers"
                - "epistemic.md#epi-rte-website-fetch"
              note: "Software message admission and serialization/parsing decide retained-content entry."
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
            - "epistemic.md#epi-rte-human-answers"
            - "epistemic.md#epi-rte-website-fetch"
          note: "Runtime records/imports content and parsing admits restored JSON without human per-turn approval."
        -
          scope: "Requirement source refresh, Signoff status and pending writer"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-obj-requirement-declaration"
              note: "Software extracts source and admits/omits entries after structural predicates."
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-obj-requirement-declaration"
          note: "Source-first reconstruction and filtering are software decisions, not human signoff."
        -
          scope: "Direct-method requirement definition admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-obj-requirement-behavior"
              note: "Direct definition admits content by programmatic syntax/path/I/O checks."
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-obj-requirement-behavior"
          note: "Definition methods parse/admit supplied declaration/behavior without per-content human veto; generic caller identity does not prove manual content supply."
        -
          scope: "Model-proposed bug/changelog report maintenance"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-project-records"
                - "epistemic.md#epi-rte-bug-records"
                - "epistemic.md#epi-rte-changelog-records"
              note: "Model/software report admission and retirement are computational."
          records:
            - "memory.md#mem-rte-project-records"
            - "epistemic.md#epi-rte-bug-records"
            - "epistemic.md#epi-rte-changelog-records"
          note: "The model/tool route admits reports after software checks rather than human approval."
        -
          scope: "Explicit human supply/edit/approval on direct report API and initial project file writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-rte-skill-loading"
            - "runtime.md#rt-rte-client-tools"
          note: "Generic API caller identity and arbitrary file authorship do not identify per-content human control. No manual classification follows from starting the workflow."
        -
          scope: "Role discovery registration"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "Registration has no per-template human approval gate."
          records:
            - "memory.md#mem-rte-role-discovery"
          note: "Software parse/format/role checks admit a project file into the template map; upstream authorship is separate."
        -
          scope: "Skill catalog/loaded-object and helper-body admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Software decides catalog/loaded-object/body admission."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Catalog import, dependency gating and helper text checks admit material without human body approval; helper and qualified entry points remain separate."
        -
          scope: "Inquire derived summary admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
              note: "Model condensation and process/parse success admit the retained tool-result summary."
          records:
            - "runtime.md#rt-rte-agent-inquire"
          note: "Caller chooses a child but program/model produce and parse the summary without human content approval."
        -
          scope: "Debug snapshot replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-debug-snapshot"
              note: "Runtime writes the diagnostic payload without per-snapshot operator content approval."
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "Raw inference I/O is automatically marshaled at fixed filenames."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes write/admission control. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-obj-agent-messages"
        - "memory.md#mem-rte-session-recovery"
        - "epistemic.md#epi-rte-human-answers"
        - "epistemic.md#epi-rte-website-fetch"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-obj-requirement-declaration"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-rte-project-records"
        - "epistemic.md#epi-rte-bug-records"
        - "epistemic.md#epi-rte-changelog-records"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-client-tools"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Software admission is distinct from who authored content and from operator startup. No explicit per-content human decision is recorded for an additional manual finding; initial/external caller-controlled writes remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Inquire child prose to retained summary"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "epistemic.md#epi-rte-inquire-projection"
              note: "Selected recorded prose is compressed into a reduced summary for later context."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "epistemic.md#epi-rte-inquire-projection"
          note: "Factual condensation is implemented as an afforded model route; fidelity is unchecked. Projection loss does not establish synthesis."
        -
          scope: "Bug Add at existing key and Fix visibility withdrawal"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-rte-project-records"
              note: "Add revises an existing report description and status."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-bug-description"
                - "memory.md#mem-obj-bug-status"
                - "memory.md#mem-rte-project-records"
              note: "Fix withdraws tool-visible current reliance while preserving the report in JSON."
          records:
            - "memory.md#mem-obj-bug-description"
            - "memory.md#mem-obj-bug-status"
            - "memory.md#mem-rte-project-records"
          note: "Add changes the current report/reopens it; Fix preserves stored text while withholding tool-list delivery."
        -
          scope: "Changelog exact duplicate suppression"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-changelog-entry"
                - "memory.md#mem-rte-project-records"
              note: "Equal type/file/symbol/description tuples are suppressed."
          records:
            - "memory.md#mem-obj-changelog-entry"
            - "memory.md#mem-rte-project-records"
          note: "Comparison includes retained description and event tuple; Remove is append, not deletion."
        -
          scope: "Direct definition replacement at requirement key"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-obj-requirement-behavior"
              note: "Direct definition replaces the existing specification unit."
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-obj-requirement-behavior"
          note: "Only direct methods support this replacement; ordinary Define* dispatch is blocked."
        -
          scope: "Requirement source precedence and implemented-entry omission"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-obj-requirement-behavior"
                - "memory.md#mem-obj-requirement-declaration"
              note: "Source collisions discard authored Behavior from the operative view and pending serialization can make its loss durable."
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-obj-requirement-behavior"
            - "memory.md#mem-obj-requirement-declaration"
          note: "Authored intent can be forgotten without retained criticism or original rationale; this is not historical invalidation."
        -
          scope: "Qualified skill Unload and helper matching-body removal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Unload withdraws the loaded object; the separate helper withdraws matching instruction content."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Loaded-script reliance or matching instruction reliance is withdrawn while disk content remains; differing historical bodies and prior effects can survive."
        -
          scope: "Role refresh/backup/debug maintenance beyond the recorded import and overwrite operations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-role-discovery"
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-obj-debug-snapshot"
          note: "These records establish registration/raw retention, not any further controlled curation transformation; no bounded absence record supports a negative."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes maintenance transformations. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "runtime.md#rt-rte-agent-inquire"
        - "epistemic.md#epi-rte-inquire-projection"
        - "memory.md#mem-obj-bug-description"
        - "memory.md#mem-obj-bug-status"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-obj-changelog-entry"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-obj-requirement-behavior"
        - "memory.md#mem-obj-requirement-declaration"
        - "runtime.md#rt-rte-skill-loading"
        - "memory.md#mem-rte-role-discovery"
        - "memory.md#mem-rte-session-recovery"
        - "memory.md#mem-obj-debug-snapshot"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Positive transformations are local: summary consolidation, report revision/dedup/withdrawal and content loss. Catalog rebuild, acquisition and ordinary checkpoint overwrite alone are not curation. Opaque maintenance prevents completeness."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Restored planner checkpoint selection and subsequent full-message supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-recovery"
                - "runtime.md#rt-rte-planner-chat"
              note: "Recovery and later inference supply accumulated planner messages wholesale."
          records:
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-planner-chat"
          note: "Startup/inference automatically supplies the selected backup without a request for individual retained turns."
        -
          scope: "Await report, project List/Search and operator GET"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-contractor-work"
                - "memory.md#mem-rte-project-records"
                - "memory.md#mem-rte-requirement-update"
                - "memory.md#mem-rte-operator-display"
              note: "Named/inventory/search/display requests retrieve recorded reports and specifications."
          records:
            - "runtime.md#rt-rte-contractor-work"
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-rte-operator-display"
          note: "Consumer calls request retained material; return is fulfillment, not a second push."
        -
          scope: "Explicit Skills.List catalog request"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "List fulfills a caller request for discovered retained skill material."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "An explicit request refreshes and returns the catalog; grant-dependent capacity is not default activation."
        -
          scope: "Requested Inquire summary return"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
              note: "Inquire fulfills the caller request for reduced retained material."
          records:
            - "runtime.md#rt-rte-agent-inquire"
          note: "Caller explicitly requests a summary of a selected recorded agent; its return is not unsolicited proactive retrieval."
        -
          scope: "Project role file discovery and later same-process template lookup"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "Boot-time discovery supplies role replacements without requesting each retained file."
          records:
            - "memory.md#mem-rte-role-discovery"
          note: "Construction automatically imports matching local files and later lookup uses the registered template; this does not establish fresh-child execution."
        -
          scope: "Requested skill selection and helper instruction delivery"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Explicit named Load or helper request adopts selected retained skill material."
            -
              value: "push"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
              note: "Once separately injected and retained, a body is included wholesale in later inference messages."
          records:
            - "runtime.md#rt-rte-skill-loading"
          note: "Load/helper requests select a body/object; later inference automatically resupplies already inserted system bodies as part of accumulated messages."
        -
          scope: "Diagnostic snapshots at a later reader"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-debug-snapshot"
          note: "A storage capability and hypothetical reader do not establish a read-back route."
        -
          scope: "Restored loaded-skill objects and pending human-wait state"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
            - "epistemic.md#epi-rte-human-answers"
          note: "Recorded message recovery does not establish these coordination/tool-state reload routes."
        -
          scope: "Provider-private retention and arbitrary program-created memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-skill-loading"
          note: "Included opaque alternatives: no recorded inspection establishes later read-back direction. Inference and host execution are not evidence of their internal retained-memory mechanisms."
      records:
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-contractor-work"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-rte-operator-display"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-rte-role-discovery"
        - "memory.md#mem-obj-debug-snapshot"
        - "epistemic.md#epi-rte-human-answers"
        - "runtime.md#rt-rte-program-execution"
      note: "Requested delivery and automatic supply are separate operations even within one chain. Known pull routes cannot resolve provider/program consumers or cross-restart extension-state uncertainty."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Startup checkpoint and later accumulated-message supply"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-recovery"
                - "runtime.md#rt-rte-planner-chat"
              note: "Fixed checkpoint availability and wholesale delivery select an undifferentiated retained bundle."
          records:
            - "memory.md#mem-rte-session-recovery"
            - "runtime.md#rt-rte-planner-chat"
          note: "Trigger: terminal/web startup and later inference. Input: backup existence/parse success and full Agent.Messages. Selected part: the project checkpoint and all accumulated planner messages; no relevance or token ranking."
        -
          scope: "Project-local role replacement"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-role-discovery"
              note: "An actual role-key match chooses which retained template replaces the same-process role entry."
          records:
            - "memory.md#mem-rte-role-discovery"
          note: "Trigger: Agents construction. Input: parsed valid YAML Role and matching template key. Selected part: retained project role template admitted as that role replacement."
        -
          scope: "Later wholesale supply of separately injected skill system bodies"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-loading"
                - "memory.md#mem-rte-session-recovery"
              note: "Bodies travel in the accumulated bundle; caller-selected skill names at Load are not a push signal."
          records:
            - "runtime.md#rt-rte-skill-loading"
            - "memory.md#mem-rte-session-recovery"
          note: "Trigger: later inference. Input: already accumulated Agent.Messages, including separately inserted body. Selected part: whole message content, not a newly identity-matched skill recommendation."
        -
          scope: "Requested Await/Inquire, project List/Search, operator GET and explicit skill catalog/Load requests"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-contractor-work"
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-rte-operator-display"
            - "runtime.md#rt-rte-skill-loading"
          note: "These local operations fulfill consumer requests. Their agent/file/symbol/name and lexical display inputs are pull selectors, so no push signal applies to these operations."
        -
          scope: "Unestablished diagnostic, restored coordination/extension and opaque-provider/program consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-debug-snapshot"
            - "memory.md#mem-rte-session-recovery"
            - "epistemic.md#epi-rte-human-answers"
            - "runtime.md#rt-rte-skill-loading"
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
          note: "Missing later-consumer/selection mechanisms prevent determining whether any additional push exists and what it selects. Known requested routes cannot make these alternatives inapplicable."
      records:
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-rte-planner-chat"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-contractor-work"
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-rte-operator-display"
        - "memory.md#mem-obj-debug-snapshot"
        - "epistemic.md#epi-rte-human-answers"
        - "runtime.md#rt-rte-program-execution"
      note: "Signals classify automatic push selection only. Fixed checkpoint/wholesale message supply is coarse; role replacement uses an actual role match. Requested identifiers/searches and display filters are not inferred proactive selectors."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Inquire child-session summary retained through Session tool result/backup and later caller inference"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "memory.md#mem-rte-session-recovery"
                - "epistemic.md#epi-rte-inquire-projection"
              note: "Automatic trace-fed production of a retained behavior-shaping summary and later consumer is afforded."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
            - "epistemic.md#epi-rte-inquire-projection"
          note: "Recorded prose feeds automatic condensation, retained tool-message output supplies later context, and raw child transcript remains separately available. No embedded grant or observed invocation is established."
        -
          scope: "Raw turn/child transcript backup and diagnostic request/response snapshot copying"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-obj-debug-snapshot"
          note: "These particular writes retain raw activity without deriving a durable behavior-shaping artifact or learned parameters. No qualifying trace-learning transformation is established by raw retention alone."
        -
          scope: "Source-derived requirement reconstruction"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-requirement-update"
            - "memory.md#mem-obj-requirement-declaration"
          note: "Input is project source syntax, not activity/experience traces; automatic status/declaration refresh is not a qualifying trace-fed write."
        -
          scope: "Initial or external authoring of project reports, roles and skills; arbitrary program/provider updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-rte-skill-loading"
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
          note: "Reports and instruction files can be authored by external humans/programs/models, but the records do not trace their original inputs and transformations into a qualifying retained update. Provider-private changes and arbitrary stores remain uninspected."
      records:
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-obj-agent-messages"
        - "memory.md#mem-rte-session-recovery"
        - "epistemic.md#epi-rte-inquire-projection"
        - "memory.md#mem-obj-debug-snapshot"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-obj-requirement-declaration"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "The afforded Inquire chain qualifies by automatic trace-fed summary retention and later context consumption, not by measured improvement. Raw logs and source-fed refresh are separate; opaque updates and arbitrary authored stores prevent a system-wide negative or complete enumeration."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Inquire automatic summary production"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-agent-inquire"
                - "memory.md#mem-obj-agent-messages"
                - "epistemic.md#epi-rte-inquire-projection"
              note: "Recorded agent-session conversational turns feed the summary write."
          records:
            - "runtime.md#rt-rte-agent-inquire"
            - "memory.md#mem-obj-agent-messages"
            - "epistemic.md#epi-rte-inquire-projection"
          note: "Original input is recorded child conversational user/assistant Content. The projection excludes tool and system messages and tool-call structures."
        -
          scope: "Raw recording/backup/debug copies and source-fed requirement refresh"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-agent-messages"
            - "memory.md#mem-rte-session-recovery"
            - "memory.md#mem-obj-debug-snapshot"
            - "memory.md#mem-rte-requirement-update"
          note: "These named writes establish no qualifying derived trace-learning route; their raw traces/source files therefore do not add trace_source findings."
        -
          scope: "Potential externally authored report/role/skill learning and opaque provider/program updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-project-records"
            - "memory.md#mem-rte-role-discovery"
            - "runtime.md#rt-rte-skill-loading"
            - "runtime.md#rt-rte-planner-chat"
            - "runtime.md#rt-rte-program-execution"
            - "memory.md#mem-rte-session-recovery"
          note: "No recorded qualifying transformation with original input provenance resolves session/tool/event/trajectory alternatives. The known Inquire source cannot settle them."
      records:
        - "runtime.md#rt-rte-agent-inquire"
        - "memory.md#mem-obj-agent-messages"
        - "epistemic.md#epi-rte-inquire-projection"
        - "memory.md#mem-rte-session-recovery"
        - "memory.md#mem-obj-debug-snapshot"
        - "memory.md#mem-rte-requirement-update"
        - "memory.md#mem-rte-project-records"
        - "memory.md#mem-rte-role-discovery"
        - "runtime.md#rt-rte-skill-loading"
        - "runtime.md#rt-rte-planner-chat"
        - "runtime.md#rt-rte-program-execution"
      note: "Sources belong to each qualifying trace-fed write, not every retained log. Inquire has a recorded session source; omitted tool messages do not establish tool-traces for that write. Unknown external learning routes prevent complete trace-source coverage."
---

# Exocomp memory profile

## Comparison rationale

This profile classifies accepted records, not fresh source inspection. No source files were read for this job. The members supply implementation and doctrine/design evidence, with no current-revision observed operation or causal experiment used. Every axis remains partial because the recorded inventory includes opaque provider retention and arbitrary program-created stores, plus narrower unresolved mechanisms. Local known units state complete classification only for their named operative part and path; they do not claim an exhaustive system union.

Page payloads are not uniformly natural language. [EPI-OBJ-website-content](epistemic.md#epi-obj-website-content) distinguishes natural-language page text from symbolic HTML/Markdown serialization, and [EPI-RTE-website-fetch](epistemic.md#epi-rte-website-fetch) carries the format-selected result into messages eligible for later retention. The form inventory separates these parts from conversation/answer prose and includes both alternatives. This classification neither authenticates page claims nor resolves extraction fidelity.

Recovery supplies accumulated messages automatically, while Await, Inquire, project List/Search and operator GET fulfill requests. A caller-selected name or path is therefore not itself an identifier-based push. Role discovery is different: code matches parsed Role to a template key before replacement. Restored checkpoint and message-bundle supply are coarse. Body selection at explicit skill Load is pull; automatic subsequent supply of retained injected bodies is coarse message delivery. See [MEM-RTE-session-recovery](memory.md#mem-rte-session-recovery), [MEM-RTE-role-discovery](memory.md#mem-rte-role-discovery) and [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading).

The Inquire summary is an afforded automatic trace-fed durable context artifact: recorded conversational prose feeds a summarizer, whose return can enter a Session tool message, backup and later inference. This supports trace-learning yes and session-logs at that local basis even though the original transcript remains and no improvement is demonstrated. Its update consumer gives retained prose learning authority; the downstream summary gives knowledge authority. Projection omits tool/system messages, so it does not establish tool-traces as a source for that qualifying write. Model condensation is consolidation, not evidenced synthesis; uncertain semantic fidelity neither removes consolidation nor proves new claims. See [RT-RTE-agent-inquire](runtime.md#rt-rte-agent-inquire), [EPI-RTE-inquire-projection](epistemic.md#epi-rte-inquire-projection) and [MEM-OBJ-agent-messages](memory.md#mem-obj-agent-messages). Raw checkpoint/snapshot copying alone does not qualify. No local trace-learning no finding is asserted without bounded absence evidence.

Content and control parts have different forces. Bug prose gives context; the fixed flag enforces tool-list exclusion without erasing JSON. Changelog descriptions and tuple metadata veto duplicates; dates affect relative order. Requirement status enforces omission from pending JSON, and source-first identity matching can discard authored Behavior. That forgetting supports decay rather than history-preserving invalidation. A reconstructed declaration is compiled from source, not extracted from an activity trace. Surviving Behavior supplies task directions and reference material, but the ordinary new Define* tool route is obstructed; direct definition replacement remains afforded. See [MEM-RTE-project-records](memory.md#mem-rte-project-records), [MEM-OBJ-changelog-entry](memory.md#mem-obj-changelog-entry) and [MEM-RTE-requirement-update](memory.md#mem-rte-requirement-update).

Local role registration affects later same-process lookup and does not establish which prompt/grants a fresh child executes. Skill catalog refresh, loaded-object adoption and system-body insertion are separate routes. Qualified Load/Unload changes loaded state and generic notices; only helpers or bare-name API use afford body insertion/removal. Removal can leave older differing bodies and never rolls back script effects. Cross-restart message-body retention cannot resolve loaded-state recovery. These distinctions prevent upgrading afforded instruction/extension routes to default wiring. See [MEM-RTE-role-discovery](memory.md#mem-rte-role-discovery), [RT-RTE-skill-loading](runtime.md#rt-rte-skill-loading) and [RT-ABS-skill-grants](runtime.md#rt-abs-skill-grants).

Software admission is automatic even when a human starts or restarts the workflow. Explicit initial human supply/edit/approval would establish manual, but generic caller identity and arbitrary project authorship do not establish that decision. Known imports, recording paths and later replacements do not resolve initial provenance. Qualified human-answer messages have implemented advisory delivery and potential recovery; only the bare-name alternative reaches the bounds defect. This does not authenticate authorship or guarantee persistence, browser delivery, ordering or restored pending waits. See [EPI-RTE-human-answers](epistemic.md#epi-rte-human-answers), [MEM-RTE-session-recovery](memory.md#mem-rte-session-recovery) and [MEM-RTE-project-records](memory.md#mem-rte-project-records).

Reconciliation supersedes the epistemic bug-description and changelog-entry duplicates with [MEM-OBJ-bug-description](memory.md#mem-obj-bug-description) and [MEM-OBJ-changelog-entry](memory.md#mem-obj-changelog-entry). Those canonical records support the corresponding substrate, form, lineage, authority and maintenance findings; supersession changes no value. Other overlapping route/container records remain distinct. The current pinned epistemic answer route agrees with the memory account; the memory report's older-fragment objection is not carried as a current conflict.

Missing records for provider-private payloads/updates and arbitrary program stores prevent positive service-object, parametric, learned-parameter, semantic-selector or additional trace-source classifications. Missing initial authorship/control, live extension-state reload and automatic diagnostic consumers prevent complete lineage, agency, read-back and authority assessments. These are limitations, not evidence of absence. Static role templates, model components and binary installation are not substituted for accumulated memory merely because they shape the runtime.
