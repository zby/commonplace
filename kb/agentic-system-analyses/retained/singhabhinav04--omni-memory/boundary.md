---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Omni-Memory's shipped memory lifecycle and host integrations at Git revision 20f9f9ffd7ece0c6514542677ba6a549841f5536."
run-id: AAS-2026-11-08-omni-memory-09378abbfe6b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/singhabhinav04/omni-memory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/omni-memory-27d76f8b7250/related-systems/singhabhinav04--omni-memory
  revision: 20f9f9ffd7ece0c6514542677ba6a549841f5536
  sha256: null
---

# Omni-Memory boundary

## Boundary and evidence

Omni-Memory is in scope as a memory/knowledge/context-engineering system for coding agents. This run covers its shipped memory lifecycle, not an enclosing coding-agent runtime. Its intended use is to retain project knowledge across sessions, retrieve it into subsequent agent context, and mark changes in the code that retained knowledge cites. The whole-system boundary includes the package, CLI, plugin wiring, extraction and usage instructions, dashboard driver, exports, sharing and maintenance paths. It does not mean that every implementation line has already been reviewed or that the system has been executed. [SRC-1: `README.md`, `ARCHITECTURE.md`, `omni_memory/cli.py`]

The package's own declared scope is:

> Persistent, branch-aware, git-anchored memory & context layer for coding agents.
> --- `pyproject.toml`

The installed command is a shipped driver, not an excluded application:

> [project.scripts]
> omni-memory = "omni_memory.cli:main"
> --- `pyproject.toml`

`bin/omni-memory` and `omni_memory/__main__.py` also route into that CLI. The plugin manifest selects the packaged skill and hook configuration. `hooks/hooks.json` routes SessionStart, UserPromptSubmit, PreCompact, SessionEnd and PostToolUse into the CLI's hook dispatcher. These paths belong to the target because they produce, refresh and deliver its retained state. [SRC-1: `bin/omni-memory`, `omni_memory/__main__.py`, `.claude-plugin/plugin.json`, `hooks/hooks.json`, `omni_memory/cli.py`]

### Included functional loop

- **Produce and admit:** `build` gathers repository context, optionally invokes the model adapter and admits structured facts; `capture` accepts agent-authored JSON or extracts from transcript text. Extraction prompts and the packaged skill are part of this boundary, including their instructions for agent-driven capture. `session_memory.py` sends candidates through cleanup and source-sensitive evidence handling into the store. [SRC-1: `omni_memory/cli.py`, `omni_memory/context.py`, `omni_memory/llm.py`, `omni_memory/session_memory.py`, `omni_memory/cleanup.py`, `omni_memory/skills/omni-memory/SKILL.md`]
- **Persist and maintain:** SQLite holds memory and related state. Session hooks reopen the store; branch refresh and the dashboard watcher maintain topology, graph and staleness. The boundary also includes merge reconciliation, use feedback, read-observation binding, point-of-use checking, quarantine, explicit purge and restoration. [SRC-1: `omni_memory/store.py`, `omni_memory/cli.py`, `omni_memory/branch.py`, `omni_memory/serve.py`, `omni_memory/staleness.py`, `omni_memory/eviction.py`, `omni_memory/witness.py`]
- **Reload and consume:** session start refreshes state, updates root AGENTS.md and, unless manual mode is selected, prints a memory seed. On-demand injection ranks retained content and emits the prompt block; auto mode additionally uses the prompt hook. The digest and managed AGENTS.md block are persistent consumption surfaces, not merely documentation. [SRC-1: `omni_memory/cli.py`, `omni_memory/inject.py`, `omni_memory/agentsmd.py`, `omni_memory/digest.py`]
- **Other shipped drivers:** the local dashboard is a reader, editor and refresh driver over the same store. Team shards and snapshots provide export/import paths. OpenCode's generated plugin refreshes on session creation and idle, and pushes an injection block into compaction context. Other named IDE integrations use the generated AGENTS.md surface. These callers are included; they must not be discarded as external merely because they invoke the CLI. [SRC-1: `omni_memory/serve.py`, `omni_memory/team.py`, `omni_memory/cli.py`, `omni_memory/install.py`]

The portable instruction surface explicitly requires later consumption and feedback:

> 2. **During:** if you learn a durable decision/flow/gotcha, run
>    `omni-memory remember "<one sentence>" --kind <kind>`.
> 3. **End of task:** extract memory from what happened and pipe JSON to
>    `omni-memory capture` (array of `{kind,text,files,symbols}`). The SessionEnd
>    hook does this automatically once installed.
> --- `omni_memory/skills/omni-memory/SKILL.md`

This is doctrine, not evidence that an agent obeyed it. The host supplies event delivery, transcript production, tool use and final model behavior. Omni-Memory supplies the hook commands, extraction prompts, storage and returned context. A deterministic fallback also exists; model calls are not required for every capture. The inspected implementation distinguishes already-JSON ingestion, permitted autonomous model extraction and heuristic fallback. [SRC-1: `omni_memory/session_memory.py`, `omni_memory/llm.py`, `omni_memory/cli.py`]

### Repository coverage

All top-level tracked entries at the acquired commit are accounted for below. “Included” sets functional/evidence scope; inspection depth is stated separately. Available but not yet deeply inspected material remains available to later analysts under SRC-1. No material shipped lifecycle path is deliberately excluded.

| Top-level tracked entry | Status and material paths | Role and initial inspection; limit or conclusion prevented |
|---|---|---|
| `.claude-plugin/` | Included: `plugin.json`, `marketplace.json` | Both inspected; distribution metadata links the skill, hooks and repository. Not proof of successful marketplace installation. |
| `.github/` | Included: `workflows/ci.yml`, `workflows/publish.yml` | Both inspected; test matrix and packaging/publishing definitions. No workflow logs were supplied, so no CI or release-success conclusion. |
| `.gitignore` | Included | Inspected; excludes local runtime state, credentials and generated artifacts from tracking. Does not establish runtime secret safety. |
| `AGENTS.md` | Included | Inspected shipped managed context and memory snapshot. Evidence of a shipped consumption artifact, not validation of its embedded facts or a supplied execution trace. |
| `ARCHITECTURE.md` | Included | Inspected module map and declared data flows. Doctrine/design; implementation takes precedence where these descriptions differ. |
| `LICENSE` | Included | Inspected proprietary/source-available terms; no license-compliance assessment. |
| `MANIFEST.in` | Included | Inspected package-data inclusions for docs, static assets and skills. |
| `PLAN.md` | Included | Inspected as roadmap/design only. Planned MCP, runtime-flow and UI descriptions cannot establish shipped implementations. |
| `README.md` | Included | Inspected usage, intended loop and advertised measurements. Example outputs and performance claims are attributed reports, not observed operation. |
| `bin/` | Included: `omni-memory` | Inspected shell shim routing into the package. |
| `hooks/` | Included: `hooks.json` | Inspected event-to-command wiring; host event semantics and actual delivery remain external. |
| `omni_memory/` — interfaces and instructions | Included: `__init__.py`, `__main__.py`, `cli.py`, `install.py`, `skills/omni-memory/SKILL.md` | Module entry, key CLI lifecycle ranges, generated OpenCode plugin, IDE dispatch and full skill inspected. Not a full CLI-option audit. |
| `omni_memory/` — memory production and retention | Included: `session_memory.py`, `cleanup.py`, `store.py`, `context.py`, `llm.py`, `artifacts.py`, `team.py` | Capture prompts/admission, store constructor and method surface, model adapter, artifact prompts and sharing surface inspected; build and import/export callers traced in CLI. Full schema, filtering, context selection and import validation remain for detailed analysis. |
| `omni_memory/` — maintenance and retrieval | Included: `branch.py`, `gitmeta.py`, `staleness.py`, `eviction.py`, `rank.py`, `inject.py`, `digest.py`, `agentsmd.py`, `collector.py`, `witness.py`, `identifier.py`, `savings.py` | Refresh orchestration, injection selection/rendering, managed-context writer, digest renderer and maintenance/evaluation surfaces inspected directly or through callers and module map. Ranker, git adapter, witness and identifier internals are not yet deeply inspected; no algorithm-correctness claim is made here. |
| `omni_memory/` — graphs and projections | Included: `graph/__init__.py`, `graph/build.py`, `graph/extract.py`, `graph/affected.py`, `graph/proximity.py`, `graphbuild.py`, `healthmap.py`, `systemmap.py` | Code-graph build/persistence entry inspected; consumers traced through build, refresh and inject. Remaining graph extraction, propagation and projection internals not yet deeply inspected; language coverage and map fidelity are not established by this boundary. |
| `omni_memory/` — dashboard | Included: `serve.py`, `static/index.html`, `static/vendor/` including `VERSIONS.txt`, `d3.min.js`, `marked.min.js`, `mermaid.min.js` | Server origin-check surface, document synchronization, watcher and launch inspected; vendored-version declaration read. Browser UI and minified dependency internals remain uninspected; this prevents rendering, sanitization and dependency-security conclusions, not inclusion of the dashboard's state-changing driver. |
| `pyproject.toml` | Included | Inspected entry point, package data, dependency declarations and test configuration. |
| `setup.py` | Included | Inspected setuptools shim. |
| `tests/` | Included: `conftest.py` and all tracked `test_*.py` | Tree inventoried; initial source sampling of `test_conformance_temporal.py` and `test_extraction_quality.py` establishes assertion-based provenance/admission checks. Other test bodies remain uninspected. Test definitions are implementation evidence, not test-run results or a model-quality benchmark. |

### Frozen evidence, dependencies and limits

The sole source is the acquired Git repository at full revision `20f9f9ffd7ece0c6514542677ba6a549841f5536`; the checkout HEAD was checked against that pin. The applicability cutoff is **2026-11-08**, the supplied run date. The evidence tier is **code-grounded**: source paths and driver connections support the boundary. No target commands, tests, examples, hooks or model services were executed.

External dependencies are Python/SQLite, the Git executable and consumer repository, host IDE/runtime facilities, browser behavior, and optional model services or an agent CLI. Package metadata declares tree-sitter dependencies for Python 3.10 and later and optional graph/serve extras. Those dependencies' implementations and service behavior are outside the source boundary. This prevents conclusions about external parser accuracy, provider guarantees, actual host compliance, end-to-end agent outcomes or installed-package equivalence. Model-adapter code is inside the boundary; remote provider operation is not. [SRC-1: `pyproject.toml`, `omni_memory/llm.py`, `omni_memory/install.py`, `omni_memory/serve.py`]

No required repository source was inaccessible during boundary selection. Local databases, genuine host transcripts, shared-memory deployments, benchmark runs and CI outputs were not supplied as frozen evidence. Their absence prevents observed-run and causal-effectiveness claims. Savings examples do not establish measured task savings; shipped tests do not establish passing execution; “verified” prompt wording does not establish truth of memory content. These are evidence limits, not reasons to narrow away shipped maintenance or consumption paths. [SRC-1: `README.md`, `omni_memory/savings.py`, `omni_memory/agentsmd.py`, `.github/workflows/ci.yml`]

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/singhabhinav04/omni-memory` | 20f9f9ffd7ece0c6514542677ba6a549841f5536 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/omni-memory-27d76f8b7250/related-systems/singhabhinav04--omni-memory`. Implementation: tracked tree, package/CLI entry points, plugin/hooks, capture/admission and model paths, store construction/method surface, refresh and consumption callers, dashboard maintenance, sharing, test samples. Doctrine/design: README, architecture, plan, packaged skill, generated AGENTS.md, artifact/extraction prompts, packaging and workflows. Reported operation: README examples/quality and savings claims; not an execution trace. Detailed coverage and unread internals are identified above. | Implementation: [CLI](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/omni_memory/cli.py), [capture](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/omni_memory/session_memory.py), [host wiring](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/omni_memory/install.py), [dashboard driver](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/omni_memory/serve.py). Doctrine/design: [skill](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/omni_memory/skills/omni-memory/SKILL.md), [architecture](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/ARCHITECTURE.md). Reported operation: [README](https://github.com/singhabhinav04/omni-memory/blob/20f9f9ffd7ece0c6514542677ba6a549841f5536/README.md). | No repository access gap identified. External host/provider implementations and actual runtime state are not captured. No observed-run or causal-experiment layer is registered; behavior in deployment, agent compliance, test success and task-level effectiveness remain unestablished. |
