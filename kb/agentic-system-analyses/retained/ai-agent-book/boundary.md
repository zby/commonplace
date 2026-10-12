---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AI Agents in Depth's companion agent workflows and operating guidance at dbc046eb896ac4e39aa19c7774c8bf49583b89a6, with external reproduction loops outside the frozen evidence."
run-id: AAS-2026-10-12-ai-agent-book-d56e8121d636-01
result-disposition: complete
target-class: "agentic workflow and teaching suite"
boundary-kind: "complete artifact, partial loop"
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/bojieli/ai-agent-book
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/ai-agent-book-d56e8121d636/related-systems/bojieli--ai-agent-book
  revision: dbc046eb896ac4e39aa19c7774c8bf49583b89a6
  sha256: null
---

# AI Agents in Depth boundary

## Boundary and evidence

The target is the book's shipped companion agent workflows and operating guidance, not an asserted single production runtime. The explicitly defined class **agentic workflow and teaching suite** means a collection of separately launched model-dependent experiments, with shared packaging and explanatory material. The intended use is to distinguish those implemented mechanisms from the book's recommendations and reproduction plans. It is in scope because shipped drivers issue model calls through agent implementations; the manuscript alone is not being classified as an executing agent. SRC-1: `docs/en/README.md`, `pyproject.toml`, `chapter1/context/main.py`, `chapter1/context/agent.py`.

> **Agent = LLM + Context + Tools** — This book builds on this core formula across 10 chapters, taking AI Agents from principles to engineering practice. The full text, illustrations, and **93 accompanying experiments** are all open source. You are welcome to run the experiments yourself.
> --- `docs/en/README.md`

The project count is the source's declaration, not an independently verified count of working runtimes. The root package describes shared experiment plumbing, rather than supplying evidence of a unified scheduler or shared state loop. SRC-1: `pyproject.toml`.

> description = "Shared packaging and plumbing for the ai-agent-book companion experiments"
> --- `pyproject.toml`

Initial entry-point tracing followed the README's `chapter1/context/main.py` example to its `ContextAwareAgent` import, CLI modes, ablation-suite construction and the implementation's model request. This establishes a shipped model-dependent path, not successful execution or task correctness. SRC-1: `docs/en/README.md`, `chapter1/context/main.py`, `chapter1/context/agent.py`.

> # Call the model with tools
> response = self.client.chat.completions.create(**create_kwargs)
> --- `chapter1/context/agent.py`

A second trace inspected the user-memory driver's construction of a conversational agent and background processor, then followed the consumer's disk reload and prompt construction and the processor's history reload and analysis-agent handoff. These shipped callers belong to the target, not to an excluded host. This preliminary trace establishes that the suite includes state maintenance and later consumption, not merely a memory API. It does not establish complete coverage of its memory modes or evaluators. SRC-1: `chapter3/user-memory/main.py`, `chapter3/user-memory/conversational_agent.py`, `chapter3/user-memory/background_memory_processor.py`.

> self.memory_manager.load_memory()
>
> # Add memory summary
> memory_str = self.memory_manager.get_context_string()
> --- `chapter3/user-memory/conversational_agent.py`

> # Analyze conversation - this now directly updates memories via agent tools
> # The agent will process the conversation and use its tools to update memories
> _ = self.analyze_conversation(conversation_context)
> --- `chapter3/user-memory/background_memory_processor.py`

### Functional scope and inspection limits

All tracked companion implementations, their shipped drivers, prompts, maintenance procedures, evaluators, fixtures and retained experiment artifacts at SRC-1's commit are eligible evidence. The following inventory separates initial inspection from material still requiring inspection. It is not a whole-system coverage claim or a path allowlist.

| Material | Boundary treatment | Initial inspection and conclusion limit |
| --- | --- | --- |
| `chapter1/` through `chapter10/` | Included: separate agent, context, memory, retrieval, tool, interaction, evaluation, training, evolution and collaboration experiments | Tracked tree inventoried by chapter/project. Source excerpts inspected in `chapter1/context/` and `chapter3/user-memory/` only. Other projects are available but not yet inspected; no suite-wide mechanism, reliability or integration claim follows. |
| `agentbook/`, `pyproject.toml`, `uv.lock`, environment examples | Included: shared packaging and provider plumbing | Manifest inspected; provider tree inventoried. Provider implementation, lockfile and individual environment contracts not yet inspected; dependency declarations do not prove runtime compatibility. |
| `book/`, translated `book-*` directories, root READMEs and `docs/` | Included as attributed doctrine/design and, where present, attributed experiment-status evidence | `README.en.md` and `docs/en/README.md` inspected. Manuscript, translations, experiment conventions and status records not yet inspected; no claim of consistency between doctrine and code or completed experiments. |
| `skills/` | Included: shipped operating guidance consumed by an external agent host | `skills/README.md` inspected; skill directory names inventoried. Individual instructions and host loading behavior not yet inspected; no conclusion about compliance or effectiveness. |
| Root `tests/` and experiment-local tests, results and `validation/` paths | Included: evaluators, assertions and retained run artifacts | Paths inventoried, including user-memory and memory-system-evaluation evidence paths. Contents not yet inspected; existence does not establish observed operation or causal effects. |
| `cursor-chats/` | Included only as the target's own development records, subject to provenance and relevance checks | File inventory only; conversations not read or adopted as instructions. No development-history or run claim is supported at this stage. |
| `web-astro/`, `extras/`, `overrides/`, `scripts/`, `slides/`, `assets/`, site configuration and EPUB/PDF builders | Publication and reader surfaces are outside the agent-workflow mechanism account; any agent execution or evidence-producing responsibility found there requires explicit reassessment | Tree inventory only. Their exclusion prevents conclusions about publishing, reader annotations, site behavior or deployment. It does not exclude chapter-local workflows that generate documents. |
| Repository metadata, license and documentation-build dependency files | Outside agent execution; may supply contextual contracts if inspected | No license, CI assurance or build reproducibility conclusion. |

The boundary kind is **complete artifact, partial loop**, not `whole-system`. The Git artifact is frozen in full, but several reproduction paths depend on other repositories and external environments not frozen here. The root documentation explicitly distinguishes standalone projects, reproductions and designs and requests separately obtained external repositories. Its appendix also retains historical chapter-path labels; it is not evidence that those components are present or executable at the current tree paths. SRC-1: `docs/en/README.md`, `pyproject.toml`.

> The 23 external repos for benchmarks, training frameworks, and robot platforms in Chapters 6, 7, 9, 10 are **not bundled** (due to size and licensing) and must be cloned into the corresponding directories.
> --- `docs/en/README.md`

No external repository, linked paper, live website, provider response, model weight set, benchmark download or separately installed host is registered. Tracked vendored content, if present, remains eligible as part of this Git artifact, not as a claim about a separately acquired upstream revision. Missing external components prevent end-to-end conclusions about reproduction and training loops. External model services and host environments prevent conclusions about service behavior, deployment and host instruction loading. Available but unread files are inspection limits, not access gaps. SRC-1: `docs/en/README.md`, `pyproject.toml`, `skills/README.md`.

The frozen revision is `dbc046eb896ac4e39aa19c7774c8bf49583b89a6`; checkout HEAD was verified against acquisition, with no working-tree changes reported. The applicability cutoff is 2026-10-12, the supplied run date. It is not a promise about later main-branch or release contents. Overall evidence is **code-grounded**, limited to source inspection. No target code, test, example or model call was executed. Retained traces may support later observed-run findings only after their contents and conditions are inspected; they do not automatically raise this boundary's evidence layer.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/bojieli/ai-agent-book` | dbc046eb896ac4e39aa19c7774c8bf49583b89a6 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/ai-agent-book-d56e8121d636/related-systems/bojieli--ai-agent-book`. Tracked top-level tree and chapter/project inventories inspected. Implementation: selected ranges of `chapter1/context/main.py`, `chapter1/context/agent.py`, `chapter3/user-memory/main.py`, `chapter3/user-memory/conversational_agent.py`, `chapter3/user-memory/background_memory_processor.py`; targeted symbol search across memory manager and conversation history. Doctrine/design: complete `README.en.md`, `docs/en/README.md`, `pyproject.toml`, `skills/README.md`. Inventory is not implementation inspection of all listed projects. | Implementation: [context driver](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter1/context/main.py), [context agent](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter1/context/agent.py), [memory driver](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter3/user-memory/main.py), [memory consumer](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter3/user-memory/conversational_agent.py), [memory processor](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/chapter3/user-memory/background_memory_processor.py). Doctrine/design: [README](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/docs/en/README.md), [package contract](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/pyproject.toml), [skill installation and index](https://github.com/bojieli/ai-agent-book/blob/dbc046eb896ac4e39aa19c7774c8bf49583b89a6/skills/README.md). | No access gap to registered tracked source was encountered. Separately obtained upstream repositories, live services, weights and execution environments are outside the frozen source; no end-to-end reproduction, provider behavior or host compliance conclusion. Most available projects and retained run evidence remain uninspected; no exhaustive suite-loop, observed-run or causal-experiment claim. |
