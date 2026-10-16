---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Cludebot memory comparison: retained content, local stores, retrieval state and durable
  derived guidance, with unresolved portable and consumer alternatives.'
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
source-identity: https://github.com/sebbsssss/cludebot
reviewed-boundary: cecf234f10397b1e21dec2ff65ded864982f3564
memory-comparison:
  version: 2
  scope: Accumulated PostgreSQL memory/conversation content, JSON and SQLite memory, dream queue results,
    derived semantic/procedural/self-model/journal content, vectors and graph/access state, shadow/evaluation
    artifacts, changing prompt-sync snapshots, their admission/maintenance and later-consumer routes.
    Portable pack/client alternatives remain included but unresolved. Excludes transient current-call
    context as a retained object, static shipped/setup policy, inference-provider weights and promotional/workstation
    metadata; dependencies and current-call renderers matter only at retained-memory consumers.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: PostgreSQL content, conversations, queue/log and access-state rows
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records:
          - memory.md#mem-obj-memories
          - memory.md#mem-obj-retrieval-state
          - runtime.md#rt-rte-chat-turn
          - memory.md#mem-rte-shadow-reconcile
          note: Supabase/PostgreSQL retains content and symbolic selection state; chat separately retains
            conversation rows.
        records:
        - memory.md#mem-obj-memories
        - memory.md#mem-obj-retrieval-state
        - runtime.md#rt-rte-chat-turn
        - memory.md#mem-rte-shadow-reconcile
        note: These inspected relational parts have source-grounded persistence; provider weights are
          not their substrate.
      - scope: Persistent dense-vector indexes and memory-link structures
        assessment: known
        findings:
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-recall-selection
          note: Retained summary/fragment vectors support similarity retrieval.
        - value: graph
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-deep-connection
          - memory.md#mem-rte-recall-selection
          note: Retained entity/link structures support traversal and candidate expansion; their physical
            backing is relational.
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-deep-connection
        - memory.md#mem-rte-recall-selection
        note: Logical vector and graph access stores coexist with their relational backing; no separate
          graph service is inferred.
      - scope: JSON local memories, prompt-sync snapshot and benchmark result artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-local-store
          - memory.md#mem-rte-prompt-sync
          - memory.md#mem-obj-evaluation-results
          note: The JSON array, changing UTF-8 memory snapshot and result JSON artifacts persist as files.
        records:
        - memory.md#mem-obj-local-store
        - memory.md#mem-rte-prompt-sync
        - memory.md#mem-obj-evaluation-results
        note: These are accumulated content surfaces, unlike static setup instructions.
      - scope: SQLite memories, vectors and dream queue
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-sqlite-store
          - memory.md#mem-rte-local-dream
          note: SQLite retains memory rows and separate generated queue results.
        records:
        - memory.md#mem-obj-sqlite-store
        - memory.md#mem-rte-local-dream
        note: The local database is not classified as PostgreSQL; queue completion is not recall adoption.
      - scope: Portable pack payloads and remaining service/client retained alternatives
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-pack-verification
        - runtime.md#rt-rte-memory-entry
        note: Pack reading and mode dispatch are established, but retained portable parts, all client
          stores and external storage internals are not enumerated by these records. No additional substrate
          can be assigned.
      records:
      - memory.md#mem-obj-memories
      - memory.md#mem-obj-retrieval-state
      - runtime.md#rt-rte-chat-turn
      - memory.md#mem-rte-shadow-reconcile
      - memory.md#mem-rte-deep-connection
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-obj-local-store
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-obj-evaluation-results
      - memory.md#mem-obj-sqlite-store
      - memory.md#mem-rte-local-dream
      - epistemic.md#epi-rte-pack-verification
      - runtime.md#rt-rte-memory-entry
      note: Positive substrates cover inspected stores and access structures, not an exhaustive inventory
        of every portable/client/service alternative.
    representational_form:
      assessment: partial
      units:
      - scope: Retained row prose and its chat, response, reflection, explanation and snapshot consumption
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memories
          - runtime.md#rt-rte-chat-turn
          - memory.md#mem-rte-response-memory
          - memory.md#mem-rte-journal-continuity
          - memory.md#mem-rte-provenance-explanation
          - memory.md#mem-rte-prompt-sync
          note: Content and summaries acquire meaning through model/host interpretation after bounded
            rendering.
        records:
        - memory.md#mem-obj-memories
        - runtime.md#rt-rte-chat-turn
        - memory.md#mem-rte-response-memory
        - memory.md#mem-rte-journal-continuity
        - memory.md#mem-rte-provenance-explanation
        - memory.md#mem-rte-prompt-sync
        note: Natural-language content is distinct from its symbolic IDs and numerical retrieval features.
      - scope: Retained IDs, tags, counters, queue operations, links, revocation fields and evaluator
          scores
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-obj-sqlite-store
          - memory.md#mem-rte-memory-withdrawal
          - memory.md#mem-obj-evaluation-results
          note: Fixed code interprets localized metadata, numerical scores and queue/link/control fields.
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-obj-sqlite-store
        - memory.md#mem-rte-memory-withdrawal
        - memory.md#mem-obj-evaluation-results
        note: Ordinary numbers with code-defined meanings are symbolic, not distributed parameters.
      - scope: Dense retained embedding parts consumed by similarity and prediction
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-obj-sqlite-store
          - memory.md#mem-rte-deep-connection
          note: Dense numerical representations distribute information across dimensions; they are not
            runtime-trained model weights.
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-obj-sqlite-store
        - memory.md#mem-rte-deep-connection
        note: Classification concerns retained vectors at these consumers, not the inference models that
          produced them.
      - scope: Opaque portable payload parts and incompletely decoded client/queue alternatives
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-pack-verification
        - memory.md#mem-rte-local-dream
        - runtime.md#rt-rte-memory-entry
        note: Readable summaries and JSON display do not establish the form of all consumed payloads or
          unseen queue-result consumers. External inference weights are dependencies, not accumulated
          memory in this scope.
      records:
      - memory.md#mem-obj-memories
      - runtime.md#rt-rte-chat-turn
      - memory.md#mem-rte-response-memory
      - memory.md#mem-rte-journal-continuity
      - memory.md#mem-rte-provenance-explanation
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-obj-sqlite-store
      - memory.md#mem-rte-memory-withdrawal
      - memory.md#mem-obj-evaluation-results
      - memory.md#mem-rte-deep-connection
      - epistemic.md#epi-rte-pack-verification
      - memory.md#mem-rte-local-dream
      - runtime.md#rt-rte-memory-entry
      note: Mixed prose, fixed-rule metadata and dense representations remain separate units; opaque consumed
        payload alternatives prevent complete coverage.
    lineage:
      assessment: partial
      units:
      - scope: Captured chat exchange and trace-derived semantic/procedural/journal outputs
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - memory.md#mem-rte-strategy-refinement
          - memory.md#mem-rte-journal-continuity
          note: Recorded conversations and action experience feed retained extracts, compaction, rules
            and continuity artifacts.
        records:
        - runtime.md#rt-rte-chat-turn
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-strategy-refinement
        - memory.md#mem-rte-journal-continuity
        note: Known derivation paths do not authenticate original assertions or establish that every episodic
          input is conversational.
      - scope: Model-authored finding, self-model, resolution, journal and strategy prose
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - workflow.md#wf-rte-store-finding
          - epistemic.md#epi-rte-self-reflection
          - memory.md#mem-rte-belief-revision
          - memory.md#mem-rte-journal-continuity
          - memory.md#mem-rte-strategy-refinement
          note: Models compose admitted natural-language content; authored does not mean human-approved
            or epistemically accepted.
        records:
        - workflow.md#wf-rte-store-finding
        - epistemic.md#epi-rte-self-reflection
        - memory.md#mem-rte-belief-revision
        - memory.md#mem-rte-journal-continuity
        - memory.md#mem-rte-strategy-refinement
        note: Authorship and trace derivation can coexist on a product; neither guarantees its truth.
      - scope: Pack and document acquisition into ordinary memory
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-pack-import
          - memory.md#mem-rte-upload-extraction
          note: Externally supplied packs and document chunks enter the memory boundary; generated extraction
            does not authenticate their authors.
        records:
        - runtime.md#rt-rte-pack-import
        - memory.md#mem-rte-upload-extraction
        note: Imported lineage is supported for these acquisition paths, not for every stored row.
      - scope: Computed retrieval structures, prompt snapshot and evaluator result artifacts
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-rte-deep-connection
          - memory.md#mem-rte-prompt-sync
          - memory.md#mem-obj-evaluation-results
          note: Embedding/index construction, computed graph links, rendered snapshots and calculated
            result artifacts derive from retained/source inputs.
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-deep-connection
        - memory.md#mem-rte-prompt-sync
        - memory.md#mem-obj-evaluation-results
        note: This describes inspected derivation, not initial provenance of the source inputs or embedding-model
          training.
      - scope: Initial caller text, complete embedding/extraction provenance and portable payload histories
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memories
        - memory.md#mem-obj-retrieval-state
        - runtime.md#rt-rte-memory-entry
        - epistemic.md#epi-rte-pack-verification
        note: Generic caller identity and source labels do not establish initial authorship; full extraction
          lineage and all pack histories remain unresolved.
      records:
      - runtime.md#rt-rte-chat-turn
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-strategy-refinement
      - memory.md#mem-rte-journal-continuity
      - workflow.md#wf-rte-store-finding
      - epistemic.md#epi-rte-self-reflection
      - memory.md#mem-rte-belief-revision
      - runtime.md#rt-rte-pack-import
      - memory.md#mem-rte-upload-extraction
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-deep-connection
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-obj-evaluation-results
      - memory.md#mem-obj-memories
      - runtime.md#rt-rte-memory-entry
      - epistemic.md#epi-rte-pack-verification
      note: Several established derivation paths coexist; initial-content and opaque payload provenance
        cannot be inferred from them.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Selected content and summaries at answering, explanation and journal consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - memory.md#mem-rte-response-memory
          - memory.md#mem-rte-provenance-explanation
          - memory.md#mem-rte-journal-continuity
          note: Retained text supplies context/reference to actual wired model consumers; delivery is
            not obedience.
        records:
        - runtime.md#rt-rte-chat-turn
        - memory.md#mem-rte-response-memory
        - memory.md#mem-rte-provenance-explanation
        - memory.md#mem-rte-journal-continuity
        note: The unit is the contextual content path, not shipped grounding rules.
      - scope: Retained procedural rules at the shared response model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-bap-procedural-guidance
          - memory.md#mem-rte-response-memory
          note: Selected rules are delivered with an explicit direction to follow them in current and
            future reselected responses.
        records:
        - memory.md#mem-bap-procedural-guidance
        - memory.md#mem-rte-response-memory
        note: Force is interpretation-dependent standing guidance, not an execution-time enforcement mechanism.
      - scope: Recorded experience and prior self-representations at durable artifact update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - epistemic.md#epi-rte-action-learning
          - memory.md#mem-rte-journal-continuity
          - epistemic.md#epi-rte-self-reflection
          note: Trace/experience and prior derived memory feed automatic durable semantic, procedural,
            self-model and journal updates.
        records:
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - epistemic.md#epi-rte-action-learning
        - memory.md#mem-rte-journal-continuity
        - epistemic.md#epi-rte-self-reflection
        note: Learning authority names the update consumer; it asserts neither parameter training nor
          improved capacity.
      - scope: Text, vectors, links, importance, decay and access state at recall scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-obj-local-store
          - memory.md#mem-rte-recall-selection
          - memory.md#mem-rte-strategy-refinement
          - memory.md#mem-rte-belief-revision
          note: Stored features and text influence relative retrieval priority; use and outcomes can change
            those inputs.
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-obj-local-store
        - memory.md#mem-rte-recall-selection
        - memory.md#mem-rte-strategy-refinement
        - memory.md#mem-rte-belief-revision
        note: Retained ranking inputs suffice even when scoring policy is fixed code.
      - scope: Queued operation/IDs at local dream dispatch and stored relation/ID inputs at trace traversal
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-local-dream
          - memory.md#mem-obj-sqlite-store
          - memory.md#mem-rte-provenance-explanation
          note: Queue state selects the operation and source window; stored evidence/link IDs select ancestry
            consumed by explanation.
        records:
        - memory.md#mem-rte-local-dream
        - memory.md#mem-obj-sqlite-store
        - memory.md#mem-rte-provenance-explanation
        note: Routing force is on operation/input selection, independent of whether a generated queue
          result has a later consumer.
      - scope: Retained encrypted access state and content at revoke/redelegate and read guards
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-memory-withdrawal
          note: Delegated/revoked state and removed provider access exclude retained material on inspected
            guarded read paths.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-rte-memory-withdrawal
          note: Stored encrypted content is the authentication target used to validate a replacement provider
            wrap by unwrap/decrypt.
        records:
        - memory.md#mem-rte-memory-withdrawal
        note: These are access/authentication effects, not truth validation; hydration and unaudited lanes
          prevent a universal veto claim.
      - scope: Prompt-sync content at a later external host
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records:
          - memory.md#mem-rte-prompt-sync
          note: The documented symlink route affords host access to rendered memory.
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-rte-prompt-sync
          note: Rendered learned-behavior sections afford later guidance if the host loads them.
        records:
        - memory.md#mem-rte-prompt-sync
        note: Snapshot production is wired; host loading and compliance are only afforded.
      - scope: Queue results, shadow proposals, portable revocations and remaining host consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-dream
        - memory.md#mem-rte-shadow-reconcile
        - epistemic.md#epi-rte-pack-verification
        - runtime.md#rt-rte-memory-entry
        note: Queue adoption, production use of shadow proposals and all-importer revocation filtering
          are not established. Their downstream force cannot be upgraded from retention alone.
      records:
      - runtime.md#rt-rte-chat-turn
      - memory.md#mem-rte-response-memory
      - memory.md#mem-rte-provenance-explanation
      - memory.md#mem-rte-journal-continuity
      - memory.md#mem-bap-procedural-guidance
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - epistemic.md#epi-rte-action-learning
      - epistemic.md#epi-rte-self-reflection
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-obj-local-store
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-rte-strategy-refinement
      - memory.md#mem-rte-belief-revision
      - memory.md#mem-rte-local-dream
      - memory.md#mem-obj-sqlite-store
      - memory.md#mem-rte-memory-withdrawal
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-rte-shadow-reconcile
      - epistemic.md#epi-rte-pack-verification
      - runtime.md#rt-rte-memory-entry
      note: Authority is consumer-specific. Positive update, guidance, ranking and access effects do not
        resolve opaque or unconsumed alternatives.
    write_agency:
      assessment: partial
      units:
      - scope: Automatic chat admission, dream/journal/strategy production, graph/link feedback and tool
          findings
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - memory.md#mem-rte-strategy-refinement
          - memory.md#mem-rte-journal-continuity
          - memory.md#mem-rte-deep-connection
          - memory.md#mem-obj-retrieval-state
          - memory.md#mem-obj-local-store
          - workflow.md#wf-rte-store-finding
          note: Code/model admits these products or selection-state updates without an explicit per-content
            human decision.
        records:
        - runtime.md#rt-rte-chat-turn
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-strategy-refinement
        - memory.md#mem-rte-journal-continuity
        - memory.md#mem-rte-deep-connection
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-obj-local-store
        - workflow.md#wf-rte-store-finding
        note: A user request, scheduler start or owner task assignment does not make subsequent individual
          admissions manual.
      - scope: Upload-node admission, prompt snapshot refresh, shadow logging and queue completion
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-upload-extraction
          - memory.md#mem-rte-prompt-sync
          - memory.md#mem-rte-shadow-reconcile
          - memory.md#mem-rte-local-dream
          note: Software parses/stores nodes, replaces a computed snapshot, logs proposals and persists
            generated queue results without per-product human approval.
        records:
        - memory.md#mem-rte-upload-extraction
        - memory.md#mem-rte-prompt-sync
        - memory.md#mem-rte-shadow-reconcile
        - memory.md#mem-rte-local-dream
        note: Known automatic transformations are separate from unresolved original input or queue admission
          control.
      - scope: Generic SDK/MCP writes, caller patches/deletion, selected import content and local queue
          admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-memory-entry
        - memory.md#mem-rte-memory-withdrawal
        - runtime.md#rt-rte-pack-import
        - memory.md#mem-rte-local-dream
        note: Callers can be human or agent. The records establish interfaces and software checks, not
          an explicit human content decision for these mechanisms; manual versus automatic control cannot
          be completed.
      - scope: Portable marketplace/client admission and remaining initial-content mechanisms
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-pack-verification
        - runtime.md#rt-rte-memory-entry
        note: All transfer, installation and client-side replacement controls are not traced. No manual
          classification follows from operator-facing UI or ownership alone.
      records:
      - runtime.md#rt-rte-chat-turn
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-strategy-refinement
      - memory.md#mem-rte-journal-continuity
      - memory.md#mem-rte-deep-connection
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-obj-local-store
      - workflow.md#wf-rte-store-finding
      - memory.md#mem-rte-upload-extraction
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-rte-shadow-reconcile
      - memory.md#mem-rte-local-dream
      - runtime.md#rt-rte-memory-entry
      - memory.md#mem-rte-memory-withdrawal
      - runtime.md#rt-rte-pack-import
      - epistemic.md#epi-rte-pack-verification
      note: Automatic admission is established locally; generic callers and uninspected portable/client
        mechanisms prevent a complete control inventory. No explicit human-content witness establishes
        manual here.
    curation_operations:
      assessment: partial
      units:
      - scope: Main semantic consolidation and old-episode compaction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          note: Selected retained summaries are compressed/combined into reduced semantic observations
            or takeaways; originals may remain.
        records:
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        note: This is the implemented reduction path, not proof of semantic fidelity. A generated semantic
          novelty is not established merely by asking for a lesson.
      - scope: Explicit existing-row patches
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-memory-withdrawal
          - epistemic.md#epi-rte-memory-mutation
          note: Caller patches revise content/summary or metadata of an existing retained entry.
        records:
        - memory.md#mem-rte-memory-withdrawal
        - epistemic.md#epi-rte-memory-mutation
        note: The inspected patch is an actual revision mechanism; re-embedding and encryption coherence
          remain unresolved.
      - scope: Decay, contradiction downweighting and use/outcome importance reinforcement
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-local-dream
          - memory.md#mem-rte-belief-revision
          note: Local scheduled/CLI decay and contradiction-based decay reduction lower future reliance
            weights.
        - value: promote
          basis: wired
          records:
          - memory.md#mem-obj-local-store
          - memory.md#mem-rte-strategy-refinement
          note: JSON recall and positive same-feature reinforcement increase retained importance/salience.
        records:
        - memory.md#mem-rte-local-dream
        - memory.md#mem-rte-belief-revision
        - memory.md#mem-obj-local-store
        - memory.md#mem-rte-strategy-refinement
        note: These transformations alter selection state; they do not establish justified falsification
          or causal strategy efficacy.
      - scope: Delegated-access revocation retaining sealed content and portable record revocations
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-withdrawal
          note: Revocation withdraws provider reliance while preserving encrypted retained content.
        - value: invalidate
          basis: wired
          records:
          - epistemic.md#epi-rte-pack-verification
          note: Signed revocations mark retained portable records withdrawn for application filtering.
        records:
        - memory.md#mem-rte-memory-withdrawal
        - epistemic.md#epi-rte-pack-verification
        note: Local revocation is operative on inspected guards; portable filtering is application-dependent.
          Neither establishes global erasure.
      - scope: Generated rule/journal/resolution semantics and local dream queue operation names
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-belief-revision
        - memory.md#mem-rte-journal-continuity
        - memory.md#mem-rte-strategy-refinement
        - memory.md#mem-rte-local-dream
        note: Outputs are not inspected, so requested synthesis does not establish a new claim absent
          from inputs. Queue prompt names do not establish adopted consolidation/evolution. Additional
          curation cannot be determined.
      - scope: Remaining enrichment, shadow enforcement and portable/client maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-rte-shadow-reconcile
        - runtime.md#rt-rte-memory-entry
        - epistemic.md#epi-rte-pack-verification
        note: Index rebuilds, write duplicate guards and unapplied shadow update/noop proposals alone
          establish no additional operation. Uninspected alternatives prevent an exhaustive curation list.
      records:
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-memory-withdrawal
      - epistemic.md#epi-rte-memory-mutation
      - memory.md#mem-rte-local-dream
      - memory.md#mem-rte-belief-revision
      - memory.md#mem-obj-local-store
      - memory.md#mem-rte-strategy-refinement
      - epistemic.md#epi-rte-pack-verification
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-journal-continuity
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-rte-shadow-reconcile
      - runtime.md#rt-rte-memory-entry
      note: Retain implemented reduction, revision, downweighting, promotion and withdrawal. Neither acquisition
        nor a duplicate insertion check alone establishes dedup; no unsupported synthesis is added.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit SDK/MCP recall, summary/hydration, trace explanation and requested service returns
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-memory-entry
          - memory.md#mem-rte-recall-selection
          - memory.md#mem-rte-provenance-explanation
          - memory.md#mem-rte-response-memory
          note: A consumer requests retained records or memory-enabled generation and receives the requested
            return.
        records:
        - runtime.md#rt-rte-memory-entry
        - memory.md#mem-rte-recall-selection
        - memory.md#mem-rte-provenance-explanation
        - memory.md#mem-rte-response-memory
        note: Requested delivery is not counted again as push merely because code returns it.
      - scope: Automatic memory/history supply in chat and procedural supplementation inside response
          generation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - memory.md#mem-rte-response-memory
          - epistemic.md#epi-rte-strategy-consumption
          note: A chat request triggers owner-scoped recall/history fitting; opted-in response generation
            triggers an independent procedural selection without a request for each retained rule.
        records:
        - runtime.md#rt-rte-chat-turn
        - memory.md#mem-rte-response-memory
        - epistemic.md#epi-rte-strategy-consumption
        note: These automatic selectors supply retained parts to the generation model. They coexist with
          the outer requested response; no unsolicited background user message is asserted.
      - scope: Automatic source selection for recurring maintenance and journal contexts
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - memory.md#mem-rte-journal-continuity
          - epistemic.md#epi-rte-self-reflection
          - epistemic.md#epi-rte-action-learning
          note: Maintenance code selects retained episodes, prior self-model/journals and action experience
            for subsequent model/update invocations.
        records:
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-journal-continuity
        - epistemic.md#epi-rte-self-reflection
        - epistemic.md#epi-rte-action-learning
        note: Later update consumers receive selected retained material, not the full foreground chat
          frame.
      - scope: Snapshot supply to an external host
        assessment: known
        findings:
        - value: push
          basis: afforded
          records:
          - memory.md#mem-rte-prompt-sync
          note: Periodic/once snapshot selection writes memory for documented later symlink-based host
            loading.
        records:
        - memory.md#mem-rte-prompt-sync
        note: File production is wired but the host supply route remains an affordance, not inspected
          loading.
      - scope: Local queue-result adoption, portable/client consumers and remaining MCP host use
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-dream
        - epistemic.md#epi-rte-pack-verification
        - runtime.md#rt-rte-memory-entry
        note: Known requested APIs and available files do not establish every later consumer or delivery
          route. Queue results cannot be treated as pull-only or absent.
      records:
      - runtime.md#rt-rte-memory-entry
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-rte-provenance-explanation
      - memory.md#mem-rte-response-memory
      - runtime.md#rt-rte-chat-turn
      - epistemic.md#epi-rte-strategy-consumption
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-journal-continuity
      - epistemic.md#epi-rte-self-reflection
      - epistemic.md#epi-rte-action-learning
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-rte-local-dream
      - epistemic.md#epi-rte-pack-verification
      note: Request, automatic selection and return are separate operations. Wired automatic context supply
        coexists with requested pull; unresolved host/portable alternatives remain included.
    read_back_signal:
      assessment: partial
      units:
      - scope: Chat automatic memory retrieval and conversation-history fitting
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - memory.md#mem-rte-recall-selection
          note: Chat input triggers semantic recall using query embeddings to select retained text.
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          note: Conversation/owner identity matches select the retained conversation rows and owner scope
            actually supplied to the model.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          note: Fetched-prefix, count limits, type rendering and heuristic budgets filter supplied history/memories.
        records:
        - runtime.md#rt-rte-chat-turn
        - memory.md#mem-rte-recall-selection
        note: Triggers are authenticated messages; inputs are current text, owner/conversation IDs and
          budgets. Expansion is skipped; no universal lexical lane is inferred for this call.
      - scope: Automatic procedural supplementation at memory-enabled shared responses
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-response-memory
          - epistemic.md#epi-rte-strategy-consumption
          note: Presence of memory options triggers procedural type, importance threshold and top-three
            selection; selected rules supplement the query result.
        records:
        - memory.md#mem-rte-response-memory
        - epistemic.md#epi-rte-strategy-consumption
        note: General strategy slots are coarse selection, not identifier targeting. Reranker alternatives
          in enhanced recall remain unresolved below.
      - scope: Main/hosted maintenance, self-model/journal continuity and action refinement source windows
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - memory.md#mem-rte-journal-continuity
          - epistemic.md#epi-rte-self-reflection
          - epistemic.md#epi-rte-action-learning
          note: Time/type/importance/count/rate predicates select retained episodes, journals, self-model
            and action groups at maintenance triggers.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-dream-compaction
          - epistemic.md#epi-rte-action-learning
          note: First-concept grouping and matching retained action feature tags select source groups
            and same-feature strategy rows for updates.
        records:
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-journal-continuity
        - epistemic.md#epi-rte-self-reflection
        - epistemic.md#epi-rte-action-learning
        note: The matched concept/feature actually selects retained parts. Journal divergence and contradiction-pair
          provider internals are not characterized by these coarse witnesses.
      - scope: Snapshot export selection for afforded later host supply
        assessment: known
        findings:
        - value: coarse
          basis: afforded
          records:
          - memory.md#mem-rte-prompt-sync
          note: Timer/once refresh selects type-specific importance/recency/count-bounded bullets.
        records:
        - memory.md#mem-rte-prompt-sync
        note: The signal describes the afforded host-supply chain; file replacement itself is wired.
      - scope: Enhanced reranking, journal divergence, contradiction-pair selectors and opaque delivery
          alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-response-memory
        - memory.md#mem-rte-journal-continuity
        - memory.md#mem-rte-belief-revision
        - memory.md#mem-rte-local-dream
        - epistemic.md#epi-rte-pack-verification
        - runtime.md#rt-rte-memory-entry
        note: Not all selector internals or downstream consumers were inspected; inferred judgment/lexical/embedding
          alternatives cannot be exhaustively classified.
      records:
      - runtime.md#rt-rte-chat-turn
      - memory.md#mem-rte-recall-selection
      - memory.md#mem-rte-response-memory
      - epistemic.md#epi-rte-strategy-consumption
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-journal-continuity
      - epistemic.md#epi-rte-self-reflection
      - epistemic.md#epi-rte-action-learning
      - memory.md#mem-rte-prompt-sync
      - memory.md#mem-rte-belief-revision
      - memory.md#mem-rte-local-dream
      - epistemic.md#epi-rte-pack-verification
      - runtime.md#rt-rte-memory-entry
      note: Signals characterize actual automatic selection operations, not IDs printed on requested records.
        Coarse filtering remains separate from identity matching and semantic selection.
    trace_learning:
      assessment: partial
      units:
      - scope: Chat-experience to main/hosted semantic and procedural memory, self-model and journal continuity
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          - memory.md#mem-rte-journal-continuity
          - epistemic.md#epi-rte-self-reflection
          - memory.md#mem-rte-response-memory
          note: Retained experience feeds automatic durable derived prose that can reach later answering
            and recurring maintenance consumers.
        records:
        - runtime.md#rt-rte-chat-turn
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-journal-continuity
        - epistemic.md#epi-rte-self-reflection
        - memory.md#mem-rte-response-memory
        note: The complete raw-to-derived-to-later-consumer wiring qualifies without observed improvement;
          prior shortened summaries may lose reasons.
      - scope: Action/outcome feedback to procedural rules and durable strategy importance
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - epistemic.md#epi-rte-action-learning
          - memory.md#mem-rte-strategy-refinement
          - memory.md#mem-bap-procedural-guidance
          - memory.md#mem-rte-response-memory
          note: Recorded actions and measured outcomes automatically produce retained guidance/ranking
            changes, with later procedural prompt consumption.
        records:
        - epistemic.md#epi-rte-action-learning
        - memory.md#mem-rte-strategy-refinement
        - memory.md#mem-bap-procedural-guidance
        - memory.md#mem-rte-response-memory
        note: Metric provenance and causal efficacy remain limited; qualifying trace-fed writes do not
          require proven behavioral benefit.
      - scope: Local dream queue-result route
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-local-dream
        - memory.md#mem-obj-sqlite-store
        note: Generation and retention are wired but no later adoption/consumer is established in the
          completion sink. That missing consumer prevents either a positive chain or a bounded negative.
      - scope: Mixed upload/import inputs, retrieval feedback origins and remaining social/client/portable
          writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-upload-extraction
        - runtime.md#rt-rte-pack-import
        - memory.md#mem-obj-retrieval-state
        - memory.md#mem-obj-local-store
        - runtime.md#rt-rte-memory-entry
        - epistemic.md#epi-rte-pack-verification
        note: Document content, complete trace origin and all later behavior-shaping consumers are not
          recorded for every route. Raw capture or metadata change alone is not generalized into qualifying
          trace learning.
      records:
      - runtime.md#rt-rte-chat-turn
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - memory.md#mem-rte-journal-continuity
      - epistemic.md#epi-rte-self-reflection
      - memory.md#mem-rte-response-memory
      - epistemic.md#epi-rte-action-learning
      - memory.md#mem-rte-strategy-refinement
      - memory.md#mem-bap-procedural-guidance
      - memory.md#mem-rte-local-dream
      - memory.md#mem-obj-sqlite-store
      - memory.md#mem-rte-upload-extraction
      - runtime.md#rt-rte-pack-import
      - memory.md#mem-obj-retrieval-state
      - memory.md#mem-obj-local-store
      - runtime.md#rt-rte-memory-entry
      - epistemic.md#epi-rte-pack-verification
      note: Positive wired trace-learning routes coexist with unresolved alternatives. There is no bounded
        absence record supporting a local or whole-system no.
    trace_source:
      assessment: partial
      units:
      - scope: Conversational input on qualifying main/hosted episode-derived routes
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-chat-turn
          - runtime.md#rt-rte-dream-cycle
          - memory.md#mem-rte-dream-compaction
          - memory.md#mem-rte-hosted-dream
          note: Recorded user/assistant exchanges enter episodic memory and feed subsequent durable semantic/procedural
            transformations.
        records:
        - runtime.md#rt-rte-chat-turn
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-dream-compaction
        - memory.md#mem-rte-hosted-dream
        note: This identifies the known conversational branch; arbitrary episodic labels do not establish
          all source origins.
      - scope: Qualifying social action/outcome strategy route
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records:
          - epistemic.md#epi-rte-action-learning
          - memory.md#mem-rte-strategy-refinement
          note: Recorded action events and later timestamp/age-gated social metrics feed the automatic
            rule and importance update.
        records:
        - epistemic.md#epi-rte-action-learning
        - memory.md#mem-rte-strategy-refinement
        note: The source is runtime/environmental action/outcome evidence, not tool traces merely because
          APIs transport metrics. Feature aggregates do not establish linked multi-step trajectories.
      - scope: Mixed episode/semantic/self-model/journal inputs on qualifying updates
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-dream-cycle
        - memory.md#mem-rte-hosted-dream
        - memory.md#mem-rte-journal-continuity
        - epistemic.md#epi-rte-self-reflection
        - epistemic.md#epi-rte-action-learning
        note: Known conversational and event branches do not resolve original provenance of every seed,
          prior derived summary or action report. All qualifying-source enumeration remains incomplete.
      - scope: Unresolved local queue, upload/import and other potential qualifying routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-local-dream
        - memory.md#mem-rte-upload-extraction
        - runtime.md#rt-rte-pack-import
        - runtime.md#rt-rte-memory-entry
        - epistemic.md#epi-rte-pack-verification
        note: A later consumer or qualifying trace input is not established on these alternatives. Trace-source
          inapplicability cannot follow from that uncertainty.
      records:
      - runtime.md#rt-rte-chat-turn
      - runtime.md#rt-rte-dream-cycle
      - memory.md#mem-rte-dream-compaction
      - memory.md#mem-rte-hosted-dream
      - epistemic.md#epi-rte-action-learning
      - memory.md#mem-rte-strategy-refinement
      - memory.md#mem-rte-journal-continuity
      - epistemic.md#epi-rte-self-reflection
      - memory.md#mem-rte-local-dream
      - memory.md#mem-rte-upload-extraction
      - runtime.md#rt-rte-pack-import
      - runtime.md#rt-rte-memory-entry
      - epistemic.md#epi-rte-pack-verification
      note: Source classification follows original content rather than serialization or adapter role.
        Known sessions and social events do not imply tool traces or trajectories, nor complete coverage.
---

# Cludebot memory profile

## Comparison rationale

This profile classifies accepted records, not source files or observed runs. All positive mechanisms are implementation-grounded unless their own finding says afforded. All ten axes remain partial: inspected witnesses do not enumerate every included portable, client, initial-admission or later-consumer alternative. Inference weights are not accumulated memory merely because retained text passes through an inference model. Dense retained embeddings do have distributed-parametric form; their relational/vector storage is a separate classification ([MEM-OBJ-retrieval-state](memory.md#mem-obj-retrieval-state)).

Canonical references resolve the supplied reconciliation's supersessions: stored content uses [MEM-OBJ-memories](memory.md#mem-obj-memories); main compaction uses [MEM-RTE-dream-compaction](memory.md#mem-rte-dream-compaction); contradiction handling uses [MEM-RTE-belief-revision](memory.md#mem-rte-belief-revision); hosted and local queue processing use [MEM-RTE-hosted-dream](memory.md#mem-rte-hosted-dream) and [MEM-RTE-local-dream](memory.md#mem-rte-local-dream). These mappings affect substrate, form, lineage, control, curation and trace-route classification without upgrading either analyst's evidence. The main cycle remains a valid container. Action measurement/refinement and shared-response/procedural consumption are overlapping but distinct routes, not duplicates.

Pull and push refer to different operations in a chain. A requested SDK return is pull. Automatic history/memory selection supplies the chat model without that model requesting individual records. Independent procedural supplementation similarly pushes selected rules into a requested generation; it is not an unsolicited user-facing background response ([RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn), [MEM-RTE-response-memory](memory.md#mem-rte-response-memory)). Snapshot generation is wired, but its later host supply remains only afforded ([MEM-RTE-prompt-sync](memory.md#mem-rte-prompt-sync)). No identifier signal follows just from an ID printed on returned data.

Curation classification follows transformation, not epistemic success. Main compaction reduces retained summaries even though fidelity and its hash pointer are unverified. Contradiction handling demonstrably downweights a source but does not implement a content-directed truth veto. Generated rules, journals and resolutions without inspected output instances do not establish synthesis of a new claim. Write duplicate checks and index construction alone do not establish deduplication ([MEM-RTE-dream-compaction](memory.md#mem-rte-dream-compaction), [MEM-RTE-belief-revision](memory.md#mem-rte-belief-revision), [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry)).

Retained experience has learning authority at the automatic artifact-update consumer, while produced rules have instruction authority at the later response model. This supports wired trace learning, not demonstrated capacity improvement or exercised self-improvement. Conversational exchanges establish session-log input; social action/outcome records establish event-stream input. Mixed seeds and incompletely traced input origins prevent complete source coverage ([EPI-RTE-action-learning](epistemic.md#epi-rte-action-learning), [MEM-RTE-journal-continuity](memory.md#mem-rte-journal-continuity), [MEM-BAP-procedural-guidance](memory.md#mem-bap-procedural-guidance)). SQLite queue completion lacks the recorded later consumer required for the same positive classification; it supplies neither an absence nor an inapplicability warrant.

Stored access controls have enforcing force on inspected guarded reads; a redelegation key is checked against retained encrypted content, giving that content a validation role. These are not factual validation or all-lane erasure. Portable revocation retains records and delegates filtering to applications, so universal enforcement is unresolved ([MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal), [EPI-RTE-pack-verification](epistemic.md#epi-rte-pack-verification)). Generic caller identity supplies no explicit human content-decision witness for manual agency. Model-written task findings instead have automatic admission ([WF-RTE-store-finding](workflow.md#wf-rte-store-finding)).

The reconciliation's pre-loop dashboard-recovery attribution conflict does not determine any memory value: this profile uses the distinct finding-write record, not an asserted shared recovery guarantee. No source reads were made; all warrants and limits come from the supplied members and their records. No new records, quotations, execution evidence or verification judgments are introduced.
