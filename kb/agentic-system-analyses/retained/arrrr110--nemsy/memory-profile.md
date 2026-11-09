---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Nemsy memory profile: retained Markdown, control ledgers and conversation-derived insight read-back at the frozen revision."
run-id: "AAS-2026-11-09-nemsy-2a6b7963bf65-01"
source-identity: "https://github.com/arrrr110/nemsy"
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
memory-comparison:
  version: 2
  scope: "Local retained source/guidance inputs, generated source/query/insight pages, Wiki index and operation log, ingest/token ledgers, their admissions, maintenance and later model/human/control consumers; included opaque provider retention alternatives remain uninspected. Excludes shipped static task/schema/template instructions, developer rules, roadmap, transient unsaved conversation/request state, and unused configured directories as memory objects."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Local accumulated Wiki pages, index, operation log, ingest and token ledgers; extant source and directory-guidance files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-insight-page"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-operation-log"
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "memory.md#mem-obj-index-guidance"
                - "epistemic.md#epi-obj-source-content"
              note: "Markdown and JSON persist as filesystem files; JSON encoding is not a separate database substrate."
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-operation-log"
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "memory.md#mem-obj-index-guidance"
            - "epistemic.md#epi-obj-source-content"
          note: "The records enumerate local content and control/accounting files. Configured but unused history/cache directories are not additional retained objects."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "memory.md#mem-obj-insight-page"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-operation-log"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "memory.md#mem-obj-index-guidance"
        - "epistemic.md#epi-obj-source-content"
        - "runtime.md#rt-cmp-deepseek"
      note: "Local retained-file inventory is classified; opaque provider retention prevents whole-inventory completeness. Transient request strings and unsaved chat history are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Wiki prose, questions, index summaries, local source prose, ancestor guidance and readable operation details at model/human consumption"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-insight-page"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-index-guidance"
                - "memory.md#mem-obj-operation-log"
                - "epistemic.md#epi-obj-source-content"
              note: "Their meaning reaches consumers through interpretation of text, including questions and any retained derivation."
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-index-guidance"
            - "memory.md#mem-obj-operation-log"
            - "epistemic.md#epi-obj-source-content"
          note: "This unit classifies text consumption rather than treating Markdown as a fourth form."
        -
          scope: "Retained ingest/token records and page/index navigation or display metadata at fixed-rule consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-insight-page"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-rte-browser-read"
              note: "Hashes, statuses, counters, frontmatter display fields, filenames and link stems have localized meanings to code/browser consumers."
          records:
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-rte-browser-read"
          note: "Metadata is separate from prose interpreted by the generation model. No vector or parametric memory representation is established by local records."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "memory.md#mem-obj-insight-page"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-index-guidance"
        - "memory.md#mem-obj-operation-log"
        - "epistemic.md#epi-obj-source-content"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "memory.md#mem-rte-browser-read"
        - "runtime.md#rt-cmp-deepseek"
      note: "Both local text and fixed-rule metadata are classified. The generation model's distributed parameters are not automatically classified as memory accumulated through Nemsy use; provider retention remains opaque."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Source-summary and archived-query derivation paths; index and bookkeeping construction"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "memory.md#mem-obj-operation-log"
                - "runtime.md#rt-rte-document-ingest"
                - "runtime.md#rt-rte-answer-archive"
              note: "Software/model processing creates summaries, reformatted answers, index entries and operational metadata from supplied inputs. This classifies the derivation path, not verified semantic preservation."
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "memory.md#mem-obj-operation-log"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-answer-archive"
          note: "Source pages can combine documents, guidance and Wiki text; query pages retain generated answers. Neither is assumed to be a pure extract."
        -
          scope: "Conversation-insight derivation"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insight-page"
                - "runtime.md#rt-rte-insight-save"
              note: "Selected user/assistant conversation is rewritten into a retained insight page."
          records:
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-insight-save"
          note: "The retained insight is distinct from raw history; no durable raw-history checkpoint is inferred."
        -
          scope: "Acquired local source and ancestor-guidance input path"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-source-content"
                - "memory.md#mem-obj-index-guidance"
                - "runtime.md#rt-rte-document-ingest"
              note: "Existing local files enter ingestion as external text and guidance."
          records:
            - "epistemic.md#epi-obj-source-content"
            - "memory.md#mem-obj-index-guidance"
            - "runtime.md#rt-rte-document-ingest"
          note: "Import is established independently of initial authorship."
        -
          scope: "Initial authorship of local sources/guidance and any pre-existing Wiki content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-index-guidance"
            - "memory.md#mem-obj-source-page"
            - "runtime.md#rt-rte-wiki-answer"
          note: "Actual local authors and original content provenance are unavailable. Import and subsequent generation do not establish authored lineage for their inputs."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "memory.md#mem-obj-operation-log"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-answer-archive"
        - "memory.md#mem-obj-insight-page"
        - "runtime.md#rt-rte-insight-save"
        - "epistemic.md#epi-obj-source-content"
        - "memory.md#mem-obj-index-guidance"
        - "runtime.md#rt-rte-wiki-answer"
        - "runtime.md#rt-cmp-deepseek"
      note: "Known acquisition and derivation paths coexist with unresolved initialization provenance and opaque provider memory. Model generation is not by itself evidence of novel authored claims."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained Wiki bodies/index at later answer, chat, ingestion and lint model consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-insight-page"
                - "memory.md#mem-obj-wiki-index"
                - "runtime.md#rt-bap-wiki-context"
              note: "Selected retained text supplies context/reference to later generation and maintenance diagnosis; delivery does not establish compliance or truth."
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
            - "memory.md#mem-obj-wiki-index"
            - "runtime.md#rt-bap-wiki-context"
          note: "Model context includes pages irrespective of their provenance category; location in a system prefix does not establish deterministic enforcement."
        -
          scope: "Extant ancestor directory guidance at the ingestion model"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-index-guidance"
                - "runtime.md#rt-rte-document-ingest"
              note: "Guidance supplies collection intent, tags and viewpoint preferences for the generated summary."
          records:
            - "memory.md#mem-obj-index-guidance"
            - "runtime.md#rt-rte-document-ingest"
          note: "This concerns actual local guidance, not the excluded static shipped template."
        -
          scope: "Retained source/path/hash status at the CLI pending selector"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ingest-log"
                - "runtime.md#rt-rte-document-ingest"
              note: "Stored hashes determine whether a source enters a later ingest input set; HTTP display has a different mtime-based route."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ingest-log"
                - "runtime.md#rt-rte-document-ingest"
              note: "A matching stored hash causes the ordinary CLI branch to skip the source unless forced, including when no page was produced."
          records:
            - "memory.md#mem-obj-ingest-log"
            - "runtime.md#rt-rte-document-ingest"
          note: "These are progression controls, not validation of the generated page's truth."
        -
          scope: "Retained page modification metadata at the Wiki recency selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-answer"
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-query-page"
                - "memory.md#mem-obj-insight-page"
              note: "Modification times order page priority before count truncation."
          records:
            - "runtime.md#rt-rte-wiki-answer"
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
          note: "Ranking is fixed-code recency, not semantic ranking of page text."
        -
          scope: "Retained conversation messages at the insight-generation update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insight-page"
                - "runtime.md#rt-rte-insight-save"
              note: "Recorded session experience feeds a durable behavior-shaping page; the page subsequently supplies knowledge, not demonstrated improvement."
          records:
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-insight-save"
          note: "Update authority is separate from downstream page authority."
        -
          scope: "Wiki pages and accounting/operation records at human-facing browser/status consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-browser-read"
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "memory.md#mem-obj-operation-log"
              note: "File contents, status badges and usage aggregates supply reference or operational information to the human-facing consumer."
          records:
            - "memory.md#mem-rte-browser-read"
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "memory.md#mem-obj-operation-log"
          note: "No automatic prompt or policy revision is inferred from accounting."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "memory.md#mem-obj-insight-page"
        - "memory.md#mem-obj-wiki-index"
        - "runtime.md#rt-bap-wiki-context"
        - "memory.md#mem-obj-index-guidance"
        - "runtime.md#rt-rte-document-ingest"
        - "memory.md#mem-obj-ingest-log"
        - "runtime.md#rt-rte-wiki-answer"
        - "runtime.md#rt-rte-insight-save"
        - "memory.md#mem-rte-browser-read"
        - "memory.md#mem-obj-token-log"
        - "memory.md#mem-obj-operation-log"
        - "runtime.md#rt-cmp-deepseek"
      note: "Local consumer/effect paths are separated. Metadata unconsumed by a particular route has no authority at that route; opaque provider consumers prevent complete coverage."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Generated summary, ordinary archive and insight admission; index and ledger/log updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-document-ingest"
                - "runtime.md#rt-rte-answer-archive"
                - "runtime.md#rt-rte-insight-save"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "memory.md#mem-obj-operation-log"
              note: "After operation selection, model/code admit the particular output or record without a human supplying, editing or approving that retained content."
          records:
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-answer-archive"
            - "runtime.md#rt-rte-insight-save"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "memory.md#mem-obj-operation-log"
          note: "Starting ingest/save/archive is not per-content approval. The unused HTTP archive flag and broken reasoning archive are not additional successful admissions."
        -
          scope: "Initial local source/guidance and existing Wiki content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-index-guidance"
            - "epistemic.md#epi-obj-source-content"
            - "runtime.md#rt-rte-wiki-answer"
          note: "Generic file/caller identity does not establish a human decision supplying the particular content. No manual finding follows from file presence."
        -
          scope: "Exposed storage-helper content admission outside the shipped call graph"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-clm-storage-lifecycle"
          note: "Write/append/delete capabilities do not identify an actual caller or its per-content human control."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-answer-archive"
        - "runtime.md#rt-rte-insight-save"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "memory.md#mem-obj-operation-log"
        - "memory.md#mem-obj-index-guidance"
        - "epistemic.md#epi-obj-source-content"
        - "runtime.md#rt-rte-wiki-answer"
        - "memory.md#mem-clm-storage-lifecycle"
        - "runtime.md#rt-cmp-deepseek"
      note: "Known software/model admissions remain automatic despite human workflow initiation; initial content control, hypothetical helper callers and provider admission remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Generation of reduced source summaries and conversation insight representations"
          assessment: "partial"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-page"
                - "memory.md#mem-obj-insight-page"
                - "runtime.md#rt-rte-document-ingest"
                - "runtime.md#rt-rte-insight-save"
              note: "Summary/insight routes select and compress supplied content into standing pages. This identifies the wired reduction route, not a guarantee that each proposition is preserved."
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-insight-save"
            - "epistemic.md#epi-rte-summary-cleanup"
          note: "Compression and deterministic cleanup are supported. Actual outputs are unavailable, so additional novel-claim synthesis or semantic revisions cannot be established from requested synthesis alone."
        -
          scope: "Same-path page replacement, archive formatting, index append and exposed mutation helpers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-clm-storage-lifecycle"
            - "runtime.md#rt-rte-answer-archive"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-insight-page"
          note: "Physical overwrite and append do not establish semantic evolve, dedup, invalidate, decay or promote. The records do not determine such transformations of existing claims; ordinary archive adds formatting without another synthesis call."
        -
          scope: "Automatic application of lint suggestions"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-lint"
          note: "Lint returns advice rather than retaining or applying a memory correction; its requested maintenance is not a curation operation over retained pages."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-insight-page"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-insight-save"
        - "epistemic.md#epi-rte-summary-cleanup"
        - "memory.md#mem-clm-storage-lifecycle"
        - "runtime.md#rt-rte-answer-archive"
        - "memory.md#mem-obj-wiki-index"
        - "runtime.md#rt-rte-wiki-lint"
        - "runtime.md#rt-cmp-deepseek"
      note: "Consolidation is supported locally; synthesis/evolution cannot be upgraded from names, prompts or overwrites. Provider transformations remain uninspected."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Wiki context loading within answer/chat/ingest/lint requests"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-answer"
                - "runtime.md#rt-rte-conversation-chat"
                - "runtime.md#rt-rte-document-ingest"
                - "runtime.md#rt-rte-wiki-lint"
                - "memory.md#mem-obj-wiki-index"
              note: "A task request triggers code to select and supply index and recent retained pages without a consumer request for those particular retained parts."
          records:
            - "runtime.md#rt-rte-wiki-answer"
            - "runtime.md#rt-rte-conversation-chat"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-wiki-lint"
            - "memory.md#mem-obj-wiki-index"
          note: "The loader is an automatic selection/delivery operation inside a caller-triggered task, not a background unsolicited workflow. CLI chat holds a session snapshot; Web reloads each request."
        -
          scope: "Human-requested retained-file viewing and citation follow-up"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-browser-read"
                - "epistemic.md#epi-rte-citation-display"
              note: "Explicit file or citation selection requests the retained material, and file delivery fulfills that request."
          records:
            - "memory.md#mem-rte-browser-read"
            - "epistemic.md#epi-rte-citation-display"
          note: "Filename/stem matching on this requested route is not identifier-based push."
        -
          scope: "CLI status/pending-ingest and human accounting reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ingest-log"
                - "memory.md#mem-obj-token-log"
                - "runtime.md#rt-rte-document-ingest"
              note: "Status and pending-processing consumers consult retained ledger records as part of their requested operation."
          records:
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
            - "runtime.md#rt-rte-document-ingest"
          note: "These are control/accounting read-backs, distinct from automatic Wiki context provision."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "runtime.md#rt-rte-wiki-answer"
        - "runtime.md#rt-rte-conversation-chat"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-wiki-lint"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-rte-browser-read"
        - "epistemic.md#epi-rte-citation-display"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "runtime.md#rt-cmp-deepseek"
      note: "Local pull and push operations coexist in request-triggered chains; request initiation does not erase automatic context selection. Provider read-back remains unknown."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Automatic Wiki loader: task/session trigger, availability plus recency/count selector, retained index and pages"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-answer"
                - "runtime.md#rt-rte-conversation-chat"
                - "runtime.md#rt-rte-document-ingest"
                - "runtime.md#rt-rte-wiki-lint"
                - "memory.md#mem-obj-wiki-index"
              note: "Index is always included; available other Markdown pages are ordered by mtime and limited by count, not matched to the question. Ingest uses ten/fifty, answer thirty, chat twenty and lint fifty other pages."
          records:
            - "runtime.md#rt-rte-wiki-answer"
            - "runtime.md#rt-rte-conversation-chat"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-wiki-lint"
            - "memory.md#mem-obj-wiki-index"
          note: "No local input-token clipping or semantic selector is established. Page identifiers merely label delivered content; they do not select it by identity."
        -
          scope: "Explicit browser file/citation and status-ledger requests"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-browser-read"
            - "memory.md#mem-obj-ingest-log"
            - "memory.md#mem-obj-token-log"
          note: "These requests are pull; path/stem/hash lookup does not establish an additional push signal."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "runtime.md#rt-rte-wiki-answer"
        - "runtime.md#rt-rte-conversation-chat"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-wiki-lint"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-rte-browser-read"
        - "memory.md#mem-obj-ingest-log"
        - "memory.md#mem-obj-token-log"
        - "runtime.md#rt-cmp-deepseek"
      note: "The inspected automatic context route uses coarse selection. Pull-only subroutes need no push signal; opaque provider alternatives prevent system-level inapplicability or completeness."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Conversation-history to retained insight to later Wiki generation"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insight-page"
                - "runtime.md#rt-rte-insight-save"
                - "runtime.md#rt-bap-wiki-context"
              note: "Software/model admission converts selected session messages to a durable page eligible for later context. Human initiation does not make the generated-content admission manual."
          records:
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-insight-save"
            - "runtime.md#rt-bap-wiki-context"
          note: "Qualifies as wired trace learning, independently of novelty, model weight change, measured improvement or retention of all raw turns."
        -
          scope: "Document-ingest and ordinary query-archive inputs as possible additional trace-fed updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-answer-archive"
          note: "Records establish document and answer derivation but do not inventory whether arbitrary local documents or generated answers contain additional qualifying recorded experience. No local negative is asserted."
        -
          scope: "Configured cross-session raw-history/summary-cache checkpoint route"
          assessment: "absent"
          findings: []
          records:
            - "memory.md#mem-abs-history-store"
          note: "Bounded search finds no shipped serialization/read-back checkpoint there; this is absence of that route, not a trace-learning no for the whole system."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-insight-page"
        - "runtime.md#rt-rte-insight-save"
        - "runtime.md#rt-bap-wiki-context"
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-answer-archive"
        - "memory.md#mem-abs-history-store"
        - "runtime.md#rt-cmp-deepseek"
      note: "A wired yes exists through insight saving. Other possible input histories and provider updates are unresolved; the bounded history-cache absence does not negate insight learning or justify a system-wide no."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Original recorded user/assistant turns consumed by insight saving"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-insight-page"
                - "runtime.md#rt-rte-insight-save"
              note: "CLI/browser save supplies conversation history through a selected answer, formatted as messages for insight generation."
          records:
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-insight-save"
          note: "Source is recorded conversation, not event-streams merely because a save request is an event. No registered tool-execution stream is established by this route."
        -
          scope: "Possible trace content in arbitrary ingested sources, archived answers and mixed prior Wiki-derived conversation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-page"
            - "memory.md#mem-obj-query-page"
            - "memory.md#mem-obj-insight-page"
            - "runtime.md#rt-rte-document-ingest"
            - "runtime.md#rt-rte-answer-archive"
          note: "Initial source provenance and nested answer origins are not fully known. Session-log origin of the insight input remains supported, but no additional event-stream, tool-trace or trajectory source is established."
        -
          scope: "Remote generation service: any provider-retained state changed through use"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-deepseek"
          note: "Provider weights, hidden state, caching and possible changes are opaque. The service component is not itself proof of an operative accumulated-memory object or route; no provider-memory value is inferred."
      records:
        - "memory.md#mem-obj-insight-page"
        - "runtime.md#rt-rte-insight-save"
        - "memory.md#mem-obj-source-page"
        - "memory.md#mem-obj-query-page"
        - "runtime.md#rt-rte-document-ingest"
        - "runtime.md#rt-rte-answer-archive"
        - "runtime.md#rt-cmp-deepseek"
      note: "Session-logs is supported for the qualifying insight write. Mixed or opaque inputs remain separate rather than being relabeled from their adapter or workflow trigger."
---

# Nemsy memory profile

## Comparison rationale

The inventory separates retained prose, operational metadata, actual consumers and opaque remote state. All findings derive from accepted records; no source file was read for this profile. There is no observed or causal basis in the supplied set. A local wired route supports existence, not complete provider or initialization coverage.

Reconciliation supersedes the epistemic insight-content declaration with [MEM-OBJ-insight-page](memory.md#mem-obj-insight-page); classifications use that canonical output and [RT-RTE-insight-save](runtime.md#rt-rte-insight-save). The summary/questions and index-entry records remain valid portions of their file containers, not additional stores. Citation rendering and browser reading overlap without superseding each other.

Request-triggered does not mean every downstream selection is pull. [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) establishes automatic recency-window provision inside the requested answering task: that operation supplies retained material without a request for those pages. [MEM-RTE-browser-read](memory.md#mem-rte-browser-read) instead fulfills a request for a particular retained file. Only the former establishes coarse push selection. A requested citation's stem match supplies no identifier push finding.

Conversation saving has automatic particular-content admission even when a person chooses the history boundary. The trace-fed result supplies knowledge to later generation; the input experience supplies learning authority at the update consumer. These mappings do not claim improved capacity, semantic acceptance or weight training. [MEM-ABS-history-store](memory.md#mem-abs-history-store) rules out only the searched history/cache checkpoint, not this separate save route.

Consolidation denotes the implemented summary/insight reduction path. [EPI-RTE-summary-cleanup](epistemic.md#epi-rte-summary-cleanup) shows deterministic selection and possible deletion, not novel synthesis. Missing actual inputs/outputs prevent classification of additional semantic synthesis/evolution; lint advice and unsynchronized overwrites do not fill that gap. Initial local authorship/admission and hidden provider retention likewise remain unresolved rather than being dropped to obtain complete coverage.
