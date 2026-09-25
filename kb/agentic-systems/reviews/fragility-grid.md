---
type: types/note.md
description: fragility-grid evaluates fixed items across prompt and scoring configurations;
  retained files support analysis and resume, with provenance and completion limits
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-fragility-grid-01
source-identity: https://github.com/NikolaTesla-007/fragility-grid
reviewed-revision: 3f51444ead009d8351de1b6b19bf901c4da3d420
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-fragility-grid-01/result.md
analysis-result-sha256: 70d8208bdae0dedbb7f16efd1e23d0c699c5f3e3ec5d5bbad313553daf88ec9f
---

# fragility-grid collection and resume subsystem

fragility-grid is a returning evaluation computation. It runs fixed multiple-choice items across prompt formats, option permutations and two likelihood scorers, then retains per-item correctness and summaries. This review covers the collector, consumed helpers, shell resume driver and downstream file loader. Full statistical methods, published empirical results and external model/dataset implementations are excluded. No autonomous agent boundary is inferred.

The default grid has 24 generation cells and two likelihood cells. Generation requests short greedy answers, extracts a letter or digit, maps its shown position back to the original option and checks the dataset gold answer. Unparsed output counts as wrong. Likelihood instead scores option continuations after a cloze stem and checks the highest mean token score. Deterministic regex parsing does not guarantee intended-answer extraction, and these scoring methods are distinct operational tests. See [generation and likelihood paths](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_grid.py#L54-L105) and [parsers](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/prompt_format_lib.py#L46-L54).

Memory here consists of operational files. Records retain question, gold, correctness bits, one score margin and parse counts; CPU analysis later requests those records. The shell requests summary-file status and skips models whose summary exists. Retained evidence never becomes guidance in the inspected model-input paths, so trace learning is absent within this boundary. Static datasets and pretrained weights are separate from memory accumulated through use. See [record writing](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_grid.py#L107-L176) and [later loader](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_analysis.py#L35-L55).

Resume is a filename-existence check, not validated completion. Direct final-path writes can leave partial files, and changed settings do not invalidate an existing summary. The loader accepts matching files without a run manifest, while a shared legend can be overwritten and later reconstructs configuration keys from current source. These paths permit stale or mixed inputs; no such incident was observed here. See [shell skip](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/run_fragility.sh#L55-L68) and [legend consumer](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/fragility_analysis.py#L300-L305).

The source commit fixes orchestration code, while model/tokenizer and dataset calls resolve names without immutable revision arguments. Retained records omit full options, raw answers, full score vectors and resolved asset hashes. Seeds and greedy decoding therefore establish explicit controls, not complete reproduction evidence across environments. HF and vLLM also differ in context handling and recovery. See [inference setup](https://github.com/NikolaTesla-007/fragility-grid/blob/3f51444ead009d8351de1b6b19bf901c4da3d420/repro/inference.py#L47-L108).

The supported contribution is inspectable measurement across a specified configuration grid. Its correctness and fragility labels depend on supplied gold, parser interpretation and chosen cells; they do not by themselves establish model uncertainty or explain a ranking. Narrow operational reflection is wired through completion-file state affecting later scheduling. Conjectural learning, self-improvement and empirical effects remain uninspected. No model calls or benchmarks were run; controlled asset-pinned executions with complete provenance would resolve different questions from this source analysis.

The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-fragility-grid-01/result.md) contains the full route inventory, source quotes, memory comparison, epistemic analysis and limitations.
