---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Wiki's shipped knowledge-production, maintenance and consumption paths at commit 0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7."
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/Clod/llmwiki-marimo
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-llmwiki-marimo-retry-1/related-systems/Clod--llmwiki-marimo
  revision: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
  sha256: null
---

# llmwiki-marimo boundary

## Boundary and evidence

This run examines LLM Wiki as a local knowledge system: how documents become retained wiki pages and searchable state, how that state is maintained, and how later reading and model calls consume it. It is in scope because its knowledge-production and question-answering paths issue model calls. The primary target class is **memory/knowledge/context-engineering system**, not merely its retrieval library or its embedded chat agent. The boundary kind is **whole-system**: the shipped web application, retained marimo applications, service and domain layers, prompts, maintenance paths and evaluation drivers belong to the target. They are not excluded hosts simply because they call shared APIs (SRC-1, `quickstart.py`, `web/app.py`, `base/services/ingest.py`, `base/services/chat.py`, `marimo/ingest_app.py`).

The intended use is personal document ingestion, browsing and grounded chat. The project's own description is:

> A personal, local-first wiki that ingests your documents, builds a structured knowledge base, and lets you read and chat with it — all on your machine, no cloud required.
> --- `README.md`

The inspected production path extracts structured knowledge, creates or updates concept and summary pages, updates references and the index, and writes overview/history state. Retention is therefore part of the shipped application, rather than an assumed behavior of an external caller (SRC-1, `base/domain/ingestion/pipeline.py`, `base/services/wiki.py`). A minimum implementation anchor is:

> existing_content = read_page(db_path, workspace, "/wiki/concepts/", slug)
> --- `base/domain/ingestion/pipeline.py`

This existing page becomes input to concept-page generation in the same path. Consumption is also shipped: the agent factory registers wiki reads, wiki search and raw-source search; service code invokes agents against the workspace database. Its declared tool priority is:

> Tools (in priority order per system prompt) — all read-only:
> --- `base/domain/chat/agent.py`

The boundary includes code-controlled pre-retrieval, strict and streaming chat paths; conversation context and condensation; optional structured datasets and the Argentine-finance overlay; manual edits, vocabulary/settings changes, verification, lint/repair, deletion, reindexing and history restoration. Initial inspection traced their composition roots and maintenance dispatch, not every internal algorithm (SRC-1, `base/services/chat.py`, `web/state.py`, `base/services/ingest.py`, `base/services/wiki.py`, `base/domain/rollback/revert.py`).

Admission of chat content is a separate application responsibility. The web caller drafts a conversation page for review, then saves submitted Markdown through the service; the retained marimo callers instead submit the last response through `save_answer`. The analysis must preserve this distinction rather than assign the web review step to every interface (SRC-1, `web/routes/chat.py`, `marimo/read_app.py`, `marimo/read_app_tabs.py`, `base/services/chat.py`). The web service states:

> Step 2 of saving (`wiki_tools.write_wiki_page`), then one git commit,
> `chat: <title>`. The text is not sent to the model; the post-save repair is
> the deterministic one.
> --- `base/services/chat.py`

### Frozen evidence and limits

The sole registered source is the acquired Git checkout at **0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7**; its HEAD was verified against the acquired revision. Applicability is cut off at **2026-10-18** and at this commit, not at the moving default branch or current dependency services. The evidence tier is **code-grounded**. Implementation and source-native doctrine/design are available. No target execution, dependency installation, provider call or test run was performed. Evaluator source establishes what is checked, not that this revision passes or that a particular model behaves reliably.

External dependencies include PydanticAI, OpenAI-compatible model endpoints, SQLite/FTS5, FastAPI/HTMX and marimo, document extractors and optional local verification-model packages. These dependencies are represented by their shipped integration code and dependency declarations, not independently frozen implementations (SRC-1, `pyproject.toml`, `base/domain/chat/agent.py`, `web/app.py`, `web/state.py`). Their internals and model weights are excluded: this prevents conclusions about provider/runtime correctness, extraction accuracy or verifier calibration beyond the target's integration contract. User-created workspaces and deployments are not supplied; the bundled examples and fixtures are not evidence of general deployment performance. No access failure was encountered. Uninspected available files below are inspection limits, not access gaps.

### Top-level coverage

All top-level tracked entries were enumerated. “Included” fixes functional scope; it does not claim a full-file audit. Material state-loop paths were traced through executable callers. Supporting assets and documentation not yet read remain available at the same registered commit.

| Top-level tracked entry | Treatment and material paths | Inspection and limits |
|---|---|---|
| `base/` | Included: `services/{wiki,chat,ingest,verification,vocabulary,settings}.py`; `domain/{ingestion,chat,datasets,finance_argentina,lint,repair,rollback,verify,tools}`; prompt/config/registry/tracing support. Produces, persists, reloads, maintains and consumes knowledge. | Read selected service and agent bodies and pipeline writes; searched maintenance, dataset/overlay, reindex and verification entry points. Detailed algorithm and edge-case inspection remains for later members. |
| `database/` | Included: `sqlite_schema.sql`, retained document/chunk/reference/verification index contract. | Read initial schema and derived-state commentary; remaining table details not yet inspected. No claim that every field is reconstructible. |
| `web/` | Included: `app.py`, `state.py`, `routes/{chat,ingest,pages,history,settings,vocabulary,datasets,picker,relations,audit,lang}.py`, templates/static/localization. Owns application orchestration and user actions. | Read factory/state and chat draft/save bodies; searched ingest, page and history service calls. Rendering assets and remaining route bodies not yet inspected; no visual/accessibility or route-security audit. |
| `marimo/` | Included: `ingest_app.py`, `read_app.py`, `read_app_tabs.py`, deletion widget and layout. Retained shipped callers, not external hosts. | Read ingestion/scan/regeneration and last-answer saving/wiki-opening cells; searched chat and maintenance service usage. Layout/widget details not yet inspected; no claim of parity with web behavior. |
| `prompts/` | Included: English/Spanish chat, extraction, ingestion, concept creation/update, overview, condensation, pre-retrieval, dataset, refusal and lint templates/directives. | Read `system_prompt.en.md`; enumerated all prompt files and searched prompt-loading integration. Other template bodies not yet inspected; no claim of translation equivalence or uniform prompt compliance. |
| `docs/` | Included as source-native design/operating instructions: manual workflows for lint, repair, ingestion, chat/save and deletion; retrieval/dataset contracts, walkthroughs and architecture maps. | Read `manual/workflows/6.2-repair.md`; scanned workflow headings. Remaining manuals, archived plans and walkthroughs not yet inspected. Plans are not implemented behavior and reported results are not independently reproduced. |
| `examples/` | Included: `fairy-tales/`, `cuentos-de-hadas/`, `finanzas-argentinas/` sources, retained pages/indexes/configuration; finance datasets and demo/UAT instructions. | Read `README.md` and enumerated workspace contents; corpus bodies and binary indexes not yet inspected. No validation of factual content, data freshness or example-generation provenance. |
| `scripts/` | Included: `build_golden_corpus.py`, `eval_chat_model.py`, `build_eval_packet.py`, `verify_pages.py`, `verify_battery.py`, `wiki_revert.py`, finance UAT, capture/demo/trace drivers. | Read model-suitability checks and packet assembly; searched verification/rollback entry points and enumerated drivers. Remaining driver bodies not yet inspected. Evaluations are part of scope, but no benchmark result is established. |
| `tests/` | Included: unit, regression, marimo/web end-to-end suites, helpers and retained golden/finance fixtures. | Read initial `regression/test_golden_corpus.py` invariants; enumerated suites and fixtures. Other assertions/fixtures not yet inspected and none executed; no pass-rate or coverage claim. |
| `quickstart.py` | Included: demo installation, configuration, dependency setup, optional verification, model check and application launch. | Read orchestration/launch and searched setup functions. Installer details not fully audited. |
| `pyproject.toml` | Included: project metadata and runtime/web/verification dependencies. | Read completely; declarations do not establish installed dependency behavior. |
| `wiki_config.example.toml`, `wiki_config_es.example.toml`, `.env.example` | Included: configuration surfaces for wiki and provider/model behavior. | Enumerated; bodies not yet inspected. No assertion of default-value equivalence across these examples. |
| `README.md`, `README_ES.md` | Included: intended use and operation. | Read English opening through workspace/history description; Spanish and remaining English sections not yet inspected. Documentation claims require implementation checks. |
| `requirements.txt`, `requirements-verify.txt`, `uv.lock` | Included as dependency/install evidence. | Searched selected package pins in requirements; lock contents not yet inspected. No independent dependency reproducibility or vulnerability conclusion. |
| `pytest.ini` | Included as evaluation configuration. | Enumerated, not yet inspected; test-selection defaults not established. |
| `.github/` | Deliberately excluded from operational-loop analysis: issue/PR templates and `workflows/test.yml`. | Tree inspected, bodies not read. Prevents conclusions about CI execution or project intake governance, not application state flow. |
| `.gitignore`, `.python-version` | Deliberately excluded repository tooling metadata. | Tree inspected, bodies not read; no conclusion about development ignore rules or interpreter-selection enforcement. |
| `CHANGELOG.md`, `ROADMAP.md` | Deliberately excluded release-history and future-planning account. | Not read; prevents historical evolution and roadmap-completion conclusions. Current behavior is bounded by implementation. |
| `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `RELEASING.md`, `SECURITY.md`, `SUPPORT.md` | Deliberately excluded contributor/release/support/security policy. | Not read; prevents conclusions about governance, release procedure or the completeness of the stated security model. Does not exclude executable access controls. |
| `LICENSE`, `NOTICE` | Deliberately excluded licensing/attribution analysis. | Not read; prevents independent license/provenance conclusions. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Clod/llmwiki-marimo` | 0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-llmwiki-marimo-retry-1/related-systems/Clod--llmwiki-marimo`. Implementation: tree, launch/factory/state, web draft/save caller, marimo save/ingest callers, selected service bodies, agent factory and pipeline writes; bounded searches of repair/rollback/reindex, datasets/finance activation, prompt loader, verification and evaluator entry points; selected evaluator/regression bodies and SQL schema. Doctrine/design: README opening, example-workspace README, repair workflow, English chat prompt and dependency declarations. | Implementation: [launch](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/quickstart.py), [web caller](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/web/routes/chat.py), [chat service](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/base/services/chat.py), [pipeline](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/base/domain/ingestion/pipeline.py), [agent](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/base/domain/chat/agent.py), [model check](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/scripts/eval_chat_model.py). Doctrine/design: [README](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/README.md), [repair instructions](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/docs/manual/workflows/6.2-repair.md), [chat prompt](https://github.com/Clod/llmwiki-marimo/blob/0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7/prompts/system_prompt.en.md). | No repository access gap. Initial inspection is selective as detailed above, not an allowlist. No execution evidence was inspected or generated; implementation and declared checks do not establish model quality, runtime success, security or causal improvement. External dependencies, deployed workspaces and subsequent revisions are outside this frozen source. |
