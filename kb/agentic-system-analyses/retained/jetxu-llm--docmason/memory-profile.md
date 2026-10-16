---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: DocMason memory profile of local document, interaction, linked-task and evaluator memory
  at the frozen repository boundary.
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
source-identity: https://github.com/JetXu-LLM/DocMason
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
memory-comparison:
  version: 2
  scope: Local retained source evidence and derived semantics/overlays/indexes; captured and pending/promoted
    interaction content/policy; linked later-turn briefs/control and hook reminders; retained answers/traces;
    runtime review/candidates and subsequent evaluator cases/baselines/results. Includes unresolved parser/attachment,
    initial-content control and answer-history consumer alternatives. Excludes static shipped instructions,
    adapter/core replacement, external host model weights/provider caches and native host context compaction.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Document evidence, semantics, overlays and reader/provenance indexes
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-source-evidence
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-semantic-overlay
          - memory.md#mem-obj-reader-index
          - runtime.md#rt-rte-sync-publish
          note: Staged/current directories and target-local JSON/text/assets are the retained substrate.
            Graph edges are file contents, not a separate graph database.
        records: *id001
        note: Staged/current directories and target-local JSON/text/assets are the retained substrate.
          Graph edges are file contents, not a separate graph database.
      - scope: Native ledgers/cursors, interaction entries and pending/promoted artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-interaction-policy
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          note: Runtime JSON and per-memory staging/current directories persist these parts; provider
            parser variants do not establish a different retained substrate.
        records: *id002
        note: Runtime JSON and per-memory staging/current directories persist these parts; provider parser
          variants do not establish a different retained substrate.
      - scope: Linked task control, publication selection and canonical answer files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-obj-publish-pointer
          - epistemic.md#epi-obj-answer
          - runtime.md#rt-rte-host-hooks
          note: Filesystem control and separate answer Markdown remain available to linked later invocations.
        records: *id003
        note: Filesystem control and separate answer Markdown remain available to linked later invocations.
      - scope: Review projections, candidates, regression drafts/cases, baselines and evaluation results
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-benchmark-candidates
          - memory.md#mem-rte-review-projection
          - runtime.md#rt-rte-operator-eval
          note: Runtime review/evaluation JSON and scorecard files feed subsequent review and replay.
        records: *id004
        note: Runtime review/evaluation JSON and scorecard files feed subsequent review and replay.
      records:
      - memory.md#mem-obj-source-evidence
      - memory.md#mem-obj-knowledge-text
      - memory.md#mem-obj-semantic-overlay
      - memory.md#mem-obj-reader-index
      - runtime.md#rt-rte-sync-publish
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-obj-interaction-policy
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-obj-publish-pointer
      - epistemic.md#epi-obj-answer
      - runtime.md#rt-rte-host-hooks
      - memory.md#mem-obj-benchmark-candidates
      - memory.md#mem-rte-review-projection
      - runtime.md#rt-rte-operator-eval
      note: The accepted inventory identifies local file storage across the included memory surfaces.
        External host/provider state, static instruction projection and core replacement are excluded,
        not silently classified as file memory.
    representational_form:
      assessment: partial
      units:
      - scope: Textual document evidence and semantic content at host interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-source-evidence
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-semantic-overlay
          note: Extracted text, summaries, statements, labels and uncertainty are interpreted by the host.
        records: *id005
        note: Extracted text, summaries, statements, labels and uncertainty are interpreted by the host.
      - scope: Source renders/media and parser-specific evidence representations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-source-evidence
        note: Records establish retained assets but do not classify every parser-specific representation
          or binary interpretation path; text does not resolve this included branch.
      - scope: Reader text versus fixed-rule access/provenance metadata
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-reader-index
          - memory.md#mem-obj-interaction-policy
          - epistemic.md#epi-rte-memory-selection
          note: Copied search strings retain linguistic content at host consumption.
        - value: symbolic
          basis: wired
          records: *id006
          note: Localized IDs, graph edges, policies and numerical scores have fixed-rule consumers; scores
            are not distributed parameters.
        records: *id006
        note: Both inspected parts have explicit consumption paths; no embedding representation is recorded.
      - scope: Native/interaction excerpts and derived semantic text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-knowledge-text
          note: User text, assistant excerpts and retained semantic summaries are linguistic trace/context
            content.
        records: *id007
        note: User text, assistant excerpts and retained semantic summaries are linguistic trace/context
          content.
      - scope: Capture recovery, interaction policy and linked task/publication control
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-obj-interaction-policy
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-obj-publish-pointer
          note: Cursor offsets/checksums, IDs, gate/closure fields, usage metadata and publication pointers
            are fixed-rule state.
        records: *id008
        note: Cursor offsets/checksums, IDs, gate/closure fields, usage metadata and publication pointers
          are fixed-rule state.
      - scope: Linked work briefs and continuation guidance at host consumption
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-rte-host-hooks
          note: Memory annotations establish host-interpreted brief content and advisory reminders, distinct
            from IDs interpreted by Python.
        records: *id009
        note: Memory annotations establish host-interpreted brief content and advisory reminders, distinct
          from IDs interpreted by Python.
      - scope: Candidate reasons/questions and evaluator case/control fields
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - memory.md#mem-obj-benchmark-candidates
          - runtime.md#rt-rte-operator-eval
          note: Operators/hosts interpret retained questions and reasons.
        - value: symbolic
          basis: wired
          records: *id010
          note: Promotion/replay interprets case IDs, expected states, baselines and scores by fixed rules.
        records: *id010
        note: The review/evaluation surface has both recorded consumption paths.
      - scope: Persisted answer text at later tracing/review
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - epistemic.md#epi-obj-answer
          - runtime.md#rt-rte-evidence-tools
          - memory.md#mem-rte-review-projection
          note: Answer Markdown remains a separate linguistic artifact, not content inside the symbolic
            turn binding.
        records: *id011
        note: Answer Markdown remains a separate linguistic artifact, not content inside the symbolic
          turn binding.
      records:
      - memory.md#mem-obj-source-evidence
      - memory.md#mem-obj-knowledge-text
      - memory.md#mem-obj-semantic-overlay
      - memory.md#mem-obj-reader-index
      - memory.md#mem-obj-interaction-policy
      - epistemic.md#epi-rte-memory-selection
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-interaction-entry
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-obj-publish-pointer
      - runtime.md#rt-rte-host-hooks
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-rte-operator-eval
      - epistemic.md#epi-obj-answer
      - runtime.md#rt-rte-evidence-tools
      - memory.md#mem-rte-review-projection
      note: Text and symbolic routes are resolved; source renders/media and parser-specific representations
        prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Imported document evidence derivation
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records: &id012
          - memory.md#mem-obj-source-evidence
          - runtime.md#rt-rte-sync-publish
          note: Documents enter from corpus placement/sample materialization and are parsed/rendered by
            software; exact private-document authorship and initial installation provenance remain unavailable.
        - value: other-compiled
          basis: wired
          records: *id012
          note: Documents enter from corpus placement/sample materialization and are parsed/rendered by
            software; exact private-document authorship and initial installation provenance remain unavailable.
        records: *id012
        note: Documents enter from corpus placement/sample materialization and are parsed/rendered by
          software; exact private-document authorship and initial installation provenance remain unavailable.
      - scope: Deterministic source semantics and index construction
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id013
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-reader-index
          - epistemic.md#epi-rte-conservative-output
          note: Python constructs conservative semantics and reader artifacts from retained evidence,
            independently of unresolved original authorship.
        records: *id013
        note: Python constructs conservative semantics and reader artifacts from retained evidence, independently
          of unresolved original authorship.
      - scope: Requested host semantic enrichment and overlays
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id014
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-semantic-overlay
          - runtime.md#rt-rte-hybrid-refresh
          note: Canonical construction requests host-authored semantic statements and additive overlays;
            no authored execution instance is supplied.
        records: *id014
        note: The requested authoring path is classifiable at claimed strength, not upgraded by deterministic
          publication wiring.
      - scope: Native capture, pending/promoted interaction semantics and policy
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records: &id015
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          - memory.md#mem-obj-interaction-policy
          note: Recorded sessions feed normalized excerpts, derived metadata and semantic summaries. Individual
            provider parsers/attachments remain uninspected, preventing complete provenance of every included
            payload.
        records: *id015
        note: Recorded sessions feed normalized excerpts, derived metadata and semantic summaries. Individual
          provider parsers/attachments remain uninspected, preventing complete provenance of every included
          payload.
      - scope: Runtime review projections and benchmark candidates
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - memory.md#mem-obj-benchmark-candidates
          - memory.md#mem-rte-review-projection
          note: Captured conversation/tool state is filtered/grouped into retained review/candidate content.
        records: *id016
        note: Captured conversation/tool state is filtered/grouped into retained review/candidate content.
      - scope: Candidate-derived regression drafts/cases
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id017
          - memory.md#mem-obj-benchmark-candidates
          - runtime.md#rt-rte-operator-eval
          note: Promotion mechanically derives proposed cases from trace-derived candidates; explicit
            selection is separate from this derivation.
        - value: other-compiled
          basis: wired
          records: *id017
          note: Promotion mechanically derives proposed cases from trace-derived candidates; explicit
            selection is separate from this derivation.
        records: *id017
        note: Promotion mechanically derives proposed cases from trace-derived candidates; explicit selection
          is separate from this derivation.
      - scope: Initial suites, reference facts, supplied judgments and baselines
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-operator-eval
        note: The record establishes supplied evaluator inputs and baseline freezing but does not resolve
          every initial content provenance; it cannot establish authored versus imported lineage for the
          whole branch.
      - scope: Linked work briefs, canonical answer and control state
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id018
          - runtime.md#rt-obj-canonical-turn
          - epistemic.md#epi-obj-answer
          - runtime.md#rt-rte-canonical-ask
          note: The host supplies answer text and semantic work-brief deltas.
        - value: other-compiled
          basis: wired
          records: *id018
          note: Python merges explicit projections and persists normalized task binding.
        records: *id018
        note: Host content authorship and deterministic control construction remain separate findings.
      records:
      - memory.md#mem-obj-source-evidence
      - runtime.md#rt-rte-sync-publish
      - memory.md#mem-obj-knowledge-text
      - memory.md#mem-obj-reader-index
      - epistemic.md#epi-rte-conservative-output
      - memory.md#mem-obj-semantic-overlay
      - runtime.md#rt-rte-hybrid-refresh
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-obj-interaction-policy
      - memory.md#mem-obj-benchmark-candidates
      - memory.md#mem-rte-review-projection
      - runtime.md#rt-rte-operator-eval
      - runtime.md#rt-obj-canonical-turn
      - epistemic.md#epi-obj-answer
      - runtime.md#rt-rte-canonical-ask
      note: Known derivations do not resolve initial document/evaluator provenance or all native-provider/attachment
        paths.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Evidence and semantics delivered to answering/authoring hosts
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id019
          - memory.md#mem-obj-source-evidence
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-semantic-overlay
          - memory.md#mem-obj-interaction-entry
          - runtime.md#rt-rte-evidence-tools
          note: Retained evidence and semantic text supply context/reference; delivery does not prove
            compliance or factual truth.
        records: *id019
        note: Retained evidence and semantic text supply context/reference; delivery does not prove compliance
          or factual truth.
      - scope: Reader search content and interaction policy at retrieval
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id020
          - memory.md#mem-obj-reader-index
          - memory.md#mem-obj-interaction-policy
          - epistemic.md#epi-rte-memory-selection
          note: Retained search text and rank priors influence relative retrieval priority.
        - value: routing
          basis: wired
          records: *id020
          note: Source IDs, graph/channel metadata and memory modes constrain selected evidence scope.
        - value: enforcement
          basis: wired
          records: *id020
          note: Interaction-family policy excludes material for external-factual and workspace-minimal
            queries.
        records: *id020
        note: These are distinct fixed-reader effects; contextual-only is not a universal support veto.
      - scope: Linked gate/scope/closure fields and publication pointer
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id021
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-obj-publish-pointer
          - runtime.md#rt-rte-canonical-ask
          - runtime.md#rt-clm-commit-gate
          note: Retained task/publication identities select continuation, workflow scope and current root.
        - value: validation
          basis: wired
          records: *id021
          note: Accepted scopes, support/version bindings and turn state determine canonical admissibility.
        - value: enforcement
          basis: wired
          records: *id021
          note: Committed/waiting/illegal binding states block invoked canonical progression.
        records: *id021
        note: Control force is bounded to cooperating invoked paths, not arbitrary host filesystem actions.
      - scope: Work briefs and advisory continuation text at later host invocation
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id022
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-rte-host-hooks
          note: Brief content supplies task context; selected continuation guidance directs exact revision/gate
            use. Optional delivery is wired, host adherence unobserved.
        - value: instruction
          basis: wired
          records: *id022
          note: Brief content supplies task context; selected continuation guidance directs exact revision/gate
            use. Optional delivery is wired, host adherence unobserved.
        records: *id022
        note: Brief content supplies task context; selected continuation guidance directs exact revision/gate
          use. Optional delivery is wired, host adherence unobserved.
      - scope: Overlay fingerprints and slots at coverage evaluation
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id023
          - memory.md#mem-obj-semantic-overlay
          - epistemic.md#epi-rte-overlay-coverage
          note: Persisted fingerprints/slot claims determine coverage credit and remaining follow-up work,
            not universal stale-text quarantine.
        - value: routing
          basis: wired
          records: *id023
          note: Persisted fingerprints/slot claims determine coverage credit and remaining follow-up work,
            not universal stale-text quarantine.
        records: *id023
        note: Persisted fingerprints/slot claims determine coverage credit and remaining follow-up work,
          not universal stale-text quarantine.
      - scope: Native cursor and entry bookkeeping at reconciliation/promotion
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id024
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          note: Retained cursor/entry status selects recovery, capture and eligible promotion inputs.
        records: *id024
        note: Retained cursor/entry status selects recovery, capture and eligible promotion inputs.
      - scope: Retained sessions/entries at automatic semantic and projection updates
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id025
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-rte-interaction-promotion
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-benchmark-candidates
          - memory.md#mem-rte-review-projection
          note: Retained trace content feeds durable context/semantic/candidate artifacts with later consumers;
            this update authority does not establish improved capacity.
        records: *id025
        note: Retained trace content feeds durable context/semantic/candidate artifacts with later consumers;
          this update authority does not establish improved capacity.
      - scope: Review/candidate content at operator and case-generation consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id026
          - memory.md#mem-obj-benchmark-candidates
          - memory.md#mem-rte-review-projection
          - runtime.md#rt-rte-operator-eval
          note: Questions/reasons advise review, retained priorities order candidates, and candidates
            feed durable regression cases consumed later.
        - value: ranking
          basis: wired
          records: *id026
          note: Questions/reasons advise review, retained priorities order candidates, and candidates
            feed durable regression cases consumed later.
        - value: learning
          basis: wired
          records: *id026
          note: Questions/reasons advise review, retained priorities order candidates, and candidates
            feed durable regression cases consumed later.
        records: *id026
        note: Questions/reasons advise review, retained priorities order candidates, and candidates feed
          durable regression cases consumed later.
      - scope: Regression expectations, reference facts and frozen baseline at later replay
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id027
          - runtime.md#rt-rte-operator-eval
          note: References supply judging context; expected-state/baseline fields determine bounded replay
            conformity and comparisons, not corpus truth.
        - value: validation
          basis: wired
          records: *id027
          note: References supply judging context; expected-state/baseline fields determine bounded replay
            conformity and comparisons, not corpus truth.
        records: *id027
        note: References supply judging context; expected-state/baseline fields determine bounded replay
          conformity and comparisons, not corpus truth.
      - scope: Persisted answer and trace outcomes at later tracing/closure
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id028
          - epistemic.md#epi-obj-answer
          - runtime.md#rt-rte-evidence-tools
          - runtime.md#rt-clm-commit-gate
          note: Answer text is the support-check target; retained trace/support results license or refuse
            a declared closure label.
        - value: validation
          basis: wired
          records: *id028
          note: Answer text is the support-check target; retained trace/support results license or refuse
            a declared closure label.
        records: *id028
        note: Answer text is the support-check target; retained trace/support results license or refuse
          a declared closure label.
      - scope: Untraced answer-history and alternate attachment/provider consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-review-projection
        - memory.md#mem-obj-native-ledger
        - memory.md#mem-obj-source-evidence
        note: Records retain incomplete consumer/capture coverage; no complete authority union for these
          alternatives can be asserted.
      records:
      - memory.md#mem-obj-source-evidence
      - memory.md#mem-obj-knowledge-text
      - memory.md#mem-obj-semantic-overlay
      - memory.md#mem-obj-interaction-entry
      - runtime.md#rt-rte-evidence-tools
      - memory.md#mem-obj-reader-index
      - memory.md#mem-obj-interaction-policy
      - epistemic.md#epi-rte-memory-selection
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-obj-publish-pointer
      - runtime.md#rt-rte-canonical-ask
      - runtime.md#rt-clm-commit-gate
      - runtime.md#rt-rte-host-hooks
      - epistemic.md#epi-rte-overlay-coverage
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-obj-benchmark-candidates
      - memory.md#mem-rte-review-projection
      - runtime.md#rt-rte-operator-eval
      - epistemic.md#epi-obj-answer
      note: Each force is attached to its actual consumer. Untraced history/provider/asset alternatives
        prevent complete authority enumeration.
    write_agency:
      assessment: partial
      units:
      - scope: Initial live corpus supply
        assessment: partial
        findings:
        - value: manual
          basis: afforded
          records: &id029
          - memory.md#mem-obj-source-evidence
          note: Operator corpus placement explicitly supplies documents; the shipped sample driver is
            an alternative materialization route.
        records: *id029
        note: Operator placement is afforded, but generic caller identity and unknown private installation
          control do not resolve every initial content admission.
      - scope: Build, conservative semantics, indexes and publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id030
          - runtime.md#rt-rte-sync-publish
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-reader-index
          - epistemic.md#epi-rte-conservative-output
          note: Software proposes/transforms/adopts after checks; initiating sync is not per-assertion
            human approval.
        records: *id030
        note: Software proposes/transforms/adopts after checks; initiating sync is not per-assertion human
          approval.
      - scope: Host semantic text/overlay proposal
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id031
          - memory.md#mem-obj-knowledge-text
          - memory.md#mem-obj-semantic-overlay
          - runtime.md#rt-rte-hybrid-refresh
          note: The instructed host model authors enrichment without a per-content human decision; the
            authoring execution is not supplied.
        records: *id031
        note: Keep requested model admission separate from the wired software publication branch.
      - scope: Native reconciliation, derived pending/promoted content and maintenance
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id032
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-interaction-policy
          note: Python admits entries, grouping and metadata; user messages provide content but do not
            approve each derived memory.
        records: *id032
        note: Python admits entries, grouping and metadata; user messages provide content but do not approve
          each derived memory.
      - scope: Linked control normalization and hook continuation claim
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id033
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-rte-canonical-ask
          - runtime.md#rt-rte-host-hooks
          note: Python normalizes/persists bindings and one-shot claims; user gate decisions are a separate
            route.
        records: *id033
        note: Python normalizes/persists bindings and one-shot claims; user gate decisions are a separate
          route.
      - scope: Explicit user gate/scope decisions
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id034
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-rte-canonical-ask
          note: The recorded decision/confirmation route requires a user decision for accepted task scope,
            not for every generated answer claim.
        records: *id034
        note: The recorded decision/confirmation route requires a user decision for accepted task scope,
          not for every generated answer claim.
      - scope: Review projection and candidate extraction
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id035
          - memory.md#mem-rte-review-projection
          - memory.md#mem-obj-benchmark-candidates
          note: Software filters/groups traces and writes candidates independently of later promotion
            selection.
        records: *id035
        note: Software filters/groups traces and writes candidates independently of later promotion selection.
      - scope: Candidate promotion and baseline replacement control
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-operator-eval
        note: An explicit request selects cases/run, but generic request-file identity does not establish
          human per-content approval versus automated admission control.
      - scope: Initial suites/references and host answer/work-brief admission
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-operator-eval
        - epistemic.md#epi-obj-answer
        - runtime.md#rt-obj-canonical-turn
        note: Supplied evaluator inputs and host-authored content are recorded, but all initial/control
          decisions are not specified; authorship alone cannot settle agency.
      records:
      - memory.md#mem-obj-source-evidence
      - runtime.md#rt-rte-sync-publish
      - memory.md#mem-obj-knowledge-text
      - memory.md#mem-obj-reader-index
      - epistemic.md#epi-rte-conservative-output
      - memory.md#mem-obj-semantic-overlay
      - runtime.md#rt-rte-hybrid-refresh
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-obj-interaction-policy
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-rte-canonical-ask
      - runtime.md#rt-rte-host-hooks
      - memory.md#mem-rte-review-projection
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-rte-operator-eval
      - epistemic.md#epi-obj-answer
      note: Automatic transformations and explicit human decisions coexist with unresolved initialization
        and request-control mechanisms.
    curation_operations:
      assessment: partial
      units:
      - scope: Interaction capture upsert, duplicate repair and grouped semantics
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id036
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-knowledge-text
          note: Stable entries are upserted, duplicates repaired/merged, turns compressed into grouped
            summaries, and pending evidence raised to published participation after validation. Promotion
            is a tier change, not truth endorsement.
        - value: dedup
          basis: wired
          records: *id036
          note: Stable entries are upserted, duplicates repaired/merged, turns compressed into grouped
            summaries, and pending evidence raised to published participation after validation. Promotion
            is a tier change, not truth endorsement.
        - value: consolidate
          basis: wired
          records: *id036
          note: Stable entries are upserted, duplicates repaired/merged, turns compressed into grouped
            summaries, and pending evidence raised to published participation after validation. Promotion
            is a tier change, not truth endorsement.
        - value: promote
          basis: wired
          records: *id036
          note: Stable entries are upserted, duplicates repaired/merged, turns compressed into grouped
            summaries, and pending evidence raised to published participation after validation. Promotion
            is a tier change, not truth endorsement.
        records: *id036
        note: Stable entries are upserted, duplicates repaired/merged, turns compressed into grouped summaries,
          and pending evidence raised to published participation after validation. Promotion is a tier
          change, not truth endorsement.
      - scope: Audit-only suppression and orphan removal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id037
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          - epistemic.md#epi-rte-orphan-cleanup
          note: Suppression withdraws pending reader reliance while retaining audit history; orphan pruning
            deletes retained groups. Neither withdraws all already-promoted subclaims.
        - value: decay
          basis: wired
          records: *id037
          note: Suppression withdraws pending reader reliance while retaining audit history; orphan pruning
            deletes retained groups. Neither withdraws all already-promoted subclaims.
        records: *id037
        note: Suppression withdraws pending reader reliance while retaining audit history; orphan pruning
          deletes retained groups. Neither withdraws all already-promoted subclaims.
      - scope: Conservative source semantics
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id038
          - memory.md#mem-obj-knowledge-text
          - epistemic.md#epi-rte-conservative-output
          note: Selected snippets are compressed; the generic inclusion proposition is new relative to
            source claims, though entailed by staged-input membership. Synthesis here does not mean ampliative
            truth production.
        - value: synthesize
          basis: wired
          records: *id038
          note: Selected snippets are compressed; the generic inclusion proposition is new relative to
            source claims, though entailed by staged-input membership. Synthesis here does not mean ampliative
            truth production.
        records: *id038
        note: Selected snippets are compressed; the generic inclusion proposition is new relative to source
          claims, though entailed by staged-input membership. Synthesis here does not mean ampliative
          truth production.
      - scope: Overlay coverage withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id039
          - memory.md#mem-obj-semantic-overlay
          - epistemic.md#epi-rte-overlay-coverage
          note: Changed fingerprints withdraw coverage reliance while files may remain; universal reader
            suppression is unresolved.
        records: *id039
        note: Changed fingerprints withdraw coverage reliance while files may remain; universal reader
          suppression is unresolved.
      - scope: Publication-root cleanup
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id040
          - runtime.md#rt-obj-publish-pointer
          note: Successful pruning removes old physical retained roots; logical ledger history is not
            a complete snapshot archive.
        records: *id040
        note: Successful pruning removes old physical retained roots; logical ledger history is not a
          complete snapshot archive.
      - scope: Runtime review/candidate projection
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id041
          - memory.md#mem-rte-review-projection
          - memory.md#mem-obj-benchmark-candidates
          note: Trace grouping produces reduced review summaries and new candidate-case suggestions; removed
            live files remove projection mirrors. Raw-log cleanup is not fully traced.
        - value: synthesize
          basis: wired
          records: *id041
          note: Trace grouping produces reduced review summaries and new candidate-case suggestions; removed
            live files remove projection mirrors. Raw-log cleanup is not fully traced.
        - value: decay
          basis: wired
          records: *id041
          note: Trace grouping produces reduced review summaries and new candidate-case suggestions; removed
            live files remove projection mirrors. Raw-log cleanup is not fully traced.
        records: *id041
        note: Trace grouping produces reduced review summaries and new candidate-case suggestions; removed
          live files remove projection mirrors. Raw-log cleanup is not fully traced.
      - scope: Requested host source/overlay transformation semantics
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-knowledge-text
        - memory.md#mem-obj-semantic-overlay
        - runtime.md#rt-rte-hybrid-refresh
        note: Authoring is requested, but no actual premise/output pair establishes which controlled transformation
          the host performs; route names cannot settle it.
      - scope: Provider-tail, attachment, cache and answer-history maintenance alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-native-ledger
        - memory.md#mem-obj-reader-index
        - memory.md#mem-rte-review-projection
        - memory.md#mem-obj-source-evidence
        note: Parser tail checkpointing is described, but complete alternate maintenance transformations
          are not assessed. Index rebuild/acquisition alone is not curation.
      records:
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-obj-knowledge-text
      - epistemic.md#epi-rte-orphan-cleanup
      - epistemic.md#epi-rte-conservative-output
      - memory.md#mem-obj-semantic-overlay
      - epistemic.md#epi-rte-overlay-coverage
      - runtime.md#rt-obj-publish-pointer
      - memory.md#mem-rte-review-projection
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-rte-hybrid-refresh
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-reader-index
      - memory.md#mem-obj-source-evidence
      note: Implemented transformations support positive operations locally; opaque semantic authoring
        and incompletely traced maintenance prevent a complete list.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested published/pending retrieve and provenance trace
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id042
          - runtime.md#rt-rte-evidence-tools
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-reader-index
          note: The consumer requests evidence or a specified trace; delivery fulfilling that request
            is not an additional push.
        records: *id042
        note: The consumer requests evidence or a specified trace; delivery fulfilling that request is
          not an additional push.
      - scope: Explicit linked ask continuation and gate resolution
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id043
          - runtime.md#rt-obj-canonical-turn
          - runtime.md#rt-rte-canonical-ask
          note: Explicit revision/gate anchors request continued task state, distinct from optional automatic
            prompt reminders.
        records: *id043
        note: Explicit revision/gate anchors request continued task state, distinct from optional automatic
          prompt reminders.
      - scope: Optional prompt-hook advisory continuation supply
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id044
          - runtime.md#rt-rte-host-hooks
          - runtime.md#rt-obj-canonical-turn
          note: Prompt event and bound state automatically select linked task/gate/scope reminders without
            a separate memory request.
        records: *id044
        note: Prompt event and bound state automatically select linked task/gate/scope reminders without
          a separate memory request.
      - scope: Requested runtime review and regression replay/promotion
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id045
          - memory.md#mem-rte-review-projection
          - memory.md#mem-obj-benchmark-candidates
          - runtime.md#rt-rte-operator-eval
          note: Explicit review/action requests load retained summaries, candidates, cases and baselines;
            background projection writes are not themselves host delivery.
        records: *id045
        note: Explicit review/action requests load retained summaries, candidates, cases and baselines;
          background projection writes are not themselves host delivery.
      - scope: Untraced answer-history and provider/attachment consumer alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-review-projection
        - memory.md#mem-obj-native-ledger
        - memory.md#mem-obj-source-evidence
        note: Records do not establish every later consumer route for these included retained parts.
      records:
      - runtime.md#rt-rte-evidence-tools
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-obj-reader-index
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-rte-canonical-ask
      - runtime.md#rt-rte-host-hooks
      - memory.md#mem-rte-review-projection
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-rte-operator-eval
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-source-evidence
      note: Both requested retrieval and automatic advisory supply are wired; incomplete alternative consumer
        coverage remains local.
    read_back_signal:
      assessment: partial
      units:
      - scope: Prompt-hook linked task targeting
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id046
          - runtime.md#rt-rte-host-hooks
          - runtime.md#rt-obj-canonical-turn
          note: On prompt submission the bound session/task linkage selects matching canonical state and
            scope/gate IDs; latest-linked-turn selection is coarse recency within that identity-bound
            set. No token budget or embedding selector is recorded.
        - value: coarse
          basis: wired
          records: *id046
          note: On prompt submission the bound session/task linkage selects matching canonical state and
            scope/gate IDs; latest-linked-turn selection is coarse recency within that identity-bound
            set. No token budget or embedding selector is recorded.
        records: *id046
        note: On prompt submission the bound session/task linkage selects matching canonical state and
          scope/gate IDs; latest-linked-turn selection is coarse recency within that identity-bound set.
          No token budget or embedding selector is recorded.
      - scope: Requested evidence, continuation, review and evaluation routes
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-evidence-tools
        - runtime.md#rt-obj-canonical-turn
        - memory.md#mem-rte-review-projection
        - runtime.md#rt-rte-operator-eval
        note: These units fulfill explicit requests; their lexical ranking and requested IDs are not push
          signals.
      - scope: Untraced later-consumer alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-review-projection
        - memory.md#mem-obj-native-ledger
        - memory.md#mem-obj-source-evidence
        note: Whether additional push operations and selectors exist in these alternatives is not established
          by accepted records.
      records:
      - runtime.md#rt-rte-host-hooks
      - runtime.md#rt-obj-canonical-turn
      - runtime.md#rt-rte-evidence-tools
      - memory.md#mem-rte-review-projection
      - runtime.md#rt-rte-operator-eval
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-source-evidence
      note: A positive targeted hook route cannot make untraced alternatives inapplicable; pull lexical
        selection is not inferred-lexical push.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic pending interaction projection and published semantics
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records: &id047
          - memory.md#mem-rte-native-capture
          - memory.md#mem-obj-interaction-entry
          - epistemic.md#epi-rte-pending-overlay
          - memory.md#mem-rte-interaction-promotion
          - memory.md#mem-obj-knowledge-text
          - runtime.md#rt-rte-evidence-tools
          note: Recorded conversational turns feed automatic retained context/semantic writes with later
            retrieve/host consumers. Individual provider/attachment inputs are not fully inspected; this
            is wired trace learning, not demonstrated improved capacity.
        records: *id047
        note: Recorded conversational turns feed automatic retained context/semantic writes with later
          retrieve/host consumers. Individual provider/attachment inputs are not fully inspected; this
          is wired trace learning, not demonstrated improved capacity.
      - scope: Automatic runtime review/candidate production
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id048
          - memory.md#mem-rte-review-projection
          - memory.md#mem-obj-benchmark-candidates
          - runtime.md#rt-rte-operator-eval
          note: Captured session/tool state automatically produces retained review/candidate artifacts
            read by later review and case-generation consumers. Case promotion control remains separately
            unresolved.
        records: *id048
        note: Captured session/tool state automatically produces retained review/candidate artifacts read
          by later review and case-generation consumers. Case promotion control remains separately unresolved.
      - scope: Linked work-brief revision and native capture recovery alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-canonical-turn
        - memory.md#mem-obj-native-ledger
        note: Explicit host-authored brief deltas and parser tail checkpointing do not themselves establish
          an automatic trace-fed behavior-shaping summary; complete qualifying input/update paths are
          not recorded.
      - scope: Source-document semantic compilation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-source-evidence
        - epistemic.md#epi-rte-conservative-output
        - memory.md#mem-obj-knowledge-text
        note: Imported document content is not necessarily activity trace content. Private payload origins
          are unknown, so neither a positive nor bounded no is supported across this unit.
      - scope: Evaluator case/baseline adoption
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-operator-eval
        - memory.md#mem-obj-benchmark-candidates
        note: Trace-derived cases have a later consumer, but explicit request control is unresolved; automatic
          candidate production does not settle downstream adoption agency.
      records:
      - memory.md#mem-rte-native-capture
      - memory.md#mem-obj-interaction-entry
      - epistemic.md#epi-rte-pending-overlay
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-obj-knowledge-text
      - runtime.md#rt-rte-evidence-tools
      - memory.md#mem-rte-review-projection
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-rte-operator-eval
      - runtime.md#rt-obj-canonical-turn
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-obj-source-evidence
      - epistemic.md#epi-rte-conservative-output
      note: Positive automatic trace-fed context/candidate paths coexist with unresolved update/input
        routes. No bounded absence record establishes a local or system-wide no.
    trace_source:
      assessment: partial
      units:
      - scope: Interaction pending/promoted context write inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records: &id049
          - memory.md#mem-obj-interaction-entry
          - memory.md#mem-obj-native-ledger
          - memory.md#mem-rte-native-capture
          - memory.md#mem-rte-interaction-promotion
          note: User turns and bounded assistant excerpts originate in recorded sessions, not event streams
            merely because hooks reconcile them. Provider parsing, attachments and tool-audit content
            used by derived metadata are incompletely inspected, preventing exhaustive source classification.
        records: *id049
        note: User turns and bounded assistant excerpts originate in recorded sessions, not event streams
          merely because hooks reconcile them. Provider parsing, attachments and tool-audit content used
          by derived metadata are incompletely inspected, preventing exhaustive source classification.
      - scope: Runtime review/candidate write inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id050
          - memory.md#mem-rte-review-projection
          - memory.md#mem-obj-benchmark-candidates
          note: Captured conversation records and linked retrieval/trace outcomes feed review and candidate
            filtering. No linked states/actions/outcomes experience route establishes trajectories.
        - value: tool-traces
          basis: wired
          records: *id050
          note: Captured conversation records and linked retrieval/trace outcomes feed review and candidate
            filtering. No linked states/actions/outcomes experience route establishes trajectories.
        records: *id050
        note: Captured conversation records and linked retrieval/trace outcomes feed review and candidate
          filtering. No linked states/actions/outcomes experience route establishes trajectories.
      - scope: Unresolved qualifying brief/document/evaluator update alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-canonical-turn
        - memory.md#mem-obj-source-evidence
        - runtime.md#rt-rte-operator-eval
        - memory.md#mem-obj-native-ledger
        note: These units lack a fully established qualifying automatic trace-fed write or complete original
          input inventory; known session-fed routes cannot make them inapplicable.
      records:
      - memory.md#mem-obj-interaction-entry
      - memory.md#mem-obj-native-ledger
      - memory.md#mem-rte-native-capture
      - memory.md#mem-rte-interaction-promotion
      - memory.md#mem-rte-review-projection
      - memory.md#mem-obj-benchmark-candidates
      - runtime.md#rt-obj-canonical-turn
      - memory.md#mem-obj-source-evidence
      - runtime.md#rt-rte-operator-eval
      note: Original recorded content establishes sessions and tool traces locally; event delivery labels
        do not add event-streams, and opaque input provenance remains unresolved.
---

# DocMason memory profile

## Comparison rationale

This classification uses only the supplied accepted records and their annotations. Evidence is implementation and doctrine/design, not an observed run or causal experiment. No source files were read, no new records were declared, and report verification was not reopened.

The reconciliation supersedes the epistemic overlay object with [MEM-OBJ-semantic-overlay](memory.md#mem-obj-semantic-overlay). All overlay classifications use that canonical record. Source semantics, interaction containers and their finer memory parts remain distinct overlapping records; they are not wholesale supersessions. The separate [EPI-OBJ-answer](epistemic.md#epi-obj-answer) is linked to [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn), not contained in its symbolic binding.

Files describe the retained substrate, including JSON graph edges and numerical ranking scores. These encodings do not establish graph storage or parametric memory. Source render/media form remains uninspected under [MEM-OBJ-source-evidence](memory.md#mem-obj-source-evidence), so a known file substrate does not make the form axis complete.

Synthesis denotes a new proposition or candidate, not necessarily ampliative knowledge. The concrete staged-inclusion proposition in [EPI-RTE-conservative-output](epistemic.md#epi-rte-conservative-output) differs from copied snippet compression. Requested host authoring remains separately claimed, and its precise curation remains indeterminate. Overlay coverage invalidation and audit-only suppression are bounded withdrawal paths, not a universal forget guarantee.

Automatic interaction summaries and runtime candidates qualify as trace-fed durable artifacts because later consumers exist in [MEM-RTE-interaction-promotion](memory.md#mem-rte-interaction-promotion) and [MEM-RTE-review-projection](memory.md#mem-rte-review-projection). This technical trace-learning classification does not assert improved capacity or automatic production self-revision. Candidate production does not resolve the explicit request's control over regression adoption in [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval).

Requested retrieve/trace is pull even where it ranks retained linguistic text. The optional [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks) route independently pushes linked continuation guidance; bound identity targeting and coarse latest-turn selection remain separate signal findings. Hook events are delivery triggers, not evidence that session-derived content has event-stream origin.

Incomplete provider/attachment parsing, initial document/evaluator provenance, request control, and answer-history reuse remain beside the affected units. Positives are retained without borrowing their wiring to upgrade opaque alternatives. No accepted bounded absence warrants trace-learning no, and no partial pull inventory warrants system-wide push-signal inapplicability.
