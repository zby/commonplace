---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of EAL-Bench's authorization-memory workflow at the frozen source revision."
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
reviewed-boundary: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
---

# EAL-Bench report verification

## Verification

The pinned reports support a bounded implementation account. No material contradiction or unsupported central conclusion requires correction. The incomplete alternative-path inventory below is a publication limit, not evidence of absent mechanisms.

I read all supplied members, types, correction-answer files and the record contract. The correction-answer files are empty and the supplied structural check reports `none`; there is no structural failure to route. I checked the meaning and evidence of every declared record, the annotations, epistemic ledger rows, containment distinctions, the one supersession and the reconciliation's integration dispositions. I independently read source consumers and intervening transformations rather than accepting the analysts' validation statements as verification. SRC-1 HEAD equals the boundary revision and its worktree is clean. All additional evidence is implementation or explicitly identified doctrine/design at that revision; no target execution or observed benefit was established.

### Runtime, memory and delivery

- [RT-RTE-study-execution](runtime.md#rt-rte-study-execution) and [workflow's selected branch](workflow.md#workflow-account) match the ordinary Procurement job builder and shared-engine progression. SRC-1 `domains/procurement/studies/routes.py` pairs generated evidence with case probes; `experiments/authorization_memory/study_engine.py` prepares callbacks, freezes the handoff, optionally pauses, runs jobs and persists completion or failure. The representative workflow does not claim to exhaust the diagnostic expansion. Its empty fallback is supported by `experiments/authorization_memory/langmem_writer.py`, not an invented successful writer update.
- [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission), [MEM-OBJ-memory-artifact](memory.md#mem-obj-memory-artifact), [MEM-OBJ-memory-attempt](memory.md#mem-obj-memory-attempt) and [RT-BAP-profile-update](runtime.md#rt-bap-profile-update) are supported by manager construction, result/underlying-call validation, payload validation, artifact construction and update-state processing in SRC-1 `experiments/authorization_memory/langmem_writer.py`. Profile identity, structural acceptance, no-change, failed-update retention and bounded repair are distinct. Citation visibility and enabled token capacity do not test semantic authorization. Freezing copies payload and sets source history to null. Audit diagnostics do not thereby reach the executor.
- [RT-RTE-executor-score](runtime.md#rt-rte-executor-score) and [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence) match SRC-1 `experiments/authorization_memory/pipeline.py` and `domains/procurement/adapter.py`: selected evidence is serialized into a fresh request frame, whereas scoring consults the independent encoded ledger. Multiple calls with a selected terminal call become invalid; no selected terminal call is no-action. The scorer records decisions rather than dispatching transactions. [RT-RTE-alternate-consumers](runtime.md#rt-rte-alternate-consumers) preserves the important counterexample: SRC-1 `src/eal_bench/llm/client.py` invokes supplied handlers, while `src/eal_bench/eval/scoring.py` delegates to benchmark scoring and `src/eal_bench/eval/inspect_adapter.py` generates without resolving tools. No universal transaction-veto guarantee follows.
- [RT-OBJ-executor-plan](runtime.md#rt-obj-executor-plan), [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume) and [MEM-RTE-saved-replay](memory.md#mem-rte-saved-replay) have distinct referents and supported returns. SRC-1 `experiments/authorization_memory/resume.py` verifies hashes, reconstructed plans and saved calls, rejects reviewer-backed checkpoints and schedules missing calls. SRC-1 `experiments/writer_variants_run.py` instead starts replay from completed saved evidence and filters ordinary writer evidence to generated-final IDs. Neither establishes exactly-once provider execution or trusted filesystem isolation.
- [RT-RTE-candidate-selection](runtime.md#rt-rte-candidate-selection) matches SRC-1 `domains/procurement/studies/writer_ttc.py`: blinded whole-candidate model selection differs from deterministic minimum field-error selection with index tie-breaking. The reports correctly avoid equating relative minimum error with correctness or reliable reviewer compliance.
- [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate) is supported by SRC-1 `experiments/mitigations/source_authority/gate.py`. Empty citations fail; all citations must pass visibility and source-capability checks. Scope entailment is not checked. SRC-1 `experiments/mitigations/source_authority/study.py` confirms memory's additional implementation evidence for paired original/gated jobs and separate diagnostics. Runtime's narrower inspection statement is not a competing finding.
- [RT-RTE-event-admission](runtime.md#rt-rte-event-admission), [MEM-OBJ-event-log](memory.md#mem-obj-event-log), [MEM-OBJ-reduced-state](memory.md#mem-obj-reduced-state) and [MEM-RTE-event-recovery](memory.md#mem-rte-event-recovery) match SRC-1 `experiments/mitigations/event_sourcing/core.py` and `experiments/mitigations/event_sourcing/runtime.py`. Validation changes a cloned reducer, checks reduced-state capacity and returns a candidate; finalization retains events and snapshots separately. Restoration replays events and compares saved records. The writer receives compact prior state and the current block, not the cumulative archive. Replay consistency does not certify the source interpretation.
- [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback) matches SRC-1 `experiments/closed_loop.py`: trial-derived content becomes a seeded writer update and the resulting current artifact reaches successor requests. The neutral arm and final-step termination are real conditions, not footnotes. Optional action logs change context. The reports preserve the distinction between this feedback wiring and activated learning or improvement.

The four hosted-model roles—[RT-CMP-writer-model](runtime.md#rt-cmp-writer-model), [RT-CMP-executor-model](runtime.md#rt-cmp-executor-model), [RT-CMP-reviewer-model](runtime.md#rt-cmp-reviewer-model) and [EPI-CMP-annotation-model](epistemic.md#epi-cmp-annotation-model)—are invocation roles, not claims of distinct weights. Their inference interfaces and unresolved provider/version mutability are consistent with SRC-1 `experiments/authorization_memory/langmem_writer.py`, `src/eal_bench/llm/client.py`, `domains/procurement/studies/writer_ttc.py` and `experiments/annotate_authorization_memories.py`. No parameter-update or immutable-weight claim is inferred from target names.

### Epistemic objects, authority and reconciliation

[The epistemic inventory and ledger](epistemic.md#epistemic-object-inventory) distinguish ledger reference truth, typed and prose content, extracted annotation state and evaluation products. Their source anchors support those different consumers. In particular, SRC-1 `src/eal_bench/eval/preservation.py` separately computes fidelity and apparent authority, resolving prose only through accepted matching-hash agreeing annotations. [EPI-RTE-memory-assessment](epistemic.md#epi-rte-memory-assessment) therefore measures encoded permissions, not independently verified organizational truth.

[EPI-RTE-annotation-extraction](epistemic.md#epi-rte-annotation-extraction) and [EPI-RTE-annotation-admission](epistemic.md#epi-rte-annotation-admission) match the memory-only request, tool/schema parser and saved child-run production in SRC-1 `domains/procurement/studies/annotations.py` and `experiments/annotate_authorization_memories.py`, followed by the public resolver. Optional human sample output is not a completed review. Agreement and parser acceptance cannot establish extraction fidelity.

[EPI-RTE-variant-construction](epistemic.md#epi-rte-variant-construction) is supported by SRC-1 `src/eal_bench/eval/propagation.py`: list widening supplies a concrete non-entailing permission alteration. The report restricts its ampliative classification to widening rather than claiming every recipe has that relation. [EPI-RTE-failure-attribution](epistemic.md#epi-rte-failure-attribution) matches SRC-1 `src/eal_bench/eval/end_to_end.py`: formation, denied requested action behind written memory and no such action behind the exact arm are required; missing/provider-failed arms withhold attribution. The optional expected population and unauthenticated caller chronology remain material qualifications. Deterministic derivation licenses these local predicates, not causal identification or model-mechanism explanation.

[RT-CLM-memory-attribution](runtime.md#rt-clm-memory-attribution) and [EPI-CLM-benchmark-test](epistemic.md#epi-clm-benchmark-test) accurately attribute SRC-1 `docs/reusable_api.md` and `README.md`. The claim comparison does not turn research intent into observed results. The ledger correctly separates checking, disposition and retention, and does not infer semantic acceptance or lifecycle integration from persistence. Its uncertain model-mediated transformations are not falsely classified as proven conjectures or faithful compression.

[Reconciliation](reconciliation.md#reconciliation) preserves a valid artifact container alongside typed/prose payload parts and event-derived snapshots. I found no conflicting containment assignment or unsupported required-part substitution. The supersession of [MEM-OBJ-annotation](memory.md#mem-obj-annotation) by [EPI-OBJ-annotation-state](epistemic.md#epi-obj-annotation-state) connects their shared extracted-state/status/hash consumer without erasing generic-caller uncertainty. The plan, audit, event history and compact payload remain distinct. All integration issues receive compatible dispositions; no unresolved disagreement is concealed by selecting a stronger status.

### Consequential omission questions and stopping decision

The frozen top-level tree and producer/consumer dependencies guided three challenges beyond the listed quotations: could an alternate shipped writer change context or artifact-form conclusions; could saved annotations or outcomes have a later consumer omitted from the account; and could a scoring integration actually dispatch effects? The annotation producer, feedback successor, event restoration, public/Inspect scorer and generic handler reads above settle the latter two without requiring narrower central claims.

The first question located additional concrete mechanisms already named as uninspected in [memory's coverage](memory.md#boundary-and-evidence): SRC-1 `experiments/authorization_memory/writing_methods.py` selects earlier messages by BM25 and periodically rebuilds from source history; `experiments/authorization_memory/hybrid_memory.py` adds prose notes to typed records. SRC-1 `experiments/writer_variants_run.py` wires these options into writer chains and later base-domain executor jobs. Manager construction in `experiments/authorization_memory/langmem_writer.py` honors the rebuild flag by supplying an empty existing profile. These are implementation findings, not evidence of successful runs.

> picked = sorted(BM25Index([turn_text(t) for t in earlier]).top(" ".join(turn_content(t) for t in block.turns), writer_retrieval_k))
> --- `experiments/authorization_memory/writing_methods.py`

> _profile_from_current(
>     domain,
>     chain,
>     empty=update.rebuild_from_history,
> ),
> --- `experiments/authorization_memory/langmem_writer.py`

The hybrid implementation explicitly separates record scoring from notes:

> return self.base_fidelity.compare(case, self.memory.records(remembered), through_block_index, prior_snapshots)
> --- `experiments/authorization_memory/hybrid_memory.py`

These alternatives do not contradict the reports' explicitly partial inventory or route-local baseline assertions. They do prevent treating that inventory as a complete comparison of retrieval, rebuild and mixed-form memory. Further optional expansion stopped here: the identified challenges have supported dispositions, and broader maintenance, pressure, diagnosis and domain-oracle audits would refine explicitly withheld comparisons rather than settle an outstanding material contradiction. Available unread artifacts are not evidence of absence. The boundary's missing primary archives still prevent independent reconstruction of the published runs; no claim in these members depends on having done so.

## Blockers

none

## Limits

- The alternate writer inventory remains partial. [MEM-OBJ-memory-artifact](memory.md#mem-obj-memory-artifact), [memory's integration issues](memory.md#integration-issues) and [epistemic coverage](epistemic.md#source-and-claim-boundary) do not separately inventory BM25-supplied earlier messages, periodic empty-profile source-history rebuilds, or hybrid prose notes that are stripped for record fidelity but retained in executor-visible payloads. SRC-1 `experiments/authorization_memory/writing_methods.py`, `experiments/authorization_memory/hybrid_memory.py`, `experiments/writer_variants_run.py` and `experiments/authorization_memory/langmem_writer.py` support these mechanisms as traced above. Readers may retain the positive baseline, admission, feedback and scoring findings, but must withhold exhaustive comparisons of working-context selection, all read-back routes and mixed-form artifact checks. No emitted complete-coverage or absence value needs repair.
