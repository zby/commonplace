---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM-Wiki-v3's shipped memory-system loop at commit 267541db838cbca757a112bd0cfa47fa61eb5fb2, including ingestion, curated admission, retained pages, retrieval and evaluation."
run-id: AAS-2026-10-18-llm-wiki-v3-0c553a3118eb-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/vvvvvivekkk/LLM-Wiki-v3
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-llm-wiki-v3-retry-1/related-systems/vvvvvivekkk--LLM-Wiki-v3
  revision: "267541db838cbca757a112bd0cfa47fa61eb5fb2"
  sha256: null
---

# LLM-Wiki-v3 boundary

## Boundary and evidence

LLM-Wiki-v3 is in scope as a memory/knowledge/context-engineering system. Its intended use is a domain-configurable Markdown knowledge store for human browsing and agent context retrieval. The frozen implementation issues model calls to extract proposed pages and supplies retrieval results from retained pages; it is not an enclosing general-purpose agent runtime. The boundary is the whole shipped repository system, including its operator CLI and curated seed driver, not only the extraction or retrieval APIs (SRC-1, `README.md`, `src/wiki/cli/__init__.py`, `scripts/seed_corpus.py`).

> It serves two readers from one store:
>
> 1. **Humans** — browsing in Obsidian, a CLI, or any markdown viewer.
> 2. **LLM agents** — retrieving context via an MCP server.
> --- `README.md`

That passage establishes intent, not a shipped MCP service. The reviewed tree and CLI implement ingestion, review, rebuild, query and evaluation beyond the README's Phase 0 status. The Makefile still labels several later surfaces as stubs. This analysis distinguishes those declarations from executable paths rather than treating either status text as a complete implementation inventory (SRC-1, `README.md`, `Makefile`, `src/wiki/cli/__init__.py`).

The included state loop is source-byte retention → chunk extraction using the root ingest instructions → quote location and validation → pending proposals and manifests → interactive curated admission or rejection → namespace Markdown pages → index rebuilding and subsequent query/evaluator consumption. Ingestion can escalate between extractors after validation failure. The separate curated seed driver directly constructs, validates and writes retained pages and stores raw sources; it is part of the target, not an excluded caller. Evaluation includes retrieval adapters, saved baselines, source-span-based ingest metrics and model-generated candidate queries for human review (SRC-1, `src/wiki/ingest/pipeline.py`, `src/wiki/extract.py`, `AGENTS.md`, `src/wiki/review.py`, `scripts/seed_corpus.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/query.py`, `src/wiki/eval/harness.py`, `src/wiki/eval/ingest_eval.py`, `src/wiki/cli/__init__.py`).

> def _system_prompt(root: Path) -> str:
>     agents = root / "AGENTS.md"
>     return agents.read_text(encoding="utf-8") if agents.is_file() else ""
> --- `src/wiki/ingest/pipeline.py`

>         system=context,
>         tools=[PROPOSE_TOOL],
>         tool_choice={"type": "tool", "name": "propose_pages"},
> --- `src/wiki/extract.py`

>     dest = _dest_for(root, page_path)
>     dest.parent.mkdir(parents=True, exist_ok=True)
>     page_path.replace(dest)
> --- `src/wiki/review.py`

> def load_pages(root: Path, include_superseded: bool = False) -> list[PageRecord]:
> --- `src/wiki/retrieve/store.py`

These passages anchor the classification and boundary: shipped instructions enter a model call, proposals have a retained-state admission path, and a later loader consumes the retained store. They do not establish that every prose policy is enforced or that the interactive review revalidates edited proposals.

### Top-level tracked coverage

Every top-level tracked entry is included below. “Inspected” describes initial boundary work, not an assertion that every included file has been read. Uninspected implementation details remain available at the same pin for later analysis; they are not access gaps or exclusions. Paths in every row refer to SRC-1.

| Top-level entry | Disposition and material paths | Role and initial inspection; limits |
| --- | --- | --- |
| `.gitignore` | Included; `.gitignore` | Inspected retention exclusions for derived indexes and raw bodies. Explains why the Git snapshot does not supply stored raw documents. |
| `AGENTS.md` | Included; `AGENTS.md` | Inspected complete ingest-model instructions, provenance rules and proposed maintenance behavior; traced its consumer in `src/wiki/ingest/pipeline.py`. These are target doctrine, not instructions governing this analysis. |
| `Makefile` | Included; `Makefile` | Inspected installation, validation, test and hook wrappers, evaluation driver and later-phase stub targets. |
| `README.md` | Included; `README.md` | Inspected intended use, store layout, principles and roadmap; status is not treated as an executable inventory. |
| `audit/` | Included; `audit/log.jsonl` | Tracked operation-log location; line-count inspection found an empty file. Audit call sites inspected in ingestion and review; `src/wiki/audit.py` function surface searched, not fully audited. No operation history is established. |
| `evals/` | Included; `evals/datasets/queries.jsonl`, `evals/baselines/baseline.json`, `evals/baselines/baseline-20260529T144104Z.md`, `evals/baselines/components.json`, `evals/runners/.gitkeep` | Dataset and saved-output inventory inspected; baseline Markdown read, JSON payloads not fully inspected. Evaluator and CLI consumers traced. Saved outputs are source-authored reports, not executions observed in this analysis or evidence that today's dataset reproduces the older report. |
| `knowledge/` | Included; `knowledge/_index.md`, `knowledge/entities/*.md`, `knowledge/concepts/*.md`, `knowledge/sources/.gitkeep`, `knowledge/notes/.gitkeep` | Tracked retained corpus and browsing catalog. Catalog and `knowledge/entities/ada-lovelace.md` inspected; remaining page bodies not individually read. Persistence traced through review and seed driver; reload/consumption through `src/wiki/retrieve/store.py`, rebuild, query and evaluation. |
| `pending/` | Included; `pending/.gitkeep` | Staging area has only a tracked placeholder. Producer, manifests and interactive accept/reject consumer inspected in ingestion and review/CLI; no frozen pending proposal history. |
| `pyproject.toml` | Included; `pyproject.toml` | Inspected console entry point, package/dependency and optional dense-model declarations. |
| `raw/` | Included; `raw/.gitkeep` | Raw-store responsibility included; content-addressed writer/reader inspected in `src/wiki/ingest/hashing.py` and curated seed driver. Actual retained raw bodies are unavailable in the tracked snapshot, preventing independent provenance replay against those stored bytes. Seed source text is available in `scripts/seed_corpus.py`, but was not executed or substituted for missing artifacts. |
| `schema/` | Included; `schema/CURRENT`, `schema/namespaces.yaml`, `schema/v1/README.md`, `schema/v1/_base.schema.yaml`, `schema/v1/{concept,entity,note,source}.schema.yaml` | Registry and narrative inspected; loader and validator read to trace namespace admission and reload. Individual schema bodies not yet inspected. Versioned contracts and validation are included, not presumed complete from documentation. |
| `scripts/` | Included; `scripts/seed_corpus.py`, `scripts/pre-commit` | Both read completely. Seed driver is an additional retained-state producer; hook validates staged namespace pages. Neither was executed. |
| `src/` | Included; `src/wiki/cli/{__init__,__main__}.py`, `src/wiki/{extract,review,validate,schema_loader,frontmatter,audit,config}.py`, `src/wiki/ingest/`, `src/wiki/retrieve/`, `src/wiki/eval/` | Entry points, extraction, ingestion pipeline, raw store, review, schema loader/validator, page reload, rebuild, query and retrieval/ingest evaluator paths read. Component function surfaces searched for BM25, dense, graph and rerank; supporting modules and component internals remain for later inspection. All shipped responsibilities remain inside the boundary. |
| `tests/` | Included; `tests/test_pipeline.py`, `tests/test_retrieve.py`, `tests/test_validate.py`, `tests/test_harness.py`, `tests/test_baseline_retriever.py`, other `tests/test_*.py`, `tests/fixtures/{good,bad}/` | Test/import surfaces searched and fixture inventory inspected for the ingestion/review, reload/retrieval, validation and evaluation consumers. Test bodies not fully read and no tests run; this supplies coverage leads, not passing-test or runtime evidence. |

### Dependencies, exclusions and evidence limits

The applicability cutoff is 2026-10-18; the sole evidence revision is `267541db838cbca757a112bd0cfa47fa61eb5fb2`. No moving branch, later revision, external document or additional repository is admitted. HEAD matched that pin and the checkout was clean at inspection. The overall tier is code-grounded: implementation is available for the shipped loop, supplemented by doctrine and source-authored reports. No target code, tests, examples, model call or evaluation was executed.

External dependencies include Anthropic's client/service for extraction and candidate-query generation, Python parsing/validation libraries, Git for optional review commits and an optional editor for interactive review. Optional local dense retrieval/reranking dependencies are declared separately. Their external implementation, model weights and live responses are excluded; this prevents conclusions about provider reliability, model truthfulness, downloaded-model behavior or deployment performance. The target's dependency declarations and integration call sites remain included (SRC-1, `pyproject.toml`, `src/wiki/extract.py`, `src/wiki/cli/__init__.py`, `src/wiki/review.py`).

Human judgment and any downstream agent's reasoning after retrieval are outside this implementation boundary. The included CLI owns its interaction and returned retrieval fields, not an unprovided consumer's prompt construction, answer generation or long-term agent outcome. MCP, context compilation and autonomous admission are mentioned as later phases; they are not silently supplied by an imagined host. This prevents treating the intended agent-facing service or autonomous write loop as established shipped behavior (SRC-1, `README.md`, `Makefile`, `src/wiki/cli/__init__.py`).

The tracked raw-store placeholder, ignored raw bodies, absent derived indexes and empty audit log prevent reproduction of stored-source lineage, inspection of an actual index build or reconstruction of an ingestion/admission run from this checkout alone. These are artifact gaps, not missing implementation paths. The frozen baseline report remains attributed reported operation, not a causal experiment or an independently observed run (SRC-1, `.gitignore`, `raw/.gitkeep`, `audit/log.jsonl`, `evals/baselines/baseline-20260529T144104Z.md`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/vvvvvivekkk/LLM-Wiki-v3` | 267541db838cbca757a112bd0cfa47fa61eb5fb2 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-llm-wiki-v3-retry-1/related-systems/vvvvvivekkk--LLM-Wiki-v3`. Implementation: tree inventory; `pyproject.toml`, `Makefile`, `scripts/pre-commit`, `scripts/seed_corpus.py`, `src/wiki/cli/__init__.py`, `src/wiki/cli/__main__.py`, `src/wiki/extract.py`, `src/wiki/ingest/pipeline.py`, `src/wiki/ingest/hashing.py`, `src/wiki/review.py`, `src/wiki/schema_loader.py`, `src/wiki/validate.py`, `src/wiki/retrieve/store.py`, `src/wiki/retrieve/rebuild.py`, `src/wiki/retrieve/query.py`, `src/wiki/eval/harness.py`, `src/wiki/eval/ingest_eval.py`; component and test surfaces searched. Doctrine/design: `README.md`, `AGENTS.md`, `schema/v1/README.md`, `schema/namespaces.yaml`, `.gitignore`, `knowledge/_index.md`. Retained-state sample: `knowledge/entities/ada-lovelace.md`. Reported operation: `evals/baselines/baseline-20260529T144104Z.md`; audit log checked empty. | Implementation: [CLI](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/cli/__init__.py), [pipeline](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/ingest/pipeline.py), [seed driver](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/scripts/seed_corpus.py), [reload](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/src/wiki/retrieve/store.py). Doctrine/design: [ingest instructions](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/AGENTS.md), [README](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/README.md). Reported operation: [baseline](https://github.com/vvvvvivekkk/LLM-Wiki-v3/blob/267541db838cbca757a112bd0cfa47fa61eb5fb2/evals/baselines/baseline-20260529T144104Z.md). | No repository access gap. Stored raw bodies, derived indexes and nonempty operation traces are not supplied by this Git snapshot; no execution observed. Implementation inspection supports code-path claims, not actual model fidelity, reproduced baseline metrics, deployed agent integration or causal improvements. Files not initially read remain available within this source identity and revision. |
