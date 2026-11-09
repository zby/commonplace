---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "MCMA-OpenMemory memory comparison: encrypted retained objects, derived access structures, caller-directed edits and request-driven recall."
run-id: AAS-2026-11-08-mcma-openmemory-a023f4989e1c-01
source-identity: https://github.com/jimmybackend/mcma-openmemory
reviewed-boundary: "556954d95f0d6d6894c5d46ffcc25a907150b0a7"
memory-comparison:
  version: 2
  scope: >-
    Retained generic library objects and revisions, manifest/root index, knowledge
    answers and eligibility metadata, explicit canonical memories and originals,
    interactions and their catalog, conversation discovery index, thematic
    derivatives, semantic vectors and identity links, context traces/catalog,
    mutable permission policy and vault payloads. Includes shipped CLI/web
    authoring, maintenance, inspection, recovery and later answer/context routes,
    plus exposed secret-use capability. Excludes static organizer/connector
    instructions, inference-provider weights not updated by these routes,
    deployment, billing/account state and ordinary current-request working state.
    Arbitrary future callers are not additional established consumption routes;
    generic caller control, arbitrary payload meaning and physical adapter state
    remain unresolved where the accepted records do not determine them.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Encrypted library object files, manifest and root-index layout shared by the retained memory objects"
          assessment: partial
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-library-index, memory.md#mem-rte-library-authoring]
              note: "Content-addressed .mcma object paths and replaceable manifest supply a file-oriented retained layout; later reads resolve current hashes."
          records: [memory.md#mem-obj-library-index, memory.md#mem-rte-library-authoring]
          note: "The logical file layout is established, but selected StorageAdapter and remote storage internals are not completely characterized; no complete physical-substrate union follows."
        - scope: "Provider-keyed semantic index vectors and symbolic identity links"
          assessment: partial
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-obj-library-index]
              note: "Vectors are retained inside encrypted library JSON objects in the same object layout, not shown to reside in a separate vector database."
          records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-obj-library-index]
          note: "Vector encoding does not determine storage substrate; physical adapter alternatives remain unresolved as for other library objects."
      records: [memory.md#mem-obj-library-index, memory.md#mem-rte-library-authoring, memory.md#mem-obj-semantic-vectors]
      note: "All included retained parts use the library's encrypted object infrastructure; the records support file layout but not exhaustive physical backend classification."
    representational_form:
      assessment: partial
      units:
        - scope: "Textual knowledge answers, canonical normalized/original text, interaction turns, thematic snippets and diagnostic/display text"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-knowledge-answer, memory.md#mem-obj-explicit-memory, memory.md#mem-obj-interaction, memory.md#mem-obj-thematic-summary, memory.md#mem-obj-context-traces, memory.md#mem-obj-context-catalog]
              note: "Humans or generation models interpret retained text; answer-copy code does not turn its meaning into fixed-rule symbolic content."
          records: [memory.md#mem-obj-knowledge-answer, memory.md#mem-obj-explicit-memory, memory.md#mem-obj-interaction, memory.md#mem-obj-thematic-summary, memory.md#mem-obj-context-traces, memory.md#mem-obj-context-catalog]
          note: "This unit concerns the named text parts, not arbitrary caller-defined answer values or the metadata beside them."
        - scope: "Addressing, hashes, validation/freshness, classification lists, discovery order, diagnostic counters, permission rules and vault-entry metadata"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-library-index, memory.md#mem-obj-knowledge-metadata, memory.md#mem-obj-conversation-index, epistemic.md#epi-obj-interaction-catalog, memory.md#mem-obj-context-catalog, runtime.md#rt-obj-permission-policy, memory.md#mem-obj-vault]
              note: "Localized fields have fixed addressing, selection, admission or display semantics; catalog labels are interpreted as bounded organization lists at their code consumer."
          records: [memory.md#mem-obj-library-index, memory.md#mem-obj-knowledge-metadata, memory.md#mem-obj-conversation-index, epistemic.md#epi-obj-interaction-catalog, memory.md#mem-obj-context-catalog, runtime.md#rt-obj-permission-policy, memory.md#mem-obj-vault]
          note: "Natural-language label meanings and validation reasons remain in the text unit; JSON serialization alone is not this classification's warrant."
        - scope: "Retained semantic vectors at query comparison, separate from their symbolic ref/hash envelope"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-rte-semantic-maintenance]
              note: "Dense numerical representations distribute retrieval information across vector coordinates; they are not updated model weights."
          records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-rte-semantic-maintenance]
          note: "The retained numerical representation and actual ranking consumer are specified despite opaque embedding-provider internals."
        - scope: "Arbitrary generic library payloads, nontext caller-defined answers and secret bytes at trusted callbacks"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, memory.md#mem-obj-knowledge-answer, memory.md#mem-obj-vault]
          note: "Format labels and opaque bytes do not establish how eventual consumers interpret arbitrary payloads; no complete form classification follows."
      records: [memory.md#mem-rte-library-authoring, memory.md#mem-obj-knowledge-answer, memory.md#mem-obj-semantic-vectors, memory.md#mem-obj-vault, memory.md#mem-obj-library-index]
      note: "Known text, fixed-rule metadata and dense vectors coexist with unresolved generic payload/callback meaning."
    lineage:
      assessment: partial
      units:
        - scope: "Explicit user original, caller-supplied knowledge replacement, imported historical objects and archived incoming question/answer content"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-explicit-memory, epistemic.md#epi-rte-answer-replacement, memory.md#mem-rte-library-authoring, memory.md#mem-obj-interaction]
              note: "These routes acquire supplied content into retained objects; import does not certify its upstream truth or original authorship."
          records: [memory.md#mem-obj-explicit-memory, epistemic.md#epi-rte-answer-replacement, memory.md#mem-rte-library-authoring, memory.md#mem-obj-interaction]
          note: "Known immediate acquisition paths, not a claim that every historical input was authored by a human."
        - scope: "Generated knowledge, optional organization and catalog classification, semantic vectors, access indexes and diagnostic catalog derivation"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-explicit-capture, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-semantic-maintenance, memory.md#mem-obj-library-index, memory.md#mem-obj-conversation-index, memory.md#mem-rte-inspector-snapshot]
              note: "Software/model transformations produce retained outputs from inputs; an indeterminate semantic relation does not erase the recorded derivation path."
          records: [runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-explicit-capture, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-semantic-maintenance, memory.md#mem-obj-library-index, memory.md#mem-obj-conversation-index, memory.md#mem-rte-inspector-snapshot]
          note: "This covers the local derivation, not external model training provenance."
        - scope: "Answer-derived thematic snippets extracted from retained interactions"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-thematic-summary, memory.md#mem-rte-thematic-sync]
              note: "Deterministic excerpt construction derives a retained point from an application-level conversational transcript."
          records: [memory.md#mem-obj-thematic-summary, memory.md#mem-rte-thematic-sync]
          note: "Original question/answer remains separately retained; extraction is not new factual warrant."
        - scope: "Initial arbitrary generic objects, policy/vault content and upstream provenance of caller content or embedding model parameters"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-permission-change, memory.md#mem-obj-vault, memory.md#mem-rte-semantic-maintenance]
          note: "Caller identity and provider ID do not determine original authorship or training lineage; no authored or exhaustive lineage conclusion is licensed for these alternatives."
      records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-semantic-maintenance, memory.md#mem-obj-vault]
      note: "Local acquisition and compilation are known; initial and upstream origins remain separate unresolved coverage."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Answer text and selected interaction/canonical/knowledge reference content at answering models and human browse/reopen consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-bap-memory-reference, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-inspector-snapshot, workflow.md#wf-rte-request-recovery]
              note: "Content supplies answers, reference or diagnostic information; the connector requests untrusted-data treatment, not standing obedience to retained instructions."
          records: [runtime.md#rt-bap-memory-reference, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-inspector-snapshot, workflow.md#wf-rte-request-recovery]
          note: "Delivery and deterministic copying are wired; actual model reliance and benefit are not observed."
        - scope: "Retained vectors, intent/text features and confidence/freshness/validation at semantic and context ranking"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-bap-knowledge-reuse, runtime.md#rt-rte-context-supply]
              note: "Retained vectors and record features influence candidate order and relative priority under fixed code."
          records: [memory.md#mem-obj-semantic-vectors, memory.md#mem-bap-knowledge-reuse, runtime.md#rt-rte-context-supply]
          note: "Ranking authority does not require a retained learned ranking policy."
        - scope: "Permission rules at actor-aware access checks and knowledge/lifecycle eligibility fields at reuse selectors"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [runtime.md#rt-bap-policy-decision, memory.md#mem-bap-knowledge-reuse, epistemic.md#epi-rte-knowledge-assessment]
              note: "Retained rules and state determine conformity/admissibility for covered access and direct reuse."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-bap-policy-decision, runtime.md#rt-clm-permission-scope, memory.md#mem-bap-knowledge-reuse, runtime.md#rt-rte-memory-mutation]
              note: "Denials and exclusion from covered reads/reuse have veto force; raw host APIs and separate canonical policies limit its scope."
          records: [runtime.md#rt-bap-policy-decision, runtime.md#rt-clm-permission-scope, memory.md#mem-bap-knowledge-reuse, epistemic.md#epi-rte-knowledge-assessment, runtime.md#rt-rte-memory-mutation]
          note: "These are code-enforced local eligibility criteria, not factual truth guarantees or process isolation."
        - scope: "Manifest/root index, conversation index and interaction catalog at object discovery, recovery and thematic destination selection"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-library-index, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-thematic-sync, workflow.md#wf-rte-request-recovery]
              note: "Retained refs/order and catalog labels choose objects, input candidates and topic destinations for later operations."
          records: [memory.md#mem-obj-library-index, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-thematic-sync, workflow.md#wf-rte-request-recovery]
          note: "Titles used for display are distinct from machine-consumed routing fields."
        - scope: "Retained interactions at automatic catalog/discovery derivation, with derived structures used by later selection"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-thematic-sync]
              note: "Recorded experience feeds durable organization artifacts that shape later candidate discovery and thematic destination selection; this is update-consumer authority, not proof of improved capacity."
          records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-thematic-sync]
          note: "The derived discovery fields' downstream routing force is a separate consumption path from this trace-fed update."
        - scope: "Arbitrary generic objects and opaque vault secret payloads at unspecified consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, memory.md#mem-obj-vault]
          note: "A read capability or trusted callback does not establish arbitrary payload authority; no instruction or other force is inferred from opaque contents."
      records: [runtime.md#rt-bap-memory-reference, memory.md#mem-bap-knowledge-reuse, runtime.md#rt-bap-policy-decision, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-obj-vault, memory.md#mem-rte-library-authoring]
      note: "Different consumers give retained parts knowledge, ranking, validation, enforcement, routing and learning force; generic payload consumers remain unresolved. Static shipped prompts do not add memory instruction authority."
    write_agency:
      assessment: partial
      units:
        - scope: "Explicit user save of original text and user-directed canonical edit/delete content"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-memory-mutation]
              note: "The described user explicitly supplies original content/save intent or the proposed canonical edit/delete; software authorization is not a substitute for that decision."
          records: [runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-memory-mutation]
          note: "Manual applies to supplied source/edit decisions, not automatic organization or subsequent mirror/derivative writes."
        - scope: "Generated capture, model organization and catalog admission, archive/index/vector/diagnostic maintenance and compatibility/privacy rule updates"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-web-request, memory.md#mem-rte-semantic-maintenance, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-inspector-snapshot, memory.md#mem-obj-conversation-index, runtime.md#rt-obj-permission-policy]
              note: "Software/model admission has no per-output human approval, including labels produced after an approval action and organized text after a save request."
          records: [runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-web-request, memory.md#mem-rte-semantic-maintenance, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-inspector-snapshot, memory.md#mem-obj-conversation-index, runtime.md#rt-obj-permission-policy]
          note: "Starting a workflow is not approval of its newly derived content. Policy automation is supported by the memory annotation on the policy object."
        - scope: "Generic library authoring/import, direct knowledge edits/validation, interaction approve/discard and caller policy/vault management"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, memory.md#mem-rte-knowledge-editing, runtime.md#rt-rte-interaction-approval, runtime.md#rt-rte-permission-change, memory.md#mem-obj-vault]
          note: "Generic caller/owner roles do not establish a human supplying or reviewing each item; permission and shape gates alone do not determine human versus software control of the content decision."
      records: [runtime.md#rt-rte-explicit-capture, runtime.md#rt-rte-memory-mutation, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-library-authoring, memory.md#mem-rte-knowledge-editing, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-semantic-maintenance, memory.md#mem-rte-thematic-sync, memory.md#mem-rte-inspector-snapshot, memory.md#mem-obj-vault]
      note: "Explicit user content decisions and automatic derived admission are established locally; human involvement on generic caller-controlled mechanisms is unresolved."
    curation_operations:
      assessment: partial
      units:
        - scope: "Deterministic thematic extraction and bounded retained discovery/diagnostic views"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-rte-thematic-sync, memory.md#mem-obj-thematic-summary, memory.md#mem-obj-conversation-index, memory.md#mem-rte-inspector-snapshot]
              note: "Retained turns/answers are compressed into snippets and bounded discovery/display representations; full originals or previous revisions remain available."
          records: [memory.md#mem-rte-thematic-sync, memory.md#mem-obj-thematic-summary, memory.md#mem-obj-conversation-index, memory.md#mem-rte-inspector-snapshot]
          note: "Excerpt fidelity limits do not turn compression into synthesis. This unit does not classify opaque model organization."
        - scope: "Canonical/knowledge edits, validation and derivative supersession"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-memory-mutation, memory.md#mem-rte-knowledge-editing, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-thematic-sync]
              note: "Existing entries or their reliance metadata are revised with version history."
            - value: invalidate
              basis: wired
              records: [runtime.md#rt-rte-memory-mutation, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-knowledge-editing, memory.md#mem-rte-thematic-sync]
              note: "Tombstones, retraction and superseded/untrusted state withdraw current reliance while retaining historical ciphertext."
            - value: promote
              basis: wired
              records: [runtime.md#rt-rte-interaction-approval, epistemic.md#epi-rte-knowledge-validation]
              note: "Approval/confirmation raises validation and confidence, enabling stronger later reuse; it does not independently prove truth."
          records: [runtime.md#rt-rte-memory-mutation, memory.md#mem-rte-knowledge-editing, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-thematic-sync, epistemic.md#epi-rte-knowledge-validation]
          note: "These findings concern implemented transformations, not route-name implications or secure erasure."
        - scope: "Capped current conversation-discovery and diagnostic trace lists"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-obj-conversation-index, memory.md#mem-obj-context-traces]
              note: "Old entries drop out of current recent/discovery and trace views at fixed caps, reducing current availability without deleting canonical originals or old encrypted revisions."
          records: [memory.md#mem-obj-conversation-index, memory.md#mem-obj-context-traces]
          note: "Bounded view forgetting, not age-weighted forgetting of answer objects."
        - scope: "Optional model organizer and catalog semantic transformations"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-explicit-capture, epistemic.md#epi-rte-catalog-classification]
          note: "Preservation/no-invention instructions and structural checks do not establish whether concrete model transformations consolidate or synthesize; actual outputs are unprovided."
        - scope: "Other arbitrary generic retained content and requested maintenance semantics"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, memory.md#mem-rte-semantic-maintenance]
          note: "Generic update, import fingerprint collision rejection and index rebuild alone establish no further controlled curation transformation."
      records: [memory.md#mem-rte-thematic-sync, runtime.md#rt-rte-memory-mutation, memory.md#mem-rte-knowledge-editing, runtime.md#rt-rte-interaction-approval, memory.md#mem-obj-context-traces, memory.md#mem-obj-conversation-index, runtime.md#rt-rte-explicit-capture, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-library-authoring]
      note: "Supported local compression, revision, withdrawal, promotion and view forgetting do not resolve optional model semantics or arbitrary caller transformations. Read-time deduplication alone is not retained-memory dedup curation."
    read_back_direction:
      assessment: known
      units:
        - scope: "Shipped CLI/web inspection, direct/semantic/broad answering, context reconstruction, interaction reopen and recovery, diagnostic snapshots and policy evaluation"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-context-supply, workflow.md#wf-rte-request-recovery, memory.md#mem-rte-inspector-snapshot, runtime.md#rt-bap-policy-decision, memory.md#mem-rte-thematic-sync]
              note: "Consumer operations request retained content or an answer; automatic selection inside that requested operation is not an additional unsolicited push."
          records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-context-supply, workflow.md#wf-rte-request-recovery, memory.md#mem-rte-inspector-snapshot, runtime.md#rt-bap-policy-decision, memory.md#mem-rte-thematic-sync]
          note: "The accepted memory inventory traces the shipped later-consumer routes, including human browsing of thematic material; no separate scheduled delivery route is part of that inventory."
        - scope: "Named vault secret at trusted callback"
          assessment: known
          findings:
            - value: pull
              basis: afforded
              records: [memory.md#mem-obj-vault]
              note: "useVaultSecret supplies the named secret to a requested trusted operation; this is an exposed later-use capability, not a deployed model consumer."
          records: [memory.md#mem-obj-vault]
          note: "Direction is determined for the exposed capability even though actual callback behavior and deployment are not established."
      records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-context-supply, workflow.md#wf-rte-request-recovery, memory.md#mem-rte-inspector-snapshot, runtime.md#rt-bap-policy-decision, memory.md#mem-rte-thematic-sync, memory.md#mem-obj-vault]
      note: "Known within the supplied inventory of shipped routes and explicitly afforded secret use. Unknown hypothetical callers are not evidence of another delivery direction."
    read_back_signal:
      assessment: inapplicable
      units:
        - scope: "All established pull routes and the afforded named-secret callback"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-context-supply, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-library-authoring, workflow.md#wf-rte-request-recovery, memory.md#mem-rte-inspector-snapshot, runtime.md#rt-bap-policy-decision, memory.md#mem-rte-thematic-sync, memory.md#mem-obj-vault]
          note: "This inventory is pull-only; the axis characterizes push selection, not exact keys, lexical relevance or query embeddings used to fulfill a request."
      records: [runtime.md#rt-rte-context-supply, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-library-authoring, workflow.md#wf-rte-request-recovery, memory.md#mem-rte-inspector-snapshot, runtime.md#rt-bap-policy-decision, memory.md#mem-rte-thematic-sync, memory.md#mem-obj-vault]
      note: "Direction coverage includes ordinary recall, browsing/inspection, recovery, retained access rules and secret use; none supplies an established push operation to classify."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic conversation-discovery derivation from archived turns, followed by later context candidate lookup"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, runtime.md#rt-rte-context-supply]
              note: "Recorded question/answer turns feed durable discovery refs/order/compact fields; later calls use that index to find canonical turns for context."
          records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, runtime.md#rt-rte-context-supply]
          note: "Automatic trace-fed durable behavior-shaping access state qualifies without a weight update, a new claim or demonstrated improvement."
        - scope: "Optional automatic catalog classification of archived interactions and later thematic destination selection"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [epistemic.md#epi-rte-catalog-classification, epistemic.md#epi-obj-interaction-catalog, memory.md#mem-rte-thematic-sync]
              note: "Session question/answer feeds model/software catalog admission; retained labels subsequently choose thematic topic paths. Owner approval of the interaction is not per-label human approval."
          records: [epistemic.md#epi-rte-catalog-classification, epistemic.md#epi-obj-interaction-catalog, memory.md#mem-rte-thematic-sync]
          note: "The durable artifact's routing consumer is established; thematic snippet browsing is not assumed to be model-summary reuse."
        - scope: "Other generated captures, caller-controlled replacements/approval, generic objects, diagnostics and external provider state"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-library-authoring, memory.md#mem-rte-inspector-snapshot, memory.md#mem-rte-semantic-maintenance]
          note: "Not every generated answer is a trace-fed update, generic caller control is unresolved and diagnostics have no established automatic policy-update consumer. No bounded evidenced-absence record warrants a local no or exhaustive learning negative."
      records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, runtime.md#rt-rte-context-supply, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-thematic-sync, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-library-authoring, memory.md#mem-rte-inspector-snapshot, memory.md#mem-rte-semantic-maintenance]
      note: "Supported automatic trace-fed discovery/catalog routes establish yes at wiring strength. Remaining routes do not supply complete learning coverage or any warranted system-wide no."
    trace_source:
      assessment: partial
      units:
        - scope: "Conversation-index derivation and interaction-catalog classification qualifying above"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification]
              note: "Original source is recorded conversational question/answer activity, not raw provider reasoning or tool traces; serialization as archive JSON does not add event-stream origin."
          records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification]
          note: "Both classified qualifying routes consume application-level recorded turns. Existing catalog is auxiliary state, not another evidenced trace-origin class."
        - scope: "Unresolved trace-learning alternatives in generic/caller-controlled capture and external provider state"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-library-authoring, runtime.md#rt-rte-ask-answer, runtime.md#rt-rte-interaction-approval, memory.md#mem-rte-semantic-maintenance, memory.md#mem-rte-inspector-snapshot]
          note: "Without a qualifying automatic trace-fed route and original-content account for these alternatives, no additional trace source or inapplicability is established."
      records: [memory.md#mem-obj-interaction, memory.md#mem-obj-conversation-index, epistemic.md#epi-rte-catalog-classification, memory.md#mem-rte-library-authoring, runtime.md#rt-rte-ask-answer, memory.md#mem-rte-semantic-maintenance, memory.md#mem-rte-inspector-snapshot]
      note: "Session logs are supported for the classified automatic update routes; unresolved learning inventory prevents complete trace-source coverage."
---

# MCMA-OpenMemory memory profile

## Comparison rationale

The comparison covers retained content and access structures, not the entire
runtime's persistence. In particular, external inference weights, deployment
checkout state and static organizer instructions do not become acquired memory
merely because a later request uses them. The included object inventory and its
consumer distinctions follow [MEM-RTE-library-authoring](memory.md#mem-rte-library-authoring),
[MEM-OBJ-conversation-index](memory.md#mem-obj-conversation-index),
[MEM-RTE-inspector-snapshot](memory.md#mem-rte-inspector-snapshot) and
[MEM-OBJ-vault](memory.md#mem-obj-vault). File layout is a supported local storage
finding, not a complete claim about remote adapters. Dense vectors are a form
of retained representation; their encrypted JSON container does not establish
a vector-database substrate ([MEM-OBJ-semantic-vectors](memory.md#mem-obj-semantic-vectors)).

Reconciliation supersedes the epistemic canonical-memory, interaction-answer
and thematic-summary object declarations with
[MEM-OBJ-explicit-memory](memory.md#mem-obj-explicit-memory),
[MEM-OBJ-interaction](memory.md#mem-obj-interaction) and
[MEM-OBJ-thematic-summary](memory.md#mem-obj-thematic-summary). It also supersedes
the epistemic thematic route with
[MEM-RTE-thematic-sync](memory.md#mem-rte-thematic-sync). The profile uses these
canonical destinations. The combined epistemic knowledge object remains a
valid container; the profile uses its answer and metadata parts where force
or form differs. Catalog classification remains a separate mechanism, not a
duplicate summary route ([EPI-RTE-catalog-classification](epistemic.md#epi-rte-catalog-classification)).

The request-driven context chain is pull, including automatic choice of
context within that request. Exact IDs, query embeddings, lexical relevance
and recent-anchor filtering therefore do not populate the push-signal axis.
The context builder's delivery is not proof that the model used the material;
its connector policy asks for reference-only treatment
([RT-RTE-context-supply](runtime.md#rt-rte-context-supply),
[RT-BAP-memory-reference](runtime.md#rt-bap-memory-reference)). Thematic browsing
and diagnostic inspection are real later consumers without being generation
routes ([MEM-RTE-thematic-sync](memory.md#mem-rte-thematic-sync),
[MEM-RTE-inspector-snapshot](memory.md#mem-rte-inspector-snapshot)).

Trace learning is classified at the automatic durable-update route, separately
from improved capacity. Conversation discovery state is produced from recorded
turns and shapes later context candidate lookup
([MEM-OBJ-conversation-index](memory.md#mem-obj-conversation-index)). Catalog
labels are automatically admitted from recorded conversational content and
later choose thematic destinations
([EPI-RTE-catalog-classification](epistemic.md#epi-rte-catalog-classification),
[MEM-RTE-thematic-sync](memory.md#mem-rte-thematic-sync)). These support wired
local yes findings even though no weight learning, benefit or exercised
self-improvement is established. Raw diagnostic retention alone supplies no
corresponding automatic revision consumer. No evidenced-absence records were
supplied for the unresolved inventory, so none is converted into a local no.
The system union retains yes but not complete learning coverage.

Thematic clipping is consolidation, not synthesis merely because it can lose a
qualification. Fixed caps reduce the current discovery/diagnostic view without
securely erasing historical content. Index rebuilds and primary-key/fingerprint
collision checks do not alone establish dedup curation
([MEM-RTE-thematic-sync](memory.md#mem-rte-thematic-sync),
[MEM-OBJ-context-traces](memory.md#mem-obj-context-traces),
[MEM-RTE-library-authoring](memory.md#mem-rte-library-authoring)). Optional model
organization remains semantically unresolved: a no-invention instruction and
JSON checks do not establish a concrete output's preservation or novelty
([RT-RTE-explicit-capture](runtime.md#rt-rte-explicit-capture)).

Manual write agency applies only where the record identifies an explicit user
content decision. It does not extend to model organization after that decision,
or to generic owner-role calls whose principal could be software. Likewise,
permission rules have enforcement force only at covered actor-aware APIs;
knowledge validation and canonical recall use different eligibility policies
([RT-CLM-permission-scope](runtime.md#rt-clm-permission-scope),
[MEM-BAP-knowledge-reuse](memory.md#mem-bap-knowledge-reuse),
[RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer)). These local distinctions
prevent a single trust, approval or authority assertion for every retained part.

No source files were read for this classification. All warrants come from the
supplied accepted records and their annotations; no new evidence or records
were added. Findings retain implementation or capability strength, not observed
operation or causal benefit.
