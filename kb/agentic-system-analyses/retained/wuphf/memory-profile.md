---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Wuphf memory profile: scoped notes, wiki/learning derivation, retrieval and saved-tool reuse
  with unresolved remote and recovery alternatives.'
run-id: AAS-2026-10-15-wuphf-b246722f99c0-01
source-identity: https://github.com/nex-crm/wuphf
reviewed-boundary: 88023d4dac7491b6e71dbc1e86d274c435b9cb2c
memory-comparison:
  version: 2
  scope: Use-accumulated private/shared notes, learning records, raw artifacts and derived facts/articles,
    embedding cache and retrieval metadata, compiled skill/registry state, saved executable tools, routine
    transcripts/artifacts and retained task outcomes/verification. Includes unresolved remote corpus/index/provider
    state, opaque native-session entries, skill/scanner/admission alternatives, app-state consumers and
    separate durable checkpoint/resume alternatives. Current-state snapshot helpers are assessed only
    as an unresolved retention alternative. Excludes shipped static prompts, transient invocation frames,
    uncaptured workspace contents and external-provider implementation claims; inference weights alone
    are not use-accumulated memory.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Private note map and persisted broker-state encoding
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-private-memory-note
          note: Broker sharedMemory map holds current notes.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-private-memory-note
          note: Broker state save/load retains the map across invocations.
        records:
        - memory.md#mem-obj-private-memory-note
        note: Both live and persisted parts are identified; JSON is encoding, not an additional substrate.
      - scope: GBrain shared page and remote retrieval index
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-rte-memory-brief
        note: Adapter identifies remote pages and queries, but does not establish the remote storage implementation.
          A service endpoint alone does not establish a service-object substrate.
      - scope: Learning log, source artifacts, fact logs, entity articles and compiled skill files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-learning-record
          - memory.md#mem-obj-typed-fact
          - epistemic.md#epi-obj-entity-brief
          - memory.md#mem-obj-compiled-skill
          note: JSONL and Markdown retain these operative parts.
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-learning-record
          - memory.md#mem-obj-typed-fact
          - epistemic.md#epi-obj-entity-brief
          - memory.md#mem-obj-compiled-skill
          note: WikiWorker retains these wiki materials in Git.
        records:
        - memory.md#mem-obj-learning-record
        - memory.md#mem-obj-typed-fact
        - epistemic.md#epi-obj-entity-brief
        - memory.md#mem-obj-compiled-skill
        note: File and repository retention coexist; article narrative has its own object record.
      - scope: Live derived fact/index state
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-typed-fact
          note: Derived store/text index includes live retained facts.
        records:
        - memory.md#mem-obj-typed-fact
        note: Classifies the inspected live part, not every backing index implementation.
      - scope: Cached dense text embeddings
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-cmp-retrieval-embedding
          note: Embedding cache retains numerical vectors in JSONL.
        records:
        - memory.md#mem-cmp-retrieval-embedding
        note: Cache encoding is documented independently of provider inference; no dedicated vector database
          is established.
      - scope: Saved tool code and metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-stored-tool
          note: Per-agent JSON files are reloaded for subsequent tool execution.
        records:
        - runtime.md#rt-obj-stored-tool
        note: Version counters do not establish retained prior code bodies.
      - scope: Routine transcript trees
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          note: Session adapter retains per-agent JSONL session trees.
        records:
        - memory.md#mem-obj-session-transcript
        note: Only the wrapper-visible representation is characterized; native dependency internals remain
          opaque.
      - scope: Separate durable session checkpoint and app-state/version internals
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-memory-snapshot
        - runtime.md#rt-rte-app-publication
        note: Snapshot structs are a current-state projection, not established retained checkpoint storage;
          app-store internals and retention details were not traced.
      - scope: Provider-owned embedding state and additional registry/index persistence details
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-cmp-retrieval-embedding
        - memory.md#mem-rte-skill-registration
        note: Provider initialization and registry backing details are not fully characterized. Static
          inference weights are not claimed as use-accumulated memory.
      records:
      - memory.md#mem-obj-private-memory-note
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-rte-memory-brief
      - memory.md#mem-obj-learning-record
      - memory.md#mem-obj-typed-fact
      - epistemic.md#epi-obj-entity-brief
      - memory.md#mem-obj-compiled-skill
      - memory.md#mem-cmp-retrieval-embedding
      - runtime.md#rt-obj-stored-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-obj-session-memory-snapshot
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-rte-skill-registration
      note: Positive file, repository and live-index witnesses do not resolve remote pages, provider state,
        checkpoints or app/registry internals; the included memory boundary is not a complete storage
        census.
    representational_form:
      assessment: partial
      units:
      - scope: Note bodies, learning insights, artifact/fact text and entity article narratives consumed
          as reference
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-private-memory-note
          - memory.md#mem-obj-shared-memory-write
          - memory.md#mem-obj-learning-record
          - memory.md#mem-obj-typed-fact
          - epistemic.md#epi-obj-entity-brief
          note: Text requires interpretation by search callers, humans or office models.
        records:
        - memory.md#mem-obj-private-memory-note
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-obj-learning-record
        - memory.md#mem-obj-typed-fact
        - epistemic.md#epi-obj-entity-brief
        note: Known readable content is separated from remote index and provider representations.
      - scope: Local identity, provenance, confidence, trust, validity and archive metadata at fixed-rule
          consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-learning-record
          - memory.md#mem-obj-typed-fact
          - memory.md#mem-rte-wiki-maintenance
          - epistemic.md#epi-rte-lint-disposal
          note: Fixed rules interpret keys, scores, timestamps, relation IDs and archived/validity fields.
        records:
        - memory.md#mem-obj-learning-record
        - memory.md#mem-obj-typed-fact
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-lint-disposal
        note: These fields differ from the natural-language assertions they organize.
      - scope: Dense cache vectors at cosine/fused retrieval
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-cmp-retrieval-embedding
          note: Dense numerical text representations influence semantic ranking.
        records:
        - memory.md#mem-cmp-retrieval-embedding
        note: Distributed numerical representation is not the cache JSON serialization.
      - scope: Compiled procedural wrapper/body
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-compiled-skill
          - epistemic.md#epi-rte-playbook-compile
          note: Procedure text and wrapper directions are intended for model interpretation.
        records:
        - memory.md#mem-obj-compiled-skill
        - epistemic.md#epi-rte-playbook-compile
        note: Actual later assignment/loading remains unresolved; form does not imply activation.
      - scope: Skill registry status, ownership and rejection identity
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-compiled-skill
          - memory.md#mem-rte-skill-registration
          note: Registration and tombstone checks use localized status and identity fields.
        records:
        - memory.md#mem-obj-compiled-skill
        - memory.md#mem-rte-skill-registration
        note: Separate from procedural text.
      - scope: Saved tool code and input declaration at worker
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-stored-tool
          - runtime.md#rt-bap-tool-execution
          note: JavaScript fixes executable steps and arguments.
        records:
        - runtime.md#rt-obj-stored-tool
        - runtime.md#rt-bap-tool-execution
        note: Title/purpose prose is classified separately from executed bytes.
      - scope: Saved tool title/purpose at matching and presentation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-stored-tool
          - runtime.md#rt-rte-scheduled-tool
          note: Readable metadata supplies lexical matching and display text.
        records:
        - runtime.md#rt-obj-stored-tool
        - runtime.md#rt-rte-scheduled-tool
        note: Fixed lexical matching does not make prose executable code.
      - scope: Routine transcript display messages
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          note: User prompt and tool-runner outcome text are the exposed messages.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          note: Message type/role and session identity govern the projection.
        records:
        - memory.md#mem-obj-session-transcript
        note: Known projected messages do not characterize every native session entry or opaque payload.
      - scope: Remote index, opaque native session entries, app bytes/state and durable checkpoint alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-cmp-retrieval-embedding
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-obj-session-memory-snapshot
        - runtime.md#rt-rte-app-publication
        note: Readable summaries and known cache vectors do not resolve opaque payloads or all app-state
          representations.
      records:
      - memory.md#mem-obj-private-memory-note
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-obj-learning-record
      - memory.md#mem-obj-typed-fact
      - epistemic.md#epi-obj-entity-brief
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-rte-lint-disposal
      - memory.md#mem-cmp-retrieval-embedding
      - memory.md#mem-obj-compiled-skill
      - epistemic.md#epi-rte-playbook-compile
      - memory.md#mem-rte-skill-registration
      - runtime.md#rt-obj-stored-tool
      - runtime.md#rt-bap-tool-execution
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-obj-session-memory-snapshot
      - runtime.md#rt-rte-app-publication
      note: Text, metadata, code and dense representations have separate consumption paths. Opaque remote/native/app/checkpoint
        alternatives prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Explicit private and shared note content at caller supply
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-private-memory-note
          - memory.md#mem-obj-shared-memory-write
          note: Caller supplies note text; this says nothing about human admission control.
        records:
        - memory.md#mem-obj-private-memory-note
        - memory.md#mem-obj-shared-memory-write
        note: External initial corpus provenance is not inferred from this known write path.
      - scope: Private-to-shared copy
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-rte-scoped-notes
          - memory.md#mem-obj-shared-memory-write
          note: Promotion copies the retained private content into a separately persisted shared page.
        records:
        - memory.md#mem-rte-scoped-notes
        - memory.md#mem-obj-shared-memory-write
        note: Known copy lineage does not resolve all preexisting GBrain pages.
      - scope: Explicit learning insight admission
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-learning-record
          - memory.md#mem-rte-learning-admission
          note: Explicit caller supplies insight content.
        records:
        - memory.md#mem-obj-learning-record
        - memory.md#mem-rte-learning-admission
        note: Source labels and trust flags do not authenticate the original author.
      - scope: Completed-task-derived learning and entity material
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          note: Task outcomes and verification feedback feed durable learning and entity/article capture.
        records:
        - memory.md#mem-rte-task-distillation
        note: Known task derivation is distinct from full provenance of task title/details and verification
          specs.
      - scope: Artifact-derived facts and brief rewrites
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-artifact-extraction
          - memory.md#mem-rte-brief-synthesis
          note: Provider extraction and fact/brief rewriting transform retained inputs into derived knowledge.
        records:
        - memory.md#mem-rte-artifact-extraction
        - memory.md#mem-rte-brief-synthesis
        note: This identifies the derivation path without asserting that every artifact originates in
          a trace.
      - scope: Playbook-to-skill wrapper
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-rte-playbook-compile
          note: Deterministic compiler emits a wrapper from current playbook source.
        records:
        - epistemic.md#epi-rte-playbook-compile
        note: Initial human/draft/scanner provenance is not resolved by wrapper compilation.
      - scope: Saved tools admitted from model or deterministic fallback
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          - runtime.md#rt-rte-scheduled-tool
          note: Model or fallback constructs code that is software-admitted for later execution.
        records:
        - runtime.md#rt-rte-tool-authoring
        - runtime.md#rt-rte-scheduled-tool
        note: Model-authored code is not inferred to be extracted from previous routine transcripts.
      - scope: Smoke-feedback-directed tool repair
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          note: Recorded simulated execution error feeds a repaired tool proposal that can be retained
            for later execution.
        records:
        - runtime.md#rt-rte-tool-authoring
        note: This is the error-informed repair branch, not every initial tool proposal or fallback.
      - scope: Routine transcript appends
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          - runtime.md#rt-rte-scheduled-tool
          note: Runner records supplied prompt and generated outcome messages.
        records:
        - memory.md#mem-obj-session-transcript
        - runtime.md#rt-rte-scheduled-tool
        note: Raw activity retention is not itself trace-extracted behavior-shaping memory.
      - scope: Cached embedding derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-cmp-retrieval-embedding
          note: Provider embeds candidate/query text and caches the vectors.
        records:
        - memory.md#mem-cmp-retrieval-embedding
        note: Known embedding call does not resolve provider weights or initialization.
      - scope: Initial remote corpus, embedding provenance, scanner/draft alternatives, app state and
          separate durable checkpoints
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-cmp-retrieval-embedding
        - memory.md#mem-rte-skill-registration
        - epistemic.md#epi-rte-playbook-compile
        - runtime.md#rt-rte-app-publication
        - memory.md#mem-obj-session-memory-snapshot
        note: Existing-source and opaque alternative provenance remains unknown; copied labels cannot
          establish it.
      records:
      - memory.md#mem-obj-private-memory-note
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-rte-scoped-notes
      - memory.md#mem-obj-learning-record
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-rte-task-distillation
      - memory.md#mem-rte-artifact-extraction
      - memory.md#mem-rte-brief-synthesis
      - epistemic.md#epi-rte-playbook-compile
      - runtime.md#rt-rte-tool-authoring
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-cmp-retrieval-embedding
      - memory.md#mem-rte-skill-registration
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-obj-session-memory-snapshot
      note: Known authored, imported, compiled and task-trace-derived paths coexist with unresolved initialization
        and additional admission paths.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected note/learning/fact/article/outcome text at office model or requesting reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-memory-brief
          - memory.md#mem-rte-task-knowledge
          - memory.md#mem-rte-upstream-results
          - memory.md#mem-bap-knowledge-guidance
          note: Delivered reference snippets and outcomes advise later work; private/shared notes explicitly
            lack operator authority.
        records:
        - memory.md#mem-rte-memory-brief
        - memory.md#mem-rte-task-knowledge
        - memory.md#mem-rte-upstream-results
        - memory.md#mem-bap-knowledge-guidance
        note: Task apply/cite/read framing is shipped delivery guidance, not evidence that every stored
          insight is a standing instruction.
      - scope: Retained text, confidence, recency and vectors at retrieval/matching selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-memory-brief
          - memory.md#mem-rte-task-knowledge
          - memory.md#mem-rte-learning-admission
          - memory.md#mem-cmp-retrieval-embedding
          - runtime.md#rt-rte-scheduled-tool
          note: Note text, learning confidence, dense vectors and tool titles influence relative selection
            priority.
        records:
        - memory.md#mem-rte-memory-brief
        - memory.md#mem-rte-task-knowledge
        - memory.md#mem-rte-learning-admission
        - memory.md#mem-cmp-retrieval-embedding
        - runtime.md#rt-rte-scheduled-tool
        note: Retained ranking inputs have ranking force even though scoring code is fixed.
      - scope: Dependency IDs, skill source identity and synthesis fact-count checkpoint at next-input
          selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-upstream-results
          - memory.md#mem-rte-skill-registration
          - memory.md#mem-rte-brief-synthesis
          note: Dependencies select upstream inputs; skill identity selects registration handling; fact
            count selects the next synthesis input window.
        records:
        - memory.md#mem-rte-upstream-results
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-rte-brief-synthesis
        note: These retained fields select scope or operation, not truth.
      - scope: Stored executable code at worker
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-stored-tool
          - runtime.md#rt-bap-tool-execution
          note: Retained JavaScript selects capability operations and arguments on later executions.
        records:
        - runtime.md#rt-obj-stored-tool
        - runtime.md#rt-bap-tool-execution
        note: Code has executable control, not merely advisory knowledge. Current-run host gates are not
          classified as retained memory controls.
      - scope: Retained task results at automatic distillation
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          note: Task activity and feedback feed a durable future-context artifact.
        records:
        - memory.md#mem-rte-task-distillation
        note: Learning force at the update consumer is distinct from knowledge force at the later office
          model; neither establishes benefit.
      - scope: Smoke error feedback at tool repair model
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          note: Execution feedback shapes repaired code that software can persist for subsequent worker
            execution.
        records:
        - runtime.md#rt-rte-tool-authoring
        note: The error-directed durable update is distinct from the stored code downstream routing authority;
          simulated feedback does not establish business correctness.
      - scope: Persisted Pass and prior TaskID at learning admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          - epistemic.md#epi-obj-verification-result
          note: Pass and prior task identity determine whether a new trusted learning is admissible.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          - epistemic.md#epi-obj-verification-result
          note: Failure to pass or an existing task learning blocks the corresponding append.
        records:
        - memory.md#mem-rte-task-distillation
        - epistemic.md#epi-obj-verification-result
        note: The verification result licenses only its checked domain, not all narrative claims.
      - scope: Rejection tombstones at compiled-skill registration
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-rte-skill-registration
          note: Matching rejected slug/source is an admission criterion.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-skill-registration
          note: Tombstone match vetoes deterministic re-registration.
        records:
        - memory.md#mem-rte-skill-registration
        note: Rejection authorship/undo is not thereby established.
      - scope: Archive flag at article-file search and contradiction acknowledgment at lint
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-rte-task-knowledge
          - epistemic.md#epi-rte-lint-judge
          - epistemic.md#epi-rte-lint-disposal
          note: Archived articles are excluded from file search; acknowledgment metadata suppresses later
            cluster checking.
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-rte-lint-judge
          - epistemic.md#epi-rte-lint-disposal
          note: Acknowledgment metadata supplies the predicate for whether the cluster is eligible for
            another check.
        records:
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-task-knowledge
        - epistemic.md#epi-rte-lint-judge
        - epistemic.md#epi-rte-lint-disposal
        note: These are bounded consumers; full expiry/deletion propagation through every query is unresolved.
      - scope: Compiled wrapper directions at intended later agent consumer
        assessment: partial
        findings:
        - value: instruction
          basis: afforded
          records:
          - epistemic.md#epi-rte-playbook-compile
          note: Wrapper tells a later agent to load canonical steps, execute and record results.
        records:
        - epistemic.md#epi-rte-playbook-compile
        - memory.md#mem-rte-skill-registration
        note: Direction text and intended consumer are established, but assignment/loading/invocation
          are not fully traced.
      - scope: Routine transcript and outcome artifact at requested frontend presentation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          - runtime.md#rt-rte-scheduled-tool
          note: Retained prompts/outcomes are available as information to requesting UI readers.
        records:
        - memory.md#mem-obj-session-transcript
        - runtime.md#rt-rte-scheduled-tool
        note: Workflow annotation on the runtime route establishes a shipped request/presentation path,
          not human receipt.
      - scope: Remote index effects, app-state consumers, checkpoint restoration and full skill/native-session
          consumption
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-cmp-retrieval-embedding
        - runtime.md#rt-rte-app-publication
        - memory.md#mem-obj-session-memory-snapshot
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-obj-session-transcript
        note: These opaque or untraced alternatives prevent complete enumeration of authority paths.
      records:
      - memory.md#mem-rte-memory-brief
      - memory.md#mem-rte-task-knowledge
      - memory.md#mem-rte-upstream-results
      - memory.md#mem-bap-knowledge-guidance
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-cmp-retrieval-embedding
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-rte-skill-registration
      - memory.md#mem-rte-brief-synthesis
      - runtime.md#rt-obj-stored-tool
      - runtime.md#rt-bap-tool-execution
      - memory.md#mem-rte-task-distillation
      - runtime.md#rt-rte-tool-authoring
      - epistemic.md#epi-obj-verification-result
      - memory.md#mem-rte-wiki-maintenance
      - epistemic.md#epi-rte-lint-judge
      - epistemic.md#epi-rte-lint-disposal
      - epistemic.md#epi-rte-playbook-compile
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-obj-shared-memory-write
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-obj-session-memory-snapshot
      note: Authority is local to the consumed retained part. Known ranking, routing, validation, enforcement,
        learning and knowledge do not upgrade the afforded procedural instruction route or resolve opaque
        consumers.
    write_agency:
      assessment: partial
      units:
      - scope: MCP scoped-note and shared-promotion software admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-scoped-notes
          note: Software accepts caller content without a required per-content human decision.
        records:
        - memory.md#mem-rte-scoped-notes
        note: Caller initiation and caller-authored prose do not make this admission manual.
      - scope: Explicit typed-learning validator and completed-task capture
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-learning-admission
          - memory.md#mem-rte-task-distillation
          note: Software validates/appends caller records and admits pass-gated task-derived learning.
        records:
        - memory.md#mem-rte-learning-admission
        - memory.md#mem-rte-task-distillation
        note: Asserted user-stated source is not authenticated human approval.
      - scope: Extraction, synthesis, compression/archive and skill-registration software writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-artifact-extraction
          - memory.md#mem-rte-brief-synthesis
          - memory.md#mem-rte-wiki-maintenance
          - memory.md#mem-rte-skill-registration
          - epistemic.md#epi-rte-playbook-compile
          note: Model/code proposals are admitted by software checks; starting a maintenance request is
            not content approval.
        records:
        - memory.md#mem-rte-artifact-extraction
        - memory.md#mem-rte-brief-synthesis
        - memory.md#mem-rte-wiki-maintenance
        - memory.md#mem-rte-skill-registration
        - epistemic.md#epi-rte-playbook-compile
        note: Known subsequent transformations remain automatic despite unresolved initial content control.
      - scope: Saved-tool authoring/upsert, including routine fallback
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          - runtime.md#rt-rte-scheduled-tool
          note: Software persistence admits model code or a routine fallback without per-code human approval.
        records:
        - runtime.md#rt-rte-tool-authoring
        - runtime.md#rt-rte-scheduled-tool
        note: Manual build endpoint and scheduled routine have different provenance conditions but both
          software admission.
      - scope: Routine transcript/outcome persistence and vector-cache writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-tool
          - memory.md#mem-obj-session-transcript
          - memory.md#mem-cmp-retrieval-embedding
          note: Runner appends outcomes and embedding caller writes cache entries.
        records:
        - runtime.md#rt-rte-scheduled-tool
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-cmp-retrieval-embedding
        note: Recording a human-supplied prompt is not a separate manual admission of generated outcomes.
      - scope: Human-edited existing brief body
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - memory.md#mem-rte-brief-synthesis
          note: Human editing supplies retained body content that the subsequent synthesis preserves.
        records:
        - memory.md#mem-rte-brief-synthesis
        note: This is the separately evidenced human edit, not a human veto over newly generated learned
          content.
      - scope: Contradiction-resolution caller, rejection-tombstone authoring, remote initialization and
          app/checkpoint replacements
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-lint-disposal
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-obj-shared-memory-write
        - runtime.md#rt-rte-app-publication
        - memory.md#mem-obj-session-memory-snapshot
        note: Synthetic human identity, generic caller identity, storage API and read selection do not
          establish who controls each content admission.
      records:
      - memory.md#mem-rte-scoped-notes
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-rte-task-distillation
      - memory.md#mem-rte-artifact-extraction
      - memory.md#mem-rte-brief-synthesis
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-rte-skill-registration
      - epistemic.md#epi-rte-playbook-compile
      - runtime.md#rt-rte-tool-authoring
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-cmp-retrieval-embedding
      - epistemic.md#epi-rte-lint-disposal
      - memory.md#mem-obj-shared-memory-write
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-obj-session-memory-snapshot
      note: Known software admissions and the specifically evidenced human edit coexist. Untraced initial/replacement
        mechanisms prevent a complete automatic/manual inventory.
    curation_operations:
      assessment: partial
      units:
      - scope: Completed-task insight distillation
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          note: Clipped task title/outcome/proof becomes a reduced retained insight.
        records:
        - memory.md#mem-rte-task-distillation
        note: This is consolidation despite raw task state remaining available; no novel transferable
          explanation is established.
      - scope: Artifact-to-standing-fact extraction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-artifact-extraction
          note: Extraction selects claims from retained source artifacts into standing fact records.
        records:
        - memory.md#mem-rte-artifact-extraction
        note: Semantic fidelity is not checked. Unknown additions cannot be classified as synthesis merely
          because a model is used.
      - scope: Entity brief update and article compression
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-brief-synthesis
          - memory.md#mem-rte-wiki-maintenance
          note: Prior prose and new facts are combined or shortened into a reduced representation.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-brief-synthesis
          - memory.md#mem-rte-wiki-maintenance
          note: Existing article body is revised or receives a learned section.
        records:
        - memory.md#mem-rte-brief-synthesis
        - memory.md#mem-rte-wiki-maintenance
        note: Implemented rewriting supports these operations, not proven factual preservation or novel-claim
          synthesis.
      - scope: Learning current-record selection and age confidence
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-obj-learning-record
          - memory.md#mem-rte-learning-admission
          note: Search removes older repeated scope/type/key results from the current view while keeping
            history.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-learning-admission
          note: Untrusted non-user-stated confidence decreases with age to its floor.
        records:
        - memory.md#mem-obj-learning-record
        - memory.md#mem-rte-learning-admission
        note: Trusted/user-stated records do not decay; view dedup is not deletion of raw history.
      - scope: Scoped private-to-shared promotion and private replacement
        assessment: known
        findings:
        - value: promote
          basis: wired
          records:
          - memory.md#mem-rte-scoped-notes
          note: Copying a private note into shared team memory raises its availability tier.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-private-memory-note
          - memory.md#mem-rte-scoped-notes
          note: Same-key writes replace the current private note.
        records:
        - memory.md#mem-obj-private-memory-note
        - memory.md#mem-rte-scoped-notes
        note: Promotion preserves the private copy; shared backend deletion/history is unknown.
      - scope: Saved-tool same-name replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-obj-stored-tool
          - runtime.md#rt-rte-tool-authoring
          note: Upsert replaces current executable code and increments version.
        records:
        - runtime.md#rt-obj-stored-tool
        - runtime.md#rt-rte-tool-authoring
        note: A version counter does not establish retained old code or quality improvement.
      - scope: Compiled-skill duplicate handling
        assessment: partial
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-skill-registration
          note: Exact/semantic duplicate checks can keep existing skill content rather than admit another
            entry.
        records:
        - memory.md#mem-rte-skill-registration
        note: Dedup/write funnel is established, but full scanner semantics remain uninspected.
      - scope: Article archive and fact contradiction disposal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-wiki-maintenance
          - epistemic.md#epi-rte-lint-disposal
          note: Archive preserves historical body while withdrawing it from traced file search; A/B disposal
            expires a fact while keeping metadata/history.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-wiki-maintenance
          note: Age/read rules remove qualifying articles from the active file-retrieval tier.
        records:
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-lint-disposal
        note: Neither proves universal derivative withdrawal; Both acknowledges conflict without expiring
          either fact.
      - scope: Novel claims in synthesis/extraction, scanner/migration operations and complete derivative
          cleanup
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-brief-synthesis
        - memory.md#mem-rte-artifact-extraction
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-rte-wiki-maintenance
        - epistemic.md#epi-rte-lint-disposal
        note: Record semantics do not establish new propositions absent from inputs. Full scanner, migration
          and index invalidation are unresolved; no positive synthesize value is warranted.
      records:
      - memory.md#mem-rte-task-distillation
      - memory.md#mem-rte-artifact-extraction
      - memory.md#mem-rte-brief-synthesis
      - memory.md#mem-rte-wiki-maintenance
      - memory.md#mem-obj-learning-record
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-obj-private-memory-note
      - memory.md#mem-rte-scoped-notes
      - runtime.md#rt-obj-stored-tool
      - runtime.md#rt-rte-tool-authoring
      - memory.md#mem-rte-skill-registration
      - epistemic.md#epi-rte-lint-disposal
      note: Classifications follow actual transformations, not names such as synthesis or promotion alone.
        Supported local operations remain positive while novel-claim creation and complete cleanup stay
        unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested note/learning/wiki searches and article-body reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-scoped-notes
          - memory.md#mem-rte-learning-admission
          - memory.md#mem-rte-task-knowledge
          note: Caller requests retained notes/learning results or a canonical article body.
        records:
        - memory.md#mem-rte-scoped-notes
        - memory.md#mem-rte-learning-admission
        - memory.md#mem-rte-task-knowledge
        note: A requested article return is not another push merely because code delivers it.
      - scope: Automatic notification and task packet delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-memory-brief
          - memory.md#mem-rte-task-knowledge
          - memory.md#mem-rte-upstream-results
          note: Code selects notes, learning/wiki snippets, article pointers and upstream outcomes without
            a request from the receiving model.
        records:
        - memory.md#mem-rte-memory-brief
        - memory.md#mem-rte-task-knowledge
        - memory.md#mem-rte-upstream-results
        note: Backend Query inside an unsolicited packet remains part of push to the office consumer.
      - scope: Saved-tool manual request and routine reuse
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-saved-call
          note: Manual named call requests stored executable bytes for execution.
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-tool
          note: Due routine automatically selects matching retained tool code for the worker.
        records:
        - runtime.md#rt-rte-saved-call
        - runtime.md#rt-rte-scheduled-tool
        note: Two distinct selectors/operations, not duplicate counting of one requested return.
      - scope: Synthesis and compilation maintenance reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-brief-synthesis
          - epistemic.md#epi-rte-playbook-compile
          note: Maintenance requests the retained entity brief/facts or canonical playbook source as input.
        records:
        - memory.md#mem-rte-brief-synthesis
        - epistemic.md#epi-rte-playbook-compile
        note: These later update consumers are distinct from automatic delivery to the office model.
      - scope: Routine transcript/artifact requested frontend retrieval
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-session-transcript
          - runtime.md#rt-rte-scheduled-tool
          note: Service GET and frontend requests retrieve persisted outcomes for display.
        records:
        - memory.md#mem-obj-session-transcript
        - runtime.md#rt-rte-scheduled-tool
        note: No automatic conversational replay into tool authoring is established.
      - scope: Full skill/native-session loading, remote alternatives, app-state reuse and durable resume
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-obj-shared-memory-write
        - runtime.md#rt-rte-app-publication
        - memory.md#mem-obj-session-memory-snapshot
        note: Known request and push routes cannot establish all unresolved consumers or durable recovery
          wiring.
      records:
      - memory.md#mem-rte-scoped-notes
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-rte-task-knowledge
      - memory.md#mem-rte-memory-brief
      - memory.md#mem-rte-upstream-results
      - runtime.md#rt-rte-saved-call
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-rte-brief-synthesis
      - epistemic.md#epi-rte-playbook-compile
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-rte-skill-registration
      - memory.md#mem-obj-shared-memory-write
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-obj-session-memory-snapshot
      note: Both pull and push are wired on named routes; unresolved alternatives prevent a complete direction
        inventory.
    read_back_signal:
      assessment: partial
      units:
      - scope: Notification-triggered private note push
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-memory-brief
          note: Trigger is notification; its text matches retained private note text to choose two clipped
            notes.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-memory-brief
          note: Recency and availability further select/bound the private brief.
        records:
        - memory.md#mem-rte-memory-brief
        note: Remote backend selection is a separate opaque branch, not upgraded by this local witness.
      - scope: Notification-triggered GBrain result push
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-memory-brief
        - memory.md#mem-obj-shared-memory-write
        note: Notification-derived query and hit limits are known, but remote ranking/selection mechanism
          is opaque; no lexical/embedding value is inferred from Query.
      - scope: Task-triggered learning/wiki/article-pointer push
        assessment: partial
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-task-knowledge
          note: Task title/details or goal-derived terms score retained learning text and article files.
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-task-knowledge
          - memory.md#mem-cmp-retrieval-embedding
          note: Configured dense retrieval uses query/candidate vectors and cosine/fused scores.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-task-knowledge
          - memory.md#mem-rte-learning-admission
          note: Confidence, age/current-record eligibility and item/clipping limits constrain supplied
            parts.
        records:
        - memory.md#mem-rte-task-knowledge
        - memory.md#mem-cmp-retrieval-embedding
        - memory.md#mem-rte-learning-admission
        note: Known local lexical and configured dense mechanisms do not resolve every remote wiki-index
          branch.
      - scope: Dependency-triggered upstream outcome push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-upstream-results
          note: DependsOn/BlockedOn IDs actually match retained task records and select delivered outcome/proof
            excerpts.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-upstream-results
          note: Done/review eligibility and clipping restrict delivery.
        records:
        - memory.md#mem-rte-upstream-results
        note: Identifiers select delivered retained parts here, rather than merely naming a requested
          file.
      - scope: Scheduled routine automatic saved-tool selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-tool
          note: Exact callable-name mention matches a retained tool identity for worker delivery.
        - value: inferred-lexical
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-tool
          note: Exact title or at least two title-word overlaps select saved code when matching the prompt.
        records:
        - runtime.md#rt-rte-scheduled-tool
        note: Due routine is trigger; current prompt is selector input; selected part is stored executable
          code.
      - scope: Untraced skill/app/checkpoint push alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-skill-registration
        - runtime.md#rt-rte-app-publication
        - memory.md#mem-obj-session-memory-snapshot
        note: Their direction and any automatic selector are unresolved; a known pull interface cannot
          make them inapplicable.
      - scope: Explicit pull-only note/learning/transcript and maintenance-request operations
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-scoped-notes
        - memory.md#mem-rte-learning-admission
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-rte-brief-synthesis
        - epistemic.md#epi-rte-playbook-compile
        note: Push selection signal is inapplicable to these named requested operations, not to the mixed
          boundary.
      records:
      - memory.md#mem-rte-memory-brief
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-rte-task-knowledge
      - memory.md#mem-cmp-retrieval-embedding
      - memory.md#mem-rte-learning-admission
      - memory.md#mem-rte-upstream-results
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-rte-skill-registration
      - runtime.md#rt-rte-app-publication
      - memory.md#mem-obj-session-memory-snapshot
      - memory.md#mem-rte-scoped-notes
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-rte-brief-synthesis
      - epistemic.md#epi-rte-playbook-compile
      note: Known push selectors use lexical, dense, identity and coarse signals. Remote and untraced
        branches prevent complete classification; no inferred-judgment selector is established by the
        accepted records.
    trace_learning:
      assessment: partial
      units:
      - scope: Completed-task state to durable insight/entity articles to later task context
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          - memory.md#mem-rte-task-knowledge
          note: Automatic completed-task capture writes durable behavior-shaping knowledge consumed by
            later selection.
        records:
        - memory.md#mem-rte-task-distillation
        - memory.md#mem-rte-task-knowledge
        note: Qualifies without a model update, novel claim or demonstrated improvement; the verification
          gate covers only one branch.
      - scope: Artifact extraction to facts and future snippets
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-artifact-extraction
        - memory.md#mem-obj-typed-fact
        - memory.md#mem-rte-task-knowledge
        note: Automatic write and later knowledge consumer are wired, but original artifact content can
          be static or trace-bearing. Trace origin is not established for every included artifact.
      - scope: Fact-fed brief rewrites and task-derived playbook/skill alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-brief-synthesis
        - epistemic.md#epi-rte-playbook-compile
        - memory.md#mem-rte-skill-registration
        - memory.md#mem-rte-task-distillation
        note: Fact provenance and full draft/skill consumption chain are unresolved; procedure registration
          alone does not complete every trace-fed later-consumer route.
      - scope: Smoke-error-directed repair to persisted code to later worker
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          - runtime.md#rt-obj-stored-tool
          - runtime.md#rt-bap-tool-execution
          note: Simulated execution error automatically feeds model repair; an admitted repaired tool
            is retained and executed on later calls.
        records:
        - runtime.md#rt-rte-tool-authoring
        - runtime.md#rt-obj-stored-tool
        - runtime.md#rt-bap-tool-execution
        note: Conditional repair/persistence wiring qualifies even within one authoring episode. No successful
          business repair or repeated learning over routine history is established.
      - scope: Routine transcript feedback alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-scheduled-tool
        - memory.md#mem-obj-session-transcript
        note: Raw history is retained for readers, but not supplied as author context in the inspected
          routine. Other native entry consumers remain opaque; this does not establish system-wide absence.
      - scope: Remote initialization, native compaction, app state and durable resume alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-obj-session-memory-snapshot
        - runtime.md#rt-rte-app-publication
        note: Opaque or untraced writes cannot be converted into bounded absence. Raw log retention and
          current-state projection alone do not establish qualifying trace learning.
      records:
      - memory.md#mem-rte-task-distillation
      - memory.md#mem-rte-task-knowledge
      - memory.md#mem-rte-artifact-extraction
      - memory.md#mem-obj-typed-fact
      - memory.md#mem-rte-brief-synthesis
      - epistemic.md#epi-rte-playbook-compile
      - memory.md#mem-rte-skill-registration
      - runtime.md#rt-rte-tool-authoring
      - runtime.md#rt-obj-stored-tool
      - runtime.md#rt-bap-tool-execution
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-obj-session-memory-snapshot
      - runtime.md#rt-rte-app-publication
      note: Task-derived capture and smoke-feedback-directed durable repair supply wired positives. Other
        trace origin/write/consumer chains remain unresolved; no system-wide negative or observed learning
        outcome is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Verification execution feedback in the qualifying completed-task capture
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          - epistemic.md#epi-rte-task-check
          - epistemic.md#epi-obj-verification-result
          note: Recorded command output, filesystem probe detail or HTTP execution feedback is clipped
            into the retained task insight.
        records:
        - memory.md#mem-rte-task-distillation
        - epistemic.md#epi-rte-task-check
        - epistemic.md#epi-obj-verification-result
        note: Original source is execution feedback, not the eventual JSONL record format. Different verification
          kinds retain their narrow domains.
      - scope: Task completion/activity state in automatic entity and learning capture
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-rte-task-distillation
          note: Recorded done-task activity and completion state feed automatic entity associations and
            learning writes.
        records:
        - memory.md#mem-rte-task-distillation
        note: Classifies runtime task activity, not all copied narrative title/detail content as events.
      - scope: Copied task narrative and optional draft provenance within that qualifying route
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-task-distillation
        - epistemic.md#epi-rte-playbook-compile
        note: Task title/details may originate in several kinds of content; the records do not establish
          session-log, tool-trace or trajectory origin for every copied part.
      - scope: Artifact, fact-fed brief and skill routes with unresolved qualifying trace learning
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-artifact-extraction
        - memory.md#mem-rte-brief-synthesis
        - memory.md#mem-rte-skill-registration
        - epistemic.md#epi-rte-playbook-compile
        note: Original input may be static, trace-bearing or mixed. Adapter/artifact labels do not resolve
          trace origin.
      - scope: Simulated tool execution feedback in qualifying tool repair
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-tool-authoring
          note: Smoke execution error text is recorded and supplied to the repair model before possible
            durable tool admission.
        records:
        - runtime.md#rt-rte-tool-authoring
        note: Simulation limits semantic warrant, not the fact that execution feedback feeds the wired
          update.
      - scope: Raw routine transcript and remote/native/app/checkpoint alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-scheduled-tool
        - memory.md#mem-obj-session-transcript
        - memory.md#mem-obj-shared-memory-write
        - memory.md#mem-obj-session-memory-snapshot
        - runtime.md#rt-rte-app-publication
        note: Raw session messages exist, but no qualifying automatic transcript-to-durable-behavior update
          is established for them. Neither session-logs nor trajectories is asserted from mere retention.
      records:
      - memory.md#mem-rte-task-distillation
      - epistemic.md#epi-rte-task-check
      - epistemic.md#epi-obj-verification-result
      - epistemic.md#epi-rte-playbook-compile
      - memory.md#mem-rte-artifact-extraction
      - memory.md#mem-rte-brief-synthesis
      - memory.md#mem-rte-skill-registration
      - runtime.md#rt-rte-tool-authoring
      - runtime.md#rt-rte-scheduled-tool
      - memory.md#mem-obj-session-transcript
      - memory.md#mem-obj-shared-memory-write
      - memory.md#mem-obj-session-memory-snapshot
      - runtime.md#rt-rte-app-publication
      note: Execution feedback and runtime task activity have local wired warrants. Mixed narrative and
        opaque original inputs prevent complete trace-source coverage; a local positive does not classify
        all included writes.
---

# Wuphf memory profile

## Comparison rationale

The boundary is a complete artifact, partial loop. Every axis is partial because the accepted inventory retains unresolved material alternatives, not because wired implementation needs a live run to be classifiable. No finding claims observation, causal benefit, or universally complete value coverage. Each positive retains its local route and consumer; the union is not a complete inventory assertion.

Reconciliation identifies six duplicate referents. This profile uses the canonical memory destinations for typed facts, learning records, artifact extraction, entity synthesis, task distillation and learning admission. Their superseded epistemic declarations do not supply stronger statuses. The epistemic entity-brief, verification, lint and playbook-compiler records remain distinct. The knowledge-packet record overlaps only the learning/index branch of [MEM-RTE-task-knowledge](memory.md#mem-rte-task-knowledge); article-pointer delivery does not establish article-body delivery. Enclosing office turns likewise remain distinct from their contained selectors.

The most consequential authority split is task experience at its automatic update consumer versus derived text at the later office model. [MEM-RTE-task-distillation](memory.md#mem-rte-task-distillation) supports learning force and trace learning in the profile's route sense; [MEM-BAP-knowledge-guidance](memory.md#mem-bap-knowledge-guidance) supports downstream reference force. Neither establishes improved capacity. Verification feedback has only the narrow command/file/HTTP license described by [EPI-RTE-task-check](epistemic.md#epi-rte-task-check). Copied task narratives retain unresolved original provenance, even when a pass result gates their retention.

The error-directed repair branch of [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring) also qualifies as wired trace learning: simulated execution feedback feeds automatic repair, admitted code persists, and a later worker consumes it. Conditional activation is not missing wiring. This does not contradict the reports' unestablished learning/improvement outcomes, and it does not turn raw routine transcripts into a feedback loop. Simulation bounds the feedback's business warrant, not its execution-trace origin.

The procedural wrapper supplies an afforded instruction path, not a fully traced invocation. [EPI-RTE-playbook-compile](epistemic.md#epi-rte-playbook-compile) and [MEM-RTE-skill-registration](memory.md#mem-rte-skill-registration) leave loading/assignment unresolved. Stored JavaScript instead reaches a wired executor through [RT-BAP-tool-execution](runtime.md#rt-bap-tool-execution). Its operation selection is executable routing, while rejection tombstones have distinct admission validation and enforcement force. Current-run approval flags and static schemas are not silently included as accumulated memory controls.

Compression, extraction and fact-fed rewriting support consolidation/evolution without proving semantic fidelity. The name synthesis and a model's involvement do not establish a new claim absent from inputs. [MEM-RTE-brief-synthesis](memory.md#mem-rte-brief-synthesis) retains that uncertainty. Archive and contradiction expiry have bounded withdrawal effects, not global deletion of derivatives; [MEM-RTE-wiki-maintenance](memory.md#mem-rte-wiki-maintenance) and [EPI-RTE-lint-disposal](epistemic.md#epi-rte-lint-disposal) prevent the stronger conclusion.

Read-back directions classify operations within a chain. Automatically querying a backend to fill a notification is push to the recipient model; an explicitly requested article return is pull. The identity signal on [MEM-RTE-upstream-results](memory.md#mem-rte-upstream-results) actually selects delivered task records. Remote query ranking stays opaque despite local lexical and dense witnesses. Routine outcomes have a requested frontend presentation path through the workflow annotation on [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool), not an established conversational feedback loop into future authoring.

No frozen source files were read for this classification. All warrants come from the supplied accepted records and their annotations; no new evidence, records, quotes or verification judgments were added. Unknown remote storage is not recast as a particular database, a display projection does not classify opaque native payloads, and the current-state projection in [MEM-OBJ-session-memory-snapshot](memory.md#mem-obj-session-memory-snapshot) is not asserted to be a durable checkpoint. Additional source inspection would require recorded facts before it could strengthen this profile.
