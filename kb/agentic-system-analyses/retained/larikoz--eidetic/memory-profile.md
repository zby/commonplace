---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Eidetic memory comparison: retained cards, retrieval projections, adaptive context,
  admission controls and export at the frozen revision.'
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
source-identity: https://github.com/LARIkoz/eidetic
reviewed-boundary: 67506b62fdd0944c243537c3cb10938f7343b6b2
memory-comparison:
  version: 2
  scope: 'Included: accumulated personal cards and topic content; mixed text, metadata, Evidence
    and dense retrieval projections; unindexed handoffs and generated rules; session history/hints;
    judged-candidate, test/filing and usage/lifecycle control traces; managed maintenance regions;
    exported pages and export control state; unresolved dark child/report payloads and possible provider-side
    accumulated state. Excluded: pretrained model weights as static inference components, shipped
    static instructions/HINTS as independent memory, ordinary unretained current-run state, host
    conversation compaction, product-update executable replacements and unfrozen SDK application
    stores. Raw host transcripts are trace inputs to included derivations, not an asserted complete
    Eidetic archive.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Personal cards, topic corpus, unindexed handoffs, generated rules and exported vault
          pages
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-memory-cards
          - memory.md#mem-rte-fresh-handoff
          - runtime.md#rt-obj-memory-context
          - memory.md#mem-rte-vault-export
          note: Markdown cards, state files, rules and vault pages are read or written as files.
        records: *id001
        note: The inspected durable text objects are filesystem artifacts; handoff producer identity
          does not obscure its file substrate.
      - scope: Card text/metadata/event projections, dense indexes, Core logical-index state and
          session counters
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-memory-chunks
          - memory.md#mem-obj-evidence-events
          - runtime.md#rt-rte-engine-worker
          - memory.md#mem-rte-session-hints
          note: memory_chunks, card_events, vector blobs, logical-index derived state and sessions.db
            use SQLite.
        records: *id002
        note: SQLite covers the inspected projections and session_log; vector encoding is not another
          substrate.
      - scope: Judged-candidate cache, filing/test correlation, lifecycle/usage/passive logs and
          export manifest/cache
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-admission-traces
          - memory.md#mem-rte-vault-export
          note: Append-only traces and export control artifacts persist on the filesystem.
        records: *id003
        note: Named local JSONL/log/manifest parts retain later-selection and re-export state.
      - scope: Provider-side retained state, if any, on extraction, embedding, reranking, translation
          and export routes
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-session-extractor
        - runtime.md#rt-cmp-embed
        - runtime.md#rt-cmp-rerank
        - runtime.md#rt-cmp-query-translation
        - memory.md#mem-cmp-export-models
        note: Adapters do not inspect provider retention or updates through use. Pretrained weights
          are not classified as accumulated memory merely because inference uses them.
      records:
      - memory.md#mem-obj-memory-cards
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-obj-memory-context
      - memory.md#mem-rte-vault-export
      - memory.md#mem-obj-memory-chunks
      - memory.md#mem-obj-evidence-events
      - runtime.md#rt-rte-engine-worker
      - memory.md#mem-rte-session-hints
      - memory.md#mem-obj-admission-traces
      - runtime.md#rt-cmp-session-extractor
      - runtime.md#rt-cmp-embed
      - runtime.md#rt-cmp-rerank
      - runtime.md#rt-cmp-query-translation
      - memory.md#mem-cmp-export-models
      note: Files and SQLite are supported for named local objects. Provider-side accumulation remains
        uninspected; no substrate value is inferred for it.
    representational_form:
      assessment: partial
      units:
      - scope: Card bodies, copied index sections, selected handoff/rules text and vault bodies at
          interpretive readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id004
          - memory.md#mem-obj-memory-cards
          - memory.md#mem-obj-memory-chunks
          - memory.md#mem-rte-fresh-handoff
          - runtime.md#rt-obj-memory-context
          - memory.md#mem-rte-vault-export
          note: Agents or humans interpret retained prose as facts, guidance or summaries.
        records: *id004
        note: Natural-language parts are separate from fixed-rule metadata.
      - scope: Frontmatter, paths/hashes, Evidence fields/confidence, caches, counters and export
          control metadata at code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - memory.md#mem-obj-memory-cards
          - memory.md#mem-obj-memory-chunks
          - memory.md#mem-obj-evidence-events
          - memory.md#mem-obj-admission-traces
          - memory.md#mem-rte-session-hints
          - memory.md#mem-rte-vault-export
          note: Types, statuses, identifiers, counts, event kinds, hashes and manifest fields determine
            code behavior.
        records: *id005
        note: Localized fields and scalar confidence have fixed parser/algebra/selector consumers.
      - scope: Retained dense vectors at semantic retrieval and maintenance neighbor selection
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id006
          - memory.md#mem-obj-memory-chunks
          - runtime.md#rt-cmp-embed
          - runtime.md#rt-rte-memory-recall
          - runtime.md#rt-rte-semantic-maintenance
          note: Numerical information distributed through embedding dimensions supports similarity
            selection.
        records: *id006
        note: Derived dense representations are distinct from scalar symbolic scores and from pretrained
          model weights.
      - scope: Optional M2 synthesis callback body and incompletely traced acquisition/child-agent
          dark payloads
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-m2-reshaping
        - memory.md#mem-obj-admission-traces
        - epistemic.md#epi-rte-acquisition-check
        note: The default text and known outcome keys are covered above; callback outputs and complete
          dark-log payload/consumer schemas are not recorded.
      - scope: Possible provider-side accumulated payload at subsequent inference
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-session-extractor
        - runtime.md#rt-cmp-shimnachi-local
        - memory.md#mem-cmp-export-models
        note: No inspected provider-state consumption path establishes its encoding.
      records:
      - memory.md#mem-obj-memory-cards
      - memory.md#mem-obj-memory-chunks
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-obj-memory-context
      - memory.md#mem-rte-vault-export
      - memory.md#mem-obj-evidence-events
      - memory.md#mem-obj-admission-traces
      - memory.md#mem-rte-session-hints
      - runtime.md#rt-cmp-embed
      - runtime.md#rt-rte-memory-recall
      - runtime.md#rt-rte-semantic-maintenance
      - epistemic.md#epi-rte-m2-reshaping
      - epistemic.md#epi-rte-acquisition-check
      - runtime.md#rt-cmp-session-extractor
      - runtime.md#rt-cmp-shimnachi-local
      - memory.md#mem-cmp-export-models
      note: Text, symbolic and dense parts are supported. Opaque generated alternatives and provider
        accumulation prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Caller-supplied personal bodies and existing personal/corpus/skill files
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records: &id007
          - memory.md#mem-obj-memory-cards
          - runtime.md#rt-rte-explicit-admission
          - memory.md#mem-obj-memory-chunks
          note: Personal answer bodies have a caller-authored route; this does not authenticate the
            caller or all initial files.
        records: *id007
        note: Caller authors/promotes bodies, but initial file provenance and human versus agent
          authorship remain unresolved.
      - scope: Topic corpus and optional source-code entity content
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id008
          - memory.md#mem-obj-memory-cards
          - runtime.md#rt-rte-explicit-admission
          - memory.md#mem-rte-code-projection
          note: External topic text and project source spans are acquired into retained retrieval
            material.
        records: *id008
        note: Source bytes enter corpus or derived code rows rather than originating as trace lessons.
      - scope: Stop signals/History and M3 mined answers, support provenance and outcome caches
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id009
          - runtime.md#rt-rte-signal-compound
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-memory-cards
          - memory.md#mem-obj-admission-traces
          note: Models/code extract session candidates and retain derived signal/answer/outcome material.
        records: *id009
        note: Session text is the recorded derivation source; re-retrieved support does not establish
          the original answer used those sources.
      - scope: Text/metadata index, confidence fold, dense vector generation, context assembly, session
          hint selection and default M2 regions
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id010
          - memory.md#mem-obj-memory-chunks
          - memory.md#mem-rte-evidence-projection
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-rte-session-hints
          - epistemic.md#epi-rte-m2-reshaping
          note: Splitting, parsing, folding, embedding, budget assembly and deterministic linked-line
            construction derive new representations.
        records: *id010
        note: Known derivations are compilation/selection from retained inputs; original file provenance
          remains a separate unit.
      - scope: Vault templates, manifests, polish and topic generation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id011
          - memory.md#mem-rte-vault-export
          - epistemic.md#epi-rte-vault-generation
          note: Export code and model calls transform source cards/exported pages into retained vault
            derivatives.
        records: *id011
        note: Known exporter derivation is not proof of proposition preservation or novel synthesis.
      - scope: Unindexed handoff initial production and opaque M2 callback/dark child payload provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-fresh-handoff
        - epistemic.md#epi-rte-m2-reshaping
        - memory.md#mem-obj-admission-traces
        note: External handoff producer and complete callback/child derivations are not established;
          known read/commit code does not resolve them.
      - scope: Provider-side state accumulated or updated through use
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-session-extractor
        - runtime.md#rt-cmp-embed
        - memory.md#mem-cmp-export-models
        note: External inference component identities do not establish retention lineage.
      records:
      - memory.md#mem-obj-memory-cards
      - runtime.md#rt-rte-explicit-admission
      - memory.md#mem-obj-memory-chunks
      - memory.md#mem-rte-code-projection
      - runtime.md#rt-rte-signal-compound
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - memory.md#mem-rte-evidence-projection
      - runtime.md#rt-rte-context-injection
      - memory.md#mem-rte-session-hints
      - epistemic.md#epi-rte-m2-reshaping
      - memory.md#mem-rte-vault-export
      - epistemic.md#epi-rte-vault-generation
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-cmp-session-extractor
      - runtime.md#rt-cmp-embed
      - memory.md#mem-cmp-export-models
      note: Known authored, imported, trace-extracted and compiled paths coexist with unresolved
        initialization and opaque derivations.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Non-feedback card/snippet/handoff/answer text at foreground recall or context reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id012
          - memory.md#mem-obj-memory-cards
          - runtime.md#rt-rte-memory-recall
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-rte-fresh-handoff
          note: Selected retained text provides candidate facts and continuation context to the host/recall
            caller.
        records: *id012
        note: Delivery is wired context/evidence supply, not observed reliance or compliance.
      - scope: Feedback text at foreground host rules loader
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id013
          - runtime.md#rt-bap-memory-rules
          - runtime.md#rt-rte-context-injection
          note: Retained feedback supplies standing natural-language behavioral directions, not enforced
            model compliance.
        records: *id013
        note: Standing directions are delivered under ALWAYS APPLY; name-only/cluster delivery is
          weaker than full-rule delivery.
      - scope: Session-count-selected hint at foreground host
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id014
          - memory.md#mem-rte-session-hints
          - memory.md#mem-bap-session-awareness
          note: The generated directive requests proactive/terser behavior in later sessions.
        records: *id014
        note: Fixed hint language is selected by accumulated history; the static HINTS table is not
          itself learned memory.
      - scope: Card text, dense vectors, source/status/confidence metadata and Evidence at retrieval/assembly/maintenance
          selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id015
          - memory.md#mem-obj-memory-chunks
          - memory.md#mem-obj-evidence-events
          - epistemic.md#epi-rte-confidence-ranking
          - runtime.md#rt-rte-memory-recall
          - runtime.md#rt-rte-semantic-maintenance
          note: Text/features and event-derived weights influence relative prominence and neighbor
            selection.
        records: *id015
        note: Content scored by fixed lexical/vector code still supplies ranking input.
      - scope: Retained transcript experience at signal/M3 durable-card update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id016
          - runtime.md#rt-rte-signal-compound
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-memory-cards
          note: Session decisions/answers feed durable card updates for later context and recall.
        records: *id016
        note: Automatic session-derived writes shape later available context; this is learning authority
          at the update consumer, not improved capacity.
      - scope: Retained session history and test/filing traces at adaptive-hint and Evidence update
          consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id017
          - memory.md#mem-rte-session-hints
          - memory.md#mem-rte-test-affirmation
          - memory.md#mem-obj-evidence-events
          note: Retained history/feedback supplies automatic updates to guidance or durable ranking
            state.
        records: *id017
        note: Count-selected guidance and gated correlated-test promotions are separate durable behavior-shaping
          updates. Ordinary hook promotion remains limited by project-identity mismatch.
      - scope: M3 judged cache at candidate retry/selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id018
          - memory.md#mem-obj-admission-traces
          - runtime.md#rt-rte-m3-filing
          - epistemic.md#epi-rte-acquisition-check
          note: Cache key/outcome selects whether retrieval/judging is performed again.
        - value: enforcement
          basis: wired
          records: *id018
          note: Definitive cached candidates are excluded from repeat processing for that session.
        records: *id018
        note: Definitive cached outcomes suppress same-session candidates; transient outcomes retry.
      - scope: Retained metadata/source spans at maintenance and filing gates
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id019
          - memory.md#mem-obj-evidence-events
          - memory.md#mem-rte-evidence-projection
          - runtime.md#rt-rte-semantic-maintenance
          - epistemic.md#epi-rte-support-check
          - runtime.md#rt-rte-m3-filing
          note: Retained authority/type/event fields and source spans supply conformity/support criteria.
        - value: enforcement
          basis: wired
          records: *id019
          note: Protected/insufficient-authority metadata vetoes mutations; source-support results
            veto unsupported filing.
        records: *id019
        note: Event types/authority criteria and retrieved spans are retained inputs to admissibility
          decisions, not authenticated truth.
      - scope: Retained project/path/count/hash/status fields at scope, hint and delta-export routing
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id020
          - memory.md#mem-rte-session-hints
          - memory.md#mem-rte-fresh-handoff
          - memory.md#mem-rte-evidence-projection
          - memory.md#mem-rte-vault-export
          note: Project identity, counts, source hashes and statuses select scope, phase or rewrite
            eligibility.
        records: *id020
        note: These are actual operation/window selectors, not inert catalog identifiers.
      - scope: Exported pages at human vault reader
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id021
          - memory.md#mem-rte-vault-export
          - epistemic.md#epi-obj-vault-pages
          note: Exported note and topic prose supplies reference material to a human reader.
        records: *id021
        note: Human-readable vault browsing is supported as an affordance, not an observed reader
          invocation.
      - scope: Dark acquisition/child report payloads, optional callback effects and provider retained
          state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-admission-traces
        - epistemic.md#epi-rte-acquisition-check
        - epistemic.md#epi-rte-m2-reshaping
        - runtime.md#rt-cmp-shimnachi-local
        note: Known retry outcomes are classified above; exact other report consumers/effects and
          provider behavior are not resolved.
      records:
      - memory.md#mem-obj-memory-cards
      - runtime.md#rt-rte-memory-recall
      - runtime.md#rt-rte-context-injection
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-bap-memory-rules
      - memory.md#mem-rte-session-hints
      - memory.md#mem-bap-session-awareness
      - memory.md#mem-obj-memory-chunks
      - memory.md#mem-obj-evidence-events
      - epistemic.md#epi-rte-confidence-ranking
      - runtime.md#rt-rte-semantic-maintenance
      - runtime.md#rt-rte-signal-compound
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-acquisition-check
      - memory.md#mem-rte-evidence-projection
      - epistemic.md#epi-rte-support-check
      - memory.md#mem-rte-vault-export
      - epistemic.md#epi-obj-vault-pages
      - epistemic.md#epi-rte-m2-reshaping
      - runtime.md#rt-cmp-shimnachi-local
      note: Knowledge, instruction, ranking, learning, routing, validation and enforcement have local
        consumers. No force or completeness is inferred for opaque payloads or downstream host compliance.
    write_agency:
      assessment: partial
      units:
      - scope: Stop signal compounding and M3 support-gated filing/outcome-cache admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id022
          - runtime.md#rt-rte-signal-compound
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-admission-traces
          - epistemic.md#epi-rte-acquisition-check
          note: Software/model filtering, support and candidate gates decide the retained writes.
        records: *id022
        note: Code/model decides admission with no per-content operator approval; configuration and
          starting hooks do not make it manual.
      - scope: Index/vector/code projection, generated rules and session-counter/hint admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id023
          - memory.md#mem-obj-memory-chunks
          - runtime.md#rt-rte-engine-worker
          - memory.md#mem-rte-code-projection
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-rte-session-hints
          note: Parser, embedding, assembly and counter code admits generated state.
        records: *id023
        note: Code derives and installs these objects without a per-entry human content decision.
      - scope: M1/M2/event/confidence updates, test promotions and decay
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id024
          - runtime.md#rt-rte-semantic-maintenance
          - epistemic.md#epi-rte-m2-reshaping
          - memory.md#mem-rte-evidence-projection
          - memory.md#mem-rte-test-affirmation
          note: Heuristic/model/program gates decide edits and durable events.
        records: *id024
        note: Activation switches differ from per-content approval; the test route is conditional
          on matching identities.
      - scope: Vault export/polish/topic, delta control state and cleanup candidate/log deletion
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - memory.md#mem-rte-vault-export
          - epistemic.md#epi-rte-vault-generation
          - memory.md#mem-rte-card-withdrawal
          note: Code/model gates admit generated pages and code-selected maintenance mutations.
        records: *id025
        note: Invocation chooses a mode, but software selects and writes each resulting retained
          transformation.
      - scope: Direct personal writer and base-add caller content
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-explicit-admission
        - memory.md#mem-obj-memory-cards
        note: Caller identity is unspecified; body supply alone does not establish explicit human
          content approval. Base MCP describes but does not enforce a user-only policy.
      - scope: Base MCP explicit-user-only policy
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id026
          - runtime.md#rt-rte-explicit-admission
          note: The advertised policy requires an explicit user request to save that content.
        records: *id026
        note: This is a claimed per-content human-request policy, separate from the ungated implemented
          caller route.
      - scope: Human source-card/Evidence/declaration editing and reversal
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records: &id027
          - memory.md#mem-rte-evidence-projection
          - memory.md#mem-rte-card-withdrawal
          note: A person can explicitly edit retained content/events or reverse status/declarations.
        records: *id027
        note: The reports establish available human edit/reversal surfaces, not observed edits or
          a universal human gate.
      - scope: Initial existing files and fresh handoff admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-cards
        - memory.md#mem-obj-memory-chunks
        - memory.md#mem-rte-fresh-handoff
        note: Scanner/read selection does not determine who supplied or approved the retained file.
      - scope: Opaque callback/child dark payload and provider-side admission
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-m2-reshaping
        - memory.md#mem-obj-admission-traces
        - runtime.md#rt-cmp-session-extractor
        note: Known local commits remain automatic; initial opaque payload control and provider admission
          remain unresolved.
      records:
      - runtime.md#rt-rte-signal-compound
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-acquisition-check
      - memory.md#mem-obj-memory-chunks
      - runtime.md#rt-rte-engine-worker
      - memory.md#mem-rte-code-projection
      - runtime.md#rt-rte-context-injection
      - memory.md#mem-rte-session-hints
      - runtime.md#rt-rte-semantic-maintenance
      - epistemic.md#epi-rte-m2-reshaping
      - memory.md#mem-rte-evidence-projection
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-rte-vault-export
      - epistemic.md#epi-rte-vault-generation
      - memory.md#mem-rte-card-withdrawal
      - runtime.md#rt-rte-explicit-admission
      - memory.md#mem-obj-memory-cards
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-cmp-session-extractor
      note: Automatic local mechanisms and afforded/claimed manual controls are retained separately.
        Generic direct callers and initial/handoff/provider admission prevent complete coverage.
    curation_operations:
      assessment: partial
      units:
      - scope: Transcript-to-standing-signal extraction and budgeted retained context
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id028
          - runtime.md#rt-rte-signal-compound
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-obj-memory-cards
          note: Bounded extraction and assembly select reduced representations for later context.
        records: *id028
        note: Extraction selects/compresses existing session content; faithfulness is not proven
          and extraction defects would not establish new-claim synthesis.
      - scope: Existing History updates and daily signal duplicate handling
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id029
          - runtime.md#rt-rte-signal-compound
          - memory.md#mem-obj-memory-cards
          note: Eligible existing cards receive new dated History content.
        - value: dedup
          basis: wired
          records: *id029
          note: Daily signal writes skip signals already present; this is not exactly-once History
            admission.
        records: *id029
        note: 'The workflow annotation qualifies retry: History appends may repeat, while daily signal
          insertion checks existing content.'
      - scope: Default M2 managed-region transformation and M3 duplicate routing
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id030
          - epistemic.md#epi-rte-m2-reshaping
          - runtime.md#rt-rte-semantic-maintenance
          - runtime.md#rt-rte-m3-filing
          note: Default M2 reduces existing source claims to linked salient lines.
        - value: dedup
          basis: wired
          records: *id030
          note: Duplicate source slugs/near-duplicate answers are suppressed or merged into the managed
            consolidation path.
        - value: evolve
          basis: wired
          records: *id030
          note: Managed-region replacement revises an existing target while preserving surrounding
            text.
        records: *id030
        note: Default M2 selects linked source one-liners, deduplicates slugs and replaces its own
          region; duplicate answers route to M2 rather than becoming new cards.
      - scope: Evidence gain/test affirmation and optional M1/M2 withdrawal/decay
        assessment: known
        findings:
        - value: promote
          basis: wired
          records: &id031
          - memory.md#mem-obj-evidence-events
          - memory.md#mem-rte-evidence-projection
          - memory.md#mem-rte-test-affirmation
          - runtime.md#rt-rte-semantic-maintenance
          note: Observed/confirmation/test events can raise folded confidence and enabled ranking
            salience.
        - value: invalidate
          basis: wired
          records: *id031
          note: Contradiction/supersession events and metadata withdraw current reliance while keeping
            content/history available.
        - value: decay
          basis: wired
          records: *id031
          note: Age-stale managed non-feedback content receives bounded confidence decay.
        records: *id031
        note: Promotion changes salience; demotion/terminal status changes current reliance without
          guaranteeing content exclusion. Test gain remains conditional and not claim verification.
      - scope: Status archival, physical card archive and old lifecycle-log cleanup
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id032
          - memory.md#mem-rte-card-withdrawal
          - epistemic.md#epi-rte-cleanup-archive
          - epistemic.md#epi-rte-curate-archive
          note: Archived status or archive relocation withdraws ordinary current reliance/availability
            while preserving card history.
        - value: decay
          basis: wired
          records: *id032
          note: Downweighting archived cards and deleting aged lifecycle logs reduce salience or
            retained trace availability.
        records: *id032
        note: Status and relocation are different withdrawal mechanisms; refresh is needed and exported
          copies may survive.
      - scope: Optional model polish/topic generation and M2 synthesis callback
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-vault-export
        - epistemic.md#epi-rte-vault-generation
        - epistemic.md#epi-rte-m2-reshaping
        note: Generation requests preservation but actual output semantics are indeterminate. Neither
          a synthesis name nor lack of entailment proof warrants synthesize; known M2 default operations
          remain above.
      - scope: Dark child/report transformations and provider-side updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-admission-traces
        - epistemic.md#epi-rte-acquisition-check
        - runtime.md#rt-cmp-session-extractor
        note: Known outcomes do not inventory all transformations; opaque state prevents a complete
          operation list.
      records:
      - runtime.md#rt-rte-signal-compound
      - runtime.md#rt-rte-context-injection
      - memory.md#mem-obj-memory-cards
      - epistemic.md#epi-rte-m2-reshaping
      - runtime.md#rt-rte-semantic-maintenance
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-evidence-events
      - memory.md#mem-rte-evidence-projection
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-rte-card-withdrawal
      - epistemic.md#epi-rte-cleanup-archive
      - epistemic.md#epi-rte-curate-archive
      - memory.md#mem-rte-vault-export
      - epistemic.md#epi-rte-vault-generation
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-acquisition-check
      - runtime.md#rt-cmp-session-extractor
      note: Consolidate, evolve, dedup, promote, invalidate and decay have implemented local transformations.
        No controlled synthesize finding is established by the recorded generation labels; opaque
        alternatives stay unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested personal/base recall/detail, serendipity and Core client search
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id033
          - runtime.md#rt-rte-memory-recall
          - memory.md#mem-rte-serendipity-read
          - runtime.md#rt-rte-engine-worker
          note: Query/detail/discovery requests select and return retained text or derived IDs/scores.
        records: *id033
        note: A caller requests retained material; returning it is not a second unsolicited push.
          External SDK agent consumption is not wired by this classification.
      - scope: SessionStart card context, fresh handoff and count-selected hint
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id034
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-rte-fresh-handoff
          - memory.md#mem-rte-session-hints
          note: Automatic selectors assemble retained content/guidance without a foreground request
            for those specific memories.
        records: *id034
        note: Lifecycle code independently supplies selected retained material before foreground
          work, under the host loading contract.
      - scope: Automatic maintenance neighbors and M3 cache/source-support selection
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id035
          - runtime.md#rt-rte-semantic-maintenance
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-admission-traces
          - epistemic.md#epi-rte-support-check
          note: Automatic selection provides retained inputs to later maintenance/mining/support
            operations.
        records: *id035
        note: Changed-card/session triggers cause selectors to supply retained neighbors, outcomes
          or source spans to update/check consumers.
      - scope: Requested export/curation and their manifest/usage/page consumers
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id036
          - memory.md#mem-rte-vault-export
          - memory.md#mem-rte-card-withdrawal
          note: Requested export/curation consumes retained source material and control state.
        - value: push
          basis: wired
          records: *id036
          note: Exporter automatically selects weighted retained notes for an enabled topic-model
            call.
        records: *id036
        note: CLI/MCP requests start these reads; automatic note/source selection within the workflow
          is distinguished from the requested output.
      - scope: Human vault browsing
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id037
          - memory.md#mem-rte-vault-export
          note: Human readers can open retained vault notes and generated topic pages.
        records: *id037
        note: The declared readable vault supports requested browsing without supplied actual use.
      - scope: Dark report/child payload consumers and possible provider-state read-back
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-admission-traces
        - epistemic.md#epi-rte-acquisition-check
        - runtime.md#rt-cmp-session-extractor
        note: Known cache retry consumers are covered above; detailed report and provider selection/delivery
          operations are not recorded.
      records:
      - runtime.md#rt-rte-memory-recall
      - memory.md#mem-rte-serendipity-read
      - runtime.md#rt-rte-engine-worker
      - runtime.md#rt-rte-context-injection
      - memory.md#mem-rte-fresh-handoff
      - memory.md#mem-rte-session-hints
      - runtime.md#rt-rte-semantic-maintenance
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-support-check
      - memory.md#mem-rte-vault-export
      - memory.md#mem-rte-card-withdrawal
      - epistemic.md#epi-rte-acquisition-check
      - runtime.md#rt-cmp-session-extractor
      note: Both requested pull and independent push chains are supported; opaque later consumers
        prevent complete direction coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: SessionStart feedback availability and budget/recency/status selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id038
          - runtime.md#rt-rte-context-injection
          - runtime.md#rt-clm-feedback-visibility
          note: All feedback is represented by name/cluster and other content is filtered by availability,
            recency, tiers and budgets.
        records: *id038
        note: Trigger is SessionStart; type, age, weights and budget select feedback/project/recent
          representations independently of a query.
      - scope: SessionStart project matching and fresh handoff location
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id039
          - runtime.md#rt-rte-context-injection
          - memory.md#mem-rte-fresh-handoff
          note: Actual project/location matches select retained project content and handoff candidates.
        - value: coarse
          basis: wired
          records: *id039
          note: Newest handoff under 30 minutes and character limits select and cap the delivered
            handoff.
        records: *id039
        note: Trigger is SessionStart; normalized CWD/project match selects project chunks and CWD/project-pattern
          state files. Age/newest/budget filtering remains a separate coarse signal.
      - scope: SessionStart adaptive guidance from prior session_log
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id040
          - memory.md#mem-rte-session-hints
          note: Normalized project identity selects the session history used for delivery.
        - value: coarse
          basis: wired
          records: *id040
          note: Count bands select novice/standard/veteran guidance from accumulated history.
        records: *id040
        note: Trigger is SessionStart; project identity selects retained rows, count thresholds select
          the emitted hint, not semantic similarity.
      - scope: Changed-card M1/M2 neighbor supply and gate-selected retained content
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id041
          - runtime.md#rt-rte-semantic-maintenance
          - epistemic.md#epi-rte-m2-reshaping
          note: Same-project identity filters retained neighbor candidates.
        - value: inferred-embedding
          basis: wired
          records: *id041
          note: Semantic nearest-neighbor selection supplies retained card candidates.
        - value: inferred-judgment
          basis: wired
          records: *id041
          note: Optional relevance/confirming evaluators gate which retained neighbor material reaches
            an edit.
        records: *id041
        note: Trigger is changed ingest; same-project filters and vector/relevance/conflict judgments
          select neighboring card material for later maintenance.
      - scope: M3 same-session cache and re-retrieved support/dedup material
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id042
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-admission-traces
          - epistemic.md#epi-rte-support-check
          - runtime.md#rt-rte-memory-recall
          note: Session/candidate-key matches select definitive cached outcomes used to suppress
            repeats.
        - value: inferred-lexical
          basis: wired
          records: *id042
          note: Recall query and overlap selection supply source chunks to the automatic support
            chain.
        - value: inferred-embedding
          basis: wired
          records: *id042
          note: Available semantic retrieval/near-neighbor similarity selects source or duplicate
            candidates.
        records: *id042
        note: Trigger is later Stop/mined candidate; session/candidate identity suppresses processed
          entries, while query retrieval/dedup selects retained source spans and neighbors.
      - scope: Post-filing test promotion producer
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id043
          - memory.md#mem-rte-test-affirmation
          note: Matching session/project and filed target identity selects the page receiving Evidence.
        records: *id043
        note: Trigger is enabled later producer; exact session/project matches select filed pages
          and corresponding retained test signals. The ordinary hooks do not establish matching project
          identities.
      - scope: Enabled vault topic-model selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id044
          - memory.md#mem-rte-vault-export
          - epistemic.md#epi-rte-vault-generation
          note: Relative weights, note count and character availability select/cap topic inputs;
            the resulting prose is not itself a selector signal.
        records: *id044
        note: Trigger is requested export with topic generation enabled; weighted note ordering,
          top-20 selection and text cap supply retained pages to the model.
      - scope: Requested recall/detail/discovery and human browsing delivery operations
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-memory-recall
        - memory.md#mem-rte-serendipity-read
        - runtime.md#rt-rte-engine-worker
        - memory.md#mem-rte-vault-export
        note: These delivery operations fulfill specific consumer requests. Their query/file IDs
          alone do not establish identifier-based push.
      - scope: Dark child/report and provider-state selectors
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-admission-traces
        - epistemic.md#epi-rte-acquisition-check
        - runtime.md#rt-cmp-session-extractor
        note: Known local cache selection does not resolve the remaining automatic consumers or provider
          payload.
      records:
      - runtime.md#rt-rte-context-injection
      - runtime.md#rt-clm-feedback-visibility
      - memory.md#mem-rte-fresh-handoff
      - memory.md#mem-rte-session-hints
      - runtime.md#rt-rte-semantic-maintenance
      - epistemic.md#epi-rte-m2-reshaping
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-support-check
      - runtime.md#rt-rte-memory-recall
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-rte-vault-export
      - epistemic.md#epi-rte-vault-generation
      - memory.md#mem-rte-serendipity-read
      - runtime.md#rt-rte-engine-worker
      - epistemic.md#epi-rte-acquisition-check
      - runtime.md#rt-cmp-session-extractor
      note: Coarse, identifier, inferred-lexical, inferred-embedding and inferred-judgment selectors
        are local findings; opaque alternatives prevent complete signal coverage.
    trace_learning:
      assessment: partial
      units:
      - scope: Stop session extraction to durable signals/History and later injection/recall
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id045
          - runtime.md#rt-rte-signal-compound
          - memory.md#mem-obj-memory-cards
          - runtime.md#rt-rte-context-injection
          - runtime.md#rt-rte-memory-recall
          note: Recorded conversational experience automatically becomes durable material available
            to later agent consumers.
        records: *id045
        note: Automatic session-fed writes produce later context; neither complete transcript retention
          nor demonstrated improvement is required.
      - scope: M3 recall filing/M2 handoff and judged-outcome retry cache
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id046
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-admission-traces
          - epistemic.md#epi-rte-m2-reshaping
          - epistemic.md#epi-rte-acquisition-check
          note: Automatic session-derived artifacts shape later context or candidate-routing behavior.
        records: *id046
        note: Session candidates yield durable answer/managed-region material or definitive outcome
          controls consumed on later invocations. Dark would_file is not a card write.
      - scope: Session history to durable count-selected behavioral hint
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id047
          - memory.md#mem-rte-session-hints
          - memory.md#mem-bap-session-awareness
          note: Accumulated session history automatically shapes later retained guidance supplied
            to the foreground host.
        records: *id047
        note: Session events feed retained history and generated guidance; selecting fixed hint text
          does not exclude a trace-fed behavior-shaping update.
      - scope: Test/filing correlation to typed Evidence and later confidence/ranking
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id048
          - memory.md#mem-rte-test-affirmation
          - memory.md#mem-obj-evidence-events
          - epistemic.md#epi-rte-confidence-ranking
          note: Recorded execution feedback can automatically update durable behavior-shaping ranking
            state for later consumers.
        records: *id048
        note: Automatic promotion capacity requires matching supplied session/project records and
          flags. Ordinary hook promotion is not established because slugs differ.
      - scope: Static topic imports, optional source-code entity projection and vector rebuild from
          supplied records
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-explicit-admission
        - memory.md#mem-rte-code-projection
        - runtime.md#rt-rte-engine-worker
        note: The named routes acquire/index content, not activity/experience. Source-code bodies
          are not tool/session traces simply because indexing runs in a hook.
      - scope: Caller-supplied personal bodies, initial/handoff admission and opaque callback/dark
          report routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-cards
        - runtime.md#rt-rte-explicit-admission
        - memory.md#mem-rte-fresh-handoff
        - epistemic.md#epi-rte-m2-reshaping
        - memory.md#mem-obj-admission-traces
        note: Origin and automatic control are not jointly established for all included alternatives;
          no local no or system-wide negative follows.
      - scope: Provider-side trace-fed durable updates
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-session-extractor
        - runtime.md#rt-cmp-embed
        - memory.md#mem-cmp-export-models
        note: Call-site inference without training requests does not establish absence of external
          provider updates.
      records:
      - runtime.md#rt-rte-signal-compound
      - memory.md#mem-obj-memory-cards
      - runtime.md#rt-rte-context-injection
      - runtime.md#rt-rte-memory-recall
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-m2-reshaping
      - epistemic.md#epi-rte-acquisition-check
      - memory.md#mem-rte-session-hints
      - memory.md#mem-bap-session-awareness
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-obj-evidence-events
      - epistemic.md#epi-rte-confidence-ranking
      - runtime.md#rt-rte-explicit-admission
      - memory.md#mem-rte-code-projection
      - runtime.md#rt-rte-engine-worker
      - memory.md#mem-rte-fresh-handoff
      - runtime.md#rt-cmp-session-extractor
      - runtime.md#rt-cmp-embed
      - memory.md#mem-cmp-export-models
      note: Several local yes chains are wired. Unresolved admissions and provider behavior preclude
        a complete trace-learning inventory; no unsupported no is authored.
    trace_source:
      assessment: partial
      units:
      - scope: Stop extraction and M3 candidate/card/cache chains
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id049
          - runtime.md#rt-rte-signal-compound
          - runtime.md#rt-rte-m3-filing
          - memory.md#mem-obj-admission-traces
          - epistemic.md#epi-rte-acquisition-check
          note: Recorded conversational turns feed automatic durable signal/answer/outcome production.
        records: *id049
        note: Original input is conversational user/assistant text or mined assistant/child conversational
          turns; retrieved static support cards do not add a trace category.
      - scope: Session-counter adaptive hint chain
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id050
          - memory.md#mem-rte-session-hints
          note: Runtime session events feed retained counts that select later behavioral guidance.
        records: *id050
        note: Original observations are discrete SessionStart occurrences grouped by project, not
          conversational logs.
      - scope: Test-correlated Evidence update chain
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id051
          - memory.md#mem-rte-test-affirmation
          - memory.md#mem-obj-evidence-events
          note: Recorded tool execution feedback feeds automatic durable Evidence promotion for later
            ranking.
        records: *id051
        note: The source is recorded Bash test invocation/execution success metadata. Serialization
          as a lifecycle callback does not by itself add another source value.
      - scope: Static imports, code projection and client index compilation
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-explicit-admission
        - memory.md#mem-rte-code-projection
        - runtime.md#rt-rte-engine-worker
        note: These scoped writes do not qualify as automatic trace-fed learning, so no original
          trace source is required for them.
      - scope: Caller bodies, handoff producer, M2 optional callback and full child/report origins
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-cards
        - runtime.md#rt-rte-explicit-admission
        - memory.md#mem-rte-fresh-handoff
        - epistemic.md#epi-rte-m2-reshaping
        - memory.md#mem-obj-admission-traces
        note: Known conversational M3 candidates are covered above; complete alternate input provenance
          and qualifying automatic writes are unresolved.
      - scope: Possible provider-side qualifying write inputs
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-session-extractor
        - runtime.md#rt-cmp-embed
        - memory.md#mem-cmp-export-models
        note: Neither a provider trace-fed update nor its original inputs were inspected.
      records:
      - runtime.md#rt-rte-signal-compound
      - runtime.md#rt-rte-m3-filing
      - memory.md#mem-obj-admission-traces
      - epistemic.md#epi-rte-acquisition-check
      - memory.md#mem-rte-session-hints
      - memory.md#mem-rte-test-affirmation
      - memory.md#mem-obj-evidence-events
      - runtime.md#rt-rte-explicit-admission
      - memory.md#mem-rte-code-projection
      - runtime.md#rt-rte-engine-worker
      - memory.md#mem-obj-memory-cards
      - memory.md#mem-rte-fresh-handoff
      - epistemic.md#epi-rte-m2-reshaping
      - runtime.md#rt-cmp-session-extractor
      - runtime.md#rt-cmp-embed
      - memory.md#mem-cmp-export-models
      note: Session logs, runtime session events and tool execution feedback are supported on distinct
        qualifying routes. Unknown origins remain; no trajectories value follows merely from multi-step
        workflow structure.
---

# Eidetic memory profile

## Comparison rationale

This profile classifies the accepted records at the supplied frozen revision. All
positive implementation findings have a wired basis, except the explicitly
claimed user-only base policy and afforded human editing/browsing surfaces.
There is no observed-run or causal classification. Every axis remains partial:
its inventory retains recorded initialization, opaque alternative-consumer or
provider limits rather than turning a local witness into a complete system list.
Provider inference components identify the unresolved boundary; they do not
establish that pretrained weights are accumulated memory.

Reconciliation supersedes EPI-CMP-vault-models with
[MEM-CMP-export-models](memory.md#mem-cmp-export-models), and
EPI-OBJ-confidence-events with
[MEM-OBJ-evidence-events](memory.md#mem-obj-evidence-events). Citations use those
canonical declarations. Card containers remain distinct from M3 provenance,
M2 managed regions, indexes, generated rules and vault pages; no other
supersession changes a value.

Dense retrieval parts map to parametric form on a SQLite substrate; localized
confidence numbers map to symbolic form. The known embedding derivation is
compiled lineage, not a finding about unknown initial card provenance or
external weight history. See
[MEM-OBJ-memory-chunks](memory.md#mem-obj-memory-chunks) and
[MEM-OBJ-evidence-events](memory.md#mem-obj-evidence-events).

Admission is classified separately from authoring and I/O. Hook/model gates
and export/maintenance software decide generated content automatically.
Generic direct caller identity leaves control unresolved, while explicit-user
base instructions remain only a claimed manual policy. Human editing is an
afforded manual route, not a universal approval barrier. See
[RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission),
[MEM-RTE-card-withdrawal](memory.md#mem-rte-card-withdrawal) and
[MEM-RTE-evidence-projection](memory.md#mem-rte-evidence-projection).

Consolidation selects existing claims. Default M2 also deduplicates and revises
managed regions; its name does not establish creation of new claims. Optional
callback, polish and topic output semantics remain unresolved, so no synthesize
value is asserted. A fact-preservation defect would not itself establish
synthesis. Promotion/decay/invalidation concern salience or current reliance,
not proof or universal deletion. See
[EPI-RTE-m2-reshaping](epistemic.md#epi-rte-m2-reshaping),
[EPI-RTE-vault-generation](epistemic.md#epi-rte-vault-generation) and
[MEM-RTE-card-withdrawal](memory.md#mem-rte-card-withdrawal).

Foreground requested recall is pull; lifecycle delivery is push. Requested
returns are not double-counted as push. Automatic maintenance, cache and topic
input selection are separately named consumers. Project/session identity matches
are targeted selectors; availability/count/budget filters remain coarse.
Similarity and relevance evaluators keep their own signal findings. Detail IDs
on requested returns alone establish no push signal. See
[RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall),
[RT-RTE-context-injection](runtime.md#rt-rte-context-injection),
[MEM-RTE-session-hints](memory.md#mem-rte-session-hints) and
[MEM-RTE-vault-export](memory.md#mem-rte-vault-export).

Trace-learning yes describes automatic trace-fed durable behavior-shaping
writes, not improved capacity. Session-derived knowledge receives learning
force at its update consumer and knowledge force at its later reader. Cached
definitive outcomes also shape later candidate routing; raw diagnostic retention
alone does not qualify. Session counts select later guidance. Test-correlated
Evidence can shape later ranking, but the ordinary hook project-identity mismatch
prevents claiming that ordinary filing receives these promotions. See
[RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound),
[RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing),
[MEM-OBJ-admission-traces](memory.md#mem-obj-admission-traces),
[MEM-RTE-session-hints](memory.md#mem-rte-session-hints) and
[MEM-RTE-test-affirmation](memory.md#mem-rte-test-affirmation).

Trace sources follow original content. Conversation mining is session-logs;
session occurrence history is event-streams; Bash test execution feedback is
tool-traces. Adapter event labels do not transform conversations or static
source files into event-stream sources. A linked multi-step workflow is not
itself evidence that the update consumes trajectories. Missing provenance stays
local to unresolved routes, not a system-wide negative.

Source-read log: none. Classification used only the supplied accepted members,
types, collection and worker/record contracts. No frozen source ambiguity required
a direct source read, no evidence or record was added, and no peer report was
changed. Deterministic output validation is the form/reference check performed
for this attempt; it does not establish analytical acceptance or activation.
