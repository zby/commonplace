---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Archie memory profile of retained modelRoles configuration at the shell runtime-client boundary."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
source-identity: https://github.com/gchamon/archie
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
memory-comparison:
  version: 2
  scope: "The use-changed modelRoles configuration value, including its opaque retained backend and initial provenance/admission, the helper's default replacement, and subsequent helper read/modify/write consumption. External model-role interpretation is an unresolved downstream contract. Excludes static shipped shell definitions and launch flags as memory, the planned assistant as an operative memory system, unrelated desktop/contributor persistence, and external agent sessions, provider weights and internal maintenance routes."
  axes:
    storage_substrate:
      assessment: not-determinable
      units:
        - scope: "Retained modelRoles value behind external omp config get/set"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "The retained backend is opaque. JSON is encoding, and the transient shell variable is transport rather than the retained substrate. No controlled retained-substrate value follows."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "The records inventory one retained configuration object but identify no backend; files, databases and other substrate alternatives remain unresolved."
    representational_form:
      assessment: known
      units:
        - scope: "modelRoles JSON at the subsequent helper getter, jq assignment and setter path"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
              note: "The helper consumes localized JSON fields under fixed assignment rules, including the default selector string; it does not interpret them as prose or numerical weights."
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "This classifies the entire inspected consumption path, including mechanically preserved other fields. It does not classify their unknown downstream meanings."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "The single configuration object's inspected consumption is symbolic. Opaque storage encoding and external model processing are not additional established forms on this path."
    lineage:
      assessment: partial
      units:
        - scope: "Updated modelRoles produced by the helper from getter output and a profile literal"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-default-update]
              note: "A deterministic jq transformation constructs the replacement configuration from the existing object and fixed selector; it does not extract traces."
          records: [runtime.md#rt-rte-default-update]
          note: "The subsequent derivation is visible independently of the original object's provenance. Static authorship of the profile code is not another retained-memory derivation route."
        - scope: "Initial modelRoles content and surviving non-default fields before the helper transformation"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "Getter output supplies existing content without its initialization or external editing history; no authored, imported or trace-extracted initial lineage is established."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "Known mechanical derivation does not resolve the provenance of retained inputs."
    behavioral_authority:
      assessment: not-determinable
      units:
        - scope: "Existing modelRoles fields at the later helper's read/modify/write consumer"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "The helper replaces the prior default and mechanically carries other fields forward. No retained field is shown supplying knowledge, directions, a ranking input, a selection policy, an admissibility criterion or a veto at that consumer. Mechanical preservation alone establishes none of the controlled forces."
        - scope: "Retained default at the intended external runtime model-role consumer"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-bap-role-arguments, runtime.md#rt-rte-profile-launch, runtime.md#rt-rte-default-update]
          note: "Configuration authority is intended, but the actual retained-default consumer and precedence are uninspected. Explicit current-launch flags cannot establish routing by the retained value."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update, runtime.md#rt-bap-role-arguments, runtime.md#rt-rte-profile-launch]
      note: "The records establish operational configuration requests, not a controlled authority value at an established retained-content consumer. Unknown external interpretation is not an evidenced absence of authority."
    write_agency:
      assessment: partial
      units:
        - scope: "Helper replacement of the default and admission request to omp config set"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-default-update]
              note: "Software constructs and submits the transformed value without separate per-content operator approval. Starting a profile does not make this admission manual."
          records: [runtime.md#rt-rte-default-update]
          note: "The complete helper establishes this subsequent write mechanism, not external setter validation or successful retention."
        - scope: "Initial configuration admission and external content replacement"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "The getter's existing content has no recorded initialization control or external editing mechanism. Generic caller identity cannot establish manual agency."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "Automatic subsequent transformation is supported; initial and external admission control remain unresolved."
    curation_operations:
      assessment: known
      units:
        - scope: "Implemented helper transformation of the retained modelRoles default"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-default-update]
              note: "The helper revises an existing configuration entry by replacing its default field while preserving other ordinary object fields."
          records: [runtime.md#rt-rte-default-update]
          note: "The complete helper has one fixed field-revision operation; whole-object serialization is not consolidation or deduplication, and replacement is not history-preserving invalidation."
      records: [runtime.md#rt-rte-default-update]
      note: "Coverage is the implemented wrapper transformation, not unspecified external maintenance or the unimplemented assistant plan. No operation is inferred from those excluded mechanisms."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Subsequent profile invocation requesting the whole retained modelRoles through config get"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-default-update]
              note: "The later helper explicitly requests the configuration key and receives the whole value for transformation. Fulfilling that request is not an independent push."
          records: [runtime.md#rt-rte-default-update]
          note: "The repeated getter/transform/setter chain is wired, conditional on external persistence; no execution establishes that it operated."
        - scope: "Intended later runtime consumption of the retained default, including direct omp invocation"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-profile-launch, runtime.md#rt-rte-direct-handoff, runtime.md#rt-bap-role-arguments]
          note: "The retained-default consumer contract is uninspected. Launch flags and a callable bypass do not resolve request, selection or delivery operations there."
      records: [runtime.md#rt-rte-default-update, runtime.md#rt-rte-profile-launch, runtime.md#rt-rte-direct-handoff, runtime.md#rt-bap-role-arguments]
      note: "The helper supplies a pull witness, but the included intended downstream default-consumption contract prevents complete direction coverage."
    read_back_signal:
      assessment: not-determinable
      units:
        - scope: "Known helper pull operation"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-default-update]
          note: "This complete local chain requests the whole value; its key identifies requested configuration, not a push selection match."
        - scope: "Unresolved downstream runtime default-consumption contract"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-profile-launch, runtime.md#rt-rte-direct-handoff, runtime.md#rt-bap-role-arguments]
          note: "No push operation, trigger or selector is established for this contract, but its direction is unresolved rather than proven pull-only."
      records: [runtime.md#rt-rte-default-update, runtime.md#rt-rte-profile-launch, runtime.md#rt-rte-direct-handoff, runtime.md#rt-bap-role-arguments]
      note: "A known local pull does not make the whole axis inapplicable while downstream delivery remains unresolved; no positive signal can be assigned."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Automatic helper default replacement and later helper consumption"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-default-update]
          note: "The route records configuration and a fixed literal as inputs, not a qualifying trace-fed update. No canonical evidenced-absence record establishes the bounded negative required for a controlled no finding. Automatic retention alone establishes neither yes nor a formally warranted no."
        - scope: "Initial or externally replaced retained configuration content"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "Initial production, admission and any trace inputs are unknown. The helper's local negative cannot establish how that earlier content was produced."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "No qualifying trace-fed write is established. No canonical bounded-absence record supports no, and initial provenance is unresolved. External sessions and provider training are outside this memory scope."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Inspected helper default-replacement write"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-default-update]
          note: "The route establishes no qualifying trace-fed write or original trace input; without a canonical bounded-absence warrant for trace learning, global or local inapplicability is not asserted."
        - scope: "Unresolved initial or external production of modelRoles content"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
          note: "Neither a qualifying trace-fed production route nor its original inputs are recorded. No trace-source value or bounded absence follows."
      records: [runtime.md#rt-obj-model-roles, runtime.md#rt-rte-default-update]
      note: "Neither a positive trace-source finding nor the complete bounded absence needed for inapplicability is established by canonical records."
---

# Archie memory profile

## Comparison rationale

The memory object is retained `modelRoles`, not the shipped profiles or current-launch flags. [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) and [RT-RTE-default-update](runtime.md#rt-rte-default-update) supply the object and implementation passage. Their memory annotations establish symbolic consumption, unknown initial provenance, automatic subsequent replacement and request-driven read-back. JSON does not identify durable storage; the transient shell variable does not justify an in-memory retained-substrate finding.

The deterministic replacement maps to `other-compiled` lineage and `evolve` curation. These classify the subsequent transformation only. Static authorship of its input literal does not resolve initial configuration authorship or add a separate memory-authoring mechanism. The initial content's unresolved history remains explicit in lineage, write agency and trace coverage.

The actual later helper consumer preserves ordinary non-default fields but overwrites the old default. That mechanism does not itself establish one of the controlled behavioral-authority forces. The intended runtime default consumer remains unresolved, and current-launch role flags are not evidence that retained state routes an agent call. [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments), [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch) and [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff) retain that distinction. The same uncertainty prevents treating read-back as completely pull-only and its signal as globally inapplicable.

[RT-RTE-default-update](runtime.md#rt-rte-default-update) records configuration and a fixed literal as helper inputs, not a qualifying outcome-driven update, session extraction or compaction route. Automatic configuration replacement does not establish trace learning merely because it changes retained state. However, the accepted set declares no evidenced-absence record supporting a controlled local no; trace learning and trace source therefore remain not-determinable rather than asserting that negative. Unknown initial provenance independently prevents a complete negative. No observed operation or improvement is inferred.

The planned assistant, [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide), adds no operative documentation-memory unit. Provider weights, external sessions and unrelated repository persistence are excluded by the subsystem boundary, not silently classified absent. The retained configuration backend and intended downstream consumer remain included uncertainties because they belong to the inspected configuration route.

Reconciliation specifies no supersessions; all citations therefore retain their declaring runtime IDs. No source files were read for this profile: the supplied accepted records and their annotations sufficed, so there is no source-read log to add.
