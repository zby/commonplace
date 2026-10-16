---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of llm-context-base: use-derived file knowledge and operating guidance, with optional local control and external-consumer recipes."
run-id: "AAS-2026-10-14-llm-context-base-f63a7c0fb5f2-01"
source-identity: "https://github.com/asakin/llm-context-base"
reviewed-boundary: "6d01cba8e2c22f9ca2519c70073a05cd54378a8c"
memory-comparison:
  version: 2
  scope: "Accumulated or use-revised profile/context/training observations, instructions/templates, inbox captures, optional source originals, working knowledge/projects/journal/private/blog/decision content, metadata/indexes, logs and local reload-control recipes; their admission, maintenance and later wiki/linked-code/reference-consumer routes. Initial shipped static guidance/examples are excluded as memory until use revises them; throwaway exports, host-native transcripts/summary/checkpoints/model weights, linked code bodies, and external plugin/sync/platform implementations are excluded. Opaque original and embedded artifact parts remain included with local uncertainty."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Use-derived profile/context/instructions/templates; inbox, sources, knowledge, decisions, indexes and durable logs"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-decision"
                - "memory.md#mem-obj-metadata"
                - "memory.md#mem-obj-logs"
                - "runtime.md#rt-obj-instruction-modules"
              note: "Markdown, original-format files and date/path files hold retained material."
            -
              value: "repo"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-logs"
              note: "Ordinary content and originals are Git-versionable; ignored material is not automatically committed. This is a persistence route, not a claim that every file has Git history."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-obj-instruction-modules"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-decision"
            - "memory.md#mem-obj-metadata"
            - "memory.md#mem-obj-logs"
            - "memory.md#mem-rte-pattern-capture"
          note: "All named target objects have file storage; repository persistence is conditional on tracking and committing. Ignored journal/private bodies retain the file finding."
        -
          scope: "Optional journal persistence variants"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "Plain local text, including unlocked encrypted-Git material, remains the assistant-facing object."
            -
              value: "repo"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-knowledge"
              note: "Plain Git and encrypted-Git recipes offer repository persistence, without inspected deployment."
          records:
            - "memory.md#mem-obj-knowledge"
          note: "The recipes preserve local files and optionally repository copies; underlying encryption/synchronization machinery is external."
        -
          scope: "Optional compaction sentinel and read-path log recipe"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "memory.md#mem-obj-logs"
              note: "Recipes retain a sentinel and path log in /tmp; these are file control/access state, not the opaque host summary."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "The documented local paths are known; installation and /tmp lifetime are not observed."
      records:
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-obj-instruction-modules"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-metadata"
        - "memory.md#mem-obj-logs"
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-rte-compact-reload"
      note: "The recorded inventory locates target-retained bodies, access state and optional reload control in files; tracked copies also use a repository. External sync implementations and host-native stores are excluded, not classified as service memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Readable content, learned facts/rules, decision reasoning and descriptive summaries/logs at assistant or human consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-decision"
                - "memory.md#mem-obj-metadata"
                - "memory.md#mem-obj-logs"
                - "runtime.md#rt-obj-instruction-modules"
                - "memory.md#mem-rte-pattern-capture"
                - "epistemic.md#epi-obj-blog-post"
                - "epistemic.md#epi-obj-lint-report"
              note: "Bodies, summaries, conventions, rationale and reports supply prose meaning."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-decision"
            - "memory.md#mem-obj-metadata"
            - "memory.md#mem-obj-logs"
            - "runtime.md#rt-obj-instruction-modules"
            - "memory.md#mem-rte-pattern-capture"
            - "epistemic.md#epi-obj-blog-post"
            - "epistemic.md#epi-obj-lint-report"
          note: "Natural-language meaning is interpreted by the assistant; a YAML wrapper does not change this consumption path."
        -
          scope: "Frontmatter keys/values at converter and fixed-format consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-metadata"
                - "epistemic.md#epi-rte-metadata-transform"
              note: "Regex and formatter consume localized legacy fields and produce YAML under fixed rules."
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-metadata"
              note: "YAML metadata is available to Obsidian Properties as a symbolic consumption path."
          records:
            - "memory.md#mem-obj-metadata"
            - "epistemic.md#epi-obj-metadata"
            - "epistemic.md#epi-rte-metadata-transform"
          note: "This unit covers localized metadata syntax, not semantic interpretation of summary text."
        -
          scope: "Optional sentinel and read-path hook state"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "memory.md#mem-obj-logs"
              note: "Sentinel existence selects reload; the read-path recipe copies path strings."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "Shell tests, removal and path-copying use localized strings rather than interpreting conversation meaning."
        -
          scope: "Original-format sources and embedded/linked non-prose artifacts"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
              note: "Readable original text is retained for reference or reprocessing; this does not classify every binary original."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "epistemic.md#epi-obj-blog-post"
          note: "Readable originals support natural-language form; opaque PDF, code/data/image or linked-artifact semantics and actual consumers prevent a complete form inventory."
      records:
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-metadata"
        - "memory.md#mem-obj-logs"
        - "runtime.md#rt-obj-instruction-modules"
        - "memory.md#mem-rte-pattern-capture"
        - "epistemic.md#epi-obj-blog-post"
        - "epistemic.md#epi-obj-lint-report"
        - "epistemic.md#epi-obj-metadata"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-obj-sources"
      note: "Readable text and fixed-rule metadata/control parts are classified separately. Original PDFs and linked artifacts lack recorded payload/consumer details; no parametric target memory is established."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Conversation-derived facts, conventions, observations and operating-text edits"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-obj-instruction-modules"
              note: "The assistant selects rules/preferences/details from conversation and usage observations for durable text."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-obj-instruction-modules"
          note: "The recorded trace-to-selected-text chain is prescribed; it is not observed production."
        -
          scope: "Human profile answers, manual context entries, decision documentation and direct capture edits"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-session-start"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-decision"
                - "runtime.md#rt-rte-capture-file"
              note: "Users supply profile answers and can author/edit retained context and documentation."
          records:
            - "runtime.md#rt-rte-session-start"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-decision"
            - "runtime.md#rt-rte-capture-file"
          note: "This is the explicitly described authorship path, not a conclusion that all initial content was human-authored."
        -
          scope: "Clipped inputs, preserved originals and extracted working copies"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-knowledge"
                - "runtime.md#rt-rte-capture-file"
              note: "Clips and originals enter from external content and can supply working articles."
            -
              value: "imported"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-capture-file"
              note: "The configured external clipper admits source text plus user intent; actual clipper execution is uninspected."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-rte-capture-file"
          note: "External source acquisition remains imported even when reformatted or selectively extracted; source truth is unknown."
        -
          scope: "Rebuilt metadata/title/body through bulk converter"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-metadata-migrate"
                - "epistemic.md#epi-rte-metadata-transform"
              note: "Regex collection and formatting mechanically rebuild file content without model generation."
          records:
            - "runtime.md#rt-rte-metadata-migrate"
            - "epistemic.md#epi-rte-metadata-transform"
          note: "Fixed software constructs retained output from prior file material; this finding concerns that derivation, not initial provenance."
        -
          scope: "Optional hook-produced read-path and sentinel state"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "memory.md#mem-obj-logs"
              note: "Shell callbacks construct sentinel state and copy read-path strings into log files."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "The documented hook commands construct local control/access state; original transcript/summary provenance is excluded."
        -
          scope: "Assistant-authored first takes, proposed templates/structure, approved optimization text and selected operation summaries"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-rte-pattern-capture"
                - "runtime.md#rt-rte-context-review"
                - "memory.md#mem-obj-logs"
              note: "The assistant composes commentary, proposals, revised guidance and descriptions."
          records:
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-rte-pattern-capture"
            - "runtime.md#rt-rte-context-review"
            - "memory.md#mem-obj-logs"
          note: "Authorship here concerns the documented production path; conversation-derived rule extraction is separately classified."
        -
          scope: "Initial or independently supplied working corpus, originals and embedded artifacts outside the named derivations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-sources"
            - "epistemic.md#epi-obj-blog-post"
          note: "The records do not identify every original producer or initial derivation. File shape, example content and Git versionability cannot resolve provenance."
      records:
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-obj-instruction-modules"
        - "runtime.md#rt-rte-session-start"
        - "memory.md#mem-obj-decision"
        - "runtime.md#rt-rte-capture-file"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-metadata-migrate"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-obj-logs"
        - "runtime.md#rt-rte-context-review"
        - "epistemic.md#epi-obj-blog-post"
      note: "Conversation derivation, operator authorship, imported originals and mechanical metadata compilation have distinct warrants. Unspecified initial corpus and artifact provenance remain unresolved."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Working content, personal facts, sources and decision reasoning/outcomes at answering or deliberating assistants"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-knowledge"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-decision"
                - "runtime.md#rt-rte-knowledge-query"
              note: "Selected files and past outcomes inform cited answers or decision deliberation."
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-bap-linked-context"
              note: "Preserved originals offer reference/reprocessing and linked-code readers are offered wiki architectural context."
          records:
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-decision"
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-bap-linked-context"
          note: "Content supplies context/evidence; it does not become an independent factual oracle or guaranteed decision rule."
        -
          scope: "Use-derived conventions, response preferences and revised module/template guidance at later assistant tasks"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-rte-pattern-capture"
                - "runtime.md#rt-obj-instruction-modules"
                - "runtime.md#rt-bap-instruction-load"
                - "runtime.md#rt-rte-context-review"
              note: "Retained directions request personalized behavior and govern future writing/query/maintenance."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-rte-pattern-capture"
            - "runtime.md#rt-obj-instruction-modules"
            - "runtime.md#rt-bap-instruction-load"
            - "runtime.md#rt-rte-context-review"
          note: "Standing textual directions are loaded in later sessions/tasks; compliance is unobserved."
        -
          scope: "Selected experience and observations at the conversation-fed behavioral update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
              note: "The assistant uses conversation/usage observations to revise durable behavior-shaping facts and conventions."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
          note: "This learning effect is the update path, separate from downstream guidance and from improved capacity."
        -
          scope: "Summary/tags/status and decision-outcome content at relevance/prioritization selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-metadata"
                - "memory.md#mem-obj-decision"
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-rte-lint-maintenance"
              note: "Summary/tag matching, filled outcomes and archived-status deprioritization influence which files are considered/read."
          records:
            - "memory.md#mem-obj-metadata"
            - "memory.md#mem-obj-decision"
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-rte-lint-maintenance"
          note: "Retained descriptions/features affect relative relevance; no learned scoring algorithm is implied."
        -
          scope: "Profile phase/date, project indexes, directory navigation, review date and operation history at startup/query/cadence consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-metadata"
                - "memory.md#mem-obj-logs"
                - "runtime.md#rt-rte-session-start"
                - "runtime.md#rt-rte-knowledge-query"
                - "runtime.md#rt-rte-context-review"
              note: "Retained phase, indexes and review date steer file loading, query starting points and maintenance cadence."
          records:
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-metadata"
            - "memory.md#mem-obj-logs"
            - "runtime.md#rt-rte-session-start"
            - "runtime.md#rt-rte-knowledge-query"
            - "runtime.md#rt-rte-context-review"
          note: "These retained values choose scope, input windows, questions and review timing; plain descriptive log text has no blanket authority."
        -
          scope: "Optional compaction reload flag at hook consumer"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
              note: "Presence of the sentinel triggers a re-init instruction and then removal."
          records:
            - "memory.md#mem-rte-compact-reload"
          note: "The flag changes the next-prompt reload operation, not the host compaction payload."
        -
          scope: "Use-revised instructions/templates containing completion or format criteria at subsequent candidate-check consumers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-instruction-modules"
                - "memory.md#mem-rte-pattern-capture"
                - "epistemic.md#epi-rte-completion-check"
                - "memory.md#mem-rte-lint-maintenance"
              note: "Revisable operating guidance and template conventions can supply candidate conformance/completion criteria to future assistant writing and maintenance."
          records:
            - "runtime.md#rt-obj-instruction-modules"
            - "memory.md#mem-rte-pattern-capture"
            - "epistemic.md#epi-rte-completion-check"
            - "memory.md#mem-rte-lint-maintenance"
          note: "Only the accumulated/revised criteria are memory here; initial shipped static checklist bodies remain outside memory scope. Procedural judgment is not executable enforcement."
        -
          scope: "Opaque original/embedded artifact semantics, specialized code/data/image consumption and reprocessing outputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "epistemic.md#epi-obj-blog-post"
          note: "The records establish reference roles but not all downstream artifact consumers/effects. No enforcement or parametric learning authority is inferred."
      records:
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-knowledge-query"
        - "memory.md#mem-bap-linked-context"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-rte-pattern-capture"
        - "runtime.md#rt-obj-instruction-modules"
        - "runtime.md#rt-bap-instruction-load"
        - "runtime.md#rt-rte-context-review"
        - "memory.md#mem-obj-metadata"
        - "memory.md#mem-rte-lint-maintenance"
        - "memory.md#mem-obj-logs"
        - "runtime.md#rt-rte-session-start"
        - "memory.md#mem-rte-compact-reload"
        - "epistemic.md#epi-rte-completion-check"
        - "epistemic.md#epi-obj-blog-post"
      note: "Known effects are local to actual consumers: evidence, guidance, relevance selection, routing and procedural admission criteria. Unspecified artifact consumers and original reprocessing effects prevent complete authority coverage; host permissions and static criteria are not treated as learned memory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Initial profile answers, human/editor context and capture/journal entry, explicit file destinations and filing decisions"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-session-start"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-knowledge"
              note: "The human supplies/edits content or chooses retained disposition."
            -
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-capture-file"
              note: "Obsidian and clipper configurations offer human-authored capture and user-filled intent outside assistant admission."
          records:
            - "runtime.md#rt-rte-session-start"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-knowledge"
          note: "These mechanisms have explicit operator content supply/edit/disposition; they do not establish human review of every model-generated sentence."
        -
          scope: "Clear conversation-pattern writes, observation-log updates, extraction/drafting and item-level source preservation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-sources"
              note: "Models select and write clear learned rules/facts, observations and extracted working content; preservation importance is item-level model judgment."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-sources"
          note: "Assistant admission follows the request/setting without a universal per-content human decision; ambiguous capture and approved structures are a separate branch."
        -
          scope: "Ambiguous pattern capture, new directories and instruction restructuring after approval"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "runtime.md#rt-rte-context-review"
              note: "Ambiguity questions, directory approval and mandatory restructuring approval gate the corresponding retained changes."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "runtime.md#rt-rte-context-review"
          note: "The human explicitly decides these proposed changes, unlike clear immediate rule capture."
        -
          scope: "Lint/format/status/index/log updates not requiring per-item approval, and human-resolved cleanup"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-lint-maintenance"
                - "epistemic.md#epi-rte-completion-status"
                - "epistemic.md#epi-rte-completion-links"
                - "memory.md#mem-obj-logs"
              note: "The assistant can apply format fixes, judged-complete status/index/link changes and operation summaries."
            -
              value: "manual"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-lint-maintenance"
              note: "Deletion/overwrite restrictions and manual broken-link resolution require explicit operator involvement on their branches."
          records:
            - "memory.md#mem-rte-lint-maintenance"
            - "epistemic.md#epi-rte-completion-status"
            - "epistemic.md#epi-rte-completion-links"
            - "memory.md#mem-obj-logs"
          note: "Conditional instructions distinguish automatic requested edits from user-controlled disposition; no universal approval invariant is inferred."
        -
          scope: "Individual matching-file admission by metadata converter"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-metadata-migrate"
                - "epistemic.md#epi-rte-metadata-transform"
              note: "Software admits mechanically rebuilt file contents."
          records:
            - "runtime.md#rt-rte-metadata-migrate"
            - "epistemic.md#epi-rte-metadata-transform"
          note: "The caller selects invocation/root; fixed code selects and overwrites individual matches without per-file approval."
        -
          scope: "Optional sentinel and read-path hook writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "memory.md#mem-obj-logs"
              note: "Documented hook commands produce and remove control/path state."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "Installation is an operator choice, but callback writes do not require per-record content approval."
        -
          scope: "Outcome reporting, saving query syntheses and specialized publication/status/URL admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-decision"
            - "runtime.md#rt-rte-knowledge-query"
            - "epistemic.md#epi-rte-blog-publish"
          note: "Outcome entry timing/control is unspecified; a save decision is distinct from actual content approval; external author/assistant/platform roles do not establish who admits each published or tracked retained part. Manual versus automatic admission cannot be completely assigned."
      records:
        - "runtime.md#rt-rte-session-start"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-rte-capture-file"
        - "memory.md#mem-obj-knowledge"
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-context-review"
        - "memory.md#mem-rte-lint-maintenance"
        - "epistemic.md#epi-rte-completion-status"
        - "epistemic.md#epi-rte-completion-links"
        - "memory.md#mem-obj-logs"
        - "runtime.md#rt-rte-metadata-migrate"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-obj-decision"
        - "runtime.md#rt-rte-knowledge-query"
        - "epistemic.md#epi-rte-blog-publish"
      note: "The named target admission inventory distinguishes explicit content decisions from automatic model/software admission. Starting capture, migration or a session is not blanket content approval. Unspecified outcome, saved-synthesis and publication admissions prevent complete coverage; external host summary writes are excluded."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Conversation-derived selected facts/rules and clip/source extraction into reduced working text"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-knowledge"
              note: "The assistant selects observations/rules and extracts what matters instead of filing full raw HTML."
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-context"
              note: "Later corrections replace current preferences/conventions and update existing context."
            -
              value: "decay"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-sources"
              note: "Default post-filing disposal forgets the inbox original when preservation is disabled; this does not establish an automatic seven-day TTL."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-knowledge"
          note: "Reduction of existing conversational/source content is consolidation, including when original retention is optional. No new claim is inferred from extraction defects."
        -
          scope: "Approved instruction restructuring/compaction and conditional loading edits"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-context-review"
              note: "The optimization procedure can compact repeated guidance into reduced text."
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-context-review"
                - "runtime.md#rt-obj-instruction-modules"
              note: "Approved edits revise existing operating instructions/loading organization."
          records:
            - "runtime.md#rt-rte-context-review"
            - "runtime.md#rt-obj-instruction-modules"
          note: "This is instruction maintenance, not host transcript compaction or demonstrated context-efficiency improvement."
        -
          scope: "Content/metadata cleanup, completion and retirement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-lint-maintenance"
                - "memory.md#mem-obj-metadata"
                - "epistemic.md#epi-rte-completion-links"
              note: "Cleanup revises existing metadata, links and content organization."
            -
              value: "promote"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-completion-status"
              note: "Draft-to-active/complete disposition raises the retained item to in-use status under the checklist."
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-lint-maintenance"
                - "memory.md#mem-obj-metadata"
              note: "Archive/supersede withdraws active reliance while preserving history/replacement reasons."
            -
              value: "decay"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-rte-lint-maintenance"
              note: "Archived status usually reduces retrieval priority; this is bounded downweighting, not a seven-day deletion timer."
          records:
            - "memory.md#mem-rte-lint-maintenance"
            - "memory.md#mem-obj-metadata"
            - "epistemic.md#epi-rte-completion-status"
            - "epistemic.md#epi-rte-completion-links"
            - "runtime.md#rt-rte-knowledge-query"
          note: "Separate effects coexist: revision, raised lifecycle tier, withdrawal of current reliance and reduced retrieval priority. No enforced universal withdrawal is claimed."
        -
          scope: "Mechanical legacy-metadata conversion alone"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-metadata-migrate"
            - "epistemic.md#epi-rte-metadata-transform"
          note: "Format conversion, key overwrite and leading-material loss alone establish none of the controlled semantic curation operations. This is not deduplication or synthesis."
        -
          scope: "Saved query syntheses, assistant first takes and opaque original/artifact reprocessing"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-query"
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
          note: "No concrete semantic input/output record decides consolidation versus creation of a claim absent from inputs. A route called synthesis does not establish synthesize; no dedup witness is recorded."
      records:
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-obj-config"
        - "runtime.md#rt-rte-capture-file"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-context-review"
        - "runtime.md#rt-obj-instruction-modules"
        - "memory.md#mem-rte-lint-maintenance"
        - "memory.md#mem-obj-metadata"
        - "epistemic.md#epi-rte-completion-status"
        - "epistemic.md#epi-rte-completion-links"
        - "runtime.md#rt-rte-knowledge-query"
        - "runtime.md#rt-rte-metadata-migrate"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-obj-sources"
      note: "Prescribed transformations retain claimed bases; mechanical metadata conversion supplies no curation value merely because it rewrites bytes. Saved answer synthesis and opaque artifact transformations remain semantically indeterminate."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "User knowledge/status query and returned selected-content synthesis"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-obj-logs"
                - "memory.md#mem-obj-knowledge"
              note: "A user question initiates content selection and cited answer delivery."
          records:
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-logs"
            - "memory.md#mem-obj-knowledge"
          note: "The return satisfies a request for retained material; code delivery is not counted as an additional push."
        -
          scope: "Session startup and task-triggered retained guidance/template/context loading"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-session-start"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-obj-instruction-modules"
                - "memory.md#mem-rte-pattern-capture"
                - "runtime.md#rt-bap-instruction-load"
              note: "The prescribed automatic foreground selector supplies accumulated context and current rules based on phase and task trigger."
          records:
            - "runtime.md#rt-rte-session-start"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-obj-instruction-modules"
            - "memory.md#mem-rte-pattern-capture"
            - "runtime.md#rt-bap-instruction-load"
          note: "A user initiating a task/session is not a separate request to retrieve all learned preferences and guidance."
        -
          scope: "Decision-context precedent and failure-constraint supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-obj-decision"
              note: "The assistant surfaces relevant completed outcomes when the conversation concerns a decision."
          records:
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-decision"
          note: "This branch proactively selects outcome-bearing past decisions without a separate retrieval request."
        -
          scope: "Old-inbox startup nudge and review-date cadence supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-logs"
                - "memory.md#mem-rte-lint-maintenance"
                - "runtime.md#rt-rte-context-review"
              note: "Startup age checks surface captures; stored review date selects an overdue-review nudge."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-logs"
            - "memory.md#mem-rte-lint-maintenance"
            - "runtime.md#rt-rte-context-review"
          note: "Age/date control state prompts triage or review without a dedicated request for those retained entries."
        -
          scope: "Optional post-compaction reinjection and durable-file reload"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "runtime.md#rt-rte-session-start"
              note: "Sentinel-triggered re-init instructs the assistant to reload retained file guidance/context."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "runtime.md#rt-rte-session-start"
          note: "The next-prompt callback supplies re-init without a separate request to retrieve retained wiki context."
        -
          scope: "Linked-code consultation and optional preserved-original reprocessing"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-bap-linked-context"
            - "memory.md#mem-obj-sources"
          note: "A documented external reader/reprocessing role establishes read-back affordances, but the records do not fully separate explicit requests from automatic selected supply. No installed caller is supplied."
      records:
        - "runtime.md#rt-rte-knowledge-query"
        - "memory.md#mem-obj-logs"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-session-start"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-obj-instruction-modules"
        - "memory.md#mem-rte-pattern-capture"
        - "runtime.md#rt-bap-instruction-load"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-rte-lint-maintenance"
        - "runtime.md#rt-rte-context-review"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-bap-linked-context"
        - "memory.md#mem-obj-sources"
      note: "The file loop includes requested retrieval and automatic startup/task/precedent supply. Optional linked-code consultation and source reprocessing lack fully specified request/selection chains; these unresolved included routes prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Startup and task-triggered accumulated context/guidance supply"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-session-start"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-obj-instruction-modules"
                - "runtime.md#rt-bap-instruction-load"
              note: "Broad phase and task conditions select retained bodies rather than matching a stored fact identity."
            -
              value: "inferred-judgment"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "runtime.md#rt-rte-session-start"
                - "memory.md#mem-obj-config"
              note: "The assistant interprets task triggers and training history to choose appropriate learned guidance, tips and questions."
          records:
            - "runtime.md#rt-rte-session-start"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-obj-instruction-modules"
            - "runtime.md#rt-bap-instruction-load"
            - "memory.md#mem-rte-pattern-capture"
          note: "Trigger is session start or a routed task; phase/date/manual override and task category select current profile/context/rules or relevant module/template bodies."
        -
          scope: "Decision-context push of completed outcomes and constraints"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-obj-decision"
                - "memory.md#mem-obj-metadata"
              note: "Domain/topic and tag/summary matching supplies relevance inputs for precedent selection."
            -
              value: "inferred-judgment"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-knowledge-query"
                - "memory.md#mem-obj-decision"
              note: "The foreground assistant judges which past outcome/constraints are relevant to the current decision."
          records:
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-decision"
            - "memory.md#mem-obj-metadata"
          note: "Trigger is a decision conversation; topic/domain, summaries/tags and filled Outcome content select retained decision parts within the 1–3-file budget."
        -
          scope: "Startup inbox-age and optimization-date nudges"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-logs"
                - "memory.md#mem-rte-lint-maintenance"
                - "runtime.md#rt-rte-context-review"
              note: "Seven-day inbox and thirty-day review conditions select age-bounded retained state."
          records:
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-logs"
            - "memory.md#mem-rte-lint-maintenance"
            - "runtime.md#rt-rte-context-review"
          note: "Startup/cadence checks read dates/age and select old captures or the overdue-review state; thresholds do not target semantic facts."
        -
          scope: "Optional post-compaction reload"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-compact-reload"
                - "runtime.md#rt-rte-session-start"
              note: "Presence test selects re-init, not an identity match over delivered retained facts."
          records:
            - "memory.md#mem-rte-compact-reload"
            - "runtime.md#rt-rte-session-start"
          note: "Trigger is next prompt after manual compaction; sentinel availability selects the reload instruction, then startup conditions select file bodies."
        -
          scope: "Requested knowledge/status answer"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-logs"
          note: "This unit is a requested pull return; its relevance selection is not push selection."
        -
          scope: "External linked-code/original-reprocessing routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-bap-linked-context"
            - "memory.md#mem-obj-sources"
          note: "The records do not specify every automatic selector, trigger or selected payload; known local push routes do not resolve these alternatives."
      records:
        - "runtime.md#rt-rte-session-start"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-obj-instruction-modules"
        - "runtime.md#rt-bap-instruction-load"
        - "memory.md#mem-rte-pattern-capture"
        - "runtime.md#rt-rte-knowledge-query"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-metadata"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-logs"
        - "memory.md#mem-rte-lint-maintenance"
        - "runtime.md#rt-rte-context-review"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-bap-linked-context"
        - "memory.md#mem-obj-sources"
      note: "Classified push routes use coarse control state, topic/tag lexical inputs and model judgment. Pull-only query operations need no push signal. The external consultation/reprocessing chains remain unresolved; file paths alone do not establish identifier-based push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Immediate patterns, training observations and conversation-derived personal context/instructions/templates"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-bap-instruction-load"
              note: "Automatic selection/write of clear observations and patterns produces durable behavior-shaping text for later consumers. Explicitly approved ambiguous/structural branches remain separately manual."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-bap-instruction-load"
          note: "Live conversational turns and usage observations feed selected retained text that later sessions/tasks are instructed to consume. This axis requires neither observed improvement nor parametric learning."
        -
          scope: "Assistant conversation capture/extraction into retained working knowledge"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-knowledge"
                - "runtime.md#rt-rte-knowledge-query"
              note: "Recorded conversation-to-derived working text can be retained and later supplied as knowledge context. Human filing disposition is distinct from automatic draft/extraction admission."
          records:
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-knowledge"
            - "runtime.md#rt-rte-knowledge-query"
          note: "This unit covers the automatic conversational branch, not independently imported clips or raw manual parking."
        -
          scope: "Explicit human entry/approval and purely mechanical metadata conversion"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-rte-session-start"
            - "runtime.md#rt-rte-context-review"
            - "runtime.md#rt-rte-metadata-migrate"
            - "epistemic.md#epi-rte-metadata-transform"
          note: "Manual content decisions are not automatic trace-fed writes; the converter consumes file metadata rather than activity traces to learn durable behavior. No local no is inflated into a system-wide absence."
        -
          scope: "Sentinel and read-path logging without a recorded automatic behavioral-update consumer"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "Raw control/path logging alone is not qualifying learning. The records disclose no automatic path-log-to-guidance pipeline; sentinel re-init reloads existing files rather than producing a conversation summary."
        -
          scope: "Decision-outcome updates, saved query syntheses, operation/report summaries and source-derived knowledge of unspecified origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-decision"
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-logs"
            - "epistemic.md#epi-obj-lint-report"
          note: "Outcome reporting has no mandatory automatic write schedule; synthesis save and original source content/admission are not fully identified. Operation summaries and logged issue counts have later status/provenance readers, but the original trace inputs to their writes are unspecified. These missing chains prevent classification of additional qualifying automatic trace-fed writes."
      records:
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-bap-instruction-load"
        - "runtime.md#rt-rte-capture-file"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-knowledge-query"
        - "runtime.md#rt-rte-session-start"
        - "runtime.md#rt-rte-context-review"
        - "runtime.md#rt-rte-metadata-migrate"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-obj-logs"
        - "memory.md#mem-obj-decision"
        - "memory.md#mem-obj-sources"
        - "epistemic.md#epi-obj-lint-report"
      note: "Conversation-fed durable behavioral writes are positively supported at the claimed layer. Other named routes are nonqualifying or have unresolved automatic-write/input chains; these limits prevent a system-wide negative or complete trace-route inventory."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Qualifying automatic conversation pattern/training/context and conversation-to-working-knowledge writes"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-pattern-capture"
                - "memory.md#mem-obj-config"
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-rte-capture-file"
                - "memory.md#mem-obj-inbox"
                - "memory.md#mem-obj-knowledge"
              note: "The recorded chain starts from live session exchanges and writes selected durable text for future reads. Raw transcript retention by the target is not required."
          records:
            - "memory.md#mem-rte-pattern-capture"
            - "memory.md#mem-obj-config"
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-rte-capture-file"
            - "memory.md#mem-obj-inbox"
            - "memory.md#mem-obj-knowledge"
          note: "Original inputs are user/assistant conversational turns and usage observations; retained selected logs are derived products, not an additional trace-source kind."
        -
          scope: "Manual content admission, mechanical metadata conversion and raw control/path-log retention"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-rte-context-review"
            - "runtime.md#rt-rte-metadata-migrate"
            - "epistemic.md#epi-rte-metadata-transform"
            - "memory.md#mem-rte-compact-reload"
            - "memory.md#mem-obj-logs"
          note: "These named routes do not establish a qualifying automatic trace-fed behavioral write, so they have no learning trace source."
        -
          scope: "Potential additional outcome/synthesis/operation-report/original-source learning routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-decision"
            - "runtime.md#rt-rte-knowledge-query"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-knowledge"
            - "memory.md#mem-obj-logs"
            - "epistemic.md#epi-obj-lint-report"
          note: "Neither every qualifying automatic admission nor original input origin is fully recorded. Outcome prose, summaries of file operations and arbitrary imported originals cannot be labeled trajectories, event-streams or tool-traces from file names alone."
      records:
        - "memory.md#mem-rte-pattern-capture"
        - "memory.md#mem-obj-config"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-rte-capture-file"
        - "memory.md#mem-obj-inbox"
        - "memory.md#mem-obj-knowledge"
        - "runtime.md#rt-rte-context-review"
        - "runtime.md#rt-rte-metadata-migrate"
        - "epistemic.md#epi-rte-metadata-transform"
        - "memory.md#mem-rte-compact-reload"
        - "memory.md#mem-obj-logs"
        - "memory.md#mem-obj-decision"
        - "runtime.md#rt-rte-knowledge-query"
        - "memory.md#mem-obj-sources"
        - "epistemic.md#epi-obj-lint-report"
      note: "The positive conversation-fed routes originate in session turns, not in an event-stream merely because selected observations become log entries. Unspecified outcome/source/synthesis inputs retain local uncertainty."
---

# llm-context-base memory profile

## Comparison rationale

The profile classifies the accepted file loop, not all storage or guidance of its external host. The inventory is grounded in the object and route records, especially [MEM-OBJ-knowledge](memory.md#mem-obj-knowledge), [MEM-RTE-pattern-capture](memory.md#mem-rte-pattern-capture), and the annotated [RT-RTE-session-start](runtime.md#rt-rte-session-start), [RT-RTE-capture-file](runtime.md#rt-rte-capture-file) and [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query). Known coverage does not upgrade doctrine to wiring. Most findings remain claimed; documented integrations retain afforded bases; the converter alone supplies the relevant wired transformation/admission witness. No finding is observed or causally supported.

Reconciliation supersedes EPI-OBJ-sources with [MEM-OBJ-sources](memory.md#mem-obj-sources), and EPI-RTE-pattern-capture with [MEM-RTE-pattern-capture](memory.md#mem-rte-pattern-capture). Accordingly, this profile cites those canonical memory declarations. The narrower metadata transformation remains [EPI-RTE-metadata-transform](epistemic.md#epi-rte-metadata-transform), alongside its valid invocation container [RT-RTE-metadata-migrate](runtime.md#rt-rte-metadata-migrate). Other valid containers and their parts are not treated as replacement identities.

### Retained parts and consumers

Filesystem and repository persistence can coexist. The repository value is conditional: [MEM-OBJ-knowledge](memory.md#mem-obj-knowledge) records ignored journal/private bodies and optional plain/encrypted Git recipes. Encryption is an encoding/access arrangement, not an additional controlled storage substrate. The optional sentinel and read-path log are local control/access state, not a readable representation of the host summary. The excluded host payload cannot be classified from the inspected sentinel. Opaque original-format sources and embedded artifacts remain included: their file substrate is known while their full forms, provenance and consumers are not.

Natural-language summaries and guidance remain natural language at the assistant consumer even when stored in YAML or Markdown. Fixed-rule metadata conversion and shell sentinel/path operations support separate symbolic consumption paths. [MEM-OBJ-metadata](memory.md#mem-obj-metadata) and [EPI-OBJ-metadata](epistemic.md#epi-obj-metadata) support this distinction. No external assistant weights are included as accumulated target memory.

Authority follows the actual effect. Outcome text supplies knowledge in decision deliberation; summaries/tags/status influence ranking; phase/index/date state supplies routing. The pattern update uses experience for learning, while its retained directions supply instruction at [RT-BAP-instruction-load](runtime.md#rt-bap-instruction-load). These distinct paths do not prove improved capacity. Use-revised checklist/template guidance can supply validation criteria, but [EPI-RTE-completion-check](epistemic.md#epi-rte-completion-check) supplies only a procedural accuracy/completion criterion, not factual acceptance or executable enforcement. Initial static schemas and host permission settings do not become memory merely by being loaded.

### Admission and transformations

Explicit human answers/edits/approvals are manual. Clear pattern capture and item-level model extraction are automatic despite upstream user initiation; ambiguous pattern admission, directory creation and optimization restructuring have explicit approval branches. [MEM-RTE-pattern-capture](memory.md#mem-rte-pattern-capture) and [RT-RTE-context-review](runtime.md#rt-rte-context-review) preserve those controls. The converter's per-file admission is automatic even though the operator launches the batch. Its rewrite is other-compiled lineage, not trace learning.

Consolidation describes selected observations and reduced source content. Optimization compaction concerns revised instructions, not opaque host conversation summaries. Retirement supports withdrawal of current reliance and reduced priority, not enforced exclusion. Draft-to-active completion supports promotion at the claimed lifecycle layer. [MEM-RTE-lint-maintenance](memory.md#mem-rte-lint-maintenance) retains conflicting link/metadata/discard wording; the profile therefore asserts neither a universal schema validator nor a seven-day deletion mechanism. [EPI-RTE-metadata-transform](epistemic.md#epi-rte-metadata-transform) records byte/meaning loss, but fixed conversion or a faithfulness defect alone does not establish deduplication or synthesis. The semantically unspecified saved-answer route remains indeterminate rather than acquiring synthesize from its name.

### Read-back and trace-fed writes

Requested answers are pull; startup/task guidance, overdue nudges and proactive precedents are push. The latter uses topic/domain and summary/tag signals plus model judgment; broad phase/age/sentinel conditions remain coarse. Named paths are not sufficient evidence for identifier-based targeted push. The file/line budget bounds delivered material, not storage or complete corpus coverage. Linked-code consultation and original reprocessing remain afforded consumers with unresolved request/selection detail, as recorded in [MEM-BAP-linked-context](memory.md#mem-bap-linked-context) and [MEM-OBJ-sources](memory.md#mem-obj-sources).

Conversation-fed automatic retained facts/rules and derived knowledge qualify for trace_learning yes at the claimed layer because the records connect their session inputs, durable products and later consumers. This classification neither requires new claims nor asserts successful improvement. Manual branches and metadata conversion do not qualify; raw control/path logging alone also does not qualify. Unspecified outcome-writing and saved-synthesis/source-input chains prevent complete enumeration. No local no or absence is asserted without a bounded warrant. Original conversational input maps to session-logs, not event-streams because a selected observation is written into a training or operation log. [MEM-RTE-compact-reload](memory.md#mem-rte-compact-reload) establishes only reload around an excluded opaque host compactor, not an additional trace-to-summary writer.

### Source-read log

No frozen-source files were read for this profile. All classifications use the supplied accepted records and annotations, resolved through the supplied reconciliation. No evidence or record was added, and no report verification was reopened.
