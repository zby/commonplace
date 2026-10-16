---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MemPalace's shipped memory system, agent integrations and evaluators at commit 1392e1810c3ca67776bd7fe3e198788a96dbd6d1."
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/milla-jovovich/mempalace
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mempalace-ed71875aea5a/related-systems/milla-jovovich--mempalace
  revision: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
  sha256: null
---

# MemPalace boundary

## Boundary and evidence

This run characterizes MemPalace as a shipped memory/knowledge/context-engineering system. Its intended use is persistent conversation and project memory for agents: import or capture content, organize and maintain retained state, retrieve it later, and supply it to an agent. The boundary is **whole-system**, not the storage API alone. It includes the Python package, optional native engine, shipped agent-facing instructions, host adapters, save hooks, coordination/task drivers, maintenance paths and evaluators at the frozen revision. These are responsibilities shipped by the target, even where an external harness invokes them. SRC-1: `README.md`, `pyproject.toml`, `mempalace/cli/__init__.py`, `mempalace/integrations/hermes/__init__.py`, `.dsh-plugin/cordis.patch.yml`.

The classification does not require MemPalace to own the enclosing agent loop or issue a generative model call on every retrieval. It serves model-dependent operation through MCP, recall instructions and host memory adapters. Its ordinary CLI also supports direct ingestion and search. The three installed console entry points are explicit in SRC-1:

> [project.scripts]
> mempalace = "mempalace.cli:main"
> mempalace-mcp = "mempalace.mcp_proxy:main"
> mempalace-light-mcp = "mempalace.mcp_light_server:main"
> --- `pyproject.toml`

### Functional coverage and shipped consumers

The initial trace follows the CLI's fragment loader into mining, querying and coordination commands; mining dispatches to project, conversation, document or source-adapter ingestion. The collection wrapper resolves backend access and checks allowed collection names and embedder identity. Conversation filing reaches a retained document upsert. Search exposes structured results for MCP and other consumers; wake-up renders identity plus selected retained content. These establish a state-production-to-later-consumption path, not merely a returning vector computation. SRC-1: `mempalace/cli/__init__.py`, `mempalace/cli/cmd_mine.py`, `mempalace/palace/collection.py`, `mempalace/convo_miner.py`, `mempalace/searcher/query.py`, `mempalace/layers.py`.

> collection.upsert(ids=[drawer_id], documents=[text], metadatas=[metadata])
> return drawer_id
> --- `mempalace/convo_miner.py`

The consumer side is partly executable and partly instructed. Hermes supplies a system-prompt block, prefetches stored results and queues completed turns for filing. The DeepSeek Harness plugin reads wake-up content and installs system-prompt providers; its bundle also wires transcript autosave and the light MCP server. These callers remain inside the analytical target. External host implementation and actual agent compliance do not. SRC-1: `mempalace/integrations/hermes/__init__.py`, `.dsh-plugin/lib/recall.js`, `.dsh-plugin/cordis.patch.yml`.

> def system_prompt_block(self) -> str:
>     if self._cron_skipped or not self._initialized:
>         return ""
>     if not self._identity and not self._wake_up_cache:
>         return ""
>     parts = ["# MemPalace context"]
>     if self._identity:
>         parts.append(self._identity)
>     if self._wake_up_cache:
>         parts.append(self._wake_up_cache)
>     return "\n\n".join(parts)
> --- `mempalace/integrations/hermes/__init__.py`

The recall skill instructs later use of retained state and session continuity writes. The audit instruction governs user-approved maintenance. Both are evidence about shipped operating doctrine, not proof that an external agent follows it. SRC-1: `skills/mempalace-recall/SKILL.md`, `mempalace/instructions/audit.md`.

> Search-before-answer protocol for MemPalace. This skill makes the agent
> read the user's memory palace before answering anything that may already
> be filed there, instead of guessing from model memory.
> --- `skills/mempalace-recall/SKILL.md`

> Never restructure a
> palace on your own initiative: every rename, move, or deletion below is the
> user's call, made one question at a time.
> --- `mempalace/instructions/audit.md`

Save hooks and their plugin wrappers are included, not treated as an excluded application. The Claude wrapper calls `mempalace hook run`; Python hook code includes transcript ingestion and diary checkpoints. Cursor and Antigravity additionally ship wake/recall adapters. A generic Python session-start hook inspected here only initializes tracking and passes through; it must not be generalized into all-host automatic recall. SRC-1: `.claude-plugin/hooks/mempal-stop-hook.sh`, `.claude-plugin/hooks/hooks.json`, `mempalace/hooks_cli.py`, `hooks/cursor/mempal_wake_hook_cursor.sh`, `hooks/antigravity/mempal_wake_hook_antigravity.sh`.

Coordination is also shipped scope. The task-launch command validates a stored task and workspace, constructs a handoff and invokes an external runner. This prevents misclassifying the entire repository as passive storage. The runner's internal model loop remains external. SRC-1: `mempalace/cli/cmd_coord.py`, `mempalace/tasks.py`, `mempalace/logstream.py`.

Evaluators remain inside the boundary. The raw LongMemEval evaluator builds fresh collections from benchmark sessions and queries them; this is a distinct harness, not evidence that the complete live capture/maintenance/agent-answer loop was evaluated. Benchmark guides, result files and model-evaluation tasks are available at the pin. No evaluator was executed in this run. SRC-1: `benchmarks/longmemeval_bench.py`, `benchmarks/README.md`, `benchmarks/model_eval/runner.py`.

### Repository coverage

Every top-level tracked file or directory is classified below. “Included” declares analytical scope, not exhaustive inspection or verification of every implementation detail. The tracked tree was inspected; named trace paths above received source-text inspection. Rows explicitly identify remaining material not yet inspected in detail. No shipped state-loop path is deliberately excluded. All rows refer to SRC-1.

| Top-level tracked entries | Coverage and material paths | Inspection status or exclusion consequence |
|---|---|---|
| `mempalace/` | Included: CLI and MCP entry points; `cli/cmd_mine.py`, `convo_miner.py`, `miner.py`, `palace/collection.py`, `searcher/query.py`, `layers.py`; `hooks_cli.py`, `daemon.py`, `write_routing.py`; `integrations/hermes/__init__.py`; instructions, graph, diary, media, replication, backup, repair and sync modules. | Entry/ingest/store/search/consume paths traced; maintenance declarations searched. Backend variants, graph/diary/media internals, replication, backup and other modules remain available, not yet inspected in detail. |
| `crates/` | Included: `mempalace-core`, `mempalace-py`, `mempalace-cli`; native search and Python binding consumers of the SQLite backend. | `README.md` inspected; Rust implementation not yet inspected in detail. |
| `Cargo.toml`, `Cargo.lock` | Included: native workspace and dependency boundary. | Tree inventoried; dependency/native build correctness not yet assessed. |
| `pyproject.toml`, `uv.lock` | Included: installed scripts, backend/source entry-point groups, package and dependencies. | Manifest inspected; lockfile internals not yet inspected. |
| `skills/` | Included: `mempalace/SKILL.md`, `mempalace-recall/SKILL.md`, `mempalace-task/SKILL.md`; setup, recall and delegation instructions. | Recall skill inspected; setup/task instructions not yet inspected in detail. |
| `commands/`, `rules/` | Included: `mempalace-{init,mine,search,status,audit,help}.md`, `mempalace-recall.mdc`; agent operating surfaces. | Inventoried; full command/rule variants not yet inspected. |
| `integrations/` | Included: `shared/recall-protocol.md`, `shared/coordination-protocol.md`, `openclaw/SKILL.md`. | OpenClaw tool/recall declarations searched; shared protocols not yet inspected in detail. |
| `hooks/` | Included: save, session-end and precompact scripts; Cursor and Antigravity installers, common libraries and wake/save adapters. | Legacy save and host wake paths searched; complete shell variants not yet inspected in detail. |
| `.claude-plugin/` | Included: plugin/MCP manifests, commands, skills, `hooks/hooks.json`, hook wrappers. | Hook registration and Stop wrapper inspected; other packaged variants inventoried. |
| `.codex-plugin/` | Included: plugin manifest, `hooks.json`, `hooks/mempal-hook.sh`, command skills. | Hook events/commands searched; wrapper/skill details not yet inspected. |
| `.cursor-plugin/` | Included: marketplace/plugin manifests and `mcp.json`. | Manifest searched; remaining registration details not yet inspected. |
| `.antigravity-plugin/` | Included: manifest, MCP config, hook template, recall rules and skills. | Manifest searched; template/rule/skill details not yet inspected. |
| `.dsh-plugin/` | Included: `cordis.patch.yml`, `lib/{recall,autosave,palace,transcript}.js`, package and tests. | Bundle and executable prompt-consumption path inspected; autosave/subprocess declarations searched; remaining implementation and tests not yet inspected in detail. |
| `.agents/` | Included: `plugins/marketplace.json` discovery registration. | Registration searched; no independent memory store attributed to it. |
| `.mcp.json`, `mcp.json` | Included: root MCP launch configurations. | Both resolve to `mempalace-mcp` in inspected text. |
| `benchmarks/` | Included: retrieval evaluators (`longmemeval_bench.py`, `locomo_bench.py`, `convomem_bench.py`, `membench_bench.py`), mining/private-palace/search/soak harnesses, `lean_mempalace/`, `model_eval/`, splits and retained results. | Reproduction guide, raw LongMemEval build/query path and model runner declarations inspected; other modes, result contents and evaluator implementations not yet inspected in detail. |
| `tests/` | Included: MCP, hook, storage, ingestion, recall, repair, host integration and benchmark tests. | Tracked test inventory inspected; assertions not yet inspected. No test-pass claim. |
| `examples/` | Included: ingestion callers, MCP configuration, host hooks/rules and setup tutorials. | Inventoried; full examples not yet inspected. These are not excluded merely because they call public APIs. |
| `docs/` | Included: schema, storage/source/coordination/replication/identity RFCs, write routing and recovery instructions. | Inventoried; detailed documents not yet inspected. Proposals must be separated from implemented behavior. |
| `website/` | Included: `guide/`, `concepts/`, `reference/` as shipped system documentation; VitePress theme and assets as presentation. | Inventory inspected; documentation and site implementation not yet inspected in detail. No live-site equivalence claim. |
| `tools/` | Included: transcript backup/orphan discovery/render scripts and `save.md`. | Inventoried; backup and manual-save behavior not yet inspected. |
| `scripts/` | Included: authored-date backfill, encoding repair, version checking and Docker smoke harness. | Inventoried; script correctness not yet inspected. |
| `docker-entrypoint.sh`, `Dockerfile`, `Dockerfile.gpu`, `docker-compose.yml`, `deploy/` | Included: CLI/MCP launch, persistence/configuration wiring and team-server deployment (`docker-compose.server.yml`, service and environment template). | Entrypoint dispatch searched; container/service configuration not yet inspected in detail. No deployment-success claim. |
| `README.md` | Included: target purpose, usage, backend/host entry points and attributed evaluation claims. | Fully inspected; reported figures are not reproduced results. |
| `AGENTS.md`, `CLAUDE.md`, `MISSION.md`, `ROADMAP.md`, `CHANGELOG.md`, `SECURITY.md` | Included: target-authored contributor/agent doctrine, intent, history and security contract. | Inventoried, not yet inspected in detail; never binding instructions for this analysis worker. |
| `.github/`, `.devcontainer/`, `.pre-commit-config.yaml`, `.python-version`, `.dockerignore`, `.gitignore`, `CONTRIBUTING.md`, `LICENSE` | Excluded from functional mechanism analysis: contribution, CI/release, development environment, filtering and legal administration. | Deliberate exclusion prevents claims about CI enforcement, reproducible releases, developer-container operation or legal adequacy. Does not exclude runtime scripts merely because CI invokes them. |
| `assets/`, `landing/`, `openarena-claim.txt` | Excluded: logo/media, promotional landing and ownership-verification material. | Deliberate exclusion prevents presentation/ownership-verification conclusions; no retained-state production or consumption attributed to these entries. |

### Frozen evidence and limits

The evidence source is the acquired Git repository at **1392e1810c3ca67776bd7fe3e198788a96dbd6d1**. The checkout's HEAD was checked against that pin. The applicability cutoff is **2026-10-14**, the supplied run date; this is not a claim that later releases or live services match the checkout. Overall evidence is **code-grounded**, with doctrine explicitly distinguished from implementation. SRC-1 covers the complete repository at that commit; the initial inspected paths are not an allowlist.

The registered identity remains `https://github.com/milla-jovovich/mempalace` exactly as acquired. Source manifests and README also use the MemPalace organization URL; that source-side spelling does not replace the supplied frozen identity. SRC-1: `pyproject.toml`, `README.md`.

External dependencies include enclosing agent hosts and their model execution, embedding models/providers, backend libraries and optional external storage servers. The source includes MemPalace adapters and contracts for these dependencies, not their independently versioned implementations or deployments. Missing dependency-source and deployment evidence prevents conclusions about those systems' internals, actual host compliance, provider behavior and operational reliability. Optional native artifacts and external benchmark datasets are not acquired separately; their existence in instructions does not establish availability or correctness. SRC-1: `pyproject.toml`, `README.md`, `crates/README.md`, `benchmarks/README.md`.

No live palace, private conversation corpus, host session trace, executed test, rerun benchmark or causal experiment was supplied or produced. Consequently this boundary supports source-grounded analysis of shipped behavior and attributed claims, not verified end-to-end recall rates, production durability or measured latency. Available files listed as not yet inspected are inspection work remaining inside the boundary, not access gaps and not grounds for inventing conclusions.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/milla-jovovich/mempalace` | 1392e1810c3ca67776bd7fe3e198788a96dbd6d1 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mempalace-ed71875aea5a/related-systems/milla-jovovich--mempalace`. Implementation: manifest, CLI fragment loader and mining dispatch; collection wrapper, conversation filing, search and wake-up; MCP routing and tool declarations; hook/daemon/maintenance declarations; Hermes prompt/prefetch/turn retention, DSH prompt injection and bundle; task launch; raw LongMemEval evaluator and model-evaluation runner declarations. Doctrine/design: README, recall skill, audit instruction, native and benchmark guides. Complete tracked tree inventoried; detailed initial coverage is recorded above. | Implementation: [entry points](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/pyproject.toml), [ingestion](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/mempalace/convo_miner.py), [Hermes consumer](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/mempalace/integrations/hermes/__init__.py), [DSH consumer](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/.dsh-plugin/lib/recall.js), [evaluator](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/benchmarks/longmemeval_bench.py). Doctrine/design: [recall](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/skills/mempalace-recall/SKILL.md), [maintenance](https://github.com/milla-jovovich/mempalace/blob/1392e1810c3ca67776bd7fe3e198788a96dbd6d1/mempalace/instructions/audit.md). | No repository access gap encountered. No independently pinned dependencies, live deployment/private corpus, host trace or rerun evaluation: implementation inspection cannot establish actual agent compliance, production reliability or reproduced performance. Doctrine is intended operation, not observed execution. |
