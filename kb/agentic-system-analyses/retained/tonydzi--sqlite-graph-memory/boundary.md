---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "sqlite-graph-memory's shipped memory layer, integrations, instructions and evaluators at f05db2778159d50a0ad8a35be4f2be3a6aea94b1."
run-id: AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/tonydzi/sqlite-graph-memory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sqlite-graph-memory-91b6673f336e/related-systems/tonydzi--sqlite-graph-memory
  revision: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
  sha256: null
---

# sqlite-graph-memory boundary

## Boundary and evidence

The target is the shipped sqlite-graph-memory memory layer for agents over linked Markdown notes, not the maintainer's larger private second-brain operation. It qualifies as a memory/knowledge/context-engineering system: its MCP tool serves context to model-driven clients, and its Stop hook retains state from assistant transcripts. It need not own an enclosing generation loop. The whole-system boundary covers the published package, its CLI and MCP interfaces, post-turn capture and ledger viewer, maintenance instructions, and shipped evaluation consumers (SRC-1, `pyproject.toml`, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/turnstate_hook.py`, `examples/README.md`).

> description = "Associative memory for LLM agents: Graph RAG over a folder of markdown notes, in one SQLite file, with no server to run."
> --- `pyproject.toml`

> "Associative memory recall over linked markdown notes. "
> "Retrieves relevant context using vector search, 1-hop [[wikilink]] graph expansion, "
> "ordered by dense similarity (cross-encoder rerank is opt-in). Returns a formatted context bundle."
> --- `src/sqlite_graph_memory/mcp_server.py`

The functional boundary includes admission of Markdown files, chunking, incremental embedding-index maintenance, reload of retained vectors and snippets, query embedding, bounded link expansion and supersession following, optional cross-encoder and PageRank ordering, formatted context delivery, A/B telemetry, transcript-tail extraction, SQLite persistence and later ledger inspection. The MCP server calls the recall CLI in a subprocess and returns its per-call answer-file contents. The ledger viewer consumes the separate `turns` table; retaining that ledger does not itself establish automatic injection of its contents into later model calls. These paths were traced in SRC-1, `src/sqlite_graph_memory/index_notes.py`, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/turnstate_hook.py`, and `src/sqlite_graph_memory/turnstate_show.py`.

> sgm-index = "sqlite_graph_memory.index_notes:main"
> sgm-ask = "sqlite_graph_memory.brain_ask:main"
> sgm-stats = "sqlite_graph_memory.vault_stats:main"
> sgm-turnstate-hook = "sqlite_graph_memory.turnstate_hook:main"
> sgm-turnstate-show = "sqlite_graph_memory.turnstate_show:main"
> sgm-mcp = "sqlite_graph_memory.mcp_server:main"
> sgm-doctor = "sqlite_graph_memory.doctor:main"
> --- `pyproject.toml`

Shipped consumers are not excluded as external applications. `eval/run_eval.py` reloads the index and calls recall functions; `eval/run_ablation.py` varies admission and gating parameters. `bench/run.py` drives `bench/adapters/sgm.py`, whose setup builds and reloads an index, and whose query path adds an extractive answer and abstention rule using `bench/adapters/_extract.py`. That benchmark answer layer is included as evaluator behavior, not attributed to the deployed MCP tool. Its cross-encoder path is not the package's dense-order default (SRC-1, those paths).

> The library retrieves; it does not answer. Answers and citations come from the shared
> extractive floor in _extract.py, and abstention from one rule fixed before the first run:
> if the reranker's best score is below ABSTAIN_BELOW, say nothing.
> --- `bench/adapters/sgm.py`

Instructions are also inside the boundary. `BITEMPORAL.md` ships a portable agent instruction block for preserving validity windows; it is doctrine, not proof that every code path implements its rules. `docs/bitemporal.md` describes a persisted-edge variant and reports a private experiment. `AGENTS.md` supplies contributor maintenance and measurement rules; `FOR-ROBOTS.md`, `llms.txt`, `README.md`, and `examples/README.md` supply agent/operator guidance. Their statements can drift from the executable revision and must be attributed accordingly (SRC-1, these paths).

> A block you can paste into an agent's instruction file (`CLAUDE.md`, `AGENTS.md`,
> `.cursor/rules`, a system prompt) so the agent stops overwriting what it knew and starts
> closing it instead.
> --- `BITEMPORAL.md`

### Coverage of the frozen tree

All top-level tracked entries are classified below. Included means within the analysis boundary, not that every line has already been inspected. Initial inspection traced all package entry points and their material state producers and consumers. Support-file and evaluator detail not yet inspected remains available at the same pin; it is not an access gap.

| Top-level tracked entry | Status and material paths / role | Inspection and limit |
|---|---|---|
| `src/` | Included: `src/sqlite_graph_memory/index_notes.py`, `brain_ask.py`, `mcp_server.py`, `turnstate_hook.py`, `turnstate_show.py`, `vault_stats.py`, `doctor.py`, `onnx_backend.py`, `ppr.py`, `schema.sql`, `__init__.py` within that package | All executable entry-point modules and schema read; package initializer not yet inspected. Covers index production/reload, recall delivery, ledger write/read, diagnostics and optional ordering/backend paths. |
| `examples/` | Included: `examples/README.md`, `examples/mcp-config.json`, `examples/claude-code-stop-hook.json` | Read integration instructions and command registration; actual host execution is not supplied. |
| `eval/` | Included: `eval/build_gold.py`, `eval/run_eval.py`, `eval/run_ablation.py` | Inspected gold-builder contract, scoring loop and ablation query loop; remaining details available, not yet inspected. Evaluation is a shipped consumer, not an external host. |
| `bench/` | Included: `bench/run.py`, `bench/adapters/sgm.py`, `bench/adapters/_extract.py`, `bench/bench_core.py`, `bench/validate.py`, generators, questions, `bench/vault/`, `bench/results/`, adapter and benchmark documentation, CI helpers and leaderboard tooling | SGM adapter and extraction helper read, driver loop traced, tree inventoried. Other scoring, fixture and result details not yet inspected. Other-system adapters are benchmark context only; no characterization of those external systems is authorized. Results are supplied artifacts to inspect under their recorded conditions, not a fresh execution. |
| `docs/` | Included: `docs/bitemporal.md`, `docs/demo.sh`, `docs/demo.gif`, `docs/RELEASING.md` | Design note and demo driver read; GIF and release procedure not yet inspected. The driver is a shipped index/recall caller; display output is not independent performance evidence. |
| `README.md` | Included: public purpose, integration, maintenance, evaluation and private-operation claims | Read completely; distinguishes package from home-pipeline reports. |
| `AGENTS.md` | Included: contributor instructions and retrieval-change gates | Read as source doctrine, not authority for this analysis. |
| `FOR-ROBOTS.md` | Included: agent-facing usage and operating claims | Read; historical assertions such as absent packaging/tests cannot override the pinned code tree. |
| `BITEMPORAL.md` | Included: portable memory-maintenance prompt | Read completely; prescribed behavior is not runtime enforcement. |
| `llms.txt` | Included: agent-facing discovery and integration guide | Read completely; version/default claims require comparison with code. |
| `pyproject.toml` | Included: package dependencies, extras, build contents and all command entry points | Read completely. |
| `.env.example`, `requirements.txt`, `server.json`, `glama.json`, `context7.json` | Included: configuration, dependency and integration/discovery metadata | Tree inventoried; details not yet inspected. Dependency declarations in `pyproject.toml` were inspected. |
| `tests/` | Included: unit and contract tests, notably indexing, recall, MCP, ledger, backend, PageRank, evaluation and integration checks | Tree inventoried; assertions not yet inspected. No tests executed and no passing-suite claim follows. |
| `.github/` | Included: workflows for tests, bench, release and credit; ownership and issue metadata | Tree inventoried; workflow and policy details not yet inspected. No live CI outcome established. |
| `scripts/` | Included: `scripts/credit_gate.py`, contributor-credit support | Tree inventoried; implementation not yet inspected, not a memory-state path. |
| `paper/` | Included: `paper/paper.md`, `paper/paper.bib`, `paper/JOSS-PREP.md`, authored design/publication context | Tree inventoried; contents not yet inspected. Not independent validation of system claims. |
| `CHANGELOG.md`, `CITATION.cff`, `CONTRIBUTING.md`, `LICENSE`, `SECURITY.md`, `SUPPORT.md` | Included: history, attribution, contribution, legal and support context | Tree inventoried; detail not yet inspected. No historical, licensing or security assessment is established here. |
| `.gitattributes`, `.gitignore` | Excluded: repository transport/ignore housekeeping | Deliberate exclusion; prevents claims about complete checkout/export and ignore-policy correctness, not memory-loop characterization. |

### External responsibilities and evidence limits

External dependencies include Python, NumPy, SQLite, a local Markdown corpus, host transcript/event formats and MCP clients, and an embedding stack using ONNX Runtime/tokenizers/Hugging Face Hub or sentence-transformers/torch. The named embedding and optional cross-encoder checkpoints are selected by code; their repositories and downloaded weights are not frozen sources in this run. This prevents claims about exact model-byte reproducibility, model internals or independently measured retrieval quality (SRC-1, `pyproject.toml`, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/onnx_backend.py`).

The enclosing Claude Code, Cursor, Codex and other client implementations, note authorship outside this repository, external starter kits and the maintainer's private vault/home pipeline are excluded. Their scheduling, reasoning, note editing, automatic context reuse and private retrieval lanes cannot be attributed to this package. The repository explicitly limits publication of one such lane:

> No entity lane. The production setup has an extra retrieval lane over people/project
> cards; it is too entangled with personal data to publish.
> --- `README.md`

That unavailable private implementation prevents conclusions about the complete private system, not about the shipped package. In particular, the shipped temporal instruction block and design note do not establish implementation of a persisted temporal graph or every home-pipeline feature (SRC-1, `BITEMPORAL.md`, `docs/bitemporal.md`, `README.md`).

The frozen revision is `f05db2778159d50a0ad8a35be4f2be3a6aea94b1`, verified against checkout HEAD, with applicability cutoff 2026-11-08. No other repository, live page, package release, model download or private dataset is registered. Overall evidence is code-grounded static inspection. No target, test, example, provider or benchmark was executed for this boundary. Private operational and measurement statements remain reported operation; supplied benchmark artifacts require their own condition checks before supporting narrower conclusions. Neither source availability nor a complete disposition establishes successful deployment, general quality gains or causal experimental support.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/tonydzi/sqlite-graph-memory` | f05db2778159d50a0ad8a35be4f2be3a6aea94b1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sqlite-graph-memory-91b6673f336e/related-systems/tonydzi--sqlite-graph-memory`. Implementation: all package entry-point modules, ONNX and PPR helpers, schema, SGM benchmark adapter/extractor and driver loop, evaluation scoring and ablation loops. Doctrine/design: complete README, AGENTS, FOR-ROBOTS, BITEMPORAL, llms, example guide/configs, pyproject, bitemporal design note and demo script. Reported operation: README and bitemporal note's private-use/measurement accounts. Entire tracked tree inventoried; further same-commit paths remain eligible evidence, with initial coverage detailed above. | Implementation: [entry points](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/pyproject.toml), [MCP delivery](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/src/sqlite_graph_memory/mcp_server.py), [retained index and recall](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/src/sqlite_graph_memory/brain_ask.py), [evaluation consumer](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/bench/adapters/sgm.py). Doctrine: [portable instruction](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/BITEMPORAL.md). Reported operation: [README](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/README.md), [temporal report/design](https://github.com/tonydzi/sqlite-graph-memory/blob/f05db2778159d50a0ad8a35be4f2be3a6aea94b1/docs/bitemporal.md). | No access gap within the frozen public checkout. Private vault, private home code, actual host sessions, external weights and live services are not supplied: cannot establish private-system completeness, production outcomes, model-byte equivalence or causal gains. Not-yet-inspected support files are available evidence, not unavailable sources. |
