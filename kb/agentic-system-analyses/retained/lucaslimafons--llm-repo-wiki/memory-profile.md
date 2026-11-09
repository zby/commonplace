---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "LLM Repo Wiki memory profile: revisioned repository knowledge, retained owner context, conversation folding and diagnostic read-back."
run-id: "AAS-2026-11-09-llm-repo-wiki-55aae7f87b1b-01"
source-identity: "https://github.com/lucaslimafons/llm-repo-wiki"
reviewed-boundary: "38a439cd649105c0cd90b687fc1f8d8dd1d0986c"
memory-comparison:
  version: 2
  scope: "Included: acquired source chunks/access structures, proposed/current/historical wiki prose and citation/tree state, section/vector indexes, editable retained project context, persisted chat messages/summary/cutoff, logs/accounting, diagnostic result/resume files and shipped application/MCP/export consumers. Excluded: unchanged shipped WIKI_SCHEMA.md and other static policy, model weights/provider retention, external indexed-repository authorship history, MCP-host internal memory and ordinary unretained current-run state."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - 
          scope: "Repository chunks, revision prose and citation/current/tree metadata, wiki sections, project state, messages, summary/cutoff and diagnostic/accounting rows"
          assessment: "known"
          findings:
            - 
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-revision-sources"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-wiki-log"
              note: "These operative parts persist in Postgres; row JSON and Markdown are encodings, not file substrates."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-revision-sources"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-obj-wiki-log"
          note: "These operative parts persist in Postgres; row JSON and Markdown are encodings, not file substrates."
        - 
          scope: "Retained dense source and wiki section embeddings used by cosine retrieval"
          assessment: "known"
          findings:
            - 
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-rte-search-knowledge"
              note: "Postgres vectors are an operative vector retrieval substrate as well as database columns."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-rte-search-knowledge"
          note: "Postgres vectors are an operative vector retrieval substrate as well as database columns."
        - 
          scope: "Benchmark transcripts, result JSON and citation judgment/report files; exported accepted Markdown"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-results"
                - "runtime.md#rt-rte-external-consumption"
              note: "Scripts persist diagnostic files and export emits Markdown. External host retention and provider storage are excluded, not inferred."
          records:
            - "memory.md#mem-obj-eval-results"
            - "runtime.md#rt-rte-external-consumption"
          note: "Scripts persist diagnostic files and export emits Markdown. External host retention and provider storage are excluded, not inferred."
      records:
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-page-revisions"
        - "memory.md#mem-obj-revision-sources"
        - "memory.md#mem-obj-wiki-chunks"
        - "memory.md#mem-obj-project-context"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-rte-search-knowledge"
        - "memory.md#mem-obj-eval-results"
        - "runtime.md#rt-rte-external-consumption"
      note: "The accepted object inventory covers application retention and shipped diagnostic/export files. Provider weights and static shipped rules are outside accumulated-memory storage."
    representational_form:
      assessment: "known"
      units:
        - 
          scope: "Repository documentation, wiki bodies/reasons, owner brief/roles, conversation text and summary, diagnostic prose and exported pages"
          assessment: "known"
          findings:
            - 
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-wiki-log"
                - "memory.md#mem-obj-eval-results"
                - "runtime.md#rt-rte-external-consumption"
              note: "These parts reach model or human interpretation as prose."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-eval-results"
            - "runtime.md#rt-rte-external-consumption"
          note: "These parts reach model or human interpretation as prose."
        - 
          scope: "Source code, citation coordinates, identifiers, statuses, tree/current pointers, layout, TSV access material, chat tool/approval structures, cutoff, counters and evaluation verdicts"
          assessment: "known"
          findings:
            - 
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-revision-sources"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-wiki-log"
                - "memory.md#mem-obj-eval-results"
              note: "Localized fields and code are consumed by fixed selection, validation, ordering and bookkeeping rules; this does not turn their neighboring prose into symbolic guidance."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-revision-sources"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-eval-results"
          note: "Localized fields and code are consumed by fixed selection, validation, ordering and bookkeeping rules; this does not turn their neighboring prose into symbolic guidance."
        - 
          scope: "Stored source/wiki dense vectors at cosine-ranking consumer"
          assessment: "known"
          findings:
            - 
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-rte-search-knowledge"
              note: "Dense numerical representations are consumed for similarity, not delivered as prose or trained local weights."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-rte-search-knowledge"
          note: "Dense numerical representations are consumed for similarity, not delivered as prose or trained local weights."
      records:
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-page-revisions"
        - "memory.md#mem-obj-project-context"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-eval-results"
        - "runtime.md#rt-rte-external-consumption"
        - "memory.md#mem-obj-revision-sources"
        - "memory.md#mem-obj-wiki-chunks"
        - "memory.md#mem-rte-search-knowledge"
      note: "Mixed rows and files are split by operative part and consumption path; remote model weights are not accumulated memory of this application."
    lineage:
      assessment: "partial"
      units:
        - 
          scope: "External repository content imported through filtered synchronization"
          assessment: "known"
          findings:
            - 
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "runtime.md#rt-rte-repo-sync"
              note: "The acquisition path is known; original repository authorship is not asserted."
          records:
            - "memory.md#mem-obj-chunks"
            - "runtime.md#rt-rte-repo-sync"
          note: "The acquisition path is known; original repository authorship is not asserted."
        - 
          scope: "Model/human wiki prose and human-facing owner-context replacements"
          assessment: "known"
          findings:
            - 
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-revisions"
                - "runtime.md#rt-rte-author-pages"
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-revision-admission"
                - "memory.md#mem-obj-project-context"
              note: "Known routes author new prose or edit retained prose; this does not recover an installed database's initial authorship."
          records:
            - "memory.md#mem-obj-page-revisions"
            - "runtime.md#rt-rte-author-pages"
            - "runtime.md#rt-rte-chat-turn"
            - "runtime.md#rt-rte-revision-admission"
            - "memory.md#mem-obj-project-context"
          note: "Known routes author new prose or edit retained prose; this does not recover an installed database's initial authorship."
        - 
          scope: "Chunking, section indexing, vectors, TSV, citation/access metadata and exported page formatting"
          assessment: "known"
          findings:
            - 
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-rte-index-page"
                - "memory.md#mem-obj-revision-sources"
                - "runtime.md#rt-rte-external-consumption"
              note: "These derivation paths compile acquired or authored material; the embedding model's training provenance is not thereby established."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-rte-index-page"
            - "memory.md#mem-obj-revision-sources"
            - "runtime.md#rt-rte-external-consumption"
          note: "These derivation paths compile acquired or authored material; the embedding model's training provenance is not thereby established."
        - 
          scope: "Persisted conversation, folded summary, activity accounting and benchmark transcripts/derived diagnostic artifacts"
          assessment: "known"
          findings:
            - 
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-wiki-log"
                - "memory.md#mem-obj-eval-results"
              note: "Messages/logs retain activity; the summary is automatically extracted from conversation/tool history. This lineage does not imply every diagnostic artifact is learned policy."
          records:
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-eval-results"
          note: "Messages/logs retain activity; the summary is automatically extracted from conversation/tool history. This lineage does not imply every diagnostic artifact is learned policy."
        - 
          scope: "Initial installed project/page content and underlying provider embedding provenance"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-wiki-chunks"
          note: "No installed database or original indexed repository was supplied; initial authorship and provider provenance cannot be classified from known subsequent transformations."
      records:
        - "memory.md#mem-obj-chunks"
        - "runtime.md#rt-rte-repo-sync"
        - "memory.md#mem-obj-page-revisions"
        - "runtime.md#rt-rte-author-pages"
        - "runtime.md#rt-rte-chat-turn"
        - "runtime.md#rt-rte-revision-admission"
        - "memory.md#mem-obj-project-context"
        - "memory.md#mem-obj-wiki-chunks"
        - "memory.md#mem-rte-index-page"
        - "memory.md#mem-obj-revision-sources"
        - "runtime.md#rt-rte-external-consumption"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-eval-results"
      note: "Known derivations coexist with unresolved initial content and provider provenance; no complete lineage claim follows."
    behavioral_authority:
      assessment: "known"
      units:
        - 
          scope: "Source/wiki text delivered to author, chat, MCP, export and human diagnostic readers; active chat history and summary as remembered context"
          assessment: "known"
          findings:
            - 
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-search-knowledge"
                - "runtime.md#rt-rte-author-pages"
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-external-consumption"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-bap-summary-context"
                - "memory.md#mem-obj-eval-results"
              note: "Retained content supplies evidence, reference or conversational context; delivery does not prove compliance or truth."
          records:
            - "memory.md#mem-rte-search-knowledge"
            - "runtime.md#rt-rte-author-pages"
            - "runtime.md#rt-rte-chat-turn"
            - "runtime.md#rt-rte-external-consumption"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-bap-summary-context"
            - "memory.md#mem-obj-eval-results"
          note: "Retained content supplies evidence, reference or conversational context; delivery does not prove compliance or truth."
        - 
          scope: "Owner brief/roles at author/chat generation and remembered goals/preferences in summary at later chat"
          assessment: "known"
          findings:
            - 
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-bap-project-brief"
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-bap-summary-context"
                - "memory.md#mem-obj-chat-summary"
              note: "Owner intent and retained decisions/preferences supply directions through instruction composition. Summary facts separately supply knowledge; not every summary sentence is a standing rule."
          records:
            - "memory.md#mem-bap-project-brief"
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-bap-summary-context"
            - "memory.md#mem-obj-chat-summary"
          note: "Owner intent and retained decisions/preferences supply directions through instruction composition. Summary facts separately supply knowledge; not every summary sentence is a standing rule."
        - 
          scope: "Retained chunk text, TSV and dense vectors at query ranking"
          assessment: "known"
          findings:
            - 
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-wiki-chunks"
                - "memory.md#mem-rte-search-knowledge"
              note: "Retained features determine relative retrieval priority even though the fusion policy is fixed code."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-wiki-chunks"
            - "memory.md#mem-rte-search-knowledge"
          note: "Retained features determine relative retrieval priority even though the fusion policy is fixed code."
        - 
          scope: "Revision/citation/tree state, summary cutoff and diagnostic resume pair/judge keys at selection consumers"
          assessment: "known"
          findings:
            - 
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-revision-sources"
                - "memory.md#mem-obj-chat-summary"
                - "runtime.md#rt-rte-context-fold"
                - "epistemic.md#epi-rte-citation-evaluation"
                - "memory.md#mem-obj-eval-results"
              note: "Current/tree/citation state selects content or maintenance scope, cutoff selects active history, and resume keys select missing judge work."
          records:
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-revision-sources"
            - "memory.md#mem-obj-chat-summary"
            - "runtime.md#rt-rte-context-fold"
            - "epistemic.md#epi-rte-citation-evaluation"
            - "memory.md#mem-obj-eval-results"
          note: "Current/tree/citation state selects content or maintenance scope, cutoff selects active history, and resume keys select missing judge work."
        - 
          scope: "Retained status/parent/current IDs at revision acceptance and indexing; stored pending approval structures at chat merge"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-revision-admission"
                - "memory.md#mem-rte-index-page"
                - "memory.md#mem-obj-chat-messages"
                - "runtime.md#rt-rte-chat-turn"
              note: "Stored state supplies admissibility criteria and vetoes outdated/unaccepted or unauthorized changes on the named paths; it is not universal human authentication."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-revision-admission"
                - "memory.md#mem-rte-index-page"
                - "memory.md#mem-obj-chat-messages"
                - "runtime.md#rt-rte-chat-turn"
              note: "Stored state supplies admissibility criteria and vetoes outdated/unaccepted or unauthorized changes on the named paths; it is not universal human authentication."
          records:
            - "runtime.md#rt-rte-revision-admission"
            - "memory.md#mem-rte-index-page"
            - "memory.md#mem-obj-chat-messages"
            - "runtime.md#rt-rte-chat-turn"
          note: "Stored state supplies admissibility criteria and vetoes outdated/unaccepted or unauthorized changes on the named paths; it is not universal human authentication."
        - 
          scope: "Existing citation keys at author draft filtering"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "epistemic.md#epi-obj-source-citations"
              note: "Exact retained citation keys can authorize preservation of a link while other references are stripped; this is reference filtering, not semantic validation."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "epistemic.md#epi-obj-source-citations"
              note: "Exact retained citation keys can authorize preservation of a link while other references are stripped; this is reference filtering, not semantic validation."
          records:
            - "runtime.md#rt-rte-author-pages"
            - "epistemic.md#epi-obj-source-citations"
          note: "Exact retained citation keys can authorize preservation of a link while other references are stripped; this is reference filtering, not semantic validation."
        - 
          scope: "Retained older conversation and prior summary at automatic summary-update consumer"
          assessment: "known"
          findings:
            - 
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "runtime.md#rt-rte-context-fold"
              note: "Retained experience feeds a durable behavior-shaping context update. Its later knowledge/instruction use is a separate path, and improved capacity is unobserved."
          records:
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "runtime.md#rt-rte-context-fold"
          note: "Retained experience feeds a durable behavior-shaping context update. Its later knowledge/instruction use is a separate path, and improved capacity is unobserved."
      records:
        - "memory.md#mem-rte-search-knowledge"
        - "runtime.md#rt-rte-author-pages"
        - "runtime.md#rt-rte-chat-turn"
        - "runtime.md#rt-rte-external-consumption"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-eval-results"
        - "memory.md#mem-bap-project-brief"
        - "memory.md#mem-obj-project-context"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-wiki-chunks"
        - "memory.md#mem-obj-page-revisions"
        - "memory.md#mem-obj-revision-sources"
        - "runtime.md#rt-rte-context-fold"
        - "epistemic.md#epi-rte-citation-evaluation"
        - "runtime.md#rt-rte-revision-admission"
        - "memory.md#mem-rte-index-page"
        - "epistemic.md#epi-obj-source-citations"
      note: "Authorities are attached to actual consumers, not all fields in a row. Diagnostic verdicts are advisory and resumed, not automatically installed production policy."
    write_agency:
      assessment: "partial"
      units:
        - 
          scope: "Source acquisition, model proposal admission, unapproved chat create, indexing, model/tool/server message admission, accounting retention, summary folding and diagnostic output/resume"
          assessment: "known"
          findings:
            - 
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-repo-sync"
                - "runtime.md#rt-rte-author-pages"
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-rte-index-page"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-wiki-log"
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-eval-results"
                - "epistemic.md#epi-rte-citation-evaluation"
              note: "Generated responses, tool results and server-derived message structures are admitted without per-content human approval. Human-supplied user text is classified separately; software persistence alone does not make its admission automatic. Starting a workflow or an author label human in a benchmark does not change generated-content admission."
          records:
            - "runtime.md#rt-rte-repo-sync"
            - "runtime.md#rt-rte-author-pages"
            - "runtime.md#rt-rte-chat-turn"
            - "memory.md#mem-rte-index-page"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-wiki-log"
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-eval-results"
            - "epistemic.md#epi-rte-citation-evaluation"
          note: "Generated responses, tool results and server-derived message structures are admitted without per-content human approval. Human-supplied user text is classified separately; software persistence alone does not make its admission automatic. Starting a workflow or an author label human in a benchmark does not change generated-content admission."
        - 
          scope: "Human-facing supply of user text retained in chat history"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-obj-chat-messages"
              note: "The chat interface affords an explicit human decision supplying the newest user turn, which the server persists. No supplied run establishes exercised human use."
          records:
            - "runtime.md#rt-rte-chat-turn"
            - "memory.md#mem-obj-chat-messages"
          note: "This unit covers human-facing user-text supply, not generated assistant/tool/server material or generic callers whose control is unresolved."
        - 
          scope: "UI accept/reject/direct edit/revert and selected chat update/move/delete approval"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-revision-admission"
                - "runtime.md#rt-rte-chat-turn"
              note: "These paths afford explicit human decisions on the particular content or tool effect; SDK approval execution remains an external contract."
          records:
            - "runtime.md#rt-rte-revision-admission"
            - "runtime.md#rt-rte-chat-turn"
          note: "These paths afford explicit human decisions on the particular content or tool effect; SDK approval execution remains an external contract."
        - 
          scope: "Human-facing project-context replacement"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-bap-project-brief"
              note: "The shipped settings action affords operator-supplied replacement; a generic API caller alone does not establish human control."
          records:
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-bap-project-brief"
          note: "The shipped settings action affords operator-supplied replacement; a generic API caller alone does not establish human control."
        - 
          scope: "Initial installed content and generic project-context API caller control"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-obj-page-revisions"
          note: "Initial admission decisions are unknown, and generic caller identity cannot resolve human versus software control."
      records:
        - "runtime.md#rt-rte-repo-sync"
        - "runtime.md#rt-rte-author-pages"
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-rte-index-page"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-wiki-log"
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-eval-results"
        - "epistemic.md#epi-rte-citation-evaluation"
        - "runtime.md#rt-rte-revision-admission"
        - "memory.md#mem-obj-project-context"
        - "memory.md#mem-bap-project-brief"
        - "memory.md#mem-obj-page-revisions"
      note: "Architectural automatic writes are known separately from afforded human user-text supply, review/editing and approval decisions; initial/generic-caller admission remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - 
          scope: "Conversation-prefix and prior-summary reduction to replacement summary"
          assessment: "known"
          findings:
            - 
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-chat-summary"
              note: "The implemented transformation requests a reduced representation of existing goals, facts and decisions. Unchecked faithfulness does not convert compression into synthesis."
          records:
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-chat-summary"
          note: "The implemented transformation requests a reduced representation of existing goals, facts and decisions. Unchecked faithfulness does not convert compression into synthesis."
        - 
          scope: "Existing-page update proposals, human direct edits/restores and chat approved updates"
          assessment: "known"
          findings:
            - 
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "runtime.md#rt-rte-revision-admission"
                - "runtime.md#rt-rte-chat-turn"
                - "memory.md#mem-obj-page-revisions"
              note: "Known routes revise existing entries; proposal persistence and current-page admission remain separate."
          records:
            - "runtime.md#rt-rte-author-pages"
            - "runtime.md#rt-rte-revision-admission"
            - "runtime.md#rt-rte-chat-turn"
            - "memory.md#mem-obj-page-revisions"
          note: "Known routes revise existing entries; proposal persistence and current-page admission remain separate."
        - 
          scope: "Proposal rejection with historical status retained while page exists"
          assessment: "known"
          findings:
            - 
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-revision-admission"
                - "memory.md#mem-obj-page-revisions"
              note: "Rejection withdraws current reliance on a proposal while retaining historical status on surviving pages; deletion is a separate route."
          records:
            - "runtime.md#rt-rte-revision-admission"
            - "memory.md#mem-obj-page-revisions"
          note: "Rejection withdraws current reliance on a proposal while retaining historical status on surviving pages; deletion is a separate route."
        - 
          scope: "Explicit page/chat/repository withdrawal and destructive author benchmark reset"
          assessment: "known"
          findings:
            - 
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-bench-author"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-chat-messages"
                - "runtime.md#rt-rte-repo-sync"
              note: "Deletion forgets retained local content; it does not retract already exported/provider/host copies."
          records:
            - "memory.md#mem-rte-bench-author"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-chat-messages"
            - "runtime.md#rt-rte-repo-sync"
          note: "Deletion forgets retained local content; it does not retract already exported/provider/host copies."
        - 
          scope: "Semantic novelty versus preservation in generated wiki and chat page content"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "runtime.md#rt-rte-author-pages"
            - "runtime.md#rt-rte-chat-turn"
            - "epistemic.md#epi-obj-page-prose"
          note: "No concrete generated propositions and checked premises establish synthesis or its exhaustive absence; transformations beyond known revision remain indeterminate."
      records:
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-chat-summary"
        - "runtime.md#rt-rte-author-pages"
        - "runtime.md#rt-rte-revision-admission"
        - "runtime.md#rt-rte-chat-turn"
        - "memory.md#mem-obj-page-revisions"
        - "memory.md#mem-rte-bench-author"
        - "memory.md#mem-obj-chat-messages"
        - "runtime.md#rt-rte-repo-sync"
        - "epistemic.md#epi-obj-page-prose"
      note: "Index rebuilds and retrieval-hit deduplication alone are not memory curation. Known consolidation/revision/withdrawal coexist with unresolved semantic transformation."
    read_back_direction:
      assessment: "known"
      units:
        - 
          scope: "Requested search, explicit page/history reads, MCP calls, export and diagnostic resume"
          assessment: "known"
          findings:
            - 
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-search-knowledge"
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-external-consumption"
                - "memory.md#mem-obj-eval-results"
                - "epistemic.md#epi-rte-citation-evaluation"
              note: "A consumer requests retained material or resumed work; returning requested hits is not another push."
          records:
            - "memory.md#mem-rte-search-knowledge"
            - "runtime.md#rt-rte-chat-turn"
            - "runtime.md#rt-rte-external-consumption"
            - "memory.md#mem-obj-eval-results"
            - "epistemic.md#epi-rte-citation-evaluation"
          note: "A consumer requests retained material or resumed work; returning requested hits is not another push."
        - 
          scope: "New chat turn automatically receiving selected active history, summary, tree and owner brief"
          assessment: "known"
          findings:
            - 
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-project-context"
              note: "A turn triggers automatic context assembly without a separate request for these retained parts."
          records:
            - "runtime.md#rt-rte-chat-turn"
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-obj-project-context"
          note: "A turn triggers automatic context assembly without a separate request for these retained parts."
        - 
          scope: "Author job automatically receiving current page, tree/project context and code-selected source evidence"
          assessment: "known"
          findings:
            - 
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "memory.md#mem-obj-project-context"
                - "memory.md#mem-rte-search-knowledge"
              note: "Code supplies retained context to separate writing calls. Code's upstream search requests are pull; downstream unsolicited evidence supply to the writer is push."
          records:
            - "runtime.md#rt-rte-author-pages"
            - "memory.md#mem-obj-project-context"
            - "memory.md#mem-rte-search-knowledge"
          note: "Code supplies retained context to separate writing calls. Code's upstream search requests are pull; downstream unsolicited evidence supply to the writer is push."
      records:
        - "memory.md#mem-rte-search-knowledge"
        - "runtime.md#rt-rte-chat-turn"
        - "runtime.md#rt-rte-external-consumption"
        - "memory.md#mem-obj-eval-results"
        - "epistemic.md#epi-rte-citation-evaluation"
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-obj-project-context"
        - "runtime.md#rt-rte-author-pages"
      note: "Request and automatic delivery are separated within chains; being triggered by a turn/job does not make all context assembly pull."
    read_back_signal:
      assessment: "known"
      units:
        - 
          scope: "Chat-turn context assembly: wiki/chat identity, history cutoff and formatter conditions select summary, tail, tree and project state"
          assessment: "known"
          findings:
            - 
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-project-context"
              note: "Trigger is a new turn. Identity selects the matching chat/wiki retained parts; availability, chronological budget and formatter conditions are coarse selectors, not inferred relevance."
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-chat-turn"
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-obj-project-context"
              note: "Trigger is a new turn. Identity selects the matching chat/wiki retained parts; availability, chronological budget and formatter conditions are coarse selectors, not inferred relevance."
          records:
            - "runtime.md#rt-rte-chat-turn"
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-obj-project-context"
          note: "Trigger is a new turn. Identity selects the matching chat/wiki retained parts; availability, chronological budget and formatter conditions are coarse selectors, not inferred relevance."
        - 
          scope: "Author context assembly: wiki/page and citation-file matching plus stale flags select existing content and maintenance targets"
          assessment: "known"
          findings:
            - 
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-revision-sources"
                - "memory.md#mem-obj-project-context"
              note: "Trigger is an author job. Actual wiki/page/repo/path matches select delivered/updated parts; stale/available/page-budget filtering remains coarse."
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "memory.md#mem-obj-page-revisions"
                - "memory.md#mem-obj-revision-sources"
                - "memory.md#mem-obj-project-context"
              note: "Trigger is an author job. Actual wiki/page/repo/path matches select delivered/updated parts; stale/available/page-budget filtering remains coarse."
          records:
            - "runtime.md#rt-rte-author-pages"
            - "memory.md#mem-obj-page-revisions"
            - "memory.md#mem-obj-revision-sources"
            - "memory.md#mem-obj-project-context"
          note: "Trigger is an author job. Actual wiki/page/repo/path matches select delivered/updated parts; stale/available/page-budget filtering remains coarse."
        - 
          scope: "Author evidence push into draft calls after code-owned query retrieval"
          assessment: "known"
          findings:
            - 
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "memory.md#mem-rte-search-knowledge"
                - "memory.md#mem-obj-chunks"
              note: "Trigger is a page draft/update. Title/path/model-query text feeds cosine and full-text selection of retained source chunks; deduplication/caps clip delivered hits. These signals do not apply to requested page-by-path returns."
            - 
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-author-pages"
                - "memory.md#mem-rte-search-knowledge"
                - "memory.md#mem-obj-chunks"
              note: "Trigger is a page draft/update. Title/path/model-query text feeds cosine and full-text selection of retained source chunks; deduplication/caps clip delivered hits. These signals do not apply to requested page-by-path returns."
          records:
            - "runtime.md#rt-rte-author-pages"
            - "memory.md#mem-rte-search-knowledge"
            - "memory.md#mem-obj-chunks"
          note: "Trigger is a page draft/update. Title/path/model-query text feeds cosine and full-text selection of retained source chunks; deduplication/caps clip delivered hits. These signals do not apply to requested page-by-path returns."
      records:
        - "runtime.md#rt-rte-chat-turn"
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-obj-project-context"
        - "runtime.md#rt-rte-author-pages"
        - "memory.md#mem-obj-page-revisions"
        - "memory.md#mem-obj-revision-sources"
        - "memory.md#mem-rte-search-knowledge"
        - "memory.md#mem-obj-chunks"
      note: "Push signals describe actual selectors, not mere catalog identifiers. Pull-only request returns have no separate push signal."
    trace_learning:
      assessment: "partial"
      units:
        - 
          scope: "Conversation folding: retained messages/tool material plus prior summary to durable summary consumed by later chat"
          assessment: "known"
          findings:
            - 
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-fold"
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "memory.md#mem-bap-summary-context"
              note: "Automatic trace-fed summary production and later instruction-context consumer establish the qualifying wired route, without observed improvement."
          records:
            - "runtime.md#rt-rte-context-fold"
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "memory.md#mem-bap-summary-context"
          note: "Automatic trace-fed summary production and later instruction-context consumer establish the qualifying wired route, without observed improvement."
        - 
          scope: "Other retained activity and diagnostics, including evaluation result/resume and log/accounting routes"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-eval-results"
            - "epistemic.md#epi-rte-citation-evaluation"
            - "memory.md#mem-rte-lint-wiki"
          note: "Records establish retention/status/resume consumers, not qualifying durable behavior-update consumers or a bounded evidenced-absence record. Do not infer a local or system-wide no."
      records:
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "memory.md#mem-bap-summary-context"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-eval-results"
        - "epistemic.md#epi-rte-citation-evaluation"
        - "memory.md#mem-rte-lint-wiki"
      note: "A wired positive is retained; other trace-bearing diagnostic alternatives lack bounded learning classifications. Remote host/provider adaptation is excluded."
    trace_source:
      assessment: "partial"
      units:
        - 
          scope: "Qualifying summary update's recorded user/assistant conversational turns"
          assessment: "known"
          findings:
            - 
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "runtime.md#rt-rte-context-fold"
              note: "Original conversational history feeds summary production, including goals/preferences and assistant text."
          records:
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "runtime.md#rt-rte-context-fold"
          note: "Original conversational history feeds summary production, including goals/preferences and assistant text."
        - 
          scope: "Qualifying summary update's recorded tool requests and results"
          assessment: "known"
          findings:
            - 
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-messages"
                - "memory.md#mem-obj-chat-summary"
                - "runtime.md#rt-rte-context-fold"
              note: "Tool inputs/outputs are clipped to 300/400 characters before generation, but remain tool-origin trace input; source-url display strings are not full source payloads."
          records:
            - "memory.md#mem-obj-chat-messages"
            - "memory.md#mem-obj-chat-summary"
            - "runtime.md#rt-rte-context-fold"
          note: "Tool inputs/outputs are clipped to 300/400 characters before generation, but remain tool-origin trace input; source-url display strings are not full source payloads."
        - 
          scope: "Unresolved qualifying status of diagnostic/log alternatives"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-wiki-log"
            - "memory.md#mem-obj-eval-results"
            - "epistemic.md#epi-rte-citation-evaluation"
          note: "Without a qualifying automatic behavior-update consumer, no trace-source learning classification or inapplicability can be assigned to these alternatives."
      records:
        - "memory.md#mem-obj-chat-messages"
        - "memory.md#mem-obj-chat-summary"
        - "runtime.md#rt-rte-context-fold"
        - "memory.md#mem-obj-wiki-log"
        - "memory.md#mem-obj-eval-results"
        - "epistemic.md#epi-rte-citation-evaluation"
      note: "Summary input origins are classified independently of JSON labels. Diagnostics cannot be made inapplicable by the known summary route."
---

# LLM Repo Wiki memory profile

## Comparison rationale

This profile classifies accepted records, not a deployed database. All wired findings concern inspected architecture. No supplied run or experiment establishes activation, reliable summary preservation, factual accuracy or benefit. The inventory and its limits follow [MEM-OBJ-chunks](memory.md#mem-obj-chunks), [MEM-OBJ-page-revisions](memory.md#mem-obj-page-revisions), [MEM-OBJ-project-context](memory.md#mem-obj-project-context), [MEM-OBJ-chat-messages](memory.md#mem-obj-chat-messages), [MEM-OBJ-chat-summary](memory.md#mem-obj-chat-summary) and [MEM-OBJ-eval-results](memory.md#mem-obj-eval-results). Diagnostic results are included because citation evaluation really reloads prior pairs and judgments, not because every report becomes production memory.

The only reconciliation supersession replaces the epistemic lint route with [MEM-RTE-lint-wiki](memory.md#mem-rte-lint-wiki). This profile uses that canonical destination. Object containers and projections remain distinct; no other supersession changes a value.

**Database versus vector versus files.** Dense vectors share Postgres rows with text, but their numerical form and cosine-ranking consumer warrant separate vector and parametric findings. Repository acquisition does not make the application's retained database a Git repository substrate. Exported Markdown and evaluator result files add files, not an inferred remote service store. See [MEM-OBJ-chunks](memory.md#mem-obj-chunks), [MEM-OBJ-wiki-chunks](memory.md#mem-obj-wiki-chunks), [MEM-RTE-search-knowledge](memory.md#mem-rte-search-knowledge) and [RT-RTE-external-consumption](runtime.md#rt-rte-external-consumption).

**Admission is not authorship.** Automatic source writes, proposal generation, chat creation, model/tool/server message admission and summary admission coexist with afforded human supply of retained user turns, review/editing and selected tool approval. The human-facing chat path lets the user decide what text to supply; server persistence does not convert that admission decision to automatic control. A benchmark's human author label does not establish manual admission. Initial installed provenance and generic project API caller control remain unresolved, rather than erasing known subsequent mechanisms. See [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission) and [MEM-OBJ-project-context](memory.md#mem-obj-project-context).

**Read-back has several operations.** The memory member's observation that routes are job/turn/request-triggered rules out an independent unsolicited daemon, not automatic push within context assembly. A requested search response is pull. A turn's automatic summary/project/history injection and code-selected evidence delivered to a separate writer are push under this profile's contract. Identity matching selects actual chat/wiki/page parts; budgets and availability are separate coarse filters. Author evidence selection uses embedding and lexical signals. No inferred-judgment signal is assigned merely because a model writes query strings or summary prose. See [RT-RTE-context-fold](runtime.md#rt-rte-context-fold), [RT-RTE-author-pages](runtime.md#rt-rte-author-pages), [MEM-RTE-search-knowledge](memory.md#mem-rte-search-knowledge) and [MEM-BAP-project-brief](memory.md#mem-bap-project-brief).

**Consolidation does not prove fidelity or novelty.** Folding is implemented reduction of retained conversation into a durable summary. Its requested compression supports consolidate even though preservation is unchecked. Existing-page replacement supports evolve, rejection with surviving history supports invalidate, and explicit forgetting supports decay. Chunking/index replacement and deduplicating retrieval hits do not alone establish consolidate or dedup over retained memory. No concrete generated proposition establishes synthesize; the indeterminate semantic routes remain included, as [RT-RTE-author-pages](runtime.md#rt-rte-author-pages) and [EPI-OBJ-page-prose](epistemic.md#epi-obj-page-prose) require.

**Trace learning is a write-route classification, not measured improvement.** Stored conversational turns and clipped tool requests/results feed automatic folding; its persisted output enters later chat instructions. This warrants a local wired "yes", session-logs and tool-traces. It does not warrant event-streams merely from log serialization, trajectories merely from sequential messages, or provider weight learning. The input's learning authority at the update consumer differs from summary knowledge/instruction authority at later chat. Diagnostic retention/resume has no established automatic production adoption and no canonical evidenced-absence record supporting "no"; those alternatives remain unresolved. The derived union therefore contains "yes" without a complete learning-inventory claim. See [RT-RTE-context-fold](runtime.md#rt-rte-context-fold), [MEM-BAP-summary-context](memory.md#mem-bap-summary-context), [MEM-OBJ-wiki-log](memory.md#mem-obj-wiki-log) and [EPI-RTE-citation-evaluation](epistemic.md#epi-rte-citation-evaluation).

Source-read log: none. Classification required no additional source reads; accepted member records supplied the warrants and retained passages.
