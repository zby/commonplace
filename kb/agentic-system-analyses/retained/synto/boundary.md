---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Synto's shipped knowledge-production, review, maintenance and consumption paths at commit 91ac6a3681df0552b6c9baef159439c7ebd780c9."
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/kytmanov/synto
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/synto-eabcdcce3da2/related-systems/kytmanov--synto
  revision: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
  sha256: null
---

# Synto boundary

## Boundary and evidence

Synto is in scope as a model-dependent knowledge system, not merely a pack-reading library or an MCP wrapper. Its intended use is to turn private source notes into retained, linked wiki articles and portable knowledge packs, then provide those artifacts to people and agents. The analysis covers the shipped system at `91ac6a3681df0552b6c9baef159439c7ebd780c9`, with an applicability cutoff of 2026-10-15. It is code-grounded: executable source establishes available paths; documentation and prompts establish declared intent. No target code, tests, examples, providers or services were executed.

The registered checkout's HEAD matches the acquired full commit and its status was clean. This commit is the evidence identity; the local checkout is only its read-only access root. No other repository, live page, installed release, model output or user vault is included.

### Functional boundary

The boundary is **whole-system** for Synto's shipped knowledge lifecycle. It includes source import and segmentation, model-driven ingestion and compilation, persistent metadata and Markdown, draft admission and rejection, structural maintenance and identity curation, index generation, saved answers and synthesis, pack export and its generated agent instructions, direct query, MCP serving, and shipped evaluation drivers. Same-repository CLI callers and the watcher remain inside this boundary; they are not excluded hosts.

The package registers `synto.cli:cli` as its command entry point (SRC-1, `pyproject.toml`). Its CLI builds the router with a database-backed cache, and its watcher callback invokes the orchestrator under a pipeline lock (SRC-1, `src/synto/cli.py`). This establishes a shipped driver beyond library interfaces:

> report = orchestrator.run(
>     paths=md_paths,
>     auto_approve=auto_approve or config.pipeline.auto_approve,
>     fix=config.pipeline.auto_maintain,
>     on_stage=_on_stage,
> )
> --- `src/synto/cli.py`

The inspected lifecycle paths establish the following scope, not a claim that generated knowledge is accurate:

- **Produce and persist:** `add` archives original documents, records source metadata, extracts PDF segments and writes canonical raw Markdown; ingestion calls the fast endpoint with source-type prompts and persists note analysis; compilation selects concepts, gathers sources and writes article drafts and database records (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/compile.py`).
- **Admit and revise:** publication writes the destination and updates database state before deleting a draft; rejection can retain feedback and reset compilation state; the next concept-writing prompt can include previous rejection feedback (SRC-1, `src/synto/pipeline/compile.py`). Review helpers load drafts and rejection history; maintenance and concept-curation commands are part of the same shipped application (SRC-1, `src/synto/pipeline/review.py`, `src/synto/pipeline/maintain.py`, `src/synto/cli.py`).
- **Reload and consume:** the query path loads an index, uses a fast-model page selection, reloads selected pages and requests a heavy-model answer. Its optional save paths retain Q&A or synthesis. `QueryEngine` delegates to that core; MCP `answer_question` builds the model router and invokes the engine. These consumers belong to Synto, even though external agents can also consume exported files (SRC-1, `src/synto/pipeline/query.py`, `src/synto/engines.py`, `src/synto/serve.py`).
- **Export and evaluate:** the exporter reads retained vault state and emits articles, source material, indexes, routing metadata and generated `AGENTS.md`/`CLAUDE.md`. `VaultReader` reloads published records and files; `PackReader` reads exported metadata. The offline evaluator reads a vault; the comparison runner creates separate contestant vaults, runs the orchestrator, queries them and retains reports (SRC-1, `src/synto/pack_export.py`, `src/synto/readers.py`, `src/synto/pipeline/eval.py`, `src/synto/compare/runner.py`).

The generated pack instructions explicitly direct later consumption, rather than leaving the consumer contract wholly to an external host (SRC-1, `src/synto/pack_export.py`):

> "1. Scan `index/INDEX.json` → `articles[].summary` — often answers simple questions"
> " without opening files.\n"
> "2. For detail, open the article file."
> " Citations ([S1], [S2]) link to files in `sources/`.\n\n"
> --- `src/synto/pack_export.py`

### Repository coverage

The tracked top-level tree was enumerated before classification. “Included” identifies the functional evidence boundary, not exhaustive line-by-line inspection. The material paths below were traced by source reading or scoped searches. Secondary implementation details remain available to later jobs at the same commit; they are not access gaps. No material lifecycle path was found unavailable.

| Top-level tracked path | Decision and role | Inspected material paths or scope; exclusion limit |
|---|---|---|
| `.github/` | Included: shipped evaluation and release automation | Scoped inspection of `workflows/ci.yml`, `workflows/benchmark.yml`, `workflows/release.yml`: test, benchmark and portability invocations. `FUNDING.yml` excluded as sponsorship metadata; no conclusions about funding. Workflow definitions are not evidence of successful runs. |
| `.gitignore` | Included: repository versus local-artifact boundary | Read file, including exclusion of database and test artifacts. Does not establish behavior of user vaults. |
| `CHANGELOG.md` | Excluded: release-history narrative | Enumerated, not used as behavior evidence. Prevents conclusions about historical evolution or regressions from changelog claims. |
| `CLAUDE.md` | Included: shipped maintainer instructions and declared architecture | Read completely; development/testing conventions, lifecycle and synthesis rules. This root file is distinct from generated pack instructions. |
| `LICENSE` | Excluded: project licensing text | Enumerated; no legal or redistribution assessment. Source-access behavior remains included in runtime code. |
| `README.md` | Included: intended use and operator workflows | Read completely: import, review, curation, watch, query, packs, MCP, maintenance and evaluation. External linked testimonials and systems were not followed. |
| `RELEASE.md` | Excluded from functional mechanism claims: release administration | Read completely to establish role. No claim that publication followed the described process. |
| `docs/` | Included: source-acquisition integration instructions | Read `web-clipper-setup.md`: browser/manual acquisition into `raw/`, followed by watch/ingest. `img/setup.png` excluded as illustrative UI imagery; no screenshot-derived setup claims. |
| `install.py` | Excluded from knowledge-lifecycle mechanisms: installer | Inspected bootstrap header and initial helpers; not a vault-state producer or query driver. Installation correctness and platform support are not established. |
| `pyproject.toml` | Included: package identity, command and dependencies | Read completely: console entry point, Python requirement, package layout and dependencies. |
| `scripts/` | Included: shipped smoke, benchmark and comparison drivers | Enumerated all scripts; scoped searches of `smoke_test.sh`, `compare_smoke.sh`, feature smokes, `mcp_smoke.py`, `portability_smoke.py` and `benchmark.sh`. Feature-identity smoke describes a live initial pipeline plus deterministic curation fixtures. `release.sh` excluded from functional analysis as distribution tooling. No script was run; no pass rate or operational reliability inferred. |
| `src/` | Included: complete shipped application, not a library-only slice | `synto/cli.py` command registration, dependency wiring, import, query, watcher, serving and maintenance; `watcher.py`; `pipeline/orchestrator.py` read completely; `pipeline/ingest.py`, `pipeline/compile.py`, `pipeline/review.py`, `pipeline/maintain.py`; `pipeline/prompts/__init__.py` and `notes.md`; `state.py`; `readers.py`; `engines.py`; `serve.py`; `pack_export.py`; `indexer.py`; `pipeline/eval.py`; `compare/runner.py`. Remaining provider/configuration, schema, extraction, cache, filesystem, metrics and formatting modules are included supporting implementation, enumerated but not exhaustively inspected at boundary declaration. The other six source-type prompt files are included and their loader traced; their individual wording is not yet inspected. |
| `tests/` | Included: authored checks, fixtures and evaluation inputs | Enumerated tests, `compare_corpus/`, `eval/` and `fixtures/`; scoped searches of `test_source_prompts.py`, `test_phase1a_eval.py`, `test_orchestrator.py` and benchmark invocation. Test definitions and corpus existence do not establish observed outcomes or knowledge quality. |
| `uv.lock` | Excluded from mechanism analysis: dependency resolution artifact | Enumerated; dependency reproducibility and transitive supply-chain behavior are not assessed. Direct dependency declarations remain included in `pyproject.toml`. |

### Dependencies and conclusion limits

Model inference is supplied by configured local or remote providers, not implemented model weights inside this repository. Their internals, quality, availability, latency and privacy guarantees are outside the boundary. Python, SQLite, filesystem/Git operations, PDF extraction, watchdog and MCP libraries are dependencies; this analysis may establish how Synto calls them, not their independent correctness (SRC-1, `pyproject.toml`, `src/synto/state.py`, `src/synto/watcher.py`, `src/synto/cli.py`).

External editors, Obsidian/browser clippers, MCP clients, agent hosts, proxies and human review judgments are excluded applications or actors. The shipped integration instructions, server handlers and generated pack instructions are included; actual host compliance, authentication supplied by deployment infrastructure, human review quality and downstream task improvement are not established (SRC-1, `docs/web-clipper-setup.md`, `README.md`, `src/synto/serve.py`, `src/synto/pack_export.py`).

No user vault, retained execution trace or model-comparison result was supplied. This prevents conclusions about achieved accuracy, sustained self-improvement, scaling or real deployments. Source-native examples and reports in documentation remain attributed claims. The evaluator's implemented boundary is structural/offline, not a demonstrated live-agent evaluation (SRC-1, `src/synto/pipeline/eval.py`):

> "synto eval --live is not implemented in Phase 1A. Use offline mode without --live."
> --- `src/synto/pipeline/eval.py`

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/kytmanov/synto` | 91ac6a3681df0552b6c9baef159439c7ebd780c9 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/synto-eabcdcce3da2/related-systems/kytmanov--synto`. Implementation: tracked tree, entry-point metadata and initially inspected lifecycle, persistence, consumer, export and evaluation paths identified above. Doctrine/design: full `README.md`, root `CLAUDE.md`, `docs/web-clipper-setup.md`, source-type prompt loader and notes prompt, concept-writing prompt and generated pack instructions. | Implementation: [entry point](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/pyproject.toml), [CLI drivers](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/src/synto/cli.py), [orchestrator](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/src/synto/pipeline/orchestrator.py), [query](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/src/synto/pipeline/query.py), [export and instructions](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/src/synto/pack_export.py). Doctrine/design: [README](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/README.md), [notes prompt](https://github.com/kytmanov/synto/blob/91ac6a3681df0552b6c9baef159439c7ebd780c9/src/synto/pipeline/prompts/notes.md). | No checkout access gap identified. Listed paths record initial inspection, not an allowlist. No observed-run or causal-experiment layer: no execution, user-vault evidence or measured result was supplied. Excluded external services and hosts prevent independent conclusions about inference quality, deployment security, host compliance or downstream effectiveness. |
