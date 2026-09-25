---
type: types/note.md
description: 'OpenViking session and user-memory subsystem: queued extraction, cumulative
  continuation and bounded recall with explicit host/training exclusions'
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-openviking-01
source-identity: https://github.com/volcengine/OpenViking
reviewed-revision: 4edc30b068934893bc94a4e1b8e87bab2100bce5
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-openviking-01/result.md
analysis-result-sha256: 1e8ba47630396c1649ccfa715649a31185f4c74fa14446e52226a189993a63af
---

# OpenViking session and user memory

Evidence basis: implementation and shipped documentation at [4edc30b068934893bc94a4e1b8e87bab2100bce5](https://github.com/volcengine/OpenViking/tree/4edc30b068934893bc94a4e1b8e87bab2100bce5), inspected 2026-09-25. No system execution or causal experiment was performed.

OpenViking's inspected subsystem converts session traces into retained continuation and user-memory material, then serves it to later model/client consumers. Session commit has two distinct outcomes: it first archives and queues work, then background processing generates summaries and applies memory operations. The returned task handle reports archive acceptance; it does not establish completed extraction. See RTE-2 in the [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-openviking-01/result.md).

> "status": "accepted",
> "task_id": task_id,
> "archive_uri": archive_uri,
> "archived": True,
> --- https://github.com/volcengine/OpenViking/blob/4edc30b068934893bc94a4e1b8e87bab2100bce5/openviking/session/session.py

The continuation path retains cumulative Working Memory and partial-turn checkpoints. Checkpoints are matched to retained message anchors; the latest summary and active messages are selected under a budget. These derived records can affect later context. The separate user-memory extractor normally omits tool output, even though Working Memory consumes hydrated tool evidence. An accepted previous-overview parameter does not establish that the user extractor actually inserts it into its conversation. These distinctions are recorded on OBJ-2, OBJ-5, RTE-2 and RTE-3.

> When Turn-budget retention keeps a still-active User Turn but archives the
> assistant/tool steps that overflow the budget, Phase 2 records a bounded
> cumulative *checkpoint* summary for that Turn. Context assembly later re-injects
> the checkpoint as a synthetic ``ContextPart`` right after the retained anchor,
> so the model keeps continuity without replaying the archived raw steps.
> --- https://github.com/volcengine/OpenViking/blob/4edc30b068934893bc94a4e1b8e87bab2100bce5/openviking/session/checkpoints.py

Extraction and merge models propose memory changes; scope, identity-resolution and patch rules constrain application. Failed field merges may preserve the old field, and operation-level failures can coexist with other applied changes. Stored differences support inspection; this analysis does not establish automatic semantic rollback or a transaction that either accepts every proposed belief or none. Schema consistency and writable identity do not verify the truth of a remembered assertion.

Read-back includes requested find/search/context blocks and distinct automatic supply to internal models. The query planner receives selected session history; extraction and merge prefetch supply existing records without a model request for each one. Optional recall bookkeeping suppresses recently returned URIs. The request-time digest is not counted as durable memory. RTE-4 through RTE-9 preserve these different consumers, selectors and authority limits.

Automatic retained summaries, checkpoints and extracted user memory support a wired trace-learning route under the analysis's memory-write definition. They do not demonstrate improved answers or conjectural learning. Physical storage alternatives, arbitrary image/tool payload form, aggregate task horizon and executed recall faithfulness remain explicitly uncertain. Reflection and achieved self-improvement are also uninspected at this subsystem boundary; session traces often describe an excluded client agent.

## Scope

This is a subsystem analysis, not an assessment of the complete OpenViking platform. It excludes optional agent-evolution/training, session skill extraction, resource/wiki compilation, bot/plugin loops, benchmark experiments and arbitrary client-host stores. Their capabilities are not judged absent. Provider weights, deployed authentication/grants and actual host adoption were not inspected. The strongest supported result is a wired retention-and-later-consumption path with separate persistence, selection and content-warrant limits.
