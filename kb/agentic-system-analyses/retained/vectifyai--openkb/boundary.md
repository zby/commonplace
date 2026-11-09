---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenKB's shipped knowledge compilation, maintenance and consumption system at commit ff54396e575ee6feb0113b631a34caa082b441cc."
run-id: AAS-2026-11-09-openkb-bd9c4c38a842-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "ff54396e575ee6feb0113b631a34caa082b441cc"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/vectifyai/openkb
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/openkb-a5bff2e57102/related-systems/vectifyai--openkb
  revision: ff54396e575ee6feb0113b631a34caa082b441cc
  sha256: null
---

# OpenKB boundary

## Boundary and evidence

OpenKB qualifies as a memory/knowledge/context-engineering system: it uses model calls to compile documents into persistent wiki pages and supplies shipped paths that maintain and later consume those pages. The target is the shipped OpenKB application, not just its query library or its external-agent skill. The intended use is document ingestion, cross-document knowledge compilation, retrieval and generation from the retained wiki. SRC-1, `README.md`, `openkb/cli.py`, `openkb/agent/compiler.py`, `openkb/agent/query.py`.

> **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents.
> --- `README.md`

The boundary is **whole-system** at the frozen repository revision: ingestion and admission, retained content and registry state, schema and prompts, maintenance and removal, query and resumed chat, generated skills and decks, graph rendering, REST service, browser client and shipped external-agent instructions. CLI and REST drivers belong to the target; they own persistence, configuration and invocation rather than merely illustrating an excluded host. The initial inspection traced these functional paths; it is not a line-by-line implementation audit or a claim that each test or asset was read.

### Functional paths established

- **Production and admission:** the CLI add path converts input, selects short-document compilation or PageIndex indexing plus long-document compilation, publishes staged artifacts and records the hash after compilation. `add_coordinator.py`, `mutation.py`, `locks.py` and `state.py` are included supporting state-management paths. The REST upload route and managed watcher also reach the add pipeline. SRC-1, `openkb/cli.py`, `openkb/converter.py`, `openkb/indexer.py`, `openkb/api.py`, `openkb/watch_service.py`.
- **Retained knowledge and instructions:** source Markdown or per-page JSON, summaries, concepts, entities, index, log, saved explorations and reports are within scope, as are the code that writes them and the schema loaded into prompts. Compilation reads source text and the current wiki schema; query and lint load that schema too. SRC-1, `openkb/schema.py`, `openkb/agent/compiler.py`, `openkb/agent/query.py`, `openkb/agent/linter.py`.
- **Maintenance:** remove edits source-associated wiki pages, index and registry; recompile reloads registered documents and invokes compilation; structural and model-based lint examine retained content. CLI watch and server-managed watch initiate ingestion from raw-file events. These are part of the system's continuing loop, not external maintenance assumed to happen elsewhere. SRC-1, `openkb/cli.py`, `openkb/agent/linter.py`, `openkb/watch_service.py`.
- **Later consumption and session persistence:** query exposes wiki reads, page-range reads and images to an SDK agent. CLI chat can resume saved sessions. The REST chat path combines retained history with a new message and persists the final turn. The browser client loads persisted text and traces for display, and sends session IDs on subsequent chat calls. SRC-1, `openkb/agent/query.py`, `openkb/agent/chat.py`, `openkb/agent/chat_session.py`, `openkb/cli.py`, `openkb/api.py`, `frontend/src/api/chat.ts`, `frontend/src/pages/ChatSession.tsx`.
- **Derived artifacts and evaluation:** Skill Factory reads the wiki and writes portable skill directories; deck generation runs a selected skill with optional critic pass. Include the skill-generation prompt, bundled producer/critic instructions, skill validators, trigger/body evaluation, version snapshots and marketplace publication helpers. Graph generation is another retained-wiki consumer. Evaluation implementation and mocked tests are evidence of an evaluation design, not proof of model quality. SRC-1, `openkb/skill/creator.py`, `openkb/prompts/skill_create.md`, `openkb/skill/generator.py`, `openkb/skill/evaluator.py`, `tests/test_skill_evaluator.py`, `openkb/deck/creator.py`, `openkb/agent/skill_runner.py`, `openkb/visualize.py`.
- **External-agent consumption:** the bundled OpenKB skill instructs an enclosing agent to discover a KB, inspect its index and read retained pages directly. Its marketplace manifest points to that skill. Include those instructions, but do not attribute the enclosing agent's execution, context selection or compliance to OpenKB. SRC-1, `skills/openkb/SKILL.md`, `.claude-plugin/marketplace.json`.

The schema explicitly establishes saved outputs as part of retained knowledge:

> - explorations/ — Saved query results, analyses, and comparisons worth keeping.
> - reports/ — Lint health check reports. Auto-generated.
> --- `openkb/schema.py`

The resumed-chat path consumes previously retained history:

> new_input = session.history + [{"role": "user", "content": user_input}]
> --- `openkb/agent/chat.py:926-942`

### Top-level coverage

Every tracked top-level entry is classified below. “Included” fixes the functional evidence boundary, not uniform depth of inspection. Material paths were traced at entry-point and consumer level above. Supporting internals and fixtures not yet inspected remain available at this same pin; that is not an access gap.

| Top-level entry | Classification and role | Initial inspection and limits / conclusion prevented |
| --- | --- | --- |
| `.claude-plugin/` | Included: `marketplace.json` distributes `skills/openkb`. | Manifest inspected; no installation or host-agent execution observed. |
| `.env.example` | Included: credentials and REST configuration contract. | Inspected as configuration doctrine, not operational credentials. |
| `.github/` | Included: `workflows/ci.yml` and `workflows/publish.yml` define tests, browser build and release packaging. | Both inspected; workflow text does not establish a successful CI or release run. |
| `.gitignore` | Excluded from mechanism analysis: repository hygiene. | Tree inventory only; no conclusion about completeness of untracked local data. |
| `AGENTS.md` | Included: developer module map and declared invariants. | Inspected as doctrine, not proof that every writer obeys it. |
| `CLAUDE.md` | Excluded as a separate evidence contribution: coding-agent entry document. | Inventory only; no additional coding-agent instruction claims based on it. Runtime wiki instructions are separately included through `openkb/schema.py`. |
| `LICENSE` | Excluded: legal terms. | No legal-compliance assessment. |
| `README.md` | Included: intended use, command surface and integration contracts. | Inspected; advertised benefits are not measured results. |
| `assets/` | Excluded: `openkb-architecture.webp` presentation image. | Not inspected; no inference depends on diagram-only content. Executable paths determine the boundary. |
| `config.yaml.example` | Included: model, language, concurrency, entity types and provider settings. | Inspected as configuration doctrine. |
| `docs/` | Included: tracked `golden-principles.md`; `.gitignore` is housekeeping. | Principles inspected. Referenced maintainer-local `docs/internal/` is unavailable at this pin; prevents reconstructing private design history, not the shipped loop. |
| `examples/` | Included: configuration, commands/sample-wiki, chat, PageIndex cloud, REST API, skills, slides, visualization and document inputs. | Landing inspected to locate shipped walkthroughs and retained examples. Individual walkthroughs, sample pages, PDFs and HTML outputs are not yet inspected; no reproducibility or output-quality conclusion follows from their presence. |
| `frontend/` | Included: browser application; `src/pages/ChatSession.tsx`, `src/api/chat.ts`, other `src/api/` wrappers and KB/configuration pages consume and initiate backend operations. Build metadata, localization and UI components support it. | Chat restore and request paths inspected; other presentation details and individual components are not yet audited. No browser execution or accessibility claim. |
| `openkb/` | Included: `cli.py`, `__main__.py`, `api.py` and `api_*` service/router helpers; ingestion via converter, URL, images and indexer; add coordination, mutations, locks, registry/state, config/admin/documents/page operations; `schema.py`, frontmatter/log; `agent/` compiler/query/chat/tools/linter/skills; `skill/`, `deck/`, `prompts/`; watcher/services, visualization/tree rendering and templates. | Material production, maintenance, persistence and consumption paths traced above. Helper internals not individually read remain included for later inspection; no complete correctness or security audit is claimed. |
| `pyproject.toml` | Included: package entry points, dependencies and bundled skill/browser packaging. | Inspected. `openkb`, `openkb-web` and alias `openkb-api` establish shipped drivers; built distribution bytes were not supplied. |
| `skills/` | Included: `openkb/SKILL.md` and references for external-agent consumption; `openkb-deck-neon`, `openkb-deck-editorial`, `openkb-html-critic` instructions for generated artifacts and maintenance. | OpenKB skill read; deck/critic frontmatter and initial instructions inspected and traced to runner. Full styling instructions and OpenKB reference files not yet inspected. No host compliance or visual-quality conclusion. |
| `tests/` | Included: compiler, state/mutation/locks, tools, query/chat/session, lint, skill evaluation/validation, deck, watcher, API and CLI test surfaces. | Tree inventoried and evaluator test setup inspected. Tests were not run; remaining assertions are not yet inspected. No test-pass claim. |
| `uv.lock` | Included: frozen dependency resolution metadata. | Inventoried, not read package by package. No dependency integrity or vulnerability assessment. |

### Frozen evidence and external limits

The source is the acquired Git object unchanged, at full commit `ff54396e575ee6feb0113b631a34caa082b441cc`, with applicability cutoff **2026-11-09**. HEAD was checked against the supplied revision and the checkout reported no local changes. The absolute checkout path is only an access root. No other repository, live documentation, package installation or revision is admitted as evidence.

The overall evidence tier is **code-grounded**: inspected implementation supports source-level behavior and inspected prompts/documentation support declared intent. No target commands, tests, examples, model calls or services were executed. No observed-run or causal-experiment evidence is established by this boundary.

External dependencies include PageIndex (local library and optional hosted service), document conversion/extraction libraries, LiteLLM and model providers, OpenAI Agents SDK, filesystem/locking facilities, FastAPI and the browser platform. Their OpenKB call sites and declared dependencies are included; their independent implementations and operational services are not frozen here. This prevents conclusions about provider internals, actual retrieval/model accuracy, hosted data handling, dependency-level failure guarantees or end-to-end runtime performance. SRC-1, `pyproject.toml`, `openkb/indexer.py`, `openkb/converter.py`, `openkb/agent/query.py`, `openkb/api.py`.

Obsidian and external agent runtimes are excluded hosts. The shipped integration instructions are included, but successful installation, navigation and enforcement by those hosts are not established. Release-built browser assets are not tracked in this checkout; frontend source and release build instructions are available instead, so behavior of a particular published wheel cannot be verified. SRC-1, `skills/openkb/SKILL.md`, `README.md`, `pyproject.toml`, `.github/workflows/publish.yml`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/vectifyai/openkb` | ff54396e575ee6feb0113b631a34caa082b441cc | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/openkb-a5bff2e57102/related-systems/vectifyai--openkb`. Implementation: tracked tree and package scripts; add/remove/recompile/query/watch/lint and chat-resume wiring in `openkb/cli.py`; compiler short/long entry paths, converter/indexer interfaces, query tools, chat persistence/reload and REST/browser consumers; mutation helpers; skill creator/runner/generator/evaluator, deck creator, graph consumer and mocked evaluator test setup. Doctrine/design: `README.md`, `AGENTS.md`, `docs/golden-principles.md`, `openkb/schema.py`, query/linter prompts, `openkb/prompts/skill_create.md` opening, OpenKB skill, bundled deck/critic openings, example landing, config samples, marketplace and CI/release manifests. Detailed coverage and remaining uninspected internals are distinguished above. | [Package and entry points](https://github.com/vectifyai/openkb/blob/ff54396e575ee6feb0113b631a34caa082b441cc/pyproject.toml); [CLI production/maintenance](https://github.com/vectifyai/openkb/blob/ff54396e575ee6feb0113b631a34caa082b441cc/openkb/cli.py); [chat persistence](https://github.com/vectifyai/openkb/blob/ff54396e575ee6feb0113b631a34caa082b441cc/openkb/agent/chat_session.py); [external-agent instructions](https://github.com/vectifyai/openkb/blob/ff54396e575ee6feb0113b631a34caa082b441cc/skills/openkb/SKILL.md). Other initial paths are named above at this same commit. | No repository access blocker. Private design documents, actual user KBs, external dependency implementations/services, published distribution bytes and host-agent executions are not supplied; prevents private-history, deployed-behavior and efficacy conclusions. Implementation and doctrine do not establish observed operation or causal benefit. |
