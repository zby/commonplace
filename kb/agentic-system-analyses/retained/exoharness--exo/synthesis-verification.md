---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent synthesis verification of Exo's public runtime, memory, self-change and evaluation account at the frozen revision."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo synthesis verification

## Verification

The handed [public synthesis](synthesis.md#bounded-synthesis) supports publication as a bounded static account. I checked its substantive statements against the supplied records, annotations and reconciliation supersessions, and assessed its readability without the supporting members. I also checked carriage of the supplied report and profile judgments. Both declare no blockers or limits; the synthesis answers file is empty and no refusal was supplied. These judgments were inputs to assess, not substitutes for checking support.

### Boundary, progression and guarantees

The opening states the frozen revision, cutoff, implementation/design evidence basis and excluded dependency and deployment evidence. Its distinction between a whole-system functional boundary and exhaustive inspection agrees with the [boundary](boundary.md#boundary-and-evidence) and [Source register](boundary.md#source-register). It does not attribute external native-agent algorithms to Exo.

Definition admission, captured queue configuration, coordinator ownership and Basic model/tool progression are supported by [RT-RTE-definition-admission](runtime.md#rt-rte-definition-admission) and [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn). The synthesis separates turn completion from task correctness. Its alternatives preserve separate owners for Responses, native agents, RLM and background wakeups through [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop), [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge), [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) and [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup).

The disconnected-client assessment retains required storage and wakeup contracts. Basic's unresolved-call guard is not generalized to native or TypeScript recovery. The account withholds exactly-once effects, universal resumption and whole-runtime isolation, as required by [RT-CLM-recovery-scope](runtime.md#rt-clm-recovery-scope) and [RT-CLM-isolation-scope](runtime.md#rt-clm-isolation-scope). No architectural guarantee is promoted to observed reliability.

### Retention, authority and context reduction

The three textual channels retain their discriminating scopes and selectors: all current agent facts, conversation plans conditional on open work, and a catalog followed by requested skill payloads. Caps are not represented as a universal context budget. Support is [MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision), [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement) and [MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle). The synthesis follows the canonical plan route after supersession and does not collapse catalog metadata into the skill body.

The public text correctly separates structural admission, model-interpreted reliance and factual acceptance. Its authoritative-memory qualification is supported by [EPI-RTE-memory-write](epistemic.md#epi-rte-memory-write) and [EPI-RTE-memory-read](epistemic.md#epi-rte-memory-read). The acquisition account preserves unknown source warrant and possible qualification loss in [EPI-RTE-web-access](epistemic.md#epi-rte-web-access). Its negative acceptance finding is expressly bounded to inspected writers, not arbitrary hosted agents or tools.

Withdrawal and corruption distinctions remain accurate: forgetting does not retract history, closed plans remain stored, and skill unlisting leaves direct bundled-file access. Filesystem rewind is not represented as rollback of conversation artifacts. The cited lifecycle routes and [MEM-RTE-sandbox-rewind](memory.md#mem-rte-sandbox-rewind) support those distinctions.

Result offload is described as fixed-rule prefix reduction, while Codex replay requests opaque native compaction. The account neither promises automatic full-result reload nor infers native rationale preservation. See [MEM-RTE-result-offload](memory.md#mem-rte-result-offload) and [MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction). The trace-learning passage explicitly uses the memory comparison's write-route meaning and immediately withholds improved future capacity. Its three positive mechanisms have automatic transformations and later consumers in those records and [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup). The statement that the comparison axes remain partial faithfully reports the supplied profile judgment; it does not claim a complete inventory or upgrade operational evidence.

### Capability change, independent properties and delivery

Host import-time execution, publication and subsequent handler selection remain distinct in the synthesis, consistent with [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) and [RT-BAP-installed-code](runtime.md#rt-bap-installed-code). Guardian activation retains writable-source and maintenance-permission conditions, queued rather than completed return, the two-second nonbarrier delay and fallible outcome recording. Development checking is not denied, but is correctly kept separate from ordinary guardian builds. See [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) and [EPI-RTE-development-checks](epistemic.md#epi-rte-development-checks).

The self-change conclusion leads with implemented activation capacity, then names the missing objective-responsive determination and later exercised dependence. It does not turn the design claim in [EPI-CLM-recursive-improvement](epistemic.md#epi-clm-recursive-improvement) into evidence of improvement. Theory-builder conditions 1–4, criticism-based learning, reflection, autonomy and self-improvement receive separate assessments. Their uncertainty agrees with the epistemic [bounded conclusion](epistemic.md#bounded-conclusion), rather than implying absent model processing or architectural impossibility.

The Harbor workflow preserves shared-agent versus trial-conversation scope, conditional sequential admission, existing-agent model reuse, container-selection checks, subprocess-only timeout enforcement and attempted export after failure. [WF-RTE-harbor-trial](workflow.md#wf-rte-harbor-trial) supports these claims. Single-page export, possible preview substitution and suppressed export failure are retained from [WF-OBJ-trajectory](workflow.md#wf-obj-trajectory). Neither artifact delivery nor sequential reuse is promoted to grading success or learning; [EPI-RTE-harbor-task](epistemic.md#epi-rte-harbor-task) supports withholding those conclusions.

### Limitations and disposition

I checked every row of the synthesis's [Limitations](synthesis.md#limitations) against the affected mechanisms. The table carries static-evidence limits, path-specific guarantees, opaque alternatives, incomplete reload/export, provenance and acceptance uncertainty, self-change attribution gaps and external grading. These qualifications also remain beside the corresponding public claims. Reconciliation retains no unresolved conflict, and the supplied verifications declare no additional limits to carry. No record fault discovered in this review requires a new publication limit or repair. The proposed evidence that would change the assessment is appropriately route-specific and distinguishes observed operation from causal benefit.

Source-read log: none. This review used the handed members and contracts only; it adds no evidence, corrected text or record. I found no unsupported central conclusion, comparison value, evidence-strength upgrade, absence assertion or complete-coverage claim requiring a blocker. Faithfully scoped uncertainties already expressed in the public account are not additional findings.

## Blockers

none

## Limits

none
