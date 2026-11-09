---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "MindBase memory comparison: retained project prose, chat records, derived access structures and diagnostic caches across a partially traced operational loop."
run-id: "AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01"
source-identity: "https://github.com/frankchu91/mindbase-llm-wiki"
reviewed-boundary: "c5273d2336c4d686df41c2a1495f14f085707f51"
memory-comparison:
  version: 2
  scope: "Includes retained project README guidance, source/context/research and legacy wiki bodies, chats and excerpt notes, snapshots/overflow, diagnostic/topic/analysis caches, derived graph/search/embedding access state, and their write, maintenance and later-consumer routes. Retains unresolved capture, filing, schema-edit, classification, brief/SRS and compiler/executor alternatives within the partial loop. Excludes shipped static prompts/agent instructions as memory, transient plans/tool-call state and transient semantic-search vectors, external provider weights and host-owned compaction internals; shipped host integration remains included."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Inspected retained project bodies, transcripts, excerpt notes, diagnostics and synthesis JSON"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-chats"
                - "memory.md#mem-obj-chat-excerpts"
                - "runtime.md#rt-rte-lint-findings"
                - "memory.md#mem-rte-synthesis-cache"
              note: "Markdown and JSON are retained in the project filesystem; serialization does not change the substrate."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-chats"
            - "memory.md#mem-obj-chat-excerpts"
            - "runtime.md#rt-rte-lint-findings"
            - "memory.md#mem-rte-synthesis-cache"
          note: "Covers these retained files, including context overflow and snapshots; no repository-backed admission or deployed corpus is established."
        -
          scope: "Graph and keyword access state derived from retained files"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
              note: "The graph cache stores derived rows in SQLite."
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
              note: "Retained link/access rows supply the graph access structure."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
              note: "MiniSearch maintains operative access state."
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
              note: "Reindex persists the search index."
          records:
            - "memory.md#mem-obj-access-metadata"
          note: "These are access structures, not additional prose stores; complete invalidation is unresolved."
        -
          scope: "Persisted dense retrieval vectors"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
              note: "Vectors and metadata reside in embeddings/<slug>.json."
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
              note: "Retained dense vectors supply the cosine retrieval access structure."
          records:
            - "memory.md#mem-obj-embeddings"
          note: "Only the BGE cache is retained here; transient MCP semantic-search vectors are excluded."
        -
          scope: "SQLite contradiction judgments and reasons"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-probe-verdict"
                - "epistemic.md#epi-rte-contradiction-probe"
              note: "Three-way verdicts and reasons are cached in SQLite."
          records:
            - "epistemic.md#epi-obj-probe-verdict"
            - "epistemic.md#epi-obj-probe-reason"
            - "epistemic.md#epi-rte-contradiction-probe"
            - "epistemic.md#epi-rte-probe-consumption"
          note: "The SQL cache is distinct from lint JSON and topic synthesis files; substrate of the separately derived analysis/suggestion cache remains unresolved."
        -
          scope: "Other included capture, classification, brief/SRS, filing, schema-edit and compiler/executor retained state"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "The accepted route records do not enumerate every retained object or access structure; available-but-uninspected mechanisms prevent complete substrate coverage."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-chats"
        - "memory.md#mem-obj-chat-excerpts"
        - "runtime.md#rt-rte-lint-findings"
        - "memory.md#mem-rte-synthesis-cache"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-obj-embeddings"
        - "epistemic.md#epi-obj-probe-verdict"
        - "epistemic.md#epi-obj-probe-reason"
        - "epistemic.md#epi-rte-contradiction-probe"
        - "epistemic.md#epi-rte-probe-consumption"
        - "memory.md#mem-rte-cli-ingest"
        - "epistemic.md#epi-rte-health-maintenance"
      note: "Known filesystem, graph, SQLite, vector and in-memory access witnesses do not exhaust the partial operational loop. Provider model weights and host-owned session machinery are external dependencies, not classified as MindBase retained memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Retained prose bodies and readable report/message fields at human or model consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-chats"
                - "memory.md#mem-obj-chat-excerpts"
                - "epistemic.md#epi-obj-lint-prose"
                - "epistemic.md#epi-obj-synthesis-prose"
                - "epistemic.md#epi-obj-probe-reason"
              note: "Claims, messages, diagnoses and reasons receive meaning through human/model interpretation."
          records:
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-chats"
            - "memory.md#mem-obj-chat-excerpts"
            - "epistemic.md#epi-obj-lint-prose"
            - "epistemic.md#epi-obj-synthesis-prose"
            - "epistemic.md#epi-obj-probe-reason"
          note: "Readable titles and snippets are this form at their display/model consumers; they do not establish delivery of a full underlying body."
        -
          scope: "Retained access, citation, transcript-envelope, diagnostic and verdict control fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
                - "memory.md#mem-obj-embeddings"
                - "memory.md#mem-obj-chats"
                - "epistemic.md#epi-obj-citation-fields"
                - "epistemic.md#epi-obj-lint-controls"
                - "epistemic.md#epi-obj-probe-verdict"
              note: "Paths, hashes, timestamps, citation ranges, role fields, kinds and enums have fixed-rule consumers."
          records:
            - "memory.md#mem-obj-access-metadata"
            - "memory.md#mem-obj-embeddings"
            - "memory.md#mem-obj-chats"
            - "epistemic.md#epi-obj-citation-fields"
            - "epistemic.md#epi-obj-lint-controls"
            - "epistemic.md#epi-obj-probe-verdict"
          note: "Mixed objects are split by operative part rather than labeling whole JSON documents as symbolic."
        -
          scope: "Cached numerical embeddings at cosine-search consumer"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embeddings"
              note: "Dense distributed representations supply similarity computation; cache sidecars remain symbolic."
          records:
            - "memory.md#mem-obj-embeddings"
          note: "This is an encoding classification, not evidence that encoder parameters are updated."
        -
          scope: "Other retained payloads and consumer paths in untraced workers, filing and compiler branches"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "No canonical record resolves all payload forms or their consumption paths."
      records:
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-chats"
        - "memory.md#mem-obj-chat-excerpts"
        - "epistemic.md#epi-obj-lint-prose"
        - "epistemic.md#epi-obj-synthesis-prose"
        - "epistemic.md#epi-obj-probe-reason"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-obj-embeddings"
        - "epistemic.md#epi-obj-citation-fields"
        - "epistemic.md#epi-obj-lint-controls"
        - "epistemic.md#epi-obj-probe-verdict"
        - "memory.md#mem-rte-cli-ingest"
        - "epistemic.md#epi-rte-health-maintenance"
      note: "The inspected corpus has natural-language, symbolic and distributed-parametric parts. External provider internals and transient action envelopes are excluded; unresolved included retained parts prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Known server model-production paths into context, research and saved answers"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-build-context"
                - "runtime.md#rt-rte-research-page"
                - "runtime.md#rt-rte-ask-answer"
                - "memory.md#mem-obj-context"
              note: "Configured models author new retained Markdown through these implemented routes."
          records:
            - "runtime.md#rt-rte-build-context"
            - "runtime.md#rt-rte-research-page"
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-obj-context"
          note: "This classifies the recorded production path, not truth, semantic novelty, initial corpus authorship or original source provenance."
        -
          scope: "Conversation-history-to-retained-answer derivation path"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
              note: "Supplied recorded conversational turns feed generated marked answer text that software persists for later queries."
          records:
            - "runtime.md#rt-rte-ask-answer"
          note: "This is conditional trace-derived lineage, not a claim that every saved answer was produced from history or that all supplied sources have trace provenance."
        -
          scope: "Hosted builder authorship path"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-plugin-build"
              note: "The shipped host sequence requests model-authored replacement content; the sequence itself is afforded, not wired by the MCP writer alone."
          records:
            - "runtime.md#rt-rte-plugin-build"
          note: "The implemented writer is not evidence that the host performed the prescribed synthesis."
        -
          scope: "Incoming contributor content, caller-provided chat records and copied excerpt bodies"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-chats"
                - "memory.md#mem-obj-chat-excerpts"
                - "memory.md#mem-rte-chat-retention"
              note: "Caller-supplied text/JSON crosses into retained project stores; excerpt bodies are copied rather than summarized."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-chats"
            - "memory.md#mem-obj-chat-excerpts"
            - "memory.md#mem-rte-chat-retention"
          note: "Import is known; initial human/model authorship and whether excerpts genuinely originate in recorded sessions remain unresolved."
        -
          scope: "Derived indexes, graph rows and persisted embeddings"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
                - "memory.md#mem-obj-embeddings"
              note: "Code derives access representations from stored bodies, metadata and encoder outputs."
          records:
            - "memory.md#mem-obj-access-metadata"
            - "memory.md#mem-obj-embeddings"
          note: "The derivation route is known, but initial source provenance and exact externally resolved encoder revision are not. No trace-extracted lineage is inferred merely from a cache."
        -
          scope: "Generated diagnostic and topic-report content"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-topic-synthesis"
                - "epistemic.md#epi-rte-contradiction-probe"
                - "runtime.md#rt-rte-lint-findings"
              note: "Models propose topic prose and diagnoses; fixed code can also author failure reasons."
          records:
            - "epistemic.md#epi-rte-topic-synthesis"
            - "epistemic.md#epi-rte-contradiction-probe"
            - "runtime.md#rt-rte-lint-findings"
            - "epistemic.md#epi-obj-probe-reason"
          note: "Known report production does not establish accepted truth or origin of every source claim."
        -
          scope: "Initial README/context content and other untraced writer/producer alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-tree-edit"
            - "memory.md#mem-rte-cli-ingest"
            - "memory.md#mem-obj-context"
          note: "Generic caller identity and incomplete executor/worker inspection do not resolve initial authorship or every derivation path."
      records:
        - "runtime.md#rt-rte-build-context"
        - "runtime.md#rt-rte-research-page"
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-rte-plugin-build"
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-chats"
        - "memory.md#mem-obj-chat-excerpts"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-obj-embeddings"
        - "epistemic.md#epi-rte-topic-synthesis"
        - "epistemic.md#epi-rte-contradiction-probe"
        - "runtime.md#rt-rte-lint-findings"
        - "epistemic.md#epi-obj-probe-reason"
        - "memory.md#mem-rte-tree-edit"
        - "memory.md#mem-rte-cli-ingest"
      note: "Supported authored, imported, compiled and conditional trace-derived paths coexist with unresolved original provenance. Chat labels and logs alone add no trace-extracted finding."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained source/context/page prose delivered to later answer, build and host-session models"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
                - "runtime.md#rt-rte-build-context"
                - "runtime.md#rt-bap-session-context"
                - "memory.md#mem-obj-context"
              note: "Retained prose supplies evidence and background context to later consumers."
          records:
            - "runtime.md#rt-rte-ask-answer"
            - "runtime.md#rt-rte-build-context"
            - "runtime.md#rt-bap-session-context"
            - "memory.md#mem-obj-context"
          note: "Delivery wiring is known; host acceptance, model compliance and causal dependence are not observed."
        -
          scope: "Retained project README guidance at contribution/build models"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-project-rules"
              note: "Loaded README supplies PROJECT RULES guiding later proposals."
          records:
            - "runtime.md#rt-bap-project-rules"
          note: "This is retained, editable project guidance; shipped static agent instructions are excluded from the memory boundary."
        -
          scope: "Retained text, index/graph features and dense vectors at retrieval/suggestion rankers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-access-metadata"
                - "memory.md#mem-obj-embeddings"
                - "epistemic.md#epi-rte-probe-consumption"
              note: "Retained content/features influence lexical, cosine and merged ranks; cached contradiction enums prioritize review suggestions."
          records:
            - "memory.md#mem-obj-access-metadata"
            - "memory.md#mem-obj-embeddings"
            - "epistemic.md#epi-rte-probe-consumption"
          note: "A fixed ranking algorithm does not remove ranking authority from the retained inputs."
        -
          scope: "Context mtime, selected-project state, cache keys/verdicts and stale queues at code selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-build-context"
                - "runtime.md#rt-bap-session-context"
                - "epistemic.md#epi-rte-contradiction-probe"
                - "epistemic.md#epi-rte-synthesis-cache"
              note: "Mtime selects source windows; project identity selects injected scope; cached pair verdicts skip judgment; stale keys choose regeneration work."
          records:
            - "runtime.md#rt-rte-build-context"
            - "runtime.md#rt-bap-session-context"
            - "epistemic.md#epi-rte-contradiction-probe"
            - "epistemic.md#epi-rte-synthesis-cache"
          note: "These are operational selectors, not evidence of truth or successful incorporation."
        -
          scope: "Retained human_touched edit-state metadata at inspected L2 rewrite/update handlers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-health-maintenance"
              note: "Retained edit_state determines whether a proposed rewrite/update is admissible."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-health-maintenance"
              note: "The same persisted control vetoes the inspected rewrite/update when human_touched."
          records:
            - "epistemic.md#epi-rte-health-maintenance"
          note: "The veto is local to inspected handlers; it does not establish a global approval policy."
        -
          scope: "Retained cached topic reports, lint diagnoses and contradiction reasons at display/tool consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-synthesis-cache"
                - "runtime.md#rt-rte-lint-findings"
                - "epistemic.md#epi-rte-probe-consumption"
              note: "Report prose supplies advisory review information; it does not compel repair."
          records:
            - "memory.md#mem-rte-synthesis-cache"
            - "runtime.md#rt-rte-lint-findings"
            - "epistemic.md#epi-rte-probe-consumption"
          note: "Stored reasons are not established as guidance to an automatic knowledge-revision consumer."
        -
          scope: "Conversational history at the automatic marked-answer generation-and-filing consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
              note: "History supplies experience to a model update producing retained answer context for later questions; downstream saved prose separately has knowledge authority."
          records:
            - "runtime.md#rt-rte-ask-answer"
          note: "Learning authority describes this trace-to-durable-context consumer path, not provider-weight updates or demonstrated capacity improvement."
        -
          scope: "Trace inputs at durable learning/update consumers and other untraced retained controls"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-chat-retention"
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
          note: "Raw chat storage and generic source-derived synthesis do not alone establish learning authority; mixed trace provenance and untraced writer/consumer paths remain unresolved."
      records:
        - "runtime.md#rt-rte-ask-answer"
        - "runtime.md#rt-rte-build-context"
        - "runtime.md#rt-bap-session-context"
        - "memory.md#mem-obj-context"
        - "runtime.md#rt-bap-project-rules"
        - "memory.md#mem-obj-access-metadata"
        - "memory.md#mem-obj-embeddings"
        - "epistemic.md#epi-rte-probe-consumption"
        - "epistemic.md#epi-rte-contradiction-probe"
        - "epistemic.md#epi-rte-synthesis-cache"
        - "epistemic.md#epi-rte-health-maintenance"
        - "memory.md#mem-rte-synthesis-cache"
        - "runtime.md#rt-rte-lint-findings"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-rte-cli-ingest"
      note: "Knowledge, instruction, learning, ranking, routing, validation and enforcement have local wired paths. The learning path is conditional history-fed answer filing, distinct from downstream knowledge use. Static schemas/prompts are excluded; other retained controls remain unresolved."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Web contribution checkbox application and interactive CLI batch admission"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-contribute-plan"
                - "memory.md#mem-rte-cli-ingest"
              note: "The shipped UI lets a human select individual actions; interactive CLI confirmation approves the batch."
          records:
            - "runtime.md#rt-rte-contribute-plan"
            - "memory.md#mem-rte-cli-ingest"
          note: "This unit covers explicit human checkpoints, not arbitrary API callers or the CLI --yes alternative."
        -
          scope: "Server build/research, configured answer filing, report refresh, embedding admission, L2 health and CLI --yes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-build-context"
                - "runtime.md#rt-rte-research-page"
                - "runtime.md#rt-rte-ask-answer"
                - "memory.md#mem-rte-synthesis-cache"
                - "memory.md#mem-obj-embeddings"
                - "epistemic.md#epi-rte-health-maintenance"
                - "memory.md#mem-rte-cli-ingest"
              note: "Software/model mechanisms admit retained outputs without a per-content human decision."
          records:
            - "runtime.md#rt-rte-build-context"
            - "runtime.md#rt-rte-research-page"
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-rte-synthesis-cache"
            - "memory.md#mem-obj-embeddings"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-rte-cli-ingest"
          note: "Human initiation or configuration is not approval of each admitted body; output quality is separate."
        -
          scope: "Hosted builder content proposal and MCP replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-plugin-build"
              note: "The prescribed builder sequence admits model content without a required reviewer approval step."
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-plugin-build"
              note: "The MCP replacement handler independently admits supplied nonempty content without a human-approval parameter."
          records:
            - "runtime.md#rt-rte-plugin-build"
          note: "The afforded host sequence and wired tool admission keep distinct bases; external host approval policy is unresolved."
        -
          scope: "Generic caller admission for tree edits, transcript/excerpt saves and MCP supplied contributions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-tree-edit"
            - "memory.md#mem-rte-chat-retention"
            - "memory.md#mem-obj-sources"
          note: "The caller supplies or replaces content, but API/MCP identity alone does not establish a human decision versus automated invocation."
        -
          scope: "Other capture, filing, schema-edit and compiler-executor admissions"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "Incomplete accepted-record coverage prevents classifying every initial and subsequent admission mechanism."
      records:
        - "runtime.md#rt-rte-contribute-plan"
        - "memory.md#mem-rte-cli-ingest"
        - "runtime.md#rt-rte-build-context"
        - "runtime.md#rt-rte-research-page"
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-rte-synthesis-cache"
        - "memory.md#mem-obj-embeddings"
        - "epistemic.md#epi-rte-health-maintenance"
        - "runtime.md#rt-rte-plugin-build"
        - "memory.md#mem-rte-tree-edit"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-obj-sources"
      note: "Manual and automatic admission are both supported. They belong to separate mechanisms; physical filesystem I/O and model authorship do not settle agency for generic callers."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Implemented replacement/append routes over existing context, pages, editable bodies and cached reports"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-build-context"
                - "memory.md#mem-rte-tree-edit"
                - "epistemic.md#epi-rte-health-maintenance"
                - "epistemic.md#epi-rte-synthesis-cache"
              note: "These routes revise existing retained entries or replace their bodies/reports; no semantic improvement is implied."
          records:
            - "runtime.md#rt-rte-build-context"
            - "memory.md#mem-rte-tree-edit"
            - "epistemic.md#epi-rte-health-maintenance"
            - "epistemic.md#epi-rte-synthesis-cache"
          note: "This is revision capability, not evidence that the model preserved truth or that all writes are revisions rather than new entries."
        -
          scope: "Requested source-to-context reduction and synthesis under build guidance"
          assessment: "partial"
          findings:
            -
              value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-context"
                - "runtime.md#rt-rte-build-context"
              note: "The build recipe requests a compact retained context from selected source/research material and prior context."
          records:
            - "memory.md#mem-obj-context"
            - "runtime.md#rt-rte-build-context"
          note: "The request supports intended consolidation, not realized semantic preservation. Generated source/output pairs are absent; reshaping versus entailment or new claims remains unresolved."
        -
          scope: "Meaning-level curation in topic synthesis and remaining L1/L2 executor alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-topic-synthesis"
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
          note: "Model-produced changes are semantically indeterminate; return-only merge/flag statuses do not establish deduplication or invalidation. Full executor and worker behavior is uninspected."
      records:
        - "runtime.md#rt-rte-build-context"
        - "memory.md#mem-rte-tree-edit"
        - "epistemic.md#epi-rte-health-maintenance"
        - "epistemic.md#epi-rte-synthesis-cache"
        - "memory.md#mem-obj-context"
        - "epistemic.md#epi-rte-topic-synthesis"
        - "memory.md#mem-rte-cli-ingest"
      note: "Evolution has an implemented witness; consolidation remains requested behavior. New factual synthesis, deduplication, promotion, decay and history-preserving invalidation are not inferred from command names, index rebuilds, stale flags or direct unlink deletion."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Question/page/project/chat/topic requests and builder source reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
                - "memory.md#mem-rte-mcp-retrieval"
                - "memory.md#mem-rte-chat-retention"
                - "memory.md#mem-rte-synthesis-cache"
                - "memory.md#mem-rte-cli-ingest"
              note: "Requests retrieve retained material or explicitly invoke a query; delivery fulfilling that request is pull."
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-plugin-build"
              note: "The hosted builder is instructed to request project/source material and Read listed bodies."
          records:
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-rte-mcp-retrieval"
            - "memory.md#mem-rte-chat-retention"
            - "memory.md#mem-rte-synthesis-cache"
            - "memory.md#mem-rte-cli-ingest"
            - "runtime.md#rt-rte-plugin-build"
          note: "Automatic candidate selection inside a requested answer does not turn its requested return into a second push."
        -
          scope: "Session hook supplying retained selected-project core on startup, clear or compact"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-session-context"
              note: "The automatic hook supplies README/context/index without a contemporaneous request selecting those files."
          records:
            - "runtime.md#rt-bap-session-context"
          note: "Code constructs additionalContext; external host acceptance and behavioral effect remain unobserved."
        -
          scope: "Other included writer/consumer routes and host-dependent reload alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "Incomplete accepted records for workers and other tools prevent a complete inventory of later delivery operations."
      records:
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-rte-mcp-retrieval"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-rte-synthesis-cache"
        - "memory.md#mem-rte-cli-ingest"
        - "runtime.md#rt-rte-plugin-build"
        - "runtime.md#rt-bap-session-context"
        - "epistemic.md#epi-rte-health-maintenance"
        - "memory.md#mem-obj-sources"
      note: "Both pull and push exist locally. Read availability does not prove model activation; unresolved included alternatives prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Session startup/clear/compact trigger: current-project resolution selects retained core files"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-session-context"
              note: "The selector reads persisted currentProjectId and resolves the project whose files are delivered."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-session-context"
              note: "Within that selected project the fixed whole README/context/index set is supplied without content-level relevance filtering or truncation."
          records:
            - "runtime.md#rt-bap-session-context"
          note: "Identifier matching selects the project; the separate coarse operation selects whole core files. Neither is a query-specific relevance score."
        -
          scope: "Completely assessed requested reads in core ask, MCP recall/project reads, CLI query and topic replay"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-rte-mcp-retrieval"
            - "memory.md#mem-rte-chat-retention"
            - "memory.md#mem-rte-cli-ingest"
            - "memory.md#mem-rte-synthesis-cache"
          note: "These operations fulfill requests rather than independently pushing retained parts; lexical and vector ranking here is not a push signal."
        -
          scope: "Other included potential unsolicited selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "Known requested retrieval cannot make untraced hook/worker/consumer alternatives inapplicable."
      records:
        - "runtime.md#rt-bap-session-context"
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-rte-mcp-retrieval"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-rte-cli-ingest"
        - "memory.md#mem-rte-synthesis-cache"
        - "epistemic.md#epi-rte-health-maintenance"
        - "memory.md#mem-obj-sources"
      note: "The inspected hook supplies identifier-based project targeting and coarse whole-core selection. Lexical, embedding and model selectors on pull routes are not reclassified as push signals."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Source/research-to-context and report-refresh updates with mixed or unknown input origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-build-context"
            - "memory.md#mem-rte-synthesis-cache"
            - "epistemic.md#epi-rte-health-maintenance"
          note: "Automatic durable updates and later consumers exist, but no accepted record establishes a qualifying original trace input rather than static source content. Possible contributed experience cannot establish a positive or bounded negative."
        -
          scope: "History-fed marked-answer auto-save, conditional on supplied conversation history, autoSave and matching output marker"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
              note: "Recorded conversational history feeds answer generation; software retains marked answer text as a research/wiki page, which later question consumers can retrieve."
          records:
            - "runtime.md#rt-rte-ask-answer"
          note: "This conditional route qualifies as automatic trace-fed durable context production. It requires neither novel claims nor measured improvement; no run is observed. Raw transcript/excerpt storage is separately unresolved."
        -
          scope: "Other included capture, classification, brief/SRS, filing and compiler/audit-to-consumer alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "Their trace-fed write and later-consumer chains were not exhaustively inspected; absence of a declared positive is not bounded absence."
        -
          scope: "Caller-saved raw chats and copied excerpt notes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-chat-retention"
            - "memory.md#mem-obj-chats"
            - "memory.md#mem-obj-chat-excerpts"
          note: "Content origin and caller admission are unresolved. Raw transcript retention or automatic titling alone does not establish qualifying automatic derivation."
      records:
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-build-context"
        - "memory.md#mem-rte-synthesis-cache"
        - "epistemic.md#epi-rte-health-maintenance"
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-rte-cli-ingest"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-obj-chats"
        - "memory.md#mem-obj-chat-excerpts"
      note: "A conditional history-fed automatic answer filing route establishes yes at wired basis. Other source-origin and worker/admission alternatives remain unresolved, so the inventory is partial. No evidenced-absence record supports a local or system-wide no; no improvement or successful exercise is inferred."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversational history actually supplied on the history-fed answer auto-save branch"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ask-answer"
              note: "The answer invocation consumes the last ten recorded history messages before software files marked output for later retrieval."
          records:
            - "runtime.md#rt-rte-ask-answer"
          note: "The source classification follows conversational history content, not JSON serialization or a transcript filename. It is conditional on that history being supplied, with no observed run."
        -
          scope: "Other possible contributed-experience and excerpt-derived trace routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-build-context"
            - "runtime.md#rt-rte-ask-answer"
            - "memory.md#mem-rte-chat-retention"
            - "memory.md#mem-obj-chat-excerpts"
          note: "The known answer-history branch does not settle provenance of arbitrary contributor text or caller-provided excerpts, nor their admission control."
        -
          scope: "Other included trace-fed input and consumer alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-cli-ingest"
            - "epistemic.md#epi-rte-health-maintenance"
            - "memory.md#mem-obj-sources"
          note: "Untraced worker/compiler/filing paths leave possible trace origins unresolved; source is not inapplicable because trace learning is not completely assessed absent."
      records:
        - "runtime.md#rt-rte-ask-answer"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-build-context"
        - "memory.md#mem-rte-chat-retention"
        - "memory.md#mem-obj-chat-excerpts"
        - "memory.md#mem-rte-cli-ingest"
        - "epistemic.md#epi-rte-health-maintenance"
      note: "Session logs are a wired source on the conditional history-fed filing route. Unknown origins on other updates and uninspected alternative mechanisms prevent complete trace-source coverage; none is made inapplicable by a local unknown."
---

# MindBase memory profile

## Comparison rationale

This profile classifies the accepted records, not a deployed corpus. All positive implementation findings are conditional capacities: none has an observed or causal basis. The hosted builder sequence remains afforded even though its MCP replacement tool is implemented. The same value may therefore appear with separate bases. See [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build) and [RT-RTE-build-context](runtime.md#rt-rte-build-context).

Reconciliation proposes no supersessions. The content objects, mixed-object parts and overlapping routes retain their declared identities. In particular, [MEM-OBJ-context](memory.md#mem-obj-context) and [EPI-OBJ-wiki-pages](epistemic.md#epi-obj-wiki-pages) have different corpus coverage; [MEM-RTE-synthesis-cache](memory.md#mem-rte-synthesis-cache) spans generation and retention whereas [EPI-RTE-topic-synthesis](epistemic.md#epi-rte-topic-synthesis) isolates generation/admission. Classification uses their local parts rather than treating one as a stronger replacement.

Filesystem JSON is a storage witness, not a representational form. Dense cache vectors are parametric representations and vector access structures, while their paths/hashes are symbolic. Graph rows are graph access state implemented in SQLite. Model weights are external machinery, not accumulated MindBase memory. [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings) and [MEM-OBJ-access-metadata](memory.md#mem-obj-access-metadata) do not establish that every mutation invalidates every cache.

Retained project README guidance is instruction at the proposal model. Retained knowledge is knowledge at the answering model. Text and vectors also have ranking force at retrieval code; retained edit-state metadata supplies validation and an enforced veto at the inspected health handlers. These forces follow actual consumers, not file ownership or a generic knowledge label. See [RT-BAP-project-rules](runtime.md#rt-bap-project-rules), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [MEM-OBJ-embeddings](memory.md#mem-obj-embeddings) and [EPI-RTE-health-maintenance](epistemic.md#epi-rte-health-maintenance).

The trace-learning positive is narrow. [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) wires recorded conversation history into an answer invocation and conditionally retains marked output for later question retrieval. On that history-fed branch, automatic production of durable later context qualifies without new knowledge, a continuation-summary label or measured improvement. History has learning authority at this production consumer; saved output has knowledge authority downstream. This does not turn all source-to-context synthesis into trace learning: [MEM-OBJ-sources](memory.md#mem-obj-sources) leaves contributed-content origin mixed or unknown. Nor does [MEM-RTE-chat-retention](memory.md#mem-rte-chat-retention) establish automatic trace derivation merely by saving caller records. The partial inventory supports a system-union yes, never a complete-value claim or a system-wide no.

Curation is equally route-specific. Direct changes and cached report replacement support evolve. Build guidance supports requested consolidation only; semantic preservation and novel claims are unresolved. Topic generation is not classified as synthesize merely because it is named synthesis, and return-only merge/flag handlers do not establish deduplication or history-preserving invalidation. See [MEM-RTE-tree-edit](memory.md#mem-rte-tree-edit), [EPI-RTE-synthesis-cache](epistemic.md#epi-rte-synthesis-cache), [MEM-OBJ-context](memory.md#mem-obj-context), [EPI-RTE-topic-synthesis](epistemic.md#epi-rte-topic-synthesis) and [EPI-RTE-health-maintenance](epistemic.md#epi-rte-health-maintenance).

Question/search delivery fulfills requests and is pull even when code automatically selects candidates. The session hook instead triggers on startup, clear or compact and supplies selected-project core without a contemporaneous file request. Its project identity match and coarse whole-core delivery are separate selection operations. Lexical and vector ranking on requested retrieval is not a push signal. See [RT-BAP-session-context](runtime.md#rt-bap-session-context), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) and [MEM-RTE-mcp-retrieval](memory.md#mem-rte-mcp-retrieval).

Unresolved units preserve the operational-loop boundary. Missing records for filing, schema edits, classification guidance and other worker/compiler alternatives prevent complete authority, admission, lineage and trace-source inventories. Missing body/output pairs prevent stronger meaning-level curation claims. Layout compatibility, snapshot success and cross-writer invalidation remain local limits, not absence. Context size checks apply only to named branches; the internal wikilink append and direct tree edit prevent inferring a universal cap or snapshot guarantee. See [MEM-RTE-cli-ingest](memory.md#mem-rte-cli-ingest), [EPI-RTE-health-maintenance](epistemic.md#epi-rte-health-maintenance), [MEM-RTE-tree-edit](memory.md#mem-rte-tree-edit) and [RT-RTE-build-context](runtime.md#rt-rte-build-context).

Source-read log: none. This classification used only the supplied accepted members and their contracts; no source read was needed to resolve a record ambiguity.
