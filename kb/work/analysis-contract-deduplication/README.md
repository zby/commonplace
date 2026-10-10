# Analysis contract deduplication

## Purpose and authority

Operator request, 2026-10-10: retain the synthesis-packet duplication audit as a workshop because it contains too many findings to resolve in the current conversation. The operator also suspects a broader tendency toward duplication in the repository. This audit establishes overlap in one packet, not a repo-wide finding.

The intended result is fewer repeated requirements without losing content semantics, verification standards, role-specific obligations, or guaranteed delivery to a consumer. This framing retains findings for later disposition; it does not commission a blanket rewrite or a repo-wide sweep. Implementation choices below are proposals, not adopted changes.

Close when each finding is consolidated, deliberately retained, or rejected with a reason; adopted changes have updated their consumers and passed relevant validation and tests. Extract any durable decision into the owning contracts or ADR, then remove this directory and its navigation entry. Do not make this workshop an analysis worker input.

## Evidence boundary and coordination

The audit examined repository method files and prompt generation at commit `f5f513c173d91e7599d813fd452a386a4c2de180`. It read the synthesis mission, rendered-prompt template, shared worker rules, shared record contract, and the eight types supplied to synthesis: boundary, runtime, memory, epistemic, reconciliation, memory profile, verification, and synthesis. It checked their loading in the plan and engine. Recheck current files before editing; another session may have changed the method.

The earlier run that motivated this investigation has `run-id: AAS-2026-10-10-dynamic-cheatsheet-fa9d998ebb28-01` and `method-commit: 877e98286ea7f5b5f227d47996db26e83207b01a`. This document is a method-text audit, not a source-system or run-evidence analysis. Repetition has not been established as the cause of that worker's premature stop.

Completed adjacent work: `e6aa3da29` deduplicates reading paths and checks rendered handouts; `f5f513c17` removes judgment gates from model delivery and restricts opening metadata to the boundary. Do not reopen these as unimplemented proposals. Trace-pointer retention is a separate Pi investigation. Fable owns the ADR 117 delivery-rule amendment, already recorded by the audit boundary. Coordinate concurrent edits before changing shared files.

## Ownership test

For each repeated clause, identify its authoritative owner, each consumer's actual loading path, and what the second occurrence adds. Consolidate only when the second occurrence adds no obligation, specialization, or independently necessary delivery path. Keep types: they define what the content means and what verification checks.

The [plan](../../agentic-system-analyses/instructions/analyse-agentic-system/plan.yaml) explicitly supplies `worker` and `contracts` criteria to record-consuming model jobs. The latter delivers the shared record contract. The loader supplies member types from roles. This supports consolidation without relying on incidental link-following. Preserve that delivery invariant in tests.

The adopted ownership rule is in [ADR 117](../../reference/adr/117-plans-derive-their-structural-jobs-from-the-type.md): types own member content, worker rules own execution, and mission instructions state what the job establishes and challenges.

## Findings awaiting disposition

### D1 — General evidence cautions repeated across types

Owner candidate: [record contract, Source-native coverage and uncertainty and Evidence interpretation](../../agentic-system-analyses/instructions/agentic-analysis-records.md#source-native-coverage-and-uncertainty).

Repeated rules include existence versus complete coverage, uninspected evidence versus absence, local missing facts and prevented conclusions, independent property assessments, and trace-fed updates not establishing improved capacity. Copies occur in:

- [Synthesis, Bounded synthesis](../../agentic-system-analyses/types/agentic-system-synthesis.md#bounded-synthesis), especially lines 43–51 at the audit commit.
- [Epistemic report, Assessment limits](../../agentic-system-analyses/types/agentic-system-epistemic-report.md#assessment-limits), especially lines 95–103.
- [Memory report, Boundary and evidence](../../agentic-system-analyses/types/agentic-system-memory-report.md#boundary-and-evidence), especially lines 39–43.
- [Memory profile, Memory comparison fields](../../agentic-system-analyses/types/agentic-system-memory-profile.md#memory-comparison-fields).

Proposal: retain general principles in the record contract and keep only output-specific requirements in types. Preserve the synthesis's obligation to discuss particular properties when supported. Preserve the profile's exact `known`, `partial`, and other assessment semantics; those are additional requirements, not interchangeable warnings. This is the strongest first consolidation candidate.

### D2 — Memory distinctions have three descriptions

The record contract's ten-dimension coverage table overlaps with the memory report's Write side and Read-back sections and the profile's Classification units, Write agency, Read-back, and Trace learning sections. Repeated distinctions include human admission versus authorship/I/O, requested delivery versus unsolicited supply, identifiers versus actual selection, and trace-fed writes with durable results and later consumers.

Proposal: the record contract owns source-native distinctions and evidence to preserve; the memory report owns their placement and connected operational account; the profile owns controlled-value mappings and aggregation. Review clause by clause. In particular, preserve the profile-specific restriction of `read_back_signal` to push selection. Do not delete its classification table wholesale.

### D3 — Supersession grammar declared twice

The [record contract, Identity and grammar](../../agentic-system-analyses/instructions/agentic-analysis-records.md#identity-and-grammar) defines `Amendment: … is superseded by …`, identity evidence, splits, and preservation of IDs. The [reconciliation type](../../agentic-system-analyses/types/agentic-system-reconciliation-report.md#reconciliation) repeats the syntax and support requirements.

Proposal: keep the grammar in the shared contract; have the reconciliation type name supersessions under that contract. Preserve its distinct `Unresolved conflict:` and integration-disposition requirements. Small, relatively straightforward reduction.

### D4 — Small mission/type overlap

The [synthesis mission](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/synthesize-analysis.md) repeats organization around operational progression and preservation of limits across corrections, already supplied by its type and worker rules.

Proposal: optionally trim those repetitions. Low priority: the mission is already short. Keep its authority boundary against reconciling records, adding evidence, or writing verification text.

### D5 — Reading guidance overlaps and disagrees

`src/commonplace/artifactrun/handouts.py` says one tool call per batch. [Worker rules, Read the prompt](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs-engine/follow-worker-rules.md#read-the-prompt) permit grouped reads only when the tool supports complete delivery. A single-file read tool does not support the former requirement.

Proposal: retain tool-compatible generic reading guidance in the engine, which serves non-analysis consumers too. Keep analysis-specific source-reading constraints in worker rules. Fix the mismatch rather than merely deleting one copy. The separately proposed change to put worker rules before the reading they govern remains unimplemented.

## Repetitions to retain unless new evidence changes the assessment

- Verification limits and synthesis limitations govern opposite ends of an interface: emitted findings versus required carried consequences.
- Correction grammar in the record contract and correction procedure in worker rules serve different purposes.
- Actual prompt bindings such as `cites` are not redundant with definitions of their meaning.
- Templates demonstrate output shape; repeated headings and fields are not automatically duplicate normative declarations.

## Next decision

The audit recommends evaluating D1 and D3 first, then D2 with its classification-specific constraints. The operator has authorized retention here, not those edits. Before implementation, follow [method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md), verify consumer delivery, and establish which clauses move or disappear. New observations beyond this packet need their own inspected scope before supporting a repo-wide claim.
