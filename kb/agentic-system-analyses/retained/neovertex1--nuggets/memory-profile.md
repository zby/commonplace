---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Nuggets memory comparison: readable JSON/local facts, reconstructed HRR state, trace extraction, deferred prompts and conditional Markdown export, with opaque host continuation retained as a limit."
run-id: "AAS-2026-10-14-nuggets-c2e87e6916cc-01"
source-identity: "https://github.com/NeoVertex1/nuggets"
reviewed-boundary: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
memory-comparison:
  version: 2
  scope: "Shipped retained shelf facts (default and named stores), keys/access metadata, extension-local facts and exposed branch snapshots, precompaction task/path artifacts, reconstructed operative HRR state, promoted Markdown and accepted cron controls/prompts, including their admission, maintenance and later-consumer routes. External Pi session/checkpoint payloads are included as unresolved continuation alternatives. Excludes shipped static instructions, transient current-turn RPC/queue state and recall scores, setup/transport controls, provider parameter training and the absent advertised plugin. External Claude loading is an unresolved consumer of included exported memory, not an established host implementation."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Shelf fact strings, keys, task excerpt and access metadata"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-hit-metadata"
                - "memory.md#mem-obj-task-summary"
              note: "Named nugget JSON retains content and counters."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-hit-metadata"
                - "memory.md#mem-obj-task-summary"
              note: "Library fact arrays retain the operative loaded content and metadata."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-hit-metadata"
            - "memory.md#mem-obj-task-summary"
          note: "Fact/configuration JSON and the corresponding process arrays are covered; this is not vector-only persistence."
        -
          scope: "Extension-local facts and exposed tool-result snapshots"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-rte-context-rebuild"
              note: "The extension accumulates key/value facts in its process Map."
          records:
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-rte-context-rebuild"
          note: "Local Map storage is inspected; host persistence of the returned details is assessed separately."
        -
          scope: "Reconstructed HRR banks and vocabulary vectors"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-hrr-vectors"
                - "epistemic.md#epi-rte-recall-decode"
              note: "Float64Array banks are operative in-process state."
          records:
            - "runtime.md#rt-cmp-hrr-vectors"
            - "epistemic.md#epi-rte-recall-decode"
          note: "Numerical encoding is reconstructed in RAM, not serialized or stored in a vector database."
        -
          scope: "Promoted Markdown artifact"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-promoted-memory"
                - "runtime.md#rt-rte-memory-promotion"
              note: "The writer merges and replaces Claude-project MEMORY.md."
          records:
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-memory-promotion"
          note: "The conditional writer establishes a retained filesystem artifact, not actual external reading."
        -
          scope: "Accepted cron job controls and prompts"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-schedule-admission"
              note: "jobs.json retains accepted controls and prompt."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
              note: "The scheduler retains a loaded CronJob array for later ticks."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-schedule-admission"
            - "runtime.md#rt-rte-proactive-turn"
          note: "Persisted accepted jobs and loaded job array are inspected, distinct from intermediate proposals."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Storage substrate cannot be completely classified."
      records:
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-hit-metadata"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-rte-context-rebuild"
        - "runtime.md#rt-cmp-hrr-vectors"
        - "epistemic.md#epi-rte-recall-decode"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-rte-schedule-admission"
        - "runtime.md#rt-rte-proactive-turn"
        - "runtime.md#rt-rte-message-turn"
        - "memory.md#mem-rte-compaction-extract"
      note: "Inspected retained objects use files and process RAM. External host session/checkpoint substrates remain unresolved; JSON and HRR are encodings, not additional substrates."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Readable shelf/local fact values, extracted preferences, task excerpt and promoted value text at model/human interpretation"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-obj-task-summary"
                - "memory.md#mem-obj-promoted-memory"
                - "epistemic.md#epi-rte-preference-capture"
                - "runtime.md#rt-bap-facts-prompt"
              note: "Later prompt/tool text and intended exported context supply meaning through language interpretation."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-obj-task-summary"
            - "memory.md#mem-obj-promoted-memory"
            - "epistemic.md#epi-rte-preference-capture"
            - "runtime.md#rt-bap-facts-prompt"
          note: "Text is distinguished from keys, formatting and scheduling controls; file paths have a separate fixed-code consumption path."
        -
          scope: "Fact keys, hit/session fields, local-map keys and Markdown section/key organization"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-hit-metadata"
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-obj-promoted-memory"
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-rte-recall-selection"
              note: "Keys select/group content; counters select promotion; section/key syntax controls the merge."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-hit-metadata"
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-obj-promoted-memory"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-recall-selection"
          note: "Localized fields have fixed matching, grouping and threshold rules."
        -
          scope: "Captured file paths at capture code and later model context"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-compaction-extract"
                - "epistemic.md#epi-obj-file-path"
              note: "Capture uses exact tool names, string path fields and basename-derived keys."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-rebuild"
                - "epistemic.md#epi-obj-file-path"
              note: "Active Files supplies the paths as interpreted model context."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-rte-context-rebuild"
            - "epistemic.md#epi-obj-file-path"
          note: "The same retained path string has distinct fixed-rule and interpreted-context consumption."
        -
          scope: "Dense HRR representation at numerical decoder"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-hrr-vectors"
                - "epistemic.md#epi-rte-recall-decode"
              note: "Superposed numerical banks and vocabulary vectors drive unbinding and decoding."
          records:
            - "runtime.md#rt-cmp-hrr-vectors"
            - "epistemic.md#epi-rte-recall-decode"
          note: "Locally reconstructed dense numerical state is distributed-parametric form, not trained provider weights."
        -
          scope: "Cron control fields at scheduler"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
              note: "Scheduler/routing rules consume localized fields."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-proactive-turn"
          note: "Job identity, recipient, enabled flag, one-shot flag and cron fields have fixed consumers."
        -
          scope: "Retained cron prompt at Pi/model"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-bap-scheduled-prompt"
              note: "Stored prompt becomes a later model request."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-bap-scheduled-prompt"
          note: "Prompt content is distinct from the job envelope."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Representational form cannot be completely classified."
      records:
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-obj-promoted-memory"
        - "epistemic.md#epi-rte-preference-capture"
        - "runtime.md#rt-bap-facts-prompt"
        - "memory.md#mem-obj-hit-metadata"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-rte-recall-selection"
        - "memory.md#mem-rte-hook-capture"
        - "memory.md#mem-rte-compaction-extract"
        - "epistemic.md#epi-obj-file-path"
        - "runtime.md#rt-cmp-hrr-vectors"
        - "epistemic.md#epi-rte-recall-decode"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-rte-proactive-turn"
        - "runtime.md#rt-bap-scheduled-prompt"
        - "runtime.md#rt-rte-message-turn"
      note: "The recorded inventory includes language, localized symbolic fields and distributed numerical representation. No inspected display summary resolves opaque host payload form."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Explicit model-authored remember proposals admitted by extension"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-mutation"
                - "epistemic.md#epi-obj-remember-value"
              note: "The model supplies key/value content to remember."
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "epistemic.md#epi-obj-remember-value"
          note: "Authored describes the explicit content producer, not human approval; actual source warrants and live initial values remain unknown."
        -
          scope: "Input/result-hook facts and precompaction task/path extraction"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-obj-task-summary"
              note: "Input fragments, tool-call paths and selected conversational text become retained facts."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-obj-task-summary"
          note: "Fixed extraction derives short records from activity traces without source rationale."
        -
          scope: "Imported legacy content through kind migration"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-legacy-migration"
                - "memory.md#mem-obj-nugget-facts"
              note: "Legacy JSON enters the kind stores through the migration driver."
          records:
            - "memory.md#mem-rte-legacy-migration"
            - "memory.md#mem-obj-nugget-facts"
          note: "This known acquisition path does not resolve who authored the original legacy facts."
        -
          scope: "Local facts restored from shelf and retained branch details"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-rte-context-rebuild"
              note: "Hydration and branch replay copy existing content into the local Map."
          records:
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-rte-context-rebuild"
          note: "This is a recorded reload/copy path, not a warrant about original authorship."
        -
          scope: "Generated HRR banks and vocabulary encoding"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-hrr-vectors"
                - "epistemic.md#epi-rte-recall-decode"
              note: "Deterministic construction derives numerical banks from readable facts/configuration."
          records:
            - "runtime.md#rt-cmp-hrr-vectors"
            - "epistemic.md#epi-rte-recall-decode"
          note: "The name seed, fact order, values and configuration establish local generation; no embedding service is used."
        -
          scope: "Tool snapshots, access metadata and promoted Markdown construction"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-obj-hit-metadata"
                - "memory.md#mem-obj-promoted-memory"
                - "runtime.md#rt-rte-memory-promotion"
              note: "Code snapshots the Map, updates hit fields and renders selected/merged Markdown entries."
          records:
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-obj-hit-metadata"
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-memory-promotion"
          note: "These derived parts are produced by serialization, counter maintenance and recognized-entry rendering."
        -
          scope: "Initial shelf/Markdown contents and generic direct-library content provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-promoted-memory"
            - "memory.md#mem-rte-fact-mutation"
          note: "Loaded files and generic callers are known entry surfaces, but no live initial content or original producer was supplied; original lineage is unresolved."
        -
          scope: "Model-origin cron prompt proposals"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-schedule-admission"
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-bap-scheduled-prompt"
              note: "The model supplies the message retained as a later prompt."
          records:
            - "runtime.md#rt-rte-schedule-admission"
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-bap-scheduled-prompt"
          note: "The schedule tool accepts model-authored prompt content; imported preexisting jobs have separate unresolved origins."
        -
          scope: "Initially loaded accepted jobs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-schedule-admission"
          note: "Reload wiring establishes availability but not original authorship or derivation of preexisting jobs."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Lineage cannot be completely classified."
      records:
        - "memory.md#mem-rte-fact-mutation"
        - "epistemic.md#epi-obj-remember-value"
        - "memory.md#mem-rte-hook-capture"
        - "memory.md#mem-rte-compaction-extract"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-rte-legacy-migration"
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-rte-context-rebuild"
        - "runtime.md#rt-cmp-hrr-vectors"
        - "epistemic.md#epi-rte-recall-decode"
        - "memory.md#mem-obj-hit-metadata"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-rte-schedule-admission"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-bap-scheduled-prompt"
        - "runtime.md#rt-rte-message-turn"
      note: "Known authored, imported, trace-extracted and other-compiled paths coexist with unknown original contents and host checkpoint provenance. A known reload path does not establish complete original lineage."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained factual/path/task text at later Pi/model prompt or requested recall"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-task-summary"
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-rte-recall-selection"
                - "runtime.md#rt-bap-facts-prompt"
              note: "Selected fact/path text and explicitly recalled task text supply context to the later model."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-task-summary"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-recall-selection"
            - "runtime.md#rt-bap-facts-prompt"
          note: "Delivery supplies reference/context without factual acceptance or obedience guarantees; _task has requested rather than ordinary push delivery."
        -
          scope: "Retained preferences as repeated host guidance"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-preference-capture"
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-context-rebuild"
                - "runtime.md#rt-bap-facts-prompt"
              note: "Preference values delivered in the Preferences system-prompt section ask for later behavior."
          records:
            - "epistemic.md#epi-rte-preference-capture"
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-context-rebuild"
            - "runtime.md#rt-bap-facts-prompt"
          note: "Preferences are supplied as standing behavioral directions, independently of extraction faithfulness."
        -
          scope: "Retained traces at automatic extraction and compaction update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-obj-session-facts"
              note: "Extension extraction consumes experience to update retained preference, path and task artifacts for future turns."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-obj-session-facts"
          note: "Recorded input/tool/session activity feeds durable context artifacts with later consumers; this does not demonstrate improved capacity."
        -
          scope: "Retained keys/values and HRR state at recall matching/decoding"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "runtime.md#rt-cmp-hrr-vectors"
                - "memory.md#mem-rte-recall-selection"
                - "epistemic.md#epi-rte-recall-score"
              note: "Lexical key matching, vocabulary similarity and cross-kind scoring determine relative recall priority."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "runtime.md#rt-cmp-hrr-vectors"
            - "memory.md#mem-rte-recall-selection"
            - "epistemic.md#epi-rte-recall-score"
          note: "Fixed selection code consumes retained content and numerical features as ranking inputs; transient confidence itself is not accumulated memory."
        -
          scope: "Retained fact keys and named-store organization at dispatch/formatting"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-rte-recall-selection"
              note: "Prefixes choose prompt sections and named kinds/stores choose recall/hydration scope."
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-recall-selection"
          note: "Keys and store names select scopes and display sections, not factual admissibility."
        -
          scope: "Retained hit metadata at promotion writer"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hit-metadata"
                - "runtime.md#rt-rte-memory-promotion"
              note: "hits supplies the threshold criterion for promotion admission."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hit-metadata"
                - "runtime.md#rt-rte-memory-promotion"
              note: "Values below three hits are excluded from the promotion writer candidates."
          records:
            - "memory.md#mem-obj-hit-metadata"
            - "runtime.md#rt-rte-memory-promotion"
          note: "The retained usage threshold governs candidate admissibility, not truth validation; missing extension session IDs limit normal activation."
        -
          scope: "Retained cron controls at scheduler and router"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
              note: "Recipient and schedule state choose destination and later invocation timing."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
              note: "Enabled/cron-match rules permit or suppress emission of a retained job."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-schedule-admission"
            - "runtime.md#rt-rte-proactive-turn"
          note: "These fields select later operation and recipient and gate whether a job fires."
        -
          scope: "Retained scheduled prompt at later Pi/model"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-bap-scheduled-prompt"
              note: "The job prompt instructs a later turn through promptAndWait."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-bap-scheduled-prompt"
          note: "The stored request supplies behavioral directions at its actual model consumer; no compliance guarantee follows."
        -
          scope: "Promoted entries at intended external Claude consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-promoted-memory"
                - "runtime.md#rt-rte-memory-promotion"
              note: "Exported fact text is intended as later host context."
          records:
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-memory-promotion"
          note: "Actual loading and activation are outside the inspected implementation; only intended context supply is afforded."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Behavioral authority cannot be completely classified."
      records:
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-rte-recall-selection"
        - "runtime.md#rt-bap-facts-prompt"
        - "epistemic.md#epi-rte-preference-capture"
        - "memory.md#mem-rte-hook-capture"
        - "memory.md#mem-rte-compaction-extract"
        - "memory.md#mem-obj-session-facts"
        - "runtime.md#rt-cmp-hrr-vectors"
        - "epistemic.md#epi-rte-recall-score"
        - "memory.md#mem-obj-hit-metadata"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-rte-schedule-admission"
        - "runtime.md#rt-rte-proactive-turn"
        - "runtime.md#rt-bap-scheduled-prompt"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-message-turn"
      note: "Authority follows each actual consumer: knowledge, instruction, learning, ranking, routing, validation and enforcement have local warrants. Exported context remains afforded and opaque host payload effects uninspected; static instructions and unrelated ingress controls are not memory findings."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Extension explicit remember/forget and snapshot admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-mutation"
                - "memory.md#mem-obj-session-facts"
              note: "Code accepts model-supplied content/deletion and emits the local snapshot."
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "memory.md#mem-obj-session-facts"
          note: "Model choices and extension rules admit changes without per-content human approval."
        -
          scope: "Input/result-hook and precompaction extraction admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-compaction-extract"
              note: "Fixed rules propose and admit the derived records."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-compaction-extract"
          note: "Human input authorship or workflow initiation is not approval of extracted content."
        -
          scope: "Branch replay, hydration and local-map replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-obj-session-facts"
              note: "The hooks restore/merge selected snapshots and missing shelf keys."
          records:
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-obj-session-facts"
          note: "Lifecycle code admits existing retained content into the later operative Map."
        -
          scope: "Hit-counter maintenance"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hit-metadata"
                - "epistemic.md#epi-rte-recall-score"
              note: "Library recall updates hits/last marker and conditionally saves."
          records:
            - "memory.md#mem-obj-hit-metadata"
            - "epistemic.md#epi-rte-recall-score"
          note: "A supplied nonempty session ID enables code-controlled counter updates, with no per-counter human decision."
        -
          scope: "Legacy migration and conditional Markdown promotion"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-legacy-migration"
                - "runtime.md#rt-rte-memory-promotion"
              note: "The drivers merge/classify or select/render facts without per-entry approval."
          records:
            - "memory.md#mem-rte-legacy-migration"
            - "runtime.md#rt-rte-memory-promotion"
          note: "Operator launch of migration is distinct from its per-fact code admission; promotion is threshold/code-admitted."
        -
          scope: "Schedule-tool request and gateway accepted-job mutation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-schedule-admission"
                - "runtime.md#rt-obj-cron-jobs"
              note: "Extension append and gateway field/default-recipient checks create/delete retained jobs."
          records:
            - "runtime.md#rt-rte-schedule-admission"
            - "runtime.md#rt-obj-cron-jobs"
          note: "The user initiates a task, but the model fields are admitted by code without a per-job approval step."
        -
          scope: "Direct-library and initial-file content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-obj-cron-jobs"
          note: "Generic caller identity and existing loaded content do not establish explicit human supply/approval or software-only admission."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Write agency cannot be completely classified."
      records:
        - "memory.md#mem-rte-fact-mutation"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-rte-hook-capture"
        - "memory.md#mem-rte-compaction-extract"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-obj-hit-metadata"
        - "epistemic.md#epi-rte-recall-score"
        - "memory.md#mem-rte-legacy-migration"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-rte-schedule-admission"
        - "runtime.md#rt-obj-cron-jobs"
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-message-turn"
      note: "Inspected model/code mechanisms are automatic. The records do not support a manual finding merely from migration launch, generic APIs or possible file editing; initial/direct-caller control and host checkpoint admission remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing fact/task value replacement and recognized Markdown-entry merge"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-mutation"
                - "memory.md#mem-rte-compaction-extract"
                - "runtime.md#rt-rte-memory-promotion"
                - "memory.md#mem-obj-promoted-memory"
              note: "Case-insensitive upsert, task overwrite and recognized section/key merge replace retained values."
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "memory.md#mem-rte-compaction-extract"
            - "runtime.md#rt-rte-memory-promotion"
            - "memory.md#mem-obj-promoted-memory"
          note: "These mechanisms revise existing retained entries; global withdrawal and prior prose preservation are not guaranteed."
        -
          scope: "Optional maximum-fact eviction"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-mutation"
                - "epistemic.md#epi-rte-fact-upsert"
              note: "Bounded-capacity retention can forget older entries under configured limits."
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "epistemic.md#epi-rte-fact-upsert"
          note: "A positive configured maximum evicts oldest insertion entries; default zero is uncapped."
        -
          scope: "Selected retained conversational text before compaction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-obj-task-summary"
              note: "The task excerpt compresses selected session messages into a short retained representation."
          records:
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-obj-task-summary"
          note: "The host supplies recorded messages; joining the last three and truncating to 200 characters reduces existing text, without evidence of novel claims."
        -
          scope: "Preference extraction from input activity"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "epistemic.md#epi-rte-preference-capture"
              note: "Regex selection and truncation retain reduced preference/learning content from input traces."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "epistemic.md#epi-rte-preference-capture"
          note: "A short fragment becomes standing memory; semantic-loss defects do not turn this reduction into a supported synthesis operation."
        -
          scope: "Three-hit Markdown tier promotion"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-promotion"
                - "memory.md#mem-obj-hit-metadata"
                - "memory.md#mem-obj-promoted-memory"
              note: "Threshold-selected shelf entries are written into the higher-context Markdown artifact."
          records:
            - "runtime.md#rt-rte-memory-promotion"
            - "memory.md#mem-obj-hit-metadata"
            - "memory.md#mem-obj-promoted-memory"
          note: "Promotion changes placement to intended persistent host context, not factual warrant; ordinary extension recall does not increment hits."
        -
          scope: "Initial/generic-library content transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-rte-fact-mutation"
            - "memory.md#mem-obj-promoted-memory"
          note: "The admitted content has no supplied producer history; any upstream curation operation is not determinable."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Curation operations cannot be completely classified."
      records:
        - "memory.md#mem-rte-fact-mutation"
        - "memory.md#mem-rte-compaction-extract"
        - "runtime.md#rt-rte-memory-promotion"
        - "memory.md#mem-obj-promoted-memory"
        - "epistemic.md#epi-rte-fact-upsert"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-rte-hook-capture"
        - "epistemic.md#epi-rte-preference-capture"
        - "memory.md#mem-obj-hit-metadata"
        - "memory.md#mem-obj-nugget-facts"
        - "runtime.md#rt-rte-message-turn"
        - "memory.md#mem-rte-context-rebuild"
      note: "Recorded transformations support evolve, decay, consolidate and promote. Key-collision handling alone is not dedup, physical deletion without retained history is not invalidate, and no synthesize value is established. Those are not system-wide absence claims."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit model recall/list and operator overlay"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recall-selection"
                - "memory.md#mem-obj-session-facts"
              note: "Model calls request retained results; the operator command requests a human display."
          records:
            - "memory.md#mem-rte-recall-selection"
            - "memory.md#mem-obj-session-facts"
          note: "These operations fulfill consumer requests; automatic decoding inside requested recall does not add another push."
        -
          scope: "Extension lifecycle selection and per-turn fact injection"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-obj-session-facts"
                - "memory.md#mem-obj-nugget-facts"
                - "runtime.md#rt-bap-facts-prompt"
              note: "Selected branch/default-shelf facts reach the later model without a retained-material request."
          records:
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-obj-session-facts"
            - "memory.md#mem-obj-nugget-facts"
            - "runtime.md#rt-bap-facts-prompt"
          note: "Branch reconstruction/start hydration supply the local Map, and before-agent code delivers unsolicited retained context."
        -
          scope: "Persisted cron jobs selected on timer ticks"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
                - "runtime.md#rt-bap-scheduled-prompt"
              note: "Clock/eligibility rules deliver a stored request to a later Pi invocation."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-proactive-turn"
            - "runtime.md#rt-bap-scheduled-prompt"
          note: "A prior request schedules the job, but the later scheduler independently selects and supplies its retained prompt."
        -
          scope: "Promoted Markdown at external intended host"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-memory-promotion"
          note: "The output writer and intended reader are recorded, but no loader/selection operation establishes pull versus push."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Read-back direction cannot be completely classified."
      records:
        - "memory.md#mem-rte-recall-selection"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-obj-nugget-facts"
        - "runtime.md#rt-bap-facts-prompt"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-rte-proactive-turn"
        - "runtime.md#rt-bap-scheduled-prompt"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-rte-message-turn"
        - "memory.md#mem-rte-compaction-extract"
      note: "Both requested pull and unsolicited push are wired. Exported Markdown loading and external host continuation mechanisms are unresolved, so the boundary is not completely pull-only or completely classified."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Branch replay selecting nuggets tool-result details"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-obj-session-facts"
              note: "The tool-result name identity selects the retained facts payload to replay."
          records:
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-obj-session-facts"
          note: "Lifecycle trigger selects current-branch messages whose tool-result identity is nuggets and whose details contain facts; this selection feeds subsequent unsolicited context."
        -
          scope: "Start hydration and per-turn local-fact formatting"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-obj-nugget-facts"
                - "memory.md#mem-obj-session-facts"
                - "runtime.md#rt-bap-facts-prompt"
              note: "Availability, default kind inventory, key categories and order/budget select retained parts, without semantic relevance inference."
          records:
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-obj-nugget-facts"
            - "memory.md#mem-obj-session-facts"
            - "runtime.md#rt-bap-facts-prompt"
          note: "Session start enumerates default-kind facts and fills missing keys; before-agent formatting selects prefix groups and a final-ten-file budget, omitting underscore entries."
        -
          scope: "Cron prompt emission"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-cron-jobs"
                - "runtime.md#rt-rte-proactive-turn"
                - "runtime.md#rt-bap-scheduled-prompt"
              note: "Clock and eligibility filters select scheduled prompts for unsolicited delivery."
          records:
            - "runtime.md#rt-obj-cron-jobs"
            - "runtime.md#rt-rte-proactive-turn"
            - "runtime.md#rt-bap-scheduled-prompt"
          note: "Each tick uses enabled state and five cron fields against the clock to select retained prompts; job ID metadata/recipient routing does not itself establish identifier matching of delivered content."
        -
          scope: "Requested recall/list/overlay operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-recall-selection"
          note: "Signal classifies push selection only; lexical matching and HRR decoding on a requested return do not populate this unit."
        -
          scope: "External promoted-Markdown loader"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-memory-promotion"
          note: "No recorded consumer selection resolves its direction, trigger or targeted signal."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Read-back signal cannot be completely classified."
      records:
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-obj-nugget-facts"
        - "runtime.md#rt-bap-facts-prompt"
        - "runtime.md#rt-obj-cron-jobs"
        - "runtime.md#rt-rte-proactive-turn"
        - "runtime.md#rt-bap-scheduled-prompt"
        - "memory.md#mem-rte-recall-selection"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-memory-promotion"
        - "runtime.md#rt-rte-message-turn"
        - "memory.md#mem-rte-compaction-extract"
      note: "Known push operations use identifier and coarse selection. Requested recall lexical/numerical selectors are pull operations, not inferred push signals. Unknown loaders prevent axis inapplicability or complete coverage."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic preference/learning fragment writes with later prompt/recall consumer"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "epistemic.md#epi-rte-preference-capture"
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-rte-recall-selection"
              note: "Automatic trace-fed extraction produces retained behavior-shaping facts."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "epistemic.md#epi-rte-preference-capture"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-recall-selection"
          note: "Input activity becomes durable short guidance/context and reaches later turns; success and improved capacity remain unobserved."
        -
          scope: "Tool-result path capture with later Active Files consumer"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "memory.md#mem-rte-context-rebuild"
                - "epistemic.md#epi-obj-file-path"
              note: "Tool-call activity automatically produces durable path context."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "memory.md#mem-rte-context-rebuild"
            - "epistemic.md#epi-obj-file-path"
          note: "Captured attempted tool paths are retained and later supplied as context; source tool success is not checked."
        -
          scope: "Precompaction task extraction and selected path retention"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-obj-task-summary"
                - "memory.md#mem-rte-recall-selection"
              note: "Selected conversational traces automatically become retained _task text for later recall/list."
          records:
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-obj-task-summary"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-recall-selection"
          note: "Task text has JSON retention plus requested later consumption. Locally copied paths reach later injection, but independent durability depends on another result-hook write or host-retained details."
        -
          scope: "Automatic session-marked recall usage counters feeding promotion selection"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hit-metadata"
                - "epistemic.md#epi-rte-recall-score"
                - "runtime.md#rt-rte-memory-promotion"
              note: "Recall experience automatically updates durable counters that shape later context-placement decisions."
          records:
            - "memory.md#mem-obj-hit-metadata"
            - "epistemic.md#epi-rte-recall-score"
            - "runtime.md#rt-rte-memory-promotion"
          note: "Saved access metadata changes later promotion eligibility. Counters are not truth evidence; the resulting external Markdown consumer remains only afforded."
        -
          scope: "Explicit model remember and schedule proposal provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "runtime.md#rt-rte-schedule-admission"
            - "runtime.md#rt-obj-cron-jobs"
            - "epistemic.md#epi-obj-remember-value"
          note: "Automatic admission is known but the proposals original content may be authored, imported or trace-derived inside the uninspected model. No complete trace-fed derivation is recorded."
        -
          scope: "Initially loaded facts/jobs, generic callers and existing Markdown"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-nugget-facts"
            - "runtime.md#rt-obj-cron-jobs"
            - "memory.md#mem-obj-promoted-memory"
            - "memory.md#mem-rte-fact-mutation"
          note: "Missing original admission and derivation prevents qualifying or excluding automatic trace-fed writes."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Trace learning cannot be completely classified."
      records:
        - "memory.md#mem-rte-hook-capture"
        - "epistemic.md#epi-rte-preference-capture"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-rte-recall-selection"
        - "epistemic.md#epi-obj-file-path"
        - "memory.md#mem-rte-compaction-extract"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-obj-hit-metadata"
        - "epistemic.md#epi-rte-recall-score"
        - "runtime.md#rt-rte-memory-promotion"
        - "memory.md#mem-rte-fact-mutation"
        - "runtime.md#rt-rte-schedule-admission"
        - "runtime.md#rt-obj-cron-jobs"
        - "epistemic.md#epi-obj-remember-value"
        - "memory.md#mem-obj-nugget-facts"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-message-turn"
      note: "Known automatic trace-fed routes support yes without observed benefit. No local no finding is asserted without a bounded absence record. Model proposal provenance, some precompaction-path durability, initial content and host checkpoint production remain unresolved."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Input-hook fragment extraction from conversation turns"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "epistemic.md#epi-rte-preference-capture"
              note: "Recorded conversational input content feeds preference/learning extraction."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "epistemic.md#epi-rte-preference-capture"
          note: "Non-extension text is conversational input, including user messages; the callback wrapper does not make it an environmental event source."
        -
          scope: "Tool-result path capture"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hook-capture"
                - "epistemic.md#epi-obj-file-path"
              note: "Recorded read/edit/write call paths feed the durable fact write."
          records:
            - "memory.md#mem-rte-hook-capture"
            - "epistemic.md#epi-obj-file-path"
          note: "Paths originate in recorded tool-call inputs exposed on result events; file contents and successful outcomes are not consumed."
        -
          scope: "Precompaction task excerpt"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-obj-task-summary"
              note: "Last-three recorded user texts feed the retained task excerpt."
          records:
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-obj-task-summary"
          note: "The original inputs are selected user-message texts, not an inferred multi-step state/action/outcome trajectory."
        -
          scope: "Precompaction path-copy alternative"
          assessment: "partial"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-compaction-extract"
                - "memory.md#mem-rte-context-rebuild"
                - "memory.md#mem-obj-session-facts"
              note: "Selected tool-use paths feed copied local facts, with conditional later durability."
          records:
            - "memory.md#mem-rte-compaction-extract"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-obj-session-facts"
          note: "Original content is assistant tool-use calls, but durable later retention of the locally copied subset depends on prior capture or opaque host details."
        -
          scope: "Session-marked recall access-counter update"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hit-metadata"
                - "epistemic.md#epi-rte-recall-score"
                - "runtime.md#rt-rte-memory-promotion"
              note: "Recall access events increment a retained usage counter used by later promotion."
          records:
            - "memory.md#mem-obj-hit-metadata"
            - "epistemic.md#epi-rte-recall-score"
            - "runtime.md#rt-rte-memory-promotion"
          note: "The update consumes discrete recall activity and a caller-supplied last-session marker; origin of that marker does not establish consumption of full session logs."
        -
          scope: "Explicit model proposals, initial/generic content and external checkpoints"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-fact-mutation"
            - "runtime.md#rt-rte-schedule-admission"
            - "memory.md#mem-obj-nugget-facts"
            - "runtime.md#rt-obj-cron-jobs"
            - "memory.md#mem-obj-promoted-memory"
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-compaction-extract"
          note: "Qualifying trace learning and original content are unresolved on these branches; no trace-source value or inapplicability can be inferred from a known automatic admission."
        -
          scope: "External Pi-retained session payloads, compaction summaries and alternative checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-message-turn"
            - "memory.md#mem-rte-context-rebuild"
            - "memory.md#mem-rte-compaction-extract"
          note: "Gateway continuation and extension branch-detail access are recorded, but external host serialization, checkpoint production and later selection are uninspected; Trace source cannot be completely classified."
      records:
        - "memory.md#mem-rte-hook-capture"
        - "epistemic.md#epi-rte-preference-capture"
        - "epistemic.md#epi-obj-file-path"
        - "memory.md#mem-rte-compaction-extract"
        - "memory.md#mem-obj-task-summary"
        - "memory.md#mem-rte-context-rebuild"
        - "memory.md#mem-obj-session-facts"
        - "memory.md#mem-obj-hit-metadata"
        - "epistemic.md#epi-rte-recall-score"
        - "runtime.md#rt-rte-memory-promotion"
        - "memory.md#mem-rte-fact-mutation"
        - "runtime.md#rt-rte-schedule-admission"
        - "memory.md#mem-obj-nugget-facts"
        - "runtime.md#rt-obj-cron-jobs"
        - "memory.md#mem-obj-promoted-memory"
        - "runtime.md#rt-rte-message-turn"
      note: "Session-log content, tool traces and discrete recall access events support local findings. Session IDs alone establish neither session-log consumption by counter updates nor trajectories. Unknown model/host derivations and conditional path durability retain incomplete coverage."
---

# Nuggets memory profile

## Comparison rationale

The profile separates readable content, localized control fields and reconstructed dense numerical state. HRR is distributed-parametric form on an in-memory substrate, not a vector-service substrate or provider-weight update. Its construction and later ranking use are supported by [RT-CMP-hrr-vectors](runtime.md#rt-cmp-hrr-vectors), [EPI-RTE-recall-decode](epistemic.md#epi-rte-recall-decode) and [MEM-RTE-recall-selection](memory.md#mem-rte-recall-selection). Fact enumeration and hydration also consume the stored strings directly.

Automatic admission is independent of human input authorship. Model remember proposals, extraction hooks, operator-launched migration and threshold promotion all have software/model admission without per-content approval. Generic caller and initial-file controls remain unresolved, rather than becoming manual by default. See [MEM-RTE-fact-mutation](memory.md#mem-rte-fact-mutation), [MEM-RTE-hook-capture](memory.md#mem-rte-hook-capture), [MEM-RTE-legacy-migration](memory.md#mem-rte-legacy-migration) and [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).

Authority is consumer-relative. Fact/path text is knowledge at the model, retained preferences supply instruction, and experience supplies learning at the automatic extraction consumer. Stored keys/values and numerical state can rank recall even though the scoring algorithm is fixed. Retained counters validate and enforce promotion eligibility, not factual truth. Scheduling controls route/gate a later invocation; the retained prompt supplies its instruction. These findings do not imply epistemic acceptance or improved capacity. See [RT-BAP-facts-prompt](runtime.md#rt-bap-facts-prompt), [MEM-OBJ-hit-metadata](memory.md#mem-obj-hit-metadata), [RT-OBJ-cron-jobs](runtime.md#rt-obj-cron-jobs), [RT-BAP-scheduled-prompt](runtime.md#rt-bap-scheduled-prompt) and [EPI-ABS-truth-acceptance](epistemic.md#epi-abs-truth-acceptance).

Requested recall is pull despite automatic internal decoding. Branch-detail replay and per-turn formatting are stages of an unsolicited push chain: tool-result identity selects snapshots, while category/availability/order budgets select injected content. Cron clock matching is coarse push selection; recipient and job identifiers used for routing/metadata are not, by themselves, identity matches selecting delivered memory. The Markdown writer does not establish its external loader's direction or signal. See [MEM-RTE-context-rebuild](memory.md#mem-rte-context-rebuild), [MEM-RTE-recall-selection](memory.md#mem-rte-recall-selection), [RT-RTE-proactive-turn](runtime.md#rt-rte-proactive-turn) and [MEM-OBJ-promoted-memory](memory.md#mem-obj-promoted-memory).

Trace learning is a route classification, not demonstrated improvement. Preference/path extraction and retained task excerpts have automatic writes and later context/recall consumers. Session-marked recall also writes durable usage metadata that determines later promotion placement. Ordinary extension recall omits the enabling session ID; this route's existence does not establish activation. Tool paths copied only locally before compaction have conditional durability, so that alternative remains partial. Input-message content is session-log origin, tool-call paths are tool-trace origin, and recall access-counter inputs are discrete access events. No linked state/action/outcome sequence establishes trajectories. See [MEM-RTE-hook-capture](memory.md#mem-rte-hook-capture), [MEM-RTE-compaction-extract](memory.md#mem-rte-compaction-extract), [MEM-OBJ-task-summary](memory.md#mem-obj-task-summary), [MEM-OBJ-hit-metadata](memory.md#mem-obj-hit-metadata) and [EPI-RTE-recall-score](epistemic.md#epi-rte-recall-score).

Curation findings follow implemented transformations. Selected text reduction is consolidation, including where extraction loses qualification; that defect does not establish synthesis. Optional oldest-entry eviction is decay, overwrite is evolution, and threshold placement in exported context is promotion. Primary-key merge alone does not establish deduplication. Forget/delete lacks retained withdrawal history and therefore does not warrant invalidate. Independent unretracted snapshots and Markdown copies also prevent a global withdrawal claim. See [EPI-RTE-preference-capture](epistemic.md#epi-rte-preference-capture), [MEM-RTE-fact-mutation](memory.md#mem-rte-fact-mutation), [MEM-RTE-context-rebuild](memory.md#mem-rte-context-rebuild) and [RT-RTE-memory-promotion](runtime.md#rt-rte-memory-promotion).

Reconciliation supersedes the epistemic task-object declaration with [MEM-OBJ-task-summary](memory.md#mem-obj-task-summary), and the epistemic migration-route declaration with [MEM-RTE-legacy-migration](memory.md#mem-rte-legacy-migration). This profile uses those canonical records; supersession changes citations, not the retained extraction, lineage or consumer limits. The residual dispute about memory's attribution of older runtime wording changes no classification: the current [RT-RTE-memory-context](runtime.md#rt-rte-memory-context) and [MEM-RTE-compaction-extract](memory.md#mem-rte-compaction-extract) both slice the final twenty tool-use blocks before filtering for qualifying file operations.

All ten axes remain partial over the named inventory. External host session serialization, compaction summaries/checkpoints, initial content origins, some caller controls and external Markdown loading prevent complete classifications; known local witnesses do not resolve those alternatives. No observed or causal basis is supplied. Model parameters and static shipped guidance are not automatically part of accumulated target memory. The included opaque host continuation boundary is retained separately from the inspectable extension snapshot payload.

Source-read log: no target-source files were read for this classification. All warrants come from the supplied accepted records and their annotations; no records, quotations or new evidence were added.
