---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "AutoSci memory profile: retained wiki, derived context, recovery files, review threads and Hiera feedback at the frozen revision."
run-id: AAS-2026-10-15-autosci-430df584df8f-01
source-identity: https://github.com/skyllwt/AutoSci
reviewed-boundary: f5c2fe009c6683b6aa5b668de759a0610c938aaf
memory-comparison:
  version: 2
  scope: >-
    Included: accumulated raw/source-derived wiki pages and outputs, semantic and
    projected relations, citations, index, gaps, context brief, audit-tail reuse,
    initialization/discovery/research checkpoints and conditional Git fan-in,
    process-local review threads, and Hiera contracts, candidates, attempts,
    ledger, replay, experience reporting and final reports. Includes their
    admission, maintenance and later-consumer alternatives, including partially
    inspected source preparation, regeneration, proposal/tuning and dissemination.
    Excluded: shipped static skills/schema/policy and setup copies as memory,
    host conversation compaction and provider-private retention/weights. Those
    excluded dependencies are not classified from the local implementation.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Local raw/wiki content, derived navigation/graphs, audit log and recovery files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-checkpoints, runtime.md#rt-obj-context-brief, runtime.md#rt-rte-daily-intake]
              note: "Markdown, JSON and JSONL persist locally; graph-shaped content does not establish a graph storage engine."
          records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-checkpoints, runtime.md#rt-obj-context-brief, runtime.md#rt-rte-daily-intake]
          note: "Recorded stores cover this local file inventory; incomplete extraction or regeneration inspection does not obscure the named substrate."
        - scope: "Hiera contract, candidate/attempt payloads, ledger and final report"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-ledger, epistemic.md#epi-rte-hiera-summary]
              note: "Sidecar files retain admitted snapshots, execution receipts and reports."
          records: [runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-ledger, epistemic.md#epi-rte-hiera-summary]
          note: "Full experience dictionaries are not included as durable file payloads merely because a report stores their revision."
        - scope: "Review conversation history and reconstructed Hiera experience/state"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, memory.md#mem-rte-ledger-replay]
              note: "Thread dictionary survives follow-up calls within a process; experience and replay state are reconstructed Python data."
          records: [runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, memory.md#mem-rte-ledger-replay]
          note: "Volatile objects are distinct from their file-backed inputs and report digests; provider-private state is excluded."
        - scope: "Actually committed initialization and daily-intake artifacts"
          assessment: known
          findings:
            - value: repo
              basis: afforded
              records: [runtime.md#rt-rte-parallel-ingest]
              note: "Git can retain and transport included commits; the prescribed staging does not establish inclusion of ignored generated payloads."
            - value: repo
              basis: wired
              records: [runtime.md#rt-rte-daily-intake]
              note: "CI wires a staging/commit/push attempt; tracked changes can persist, but new ignored pages need additional tracking conditions."
          records: [runtime.md#rt-rte-parallel-ingest, runtime.md#rt-rte-daily-intake]
          note: "Classification is conditional repository retention, not a claim that all local file memory is versioned or transported."
      records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-checkpoints, memory.md#mem-obj-ledger, memory.md#mem-obj-experience, runtime.md#rt-obj-context-brief, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, runtime.md#rt-rte-review-call, runtime.md#rt-rte-parallel-ingest, runtime.md#rt-rte-daily-intake, memory.md#mem-rte-ledger-replay]
      note: "Known for the explicitly scoped stores, including volatile and conditional repository parts. This does not classify the excluded host/provider storage or assert observed persistence."
    representational_form:
      assessment: partial
      units:
        - scope: "Wiki prose, gap bullets, brief, index descriptions, edge evidence and conversational review turns"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-edges, runtime.md#rt-obj-context-brief, runtime.md#rt-rte-review-call]
              note: "Text is consumed as evidence, summaries, questions, criticism and review context."
          records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-edges, runtime.md#rt-obj-context-brief, runtime.md#rt-rte-review-call]
          note: "Text remains natural language when placed in a YAML field or JSON message."
        - scope: "Localized identifiers/statuses/links, graph/citation structure, checkpoints and Hiera controls/code/metrics"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-checkpoints, memory.md#mem-obj-ledger, memory.md#mem-obj-experience, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, epistemic.md#epi-obj-evaluation-receipt]
              note: "Fixed code interprets field values, IDs, numerical scores, configuration and executable snapshots; numbers here are not distributed weights."
          records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-checkpoints, memory.md#mem-obj-ledger, memory.md#mem-obj-experience, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, epistemic.md#epi-obj-evaluation-receipt]
          note: "Split from text on the same files by actual consumption path."
        - scope: "Arbitrary raw/evaluator payload contents and incompletely inspected source/dissemination transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-wiki-pages, epistemic.md#epi-obj-evaluation-receipt, runtime.md#rt-rte-hiera-search]
          note: "Available records identify envelopes and file stores, not every payload's operative encoding or consumption. No parametric finding follows from a configurable evaluator or external model."
      records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-edges, memory.md#mem-obj-citations, memory.md#mem-obj-open-questions, memory.md#mem-obj-index, memory.md#mem-obj-checkpoints, memory.md#mem-obj-ledger, memory.md#mem-obj-experience, runtime.md#rt-obj-context-brief, runtime.md#rt-rte-review-call, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, epistemic.md#epi-obj-evaluation-receipt]
      note: "Positive text and symbolic parts are resolved; opaque payload semantics prevent a complete inventory of forms. External decision-model weights are not retained memory within this scope."
    lineage:
      assessment: partial
      units:
        - scope: "Paper/foundation source portions and admitted externally supplied source material"
          assessment: known
          findings:
            - value: imported
              basis: afforded
              records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-obj-wiki-pages]
              note: "Paper and Wikipedia claims enter from sources; marked model commentary is a separate derivation."
          records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-obj-wiki-pages]
          note: "Import does not establish source truth or extraction fidelity."
        - scope: "Agent-composed summaries, concepts, hypotheses, answers, foundations analysis and explicit edits"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [memory.md#mem-obj-wiki-pages, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-memory-maintenance]
              note: "Foreground composition produces interpretations/proposals rather than a byte-preserving source copy."
          records: [memory.md#mem-obj-wiki-pages, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-memory-maintenance]
          note: "Authorship does not decide human admission or whether new claims are entailed."
        - scope: "Deterministic derived context, gap map, projected relations and replay/report summaries"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-summary]
              note: "Code extracts, projects, ranks and aggregates retained inputs."
          records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-summary]
          note: "Compilation lineage is independent of original input provenance; receipt-derived counts also retain trace origin."
        - scope: "Experiment-derived failure memory, ledger feedback and audit-tail targeting"
          assessment: known
          findings:
            - value: trace-extracted
              basis: afforded
              records: [memory.md#mem-rte-negative-memory]
              note: "Pilot/formal execution feedback is interpreted into retained reasons; initial filter eliminations have a different origin."
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, runtime.md#rt-rte-daily-intake]
              note: "Receipt history becomes replay state and durable bouts; recorded audit tails supply later targeting input."
          records: [memory.md#mem-rte-negative-memory, memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, runtime.md#rt-rte-daily-intake]
          note: "Trace derivation can coexist with authored text or compiled symbolic output."
        - scope: "Initial deployment pages/checkpoints, arbitrary candidate payload provenance and uninspected conversion/regeneration branches"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-hiera-search]
          note: "A scaffold and admission interface do not establish the origin of pre-existing deployment content or all transformations."
      records: [memory.md#mem-obj-wiki-pages, memory.md#mem-obj-checkpoints, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-memory-maintenance, memory.md#mem-rte-context-compilation, memory.md#mem-rte-negative-memory, memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, runtime.md#rt-rte-daily-intake, epistemic.md#epi-rte-hiera-summary, runtime.md#rt-rte-hiera-search]
      note: "Derivation paths are supported, but they cannot resolve all initial-content and payload provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Full wiki content and compressed text at later answering/research/review consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [runtime.md#rt-bap-retained-context, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-obj-open-questions, memory.md#mem-rte-foundation-seeding]
              note: "Retained claims, gaps and source summaries supply evidence/context, not an answer oracle."
            - value: instruction
              basis: claimed
              records: [memory.md#mem-rte-negative-memory, runtime.md#rt-bap-retained-context]
              note: "Retained concrete failure reasons are designated a banlist/avoid-repetition guide for later ideation; this is model-interpreted guidance, not an enforced veto."
          records: [runtime.md#rt-bap-retained-context, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-obj-open-questions, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-negative-memory]
          note: "Different forces belong to evidence text and negative guidance even when the same brief carries both."
        - scope: "Retained content/features consumed by context and intake selectors"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-edges, runtime.md#rt-rte-daily-intake]
              note: "Semantic-edge degree orders compiler entries; retained wiki-derived keywords and previews influence later recommendation targeting."
            - value: ranking
              basis: claimed
              records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-obj-index]
              note: "Index descriptions and brief text inform model relevance ordering of full pages."
          records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-edges, runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-obj-index]
          note: "Fixed scoring still gives its retained inputs ranking force; it need not be a learned ranker."
        - scope: "Recovery metadata and Hiera retained execution controls at their code/agent consumers"
          assessment: known
          findings:
            - value: routing
              basis: afforded
              records: [memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, runtime.md#rt-rte-parallel-ingest]
              note: "Stage, selected slugs, manifests and completed/failed lists select resumed work, subject to the recorded payload-transport limits."
            - value: routing
              basis: wired
              records: [memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select]
              note: "Ledger state and candidate IDs determine continuation and next evaluation."
            - value: ranking
              basis: wired
              records: [memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select]
              note: "Retained best scores, bout counts and tried configurations change candidate priority."
            - value: validation
              basis: wired
              records: [runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search]
              note: "Frozen contract and admitted snapshot digests are criteria checked before execution."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, memory.md#mem-rte-ledger-replay]
              note: "Changed digests or exhausted reservation budget reject execution on the inspected path; this is not an OS sandbox."
          records: [memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, runtime.md#rt-rte-parallel-ingest, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search]
          note: "These are accumulated per-run controls, not the excluded shipped writer/schema policy."
        - scope: "Retained experiment feedback at the durable negative-guidance update consumer"
          assessment: known
          findings:
            - value: learning
              basis: afforded
              records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-integrate]
              note: "Recorded experiment results feed durable failure-reason/idea updates for later avoidance guidance; this update force is separate from downstream instruction/knowledge force."
          records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-integrate]
          note: "This does not establish improved capacity, calibrated science or exercised self-improvement."
        - scope: "Review-thread messages at later provider calls and experience revision at report consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, epistemic.md#epi-rte-hiera-summary]
              note: "Thread history supplies follow-up context; reports expose revision/coverage, not the full experience dictionary as scheduler guidance."
          records: [runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, epistemic.md#epi-rte-hiera-summary]
          note: "Display/report consumers are not substituted for the distinct replay/scheduler path."
        - scope: "Uninspected source conversion, regeneration, remaining dissemination and opaque payload consumers"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-wiki-pages, runtime.md#rt-rte-hiera-search, epistemic.md#epi-obj-evaluation-receipt]
          note: "Records do not enumerate every such consumer/effect; known paths cannot establish complete authority coverage."
      records: [runtime.md#rt-bap-retained-context, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-obj-open-questions, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-negative-memory, memory.md#mem-rte-context-compilation, memory.md#mem-obj-edges, runtime.md#rt-rte-daily-intake, memory.md#mem-obj-index, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, runtime.md#rt-rte-parallel-ingest, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select, runtime.md#rt-obj-task-contract, runtime.md#rt-rte-hiera-search, epistemic.md#epi-rte-verdict-integrate, runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, epistemic.md#epi-rte-hiera-summary, memory.md#mem-obj-wiki-pages, epistemic.md#epi-obj-evaluation-receipt]
      note: "Seven forces are supported on named consumers, with local bases preserved; uninspected alternatives prevent a complete inventory."
    write_agency:
      assessment: partial
      units:
        - scope: "Compiler, gap/projection/dedup, automatic lint repair and ledger/reconciliation writes"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, memory.md#mem-obj-citations, epistemic.md#epi-rte-edge-dedup, epistemic.md#epi-rte-wiki-repair, memory.md#mem-rte-ledger-replay]
              note: "Software selects resulting content without a per-entry human decision; requesting rebuild/fix is not approving each result."
          records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, memory.md#mem-obj-citations, epistemic.md#epi-rte-edge-dedup, epistemic.md#epi-rte-wiki-repair, memory.md#mem-rte-ledger-replay]
          note: "Physical file I/O is not the basis: code owns content selection and reconciliation."
        - scope: "Model admission during ingest, seeding, eliminated-idea retention, refinement and auto evaluation"
          assessment: known
          findings:
            - value: automatic
              basis: afforded
              records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-negative-memory, memory.md#mem-rte-memory-maintenance, epistemic.md#epi-rte-verdict-disposition]
              note: "Model chooses content under the invoked procedure; starting the task is not per-content human approval. Auto verdict mode removes the interactive veto."
          records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-negative-memory, memory.md#mem-rte-memory-maintenance, epistemic.md#epi-rte-verdict-disposition]
          note: "Afforded model writes do not become observed admissions or deterministic compliance."
        - scope: "Unattended CI intake admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-daily-intake]
              note: "Schedule/config enables model selection and writeback attempt without per-paper human approval."
          records: [runtime.md#rt-rte-daily-intake]
          note: "Repository retention remains conditional on staging/tracking, independently of agency."
        - scope: "Explicit human crystallization authorization, user-specified edit and interactive verdict approval"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-memory-maintenance, epistemic.md#epi-rte-verdict-disposition]
              note: "These procedures require an explicit user content decision or confirmation; the human control is a prompt contract, not authenticated enforcement."
          records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-memory-maintenance, epistemic.md#epi-rte-verdict-disposition]
          note: "Does not extend manual classification to basic ingest, auto verdict or arbitrary browser callers."
        - scope: "Generic browser/direct CLI writes, checkpoint initialization, reset flags and Hiera approval/admission caller identity"
          assessment: partial
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-hiera-search, memory.md#mem-rte-memory-maintenance]
              note: "Hiera skill specifies human contract/source review and reset specifies plan approval."
          records: [runtime.md#rt-rte-browser-write, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-hiera-search, memory.md#mem-rte-memory-maintenance]
          note: "Executable caller identity and --yes/approve commands do not authenticate a person; initial content control and generic direct-write agency remain unresolved."
      records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, memory.md#mem-obj-edges, memory.md#mem-obj-citations, epistemic.md#epi-rte-edge-dedup, epistemic.md#epi-rte-wiki-repair, memory.md#mem-rte-ledger-replay, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-foundation-seeding, memory.md#mem-rte-negative-memory, memory.md#mem-rte-memory-maintenance, epistemic.md#epi-rte-verdict-disposition, runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-browser-write, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-hiera-search]
      note: "Both agencies occur on separate mechanisms. Initial and generic-caller admissions are not resolved by downstream automatic writes or human-gate doctrine."
    curation_operations:
      assessment: partial
      units:
        - scope: "Context brief and gap-map extraction from retained pages"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions]
              note: "Selected metadata and bullets compress existing claims; sources remain reachable."
          records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions]
          note: "Lossy selection does not become synthesis just because qualifications may be dropped."
        - scope: "Semantic edge/citation cleanup and checkpoint item normalization"
          assessment: known
          findings:
            - value: dedup
              basis: wired
              records: [epistemic.md#epi-rte-edge-dedup, memory.md#mem-obj-citations, memory.md#mem-obj-checkpoints]
              note: "Cleanup retains first canonical relations; checkpoint save deduplicates within lists. These are implemented removals, not merely collision rejection."
          records: [epistemic.md#epi-rte-edge-dedup, memory.md#mem-obj-citations, memory.md#mem-obj-checkpoints]
          note: "First-occurrence survival does not compare scientific merit or merge alternative evidence."
        - scope: "Existing wiki metadata/default/reverse-link repair and direct replacement"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-browser-write, epistemic.md#epi-rte-wiki-repair]
              note: "Existing entries acquire changed fields or repaired links."
          records: [runtime.md#rt-rte-browser-write, epistemic.md#epi-rte-wiki-repair]
          note: "An implemented mutation does not certify the new metadata as true."
        - scope: "Model review/refine, concept merging and verdict-dependent memory revision"
          assessment: partial
          findings:
            - value: evolve
              basis: afforded
              records: [memory.md#mem-rte-memory-maintenance, runtime.md#rt-rte-knowledge-cycle]
              note: "Procedures offer content revision and merge paths, rather than an implemented semantic repair algorithm."
            - value: invalidate
              basis: claimed
              records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-disposition, epistemic.md#epi-rte-verdict-integrate]
              note: "Failed status, concrete reasons and invalidates edges withdraw reliance while keeping the failed idea/evidence."
            - value: promote
              basis: claimed
              records: [epistemic.md#epi-rte-verdict-disposition]
              note: "Supported main single-hypothesis results may raise the idea to validated for subsequent paper planning."
          records: [memory.md#mem-rte-memory-maintenance, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-disposition, epistemic.md#epi-rte-verdict-integrate, memory.md#mem-obj-wiki-pages]
          note: "Concrete semantic inputs/outputs are absent; claims newly synthesized versus faithfully consolidated cannot be fully classified. No synthesize finding follows merely from a command name or fluent output."
        - scope: "Explicit scoped reset/deletion"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-memory-maintenance]
              note: "Deletion forgets selected retained files; it is not historical invalidation or universal erasure."
          records: [memory.md#mem-rte-memory-maintenance]
          note: "Projected edges, root manifests and sidecars can survive; freshness and withdrawal are not globally propagated."
        - scope: "Hiera derived feedback, full index/backfill regeneration and remaining proposal/dissemination transformations"
          assessment: partial
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-summary]
              note: "Replay and reports reduce retained receipts to best scores, counts and summaries; durable bout reconciliation preserves completed-work constraints."
          records: [memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-summary, memory.md#mem-obj-index, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-wiki-pages]
          note: "Reporting counts do not imply durable full experience snapshots. Other named regeneration/proposal/dissemination branches lack complete transformation coverage."
      records: [memory.md#mem-rte-context-compilation, memory.md#mem-obj-open-questions, epistemic.md#epi-rte-edge-dedup, memory.md#mem-obj-citations, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-browser-write, epistemic.md#epi-rte-wiki-repair, memory.md#mem-rte-memory-maintenance, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-disposition, epistemic.md#epi-rte-verdict-integrate, memory.md#mem-obj-wiki-pages, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-summary, memory.md#mem-obj-index, runtime.md#rt-rte-hiera-search]
      note: "Positive operations retain their own evidence layers; indeterminate semantics and incompletely inspected transformations prevent completeness. Projection/index acquisition alone supplies no additional curation value."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested wiki/brief/gap/index/page reads, rebuild returns, recovery and browser reads"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-context-compilation, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, memory.md#mem-rte-foundation-seeding]
              note: "Later agent requests retained files for answering, resumed research or existing-foundation checks; requested compilation return is not unsolicited injection."
          records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-context-compilation, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, memory.md#mem-rte-foundation-seeding]
          note: "File names and top-K relevance selection do not by themselves add a push delivery operation."
        - scope: "Later review replies and Hiera loop/status/tune replay requests"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-review-call, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select]
              note: "Follow-up caller requests the retained thread, and later Hiera invocations load prior events/configurations."
          records: [runtime.md#rt-rte-review-call, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select]
          note: "Requested reloads are separate from downstream automatic selection of the next execution."
        - scope: "Scheduled/manual daily intake preparation supplies retained wiki/audit context to recommendation"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-daily-intake]
              note: "The intake trigger automatically builds a retained-wiki profile and supplies selected evidence to the recommendation consumer, without that consumer requesting the specific retained cards/log tail."
          records: [runtime.md#rt-rte-daily-intake]
          note: "Operator workflow invocation is upstream of automatic selection; compatible model receives further compacted evidence, not the full corpus."
        - scope: "Other host-context, source-preparation and dissemination alternatives within recorded local routes"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-wiki-pages, runtime.md#rt-rte-parallel-ingest, runtime.md#rt-rte-hiera-search]
          note: "Records do not establish every later delivery operation; intended worktree transport is additionally conditional on actual committed payloads. Excluded host compaction is not inferred."
      records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-context-compilation, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-research-verdict, memory.md#mem-rte-foundation-seeding, runtime.md#rt-rte-review-call, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select, runtime.md#rt-rte-daily-intake, memory.md#mem-obj-wiki-pages, runtime.md#rt-rte-parallel-ingest, runtime.md#rt-rte-hiera-search]
      note: "Both requested access and automatic recommendation-context supply are supported, but not a complete delivery inventory."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Daily intake wiki-profile push to recommendation"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-daily-intake]
              note: "Trigger is scheduled/manual intake; selector uses entity category, mtime, per-category counts and preview/log-tail caps to select newest cards and the last 20 audit lines for prepared recommendation context."
          records: [runtime.md#rt-rte-daily-intake]
          note: "Keyword/gap extraction further transforms selected text. Selection of new external papers by lexical scores is not itself read-back of retained memory."
        - scope: "Requested wiki/recovery/thread/ledger reads and compilation returns"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-context-compilation, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-review-call, memory.md#mem-rte-ledger-replay]
          note: "These units fulfill explicit retained-material requests; filenames, thread IDs and checkpoint keys are not evidence of targeted push."
        - scope: "Additional automatic selection/delivery inside Hiera and uninspected local consumer alternatives"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-hiera-select, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-wiki-pages]
          note: "Score-directed choice of an execution is established, but records do not separately establish every retained-payload delivery/identity-match operation or other automatic injection route. Cannot use known pull paths to declare this unit inapplicable."
      records: [runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-knowledge-cycle, memory.md#mem-rte-context-compilation, memory.md#mem-obj-checkpoints, runtime.md#rt-rte-review-call, memory.md#mem-rte-ledger-replay, epistemic.md#epi-rte-hiera-select, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-wiki-pages]
      note: "Coarse profile selection is supported; no inferred embedding, lexical relevance, judgment or identifier push is inferred from mere file addressing or action selection. Other push alternatives remain unresolved."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic pilot/formal outcome-to-negative-memory update and later ideation"
          assessment: known
          findings:
            - value: "yes"
              basis: afforded
              records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-integrate]
              note: "Auto evaluation can turn metrics/logs and result judgments into durable failure reasons/pages, later consumed as avoidance guidance. Human-confirmed branches are separate manual admissions."
          records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-integrate]
          note: "Filter rejection without execution feedback is not silently equated to experiment trace learning. Actual use or improvement is unobserved."
        - scope: "Failure-summary compilation into a retained brief for later agents"
          assessment: known
          findings:
            - value: "yes"
              basis: afforded
              records: [memory.md#mem-rte-context-compilation, memory.md#mem-rte-negative-memory, runtime.md#rt-bap-retained-context]
              note: "Trace-derived failure fields feed automatic durable summary production, with a later agent read afforded by skills. Wired compilation alone does not upgrade that later consumption to observation."
          records: [memory.md#mem-rte-context-compilation, memory.md#mem-rte-negative-memory, runtime.md#rt-bap-retained-context]
          note: "Non-ampliative summarization still qualifies; detailed reasons may be omitted under budgets."
        - scope: "Hiera feedback and attempt-bound durable reconciliation consumed by later loop/tune"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, epistemic.md#epi-rte-hiera-select]
              note: "Automatic receipts and durable bout reconciliation retain experience-dependent constraints; later replay uses scores/completed bouts/tried configs to change priority and prevent duplicate work. No learned parameters are required."
          records: [memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, epistemic.md#epi-rte-hiera-select]
          note: "This names the operative ledger-to-decision route, not mere retention of stdout or the separately reported experience revision."
        - scope: "Audit-tail recommendation preparation, process-local review history, report-only experience digest and remaining opaque write alternatives"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-checkpoints]
          note: "Context use/count reporting is known, but these records do not establish for every branch an automatic trace-fed durable behavior-shaping output and later consumer. No bounded absence record warrants a local no."
      records: [memory.md#mem-rte-negative-memory, epistemic.md#epi-rte-verdict-integrate, memory.md#mem-rte-context-compilation, runtime.md#rt-bap-retained-context, memory.md#mem-rte-ledger-replay, memory.md#mem-obj-ledger, epistemic.md#epi-rte-hiera-select, runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, runtime.md#rt-rte-hiera-search, memory.md#mem-obj-checkpoints]
      note: "Supported yes findings coexist with unresolved branches. This axis is automatic trace-fed artifact updating, not demonstrated improved capacity, scientific validity or self-improvement."
    trace_source:
      assessment: partial
      units:
        - scope: "Pilot/formal failure updates and their downstream brief summaries"
          assessment: partial
          findings:
            - value: tool-traces
              basis: afforded
              records: [memory.md#mem-rte-negative-memory, memory.md#mem-rte-context-compilation, epistemic.md#epi-rte-verdict-check]
              note: "Execution metrics, logs and experiment results feed failure judgments and then summary fields. The original feedback origin is retained through the derived-page carrier."
          records: [memory.md#mem-rte-negative-memory, memory.md#mem-rte-context-compilation, epistemic.md#epi-rte-verdict-check]
          note: "Hypotheses, model judgments and sibling summaries are mixed inputs; complete trace provenance is not supplied. Imported paper/static instruction content is not an additional trace-source value."
        - scope: "Hiera durable receipt and tuning-bout feedback"
          assessment: known
          findings:
            - value: tool-traces
              basis: wired
              records: [runtime.md#rt-rte-hiera-search, memory.md#mem-rte-ledger-replay, epistemic.md#epi-obj-evaluation-receipt]
              note: "Local/remote command execution receipts, status and scores are the execution-feedback source for retained replay/bout constraints."
            - value: event-streams
              basis: wired
              records: [memory.md#mem-obj-ledger, memory.md#mem-rte-ledger-replay]
              note: "Recorded runtime reservations, releases and tuning-bout/decision events supply completed-work and budget history for later reconciliation and scheduling. This value names actual runtime events, not JSONL serialization alone."
          records: [runtime.md#rt-rte-hiera-search, memory.md#mem-rte-ledger-replay, epistemic.md#epi-obj-evaluation-receipt, memory.md#mem-obj-ledger]
          note: "The known unit is execution/control feedback, not arbitrary evaluator result-payload semantics or a claim that linked IDs alone constitute multi-step trajectories."
        - scope: "Other unresolved qualifying-write alternatives and mixed evaluator payload provenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-review-call, memory.md#mem-obj-experience, runtime.md#rt-rte-hiera-search, epistemic.md#epi-obj-evaluation-receipt]
          note: "Without the missing durable-update/later-consumer facts, cannot classify source for these alternatives or declare it inapplicable. Conversational history alone does not establish session-log learning."
      records: [memory.md#mem-rte-negative-memory, memory.md#mem-rte-context-compilation, epistemic.md#epi-rte-verdict-check, runtime.md#rt-rte-hiera-search, memory.md#mem-rte-ledger-replay, epistemic.md#epi-obj-evaluation-receipt, memory.md#mem-obj-ledger, runtime.md#rt-rte-daily-intake, runtime.md#rt-rte-review-call, memory.md#mem-obj-experience]
      note: "Tool feedback and runtime event history have positive local warrants. Mixed inputs and unresolved automatic writes prevent complete source coverage; no session-logs or trajectories finding is inferred from storage labels."
---

# AutoSci memory profile

## Comparison rationale

This profile classifies accepted records, not new source evidence. No source files were read. No records are declared. Reconciliation supplies no supersessions: broad page/route containers and their narrower epistemic and memory parts remain distinct canonical records.

The retained boundary is not the enclosing model's storage. [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages), [MEM-OBJ-ledger](memory.md#mem-obj-ledger) and [RT-RTE-review-call](runtime.md#rt-rte-review-call) establish file-backed knowledge, feedback history and volatile review turns respectively. External model parameters and host compaction are excluded from this memory account, not classified as absent. Likewise, installed language-selected skills are static configuration rather than accumulated experience. Graph JSONL remains a file substrate; symbolic graph access and natural-language evidence are separate operative parts of [MEM-OBJ-edges](memory.md#mem-obj-edges).

Repository retention is conditional. [RT-RTE-parallel-ingest](runtime.md#rt-rte-parallel-ingest) and [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake) retain the ignored-payload/unforced-staging limitation. Their Git routes do not prove that prepared sources reach workers, generated output returns, or every local file survives CI. The memory annotation's broader task-isolation wording is not used to strengthen transport. This preserves the reconciliation's unresolved disagreement without reopening verification.

The other recorded disagreement concerns general versus purpose-specific context packs. [MEM-RTE-context-compilation](memory.md#mem-rte-context-compilation) supports consolidation and selection with explicit section budgets. The profile does not infer that a general pack contains experiments or stale entities. Both positive mechanisms and omission limits survive the runtime's less specific description of [RT-OBJ-context-brief](runtime.md#rt-obj-context-brief).

Authority is attached to actual consumers. Knowledge at answering agents, instruction-like failed-idea avoidance, ranking inputs, recovery routing and executable contract/budget checks are different effects. The experiment-results-to-failure-guidance update has learning authority at its update consumer; the resulting reason supplies knowledge or instruction downstream. These findings rely on [MEM-RTE-negative-memory](memory.md#mem-rte-negative-memory), [EPI-RTE-verdict-integrate](epistemic.md#epi-rte-verdict-integrate) and [RT-BAP-retained-context](runtime.md#rt-bap-retained-context), not on a blanket implication from persistence to learning. Prompt gates remain claimed; browser/direct CLI callers do not authenticate human review.

Read-back distinguishes requested retrieval from automatic context supply. [RT-RTE-knowledge-cycle](runtime.md#rt-rte-knowledge-cycle) requests files and relevant full pages. A requested rebuild's selector does not make its return push. In contrast, the annotation on [RT-RTE-daily-intake](runtime.md#rt-rte-daily-intake) establishes automatic newest-card/log-tail preparation for recommendation. Its coarse selection is distinct from lexical scoring of new external papers. The profile does not manufacture targeted identifier push from requested filenames, or infer a complete push inventory from one inspected route.

Trace-learning positives name durable outputs and later consumers. Automatic experimental failure-memory updates and their retained brief projection are afforded routes; ledger feedback and durable bout reconciliation feeding later execution are wired in [MEM-RTE-ledger-replay](memory.md#mem-rte-ledger-replay). Raw logging alone is insufficient. [MEM-OBJ-experience](memory.md#mem-obj-experience) and [EPI-RTE-hiera-summary](epistemic.md#epi-rte-hiera-summary) expose a reporting revision, not a durable full experience dictionary driving the scheduler. [EPI-RTE-hiera-select](epistemic.md#epi-rte-hiera-select) identifies the actual score/bout/tried-config consumers. These distinctions permit architectural trace-learning findings without asserting improved capacity, scientific confirmation, observed activation or causal benefit.

Partial axes retain unresolved initial provenance/admission, arbitrary payload semantics, mixed trace origins and incompletely inspected regeneration, proposal and dissemination routes. No bounded absence records were declared, so this profile does not turn missing recorded facts into absent operations or a system-wide trace-learning negative. Local known units do not erase those alternatives.
