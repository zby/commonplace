---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "expo-llm-wiki memory comparison: local SQLite conversation/document knowledge and maintenance with shipped later consumers and opaque remote alternatives."
run-id: "AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01"
source-identity: "https://github.com/equationalapplications/expo-llm-wiki"
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
memory-comparison:
  version: 2
  scope: "Accumulated local events, assertions, embeddings, task and graph parts, access/trust/validity metadata, entity manifests, scheduling/source/checkpoint state, imported summary and change outbox; their extraction, direct/import admission, maintenance, retrieval, graph and later consumer routes; benchmark replay/reopen and conditional ScopeLab context supply. The shipped MCP remote-retention alternative and host-defined outbox effects remain included as opaque units. Excludes static shipped prompt templates, static ontology packages, provider weights/internals with no recorded retained-memory update, ordinary transient job locks/history and benchmark scoring reports not fed into later memory behavior. External service implementations are outside the frozen source, not silently resolved by local findings."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Local retained events; entry text, vectors and metadata; tasks; edges; entity manifests; checkpoints, source indexes and maintenance markers; imported summary; change outbox"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","memory.md#mem-obj-tasks","memory.md#mem-obj-edges","memory.md#mem-obj-entity-manifests","memory.md#mem-obj-checkpoints","memory.md#mem-obj-entity-summary","memory.md#mem-obj-outbox"]
              note: "Each named part is persisted as SQLite rows/fields. Embedding blobs are an encoding, and edges are adjacency data, not separate vector-service or graph substrates."
          records: ["memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","memory.md#mem-obj-tasks","memory.md#mem-obj-edges","memory.md#mem-obj-entity-manifests","memory.md#mem-obj-checkpoints","memory.md#mem-obj-entity-summary","memory.md#mem-obj-outbox"]
          note: "The memory object inventory identifies the local substrate for every listed part; host adapter durability is not established."
        -
          scope: "Benchmark replay memory cache"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-benchmark-answer"]
              note: "The driver closes and reopens a file-backed SQLite database; files are backing for the same substrate, not a second logical memory store."
          records: ["workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-benchmark-answer"]
          note: "Cache reuse and later answer consumption are wired, not observed."
        -
          scope: "Remote SynapseTree retained state and its storage substrate"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
        -
          scope: "Host-defined external state produced by outbox mapping"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-outbox","runtime.md#rt-rte-outbox-sync"]
          note: "The worker supplies a Prisma transaction to a caller-defined mapper; retained external objects and their later consumers are not identified."
      records: ["memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","memory.md#mem-obj-tasks","memory.md#mem-obj-edges","memory.md#mem-obj-entity-manifests","memory.md#mem-obj-checkpoints","memory.md#mem-obj-entity-summary","memory.md#mem-obj-outbox","workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-benchmark-answer","runtime.md#rt-rte-remote-tools","runtime.md#rt-rte-outbox-sync"]
      note: "Local SQLite coverage is established by the object inventory and replay route. Remote retention and caller-defined external effects prevent complete substrate coverage. Provider weights and static package instructions are not retained memory objects in this scope."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Local assertion text, event summaries, task descriptions, imported summary and manifest descriptions at language consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","epistemic.md#epi-obj-task-description","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-graph-context"]
              note: "Titles/bodies/tags, clipped event summaries, task descriptions, summary text and ontology descriptions are interpreted as language; graph presentation delivers titles rather than fact bodies."
          records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","epistemic.md#epi-obj-task-description","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-graph-context"]
          note: "This unit covers the language parts, not their IDs, constraints or numerical arrays. Summary storage/API exposure does not establish model delivery."
        -
          scope: "Local identity, adjacency, validity, access, trust, task status, ontology constraints and scheduling/control parts"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-metadata","epistemic.md#epi-obj-grounding-trust","memory.md#mem-obj-edges","memory.md#mem-obj-tasks","memory.md#mem-obj-entity-manifests","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox"]
              note: "Fixed rules consume IDs, graph adjacency, lifecycle/valid-time fields, access counts, task priority/status, manifest type constraints, checkpoints and outbox operation structure."
          records: ["memory.md#mem-obj-entry-metadata","epistemic.md#epi-obj-grounding-trust","memory.md#mem-obj-edges","memory.md#mem-obj-tasks","memory.md#mem-obj-entity-manifests","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox"]
          note: "Symbolic consumers are distinct from text renderings; outbox JSON payloads can additionally carry the language entry parts already classified above."
        -
          scope: "Retained per-entry embedding arrays used for similarity"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify"]
              note: "Dense numerical representations of text feed similarity selection and gating; these are not model weights or language summaries."
          records: ["memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify"]
          note: "The controlled form includes distributed dense representations, independently of SQLite blob/text serialization."
        -
          scope: "Remote SynapseTree retained state and its operative representations"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
        -
          scope: "Host-defined outbox effect payload and later consumption"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-outbox-sync"]
          note: "The callback's external retained representation and interpretation are unspecified."
      records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","epistemic.md#epi-obj-task-description","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-graph-context","memory.md#mem-obj-entry-metadata","epistemic.md#epi-obj-grounding-trust","memory.md#mem-obj-edges","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox","memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify","runtime.md#rt-rte-remote-tools","runtime.md#rt-rte-outbox-sync"]
      note: "The inspected local memory is mixed language, symbolic and dense numerical material, split by operative part. Remote and host-defined consumed payloads remain unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Conversation-derived assertions and tasks from retained session turns"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-tasks","workflow.md#wf-rte-replay-cache"]
              note: "Librarian transforms retained conversational summaries into separately persisted assertions/tasks. Benchmark replay provides a concrete session-turn input route."
          records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-tasks","workflow.md#wf-rte-replay-cache"]
          note: "This classifies the derivation path, not truth, full transcript fidelity or the origin of every generic event."
        -
          scope: "Document extraction and local embedding derivation"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["runtime.md#rt-rte-document-ingest","memory.md#mem-obj-entry-vectors"]
              note: "Model extraction from document chunks and encoder conversion of title/body/tags are transformations of supplied content, without establishing trace origin for arbitrary documents."
          records: ["runtime.md#rt-rte-document-ingest","memory.md#mem-obj-entry-vectors"]
          note: "Local transformation is known; unknown document origin is retained separately below."
        -
          scope: "Dump admission of assertions, tasks, edges, summary and optional embedding blobs"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records: ["runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-tasks","memory.md#mem-obj-edges"]
              note: "The import route adopts existing dump parts rather than establishing their upstream derivation."
          records: ["runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-tasks","memory.md#mem-obj-edges"]
          note: "Import is known. Summary authorship, upstream review and imported encoder provenance remain unresolved; import does not imply local extraction."
        -
          scope: "Direct fact authoring and explicit replacement supplied by a host caller"
          assessment: "partial"
          findings:
            -
              value: "authored"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-text","runtime.md#rt-rte-direct-admission","memory.md#mem-rte-temporal-history"]
              note: "The entry inventory includes host-authored direct facts and the direct/temporal APIs admit explicit content without extraction."
          records: ["memory.md#mem-obj-entry-text","runtime.md#rt-rte-direct-admission","memory.md#mem-rte-temporal-history"]
          note: "Authored content is an available path; a generic caller may also forward preexisting content, so the origin of all direct inputs is not established."
        -
          scope: "Local access/checkpoint and change-delivery state produced during use"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-metadata","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox","runtime.md#rt-rte-memory-read"]
              note: "Read access updates and write/maintenance progress encode prior activity for later ranking, retention, retry and scheduling."
          records: ["memory.md#mem-obj-entry-metadata","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox","runtime.md#rt-rte-memory-read"]
          note: "This is operational activity-derived state, not an explanation or automatically warranted knowledge."
        -
          scope: "Initial events/documents, effective-manifest inheritance and emergent proposal derivation"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-events","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-document-ingest"]
          note: "Generic event/document inputs do not identify original authors or trace content. Manifest initialization/merge helpers and the semantic derivation of model proposals remain unresolved."
        -
          scope: "Remote SynapseTree retained state and its lineage"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","memory.md#mem-obj-tasks","workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-document-ingest","memory.md#mem-obj-entry-vectors","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","memory.md#mem-obj-edges","runtime.md#rt-rte-direct-admission","memory.md#mem-rte-temporal-history","memory.md#mem-obj-entry-metadata","memory.md#mem-obj-checkpoints","memory.md#mem-obj-outbox","runtime.md#rt-rte-memory-read","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-remote-tools"]
      note: "Known imported and derived paths do not settle initial provenance, imported vector encoder identity, manifest inheritance or remote derivation."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained assertions and event/task content delivered as reference/context to answer and maintenance consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","runtime.md#rt-bap-memory-context","runtime.md#rt-rte-benchmark-answer","memory.md#mem-rte-heal-memory"]
              note: "Selected fact language supplies answer context and existing knowledge to maintenance; task/event renderings supply contextual data. Delivery does not prove reliance or compliance."
          records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","runtime.md#rt-bap-memory-context","runtime.md#rt-rte-benchmark-answer","memory.md#mem-rte-heal-memory"]
          note: "ScopeLab's wiring carries provider/persistence limits; the reopened benchmark supplies a separate wired later consumer."
        -
          scope: "Retained tasks as prospective action requests"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records: ["epistemic.md#epi-obj-task-description","memory.md#mem-obj-tasks"]
              note: "Task descriptions are retained prospective instructions returned for later consumers; this is an afforded guidance surface, not proof that an agent executes tasks."
          records: ["epistemic.md#epi-obj-task-description","memory.md#mem-obj-tasks"]
          note: "Benchmark formatting explicitly excludes tasks. No deployed task-execution loop is inferred."
        -
          scope: "Persisted manifest language at writer and classifier prompts"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records: ["memory.md#mem-obj-entity-manifests","memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill"]
              note: "Retained ontology descriptions and choices guide later writer/classifier behavior."
          records: ["memory.md#mem-obj-entity-manifests","memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill"]
          note: "Advisory language guidance is separate from normalization constraints."
        -
          scope: "Persisted manifest constraints at normalization/admission"
          assessment: "partial"
          findings:
            -
              value: "validation"
              basis: "wired"
              records: ["memory.md#mem-obj-entity-manifests","memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill"]
              note: "Effective manifest supplies permitted type/edge constraints checked before inspected writes."
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill"]
              note: "Inspected normalization and mode checks can refuse a proposed type/edge change."
          records: ["memory.md#mem-obj-entity-manifests","memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill"]
          note: "Known call-site constraints do not establish complete helper enforcement or globally sound ontology."
        -
          scope: "Retained graph adjacency at traversal and manifest mode at maintenance dispatch"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-edges","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill"]
              note: "Adjacency selects reachable retained nodes at graph traversal; persisted ontology mode selects or skips maintenance/application branches."
          records: ["memory.md#mem-obj-edges","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill"]
          note: "This is selection through symbolic retained state, distinct from interpreting graph text as reference information. TS/native parity is not established."
        -
          scope: "Assertion text, dense vectors and access/confidence/recency fields at selectors and formatters"
          assessment: "partial"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","runtime.md#rt-rte-memory-read","epistemic.md#epi-rte-ops-classify"]
              note: "Retained text/vectors determine neighbors and query scores; access/confidence/recency influence formatting order and retention."
          records: ["memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","runtime.md#rt-rte-memory-read","epistemic.md#epi-rte-ops-classify"]
          note: "Native/custom ranker branches remain incompletely characterized; no learned ranking policy is implied."
        -
          scope: "Validity, lifecycle and retained scheduling/idempotence state at code consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-checkpoints","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-memory-withdrawal"]
              note: "Checkpoints/watermarks and cooldown/source state select event windows, retries and eligible maintenance work."
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-metadata","memory.md#mem-rte-temporal-history","epistemic.md#epi-rte-grounding-status","runtime.md#rt-rte-memory-read"]
              note: "Validity/liveness and optional draft filtering exclude rows from applicable reads; this is not universal draft quarantine."
          records: ["memory.md#mem-obj-checkpoints","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-memory-withdrawal","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-temporal-history","epistemic.md#epi-rte-grounding-status","runtime.md#rt-rte-memory-read"]
          note: "These effects are local selectors. Draft status is included by default; source-index cleanup and external erasure are not guaranteed."
        -
          scope: "Retained conversational evidence at automatic extraction update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-benchmark-answer"]
              note: "Retained session turns feed automatic durable assertions/tasks which reach subsequent retrieval/answer or maintenance invocations."
          records: ["memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-benchmark-answer"]
          note: "Learning authority is at the trace-to-memory update consumer. The resulting assertions supply knowledge downstream; neither path demonstrates improved capacity."
        -
          scope: "Read-usage metadata at durable behavior-shaping update/selection chain"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-metadata","runtime.md#rt-rte-memory-read","memory.md#mem-rte-heal-memory"]
              note: "Nonempty-query reads update retained access data, which affects subsequent formatting and survival policies."
          records: ["memory.md#mem-obj-entry-metadata","runtime.md#rt-rte-memory-read","memory.md#mem-rte-heal-memory"]
          note: "This is operational feedback, not explanatory knowledge or evidence of better answers."
        -
          scope: "Imported summary and host-defined outbox effects at later consumers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-entity-summary","memory.md#mem-obj-outbox","runtime.md#rt-rte-outbox-sync"]
          note: "Summary API exposure does not establish a later model consumer; external mapEvent consumption is host-defined."
        -
          scope: "Remote SynapseTree retained state and its behavioral-authority paths"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["memory.md#mem-obj-entry-text","memory.md#mem-obj-events","memory.md#mem-obj-tasks","runtime.md#rt-bap-memory-context","runtime.md#rt-rte-benchmark-answer","memory.md#mem-rte-heal-memory","epistemic.md#epi-obj-task-description","memory.md#mem-obj-entity-manifests","memory.md#mem-bap-manifest-guidance","memory.md#mem-rte-ontology-backfill","memory.md#mem-obj-edges","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entry-vectors","memory.md#mem-obj-entry-metadata","runtime.md#rt-rte-memory-read","epistemic.md#epi-rte-ops-classify","memory.md#mem-obj-checkpoints","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-memory-withdrawal","memory.md#mem-rte-temporal-history","epistemic.md#epi-rte-grounding-status","workflow.md#wf-rte-replay-cache","memory.md#mem-obj-entity-summary","memory.md#mem-obj-outbox","runtime.md#rt-rte-outbox-sync","runtime.md#rt-rte-remote-tools"]
      note: "Authority follows each actual consumer, not object labels. Supported language, ranking, constraint, routing and trace-update effects coexist with unresolved helper/external consumers."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model extraction, document admission, heal, ontology/classifier application, embedding and automatic usage/control updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","epistemic.md#epi-rte-ops-disposition","runtime.md#rt-rte-document-ingest","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","memory.md#mem-obj-entry-vectors","runtime.md#rt-rte-memory-read","memory.md#mem-obj-checkpoints","workflow.md#wf-rte-report-delivery"]
              note: "Software/model admission does not require per-content human approval. Starting maintenance or spending authorization does not make resulting writes manual."
          records: ["runtime.md#rt-rte-event-librarian","epistemic.md#epi-rte-ops-disposition","runtime.md#rt-rte-document-ingest","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","memory.md#mem-obj-entry-vectors","runtime.md#rt-rte-memory-read","memory.md#mem-obj-checkpoints","workflow.md#wf-rte-report-delivery"]
          note: "This unit names the inspected subsequent admission mechanisms; it does not assign the initial caller's identity."
        -
          scope: "ScopeLab user-message content supplied explicitly by a user"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
              note: "The user supplies the message which the shipped caller writes as a memory event; the operator decision concerns that content, not extracted successor facts."
          records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
          note: "The write path is wired conditionally on wrapper/provider lifecycle limits. Derived facts are admitted automatically and are not covered by this manual finding."
        -
          scope: "ScopeLab assistant/tool-result event renderings"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
              note: "Caller code retains abbreviated assistant output or tool call/result content without per-rendering human approval."
          records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
          note: "This is separate from the user-supplied message route and does not establish successful end-to-end persistence."
        -
          scope: "Generic event, remember/graph, import, manifest/trust/reviewer and temporal/forget caller decisions; UI alternatives"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-events","runtime.md#rt-rte-direct-admission","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-temporal-history","memory.md#mem-rte-memory-withdrawal"]
          note: "API callers decide supplied/replacement content, but human versus software control is unresolved. A nonempty reviewer string does not prove human approval; remaining UI policy was not exhaustively inspected."
        -
          scope: "Remote SynapseTree retained state and its write/admission control"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["runtime.md#rt-rte-event-librarian","epistemic.md#epi-rte-ops-disposition","runtime.md#rt-rte-document-ingest","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","memory.md#mem-obj-entry-vectors","runtime.md#rt-rte-memory-read","memory.md#mem-obj-checkpoints","workflow.md#wf-rte-report-delivery","runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events","runtime.md#rt-rte-direct-admission","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-temporal-history","memory.md#mem-rte-memory-withdrawal","runtime.md#rt-rte-remote-tools"]
      note: "Automatic admission and explicit human-supplied messages are local witnesses. Generic caller APIs, initialization, UI alternatives and remote control prevent a complete manual/automatic assignment."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Retained conversational-event extraction into standing assertions/tasks"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","workflow.md#wf-rte-replay-cache"]
              note: "The librarian selects and reduces retained conversational summaries into reusable facts/tasks. Raw events may remain; semantic fidelity is not established."
          records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","workflow.md#wf-rte-replay-cache"]
          note: "Consolidation names the implemented extraction task, not a claim that every output is entailed."
        -
          scope: "Legacy inferred-title suppression and ops duplicate/noop handling"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","epistemic.md#epi-rte-ops-classify","epistemic.md#epi-rte-ops-disposition"]
              note: "Duplicate title/equivalence/neighbor decisions suppress redundant admission; NOOP preserves existing content."
          records: ["runtime.md#rt-rte-event-librarian","epistemic.md#epi-rte-ops-classify","epistemic.md#epi-rte-ops-disposition"]
          note: "Primary-key checks and index rebuilds alone are excluded from this classification."
        -
          scope: "Ops updates and caller temporal replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["epistemic.md#epi-rte-ops-disposition","memory.md#mem-rte-temporal-history"]
              note: "Inferred rows can have title/body revised; temporal replacement supplies a successor entry."
            -
              value: "invalidate"
              basis: "wired"
              records: ["memory.md#mem-rte-temporal-history"]
              note: "Successful supersession closes the old valid-time interval while retaining history for explicit historical access."
          records: ["epistemic.md#epi-rte-ops-disposition","memory.md#mem-rte-temporal-history"]
          note: "A failed supersession linkage can leave the new candidate admitted; it is not classified as successful withdrawal of the old row."
        -
          scope: "Heal and local retention/withdrawal policy"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records: ["memory.md#mem-rte-heal-memory","memory.md#mem-rte-memory-withdrawal"]
              note: "Age/access-driven downgrading, forgetting and pruning reduce confidence or remove retained entries/events."
            -
              value: "invalidate"
              basis: "wired"
              records: ["epistemic.md#epi-rte-heal-dispose","memory.md#mem-rte-memory-withdrawal"]
              note: "Soft deletion withdraws normal live reliance while retaining a row until pruning."
            -
              value: "dedup"
              basis: "wired"
              records: ["epistemic.md#epi-rte-heal-dispose"]
              note: "Heal's inferred-title check avoids duplicate new-fact insertion."
          records: ["memory.md#mem-rte-heal-memory","memory.md#mem-rte-memory-withdrawal","epistemic.md#epi-rte-heal-dispose"]
          note: "Physical erasure is not guaranteed across events, external indexes or backups; downweighting and withdrawal are distinct operations."
        -
          scope: "Explicit draft promotion"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records: ["runtime.md#rt-rte-direct-admission","epistemic.md#epi-obj-grounding-trust"]
              note: "The live-draft promotion API raises lifecycle status to stable after checking a nonempty reviewer string."
          records: ["runtime.md#rt-rte-direct-admission","epistemic.md#epi-obj-grounding-trust"]
          note: "This is a lifecycle-tier increase, not authenticated human review, epistemic warrant or a guarantee of changed default retrieval."
        -
          scope: "Semantic contribution of heal newFacts, resolver rewriting and emergent ontology proposals"
          assessment: "not-determinable"
          findings: []
          records: ["epistemic.md#epi-rte-heal-dispose","epistemic.md#epi-rte-ops-disposition","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill"]
          note: "Interfaces admit generated/revised content but do not establish a claim absent from the inputs. A name such as newFacts or synthesize does not support the controlled synthesize value."
        -
          scope: "Remote SynapseTree retained state and its curation transformations"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","workflow.md#wf-rte-replay-cache","epistemic.md#epi-rte-ops-classify","epistemic.md#epi-rte-ops-disposition","memory.md#mem-rte-temporal-history","memory.md#mem-rte-heal-memory","memory.md#mem-rte-memory-withdrawal","epistemic.md#epi-rte-heal-dispose","runtime.md#rt-rte-direct-admission","epistemic.md#epi-obj-grounding-trust","memory.md#mem-obj-entity-manifests","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-remote-tools"]
      note: "Supported reduction, deduplication, revision, withdrawal, decay and lifecycle promotion remain distinct. Novel-claim synthesis, opaque remote transformations and uninspected helper semantics are unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested local read, history, graph traversal/presentation, full bundle/summary and outbox retrieval operations"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-memory-read","memory.md#mem-rte-temporal-history","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-import-admission","runtime.md#rt-rte-outbox-sync"]
              note: "Hosts request retained material and receive selected bundles, histories, graph DTO/text, exported parts or pending rows. Ranking within a requested return does not make that return push."
          records: ["runtime.md#rt-rte-memory-read","memory.md#mem-rte-temporal-history","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-import-admission","runtime.md#rt-rte-outbox-sync"]
          note: "Graph/model delivery is afforded rather than universally deployed. Summary exposure is an API route, not established model consumption."
        -
          scope: "ScopeLab automatic memory-context supply before a conversational model call"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","runtime.md#rt-bap-memory-context"]
              note: "On a user message, caller code requests query context and inserts selected fact text into Gemini's first request without a memory request by Gemini."
          records: ["runtime.md#rt-rte-scopelab-chat","runtime.md#rt-bap-memory-context"]
          note: "The upstream library read is pull. This downstream context-supply operation is push; provider/storage mismatch prevents claiming successful operation."
        -
          scope: "Automatic selection and supply of retained context in librarian/heal/backfill model calls"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill"]
              note: "Scheduling or a host maintenance call triggers code selection of recent events/facts, neighbors, anchors or untyped entries and supplies them to a provider that did not request those retained parts."
          records: ["runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill"]
          note: "Manual initiation does not make provider-side selection a requested return. These are service model requests, not separate conversational subagents."
        -
          scope: "Benchmark requested memory-to-answer chain"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-benchmark-answer","workflow.md#wf-rte-replay-cache"]
              note: "Driver explicitly requests retained facts for a question and formats the returned bundle as answer input."
          records: ["runtime.md#rt-rte-benchmark-answer","workflow.md#wf-rte-replay-cache"]
          note: "Requested fulfillment is not counted a second push merely because the driver formats and delivers it."
        -
          scope: "Remote SynapseTree retained state and its read-back operations"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
        -
          scope: "Later consumption of host-defined outbox effects and imported entity summary"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-outbox-sync","memory.md#mem-obj-entity-summary"]
          note: "Known local API return paths do not establish the direction of external downstream consumers."
      records: ["runtime.md#rt-rte-memory-read","memory.md#mem-rte-temporal-history","memory.md#mem-rte-graph-context","runtime.md#rt-rte-native-traversal","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-import-admission","runtime.md#rt-rte-outbox-sync","runtime.md#rt-rte-scopelab-chat","runtime.md#rt-bap-memory-context","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-benchmark-answer","workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-remote-tools"]
      note: "Both requested returns and independent model-context supply are wired within named operations. Unknown external consumers prevent complete directional coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Recent-window context pushed to legacy writer and heal; eligible backfill candidate batches"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records: ["runtime.md#rt-rte-event-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-ops-librarian"]
              note: "Automatic triggers select bounded recent events/facts or oldest eligible untyped/heal candidates using entity, windows, cooldown and budget filters, then supply retained parts to maintenance providers."
          records: ["runtime.md#rt-rte-event-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-ops-librarian"]
          note: "Counts, recency, availability and prompt-degradation levels are coarse selection; they do not demonstrate query-targeted identity matching."
        -
          scope: "Heal immutable-document anchors pushed with candidate facts"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records: ["memory.md#mem-rte-heal-memory"]
              note: "On heal, concatenated candidate titles drive keyword anchor retrieval; filtered/capped retained document anchors enter the provider context."
          records: ["memory.md#mem-rte-heal-memory"]
          note: "Title-keyword overlap can miss contradictory documents without shared vocabulary."
        -
          scope: "Ops neighbor material supplied to ambiguous-candidate resolver"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records: ["memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify","runtime.md#rt-rte-ops-librarian"]
              note: "Candidate text vectors select retained neighboring assertions for similarity gating and ambiguous resolution."
            -
              value: "inferred-lexical"
              basis: "wired"
              records: ["epistemic.md#epi-rte-ops-classify","runtime.md#rt-rte-ops-librarian"]
              note: "Keyword-neighbor fallback selects retained assertions for ambiguous resolution."
          records: ["memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify","runtime.md#rt-rte-ops-librarian"]
          note: "Known selector branches are alternatives. Resolver target aliases constrain mutations, not a separate identifier-based context injection."
        -
          scope: "ScopeLab query-targeted automatic context supply"
          assessment: "partial"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","runtime.md#rt-rte-memory-read"]
              note: "Keyword fallback can select query-related retained facts supplied through the same wrapper."
          records: ["runtime.md#rt-rte-scopelab-chat","runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-vectors"]
          note: "The query-context wrapper and keyword fallback are recorded. Caller-specific embedding-enabled selection is not established: shared retrieval alternatives and retained vectors do not supply the missing ScopeLab provider configuration. No inferred-embedding finding is emitted for this unit. Custom/native ranker detail and wrapper provider/persistence mismatches also prevent complete or observed selector coverage."
        -
          scope: "Remote SynapseTree retained state and its push selectors"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
        -
          scope: "Requested graph/history/summary and benchmark returns"
          assessment: "inapplicable"
          findings: []
          records: ["memory.md#mem-rte-graph-context","memory.md#mem-rte-temporal-history","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-benchmark-answer"]
          note: "These operations fulfil requests and have no independent push selector in their classified operation; IDs on requested objects alone are not push signals."
      records: ["runtime.md#rt-rte-event-librarian","memory.md#mem-rte-heal-memory","memory.md#mem-rte-ontology-backfill","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-entry-vectors","epistemic.md#epi-rte-ops-classify","runtime.md#rt-rte-scopelab-chat","runtime.md#rt-rte-memory-read","runtime.md#rt-rte-remote-tools","memory.md#mem-rte-graph-context","memory.md#mem-rte-temporal-history","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-benchmark-answer"]
      note: "Signals classify actual automatic context selection, not all retrieval parameters. Known push witnesses prevent a pull-only inapplicability claim; opaque/custom selectors remain unresolved."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Benchmark conversation replay through automatic librarian extraction to retained facts and later answer input"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","runtime.md#rt-rte-benchmark-answer"]
              note: "Role-prefixed recorded session turns become retained events, automatic extraction writes durable facts/tasks, and a reopened database supplies facts to the answer model."
          records: ["workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","runtime.md#rt-rte-benchmark-answer"]
          note: "A wired trace-fed behavior-shaping artifact chain is sufficient; successful execution, correct extraction and improved capacity are not established."
        -
          scope: "ScopeLab mixed user/assistant/tool feedback through event extraction and future reads"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-bap-memory-context"]
              note: "The caller writes conversation/tool renderings for future extraction/retrieval; core admission and later-consumer construction are wired."
          records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-bap-memory-context"]
          note: "The wrapper's missing provider/persistence mismatch prevents claiming an exercised or fully operational application loop; core and benchmark paths remain independent."
        -
          scope: "Retained read-access feedback shaping later order and survival"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory"]
              note: "Query activity automatically updates durable access counters/times; later format ordering and retention policies consume that state."
          records: ["runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory"]
          note: "This is trace-fed durable behavioral shaping, not parameter learning, new explanatory content or demonstrated improvement."
        -
          scope: "Generic document/event imports, entity summary, emergent initialization and host-defined outbox effects"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-document-ingest","memory.md#mem-obj-events","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entity-manifests","runtime.md#rt-rte-outbox-sync"]
          note: "Original content, admission provenance or later behavior-shaping consumers are unresolved for these alternatives. No evidenced-absence record licenses local no."
        -
          scope: "Remote SynapseTree retained state and its automatic trace-fed write and later-consumer chains"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["workflow.md#wf-rte-replay-cache","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-ops-librarian","memory.md#mem-obj-events","memory.md#mem-obj-entry-text","runtime.md#rt-rte-benchmark-answer","runtime.md#rt-rte-scopelab-chat","runtime.md#rt-bap-memory-context","runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory","runtime.md#rt-rte-document-ingest","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","memory.md#mem-obj-entity-manifests","runtime.md#rt-rte-outbox-sync","runtime.md#rt-rte-remote-tools"]
      note: "Qualifying wired yes witnesses coexist with unresolved alternatives. No system-wide no or complete learning inventory is supported, and this axis does not measure improved capacity."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Benchmark replay qualifying extraction chain"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records: ["workflow.md#wf-rte-replay-cache","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-benchmark-answer"]
              note: "Original input is recorded conversational turns replayed as role-prefixed observation summaries; the event wrapper adds no event-stream source."
          records: ["workflow.md#wf-rte-replay-cache","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-benchmark-answer"]
          note: "Dates and observation labels do not turn session logs into environmental event streams or trajectories."
        -
          scope: "ScopeLab qualifying mixed feedback chain"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
              note: "User messages and abbreviated assistant responses are recorded conversational content."
            -
              value: "tool-traces"
              basis: "wired"
              records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events"]
              note: "Recorded function-call arguments and truncated tool results are explicit tool activity inputs to the future extraction route."
          records: ["runtime.md#rt-rte-scopelab-chat","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian"]
          note: "The content origins are known in this caller even though actual persistence/extraction has implementation limits. Truncation limits source completeness."
        -
          scope: "Read-access feedback qualifying update"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records: ["runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory"]
              note: "Original activity is discrete nonempty-query access to returned fact IDs; recorded counters/times shape later retention and formatting."
          records: ["runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory"]
          note: "This is runtime-use feedback, not imported conversational events relabelled as environmental events."
        -
          scope: "Generic core event/document input, imported summary and external qualifying alternatives"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-events","runtime.md#rt-rte-document-ingest","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-outbox-sync"]
          note: "Generic APIs do not establish original content or even a qualifying trace-fed write for every alternative. Summary naming, imported blobs and outbox serialization cannot determine trace source."
        -
          scope: "Remote SynapseTree retained state and its original trace inputs"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-remote-tools"]
          note: "The shipped transport is inspected, but remote retained parts and mechanisms are opaque. Local-core classifications do not resolve this alternative."
      records: ["workflow.md#wf-rte-replay-cache","memory.md#mem-obj-events","runtime.md#rt-rte-event-librarian","runtime.md#rt-rte-benchmark-answer","runtime.md#rt-rte-scopelab-chat","runtime.md#rt-rte-memory-read","memory.md#mem-obj-entry-metadata","memory.md#mem-rte-heal-memory","runtime.md#rt-rte-document-ingest","runtime.md#rt-rte-import-admission","memory.md#mem-obj-entity-summary","runtime.md#rt-rte-outbox-sync","runtime.md#rt-rte-remote-tools"]
      note: "Session and tool content support concrete local routes; access feedback has runtime-event origin. No linked state/action/outcome trajectory source is established, but absence is not asserted."
---

# expo-llm-wiki memory profile

## Comparison rationale

### Boundary and evidence strength

The profile classifies retained memory and its consumers, not every store used by the runtime. SQLite holds both text and numerical arrays; adjacency and vectors do not independently establish graph-service or vector-service substrates. The local object inventory distinguishes language from symbolic controls and dense numerical representation. Imported summary exposure is not a demonstrated continuation-summary route. See [MEM-OBJ-entry-vectors](memory.md#mem-obj-entry-vectors), [MEM-OBJ-edges](memory.md#mem-obj-edges) and [MEM-OBJ-entity-summary](memory.md#mem-obj-entity-summary).

Every positive basis is wired except the explicitly afforded prospective task-instruction consumer. No observed-run or causal basis is inferred. ScopeLab supplies inspected request construction and mixed feedback content, but its missing-provider and persistence-property mismatches remain limits on operation. The replay/reopen benchmark is an independent wired trace-to-later-consumer witness, not evidence of successful execution or improvement. See [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat) and [WF-RTE-replay-cache](workflow.md#wf-rte-replay-cache).

Each axis remains partial because the shipped remote integration does not reveal retained payloads or remote admission/selection mechanisms. Host-defined outbox effects and unresolved local initialization or helper branches are kept where they prevent stronger classification. These are not negative findings. Neither external provider model internals nor static configuration is substituted for accumulated memory. See [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools), [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync) and [MEM-OBJ-entity-manifests](memory.md#mem-obj-entity-manifests).

### Admission, transformation and authority

Explicit human supply of a user message is a manual content decision. Subsequent model extraction, admission and maintenance remain automatic; authoring or spending authorization does not approve their contents. Generic caller-controlled remember/import/reviewer APIs cannot establish human control. Rejected resolver operations can still admit assertions, so operation rejection is not a universal content veto. See [MEM-OBJ-events](memory.md#mem-obj-events), [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission), [EPI-RTE-ops-disposition](epistemic.md#epi-rte-ops-disposition) and [WF-RTE-report-delivery](workflow.md#wf-rte-report-delivery).

Event-to-standing-fact extraction supports consolidation without proving semantic faithfulness. Resolver updates, deduplication, temporal withdrawal, lifecycle promotion and age/access decay have distinct mechanisms. Generated newFacts do not establish novel-claim synthesis: the accepted epistemic records leave semantic preservation, entailment and non-entailment unresolved. Retained criticism or improved knowledge is not inferred from heal's name. See [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [MEM-RTE-temporal-history](memory.md#mem-rte-temporal-history), [EPI-RTE-heal-dispose](epistemic.md#epi-rte-heal-dispose) and [MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal).

Persisted manifest language guides writers while symbolic constraints validate and sometimes veto candidates. Access/trust/validity fields act at ranking, filtering and scheduling consumers; default inclusion of drafts prevents a blanket enforcement interpretation. Task descriptions afford standing action requests, but the benchmark does not deliver them. Trace inputs have learning authority at their durable update consumer; resulting facts have knowledge authority downstream. These forces do not imply improved capacity. See [MEM-BAP-manifest-guidance](memory.md#mem-bap-manifest-guidance), [MEM-OBJ-entry-metadata](memory.md#mem-obj-entry-metadata), [EPI-OBJ-task-description](epistemic.md#epi-obj-task-description) and [EPI-RTE-grounding-status](epistemic.md#epi-rte-grounding-status).

### Read-back and trace-source distinctions

A requested read remains pull even when its implementation ranks and packs results. The benchmark's requested memory return is not counted again as push merely because it enters an answer prompt. ScopeLab separately supplies selected context before Gemini asks for memory, and maintenance automatically supplies selected retained context to its providers. These independent selector operations support push. ScopeLab retains a lexical finding only: its accepted records do not establish caller-specific embedding-enabled selection, so the former local wired inferred-embedding finding is withdrawn rather than downgraded to a conditional capability. The separately recorded ops vector selector remains wired. The profile distinguishes coarse windows/eligibility from lexical anchors and vector/keyword neighbors; IDs on requested history or graph objects and resolver aliases do not establish identifier-targeted push. See [RT-RTE-memory-read](runtime.md#rt-rte-memory-read), [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer), [RT-BAP-memory-context](runtime.md#rt-bap-memory-context), [MEM-RTE-heal-memory](memory.md#mem-rte-heal-memory) and [EPI-RTE-ops-classify](epistemic.md#epi-rte-ops-classify).

The benchmark original input is session turns, despite observation-event serialization. ScopeLab additionally records tool-call/result traces. Durable access feedback is a separate runtime-event route: read activity becomes counters/times consumed by later ordering and retention. Generic event/document APIs and imported summaries cannot establish original trace content. Supported local yes findings do not resolve those alternatives or license a complete trace-source union; no absence record supports local or system-wide no. See [WF-RTE-replay-cache](workflow.md#wf-rte-replay-cache), [MEM-OBJ-events](memory.md#mem-obj-events), [RT-RTE-memory-read](runtime.md#rt-rte-memory-read) and [MEM-OBJ-entity-summary](memory.md#mem-obj-entity-summary).

### Reconciliation and source-read log

The supplied reconciliation supersedes the epistemic fact-text declaration with [MEM-OBJ-entry-text](memory.md#mem-obj-entry-text); this profile uses that canonical object. Task descriptions and grounding trust remain valid parts of the memory containers, and runtime route containers coexist with their specialist functions. No other supersession changes a value. The ops and benchmark refinements resolve previously open details rather than upgrading evidence strength.

No frozen source file was read for this classification. All warrants are accepted member records and their supplied annotations, resolved through the supplied reconciliation. No records, quotations or new source evidence were added.
