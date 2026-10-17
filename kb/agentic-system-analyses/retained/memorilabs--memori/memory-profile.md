---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Memori memory profile across SDK retained conversations, derived memory, hosted resume routes
  and benchmark artifacts at the frozen partial-loop boundary.
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
source-identity: https://github.com/MemoriLabs/Memori
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
memory-comparison:
  version: 2
  scope: 'Included: accumulated conversation rows, derived facts, embeddings, mention/access metadata,
    summaries, graph triples, process attributes, hosted conversation/agent/resume memory, benchmark index/metadata/report
    parts and unresolved feedback retention; their admission, maintenance and later-consumer routes, including
    native mock/fallback and uninspected adapter/framework alternatives. Excluded: transient provider
    request envelopes, static shipped skills/configuration, inference/embedding model weights and external
    host machinery. Hosted retained state is included at its client boundary, with private implementation
    unresolved.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Inspected SQLite conversations, facts, summaries, process attributes and access metadata
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-process-attribute
          - memory.md#mem-obj-fact-access
          note: SQLite driver storage is directly recorded.
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-process-attribute
          - memory.md#mem-obj-fact-access
          note: Relational rows and joins implement these same retained parts.
        records:
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-fact-access
        note: These retained parts are database rows/columns, not transient request messages.
      - scope: SQLite semantic graph and fact-vector access structures
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-content-embedding
          note: Graph tables and embedding fields reside in SQLite.
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-content-embedding
          note: Structured tables/columns hold graph relations and vectors.
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-knowledge-graph
          note: Subject/predicate/object relations are retained in database graph tables.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-content-embedding
          - memory.md#mem-rte-fact-selection
          note: Stored dense embeddings are consumed by similarity search.
        records:
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-content-embedding
        note: Logical graph/vector stores coexist with their physical SQLite substrate.
      - scope: Benchmark FAISS index, metadata and evaluation JSON
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          note: FAISS and JSON artifacts are filesystem outputs.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          note: The retained FAISS index supplies dense retrieval.
        records:
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-benchmark-reload
        note: Notebooks write and later reload index/metadata files; reports are saved locally.
      - scope: Hosted conversations, agent memory, resume material and cloud SDK memory
        assessment: partial
        findings:
        - value: service-object
          basis: wired
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-rte-augmentation-admission
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          note: SDKs and tools access retained state through hosted service interfaces.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-rte-augmentation-admission
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        note: Client contracts establish service-held state, not its private physical stores or ontology.
      - scope: Other configured drivers and bridges
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-content-embedding
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-rte-benchmark-reload
        note: Configured database alternatives remain included; their physical substrate semantics were
          not independently audited.
      - scope: Feedback retention behind submission endpoint
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-feedback-submission
        note: Transmission is wired; whether feedback is retained and in what substrate is unavailable.
      records:
      - memory.md#mem-obj-conversation-message
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-obj-fact-access
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-content-embedding
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-benchmark-reload
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-rte-augmentation-admission
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-typescript-hooks
      - memory.md#mem-rte-feedback-submission
      note: Local rows, access structures, evaluator files and hosted interfaces are covered; private
        storage and cross-adapter implementation remain unresolved.
    representational_form:
      assessment: partial
      units:
      - scope: Local message/fact/summary/attribute text and benchmark prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-process-attribute
          - memory.md#mem-obj-benchmark-artifacts
          note: Retained utterances, assertions, summaries, attributes, answers and judgments are textual.
        records:
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-benchmark-artifacts
        note: Text is interpreted as language by models or report readers; attributes have no established
          model-facing reader.
      - scope: Roles, IDs, joins, graph fields, access counts and benchmark labels/metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-fact-access
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-process-attribute
          - memory.md#mem-obj-benchmark-artifacts
          - epistemic.md#epi-obj-benchmark-verdict
          note: Replay, joins, graph writes, candidate ordering and metric rules consume structured fields.
        records:
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-fact-access
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-benchmark-artifacts
        - epistemic.md#epi-obj-benchmark-verdict
        note: These localized structures have fixed program consumers, independently of their textual
          values.
      - scope: Fact embeddings and benchmark FAISS vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-content-embedding
          - memory.md#mem-obj-benchmark-artifacts
          note: Dense representations distribute similarity information across numerical dimensions.
        records:
        - memory.md#mem-obj-content-embedding
        - memory.md#mem-obj-benchmark-artifacts
        note: Dense numerical memory representations, not mutable inference-model weights.
      - scope: Client-visible agent recall/compaction response envelope
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-agent-memory
          note: Clients serialize structured service responses.
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-bap-host-memory-guidance
          note: Compaction guidance advertises standing orders and continuation prose.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-bap-host-memory-guidance
        note: JSON serialization is wired, while natural-language resume fields are advertised rather
          than inspected instances; this does not classify the private retained payload.
      - scope: Private hosted representation and feedback payload retention
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-memory
        - memory.md#mem-rte-feedback-submission
        - runtime.md#rt-rte-augmentation-admission
        note: No private representation or retained feedback instance is established; visible display
          fields cannot resolve it.
      records:
      - memory.md#mem-obj-conversation-message
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-obj-fact-access
      - memory.md#mem-obj-knowledge-graph
      - epistemic.md#epi-obj-benchmark-verdict
      - memory.md#mem-obj-content-embedding
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-bap-host-memory-guidance
      - memory.md#mem-rte-feedback-submission
      - runtime.md#rt-rte-augmentation-admission
      note: Text, fixed-rule structures and dense representations are distinct known parts. Hosted consumed
        payload internals and some downstream consumers remain unresolved.
    lineage:
      assessment: partial
      units:
      - scope: Adapted conversation history from completed interactions
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-stream-exhaustion
          note: Persisted role/content rows originate in recorded interactions.
        records:
        - memory.md#mem-obj-conversation-message
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-stream-exhaustion
        note: Provider adaptation and persistence extract conversation activity, with lossy replay rather
          than an untouched execution trace.
      - scope: Service-proposed facts, summaries, triples and process attributes
        assessment: partial
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-augmentation-admission
          - epistemic.md#epi-clm-structured-memory
          note: The documented augmentation contract extracts memory from conversations.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-entity-fact
          - epistemic.md#epi-rte-triple-rendering
          note: Client rendering compiles structured triple fields into fact text.
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - runtime.md#rt-rte-augmentation-admission
        - epistemic.md#epi-clm-structured-memory
        note: The client mapping is wired, but the service derivation and semantic preservation are opaque;
          mock/fallback alternatives are separate.
      - scope: Embeddings and access metadata constructed from admitted content
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-content-embedding
          - memory.md#mem-obj-fact-access
          note: Embedding, hashing, counters and mention attachment derive access structures from retained
            content.
        records:
        - memory.md#mem-obj-content-embedding
        - memory.md#mem-obj-fact-access
        note: Vector generation and metadata derivation are recorded; immutable embedding-model provenance
          is not.
      - scope: Native mock and empty-operation content fallback
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - runtime.md#rt-rte-augmentation-admission
        note: Emission alternatives are recorded, but supplied mock/content origin and adapter persistence
          are not established; no universal service-extracted lineage follows.
      - scope: Benchmark initial memories and derived index/report artifacts
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          note: Notebooks acquire preaugmented memory data externally.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          - epistemic.md#epi-rte-benchmark-retention
          note: Encoding, metadata assembly and report serialization construct new access/report artifacts.
        records:
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-benchmark-reload
        - epistemic.md#epi-rte-benchmark-retention
        note: Imported JSON is external preaugmented content; upstream trace ancestry is not frozen.
      - scope: Hosted agent memory/resume lineage and feedback disposition
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-memory
        - memory.md#mem-rte-feedback-submission
        note: Submitted turns and traces are known inputs, but private retention/derivation and feedback
          use cannot be reconstructed from the client.
      records:
      - memory.md#mem-obj-conversation-message
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-stream-exhaustion
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - runtime.md#rt-rte-augmentation-admission
      - epistemic.md#epi-clm-structured-memory
      - memory.md#mem-obj-content-embedding
      - memory.md#mem-obj-fact-access
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-benchmark-reload
      - epistemic.md#epi-rte-benchmark-retention
      - memory.md#mem-obj-agent-memory
      - memory.md#mem-rte-feedback-submission
      note: Recorded derivation paths do not resolve private extraction, external benchmark ancestry,
        vector-model provenance or native fallback authorship.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Replayed conversation, recalled facts and joined summaries at provider input
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-fact-selection
          - runtime.md#rt-bap-recalled-context
          note: Provider receives retained text as context/reference.
        records:
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-fact-selection
        - runtime.md#rt-bap-recalled-context
        note: Delivery gives contextual force at the next inference, not enforced truth or reliable obedience.
      - scope: Retained fact text, vectors and access counters at recall selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-content-embedding
          - memory.md#mem-obj-fact-access
          - memory.md#mem-rte-fact-selection
          note: These retained inputs affect candidate eligibility and ordering under fixed code.
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-content-embedding
        - memory.md#mem-obj-fact-access
        - memory.md#mem-rte-fact-selection
        note: Text lexical scores, vector similarity and candidate recency/count ordering influence relative
          priority.
      - scope: Prior Python conversation summary at next augmentation
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-augmentation-admission
          note: Retained derived experience feeds an update to durable later-consumed memory.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-augmentation-admission
          note: Existing-summary state selects the next extraction input window.
        records:
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-augmentation-admission
        note: Summary text feeds subsequent durable derivation; its presence also selects the latest user/assistant
          pair. Rust sends no prior summary.
      - scope: Benchmark retained metadata/index at retrieval and answer model
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          note: Dense and lexical retrieval score retained memory content.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          note: Selected memories and session summaries supply answer-model context.
        records:
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-benchmark-reload
        note: Index and prose have distinct consumers and effects.
      - scope: Hosted recall/resume results at requesting foreground agents
        assessment: partial
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-rte-hermes-provider
          note: Requested recall supplies contextual material to the agent.
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-bap-host-memory-guidance
          note: Compaction guidance advertises retained standing orders and expected formats for continuation.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-bap-host-memory-guidance
        - runtime.md#rt-rte-hermes-provider
        note: Result delivery is wired; advertised standing-order fields and their actual contents are
          not inspected. Static shipped skills are excluded as accumulated memory.
      - scope: Graph rows, process attributes, retained evaluation reports and feedback downstream
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-feedback-submission
        - epistemic.md#epi-rte-benchmark-retention
        note: Storage/report output and feedback transmission are established, but later readers or adaptation
          consumers are not inspected; no enforcement, validation or learning authority is inferred.
      records:
      - memory.md#mem-obj-conversation-message
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-rte-fact-selection
      - runtime.md#rt-bap-recalled-context
      - memory.md#mem-obj-content-embedding
      - memory.md#mem-obj-fact-access
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-benchmark-reload
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-bap-host-memory-guidance
      - runtime.md#rt-rte-hermes-provider
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-rte-feedback-submission
      - epistemic.md#epi-rte-benchmark-retention
      note: Authority is assigned to actual part/consumer/effect paths, not all outputs of augmentation.
        Opaque hosted outputs and uninspected graph/process/feedback consumers prevent completeness.
    write_agency:
      assessment: partial
      units:
      - scope: Completed-turn conversation admission and generic-stream exhaustion writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          - runtime.md#rt-rte-stream-exhaustion
          - memory.md#mem-obj-conversation-message
          note: Capture/persistence handlers admit content without per-item human review.
        records:
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        - runtime.md#rt-rte-stream-exhaustion
        - memory.md#mem-obj-conversation-message
        note: Software decides to persist formatted turns; a human starting a call is not per-content
          approval.
      - scope: Mapped service response, graph/process/summary writes and access updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-augmentation-admission
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-knowledge-graph
          - memory.md#mem-obj-process-attribute
          - memory.md#mem-obj-fact-access
          - epistemic.md#epi-rte-memory-scheduling
          note: Software admits returned fields and updates counters/summary rows.
        records:
        - runtime.md#rt-rte-augmentation-admission
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-fact-access
        - epistemic.md#epi-rte-memory-scheduling
        note: Client mapping, nonempty checks and driver rules admit writes automatically, independently
          of opaque proposal policy.
      - scope: Host capture under Hermes/OpenClaw/Claude and MCP submission policy
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-provider
          - runtime.md#rt-rte-openclaw-hooks
          - runtime.md#rt-rte-claude-skill
          note: Host callbacks or foreground-agent/CLI submissions require no per-content human confirmation.
        - value: automatic
          basis: claimed
          records:
          - runtime.md#rt-rte-mcp-guidance
          note: Durable-only guidance delegates content submission to the foreground agent.
        records:
        - runtime.md#rt-rte-hermes-provider
        - runtime.md#rt-rte-openclaw-hooks
        - runtime.md#rt-rte-claude-skill
        - runtime.md#rt-rte-mcp-guidance
        note: Capture wiring is inspected for shipped clients; MCP agent admission is documented, not
          server implementation.
      - scope: Benchmark index, metadata, answers and report admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-benchmark-artifacts
          - memory.md#mem-rte-benchmark-reload
          - epistemic.md#epi-rte-benchmark-retention
          note: Notebook code constructs and writes derived artifacts.
        records:
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-benchmark-reload
        - epistemic.md#epi-rte-benchmark-retention
        note: Running a notebook does not constitute explicit approval of each retained output.
      - scope: Native mock/fallback content control, private hosted initialization and feedback handling
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-agent-memory
        - memory.md#mem-rte-feedback-submission
        note: Generic caller or submission identity does not decide human versus computational admission.
          No manual classification is established.
      - scope: Explicit entity withdrawal caller decision
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-entity-withdrawal
        note: The API caller chooses destructive maintenance, but the records do not identify an explicit
          human content decision.
      records:
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-typescript-hooks
      - runtime.md#rt-rte-stream-exhaustion
      - memory.md#mem-obj-conversation-message
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-obj-fact-access
      - epistemic.md#epi-rte-memory-scheduling
      - runtime.md#rt-rte-hermes-provider
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-rte-claude-skill
      - runtime.md#rt-rte-mcp-guidance
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-benchmark-reload
      - epistemic.md#epi-rte-benchmark-retention
      - memory.md#mem-obj-agent-memory
      - memory.md#mem-rte-feedback-submission
      - memory.md#mem-rte-entity-withdrawal
      note: Automatic client admission is known. Caller identity is not a human decision; private initialization,
        fallback content control and feedback handling remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Mutable local conversation summary
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - epistemic.md#epi-rte-local-retention
          note: UPDATE overwrites the existing summary entry.
        records:
        - memory.md#mem-obj-conversation-summary
        - epistemic.md#epi-rte-local-retention
        note: An existing summary field is replaced. This establishes revision, not semantic correctness
          or retained revision history.
      - scope: Recall-time removal of repeated summary text
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-rte-benchmark-reload
          note: Selected summaries are made unique before model-context delivery.
        records:
        - memory.md#mem-rte-fact-selection
        - memory.md#mem-rte-benchmark-reload
        note: This is deduplication of the selected representation, not deletion or merging of durable
          fact rows.
      - scope: SQLite repeated-fact metadata refresh affecting bounded recall
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - memory.md#mem-obj-fact-access
          - memory.md#mem-rte-fact-selection
          note: Repetition refreshes salience through recency/count-ordered candidate selection.
        records:
        - memory.md#mem-obj-fact-access
        - memory.md#mem-rte-fact-selection
        note: Counter/time refresh raises subsequent candidate eligibility. Primary-key collision checking
          alone is not classified as deduplication.
      - scope: BYODB entity fact/graph deletion
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-entity-withdrawal
          note: Deleting facts/graph entries removes them from future local selection.
        records:
        - memory.md#mem-rte-entity-withdrawal
        note: Forgetting is destructive for the selected retained rows, while conversation history remains;
          this is not history-preserving invalidation.
      - scope: Hosted fact extraction, summaries and resume generation
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-augmentation-admission
          - memory.md#mem-obj-agent-memory
          - epistemic.md#epi-clm-structured-memory
          note: Declared extraction and summary generation compress retained conversation claims.
        records:
        - runtime.md#rt-rte-augmentation-admission
        - memory.md#mem-obj-agent-memory
        - epistemic.md#epi-clm-structured-memory
        note: The declared extraction/summary contract reduces conversational material; the implemented
          server transformation is unavailable.
      - scope: Native fallback, graph/process semantic maintenance, feedback-driven changes and alternative
          drivers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-rte-feedback-submission
        - runtime.md#rt-rte-augmentation-admission
        note: Recorded writes, conversions and index construction do not establish further controlled
          curation operations. No synthesis or semantic invalidation is inferred.
      records:
      - memory.md#mem-obj-conversation-summary
      - epistemic.md#epi-rte-local-retention
      - memory.md#mem-rte-fact-selection
      - memory.md#mem-rte-benchmark-reload
      - memory.md#mem-obj-fact-access
      - memory.md#mem-rte-entity-withdrawal
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-agent-memory
      - epistemic.md#epi-clm-structured-memory
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-rte-feedback-submission
      note: Local summary replacement, read-time deduplication, salience refresh and destructive forgetting
        are implemented. Hosted consolidation is claimed; opaque derivation and feedback maintenance remain
        unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: SDK recall backend requests and automatic fact/history delivery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          - memory.md#mem-rte-fact-selection
          note: SDK retrieval fulfills a request to the local/cloud memory backend.
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-obj-conversation-message
          note: Automatic query-based recall and conversation replay supply retained context to subsequent
            provider invocations.
        records:
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        - memory.md#mem-rte-fact-selection
        - memory.md#mem-obj-conversation-message
        note: The wrapper requests retained data; its automatic selector enriches the provider request
          without a consumer request for those memory items.
      - scope: Prior-summary read into Python augmentation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-augmentation-admission
          note: Stored summary is automatically supplied to the next derivation request.
        records:
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-augmentation-admission
        note: On augmentation, software selects retained summary and messages without a separate request
          from the update consumer for those parts.
      - scope: Intentional host recall, summary and compaction
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-rte-hermes-provider
          - runtime.md#rt-rte-claude-skill
          - runtime.md#rt-rte-openclaw-hooks
          note: Foreground-agent tool/CLI calls request retained context.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-rte-hermes-provider
        - runtime.md#rt-rte-claude-skill
        - runtime.md#rt-rte-openclaw-hooks
        note: These inspected clients return requested service material; JSON delivery is not another
          push.
      - scope: Documented MCP retrieval
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-rte-mcp-guidance
          note: MCP agent intentionally requests recall/summary/compaction.
        records:
        - runtime.md#rt-rte-mcp-guidance
        note: Classification concerns the documented route, not verified server operation.
      - scope: Benchmark reload and automatic context selection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-benchmark-reload
          - memory.md#mem-obj-benchmark-artifacts
          note: Saved FAISS and metadata are explicitly reloaded.
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-benchmark-reload
          - memory.md#mem-obj-benchmark-artifacts
          note: Question-triggered selector supplies retained text to the answer prompt.
        records:
        - memory.md#mem-rte-benchmark-reload
        - memory.md#mem-obj-benchmark-artifacts
        note: Notebook reload requests saved artifacts; automatic hybrid retrieval supplies the answer
          model selected memories.
      - scope: Independent graph/process, feedback/report read-back and framework-specific alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-rte-feedback-submission
        - memory.md#mem-obj-benchmark-artifacts
        - runtime.md#rt-rte-python-invocation
        note: No independent later consumer is established for these stored outputs, and framework-specific
          branches are not exhaustively inspected.
      records:
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-typescript-hooks
      - memory.md#mem-rte-fact-selection
      - memory.md#mem-obj-conversation-message
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-rte-hermes-provider
      - runtime.md#rt-rte-claude-skill
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-rte-mcp-guidance
      - memory.md#mem-rte-benchmark-reload
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-rte-feedback-submission
      note: Requested retrieval and automatic within-invocation selection coexist. Internal SDK requests
        are pull operations; unrequested context injection within the chain is push, not independent background
        supply.
    read_back_signal:
      assessment: partial
      units:
      - scope: Invocation-triggered local fact selection
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-obj-content-embedding
          note: Query/fact vector similarity selects fact candidates.
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-obj-entity-fact
          note: Query and fact text contribute lexical ranking.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-obj-fact-access
          - memory.md#mem-obj-conversation-summary
          note: Entity identity scopes candidates and fact IDs/mention joins select associated summaries.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-fact-selection
          - memory.md#mem-obj-fact-access
          note: Storage availability, candidate recency/count limits, top-k and threshold bound delivery
            independently of targeted similarity.
        records:
        - memory.md#mem-rte-fact-selection
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-content-embedding
        - memory.md#mem-obj-fact-access
        - memory.md#mem-obj-conversation-summary
        note: 'Trigger: registered model call. Inputs: query text/embedding and entity; selected parts:
          facts and mention-linked summaries, after bounded candidate ordering and threshold.'
      - scope: Conversation replay and prior-summary augmentation selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-augmentation-admission
          note: Conversation identity selects retained rows/summary for automatic delivery.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-augmentation-admission
          note: Summary availability changes latest-pair versus broader message selection.
        records:
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-augmentation-admission
        note: 'Triggers: later model call or augmentation. Inputs: current resolved conversation identity
          and summary presence; selected parts: matching history rows or summary/latest pair.'
      - scope: Benchmark question-triggered memory selection
        assessment: partial
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-benchmark-reload
          - memory.md#mem-obj-benchmark-artifacts
          note: FAISS similarity selects dense candidates.
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-benchmark-reload
          - memory.md#mem-obj-benchmark-artifacts
          note: BM25 and reciprocal-rank fusion affect selected documents.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-benchmark-reload
          - memory.md#mem-obj-benchmark-artifacts
          note: Available-index and top-k pool limits bound automatic context supply.
        records:
        - memory.md#mem-rte-benchmark-reload
        - memory.md#mem-obj-benchmark-artifacts
        note: 'Trigger: benchmark question. Push selector inputs: question text/embedding and limits;
          selected parts: saved metadata memories and unique session summaries. Conversation ID belongs
          to requested per-conversation index access, not an established identity match selecting delivered
          memory parts. Dense, lexical and coarse selection are supported; records do not establish a
          separate identifier-based push selector or warrant a complete signal inventory.'
      - scope: Intentional host/MCP return operations only
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-rte-mcp-guidance
        - runtime.md#rt-rte-hermes-provider
        note: These requested returns are pull; push-signal classification does not apply to this unit.
      - scope: Cloud SDK internal selection and other uninspected consumer branches
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        - memory.md#mem-obj-agent-memory
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-rte-feedback-submission
        note: Client query/filter transmission does not establish the service selector; no inferred-judgment
          or complete signal inventory is established.
      records:
      - memory.md#mem-rte-fact-selection
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-content-embedding
      - memory.md#mem-obj-fact-access
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-conversation-message
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-rte-benchmark-reload
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-rte-mcp-guidance
      - runtime.md#rt-rte-hermes-provider
      - runtime.md#rt-rte-typescript-hooks
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-rte-feedback-submission
      note: Signals describe automatic selectors only. Requested host project/session/category filters
        are not additional push signals; private SDK selection and uninspected alternatives remain unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Ordinary SDK conversation-to-derived-facts/summaries-to-later-provider chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-augmentation-admission
          - memory.md#mem-obj-entity-fact
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-fact-selection
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          note: Automatic trace-fed writes produce durable context-shaping artifacts consumed by later
            invocations.
        records:
        - runtime.md#rt-rte-augmentation-admission
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-fact-selection
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        note: Completed interaction messages feed automatic retained outputs and later wired model-context
          delivery. Server semantics remain opaque without negating this client-mediated chain.
      - scope: Python recursive summary update chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-augmentation-admission
          - memory.md#mem-rte-fact-selection
          note: Automatically updated summary is reused by derivation and later fact-associated context
            delivery.
        records:
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-augmentation-admission
        - memory.md#mem-rte-fact-selection
        note: Existing summary plus latest turns feed subsequent durable memory; Rust summary=None is
          a distinct route.
      - scope: Hosted host-agent memory and resume generation
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-obj-agent-memory
          - runtime.md#rt-bap-host-memory-guidance
          - epistemic.md#epi-clm-structured-memory
          note: The declared hosted chain derives reusable context/resume memory from captured activity.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-bap-host-memory-guidance
        - runtime.md#rt-rte-hermes-provider
        - runtime.md#rt-rte-openclaw-hooks
        - runtime.md#rt-rte-claude-skill
        - runtime.md#rt-rte-mcp-guidance
        note: Trace submission and requested delivery are wired in clients, but private derivation/retention
          and actual resume fields are unavailable.
      - scope: Native mock/fallback, graph/process independent consumer routes, benchmark import ancestry
          and feedback adaptation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-feedback-submission
        note: Mock/content origin, separate later consumers, upstream benchmark extraction and feedback
          updates are unresolved. Raw persistence/report creation alone does not establish qualifying
          learning; no system-wide no is inferred.
      records:
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-rte-fact-selection
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-typescript-hooks
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-bap-host-memory-guidance
      - runtime.md#rt-rte-hermes-provider
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-rte-claude-skill
      - runtime.md#rt-rte-mcp-guidance
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-feedback-submission
      note: Automatic trace-fed durable fact/summary production has a later context consumer. That architectural
        channel is not observed improvement; opaque hosted and native alternatives cannot inherit complete
        classification.
    trace_source:
      assessment: partial
      units:
      - scope: Ordinary SDK fact/summary writes and recursive Python summary updates
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-augmentation-admission
          - memory.md#mem-obj-conversation-message
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-rte-python-invocation
          - runtime.md#rt-rte-typescript-hooks
          note: Interaction messages are the source of later context-shaping memory.
        records:
        - runtime.md#rt-rte-augmentation-admission
        - memory.md#mem-obj-conversation-message
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-python-invocation
        - runtime.md#rt-rte-typescript-hooks
        note: Original qualifying inputs are recorded user/assistant conversational turns; prior derived
          summary is intermediate material, not a new trace source.
      - scope: Declared hosted agent-memory derivation with optional trace payload
        assessment: partial
        findings:
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-obj-agent-memory
          - epistemic.md#epi-clm-structured-memory
          note: Hosted augmentation is declared to consume user/assistant turns.
        - value: tool-traces
          basis: claimed
          records:
          - runtime.md#rt-rte-hermes-provider
          - runtime.md#rt-rte-openclaw-hooks
          - memory.md#mem-obj-agent-memory
          - epistemic.md#epi-clm-structured-memory
          note: The declared trace-aware chain accepts recorded tool requests/results, not merely a synthetic
            role label.
        records:
        - memory.md#mem-obj-agent-memory
        - runtime.md#rt-rte-hermes-provider
        - runtime.md#rt-rte-openclaw-hooks
        - runtime.md#rt-rte-claude-skill
        - runtime.md#rt-rte-mcp-guidance
        note: Completed turns and tool names/args/results can be submitted. Whether the private update
          consumes every optional trace is not established; native and cloud payloads differ.
      - scope: Native mock/fallback, benchmark preaugmented input, feedback and unresolved consumer routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-entity-fact
        - memory.md#mem-obj-benchmark-artifacts
        - memory.md#mem-rte-feedback-submission
        - memory.md#mem-obj-knowledge-graph
        - memory.md#mem-obj-process-attribute
        note: Original qualifying trace content or the qualifying update itself is unresolved. Hook triggering
          alone does not add event-streams; ordered conversation does not establish state/action/outcome
          trajectories.
      records:
      - runtime.md#rt-rte-augmentation-admission
      - memory.md#mem-obj-conversation-message
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-rte-python-invocation
      - runtime.md#rt-rte-typescript-hooks
      - memory.md#mem-obj-agent-memory
      - runtime.md#rt-rte-hermes-provider
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-rte-claude-skill
      - runtime.md#rt-rte-mcp-guidance
      - memory.md#mem-obj-entity-fact
      - memory.md#mem-obj-benchmark-artifacts
      - memory.md#mem-rte-feedback-submission
      - memory.md#mem-obj-knowledge-graph
      - memory.md#mem-obj-process-attribute
      note: Conversational session sources are established for the wired SDK chain. Host tool trace inputs
        are recorded but private use is unresolved; benchmark upstream and other unknown routes prevent
        complete source coverage.
---

# Memori memory profile

## Comparison rationale

This profile classifies the supplied accepted records, not a newly inspected implementation. No source reads were needed. All implementation findings are wiring, not observed activation or causal benefit. Claimed hosted transformations remain claimed even beside wired client submission, local persistence and tool-result delivery.

### Canonical identities and coverage

Reconciliation supersedes the epistemic fact, triple, summary, process-attribute and embedding object declarations with the corresponding memory objects. It also supersedes epistemic recall-selection, entity-withdrawal and feedback-delivery with their memory route declarations. This profile uses those canonical destinations. Their epistemic annotations and function-level assessments still constrain meaning; supersession establishes identity, not stronger evidence. In particular, [MEM-OBJ-entity-fact](memory.md#mem-obj-entity-fact) retains mock/fallback emission and [MEM-RTE-fact-selection](memory.md#mem-rte-fact-selection) retains selection rather than truth endorsement.

The broader [EPI-OBJ-conversation-messages](epistemic.md#epi-obj-conversation-messages) is not identical to persisted [MEM-OBJ-conversation-message](memory.md#mem-obj-conversation-message): transmitted host trace fields are not proven retained row fields. The benchmark artifact container and its answer/judgment function records likewise remain distinct. No superseded record is used as a classification destination.

Every axis remains partial because an opaque or uninspected included branch cannot be omitted to make the inventory complete. Graph/process storage is known without a separate later model-facing consumer. Feedback submission is known without retained feedback or an adaptation consumer. Benchmark import is known without the upstream memory-producing trace. These are different limitations, not evidence of absent mechanisms.

### Part and consumer distinctions

The SQLite substrate also supports relational, graph and vector access structures; the values describe coexisting mechanisms rather than separate copies. Numerical fact embeddings are parametric representations, not learned model weights. Benchmark files are an independent retained route. The hosted service interface does not identify the private storage engine or representation. See [MEM-OBJ-content-embedding](memory.md#mem-obj-content-embedding), [MEM-OBJ-knowledge-graph](memory.md#mem-obj-knowledge-graph), [MEM-OBJ-agent-memory](memory.md#mem-obj-agent-memory) and [MEM-OBJ-benchmark-artifacts](memory.md#mem-obj-benchmark-artifacts).

Facts can have ranking authority as lexical inputs and knowledge authority at provider delivery. A prior summary has learning authority at the update consumer and knowledge authority at the later answering consumer; its presence also routes extraction to the latest pair. These classifications neither certify truth nor establish improved capacity. Standing-order instruction is retained only as a claimed hosted output path, not inferred from a system-role envelope or static shipped skill. See [MEM-OBJ-conversation-summary](memory.md#mem-obj-conversation-summary), [MEM-RTE-fact-selection](memory.md#mem-rte-fact-selection) and [RT-BAP-host-memory-guidance](runtime.md#rt-bap-host-memory-guidance).

### Transformations and read-back chains

Curation follows the recorded transformation. Summary overwrites are evolution; repeated summary removal is read-time deduplication; recurrence refresh changes salience through bounded candidate ordering. Destructive entity deletion is forgetting/decay, not history-preserving invalidation, and it leaves conversations replayable. Primary-key collision checks, triple rendering, embedding attachment and index rebuild alone add no curation value. Hosted extraction/summary consolidation remains claimed because its implemented semantics are unavailable. See [MEM-OBJ-fact-access](memory.md#mem-obj-fact-access), [MEM-OBJ-conversation-summary](memory.md#mem-obj-conversation-summary), [MEM-RTE-entity-withdrawal](memory.md#mem-rte-entity-withdrawal) and [EPI-RTE-triple-rendering](epistemic.md#epi-rte-triple-rendering).

The SDK's backend request is pull; automatic fact/history selection into the provider call is push within that same invocation chain. This does not assert unsolicited background messaging. Intentional host tool returns remain pull even when the client automatically serializes them. Benchmark reload and automatic answer-context selection are similarly separate operations. Identifier findings on the SDK routes name actual entity/conversation/fact matches, not IDs merely present on a catalog. The benchmark conversation ID selects the index during requested access; the records establish no separate identity match selecting delivered memory parts during automatic context selection. Its push-signal unit therefore retains dense, lexical and coarse findings, removes identifier, and remains partial rather than asserting complete coverage. Coarse gates and budgets remain separate from dense/lexical targeting. See [RT-RTE-python-invocation](runtime.md#rt-rte-python-invocation), [RT-RTE-typescript-hooks](runtime.md#rt-rte-typescript-hooks), [MEM-RTE-fact-selection](memory.md#mem-rte-fact-selection) and [MEM-RTE-benchmark-reload](memory.md#mem-rte-benchmark-reload).

### Trace-fed updates and limits

The ordinary SDK chain qualifies for trace learning because automatic interaction-fed writes produce durable facts/summaries for later model context. Opaque server semantics prevent stronger content/warrant conclusions, not the wired existence of that mediated chain. Raw-log capture by itself, generic-stream persistence without augmentation, benchmark judgment retention and feedback transmission do not supply a qualifying positive or a bounded system-wide negative. Optional host tool traces support a claimed hosted source path, not proof every result reaches extraction. Hook events are triggers, not evidence that the update consumes event-stream content. See [RT-RTE-augmentation-admission](runtime.md#rt-rte-augmentation-admission), [RT-RTE-stream-exhaustion](runtime.md#rt-rte-stream-exhaustion), [MEM-OBJ-agent-memory](memory.md#mem-obj-agent-memory) and [MEM-RTE-feedback-submission](memory.md#mem-rte-feedback-submission).
