---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of SkillRL's memory comparison against the accepted records at the frozen source boundary."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
---

# SkillRL profile verification

## Verification

Checked all ten axes in the [profile](memory-profile.md#comparison-rationale), including each unit's scope, coverage assessment, positive findings and evidence basis. The profile uses the canonical skill-content object after reconciliation; the cleanup and abstraction stages remain parts of the SFT production container, and withdrawal remains an afforded operation rather than a wired cleanup workflow. No source reads or new evidence were needed.

Storage and representation findings distinguish instruction text, access fields, numerical vectors, SFT artifacts and actor parameters. The file, live-memory, vector and model-weight findings are supported by [MEM-OBJ-skill-content](memory.md#mem-obj-skill-content), [MEM-OBJ-skill-metadata](memory.md#mem-obj-skill-metadata), [MEM-OBJ-experience-records](memory.md#mem-obj-experience-records), [MEM-OBJ-retrieval-index](memory.md#mem-obj-retrieval-index), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-RTE-sft-production](runtime.md#rt-rte-sft-production) and [RT-RTE-policy-update](runtime.md#rt-rte-policy-update). Some units combine several parts, but their findings identify the text, structural and numerical parts separately. Uncertainty about initial provenance does not prevent classifying their recorded forms. The partial storage assessment preserves unaudited numerical serialization alternatives.

Lineage and write agency retain the distinction between known transformations and unresolved initial admission. Trace extraction and automatic admission follow the two dynamic admission routes and [MEM-RTE-trace-abstraction](memory.md#mem-rte-trace-abstraction). Import and compiled-vector findings describe different derivation paths. Generic callers of [MEM-RTE-bank-maintenance](memory.md#mem-rte-bank-maintenance) and [MEM-RTE-experience-save](memory.md#mem-rte-experience-save) do not establish manual agency. Starting a run is not per-content approval. The profile does not turn those unresolved alternatives into negative findings or complete coverage.

Behavioral authority is predominantly classified at the actual consumer: instruction text at the policy, experience display as context, retained vectors/text at ranking, and retained IDs/categories at admission or selection. Existing-ID vetoes are supported on the wired admission chain even though direct maintenance also exists as an affordance. The finding does not promise semantic deduplication or within-call uniqueness. Withdrawal retains its afforded basis and cached-selection limit. Learning authority at fitting and SFT transformation consumers does not imply the same controlled authority for successor actor weights; their downstream generative force remains not-determinable. One partial-inventory omission is retained below.

Curation findings follow transformations rather than names: [EPI-RTE-trajectory-cleanup](epistemic.md#epi-rte-trajectory-cleanup) supports action-window deduplication; [MEM-RTE-trace-abstraction](memory.md#mem-rte-trace-abstraction) supports reduction to patterns and rules; [EPI-RTE-skill-withdrawal](epistemic.md#epi-rte-skill-withdrawal) supports afforded forgetting, not history-preserving invalidation. Requests for new rules do not independently establish synthesis. Unresolved generated semantics and alternative repair stages remain explicit, so the positive findings assert neither faithfulness nor a complete curation inventory.

Read-back direction separates manager requests from automatic supply to the policy. Both pull and push are supported by [RT-RTE-environment-rollout](runtime.md#rt-rte-environment-rollout) and [MEM-RTE-experience-selection](memory.md#mem-rte-experience-selection); this does not create a foreground policy memory tool. Recorded SFT file consumers and checkpoint resume support requested reads. The heuristic save finding stays afforded and does not establish a live saver-to-selector loop. Push signals identify reset triggers, task/category or embedding inputs, and supplied retained bodies. Coarse slices and lexical category detection remain distinct from embedding ranking. Neither file paths nor dynamic prefixes establish exact-identity push. Uninspected alternative context delivery prevents complete signal coverage; requested-read units alone are locally inapplicable.

Trace learning and source classify automatic experience-fed durable writes with later consumers, not demonstrated improvement. Dynamic skill admission, inspected offline/SFT transformation and numerical fitting support wired positive findings. Their original linked environment experience supports trajectories even when a downstream update consumes only a bounded projection. The profile does not infer session logs, tool traces or event streams from formatting or incidental tool use. Unresolved initial and caller-driven alternatives preserve partial coverage. Neither observed operation nor causal benefit is asserted on any axis.

## Blockers

none

## Limits

- The partial behavioral-authority inventory omits a separate learning-authority finding for failure excerpts at the updater and for supplied derived experience at the original offline bank generator. [RT-RTE-validation-admission](runtime.md#rt-rte-validation-admission), [RT-RTE-training-admission](runtime.md#rt-rte-training-admission) and [RT-RTE-offline-production](runtime.md#rt-rte-offline-production) establish those inputs feeding automatic durable instruction writes with later policy consumers; the profile's corresponding trace-learning positives already retain the chains. The omission leaves the emitted system-level learning value and downstream instruction finding supported, but consumers should withhold complete unit-level comparisons of learning authority across skill-production routes. The axis is already partial, so this local omission does not imply absent authority or complete coverage.
