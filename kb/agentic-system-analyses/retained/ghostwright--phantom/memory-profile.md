---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Phantom memory comparison: channel vector extraction, selective file guidance, durable chat
  continuity and unresolved SDK history at the frozen revision.'
run-id: AAS-2026-10-15-phantom-cc566f03ac40-01
source-identity: https://github.com/ghostwright/phantom
reviewed-boundary: f8c7ab42d885936ee54abc785528000260f4acc5
memory-comparison:
  version: 2
  scope: 'Retained material accumulated or changed through use: episode/fact/procedure payloads and dense/sparse
    access indexes; evolved and reflection-only files, working memory, append notes and dashboard user
    Markdown; evolution queue/poison/version/reason state; committed chat text, attachment payloads, translated
    events and durable timelines; host SDK-session selectors and opaque dependency-owned histories/checkpoints;
    changed dynamic capabilities and operator extensions/settings; durable scheduled task handoffs. Includes
    write/admission, maintenance and later model/software/client consumption routes. Excludes unmodified
    shipped roles/security/constitution/teaching prompts and baseline skills as accumulated memory, transient
    query coordination/staging/snapshots as standalone durable stores, arbitrary work products without
    a recorded later consumer, and provider model weights without an established in-scope update. External
    SDK retained state is included as opaque, not silently excluded.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Qdrant episode, semantic-fact and procedure payloads and their retrieval indexes
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          - memory.md#mem-obj-procedures
          - memory.md#mem-obj-retrieval-indexes
          note: Qdrant collections retain the payloads and named dense/sparse indexes.
        records:
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-obj-retrieval-indexes
        note: Payloads and access vectors live in the vector store, not in model weights.
      - scope: Evolved files, reflection-only files, working memory, agent notes and user-scope Markdown
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-reflection-context
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          - memory.md#mem-obj-user-memory
          note: These named memory surfaces are filesystem files.
        records:
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        - memory.md#mem-obj-user-memory
        note: The live EvolvedConfig copy is backed by retained filesystem text.
      - scope: Evolution queue and poison state
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          note: Queue and rejection state persist in SQLite.
        records:
        - memory.md#mem-obj-evolution-queue
        note: Staging JSONL is a transient delivery copy, not an additional durable memory substrate.
      - scope: Evolution versions, gate logs, change summaries and metrics
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-evolution-log
          note: Version JSON and log/metrics files retain metadata and reasons.
        records:
        - memory.md#mem-obj-evolution-log
        note: Transient snapshots are not a retained Git repository of prior versions.
      - scope: Committed web transcript, translated events and derived timelines
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          note: Message JSON, event JSON and timeline summary JSON are stored in SQLite.
        records:
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        note: Attachment payloads are split from descriptors and message rows.
      - scope: Chat binary attachments
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          note: Binary attachment payloads reside in files alongside database metadata.
        records:
        - memory.md#mem-obj-chat-transcript
        note: The record establishes attachment files, not a text rendering of their contents.
      - scope: SDK session access rows
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - runtime.md#rt-obj-session-store
          note: Session rows retain SDK IDs and timestamps.
        records:
        - runtime.md#rt-obj-session-store
        note: These are selectors, not the selected SDK conversation.
      - scope: Dynamic capability definitions and executable script files
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          note: Definitions persist in dynamic_tools.
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          note: An operative Map holds reloaded definitions for registration and lookup.
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-dynamic-tools
          note: Script-path handlers execute independently retained script file contents.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-dynamic-tools
        note: Definitions are durable in SQLite and reloaded into a Map; script bodies can mutate separately.
      - scope: Changed skills, subagent instructions, hooks, plugin settings and runtime YAML
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-operator-config
          note: Markdown/settings/YAML mutations persist on disk.
        records:
        - runtime.md#rt-rte-operator-config
        note: Only changed or installed content is included, not shipped static defaults.
      - scope: Scheduled job instruction and dispatch metadata
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          note: scheduled_jobs rows retain task and schedule.
        records:
        - workflow.md#wf-obj-scheduled-job
        note: A retained future-work handoff, distinct from learned vector procedures.
      - scope: Dependency-owned persisted SDK conversations and compaction payloads
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: The records distinguish SDK persistence from host rows but do not inspect its storage implementation.
          No host SQLite or file classification is transferred to the opaque payload.
      records:
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-procedures
      - memory.md#mem-obj-retrieval-indexes
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-user-memory
      - memory.md#mem-obj-evolution-queue
      - memory.md#mem-obj-evolution-log
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-rte-dynamic-tools
      - runtime.md#rt-rte-operator-config
      - workflow.md#wf-obj-scheduled-job
      - runtime.md#rt-rte-chat-context
      note: The inventory covers vector memory and indexes, file memories and extensions, chat stores,
        learning controls, session selectors and scheduled handoffs. SDK-owned retained conversation/checkpoint
        storage is unresolved; external inference weights are not assumed to be accumulated memory.
    representational_form:
      assessment: partial
      units:
      - scope: Episode/fact/procedure text at model and requested lookup consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          - memory.md#mem-obj-procedures
          - memory.md#mem-rte-vector-context
          - memory.md#mem-rte-memory-tools
          note: Selected summaries, facts and steps are interpreted as contextual advice.
        records:
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-rte-vector-context
        - memory.md#mem-rte-memory-tools
        note: Natural-language assertions and suggested procedure actions are not executable code.
      - scope: Vector-payload validity, IDs, counters, ordering and access metadata at store selectors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          - memory.md#mem-obj-procedures
          - epistemic.md#epi-rte-validity-change
          note: Validity filters, numeric confidence comparisons, step order and access metadata have
            symbolic consumers.
        records:
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-rte-vector-context
        - epistemic.md#epi-rte-validity-change
        note: Localized fields receive fixed-code consequences independently of the text.
      - scope: Dense retrieval vectors
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-indexes
          note: Ollama-generated dense numerical representations support retrieval.
        records:
        - memory.md#mem-obj-retrieval-indexes
        note: The dense encodings are not trained Phantom weights; unused episode detail vectors are retained
          but not used by summary recall.
      - scope: Sparse hashed token-frequency indexes
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-indexes
          note: Sparse token indices and frequencies are deterministic localized retrieval features.
        records:
        - memory.md#mem-obj-retrieval-indexes
        note: Numerical values alone do not make localized token features parametric.
      - scope: File-memory prose, reflection inputs/reasons and rendered host continuity text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-reflection-context
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          - memory.md#mem-obj-user-memory
          - memory.md#mem-obj-evolution-queue
          - memory.md#mem-obj-evolution-log
          - runtime.md#rt-obj-chat-context
          note: Retained prose and its rendered projections require model or human interpretation.
        records:
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        - memory.md#mem-obj-user-memory
        - memory.md#mem-obj-evolution-queue
        - memory.md#mem-obj-evolution-log
        - runtime.md#rt-obj-chat-context
        note: This includes readable content, not path and status metadata.
      - scope: Evolution controls, session selectors and file access metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - memory.md#mem-obj-evolution-log
          - runtime.md#rt-obj-session-store
          - memory.md#mem-obj-user-memory
          note: Fixed-code consumers interpret these localized control fields.
        records:
        - memory.md#mem-obj-evolution-queue
        - memory.md#mem-obj-evolution-log
        - runtime.md#rt-obj-session-store
        - memory.md#mem-obj-user-memory
        note: IDs, retries, versions, paths and timestamps are separate from prose.
      - scope: Committed chat text and readable event/timeline labels or summaries
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          note: Text content and readable summaries are interpreted by users or later agents.
        records:
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        note: Not all stored JSON fields are prose.
      - scope: Chat sequence/status/artifact descriptors and checkpoint counters
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          - runtime.md#rt-rte-chat-context
          note: Code extracts/filter/deduplicates artifacts and compaction metadata.
        records:
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        - runtime.md#rt-rte-chat-context
        note: These are host metadata, not a semantic classification of the SDK checkpoint.
      - scope: Dynamic handler code, schemas, names and paths
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-bap-handler-execution
          note: Handler execution and dispatch interpret retained symbolic definitions.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-bap-handler-execution
        note: Code and schema are distinct from the description interpreted by the model.
      - scope: Dynamic descriptions and changed skill/subagent instruction bodies
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-operator-config
          note: Descriptions and Markdown bodies are model-facing language.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-operator-config
        note: Natural-language instruction or selection guidance coexists with symbolic configuration.
      - scope: Changed hook/plugin settings, extension frontmatter and runtime YAML controls
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-operator-config
          note: Settings and frontmatter contain localized controls requested by the SDK/startup consumer.
        records:
        - runtime.md#rt-rte-operator-config
        note: The external SDK activation semantics remain uninspected.
      - scope: Scheduled task prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          note: The future invocation receives the job instruction.
        records:
        - workflow.md#wf-obj-scheduled-job
        note: The main model interprets the stored task.
      - scope: Scheduled dispatch state
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: Schedule, status, target and counters determine dispatch/bookkeeping.
        records:
        - workflow.md#wf-obj-scheduled-job
        - runtime.md#rt-rte-direct-work
        note: The timer/executor consumes fixed fields.
      - scope: Binary attachment content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-chat-transcript
        note: A file name and descriptor do not establish whether the payload is natural language, symbolic
          or distributed-parametric.
      - scope: SDK persisted conversation and compaction payload
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: No payload inspection establishes its mixture of verbatim turns, generated summary, tool
          content or hidden state.
      records:
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-procedures
      - memory.md#mem-rte-vector-context
      - memory.md#mem-rte-memory-tools
      - epistemic.md#epi-rte-validity-change
      - memory.md#mem-obj-retrieval-indexes
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-user-memory
      - memory.md#mem-obj-evolution-queue
      - memory.md#mem-obj-evolution-log
      - runtime.md#rt-obj-chat-context
      - runtime.md#rt-obj-session-store
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - runtime.md#rt-rte-chat-context
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-bap-handler-execution
      - runtime.md#rt-rte-operator-config
      - workflow.md#wf-obj-scheduled-job
      - runtime.md#rt-rte-direct-work
      note: Text, control fields and dense numerical indexes have separate consumers. Binary attachment
        encoding and opaque SDK content remain unresolved; readable host compact-boundary metadata does
        not classify the provider summary.
    lineage:
      assessment: partial
      units:
      - scope: Channel-derived episodes and semantic facts
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-vector-extraction
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          note: Channel session messages feed heuristic episode and fact extraction.
        records:
        - memory.md#mem-rte-vector-extraction
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        note: Source message fragments and caller metadata are transformed without a per-fact content
          decision by a human.
      - scope: Reflection changes derived from queued session evidence
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-evolution-queue
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-reflection-context
          note: Queued user/assistant summaries can shape retained instructions and correction/principle
            files.
        records:
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-evolution-queue
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        note: This classifies the wired derivation route, not the entire initial content of every file.
      - scope: Foreground-authored working-memory and append-note entries
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          note: The foreground agent can author durable notes.
        - value: trace-extracted
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          note: Prior work, preferences and discoveries can feed retained entries.
        records:
        - memory.md#mem-rte-foreground-notes
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        note: Instructions afford generation and editing; no generated instance was observed.
      - scope: Known initial working-memory and append-note seeds
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          note: Startup or Docker startup seeds named files from supplied baseline content.
        records:
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        note: Startup/bootstrap writes are separate from learned additions.
      - scope: Dense/sparse indexes on the inspected embedding/tokenization path
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-indexes
          - epistemic.md#epi-rte-fact-retention
          note: Embedding inference and deterministic tokenization derive access structures from payload
            text.
        records:
        - memory.md#mem-obj-retrieval-indexes
        - epistemic.md#epi-rte-fact-retention
        note: This does not resolve provenance of every preexisting stored vector.
      - scope: Web committed messages and translated event content
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-events
          - runtime.md#rt-rte-durable-chat
          note: The writer imports conversational content and SDK frames into host persistence.
        records:
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - runtime.md#rt-rte-durable-chat
        note: User/assistant content and SDK events enter host stores; host retention does not establish
          their original truth warrant.
      - scope: Durable code-derived chat run timelines
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-chat-timelines
          note: Translated run/tool events feed durable timeline summaries.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-chat-timelines
          note: Fixed code constructs summary_json from those events.
        records:
        - memory.md#mem-obj-chat-timelines
        note: These retain activity-derived summaries rather than model-learned rules.
      - scope: Evolution queue inputs, gate reasons and version/change metadata
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          note: Session summaries are admitted to the queue.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-evolution-log
          note: Version/status/count records are assembled by software.
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - memory.md#mem-obj-evolution-log
          note: Gate judgment and sentinel change summaries supply model-authored text.
        records:
        - memory.md#mem-obj-evolution-queue
        - memory.md#mem-obj-evolution-log
        - runtime.md#rt-rte-reflection-admission
        note: Source arrays are imported; code assembles control and version metadata, and the judge authors
          reasons.
      - scope: Foreground-authored persistent capability bodies
        assessment: known
        findings:
        - value: authored
          basis: afforded
          records:
          - runtime.md#rt-rte-channel-work
          - runtime.md#rt-rte-dynamic-tools
          - runtime.md#rt-rte-operator-config
          note: The foreground model can write persistent instructions or propose executable handler code.
        records:
        - runtime.md#rt-rte-channel-work
        - runtime.md#rt-rte-dynamic-tools
        - runtime.md#rt-rte-operator-config
        note: Model authorship is distinct from unresolved external caller provenance.
      - scope: Model-authored scheduled task handoff
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - workflow.md#wf-rte-job-creation
          - workflow.md#wf-obj-scheduled-job
          note: The main agent supplies self-contained task text to the scheduler tool.
        records:
        - workflow.md#wf-rte-job-creation
        - workflow.md#wf-obj-scheduled-job
        note: The supplied workflow establishes agent proposal and durable creation, not successful execution.
      - scope: Initial episode/fact/procedure contents and historical embedding provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-obj-retrieval-indexes
        note: The known extraction path does not resolve preexisting payloads, procedure authorship or
          embedding model versions.
      - scope: Initial evolved/reflection files, arbitrary user Markdown and externally supplied extension/handler
          content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        - memory.md#mem-obj-user-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-obj-dynamic-tools
        note: The records establish edit/import surfaces but not the original derivation of every supplied
          body. Foreground model authorship is separately afforded by the runtime. No single lineage covers
          all caller-supplied content.
      - scope: Optional memory/session-log.jsonl production and population
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-reflection-context
        note: Teaching-prompt mention does not establish an active production writer or complete historical
          lineage.
      - scope: SDK retained history and compaction output derivation
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: Host counters and artifact summaries do not expose the provider raw-to-summary path.
      records:
      - memory.md#mem-rte-vector-extraction
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-obj-evolution-queue
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-rte-foreground-notes
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-retrieval-indexes
      - epistemic.md#epi-rte-fact-retention
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-obj-chat-events
      - runtime.md#rt-rte-durable-chat
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-obj-evolution-log
      - runtime.md#rt-rte-channel-work
      - runtime.md#rt-rte-dynamic-tools
      - runtime.md#rt-rte-operator-config
      - workflow.md#wf-rte-job-creation
      - workflow.md#wf-obj-scheduled-job
      - memory.md#mem-obj-procedures
      - memory.md#mem-obj-user-memory
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-rte-chat-context
      note: Known subsequent derivation paths coexist with unresolved initial vector/procedure admission,
        historical embedding versions, optional session-log population, arbitrary caller provenance and
        SDK summaries.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Vector prose and suggested steps at the foreground model/tool-result consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          - memory.md#mem-obj-procedures
          - memory.md#mem-rte-vector-context
          - memory.md#mem-rte-memory-tools
          note: Facts, episodes and procedure actions supply contextual information to the answering agent.
        records:
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-rte-vector-context
        - memory.md#mem-rte-memory-tools
        note: Advice/evidence delivery is wired; compliance and improved action are unobserved.
      - scope: Retained vector content, embeddings and episode salience metadata at retrieval/reranking
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-indexes
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          - memory.md#mem-obj-procedures
          - memory.md#mem-rte-vector-context
          note: Text-derived access vectors, episode importance/age/access fields and procedure similarity
            determine relative retrieval priority.
        records:
        - memory.md#mem-obj-retrieval-indexes
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-rte-vector-context
        note: Fixed scoring code does not remove the ranking force of retained inputs.
      - scope: Fact validity state at default recall and conflict selection
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-semantic-facts
          - epistemic.md#epi-rte-validity-change
          - epistemic.md#epi-rte-similarity-check
          note: Non-null valid_until excludes a fact from default recall and active conflict candidates.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-semantic-facts
          - epistemic.md#epi-rte-validity-change
          note: Validity state selects the current-eligible set rather than globally erasing old content.
        records:
        - memory.md#mem-obj-semantic-facts
        - epistemic.md#epi-rte-validity-change
        - epistemic.md#epi-rte-similarity-check
        note: Temporal recall can bypass the default expiry exclusion.
      - scope: Evolved persona/profile/strategy prose at later foreground prompt consumer
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          - runtime.md#rt-rte-reflection-admission
          note: Retained style, preferences and strategies supply standing behavioral guidance.
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          note: Retained domain knowledge and user facts supply context/reference.
        records:
        - memory.md#mem-obj-evolved-files
        - runtime.md#rt-rte-reflection-admission
        note: The fixed loader and more-than-one-content-line formatter condition bound delivery.
      - scope: Queued messages, current reflection files and notes at reflection-update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-reflection-context
          note: Retained session evidence and current rules feed durable instruction revision.
        - value: learning
          basis: afforded
          records:
          - memory.md#mem-obj-agent-notes
          - memory.md#mem-obj-reflection-context
          note: Later reflection can read append notes and reflection-only rules to shape subsequent updates.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-reflection-context
          - memory.md#mem-obj-agent-notes
          note: Corrections and principles can provide reference content during reflection.
        records:
        - memory.md#mem-obj-evolution-queue
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-reflection-context
        - memory.md#mem-obj-agent-notes
        note: Learning authority denotes an update input, not demonstrated improved capacity.
      - scope: Working-memory projection at foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-working-memory
          note: Projected facts supply contextual information.
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-working-memory
          note: Retained preferences/corrections and trust framing guide later work.
        records:
        - memory.md#mem-obj-working-memory
        - memory.md#mem-rte-foreground-notes
        note: The host explicitly asks the model to trust the selected notes; this is not enforcement.
      - scope: Append notes read through foreground tools
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-agent-notes
          - memory.md#mem-rte-foreground-notes
          note: Requested file reads can supply durable preferences/discoveries as reference.
        records:
        - memory.md#mem-obj-agent-notes
        - memory.md#mem-rte-foreground-notes
        note: These notes are deliberately excluded from automatic injection.
      - scope: Queue key/age/retry/poison state at batching and rejection consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          note: Session keys, age and retry disposition select and order future batches.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          note: Poison disposition removes repeatedly invariant-failing inputs from ordinary draining.
        records:
        - memory.md#mem-obj-evolution-queue
        note: Control fields differ from the natural-language evidence they gate.
      - scope: SDK-ID and timestamp rows at session-resume consumer
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-session-store
          - runtime.md#rt-rte-channel-work
          note: Key lookup, expiry and stored SDK ID select whether/which conversation to resume.
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-channel-work
        note: This is authority of the host selector, not of opaque transcript contents.
      - scope: Chat transcript and host event/timeline artifacts at recovery and continuity consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          - memory.md#mem-rte-transcript-recovery
          - runtime.md#rt-rte-chat-context
          note: Earlier text and artifact/checkpoint facts provide context to later queries.
        records:
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        - memory.md#mem-rte-transcript-recovery
        - runtime.md#rt-rte-chat-context
        note: Checkpoint counters do not become hidden standing instructions.
      - scope: Chat session/sequence/status metadata at bound transcript access and continuity selector
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-transcript-recovery
          - memory.md#mem-obj-chat-transcript
          note: Session-bound lookup and soft-deletion state restrict delivered transcript content.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-chat-context
          - memory.md#mem-rte-transcript-recovery
          note: Session IDs, tool identities and sequence constraints select the source scope and retained
            parts.
        records:
        - memory.md#mem-rte-transcript-recovery
        - memory.md#mem-obj-chat-transcript
        - runtime.md#rt-rte-chat-context
        note: Access and selection consequences are distinct from prose advice.
      - scope: Evolution reason/change metadata at requesting MCP/dashboard reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-evolution-log
          - memory.md#mem-rte-memory-tools
          note: Requested changelog/config access supplies version/change information, not an automatic
            rationale for each instruction.
        records:
        - memory.md#mem-obj-evolution-log
        - memory.md#mem-rte-memory-tools
        note: Automatic evolved prompts omit these reasons.
      - scope: Dynamic handler identity/type/path at dispatch
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-dynamic-tools
          note: Names/type/path choose the operation and handler.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-dynamic-tools
        note: Dispatch fields select executable operations; executable force alone is not the controlled
          enforcement value.
      - scope: Arbitrary retained handler code at OS execution
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-handler-execution
        - runtime.md#rt-rte-dynamic-tools
        note: The records establish executable force under process rights, but not whether each body has
          a controlled instruction, knowledge, enforcement, validation or other listed effect. Execution
          alone is not a permit/refuse mechanism.
      - scope: Retained dynamic descriptions at model tool selection
        assessment: known
        findings:
        - value: routing
          basis: afforded
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-dynamic-tools
          note: Natural-language descriptions guide the model in selecting a registered operation.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-dynamic-tools
        note: This is selection guidance, not observed choice or an enforced route.
      - scope: Changed skill/subagent prose at requested SDK settings consumption
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records:
          - runtime.md#rt-rte-operator-config
          note: Edited Markdown bodies can supply standing agent/subagent instructions.
        records:
        - runtime.md#rt-rte-operator-config
        note: Host settings exposure is wired; exact dependency loading/activation remains uninspected.
      - scope: Scheduled task and dispatch policy at timer and later runtime
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: The later main-agent query receives the retained task as its instruction.
        - value: routing
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: Schedule, enabled/status fields and delivery target select execution time and destination.
        - value: enforcement
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: Paused/terminal state excludes future ordinary dispatch.
        records:
        - workflow.md#wf-obj-scheduled-job
        - workflow.md#wf-rte-job-creation
        - runtime.md#rt-rte-direct-work
        note: Run classification/delivery are not task correctness acceptance.
      - scope: User-scope Markdown at dashboard reader and optional foreground file reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-user-memory
          - memory.md#mem-rte-operator-memory
          note: Dashboard read requests supply the retained file as information to a client.
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-obj-user-memory
          note: Generic agent filesystem reading can supply the retained file as reference.
        records:
        - memory.md#mem-obj-user-memory
        - memory.md#mem-rte-operator-memory
        note: These reader paths do not establish arbitrary SDK automatic injection.
      - scope: Arbitrary user-scope Markdown at automatic SDK consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-user-memory
        note: SDK project/user settings exposure does not establish automatic consumption of every file
          or its downstream force.
      - scope: Changed plugin/hook/YAML controls and SDK retained payload effects
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: Settings exposure does not establish all dependency-specific consumers or effects; opaque
          history may include instructions, tools and summaries.
      records:
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-procedures
      - memory.md#mem-rte-vector-context
      - memory.md#mem-rte-memory-tools
      - memory.md#mem-obj-retrieval-indexes
      - epistemic.md#epi-rte-validity-change
      - epistemic.md#epi-rte-similarity-check
      - memory.md#mem-obj-evolved-files
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-obj-evolution-queue
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-working-memory
      - memory.md#mem-rte-foreground-notes
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-rte-channel-work
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-rte-transcript-recovery
      - runtime.md#rt-rte-chat-context
      - memory.md#mem-obj-evolution-log
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-rte-dynamic-tools
      - runtime.md#rt-bap-handler-execution
      - runtime.md#rt-rte-operator-config
      - workflow.md#wf-obj-scheduled-job
      - workflow.md#wf-rte-job-creation
      - runtime.md#rt-rte-direct-work
      - memory.md#mem-obj-user-memory
      - memory.md#mem-rte-operator-memory
      note: Authority follows each actual consumer, not the prompt container or write agency. Retained
        evidence can shape reflection while its output gives later instruction/knowledge. Arbitrary Markdown,
        dependency settings effects and SDK payload authority remain unresolved; static check code/constitution
        are excluded from accumulated memory.
    write_agency:
      assessment: partial
      units:
      - scope: Channel episode/fact extraction and subsequent index/store updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-vector-extraction
          - epistemic.md#epi-rte-fact-retention
          - memory.md#mem-obj-retrieval-indexes
          - epistemic.md#epi-rte-validity-change
          note: Software extracts, embeds, admits and expires payloads.
        records:
        - memory.md#mem-rte-vector-extraction
        - epistemic.md#epi-rte-fact-retention
        - memory.md#mem-obj-retrieval-indexes
        - epistemic.md#epi-rte-validity-change
        note: No per-fact approval is required.
      - scope: Reflection queue admission, model edits and branch-limited software acceptance
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-evolution-queue
          note: Gate/cadence/model/software decide admission without a per-content human decision.
        records:
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-evolution-queue
        note: User corrections are evidence rather than per-edit approval.
      - scope: Foreground note admission and ordinary model file/capability edits
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - runtime.md#rt-rte-channel-work
          note: Model-selected notes/files can persist without compulsory human approval.
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-dynamic-tools
          note: The in-process registration route admits shape-valid agent definitions without per-definition
            human review.
        records:
        - memory.md#mem-rte-foreground-notes
        - runtime.md#rt-rte-channel-work
        - runtime.md#rt-rte-dynamic-tools
        note: Foreground persistence is distinct from reflection admission.
      - scope: Startup note seeding, host chat persistence/timeline construction, logs and session bookkeeping
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          - runtime.md#rt-rte-durable-chat
          - memory.md#mem-obj-chat-timelines
          - memory.md#mem-obj-evolution-log
          - runtime.md#rt-obj-session-store
          note: Startup/runtime code admits seeds, messages/events, derived timelines and control metadata.
        records:
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        - runtime.md#rt-rte-durable-chat
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        - memory.md#mem-obj-evolution-log
        - runtime.md#rt-obj-session-store
        note: 'Physical I/O is not the criterion: these are software-selected admissions.'
      - scope: Scheduled job creation by foreground model
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - workflow.md#wf-rte-job-creation
          note: Model supplies a proposed job and software admits it against shape/schedule criteria.
        records:
        - workflow.md#wf-rte-job-creation
        note: An initiating request is not approval of the resulting task body.
      - scope: Dashboard memory Markdown edits/vector deletion and external extension/dynamic-tool admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-operator-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-rte-dynamic-tools
        note: The authenticated caller could be human or software. No record establishes the human decision
          required for manual classification on every such request.
      - scope: Initial vector/procedure and evolved-file admission; optional historical session log
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-procedures
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        - memory.md#mem-obj-retrieval-indexes
        note: Subsequent known transformations do not resolve initial control or an unestablished writer.
      - scope: Dependency-owned SDK conversation persistence and compaction admission
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: The wrapper requests persistence, but does not expose internal content selection/admission
          or checkpoint replacement.
      records:
      - memory.md#mem-rte-vector-extraction
      - epistemic.md#epi-rte-fact-retention
      - memory.md#mem-obj-retrieval-indexes
      - epistemic.md#epi-rte-validity-change
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-obj-evolution-queue
      - memory.md#mem-rte-foreground-notes
      - runtime.md#rt-rte-channel-work
      - runtime.md#rt-rte-dynamic-tools
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - runtime.md#rt-rte-durable-chat
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-obj-evolution-log
      - runtime.md#rt-obj-session-store
      - workflow.md#wf-rte-job-creation
      - memory.md#mem-rte-operator-memory
      - runtime.md#rt-rte-operator-config
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-procedures
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - runtime.md#rt-rte-chat-context
      note: Software/model admission is automatic even when a user starts work or authors source messages.
        Authenticated caller identity does not establish a per-content human decision. Initial procedure/vector
        admission and SDK writes remain unresolved; no manual value is inferred from dashboard labels.
    curation_operations:
      assessment: partial
      units:
      - scope: Heuristic episode/fact extraction from channel messages
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-vector-extraction
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          note: User traces are reduced to first-message episode summaries and selected/truncated fact
            statements.
        records:
        - memory.md#mem-rte-vector-extraction
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        note: Extraction compresses selected existing statements, even though field assignment may lose
          scope.
      - scope: Confidence-driven validity withdrawal of older semantic facts
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-semantic-facts
          - epistemic.md#epi-rte-validity-change
          note: Greater/equal incoming confidence dates out selected older payloads from default recall.
        records:
        - memory.md#mem-obj-semantic-facts
        - epistemic.md#epi-rte-validity-change
        note: History remains stored; this is not a checked logical contradiction decision.
      - scope: Episode retention ranking and availability
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-episodes
          - memory.md#mem-rte-vector-context
          note: Age/durability rules downweight or omit older episodic material.
        records:
        - memory.md#mem-obj-episodes
        - memory.md#mem-rte-vector-context
        note: Age/access metadata changes ranking rather than proving physical deletion.
      - scope: Requested reflection maintenance of retained instruction files
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-evolved-files
          note: Reflection is asked to compact existing file content.
        - value: dedup
          basis: afforded
          records:
          - runtime.md#rt-rte-reflection-admission
          note: Teaching guidance requests duplicate merging.
        - value: evolve
          basis: afforded
          records:
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-reflection-context
          note: Permitted edits can revise current rules/preferences.
        - value: promote
          basis: afforded
          records:
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-reflection-context
          - memory.md#mem-obj-evolved-files
          note: Guidance permits moving durable content into selected higher-salience files.
        - value: decay
          basis: afforded
          records:
          - runtime.md#rt-rte-reflection-admission
          note: Teaching guidance requests removal of obsolete entries.
        records:
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        note: The implemented prompt/tools afford these operations; no particular successful rewrite or
          semantic novelty is observed.
      - scope: Requested foreground working-memory maintenance
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          note: Agent guidance requests summarization near the line bound.
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          note: Agent may revise current preferences and corrections.
        - value: decay
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          note: Guidance requests removal of obsolete/already-adopted facts.
        records:
        - memory.md#mem-rte-foreground-notes
        - memory.md#mem-obj-working-memory
        note: Formatter clipping alone is a projection, not an on-disk rewrite.
      - scope: Durable event-to-timeline reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-chat-timelines
          note: Code reduces translated activity into durable run/tool/artifact summaries.
        records:
        - memory.md#mem-obj-chat-timelines
        - memory.md#mem-obj-chat-events
        note: A deterministic retained activity summary qualifies without model distillation.
      - scope: Chat event/session sweep
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-transcript
          - memory.md#mem-obj-chat-timelines
          note: Events expire after 24 hours; deleted sessions eventually lose retained transcript/timeline/attachment
            state.
        records:
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-transcript
        - memory.md#mem-obj-chat-timelines
        note: Expiry and hard deletion are not global erasure of derived memories.
      - scope: Caller-selected memory/extension/handler replacement and deletion
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-operator-memory
          - runtime.md#rt-rte-operator-config
          - runtime.md#rt-rte-dynamic-tools
          note: Existing Markdown/settings or definitions can be replaced.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-operator-memory
          - runtime.md#rt-rte-operator-config
          - runtime.md#rt-rte-dynamic-tools
          note: Deletion/unregistration removes selected retained material from later ordinary access.
        records:
        - memory.md#mem-rte-operator-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-rte-dynamic-tools
        note: Agency remains unresolved for external callers, independently of the implemented transformation.
      - scope: Initial/prospective procedure maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-procedures
        - memory.md#mem-abs-procedure-learning
        note: Store/outcome methods do not establish a shipped automatic trace-fed caller or an implemented
          semantic curation loop.
      - scope: Semantic novelty of reflection outputs and optional session-log maintenance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-reflection-context
        note: No output-level record establishes synthesis; requested inference and principle names do
          not settle the implemented transformation of every candidate.
      - scope: SDK conversation compaction and checkpoint maintenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: The provider algorithm and opaque retained summary were not inspected. Host compact-boundary
          events are not its output text.
      records:
      - memory.md#mem-rte-vector-extraction
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - epistemic.md#epi-rte-validity-change
      - memory.md#mem-rte-vector-context
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-rte-foreground-notes
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-transcript
      - memory.md#mem-rte-operator-memory
      - runtime.md#rt-rte-operator-config
      - runtime.md#rt-rte-dynamic-tools
      - memory.md#mem-obj-procedures
      - memory.md#mem-abs-procedure-learning
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-rte-chat-context
      note: Known code transformations, afforded model maintenance and unresolved semantic/SDK branches
        remain separate. Neither a consolidate method name nor index construction establishes semantic
        curation. No synthesis value is inferred from a principle label or a possible extraction error.
    read_back_direction:
      assessment: partial
      units:
      - scope: Automatic vector selection during channel/chat prompt building
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-vector-context
          note: Selected facts/episodes/procedure are supplied in appended prompt context.
        records:
        - memory.md#mem-rte-vector-context
        note: Foreground query triggers code selection without a memory-tool request.
      - scope: Fixed evolved snapshot loading and working-memory projection
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-working-memory
          - runtime.md#rt-rte-reflection-admission
          note: Prompt assembly supplies selected retained files/lines automatically.
        records:
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-working-memory
        - runtime.md#rt-rte-reflection-admission
        note: Only fixed evolved files passing formatting conditions are automatically delivered; notes/corrections
          are not silently included.
      - scope: Host chat artifact/checkpoint supplement
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-chat-context
          note: Code supplies selected artifact/checkpoint context on later chat invocations.
        records:
        - runtime.md#rt-rte-chat-context
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        note: Fresh host supplement replaces prior tagged context under Murph; it is not full transcript
          compaction.
      - scope: Requested vector/config/changelog resources and transcript search
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-memory-tools
          - memory.md#mem-rte-transcript-recovery
          - memory.md#mem-obj-evolution-log
          note: The agent/client requests prior retained material and receives the bounded result.
        records:
        - memory.md#mem-rte-memory-tools
        - memory.md#mem-rte-transcript-recovery
        - memory.md#mem-obj-evolution-log
        note: External resource exposure does not prove a deployed client.
      - scope: Requested direct note/current-file reads
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-agent-notes
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-reflection-context
          note: Foreground or reflection Read/Grep can request retained notes and current files.
        records:
        - memory.md#mem-obj-agent-notes
        - memory.md#mem-rte-foreground-notes
        - memory.md#mem-obj-reflection-context
        note: Agent notes remain outside automatic injection.
      - scope: Dashboard memory inspection
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-operator-memory
          - memory.md#mem-obj-user-memory
          note: Authenticated clients explicitly list/read retained payloads and Markdown.
        records:
        - memory.md#mem-rte-operator-memory
        - memory.md#mem-obj-user-memory
        note: This read route does not establish arbitrary SDK injection.
      - scope: Reflection batch delivery of queued evidence
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          note: Eligible queued inputs are supplied to reflection without a model retrieval request.
        records:
        - memory.md#mem-obj-evolution-queue
        - runtime.md#rt-rte-reflection-admission
        note: Cadence selects and stages retained summaries for the update invocation.
      - scope: Retained SDK-ID lookup for resumed foreground execution
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-session-store
          - runtime.md#rt-rte-channel-work
          - runtime.md#rt-rte-durable-chat
          note: Code selects the active matching session and supplies its SDK ID to query options.
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-channel-work
        - runtime.md#rt-rte-durable-chat
        note: This describes the host selection and requested resume, not complete SDK payload supply.
      - scope: Dynamic-definition reload and scheduled job dispatch
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-dynamic-tools
          note: New server construction automatically enumerates retained definitions.
        - value: push
          basis: wired
          records:
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: Due-job selection supplies stored task text to a later runtime invocation.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-dynamic-tools
        - workflow.md#wf-obj-scheduled-job
        - runtime.md#rt-rte-direct-work
        note: These are later consumption of retained capabilities and handoffs, not vector-memory retrieval.
      - scope: Arbitrary user Markdown, installed settings/skills/hooks and dependency conversation/summary
          delivery
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-user-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: The records do not resolve every actual dependency selection and delivery route. The known
          host resume-ID push does not establish complete SDK read-back coverage.
      records:
      - memory.md#mem-rte-vector-context
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-working-memory
      - runtime.md#rt-rte-reflection-admission
      - runtime.md#rt-rte-chat-context
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-rte-memory-tools
      - memory.md#mem-rte-transcript-recovery
      - memory.md#mem-obj-evolution-log
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-rte-foreground-notes
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-rte-operator-memory
      - memory.md#mem-obj-user-memory
      - memory.md#mem-obj-evolution-queue
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-rte-channel-work
      - runtime.md#rt-rte-durable-chat
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-rte-dynamic-tools
      - workflow.md#wf-obj-scheduled-job
      - runtime.md#rt-rte-direct-work
      - runtime.md#rt-rte-operator-config
      note: Both automatic supply and requested retrieval are established. Operations within each chain
        are distinguished; returning a requested tool/resource result is not a second push. SDK history
        selection is wired but its internal summary delivery and arbitrary settings consumption remain
        unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic vector query relevance selection
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-vector-context
          - memory.md#mem-obj-retrieval-indexes
          note: Dense query-to-retained-vector similarity selects prior content.
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-vector-context
          - memory.md#mem-obj-retrieval-indexes
          note: Hashed sparse query/text features contribute to episode hybrid retrieval.
        records:
        - memory.md#mem-rte-vector-context
        - memory.md#mem-obj-retrieval-indexes
        note: 'Trigger: foreground text. Inputs: text embeddings and sparse token features. Selected parts:
          episode/fact/procedure candidates.'
      - scope: Vector availability, validity, recency and prompt-budget filtering
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-vector-context
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          note: Non-targeted availability, durability and budget predicates further restrict delivery.
        records:
        - memory.md#mem-rte-vector-context
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        note: 'Trigger: prompt construction. Inputs: readiness, score/age/importance/access and estimated
          remaining budget. Selected parts: whole fact/procedure sections and bounded episodes.'
      - scope: Fixed evolved-file and working-memory projection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-working-memory
          - runtime.md#rt-rte-reflection-admission
          note: This is fixed inclusion/availability and line-bound selection, not a topical identifier
            match.
        records:
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-working-memory
        - runtime.md#rt-rte-reflection-admission
        note: 'Trigger: assembly/reload. Inputs: fixed file slots, nonempty/content-line conditions and
          line count. Selected parts: evolved sections and working-memory head/tail.'
      - scope: Chat artifact/checkpoint continuity selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-chat-context
          note: Session and supported tool identity matches select retained source rows/parts for delivery.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-chat-context
          note: Recent-tail, URL/path availability, deduplication and eight-artifact/three-checkpoint
            limits further filter the supplement.
        records:
        - runtime.md#rt-rte-chat-context
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        note: 'Trigger: later chat query. Inputs: current session ID and supported page-tool identities;
          event/timeline tails, parseability, filters and caps. Selected parts: matching artifacts and
          recent checkpoint metadata.'
      - scope: Evolution batch selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          note: Batch age/eligibility controls do not establish content-targeted retrieval.
        - value: inferred-judgment
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          note: The upstream gate model judges sampled session text for admission to the later delivered
            evidence queue; failures can also enqueue without that judgment.
        records:
        - memory.md#mem-obj-evolution-queue
        - runtime.md#rt-rte-reflection-admission
        note: 'Trigger: cadence drain. Inputs: queue age, eligibility/retries and batching. Selected parts:
          staged session summaries and gate reasons.'
      - scope: Runtime SDK session-ID selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-obj-session-store
          - runtime.md#rt-rte-channel-work
          - runtime.md#rt-rte-durable-chat
          note: An actual key match selects which retained SDK history is requested.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-obj-session-store
          note: Staleness/availability can clear the resume handle.
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-channel-work
        - runtime.md#rt-rte-durable-chat
        note: 'Trigger: foreground query. Input: channel/conversation key and expiry. Selected retained
          part: matching active SDK-history handle; payload is opaque.'
      - scope: Dynamic catalog enumeration and scheduled dispatch
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-obj-dynamic-tools
          - runtime.md#rt-rte-dynamic-tools
          - workflow.md#wf-obj-scheduled-job
          - runtime.md#rt-rte-direct-work
          note: Full-catalog exposure and time/status eligibility do not imply relevance inference.
        records:
        - runtime.md#rt-obj-dynamic-tools
        - runtime.md#rt-rte-dynamic-tools
        - workflow.md#wf-obj-scheduled-job
        - runtime.md#rt-rte-direct-work
        note: 'Trigger: server creation or scheduler tick. Inputs: catalog availability or due/enabled/status.
          Selected parts: retained definitions or due tasks.'
      - scope: SDK internal history/checkpoint selection and user/project extension selection
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        - memory.md#mem-obj-user-memory
        - runtime.md#rt-rte-operator-config
        note: Known host IDs and display summaries do not classify the hidden selector or selected payload.
      records:
      - memory.md#mem-rte-vector-context
      - memory.md#mem-obj-retrieval-indexes
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-working-memory
      - runtime.md#rt-rte-reflection-admission
      - runtime.md#rt-rte-chat-context
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - memory.md#mem-obj-evolution-queue
      - runtime.md#rt-obj-session-store
      - runtime.md#rt-rte-channel-work
      - runtime.md#rt-rte-durable-chat
      - runtime.md#rt-obj-dynamic-tools
      - runtime.md#rt-rte-dynamic-tools
      - workflow.md#wf-obj-scheduled-job
      - runtime.md#rt-rte-direct-work
      - memory.md#mem-obj-user-memory
      - runtime.md#rt-rte-operator-config
      note: Push signals are classified at actual selectors. Coarse readiness/budget/availability and
        targeted matches are separate findings. Requested lexical transcript and vector searches are pull
        operations and add no push-signal values. SDK/settings selectors remain unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic channel trace-to-episode/fact-to-later-model chain
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-vector-extraction
          - memory.md#mem-rte-vector-context
          - memory.md#mem-rte-memory-tools
          note: Recorded user session messages feed automatic extraction; stored results reach later prompt/tool
            consumers.
        records:
        - memory.md#mem-rte-vector-extraction
        - memory.md#mem-rte-vector-context
        - memory.md#mem-rte-memory-tools
        note: Durable contextual artifacts qualify without novel claims or measured benefit.
      - scope: Queued conversational evidence to evolved/reflection files to later consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          - memory.md#mem-obj-evolved-files
          - memory.md#mem-obj-reflection-context
          note: Trace-fed computational edits persist as durable guidance used by later invocations.
        records:
        - memory.md#mem-obj-evolution-queue
        - runtime.md#rt-rte-reflection-admission
        - memory.md#mem-obj-evolved-files
        - memory.md#mem-obj-reflection-context
        note: Fixed-loader files reach foreground prompts; other files can shape later reflection and
          require promotion for automatic foreground delivery.
      - scope: Foreground experience-fed note writing and later use
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          note: The model can retain prior work/preferences/discoveries into working memory or append
            notes, with later prompt/tool/reflection readers.
        records:
        - memory.md#mem-rte-foreground-notes
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        note: This remains an affordance, not an observed or deterministically scheduled note-writing
          episode.
      - scope: Translated chat events to durable timelines to later artifact context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          - runtime.md#rt-rte-chat-context
          note: Recorded run/tool activity feeds durable derived timelines whose page artifacts reach
            later model context.
        records:
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        - runtime.md#rt-rte-chat-context
        note: The generated summary qualifies through retention and later contextual supply, not merely
          browser display.
      - scope: Shipped automatic trace-to-procedure producer/outcome loop
        assessment: known
        findings:
        - value: 'no'
          basis: wired
          records:
          - memory.md#mem-abs-procedure-learning
          - memory.md#mem-obj-procedures
          note: Within the searched shipped producer boundary, consolidation returns zero procedures and
            public write/outcome methods have no established callers.
        records:
        - memory.md#mem-abs-procedure-learning
        - memory.md#mem-obj-procedures
        note: The bounded non-test source caller search establishes no shipped automatic procedure-learning
          chain; external/preexisting procedure admission is assessed separately.
      - scope: Initial/external procedure and vector writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-procedures
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-obj-retrieval-indexes
        note: Unresolved initial producers cannot inherit the local shipped-procedure no; their trace
          inputs and later behavior-shaping updates are not established.
      - scope: SDK compaction/checkpoint production and later consumption
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: Host compaction counters do not reveal whether or how an automatic retained summary reaches
          a later invocation.
      - scope: External memory/extension/handler edits, initial files and optional session-log population
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-operator-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-obj-dynamic-tools
        - memory.md#mem-obj-reflection-context
        note: Generic caller edits or a named log path do not establish the trace-fed durable-update chain.
      - scope: Scheduled handoff generation and direct executable capability creation
        assessment: not-determinable
        findings: []
        records:
        - workflow.md#wf-rte-job-creation
        - runtime.md#rt-rte-dynamic-tools
        - workflow.md#wf-obj-scheduled-job
        note: Automatic admission and later use are known, but records do not establish that the task/handler
          was extracted from recorded activity rather than an immediate open request. Neither yes nor
          no follows for all these writes.
      records:
      - memory.md#mem-rte-vector-extraction
      - memory.md#mem-rte-vector-context
      - memory.md#mem-rte-memory-tools
      - memory.md#mem-obj-evolution-queue
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-obj-evolved-files
      - memory.md#mem-obj-reflection-context
      - memory.md#mem-rte-foreground-notes
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - runtime.md#rt-rte-chat-context
      - memory.md#mem-abs-procedure-learning
      - memory.md#mem-obj-procedures
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-retrieval-indexes
      - runtime.md#rt-obj-session-store
      - memory.md#mem-rte-operator-memory
      - runtime.md#rt-rte-operator-config
      - runtime.md#rt-obj-dynamic-tools
      - workflow.md#wf-rte-job-creation
      - runtime.md#rt-rte-dynamic-tools
      - workflow.md#wf-obj-scheduled-job
      note: The profile uses the automatic trace-fed durable-artifact definition, not demonstrated improved
        capacity. Wired vector extraction, reflection and durable chat summaries qualify; raw retention
        alone does not. Local procedure absence does not become a system-wide no. Opaque SDK summaries,
        mixed foreground writes and initial state prevent complete coverage.
    trace_source:
      assessment: partial
      units:
      - scope: Channel episode/fact extraction input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-vector-extraction
          - memory.md#mem-obj-episodes
          - memory.md#mem-obj-semantic-facts
          note: Recorded user conversational turns feed the qualifying automatic extraction.
        records:
        - memory.md#mem-rte-vector-extraction
        - memory.md#mem-obj-episodes
        - memory.md#mem-obj-semantic-facts
        note: The heuristic actually consumes user messages plus metadata, not assistant reasoning.
      - scope: Queued reflection conversational input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-evolution-queue
          - runtime.md#rt-rte-reflection-admission
          note: Recorded conversational turns feed trace-driven file revision.
        records:
        - memory.md#mem-obj-evolution-queue
        - runtime.md#rt-rte-reflection-admission
        note: Channel summaries retain user/assistant arrays; tools are empty. Feedback arrays can be
          empty and reaction content is not fully supplied.
      - scope: Foreground experience-fed notes
        assessment: partial
        findings:
        - value: session-logs
          basis: afforded
          records:
          - memory.md#mem-rte-foreground-notes
          - memory.md#mem-obj-working-memory
          - memory.md#mem-obj-agent-notes
          note: Conversation-derived preferences and corrections can feed durable notes without per-entry
            approval.
        records:
        - memory.md#mem-rte-foreground-notes
        - memory.md#mem-obj-working-memory
        - memory.md#mem-obj-agent-notes
        note: Session preferences/corrections are a supported source; agent-discovered patterns can have
          additional origins not resolved by the records.
      - scope: Durable chat event-to-timeline-to-continuity chain
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          note: Translated runtime frames carry run status and event sequences into timeline construction.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-chat-events
          - memory.md#mem-obj-chat-timelines
          - runtime.md#rt-rte-chat-context
          note: Recorded tool requests/results and page-artifact summaries feed durable timelines and
            later artifact context.
        records:
        - memory.md#mem-obj-chat-events
        - memory.md#mem-obj-chat-timelines
        - runtime.md#rt-rte-chat-context
        note: Unlike session messages merely wrapped as events, these inputs include discrete SDK/runtime
          events and recorded tool activity.
      - scope: Bounded shipped automatic procedure producer
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-abs-procedure-learning
        - memory.md#mem-obj-procedures
        note: No qualifying shipped trace-fed producer is established in the bounded caller search, so
          there is no original learning input to classify on that route.
      - scope: Initial/external vector/procedure and file/capability updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-procedures
        - memory.md#mem-obj-semantic-facts
        - memory.md#mem-rte-operator-memory
        - runtime.md#rt-rte-operator-config
        - runtime.md#rt-rte-dynamic-tools
        - memory.md#mem-obj-reflection-context
        note: Original input to any qualifying update is unresolved; imported static instructions alone
          establish no trace source.
      - scope: SDK compaction/checkpoint update inputs
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-session-store
        - runtime.md#rt-rte-chat-context
        note: The provider raw input and compaction algorithm are uninspected; host display counters do
          not classify hidden source content.
      - scope: Scheduled task and dynamic handler source derivation
        assessment: not-determinable
        findings: []
        records:
        - workflow.md#wf-rte-job-creation
        - workflow.md#wf-obj-scheduled-job
        - runtime.md#rt-rte-dynamic-tools
        note: The records establish open-request admission but not a qualifying recorded-activity input;
          no event-stream/session-log value is inferred from a later execution key.
      records:
      - memory.md#mem-rte-vector-extraction
      - memory.md#mem-obj-episodes
      - memory.md#mem-obj-semantic-facts
      - memory.md#mem-obj-evolution-queue
      - runtime.md#rt-rte-reflection-admission
      - memory.md#mem-rte-foreground-notes
      - memory.md#mem-obj-working-memory
      - memory.md#mem-obj-agent-notes
      - memory.md#mem-obj-chat-events
      - memory.md#mem-obj-chat-timelines
      - runtime.md#rt-rte-chat-context
      - memory.md#mem-abs-procedure-learning
      - memory.md#mem-obj-procedures
      - memory.md#mem-rte-operator-memory
      - runtime.md#rt-rte-operator-config
      - runtime.md#rt-rte-dynamic-tools
      - memory.md#mem-obj-reflection-context
      - runtime.md#rt-obj-session-store
      - workflow.md#wf-rte-job-creation
      - workflow.md#wf-obj-scheduled-job
      note: Sources are original activity content, not adapter names. Session extraction and reflection
        use conversational logs, not a tool transcript merely because file-path metadata is present. Chat
        timeline production uses actual runtime events/tool results. Mixed foreground and opaque/external
        branches prevent a complete source union.
---

# Phantom memory profile

## Comparison rationale

The comparison classifies accepted records, not a newly inspected source. All
positive findings describe wiring or affordances; no supplied observed run or
causal experiment establishes activation or benefit. Axis coverage is partial
because the included inventory retains SDK-owned conversation/compaction state,
unknown initial producers and caller-dependent branches alongside known host
mechanisms. A local known unit is complete only for its named path and parts.

### Derivation and canonical identity

The reconciliation supersedes the epistemic episode, fact and procedure objects
with [MEM-OBJ-episodes](memory.md#mem-obj-episodes),
[MEM-OBJ-semantic-facts](memory.md#mem-obj-semantic-facts) and
[MEM-OBJ-procedures](memory.md#mem-obj-procedures), and the epistemic extraction
route with [MEM-RTE-vector-extraction](memory.md#mem-rte-vector-extraction).
Those canonical declarations supply the classifications. The separate epistemic
retention, similarity and validity stages remain distinct; none is superseded
by extraction. In particular,
[EPI-RTE-validity-change](epistemic.md#epi-rte-validity-change) establishes
withdrawal from default recall, not truth acceptance or universal erasure.

Compaction is a change action under ok, not a separate accepted status.
[RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) therefore
supports changed-ok refresh for admitted compactions. It does not imply delivery
of every admitted file: [MEM-OBJ-evolved-files](memory.md#mem-obj-evolved-files)
and [MEM-OBJ-reflection-context](memory.md#mem-obj-reflection-context) distinguish
fixed-loader/formatter delivery from reflection-only material requiring
promotion. Reconciliation's residual conflict concerns memory's stale attribution
of earlier runtime claims, not these current mechanisms. This profile neither
reopens verification nor treats those requested corrections as outstanding.

### Independent forms, forces and evidence layers

Dense access vectors are parametric representations in a vector substrate;
sparse token features are symbolic. Neither is a Phantom weight-update route.
[MEM-OBJ-retrieval-indexes](memory.md#mem-obj-retrieval-indexes) leaves historical
embedding provenance unresolved. File prose, control metadata and binary
attachments are likewise separate units: a display description cannot classify
an opaque payload.

Retained text and access features can rank retrieval even with fixed scoring
code. Fact validity can enforce exclusion; session/queue/job metadata can route
later work. At reflection's update consumer, queued experience has learning
force, while selected output files provide instruction or knowledge at the
foreground model. These are separate paths, not an implication from the
trace-learning label. The relevant routes are
[MEM-RTE-vector-context](memory.md#mem-rte-vector-context),
[RT-RTE-reflection-admission](runtime.md#rt-rte-reflection-admission) and
[WF-RTE-job-creation](workflow.md#wf-rte-job-creation).

Known automatic admission never implies manual approval merely because the
operator initiated work. Conversely, the authenticated caller on
[MEM-RTE-operator-memory](memory.md#mem-rte-operator-memory) and
[RT-RTE-operator-config](runtime.md#rt-rte-operator-config) does not establish
human control of each body. Reflection/foreground consolidation, deduplication
and promotion remain afforded where the records establish model guidance and
tools rather than a particular performed transformation. A principle label,
inferred preference or faithfulness defect does not establish synthesis.

### Read-back and qualifying trace routes

Automatic vector selection and host continuity are push; requested memory tools,
transcript search and file reads are pull. A requested lexical search adds no
push lexical signal. Fixed-file inclusion is coarse, not identifier targeting
merely because a filename exists. Session/tool identity matching in
[RT-RTE-chat-context](runtime.md#rt-rte-chat-context) does select retained parts;
its caps and availability filters remain coarse. The evolution gate's
content-sensitive judgment is an upstream selection into retained evidence for
later reflection, independently of cadence's coarse batching and its fail-open
admission alternative.

Automatic extraction and durable event-derived timeline summaries qualify as
trace learning when their retained outputs reach later context, even without a
novel claim or measured benefit. Raw chat persistence alone is not that update.
[MEM-OBJ-chat-timelines](memory.md#mem-obj-chat-timelines) and
[RT-RTE-chat-context](runtime.md#rt-rte-chat-context) close the derived-summary
and later-consumer path; compact-boundary counters do not close the opaque SDK
summary path. The local procedure no is bounded by
[MEM-ABS-procedure-learning](memory.md#mem-abs-procedure-learning), not extended
to initial/external procedures or the whole system. Original conversational
turns remain session logs even when staged as JSONL. Actual translated runtime
and tool events feeding timelines support event-streams and tool-traces. No
record establishes linked state/action/outcome trajectories as an additional
qualifying source.

### Source-read log

No frozen-source files were read for this classification. Only the supplied
contracts, boundary and accepted members were read; all warrants stay in their
canonical records. No new evidence or analyst records are declared here.
