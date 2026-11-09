---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "EXIA SEED memory comparison: conversational sources, derived subject pages, retrieval structures and shipped evaluation alternatives."
run-id: "AAS-2026-11-07-exia-seed-804e805b7a8d-01"
source-identity: "https://github.com/francisdu53/exia-seed"
reviewed-boundary: "c7497ac96da20bd1818096e35a59b6c0237f9730"
memory-comparison:
  version: 2
  scope: "Included: accumulated raw conversations, explicit/native notes, subject facts and parsed controls, summaries/keywords, thesaurus, graph, progress/provenance state, cross-invocation retrieval cache/priming and shipped replay/call-cache/answer consumers, including unresolved benchmark baseline/fusion alternatives and initial-content provenance. Excluded: static shipped instructions as memory, external provider weights/internals, host compaction/checkpoints and unfrozen deployment state. Generated EXIA SEED page outputs remain included even when their downstream host behavior is unobserved."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Durable raw batches, register, page prose/metadata, summaries, keywords, thesaurus, graph and audit/progress files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-registre"
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-thesaurus"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-obj-journals"
              note: "Markdown, YAML, JSON and JSONL are filesystem storage; graph encoding does not replace the files substrate."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-obj-journals"
          note: "Markdown, YAML, JSON and JSONL are filesystem storage; graph encoding does not replace the files substrate."
        -
          scope: "Memory history"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journals"
              note: "Best-effort Git retains page history; successful commits and recovery are unobserved."
          records:
            - "memory.md#mem-obj-journals"
          note: "Best-effort Git retains page history; successful commits and recovery are unobserved."
        -
          scope: "Cross-invocation Memoire cache and short-lived topic priming"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-memoire"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Python retrieval structures and priming live in process memory; the cache includes SQLite :memory: FTS."
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-cmp-memoire"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Python retrieval structures and priming live in process memory; the cache includes SQLite :memory: FTS."
          records:
            - "memory.md#mem-cmp-memoire"
            - "runtime.md#rt-rte-memory-delivery"
          note: "Python retrieval structures and priming live in process memory; the cache includes SQLite :memory: FTS."
        -
          scope: "Persisted benchmark model-call caches and generated memory/results"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
              note: "JSONL call caches and generated replay state survive relaunch."
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "JSONL call caches and generated replay state survive relaunch."
        -
          scope: "Additional benchmark baseline/fusion memory parts"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-registre"
        - "memory.md#mem-obj-page-facts"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-obj-graphe"
        - "memory.md#mem-obj-journals"
        - "memory.md#mem-cmp-memoire"
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Files, repository history and process-local structures are supported; unresolved benchmark alternatives prevent complete inventory coverage. External provider weights and host compaction are excluded, not treated as retained EXIA SEED objects."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Conversation and note text, page facts, summaries, graph proof snippets and audit prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-registre"
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-obj-journals"
              note: "Models or humans interpret the prose; graph evidence retains quoted/truncated prose separately from fixed-rule edge structure."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-obj-journals"
          note: "Models or humans interpret the prose; graph evidence retains quoted/truncated prose separately from fixed-rule edge structure."
        -
          scope: "Parsed identity/time/progress fields, page controls, keywords, thesaurus, graph weights, cache and topic activations"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-thesaurus"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-obj-journals"
                - "memory.md#mem-cmp-memoire"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Localized fields and fixed rules govern eligibility and retrieval; sparse numerical edge arrays are not distributed parameters."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-obj-journals"
            - "memory.md#mem-cmp-memoire"
            - "runtime.md#rt-rte-memory-delivery"
          note: "Localized fields and fixed rules govern eligibility and retrieval; sparse numerical edge arrays are not distributed parameters."
        -
          scope: "Benchmark cached answer prose and judgment/control fields"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
                - "epistemic.md#epi-obj-evaluations"
              note: "Cached text is interpreted by models; labels, votes and request keys have fixed consumers."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
                - "epistemic.md#epi-obj-evaluations"
              note: "Cached text is interpreted by models; labels, votes and request keys have fixed consumers."
          records:
            - "runtime.md#rt-rte-benchmark-replay"
            - "epistemic.md#epi-obj-evaluations"
          note: "Cached text is interpreted by models; labels, votes and request keys have fixed consumers."
        -
          scope: "Baseline embedding and remaining benchmark payload forms"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-registre"
        - "memory.md#mem-obj-page-facts"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-graphe"
        - "memory.md#mem-obj-journals"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-cmp-memoire"
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-rte-benchmark-replay"
        - "epistemic.md#epi-obj-evaluations"
      note: "Inspected memory mixes prose and symbolic controls. No parametric finding is inferred from numerical graph weights or from an uninspected embedding alternative."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Captured conversational source text and facts extracted from it"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-page-facts"
                - "runtime.md#rt-rte-conversation-ingest"
                - "runtime.md#rt-rte-page-consolidation"
              note: "Raw turns are captured with masking/formatting; derived facts originate in selected session lines."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-page-facts"
            - "runtime.md#rt-rte-conversation-ingest"
            - "runtime.md#rt-rte-page-consolidation"
          note: "Raw turns are captured with masking/formatting; derived facts originate in selected session lines."
        -
          scope: "Explicit note content and native-memory mirror"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-register-admission"
                - "memory.md#mem-obj-registre"
              note: "Explicit callers supply note content; the native callback imports supplied memory. This says nothing about human admission."
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-register-admission"
                - "memory.md#mem-obj-registre"
              note: "Explicit callers supply note content; the native callback imports supplied memory. This says nothing about human admission."
          records:
            - "runtime.md#rt-rte-register-admission"
            - "memory.md#mem-obj-registre"
          note: "Explicit callers supply note content; the native callback imports supplied memory. This says nothing about human admission."
        -
          scope: "Derived summaries, keyword controls, metadata, concept enrichment, graph and retrieval cache"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-thesaurus"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-cmp-memoire"
              note: "Model/code transformations compile existing pages and source controls into additional retained representations."
          records:
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-cmp-memoire"
          note: "Model/code transformations compile existing pages and source controls into additional retained representations."
        -
          scope: "Replay dataset sessions and generated call/result records"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
              note: "Preparation imports dataset sessions; caches record model request/response activity."
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
              note: "Preparation imports dataset sessions; caches record model request/response activity."
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Preparation imports dataset sessions; caches record model request/response activity."
        -
          scope: "Starting pages/thesaurus and arbitrary register content's upstream derivation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-page-facts"
          note: "Known subsequent transformations do not establish provenance of initial state or every note."
        -
          scope: "Uninspected benchmark baseline and fusion derivation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-page-facts"
        - "runtime.md#rt-rte-conversation-ingest"
        - "runtime.md#rt-rte-page-consolidation"
        - "runtime.md#rt-rte-register-admission"
        - "memory.md#mem-obj-registre"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-obj-graphe"
        - "memory.md#mem-cmp-memoire"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Known acquisition and compilation coexist with unresolved initialization and benchmark provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Page facts and identity summaries delivered to the foreground model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-summary"
                - "runtime.md#rt-bap-recalled-content"
              note: "Selected content supplies context/advice, not a truth guarantee."
          records:
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-summary"
            - "runtime.md#rt-bap-recalled-content"
          note: "Selected content supplies context/advice, not a truth guarantee."
        -
          scope: "Procedural conduct corrections delivered as later guidance"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-facts"
                - "runtime.md#rt-bap-recalled-content"
              note: "Retained rules can direct host behavior through model interpretation; compliance is not observed."
          records:
            - "memory.md#mem-obj-page-facts"
            - "runtime.md#rt-bap-recalled-content"
          note: "Retained rules can direct host behavior through model interpretation; compliance is not observed."
        -
          scope: "Raw session text at fact extraction and derived facts at summary/vocabulary updates"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-consolidation"
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-thesaurus"
              note: "Retained experience feeds durable behavior-shaping pages, summaries and retrieval inputs. Learning authority here does not assert improved capacity."
          records:
            - "runtime.md#rt-rte-page-consolidation"
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-thesaurus"
          note: "Retained experience feeds durable behavior-shaping pages, summaries and retrieval inputs. Learning authority here does not assert improved capacity."
        -
          scope: "Facts, aliases, concept fields, keywords, graph edges and recent activations at retrieval"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-thesaurus"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-cmp-memoire"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Retained content and symbolic features determine relative retrieval priority under fixed code."
          records:
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-cmp-memoire"
            - "runtime.md#rt-rte-memory-delivery"
          note: "Retained content and symbolic features determine relative retrieval priority under fixed code."
        -
          scope: "Progress/integration state and page identities at source/window/page selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journals"
                - "memory.md#mem-obj-registre"
                - "memory.md#mem-obj-page-metadata"
                - "runtime.md#rt-rte-page-consolidation"
              note: "Pending IDs and batch journals choose subsequent input windows; aliases resolve destinations."
          records:
            - "memory.md#mem-obj-journals"
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-page-metadata"
            - "runtime.md#rt-rte-page-consolidation"
          note: "Pending IDs and batch journals choose subsequent input windows; aliases resolve destinations."
        -
          scope: "Withdrawal IDs at consolidation and graph-reference consumers"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-journals"
                - "runtime.md#rt-rte-conversation-ingest"
                - "epistemic.md#epi-rte-withdrawal-read"
              note: "Retained withdrawals exclude selected raw lines/references. They do not erase already derived facts."
          records:
            - "memory.md#mem-obj-journals"
            - "runtime.md#rt-rte-conversation-ingest"
            - "epistemic.md#epi-rte-withdrawal-read"
          note: "Retained withdrawals exclude selected raw lines/references. They do not erase already derived facts."
        -
          scope: "Retained source text and node/alias/concept vocabulary at fact, summary and keyword gates"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-fragment-check"
                - "epistemic.md#epi-rte-summary-check"
                - "memory.md#mem-obj-thesaurus"
                - "runtime.md#rt-rte-state-maintenance"
              note: "Sources and vocabularies supply admissibility criteria; code vetoes lexical/known-concept failures. The force belongs to these consumed retained inputs, not every metadata field."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-fragment-check"
                - "epistemic.md#epi-rte-summary-check"
                - "memory.md#mem-obj-thesaurus"
                - "runtime.md#rt-rte-state-maintenance"
              note: "Sources and vocabularies supply admissibility criteria; code vetoes lexical/known-concept failures. The force belongs to these consumed retained inputs, not every metadata field."
          records:
            - "epistemic.md#epi-rte-fragment-check"
            - "epistemic.md#epi-rte-summary-check"
            - "memory.md#mem-obj-thesaurus"
            - "runtime.md#rt-rte-state-maintenance"
          note: "Sources and vocabularies supply admissibility criteria; code vetoes lexical/known-concept failures. The force belongs to these consumed retained inputs, not every metadata field."
        -
          scope: "Remaining benchmark alternatives' consequential consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "memory.md#mem-obj-page-facts"
        - "memory.md#mem-obj-summary"
        - "runtime.md#rt-bap-recalled-content"
        - "runtime.md#rt-rte-page-consolidation"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-graphe"
        - "memory.md#mem-cmp-memoire"
        - "runtime.md#rt-rte-memory-delivery"
        - "memory.md#mem-obj-journals"
        - "memory.md#mem-obj-registre"
        - "runtime.md#rt-rte-conversation-ingest"
        - "epistemic.md#epi-rte-withdrawal-read"
        - "epistemic.md#epi-rte-fragment-check"
        - "epistemic.md#epi-rte-summary-check"
        - "runtime.md#rt-rte-state-maintenance"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Authority is consumer-specific. Knowledge, instruction, update learning, ranking, routing and enforcing validation are distinct paths; unread audit prose and privacy labels receive no invented force."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Ordinary capture, fact admission, summaries/keywords, derived metadata/graph/cache and progress records"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-ingest"
                - "runtime.md#rt-rte-page-consolidation"
                - "runtime.md#rt-rte-state-maintenance"
                - "epistemic.md#epi-rte-summary-write"
                - "memory.md#mem-obj-graphe"
                - "memory.md#mem-obj-journals"
              note: "Software/model admission does not require per-content approval; enabling CLI write mode is not approval of each resulting phrase."
          records:
            - "runtime.md#rt-rte-conversation-ingest"
            - "runtime.md#rt-rte-page-consolidation"
            - "runtime.md#rt-rte-state-maintenance"
            - "epistemic.md#epi-rte-summary-write"
            - "memory.md#mem-obj-graphe"
            - "memory.md#mem-obj-journals"
          note: "Software/model admission does not require per-content approval; enabling CLI write mode is not approval of each resulting phrase."
        -
          scope: "Recognized human retention/withdrawal decisions"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-ingest"
                - "memory.md#mem-obj-raw"
              note: "User omission/retrospective withdrawal supplies an explicit per-content retention decision; code executes the decision."
          records:
            - "runtime.md#rt-rte-conversation-ingest"
            - "memory.md#mem-obj-raw"
          note: "User omission/retrospective withdrawal supplies an explicit per-content retention decision; code executes the decision."
        -
          scope: "Shipped replay construction and model-call cache admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-replay"
              note: "Starting a run does not make later session writes or cached responses human-approved."
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Starting a run does not make later session writes or cached responses human-approved."
        -
          scope: "Per-entry explicit-note/native mirror admission and pre-existing page/thesaurus supply"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-thesaurus"
            - "runtime.md#rt-rte-register-admission"
          note: "Generic caller identity does not resolve human versus computational admission; arbitrary starting state has no established approval history."
        -
          scope: "Other benchmark writers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "runtime.md#rt-rte-conversation-ingest"
        - "runtime.md#rt-rte-page-consolidation"
        - "runtime.md#rt-rte-state-maintenance"
        - "epistemic.md#epi-rte-summary-write"
        - "memory.md#mem-obj-graphe"
        - "memory.md#mem-obj-journals"
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-benchmark-replay"
        - "memory.md#mem-obj-registre"
        - "memory.md#mem-obj-thesaurus"
        - "runtime.md#rt-rte-register-admission"
      note: "Known automatic transformations and explicit human retention decisions do not resolve all initial-content or caller-controlled admissions."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Fact extraction from retained sessions and bounded identity summaries"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-consolidation"
                - "memory.md#mem-obj-page-facts"
                - "memory.md#mem-obj-summary"
                - "epistemic.md#epi-rte-summary-proposal"
              note: "The implemented route selects/compresses retained source claims. Indeterminate semantic fidelity and possible error do not by themselves establish synthesis."
          records:
            - "runtime.md#rt-rte-page-consolidation"
            - "memory.md#mem-obj-page-facts"
            - "memory.md#mem-obj-summary"
            - "epistemic.md#epi-rte-summary-proposal"
          note: "The implemented route selects/compresses retained source claims. Indeterminate semantic fidelity and possible error do not by themselves establish synthesis."
        -
          scope: "Normalized duplicate fact suppression"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-facts"
                - "epistemic.md#epi-obj-fragments"
              note: "Same-section normalized duplicates are omitted; this is not contradiction resolution."
          records:
            - "memory.md#mem-obj-page-facts"
            - "epistemic.md#epi-obj-fragments"
          note: "Same-section normalized duplicates are omitted; this is not contradiction resolution."
        -
          scope: "Summary and keyword replacement; concept/timestamp enrichment"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-summary-write"
                - "runtime.md#rt-rte-state-maintenance"
                - "memory.md#mem-obj-keywords"
              note: "Existing retained fields can be revised or augmented; failed proposals preserve predecessors."
          records:
            - "epistemic.md#epi-rte-summary-write"
            - "runtime.md#rt-rte-state-maintenance"
            - "memory.md#mem-obj-keywords"
          note: "Existing retained fields can be revised or augmented; failed proposals preserve predecessors."
        -
          scope: "Raw-source withdrawal and corresponding provenance-reference exclusion"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-conversation-ingest"
                - "epistemic.md#epi-rte-withdrawal-read"
              note: "Selected source lines cease to support later extraction/graph references while bytes/history remain. Already stored fact prose is not globally retracted."
          records:
            - "runtime.md#rt-rte-conversation-ingest"
            - "epistemic.md#epi-rte-withdrawal-read"
          note: "Selected source lines cease to support later extraction/graph references while bytes/history remain. Already stored fact prose is not globally retracted."
        -
          scope: "Semantic novelty of model proposals"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-page-consolidation"
            - "epistemic.md#epi-rte-summary-proposal"
          note: "No linked generated outputs settle synthesis versus faithful compression or error; no synthesize finding is asserted."
        -
          scope: "Remaining benchmark maintenance/fusion"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "runtime.md#rt-rte-page-consolidation"
        - "memory.md#mem-obj-page-facts"
        - "memory.md#mem-obj-summary"
        - "epistemic.md#epi-rte-summary-proposal"
        - "epistemic.md#epi-obj-fragments"
        - "epistemic.md#epi-rte-summary-write"
        - "runtime.md#rt-rte-state-maintenance"
        - "memory.md#mem-obj-keywords"
        - "runtime.md#rt-rte-conversation-ingest"
        - "epistemic.md#epi-rte-withdrawal-read"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Supported local transformations do not imply comprehensive truth maintenance. Graph rebuilds alone establish no curation value; temporal delivery filtering is not classified as durable forgetting."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Primary phase-2 automatic recall"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-delivery"
                - "runtime.md#rt-bap-recalled-content"
              note: "Query-triggered code automatically supplies selected retained facts/summaries without a foreground tool request; phase 1 computes but returns empty."
          records:
            - "runtime.md#rt-rte-memory-delivery"
            - "runtime.md#rt-bap-recalled-content"
          note: "Query-triggered code automatically supplies selected retained facts/summaries without a foreground tool request; phase 1 computes but returns empty."
        -
          scope: "Explicit search/page tools"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-delivery"
              note: "A consumer requests memory; ranking and delivery within that request are not an additional push."
          records:
            - "runtime.md#rt-rte-memory-delivery"
          note: "A consumer requests memory; ranking and delivery within that request are not an additional push."
        -
          scope: "Direct file-reading usage"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-memory-delivery"
                - "memory.md#mem-obj-page-facts"
              note: "Host/human file reading is an afforded usage surface, not demonstrated host tool wiring."
          records:
            - "runtime.md#rt-rte-memory-delivery"
            - "memory.md#mem-obj-page-facts"
          note: "Host/human file reading is an afforded usage surface, not demonstrated host tool wiring."
        -
          scope: "Consolidation/summary readers and shipped benchmark response/cache readers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-consolidation"
                - "epistemic.md#epi-rte-summary-proposal"
                - "runtime.md#rt-rte-benchmark-replay"
              note: "Explicit program requests load pending sources, page excerpts, generated contexts/all facts/transcripts or keyed cached responses."
          records:
            - "runtime.md#rt-rte-page-consolidation"
            - "epistemic.md#epi-rte-summary-proposal"
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Explicit program requests load pending sources, page excerpts, generated contexts/all facts/transcripts or keyed cached responses."
        -
          scope: "Additional benchmark baseline/fusion read paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "runtime.md#rt-rte-memory-delivery"
        - "runtime.md#rt-bap-recalled-content"
        - "memory.md#mem-obj-page-facts"
        - "runtime.md#rt-rte-page-consolidation"
        - "epistemic.md#epi-rte-summary-proposal"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Both automatic supply and explicit consumption exist; unknown benchmark alternatives prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Phase-2 automatic recall facts and selected-subject summaries"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-delivery"
                - "memory.md#mem-cmp-memoire"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-graphe"
              note: "Trigger: primary query/prefetch in phase 2. Inputs: query words, aliases, concept lexical fields, graph activation and recent priming. Selected parts: ranked page facts and summaries of selected subjects. Fixed lexical/graph inference, not embedding or model judgment; subject IDs and budgets alone do not establish identifier/coarse push."
          records:
            - "runtime.md#rt-rte-memory-delivery"
            - "memory.md#mem-cmp-memoire"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-graphe"
          note: "Trigger: primary query/prefetch in phase 2. Inputs: query words, aliases, concept lexical fields, graph activation and recent priming. Selected parts: ranked page facts and summaries of selected subjects. Fixed lexical/graph inference, not embedding or model judgment; subject IDs and budgets alone do not establish identifier/coarse push."
        -
          scope: "Explicit tools, file reads and requested auxiliary/benchmark loads"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-memory-delivery"
            - "runtime.md#rt-rte-page-consolidation"
            - "runtime.md#rt-rte-benchmark-replay"
          note: "These identified operations fulfill requests rather than independent pushes, so the push-selector axis does not classify their request arguments."
        -
          scope: "Unresolved benchmark delivery/selection alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Replay and answer modes are established, but baseline embeddings, full fusion/diagnostic details and the separate plugin copy are unresolved; no complete classification of these alternatives follows."
      records:
        - "runtime.md#rt-rte-memory-delivery"
        - "memory.md#mem-cmp-memoire"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-graphe"
        - "runtime.md#rt-rte-page-consolidation"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Known push uses lexical/graph selection; pull routes are locally inapplicable, not grounds for declaring the entire signal axis inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic conversation-to-page-to-later-host path"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-consolidation"
                - "memory.md#mem-obj-page-facts"
                - "runtime.md#rt-bap-recalled-content"
              note: "Retained session traces feed software-admitted durable facts/conduct rules delivered on later invocations. This meets the trace-fed-write definition without proving improved capacity."
          records:
            - "runtime.md#rt-rte-page-consolidation"
            - "memory.md#mem-obj-page-facts"
            - "runtime.md#rt-bap-recalled-content"
          note: "Retained session traces feed software-admitted durable facts/conduct rules delivered on later invocations. This meets the trace-fed-write definition without proving improved capacity."
        -
          scope: "Session-derived summary, keyword and retrieval-vocabulary updates"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-keywords"
                - "memory.md#mem-obj-thesaurus"
                - "memory.md#mem-obj-graphe"
                - "runtime.md#rt-rte-memory-delivery"
              note: "Derived session facts feed automatic retained summaries and selectors with later consumers; provider weights need not change."
          records:
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-keywords"
            - "memory.md#mem-obj-thesaurus"
            - "memory.md#mem-obj-graphe"
            - "runtime.md#rt-rte-memory-delivery"
          note: "Derived session facts feed automatic retained summaries and selectors with later consumers; provider weights need not change."
        -
          scope: "Arbitrary note provenance, starting state and uninspected benchmark update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-registre"
            - "memory.md#mem-obj-thesaurus"
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Not every note or baseline input is known to be a trace, and remaining update chains are unresolved. Raw audit retention alone supplies no qualifying positive or bounded negative."
      records:
        - "runtime.md#rt-rte-page-consolidation"
        - "memory.md#mem-obj-page-facts"
        - "runtime.md#rt-bap-recalled-content"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-keywords"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-obj-graphe"
        - "runtime.md#rt-rte-memory-delivery"
        - "memory.md#mem-obj-registre"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Supported wired yes routes coexist with unresolved alternatives. No evidenced-absence record supports a local no; no system-wide negative or demonstrated improvement is asserted."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Captured conversational turns feeding page facts and downstream summaries/selectors"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "runtime.md#rt-rte-page-consolidation"
                - "memory.md#mem-obj-summary"
                - "memory.md#mem-obj-thesaurus"
              note: "Original input is recorded user/assistant conversation, including spoken content substituted into a turn. Timestamps alone do not turn it into event-streams."
          records:
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-rte-page-consolidation"
            - "memory.md#mem-obj-summary"
            - "memory.md#mem-obj-thesaurus"
          note: "Original input is recorded user/assistant conversation, including spoken content substituted into a turn. Timestamps alone do not turn it into event-streams."
        -
          scope: "Explicit/native notes' original content and remaining benchmark update inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-registre"
            - "runtime.md#rt-rte-benchmark-replay"
          note: "Notes may have mixed/opaque origins; adapter names do not establish tool traces or event streams. Baseline update content is unresolved."
      records:
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-page-consolidation"
        - "memory.md#mem-obj-summary"
        - "memory.md#mem-obj-thesaurus"
        - "memory.md#mem-obj-registre"
        - "runtime.md#rt-rte-benchmark-replay"
      note: "Session logs support the known trace-fed chain; no recorded qualifying write establishes tool-traces, event-streams or trajectories as additional original inputs."
---

# EXIA SEED memory profile

## Comparison rationale

### Inventory and evidence strength

The comparison separates retained prose, fixed-parsed controls and retrieval structures. Files are the durable substrate of the graph; graph topology is its symbolic encoding. The SQLite FTS cache is process-local, not a durable database of independently acquired memories. External model components are consumers/producers, not evidence that EXIA SEED retains changing provider parameters ([MEM-CMP-memoire](memory.md#mem-cmp-memoire), [MEM-OBJ-graphe](memory.md#mem-obj-graphe), [RT-CMP-consolidation-model](runtime.md#rt-cmp-consolidation-model)).

All ten axes retain partial inventory coverage. This is not an inference from missing run traces: wired architectural values are classifiable. It follows from unresolved included starting-content/caller provenance and benchmark alternatives where relevant. The known replay modes do not classify opaque baseline embeddings or every fusion transformation. The units preserve these local limits instead of excluding alternatives to obtain complete coverage ([MEM-OBJ-thesaurus](memory.md#mem-obj-thesaurus), [MEM-OBJ-registre](memory.md#mem-obj-registre), [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay)). No observed or causal finding is inferred from implementation.

### Content, controls and update routes

Standing conduct corrections can be instructions at a later host model while ordinary facts and summaries supply knowledge. The same retained experience has learning authority at the automatic update consumer. Retrieval features have ranking authority under fixed code. Sources and vocabularies have validation/enforcement force at admission gates, whereas privacy labels and confidence claims do not thereby become authorization or truth controls ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content), [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata), [EPI-RTE-fragment-check](epistemic.md#epi-rte-fragment-check), [EPI-RTE-summary-check](epistemic.md#epi-rte-summary-check)).

Automatic fact extraction and summary compression establish consolidation as a transformation route, not semantic fidelity. Indeterminate output semantics do not establish synthesis, and a possible negation error does not redefine consolidation as synthesis. Summary replacement establishes evolution; normalized duplicate suppression establishes deduplication. Withdrawal invalidates raw-source eligibility and selected graph references, not all downstream knowledge. Page prose survives reference removal ([MEM-OBJ-page-facts](memory.md#mem-obj-page-facts), [EPI-RTE-summary-write](epistemic.md#epi-rte-summary-write), [EPI-RTE-withdrawal-read](epistemic.md#epi-rte-withdrawal-read)).

Explicit human retention commands differ from software-controlled admission of ordinary turns and model-produced phrases. Note/native caller identity and an arbitrary starting thesaurus do not establish per-content human control. A write-enabled maintenance invocation authorizes a mechanism, not each resulting phrase ([RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance)).

### Read-back and trace interpretation

Phase-2 prefetch is push because selection is automatic without a foreground memory-tool request. It is query-triggered lexical/graph inference; the subject identifier in the delivered pointer does not alone establish identifier-based push. Explicit search/read and requested page/source/cache loading are pull. Phase 1 returns no automatic content, without disabling explicit tools. Estimated budgets do not prove a universal final-context ceiling ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [MEM-CMP-memoire](memory.md#mem-cmp-memoire)).

Session traces automatically produce retained pages, summaries and retrieval inputs that affect later context. This supports wired trace-learning "yes" without claiming observed benefit, host compliance, weight training or exercised self-improvement. Original inputs support session-logs; ordinary timestamps, voice substitution or note serialization do not add an event-stream source. Unknown note origins remain separate from that known chain. Audit logs without an update reader are not additional qualifying learning routes; no accepted bounded absence record supports a trace-learning "no" ([MEM-OBJ-raw](memory.md#mem-obj-raw), [MEM-OBJ-journals](memory.md#mem-obj-journals), [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [MEM-OBJ-summary](memory.md#mem-obj-summary), [MEM-OBJ-thesaurus](memory.md#mem-obj-thesaurus), [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)).

### Supersessions and source-read log

Reconciliation supersedes EPI-OBJ-summaries with [MEM-OBJ-summary](memory.md#mem-obj-summary), and EPI-OBJ-keywords with [MEM-OBJ-keywords](memory.md#mem-obj-keywords). This profile cites those canonical objects. The fragment and concept containers remain valid alongside their differentiated memory parts; they create no extra values simply by overlapping.

No source files were read. Classification used only the supplied accepted members and reconciliation; no evidence or record was added.
