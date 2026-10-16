---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Stash memory comparison: PostgreSQL observations, derived knowledge, typed state and operational access structures at the frozen revision."
run-id: "AAS-2026-10-15-stash-7ac5612837a0-01"
source-identity: "https://github.com/alash3al/stash"
reviewed-boundary: "d34ed430c4348ef741ef95146b488aea8616f4fb"
memory-comparison:
  version: 2
  scope: "Use-accumulated PostgreSQL episodes, facts, dense embeddings, entity relationships, causal links, abstraction patterns, contradictions, hypotheses, goals, failures, namespace focus and descriptions, maintenance cursors, embedding cache and the recorded dimension/model settings; caller admissions, all maintenance transformations and later client/model/operational reads. Includes unresolved provenance, human control and storage-only consumer alternatives. Excludes compiled server/model prompts and release products, current request-local state, external client histories/decisions, Stash Cloud and provider model weights not updated through these routes. Further settings consumers remain unresolved rather than silently excluded."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Episode/fact text and metadata; relationships, causal links, patterns, contradictions, hypotheses, goals, failures, focus, namespaces, cursors, settings and embedding cache"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-relationship"
                - "memory.md#mem-obj-causal-link"
                - "memory.md#mem-obj-pattern"
                - "memory.md#mem-obj-contradiction"
                - "memory.md#mem-obj-hypothesis"
                - "memory.md#mem-obj-goal"
                - "memory.md#mem-obj-failure"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-obj-embedding-cache"
                - "memory.md#mem-obj-settings"
                - "memory.md#mem-obj-memory-vectors"
              note: "PostgreSQL persists these objects across invocations."
          records:
            - "memory.md#mem-obj-episode"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-relationship"
            - "memory.md#mem-obj-causal-link"
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-obj-contradiction"
            - "memory.md#mem-obj-hypothesis"
            - "memory.md#mem-obj-goal"
            - "memory.md#mem-obj-failure"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-settings"
            - "memory.md#mem-obj-memory-vectors"
          note: "The accepted object inventory identifies PostgreSQL for each retained part; graph-shaped edges are relational rows, not evidence of a graph storage engine."
        -
          scope: "Episode/fact embeddings and cached embedding vectors"
          assessment: "known"
          findings:
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vectors"
                - "memory.md#mem-obj-embedding-cache"
              note: "pgvector columns retain embeddings used for later similarity and memoization."
          records:
            - "memory.md#mem-obj-memory-vectors"
            - "memory.md#mem-obj-embedding-cache"
          note: "Dense numerical parts have an explicit vector store within the relational database."
      records:
        - "memory.md#mem-obj-episode"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-relationship"
        - "memory.md#mem-obj-causal-link"
        - "memory.md#mem-obj-pattern"
        - "memory.md#mem-obj-contradiction"
        - "memory.md#mem-obj-hypothesis"
        - "memory.md#mem-obj-goal"
        - "memory.md#mem-obj-failure"
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-settings"
        - "memory.md#mem-obj-memory-vectors"
      note: "All inventoried use-accumulated objects reside in PostgreSQL; vector columns and cache are included explicitly. Provider weights and shipped static products are outside this memory inventory."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Text of episodes, fact summaries, patterns, contradiction resolutions, hypotheses/plans/reasons, goals/notes, failures/lessons, focus and namespace descriptions"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-pattern"
                - "memory.md#mem-obj-contradiction"
                - "memory.md#mem-obj-hypothesis"
                - "memory.md#mem-obj-goal"
                - "memory.md#mem-obj-failure"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-namespace"
              note: "Text is supplied to maintenance models or requested client readers; pattern text has only a library read affordance."
          records:
            - "memory.md#mem-obj-episode"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-obj-contradiction"
            - "memory.md#mem-obj-hypothesis"
            - "memory.md#mem-obj-goal"
            - "memory.md#mem-obj-failure"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-namespace"
          note: "These retained fields receive meaning through human or model interpretation."
        -
          scope: "IDs, namespaces, statuses, priority/confidence/validity fields, fact matching fields, edge structures, source arrays, cursors, settings and cache keys"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-episode"
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-relationship"
                - "memory.md#mem-obj-causal-link"
                - "memory.md#mem-obj-pattern"
                - "memory.md#mem-obj-contradiction"
                - "memory.md#mem-obj-hypothesis"
                - "memory.md#mem-obj-goal"
                - "memory.md#mem-obj-failure"
                - "memory.md#mem-obj-context"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-obj-settings"
                - "memory.md#mem-obj-embedding-cache"
              note: "Database selectors, state transitions, exact matches, traversal and cache lookups consume these fields."
          records:
            - "memory.md#mem-obj-episode"
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-relationship"
            - "memory.md#mem-obj-causal-link"
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-obj-contradiction"
            - "memory.md#mem-obj-hypothesis"
            - "memory.md#mem-obj-goal"
            - "memory.md#mem-obj-failure"
            - "memory.md#mem-obj-context"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-settings"
            - "memory.md#mem-obj-embedding-cache"
          note: "Fixed consumer rules use localized fields; a semantic edge can also be interpreted as language at a model consumer."
        -
          scope: "Relationship words and structured fact values as interpreted by the pattern reasoner or client"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "memory.md#mem-obj-relationship"
                - "memory.md#mem-bap-maintenance-input"
              note: "Maintenance formats fact/relationship fields as model-readable evidence."
          records:
            - "memory.md#mem-obj-fact"
            - "memory.md#mem-obj-relationship"
            - "memory.md#mem-bap-maintenance-input"
          note: "The same fields have a separate interpreted consumption path, not just fixed matching."
        -
          scope: "Episode/fact vectors and embedding-cache vector payload"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vectors"
                - "memory.md#mem-obj-embedding-cache"
              note: "Numerical state distributes representation across vector dimensions."
          records:
            - "memory.md#mem-obj-memory-vectors"
            - "memory.md#mem-obj-embedding-cache"
          note: "Dense representations are distinct from readable text and model weights."
      records:
        - "memory.md#mem-obj-episode"
        - "memory.md#mem-obj-fact"
        - "memory.md#mem-obj-pattern"
        - "memory.md#mem-obj-contradiction"
        - "memory.md#mem-obj-hypothesis"
        - "memory.md#mem-obj-goal"
        - "memory.md#mem-obj-failure"
        - "memory.md#mem-obj-context"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-obj-relationship"
        - "memory.md#mem-obj-causal-link"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-settings"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-bap-maintenance-input"
        - "memory.md#mem-obj-memory-vectors"
      note: "The inventory separates interpreted text, fixed-rule fields/edges and dense vectors. Provider model parameters are not these stored numerical outputs."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-supplied episode, focus, goal, hypothesis, failure, namespace descriptive content and asserted causal links at Stash admission"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-remember-write"
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-edge-extraction"
                - "memory.md#mem-rte-fact-withdrawal"
              note: "Registered callers supply substantive content; Stash does not originate those initial assertions."
          records:
            - "runtime.md#rt-rte-remember-write"
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "At the Stash boundary these are imports; human versus model origin upstream remains unresolved."
        -
          scope: "Failure reports and recent episode reports transformed into repeat-failure episodes and failure-pattern facts"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-obj-failure"
              note: "Automatic review of reported failures/activity writes derived durable episodes and facts."
          records:
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-obj-failure"
          note: "Derivation extracts experience reports; it does not authenticate their claimed events."
        -
          scope: "General episode-to-fact summaries, and downstream facts/relationships/patterns/goal notes/hypothesis assessments"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-edge-extraction"
                - "memory.md#mem-rte-pattern-extraction"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-fact-withdrawal"
              note: "Model transformations compile retained content and metadata into additional retained artifacts."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "Software/model derivation is known. Inputs can contain session experience or arbitrary assertions, so the full trace-extracted versus other compilation split is unresolved."
        -
          scope: "Embedding outputs/cache, automatic namespace scaffold/ancestors, maintenance cursors, settings and deterministic state updates"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vectors"
                - "memory.md#mem-obj-embedding-cache"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-obj-settings"
                - "memory.md#mem-rte-fact-withdrawal"
              note: "Vectors and operational metadata are generated or updated through fixed code/provider calls."
          records:
            - "memory.md#mem-obj-memory-vectors"
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-settings"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "These known software/provider-output paths do not establish initial content authorship."
      records:
        - "runtime.md#rt-rte-remember-write"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-obj-failure"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-obj-memory-vectors"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-settings"
      note: "Known derivation paths do not authenticate original caller reports or resolve every episode-to-fact input origin. No authored/manual inference follows from caller identity."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Recalled episodes/facts, typed retained knowledge, focus and descriptive namespace text at requesting external client"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-read"
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-rte-typed-read"
              note: "Tool text supplies retained content as context/reference."
          records:
            - "runtime.md#rt-rte-recall-read"
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-rte-typed-read"
            - "memory.md#mem-bap-retained-advice"
          note: "Knowledge/advice is delivered, without enforcing the external agent's answer."
        -
          scope: "Retained preferences or standing self-advice at external agent following the session protocol"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-bap-retained-advice"
              note: "A client can recall retained standing directions and use them as guidance."
          records:
            - "memory.md#mem-bap-retained-advice"
          note: "The documented standing-guidance role is afforded; stored instances, activation and host instruction precedence are uninspected."
        -
          scope: "Episode/fact/relationship, hypothesis/goal and failure content at maintenance model evidence consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-maintenance-input"
              note: "Constructed maintenance messages supply retained texts as evidence."
          records:
            - "memory.md#mem-bap-maintenance-input"
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "Retained content is evidence for bounded model judgements, not a truth certificate."
        -
          scope: "Reported episode/failure experience at automatic durable-derivation consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-failure-derivation"
              note: "Experience reports feed summaries/repeat evidence/pattern facts consumed later."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-failure-derivation"
          note: "Learning authority here means experience feeding durable artifact updates, not demonstrated improved capacity."
        -
          scope: "Stored embeddings at recall ranking and clustering/deduplication; goal priority at list ordering"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vectors"
                - "runtime.md#rt-rte-recall-read"
                - "memory.md#mem-rte-goal-maintenance"
              note: "Vector similarity ranks memory; retained goal priority orders goal lists."
          records:
            - "memory.md#mem-obj-memory-vectors"
            - "runtime.md#rt-rte-recall-read"
            - "memory.md#mem-rte-goal-maintenance"
          note: "The retained numerical state and priority influence relative ordering/grouping under fixed rules."
        -
          scope: "Namespace IDs/slugs and checkpoint watermarks at storage/maintenance selectors; retained hypothesis/goal state at next scan"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-goal-maintenance"
              note: "Retained state selects later batches, namespaces and open/active candidates."
          records:
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-goal-maintenance"
          note: "These fields choose input scope/window and eligible operation, not caller authorization."
        -
          scope: "Deleted/resolved/terminal state at read/scan selectors and dimension-lock setting at bootstrap"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-withdrawal"
                - "memory.md#mem-rte-typed-read"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-obj-settings"
              note: "Stored state excludes rows/transitions or refuses incompatible dimensions."
          records:
            - "memory.md#mem-rte-fact-withdrawal"
            - "memory.md#mem-rte-typed-read"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-obj-settings"
          note: "Only consumers consulting a field enforce it; valid_until is not enforced by ordinary recall."
        -
          scope: "Retained hypothesis/goal status at transition admission and dimension lock at vector setup"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-hypothesis-control"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-obj-settings"
              note: "Transition/status and dimension checks compare candidates with retained criteria."
          records:
            - "epistemic.md#epi-rte-hypothesis-control"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-obj-settings"
          note: "Retained criteria constrain admissible transitions/dimensions, separately from generated model judgement."
        -
          scope: "Pattern rows beyond QueryPatterns capability and unspecified additional settings consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-obj-settings"
          note: "No concrete shipped pattern consumer was found; settings were not exhaustively audited. These gaps prevent a complete authority inventory."
      records:
        - "runtime.md#rt-rte-recall-read"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-rte-typed-read"
        - "memory.md#mem-bap-retained-advice"
        - "memory.md#mem-bap-maintenance-input"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-obj-memory-vectors"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-settings"
        - "epistemic.md#epi-rte-hypothesis-control"
        - "memory.md#mem-obj-pattern"
      note: "Positive forces are consumer-specific. Pattern downstream use and further settings consumers remain unresolved; delivery does not establish client obedience or benefit."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Maintenance model proposals admitted by code, confidence/validity updates, cursor saves, embedding memoization and namespace scaffold ancestors"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-edge-extraction"
                - "memory.md#mem-rte-pattern-extraction"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-fact-withdrawal"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-obj-embedding-cache"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-settings"
              note: "Software/model rules admit these writes without an explicit human decision on each retained result."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-fact-withdrawal"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-settings"
          note: "Starting consolidation is not per-content human approval."
        -
          scope: "Caller remember/focus, namespace descriptive writes, goals, failures, hypotheses, causal assertions, explicit edits/status changes and withdrawal"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-remember-write"
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "The API accepts the caller decision but does not identify human approval. Physical SQL writes and possible agent authorship do not resolve admission control."
      records:
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-obj-settings"
        - "runtime.md#rt-rte-remember-write"
        - "runtime.md#rt-rte-context-handoff"
      note: "Automatic admissions are established locally. Generic caller identity cannot resolve manual versus automatic initial content/edit/withdrawal decisions."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Episode clusters reduced to fact summaries"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "epistemic.md#epi-rte-fact-synthesis"
              note: "Maintenance compresses selected retained episode claims into summaries."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "epistemic.md#epi-rte-fact-synthesis"
          note: "This is consolidation even though raw episodes remain. Semantic faithfulness is not guaranteed by anti-copy checks."
        -
          scope: "Near-duplicate fact suppression and repeated source-edge suppression"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-edge-extraction"
              note: "Existing retained facts are used to suppress near-duplicate admissions; repeated extracted edges are skipped."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
          note: "Similarity dedup is distinct from a primary-key collision check; model/SQL failures qualify reliability."
        -
          scope: "Focus replacement, goal edits/notes and hypothesis confidence/status changes"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-handoff"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-hypothesis-maintenance"
              note: "Updates replace focus or revise retained notes/state."
          records:
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-hypothesis-maintenance"
          note: "These modify existing retained entries; caller control remains a separate uncertainty."
        -
          scope: "Caller hypothesis content/plan refinement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "epistemic.md#epi-rte-hypothesis-control"
              note: "The exposed operation intends content/plan replacement and state reset."
          records:
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "epistemic.md#epi-rte-hypothesis-control"
          note: "A timestamp method-value defect prevents claiming runnable successful refinement."
        -
          scope: "Testing hypothesis promoted to fact by caller or automatic evidence scan"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "epistemic.md#epi-rte-hypothesis-assessment"
                - "epistemic.md#epi-rte-hypothesis-control"
              note: "Confirmation inserts a fact and links the confirmed hypothesis."
          records:
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "epistemic.md#epi-rte-hypothesis-assessment"
            - "epistemic.md#epi-rte-hypothesis-control"
          note: "Promotion changes storage role and later eligibility; direct confirmation is not evidence-consuming acceptance."
        -
          scope: "Age-based confidence downweighting"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-withdrawal"
                - "epistemic.md#epi-rte-memory-withdrawal"
              note: "Fixed age/confidence rules reduce retained fact confidence."
          records:
            - "memory.md#mem-rte-fact-withdrawal"
            - "epistemic.md#epi-rte-memory-withdrawal"
          note: "Downweighting is implemented even though expiry does not remove facts from recall."
        -
          scope: "Episode soft deletion and rejection/closure excluding candidates from automatic open/active selection"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-fact-withdrawal"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-goal-maintenance"
              note: "Selectors withdraw current use of soft-deleted episodes or rejected/inactive candidates."
          records:
            - "memory.md#mem-rte-fact-withdrawal"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-goal-maintenance"
          note: "History remains in soft-deleted/terminal rows; no general derivative erasure or fact validity exclusion is inferred."
        -
          scope: "Possible new claims in abstraction, edge, goal/hypothesis judgement and failure-pattern outputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-failure-derivation"
            - "epistemic.md#epi-rte-relationship-extraction"
            - "epistemic.md#epi-rte-causal-links"
            - "epistemic.md#epi-rte-goal-assessment"
            - "epistemic.md#epi-rte-hypothesis-assessment"
          note: "No output/source comparison establishes a claim absent from its inputs. Synthesis labels and broader-theme requests cannot establish synthesize."
      records:
        - "runtime.md#rt-rte-consolidation-run"
        - "epistemic.md#epi-rte-fact-synthesis"
        - "memory.md#mem-rte-edge-extraction"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "epistemic.md#epi-rte-hypothesis-control"
        - "epistemic.md#epi-rte-hypothesis-assessment"
        - "memory.md#mem-rte-fact-withdrawal"
        - "epistemic.md#epi-rte-memory-withdrawal"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-rte-failure-derivation"
        - "epistemic.md#epi-rte-relationship-extraction"
        - "epistemic.md#epi-rte-causal-links"
        - "epistemic.md#epi-rte-goal-assessment"
      note: "Recorded transformations establish several operations, but semantic novelty of model outputs is unresolved and hypothesis refinement is only afforded. Fact validity retirement is not general reliance withdrawal."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Recall, typed tools and exact-namespace focus reload"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-read"
                - "memory.md#mem-rte-typed-read"
                - "runtime.md#rt-rte-context-handoff"
              note: "Request parameters select later delivery to the requesting client."
          records:
            - "runtime.md#rt-rte-recall-read"
            - "memory.md#mem-rte-typed-read"
            - "runtime.md#rt-rte-context-handoff"
          note: "A consumer requests the returned material; serialization is not another push."
        -
          scope: "Embedding cache lookup and operational namespace/checkpoint/settings reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-embedding-cache"
                - "memory.md#mem-obj-namespace"
                - "memory.md#mem-obj-consolidation-progress"
                - "memory.md#mem-obj-settings"
              note: "Embed/bootstrap/maintenance request retained numerical or control state."
          records:
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-settings"
          note: "These are requested operational reloads, not client knowledge delivery."
        -
          scope: "Automatic retained batch selection and message assembly for maintenance reasoner"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-edge-extraction"
                - "memory.md#mem-rte-pattern-extraction"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-fact-withdrawal"
                - "memory.md#mem-bap-maintenance-input"
              note: "Go selectors supply retained evidence to a fresh model invocation without the reasoner asking for those rows."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-fact-withdrawal"
            - "memory.md#mem-bap-maintenance-input"
          note: "Manual or timer initiation does not make each model input batch a consumer request for that retained material."
        -
          scope: "Pattern QueryPatterns route"
          assessment: "partial"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-pattern-extraction"
              note: "QueryPatterns can return retained pattern rows to a requesting caller."
          records:
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-rte-pattern-extraction"
          note: "Requested API read is afforded, but no shipped later consumer is found, preventing a complete wired read-back account."
        -
          scope: "Bare GetFact/GetEpisode alternatives without a found shipped consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-typed-read"
          note: "Storage getters alone do not establish a concrete later-consumer route."
      records:
        - "runtime.md#rt-rte-recall-read"
        - "memory.md#mem-rte-typed-read"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-settings"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-bap-maintenance-input"
        - "memory.md#mem-obj-pattern"
      note: "Requested external reload coexists with automatic maintenance supply. Pattern and bare getter alternatives are capabilities with unresolved actual later consumers; they remain in scope."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Maintenance trigger -> namespace/watermark/status/availability/row-limit selection -> model evidence batches"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-consolidation-progress"
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-rte-edge-extraction"
                - "memory.md#mem-rte-pattern-extraction"
                - "memory.md#mem-rte-goal-maintenance"
                - "memory.md#mem-rte-failure-derivation"
                - "memory.md#mem-rte-hypothesis-maintenance"
                - "memory.md#mem-rte-fact-withdrawal"
              note: "Checkpoint ranges, active/open status, namespace scope and fixed row budgets supply broad batches."
          records:
            - "memory.md#mem-obj-consolidation-progress"
            - "memory.md#mem-obj-namespace"
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-pattern-extraction"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-fact-withdrawal"
          note: "Every maintenance invocation uses bounded availability/window filters; row limits are not token budgets."
        -
          scope: "Episode-to-fact trigger -> stored episode vector similarity -> clustered episode texts delivered to reasoner"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-vectors"
                - "runtime.md#rt-rte-consolidation-run"
              note: "Dense similarity groups selected episode parts into reasoner evidence clusters."
          records:
            - "memory.md#mem-obj-memory-vectors"
            - "runtime.md#rt-rte-consolidation-run"
          note: "The cluster selector operates before model input; this is distinct from requested semantic recall."
        -
          scope: "Inline contradiction trigger -> retained entity/property identity match with differing values -> old/new values delivered to comparator model"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fact"
                - "epistemic.md#epi-rte-contradiction-review"
              note: "Exact entity/property identity selects comparison partners for automatic delivery."
          records:
            - "memory.md#mem-obj-fact"
            - "epistemic.md#epi-rte-contradiction-review"
          note: "The actual equality match chooses retained old fact values, not merely a catalog or requested ID."
        -
          scope: "External requested recall/typed/context routes and operational cache/control lookups"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-recall-read"
            - "memory.md#mem-rte-typed-read"
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-settings"
          note: "These local routes fulfill a consumer request; their filters do not classify push signals."
        -
          scope: "Unestablished consumers of patterns and bare getters"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-pattern"
            - "memory.md#mem-rte-typed-read"
          note: "A hypothetical actual consumer could select/deliver differently. The records do not establish that chain."
      records:
        - "memory.md#mem-obj-consolidation-progress"
        - "memory.md#mem-obj-namespace"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-obj-memory-vectors"
        - "memory.md#mem-obj-fact"
        - "epistemic.md#epi-rte-contradiction-review"
        - "runtime.md#rt-rte-recall-read"
        - "memory.md#mem-rte-typed-read"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-settings"
        - "memory.md#mem-obj-pattern"
      note: "Push findings apply to maintenance selectors, not query embeddings on requested recall. Unknown actual use of storage-only alternatives prevents completely assessing every direction."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Failure/activity reports plus recent episodes -> automatic repeat evidence and failure-pattern facts -> later consolidation/recall"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-failure-derivation"
              note: "Automatic report-fed writes produce durable behavior-shaping knowledge consumed by later memory operations."
          records:
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-obj-failure"
            - "memory.md#mem-obj-episode"
          note: "Reports of experience are trace inputs; no authentication or measured benefit is implied."
        -
          scope: "Session activity summarized into episodes -> automatic fact consolidation -> later recall/maintenance"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-consolidation-run"
                - "memory.md#mem-obj-episode"
              note: "When retained episodes report session activity, automatic summaries persist for later context and maintenance."
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-obj-episode"
            - "memory.md#mem-bap-retained-advice"
          note: "The write/retention/later-consumer chain is wired for experience-bearing episodes. Arbitrary caller assertions are also admitted, so not every consolidation input is known to be a trace."
        -
          scope: "Caller initial writes/focus replacement and downstream knowledge-only updates with unresolved original episode/fact provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-remember-write"
            - "runtime.md#rt-rte-context-handoff"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-rte-goal-maintenance"
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-rte-hypothesis-maintenance"
            - "memory.md#mem-rte-edge-extraction"
            - "memory.md#mem-rte-fact-withdrawal"
            - "memory.md#mem-rte-pattern-extraction"
          note: "Caller control and original input content are unresolved. Neither raw storage nor an unknown upstream derivation warrants a blanket no or yes."
        -
          scope: "Cache, namespaces, settings and cursor bookkeeping as operational metadata rather than trace-derived behavior-shaping artifacts"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-embedding-cache"
            - "memory.md#mem-obj-namespace"
            - "memory.md#mem-obj-settings"
            - "memory.md#mem-obj-consolidation-progress"
          note: "These recorded mechanisms memoize values or route work; they are not the qualifying trace-to-durable-content update."
      records:
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-obj-failure"
        - "memory.md#mem-obj-episode"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-bap-retained-advice"
        - "runtime.md#rt-rte-remember-write"
        - "runtime.md#rt-rte-context-handoff"
        - "memory.md#mem-obj-namespace"
        - "memory.md#mem-rte-goal-maintenance"
        - "memory.md#mem-rte-hypothesis-maintenance"
        - "memory.md#mem-rte-edge-extraction"
        - "memory.md#mem-rte-fact-withdrawal"
        - "memory.md#mem-rte-pattern-extraction"
        - "memory.md#mem-obj-embedding-cache"
        - "memory.md#mem-obj-settings"
        - "memory.md#mem-obj-consolidation-progress"
      note: "Experience-fed durable derivation is supported without weight training or demonstrated improvement. Generic episode provenance and caller-controlled admissions prevent exhaustive route coverage."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Original inputs to failure-review repeat/pattern writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-failure-derivation"
            - "memory.md#mem-obj-failure"
            - "memory.md#mem-obj-episode"
          note: "Caller failure explanations and recent episode texts may summarize activity, but their original trace format/content is unresolved; no controlled source class is established."
        -
          scope: "Original inputs to general episode-to-fact trace-fed consolidation and downstream derived routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-consolidation-run"
            - "memory.md#mem-obj-episode"
            - "memory.md#mem-obj-fact"
          note: "Session summaries are not shown to be recorded turns; event metadata/serialization does not establish event-stream origin. Unknown inputs cannot be dropped to classify trace_source as inapplicable."
      records:
        - "memory.md#mem-rte-failure-derivation"
        - "memory.md#mem-obj-failure"
        - "memory.md#mem-obj-episode"
        - "runtime.md#rt-rte-consolidation-run"
        - "memory.md#mem-obj-fact"
      note: "Qualifying experience-fed updates exist, but accepted records do not establish original inputs as recorded conversational turns, tool requests/results, event callbacks or linked state/action/outcome sequences. Reports and summaries must not be relabelled by their episode container."
---

# Stash memory profile

## Comparison rationale

The comparison is architectural, not an operational success report. The accepted inventory separates the retained objects from provider weights, compiled instructions and release machinery. PostgreSQL is the substrate; pgvector is a retained vector surface. Relational edges do not independently establish graph storage. Dense vectors receive the parametric form, not natural-language form, even when generated from readable text. See [MEM-OBJ-memory-vectors](memory.md#mem-obj-memory-vectors), [MEM-OBJ-embedding-cache](memory.md#mem-obj-embedding-cache) and [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder).

Canonical citations use the memory object declarations and pattern/failure routes selected by reconciliation. Superseded epistemic object declarations, pattern extraction and failure review are not cited as independent witnesses. Their identity amendments change citation destinations, not evidence strength. The combined edge, hypothesis, goal and withdrawal routes remain valid overlaps, not aliases of their narrower epistemic routes or of the runtime consolidation container.

Curation and epistemic warrant answer different questions. Summarizing retained episodes is consolidation even when actual semantic faithfulness is unestablished. Hypothesis confirmation promotes content without necessarily accepting it against evidence; the automatic scan and direct caller confirmation have different acceptance paths. Neither extraction wording nor a command named synthesis establishes a new claim absent from its inputs. This prevents a positive synthesize classification, not the positively wired consolidation, promotion and state edits. See [EPI-RTE-fact-synthesis](epistemic.md#epi-rte-fact-synthesis), [EPI-RTE-hypothesis-assessment](epistemic.md#epi-rte-hypothesis-assessment) and [EPI-RTE-hypothesis-control](epistemic.md#epi-rte-hypothesis-control).

Read-back is split by operation. External recall and typed reload are requested pulls. Maintenance selects and supplies batches to its model without that model requesting those retained rows. Those pushes have coarse windows, embedding-based episode grouping and exact entity/property contradiction matching. Background persistence alone is not a foreground context push. No finding treats query-vector pull retrieval as inferred-embedding push. See [RT-RTE-recall-read](runtime.md#rt-rte-recall-read), [MEM-BAP-maintenance-input](memory.md#mem-bap-maintenance-input) and [EPI-RTE-contradiction-review](epistemic.md#epi-rte-contradiction-review).

Experience reports can feed qualifying automatic durable writes without authenticated logs or measured learning benefit. Failure-review outputs and episode summaries have later consumers. Their original inputs, however, are not established as conversational turns, tool execution records, discrete environmental events or linked trajectories. Thus local trace-learning positives do not fill trace_source by inference from the word episode. Generic caller content also prevents an exhaustive trace-learning conclusion. See [MEM-RTE-failure-derivation](memory.md#mem-rte-failure-derivation), [MEM-OBJ-episode](memory.md#mem-obj-episode) and [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run).

The unresolved theory-builder condition-3 label disagreement has no effect on these memory values. Neither label supplies a criticism instance or a synthesis/benefit warrant. State-dependent scans and retained rejection reasons remain supported independently. See [MEM-RTE-hypothesis-maintenance](memory.md#mem-rte-hypothesis-maintenance) and [EPI-RTE-hypothesis-assessment](epistemic.md#epi-rte-hypothesis-assessment).

Coverage remains partial where original admission control, upstream provenance, pattern/getter consumers and additional settings uses remain unresolved. There are no invented bounded-absence records and no global trace-learning negative. Known schema inventory does not imply a complete audit of every constraint or consumer. Stored validity is especially not equivalent to enforced retirement: ordinary recall still admits ended facts. See [MEM-OBJ-settings](memory.md#mem-obj-settings), [MEM-RTE-typed-read](memory.md#mem-rte-typed-read) and [MEM-RTE-fact-withdrawal](memory.md#mem-rte-fact-withdrawal).

Source-read log: no target source reads. This profile classifies only the supplied accepted records and their annotations; it adds no records, quotations, execution evidence or independent source findings.
