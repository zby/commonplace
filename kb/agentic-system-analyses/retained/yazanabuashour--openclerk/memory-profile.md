---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "OpenClerk memory profile of retained vault content, derived access state, explicit retrieval baselines and opaque resumed host sessions."
run-id: "AAS-2026-10-16-openclerk-ec0e00c2bb0a-01"
source-identity: "https://github.com/yazanabuashour/openclerk"
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
memory-comparison:
  version: 2
  scope: "Retained and revised vault Markdown, source assets/notes, SQLite mirrors/chunks/typed and graph projections, freshness/provenance, semantic vector caches, retrieval regression cases, changed installed module configuration at later dispatch, and shipped evaluation host-session continuation. Includes unresolved original-asset consumers, initial admission, untraced maintenance/report alternatives and opaque host checkpoints. Excludes static shipped skills/contracts, transient unadopted planning/report output, ordinary current-call state, external provider model weights/training and private deployment contents."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Canonical vault notes, raw source assets, semantic cache and regression cases"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-source-assets"
                - "memory.md#mem-obj-semantic-cache"
                - "memory.md#mem-obj-retrieval-cases"
              note: "Vault Markdown/assets, cache JSON and case JSONL are retained on the filesystem."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-source-assets"
            - "memory.md#mem-obj-semantic-cache"
            - "memory.md#mem-obj-retrieval-cases"
          note: "These retained objects are files; JSON and numerical encoding do not add a storage substrate."
        -
          scope: "Document mirror, chunks, typed projections, graph relationships and freshness/provenance state"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-record-entities"
                - "memory.md#mem-obj-service-records"
                - "memory.md#mem-obj-decision-records"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-projection-states"
              note: "Later store readers consume retained SQLite tables and indexes."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-projection-states"
          note: "The graph is represented in SQLite; graph structure is not a separate demonstrated graph storage engine."
        -
          scope: "Installed module configuration used by subsequent semantic dispatch"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-module-install"
          note: "Configuration persistence is established, but its physical substrate is not specified in this accepted record."
        -
          scope: "Resumed evaluation host session, including possible checkpoint/summary parts"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "A session ID selects external retained state. Its physical storage is not inspected. Provider weights themselves are outside this accumulated-memory inventory."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-source-assets"
        - "memory.md#mem-obj-semantic-cache"
        - "memory.md#mem-obj-retrieval-cases"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-record-entities"
        - "memory.md#mem-obj-service-records"
        - "memory.md#mem-obj-decision-records"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-projection-states"
        - "runtime.md#rt-rte-module-install"
        - "runtime.md#rt-rte-eval-turn"
      note: "The recorded local objects have file and SQLite witnesses. The resumed host payload is included but its storage is opaque; no complete substrate union is established."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Document and chunk prose, typed fact values, synthesis summaries and replay query text at their interpretive consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-record-entities"
                - "memory.md#mem-obj-service-records"
                - "memory.md#mem-obj-decision-records"
                - "memory.md#mem-obj-retrieval-cases"
                - "memory.md#mem-rte-synthesis-compile"
                - "memory.md#mem-rte-projection-read"
              note: "Bodies, snippets, summaries and query text carry language content."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-obj-retrieval-cases"
            - "memory.md#mem-rte-synthesis-compile"
            - "memory.md#mem-rte-projection-read"
          note: "Natural-language content is separate from fields consumed by fixed rules."
        -
          scope: "Frontmatter, IDs, paths, projection fields, graph edges, provenance, cache identities, regression fields and module configuration at code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-record-entities"
                - "memory.md#mem-obj-service-records"
                - "memory.md#mem-obj-decision-records"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-projection-states"
                - "memory.md#mem-obj-semantic-cache"
                - "memory.md#mem-obj-retrieval-cases"
                - "runtime.md#rt-rte-module-install"
              note: "Code interprets metadata, relationships, cache identities and controls as localized fields."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-projection-states"
            - "memory.md#mem-obj-semantic-cache"
            - "memory.md#mem-obj-retrieval-cases"
            - "runtime.md#rt-rte-module-install"
          note: "Localized fields are consumed by fixed selection, admission and comparison rules."
        -
          scope: "Reused semantic-cache vector payload at similarity computation"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-cache"
                - "runtime.md#rt-rte-semantic-search"
              note: "Retained dense chunk vectors are rehydrated and used for semantic ranking."
          records:
            - "memory.md#mem-obj-semantic-cache"
            - "runtime.md#rt-rte-semantic-search"
          note: "Dense representations are not model weights, but their numerical encoding is distributed-parametric."
        -
          scope: "Source-note extraction/transcript text and URL/hash/provenance fields"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-assets"
                - "epistemic.md#epi-rte-web-import"
              note: "Extraction and supplied transcripts become note text."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-assets"
                - "epistemic.md#epi-rte-web-import"
              note: "URL, hash, capture and provenance fields have fixed-rule uses."
          records:
            - "memory.md#mem-obj-source-assets"
            - "epistemic.md#epi-rte-web-import"
          note: "The readable source-note parts are distinct from original assets."
        -
          scope: "Original PDF bytes and optional video metadata asset payload"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-assets"
          note: "Asset retention is known, but the record does not inspect all payload parts or establish their later consumption. A readable note cannot classify the original PDF."
        -
          scope: "External resumed host-session payload and alternative compaction/checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "The host handle does not disclose the retained content encoding."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-record-entities"
        - "memory.md#mem-obj-service-records"
        - "memory.md#mem-obj-decision-records"
        - "memory.md#mem-obj-retrieval-cases"
        - "memory.md#mem-rte-synthesis-compile"
        - "memory.md#mem-rte-projection-read"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-projection-states"
        - "memory.md#mem-obj-semantic-cache"
        - "runtime.md#rt-rte-module-install"
        - "runtime.md#rt-rte-semantic-search"
        - "memory.md#mem-obj-source-assets"
        - "epistemic.md#epi-rte-web-import"
        - "runtime.md#rt-rte-eval-turn"
      note: "Local consumed text, access metadata and dense vectors are separable. Original PDF payloads and resumed host payloads are not classified from their readable summaries."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-supplied document body/facts at lifecycle and compilation input"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-documents"
                - "runtime.md#rt-rte-document-write"
                - "memory.md#mem-rte-synthesis-compile"
              note: "Caller text supplies document and synthesis claims."
          records:
            - "memory.md#mem-obj-documents"
            - "runtime.md#rt-rte-document-write"
            - "memory.md#mem-rte-synthesis-compile"
          note: "This classifies the supplied-content path, not whether the author was human."
        -
          scope: "Vault-file import, external source extraction and supplied transcript acquisition"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-vault-sync"
                - "memory.md#mem-obj-source-assets"
                - "epistemic.md#epi-rte-web-import"
              note: "Existing Markdown and external assertions enter the retained corpus."
          records:
            - "memory.md#mem-rte-vault-sync"
            - "memory.md#mem-obj-source-assets"
            - "epistemic.md#epi-rte-web-import"
          note: "Import is distinct from the unknown history before acquisition."
        -
          scope: "Document/chunk/typed/graph/projection derivatives and compiler/repair output"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-rte-vault-sync"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-record-entities"
                - "memory.md#mem-obj-service-records"
                - "memory.md#mem-obj-decision-records"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-projection-states"
                - "memory.md#mem-rte-synthesis-compile"
                - "epistemic.md#epi-rte-audit-repair"
              note: "Parsing, projection rebuild, body assembly and source-role copying produce retained derivatives."
          records:
            - "memory.md#mem-rte-vault-sync"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-projection-states"
            - "memory.md#mem-rte-synthesis-compile"
            - "epistemic.md#epi-rte-audit-repair"
          note: "Mechanical derivatives and reduced source summaries are compiled rather than evidence of new experiential claims."
        -
          scope: "Semantic cache vector derivation from selected corpus chunks"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-cache"
                - "runtime.md#rt-rte-semantic-search"
              note: "Provider embedding inference compiles chunk content into cached vectors."
          records:
            - "memory.md#mem-obj-semantic-cache"
            - "runtime.md#rt-rte-semantic-search"
          note: "The embedding path is known; original provider training and exact weight provenance remain outside inspection."
        -
          scope: "Reduced retrieval-execution cases"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-cases"
                - "epistemic.md#epi-rte-eval-capture"
              note: "Automatic capture constructs result-identity and measurement rows from retrieval activity."
          records:
            - "memory.md#mem-obj-retrieval-cases"
            - "epistemic.md#epi-rte-eval-capture"
          note: "These are extracted execution records, not learned ranking policy."
        -
          scope: "Initial imported-vault content and explicit session artifact origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-rte-vault-sync"
            - "runtime.md#rt-rte-session-plan"
            - "workflow.md#wf-rte-artifact-plan"
          note: "Imported content may have several prior origins. Explicit session files may be authored handoffs or logs; no uniform original derivation is established."
        -
          scope: "Module configuration initial content and host-session/checkpoint derivation"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-module-install"
            - "runtime.md#rt-rte-eval-turn"
          note: "Caller identity does not settle configuration provenance, and the resumed host payload and compaction derivation are opaque."
      records:
        - "memory.md#mem-obj-documents"
        - "runtime.md#rt-rte-document-write"
        - "memory.md#mem-rte-synthesis-compile"
        - "memory.md#mem-rte-vault-sync"
        - "memory.md#mem-obj-source-assets"
        - "epistemic.md#epi-rte-web-import"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-record-entities"
        - "memory.md#mem-obj-service-records"
        - "memory.md#mem-obj-decision-records"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-projection-states"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-obj-semantic-cache"
        - "runtime.md#rt-rte-semantic-search"
        - "memory.md#mem-obj-retrieval-cases"
        - "epistemic.md#epi-rte-eval-capture"
        - "runtime.md#rt-rte-session-plan"
        - "workflow.md#wf-rte-artifact-plan"
        - "runtime.md#rt-rte-module-install"
        - "runtime.md#rt-rte-eval-turn"
      note: "Authored, imported, compiled and trace-extracted routes coexist. Initial history and provider derivation are not resolved by these positive witnesses."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retrieved note/chunk prose, typed fact values and synthesis summaries delivered to the external agent"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-projection-read"
                - "runtime.md#rt-rte-context-pack"
                - "epistemic.md#epi-rte-audit-repair"
              note: "Selected retained content supplies evidence and context to the requesting host."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-rte-projection-read"
            - "runtime.md#rt-rte-context-pack"
            - "epistemic.md#epi-rte-audit-repair"
          note: "Knowledge identifies evidence/context supply, not observed compliance or answer improvement."
        -
          scope: "Retained chunk text and cached chunk vectors at lexical/semantic ranking"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-rte-projection-read"
              note: "Chunk text is scored by lexical retrieval."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-cache"
                - "runtime.md#rt-rte-semantic-search"
              note: "Reused retained vectors influence semantic hit priority."
          records:
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-rte-projection-read"
            - "memory.md#mem-obj-semantic-cache"
            - "runtime.md#rt-rte-semantic-search"
          note: "Fixed scoring code can confer ranking force on retained content."
        -
          scope: "Stored document fields, projection source classes and module configuration at route/target selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-states"
                - "epistemic.md#epi-rte-synthesis-freshness"
                - "epistemic.md#epi-rte-audit-repair"
              note: "Retained current/superseded source classes select the Summary used in repair."
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-module-install"
              note: "Persisted module binding/configuration selects later dispatch."
          records:
            - "memory.md#mem-obj-documents"
            - "memory.md#mem-obj-projection-states"
            - "epistemic.md#epi-rte-synthesis-freshness"
            - "epistemic.md#epi-rte-audit-repair"
            - "runtime.md#rt-rte-module-install"
          note: "Source roles select copied input; installed configuration selects later module execution, not model learning."
        -
          scope: "Module enabled state and verified binding at subsequent configured execution"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-module-install"
                - "runtime.md#rt-rte-semantic-search"
              note: "Disabled or invalid installed bindings block configured semantic execution."
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-module-install"
                - "runtime.md#rt-rte-semantic-search"
              note: "Retained binding hashes/configuration provide criteria for admissible configured use."
          records:
            - "runtime.md#rt-rte-module-install"
            - "runtime.md#rt-rte-semantic-search"
          note: "These controls act on the runner module path, not every possible direct executable call."
        -
          scope: "Cache identity metadata at vector reuse admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-cache"
              note: "Schema/provider/model/corpus and chunk hashes determine reuse admissibility."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-cache"
              note: "Cache validation gates rehydration of stored vectors."
          records:
            - "memory.md#mem-obj-semantic-cache"
          note: "Stored identity fields are compared against the current request/corpus; rejected entries cannot supply reused vectors."
        -
          scope: "Captured retrieval query/action/filter and baseline result identities at replay"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-cases"
                - "epistemic.md#epi-rte-eval-replay"
              note: "Captured selectors choose the later retrieval operation and inputs."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-retrieval-cases"
                - "epistemic.md#epi-rte-eval-replay"
              note: "Baseline references are comparison criteria for result agreement, not factual correctness."
          records:
            - "memory.md#mem-obj-retrieval-cases"
            - "epistemic.md#epi-rte-eval-capture"
            - "epistemic.md#epi-rte-eval-replay"
          note: "The trace has operative replay/comparison consumers, but no recorded automatic behavior-shaping update."
        -
          scope: "Freshness reasons and policy evidence at audit/report consumers"
          assessment: "partial"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-states"
                - "memory.md#mem-rte-policy-recall"
                - "epistemic.md#epi-rte-synthesis-freshness"
              note: "Reports expose currentness reasons and policy evidence as advice to the host."
          records:
            - "memory.md#mem-obj-projection-states"
            - "memory.md#mem-rte-policy-recall"
            - "epistemic.md#epi-rte-synthesis-freshness"
          note: "Recorded metadata informs warnings and source-role selection. Full policy interpretation and every composite report conversion remain unresolved."
        -
          scope: "Host-retained session parts at resumed Codex turn"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "Continuation is wired, but consumed payload parts and their distinct effects are not inspected."
      records:
        - "memory.md#mem-obj-documents"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-record-entities"
        - "memory.md#mem-obj-service-records"
        - "memory.md#mem-obj-decision-records"
        - "memory.md#mem-rte-projection-read"
        - "runtime.md#rt-rte-context-pack"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-obj-semantic-cache"
        - "runtime.md#rt-rte-semantic-search"
        - "memory.md#mem-obj-projection-states"
        - "epistemic.md#epi-rte-synthesis-freshness"
        - "runtime.md#rt-rte-module-install"
        - "memory.md#mem-obj-retrieval-cases"
        - "epistemic.md#epi-rte-eval-capture"
        - "epistemic.md#epi-rte-eval-replay"
        - "memory.md#mem-rte-policy-recall"
        - "runtime.md#rt-rte-eval-turn"
      note: "Classifications name actual retained-part consumers. Shipped static skill instructions are excluded; code-authored policy summaries do not establish consumption of all retained policy prose as standing instructions."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Vault parse/import and derived chunk/projection admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-vault-sync"
                - "memory.md#mem-obj-chunks"
                - "memory.md#mem-obj-record-entities"
                - "memory.md#mem-obj-service-records"
                - "memory.md#mem-obj-decision-records"
                - "memory.md#mem-obj-graph"
                - "memory.md#mem-obj-projection-states"
              note: "Code selects parseable files and constructs retained access structures without per-derived-item human approval."
          records:
            - "memory.md#mem-rte-vault-sync"
            - "memory.md#mem-obj-chunks"
            - "memory.md#mem-obj-record-entities"
            - "memory.md#mem-obj-service-records"
            - "memory.md#mem-obj-decision-records"
            - "memory.md#mem-obj-graph"
            - "memory.md#mem-obj-projection-states"
          note: "Initial authorship is separate from software admission into the mirror and derived stores."
        -
          scope: "Source-note rendering, compiler assembly, admitted audit repair, cache rebuild and retrieval-row construction"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-assets"
                - "epistemic.md#epi-rte-web-import"
                - "memory.md#mem-rte-synthesis-compile"
                - "epistemic.md#epi-rte-audit-repair"
                - "memory.md#mem-obj-semantic-cache"
                - "runtime.md#rt-rte-semantic-search"
                - "epistemic.md#epi-rte-eval-capture"
              note: "Software renders, selects or constructs the retained derivative on each recorded path."
          records:
            - "memory.md#mem-obj-source-assets"
            - "epistemic.md#epi-rte-web-import"
            - "memory.md#mem-rte-synthesis-compile"
            - "epistemic.md#epi-rte-audit-repair"
            - "memory.md#mem-obj-semantic-cache"
            - "runtime.md#rt-rte-semantic-search"
            - "epistemic.md#epi-rte-eval-capture"
          note: "An upstream request does not make the downstream software-selected content manual."
        -
          scope: "Caller-supplied original note content, replacement, move and configuration admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-document-write"
            - "memory.md#mem-rte-document-move"
            - "runtime.md#rt-rte-module-install"
          note: "Callers may be human or agent. Doctrine asks for approval but the mode check does not authenticate a human content decision; manual admission cannot be asserted."
        -
          scope: "Separate adoption of session candidate into a durable document"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-session-plan"
            - "workflow.md#wf-rte-artifact-plan"
            - "runtime.md#rt-rte-document-write"
          note: "The planner writes no document and leaves adoption to a subsequent caller; no automatic end-to-end adoption or authenticated human choice is established."
        -
          scope: "Resumed host-session persistence and alternative checkpoint replacements"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "The driver resumes an ID but does not expose internal content-write decisions."
      records:
        - "memory.md#mem-rte-vault-sync"
        - "memory.md#mem-obj-chunks"
        - "memory.md#mem-obj-record-entities"
        - "memory.md#mem-obj-service-records"
        - "memory.md#mem-obj-decision-records"
        - "memory.md#mem-obj-graph"
        - "memory.md#mem-obj-projection-states"
        - "memory.md#mem-obj-source-assets"
        - "epistemic.md#epi-rte-web-import"
        - "memory.md#mem-rte-synthesis-compile"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-obj-semantic-cache"
        - "runtime.md#rt-rte-semantic-search"
        - "epistemic.md#epi-rte-eval-capture"
        - "runtime.md#rt-rte-document-write"
        - "memory.md#mem-rte-document-move"
        - "runtime.md#rt-rte-module-install"
        - "runtime.md#rt-rte-session-plan"
        - "workflow.md#wf-rte-artifact-plan"
        - "runtime.md#rt-rte-eval-turn"
      note: "Software admission is supported on particular transformations; generic caller requests and an approval-mode label do not establish explicit human per-content decisions."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing document body/section replacement and source-sensitive Summary repair"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-document-write"
                - "epistemic.md#epi-rte-audit-repair"
              note: "Replacement revises existing retained document text."
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-audit-repair"
              note: "Repair selects a current retained source Summary and source-role references into a reduced target Summary."
          records:
            - "runtime.md#rt-rte-document-write"
            - "epistemic.md#epi-rte-audit-repair"
          note: "The retained entry changes. Copying a source summary does not establish novel-claim synthesis."
        -
          scope: "Compiler selection of retained source-role facts and narrow current-source Summary"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-synthesis-compile"
                - "epistemic.md#epi-rte-synthesis-build"
              note: "Selected retained source material is reduced into synthesis role facts/body."
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-synthesis-compile"
              note: "The update branch replaces an existing synthesis entry."
          records:
            - "memory.md#mem-rte-synthesis-compile"
            - "epistemic.md#epi-rte-synthesis-build"
          note: "Caller claims are preserved; the recorded automatic source selection/assembly does not establish ampliative synthesis."
        -
          scope: "Synthesis freshness/supersession metadata and module disable"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-states"
                - "epistemic.md#epi-rte-synthesis-freshness"
              note: "Persisted stale/source-role status withdraws the currentness claim while preserving underlying text and provenance."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-module-install"
              note: "Disabling configured module use withdraws future runner reliance on the binding without undoing past effects."
          records:
            - "memory.md#mem-obj-projection-states"
            - "epistemic.md#epi-rte-synthesis-freshness"
            - "runtime.md#rt-rte-module-install"
          note: "Invalidation has bounded force: derived currency/configured use changes, but stale source prose is not universally blocked from retrieval."
        -
          scope: "Structural moves, index/cache rebuilds and regression capture/replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-document-move"
            - "memory.md#mem-rte-vault-sync"
            - "memory.md#mem-obj-semantic-cache"
            - "epistemic.md#epi-rte-eval-capture"
            - "epistemic.md#epi-rte-eval-replay"
          note: "Known maintenance does not alone establish a controlled curation operation. A move called promotion need not raise tier/salience; cache rebuild is not automatically deduplication or consolidation."
        -
          scope: "Cleanup apply, source-refresh/restore details, untraced report transformations and host compaction/checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-document-move"
            - "memory.md#mem-obj-source-assets"
            - "memory.md#mem-rte-projection-read"
            - "runtime.md#rt-rte-eval-turn"
          note: "These included alternatives lack complete transformation evidence, preventing a complete operation inventory."
      records:
        - "runtime.md#rt-rte-document-write"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-rte-synthesis-compile"
        - "epistemic.md#epi-rte-synthesis-build"
        - "memory.md#mem-obj-projection-states"
        - "epistemic.md#epi-rte-synthesis-freshness"
        - "runtime.md#rt-rte-module-install"
        - "memory.md#mem-rte-document-move"
        - "memory.md#mem-rte-vault-sync"
        - "memory.md#mem-obj-semantic-cache"
        - "epistemic.md#epi-rte-eval-capture"
        - "epistemic.md#epi-rte-eval-replay"
        - "memory.md#mem-obj-source-assets"
        - "memory.md#mem-rte-projection-read"
        - "runtime.md#rt-rte-eval-turn"
      note: "Recorded transformations support local evolution, consolidation and invalidation. Route names such as synthesis or promotion do not establish new-claim synthesis or raised salience; cleanup, report transformations and host maintenance remain incompletely inspected."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Context packs, primitive projection/document reads, policy recall and explicit semantic retrieval"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-pack"
                - "memory.md#mem-rte-projection-read"
                - "memory.md#mem-rte-policy-recall"
                - "runtime.md#rt-rte-semantic-search"
              note: "Requested results deliver selected previously retained content."
          records:
            - "runtime.md#rt-rte-context-pack"
            - "memory.md#mem-rte-projection-read"
            - "memory.md#mem-rte-policy-recall"
            - "runtime.md#rt-rte-semantic-search"
          note: "A task/query or explicit action requests retained material; fixed-path or embedding selection inside that chain is not by itself push."
        -
          scope: "Explicit regression replay and audit/compiler evidence reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-eval-replay"
                - "epistemic.md#epi-rte-audit-repair"
                - "memory.md#mem-rte-synthesis-compile"
              note: "Caller-selected operations request the retained inputs used by the consumer."
          records:
            - "epistemic.md#epi-rte-eval-replay"
            - "epistemic.md#epi-rte-audit-repair"
            - "memory.md#mem-rte-synthesis-compile"
          note: "Requested replay/maintenance calls consume retained cases and source state."
        -
          scope: "Original PDF/video metadata assets outside extracted-note reads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-assets"
          note: "Retention is established but no later consumer route for these original payloads is established by the record."
        -
          scope: "External resumed host payload and untraced compound-report/host retention routes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
            - "memory.md#mem-rte-projection-read"
          note: "ID-based resume is wired; which retained parts are delivered by request versus independent host supply is not exposed."
      records:
        - "runtime.md#rt-rte-context-pack"
        - "memory.md#mem-rte-projection-read"
        - "memory.md#mem-rte-policy-recall"
        - "runtime.md#rt-rte-semantic-search"
        - "epistemic.md#epi-rte-eval-replay"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-rte-synthesis-compile"
        - "memory.md#mem-obj-source-assets"
        - "runtime.md#rt-rte-eval-turn"
      note: "All inspected external retrieval deliveries fulfill explicit requests. Internal selection is distinguished from a second unsolicited delivery. Host continuation has opaque selection and delivery internals."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "Inspected explicit context, primitive, policy, semantic and replay request chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-pack"
            - "memory.md#mem-rte-projection-read"
            - "memory.md#mem-rte-policy-recall"
            - "runtime.md#rt-rte-semantic-search"
            - "epistemic.md#epi-rte-eval-replay"
          note: "These named operations fulfill retained-material requests rather than push. Requested IDs and fixed policy paths are not evidence of identifier-based push."
        -
          scope: "Original source assets with no established later delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-assets"
          note: "No push trigger, selector input and selected original payload are recorded."
        -
          scope: "Resumed host-session selection and opaque checkpoint/compaction delivery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "The session ID alone does not establish an identity match selecting delivered retained parts. No controlled push signal can be assigned."
      records:
        - "runtime.md#rt-rte-context-pack"
        - "memory.md#mem-rte-projection-read"
        - "memory.md#mem-rte-policy-recall"
        - "runtime.md#rt-rte-semantic-search"
        - "epistemic.md#epi-rte-eval-replay"
        - "memory.md#mem-obj-source-assets"
        - "runtime.md#rt-rte-eval-turn"
      note: "No positive push selector is established in the inspected request routes. The included opaque host alternative prevents a completely assessed pull-only boundary and therefore prevents axis-level inapplicability."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Explicit session artifact planning followed by separate possible lifecycle adoption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-session-plan"
            - "workflow.md#wf-rte-artifact-plan"
            - "runtime.md#rt-rte-document-write"
          note: "Planning has no durable candidate write. Neither automatic durable adoption nor bounded absence of such adoption is established across subsequent callers."
        -
          scope: "Retrieval execution capture and later regression replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-retrieval-cases"
            - "epistemic.md#epi-rte-eval-capture"
            - "epistemic.md#epi-rte-eval-replay"
          note: "Recorded rows are reduced traces used as selectors/comparison baselines. They do not establish a new durable behavior-shaping update. No absence record warrants a controlled no finding."
        -
          scope: "Corpus-derived caches and synthesis/source maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-cache"
            - "memory.md#mem-rte-synthesis-compile"
            - "epistemic.md#epi-rte-audit-repair"
            - "memory.md#mem-obj-source-assets"
          note: "Automatic derivation exists, but the records do not establish qualifying trace-fed inputs on these paths. Imported transcripts and original notes have unresolved activity/content provenance."
        -
          scope: "Resumed host-session checkpoint, summary or compaction writes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "Later continuation is wired, but automatic summary production, retained payload and later consumption chain are opaque. This included alternative cannot be classified no."
      records:
        - "runtime.md#rt-rte-session-plan"
        - "workflow.md#wf-rte-artifact-plan"
        - "runtime.md#rt-rte-document-write"
        - "memory.md#mem-obj-retrieval-cases"
        - "epistemic.md#epi-rte-eval-capture"
        - "epistemic.md#epi-rte-eval-replay"
        - "memory.md#mem-obj-semantic-cache"
        - "memory.md#mem-rte-synthesis-compile"
        - "epistemic.md#epi-rte-audit-repair"
        - "memory.md#mem-obj-source-assets"
        - "runtime.md#rt-rte-eval-turn"
      note: "No accepted record establishes the complete qualifying automatic trace-to-durable-behavior-shaping-artifact chain. This is not bounded system-wide absence: host checkpoints and separate session adoption remain unresolved."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Session candidate and separately admitted knowledge document"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-session-plan"
            - "workflow.md#wf-rte-artifact-plan"
            - "runtime.md#rt-rte-document-write"
          note: "A handoff, authored note or log can enter planning. No qualifying automatic durable update and original trace source are jointly established."
        -
          scope: "Captured retrieval activity and regression replay"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-eval-capture"
            - "epistemic.md#epi-rte-eval-replay"
            - "memory.md#mem-obj-retrieval-cases"
          note: "Execution measurements are known, but the chain does not establish the required behavior-shaping derived write; tool-traces is not assigned merely because traces are stored."
        -
          scope: "Source/transcript intake and compiler/repair derivatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-assets"
            - "memory.md#mem-rte-synthesis-compile"
            - "epistemic.md#epi-rte-audit-repair"
          note: "A supplied video transcript is not automatically an agent session log or timestamped event stream. Qualifying trace content and update consumer are not established."
        -
          scope: "Original inputs to possible host summary/checkpoint writes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-eval-turn"
          note: "The host payload and transformation are uninspected, so session-logs, tool-traces, event-streams and trajectories cannot be inferred from a session handle."
      records:
        - "runtime.md#rt-rte-session-plan"
        - "workflow.md#wf-rte-artifact-plan"
        - "runtime.md#rt-rte-document-write"
        - "epistemic.md#epi-rte-eval-capture"
        - "epistemic.md#epi-rte-eval-replay"
        - "memory.md#mem-obj-retrieval-cases"
        - "memory.md#mem-obj-source-assets"
        - "memory.md#mem-rte-synthesis-compile"
        - "epistemic.md#epi-rte-audit-repair"
        - "runtime.md#rt-rte-eval-turn"
      note: "Source values require a qualifying trace-learning write. Raw retrieval traces and session-labeled files alone do not establish one; unresolved routes prevent inapplicability."
---

# OpenClerk memory profile

## Comparison rationale

The inventory separates retained payloads from access structures and separates automatic transformations from original content decisions. [MEM-OBJ-documents](memory.md#mem-obj-documents), [MEM-RTE-vault-sync](memory.md#mem-rte-vault-sync) and [RT-RTE-document-write](runtime.md#rt-rte-document-write) establish file/SQLite storage and software derivation, not authenticated human approval. No manual finding follows from a user starting a workflow or from an approval-mode string.

Graph relationships remain symbolic SQLite state; dense cache vectors are parametric representations stored in files. Neither encoding adds a graph/vector storage engine or makes provider weights part of accumulated memory. The cache's compiled lineage does not resolve provider provenance. These distinctions follow [MEM-OBJ-graph](memory.md#mem-obj-graph), [MEM-OBJ-semantic-cache](memory.md#mem-obj-semantic-cache) and [RT-RTE-semantic-search](runtime.md#rt-rte-semantic-search).

Behavioral authority is consumer-relative. Stored chunk text and vectors influence ranking; selected text supplies knowledge to the host. Projection source classes route repair; cache identities validate and gate reuse. Regression cases route replay and supply comparison criteria, not gold answers or an automatically adopted ranker. These are distinct effects supported by [MEM-RTE-projection-read](memory.md#mem-rte-projection-read), [MEM-OBJ-semantic-cache](memory.md#mem-obj-semantic-cache), [EPI-RTE-audit-repair](epistemic.md#epi-rte-audit-repair) and [EPI-RTE-eval-replay](epistemic.md#epi-rte-eval-replay). No learning authority is inferred merely from trace retention.

The reconciliation supersedes the memory repair declaration with [EPI-RTE-audit-repair](epistemic.md#epi-rte-audit-repair). All repair-dependent findings use that canonical record. It supports evolution and reduced-source consolidation, not general contradiction adjudication. [MEM-RTE-synthesis-compile](memory.md#mem-rte-synthesis-compile) remains a valid container alongside its content/write parts; its name does not establish new-claim synthesis. [EPI-RTE-synthesis-freshness](epistemic.md#epi-rte-synthesis-freshness) supports narrow invalidation of derived currency, not universal exclusion of stale prose.

Requested task context and explicit policy recall remain pull even when code selects the contents. A requested path or session handle does not alone prove identifier-based push. [RT-RTE-context-pack](runtime.md#rt-rte-context-pack) and [MEM-RTE-policy-recall](memory.md#mem-rte-policy-recall) establish inspected request chains; [RT-RTE-eval-turn](runtime.md#rt-rte-eval-turn) leaves host payload and selection opaque. Thus the signal axis has no positive finding and cannot be made globally inapplicable.

The planning boundary matters for trace learning. [WF-RTE-artifact-plan](workflow.md#wf-rte-artifact-plan) returns a candidate without retaining it, and [EPI-RTE-eval-capture](epistemic.md#epi-rte-eval-capture) retains a baseline rather than revising durable guidance or parameters. These records do not establish qualifying automatic trace learning. They also supply no canonical bounded-absence record justifying a controlled negative. The resumed host's uninspected checkpoint/summary alternatives prevent a complete negative and prevent trace-source inapplicability. The corresponding axes retain uncertainty rather than manufacturing a positive or a system-wide no.

Coverage is record-bounded, not an exhaustive implementation audit. Original PDF payloads cannot be classified from extracted notes; configuration persistence does not identify a physical substrate; cleanup, compound reports and host compaction retain missing facts beside their units. No observed or causal basis is asserted. Every positive finding above has implementation wiring, not an observed benefit warrant.

Source-read log: none. This profile uses only the supplied accepted records and reconciliation; no source ambiguity required a new source read.
