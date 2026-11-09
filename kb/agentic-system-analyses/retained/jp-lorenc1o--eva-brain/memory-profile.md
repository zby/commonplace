---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Eva-brain memory profile: Git-backed wiki curation, settings, saved analyses and operation-log eligibility at the frozen desktop boundary."
run-id: "AAS-2026-11-09-eva-brain-de4240cd9e79-01"
source-identity: "https://github.com/jp-lorenc1o/eva-brain"
reviewed-boundary: "706fb91f4ee851cc355785f4e7c6eab37146938f"
memory-comparison:
  version: 2
  scope: "Eva-owned retained raw inputs, maintained wiki prose and access metadata, saved analyses, accumulated operation log, and use-modified instruction/profile/manifest state, including their admission and later-consumer routes. Includes unresolved initial/imported provenance and arbitrary raw payloads. Excludes unchanged shipped instructions/starter files, temporary proposal frames, ordinary current-task state and reconstructed graph objects as independent accumulated stores, and external runtime histories, host compaction, provider memory and weights."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Eva's retained raw sources, wiki prose and symbolic metadata, operation log, and use-modified contract/manifest"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-knowledge-pages"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-analyses"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-brain-settings"
              note: "The operative retained parts live as local files; Markdown is encoding, not a separate substrate."
            -
              value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-analysis-save"
                - "runtime.md#rt-rte-brain-settings"
                - "memory.md#mem-obj-log"
              note: "Git commits retain admitted wiki, source, log and settings history."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-analyses"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-brain-settings"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-analysis-save"
          note: "The accepted inventory covers retained files and their Git backing. Parsed adjacency and UI graphs are reconstructed access structures, not an independently accumulated graph store."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-knowledge-pages"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-analyses"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-brain-settings"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-analysis-save"
      note: "Known for Eva-owned retained memory. Temporary worktrees, reconstructed process state and external provider/runtime stores are not additional retained-memory substrates here."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Wiki prose, source digests, saved answer prose, operation descriptions and changed human guidance at model/person consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge-pages"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-analyses"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-bap-vault-contract"
                - "memory.md#mem-bap-wiki-evidence"
              note: "Models and people interpret page prose, log descriptions and retained guidance."
          records:
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-analyses"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-bap-vault-contract"
            - "memory.md#mem-bap-wiki-evidence"
          note: "The natural-language parts are distinct from parser fields and dispatch controls."
        -
          scope: "Persisted page identifiers, links and frontmatter; source-name occurrence in the log; manifest dispatch values"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-brain-settings"
              note: "Parser/graph rules consume localized metadata; enqueue matches filename strings; Rust parses configuration for dispatch."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-brain-settings"
          note: "Natural-language titles/aliases also have literal software matching roles."
        -
          scope: "Textual raw document content"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
              note: "The recorded text-document branch supplies source assertions for model interpretation."
          records:
            - "memory.md#mem-obj-raw"
          note: "This finding covers textual inputs only."
        -
          scope: "Other arbitrary selected raw payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
          note: "The retained bytes are included but their operative encodings and model consumption are not established for every format."
      records:
        - "memory.md#mem-obj-knowledge-pages"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-analyses"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-bap-vault-contract"
        - "memory.md#mem-bap-wiki-evidence"
        - "memory.md#mem-obj-page-metadata"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-raw"
      note: "The inspected paths establish text and symbolic consumption, not dense learned memory representations. Arbitrary raw payloads prevent complete form coverage; external model parameters are outside this memory inventory."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Raw acquisition and initially imported wiki/instruction content: import path"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-knowledge-pages"
                - "runtime.md#rt-rte-brain-settings"
              note: "Source copying and vault import preserve pre-existing content; import does not authenticate its original authorship."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-knowledge-pages"
            - "runtime.md#rt-rte-brain-settings"
          note: "Known import path, not known historical provenance."
        -
          scope: "Subsequent model-created or revised wiki prose"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge-pages"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-analyses"
                - "runtime.md#rt-rte-source-ingest"
              note: "External models propose new pages and revisions under the retained contract; the branch gate admits the files."
          records:
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-analyses"
            - "runtime.md#rt-rte-source-ingest"
          note: "Authored transformation is established as a route; actual semantic fidelity is not."
        -
          scope: "Saved-analysis output derived by the Rust answer formatter, including its constructed reference metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-analyses"
                - "epistemic.md#epi-rte-analysis-format"
              note: "Rust constructs analysis Markdown and selected reference metadata from supplied answer products by trimming, formatting and filtering."
          records:
            - "memory.md#mem-obj-analyses"
            - "epistemic.md#epi-rte-analysis-format"
          note: "Known only for this formatter derivation, not initial answer provenance or metadata elsewhere. Formatting does not establish newly synthesized answer claims."
        -
          scope: "Persisted identifiers, frontmatter and links outside the saved-analysis formatter output"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-knowledge-pages"
            - "runtime.md#rt-rte-brain-settings"
          note: "The records establish persisted syntax and its symbolic consumption, but do not resolve the derivation of each retained metadata part in imported, model-authored or preserved pages. Parser and graph reconstruction do not establish compiled lineage for the files they read."
        -
          scope: "Operation entries accumulated from ingest outcomes and rejection decisions"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "Eva appends operation, subject and result/summary content arising from task activity."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-source-ingest"
          note: "This covers operation-derived entries, not an inferred full conversation transcript."
        -
          scope: "Historical authorship of imported pages, summaries and preserved instruction files; arbitrary raw provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "runtime.md#rt-rte-brain-settings"
          note: "Preservation and import do not resolve the original authoring/derivation path."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-knowledge-pages"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-analyses"
        - "runtime.md#rt-rte-source-ingest"
        - "epistemic.md#epi-rte-analysis-format"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-log"
      note: "Known subsequent authoring, import and formatting do not resolve initial provenance. Bootstrap's shipped static seed is not classified as accumulated use-memory."
    behavioral_authority:
      assessment: "known"
      units:
        -
          scope: "Retained wiki and raw evidence delivered to later ingest/query/advisory models and people"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-bap-wiki-evidence"
                - "memory.md#mem-obj-analyses"
                - "memory.md#mem-rte-mcp-navigation"
              note: "Subject content supplies evidence/context, without a truth or compliance guarantee."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-bap-wiki-evidence"
            - "memory.md#mem-obj-analyses"
            - "memory.md#mem-rte-mcp-navigation"
          note: "Saved analyses enter the same downstream evidence path as other admitted pages."
        -
          scope: "Retained title/stem/alias/body content at MCP search scoring"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-rte-mcp-navigation"
              note: "Lexical retained content contributes to scores and relative top-ten priority, even though scoring code is fixed."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-rte-mcp-navigation"
          note: "A separate effect from the returned content's knowledge authority."
        -
          scope: "Page metadata and explicit links at resolution, graph traversal and structural checking"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-rte-mcp-navigation"
              note: "Retained identifiers and links determine which page or graph path a request resolves to."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-rte-mcp-navigation"
          note: "Metadata is the checked object at lint, not itself a retained validation criterion; static lint code is excluded from the memory boundary."
        -
          scope: "Use-modified retained contract/profile guidance at later model tasks"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-vault-contract"
                - "runtime.md#rt-rte-brain-settings"
              note: "Retained language, purpose and profile guidance supplies standing task directions."
          records:
            - "runtime.md#rt-bap-vault-contract"
            - "runtime.md#rt-rte-brain-settings"
          note: "Instruction delivery does not establish adherence."
        -
          scope: "Retained manifest/runtime/model configuration at Rust dispatch"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-brain-settings"
              note: "Configuration selects later adapter/model and task framing."
          records:
            - "runtime.md#rt-rte-brain-settings"
          note: "This concerns parsed choices rather than external model weights."
        -
          scope: "Accumulated log at source eligibility filtering"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "Source-name presence determines whether work is queued."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "The filename-substring rule removes matching candidates, including prior rejections; it is a software veto."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "The retained matching text is the criterion for admitting a candidate source to the queue."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-source-ingest"
          note: "The same predicate has criterion, veto and scheduling consequences; it is not semantic endorsement."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-bap-wiki-evidence"
        - "memory.md#mem-obj-analyses"
        - "memory.md#mem-rte-mcp-navigation"
        - "memory.md#mem-obj-page-metadata"
        - "runtime.md#rt-bap-vault-contract"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-source-ingest"
      note: "Known for the recorded Eva consumers of retained evidence, access metadata, changed guidance/configuration and log eligibility state. No learning authority is inferred merely from retention; static gate criteria and transient issue lists are excluded."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Clean ingest proposal admission and Eva-owned operation-log append"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-log"
              note: "Software admits mechanically clean model edits and appends operational state without a per-content operator approval."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-log"
          note: "Starting ingest is not approval of every resulting page."
        -
          scope: "Held ingest edits, saved query/profile analyses, and shipped UI settings changes"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-analysis-save"
                - "runtime.md#rt-rte-brain-settings"
              note: "Shipped UI supplies explicit accept/reject or content-setting decisions; saved analyses require review."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-analysis-save"
            - "runtime.md#rt-rte-brain-settings"
          note: "The finding is bounded to human-operated UI paths, not every command caller."
        -
          scope: "Selected raw files through the human UI"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
              note: "The person explicitly chooses source content for acquisition."
          records:
            - "memory.md#mem-obj-raw"
          note: "This does not cover discovery of arbitrary predeposited files."
        -
          scope: "Manually deposited/discovered raw, generic command callers, and preserved initial wiki/instruction admissions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-rte-analysis-save"
            - "runtime.md#rt-rte-brain-settings"
            - "memory.md#mem-obj-knowledge-pages"
          note: "Caller identity and initial control do not establish an explicit human content decision or its absence."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-analysis-save"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-knowledge-pages"
      note: "Software and explicit UI-human admission coexist. Unknown initial and generic-caller control prevents uniformly manual or automatic coverage."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Requested model production of source digests and integration into existing wiki pages"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-knowledge-pages"
                - "runtime.md#rt-rte-source-ingest"
              note: "The source-digest and merge-existing instructions afford compressed/integrated representations of existing source claims."
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-knowledge-pages"
                - "runtime.md#rt-rte-source-ingest"
              note: "The model is explicitly directed to revise existing pages as sources arrive."
            -
              value: "dedup"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-knowledge-pages"
                - "runtime.md#rt-rte-source-ingest"
              note: "Search-before-write and merge-over-duplicate guidance affords combining overlapping entries rather than creating duplicates."
          records:
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-knowledge-pages"
            - "runtime.md#rt-rte-source-ingest"
          note: "These are afforded model curation under instructions, not observed faithful transformations or deterministic semantic implementations."
        -
          scope: "Actual semantic transformation of model-produced analyses and revisions, including new-claim synthesis"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-analyses"
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "runtime.md#rt-rte-source-ingest"
          note: "No concrete source/output pair establishes which claims were merely combined versus newly created. A synthesis label alone cannot establish synthesize."
        -
          scope: "Rust formatting, access reconstruction and eligibility filtering"
          assessment: "inapplicable"
          findings: []
          records:
            - "epistemic.md#epi-rte-analysis-format"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-log"
          note: "Formatting, rebuilding access structures and suppressing source enqueue do not by themselves transform retained claims through one of the controlled curation operations."
      records:
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-knowledge-pages"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-analyses"
        - "epistemic.md#epi-rte-analysis-format"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-log"
      note: "Supported affordances are retained at their own evidence layer. No observed operation, automatic decay, promotion or semantic invalidation is inferred from structural gating, deletion review or Health advice."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Requested wiki/raw/contract reads in later model tasks and person-requested desktop opening"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-mcp-navigation"
                - "runtime.md#rt-rte-vault-query"
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-rte-desktop-reload"
                - "runtime.md#rt-bap-vault-contract"
              note: "Models request tools/files; opening/reopening asks the desktop to load the brain. A response to a requested read is not a second push."
          records:
            - "memory.md#mem-rte-mcp-navigation"
            - "runtime.md#rt-rte-vault-query"
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-rte-desktop-reload"
            - "runtime.md#rt-bap-vault-contract"
          note: "MCP and native filesystem access are alternatives into the same retained brain."
        -
          scope: "Profile/configuration selected automatically when Eva prepares later ingest/query/advisory invocations"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-brain-settings"
                - "runtime.md#rt-rte-source-ingest"
              note: "Task startup rereads retained settings/profile and supplies dispatch/task guidance without the model requesting that memory."
          records:
            - "runtime.md#rt-rte-brain-settings"
            - "runtime.md#rt-rte-source-ingest"
          note: "The retained dynamic settings, not the shipped static prompt template, establish this push."
        -
          scope: "Enqueue's requested read of accumulated operation log"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "The enqueue consumer reads log text to apply its eligibility predicate."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-source-ingest"
          note: "Suppression changes scheduling; it is not an unsolicited relevance-selected page delivery."
      records:
        - "memory.md#mem-rte-mcp-navigation"
        - "runtime.md#rt-rte-vault-query"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-rte-desktop-reload"
        - "runtime.md#rt-bap-vault-contract"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-log"
      note: "Known within Eva-owned routes. The memory report's request-driven retrieval finding concerns wiki retrieval, not automatic profile/configuration supply. External host auto-memory and compaction are excluded, not silently classified."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "Automatic task-start profile/configuration supply"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-brain-settings"
                - "runtime.md#rt-rte-source-ingest"
              note: "Trigger: task start. Selector input: the active vault and its retained settings/profile. Selected part: the active configuration/profile as a whole; no query-relevance or identity-matched page subset is established."
          records:
            - "runtime.md#rt-rte-brain-settings"
            - "runtime.md#rt-rte-source-ingest"
          note: "A user can change upstream settings, but per-task inclusion remains coarse automatic supply."
        -
          scope: "Requested MCP/native page access, desktop reload and enqueue log read"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-mcp-navigation"
            - "memory.md#mem-rte-desktop-reload"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-vault-query"
          note: "These are pull operations. MCP lexical scoring and requested page IDs are not push-selection signals."
      records:
        - "runtime.md#rt-rte-brain-settings"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-rte-mcp-navigation"
        - "memory.md#mem-rte-desktop-reload"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-vault-query"
      note: "Known for the direction inventory above. Lexical search does not add inferred-lexical here because the actual operation fulfills a consumer request; a requested ID alone does not establish identifier push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic operation-result log writes with later source-eligibility consumer"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "Task outcome/summary or rejection activity automatically becomes retained log state; later enqueue uses its subject occurrence as a durable admission veto. This meets the trace-fed behavior-shaping write criterion, not improved-capacity learning."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-source-ingest"
          note: "Raw log storage alone would be insufficient; the established later scheduling consumer supplies the behavioral consequence."
        -
          scope: "Model curation from arbitrary raw source payloads and initially imported memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-knowledge-pages"
            - "memory.md#mem-obj-summaries"
            - "runtime.md#rt-rte-source-ingest"
          note: "Source-fed automatic page admission is known, but source content/origin is not fixed. The records do not establish whether any included user document is qualifying activity trace material."
        -
          scope: "Human-reviewed saved analyses and human UI settings edits"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-analysis-save"
            - "runtime.md#rt-rte-brain-settings"
            - "memory.md#mem-obj-analyses"
          note: "These scoped writes depend on explicit human retention/content decisions rather than automatic trace-fed admission."
      records:
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-knowledge-pages"
        - "memory.md#mem-obj-summaries"
        - "runtime.md#rt-rte-analysis-save"
        - "runtime.md#rt-rte-brain-settings"
        - "memory.md#mem-obj-analyses"
      note: "Known automatic log-to-eligibility route supports yes locally; unresolved raw-source origin prevents complete trace-learning coverage. No local no is asserted because no accepted evidenced-absence record warrants it. This axis does not assert semantic learning, exercised improvement or parameter training."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Runtime operation/outcome and review-rejection activity feeding the automatic operation log"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-source-ingest"
              note: "Original inputs include discrete ingest outcomes and review rejection events; Eva retains their dated operation/subject/result for later scheduling."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-source-ingest"
          note: "This is activity-derived operational state, not a claim that every imported source is an event stream."
        -
          scope: "Agent summary provenance within log bodies and arbitrary raw inputs to potential trace-fed curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-rte-source-ingest"
          note: "The records name an agent summary and arbitrary source documents but do not establish recorded session turns, tool requests/results, linked trajectories or other specific original trace content."
        -
          scope: "Manually retained answers and human-chosen settings"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-analysis-save"
            - "runtime.md#rt-rte-brain-settings"
          note: "These units have no qualifying automatic trace-learning write in the scoped UI routes."
      records:
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-analysis-save"
        - "runtime.md#rt-rte-brain-settings"
      note: "Event-stream provenance is supported for operation activity. Summary labels and document serialization do not justify adding session-logs, tool-traces or trajectories; unresolved original content remains included."
---

# Eva-brain memory profile

## Comparison rationale

This profile classifies accepted records, not a fresh source inspection. All
positive bases concern implementation wiring or model curation affordances;
none asserts observed activation, factual correctness or causal benefit.

The comparison inventory is the retained brain and its later consumers, not
the whole runtime. Files and Git history are storage; parsed adjacency is an
access structure rebuilt from retained metadata, not a separate accumulated
graph memory. Natural-language page content and symbolic matching/dispatch
parts remain distinct ([MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata),
[MEM-OBJ-log](memory.md#mem-obj-log),
[RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings)). Unknown initial
provenance does not erase known later import, authoring, formatting or admission.
The lineage finding for compiled output is limited to Rust-formatted saved
analyses and their constructed reference metadata. Persisted identifiers,
frontmatter and links elsewhere remain separately unresolved: deterministic
parsing or consumption does not establish their derivation. The recorded
page-level import and authoring routes do not resolve every metadata part's
origin ([MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata),
[EPI-RTE-analysis-format](epistemic.md#epi-rte-analysis-format)).

Curation has weaker evidence than persistence. The model is asked to digest,
revise and merge instead of duplicate; the code makes such edits retainable.
These establish affordances, not a verified semantic transformation.
Neither a named synthesis product nor the research profile proves that a new
claim was created. Answer formatting is independently wired but does not
supply a controlled semantic curation operation
([MEM-OBJ-knowledge-pages](memory.md#mem-obj-knowledge-pages),
[MEM-OBJ-summaries](memory.md#mem-obj-summaries),
[EPI-RTE-analysis-format](epistemic.md#epi-rte-analysis-format)).

Wiki retrieval is pull even when deterministic lexical scoring selects the
requested result. The same text can have ranking authority without an
inferred-lexical push signal. Dynamic profile/configuration supply on task
startup is a different operation: retained settings are selected automatically
for dispatch and guidance. This coarse push does not turn a requested page
read into identifier-based push
([MEM-RTE-mcp-navigation](memory.md#mem-rte-mcp-navigation),
[RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest),
[RT-RTE-brain-settings](runtime.md#rt-rte-brain-settings)).
Static prompt construction alone is excluded from this classification.

The automatic operation log has a narrow trace-learning mapping. Its later
consumer uses filename occurrence to alter future admission, including after
rejection. Thus the retained result is more than an unused activity log.
The wired yes is confined to this behavior-shaping state route; it does not
contradict the records' refusal to establish semantic learning or improved
capacity. Ordinary source-derived knowledge is not automatically called
trace learning, and manually reviewed answer retention does not become
automatic merely because Rust performs the write
([MEM-OBJ-log](memory.md#mem-obj-log),
[RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest),
[RT-RTE-analysis-save](runtime.md#rt-rte-analysis-save)).
Arbitrary user documents and agent-summary origin leave the learning/source
inventories partial. No bounded absence record supports a local no, and no
system-wide negative is inferred.

Reconciliation supersedes the epistemic raw-source declaration with
[MEM-OBJ-raw](memory.md#mem-obj-raw) and its duplicate navigation declaration
with [MEM-RTE-mcp-navigation](memory.md#mem-rte-mcp-navigation).
All findings use those canonical records. The corpus container and its
prose/metadata parts remain distinct valid records; formatting remains a
part of saving rather than a second admission route. No supersession
changes a controlled value or upgrades its basis.

Additional source reads: none. The accepted records supply all warrants;
no new quotes, records or evidence were added.
