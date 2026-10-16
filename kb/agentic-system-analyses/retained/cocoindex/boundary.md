---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "CocoIndex's incremental context-indexing framework and shipped consumers at commit 1639793b3602408a9cb220728fb30e306d433473."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/cocoindex-io/cocoindex
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-cocoindex/related-systems/cocoindex-io--cocoindex
  revision: "1639793b3602408a9cb220728fb30e306d433473"
  sha256: null
---

# CocoIndex boundary

## Boundary and evidence

The target is CocoIndex's shipped incremental data-processing and context-indexing system, including its Python and Rust interfaces, state engine, connectors, operations, authoring guidance, example applications and their retrieval consumers. The intended use of this analysis is to explain how source material becomes retained, maintained and subsequently retrieved context. It is not an analysis of an enclosing autonomous agent. Classification is **memory/knowledge/context-engineering system**, with a **whole-system** boundary: indexing and maintenance are central, but shipped query programs and pipeline drivers remain inside the boundary rather than being dismissed as external API callers. SRC-1: `pyproject.toml`, `examples/text_embedding/main.py`, `examples/entire_session_search/main.py`, `rust/sdk/cocoindex/src/app.rs`.

The package states its indexing responsibility directly:

> description = "With CocoIndex, users declare the transformation, CocoIndex creates & maintains an index, and keeps the derived index up to date based on source update, with minimal computation and changes."
> --- `pyproject.toml`

The in-scope classification does not imply that every pipeline uses a generative model. The shipped text-embedding application creates embeddings, declares rows in PostgreSQL and later reads those retained rows through a query path. The session-search application similarly indexes checkpoint files and retrieves session content. These are concrete context-serving uses, not solely an inference from marketing. SRC-1: `examples/text_embedding/main.py`, `examples/entire_session_search/main.py`.

> async def query_once(
>     pool: asyncpg.Pool,
>     embedder: SentenceTransformerEmbedder,
>     query: str,
>     *,
>     top_k: int = TOP_K,
> ) -> None:
>     query_vec = await embedder.embed(query)
> --- `examples/text_embedding/main.py`

### Entry points and state-loop coverage

Initial inspection traced these material responsibilities at the frozen revision:

- **Start and maintain:** the Python package installs `cocoindex.cli:cli`; the CLI's update command loads an application and invokes `app.update`, including live and full-reprocessing modes. Python `App.update` constructs the root processor and calls the core binding. The Rust SDK separately calls the same core application engine, so it is included rather than treated as a third-party host. SRC-1: `pyproject.toml`, `python/cocoindex/cli.py`, `python/cocoindex/_internal/app.py`, `rust/sdk/cocoindex/src/app.rs`.
- **Produce and admit:** the text example walks Markdown sources, mounts file processors, splits text, embeds chunks and declares target rows. LocalFS exposes snapshot and live directory walking. The core admission module supplies per-app inflight tokens and parent-to-child loans. SRC-1: `examples/text_embedding/main.py`, `python/cocoindex/connectors/localfs/_source.py`, `rust/core/src/engine/admission.rs`.
- **Retain and reload:** core component memo lookup restores prior memoization and may revalidate states before reuse. Submit-session code writes function memo records, ownership and user state. The storage documentation identifies LMDB as the internal store; this is separate from the external stores holding indexed content. SRC-1: `rust/core/src/engine/component.rs`, `rust/core/src/state_store/submit_session.rs`, `docs/src/content/docs/advanced_topics/internal_storage.mdx`.
- **Apply and retire:** the PostgreSQL row handler separates upserts and deletes; core application drop drains live components, deletes the root and clears per-app stored state. CLI reset and drop are shipped maintenance controls, not outside operators invented for this analysis. SRC-1: `python/cocoindex/connectors/postgres/_target.py`, `rust/core/src/engine/app.rs`, `python/cocoindex/cli.py`.
- **Consume:** text-embedding and session-search query programs embed queries, select retained content by vector distance and display results. Their query functions are included even though they use database clients directly instead of a CocoIndex retrieval API. SRC-1: `examples/text_embedding/main.py`, `examples/entire_session_search/main.py`.
- **Guide and evaluate:** the public skill supplies pipeline-writing and maintenance patterns; repository agent instructions describe contributor checks. Component-memo test source specifies repeated-update and deletion expectations. The state-store benchmark describes cold, warm and drop phases, not answer-quality evaluation. These are design and evaluation artifacts, not evidence that the checks passed in this run. SRC-1: `skills/cocoindex/SKILL.md`, `AGENTS.md`, `python/tests/core/test_component_memo.py`, `benchmarks/state_store/README.md`.

A minimal implementation anchor for retained-state reuse is:

>     let memo = match use_or_invalidate_component_memoization(comp_ctx, memo_fp).await {
>         Ok(memo) => memo,
>         Err(err) => {
>             error!("component memoization restore failed: {err:?}");
>             None
>         }
>     };
> --- `rust/core/src/engine/component.rs`

The shipped instruction layer makes its maintenance contract explicit:

> By default, `app.update()` runs in **catch-up mode**: it scans all sources, processes what changed since the last run (memoized components are skipped), syncs target states, and returns. Each call still has to scan sources to discover changes.
> --- `skills/cocoindex/SKILL.md`

### Top-level coverage

Every top-level tracked entry is classified below. Included means part of the functional evidence boundary, not that every file has been audited. The inspection column distinguishes direct initial reads, bounded code inspection and tree inventory. Unread material remains available at the same commit for later jobs; it is not an access gap. Whole-system here covers the shipped state loop and its supporting surfaces, not an exhaustive implementation verification.

| Top-level tracked entry | Classification and material paths / role | Initial inspection and limits |
|---|---|---|
| `python/` | Included: `cocoindex/cli.py`, `_internal/app.py`, `_internal/runner.py`, connectors, resources, operations and `tests/`; public entry, processing, external persistence and evaluation. | Read package metadata and text pipeline; inspected CLI update/drop/init, App update/drop, LocalFS walk, PostgreSQL row handler, LiteLLM module beginning, and component-memo test beginning. Other connectors, operations and tests are inventoried, not individually audited. SRC-1. |
| `rust/` | Included: `core/src/engine/`, `core/src/state_store/`, `core/src/state/`, `core/src/inspect/`; `py/`, `sdk/`, `py_utils/`, `utils/`, `code_ast/`, `code_match/`, `ops_text/`; engine, storage, bindings, second SDK and transformation support. | Inspected core application update/drop, admission introduction, component memo lookup, submit-session writes and Rust SDK update/drop; inventoried crates and binding entry points. Other internals remain uninspected, not unavailable. SRC-1. |
| `examples/` | Included: `text_embedding/main.py`, `entire_session_search/main.py`, graph/extraction pipelines, `sec_edgar_analytics/search.py`, image-search API programs, and Rust examples. Shipped producers, drivers and retained-content consumers. | Full text-embedding read; session indexing/query tail read; bounded search and tree inventory of other callers. These callers are not excluded merely because they instantiate the library or query stores directly. SRC-1. |
| `skills/` | Included: `cocoindex/SKILL.md` and `references/`; shipped agent-facing authoring, configuration and maintenance guidance. | Public skill read fully; reference paths inventoried through its own resource list, not fully inspected. SRC-1. |
| `docs/` | Included: `src/content/docs/` programming, internal-storage, connector and ops contracts; `src/content/example-posts/`; documentation site and skill-serving routes. | Internal-storage page read; content and site tree inventoried. Other pages and site-serving implementation have not been audited. SRC-1. |
| `benchmarks/` | Included: state-store, entity-resolution and file-summarization benchmark artifacts, including Python/Rust drivers where shipped. | State-store README read; benchmark tree inventoried. No benchmark executed and no performance result adopted. SRC-1: `benchmarks/state_store/README.md`. |
| `dev/` | Included as contributor support: `agent-skills/`, `agent-checks/`, scripts, database service configurations, plans and Rust guidelines. | Tree inventory and references in `AGENTS.md`; individual scripts and plans not inspected. Not evidence of production behavior. SRC-1. |
| `.agents/` | Included: skill-discovery symlinks to public skill and contributor playbooks. | Tracked symlink inventory; not an additional execution runtime. SRC-1: `AGENTS.md`. |
| `.claude/` | Included: contributor skill symlinks, settings, hooks and launch configuration. | Tracked paths inventoried; descriptions read in `AGENTS.md`; hooks not audited. No conclusion about their effectiveness. SRC-1. |
| `AGENTS.md`, `CLAUDE.md` | Included: repository contributor instructions and compatibility entry. | `AGENTS.md` read fully; compatibility relationship declared there. These instructions are evidence, not authority to execute target setup. SRC-1: `AGENTS.md`. |
| `README.md` | Included: project intent, public entry example and external-product references. | Read fully; performance and enterprise claims are attributed intent/reporting only, not measured results. SRC-1. |
| `pyproject.toml`, `Cargo.toml`, `uv.lock`, `Cargo.lock` | Included: package/build entry points, workspace and dependency pins. | Python manifest read fully; others inventoried. Dependency internals are not frozen by these lockfiles. SRC-1: `pyproject.toml`. |
| `.github/` | Included as evaluation/release support: workflows, scripts, issue templates and security policy. | Tree inventory only; no CI run evidence inspected. Cannot establish passing builds or release provenance. SRC-1: `AGENTS.md`. |
| `.cargo/`, `.env.lib_debug`, `.gitignore`, `.gitleaks.toml`, `.lycheeignore`, `.pre-commit-config.yaml`, `.python-version`, `ruff.toml` | Included as build, development and check configuration. | Top-level inventory, with contributor check role declared in `AGENTS.md`; contents not individually inspected. No configuration-effectiveness claim. SRC-1. |
| `context7.json` | Included as documentation-discovery support. | Top-level inventory only; contents uninspected. No conclusion about external documentation indexing. SRC-1. |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, `about.hbs`, `about.toml` | Excluded from operational mechanism analysis: contribution/governance, licensing and notice-generation surfaces. | Inventory only. Prevents a legal-compliance, governance or attribution-generation assessment; does not remove shipped processing or retrieval paths. |

### Dependencies, exclusions and evidence limits

External source systems, databases, object stores, model providers, model weights and dependency implementations are outside this single-repository pin. Their **shipped adapters and example call sites remain included**. Thus the boundary supports source-grounded descriptions of calls and requested effects, not independent claims about provider accuracy, database guarantees or deployment availability. SRC-1: `pyproject.toml`, `python/cocoindex/connectors/postgres/_target.py`, `python/cocoindex/ops/litellm.py`, `examples/text_embedding/main.py`.

The separately linked CocoIndex-code product, external websites, hosted documentation revisions and enterprise deployments are not acquired sources. This prevents conclusions about that product's MCP/tool loop, real agent adoption of retrieved context, hosted behavior and enterprise-scale performance. The README links and claims do not freeze their implementation. SRC-1: `README.md`.

No source-access failure was encountered: HEAD matched the acquired full commit and the working tree was clean. Available but uninspected files are distinguished above from deliberate exclusions. No target code, tests, examples or provider calls were executed. No observed-run trace or causal experiment is supplied. The overall tier is **code-grounded**: executable source supports the boundary, while documentation and skills supply declared intent. Source-only tests and benchmarks cannot establish observed reliability, latency, retrieval quality or causal benefit.

The applicability cutoff is **2026-10-15**, the supplied run date, limited to repository revision **1639793b3602408a9cb220728fb30e306d433473**. It is not a claim about later releases or the state of external services on that date.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cocoindex-io/cocoindex` | 1639793b3602408a9cb220728fb30e306d433473 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-cocoindex/related-systems/cocoindex-io--cocoindex`. Implementation: package entry metadata; Python CLI update/drop/init, App update/drop and runner; LocalFS walk API; PostgreSQL row application; LiteLLM module beginning; core application update/drop, admission introduction, memo lookup and submit-session writes; Rust SDK update/drop; text-embedding pipeline/query; session-search indexing/query; component-memo test source. Doctrine/design: full README, AGENTS, public skill, internal-storage page and state-store benchmark README. Remaining coverage is the explicit inventory above, not an assertion of inspected behavior. | Implementation: [package entry](https://github.com/cocoindex-io/cocoindex/blob/1639793b3602408a9cb220728fb30e306d433473/pyproject.toml), [core application](https://github.com/cocoindex-io/cocoindex/blob/1639793b3602408a9cb220728fb30e306d433473/rust/core/src/engine/app.rs), [producer and consumer](https://github.com/cocoindex-io/cocoindex/blob/1639793b3602408a9cb220728fb30e306d433473/examples/text_embedding/main.py). Doctrine/design: [public skill](https://github.com/cocoindex-io/cocoindex/blob/1639793b3602408a9cb220728fb30e306d433473/skills/cocoindex/SKILL.md), [storage contract](https://github.com/cocoindex-io/cocoindex/blob/1639793b3602408a9cb220728fb30e306d433473/docs/src/content/docs/advanced_topics/internal_storage.mdx). | No encountered repository access gap. No execution trace, external dependency implementation, separate product repository or live service capture: prevents observed-operation, provider-guarantee and end-to-end agent-effectiveness conclusions. |
