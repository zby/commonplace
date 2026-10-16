---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Mem0 memory profile: retained facts, raw context, indexes, configuration and shipped recall/capture
  routes, with hosted and uninspected alternatives unresolved.'
run-id: AAS-2026-10-14-mem0-5b642a1731b4-01
source-identity: https://github.com/mem0ai/mem0
reviewed-boundary: 0724291bd864cf807e88ee8981c8226644e8fb42
memory-comparison:
  version: 2
  scope: Accumulated Python and TypeScript memory text and access structures; Python recent messages/history;
    coding-agent evidence/checkpoint/retrieval state; service-held memories as exposed by clients; installed
    extraction-guidance overrides; inspected OpenClaw, Claude Code, Pi and Hermes write/maintenance/later-consumer
    paths. Includes unresolved hosted internals, optional stores, other coding adapters, async/provider
    variants and CLI/framework/dashboard consumers named by the accepted inventory. Excludes external
    provider weights/implementations, native host compaction, unavailable evaluator contents and shipped
    static prompts/protocols as memory objects; those may describe included mechanisms.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Python fact text, access payload, dense vectors and entity collection
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory-data
          - memory.md#mem-obj-memory-access
          - memory.md#mem-obj-memory-vectors
          - memory.md#mem-obj-entity-links
          note: These operative parts reside in configured vector collections; entity links do not establish
            graph storage.
        records: *id001
        note: These operative parts reside in configured vector collections; entity links do not establish
          graph storage.
      - scope: Python recent messages and mutation history
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-messages
          - memory.md#mem-obj-history
          note: Separate SQLite tables retain raw context and old/new text plus event metadata.
        records: *id002
        note: Separate SQLite tables retain raw context and old/new text plus event metadata.
      - scope: Claude Code raw evidence, flush and retrieval bookkeeping
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-evidence-store
          note: Local evidence.sqlite3 stores event payloads and retrieval copies; it is not the remote
            derived store.
        records: *id003
        note: Local evidence.sqlite3 stores event payloads and retrieval copies; it is not the remote
          derived store.
      - scope: Persisted server configuration overrides including extraction guidance
        assessment: known
        findings:
        - value: rdbms
          basis: wired
          records: &id004
          - runtime.md#rt-obj-config-overrides
          - runtime.md#rt-obj-custom-instructions
          note: Settings rows retain override JSON; database persistence is attempted and can fail.
        records: *id004
        note: Settings rows retain override JSON; database persistence is attempted and can fail.
      - scope: Pi session seen-ID state
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id005
          - memory.md#mem-rte-pi-memory
          note: Session-local selection state accumulates through recalls and resets at session start;
            this does not imply durable fact storage.
        records: *id005
        note: Session-local selection state accumulates through recalls and resets at session start; this
          does not imply durable fact storage.
      - scope: Hosted retained memories as exposed service objects
        assessment: partial
        findings:
        - value: service-object
          basis: afforded
          records: &id006
          - runtime.md#rt-rte-hosted-client
          - memory.md#mem-rte-coding-recall
          note: Clients afford retained objects retrievable by search/get; backend substrate and actual
            persistence remain opaque. This is not a vector-store inference.
        records: *id006
        note: Clients afford retained objects retrievable by search/get; backend substrate and actual
          persistence remain opaque. This is not a vector-store inference.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: &id012
        - runtime.md#rt-rte-hosted-client
        - memory.md#mem-rte-typescript-memory
        - memory.md#mem-rte-pi-memory
        - memory.md#mem-rte-hermes-memory
        - memory.md#mem-rte-coding-flush
        note: Alternative history substrates, non-default adapters and remote physical persistence are
          not classified by accepted records; no exhaustive substrate union is established.
      records:
      - memory.md#mem-obj-memory-data
      - memory.md#mem-obj-memory-access
      - memory.md#mem-obj-memory-vectors
      - memory.md#mem-obj-entity-links
      - memory.md#mem-obj-messages
      - memory.md#mem-obj-history
      - memory.md#mem-obj-evidence-store
      - runtime.md#rt-obj-config-overrides
      - runtime.md#rt-obj-custom-instructions
      - memory.md#mem-rte-pi-memory
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-rte-typescript-memory
      - memory.md#mem-rte-hermes-memory
      - memory.md#mem-rte-coding-flush
      note: Known local stores coexist with an exposed service-object boundary and unresolved physical/provider
        alternatives. Model weights and shipped repository prompts are production dependencies, not accumulated
        memory substrates here.
    representational_form:
      assessment: partial
      units:
      - scope: Python fact and procedural text; recent-message content; history text; coding evidence
          and recall text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-memory-data
          - memory.md#mem-obj-procedural-memory
          - memory.md#mem-obj-messages
          - memory.md#mem-obj-history
          - memory.md#mem-obj-evidence-store
          - memory.md#mem-rte-coding-recall
          note: Text reaches model interpretation or requesting inspection consumers, separated from its
            access columns.
        records: *id007
        note: Text reaches model interpretation or requesting inspection consumers, separated from its
          access columns.
      - scope: Python access fields, message/history columns and entity links; coding flush/retrieval
          state; Pi seen IDs; server settings structure
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-memory-access
          - memory.md#mem-obj-messages
          - memory.md#mem-obj-history
          - memory.md#mem-obj-entity-links
          - memory.md#mem-obj-evidence-store
          - memory.md#mem-rte-pi-memory
          - runtime.md#rt-obj-config-overrides
          note: Localized fields drive fixed filtering, matching, checkpoint and configuration rules;
            readable entity labels and retrieval copies are not collapsed into these fields.
        records: *id008
        note: Localized fields drive fixed filtering, matching, checkpoint and configuration rules; readable
          entity labels and retrieval copies are not collapsed into these fields.
      - scope: Retained memory and entity embeddings at similarity consumers
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id009
          - memory.md#mem-obj-memory-vectors
          - memory.md#mem-obj-entity-links
          note: Distributed dense representations supply similarity, not localized propositions or newly
            trained model weights.
        records: *id009
        note: Distributed dense representations supply similarity, not localized propositions or newly
          trained model weights.
      - scope: Custom extraction instruction text at extraction consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - runtime.md#rt-obj-custom-instructions
          note: The guidance is interpreted language within otherwise symbolic settings.
        records: *id010
        note: The guidance is interpreted language within otherwise symbolic settings.
      - scope: Hosted fact display text at coding/Pi/Hermes recall consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          note: Inspected formatting delivers memory strings; this classifies delivered text, not the
            opaque complete hosted payload.
        records: *id011
        note: Inspected formatting delivers memory strings; this classifies delivered text, not the opaque
          complete hosted payload.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Opaque backend payloads and unread provider/adapter parts prevent complete form coverage;
          inspected text displays do not resolve them.
      records:
      - memory.md#mem-obj-memory-data
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-obj-messages
      - memory.md#mem-obj-history
      - memory.md#mem-obj-evidence-store
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-obj-memory-access
      - memory.md#mem-obj-entity-links
      - memory.md#mem-rte-pi-memory
      - runtime.md#rt-obj-config-overrides
      - memory.md#mem-obj-memory-vectors
      - runtime.md#rt-obj-custom-instructions
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      - memory.md#mem-rte-coding-flush
      note: Text, fixed-rule metadata and dense representations remain separate operative parts. No parametric
        finding is inferred for opaque hosted payloads.
    lineage:
      assessment: partial
      units:
      - scope: Conversation extraction and procedural-summary derivation paths
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - runtime.md#rt-rte-extract-add
          - memory.md#mem-obj-procedural-memory
          - memory.md#mem-rte-coding-flush
          - memory.md#mem-rte-hermes-memory
          - memory.md#mem-rte-pi-memory
          note: Software/model routes derive retained text from conversational activity. This describes
            derivation, not verified original authorship or remote semantic fidelity.
        records: *id013
        note: Software/model routes derive retained text from conversational activity. This describes
          derivation, not verified original authorship or remote semantic fidelity.
      - scope: Raw non-system message insertion and CLI file-content acquisition
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id014
          - runtime.md#rt-rte-direct-write
          - epistemic.md#epi-rte-cli-import
          note: Existing caller/file text is acquired; wrapping it as a user message neither establishes
            human authorship nor a trace origin.
        records: *id014
        note: Existing caller/file text is acquired; wrapping it as a user message neither establishes
          human authorship nor a trace origin.
      - scope: Hashes, lemmatized terms, vectors and entity-index derivations
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - memory.md#mem-obj-memory-access
          - memory.md#mem-obj-memory-vectors
          - memory.md#mem-obj-entity-links
          - epistemic.md#epi-rte-keyword-index
          note: These representations are computed from text for access. Embedding derivation is known
            while encoder training provenance remains unresolved.
        records: *id015
        note: These representations are computed from text for access. Embedding derivation is known while
          encoder training provenance remains unresolved.
      - scope: Initial input authorship, explicit replacement and installed custom-instruction origin
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-data
        - runtime.md#rt-obj-custom-instructions
        - runtime.md#rt-rte-runtime-config
        note: Caller/admin proposal alone does not establish authored content rather than imported or
          generated content; initial provenance is unresolved.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Hosted internal derivations, optional stores and unread admission routes are not enumerated;
          embedding upstream provenance also prevents complete lineage coverage.
      records:
      - runtime.md#rt-rte-extract-add
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-rte-coding-flush
      - memory.md#mem-rte-hermes-memory
      - memory.md#mem-rte-pi-memory
      - runtime.md#rt-rte-direct-write
      - epistemic.md#epi-rte-cli-import
      - memory.md#mem-obj-memory-access
      - memory.md#mem-obj-memory-vectors
      - memory.md#mem-obj-entity-links
      - epistemic.md#epi-rte-keyword-index
      - memory.md#mem-obj-memory-data
      - runtime.md#rt-obj-custom-instructions
      - runtime.md#rt-rte-runtime-config
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      note: Derivation and acquisition positives do not settle initial authorship. No authored finding
        is inferred merely from a caller supplying text.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Fact and procedural text at README answer model and host recall consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id016
          - runtime.md#rt-bap-answer-context
          - memory.md#mem-obj-procedural-memory
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          - runtime.md#rt-rte-openclaw-hooks
          note: Selected text supplies reference/context to later models; system-message placement alone
            does not make each fact a standing instruction.
        records: *id016
        note: Selected text supplies reference/context to later models; system-message placement alone
          does not make each fact a standing instruction.
      - scope: Accumulated custom extraction instructions at extraction model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id017
          - runtime.md#rt-obj-custom-instructions
          - runtime.md#rt-rte-runtime-config
          note: Installed guidance shapes subsequent extraction requests; generated proposals have no
            installed force until separately submitted.
        records: *id017
        note: Installed guidance shapes subsequent extraction requests; generated proposals have no installed
          force until separately submitted.
      - scope: Retained prior messages and existing fact context at extraction update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id018
          - memory.md#mem-obj-messages
          - runtime.md#rt-bap-extraction-context
          - runtime.md#rt-rte-extract-add
          note: Experience/context influences a later automatic fact-producing write. Learning authority
            here does not establish improved capacity or weight updates.
        records: *id018
        note: Experience/context influences a later automatic fact-producing write. Learning authority
          here does not establish improved capacity or weight updates.
      - scope: Stored fact text, embeddings, keyword terms and entity links at search scoring
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id019
          - memory.md#mem-obj-memory-data
          - memory.md#mem-obj-memory-vectors
          - memory.md#mem-obj-entity-links
          - epistemic.md#epi-rte-keyword-index
          - epistemic.md#epi-rte-memory-selection
          note: Retained content and features affect relative priority under fixed similarity/lexical/entity
            scoring; retained ranking policy is unnecessary.
        records: *id019
        note: Retained content and features affect relative priority under fixed similarity/lexical/entity
          scoring; retained ranking policy is unnecessary.
      - scope: Scope fields and local checkpoint/status state at selection and flush assembly
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id020
          - memory.md#mem-obj-memory-access
          - memory.md#mem-obj-evidence-store
          - memory.md#mem-rte-coding-flush
          note: Stored scopes and event ranges/status choose retained inputs and submission/retry windows.
        records: *id020
        note: Stored scopes and event ranges/status choose retained inputs and submission/retry windows.
      - scope: Retained hashes at candidate admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-memory-access
          - epistemic.md#epi-rte-extraction-checks
          note: Stored hash membership is an admission criterion.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-memory-access
          - epistemic.md#epi-rte-extraction-checks
          note: A matching retained hash causes the insertion loop to skip the proposal.
        records:
        - memory.md#mem-obj-memory-access
        - epistemic.md#epi-rte-extraction-checks
        note: Existing hashes supply both a conformance criterion and a veto; this checks bounded identity,
          not truth.
      - scope: Expiry metadata and accumulated seen IDs at delivery filters
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id021
          - memory.md#mem-obj-memory-access
          - epistemic.md#epi-rte-memory-selection
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          note: Expiry excludes default public search results; seen IDs veto re-delivery. Direct ID and
            extraction counterpaths remain; this is not universal suppression.
        records: *id021
        note: Expiry excludes default public search results; seen IDs veto re-delivery. Direct ID and
          extraction counterpaths remain; this is not universal suppression.
      - scope: Already-shown memory ID set at recall eligibility check
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id022
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          note: Membership determines eligibility for another injection as well as enforcing its exclusion;
            it is not content-truth validation.
        records: *id022
        note: Membership determines eligibility for another injection as well as enforcing its exclusion;
          it is not content-truth validation.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Hosted internal consumers and unread integration/admission routes have unresolved forces;
          metadata with no recorded consumer is assigned none, not assumed powerless everywhere.
      records:
      - runtime.md#rt-bap-answer-context
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-obj-custom-instructions
      - runtime.md#rt-rte-runtime-config
      - memory.md#mem-obj-messages
      - runtime.md#rt-bap-extraction-context
      - runtime.md#rt-rte-extract-add
      - memory.md#mem-obj-memory-data
      - memory.md#mem-obj-memory-vectors
      - memory.md#mem-obj-entity-links
      - epistemic.md#epi-rte-keyword-index
      - epistemic.md#epi-rte-memory-selection
      - memory.md#mem-obj-memory-access
      - memory.md#mem-obj-evidence-store
      - memory.md#mem-rte-coding-flush
      - epistemic.md#epi-rte-extraction-checks
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      note: Each force is local to an actual consumer. Retained experience at an update consumer and derived
        fact text at an answer consumer have distinct learning and knowledge paths; no blanket equivalence
        is asserted.
    write_agency:
      assessment: partial
      units:
      - scope: Inferred extraction, procedural summary, raw message-tail save and index/history writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id023
          - runtime.md#rt-rte-extract-add
          - memory.md#mem-obj-procedural-memory
          - memory.md#mem-obj-messages
          - memory.md#mem-obj-history
          - memory.md#mem-obj-memory-vectors
          note: Software/model admission lacks per-content human approval. Triggering add does not make
            its subsequent admissions manual.
        records: *id023
        note: Software/model admission lacks per-content human approval. Triggering add does not make
          its subsequent admissions manual.
      - scope: OpenClaw foreground-agent fact admission and legacy capture
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id024
          - runtime.md#rt-rte-openclaw-add
          - runtime.md#rt-rte-openclaw-hooks
          note: Agent fact choice and callback filtering/admission are computational; host scheduling
            is not a human decision approving each fact.
        records: *id024
        note: Agent fact choice and callback filtering/admission are computational; host scheduling is
          not a human decision approving each fact.
      - scope: Coding checkpoint assembly, Pi capture and Hermes trace sync
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - memory.md#mem-rte-coding-flush
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          note: Adapters select/redact and submit traces without mandatory per-memory human review; remote
            internal selection remains opaque.
        records: *id025
        note: Adapters select/redact and submit traces without mandatory per-memory human review; remote
          internal selection remains opaque.
      - scope: Generic direct/raw insertion, explicit replacement, CLI file selection and server override
          installation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-write
        - epistemic.md#epi-rte-cli-import
        - runtime.md#rt-rte-runtime-config
        note: Caller/admin initiation and permission do not reveal whether a human supplied or approved
          the retained content. Known software I/O is not enough to classify these content-control decisions.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Other adapters, explicit Pi tools and remote admission decisions lack complete recorded
          control facts; automatic witnesses do not establish a universal admission policy.
      records:
      - runtime.md#rt-rte-extract-add
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-obj-messages
      - memory.md#mem-obj-history
      - memory.md#mem-obj-memory-vectors
      - runtime.md#rt-rte-openclaw-add
      - runtime.md#rt-rte-openclaw-hooks
      - memory.md#mem-rte-coding-flush
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-direct-write
      - epistemic.md#epi-rte-cli-import
      - runtime.md#rt-rte-runtime-config
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      note: Automatic mechanisms are positively wired; no manual value is established merely from a generic
        caller or admin role.
    curation_operations:
      assessment: partial
      units:
      - scope: Local Python conversation-to-standing-fact and procedural-summary transformations
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id026
          - runtime.md#rt-rte-extract-add
          - memory.md#mem-obj-procedural-memory
          note: Inspected local extraction and summarization select/compress existing conversational
            claims for later use; this warrant excludes the hosted coding-checkpoint transformation.
        records: *id026
        note: Local implementation establishes consolidation, not instance-level semantic fidelity
          or a hosted transformation.
      - scope: Hosted derivation from coding-agent checkpoint submissions
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-coding-flush
        note: Checkpoint selection, redaction and inferred-add submission are wired, but the remote
          derived representation and admission are unavailable. Instructions request durable facts
          and completed decisions; they do not establish the hosted curation transformation. No
          controlled operation is assigned to that opaque transformation.
      - scope: Retrieved/batch hash duplicate suppression in Python and TypeScript
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id027
          - epistemic.md#epi-rte-extraction-checks
          - memory.md#mem-rte-typescript-memory
          note: Exact duplicate candidates are removed from admission within the retrieved pool/current
            batch; this is not a global uniqueness index.
        records: *id027
        note: Exact duplicate candidates are removed from admission within the retrieved pool/current
          batch; this is not a global uniqueness index.
      - scope: Python explicit ID-preserving text replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id028
          - runtime.md#rt-rte-direct-write
          - memory.md#mem-obj-history
          note: An existing entry is revised and re-embedded, with attempted old/new history. Cross-store
            atomicity is not established.
        records: *id028
        note: An existing entry is revised and re-embedded, with attempted old/new history. Cross-store
          atomicity is not established.
      - scope: Python vector deletion retaining old text in mutation history
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id029
          - runtime.md#rt-rte-direct-write
          - memory.md#mem-obj-history
          note: The current vector entry is withdrawn while history retains its old claim. Raw messages
            and copied contexts can survive.
        records: *id029
        note: The current vector entry is withdrawn while history retains its old claim. Raw messages
          and copied contexts can survive.
      - scope: Recent-message tail eviction and expiry-driven public visibility
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id030
          - memory.md#mem-obj-messages
          - epistemic.md#epi-rte-memory-selection
          note: Older raw rows are deleted beyond ten; expired payloads are forgotten by default public
            search, not erased or excluded from every consumer.
        records: *id030
        note: Older raw rows are deleted beyond ten; expired payloads are forgotten by default public
          search, not erased or excluded from every consumer.
      - scope: Active extraction prompt prescribed cessation inference
        assessment: known
        findings:
        - value: synthesize
          basis: claimed
          records: &id031
          - epistemic.md#epi-clm-evidence-bound
          note: Doctrine prescribes inferring no-longer-loves from used-to-love, a claim not entailed
            by that sentence. This is a claimed transformation, not observed production or a wired guarantee
            of novel truth.
        records: *id031
        note: Doctrine prescribes inferring no-longer-loves from used-to-love, a claim not entailed by
          that sentence. This is a claimed transformation, not observed production or a wired guarantee
          of novel truth.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Hosted transformations, full OpenClaw TTL translation and unread maintenance variants prevent
          exhaustive curation classification; no promote operation is inferred from ranking or category
          labels.
      records:
      - runtime.md#rt-rte-extract-add
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-rte-coding-flush
      - epistemic.md#epi-rte-extraction-checks
      - memory.md#mem-rte-typescript-memory
      - runtime.md#rt-rte-direct-write
      - memory.md#mem-obj-history
      - memory.md#mem-obj-messages
      - epistemic.md#epi-rte-memory-selection
      - epistemic.md#epi-clm-evidence-bound
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      note: Curation values describe transformations rather than command names. Claimed synthesis stays
        separate from implemented consolidation/dedup/revision; instance-level semantic relation remains
        unresolved without input/output evidence.
    read_back_direction:
      assessment: partial
      units:
      - scope: README search, extraction context request and explicit ID/history/search tools
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id032
          - runtime.md#rt-rte-chat-memories
          - runtime.md#rt-rte-extract-add
          - runtime.md#rt-rte-direct-write
          - memory.md#mem-obj-history
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-hermes-memory
          note: Consumers request retained material. The backend return fulfilling a hook search is also
            pull at that backend boundary, not a second automatic push.
        records: *id032
        note: Consumers request retained material. The backend return fulfilling a hook search is also
          pull at that backend boundary, not a second automatic push.
      - scope: Automatic OpenClaw/Pi/coding first-prompt/Hermes prompt-time supply
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id033
          - runtime.md#rt-rte-openclaw-hooks
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-hermes-memory
          note: Host events/current prompts trigger selectors that supply recalled facts without an explicit
            memory request from the receiving model; external host invocation remains conditional.
        records: *id033
        note: Host events/current prompts trigger selectors that supply recalled facts without an explicit
          memory request from the receiving model; external host invocation remains conditional.
      - scope: Coding sidekick start delivery of selected parent recall snapshot
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-obj-evidence-store
          note: Start code automatically supplies stored injected-memory text for the tracked parent session,
            not the whole parent conversation.
        records: *id034
        note: Start code automatically supplies stored injected-memory text for the tracked parent session,
          not the whole parent conversation.
      - scope: Hosted API retained-object retrieval contract
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records: &id035
          - runtime.md#rt-rte-hosted-client
          note: Later service search/get is afforded; wrappers do not establish remote persistence or
            all later consumers.
        records: *id035
        note: Later service search/get is afforded; wrappers do not establish remote persistence or all
          later consumers.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Unread consumers and backend alternatives prevent a complete direction inventory. The proxy
          recall branch is incompatible and is not counted as successful delivered read-back.
      records:
      - runtime.md#rt-rte-chat-memories
      - runtime.md#rt-rte-extract-add
      - runtime.md#rt-rte-direct-write
      - memory.md#mem-obj-history
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-openclaw-hooks
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-obj-evidence-store
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      - memory.md#mem-rte-coding-flush
      note: Pull requests and automatic host supply coexist at different operations in the same chain;
        neither eliminates the other.
    read_back_signal:
      assessment: partial
      units:
      - scope: OpenClaw automatic prompt-build recall
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-openclaw-hooks
          note: User/session scope and category/importance/count/budget rules further select the delivered
            memories.
        records:
        - runtime.md#rt-rte-openclaw-hooks
        note: Interactive non-bootstrap prompt triggers provider semantic search followed by scope/category/importance/relevance
          filtering and approximate budget over retained fact text.
      - scope: Coding first-prompt, Pi before-agent-start and Hermes query prefetch
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          note: Scope, query identity, category/run/count and format limits bound selected fact text.
        records:
        - memory.md#mem-rte-coding-recall
        - memory.md#mem-rte-pi-memory
        - memory.md#mem-rte-hermes-memory
        note: Current prompt/query triggers scoped backend search and automatic context supply. Accepted
          records establish query/scope/top-k/seen-ID/format limits, not the opaque remote relevance algorithm.
      - scope: Pi and coding recall already-shown ID exclusion
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id036
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-coding-recall
          note: Automatic prompt recall matches candidate memory IDs against accumulated seen/retrieval
            state to select unseen delivered facts; IDs on ordinary requested gets are not counted.
        records: *id036
        note: Automatic prompt recall matches candidate memory IDs against accumulated seen/retrieval
          state to select unseen delivered facts; IDs on ordinary requested gets are not counted.
      - scope: Sidekick start selection of parent injected-memory snapshots
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id037
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-obj-evidence-store
          note: At sidekick start, tracked parent session/repository identity selects its stored injected-memory
            text for supply; this is an actual identity-matched delivery route.
        records: *id037
        note: At sidekick start, tracked parent session/repository identity selects its stored injected-memory
          text for supply; this is an actual identity-matched delivery route.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Opaque remote relevance selectors and unread push branches prevent complete signal coverage;
          no inferred-lexical or inferred-judgment push is inferred from Python public search or extraction
          model admission.
      records:
      - runtime.md#rt-rte-openclaw-hooks
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      - memory.md#mem-obj-evidence-store
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      - memory.md#mem-rte-coding-flush
      note: Push selection is not inapplicable because concrete push routes exist. Backend query affordances
        do not resolve exact algorithms; identifier suppression is distinct from coarse budgets and identity-matched
        snapshot delivery.
    trace_learning:
      assessment: partial
      units:
      - scope: Python inferred conversational facts and procedural continuation summaries with later extraction/answer
          use
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id038
          - runtime.md#rt-rte-extract-add
          - runtime.md#rt-rte-chat-memories
          - runtime.md#rt-bap-extraction-context
          - memory.md#mem-obj-procedural-memory
          note: Automatic conversation-fed writes produce retained context/summary text available to later
            consumers. Durable behavior-shaping here means later model input, not learned weights or demonstrated
            improvement.
        records: *id038
        note: Automatic conversation-fed writes produce retained context/summary text available to later
          consumers. Durable behavior-shaping here means later model input, not learned weights or demonstrated
          improvement.
      - scope: Coding checkpoints, Pi capture, Hermes sync and OpenClaw legacy capture to future recall
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id039
          - memory.md#mem-rte-coding-flush
          - memory.md#mem-rte-coding-recall
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          - runtime.md#rt-rte-openclaw-hooks
          note: Adapters wire automatic trace submission and subsequent fact delivery. Remote extraction/admission
            and host activation remain opaque/unobserved; the positive is the implemented route, not service
            compliance.
        records: *id039
        note: Adapters wire automatic trace submission and subsequent fact delivery. Remote extraction/admission
          and host activation remain opaque/unobserved; the positive is the implemented route, not service
          compliance.
      - scope: Generic raw/direct replacement, CLI import and configuration submissions
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-direct-write
        - epistemic.md#epi-rte-cli-import
        - runtime.md#rt-rte-runtime-config
        note: Content can be static or trace-derived and human or computationally selected. These paths
          do not establish either qualifying trace learning or its bounded absence.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Other adapters and hosted internal write/consumer routes remain uninspected; no system-wide
          no or exhaustive yes-route inventory is justified.
      records:
      - runtime.md#rt-rte-extract-add
      - runtime.md#rt-rte-chat-memories
      - runtime.md#rt-bap-extraction-context
      - memory.md#mem-obj-procedural-memory
      - memory.md#mem-rte-coding-flush
      - memory.md#mem-rte-coding-recall
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-openclaw-hooks
      - runtime.md#rt-rte-direct-write
      - epistemic.md#epi-rte-cli-import
      - runtime.md#rt-rte-runtime-config
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      note: Positive routes suffice for existence, not complete coverage or benefit. Raw trace storage
        alone and static shipped protocols are not treated as trace learning.
    trace_source:
      assessment: partial
      units:
      - scope: Python conversational fact extraction; Pi and Hermes conversation capture; OpenClaw legacy
          turn capture
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id040
          - runtime.md#rt-rte-extract-add
          - memory.md#mem-rte-pi-memory
          - memory.md#mem-rte-hermes-memory
          - runtime.md#rt-rte-openclaw-hooks
          note: Qualifying writes consume recorded conversational turns including user and generated assistant
            text; original source follows content, not adapter labels.
        records: *id040
        note: Qualifying writes consume recorded conversational turns including user and generated assistant
          text; original source follows content, not adapter labels.
      - scope: Coding checkpoint input with conversation and selected execution evidence
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-coding-flush
          note: Redacted user/assistant extraction messages originate in coding sessions.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-coding-flush
          note: Selected tool evidence, including failed command details, can enter checkpoint batches
            used for memory derivation.
        records:
        - memory.md#mem-rte-coding-flush
        note: User problems/assistant conclusions and selected subagent/tool evidence feed hosted derivation.
          Static repository details in the same packet do not become traces.
      - scope: Procedural supplied-message original provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-procedural-memory
        - runtime.md#rt-rte-direct-write
        note: Conversation summary route is known, but the record does not fully establish original content/origin
          of every supplied message; no tool/event/trajectory origin is inferred.
      - scope: 'Included unresolved alternatives: hosted internals; optional TypeScript history stores;
          other coding-agent adapters, framework/CLI/dashboard consumers, async and provider variants'
        assessment: uninspected
        findings: []
        records: *id012
        note: Uninspected trace-fed alternatives and opaque mixed inputs prevent complete source coverage.
          Journal/hook event wrapping alone does not establish event-streams, and multi-turn conversations
          alone do not establish trajectories.
      records:
      - runtime.md#rt-rte-extract-add
      - memory.md#mem-rte-pi-memory
      - memory.md#mem-rte-hermes-memory
      - runtime.md#rt-rte-openclaw-hooks
      - memory.md#mem-rte-coding-flush
      - memory.md#mem-obj-procedural-memory
      - runtime.md#rt-rte-direct-write
      - runtime.md#rt-rte-hosted-client
      - memory.md#mem-rte-typescript-memory
      note: Session and tool evidence are supported origins. Mixed static/opaque material remains unresolved
        rather than being forced into an event-stream or trajectory category.
---

# Mem0 memory profile

## Comparison rationale

The ten axes remain partial. Inspected local objects and shipped consumers establish positive mechanisms, while service internals and unread included alternatives prevent complete coverage. A wired classification describes source-connected operations, not observed execution, compliance, truthful extraction or improved capacity. Scope follows the accepted inventory rather than only the strongest Python witness.

Reconciliation supersedes EPI-OBJ-data with [MEM-OBJ-memory-data](memory.md#mem-obj-memory-data). All payload findings use that canonical object; its old/new history copies remain [MEM-OBJ-history](memory.md#mem-obj-history). The symbolic keyword part remains separately citable as [EPI-OBJ-text-lemmatized](epistemic.md#epi-obj-text-lemmatized), without replacing the valid access-payload container. No other supplied supersession changes a value.

Dense vectors are retained parametric representations, not the external encoder's weights. Entity links do not establish graph storage. The service-object affordance preserves the opaque hosted alternative rather than exporting local vector/SQLite architecture to it. See [MEM-OBJ-memory-vectors](memory.md#mem-obj-memory-vectors), [MEM-OBJ-entity-links](memory.md#mem-obj-entity-links) and [RT-RTE-hosted-client](runtime.md#rt-rte-hosted-client).

Inspected local Python fact extraction and procedural summaries qualify as wired consolidation and automatic trace-fed memory writes when their retained results reach later context. The coding-checkpoint branch separately wires selection, redaction, submission and later recall, but its unavailable hosted extractor does not establish a wired curation transformation. Its curation unit therefore retains no positive finding and a not-determinable assessment; requested extraction instructions do not resolve that operation. See [MEM-RTE-coding-flush](memory.md#mem-rte-coding-flush). This distinction leaves the local consolidation positive intact and does not settle instance-level entailment. The prescribed cessation inference supports only claimed synthesis; an extraction error by itself would not establish synthesis. No parameter-training conclusion follows. See [RT-RTE-extract-add](runtime.md#rt-rte-extract-add), [MEM-OBJ-procedural-memory](memory.md#mem-obj-procedural-memory), [EPI-CLM-evidence-bound](epistemic.md#epi-clm-evidence-bound) and [RT-BAP-extraction-context](runtime.md#rt-bap-extraction-context).

Curation is consumer-specific. Hash deduplication is bounded, expiry does not prevent direct ID/extraction reads, and vector withdrawal leaves history and recent messages. Explicit replacement establishes evolve without universal human control. TypeScript ADD-shaped returns can include failed insertions and do not inherit Python result-accounting guarantees. See [EPI-RTE-extraction-checks](epistemic.md#epi-rte-extraction-checks), [EPI-RTE-memory-selection](epistemic.md#epi-rte-memory-selection), [RT-RTE-direct-write](runtime.md#rt-rte-direct-write) and [MEM-RTE-typescript-memory](memory.md#mem-rte-typescript-memory).

Read-back separates a backend pull request from automatic host-context push. Query strings alone do not establish a remote embedding, lexical or model-judgment selector. The OpenClaw and coding/Pi/Hermes backend relevance selectors retain their unresolved algorithms. Seen-ID filtering is an actual identity match affecting delivered facts, not merely an ID attached to a requested object. Sidekick delivery separately selects stored parent recall by tracked identity. See [RT-RTE-openclaw-hooks](runtime.md#rt-rte-openclaw-hooks), [MEM-RTE-coding-recall](memory.md#mem-rte-coding-recall), [MEM-RTE-pi-memory](memory.md#mem-rte-pi-memory) and [MEM-RTE-hermes-memory](memory.md#mem-rte-hermes-memory). The incompatible proxy is not counted as successful recall delivery; see [RT-RTE-proxy-chat](runtime.md#rt-rte-proxy-chat).

Trace origins follow original content: coding tool evidence remains tool-traces; conversational turns remain session-logs even when captured as host events. Static repository evidence supplies no additional trace source. Opaque provenance, initial-content control, alternative stores, remote transformations and unread integration routes prevent stronger assessments. See [MEM-RTE-coding-flush](memory.md#mem-rte-coding-flush), [EPI-RTE-cli-import](epistemic.md#epi-rte-cli-import) and [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config).

Source-read log: none. This profile uses only supplied accepted records and reconciliation; it adds no records, source quotations or execution evidence.
