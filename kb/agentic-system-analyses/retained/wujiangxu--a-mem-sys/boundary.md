---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "A-MEM's shipped memory library, callers, prompts and tests at frozen commit f303dfc71e07bdc787f4bc135d4cea328ae30e99."
run-id: AAS-2026-10-16-a-mem-sys-eff95cd80440-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f303dfc71e07bdc787f4bc135d4cea328ae30e99
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/WujiangXu/A-mem-sys
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-a-mem/related-systems/WujiangXu--A-mem-sys
  revision: f303dfc71e07bdc787f4bc135d4cea328ae30e99
  sha256: null
---

# A-MEM boundary

## Boundary and evidence

The target is the complete A-MEM memory library and its shipped usage and evaluation surfaces in this repository, not a complete task-solving agent. Its intended use is to supply memory creation, semantic metadata, relationship evolution and retrieval to an enclosing LLM application. It qualifies as a memory/knowledge/context-engineering system because its implementation issues model calls for metadata and evolution and serves retained content through memory APIs (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/llm_controller.py`). The repository itself distinguishes this library from the separate paper-reproduction project:

> **Note:** This repository provides a memory system to facilitate agent construction. If you want to reproduce the results presented in our paper, please refer to: [https://github.com/WujiangXu/AgenticMemory](https://github.com/WujiangXu/AgenticMemory)
> --- `README.md`

The boundary is **whole-system** relative to this shipped memory system. Inspection traced the README callers and test callers into `AgenticMemorySystem`, its embedded analysis and evolution prompts, `MemoryNote`, `LLMController` and all four backend adapters, and `ChromaRetriever`. It includes creation/admission of notes, generated and caller-supplied metadata, neighbor mutation, consolidation, vector storage and metadata conversion, updates, deletion, direct reads, and search/linked-memory consumption. README best practices and source-native maintenance documents are included as declared guidance, not additional executable behavior (SRC-1, `README.md`, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`, `MERGE_PR4_SUMMARY.md`, `PR_REVIEW_ANALYSIS.md`).

The whole-system designation does not assert durable cross-session memory. The shipped constructor initializes an empty object map and attempts to reset the Chroma collection; the retriever uses `chromadb.Client(Settings(allow_reset=True))`. Shipped consumers read and search notes within the constructed system; the inspected tree contains no save/load driver or application that reloads notes into a new instance. Thus cross-session restoration and downstream agent answer generation are not established, rather than being silently delegated to an excluded shipped caller (SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`, `README.md`, `tests/test_memory_system.py`). The relevant initialization is explicit:

> self.memories = {}
> self.model_name = model_name
> # Initialize ChromaDB retriever with empty collection
> try:
>     # First try to reset the collection if it exists
>     temp_retriever = ChromaRetriever(collection_name="memories",model_name=self.model_name)
>     temp_retriever.client.reset()
> --- `agentic_memory/memory_system.py`

The evidence is frozen at commit `f303dfc71e07bdc787f4bc135d4cea328ae30e99`, verified as the supplied checkout's HEAD. The applicability cutoff is 2026-10-16; no later revisions or live service behavior enter the evidence. The overall tier is **code-grounded**: source was inspected, but target code, examples and tests were not executed.

### Tracked top-level coverage

Every top-level tracked file or directory is accounted for below. “Excluded” is deliberate, not an access failure. All listed text files were inspected; the figures were inventoried but not opened.

| Top-level path | Status | Material paths and responsibility | Limit or conclusion prevented |
|---|---|---|---|
| `agentic_memory/` | Included | `memory_system.py`: note state, admission, inline prompts, model-output application, consolidation, CRUD and retrieval; `llm_controller.py`: OpenAI, Ollama, SGLang and OpenRouter adapters and fallbacks; `retrievers.py`: Chroma setup, embedding input, metadata serialization and search; `__init__.py`: empty package marker, checked by tree and size. | Supports implementation analysis of the shipped memory loop, not successful provider operation. |
| `README.md` | Included | Library contract, construction and CRUD/search examples, model service setup, best practices and attributed results claim. | Examples and performance assertions are not observed runs. |
| `tests/` | Included | `test_memory_system.py`: caller paths for creation, storage/retrieval, updates, relationships, evolution, deletion and consolidation; `test_llm_backends.py`: backend selection, mocked SGLang requests and schema/error handling; `test_utils.py`: mock controller; `SGLANG_TESTS.md`: test guidance and real-service example; `__init__.py`: empty marker. | Test source establishes intended checks, not passing results or cross-session durability. No paper benchmark runner is shipped here. |
| `pyproject.toml` | Included | Package discovery, library metadata, dependency declarations; no executable script entry point declared. | Dependency implementation and installed-version compatibility are not frozen. |
| `requirements.txt` | Included | Alternative dependency list. | Minimum versions do not establish a reproducible runtime environment. |
| `MERGE_PR4_SUMMARY.md` | Included | Source-native OpenRouter integration account and example; testing recommendations. | Historical integration claims remain attributed, not independently observed. |
| `PR_REVIEW_ANALYSIS.md` | Included | Source-native review and proposed environment/client/example changes. | Proposed PR code is not treated as shipped implementation; this does not freeze the referenced branches. |
| `Figure/` | Excluded; not inspected | `framework.jpg`, `intro-a.jpg`, `intro-b.jpg`: README illustrations. | No conclusions rest on image-only architecture or comparison assertions. Executable paths and textual contracts remain included. |
| `.gitignore` | Included as support metadata | Ignore patterns for development and generated state. | Does not establish that ignored artifacts or deployments exist. |
| `LICENSE` | Included as support metadata | MIT license. | Supplies no operational evidence. |

External dependencies include ChromaDB, its sentence-transformer embedding function and model artifacts, and the Python packages declared in the packaging files. Model inference is delegated to OpenAI, Ollama through LiteLLM, SGLang HTTP, or OpenRouter through LiteLLM. Their service internals, model weights, storage internals and live responses are outside the frozen source; this prevents claims about provider reliability, actual model decisions, measured latency or dependency-level durability (SRC-1, `agentic_memory/retrievers.py`, `agentic_memory/llm_controller.py`, `pyproject.toml`, `requirements.txt`). An enclosing application chooses experiences to store and decides how retrieved material affects its task; no such general-purpose application is shipped here. The separate paper, reproduction repository, linked PR branches and other external pages were not acquired. Consequently paper-result reproduction and end-to-end agent performance cannot be concluded from this boundary (SRC-1, `README.md`, `PR_REVIEW_ANALYSIS.md`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/WujiangXu/A-mem-sys` | f303dfc71e07bdc787f4bc135d4cea328ae30e99 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-a-mem/related-systems/WujiangXu--A-mem-sys`. Implementation: all three nonempty package modules, both test suites and test utility; package markers checked by tree/size. Doctrine/design: complete README, packaging files, test guide, merge summary and source-native PR review; support metadata: `.gitignore`, `LICENSE`. Reported operation: README empirical-results statement and merge summary's integration account only. Figures inventoried, deliberately excluded. | Implementation: [memory system](https://github.com/WujiangXu/A-mem-sys/blob/f303dfc71e07bdc787f4bc135d4cea328ae30e99/agentic_memory/memory_system.py), [retriever](https://github.com/WujiangXu/A-mem-sys/blob/f303dfc71e07bdc787f4bc135d4cea328ae30e99/agentic_memory/retrievers.py), [controllers](https://github.com/WujiangXu/A-mem-sys/blob/f303dfc71e07bdc787f4bc135d4cea328ae30e99/agentic_memory/llm_controller.py), `tests/test_memory_system.py`, `tests/test_llm_backends.py`, `tests/test_utils.py`. Doctrine/design and reported operation: [README](https://github.com/WujiangXu/A-mem-sys/blob/f303dfc71e07bdc787f4bc135d4cea328ae30e99/README.md), `pyproject.toml`, `requirements.txt`, `tests/SGLANG_TESTS.md`, `MERGE_PR4_SUMMARY.md`, `PR_REVIEW_ANALYSIS.md`. | No access failure for the registered checkout. No observed-run or causal-experiment layer was established. Test source, examples and historical reports cannot establish passing execution, actual model behavior, cross-session recovery or benchmark performance. External services, dependencies and linked research are not frozen evidence. |
