---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "LLM-WIKI-MCP memory profile: local knowledge, access metadata, retained conversation reductions and diagnostic read-back, with unresolved guidance and provider alternatives."
run-id: "AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01"
source-identity: "https://github.com/Electro-resonance/LLM-WIKI-MCP"
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
memory-comparison:
  version: 2
  scope: "Included: use-produced or changed wiki pages and raw ingest copies, sidecars, SQLite indexes/provenance/decisions, process caches, exact and compressed ask histories, CLI session/command history, runtime config, metrics/journal records, generated documentation and their write/maintenance/later-consumer routes. Additional editable guidance/maintenance paths and any accumulated provider state remain unresolved included alternatives. Excluded: static shipped prompts/developer instructions, fixed model weights, transient current-call context before retention, external host responsibilities and mere hypothetical external learning."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Wiki, sidecars, live and compressed history, configuration, diagnostics and generated documentation files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-obj-ask-history-compressed"
                - "runtime.md#rt-rte-runtime-config"
                - "memory.md#mem-obj-runtime-traces"
                - "runtime.md#rt-rte-docs-consolidate"
              note: "Local file persistence is implemented for these parts."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-ask-history-compressed"
            - "runtime.md#rt-rte-runtime-config"
            - "memory.md#mem-obj-runtime-traces"
            - "runtime.md#rt-rte-docs-consolidate"
          note: "These retained objects use local filesystem files. JSON/JSONL/Markdown are encodings, not separate substrates."
        - scope: "Page index, ingest provenance and decision rows"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-pages-fts"
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-rte-transcript-decision"
              note: "SQLite tables retain copied page text, metadata, provenance and decisions."
          records:
            - "memory.md#mem-obj-pages-fts"
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-rte-transcript-decision"
          note: "The SQLite-backed access/update structures and decision rows are separate from the readable files."
        - scope: "Search/context caches and CLI session fallback"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-pages-fts"
                - "memory.md#mem-rte-cli-history"
              note: "Caches and session copies are later-consumed process memory."
          records:
            - "memory.md#mem-obj-pages-fts"
            - "memory.md#mem-rte-cli-history"
          note: "Process-local material survives across requests within a shell/process, not across process exit."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-obj-ask-history-compressed"
        - "runtime.md#rt-rte-runtime-config"
        - "memory.md#mem-obj-runtime-traces"
        - "runtime.md#rt-rte-docs-consolidate"
        - "memory.md#mem-obj-pages-fts"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-rte-cli-history"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Known storage routes establish files, SQLite and process memory, not vector, repository or provider-service memory. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Wiki prose, note prose, history question/prompt/answer text and generated documentation at interpretive consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-obj-ask-history-compressed"
                - "runtime.md#rt-rte-docs-consolidate"
                - "runtime.md#rt-obj-context-pack"
              note: "Readers and prompt consumers interpret retained prose."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-ask-history-compressed"
            - "runtime.md#rt-rte-docs-consolidate"
            - "runtime.md#rt-obj-context-pack"
          note: "Natural-language material is separated from its structured access fields."
        - scope: "Page/link/frontmatter selectors, FTS/cache fields, history row fields, provenance, config and diagnostic fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-pages-fts"
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-obj-provenance"
                - "runtime.md#rt-rte-runtime-config"
                - "memory.md#mem-obj-runtime-traces"
                - "memory.md#mem-rte-cli-history"
              note: "Fixed parsing, lookup, scoring and dispatch give these parts symbolic consequences."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-pages-fts"
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-provenance"
            - "runtime.md#rt-rte-runtime-config"
            - "memory.md#mem-obj-runtime-traces"
            - "memory.md#mem-rte-cli-history"
          note: "Fixed code consumes localized fields, lexical text features and numerical estimates. Numerical fields are not distributed parameters."
        - scope: "Provider answer bodies independently retained in diagnostic metadata"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-traces"
              note: "Retained provider answer text remains interpretable content even in a JSON envelope."
          records:
            - "memory.md#mem-obj-runtime-traces"
          note: "Split from the symbolic envelope: answers/raw provider output may include text returned by explicit diagnostic consumers."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-obj-ask-history-compressed"
        - "runtime.md#rt-rte-docs-consolidate"
        - "runtime.md#rt-obj-context-pack"
        - "memory.md#mem-obj-pages-fts"
        - "memory.md#mem-obj-provenance"
        - "runtime.md#rt-rte-runtime-config"
        - "memory.md#mem-obj-runtime-traces"
        - "memory.md#mem-rte-cli-history"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-cmp-ollama-model"
      note: "The inspected retained boundary has mixed natural-language and symbolic parts. The provider component form does not classify unknown accumulated provider memory. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Direct caller page bodies, decisions, explicit history records and configuration proposals"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-rte-transcript-decision"
                - "memory.md#mem-obj-ask-history"
                - "runtime.md#rt-rte-runtime-config"
              note: "Caller-supplied original bodies/values have an authored route; this does not identify the author."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-rte-transcript-decision"
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-rte-runtime-config"
          note: "Content is supplied to an authoring/admission surface; human versus computational authorship and initial corpus history remain unresolved."
        - scope: "File-extracted wiki bodies and optional preserved raw originals"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-knowledge-write"
              note: "Local source extraction and wrapping provide an import path."
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "Acquisition copies/extracts external source content rather than establishing new warrant."
        - scope: "Indexes, caches, provenance metadata, note templates and reorganized documentation"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-pages-fts"
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-rte-note-template"
                - "runtime.md#rt-rte-docs-consolidate"
              note: "Deterministic indexing, metadata construction, term/link templates and document regrouping compile existing inputs."
          records:
            - "memory.md#mem-obj-pages-fts"
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-note-template"
            - "runtime.md#rt-rte-docs-consolidate"
          note: "These are program-derived access structures or content. Unknown initial page provenance is not resolved by their known derivation."
        - scope: "Ask-turn records, compressed answer excerpts, CLI session copies and metrics"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-obj-ask-history-compressed"
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-rte-cli-history"
                - "memory.md#mem-obj-runtime-traces"
              note: "The automatic ask/metrics/CLI paths extract retained records or reductions from activity."
          records:
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-ask-history-compressed"
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-rte-cli-history"
            - "memory.md#mem-obj-runtime-traces"
          note: "These derive from recorded interaction/activity. Explicit caller record tools and journal helpers do not authenticate original trace provenance."
        - scope: "Caller transcript clipping into an indexed wiki page"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-decision"
              note: "Clipped transcript lines become durable page content."
          records:
            - "memory.md#mem-rte-transcript-decision"
          note: "A reduction of supplied conversational material is implemented; exact session/tool/environment origin is not authenticated."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-obj-ask-history"
        - "runtime.md#rt-rte-runtime-config"
        - "runtime.md#rt-rte-knowledge-write"
        - "memory.md#mem-obj-pages-fts"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-rte-note-template"
        - "runtime.md#rt-rte-docs-consolidate"
        - "memory.md#mem-obj-ask-history-compressed"
        - "memory.md#mem-rte-history-compaction"
        - "memory.md#mem-rte-cli-history"
        - "memory.md#mem-obj-runtime-traces"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Known admission and derivation paths coexist with unresolved initial corpus and explicit-caller provenance. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Wiki, sidecar and recent-history text delivered as answering evidence or follow-up context"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-ask-history"
                - "runtime.md#rt-rte-agentic-ask"
                - "runtime.md#rt-rte-store-ask"
                - "runtime.md#rt-rte-plain-ask"
                - "runtime.md#rt-obj-context-pack"
              note: "Selected retained text supplies reference material to a later answering consumer."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-rte-agentic-ask"
            - "runtime.md#rt-rte-store-ask"
            - "runtime.md#rt-rte-plain-ask"
            - "runtime.md#rt-obj-context-pack"
          note: "These parts supply interpreted evidence/context, not executable permission or verified truth."
        - scope: "Archive and recent history returned by recursive context"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-ask-history-compressed"
                - "memory.md#mem-rte-recursive-context"
              note: "The returned context is offered to the external host/model role as memory."
          records:
            - "memory.md#mem-obj-ask-history-compressed"
            - "memory.md#mem-rte-recursive-context"
          note: "Local composition and context return are wired; actual external model use is not inspected."
        - scope: "Page/title/note text and FTS/cache content at retrieval scorers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-obj-pages-fts"
                - "runtime.md#rt-rte-store-ask"
                - "epistemic.md#epi-rte-note-template"
              note: "Text, titles and note matches influence relative retrieval priority."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-pages-fts"
            - "runtime.md#rt-rte-store-ask"
            - "epistemic.md#epi-rte-note-template"
          note: "Lexical fixed-code ranking gives retained content influence before any semantic acceptance."
        - scope: "Prior questions at intent resolution, provenance at ingest planning, and config at later dispatch"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ask-history"
                - "runtime.md#rt-rte-agentic-ask"
                - "memory.md#mem-obj-provenance"
                - "runtime.md#rt-rte-runtime-config"
                - "runtime.md#rt-bap-config-control"
              note: "Retained values determine operation, destination or input window."
          records:
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-rte-agentic-ask"
            - "memory.md#mem-obj-provenance"
            - "runtime.md#rt-rte-runtime-config"
            - "runtime.md#rt-bap-config-control"
          note: "Consumers select a resolved query, skip/update work, endpoint/model/mode or input budgets."
        - scope: "Configured history enablement and budget controls at recorder/pack code"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-runtime-config"
                - "runtime.md#rt-bap-config-control"
                - "runtime.md#rt-rte-agentic-ask"
                - "memory.md#mem-rte-history-compaction"
              note: "Loaded settings gate history writes and constrain selected context."
          records:
            - "runtime.md#rt-rte-runtime-config"
            - "runtime.md#rt-bap-config-control"
            - "runtime.md#rt-rte-agentic-ask"
            - "memory.md#mem-rte-history-compaction"
          note: "These retained controls can suppress append or constrain delivered material. The effect is code-enforced, not model instruction."
        - scope: "Prior turns at automatic compaction and transcript records at clipped-page production"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-rte-transcript-decision"
                - "memory.md#mem-rte-recursive-context"
              note: "Trace content feeds automatic production of durable context-bearing artifacts."
          records:
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-rte-transcript-decision"
            - "memory.md#mem-rte-recursive-context"
          note: "The update consumer uses experience to produce a durable later-context artifact. This is distinct from downstream knowledge authority and from improved capacity."
        - scope: "Generated sidecar suggestions/actions at later human or agent editor"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-rte-note-template"
              note: "Retained suggested actions offer directions to an editor rather than enforced admission criteria."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-note-template"
          note: "The emitted note supplies directions for review/promotion; actual editorial compliance is unobserved."
        - scope: "Diagnostic metrics and CLI/session history at explicit diagnostic/display consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-runtime-traces"
                - "memory.md#mem-rte-cli-history"
              note: "Retained rows are displayed or returned as operational reference."
          records:
            - "memory.md#mem-obj-runtime-traces"
            - "memory.md#mem-rte-cli-history"
          note: "Reports and history displays inform callers; no automatic score-driven policy update is established."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-ask-history"
        - "runtime.md#rt-rte-agentic-ask"
        - "runtime.md#rt-rte-store-ask"
        - "runtime.md#rt-rte-plain-ask"
        - "runtime.md#rt-obj-context-pack"
        - "memory.md#mem-obj-ask-history-compressed"
        - "memory.md#mem-rte-recursive-context"
        - "memory.md#mem-obj-pages-fts"
        - "epistemic.md#epi-rte-note-template"
        - "memory.md#mem-obj-provenance"
        - "runtime.md#rt-rte-runtime-config"
        - "runtime.md#rt-bap-config-control"
        - "memory.md#mem-rte-history-compaction"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-obj-runtime-traces"
        - "memory.md#mem-rte-cli-history"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Authority is attached to actual local consumers or an explicitly afforded external role. Static answer rules do not make every retained page an instruction; no common validation register is inferred. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Automatic ask/metrics admission and CLI visible-turn guard"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agentic-ask"
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-obj-runtime-traces"
                - "memory.md#mem-rte-cli-history"
              note: "Software admits turn, metrics and fallback session content without per-content approval."
          records:
            - "runtime.md#rt-rte-agentic-ask"
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-runtime-traces"
            - "memory.md#mem-rte-cli-history"
          note: "A user initiating an ask does not approve each retained answer/record."
        - scope: "Compaction, file ingestion, sidecar iteration, structural repairs, indexing and document regrouping"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-compaction"
                - "runtime.md#rt-rte-knowledge-write"
                - "memory.md#mem-obj-pages-fts"
                - "memory.md#mem-obj-provenance"
                - "epistemic.md#epi-rte-note-template"
                - "runtime.md#rt-rte-docs-consolidate"
              note: "Code selects and admits derived/replaced retained content after the workflow is triggered."
          records:
            - "memory.md#mem-rte-history-compaction"
            - "runtime.md#rt-rte-knowledge-write"
            - "memory.md#mem-obj-pages-fts"
            - "memory.md#mem-obj-provenance"
            - "epistemic.md#epi-rte-note-template"
            - "runtime.md#rt-rte-docs-consolidate"
          note: "Batch apply or command invocation can authorize work without deciding each produced entry."
        - scope: "Transcript clipping and readable decision-log derivation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-decision"
              note: "Clipped pages and appended readable entries are admitted without separate per-result human review."
          records:
            - "memory.md#mem-rte-transcript-decision"
          note: "Software transforms supplied transcript/decision fields into retained derivatives; this does not resolve who supplied the originals."
        - scope: "Direct body edits, explicit record tools, config changes and caller-selected rename/delete"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-rte-runtime-config"
            - "memory.md#mem-rte-page-withdrawal"
            - "memory.md#mem-rte-transcript-decision"
          note: "Generic caller identity does not establish an explicit human content decision or fully resolve software agency for the original proposal."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "runtime.md#rt-rte-agentic-ask"
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-obj-runtime-traces"
        - "memory.md#mem-rte-cli-history"
        - "memory.md#mem-rte-history-compaction"
        - "runtime.md#rt-rte-knowledge-write"
        - "memory.md#mem-obj-pages-fts"
        - "memory.md#mem-obj-provenance"
        - "epistemic.md#epi-rte-note-template"
        - "runtime.md#rt-rte-docs-consolidate"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-runtime-config"
        - "memory.md#mem-rte-page-withdrawal"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Automatic derivation is supported; no manual value is inferred merely from a CLI, caller or apply flag. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "History compaction over retained turns"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-obj-ask-history-compressed"
                - "memory.md#mem-rte-recursive-context"
              note: "Older retained claims are compressed into a lossy durable representation."
          records:
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-obj-ask-history-compressed"
            - "memory.md#mem-rte-recursive-context"
          note: "The reducer keeps question headings and shortened answer/source material. It is not semantic criticism or an invented synthesis."
        - scope: "Removal of exact older live rows during compaction"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-obj-ask-history"
              note: "Code removes older exact rows and can discard rows outside the loaded 500-row window."
          records:
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-obj-ask-history"
          note: "This is local forgetting of exact live records, not whole-system erasure: archives and independent metrics remain."
        - scope: "Clipped transcript-page production"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-decision"
              note: "Clipping and bullet conversion reduce supplied transcript content."
          records:
            - "memory.md#mem-rte-transcript-decision"
          note: "The implemented transformation reduces conversational lines, not a checked semantic synthesis."
        - scope: "Existing pages, sidecars and documentation revised by update, refresh, repair or rerun"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-knowledge-write"
                - "epistemic.md#epi-rte-note-template"
                - "runtime.md#rt-rte-docs-consolidate"
                - "memory.md#mem-rte-page-withdrawal"
              note: "Replacement, append/prepend, note rerun and structural link maintenance revise retained content."
          records:
            - "runtime.md#rt-rte-knowledge-write"
            - "epistemic.md#epi-rte-note-template"
            - "runtime.md#rt-rte-docs-consolidate"
            - "memory.md#mem-rte-page-withdrawal"
          note: "Overwrites and structural edits change existing retained entries. Note semantic novelty remains indeterminate."
        - scope: "Page withdrawal with optional tombstone"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-page-withdrawal"
              note: "Active reliance through ordinary page scans is withdrawn while tombstone bytes retain history."
          records:
            - "memory.md#mem-rte-page-withdrawal"
          note: "This finding is limited to the history-preserving tombstone branch, not every delete and not semantic refutation."
        - scope: "CLI history merge and signature-based guard"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-cli-history"
          note: "Signature comparison suppresses duplicate admission/display; the record does not establish merging or removing near-duplicate retained entries, so no dedup transformation is inferred."
        - scope: "Sidecar semantic topic/suggestion content and later editorial promotion"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-note-template"
          note: "The implemented overwrite supports evolve above. The records leave semantic novelty indeterminate and describe, rather than implement, later promotion; neither synthesize nor promote is established here."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-rte-history-compaction"
        - "memory.md#mem-obj-ask-history-compressed"
        - "memory.md#mem-rte-recursive-context"
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-rte-transcript-decision"
        - "runtime.md#rt-rte-knowledge-write"
        - "epistemic.md#epi-rte-note-template"
        - "runtime.md#rt-rte-docs-consolidate"
        - "memory.md#mem-rte-page-withdrawal"
        - "memory.md#mem-rte-cli-history"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Transformation semantics, not command labels, establish these findings. Index rebuilds and document concatenation alone do not establish consolidation or deduplication. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit page/search/retrieve/history/recursive/diagnostic requests and CLI history display"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-store-ask"
                - "runtime.md#rt-rte-plain-ask"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-notes"
                - "memory.md#mem-rte-recursive-context"
                - "memory.md#mem-obj-runtime-traces"
                - "memory.md#mem-rte-cli-history"
              note: "Consumers explicitly request retained material or a context/history/diagnostic return."
          records:
            - "runtime.md#rt-rte-store-ask"
            - "runtime.md#rt-rte-plain-ask"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-rte-recursive-context"
            - "memory.md#mem-obj-runtime-traces"
            - "memory.md#mem-rte-cli-history"
          note: "Fulfilling a request for retained content is pull even when code ranks or formats the returned material."
        - scope: "Recent history automatically supplied to intent resolution and an answer prompt"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agentic-ask"
                - "memory.md#mem-obj-ask-history"
                - "runtime.md#rt-obj-context-pack"
              note: "Ask-triggered code inserts selected recent turns into intent/context and may include full-row history tool evidence."
          records:
            - "runtime.md#rt-rte-agentic-ask"
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-obj-context-pack"
          note: "A request for an answer is not a separate request for prior turns. Code selects them automatically; final prompt assembly does not guarantee full delivery."
        - scope: "Configuration and provenance automatically loaded during later work"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-runtime-config"
                - "runtime.md#rt-bap-config-control"
                - "memory.md#mem-obj-provenance"
                - "runtime.md#rt-rte-knowledge-write"
              note: "Later ask/write work triggers automatic loading of retained settings and source-status rows."
          records:
            - "runtime.md#rt-rte-runtime-config"
            - "runtime.md#rt-bap-config-control"
            - "memory.md#mem-obj-provenance"
            - "runtime.md#rt-rte-knowledge-write"
          note: "Code supplies retained control/update metadata to its decision consumers without a separate request for that retained material."
        - scope: "Archive/recent insertion within an explicitly requested recursive context"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-recursive-context"
                - "memory.md#mem-obj-ask-history-compressed"
              note: "The caller explicitly requests memory context."
          records:
            - "memory.md#mem-rte-recursive-context"
            - "memory.md#mem-obj-ask-history-compressed"
          note: "The requested return is pull, not an additional push merely because the helper composes text."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "runtime.md#rt-rte-store-ask"
        - "runtime.md#rt-rte-plain-ask"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-rte-recursive-context"
        - "memory.md#mem-obj-runtime-traces"
        - "memory.md#mem-rte-cli-history"
        - "runtime.md#rt-rte-agentic-ask"
        - "memory.md#mem-obj-ask-history"
        - "runtime.md#rt-obj-context-pack"
        - "runtime.md#rt-rte-runtime-config"
        - "runtime.md#rt-bap-config-control"
        - "memory.md#mem-obj-provenance"
        - "runtime.md#rt-rte-knowledge-write"
        - "memory.md#mem-obj-ask-history-compressed"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Both requested returns and automatic retained-input supply exist; external host reinjection after a tool return is not established. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Ask-triggered recent-history selection for intent and prompt sections"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-agentic-ask"
                - "memory.md#mem-obj-ask-history"
                - "runtime.md#rt-obj-context-pack"
              note: "Recency/count and budget selection are coarse, not identity-targeted or relevance-judged selection."
          records:
            - "runtime.md#rt-rte-agentic-ask"
            - "memory.md#mem-obj-ask-history"
            - "runtime.md#rt-obj-context-pack"
          note: "Trigger: later ask. Input: available live rows and recency/count/budget rules. Selected part: latest question or bounded recent rows, with separate sanitized tool-row serialization."
        - scope: "Automatic configuration supply at later dispatch/recording/context construction"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-runtime-config"
                - "runtime.md#rt-bap-config-control"
              note: "Current-settings availability supplies controls without a semantic match."
          records:
            - "runtime.md#rt-rte-runtime-config"
            - "runtime.md#rt-bap-config-control"
          note: "Trigger: later operation. Input: current config/default fields. Selected part: active settings as a broad control bundle, not targeted memory matching."
        - scope: "Automatic ingest-status lookup"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provenance"
                - "runtime.md#rt-rte-knowledge-write"
              note: "An actual source identity lookup selects the retained provenance row consumed by the planner."
          records:
            - "memory.md#mem-obj-provenance"
            - "runtime.md#rt-rte-knowledge-write"
          note: "Trigger: re-ingest. Input: source-file identity/path plus recorded hash and datestamp. Selected part: matching source-status row used to skip or update."
        - scope: "Explicit query-ranked page/note retrieval"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-store-ask"
            - "memory.md#mem-obj-notes"
            - "memory.md#mem-obj-pages-fts"
          note: "Lexical scoring on these requested retained-content returns does not establish an inferred-lexical push signal. No positive push finding is assigned to this pull operation."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "runtime.md#rt-rte-agentic-ask"
        - "memory.md#mem-obj-ask-history"
        - "runtime.md#rt-obj-context-pack"
        - "runtime.md#rt-rte-runtime-config"
        - "runtime.md#rt-bap-config-control"
        - "memory.md#mem-obj-provenance"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-rte-store-ask"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-pages-fts"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Signals describe automatic supply only. Lexical ranking remains a positive authority finding without being misclassified as push selection. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic older-turn compaction to persistent archive with recursive-context consumer"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-obj-ask-history-compressed"
                - "memory.md#mem-rte-recursive-context"
              note: "Recorded interaction turns feed automatic retained reduction and later context composition."
          records:
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-obj-ask-history-compressed"
            - "memory.md#mem-rte-recursive-context"
          note: "The archive is a durable behavior-shaping context artifact with an implemented later context-return route. External model delivery is afforded, not observed; improvement is not required for this axis."
        - scope: "Automatic transcript clipping to indexed page for later answers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-decision"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-store-ask"
              note: "Software converts a supplied transcript into durable later-consumed knowledge context."
          records:
            - "memory.md#mem-rte-transcript-decision"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-store-ask"
          note: "The transformation retains reduced conversational material and makes it available to ordinary later context retrieval. Actual source authenticity and model activation remain unobserved."
        - scope: "Raw ask records, metrics, journal helpers and CLI copies apart from qualifying reductions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-obj-runtime-traces"
            - "memory.md#mem-rte-cli-history"
          note: "Raw logging alone is not a qualifying update; these records do not provide a bounded exhaustive absence warrant for all downstream transformations. No local no is asserted."
        - scope: "Sidecar updates over pages whose initial provenance may include transcripts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-note-template"
            - "memory.md#mem-obj-wiki"
          note: "Known note rewriting does not resolve which original experience sources feed a particular page or whether all included paths are trace-fed. No trace-learning positive or negative is inferred for this alternative."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-rte-history-compaction"
        - "memory.md#mem-obj-ask-history-compressed"
        - "memory.md#mem-rte-recursive-context"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-store-ask"
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-obj-runtime-traces"
        - "memory.md#mem-rte-cli-history"
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-rte-note-template"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Qualifying automatic trace-to-durable-context routes support yes locally, not observed learning benefit or a system-wide negative elsewhere. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Recorded ask conversation consumed by history compaction"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ask-history"
                - "memory.md#mem-rte-history-compaction"
                - "memory.md#mem-obj-ask-history-compressed"
              note: "The qualifying reducer consumes recorded conversational questions/answers, not an event stream inferred from JSONL."
          records:
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-rte-history-compaction"
            - "memory.md#mem-obj-ask-history-compressed"
          note: "Questions and answers are recorded conversational turns from ask work. Tool-name source labels are not recorded tool requests/results consumed by this reduction."
        - scope: "Original provenance of explicit supplied histories and transcript material"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-ask-history"
            - "memory.md#mem-rte-transcript-decision"
          note: "A transcript/record label does not identify agent-session, tool-execution, environmental-event or trajectory origin for every supplied payload. No additional controlled trace source is established."
        - scope: "Possible trace inputs behind generated pages/notes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-note-template"
          note: "The initial corpus and all source paths are unresolved, so no complete trace-origin union can be derived for those alternative writes."
        - scope: "Additional editable guidance and incompletely traced maintenance alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-knowledge-write"
          note: "The accepted corpus and broad write-route records do not enumerate every editable guidance part or its complete maintenance/consumer chain. No controlled value is inferred for those additional parts; an exhaustive classification is prevented."
        - scope: "Opaque provider state, if accumulated or changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-ollama-model"
          note: "The endpoint component is recorded, but its retained mutable state and internal update/consumer paths are uninspected. Shipped or fixed model weights alone are excluded from accumulated memory. No provider-memory value or negative is inferred."
      records:
        - "memory.md#mem-obj-ask-history"
        - "memory.md#mem-rte-history-compaction"
        - "memory.md#mem-obj-ask-history-compressed"
        - "memory.md#mem-rte-transcript-decision"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-rte-note-template"
        - "runtime.md#rt-rte-knowledge-write"
        - "runtime.md#rt-cmp-ollama-model"
      note: "Session-log origin is supported on the inspected ask-compaction path. Tool labels, timestamps and imported source wrappers alone do not add tool-traces, event-streams or trajectories. Additional guidance/maintenance coverage and any accumulated provider state remain unresolved; positive local findings do not close the inventory."
---

# LLM-WIKI-MCP memory profile

## Comparison rationale

The profile classifies accepted records, not source files or an observed deployment. All positive implementation findings are wired unless a finding explicitly retains an afforded consumer. No record supplies observed activation or causal benefit. Every axis is partial: the accepted inventory does not close additional editable-guidance/maintenance coverage, and the provider record leaves any use-accumulated internal state uninspected. Static model weights are not silently substituted for that unknown memory boundary.

### Storage, form and origin

[MEM-OBJ-wiki](memory.md#mem-obj-wiki), [MEM-OBJ-notes](memory.md#mem-obj-notes), [MEM-OBJ-pages-fts](memory.md#mem-obj-pages-fts) and [MEM-OBJ-provenance](memory.md#mem-obj-provenance) separate retained text, access structures and refresh metadata. SQLite is the specific substrate; its relational implementation does not require a second rdbms finding for the same part. Wiki-link syntax does not establish a separate graph store. Process caches and CLI session copies count only over their cross-invocation process horizon. A Git evidence checkout does not make deployment memory repo-backed.

Natural-language and symbolic findings have different consumption paths even where their bytes share a file. Copied prose retains its natural-language role; fixed lexical scoring also consumes localized text features symbolically. Initial authorship and explicit-caller provenance remain unresolved. Imported source text, authored bodies, deterministic derivatives and interaction-derived records therefore coexist without a complete lineage claim. See [MEM-OBJ-ask-history](memory.md#mem-obj-ask-history), [MEM-OBJ-runtime-traces](memory.md#mem-obj-runtime-traces) and [RT-RTE-docs-consolidate](runtime.md#rt-rte-docs-consolidate).

### Authority and control

Retained text can provide knowledge to an answering consumer and ranking inputs to fixed scoring code. Prior questions also route follow-up interpretation; provenance routes refresh; config routes endpoint/mode/budget decisions and enforces append/context gates. These are distinct effects, not an upgrade from evidence to executable instructions. Sidecar suggested actions afford editorial instruction, but no human acceptance or actual promotion is established. See [MEM-OBJ-notes](memory.md#mem-obj-notes), [EPI-RTE-note-template](epistemic.md#epi-rte-note-template), [RT-BAP-config-control](runtime.md#rt-bap-config-control) and [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask).

The automatic reducer consumes retained experience to build durable later-context artifacts, giving its inputs learning authority at that update consumer. The output has a separate knowledge role. This does not imply revised weights, improved competence or acceptance of the retained assertions. Automatic admission is supported for software-produced derivatives even when a caller starts the workflow. Generic body/config/record callers do not establish manual admission. See [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction) and [MEM-RTE-transcript-decision](memory.md#mem-rte-transcript-decision).

### Transformations and later supply

Compaction consolidates retained turns and locally forgets removed exact rows. The archive and independent metrics prevent treating that local decay as whole-system forgetting. Tombstone-preserving deletion withdraws active reliance while keeping history; plain destructive deletion is not the warrant for invalidate. Sidecar replacement and structural edits establish evolve. Neither index rebuilding nor a command named consolidation establishes semantic consolidation. Signature admission guards alone do not establish a dedup transformation over retained near duplicates. Semantic novelty of topic suggestions and later editorial promotion remain unresolved. See [MEM-RTE-page-withdrawal](memory.md#mem-rte-page-withdrawal), [MEM-RTE-cli-history](memory.md#mem-rte-cli-history) and [EPI-RTE-note-template](epistemic.md#epi-rte-note-template).

Requested retained-content returns are pull. Automatic recent-history/context and control-state supply within later work is push. Recent-row count/recency and config availability are coarse signals; source-identity matching selects provenance metadata. Lexical scoring on explicitly requested retrieval is not automatically a lexical push signal. The context pack has two historical channels: reduced recent Q/A and serialized full-row history evidence, potentially including stored prompts. A dedicated history budget does not cap both. The recursive reader's requested archive return is not another push, and downstream external model delivery remains afforded. See [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), [MEM-RTE-recursive-context](memory.md#mem-rte-recursive-context) and [MEM-OBJ-provenance](memory.md#mem-obj-provenance).

The qualifying compaction path consumes session logs. Tool names in source lists are not tool traces; JSONL serialization and timestamps do not turn conversation into environmental event streams. Transcript clipping supports a qualifying durable context transformation, while its original agent-session/tool/event provenance is unresolved. Raw metrics/journal retention alone supplies neither a qualifying learning update nor a bounded absence warrant. See [MEM-RTE-history-compaction](memory.md#mem-rte-history-compaction), [MEM-RTE-transcript-decision](memory.md#mem-rte-transcript-decision) and [MEM-OBJ-runtime-traces](memory.md#mem-obj-runtime-traces).

### Reconciliation and coverage limits

Supersessions affect corpus, sidecar and withdrawal citations: the canonical records are [MEM-OBJ-wiki](memory.md#mem-obj-wiki), [MEM-OBJ-notes](memory.md#mem-obj-notes) and [MEM-RTE-page-withdrawal](memory.md#mem-rte-page-withdrawal), not their epistemic duplicates. The combined history record and its separately declared live/archive objects remain valid containers/parts rather than competing identities. No supersession erases the epistemic note-template uncertainty or withdrawal limits.

The records lack an exhaustive editable-guidance inventory and complete downstream instruction/maintenance tracing. No positive schema-specific value is manufactured from report prose outside a declaring record. These omissions prevent complete authority, write, curation and read-back unions, and prevent complete storage/form/lineage/trace coverage for the included alternatives. [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model) independently prevents classification of opaque use-accumulated provider state. Explicit record/transcript callers also leave original control and trace origin unresolved. These are limitations, not absences; no local trace-learning no or system-wide inapplicability is inferred.

### Source-read log

No frozen-source files were read. Classification used only the supplied contracts and accepted boundary, runtime, memory, epistemic, workflow and reconciliation members. No records or source evidence were added.
