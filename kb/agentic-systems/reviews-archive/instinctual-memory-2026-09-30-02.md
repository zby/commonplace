---
type: agentic-systems/types/generated-review.md
description: Instinctual Memory journals source events, publishes curated facts to Git, and supplies selected facts by hooks or requests; delivery is wired, while factual warrant and host use remain unestablished.
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-30-instinctual-memory-02
source-identity: https://github.com/jasonkneen/instinctual-memory
reviewed-revision: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
analysis-artifact: kb/reports/retained/agentic-system-analysis-archive/AAS-2026-09-30-instinctual-memory-02/ARTIFACT.yaml
analysis-artifact-sha256: b7a273548a14914b7eca548ff6d622b5fcf9ddeaf72b8b118fe0ae40a8c2d50e
---

# Instinctual Memory

Evidence basis: code-grounded analysis of `https://github.com/jasonkneen/instinctual-memory` at `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, with an analysis cutoff of 2026-09-30.

Evidence basis: the whole-repository boundary at Instinctual Memory commit 6acb13dc35765bf5ccfc87e445dd09c480f1c28a, with implementation and bundled design inspected but no configured deployment or observed host run (SRC-1).

Instinctual Memory appends source events to a journal, then rules or a configured language model can propose durable facts for a Git-published tree. The extractor can run after session-end backfill or through direct operator commands; caller-requested remember and correction operations provide another write path (OBJ-1, OBJ-2, RTE-1, RTE-4, RTE-5). The extraction check ties evidence text to a source event and applies schema/domain conditions, but no truth oracle or per-fact human approval is established. The semantic relation between an extracted statement and its source remains indeterminate; persistence does not amount to epistemic acceptance (EPI-RTE-1, EPI-OBJ-1, EPI-OBJ-2). Normal publication uses validated compare-and-swap; that protocol constrains writes, not factual warrant (CLM-2, RTE-4, RTE-5).

Later access comes through automatic Claude hooks, requested reads/searches, or operator-requested writeback (RTE-1, RTE-2, RTE-3, RTE-6). The start hook selects a preference by identifier; prompt retrieval uses lexical overlap and a six-fact limit. Explicit search can use relevance reranking. Eligibility, selection and ranking affect which facts are presented and in what order, not their truth status (EPI-RTE-2, EPI-RTE-3). Writeback places selected facts in a host instruction-file block. These mechanisms wire context delivery or file writing, but host loading, model uptake and behavior change were not observed (BAP-1, BAP-2, BAP-3, EPI-OBJ-4).

The runtime pass does not establish a theory route meeting conditions 1–4: it does not establish a consumed localized theory, content-directed criticism, or iteration using criticism (RTE-4). Whether criticism improves capacity for future action is uninspected. The system is not established as reflective or autonomous at this boundary, and its wired trace-fed memory path does not establish self-improvement (RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, MEM-RTE-1, EPI-OBJ-1). There is no task-level faithfulness or causal benefit evidence (MEM-CLM-1).

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No installed host, configured store, live operation, or model-service response was inspected. | SRC-1, RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7, MEM-RTE-1, MEM-RTE-2, MEM-RTE-3, MEM-RTE-4, EPI-OBJ-1, EPI-OBJ-2, EPI-OBJ-3, EPI-OBJ-4 | Repository commit 6acb13dc35765bf5ccfc87e445dd09c480f1c28a; external host/provider operation excluded. | Actual invocation, output, candidate state, host activation and successful deployment are not established. | A retained execution trace or artifact from a configured host and store, with provider interactions identified where relevant. |
| No evidence-consuming truth criterion or independent factual reviewer was identified in inspected paths. | RTE-4, RTE-5, EPI-RTE-1, EPI-OBJ-1, EPI-OBJ-2 | Same frozen repository boundary; extraction, change, validation and publication paths inspected. | No produced or caller-supplied fact is established as true or supported by its cited evidence. | A specified truth/evidence criterion and retained candidate-level results showing its application. |
| The semantic relation between extracted statements and source events is not determined by text-occurrence checks. | RTE-4, EPI-RTE-1, EPI-OBJ-1 | Consolidation/check implementation at the frozen commit; no candidate instance supplied. | Whether extraction preserves, entails, reshapes or adds propositions, and any candidate-linked discovery lifecycle, remain unresolved. | An observed candidate and source event with semantic comparison, followed by evidence for any claimed criticism or revision stages. |
| Host use and behavioral effects were outside the evidence set; the shipped retrieval evaluation scores search results. | BAP-1, BAP-2, BAP-3, MEM-CLM-1, EPI-OBJ-3, EPI-OBJ-4 | Hook, operation, writeback and evaluation paths at the frozen commit; no host session or task comparison. | Faithfulness to recalled content, downstream benefit and behavioral authority in host practice are not established. | Retained task executions comparing behavior with and without returned memory, including task outcome and exposure evidence. |
| The full set of supported ingestion adapters was not classified as trace-source categories. | MEM-RTE-1, RTE-4 | Specialist traced session-log paths and a broader but incompletely mapped adapter set within the same repository boundary. | Completeness of trace_source beyond the supported session-logs value cannot be concluded. | Adapter-by-adapter mapping of retained inputs to the controlled trace-source categories. |
