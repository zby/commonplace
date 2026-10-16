---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "PageIndex's shipped document indexing, persistent storage, retrieval and chat paths at af92d9658a6a9c0ae31171b43198db28951af2f4."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/VectifyAI/PageIndex
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/pageindex-50056ef72767/related-systems/VectifyAI--PageIndex
  revision: af92d9658a6a9c0ae31171b43198db28951af2f4
  sha256: null
---

# PageIndex boundary

## Boundary and evidence

The target is the PageIndex repository's shipped document knowledge system, not only its tree-building API and not the separately operated PageIndex Cloud service. Its intended use is to index long documents once, retain their tree and page content, and let a model retrieve evidence for later answers. This qualifies as a memory/knowledge/context-engineering system: model-dependent indexing and answer-time retrieval serve retained document knowledge. The repository also ships its own chat orchestration and framework adapters; it is not bounded here as a returning index computation. SRC-1: `README.md`, `pageindex/__init__.py`, `pageindex/client.py`, `pageindex/local_api.py`, `pageindex/local_chat.py`.

The boundary kind is **whole-system for the shipped repository artifact**. It includes local PDF ingestion, Flash layout extraction and model-based refinement, classic PDF indexing, Markdown tree generation, local persistence and repair of its manifest cache, document listing/deletion, tree/page access, agent tools and prompts, chat drivers, citations, cloud client/bridge behavior, integration adapters, shipped notebook callers and evaluation material. The CLI and notebooks are included callers, not excluded hosts merely because they invoke package APIs. SRC-1: `run_pageindex.py`, `pageindex/local_store.py`, `pageindex/agent_tools.py`, `pageindex/integrations/openai_agents.py`, `cookbook/pageindex-vision-rag.ipynb`.

Initial inspection traced the local state loop through `PageIndexClient` selecting `LocalAPI`, submission building a structure and checking page bounds, `DocStore` saving trees/pages/metadata, and later tree/page reload and document discovery. Deletion and manifest reconstruction are shipped maintenance paths. These responsibilities stay within the target. SRC-1: `pageindex/client.py`, `pageindex/local_api.py`, `pageindex/local_store.py`.

>         _write_json_atomic(doc_dir / "tree.json", tree)
>         _write_json_atomic(doc_dir / "pages.json", pages)
>         _write_json_atomic(doc_dir / "doc.json", meta)
> --- `pageindex/local_store.py`

The retained state has shipped consumers. The package's chat prologue combines managed instructions, document targeting and supplied history, then runs a configured agent. Its non-streaming chat-completions driver invokes the external Agents SDK runner; that SDK dependency does not remove the shipped driver from this boundary. Framework adapters also expose the same tool responsibilities to caller-owned agents. SRC-1: `pageindex/local_chat.py`, `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py`.

>             result = _run_sync(_run_closing(agent,
>                 Runner.run(agent, input=items, **run_kwargs)))
> --- `pageindex/local_chat.py`

Prompts are part of the mechanism, not commentary outside it. Local guidance controls discovery and structure-first reading, with optional citation instructions. Cloud-mode guidance and tool schemas may instead arrive from the remote MCP server; the frozen client establishes how they are obtained, not their current remote contents. SRC-1: `pageindex/agent_tools.py`.

> READING WORKFLOW:
> - For documents over {STRUCTURE_FIRST_PAGE_THRESHOLD} pages: call get_document_structure() first to locate relevant sections, then get_page_content() with targeted page ranges.
> - For small documents ({STRUCTURE_FIRST_PAGE_THRESHOLD} pages or fewer): call get_page_content() directly.
> --- `pageindex/agent_tools.py`

The notebook consumers include a local submit-and-chat example and cloud retrieval/citation/cost examples. The vision-RAG notebook additionally ships an explicit tree-search prompt, page-image selection and answer-generation call. It therefore belongs to the functional boundary rather than being treated as an unrelated enclosing application. Its cloud tree generation remains dependent on an unavailable server implementation. SRC-1: `cookbook/pageindex-flash-demo.ipynb`, `cookbook/pageindex-citation.ipynb`, `cookbook/pageindex-indexing-cost-demo.ipynb`, `cookbook/pageindex-multimodal.ipynb`, `cookbook/pageindex-query-pricing-demo.ipynb`, `cookbook/pageindex-vision-rag.ipynb`.

### Repository coverage

All rows refer to SRC-1 at the frozen commit. “Included” is a functional scope decision, not a claim that every line has already been inspected. Initial inspection is distinguished below from available material still requiring detailed analysis. No material shipped state-loop path was inaccessible.

| Top-level tracked path | Scope and role | Initial inspection and limits |
|---|---|---|
| `pageindex/` | Included: package entry points, indexing, retained state, admission, maintenance, retrieval, prompts and chat. | Inspected exports; client backend selection; complete local API/store; Flash public orchestration; classic/Markdown/optimizer/utility function inventory; local chat prologue and runner; tool/instruction construction; cloud upload; all three integration adapters. Material paths include `pageindex/flash/` parser, layout, heading, outline, embedded-TOC and data machinery; `pageindex/page_index_classic.py`, `pageindex/page_index_md.py`, `pageindex/tree_optimize.py`, `pageindex/utils.py`, `pageindex/local_api.py`, `pageindex/local_store.py`, `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/agent_tools.py`, `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`, `pageindex/integrations/`, `pageindex/imaging.py`, `pageindex/chat_stream.py`, `pageindex/types.py`, `pageindex/config.yaml`, `pageindex/naming.py`, `pageindex/errors.py` and version/type markers. Deep parser internals and remaining endpoint/stream/citation branches are available, not access gaps; later claims need their own inspection. |
| `run_pageindex.py` | Included: PDF/Markdown CLI driver and JSON result writer. | Read completely, including Flash/classic/Markdown routing, model/config options, rejection check and persistence to `results/`. |
| `cookbook/` | Included: all six shipped notebook workflows, their prompts and consumers. | Read every code/Markdown cell from all six notebooks; embedded outputs were not inspected as execution evidence. Vision-RAG explicitly consumes tree nodes and page images; newer demos use SDK chat/citations and cost instrumentation. Notebook downloads, package installs and live calls were not run. |
| `tests/` | Included: contract evaluators, fixtures and regression tests, not an observed successful run. | Inventoried all tracked test paths; searched test names for tool/client/chat/Flash/tree/package coverage and inspected chat tool-round-trip and manifest-recovery tests. Includes `tests/conftest.py`, `tests/data/`, `tests/fixtures/`, local/chat/tool suites, classic/Markdown suites, extraction, image, naming and tree-format suites. Remaining bodies and fixture bytes are available but not yet inspected in detail. No tests executed. |
| `examples/` | Included: document inputs and retained example structures. | Inventoried `examples/documents/*.pdf` and `examples/results/*_structure.json`; contents not yet inspected. They may support format or attributed example claims after inspection, not independent retrieval accuracy. |
| `README.md` | Included: system intent, usage, cloud/local distinction and reported benchmarks. | Read completely. External benchmark links are not frozen benchmark data. |
| `pyproject.toml` | Included: package surface and external dependency declarations. | Read completely, including package data and optional framework dependencies. |
| `requirements.txt` | Included: dependency support for repository usage. | Available and inventoried; contents not yet inspected. Do not infer exact installed versions from it. |
| `assets/` | Included as supporting documentation/evaluation illustrations. | Inventoried benchmark charts and RAG diagrams; image pixels not inspected. These are not a frozen benchmark runner or independently verified measurements. |
| `.github/` | Excluded: CI/security/dependency and package-publication configuration. | Tree inventory identifies workflows and Dependabot config. Exclusion prevents assessment of release automation and CI enforcement, not source-level state-loop behavior. |
| `.gitattributes` | Excluded: Git file handling metadata. | Inventoried only; no conclusion about checkout/export transformations. |
| `.gitignore` | Excluded: developer ignore policy. | Inventoried only; no claim that the source inventory describes all files generated by execution. |
| `LICENSE` | Excluded: legal terms. | Inventoried only; no licensing/compliance conclusion. |

### Frozen evidence and external limits

The frozen revision is **af92d9658a6a9c0ae31171b43198db28951af2f4**, with applicability cutoff **2026-10-15**. The evidence tier is **code-grounded**. HEAD was checked against the acquired revision; the checkout is read-only. No other repository, external documentation page, model service or live cloud response is admitted as evidence.

External dependencies include model providers and their SDKs, LiteLLM, the Agents SDK, optional Anthropic/Claude Agent SDKs, MCP, PDF parsers and HTTP services (SRC-1: `pyproject.toml`). Their implementations are not frozen here, preventing conclusions about provider internals and dependency-version-specific operational behavior. This does not exclude the package's own orchestration, adapters or error handling.

The repository supplies Cloud HTTP/MCP clients, not Cloud's server-side OCR, image understanding, corpus/file-system indexing, managed storage or managed chat implementation. Those implementations and live MCP prompts/schemas are unavailable evidence, not merely uninspected repository files. Their absence prevents code-grounded accounts of cloud state production, remote search policy and managed chat internals. Client-side request construction, discovery and consumption remain included. SRC-1: `README.md`, `pageindex/cloud_api.py`, `pageindex/agent_tools.py`, `pageindex/integrations/claude_agent_sdk.py`.

External benchmark repositories, websites and blog posts linked by the README were not acquired. This prevents independent assessment of their datasets, runners and headline accuracy/cost claims. The frozen README and Flash documentation support attributed reported operation only. No target execution, tests, provider calls or causal experiments were performed; static source and test assertions cannot establish measured production reliability or retrieval effectiveness. SRC-1: `README.md`, `pageindex/flash/README.md`, `tests/test_local_chat.py`, `tests/test_client.py`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/VectifyAI/PageIndex` | af92d9658a6a9c0ae31171b43198db28951af2f4 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/pageindex-50056ef72767/related-systems/VectifyAI--PageIndex`. Implementation: tree inventory, package exports/backend routing, local ingestion/store/reload/maintenance, Flash orchestration, indexing/optimizer/utility inventory, chat prologue/runner, agent instructions/tools, Cloud upload, integration adapters, six notebook code/Markdown sources and selected test contracts. Doctrine/design: complete README, Flash README and package metadata. Reported operation: benchmark descriptions in those README files; not independently observed. | Implementation: [local state API](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/pageindex/local_api.py), [store](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/pageindex/local_store.py), [chat](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/pageindex/local_chat.py), [tools/prompts](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/pageindex/agent_tools.py), [CLI](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/run_pageindex.py), [vision notebook](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/cookbook/pageindex-vision-rag.ipynb). Doctrine and reported operation: [README](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/README.md), [Flash README](https://github.com/VectifyAI/PageIndex/blob/af92d9658a6a9c0ae31171b43198db28951af2f4/pageindex/flash/README.md). | No inaccessible material shipped path found. Cloud server/dependency internals, live server prompts and external benchmark data are outside the frozen source; prevents server-internal and independently verified performance claims. No observed-run or causal-experiment layer established. Available but not initially inspected files are identified in the coverage table, not classified as access gaps. |
