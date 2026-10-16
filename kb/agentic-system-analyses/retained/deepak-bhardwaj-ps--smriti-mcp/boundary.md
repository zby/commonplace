---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Smriti MCP's shipped markdown memory server, library, maintenance tools and tests at commit 8264bf9103477d9521e57b27c81dcc2e943a3230."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/Deepak-Bhardwaj-PS/smriti-mcp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/smriti-mcp-14f6928f9817/related-systems/Deepak-Bhardwaj-PS--smriti-mcp
  revision: "8264bf9103477d9521e57b27c81dcc2e943a3230"
  sha256: null
---

# Smriti MCP boundary

## Boundary and evidence

This run analyses Smriti MCP as a **memory/knowledge/context-engineering system** serving model-driven agents. Its intended use is to preserve facts, decisions, preferences and reusable project context beyond a chat. It qualifies through the memory operations it serves over MCP, not through ownership of a model-call loop (SRC-1, `src/smriti_mcp/server.py`, `README.md`). The server's shipped instructions state:

> "Smriti gives agents durable markdown memory. Store facts, decisions, "
> "preferences, project context, and reusable notes that should survive "
> "beyond the current chat."
> --- `src/smriti_mcp/server.py`

The boundary is **whole-system for the shipped Smriti artifact**, not for an enclosing agent application. Inspection traced the package command to the CLI, CLI server startup to `create_server`, tool wrappers to `MemoryStore`, and storage, reload, retrieval, trace consolidation and maintenance paths through their implementations. The Python library examples and test callers are included, not treated as external merely because they use the library API (SRC-1, `pyproject.toml`, `src/smriti_mcp/cli.py`, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`, `README.md`, `tests/test_smriti_store.py`). The installed entry point is:

> [project.scripts]
> smriti-mcp = "smriti_mcp.cli:main"
> --- `pyproject.toml`

Included functions are memory creation, metadata admission, append/update, archive/delete, filesystem reload, list/search, task recall, access reinforcement, raw trace recording and loading, consolidation suggestions and writes, supersession, health reports, frontmatter repair, wikilink maintenance, and markdown/YAML index generation and markdown index loading. These cover production, maintenance and subsequent consumption of retained state within the artifact. Agent-facing instructions and parameter descriptions in the server, host configuration examples, maintenance instructions and shipped tests are included (SRC-1, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`, `src/smriti_mcp/fix_frontmatter.py`, `QUICKSTART.md`, `FRONTMATTER_FIX.md`, `tests/test_smriti_mcp_integration.py`). Recall's returned context is explicitly materialized for a caller:

> return {
>     "query": query,
>     "count": len(memories),
>     "memories": memories,
>     "context": "\n".join(markdown_lines).rstrip() + "\n",
>     "token_budget": token_budget,
> }
> --- `src/smriti_mcp/store.py`

The semantic decision to retain information, final consolidated prose, invocation timing and use of returned context in a model's next prompt belong to an external agent or operator. They are not attributed to Smriti. The shipped consolidation tool states that division:

> "Create, append, or update a durable memory from agent-supplied consolidated content. "
> "Use after reviewing traces; Smriti records provenance but does not summarize content itself."
> --- `src/smriti_mcp/server.py`

External dependencies include Python, an accessible local filesystem, MCP/FastMCP for transport and tool serving, Pydantic for input models, and PyYAML for frontmatter/index serialization. MCP-compatible hosts such as Claude Desktop, Cline and Cursor are documented consumers; their implementations, model providers and prompts beyond the shipped examples are outside this repository boundary. Their exclusion prevents conclusions about autonomous capture policy, actual prompt injection of recall, cross-session task improvement or end-to-end agent reliability. Dependency internals are not frozen here, so source inspection supports Smriti's calls and declarations, not a full transport or dependency security assessment (SRC-1, `pyproject.toml`, `requirements.txt`, `QUICKSTART.md`, `src/smriti_mcp/server.py`, `src/smriti_mcp/frontmatter.py`).

The frozen source is the acquired repository at **8264bf9103477d9521e57b27c81dcc2e943a3230**, with applicability cutoff **2026-10-14**. The overall tier is **code-grounded**. Implementation and declared intent are distinguishable; README test-success claims and test source do not establish an observed run. No target code, tests, examples, providers or services were executed. There are no supplied execution traces, production memory corpora or causal experiments, so the boundary supports source-level mechanisms and test intent, not measured retrieval quality, performance, deployed correctness or causal benefit.

### Shipped-path coverage

All rows concern SRC-1 at the frozen commit. Included executable files and tests were read in full. Documentation was inspected as declared intent, not as an instruction to execute. No material shipped memory-loop path remains uninspected. Exclusions below are deliberate, not access failures; no source access gap was encountered.

| Top-level tracked entry | Coverage and material paths | Role and limits |
|---|---|---|
| `src/` | Included: `src/smriti_mcp/__init__.py`, `src/smriti_mcp/cli.py`, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`, `src/smriti_mcp/fix_frontmatter.py`. | Package identity; installed and module entry points; MCP instructions, schemas and wrappers; durable writes, reload, traces, recall, consolidation, review and maintenance. Covers the artifact's state loop, not external model decisions. |
| `tests/` | Included: `tests/test_cli.py`, `tests/test_smriti_store.py`, `tests/test_smriti_mcp_server.py`, `tests/test_smriti_mcp_integration.py`. | CLI dispatch, store/reload and maintenance regressions, tool registration/descriptions, stdio client create/search/get/index round trip. Inspected test callers are inside the boundary; tests were not run. No end-to-end model evaluator was found in these paths. |
| `.github/` | Included: `.github/workflows/tests.yml`; excluded after inspection: `.github/workflows/publish.yml`. | CI test declaration is evaluation context, not evidence of a passing run. Release automation does not govern retained memory; exclusion prevents assessing publication execution or release integrity. |
| `pyproject.toml` | Included, inspected. | Package dependencies, build configuration and installed CLI entry point. Does not freeze dependency implementations. |
| `requirements.txt` | Included, inspected. | Compiled dependency pins; dependency source is not acquired. |
| `README.md` | Included, inspected. | Intended memory use, file format, MCP host setup and direct library write/search/list/rebuild consumers. Success and portability claims remain documentation claims. |
| `QUICKSTART.md` | Included, inspected. | Host configuration, user invocation examples, index review and maintenance guidance; not an executable host agent or automatic recall scheduler. |
| `FRONTMATTER_FIX.md` | Included, inspected. | Shipped metadata repair instructions and declared indexing purpose; implementation remains the authority for actual behavior. References to external KB linting do not supply its implementation. |
| `CHANGELOG.md` | Included, inspected. | Attributed release intent and regression history, not independent operational evidence. |
| `CONTRIBUTING.md` | Excluded after inspection. | Contributor development/testing procedure, not agent memory maintenance. No conclusion about contributor compliance follows. |
| `PUBLISHING.md` | Excluded after inspection. | Release instructions, not the memory loop. No conclusion about successful distribution follows. |
| `PUBLICATION_CHECKLIST.md` | Excluded; tracked empty file confirmed by tree/size inspection. | Supplies no operational content or completed release evidence. |
| `.gitignore` | Excluded after inspection. | Development/build/cache ignore rules; no assessment of repository hygiene or data retention policy follows. |
| `LICENSE` | Excluded, contents not inspected. | Legal terms are outside functional analysis; no licensing conclusion follows. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Deepak-Bhardwaj-PS/smriti-mcp` | 8264bf9103477d9521e57b27c81dcc2e943a3230 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/smriti-mcp-14f6928f9817/related-systems/Deepak-Bhardwaj-PS--smriti-mcp`. Implementation: all six Python files under `src/smriti_mcp/`, all four test files under `tests/`, `pyproject.toml`, `requirements.txt`, `.github/workflows/tests.yml`. Doctrine/design: `README.md`, `QUICKSTART.md`, `FRONTMATTER_FIX.md`, server instructions and tool descriptions. Reported operation: README test-pass assertion and `CHANGELOG.md` release claims. Administrative inspection: `CONTRIBUTING.md`, `PUBLISHING.md`, `.github/workflows/publish.yml`, `.gitignore`; tracked-tree/size inventory. | Implementation: [CLI](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/src/smriti_mcp/cli.py), [server and instructions](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/src/smriti_mcp/server.py), [store](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/src/smriti_mcp/store.py), [integration test](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/tests/test_smriti_mcp_integration.py). Doctrine/design and reported operation: [README](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/README.md), [maintenance guide](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/FRONTMATTER_FIX.md), [changelog](https://github.com/Deepak-Bhardwaj-PS/smriti-mcp/blob/8264bf9103477d9521e57b27c81dcc2e943a3230/CHANGELOG.md). | No access gap in the registered checkout. Test source supplies implementation/test intent, not observed execution; documentation reports are not run artifacts. External host/dependency implementations, production memories and causal evaluations are not supplied, preventing claims about actual host context consumption, deployment behavior or demonstrated agent benefit. |
