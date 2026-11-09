---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "WikiBrain memory comparison of retained workspace pages, rule stores, navigation, snapshots, conversations, job-derived context and attachments."
run-id: "AAS-2026-11-08-wikibrain-f815b0976cda-01"
source-identity: "https://github.com/wikibrain-app/wikibrain"
reviewed-boundary: "32cc135877c8d7cd7be997ce57f25bb83128d891"
memory-comparison:
  version: 2
  scope: "Retained local raw/wiki/schema notes; parsed access metadata; note snapshots; delivered template comparison bases and editable custom bundles; saved conversations and job-derived summaries/fallback; image attachments; their admission, maintenance and later model/human delivery routes. Includes generic client-content and admission uncertainty. Excludes shipped static files until admitted into these stores, inference-service weights, external-client private context/state, private hosted operations, transient per-job model arrays and unretained structural-check returns. Exported files are downstream delivery copies, not an independent operative store."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Live raw, wiki and schema pages; derived links/tags; note versions"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-links-tags"
                - "memory.md#mem-obj-note-versions"
              note: "PostgreSQL holds Markdown, parsed access rows and snapshots; slash-delimited paths are logical identifiers, not filesystem storage."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-links-tags"
            - "memory.md#mem-obj-note-versions"
          note: "PostgreSQL holds Markdown, parsed access rows and snapshots; slash-delimited paths are logical identifiers, not filesystem storage."
        -
          scope: "Saved chat messages and diagnostic job events"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-obj-ingest-jobs"
              note: "Conversation JSON and bounded job-event logs are retained in PostgreSQL."
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-obj-ingest-jobs"
          note: "Conversation JSON and bounded job-event logs are retained in PostgreSQL."
        -
          scope: "Delivered template bases and editable custom bundles"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-template-state"
                - "memory.md#mem-obj-user-templates"
              note: "Both upstream rule stores are PostgreSQL content/JSON, separate from live rules."
          records:
            - "memory.md#mem-obj-template-state"
            - "memory.md#mem-obj-user-templates"
          note: "Both upstream rule stores are PostgreSQL content/JSON, separate from live rules."
        -
          scope: "Attachment payloads and associated metadata"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-assets"
              note: "Payload bytea and metadata reside in PostgreSQL; exported files are delivery copies, not the operative store."
          records:
            - "memory.md#mem-obj-assets"
          note: "Payload bytea and metadata reside in PostgreSQL; exported files are delivery copies, not the operative store."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-links-tags"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-chat-sessions"
        - "runtime.md#rt-obj-ingest-jobs"
        - "memory.md#mem-obj-template-state"
        - "memory.md#mem-obj-user-templates"
        - "memory.md#mem-obj-assets"
      note: "The accepted memory inventory covers the retained local objects and their access structures. Remote inference weights and external-client private state are outside this memory boundary, not opaque local memory alternatives. Temporary model arrays and structural function returns are not retained stores."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Raw/wiki/schema prose and saved conversation content at model or human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-chat-sessions"
              note: "Prose receives consequences through model/human interpretation, including catalog descriptions and instructions."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-chat-sessions"
          note: "Prose receives consequences through model/human interpretation, including catalog descriptions and instructions."
        -
          scope: "Paths, frontmatter controls, parsed links/tags and snapshot recovery selectors"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-links-tags"
                - "memory.md#mem-obj-note-versions"
              note: "Localized fields and SQL predicates determine navigation, eligibility and recovery."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-links-tags"
            - "memory.md#mem-obj-note-versions"
          note: "Localized fields and SQL predicates determine navigation, eligibility and recovery."
        -
          scope: "Snapshot bodies, delivered rule bases and custom template text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-template-state"
                - "memory.md#mem-obj-user-templates"
              note: "Text is later displayed, copied, merged or admitted as live prose."
          records:
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-obj-template-state"
            - "memory.md#mem-obj-user-templates"
          note: "Text is later displayed, copied, merged or admitted as live prose."
        -
          scope: "Template hashes/versions/path maps and chat/job status metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-template-state"
                - "memory.md#mem-obj-user-templates"
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-obj-ingest-jobs"
              note: "Fixed comparison, role/status and projection rules consume these fields."
          records:
            - "memory.md#mem-obj-template-state"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-obj-ingest-jobs"
          note: "Fixed comparison, role/status and projection rules consume these fields."
        -
          scope: "Diagnostic text/results in job events"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
              note: "Readable tool/model text is retained alongside symbolic event structure."
          records:
            - "runtime.md#rt-obj-ingest-jobs"
          note: "Readable tool/model text is retained alongside symbolic event structure."
        -
          scope: "Attachment metadata and SVG markup where present"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-assets"
              note: "IDs, MIME and embedded markup have localized encoding; image bytes are not learned parameters."
          records:
            - "memory.md#mem-obj-assets"
          note: "IDs, MIME and embedded markup have localized encoding; image bytes are not learned parameters."
        -
          scope: "Image payload visual content at browser/shared-page consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-assets"
            - "memory.md#mem-rte-human-delivery"
          note: "Encoded images do not establish any listed form for their visual content. Rendering/multimodal interpretation is not classified by these records; no parametric or natural-language payload conclusion follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-chat-sessions"
        - "memory.md#mem-obj-links-tags"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-template-state"
        - "memory.md#mem-obj-user-templates"
        - "runtime.md#rt-obj-ingest-jobs"
        - "memory.md#mem-obj-assets"
        - "memory.md#mem-rte-human-delivery"
      note: "Text and code-consumed fields are classified separately. The included visual payload cannot be forced into the three controlled forms. No vector or model-weight memory follows from image encoding."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Converted sources and template-supplied initial pages/rules"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-rte-source-admission"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-schema"
              note: "External capture and built-in/custom template application bring existing content into local memory; raw location alone does not guarantee this provenance."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-rte-source-admission"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-schema"
          note: "External capture and built-in/custom template application bring existing content into local memory; raw location alone does not guarantee this provenance."
        -
          scope: "Directly supplied/edited notes and custom bundle content"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-user-templates"
                - "runtime.md#rt-rte-client-tools"
              note: "Caller or model can supply original content; authored does not imply human control, truth or original external authorship."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-user-templates"
            - "runtime.md#rt-rte-client-tools"
          note: "Caller or model can supply original content; authored does not imply human control, truth or original external authorship."
        -
          scope: "Derived links/tags, note snapshots, delivered bases and template snapshots"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-links-tags"
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-template-state"
                - "memory.md#mem-obj-user-templates"
              note: "Parsing, copying and deterministic snapshot/merge paths compile retained material without requiring a trace input."
          records:
            - "memory.md#mem-obj-links-tags"
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-obj-template-state"
            - "memory.md#mem-obj-user-templates"
          note: "Parsing, copying and deterministic snapshot/merge paths compile retained material without requiring a trace input."
        -
          scope: "Automatic source-to-wiki derivation"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "memory.md#mem-obj-wiki"
              note: "Models compile retained source pages into persistent wiki content; semantic novelty remains indeterminate."
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "memory.md#mem-obj-wiki"
          note: "Models compile retained source pages into persistent wiki content; semantic novelty remains indeterminate."
        -
          scope: "Saved session prose and discussion-fed wiki derivation"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-sessions"
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-chat-session"
              note: "Conversation activity is retained/projected into later history and can feed automatic compilation; it is not the full historical tool episode."
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-chat-session"
          note: "Conversation activity is retained/projected into later history and can feed automatic compilation; it is not the full historical tool episode."
        -
          scope: "Diagnostic event summaries and fallback text"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
                - "memory.md#mem-obj-chat-sessions"
              note: "Clipped job events feed readable summaries and the written-path fallback; these projections are distinct from full model-visible tool results."
          records:
            - "runtime.md#rt-obj-ingest-jobs"
            - "memory.md#mem-obj-chat-sessions"
          note: "Clipped job events feed readable summaries and the written-path fallback; these projections are distinct from full model-visible tool results."
        -
          scope: "Uploaded/downloaded attachment acquisition"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-assets"
              note: "Upload/download routes import payloads; source URL is not proof of authenticity."
          records:
            - "memory.md#mem-obj-assets"
          note: "Upload/download routes import payloads; source URL is not proof of authenticity."
        -
          scope: "Initial provenance of arbitrary direct-client content and custom bundle inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-client-tools"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-obj-raw"
          note: "The API accepts caller bytes without establishing whether they were originally authored, imported, or derived from uninspected external traces. Known local copying does not resolve that upstream provenance."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-rte-source-admission"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-user-templates"
        - "runtime.md#rt-rte-client-tools"
        - "memory.md#mem-obj-links-tags"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-template-state"
        - "runtime.md#rt-rte-ingest-job"
        - "memory.md#mem-obj-chat-sessions"
        - "memory.md#mem-rte-discussion-guidance"
        - "runtime.md#rt-rte-chat-session"
        - "runtime.md#rt-obj-ingest-jobs"
        - "memory.md#mem-obj-assets"
      note: "Known derivation paths coexist with unresolved initial caller provenance. No claim is made about every source author's history or capture fidelity."
    behavioral_authority:
      assessment: "known"
      units:
        -
          scope: "Raw/wiki prose, snapshot views and chat history at later model/human readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-chat-sessions"
                - "memory.md#mem-rte-note-retrieval"
              note: "Retained content supplies reference or context; delivery does not prove compliance or improved answers."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-obj-chat-sessions"
            - "memory.md#mem-rte-note-retrieval"
          note: "Retained content supplies reference or context; delivery does not prove compliance or improved answers."
        -
          scope: "Live schema at the requesting model/client"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-schema"
                - "runtime.md#rt-bap-schema-instructions"
              note: "Requested rule text supplies standing directions, not an executor-enforced semantic invariant."
          records:
            - "memory.md#mem-obj-schema"
            - "runtime.md#rt-bap-schema-instructions"
          note: "Requested rule text supplies standing directions, not an executor-enforced semantic invariant."
        -
          scope: "Catalog prose at the model choosing subsequent pages"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-rte-note-retrieval"
              note: "The interpreted index guides subsequent page selection; index-first use is requested, not forced."
          records:
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-rte-note-retrieval"
          note: "The interpreted index guides subsequent page selection; index-first use is requested, not forced."
        -
          scope: "Note title/body, tags/folders and modification metadata at lexical search"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-retrieval"
                - "memory.md#mem-obj-links-tags"
              note: "Retained fields affect query matching and newest-first result priority; ranking does not require learned retrieval."
          records:
            - "memory.md#mem-rte-note-retrieval"
            - "memory.md#mem-obj-links-tags"
          note: "Retained fields affect query matching and newest-first result priority; ranking does not require learned retrieval."
        -
          scope: "Link/path and session selectors at pending scheduling, retrieval and history selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-links-tags"
                - "epistemic.md#epi-rte-pending-selection"
                - "memory.md#mem-rte-note-retrieval"
                - "runtime.md#rt-rte-chat-session"
              note: "Retained relationships/identities choose compilation targets or content scope; backlinks do not validate compilation quality."
          records:
            - "memory.md#mem-obj-links-tags"
            - "epistemic.md#epi-rte-pending-selection"
            - "memory.md#mem-rte-note-retrieval"
            - "runtime.md#rt-rte-chat-session"
          note: "Retained relationships/identities choose compilation targets or content scope; backlinks do not validate compilation quality."
        -
          scope: "Current versions and delivered template bases at update/merge admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-template-state"
                - "runtime.md#rt-rte-rule-update"
                - "memory.md#mem-rte-state-withdrawal"
              note: "Stored versions/text/hashes supply comparison criteria; stale updates and safe-mode conflicts can veto replacement. They do not evaluate semantic merit."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-template-state"
                - "runtime.md#rt-rte-rule-update"
                - "memory.md#mem-rte-state-withdrawal"
              note: "Stored versions/text/hashes supply comparison criteria; stale updates and safe-mode conflicts can veto replacement. They do not evaluate semantic merit."
          records:
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-obj-template-state"
            - "runtime.md#rt-rte-rule-update"
            - "memory.md#mem-rte-state-withdrawal"
          note: "Stored versions/text/hashes supply comparison criteria; stale updates and safe-mode conflicts can veto replacement. They do not evaluate semantic merit."
        -
          scope: "Deleted/archive state and retained share credentials at later read gates"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-withdrawal"
                - "memory.md#mem-rte-human-delivery"
              note: "State excludes ordinary reads, pending entries or revoked shared access; archive does not bar exact reads/search."
          records:
            - "memory.md#mem-rte-state-withdrawal"
            - "memory.md#mem-rte-human-delivery"
          note: "State excludes ordinary reads, pending entries or revoked shared access; archive does not bar exact reads/search."
        -
          scope: "Retained discussion transcript at the automatic wiki-writing consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-ingest-job"
              note: "Retained conversational experience feeds automatically admitted durable wiki artifacts available to later readers. This update-consumer force does not classify ordinary history copying or assert improved capacity."
          records:
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-ingest-job"
          note: "The unit covers only discussion-fed compilation. Ordinary saved role/content projection supplies context, classified as knowledge in the reader unit; its copying alone establishes no learning authority. Qualifying derivation on ordinary-history branches remains not-determinable under trace_learning."
        -
          scope: "Job events at fallback/summary construction and terminal display"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
                - "memory.md#mem-obj-chat-sessions"
              note: "Event-derived written paths select fallback text; readable diagnostics inform the browser. Truncated success parsing limits their evidentiary authority."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
                - "memory.md#mem-obj-chat-sessions"
              note: "Event-derived written paths select fallback text; readable diagnostics inform the browser. Truncated success parsing limits their evidentiary authority."
          records:
            - "runtime.md#rt-obj-ingest-jobs"
            - "memory.md#mem-obj-chat-sessions"
          note: "Event-derived written paths select fallback text; readable diagnostics inform the browser. Truncated success parsing limits their evidentiary authority."
        -
          scope: "Attachment bytes at browser/share/export readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-assets"
                - "memory.md#mem-rte-human-delivery"
              note: "Payloads are reference material for recipients, not established binary model inputs."
          records:
            - "memory.md#mem-obj-assets"
            - "memory.md#mem-rte-human-delivery"
          note: "Payloads are reference material for recipients, not established binary model inputs."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-chat-sessions"
        - "memory.md#mem-rte-note-retrieval"
        - "memory.md#mem-obj-schema"
        - "runtime.md#rt-bap-schema-instructions"
        - "memory.md#mem-obj-links-tags"
        - "epistemic.md#epi-rte-pending-selection"
        - "runtime.md#rt-rte-chat-session"
        - "memory.md#mem-obj-template-state"
        - "runtime.md#rt-rte-rule-update"
        - "memory.md#mem-rte-state-withdrawal"
        - "memory.md#mem-rte-human-delivery"
        - "memory.md#mem-rte-discussion-guidance"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-obj-ingest-jobs"
        - "memory.md#mem-obj-assets"
      note: "This inventory classifies recorded consumer effects, not every possible claim in uninspected template prose or external clients. Template bundles/bases are not standing instructions before application; metadata with no consumer is assigned no force. Learning here describes a trace-update path, not successful learning in the broader epistemic sense."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Built-in ingest/chat/lint tools, including noncanonical schema writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-chat-session"
                - "runtime.md#rt-rte-lint-job"
                - "runtime.md#rt-rte-schema-spelling"
              note: "Model/software admits individual content without per-page human approval; starting the job is not manual admission."
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-chat-session"
            - "runtime.md#rt-rte-lint-job"
            - "runtime.md#rt-rte-schema-spelling"
          note: "Model/software admits individual content without per-page human approval; starting the job is not manual admission."
        -
          scope: "Scheduled Zotero admission and software-derived snapshots/navigation/bases/history"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-source-admission"
                - "memory.md#mem-obj-links-tags"
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-obj-template-state"
                - "memory.md#mem-obj-chat-sessions"
              note: "Scheduling, parsing, copying and saved replies/history proceed without per-item human content decisions."
          records:
            - "memory.md#mem-rte-source-admission"
            - "memory.md#mem-obj-links-tags"
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-obj-template-state"
            - "memory.md#mem-obj-chat-sessions"
          note: "Scheduling, parsing, copying and saved replies/history proceed without per-item human content decisions."
        -
          scope: "Browser note editing, source selection and answer filing"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-withdrawal"
                - "memory.md#mem-rte-source-admission"
                - "runtime.md#rt-rte-chat-session"
              note: "These specific human-facing paths supply/edit/select the retained content explicitly; generic API actors are not included in this unit."
          records:
            - "memory.md#mem-rte-state-withdrawal"
            - "memory.md#mem-rte-source-admission"
            - "runtime.md#rt-rte-chat-session"
          note: "These specific human-facing paths supply/edit/select the retained content explicitly; generic API actors are not included in this unit."
        -
          scope: "Discussion-guided compilation output admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-ingest-job"
              note: "The user selects an episode, but models choose and software admits the resulting page text without per-page approval."
          records:
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-ingest-job"
          note: "The user selects an episode, but models choose and software admits the resulting page text without per-page approval."
        -
          scope: "Browser-selected discussion guidance and rule overwrite choice"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-rule-update"
              note: "The human-facing actions explicitly choose the transcript or replacement rules; downstream automatic wiki writes are a different mechanism."
          records:
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-rule-update"
          note: "The human-facing actions explicitly choose the transcript or replacement rules; downstream automatic wiki writes are a different mechanism."
        -
          scope: "Generic MCP/REST writes, API template/bundle actions, rollback and import/asset callers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-client-tools"
            - "runtime.md#rt-rte-rule-update"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-rte-state-withdrawal"
            - "memory.md#mem-rte-source-admission"
            - "memory.md#mem-obj-assets"
          note: "Authorization and actor strings do not settle whether the caller is a human making a content decision or software. The same physical write function cannot resolve these alternative admissions."
      records:
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-chat-session"
        - "runtime.md#rt-rte-lint-job"
        - "runtime.md#rt-rte-schema-spelling"
        - "memory.md#mem-rte-source-admission"
        - "memory.md#mem-obj-links-tags"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-template-state"
        - "memory.md#mem-obj-chat-sessions"
        - "memory.md#mem-rte-state-withdrawal"
        - "memory.md#mem-rte-discussion-guidance"
        - "runtime.md#rt-rte-rule-update"
        - "runtime.md#rt-rte-client-tools"
        - "memory.md#mem-obj-user-templates"
        - "memory.md#mem-obj-assets"
      note: "Manual and automatic routes are both wired, with caller control unresolved on generic authorized interfaces. Human ownership doctrine is not proof of universal human admission."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing page replacement, optimistic update, rollback and template merge/overwrite"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-chat-session"
                - "runtime.md#rt-rte-rule-update"
                - "memory.md#mem-rte-state-withdrawal"
              note: "Wired operations revise an existing retained entry; rollback copies historical content into a new version."
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-chat-session"
            - "runtime.md#rt-rte-rule-update"
            - "memory.md#mem-rte-state-withdrawal"
          note: "Wired operations revise an existing retained entry; rollback copies historical content into a new version."
        -
          scope: "Soft delete/reset and archive's pending-only withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-withdrawal"
              note: "Visibility/reliance is withdrawn while history/content can survive; archive invalidation is limited to pending selection."
          records:
            - "memory.md#mem-rte-state-withdrawal"
          note: "Visibility/reliance is withdrawn while history/content can survive; archive invalidation is limited to pending selection."
        -
          scope: "Scheduled expiration of old non-current snapshots"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-note-versions"
                - "memory.md#mem-rte-state-withdrawal"
              note: "Age/plan predicates forget recoverable history, excluding the current snapshot."
          records:
            - "memory.md#mem-obj-note-versions"
            - "memory.md#mem-rte-state-withdrawal"
          note: "Age/plan predicates forget recoverable history, excluding the current snapshot."
        -
          scope: "Requested source summaries, semantic consolidation and cross-source synthesis"
          assessment: "partial"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "memory.md#mem-obj-wiki"
              note: "The compilation contract requests source summaries; this is intended compression, not an observed faithful transformation."
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "memory.md#mem-obj-wiki"
            - "epistemic.md#epi-rte-semantic-check"
          note: "Model-backed compilation and maintenance can transform retained claims, but no concrete inputs/outputs establish semantic preservation, new claims, deduplication or promotion. A synthesis page label alone cannot establish synthesize."
        -
          scope: "Conversation projection, answer filing, custom snapshots and derived metadata as semantic curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "memory.md#mem-rte-discussion-guidance"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-obj-links-tags"
          note: "Copying, tail slicing, log reset and index rebuilding do not by themselves establish any listed semantic curation operation. These records provide no complete bounded absence warrant for all content transformations."
      records:
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-chat-session"
        - "runtime.md#rt-rte-rule-update"
        - "memory.md#mem-rte-state-withdrawal"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-wiki"
        - "epistemic.md#epi-rte-semantic-check"
        - "memory.md#mem-obj-chat-sessions"
        - "memory.md#mem-rte-discussion-guidance"
        - "memory.md#mem-obj-user-templates"
        - "memory.md#mem-obj-links-tags"
      note: "Implemented revision, withdrawal and expiry are distinguished from requested model behavior. Initial acquisition, unique-key skips and rebuilding access rows do not establish dedup. No supported semantic synthesis value is inferred from the product name or output type."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Requested note/schema/search, history views, sharing and export"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-note-retrieval"
                - "runtime.md#rt-bap-schema-instructions"
                - "memory.md#mem-rte-human-delivery"
                - "memory.md#mem-obj-note-versions"
              note: "Requested return remains pull even when code adds pending hints or chooses lexical matches inside the response."
          records:
            - "memory.md#mem-rte-note-retrieval"
            - "runtime.md#rt-bap-schema-instructions"
            - "memory.md#mem-rte-human-delivery"
            - "memory.md#mem-obj-note-versions"
          note: "Requested return remains pull even when code adds pending hints or chooses lexical matches inside the response."
        -
          scope: "Next-turn saved conversation delivery"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-rte-chat-session"
              note: "A new message triggers automatic loading of the selected session's prior role/content prose without a separate consumer request for each historical message."
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "A new message triggers automatic loading of the selected session's prior role/content prose without a separate consumer request for each historical message."
        -
          scope: "Discussion-selected transcript guidance delivered to compilation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
              note: "The browser action selects retained episode text, filters failures and supplies its tail as task guidance; the compilation model did not request that retained transcript."
          records:
            - "memory.md#mem-rte-discussion-guidance"
          note: "The browser action selects retained episode text, filters failures and supplies its tail as task guidance; the compilation model did not request that retained transcript."
        -
          scope: "Default ingest target selection from retained pending-source metadata"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-pending-selection"
                - "runtime.md#rt-rte-ingest-job"
              note: "When explicit targets are absent, code supplies pending paths/titles to the model task. Full source bodies still require requested reads."
          records:
            - "epistemic.md#epi-rte-pending-selection"
            - "runtime.md#rt-rte-ingest-job"
          note: "When explicit targets are absent, code supplies pending paths/titles to the model task. Full source bodies still require requested reads."
      records:
        - "memory.md#mem-rte-note-retrieval"
        - "runtime.md#rt-bap-schema-instructions"
        - "memory.md#mem-rte-human-delivery"
        - "memory.md#mem-obj-note-versions"
        - "memory.md#mem-obj-chat-sessions"
        - "runtime.md#rt-rte-chat-session"
        - "memory.md#mem-rte-discussion-guidance"
        - "epistemic.md#epi-rte-pending-selection"
        - "runtime.md#rt-rte-ingest-job"
      note: "Both delivery directions occur at distinct operations. External-client private preload policies are excluded; retained rule/source tool responses are not recounted as push merely because server code delivers them."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "New chat turn: selected session history to provider input"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-rte-chat-session"
              note: "Trigger is the next turn; workspace/session identity selects the stored conversation whose role/content messages are delivered. This is an actual match selecting delivered history, not a path on a requested file."
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "Trigger is the next turn; workspace/session identity selects the stored conversation whose role/content messages are delivered. This is an actual match selecting delivered history, not a path on a requested file."
        -
          scope: "Discussion-ingest browser action: session transcript to compilation guidance"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
              note: "The chosen session and pending raw-path match gate the action; nonfailed-message filtering and the last-12000-character tail select available transcript text. No relevance judgment selector is implemented."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
              note: "The chosen session and pending raw-path match gate the action; nonfailed-message filtering and the last-12000-character tail select available transcript text. No relevance judgment selector is implemented."
          records:
            - "memory.md#mem-rte-discussion-guidance"
          note: "The chosen session and pending raw-path match gate the action; nonfailed-message filtering and the last-12000-character tail select available transcript text. No relevance judgment selector is implemented."
        -
          scope: "Default ingest request: pending source paths/titles supplied to task"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-pending-selection"
                - "memory.md#mem-obj-links-tags"
              note: "Trigger is ingest without explicit paths; live raw availability, archive exclusion and absence of live wiki inbound links select the pending set, not a query-specific semantic match."
          records:
            - "epistemic.md#epi-rte-pending-selection"
            - "memory.md#mem-obj-links-tags"
          note: "Trigger is ingest without explicit paths; live raw availability, archive exclusion and absence of live wiki inbound links select the pending set, not a query-specific semantic match."
      records:
        - "memory.md#mem-obj-chat-sessions"
        - "runtime.md#rt-rte-chat-session"
        - "memory.md#mem-rte-discussion-guidance"
        - "epistemic.md#epi-rte-pending-selection"
        - "memory.md#mem-obj-links-tags"
      note: "Signals cover the push operations above. Lexical search is a pull operation and therefore does not add inferred-lexical here; model page choices after requested retrieval do not independently establish push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Saved chat prose and next-turn history without a derived update"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "Raw conversation retention and reloading alone do not establish a qualifying automatic derivation. The records do not isolate whether ordinary finalText is a trace-derived continuation artifact on every branch. The separately traced fallback and discussion-to-wiki chains below establish positives without upgrading all message retention."
        -
          scope: "Discussion transcript to automatically written, later-readable wiki"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-ingest-job"
                - "memory.md#mem-rte-note-retrieval"
              note: "An operator starts compilation, but software/model admits the resulting durable pages without per-page approval; the original input includes retained conversational traces."
          records:
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-ingest-job"
            - "memory.md#mem-rte-note-retrieval"
          note: "An operator starts compilation, but software/model admits the resulting durable pages without per-page approval; the original input includes retained conversational traces."
        -
          scope: "Diagnostic tool events through chat summaries/fallback into retained prose"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-rte-chat-session"
              note: "Event-derived written-path fallback can become retained assistant content delivered on a later turn. Mere log storage is not the warrant; the fallback-to-history chain is."
          records:
            - "runtime.md#rt-obj-ingest-jobs"
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "Event-derived written-path fallback can become retained assistant content delivered on a later turn. Mere log storage is not the warrant; the fallback-to-history chain is."
        -
          scope: "Generic external-client/custom-content writes and uninspected source-content origins"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-client-tools"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-rte-source-admission"
          note: "Records do not settle whether these inputs contain activity traces or whether opaque callers automatically derive behavior-shaping content. They support neither a qualifying positive nor a bounded local no."
      records:
        - "memory.md#mem-obj-chat-sessions"
        - "runtime.md#rt-rte-chat-session"
        - "memory.md#mem-rte-discussion-guidance"
        - "runtime.md#rt-rte-ingest-job"
        - "memory.md#mem-rte-note-retrieval"
        - "runtime.md#rt-obj-ingest-jobs"
        - "runtime.md#rt-rte-client-tools"
        - "memory.md#mem-obj-user-templates"
        - "memory.md#mem-rte-source-admission"
      note: "Supported automatic trace-to-context/wiki chains establish yes locally. Unresolved caller/input alternatives prevent complete learning-inventory coverage. No evidenced-absence records support any local no; broad claims about improvement, reflection or weight training are not inferred."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Discussion transcript feeding automatic wiki compilation"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-discussion-guidance"
                - "runtime.md#rt-rte-ingest-job"
              note: "Recorded conversational turns are the original input to the automatic page-writing route; an operator selects the episode but does not approve each generated page."
          records:
            - "memory.md#mem-rte-discussion-guidance"
            - "runtime.md#rt-rte-ingest-job"
          note: "Both user and assistant turns contribute; role-labeled guidance does not change their conversational origin."
        -
          scope: "Diagnostic written-path fallback retained as later chat context"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-ingest-jobs"
                - "memory.md#mem-obj-chat-sessions"
                - "runtime.md#rt-rte-chat-session"
              note: "Original inputs are recorded tool requests/results projected through clipped job events; classifying them by origin avoids mistaking a JSON event wrapper for environmental event streams."
          records:
            - "runtime.md#rt-obj-ingest-jobs"
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "Original inputs are recorded tool requests/results projected through clipped job events; classifying them by origin avoids mistaking a JSON event wrapper for environmental event streams."
        -
          scope: "Unresolved external-client/custom-content and imported source alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-client-tools"
            - "memory.md#mem-obj-user-templates"
            - "memory.md#mem-rte-source-admission"
          note: "Neither qualifying trace learning nor original trace content is established for these alternatives. Bibliography or ordinary static documents are not automatically session logs or event streams."
        -
          scope: "Ordinary saved chat history without the separately identified derivations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-chat-sessions"
            - "runtime.md#rt-rte-chat-session"
          note: "Raw logs being reloaded is not by itself a qualifying learned artifact. Conversation origin is known, but the prerequisite qualifying trace-fed update is not established for every ordinary history branch."
      records:
        - "memory.md#mem-rte-discussion-guidance"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-obj-ingest-jobs"
        - "memory.md#mem-obj-chat-sessions"
        - "runtime.md#rt-rte-chat-session"
        - "runtime.md#rt-rte-client-tools"
        - "memory.md#mem-obj-user-templates"
        - "memory.md#mem-rte-source-admission"
      note: "Known qualifying routes have named original trace sources. No trajectory, calendar or environmental-event source is established by these records; unresolved alternatives remain included rather than declared inapplicable."
---

# WikiBrain memory profile

## Comparison rationale

This profile classifies the accepted records, not a running service. All positive findings are implementation wiring unless explicitly marked claimed. None is an observation of model compliance, successful retrieval, semantic correctness or improved capacity. The ordinary compilation route admits individual page changes before any mandatory semantic acceptance; the retained wiki therefore supplies knowledge/context without thereby becoming warranted truth. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) and [MEM-OBJ-wiki](memory.md#mem-obj-wiki).

**Canonical identities.** Reconciliation supersedes the epistemic raw and wiki object declarations with [MEM-OBJ-raw](memory.md#mem-obj-raw) and [MEM-OBJ-wiki](memory.md#mem-obj-wiki). This profile uses those canonical objects. Import-fidelity limits remain supported by [EPI-RTE-source-import](epistemic.md#epi-rte-source-import). The structural lint return is not the retained wiki lint report; live schema is not its delivered template base or custom bundle. These distinctions prevent spurious in-memory storage and premature instruction authority for upstream text. See [EPI-OBJ-lint-report](epistemic.md#epi-obj-lint-report), [MEM-OBJ-schema](memory.md#mem-obj-schema), [MEM-OBJ-template-state](memory.md#mem-obj-template-state), and [MEM-OBJ-user-templates](memory.md#mem-obj-user-templates).

**Substrate and form.** Markdown paths, linked pages and exported assets do not make the operative store files, repo or graph: the accepted objects are PostgreSQL rows/JSON/bytea, including the relational link table. Natural-language bodies and code-consumed selectors remain separate forms. Image payloads are not distributed parameters, and their visual representation lacks a supported controlled classification. The unresolved visual unit makes form partial without making PostgreSQL storage uncertain. See [MEM-OBJ-links-tags](memory.md#mem-obj-links-tags) and [MEM-OBJ-assets](memory.md#mem-obj-assets).

**Admission and curation.** A human-started job can admit automatic model writes. Browser selection/editing supplies a narrower manual witness; generic write-token identity does not settle per-content control. The alternate normalized schema path is another automatic admission, not evidence of actual self-modification in a run. See [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools), and [RT-RTE-rule-update](runtime.md#rt-rte-rule-update). Revision, soft withdrawal and snapshot expiry support evolve, invalidate and decay. Requested summaries support only claimed consolidation. The semantic relation of generated content remains unresolved, so a requested synthesis or lint diagnosis is not upgraded to implemented semantic synthesis or demonstrated criticism. See [MEM-RTE-state-withdrawal](memory.md#mem-rte-state-withdrawal), [EPI-RTE-semantic-check](epistemic.md#epi-rte-semantic-check), and [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job).

**Read-back operations.** A requested get_instructions response is pull even though it includes automatically chosen pending hints. By contrast, next-turn history is automatically supplied after the session is selected, and default compilation receives code-selected pending targets without the model first requesting that retained set. The pending selector is coarse availability/backlink gating; the conversation selector actually matches a session identity. Lexical search supplies no inferred-lexical push finding because it answers a request. See [MEM-RTE-note-retrieval](memory.md#mem-rte-note-retrieval), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), and [EPI-RTE-pending-selection](epistemic.md#epi-rte-pending-selection).

**Trace-fed updates.** Raw log retention alone is insufficient. The positive chains are more specific: retained discussion turns feed automatically admitted wiki text with a later read route; tool events feed diagnostic written-path fallback that can be retained as assistant prose and supplied in a later turn. Operator initiation of discussion compilation is not approval of each output page. These wired chains establish local trace-learning yes without asserting improved future capacity. Their original inputs support session-logs and tool-traces respectively; the job event wrapper does not establish environmental event-stream origin. See [MEM-RTE-discussion-guidance](memory.md#mem-rte-discussion-guidance), [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs), [MEM-OBJ-chat-sessions](memory.md#mem-obj-chat-sessions), and [RT-RTE-chat-session](runtime.md#rt-rte-chat-session).

Ordinary history retention without those derived branches and opaque external-content admissions remain unresolved learning units. No accepted evidenced-absence record supports a local no. The derived system union therefore retains yes and the known trace sources but cannot claim complete coverage or any system-wide no. The discussion transcript has learning authority at the automatic wiki-writing consumer, not at ordinary history projection. Copying saved role/content into a later history supplies knowledge/context; it does not establish an update to parameters or a durable behavior-shaping artifact at that projection consumer. The resulting wiki/fallback prose supplies knowledge at later readers. Requested log/reason retention does not guarantee a later reader receives all reasons. See [MEM-OBJ-wiki](memory.md#mem-obj-wiki) and [MEM-RTE-discussion-guidance](memory.md#mem-rte-discussion-guidance).

**Coverage limits and source reads.** Scope concerns the shipped local retained loop, not provider internals or private MCP-client policies. Generic caller provenance, qualifying ordinary-history derivation, visual payload form and actual model transformations prevent stronger assessments where named. Uninspected template-language content does not make its inspected PostgreSQL storage or rule-delivery path unknown, but it prevents classifying every template's semantics or epistemic method. No additional source reads were needed or performed; all warrants remain in the supplied accepted records. This profile declares no records and adds no evidence.
