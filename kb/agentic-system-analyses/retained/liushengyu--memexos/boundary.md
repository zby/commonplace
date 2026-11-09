---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MemexOS's shipped knowledge production, maintenance and retrieval loop at commit bb9e9b2ac0adbca87d13a9f7600867128b5f71b9."
run-id: AAS-2026-11-07-memexos-5cd34a715eb7-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
analysis-cutoff: "2026-11-07"
evidence-tier: code-grounded
source:
  identity: https://github.com/liushengyu/memexos
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/memexos-4460a2f51a56/related-systems/liushengyu--memexos
  revision: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
  sha256: null
---

# MemexOS boundary

## Boundary and evidence

This run examines MemexOS as a personal knowledge system that admits sources, compiles retained knowledge with model workers, maintains it, and returns it to later agent sessions. The target class is **memory/knowledge/context-engineering system**. The boundary is **whole-system**, not just its search API or compiler library. Its shipped CLI, scheduled driver, console actions, prompts, vault instructions and evaluators belong to the target. External agents that ask ordinary user questions remain consumers, but the shipped code and instructions that connect those consumers to retained state are included. This classification follows the declared purpose and the traced CLI-to-intake, compile-to-publication, retrieval and feedback paths (SRC-1: `README.md`, `pyproject.toml`, `src/memexos/cli.py`, `src/memexos/intake/admit.py`, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`, `src/memexos/search/cli.py`, `src/memexos/usage.py`).

The purpose is explicit in the package metadata:

> description = "A memory OS for you and your agents: agents compile what you collect into a verified, searchable wiki."
> --- `pyproject.toml`

Model-dependent production is not merely proposed integration. The compiler invokes a writer in its staging directory (SRC-1, implementation):

> return backends.agent(self.cfg, "writer", prompt, cwd=self.stage.dir, workdir=wd, policy=self.policy(),
>                               timeout=float(self.cfg.get("pipeline.writer_timeout") or 5400), job=self.job)
> --- `src/memexos/pipeline/compile.py`

The functional boundary includes capture and session intake; admission and source classification; raw and wiki files and machine ledgers; staged writing, checks, review, rework, publication and holding; index building and search/get; feedback verification and repair; inbox decisions; scheduled maintenance; console control and observability; and retrieval, review and tool-use evaluation. The entry point is `memexos.cli:main`, also reached through `python -m memexos`. Its command map dispatches these responsibilities rather than leaving them to an unspecified enclosing application (SRC-1: `pyproject.toml`, `src/memexos/__main__.py`, `src/memexos/cli.py`).

Initial implementation tracing established the loop's ownership: intake calls admission, post-processes outputs and commits retained sources; ingest builds a classification-bearing compile prompt, runs the writer and review loop, updates ledgers and calls publication; publication merges into the vault, updates full-text search and starts background reindexing. Search returns ranked hits and get reloads file contents. Usage verification produces review-format fix jobs, and the nightly driver invokes intake, configured maintenance steps and ingest. Inbox application uses the same staged writer and review machinery. Console actions start these CLI jobs and record decisions. These are boundary-establishing traces, not a correctness finding about every branch or configuration (SRC-1: `src/memexos/intake/admit.py`, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`, `src/memexos/search/cli.py`, `src/memexos/usage.py`, `src/memexos/schedule.py`, `src/memexos/inbox.py`, `src/memexos/console/actions.py`).

Later consumption is an explicit shipped instruction, not inferred from the presence of Markdown files (SRC-1, doctrine/design):

> 1. Find pages with `memex search "<question>" --kw "<keywords>"` (`memex help` explains the options). `index.md` lists
>    every page; it is for browsing a small knowledge base, not for searching a large one
> 2. Read the relevant pages with `memex get <page>`
> --- `src/memexos/templates/vault/en/AGENTS.md`

The evaluator also ships a concrete caller that exercises the CLI from outside the vault (SRC-1, implementation):

> r = backends.agent(cfg, "@" + agent, prompt, cwd=work, workdir=d / "l2" / rid, policy=pol, effort="medium",
>                                timeout=float(cfg.get("evals.l2_timeout") or 1200), job="eval")
> --- `src/memexos/evals/retrieval.py`

### Frozen evidence and limits

The sole frozen source is SRC-1 at **bb9e9b2ac0adbca87d13a9f7600867128b5f71b9**, verified against the acquired checkout's HEAD. The applicability cutoff is **2026-11-07**, the supplied run date. No moving branch, linked external repository or live documentation is evidence for this run. The evidence tier is **code-grounded**: implementation text is available alongside the project's doctrine/design. No target code, tests, examples, model calls or services were executed.

External dependencies include model CLIs and model APIs, optional judging services, qmd and its local models, browser and collection tools, transcription tools, Git and operating-system scheduling facilities. MemexOS's adapters and invocation policies are included; those dependencies' internal implementations and their independently evolving versions are excluded. This prevents conclusions about provider quality, actual sandbox enforcement inside external runtimes, live collection availability or the internals of external retrieval and transcription models. Ordinary consuming agents' own task reasoning is excluded, so the run cannot attribute their search decisions or final answers to MemexOS alone (SRC-1: `README.md`, `docs/architecture.md`, `src/memexos/backends/base.py`).

There is no established source access gap. Available material not yet read in depth is distinguished below from exclusion. Whole-system denotes the selected functional scope and traced material loop, not exhaustive inspection or successful operation. No real user vault or longitudinal deployment trace was supplied; sample content and shipped evaluation artifacts cannot establish production durability or general retrieval quality. Any later use of the shipped evaluation results must inspect their own conditions before making performance claims.

### Top-level coverage

All rows refer to SRC-1 at the frozen revision. Grouped rows enumerate their top-level entries explicitly. “Included” retains the path within analytical scope; inspection status records the boundary worker's initial coverage rather than an allowlist for subsequent source reading.

| Top-level tracked entry | Classification and material paths/role | Initial inspection and consequence |
|---|---|---|
| `src/` | Included: `src/memexos/cli.py`, `__main__.py`; `intake/` and `capture/` produce sources; `catalog/` classifies; `pipeline/` stages, checks, reviews and publishes; `search/` reloads and returns knowledge; `usage.py`, `inbox.py`, `schedule.py` maintain the loop; `console/` reads state and starts work. | CLI map inspected; intake orchestration, writer/review/ingest, staging publication, search/get, usage verification, nightly driver, inbox application and console actions traced. Lower-level capture, catalog, backend and search implementations remain available for detailed analysis, not excluded or inaccessible. |
| `src/` (instruction and evaluation assets) | Included: `src/memexos/prompts/{en,zh}/`, `templates/vault/{en,zh}/`, `help/`, `locale/`, `scaffold.py`, `default_config.toml`, `evals/`, `examples/sample-vault/`. These ship the maintenance contract, task prompts, initialization, consumer help and evaluators. | English vault rules and compile prompt read; scaffold and evaluator entry paths searched; retrieval evaluator's external-directory caller read. Other prompts, translations, fixtures and evaluator branches are not yet inspected in depth; no equivalence or score claim follows from their existence. |
| `README.md` | Included: purpose, installation, consumer integration, role and command overview. | Read completely; claims treated as doctrine/design, not verified runtime guarantees. |
| `README.zh-CN.md` | Included: Chinese-language public contract. | Tree inventoried; text not yet inspected. No translation-equivalence conclusion. |
| `docs/` | Included: `architecture.md`, `evals.md`, `console.md`, `install-prompt.md`; `images/` supplies illustrations. | Architecture and evaluation descriptions read; remaining text and images not yet inspected. Illustrations alone do not establish observed operation. |
| `evals/` | Included: `results/2026-11-03-tooluse-sample/` report, summary and README. | Inventoried, not yet read. No quantitative result adopted at boundary stage; these are target-authored evaluation evidence, not an independent deployment study. |
| `tests/` | Included: pipeline, search, backends, scheduling, console, evaluation and tool-use tests; `conftest.py`, `fakes/fake_cli.py`. | Tracked names inventoried; assertions not yet inspected and tests not run. No test-pass claim. |
| `tools/` | Included: `make_demo.py`, `demo_content.py`, `leak_scan.py`. | Inventoried, not yet inspected; demo-generation and release hygiene remain within source scope, without claims that generated displays show real users. |
| `install.sh` | Included: shipped environment bootstrap. | Inventoried; not yet inspected or executed. No fresh-install success claim. |
| `pyproject.toml` | Included: package contract, CLI entry point, dependencies and tooling configuration. | Read completely; establishes shipped entry point, not installed availability. |
| `uv.lock` | Included: frozen development dependency resolution. | Inventoried; not yet inspected. No dependency audit. |
| `.github/` | Included: `workflows/ci.yml`, `ci-retry.yml`, issue templates, CODEOWNERS, Dependabot and pull-request template. | Inventoried, not yet inspected. No independent CI-success or release-governance finding. |
| `.githooks/` | Included: `pre-commit` repository hygiene hook. | Inventoried; not yet inspected or run. No hook-effectiveness claim. |
| `.gitignore`, `.leakscan-allow`, `.leakscan-allow-terms` | Included: repository exclusion and leak-scan configuration. | Inventoried; not yet inspected. No secret-exposure audit. |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE` | Included: contribution, community, security-reporting and licensing contracts. | Inventoried; not yet inspected. No legal or security-process assessment. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/liushengyu/memexos` | bb9e9b2ac0adbca87d13a9f7600867128b5f71b9 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/memexos-4460a2f51a56/related-systems/liushengyu--memexos`. Tracked tree inventoried. Implementation: package metadata and module entry point; CLI command map; targeted ranges of intake/admit, pipeline/compile and stage, schedule, search/cli, usage, inbox, console/actions, backends/base and evals/retrieval; scoped searches of scaffold and evals/tooluse. Doctrine/design: complete README, architecture and eval docs, English vault AGENTS and compile prompt. Other tracked paths remain available under this same source identity. | [Entry point](https://github.com/liushengyu/memexos/blob/bb9e9b2ac0adbca87d13a9f7600867128b5f71b9/src/memexos/cli.py); [compiler](https://github.com/liushengyu/memexos/blob/bb9e9b2ac0adbca87d13a9f7600867128b5f71b9/src/memexos/pipeline/compile.py); [vault contract](https://github.com/liushengyu/memexos/blob/bb9e9b2ac0adbca87d13a9f7600867128b5f71b9/src/memexos/templates/vault/en/AGENTS.md); [architecture](https://github.com/liushengyu/memexos/blob/bb9e9b2ac0adbca87d13a9f7600867128b5f71b9/docs/architecture.md) | No known checkout access gap. Implementation text supports code-path analysis; doctrine supports intended operation only. No independent observed run or causal experiment established. External dependencies and live user state are outside the frozen source, preventing conclusions about their actual operation or longitudinal effectiveness. |
