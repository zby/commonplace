---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AgentFly's shipped planner–executor runtime, case-memory drivers, retriever training and MCP tools at commit 42fbbcac63dd58ed6856c0761357345a58e4f032."
run-id: AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/Agent-on-the-Fly/AgentFly
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/agentfly-bbfc9fb2d5c7/related-systems/Agent-on-the-Fly--AgentFly
  revision: 42fbbcac63dd58ed6856c0761357345a58e4f032
  sha256: null
---

# AgentFly boundary

## Boundary and evidence

This run characterizes the shipped agent runtime and its experience-reuse loop, not only the memory retrieval APIs. The normalized target identity remains AgentFly. The frozen repository's README calls the project Memento and its package metadata uses `memento`; those are source-native names, not authorization to substitute another repository (SRC-1, `README.md`, `pyproject.toml`).

The target is in scope as an **enclosing runtime** with a **whole-system** boundary. Its shipped clients issue planner and executor model calls, discover MCP tools, execute model-selected calls and return task results to the planner. The interactive entry points and the benchmark/memory drivers are part of the target, not excluded host applications. Initial tracing covered all four client entry points, both retrieval implementations, the memory writers and reloaders, the LLM judges and the retriever training entry point (SRC-1, `client/agent.py`, `client/agent_local_server.py`, `client/no_parametric_cbr.py`, `client/parametric_memory_cbr.py`, `memory/np_memory.py`, `memory/parametric_memory.py`, `memory/train_memory_retriever.py`).

The runtime classification rests on executable control flow, not the README's architectural labels. For example, the baseline client owns both model backends:

> self.meta_llm = OpenAIBackend(meta_model, is_azure)
> self.exec_llm = OpenAIBackend(exec_model, is_azure)
> --- `client/agent.py`

It consumes tool calls within its executor loop:

> session = self.sessions[t_name]
> result_msg = await session.call_tool(t_name, t_args)
> result_text = str(result_msg.content)
> --- `client/agent.py`

The functional boundary includes query intake, shipped planner/executor prompts, temporary conversation state, tool-schema admission and dispatch, case retrieval and prompt construction, judgment-dependent case writes, result persistence, subsequent memory reload and reuse, and the separate retriever training/evaluation program. The parametric driver itself closes the persistence/reload path (SRC-1, `client/parametric_memory_cbr.py`):

> case_label = "positive" if is_correct else "negative"
> save_memory_entry(q, rec.plan_json or "", case_label)
>
> client._load_memory()
> --- `client/parametric_memory_cbr.py`

Training is included as a shipped improvement plane; its presence does not establish an automatically scheduled training cycle. The standalone training program and inference checkpoint loader both belong to this boundary (SRC-1, `memory/train_memory_retriever.py`, `memory/parametric_memory.py`). The MCP servers include model-dependent page extraction and media analysis as well as returning tools, workspace persistence and interpreter backends. They are not reduced to external black boxes merely because clients communicate through stdio (SRC-1, `server/ai_crawl.py`, `server/image_tool.py`, `server/video_tool.py`, `server/code_agent.py`).

### Repository coverage

The tracked tree at the frozen commit supplies the coverage inventory. “Included” means within the functional/evidence boundary, not an assertion that every line has already been analyzed. Searches inspected server registrations, imports, entry points and interpreter interfaces; direct reads traced the core state loop. Available material awaiting deeper reading is distinguished from unavailable evidence.

| Top-level tracked path | Treatment and role | Initial inspection and limits |
|---|---|---|
| `.env.example` | Included: provider, model and memory configuration surface. | Read completely; configured secrets and deployed endpoints are not supplied. |
| `.gitignore` | Excluded: checkout hygiene. | Tree inventory only; no conclusion about ignored local artifacts or operator practices. |
| `.python-version` | Included: Python environment declaration. | Inventoried, contents not yet inspected; no interpreter-version compatibility conclusion from this file. |
| `Figure/` | Included: README's benchmark/learning plots and community images. | Names and README references inspected; JPG/PDF contents not yet inspected. No plotted results or experimental evidence are established by this inventory. |
| `LICENSE` | Excluded: repository licensing. | Inventoried; this run makes no licensing or redistribution judgment. |
| `README.md` | Included: declared architecture, installation, usage, evaluation claims and maintenance intentions. | Read completely as doctrine/design and reported operation, not a run trace. Some named files are absent from the tracked tree. |
| `client/` | Included: all shipped drivers, prompts, model clients, MCP consumers, judges, result writers and memory writers/reloaders. | Traced `agent.py`, `agent_local_server.py`, `no_parametric_cbr.py` and `parametric_memory_cbr.py`; read baseline completely and relevant entry-point, state-loop, prompt and persistence ranges of the others. Remaining utility/backend detail is available for later inspection, not an access gap. |
| `data/` | Included: benchmark input consumed by the memory drivers. | `deepresearcher.jsonl` path traced from both drivers; first record inspected for question/ground-truth fields. Remaining records not yet inspected; no dataset-wide quality or provenance conclusion. |
| `memory/` | Included: retained cases, training examples, retrieval, standalone retriever training and evaluation. | Read `np_memory.py`, `parametric_memory.py` and `train_memory_retriever.py` completely; sampled the first records of `dummy_memo.jsonl`, `memory.jsonl` and `training_data.jsonl`. Full corpus content not yet inspected. No checkpoint files are tracked. |
| `pyproject.toml` | Included: package identity and dependency declaration. | Read completely; declaration does not prove installability. |
| `requirements.txt` | Included: alternative dependency declaration. | Inventoried, contents not yet inspected; dependency equivalence is not established. |
| `searxng-docker/` | Included: shipped search-service deployment/configuration. | Read `docker-compose.yaml`; inventoried `Caddyfile`, service template, README, license, `.dockerignore` and `searxng/{settings.yml,limiter.toml,uwsgi.ini}`. Configuration details beyond Compose remain uninspected. External container implementations are not frozen here. |
| `server/` | Included: shipped MCP tool producers, tool-local model calls, workspace state and interpreter backends. | Searched registrations, executable entry points, imports and dependency calls in `ai_crawl.py`, `craw_page.py`, `code_agent.py`, `documents_tool.py`, `excel_tool.py`, `image_tool.py`, `math_tool.py`, `search_tool.py`, `serp_search.py`, `video_tool.py` and `jina_fetch_tool.py`. Read `ai_crawl.py` completely and material workspace/file-write, document-dispatch and media-call ranges. Traced `code_agent.py` to `interpreters/interpreters.py` and searched all interpreter classes, including subprocess, Docker, E2B, IPython and internal Python. Remaining implementation details are available, not excluded. No security certification follows from interface tracing. |
| `uv.lock` | Included: dependency lock evidence. | Inventoried, contents not yet inspected; resolved dependency behavior is not attributed to this repository. |

All coverage rows refer to SRC-1. Included paths not yet read can be inspected later at this same registered commit; initial coverage is not an evidence allowlist.

### Frozen evidence and exclusions

The acquired Git checkout reports HEAD `42fbbcac63dd58ed6856c0761357345a58e4f032` and a clean working tree. The applicability cutoff is the supplied run date, **2026-10-12**, not a claim that the repository or any live service was current on that date. Only this frozen commit supplies evidence. The overall tier is **code-grounded**; documentation and supplied JSONL data remain distinct evidence layers.

External dependencies include OpenAI/Azure/OpenAI-compatible model endpoints (including the local-server client), pretrained transformer assets and trained checkpoints, MCP and other Python dependencies, search APIs or SearxNG, browser/crawling infrastructure, document/transcription services, FFmpeg, and optional execution backends. Their integration code and bundled deployment configuration are included; their implementations, live responses, provider policies and operator installations are excluded. This prevents conclusions about deployed reliability, model quality, service behavior or isolation guarantees from the repository alone (SRC-1, `client/agent.py`, `client/agent_local_server.py`, `memory/parametric_memory.py`, `server/documents_tool.py`, `server/video_tool.py`, `server/jina_fetch_tool.py`, `server/serp_search.py`, `server/interpreters/e2b_interpreter.py`, `searxng-docker/docker-compose.yaml`).

The README refers to installation/guide/shell-script/checkpoint paths that the tracked inventory does not contain, including `INSTALL.md`, `client/run_parametric.sh`, `client/PARAMETRIC_MEMORY_GUIDE.md`, `memory/retrain.sh` and `memory/ckpts/retriever/best.pt`. Missing guide and automation files prevent treating the documented deployment/retraining workflow as fully inspectable shipped behavior. The missing checkpoint prevents inspection of trained inference parameters, not inspection of the loader and training code. External papers and repositories linked by the README are not additional sources (SRC-1, `README.md`, `memory/parametric_memory.py`).

No target program, example or test was executed. The supplied opening and acquisition records contain no execution trace or intervention/comparison evidence. Committed case and training records are inspected data artifacts, not verified observations of their generation. Consequently this boundary supports source-level operation and attributed claims, not reproduced benchmark scores, successful end-to-end operation or causal learning gains.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Agent-on-the-Fly/AgentFly` | 42fbbcac63dd58ed6856c0761357345a58e4f032 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/agentfly-bbfc9fb2d5c7/related-systems/Agent-on-the-Fly--AgentFly`. Implementation: all four client entry points and their state consumers/writers, all three memory Python modules, server/tool and interpreter searches plus material source ranges, sampled JSONL records and Compose. Doctrine/design: complete README, configuration and source prompts. Reported operation: README performance/learning claims; no observed-run or causal-experiment layer established. | Implementation: [client](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py), [memory driver](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py), [training](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py), [model-dependent tool](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/server/ai_crawl.py). Doctrine/design and reported operation: [README](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/README.md). Further commit-relative anchors are in the coverage table and boundary text. | Implementation: no tracked trained checkpoint or README-mentioned guide/automation files; cannot establish trained parameters or those missing workflow steps. External service and dependency internals excluded. Doctrine/design: intentions do not establish execution. Reported operation: no supplied trace or experiment validates performance claims. Available but uninspected ranges and records are listed above and are not access gaps. |
