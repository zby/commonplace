---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MemoryOS's shipped memory libraries, MCP server, Playground and evaluation workflow at commit 587ed7755c7aed179965792830ff1b5ad9a6fa92."
run-id: AAS-2026-10-16-memoryos-bb72a1b70e03-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/BAI-LAB/MemoryOS
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-memoryos/related-systems/BAI-LAB--MemoryOS
  revision: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
  sha256: null
---

# MemoryOS boundary

## Boundary and evidence

This run analyses MemoryOS as a **memory/knowledge/context-engineering system**, not as a general agent runtime. Its intended use is persistent, personalized dialogue: accept user–assistant exchanges, maintain short-, mid- and long-term memory, retrieve retained context, and supply or generate subsequent responses. The boundary is **whole-system** across the material shipped library variants, server, application, prompts and evaluation driver. These callers are part of the target rather than excluded applications (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-mcp/server_new.py`, `memoryos-playground/memdemo/app.py`, `eval/main_loco_parse.py`).

The frozen evidence is the repository at **587ed7755c7aed179965792830ff1b5ad9a6fa92**, applicable through **2026-10-16**. The acquired checkout's HEAD was checked against that pin; its working tree was clean. The evidence tier is **code-grounded**. No target code, tests, examples or providers were executed. Repository documentation supplies declared design and attributed performance claims, not observed operation or a causal experiment.

### Functional scope and entry-point trace

The Python-facing path includes initialization of user- and assistant-specific storage, JSON reload, admission of dialogue pairs, migration to mid-term sessions, model-assisted summaries and continuity metadata, heat-triggered profile/knowledge updates, retrieval and response generation. The response path itself writes the generated exchange back to memory. Maintenance entry points, including forced analysis, are included (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/short_term.py`, `memoryos-pypi/mid_term.py`, `memoryos-pypi/long_term.py`, `memoryos-pypi/updater.py`, `memoryos-pypi/retriever.py`). The following implementation passage establishes that the consumption path closes back into admission:

> # 10. Add this interaction to memory
> self.add_memory(user_input=query, agent_response=response_content, timestamp=get_timestamp())
> --- `memoryos-pypi/memoryos.py`

Model instructions are part of this mechanism, not incidental documentation. Generation prompts consume recent history, historical memory and user traits; summarization, preference analysis, knowledge extraction and continuity prompts govern derived state. The utilities call these prompts through the model client (SRC-1: `memoryos-pypi/prompts.py`, `memoryos-pypi/utils.py`). For example:

> PERSONALITY_ANALYSIS_SYSTEM_PROMPT = """You are a professional user preference analysis assistant. Your task is to analyze the user's personality preferences from the given dialogue based on the provided dimensions.
> --- `memoryos-pypi/prompts.py`

The ChromaDB variant is included separately rather than presumed identical to the JSON variants. Its `Memoryos` constructs a shared storage provider, uses persistent vector collections and reloadable JSON metadata, and registers an exit-time metadata save. Its generation path also retrieves retained content and calls `add_memory` (SRC-1: `memoryos-chromadb/memoryos.py`, `memoryos-chromadb/storage_provider.py`).

The MCP server initializes its bundled memory implementation from configuration and exposes `add_memory`, `retrieve_memory` and `get_user_profile` over stdio. Retrieval returns memory and profile data; final client-side answer generation remains the responsibility of the external MCP host. The repository's own server and bundled implementation remain included (SRC-1: `memoryos-mcp/server_new.py`, `memoryos-mcp/memoryos/memoryos.py`).

The shipped Flask Playground is also included. Its `/chat` route calls `get_response`; its import route admits supplied exchanges; its analysis route calls forced analysis; its clear route deletes retained user and assistant directories and reconstructs the memory object. The browser template calls these routes. Import paths, the fixed embedding-cache location and launcher assumptions require later compatibility analysis; source inclusion is not evidence that this application launches successfully as checked out (SRC-1: `memoryos-playground/memdemo/app.py`, `memoryos-playground/memdemo/templates/index.html`, `memoryos-playground/memdemo/start_demo.sh`).

The evaluation workflow is a material state producer and consumer, not merely an external benchmark. It uses its own memory modules, imports conversation histories from LoCoMo, stores and updates memory, retrieves it to answer benchmark questions, and writes `all_loco_results.json`. A separate scorer reads those results and computes category-level token-set F1. These are implementation paths, not supplied run results (SRC-1: `eval/main_loco_parse.py`, `eval/evalution_loco.py`). Its own imports establish the separate implementation:

> from short_term_memory import ShortTermMemory
> from mid_term_memory import MidTermMemory
> from long_term_memory import LongTermMemory
> from dynamic_update import DynamicUpdate
> from retrieval_and_answer import RetrievalAndAnswer
> --- `eval/main_loco_parse.py`

### Top-level tracked coverage

Every top-level tracked file or directory is classified below. “Included” fixes functional scope; it does not claim every line has already been examined. Initial inspection followed the shipped entry points and their storage, maintenance and consumption responsibilities. Available but not yet deeply inspected helpers and documentation remain distinguishable from unavailable evidence and deliberate exclusions. All rows refer to SRC-1.

| Top-level path | Classification and material paths | Initial inspection and consequence of exclusion or limit |
|---|---|---|
| `Dockerfile` | Included: copies `memoryos-pypi/` and installs its requirements. | Read in full. Packaging evidence only; no image build or deployment observation. |
| `LICENSE` | Excluded: licensing text. | Deliberate non-operational exclusion; no legal/licensing assessment. |
| `Paper-MemoryOS.pdf` | Excluded: research paper. | Available but deliberately not inspected; no paper-method or paper-result verification. README-reported results remain attributed claims. |
| `README.md` | Included: intended use, Python/MCP/ChromaDB/Playground entry points, Docker and evaluation instructions. | Read in full. Claims and instructions are doctrine/design or reported operation, not execution evidence. Linked projects and surveys are not followed. |
| `docs/` | Included: `docs/docs.html` operating description and API documentation. Excluded: `docs/local1.png`, `docs/local2.png`, `docs/memoryos.png` illustrations. | Searched headings/API names and read operation, local Playground and API sections. Remaining HTML is not yet deeply inspected. Image exclusion prevents visual-interface verification, not source-level loop analysis. |
| `eval/` | Included: `main_loco_parse.py`, `dynamic_update.py`, `short_term_memory.py`, `mid_term_memory.py`, `long_term_memory.py`, `retrieval_and_answer.py`, `utils.py`, `evalution_loco.py`, `locomo10.json`. | Driver and scorer read in full; supporting module definitions and save/load/retrieval paths searched. Dataset records and all supporting prompt bodies are not yet deeply inspected. Supports workflow boundary, not dataset validity or reproduced performance. |
| `memoryos-chromadb/` | Included: `memoryos.py`, `storage_provider.py`, `short_term.py`, `mid_term.py`, `long_term.py`, `retriever.py`, `updater.py`, `prompts.py`, `utils.py`, `__init__.py`, `requirements.txt`, `comprehensive_test.py`. | Read initialization, admission/generation and provider persistence setup; searched storage, maintenance, retrieval and demonstration paths. Remaining internals, prompt bodies and dependency details require later inspection before variant-specific claims. No persistence or quality guarantees established by execution. |
| `memoryos-mcp/` | Included: `server_new.py`, `config.json`, `mcp.json`, `requirements.txt`, bundled `memoryos/` modules, prompts and `test.py`, plus `test_simple.py`. | Server read in full; bundled orchestration searched and compared with Playground orchestration. Configuration and test-client details are not yet deeply inspected. External MCP client behavior is not established. |
| `memoryos-playground/` | Included: Python memory modules, `prompts.py`, `utils.py`, `__init__.py`, `requirements.txt`, `test.py`; `memdemo/app.py`, `templates/index.html`, `start_demo.sh`, `sample_conversations.json`, `requirements.txt`. | Flask application and launcher read in full, browser route calls searched, orchestration compared with Python variant. Full UI, sample data and all helper internals are not yet deeply inspected; no browser/deployment result is asserted. |
| `memoryos-pypi/` | Included: `memoryos.py`, `short_term.py`, `mid_term.py`, `long_term.py`, `updater.py`, `retriever.py`, `prompts.py`, `utils.py`, `__init__.py`, `requirements.txt`, `test.py`. | Orchestrator, short-term storage and requirements read in full; persistence, updater, retrieval and prompt sections read; utility and demonstration entry points searched. Remaining helper details are available for subsequent source tracing. Published PyPI artifact equivalence is not established. |
| `readme_cn.md` | Included: alternate-language project and setup documentation. | Searched section structure and entry-point references; not fully compared with English documentation. No translation-equivalence claim. |

### Dependencies, exclusions and evidence limits

External model endpoints and embedding weights, dependency implementations such as OpenAI's client, sentence-transformers, FlagEmbedding, FAISS, ChromaDB, Flask and FastMCP, and the enclosing MCP applications are outside the frozen repository. Their call sites and supplied configuration are included, not their internals (SRC-1: `memoryos-pypi/requirements.txt`, `memoryos-pypi/utils.py`, `memoryos-chromadb/storage_provider.py`, `memoryos-mcp/server_new.py`, `memoryos-playground/memdemo/app.py`). This prevents claims about provider reliability, dependency correctness, host-side memory use or end-to-end deployment success. The Playground's machine-specific embedding-cache path is visible in source; the referenced local cache is not supplied, so successful local model loading is not established.

Live websites, remote images, videos, other repositories, the registry package and published container image are not frozen evidence. Their behavior and equivalence to this checkout cannot be concluded. No execution trace or experimental comparison was supplied: this prevents verified latency, benchmark improvement, crash recovery and causal effectiveness claims. These limits do not remove any shipped memory-loop responsibility from the functional boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/BAI-LAB/MemoryOS` | 587ed7755c7aed179965792830ff1b5ad9a6fa92 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-memoryos/related-systems/BAI-LAB--MemoryOS`. Implementation: tracked tree; Python orchestrator, storage save/load, updater and retriever sections; ChromaDB initialization, generation and provider metadata; MCP server and bundled orchestration; Flask routes, browser route calls and launcher; evaluation driver, scorer and supporting module searches; Dockerfile and core requirements. Doctrine/design: README, scoped HTML documentation and shipped prompt sections. Reported operation: README performance and release claims only. Coverage and pending deep reads are detailed above. | Implementation: [Python orchestration](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/memoryos-pypi/memoryos.py), [ChromaDB storage](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/memoryos-chromadb/storage_provider.py), [MCP server](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/memoryos-mcp/server_new.py), [Playground](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/memoryos-playground/memdemo/app.py), [evaluation driver](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/eval/main_loco_parse.py). Doctrine/design: [prompts](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/memoryos-pypi/prompts.py), `docs/docs.html`. Reported operation and design: [README](https://github.com/BAI-LAB/MemoryOS/blob/587ed7755c7aed179965792830ff1b5ad9a6fa92/README.md). | Repository code is available; uninspected portions are not access gaps. External provider/dependency internals, model cache and live deployments are not supplied. No observed run or causal experiment supports performance, deployment success or persistence guarantees. Deliberately excluded paper, licensing text and illustrations support no conclusions here. |
