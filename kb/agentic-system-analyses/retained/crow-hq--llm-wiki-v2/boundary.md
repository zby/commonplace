---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Wiki v2's shipped knowledge lifecycle, interfaces and evaluators at commit e0a205afe60bd1913d083a3ed4cdab81e38e4c26."
run-id: AAS-2026-11-08-llm-wiki-v2-5abff9a6c5c3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e0a205afe60bd1913d083a3ed4cdab81e38e4c26
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/crow-hq/llm-wiki-v2
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-v2-0504f862305f/related-systems/crow-hq--llm-wiki-v2
  revision: e0a205afe60bd1913d083a3ed4cdab81e38e4c26
  sha256: null
---

# LLM Wiki v2 boundary

## Boundary and evidence

This run analyses the shipped LLM Wiki v2 repository as a knowledge system: how documents and client memories become retained Markdown notes, how later questions consume those notes, and how users and code maintain the retained state. The target includes both classic and classifier-routed CROW operation. It is not limited to the Python library API or to its MCP endpoint. The repository ships callers, persistence, retrieval, maintenance, prompts and evaluation drivers, so the boundary is `whole-system`, not an excluded-host library boundary.

The classification rests on the shipped loop, not only the product description. SRC-1 `src/llmw2/wiki.py` constructs the store, models, prompts, Librarian and Researcher. SRC-1 `src/llmw2/agents/librarian.py` routes incoming material, chooses merge or creation, saves the source, writes a note, links related notes and logs the change. SRC-1 `src/llmw2/bundle/store.py` writes notes and indexes, retains raw text, and reloads folder state. SRC-1 `src/llmw2/agents/researcher.py` reloads the tree for a subsequent question, selects notes and produces an answer from them. The latter explicitly constrains returned citation paths to the selected notes:

> citations = [c for c in dict.fromkeys(_cited(text)) if c in read]
> --- `src/llmw2/agents/researcher.py`

The shipped prompts state the intended division of responsibilities; these are design evidence, not proof of factual preservation:

> You decide where knowledge goes and write the notes; code creates the files, the indexes and the links.
> --- `src/llmw2/agents/prompts/librarian/system.md`

The same retained state is exposed through the CLI, HTTP/web application and optional MCP memory. The console script is bound to `llmw2.cli:main` in SRC-1 `pyproject.toml`; SRC-1 `src/llmw2/__main__.py` calls that same entry point. The CLI's ingest, sync, rebuild and ask branches call the Wiki facade. SRC-1 `src/llmw2/server.py` routes HTTP ingest/upload/ask requests to its current Wiki and serves the web assets; SRC-1 `src/llmw2/web/queue.js` sends uploads or text ingests, and SRC-1 `src/llmw2/web/app.js` posts questions. These are included shipped consumers, not external applications.

SRC-1 `src/llmw2/memory.py` connects MCP tools to the same loop. In particular, `remember` calls `wiki.ingest`, `recall` calls `wiki.ask`, and `read_note` reads the store. Its client-model setting can relay model requests through a client while the wiki still runs its filing and retrieval code. This makes the MCP integration part of the system, but does not make Claude Code, Codex or another MCP client's enclosing agent loop part of the target. The retained-memory write enters the same filing implementation:

> return self.run(lambda wiki: filed(wiki.ingest(text, title=title or None, author=by)))
> --- `src/llmw2/memory.py`

Maintenance includes source synchronization and origin tracking, replacement/archiving, deletion and purge, route audits, taxonomy health, user-managed areas, batch planning and folder splitting, plus rebuilding from retained raw copies. These responsibilities stay inside the boundary even when initiated by a user or driver. SRC-1 `src/llmw2/sources/sync.py` turns connector changes into `wiki.ingest_many` calls and stores per-connector cursor state. SRC-1 `src/llmw2/wiki.py` implements rebuild by clearing retained state while keeping folders, then filing again without a plan:

> with self.store.lock():
>     self.store.clear(keep_folders=True)
> return self.ingest_many(items, concurrency=concurrency, on_result=on_result, plan=False)
> --- `src/llmw2/wiki.py`

The evidence is frozen at SRC-1 commit `e0a205afe60bd1913d083a3ed4cdab81e38e4c26`, with applicability cutoff 2026-11-08. The checkout HEAD was checked against that pin. The overall tier is `code-grounded`: executable source was traced from shipped entry points into retention and later consumption. No target code, tests, examples, benchmarks or providers were executed. Prompt goals, benchmark tables and author explanations remain declared or reported evidence, not independently observed success.

### Top-level coverage

The tracked tree was enumerated. Included means eligible evidence within the functional boundary, not a claim that every file has already been read. The initial inspection below traces the material lifecycle; remaining available files may be inspected at the same pin. No material lifecycle path was unavailable.

| Top-level tracked path | Treatment and role | Initial inspection and conclusion limit |
|---|---|---|
| `src/` | Included: `llmw2/wiki.py`; `agents/` including classic/CROW steps, revisions and packaged prompts; `bundle/` persistence, formats, origins, proposals and checking; `models/` providers, classifier, cache and relay; `sources/` connectors and sync; `cli.py`, `server.py`, `memory.py`, settings/config; `web/` clients and `demo/` seed state. | Traced Wiki construction and ingest/batch/rebuild/ask, Librarian filing, store load/write/raw retention, Researcher selection/answer, CLI and HTTP consumers, MCP tools and relay dispatch; read core system prompts; searched web upload and question calls. Supporting algorithms, remaining prompt templates, demo content and vendor assets are available, not all inspected. This is not a feature-by-feature correctness finding. |
| `benchmarks/` | Included: corpus and labels, judgement prompts and retained judgements; stability, filing-error, fact-retention, incremental and retrieval evaluators; replay and corpus-selection/generation tools, including `office/`. | Read benchmark README's corpus/script inventory and retrieval driver opening and setup; searched incremental driver's calls into Wiki. Evaluation consumers belong to the target. No benchmark was run; uncommitted real corpora and private results cannot be independently reconstructed from this checkout alone. |
| `tests/` | Included: `wiki/` fake models and tests for persistence, filing, retrieval, sources, maintenance, server/MCP, providers and evaluators. | Enumerated tests and read MCP test setup using fake models and an in-process client. Other tests are available, not all inspected. Test existence is not a passed test result or real-model evidence. |
| `examples/` | Included: quickstart, custom selection/summarization, labelled dataset and sync connector callers. | Read `sync_connector.py`, which persists successive connector changes through the library. Remaining examples were inventoried, not fully read; no example was executed. |
| `docs/` | Included: `library/index.md`, `library/steps.md`, `wiki/crow.md`, `wiki/memory.md`, `wiki/prompts.md`, `wiki/providers.md`; `assets/` presentation material. | Paths inventoried; README links and role descriptions inspected. Full guides and images not yet inspected. Available design material, not an access gap or independent runtime evidence. |
| `README.md` | Included: usage, lifecycle, storage, interfaces and author-reported measurements. | Read; linked external papers, desktop application and corpora are not imported into this evidence boundary. |
| `pyproject.toml` | Included: package, entry point, dependency and resource declarations. | Read; establishes shipped CLI and packaged prompts/web/demo resources, not dependency implementation behavior. |
| `Dockerfile`, `docker-compose.yml` | Included: server launch, model configuration and persistent volume integration. | Read; deployment caller and persistence mounting are included, but successful deployment is not observed. |
| `.env.example` | Included: configuration surface. | Inventoried; README configuration account inspected, full file not yet read. |
| `uv.lock` | Included: dependency lock evidence. | Inventoried, not read in detail; no claim of installed dependency behavior or reproducible runtime execution. |
| `CHANGELOG.md`, `CITATION.cff` | Included: release narrative and attribution metadata. | Inventoried, not yet inspected; historical claims require reading and attribution before use. |
| `.github/` | Excluded: issue/PR templates and CI/CLA/release workflows. | Paths inventoried. Exclusion prevents conclusions about CI execution, release integrity or contribution automation; it does not exclude the test source itself. |
| `.dockerignore`, `.gitignore` | Excluded: build-context and version-control hygiene. | Inventoried. No conclusion about exhaustive image contents or ignored local artifacts. |
| `CLA.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md` | Excluded: governance, contribution and disclosure policies. | Inventoried. No assessment of policy compliance, disclosure practice or organizational security maturity. Executable server guards remain included. |
| `LICENSE`, `LICENSES/`, `NOTICE` | Excluded: legal texts and third-party notices. | Inventoried. No legal or licensing-compliance conclusion. |

### External dependencies and evidence limits

Model providers and classifier servers, Python dependencies (including the optional MCP SDK), operating system/filesystem behavior, browser engines and external source connectors are dependencies, not separately frozen implementations. Their integration code in SRC-1 is included; their independent guarantees are not. Client-side model compliance and the enclosing MCP client's scheduling, tools and session memory are outside the target, preventing claims that wiki instructions enforce those clients' behavior. The separate Crow desktop repository is outside this source pin, preventing conclusions about its packaging, UI or agent behavior (SRC-1 `README.md`, `src/llmw2/memory.py`, `pyproject.toml`).

The external papers and noncommitted real benchmark corpora mentioned in SRC-1 `README.md` and `benchmarks/README.md` are not frozen sources here. Repository descriptions and retained tables can support attributed reports, but not verification of the underlying private corpus, external experiments or broad accuracy/scaling claims. No live browsing or additional repository is needed to establish this boundary. Missing execution evidence limits operational conclusions; available-but-unread files are not described as inaccessible.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/crow-hq/llm-wiki-v2` | e0a205afe60bd1913d083a3ed4cdab81e38e4c26 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-v2-0504f862305f/related-systems/crow-hq--llm-wiki-v2`. Implementation: tracked tree, `pyproject.toml`, `src/llmw2/__main__.py`, `src/llmw2/wiki.py` construction/batch/ingest/ask/rebuild, `src/llmw2/agents/librarian.py` filing/source save, `src/llmw2/agents/researcher.py` ask, `src/llmw2/bundle/store.py` load/write/raw retention, CLI dispatch, HTTP app and upload/ask endpoints, `src/llmw2/memory.py`, sync apply/cursor paths, web call sites, `examples/sync_connector.py`, `benchmarks/retrieval.py` setup, incremental call sites, MCP test setup, Docker files. Doctrine/design: `README.md`, librarian/researcher system prompts and MCP instructions. Reported operation: README measurements; benchmark README corpus and evaluator descriptions. | [Wiki facade](https://github.com/crow-hq/llm-wiki-v2/blob/e0a205afe60bd1913d083a3ed4cdab81e38e4c26/src/llmw2/wiki.py); [MCP tools](https://github.com/crow-hq/llm-wiki-v2/blob/e0a205afe60bd1913d083a3ed4cdab81e38e4c26/src/llmw2/memory.py); [store](https://github.com/crow-hq/llm-wiki-v2/blob/e0a205afe60bd1913d083a3ed4cdab81e38e4c26/src/llmw2/bundle/store.py); [product account](https://github.com/crow-hq/llm-wiki-v2/blob/e0a205afe60bd1913d083a3ed4cdab81e38e4c26/README.md); [evaluation inventory](https://github.com/crow-hq/llm-wiki-v2/blob/e0a205afe60bd1913d083a3ed4cdab81e38e4c26/benchmarks/README.md) | No unavailable shipped lifecycle path encountered. No observed run or causal experiment established. External clients/providers, separate desktop app, papers and uncommitted/private corpora are outside the frozen source: their internals, empirical validity and end-to-end operating guarantees cannot be established here. |
