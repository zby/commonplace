---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "TheKnowledge comparison profile of accumulated vault content, selectors, editorial feedback, recovery state and session continuation at the frozen revision."
run-id: "AAS-2026-10-14-theknowledge-319a64927ee3-01"
source-identity: "https://github.com/BadWally/TheKnowledge"
reviewed-boundary: "aca6e29e69c6a72b697b8178841d03e6296ee3fc"
memory-comparison:
  version: 2
  scope: "Included: accumulated raw/wiki content and metadata; derived lexical/dense access stores and cache; corrected examples, policy candidates/live updates and generated domain skills; demand/evaluation/conflict histories, intents and recovery provenance; research plans, notebook registry/source maps, opaque persistent remote corpus, downloaded artifacts and wrappers; requested development-session checkpoint and opaque host alternatives; remaining included but incompletely inspected acquisition, legacy, maintenance, editing, domain lifecycle, synchronization and export routes. Excluded: static shipped instructions/schema/code and inference model weights not changed through use, ordinary transient current-call frames, external provider internals as implementation evidence, deployment-specific state and unshipped consumers. Remote retained state and host alternatives stay in the inventory despite opacity."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Local raw and wiki bodies, examples, demand, provenance, evaluation history, policies, generated skills, artifact downloads and operational intents"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-examples"
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-obj-eval-results"
                - "epistemic.md#epi-obj-policy-text"
                - "memory.md#mem-obj-artifact"
                - "runtime.md#rt-obj-intent"
              note: "The records identify retained markdown, YAML, JSON, JSONL, CSV and binary files. Encoding does not change their filesystem substrate."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-obj-demand"
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-obj-eval-results"
            - "epistemic.md#epi-obj-policy-text"
            - "memory.md#mem-obj-artifact"
            - "runtime.md#rt-obj-intent"
          note: "The records identify retained markdown, YAML, JSON, JSONL, CSV and binary files. Encoding does not change their filesystem substrate."
        - scope: "Requested development checkpoint and its requested commit"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Requested docs/session-state.md retention."
            - value: "repo"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Requested checkpoint commit preserves state across sessions."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Instructions request a markdown checkpoint and a Git commit; this is a declared retention path, not a completed write."
        - scope: "Committed deposit history and accepted queued policy provenance"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-deposit-commit"
                - "runtime.md#rt-rte-policy-edit"
              note: "Gate Git commits retain explicit paths and intent/policy provenance for later redelivery and audit decisions."
          records:
            - "runtime.md#rt-rte-deposit-commit"
            - "runtime.md#rt-rte-policy-edit"
          note: "Gate Git commits retain explicit paths and intent/policy provenance for later redelivery and audit decisions."
        - scope: "Derived lexical and vector index stores"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-section-vectors"
              note: "FTS and namespace/key/vector rows persist in SQLite. Vector names classify the operative vector store as well as its database substrate."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-section-vectors"
              note: "FTS and namespace/key/vector rows persist in SQLite. Vector names classify the operative vector store as well as its database substrate."
          records:
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-section-vectors"
          note: "FTS and namespace/key/vector rows persist in SQLite. Vector names classify the operative vector store as well as its database substrate."
        - scope: "Reloadable dense index process cache"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-section-vectors"
              note: "Retrieval additionally caches derived index state by database mtime; this is retained selector state reused by later retrieval invocations."
          records:
            - "memory.md#mem-obj-section-vectors"
          note: "Retrieval additionally caches derived index state by database mtime; this is retained selector state reused by later retrieval invocations."
        - scope: "Persistent remote notebook corpus"
          assessment: "partial"
          findings:
            - value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-query"
                - "memory.md#mem-obj-artifact"
              note: "Notebook IDs and later query establish provider-held retained service state. Its internal storage and additional substrates remain opaque."
          records:
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-obj-artifact"
          note: "Notebook IDs and later query establish provider-held retained service state. Its internal storage and additional substrates remain opaque."
        - scope: "Other included acquisition, backfill, promotion, editing, watcher and export state"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-rte-artifact-filing"
            - "memory.md#mem-obj-section-vectors"
          note: "Converter sidecars, legacy bank production, additional authoring and upload/sync, and all vector cleanup paths are not completely traced; no complete substrate inventory follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-examples"
        - "memory.md#mem-obj-demand"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-obj-eval-results"
        - "epistemic.md#epi-obj-policy-text"
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-obj-intent"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "runtime.md#rt-rte-deposit-commit"
        - "runtime.md#rt-rte-policy-edit"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-section-vectors"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-rte-local-amendments"
        - "memory.md#mem-rte-artifact-filing"
      note: "Local stores and remote service objects are supported; opaque provider storage and incompletely traced included producers prevent a complete whole-system substrate inventory. Static model weights and shipped instructions are excluded, not classified as accumulated memory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Retained raw/wiki prose, example rationales, gap text, saved recovery bodies, evaluation explanations and artifact wrappers at interpretive consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-examples"
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-obj-eval-results"
                - "memory.md#mem-obj-artifact"
              note: "Models or humans interpret these textual parts; structured envelopes and selectors are separate."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-obj-demand"
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-obj-eval-results"
            - "memory.md#mem-obj-artifact"
          note: "Models or humans interpret these textual parts; structured envelopes and selectors are separate."
        - scope: "Retained identifiers, links, domain/draft/control fields, lexical rows, queue/lease state, recovery paths and score trends at fixed software consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-examples"
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-obj-eval-results"
                - "runtime.md#rt-obj-intent"
              note: "Localized fields have fixed selector, admission, retry, rendering or recovery rules."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-obj-demand"
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-obj-eval-results"
            - "runtime.md#rt-obj-intent"
          note: "Localized fields have fixed selector, admission, retry, rendering or recovery rules."
        - scope: "Neural dense retrieval vectors and section keys"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-section-vectors"
              note: "Dense section embeddings are scored against question embeddings."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-section-vectors"
              note: "Selected keys identify live sections for subsequent lookup."
          records:
            - "memory.md#mem-obj-section-vectors"
          note: "Neural embeddings are distributed numerical representations; section keys have fixed lookup semantics."
        - scope: "Deterministic lexical dedup vectors"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-section-vectors"
              note: "Lexical dedup uses deterministic hashed lexical features, not the neural encoder; fixed feature scoring is symbolic."
          records:
            - "memory.md#mem-obj-section-vectors"
          note: "Lexical dedup uses deterministic hashed lexical features, not the neural encoder; fixed feature scoring is symbolic."
        - scope: "Policy criteria, generated host skills and requested checkpoint prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-policy-text"
                - "runtime.md#rt-rte-skill-emission"
                - "memory.md#mem-obj-session-state"
              note: "Policy criteria and emitted skill text are interpretive guidance."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-policy-text"
                - "runtime.md#rt-rte-skill-emission"
                - "memory.md#mem-obj-session-state"
              note: "Requested checkpoint prose preserves working decisions and next actions."
          records:
            - "epistemic.md#epi-obj-policy-text"
            - "runtime.md#rt-rte-skill-emission"
            - "memory.md#mem-obj-session-state"
          note: "Policy and generated skills are textual guidance. Checkpoint content is specified by instructions rather than observed production."
        - scope: "Remote notebook corpus and downloaded PDF/audio payload consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-obj-artifact"
          note: "Readable wrappers and registry IDs do not expose opaque remote selected content or the interpretation of downloaded payload bytes; no positive form is assigned to those parts."
        - scope: "Remaining converter, legacy and alternative maintenance payloads"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-rte-artifact-filing"
          note: "Their exact operative content and consumer paths are not fully inspected."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-examples"
        - "memory.md#mem-obj-demand"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-obj-eval-results"
        - "memory.md#mem-obj-artifact"
        - "memory.md#mem-obj-search-index"
        - "runtime.md#rt-obj-intent"
        - "memory.md#mem-obj-section-vectors"
        - "epistemic.md#epi-obj-policy-text"
        - "runtime.md#rt-rte-skill-emission"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-rte-local-amendments"
        - "memory.md#mem-rte-artifact-filing"
      note: "Text, symbolic selectors and numerical dense representations coexist. Wrapper inspection does not resolve remote or binary payload form; included uninspected paths remain unresolved."
    lineage:
      assessment: "partial"
      units:
        - scope: "Acquired raw source content"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Source acquisition imports retained content. Adapter-specific extraction/normalization and externally populated initial vault provenance remain unresolved."
          records:
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-rte-ingest-authorship"
          note: "Source acquisition imports retained content. Adapter-specific extraction/normalization and externally populated initial vault provenance remain unresolved."
        - scope: "Model-produced wiki updates, local answers, digest prose and caller page content"
          assessment: "partial"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-retrieve-answer"
                - "memory.md#mem-rte-digest-authoring"
                - "memory.md#mem-rte-local-amendments"
                - "runtime.md#rt-rte-deposit-commit"
              note: "Model and caller authorship routes exist. Caller human identity, original vault provenance and the exact derivation of every retained claim are unresolved."
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-ingest-authorship"
            - "runtime.md#rt-rte-retrieve-answer"
            - "memory.md#mem-rte-digest-authoring"
            - "memory.md#mem-rte-local-amendments"
            - "runtime.md#rt-rte-deposit-commit"
          note: "Model and caller authorship routes exist. Caller human identity, original vault provenance and the exact derivation of every retained claim are unresolved."
        - scope: "Source-page wrappers, search rows, dense/lexical vectors and domain skills derived from retained content"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-section-vectors"
                - "runtime.md#rt-rte-skill-emission"
              note: "Inspected code compiles copied metadata, index rows/vectors and skill text. Initial vector encoder provenance and complete update/removal scheduling are unresolved."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-section-vectors"
            - "runtime.md#rt-rte-skill-emission"
          note: "Inspected code compiles copied metadata, index rows/vectors and skill text. Initial vector encoder provenance and complete update/removal scheduling are unresolved."
        - scope: "Remote synthesis filed locally and remote artifact downloads"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-query"
                - "memory.md#mem-rte-artifact-filing"
                - "memory.md#mem-obj-artifact"
              note: "Gateway imports provider-produced prose/payloads. Remote derivation is opaque, and briefing report bytes do not survive the wrapper overwrite."
          records:
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-rte-artifact-filing"
            - "memory.md#mem-obj-artifact"
          note: "Gateway imports provider-produced prose/payloads. Remote derivation is opaque, and briefing report bytes do not survive the wrapper overwrite."
        - scope: "Pinned correction examples derived from editorial decision feedback"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
              note: "Software persists selected decision/score/rationale feedback in a durable example. This is extraction of decision experience, not automatic capture of all filter calls."
          records:
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
          note: "Software persists selected decision/score/rationale feedback in a durable example. This is extraction of decision experience, not automatic capture of all filter calls."
        - scope: "Example-fed policy candidates"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-distillation"
                - "memory.md#mem-obj-examples"
              note: "Distillation automatically derives candidate criteria from selected decision examples. Original legacy labels and their derivation remain uninspected."
          records:
            - "runtime.md#rt-rte-policy-distillation"
            - "memory.md#mem-obj-examples"
          note: "Distillation automatically derives candidate criteria from selected decision examples. Original legacy labels and their derivation remain uninspected."
        - scope: "Agent checkpoint derived from session working memory"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Requested working-memory extraction into a durable checkpoint."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Instructions ask the foreground agent to summarize decisions and rejected approaches. Exact source turns and alternative host summaries/tails are opaque."
        - scope: "Automatic gap, recovery, evaluation and conflict histories"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-demand-feedback"
                - "memory.md#mem-rte-corpus-recovery"
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-contradiction-scan"
              note: "Code records request/operation history, saved content, judgments and diagnostic snapshots for later consumers."
          records:
            - "memory.md#mem-rte-demand-feedback"
            - "memory.md#mem-rte-corpus-recovery"
            - "memory.md#mem-rte-evaluation-retention"
            - "epistemic.md#epi-rte-contradiction-scan"
          note: "Code records request/operation history, saved content, judgments and diagnostic snapshots for later consumers."
        - scope: "Additional acquisition, legacy bank, policy promotion and notebook synchronization routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-rte-artifact-filing"
          note: "These included routes cannot be assigned complete lineage from their names or one inspected producer."
      records:
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-ingest-authorship"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-retrieve-answer"
        - "memory.md#mem-rte-digest-authoring"
        - "memory.md#mem-rte-local-amendments"
        - "runtime.md#rt-rte-deposit-commit"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-section-vectors"
        - "runtime.md#rt-rte-skill-emission"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-obj-artifact"
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-rte-corpus-recovery"
        - "memory.md#mem-rte-evaluation-retention"
        - "epistemic.md#epi-rte-contradiction-scan"
      note: "Imported, authored, compiled and trace-extracted paths are supported locally. Initial and provider provenance and uninspected alternate producers prevent a complete lineage account."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Raw/wiki prose delivered to plan models, answering models and requested neighborhood readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-retrieve-answer"
                - "memory.md#mem-rte-neighborhood-fetch"
              note: "Selected retained content provides evidence/reference/context, not mandatory execution policy."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-ingest-authorship"
            - "runtime.md#rt-rte-retrieve-answer"
            - "memory.md#mem-rte-neighborhood-fetch"
          note: "Selected retained content provides evidence/reference/context, not mandatory execution policy."
        - scope: "Retained section text, title/link/trust/draft metadata and dense vectors at retrieval rankers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-section-vectors"
                - "runtime.md#rt-rte-retrieve-answer"
              note: "Retained text/features and access metadata influence relative priority even though ranking code is fixed."
          records:
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-section-vectors"
            - "runtime.md#rt-rte-retrieve-answer"
          note: "Retained text/features and access metadata influence relative priority even though ranking code is fixed."
        - scope: "Live editorial criteria and selected corrected examples at the filter model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-policy-text"
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
              note: "Criteria and calibration examples direct future scoring; software thresholds separately decide source admission."
          records:
            - "epistemic.md#epi-obj-policy-text"
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
          note: "Criteria and calibration examples direct future scoring; software thresholds separately decide source admission."
        - scope: "Example feedback at policy-candidate distillation"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-examples"
                - "runtime.md#rt-rte-policy-distillation"
              note: "Retained decision explanations feed an automatic durable guidance-artifact update. This learning force does not demonstrate improved capacity or live candidate installation."
          records:
            - "memory.md#mem-obj-examples"
            - "runtime.md#rt-rte-policy-distillation"
          note: "Retained decision explanations feed an automatic durable guidance-artifact update. This learning force does not demonstrate improved capacity or live candidate installation."
        - scope: "Generated domain skill at a later host agent"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-emission"
                - "runtime.md#rt-bap-domain-skill"
              note: "Generated usage/criteria text directs later host work when loaded."
            - value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-skill-emission"
                - "runtime.md#rt-bap-domain-skill"
              note: "Selected concept/entity links and synthesis titles supply domain context when loaded."
          records:
            - "runtime.md#rt-rte-skill-emission"
            - "runtime.md#rt-bap-domain-skill"
          note: "Persisted skill supplies usage directions and selected domain reference material if the host discovers and loads it."
        - scope: "Requested checkpoint at resumed foreground agent"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Next action and open-contract guidance are requested inputs to resumed work."
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Retained decisions and rejected-approach reasons are requested working context."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Instructions afford later checkpoint reread and interpretation, with tree verification and escalation requested rather than enforced."
        - scope: "Retained policy thresholds and queue retry/fencing/identity state at admission and worker consumers"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-policy-edit"
                - "runtime.md#rt-obj-intent"
                - "runtime.md#rt-rte-deposit-commit"
              note: "Policy thresholds and queued version/fencing/committed-history criteria determine admissibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-policy-edit"
                - "runtime.md#rt-obj-intent"
                - "runtime.md#rt-rte-deposit-commit"
              note: "Failed checks or already committed identity can refuse admission/redelivery."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-policy-edit"
                - "runtime.md#rt-obj-intent"
                - "runtime.md#rt-rte-deposit-commit"
              note: "Typed queue dispatch and lifecycle state choose processing and recovery routes."
          records:
            - "runtime.md#rt-rte-ingest-authorship"
            - "runtime.md#rt-rte-policy-edit"
            - "runtime.md#rt-obj-intent"
            - "runtime.md#rt-rte-deposit-commit"
          note: "Thresholds and identity/version/lease/history checks provide criteria and can veto admission or redelivery; typed payload state chooses worker operation."
        - scope: "Query plans, notebook registry and source maps at research resumption/query rendering"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-research-query"
              note: "Retained plans and IDs choose resumed search/corpus access; source maps furnish source references for local rendering."
          records:
            - "runtime.md#rt-rte-research-query"
          note: "Retained plans and IDs choose resumed search/corpus access; source maps furnish source references for local rendering."
        - scope: "Gap history and trigger IDs at preflight/clustering"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-rte-demand-feedback"
              note: "Preflight returns overlapping historical demand as planning context."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-rte-demand-feedback"
              note: "Gap recurrence selects synthesis-shaped queue submissions."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-rte-demand-feedback"
              note: "Triggered identity membership tests eligibility for another submission."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-demand"
                - "memory.md#mem-rte-demand-feedback"
              note: "Recorded trigger IDs suppress repeated submission."
          records:
            - "memory.md#mem-obj-demand"
            - "memory.md#mem-rte-demand-feedback"
          note: "Raw gaps supply planning diagnostics; recurrence selects queued work; retained trigger identities suppress duplicate submission."
        - scope: "Recovery provenance at reachability checks and restoration"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-rte-corpus-recovery"
              note: "Provenance reachability constrains cleanup eligibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-rte-corpus-recovery"
              note: "Referenced pages are excluded from scan-time deletion candidates."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-rte-corpus-recovery"
              note: "Exact target and act identity select recovery content/operation."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provenance"
                - "memory.md#mem-rte-corpus-recovery"
              note: "Recorded page text is the content basis for restoration."
          records:
            - "memory.md#mem-obj-provenance"
            - "memory.md#mem-rte-corpus-recovery"
          note: "Saved paths determine cleanup eligibility; stored bodies supply reconstruction content; act identity locates withdrawal targets."
        - scope: "Evaluation history at status and retained goldens at evaluator gates"
          assessment: "partial"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-results"
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-retrieval-measure"
                - "epistemic.md#epi-rte-filter-calibration"
                - "runtime.md#rt-rte-policy-edit"
              note: "Trend scores and deltas supply operator assessment context."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-results"
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-retrieval-measure"
                - "epistemic.md#epi-rte-filter-calibration"
                - "runtime.md#rt-rte-policy-edit"
              note: "Retained expected slugs and labels determine reference conformity."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-eval-results"
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-retrieval-measure"
                - "epistemic.md#epi-rte-filter-calibration"
                - "runtime.md#rt-rte-policy-edit"
              note: "Policy-edit retrieval and merge nonregression results can block replacement."
          records:
            - "memory.md#mem-obj-eval-results"
            - "memory.md#mem-rte-evaluation-retention"
            - "epistemic.md#epi-rte-retrieval-measure"
            - "epistemic.md#epi-rte-filter-calibration"
            - "runtime.md#rt-rte-policy-edit"
          note: "Status supplies advisory history; goldens supply validation criteria and policy gates can veto. Initial golden provenance and full result consumers remain uninspected."
        - scope: "Opaque remote payload consumers and incompletely inspected alternative maintenance consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "memory.md#mem-rte-artifact-filing"
            - "memory.md#mem-obj-section-vectors"
            - "memory.md#mem-rte-local-amendments"
          note: "Known wrapper and rank effects cannot identify every remote consumed part or authority on alternative included routes."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-ingest-authorship"
        - "runtime.md#rt-rte-retrieve-answer"
        - "memory.md#mem-rte-neighborhood-fetch"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-section-vectors"
        - "epistemic.md#epi-obj-policy-text"
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "runtime.md#rt-rte-skill-emission"
        - "runtime.md#rt-bap-domain-skill"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "runtime.md#rt-rte-policy-edit"
        - "runtime.md#rt-obj-intent"
        - "runtime.md#rt-rte-deposit-commit"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-obj-demand"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-rte-corpus-recovery"
        - "memory.md#mem-obj-eval-results"
        - "memory.md#mem-rte-evaluation-retention"
        - "epistemic.md#epi-rte-retrieval-measure"
        - "epistemic.md#epi-rte-filter-calibration"
        - "memory.md#mem-obj-artifact"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-rte-local-amendments"
      note: "Authority is consumer-specific: interpretive knowledge/instruction, priority inputs, update inputs, routing and admission/veto controls coexist. Provider payloads and additional included consumer paths prevent complete coverage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Generated page admission, direct digest admission, query filing, skill emission and bootstrap"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
                - "runtime.md#rt-rte-retrieve-answer"
                - "runtime.md#rt-rte-research-query"
                - "memory.md#mem-rte-digest-authoring"
                - "runtime.md#rt-rte-skill-emission"
                - "runtime.md#rt-rte-policy-bootstrap"
              note: "Code/model admission lacks compulsory per-content human approval. Starting these workflows does not make subsequent admission manual."
          records:
            - "runtime.md#rt-rte-ingest-authorship"
            - "runtime.md#rt-rte-retrieve-answer"
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-rte-digest-authoring"
            - "runtime.md#rt-rte-skill-emission"
            - "runtime.md#rt-rte-policy-bootstrap"
          note: "Code/model admission lacks compulsory per-content human approval. Starting these workflows does not make subsequent admission manual."
        - scope: "Worker admission of deposited content and deterministic recovery/demand output"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-deposit-commit"
                - "memory.md#mem-rte-corpus-recovery"
                - "memory.md#mem-rte-demand-feedback"
              note: "Worker software independently renders/checks/adopts retained output; caller payload authorship is separate from this admission."
          records:
            - "runtime.md#rt-rte-deposit-commit"
            - "memory.md#mem-rte-corpus-recovery"
            - "memory.md#mem-rte-demand-feedback"
          note: "Worker software independently renders/checks/adopts retained output; caller payload authorship is separate from this admission."
        - scope: "Derived index refresh, evaluation history and bibliographic metadata updates"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-index"
                - "memory.md#mem-obj-section-vectors"
                - "memory.md#mem-rte-evaluation-retention"
                - "memory.md#mem-rte-source-maintenance"
                - "epistemic.md#epi-rte-contradiction-scan"
              note: "Inspected software transformations and persistence decide admission without a per-result human approver."
          records:
            - "memory.md#mem-obj-search-index"
            - "memory.md#mem-obj-section-vectors"
            - "memory.md#mem-rte-evaluation-retention"
            - "memory.md#mem-rte-source-maintenance"
            - "epistemic.md#epi-rte-contradiction-scan"
          note: "Inspected software transformations and persistence decide admission without a per-result human approver."
        - scope: "Correction pinning into durable examples"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
              note: "Software validates and pins the feedback example; user-correction naming does not authenticate the proposer as human."
          records:
            - "memory.md#mem-rte-example-correction"
          note: "Software validates and pins the feedback example; user-correction naming does not authenticate the proposer as human."
        - scope: "Correction labels, caller deposits/local edits, force overrides and queued policy replacement proposals"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-example-correction"
            - "runtime.md#rt-rte-deposit-commit"
            - "memory.md#mem-rte-local-amendments"
            - "runtime.md#rt-rte-ingest-authorship"
            - "runtime.md#rt-rte-policy-edit"
          note: "Generic caller identity and server principal do not establish explicit human content control. No manual value is inferred from CLI access or initiation."
        - scope: "Requested checkpoint writing and replacement"
          assessment: "partial"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Foreground agent is requested to select and admit the summary."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Hooks request agent selection, writing and committing without compulsory human approval; actual checkpoint and host alternatives remain opaque."
        - scope: "Legacy initialization, candidate promotion, additional domain lifecycle and upload/sync mechanisms"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-examples"
            - "runtime.md#rt-rte-policy-distillation"
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-rte-artifact-filing"
          note: "Human versus software admission is unresolved on the remaining included paths; declared human review is not evidence of a completed manual promotion."
      records:
        - "runtime.md#rt-rte-ingest-authorship"
        - "runtime.md#rt-rte-retrieve-answer"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-rte-digest-authoring"
        - "runtime.md#rt-rte-skill-emission"
        - "runtime.md#rt-rte-policy-bootstrap"
        - "runtime.md#rt-rte-deposit-commit"
        - "memory.md#mem-rte-corpus-recovery"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-obj-search-index"
        - "memory.md#mem-obj-section-vectors"
        - "memory.md#mem-rte-evaluation-retention"
        - "memory.md#mem-rte-source-maintenance"
        - "epistemic.md#epi-rte-contradiction-scan"
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-rte-local-amendments"
        - "runtime.md#rt-rte-policy-edit"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-rte-artifact-filing"
      note: "Automatic admission is supported on inspected routes. No authenticated per-content human decision establishes manual admission; unknown caller control, legacy initialization and opaque host/provider paths remain unresolved rather than negative."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Gate entity duplicate merging"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-deposit-commit"
                - "epistemic.md#epi-rte-conflict-selection"
              note: "Gate uses deterministic dedup/domain rules and can merge same-kind normalized-name entries; identity policy does not verify factual co-reference."
          records:
            - "runtime.md#rt-rte-deposit-commit"
            - "epistemic.md#epi-rte-conflict-selection"
          note: "Gate uses deterministic dedup/domain rules and can merge same-kind normalized-name entries; identity policy does not verify factual co-reference."
        - scope: "Existing-page full updates and named section replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
                - "memory.md#mem-rte-local-amendments"
                - "memory.md#mem-obj-wiki"
              note: "These routes revise retained entries. Their validators and draft modes differ, and claim truth is not established."
          records:
            - "runtime.md#rt-rte-ingest-authorship"
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-obj-wiki"
          note: "These routes revise retained entries. Their validators and draft modes differ, and claim truth is not established."
        - scope: "Recent retained sources summarized into daily digest"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-digest-authoring"
              note: "The implemented route asks a model for a reduced summary of existing source heads, retains it and makes it available to later retrieval. Summary faithfulness remains unobserved."
          records:
            - "memory.md#mem-rte-digest-authoring"
          note: "The implemented route asks a model for a reduced summary of existing source heads, retains it and makes it available to later retrieval. Summary faithfulness remains unobserved."
        - scope: "Selected domain content rendered as generated skill"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-emission"
              note: "Code selects/caps policy, links and synthesis titles into a reduced guidance artifact; this is consolidation rather than trace-fed synthesis."
          records:
            - "runtime.md#rt-rte-skill-emission"
          note: "Code selects/caps policy, links and synthesis titles into a reduced guidance artifact; this is consolidation rather than trace-fed synthesis."
        - scope: "Example-fed criteria replacement candidates"
          assessment: "partial"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-distillation"
                - "memory.md#mem-obj-examples"
              note: "Route proposes tightened criteria and removal of nondiscriminating ones. Exact candidate semantic relation is not established; replacing criteria supports evolution, not a proven novel claim."
          records:
            - "runtime.md#rt-rte-policy-distillation"
            - "memory.md#mem-obj-examples"
          note: "Route proposes tightened criteria and removal of nondiscriminating ones. Exact candidate semantic relation is not established; replacing criteria supports evolution, not a proven novel claim."
        - scope: "Requested session checkpoint summary"
          assessment: "partial"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Requested selected summary reduces accumulated session material."
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Later snapshots can replace the retained working checkpoint."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Instructions request compression of session working memory and replacement of checkpoint content. Opaque host alternatives and actual agent fulfillment remain unresolved."
        - scope: "Draft finalization and abandonment"
          assessment: "known"
          findings:
            - value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-draft-finalization"
              note: "Finalization raises retained page status after strict checks; abandonment removes a draft. These effects do not mean factual acceptance."
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-draft-finalization"
              note: "Finalization raises retained page status after strict checks; abandonment removes a draft. These effects do not mean factual acceptance."
          records:
            - "runtime.md#rt-rte-draft-finalization"
          note: "Finalization raises retained page status after strict checks; abandonment removes a draft. These effects do not mean factual acceptance."
        - scope: "De-path cleanup and annotation withdrawal with preserved recovery history"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-corpus-recovery"
                - "epistemic.md#epi-rte-resolution-revert"
                - "memory.md#mem-obj-provenance"
              note: "De-path removes canonical pages from subsequent ordinary retrieval."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-corpus-recovery"
                - "epistemic.md#epi-rte-resolution-revert"
                - "memory.md#mem-obj-provenance"
              note: "Resolution reversion withdraws current annotation reliance while retaining the reverted act history."
          records:
            - "memory.md#mem-rte-corpus-recovery"
            - "epistemic.md#epi-rte-resolution-revert"
            - "memory.md#mem-obj-provenance"
          note: "Deletion forgets canonical content while saved history permits restoration; successful resolution reversal withdraws the annotation and marks its retained act reverted."
        - scope: "Retraction/supersession review signals"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-source-maintenance"
          note: "Metadata marks old sources and lists dependents, but inspected retrieval still admits their claims. No universal invalidation or decay finding follows for this route."
        - scope: "Opaque remote transformations and other included maintenance, promotion, backfill and reverse-merge branches"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-artifact-filing"
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-obj-section-vectors"
            - "memory.md#mem-rte-corpus-recovery"
          note: "Actual transformations are not exhaustively inspected; names cannot establish synthesize or any additional operation."
      records:
        - "runtime.md#rt-rte-deposit-commit"
        - "epistemic.md#epi-rte-conflict-selection"
        - "runtime.md#rt-rte-ingest-authorship"
        - "memory.md#mem-rte-local-amendments"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-rte-digest-authoring"
        - "runtime.md#rt-rte-skill-emission"
        - "runtime.md#rt-rte-policy-distillation"
        - "memory.md#mem-obj-examples"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "runtime.md#rt-rte-draft-finalization"
        - "memory.md#mem-rte-corpus-recovery"
        - "epistemic.md#epi-rte-resolution-revert"
        - "memory.md#mem-obj-provenance"
        - "memory.md#mem-rte-source-maintenance"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-obj-section-vectors"
      note: "Consolidation, deduplication, revision, status promotion, forgetting and bounded annotation invalidation have local warrants. No supported synthesis value is inferred from model fluency, empty demand output or a synthesis filename; other included transformations remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit retrieve/answer, neighborhood context and persistent notebook query returns"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-retrieve-answer"
                - "memory.md#mem-rte-neighborhood-fetch"
                - "runtime.md#rt-rte-research-query"
              note: "These supply retained material in fulfillment of a consumer request. Ranking or graph walking within a requested return is not another unsolicited push."
          records:
            - "runtime.md#rt-rte-retrieve-answer"
            - "memory.md#mem-rte-neighborhood-fetch"
            - "runtime.md#rt-rte-research-query"
          note: "These supply retained material in fulfillment of a consumer request. Ranking or graph walking within a requested return is not another unsolicited push."
        - scope: "Explicit evaluate/status, preflight/demand and restore requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-retention"
                - "memory.md#mem-rte-demand-feedback"
                - "memory.md#mem-rte-corpus-recovery"
              note: "Requested operations reload retained evaluation trends, gaps and saved page content for their named consumer."
          records:
            - "memory.md#mem-rte-evaluation-retention"
            - "memory.md#mem-rte-demand-feedback"
            - "memory.md#mem-rte-corpus-recovery"
          note: "Requested operations reload retained evaluation trends, gaps and saved page content for their named consumer."
        - scope: "Existing-page context supplied to the plan model during ingest"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Ingest code automatically selects retained pages on title/domain context and delivers them without the plan model requesting particular retained pages."
          records:
            - "runtime.md#rt-rte-ingest-authorship"
          note: "Ingest code automatically selects retained pages on title/domain context and delivers them without the plan model requesting particular retained pages."
        - scope: "Policy and example context supplied to later filter model calls"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Filter construction automatically delivers current criteria and selected retained decision examples on each invoked filtering path."
          records:
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
            - "runtime.md#rt-rte-ingest-authorship"
          note: "Filter construction automatically delivers current criteria and selected retained decision examples on each invoked filtering path."
        - scope: "Retained context selected for evaluator and candidate distillation model calls"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-retention"
                - "runtime.md#rt-rte-policy-distillation"
                - "epistemic.md#epi-rte-filter-calibration"
              note: "Orchestration automatically supplies selected retained wiki/source context and sampled examples/reference labels to these model consumers."
          records:
            - "memory.md#mem-rte-evaluation-retention"
            - "runtime.md#rt-rte-policy-distillation"
            - "epistemic.md#epi-rte-filter-calibration"
          note: "Orchestration automatically supplies selected retained wiki/source context and sampled examples/reference labels to these model consumers."
        - scope: "Requested checkpoint reanchor and generated skill discovery"
          assessment: "partial"
          findings:
            - value: "push"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
                - "runtime.md#rt-rte-skill-emission"
              note: "SessionStart instruction requests checkpoint context before plan/write when the predicate holds."
            - value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
                - "runtime.md#rt-rte-skill-emission"
              note: "Host discovery/loading can supply the retained generated skill to a later foreground session."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
            - "runtime.md#rt-rte-skill-emission"
          note: "Checkpoint reread is requested by host-event instruction rather than mechanically performed; generated skills afford later host-triggered delivery. Exact host selectors and actual delivery remain unresolved."
        - scope: "Remote selected corpus, downloaded payload rereads and remaining included callers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "memory.md#mem-rte-artifact-filing"
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-rte-local-amendments"
          note: "Remote selection/delivery, automatic model payload reload and untraced additional readers cannot be classified from local wrappers or known pull routes."
      records:
        - "runtime.md#rt-rte-retrieve-answer"
        - "memory.md#mem-rte-neighborhood-fetch"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-rte-evaluation-retention"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-rte-corpus-recovery"
        - "runtime.md#rt-rte-ingest-authorship"
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "epistemic.md#epi-rte-filter-calibration"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "runtime.md#rt-rte-skill-emission"
        - "memory.md#mem-obj-artifact"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-rte-local-amendments"
      note: "Pull returns and internal automatic context push coexist. Static hook instructions themselves are excluded accumulated memory; their requested checkpoint delivery and generated skill affordance remain separate from opaque host/provider alternatives."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Ingest page push to plan model"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Title-query/domain ranking selects whole existing pages."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Fallback domain glob, page count and byte budget select available pages without query-specific matching."
          records:
            - "runtime.md#rt-rte-ingest-authorship"
          note: "Trigger: authored ingest. Input: retained source title and chosen domain. Selected part: existing wiki pages. Ranked title-query selection and unranked glob fallback are distinct selectors."
        - scope: "Example and policy push to filter model"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Effective-domain identity chooses the matching policy/example bank."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
                - "runtime.md#rt-rte-ingest-authorship"
              note: "Balanced/recent/corrections-weighted strategy and count caps select examples; no semantic query match is established."
          records:
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
            - "runtime.md#rt-rte-ingest-authorship"
          note: "Trigger: filter invocation. Input: effective domain and policy strategy/count. Selected parts: policy and example labels/scores/rationales/IDs, not stored excerpt bodies."
        - scope: "Example push to distillation model"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-distillation"
                - "memory.md#mem-obj-examples"
              note: "Domain chooses the corresponding retained bank and current policy."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-policy-distillation"
                - "memory.md#mem-obj-examples"
              note: "First include/exclude samples and text caps determine delivered example lines."
          records:
            - "runtime.md#rt-rte-policy-distillation"
            - "memory.md#mem-obj-examples"
          note: "Trigger: distillation. Input: domain bank and decision category. Selected parts: sampled titles and capped rationales."
        - scope: "Wiki/source context push to judge and calibration classifier"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-filter-calibration"
              note: "Domain and synthesis/calibration source-ID matches select delivered retained parts."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-retention"
                - "epistemic.md#epi-rte-filter-calibration"
              note: "Page-type line caps, source-body ceilings and example limits restrict context."
          records:
            - "memory.md#mem-rte-evaluation-retention"
            - "epistemic.md#epi-rte-filter-calibration"
          note: "Trigger: evaluation/calibration. Inputs: domain and retained reference entries/source IDs. Selected parts: domain wiki bodies, enumerated raw source bodies or capped source text."
        - scope: "Checkpoint requested on host SessionStart"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-session-reanchor"
                - "memory.md#mem-obj-session-state"
              note: "Existence/mtime condition requests reread of the checkpoint; distinct hook and CLAUDE predicates and compliance limits remain."
          records:
            - "runtime.md#rt-rte-session-reanchor"
            - "memory.md#mem-obj-session-state"
          note: "Trigger: SessionStart. Input: checkpoint existence/mtime. Selected part: requested whole checkpoint. This is coarse availability/time gating, not targeted identity selection within the file."
        - scope: "Generated skill host loading and opaque remote corpus selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-emission"
            - "runtime.md#rt-bap-domain-skill"
            - "runtime.md#rt-rte-research-query"
            - "memory.md#mem-obj-artifact"
          note: "Host discovery and provider selection inputs are not disclosed sufficiently to classify their automatic selectors. Declared skill triggers alone are not wired identity matches."
        - scope: "Requested retrieve/neighborhood return operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-retrieve-answer"
            - "memory.md#mem-rte-neighborhood-fetch"
          note: "These local operations fulfill explicit retained-material requests; push selection signals do not classify their lexical, dense or identifier pull selectors."
        - scope: "Additional included context/maintenance selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-local-amendments"
            - "memory.md#mem-rte-artifact-filing"
            - "memory.md#mem-obj-section-vectors"
          note: "Unknown consumers/selectors on remaining included routes cannot be made inapplicable by the inspected requested-return paths."
      records:
        - "runtime.md#rt-rte-ingest-authorship"
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "memory.md#mem-rte-evaluation-retention"
        - "epistemic.md#epi-rte-filter-calibration"
        - "runtime.md#rt-rte-session-reanchor"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-skill-emission"
        - "runtime.md#rt-bap-domain-skill"
        - "runtime.md#rt-rte-research-query"
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-retrieve-answer"
        - "memory.md#mem-rte-neighborhood-fetch"
        - "memory.md#mem-rte-local-amendments"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-obj-section-vectors"
      note: "Coarse, identifier and lexical push selectors have scoped support. Dense retrieval embeddings are a pull selector here, so inferred-embedding is not added as a push signal. Opaque host/provider and uninspected alternatives prevent complete assessment."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Correction decision feedback to pinned example to future filter guidance"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-example-correction"
                - "memory.md#mem-obj-examples"
                - "memory.md#mem-bap-example-calibration"
              note: "Code automatically admits durable decision/rationale examples; selected examples later shape filter model guidance. Human identity is unresolved, but automatic example admission and later consumer are wired. No improved capacity is claimed."
          records:
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-bap-example-calibration"
          note: "Code automatically admits durable decision/rationale examples; selected examples later shape filter model guidance. Human identity is unresolved, but automatic example admission and later consumer are wired. No improved capacity is claimed."
        - scope: "Example-fed durable policy candidates and intended review"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-policy-distillation"
                - "memory.md#mem-obj-examples"
                - "epistemic.md#epi-rte-filter-calibration"
              note: "Durable guidance candidate from past decisions is available for a later reviewer; downstream live policy adoption is unresolved."
          records:
            - "runtime.md#rt-rte-policy-distillation"
            - "memory.md#mem-obj-examples"
            - "epistemic.md#epi-rte-filter-calibration"
          note: "Automatic trace-fed candidate writing is wired; retained candidate is afforded for later review, but live installation and subsequent deployed use are not wired by this route."
        - scope: "Session working memory to durable checkpoint to resumed agent"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-session-state"
                - "runtime.md#rt-rte-session-reanchor"
              note: "Requested trace-fed checkpoint is durable context/guidance for later foreground sessions."
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "A generated continuation summary qualifies even without new claims. The source establishes requested automatic agent production and later reread, not completed production or exact host compaction inputs."
        - scope: "Demand history, evaluation results, recovery histories and conflict diagnostic snapshots"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-demand-feedback"
            - "memory.md#mem-rte-evaluation-retention"
            - "memory.md#mem-rte-corpus-recovery"
            - "epistemic.md#epi-rte-contradiction-scan"
          note: "These have automatic history writes and named later consumers, but records do not establish a further durable behavior-shaping artifact on every route. Empty demand body, advisory score display and restoration are not by themselves universal trace-learning witnesses."
        - scope: "Static source-based digest/skill routes, mixed acquired source content and remaining legacy/host/provider update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-digest-authoring"
            - "runtime.md#rt-rte-skill-emission"
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-rte-artifact-filing"
            - "runtime.md#rt-rte-session-reanchor"
          note: "Digest/skill records do not demonstrate trace-fed inputs; static acquired content alone is not a trace. Original mixed acquisition/legacy provenance and opaque alternatives prevent bounded route-wide no findings."
      records:
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "memory.md#mem-bap-example-calibration"
        - "runtime.md#rt-rte-policy-distillation"
        - "epistemic.md#epi-rte-filter-calibration"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-rte-evaluation-retention"
        - "memory.md#mem-rte-corpus-recovery"
        - "epistemic.md#epi-rte-contradiction-scan"
        - "memory.md#mem-rte-digest-authoring"
        - "runtime.md#rt-rte-skill-emission"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-rte-artifact-filing"
      note: "Correction reuse establishes a positive wired route; candidate guidance and session continuation have weaker local warrants. There are no supplied bounded absence records supporting a system-wide or local no; unresolved alternatives remain explicit. This axis is independent of demonstrated learning or self-improvement."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Correction/example and candidate-distillation original feedback inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-example-correction"
            - "memory.md#mem-obj-examples"
            - "runtime.md#rt-rte-policy-distillation"
          note: "Records identify past editorial labels/rationales and mixed human/agent/legacy provenance, but not whether original qualifying content was conversational turns, logged tool results, environmental events or linked trajectories. CLI/MCP transport alone does not establish tool-traces or event-streams."
        - scope: "Requested checkpoint original foreground session material"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session-state"
            - "runtime.md#rt-rte-session-reanchor"
          note: "The requested summary concerns working memory, decisions, rejected approaches and next action. Neither record identifies recorded conversational turns as its original input. Exact source turns, included tool results and host summary/tail provenance remain uninspected, preventing classification as session-logs or another controlled trace source."
        - scope: "Opaque host checkpoint variants and remaining candidate/legacy/acquisition origins"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-session-reanchor"
            - "memory.md#mem-obj-examples"
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-rte-artifact-filing"
          note: "Neither opaque compaction alternatives nor incompletely traced legacy sources can be assigned original trace content. Imported static instructions are not trace-source evidence."
        - scope: "Demand, evaluation and recovery histories without a fully resolved qualifying write chain"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-demand-feedback"
            - "memory.md#mem-rte-evaluation-retention"
            - "memory.md#mem-rte-corpus-recovery"
            - "epistemic.md#epi-rte-contradiction-scan"
          note: "Raw history origin is not aggregated into trace_source unless a qualifying trace-learning write and later behavior-shaping consumer are established for the same unit."
      records:
        - "memory.md#mem-rte-example-correction"
        - "memory.md#mem-obj-examples"
        - "runtime.md#rt-rte-policy-distillation"
        - "memory.md#mem-obj-session-state"
        - "runtime.md#rt-rte-session-reanchor"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-rte-artifact-filing"
        - "memory.md#mem-rte-demand-feedback"
        - "memory.md#mem-rte-evaluation-retention"
        - "memory.md#mem-rte-corpus-recovery"
        - "epistemic.md#epi-rte-contradiction-scan"
      note: "No controlled original-input category is established by the accepted records. Correction learning is wired and checkpoint continuation is claimed, but neither working-memory origin nor transport/adapter labels establish recorded conversational turns, tool results, environmental events or trajectories. Uninspected alternatives remain included. Without positive source findings the axis is not-determinable, not partial; it is not inapplicable because qualifying trace-fed routes remain included."
---

# TheKnowledge memory profile

## Comparison rationale

This profile classifies accepted records, not the entire runtime's stores or the truth of its wiki claims. Nine axes remain partial because the accepted inventory retains opaque or uninspected included alternatives alongside supported positives. Trace source is not-determinable: the accepted records establish no controlled original-input value. A known local unit means its named classification is resolved at its evidence layer; it does not mean observed operation. No target execution or causal evidence upgrades the wired, afforded or claimed findings.

Canonical identity follows reconciliation: the imported source-text object resolves to [MEM-OBJ-raw](memory.md#mem-obj-raw), and the caller correction route resolves to [MEM-RTE-example-correction](memory.md#mem-rte-example-correction). The profile uses these replacement records, not the superseded epistemic IDs. The broad epistemic policy/content/result containers remain valid alongside their narrower memory objects; their existence does not duplicate units or erase uncertainty.

Read-back separates the requested tool return from automatic delivery to a different model consumer. Question retrieval and neighborhood fetch are pull even when ranking or graph expansion chooses their contents. Ingest page selection, example injection and evaluator context construction are push to their model consumers. Dense question retrieval therefore does not establish an embedding push signal. [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [MEM-RTE-neighborhood-fetch](memory.md#mem-rte-neighborhood-fetch), [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [MEM-RTE-example-correction](memory.md#mem-rte-example-correction), [MEM-RTE-evaluation-retention](memory.md#mem-rte-evaluation-retention).

Examples carry interpretive directions into scoring and learning force when consumed to produce durable criterion candidates. Their automatic pinning is independent of whether the original correction caller was human. A software-admitted candidate or page is not manual merely because an operator began the command. Conversely, unidentified callers do not establish human decisions. Candidate promotion, initial legacy-bank control and host checkpoint production remain unresolved. [MEM-OBJ-examples](memory.md#mem-obj-examples), [MEM-RTE-example-correction](memory.md#mem-rte-example-correction), [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [MEM-OBJ-session-state](memory.md#mem-obj-session-state).

Trace learning is assessed by durable automatic trace-fed artifacts and later consumers, not demonstrated improvement. The requested continuation summary qualifies at the claimed layer, while actual checkpoint creation, exact selected session turns and host-generated alternatives remain opaque. Correction guidance qualifies at the wired layer, but its recorded decision-feedback origin is insufficient to choose an original-input category without treating a transport label as evidence. Distilled candidates retain an afforded reviewer path rather than a wired deployment path. These limits stay in trace_source as well as trace_learning. In particular, the checkpoint's working-memory origin does not establish recorded conversational turns. The unsupported claimed session-logs finding is withdrawn; no other controlled source value replaces it, so both the checkpoint source unit and the trace_source axis are not-determinable. [MEM-RTE-example-correction](memory.md#mem-rte-example-correction), [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor).

Curation names transformations, not commands: digest and selected skill rendering reduce retained material; named section and full-page changes revise entries; dedup merges entries; deletion forgets canonical content while preserving recovery material; resolution reversion withdraws the annotation and retains its history. A model-authored synthesis page does not establish a novel claim absent from inputs. Bibliographic warnings do not establish universal withdrawal. Wrapper markdown does not establish the form or later model consumption of opaque downloaded payloads. [MEM-RTE-digest-authoring](memory.md#mem-rte-digest-authoring), [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission), [MEM-RTE-local-amendments](memory.md#mem-rte-local-amendments), [MEM-RTE-corpus-recovery](memory.md#mem-rte-corpus-recovery), [EPI-RTE-resolution-revert](epistemic.md#epi-rte-resolution-revert), [MEM-RTE-source-maintenance](memory.md#mem-rte-source-maintenance), [MEM-OBJ-artifact](memory.md#mem-obj-artifact).

Source-read log: none. Classification used only the supplied accepted reports and reconciliation; no frozen target source was opened and no new records or evidence were introduced.
