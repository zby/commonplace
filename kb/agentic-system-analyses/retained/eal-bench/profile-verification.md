---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of EAL-Bench's memory comparison against accepted records at the frozen revision."
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
reviewed-boundary: "51648690bc52d7a9c7ac080a2c67a784fe9d56cb"
---

# EAL-Bench profile verification

## Verification

Checked all ten axes in [the memory profile](memory-profile.md#comparison-rationale), including their findings, evidence bases, named units and coverage assessments. The profile uses the accumulated-memory boundary rather than treating all runtime storage or hosted inference weights as memory. Each axis remains partial; the included uninspected study and maintenance alternatives are not converted into absences. No source reads or new evidence were needed.

**Storage and form.** File-backed and process-resident findings are supported by [MEM-OBJ-memory-artifact](memory.md#mem-obj-memory-artifact), [MEM-OBJ-memory-attempt](memory.md#mem-obj-memory-attempt), [MEM-OBJ-event-log](memory.md#mem-obj-event-log), [MEM-OBJ-reduced-state](memory.md#mem-obj-reduced-state), [RT-OBJ-executor-plan](runtime.md#rt-obj-executor-plan) and [EPI-OBJ-annotation-state](epistemic.md#epi-obj-annotation-state). The profile distinguishes symbolic parsing/reduction from model-interpreted consumption and separates repair text from audit fields. Generic caller persistence remains unresolved rather than inheriting the shipped annotation child's file storage.

**Lineage and agency.** Feedback extraction, event reduction, deliberate diagnostic authorship, saved-evidence transfer and annotation interpretation retain distinct derivation paths. The feedback lineage finding is explicitly bounded to descendants, with initial history provenance unresolved. Automatic agency follows model/software content admission, not physical writes or operator launch. The annotation object uses the canonical epistemic declaration after the supplied supersession; that identity resolution does not erase uncertainty about generic callers. See [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback), [MEM-RTE-event-recovery](memory.md#mem-rte-event-recovery), [MEM-RTE-saved-replay](memory.md#mem-rte-saved-replay), [EPI-RTE-variant-construction](epistemic.md#epi-rte-variant-construction) and [EPI-RTE-annotation-admission](epistemic.md#epi-rte-annotation-admission).

**Authority and curation.** Executor/profile context, feedback consumption, candidate ranking and checkpoint/annotation eligibility have supported consumer-specific forces. Checkpoint enforcement is not attributed to remembered authorization claims. Compression is conservatively afforded for model writing, while replacement, lifecycle reduction, withdrawal and diagnostic widening have wired effects. Widening's synthesis finding is supported by the explicit non-entailing permission change in [EPI-RTE-variant-construction](epistemic.md#epi-rte-variant-construction); erroneous extraction alone is not treated as synthesis. [RT-RTE-authority-gate](runtime.md#rt-rte-authority-gate) and its memory annotation support retained original/filtered arms without implying semantic correctness. One local authority omission is retained below.

**Read-back and selection.** Requested saved replay, checkpoint continuation and event restoration support pull; automatic model-context preparation supports push. Requested return is not counted again as unsolicited delivery. The identifier findings name chain, case/job and pool associations that select delivered content, rather than merely file labels. Model judgment selects a whole candidate; the profile does not relabel symbolic gold-fidelity comparison as model judgment. See [RT-RTE-writer-admission](runtime.md#rt-rte-writer-admission), [RT-RTE-candidate-selection](runtime.md#rt-rte-candidate-selection), [RT-BAP-memory-evidence](runtime.md#rt-bap-memory-evidence) and [MEM-RTE-saved-replay](memory.md#mem-rte-saved-replay).

**Trace learning and source.** [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback) supports automatic trial-fed revision of retained context consumed by later requests. This establishes a wired qualifying route without observed improvement or parameter training. Tool-decision/payload and scoring feedback support the emitted tool-traces source. Synthetic conversation formatting does not establish session-log or event-stream origin. Other source provenance remains unresolved, and no global negative or inapplicability is emitted.

The grouped units are sometimes coarse, but their notes preserve consequential branch distinctions and uncertainty. No unsupported emitted comparison value, evidence upgrade or system-complete coverage claim was established. Missing execution evidence limits observed and causal conclusions, not the positive wiring findings.

## Blockers

none

## Limits

- The partial behavioral-authority inventory in [the memory profile](memory-profile.md#comparison-rationale) lists validation for the retained event log at reducer recovery but omits its enforced rejection consequence. [MEM-RTE-event-recovery](memory.md#mem-rte-event-recovery) establishes that inconsistent replayed/saved records reject restoration; [MEM-OBJ-event-log](memory.md#mem-obj-event-log) identifies the consumed retained events. Withhold complete consumer-by-consumer authority comparisons for event recovery. This local omission does not invalidate the listed validation finding or change the supported system-level existence of enforcement, already established separately by [RT-RTE-checkpoint-resume](runtime.md#rt-rte-checkpoint-resume). The authority axis remains partial, so publication need not assert a complete route inventory.
