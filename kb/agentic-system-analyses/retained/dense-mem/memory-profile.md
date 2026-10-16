---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Dense-Mem memory comparison of retained evidence, semantic/access state, session checkpoints, maintenance, recovery and historical alternatives."
run-id: "AAS-2026-10-15-dense-mem-1a314bed9a5c-01"
source-identity: "https://github.com/markhuangai/dense-mem"
reviewed-boundary: "bd736450454e237f1ab6d138f4ae9755916d73f6"
memory-comparison:
  version: 2
  scope: "Included: accumulated PostgreSQL evidence/relationship/support/lifecycle state; search documents/vectors; raw session events and extraction/linking checkpoints; ontology records/receipts, community projections and conflict audit/recovery; terminal/recovery outcomes, optional feedback/diagnostics, historical Dream payload/display and evaluation mapping/checkpoint/trace artifacts. Included uncertainty: initial vocabulary and historical provenance, opaque payloads, detailed admission/selection and downstream consumer alternatives. Excluded: external model weights/training, static shipped prompts/configuration, transient provider working history, external host prompt assembly and unestablished persistence/installation of exported packs or drafted skills."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Persistent evidence, semantic/support/lifecycle state, search text, raw sessions, checkpoints, ontology/receipts and conflict audit parts"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-relationship-records"
                - "memory.md#mem-obj-search-documents"
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-obj-organization-receipt"
                - "memory.md#mem-obj-conflict-derivation"
              note: "These retained parts use PostgreSQL, including structured JSON. JSON and relationship edges do not imply a separate file or graph database."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-relationship-records"
            - "memory.md#mem-obj-search-documents"
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-obj-organization-receipt"
            - "memory.md#mem-obj-conflict-derivation"
          note: "The records identify PostgreSQL for these operative stores."
        - scope: "Retained dense search vectors and their contract metadata"
          assessment: "known"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-vectors"
              note: "PostgreSQL persists the vectors and symbolic contract metadata."
            - value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-vectors"
              note: "The retained embeddings form the numerical vector-search access surface consumed by candidate retrieval."
          records:
            - "memory.md#mem-obj-search-vectors"
          note: "Vector access and relational persistence coexist; this does not classify external provider weights as use-accumulated memory."
        - scope: "Evaluation mappings, checkpoints and saved traces/scores in run artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-evaluation-suite"
              note: "Saved traces/mapping and run directories are retained and can be loaded for later scoring or resume."
          records:
            - "runtime.md#rt-rte-evaluation-suite"
          note: "The shipped runner establishes file-artifact retention/reload, not observed artifact creation."
        - scope: "Optional feedback, assessment diagnostics, other recovery ledgers, community state and historical Dream payloads"
          assessment: "partial"
          findings:
            - value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-recording"
              note: "The optional event repository persists feedback/snapshots in PostgreSQL."
          records:
            - "memory.md#mem-rte-feedback-recording"
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-rte-derived-projections"
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-conflict-review"
          note: "Feedback persistence is identified, but the accepted records do not locate every included historical, diagnostic and recovery part precisely enough for complete substrate enumeration. A service/repository interface alone does not locate storage."
      records:
        - "memory.md#mem-obj-evidence-fragments"
        - "memory.md#mem-obj-relationship-records"
        - "memory.md#mem-obj-search-documents"
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-obj-organization-receipt"
        - "memory.md#mem-obj-conflict-derivation"
        - "memory.md#mem-obj-search-vectors"
        - "runtime.md#rt-rte-evaluation-suite"
        - "memory.md#mem-rte-feedback-recording"
        - "memory.md#mem-rte-administrative-views"
        - "memory.md#mem-rte-derived-projections"
        - "runtime.md#rt-rte-remember-intake"
        - "runtime.md#rt-rte-conflict-review"
      note: "The inventory includes primary memory, access structures, recovery/provenance, optional feedback, evaluation and historical state. Named storage gaps prevent a complete substrate union; external model parameters and ordinary process-local working conversations are excluded."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Evidence text, relationship quotes/text values, search-document prose, raw session text, checkpoint prose, ontology definitions, receipt reasons and fixed conflict audit statement"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-relationship-records"
                - "memory.md#mem-obj-search-documents"
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-obj-organization-receipt"
                - "memory.md#mem-obj-conflict-derivation"
              note: "Models or readers interpret these textual parts; readable JSON wrappers do not change their form."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-relationship-records"
            - "memory.md#mem-obj-search-documents"
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-obj-organization-receipt"
            - "memory.md#mem-obj-conflict-derivation"
          note: "Text parts are separated from code-interpreted references and numerical vectors."
        - scope: "Identity, ownership, lifecycle/support/temporal controls; checkpoint references; ontology assignments/groups/dependencies; receipts and recovery/measurement references"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-relationship-records"
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-obj-organization-receipt"
                - "memory.md#mem-obj-conflict-derivation"
                - "runtime.md#rt-rte-evaluation-suite"
                - "memory.md#mem-rte-feedback-recording"
              note: "Code applies localized identifiers, statuses, versions, references, outcomes and completion state through fixed rules."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-relationship-records"
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-obj-organization-receipt"
            - "memory.md#mem-obj-conflict-derivation"
            - "runtime.md#rt-rte-evaluation-suite"
            - "memory.md#mem-rte-feedback-recording"
          note: "This unit covers the explicitly described fixed-rule parts, not opaque payloads behind their references."
        - scope: "Retained dense embeddings at later vector retrieval"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-vectors"
              note: "Dense numerical encoding distributes representation across vector components. This value concerns retained embeddings, not an assertion of updated provider weights."
          records:
            - "memory.md#mem-obj-search-vectors"
          note: "Contract IDs/dimensions belong to the separate symbolic unit."
        - scope: "Historical Dream display statement/rationale"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-rte-administrative-views"
              note: "Administrative readers receive natural-language historical statements and rationales."
          records:
            - "memory.md#mem-rte-administrative-views"
          note: "The inspected display identifies these parts only."
        - scope: "Historical Dream raw payload, full diagnostics and exact saved evaluation-trace bodies"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "runtime.md#rt-rte-evaluation-suite"
            - "runtime.md#rt-rte-remember-intake"
          note: "Payload schemas and full diagnostic content/consumption remain uninspected. The display summary does not resolve the raw payload form."
      records:
        - "memory.md#mem-obj-evidence-fragments"
        - "memory.md#mem-obj-relationship-records"
        - "memory.md#mem-obj-search-documents"
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-obj-organization-receipt"
        - "memory.md#mem-obj-conflict-derivation"
        - "runtime.md#rt-rte-evaluation-suite"
        - "memory.md#mem-rte-feedback-recording"
        - "memory.md#mem-obj-search-vectors"
        - "memory.md#mem-rte-administrative-views"
        - "runtime.md#rt-rte-remember-intake"
      note: "All three forms have local implementation witnesses. Opaque historical payload and incompletely described diagnostic/evaluation bodies prevent complete coverage."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller evidence and raw session text entering retention"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-session-events"
              note: "External caller text is acquired; attributed source/framework labels do not authenticate its earlier origin."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-session-events"
          note: "Known admission/import path does not resolve pre-import authorship or trace origin."
        - scope: "Session extraction/linking checkpoints and downstream semantic artifacts"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-session-intake"
              note: "Software/model extraction and linking transform staged text into retained proposals and semantic state."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-session-intake"
                - "memory.md#mem-obj-session-events"
              note: "When supplied text is an interaction trace, the same wired path extracts durable material from that trace; this does not label arbitrary session text as a trace."
          records:
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-session-intake"
            - "memory.md#mem-obj-session-events"
          note: "The derivation path is inspected, but actual supplied event origin is mixed or opaque. Trace-extracted is conditional on input content, not authenticated origin of all entries."
        - scope: "Search projections/vectors, automatic ontology/community organization and fixed conflict audit derivation"
          assessment: "partial"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-documents"
                - "memory.md#mem-obj-search-vectors"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-rte-derived-projections"
                - "memory.md#mem-obj-conflict-derivation"
              note: "These are generated projections, numerical encodings, organization or fixed audit outputs from retained source state."
          records:
            - "memory.md#mem-obj-search-documents"
            - "memory.md#mem-obj-search-vectors"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-rte-derived-projections"
            - "memory.md#mem-obj-conflict-derivation"
          note: "The recorded downstream derivation is known; inherited source warrant and external embedding-provider training provenance remain unresolved."
        - scope: "Explicit caller correction content and manager-supplied ontology edits"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-lifecycle-changes"
                - "runtime.md#rt-rte-manager-publication"
              note: "Callers supply deliberate patches/edits and publication choices, rather than those edits being solely extracted by the automatic organizer. Authored does not mean human-authored."
          records:
            - "memory.md#mem-rte-lifecycle-changes"
            - "runtime.md#rt-rte-manager-publication"
          note: "Explicit editing lineage is supported independently of actor humanity."
        - scope: "Historical Dream payload initialization, initial vocabulary seeding and complete diagnostic/evaluation artifact provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "runtime.md#rt-rte-ontology-maintenance"
            - "runtime.md#rt-rte-evaluation-suite"
            - "runtime.md#rt-rte-remember-intake"
          note: "Initial historical/vocabulary provenance and complete evaluation import/diagnostic derivation are not inspected; no authorship or trace lineage is inferred from names."
      records:
        - "memory.md#mem-obj-evidence-fragments"
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "runtime.md#rt-rte-session-intake"
        - "memory.md#mem-obj-search-documents"
        - "memory.md#mem-obj-search-vectors"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-rte-derived-projections"
        - "memory.md#mem-obj-conflict-derivation"
        - "memory.md#mem-rte-lifecycle-changes"
        - "runtime.md#rt-rte-manager-publication"
        - "memory.md#mem-rte-administrative-views"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "runtime.md#rt-rte-evaluation-suite"
        - "runtime.md#rt-rte-remember-intake"
      note: "Import, explicit editing and compiled derivation coexist. Conditional trace extraction is preserved without upgrading opaque event origin or external provider provenance."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Eligible evidence, relationship text and historical/feedback/trace displays at interpreting readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-relationship-records"
                - "memory.md#mem-rte-administrative-views"
                - "memory.md#mem-rte-feedback-recording"
                - "memory.md#mem-rte-trace-export"
              note: "Returned content and lineage supply reference/context to clients or administrative readers; delivery is not compliance or factual endorsement."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-relationship-records"
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-rte-feedback-recording"
            - "memory.md#mem-rte-trace-export"
          note: "This classifies the delivered reference parts, not uninspected opaque payload effects or full fragment delivery."
        - scope: "Search text, vectors and ontology name/lexical inputs at retrieval"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-documents"
                - "memory.md#mem-obj-search-vectors"
                - "memory.md#mem-obj-ontology-records"
                - "runtime.md#rt-rte-recall-context"
              note: "Retained text and dense features affect candidate scores/fusion; definition/name matches influence discovery selection."
          records:
            - "memory.md#mem-obj-search-documents"
            - "memory.md#mem-obj-search-vectors"
            - "memory.md#mem-obj-ontology-records"
            - "runtime.md#rt-rte-recall-context"
          note: "Ranking authority needs no retained scoring policy and does not imply learned retrieval parameters."
        - scope: "Retained IDs, scope/generation, lifecycle/support state and current ontology controls at service admission/selection"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-fragments"
                - "memory.md#mem-obj-relationship-records"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-rte-private-erasure"
              note: "Eligibility, lifecycle, current-state and generation controls can exclude delivery or writes."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-remember-intake"
                - "memory.md#mem-rte-private-erasure"
              note: "Reloaded checkpoints are decoded/revalidated, durable request identity constrains replay/admission, and generation/fence state constrains erasure completion."
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-relationship-records"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-rte-private-erasure"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-remember-intake"
          note: "Only the recorded criteria actually consumed by software are classified. Ordinary evidence need not have a qualifying relationship; no universal final support gate is asserted."
        - scope: "Session events/checkpoints, durable Remember outcomes, ontology dependencies and evaluation mappings at later progression"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-remember-intake"
                - "memory.md#mem-obj-ontology-records"
                - "runtime.md#rt-rte-evaluation-suite"
              note: "Prior-event identity/budgets select extraction context; cached extraction/linking and terminal attempts select resume/replay; retained organization and evaluation completion mappings select later work."
          records:
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-remember-intake"
            - "memory.md#mem-obj-ontology-records"
            - "runtime.md#rt-rte-evaluation-suite"
          note: "Fixed control effects are distinct from semantic interpretation of the same retained objects."
        - scope: "Trace-bearing raw session content at automatic extraction and linking"
          assessment: "partial"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-session-intake"
              note: "When retained event content is a trace, the extractor consumes it to produce durable semantic/context artifacts that reach later intake/recall."
          records:
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-session-intake"
          note: "This conditional update-consumer force is distinct from downstream knowledge authority and does not establish improved capacity. Actual input origin is unresolved."
        - scope: "Ontology definition prose at the later organizer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-bap-organization-selection"
              note: "The organizer interprets definitions as source/organization context, not as newly submitted evidence or standing instructions."
          records:
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-bap-organization-selection"
          note: "Manager overrides have separate fixed control force; definition prose alone is not instruction authority."
        - scope: "Opaque historical payload consumers, full diagnostic/review reasons and possible later exported-skill adoption"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-obj-organization-receipt"
            - "runtime.md#rt-rte-conflict-review"
            - "runtime.md#rt-rte-skill-export"
          note: "Display/reference and receipt-reuse paths do not establish all payload or rationale consumers. Skill drafting has no established retained installation. Shipped prompts are excluded from accumulated-memory authority."
      records:
        - "memory.md#mem-obj-evidence-fragments"
        - "memory.md#mem-obj-relationship-records"
        - "memory.md#mem-rte-administrative-views"
        - "memory.md#mem-rte-feedback-recording"
        - "memory.md#mem-rte-trace-export"
        - "memory.md#mem-obj-search-documents"
        - "memory.md#mem-obj-search-vectors"
        - "memory.md#mem-obj-ontology-records"
        - "runtime.md#rt-rte-recall-context"
        - "memory.md#mem-rte-private-erasure"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "runtime.md#rt-rte-remember-intake"
        - "memory.md#mem-obj-session-events"
        - "runtime.md#rt-rte-evaluation-suite"
        - "runtime.md#rt-rte-session-intake"
        - "memory.md#mem-bap-organization-selection"
        - "memory.md#mem-obj-organization-receipt"
        - "runtime.md#rt-rte-conflict-review"
        - "runtime.md#rt-rte-skill-export"
      note: "Knowledge, ranking, enforcement, validation, routing and conditional learning have local consumer warrants. No instruction value is inferred merely from preferences in recalled text or the static export prompt; unresolved consumers prevent a complete authority classification."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Remember semantic admission, session staging/extraction/checkpoint/semantic commits, automatic ontology and conflict review"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-remember-intake"
                - "runtime.md#rt-rte-session-intake"
                - "runtime.md#rt-rte-ontology-maintenance"
                - "runtime.md#rt-rte-conflict-review"
              note: "Application/model/repository admission proceeds without a required per-content human decision. Starting the workflow does not make these later writes manual."
          records:
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-session-intake"
            - "runtime.md#rt-rte-ontology-maintenance"
            - "runtime.md#rt-rte-conflict-review"
          note: "This classifies inspected software admission, not humanity of whoever supplied initial content."
        - scope: "Search/community projection maintenance, optional snapshot recording and policy-triggered retention/erasure"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-derived-projections"
                - "memory.md#mem-rte-feedback-recording"
                - "memory.md#mem-rte-private-erasure"
              note: "Workers/configured software create projections/snapshots or execute policy-triggered retention without per-item operator approval."
          records:
            - "memory.md#mem-rte-derived-projections"
            - "memory.md#mem-rte-feedback-recording"
            - "memory.md#mem-rte-private-erasure"
          note: "Caller-triggered erasure and volunteered feedback have distinct unresolved operator-control paths below."
        - scope: "Explicit initial evidence supply, lifecycle patches/confirmations, manager edits/publication, voluntary feedback and caller erasure decisions"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-remember-intake"
            - "memory.md#mem-rte-lifecycle-changes"
            - "runtime.md#rt-rte-manager-publication"
            - "memory.md#mem-rte-feedback-recording"
            - "memory.md#mem-rte-private-erasure"
          note: "Generic caller/owner/manager identity does not establish a human decision. Per-content control at these caller decisions cannot be classified manual or automatic merely from role names."
        - scope: "Historical Dream initialization, initial ontology vocabulary, full evaluation import/admission and diagnostic persistence controls"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "runtime.md#rt-rte-ontology-maintenance"
            - "runtime.md#rt-rte-evaluation-suite"
            - "runtime.md#rt-rte-remember-intake"
          note: "The reports leave these admission mechanisms or initial control uninspected. Known later transformations do not resolve them."
      records:
        - "runtime.md#rt-rte-remember-intake"
        - "runtime.md#rt-rte-session-intake"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "runtime.md#rt-rte-conflict-review"
        - "memory.md#mem-rte-derived-projections"
        - "memory.md#mem-rte-feedback-recording"
        - "memory.md#mem-rte-private-erasure"
        - "memory.md#mem-rte-lifecycle-changes"
        - "runtime.md#rt-rte-manager-publication"
        - "memory.md#mem-rte-administrative-views"
        - "runtime.md#rt-rte-evaluation-suite"
      note: "Automatic admission has several inspected witnesses. Manual requires explicit human content control, absent from the available positive evidence; that is not a bounded claim that manual control never occurs."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Session extraction of durable entity/relationship facts from retained messages"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-session-intake"
              note: "Window extraction reduces retained message content into cited fact/proposal representations, even while raw messages remain."
          records:
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-session-intake"
          note: "The implemented transformation is consolidation. Unknown semantic faithfulness and opaque input origin do not turn its requested extraction into synthesis."
        - scope: "Lifecycle correction and ontology revision/publication"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-lifecycle-changes"
                - "runtime.md#rt-rte-manager-publication"
                - "memory.md#mem-obj-ontology-records"
              note: "Existing semantic or organization entries receive successor/revised content under explicit editing/publication routes."
          records:
            - "memory.md#mem-rte-lifecycle-changes"
            - "runtime.md#rt-rte-manager-publication"
            - "memory.md#mem-obj-ontology-records"
          note: "Wiring supports revisions, not universally correct corrections or complete rollback."
        - scope: "Retraction, one-cardinality replacement, lifecycle supersession and conflict withdrawal"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-lifecycle-changes"
                - "memory.md#mem-obj-relationship-records"
                - "runtime.md#rt-rte-conflict-review"
                - "memory.md#mem-obj-conflict-derivation"
              note: "Current reliance/eligibility is withdrawn while support, transition or audit history remains."
          records:
            - "memory.md#mem-rte-lifecycle-changes"
            - "memory.md#mem-obj-relationship-records"
            - "runtime.md#rt-rte-conflict-review"
            - "memory.md#mem-obj-conflict-derivation"
          note: "The deletion-only conflict artifact is audit state, not new support."
        - scope: "Private retention erasure and feedback age-based pruning"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-private-erasure"
                - "memory.md#mem-rte-feedback-recording"
              note: "Retention-triggered physical deletion and age-based event pruning forget retained content. Logical retraction is classified separately as invalidation."
          records:
            - "memory.md#mem-rte-private-erasure"
            - "memory.md#mem-rte-feedback-recording"
          note: "Policy-triggered forgetting is wired; no executed erasure or external-copy deletion is inferred."
        - scope: "Duplicate canonicalization, automatic equivalence organization, historical Dream and uninspected semantic transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-evidence-fragments"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-rte-administrative-views"
            - "runtime.md#rt-rte-remember-intake"
          note: "Detailed duplicate mutation helpers and historical transformations are uninspected. Equivalence grouping/result filtering and index rebuilds alone do not establish retained deduplication; no actual new claim establishes synthesis. Unresolved operations prevent complete enumeration."
      records:
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "runtime.md#rt-rte-session-intake"
        - "memory.md#mem-rte-lifecycle-changes"
        - "runtime.md#rt-rte-manager-publication"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-obj-relationship-records"
        - "runtime.md#rt-rte-conflict-review"
        - "memory.md#mem-obj-conflict-derivation"
        - "memory.md#mem-rte-private-erasure"
        - "memory.md#mem-rte-feedback-recording"
        - "memory.md#mem-obj-evidence-fragments"
        - "memory.md#mem-rte-administrative-views"
        - "runtime.md#rt-rte-remember-intake"
      note: "Consolidate, evolve, invalidate and decay follow implemented transformations, not command names. No promote, dedup or synthesize value is inferred from acquisition, projection repair, output filtering or requested model semantics alone."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Caller-requested recall, handle trace/export, administrative/feedback readers and explicit replay/scoring loads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-recall-context"
                - "memory.md#mem-rte-trace-export"
                - "memory.md#mem-rte-administrative-views"
                - "memory.md#mem-rte-feedback-recording"
                - "runtime.md#rt-rte-remember-intake"
                - "runtime.md#rt-rte-evaluation-suite"
              note: "These operations fulfill a caller or evaluator request for retained material, including recovery output. Automatic ranking within requested recall is not a separate unsolicited push."
          records:
            - "runtime.md#rt-rte-recall-context"
            - "memory.md#mem-rte-trace-export"
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-rte-feedback-recording"
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-evaluation-suite"
          note: "Concrete request/return and later-consumer routes are recorded; external host answer use is not required for this route classification."
        - scope: "Automatic prior-session selection into a new extraction frame"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "runtime.md#rt-rte-session-intake"
              note: "New intake triggers automatic selection of retained prior same-session events into the extractor without a request by that extractor for those events."
          records:
            - "memory.md#mem-obj-session-events"
            - "runtime.md#rt-rte-session-intake"
          note: "The caller initiates intake, but software independently supplies prior context to the model under count/token bounds."
        - scope: "Automatic organization source/vocabulary context and projection/conflict worker inputs"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ontology-maintenance"
                - "memory.md#mem-obj-ontology-records"
                - "memory.md#mem-rte-derived-projections"
                - "runtime.md#rt-rte-conflict-review"
              note: "Scheduled/claimed work and server context builders supply selected retained sources, vocabulary or dossier inputs to the next worker/model consumer."
          records:
            - "runtime.md#rt-rte-ontology-maintenance"
            - "memory.md#mem-obj-ontology-records"
            - "memory.md#mem-rte-derived-projections"
            - "runtime.md#rt-rte-conflict-review"
          note: "Automatic worker/model supply is within the memory boundary even though no unsolicited host conversation injection is established."
        - scope: "Opaque historical payload reuse, full diagnostic readers and all alternative recovery consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-obj-organization-receipt"
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-conflict-review"
          note: "Known displays/replay do not establish every later opaque payload or diagnostic consumer; complete alternative-route coverage is unavailable."
      records:
        - "runtime.md#rt-rte-recall-context"
        - "memory.md#mem-rte-trace-export"
        - "memory.md#mem-rte-administrative-views"
        - "memory.md#mem-rte-feedback-recording"
        - "runtime.md#rt-rte-remember-intake"
        - "runtime.md#rt-rte-evaluation-suite"
        - "memory.md#mem-obj-session-events"
        - "runtime.md#rt-rte-session-intake"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-rte-derived-projections"
        - "runtime.md#rt-rte-conflict-review"
        - "memory.md#mem-obj-organization-receipt"
      note: "Pull requests and automatic push-to-internal-consumer operations coexist. A request for recall is not counted as push merely because the service selects results; upstream intake initiation does not erase independent prior-context selection."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Prior-session events automatically supplied at new extraction"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "runtime.md#rt-rte-session-intake"
              note: "Trigger: new session intake. Selector: same session identity/completed-event match. Selected part: matching retained prior events."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "runtime.md#rt-rte-session-intake"
              note: "Within matching prior events, newest-first availability and ten-event/2048-token bounds select the delivered context."
          records:
            - "memory.md#mem-obj-session-events"
            - "runtime.md#rt-rte-session-intake"
          note: "Identity targeting and coarse recency/budget selection are separate operations in one push chain."
        - scope: "Ontology context supplied to later organization"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ontology-maintenance"
                - "memory.md#mem-obj-ontology-records"
              note: "Trigger: organization work. Selector: source dependencies/current assignments/overrides and exact definition references. Selected parts: source-linked records and forced vocabulary definitions."
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ontology-maintenance"
                - "memory.md#mem-obj-ontology-records"
              note: "The context builder also supplies vocabulary candidates selected by lexical/name correspondence to the source items."
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ontology-maintenance"
                - "memory.md#mem-obj-ontology-records"
              note: "Vocabulary/input bounds limit the retained source and definition material supplied to the organizer."
          records:
            - "runtime.md#rt-rte-ontology-maintenance"
            - "memory.md#mem-obj-ontology-records"
          note: "These inputs select delivered retained parts, not merely catalog IDs. No inferred-embedding or inferred-judgment push value is inferred from requested recall ranking."
        - scope: "Search/community maintenance and conflict-review automatic inputs"
          assessment: "partial"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-derived-projections"
                - "runtime.md#rt-rte-conflict-review"
              note: "Worker trigger, available/overdue/claimed work and bounded batches select retained projection sources or conflict dossiers."
          records:
            - "memory.md#mem-rte-derived-projections"
            - "runtime.md#rt-rte-conflict-review"
          note: "The recorded selectors establish coarse policy/work availability. Detailed repository selection and all dossier composition predicates remain uninspected."
        - scope: "Requested recall, trace/export, administrative readers and explicit replay/scoring loads"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-recall-context"
            - "memory.md#mem-rte-trace-export"
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-rte-feedback-recording"
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-evaluation-suite"
          note: "These are pull operations. Query vectors or requested relationship/file IDs do not establish a push signal."
        - scope: "Other historical/diagnostic/recovery alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-administrative-views"
            - "memory.md#mem-obj-organization-receipt"
            - "runtime.md#rt-rte-remember-intake"
            - "runtime.md#rt-rte-conflict-review"
          note: "Insufficient consumer/selection coverage to decide whether additional push selectors operate. Known pull routes cannot make this unresolved branch inapplicable."
      records:
        - "memory.md#mem-obj-session-events"
        - "runtime.md#rt-rte-session-intake"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "memory.md#mem-obj-ontology-records"
        - "memory.md#mem-rte-derived-projections"
        - "runtime.md#rt-rte-conflict-review"
        - "runtime.md#rt-rte-recall-context"
        - "memory.md#mem-rte-trace-export"
        - "memory.md#mem-rte-administrative-views"
        - "memory.md#mem-rte-feedback-recording"
        - "runtime.md#rt-rte-remember-intake"
        - "runtime.md#rt-rte-evaluation-suite"
        - "memory.md#mem-obj-organization-receipt"
      note: "Identifier, coarse and lexical signals attach to named internal push selections. Complete pull-only scope is not established; signal is therefore not globally inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic session extraction/checkpoint-to-semantic-memory chain when event content records interaction experience"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-events"
                - "memory.md#mem-obj-extraction-checkpoints"
                - "runtime.md#rt-rte-session-intake"
              note: "Trace-bearing input can automatically produce retained proposals/semantic knowledge consumed by later linking, intake or recall. This is wired trace-fed durable behavior shaping, not observed benefit."
          records:
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-session-intake"
          note: "The conditional route is implemented; opaque/mixed caller origin prevents treating every session submission as a qualifying trace."
        - scope: "Feedback/evaluation records, conflict/organization inputs, historical Dream and other opaque write provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-feedback-recording"
            - "runtime.md#rt-rte-evaluation-suite"
            - "runtime.md#rt-rte-conflict-review"
            - "runtime.md#rt-rte-ontology-maintenance"
            - "memory.md#mem-rte-administrative-views"
          note: "Feedback and evaluation readers do not establish an automatic behavior-shaping update; their broader consumers and other historical/input provenance remain uninspected. Without bounded complete negatives, these branches receive neither no nor inapplicable."
      records:
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "runtime.md#rt-rte-session-intake"
        - "memory.md#mem-rte-feedback-recording"
        - "runtime.md#rt-rte-evaluation-suite"
        - "runtime.md#rt-rte-conflict-review"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "memory.md#mem-rte-administrative-views"
      note: "A conditional positive survives incomplete system coverage. No local or system-wide no is asserted from missing run evidence, absent parameter training or ordinary event retention alone."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Original content entering the qualifying conditional session-extraction write"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-session-events"
            - "memory.md#mem-obj-extraction-checkpoints"
            - "runtime.md#rt-rte-session-intake"
          note: "Session event text may be an interaction trace or arbitrary caller text. Framework/session labels do not establish whether the actual original content is conversational session logs, tool results, environmental events or linked trajectories. No controlled source is established for the opaque input."
        - scope: "Other unresolved potential trace-fed updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-feedback-recording"
            - "runtime.md#rt-rte-evaluation-suite"
            - "runtime.md#rt-rte-ontology-maintenance"
            - "runtime.md#rt-rte-conflict-review"
            - "memory.md#mem-rte-administrative-views"
          note: "The records do not completely establish qualifying update consumers or original input content for these alternatives. Operational event storage alone does not classify a learning source."
      records:
        - "memory.md#mem-obj-session-events"
        - "memory.md#mem-obj-extraction-checkpoints"
        - "runtime.md#rt-rte-session-intake"
        - "memory.md#mem-rte-feedback-recording"
        - "runtime.md#rt-rte-evaluation-suite"
        - "runtime.md#rt-rte-ontology-maintenance"
        - "runtime.md#rt-rte-conflict-review"
        - "memory.md#mem-rte-administrative-views"
      note: "Not-determinable, not absent or inapplicable: a conditional trace-fed write is wired, but accepted records do not identify its actual original trace content. No source value is inferred from adapter labels."
---

# Dense-Mem memory profile

## Comparison rationale

This profile classifies accepted records, not additional source facts. All positive findings are implementation wiring; none claims observed operation or causal benefit. Coverage remains partial wherever retained alternatives, provenance or consumer effects are unresolved. The inventory is broader than answering-agent recall: retry checkpoints, worker context, feedback readers, historical displays and evaluation reloads are later memory consumers too.

### Forms, storage and authority

Relational persistence and vector access coexist for [MEM-OBJ-search-vectors](memory.md#mem-obj-search-vectors). Parametric here denotes dense encoding, not model training. Relationship edges and JSON serialization do not by themselves establish graph or file substrates. Text, symbolic controls and vectors have separate consumption paths. Historical statement/rationale display does not classify the opaque payload described by [MEM-RTE-administrative-views](memory.md#mem-rte-administrative-views).

Retained eligibility state has enforcement force; retained text/features can influence ranking under fixed code. Session traces at extraction have conditional learning force independently of downstream knowledge authority. Ontology definitions are interpreted source context, not standing instructions: see [MEM-BAP-organization-selection](memory.md#mem-bap-organization-selection). The static assessment/export prompts and external provider parameters are outside accumulated-memory scope. The afforded skill draft in [RT-RTE-skill-export](runtime.md#rt-rte-skill-export) has no established retained installation, so it supplies neither instruction authority nor another trace-learning write.

### Write and curation distinctions

Automatic admission and unknown human control coexist. Software/model commits require no human content decision, while generic manager/owner/caller roles do not establish manual control. These are different mechanisms, not contradictory classifications of the same decision. Initial vocabulary and historical admission remain unresolved rather than inheriting the automatic writer's classification: see [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance) and [RT-RTE-manager-publication](runtime.md#rt-rte-manager-publication).

Session extraction is consolidation even though its semantic faithfulness is unobserved. The epistemic indeterminacy in [EPI-OBJ-relationship-proposals](epistemic.md#epi-obj-relationship-proposals) does not establish synthesis. Correction evolves an entry; withdrawal invalidates reliance while preserving history; retention erasure/pruning forgets content. Index rebuild, requested model behavior and result deduplication do not establish additional retained curation operations. The fixed [MEM-OBJ-conflict-derivation](memory.md#mem-obj-conflict-derivation) is audit/recovery material, not newly recalled factual support.

### Read-back and trace uncertainty

Requested recall remains pull despite automatic ranking. New intake automatically supplies matching retained prior events to the extractor; source-linked vocabulary is automatically supplied to the organizer. These internal push operations have actual identity/lexical targeting and separate coarse budget filters. They do not establish unsolicited host-conversation insertion. Their controls are recorded in [MEM-OBJ-session-events](memory.md#mem-obj-session-events), [MEM-OBJ-ontology-records](memory.md#mem-obj-ontology-records) and the annotations on [RT-RTE-session-intake](runtime.md#rt-rte-session-intake) and [RT-RTE-ontology-maintenance](runtime.md#rt-rte-ontology-maintenance).

The wired session path qualifies for trace learning when caller text records experience, because it automatically derives durable material for later consumers. That conditional positive does not authenticate all inputs. The accepted records explicitly leave actual event origin mixed or opaque; no session-log, tool-trace, event-stream or trajectory source can be assigned merely from the session/framework wrapper. Trace-source therefore remains not-determinable, not inapplicable. Feedback snapshots and loaded evaluation traces establish retention/read-back, not an independently demonstrated automatic adaptation route: see [MEM-RTE-feedback-recording](memory.md#mem-rte-feedback-recording) and [RT-RTE-evaluation-suite](runtime.md#rt-rte-evaluation-suite).

### Reconciliation and limits

Reconciliation supersedes EPI-RTE-recall-feedback with [MEM-RTE-feedback-recording](memory.md#mem-rte-feedback-recording). All profile feedback citations use that canonical route; [EPI-OBJ-feedback-assessment](epistemic.md#epi-obj-feedback-assessment) remains a separate content object. No other supersession changes a value.

The retained disagreement about original fragment delivery does not prevent form or direction classification. This profile asserts source-derived natural-language context, not delivery of a complete fragment. [EPI-RTE-recall-hydration](epistemic.md#epi-rte-recall-hydration) describes truncation and the ordinary lexical-path support-gating counterexample. Accordingly no full-content guarantee or universal relationship-support gate is used to establish an authority finding. The example's discarded recall/trace responses in [WF-CLM-client-delivery](workflow.md#wf-clm-client-delivery) establish neither semantic verification nor host answer benefit.

Missing initial control, historical payload schemas, actual trace origin, full diagnostic consumers, complete evaluation import provenance and detailed alternative maintenance/recovery selectors prevent stronger coverage assessments. No bounded absence record is supplied that would justify converting these limits into absent axes or a system-wide trace-learning no. No source files were read for this profile; all classifications use the supplied accepted records and reconciliation only.
