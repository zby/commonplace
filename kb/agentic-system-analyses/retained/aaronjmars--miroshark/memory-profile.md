---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of MiroShark: retained simulation context, graph memory, checkpoints, reusable
  setup and report/appraisal consumers.'
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
source-identity: https://github.com/aaronjmars/MiroShark
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
memory-comparison:
  version: 2
  scope: Retained or changed-through-use round/action narratives, cross-platform tails, belief/checkpoint/trajectory
    state, document/activity graph parts and access vectors, communities, generated persona/configuration
    reuse, director assumptions, cached briefings/research, report files/traces and appraisals, plus their
    admission, maintenance and later-consumer routes. Includes unresolved market/media, dedicated-driver,
    auxiliary consumer and opaque provider/host alternatives where they can retain or deliver this memory.
    Excludes shipped static prompts, inference weights as such, ordinary current-call observation filtering
    without retained results, capability registries/API permissions as such, and external service internals
    not captured by the boundary.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Resident round narratives, cross-platform action tails, belief objects and pending tool-result
          buffers
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-obj-cross-platform-log
          - memory.md#mem-rte-belief-feedback
          - runtime.md#rt-rte-agent-mcp
          note: Python resident objects retain content until later round or activation consumers.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-obj-cross-platform-log
        - memory.md#mem-rte-belief-feedback
        - runtime.md#rt-rte-agent-mcp
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Belief checkpoints/trajectories, profiles/configuration, director files and retained reports/appraisals
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          - runtime.md#rt-obj-agent-profiles
          - runtime.md#rt-obj-simulation-config
          - runtime.md#rt-rte-director-context
          - workflow.md#wf-rte-report-delivery
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-outcome-annotation
          - epistemic.md#epi-rte-prediction-resolution
          note: JSON/CSV/Markdown and action-log files persist selected content across calls or starts.
        records:
        - memory.md#mem-rte-belief-feedback
        - runtime.md#rt-obj-agent-profiles
        - runtime.md#rt-obj-simulation-config
        - runtime.md#rt-rte-director-context
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-quality-diagnostics
        - epistemic.md#epi-rte-outcome-annotation
        - epistemic.md#epi-rte-prediction-resolution
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Episode/entity/relation/community and optional report-trace graph parts
        assessment: known
        findings:
        - value: graph
          basis: wired
          records:
          - memory.md#mem-rte-graph-ingestion
          - memory.md#mem-rte-community-rebuild
          - memory.md#mem-obj-reasoning-trace
          note: Neo4j nodes, relationships and membership/trace links retain these parts.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-relation
          - memory.md#mem-obj-community
          note: Stored fact and community embeddings supply vector retrieval access, separate from graph
            text.
        records:
        - memory.md#mem-rte-graph-ingestion
        - memory.md#mem-rte-community-rebuild
        - memory.md#mem-obj-reasoning-trace
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Platform action/recommendation stores read by belief and interview paths
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: RoundAnalyzer reads SQLite recommendation/engagement data retained by the platforms.
        records:
        - memory.md#mem-rte-belief-feedback
        - runtime.md#rt-rte-interview-manual
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Ask and research caches
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - epistemic.md#epi-rte-ask-briefing
          - epistemic.md#epi-rte-web-research
          note: Repeated question/entity requests reuse process-local cached generated content.
        records:
        - epistemic.md#epi-rte-ask-briefing
        - epistemic.md#epi-rte-web-research
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Opaque provider/host state and incompletely inventoried market/media and auxiliary retained
          objects
        assessment: uninspected
        findings: []
        records: &id001
        - runtime.md#rt-rte-synchronized-rounds
        - memory.md#mem-obj-belief-state
        - runtime.md#rt-rte-agent-mcp
        - memory.md#mem-rte-graph-retrieval
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-obj-cross-platform-log
      - memory.md#mem-rte-belief-feedback
      - runtime.md#rt-rte-agent-mcp
      - runtime.md#rt-obj-agent-profiles
      - runtime.md#rt-obj-simulation-config
      - runtime.md#rt-rte-director-context
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-quality-diagnostics
      - epistemic.md#epi-rte-outcome-annotation
      - epistemic.md#epi-rte-prediction-resolution
      - memory.md#mem-rte-graph-ingestion
      - memory.md#mem-rte-community-rebuild
      - memory.md#mem-obj-reasoning-trace
      - runtime.md#rt-rte-interview-manual
      - epistemic.md#epi-rte-ask-briefing
      - epistemic.md#epi-rte-web-research
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-obj-belief-state
      - memory.md#mem-rte-graph-retrieval
      note: Known local stores coexist with uninspected provider/host and auxiliary parts. Model weights
        used for inference are not accumulated memory merely because they are loaded.
    representational_form:
      assessment: partial
      units:
      - scope: Graph facts/entity descriptions/community summaries, round prose, persona/report/research/seed
          prose and director assumptions
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-relation
          - epistemic.md#epi-obj-entity-summaries
          - memory.md#mem-rte-community-rebuild
          - memory.md#mem-rte-round-history
          - runtime.md#rt-obj-agent-profiles
          - workflow.md#wf-rte-report-delivery
          - epistemic.md#epi-rte-web-research
          - epistemic.md#epi-rte-ask-briefing
          - runtime.md#rt-rte-director-context
          note: These text parts are interpreted as descriptions, assumptions, summaries or guidance by
            their consumers.
        records:
        - memory.md#mem-obj-relation
        - epistemic.md#epi-obj-entity-summaries
        - memory.md#mem-rte-community-rebuild
        - memory.md#mem-rte-round-history
        - runtime.md#rt-obj-agent-profiles
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-web-research
        - epistemic.md#epi-rte-ask-briefing
        - runtime.md#rt-rte-director-context
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Belief values and rendered labels
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          - memory.md#mem-obj-belief-state
          note: Topic-keyed position/confidence/trust scalars have localized fixed-rule updates; they
            are not model weights.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: Rendered stance/trust labels become model-interpreted guidance.
        records:
        - memory.md#mem-rte-belief-feedback
        - memory.md#mem-obj-belief-state
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Graph fact/community embeddings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-relation
          - memory.md#mem-obj-community
          - epistemic.md#epi-rte-graph-ranking
          note: Dense distributed retrieval representations are distinct from readable claims and symbolic
            provenance.
        records:
        - memory.md#mem-obj-relation
        - memory.md#mem-obj-community
        - epistemic.md#epi-rte-graph-ranking
        note: The cited records establish the named inspected part, not successful operation.
      - scope: IDs, time/kind/provenance, membership, config controls, trace navigation and appraisal
          labels
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-relation
          - memory.md#mem-obj-community
          - runtime.md#rt-obj-simulation-config
          - memory.md#mem-obj-reasoning-trace
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-outcome-annotation
          - epistemic.md#epi-rte-prediction-resolution
          note: Fixed consumers use metadata, numeric fields and categorical labels for selection or computation.
        records:
        - memory.md#mem-obj-relation
        - memory.md#mem-obj-community
        - runtime.md#rt-obj-simulation-config
        - memory.md#mem-obj-reasoning-trace
        - epistemic.md#epi-rte-quality-diagnostics
        - epistemic.md#epi-rte-outcome-annotation
        - epistemic.md#epi-rte-prediction-resolution
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Retained action and external result wrappers
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-cross-platform-log
          - runtime.md#rt-rte-agent-mcp
          note: Action types, agent keys and RPC result structures are localized selection/dispatch material.
        records:
        - memory.md#mem-obj-cross-platform-log
        - runtime.md#rt-rte-agent-mcp
        note: Known wrappers do not classify every included remote result payload; text, numerical content
          and remote semantics remain unresolved.
      - scope: Provider-managed conversation and market/media payload parts
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-obj-relation
      - epistemic.md#epi-obj-entity-summaries
      - memory.md#mem-rte-community-rebuild
      - memory.md#mem-rte-round-history
      - runtime.md#rt-obj-agent-profiles
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-web-research
      - epistemic.md#epi-rte-ask-briefing
      - runtime.md#rt-rte-director-context
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-belief-state
      - memory.md#mem-obj-community
      - epistemic.md#epi-rte-graph-ranking
      - runtime.md#rt-obj-simulation-config
      - memory.md#mem-obj-reasoning-trace
      - epistemic.md#epi-rte-quality-diagnostics
      - epistemic.md#epi-rte-outcome-annotation
      - epistemic.md#epi-rte-prediction-resolution
      - memory.md#mem-obj-cross-platform-log
      - runtime.md#rt-rte-agent-mcp
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-rte-graph-retrieval
      note: Text, symbolic controls and dense vectors remain separate operative parts. Display text does
        not resolve opaque payloads.
    lineage:
      assessment: partial
      units:
      - scope: Round summaries, cross-platform digest and belief updates derived from recorded activity
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-obj-cross-platform-log
          - memory.md#mem-rte-belief-feedback
          note: Action/exposure records feed retained summaries, bounded activity tails and stance state
            for later use.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-obj-cross-platform-log
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Document episodes and caller-supplied director assumptions
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-episode
          - memory.md#mem-rte-graph-ingestion
          - runtime.md#rt-rte-director-context
          note: Submitted source text and caller scenario text enter retained state; caller identity does
            not prove human authorship.
        records:
        - memory.md#mem-obj-episode
        - memory.md#mem-rte-graph-ingestion
        - runtime.md#rt-rte-director-context
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Optional action-derived episodes/relations
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-graph-ingestion
          note: Rendered simulation activity is ingested into derived graph memory for subsequent retrieval.
        records:
        - memory.md#mem-rte-graph-ingestion
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Extraction, community labels, personas/configuration, reports and diagnostic derivatives
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-graph-ingestion
          - memory.md#mem-rte-community-rebuild
          - runtime.md#rt-rte-prepare-population
          - workflow.md#wf-rte-report-delivery
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-signal-derivation
          note: Models and fixed algorithms transform their supplied inputs into stored/reused outputs;
            this is not a claim of faithful entailment.
        records:
        - memory.md#mem-rte-graph-ingestion
        - memory.md#mem-rte-community-rebuild
        - runtime.md#rt-rte-prepare-population
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-quality-diagnostics
        - epistemic.md#epi-rte-signal-derivation
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Recorded report thoughts, tool observations and conclusions
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-reasoning-trace
          note: Recorder extracts emitted report-loop steps into an inspection graph, not private provider
            reasoning.
        records:
        - memory.md#mem-obj-reasoning-trace
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Initial document/ontology/config approval, model-only seed/enrichment provenance and exact
          embedding source provenance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-prepare-population
        - memory.md#mem-rte-graph-ingestion
        - epistemic.md#epi-rte-ask-briefing
        - epistemic.md#epi-rte-web-research
        - memory.md#mem-obj-relation
        note: Accepted records establish generation and ingestion paths but not all initial authorship
          or the provenance of model-only additions. No authored value follows solely from a caller label.
      - scope: Remote tool payload and uninspected auxiliary derivations
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-agent-mcp
        - memory.md#mem-rte-graph-retrieval
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-obj-cross-platform-log
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-episode
      - memory.md#mem-rte-graph-ingestion
      - runtime.md#rt-rte-director-context
      - memory.md#mem-rte-community-rebuild
      - runtime.md#rt-rte-prepare-population
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-quality-diagnostics
      - epistemic.md#epi-rte-signal-derivation
      - memory.md#mem-obj-reasoning-trace
      - epistemic.md#epi-rte-ask-briefing
      - epistemic.md#epi-rte-web-research
      - memory.md#mem-obj-relation
      - runtime.md#rt-rte-agent-mcp
      - memory.md#mem-rte-graph-retrieval
      note: Known derivation paths do not settle initial provenance or opaque enrichment. Trace-derived
        and other compilation findings describe distinct mechanisms, not exclusive system labels.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Round/action experience at compaction and belief update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-rte-belief-feedback
          note: Retained action/exposure experience feeds automatic revision of durable later-invocation
            context and checkpointed stance, independent of measured improvement.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Derived history/digest/stance at SocialAgent
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-obj-cross-platform-log
          - memory.md#mem-rte-belief-feedback
          note: Delivered retained experience supplies context about simulated history and attitudes.
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-rte-belief-feedback
          note: History-use directions and rendered stance guidance request changes to later posting/trading;
            delivery does not establish compliance.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-obj-cross-platform-log
        - memory.md#mem-rte-belief-feedback
        - runtime.md#rt-bap-agent-context
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Persona content and director interventions at agent prompts
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-obj-agent-profiles
          - runtime.md#rt-rte-director-context
          note: Retained persona assumptions and event reaction directions guide model invocations.
        records:
        - runtime.md#rt-obj-agent-profiles
        - runtime.md#rt-rte-director-context
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Graph text, embeddings and temporal/category controls at search
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-graph-retrieval
          - epistemic.md#epi-rte-graph-ranking
          note: Retained text/vectors influence relative query relevance under fixed search and optional
            reranking.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-graph-retrieval
          - epistemic.md#epi-rte-edge-invalidation
          note: Invalidation and kind/time metadata exclude edges on covered filtered paths; node/fallback/historical
            paths differ.
        records:
        - memory.md#mem-rte-graph-retrieval
        - epistemic.md#epi-rte-graph-ranking
        - epistemic.md#epi-rte-edge-invalidation
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Retrieved graph/community/research and saved reports/traces at requested consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-graph-retrieval
          - memory.md#mem-rte-community-rebuild
          - epistemic.md#epi-rte-web-research
          - workflow.md#wf-rte-report-delivery
          - memory.md#mem-obj-reasoning-trace
          note: Selected facts, overviews, biographies, reports and emitted trace records supply reference
            or inspection content; they are not verified truth by storage.
        records:
        - memory.md#mem-rte-graph-retrieval
        - memory.md#mem-rte-community-rebuild
        - epistemic.md#epi-rte-web-research
        - workflow.md#wf-rte-report-delivery
        - memory.md#mem-obj-reasoning-trace
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Config controls and matched checkpoint fields at driver/tracker
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-simulation-config
          - memory.md#mem-rte-belief-feedback
          note: Retained platform/time/activity controls and matching checkpoint agent IDs select future
            execution/state restoration.
        records:
        - runtime.md#rt-obj-simulation-config
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Retained quality and public outcome labels at gallery and signal consumers
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-outcome-annotation
          note: Gallery inclusion predicates consume retained health or annotation labels.
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-outcome-annotation
          - epistemic.md#epi-rte-signal-derivation
          note: Retained health/outcome categories select output risk/feed categories.
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-prediction-resolution
          - epistemic.md#epi-rte-outcome-annotation
          - epistemic.md#epi-rte-signal-derivation
          note: Diagnostics and caller-reference appraisals provide advisory display/summary inputs, not
            factual acceptance.
        records:
        - epistemic.md#epi-rte-quality-diagnostics
        - epistemic.md#epi-rte-outcome-annotation
        - epistemic.md#epi-rte-signal-derivation
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Complete retained criteria use, market/media effects and remote payload consumers
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-cross-platform-log
      - runtime.md#rt-bap-agent-context
      - runtime.md#rt-obj-agent-profiles
      - runtime.md#rt-rte-director-context
      - memory.md#mem-rte-graph-retrieval
      - epistemic.md#epi-rte-graph-ranking
      - epistemic.md#epi-rte-edge-invalidation
      - memory.md#mem-rte-community-rebuild
      - epistemic.md#epi-rte-web-research
      - workflow.md#wf-rte-report-delivery
      - memory.md#mem-obj-reasoning-trace
      - runtime.md#rt-obj-simulation-config
      - epistemic.md#epi-rte-quality-diagnostics
      - epistemic.md#epi-rte-outcome-annotation
      - epistemic.md#epi-rte-signal-derivation
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-obj-belief-state
      - runtime.md#rt-rte-agent-mcp
      note: Authority is local to each actual consumer; learning at updates and instruction/knowledge
        downstream are separate paths. No universal validation or enforcement follows from a schema, static
        prompt or API guard.
    write_agency:
      assessment: partial
      units:
      - scope: Software/model admission of round, belief, graph, community, persona, report, cache and
          diagnostic outputs
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-rte-belief-feedback
          - memory.md#mem-rte-graph-ingestion
          - memory.md#mem-rte-community-rebuild
          - runtime.md#rt-rte-prepare-population
          - workflow.md#wf-rte-report-delivery
          - epistemic.md#epi-rte-ask-briefing
          - epistemic.md#epi-rte-web-research
          - epistemic.md#epi-rte-quality-diagnostics
          - memory.md#mem-obj-reasoning-trace
          note: Code/model admits content without a separate human decision for each retained item. Workflow
            initiation is not per-content approval.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-rte-belief-feedback
        - memory.md#mem-rte-graph-ingestion
        - memory.md#mem-rte-community-rebuild
        - runtime.md#rt-rte-prepare-population
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-ask-briefing
        - epistemic.md#epi-rte-web-research
        - epistemic.md#epi-rte-quality-diagnostics
        - memory.md#mem-obj-reasoning-trace
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Caller document/ontology/config initialization, director/counterfactual inputs and appraisal
          replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-graph-ingestion
        - runtime.md#rt-obj-simulation-config
        - runtime.md#rt-rte-director-context
        - epistemic.md#epi-rte-outcome-annotation
        - epistemic.md#epi-rte-prediction-resolution
        note: Generic caller or authenticated administrator identity does not establish an explicit human
          content decision. No manual finding is licensed for these admissions.
      - scope: Dedicated-script and opaque host/remote admission mechanisms
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-rte-graph-ingestion
      - memory.md#mem-rte-community-rebuild
      - runtime.md#rt-rte-prepare-population
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-ask-briefing
      - epistemic.md#epi-rte-web-research
      - epistemic.md#epi-rte-quality-diagnostics
      - memory.md#mem-obj-reasoning-trace
      - runtime.md#rt-obj-simulation-config
      - runtime.md#rt-rte-director-context
      - epistemic.md#epi-rte-outcome-annotation
      - epistemic.md#epi-rte-prediction-resolution
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-obj-belief-state
      - runtime.md#rt-rte-agent-mcp
      - memory.md#mem-rte-graph-retrieval
      note: Known automatic transformations coexist with unresolved initialization/replacement control;
        physical file I/O is not the admission agency.
    curation_operations:
      assessment: partial
      units:
      - scope: Round/action history compression and batching
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          note: Recorded actions become reduced round/count/ancient summaries of existing experience,
            despite unresolved fidelity.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          note: Ancient batching deletes resident individual records and bounds retained detail.
        records:
        - memory.md#mem-rte-round-history
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Cross-platform retained action-tail maintenance
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-cross-platform-log
          note: Automatic trimming evicts older actions from bounded per-agent/platform tails.
        records:
        - memory.md#mem-obj-cross-platform-log
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Belief-state revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: Fixed-rule exposure/engagement updates revise existing stance, confidence and trust entries.
        records:
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Canonical entity admission/merge
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - epistemic.md#epi-rte-entity-resolution
          - memory.md#mem-rte-graph-ingestion
          note: Threshold and optional model identity matching fold entities into canonical MERGE identities;
            this does not deduplicate relation CREATE replays.
        records:
        - epistemic.md#epi-rte-entity-resolution
        - memory.md#mem-rte-graph-ingestion
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Old graph relation current-reliance withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - epistemic.md#epi-rte-edge-invalidation
          - memory.md#mem-rte-graph-ingestion
          note: Timestamping withdraws older relations from current filtered edge search while retaining
            historical text.
        records:
        - epistemic.md#epi-rte-edge-invalidation
        - memory.md#mem-rte-graph-ingestion
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Sampled community summarization and replacement
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-community-rebuild
          note: Member-description summaries reduce retained graph content for overviews; generated claim
            novelty is not established.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-community-rebuild
          note: Explicit rebuild replaces the existing community representation, without an atomic rollback
            guarantee.
        records:
        - memory.md#mem-rte-community-rebuild
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Novel-claim synthesis versus reshaping in model outputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-community-rebuild
        - memory.md#mem-rte-graph-ingestion
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-web-research
        note: Accepted records leave semantic entailment unresolved; a synthesis route name alone cannot
          establish the synthesize operation.
      - scope: Uninspected auxiliary maintenance and dedicated-driver alternatives
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-obj-cross-platform-log
      - memory.md#mem-rte-belief-feedback
      - epistemic.md#epi-rte-entity-resolution
      - memory.md#mem-rte-graph-ingestion
      - epistemic.md#epi-rte-edge-invalidation
      - memory.md#mem-rte-community-rebuild
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-web-research
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-obj-belief-state
      - runtime.md#rt-rte-agent-mcp
      - memory.md#mem-rte-graph-retrieval
      note: Supported curation survives unresolved branches. Indexing/embedding, primary-key checks and
        generation alone do not establish promote, dedup or synthesize.
    read_back_direction:
      assessment: partial
      units:
      - scope: Round scheduling to history, stance and cross-platform context
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-rte-belief-feedback
          - memory.md#mem-obj-cross-platform-log
          - runtime.md#rt-rte-synchronized-rounds
          note: Driver supplies selected retained context to active agents without their requesting that
            memory.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-rte-belief-feedback
        - memory.md#mem-obj-cross-platform-log
        - runtime.md#rt-rte-synchronized-rounds
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Pending external tool-result delivery
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-agent-mcp
          note: Model-authored mcp_call requests initiate dispatch; next-activation delivery fulfills
            those requests. Buffering and recipient matching do not add unsolicited selection.
        records:
        - runtime.md#rt-rte-agent-mcp
        note: The recorded request-to-result chain establishes pull within this delivery unit;
          no separate unsolicited result-selection operation is established.
      - scope: Graph, overview, trace, report, cache and appraisal requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-graph-retrieval
          - memory.md#mem-rte-community-rebuild
          - memory.md#mem-obj-reasoning-trace
          - workflow.md#wf-rte-report-delivery
          - epistemic.md#epi-rte-ask-briefing
          - epistemic.md#epi-rte-web-research
          - epistemic.md#epi-rte-quality-diagnostics
          - epistemic.md#epi-rte-outcome-annotation
          - epistemic.md#epi-rte-prediction-resolution
          note: Caller/model requests retained material; selection and response fulfill that request rather
            than adding an unsolicited graph push.
        records:
        - memory.md#mem-rte-graph-retrieval
        - memory.md#mem-rte-community-rebuild
        - memory.md#mem-obj-reasoning-trace
        - workflow.md#wf-rte-report-delivery
        - epistemic.md#epi-rte-ask-briefing
        - epistemic.md#epi-rte-web-research
        - epistemic.md#epi-rte-quality-diagnostics
        - epistemic.md#epi-rte-outcome-annotation
        - epistemic.md#epi-rte-prediction-resolution
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Profile/config/checkpoint reload within startup chain
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-prepare-population
          - runtime.md#rt-obj-simulation-config
          - memory.md#mem-rte-belief-feedback
          note: Runner/tracker requests stored files and matching checkpoint state for initialization;
            later prompt supply is separately classified.
        records:
        - runtime.md#rt-rte-prepare-population
        - runtime.md#rt-obj-simulation-config
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Provider history and incompletely traced auxiliary consumers
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-cross-platform-log
      - runtime.md#rt-rte-synchronized-rounds
      - runtime.md#rt-rte-agent-mcp
      - memory.md#mem-rte-graph-retrieval
      - memory.md#mem-rte-community-rebuild
      - memory.md#mem-obj-reasoning-trace
      - workflow.md#wf-rte-report-delivery
      - epistemic.md#epi-rte-ask-briefing
      - epistemic.md#epi-rte-web-research
      - epistemic.md#epi-rte-quality-diagnostics
      - epistemic.md#epi-rte-outcome-annotation
      - epistemic.md#epi-rte-prediction-resolution
      - runtime.md#rt-rte-prepare-population
      - runtime.md#rt-obj-simulation-config
      - memory.md#mem-obj-belief-state
      note: Both requested retrieval and automatic prompt delivery exist. Known directions do not close
        auxiliary or opaque host alternatives.
    read_back_signal:
      assessment: partial
      units:
      - scope: Common round-history push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          note: 'Trigger: round activation. Selector: available rounds and age windows/count fallback.
            Selected part: common recent/compacted/ancient history, not query-targeted facts.'
        records:
        - memory.md#mem-rte-round-history
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Per-agent stance and other-platform digest push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          - memory.md#mem-obj-cross-platform-log
          note: 'Trigger: active-agent invocation. Agent ID matches retained stance and cross-platform
            buckets; current platform excludes its own bucket.'
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-cross-platform-log
          note: Within matched buckets, fixed tail and preview limits choose the delivered recent action
            slice.
        records:
        - memory.md#mem-rte-belief-feedback
        - memory.md#mem-obj-cross-platform-log
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Pending RPC requested-result delivery
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-agent-mcp
        note: This bounded delivery chain fulfills the agent's tool request and is classified as pull.
          Agent-ID recipient matching does not establish an independent push selector, so a push
          signal is inapplicable here. Other unresolved host/remote routes remain separate.
      - scope: Market/media and opaque provider/host context selectors
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-cross-platform-log
      - runtime.md#rt-rte-agent-mcp
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-obj-belief-state
      - memory.md#mem-rte-graph-retrieval
      note: Only actual push selectors are classified here. Embedding/lexical graph ranking belongs to
        requested pull retrieval and does not establish a push signal.
    trace_learning:
      assessment: partial
      units:
      - scope: Round compaction into later history
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          note: Automatic trace-fed summaries are retained and supplied to later agent invocations, including
            within one resident run.
        records:
        - memory.md#mem-rte-round-history
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Checkpointed belief feedback
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: Action/exposure traces automatically revise durable stance/trust state whose labels reach
            subsequent agents and resume paths.
        records:
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Cross-platform bounded digest
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-cross-platform-log
          - runtime.md#rt-rte-synchronized-rounds
          note: Recorded actions automatically become retained targeted digests consumed as later context,
            without requiring new knowledge or measured benefit.
        records:
        - memory.md#mem-obj-cross-platform-log
        - runtime.md#rt-rte-synchronized-rounds
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Optional simulated-activity graph updates
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-graph-ingestion
          - memory.md#mem-rte-graph-retrieval
          note: Enabled updater automatically transforms action logs into retained graph content consumed
            by later profile/report retrieval.
        records:
        - memory.md#mem-rte-graph-ingestion
        - memory.md#mem-rte-graph-retrieval
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Raw report trace retention and external tool-result replay
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-reasoning-trace
        - runtime.md#rt-rte-agent-mcp
        note: Inspection/replay is wired but accepted records do not settle every result-specific durable
          behavior-shaping transformation; raw retention alone does not license a qualifying learning
          write.
      - scope: Market/media, dedicated-driver and opaque host alternatives
        assessment: uninspected
        findings: []
        records: *id001
        note: Included market/media transforms, dedicated-driver reset/resume alternatives, external host
          context management, and auxiliary browser/export/cache consumers are not fully characterized
          in accepted records. These parts remain included uncertainties; inspected routes do not establish
          an exhaustive inventory.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-rte-belief-feedback
      - memory.md#mem-obj-cross-platform-log
      - runtime.md#rt-rte-synchronized-rounds
      - memory.md#mem-rte-graph-ingestion
      - memory.md#mem-rte-graph-retrieval
      - memory.md#mem-obj-reasoning-trace
      - runtime.md#rt-rte-agent-mcp
      - memory.md#mem-obj-belief-state
      note: Positive qualifying routes do not establish universal coverage, observed improvement or parameter
        training. No system-wide no is inferred from missing evidence.
    trace_source:
      assessment: partial
      units:
      - scope: Round history, cross-platform digest and optional graph updater original inputs
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-round-history
          - memory.md#mem-obj-cross-platform-log
          - memory.md#mem-rte-graph-ingestion
          note: Original inputs are recorded simulated platform action requests/arguments and execution
            activity, not conversational session transcripts.
        records:
        - memory.md#mem-rte-round-history
        - memory.md#mem-obj-cross-platform-log
        - memory.md#mem-rte-graph-ingestion
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Belief feedback original action and exposure/engagement inputs
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: Explicit interaction actions and their execution feedback feed trust and fallback exposure
            updates.
        - value: event-streams
          basis: wired
          records:
          - memory.md#mem-rte-belief-feedback
          note: Recorded recommendation exposure and social engagement events feed post-round stance/confidence
            updates; approximate exposure is not proof of actual reading.
        records:
        - memory.md#mem-rte-belief-feedback
        note: The cited records establish the named inspected part, not successful operation.
      - scope: Mixed/opaque input provenance for incomplete analyzer, market/media and remote/host update
          alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-belief-feedback
        - runtime.md#rt-rte-agent-mcp
        - runtime.md#rt-rte-synchronized-rounds
        note: Full exposure construction and auxiliary writes are not inventoried. Saved trajectory outputs
          do not prove trajectories were learning inputs; tool results do not establish session-log origin.
      records:
      - memory.md#mem-rte-round-history
      - memory.md#mem-obj-cross-platform-log
      - memory.md#mem-rte-graph-ingestion
      - memory.md#mem-rte-belief-feedback
      - runtime.md#rt-rte-agent-mcp
      - runtime.md#rt-rte-synchronized-rounds
      note: Sources describe original consumed content on qualifying routes, not serialization or saved
        derivative filenames. Unresolved input origin remains local.
---

# MiroShark memory profile

## Comparison rationale

This profile classifies accepted records, not source execution. Every positive finding is wired implementation evidence; there is no supplied observed run or causal experiment. All axes remain partial because local witnesses do not close the retained-memory inventory or its auxiliary and host alternatives.

The comparison separates graph text, symbolic selection metadata and dense access vectors. Belief scalars are symbolic state, not model parameters. Persona/configuration files and caches count through reuse, not because all files are memory. Current observation filtering alone is outside the retained boundary; its later accumulated/derived uses remain covered by the round and belief routes. See [MEM-OBJ-agent-observation](memory.md#mem-obj-agent-observation), [MEM-OBJ-belief-state](memory.md#mem-obj-belief-state) and [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population).

Consolidation does not require a faithful observed output. The round and community mechanisms compress existing retained content, while entailment of particular generated claims remains unresolved. Neither an operation called synthesis nor missing fidelity evidence establishes a new claim absent from inputs. Entity resolution supports deduplication; exact-replay skipping in contradiction checking does not make relation creation deduplicated. See [MEM-RTE-round-history](memory.md#mem-rte-round-history), [MEM-RTE-community-rebuild](memory.md#mem-rte-community-rebuild), [EPI-RTE-entity-resolution](epistemic.md#epi-rte-entity-resolution) and [MEM-RTE-graph-ingestion](memory.md#mem-rte-graph-ingestion).

Learning authority at the update consumer is separate from knowledge or instruction at the subsequent agent. Qualifying trace learning includes resident continuation summaries because later invocations receive the retained result; cross-run serialization and observed benefit are not prerequisites. Saved trajectories and report traces are not automatically training inputs. Approximate exposure limits what belief feedback says about actual perception, without erasing its implemented update. See [MEM-RTE-belief-feedback](memory.md#mem-rte-belief-feedback), [MEM-OBJ-cross-platform-log](memory.md#mem-obj-cross-platform-log) and [MEM-OBJ-reasoning-trace](memory.md#mem-obj-reasoning-trace).

Requested graph search remains pull even though code ranks the response. Round scheduling independently pushes history, stance and cross-platform digests. Pending MCP results instead fulfill model-authored tool requests: delayed delivery and agent-ID recipient matching do not establish another push or an identifier push signal. This requested-result unit is pull, with its push signal inapplicable; independent round-context push and identifier findings remain. Embedding and lexical retrieval establish ranking authority but not inferred push signals. Temporal withdrawal enforces only covered edge-search paths; node/fallback/historical paths and copied summaries remain separate. See [MEM-RTE-graph-retrieval](memory.md#mem-rte-graph-retrieval), [EPI-RTE-graph-ranking](epistemic.md#epi-rte-graph-ranking) and [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp).

Reconciliation resolves duplicate relation, belief and community objects to memory declarations and resolves duplicate round-compaction, belief-revision and community-generation routes to their memory counterparts. Those canonical destinations supply all affected findings above. The narrower round-prose object remains a valid contained part, not a duplicate of the whole round store. No recorded unresolved cross-report conflict requires choosing a stronger status. Report synthesis receives truncated returned sections; it is not a semantic acceptance gate, and parallel workers do not consume sibling drafts. See [WF-RTE-report-delivery](workflow.md#wf-rte-report-delivery) and [RT-RTE-report-sections](runtime.md#rt-rte-report-sections).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required an additional read. Missing initial approval, exact remote payload provenance, complete analyzer/market-media processing and auxiliary consumer inventories prevent stronger assessments. These uncertainties do not establish absence, manual admission, universal withdrawal or improved future capacity.
