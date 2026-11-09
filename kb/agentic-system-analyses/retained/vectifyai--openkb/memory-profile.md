---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "OpenKB memory profile: retained wiki, conversational context, access controls and portable instruction artifacts at the frozen source."
run-id: "AAS-2026-11-09-openkb-bd9c4c38a842-01"
source-identity: "https://github.com/vectifyai/openkb"
reviewed-boundary: "ff54396e575ee6feb0113b631a34caa082b441cc"
memory-comparison:
  version: 2
  scope: "Retained and revised wiki bodies, sources/images, routing metadata/catalog, hash registry, explorations, sanitized chat history and display data, mutable local schema/installed skills, generated packages, eval sets, snapshots, diagnostics, graph/deck outputs and their write/maintenance/later-consumer routes. Includes unresolved PageIndex private persistence at its call boundary; excludes provider weights and independent implementations, external-host internals, static shipped fallback instructions and ordinary transient current-call state."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Local retained wiki bodies, source exports/images, catalog, frontmatter, registry, explorations and diagnostics"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-wiki-pages"
                - "memory.md#mem-obj-source-content"
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-hashes"
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-diagnostics"
              note: "Markdown, JSON and image bytes are filesystem artifacts; a link graph and hash mapping do not establish graph or KV storage."
          records:
            - "runtime.md#rt-obj-wiki-pages"
            - "memory.md#mem-obj-source-content"
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-hashes"
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-diagnostics"
          note: "Markdown, JSON and image bytes are filesystem artifacts; a link graph and hash mapping do not establish graph or KV storage."
        -
          scope: "Retained chat history and display arrays"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-session-display"
              note: "The reusable history and display data persist in session JSON."
          records:
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-session-display"
          note: "The reusable history and display data persist in session JSON."
        -
          scope: "Live chat history and graph projection"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-graph"
              note: "Session history is a runtime list; graph construction produces a mapping before HTML persistence."
          records:
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-graph"
          note: "Session history is a runtime list; graph construction produces a mapping before HTML persistence."
        -
          scope: "Generated skills, evaluation sets, checkpoints, graph HTML and decks"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-package"
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-obj-iterations"
                - "memory.md#mem-obj-graph"
                - "runtime.md#rt-rte-deck-produce"
              note: "Output directories and JSON/HTML are retained files, not evidence of a separate database."
          records:
            - "memory.md#mem-obj-skill-package"
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-obj-iterations"
            - "memory.md#mem-obj-graph"
            - "runtime.md#rt-rte-deck-produce"
          note: "Output directories and JSON/HTML are retained files, not evidence of a separate database."
        -
          scope: "Locally editable schema and installed skill instructions"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-agents-md"
                - "runtime.md#rt-bap-skill-instructions"
              note: "Local retained instruction files can be reloaded; static bundled fallback is excluded as accumulated memory."
          records:
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-skill-instructions"
          note: "Local retained instruction files can be reloaded; static bundled fallback is excluded as accumulated memory."
        -
          scope: "PageIndex private local state and optional hosted persistence"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-pageindex-client"
            - "memory.md#mem-obj-source-content"
          note: "The .openkb path and client interface do not determine the operative blobs/database or remote substrate. Provider implementation is outside the pin."
      records:
        - "runtime.md#rt-obj-wiki-pages"
        - "memory.md#mem-obj-source-content"
        - "memory.md#mem-obj-page-frontmatter"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-hashes"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-obj-session-history"
        - "memory.md#mem-obj-session-display"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-skill-package"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-obj-iterations"
        - "runtime.md#rt-rte-deck-produce"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-bap-skill-instructions"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Local substrate coverage is recorded across the artifact inventory; opaque PageIndex persistence prevents complete classification."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Wiki/source/answer prose, descriptions, reports, session text and skill body/references"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-wiki-pages"
                - "memory.md#mem-obj-source-content"
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-diagnostics"
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-session-display"
                - "memory.md#mem-obj-skill-package"
              note: "These parts reach models or humans as interpreted prose."
          records:
            - "runtime.md#rt-obj-wiki-pages"
            - "memory.md#mem-obj-source-content"
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-diagnostics"
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-session-display"
            - "memory.md#mem-obj-skill-package"
          note: "These parts reach models or humans as interpreted prose."
        -
          scope: "Paths, page numbers, source lists, catalog link structure, hash registry and session/tool record structure"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-content"
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-hashes"
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-session-display"
              note: "Localized fields are interpreted under fixed selection, removal, SDK or display rules; their prose payloads are classified separately."
          records:
            - "memory.md#mem-obj-source-content"
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-hashes"
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-session-display"
          note: "Localized fields are interpreted under fixed selection, removal, SDK or display rules; their prose payloads are classified separately."
        -
          scope: "Saved evaluation questions"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
              note: "Question strings are interpreted by evaluator models."
          records:
            - "memory.md#mem-obj-eval-sets"
          note: "Question strings are interpreted by evaluator models."
        -
          scope: "Saved evaluation labels"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-rte-skill-eval"
              note: "Expected trigger membership determines fixed comparisons and which questions receive coverage grading."
          records:
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-rte-skill-eval"
          note: "Expected trigger membership determines fixed comparisons and which questions receive coverage grading."
        -
          scope: "Graph nodes/edges and rendered descriptions"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph"
              note: "Graph structure is symbolic; node descriptions are interpreted prose."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-graph"
              note: "Graph structure is symbolic; node descriptions are interpreted prose."
          records:
            - "memory.md#mem-obj-graph"
          note: "Graph structure is symbolic; node descriptions are interpreted prose."
        -
          scope: "Mutable schema and installed skill guidance"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-agents-md"
                - "runtime.md#rt-bap-schema-instructions"
                - "runtime.md#rt-bap-skill-instructions"
              note: "Instructions are text, not a separate prompt representational form."
          records:
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-schema-instructions"
            - "runtime.md#rt-bap-skill-instructions"
          note: "Instructions are text, not a separate prompt representational form."
        -
          scope: "Skill activation metadata and possible scripts; deck markup/control structure"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-skill-package"
                - "runtime.md#rt-rte-deck-produce"
              note: "Metadata and authored code/HTML are fixed-rule parts, separate from natural-language method or slide text; actual generated scripts are not supplied."
          records:
            - "memory.md#mem-obj-skill-package"
            - "runtime.md#rt-rte-deck-produce"
          note: "Metadata and authored code/HTML are fixed-rule parts, separate from natural-language method or slide text; actual generated scripts are not supplied."
        -
          scope: "Checkpoint copies of skill content"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-iterations"
                - "memory.md#mem-obj-skill-package"
              note: "Copies retain the package's split prose and fixed-rule structure, not hidden reasoning."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-iterations"
                - "memory.md#mem-obj-skill-package"
              note: "Copies retain the package's split prose and fixed-rule structure, not hidden reasoning."
          records:
            - "memory.md#mem-obj-iterations"
            - "memory.md#mem-obj-skill-package"
          note: "Copies retain the package's split prose and fixed-rule structure, not hidden reasoning."
        -
          scope: "Extracted image payloads and opaque PageIndex internal representations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-content"
            - "runtime.md#rt-cmp-pageindex-client"
          note: "Base64 transport and a readable exported tree do not establish a controlled form for visual content or private provider state."
      records:
        - "runtime.md#rt-obj-wiki-pages"
        - "memory.md#mem-obj-source-content"
        - "memory.md#mem-obj-page-frontmatter"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-obj-session-history"
        - "memory.md#mem-obj-session-display"
        - "memory.md#mem-obj-skill-package"
        - "memory.md#mem-obj-hashes"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-rte-skill-eval"
        - "memory.md#mem-obj-graph"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-bap-schema-instructions"
        - "runtime.md#rt-bap-skill-instructions"
        - "runtime.md#rt-rte-deck-produce"
        - "memory.md#mem-obj-iterations"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Mixed artifacts are split by operative part; opaque visual/provider parts prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Converted document prose, page exports and image files"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-content"
                - "runtime.md#rt-rte-document-add"
              note: "External documents enter through conversion/cloud or local extraction; extraction fidelity remains unverified."
          records:
            - "memory.md#mem-obj-source-content"
            - "runtime.md#rt-rte-document-add"
          note: "External documents enter through conversion/cloud or local extraction; extraction fidelity remains unverified."
        -
          scope: "Generated summary, concept/entity bodies, exploration prose and portable skill text"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-wiki-pages"
                - "epistemic.md#epi-obj-summary"
                - "epistemic.md#epi-obj-concept"
                - "epistemic.md#epi-obj-entity"
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-skill-package"
              note: "Model calls author candidate text from source/wiki and current requests; authorship does not establish novel claims or semantic warrant."
          records:
            - "runtime.md#rt-obj-wiki-pages"
            - "epistemic.md#epi-obj-summary"
            - "epistemic.md#epi-obj-concept"
            - "epistemic.md#epi-obj-entity"
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-skill-package"
          note: "Model calls author candidate text from source/wiki and current requests; authorship does not establish novel claims or semantic warrant."
        -
          scope: "Code-managed metadata, catalog edits, hashes, graph projection and checkpoint copies"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-hashes"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-iterations"
              note: "Deterministic construction, hashing, projection and copying establish these derivation paths, not their arbitrary initial provenance."
          records:
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-hashes"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-iterations"
          note: "Deterministic construction, hashing, projection and copying establish these derivation paths, not their arbitrary initial provenance."
        -
          scope: "Sanitized reusable SDK history and filtered display trace"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-session-display"
              note: "Recorded interactions are filtered into reusable and display-specific retained parts."
          records:
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-session-display"
          note: "Recorded interactions are filtered into reusable and display-specific retained parts."
        -
          scope: "Generated evaluation sets"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
                - "epistemic.md#epi-rte-eval-set"
              note: "The generator authors questions and expected labels; imported saved alternatives are separate."
          records:
            - "memory.md#mem-obj-eval-sets"
            - "epistemic.md#epi-rte-eval-set"
          note: "The generator authors questions and expected labels; imported saved alternatives are separate."
        -
          scope: "Loaded externally supplied evaluation sets"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
                - "epistemic.md#epi-rte-eval-set"
              note: "The replay route admits supplied JSON, without establishing who initially authored its labels."
          records:
            - "memory.md#mem-obj-eval-sets"
            - "epistemic.md#epi-rte-eval-set"
          note: "The replay route admits supplied JSON, without establishing who initially authored its labels."
        -
          scope: "Operation-log formatting from operation records"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-diagnostics"
              note: "Log descriptions retain activity; this does not establish a later learning consumer."
          records:
            - "memory.md#mem-obj-diagnostics"
          note: "Log descriptions retain activity; this does not establish a later learning consumer."
        -
          scope: "Initial arbitrary local schema, installed skills and user-edited metadata; provider tree-summary provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-skill-instructions"
            - "memory.md#mem-obj-page-frontmatter"
            - "runtime.md#rt-cmp-pageindex-client"
            - "memory.md#mem-obj-source-content"
          note: "Read functions cannot reconstruct initial authorship or approval, and provider derivation remains opaque. Known downstream rewrites do not resolve these origins."
      records:
        - "memory.md#mem-obj-source-content"
        - "runtime.md#rt-rte-document-add"
        - "runtime.md#rt-obj-wiki-pages"
        - "epistemic.md#epi-obj-summary"
        - "epistemic.md#epi-obj-concept"
        - "epistemic.md#epi-obj-entity"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-skill-package"
        - "memory.md#mem-obj-page-frontmatter"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-hashes"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-iterations"
        - "memory.md#mem-obj-session-history"
        - "memory.md#mem-obj-session-display"
        - "memory.md#mem-obj-eval-sets"
        - "epistemic.md#epi-rte-eval-set"
        - "memory.md#mem-obj-diagnostics"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-bap-skill-instructions"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Known derivation paths coexist with unresolved initial content and provider provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Wiki/source/answer/report text delivered to answering, compiling and generating models or human readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-wiki-pages"
                - "memory.md#mem-obj-source-content"
                - "runtime.md#rt-rte-wiki-query"
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-diagnostics"
                - "memory.md#mem-obj-session-history"
              note: "Content supplies evidence or context, not a semantic truth gate."
          records:
            - "runtime.md#rt-obj-wiki-pages"
            - "memory.md#mem-obj-source-content"
            - "runtime.md#rt-rte-wiki-query"
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-diagnostics"
            - "memory.md#mem-obj-session-history"
          note: "Content supplies evidence or context, not a semantic truth gate."
        -
          scope: "Retained local schema and installed skill body at instruction consumers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-schema-instructions"
                - "runtime.md#rt-bap-skill-instructions"
              note: "Schema is interpolated into instructions; installed bodies guide chat or runner behavior. Generated output gains this effect only after installation."
          records:
            - "runtime.md#rt-bap-schema-instructions"
            - "runtime.md#rt-bap-skill-instructions"
          note: "Schema is interpolated into instructions; installed bodies guide chat or runner behavior. Generated output gains this effect only after installation."
        -
          scope: "Retained briefs and source counts at the page planner"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-index"
                - "runtime.md#rt-rte-document-add"
              note: "Descriptions and recurrence cues influence which concepts/entities receive attention and updates; no learned ranker is implied."
          records:
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-index"
            - "runtime.md#rt-rte-document-add"
          note: "Descriptions and recurrence cues influence which concepts/entities receive attention and updates; no learned ranker is implied."
        -
          scope: "Catalog paths, source pointers/lists and registry entries at selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-hashes"
                - "runtime.md#rt-rte-wiki-maintain"
              note: "These fields select reads, source-associated cleanup, reloads and retries under model or code control."
          records:
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-hashes"
            - "runtime.md#rt-rte-wiki-maintain"
          note: "These fields select reads, source-associated cleanup, reloads and retries under model or code control."
        -
          scope: "Registered content hashes at duplicate admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hashes"
                - "runtime.md#rt-rte-document-add"
              note: "Previously registered hashes define a duplicate criterion and cause the add path to skip work. This is not near-duplicate consolidation."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-hashes"
                - "runtime.md#rt-rte-document-add"
              note: "Previously registered hashes define a duplicate criterion and cause the add path to skip work. This is not near-duplicate consolidation."
          records:
            - "memory.md#mem-obj-hashes"
            - "runtime.md#rt-rte-document-add"
          note: "Previously registered hashes define a duplicate criterion and cause the add path to skip work. This is not near-duplicate consolidation."
        -
          scope: "Saved evaluation labels at trigger comparison and coverage selection"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-rte-skill-eval"
              note: "Labels determine agreement criteria and the coverage-question subset; they do not veto skill installation."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-rte-skill-eval"
              note: "Labels determine agreement criteria and the coverage-question subset; they do not veto skill installation."
          records:
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-rte-skill-eval"
          note: "Labels determine agreement criteria and the coverage-question subset; they do not veto skill installation."
        -
          scope: "Retained interaction history at sanitizer and subsequent model invocation"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "Activity is automatically transformed into durable reusable context for later behavior. This labels the trace-fed update consumer, not demonstrated capacity improvement."
          records:
            - "memory.md#mem-obj-session-history"
            - "runtime.md#rt-rte-session-chat"
          note: "Activity is automatically transformed into durable reusable context for later behavior. This labels the trace-fed update consumer, not demonstrated capacity improvement."
        -
          scope: "Generated package before installation, arbitrary script effects and opaque provider state"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-skill-package"
            - "runtime.md#rt-rte-skill-create"
            - "runtime.md#rt-cmp-pageindex-client"
          note: "Exported method candidates have no automatically established instruction consumer; actual script contents and private state effects are not recorded."
      records:
        - "runtime.md#rt-obj-wiki-pages"
        - "memory.md#mem-obj-source-content"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-obj-session-history"
        - "runtime.md#rt-bap-schema-instructions"
        - "runtime.md#rt-bap-skill-instructions"
        - "memory.md#mem-obj-page-frontmatter"
        - "memory.md#mem-obj-index"
        - "runtime.md#rt-rte-document-add"
        - "memory.md#mem-obj-hashes"
        - "runtime.md#rt-rte-wiki-maintain"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-rte-skill-eval"
        - "runtime.md#rt-rte-session-chat"
        - "memory.md#mem-obj-skill-package"
        - "runtime.md#rt-rte-skill-create"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Classifications follow actual consumers; unconsumed metadata and output candidates acquire no authority merely by retention."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Document conversion/compilation, metadata/hash registration and schema refresh"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-document-add"
                - "memory.md#mem-obj-page-frontmatter"
                - "memory.md#mem-obj-hashes"
                - "runtime.md#rt-obj-agents-md"
              note: "Software admits converted/model-authored content and explicit refresh replacement without per-content approval; operator initiation is not manual page admission."
          records:
            - "runtime.md#rt-rte-document-add"
            - "memory.md#mem-obj-page-frontmatter"
            - "memory.md#mem-obj-hashes"
            - "runtime.md#rt-obj-agents-md"
          note: "Software admits converted/model-authored content and explicit refresh replacement without per-content approval; operator initiation is not manual page admission."
        -
          scope: "Query saves, model chat notes/output and session recording"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-session-history"
                - "memory.md#mem-obj-session-display"
                - "runtime.md#rt-rte-session-chat"
              note: "Code/model writes retain answers and sanitized interactions without per-file human confirmation."
          records:
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-session-history"
            - "memory.md#mem-obj-session-display"
            - "runtime.md#rt-rte-session-chat"
          note: "Code/model writes retain answers and sanitized interactions without per-file human confirmation."
        -
          scope: "Skill/deck generation, evaluation-set saving, graph and diagnostic production"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-create"
                - "runtime.md#rt-rte-deck-produce"
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-diagnostics"
              note: "Software/model admission follows workflow initiation; validation diagnostics are not human approval."
          records:
            - "runtime.md#rt-rte-skill-create"
            - "runtime.md#rt-rte-deck-produce"
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-diagnostics"
          note: "Software/model admission follows workflow initiation; validation diagnostics are not human approval."
        -
          scope: "Workbench human-supplied page replacement"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-page-edit"
              note: "The human-facing editor affords supplying/editing/vetoing retained body content."
          records:
            - "memory.md#mem-rte-page-edit"
          note: "The human-facing editor affords supplying/editing/vetoing retained body content."
        -
          scope: "Operator-selected checkpoint restoration and authorized replacement"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-obj-iterations"
                - "runtime.md#rt-rte-skill-create"
              note: "Explicit rollback/overwrite decisions select retained checkpoints; automatic snapshot I/O is not the control decision."
          records:
            - "memory.md#mem-obj-iterations"
            - "runtime.md#rt-rte-skill-create"
          note: "Explicit rollback/overwrite decisions select retained checkpoints; automatic snapshot I/O is not the control decision."
        -
          scope: "Arbitrary API page caller, initial schema/local skills and private provider writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-page-edit"
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-skill-instructions"
            - "runtime.md#rt-cmp-pageindex-client"
          note: "Generic caller identity and read-time discovery do not establish human admission; opaque provider internals prevent classifying their write control."
      records:
        - "runtime.md#rt-rte-document-add"
        - "memory.md#mem-obj-page-frontmatter"
        - "memory.md#mem-obj-hashes"
        - "runtime.md#rt-obj-agents-md"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-session-history"
        - "memory.md#mem-obj-session-display"
        - "runtime.md#rt-rte-session-chat"
        - "runtime.md#rt-rte-skill-create"
        - "runtime.md#rt-rte-deck-produce"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-rte-page-edit"
        - "memory.md#mem-obj-iterations"
        - "runtime.md#rt-bap-skill-instructions"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Separate human editing/replacement from automatic generation and from unresolved initialization."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Summary and brief production over retained document/wiki content"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-summary"
                - "memory.md#mem-obj-page-frontmatter"
                - "runtime.md#rt-rte-document-add"
              note: "Summarization and compact descriptions reduce existing material; no claim of faithful factual preservation follows."
          records:
            - "epistemic.md#epi-obj-summary"
            - "memory.md#mem-obj-page-frontmatter"
            - "runtime.md#rt-rte-document-add"
          note: "Summarization and compact descriptions reduce existing material; no claim of faithful factual preservation follows."
        -
          scope: "Existing concept/entity full-body update and recompilation"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-concept"
                - "epistemic.md#epi-obj-entity"
                - "runtime.md#rt-obj-wiki-pages"
                - "runtime.md#rt-rte-wiki-maintain"
              note: "Selected prior bodies are rewritten with new material; wired revision is distinct from semantic novelty."
          records:
            - "epistemic.md#epi-obj-concept"
            - "epistemic.md#epi-obj-entity"
            - "runtime.md#rt-obj-wiki-pages"
            - "runtime.md#rt-rte-wiki-maintain"
          note: "Selected prior bodies are rewritten with new material; wired revision is distinct from semantic novelty."
        -
          scope: "Page body edit and checkpoint replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-page-edit"
                - "memory.md#mem-obj-iterations"
              note: "Explicit replacement revises the current retained entry; checkpoints do not establish automatic winner selection."
          records:
            - "memory.md#mem-rte-page-edit"
            - "memory.md#mem-obj-iterations"
          note: "Explicit replacement revises the current retained entry; checkpoints do not establish automatic winner selection."
        -
          scope: "Novel-claim production in concepts, skills or answers"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-concept"
            - "epistemic.md#epi-obj-entity"
            - "memory.md#mem-obj-skill-package"
            - "memory.md#mem-obj-explorations"
          note: "Requests for synthesis and model-authored text do not establish claims absent from inputs, so synthesize is not asserted."
        -
          scope: "Source/page deletion, structural repair, hash skipping and graph projection as controlled curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-source-withdrawal"
            - "runtime.md#rt-rte-wiki-maintain"
            - "memory.md#mem-obj-hashes"
            - "memory.md#mem-obj-graph"
          note: "Deletion does not retain an invalidation history or establish temporal decay; link repair, primary-key skipping and projection alone establish none of the remaining controlled operations. No bounded absence records support an absent unit."
        -
          scope: "Opaque PageIndex maintenance and uninspected checkpoint/critic semantic effects"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-pageindex-client"
            - "memory.md#mem-obj-iterations"
            - "runtime.md#rt-rte-deck-produce"
          note: "These records do not enumerate private transformations or semantic changes in actual artifacts."
      records:
        - "epistemic.md#epi-obj-summary"
        - "memory.md#mem-obj-page-frontmatter"
        - "runtime.md#rt-rte-document-add"
        - "epistemic.md#epi-obj-concept"
        - "epistemic.md#epi-obj-entity"
        - "runtime.md#rt-obj-wiki-pages"
        - "runtime.md#rt-rte-wiki-maintain"
        - "memory.md#mem-rte-page-edit"
        - "memory.md#mem-obj-iterations"
        - "memory.md#mem-obj-skill-package"
        - "memory.md#mem-obj-explorations"
        - "epistemic.md#epi-rte-source-withdrawal"
        - "memory.md#mem-obj-hashes"
        - "memory.md#mem-obj-graph"
        - "runtime.md#rt-cmp-pageindex-client"
        - "runtime.md#rt-rte-deck-produce"
      note: "Supported consolidation and revision remain visible without classifying synthesis, deduplication, promotion, decay or invalidation from operation names alone."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Question-driven wiki/source/page/image retrieval, explicit exploration/report reads and saved-set replay"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-query"
                - "memory.md#mem-obj-source-content"
                - "memory.md#mem-obj-explorations"
                - "memory.md#mem-obj-diagnostics"
                - "memory.md#mem-obj-eval-sets"
                - "memory.md#mem-rte-skill-eval"
              note: "Models/callers request retained paths or sets; returning requested text is not a second push."
          records:
            - "runtime.md#rt-rte-wiki-query"
            - "memory.md#mem-obj-source-content"
            - "memory.md#mem-obj-explorations"
            - "memory.md#mem-obj-diagnostics"
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-rte-skill-eval"
          note: "Models/callers request retained paths or sets; returning requested text is not a second push."
        -
          scope: "Direct external-host wiki navigation"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-host-read"
              note: "Shipped instructions afford requested direct reads/search, not observed host execution."
          records:
            - "memory.md#mem-rte-host-read"
          note: "Shipped instructions afford requested direct reads/search, not observed host execution."
        -
          scope: "Selected-session history composition"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "After the session is selected, code supplies all sanitized history without a separate request for individual retained turns."
          records:
            - "memory.md#mem-obj-session-history"
            - "runtime.md#rt-rte-session-chat"
          note: "After the session is selected, code supplies all sanitized history without a separate request for individual retained turns."
        -
          scope: "Compile planner briefs/counts and selected old-body context"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-frontmatter"
                - "runtime.md#rt-obj-wiki-pages"
                - "runtime.md#rt-rte-document-add"
              note: "Code automatically constructs planning context and loads selected prior bodies for updates."
          records:
            - "memory.md#mem-obj-page-frontmatter"
            - "runtime.md#rt-obj-wiki-pages"
            - "runtime.md#rt-rte-document-add"
          note: "Code automatically constructs planning context and loads selected prior bodies for updates."
        -
          scope: "Retained schema and discovered skill descriptions at construction"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-schema-instructions"
                - "runtime.md#rt-obj-agents-md"
                - "runtime.md#rt-bap-skill-instructions"
              note: "Local schema and available installed descriptions are supplied automatically; static fallback instructions are outside accumulated memory."
          records:
            - "runtime.md#rt-bap-schema-instructions"
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-skill-instructions"
          note: "Local schema and available installed descriptions are supplied automatically; static fallback instructions are outside accumulated memory."
        -
          scope: "Requested installed skill body, selected runner method, checkpoint restoration and critic artifact reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-skill-instructions"
                - "memory.md#mem-obj-iterations"
                - "runtime.md#rt-rte-deck-produce"
              note: "A model or explicit invocation requests the retained body/checkpoint/artifact; the subsequent delivery fulfills that request."
          records:
            - "runtime.md#rt-bap-skill-instructions"
            - "memory.md#mem-obj-iterations"
            - "runtime.md#rt-rte-deck-produce"
          note: "A model or explicit invocation requests the retained body/checkpoint/artifact; the subsequent delivery fulfills that request."
        -
          scope: "PageIndex private read-back alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-pageindex-client"
            - "memory.md#mem-obj-source-content"
          note: "Exports establish local read routes but do not enumerate private dependency persistence consumers."
      records:
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-source-content"
        - "memory.md#mem-obj-explorations"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-rte-skill-eval"
        - "memory.md#mem-rte-host-read"
        - "memory.md#mem-obj-session-history"
        - "runtime.md#rt-rte-session-chat"
        - "memory.md#mem-obj-page-frontmatter"
        - "runtime.md#rt-obj-wiki-pages"
        - "runtime.md#rt-rte-document-add"
        - "runtime.md#rt-bap-schema-instructions"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-bap-skill-instructions"
        - "memory.md#mem-obj-iterations"
        - "runtime.md#rt-rte-deck-produce"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Both requested retrieval and automatic contextual supply are wired; opaque private alternatives prevent complete inventory coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Selected-session historical push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "Trigger: next/resumed turn. Selector input: requested session ID. Selected part: that session's sanitized history, all of it rather than semantic matches."
          records:
            - "memory.md#mem-obj-session-history"
            - "runtime.md#rt-rte-session-chat"
          note: "Trigger: next/resumed turn. Selector input: requested session ID. Selected part: that session's sanitized history, all of it rather than semantic matches."
        -
          scope: "Planner brief enumeration and instruction discovery"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-frontmatter"
                - "runtime.md#rt-rte-document-add"
                - "runtime.md#rt-obj-agents-md"
                - "runtime.md#rt-bap-schema-instructions"
                - "runtime.md#rt-bap-skill-instructions"
              note: "Trigger: compile/agent construction. Selector: available pages/local schema/discovered skill roots. Selected parts: compact briefs/counts, local schema and skill descriptions; availability is not targeted semantic matching."
          records:
            - "memory.md#mem-obj-page-frontmatter"
            - "runtime.md#rt-rte-document-add"
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-bap-schema-instructions"
            - "runtime.md#rt-bap-skill-instructions"
          note: "Trigger: compile/agent construction. Selector: available pages/local schema/discovered skill roots. Selected parts: compact briefs/counts, local schema and skill descriptions; availability is not targeted semantic matching."
        -
          scope: "Update context selected by compiler plan"
          assessment: "known"
          findings:
            -
              value: "inferred-judgment"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-document-add"
                - "runtime.md#rt-obj-wiki-pages"
                - "memory.md#mem-obj-page-frontmatter"
              note: "Trigger: ingestion/recompile. Planner interprets retained briefs with new material and chooses target pages for automatic old-body delivery."
          records:
            - "runtime.md#rt-rte-document-add"
            - "runtime.md#rt-obj-wiki-pages"
            - "memory.md#mem-obj-page-frontmatter"
          note: "Trigger: ingestion/recompile. Planner interprets retained briefs with new material and chooses target pages for automatic old-body delivery."
        -
          scope: "Old-body lookup after plan selection"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-document-add"
                - "runtime.md#rt-obj-wiki-pages"
              note: "Trigger: update action. Planned slug/path matches the retained page whose body enters the update call; distinct from the upstream model judgment."
          records:
            - "runtime.md#rt-rte-document-add"
            - "runtime.md#rt-obj-wiki-pages"
          note: "Trigger: update action. Planned slug/path matches the retained page whose body enters the update call; distinct from the upstream model judgment."
        -
          scope: "Private provider push selectors and opaque alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-cmp-pageindex-client"
          note: "No accepted record classifies selectors within dependency persistence; pull-only local routes cannot make this branch inapplicable."
      records:
        - "memory.md#mem-obj-session-history"
        - "runtime.md#rt-rte-session-chat"
        - "memory.md#mem-obj-page-frontmatter"
        - "runtime.md#rt-rte-document-add"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-bap-schema-instructions"
        - "runtime.md#rt-bap-skill-instructions"
        - "runtime.md#rt-obj-wiki-pages"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Signals apply only to push operations, not identifiers supplied on requested file reads. No embedding selector is established."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "SDK interaction trace to sanitized persisted history to later session model"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "Automatic filtering retains text/tool records and image reload hints; a later turn receives them as context. No semantic summary, weight update or measured improvement is required."
          records:
            - "memory.md#mem-obj-session-history"
            - "runtime.md#rt-rte-session-chat"
          note: "Automatic filtering retains text/tool records and image reload hints; a later turn receives them as context. No semantic summary, weight update or measured improvement is required."
        -
          scope: "Saved query/chat result to exploration to later explicit wiki consumer"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-explorations"
                - "runtime.md#rt-rte-wiki-query"
                - "runtime.md#rt-rte-session-chat"
              note: "Software/model admission retains conversational results as behavior-relevant context for later reads; no automatic catalog discovery or observed reuse is claimed."
          records:
            - "memory.md#mem-obj-explorations"
            - "runtime.md#rt-rte-wiki-query"
            - "runtime.md#rt-rte-session-chat"
          note: "Software/model admission retains conversational results as behavior-relevant context for later reads; no automatic catalog discovery or observed reuse is claimed."
        -
          scope: "Document-derived wiki/skill generation, diagnostic and checkpoint routes, initial local instructions and provider alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-document-add"
            - "memory.md#mem-obj-skill-package"
            - "memory.md#mem-obj-diagnostics"
            - "memory.md#mem-obj-eval-sets"
            - "memory.md#mem-obj-iterations"
            - "runtime.md#rt-obj-agents-md"
            - "runtime.md#rt-cmp-pageindex-client"
          note: "Document ingestion alone is not experience learning; raw logs alone lack a qualifying automatic later update. These records do not provide bounded absence warrants for all alternatives, initial content or private mechanisms, so no local or system-wide no is asserted."
      records:
        - "memory.md#mem-obj-session-history"
        - "runtime.md#rt-rte-session-chat"
        - "memory.md#mem-obj-explorations"
        - "runtime.md#rt-rte-wiki-query"
        - "runtime.md#rt-rte-document-add"
        - "memory.md#mem-obj-skill-package"
        - "memory.md#mem-obj-diagnostics"
        - "memory.md#mem-obj-eval-sets"
        - "memory.md#mem-obj-iterations"
        - "runtime.md#rt-obj-agents-md"
        - "runtime.md#rt-cmp-pageindex-client"
      note: "Two positive trace-fed chains establish yes at wired basis, while incomplete learning inventory forbids a complete or negative conclusion."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Reusable session history trace-fed write"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "Original inputs are conversational turns and recorded tool requests/results in SDK history; display filtering does not define this source."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-history"
                - "runtime.md#rt-rte-session-chat"
              note: "Original inputs are conversational turns and recorded tool requests/results in SDK history; display filtering does not define this source."
          records:
            - "memory.md#mem-obj-session-history"
            - "runtime.md#rt-rte-session-chat"
          note: "Original inputs are conversational turns and recorded tool requests/results in SDK history; display filtering does not define this source."
        -
          scope: "Saved answer and conversational-note route"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-explorations"
                - "runtime.md#rt-rte-wiki-query"
                - "runtime.md#rt-rte-session-chat"
              note: "The retained question/answer or chat note derives from conversational activity; document evidence used in an answer is not itself an event stream."
          records:
            - "memory.md#mem-obj-explorations"
            - "runtime.md#rt-rte-wiki-query"
            - "runtime.md#rt-rte-session-chat"
          note: "The retained question/answer or chat note derives from conversational activity; document evidence used in an answer is not itself an event stream."
        -
          scope: "Additional mixed inputs to arbitrary chat notes and unresolved trace-learning alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-explorations"
            - "runtime.md#rt-rte-session-chat"
            - "memory.md#mem-obj-diagnostics"
            - "runtime.md#rt-cmp-pageindex-client"
            - "memory.md#mem-obj-skill-package"
          note: "Actual note/tool provenance and private update inputs are not fully recorded; no trajectory or event-stream learning route can be inferred from timestamps, watcher events or log retention alone."
      records:
        - "memory.md#mem-obj-session-history"
        - "runtime.md#rt-rte-session-chat"
        - "memory.md#mem-obj-explorations"
        - "runtime.md#rt-rte-wiki-query"
        - "memory.md#mem-obj-diagnostics"
        - "runtime.md#rt-cmp-pageindex-client"
        - "memory.md#mem-obj-skill-package"
      note: "Trace origin follows the qualifying writes, not adapter labels; unresolved learning routes keep their source uncertainty."
---

# OpenKB memory profile

## Comparison rationale

This profile classifies accepted records, not target execution. All implemented findings retain a wired basis; the Workbench human-edit and external-host navigation alternatives retain afforded basis. No supplied execution or causal evidence upgrades those findings. The inventory includes local exported artifacts and unresolved PageIndex persistence, but does not turn provider model weights into accumulated OpenKB memory.

The sole reconciliation supersession replaces the epistemic source-content object with [MEM-OBJ-source-content](memory.md#mem-obj-source-content). All source-artifact findings therefore cite that canonical declaration. Summary, concept and entity records remain valid parts of [RT-OBJ-wiki-pages](runtime.md#rt-obj-wiki-pages); they are not superseded. Source prose and images, metadata, catalog entries, saved answers, session display and reusable SDK history remain distinct operative parts.

Compilation supports consolidation and revision without establishing semantic novelty. Full-body replacement is an implemented evolve operation; requests for cross-document synthesis do not establish a synthesize finding without recorded claim-level evidence. Source removal changes availability and associations but does not establish history-preserving invalidation, temporal decay or complete semantic forgetting. Hash duplicate skips and graph edge uniqueness are not memory dedup transformations. See [EPI-RTE-source-withdrawal](epistemic.md#epi-rte-source-withdrawal), [MEM-OBJ-hashes](memory.md#mem-obj-hashes) and [MEM-OBJ-graph](memory.md#mem-obj-graph).

Authority follows the consumer rather than the file extension. Retained source/body text supplies knowledge; compact descriptions and recurrence cues influence planner priority; source lists, pointers and registry entries route work. Hash entries also enforce duplicate rejection. Saved evaluation labels supply validation references and select coverage questions, not semantic acceptance of an installed skill. Instruction candidates in output/skills are not automatically installed guidance. These distinctions follow [MEM-OBJ-page-frontmatter](memory.md#mem-obj-page-frontmatter), [MEM-OBJ-eval-sets](memory.md#mem-obj-eval-sets) and [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).

Requested file/tool retrieval is pull. Automatic composition of retained history, compact planner context and local instruction catalogs is push. Session IDs and update slugs select actual retained parts; the mere presence of a path on a requested file read does not establish identifier push. No save-to-index guarantee is inferred for explorations. See [RT-RTE-session-chat](runtime.md#rt-rte-session-chat), [RT-RTE-document-add](runtime.md#rt-rte-document-add) and [MEM-OBJ-explorations](memory.md#mem-obj-explorations).

The trace-learning positives concern durable automatic context writes, not demonstrated improved capacity: interaction history is sanitized and later prepended, and conversational answers/notes can be retained for later reads. History retains tool records as well as conversational turns; the browser display trace is not its substitute. Document-to-wiki-to-skill generation alone establishes neither experience learning nor its absence. No evidenced-absence record supports a local no on the remaining inventory. Thus the learning union has supported yes with partial coverage, and trace-source coverage remains partial rather than inapplicable. See [MEM-OBJ-session-history](memory.md#mem-obj-session-history), [MEM-OBJ-session-display](memory.md#mem-obj-session-display) and [MEM-OBJ-explorations](memory.md#mem-obj-explorations).

Missing initial instruction provenance/control, private PageIndex state semantics, actual script contents, semantic novelty and unrecorded alternative trace inputs prevent stronger coverage assessments. They do not erase supported local findings or convert implementation into observed benefit. No additional source reads were made; all warrants are in the supplied accepted records and their annotations.
