---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "sift-kg's shipped document-to-graph pipeline and agent-facing memory interface at commit d786991c024f5401f113fc0cb70aee96dd1bd3bf."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/juanceresa/sift-kg
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c/related-systems/juanceresa--sift-kg
  revision: d786991c024f5401f113fc0cb70aee96dd1bd3bf
  sha256: null
---

# sift-kg boundary

## Boundary and evidence

This run analyses sift-kg as a document-derived knowledge system that exposes retained graph state to people and agents. The intended use is to explain how its shipped pipeline produces, maintains, admits and later consumes that state, including the instructions for using it across agent sessions. The target is in scope because its extraction, schema discovery, resolution and narration paths issue model calls, and its bundled skill explicitly serves later agent use. It is not classified as an enclosing agent runtime. These classifications rest on SRC-1, `src/sift_kg/pipeline.py`, `src/sift_kg/extract/extractor.py`, `src/sift_kg/cli.py` and `.agents/skills/sift-kg/SKILL.md`.

> The knowledge graph is your persistent, structured memory of the user's world — entities, relationships, communities, and how they all connect. It is built from the user's documents and persists across sessions.
> --- `.agents/skills/sift-kg/SKILL.md`

The boundary is **whole-system**, not just the library API. Both the `sift` CLI and `python -m sift_kg` enter the shipped CLI application. The separate library pipeline also belongs to the target; it does not stand in for the CLI's additional review, search, information, topology and query paths. The boundary includes document ingestion and OCR adapters; configuration and domain instructions; schema discovery and extraction caches; graph construction, normalization and communities; merge proposals, review and application; narrative and description generation; graph reload and agent-facing retrieval; and browser/export consumption. SRC-1: `pyproject.toml`, `src/sift_kg/__main__.py`, `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py`.

The initial trace follows the shipped entry point into extraction and persisted per-document results, then graph build and save, proposal/review files and graph mutation, narration, and later graph loading by query/topology/search. The agent skill's session-start and rebuild procedures are included as doctrine, not treated as proof that an agent actually follows them. The library's convenience pipeline does not include the entire maintenance loop:

> Skips resolve/apply-merges (those require human review).
> --- `src/sift_kg/pipeline.py`

The CLI review surface is included independently of that description. In particular, its configurable auto-approval and auto-rejection options must be inspected before treating admission as necessarily manual. SRC-1: `src/sift_kg/cli.py`, `src/sift_kg/resolve/reviewer.py`.

Persistence and later consumption are executable responsibilities inside this boundary, not delegated to an excluded application. Extraction writes per-document JSON; build saves `graph_data.json` and community assignments; merge application can save the changed graph; query and topology reload saved state. SRC-1: `src/sift_kg/extract/extractor.py`, `src/sift_kg/pipeline.py`, `src/sift_kg/cli.py`.

> kg = KnowledgeGraph.load(graph_path)
> clean = strip_metadata(kg)
> --- `src/sift_kg/cli.py:1230-1231`

### Tracked top-level coverage

Every top-level tracked entry at the frozen commit is classified below. “Included” defines functional coverage, not a claim that every byte has already been read. Initial inspection comprises the entry-point and state-flow reads above plus path, function and persistence searches across the implementation and tests. Detailed bodies, prompts and example artifacts not yet read remain available under SRC-1; they are not access gaps or deliberate exclusions.

| Top-level entry | Coverage | Material paths and role | Initial inspection and limit |
|---|---|---|---|
| `.agents/` | Included | `.agents/skills/sift-kg/SKILL.md`: session orientation, graph retrieval, reasoning patterns, rebuild and maintenance instructions for agents | Entire skill inspected as doctrine; actual host-agent compliance is not observed. |
| `.env.example` | Included | Provider-key, model and output-directory configuration template | Configuration entries inspected; credentials and deployed settings are not supplied. |
| `.github/` | Included | `.github/workflows/ci.yml`: lint/test evaluator; `.github/workflows/pages.yml`: copies retained demo outputs into the static site | CI commands searched and Pages workflow read; neither workflow was executed and no CI run result is supplied. |
| `.gitignore` | Excluded from operational analysis | Repository hygiene and ignored local state | Inventoried and headings searched. Exclusion prevents claims about completeness of untracked developer/runtime files, not analysis of shipped state paths. |
| `LICENSE` | Excluded from operational analysis | Legal terms | Inventoried; no licensing interpretation is made. |
| `README.md` | Included | User workflow, agent knowledge-base positioning, configuration and external integration claims | Opening workflow, AI knowledge-base section, domain description and installation/configuration inspected; remaining command reference is available for later inspection. Marketing claims are not measured outcomes. |
| `examples/` | Included | `ftx/docs/`, `ftx/output/extractions/`, `ftx/output/graph_data.json`, `ftx/output/merge_proposals.yaml`, and all three examples' community, description, narrative and viewer outputs; `transformers/sift.yaml`, `ontoverse_az/sift.yaml` and example READMEs | Entire tracked inventory checked; FTX README read and all example README headings searched. Artifact contents and other example configurations are not yet inspected. These are supplied demonstrations and reported statistics, not a reproduced benchmark or a complete execution trace. |
| `pages/` | Included | `pages/index.html`: links to static example viewers | Title and demo links inspected; live deployment is outside the frozen evidence. |
| `pyproject.toml` | Included | Packaging, `sift` entry point, dependency and optional backend declarations, pytest/lint configuration | Entire file inspected. Metadata's `civictable` URLs do not replace the supplied source identity or authorize another repository. |
| `src/` | Included | `src/sift_kg/cli.py`, `__main__.py`, `pipeline.py`: shipped drivers; `config.py`, `domains/` including bundled YAML and discovery: configuration and prompts; `ingest/`: documents/OCR/chunks; `extract/`: prompts, model adapter, extraction/cache; `graph/`: build, save/reload, pre-dedup, postprocessing and communities; `resolve/`: models, proposal IO, resolution, reviewer and application; `narrate/`: prompts and persisted derived prose/descriptions; `export.py`, `visualize.py`, `viewer/`: downstream exports and browser consumption | Entire library pipeline and module entry point read; CLI extraction, review/application, search setup, topology and query traced; extraction cache/write and narration generation traced. Function and persistence searches cover remaining modules; extraction prompt opening, domain instruction markers, visualization sidecar/template loading and viewer description rendering inspected. Remaining bodies are available, not unavailable evidence. |
| `tests/` | Included | `test_cli_json.py`, `test_communities.py`: saved-state retrieval and topology; `test_review.py`, `test_resolve.py`: admission/mutation; `test_graph.py`, `test_prededup.py`: graph maintenance; `test_domains.py`, `test_extract.py`, `test_llm_client.py`, `test_ingest.py`, `test_config.py`: production/configuration; `test_narrate.py`, `test_export.py`, `test_view_filters.py`: derived output consumers; `conftest.py`: fixtures | All test classes/functions inventoried; opening CLI JSON tests inspected, including fixture graph save and CLI reload. Test source supports intended assertions, not a claim of passing tests or extraction quality. Remaining test bodies and fixtures are not yet inspected. |

### Dependencies, exclusions and time limit

External dependencies include LiteLLM and its selected model provider, NetworkX, document extraction libraries, optional local/cloud OCR, optional embedding models, and PyVis/browser rendering. Their declared interfaces and sift-kg adapters are in scope; their independent implementations, service behavior and operational guarantees are not frozen here. Consequently this run cannot establish provider reliability, model accuracy, OCR quality, actual costs or end-to-end privacy from this checkout alone. SRC-1: `pyproject.toml`, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/ingest/reader.py`, `src/sift_kg/visualize.py`.

The host agent's scheduling, context assembly, session persistence and response generation are outside the target. Only the shipped skill and retrieval interface are included; this prevents attributing reliable cross-session agent behavior to sift-kg alone. The separately linked Civic Table platform is also outside the frozen repository; its verification and hosted-application responsibilities are not attributed to this target. SRC-1: `.agents/skills/sift-kg/SKILL.md`, `README.md`.

Evidence is frozen at commit `d786991c024f5401f113fc0cb70aee96dd1bd3bf`, checked against checkout HEAD. The applicability cutoff is 2026-10-15, the opening run date; it is not a claim about the commit's author date or the current upstream release. Overall evidence tier is **code-grounded**. No target code, tests, examples, model calls or external services were executed. No separate trace or causal experiment was supplied. Available but unread source is an inspection obligation for later claims, not an access failure. The boundary supports a source-level account of the whole shipped loop, not observed performance or causal effectiveness.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/juanceresa/sift-kg` | d786991c024f5401f113fc0cb70aee96dd1bd3bf | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sift-kg-dca68bc45a2c/related-systems/juanceresa--sift-kg`. Implementation: tracked tree, entry points, entire library pipeline, selected CLI production/maintenance/retrieval bodies, extraction cache/write path, narrative generation, implementation-wide function/persistence searches and test inventory with selected CLI test bodies. Doctrine/design: bundled skill, README opening workflow and AI knowledge-base/domain/configuration sections, extraction prompt opening, bundled-domain instruction markers, package and deployment configuration. Reported operation: FTX example README statistics; other example headings inventoried. Remaining registered paths may be inspected at this same commit. | Implementation: [CLI](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/cli.py), [pipeline](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/pipeline.py), [extraction](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/extract/extractor.py), [narration](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/src/sift_kg/narrate/generator.py), [CLI tests](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/tests/test_cli_json.py). Doctrine/design: [skill](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/.agents/skills/sift-kg/SKILL.md), [README](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/README.md), [package](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/pyproject.toml). Reported operation: [FTX example](https://github.com/juanceresa/sift-kg/blob/d786991c024f5401f113fc0cb70aee96dd1bd3bf/examples/ftx/README.md). | No repository access gap encountered. External host-agent implementation, provider/dependency internals, live deployments and private inputs are not in this source. No supplied full execution trace, test-run result or intervention/comparison supports observed reliability, extraction accuracy, real session reuse or causal effectiveness. Example statistics remain attributed reports. |
