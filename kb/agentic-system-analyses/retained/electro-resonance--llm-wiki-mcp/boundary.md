---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM-WIKI-MCP's local wiki, shipped callers and maintenance paths at frozen commit 25efb7631082fa3732723fee08e24d39b43311fa."
run-id: AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/Electro-resonance/LLM-WIKI-MCP
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-llm-wiki-mcp/related-systems/Electro-resonance--LLM-WIKI-MCP
  revision: "25efb7631082fa3732723fee08e24d39b43311fa"
  sha256: null
---

# LLM-WIKI-MCP boundary

## Boundary and evidence

The target is the shipped local-first knowledge system, not just its MCP adapter or Python retrieval API. Its intended use is to maintain local Markdown knowledge and supply that knowledge to people and model-assisted applications through a CLI, an in-process API and MCP. It qualifies as a **memory/knowledge/context-engineering system** because its retained wiki pages, sidecar notes and conversation records feed later retrieval and model prompts. The selected boundary is **whole-system**: it includes the shipped producers, maintenance commands, retained-state readers, prompt builders, model-request path and evaluators. SRC-1: `README.md`, `METHODOLOGY.md`, `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/server.py`.

The source states its intended retention and consumption sequence:

> 1. Ingest local source material into stable wiki pages.
> 2. Preserve provenance so pages can be refreshed when source files change.
> 3. Search and retrieve from the wiki rather than repeatedly throwing raw fragments at a model.
> 4. Let local agents query the wiki through context packs, CLI commands, or MCP tools.
> --- `METHODOLOGY.md`

The shipped CLI is part of this target, not an excluded enclosing application. The package declares both user-facing entry points:

> [project.scripts]
> llm-wiki-mcp = "llm_wiki_mcp.server:main"
> llm-wiki = "llm_wiki_mcp.cli:main"
> --- `pyproject.toml`

Initial tracing followed the root launchers into the package, the interactive shell into `release_ask`, the final ask implementation into evidence retrieval, context construction, Ollama synthesis and ask-turn persistence, and the MCP SDK callbacks into the tool-handler table. The Python context engine also provides direct ingestion, page creation, retrieval and maintenance. These are shipped responsibilities even when another application calls them. SRC-1: `llm_wiki_cli.py`, `llm_wiki_mcp_server.py`, `src/llm_wiki_mcp/__main__.py`, `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

The retained-state loop includes Markdown page creation and updates with indexing; provenance-aware file ingestion followed by reindexing; sidecar-note generation and combined-page retrieval; JSONL ask-turn persistence and history compression; and later prompt construction using recent conversation records. The final context-pack builder explicitly reads retained conversation history:

> history_md = release_recent_history_markdown(vault_path, limit=8, answer_chars=900)
> history_md = release_trim_to_token_budget(history_md, settings["history_budget_tokens"])
> --- `src/llm_wiki_mcp/context_api.py`

The scope includes older helper definitions as well as their later overrides and saved predecessor functions. This file repeatedly redefines ask, search and tool-dispatch functions; a declaration found earlier in the file is not by itself evidence of the final exported behavior. The initial boundary trace inspected the final ask/context-budget path and final provenance-ingestion path rather than treating the first matching definition as authoritative. SRC-1: `src/llm_wiki_mcp/context_api.py`.

### Tracked-root coverage

All top-level tracked entries at the frozen commit are classified below. Included means within the functional evidence boundary, not that every line has already been inspected. Uninspected available material is distinguished from unavailable evidence. Paths below are SRC-1 paths.

| Top-level tracked entry | Status and role | Initial inspection and limits |
| --- | --- | --- |
| `.github/` | Excluded: sponsorship metadata (`.github/FUNDING.yml`). | Tree inspected only; no conclusions about funding or governance. No retained-state responsibility identified in the tracked tree. |
| `.gitignore` | Included: generated-state/version-control policy. | Available, not yet inspected; no claim that ignore patterns enforce the documented privacy policy. |
| `AGENTS.md` | Included: developer maintenance instructions. | Read; specifies documentation updates, explicit tool tables and keeping generated state uncommitted. Not evidence that contributors complied. |
| `CLAUDE.md` | Included: parallel developer instructions. | Read; same maintenance guidance. |
| `ARCHITECTURE.md` | Included: declared page/index/notes/retrieval/model architecture. | Read as design, not proof of execution. |
| `CLI_GUIDE.md` | Included: CLI operating contract. | Available, not yet inspected; caller tracing used implementation instead. |
| `CLI_TOOLS_LIST.md` | Included: declared CLI surface. | Available, not yet inspected; no completeness claim for this reference. |
| `FUNCTION_LIST.md` | Included: declared implementation surface. | Available, not yet inspected; no reference-to-code consistency conclusion. |
| `INSTALL.md` | Included: deployment instructions. | Available, not yet inspected; installation success is not established. |
| `LICENSE` | Excluded: licensing text. | Tree inspected only; no legal interpretation. |
| `MCP_FUNCTIONS_LIST.md` | Included: MCP contract/reference. | Available, not yet inspected; actual entry point and SDK handler dispatch inspected. |
| `METHODOLOGY.md` | Included: source-native operating doctrine. | Read; ingestion, refresh, retrieval and maintenance intent. |
| `README.md` | Included: product intent, setup examples, shipped-path map and history/context guidance. | Read; operational assertions remain attributed unless supported by code. |
| `SKILLS.md` | Included: agent operating and maintenance instructions. | Read; dry-run/retrieve checks, lint/repair/reindex and local-state handling. |
| `docs/` | Included: shipped guides, maintenance procedures, prompts/operating notes and authored research narratives. | Read `docs/04_AGENTIC_ASK_AND_MEMORY.md`, `docs/05_NOTES_GRAPHS_AND_MAINTENANCE.md` and `docs/SKILLS.md`; tree inventoried the architecture/user/tool guides, demo, conversational examples, references and books. Other documents remain available, uninspected. Their titles do not establish observed operation or causal results. |
| `examples/` | Included: shipped demonstration caller and ingest fixture. | Read `examples/demo_commands.sh`; `examples/raw/example_source.md` is available, not yet inspected. The script's command sequence is source evidence, not a successful demonstration run. |
| `images/` | Excluded: `images/Startup_Screenshot.jpg`, presentation artifact. | Not inspected; no screenshot-based claims about UI or live operation. |
| `llm_wiki_cli.py` | Included: checkout CLI launcher. | Read; imports and calls package CLI `main`. |
| `llm_wiki_config.sample.jsonc` | Included: sample Ollama, history and context-budget configuration. | Read; illustrative configuration, not the actual runtime settings of an observed deployment. |
| `llm_wiki_mcp_server.py` | Included: checkout MCP launcher. | Read; imports and calls package server `main`. |
| `pyproject.toml` | Included: packaging, script entry points and optional dependencies. | Read; CLI/server scripts plus MCP and PDF/DOCX extras. |
| `src/` | Included: all executable system responsibilities. | `src/llm_wiki_mcp/__init__.py` and `src/llm_wiki_mcp/__main__.py` read. In `src/llm_wiki_mcp/server.py`, inspected store construction, seed/page writes, index rebuilding, SDK dispatch and regression harness; searched tool wrappers and LLM call locations. In `src/llm_wiki_mcp/context_api.py`, inspected context engine API, history write/load/compression, note generation, model adapter/system prompt, final context-budget builder, ask and provenance-ingest overrides; searched the definition inventory. In `src/llm_wiki_mcp/cli.py`, inspected shell initialization and ask dispatch, and inventoried command/function locations. Other implementation bodies remain available for later tracing. |
| `tests/` | Included: shipped evaluators of retained-state production and use. | Read history regression body in `tests/ask_history_context_test.py`; searched assertions in `tests/context_budget_debug_test.py` and `tests/provenance_ingest_search_test.py`. Remaining tracked tests were inventoried, including ingest, search, CLI, fallback-answer, progress and output tests. Tests were not run; assertions support intended checks, not passing results. |
| `wiki_vault/` | Included: tracked `.llm_wiki_history` command-history artifact. | Read; command strings without paired outputs. It cannot establish answers, successful ingestion, model identity or retrieval quality. No substantive populated wiki corpus accompanies this tracked directory. |

### External dependencies and evidence limits

The configured Ollama-compatible endpoint and its model weights are outside the source boundary. The system's HTTP request construction and response handling are inside it; actual provider behavior, model context capacity, inference quality and availability are not established. Optional MCP SDK, PDF and DOCX extractor implementations are external dependencies, while their adapters and declared extras are inside. No external MCP host application or consuming agent runtime is frozen here, so the analysis cannot attribute host planning, authorization, scheduling or downstream persistence to this target. SRC-1: `pyproject.toml`, `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

User input corpora, generated vault pages, live indexes, runtime histories/metrics and deployment configuration are not supplied as an inspectable deployment. The tracked command-history file does not fill that gap. This prevents conclusions about corpus quality, long-term memory effectiveness, real model answers, latency, privacy in deployment or end-to-end success. No target code, tests or examples were executed. The available code and documentation permit a complete evidence boundary without providing observed-run or causal-experiment evidence.

The frozen revision is **25efb7631082fa3732723fee08e24d39b43311fa**, verified against the acquired checkout's HEAD. The applicability cutoff is **2026-10-15**, the supplied run date. This is not a claim about later upstream changes or the repository's state on any other date. The overall evidence tier is **code-grounded**, with source-native documentation supplying separately attributed doctrine/design.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/Electro-resonance/LLM-WIKI-MCP` | 25efb7631082fa3732723fee08e24d39b43311fa | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-llm-wiki-mcp/related-systems/Electro-resonance--LLM-WIKI-MCP`. Implementation: tracked-tree inventory; launchers, packaging, package entry points, store/page/index code, MCP callbacks/harness, context API, history, notes, final ask/context and ingestion paths, CLI shell/ask, selected regression assertions and demonstration caller as detailed above. Doctrine/design: README, architecture, methodology, agent/developer instructions, sample config and selected memory/maintenance guides. | Implementation: [entry points](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/pyproject.toml), [CLI](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/cli.py), [store/server](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/server.py), [context/history/ask](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py), [history checks](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/tests/ask_history_context_test.py). Doctrine/design: [methodology](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/METHODOLOGY.md), [agent operations](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/SKILLS.md), [memory guide](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/docs/04_AGENTIC_ASK_AND_MEMORY.md). | No source-access failure identified. Available but uninspected files are marked above, not access gaps. No frozen external host/provider, populated deployment corpus, paired execution trace or experiment; therefore no observed success, answer-quality, deployment-performance or causal-effect claim. Test source and command history are not test results. |
