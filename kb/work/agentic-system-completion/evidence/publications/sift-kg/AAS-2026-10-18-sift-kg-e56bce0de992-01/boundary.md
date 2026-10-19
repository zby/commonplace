---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "sift-kg's shipped document-to-graph pipeline and agent-facing memory interface at commit d786991c024f5401f113fc0cb70aee96dd1bd3bf."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/juanceresa/sift-kg
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-sift-kg/related-systems/juanceresa--sift-kg
  revision: d786991c024f5401f113fc0cb70aee96dd1bd3bf
  sha256: null
---

# sift-kg boundary

## Boundary and evidence

sift-kg is in scope as a memory/knowledge/context-engineering system. Its intended use is to turn documents into a retained knowledge graph, maintain that graph through build and resolution commands, and expose it to humans and external AI agents. The boundary covers the whole shipped repository product, not merely its library API or its extraction computation. The bundled agent skill is part of this boundary: it prescribes how an external agent reloads and consumes retained content across sessions. It is evidence of intended host use, not evidence that a host actually follows it (SRC-1, `README.md`, `.agents/skills/sift-kg/SKILL.md`).

> Use sift-kg as an AI second brain — a persistent knowledge graph your agent operates from across sessions.
> --- `.agents/skills/sift-kg/SKILL.md`

The shipped entry points are the `sift` console application, module invocation and Python exports. The CLI itself performs extraction, build, resolution, review, application of decisions, narrative generation and retrieval; it is not an excluded application around a narrower library. `pipeline.py` separately offers explicit-parameter library functions and an extract/build/narrate driver. Both callers belong to the target (SRC-1, `pyproject.toml`, `src/sift_kg/__main__.py`, `src/sift_kg/__init__.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`).

> sift = "sift_kg.cli:app"
> --- `pyproject.toml`

The functional loop includes document reading and chunking; model-backed schema discovery and extraction; per-document extraction persistence and reuse; deterministic graph construction and deduplication; model-proposed entity resolution; review decisions; graph mutation; community and narrative artifacts; and later reload for query, topology, search, export and visualization. The extraction caller writes cached extraction JSON; build consumes extraction files and saves `graph_data.json`; resolution and review use YAML decision files; apply-merges reloads and updates the graph. The CLI's topology and query commands reload that retained graph to return agent-facing structure (SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`).

> extraction_path = extraction_dir / f"{doc_id}.json"
> extraction_path.write_text(extraction.model_dump_json(indent=2))
> --- `src/sift_kg/extract/extractor.py`

> kg = KnowledgeGraph.load(graph_path)
>
> # --- Input resolution ---
> matched_id: str | None = None
> --- `src/sift_kg/cli.py`

Admission and maintenance include automatic processing as well as human decisions. In particular, the shipped reviewer can automatically confirm sufficiently confident proposals; the boundary does not assume every merge requires a separate human approval. The simple library pipeline does not perform the review loop itself, but that loop remains included through the shipped CLI and library stage functions (SRC-1, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`).

> Proposals where ALL members have confidence >= auto_approve_threshold
> are automatically confirmed without interactive review.
> --- `src/sift_kg/resolve/reviewer.py`

### Repository coverage

The tracked top-level tree was enumerated at the frozen commit. “Included” defines analytical scope; it does not assert exhaustive file-level inspection. Initial inspection below distinguishes full reads, bounded code reads and symbol/call-site scans. No material shipped loop path is deliberately excluded or unavailable.

| Top-level tracked path | Scope and role | Initial inspection and limits |
|---|---|---|
| `.agents/` | Included: `.agents/skills/sift-kg/SKILL.md`, agent session orientation, graph lookup, rebuild and resolution instructions. | Skill read fully; instructions are doctrine, not an observed agent session. |
| `.env.example` | Included: example provider and project configuration. | Enumerated, not read; no claim about every example setting. Configuration responsibilities were located in `src/sift_kg/config.py` and the extraction CLI. |
| `.github/` | Included: `workflows/ci.yml` lint/test driver and `workflows/pages.yml` demo publication. | Command/path scan identifies pytest and static demo deployment; no execution or CI success inferred. |
| `.gitignore` | Included: repository hygiene. | Enumerated, not read; no ignore-policy conclusion. |
| `LICENSE` | Included: distribution terms. | Enumerated, not read; no legal conclusion. |
| `README.md` | Included: user workflow, library API, configuration, review and agent-memory claims. | Read fully; claims remain declared intent unless supported by implementation. |
| `examples/` | Included: `ftx/docs/`, extraction caches and graph/review/narrative outputs; `transformers/` and `ontoverse_az/` configuration and retained community/narrative/viewer outputs. | Tree and README command/description scan identifies shipped input/output examples. Output bodies not yet inspected. Examples do not by themselves establish reproducibility, correctness or measured agent benefit. |
| `pages/` | Included: `index.html`, static demo landing page consuming the published examples. | Link/title scan plus pages workflow paths; no browser behavior verified. |
| `pyproject.toml` | Included: installation, `sift` entry point, dependencies and test/lint configuration. | Read fully. |
| `src/` | Included: `sift_kg/cli.py`, `__main__.py`, `__init__.py`, `pipeline.py`; `config.py`; `ingest/` readers, chunker and OCR backends; `domains/` schema discovery, loader, models and bundled YAML; `extract/` prompts, models, caching and model client; `graph/` builder, pre-deduplication, postprocessor, persistence and communities; `resolve/` proposal generation, models, YAML I/O, review and application; `narrate/` prompts and generator; `export.py`, `visualize.py`, and `viewer/` browser assets. | Entry modules and pipeline read fully; bounded CLI reads trace extraction, review/application, topology and query. Async extraction cache/discovery/write path read; reviewer admission excerpt read. Symbol, persistence and model-call scans locate the other stage implementations, prompts and viewer consumers. Detailed algorithms and presentation bodies not exhaustively inspected here. |
| `tests/` | Included: `conftest.py` fixtures and `test_*.py` covering configuration, domains, ingestion, extraction/prompts, model JSON parsing, graph build, deduplication, clustering, review/application, communities, narrative prompts, export, view filtering and agent-facing CLI JSON. | Test-class/function scan plus bounded `test_cli_json.py` read shows synthetic graph construction and CLI invocation. Test bodies are implementation evidence of checks, not observed passing runs or a quality benchmark. |

### Frozen boundary and external limits

The sole frozen source is SRC-1 at `d786991c024f5401f113fc0cb70aee96dd1bd3bf`; checkout HEAD was checked against the acquired revision. The analysis cutoff is 2026-10-18, the supplied run date, not an assertion about a deployment date. Evidence is code-grounded with source-native doctrine/design. Later changes, linked external repositories and moving web pages are outside the evidence set.

External dependencies include model providers reached through LiteLLM, document/OCR engines, NetworkX, optional embedding/clustering packages, and browser/rendering libraries (SRC-1, `pyproject.toml`, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/ingest/reader.py`, `src/sift_kg/visualize.py`). Their internals and service operation are not frozen here; the analysis can explain sift-kg's integration code but cannot establish provider reliability, OCR accuracy or embedding quality. User corpora and custom schemas outside this commit are also absent, preventing general accuracy and workload-cost conclusions.

The external agent runtime and its response generation remain outside the target; the shipped skill and retrieval interfaces are inside. Therefore this run can establish the prescribed memory-consumption route, not actual cross-session agent compliance or improved answers. Civic Table is a separately described downstream platform, not a shipped local caller; its analyst/legal verification responsibilities are not attributed to sift-kg (SRC-1, `README.md`). No target code, tests, examples, models or services were executed. There is no inspected execution trace or causal experiment, so operational success and causal benefit remain unestablished. Available but uninspected source files are inspection limits, not access gaps, and remain available at the same registered commit.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/juanceresa/sift-kg` | d786991c024f5401f113fc0cb70aee96dd1bd3bf | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-sift-kg/related-systems/juanceresa--sift-kg`. Implementation: tracked tree; full `pyproject.toml`, `src/sift_kg/__init__.py`, `src/sift_kg/__main__.py`, `src/sift_kg/pipeline.py`; bounded `src/sift_kg/cli.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/resolve/reviewer.py`, `tests/test_cli_json.py`; symbol/call-site scans across graph, domains, ingest, resolve, prompts, model client, narrative generator, export, visualization, viewer and tests. Doctrine/design: full `README.md` and `.agents/skills/sift-kg/SKILL.md`; example README and demo/workflow path scans. | Implementation: [entry point](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/pyproject.toml), [pipeline](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/pipeline.py), [CLI consumers](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py), [extraction persistence](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py). Doctrine/design: [README](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/README.md), [agent skill](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md). | No repository access gap identified. External service internals, host sessions and independent execution/experiment evidence are absent: no conclusion about deployed reliability, actual agent uptake, benchmark accuracy or causal benefit. Initial scans are not exhaustive algorithm verification; example artifact contents are not yet inspected. |
