---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of Exo's memory profile against accepted records at the frozen source revision."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo profile verification

## Verification

I checked all ten axes, their positive findings and evidence bases, their unresolved units, and their inventory scope in the [profile](memory-profile.md#comparison-rationale). The classifications are supported within their stated boundaries. All axes remain partial; the profile does not turn an inspected witness into complete system coverage. No correction answers or refusal arguments were supplied.

The retained-memory scope is appropriate. Mutable guidance, installed capabilities and repository edits are included through recorded later consumers, rather than because they occupy storage. Static shipped instructions, ordinary turn-local RLM variables and external inference weights are excluded. Harbor's later read of journal events is included without treating the exported trajectory as a demonstrated learning input. These distinctions agree with [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions), [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update), [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) and [WF-OBJ-trajectory](workflow.md#wf-obj-trajectory).

### Objects, forms and derivations

Storage findings distinguish filesystem artifact versions, installed files, writable repository source and the process-local web cache. The profile does not classify native continuation state or backend checkpoint bytes from their IDs. Support comes from [MEM-OBJ-artifact-versions](memory.md#mem-obj-artifact-versions), [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry), [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update), [EPI-OBJ-web-result](epistemic.md#epi-obj-web-result) and [MEM-OBJ-sandbox-snapshots](memory.md#mem-obj-sandbox-snapshots).

Representational form is separated by operative part and consumer: interpreted text, fixed-rule metadata and executable modules do not classify opaque artifact or native payloads. Grouped units retain the same local classification and coverage; they do not imply that every part of the containing object has that form. The supporting distinctions are explicit in [MEM-OBJ-exo-memory](memory.md#mem-obj-exo-memory), [MEM-OBJ-exo-todos](memory.md#mem-obj-exo-todos), [MEM-OBJ-skills-index](memory.md#mem-obj-skills-index), [MEM-OBJ-skill-record](memory.md#mem-obj-skill-record) and [MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction).

Lineage findings classify proposal and derivation paths, not authenticated origins of arbitrary submitted bytes. Authored proposals, imported web assertions and trace-derived continuation material have distinct witnesses. Unknown skill, initial guidance, source-edit and native-state provenance remains visible. See [MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision), [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission), [EPI-RTE-web-access](epistemic.md#epi-rte-web-access) and [MEM-RTE-result-offload](memory.md#mem-rte-result-offload).

### Consumers, admission and maintenance

Behavioral authority is attached to actual consumers and effects. Standing guidance and informational context are distinguished from lookup/progression routing and local read or recovery vetoes. Learning authority at a trace-update consumer is not confused with the resulting context's authority at the model. Skill unlisting is not generalized into complete revocation, and executable authority is not automatically labelled enforcement. These dispositions are supported by [MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle), [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn), [RT-CLM-recovery-scope](runtime.md#rt-clm-recovery-scope), [RT-BAP-installed-code](runtime.md#rt-bap-installed-code) and the three continuation routes discussed below.

Write agency uses admission mechanisms, not physical writers or presumed human authorship. The model/software branches support automatic admission, while generic callers and local/source editing control remain unresolved. Starting a task or requesting a rewind does not establish per-content human approval. See [MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision), [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement), [MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [MEM-RTE-sandbox-rewind](memory.md#mem-rte-sandbox-rewind).

Curation findings follow implemented transformations: fact withdrawal with retained history, capacity eviction, plan/skill replacement, bounded catalog withdrawal, result-prefix reduction, cache expiry and executable-tool replacement/removal. Consolidation here does not require semantic model summarization. The native compaction command alone supplies no controlled curation value. The relevant support is [MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision), [MEM-OBJ-artifact-versions](memory.md#mem-obj-artifact-versions), [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement), [MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle), [MEM-RTE-result-offload](memory.md#mem-rte-result-offload), [EPI-RTE-web-access](epistemic.md#epi-rte-web-access), [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction).

### Delivery, selection and trace-fed updates

Read direction distinguishes automatically supplied context/catalogs from requested skill bodies, checkpoint restoration, cached query results and exported event pages. Requested returns are not counted again as independent push. Introspection retains afforded strength rather than inheriting wiring from unrelated history consumers. The unresolved general full-result reload route remains unresolved. See [MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle), [MEM-RTE-sandbox-rewind](memory.md#mem-rte-sandbox-rewind), [EPI-RTE-web-access](epistemic.md#epi-rte-web-access), [WF-RTE-harbor-trial](workflow.md#wf-rte-harbor-trial), [MEM-CLM-history-inspection](memory.md#mem-clm-history-inspection) and [MEM-RTE-result-offload](memory.md#mem-rte-result-offload).

Push signals name their trigger, inputs and selected material. Availability, open-item predicates, cursor/chunk rules and fixed prefixes support coarse selection. Scheduler owner/task matching supports the locally targeted identifier finding. Neither a requested file address nor an opaque native compaction operation establishes a semantic selector. See [MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision), [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement), [MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction) and [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup).

Trace learning's three positive routes have automatic trace-fed writes, retained continuation material and later consumers: result normalization, Codex replay compaction and scheduler feedback formatting. The profile correctly applies the write-route definition without demanding novel knowledge, transparent native semantics or demonstrated improvement. Their original inputs support tool-traces and, for conversational replay, session-logs. Journal wrapping does not add event-streams; sequential calls or an exported trajectory do not alone establish trajectories as a qualifying update source. Mixed antecedents and other possible updates remain unresolved. See [MEM-RTE-result-offload](memory.md#mem-rte-result-offload), [MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction), [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup) and [WF-OBJ-trajectory](workflow.md#wf-obj-trajectory).

### Coverage and reconciliation

I resolved the supplied supersessions before judging classifications. The profile uses the canonical memory-entry, todo-object and plan-route records; the combined epistemic skill object remains a compatible container, not a replacement for separate catalog/payload units. Specialized memory write/read/forget routes remain valid functional subdivisions. The profile does not resolve the reports' different emphases by upgrading evidence strength.

Opaque native payloads, backend checkpoint contents, alternate harnesses, host-specific selection and unresolved caller control prevent complete comparisons. They are already expressed in the profile's assessments and notes, rather than deferred to a publication-only caveat. These are faithful uncertainty, not additional verification findings. No emitted value requires observed or causal strength; the introspection affordance remains distinct from wired routes. No central conclusion, unsupported comparison value, false absence or complete-coverage assertion requires repair.

Source-read log: none. This verification used only the supplied members, types and contracts; it adds no evidence, record or replacement profile text.

## Blockers

none

## Limits

none
