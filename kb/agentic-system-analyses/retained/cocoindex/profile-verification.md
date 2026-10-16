---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of CocoIndex's ten memory-comparison axes against the handed records at the frozen revision."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
---

# CocoIndex profile verification

## Verification

Checked all ten axes, their findings, evidence bases, classification units and coverage assessments in [the memory profile](memory-profile.md#comparison-rationale). The profile supports bounded comparison findings, not a complete inventory. All axes retain partial coverage. No source reads were needed; this judgment uses the handed records and their annotations. No supersession changes their identities.

- **Storage substrate:** Internal LMDB supports `kv`; PostgreSQL supports `rdbms`, independently of vector encoding. The alternate image-search record supports the local Qdrant `vector` finding without establishing every producer's storage. Generic payload and alternate-output coverage remains unresolved. See [MEM-OBJ-function-memoization](memory.md#mem-obj-function-memoization), [MEM-OBJ-doc-vector](memory.md#mem-obj-doc-vector) and [MEM-RTE-alternate-search](memory.md#mem-rte-alternate-search).
- **Representational form:** Text, fixed-rule fields and dense numerical representations are distinguished by operative part and consumption. The grouped manual unit identifies descriptions separately from API structure and counts in its finding notes. Symbolic envelopes do not classify opaque payloads. See [MEM-OBJ-doc-embedding](memory.md#mem-obj-doc-embedding), [MEM-OBJ-session-embedding](memory.md#mem-obj-session-embedding), [EPI-OBJ-module-info](epistemic.md#epi-obj-module-info), [EPI-OBJ-module-counts](epistemic.md#epi-obj-module-counts) and [MEM-OBJ-state-handle](memory.md#mem-obj-state-handle).
- **Lineage:** Acquisition, transcript extraction and local compilation have separate warrants. Known local derivation does not resolve upstream context-summary creation, initial state provenance or embedding-model provenance. See [MEM-OBJ-session-embedding](memory.md#mem-obj-session-embedding), [MEM-OBJ-doc-vector](memory.md#mem-obj-doc-vector) and [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction).
- **Behavioral authority:** Search recipients receive reference material; vectors and filing features influence ranking; memo dependencies and bookkeeping affect execution selection and cache admissibility. Pair-decision fields select canonical-map operations. These findings name actual consumers rather than deriving standing instruction or learning authority from retention alone. See [RT-RTE-query-index](runtime.md#rt-rte-query-index), [MEM-RTE-alternate-search](memory.md#mem-rte-alternate-search), [MEM-RTE-function-reuse](memory.md#mem-rte-function-reuse), [MEM-OBJ-tracking-info](memory.md#mem-obj-tracking-info) and [EPI-RTE-pair-disposition](epistemic.md#epi-rte-pair-disposition).
- **Write agency:** Software admission is supported for the inspected indexing, extraction, memo and counter mechanisms. The counter finding concerns test wiring, not a passing execution. Generic caller control and alternate producers remain unresolved; operator startup is not classified as manual content approval. See [RT-RTE-index-update](runtime.md#rt-rte-index-update), [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction), [MEM-RTE-function-reuse](memory.md#mem-rte-function-reuse) and [MEM-RTE-state-access](memory.md#mem-rte-state-access).
- **Curation operations:** Tracked replacement of existing indexed entries supports `evolve`. The profile does not infer consolidation from text filtering, synthesis from opaque extraction, or retained-history invalidation from physical deletion. Its unresolved transformation units make no absence assertion. See [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance), [MEM-RTE-session-search](memory.md#mem-rte-session-search), [MEM-OBJ-tracking-info](memory.md#mem-obj-tracking-info) and [RT-RTE-drop-app](runtime.md#rt-rte-drop-app).
- **Read-back direction and signal:** Requested search, diagnostics and keyed state access support pull at their respective bases. Automatic memo substitution supplies a retained result to a computation request, supporting push; stable-path or fingerprint matching selects the actual retained entry and supports identifier selection. Requested search ranking is not relabeled as a push signal. Uninspected readers remain unresolved on both axes. See [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization), [MEM-RTE-function-reuse](memory.md#mem-rte-function-reuse), [MEM-RTE-state-access](memory.md#mem-rte-state-access) and [MEM-RTE-inspect-state](memory.md#mem-rte-inspect-state).
- **Trace learning and trace source:** The session route automatically transforms conversational traces into retained text and numerical retrieval representations, then delivers derived snippets on a later invocation. This meets the profile's trace-fed artifact-and-consumer definition at wired strength; it does not establish improved capacity or answering-agent use. Conversational turns support `session-logs`; packaging and role labels do not independently support event streams or tool traces. Unknown summary generation and other writes remain unresolved. See [MEM-OBJ-session-embedding](memory.md#mem-obj-session-embedding) and [MEM-RTE-session-search](memory.md#mem-rte-session-search).

The reconciliation's unresolved pair-retention attribution does not invalidate the profile's symbolic decision, local inference lineage or canonical-selection findings. The profile expressly withholds attribution to a specific memo container. The conflicting component-versus-function references therefore remain bounded rather than silently resolved. See [EPI-RTE-pair-proposal](epistemic.md#epi-rte-pair-proposal), [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization) and [MEM-OBJ-function-memoization](memory.md#mem-obj-function-memoization).

No finding claims observed operation or causal benefit. The unresolved included alternatives prevent complete-value comparisons, but that uncertainty is already expressed in the profile's assessments and notes. It is not an additional verification defect.

## Blockers

none

## Limits

none
