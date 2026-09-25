---
{
  "type": "note",
  "description": "DualGraph research workflow: graph-guided search and per-report context reuse, with default-path defects and bounded factual warrant.",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-25-dualgraph-01",
  "source-identity": "https://github.com/microsoft/DKI_LLM",
  "reviewed-revision": "c090b7d57e3996c8900e86fecd16085b27e07f29",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/result.md",
  "analysis-result-sha256": "8de561b3cafce86fa18e7ca691f1576f56a9f9941fa6154a9bc5a9213417c705"
}
---

# DualGraph

Evidence basis: source code and repository documentation at `c090b7d57e3996c8900e86fecd16085b27e07f29`, inspected 2026-09-25. No model-backed run or benchmark reproduction was performed.

DualGraph is a research-report workflow in the DKI_LLM repository. It maintains an outline for report organization and an evidence-linked knowledge graph for planning further searches. The ordinary sequence acquires pages, summarizes them, updates both representations, selects new queries, judges outline sufficiency, and writes sections from selected evidence and earlier report text. The inspected boundary is the named DualGraph subsystem; external model, search, reader and database implementations are excluded. [Pipeline](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/main.py#L300-L778).

The connections are inspectable, but the pinned defaults have static defects: summary-only graph extraction calls an undefined helper; Serper can receive a Pydantic field object where arithmetic expects a number; the live web path passes unsupported keywords to its imported RunConfig dataclass. These were established by source inspection, not observed execution. Demo playback branches before the live configuration construction. The defects prevent treating the downstream wiring as a demonstrated working default deployment. [Extraction](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/knowledge_graph_module.py#L1557-L1567), [search argument](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/search_module.py#L687-L695), [Serper arithmetic](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/search_module.py#L206-L212), [web configuration](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/app.py#L410-L419).

The distinctive memory route is within a report. Summaries, graph relations, outline revisions and the growing report prefix feed later calls. Graph planning combines evidence counts, topology, embeddings and model selection. Candidate reasons reach the query-selection model, whereas separate page-usefulness and semantic-merge rationales are discarded. Selected chains are marked visited before their searches execute; an end-of-round stop can therefore leave newly planned work unexecuted. Saved products and optional Neo4j persistence do not establish cross-report agent learning or complete restart recovery. [Planning](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/knowledge_graph_module.py#L2015-L2126), [writer context](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/write_module.py#L338-L412), [partial database load](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/neo4j_kg_store.py#L212-L283).

Attribution and factual acceptance remain different. Graph edges may survive without a valid evidence mapping. Semantic merging joins endpoint pairs while retaining the first relation label. The completion judge rates the root query and outline, without inspecting source evidence bodies. The ordinary writer receives selected evidence and prior prose; direct graph text is disabled by main. Citation cleanup rewrites references and removes unmapped numbers, without checking whether claims follow from cited material. Missing-link candidates are search hypotheses, not confirmed discoveries. [Graph admission](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/data_model.py#L325-L388), [merge](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/data_model.py#L462-L519), [judge](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/terminal_module.py#L74-L142), [writer call](https://github.com/microsoft/DKI_LLM/blob/c090b7d57e3996c8900e86fecd16085b27e07f29/DualGraph/deepresearch/baselines/main.py#L769-L778).

The normalized memory profile records wired trace-fed reuse, per-task online scope, and natural-language/symbolic content. Its push-signal classification remains explicitly incomplete because topology and evidence-count selectors lack faithful controlled tokens. No recalled-content experiment or criticism-linked improvement was admitted. A limited task-level reflection route represents accumulated knowledge and search progress to steer later work; a revised theory of the workflow's organization and measured self-improvement remain unestablished.

## Scope

This review characterizes a frozen architecture, not factual performance or deployed reliability. The README's benchmark claims remain attributed claims. Corrected default paths and candidate-linked execution would establish a different operational boundary; controlled interventions would be needed to attribute benefits to retained context.

---

Relevant Notes:

- [Exact analysis result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-dualgraph-01/result.md) — see-also: canonical records, retained quotations, both lenses and normalized comparison fields.
