---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "post-graph-rag's shipped knowledge-system paths and consumers at commit bce4146a7dc4684e9b66806915c29b0eed57ba23."
run-id: AAS-2026-11-08-post-graph-rag-448d75e4222d-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/crajah/post-graph-rag
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/post-graph-rag-2c29e35fc2c9/related-systems/crajah--post-graph-rag
  revision: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
  sha256: null
---

# post-graph-rag boundary

## Boundary and evidence

This run analyses post-graph-rag as a knowledge system for retaining document and conversational information and supplying retrieved context or synthesized answers. It is in scope because its shipped indexing, community reporting and answering paths issue model calls. The target is not an enclosing autonomous-agent runtime. The whole-system boundary includes the Python package, its embedded prompts, and shipped examples, corpus drivers, maintenance interfaces and evaluation consumers—not merely the exported API. The applicability cutoff is 2026-11-08; all evidence is fixed to commit `bce4146a7dc4684e9b66806915c29b0eed57ba23` of SRC-1, not a moving release or website.

The intended role is explicit in the shipped introduction (SRC-1, `README.md`):

> `post-graph-rag` extracts entities and relations with an LLM, stores them as a property graph beside `pgvector` embeddings, and answers questions by fusing vector similarity, graph traversal and full-text search.
> --- `README.md`

The public package exports `GraphRAG`, the store, extractor, model service, metadata and retrieval parameters (SRC-1, `post_graph_rag/__init__.py`). The implementation trace connects `GraphRAG` construction to the model service, extractor, reporter and store; indexing prepares a chunk and writes its passage and derived structure; retrieval feeds stored chunks, entities, relations and community reports into answer synthesis (SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/extractor.py`, `post_graph_rag/reporting.py`). These executable paths establish a code-grounded classification, rather than relying solely on the introduction. The model call itself is visible in SRC-1, `post_graph_rag/extractor.py`:

> result = await self.llm_service.chat_completion(
>     messages, response_format=ExtractionResult, role="extraction")
> --- `post_graph_rag/extractor.py`

Functional coverage includes admission through extraction and validation, passage/graph persistence, replacement and dormancy, relation supersession, community rebuilds, optional retention and retrieval telemetry, change polling, retrieval and prompt assembly. These responsibilities are shipped in SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`, `post_graph_rag/extractor.py`, `post_graph_rag/retention.py` and `post_graph_rag/deltas.py`. This identifies the paths to analyse; it does not establish correctness of every path.

The shipped callers are part of this boundary. `demo_rag.py` indexes documents and consumes both structured retrieval and synthesized answers. `examples/05_incremental_and_deltas.py` consumes retained-state changes; `examples/06_communities_and_exploration.py` builds reports and queries them. `evaluation/index_corpus.py` persists corpus chunks in a named realm, optionally resetting it; `evaluation/analyse_graph.py` connects to that realm and queries it later. `evaluation/ectqa/replay.py` reloads baseline question records and queries a supplied existing realm. `evaluation/longmemeval/run.py` supplies a conversational extraction prompt and maps sessions into indexed documents. These are not excluded applications merely because they call the package API (all SRC-1).

The enclosing exploration or verification loop remains a consumer responsibility. The shipped design states the distinction (SRC-1, `docs/ROADMAP.md`):

> Explorer/verifier agents, hypothesis generation, report stacks: application
> layer. The engine exposes structure (§3), coverage (§2), and change (§1);
> what explores them is the consumer's loop.
> --- `docs/ROADMAP.md`

External dependencies are not independently frozen sources. Packaging declares `post-graph`, OpenAI's client, Pydantic, igraph and leidenalg; the store constructs `AsyncPostGraph`, and the model service calls OpenAI-compatible APIs (SRC-1, `pyproject.toml`, `requirements.txt`, `post_graph_rag/graph_store.py`, `post_graph_rag/llm.py`). PostgreSQL and pgvector are external infrastructure. This boundary supports claims about this repository's calls, SQL and contracts, not independent claims about dependency internals, deployed database guarantees, provider behavior or authorization configuration. Consumer-supplied connections, extractors and prompts are supported interfaces, not evidence that a particular outside application implemented them correctly.

### Repository coverage

The tracked tree was enumerated at the frozen commit. “Included” means evidence within the functional boundary, not that every blob has already been reviewed. Inspection status below separates traced material paths from available material awaiting detailed analysis. No material shipped path was found inaccessible. All paths in this table belong to SRC-1.

| Top-level tracked path | Coverage and role | Initial inspection and limits |
| --- | --- | --- |
| `post_graph_rag/` | Included: `__init__.py` exports; `engine.py` indexing, maintenance, retrieval and synthesis; `graph_store.py` persisted state and SQL; `extractor.py` admission and prompts; `llm.py` model access; `reporting.py` report prompts; `retention.py` archiving; `deltas.py` change reads; `communities.py`, `chunking.py`, `models.py`, `config.py`, `errors.py` supporting algorithms and contracts. | Public exports and material engine paths traced into extraction, writes, community rebuilds, query assembly, telemetry and retention. Store construction, extraction call and service call inspected; retention read. Supporting definitions and remaining SQL are available for deeper analyst inspection, not access gaps. |
| `demo_rag.py` | Included: shipped indexing and answering consumer, with demo cleanup. | Read in full; follows initialization, writes, queries and schema drop. |
| `examples/` | Included: `01_quickstart.py` through `07_retrieval_modes.py`, `_shared.py` and `README.md`; demonstrations of retained-state production and consumption. | Scripts 05 and 06 read; all seven roles identified in root README. Other scripts and helper details remain available, not independently verified here. |
| `evaluation/` | Included: corpus acquisition, `index_corpus.py`, `analyse_graph.py`, `build_communities.py`, `temporal_eval.py`, `compare_realms.py`, `compare_lightrag.py`, `blind_quota_judge.py`; LongMemEval, ECT-QA and TEMPO subdirectories with indexing/reader/scoring/replay/ablation code, prompts and tracked results. | README read; evaluator entry points inventoried; corpus writer and later reader traced; LongMemEval prompt/mapping inspected; ECT-QA replay into an existing realm traced; indexing/query/output call sites inspected for benchmark runners. Other evaluator internals and result JSON bodies remain available but unassessed. Their presence does not establish benchmark validity or observed success. `.DS_Store` files are excluded metadata. |
| `tests/` | Included: contract and regression evidence, especially lifecycle, provenance/dormancy, temporal, hierarchy, retention, model-role and query-path suites plus `conftest.py`. | Tree inventoried; retention call sites searched; CI test configuration inspected. Assertions and fixtures otherwise await detailed inspection. Tests were not run, so no passing-test conclusion is available. |
| `README.md` | Included: intended use, API, maintenance guidance and attributed benchmark claims. | Read in full. Claims are doctrine or reported operation, not independently reproduced results. |
| `docs/` | Included: `index.md` explanatory article, `ROADMAP.md` exploration/maintenance design and `_config.yml` publishing configuration. | Article/roadmap headings surveyed and roadmap application-layer exclusion read. Remaining prose/configuration is available, not yet assessed for consistency with code. |
| `tables/` | Included: article CSV tables, `README.md` provenance/publication explanation and `extract.py` table-generation utility. | README read and files inventoried; CSV figures and extraction implementation not yet audited. No independent comparative-performance conclusion follows. External gists were not consulted. |
| `pyproject.toml` | Included: package metadata, dependencies, build and test/lint settings. | Read in full; no installed package or release artifact inspected. |
| `requirements.txt` | Included: dependency declaration. | Read in full; dependencies not installed or independently reviewed. |
| `.github/` | Included: `workflows/ci.yml`, `workflows/publish.yml` and `FUNDING.yml`; test/release configuration and funding metadata. | Workflows read; funding file only inventoried. Configured jobs are not execution traces or proof of a released artifact. |
| `Makefile` | Included: development, test, build and publication commands. | Read in full, not executed. |
| `CONTRIBUTING.md` | Included: contributor/test/evaluation instructions and invariants. | Headings surveyed; detailed instructions remain available. |
| `CHANGELOG.md` | Included: attributed release history, subordinate to the pinned implementation for current behavior. | Inventoried, not yet read; no historical transition claim established here. |
| `LICENSE` | Excluded: legal terms, not knowledge-state operation. | Prevents a legal/licensing assessment; does not remove a state path. |
| `.gitignore` | Excluded: checkout hygiene. | No conclusions about completeness of an operator's ignored local runtime data. |
| `.DS_Store` | Excluded: desktop metadata. | No desktop-environment reconstruction; no knowledge-loop conclusion depends on it. |

### Evidence limits

The source register is one repository at one commit. It does not include linked papers, external repositories, hosted documentation revisions, datasets downloaded by fetch scripts, ignored corpus files, database contents, provider services or external comparison-system installations. Their absence prevents independent reconstruction of deployed operation and external comparisons; it does not exclude the shipped harness code that refers to them. No target code, examples, tests or provider calls were executed for this boundary.

Tracked result files are available for later inspection within SRC-1. They have not been inspected as run evidence here. The root README and evaluation README supply attributed reported operation, while implementation and embedded prompts supply executable mechanisms and declared contracts. This boundary establishes neither independently observed performance nor causal effects. Unread available files are not access gaps and remain within the registered repository boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/crajah/post-graph-rag` | bce4146a7dc4684e9b66806915c29b0eed57ba23 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/post-graph-rag-2c29e35fc2c9/related-systems/crajah--post-graph-rag`. Implementation: exports, material engine indexing/maintenance/community/query paths, extractor/model-service calls, store construction, retention, demo and selected example/evaluator consumers, packaging and workflows. Doctrine/design: full root README, embedded extraction/report/synthesis prompts, roadmap application-layer boundary, evaluation README and table-publication README. Reported operation: benchmark/operational accounts in root and evaluation READMEs only. Coverage table records bounded inspection and outstanding detail. | Implementation: [engine](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/post_graph_rag/engine.py), [extractor](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/post_graph_rag/extractor.py), [persistent-corpus reader](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/evaluation/analyse_graph.py), [replay consumer](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/evaluation/ectqa/replay.py). Doctrine/design: [README](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/README.md), [roadmap](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/docs/ROADMAP.md). Reported operation: [evaluation account](https://github.com/crajah/post-graph-rag/blob/bce4146a7dc4684e9b66806915c29b0eed57ba23/evaluation/README.md). | No identified repository access gap. External dependency internals, live deployments, downloaded corpora and service responses are outside the frozen source set; no independent runtime, benchmark-reproduction or causal-effect conclusion. Tracked result artifacts remain unassessed, not inaccessible. |
