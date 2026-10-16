---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Synapptic memory comparison: transcript-derived profiles and narratives, evaluator feedback and context, and retained relay/browser state."
run-id: "AAS-2026-10-15-synapptic-9dce97c66546-01"
source-identity: "https://github.com/appcuarium/synapptic"
reviewed-boundary: "bcde026770daa5cd9a8ca18ca7182b0aeaa87d1f"
memory-comparison:
  version: 2
  scope: "Includes accumulated observation content/envelopes, weighted profile text/metadata/history, saved and published narratives, benchmark cases/results/reduced verdicts, opaque resumed evaluator context, original transcript read-back, relay request displays, transcript indexes and restored session bookkeeping, with their write, maintenance and later-consumer routes. Excludes static shipped patterns/skills/configuration as memory, ordinary transient current-call state, external host instruction admission/compaction and model weights/provider internals other than the included opaque resumed context."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Observations/envelopes, profiles/history, narratives/published copies, evaluator cases/results and original transcript files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-archetype"
                - "memory.md#mem-obj-benchmark-cases"
                - "memory.md#mem-obj-benchmark-results"
                - "memory.md#mem-rte-browser-readback"
              note: "Session JSON, YAML/history, Markdown, evaluator JSON and browser-readable JSONL are files."
          records:
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-observation-envelope"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-profile-metadata"
            - "memory.md#mem-obj-archetype"
            - "memory.md#mem-obj-benchmark-cases"
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-rte-browser-readback"
          note: "All these retained parts have recorded file-backed persistence; JSON/YAML/Markdown are encodings, not extra substrates."
        -
          scope: "Relay request displays, transcript index and session bookkeeping"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-obj-session-bookkeeping"
              note: "Request, index and session tables persist in SQLite."
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-bookkeeping"
              note: "Restart reconstructs retained session bookkeeping into Python tracker entries used for assignment."
          records:
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-obj-session-bookkeeping"
          note: "The records distinguish database retention from reconstructed operative tracker objects."
        -
          scope: "Claude evaluator condition-session retention"
          assessment: "known"
          findings:
            -
              value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-session"
              note: "Claude CLI resume addresses retained external conversation state."
          records:
            - "memory.md#mem-obj-claude-session"
          note: "The session is externally retained; the handle alone is not its substrate. Internal storage technology is not classified."
      records:
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-observation-envelope"
        - "memory.md#mem-obj-profile-observations"
        - "memory.md#mem-obj-profile-metadata"
        - "memory.md#mem-obj-archetype"
        - "memory.md#mem-obj-benchmark-cases"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-rte-browser-readback"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-obj-session-index"
        - "memory.md#mem-obj-session-bookkeeping"
        - "memory.md#mem-obj-claude-session"
      note: "The recorded inventory covers local files, relay SQLite and reconstructed tracker state, and the external resumed-session object. Service-object describes the external interface, not an assertion about its hidden physical medium."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Observation/profile/narrative wording and evaluator scenarios, responses and explanations"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-archetype"
                - "memory.md#mem-obj-benchmark-cases"
                - "memory.md#mem-obj-benchmark-results"
              note: "Claims, preferences, guards, scenarios and explanations are natural-language content."
          records:
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-archetype"
            - "memory.md#mem-obj-benchmark-cases"
            - "memory.md#mem-obj-benchmark-results"
          note: "These parts are interpreted as language by models or human readers."
        -
          scope: "Envelopes, eligibility fields, cache/result identifiers and labels, publication wrappers, relay metrics/index IDs and bookkeeping"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation-envelope"
                - "memory.md#mem-obj-profile-metadata"
                - "memory.md#mem-obj-archetype"
                - "memory.md#mem-obj-benchmark-cases"
                - "memory.md#mem-obj-benchmark-results"
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-obj-session-bookkeeping"
              note: "Fields and markers govern fixed routing, filtering, cache reuse, result reporting and session assignment."
          records:
            - "memory.md#mem-obj-observation-envelope"
            - "memory.md#mem-obj-profile-metadata"
            - "memory.md#mem-obj-archetype"
            - "memory.md#mem-obj-benchmark-cases"
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-obj-session-bookkeeping"
          note: "Fixed software consumers interpret these localized fields; numerical weights here are symbolic, not distributed-parametric state."
        -
          scope: "Relay message displays and indexed title/first-user snippets"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-rte-browser-readback"
              note: "Operators interpret message/response text and snippets."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-rte-browser-readback"
              note: "FTS and path/identity selection operate over localized index fields."
          records:
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-rte-browser-readback"
          note: "Readable text and fixed search/display structures have different consumption paths."
        -
          scope: "Consumed resumed Claude condition history, including possible checkpoint alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
          note: "The record establishes reuse but not the retained encoding or complete payload; neither text-only nor parametric checkpoint form follows."
      records:
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "memory.md#mem-obj-archetype"
        - "memory.md#mem-obj-benchmark-cases"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-obj-observation-envelope"
        - "memory.md#mem-obj-profile-metadata"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-obj-session-index"
        - "memory.md#mem-obj-session-bookkeeping"
        - "memory.md#mem-rte-browser-readback"
        - "memory.md#mem-obj-claude-session"
      note: "Text and fixed-rule fields are classified separately. The consumed provider-session payload is opaque, so visible responses cannot complete its form inventory."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Transcript-derived observation wording and profile/narrative derivation paths"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-ingest-profile"
              note: "Session conversation content feeds model extraction of observations and guards."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-archetype"
                - "runtime.md#rt-rte-publish-archetypes"
                - "epistemic.md#epi-rte-profile-curation"
              note: "Software merges observation wording and models generate saved narratives from filtered profiles."
          records:
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-archetype"
            - "runtime.md#rt-rte-ingest-profile"
            - "runtime.md#rt-rte-publish-archetypes"
          note: "The trace-extraction and subsequent compilation paths are known. Exact semantic provenance of generated diagnoses/rationales is not determined without instances."
        -
          scope: "Automatically generated benchmark scenarios"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-cases"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "A model authors scenarios admitted into caches."
          records:
            - "memory.md#mem-obj-benchmark-cases"
            - "runtime.md#rt-rte-benchmark-feedback"
          note: "These are authored hypothetical cases from guards, not imported real tasks."
        -
          scope: "Evaluator result records and reduced profile verdicts"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-results"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "Recorded evaluator responses and judgments feed retained results and feedback."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-metadata"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "Code aggregates labels into classifications and profile selectors."
          records:
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-obj-profile-metadata"
            - "runtime.md#rt-rte-benchmark-feedback"
          note: "Results derive from generated responses, model judgments and code classification; this does not establish external outcome warrant."
        -
          scope: "External JSONL and host-message acquisition, derived relay displays/index/bookkeeping"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-rte-browser-readback"
              note: "External host messages and JSONL supply retained content."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-obj-session-bookkeeping"
              note: "Display conversion, snippet extraction and event-derived grouping build retained local structures."
          records:
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-obj-session-bookkeeping"
            - "memory.md#mem-rte-browser-readback"
          note: "Acquired traces remain distinct from local derived access structures."
        -
          scope: "Opaque resumed evaluator context"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
          note: "Session handles identify a derivation interface, not complete retained-content provenance or any hidden summary production."
      records:
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "memory.md#mem-obj-archetype"
        - "runtime.md#rt-rte-ingest-profile"
        - "runtime.md#rt-rte-publish-archetypes"
        - "memory.md#mem-obj-benchmark-cases"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-obj-profile-metadata"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-obj-session-index"
        - "memory.md#mem-obj-session-bookkeeping"
        - "memory.md#mem-rte-browser-readback"
        - "memory.md#mem-obj-claude-session"
      note: "Recorded acquisition and transformation paths are classified without inferring the origin of opaque resumed context or every generated narrative proposition."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Observations, profiles and evaluation experience at durable update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
                - "runtime.md#rt-rte-ingest-profile"
                - "runtime.md#rt-rte-publish-archetypes"
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-profile-metadata"
              note: "Merge, synthesis and benchmark feedback use retained content/experience to update durable behavior-shaping artifacts."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-profile-curation"
              note: "Retained text similarity and weights determine matching and relative order."
          records:
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "runtime.md#rt-rte-ingest-profile"
            - "runtime.md#rt-rte-publish-archetypes"
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-profile-metadata"
          note: "Retained experience changes durable profiles, narratives and future eligibility; this is learning authority at update consumers, not demonstrated improvement."
        -
          scope: "Selected profile context at later extraction and saved descriptive narratives at evaluators"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-archetype"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "Existing observations and archetype descriptions supply model context."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-archetype"
            - "runtime.md#rt-rte-benchmark-feedback"
          note: "These consumers receive reference context. Preventive imperatives have a separately scoped instruction path."
        -
          scope: "Published imperative guards at external assistant"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-archetype"
                - "runtime.md#rt-bap-archetype-host"
              note: "Retained imperatives are delivered through host guidance/memory files, conditional on host loading."
          records:
            - "memory.md#mem-obj-archetype"
            - "runtime.md#rt-bap-archetype-host"
          note: "The documented host-loading route is afforded; loading, precedence and compliance are not observed."
        -
          scope: "Observation envelope and profile selectors at processed-selection, merge and synthesis"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observation-envelope"
                - "memory.md#mem-obj-profile-metadata"
                - "runtime.md#rt-rte-ingest-profile"
              note: "Session/project/dimension fields and source IDs choose work, scope and merge eligibility."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-metadata"
                - "runtime.md#rt-rte-ingest-profile"
              note: "Weights and ordering select extraction context."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-narrative-inputs"
              note: "Retained exclusions/verdicts and eligibility fields determine admissibility to narrative input."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-narrative-inputs"
              note: "The filter actually blocks excluded or model-ineligible entries from synthesis."
          records:
            - "memory.md#mem-obj-observation-envelope"
            - "memory.md#mem-obj-profile-metadata"
            - "epistemic.md#epi-rte-narrative-inputs"
            - "runtime.md#rt-rte-ingest-profile"
          note: "IDs select work/scope, weights/counts rank or filter, and exclusion/verdict fields veto source eligibility. Exclusions are not read by the extraction summary."
        -
          scope: "Benchmark cache identities and cached criteria at evaluator consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-cases"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "Cache identity/version selects reusable scenarios."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-cases"
                - "epistemic.md#epi-rte-benchmark-judgment"
              note: "Retained rules and criteria are applied by the judge as compliance criteria."
          records:
            - "memory.md#mem-obj-benchmark-cases"
            - "runtime.md#rt-rte-benchmark-feedback"
          note: "Cache fields choose reuse; retained rule/criteria content defines the model compliance check, without an independent factual oracle."
        -
          scope: "Detailed results, relay displays and transcript index at operator/UI and software consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-results"
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-rte-browser-readback"
              note: "Results and transcript displays inform operator inspection."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-rte-browser-readback"
              note: "Retained indexed title/first-user text supplies FTS search matching."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-obj-session-bookkeeping"
                - "memory.md#mem-rte-browser-readback"
              note: "Index identity/path and restored tracker fields choose transcript locations and session assignment."
          records:
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-obj-session-bookkeeping"
            - "memory.md#mem-rte-browser-readback"
          note: "Detailed results inform operators, not synthesis directly; only reduced profile verdicts reach eligibility filtering."
        -
          scope: "Opaque resumed condition history and incompletely inspected live UI consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-rte-browser-readback"
          note: "Later consumption exists, but the complete consumed payload/effects and live display paths are not recorded well enough to enumerate their authority."
      records:
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "runtime.md#rt-rte-ingest-profile"
        - "runtime.md#rt-rte-publish-archetypes"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-profile-metadata"
        - "memory.md#mem-obj-archetype"
        - "runtime.md#rt-bap-archetype-host"
        - "memory.md#mem-obj-observation-envelope"
        - "epistemic.md#epi-rte-narrative-inputs"
        - "memory.md#mem-obj-benchmark-cases"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-obj-session-index"
        - "memory.md#mem-obj-session-bookkeeping"
        - "memory.md#mem-rte-browser-readback"
        - "memory.md#mem-obj-claude-session"
      note: "Authority is assigned at actual consumers, separately from write agency. Opaque resumed payloads and uninspected live display paths prevent a complete inventory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Extraction, merge/promotion, synthesis/publication, evaluator cases/results/verdicts, relay capture/index/bookkeeping"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-observations"
                - "runtime.md#rt-rte-ingest-profile"
                - "runtime.md#rt-rte-publish-archetypes"
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-request-log"
                - "memory.md#mem-obj-session-index"
                - "memory.md#mem-obj-session-bookkeeping"
              note: "Software/model admission controls these writes."
          records:
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-observation-envelope"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-profile-metadata"
            - "memory.md#mem-obj-archetype"
            - "memory.md#mem-obj-benchmark-cases"
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-obj-session-index"
            - "memory.md#mem-obj-session-bookkeeping"
            - "runtime.md#rt-rte-ingest-profile"
            - "runtime.md#rt-rte-publish-archetypes"
            - "runtime.md#rt-rte-benchmark-feedback"
          note: "Humans start/install machinery; models/software admit this content without per-item human decisions."
        -
          scope: "Global exclusion confirmation, explicit re-inclusion and rollback replacement"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "epistemic.md#epi-rte-withdrawal-recovery"
                - "memory.md#mem-rte-state-maintenance"
              note: "Confirmation or explicit include/rollback commands decide the retained eligibility/content replacement."
          records:
            - "runtime.md#rt-rte-benchmark-feedback"
            - "epistemic.md#epi-rte-withdrawal-recovery"
            - "memory.md#mem-rte-state-maintenance"
          note: "Human decisions approve exclusion changes or request restoration of the previous global checkpoint; software performs selection/I/O."
        -
          scope: "Original external transcript production and provider-internal resumed-context/checkpoint admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-rte-browser-readback"
          note: "External logs are available and handles are chosen by code; the records do not establish per-content admission control for every original/hidden write."
      records:
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-observation-envelope"
        - "memory.md#mem-obj-profile-observations"
        - "memory.md#mem-obj-profile-metadata"
        - "memory.md#mem-obj-archetype"
        - "memory.md#mem-obj-benchmark-cases"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-obj-session-index"
        - "memory.md#mem-obj-session-bookkeeping"
        - "runtime.md#rt-rte-ingest-profile"
        - "runtime.md#rt-rte-publish-archetypes"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "epistemic.md#epi-rte-withdrawal-recovery"
        - "memory.md#mem-rte-state-maintenance"
        - "memory.md#mem-obj-claude-session"
        - "memory.md#mem-rte-browser-readback"
      note: "Known automatic admissions coexist with explicit human-controlled exclusions/replacement. Initial external transcript admission and hidden provider checkpoint writes are not resolved by a generic caller or a resume read."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Session facts extraction and weighted profile accumulation"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
              note: "Selected conversational traces become reduced standing observations."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-profile-curation"
                - "memory.md#mem-obj-profile-observations"
              note: "Similar entries merge into existing profile entries instead of remaining separate."
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-profile-curation"
                - "memory.md#mem-obj-profile-observations"
              note: "Longer matching wording can replace existing text."
            -
              value: "decay"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-profile-curation"
                - "memory.md#mem-obj-profile-metadata"
              note: "Per-merge/time decay downweights entries and pruning removes low-weight current entries."
            -
              value: "promote"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-profile-curation"
                - "memory.md#mem-obj-profile-metadata"
              note: "Cross-project grouping raises eligible entries to global scope."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "epistemic.md#epi-rte-profile-curation"
          note: "Extracting standing observations from retained messages consolidates them even though original logs survive. Similarity-based merges do not establish semantic agreement."
        -
          scope: "Benchmark exclusions and restored eligibility"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-withdrawal-recovery"
              note: "Global exclusions and model-specific negative verdicts withhold future synthesis use while keeping entry data."
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-withdrawal-recovery"
              note: "Later verdict writes or explicit re-inclusion revise retained eligibility metadata."
          records:
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-profile-metadata"
            - "epistemic.md#epi-rte-withdrawal-recovery"
          note: "Exclusion preserves entry/history while withdrawing later synthesis reliance. This does not withdraw saved/published prose."
        -
          scope: "Narrative generation, hidden condition-session maintenance and live-display transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archetype"
            - "runtime.md#rt-rte-publish-archetypes"
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-rte-browser-readback"
          note: "Narrative requests and indeterminate semantic relations do not establish novel claims; no generated artifact establishes synthesize. Hidden summaries/eviction and full live transformations are uninspected."
      records:
        - "runtime.md#rt-rte-ingest-profile"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "epistemic.md#epi-rte-profile-curation"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-profile-metadata"
        - "epistemic.md#epi-rte-withdrawal-recovery"
        - "memory.md#mem-obj-archetype"
        - "runtime.md#rt-rte-publish-archetypes"
        - "memory.md#mem-obj-claude-session"
        - "memory.md#mem-rte-browser-readback"
      note: "Implemented profile and eligibility transformations support six operations. Semantic novelty in model generation, opaque session maintenance and complete live-display transformations remain unresolved; no synthesize value is inferred from a command name."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested merge/synthesis/integration/results/history/browser retrieval"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "runtime.md#rt-rte-publish-archetypes"
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-benchmark-results"
                - "memory.md#mem-rte-state-maintenance"
                - "memory.md#mem-rte-browser-readback"
              note: "Shipped consumers request retained state by operation, project, session, model or query."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "runtime.md#rt-rte-publish-archetypes"
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-rte-state-maintenance"
            - "memory.md#mem-rte-browser-readback"
          note: "Drivers/operators request retained files, cases, snapshots or UI material. Fulfilling these requests is pull, not a second push merely because code delivers bytes."
        -
          scope: "Profile context automatically supplied at extraction and eligible profile/case treatment supplied to model calls"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "runtime.md#rt-rte-publish-archetypes"
                - "runtime.md#rt-rte-benchmark-feedback"
                - "epistemic.md#epi-rte-narrative-inputs"
              note: "Code supplies selected profile observations, filtered profile YAML, saved archetype treatment and cached cases in model prompts."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "runtime.md#rt-rte-publish-archetypes"
            - "runtime.md#rt-rte-benchmark-feedback"
            - "epistemic.md#epi-rte-narrative-inputs"
          note: "The extraction, synthesis and benchmark triggers cause code to select and attach retained context without a model retrieval request."
        -
          scope: "Published guidance at external host"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-archetype-host"
                - "memory.md#mem-obj-archetype"
              note: "Host instruction/memory-file channels can automatically supply published retained guidance."
          records:
            - "runtime.md#rt-bap-archetype-host"
            - "memory.md#mem-obj-archetype"
          note: "Static shipped instructions are excluded; these files contain accumulated generated memory. Host loading is documented/afforded, not observed."
        -
          scope: "Condition-session resume request and hidden payload selection; full live UI delivery"
          assessment: "partial"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claude-session"
              note: "Benchmark code requests retained external context through a session handle."
          records:
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-rte-browser-readback"
          note: "Code explicitly requests session reuse, establishing pull at the interface. Internal context selection/delivery and full live-update routes are not inspected."
      records:
        - "runtime.md#rt-rte-ingest-profile"
        - "runtime.md#rt-rte-publish-archetypes"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-rte-state-maintenance"
        - "memory.md#mem-rte-browser-readback"
        - "epistemic.md#epi-rte-narrative-inputs"
        - "runtime.md#rt-bap-archetype-host"
        - "memory.md#mem-obj-archetype"
        - "memory.md#mem-obj-claude-session"
      note: "Explicit requested returns and automatic model-context supply are separate operations. Hidden provider selection and incompletely inspected live UI paths retain local uncertainty."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Extraction and synthesis automatic context selection"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-narrative-inputs"
              note: "Availability, weight/count gates, per-dimension caps and exclusions select eligible profile content; no task-semantic lookup occurs."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-narrative-inputs"
              note: "An explicit target-model identity selects its retained model_verdicts entry to filter the delivered profile parts."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "memory.md#mem-obj-profile-metadata"
            - "epistemic.md#epi-rte-narrative-inputs"
          note: "Trigger: session extraction or synthesis. Inputs: global availability, weight/count/dimension order, exclusions and optional target-model name. Parts: profile observations and associated fields."
        -
          scope: "Benchmark model prompt treatment and cached case reuse"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-archetype"
              note: "WITH/WITHOUT mode selects the full saved narrative or a guard-adjusted treatment; lexical adjustment is classified separately."
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "epistemic.md#epi-rte-benchmark-judgment"
              note: "At per-guard benchmark setup, chosen guard text drives heuristic matching against the retained archetype to remove its matching block for WITHOUT, or append the guard for WITH when absent; this automatically selects narrative parts delivered to the respondent."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-benchmark-cases"
                - "runtime.md#rt-rte-benchmark-feedback"
              note: "Cache-key/version/hash matching selects retained cases supplied to the evaluator; batched keys omit guard/model freshness checks."
          records:
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-benchmark-cases"
            - "memory.md#mem-obj-archetype"
            - "epistemic.md#epi-rte-benchmark-judgment"
          note: "Trigger: explicit benchmark. Inputs: mode, project/model/seed/hash cache identity and chosen guard text. Parts: retained cases and saved narrative treatment, including lexical selection of matching archetype blocks in per-guard mode. Coarse treatment choice, lexical block selection and identifier-based case reuse are distinct operations."
        -
          scope: "External host loading of published generated guidance"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-archetype-host"
                - "memory.md#mem-obj-archetype"
              note: "Destination-wide guidance is afforded through memory references or always-apply/instruction conventions."
          records:
            - "runtime.md#rt-bap-archetype-host"
            - "memory.md#mem-obj-archetype"
          note: "Trigger: host instruction/memory loading. Inputs: destination/discovered project and output conventions. Parts: combined published narrative; current task content does not select passages."
        -
          scope: "Opaque resumed-session payload and uninspected live UI push selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-rte-browser-readback"
          note: "A requested resume identifier is not by itself a push selector. The actual hidden delivery operation and full live UI selection are not established."
      records:
        - "runtime.md#rt-rte-ingest-profile"
        - "memory.md#mem-obj-profile-metadata"
        - "epistemic.md#epi-rte-narrative-inputs"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-benchmark-cases"
        - "memory.md#mem-obj-archetype"
        - "runtime.md#rt-bap-archetype-host"
        - "memory.md#mem-obj-claude-session"
        - "memory.md#mem-rte-browser-readback"
        - "epistemic.md#epi-rte-benchmark-judgment"
      note: "Known push selectors include coarse eligibility/treatment, identifier matching and inferred-lexical matching of guard text to retained narrative blocks in per-guard benchmarks. Embedding or judgment retrieval is not established. Requested FTS/browser search is pull and does not add a push signal. Hidden provider and live UI alternatives remain unresolved."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Session conversation to observations, profiles and saved/published narrative"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
                - "memory.md#mem-obj-archetype"
                - "runtime.md#rt-rte-publish-archetypes"
              note: "Recorded session text automatically changes durable later-consumed behavior-shaping memory."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "memory.md#mem-obj-archetype"
            - "runtime.md#rt-rte-publish-archetypes"
          note: "Automatic trace-fed extraction produces durable artifacts reused by future extraction/synthesis and afforded host guidance. Hook maintenance alone omits external publication."
        -
          scope: "Benchmark execution feedback to durable profile eligibility"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-benchmark-feedback"
                - "memory.md#mem-obj-profile-metadata"
                - "epistemic.md#epi-rte-benchmark-disposition"
              note: "Recorded response/judgment experience automatically changes durable behavior-shaping selectors."
          records:
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-profile-metadata"
            - "epistemic.md#epi-rte-benchmark-disposition"
          note: "Automatic per-model verdicts change future explicit-target synthesis inputs; human global exclusions remain a separate mechanism."
        -
          scope: "Opaque evaluator context maintenance and complete relay/live UI alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-rte-browser-readback"
          note: "Resume establishes retained consumption, not any particular automatic derived checkpoint write. Relay storage/operator read-back is established but no qualifying profile-update route or bounded system-complete absence record is supplied."
      records:
        - "runtime.md#rt-rte-ingest-profile"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "memory.md#mem-obj-archetype"
        - "runtime.md#rt-rte-publish-archetypes"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-profile-metadata"
        - "epistemic.md#epi-rte-benchmark-disposition"
        - "memory.md#mem-obj-claude-session"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-rte-browser-readback"
      note: "Automatic session-derived durable updates and benchmark feedback qualify without observed benefit or parameter changes. Hidden resumed-session transformations and the complete observability write/consumer inventory are unresolved, not system-wide negatives."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Conversation-fed profile/narrative update chain"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-profile"
                - "memory.md#mem-obj-observations"
                - "memory.md#mem-obj-profile-observations"
                - "runtime.md#rt-rte-publish-archetypes"
              note: "Original input is recorded coding-session user and assistant turns."
          records:
            - "runtime.md#rt-rte-ingest-profile"
            - "memory.md#mem-obj-observations"
            - "memory.md#mem-obj-profile-observations"
            - "runtime.md#rt-rte-publish-archetypes"
          note: "Filtering keeps user/assistant conversational text and omits tool-use/results/thinking; no event-stream value is added for the SessionEnd trigger."
        -
          scope: "Synthetic evaluator feedback and opaque alternative qualifying writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-benchmark-feedback"
            - "memory.md#mem-obj-benchmark-results"
            - "memory.md#mem-obj-claude-session"
            - "memory.md#mem-obj-request-log"
            - "memory.md#mem-rte-browser-readback"
          note: "Benchmark scenarios/responses/judgments establish activity-fed updates, but records do not locate their original content unambiguously in a controlled trace-source class. Provider checkpoint inputs and any additional qualifying observability writes remain unresolved; neither tool-traces nor session-logs is inferred from an inference-call wrapper."
      records:
        - "runtime.md#rt-rte-ingest-profile"
        - "memory.md#mem-obj-observations"
        - "memory.md#mem-obj-profile-observations"
        - "runtime.md#rt-rte-publish-archetypes"
        - "runtime.md#rt-rte-benchmark-feedback"
        - "memory.md#mem-obj-benchmark-results"
        - "memory.md#mem-obj-claude-session"
        - "memory.md#mem-obj-request-log"
        - "memory.md#mem-rte-browser-readback"
      note: "Original content, not storage wrapper, determines trace origin. Session extraction is resolved; the precise controlled origin of synthetic evaluator experience and hidden session/relay alternatives is not completely recorded."
---

# Synapptic memory profile

## Comparison rationale

The comparison follows retained parts and actual consumers, not file formats or the enclosing model runtime. Profiles and narratives carry natural-language content; weights, IDs, exclusions and cache keys carry symbolic control. Relay tables and tracker state have operator/bookkeeping consumers, not an established instruction-learning path. The opaque resumed condition session remains included even where its form, origin and transformations cannot be classified. See [MEM-OBJ-claude-session](memory.md#mem-obj-claude-session), [MEM-OBJ-request-log](memory.md#mem-obj-request-log) and [MEM-OBJ-session-bookkeeping](memory.md#mem-obj-session-bookkeeping).

Reconciliation supersedes the epistemic profile-text, profile-fields, archetype and benchmark-case objects with their memory counterparts. The profile therefore cites [MEM-OBJ-profile-observations](memory.md#mem-obj-profile-observations), [MEM-OBJ-profile-metadata](memory.md#mem-obj-profile-metadata), [MEM-OBJ-archetype](memory.md#mem-obj-archetype) and [MEM-OBJ-benchmark-cases](memory.md#mem-obj-benchmark-cases), not the superseded objects. Returned-observation and evaluator-result containers remain valid but are not counted as additional stored parts merely because another member describes them.

Learning authority at merge/synthesis/feedback consumers differs from downstream knowledge or instruction authority. Automatic admission is not human approval merely because an operator starts ingest or installs a hook. Benchmark verdict writes precede the separate human exclusion decision. A human-requested global snapshot replacement is classified at its admission mechanism rather than inferred from a read of history. See [RT-RTE-ingest-profile](runtime.md#rt-rte-ingest-profile), [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback) and [MEM-RTE-state-maintenance](memory.md#mem-rte-state-maintenance).

Trace-fed extraction qualifies even without demonstrated improved performance. Extracting standing observations consolidates retained conversation; similarity merging, longer-text replacement, decay and cross-project promotion have separate implemented effects. Neither a command named synthesis nor a requested failure explanation establishes a novel claim. Narrative semantic novelty therefore stays unresolved rather than adding the curation value synthesize. The omitted separate evidence field also prevents interpreting the compiled profile as a guaranteed warrant-preserving representation. See [EPI-RTE-profile-curation](epistemic.md#epi-rte-profile-curation), [MEM-OBJ-profile-observations](memory.md#mem-obj-profile-observations) and [RT-RTE-publish-archetypes](runtime.md#rt-rte-publish-archetypes).

Pull and push can occur within one chain: a driver requests files, then automatically supplies selected retained content to a model. Browser FTS selection fulfills an operator request; it is not lexical push into an agent. Target-model identity matching actually selects the verdict field used by synthesis, whereas integration merely computes filtering counts before writing unchanged saved prose. This mapping does not claim model-specific publication filtering. Host loading is only afforded, so its push/instruction findings retain that basis rather than inheriting local writer wiring. See [MEM-RTE-browser-readback](memory.md#mem-rte-browser-readback), [EPI-RTE-narrative-inputs](epistemic.md#epi-rte-narrative-inputs), [RT-CLM-target-filtering](runtime.md#rt-clm-target-filtering) and [RT-BAP-archetype-host](runtime.md#rt-bap-archetype-host).

The benchmark also has a distinct lexical push selector: at per-guard setup, chosen guard text selects a matching block of the retained full archetype for removal from WITHOUT, or the guard is appended to WITH when absent. This controls which narrative parts the respondent receives without a respondent retrieval request. It supports inferred-lexical at wired basis, separately from coarse treatment choice and identifier-based cached-case reuse. Heuristic matching limits comparison fidelity; it does not erase the implemented selector. See [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback) and [EPI-RTE-benchmark-judgment](epistemic.md#epi-rte-benchmark-judgment).

The session conversation route supports session-logs as an original trace source. The SessionEnd event is a trigger, not evidence that event content feeds the qualifying write. Benchmark feedback qualifies as automatic activity-fed durable adaptation, but its synthetic inference responses and judgments do not unambiguously establish one controlled source class in the accepted records. The source axis retains that gap instead of treating every API result as tool-traces. No bounded absence record licenses a system-wide trace-learning no or an inapplicable trace-source axis. See [RT-RTE-session-hook](runtime.md#rt-rte-session-hook), [RT-RTE-benchmark-feedback](runtime.md#rt-rte-benchmark-feedback) and [MEM-OBJ-benchmark-results](memory.md#mem-obj-benchmark-results).

All positive findings are implementation wiring or explicitly afforded external consumption. No observed or causal basis is supplied. Partial assessments preserve missing facts about opaque context and incompletely inspected live UI paths; they do not turn those paths into absence. No source files were read for this classification: the supplied accepted records and reconciliation were sufficient, and no new quotes or records were added.
