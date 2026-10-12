---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of Instinctual Memory: adapted journal, Git facts and controls, task/protocol state and later host-context routes."
run-id: "AAS-2026-10-12-instinctual-memory-af48437aa60c-01"
source-identity: "https://github.com/jasonkneen/instinctual-memory"
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
memory-comparison:
  version: 2
  scope: "Target-retained adapted journal events; published facts, source references, controls, checkpoint, dispositions, displays/index and prior snapshots; immediate-change intents/receipts; separate tasks; generated project instruction blocks; their acquisition, update, maintenance and later extraction/host/recovery consumers. Excludes transient proposals/ranking results, static shipped skill/prompts, deployment/model-selection configuration, external inference weights/provider retention, and transient evaluator/benchmark reports. External host consumption remains included as afforded delivery, not attributed internal host implementation."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Adapted journal text, metadata and redaction markers"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-rte-adapter-ingestion"
              note: "Framed JSONL persists adapted events separately from memory.git."
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
          note: "Day files are the operative raw input and independently reloaded retrieval store."
        - scope: "Published facts, evidence, controls, checkpoint, dispositions, entity bodies and index; retained prior snapshots"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-obj-dispositions"
                - "memory.md#mem-obj-entity-display"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-immediate-change"
                - "memory.md#mem-rte-index-rebuild"
              note: "Git publication retains the structured content, access state and generated displays together."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-source-ref"
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-obj-dispositions"
            - "memory.md#mem-obj-entity-display"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-immediate-change"
            - "memory.md#mem-rte-index-rebuild"
          note: "All these parts are stored in published bare-Git snapshots; Markdown/JSON/YAML describe encodings, not extra substrates."
        - scope: "Immediate-change intents and receipts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "Durable pending intents are written before publication and consumed by later recovery."
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "Published receipts are looked up for later replay decisions."
          records:
            - "runtime.md#rt-rte-immediate-change"
          note: "Recovery/replay retain change state; the route supplies the filesystem intent and Git publisher receipt account."
        - scope: "Separate task titles, IDs and version"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "Task reads reload the ordinary locked task file."
          records:
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
          note: "tasks.json is outside the Git memory publisher."
        - scope: "Generated project instruction block"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-writeback"
                - "runtime.md#rt-bap-instruction-file"
              note: "Writeback persists selected statements in the caller-chosen project file."
          records:
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-bap-instruction-file"
          note: "The target file is separately written and can be loaded in later host sessions."
      records:
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-rte-adapter-ingestion"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-source-ref"
        - "memory.md#mem-obj-controls"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-dispositions"
        - "memory.md#mem-obj-entity-display"
        - "runtime.md#rt-rte-journal-consolidation"
        - "runtime.md#rt-rte-immediate-change"
        - "memory.md#mem-rte-index-rebuild"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-bap-instruction-file"
      note: "The inventory covers the target-retained raw, derived, control, recovery, task and writeback parts. External inference parameters and provider retention are not target memory stores in this scope."
    representational_form:
      assessment: "known"
      units:
        - scope: "Journal content and searchable textual metadata"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "runtime.md#rt-rte-memory-retrieval"
              note: "Recorded conversational, file, calendar, voice and IDE text supplies interpreted content."
          records:
            - "memory.md#mem-obj-journal-event"
            - "runtime.md#rt-rte-memory-retrieval"
          note: "Text reaches extractor or host interpretation; adapter retention is not an untouched transcript."
        - scope: "Journal identities, sequence, source, role, project and redaction fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-rte-adapter-ingestion"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-memory-retrieval"
              note: "Fields govern ordering, role eligibility, filtering and lookup."
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-memory-retrieval"
          note: "Fixed parser and selector rules consume these localized fields."
        - scope: "Fact statements and evidence quotes"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-rte-host-hooks"
                - "runtime.md#rt-rte-instruction-writeback"
              note: "Statements inform extraction and hosts; evidence retains source wording without semantic proof."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-memory-retrieval"
            - "runtime.md#rt-rte-host-hooks"
            - "runtime.md#rt-rte-instruction-writeback"
          note: "Statements and evidence are separate retained text parts; ordinary host delivery often omits the quote."
        - scope: "Fact eligibility/reference fields and source IDs/roles"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-rte-erasure-maintenance"
              note: "Localized metadata controls eligibility, lookup and erasure targets."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-memory-retrieval"
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "Software interprets identifiers, statuses, dates, visibility and source references."
        - scope: "Suppression/deletion membership and progress checkpoint"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-host-hooks"
              note: "Membership gates admission/reads and sequence progress selects later extraction windows."
          records:
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-checkpoint"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-host-hooks"
          note: "Control IDs and through_seq have different effects but the same fixed-rule encoding."
        - scope: "Control reasons and quarantine explanation text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-dispositions"
                - "runtime.md#rt-rte-tidy-maintenance"
              note: "Suppression reasons and quarantine categories explain outcomes to potential inspectors."
          records:
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-dispositions"
            - "runtime.md#rt-rte-tidy-maintenance"
          note: "Reasons are retained prose, not a learned criterion; no subsequent automatic reason-reading consumer is established."
        - scope: "Disposition window/extractor/outcome IDs and receipt/intent change state"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-dispositions"
                - "runtime.md#rt-rte-immediate-change"
              note: "Localized identifiers, sequences and canonical change data represent protocol state."
          records:
            - "memory.md#mem-obj-dispositions"
            - "runtime.md#rt-rte-immediate-change"
          note: "These encode update outcomes and replay/recovery state rather than host knowledge."
        - scope: "Entity display and navigation index text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-display"
                - "memory.md#mem-rte-index-rebuild"
              note: "Titles and rendered statements remain readable textual summaries."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-display"
                - "memory.md#mem-rte-index-rebuild"
              note: "Displayed IDs and Active counts support navigation under fixed rendering rules."
          records:
            - "memory.md#mem-obj-entity-display"
            - "memory.md#mem-rte-index-rebuild"
          note: "Core search parses facts rather than these displays; external inspection is afforded."
        - scope: "Task title versus task coordination fields"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "Titles are interpreted work descriptions."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "IDs and versions coordinate task append/read."
          records:
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
          note: "Split the interpreted work description from software version/ID checks."
        - scope: "Generated instruction block statement and identity parts"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-writeback"
                - "runtime.md#rt-bap-instruction-file"
              note: "Statements become host instruction/context text."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-writeback"
                - "runtime.md#rt-bap-instruction-file"
              note: "Fact IDs and a source revision label identify generated content."
          records:
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-bap-instruction-file"
          note: "Persisted block includes interpreted statements and mechanically rendered IDs/revision markers."
      records:
        - "memory.md#mem-obj-journal-event"
        - "runtime.md#rt-rte-memory-retrieval"
        - "memory.md#mem-rte-adapter-ingestion"
        - "runtime.md#rt-rte-journal-consolidation"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-source-ref"
        - "runtime.md#rt-rte-host-hooks"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-rte-erasure-maintenance"
        - "memory.md#mem-obj-controls"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-dispositions"
        - "runtime.md#rt-rte-tidy-maintenance"
        - "runtime.md#rt-rte-immediate-change"
        - "memory.md#mem-obj-entity-display"
        - "memory.md#mem-rte-index-rebuild"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
        - "runtime.md#rt-bap-instruction-file"
      note: "All included text and localized metadata encodings are classified. No retained target part in this inventory is a learned dense representation; external inference weights are excluded, not declared absent."
    lineage:
      assessment: "partial"
      units:
        - scope: "Adapter-to-journal acquisition path"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-rte-adapter-ingestion"
              note: "Adapters acquire conversations, project files, calendar/voice and IDE/export material."
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
          note: "Imported origin is known even though original authorship, authenticity and transcript completeness are not."
        - scope: "Rules/model event-to-fact derivation"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "Session text and calendar/voice experience can feed derived standing facts."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "Static project instruction text is also compiled into facts by extraction."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-rules-extraction"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Separate source-side activity from static project-file input; Role::Note alone does not authenticate either."
        - scope: "Initial authored/generated provenance of imported file and export content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-instruction-writeback"
          note: "Role labels and file hashes do not recover original hand-authored versus generated provenance. This prevents a complete original-lineage classification."
        - scope: "Caller remember/correct statement admission"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
                - "memory.md#mem-obj-fact"
              note: "Direct assertions/corrections import supplied statements without extraction evidence checks."
          records:
            - "runtime.md#rt-rte-immediate-change"
            - "memory.md#mem-obj-fact"
          note: "The route acquires caller content but generic caller labels do not identify its prior creation process."
        - scope: "Generated access/control/outcome/recovery parts"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-obj-dispositions"
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-immediate-change"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-tidy-maintenance"
                - "runtime.md#rt-rte-erasure-maintenance"
              note: "Software compiles operation state and references into durable protocol metadata."
          records:
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-obj-dispositions"
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-immediate-change"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-tidy-maintenance"
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "Current IDs, progress, outcome categories, intents and receipts are generated from update and withdrawal operations."
        - scope: "Entity body/index and instruction writeback from retained facts"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-display"
                - "memory.md#mem-rte-index-rebuild"
                - "runtime.md#rt-rte-instruction-writeback"
              note: "Rendering compiles retained fact content and metadata into displays and instruction blocks."
          records:
            - "memory.md#mem-obj-entity-display"
            - "memory.md#mem-rte-index-rebuild"
            - "runtime.md#rt-rte-instruction-writeback"
          note: "Generated display and copied instruction blocks do not establish new source truth."
        - scope: "Task titles supplied by callers"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "Caller titles enter the separate task store."
          records:
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
          note: "The append path acquires titles; their initial human/model/file provenance is not recorded."
      records:
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-rte-adapter-ingestion"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-source-ref"
        - "runtime.md#rt-rte-journal-consolidation"
        - "epistemic.md#epi-rte-rules-extraction"
        - "epistemic.md#epi-rte-llm-proposal"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-rte-immediate-change"
        - "memory.md#mem-obj-controls"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-dispositions"
        - "runtime.md#rt-rte-tidy-maintenance"
        - "runtime.md#rt-rte-erasure-maintenance"
        - "memory.md#mem-obj-entity-display"
        - "memory.md#mem-rte-index-rebuild"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
      note: "Known import, trace extraction and compilation paths coexist with unresolved initial authorship and caller derivation. No generic caller is upgraded to human-authored content."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Raw journal text at later answering host"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-bap-host-context"
              note: "Adapted text and excerpts can supply reference/context to the host."
          records:
            - "memory.md#mem-obj-journal-event"
            - "runtime.md#rt-rte-memory-retrieval"
            - "runtime.md#rt-bap-host-context"
          note: "Requested search/read delivers raw context, not enforced instructions."
        - scope: "Eligible retained experience at extraction updater"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "Recorded experience feeds automatic production of durable behavior-shaping facts."
          records:
            - "memory.md#mem-obj-journal-event"
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-rules-extraction"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Selected session/calendar/voice text feeds durable standing statements subsequently consumed by extraction or hosts."
        - scope: "Journal text/metadata and fact text at lexical or reranking selectors"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-memory-retrieval"
              note: "Retained candidate text/features determine relative retrieval scores and order."
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
            - "runtime.md#rt-rte-memory-retrieval"
          note: "Relative priority depends on retained content under fixed lexical rules or optional model judgments."
        - scope: "Fact statements at host search/read and prompt-context consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-rte-host-hooks"
                - "runtime.md#rt-bap-host-context"
              note: "Returned or prompt-matched statements inform host interpretation."
          records:
            - "memory.md#mem-obj-fact"
            - "runtime.md#rt-rte-memory-retrieval"
            - "runtime.md#rt-rte-host-hooks"
            - "runtime.md#rt-bap-host-context"
          note: "Delivery establishes context capacity, not host compliance or benefit."
        - scope: "Standing preference statements at SessionStart and generated instruction-file consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-host-hooks"
                - "runtime.md#rt-rte-instruction-writeback"
                - "runtime.md#rt-bap-instruction-file"
              note: "Retained standing preferences and written directions are supplied as host guidance."
          records:
            - "memory.md#mem-obj-fact"
            - "runtime.md#rt-rte-host-hooks"
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-bap-instruction-file"
          note: "Preference guidance is pushed through additionalContext; instruction-block authority is conditional on later host loading."
        - scope: "Existing fact statements at next extraction and duplicate check"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-journal-consolidation"
              note: "Previously derived statements feed a subsequent durable fact update."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-journal-consolidation"
              note: "Current statement overlap supplies candidate admissibility criteria."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "runtime.md#rt-rte-journal-consolidation"
              note: "Near-duplicate rejection prevents candidate placement."
          records:
            - "memory.md#mem-obj-fact"
            - "runtime.md#rt-rte-journal-consolidation"
          note: "Known-entity summaries guide new proposals; existing text can veto near-duplicate placement."
        - scope: "Fact status/date/visibility and suppression/deletion controls at read/admission gates"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-controls"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-rte-immediate-change"
                - "runtime.md#rt-rte-tidy-maintenance"
              note: "Retained eligibility/control fields determine candidate/read conformance."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-controls"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-memory-retrieval"
                - "runtime.md#rt-rte-immediate-change"
                - "runtime.md#rt-rte-tidy-maintenance"
              note: "Blocked IDs and relevant status/eligibility checks veto admission or delivery."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-controls"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-memory-retrieval"
            - "runtime.md#rt-rte-immediate-change"
            - "runtime.md#rt-rte-tidy-maintenance"
          note: "Eligibility differs by route; writeback does not load Controls and entity reads do not uniformly apply temporal bounds."
        - scope: "Source IDs at changed-file retirement and erasure"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-ref"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-erasure-maintenance"
              note: "Source identity determines retirement and which source events erasure processes."
          records:
            - "memory.md#mem-obj-source-ref"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "References select old-source facts and journal redaction targets, not proof of entailment."
        - scope: "Checkpoint sequence and derived lag at consolidation and hook sync"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint"
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-host-hooks"
              note: "through_seq chooses the next extraction window; lag selects whether sync consolidates."
          records:
            - "memory.md#mem-obj-checkpoint"
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-host-hooks"
          note: "Checkpoint is progress metadata, not a semantic continuation summary."
        - scope: "Intent/receipt state at recovery and replay"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "Retained intents/receipts select recovery, replay or stale set-aside behavior."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "At the core publisher, a retained receipt digest checks reused-request conformance."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "Core digest mismatch rejects conflicting reuse; the shared operation early-return bypass remains a limit."
          records:
            - "runtime.md#rt-rte-immediate-change"
          note: "Recovery consumes retained changes and base/request identity rather than fact truth."
        - scope: "Task title at later host and task version at append"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "A returned task title supplies a work directive to the host."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "Retained version determines whether the requested append conforms."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-tasks"
                - "runtime.md#rt-rte-task-update"
              note: "Version mismatch refuses the update."
          records:
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
          note: "Title interpretation does not enforce task execution; the expected-version check does enforce append concurrency."
        - scope: "Entity/index display at external inspection"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-entity-display"
                - "memory.md#mem-rte-index-rebuild"
              note: "Rendered statements, titles and counts can supply reference/navigation information."
          records:
            - "memory.md#mem-obj-entity-display"
            - "memory.md#mem-rte-index-rebuild"
          note: "Human or external snapshot inspection is supported as an affordance, not demonstrated deployment."
        - scope: "Source evidence text, suppression reasons and disposition explanations as later automatic guidance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-ref"
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-dispositions"
          note: "Evidence/reasons are retained, but ordinary delivery omits evidence and no later criterion-revision consumer of reasons/dispositions is established. Their existence cannot establish learning or instruction authority."
      records:
        - "memory.md#mem-obj-journal-event"
        - "runtime.md#rt-rte-memory-retrieval"
        - "runtime.md#rt-bap-host-context"
        - "runtime.md#rt-rte-journal-consolidation"
        - "epistemic.md#epi-rte-rules-extraction"
        - "epistemic.md#epi-rte-llm-proposal"
        - "memory.md#mem-obj-fact"
        - "runtime.md#rt-rte-host-hooks"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-bap-instruction-file"
        - "memory.md#mem-obj-controls"
        - "runtime.md#rt-rte-immediate-change"
        - "runtime.md#rt-rte-tidy-maintenance"
        - "memory.md#mem-obj-source-ref"
        - "runtime.md#rt-rte-erasure-maintenance"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
        - "memory.md#mem-obj-entity-display"
        - "memory.md#mem-rte-index-rebuild"
        - "memory.md#mem-obj-dispositions"
      note: "Consumer/effect units retain knowledge, instruction, learning, ranking, routing, validation and enforcement independently. Unconsumed reason/evidence alternatives cannot be upgraded from their readable encoding."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Adapter parse/dedup admission, including detached sync and public append"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-adapter-ingestion"
                - "runtime.md#rt-rte-host-hooks"
              note: "Software parsing and bulk seen-ID checks admit retained source events."
          records:
            - "memory.md#mem-rte-adapter-ingestion"
            - "runtime.md#rt-rte-host-hooks"
          note: "Caller file selection is not per-content approval; software admits adapted events."
        - scope: "Rules/model consolidation and state/display updates"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
                - "memory.md#mem-obj-dispositions"
                - "memory.md#mem-obj-entity-display"
              note: "Rules/model proposals and fixed software gates admit derived facts and accompanying state."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-checkpoint"
            - "memory.md#mem-obj-dispositions"
            - "memory.md#mem-obj-entity-display"
          note: "No per-fact human approval is required for candidate placement and publication."
        - scope: "Immediate-change structural admission and replay/recovery publication"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
              note: "Software validates and publishes caller candidates without a required human approval artifact."
          records:
            - "runtime.md#rt-rte-immediate-change"
          note: "The publisher is known, while actual content-supplying human control is separately unresolved."
        - scope: "Content-supplying decision for generic remember/correct/forget caller"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-immediate-change"
          note: "Live-agent/caller labels do not establish an explicit human content decision; automatic publisher wiring does not resolve that contribution."
        - scope: "Tidy recomputed suppression admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-tidy-maintenance"
                - "memory.md#mem-obj-controls"
              note: "Software/model selection plus publication admit the new suppression set."
          records:
            - "runtime.md#rt-rte-tidy-maintenance"
            - "memory.md#mem-obj-controls"
          note: "Apply recomputes the selected IDs; initiating apply and supplied keep IDs do not prove per-content approval of its new result."
        - scope: "Human approval of eventual tidy removals or erasure target"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-tidy-maintenance"
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "The skill requests review/confirmation, but direct executable calls do not bind an immutable approval artifact. Actual per-content human decision remains unresolved."
        - scope: "Erasure current-tree/control and source/history removal machinery"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-erasure-maintenance"
              note: "Programmed target resolution and scrub stages perform withdrawal without executable confirmation."
          records:
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "Software applies the supplied target across sequential stores; success and human target selection are separate issues."
        - scope: "Index/body generation and instruction-block selection/rendering"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-index-rebuild"
                - "memory.md#mem-obj-entity-display"
                - "runtime.md#rt-rte-instruction-writeback"
              note: "Software generates and replaces retained displays and selected instruction blocks."
          records:
            - "memory.md#mem-rte-index-rebuild"
            - "memory.md#mem-obj-entity-display"
            - "runtime.md#rt-rte-instruction-writeback"
          note: "Invocation and target choice do not amount to individual row/statement approval."
        - scope: "Task append structural admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-update"
              note: "Software admits a title when the retained version matches."
          records:
            - "runtime.md#rt-rte-task-update"
          note: "Version checking is known separately from the unresolved identity of the title-supplying decision."
        - scope: "Per-content human decision supplying task title or initial imported material"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
          note: "Generic callers and source role labels do not establish explicit human approval/authorship; import initiation alone is insufficient."
      records:
        - "memory.md#mem-rte-adapter-ingestion"
        - "runtime.md#rt-rte-host-hooks"
        - "runtime.md#rt-rte-journal-consolidation"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-controls"
        - "memory.md#mem-obj-checkpoint"
        - "memory.md#mem-obj-dispositions"
        - "memory.md#mem-obj-entity-display"
        - "runtime.md#rt-rte-immediate-change"
        - "runtime.md#rt-rte-tidy-maintenance"
        - "runtime.md#rt-rte-erasure-maintenance"
        - "memory.md#mem-rte-index-rebuild"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-rte-task-update"
        - "runtime.md#rt-obj-tasks"
        - "memory.md#mem-obj-journal-event"
      note: "Known automatic mechanisms remain positive. Human content-supplying or approval contributions at generic imports, assertions, tasks and destructive maintenance are unresolved, so a complete agency union is not justified."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Standing-fact extraction from retained session/file events"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
              note: "Extraction selects/compresses retained event claims into a reduced standing-fact representation."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-rules-extraction"
            - "epistemic.md#epi-rte-llm-proposal"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
          note: "Both rules and model routes reduce retained input into standing statements. Semantic fidelity is not guaranteed; defects do not automatically become synthesis."
        - scope: "Fact placement and tidy duplicate removal"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-tidy-maintenance"
                - "memory.md#mem-obj-fact"
              note: "Placement drops near duplicates and tidy suppresses shorter overlapping statements."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-tidy-maintenance"
            - "memory.md#mem-obj-fact"
          note: "Overlap/containment implements duplicate elimination without establishing semantic equivalence."
        - scope: "Direct correction of an existing retained fact"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
                - "memory.md#mem-obj-fact"
              note: "Caller correction revises an existing retained claim through replacement."
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-immediate-change"
                - "memory.md#mem-obj-fact"
              note: "The superseded predecessor loses current active reliance while history remains."
          records:
            - "runtime.md#rt-rte-immediate-change"
            - "memory.md#mem-obj-fact"
          note: "Correction changes reliance through supersession and replacement, not independent truth checking."
        - scope: "Changed-file retirement, soft forget and tidy suppression"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "runtime.md#rt-rte-immediate-change"
                - "runtime.md#rt-rte-tidy-maintenance"
                - "memory.md#mem-obj-controls"
              note: "Outdated, forgotten or cleanup-selected facts lose active reliance while prior content is retained."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "runtime.md#rt-rte-immediate-change"
            - "runtime.md#rt-rte-tidy-maintenance"
            - "memory.md#mem-obj-controls"
          note: "Withdrawal is ID/status/channel bounded; raw events and previously written blocks remain separate."
        - scope: "Destructive erasure of fact, raw source event and history"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-erasure-maintenance"
              note: "Sequential current-tree, journal and history removal implements forgetting of targeted retained content."
          records:
            - "runtime.md#rt-rte-erasure-maintenance"
          note: "The stages remove content rather than merely invalidating a current version; partial failure limits actual completion."
        - scope: "Semantic novelty of model-derived statements"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-llm-proposal"
            - "epistemic.md#epi-rte-rules-extraction"
          note: "Linked model outputs and interpretation checks are absent. Records do not establish an added non-entailed claim, so synthesize is not asserted from possible model invention."
      records:
        - "runtime.md#rt-rte-journal-consolidation"
        - "epistemic.md#epi-rte-rules-extraction"
        - "epistemic.md#epi-rte-llm-proposal"
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-obj-fact"
        - "runtime.md#rt-rte-tidy-maintenance"
        - "runtime.md#rt-rte-immediate-change"
        - "memory.md#mem-obj-controls"
        - "runtime.md#rt-rte-erasure-maintenance"
      note: "Implemented consolidation, deduplication, revision, withdrawal and forgetting are retained with their local routes. Index rendering and primary-key publication alone add no curation value. Semantic novelty remains unresolved."
    read_back_direction:
      assessment: "known"
      units:
        - scope: "Requested search, ID/entity/history reads and CLI source enrichment"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-retrieval"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-source-ref"
              note: "A caller requests retained facts or adapted journal material and receives the selected result."
          records:
            - "runtime.md#rt-rte-memory-retrieval"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-source-ref"
          note: "These fulfill an explicit consumer query or identifier lookup; delivery is not a second unsolicited supply."
        - scope: "Automatic SessionStart preference delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "The hook selects and supplies retained pref_user statements through additionalContext."
          records:
            - "runtime.md#rt-rte-host-hooks"
            - "memory.md#mem-obj-fact"
          note: "Host callback triggers an independent context selector rather than a host request for specified memory."
        - scope: "Automatic UserPromptSubmit fact delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "Lexical overlap selection supplies retained fact statements unsolicited through additionalContext."
          records:
            - "runtime.md#rt-rte-host-hooks"
            - "memory.md#mem-obj-fact"
          note: "Prompt text is selection input; the agent did not explicitly request these facts."
        - scope: "Later consolidation reload of journal, facts, controls and checkpoint"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
              note: "The batch loads retained state required for its update."
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-controls"
                - "memory.md#mem-obj-checkpoint"
              note: "Automatic sequence/scope and known-entity selection supplies bounded retained material to the extractor without an extractor request for those parts."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-controls"
            - "memory.md#mem-obj-checkpoint"
          note: "The updater explicitly loads its retained inputs; it then automatically chooses an extraction context."
        - scope: "Writeback request for retained statements"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-instruction-writeback"
              note: "Writeback requests retained statements and persists the selected block."
          records:
            - "runtime.md#rt-rte-instruction-writeback"
          note: "The command requests a generated block; this requested return is distinct from eventual unsolicited host input supply."
        - scope: "Generated block at later host instruction-file load"
          assessment: "known"
          findings:
            - value: "push"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-instruction-writeback"
                - "runtime.md#rt-bap-instruction-file"
              note: "A later host instruction-file load can supply the generated statements as standing context."
          records:
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-bap-instruction-file"
          note: "Actual host loading is external and unobserved; the retained block affords later standing context."
        - scope: "Task reads and immediate-change recovery/replay state reload"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-update"
                - "runtime.md#rt-rte-immediate-change"
              note: "tasks_read, recovery and replay lookups reload accumulated task/change state."
          records:
            - "runtime.md#rt-rte-task-update"
            - "runtime.md#rt-rte-immediate-change"
          note: "Later operations request the retained task/protocol state they need."
        - scope: "External snapshot inspection of evidence, dispositions and entity/index displays"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-source-ref"
                - "memory.md#mem-obj-dispositions"
                - "memory.md#mem-obj-entity-display"
                - "memory.md#mem-rte-index-rebuild"
              note: "An external inspector can request retained snapshots/display/outcome parts."
          records:
            - "memory.md#mem-obj-source-ref"
            - "memory.md#mem-obj-dispositions"
            - "memory.md#mem-obj-entity-display"
            - "memory.md#mem-rte-index-rebuild"
          note: "Repository/file access affords later requested inspection, not automatic host deployment."
      records:
        - "runtime.md#rt-rte-memory-retrieval"
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-source-ref"
        - "runtime.md#rt-rte-host-hooks"
        - "runtime.md#rt-rte-journal-consolidation"
        - "memory.md#mem-obj-controls"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-bap-instruction-file"
        - "runtime.md#rt-rte-task-update"
        - "runtime.md#rt-rte-immediate-change"
        - "memory.md#mem-obj-dispositions"
        - "memory.md#mem-obj-entity-display"
        - "memory.md#mem-rte-index-rebuild"
      note: "Requested returns and independent automatic context supply coexist. Wiring establishes hooks/extractor delivery; the instruction-file host load and external inspection remain afforded rather than observed."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "SessionStart preferences push"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "The pref_user identity match selects the delivered preference entity."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "Availability and the fixed delivery cap further limit which statements are supplied."
          records:
            - "runtime.md#rt-rte-host-hooks"
            - "memory.md#mem-obj-fact"
          note: "Trigger: SessionStart; selector: active-count availability then pref_user entity identity and a 20-statement cap; retained part: preference statements."
        - scope: "UserPromptSubmit context push"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "Lexical scoring and word overlap select prompt-relevant retained facts."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-host-hooks"
                - "memory.md#mem-obj-fact"
              note: "Slash/short-prompt and fixed shortlist/delivery limits gate automatic supply."
          records:
            - "runtime.md#rt-rte-host-hooks"
            - "memory.md#mem-obj-fact"
          note: "Trigger: eligible prompt callback; selector input: up to 600 prompt characters; retained part: up to six lexical/meaningful-word-overlap fact statements."
        - scope: "Automatic event and known-entity selection for extraction"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-checkpoint"
              note: "Sequence windows, role/scope eligibility and entity/fact/text budgets select coarse retained subsets."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-checkpoint"
              note: "Scope identity filtering selects matching retained events within the window."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-checkpoint"
          note: "Trigger: batch; inputs: checkpoint sequence, scope/role eligibility and current entities; selected parts: bounded event text and active statement summaries."
        - scope: "Generated block at later host instruction-file supply"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-bap-instruction-file"
          note: "Trigger: subsequent instruction-file loading; supplied block is available but host selection internals are not frozen."
      records:
        - "runtime.md#rt-rte-host-hooks"
        - "memory.md#mem-obj-fact"
        - "runtime.md#rt-rte-journal-consolidation"
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-obj-checkpoint"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-bap-instruction-file"
      note: "Known hook and extractor selectors coexist with an external host-load selector whose actual matching/budget behavior is not recorded. A requested target-file identifier does not establish identifier-based host push."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Rules/model user-session extraction into facts and next-update/host context"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
              note: "Recorded conversational experience feeds automatic durable behavior-shaping fact production and later consumption."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-rules-extraction"
            - "epistemic.md#epi-rte-llm-proposal"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
          note: "Automatic trace-fed writes persist standing statements consumed in subsequent extraction, search or hooks; faithful semantics and improvement are not required for wired classification."
        - scope: "Calendar/voice Note extraction into facts"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-journal-consolidation"
                - "memory.md#mem-obj-journal-event"
                - "memory.md#mem-obj-fact"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "Calendar entries and voice cues can be extracted into facts consumed by later updates/hosts."
          records:
            - "runtime.md#rt-rte-journal-consolidation"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Note framing is not source origin: timestamped experience can feed the same automatic durable fact route."
        - scope: "Opaque prior origin of generic Note/export and direct caller/task content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
            - "runtime.md#rt-rte-immediate-change"
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Generic imported/caller content may derive from activity, but records do not trace every origin and later behavior-shaping automatic write. A system-wide no or complete route inventory cannot be inferred."
        - scope: "Derived instruction-block feedback into later Markdown extraction"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-rte-journal-consolidation"
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-obj-fact"
          note: "The feedback path is wired, but file origin does not distinguish trace-derived statements from static imported rules. The qualifying trace-fed subset cannot be completely identified from Role::Note alone."
      records:
        - "runtime.md#rt-rte-journal-consolidation"
        - "epistemic.md#epi-rte-rules-extraction"
        - "epistemic.md#epi-rte-llm-proposal"
        - "memory.md#mem-obj-journal-event"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-rte-adapter-ingestion"
        - "runtime.md#rt-rte-immediate-change"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
        - "runtime.md#rt-rte-instruction-writeback"
      note: "Qualifying automatic session and event-derived fact routes establish yes. Unresolved generic origins remain local uncertainties; no absence record supports a system-wide or local no."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Qualifying user-session rules/model extraction"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-rules-extraction"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "User turns from agent work sessions feed the qualifying standing-fact update."
          records:
            - "memory.md#mem-obj-journal-event"
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-rules-extraction"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Original source is recorded conversational turns, not the adapter event wrapper. Assistant/tool/system roles are excluded from model consolidation; raw tool retrieval alone does not establish trace learning."
        - scope: "Qualifying calendar and timestamped voice extraction"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journal-event"
                - "runtime.md#rt-rte-journal-consolidation"
                - "epistemic.md#epi-rte-llm-proposal"
              note: "Calendar entries and timestamped voice cues supply recorded environmental/runtime experience."
          records:
            - "memory.md#mem-obj-journal-event"
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Calendar/voice inputs remain event sources when adapted as Notes and framed as memory files."
        - scope: "Generic Note/export and instruction-block feedback origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-journal-event"
            - "memory.md#mem-rte-adapter-ingestion"
            - "runtime.md#rt-rte-instruction-writeback"
            - "runtime.md#rt-rte-journal-consolidation"
            - "epistemic.md#epi-rte-llm-proposal"
          note: "Generic file/export origin and generated-block mixture do not reveal every qualifying original trace source. Static project instructions are imported lineage, not a trace-source value."
        - scope: "Possible trace origin behind direct assertions/tasks"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-immediate-change"
            - "runtime.md#rt-obj-tasks"
            - "runtime.md#rt-rte-task-update"
          note: "Generic caller identity and titles/statements do not establish original trace content or a qualifying trace-fed route; no additional source value is inferred."
      records:
        - "memory.md#mem-obj-journal-event"
        - "runtime.md#rt-rte-journal-consolidation"
        - "epistemic.md#epi-rte-rules-extraction"
        - "epistemic.md#epi-rte-llm-proposal"
        - "memory.md#mem-rte-adapter-ingestion"
        - "runtime.md#rt-rte-instruction-writeback"
        - "runtime.md#rt-rte-immediate-change"
        - "runtime.md#rt-obj-tasks"
        - "runtime.md#rt-rte-task-update"
      note: "Known session-log and event-stream sources belong to their qualifying writes. Tool/IDE content is retained raw, but no recorded qualifying update consumes those tool traces; wrapper serialization does not add event-streams."
---

# Instinctual Memory memory profile

## Comparison rationale

This profile classifies accepted records rather than adding source findings. No target source files were read for this job. All positive bases are wiring or explicitly afforded consumption; no observed operation or causal benefit is inferred.

The memory boundary is the target's accumulated material, not its entire storage surface. Cached cross-encoder weights, configurable remote models, installed static skill and setup configuration are inference/deployment machinery, not memory accumulated through the reviewed use loop. Transient proposals and score reports do not become retained memory merely because a later fact can be published.

The published fact and its source reference have separate consumers. Statements reach extraction and host context; evidence quotes ordinarily do not accompany delivery. Suppression reasons and dispositions are readable retained text without an established automatic criterion-revision reader. Their encoding is known while their additional behavioral authority is not determinable. Knowledge, instruction, learning, ranking, routing, validation and enforcement therefore remain consumer-specific rather than a property assigned to every stored fact. See [MEM-OBJ-fact](memory.md#mem-obj-fact), [MEM-OBJ-source-ref](memory.md#mem-obj-source-ref), [MEM-OBJ-controls](memory.md#mem-obj-controls) and [MEM-OBJ-dispositions](memory.md#mem-obj-dispositions).

Automatic software admission is distinct from a human supplying or approving that content. Command initiation, caller labels and tidy keep exclusions do not settle every human contribution. Tidy's recomputed application is not an approved immutable preview. These limits retain known automatic writes without asserting manual agency from an intended host interaction. See [RT-RTE-immediate-change](runtime.md#rt-rte-immediate-change), [RT-RTE-tidy-maintenance](runtime.md#rt-rte-tidy-maintenance) and [RT-RTE-task-update](runtime.md#rt-rte-task-update).

Standing-fact extraction is consolidation even where a regex drops negation or a model's semantic fidelity is unresolved. Neither defect establishes synthesis. Corrections revise entries; retirement/soft suppression withdraw reliance with history; destructive erasure forgets targeted content through sequential stages. No complete erasure result is inferred. See [EPI-RTE-rules-extraction](epistemic.md#epi-rte-rules-extraction), [EPI-RTE-llm-proposal](epistemic.md#epi-rte-llm-proposal) and [RT-RTE-erasure-maintenance](runtime.md#rt-rte-erasure-maintenance).

Push classification separates requested returns from unsolicited selection. Hooks independently select preferences or prompt-matched facts. The extraction chain loads state and automatically supplies a bounded subset to its extractor. Writeback persists a requested generated block, but subsequent host loading remains an affordance with an unresolved selector; the requested target filename alone is not evidence of identity-based push. See [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks), [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation) and [RT-RTE-instruction-writeback](runtime.md#rt-rte-instruction-writeback).

Trace learning means automatic trace-fed production of durable behavior-shaping material, not parameter training, truth acceptance or measured improvement. Session messages and calendar/voice experience qualify on their recorded paths. Project instruction imports do not become traces merely because they are wrapped as events. Raw IDE/tool retention and retrieval do not establish a qualifying tool-trace update, and generic file/caller origins prevent complete trace-source coverage. See [MEM-OBJ-journal-event](memory.md#mem-obj-journal-event) and [RT-RTE-journal-consolidation](runtime.md#rt-rte-journal-consolidation).

Reconciliation supersedes EPI-OBJ-fact with MEM-OBJ-fact, EPI-OBJ-source-ref with MEM-OBJ-source-ref, and EPI-RTE-index-rebuild with MEM-RTE-index-rebuild. The profile cites only those canonical declarations. The amendments preserve unknown source warrant and bounded metadata derivation; they change citation identity, not evidence strength or value. The valid consolidation container remains alongside its rules, model and candidate-gate parts. No current unresolved inter-report conflict requires selecting a stronger finding.
