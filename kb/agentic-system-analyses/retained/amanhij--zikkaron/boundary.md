---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Zikkaron's shipped memory engine, MCP service, host hooks, instructions and evaluators at commit dda34a5d903d04ecb5517af214d437873c833302."
run-id: AAS-2026-10-15-zikkaron-0102ec63c6e5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: dda34a5d903d04ecb5517af214d437873c833302
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/amanhij/zikkaron
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/zikkaron-0102ec63c6e5/related-systems/amanhij--zikkaron
  revision: dda34a5d903d04ecb5517af214d437873c833302
  sha256: null
---

# Zikkaron boundary

## Boundary and evidence

Zikkaron is in scope as a memory/knowledge/context-engineering system serving an external model-driven host. Its intended use is persistent project and working context for Claude Code. The executable entry is `zikkaron = "zikkaron.__main__:cli"`; the CLI starts the MCP service or dispatches drain, restore, capture, context, seed and statistics operations (SRC-1, `pyproject.toml`, `zikkaron/__main__.py`). This is a whole-system boundary, not just the storage or retrieval library: the shipped callers, instruction installation, direct database hooks and evaluation drivers belong to the target.

The scope follows the state loop. Explicit `remember` calls pass a write gate and then curation or direct insertion; project seeding and automatic action summaries are additional production paths. The service initializes storage, embeddings, retrieval, consolidation, replay and related engines. Background consolidation processes episodes and the action log and maintains retained state. MCP recall, project context, session-start context, per-prompt recall and post-compaction restoration consume retained content (SRC-1, `zikkaron/server.py`, `zikkaron/seed.py`, `zikkaron/consolidation.py`, `zikkaron/hooks/session-start-context.py`, `zikkaron/hooks/prompt-recall.py`, `zikkaron/__main__.py`). These are boundary responsibilities; detailed correctness and effectiveness remain for later analysis.

The admission path is executable, not merely a README promise:

> # Predictive coding write gate — FIRST check before any storage
> gate_result = None
> if _write_gate is not None:
>     should_store, surprisal, reason = _write_gate.should_store(
>         content, context, tags
>     )
> --- `zikkaron/server.py`

The model-dependent part includes local embedding inference, rather than requiring an enclosing conversational generation loop. The embedding wrapper calls the loaded model and converts its output to a normalized stored vector (SRC-1, `zikkaron/embeddings.py`):

> vec = self._model.encode(text)
> arr = self._normalize(np.asarray(vec, dtype=np.float32))
> result = arr.tobytes()
> --- `zikkaron/embeddings.py`

The host integration is material to consumption. Startup calls instruction synchronization and hook installation; the hook installer configures PreCompact, SessionStart, PostToolUse and UserPromptSubmit events. Per-prompt recall performs its own database retrieval and outputs context, rather than calling the server's `recall` function (SRC-1, `zikkaron/server.py`, `zikkaron/hooks/prompt-recall.py`). Its consumption contract is explicit:

> # Plain text stdout is auto-injected as context by Claude Code
> # This is simpler and more reliable than JSON hookSpecificOutput
> print(context)
> --- `zikkaron/hooks/prompt-recall.py`

The frozen evidence is the acquired Git checkout at full commit `dda34a5d903d04ecb5517af214d437873c833302`; HEAD matched that pin and the checkout reported no tracked modifications. The applicability cutoff is 2026-10-15, the supplied run date, not a claim to have inspected later upstream releases. The overall tier is code-grounded: executable paths and their shipped consumers were traced statically. No target code, tests, examples, model calls or services were executed.

### Repository coverage

All top-level tracked entries are classified below. Included means within the functional evidence boundary, not that every line has already been inspected. Initial inspection traced entry points and material lifecycle callers; module inventories identify additional in-boundary implementation for later jobs. No material shipped lifecycle path was unavailable or deliberately excluded.

| Top-level entry | Status | Material paths and role | Inspection and conclusion limits |
|---|---|---|---|
| `.github/` | Included | `.github/workflows/test.yml` runs the package tests; `.github/workflows/publish.yml` gates publishing on those tests. | Both workflows inspected. They establish configured CI/release behavior, not a successful CI run or published package equivalence. |
| `.gitignore` | Included | Excludes local databases, host configuration, benchmark datasets and result artifacts from tracking. | Inspected. Exclusion patterns are not evidence that any particular experiment ran. |
| `LICENSE` | Excluded | Legal licensing text, not a state producer, maintainer or consumer. | Deliberate functional exclusion; no licensing or redistribution conclusion is made. |
| `README.md` | Included | Setup instructions, intended host use, architecture descriptions and reported benchmark results. | Setup and usage passages inspected; benchmark claims remain attributed reports, not observed runs. Remaining documentation is in scope but not yet fully inspected. |
| `benchmarks/` | Included | `test_e_locomo.py` contains ingestion/settings/evaluation helpers; `run_benchmark_gpu.py` ingests and retrieves; `run_locomo_ablation.py` orchestrates configurations and comparisons; `run_locomo_jscore.py` retrieves, generates and judges answers; `run_longmemeval.py` supplies another ingestion/retrieval/QA driver; `od_diagnostic.py` inspects retrieval ranking; `__init__.py` is an empty package marker. | Tree and driver/helper entry points inspected, with ingestion, retrieval-to-generation and ablation dispatch passages read. Evaluators are shipped consumers, not excluded external applications. Dataset contents, generated results and provider responses are not frozen here; benchmark reproduction and measured performance cannot be established from these scripts alone. |
| `pyproject.toml` | Included | Package metadata, wheel inclusion of `zikkaron`, runtime dependencies, console entry point and test discovery. | Fully inspected; metadata does not prove installation behavior on a particular host. |
| `requirements.txt` | Included | Alternate dependency installation list used by CI. | Fully inspected; dependency implementations and exact resolved versions are outside this source pin. |
| `server.json` | Included | MCP registry/package declaration and stdio transport declaration. | Fully inspected; it is a declaration, not evidence of registry deployment or equivalence to the checkout. |
| `zikkaron/` | Included | `__main__.py` supplies server/CLI dispatch and direct database commands; `server.py` supplies tools, resources, HTTP hook routes, engine wiring, hook installation and the canonical host instruction string. `hooks/post-tool-capture.py` persists tool actions; `hooks/session-start-context.py` reloads context; `hooks/prompt-recall.py` retrieves on user turns; `hooks/pre-compact-drain.sh` and `hooks/post-compact-rehydrate.sh` call the drain/restore CLI. | Dispatch, lifecycle wiring, instruction/hook installation, direct capture/context and all five hook responsibilities inspected. Host invocation and actual injection are not observed. |
| `zikkaron/` (state implementation) | Included | `storage.py`, `models.py`, `config.py`, `embeddings.py` define persistence, records, settings and embedding inference. `sensory_buffer.py`, `predictive_coding.py`, `curation.py`, `seed.py`, `enrichment.py`, `profiles.py` produce/admit content. `consolidation.py`, `astrocyte_pool.py`, `cls_store.py`, `compression.py`, `sleep_compute.py`, `thermodynamics.py`, `staleness.py`, `reconsolidation.py`, `crdt_sync.py` maintain state. `retrieval.py`, `knowledge_graph.py`, `fractal.py`, `hdc_encoder.py`, `hopfield.py`, `engram.py`, `cognitive_map.py`, `rules_engine.py`, `metacognition.py`, `prospective.py`, `narrative.py`, `restoration.py` support organization, retrieval, contextual surfacing and replay. `__init__.py` supplies package initialization/version identity. | Inventory and server/CLI consumers inspected; insertion, embedding inference, seeding, consolidation/action-log processing, service recall and replay reconstruction received direct passage inspection. Internal algorithms not yet traced in full remain in scope, not access gaps. No claim of comprehensive algorithm verification is made. |
| `zikkaron/` (tests) | Included | `tests/` supplies unit, integration, transport and schema specifications, including `test_frontier_integration.py`, `test_integration.py`, `test_server.py`, `test_restoration.py`, `test_retrieval.py`, `test_storage.py` and subsystem tests. | Inventory and test declarations searched; restoration assertions inspected directly. Tests are specification evidence unless an execution trace is supplied; none was supplied or generated. |

### External dependencies and excluded responsibilities

Claude Code owns conversation execution, tool selection, event delivery and the interpretation of hook stdout. Its implementation and actual sessions are not in this checkout. The target ships hooks and usage instructions, so those are included; host compliance and end-to-end task improvement cannot be concluded from them (SRC-1, `README.md`, `zikkaron/server.py`, `zikkaron/hooks/prompt-recall.py`).

The dependency packages, downloadable embedding/model weights, external project files scanned by seeding, benchmark datasets and model-provider services are outside the frozen repository. Dependency declarations and loading/calling code are included; their external implementations, exact model artifacts and live responses are not. This prevents claims about resolved dependency behavior, deployment reliability, reproduced benchmark scores and causal performance gains. The embedding loader may load cached or online SentenceTransformer models; the QA driver also calls generation and judging functions after retrieval (SRC-1, `pyproject.toml`, `requirements.txt`, `zikkaron/embeddings.py`, `zikkaron/seed.py`, `benchmarks/run_locomo_jscore.py`). These are evidence limits, not reasons to drop the shipped drivers from the boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/amanhij/zikkaron` | dda34a5d903d04ecb5517af214d437873c833302 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/zikkaron-0102ec63c6e5/related-systems/amanhij--zikkaron`. Implementation: tracked tree, package/CLI dispatch, service wiring, memory admission/insertion/recall, consolidation and action-log processing, embedding loading/inference, seed persistence, replay reconstruction, all hook responsibilities, benchmark entry points and selected driver/helper paths, CI workflows and selected test assertions. Doctrine/design: README setup and usage, canonical instruction string and hook contracts. Reported operation: README's claims are available for attribution, not accepted measurements. | Implementation: [CLI](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/__main__.py), [service and instructions](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [maintenance](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py), [prompt consumer](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py), [evaluator](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/benchmarks/run_locomo_jscore.py). Doctrine/design and reported operation: [README](https://github.com/amanhij/zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/README.md); doctrine/design also `zikkaron/server.py`. Other initially inspected paths are identified in the coverage table and prose above. | No source-access gap within the tracked repository was encountered. No observed-run or causal-experiment layer was supplied. External host, dependencies, model weights, datasets and generated evaluation artifacts are not frozen; actual operation, reproduced scores and causal benefit remain unestablished. Uninspected in-scope code is not an access gap. |
